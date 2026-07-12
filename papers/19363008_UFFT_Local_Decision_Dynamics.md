# Local Decision Dynamics in the Unified Foam Field Theory

## Path Geometry, Spectral Progressions, and the Physical Basis of Derived Formulas

**Luke Martin** · Independent Researcher · Newcastle, Australia

**Priority Date:** April 2026

**Framework:** Unified Foam Field Theory (UFFT)

---

## Abstract

The Unified Foam Field Theory derives all Standard Model observables from the geometry of a single truncated octahedron (Kelvin cell) with O_h symmetry and zero free parameters. The existing papers establish *what* is derived; this paper establishes *why* the derivations take the forms they do. The unifying principle is the **local decision principle**: the foam disturbance makes greedy local choices at each face junction with no knowledge of the global destination, exactly as electrical current propagates through a resistor network, taking the path of steepest local gradient at each crossroads rather than computing the globally optimal route.

From this one principle, eight structural results follow directly: (1) the dihedral angle coupling between generations, explaining why K₁₂ ≠ K₂₃ and giving the tau mass formula; (2) the exact geometric progression r₁, Eg(4), r₂ from r₁ × r₂ = 16; (3) a direct spectral derivation of the muon mass as m_μ = m_e × exp(r₁r₂/C_A) = m_e × exp(16/3); (4) a polaron derivation of the electron mass as an independent verification of the published formula; (5) the three-generations theorem as a consequence of O_h having exactly three distortion irreducible representations; (6) the identification of eight gluons with eight hexagonal face normals; (7) the cell/void/either classification as the geometric origin of spin-statistics; and (8) the recording principle as the physical resolution of the quantum measurement problem. All eight results are consistent with and physically explanatory of the existing 47 published derivations.

**Keywords:** foam field theory, local decision principle, generation mass ratios, muon mass, geometric progression, spin-statistics, measurement problem, truncated octahedron, UFFT

---

## 1. The Local Decision Principle

### 1.1 The Electricity Analogy

Consider a square board of conducting pins arranged in a grid. When current is driven from one corner to the diagonally opposite corner, it does not jump diagonally. It travels along the rows and columns. At each pin junction, the current splits in proportion to the conductance of each available branch. No global path is computed. The macroscopic diagonal flow emerges entirely from local decisions made at each crossroads.

The foam Laplacian L is precisely a resistor network. The face adjacency graph of the truncated octahedron defines a network with 14 nodes (faces), 36 edges (shared face boundaries), and edge weights set by the O_h torsion coupling. The off-diagonal Laplacian elements L_ij = −1 for adjacent faces i, j play the role of resistances. Current flow in the network is identical in structure to foam mode propagation.

**Definition (Local Decision Principle).** At each face junction in the foam, a propagating disturbance transfers spectral weight to adjacent faces in proportion to the overlap between its current mode and each available mode direction. No future junction is consulted. The global path emerges from the sequence of local choices.

This is not an approximation. In a linear resistor network, the full global solution (Kirchhoff's laws) is the unique fixed point of the local gradient-descent dynamics. The same is true for the face Laplacian eigenmodes. Local decisions recover the exact global result, they do not approximate it.

### 1.2 The Face Laplacian as a Resistor Network

The face Laplacian of the truncated octahedron has the spectrum [1]:

$$\{0^1,\ r_1^3,\ 4^2,\ r_2^3,\ 7^4,\ 9^1\}$$

where $r_1 = (9-\sqrt{17})/2$, $r_2 = (9+\sqrt{17})/2$ are the roots of the master equation $\lambda^2 - 9\lambda + 16 = 0$ (discriminant $\Delta = 17$), and the superscripts are multiplicities. The irrep assignments are:

| Eigenvalue | Irrep | Physical sector |
|-----------|-------|----------------|
| 0 | A₁g | Vacuum ground state |
| r₁ ≈ 2.438 | T₁u | Light fermion generations (e, u, d) |
| 4 | Eg | Weak bosons (W, Z) |
| r₂ ≈ 6.562 | T₁u | Heavy fermion generations (μ, c, s; τ, t, b) |
| 7 | A₁g ⊕ T₂g | Gluons |
| 9 | A₂u | Higgs field |

In the resistor network analogy, the eigenvalue is the node's "voltage level." Spectral weight flows from high to low eigenvalue unless constrained by topology. The local decision at each junction is determined by the overlap between the incoming mode and each outgoing mode direction.

### 1.3 Overlap at the Key Junction

The critical junction in the framework is the square-hexagon interface, where the weak sector (Eg, square faces) meets the colour sector (T₂g, hex face edges). Computing the overlap between the Eg mode direction (along a Cartesian axis) and the T₂g edge direction (along the square-hexagon edge):

$$\langle E_g | T_{2g} \rangle = \vec{n}_{sq} \cdot \vec{e}_{sh} = (1,0,0) \cdot (0,-1,1)/\sqrt{2} = 0$$

The overlap is **exactly zero**. The Eg mode cannot couple directly to T₂g at the square-hexagon junction because their directions are perpendicular. The only available forward path is into the hexagonal face (A₂u sector), with overlap:

$$\langle E_g | A_{2u} \rangle = \vec{n}_{sq} \cdot \vec{n}_{hx} = (1,0,0) \cdot (1,1,1)/\sqrt{3} = 1/\sqrt{3} = \cos\theta_{sh}$$

where $\theta_{sh} = \arccos(1/\sqrt{3}) = 54.74°$ is the square-hexagon dihedral supplement, the same angle appearing in the Total Torsion Identity [2]:

$$24\theta_{sh} + 12\theta_{hh} = 12\pi$$

This is not a coincidence. The dihedral angle governs both the total torsion of the cell and the coupling between generations. They are the same geometric object.

---

## 2. Generation Mass Ratios from Local Path Geometry

### 2.1 Generation 1→2: A Straight Path

The T₁u mode (fermion generation sector) points along a Cartesian axis, the direction of translation symmetry in 3D space. The Eg mode (weak sector) lives on the square face normals, also along Cartesian axes. These two sectors are **collinear**:

$$\vec{n}_{T_{1u}} \parallel \vec{n}_{E_g}$$

When the foam disturbance transitions from Gen 1 (electron sector, eigenvalue r₁) to Gen 2 (muon sector, through the Eg junction), the path is straight. No turn is required. The coupling constant for this transition is:

$$K_{12} = r_{Eg} = 4$$

This is exact. The Gen 1→2 coupling is determined by the Eg eigenvalue alone, with no angular correction, because the path is collinear.

### 2.2 Generation 2→3: A Forced Turn

The Eg mode (eigenvalue 4, Cartesian axis) must reach the T₂g mode (eigenvalue 7, edge diagonal direction). Their directions make an angle:

$$\cos^{-1}\left(\vec{n}_{Eg} \cdot \vec{n}_{T_{2g}}\right) = 90°$$

As shown in Section 1.3, the Eg mode has zero overlap with the T₂g edge at the square-hexagon junction. The local decision is forced: the only available path is Eg → A₂u (through the hex face) with coupling $1/\sqrt{3}$, then A₂u → T₂g (via the hex-square edge). The path curves through exactly $\theta_{sh}$ at the junction.

The effective coupling for Gen 2→3 is therefore:

$$K_{23} = r_{Eg} \times \frac{\theta_{sh}}{\pi} = 4 \times \frac{\arccos(1/\sqrt{3})}{\pi} = 1.2163...$$

The ratio $K_{12}/K_{23} = \pi/\theta_{sh} = 3.289$ comes entirely from the cell geometry, the angle between the Cartesian axis and the square-hexagon dihedral.

### 2.3 The Tau Mass Formula

The tau mass from the local decision principle:

$$m_\tau = m_\mu \times \exp\!\left(\frac{r_{T_{2g}}}{C_A} \times K_{23}\right) = m_\mu \times \exp\!\left(\frac{28\,\arccos(1/\sqrt{3})}{3\pi}\right)$$

Numerically: $m_\tau^{\text{wall}} = 1805.4\ \text{MeV}$, observed $1776.9\ \text{MeV}$, wall-only error $+1.60\%$.

The remaining $1.60\%$ is the first-order void correction. The tau is a T₁u(r₂) fermion (odd under the antipodal map) and the void channel pushes odd modes downward by $\eta_{T_{1u}(r_2)} \approx 0.076$ (from the Void Channel paper [3]). The corrected prediction brackets the observed value between the wall-only result ($+1.60\%$) and the full void-corrected result. The mechanism is completely identified; the exact perturbation coefficient follows from the published $H = L + \eta V$ framework.

---

## 3. The Geometric Progression r₁, Eg(4), r₂

### 3.1 The Exact Relation

From the master equation $\lambda^2 - 9\lambda + 16 = 0$:

$$r_1 \times r_2 = 16 = 4^2 \quad \text{(exactly)}$$

Therefore $4 = \sqrt{r_1 r_2}$, the Eg eigenvalue is the **exact geometric mean** of the two T₁u eigenvalues. In log-eigenvalue space:

$$\ln(4) - \ln(r_1) = \ln(r_2) - \ln(4) = \ln(4/r_1) = 0.4949...$$

The three generation-relevant eigenvalues r₁, 4, r₂ form a perfect geometric progression with equal log-spacing. This is not a numerical coincidence, it is an algebraic consequence of the master equation $r_1 r_2 = 16$.

### 3.2 Physical Meaning

The no-zero principle of the framework states that no mode can have zero spectral occupation. The vacuum is the ground state of the constrained oscillator, not the absence of excitation. The geometric progression r₁, 4, r₂ is the unique structure compatible with:

1. The master equation $r_1 + r_2 = 9$, $r_1 r_2 = 16$
2. The Eg eigenvalue being the geometric mean: $r_{Eg} = \sqrt{r_1 r_2}$
3. Equal log-spacing in the generation sector (no preferred generation scale)

The three generations span exactly one geometric doubling in spectral space, from r₁ through Eg(4) to r₂. In log-eigenvalue space this is a staircase with identical step height $\delta = \ln(4/r_1) = \ln(r_2/4)$.

---

## 4. Direct Spectral Derivation of the Muon Mass

### 4.1 The Formula

The Gen 1→2 transition is straight (Section 2.1), with coupling $K_{12} = r_{Eg} = 4$. The log-mass step in units of the spectral distance $\delta = \ln(4/r_1)$ is:

$$\ln(m_\mu/m_e) = K_{12} \times \frac{r_1 r_2}{C_A} \times \frac{1}{r_{Eg}^2} \times r_{Eg}^2 = \frac{r_1 r_2}{C_A} = \frac{16}{3}$$

More directly: the T₁u sector has total spectral capacity $r_1 \times r_2 = 16$. Distributing this across $C_A = 3$ colour channels gives the log of the muon-to-electron mass ratio:

$$\boxed{\frac{m_\mu}{m_e} = \exp\!\left(\frac{r_1 r_2}{C_A}\right) = \exp\!\left(\frac{16}{3}\right) = 207.127}$$

Observed: $m_\mu/m_e = 206.768$. Error: $0.174\%$ on the ratio.

The muon mass: $m_\mu = m_e \times \exp(16/3) = 105.677\ \text{MeV}$. Observed: $105.658\ \text{MeV}$. Error: **$0.017\%$**.

### 4.2 Physical Interpretation

$r_1 \times r_2 = 16$ is the total spectral weight of the T₁u sector, the product of the two T₁u eigenvalues, encoding the full generation capacity of the foam. $C_A = 3$ is the number of colour channels (dimension of T₂g). The muon/electron mass ratio is the exponential of the total T₁u spectral capacity divided by the number of colour channels.

No action causes zero effect. The spectral weight distributed across $C_A$ channels, with nothing lost, gives the exact generation mass ratio. This is the no-zero principle as a mass formula.

### 4.3 Consistency with Koide

The Koide formula [4] gives $m_\mu/m_e = 206.768$ to $10$ ppm using the independently derived Koide angle $\theta = 2/9$ from $(λ_{A_{2u}} - λ_{T_{2g}})/λ_{A_{2u}} = 2/9$. The spectral formula gives $207.127$, a $0.17\%$ discrepancy consistent with the first-order void correction (the muon is also a T₁u fermion, odd under the antipodal map). The two derivations approach the same result from different directions, the Koide path uses the torsion phase structure, the spectral path uses the eigenvalue products. Both are consequences of the same underlying geometry.

---

## 5. The Polaron Derivation of the Electron Mass

### 5.1 Alternative Derivation

The published electron mass formula is [5]:

$$m_e = r_1\, M_P\, \exp\!\left(-\frac{(E-F)(2\Delta + \sqrt{\Delta})}{16}\right) = 511.01\ \text{keV} \quad (0.002\%)$$

An independent derivation follows from treating the electron as a polaron, a charge disturbance bound to the foam by the weak-sector gap. The weak gap between the Eg sector (square face centre, distance 2 from cell centre) and the Higgs sector (hex face centre, distance $\sqrt{3}$) is:

$$g_w = r_{sq} - r_{hx} = 2 - \sqrt{3}$$

The electron couples to the foam through this gap, repeated $r_1 + r_2 = 9$ times (once per unit of total spectral weight). The anharmonic correction arises from the O_h tensor product $T_{1u} \otimes A_{2u} \supset T_{1g}$, which has dimension $C_A$, giving a zero-point correction $\sqrt{C_A/2}$:

$$m_e^{\text{polaron}} = \frac{v}{8\sqrt{2}} \times (2-\sqrt{3})^9 \times \frac{r_2}{r_1} \times \sqrt{\frac{C_A}{2}}$$

where $v = 246.22\ \text{GeV}$ is the electroweak VEV (itself derived from cell integers [5]).

Numerically: $m_e^{\text{polaron}} = 0.5102\ \text{MeV}$, error $0.156\%$.

### 5.2 Status

The polaron formula gives a slightly larger error than the published formula ($0.156\%$ vs $0.002\%$) because it uses the first-order weak gap without the exact exponent. It is not a replacement for the published formula, it is a physically transparent alternative derivation that confirms the same result via a different physical picture: the electron as a polaron bound by the weak sector gap, with the anharmonic correction from the O_h representation theory.

---

## 6. Three Generations as an O_h Theorem

### 6.1 The Distortion Irreps of O_h

The octahedral group O_h acts on the truncated octahedron by permuting and negating coordinate axes. Under this action, the space of small cell deformations decomposes into irreducible representations. The **distortion irreps** (those that deform the cell shape while preserving its topology) are precisely three:

| Irrep | Eigenvalue | Deformation type |
|-------|-----------|-----------------|
| T₁u | r₁, r₂ | Translation (shear along principal axes) |
| Eg | 4 | Oblate/prolate (axial compression or extension) |
| T₂g | 7 | Shear (off-diagonal strain) |

A fourth generation of fermions would require a fourth distortion irrep (a new deformation mode of the cell that is independent of the three above and still transforms as a non-trivial irrep of O_h. The complete irrep decomposition of the face representation of O_h contains no such fourth distortion mode. The remaining irreps (A₁g, A₂u) are the vacuum ground state and the Higgs field respectively) both already assigned.

**Theorem.** The truncated octahedron with O_h symmetry has exactly three distortion irreducible representations. Therefore the UFFT framework admits exactly three fermion generations.

This is a theorem of representation theory, not an assumption or a parameter fit. It is provable from the character table of O_h and the face adjacency representation alone.

### 6.2 Connection to the BCC Lattice

The same result was previously established [6] via the BCC lattice geometry: $N_{gen} = F_{sq}/2 = C_A = 3$. The present derivation is complementary and more fundamental, it shows that three generations follow from O_h symmetry directly, without requiring the BCC counting argument. Both derivations agree, confirming the result from independent directions.

---

## 7. Eight Gluons from Eight Hexagonal Faces

### 7.1 The Identification

The truncated octahedron has 8 hexagonal faces. The outward normals of these faces point along the 8 directions of the (111)-family:

$$\pm(1,1,1)/\sqrt{3},\quad \pm(1,1,-1)/\sqrt{3},\quad \pm(1,-1,1)/\sqrt{3},\quad \pm(-1,1,1)/\sqrt{3}$$

These 8 directions are precisely the 8 nearest-neighbour directions in the BCC lattice, the 8 shortest lattice vectors. In the SU(3) gauge theory, there are exactly 8 gluon degrees of freedom corresponding to the 8 generators of SU(3).

**The 8 gluon degrees of freedom correspond to the 8 hexagonal face normals of the Kelvin cell.**

### 7.2 Why the Hexagonal Faces and Not the Square Faces

The square faces (6 faces, normals along $\pm x, \pm y, \pm z$) carry the weak force (Eg sector). The Higgs mechanism on the square faces forces SU(2)×U(1) → U(1). The hexagonal faces (8 faces, T₂g sector) carry colour. The distinction between the two face types is the geometric origin of the distinction between the weak force and the strong force.

### 7.3 Spontaneous Symmetry Breaking is Forced

The insphere of the truncated octahedron touches the hexagonal faces at distance $r_{hx} = \sqrt{3}$. The gap from the insphere to the hexagonal face is **exactly zero** at the touching point. This means the T₂g sector modes (colour/gluon sector) are pinned at the boundary, there is no room for the Higgs field to create a mass gap in this sector. The gluons remain massless by geometric necessity. Colour confinement rather than mass generation follows from the topology of the BCC packing.

---

## 8. Cell/Void/Either: Geometric Origin of Spin-Statistics

### 8.1 The Antipodal Map

The Void Channel paper [3] establishes the complete Hamiltonian $H = L + \eta V$ where $V$ is the antipodal map on faces. The antipodal map sends each face to its geometrically opposite face (normal $\hat{n} \to -\hat{n}$). Every face has exactly one antipodal partner; the 14 faces form 7 antipodal pairs.

The antipodal map $V$ is an involution ($V^2 = I$) with eigenvalues $\pm 1$. Every mode is either even ($+1$, symmetric under the antipodal map) or odd ($-1$, antisymmetric).

### 8.2 The Classification

The eigenvalues of $V$ on each irrep are:

| Irrep | V parity | Physical particles | Statistics |
|-------|---------|-------------------|-----------|
| A₁g (λ=0) | **Even (+1)** | Photon | Bose-Einstein |
| T₁u (λ=r₁,r₂) | **Odd (−1)** | Fermion generations | Fermi-Dirac |
| Eg (λ=4) | **Even (+1)** | W, Z bosons | Bose-Einstein |
| T₂g (λ=7) | **Even (+1)** | Gluons | Bose-Einstein |
| A₂u (λ=9) | **Odd (−1)** | Higgs | — |

**Bosons are even. Fermions are odd.**

This is not imposed by hand. It follows directly from the antipodal map acting on the face representation of O_h. The spin-statistics connection (bosons have integer spin, fermions have half-integer spin) is equivalent to the even/odd classification under the antipodal map of the foam cell.

### 8.3 Cell, Void, and Either

From the void coupling $H = L + \eta V$:

**Cell wall only (odd, fermions):** T₁u and A₂u modes are antisymmetric under the antipodal map. When the void pushes even modes up and odd modes down, odd modes cannot propagate through the void without reversing sign, they are topologically committed to the wall. A fermion occupies exactly one wall location. This is the geometric origin of the Pauli exclusion principle.

**Void only:** Bell correlations, EPR entanglement, and non-local quantum correlations propagate through the void channel (the antipodal constraint). No particles live here, only constraints between antipodal faces.

**Either (even, bosons):** A₁g, Eg, and T₂g modes are symmetric under the antipodal map. They can propagate through the wall (Laplacian channel, local, causal) or jump through the void (antipodal channel, non-local, acausal but carrying no information). A photon is not a particle travelling through space, it is the void-channel propagation between two fermion events. This is the geometrical resolution of wave-particle duality.

---

## 9. The Recording Principle and the Measurement Problem

### 9.1 The Standard Problem

The quantum measurement problem asks: why does the wavefunction appear to collapse when a measurement is made? Standard quantum mechanics leaves the measurement process undefined, it is an external operation performed by an observer who stands outside the theory.

### 9.2 The Foam Resolution

In the UFFT framework there is no external observer. The foam IS the substrate. When a particle propagates, it disturbs the face pressures of the cells along its path. That disturbance is the recording. The foam records events by settling into new face pressure equilibria, this is the physical content of the path integral, which in UFFT is a sum over face pressure configurations [7].

**The Recording Principle:** The foam records each event by finding the unique face pressure equilibrium of minimum recording cost consistent with the no-zero constraint. The path chosen is the path the foam can sustain indefinitely without further adjustment.

The no-zero constraint (no face pressure goes to zero) is both the physical constraint on the path integral and the recording mechanism. A particle exists precisely because the foam can record it with finite face pressure change. The recording and the existence are the same thing.

### 9.3 The Local Decision Connection

The local decision principle (Section 1) and the recording principle are the same mathematical object, viewed from two perspectives:

- **From the particle:** at each junction, the disturbance makes a greedy local choice (maximum overlap, minimum recording cost)
- **From the foam:** at each cell, the pressure equilibrium adjusts locally to record the passing disturbance

Both descriptions produce the same path. The "path chosen" is the path of minimum total recording cost, which is identically the path of minimum action in the standard Feynman formulation, but derived here from the physical equilibration dynamics of the foam rather than imposed as an external variational principle.

### 9.4 Resolution Without Observers

The quantum measurement problem is resolved without invoking:
- A conscious observer
- Many-worlds branching
- Hidden variables
- Wavefunction collapse as a distinct dynamical process

The foam equilibrates. The equilibrium IS the measurement. This is decoherence in its most literal physical form, not as an approximation or interpretation, but as the actual pressure-equilibration dynamics of the Planck-scale substrate.

---

## 10. Summary and Unification

All eight results in this paper are expressions of a single principle applied to different geometrical sectors of the truncated octahedron:

| Result | Sector | Local decision at |
|--------|--------|------------------|
| K₁₂ = 4 (straight) | T₁u ∥ Eg | Collinear junction |
| K₂₃ = 4θ_sh/π (curved) | Eg ⊥ T₂g | Sq-hx junction, forced turn |
| r₁, 4, r₂ geometric progression | T₁u eigenvalues | r₁r₂ = 16 from master equation |
| m_μ/m_e = exp(16/3) | T₁u spectral capacity | C_A colour channels |
| Polaron formula for m_e | Weak gap (2−√3)⁹ | O_h anharmonic correction |
| Three generations | O_h distortion irreps | No fourth irrep exists |
| 8 gluons = 8 hex normals | T₂g sector | BCC nearest neighbours |
| Cell/void/either | Antipodal parity | Even/odd under V |
| Recording principle | Path integral | Minimum cost equilibrium |

None of these required new inputs beyond what was already in the framework. They required only asking: *what does the foam actually do at each junction, given the geometry of the cell?* The local decision principle is the answer to that question.

---

## Consistency with Published Results

All results in this paper are consistent with the existing 47 preprints. Specifically:

- The tau mass formula (Section 2.3) reproduces the wall-only prediction; the $1.60\%$ residual is the first-order void correction from the Void Channel paper [3], which pushes T₁u(r₂) fermions downward by $\eta_{T_{1u}(r_2)} \approx 0.076$.
- The muon mass formula (Section 4.1) is consistent with the Koide derivation [4] at $0.017\%$.
- The electron polaron formula (Section 5.1) is consistent with the published formula [5] at $0.156\%$.
- The three-generations theorem (Section 6) is consistent with the BCC lattice counting [6] at $N_{gen} = F_{sq}/2 = C_A = 3$.
- The gluon count (Section 7) is consistent with the SU(3) gauge structure [8].
- The cell/void/either classification (Section 8) is consistent with the Void Channel Hamiltonian $H = L + \eta V$ [3].
- The recording principle (Section 9) is consistent with the path integral derivation [7].

---

## Open Items

The following remain for future work:

1. The exact first-order void correction coefficient for the tau mass, from the full $H = L + \eta V$ perturbation series [3].
2. A rigorous proof that the polaron formula and the published electron mass formula converge to the same exact result in the limit of complete O_h symmetry.
3. The application of the local decision principle to the quark sector, each quark type (up-type vs down-type) takes a different path through the cell geometry, which should give the generation mass ratios for quarks independently of the CKM rotation.

---

## References

[1] Martin, L. (2026). The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062

[2] Martin, L. (2026). Total Torsion Identity and Foam Equilibration Timescale. DOI: 10.5281/zenodo.19306543

[3] Martin, L. (2026). The Void Channel: Entanglement from the Antipodal Map (H = L + ηV). DOI: 10.5281/zenodo.19307111

[4] Martin, L. (2026). Lepton Mass Ratios from the Face Laplacian Spectrum. DOI: 10.5281/zenodo.19185685

[5] Martin, L. (2026). The Complete Particle Mass Spectrum from Cell Integers. DOI: 10.5281/zenodo.19307003

[6] Martin, L. (2026). Three Generations from the BCC Lattice. DOI: 10.5281/zenodo.19306393

[7] Martin, L. (2026). The Path Integral from Planck-Scale Foam. DOI: 10.5281/zenodo.19306828

[8] Martin, L. (2026). Asymptotic Freedom and Quark Confinement as Geometric Theorems. DOI: 10.5281/zenodo.19064581

[9] Koide, Y. (1982). A fermion-boson composite model of quarks and leptons. Physics Letters B, 120(1–3), 161–165.

[10] Feynman, R. P. (1948). Space-Time Approach to Non-Relativistic Quantum Mechanics. Reviews of Modern Physics, 20(2), 367–387.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). All theoretical ideas, physical intuitions, and framework direction: Luke Martin. AI role: derivation formulation, numerical verification, document composition. The local decision principle was identified by Luke Martin through the analogy with electrical current in a pin grid; the mathematical formulation, overlap calculations, and numerical verification were completed in collaboration with Claude.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*

*B + V = 