# Lean 4 proofs for the face-graph note

Machine-checked statements from "The face-adjacency graph of the truncated octahedron" (journal note, Draft 10). Every file ends with `#print axioms`; in all of them the list is `propext`, `Classical.choice`, `Quot.sound` only. No `sorry`, no `native_decide`: every matrix identity is decided by kernel reduction (`decide +kernel` on `Matrix.mulᵣ` / `Matrix.mulVecᵣ`), not by compiled evaluation.

| File | Statement in the note | What is checked |
|---|---|---|
| `FaceGraph/Theorem31.lean` | Theorem 3.1: det(x − Δ) = x(x−9)(x−7)⁴(x−4)²(x²−9x+16)³ | the full statement, for the explicit 14 × 14 integer Laplacian `Lfin` |
| `FaceGraph/Theorem51.lean` | Theorem 5.1 (1), (2), (4): K kills E_g, T_2g, A_2u; K² = −4 on T_1u; K² = −12 on the A_1g plane; K·1 lies in E_7 | on the explicit rational orbit basis `Pfin` of Theorem 3.1 (`K * Pfin = Pfin * Kb`, `K * K * Pfin = Pfin * Kb2`); the identification of that basis with the O_h isotypic components (Lemma 3.2) and part (3) (singular values between the irrational eigenspaces) are not formalised |
| `FaceGraph/HalfFlux.lean` | Theorem 6.4, q = 12: det(x − Δ₁₂) = (x−8)³(x−5)³(x−4)²(x−3)⁴(x²−13x+24) | the full statement, for the signless Laplacian `Sfin = D + A` (the all-negative gauge of the note) |
| `FaceGraph/QuarterFlux.lean` | Theorem 6.4, q = 6: det(x − Δ₆) = (x−9)(x−8)³(x−3)⁴(x²−9x+16)³; Proposition 6.5 (Gram identity) | the full statement, for the Gaussian-integer matrix `D6` of the note's gauge (B); `Q6 * P6 = diag(32, 8, …)` is the Gram identity on the Walsh/partner basis |
| `FaceGraph/Graph.lean` | Proposition 2.1 (adjacency rules), the gauge formula (B), and the three characteristic polynomials for the rule-built matrices | the bridge asked for by the ninth review round: the adjacency rules (a square `(a, σ)` is adjacent to the hexagons with `h_a = σ`; hexagons at Hamming distance one) and the gauge formula `B = (h_b − iσ h_c)/(1 − iσ)` are Lean functions on the vertex indices; `Lgraph_eq_Lfin`, `Sgraph_eq_Sfin`, `Dre_eq_D6r`, `Dim_eq_D6i` prove the rule-built matrices equal the literals (kernel evaluation on every index pair), so `charpoly_Lgraph`, `charpoly_Sgraph`, `charpoly_Dgraph` state the three theorems for the matrices defined by the rules. Not covered: that the rules describe the truncated octahedron and its plaquette holonomies (Proposition 2.1 and Section 6.1 by hand) |
| `FaceGraph/Fedorov.lean` | Table 2 rows 1–4 and Appendix A: the face-graph Laplacian polynomials of the cube x(x−4)³(x−6)², the hexagonal prism x(x−3)²(x−5)²(x−6)²(x−8), the rhombic dodecahedron x(x−2)³(x−4)³(x−6)⁵ and the elongated dodecahedron x(x−2)(x−4)²(x−6)³(x−8)(x²−10x+20)² | each graph is defined by its adjacency rule as the note states it (K_{2,2,2}; C₆ ∨ K̄₂; the line graph of the cube on the twelve cube edges; the H_i/T_i/B_i cycles with H_i ~ T_i, T_{i+1}, B_i, B_{i+1}); `lapOf` builds the Laplacian from the rule, `L*G_eq` proves it equal to a literal by kernel evaluation, and the polynomial follows by the Theorem 3.1 method with a rational change of basis to 2 × 2 blocks (diagonal blocks for the integer eigenvalues; the cyclic pair (v, Lv) for the irreducible quadratic of the elongated dodecahedron). The change-of-basis matrices come from `gen_fedorov.py` and are checked, not trusted. Fedorov's classification itself is a cited theorem, not formalised |
| `FaceGraph/Support.lean` | Proposition 4.1 (square weights): ω(E₀) = 3/7, ω(E₄) = 1, ω(E₇) = 1/7, ω(E₉) = 0, ω(E_{r₁,₂}) = (1 ± 1/√17)/2 | rational part (`weights`): explicit rational matrices `P0, P4, P7, P9` are symmetric idempotents with `Lfin * P = λ P` and traces 1, 2, 4, 1 (the multiplicities, so each is the orthogonal projector on the eigenspace, given that a symmetric matrix has eigenspace dimension equal to multiplicity, which is not re-proved); `PT` is the projector on the T_1u sector, `L² PT − 9 L PT + 16 PT = 0`, trace 6; the five are mutually orthogonal and sum to the identity; the weights tr(P_sq P)/tr(P) are 3/7, 1, 1/7, 0 and 1/2 for the T_1u sector as a whole. Irrational part: for every root λ of x² − 9x + 16 in any field, `vT1u λ = 4 s + (4 − λ) h` is an eigenvector of the 14 × 14 Laplacian (`vT1u_eig`, checked row by row), its square part has squared norm 32 and its hexagon part 8(4 − λ)², the weight 32/(32 + 8(4 − λ)²) equals 4/(4 + λ) on the roots (`t1u_weight`), and over a field with s² = 17 the roots are (9 ∓ s)/2 and 4/(4 + r₁) = (1 + 1/s)/2, 4/(4 + r₂) = (1 − 1/s)/2 (`t1u_weights_sqrt`). That the three T_1u pairs give the same weight (the O_h symmetry) is not re-proved; the note's proof uses one pair as here |

## Method

Each proof is the note's own argument. An explicit change of basis `P` (orbit sums, the E_g pair, the three T_1u pairs, the T_2g triple, the A_2u singlet; at q = 6 the Walsh vectors χ_S and their square partners B χ_S) conjugates the operator to a block diagonal of seven 2 × 2 blocks; `Matrix.charpoly_units_conj` gives invariance of the characteristic polynomial under conjugation, a short lemma gives the characteristic polynomial of a block diagonal matrix as the product of the blocks', and `Matrix.charpoly_fin_two` finishes each block. The matrix identities (`L * P = P * B`, `P * Q = 1`, `Q * P = 1`) are decided by kernel reduction.

At q = 6 the entries are Gaussian integers. A matrix over ℤ[i] is written as `ofRI R I` (real and imaginary integer parts), so that `ofRI_mul` turns each identity into two identities between integer matrices, which the kernel decides as before. `P6` is not unimodular (`Q6 * P6 = diag(32, 8, …)`), so the conjugation is carried out in the fraction field ℚ(i) (`FractionRing ℤ[i]`, nothing computed there) and pulled back to ℤ[i][x] by injectivity of `Polynomial.map`.

## Build

Requires [elan](https://github.com/leanprover/elan). Then, in this directory:

```
lake exe cache get     # downloads the Mathlib build cache (large, once)
lake build             # a few minutes; prints the axiom lists (build the modules one at a time on a machine with under 8 GB:
                       #   for m in Theorem31 Theorem51 HalfFlux QuarterFlux Graph Fedorov Support; do lake build FaceGraph.$m; done)
```

Toolchain: `leanprover/lean4:v4.34.1`, Mathlib `v4.34.1` (pinned in `lake-manifest.json`).

## Not formalised

The step from the adjacency rules and the gauge formula to the polyhedron and its plaquette holonomies is by hand (Proposition 2.1, Section 6.1). Proposition 6.2 (thirteen distinct spectra) rests on the third-moment identity tr Δ_q³ = 3264 − 144 cos(πq/12) for all 24 charges, which needs the cyclotomic phases e^{iπq/12}; Proposition 6.1 (spherical gauge classification) is a statement about all cellular embeddings in S². Lemma 3.2 (the identification of the basis with the O_h isotypic components) and Theorem 5.1 (3) are not formalised; Fedorov's classification is cited, not proved. Table 2 of the note records, for each result, whether it is proof-assistant checked.
