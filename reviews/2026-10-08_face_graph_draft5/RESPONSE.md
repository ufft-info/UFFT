# Response to the fifth review of the face-graph note (Draft 5), 8 October 2026

**Report:** `UFFT_Draft5_Evolved_Referee_Report_2026-10-08.pdf` (9 pages), filed verbatim. ReviewBot assessment of Draft 5, run as a bounded pilot of the reviewer's memetic review method. Recommendation: accept with minor revisions, subject to R1 to R6.

**Received:** the PDF only. The report's provenance section describes an accompanying ZIP (manuscript, check programs, Current/Pocket trace, fourteen task results, manifest); that archive was not received, so this folder has no `run_all.py` and `verification/run_face_graph_checks.py` skips it. If the archive arrives it will be added here unedited.

**Inspected state:** tag `face-graph-note-v5`, commit `adae53bbb6e87e3ac3f4422e1f77711f4edbe3c4`.

**Answered by:** Draft 6 of the note and tag `face-graph-note-v6` (the commit that adds this folder).

## Checked before adopting

Every claim in the report that could be checked was checked here first.

- **V2, spanning trees.** The exact cofactor of the Laplacian is 101,154,816, equal to 9 · 7⁴ · 4² · 16³ / 14 from the spectrum. Confirmed; now an EXACT check in `verify_face_graph_paper_2026-10-06.py` revision 5 and Remark 6.3 of Draft 6.
- **V3, fourth moment.** Exact enumeration of closed walks of length four in the integer-lift gauge gives the Laurent coefficients {z⁰: 25080, z^±1: −1536, z^±2: 144, z^±4: 24}, i.e. tr Δ_q⁴ = 25080 − 3072 cos(πq/12) + 288 cos(πq/6) + 48 cos(πq/3). Confirmed; checked numerically at every charge by the figure script (max residual 2.9e−11) and stated as a cross-check in Remark 6.3.
- **R1, negative test.** `np.allclose(8.00005, 8, atol=1e-9)` is True with the default relative tolerance and False with `rtol=0`. Reproduced.
- **R2, determinant.** The 23 × 23 free-edge minor has exact determinant +1 (SymPy, and Bareiss elimination in Python integers). Confirmed.
- **Category arithmetic.** The weighted contributions sum to 8.871, the stated Q, and the correctness average 9.00 follows from M1 to M4. No discrepancy.

## Findings and actions

| Finding | Bin | Action |
|---|---|---|
| R1 Five `np.allclose` calls in the figure script omit `rtol=0` | fixed | `plot_face_graph_flux_sweep.py` revision 2: every call sets `rtol=0`; holonomy and gauge comparisons state 1e−12. Section 8 of Draft 6 states absolute 1e−9 with relative tolerance 0. |
| R2 Unimodularity certified by a rounded float determinant | fixed | Revision 2 computes the determinant exactly by Bareiss elimination in Python integers (tested against SymPy on 300 random integer matrices, singular ones included); the check reads "exact integer determinant +1". |
| R3 Lift written (1, …, 1, −23) in Section 8, code uses (−23, 1, …, 1) | fixed | Draft 6 and the script docstring use (−23, 1, …, 1) and say the −23 belongs to plaquette 0, the first oriented plaquette in the certificate. (The vector is indexed by plaquettes, not faces; the report's "face 0" should read "plaquette 0".) |
| R4 "Independent audit" wording; earlier rounds not to be relabelled as memetic runs | fixed | Every "independent audit" in Sections 6, 6.1 and Appendix A now reads "review round". The acknowledgements say five rounds of AI-assisted review conducted by Prof. Moscato, that the fifth was a bounded pilot of his ReviewBot memetic method, and that no claim is made about the procedure behind the earlier rounds. The reviewer's checkers are described as written separately from the author's scripts. |
| R5 `requirements.txt` lacks matplotlib | fixed | matplotlib added to `verification/requirements.txt`; networkx listed as optional in a comment; the runner and Section 8 give one install command. (The report describes the archived file as NumPy, SymPy, NetworkX; the committed file listed NumPy, SymPy, SciPy, SciPy being used by other scripts in that directory. The missing matplotlib, which is the finding, holds either way.) |
| R6 No proof-checking disclosure | fixed | New "Proof status" paragraph and Table 2 in Section 8: no statement is machine-checked; each result is listed with how it is established and what computation corroborates it. |
| Optional 1: display the gauge law; define A_hs | done | Section 6 displays G Δ_θ G* = Δ_θ′ with θ′_jk = θ_jk + χ_j − χ_k; Section 2 defines A_hs = A_sh^T. |
| Optional 2: roadmap before the quarter-flux proof | done | Opening sentence of Section 6.1 lists the five steps. |
| Optional 3: cycle generation; fourth moment as a cross-check | done | Proof of Proposition 6.1 states the rank count 23 = 36 − 14 + 1 and Euler's formula; Remark 6.3 gives the fourth moment and the spanning-tree count as cross-checks, attributed. |
| Retractions (prism overbar; quarter-flux holonomy evidence) | noted | Nothing to change. |

## Runner and scripts

`verification/run_face_graph_checks.py` revision 2 matches every `reviews/*_face_graph_*/` folder rather than only those dated 2026-10-07, and skips a folder with no `run_all.py`. All three author scripts and every filed reviewers' suite pass against the freshly generated certificate.

No mathematical statement of the note changes. The note makes no physics claim, so none is affected.
