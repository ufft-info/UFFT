# Clean-environment replay of commit cfe80fc (seven-file Lean tree), Python runner and Lean build

Author-side receipt (not an independent replay). Written 10 October 2026 after the commit that added `Fedorov.lean` and `Support.lean` to the Lean project. It repeats the v10 receipt (`CLEAN_RUN_face-graph-note-v10.md`) at the new commit; the manuscript is unchanged (Draft 10 stands) and this commit carries no tag.

## Environment

Fresh `git clone https://github.com/ufft-info/UFFT` into an empty directory in a cloud Linux container (Anthropic Cowork sandbox), `git checkout cfe80fc`, HEAD `cfe80fc3ff8865488d22c1e2d7edab4a02e10f22` (`git describe`: face-graph-note-v10-2-gcfe80fc). No files from the author's machine were copied in. Python 3.11.15 with the `verification/requirements.txt` packages (numpy 2.4.4, sympy 1.14.0, scipy 1.17.1, matplotlib 3.10.9) and the optional networkx 3.6.1. Lean toolchain `leanprover/lean4:v4.34.1` via elan; Mathlib at the pinned revision `d13f23b723b8a846827a245b89c10fc7d3f11612` from `lake-manifest.json`, with its build cache fetched by `lake exe cache get`.

## Python runner

`cd verification && python3 run_face_graph_checks.py` (no `-O`). Exit status 0; 70 lines marked PASS, 0 marked FAIL; final line `ALL FACE-GRAPH CHECKS PASSED: author scripts, figure route, and every reviewers' suite against the fresh certificate.` Regenerated `flux_gauge_certificate.json` byte-identical to the committed file (SHA-256 b0fb72eb70632086…); regenerated `face_graph_magnetic_sweep.csv` identical to the committed file after line-ending normalisation (3e182f06a5def82e…); the figure PDF differs only in matplotlib's creation-date metadata, as at v8 and v10. The runner output is identical in PASS count and FAIL count to the v10 replay; nothing in the Python side changed in this commit.

## Lean build

`cd verification/lean/FaceGraph && lake exe cache get && lake build FaceGraph.<module>` for the seven modules in turn (Theorem31, Theorem51, HalfFlux, QuarterFlux, Graph, Fedorov, Support), each with exit status 0, then `lake build`: exit status 0, `Build completed successfully (1838 jobs)`. The `#print axioms` output for every main theorem, verbatim from the build log:

    'charpoly_Lfin'      depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_conj'             depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_sq_conj'          depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_one_in_E7'        depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Sfin'      depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_D6'        depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Lgraph'    depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Sgraph'    depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Dgraph'    depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_LcubeG'    depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_LprismG'   depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_LrhombicG' depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_LelongG'   depends on axioms: [propext, Classical.choice, Quot.sound]
    'weights'            depends on axioms: [propext, Classical.choice, Quot.sound]
    'vT1u_eig'           depends on axioms: [propext, Classical.choice, Quot.sound]
    't1u_weight'         depends on axioms: [propext, Classical.choice, Quot.sound]
    't1u_weights_sqrt'   depends on axioms: [propext, Classical.choice, Quot.sound]

No `sorry`, no `native_decide` anywhere in the build log. Serial per-module build as the README instructs; `Support.lean` is the slowest module (about four minutes, the row-by-row `vT1u_eig` and the fourteen-term trace sums).

## Source hashes at the commit (SHA-256, first 16 hex)

    Theorem31.lean    bf4be58b7a1a0390
    Theorem51.lean    a22ff77f9a1233eb
    HalfFlux.lean     cff317492d630a18
    QuarterFlux.lean  c659fecbc91e66bd
    Graph.lean        61842933f67fd38b
    Fedorov.lean      8f646c043d96c8c5
    Support.lean      4f752d6418cc6df4

The first five are unchanged from the v10 receipt.

## What this does and does not establish

The commit runs from a clean checkout with the pinned requirements, reproduces the committed certificate and data, and the seven-file Lean project builds with the stated axiom lists. Run by the author's assistant, not by a third party: a receipt, not independent verification. The manuscript's coverage statement (Draft 10, Section 8 and Table 3) still lists Proposition 4.1 and the Fedorov table as not formalised; that text is updated at the venue revision.
