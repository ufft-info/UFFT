# Clean-environment replay of tag face-graph-note-v10, Python runner and Lean build

Author-side receipt (not an independent replay). Written 9 October 2026 in response to R1 of the tenth review round. It repeats the v8 receipt at the current tag and adds the Lean build, which the v8 receipt did not cover.

## Environment

Fresh `git clone https://github.com/ufft-info/UFFT` into an empty directory in a cloud Linux container (Anthropic Cowork sandbox), `git checkout face-graph-note-v10`, HEAD `56f6bfd5f12dafaaa909e0a26d0309efafd47d01`. No files from the author's machine were copied in. Python 3.11.15 with the `verification/requirements.txt` packages (numpy 2.4.4, sympy 1.14.0, scipy 1.17.1, matplotlib 3.10.9) and the optional networkx 3.6.1. Lean toolchain `leanprover/lean4:v4.34.1` via elan; Mathlib at the pinned revision `d13f23b723b8a846827a245b89c10fc7d3f11612` from `lake-manifest.json`, with its build cache fetched by `lake exe cache get`.

## Python runner

`cd verification && python3 run_face_graph_checks.py` (no `-O`). Exit status 0; 70 lines marked PASS, 0 marked FAIL; final line `ALL FACE-GRAPH CHECKS PASSED: author scripts, figure route, and every reviewers' suite against the fresh certificate.` Regenerated `flux_gauge_certificate.json` byte-identical to the committed file (SHA-256 b0fb72eb70632086…); regenerated `face_graph_magnetic_sweep.csv` identical to the committed file after line-ending normalisation (3e182f06a5def82e…); the figure PDF differs only in matplotlib's creation-date metadata, as at v8.

## Lean build

`cd verification/lean/FaceGraph && lake exe cache get && lake build FaceGraph.<module>` for the five modules in turn (Theorem31, Theorem51, HalfFlux, QuarterFlux, Graph), then `lake build`. Exit status 0; `Build completed successfully (1836 jobs)`. The `#print axioms` output for every main theorem, verbatim from the build log:

    'charpoly_Lfin'   depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_conj'          depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_sq_conj'       depends on axioms: [propext, Classical.choice, Quot.sound]
    'K_one_in_E7'     depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Sfin'   depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_D6'     depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Lgraph' depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Sgraph' depends on axioms: [propext, Classical.choice, Quot.sound]
    'charpoly_Dgraph' depends on axioms: [propext, Classical.choice, Quot.sound]

No `sorry`, no `native_decide`. Peak memory for the serial build is under 6 GB; a parallel `lake build` of the five modules on an 8 GB machine is killed by the kernel, which is why the README says to build them one at a time.

## Source hashes at the tag (SHA-256, first 16 hex)

    Theorem31.lean    bf4be58b7a1a0390
    Theorem51.lean    a22ff77f9a1233eb
    HalfFlux.lean     cff317492d630a18
    QuarterFlux.lean  c659fecbc91e66bd
    Graph.lean        61842933f67fd38b

## What this does and does not establish

The tagged release runs from a clean checkout with the pinned requirements, reproduces the committed certificate and data, and the Lean project builds with the stated axiom lists. Run by the author's assistant, not by a third party: it is the receipt the review asked for, not independent verification.
