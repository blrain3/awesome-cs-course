# Awesome CS Courses Curation Design

**Date:** 2026-09-06

## Context

The repository currently contains only an untracked `README.md`. The file is 2,237 lines long and combines at least five independently structured catalogs: a recent Chinese resource list, an older `CS-Awesome-Courses` list, a Chinese recommendation list, an `Awesome-OpenCS` university list, and a `University Courses Collection`. Static inspection found 816 list-item lines, 1,371 Markdown links, repeated course identities and URLs, empty link targets, malformed headings, stale endpoints, and many non-course resources.

The maintenance objective is a trustworthy, long-lived course index. The primary quality axis is accuracy and maintainability, not raw entry count.

## Goals

1. Create one canonical, subject-first course index that a learner can scan and extend.
2. Merge aliases and year-specific duplicates into one canonical entry unless a historical version has distinct instructional value.
3. Prefer official university course pages, official course repositories, and first-party open-course platforms.
4. Keep concise, consistent metadata: course name, institution, level/status where useful, and a one-sentence scope statement.
5. Add verified high-value courses that close clear curriculum gaps without padding the list.
6. Make the curation rules and static checks executable for future contributors.
7. Record curriculum coverage and unresolved gaps separately from the main list.

## Non-goals

- Preserving every imported link in the main README.
- Maintaining random video playlists, personal notes, SEO aggregators, or commercial/entrepreneurship resources as CS courses.
- Building a course database or a dependency-heavy documentation site.
- Claiming that linked course materials share this repository's license.

## Information Architecture

`README.md` will be English-first, with a short Chinese note for the existing audience. It will contain one introduction, a table of contents, a compact usage/selection policy, and these stable subject sections:

1. Foundations and Programming
2. Mathematics for Computer Science
3. Data Structures and Algorithms
4. Computer Architecture and Systems
5. Operating Systems
6. Computer Networks and Distributed Systems
7. Databases and Data Management
8. Programming Languages and Compilers
9. Theory of Computation
10. Security and Cryptography
11. Artificial Intelligence, Machine Learning, and NLP
12. Computer Vision, Graphics, HCI, and Robotics
13. Data Science, Parallel Computing, and Web Development
14. Texts and Companion Resources

The taxonomy intentionally groups closely related subjects to avoid the fragmentation and cross-listing in the source file. A course appears once, under the subject that best matches its learning objective. A historical offering is retained only when its assignments, labs, or tooling provide distinct value and is explicitly labeled `Archived`.

## Entry Contract

Course entries use one stable form:

```markdown
- [Course name](https://official.example/course) - Institution (level/status). One sentence describing the syllabus and practical value.
```

The primary link must be the most authoritative stable landing page. Supporting books or repositories belong in `Texts and Companion Resources` or in a short parenthetical note only when they are part of the same official course. Descriptions avoid rankings, marketing language, unverifiable claims, and copied promotional text.

## Curation and Research

Existing entries are classified as keep, consolidate, repair, archive, or remove. Removal is limited to dead/empty links, exact or semantic duplicates, non-course material, clearly out-of-scope commercial content, or resources whose quality and provenance cannot be established. High-value material is migrated to a canonical entry rather than silently discarded.

New candidates are checked against first-party pages in this order: official university course page, official course repository, official open-course platform, then a reputable mirror only when no first-party landing page is available. A candidate must expose a meaningful syllabus and multiple learning components (such as lectures, readings, assignments, labs, or projects), be publicly accessible, and fill a documented coverage need. Research notes cite the source URL and the evidence used for inclusion.

## Repository Artifacts

- `README.md` is the canonical curated catalog.
- `CONTRIBUTING.md` defines inclusion, update, duplicate, and link policies.
- `docs/coverage.md` is the curriculum coverage matrix and candidate backlog.
- `docs/research/course-candidates.md` records first-party evidence for newly added courses.
- `scripts/validate_readme.py` performs dependency-free structural, format, and duplicate checks; `--check-links` is an optional local network pass.
- `.github/workflows/validate.yml` runs the deterministic validator on pushes and pull requests.
- `LICENSE` identifies the license for this repository's curation text and clarifies that linked materials retain their own licenses.

## Validation

The validator must fail on malformed Markdown links, empty targets, duplicate canonical course URLs, duplicate course titles within a subject, missing required headings, incorrect entry shape, and known forbidden patterns (for example, an empty link target or a list item containing a heading). It must print counts and line numbers for actionable failures. Network checks remain opt-in so CI is deterministic; the final maintenance pass records the observed status of every canonical link.

## Acceptance Criteria

- The main README has exactly one top-level title, one table of contents, no imported sub-README, and no duplicate course entries.
- Every main-list course has a first-party or explicitly labeled archived URL and a concise, accurate description.
- The final taxonomy covers the core undergraduate CS path and makes remaining gaps explicit in `docs/coverage.md`.
- The repository contains contribution guidance and a runnable validator with no third-party dependencies.
- Static validation, Markdown parsing, duplicate detection, and the documented link audit all complete successfully; any inaccessible optional/archived resource is clearly labeled rather than hidden.
- The diff contains only catalog, maintenance-documentation, licensing, and validation changes related to this goal.

## Risks and Decisions

Course websites change frequently, especially semester-specific pages. Stable department roots and official course repositories are preferred; year-specific pages are retained only when they are the actual public materials and are labeled. Because the source README combines material from projects with different provenance, the repository license is applied only to this catalog's original selection and descriptions, not to external course content.
