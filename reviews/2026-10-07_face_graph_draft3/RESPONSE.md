# Response to the consolidated review of the face-graph note, draft 3 (7 October 2026)

Review: `Draft3_Consolidated_Referee_Report.pdf` (nine pages) with `run_all.py` and five checkers; author-script execution logs, the negative test confirming the harness fix, the strict-tolerance rerun and the regenerated certificate are in `author_evidence/`. Recommendation: minor revision, with a favourable assessment of the standalone mathematics. The review also assesses a separate referee report that had been supplied to the reviewer and sorts its requests into retained, already satisfied, and optional.

| Finding | Action in draft 4 |
|---|---|
| §6.1 gives the hexagon centre as 3h/2; in the coordinates of §2 it is h (the plane h·x = 3 contains h since h·h = 3). | Corrected. Coordinate error only; incidence rules and phases were unaffected. |
| Checks advertised at 1e-12 used `np.allclose(..., atol=1e-12)` with NumPy's default relative tolerance; the strict rerun (rtol=0) also passes. | All eight such calls now set `rtol=0` (revision 3 of `verify_face_graph_paper_2026-10-06.py`); the paper states "absolute tolerance 1e-12 with relative tolerance 0". |
| The tag `face-graph-note-v3` named in §8 was not publicly retrievable on 7 October. | Correct; the tag had not been pushed. Draft 4 names `face-graph-note-v4`, which is pushed with this commit and carries the commit hash in its message. |
| "Every stated fact is checked by two accompanying test scripts" is too broad. | Replaced by the reviewer's precise coverage sentence in the abstract and §8; the auditors' checkers and sweep data are acknowledged and filed under `reviews/` with `run_all.py` as entry point. |
| Add a short existence/uniqueness proof for the magnetic connection (gauge classification). | Added as Proposition 6.1 with the reviewer's constructive proof, with Reff (2012) and Lange, Liu, Peyerimhoff, Post (2015) cited. |
| Prove that the compensated rotations are monomial. | The reviewer's argument added to §6.1, with the generator formulas for r and t (checked exactly here before inclusion). |
| Give the elongated-dodecahedron graph with indexed incidences and a short proof of the Fedorov table. | Appendix A added, reproducing the reviewer's self-contained proofs of the first four rows, with attribution; the elongated graph is defined by indexed incidences. |
| Triangle count: say why there are exactly 24; make the 4-cycle substitution explicit. | Done in the proof of Proposition 2.1 (tr A⁴ = 1032, Σd² = 384, Σd = 72). |
| Figure 1: state the eigenvalue-ordering convention; segments are guides. | Caption now says the eigenvalues are sorted at each integer q and the k-th smallest are joined; segments are visual guides, not analytic branches. |
| Shorten the abstract; "irreducible decomposition of each eigenspace" rather than "isotypic type". | Abstract rewritten and shortened accordingly. |
| Requests in the supplied report already satisfied by draft 3 (eight items) and optional items (character table, weighted extension, DOIs for every reference, AI-process questionnaire). | Left as the reviewer sorted them; not treated as acceptance conditions. |

Nothing in this review bears on UFFT's physics claims, and the note continues to make none.
