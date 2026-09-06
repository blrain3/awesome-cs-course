# Coverage Matrix

This page is the maintainer-facing snapshot of curriculum coverage and the place to park any candidate that is not yet strong enough for `README.md`.

The current README is already subject-first, so the table below focuses on what is covered well, what is only partially represented, and where future additions would still need first-party evidence.

The [canonical link audit](research/link-audit.md) records the response, redirect, and page-content checks for every external README URL; internal repository links are checked structurally by the validator.

| Domain | Core coverage | Representative entries | Gap or maintenance note |
| --- | --- | --- | --- |
| Foundations and Programming | Covered | [Foundations and Programming](../README.md#foundations-and-programming): CS50x, CS61A, COS 126, MIT 6.100L | Strong intro coverage; keep favoring official course roots and avoid adding narrower tutorial fragments. |
| Mathematics for Computer Science | Covered | [Mathematics for Computer Science](../README.md#mathematics-for-computer-science): CS70, MIT 6.042J, CS109 | Good balance of proof, probability, and discrete structures; future additions should close any missing linear algebra or statistics angle only if a first-party course appears. |
| Data Structures and Algorithms | Covered | [Data Structures and Algorithms](../README.md#data-structures-and-algorithms): CS61B, MIT 6.006, MIT 6.046J, COS 226, UIUC CS225 | Well represented across implementation and analysis; duplicates should stay merged by course family. |
| Computer Architecture and Systems | Covered | [Computer Architecture and Systems](../README.md#computer-architecture-and-systems): CS61C, MIT 6.004, CMU 15-213, ETH DDCA, CMU 18-447 | Coverage spans digital logic to modern processor design; the 18-447 page is an explicitly labeled Spring 2024 archive, so recheck for a newer public offering before replacing it. |
| Operating Systems | Covered | [Operating Systems](../README.md#operating-systems): MIT 6.1810, UC Berkeley CS162 | Compact but strong; OSTEP remains in the texts section as the canonical companion rather than a duplicate course entry. |
| Computer Networks | Covered | [Computer Networks and Distributed Systems](../README.md#computer-networks-and-distributed-systems): Stanford CS144 | The live Stanford host now redirects to a dead GitHub Pages site, so the README uses a dated archive of the official Fall 2025 course page and labels it `Archived`; recheck for a new first-party host before replacing it. |
| Distributed Systems | Covered | [Computer Networks and Distributed Systems](../README.md#computer-networks-and-distributed-systems): MIT 6.5840, CMU 15-440 | The same combined section also covers distributed systems well; keep replication, consensus, and fault-tolerance courses together under the shared anchor. |
| Databases and Data Management | Covered | [Databases and Data Management](../README.md#databases-and-data-management): CMU 15-445/645, CMU 15-721 | Strong implementation and advanced coverage; 15-721 currently exposes its Fall 2025 materials and is labeled `Archived`; DDIA stays in the texts section as the stable companion resource. |
| Programming Languages and Compilers | Partial | [Programming Languages and Compilers](../README.md#programming-languages-and-compilers): MIT 6.1100, Stanford CS143 | The compiler side is solid, with MIT 6.1100 retained as an explicitly labeled Spring 2025 archive; the section still lacks an explicit language-systems or PL-theory course family beyond compilers. |
| Theory of Computation | Covered | [Theory of Computation](../README.md#theory-of-computation): Stanford CS103 | The foundational theory slot is filled; future entries should stay focused on proof-heavy, first-party offerings. |
| Security and Cryptography | Covered | [Security and Cryptography](../README.md#security-and-cryptography): MIT 6.858, Stanford CS155 | Good systems-security coverage; cryptography remains represented through course framing rather than a standalone survey. |
| Artificial Intelligence, Machine Learning, and NLP | Covered | [Artificial Intelligence, Machine Learning, and NLP](../README.md#artificial-intelligence-machine-learning-and-nlp): CS50 AI, CS221, CS229, CS188, CS189, CS224N, CS336 | Broad and deep coverage; keep a close eye on overlap so new candidates add real syllabus value. |
| Computer Vision, Graphics, HCI, and Robotics | Partial | [Computer Vision, Graphics, HCI, and Robotics](../README.md#computer-vision-graphics-hci-and-robotics): CS184/284A, CS231N | Graphics and vision are present, but HCI and robotics still need a first-party course before this domain feels complete. |
| Data Science, Parallel Computing, and Web Development | Partial | [Data Science, Parallel Computing, and Web Development](../README.md#data-science-parallel-computing-and-web-development): CS50 Web, CS149 | Web and parallel computing are covered, but the section still lacks an explicit data science course. |

## Texts and companion rationale

The high-value items in [Texts and Companion Resources](../README.md#texts-and-companion-resources) were intentionally retained or relocated there because they are standalone companions, not separate course families. Moving them back into course sections would blur the canonical course index and create duplicate coverage signals.

- `Operating Systems: Three Easy Pieces` stays as the systems text because it is the stable free companion for operating systems coverage.
- `Computer Networking: A Top-Down Approach` stays as the networking text because it is a first-party companion site that complements the network courses without duplicating them.
- `Designing Data-Intensive Applications` stays as the database companion because it adds durable conceptual depth without pretending to be a course page.
- `Nand2Tetris` is kept as a project because it is a self-contained build-up curriculum that spans multiple domains.
- `The Missing Semester of Your CS Education` is kept as a project because it is a cross-cutting skills curriculum, not a university course entry.

## Deferred candidates

None. `docs/research/course-candidates.md` currently has no rejected or deferred entries, so there is no evidence-backed candidate being held out of `README.md` today.

If a future candidate lacks a verified official page, a complete syllabus/material set, or stable long-term URL behavior, it should stay out of the main README and be recorded here instead.
