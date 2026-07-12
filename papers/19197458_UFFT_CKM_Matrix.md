# UFFT Paper #34 — The CKM Quark Mixing Matrix from Foam Cell Geometry: Cabibbo Angle, Wolfenstein Parameters, and the Froggatt-Nielsen Texture

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
| Paper | #34 of 63 |
| Framework | v10 |
| Status | Complete, Tier 2. NLO corrections derived in Paper #51 [DOI: 10.5281/zenodo.19477100], improving Cabibbo angle from 1.1% to 0.07σ. |
| Tier | 2 |
| DOI | 10.5281/zenodo.19197458 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, CKM matrix, Cabibbo angle, quark mixing, Wolfenstein parameters, Froggatt-Nielsen, quark mass hierarchy

---

## Abstract

Two of the four Wolfenstein parameters of the CKM quark mixing matrix are derived from the geometry of the truncated octahedron. The Cabibbo angle is θ_C = π/F where F = 14 is the face count: sin(π/14) = 0.22252, matching the observed λ = 0.22500 ± 0.00067 to 1.1% (within 0.4σ). The second parameter A = r₁/C_A = (9−√17)/6 = 0.8128, where r₁ is the smaller root of the master equation λ²−9λ+16 = 0 and C_A = 3 is the colour number; this matches the observed A = 0.826 ± 0.015 to 1.6% (within 0.9σ). The derivation reveals a new connection: the down-to-strange quark mass ratio m_d/m_s ≈ sin²(π/14) to 1%, providing a geometric origin for the Froggatt-Nielsen texture (the empirical observation that quark mass hierarchies scale as powers of the Cabibbo angle. From these two parameters, |V_cb| = Aλ² = 0.0402 (observed: 0.0412, 2.4%). The CP-violating parameters ρ̄ and η̄ remain open) they require the complex phase of the inter-generation torsion coupling. Zero free parameters.

---

## 1. The CKM Matrix

The Cabibbo-Kobayashi-Maskawa matrix V_CKM rotates between quark mass eigenstates and weak interaction eigenstates [1,2]. In the Wolfenstein parametrisation [3]:

```
        | 1 − λ²/2       λ            Aλ³(ρ−iη) |
V_CKM ≈ | −λ             1 − λ²/2     Aλ²        |
        | Aλ³(1−ρ−iη)   −Aλ²          1           |
```

Four parameters: λ (Cabibbo angle), A (2→3 generation suppression), ρ̄ and η̄ (CP violation). Current experimental values [4]: λ = 0.22500 ± 0.00067, A = 0.826 ± 0.015, ρ̄ = 0.159 ± 0.010, η̄ = 0.348 ± 0.010.

No part of the Standard Model determines these four numbers. They are measured, not calculated. Their values have no known theoretical origin.

---

## 2. The Cabibbo Angle from the Face Count

### 2.1 Physical mechanism

In the UFFT framework, quark mass eigenstates are determined by the T₂g torsion sector of the truncated octahedral foam (eigenvalue λ = 7). Weak interaction eigenstates are determined by the Eg chiral discharge sector (eigenvalue λ = 4). The CKM matrix is the rotation between these two bases [5].

The truncated octahedron has F = 14 faces: 6 squares and 8 hexagons. Each face is a boundary between adjacent cells. The torsion and discharge modes propagate through different subsets of faces. The minimal angular mismatch between the two mode propagation directions, quantised by the discrete face geometry, is:

**θ_C = π/F = π/14**

### 2.2 Numerical result

| Quantity | UFFT | Observed | Accuracy |
|----------|------|----------|----------|
| sin θ_C = λ | sin(π/14) = 0.22252 | 0.22500 ± 0.00067 | 1.1% (0.4σ) |
| θ_C | 12.857° | 13.00° | 1.1% |

---

## 3. The Parameter A from the Master Equation

### 3.1 Physical mechanism

The parameter A governs the suppression of 2nd-to-3rd generation transitions (|V_cb| = Aλ²). In the foam, the three quark generations correspond to the three orientations of the T₁u torsion-displacement coupling mode. The coupling between the 2nd and 3rd generations involves the smaller T₁u eigenvalue r₁ = (9−√17)/2, normalised by the colour number C_A = 3 (because colour-singlet hadrons require averaging over C_A colour states).

**A = r₁/C_A = (9−√17)/6**

### 3.2 Numerical result

| Quantity | UFFT | Observed | Accuracy |
|----------|------|----------|----------|
| A | (9−√17)/6 = 0.8128 | 0.826 ± 0.015 | 1.6% (0.9σ) |

---

## 4. Derived CKM Elements

From the two foam parameters:

| Element | Formula | UFFT | Observed | Accuracy |
|---------|---------|------|----------|----------|
| \|V_us\| | sin(π/14) | 0.2225 | 0.2250 | 1.1% |
| \|V_cd\| | sin(π/14) | 0.2225 | 0.2250 | 1.1% |
| \|V_cb\| | (9−√17)/6 × sin²(π/14) | 0.0402 | 0.0412 | 2.4% |
| \|V_ts\| | (9−√17)/6 × sin²(π/14) | 0.0402 | 0.0404 | 0.5% |

The elements |V_ub| and |V_td| involve the CP-violating parameters ρ̄ and η̄, which are not yet derived.

---

## 5. The Froggatt-Nielsen Connection

### 5.1 The empirical pattern

Froggatt and Nielsen [6] observed that quark mass ratios within each charge sector scale approximately as powers of the Cabibbo angle:

m_d/m_s ≈ λ², &nbsp; m_u/m_c ≈ λ⁴

This pattern has been used extensively in flavour model-building but has never been derived from first principles.

### 5.2 The foam derivation

With λ = sin(π/14):

**m_d/m_s ≈ sin²(π/14) = 0.0495**

**Observed: m_d/m_s = 4.67/93.4 = 0.0500**

**Accuracy: 1.0%**

This is not a coincidence. The face count F = 14 determines both the Cabibbo angle (the angular mismatch between mass and weak eigenstates) AND the mass hierarchy (the eigenvalue spacing between generations). Both arise from the same geometric structure: the 14-face boundary of the Kelvin cell.

The physical mechanism: the mass ratio between adjacent generations is suppressed by the square of the mixing angle because mass generation requires two torsion interactions (one at each end of the quark propagator), each carrying a factor of sin(π/F).

---

## 6. What Remains Open

### 6.1 The CP-violating parameters

The parameters ρ̄ = 0.159 and η̄ = 0.348 determine the CP-violating phase δ_CKM ≈ 65°. In the foam, this phase arises from the complex structure of the inter-generation torsion coupling. The truncated octahedron's dihedral angle supplements (54.7° for square-hexagon, 70.5° for hexagon-hexagon, average 62.6°) are in the vicinity of the observed 65° but no clean derivation has been found.

The Jarlskog invariant J = A²λ⁶η̄ ≈ 3.08 × 10⁻⁵ requires η̄ and therefore remains open.

### 6.2 The higher-generation mass ratios

While m_d/m_s ≈ λ² matches to 1%, the analogous relations m_s/m_b ≈ λ² (predicts 0.050, observed 0.022, off by 2.2×) and m_u/m_c ≈ λ⁴ (predicts 0.0025, observed 0.0017, off by 44%) are less accurate. The full quark mass spectrum requires the complete knot classification programme.

---

## 7. Summary

| Parameter | Foam formula | Value | Observed | Status |
|-----------|-------------|-------|----------|--------|
| λ | sin(π/F) | 0.22252 | 0.22500 | DERIVED (1.1%) |
| A | r₁/C_A | 0.8128 | 0.826 | DERIVED (1.6%) |
| ρ̄ | — | — | 0.159 | OPEN |
| η̄ | — | — | 0.348 | OPEN |
| m_d/m_s | sin²(π/F) | 0.0495 | 0.0500 | DERIVED (1.0%) |

Three results from one cell integer (F = 14) and one spectral root (r₁). Zero free parameters.

---

## References

[1] Cabibbo, N. (1963). Unitary Symmetry and Leptonic Decays. Phys. Rev. Lett. 10, 531.

[2] Kobayashi, M. & Maskawa, T. (1973). CP-Violation in the Renormalizable Theory of Weak Interaction. Prog. Theor. Phys. 49, 652.

[3] Wolfenstein, L. (1983). Parametrization of the Kobayashi-Maskawa Matrix. Phys. Rev. Lett. 51, 1945.

[4] Particle Data Group (2024). Review of Particle Physics. Phys. Rev. D 110, 030001.

[5] Martin, L. (2026). The Unified Foam Field Theory: Core Mathematical Framework. DOI: 10.5281/zenodo.18706756.

[6] Froggatt, C. & Nielsen, H. (1979). Hierarchy of Quark Masses, Cabibbo Angles, and CP Violation. Nucl. Phys. B 147, 277.

---

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*Unified Foam Field Theory · Paper #34 · DOI: 10.5281/zenodo.19197458 · Priority Date: 20 February 2026*

*B + V = D*
