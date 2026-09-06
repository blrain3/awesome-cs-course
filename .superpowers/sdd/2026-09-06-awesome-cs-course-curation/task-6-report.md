# Task 6 Report: Final Review Fixes

## Summary

Implemented the two final review fixes:

- Pinned GitHub Actions to `ubuntu-24.04` and Python `3.12.8` in `.github/workflows/validate.yml`.
- Extended `scripts/validate_readme.py` to require the exact 14-item `## Contents` anchor block, with line-numbered errors for malformed, missing, wrong, duplicate, and extra entries.

The validator still ignores local `#...` anchors for external-link checks and keeps the existing stdlib-only structure.

## Verification

Command:

```bash
python -m py_compile scripts/validate_readme.py
```

Result:

```text
```

Command:

```bash
python scripts/validate_readme.py --self-test
```

Result:

```text
Links: 15
Course bullets: 15
Validation passed
Links: 15
Course bullets: 15
Line 52: malformed or unclosed markdown link
Line 23: invalid course status: Draft
Line 25: text/project entries belong only in Texts and Companion Resources
Line 7: wrong Contents anchor 1: expected #foundations-and-programming, got #foundations-and-programming-wrong
Validation failed: 4 problem(s)
Self-test passed
```

Command:

```bash
python scripts/validate_readme.py README.md
```

Result:

```text
Links: 45
Course bullets: 45
Validation passed
```

Command:

```bash
git diff --check
```

Result:

```text
warning: in the working copy of '.github/workflows/validate.yml', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'scripts/validate_readme.py', LF will be replaced by CRLF the next time Git touches it
```

## Notes

- At this stage, no README, docs, or license files were modified.
- The generated `scripts/__pycache__/` artifact from `py_compile` was removed after verification.

## Follow-up: URL hardening

Extended `_is_external_url()` to reject raw whitespace/control characters and to treat `urlsplit()` parsing failures as invalid URLs. The self-test now exercises both malformed forms: an invalid IPv6-style URL and a URL with embedded whitespace.

### Verification

Command:

```bash
python scripts/validate_readme.py --self-test
```

Result:

```text
Links: 15
Course bullets: 15
Validation passed
Links: 15
Course bullets: 15
Line 52: malformed or unclosed markdown link
Line 23: invalid course status: Draft
Line 23: malformed external URL: https://[bad
Line 25: text/project entries belong only in Texts and Companion Resources
Line 25: malformed external URL: https://example.com/a b
Line 7: wrong Contents anchor 1: expected #foundations-and-programming, got #foundations-and-programming-wrong
Line 23: malformed external URL: https://[bad
Line 25: malformed external URL: https://example.com/a b
Validation failed: 8 problem(s)
Self-test passed
```

Command:

```bash
python scripts/validate_readme.py README.md
```

Result:

```text
Links: 45
Course bullets: 45
Validation passed
```

Command:

```bash
git diff --check
```

Result:

```text
warning: in the working copy of 'scripts/validate_readme.py', LF will be replaced by CRLF the next time Git touches it
```

## Follow-up: content and validator audit

The canonical-link audit found that `cs61b.org` was a parked placeholder and that the Stanford CS144 host redirected to a GitHub Pages 404. CS61B now points to the substantive UC Berkeley Fall 2026 page at `https://fa26.datastructur.es/`; CS144 now points to a dated Wayback capture of the official Fall 2025 course page and is explicitly labeled `Archived`. Stanford CS155, CS221, and CS231N directory-index URLs were replaced with their substantive official course roots. Dated CMU 18-447, CMU 15-721, and MIT 6.1100 offerings were relabeled `Archived`. The per-link evidence is recorded in `docs/research/link-audit.md`.

The validator now rejects duplicate required taxonomy headings and its self-test includes a repeated-heading fixture. The test was observed failing before this change and passing after it. CI action references are pinned to verified release commit SHAs (`actions/checkout` v4.2.2 and `actions/setup-python` v5.6.0), in addition to `ubuntu-24.04` and Python `3.12.8`.

### Fresh verification

```text
python scripts/validate_readme.py --self-test: exit 0
python scripts/validate_readme.py README.md: exit 0; Links: 45; Course bullets: 45
python scripts/validate_readme.py README.md --check-links --timeout 20: exit 0; Links: 45; Course bullets: 45
python -m py_compile scripts/validate_readme.py: exit 0
git diff --check: exit 0 (Windows line-ending advisory warnings only)
```

## Follow-up: entry-shape hardening

The validator now treats every unordered list marker (`-`, `*`, or `+`) in a taxonomy section as an entry candidate, so alternate markers cannot silently bypass the canonical hyphen bullet contract. It also rejects empty course labels with a line-numbered error. The built-in self-test includes regression fixtures for both cases.

### Fresh verification

```text
python -B scripts/validate_readme.py --self-test: exit 0
python -B scripts/validate_readme.py README.md: exit 0; Links: 45; Course bullets: 45
```
