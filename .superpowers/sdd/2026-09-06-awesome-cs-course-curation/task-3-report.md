# Task 3 Report: Coverage and Contribution Policy

## Summary

Added the maintainer-facing curriculum matrix in `docs/coverage.md` and the contributor contract in `CONTRIBUTING.md`.

## Commands and Results

- `Get-Content -Raw` on the task brief, design spec, README, Task 2 report, and research notes: confirmed the section contract, the current canonical taxonomy, and the absence of deferred candidates in the research file.
- `rg -n 'README\.md|validate_readme|coverage' CONTRIBUTING.md docs/coverage.md`: confirmed the new docs mention the expected files and validator command names.
- `git diff --check`: clean, no whitespace or patch-format issues.

## Files Changed

- `docs/coverage.md`
- `CONTRIBUTING.md`

## Notes

- The coverage matrix uses the exact requested columns and cites real README anchors for every domain.
- The texts/projects rationale is called out explicitly so the retained companion resources remain justified outside the main course bullets.
- Concern: this checkout does not currently contain `scripts/validate_readme.py`, so the validation commands in `CONTRIBUTING.md` document the intended interface but cannot be executed here yet.
