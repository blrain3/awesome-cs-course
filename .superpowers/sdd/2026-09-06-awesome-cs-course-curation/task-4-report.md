# Task 4 Report: Dependency-Free README Validator

## Summary

Added `scripts/validate_readme.py`, a dependency-free README validator with deterministic structure checks, optional live link checking, and a built-in self-test.

## Verification

### Syntax check

Command:

```bash
python -m py_compile scripts/validate_readme.py
```

Result:

```text
exit 0
```

### Self-test

Command:

```bash
python scripts/validate_readme.py --self-test
```

Result:

```text
Links: 14
Course bullets: 14
Validation passed
Links: 14
Course bullets: 14
Line 8: list item contains a heading
Line 9: duplicate normalized course URL (also line 6)
Validation failed: 2 problem(s)
Self-test passed
```

### README validation

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

### Patch hygiene

Command:

```bash
git diff --check
```

Result:

```text
exit 0
```

## Notes

- The validator skips local anchors and fenced code blocks when extracting links.
- Optional live link checks use `HEAD` with a descriptive User-Agent and fall back to a small `GET` request for `403`/`405`.
- The built-in self-test exercises the same validation path with one valid snippet and one intentionally invalid snippet.

## Fix Round 1

Addressed the review findings by tightening status validation, rejecting `Text`/`Project` bullets outside `Texts and Companion Resources`, and replacing the markdown-link regex with a balanced-parentheses scanner that reports malformed/unclosed links.

### Post-fix verification

Command:

```bash
python -m py_compile scripts/validate_readme.py
```

Result:

```text
exit 0
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
Line 35: malformed or unclosed markdown link
Line 6: invalid course status: Draft
Line 8: text/project entries belong only in Texts and Companion Resources
Validation failed: 3 problem(s)
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
