# Task 2 Report: Canonical README

## Summary

Replaced the stitched catalog in `README.md` with a curated, subject-first README that uses the exact 14 taxonomy headings, one canonical bullet per course family, and a dedicated texts section for books/projects.

## Commands and Results

- `Get-Content` on the brief, spec, evidence, and final `README.md`: confirmed the task contract, accepted candidates, and final file shape.
- `curl.exe -I -L` network checks against official roots: verified the chosen course URLs; one initial MIT 6.100L slug returned `404`, and I corrected it to the working OCW path used in the final README.
- `rg -n '^# |^## |^- \[' README.md`: found one H1, the 14 canonical section headings, policy headings, and the expected course bullets.
- `rg -n '\]\(\s*\)' README.md`: no empty link targets found.
- `git diff --check`: clean, no whitespace errors.

## Files Changed

- `README.md`
- `.superpowers/sdd/2026-09-06-awesome-cs-course-curation/task-2-report.md`

## Self-Review

- The README now has a single top-level title, a ToC that links only to the 14 taxonomy sections, and one canonical placement per course.
- High-value families from the brief are represented with first-party or archived official roots, and historical offerings are labeled `Archived`.
- The final Texts section keeps books and projects separate from course bullets with explicit `Text` and `Project` labels.
- Open concern: `docs/coverage.md` was not updated because the task scope explicitly limited edits to `README.md` plus this report.
