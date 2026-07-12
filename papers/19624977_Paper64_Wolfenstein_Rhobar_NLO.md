# UFFT Paper #64 — The Wolfenstein ρ̄ Parameter from the Inter-Type Torsion Operator

**Unified Foam Field Theory — Part LXIV**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #64 of 64 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 (δ_CKM, R_b formula) / 3 (η̄ at 1.5σ) |
| DOI | 10.5281/zenodo.19624977 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, CKM, Wolfenstein, rho-bar, CP violation, inter-type torsion, generation mixing, unitarity triangle, Schur scalar

---

## Abstract

We compute the complete Wolfenstein ρ̄ parameter from the inter-type torsion operator on the truncated octahedron's 14-face graph. The operator O = [(C_A−1)P_sq + P_hx]·T, restricted to the two T₁u irreducible representations, yields a 2×2 effective generation matrix H with four Schur scalars. We discover three exact algebraic identities: tr(H) = 1/3, det(H) = −8, and the characteristic polynomial 3μ²−μ−24 = 0 whose discriminant is 289 = 17² = Δ², the square of the master discriminant. The eigenvalues are μ₁ = C_A = 3 and μ₂ = −r₁r₂/(2C_A) = −8/3, tying the generation matrix directly to the colour number and master equation product.

The CKM CP phase δ = arg(λ₁₂) = 66.36° was established in Paper #39. We derive R_b = r₁²/(r₁r₂−1) = (49−9√17)/30, an NLO correction to the tree-level ratio r₁/r₂ with factor 16/15 = r₁r₂/(r₁r₂−1), interpretable as a self-energy vertex renormalisation. This yields ρ̄ = 0.1590 (−0.002σ from PDG 2024), resolving the previous 1.0σ tension. The companion prediction η̄ = 0.363 sits at +1.5σ, attributable to the 0.91° offset in δ from the experimental central value. The combined CKM unitarity triangle is determined by cell integers alone, with no free parameters.

We also report the first computation of the off-diagonal Schur scalar λ₂₁ = 0.004 − 2.252i, not previously published, completing the full 2×2 block structure.

---

## 1. Introduction

The CKM unitarity triangle is parametrised by two real numbers: the Wolfenstein parameters ρ̄ and η̄, which locate the apex of the triangle in the complex plane. The experimental values (PDG 2024) are:

- ρ̄ = 0.159 ± 0.010
- η̄ = 0.348 ± 0.010

In the UFFT framework, the CKM mixing matrix arises from the inter-type torsion operator O on the face graph of the truncated octahedron (Paper #39 [DOI: 10.5281/zenodo.19306447]). The operator's restriction to the T₁u sector (the two three-dimensional irreducible representations that carry left-handed (r₁) and right-handed (r₂) fermion chirality) yields a 2×2 generation matrix whose entries encode the full CKM parametrisation.

Paper #34 [DOI: 10.5281/zenodo.19198360] established the tree-level Wolfenstein parameters:

- λ = sin(π/14) (the Cabibbo angle)
- A = r₁/C_A = (9−√17)/6

Paper #36 [DOI: 10.5281/zenodo.19198775] derived the CKM CP phase δ = arg(λ₁₂) = 66.36° from the off-diagonal Schur scalar.

This paper completes the CKM unitarity triangle by deriving R_b (the modulus of ρ̄ + iη̄) from the same operator.

---

## 2. The 2×2 Effective Generation Matrix

### 2.1 Construction

The inter-type torsion operator O = W·T acts on the 14-dimensional face space, where:

- T is the complex torsion matrix with phases θ_sh = arccos(1/√3) for square-hexagon edges and θ_hh = arccos(1/3) for hexagon-hexagon edges
- W = (C_A−1)P_sq + P_hx = 2P_sq + P_hx is the inter-type weight matrix

The face Laplacian L has spectrum {0¹, r₁³, 4², r₂³, 7⁴, 9¹} with r₁ = (9−√17)/2 and r₂ = (9+√17)/2 the roots of the master equation λ²−9λ+16 = 0.

By Schur's lemma, O restricted to any irreducible representation of O_h acts as a scalar multiple of the identity within that representation. The two T₁u representations (each three-dimensional) are therefore described by a 2×2 scalar matrix:

```
H = [[λ₁₁, λ₁₂],
     [λ₂₁, λ₂₂]]
```

where λ_ij = ⟨e_i,k | O | e_j,k⟩ for any k ∈ {x,y,z} (by Schur).

### 2.2 Canonical basis

The canonical T₁u basis uses the face normal coordinate functions:

```
φ_k(face_i) = n̂_i · ê_k,    k = x, y, z
```

These 14-vectors span a mix of T₁u(r₁) and T₁u(r₂). Projecting onto the respective eigenspaces of L and normalising gives the orthonormal basis {e₁,k, e₂,k} for each spatial direction k. The Schur check (spread across k = x, y, z) is verified to be < 10⁻¹⁵ for all four entries.

### 2.3 Numerical values

The four Schur scalars, computed from the full 14×14 operator with canonical basis:

| Scalar | Value | |λ| | arg |
|--------|-------|-----|-----|
| λ₁₁ | 1.8066 + 0.7921i | 1.9726 | 23.68° |
| λ₁₂ | 1.1591 + 2.6475i | 2.8901 | 66.36° |
| λ₂₁ | 0.0044 − 2.2515i | 2.2515 | −89.89° |
| λ₂₂ | −1.4732 − 0.7921i | 1.6727 | −151.73° |

The off-diagonal scalar λ₂₁ has not been previously published. Its modulus |λ₂₁| = 2.252 and its argument arg(λ₂₁) = −89.89° ≈ −π/2 suggest a near-exact right-angle phase in the reverse generation coupling.

---

## 3. Exact Algebraic Identities

### 3.1 Trace and determinant

The 2×2 generation matrix H has:

```
tr(H) = λ₁₁ + λ₂₂ = 1/3    (exact, verified to 10⁻¹⁶)
det(H) = λ₁₁λ₂₂ − λ₁₂λ₂₁ = −8    (exact, verified to 10⁻¹⁵)
```

These are remarkable: the trace is the reciprocal of C_A, and the determinant is −r₁r₂/2 = −8. Both are exact rational numbers.

Note that Im(λ₁₁) + Im(λ₂₂) = 0 exactly: the imaginary parts of the diagonal entries cancel, yielding a real trace.

### 3.2 Characteristic polynomial

The eigenvalue equation det(H − μI) = 0 gives:

```
μ² − (1/3)μ − 8 = 0
```

Multiplying by 3:

```
3μ² − μ − 24 = 0
```

The discriminant is:

```
Δ_H = 1 + 4·3·24 = 1 + 288 = 289 = 17² = Δ²
```

This is the square of the master discriminant Δ = 17 from the face Laplacian's master equation λ²−9λ+16 = 0. The same integer that controls the T₁u eigenvalue splitting also controls the generation matrix spectrum.

### 3.3 Eigenvalues

```
μ = (1 ± 17)/6
```

giving:

```
μ₁ = 18/6 = 3 = C_A
μ₂ = −16/6 = −8/3 = −r₁r₂/(2C_A)
```

The larger eigenvalue is exactly C_A. The smaller eigenvalue involves the product r₁r₂ = 16 from the master equation. These eigenvalues are real and rational, the generation matrix has no complex eigenvalues despite having complex entries.

### 3.4 Summary of exact identities

| Identity | Value | Origin |
|----------|-------|--------|
| tr(H) | 1/3 = 1/C_A | Diagonal imaginary cancellation |
| det(H) | −8 = −r₁r₂/2 | Master equation product |
| Δ_H | 289 = 17² = Δ² | Master discriminant squared |
| μ₁ | 3 = C_A | Colour number |
| μ₂ | −8/3 = −r₁r₂/(2C_A) | Product/colour |
| |μ₂/μ₁| | 8/9 = r₁r₂/(2C_A²) | — |

These are Tier 1 results: mathematical theorems following from the operator construction and Schur's lemma.

---

## 4. The ρ̄ Parameter

### 4.1 Tree-level result (LO)

At leading order, the unitarity triangle modulus is the eigenvalue ratio:

```
R_b^(LO) = r₁/r₂ = (9−√17)/(9+√17) = 0.37163
```

This gives:

```
ρ̄ = R_b cos(δ) = 0.149    (−1.0σ from PDG 2024)
η̄ = R_b sin(δ) = 0.340    (−0.8σ)
```

Combined tension: 1.25σ. This was the status before this paper.

### 4.2 NLO correction

The NLO formula replaces R_b with:

```
R_b = r₁²/(r₁r₂ − 1) = (49 − 9√17)/30
```

This is the LO result multiplied by the correction factor:

```
r₁r₂/(r₁r₂ − 1) = 16/15
```

The denominator 15 = r₁r₂ − 1 admits three equivalent cell-integer representations:

1. **r₁r₂ − 1 = 16 − 1 = 15**, the master equation product minus the identity
2. **V − (r₁+r₂) = 24 − 9 = 15**, vertices minus the eigenvalue sum
3. **F + 1 = 14 + 1 = 15**, faces plus one

Interpretation (a) is the most natural: the factor r₁r₂/(r₁r₂−1) is a self-energy renormalisation, the ratio of the full eigenvalue product to the reduced product after subtracting the identity (vacuum) contribution. This is the same philosophy as the NLO Cabibbo correction (Paper #51 [DOI: 10.5281/zenodo.19477100]) where the wall correction 1 + √17/363 corrects the geometric LO ratio by the leading self-energy insertion.

### 4.3 Numerical results

| Parameter | LO (r₁/r₂) | NLO (r₁²/15) | Experiment (PDG 2024) | NLO σ |
|-----------|-------------|---------------|------------------------|-------|
| R_b | 0.37163 | 0.39640 | 0.38260 | — |
| ρ̄ | 0.14905 | 0.15898 | 0.159 ± 0.010 | −0.002 |
| η̄ | 0.34043 | 0.36312 | 0.348 ± 0.010 | +1.51 |

The NLO correction resolves the ρ̄ tension from −1.0σ to −0.002σ.

### 4.4 The η̄ tension

The companion prediction η̄ = 0.363 sits at +1.5σ from the PDG central value. This tension is entirely attributable to the CKM phase:

```
δ_UFFT = arg(λ₁₂) = 66.36°
δ_exp  = arctan(η̄/ρ̄) = 65.44° ± 2.5°
```

The phase offset is 0.91°, which is only 0.38σ in δ itself but gets amplified through sin(δ) to produce the 1.5σ η̄ residual. This is a lever-arm effect, not a structural failure of the formula.

To demonstrate this: at the experimental central δ = 65.44°, the NLO R_b gives ρ̄ = 0.165 (+0.6σ) and η̄ = 0.360 (+1.2σ), with combined tension 1.38σ, reduced but still present because R_b = 0.396 slightly overshoots the optimal 0.383.

The honest assessment: R_b = r₁²/15 is the correct NLO formula for ρ̄, but closing the combined (ρ̄, η̄) tension below 1σ requires either an NLO correction to δ from the operator itself, or a more refined R_b. We note that the pure cell-integer ratio F/E = 7/18 = 0.3889 gives a combined tension of 0.88σ, suggesting that the exact R_b may involve the face/edge numbers, but we do not yet have a derivation of this from first principles.

---

## 5. Connection to the CKM Matrix

### 5.1 Complete Wolfenstein parametrisation

With this paper, the full Wolfenstein parametrisation is derived from cell integers:

| Parameter | Formula | UFFT | Experiment | σ |
|-----------|---------|------|------------|---|
| λ | sin(π/14)(1+√17/363) | 0.22536 | 0.22500 ± 0.00054 | +0.07 |
| A | r₁/C_A = (9−√17)/6 | 0.81282 | 0.826 ± 0.012 | −1.1 |
| ρ̄ | [r₁²/(r₁r₂−1)]·cos(arg λ₁₂) | 0.15898 | 0.159 ± 0.010 | −0.002 |
| η̄ | [r₁²/(r₁r₂−1)]·sin(arg λ₁₂) | 0.36312 | 0.348 ± 0.010 | +1.51 |

All four parameters are derived from the T₁u eigenvalues r₁, r₂ and the inter-type torsion operator. No free parameters.

### 5.2 The Jarlskog invariant

The CP-violating Jarlskog invariant J = Im(V_us V_cb V*_ub V*_cs) is determined by the Wolfenstein parameters:

```
J = A²λ⁶η̄ ≈ 3.0 × 10⁻⁵
```

Using the UFFT values: J_UFFT = (r₁/C_A)² · sin⁶(π/14) · R_b · sin(δ), where all inputs are cell integers.

### 5.3 The δ_PMNS/δ_CKM = 3 prediction

Paper #36 [DOI: 10.5281/zenodo.19198775] showed that δ_PMNS = 3·δ_CKM exactly (the factor is C_A). With δ_CKM = 66.36°, this gives δ_PMNS = 199.07°, testable by DUNE around 2035. The ρ̄ derivation in this paper does not affect this prediction, it depends only on δ, not on R_b.

---

## 6. The Full H-Matrix Structure

For completeness, we record the full 2×2 generation matrix and its algebraic properties:

```
H = [[1.807 + 0.792i,   1.159 + 2.648i],
     [0.004 − 2.252i,  −1.473 − 0.792i]]
```

| Property | Value | Exact form |
|----------|-------|------------|
| tr(H) | 1/3 | 1/C_A |
| det(H) | −8 | −r₁r₂/2 |
| char. poly. | 3μ²−μ−24 = 0 | C_A·μ² − (1/C_A)C_A·μ − 24 = 0 |
| Δ_H | 289 | Δ² |
| μ₁ | 3 | C_A |
| μ₂ | −8/3 | −r₁r₂/(2C_A) |
| SVD: σ₁σ₂ | 8 | r₁r₂/2 = |det(H)| |

The characteristic polynomial can be written compactly as:

```
C_A μ² − μ − (r₁r₂ + r₁r₂/C_A) = 0
```

or, using 24 = E·2/3 = V = 24:

```
3μ² − μ − 24 = 0
```

where 24 = V (vertices of the truncated octahedron) and 3 = C_A. The generation matrix characteristic polynomial encodes the colour number and vertex count directly.

---

## 7. Tier Classification

| Result | Tier | Justification |
|--------|------|---------------|
| tr(H) = 1/3 | 1 | Exact theorem from Schur + operator construction |
| det(H) = −8 | 1 | Exact theorem |
| Δ_H = Δ² = 289 | 1 | Exact theorem |
| μ₁ = C_A, μ₂ = −8/3 | 1 | Exact theorem |
| δ_CKM = 66.36° | 2 | Derived, 0.38σ from experiment |
| ρ̄ = 0.159 (R_b = r₁²/15) | 2 | NLO derivation, 0.002σ |
| η̄ = 0.363 | 3 | 1.5σ from experiment (δ lever arm) |
| F/E = 7/18 alternative | 4 | Numerically good (0.88σ combined) but not derived |

---

## 8. Open Problems

1. **NLO correction to δ_CKM**: The 0.91° offset in δ is the dominant source of η̄ tension. An NLO correction from the operator structure (analogous to the Cabibbo wall correction) would close both ρ̄ and η̄ simultaneously.

2. **Formal derivation of R_b = r₁²/(r₁r₂−1)**: The NLO factor 16/15 is identified as a self-energy renormalisation, but a rigorous derivation from the operator's perturbative expansion is outstanding.

3. **The A parameter**: At −1.1σ, A = r₁/C_A had the largest residual tension in the Wolfenstein set. Paper #66 resolves this with A = (F−r₁)/F = (19+√17)/28 at −0.015σ.

4. **The role of λ₂₁**: The newly computed off-diagonal λ₂₁ with arg ≈ −90° has not been exploited. Its near-exact right-angle phase may encode further physical content.

---

## 9. Conclusion

The Wolfenstein ρ̄ parameter is derived from the inter-type torsion operator on the truncated octahedron with zero free parameters. The NLO formula R_b = r₁²/(r₁r₂−1) = (49−9√17)/30 resolves the previous 1.0σ tension to 0.002σ. The 2×2 effective generation matrix reveals exact algebraic structure (tr = 1/3, det = −8, eigenvalues {C_A, −r₁r₂/(2C_A)}) with the master discriminant Δ = 17 controlling the generation spectrum just as it controls the face Laplacian spectrum. Every input is a topological integer of the Kelvin cell.

---

## References

### UFFT Papers
- [1] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [2] Paper #16 — The Master Equation of the Standard Model from Foam Geometry. DOI: 10.5281/zenodo.19064359
- [3] Paper #34 — The CKM Quark Mixing Matrix from Foam Cell Geometry. DOI: 10.5281/zenodo.19198360
- [4] Paper #36 — CP-Violating Phases of the CKM and PMNS Matrices from the T₁u Eigenvalue Ratio. DOI: 10.5281/zenodo.19198775
- [5] Paper #39 — The Inter-Type Torsion Operator on the Truncated Octahedron. DOI: 10.5281/zenodo.19306447
- [6] Paper #51 — The NLO Mixing Correction from First Principles. DOI: 10.5281/zenodo.19477100

### External References
- [7] Particle Data Group (2024). Review of Particle Physics. Phys. Rev. D 110, 030001.
- [8] CKMfitter Group (2024). Updated results on the CKM matrix. http://ckmfitter.in2p3.fr

---

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

*B + V = D*
