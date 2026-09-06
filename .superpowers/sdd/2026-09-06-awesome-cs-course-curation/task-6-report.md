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

- No README, docs, or license files were modified.
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
