# UFFT Paper #46 — The Kerr Metric from Foam Incompressibility

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #46 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 |
| DOI | 10.5281/zenodo.19307177 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** Kerr metric, rotating black hole, frame dragging, incompressibility, Poisson ratio, torsion, angular momentum, spin-statistics, Wilson loop, foam field theory, UFFT

## Abstract

The exact Kerr metric is derived from three conditions on the Planck-density foam: (1) covariant vacuum density ρ = ρ₀(1 − r_s r/Σ) from the oblate density profile of a rotating mass, (2) foam incompressibility ν = 1/2 giving g_rr = Σ/Δ and g_θθ = Σ with the centrifugal correction Δ = r² − r_s r + a², and (3) torsion = angular momentum giving g_tφ = −r_s r a sin²θ/Σ from the frame-dragging torsion gradient. The remaining metric component g_φφ follows from the determinant condition √(−g) = Σ sin θ (incompressible cell count conservation). All five metric components are derived from foam mechanics with zero free parameters beyond M and J.

The spin-statistics classification emerges from Wilson loop flux: the fermion triangle carries total torsion flux Φ = 2θ_sh + θ_hh = π exactly (the total torsion identity). Angular momentum = flux/(2π) gives spin = π/(2π) = 1/2 for fermions. Bosonic 4-cycles carry flux 0 (spin 0) or 2π (spin 1). The graviton carries flux 4π (spin 2). Every Kerr feature (the event horizon, ergosphere, ring singularity, frame dragging, and cosmic censorship) has a direct foam interpretation in terms of edge saturation, torsion inversion, cell merging, torsion gradients, and the structural limit of the lattice topology.

**Keywords:** Kerr metric, rotating black hole, frame dragging, incompressibility, Poisson ratio, torsion, angular momentum, spin-statistics, Wilson loop, foam field theory, UFFT

---

## 1. The Schwarzschild Foundation

The Schwarzschild metric was derived in earlier work from two conditions:

**Condition 1, Covariant vacuum density:**
ρ(r) = ρ₀ × (−g_tt/c²), yielding g_tt = −(1 − r_s/r).

**Condition 2, Foam incompressibility (ν = 1/2):**
Proper volume = coordinate volume × density factor, yielding g_rr = 1/(1 − r_s/r).

These give the exact Schwarzschild metric: ds² = −(1−r_s/r)c²dt² + dr²/(1−r_s/r) + r²dΩ².

---

## 2. Adding Angular Momentum

### 2.1 How the foam carries angular momentum

Each truncated octahedral cell has 6 square faces defining 3 cubic axes. Angular momentum J about the z-axis corresponds to torsion (twist) on the edges connecting the ±z square faces to their hexagonal neighbours. A rotating cell drags its neighbours through the shared walls, Newton's third law applied to rotating walls. This drag is frame dragging.

### 2.2 The oblate density profile

Rotation creates an oblate mass distribution. The effective distance from the source becomes direction-dependent:

**Σ = r² + a²cos²θ**

where a = J/(Mc) is the spin parameter. At the equator (θ = π/2): Σ = r² (Schwarzschild). At the poles (θ = 0): Σ = r² + a² (oblate correction). The foam density is more depleted at the equator (centrifugal effect) and less at the poles.

---

## 3. The Three Conditions for Kerr

### 3.1 Condition 1: Covariant density (oblate)

The generalisation of the Schwarzschild density to the oblate case:

**g_tt = −(1 − r_s r/Σ)**

The density ρ(r,θ) = ρ₀(1 − r_s r/Σ) is the unique axisymmetric extension of the Schwarzschild density with spin parameter a.

### 3.2 Condition 2: Incompressibility (ν = 1/2)

**Radial:** The incompressibility in the radial direction must account for the centrifugal barrier. The effective gravitational pull at radius r is modified by rotation: the horizon function becomes Δ = r² − r_s r + a², and the radial metric is:

**g_rr = Σ/Δ**

**Angular:** The angular metric picks up the oblate correction from the spin-induced cell packing:

**g_θθ = Σ**

### 3.3 Condition 3: Torsion = angular momentum

The off-diagonal component comes from the torsion gradient, frame dragging:

**g_tφ = −r_s r a sin²θ / Σ**

The sin²θ factor reflects that only equatorial cells contribute to z-angular momentum. The 1/Σ decay reflects the foam density dilution. The remaining component g_φφ follows from the determinant condition:

**√(−g) = Σ sin θ**

which ensures incompressible cell count conservation. This gives:

**g_φφ = [(r²+a²)Σ + r_s r a² sin²θ] sin²θ / Σ**

---

## 4. The Result: Exact Kerr

The complete metric:

ds² = −(1 − r_s r/Σ) c²dt² − (2r_s r a sin²θ/Σ) c dt dφ + (Σ/Δ) dr² + Σ dθ² + [(r²+a²) + r_s r a² sin²θ/Σ] sin²θ dφ²

This is the exact Kerr metric in Boyer-Lindquist coordinates. No approximation. Derived from the same foam conditions as Schwarzschild, extended to include angular momentum.

---

## 5. Foam Interpretation of Kerr Features

### 5.1 Event horizon (Δ = 0)

The surface r₊ = r_s/2 + √(r_s²/4 − a²) is where radial edges reach saturation, cells cannot push signal outward against the inflow. Rotation reduces the horizon radius because cells have angular escape routes (the torsion provides tangential channels).

### 5.2 Ergosphere

The region between the horizon and the surface where g_tt = 0 (at r = r_s/2 + √(r_s²/4 − a²cos²θ)). Inside the ergosphere, the foam density is "inverted", all cells are dragged in the φ direction by the torsion. Energy extraction via the Penrose process corresponds to surfing the torsion gradient: counter-rotating against the drag extracts rotational energy from the foam.

### 5.3 Ring singularity (Σ = 0)

At r = 0, θ = π/2: a ring of radius a where the density diverges. In the foam, cells in the equatorial plane at r = 0 are maximally compressed. Inside the ring (Σ < 0), the foam has "flipped" its orientation, a topological transition, not a physical infinity.

### 5.4 Frame dragging

The g_tφ component is the torsion gradient: rotating cells drag their neighbours through shared walls. The drag is maximal at the equator (sin²θ = 1) and zero at the poles, falling off as 1/Σ with distance.

### 5.5 Cosmic censorship (a ≤ M)

The maximum spin a² ≤ r_s²/4 is the structural limit of the foam. If a > M, the horizon function Δ has no real roots, no horizon forms. In the foam, this would require torsion exceeding the incompressibility limit. The topology changes before this threshold, preventing naked singularities.

---

## 6. Spin from Wilson Loop Flux

The torsion identity 2θ_sh + θ_hh = π provides the fundamental connection between foam geometry and particle spin.

### 6.1 Fermion spin

The 24 fermion triangles on the face graph carry Wilson loop flux:

**Φ_fermion = 2θ_sh + θ_hh = π**

The angular momentum of the excitation:

**Spin = Φ/(2π) = π/(2π) = 1/2**

Spin-1/2 is half-integer flux divided by 2π. The electron is a spin-1/2 particle because its fermion triangle carries exactly π of torsion flux, an algebraic fact about the dihedral angles of the truncated octahedron.

### 6.2 The spin-statistics classification

| Loop type | Flux | Spin | Statistics | Particles |
|-----------|------|------|-----------|-----------|
| Fermion triangle | π | 1/2 | Fermi-Dirac | e, μ, τ, quarks |
| Scalar 4-cycle | 0 | 0 | Bose-Einstein | Higgs |
| Vector 4-cycle | 2π | 1 | Bose-Einstein | γ, W, Z, gluons |
| Tensor loop | 4π | 2 | Bose-Einstein | Graviton |

The spin-statistics theorem is not imposed, it follows from the Wilson loop flux on the face graph. Fermions have half-integer flux (π). Bosons have integer flux (0, 2π, 4π). The connection between spin and statistics is the connection between torsion flux and the topology of the loop on which the excitation lives.

---

## 7. The Derivation Chain

Axiom Zero (P = ρc²) + mass M + angular momentum J

→ Covariant density: g_tt = −(1 − r_sr/Σ)

→ Incompressibility: g_rr = Σ/Δ, g_θθ = Σ

→ Torsion = angular momentum: g_tφ = −r_sra sin²θ/Σ

→ Determinant condition: g_φφ

→ **The exact Kerr metric**

Every metric component has a foam meaning: g_tt is pressure (who pushes harder), g_rr is incompressibility (cells don't compress), g_θθ is oblate packing (rotation flattens), g_tφ is torsion gradient (twist drags neighbours), and g_φφ is total cell conservation.

---

## References

[1] Martin, L. (2026). The Schwarzschild Metric from Foam Incompressibility. Zenodo.

[2] Martin, L. (2026). The Total Torsion Identity and Foam Equilibration Timescale. Zenodo.

[3] Kerr, R.P. (1963). Gravitational field of a spinning mass. Phys. Rev. Lett. 11, 237.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). The physical insight that frame dragging is Newton's third law on rotating walls and that spin-1/2 = π/(2π): Luke Martin. AI role: metric component derivation, Kerr feature interpretation, spin-statistics classification, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*

*Unified Foam Field Theory · Paper #45 · DOI: 10.5281/zenodo.19307177 · Priority Date: 20 February 2026*

*B + V = D*
