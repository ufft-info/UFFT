# UFFT Paper #75 — The Born Rule from Imprint Statistics and the Entangled Pair State from the Antiunitary Twin Map

**Unified Foam Field Theory — Part LXXV**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | July 2026 |
| Series | Unified Foam Field Theory |
| Paper | #75 of 75 |
| Framework | v9 |
| Status | Draft — UNDER_REVIEW. Companion (Part II) to Paper #45 [DOI: 10.5281/zenodo.19307111]. |
| Tier | T75.1, T75.3, T75.4, T75.5, T75.6, T75.7: Tier 1 (exact; T75.6 conditional on R1/R2, T75.7 conditional on P-ISO/P-G). T75.2 (no-signalling forcing): Tier 2, conditional on Paper #45 §8. Result 75.8 (lattice-level existence): Tier 2, conditional on the corpus inter-cell void-hopping model. Named residual premises: R1 (equilibrated substrate, Paper #40), R2 (narrowband channel), P-ISO (orientation-averaged observables), P-G (gauge kernel unphysical). Open: the detector-coupling half of the bridge (lab routing coarse-grains to C). |
| DOI | 10.5281/zenodo.21323993 |
| Verification | verify_born_rule_imprint_2026-07-12.py (9 checks), verify_entanglement_twin_state_2026-07-12.py (15 checks), verify_pa_stationarity_2026-07-12.py (6 checks), verify_pe1_schur_uniqueness_2026-07-12.py (12 checks), verify_pe1_bridge_lattice_2026-07-12.py (8 checks), all green. |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, Born rule, measurement, entanglement, Bell, decoherence, antiunitary, Tsirelson bound, void channel

---

## Abstract

Paper #45 gave the foam two propagation channels: the wall channel (the face Laplacian L, local, causal) and the void channel (ηV, antipodal, non-local, no signalling). This paper supplies the two pieces of quantum mechanics that the corpus had until now imported rather than derived: the Born rule and the entangled pair state. First, the Born rule is reduced to two structural premises about the void-pair imprint event. Phase-blindness (the imprint probability depends only on a channel's amplitude modulus) and fine-graining additivity (a local refinement of detector channels cannot change coarse probabilities) force p_k = |c_k|² uniquely, by the Cauchy functional equation. Both premises are then discharged in turn. Fine-graining additivity is equivalent to no-signalling, which Paper #45 §8 derives from bulk incompressibility. Phase-blindness follows from substrate stationarity: a channel's phase is a time offset of its carrier, and no threshold functional driven by stationary substrate fluctuations can depend on a time offset; the same argument kills the linear response identically, so the trigger rate is quadratic in the amplitude at leading order. The Born exponent thus traces to two equation-of-state properties of the foam, incompressibility of the bulk and equilibration of the substrate. On a discrete substrate the counting measure is literal: channel k holds exactly N|c_k|² micro-quanta (Parseval). Second, the pair state of a displacement event is derived rather than selected. The twin map Θ = V∘K (antipodal map composed with conjugation, both existing corpus operators) is antiunitary and flips the torsion charge exactly. The pair state Σ_k |k⟩⊗Θ|k⟩ is proved basis-independent if and only if the twin map is antiunitary, which is the operator content of "opposite in every direction simultaneously". The resulting state is unique, maximally entangled, saturates the Tsirelson bound (CHSH = 2√2), carries exactly zero total torsion charge, and is one local unitary from the singlet of Paper #2. Third, the laboratory qubit is unique by symmetry: orientation-averaged observables commute with the cell's O_h action, Schur's lemma confines two-state structure to the two multiplicity-two sectors, the gauge pair is excluded, and the chiral doublet with routing observable C is all that remains. The η-tension between Papers #2 and #45 is also resolved: the void coupling scales the formation probability of entangled pairs (∝ η²) and never the strength of their correlations.

---

## 1. Introduction

The corpus has an objective collapse criterion (the first irreversible void-pair imprint) but until now no derivation of outcome statistics: every statement of the form "the correlations follow" (Paper #2 §4.2, Paper #45 §6) applied the standard quantum rule p = |amplitude|² at the last step. Likewise the singlet state of Paper #2 was selected by a symmetry desideratum rather than derived from the foam's operators. This paper closes both gaps to the extent the mathematics allows, and names exactly what remains assumed.

The mathematics of §3 is not new; it is the branch-additivity route associated with Everett and DeWitt, adjacent to Gleason's theorem, and the exclusion of non-Born exponents by signalling echoes observations of Aaronson. The basis-independence property of §5 is the standard pairing of maximally entangled states with antiunitary maps, and is the reason Wigner's theorem gives time reversal an antiunitary representation. What is UFFT's own: the counting measure is literal on a discrete substrate (§2), no-signalling is derived inside the framework rather than assumed (§4), and the twin map is composed from two operators already load-bearing elsewhere in the corpus (§5).

## 2. Charge counting on the discrete substrate (T75.1, Tier 1)

Let a displacement event be spread over M orthonormal detector channels, ψ = Σ_k c_k φ_k with Σ|c_k|² = 1, on a lattice of N faces. The channel charge is

Q_k = |⟨φ_k, ψ⟩|² = |c_k|²,   Σ_k Q_k = Q_total.   (1)

This is Parseval's identity, exact at any N. If the event's charge is carried by N_q substrate micro-quanta, channel k holds n_k = N_q|c_k|² of them. On a discrete substrate the statement "the number of micro-configurations available to channel k scales as |c_k|²" is therefore an identity, not a postulate. Continuum interpretations must postulate this measure; the foam gets it from discreteness.

## 3. The Born reduction (T75.3, Tier 1, conditional on P-A and P-B)

**Premise P-A (phase-blindness).** The imprint probability for channel k is a function of |c_k| alone. Physical reading: imprinting is a threshold energy conversion in a homogeneous substrate; torsion phases advance dynamically and the imprint event has no clock to read them.

**Premise P-B (fine-graining additivity).** If a channel is split unitarily into two sub-channels (an apparatus routing choice, not a change in the physics), the imprint probability of the parent equals the sum over the sub-channels.

**Theorem T75.3.** P-A and P-B imply p_k = |c_k|², uniquely.

*Proof.* P-A gives p_k = f(|c_k|). A unitary split c → (a, b) preserves charge, |a|² + |b|² = |c|², and P-B gives f(|c|) = f(|a|) + f(|b|). Substituting g(x) := f(√x) turns this into g(x + y) = g(x) + g(y) on charges. Monotone solutions of the Cauchy equation are linear, g(x) = x·g(1), and normalisation Σ_k p_k = 1 fixes g(1) = 1. Hence f(|c|) = |c|². ∎

Numerically, exponent 2 is additive under random unitary splits to 10⁻¹⁵ while exponents 1, 1.5, 3, 4 violate additivity at order one (script, section B). Because linear routing preserves coefficients exactly, channel-Born extends to every observable: measuring A is unitary routing of A's eigenmodes into disjoint imprint channels (script, section T).

## 4. No-signalling forces the exponent (T75.2, Tier 2 via Paper #45 §8)

Paper #45 §8 derives no-signalling from bulk incompressibility: the void channel has zero directed capacity because P = ρc² admits no propagating wave. That derived law makes P-B redundant rather than axiomatic.

Take the pair state √0.8·|0,0⟩ + √0.2·|1,1⟩ and an imprint rule p ∝ |c|ⁿ. If the near-side apparatus refines one local channel into two equal sub-channels, the far-side marginal shifts by 0.081 (n = 1), 0.035 (n = 1.5), 0.030 (n = 3), 0.029 (n = 4), and by exactly zero at n = 2 (script, section NS). A refinement is a strictly local choice, so any shift is a signal through the void channel, which the incompressible bulk forbids. Among modulus-only rules the bulk equation of state selects n = 2.

A structural lemma found in this audit: binary-against-binary measurement settings can never discriminate the exponent, because 2×2 unitarity forces both measurement columns to identical modulus profiles and the far-side marginal stays flat for every n. The discriminator is refinement freedom, which is P-B exercised as a physical no-signalling constraint.

### 4.1 Phase-blindness derived from substrate stationarity (T75.6)

P-A itself reduces to a stationarity property of the substrate. The observation that does the work: a channel's phase is a time offset and nothing else,

s(t) = |c| cos(ωt − φ) = s₀(t − φ/ω).   (1a)

**Theorem T75.6.** Let the imprint trigger be any threshold or first-passage functional of s(t) + ξ(t), where ξ is a stationary process independent of the signal, observed over full periods (or ωT ≫ 1). Then (i) the imprint probability is independent of φ, and (ii) the leading dependence on the amplitude is exactly quadratic.

*Proof.* (i) By (1a) a phase shift is a time translation of the signal; the stationary ensemble of ξ is invariant under time translations; therefore every statistic of s + ξ, including any first-passage probability, is invariant under φ. (ii) The linear term of the period-averaged trigger rate is proportional to the period average of s, which is zero; the first surviving term is quadratic in |c|. ∎

Numerically (script `verify_pa_stationarity_2026-07-12.py`, 6 checks): the period-averaged Rice rate is flat in φ to 10⁻¹⁷; the identical first-passage experiment with phase-locked (non-stationary) noise shows a 0.36 modulation where the stationary case is flat, so stationarity is the load-bearing property; the odd-in-signal response is zero to 10⁻¹⁸; the excess rate scales with log-log slope 2.016 in the weak-signal regime. The dynamics therefore realises the |c|² rule at leading order, and T75.3 with T75.2 forces exactness at all orders.

**What remains assumed.** Two residual premises, both weaker than P-A was: (R1) the substrate trigger process is stationary and not phase-locked to the mode, which is the equilibrated-foam property whose timescale Paper #40 [DOI: 10.5281/zenodo.19306543] establishes (a vacuum phase-locked to a laboratory mode would violate equilibration); (R2) the channel is narrowband, so that phase is a carrier time offset (exact in the monochromatic limit). The honest statement is now: the Born rule is the unique imprint statistics of an equilibrated substrate with an incompressible bulk.

## 5. The endpoint qubit and the twin map (T75.4, Tier 1)

The inter-type torsion operator T of Paper #39 [DOI: 10.5281/zenodo.19306447] gives the chirality operator C = T/(2i). Restricted to the T1u radial doublet (sq_x, hx_x), C is exactly a Pauli operator,

C|_doublet = −σ_y,  eigenvalues ±1,  chiral states (sq_x ∓ i·hx_x)/√2,   (2)

with no approximation (script E1). The endpoint of a displacement event carries this doublet as its two-state space.

The void address is the antipodal, conjugate image of the bubble address. Define the twin map

Θ = V ∘ K,   (3)

with V the antipodal map of Paper #45 and K complex conjugation. On the doublet V = −I (T1u is antipodal-odd), K C K = −C exactly (C is purely imaginary Hermitian), and [V, C] = 0, so

Θ C Θ⁻¹ = −C.   (4)

The twin carries the opposite torsion charge. Θ is antiunitary. Both component operators are already load-bearing in the corpus; nothing is introduced.

## 6. The twin-state theorem (T75.5, Tier 1)

**Theorem T75.5 (basis-independence).** For a twin map Θ = UK with U unitary, the pair state

|D⟩ = (1/√2) Σ_k |f_k⟩ ⊗ Θ|f_k⟩   (5)

is the same state for every orthonormal basis {f_k}. For a unitary twin map (no conjugation) the state depends on the basis.

*Proof.* Write pair states as matrices, |ψ⟩ = Σ_ij M_ij |i⟩⊗|j⟩. The (i, j) component of Σ_k |f_k⟩⊗UK|f_k⟩ is Σ_l U_jl Σ_k (f_k)_i (f_k)_l* = Σ_l U_jl δ_il = U_ji, by completeness of the basis. So M = Uᵀ regardless of the basis. For a unitary twin the inner sum is Σ_k (f_k)_i (f_k)_l, which is not δ_il for complex bases, and the state varies. ∎

The consistency condition "the void mirrors the bubble in every direction simultaneously" is therefore satisfiable by an antiunitary twin and by nothing else, and given Θ the pair state is unique. Numerically: invariant to 2×10⁻¹⁶ over 300 random bases for Θ, deviations of order one for a unitary twin (script E3).

**Corollaries (all exact, script E4/E5).**

(a) *Maximal entanglement.* M = Uᵀ is proportional to a unitary matrix, so the Schmidt coefficients are (1/√2, 1/√2).

(b) *Zero pair torsion.* On the doublet Θ = −K, so M ∝ I, and (C⊗I + I⊗C) acts on M as c₂M + Mc₂ᵀ = −(σ_y + σ_yᵀ)/√2 = 0, since σ_y is antisymmetric. The pair carries exactly zero total torsion charge, the pair-level form of the Total Torsion Identity of Paper #40 [DOI: 10.5281/zenodo.19306543].

(c) *Tsirelson saturation.* The correlation matrix is diag(+1, −1, +1); its two largest singular values give CHSH = 2√2 by the Horodecki criterion, the quantum maximum.

(d) *Local singlet equivalence.* With ε the antisymmetric 2×2 matrix, u = −ε is unitary and maps M ∝ I to the singlet matrix ∝ ε. Paper #2's singlet is the twin state in a local convention.

**Scope-down of Paper #2 §4.1.** The twin state anti-correlates the chirality (E = −1) and correlates the two quadratures (E = +1). The claim "anti-correlated in every measurement direction" is exact only after the local rotation of corollary (d). No Bell-experimental content changes, since local unitaries preserve all CHSH statistics, but the prose of Paper #2 §4.1 is stronger than the geometry and will be scoped down at that record's next revision (a correction note per the corpus corrections protocol).

Combining T75.5 with §3, the measured statistics of the twin state are |E(a, b)| = |cos θ| with CHSH = 2√2 at optimal settings (script E7). With T75.6 discharging phase-blindness and T75.7 below fixing the qubit, every step is foam-internal up to the four residual premises named in the header.

### 6.1 Schur uniqueness of the laboratory qubit (T75.7)

The identification of the measured qubit with the chiral doublet is itself forced, up to one bridge premise. The physical input: laboratory apparatus does not resolve Planck-cell orientation, so effective observables are averaged over cell orientations and therefore commute with the O_h action on the face space (premise P-ISO).

**Theorem T75.7.** The commutant of the 14-face permutation representation of O_h has complex dimension Σmᵢ² = 11 (multiplicities A1g:2, Eg:1, T1u:2, A2u:1, T2g:1). Its Θ-odd (purely imaginary Hermitian) part is exactly two-dimensional, and both generators are blocks of the single corpus operator C = T/(2i): one on the A1g radial pair (eigenvalues ±√3), one on the T1u radial pair (eigenvalues ±1). Every multiplicity-one sector (Eg, T2g, A2u) admits only scalar equivariant observables: no two-state system can be routed there at all. (The corpus Tier-1 result "torsion annihilates Eg" is an instance of this Schur exclusion.)

*Proof structure.* V represents the central inversion of O_h, so V = ±I on each irrep block and Θ = V∘K flips exactly the imaginary Hermitian operators; Schur's lemma reduces the equivariant algebra to M_{mᵢ}(C) per isotypic sector; imaginary Hermitian content exists only where mᵢ ≥ 2, and the face space has exactly two such sectors. Verified by explicit group closure (48 elements), commutant nullspace (dimension 11), and exhaustion of the imaginary-Hermitian subspace (dimension 2). ∎

The A1g pair is excluded physically: it contains the Laplacian kernel, the corpus's U(1) gauge direction (premise P-G, already load-bearing in the QED emergence), and it is maximally split (λ = 0 versus 7, the full spectral width). The unique surviving two-state system is the T1u radial (chiral) doublet, and the unique Θ-odd routing observable on it is C, the operator of equation (2).

**What this does and does not establish.** Uniqueness is derived: under P-ISO and P-G, if a Bell experiment routes on any foam two-state system, that system is the chiral doublet and the routed observable is C. Existence splits into two halves, and the first is closed below.

### 6.2 Lattice-level existence of the qubit (Result 75.8, Tier 2)

In the corpus's own inter-cell model (the void-hopping Bloch Hamiltonian H(k) = L + diag(η_f) − X(k) of the Papers #45/#48 machinery), the chiral doublet is a bulk band degree of freedom, not a single-cell abstraction. Verified over the Brillouin zone (script `verify_pe1_bridge_lattice_2026-07-12.py`):

- The six-dimensional T1u span (radial doublet × three angular copies) is exactly invariant under the intra-cell dynamics; the only leakage channel is the void hopping, bounded by η (measured maximum 0.0863 = η_hx).
- The six Bloch bands connected to the T1u sector stay aligned with the cell's T1u span with principal-angle fidelity ≥ 0.985 (1 − O(η²)) and remain separated from the other eight bands by an open gap (minimum 0.286) at every sampled k: the qubit subspace is gap-protected across the zone.
- The band-projected chirality has spectrum ±1 (threefold each) within 0.019 = O(η²) everywhere: the routing observable survives transport.
- The bands disperse (width 0.139, O(η)): the qubit propagates cell to cell through the void channel.
- Consistency: the face-type off-diagonal of L on the (hex, sq) doublet is exactly −2σ_x, reproducing Paper #72 T72.3a [DOI: 10.5281/zenodo.19658759], whose multiplicity count (2 × 3 = chirality partners × generations) is the continuum-side face of the same structure. Paper #72's physical left/right labelling (T72.3b) remains a conjecture there and is not used here.

The second half of existence, that a laboratory detector's routing coupling coarse-grains to C, is a detector-modelling problem in the Paper #59 lattice-to-continuum programme and remains the named open item of this paper.

## 7. The η-tension of Papers #2 and #45 resolved (Tier 1 within the model of §7)

Paper #45 presents entanglement as an O(η) void correction; experiment shows full-strength correlations. Both are correct about different quantities. In an exactly diagonalised vacuum-pair model with void coupling η sourcing the twin state, the formation probability of the pair scales as η² (with corrections of order η², 3% at η = 0.1), while the normalised pair state and all of its correlations are independent of η to machine precision (script E6).

The void coupling suppresses the amplitude of entanglement, never its strength. Entanglement is rare and fragile because formation and decoherence scale with η; a formed pair is maximally correlated because the correlations are kinematic properties of the unique twin state.

## 8. Verification

All claims trace to five scripts in `verification/` on the repository:

- `verify_born_rule_imprint_2026-07-12.py`: Parseval counting (L1), fine-graining uniqueness (B), no-signalling forcing and the binary-cancellation lemma (NS), stochastic imprint realisation with χ² = 2.2 at dof 3 and sequential singlet imprinting reproducing E(a, b) = −cos θ (S), basis transport (T). 9 checks, all green.
- `verify_entanglement_twin_state_2026-07-12.py`: endpoint qubit exactness (E1), twin map properties (E2), basis-independence both ways (E3), zero pair torsion (E4), Schmidt/Tsirelson/local equivalence and the correlation signs (E5), η-independence of correlations and η² formation scaling (E6), end-to-end Bell statistics through the imprint rule (E7). 15 checks, all green.
- `verify_pa_stationarity_2026-07-12.py`: period-averaged rate flat in phase to 10⁻¹⁷ (PA1), stationary-versus-phase-locked first-passage contrast (PA2), vanishing linear response and log-log slope 2.016 (PA3), channel competition reproducing Born (PA4). 6 checks, all green.
- `verify_pe1_schur_uniqueness_2026-07-12.py`: O_h closure on the face space (48 elements) and commutant dimension 11 (Q1), V central and Θ-odd = imaginary Hermitian on the equivariant algebra (Q2), imaginary-Hermitian equivariant space exactly two-dimensional with both generators blocks of C, multiplicity-one sectors scalar (Q3), gauge-kernel membership and maximal splitting of the A1g pair (Q4). 12 checks, all green.
- `verify_pe1_bridge_lattice_2026-07-12.py`: exact intra-cell invariance and the η leakage bound (BL1), band-subspace fidelity ≥ 0.985 and open gap 0.286 across the zone (BL2), band-projected chirality ±1 within 0.019 (BL3), band dispersion 0.139 (BL4), Paper #72 T72.3a reproduced (BL5). 8 checks, all green.

## 9. Conclusion

The Born rule is no longer a postulate and no longer rests on a bespoke premise. Its exponent is fixed three times over: by fine-graining consistency, by the framework's own no-signalling law, and dynamically by the vanishing of the linear response under stationary triggering. Phase-blindness itself is a theorem of time-translation invariance, so p = |c|² traces to two equation-of-state properties of the foam: the bulk is incompressible (P = ρc², no signalling) and the substrate is equilibrated (stationary, no phase-locking). The entangled pair state of Paper #2 is no longer selected; it is the unique basis-independent state of an antiunitary twin map composed from the corpus's antipodal and conjugation operators, and it saturates the Tsirelson bound with zero total torsion charge. The laboratory qubit is no longer a bald identification: Schur's lemma leaves the foam exactly one routable two-state system once the gauge pair is excluded, the chiral doublet with observable C, and in the corpus's own inter-cell model that doublet is a gap-protected, propagating band degree of freedom whose routing observable survives transport with O(η²) corrections. What remains open is the final step of the bridge: showing that a real detector's routing coupling coarse-grains to C in the continuum limit, a detector-modelling problem in the Paper #59 programme. The residual premises (R1 equilibrated substrate, R2 narrowband, P-ISO orientation averaging, P-G gauge exclusion, and the inter-cell model of Result 75.8) are each corpus-native or exact in a stated limit.

---

## References

### UFFT Papers
- [1] Paper #2 — Void-Pair Conservation as the Physical Mechanism of Quantum Entanglement and Bell Correlations. DOI: 10.5281/zenodo.18706806
- [2] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [3] Paper #16 — The Master Equation. DOI: 10.5281/zenodo.19064359
- [4] Paper #39 — The Inter-Type Torsion Operator. DOI: 10.5281/zenodo.19306447
- [5] Paper #40 — Total Torsion Identity and Foam Equilibration Timescale. DOI: 10.5281/zenodo.19306543
- [6] Paper #45 — The Void Channel: Entanglement from the Antipodal Map. DOI: 10.5281/zenodo.19307111
- [7] Paper #48 — The Standard Model from One Matrix (v2). DOI: 10.5281/zenodo.19662029
- [8] Paper #72 — Dirac Operator, Generation Count, Chirality Structure, and the m₃ Integer. DOI: 10.5281/zenodo.19658759

### External References
- [9] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195-200.
- [10] Gleason, A. M. (1957). Measures on the closed subspaces of a Hilbert space. *Journal of Mathematics and Mechanics*, 6(6), 885-893.
- [11] Everett, H. (1957). "Relative state" formulation of quantum mechanics. *Reviews of Modern Physics*, 29(3), 454-462.
- [12] Zurek, W. H. (2005). Probabilities from entanglement, Born's rule from envariance. *Physical Review A*, 71, 052105.
- [13] Wigner, E. P. (1931). *Gruppentheorie und ihre Anwendung auf die Quantenmechanik der Atomspektren.* Vieweg, Braunschweig.
- [14] Cirel'son, B. S. (1980). Quantum generalizations of Bell's inequality. *Letters in Mathematical Physics*, 4, 93-100.
- [15] Horodecki, R., Horodecki, P., & Horodecki, M. (1995). Violating Bell inequality by mixed spin-1/2 states. *Physics Letters A*, 200, 340-344.
- [16] Aaronson, S. (2004). Is quantum mechanics an island in theoryspace? *Proceedings of the Växjö Conference on Quantum Theory* (arXiv:quant-ph/0401062).

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Paper #75 · DOI 10.5281/zenodo.21323993 · Priority Date: 20 February 2026*

*B + V = D*
