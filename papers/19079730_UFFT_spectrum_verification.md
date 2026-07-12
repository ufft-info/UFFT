# UFFT Paper #20 — Spectral Verification: Face Adjacency Laplacian of the Truncated Octahedron

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
| Paper | #20 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | Tier 1 (supplementary/verification) |
| DOI | 10.5281/zenodo.19079730 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, spectrum verification, √17 discriminant, neutrino mixing, Higgs mass

---

## What This Is

This package independently verifies a new result in discrete mathematics that underlies the Unified Foam Field Theory (UFFT) framework:

> The face adjacency Laplacian of the truncated octahedron has eigenvalue spectrum:
> **Spec(L) = {0¹, ((9−√17)/2)³, 4², ((9+√17)/2)³, 7⁴, 9¹}**
>
> Characteristic polynomial: **p(λ) = λ(λ²−9λ+16)³(λ−4)²(λ−7)⁴(λ−9)**

The irrational eigenvalues arise from the discriminant 81−64=**17** of the quadratic factor. This result does not appear in prior published graph theory or spectral geometry literature.

---

## Why It Matters

Every UFFT physical prediction depending on √17 rests on this spectrum:

| Prediction | Formula |
|-----------|---------|
| Solar neutrino mixing | tan²θ₁₂ = √17/9 (0.49σ agreement) |
| Higgs/Z mass ratio | m_H/M_Z = 18/(9+√17) (0.97σ agreement) |
| PMNS reactor angle | sin(θ₁₃) = √17/27 (2.5% agreement) |
| Master equation | λ²−9λ+16=0 (all spectral predictions) |

---

## Files

| File | Description |
|------|-------------|
| `UFFT_Spectrum_Verification.ipynb` | Jupyter notebook — step-by-step with narrative |
| `UFFT_Spectrum_Verification.py` | Standalone Python script — same verification |
| `README_spectrum_verification.md` | This file |

---

## Running the Verification

**Option 1, Jupyter notebook:**
```
jupyter notebook UFFT_Spectrum_Verification.ipynb
```
Run all cells. Each step is documented with explanation.

**Option 2, Python script:**
```
python UFFT_Spectrum_Verification.py
```
Runs in < 30 seconds and prints full results to stdout.

---

## Requirements

```
numpy    (any recent version)
sympy    (any recent version)
```

Both are standard scientific Python packages. No other dependencies.

```bash
pip install numpy sympy
```

---

## Verification Result

```
Numerical (numpy.linalg.eigvalsh):
  Max deviation from claimed values: 4.44e-15  ✓  EXACT (machine precision)

Symbolic (sympy.Matrix.charpoly):
  p(λ) = lambda*(lambda-9)*(lambda-7)**4*(lambda-4)**2*(lambda**2-9*lambda+16)**3
  Polynomial identity check: True  ✓  EXACT

Symbolic eigenvalues:
  λ = 0                  (multiplicity 1)
  λ = 9/2 - sqrt(17)/2   (multiplicity 3)
  λ = 4                  (multiplicity 2)
  λ = sqrt(17)/2 + 9/2   (multiplicity 3)
  λ = 7                  (multiplicity 4)
  λ = 9                  (multiplicity 1)
```

---

## How It Works

1. **Construct the truncated octahedron** from vertex coordinates: all permutations of (0, ±1, ±2). This gives 24 vertices with edge length √2. No free parameters.

2. **Identify 14 faces**: 6 square faces (perpendicular to coordinate axes) + 8 hexagonal faces (perpendicular to body diagonals). Each identified purely from the vertex coordinates.

3. **Build the 14×14 face adjacency matrix A**: two faces are adjacent if they share exactly 2 vertices connected by an edge.

4. **Compute L = D − A** where D is the diagonal degree matrix (squares have degree 4, hexagons have degree 6).

5. **Find eigenvalues** numerically (numpy) and symbolically (sympy). Both confirm the claimed spectrum exactly.

---

## Citation

If you use this verification, please cite the underlying paper:

> Martin, L. (2026). *The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph*. Zenodo. DOI: 10.5281/zenodo.19011758

---

*Developed in collaboration with Claude (Anthropic). Ideas, framework, direction: Luke Martin. AI role: code implementation, notebook structure.*

---

---

---

## References

### UFFT Papers
- [1] Paper #3 — The Fine Structure Constant from Planck-Scale Foam Geometry. DOI: 10.5281/zenodo.19011758
- [2] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [3] Paper #16 — The Master Equation of the Standard Model from Foam Geometry. DOI: 10.5281/zenodo.19064359

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*Unified Foam Field Theory · Paper #20 · DOI: 10.5281/zenodo.19079730 · Priority Date: 20 February 2026*

*B + V = D*
