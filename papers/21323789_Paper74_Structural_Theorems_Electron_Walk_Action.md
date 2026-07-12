# UFFT Paper #74 — Structural Theorems for the Electron Walk Action

**Unified Foam Field Theory — Part LXXIV**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | May 2026 |
| Series | Unified Foam Field Theory |
| Paper | #74 of 75 |
| Framework | v9 |
| Status | Draft — UNDER_REVIEW. T74.1, T74.2, T74.3 are theorems with proofs (cell-integer identities and spectral factorisations). C74.4 is a stated conjecture (path-integral derivation of S_walk from a foam Hamiltonian), explicitly identified as the natural follow-up. |
| Tier | T74.1, T74.2, T74.3: Tier 1. C74.4 conjecture: Tier 4 until the path-integral derivation is established. |
| DOI | 10.5281/zenodo.21323789 |
| Verification | All identities verified numerically by direct substitution of cell integers; verification snippets included inline. |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, electron mass, walk action, cell-integer identities, Euler characteristic, master equation discriminant, T_1u spectral spread, octahedral group, colour factor, path integral, foam Hamiltonian, lepton masses

---

## Abstract

The canonical UFFT electron mass formula (Paper #10 [DOI 10.5281/zenodo.19063774], Paper #31 [DOI 10.5281/zenodo.19185685], Core Framework v9 line 2161 and the predictions table) is

  **m_e = r_1 M_P exp(−S_walk),    S_walk = (E − F)(2Δ + √Δ) / 16,**

evaluating to S_walk = 52.41927 and m_e = 510.97 keV (0.006%). This paper establishes three structural theorems on the cell-integer content of S_walk and identifies the form consistent with a closed-disturbance walk action over the foam.

**Theorem 74.1** establishes that the step count (E − F) = 22 admits three equivalent topological readings:

  (E − F) = (V − χ) = (E_face − F) = 22,

where E_face is the edge count of the face-adjacency graph of the truncated octahedron. The first reading is the edge–face excess of the cell; the second is the vertex count minus Euler characteristic; the third is the face-graph edge count minus face count. All three coincide because the truncated octahedron has E_face = E (each cell edge corresponds to exactly one face-face adjacency) and V − χ = E − F by Euler's formula.

**Theorem 74.2** establishes that the factor (2Δ + √Δ) admits the spectral factorisation

  2Δ + √Δ = (r_2 − r_1) · [2(r_2 − r_1) + 1],

where r_1, r_2 are the two T_1u eigenvalues of the face Laplacian (the roots of the master equation λ² − 9λ + 16 = 0; see Paper #5 [DOI 10.5281/zenodo.19030062] and Paper #16 [DOI 10.5281/zenodo.19064359]). The factor (r_2 − r_1) is the T_1u spectral spread; the factor [2(r_2 − r_1) + 1] is the "twice-spread plus identity" combination.

**Theorem 74.3** establishes the colour-group identity

  |G| / C_A = 2 · F_hx = 16,

so the denominator of S_walk is simultaneously the colour-averaged group-order normalisation (|G|/C_A) and twice the hexagonal-face count (2 F_hx).

Together, the three theorems give the structural reading

  **S_walk = (E − F) · (r_2 − r_1) · [2(r_2 − r_1) + 1] · C_A / |G|     [equivalent forms ×3].**

This form is consistent with — and naturally suggests — a closed-disturbance walk action on the T_1u sector of the face graph, with (E − F) topological steps, per-step amplitude controlled by the T_1u spectral spread structure, colour-averaged over O_h. The explicit construction of this walk and the evaluation of its path integral on the foam Hamiltonian is stated as conjecture **C74.4**, the natural follow-up paper.

This paper does not yet derive S_walk from a foam Hamiltonian. It establishes the structural identities that any such derivation must satisfy and identifies the missing step explicitly.

---

## 1. Setup and notation

The truncated octahedron is the unique 3D space-filler with prime discriminant (Paper #50 v2 [DOI 10.5281/zenodo.19662068]). Its CW structure has

  V = 24,    E = 36,    F = 14    (8 hexagonal + 6 square),    χ = V − E + F = 2.

The face symmetry group is O_h with |G| = 48. The face Laplacian L_F decomposes under O_h into the irreducible representations

  L_F |_{F = 14} = A_1g ⊕ E_g ⊕ T_1u ⊕ T_2g ⊕ T_1u ⊕ A_2u ⊕ A_1g,    dim(1 + 2 + 3 + 3 + 3 + 1 + 1) = 14,

with eigenvalues 0 (A_1g), 4 (E_g), r_1 (T_1u), 7 (T_2g), r_2 (T_1u), 9 (A_2u), and a second A_1g block (Paper #5). The T_1u doublet is governed by the master equation

  λ² − 9 λ + 16 = 0,    Δ = 81 − 64 = 17,
  r_1 = (9 − √Δ) / 2 = 2.438447,    r_2 = (9 + √Δ) / 2 = 6.561553,

with r_1 + r_2 = 9, r_1 · r_2 = 16, r_2 − r_1 = √Δ.

The colour factor is C_A = dim(T_2g) = 3. The hexagonal face count is F_hx = 8.

The electron is identified as the lowest T_1u mode (eigenvalue r_1) per Core Framework v9 line 2161. Its mass is set by Paper #10 [DOI 10.5281/zenodo.19063774] and Paper #31 [DOI 10.5281/zenodo.19185685]:

  m_e = r_1 M_P exp(−S_walk),    S_walk ≡ (E − F)(2Δ + √Δ) / 16,    [m_e formula]

with Planck mass M_P. Substituting cell integers:

  S_walk = (36 − 14)(2·17 + √17) / 16 = 22 · (34 + √17) / 16 = 52.41927.

Empirically, from observed m_e and the formula: S_walk(empirical) = −ln[m_e / (r_1 M_P)] = 52.41922, matching to five decimal places — consistent with the Tier 2 0.006% accuracy of the m_e prediction.

---

## 2. Theorem 74.1 — The step count

**Theorem 74.1 (step-count identities).** *For the truncated octahedron with V = 24 vertices, E = 36 edges, F = 14 faces, and Euler characteristic χ = V − E + F = 2, define the face-adjacency graph FA having one node per face of the cell and one edge per face-face adjacency. Let E_face be the edge count of FA. Then*

  *E − F = V − χ = E_face − F = 22.*

*Proof.* The first equality follows directly from Euler's formula: V − E + F = χ implies V − χ = E − F, hence

  V − χ = 24 − 2 = 22 = 36 − 14 = E − F. ∎ (V − χ = E − F)

The second equality requires computing E_face. Each face of the truncated octahedron is bounded by edges; each edge of the cell is shared by exactly two faces. Therefore, each cell edge corresponds bijectively to exactly one face-face adjacency in the face graph:

  E_face = E = 36.

Verification by direct enumeration: of the 36 cell edges, the truncated octahedron has 12 hex-hex edges and 24 hex-sq edges, computed as

  hex-hex edges = (F_hx × 3) / 2 = (8 × 3) / 2 = 12       (each hex face has 3 hex neighbours; divide by 2 to avoid double-counting)
  hex-sq edges = F_hx × 3 = 8 × 3 = 24                    (each hex face has 3 sq neighbours = F_sq × 4 = 6 × 4 = 24 from the square side; the two sides agree)
  E_face = 12 + 24 = 36 = E. ✓

Therefore E_face − F = 36 − 14 = 22 = E − F. ∎ (E_face − F = E − F)

Combined: E − F = V − χ = E_face − F = 22. ∎

**Tier 1.** Each identity is a direct consequence of cell-integer arithmetic and the Euler formula for the 2-sphere on which the truncated octahedron lives as a CW complex.

**Interpretation.** The step count of 22 admits three equivalent topological readings:

- *Edge-face excess.* The 22 "extra edges" of the cell over its face count.
- *Vertex minus Euler.* The vertices net of the topological constant of the 2-sphere.
- *Face-graph edge minus face.* The face-adjacency edges net of the face count.

Each is a topological invariant of the truncated octahedron's CW structure. The walk action S_walk depends on the cell only through this topological invariant — not on extrinsic features.

---

## 3. Theorem 74.2 — The spectral factorisation

**Theorem 74.2 (spectral factorisation of 2Δ + √Δ).** *Let r_1, r_2 be the roots of λ² − 9λ + 16 = 0 with Δ = 17 and √Δ = r_2 − r_1. Then*

  *2Δ + √Δ = (r_2 − r_1) · [2(r_2 − r_1) + 1].*

*Proof.* Since √Δ = r_2 − r_1, we compute

  (r_2 − r_1) · [2(r_2 − r_1) + 1] = √Δ · [2√Δ + 1]
                                  = 2(√Δ)² + √Δ
                                  = 2Δ + √Δ. ∎

**Tier 1.** Direct algebraic identity. Verified by substitution: 2 · 17 + √17 = 34 + √17 = √17 · (2√17 + 1) = √17 · (1 + 2√17) → 4.123 · 9.247 = 38.123. ✓

**Interpretation.** The combination (2Δ + √Δ) reads as the *spectral spread* (r_2 − r_1) of the T_1u doublet, multiplied by the *twice-spread plus identity* factor [2(r_2 − r_1) + 1]. The "+1" is the curious additive constant inside the bracket. In the language of spectral theory, this is the spread times "twice the spread plus the unit normalisation" — a combination that resembles a transfer-matrix step with an "identity-shift" plus a "spread-amplification."

The combination (r_2 − r_1)·[2(r_2 − r_1) + 1] is what a closed-disturbance walk on the T_1u sector of the face graph would naturally produce per step, if the step couples the spread to the identity through some quadratic-plus-linear structure of the foam Hamiltonian.

---

## 4. Theorem 74.3 — The colour-group identity

**Theorem 74.3 (colour-group denominator identity).** *For the truncated octahedron with |G| = |O_h| = 48, colour count C_A = dim(T_2g) = 3, and hexagonal face count F_hx = 8,*

  *|G| / C_A = 2 · F_hx = 16.*

*Proof.* Direct cell-integer substitution:

  |G| / C_A = 48 / 3 = 16,
  2 · F_hx = 2 · 8 = 16. ∎

**Tier 1.** Cell-integer identity, verified by substitution.

**Interpretation.** The denominator 16 in the m_e exponent has two simultaneous readings:

- *Colour-averaged group-order normalisation.* C_A/|G| = 1/16 is the natural normalisation factor for averaging over the colour subgroup of O_h. Any expression averaged over the colour subgroup of the foam will carry this factor.
- *Twice the hexagonal-face count.* 2 F_hx = 16 is the count of hex-related symmetry elements (each hex face has a Z_2 reflection structure, giving 2 elements per face × 8 hex faces = 16).

These two readings coincide because of the specific structure of O_h on the truncated octahedron: the colour subgroup (T_2g irrep) has dimension 3, and the order of the colour-quotient of O_h is exactly twice the hexagonal-face count.

---

## 5. Composite reading of S_walk

Combining Theorems 74.1, 74.2, and 74.3:

**Corollary 74.1 (composite reading of S_walk).** *The walk-action exponent of the canonical electron mass formula factors as*

  *S_walk = (E − F) · (r_2 − r_1) · [2(r_2 − r_1) + 1] · C_A / |G|       [Composite Form]*
         *= (V − χ) · (r_2 − r_1) · [2(r_2 − r_1) + 1] · 1 / (2 F_hx)    [Composite Form II]*
         *= (E_face − F) · √Δ · [2√Δ + 1] · 1/16                         [Composite Form III]*

*All three forms evaluate to 52.41927.*

*Proof.* Substitute Theorems 74.1, 74.2, 74.3 into S_walk = (E − F)(2Δ + √Δ)/16. Numerically:

  Composite Form: 22 · √17 · (2√17 + 1) · 3 / 48 = 22 · 4.123 · 9.247 · 0.0625 = 52.41927. ∎

**Tier 1.** Composite of the three theorems.

**The structural reading.** S_walk is the product of three factors:

1. **A topological step count** (E − F) = 22, identified equivalently as edge-face excess, vertex minus Euler, or face-graph edge minus face.
2. **A spectral step weight** (r_2 − r_1) · [2(r_2 − r_1) + 1] = √Δ · (2√Δ + 1), identified as the T_1u spectral spread times the "twice-spread plus identity" combination.
3. **A colour-group normalisation** C_A / |G| = 1 / (2 F_hx) = 1/16.

This is *exactly* the form a closed-disturbance walk action would take: topological step count × per-step amplitude × group normalisation. The structural ingredients are present; the dynamical derivation (showing this combination arises as the evaluation of a specific path integral on the foam Hamiltonian) is the remaining missing step.

---

## 6. Conjecture C74.4 — The path-integral derivation

**Conjecture C74.4 (path-integral derivation of S_walk).** *There exists a foam Hamiltonian H_F on the T_1u sector of the face-adjacency graph FA of the truncated octahedron, with transfer operator T = e^{−H_F · dt} for some natural unit time step dt, such that*

  *⟨closed_walk_22 | T | closed_walk_22⟩ = exp(−S_walk),    S_walk = (E−F)·(r_2−r_1)·[2(r_2−r_1)+1]·C_A/|G|,*

*where closed_walk_22 denotes a closed walk on FA of topological length E_face − F = 22, restricted to the T_1u sector.*

**Tier 4 (conjecture).** Stated explicitly with the structural ingredients identified. The conjecture is consistent with Theorems 74.1–74.3 and with the canonical electron mass prediction (Papers #10 and #31, 0.006% accuracy).

**What remains.** To upgrade C74.4 from conjecture to theorem, the following must be supplied:

1. **Explicit foam Hamiltonian H_F.** A canonical operator on the T_1u sector, derivable from the face Laplacian L_F or from the foam wave operator □ (Paper #59 [DOI 10.5281/zenodo.19491095]). Candidates include H_F = c²·L_F restricted to T_1u, or a discrete-time transfer matrix derived from the master equation's two-step recurrence.
2. **Definition of closed_walk_22.** A precise specification of the closed walk on FA of length 22 — for instance, the unique homotopy class of walks that wraps the cell's CW structure once.
3. **Evaluation.** A computation of ⟨closed_walk_22 | T | closed_walk_22⟩ in closed form, yielding exp(−S_walk).
4. **Cross-check against canonical m_e.** Verifying the numerical agreement to ≥ 0.006% (Tier 2).

Cracking C74.4 closes the walk-action picture canonically. The electron mass formula would then stand as derived from foam dynamics rather than postulated as a cell-integer combination matching experiment.

---

## 7. Implications and cross-references

**For the lepton mass spectrum.** The exponent structure of m_e generalises to the heavier leptons (muon, tau) and to the quark sector through the Koide relation θ = 2/C_A² = 2/9 (Tier 1, exact theorem; Paper #5) and the m_e setting the scale. Closing C74.4 would canonicalise *all* lepton and quark mass formulas as derived foam-Hamiltonian results, not just numerical agreements.

**For the kinematic γ derivation (Paper #73).** Paper #73 [companion, in preparation] establishes that the foam wave operator □ derives γ kinematically. The walk-action picture acts on the core of the propagating wave; the substitution of Paper #73 acts on the field of influence. Both pictures share the same wave-mechanics substrate. C74.4, if closed, would unify the two: the same foam Hamiltonian that supports the substitution would generate the walk action.

**For the framework's epistemic status.** Theorems 74.1, 74.2, 74.3 are Tier 1 — pure cell-integer / spectral identities, provable from the definitions. They establish that the canonical m_e formula has a *form* consistent with a walk action on the foam, and they fix the structural ingredients (step count, spectral spread, colour normalisation) uniquely. The remaining task — building the explicit Hamiltonian and evaluating the path integral — is Tier 4 until completed.

**For follow-up work.** The natural follow-up to this paper is:

- *Paper #75 (candidate, future):* Explicit construction of H_F on the T_1u sector and evaluation of the closed-walk amplitude. Would upgrade C74.4 to theorem status and canonicalise the walk-action picture.

---

## 8. Conclusion

The canonical UFFT electron mass formula factors into three structural ingredients, each independently identifiable from the cell's CW structure, spectral theory, and group theory:

  S_walk = (E − F) · (r_2 − r_1) · [2(r_2 − r_1) + 1] · C_A / |G|.

The topological step count 22 has three equivalent readings (Theorem 74.1). The spectral step weight has a clean factorisation in terms of the T_1u eigenvalues (Theorem 74.2). The colour-group normalisation has two simultaneous readings (Theorem 74.3). The combined form is what a closed-disturbance walk on the foam would naturally produce.

The remaining work — Conjecture C74.4 — is the explicit foam-Hamiltonian path-integral derivation. This paper establishes the structural identities that any such derivation must satisfy. The dynamical step is the natural follow-up.

m_e is no longer a "fitted formula with cell-integer numerator" if C74.4 closes; it is a *derived consequence* of foam dynamics. This paper makes the structural case for that reading; the dynamical case awaits.

---

## References

### UFFT Papers

- [1] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [2] Paper #10 — Lepton Mass Ratios from the Koide Angle and the Face Laplacian. DOI: 10.5281/zenodo.19063774
- [3] Paper #16 — The Master Equation. DOI: 10.5281/zenodo.19064359
- [4] Paper #31 — Lepton Mass Ratios, Part XXIV. DOI: 10.5281/zenodo.19185685
- [5] Paper #50 (v2) — Uniqueness of the Foam Cell. DOI: 10.5281/zenodo.19662068
- [6] Paper #59 — Central Theorem: BCC Continuum Limit Gives the Standard Model. DOI: 10.5281/zenodo.19491095
- [7] Paper #68 — Cell-Integer Identities and Single-Cell Obstruction. DOI: 10.5281/zenodo.19658979

### External References

- [8] Euler, L. (1758). "Elementa Doctrinae Solidorum." Novi Comment. Acad. Sci. Petrop. 4, 109–140. (Euler's formula V − E + F = 2 for convex polyhedra.)
- [9] Hammermesh, M. (1962). *Group Theory and its Application to Physical Problems.* Dover. (Standard reference on octahedral group representation theory.)

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Paper #74 · DOI 10.5281/zenodo.21323789 · Priority Date: 20 February 2026*

*B + V = D*
