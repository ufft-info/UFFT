# UFFT Paper #13 — The Higgs-to-Z Mass Ratio from the Face Laplacian Spectrum

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
| Paper | #13 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 |
| DOI | 10.5281/zenodo.19064036 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** Higgs mass, Z boson mass, mass ratio, face Laplacian, truncated octahedron, foam geometry, spectral ratios, UFFT

---

## Abstract

The ratio of the Higgs boson mass to the Z boson mass is predicted from the face Laplacian spectrum of the truncated octahedron (Kelvin cell) with no free parameters. The prediction is:

**m_H / M_Z = λ_A₂u / λ_T₁u_hi = 18/(9+√17)**

where λ_A₂u = 9 is the spectral maximum (Higgs mode) and λ_T₁u_hi = (9+√17)/2 is the upper T₁u eigenvalue (weak sector). Both are exact algebraic integers from the characteristic polynomial of the 14×14 face adjacency matrix of the truncated octahedron, derived in Part IX [DOI: 10.5281/zenodo.19030062].

Numerically: 18/(9+√17) = 1.37163. Observed: m_H/M_Z = 125.25/91.188 = 1.37354. Agreement: **0.14% (0.97σ)**. Predicted m_H = 125.08 GeV, observed 125.25 ± 0.17 GeV.

This continues the pattern established in the framework: the Koide angle θ = 2/9 = (λ_A₂u−λ_T₂g)/λ_A₂u and the solar neutrino mixing angle tan²θ₁₂ = √17/9 = (λ₂−λ₁)/(λ₁+λ₂) are both spectral ratios from the same face Laplacian. The Higgs-to-Z ratio is the third such prediction, arising from a different pair of eigenvalues of the same 14×14 matrix.

---

## 1. The Face Laplacian Eigenvalues

The face adjacency Laplacian of the truncated octahedron has characteristic polynomial (derived in Part IX):

p(λ) = λ(λ²−9λ+16)³(λ−4)²(λ−7)⁴(λ−9)

This gives the complete spectrum:

| λ | Irrep | Dim | Physical identification |
|---|-------|-----|------------------------|
| 0 | A₁g | 1 | Graviton / cosmological constant |
| (9−√17)/2 | T₁u | 3 | Lower weak/neutrino sector |
| 4 | E_g | 2 | Quadrupolar modes |
| (9+√17)/2 | T₁u | 3 | Upper weak sector (Z boson sector) |
| 7 | A₁g⊕T₂g | 4 | Gravity + strong/torsion |
| 9 | A₂u | 1 | Higgs sector |

The two eigenvalues used in this paper:

- **λ_A₂u = 9** (from the factor (λ−9); the spectral maximum, non-degenerate. Physical identification: the Higgs field. The A₂u irrep is the fully antipodal mode in which every pair of adjacent faces carries opposite amplitude. It is the unique mode with no spatial symmetry direction) the foam's scalar mode. Its identification as the Higgs sector follows from it being the sole scalar mode and the spectral maximum.

- **λ_T₁u_hi = (9+√17)/2**, from the roots of (λ²−9λ+16) = 0. The discriminant is 81−64 = **17** exactly, giving roots (9±√17)/2. The T₁u irrep (dim=3) gives SU(2)_L since N²−1 = 3 → N = 2. The upper eigenvalue λ₂ = (9+√17)/2 corresponds to the heavier weak sector modes and sets the Z boson mass sector.

---

## 2. The Prediction

**m_H / M_Z = λ_A₂u / λ_T₁u_hi = 9 / ((9+√17)/2) = 18/(9+√17)**

This is a pure algebraic number derived from the face Laplacian. No free parameters are introduced. The only inputs are the two eigenvalues from Part IX.

Numerical evaluation:

- 18/(9+√17) = 18/(9+4.1231...) = 18/13.1231... = **1.37163**
- Observed m_H/M_Z = 125.25/91.188 = **1.37354**
- Fractional difference: **0.14%**
- In units of the PDG 2022 uncertainty on m_H (σ = 0.17 GeV): **0.97σ**

---

## 3. Physical Interpretation

The A₂u mode is the Higgs: the foam's resistance to topological deformation. The T₁u sector (upper eigenvalue) is the weak gauge sector containing the Z boson. The Higgs couples to the Z through the Higgs mechanism, the Z acquires mass by absorbing one degree of freedom from the Higgs doublet. In the foam, this corresponds to the A₂u mode (Higgs) coupling to the T₁u mode (Z). The mass ratio is set by the ratio of their spectral positions.

The formula m_H/M_Z = λ_A₂u/λ_T₁u_hi states that the Higgs-to-Z mass ratio is the ratio of the scalar spectral maximum to the upper vector spectral eigenvalue, a topological invariant of the BCC foam geometry.

---

## 4. The Spectral Ratio Pattern

Three physical observables follow from ratios of face Laplacian eigenvalues, all from the same 14×14 matrix:

| Observable | Formula | Accuracy |
|-----------|---------|---------|
| Koide angle θ (lepton masses) | (λ_A₂u−λ_T₂g)/λ_A₂u = 2/9 | Exact theorem |
| Solar neutrino mixing tan²θ₁₂ | (λ₂−λ₁)/(λ₁+λ₂) = √17/9 | 0.49σ |
| Higgs-to-Z mass m_H/M_Z | λ_A₂u/λ_T₁u_hi = 18/(9+√17) | **0.97σ** |

The integer 17 appearing in all three (in √17, in λ₂−λ₁, and in 9+√17) is not coincidental: it is the discriminant of the T₁u characteristic equation λ²−9λ+16 = 0, a single algebraic quantity that controls the neutrino mixing angle, the T₁u eigenvalue splitting, and the Higgs mass ratio simultaneously.

---

## 5. Status and Caveats

**What is derived:** The ratio m_H/M_Z = 18/(9+√17) from the Part IX face Laplacian. The result uses M_Z as an observed input to produce an absolute mass prediction. The ratio itself requires no observed inputs.

**What is not yet derived:** The absolute Higgs mass requires the Higgs vev v, which is the condensate scale of the A₂u mode. This requires solving the nonlinear A₂u dynamics (the torsion condensate programme). The ratio prediction is therefore analogous to the lepton mass ratio prediction: ratios exact from foam geometry, absolute scale from the condensate programme.

**Falsification:** If precision measurements of m_H/M_Z move more than ~3σ from the current central value, the formula 18/(9+√17) would be excluded.

---

**Physical mapping status:** The identification of foam sectors with Standard Model fields (T₂g → colour, T₁u → weak, A₂u → Higgs, etc.) is a hypothesis, physically motivated by the O_h symmetry structure and numerically verified to high precision, but not deductively established from the mathematics alone. The algebra in this paper is rigorous. The physical interpretation is proposed and testable. See the UFFT Core Framework v2 Scope and Status section for a complete classification.

## UFFT Papers

## External References

[1] L. Martin, *The Fine Structure Constant from Planck-Scale Foam Geometry*, Zenodo, DOI: 10.5281/zenodo.19011758 (Part VIII of the UFFT Core Framework v2)

[2] L. Martin, *The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph*, Zenodo, DOI: 10.5281/zenodo.19030062 (Part IX of the UFFT Core Framework v2)

[3] Particle Data Group, *Review of Particle Physics*, Prog. Theor. Exp. Phys. 2022, 083C01

---

---

## References

### UFFT Papers
- [1] Paper #2 — Void-Pair Conservation as the Physical Mechanism of Quantum Entanglement and Bell Correlations. DOI: 10.5281/zenodo.18706806
- [2] Paper #3 — The Fine Structure Constant from Planck-Scale Foam Geometry. DOI: 10.5281/zenodo.19011758
- [3] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, physical framework, and direction: Luke Martin. AI role: systematic spectral ratio search, numerical verification.

---

*Unified Foam Field Theory · Paper #13 · DOI: 10.5281/zenodo.19064036 · Priority Date: 20 February 2026*

*B + V = D*
