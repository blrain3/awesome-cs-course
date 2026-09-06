# Task 1 Report

Completed the first-party source pass and wrote the candidate table to `docs/research/course-candidates.md`.

I accepted 11 course records. The MIT OS entry and Stanford CS149 are archived offerings; MIT 6.5840 and Stanford CS103 are current official pages; the Harvard, Berkeley CS70/CS184, CMU 15-445, and UIUC CS225 entries are current official pages.

No candidates were deferred. I also ran the required unsupported-claim scan on `docs/research/course-candidates.md` and removed the risk of any `TBD`, `unverified`, `rumour`, `best`, or `#1` language from the research file.

Fix review follow-up:

`rg -n "TBD|unverified|rumou?r|best|#1" docs/research/course-candidates.md`

Output: no matches.

Documentation note: updated the summary sentence above to match the corrected status flags. No code test needed.
