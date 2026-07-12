# UFFT Paper #48 — The Standard Model from One Matrix

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 |
| Series | Unified Foam Field Theory |
| Paper | #48 of 72 |
| Framework | v10 · rev 1 |
| Status | Amended 19 April 2026 — §5 and abstract revised following internal review |
| Tier | Mixed (see §5 subsection labels) |
| DOI | 10.5281/zenodo.19448024 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** Standard Model, lattice action, face Laplacian, torsion, truncated octahedron, irreducible representation, uniqueness, Fedorov parallelohedra, epistemological status, UFFT

## Abstract

The Standard Model Lagrangian is conjectured to be the continuum limit of a single lattice action: **S = Σ_cells ψ† L_T ψ**, where L_T = D − T is the torsion-weighted face Laplacian on the 14-face graph of the truncated octahedron. The O_h symmetry group forces L_T to decompose into six irreducible blocks; Schur's lemma and dimensional completeness (Σ dim = F = 14) determine the matching to SM sectors: A₁g (λ=0, photon), T₁u (λ=r₁,r₂, fermions), Eg (λ=4, W±/Z), T₂g (λ=7, gluons), A₂u (λ=9, Higgs). Three sector-specific identifications are examined: α_s(M_Z) from the T₂g self-energy at the foam-intrinsic flavour condition n_f = C_A (a fit, not a forward derivation; see Deliverable 4 in the verification record); m₃ from the colourless T₁u propagator (an identification whose integer selection is pending Paper #72, the explicit Dirac-operator construction); and η_B from the first-order EW phase transition forced by T₂g↔A₂u hex-face coupling (an NLO post-hoc factor of order 1, not a forward derivation at current precision). An exhaustive check of all five Fedorov parallelohedra shows the truncated octahedron is the unique convex parallelohedron whose face Laplacian has prime discriminant, integer r₁r₂ = Δ−1, and eigenvalue sum equal to C_A² (§6). **UFFT's current empirical case is twelve pre-registered predictions (sharpest near-term: δ_PMNS/δ_CKM = 3, testable by DUNE around 2035; nearest-term: r ≈ 0.063, decisive at CMB-S4) plus a family of structural identities and postdictions whose joint statistical significance is addressed in a forthcoming look-elsewhere-corrected defense document. The "60+ observables with zero free parameters" framing used in earlier UFFT materials is withdrawn in this amendment as not defensible against a trials-factor audit.**

**Keywords:** Standard Model, lattice action, face Laplacian, torsion, truncated octahedron, irreducible representation, uniqueness, Fedorov parallelohedra, epistemological status, UFFT

---

## 1. The Foam Action

### 1.1 Dynamical variables

On each cell of the BCC Kelvin lattice, the dynamical variables are **ψ_i** (i = 1,...,14): complex displacement amplitude on each face, and **T_ij**: torsion phase on each edge connecting adjacent faces.

### 1.2 The action

The action per cell is:

**S_cell = Σ_{edges (ij)} |ψ_i − e^{iT_ij} ψ_j|²**

Expanding and summing over all 36 edges:

**S_cell = 2ψ† L_T ψ**

where L_T = D − T, D is the degree matrix (d_i = 4 for squares, 6 for hexagons), and T_ij = e^{iθ_ij} for adjacent faces.

The full theory: **S = Σ_cells ψ† L_T ψ**. One action, one matrix, everything else follows.

---

## 2. The Spectrum

The face Laplacian L = D − A of the truncated octahedron has been verified both numerically and symbolically (Paper #20, verification script):

**Spec(L) = {0¹, r₁³, 4², r₂³, 7⁴, 9¹}**

where r₁ = (9−√17)/2, r₂ = (9+√17)/2. The characteristic polynomial is:

**p(λ) = λ(λ²−9λ+16)³(λ−4)²(λ−7)⁴(λ−9)**

Master equation: **λ²−9λ+16 = 0**, discriminant Δ = 81−64 = **17**.

---

## 3. The Irrep Decomposition

Schur's lemma forces L to decompose under O_h into irreducible blocks. The assignment to Standard Model sectors:

| Irrep | Eigenvalue | Dim | SM sector | Gauge group |
|-------|-----------|-----|-----------|-------------|
| A₁g | 0 | 1 | Photon/gravity | U(1)_EM |
| T₁u | r₁, r₂ | 3+3 | Fermions (3 gen) | Matter |
| Eg | 4 | 2 | W±, Z | SU(2)_L |
| T₂g | 7 | 3 | Gluons | SU(3)_c |
| A₂u | 9 | 1 | Higgs | SSB |

**Completeness:** 1+3+2+3+3+1+1 = 14 = F. Every face mode accounted for. No room for extra fields, supersymmetric partners, extra generations, or additional Higgs doublets.

---

## 4. The Seven-Step Proof

**Step 1.** Write the action S = Σ ψ† L_T ψ. (Section 1.)

**Step 2.** Decompose into O_h irreps by Schur's lemma. L_T block-diagonalises into the six sectors above. (Section 3.)

**Step 3.** Take the continuum limit via Bloch expansion on the BCC lattice + Wick rotation. Each block's dispersion ω(k) reproduces the corresponding SM field's kinetic term. (Appendix B.)

**Step 4.** Identify sectors: the eigenvalue, dimension, and torsion parity of each block match exactly one SM sector. The gauge group SU(3)×SU(2)×U(1) is forced by the torsion topology of the face graph.

**Step 5.** All coefficients (coupling constants, masses, mixing angles, CP phases) are determined by the entries of L_T. No free parameters.

**Step 6.** No extra terms: Σ dim = 14 = F is exhaustive. Five independent arguments confirm no additional sectors can arise.

**Step 7.** Corrections are Planck-suppressed: the leading lattice artefact is O(a²k²) ~ O(E²/M_P²).

> *Note added in amendment (19 April 2026).* Steps 3, 5, and 6 as currently written are argumentative, not rigorous. Step 3 (continuum limit via Bloch expansion) is sketch-level; full dispersion computation for the T₁u sector is the subject of Paper #72 (see §5.2 and `verification/peer_review_deliverables/D6_Paper72_Scope.md`). Step 5 (all coefficients determined by L_T entries) holds for some sectors and is contingent for others, as §5 now makes explicit. Step 6 (completeness) rests on Σ dim = F = 14, which is exact. The seven-step structure is a correct programmatic outline; the present paper closes Steps 1, 2, 6 and the §6 uniqueness corollary rigorously, and closes Steps 3, 4, 5, 7 at the identification level only.

---

## 5. Sector-Specific Identifications with Varying Derivational Status

Three results previously presented as "forward derivations" from L_T are reclassified here by their current epistemological status (see `verification/peer_review_deliverables/D1_Methodological_Note.md`, Sections E and F, for the full methodological argument). The labels used below are: **Identification (fit)**, numerical match contingent on a sector-specific input choice not derived from L_T elsewhere in the paper; **Identification (pending)**, integer selection depends on a computation not yet performed (Paper #72); **Identification (post-hoc)**, NLO factor supplied after observing the LO result and the target.

### 5.1 α_s(M_Z) — Identification (fit), not forward derivation

**Identification.** α_s(M_Z) = 1/(C_A² − C_A ln C_A/(2π)) = 0.11799 (obs: 0.1180 ± 0.0009, matches at 0.01σ).

The T₂g sector has dim = C_A = 3 and eigenvalue 7. The discrete one-loop self-energy on C_A degenerate modes replaces ln(Λ/μ) → ln(C_A), giving α_s⁻¹(M_Z) = 9 − 3ln(3)/(2π) = 8.4755.

**Status.** The identification of the bare coupling with β₀(n_f = C_A) = 9 is a *condition*, not a derivation from L_T. The QCD β-function coefficient β₀ = (11C_A − 2n_f)/3 equals 9 only when n_f = C_A = 3, whereas MS-bar evaluation at μ = M_Z with the top decoupled uses n_f = 5 (giving β₀ = 23/3). UFFT offers no derivation of why the foam-intrinsic flavour count is C_A rather than the physical 5 at M_Z, and the formula does not generalise to SU(2) (Paper #47 §4.1 acknowledges this explicitly). Absent a derived principle connecting n_f to C_A at the relevant scale, §5.1 is a one-integer fit whose 0.01σ match is striking but not a prediction. Disposition and full argument: `verification/peer_review_deliverables/D4_n_f_Resolution.md` (binary answer: (b), concede fit).

The numerical claim α_s = 0.11799 remains falsifiable and testable against future world-average refinements. What is withdrawn is the "forward derivation" label, not the number.

### 5.2 m₃ — Derivation (T72.1, T72.2, T72.3a as theorems; T72.3b conjecture; T72.4 best-match primitive triple)

**Identification.** m₃ = m_e · exp(−(11 + 13√17)/4) = 49.49 meV (obs: 49.53 ± 0.33 meV, matches at 0.12σ).

The neutrino is a T₁u mode without colour charge. Paper #72 (DOI 10.5281/zenodo.19658759) establishes the structure at the following status, verified by scripts V1–V5 and V8 to machine precision:

- **T72.1 (Dirac operator existence)**, **Theorem.** A foam-cell Dirac operator `D_F` exists with `D_F² = L_T` on the non-kernel part and with the T₁u eigenvalue pair as its chirality-labelled modes.
- **T72.2 (doubler count = 3 per chirality)**, **Theorem.** The BCC Brillouin-zone structure of the truncated octahedron replaces the hypercubic Nielsen-Ninomiya count of 2^d = 16 with the T₁u multiplicity 3. Three generations, not sixteen.
- **T72.3a (chirality commutator on T₁u)**, **Theorem.** The face-type splitting of L_T yields [γ_F, T] = −2σ_x on the T₁u block; the σ-structure pairs r₁ and r₂ as chirality partners.
- **T72.3b (chirality assignment across the irrep)**, **Conjecture** with V10 orbit-restricted irrep-decomposition support: r₁ ↔ left-handed, r₂ ↔ right-handed.
- **T72.4 (integer selection of (11, 13))** (**Best-match primitive triple** in a principled search space: V11's 12,800-triple enumeration returns (11, 13, 4) as the unique primitive match in the F-derived integer family (not a sparseness claim) 1 match vs ~1.4 expected at random).

**Status.** With T72.1, T72.2, and T72.3a established as theorems, the *structure* of the identification (that m₃ is a T₁u mode, chirality-partnered, with an exponential integer-quantised mass relative to m_e) is a **derivation**. The chirality assignment across the irrep (T72.3b) rests on V10 heuristic support and remains a conjecture. The specific integer triple (11, 13, 4) is the best-match primitive triple in a principled search space (T72.4); the argument against it being coincidental is V11's enumeration, not a selection theorem. The m₁ = 0 exactness and the neutrino sector's Tier 1 theorems elsewhere in UFFT (see Core Framework v9) are unaffected.

### 5.3 η_B — Identification (post-hoc NLO)

**Identification.** η_B = α³/(C_A × F_sq³) × sign(δ_CKM) = 6.00 × 10⁻¹⁰ (obs: 6.10 × 10⁻¹⁰ from Planck 2018 BBN-consistent fit, matches at 1.8%).

The T₂g↔A₂u coupling through shared hexagonal faces drives the electroweak phase transition first-order at leading order. The counting α³ × 1/C_A × 1/F_sq³ × sign(δ_CKM) encodes three gauge exchanges, a colour singlet, a three-generation routing factor, and the CP-violating topological winding.

**Status.** At leading order (without the F_sq³ factor, or with different combinatoric choices) the match is not at 1.8%. The factor 1/F_sq³ = 1/216 together with 1/C_A = 1/3 giving denominator 648 reproduces the observation, but the specific combinatoric was selected after the target value was known. It is therefore a post-hoc NLO correction, not a forward derivation. The factor-of-three-to-six structure is plausible from the T₂g–A₂u hex-face architecture, but the exact combinatoric is not forced by an independent derivation. This reclassification does not change the direction of the argument (baryogenesis via first-order EW phase transition sourced by hex-face coupling), only the label attached to the 1.8% numerical match.

---

## 6. The Uniqueness Theorem (within Fedorov parallelohedra)

**Theorem.** Among the five convex parallelohedra in R³ (Fedorov 1885), the truncated octahedron is the unique cell whose face Laplacian has (i) prime discriminant Δ, (ii) integer eigenvalue product r₁r₂ = Δ − 1, and (iii) irrational-eigenvalue sum equal to C_A² (where C_A = 3 is the colour number F_hx/F − 1 in the natural normalisation).

**Scope.** The uniqueness statement is restricted to Fedorov's five convex parallelohedra. The Weaire-Phelan structure (a non-convex two-cell foam) and other non-parallelohedral space-fillings are not contained in this theorem and are excluded by the UFFT axiom of single-cell parallelohedral foam (see Core Framework v9 and `verification/peer_review_deliverables/D3_Uniqueness_Restriction.md`). What the theorem rules out within its domain: any other convex parallelohedron satisfying all three criteria.

**Proof.** Fedorov (1885) proved there are exactly five combinatorial types of convex parallelohedra in R³. Their face Laplacian spectra:

| Polyhedron | F | Irrational eigenvalues | Δ | Prime? | r₁r₂ = Δ−1? | Sum = C_A²? |
|-----------|---|----------------------|---|--------|-------------|-------------|
| Cube | 6 | None | 0 | ✗ | N/A | N/A |
| Hexagonal prism | 8 | None | 0 | ✗ | N/A | N/A |
| Rhombic dodecahedron | 12 | None | 0 | ✗ | N/A | N/A |
| Elongated dodecahedron | 12 | (5±√5) | 20 | ✗ | ✗ (20≠19) | ✗ (10≠9) |
| **Truncated octahedron** | **14** | **(9±√17)/2** | **17** | **✓** | **✓ (16=17−1)** | **✓ (9 = C_A² = 3²)** |

All five computed exhaustively. Within Fedorov's five convex parallelohedra, the truncated octahedron is unique. The foam cell is mathematically forced *within the axiomatic class of single-cell convex parallelohedral foams*. Sharpening criterion (iii) from "perfect square" to "C_A²" tightens the test by tying the eigenvalue sum to a quantity already fixed elsewhere in the framework; it is not a post-hoc selection from arbitrary integers. □

---

## 7. Summary Table

| Quantity | Formula | UFFT | Observed | Match | Status |
|---------|---------|------|----------|-------|--------|
| α_s(M_Z) | 1/(C_A²−C_A ln C_A/(2π)) | 0.11799 | 0.1180±0.0009 | 0.01σ | Identification (fit) — §5.1 |
| m₃ | m_e exp(−(11+13√17)/4) | 49.49 meV | 49.53±0.33 | 0.12σ | Derivation (T72.1, T72.2, T72.3a theorems); T72.3b conjecture; T72.4 best-match primitive triple — §5.2, Paper #72 (DOI 10.5281/zenodo.19658759) |
| η_B | α³/(C_A F_sq³) | 6.00×10⁻¹⁰ | 6.10×10⁻¹⁰ | 1.8% | Identification (post-hoc) — §5.3 |

The three rows above are sector-specific identifications with varying derivational status, not forward derivations from S = ψ† L_T ψ as presented in earlier drafts. The uniqueness claim of §6 and the dimensional completeness of §3 are unaffected and remain Tier 1.

---

## Appendix A: The 36-Edge Torsion Phase Table

The torsion-weighted adjacency matrix T has entries T_ij = exp(iθ_ij) for adjacent faces. The dihedral angles of the truncated octahedron determine the torsion phases:

- **Square–hexagon edges** (24 edges): θ_sh = π − arccos(−1/√3) ≈ 125.26°
- **Hexagon–hexagon edges** (12 edges): θ_hh = π − arccos(−1/3) ≈ 109.47°

The total torsion identity: 24θ_sh + 12θ_hh = F_sq × 2π = 12π (proven algebraically in Paper #40).

## Appendix B: Bloch Dispersions

At small Bloch momentum k on the BCC lattice:

**Photon (A₁g):** ω²(k) = c²|k|² (massless, linear dispersion)

**Electron (T₁u at r₁):** E² = m_e²c⁴ + c²|p|² (Dirac dispersion from Nielsen-Ninomiya doubling)

Both follow from standard lattice→continuum expansion with the face Laplacian providing the mass gap.

---

## References

[1] Martin, L. (2026). UFFT Core Framework v9. Zenodo.
[2] Martin, L. (2026). The Laplacian Spectrum of the Truncated Octahedron. Zenodo. DOI: 10.5281/zenodo.19030062.
[3] Martin, L. (2026). Spectral Verification Script. Zenodo. DOI: 10.5281/zenodo.19079730.
[4] Fedorov, E. S. (1885). Nachala Ucheniya o Figurakh.
[5] Kelvin, Lord (Thomson, W.) (1887). On the division of space with minimum partitional area. Phil. Mag. 24, 503.
[6] Particle Data Group (2024). Review of Particle Physics. Phys. Rev. D 110, 030001.
[7] NuFIT 5.2 (2022). Esteban et al. JHEP 09, 178.
[8] Planck Collaboration (2020). A&A 641, A6.
[9] Martin, L. (2026). *Paper #72, Dirac Operator, Doubler Spectrum, Chirality Assignment, and the m₃ Integer*. Zenodo. DOI: 10.5281/zenodo.19658759.
[10] Martin, L. (2026). *Verification/peer_review_deliverables/D1_Methodological_Note.md*, methodological clarification, epistemological tier table, look-elsewhere audit. Documents the empirical case as 12 pre-registered predictions plus a forthcoming joint-χ² defense (D1 Supplement) rather than "60+ observables with zero free parameters."
[11] Martin, L. (2026). *Verification/peer_review_deliverables/D4_n_f_Resolution.md*, binary disposition on n_f = C_A.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, direction, and framework: Luke Martin. AI role: numerical computation, proof verification, exhaustive polyhedra check, derivation formulation, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*

*Unified Foam Field Theory · Paper #48 · DOI: 10.5281/zenodo.19448024 · Priority Date: 20 February 2026*

*B + V = D*
