# UFFT Paper #72 — Dirac Operator, Generation Count, Chirality Structure, and the m₃ Integer

**Unified Foam Field Theory — Part LXXII**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #72 of 72 |
| Framework | v10 |
| Status | T72.1, T72.2, T72.3a are theorems with proofs supported by `verify_Paper72_Oh_irreps.py`. T72.3b (physical chirality identification) is a conjecture with V10 heuristic support (T_2g hex-only necessary condition under the standard SM embedding). T72.4 (integer triple (11, 13, 4) in the m₃ exponent) is the best-matching primitive triple under a principled search-space ansatz, pending a closed-form counting rule. |
| Tier | T72.1, T72.2, T72.3a: Tier 1 (theorems). T72.3b: Tier 2 (conjecture with V10 heuristic support). T72.4: Tier 2 (best-match primitive triple in a principled search space). |
| DOI | 10.5281/zenodo.19658759 |
| Verification | `/verification/verify_Paper72_Oh_irreps.py` — V1–V11, reproduces every numerical claim from raw cell integers; runs in under 10 seconds. |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, Dirac operator on a graph, face Laplacian, O_h representation theory, T₁u multiplicity, canonical pairing, Schur's lemma, face-type orbit splitting, Pauli matrix structure, chirality, neutrino mass m₃

---

## Abstract

Paper #48 identifies the fermion sector of the Standard Model with the low-lying spectrum of `S = ψ† L_T ψ` built from the face Laplacian L_T of the truncated octahedron and a 14-component field ψ. Section 5.2 of Paper #48 quotes the heaviest neutrino mass `m₃ = m_e · exp[−(11 + 13√17)/4]` as a "sector-specific identification." This paper upgrades that identification to derivation at the Dirac-operator and multiplicity level, addressing four questions:

(i) does a canonical foam-cell Dirac operator exist?
(ii) does the three-generation count follow from the cell's symmetry?
(iii) does the chirality-mixing mass operator on the T₁u sector take a specific 2×2 Pauli-matrix form forced by the cell's geometric structure?
(iv) is the integer pair (11, 13) in the m₃ exponent geometrically selected rather than fitted?

The results:

- **T72.1** (existence of a canonical foam-cell Dirac operator `D_F` with `D_F² = L_T`, self-adjoint, commuting with the permutation representation of O_h): theorem with proof. Verified by V1, V3, V4 of `verify_Paper72_Oh_irreps.py`.
- **T72.2** (three-generation count = T₁u multiplicity, derived by O_h character theory): theorem with proof. Verified by V2, V5.
- **T72.3a** (chirality-mixing operator on T₁u sector = `−2 σ_x` in the canonical face-type basis): theorem with proof. The canonical face-type orbit splitting `L_T = L_diag + L_off` yields `L_off|_{T₁u} = −2 σ_x` exactly, uniform across all three T₁u generation copies. Verified by V8 to machine precision.
- **T72.3b** (physical chirality identification hex ↔ L, sq ↔ R): conjecture with V10 heuristic support. V10 verifies the orbit-restricted irrep decompositions `hex (8-dim) = A_1g ⊕ T_1u ⊕ T_2g ⊕ A_2u` and `sq (6-dim) = A_1g ⊕ E_g ⊕ T_1u`, showing that T_2g lives only on the hex-orbit. In the standard SM embedding where SU(2)_L adjoint ↔ T_2g, this forces hex-T₁u to form SU(2)_L doublets (left-handed) and sq-T₁u to be an SU(2)_L singlet (right-handed), a geometric necessary condition for T72.3b.
- **T72.4** (integer triple (11, 13, 4) in the m₃ exponent): best-match primitive triple in a principled search space. V9 surfaces three natural cell-integer decompositions of (11, 13). V11 performs an exhaustive search over 12,800 integer triples `(a, b, c)` with `a, b ∈ [1, 40]`, `c ∈ {1, 2, 3, 4, 6, 8, 12, 16}` and shows that (11, 13, 4) is the single primitive (gcd = 1) triple within 1 sigma of the PDG 2024 reference `m₃ = 49.50 meV`, ranked #1 by rel-err accuracy (0.019%) across the full 4-sigma window. The 1-sigma match count is consistent with the uniform-prior expectation of ~1.4 primitive matches, so V11 provides a principled search-space characterization rather than statistical evidence against random placement. No closed-form counting rule is derived.

Three of five sub-claims are theorems. T72.3b rests on a geometric necessary condition (V10) pending substantiation of the SU(2)_L-↔-T_2g embedding. T72.4 has a characterized best-match identification (V11) pending a closed-form counting rule and resolution of the PDG-vs-NuFIT convention dependence. Both open items are well-defined closed-form problems with documented candidate paths.

---

## 1. Context

See Paper #48 §§1–5 for the framework setup. UFFT's master equation `λ² − 9λ + 16 = 0` has roots `r₁ = (9 − √17)/2 ≈ 2.438` and `r₂ = (9 + √17)/2 ≈ 6.562`, each appearing with multiplicity 3 in the T₁u block of the O_h decomposition of the face Laplacian L_T of the truncated octahedron. Paper #48 identifies the T₁u multiplicity with three fermion generations and the pair (r₁, r₂) with the eigenvalues of a chirality-discriminating operator on each generation copy.

This paper builds the foam-cell Dirac operator `D_F` whose square is L_T, derives the three-generation count from O_h character theory, characterises the chirality-mixing operator on the T₁u sector as `−2 σ_x` in the canonical face-type basis, and analyses the integer triple `(11, 13, 4)` appearing in the m₃ exponent of Paper #48 §5.2. The companion script `verify_Paper72_Oh_irreps.py` reproduces every numerical claim from raw cell integers and the master equation in under ten seconds.

---

## 2. Setup: Foam Graph, Face Laplacian, and O_h Action

Let `G = (V_F, E_F)` be the face adjacency graph of the truncated octahedron: `|V_F| = 14` faces (6 square `S₀…S₅`, 8 hexagonal `H₀…H₇`); `|E_F| = 36` face-sharing adjacencies, distributed as 12 hexagon–hexagon + 24 hexagon–square + 0 square–square. Let `A` be the 14×14 adjacency matrix, `D = diag(6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4)` the degree matrix (hexagons have 6 neighbours, squares have 4), and `L_T = D − A` the face Laplacian.

**Symmetry action.** The octahedral symmetry group O_h has order 48 and acts on V_F by permuting faces. This action preserves the partition of V_F into the hex-orbit (8 faces) and the sq-orbit (6 faces), these are the two distinct O_h orbits on V_F, and no group element mixes them. The induced 14-dimensional permutation representation `ρ: O_h → GL₁₄(R)` is constructed explicitly in V2 of `verify_Paper72_Oh_irreps.py`.

**Spectrum of L_T** (V1 pass). The eigenvalues of L_T are
`{0, r₁, r₁, r₁, 4, 4, r₂, r₂, r₂, 7, 7, 7, 7, 9}`
with `r_{1,2} = (9 ∓ √17)/2`. Reproduction error `< 10⁻¹⁰` from raw double-precision `numpy.linalg.eigh`.

**Irrep decomposition** (V2 pass, proven by character orthogonality). The 14-dim permutation representation decomposes as
`ρ = 2 A_1g ⊕ E_g ⊕ 2 T_1u ⊕ T_2g ⊕ A_2u`
with dimensions `2·1 + 1·2 + 2·3 + 1·3 + 1·1 = 14`. The A_1g appears twice (hex-constant ⊕ sq-constant). The T_1u appears twice (one copy from hex-T₁u, one from sq-T₁u; mixed by L_T). All other irreps appear with multiplicity one.

V2 computes the character of ρ on each of the 10 O_h conjugacy classes and applies the orthogonality relation `m_Γ = (1/|G|) Σ_c |c| χ_ρ(c) χ_Γ(c)` to get the multiplicities above. All multiplicities come out to integer values within numerical roundoff (< 10⁻⁹).

---

## 3. Theorem T72.1 — Canonical Foam-Cell Dirac Operator

**Theorem T72.1.** There exists a linear operator `D_F: C¹⁴ → C¹⁴` satisfying:

(i) `D_F² = L_T` on the non-kernel subspace of L_T.
(ii) `D_F = D_F†` (self-adjoint).
(iii) `D_F` commutes with the permutation representation of O_h, block-by-block in the irrep decomposition of ρ.
(iv) The construction is canonical up to a choice of sign on each non-kernel eigenspace; demanding positivity on the spectral square root fixes a canonical choice.

Moreover, the T_1u sector of `D_F` admits a canonical pairing between the two T_1u copies (one supported primarily on hexagons, one on squares) via the off-diagonal L_T block connecting hex and sq faces. Schur's lemma makes this pairing unique up to scalar; eigenvalue matching `D_F² = L_T` fixes the scalar to the pair `(√r₁, √r₂)`. The 2×2 block in the canonical (hex-T_1u, sq-T_1u) basis is
`L_T|_{T_1u} = [[5, −2], [−2, 4]]`
with trace 9 = r₁ + r₂ and determinant 16 = r₁ r₂ (Vieta identities of the master equation). Verified by V3 of `verify_Paper72_Oh_irreps.py` to 10⁻¹⁵ precision.

**Proof.** Construct `D_F := Σ_{λ_k ≠ 0} +√λ_k · P_k`, where `P_k` is the orthogonal projector onto the eigenspace of L_T at eigenvalue λ_k. Positivity of L_T (V1) guarantees each non-kernel eigenvalue has a real positive square root, giving (i). Self-adjointness (ii) is inherited from self-adjointness of each `P_k`. Orthogonality of eigenspaces across distinct irreps (a consequence of L_T commuting with ρ and Schur's lemma applied to the O_h action) gives (iii). The 2^6 = 64 sign choices reduce to two canonical ones (D_F and −D_F, related by the chirality involution γ_F discussed in §5) once positivity on each non-kernel block is imposed.

The 2×2 block structure is computed in V3. The hex-T_1u basis is `{(1/√8) Σ_i s_k^{(i)} e_{H_i} : k = 1, 2, 3}` where `s_k^{(i)}` is the k-th component of the i-th hexagonal normal in `(±1, ±1, ±1)`. The sq-T_1u basis is `{(1/√2)(e_{S_{axis=k,+}} − e_{S_{axis=k,−}}) : k = 1, 2, 3}`. Both are O_h-equivariant by the T_1u-transformation-law of (x, y, z) under rotations and inversions. The matrix elements `<hex_x|L_T|hex_x> = 5`, `<hex_x|L_T|sq_x> = −2`, `<sq_x|L_T|sq_x> = 4` follow by direct evaluation (24 hex-sq edges projected to T_1u contribute the off-diagonal −2; hex degree 6 minus the hex-hex T_1u-projected adjacency 1 gives 5; sq degree 4 with no sq-sq adjacency gives 4). The Vieta identities `5 + 4 = 9` and `5·4 − 2² = 16` are exact. ∎

**Remark.** The canonical pairing in (iv) is what makes `D_F` a *Dirac* operator rather than just any square-root of L_T: the pairing asserts that the two T_1u copies are related by the graph-geometric off-diagonal block of L_T, and Schur's lemma supplies uniqueness. This off-diagonal block is the precise object whose Pauli structure is characterised in T72.3.

**Remark on the BCC continuum limit.** Paper #48 §6 constructs a Bloch-momentum extension of L_T to a BCC sublattice of foam cells. Within each Bloch unit cell, the Dirac operator `D_F(k)` acquires a k-dependent phase but its spectrum at k = 0 coincides with the single-cell `D_F` of this theorem. Continuum-limit extension is Paper #48's responsibility, not Paper #72's. This paper's Dirac operator is explicitly the single-cell operator.

---

## 4. Theorem T72.2 — Three-Generation Count From O_h Representation Theory

**Theorem T72.2.** The three-generation count of Standard Model fermions, identified with the multiplicity of T_1u in the face Laplacian decomposition, follows directly from O_h character theory and does **not** require a Brillouin-zone doubler count.

**Precise statement.** Let ρ be the 14-dimensional permutation representation of O_h on the face set V_F of the truncated octahedron. Let m_Γ denote the multiplicity of irrep Γ in ρ, computed by the standard character-orthogonality relation
`m_Γ = (1/|O_h|) Σ_{c ∈ classes} |c| χ_ρ(c) χ_Γ(c)`
where |O_h| = 48 and the sum ranges over the 10 conjugacy classes of O_h. Then:
- `m_{A_1g} = 2` (one hex-constant mode, one sq-constant mode)
- `m_{E_g} = 1` (supported on squares)
- `m_{T_1u} = 2` (hex-T_1u and sq-T_1u, the object of T72.3)
- `m_{T_2g} = 1` (supported on hexagons)
- `m_{A_2u} = 1` (supported on hexagons)

with total dimension `2·1 + 1·2 + 2·3 + 1·3 + 1·1 = 14 = dim ρ`.

**The three-generation count is `dim(T_1u) = 3`**, the dimension of each T_1u copy. The multiplicity `m_{T_1u} = 2` supplies the two chirality partners. The total fermion count is `m_{T_1u} · dim(T_1u) = 2 · 3 = 6` internal degrees of freedom, matching (3 generations) × (2 chiralities).

**Proof.** Direct character computation, verified by `verify_Paper72_Oh_irreps.py` V2. Construct the 48-element O_h explicitly by closure under the generators `{R_x(90°), R_y(90°), R_z(90°), inversion}`; partition into conjugacy classes by the quadruple (element order, 3×3-matrix trace, 3×3-matrix determinant, 14×14-permutation-matrix trace); compute the character `χ_ρ(c) = Tr(ρ(g)) = #fixed faces under g`; apply character orthogonality against the standard O_h character table. Character orthogonality is an exact algebraic identity in finite-group representation theory; the script confirms numerical identity to better than 10⁻⁹. ∎

**Remark on Nielsen–Ninomiya.** The three-generation count is *not* a Nielsen–Ninomiya doubler-count result. The Nielsen–Ninomiya theorem counts zero modes of a Dirac operator in momentum space on a Bravais lattice; the foam-cell `D_F` has exactly one zero mode (the A_1g(0) mode, identified with the Higgs at the relevant scale). The **nonzero** T_1u modes at eigenvalues `√r₁` and `√r₂` are not doublers in the Nielsen–Ninomiya sense, they are massive propagating modes. The three-generation count comes from the dimension of the T_1u irrep itself, a symmetry-protected representation-theoretic datum, not from a BZ momentum enumeration.

**Connection to Paper #48.** Paper #48 §5.2's identification "T_1u multiplicity ↔ three generations" is now derived, not asserted, by T72.2.

---

## 5. Theorem T72.3 — Pauli Structure of the Chirality-Mixing Operator on T_1u

This section characterises the chirality-mixing operator on the T_1u sector of L_T. The canonical face-type orbit splitting `L_T = L_diag + L_off` (the unique decomposition of L_T with respect to the two O_h orbits on V_F (hex-orbit and sq-orbit)) yields `L_off|_{T_1u} = −2 σ_x` exactly in the canonical (hex-T_1u, sq-T_1u) basis, uniform across the three T_1u generation copies. This establishes T72.3 in its geometric form. The physical identification of (hex, sq) orbits with chirality is treated as a separate conjecture, supported by the orbit-restricted irrep decomposition derived in §5.2.

### 5.1. Geometric Theorem (T72.3a, Theorem)

**Theorem T72.3a (geometric form).** Let `L_T = L_diag + L_off` be the canonical decomposition of the face Laplacian with respect to the O_h-orbit partition `V_F = (hex-orbit) ⊔ (sq-orbit)`, where:
- `L_diag` retains all matrix elements of L_T within each orbit (the hex-hex 8×8 block and the sq-sq 6×6 block);
- `L_off` retains all matrix elements of L_T between orbits (the hex-sq 8×6 block and its transpose).

Both `L_diag` and `L_off` are O_h-equivariant operators on `C¹⁴` because each orbit is an O_h-invariant subset of V_F. Their projections onto each T_1u copy in the canonical (hex-T_1u, sq-T_1u) 2×2 basis (per generation index k = 1, 2, 3) are:
`L_diag|_{T_1u, 2×2} = diag(5, 4)`
`L_off|_{T_1u, 2×2} = −2 σ_x`
where `σ_x = [[0, 1], [1, 0]]`. The Pauli structure of `L_off` is uniform across the three T_1u generation copies: in the 6-dimensional T_1u sector with basis (hex-T_1u_x, hex-T_1u_y, hex-T_1u_z, sq-T_1u_x, sq-T_1u_y, sq-T_1u_z), `L_off` is block-anti-diagonal with hex→sq block equal to `−2 · I₃`.

**Proof.** Existence and uniqueness of the orbit-splitting decomposition follow from the orbit partition itself: any matrix on a graph with vertex partition `V = V₁ ⊔ V₂` decomposes uniquely as `M = M_diag + M_off` where `M_diag` is supported on `V₁ × V₁ ∪ V₂ × V₂` and `M_off` on the cross blocks. O_h-equivariance of each piece follows from O_h-invariance of the partition: for any `g ∈ O_h`, `ρ(g) M_diag ρ(g)⁻¹` has support on `(g·V₁) × (g·V₁) ∪ (g·V₂) × (g·V₂) = V₁ × V₁ ∪ V₂ × V₂` (since g preserves each orbit), so `ρ(g) M_diag ρ(g)⁻¹ = M_diag(g)` is itself an orbit-diagonal matrix; similarly for `M_off`.

The 2×2 projections are computed in V8 of `verify_Paper72_Oh_irreps.py`:
- `<hex_T_1u_x | L_diag | hex_T_1u_x> = 5` (hex degree 6 minus the T_1u-projected hex-hex adjacency 1)
- `<hex_T_1u_x | L_diag | sq_T_1u_x> = 0` (L_diag has no hex-sq matrix elements by construction)
- `<sq_T_1u_x | L_diag | sq_T_1u_x> = 4` (sq degree 4 minus the T_1u-projected sq-sq adjacency 0)
- `<hex_T_1u_x | L_off | hex_T_1u_x> = 0` (L_off has no hex-hex matrix elements)
- `<hex_T_1u_x | L_off | sq_T_1u_x> = −2` (the 24 hex-sq adjacencies of L_T = D − A contribute `−1` each in A; their T_1u projection sums to −2 in this basis)
- `<sq_T_1u_x | L_off | sq_T_1u_x> = 0` (no sq-sq matrix elements in L_off)

Thus `L_diag|_{T_1u, 2×2} = [[5, 0], [0, 4]] = diag(5, 4)` and `L_off|_{T_1u, 2×2} = [[0, −2], [−2, 0]] = −2 σ_x`.

The uniformity across the three generation copies (V8 final block) follows from O_h-equivariance: the T_1u irrep on each orbit is 3-dimensional, the off-diagonal coupling matrix in the 6D T_1u sector commutes with the diagonal action of `O_h` on the (x, y, z) generation labels, and Schur's lemma applied to the irreducible action of the rotation subgroup on each generation index forces the hex→sq coupling to be a scalar multiple of the identity matrix `I₃`. The scalar is fixed to −2 by V8's explicit numerical computation. Reproduction error 4.4 × 10⁻¹⁶, within machine precision. ∎

**Remark.** `L_off` is the unique non-trivial O_h-equivariant linear combination of L_T components that vanishes on the diagonal hex-hex and sq-sq blocks. Its T_1u 2×2 projection has the σ_x form *because* the (hex, sq) basis is canonical (an O_h-orbit basis) and *because* the T_1u multiplicity is exactly 2 (one copy per orbit), forcing any off-diagonal O_h-equivariant operator to have rank-1 σ_x block structure on T_1u up to scalar. Schur's lemma is the key abstract input.

### 5.2. Physical Chirality Identification (T72.3b, Conjecture — with V10 heuristic support)

**Conjecture T72.3b (chirality identification).** Identify the two T_1u multiplicity copies (one supported on the hex-orbit, one on the sq-orbit) with left-handed and right-handed chiralities of Standard Model fermions:
- hex-orbit ↔ left-handed (SU(2)_L doublet)
- sq-orbit ↔ right-handed (SU(2)_L singlet)

Under this identification, `L_off|_{T_1u} = −2 σ_x` is the chirality-mixing Dirac mass operator (off-diagonal in the chirality basis = (hex-orbit, sq-orbit) basis). The eigenvalues `r_1, r_2` of `L_T|_{T_1u}` are then the squared Dirac mass eigenvalues per generation, with `r_1 < r_2` reflecting the asymmetry between the two chirality sectors.

**Heuristic support from V10 (orbit-restricted irrep decomposition).** The 14-dim face permutation representation `ρ` decomposes as `ρ = 2 A_1g ⊕ E_g ⊕ 2 T_1u ⊕ T_2g ⊕ A_2u`. Restricting to each O_h-invariant orbit separately:

- **hex-orbit (8-dim) = A_1g ⊕ T_1u ⊕ T_2g ⊕ A_2u**  (character-theoretic result, V10)
- **sq-orbit  (6-dim) = A_1g ⊕ E_g ⊕ T_1u**  (character-theoretic result, V10)

**Key asymmetry:** T_2g lives ONLY on the hex-orbit (multiplicity 1 in hex, 0 in sq).

In the standard Standard Model embedding where the SU(2)_L adjoint is identified with T_2g (the natural non-T_1u 3-dim irrep of O_h), this forces:

1. hex-T_1u can form SU(2)_L doublets by coupling to T_2g within the hex sector (via the O_h tensor product `T_1u ⊗ T_2g ⊃ T_1u` on the 8-dim hex rep).
2. sq-T_1u cannot couple to T_2g within its 6-dim sector. Hence sq-T_1u is an SU(2)_L singlet.
3. SM phenomenology: SU(2)_L doublets = left-handed; SU(2)_L singlets = right-handed. Therefore hex-T_1u ↔ left, sq-T_1u ↔ right.

**Status.** V10 establishes a **geometric necessary condition** for T72.3b in the standard SM embedding: the SU(2)_L adjoint structure is hosted only by the hex-orbit, so the opposite assignment (sq ↔ L, hex ↔ R) is ruled out by orbit geometry in that embedding. However, this is still not a forcing theorem because the identification "SU(2)_L adjoint ↔ T_2g" is itself an embedding ansatz that must be verified against other SM observables (for example CKM/PMNS hierarchy with δ_PMNS/δ_CKM = 3 = C_A, parity violation in β decay, or the V_e/V_b cosmological ratio).

The conjecture is **falsifiable**: any independent UFFT calculation that derives a chirality assignment from another corner of the framework can confirm or refute the (hex ↔ L, sq ↔ R) identification.

### 5.3. Why the Face-Type Splitting, Not a Uniform-Regge Torsion

A natural alternative candidate for the chirality-mixing operator is the uniform-Regge hex-hex torsion `T_hex` of Paper #28. V6 of the verification script computes its T_1u projection and shows `T_hex|_{T_1u} = [[1, 0], [0, 0]]`, scalar, not σ_x. The reason is geometric: `T_hex` is supported only on the hex-hex block, so its hex-sq off-diagonal vanishes by construction. `L_off`, by contrast, is supported precisely on the hex-sq block and carries the σ_x structure required for a Dirac mass coupling between the two T_1u chirality partners. The face-type splitting is the correct O_h-equivariant decomposition of L_T that isolates the chirality-mixing block.

### 5.4. Impact on Paper #48

Paper #48 §5.2's chirality-assignment component is derived as a theorem in its geometric form (T72.3a). The physical identification (T72.3b) remains a structural conjecture, supported by the V10 geometric necessary condition but not forced. The Dirac mass operator on the T_1u sector is `−2 σ_x` in the canonical face-type basis; the assignment of chirality labels to that basis is the remaining open component of §5.2.

---

## 6. T72.4 — The Integer Triple (11, 13, 4) in the m_3 Exponent: Best-Match Primitive Triple in a Principled Search Space

The m₃ formula `m₃ = m_e · exp[−(11 + 13√17)/4]` with integer triple `(a, b, c) = (11, 13, 4)` is not a closed-form theorem. V9 and V11 of the verification script together characterise it as the best-matching primitive triple in a principled search space (see §6.3 interpretation), rather than as either a closed-form derivation or a pure numerical coincidence.

### 6.1. V7: Numerical reproduction

V7 tabulates heat-kernel moments `Tr(L_T^n)` for `n = 1, …, 6` and confirms the target exponent: `(11 + 13·4.123)/4 = 16.150`, so `m_e · exp(−16.150) = 49.491 meV`, matching oscillation-data m_3 ≈ 49.50 meV (PDG 2024 NH convention, Δm²_32 ≈ 2.453·10⁻³ eV² with m_1 = 0) to 0.019%, or m_3 ≈ 50.26 meV (NuFIT 5.2 NH) to 1.53%. The accuracy claim "0.075%" in UFFT Framework v9 is consistent with the PDG 2024 convention.

### 6.2. V9: Three candidate geometric decompositions for (11, 13)

V9 searches cell-integer combinations that produce 11 and 13. Three natural decompositions surface:

**Candidate (A), Vieta-mixed decomposition.**
- `a = 3(r₁ + r₂) − r₁ r₂ = 27 − 16 = 11`
- `b = 3(r₁ + r₂) − F = 27 − 14 = 13`
where (r₁ + r₂, r₁ r₂) = (9, 16) are the Vieta data of the master equation and F = 14 is the dim of the face permutation rep.

**Candidate (B), Face-count-minus-k.**
- `a = F − C_A = 14 − 3 = 11`  (face count minus colour number)
- `b = F − 1 = 14 − 1 = 13`      (face count minus singleton)
Difference `b − a = C_A − 1 = 2`.

**Candidate (C), Non-T_1u spectrum-pair.**
- `a = λ_7 + λ_4 = 7 + 4 = 11`  (T_2g + E_g)
- `b = λ_9 + λ_4 = 9 + 4 = 13`  (top A_1g + E_g)
Both are two-term sums of integer eigenvalues in the non-T_1u sector.

No closed-form O_h-symmetry argument uniquely selects (A), (B), or (C).

### 6.3. V11: Direct enumeration and primitive-triple analysis

V11 performs an exhaustive search over integer triples `(a, b, c)` with `a ∈ [1, 40]`, `b ∈ [1, 40]`, `c ∈ {1, 2, 3, 4, 6, 8, 12, 16}` (12,800 total triples). The exponent `(a + b√17)/c` is invariant under common-factor rescaling `(a, b, c) → (ka, kb, kc)`, so the true count of distinct geometric identifications is the number of **primitive triples** with `gcd(a, b, c) = 1`.

**Result (primitive, against PDG 2024 m_3 = 49.50 meV):**

| Window | All triples | Primitive triples | Uniform-prior expectation |
|--------|-------------|-------------------|---------------------------|
| 1 sigma (0.5%) | 3 | **1** | ~1.4 |
| 2 sigma (1%)   | 4 | 2 | ~2.8 |
| 4 sigma (2%)   | 11 | 9 | ~5.6 |

Within 1 sigma of PDG 49.50 meV, exactly one primitive triple exists: **(11, 13, 4)**, the triple of the Paper #72 formula. The other two 1-sigma matches, `(22, 26, 8) = 2·(11, 13, 4)` and `(33, 39, 12) = 3·(11, 13, 4)`, are non-primitive rescalings giving the same exponent.

**Interpretation, what the data does and does not show.**

The uniform-prior expectation is ~1.4 primitive matches in the 1-sigma window; the observation is 1. This is consistent with chance under a uniform distribution, slightly below the uniform-prior expectation. The observation does not constitute statistical evidence against the null hypothesis of random integer-triple placement.

What V11 does establish:

1. **(11, 13, 4) is the single primitive match at 1-sigma.** Under a small-denominator ansatz `c ≤ 16` and integer bounds `a, b ∈ [1, 40]`, the search space contains exactly one primitive triple landing within 1 sigma of the PDG reference.
2. **(11, 13, 4) is the #1 ranked match by accuracy across the full 2% window.** Among 9 primitive matches within 4 sigma of PDG, (11, 13, 4) achieves the smallest relative error (0.019%).
3. **The match is convention-dependent.** Against NuFIT 5.2 NH (50.26 meV), (11, 13, 4) lands at 1.53% rel-err, outside 1 sigma. The 0.019% accuracy claim holds specifically against PDG 2024 NH (49.50 meV). UFFT Framework v9's quoted 0.075% accuracy is consistent with the PDG convention.

What V11 does not establish:

1. **Statistical evidence against accident.** The match count in the 1-sigma window is consistent with uniform-prior expectation; "sparseness" in the sense of observing fewer matches than chance predicts is not demonstrated.
2. **Uniqueness of the geometric identification.** (11, 13, 4) is the unique primitive 1-sigma match only under the specific search space (bounds on `a, b, c`; PDG convention; √17 as the specified surd). Varying these choices could change the match count.
3. **A closed-form counting rule.** V11 reports the empirical match distribution; it does not derive which `(a, b, c)` should be selected from first principles.

### 6.4. Status assessment

T72.4 is **upgraded** from "pure numerical identification" to **"best-match primitive triple in a principled search space"**. The upgrade rests on:

1. Three natural geometric decompositions of (11, 13) from cell integers (V9 candidates A, B, C).
2. (11, 13, 4) is the most accurate primitive triple in a 12,800-triple search, under a small-denominator ansatz, against the PDG 2024 convention.

What remains unfinished:

1. A closed-form rule that uniquely selects one of candidates (A), (B), (C) over the others.
2. A closed-form derivation of the denominator `c = 4` (candidates include `2·dim_chiralities = 4`, `λ_4 = 4`, `F_sq − 2 = 4`).
3. Resolution of the convention dependence between PDG 2024 and NuFIT 5.2 neutrino-mass references.

T72.4 is therefore not yet a theorem, and the V11 match-distribution analysis does not constitute statistical evidence against random placement. What V11 provides is a principled search-space characterization: under a defined ansatz, (11, 13, 4) is the best-matching primitive triple by accuracy, consistent with its role in the framework but not forced by sparseness.

**Impact on Paper #48.** Paper #48 §5.2's m_3 formula status is **upgraded** to "identification, best-match primitive triple in principled search space (V11), pending closed-form counting rule and convention-dependence resolution."

---

## 7. Summary: Status of Paper #48 §5.2 Components

| Component | Status | Evidence |
|-----------|--------|----------|
| Dirac operator exists | **Theorem (T72.1)** | Spectral square root + Schur's lemma; V1, V3, V4 |
| Generation count = 3 | **Theorem (T72.2)** | O_h character theory; V2, V5 |
| Chirality-mixing op = σ_x form | **Theorem (T72.3a)** | Face-type splitting `L_T = L_diag + L_off`; V8 to machine precision |
| Hex/sq ↔ L/R identification | **Conjecture with V10 heuristic support (T72.3b)** | Orbit-restricted irrep decomposition: T_2g hosts only on hex-orbit — geometric necessary condition under standard SM embedding; V10 |
| Integer triple (11, 13, 4) | **Best-match primitive triple in a principled search space (T72.4)** | Single primitive 1-sigma match in 12,800-triple exhaustive search against PDG 2024 m_3 = 49.50 meV (V11); match count (1) consistent with uniform-prior expectation of ~1.4, i.e. the result is a principled search-space characterisation rather than statistical evidence against random placement |

Closing the two remaining items at theorem level would require (i) substantiation of T72.3b, promotion of the SU(2)_L-↔-T_2g embedding from ansatz to derivation (for example via CKM/PMNS with δ_PMNS/δ_CKM = 3 = C_A, or via the V_e/V_b cosmological ratio, or from neutron-star Regge-torsion chirality), and (ii) a closed-form counting rule for T72.4 that uniquely selects one of candidates (A), (B), (C) of §6.2 and derives the denominator c = 4. Both items are well-defined open problems suitable for follow-up work.

---

## 8. Verification

Every numerical claim in this paper is verified by `/verification/verify_Paper72_Oh_irreps.py`, whose cold-run output reproduces:

- L_T spectrum to 10⁻¹⁰ precision (V1)
- O_h character decomposition to 10⁻⁹ precision via character orthogonality (V2)
- T_1u 2×2 block `[[5, −2], [−2, 4]]` to 10⁻¹⁵ precision, with Vieta-matching trace and determinant (V3)
- Canonical D_F via spectral square root, `||D_F² − L_T|| < 10⁻⁸` (V4)
- Generation count 3 = T_1u dimension (V5)
- Uniform-Regge hex-hex torsion `T_hex` projection onto T_1u 2×2 = `[[1, 0], [0, 0]]` (scalar, not σ_x, see §5.3) (V6)
- Heat-kernel moments Tr(L_T^n) for n = 1, …, 6 (V7)
- **Face-type splitting `L_T = L_diag + L_off`** with `L_diag|_{T_1u} = diag(5, 4)` and `L_off|_{T_1u} = −2 σ_x`, uniform across all three T_1u generation copies, machine-precision (4.4 × 10⁻¹⁶), the T72.3a geometric result (V8)
- T72.4 systematic decomposition search: three natural candidates (A: Vieta-mixed; B: F-minus-k; C: spectrum-pair) reproduce (11, 13); no unique forcing rule (V9)
- **Orbit-restricted irrep decomposition** (V10): hex-orbit (8-dim) = A_1g ⊕ T_1u ⊕ T_2g ⊕ A_2u; sq-orbit (6-dim) = A_1g ⊕ E_g ⊕ T_1u. Verifies T_2g multiplicity = 1 on hex, 0 on sq, the T72.3b heuristic support
- **Primitive-triple enumeration** (V11): 12,800-triple exhaustive search with `a, b ∈ [1, 40]`, `c ∈ {1, 2, 3, 4, 6, 8, 12, 16}`. Identifies (11, 13, 4) as the single primitive (gcd = 1) match within 1 sigma of PDG 2024 m_3 = 49.50 meV, ranked #1 by rel-err accuracy (0.019%) across the full 4-sigma match window. 1-sigma match count (1) is consistent with uniform-prior expectation (~1.4), the T72.4 best-match-triple characterisation

Script runs in under 10 seconds on a laptop. No free parameters. All inputs are cell integers `{F = 14, F_hx = 8, F_sq = 6, V = 24, E = 36, C_A = 3}` and the master equation `λ² − 9λ + 16 = 0`.

---

## 9. Open Work

| Item | Status | What's required to close |
|------|----------------|--------------------------|
| T72.1 | Theorem | Complete (this paper) |
| T72.2 | Theorem | Complete (this paper) |
| T72.3a (geometric) | Theorem | Complete (this paper) |
| T72.3b (chirality identification) | Conjecture + V10 heuristic support (T_2g hex-only) | Independent derivation promoting SU(2)_L-↔-T_2g from embedding ansatz to forced identification (from CKM/PMNS hierarchy with δ_PMNS/δ_CKM = 3 = C_A, V_e/V_b cosmological ratio, or neutron-star Regge-torsion chirality) |
| T72.4 | Best-match primitive triple in principled search space | Closed-form counting rule that selects one of candidates (A), (B), (C), derives the denominator c = 4, and resolves the PDG-vs-NuFIT convention dependence |

Three of five items are closed at theorem level; T72.3b has V10 heuristic support as a geometric necessary condition; T72.4 has V11 match-distribution analysis showing (11, 13, 4) is the best-matching primitive triple in the search space, the 1-sigma match count is consistent with uniform-prior expectation, so this is a principled characterization rather than statistical evidence against random placement. The remaining two closures are well-defined mathematical/physical problems suitable for follow-up papers.

---

## References

[1] Martin, L. (2026). Paper #48, The Standard Model From One Matrix. *Unified Foam Field Theory*. Zenodo DOI to follow.
[2] Martin, L. (2026). Paper #05, Face Laplacian Spectrum of the Truncated Octahedron. *Unified Foam Field Theory*. Zenodo DOI 10.5281/zenodo.19030062.
[3] Martin, L. (2026). Paper #28, Schwarzschild Metric and Regge Torsion Convention. *Unified Foam Field Theory*. Zenodo DOI pending.
[4] Nielsen, H. B. & Ninomiya, M. (1981). Absence of neutrinos on a lattice. *Phys. Lett. B* **105**, 219. (T72.2 is derived by O_h character theory directly and is not a Nielsen–Ninomiya doubler count; reference retained for the contrast discussed in §4.)
[5] Serre, J.-P. (1977). *Linear Representations of Finite Groups.* Springer. (Character orthogonality used in T72.2; Schur's lemma used in T72.1 and T72.3a.)
[6] Regge, T. (1961). General relativity without coordinates. *Nuovo Cimento* **19**, 558. (Regge angular-deficit torsion convention; used in V6's uniform hex-hex torsion construction. The σ_x structure of the chirality-mixing operator comes from the face-type orbit splitting of L_T itself, not from `T_hex`; see §5.3.)

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Paper #72 · DOI 10.5281/zenodo.19658759 · Priority Date: 20 February 2026*

*B + V = D*
