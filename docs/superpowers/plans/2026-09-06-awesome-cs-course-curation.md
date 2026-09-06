# Awesome CS Courses Curation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the stitched course catalog with a verified, subject-first Awesome CS Courses repository that is easy to maintain.

**Architecture:** Keep one canonical Markdown catalog in `README.md`; put provenance and curriculum analysis in `docs/`; enforce the entry contract with a dependency-free Python validator and a deterministic GitHub Actions job. External link checks are an explicit local command, not a CI requirement.

**Tech Stack:** Markdown, Python 3 standard library (`argparse`, `re`, `urllib`), GitHub Actions, CC0 1.0 text.

**Spec:** `docs/superpowers/specs/2026-09-06-awesome-cs-course-curation-design.md`

## Global Constraints

- Prefer official university course pages, official repositories, and first-party open-course platforms.
- Use one canonical entry per course; label a distinct historical offering `Archived`.
- Keep descriptions to one factual sentence and avoid rankings, marketing copy, and unverifiable claims.
- Do not retain empty links, malformed Markdown, random playlists, SEO aggregators, or out-of-scope commercial material in the main catalog.
- Apply the repository license only to original curation text; linked course materials retain their own licenses.
- Keep CI deterministic; network link checks remain opt-in.

---

### Task 1: Capture first-party evidence for additions and repairs

**Files:**
- Create: `docs/research/course-candidates.md`
- Read: `README.md`, `docs/superpowers/specs/2026-09-06-awesome-cs-course-curation-design.md`

**Interfaces:**
- Produces a table of candidate/course records consumed by Task 2. Each record has `course`, `institution`, `area`, `url`, `status`, `evidence`, and `decision` columns.

- [ ] **Step 1: Enumerate source gaps from the existing catalog**

  Compare the existing headings and canonical course names with the proposed taxonomy. Record only candidates that are missing or need a first-party replacement, including Harvard CS50x/CS50AI/CS50W, MIT 6.S081, MIT 6.5840, Stanford CS103, Berkeley CS70, Berkeley CS184, Stanford CS149, CMU 15-445 current, and UIUC CS225.

- [ ] **Step 2: Verify each candidate against a first-party page**

  For each candidate, confirm that the page is publicly reachable and exposes a syllabus plus at least two learning components (lectures, readings, assignments, labs, or projects). Capture the exact URL and a short factual evidence note; mark a candidate `Archived` when the page is a historical offering.

- [ ] **Step 3: Write the research record**

  Use this exact shape for each accepted record:

  ```markdown
  | Course | Institution | Area | Official link | Status | Evidence | Decision |
  | --- | --- | --- | --- | --- | --- | --- |
  | MIT 6.S081: Operating System Engineering | MIT | Operating Systems | https://pdos.csail.mit.edu/6.S081/ | Current | Lectures, labs, xv6 projects | Add |
  ```

  Add a `Rejected or deferred` subsection for candidates that fail the evidence or stability check, with the reason and source URL.

- [ ] **Step 4: Check the research document for unsupported claims**

  Run `rg -n "TBD|unverified|rumou?r|best|#1" docs/research/course-candidates.md` and remove any hit that is not a source-backed factual statement.

### Task 2: Write the canonical README

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: accepted records in `docs/research/course-candidates.md` and the entry contract in the spec.
- Produces: one H1, one ToC, 14 stable subject sections, and one canonical bullet per selected course.

- [ ] **Step 1: Replace the concatenated document header**

  Start `README.md` with:

  ```markdown
  # Awesome CS Courses

  A curated index of rigorous, publicly available computer science courses and companion texts. Quality over quantity: entries favor complete teaching material, stable links, and long-term learning value.

  中文说明：本目录按知识领域整理公开计算机科学课程，优先收录官方、完整、可长期访问的学习材料。
  ```

  Follow it with a `## Contents` list linking only to the 14 taxonomy headings, then a short `## How to use this list` and `## Selection criteria` section.

- [ ] **Step 2: Add the 14 canonical sections in taxonomy order**

  Use exactly these headings: `Foundations and Programming`, `Mathematics for Computer Science`, `Data Structures and Algorithms`, `Computer Architecture and Systems`, `Operating Systems`, `Computer Networks and Distributed Systems`, `Databases and Data Management`, `Programming Languages and Compilers`, `Theory of Computation`, `Security and Cryptography`, `Artificial Intelligence, Machine Learning, and NLP`, `Computer Vision, Graphics, HCI, and Robotics`, `Data Science, Parallel Computing, and Web Development`, and `Texts and Companion Resources`.

- [ ] **Step 3: Migrate and consolidate high-value existing courses**

  Keep one canonical entry for each of the existing high-value families, using stable official roots where available: Harvard CS50, MIT 6.0001/6.100L, Berkeley CS61A/61B/61C/CS70/CS162/CS184/CS188/CS189, MIT 6.006/6.046J/6.004/6.S081/6.5840/6.035/6.042J/6.858, Stanford CS103/CS109/CS143/CS144/CS149/CS155/CS221/CS229/CS231N/CS224N/CS336, CMU 15-213/15-445/15-721/15-440/18-447, Princeton COS 126/COS 226, ETH digital design, Nand2Tetris, OSTEP, and equivalent verified entries from the source list.

- [ ] **Step 4: Apply the one-line metadata contract**

  Every course bullet must follow this shape:

  ```markdown
  - [Course name](https://official.example/course) - Institution (Intro|Core|Advanced|Archived). Factual one-sentence scope statement.
  ```

  Keep supporting resource links out of the course bullet unless they are part of the same official landing page. Put standalone books and implementation tutorials in `Texts and Companion Resources` with an explicit `Text` or `Project` label.

- [ ] **Step 5: Remove or relocate non-course material**

  Remove duplicated imported ToCs, personal notes, random video-only playlists, application/entrepreneurship sections, Persian link directories, and empty targets. Preserve a high-value book or project by moving it to `Texts and Companion Resources` and state the rationale in `docs/coverage.md`.

- [ ] **Step 6: Run a local structural scan before moving on**

  Run `rg -n '^# |^## |^- \[' README.md`, `rg -n '\]\(\s*\)' README.md`, and `git diff --check`. Expected: one H1, the 14 headings plus policy headings, no empty link targets, and no whitespace errors.

### Task 3: Document coverage and contribution policy

**Files:**
- Create: `docs/coverage.md`
- Create: `CONTRIBUTING.md`

**Interfaces:**
- `docs/coverage.md` is the maintainer-facing curriculum matrix and candidate backlog.
- `CONTRIBUTING.md` is the contributor-facing acceptance contract and points to the validator command.

- [ ] **Step 1: Write the coverage matrix**

  Add a table with columns `Domain`, `Core coverage`, `Representative entries`, `Gap or maintenance note`. Include at least Foundations, Mathematics, Algorithms, Architecture, Operating Systems, Networks, Distributed Systems, Databases, Languages/Compilers, Theory, Security, AI/ML/NLP, Vision/Graphics/HCI/Robotics, Data Science/Parallel/Web. Mark each as `Covered`, `Partial`, or `Candidate` and cite the relevant README anchors.

- [ ] **Step 2: Record explicit deferred candidates**

  Add a `Deferred candidates` section for any course whose official page, syllabus completeness, or long-term URL stability could not be confirmed. Do not place deferred candidates in the main README.

- [ ] **Step 3: Write contributor rules**

  Explain official-source priority, course-vs-tutorial boundaries, required syllabus/material evidence, duplicate normalization (lowercase host, strip fragments and trailing slash), `Archived` labeling, one-line format, and the commands `python scripts/validate_readme.py` and `python scripts/validate_readme.py --check-links`.

- [ ] **Step 4: Check docs cross-links**

  Run `rg -n 'README\.md|validate_readme|coverage' CONTRIBUTING.md docs/coverage.md` and ensure every referenced path exists.

### Task 4: Implement the dependency-free README validator

**Files:**
- Create: `scripts/validate_readme.py`

**Interfaces:**
- `parse_links(text: str) -> list[Link]` extracts Markdown links with labels, URLs, and line numbers.
- `normalize_url(url: str) -> str` lowercases the host, removes fragments, and strips a trailing slash.
- `validate(path: Path, check_links: bool = False) -> int` prints counts/errors and returns process status `0` on success, `1` on validation failure.
- CLI: `python scripts/validate_readme.py [README] [--check-links] [--timeout SECONDS]`.

- [ ] **Step 1: Define parser and normalization helpers**

  Use only `argparse`, `dataclasses`, `re`, `sys`, `urllib.parse`, and `urllib.request`. Ignore image syntax, local anchors, and links inside fenced code blocks. Preserve one-based line numbers.

- [ ] **Step 2: Implement deterministic checks**

  Fail with line-numbered messages for: a missing or multiple H1 headings; missing required taxonomy headings; empty or malformed external URLs; list items containing headings; course bullets that do not match `- [label](url) - institution (status). description`; duplicate normalized course URLs; duplicate normalized course labels within a section; and forbidden imported headings such as `CS-Awesome-Courses`, `Free Programming Courses`, or `University Courses Collection`.

- [ ] **Step 3: Implement optional link checks**

  For `--check-links`, issue a `HEAD` request with a descriptive User-Agent and fall back to a small `GET` request on `405`/`403`. Treat 2xx and 3xx as reachable; report timeout, DNS, and 4xx/5xx failures without hiding them. Do not run this mode in CI.

- [ ] **Step 4: Add a self-test fixture in the module**

  Add `if __name__ == '__main__':` CLI execution and a `--self-test` option that feeds an in-memory valid and invalid snippet to the same validation functions. `python scripts/validate_readme.py --self-test` must exit `0` only when the valid snippet passes and the invalid snippet is rejected.

- [ ] **Step 5: Run validator against the new README**

  Run `python scripts/validate_readme.py README.md` and record the reported course/link counts. Expected: exit `0`, zero structural errors, and zero duplicate course URLs.

### Task 5: Add deterministic CI and licensing metadata

**Files:**
- Create: `.github/workflows/validate.yml`
- Create: `LICENSE`

- [ ] **Step 1: Add the workflow**

  Configure a workflow triggered by `push` and `pull_request` that checks out the repository, sets up Python 3.x, and runs `python scripts/validate_readme.py README.md` and `python scripts/validate_readme.py --self-test`.

- [ ] **Step 2: Add the license file**

  Add the official CC0 1.0 deed/legal-code text and a short header stating that it applies to this repository's original curation text; linked course materials remain under their source licenses.

- [ ] **Step 3: Validate workflow and license references**

  Run `rg -n 'validate_readme|CC0|linked course' .github/workflows/validate.yml README.md CONTRIBUTING.md LICENSE` and `git diff --check`.

### Task 6: Run the end-to-end audit and review the diff

**Files:**
- Read/verify: all files created or modified above.

- [ ] **Step 1: Run all deterministic checks**

  Run `python scripts/validate_readme.py --self-test`, `python scripts/validate_readme.py README.md`, and `git diff --check`. Save the complete outputs for the final report.

- [ ] **Step 2: Run the full canonical link audit**

  Run `python scripts/validate_readme.py README.md --check-links --timeout 20`. For each failure, either repair the URL from an official source, label the entry `Archived`, or remove it with a documented reason. Re-run until no unclassified failure remains.

- [ ] **Step 3: Perform a semantic duplicate review**

  Compare course labels across all sections with `rg -n '^\- \[' README.md`; inspect aliases such as `6.824`/`6.5840`, year-specific MIT 6.006 offerings, CS50 playlists, and Berkeley/Stanford duplicate entries. Keep one canonical bullet per course identity.

- [ ] **Step 4: Check requirement coverage**

  Re-read the spec and verify each acceptance criterion against the current files, including the coverage matrix, research evidence, contribution rules, validator behavior, CI trigger, licensing boundary, and final link status.

- [ ] **Step 5: Review final diff and status**

  Run `git status --short`, `git diff --stat`, and `git diff --check`. Confirm that only README, docs, validator, CI, and license files changed and that no generated or temporary files remain.

- [ ] **Step 6: Commit the implementation**

  ```bash
  git add README.md CONTRIBUTING.md LICENSE docs/coverage.md docs/research/course-candidates.md scripts/validate_readme.py .github/workflows/validate.yml
  git commit -m "curate: rebuild computer science course catalog"
  ```
