# UFFT Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | March 2026 |
| Series | Unified Foam Field Theory |
| Paper | #5 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | 1 |
| DOI | 10.5281/zenodo.19030062 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** truncated octahedron, Kelvin cell, graph Laplacian, spectral graph theory, octahedral group, face adjacency

**Note:** This paper establishes the foundational eigenvalue spectrum used by all subsequent UFFT papers. The uniqueness of this spectrum among Fedorov parallelohedra was later proved in Paper #50 [DOI: 10.5281/zenodo.19447996].

---

## Abstract

We compute the exact spectrum of the graph Laplacian on the face adjacency graph of the truncated octahedron (Kelvin cell). The 14 faces (6 squares, 8 hexagons) form a graph where two faces are adjacent if they share an edge. The Laplacian eigenvalues are:

**0 (×1), (9−√17)/2 (×3), 4 (×2), (9+√17)/2 (×3), 7 (×4), 9 (×1)**

The characteristic polynomial factors completely:

**p(λ) = λ · (λ²−9λ+16)³ · (λ−4)² · (λ−7)⁴ · (λ−9)**

All eigenvalues are algebraic numbers over Q(√17). Using the full octahedral symmetry group O_h (order 48), each eigenspace is identified with an irreducible representation: λ=0 (A1g), λ=(9−√17)/2 (T1u), λ=4 (Eg), λ=(9+√17)/2 (T1u), λ=7 (A1g ⊕ T2g), λ=9 (A2u). All results are verified by trace identities and numerical computation.

---

## 1. Introduction

The truncated octahedron is the unique Archimedean solid that tiles three-dimensional Euclidean space. It is the Voronoi cell of the body-centred cubic (BCC) lattice and the solution to Kelvin's problem of partitioning space into cells of equal volume with minimal surface area [1]. Its graph-theoretic properties are relevant to crystallography, foam physics, and discrete geometry.

The vertex adjacency graph and edge adjacency graph of the truncated octahedron are well studied [2]. The face adjacency graph (where vertices represent faces and edges connect faces sharing a common edge of the polyhedron) appears not to have been studied in the literature. We compute its complete Laplacian spectrum and identify each eigenspace with an irreducible representation of the symmetry group.

---

## 2. The Face Adjacency Graph

### 2.1 Construction

The truncated octahedron has V = 24 vertices (all permutations of (0, ±1, ±2)), E = 36 edges (pairs at distance √2), and F = 14 faces: 6 squares with normals along ±x, ±y, ±z, and 8 regular hexagons with normals along (±1,±1,±1)/√3.

The face adjacency graph G_F has 14 vertices (one per face) and an edge between two vertices whenever the corresponding faces share a polyhedron edge. The resulting graph has:

- **6 square vertices**, each of degree 4 (adjacent to 4 hexagons)
- **8 hexagonal vertices**, each of degree 6 (adjacent to 3 squares and 3 hexagons)
- **36 edges** in the face graph
- **No square-square adjacency** (no two squares share an edge)

> ✓ Verified by explicit construction from vertex coordinates. Each square face shares its 4 edges with 4 distinct hexagonal faces. Each hexagonal face shares 3 edges with squares and 3 with other hexagons.

### 2.2 Bipartite Structure

The face graph is NOT bipartite: hexagonal faces are adjacent to other hexagonal faces. However, the square-vertex subgraph is an independent set (no edges between squares).

---

## 3. The Graph Laplacian

The graph Laplacian is L = D − A, where D is the diagonal degree matrix and A is the adjacency matrix:

**L is a 14×14 integer matrix with Tr(L) = Σ deg(v) = 6(4) + 8(6) = 72  (1)**

---

## 4. Spectrum

### 4.1 Eigenvalues

The eigenvalues of L, computed both numerically and verified algebraically:

| Eigenvalue | Exact value | Multiplicity |
|-----------|-------------|-------------|
| λ₁ | 0 | 1 |
| λ₂ | (9−√17)/2 ≈ 2.4384 | 3 |
| λ₃ | 4 | 2 |
| λ₄ | (9+√17)/2 ≈ 6.5616 | 3 |
| λ₅ | 7 | 4 |
| λ₆ | 9 | 1 |

> ✓ Sum of multiplicities: 1+3+2+3+4+1 = 14 = F ✓

### 4.2 The Irrational Pair

The eigenvalues (9±√17)/2 are roots of the quadratic:

**x² − 9x + 16 = 0  (2)**

Their properties:
- **Sum**: (9−√17)/2 + (9+√17)/2 = 9 (= λ₆, the maximum eigenvalue)
- **Product**: (81−17)/4 = 64/4 = 16 = 2⁴
- **Discriminant**: 17 (prime)

The irrational eigenvalues lie in Q(√17). Since 17 is prime and squarefree, this is the minimal field extension required.

### 4.3 Characteristic Polynomial

**p(λ) = λ · (λ²−9λ+16)³ · (λ−4)² · (λ−7)⁴ · (λ−9)  (3)**

Degree: 1 + 2(3) + 1(2) + 1(4) + 1(1) = 14 ✓

> ✓ Verified by evaluating det(L−λI) at λ = 3.5: numerical determinant = 24790.94, formula = 24790.94. Match to 6 significant figures.

---

## 5. Trace Identity Verification

### 5.1 First Trace

**Tr(L) = 0(1) + (9−√17)/2·(3) + 4(2) + (9+√17)/2·(3) + 7(4) + 9(1)  (4)**

The √17 terms cancel: 3(9−√17)/2 + 3(9+√17)/2 = 27.

**Tr(L) = 0 + 27 + 8 + 28 + 9 = 72 = Σ deg(v) ✓**

### 5.2 Second Trace

**Tr(L²) = Σ λᵢ² = Σ deg(v)² + 2|E(G_F)|  (5)**

Using r₁² + r₂² = (r₁+r₂)² − 2r₁r₂ = 81 − 32 = 49:

**Tr(L²) = 3(49) + 0 + 2(16) + 4(49) + 81 = 147 + 0 + 32 + 196 + 81 = 456**

**Σ deg² + 2|E| = 6(16)+8(36) + 2(36) = 96+288+72 = 456 ✓**

---

## 6. Symmetry Decomposition

### 6.1 The Octahedral Group O_h

The symmetry group of the truncated octahedron is O_h (order 48). It acts on the 14 faces, permuting them. This action preserves the Laplacian: L commutes with all permutation matrices induced by O_h. Therefore each eigenspace is a union of irreducible representations (irreps) of O_h.

### 6.2 The Face Representation

The 14-dimensional permutation representation of O_h on the faces decomposes as [3]:

**Face rep = A1g(2) ⊕ Eg(1) ⊕ T2g(1) ⊕ A2u(1) ⊕ T1u(2)  (6)**

where the notation ρ(m) means irrep ρ appears with multiplicity m. The dimensions are: A1g(1), Eg(2), T2g(3), A2u(1), T1u(3). Total: 2(1)+1(2)+1(3)+1(1)+2(3) = 14 ✓.

### 6.3 Eigenspace Identification

The character of the O_h action restricted to each eigenspace was computed by constructing all 48 group elements explicitly as 3×3 orthogonal matrices, determining the induced permutation on faces, and computing traces on each eigenspace projector:

| Eigenvalue | Dim | O_h Irrep | Character (E, 8C₃, 6C₂, 6C₄, 3C₂', i, 8S₆, 6σ_d, 6S₄, 3σ_h) |
|-----------|-----|-----------|----------------------------------------------------------------|
| 0 | 1 | A1g | (1, 1, 1, 1, 1, 1, 1, 1, 1, 1) |
| (9−√17)/2 | 3 | T1u | (3, 0, −1, 1, −1, −3, 0, 1, −1, 1) |
| 4 | 2 | Eg | (2, −1, 0, 0, 2, 2, −1, 0, 0, 2) |
| (9+√17)/2 | 3 | T1u | (3, 0, −1, 1, −1, −3, 0, 1, −1, 1) |
| 7 | 4 | A1g ⊕ T2g | (4, 1, 2, 0, 0, 4, 1, 2, 0, 0) |
| 9 | 1 | A2u | (1, 1, −1, −1, 1, −1, −1, 1, 1, −1) |

> ✓ All characters verified against the standard O_h character table. Each eigenspace character decomposes uniquely into known irreps.

### 6.4 Notable Features

The two copies of T1u (each 3-dimensional) correspond to the two irrational eigenvalues (9±√17)/2. The quadratic x²−9x+16 = 0 is the minimal polynomial governing the T1u splitting. The fact that T1u splits into two eigenspaces (rather than having a single 6-dimensional eigenspace) reflects the inequivalence of the two T1u copies in the face representation, one arises from the square-hex coupling and the other from the hex-hex coupling.

The eigenspace at λ = 7 carries A1g ⊕ T2g (dimensions 1+3 = 4). This is the only eigenspace containing more than one irrep, forced by the coincidence of eigenvalues from two distinct irrep sectors.

The two A1g copies (λ = 0 and one component of λ = 7) correspond to the uniform (breathing) mode and the mode that is uniform within each orbit but differs between orbits.

---

## 7. Physical Significance

The truncated octahedron face graph arises naturally in the BCC lattice tiling, where each face represents a connection to a neighbouring cell. The Laplacian spectrum governs diffusion and wave propagation on this connectivity graph. The spectral gap (9−√17)/2 ≈ 2.438 determines the mixing rate of any process that equilibrates through face-to-face coupling in the BCC tiling.

---

## 8. Conclusion

The complete Laplacian spectrum of the truncated octahedron face adjacency graph is:

**Spec(L) = {0¹, ((9−√17)/2)³, 4², ((9+√17)/2)³, 7⁴, 9¹}**

with characteristic polynomial p(λ) = λ(λ²−9λ+16)³(λ−4)²(λ−7)⁴(λ−9). All eigenvalues lie in Q(√17). Each eigenspace is identified with an O_h irrep: A1g, T1u, Eg, T1u, A1g ⊕ T2g, A2u respectively. The result is verified by trace identities, numerical computation, and character-theoretic decomposition.

---

## References

[1] Thomson, W. (Lord Kelvin) (1887). On the division of space with minimum partitional area. Philosophical Magazine, 24, 503.

[2] Coxeter, H. S. M. (1973). Regular Polytopes (3rd ed.). Dover Publications.

[3] Dresselhaus, M. S., Dresselhaus, G., & Jorio, A. (2008). Group Theory: Application to the Physics of Condensed Matter. Springer.

---

## UFFT Papers Referenced

- Paper #1: [DOI: TBD] — Foundational theory and Axiom Zero
- Paper #2: [DOI: TBD] — B-V-D modal structure
- Paper #3: [DOI: 10.5281/zenodo.19011758] — Fine Structure Constant (v1)
- Paper #4: [DOI: 10.5281/zenodo.19019944] — Fine Structure Constant (v2)

---

## Reproduction

All results can be reproduced by: (1) constructing the 24 vertices as permutations of (0,±1,±2), (2) identifying the 14 faces by normal directions, (3) building the 14×14 adjacency matrix (faces sharing ≥2 vertices), (4) computing L = D−A, (5) diagonalising. The computation requires only integer arithmetic and one square root (√17).

---

## AI Disclosure

Developed in collaboration with Claude (Anthropic). Ideas and direction: Luke Martin. AI role: matrix computation, eigenvalue verification, character-theoretic decomposition.

---

*Unified Foam Field Theory · Paper #5 · DOI: 10.5281/zenodo.19030062 · Priority Date: 20 February 2026*

*B + V = D*
