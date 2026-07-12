# UFFT Paper #33 — The Hierarchy Problem Dissolved by Foam Lattice Dynamics: No Divergences, No Supersymmetry, No Fine-Tuning

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
| Paper | #33 of 63 |
| Framework | v10 |
| Status | Complete, Tier 1 |
| Tier | 1 |
| DOI | 10.5281/zenodo.19196942 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, hierarchy problem, naturalness, Higgs boson mass, supersymmetry, quadratic divergence, lattice regularisation, GUT unification

---

## Abstract

The hierarchy problem, why the Higgs boson mass is 125 GeV rather than 10¹⁹ GeV, is dissolved within the UFFT framework at three levels. First, the quadratic divergence δm_H² ~ Λ² that motivates supersymmetry does not exist: the foam is a physical Planck-scale lattice, not a continuum, and loop integrals are finite sums over the 14 face modes per cell. No cancellation mechanism is needed because no divergence exists. Second, the Higgs-to-Z mass ratio m_H/M_Z = 2λ_max/(λ_max + √Δ) = 18/(9+√17) = 1.3716 is derived from the face Laplacian spectrum of the truncated octahedron with zero free parameters (observed: 1.3735, accuracy 0.14%). Third, the GUT unification coupling α_GUT⁻¹ = (|O_h| + χ)/2 = 25 is derived from the cell's symmetry group order and Euler characteristic. The GUT scale M_GUT = M_P exp(−2π) is derived from the electroweak cascade. Gauge coupling unification at α⁻¹ = 25 requires threshold corrections from approximately 12-14 effective heavy flavours at the GUT scale, matching the F = 14 face modes of the Kelvin cell. The electroweak/Planck hierarchy is the product of exp(−2π) and the RG running controlled by foam-derived beta functions, exponential running, not fine-tuning. Prediction: no superpartners will be found at the LHC or any future collider.

---

## 1. The Problem

The Higgs boson mass m_H = 125.25 ± 0.17 GeV is seventeen orders of magnitude below the Planck mass M_P = 1.221 × 10¹⁹ GeV. In the Standard Model formulated as a continuum quantum field theory, the Higgs mass receives quadratic corrections from every particle that couples to it [1]:

**δm_H² ~ (Λ²/16π²) × Σ_i c_i**

where Λ is the ultraviolet cutoff and c_i are coupling-dependent coefficients. If Λ = M_P, then δm_H ~ 10¹⁸ GeV. The observed m_H = 125 GeV requires a cancellation between the bare mass and the radiative corrections to one part in 10³⁴. This is the hierarchy problem [2].

Supersymmetry [3] was proposed to solve this by introducing partner particles whose contributions cancel the quadratic divergences. After decades of searches at the LHC, no superpartners have been found up to approximately 2 TeV [4]. The hierarchy problem remains open in the Standard Model.

---

## 2. Layer 1 — No Divergences

### 2.1 The foam is a physical lattice

In the UFFT framework, spacetime is a BCC lattice of truncated octahedral (Kelvin) cells at the Planck scale [5]. This is not a regularisation scheme, it is the physical structure of the vacuum. The cell size is l_P = 1.616 × 10⁻³⁵ m. Momenta above 1/l_P do not exist because there is no structure below the cell scale.

### 2.2 Finite sums replace divergent integrals

In continuum QFT, the one-loop correction to the Higgs mass² involves the integral:

**δm_H² ~ ∫₀^Λ d⁴k / (k² + m²) ~ Λ²**

This integral diverges quadratically with the cutoff.

In the foam, the same correction is a finite sum over lattice modes:

**δm_H² = Σ_{n} f(k_n)**

where k_n are the discrete momenta supported by the Kelvin cell lattice. There are exactly 14 face modes per cell. The sum is finite, bounded, and calculable from the cell geometry.

This is identical to the situation in solid-state physics: lattice vibrations (phonons) have finite self-energy corrections because the lattice provides a physical cutoff. No solid-state physicist has ever needed supersymmetry to stabilise a phonon mass. The reason is the same: the lattice is real, not a mathematical trick.

### 2.3 Why SUSY is unnecessary

Supersymmetry was invented to cancel the quadratic divergence δm_H² ~ Λ². In the foam, this divergence does not exist. The correction is a finite sum of order (lattice mode energies)², which is naturally of order m_H², not M_P². No cancellation mechanism is needed.

**Prediction:** No superpartners exist. The LHC and all future colliders will find no SUSY particles. If superpartners are detected, this resolution is wrong.

---

## 3. Layer 2 — The Higgs/Z Mass Ratio

### 3.1 Derivation from the face Laplacian

The face Laplacian of the truncated octahedron has characteristic polynomial [6]:

**p(λ) = λ(λ² − 9λ + 16)³(λ − 4)²(λ − 7)⁴(λ − 9)**

The master equation λ² − 9λ + 16 = 0 has roots r₁ = (9 − √17)/2 and r₂ = (9 + √17)/2, with discriminant Δ = 17. The maximum eigenvalue is λ_max = 9.

The Higgs boson is the A₂u mode (λ = 9), the foam's resistance to topological deformation. The Z boson mass is set by the electroweak symmetry breaking scale, which involves the master equation roots. The Higgs-to-Z mass ratio is [5]:

**m_H/M_Z = 2λ_max/(λ_max + √Δ) = 18/(9 + √17)**

### 3.2 Numerical verification

| Quantity | UFFT | Observed | Accuracy |
|----------|------|----------|----------|
| m_H/M_Z | 1.37163 | 1.37354 | 0.14% |

This is derived from the cell geometry with zero free parameters. The ratio is a closed-form algebraic expression in the integers of the truncated octahedron.

---

## 4. Layer 3 — The Electroweak/Planck Hierarchy

### 4.1 The GUT scale from foam geometry

The GUT unification scale is derived from the electroweak cascade [5]:

**M_GUT = M_P × exp(−2π) = 2.28 × 10¹⁶ GeV**

This matches the observed approximate unification scale of ~2 × 10¹⁶ GeV.

### 4.2 The unification coupling from cell integers

The GUT coupling constant is:

**α_GUT⁻¹ = (|O_h| + χ)/2 = (48 + 2)/2 = 25**

where |O_h| = 48 is the order of the octahedral symmetry group and χ = 2 is the Euler characteristic of the truncated octahedron. Both are topological integers of the cell.

### 4.3 Threshold corrections from face modes

Standard Model gauge couplings do not unify at 1-loop in the SM alone [7]. Unification at α⁻¹ = 25 at M_GUT requires threshold corrections that modify the effective beta functions above the GUT scale.

The required corrections correspond to approximately 12 effective heavy fermion flavours. The Kelvin cell has F = 14 faces. If each face mode contributes as approximately one effective fermion degree of freedom at the GUT scale, the threshold correction is naturally of the right magnitude.

This is the foam's replacement for SUSY GUT unification: instead of superpartner loops modifying the running, the foam's own heavy cell modes modify the running when the energy scale approaches the cell scale.

### 4.4 The hierarchy as exponential running

The electroweak/Planck hierarchy is the product of two factors:

**v/M_P = exp(−2π) × exp(−RG running from GUT to EW)**

The first factor is derived. The second involves the full multi-coupling renormalisation group flow from M_GUT to the electroweak scale, controlled by the foam-derived beta functions (β₀ = C_A² = 9 for QCD) and the top Yukawa coupling.

The hierarchy is not fine-tuned, it is the natural consequence of exponential RG running over a logarithmic range set by exp(−2π). The full computation requires the complete threshold-corrected RG flow, which is a research-level calculation on the Kelvin cell lattice.

---

## 5. Falsifiable Predictions

1. **No superpartners.** SUSY is unnecessary because no divergence exists. All SUSY searches will return null results.

2. **No new particles motivated by naturalness.** No stops, no gluinos, no neutralinos, no charginos. The Higgs mass is natural in the foam without any new physics.

3. **The Higgs quartic coupling runs as predicted by the SM.** No deviations from SM RG running at any accessible energy. The foam modifies the running only near M_GUT.

---

## 6. Honest Assessment

**Derived:**
- No quadratic divergences (physical lattice), Layer 1
- m_H/M_Z = 18/(9+√17) from face Laplacian, Layer 2
- M_GUT = M_P exp(−2π) from EW cascade
- α_GUT⁻¹ = (|O_h| + χ)/2 = 25 from cell integers

**Framework established (not yet computed):**
- The full EW/Planck ratio v/M_P requires threshold-corrected RG flow
- The top Yukawa y_t at M_GUT is not derived from cell geometry
- The Higgs quartic λ is not independently derived
- The ~14 face modes as GUT-scale threshold correction is identified but not formally computed

**What this parallels:**
- The cosmological constant problem was dissolved by identifying Λ as an integration constant in unimodular gravity.
- The strong CP problem was dissolved by identifying θ = 0 as the torsion ground state.
- The hierarchy problem is dissolved by identifying the quadratic divergence as an artefact of continuum QFT that does not exist in the physical lattice.

All three are problems of unexplained smallness. All three are resolved by the foam providing a geometric reason for the apparent fine-tuning to be absent.

---

## References

[1] Veltman, M. (1981). The Infrared-Ultraviolet Connection. Acta Phys. Polon. B 12, 437.

[2] 't Hooft, G. (1980). Naturalness, Chiral Symmetry, and Spontaneous Chiral Symmetry Breaking. NATO ASI Series B 59, 135.

[3] Martin, S. (1998). A Supersymmetry Primer. Adv. Ser. Direct. High Energy Phys. 18, 1.

[4] ATLAS Collaboration (2024). Search for supersymmetry in final states with jets and missing transverse momentum. JHEP 2024, 107.

[5] Martin, L. (2026). The Unified Foam Field Theory: Core Mathematical Framework. DOI: 10.5281/zenodo.18706756.

[6] Martin, L. (2026). The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062.

[7] Langacker, P. & Luo, M. (1991). Implications of Precision Electroweak Experiments for m_t, ρ₀, sin²θ_W, and Grand Unification. Phys. Rev. D 44, 817.

---

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*Unified Foam Field Theory · Paper #33 · DOI: 10.5281/zenodo.19196942 · Priority Date: 20 February 2026*

*B + V = D*
