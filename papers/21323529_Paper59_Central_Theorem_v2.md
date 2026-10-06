# UFFT Paper #59 — The Central Theorem: From Foam to the Standard Model

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 (v2.0: July 2026; v3.0: October 2026) |
| Series | Unified Foam Field Theory |
| Paper | #59 of 75 |
| Framework | v10 |
| Version | 3.0 |
| Status | WITHDRAWN AS PROOF (October 2026). The composite five-step argument does not establish its conclusion; the external audit it was pending (Moscato, 6 October 2026) found explicit algebraic errors in Steps 2, 3 and 4 and an unproved premise in Steps 1 and 5. Retained as the record of the claim and its correction. The step-lemmas that are graph theorems (Theorem 4.1, 56.1, 56.2) stand. |
| Tier | 1 (graph-theorem step-lemmas only) · composite statement: OPEN, not established |
| DOI | 10.5281/zenodo.21323529 (v2.0; v1: 10.5281/zenodo.19491095) |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, foam field theory

## Changes in this version (3.0): withdrawal of the composite theorem

On 6 October 2026 an adversarial referee audit of the public repository (prepared for Prof. Pablo Moscato, University of Newcastle; one automated reviewer, not a human panel) examined this paper at full depth. Its findings on the five-step argument are correct and are accepted in full. Each is stated here with what it does to the paper. The original text is retained below, marked at the affected passages, so that the record of the claim and the record of its failure sit in one place.

**R1, Step 1 and Step 5 (gauge groups are supplied, not derived).** §2.1 and §6.4(ii) take the inter-cell link variables to be elements of SU(2) (and SU(3)), and then recover SU(2) Yang–Mills from the Wilson plaquette action. That derives SU(2) Yang–Mills from SU(2) links; it does not derive SU(2) from the face graph. The single-cell structure established in Paper #58 is the finite group D₃ on the Eg subspace, and nothing in this paper turns a finite internal group into a continuous local gauge redundancy. The stated quadratic action also lacks a temporal discretisation, a full inter-cell coupling prescription, a fermionic measure and gravitational variables; plaquette, Yukawa and quartic terms are added, not obtained by integrating out stated degrees of freedom. **Steps 1 and 5 are withdrawn as derivations.** They stand only as the statement of what a microscopic model would need to contain.

**R2, Step 2 (the displayed gamma matrices are not a Clifford algebra).** §3.3 sets γ⁰ = σ_z, γⁱ = σ_x ∂_i and γ⁵ = σ_z. A gamma matrix is not a differential operator; the same σ_x for all three spatial directions does not anticommute between directions; and γ⁵ = γ⁰ does not anticommute with γ⁰. The 2 × 2 block of §3.2 therefore does not define a 3+1-dimensional Dirac operator. The positive square root of Paper #72 is valid spectral mathematics but supplies neither spinor indices, Lorentz spin, statistics nor a chiral gauge representation, and its "chirality involution" cannot relate the positive and negative roots by unitary conjugation, which preserves the spectrum. **Step 2 is withdrawn.** No lattice fermion operator with a spinor space, Clifford relations and a treatment of doublers has been constructed.

**R3, Step 3 (the displayed Yukawa vertex is identically zero).** §4.2 writes ⟨T₁u(r₂)| T · P_A₂u · T |T₁u(r₁)⟩ ∝ −4I. The same section, corrected in v2.0, states that the inter-type operator T annihilates A₂u. Then T P_A₂u = P_A₂u T = 0 and the product vanishes identically; the referee's direct reconstruction gives ‖T P_A₂u T‖ = 0, and so does ours. The −1 charge of A₂u under T_hex cannot be inserted into a product mediated by a different operator. There is also a selection-rule obstruction: two odd T₁u fields and an odd A₂u field do not form an even O_h invariant by ordinary tensor product. **Step 3 is withdrawn.** The walk-action masses of Chapter 23 are a separate identification and are not affected by this paragraph, but no Yukawa vertex connecting them to the A₂u mode has been derived.

**R4, Step 4 (the Higgs mass-squared has the wrong sign as printed).** §5.1 writes μ² = −(λ_A₂u × τ_A₂u) × M_P² e^{−2S_H} and calls it negative. With λ_A₂u = 9 and τ_A₂u = −1 the bracket is −(9 × −1) = +9, so μ² is positive and the potential has a stable origin: no symmetry breaking follows. Independently of the sign, a negative T_hex eigenvalue does not imply a negative physical mass-squared (Paper #57 v2.0 already records that mapping as a premise, not a theorem), and a one-dimensional spatial irrep does not supply the four real components of a complex SU(2) doublet or its three Goldstone directions. **Step 4 is withdrawn.**

**R6 (the Symanzik matching script is not Hermitian).** §7 rests on `verification/Symanzik_Matching_BCC.py`. Its Bloch builder adds −t e^{ik·δ} to each diagonal entry without the reverse-hop conjugate, so H(k) is not Hermitian (‖H − H†‖_F ≈ 2.10 at k = (0.2, 0.3, 0.4)); `numpy.linalg.eigvalsh` then silently discards the imaginary diagonal. The script validates nothing about the matrix it builds, and several matching coefficients in it are stated rather than extracted. **§7 is withdrawn and the script is retired** (renamed `Symanzik_Matching_BCC_RETIRED.py` with a header note; it is kept so that the defect can be seen).

**R7 (D₃ is not a subgroup of SU(2)).** §6.4(i) says D₃ ≅ S₃ embeds in SU(2) through the binary dihedral lift. SU(2) has exactly one element of order two, −I; S₃ has three, so S₃ has no faithful embedding in SU(2). The binary dihedral group 2D₃ embeds, and S₃ is its quotient. Elementary, and it leaves the emergence problem of R1 untouched.

**What stands.** Theorem 4.1 (O_h decomposition of the face space, ρ = 2A₁g ⊕ Eg ⊕ 2T₁u ⊕ T₂g ⊕ A₂u), Theorems 56.1 and 56.2 (T² = −4I on T₁u; T₂₁ = 2U), the face-content table of Paper #57, and the spectrum itself are graph theorems and are confirmed by the audit. The particle–irrep map, the chirality labelling, the walk-action masses and every "derived" observable that depends on them are identifications conditional on premises (1)–(4) of the Core Framework's axiomatic accounting, and are now labelled that way throughout the framework. The sentence "all 26 Standard Model parameters determined by seven cell integers" is withdrawn as a theorem statement.

**What would be needed.** One complete microscopic model: all variables, the full action with time, inter-cell coupling, measure and interactions, and a derivation of its interacting continuum limit with a Hermitian lattice operator, an actual spinor structure, gauge anomaly cancellation with the complete chiral content, and a stated mechanism for continuous gauge redundancy. None of that is supplied by correcting the arithmetic above.

---

## Abstract

We state and assemble the framework's central claim: the continuum limit of the torsion-weighted face Laplacian action S = 2 Σ ψ†L_Tψ on the BCC lattice of truncated octahedra is the Standard Model coupled to general relativity, with gauge group SU(3)×SU(2)×U(1), three fermion generations, one Higgs doublet, and all parameters determined by the seven cell integers {V, E, F, |O_h|, C_A, Δ, d} = {24, 36, 14, 48, 3, 17, 3}. The argument proceeds in five steps: gauge kinetic terms from the 24 triangles and 42 four-cycles of the face graph; the Dirac equation from T₁u Wilson fermions; Yukawa couplings from the torsion cross-block T₂₁ = 2U; spontaneous symmetry breaking forced by the A₂u T_hex charge −1; and uniqueness of the continuum limit from asymptotic freedom with irrelevant O_h artefacts. Symanzik-style matching gives corrections scaling as (E/M_P)² ~ 10⁻³⁵, numerically negligible. Status is declared precisely: the individual step-lemmas are theorem-strength and cite their proofs; the composite five-step statement is a proof-sketch pending external audit.

---

## Changes in this version (2.0)

1. **Torsion operator citations corrected** per Paper #57 v2.0: the A₂u charge −1 is its eigenvalue under T_hex = (1/3)·A_hh (the hexagonal-subgraph operator), not under the inter-type operator T (which annihilates A₂u). Sections 4.2 and 5.1 updated; no numerical result changes.
2. **Status field clarified:** the individual step-lemmas are theorem-strength; the composite five-step statement is a proof-sketch pending external audit, consistent with the framework's own status declaration in *From Foam to Fermions* ("Before You Begin").
3. Corrections machine-verified in `verification/verify_FtF_audit_2026-07.py` (UFFT repository).

---

## 1. Statement

**Central Theorem.** *Let Λ_BCC be the BCC lattice of truncated octahedra in R³, with face displacement field ψ_i (i = 1,...,14) on each cell, torsion phase T_{ij} = exp(iθ_{ij}) on each edge, and the lattice action:*

***S = Σ_{cells} Σ_{edges (ij)} |ψ_i − e^{iT_{ij}} ψ_j|² = 2 Σ_{cells} ψ† L_T ψ***

*where L_T = D − T is the torsion-weighted face Laplacian (D = degree matrix, T = torsion adjacency). In the continuum limit a → 0, the long-wavelength effective field theory is:*

***L = L_{YM} + L_{Dirac} + L_{Yukawa} + L_{Higgs} + L_{GR}***

*with gauge group SU(3)_c × SU(2)_L × U(1)_Y, three fermion generations, one Higgs doublet, and all 26 Standard Model parameters determined by seven cell integers {V, E, F, |O_h|, C_A, Δ, d} = {24, 36, 14, 48, 3, 17, 3}.*

The proof proceeds in five steps.

---

## 2. Step 1 — Gauge Kinetic Terms

### 2.1 The gauge link variables

*[Withdrawn in v3.0, item R1: the links are assigned values in the gauge group rather than derived; see the notice at the top of this paper.]*

On each edge of the face graph, the torsion phase T_{ij} = exp(igA_μ^a τ^a · Δx_μ) serves as the lattice gauge link. The 36 edges of the face graph carry 36 link variables. Under a local gauge transformation Ω_i at face i:

T_{ij} → Ω_i T_{ij} Ω_j†

This is the standard lattice gauge transformation.

### 2.2 The plaquette action

The face graph of the truncated octahedron has:
- **24 triangles** (3-cycles): each with 1 square face and 2 hexagonal faces sharing an edge. These are the elementary plaquettes of the strong sector.
- **42 four-cycles** (4-cycles): the elementary plaquettes of the electroweak sector.

The Wilson plaquette action on the face graph is:

**S_gauge = β₃ Σ_{triangles} Re Tr(1 − U_△) + β₂ Σ_{4-cycles} Re Tr(1 − U_□)**

where U_△ = T_{ij}T_{jk}T_{ki} is the ordered product around a triangle, and similarly for 4-cycles.

### 2.3 Continuum limit

Expanding U_P = 1 − ig²a²F_μν + O(a⁴) and summing over plaquettes:

**S_gauge → (1/4) ∫ d⁴x [F_μν^a F^{μν,a}]_{SU(3)} + (1/4) ∫ d⁴x [W_μν^a W^{μν,a}]_{SU(2)} + (1/4) ∫ d⁴x [B_μν B^{μν}]_{U(1)}**

The 24 triangles provide the SU(3) plaquettes (each triangle involves hex-hex torsion = colour exchange). The 42 four-cycles provide the SU(2)×U(1) plaquettes (each involves sq-hex boundaries = electroweak transitions).

The gauge couplings are set by the plaquette counts:
- g₃² ∝ 1/(24 × a⁴) × (lattice→continuum matching factor)
- g₂² ∝ 1/(42 × a⁴) × (matching factor)

The ratio g₃²/g₂² is determined by the triangle-to-plaquette ratio and the irrep dimensions, ultimately yielding the cell-integer formulas for α_s and sin²θ_W. □

---

## 3. Step 2 — Dirac Equation from T₁u Wilson Fermions

### 3.1 The two-sublattice structure

The T₁u sector of L_T restricted to the (square, hexagonal) face-type basis is:

**L|_{T₁u} = [4, −2; −2, 5]**

This is a 2×2 massive Dirac Hamiltonian with:
- Sublattice masses: m_sq = 4 (square-face degree), m_hx = 5 (hex-face effective degree)
- Inter-sublattice hopping: t = 2 (the off-diagonal coupling from sq-hex adjacency)
- Eigenvalues: r₁ = (9−√17)/2 ≈ 2.438 (light), r₂ = (9+√17)/2 ≈ 6.562 (heavy)
- Wilson mass parameter: δm = |m_hx − m_sq|/2 = 1/2

### 3.2 The Bloch expansion

On the BCC lattice with lattice vectors **a₁** = a(1,1,−1)/2, **a₂** = a(−1,1,1)/2, **a₃** = a(1,−1,1)/2, the Bloch-expanded T₁u Hamiltonian at small k is:

**H(k) = [4 + c_sq|k|²a², −2 + t₁(k); −2 + t₁(k)*, 5 + c_hx|k|²a²]**

where c_sq, c_hx are the band curvatures (computable from the BCC second-neighbour hopping integrals) and t₁(k) is the k-dependent inter-sublattice coupling.

### 3.3 Continuum identification

*[Withdrawn in v3.0, item R2: the matrices displayed below do not satisfy the Clifford relations; see the notice at the top of this paper.]*

Defining the Dirac spinor ψ = (ψ_L, ψ_R)ᵀ where ψ_L is the T₁u(r₁) component (left-handed, 62% square, Paper #57) and ψ_R is the T₁u(r₂) component (right-handed, 38% square):

**H(k) → iγ^μ ∂_μ + m_f**

with:
- γ⁰ = σ_z (distinguishes particle from antiparticle by eigenvalue sign)
- γ^i = σ_x ∂_i (mixes left and right through the off-diagonal coupling)
- γ⁵ = σ_z (chirality = sublattice identity)
- m_f determined by the eigenvalue and the exponential suppression from the walk action

### 3.4 Doubler absence

The Nielsen-Ninomiya theorem is evaded by the natural Wilson mechanism (Paper #57, §10.2). The T₁u block has **unequal diagonal entries** (4 ≠ 5), explicitly breaking the naive chiral symmetry {D, γ₅} = 0. The eigenvalue gap √17 ≈ 4.12 in lattice units serves as the Wilson mass parameter, lifting all would-be doublers at the Brillouin zone boundary. Numerical scan at 40³ k-points confirms exactly one minimum per band (§10.2). □

---

## 4. Step 3 — Yukawa Couplings from the Torsion Cross-Block

### 4.1 The vertex structure

The Yukawa coupling connects left-handed fermions, the Higgs, and right-handed fermions:

**L_Yukawa = y_f ψ̄_L φ ψ_R + h.c.**

On the foam, this vertex is the trilinear coupling T₁u(r₁) × A₂u × T₁u(r₂) mediated by the torsion operator.

### 4.2 The torsion cross-block

*[Withdrawn in v3.0, item R3: since T annihilates A₂u, the matrix element displayed below is identically zero; see the notice at the top of this paper.]*

Paper #56 proved that the inter-type torsion operator T has off-diagonal block T₂₁ = 2U where U is unitary (all singular values = 2). This operator connects the two T₁u eigenspaces through the A₂u channel:

**⟨T₁u(r₂)| T · P_{A₂u} · T |T₁u(r₁)⟩ ∝ T₂₁ × (−1) × T₁₂ = −4I**

The factor (−1) is the A₂u scalar torsion charge: its eigenvalue under T_hex = (1/3)·A_hh, the degree-normalised adjacency of the hexagonal subgraph (Paper #57 v2.0; the inter-type operator T annihilates A₂u, so the charge belongs to T_hex, not T). The Yukawa coupling for each generation is:

**y_f ∝ exp(−S_f)** where S_f is the walk action on the face graph

The walk action S_f = (R_f + I_f √17)/16 involves cell-integer combinations specific to each fermion flavour (the rational part R_f and irrational part I_f are computed in Chapter 23 of the book). The exponential suppression from the walk action generates the mass hierarchy: from the top quark (y_t ≈ 1) to the electron neutrino (y_ν ≈ 10⁻¹²). □

---

## 5. Step 4 — Spontaneous Symmetry Breaking

### 5.1 The Higgs potential from A₂u

*[Withdrawn in v3.0, item R4: with λ_A₂u = 9 and τ_A₂u = −1 the printed μ² is +9 × (positive), not negative; see the notice at the top of this paper.]*

The A₂u mode (Laplacian eigenvalue 9, T_hex charge −1) generates the Higgs potential:

**V(φ) = μ²|φ|² + λ|φ|⁴**

where:
- μ² = −(λ_{A₂u} × τ_{A₂u}) × M_P² × exp(−2S_H) = negative (because the T_hex charge τ_{A₂u} = −1)
- λ = 1/F_hx = 1/8 = 0.125 (tree-level, from the A₂u ⊗ A₂u → A₁g channel)

The negative μ² is not a parameter choice. It is a geometric theorem: the A₂u mode is the UNIQUE mode with negative T_hex charge (−1 is the bipartite minimum of the cube graph; Paper #57 v2.0, Theorem 57.1), and negative charge → negative mass-squared (the mode sits at a local maximum, not minimum, of the torsion potential).

### 5.2 The vacuum expectation value

The VEV v = √(−μ²/λ) is determined by the hierarchy formula:

**v = M_P × exp(−(|O_h| + V + E + F + (|O_h| − C_A)√Δ)/8) = 246.24 GeV**

(observed: 246.22 GeV, 0.009% match).

### 5.3 The Goldstone mechanism

After SSB, the A₂u scalar φ = v + h (where h is the physical Higgs) provides three Goldstone bosons absorbed by the Eg modes (W±) and the Eg–A₁g mixed mode (Z):

- W± mass: M_W = gv/2 (from Eg coupling to the VEV)
- Z mass: M_Z = M_W/cosθ_W (from Eg–A₁g mixing at angle θ_W)
- Photon: remains massless (A₁g at λ = 0, the flat mode)
- Higgs mass: m_H = √(2λ)v = v/(2√2) × (correction from eigenvalue ratio) → m_H/M_Z = 18/(9+√17) □

---

## 6. Step 5 — Uniqueness of the Continuum Limit

### 6.1 Asymptotic freedom

Both non-abelian gauge sectors are asymptotically free:

**SU(3):** β₀ = (11C_A − 2n_f)/3 = (33 − 6)/3 = 9 > 0 (for n_f = 3 active flavours at M_Z)

**SU(2):** β₀ = (22/3 − 4n_g/3) = (22 − 12)/3 = 10/3 > 0 (for n_g = 3 generations)

Asymptotic freedom guarantees the existence of a continuum limit: the gauge coupling g → 0 as a → 0, with the lattice theory flowing to a free (Gaussian) fixed point in the ultraviolet. The SM is the unique non-trivial infrared theory emerging from this UV fixed point with the specified matter content.

### 6.2 O_h → O(3) lattice artefacts

The BCC lattice has O_h point symmetry (|O_h| = 48). In the continuum limit, O_h → O(3). The first O_h-invariant operator not proportional to an O(3) invariant is the quartic:

**Δ_4 = ∂_x⁴ + ∂_y⁴ + ∂_z⁴ − (3/5)(∂²)²**

This operator has dimension 4 in spatial coordinates, hence dimension **6** in the 4D spacetime action (including time derivatives). In 4D, operators of dimension d > 4 are **irrelevant** in the renormalisation group sense: their coefficients scale as a^{d−4} → 0 as a → 0.

Therefore: all O_h lattice artefacts vanish in the continuum limit. The theory flows to the unique O(3)-symmetric (and hence Lorentz-symmetric after Wick rotation) fixed point. The BCC lattice structure leaves no trace in the continuum physics.

### 6.3 Completeness excludes extra sectors

The face space is 14-dimensional (F = 14). The O_h irrep decomposition is exhaustive:

dim(A₁g) + dim(T₁u) + dim(Eg) + dim(T₁u) + dim(T₂g) + dim(A₁g) + dim(A₂u) = 1+3+2+3+3+1+1 = 14

No additional sectors can appear without increasing F beyond 14, which would require a different polyhedron — but the truncated octahedron is the unique space-filler with prime discriminant (Paper #50). The Standard Model is the ONLY theory that fits in 14 dimensions with the O_h symmetry constraints.

### 6.4 D₃ → SU(2) emergence

*[Withdrawn in v3.0, items R1 and R7: (i) is false (S₃ does not embed in SU(2)); (ii)–(iv) assume SU(2)-valued links and so assume the conclusion; see the notice at the top of this paper.]*

Paper #58 showed that the Eg subspace carries the dihedral group D₃ ≅ S₃ at the single-cell level, not SU(2). The emergence of the continuous gauge group proceeds by the standard lattice mechanism:

(i) D₃ is a subgroup of SU(2) (via the binary dihedral embedding BD₃ ↪ SU(2)).
(ii) On the lattice, gauge link variables U_{ij} take values in the full group SU(2), not just D₃. The D₃ structure constrains the single-cell representation, but inter-cell links sample the full group.
(iii) The Wilson action for the gauge links:

**S_W = β Σ_P Re Tr(1 − U_P)**

is invariant under the full SU(2) gauge group, regardless of the discrete D₃ structure of individual plaquettes.
(iv) In the continuum limit, the lattice gauge theory with SU(2) link variables and Wilson action flows to SU(2) Yang-Mills — this is the foundational result of lattice gauge theory (Wilson 1974, Creutz 1980).

The same argument applies to SU(3) via the T₂g sector, where the discrete D₃ structure of the three torsion directions embeds into the full SU(3) gauge group through the lattice link variables. □

---

## 7. The Symanzik Matching — Computed

*[Withdrawn in v3.0, item R6: the script this section relies on builds a non-Hermitian Bloch matrix; see the notice at the top of this paper.]*

The five steps above constitute the proof. The Symanzik matching — the one caveat identified in the original formulation — has now been computed explicitly.

**The Symanzik effective theory** expands the lattice action in powers of the lattice spacing a:

S_eff = S_continuum + a² Σ_i c_i O_i^(6) + O(a⁴)

where O_i^(6) are dimension-6 operators. For the BCC truncated octahedron lattice, the computation yields:

**Gauge sector (Wilson plaquette action):** The standard Wilson coefficient c_gauge = 1/12 applies. The 24 triangle plaquettes (SU(3)) and 42 four-cycle plaquettes (SU(2)×U(1)) both contribute standard O(a²) corrections.

**Fermion sector (natural Wilson fermions):** The Wilson parameter r_W = (m_hx − m_sq)/2 = (5−4)/2 = 1/2 gives c_ferm = r_W/2 = 1/4. The mass gap √17 lifts all doublers.

**O_h anisotropy:** The Q₄ = Σ k_i⁴ − (3/5)|k|⁴ coefficient from the BCC nearest-neighbour geometry is 1.2 (nonzero — the BCC lattice does break O(3) at fourth order in momentum). This produces dimension-6 operators of the form (∂⁴φ) with O_h symmetry rather than O(3) symmetry. These operators are **irrelevant** in 4D (dimension 6 > 4), confirming Step 5 of the proof.

**Physical magnitude:** At the electroweak scale, the Symanzik corrections scale as:

δO/O ~ c × (E/M_P)² ~ 0.25 × (M_Z/M_P)² ~ 1.4 × 10⁻³⁵

This is **30 orders of magnitude below** the precision of any UFFT prediction (the most precise being α at ~10⁻⁸ relative accuracy). Even at the GUT scale (E ~ 10¹⁶ GeV), the correction is ~10⁻⁷, still far below any observable effect.

**Conclusion:** The Symanzik matching exists, is calculable, and is negligible. It does not affect the identity of the continuum theory (proved by Steps 1–5) or the numerical accuracy of any framework prediction. The Central Theorem stands without qualification.

**Verification:** The computation is performed by the script `Symanzik_Matching_BCC.py`, which builds the Bloch Hamiltonian H(k) on the BCC lattice, computes the Taylor expansion to O(k⁴), extracts the fourth-order anisotropy coefficients, and evaluates the physical magnitude of the corrections. All numbers are reproduced from cell integers with no external input.

---

## 8. The Proof Chain

The complete logical chain from axiom to Standard Model:

**Axiom Zero (B+V=D)** → truncated octahedron is the unique cell (Paper #50) → face Laplacian L with spectrum {0, r₁, 4, r₂, 7, 9} (Paper #10) → O_h irrep decomposition (Theorem 4.1) → particle–irrep map forced by exhaustion (Papers #57, #58) → lattice action S = ψ†L_Tψ (Paper #48) → Dirac fermions from T₁u Wilson mechanism (§3) → gauge kinetic terms from plaquette action (§2) → Yukawa couplings from torsion cross-block T₂₁ = 2U (§4, Paper #56) → SSB from A₂u torsion = −1 (§5, Paper #57) → all 26 parameters from seven cell integers → continuum limit exists and is unique (§6) → **QED**.

Every link is either a mathematical theorem or a consequence of established lattice field theory. No free parameters. No adjustable identifications. The Standard Model is the continuum limit of the foam.

---

## 9. Complete Status Summary

| Component | Status | Proved in |
|-----------|--------|-----------|
| Cell uniqueness | Theorem | Paper #50 |
| Spectrum | Theorem | Paper #10, verification script |
| Particle–irrep map | Theorem (exhaustion) | Papers #57, #58 |
| Chirality assignment | Theorem (B+V=D + T²=−4I) | Papers #56, #57 |
| Three generations = dim(T₁u) = 3 | **Theorem (face space exhaustion)** | **Paper #60, Theorem 60.2** |
| SSB forced | Theorem (A₂u torsion = −1) | Paper #57 |
| Gauge group SU(3)×SU(2)×U(1) | Theorem (exhaustion + lattice) | Paper #58 + §2 |
| Fermion kinetic terms | Theorem (Wilson mechanism) | §3, book §10.2 |
| Yukawa couplings | Theorem (T₂₁ = 2U) | Paper #56 + §4 |
| Chiral anomaly coefficients {3,2,1} | **Theorem (T₁u dim + torsion GW relation)** | **Paper #60, Theorem 60.1** |
| Hierarchy v/M_P | Derived (0.009%) | §5 |
| General Relativity emergence | **Theorem (T₂g metric mode + Weinberg-Witten)** | **Paper #60, Theorem 60.3** |
| Continuum limit exists | Standard result (AF + irrelevant artefacts) | §6 |
| Continuum limit unique | Standard result (completeness + AF) | §6 |
| Lattice-to-continuum Bloch expansion complete | **Theorem (face space exhaustion + Bloch)** | **Paper #60, Theorem 60.4** |
| Symanzik matching | **Computed: ~10⁻³⁵ at EW scale — negligible** | §7 |

---

## 10. Conclusion

The Central Theorem is proved. The BCC lattice of truncated octahedra, with the torsion-weighted face Laplacian action S = ψ†L_Tψ and the single axiom B+V=D, flows in the continuum limit to the Standard Model coupled to General Relativity, with all parameters determined by cell geometry.

The Symanzik matching — the one remaining calculation — has been computed explicitly (§7). The O(a²) corrections scale as (E/M_P)² ~ 10⁻³⁵ at the electroweak scale, 30 orders of magnitude below any framework prediction.

**Paper #60 (April 2026) closes the four remaining proof-chain gaps acknowledged in the original version of this paper:** (1) the chiral anomaly coefficients are correct (Theorem 60.1); (2) exactly three generations follows from dim(T₁u) = 3 by face-space exhaustion (Theorem 60.2); (3) General Relativity emerges from the T₂g collective metric mode via the Weinberg-Witten theorem (Theorem 60.3); (4) the Bloch expansion of the foam action is the complete SM+GR Lagrangian (Theorem 60.4). The proof is complete without qualification.

The Standard Model is not postulated. It is the unique continuum limit of the simplest possible foam. The particle content, gauge group, chirality structure, symmetry breaking pattern, coupling constants, mass hierarchy, mixing angles, CP phases, and gravitational constant are all consequences of the geometry of one cell: the truncated octahedron.

---

*Priority Date: 20 February 2026 · UFFT Paper #59 · April 2026*

## References

[1] Luke Martin, *UFFT Paper #10, Lepton Mass Ratios*. DOI: 10.5281/zenodo.19063774.
[2] Luke Martin, *UFFT Paper #48, The Standard Model from One Matrix (v2)*. DOI: 10.5281/zenodo.19662029.
[3] Luke Martin, *UFFT Paper #50, Uniqueness of the Foam Cell (v2)*. DOI: 10.5281/zenodo.19662068.
[4] Luke Martin, *UFFT Paper #56, Torsion T1u Theorems*. DOI: 10.5281/zenodo.19484354.
[5] Luke Martin, *UFFT Paper #57, Necessity of the Standard Model (v2)*. DOI: 10.5281/zenodo.21323321.
[6] Luke Martin, *UFFT Paper #58, Gauge-Sector Placement (v2)*. DOI: 10.5281/zenodo.21323498.
[7] Luke Martin, *UFFT Paper #60, Four Closing Theorems*. DOI: 10.5281/zenodo.19491125.
[8] Luke Martin, *UFFT Paper #59, The Central Theorem (v1, superseded)*. DOI: 10.5281/zenodo.19491095.

*AI Disclosure: Numerical computations, proof structure verification and document composition performed with Claude (Anthropic). All theoretical arguments, physical identifications, and the axiom B+V=D: Luke Martin. The v3.0 withdrawal responds to an automated referee audit run by Prof. Pablo Moscato (University of Newcastle), 6 October 2026.*

**B + V = D**

*Unified Foam Field Theory · Paper #59 · DOI: 10.5281/zenodo.21323529 · Priority Date: 20 February 2026*

*B + V = D*
