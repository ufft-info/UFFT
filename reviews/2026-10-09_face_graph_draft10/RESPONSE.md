# Response to the tenth review round (ReviewBot on Draft 10, 9 October 2026)

Files in this folder: `ReviewBot_Draft10_Client_Delivery.zip` as received (containing `ReviewBot_Draft10_Referee_Report.pdf`, 7 pp, and `ReviewBot_Draft10_Author_Checklist.pdf`, 1 p), filed verbatim from Pablo Moscato's email of 9 October 2026, 16:42 AEDT; the two PDFs extracted alongside; `check_tenth_round_arithmetic.py`, the author-side recomputation of the round's geometry-to-rule test; this response.

Draft reviewed: Draft 10, tag `face-graph-note-v10`, commit 56f6bfd. **No Draft 11.** The round asks for nothing that changes the manuscript; see below.

## What the round did

It attacked the one gap the ninth round's bridge left open, the step from the polyhedron to the adjacency rules, from the other side: it rebuilt the fourteen faces as vertex subsets of the 24 points (permutations of (0, ±1, ±2)), declared two faces adjacent when they share exactly two vertices, and compared with `Graph.lean`'s rule entry by entry, with the labeled bit convention, not up to isomorphism (44/44); it rebuilt the quarter-flux matrix from the gauge formula, checked both Gram identities and the holonomy of all 24 outward triangles, and showed that a reversed bit order and a single sign flip are both detected. It then stated, in its own words, that no additional generalisation, computation or formalisation is required to close the round, and that what closes the file is an independent replay of the tagged runner and Lean build plus the archive identifier.

## Arithmetic check

`check_tenth_round_arithmetic.py` reproduces the geometry-to-rule construction exactly (sympy): the 24 vertices, the face vertex sets (4 and 6), geometric adjacency equal to the rule, 36 edges and degrees 4⁶6⁸, the reversed-bit-order control, the two Gram identities from the integer formula, the 24 outward triangles, the sign-flip control, and the three characteristic polynomials from the rule-built matrices. All pass. One reading note on the report's Section 3.3: the holonomy of the magnetic adjacency around an outward triangle (s, h, h′) is the product of its three entries, B_{s,h} · 1 · B̄_{s,h′}, which is uniformly i; the report writes the product without the conjugate, B_{s,h} B_{s,h′}, which is i on some triangles and −i on others. The report's conclusion (every outward plaquette carries the q = 6 holonomy) is correct; the formula in its text should be read with the conjugate on the second factor.

## Findings and what was done

**R1, tagged release replay (required at acceptance).** As in rounds six to nine: the independent replay is a submission-time item and needs a third party with Lean installed. In the meantime the author-side replay is repeated at tag v10 and extended to the Lean build: a fresh clone in a clean Linux container, the pinned requirements, the one-command runner, then `lake exe cache get` and `lake build` of the five modules, with exit codes, the five axiom lists and file hashes recorded in `verification/CLEAN_RUN_face-graph-note-v10.md`. Author-side, and it says so.

**R2, permanent archive (required for deposit).** Submission-time. The deposit will be made from the GitHub release of the submitted tag so that the DOI points at exactly that commit, and the release archive (manuscript source and PDF, scripts, the Lean tree, certificates, the reviewers' checkers, CSV and figure, with a hash manifest) is the same file sent with the submission, so that a reviewer can validate from the archive alone without GitHub access. That is also the answer to the covering email's question about closing the gap for ReviewBot: the submission package is the manuscript plus the release archive, not a pointer to a repository.

**R3, keep the boundary explicit.** Kept as written in Draft 10 (Section 8 and Tables 2 and 3). No change.

**R4, attribution length (optional).** Noted for submission: the acknowledgements will be condensed to the intellectual credit, the non-independence statement and the responsibility line, with the round-by-round mechanics left in `reviews/README.md`, if the venue prefers. Not changed now, since the round asks for nothing else and a Draft 11 for this alone would be churn.

## Status of the note

Ten rounds. The last five found no mathematical defect; rounds eight to ten each attacked a named weakest step (the spherical gauge classification, the typed matrices, the geometry-to-rule step) and each attack failed. The manuscript is at the point the tenth report describes: closed on the mathematics, open only on the two submission-time items. It does not change until a venue is chosen.
