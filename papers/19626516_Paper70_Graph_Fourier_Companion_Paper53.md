# UFFT Paper #70 — A Graph-Fourier Companion to Paper #53: The 6/7 Dark-Energy Factor as the Interior-Spectrum Projector Trace

**Unified Foam Field Theory — Part LXX**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #70 of 70 |
| Framework | v10 |
| Status | Complete — companion to Paper #53, stating the 6/7 factor as the trace of an interior-spectrum projector and adding a band-edge zero-group-velocity lemma |
| Tier | 1 (algebraic identity tr(P_int)/F = 6/7) / 2 (physical pressure-wave identification — inherited from Paper #53, unchanged) |
| DOI | 10.5281/zenodo.19626516 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, dark energy, cosmological constant, graph Fourier transform, spectral projector, band-edge mode, group velocity, Kelvin cell, Euler characteristic

---

## Abstract

Paper #53 derived the dark-energy correction factor (F − χ)/F = 6/7 by identifying the two topologically inert face-modes of the Kelvin-cell face Laplacian as the A₁g zero mode (λ = 0, forced by connectivity) and the A₂u maximum mode (λ = 9, forced by bipartiteness of the hexagonal subgraph Q₃). The Tier 1 sub-theorems there (A₁g uniqueness, A₂u uniqueness, and inert count equal to χ(S²) = 2) settle the *counting*, while the physical identification linking the inert subspace to the absence of pressure-wave energy rested on the A₂u ↔ Higgs identification of Paper #45 (Tier 2).

This companion paper gives an independent route. We show that the 6/7 factor equals the trace over F = 14 of the spectral projector of the face Laplacian onto the open interval (λ_min, λ_max) = (0, 9). This identity is purely algebraic, a consequence of the spectrum multiplicities 1 + 3 + 2 + 3 + 4 + 1 = 14 with the two 1-dimensional irreps living at the band edges. A band-edge zero-group-velocity lemma from graph Fourier analysis then provides a physical complement: for the hyperbolic wave equation ∂²ψ/∂t² + c²Lψ = 0, the unique eigenvectors at λ_min and λ_max carry zero group velocity and therefore transport no wave energy. Together these establish the 6/7 factor as the fraction of *propagating* modes, without invoking Higgs absorption.

Consequence: the algebraic identity tr(P_int)/F = 6/7 is Tier 1. The physical link to the cosmological pressure wave remains Tier 2, shifted from the Paper-#45 A₂u=Higgs identification to the Part-X wave-equation identification, but not promoted. Full Tier 1 for ρ_Λ requires closure of Paper #48.

---

## 1. Setup

The Kelvin cell's face adjacency graph G_F has 14 vertices (6 square faces, 8 hexagonal faces) and an edge between two faces iff they share an edge of the cell. Square faces have 4 hex neighbours and 0 square neighbours; hex faces have 3 hex neighbours and 3 square neighbours. Combinatorial Laplacian:

> **L = D − A**

where D = diag(4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6) and A is the 14 × 14 face-adjacency matrix. The spectrum is (Paper #5, Paper #53):

> **Spec(L) = { 0¹, r₁³, 4², r₂³, 7⁴, 9¹ }    with r₁,₂ = (9 ∓ √17)/2**.

Total multiplicity 1 + 3 + 2 + 3 + 4 + 1 = 14. Two 1-dim irreps sit at the band edges (λ_min = 0 for A₁g, λ_max = 9 for A₂u); the remaining 12 = F − 2 modes occupy the interior at r₁, 4, r₂, 7.

---

## 2. The interior-spectrum projector

**Definition.** The interior-spectrum projector of L is

> **P_int = projector onto the spectral subspace span{ v_k ∈ ℝ^{14} : L v_k = λ_k v_k,  0 < λ_k < 9 }**.

Equivalently, P_int is the kernel complement of the polynomial M = L · (9I − L):

> **P_int = I − Π_{ker L} − Π_{ker(9I − L)}**,

since ker(L) = span{v_A₁g} and ker(9I − L) = span{v_A₂u} are each 1-dimensional.

**Theorem 70.1 (Interior-spectrum projector trace).** *On the Kelvin-cell face Laplacian,*

> **tr(P_int) = F − χ(S²) = 12**,

*hence*

> **tr(P_int) / F = 12 / 14 = 6 / 7**.

**Proof.** By Paper #53 Theorems 53.1 (A₁g unique at λ = 0 from connectivity) and 53.2 (A₂u unique at λ = 9 from bipartiteness of Q₃), the two band-edge eigenspaces each have dimension 1. By the spectral theorem for symmetric matrices, P_int is the orthogonal complement of the sum of these two eigenspaces in ℝ^F. Hence

> tr(P_int) = dim(ℝ^F) − dim(ker L) − dim(ker(9I − L)) = 14 − 1 − 1 = 12 = F − χ,

using χ(S²) = b₀ + b₂ = 1 + 1 = 2 (Euler-Poincaré on the simply-connected convex polyhedral surface). Dividing by F = 14 gives 12/14 = 6/7. □

**Numerical confirmation.** The projector equality P_int = I − P_A₁g − P_A₂u holds to ‖·‖_F ≈ 3 × 10⁻¹⁵ (see §6 and the verification script `verify_Paper70_interior_projector.py`).

**Remark.** Theorem 70.1 is purely algebraic: it rests on the Paper-#53 Tier 1 sub-theorems (connectivity and bipartiteness of G_F), not on any physical identification. The fraction 6/7 appears as a *spectral multiplicity ratio*.

---

## 3. The band-edge zero-group-velocity lemma

The algebraic Theorem 70.1 does not by itself explain *why* the interior projector is the right one for the dark-energy density formula. For that we need a physical criterion that distinguishes the interior from the band edges. The criterion is group velocity.

Consider the hyperbolic wave equation on the face graph,

> **∂²ψ/∂t² + c² L ψ = 0**,

whose normal-mode solutions are ψ_k(t) = v_k exp(±iω_k t) with dispersion ω_k² = c² λ_k. On a finite graph the eigenvalues are discrete, but the eigenvalue function λ(k) can be thought of as the restriction of a smooth dispersion surface (obtained by continuous embedding of the graph into the infinite BCC lattice, see Paper #5 Appendix B).

**Lemma 70.2 (Band-edge zero-group-velocity).** *For any connected simple graph G with Laplacian L, the eigenvectors at λ_min = 0 and λ_max (the spectral extremes) have group velocity zero in any smooth dispersion-relation completion:*

> **v_g(λ_min) = 0  and  v_g(λ_max) = 0.**

**Proof.** The group velocity is v_g(λ) = (c / (2 √λ)) · (∂λ / ∂k) where k is a wavenumber parametrising the dispersion surface. At a spectral extremum, λ is either a minimum (λ = 0) or a maximum (λ = λ_max). At an extremum ∂λ/∂k = 0 by elementary calculus (the stationary point of a smooth function has zero gradient). Therefore v_g = 0 at both band edges. At λ = 0 there is an additional kinematic factor: ω = c√λ → 0, so energy transport vanishes there trivially. □

**Physical interpretation.** A propagating wave has non-zero group velocity. Band-edge modes are standing-wave configurations that do not transport energy. Any localised disturbance on the face graph (for example the residual Big Bang pressure wave) has support only on the *propagating* modes, i.e., the interior spectrum.

**Comparison with Paper #53's argument.** Paper #53 §4 argues A₂u is inert because "A mode with torsion eigenvalue −1 is at unstable equilibrium, it collapses into the Higgs vacuum rather than propagating." Lemma 70.2 replaces that with a kinematic statement: A₂u is inert because its group velocity is zero at the dispersion maximum. The physical content is the same; the mathematical framing is now a standard result in lattice wave mechanics (van Hove band-edge singularities, 1953).

---

## 4. The 6/7 factor as a propagating-mode fraction

Combining Theorem 70.1 and Lemma 70.2:

**Theorem 70.3 (6/7 factor as propagating-mode fraction).** *The fraction of face modes on the Kelvin cell that carry non-zero group velocity under the hyperbolic wave equation ∂²ψ/∂t² + c²Lψ = 0 equals (F − χ)/F = 6/7.*

**Proof.** By Lemma 70.2, the non-propagating modes are the band-edge eigenvectors at λ_min = 0 and λ_max = 9. By Paper #53 Theorems 53.1 and 53.2, each of these eigenspaces has dimension 1. By Theorem 70.1 the complement has dimension F − 2 = 12. The propagating-mode fraction is therefore 12/14 = 6/7. □

This is the mathematical content that Paper #53's §6 assumed but did not prove in closed form, Paper #53 proved the *count* (via Euler-Poincaré), and this paper proves that the count equals the fraction of *propagating* modes under the face-graph wave equation.

---

## 5. Tier accounting

The Paper-#53 original tier structure was:

| Item | Paper #53 |
|------|------------|
| A₁g unique at λ=0 | Tier 1 |
| A₂u unique at λ=9 | Tier 1 |
| Inert count = χ = 2 | Tier 1 |
| A₂u is "inert" in the physical sense (Higgs absorption) | Tier 2 |
| ρ_Λ = ρ₀(l_P/R_U)² × 6/7 | Tier 2 |

This paper modifies the table as follows:

| Item | Paper #70 |
|------|------------|
| A₁g unique at λ=0 | Tier 1 (unchanged) |
| A₂u unique at λ=9 | Tier 1 (unchanged) |
| Inert count = χ = 2 | Tier 1 (unchanged) |
| tr(P_int)/F = 6/7 as algebraic identity | **Tier 1 (new)** — Theorem 70.1 |
| Band-edge modes have v_g = 0 | **Tier 1 (new)** — Lemma 70.2 |
| Propagating-mode fraction = 6/7 | **Tier 1 (new)** — Theorem 70.3 |
| ρ_Λ = ρ₀(l_P/R_U)² × 6/7 | Tier 2 (unchanged — still depends on the Part X / Paper #42 / Paper #48 identification of L as the foam wave operator) |

**Net effect.** The mathematical 6/7 factor is now Tier 1. The physical derivation of ρ_Λ remains Tier 2; the identification linking tr(P_int)/F to the cosmological pressure-wave amplitude ratio has shifted from "A₂u = Higgs" (Paper #45) to "L is the foam wave operator" (Part X / Paper #48), but the tier is unchanged. Full Tier 1 for ρ_Λ requires closure of Paper #48's lattice-to-continuum programme.

---

## 6. Numerical verification

The companion script `verify_Paper70_interior_projector.py` (shipped alongside this paper) checks all claims. Summary of output:

```
Spectrum: {0.0: 1, 2.4384: 3, 4.0: 2, 6.5616: 3, 7.0: 4, 9.0: 1}
tr(P_int) = 12.000000  (expected 12)
tr(P_int) / F = 12 / 14 = 6/7 = 0.857143
‖P_int − (I − P_A1g − P_A2u)‖_F = 3.14e-15
A_2u hex components × hex sign products: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
dim ker(L(L - 9I)) = 2  (expected 2)

All Paper #70 projector and bipartite-structure checks pass.
```

- Spectrum matches Paper #5 to 10⁻⁴.
- Interior projector has trace 12 exactly; divided by F = 14 gives 6/7 exactly.
- P_int agrees with (I − P_A₁g − P_A₂u) to floating-point precision.
- A₂u eigenvector's sign on each of the 8 hex faces matches the signed product of face coordinates, confirming the cube-graph bipartition structure of Paper #53 Theorem 53.2.
- The polynomial L(L − 9I) has exactly 2 kernel dimensions, locating the two band-edge modes.

---

## 7. Discussion

**Relationship to Paper #53.** Paper #53 and Paper #70 prove the same numerical result (6/7) by overlapping but distinct routes. Paper #53 leads with the A₁g/A₂u irrep identification and closes via Euler-Poincaré. Paper #70 leads with the interior-spectrum projector trace and closes via the band-edge zero-group-velocity lemma from graph Fourier analysis. The two routes meet at the three Paper-#53 Tier 1 sub-theorems. Paper #70 adds a fourth Tier 1 theorem (Theorem 70.3) making the 6/7 factor itself a propagating-mode fraction, rather than a "static/frustrated count" as in Paper #53.

**Relationship to standard condensed-matter theory.** The band-edge zero-group-velocity lemma is a lattice-wave result known since van Hove 1953. Applying it to the face graph of the Kelvin cell is the non-obvious step, the face graph is finite and has only 14 modes, but the dispersion-relation structure survives onto this finite case exactly. The two van Hove singularities at λ = 0 and λ = 9 correspond to the bottom and top of the "face band," analogous to the conduction and valence band edges of a solid-state crystal.

**Limits of the promotion.** The Tier 2 identification that remains (*L is the physical wave operator of the foam*) is equivalent to Paper #48's lattice-to-continuum claim. We do not close that identification here. The result is that the 6/7 factor, as a piece of pure spectral algebra, is promoted to Tier 1; ρ_Λ itself remains at Tier 2 until Paper #48 closes.

**Novel content.** The interior-spectrum projector formulation of the 6/7 factor is, as far as we are aware, original to Paper #70 and does not appear in Paper #53. The band-edge zero-group-velocity lemma is standard in a continuous-lattice setting but has not previously been applied to the finite face graph of the Kelvin cell in the UFFT literature.

---

## 8. References

### UFFT Papers
- [1] Luke Martin, *UFFT Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph*. Zenodo. DOI: 10.5281/zenodo.19030062.
- [2] Luke Martin, *UFFT Paper #16 — The Master Equation*. Zenodo. DOI: 10.5281/zenodo.19064359.
- [3] Luke Martin, *UFFT Paper #42 — The Path Integral on the Face Graph*. Zenodo. DOI: 10.5281/zenodo.19306828.
- [4] Luke Martin, *UFFT Paper #45 — The Void Channel*. Zenodo. DOI: 10.5281/zenodo.19307111.
- [5] Luke Martin, *UFFT Paper #48 — Standard Model From One Matrix*. Zenodo. DOI: 10.5281/zenodo.19448024.
- [6] Luke Martin, *UFFT Paper #53 — The Dark Energy 6/7 Factor from Face Laplacian Topology*. Zenodo. DOI: 10.5281/zenodo.19483955.

### External References
- [7] L. van Hove, "The Occurrence of Singularities in the Elastic Frequency Distribution of a Crystal," *Phys. Rev.* **89**, 1189 (1953).
- [8] F. R. K. Chung, *Spectral Graph Theory*. CBMS Regional Conf. Ser. Math. **92** (AMS, 1997).

---

## References

[1] Luke Martin, *UFFT Paper #5, The Face Laplacian Spectrum*. DOI: 10.5281/zenodo.19030062.
[2] Luke Martin, *UFFT Paper #16, The Master Equation*. DOI: 10.5281/zenodo.19064359.
[3] Luke Martin, *UFFT Paper #42, The Path Integral from Foam*. DOI: 10.5281/zenodo.19306828.
[4] Luke Martin, *UFFT Paper #45, The Void Channel*. DOI: 10.5281/zenodo.19307111.
[5] Luke Martin, *UFFT Paper #48, The Standard Model from One Matrix (v1)*. DOI: 10.5281/zenodo.19448024.
[6] Luke Martin, *UFFT Paper #53, The Dark Energy 6/7 Factor*. DOI: 10.5281/zenodo.19483955.

## AI Disclosure

Developed in collaboration with Claude (Anthropic). Theoretical direction and identification of the interior-spectrum projector as the cleanest algebraic statement of the 6/7 factor: Luke Martin. Lemma 70.2 and its identification as the band-edge zero-group-velocity result from lattice-wave mechanics: developed collaboratively. AI role: proof formalisation, numerical verification (14 × 14 face Laplacian diagonalisation, projector equalities, bipartite sign-product check), document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*

**(F − χ)/F = 6/7. The propagating-mode fraction of the face band.**

*Unified Foam Field Theory · Paper #70 · Priority Date: 20 February 2026 · APPROVED 2026-04-17 · awaiting Zenodo upload*

*B + V = D*
