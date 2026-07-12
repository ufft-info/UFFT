# UFFT Paper #36 — CP-Violating Phases of the CKM and PMNS Matrices from the T₁u Eigenvalue Ratio: The Complete Mixing Sector from Foam Cell Geometry

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | March 2026 |
| Series | Unified Foam Field Theory |
| Paper | #36 of 63 |
| Framework | v10 |
| Status | Complete, Tier 2. Contains the sharpest near-term prediction: δ_PMNS/δ_CKM = C_A = 3 exactly, testable by DUNE ~2035. |
| Tier | 2 |
| DOI | 10.5281/zenodo.19198775 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, CP violation, CKM matrix, PMNS matrix, Dirac phase, unitarity triangle, Jarlskog invariant, T₁u eigenvalue ratio, foam field theory

---

## Abstract

The CP-violating phases of both the CKM and PMNS mixing matrices are derived from a single algebraic quantity: the eigenvalue ratio R = r₁/r₂ = (9−√17)/(9+√17) of the T₁u sector of the truncated octahedron face Laplacian.

The CKM phase is δ_CKM = πR = 66.89°, matching the observed 65.5° ± 3.4° (0.4σ). Setting the unitarity triangle modulus R_b = R gives ρ̄ = R cos(πR) = 0.146 (1.3σ) and η̄ = R sin(πR) = 0.342 (0.6σ), closing the CKM matrix to 4/4 Wolfenstein parameters. The derived sin(2β) = 0.690 matches the B-factory measurement 0.699 ± 0.017 (0.5σ).

The PMNS phase is δ_PMNS = C_A × πR = 3πR = 200.7°, matching the observed 197° ± 25° (0.15σ), where C_A = 3 is the colour number. The factor of C_A arises because leptons couple to all three torsion axes simultaneously, while quarks (confined to colour singlets) couple through a single colour channel.

This gives a sharp prediction: δ_PMNS/δ_CKM = C_A = 3 exactly, testable by DUNE and Hyper-Kamiokande within the decade.

Combined with previous results, the complete quark and lepton mixing sector (9 parameters total (4 CKM + 4 PMNS angles + 1 mass-squared ratio)) is determined by three cell integers: F = 14, C_A = 3, Δ = 17. Zero free parameters.

---

## 1. The Eigenvalue Ratio

The face Laplacian of the truncated octahedron has two T₁u eigenvalues, each with multiplicity 3 [3]:

```
r₁ = (9 − √17)/2 ≈ 2.4384
r₂ = (9 + √17)/2 ≈ 6.5616
```

These are the roots of the master equation λ² − 9λ + 16 = 0, with discriminant Δ = 17 (prime). Their ratio defines the T₁u asymmetry parameter:

**R ≡ r₁/r₂ = (9−√17)/(9+√17)**

Numerically: R = 0.37163. Algebraically: R = (98−18√17)/64. The quantity R measures how much the foam's symmetry breaking (from the void lattice (integer spectrum) to the bubble lattice (irrational spectrum)) splits the T₁u sector. It has already appeared in the framework as the Higgs-to-Z mass ratio m_H/M_Z = 2/(1+R) [4] and the CKM parameter A = r₁/C_A [1].

---

## 2. The CKM CP Phase

### 2.1 Derivation

The CKM matrix rotates between quark mass eigenstates (T₂g torsion sector, eigenvalue λ = 7) and weak interaction eigenstates (Eg chiral discharge sector, eigenvalue λ = 4). The inter-generation torsion coupling is a complex quantity whose phase is set by the T₁u eigenvalue ratio propagating between the two bases.

The physical mechanism: a quark undergoing a generation-changing weak transition must traverse the T₁u sector, which carries the generation quantum number. The complex amplitude for this traversal has modulus and phase both determined by R. The modulus sets the unitarity triangle size; the phase sets the CP-violating angle:

**δ_CKM = πR = π(9−√17)/(9+√17)**

### 2.2 Numerical result

| Quantity | UFFT | Observed | Accuracy |
|----------|------|----------|----------|
| δ_CKM | πR = 66.89° | 65.5° ± 3.4° | 0.4σ |

---

## 3. The Unitarity Triangle from R

### 3.1 The apex

The unitarity triangle apex (ρ̄, η̄) in the Wolfenstein parametrisation satisfies:

```
ρ̄ + iη̄ = R_b × e^{iγ}
```

where γ = δ_CKM and R_b = |ρ̄ + iη̄| is the modulus. In the foam, the same T₁u eigenvalue ratio that determines the phase also determines the modulus:

**R_b = R = r₁/r₂**

The physical argument: the inter-generation torsion coupling propagator has the form R × e^{iπR}, where R enters both as the amplitude suppression (the lighter T₁u mode coupling to the heavier) and as the phase (the asymmetry between forward and backward propagation through the T₁u gap). Both effects originate from the same eigenvalue splitting.

Therefore:

**ρ̄ = R cos(πR) = 0.1458**

**η̄ = R sin(πR) = 0.3418**

### 3.2 Complete unitarity triangle

From (ρ̄, η̄), the three angles of the unitarity triangle follow:

| Angle | UFFT formula | UFFT | Observed | σ |
|-------|-------------|------|----------|---|
| γ (= δ) | πR | 66.89° | 65.5° ± 3.4° | 0.4 |
| β | arctan(η̄/(1−ρ̄)) | 21.81° | 22.2° ± 0.7° | 0.6 |
| α | π − γ − β | 91.30° | 84.5° ± 5.1° | 1.3 |

The B-factory golden measurement:

**sin(2β) = 0.690** (observed: 0.699 ± 0.017, 0.5σ)

### 3.3 Derived CKM elements

Using all four Wolfenstein parameters (λ = sin(π/14), A = r₁/C_A, ρ̄ = R cos(πR), η̄ = R sin(πR)):

| Element | UFFT | Observed | Accuracy |
|---------|------|----------|----------|
| \|V_us\| = λ | 0.2225 | 0.2250 | 1.1% |
| \|V_cb\| = Aλ² | 0.0402 | 0.0406 | 0.8% |
| \|V_ub\| | 0.00333 | 0.00382 | 13% |
| \|V_td\| | 0.00824 | 0.00854 | 3.5% |

The Jarlskog invariant:

**J_CKM = A²λ⁶η̄(1−λ²/2)² = 2.61 × 10⁻⁵** (observed: 3.08 × 10⁻⁵, 15%)

The 15% Jarlskog discrepancy propagates from the 13% |V_ub| discrepancy, which in turn comes from R_b being 4% below the measured value. This is the weakest point of the derivation. R_b = R is classified SUGGESTIVE; the phase δ = πR is classified DERIVED.

---

## 4. The PMNS CP Phase

### 4.1 Derivation

The PMNS matrix rotates between neutrino mass eigenstates and flavour eigenstates, both within the T₁u sector [2]. The CP-violating phase arises from the same inter-generation torsion coupling as the CKM phase, but with a critical difference: leptons are colour-neutral.

In the quark sector, colour confinement projects the torsion coupling onto a single colour channel. The CP phase from one colour axis is πR, and this is the full CKM phase because hadrons are colour singlets.

In the lepton sector, there is no colour confinement. The T₁u displacement modes couple through all C_A = 3 torsion axes simultaneously. Each axis contributes a phase πR. The total lepton CP phase is:

**δ_PMNS = C_A × πR = 3πR = 3π(9−√17)/(9+√17)**

### 4.2 Numerical result

| Quantity | UFFT | Observed | Accuracy |
|----------|------|----------|----------|
| δ_PMNS | 3πR = 200.68° | 197° ± 25° | 0.15σ |

### 4.3 The colour factor prediction

The ratio of the two CP phases is:

**δ_PMNS / δ_CKM = C_A = 3 (exactly)**

This is a sharp, falsifiable prediction. It does not depend on R, on the master equation, or on any numerical value, it depends only on the colour number C_A = dim(T₂g) = 3. If both phases are measured to sufficient precision, their ratio must be exactly 3.

Current data: δ_PMNS/δ_CKM = 197°/65.5° = 3.01 ± 0.78. Consistent with 3, but the PMNS uncertainty dominates. DUNE (expected ±5° on δ_PMNS by ~2035) will test this to ~8% precision.

---

## 5. Algebraic Structure

The entire quark and lepton mixing sector is determined by one complex number and two real parameters:

**The inter-generation torsion coupling: R × e^{iπR}**

where R = r₁/r₂ = (9−√17)/(9+√17) is the T₁u eigenvalue ratio. From this:

CKM sector (quarks, one colour channel):
- δ_CKM = arg(R × e^{iπR}) = πR
- R_b = |R × e^{iπR}| = R
- ρ̄ = Re(R × e^{iπR}) = R cos(πR)
- η̄ = Im(R × e^{iπR}) = R sin(πR)

PMNS sector (leptons, C_A colour channels):
- δ_PMNS = C_A × πR

Combined with the previously derived parameters:
- λ = sin(π/F) from the face count F = 14 [1]
- A = r₁/C_A from the spectral root and colour number [1]
- Three PMNS angles from Δ = 17 and C_A = 3 [2]

Total: **9 mixing parameters from 3 integers (F = 14, C_A = 3, Δ = 17)**.

---

## 6. Status Assessment

| Parameter | Formula | UFFT | Observed | σ | Status |
|-----------|---------|------|----------|---|--------|
| δ_CKM | πR | 66.89° | 65.5° ± 3.4° | 0.4 | DERIVED |
| η̄ | R sin(πR) | 0.342 | 0.348 ± 0.010 | 0.6 | DERIVED |
| β | arctan(η̄/(1−ρ̄)) | 21.81° | 22.2° ± 0.7° | 0.6 | DERIVED |
| sin(2β) | from triangle | 0.690 | 0.699 ± 0.017 | 0.5 | DERIVED |
| ρ̄ | R cos(πR) | 0.146 | 0.159 ± 0.010 | 1.3 | SUGGESTIVE |
| α | π−γ−β | 91.3° | 84.5° ± 5.1° | 1.3 | SUGGESTIVE |
| R_b | R = r₁/r₂ | 0.372 | 0.387 ± 0.012 | 1.3 | SUGGESTIVE |
| δ_PMNS | C_A × πR | 200.7° | 197° ± 25° | 0.15 | CONSISTENT |
| δ_PMNS/δ_CKM | C_A | 3 | 3.01 ± 0.78 | — | PREDICTION |

Four results below 1σ. Three at 1.3σ. One consistent with wide uncertainty. One testable prediction.

---

## 7. What Remains Open

The |V_ub| element (13% discrepancy) and the Jarlskog invariant (15%) are the weakest predictions. Both trace to R_b = R being 4% below the measured value. Three possibilities:

(a) R_b = R is exact and the current |V_ub| measurement is slightly high, it is one of the least precisely known CKM elements and has historically fluctuated.

(b) R_b receives a small correction from higher-order terms in the face Laplacian, analogous to the NLO corrections that affect the kaon mass in the hadron sector.

(c) R_b = R is wrong and a different combination of cell integers gives R_b. No clean alternative has been found.

The PMNS phase δ_PMNS = 3πR = 200.7° is consistent with data but cannot be classified DERIVED until the experimental uncertainty narrows from ±25° to ±5°. This is expected from DUNE by ~2035.

---

## 8. Summary

The CP-violating phases of the Standard Model arise from the T₁u eigenvalue asymmetry of the truncated octahedron:

**δ_CKM = πR** (quarks: one colour channel)

**δ_PMNS = 3πR** (leptons: three colour channels)

where **R = (9−√17)/(9+√17)** is the ratio of the two T₁u eigenvalues of the master equation λ²−9λ+16 = 0. The colour factor C_A = 3 connecting the two phases is the dimension of the T₂g torsion sector, the same integer that gives the number of colours, the number of generations, and the number of spatial dimensions.

With these results, the complete CKM matrix (4/4 Wolfenstein parameters) and the complete PMNS matrix (3 angles + phase) are determined by the geometry of a single 14-faced polyhedron. Nine mixing parameters from three integers. Zero free parameters.

---

## References

[1] Martin, L. (2026). The CKM Quark Mixing Matrix from Foam Cell Geometry. Zenodo. DOI: 10.5281/zenodo.19198360.

[2] Martin, L. (2026). The PMNS Neutrino Mixing Matrix from Foam Cell Geometry. Zenodo. DOI: 10.5281/zenodo.19198422.

[3] Martin, L. (2026). The Face Laplacian Spectrum of the Kelvin Cell. Zenodo. DOI: 10.5281/zenodo.19030062.

[4] Martin, L. (2026). The Higgs-to-Z Mass Ratio from the Face Laplacian Spectrum. Zenodo. DOI: 10.5281/zenodo.19064036.

[5] Martin, L. (2026). The Master Equation of the Standard Model from Foam Geometry. Zenodo. DOI: 10.5281/zenodo.19064359.

[6] Particle Data Group (2024). Review of Particle Physics. Phys. Rev. D 110, 030001.

[7] Esteban, I. et al. (2020). The fate of hints: updated global analysis of three-flavour neutrino oscillations. JHEP 09, 178. NuFIT 5.2 (2022).

---

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*Unified Foam Field Theory · Paper #36 · DOI: 10.5281/zenodo.19198775 · Priority Date: 20 February 2026*

*B + V = D*
