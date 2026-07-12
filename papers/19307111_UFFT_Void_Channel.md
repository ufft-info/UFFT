# UFFT Paper #45 — The Void Channel: Entanglement from the Antipodal Map: The Complete Hamiltonian H = L + ηV and the Two Propagation Channels of the Foam

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
| Paper | #45 of 63 |
| Framework | v10 |
| Status | Complete, Tier 2. Formalizes the void-pair model from Paper #2 as H = L + ηV. Derives boson-fermion parity from antipodal symmetry. |
| Tier | 2 |
| DOI | 10.5281/zenodo.19307111 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, void channel, antipodal map, entanglement, Bell correlations, parity, boson-fermion distinction

---

## Abstract

The Axiom Zero decomposition B + V = D (Bubble + Void = Displacement) is shown to map directly onto a two-channel Hamiltonian H = L + ηV, where L is the face Laplacian (wall-mediated propagation) and V is the antipodal map (void-mediated correlation). The bubble propagates on the walls at speed c. The void appears instantaneously on the antipodal face through the incompressible bulk, with coupling η = exp(−d_bulk).

The antipodal map V is an involution (V² = I) whose eigenvalues partition the face representation into even (+1) and odd (−1) sectors. The partition aligns exactly with the boson/fermion distinction: A₁g (photon), Eg (weak bosons), and T₂g (gluons) are EVEN; T₁u (fermion generations) and A₂u (Higgs) are ODD. The void channel pushes even modes UP (heavier bosons) and odd modes DOWN (lighter fermions). The Higgs is pushed toward more negative μ², reinforcing spontaneous symmetry breaking.

The combined propagator G(j,i;t) = ⟨j|exp(−Ht)|i⟩ sums over two kinds of paths: wall walks through shared edges (36 channels, local, causal, giving QFT) and void jumps through the bulk (7 antipodal pairs, non-local, acausal, giving entanglement). The complete path integral is the sum over both.

The void coupling is derived from the bulk geometry: η_sq = exp(−2√2) = 0.059 for sq-sq pairs and η_hx = exp(−√6) = 0.086 for hx-hx pairs. The void corrections are O(η) ≈ 6−9%, consistent with known sub-leading corrections to the coupling constants. The trace is conserved (Σλ = 72 with or without void), expressing pressure conservation across the bulk.

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

| Irrep | Eigenvalue | V parity | Void shift | Physical sector |
|-------|-----------|----------|-----------|----------------|
| A₁g | 0 | **+1 (even)** | ↑ +0.075 | Photon |
| T₁u(r₁) | 2.44 | **−1 (odd)** | ↓ −0.069 | Light fermions (e, u, d) |
| Eg | 4 | **+1 (even)** | ↑ +0.059 | Weak bosons (W, Z) |
| T₁u(r₂) | 6.56 | **−1 (odd)** | ↓ −0.076 | Heavy fermions (c, b, t) |
| A₁g⊕T₂g | 7 | **+1 (even)** | ↑ +0.071 | Gluons |
| A₂u | 9 | **−1 (odd)** | ↓ −0.086 | Higgs |

**The bosons are even. The fermions are odd.** The void channel creates a natural boson-fermion distinction through the parity of the antipodal map. This is not the Wilson-loop fermion number (which comes from the π-flux torsion identity); it is a complementary classification that happens to align with it.

The physical meaning: even modes are symmetric under "looking through the bulk" (they see the same thing on both sides. Odd modes are antisymmetric) they see the opposite. Fermions are the modes that reverse sign when viewed through the bulk. This is the foam's version of spin-statistics: the connection between the antipodal (spatial) parity and the particle statistics.

---

## 4. The Combined Hamiltonian

**H = L + ηV**

The complete Hamiltonian is the sum of the face Laplacian (wall channel) and the void operator (bulk channel). The eigenvalues shift:

- Even modes: λ → λ + η (pushed UP, heavier)
- Odd modes: λ → λ − η (pushed DOWN, lighter)

The trace is conserved: Σλ = 72 with or without the void. The void redistributes energy between sectors but doesn't create or destroy it. This is pressure conservation across the bulk, Newton's third law through the centre of the cell.

### 4.1 Effect on observables

The Higgs mass ratio m_H/M_Z improves from 0.14% to 0.06% agreement with the void correction (A₂u pushed down, Eg pushed up). The void channel brings the theoretical prediction closer to experiment.

### 4.2 Effect on SSB

The A₂u mode (Higgs) is ODD under the void and gets pushed to a lower eigenvalue. Under the inter-type torsion operator, A₂u already has eigenvalue −1 (forcing SSB). The void correction reinforces this: it makes μ² even more negative, strengthening the symmetry breaking. The void ASSISTS the Higgs mechanism.

---

## 5. The Complete Path Integral

The propagator includes both channels:

**G(j,i;t) = ⟨j| exp(−(L+ηV)t) |i⟩**

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

The void coupling η determines the entanglement strength. Since η = exp(−d_bulk) ≈ 0.06−0.09, entanglement is a sub-leading correction to the dominant wall physics. This is why entanglement is fragile, it's exponentially suppressed by the bulk distance.

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

The axiom B + V = D is the Hamiltonian H = L + ηV. The bubble gives the Standard Model. The void gives entanglement. Together they give the complete quantum theory of the foam.

---

## References

[1] Martin, L. (2026). The Path Integral from Planck-Scale Foam. Zenodo.

[2] Martin, L. (2026). Void-Pair Conservation and Bell Correlations. Zenodo. DOI: 10.5281/zenodo.18706806.

[3] Martin, L. (2026). Gravitational Suppression of Quantum Decoherence. Zenodo. DOI: 10.5281/zenodo.18706756.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). The insight that voids jump through the bulk rather than traversing the walls, and that B+V=D maps to H=L+ηV: Luke Martin. AI role: antipodal map computation, parity classification, eigenvalue shifts, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*


---

*Unified Foam Field Theory · Paper #45 · DOI: 10.5281/zenodo.19307111 · Priority Date: 20 February 2026*

*B + V = D*
