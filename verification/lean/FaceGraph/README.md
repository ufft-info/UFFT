# Lean 4 proofs for the face-graph note

Machine-checked statements from "The face-adjacency graph of the truncated octahedron" (journal note, Draft 8).

| File | Statement | Status |
|---|---|---|
| `FaceGraph/Theorem31.lean` | Theorem 3.1: the Laplacian of Γ has characteristic polynomial x(x−9)(x−7)⁴(x−4)²(x²−9x+16)³ | checked by the Lean kernel; axioms used: `propext`, `Classical.choice`, `Quot.sound` only (`#print axioms` at the end of the file) |

The proof is the note's own argument: an explicit change of basis `Pfin` (orbit sums, the Eg pair, the three T₁u pairs, the T₂g triple, the A₂u singlet) conjugates the Laplacian `Lfin` to a block diagonal `Bfin` of seven 2 × 2 blocks; `Matrix.charpoly_units_conj` gives invariance under conjugation; a short lemma gives the characteristic polynomial of a block diagonal matrix as the product of the blocks'; `Matrix.charpoly_fin_two` finishes each block. The three matrix identities (`Lfin * Pfin = Pfin * Bfin`, `Pfin * Qfin = 1`, `Qfin * Pfin = 1`) are decided by kernel reduction (`decide +kernel` on `Matrix.mulᵣ`), not by compiled evaluation, so no `native_decide` axiom enters.

## Build

Requires [elan](https://github.com/leanprover/elan). Then, in this directory:

```
lake exe cache get     # downloads the Mathlib build cache (large, once)
lake build             # about a minute; prints the axiom list for charpoly_Lfin
```

Toolchain: `leanprover/lean4:v4.34.1`, Mathlib `v4.34.1` (pinned in `lake-manifest.json`).

## Scope

Only Theorem 3.1 is formalised. The quarter-flux factorisation (Theorem 6.4), the signless-Laplacian half-flux result and the thirteen-sector proposition (6.2, via the third-moment identity) are the next targets, in that order. Table 2 of the note records, for each result, whether it is proof-assistant checked; as of Draft 8 this row is the only one.
