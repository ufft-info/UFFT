# Lean 4 proofs for the face-graph note

Machine-checked statements from "The face-adjacency graph of the truncated octahedron" (journal note, Draft 9). Every file ends with `#print axioms`; in all of them the list is `propext`, `Classical.choice`, `Quot.sound` only. No `sorry`, no `native_decide`: every matrix identity is decided by kernel reduction (`decide +kernel` on `Matrix.mulᵣ` / `Matrix.mulVecᵣ`), not by compiled evaluation.

| File | Statement in the note | What is checked |
|---|---|---|
| `FaceGraph/Theorem31.lean` | Theorem 3.1: det(x − Δ) = x(x−9)(x−7)⁴(x−4)²(x²−9x+16)³ | the full statement, for the explicit 14 × 14 integer Laplacian `Lfin` |
| `FaceGraph/Theorem51.lean` | Theorem 5.1 (1), (2), (4): K kills E_g, T_2g, A_2u; K² = −4 on T_1u; K² = −12 on the A_1g plane; K·1 lies in E_7 | on the explicit rational orbit basis `Pfin` of Theorem 3.1 (`K * Pfin = Pfin * Kb`, `K * K * Pfin = Pfin * Kb2`); the identification of that basis with the O_h isotypic components (Lemma 3.2) and part (3) (singular values between the irrational eigenspaces) are not formalised |
| `FaceGraph/HalfFlux.lean` | Theorem 6.4, q = 12: det(x − Δ₁₂) = (x−8)³(x−5)³(x−4)²(x−3)⁴(x²−13x+24) | the full statement, for the signless Laplacian `Sfin = D + A` (the all-negative gauge of the note) |
| `FaceGraph/QuarterFlux.lean` | Theorem 6.4, q = 6: det(x − Δ₆) = (x−9)(x−8)³(x−3)⁴(x²−9x+16)³; Proposition 6.5 (Gram identity) | the full statement, for the Gaussian-integer matrix `D6` of the note's gauge (B); `Q6 * P6 = diag(32, 8, …)` is the Gram identity on the Walsh/partner basis |

## Method

Each proof is the note's own argument. An explicit change of basis `P` (orbit sums, the E_g pair, the three T_1u pairs, the T_2g triple, the A_2u singlet; at q = 6 the Walsh vectors χ_S and their square partners B χ_S) conjugates the operator to a block diagonal of seven 2 × 2 blocks; `Matrix.charpoly_units_conj` gives invariance of the characteristic polynomial under conjugation, a short lemma gives the characteristic polynomial of a block diagonal matrix as the product of the blocks', and `Matrix.charpoly_fin_two` finishes each block. The matrix identities (`L * P = P * B`, `P * Q = 1`, `Q * P = 1`) are decided by kernel reduction.

At q = 6 the entries are Gaussian integers. A matrix over ℤ[i] is written as `ofRI R I` (real and imaginary integer parts), so that `ofRI_mul` turns each identity into two identities between integer matrices, which the kernel decides as before. `P6` is not unimodular (`Q6 * P6 = diag(32, 8, …)`), so the conjugation is carried out in the fraction field ℚ(i) (`FractionRing ℤ[i]`, nothing computed there) and pulled back to ℤ[i][x] by injectivity of `Polynomial.map`.

## Build

Requires [elan](https://github.com/leanprover/elan). Then, in this directory:

```
lake exe cache get     # downloads the Mathlib build cache (large, once)
lake build             # a few minutes; prints the axiom lists
```

Toolchain: `leanprover/lean4:v4.34.1`, Mathlib `v4.34.1` (pinned in `lake-manifest.json`).

## Not formalised

Proposition 6.2 (thirteen distinct spectra) rests on the third-moment identity tr Δ_q³ = 3264 − 144 cos(πq/12) for all 24 charges, which needs the cyclotomic phases e^{iπq/12}; Proposition 6.1 (spherical gauge classification) is a statement about all cellular embeddings in S²; the Fedorov table (Appendix A) and Proposition 4.1 (support weights) are the remaining finite targets. Table 2 of the note records, for each result, whether it is proof-assistant checked.
