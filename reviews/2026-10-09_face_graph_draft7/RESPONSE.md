# Response to the seventh review round (ReviewBot assessment of Draft 7, received 9 October 2026)

Files in this folder, verbatim: `ReviewBot_Draft7_Referee_Report.pdf` (7 pages; SHA-256 7bf2d031…f33b45). Author-side check of the numbers the report states: `check_seventh_round_arithmetic.py` (ALL PASS: the support weights 3/7, 1, 1/7, 0 and (1 ± 1/√17)/2, the 42 simple four-cycles and 24 triangles, the weighted total 9.171).

Recommendation received: accept with minor editorial and release revisions; 9.2/10; no mathematical findings; F3 (figure language) closed; F4 is a stated assessment boundary (the release was not executed by the reviewer), not a finding. Draft 8 answers this round. No mathematical statement changes.

| Finding | Where | Action |
|---|---|---|
| F1 immutable archive at submission, with a clean-environment run record of the one-command check | Section 8 | Submission-stage, as the report says. The archive is made when the venue is chosen; the clean-environment run of `run_face_graph_checks.py` against the tagged release, with versions and outcome, will be retained with it. Section 8's future tense stands until then. |
| F2 optional shorter acknowledgements | Acknowledgements | Kept at the Draft 7 length (contributions listed once, history in `reviews/README.md`), with two additions from the reviewer's covering email: the ReviewBot naming is stated as made with his agreement, and the author's responsibility for every statement is stated explicitly (the accountability principle of the Leiden Declaration on AI and Mathematics). |
| Covering email: strip any hint of a wider physical programme | Section 1 | Done. The "word on motivation" paragraph, which mentioned the programme only to disclaim it, is replaced by a scope sentence that mentions nothing outside the note. The note now contains no reference to any physical programme. Section 7's "not a canonical selection principle" sentence is kept as a mathematical remark. |
| F3 figure and evidential language | Section 1, Figure 1, Section 8 | Closed by the reviewer. |
| F4 release not executed by the reviewer | assessment boundary | Noted; the full runner is executed by the author at every tag and the log kept with the tag. |

Reviewer's numbers checked: all exact. The report's identification of Γ as the tetrakis hexahedral graph agrees with Section 1 of the note (stated there since Draft 1 with the MathWorld reference).

State answering this round: tag `face-graph-note-v8`. Previous state: tag `face-graph-note-v7`, commit 4fee5f6975fc62e3a073825eb1b5393cc9cae71c.
