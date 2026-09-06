# Task 5 Report: Deterministic CI and Licensing Metadata

## Summary

Added a minimal GitHub Actions workflow in `.github/workflows/validate.yml` and a repository-level `LICENSE` file for the original curation text.

## Verification

### Reference check

Command:

```bash
rg -n 'validate_readme|CC0|linked course' .github/workflows/validate.yml README.md CONTRIBUTING.md LICENSE
```

Result:

```text
.github/workflows/validate.yml:21:        run: python scripts/validate_readme.py README.md
.github/workflows/validate.yml:24:        run: python scripts/validate_readme.py --self-test
CONTRIBUTING.md:63:- `python scripts/validate_readme.py`
CONTRIBUTING.md:64:- `python scripts/validate_readme.py --check-links`
LICENSE:1:This repository's original curation text is dedicated under CC0 1.0 Universal.
LICENSE:4:CC0 1.0 Universal
LICENSE:5:CC0 1.0
LICENSE:35:additional consideration or compensation, the person associating CC0 with a
LICENSE:37:and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and
LICENSE:40:effect of CC0 on those rights.
LICENSE:44:A Work made available under CC0 may be protected by copyright and related or
LICENSE:96:The License shall be deemed effective as of the date CC0 was applied by
LICENSE:122:     to this document and has no duty or obligation with respect to this CC0 or
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

### Validator smoke test

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

## Notes

- The workflow uses only `actions/checkout` and `actions/setup-python`, and it runs exactly the two requested deterministic validator commands.
- The `LICENSE` file limits CC0 coverage to the repository’s original curation text; linked course materials keep their source licenses.
- Existing untracked `scripts/__pycache__/` content was left untouched.

## Fix Round 1

Added the official CC0 deed summary ahead of the legal code in `LICENSE`, including the public-domain dedication, the "No Copyright" summary, the canonical URL, and the link to the legal code.

### Re-check

Command:

```bash
rg -n 'validate_readme|CC0|linked course' .github/workflows/validate.yml README.md CONTRIBUTING.md LICENSE
```

Result:

```text
.github/workflows/validate.yml:21:        run: python scripts/validate_readme.py README.md
.github/workflows/validate.yml:24:        run: python scripts/validate_readme.py --self-test
CONTRIBUTING.md:63:- `python scripts/validate_readme.py`
CONTRIBUTING.md:64:- `python scripts/validate_readme.py --check-links`
LICENSE:1:This repository's original curation text is dedicated under CC0 1.0 Universal.
LICENSE:4:CC0 1.0 Universal
LICENSE:5:CC0 1.0
LICENSE:11:No Copyright
LICENSE:47:additional consideration or compensation, the person associating CC0 with a
LICENSE:49:and Related Rights in the Work, voluntarily elects to apply CC0 to the Work and
LICENSE:52:effect of CC0 on those rights.
LICENSE:56:A Work made available under CC0 may be protected by copyright and related or
LICENSE:108:The License shall be deemed effective as of the date CC0 was applied by
LICENSE:134:     to this document and has no duty or obligation with respect to this CC0 or
```

Command:

```bash
git diff --check
```

Result:

```text
exit 0
```
