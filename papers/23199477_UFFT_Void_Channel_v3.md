# UFFT Paper #45 — The Void Channel: Entanglement from the Antipodal Map: The Lattice Hamiltonian H = L + η(I − V) and the Two Propagation Channels of the Foam

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | March 2026 (v2.0: July 2026; v3.0: October 2026) |
| Series | Unified Foam Field Theory |
| Paper | #45 of 75 |
| Framework | v10 |
| Version | 3.0 |
| Status | Complete, Tier 2. Formalizes the void-pair model from Paper #2 as the lattice operator H = L + η(I − V). Derives boson-fermion parity from antipodal symmetry. v3.0 corrects the sign of the void term, withdraws the Higgs 0.06% claim, and records the void-protection theorem. |
| Tier | 2 |
| DOI | 10.5281/zenodo.23199477 (v3.0; v2: 10.5281/zenodo.21331511; v1: 10.5281/zenodo.19307111) |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, void channel, antipodal map, entanglement, Bell correlations, parity, boson-fermion distinction

---

## Abstract

The Axiom Zero decomposition B + V = D (Bubble + Void = Displacement) is shown to map directly onto a two-channel lattice Hamiltonian H = L + η(I − V), where L is the face Laplacian (wall-mediated propagation) and V is the antipodal partner-face map (void-mediated correlation). The bubble propagates on the walls at speed c. The void appears instantaneously on the antipodal face through the incompressible bulk, with coupling η = exp(−d_bulk).

The antipodal map V is an involution (V² = I) whose eigenvalues partition the face representation into even (+1) and odd (−1) sectors. The partition aligns exactly with the boson/fermion distinction: A₁g (photon), Eg (weak bosons), and T₂g (gluons) are EVEN; T₁u (fermion generations) and A₂u (Higgs) are ODD. In the operative (I − V) form the void term annihilates the even sector at the zone centre and shifts the odd sector by 2η there; at the zone face-centres and corner the single-cell odd eigenvalues are exact for any η (void-protection theorem). The earlier statement that odd modes are pushed down and that this reinforces symmetry breaking is withdrawn in v3.0.

The combined propagator G(j,i;t) = ⟨j|exp(−Ht)|i⟩ sums over two kinds of paths: wall walks through shared edges (36 channels, local, causal, giving QFT) and void jumps through the bulk (7 antipodal pairs, non-local, acausal, giving entanglement). The complete path integral is the sum over both.

The void coupling is taken from the bulk geometry (Tier 2, physically motivated form): η_sq = exp(−2√2) = 0.059 for sq-sq pairs and η_hx = exp(−√6) = 0.086 for hx-hx pairs. The void corrections are O(η) ≈ 6−9%, consistent with known sub-leading corrections to the coupling constants. The trace of L is 72; the void term adds 2η per odd mode at the zone centre and nothing at the protected points.

---

## Changes in this version (3.0)

1. **Sign of the void term (substantive).** v1.0 and v2.0 wrote the Hamiltonian as H = L + ηV. Every lattice verification script in the repository since July 2026 (`verify_void_protection_2026-07-03.py`, `verify_pe1_bridge_lattice_2026-07-12.py`, the ml3 family) uses H(q) = L + η(I − V(q)), which is the B + V = D form: it annihilates the uniform A₁g mode for every η (the photon stays massless) and it is the form under which the void-protection theorem holds. The (I − V) form is now stated throughout. The table in §3 and the shifts in §4 are rewritten accordingly.
2. **Higgs claim withdrawn (§4.1).** The statement that m_H/M_Z improves from 0.14% to 0.06% via a factor (1 + η_hx/9) is withdrawn. The arithmetic was wrong (18/(9+√17) × (1 + η_hx/9) = 1.3848, 0.8% from the observed 1.3735), and under the operative operator the A₂u level is exact at the zone corner for any η, so there is no void correction to the Higgs level. The leading-order ratio 18/(9+√17) = 1.3716 (125.08 GeV, −1.0σ) stands.
3. **Void-protection theorem recorded (§4.3, new).** The single-cell eigenvalues are exact eigenvalues of the foam at specific zone points independently of η_sq and η_hx.
4. **SSB statement revised (§4.2).** The void does not drive SSB; the A₂u identification rests on the inter-type torsion operator alone (Tier 2).
5. Header, abstract and §5 updated to the (I − V) form. Sections 1, 2, 6 and 7 unchanged from v2.0.

## Changes in version 2.0

1. **Section 6 correction (the only substantive change).** The v1.0 sentence "The void coupling η determines the entanglement strength" named the wrong quantity. Paper #75 [DOI: 10.5281/zenodo.21323993] derives the twin state and shows η scales the FORMATION probability of entangled pairs (∝ η²) and the fragility of the channel, never the correlation strength of a formed pair, which is kinematic and maximal (Tsirelson-saturating, CHSH = 2√2). Section 6 is corrected accordingly; the fragility claim of v1.0 stands.
2. Reference [4] (Paper #75) added.
3. Header updated to v2.0. No other content changes.

---

## 1. The Two Channels of Axiom Zero

Axiom Zero states: B + V = D. Every displacement D creates a bubble B (a pressure increase at position x) and a void V (a pressure decrease at position x'). These propagate differently:

- **The Bubble** propagates on the cell walls, face to face through shared edges, weighted by torsion phases. This is the face Laplacian L. It gives the Standard Model: forces, particles, coupling constants, mass spectrum. Speed: c. Local. Causal.

- **The Void** appears on the antipodal face of the same cell (the face with opposite normal direction, on the far side of the incompressible bulk. The bulk transmits no waves (P = ρc², infinite stiffness), but the pressure conservation law requires the void to appear. No traversal) instantaneous pair creation. Non-local. Acausal (but no information transfer).

---

## 2. The Antipodal Map

### 2.1 Definition

The truncated octahedron has 7 antipodal pairs: each face i has a unique face ī with normal n̂_ī = −n̂_i. The antipodal map V is:

**V_ij = η(i) × δ_{j,ī}**

where η(i) = exp(−d_i) is the void coupling and d_i is the geometric distance from face i to its antipodal face through the cell centre.

### 2.2 Properties

V² = I (involution: two void jumps return to start). The eigenvalues of V are ±1, partitioning the face representation into even and odd sectors.

### 2.3 The 7 antipodal pairs

| Pair | Face types | Adjacent? | Graph distance | η |
|------|-----------|-----------|---------------|---|
| 0 ↔ 1 | sq ↔ sq | No | 3 | exp(−2√2) = 0.059 |
| 2 ↔ 3 | sq ↔ sq | No | 3 | 0.059 |
| 4 ↔ 5 | sq ↔ sq | No | 3 | 0.059 |
| 6 ↔ 13 | hx ↔ hx | No | 3 | exp(−√6) = 0.086 |
| 7 ↔ 12 | hx ↔ hx | No | 3 | 0.086 |
| 8 ↔ 11 | hx ↔ hx | No | 3 | 0.086 |
| 9 ↔ 10 | hx ↔ hx | No | 3 | 0.086 |

Antipodal faces are NEVER adjacent on the face graph. The void jump connects faces that require 3 wall steps to reach. It is a shortcut through the bulk.

---

## 3. The Parity Partition: Bosons Are Even, Fermions Are Odd

Each irrep of the face Laplacian has definite parity under the antipodal map:

| Irrep | Eigenvalue | V parity | Zone-centre shift, H = L + η(I − V) | Protected point (exact, any η) | Physical sector |
|-------|-----------|----------|-------------------------------------|-------------------------------|----------------|
| A₁g | 0 | **+1 (even)** | 0 (zero mode preserved) | zone centre | Photon |
| T₁u(r₁) | 2.44 | **−1 (odd)** | +2η (mixed sq/hx, +0.139) | zone face-centres | Light fermions (e, u, d) |
| Eg | 4 | **+1 (even)** | 0 | zone centre | Weak bosons (W, Z) |
| T₁u(r₂) | 6.56 | **−1 (odd)** | +2η (mixed sq/hx, +0.152) | zone face-centres | Heavy fermions (c, b, t) |
| A₁g⊕T₂g | 7 | **+1 (even)** | 0 | zone centre | Gluons |
| A₂u | 9 | **−1 (odd)** | +2η_hx (+0.173) | zone corner | Higgs |

**The bosons are even. The fermions are odd.** The void channel creates a natural boson-fermion distinction through the parity of the antipodal map. This is not the Wilson-loop fermion number (which comes from the π-flux torsion identity); it is a complementary classification that happens to align with it.

The physical meaning: even modes are symmetric under "looking through the bulk" (they see the same thing on both sides. Odd modes are antisymmetric) they see the opposite. Fermions are the modes that reverse sign when viewed through the bulk. This is the foam's version of spin-statistics: the connection between the antipodal (spatial) parity and the particle statistics.

---

## 4. The Combined Hamiltonian

**H(q) = L + η(I − V(q))**

The lattice Hamiltonian is the face Laplacian (wall channel) plus the void term η(I − V(q)), where V(q) maps each face to its antipodal partner in the neighbouring cell with the Bloch phase e^{iq·R_f} and η = diag(η_sq, η_hx) by face type. This is the B + V = D form: a displacement on a face and the matching void on its partner enter as the difference ψ_f − ψ_f̄, so a pattern equal on both sides of every wall (the pair-even sector) costs nothing. At the zone centre:

- Even modes (V = +1): unshifted. The uniform A₁g mode remains an exact zero mode for every η: the photon is massless.
- Odd modes (V = −1): shifted up by 2η (2η_sq on square content, 2η_hx on hexagon content).

The earlier form H = L + ηV, with even modes up and odd modes down and trace conserved, is superseded; it lifts the zero mode (A₁g → 0.075) and is not the operator used in any verification script.

### 4.1 Effect on observables

Withdrawn. See "Changes in this version", item 2. Under the operative operator the Higgs level is void-protected (§4.3) and carries no correction; the leading-order m_H/M_Z = 18/(9+√17) stands at −1.0σ.

### 4.2 Effect on SSB

The A₂u mode is odd under the void. The identification of its T_hex charge −1 under the inter-type torsion operator with the sign of μ² is unchanged and is a Tier 2 identification. The void does not drive it: at the protected zone corner the A₂u level is exactly 9 for any η, and at the zone centre it moves up, not down.

### 4.3 The void-protection theorem

(`verification/verify_void_protection_2026-07-03.py`, five checks, one symbolic in η_sq, η_hx.) At a zone face-centre q* = π e_axis the Bloch phases are ±1 and the void coefficient on face f is η_f(1 + φ_f). The pure-L T₁u eigenvector at r₁, in the polarisation transverse to the axis, is supported exactly on the φ = −1 faces, so H(q*) v = L v = r₁ v identically in η. The same holds for r₂ at the same point, for the even levels 0, 4, 7 at the zone centre, and for A₂u = 9 at the zone corner q = π(1,1,1). The single-cell spectrum {0, r₁, 4, r₂, 7, 9}, with √17 = r₂ − r₁, r₁ + r₂ = 9 and r₁r₂ = 16, is therefore a property of the foam at its protected points, not of an isolated cell, and every pure-cell formula in the corpus is protected against void corrections to all orders in η.

---

## 5. The Complete Path Integral

The propagator includes both channels:

**G(j,i;t) = ⟨j| exp(−(L + η(I − V))t) |i⟩**

Expanding in powers of η:

G = G_wall + η × G_void + η² × G_void² + ...

where G_wall = ⟨j|e^{−Lt}|i⟩ sums over wall walks (Paper 42), and the void corrections add paths that include bulk jumps.

A general path consists of k wall steps and m void jumps:

**G(j,i;k,m) = Σ_{paths with k walls, m voids} (Π wall phases) × η^m**

The wall paths give QFT (Feynman rules, propagators, vertices). The void jumps give entanglement corrections (Bell correlations, non-local correlations). Both are part of the same path integral over the same cell.

---

## 6. Entanglement as Void-Pair Correlation

When face i is displaced (B at face i), the void appears at antipodal face ī. If ī is in a NEIGHBOURING cell on the BCC lattice, the correlation is non-local: measuring the displacement at face i immediately constrains the state at face ī in the adjacent cell.

This is entanglement. The void pair (B, V) are two addresses of one displacement event D. They are not two separate particles communicating faster than light, they are one event seen from two faces. Bell's factorisation assumption fails because D is inherently non-local: it cannot be written as a product of functions at i and ī separately.

The void coupling η sets how OFTEN entanglement forms, not how strong it is. Pair formation scales as η² and the channel's robustness against scrambling scales with η, while the correlation strength of a formed pair is kinematic and maximal: the twin state saturates the Tsirelson bound (CHSH = 2√2) regardless of η [4]. Since η = exp(−d_bulk) ≈ 0.06−0.09, entangled pairs are rare and fragile, exponentially suppressed by the bulk distance, but always full strength when they form.

---

## 7. Decoherence from Void Scrambling

In a dense environment (many displacements, many cells involved), each displacement creates its own void pair. The voids from different events overlap and interfere, scrambling the individual correlations. This is decoherence, not wavefunction collapse, but loss of specific void-pair correlations in the noise of many overlapping pairs.

Near a massive object (higher foam density, more cells per unit volume): more displacement events → more void pairs → more scrambling → FASTER decoherence? No, the opposite. Higher density means the cells are more tightly packed, which means each void pair is MORE constrained by its neighbours. The constraints REDUCE the scrambling. Gravity SUPPRESSES decoherence.

This is the opposite prediction to Diósi-Penrose (which predicts gravity enhances decoherence). It is the specific, testable UFFT prediction from the void channel physics.

---

## 8. Why Entanglement Cannot Signal

The void channel is non-local but cannot transmit information, for a precise physical reason: the bulk is incompressible (P = ρc²). No wave propagates through it. The void appears because of pressure conservation, not because a signal was sent. The correlation is a CONSTRAINT (B + V = D must hold globally), not a COMMUNICATION (no energy flows through the bulk).

In information-theoretic terms: the void channel has zero capacity for directed information transfer, but nonzero capacity for correlation. This is exactly the no-signalling theorem of quantum mechanics, derived from the equation of state of the bulk.

---

## 9. Summary

| | Wall Channel (L) | Void Channel (V) |
|---|---|---|
| Medium | Cell walls (faces, edges) | Cell bulk (incompressible) |
| Operator | Face Laplacian | Antipodal map |
| Speed | c (1 cell/t_P) | Instantaneous (pair creation) |
| Coupling | Torsion phases e^{iθ} | η = exp(−d_bulk) ≈ 0.06−0.09 |
| Channels | 36 edges | 7 antipodal pairs |
| Locality | Local, causal | Non-local, acausal |
| Physics | Forces, particles, QFT | Entanglement, Bell correlations |
| Information | Can signal | Cannot signal (incompressible bulk) |
| Eigenvalue effect | Sets the spectrum | Shifts: even ↑, odd ↓ |
| Parity | — | Bosons even, fermions odd |

The axiom B + V = D is the lattice Hamiltonian H = L + η(I − V). The bubble gives the Standard Model. The void gives entanglement. Together they give the complete quantum theory of the foam.

---

## References

[1] Martin, L. (2026). The Path Integral from Planck-Scale Foam. Zenodo.

[2] Martin, L. (2026). Void-Pair Conservation and Bell Correlations. Zenodo. DOI: 10.5281/zenodo.18706806.

[3] Martin, L. (2026). Gravitational Suppression of Quantum Decoherence. Zenodo. DOI: 10.5281/zenodo.18706756.

[4] Martin, L. (2026). UFFT Paper #75, The Twin State: Entanglement and the Born Rule from B + V = D. Zenodo. DOI: 10.5281/zenodo.21323993.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). The insight that voids jump through the bulk rather than traversing the walls, and that B+V=D maps to H=L+ηV: Luke Martin. AI role: antipodal map computation, parity classification, eigenvalue shifts, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*


---

*Unified Foam Field Theory · Paper #45 · v2.0 DOI: 10.5281/zenodo.21331511 (v1: 10.5281/zenodo.19307111) · Priority Date: 20 February 2026*

*B + V = D*
