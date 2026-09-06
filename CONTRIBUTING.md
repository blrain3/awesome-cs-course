# Contributing

This repository is a curated course index, so contributions are judged by evidence, not enthusiasm. Focused pull requests are welcome for course additions, link repairs, metadata corrections, documentation improvements, and translations.

## What to contribute

- Add a substantive course that meets the source and evidence standards below.
- Report or repair a dead, redirected, outdated, or misclassified entry.
- Improve a concise description without adding marketing language or duplicate links.
- Add or maintain a translation of the canonical README.

Keep one concern per pull request where practical. Do not add a course only to increase the list size.

## Source priority

Use official sources first:

1. Official university course page.
2. Official course repository.
3. Official open-course platform.
4. A reputable mirror only when no first-party landing page exists.

Prefer stable landing pages over semester-specific URLs unless the historical page is the best available canonical source.
For an `Archived` entry, a dated snapshot from a reputable web archive is acceptable when the original first-party host is no longer available.

## Course vs. tutorial boundary

The main README is for real course families with syllabus-level structure. Keep out:

- tutorial collections,
- personal note dumps,
- video-only playlists,
- application or entrepreneurship lists,
- random resource directories,
- empty or dead targets.

Standalone books and implementation curricula belong in `Texts and Companion Resources`, not inside a course bullet, unless they are part of the same official course page.

## Evidence required

Before adding or keeping a course, confirm that the official page exposes a meaningful syllabus and multiple learning components such as lectures, readings, assignments, labs, or projects. Record the source URL and the evidence used for the decision in the research notes.

## Duplicate normalization

Treat course URLs as duplicates after normalizing them by:

- lowercasing the host,
- stripping fragments,
- stripping any trailing slash.

When two rows point to the same course family, keep one canonical entry and consolidate the rest under it. Historical offerings should only survive when the archived page is the clearest long-term source or has distinct instructional value.

## Archived labeling

Use `Archived` when the maintained page is a historical offering rather than the current live course page, or when the archived version is the most reliable stable source for the materials.

## Translation contributions

Translations are welcome and should remain faithful mirrors of the canonical English catalog:

- Name the file `README.<locale>.md`, for example `README.zh-CN.md`.
- Keep the same section order, course set, and destination URLs as `README.md`. Translate headings, descriptions, and status text consistently, but do not silently add locale-specific entries.
- Link to both `README.md` and `CONTRIBUTING.md` so readers can find the canonical catalog and contribution rules.
- Keep the translation's contents and links synchronized when the English catalog changes. A translation-only pull request should identify the language and the sections it covers.

The validator enforces the canonical English taxonomy and entry format. Run it against `README.md`; review translated headings, anchors, and cross-file links manually for parity.

## Entry format

Use one bullet per entry and keep it to one line:

```markdown
- [Course name](https://official.example/course) - Institution (Core). One sentence describing the syllabus and practical value.
- [Book title](https://official.example/book) - Text (Core). One sentence describing the companion value.
- [Project title](https://official.example/project) - Project (Core). One sentence describing the scope and skills it teaches.
```

Use `Text` and `Project` labels only in `Texts and Companion Resources`. Do not add extra bullets or supporting links to a course line unless they are part of the same official landing page.

## Pull request checklist

Before opening a pull request:

- Confirm that every changed course link is first-party or an explicitly justified archive.
- Check that the entry is not a duplicate after URL and course-family normalization.
- Keep each course line to one concise sentence and place it in the best-fit section.
- Describe redirects, archive dates, or other maintenance context in the pull request.
- Complete the repository pull request template and include the commands you ran.

## Validation

Run the local validator before opening a change:

- `python scripts/validate_readme.py`
- `python scripts/validate_readme.py --check-links`

The first command checks structure, formatting, and duplicates. The second adds a live link pass for official URLs.
