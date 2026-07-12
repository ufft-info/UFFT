# UFFT Paper #50 — The Uniqueness of the Foam Cell

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #50 of 72 |
| Framework | v10 · rev 1 |
| Status | Amended 19 April 2026 — criterion (iii) sharpened to "= C_A²"; Weaire-Phelan axiomatic-exclusion scope note added following internal review |
| Tier | 1 (within Fedorov parallelohedra) |
| DOI | 10.5281/zenodo.19447996 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** face Laplacian, truncated octahedron, Fedorov parallelohedra, space-filling polyhedra, spectral graph theory, uniqueness

## Abstract

We compute the face adjacency Laplacian for all five Fedorov parallelohedra (the complete list of convex polyhedra that tile three-dimensional Euclidean space by translation alone. The truncated octahedron is the unique member whose face Laplacian has (a) a prime discriminant (Δ = 17), (b) irrational eigenvalue products equal to Δ−1 (r₁r₂ = 16), and (c) irrational eigenvalue sum equal to C_A² (r₁+r₂ = 9 = 3² = C_A², where C_A = F_hx/F − 1 in the natural normalisation is the framework's colour number). It is also the only member with two distinct types of regular faces. This exhaustive computation requires no physical assumptions) it is a theorem of combinatorial geometry, restricted to Fedorov's five convex parallelohedra. Non-parallelohedral space-fillings (notably the two-cell Weaire-Phelan structure) are outside the scope of this theorem; UFFT excludes them axiomatically by restriction to single-cell parallelohedral foams (see §6 and `verification/peer_review_deliverables/D3_Uniqueness_Restriction.md`).

**Keywords:** face Laplacian, truncated octahedron, Fedorov parallelohedra, space-filling polyhedra, spectral graph theory, uniqueness

---

## 1. Background

The Unified Foam Field Theory (UFFT) derives the Standard Model of particle physics from the face adjacency Laplacian of the truncated octahedron. A natural objection: why this polyhedron? Could a different space-filling shape produce the same or similar physics?

This paper answers the question exhaustively.

## 2. The Fedorov Classification

Fedorov (1885) proved that there are exactly five combinatorial types of convex polyhedra that tile R³ by translation alone (parallelohedra):

1. **Cube** (parallelepiped): F = 6, all square faces
2. **Hexagonal prism**: F = 8, two hexagonal + six rectangular faces
3. **Rhombic dodecahedron**: F = 12, all rhombic faces
4. **Elongated dodecahedron**: F = 12, eight rhombic + four rectangular faces
5. **Truncated octahedron**: F = 14, six square + eight hexagonal faces

No other convex polyhedra tile R³ monohedrally by translation. This list is complete.

## 3. Face Adjacency Laplacians

For each polyhedron, we construct the face adjacency graph G = (V_F, E_F) where vertices represent faces and edges connect faces sharing an edge. The face Laplacian is L = D − A where D is the degree matrix and A the adjacency matrix.

### 3.1 Cube (F = 6)

Each face is adjacent to four others (all except its opposite). The face graph is the octahedron graph.

Spectrum: **{0¹, 4³, 6²}**

All eigenvalues are integers. No quadratic structure. Discriminant: 0.

### 3.2 Hexagonal prism (F = 8)

Two hexagonal end-caps, each adjacent to all six rectangular sides. Each rectangular side adjacent to two hexagons and two neighbouring rectangles (degree 4). Hexagons have degree 6.

Spectrum: **{0¹, 3², 5², 6², 8¹}**

All eigenvalues are integers. No quadratic structure. Discriminant: 0.

### 3.3 Rhombic dodecahedron (F = 12)

Twelve rhombic faces, each adjacent to four others. The face adjacency graph is the cuboctahedral graph (regular, degree 4).

Spectrum: **{0¹, 2³, 4³, 6⁵}**

All eigenvalues are integers. No quadratic structure. Discriminant: 0.

### 3.4 Elongated dodecahedron (F = 12)

Eight rhombic faces and four rectangular faces. Rectangles have degree 6; rhombi have degree 4.

Spectrum: **{0¹, 2¹, ((10−√20)/2)², 4², 6³, ((10+√20)/2)², 8¹}**

This polyhedron DOES have irrational eigenvalues from the quadratic λ²−10λ+20 = 0.

- Discriminant: Δ = 100 − 80 = **20**
- 20 = 4 × 5. **Not prime.** ✗
- Product: r₁r₂ = 20. Is 20 = Δ−1 = 19? **No.** ✗
- Sum: r₁+r₂ = 10. Is 10 = C_A² = 9? **No.** ✗

All three conditions fail.

### 3.5 Truncated octahedron (F = 14)

Six square faces (degree 4) and eight hexagonal faces (degree 6). Face adjacency: 24 square-hexagon edges + 12 hexagon-hexagon edges = 36 edges total.

Spectrum: **{0¹, ((9−√17)/2)³, 4², ((9+√17)/2)³, 7⁴, 9¹}**

Quadratic: λ²−9λ+16 = 0.

- Discriminant: Δ = 81 − 64 = **17**
- 17 is **prime**. ✓
- Product: r₁r₂ = **16** = 17 − 1 = Δ − 1. ✓
- Sum: r₁+r₂ = **9** = 3² = **C_A²** (where C_A = F_hx/F − 1 in the natural normalisation). ✓

All three conditions hold. **Unique among all five Fedorov parallelohedra.**

## 4. Summary

| Polyhedron | F | Δ | Prime? | r₁r₂ = Δ−1? | Sum = C_A² (= 9)? | Regular faces? |
|-----------|---|---|--------|-------------|--------------------|----------------|
| Cube | 6 | 0 | ✗ | — | — | 1 type |
| Hex. prism | 8 | 0 | ✗ | — | — | mixed |
| Rhombic dodec. | 12 | 0 | ✗ | — | — | 1 type |
| Elongated dodec. | 12 | 20 | ✗ | ✗ | ✗ (10 ≠ 9) | mixed |
| **Trunc. octahedron** | **14** | **17** | **✓** | **✓** | **✓** | **2 types (sq+hex)** |

## 5. Theorem (Restricted)

**Theorem.** Among the five convex parallelohedra in R³ (Fedorov 1885), the truncated octahedron is the unique cell whose face adjacency Laplacian has:

1. **A prime discriminant Δ** (the discriminant of the irrational quadratic factor of the characteristic polynomial)
2. **Irrational eigenvalue product r₁r₂ = Δ − 1**
3. **Irrational eigenvalue sum r₁ + r₂ = C_A²** (where C_A = F_hx/F − 1 = 3 is the framework's colour number, *not* an arbitrary perfect square)

It is also the unique convex parallelohedron in this list with exactly two types of regular faces.

The proof is exhaustive: all five cases checked. □

**Sharpening note.** Criterion 3 was stated in earlier drafts of this paper as "a perfect square," which is post-hoc, any square integer would satisfy it. The sharpened "= C_A²" statement ties the test to a quantity already fixed elsewhere in the framework (the natural-normalisation colour number) and is therefore a derivation-style criterion rather than a retrofit. See `verification/peer_review_deliverables/D3_Uniqueness_Restriction.md` §4 for the full scope-restriction argument.

## 6. Scope and Axiomatic Exclusions

The theorem above is restricted to Fedorov's five **convex parallelohedra**, convex polyhedra that tile R³ by translation alone under a Bravais lattice. Three categories of structure are explicitly outside the theorem's scope:

**Stereohedra (convex isohedral fillers under the full crystallographic groups).** A strictly larger class than parallelohedra; classified in modern crystallography (e.g., Delgado-Friedrichs and O'Keeffe 2003). UFFT axiomatically restricts to translation-only symmetry; stereohedra requiring rotations or glide reflections are excluded by axiom, not by this theorem.

**The Weaire-Phelan structure (Weaire & Phelan 1994).** A two-cell tiling (irregular pentagonal dodecahedra (12 faces) interleaved with tetrakaidecahedra (14 faces) in a 6:2 ratio) that beats the Kelvin cell on Lord Kelvin's *isoperimetric* (minimum-surface) question by ~0.3%. Weaire-Phelan is not a single-cell tiling, has no single face Laplacian, and has symmetry group Pm-3n (a chiral subgroup of O_h, not O_h itself). It is excluded by UFFT's axiom of single-cell parallelohedral foam, not by this theorem. **The honest statement: UFFT optimises for spectral structure (the criteria above), not for surface area; the Weaire-Phelan structure does not refute UFFT, but it is also not addressed by Paper #50.** A reader who insists "but the universe might be a Weaire-Phelan-like two-cell foam" is making a claim against UFFT's axiomatic basis, not against this theorem; if such a structure turns out to be physically required, the framework is falsified or extended.

**Multi-cell tilings generally.** Excluded by the same axiomatic restriction. UFFT's "one matrix → SM" claim depends on a single face Laplacian per cell; multi-cell tilings introduce inter-cell coupling structures that double the parameter count.

## 7. Implications

If the fundamental structure of spacetime is a foam of single space-filling convex parallelohedral cells, and if the physics of the Standard Model derives from the face Laplacian of that cell, then **within that axiomatic class** the cell geometry is not a choice, it is the only possibility. The truncated octahedron is forced by the spectral criteria of §5. The single-cell, translation-only restriction is itself an axiomatic choice (per §6); the framework does not derive it from anything more primitive, and a reader is entitled to ask why this restriction. The honest answer is: simplicity. Multi-cell tilings introduce ambiguity that breaks the framework's core "one matrix → SM" structure. Whether the universe respects this restriction is itself a falsifiable empirical question.

No alternative exists *within UFFT's axiomatic scope*. Outside that scope (Weaire-Phelan, stereohedra, multi-cell foams), the question is open and not addressed here.

---

## References

[1] Fedorov, E. S. (1885). Nachala Ucheniya o Figurakh. [The beginnings of the study of figures.]
[2] Martin, L. (2026). The Laplacian Spectrum of the Truncated Octahedron. Zenodo. DOI: 10.5281/zenodo.19030062.
[3] Kelvin, Lord (1887). On the division of space with minimum partitional area. Phil. Mag. 24, 503.
[4] Weaire, D. & Phelan, R. (1994). A counter-example to Kelvin's conjecture on minimal surfaces. Phil. Mag. Lett. 69, 107.
[5] Delgado-Friedrichs, O. & O'Keeffe, M. (2003). Identification of and symmetry computation for crystal nets. Acta Cryst. A59, 351.
[6] Martin, L. (2026). *Verification/peer_review_deliverables/D3_Uniqueness_Restriction.md*, uniqueness-language restriction, Weaire-Phelan axiomatic exclusion, criterion 3 sharpening.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). The exhaustive computation of all five face Laplacians was performed by Claude. Ideas, direction, and framework: Luke Martin.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*

*Unified Foam Field Theory · Paper #50 · DOI: 10.5281/zenodo.19447996 · Priority Date: 20 February 2026*

*B + V = D*
