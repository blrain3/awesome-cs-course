# Contributing

This repository is a curated course index, so contributions are judged by evidence, not enthusiasm.

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

## Entry format

Use one bullet per entry and keep it to one line:

```markdown
- [Course name](https://official.example/course) - Institution (Core). One sentence describing the syllabus and practical value.
- [Book title](https://official.example/book) - Text (Core). One sentence describing the companion value.
- [Project title](https://official.example/project) - Project (Core). One sentence describing the scope and skills it teaches.
```

Use `Text` and `Project` labels only in `Texts and Companion Resources`. Do not add extra bullets or supporting links to a course line unless they are part of the same official landing page.

## Validation

Run the local validator before opening a change:

- `python scripts/validate_readme.py`
- `python scripts/validate_readme.py --check-links`

The first command checks structure, formatting, and duplicates. The second adds a live link pass for official URLs.
