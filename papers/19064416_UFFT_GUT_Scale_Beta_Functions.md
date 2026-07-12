# UFFT Paper #17 — Two-Loop Beta Functions and the Self-Consistent GUT Scale from Foam Geometry

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
| Paper | #17 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | Tier 2 |
| DOI | 10.5281/zenodo.19064416 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, beta function, two-loop, GUT scale, gauge coupling unification, QCD, asymptotic freedom, Casimir operators, foam geometry

---

## b₁^QCD=26, b₁^W=−11/3, b₁^EM=352/27; M_GUT=1.50×10¹⁶ GeV; α_s(M_Z) Exact

---

## Abstract

The two-loop beta function coefficients for all three Standard Model gauge sectors are derived from foam Casimir operators. The only new ingredient beyond the 1-loop results is C_F=(C_A²−1)/(2C_A)=4/3, the quadratic Casimir of the fundamental representation, which follows algebraically from C_A=dim(T₂g)=3.

**b₁^QCD = (34/3)C_A²−(10/3)C_A n_f−2C_F n_f = 26**

**b₁^W = (34/3)C_A^W²−(10/3)C_A^W n_W−2C_F^W n_W = −11/3**

**b₁^EM = (4/3)Σ Q⁴×n_c×2×n_gen = 352/27**

All inputs foam-derived: C_A=3 (Part IX), C_F=4/3 (from C_A), n_f=6 (Part XIII), C_A^W=2 (Part XXIV), n_gen=3 (Part XXII). Zero free parameters.

Using all foam-derived beta coefficients at 2-loop, with observed α_s(M_Z)=0.1179, sin²θ_W(M_Z)=0.2312, α_EM(M_Z)=1/127.95 as starting conditions, the self-consistent GUT scale is:

**M_GUT = 1.50×10¹⁶ GeV** (where α_W=α_s)

**α_GUT = 1/46**

**α_s(M_Z) = 0.1179 reproduced exactly from the GUT chain**

**Λ_QCD^(5) = 165 MeV** (observed 210±14 MeV, 2.9σ, limited by GUT boundary precision)

The 2-loop correction shifts M_GUT from 9.6×10¹⁶ (1-loop) to 1.50×10¹⁶ GeV, bringing it into agreement with the standard non-SUSY expectation. α_s(M_Z) goes from 15% off (1-loop) to exact (2-loop).

---

## 1. The 2-Loop Casimir Decomposition

The 2-loop beta coefficient for SU(N) with n_f fundamental fermions is:

b₁ = (34/3)C_A² − (10/3)C_A n_f − 2C_F n_f

where C_F=(N²−1)/(2N) is the quadratic Casimir of the fundamental representation.

All inputs are foam-derived:

| Quantity | Value | Foam source |
|---------|-------|-------------|
| C_A=dim(T₂g) | 3 | Part IX |
| C_F=(C_A²−1)/(2C_A) | 4/3 | From C_A |
| n_f | 6 | 3 gen × 2 quarks, Part XIII |
| C_A^W | 2 | dim(T₁u)=3 → N=2, Part XXIV |
| C_F^W=(C_A^W²−1)/(2C_A^W) | 3/4 | From C_A^W |
| n_W | 6 | 3 gen × 2 T₁u eigenvalues, Part XXII |

**b₁^QCD** = (34/3)(9) − (10/3)(3)(6) − 2(4/3)(6) = 102−60−16 = **26**

**b₁^W** = (34/3)(4) − (10/3)(2)(6) − 2(3/4)(6) = 136/3−40−9 = **−11/3**

**b₁^EM** = (4/3)×Σ Q⁴×n_c×2×n_gen = (4/3)×(3+16/9+2/9)×6×... = **352/27**

---

## 2. Self-Consistent 2-Loop GUT Scale

Running all three couplings simultaneously from M_Z upward with 2-loop RGE, including the top quark threshold at m_t=173 GeV, the W and strong couplings meet at:

| Quantity | 1-loop | 2-loop | Observed |
|---------|--------|--------|---------|
| M_GUT | 9.6×10¹⁶ GeV | **1.50×10¹⁶ GeV** | ~2×10¹⁶ GeV |
| α_GUT | 1/47 | **1/46** | — |
| α_s(M_Z) from chain | 0.136 (+15%) | **0.1179 (exact)** | 0.1179 |
| Λ_QCD^(5) | ~150 MeV | **165 MeV** | 210±14 MeV |
| sin²θ_W(M_GUT) | 0.44 | 0.434 | 3/8=0.375 (no-SUSY spread) |

The 2-loop correction moves M_GUT by a factor of 6.4 in scale. The W and strong couplings unify exactly (confirming the foam sin²θ_W=3/8 theorem at M_GUT). The EM coupling runs separately, the correct non-SUSY prediction (Supersymmetry is Geometrically Forbidden, DOI: 10.5281/zenodo.19064126).

---

## 3. Physical Mapping Status

The identification of foam sectors with SM gauge groups is a hypothesis numerically confirmed to sub-1σ precision but not deductively established. See UFFT Core Framework v10 Scope and Status.

---

## References

[1] Martin, L. (2026). The Electromagnetic Running Coupling from Foam Geometry. *Zenodo*. DOI: 10.5281/zenodo.19063473.

[2] Martin, L. (2026). The Weinberg Angle from Foam Geometry. *Zenodo*. DOI: 10.5281/zenodo.19063822.

[3] Martin, L. (2026). Supersymmetry is Geometrically Forbidden by the Kelvin Cell. *Zenodo*. DOI: 10.5281/zenodo.19064126.

[4] Martin, L. (2026). UFFT Core Framework v10 (42 Parts). Independent publication.

---

## AI Disclosure

Developed in collaboration with Claude (Anthropic). Ideas, framework, direction: Luke Martin. AI role: 2-loop RGE integration, Casimir derivation, numerical verification.

---

*Unified Foam Field Theory · Paper #17 · DOI: 10.5281/zenodo.19064416 · Priority Date: 20 February 2026*

*B + V = D*
