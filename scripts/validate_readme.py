#!/usr/bin/env python3
"""Dependency-free validator for the Awesome CS Courses README."""

import argparse
from dataclasses import dataclass
import re
import sys
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class Link:
    label: str
    url: str
    line: int


USER_AGENT = "Awesome-CS-Courses-Validator/1.0 (+local README checks)"
DEFAULT_TIMEOUT = 5
ALLOWED_STATUSES = {"Intro", "Core", "Advanced", "Archived"}
FORBIDDEN_HEADINGS = {
    "CS-Awesome-Courses",
    "Free Programming Courses",
    "University Courses Collection",
}
FINAL_SECTION = "Texts and Companion Resources"
CONTENTS_SECTION = "Contents"
REQUIRED_SECTIONS = [
    "Foundations and Programming",
    "Mathematics for Computer Science",
    "Data Structures and Algorithms",
    "Computer Architecture and Systems",
    "Operating Systems",
    "Computer Networks and Distributed Systems",
    "Databases and Data Management",
    "Programming Languages and Compilers",
    "Theory of Computation",
    "Security and Cryptography",
    "Artificial Intelligence, Machine Learning, and NLP",
    "Computer Vision, Graphics, HCI, and Robotics",
    "Data Science, Parallel Computing, and Web Development",
    FINAL_SECTION,
]
COURSE_SECTIONS = set(REQUIRED_SECTIONS)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<text>.+?)\s*$")
LIST_HEADING_RE = re.compile(r"^\s*[-*+]\s+#{1,6}\s+\S")
COURSE_TAIL_RE = re.compile(r"^(?P<institution>.+?)\s+\((?P<status>[^()]+)\)\.\s+(?P<description>.+)$")
CONTENTS_ENTRY_RE = re.compile(r"^\s*-\s+\[(?P<label>[^\]]+)\]\((?P<target>#[^)]+)\)\s*$")

_REQUEST_TIMEOUT = DEFAULT_TIMEOUT


def parse_links(text: str) -> list[Link]:
    links, _ = _scan_links(text, report_errors=False)
    return links


def normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/")
    return urlunsplit((parts.scheme, parts.netloc.lower(), path, parts.query, ""))


def validate(path, check_links: bool = False) -> int:
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except OSError as exc:
        print(f"Line 1: could not read {path}: {exc}")
        return 1
    return _validate_text(text, check_links=check_links)


def _validate_text(text: str, check_links: bool = False) -> int:
    errors, link_count, course_count = _collect_issues(text, check_links)
    print(f"Links: {link_count}")
    print(f"Course bullets: {course_count}")
    if errors:
        for line_no, message in errors:
            print(f"Line {line_no}: {message}")
        print(f"Validation failed: {len(errors)} problem(s)")
        return 1
    print("Validation passed")
    return 0


def _collect_issues(text: str, check_links: bool) -> tuple[list[tuple[int, str]], int, int]:
    errors: list[tuple[int, str]] = []
    headings: dict[str, int] = {}
    h1_lines: list[int] = []
    current_section = ""
    section_labels: dict[str, dict[str, int]] = {section: {} for section in COURSE_SECTIONS}
    normalized_urls: dict[str, int] = {}
    course_count = 0
    contents_heading_line: int | None = None
    contents_entries: list[tuple[int, str, str]] = []
    in_contents = False

    links, link_errors = _scan_links(text, report_errors=True)
    errors.extend(link_errors)

    in_fence = False
    fence_marker = ""
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group("marks"))
            text_value = heading_match.group("text").strip()
            if level == 1:
                h1_lines.append(line_no)
            elif level == 2:
                if text_value == CONTENTS_SECTION:
                    if contents_heading_line is None:
                        contents_heading_line = line_no
                    else:
                        errors.append((line_no, "duplicate Contents heading"))
                    in_contents = True
                else:
                    in_contents = False
                current_section = text_value
                if text_value in REQUIRED_SECTIONS and text_value not in headings:
                    headings[text_value] = line_no
            elif in_contents:
                errors.append((line_no, "malformed Contents entry"))
            if text_value in FORBIDDEN_HEADINGS:
                errors.append((line_no, f"forbidden imported heading: {text_value}"))
            continue

        if in_contents:
            if not line.strip():
                continue
            contents_match = CONTENTS_ENTRY_RE.match(line)
            if contents_match is None:
                errors.append((line_no, "malformed Contents entry"))
                continue
            contents_entries.append(
                (
                    line_no,
                    contents_match.group("label").strip(),
                    contents_match.group("target").strip(),
                )
            )
            continue

        if LIST_HEADING_RE.match(line):
            errors.append((line_no, "list item contains a heading"))
            continue

        if current_section not in COURSE_SECTIONS:
            continue

        if re.match(r"^\s*-\s+\S", line):
            course_count += 1
            bullet = _parse_course_bullet(line)
            if bullet is None:
                errors.append((line_no, f"malformed course bullet in {current_section}"))
                continue

            label = bullet["label"].strip()
            url = bullet["url"].strip()
            institution = bullet["institution"].strip()
            status = bullet["status"].strip()
            if status not in ALLOWED_STATUSES:
                errors.append((line_no, f"invalid course status: {status}"))
            if current_section != FINAL_SECTION and institution in {"Text", "Project"}:
                errors.append((line_no, f"text/project entries belong only in {FINAL_SECTION}"))
            if not url:
                errors.append((line_no, "empty external URL"))
                continue

            if not _is_external_url(url):
                errors.append((line_no, f"malformed external URL: {url}"))
                continue

            normalized_url = normalize_url(url)
            if normalized_url in normalized_urls:
                errors.append(
                    (
                        line_no,
                        f"duplicate normalized course URL (also line {normalized_urls[normalized_url]})",
                    )
                )
            else:
                normalized_urls[normalized_url] = line_no

            normalized_label = _normalize_label(label)
            section_seen = section_labels[current_section]
            if normalized_label in section_seen:
                errors.append(
                    (
                        line_no,
                        f"duplicate normalized course label in section {current_section} (also line {section_seen[normalized_label]})",
                    )
                )
            else:
                section_seen[normalized_label] = line_no

    if not h1_lines:
        errors.append((1, "missing top-level H1 heading"))
    elif len(h1_lines) > 1:
        for extra_line in h1_lines[1:]:
            errors.append((extra_line, "multiple H1 headings"))

    if contents_heading_line is None:
        errors.append((1, "missing required taxonomy heading: ## Contents"))
    else:
        errors.extend(_validate_contents_entries(contents_heading_line, contents_entries))

    for section in REQUIRED_SECTIONS:
        if section not in headings:
            errors.append((1, f"missing required taxonomy heading: ## {section}"))

    for link in links:
        if not _is_external_url(link.url):
            errors.append((link.line, f"malformed external URL: {link.url}"))

    if check_links:
        errors.extend(_check_links(links))

    return errors, len(links), course_count


def _normalize_label(label: str) -> str:
    return re.sub(r"\s+", " ", label).strip().casefold()


def _normalize_contents_target(label: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", label.casefold()).strip("-")
    return f"#{slug}"


def _is_external_url(url: str) -> bool:
    parts = urlsplit(url)
    return parts.scheme in {"http", "https"} and bool(parts.netloc)


def _validate_contents_entries(
    contents_heading_line: int, contents_entries: list[tuple[int, str, str]]
) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    seen_labels: dict[str, int] = {}
    seen_targets: dict[str, int] = {}

    for index, expected_label in enumerate(REQUIRED_SECTIONS, 1):
        expected_target = _normalize_contents_target(expected_label)
        if index > len(contents_entries):
            errors.append(
                (
                    contents_heading_line,
                    f"missing Contents entry {index}: expected [{expected_label}]({expected_target})",
                )
            )
            continue

        line_no, actual_label, actual_target = contents_entries[index - 1]
        if actual_label != expected_label or actual_target != expected_target:
            if actual_label != expected_label and actual_target != expected_target:
                message = (
                    f"wrong Contents entry {index}: expected [{expected_label}]({expected_target}), "
                    f"got [{actual_label}]({actual_target})"
                )
            elif actual_label != expected_label:
                message = (
                    f"wrong Contents label {index}: expected {expected_label}, got {actual_label}"
                )
            else:
                message = (
                    f"wrong Contents anchor {index}: expected {expected_target}, got {actual_target}"
                )
            errors.append((line_no, message))

        previous_label_line = seen_labels.get(actual_label)
        if previous_label_line is not None:
            errors.append(
                (
                    line_no,
                    f"duplicate Contents label: {actual_label} (also line {previous_label_line})",
                )
            )
        else:
            seen_labels[actual_label] = line_no

        previous_target_line = seen_targets.get(actual_target)
        if previous_target_line is not None:
            errors.append(
                (
                    line_no,
                    f"duplicate Contents anchor: {actual_target} (also line {previous_target_line})",
                )
            )
        else:
            seen_targets[actual_target] = line_no

    for extra_line_no, actual_label, actual_target in contents_entries[len(REQUIRED_SECTIONS) :]:
        errors.append(
            (
                extra_line_no,
                f"unexpected Contents entry: [{actual_label}]({actual_target})",
            )
        )

    return errors


def _scan_links(text: str, report_errors: bool) -> tuple[list[Link], list[tuple[int, str]]]:
    links: list[Link] = []
    errors: list[tuple[int, str]] = []
    in_fence = False
    fence_marker = ""

    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if in_fence:
            continue

        index = 0
        while index < len(line):
            open_bracket = line.find("[", index)
            if open_bracket == -1:
                break
            is_image = open_bracket > 0 and line[open_bracket - 1] == "!"
            label_end = line.find("]", open_bracket + 1)
            if label_end == -1:
                if report_errors and not is_image and _looks_like_unclosed_link(line, open_bracket):
                    errors.append((line_no, "malformed or unclosed markdown link"))
                index = open_bracket + 1
                continue
            if label_end + 1 >= len(line) or line[label_end + 1] != "(":
                index = label_end + 1
                continue
            url, end_index = _parse_link_destination(line, label_end + 2)
            if end_index is None:
                if report_errors and not is_image:
                    errors.append((line_no, "malformed or unclosed markdown link"))
                index = label_end + 1
                continue
            if not is_image:
                url = url.strip()
                if not url.startswith("#"):
                    label = line[open_bracket + 1 : label_end]
                    links.append(Link(label, url, line_no))
            index = end_index

    return links, errors


def _looks_like_unclosed_link(line: str, open_bracket: int) -> bool:
    return "(" in line[open_bracket + 1 :]


def _parse_link_destination(line: str, start_index: int) -> tuple[str, int | None]:
    depth = 1
    index = start_index
    while index < len(line):
        char = line[index]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return line[start_index:index], index + 1
        index += 1
    return "", None


def _parse_course_bullet(line: str) -> dict[str, str] | None:
    stripped = line.lstrip()
    if not stripped.startswith("- ["):
        return None
    offset = len(line) - len(stripped)
    label_start = offset + 3
    label_end = line.find("]", label_start)
    if label_end == -1 or label_end + 1 >= len(line) or line[label_end + 1] != "(":
        return None
    url, url_end = _parse_link_destination(line, label_end + 2)
    if url_end is None:
        return None
    tail = line[url_end:].lstrip()
    if not tail.startswith("- "):
        return None
    tail_match = COURSE_TAIL_RE.match(tail[2:])
    if tail_match is None:
        return None
    return {
        "label": line[label_start:label_end],
        "url": url,
        "institution": tail_match.group("institution"),
        "status": tail_match.group("status"),
        "description": tail_match.group("description"),
    }


def _check_links(links: list[Link]) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []
    for link in links:
        error = _probe_link(link.url)
        if error is not None:
            errors.append((link.line, f"{error} ({link.url})"))
    return errors


def _probe_link(url: str) -> str | None:
    result = _request(url, "HEAD")
    if result is None:
        return None
    code, error = result
    if code is not None and 200 <= code < 400:
        return None
    if code in {403, 405}:
        retry = _request(url, "GET")
        if retry is None:
            return None
        retry_code, retry_error = retry
        if retry_code is not None and 200 <= retry_code < 400:
            return None
        return _describe_network_error(retry_error, retry_code)
    return _describe_network_error(error, code)


def _request(url: str, method: str):
    headers = {"User-Agent": USER_AGENT}
    if method == "GET":
        headers["Range"] = "bytes=0-0"
    request = Request(url, headers=headers, method=method)
    try:
        with urlopen(request, timeout=_REQUEST_TIMEOUT) as response:
            return response.getcode(), None
    except Exception as exc:  # urllib raises a family of request/HTTP errors here
        code = getattr(exc, "code", None)
        return code, exc


def _describe_network_error(error: Exception | None, code: int | None) -> str:
    if code is not None:
        return f"HTTP {code}"
    if error is None:
        return "network error"
    reason = getattr(error, "reason", error)
    reason_text = str(reason)
    reason_name = type(reason).__name__.lower()
    text = reason_text.lower()
    if "timeout" in reason_name or "timed out" in text:
        return "timeout"
    if "gaierror" in reason_name or "name or service not known" in text or "temporary failure" in text:
        return "DNS failure"
    return f"{type(reason).__name__}: {reason_text}"


def _build_self_test_snippet(valid: bool) -> str:
    sections: list[str] = ["# Sample README", "", "Intro text.", "", "## Contents", ""]
    for index, section in enumerate(REQUIRED_SECTIONS, 1):
        target = _normalize_contents_target(section)
        if not valid and index == 1:
            sections.append("- [Foundations and Programming](#foundations-and-programming-wrong)")
        else:
            sections.append(f"- [{section}]({target})")
    sections.append("")
    for index, section in enumerate(REQUIRED_SECTIONS[:-1], 1):
        sections.append(f"## {section}")
        if valid and index == 1:
            sections.append(
                "- [Balanced Link](https://example.com/a(b)/c) - Example University (Core). Example description."
            )
            continue
        if not valid and index == 1:
            sections.append(
                "- [Balanced Link](https://example.com/a(b)/c) - Example University (Draft). Example description."
            )
            continue
        institution = "Example University"
        if not valid and index == 2:
            institution = "Text"
        sections.append(
            f"- [{section}](https://example.com/{index}) - {institution} (Core). Example description."
        )

    sections.append(f"## {FINAL_SECTION}")
    sections.append("- [Example Text](https://example.com/book(a)/index) - Text (Core). Example text.")
    sections.append("- [Example Project](https://example.com/project) - Project (Advanced). Example project.")

    if not valid:
        sections.extend(
            [
                "",
                "Broken link: [oops](https://example.com/a(b)",
            ]
        )

    sections.append("")
    return "\n".join(sections)


def _self_test() -> int:
    valid_text = _build_self_test_snippet(True)
    invalid_text = _build_self_test_snippet(False)
    if not any(link.url == "https://example.com/a(b)/c" for link in parse_links(valid_text)):
        print("Self-test failed")
        return 1
    invalid_errors, _, _ = _collect_issues(invalid_text, False)
    if not any("malformed or unclosed markdown link" in message for _, message in invalid_errors):
        print("Self-test failed")
        return 1
    valid_result = _validate_text(valid_text, check_links=False)
    invalid_result = _validate_text(invalid_text, check_links=False)
    if valid_result == 0 and invalid_result != 0:
        print("Self-test passed")
        return 0
    print("Self-test failed")
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("readme", nargs="?", default="README.md")
    parser.add_argument("--check-links", action="store_true")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    global _REQUEST_TIMEOUT
    _REQUEST_TIMEOUT = args.timeout

    if args.self_test:
        return _self_test()
    return validate(args.readme, check_links=args.check_links)


if __name__ == "__main__":
    sys.exit(main())
