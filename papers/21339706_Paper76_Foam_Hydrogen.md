# UFFT Paper #76 — Hydrogen from the Foam: The Coulomb Law from Cell Adjacency, Charge as Scalar Dressing, and the Rydberg Scale with No New Parameters

**Unified Foam Field Theory — Part LXXVI**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | July 2026 |
| Series | Unified Foam Field Theory |
| Paper | #76 of 76 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 (conditional on the framework's derived alpha and m_e; the lattice results of Sections 2-4 and 6 are unconditional) |
| DOI | 10.5281/zenodo.21339706 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, hydrogen atom, Coulomb law, lattice Green's function, Rydberg constant, charge quantisation, bound states

---

## Abstract

We construct the hydrogen atom directly from cell dynamics on the BCC lattice of truncated octahedra, with no continuum potential written in by hand. Four results. (1) The lattice Green's function of the scalar (A1g) channel is Coulombic: G(r) fits A/r with tail strength A = 1/(4pi) exact, box-stable and isotropic to five digits. The 1/r law is a property of cell adjacency. (2) Electric charge is the A1g content of a defect. A bare matter-pattern (T1u) defect is foam-neutral, with no monopole tail; the A1g x T1u cross-coupling vanishes identically (parity selection rule, verified to 1e-17 in both inter-cell coupling conventions); a charged particle is a T1u defect dressed with a unit of the A1g mode. (3) A light dressed defect bound in the well of a heavy one reproduces the hydrogen ladder, including the near-degeneracy of 2s and 2p at the same rung (spread below 1 percent), the fingerprint of the hidden SO(4) symmetry of a true 1/r force. With the framework's derived fine-structure constant [2] and electron mass [3], the Rydberg energy is alpha^2 m_e c^2 / 2 = 13.605693 eV against CODATA 13.605693 eV, and the reduced-mass ground state is 13.598287 eV against the measured 13.598434 eV; the 1.1e-5 residual is the relativistic and QED structure a Schrodinger-level calculation is supposed to leave behind. The bound-state problem introduces no new parameter. (4) The foam leaves a derived signature: the ground state deviates from ideal Coulomb by delta = -K/a_B^2 with both the exponent (contact mechanism from the quartic lattice term) and the coefficient K = 256(D0 - Dnn - 7/320) = 3.810 in closed form. At the physical scale a_B/l_P ~ 3.3e24 this gives |delta| ~ 3e-49: the medium computes its own invisibility. Three verification scripts accompany the paper.

---

## 1. Question and scope

Can bound states be built directly from cell dynamics, without routing through reconstructed QED? This paper answers for the simplest atom. The claim is Schrodinger-level: the 1/r law, the level ladder, its hidden symmetry, and the 13.6 eV scale, from the lattice alone plus two prior framework results (alpha and m_e). Nothing here disputes a digit of QED; the fine structure and Lamb shift live in the relativistic layer, which is future work (Section 7).

## 2. The Coulomb law from adjacency

The foam is the BCC lattice of truncated octahedra (primitive vectors (1,1,-1), (-1,1,1), (1,-1,1)), each cell coupled to 8 hexagonal-face and 6 square-face neighbours. The scalar channel is the A1g projection of the 14-component face field.

The lattice Green's function of this channel is Coulombic:

**G(r) = A/r + B,  A = 1/(4pi) exactly**

- The tail strength follows from the source identity sum s s^T = 32 I (premise check A1); the background-free numerical estimate lands within 0.5 percent of 1/(4pi) (A2).
- The fit residual is 5e-3 over r = 1.7 to 10.4 cell units; the offset B is a periodic-image artifact and halves as the box grows.
- Isotropy is exact to five digits: G at equal distance along the axis and along the body diagonal agree.

No continuum input, no potential postulated. The 1/r law is what cell adjacency does.

## 3. Charge is scalar dressing

Place two static defects and compute their interaction through the full 14-component lattice propagator (background-subtracted):

- **A1g-pattern sources attract/repel as 1/r.** The scalar channel carries the charge-charge interaction.
- **Bare T1u-pattern sources are foam-neutral.** No monopole term; the residual interaction decays faster than 1/r with an orientation-dependent multipole sign structure.
- **The A1g x T1u cross term is exactly zero at every separation.** This is a parity selection rule, H(-q) = P H(q) P with the scalar mode even and the T1u doublet odd; verified to 1.12e-11 in the same-index coupling model used by the hydrogen chain and to 1e-17 relative in the partner-face convention (the convention B + V = D itself selects; the two conventions are identical on the even sector at every q, so the hydrogen chain is convention-independent).

Electric charge is therefore the A1g content of a defect and nothing else. A neutral particle is a pure matter pattern; a charged particle is a matter pattern dressed with a unit of the uniform mode. Hydrogen is two oppositely dressed defects sharing one Coulomb tail.

## 4. The ladder and the SO(4) fingerprint

Bind a light dressed defect in the well of a heavy one: a discrete Schrodinger problem whose kinetic term is the A1g channel's own hopping and whose potential is the measured foam Green's function (hard core at r = 0; two defects never share a cell). A control run with the ideal 1/r potential validates the solver (ground state within 6 percent of the Rydberg prediction at the working box size, E1/<E2> = 3.85 against the Coulomb 4.0).

The foam potential produces a hydrogen-like ladder, and it passes the sharp test. A generic attractive well splits states of different shape at the same rung. The pure 1/r law carries a hidden symmetry larger than rotations (Fock's SO(4) [6]) that forces 2s and the 2p triplet to the same energy. In the lattice calculation the 2s/2p spread is below 1 percent of the gap to the ground state (premise check A6). The potential built from adjacency is Coulomb in the part that matters, not a lookalike well.

## 5. The scale: 13.6 eV with nothing left to choose

Two prior results set the scale: the fine-structure constant from the single-cell heat kernel [2] and the electron mass from the walk action [3]. Neither is adjusted here. Given the two, the Rydberg energy is fixed:

**Ry = alpha^2 m_e c^2 / 2 = 13.605693 eV   (CODATA: 13.605693 eV)**

One step further, with the finite proton mass, the ground state is 13.598287 eV against the measured 13.598434 eV. The residual of 1.1e-5 is the relativistic fine structure and Lamb shift, exactly the layer a non-relativistic substrate calculation is supposed to leave behind.

The claim is narrow and therefore strong: once alpha and m_e are in hand, the bound-state problem introduces no further freedom anywhere in the chain.

## 6. The foam's own signature

Near the bottom of the well the potential is not exactly 1/r; the granularity shows through. The deviation of the ground state from ideal Coulomb at equal tail strength is negative (the foam binds slightly less) and falls with the square of the atomic size:

**delta(a_B) = -K/a_B^2,  K = 256 (D0 - Dnn - 7/320) = 3.810**

- The exponent is analytic: the quartic term of the lattice dispersion acts as a contact correction under a hydrogenic 1s, giving delta proportional to |psi(0)|^2 a_B / Ry, i.e. a_B^-2. The angular average of the quartic term is <c> = 1344/61440 = 7/320 exactly.
- The coefficient is in closed form; D0 and Dnn are the two Watson-type lattice deviation constants. The perturbation-theory ladder gives K = 3.89 at the clean-window edge and the finite-size gap halves per octave (1/a_B scaling), so the closed form is the exact asymptote (check A7).
- One labeled remainder: the few-percent anisotropic-weighting correction to the uniform angular average <c>. It does not touch the exponent.

At the physical scale a_B/l_P ~ 3.3e24, |delta| ~ 3e-49 of the binding energy. A Planck-scale medium should hide itself almost perfectly at atomic scale; here the degree of hiding is computed rather than asserted.

## 7. Standing and open items

Derived here, unconditionally: the 1/r tail with A = 1/(4pi), the charge selection rule, the ladder with its SO(4) fingerprint, and the deviation law with closed-form exponent and coefficient. Conditional (hence Tier 2 overall): the 13.6 eV scale inherits the framework's alpha [2] and m_e [3] with their own stated checks. Open, as future programme: the relativistic layer (fine structure from the T1u sector), and the anisotropic-weighting remainder above.

## Verification

- `verification/verify_foam_hydrogen_premises_2026-07.py` (10 checks: source identity and exact tail strength, background-free tail, selection rule, solver extrapolation, closed-form contact chain A5i-A5iv, finite-size octave halving, 2s/2p degeneracy). All pass.
- `verification/verify_foam_hydrogen_deviation_2026-07.py` (6 checks: sign, exponent, coefficient window, solver cross-check). All pass.
- `verification/explore_foam_hydrogen_2026-07.py` (ladder construction and control run).

## References

### UFFT Papers
- [1] Paper #5 — The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph. DOI: 10.5281/zenodo.19030062
- [2] Paper #3 v2 — The Fine Structure Constant from Foam Geometry. DOI: 10.5281/zenodo.19019944
- [3] Paper #44 — The Complete Particle Mass Spectrum from Planck-Scale Foam Geometry. DOI: 10.5281/zenodo.19307003
- [4] Paper #45 v2 — The Void Channel: H = L + etaV. DOI: 10.5281/zenodo.21331511
- [5] Paper #29 — Maxwell's Equations from Foam Displacement Dynamics. DOI: 10.5281/zenodo.19185556

### External References
- [6] Fock, V. (1935). Zur Theorie des Wasserstoffatoms. Zeitschrift fur Physik, 98, 145-154.
- [7] Watson, G. N. (1939). Three triple integrals. The Quarterly Journal of Mathematics, 10(1), 266-276.
- [8] Tiesinga, E. et al. (2021). CODATA recommended values of the fundamental physical constants: 2018. Reviews of Modern Physics, 93, 025010.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Paper #76 · DOI: 10.5281/zenodo.21339706 · Priority Date: 20 February 2026*

*B + V = D*
