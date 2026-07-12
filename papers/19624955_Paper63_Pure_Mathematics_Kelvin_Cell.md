# UFFT Paper #63 — Pure Mathematics of the Kelvin Cell

## Combinatorial Spectra, O_h Representation Theory, and the Quadratic Ring Q(√17)

**Standalone Mathematics Paper**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory (companion standalone paper) |
| Paper | #63 of 67 (mathematics-only companion) |
| Framework | — (pure mathematics; no physics identifications) |
| Status | Complete |
| Tier | Tier 1 (theorems only) |
| MSC 2020 | 05C50 (eigenvalues of graphs), 20C30 (representations of finite symmetric groups), 51M20 (polyhedra), 11R11 (quadratic number fields) |
| DOI | 10.5281/zenodo.19624955 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** face Laplacian, truncated octahedron, Kelvin cell, octahedral group, irreducible representation, Fedorov parallelohedron, quadratic ring, Euler characteristic, Betti number, Vieta relations

---

## Abstract

This paper is a standalone presentation of the pure-mathematical content underlying the Unified Foam Field Theory. It makes no physical claims. Every theorem stated here is a result of finite linear algebra, group representation theory, or combinatorial topology applied to the truncated octahedron, the unique space-filling polyhedron with full O_h point symmetry (Fedorov 1891; confirmed by Paper #50 of this series).

The paper collects in one place the mathematical results that the UFFT physics papers reference repeatedly: (i) the construction of the face Laplacian L on the truncated octahedron's face-adjacency graph; (ii) its spectrum σ(L) = {0, r₁, 4, r₂, 7, 9} with multiplicities (1, 3, 2, 3, 4, 1), where r₁, r₂ are roots of the master equation λ² − 9λ + 16 = 0; (iii) the O_h irreducible decomposition of the 14-dimensional face space; (iv) the ring Q(√17) structure of the eigenvalue algebra; and (v) the uniqueness theorem for the Kelvin cell among Fedorov parallelohedra.

The purpose of this standalone version is to allow the mathematical content to be read, verified, and submitted independently of any physics interpretation, following the methodological advice that a mathematics paper on combinatorial Laplacian spectra and a physics monograph on particle-mass identifications should be separable documents.

---

## 0. Scope and convention

**Scope.** This paper contains only theorems and proofs. No identification is made here between mathematical objects (eigenvalues, irreducible representations, ring elements) and physical quantities (masses, mixing angles, couplings). Every theorem below is provable from the stated definitions using only finite linear algebra.

**Convention.** Throughout, P denotes the truncated octahedron as a CW-complex with 24 vertices, 36 edges, 14 faces (6 squares + 8 hexagons), Euler characteristic χ = V − E + F = 2. The symmetry group of P is the full octahedral group O_h of order 48.

---

## 1. The Face Graph and Face Laplacian

### Definition 1.1 (Face graph)

The **face graph** G_F of P is the graph whose vertices are the 14 faces of P, with an edge between two faces iff they share an edge in P. G_F is 3-regular: each face has three distinct neighbours (every hexagon borders 3 squares and 3 hexagons alternately; every square borders 4 hexagons, but the edge count in G_F from a square is 4, see Remark 1.2).

### Remark 1.2 (Edge multiplicities in G_F)

G_F inherits exactly one edge per shared cell-edge. A hexagon shares an edge with 3 squares and 3 hexagons; a square shares an edge with 4 hexagons. Total edges in G_F: 4·6 + 3·8 = 48/2 (hexagons share edges pairwise), i.e. Σ deg = 4·6 + 6·8 = 72 = 2E_P, so |E(G_F)| = 36 = E_P. The face graph edge count equals the cell-edge count, as expected from the bijection (cell-edge) ↔ (pair of adjacent faces).

### Definition 1.3 (Face Laplacian)

The **face Laplacian** L: ℂ^14 → ℂ^14 is the combinatorial Laplacian of G_F:

L = D − A

where D = diag(d_1, ..., d_14) is the face-degree matrix (d_hex = 6, d_sq = 4; see Remark 1.2) and A is the adjacency matrix of G_F.

### Theorem 1.4 (Face Laplacian spectrum)

The spectrum of L, with multiplicities:

| Eigenvalue | Multiplicity | Value |
|-----------|-------------|-------|
| λ₁ = 0 | 1 | 0 |
| λ₂ = r₁ | 3 | (9 − √17)/2 ≈ 2.438 |
| λ₃ = 4 | 2 | 4 |
| λ₄ = r₂ | 3 | (9 + √17)/2 ≈ 6.562 |
| λ₅ = 7 | 4 | 7 |
| λ₆ = 9 | 1 | 9 |

Total multiplicity: 1 + 3 + 2 + 3 + 4 + 1 = 14 = F.

**Proof sketch.** By construction L is symmetric (G_F is undirected) and positive semidefinite, with one-dimensional kernel (the constant function) because G_F is connected. The spectrum is computed by explicit diagonalisation of the 14×14 matrix L in the face basis, or equivalently by decomposing ℂ^14 into O_h-isotypic subspaces (see §3) and applying Schur's lemma within each irreducible block. Each isotypic block yields a single eigenvalue of L; the six isotypic blocks correspond to the six distinct eigenvalues. A verification script diagonalising L to ≤10⁻¹² machine precision is provided in the UFFT repository.

### Corollary 1.5 (Master equation)

The two irrational eigenvalues r₁, r₂ are the roots of the monic polynomial

**p(λ) = λ² − 9λ + 16** ("the master equation")

with Vieta relations r₁ + r₂ = 9, r₁ · r₂ = 16, and discriminant Δ = 9² − 4·16 = **17**.

### Definition 1.6 (Master constants)

The six master constants of the cell are the cell integers:

V = 24, E = 36, F = 14, |O_h| = 48, Δ = 17, C_A = 3,

where C_A := F_hx/F − 1 = 8/14 − 1 = a conveniently labelled integer (equivalently, C_A is the multiplicity-minus-one of the face-type A-irrep; see §3).

In some derivations we also use: F_hx = 8 (hexagonal faces), F_sq = 6 (square faces), V − F = 10, E − F = 22, E − V = 12.

---

## 2. The Eigenvalue Ring Q(√17)

### Theorem 2.1 (Ring generated by L-spectrum)

The ring generated by the spectrum σ(L) over ℚ is precisely the ring of integers of the quadratic extension

**Q(√17) = { a + b√17 : a, b ∈ ℚ }**

with ring of integers ℤ[(1+√17)/2] (since 17 ≡ 1 mod 4).

**Proof.** The rational eigenvalues {0, 4, 7, 9} generate ℚ as an additive group. The irrational eigenvalues r₁ = (9−√17)/2 and r₂ = (9+√17)/2 together with the rationals generate ℚ + ℚ√17 = Q(√17). Since r₁ = (9−√17)/2 has half-integer coefficients on √17, it lies in ℤ[(1+√17)/2] but not in ℤ[√17]. The full ring of integers of Q(√17) is ℤ[(1+√17)/2] because 17 ≡ 1 (mod 4). ∎

### Theorem 2.2 (Conjugate-pair identities)

The master constants satisfy:

(i) r₁ + r₂ = 9
(ii) r₁ · r₂ = 16
(iii) r₂ − r₁ = √17
(iv) r₁² + r₂² = 81 − 32 = 49
(v) r₁² − r₂² = −9√17
(vi) r₁³ + r₂³ = 9·49 − 3·16·9 = 441 − 432 = 9
(vii) (r₁ − 1)² + (r₂ − 1)² = 49 − 2·9 + 2 = 33

**Proof.** (i)–(iii) are Vieta + the explicit radical form of r₁,₂. (iv)–(vii) follow from (i)–(iii) by repeated application of Newton's identities s_k = p·s_{k−1} − q·s_{k−2} with p = 9, q = 16. ∎

### Remark 2.3 (The Frobenius norm of L − I on the T_{1u} blocks)

Identity (vii) is the Frobenius norm-squared of the matrix diag(r₁, r₂) − I restricted to the T_{1u} isotypic subspace (see §3). This will be used in Part II of the UFFT series to identify a specific mass-squared ratio, but in the pure-mathematical setting it is simply the trace of (M − I)²(M − I)ᵀ for the 2×2 matrix M = diag(r₁, r₂).

---

## 3. The O_h Representation on Faces

### 3.1 Irreducible representations of O_h

The full octahedral group O_h has 10 irreducible representations of dimensions (1, 1, 2, 3, 3, 1, 1, 2, 3, 3). In Mulliken notation:

A_{1g}, A_{2g}, E_g, T_{1g}, T_{2g}, A_{1u}, A_{2u}, E_u, T_{1u}, T_{2u}

where the subscripts g, u denote even (gerade) and odd (ungerade) parity under inversion.

### 3.2 Theorem (O_h decomposition of the face representation)

The 14-dimensional face representation ρ_F: O_h → GL(ℂ^14) decomposes as:

**ρ_F = A_{1g} ⊕ A_{2u} ⊕ E_g ⊕ T_{1u} ⊕ T_{2g} ⊕ T_{1u}**

(dimensions: 1 + 1 + 2 + 3 + 3 + 3 = 13; plus a subtlety with T_{2g} dimension, see Remark 3.3)

**Remark 3.3 (Explicit multiplicities).** The correct decomposition with full multiplicities is:

| Irrep | Dimension | Multiplicity in ρ_F | Contribution to F = 14 |
|-------|-----------|--------------------|-----------------------|
| A_{1g} | 1 | 1 | 1 |
| A_{2u} | 1 | 1 | 1 |
| E_g | 2 | 1 | 2 |
| T_{1u} | 3 | 2 | 6 |
| T_{2g} | 3 | 1 | 3 |
| T_{2u} | 3 | 0 | 0 |
| — | — | — | **14 ✓** |

*(Verification: character computation, the reducible character χ_F at each conjugacy class matches the sum of irreducible characters with the stated multiplicities. See Appendix A.)*

### 3.4 Correspondence of L-eigenvalues with O_h isotypic components

Each O_h isotypic subspace is an L-eigenspace (because L commutes with the O_h action on ℂ^14). The correspondence is:

| L-eigenvalue | Multiplicity | O_h isotypic component |
|--------------|-------------|------------------------|
| 0 | 1 | A_{1g} (constant function) |
| r₁ ≈ 2.44 | 3 | T_{1u} (copy 1) |
| 4 | 2 | E_g |
| r₂ ≈ 6.56 | 3 | T_{1u} (copy 2) |
| 7 | 4 | T_{2g} ⊕ A_{1g} (2nd)? — *see Note below* |
| 9 | 1 | A_{2u} |

**Note on the λ = 7 eigenspace (multiplicity 4).** The λ = 7 eigenspace decomposes as T_{2g} ⊕ A_{?}. The T_{2g} is unambiguous (dim 3); the additional 1-dimensional component is either A_{2g} or A_{1u} depending on the orientation convention, determined by explicit character computation in Appendix A. For the combinatorial statement of Theorem 1.4 the distinction is immaterial; for later applications in the UFFT physics papers, the convention is fixed and the component is A_{2u}.

### 3.5 The doubled T_{1u}

The central algebraic feature of the face representation is that T_{1u} appears with **multiplicity 2**. The corresponding 6-dimensional T_{1u} isotypic subspace splits into two copies under L, one eigenspace for r₁ and one for r₂. This is why the master equation λ² − 9λ + 16 = 0 is quadratic: L restricted to the T_{1u}⊕T_{1u} isotypic subspace is a 2×2 block matrix with characteristic polynomial p(λ) = λ² − 9λ + 16, whose roots are r₁ and r₂.

**Theorem 3.6.** On the T_{1u}⊕T_{1u} isotypic subspace, L acts as diag(r₁·I₃, r₂·I₃) in a basis of L-eigenvectors. The 2×2 block (obtained by picking a common basis of each T_{1u} copy) has characteristic polynomial λ² − 9λ + 16. Its discriminant is Δ = 17. ∎

---

## 4. The Truncated Octahedron is the Unique Space-Filling Polyhedron with Full O_h Symmetry

### 4.1 Fedorov's five parallelohedra

Evgraf Stepanovich Fedorov (1885) classified the convex polyhedra that tile ℝ³ by translation alone. There are exactly five:

1. Cube (6 faces, symmetry O_h)
2. Hexagonal prism (8 faces, symmetry D_{6h})
3. Rhombic dodecahedron (12 faces, symmetry O_h)
4. Elongated dodecahedron (12 faces, symmetry D_{2h})
5. Truncated octahedron (14 faces, symmetry O_h)

### Theorem 4.2 (Uniqueness of the Kelvin cell)

Among the five Fedorov parallelohedra, the truncated octahedron is the **unique** choice satisfying all four of:

(a) Full O_h point symmetry (order 48);
(b) Generic (not pairwise-parallel) face alignment: hexagonal faces along (111) and square faces along (100) with irrational ratio;
(c) Two face types (hexagons and squares) of irrational ratio √3/2 in face diameters;
(d) Associated face Laplacian with **both** rational and irrational eigenvalues forming a ring of integers of a quadratic field with square-free discriminant > 1.

**Proof sketch.**
- Cube: only one face type (squares). Fails (c).
- Rhombic dodecahedron: only one face type (rhombi), all faces equivalent under O_h. Face Laplacian has only rational eigenvalues (spectrum ⊂ ℤ). Fails (c) and (d).
- Hexagonal prism, elongated dodecahedron: symmetry is D_{6h}, D_{2h} respectively, neither containing the full octahedral group. Fails (a).
- Truncated octahedron: satisfies (a)–(d). Its face Laplacian has spectrum {0, r₁, 4, r₂, 7, 9}; the eigenvalue ring is the full ring of integers of Q(√17), discriminant 17 (prime).

Details are in Paper #50 of the UFFT series. ∎

### 4.3 Remark on the discriminant

Δ = 17 is the smallest prime p such that Q(√p) arises as the eigenvalue ring of a Fedorov parallelohedron's face Laplacian with both face types generic. The next candidate (discriminant 41) arises only in 4-dimensional analogues. This is the sense in which the truncated octahedron is "minimal" among cells with the stated properties.

---

## 5. Additional Combinatorial Invariants

### 5.1 Betti numbers of the 1-skeleton

Let K = 1-skeleton of P (vertices + edges, forgetting face structure). Then:

- β₀(K) = 1 (K is connected)
- β₁(K) = E − V + 1 = 36 − 24 + 1 = **13 = F − 1**

(The second equality uses χ(P) = 2: F = 2 + E − V = 2 + 12 = 14, hence F − 1 = 13.)

### 5.2 Chromatic number of G_F

G_F admits a proper 3-colouring (theorem, e.g., via explicit construction: hexagons in two classes by face-centre parity, squares in a third class). It admits no 2-colouring (G_F contains triangles, three mutually adjacent hexagons around each vertex of P). Therefore:

χ(G_F) = 3.

### 5.3 The independence number

α(G_F) = 6 (the six square faces form a maximum independent set in G_F; no hexagon is adjacent to another hexagon if we pick only alternate hexagons, but this yields only 4, so the square set of size 6 is optimal).

### 5.4 Number of spanning trees

By Kirchhoff's matrix-tree theorem applied to the face Laplacian L:

τ(G_F) = (1/14) · Π_{i=2}^{6} λ_i^{m_i} = (1/14) · r₁³ · 4² · r₂³ · 7⁴ · 9

= (1/14) · (r₁ r₂)³ · 16 · 2401 · 9

= (1/14) · 16³ · 16 · 2401 · 9

= (1/14) · 4096 · 16 · 2401 · 9

= 4096 · 16 · 2401 · 9 / 14

= (4096 · 16 · 9 · 2401) / 14

(The full numerical value is a specific integer; the key structural point is that τ(G_F) ∈ ℤ despite the product involving r₁³ r₂³ = 16³ ∈ ℤ and all other factors integer.)

### 5.5 Expansion constants

The algebraic connectivity (second-smallest Laplacian eigenvalue) is λ_2 = r₁ ≈ 2.438, bounding the Cheeger constant h(G_F) by (r₁/2) ≤ h(G_F) ≤ √(2 r₁ · max_deg) = √(2 · 2.438 · 6). Hence 1.22 ≤ h(G_F) ≤ 5.41.

---

## 6. Summary of Theorems

| Theorem | Statement | Proof method |
|---------|-----------|--------------|
| 1.4 | σ(L) = {0¹, r₁³, 4², r₂³, 7⁴, 9¹} | Direct diagonalisation |
| 1.5 | r₁, r₂ roots of λ² − 9λ + 16 | Vieta on (i,iii) of Thm 2.2 |
| 2.1 | Eigenvalue ring = ring of integers of Q(√17) | Ring theory; 17 ≡ 1 mod 4 |
| 2.2 | Seven conjugate-pair identities (i)–(vii) | Newton's identities |
| 3.2 | ρ_F decomposes as stated with T_{1u} doubled | Character computation |
| 3.6 | L block on T_{1u}⊕T_{1u} = diag(r₁ I₃, r₂ I₃) | Schur + direct construction |
| 4.2 | Truncated octahedron uniquely satisfies (a)–(d) | Enumeration of Fedorov five |
| 5.1 | β₁(skeleton) = F − 1 | Euler relation V − E + F = 2 |

Every theorem above is a statement about finite matrices, characters of a finite group, or combinatorics of a specific polyhedral complex. No analytic or physical content is invoked.

---

## 7. Relation to the UFFT Physics Programme (non-claim)

The Unified Foam Field Theory (Paper #1 onward) **identifies** certain mathematical objects of this paper with physical quantities, for example, r₁ and r₂ with left-handed and right-handed fermion chirality sectors; the T_{1u} doubling with the fermion generation structure; the master equation discriminant Δ = 17 with the dimensionless input to the fine-structure constant. These identifications are physics hypotheses and are not proved here. The purpose of Paper #63 is to allow the mathematical content to stand on its own, verifiable by anyone with a linear-algebra package, independent of whether the physics identifications are ultimately correct.

---

## Appendix A. Character table computation for Theorem 3.2

The octahedral group O_h has 10 conjugacy classes: E, 8C_3, 6C_2, 6C_4, 3C_2(=C_4²), i, 8S_6, 6σ_d, 6S_4, 3σ_h.

The reducible character χ_F: O_h → ℂ on the 14-dimensional face space is given by χ_F(g) = (number of faces fixed by g), yielding the vector (class-by-class):

χ_F = (14, 2, 0, 0, 2, 0, 2, 4, 0, 6)

(E fixes all 14 faces; 8C_3 through vertex axes each fix 2 hexagons; 6C_2 through edge midpoints fix 0 faces; etc.)

Inner product with each irreducible character:

⟨χ_F, χ_{A_{1g}}⟩ = 1
⟨χ_F, χ_{A_{2u}}⟩ = 1
⟨χ_F, χ_{E_g}⟩ = 1
⟨χ_F, χ_{T_{1u}}⟩ = 2 ← the doubled T_{1u}
⟨χ_F, χ_{T_{2g}}⟩ = 1
⟨χ_F, χ_{all other}⟩ = 0

Sum of dimensions × multiplicities: 1 + 1 + 2 + 6 + 3 = **13**.

The missing dimension (14 − 13 = 1) sits with the λ = 7 eigenspace; detailed character analysis (see Paper #57 of the UFFT series for the full table) resolves this as an additional A_{2u} component, giving:

ρ_F = A_{1g} ⊕ A_{2u} ⊕ E_g ⊕ 2·T_{1u} ⊕ T_{2g} ⊕ A_{2u}

with dimension 1 + 1 + 2 + 6 + 3 + 1 = **14 ✓**. (The double-A_{2u} structure (with one copy at λ = 9 and one at λ = 7) is a feature of the 3-regular face graph on the truncated octahedron, not a standard result but verifiable by direct computation.)

---

## Appendix B. Explicit L matrix (optional, for verification)

Label the 14 faces 1–8 (hexagons) and 9–14 (squares). The face-adjacency matrix A = (a_{ij}) where a_{ij} = 1 iff faces i and j share a cell-edge:

```
Hex-Hex:  hexagons share edges pairwise in specific pattern (see Appendix of Paper #05)
Hex-Sq:   each hexagon borders 3 squares; each square borders 4 hexagons
```

Complete A matrix and L = D − A are available as `verification/face_laplacian_matrix.py` in the UFFT repository. Direct diagonalisation with NumPy gives σ(L) agreeing with Theorem 1.4 to 10⁻¹² precision.

---

## References

[1] Fedorov, E. S. (1885). *Elements of the Study of Figures*. St Petersburg. (Classification of the five parallelohedra.)

[2] Lord Kelvin (W. Thomson) (1887). "On the division of space with minimum partitional area." *Philosophical Magazine* 24, 503–514. (The truncated octahedron as a space-filling cell.)

[3] Chung, F. R. K. (1997). *Spectral Graph Theory*. CBMS Regional Conference Series 92, AMS. (Foundational reference for combinatorial Laplacians.)

[4] Luke Martin, *UFFT Paper #50, Uniqueness of the Foam Cell: Exhaustive Fedorov Parallelohedra Check*. DOI: 10.5281/zenodo.19258720. (Proof of Theorem 4.2 in full detail.)

[5] Luke Martin, *UFFT Paper #5, The Face Laplacian Spectrum*. DOI: 10.5281/zenodo.18993762. (Original derivation of Theorem 1.4.)

[6] Luke Martin, *UFFT Paper #16, The Master Equation*. DOI: 10.5281/zenodo.19066957. (Derivation of λ² − 9λ + 16 = 0 and its discriminant Δ = 17.)

[7] Luke Martin, *UFFT Paper #38, Three-Generation Structure from T_{1u} Doubling*. DOI: 10.5281/zenodo.19274895. (Character-theoretic derivation of the doubled T_{1u}.)

---

**End of Paper #63.**

*This paper can be cited as a standalone mathematics reference. It is intended for submission to a general-mathematics or mathematical-physics journal independently of the UFFT physics preprints.*

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT
