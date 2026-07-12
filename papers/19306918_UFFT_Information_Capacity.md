# UFFT Paper #43 — Information Capacity and Bandwidth of the Planck-Scale Foam: Why Physics Is Simple, Why Forces Have Different Strengths, and Why Black Holes Exist

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | March 2026 |
| Series | Unified Foam Field Theory |
| Paper | #43 of 63 |
| Framework | v10 |
| Status | Complete, Tier 2 |
| Tier | 2 |
| DOI | 10.5281/zenodo.19306918 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, information capacity, bandwidth, Planck foam, Bekenstein bound, asymptotic freedom

---

## Abstract

The truncated octahedron foam lattice is analysed as an information network. Each face carries one information quantum (~1 bit at saturation). Each edge is a channel with capacity one displacement quantum per Planck time. Each vertex is a routing node. The maximum throughput per face equals the face degree: 4 channels for square faces, 6 for hexagonal faces. This bandwidth asymmetry explains the force hierarchy: the weak force (Eg irrep, pure square faces) propagates through only 24 of 36 edges (2/3 of EM bandwidth), making it intrinsically weaker and shorter-range. The strong force's asymptotic freedom arises because its preferred channels (hx-hx edges) saturate first at high energy, forcing signal rerouting to less efficient edges. The Bekenstein-Hawking entropy S = A/(4l_P²) reduces to ~F = 14 per cell, with the factor 4 being the average face area in Planck units (3.83 l_P²). A black hole is a cell with all 36 edges at maximum capacity. The hierarchy exp(−F) emerges as the probability of a localised excitation sustaining itself against 14 neighbours pushing back. All known physics operates below 10⁻²⁰ of the foam's edge capacity, explaining why the linear face Laplacian is accurate and why the laws of physics appear simple.

---

## 1. The Foam as Information Network

The truncated octahedron has 14 faces, 36 edges, and 24 vertices. In the UFFT framework, these are not abstract geometric elements, they are the physical components of an information network operating at the Planck scale.

- **Face** = information carrier. Each face holds a displacement amplitude ψ_i. At saturation, each face carries approximately 1 bit of information (from the Bekenstein bound; see §5).

- **Edge** = channel. Each edge connects two adjacent faces and transmits the pressure differential (ψ_i − ψ_j) between them, weighted by the torsion phase e^{iθ}. Maximum capacity: 1 displacement quantum per Planck time.

- **Vertex** = routing node. Each vertex is shared by 3 faces and 3 edges, and determines how signal splits between channels.

---

## 2. Face Bandwidth

The **bandwidth** of a face equals its degree in the face graph, the number of edges through which it can send or receive signal.

| Face type | Degree | Bandwidth | Neighbours |
|-----------|--------|-----------|-----------|
| Square | 4 | 4 channels | 4 hexagonal (no sq-sq edges) |
| Hexagonal | 6 | 6 channels | 3 square + 3 hexagonal |

The hexagonal sector has 50% more bandwidth per face than the square sector. This asymmetry is the physical origin of the force hierarchy.

**Total network bandwidth:** 36 edges (each shared by 2 faces). Of these, 24 are sq-hx edges and 12 are hx-hx edges.

---

## 3. Force Strengths from Channel Counts

Each force in the Standard Model lives on a specific irrep of O_h, which restricts it to specific edge types.

| Force | Irrep | Available edges | Bandwidth | Fraction of total |
|-------|-------|----------------|-----------|-------------------|
| Electromagnetic | A₁g | All 36 | 36 | 100% |
| Strong | T₂g | All 36 (dominated by hx-hx) | 36 | 100% |
| Weak | Eg | 24 (sq-hx only) | 24 | 67% |
| Higgs | A₂u | 12 (hx-hx only) | 12 | 33% |

The weak force uses only 2/3 of the electromagnetic bandwidth because it lives on the Eg irrep (pure square faces), and square faces connect only to hexagonal faces through sq-hx edges. There are no sq-sq edges. The weak force has no alternative routing.

The Higgs field uses only 1/3 of the bandwidth because the A₂u irrep lives purely on hexagonal faces, and only the 12 hx-hx edges connect hexagons to hexagons without passing through a square face.

---

## 4. Running Couplings as Bandwidth Management

As the energy of a process increases, the edge loads approach capacity. The signal must redistribute. Different forces redistribute differently because they use different edge sets.

### 4.1 Vacuum polarisation (α increases with E)

The electromagnetic coupling uses all 36 edges equally. As energy increases, all edges load up together. More signal on all channels simultaneously increases the effective coupling. This is vacuum polarisation, α runs upward with energy.

### 4.2 Asymptotic freedom (α_s decreases with E)

The strong force is dominated by hx-hx edges (the torsion channel carrying T₂g). These 12 edges have higher load per edge than the 24 sq-hx edges (because the strong force preferentially uses them). At high energy, the hx-hx edges approach capacity first. The signal reroutes to sq-hx edges, which don't carry the T₂g mode efficiently. The effective coupling decreases. This is asymptotic freedom.

The same edge set that makes the strong force strong at low energy (concentrated on 12 hx-hx edges = high signal density) makes it weak at high energy (12 edges saturate before 24 do).

### 4.3 Electroweak unification

The weak force uses 24 sq-hx edges. At high energy, these edges approach capacity. But square faces have no sq-sq alternative (every sq edge goes to a hexagon. When the sq-hx edges saturate, the distinction between the sq sector (weak) and the full network (EM) dissolves. The forces merge. This is electroweak unification) the bandwidth bottleneck at square faces disappears when all edges are equally loaded.

---

## 5. The Bekenstein Bound = Face Count

The Bekenstein-Hawking entropy of a black hole is S = A/(4l_P²). For a single foam cell:

- Total surface area: A = 6 × 1 + 8 × (3√3/2) = 26.78 (in edge-length² units)
- In Planck units (edge = √2 l_P): A = 53.57 l_P²
- Bekenstein entropy: S = 53.57/4 = **13.4 bits**
- Face count: F = **14**

S_Bekenstein ≈ F to 4%. Each face carries approximately 1 bit at maximum capacity.

The mysterious factor 4 in the Bekenstein formula is the average face area in Planck units: A_total/F = 53.57/14 = 3.83 l_P² ≈ 4 l_P². The "quarter" in S = A/4 is not a fundamental constant, it is the area of one face of the Kelvin cell.

---

## 6. Black Holes as Saturated Cells

When all 36 edges of a cell reach maximum capacity:

- Total energy: 36 × ½ E_P = 18 E_P = 2.2 × 10²⁰ GeV
- All faces informationally isolated, no signal can enter or leave
- The cell is a **trapped surface**, a Planck-scale black hole

A Planck-mass black hole (M = M_P, R_s = l_P) is one cell at maximum throughput. Larger black holes are regions where MANY cells are saturated: the event horizon is the boundary between saturated and unsaturated cells.

Hawking radiation is quantum tunnelling through saturated edges, a small probability per Planck time that a displacement quantum leaks through a maxed-out channel. The temperature T_H ∝ 1/M is the inverse of the number of saturated edges on the horizon.

---

## 7. The Speed of Light as Network Speed Limit

The maximum propagation rate is 1 cell per Planck time. This follows directly from the edge capacity: each edge can transmit at most 1 quantum per t_P. A signal traversing one cell (diameter ≈ l_P) takes at least t_P.

**c = l_P / t_P = maximum network propagation speed**

Nothing can exceed c because the edges have finite capacity. Sending more signal per Planck time than the edges can carry is physically impossible. Lorentz invariance is the statement that the foam network has a maximum throughput rate.

---

## 8. Pair Production as Overflow Routing

When an edge approaches capacity, the excess energy cannot propagate through. It creates a new excitation (particle-antiparticle pair) on the adjacent faces.

The pair production threshold is the energy at which the edge load equals the minimum excitation energy (2m_e for electron-positron pairs):

**|ψ_threshold| ≈ √(4m_e/M_P) ≈ 1.3 × 10⁻¹¹** (Planck units)

This is 10⁻¹¹ of the edge capacity. Pair production occurs at absurdly low edge loading. This is why particle physics exists at everyday energies, we never come close to saturating the foam.

---

## 9. Confinement as Tube Saturation

Separating quarks creates a tube of edges carrying the colour signal. Each edge in the tube carries the full colour signal strength. As the tube lengthens, more edges are recruited at the same load per edge. The energy grows linearly with tube length, the QCD string tension.

When any edge in the tube reaches the pair production threshold, the tube snaps. A new quark-antiquark pair appears at the break point. The original quarks are re-confined.

The QCD string tension σ ≈ (440 MeV)² uses only 3 × 10⁻⁴⁰ of the edge capacity. Confinement is a weak perturbation of the foam, not a saturation effect.

---

## 10. The Hierarchy from Collective Pushback

A localised defect (particle) excites a subset of faces. Every excited face shares a wall with unexcited neighbours. Each neighbour pushes back (Newton's third law, equal and opposite pressure on every shared wall). The particle must sustain itself against F = 14 restoration forces simultaneously.

The survival probability is exponentially suppressed:

**m_particle ∝ exp(−F) = exp(−14) ≈ 8 × 10⁻⁷**

This IS the hierarchy between the Planck scale and the electroweak scale. The electron exists because it has enough energy to overcome 14 walls pushing back. The hierarchy isn't fine-tuning, it's 14 neighbours collectively resisting a disturbance.

---

## 11. Why Physics Is Simple

The edge capacity is E_P = 1.22 × 10¹⁹ GeV. The electron mass is 5 × 10⁻⁴ GeV = 4 × 10⁻²³ E_P.

All of particle physics, nuclear physics, atomic physics, chemistry, and biology occurs at edge loads below **10⁻²⁰ of capacity.**

The foam is operating at 0.00000000000000000001% of maximum throughput. The face Laplacian (a linear operator) is an extraordinarily accurate approximation because we are so far from the nonlinear saturation regime.

The "laws of physics" are the leading-order Taylor expansion of a nonlinear information network around the zero-load point. They look simple because the foam is barely loaded. They look linear because |ψ|/ψ_max ≈ 0. They look perturbative because the coupling constants (α, α_s) measure tiny fractions of the edge capacity.

All of these break down near the Planck scale, where edges approach saturation and the nonlinear terms become important. Quantum gravity is not a new theory, it is the full nonlinear dynamics of the foam network, of which the Standard Model and General Relativity are the leading-order linear approximations.

---

## 12. Can an Edge Be Overloaded?

No. An edge is a shared boundary between two faces. The maximum displacement is one Planck length (the face width). If both faces move toward each other by l_P, they overlap, the edge has zero length. The two cells have merged.

Beyond maximum capacity, the topology changes. Two cells become one cell with a different face graph. This is not overload, it is topological transition. In physics, this is what happens at a black hole singularity: the cells merge and the geometry restructures.

The edge capacity is not a speed limit. It is a structural limit. Beyond it, the structure itself changes.

---

## 13. Summary

| Network quantity | Physical meaning |
|-----------------|-----------------|
| Face (14) | Information carrier (~1 bit at saturation) |
| Edge (36) | Channel (max 1 quantum per t_P) |
| Vertex (24) | Routing node |
| Face degree (4 or 6) | Force bandwidth |
| A₁g bandwidth (36) | Electromagnetic strength |
| Eg bandwidth (24) | Weak force strength |
| A₂u bandwidth (12) | Higgs coupling |
| Edge saturation | Pair production / black hole |
| Tube saturation | Confinement / string breaking |
| exp(−F) | 14 neighbours pushing back |
| c = l_P/t_P | Network speed limit |
| S = A/(4l_P²) ≈ F | 1 bit per face |
| 10⁻²⁰ of capacity | Why physics looks linear |

The cell integers V = 24, E = 36, F = 14 are not abstract topological quantities. They are the node count, channel count, and carrier count of the universe's information network. The physics is the information theory. The information theory is the physics.

---

## References

[1] Martin, L. (2026). The UFFT Core Framework v11. github.com/ufft-info/UFFT.

[2] Bekenstein, J.D. (1973). Black holes and entropy. Phys. Rev. D 7, 2333.

[3] Hawking, S.W. (1975). Particle creation by black holes. Commun. Math. Phys. 43, 199.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). The insight that the foam has finite bandwidth and that overloaded edges explain pair production, running couplings, and confinement: Luke Martin. AI role: bandwidth computation, capacity analysis, energy regime table, document composition.

---

*UFFT Core Framework: github.com/ufft-info/UFFT*


---

*Unified Foam Field Theory · Paper #43 · DOI: 10.5281/zenodo.19306918 · Priority Date: 20 February 2026*

*B + V = D*
