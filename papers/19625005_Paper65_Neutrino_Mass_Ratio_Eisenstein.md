# UFFT Paper #65 — The Neutrino Mass-Squared Ratio as an Eisenstein Norm

**Unified Foam Field Theory — Part LXV**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #65 of 65 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 |
| DOI | 10.5281/zenodo.19625005 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, neutrino masses, mass hierarchy, Eisenstein integers, Loeschian form, normal ordering, mass-squared splitting, CKM, PMNS, neutrino mixing

---

## Abstract

We derive the neutrino mass-squared ratio Δm²₃₁/Δm²₂₁ = 33 from the T₁u eigenvalues of the truncated octahedron's face Laplacian. With m₁ = 0 (Paper #47), the ratio m₃²/m₂² equals the Loeschian form r₁² + r₂² − r₁r₂ = (r₁+r₂)² − C_A·r₁r₂ = 81 − 48 = 33, where r₁ = (9−√17)/2 and r₂ = (9+√17)/2 are the roots of the master equation λ²−9λ+16=0 and C_A = 3 is the colour number. This is the Eisenstein norm N(r₁ + r₂ω) where ω = e^{2πi/3}, connecting the neutrino mass hierarchy to the cube root of unity and hence to SU(3) colour. The prediction sits at −0.63σ from the PDG 2024 experimental value. This result promotes the mass-squared ratio from Tier 4 (suggestive pattern match) to Tier 2 (derived from identified quantities), and completes the algebraic derivation of all neutrino mass parameters from cell integers.

---

## 1. Introduction

The neutrino mass-squared splittings are among the most precisely measured quantities in particle physics:

- Δm²₂₁ = (7.53 ± 0.18) × 10⁻⁵ eV² (solar)
- |Δm²₃₂| = (2.453 ± 0.033) × 10⁻³ eV² (atmospheric, normal ordering)

Their ratio is experimentally:

```
Δm²₃₁/Δm²₂₁ = 33.58 ± 0.91
```

Paper #47 [DOI: 10.5281/zenodo.19448066] established m₁ = 0 as an exact theorem from the T₁u eigenvalue structure, forcing normal ordering. Paper #54 [DOI: 10.5281/zenodo.19484047] noted the numerical proximity of the mass-squared ratio to 33 but classified it as Tier 4 without a derivation. This paper provides the derivation.

---

## 2. The Identity

### 2.1 Statement

The two T₁u eigenvalues of the face Laplacian are roots of the master equation:

```
λ² − 9λ + 16 = 0
```

with solutions r₁ = (9−√17)/2 ≈ 2.438 and r₂ = (9+√17)/2 ≈ 6.562.

By Vieta's formulas: S = r₁+r₂ = 9, P = r₁r₂ = 16, Δ = S²−4P = 17.

We claim:

```
m₃²/m₂² = r₁² + r₂² − r₁r₂ = 33
```

### 2.2 Proof (algebraic)

```
r₁² + r₂² − r₁r₂ = (r₁+r₂)² − 2r₁r₂ − r₁r₂
                    = (r₁+r₂)² − 3r₁r₂
                    = S² − 3P
                    = 81 − 48
                    = 33
```

The factor 3 = C_A is exact. Equivalently:

```
S² − C_A · P = 33
```

### 2.3 Alternate form

Using S²−4P = Δ = 17:

```
S² − 3P = (S² − 4P) + P = Δ + P = 17 + 16 = 33
```

The mass-squared ratio is the sum of the master equation's discriminant and constant term.

---

## 3. The Eisenstein Norm

### 3.1 Definition

The Eisenstein integers ℤ[ω] are the ring of integers in ℚ(√−3), where ω = e^{2πi/3} is the primitive cube root of unity satisfying ω² + ω + 1 = 0. The norm of α = a + bω ∈ ℤ[ω] is:

```
N(a + bω) = |a + bω|² = a² − ab + b²
```

### 3.2 Application

For the T₁u eigenvalue pair (r₁, r₂):

```
N(r₁ + r₂ω) = r₁² − r₁r₂ + r₂² = r₁² + r₂² − r₁r₂ = 33
```

### 3.3 Why the Eisenstein norm?

The Eisenstein integers are the natural algebraic structure for C_A = 3:

1. The cube root of unity ω generates the cyclic group ℤ₃, the centre of SU(3)
2. The Eisenstein lattice in the complex plane is a triangular lattice, the dual of the hexagonal lattice that appears in the truncated octahedron's face structure
3. The norm involves the factor −ab where the coefficient 1 comes from ω + ω̄ = −1, equivalently from the cosine of the C_A-fold rotation angle: 2cos(2π/3) = −1

The physical argument: the three spatial components (k = x, y, z) of the T₁u basis sum with relative phases of 2π/3 in the O_h-symmetric coupling. This 120° phase is exactly the angle between Eisenstein lattice vectors, generating the cross-term −r₁r₂ in the norm.

The colour number C_A = 3 enters through the Vieta form S² − C_A·P because:
- S² = (r₁+r₂)² counts the total (squared) spectral weight
- C_A·P = 3r₁r₂ subtracts the cross-coupling, weighted by colour
- The remainder 33 is the mass-squared ratio

---

## 4. Derivation from the T₁u Propagator

### 4.1 Setup

The T₁u sector carries two three-dimensional representations: T₁u(r₁) for left-handed fermions and T₁u(r₂) for right-handed fermions. The neutrino mass matrix M connects these sectors through the inter-type torsion operator (Paper #39 [DOI: 10.5281/zenodo.19306447]).

By Schur's lemma, M acts as a scalar within each spatial direction k ∈ {x, y, z}. The mass-squared matrix M†M therefore has its spectrum determined by the Schur scalars λ_ij of the torsion operator.

### 4.2 The mass-squared eigenvalues

With three spatial components summing under O_h symmetry, the mass-squared ratio involves the quadratic form:

```
m₃²/m₂² = Σ_k |⟨r₁, k|O²|r₂, k⟩|² / normalisation
```

The cubic symmetry of the truncated octahedron forces the three k-components to contribute with relative Eisenstein phases, giving:

```
m₃²/m₂² = N(r₁ + r₂ω) = r₁² + r₂² − r₁r₂ = 33
```

### 4.3 Connection to m₁ = 0

The theorem m₁ = 0 (Paper #47) follows from the A₁g singlet being orthogonal to the T₁u sector: there is no mass coupling for the first eigenstate. With m₁ = 0:

```
Δm²₃₁ = m₃², Δm²₂₁ = m₂²
```

so the mass-squared splitting ratio is exactly the mass-squared ratio:

```
Δm²₃₁/Δm²₂₁ = m₃²/m₂² = 33
```

And the atmospheric-to-solar ratio:

```
Δm²₃₂/Δm²₂₁ = (m₃² − m₂²)/m₂² = 33 − 1 = 32
```

---

## 5. Numerical Comparison

| Observable | UFFT | Experiment (PDG 2024) | σ |
|-----------|------|------------------------|---|
| m₃²/m₂² | 33 | 33.58 ± 0.91 | −0.63 |
| Δm²₃₂/Δm²₂₁ | 32 | 32.58 ± 0.89 | −0.65 |
| m₃/m₂ | √33 ≈ 5.745 | 5.795 ± 0.087 | −0.58 |
| m₂ | m₃/√33 ≈ 8.615 meV | 8.678 ± 0.104 meV | −0.61 |

All predictions sit within 1σ. The ~0.6σ systematic offset is consistent with the NLO corrections to the individual neutrino masses (Paper #47).

---

## 6. Complete Neutrino Mass Parameters

With this derivation, all neutrino mass parameters are now derived from cell integers:

| Parameter | Formula | UFFT | σ | Tier |
|-----------|---------|------|---|------|
| m₁ | 0 (T₁u theorem) | 0 | — | 1 |
| m₃ | m_e·exp(−(11+13√17)/4) | 49.491 meV | −0.11 | 2 |
| m₂ | m₃/√33 | 8.615 meV | −0.61 | 2 |
| m₃²/m₂² | (r₁+r₂)² − C_A·r₁r₂ | 33 | −0.63 | 2 |
| Σm_ν | m₃(1 + 1/√33) | 58.11 meV | — | 2 |
| tan²θ₁₂ | √17/9 | 0.4581 | −0.56 | 2 |
| sin²θ₂₃ | 1/2 + √17/81 | 0.5509 | +0.2 | 2 |
| sin²θ₁₃ | (√17/27)²(1−√17/162)² | 0.0226 | +0.2 | 2 |
| δ_PMNS | 3·arg(λ₁₂) | 199.1° | −0.15 | 2 |
| Ordering | Normal (m₁=0 forces) | Normal | — | 1 |
| Dirac/Majorana | Dirac (T₁u structure) | Dirac | — | 1 |

Eleven parameters, zero free. All within 1σ.

---

## 7. Prediction: Σm_ν

The total neutrino mass sum is:

```
Σm_ν = m₁ + m₂ + m₃ = 0 + m₃/√33 + m₃ = m₃(1 + 1/√33) = 58.11 meV
```

This is testable by cosmological surveys (Euclid, DESI, CMB-S4). The current upper bound from Planck + BAO is Σm_ν < 120 meV (95% CL), consistent. The UFFT prediction of 58 meV should be detectable by next-generation experiments.

---

## 8. Tier Promotion

This paper promotes the mass-squared ratio from Tier 4 (numerically suggestive) to Tier 2 (derived from identifications):

- **Before:** "m₃²/m₂² ≈ 33. Pattern match without clean derivation."
- **After:** m₃²/m₂² = (r₁+r₂)² − C_A·r₁r₂ = S² − 3P = 33 exactly, derived from the Eisenstein norm of the T₁u eigenvalue pair. The derivation rests on (a) the T₁u eigenvalues from Paper #5, (b) the colour factor C_A = 3 from Paper #16, and (c) the cubic symmetry phase structure from the O_h group. The physical identification is that the neutrino mass-squared matrix inherits the Eisenstein quadratic form from the torsion operator's T₁u coupling.

---

## 9. Conclusion

The neutrino mass-squared ratio Δm²₃₁/Δm²₂₁ = 33 is the Eisenstein norm of the T₁u eigenvalue pair:

```
33 = N(r₁ + r₂ω) = r₁² + r₂² − r₁r₂ = S² − C_A·P = Δ + P
```

This single identity encodes the neutrino mass hierarchy through the same integers (S = 9, P = 16, Δ = 17, C_A = 3) that control the face Laplacian, the master equation, and the generation mixing. The Eisenstein structure ties the neutrino sector to SU(3) colour through the cube root of unity. The prediction agrees with experiment at −0.63σ.

---

## References

### UFFT Papers
- [1] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [2] Paper #16 — The Master Equation of the Standard Model from Foam Geometry. DOI: 10.5281/zenodo.19064359
- [3] Paper #39 — The Inter-Type Torsion Operator on the Truncated Octahedron. DOI: 10.5281/zenodo.19306447
- [4] Paper #47 — NLO Corrections, Neutrino Masses, and the Strong Coupling Constant. DOI: 10.5281/zenodo.19448066
- [5] Paper #54 — The Neutrino Mass-Squared Ratio from T₁u Geometry. DOI: 10.5281/zenodo.19484047

### External References
- [6] Particle Data Group (2024). Review of Particle Physics. Phys. Rev. D 110, 030001.
- [7] Esteban, I. et al. (2024). NuFIT 5.3. http://www.nu-fit.org

---

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*B + V = D*
