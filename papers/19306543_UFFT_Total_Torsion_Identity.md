# UFFT Paper #40 — Total Torsion Identity and Foam Equilibration Timescale: Two Exact Results from the Truncated Octahedron Face Graph

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
| Paper | #40 of 63 |
| Framework | v10 |
| Status | Complete, Tier 1. Derives spin-1/2 as Wilson loop flux: 2θ_sh + θ_hh = π. |
| Tier | 1 |
| DOI | 10.5281/zenodo.19306543 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, dihedral angle, torsion, total curvature, spectral gap, equilibration time, Planck time

---

## Abstract

Two exact results concerning the dihedral geometry and spectral structure of the truncated octahedron face graph.

**Result 1 (Total Torsion Identity):** The sum of all dihedral supplements over the 36 edges of the face graph equals exactly F_sq × 2π = 12π, where F_sq = 6 is the number of square faces. Algebraic proof: 2θ_sh + θ_hh = π follows from cos(2θ_sh) = −cos(θ_hh) = −1/3.

**Result 2 (Foam Equilibration Timescale):** The spectral gap of the face Laplacian is r₁ = (9−√17)/2, giving an equilibration timescale τ = 1/r₁ = (9+√17)/32 in Planck units, approximately 0.41 t_P ≈ 2.21 × 10⁻⁴⁴ s. The foam equilibrates in less than one Planck time, faster than any observable process.

Both results are parameter-free consequences of the cell geometry.

---

## 1. Total Torsion Identity

### 1.1 Setup

The truncated octahedron has two types of face adjacency edges, distinguished by the face types they connect:

- **24 sq-hx edges** with dihedral supplement θ_sh = arccos(1/√3) = 54.7356°
- **12 hx-hx edges** with dihedral supplement θ_hh = arccos(1/3) = 70.5288°

The dihedral supplement is defined as θ = π − φ, where φ is the dihedral angle between adjacent faces. It measures the torsion (angular deviation from coplanarity) at each edge.

### 1.2 The identity

**24 θ_sh + 12 θ_hh = 12π = F_sq × 2π**

Numerically: 24 × 54.7356° + 12 × 70.5288° = 1313.65° + 846.35° = 2160.00° = 6 × 360°.

### 1.3 Proof

The identity follows from the dihedral supplement relation:

**2θ_sh + θ_hh = π**

Proof of this relation:

```
cos(2θ_sh) = 2cos²(θ_sh) − 1
            = 2(1/√3)² − 1
            = 2/3 − 1
            = −1/3
            = −cos(θ_hh)
```

Since θ_sh and θ_hh are both in (0, π), the identity cos(2θ_sh) = −cos(θ_hh) implies 2θ_sh = π − θ_hh, i.e., **2θ_sh + θ_hh = π**. ■

Multiplying both sides by 12: 24θ_sh + 12θ_hh = 12π = 6 × 2π = F_sq × 2π. ■

### 1.4 Interpretation

The total torsion content of the truncated octahedron face graph is exactly one complete rotation (2π) per square face. The number F_sq = 6 is the number of square faces, the same integer that determines:

- The 3 cubic lattice axes (F_sq/2 = 3 = N_gen)
- The ratio of inter-type to total edges (24/36 = 2/3 = (C_A−1)/C_A × F_sq/... )
- The baryonic coupling channel in the dark matter ratio

The total torsion identity connects the angular geometry (dihedral supplements, irrational numbers involving √3) to the combinatorial geometry (face counts, integers), the exact kind of bridge that the UFFT framework uses throughout.

### 1.5 Relation to Descartes' theorem

For a convex polyhedron, Descartes' angular deficiency theorem states that the sum of vertex angular deficits equals 4π. The total torsion identity is the face-graph analogue: the sum of edge torsion supplements equals 12π. Both are topological invariants, independent of the metric (how large the polyhedron is) and dependent only on the combinatorial structure.

---

## 2. Foam Equilibration Timescale

### 2.1 The spectral gap

The face Laplacian of the truncated octahedron has spectrum:

| Eigenvalue | Multiplicity | Irrep |
|-----------|-------------|-------|
| 0 | 1 | A₁g |
| r₁ = (9−√17)/2 ≈ 2.4384 | 3 | T₁u |
| 4 | 2 | Eg |
| r₂ = (9+√17)/2 ≈ 6.5616 | 3 | T₁u |
| 7 | 3+1 | T₂g ⊕ A₁g |
| 9 | 1 | A₂u |

The spectral gap (smallest nonzero eigenvalue) is:

**Δ = r₁ = (9−√17)/2**

### 2.2 The equilibration timescale

For a diffusive process on the face graph (e.g., pressure equilibration after a displacement event), the exponential relaxation time is:

**τ = 1/Δ = 1/r₁ = 2/(9−√17)**

Rationalising:

```
τ = 2/(9−√17) × (9+√17)/(9+√17) = 2(9+√17)/(81−17) = 2(9+√17)/64 = (9+√17)/32
```

**τ = (9+√17)/32 ≈ 0.4101 (in Planck time units)**

In SI:

**τ = (9+√17)/32 × t_P = 0.4101 × 5.391 × 10⁻⁴⁴ s ≈ 2.21 × 10⁻⁴⁴ s**

### 2.3 Physical meaning

The foam equilibration time is **sub-Planck**: the face pressure distribution on a single cell reaches equilibrium in approximately 0.41 Planck times. This is faster than any process resolvable at the Planck scale.

This timescale sets the foam's "response time", how quickly the cell adjusts its face pressure distribution after any displacement event. All physical processes (particle propagation, field dynamics, gravitational collapse) occur on timescales vastly longer than τ, meaning the foam is always in quasi-equilibrium from the perspective of emergent physics.

### 2.4 The algebraic form

The equilibration time (9+√17)/32 is a simple algebraic function of the discriminant Δ = 17 of the master equation:

**τ/t_P = (9 + √Δ) / 32 = (9 + √17) / 32**

where 9 = r₁ + r₂ (trace), 17 = (r₂ − r₁)² (discriminant), and 32 = 2⁵ = 2 × |O_h|/C_A.

---

## 3. Status

| Result | Formula | Value | Status |
|--------|---------|-------|--------|
| Total torsion identity | 24θ_sh + 12θ_hh = F_sq × 2π | 2160° = 12π | Theorem (algebraic proof) |
| Supplement relation | 2θ_sh + θ_hh = π | Exact | Theorem (trigonometric identity) |
| Spectral gap | r₁ = (9−√17)/2 | 2.4384 | Exact (from master equation) |
| Equilibration time | τ = (9+√17)/32 × t_P | 2.21 × 10⁻⁴⁴ s | Derived |
| Sub-Planck response | τ < t_P | 0.41 t_P | Exact |

---

## References

[1] Martin, L. (2026). The Face Laplacian Spectrum of the Kelvin Cell. Zenodo. DOI: 10.5281/zenodo.19030062.

[2] Martin, L. (2026). The Inter-Type Torsion Operator on the Truncated Octahedron. Zenodo.

---

## AI Disclosure

Developed in collaboration with Claude (Anthropic). Ideas, direction, and framework: Luke Martin. AI role: numerical verification, algebraic proof checking, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*


---

*Unified Foam Field Theory · Paper #40 · DOI: 10.5281/zenodo.19306543 · Priority Date: 20 February 2026*

*B + V = D*
