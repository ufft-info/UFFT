# Response to the ninth review round (ReviewBot on Draft 9, 9 October 2026)

Files in this folder: `ReviewBot_Draft9_Referee_Report.pdf` (7 pp) and `ReviewBot_Draft9_Author_Checklist.pdf` (1 p), filed verbatim as received from Pablo Moscato on 9 October 2026; `check_ninth_round_arithmetic.py`, the author-side recomputation of every identity the report states; this response.

Draft reviewed: Draft 9, tag `face-graph-note-v9`, commit 1651c1a. Draft produced in response: Draft 10, tag `face-graph-note-v10`.

## What the round did

The first round to look at the Lean sources. It inspected the five theorem files at the tag (without building them, Lean not being installed in its environment), tabulated what each one proves and what it leaves outside, reconstructed the graph, the two magnetic matrices, K and the boundary maps independently (25 checks, including a sign-perturbation control on the quarter-flux gauge), and closed the previous round's C2 and the optional topology item. Recommendation: conditional minor revision; no mathematical finding; R1 required (independent replay of the Python runner and the Lean build at the tag, with the archive), R2 optional (the bridge from the typed matrices to the graph).

## Arithmetic check

`check_ninth_round_arithmetic.py` recomputes exactly (sympy over Q and Q(i)): the two characteristic polynomials from the adjacency rules; the Gram identities B*B = (9I − C²)/2 and BB* = 4I for the printed gauge, that every nonzero entry of B is a unit phase, and that one sign flip breaks the Gram identity (the report's control); the q = 6 polynomial from the gauge formula; the K relations (Kᵀ = −K, K s_a = h_a, K h_a = −4 s_a, K² = −12 on the orbit constants); the chain-complex ranks. All pass.

## Findings and what was done

**R1, independent replay (required at acceptance).** Unchanged position: the Zenodo deposit of the submitted tag and an independent clean-environment run of the four-script runner and of `lake build` are produced at submission. The author-side clean-clone replay of tag v8 is at `verification/CLEAN_RUN_face-graph-note-v8.md`; it is not independent and says so. The report notes, correctly, that the reviewer cannot run Lean; an independent replay will need a third party with elan installed, and the README gives the two commands.

**R2, the bridge (optional; done).** The report's point is exact: a kernel proof about a typed matrix is a proof about whatever was typed. Draft 10 adds `verification/lean/FaceGraph/FaceGraph/Graph.lean`: the adjacency rules of Proposition 2.1 (a square (a, σ) is adjacent to the hexagons with h_a = σ; hexagons adjacent at Hamming distance one) and the gauge formula (B) are Lean functions on the vertex indices; the Laplacian, the signless Laplacian and Δ₆ are built from them; `Lgraph_eq_Lfin`, `Sgraph_eq_Sfin`, `Dre_eq_D6r`, `Dim_eq_D6i` prove the rule-built matrices equal the literals by kernel evaluation on every index pair; `charpoly_Lgraph`, `charpoly_Sgraph`, `charpoly_Dgraph` then state the three theorems for the rule-built matrices, and `gauge_unit_modulus` that every square–hexagon entry of the gauge is a unit phase. Axioms: `propext`, `Classical.choice`, `Quot.sound`. What the bridge does not do, and the note now says in Section 8: that these rules describe the truncated octahedron and its plaquette holonomies is Proposition 2.1 and Section 6.1 by hand.

**The one-page mapping (the report's suggestion to the authors).** Draft 10 has a new Table 3 listing every Lean theorem name against the equation or result of the note it establishes and what object it is about.

**Table 2.** Rows for Proposition 2.1 and Theorem 3.1 now name the bridge. The coverage sentence in Section 8 adds the rules-to-polyhedron step to the list of what is not formalised. The report's warning not to describe the whole paper as formally verified is already the note's position and is kept.

**Acknowledgements.** Nine rounds; the request for the bridge is credited to this round.

## Not changed

Everything mathematical. No script changes. Figure 1 and its qualifier unchanged.
