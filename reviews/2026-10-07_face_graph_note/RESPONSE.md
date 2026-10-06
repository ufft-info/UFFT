# Response to the standalone review of the face-graph note (7 October 2026)

Review: `Standalone_Referee_Review.pdf` (7 pages) with its own exact verifier `verify_review.py` and `verification_results.json`. Recommendation: revise and resubmit as a short mathematical or computational note. Every polynomial in the draft was independently reproduced exactly.

| Finding | Action in draft 2 |
|---|---|
| Abstract and Corollary 3.3 wrongly place the adjacency spectrum in Q(√17); x² − 3x − 12 has discriminant 57 | corrected throughout: adjacency splitting field Q(√17, √57); the 2×2 blocks now show where 57 and 17 arise |
| Aut(Γ) by exhaustive search | replaced by the reviewer's structural argument through the cube graph; enumeration kept as a check |
| flux π computed, not proved | the reviewer's proof added: all-negative gauge gives the signless Laplacian D + A, blocks give x² − 13x + 24 and (x−3)(x−8) by hand |
| magnetic symmetry remark attributed the failure to a subgroup of O_h | rewritten: gauge-compensated projective symmetry of the rotation group; open question restated as an explicit intertwiner |
| "no net monopole charge" misleading; L_q defined only up to gauge | corrected: total flux 2πq quantised; spectrum and gauge class periodic in q; q → −q is conjugation |
| "maximally frustrated" / Lieb | removed |
| trace explanation 3 + 6 − 0 wrong | replaced by 4 + (6 − 1) |
| "two eigenspaces" confined to one orbit | three irreducible summands |
| unitary vs orthogonal | orthogonal over the reals, unitary noted for the complexification; K² = −12I on the A1g plane added |
| Avishai–Luck entry incomplete | P06007 and DOI added |
| Kelvin's curved cells vs the combinatorial type | separated |
| provisional named acknowledgement | removed; no personal endorsement implied |
| reproducibility: exact arithmetic not guaranteed; no certificate; abstract said all-NumPy | scripts restated (object-dtype exact integers; SymPy for Z[i]); exact block checks on raw vectors; numerical checks labelled; holonomy check on every triangle; JSON gauge certificate written; scripts committed to verification/ |
| novelty and priority | qualified in the introduction |

The reviewer's own verifier passes on the author's machine.
