# Unified Foam Field Theory (UFFT)

**Author:** Luke Martin — Independent Researcher, Newcastle, New South Wales, Australia
**Contact:** hello@ufft.info · ORCID 0009-0006-3716-5951
**Priority Date:** 20 February 2026
**Current Version:** Framework v9 (canonical document; last revised July 2026)
**Status:** 73 papers published on Zenodo + 1 standalone maths preprint · 3 papers in the upload queue · Not yet peer reviewed · Independent reproduction invited

---

## What This Is

The Unified Foam Field Theory derives the dimensionless constants of the Standard Model, general relativity, and cosmology from the geometry of a single Planck-scale cell — the truncated octahedron (Kelvin cell).

**Axiom Zero: B + V = D** — Bubble + Void = Displacement.

Every event in the universe is a displacement in an infinite pre-existing foam at the Planck scale. From this single axiom and the integer topology of the Kelvin cell, UFFT pre-registers **eleven falsifiable predictions** (the sharpest near-term being δ_PMNS/δ_CKM = 3, testable by DUNE around 2035) and contains **a family of structural identities and sector-specific identifications of varying derivational status**. The framework's postdictions across roughly 60 observables are under ongoing look-elsewhere-corrected joint-χ² audit; per the 19 April 2026 methodological review, the earlier "60+ observables with zero free parameters" framing has been retired as not defensible against a trials-factor audit. The honest summary of the empirical case lives in `verification/peer_review_deliverables/D1_Supplement_Joint_Chi2_Defense.md`.

---

## Core Inputs

All inputs are topological integers of the truncated octahedron:

| Symbol | Value | Meaning |
|--------|-------|---------|
| \|O_h\| | 48 | Order of octahedral symmetry group |
| V | 24 | Vertices |
| E | 36 | Edges |
| F | 14 | Faces (8 hexagonal + 6 square) |
| F_hx | 8 | Hexagonal faces |
| F_sq | 6 | Square faces |
| d | 3 | Spatial dimensions |
| Δ | 17 | Discriminant of master equation |
| C_A | 3 | Colour number (= F_hx/F − 1 in the natural normalisation) |
| r₁ | (9−√17)/2 ≈ 2.438 | Lower T₁u eigenvalue (left-handed fermions) |
| r₂ | (9+√17)/2 ≈ 6.562 | Upper T₁u eigenvalue (right-handed fermions) |

**Master equation:** λ² − 9λ + 16 = 0

---

## Selected Results

| Observable | Formula | Accuracy |
|-----------|---------|----------|
| α⁻¹ (fine structure) | (4π)^{3/2}π[47/48 + 10/(3·48³) + 22/(3·48⁵)] | 0.3σ from Cs 2018 |
| sin²θ_W (EW geometric) | (17 − 3√17)/20 | 0.14% |
| α_s(M_Z) | C_A² − C_A ln(C_A)/(2π) | 0.01σ |
| m_H/M_Z | 18/(9+√17) | 0.14% |
| λ (Cabibbo, NLO) | sin(π/14)(1 + √17/363) | 0.07σ |
| A (Wolfenstein) | (19+√17)/28 | −0.015σ |
| R_b (CKM triangle) | (49 − 9√17)/30 | 0.36σ |
| ρ̄ | R_b cos(δ_CKM) | −0.002σ |
| δ_PMNS/δ_CKM | = 3 exactly (colour factor C_A) | Novel — testable by DUNE ~2035 |
| m₁ (neutrino) | = 0 exact theorem | Exact |
| m₃ (neutrino) | m_e exp(−(11+13√17)/4) | 0.075% |
| Δm²₃₁/Δm²₂₁ | = 33 (Frobenius = Eisenstein norm) | 0.8σ |
| Bekenstein area quantum k | = C_A = 3 | Exact |
| r_p (proton radius) | 4ℏ/(m_p c) | 0.02% |

---

## Sharpest Falsifiable Prediction

**δ_PMNS / δ_CKM = 3 exactly.**
This follows from the colour factor C_A = 3 alone. It is exact, parameter-free, and testable by the DUNE experiment around 2035. If the ratio is confirmed ≠ 3 at >3σ, the framework is falsified.

Full list of falsifiable predictions in `UFFT_Core_Framework_v9.md`.

---

## Repository Structure

```
UFFT_Core_Framework_v9.md      ← Canonical framework (77 parts, all derivations)
From_Foam_to_Fermions.md       ← Self-contained book (44 chapters, narrative + theorems)
README.md                      ← This file
LICENSE                        ← CC-BY 4.0 (text/figures) · MIT (code)

papers/                        ← Published Zenodo papers
  ├── INDEX.md                 ← Master index of all papers with DOIs
  └── {ZenodoID}_*.md          ← One file per paper (Zenodo ID + short title), DOI in header

verification/                  ← Numerical verification scripts (zero external data)
```

---

## Verification

Every number in this repository can be recomputed from the cell integers alone:

```bash
pip install numpy scipy
python verification/19079730_UFFT_Spectrum_Verification.py
```

Runs in under one minute. No external data imported.

For Fedorov-parallelohedron spectral uniqueness, `verify_spectra_v2.py` ships with the standalone spectral-uniqueness record on Zenodo (DOI 10.5281/zenodo.19625142). It reproduces all five Fedorov-cell face Laplacian spectra and their characterising identities.

---

## Zenodo

73 papers are published with permanent DOIs, plus one standalone mathematics preprint (spectral uniqueness of the truncated octahedron among the Fedorov parallelohedra). Three further papers are queued for upload.

See `papers/INDEX.md` for the full list of published papers with DOIs.

---

## Epistemological Status

The framework uses a four-tier classification for all claims:

- **Tier 1 — Mathematical theorems:** m₁ = 0, Koide identity, normal hierarchy, SUSY exclusion, Higgs = A₂u uniquely, sin²θ_W = (17 − 3√17)/20, three-generation theorem, T² = −4·I on T₁u, Eisenstein-norm identity 33 = S² − C_A·P, R_b = r₁²/(r₁r₂ − 1)
- **Tier 2 — Derived given identifications:** Sector-specific identifications of varying derivational status across roughly 60 observables; joint statistical significance under look-elsewhere correction is documented in `verification/peer_review_deliverables/D1_Supplement_Joint_Chi2_Defense.md` (two-ledger method)
- **Tier 3 — >1.5σ tension:** η̄ lever-arm residual (phase sensitivity, not an R_b tension)
- **Tier 4 — Suggestive/speculative:** Visible spectrum mapping, infinite-nesting cosmology

Full status table in `UFFT_Core_Framework_v9.md`.

---

## AI Disclosure

Developed in collaboration with Claude (Anthropic). All theoretical ideas, physical intuitions, and framework direction: Luke Martin. AI role: numerical computation, derivation verification, formula search, operator construction, document composition.

---

## License

All text and figures in this repository are released under the Creative Commons Attribution 4.0 International License (CC-BY 4.0). All code is released under the MIT License. Attribute as:

> Martin, L. (2026). *Unified Foam Field Theory*. Zenodo / GitHub. https://github.com/ufft-info/UFFT

---

*Priority Date: 20 February 2026 · Framework v9 · July 2026*

**B + V = D**
