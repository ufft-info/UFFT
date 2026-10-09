# Response to the eighth review round (ReviewBot on Draft 8, 9 October 2026)

Files in this folder: `ReviewBot_Draft8_Referee_Report.pdf` (6 pp) and `ReviewBot_Draft8_Author_Checklist.pdf` (1 p), filed verbatim as received by email from Pablo Moscato at 13:32 AEDT on 9 October 2026; `check_eighth_round_arithmetic.py`, the author-side recomputation of every number the report states; this response.

Draft reviewed: Draft 8, tag `face-graph-note-v8`, commit 2b7619b. Draft produced in response: Draft 9, tag `face-graph-note-v9`.

## What the round did

The report follows the six-point list the author sent with Draft 8 (what the earlier rounds were not doing): the aggregate score is omitted; the recommendation states what would reverse it; an adversarial test is run on the step the author named as weakest, the spherical gauge classification (Proposition 6.1); a bounded prior-art search is run and reported as a bounded non-detection; and the report says plainly that inherited exact checks are not a new execution of the Draft 8 code. Recommendation: conditional minor revision; no critical or major finding; two closure requests (C1, C2), one optional clarification.

## Arithmetic check

`check_eighth_round_arithmetic.py` recomputes, exactly where the quantity is an integer or a rank over Q and to machine precision otherwise: the chain-complex ranks (d1 d2 = 0, rank d1 = 13, rank d2 = 23, dim ker d1 = 23, so the 24 oriented triangles span the cycle space with the single relation that their outward boundaries sum to zero); that a vertex gauge changes no plaquette holonomy; vertex connectivity 4; tr D³ = 2112, tr(D A²) = 384, tr A³ = 144 at q = 0; the toroidal negative control (4 × 4 periodic lattice, phase e^{iθ/4} on horizontal edges: every face holonomy trivial, winding-loop holonomy e^{iθ}); and the two orthonormal quarter-flux blocks. All pass. The report's description of the graph (MathWorld's tetrakis hexahedral graph, order-48 automorphism group, degree sequence 4⁶6⁸) agrees with Section 1 of the note.

## Findings and what was done

**C1, release-level reproduction (closure required at submission).** Unchanged position, as in rounds six and seven: the Zenodo deposit of the submitted tag, the pinned environment and the clean-environment runner receipt are produced at submission, and the note says so in Section 8. Not a Draft 9 change. The author-side clean-clone replay of the tagged release is recorded separately in `verification/README.md` when run.

**C2, precision of priority and context (minor).** Draft 9, Section 1, last paragraph: the sentence that already separated the catalogued graph and the spherical flux construction from this note's contribution now names both antecedents and what they contain: MathWorld's entry (the graph, its automorphism group, its adjacency polynomial) and Avishai and Luck's monopole construction with its examples (the Platonic graphs, C₆₀, the N-diamonds and N-prisms, none with degree sequence 4⁶6⁸), against the Laplacian orbit decomposition and the two exact magnetic factorisations given here. No priority claim is added; the bounded-search wording is kept.

**Optional, the topology premise.** Draft 9, proof of Proposition 6.1: the parenthetical rank statement is promoted to a sentence giving the chain-complex ranks for Γ (d1 d2 = 0, rank d1 = 13, rank d2 = 23, so the 24 triangle boundaries span the 23-dimensional cycle space with one relation), and a sentence that the sphere hypothesis is essential, with the toroidal counterexample of this round credited to it. The S² hypothesis stays in the statement.

**Table 2.** The round reviewed Draft 8, in which nothing was machine-checked. Between Draft 8 and Draft 9 the Lean project `verification/lean/FaceGraph/` grew from Theorem 3.1 to four files, all kernel-checked with axioms `propext`, `Classical.choice`, `Quot.sound` only: Theorem 3.1 (full statement); Theorem 5.1 (1), (2), (4) on the explicit orbit basis; Theorem 6.4 at q = 12 (full statement, signless Laplacian) and at q = 6 (full statement over the Gaussian integers, with the Gram identity of Proposition 6.5 as a lemma). Table 2 and the sentence in Section 8 that said nothing was machine-checked are updated accordingly; what the Lean files do not cover (Lemma 3.2's identification of the basis with the isotypic components, Theorem 5.1 (3), Propositions 6.1 and 6.2, the Fedorov table) is stated in the table and in the project README. This is the author's own formalisation and is reported as such.

**Acknowledgements.** Eight rounds. The chain-complex test and the toroidal control are credited to this round at the place they appear.

## Not changed

Figure 1 stays as ranked eigenvalues with the non-analytic-branches qualifier (the report asks that this be kept). The quarter-flux gauge, the Gram identity, the magnetic representation and the Fedorov table are unchanged from Draft 7.
