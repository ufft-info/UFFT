# UFFT Paper #58 — Placement Theorems for the Gauge Sector: Necessity of SU(3)×SU(2)×U(1)

**Unified Foam Field Theory**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | April 2026 (v2.0: July 2026) |
| Series | Unified Foam Field Theory |
| Paper | #58 of 75 |
| Framework | v10 |
| Version | 2.0 |
| Status | Complete |
| Tier | 1 (Thms 58.1, 58.2) · 2 (Thm 58.3 result — derivation open) |
| DOI | 10.5281/zenodo.21323498 (v2.0; v1: 10.5281/zenodo.19484967) |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, gauge sector, electroweak, Weinberg angle, QCD, colour, confinement, Eg irrep, T2g irrep, placement theorem

## Abstract

We establish by exhaustion the placement of the Standard Model gauge sectors on the eigenspaces of the truncated octahedron's face Laplacian. **Theorem 58.1 (Electroweak Placement):** the Eg doublet at eigenvalue 4 is the unique candidate for the electroweak sector: it is the only even-parity doublet, it is annihilated by the torsion operators (no FCNC channel), and it carries 100% square-face content. **Theorem 58.2 (Colour Placement):** the T₂g triplet at eigenvalue 7 is the unique candidate for the colour sector: it is the only even triplet, it is torsion-active, and its face content is exactly 100% hexagonal (the square subspace decomposes as A₁g ⊕ Eg ⊕ T₁u only, so T₂g cannot occur on squares), the geometric reading of confinement. Together with the fermion and Higgs placements of Paper #57, all six eigenspaces are uniquely assigned, forcing the group content SU(3)×SU(2)×U(1). **Result 58.3 (Weinberg Angle, Tier 2):** the on-shell effective mixing angle formula sin²θ_W = (17 − 3√17)/20 = 0.23153 matches the LEP effective value at 0.00σ and satisfies the exact structural identity cos²θ_W = 2C_A√Δ·s₁/(Δ + C_A), where s₁ is the T₁u(r₁) square-face content; the derivation of the mixing weight itself remains open, and Result 58.3 is stated as a derived formula with an open derivation, not a theorem.

---

## Changes in this version (2.0)

1. **Theorem 58.3 (Weinberg angle) demoted from theorem to derived formula with open derivation.** The v1.0 "proof" contained an abandoned intermediate derivation (evaluating to 1/(1+√17) ≈ 0.195, not the stated result) followed by a bracketed placeholder. Version 2.0 removes the dead end, states the exact structural identity linking the formula to the T₁u(r₁) square content, and names the missing normalisation step as an open problem. The formula and its 0.00σ match to the LEP effective value are unchanged.
2. **The section title "Sin²θ_W = 3/13" corrected** (a stale draft value; the formula is (17 − 3√17)/20 = 0.23153).
3. **Torsion columns in the Section 2 table now name their operators** (T_hex for scalar charges, inter-type T for the chiral ±2i structure), per Paper #57 v2.0. The per-band "+2i / −2i" entries of v1.0 are corrected: the ±2i eigenvectors are equal-weight superpositions of the two T₁u bands.
4. **MS-bar comparison corrected to 7.75σ** (was 7.85σ).
5. A selection-criteria honesty note is added to Section 2 (the criteria C1–C4 are informed by the Standard Model being targeted).
6. **T₂g face content corrected to exactly 100% hexagonal / 0% square** (v1.0 said 98.4%/1.6%; the square subspace decomposes as A₁g ⊕ Eg ⊕ T₁u only, so T₂g cannot occur on squares). The correction strengthens the T₂g exclusion in Theorem 58.1 and the confinement reading in Theorem 58.2. Verified in `verification/verify_Weinberg_obstruction_2026-07.py` (UFFT repository).
7. All other corrections are machine-verified in `verification/verify_FtF_audit_2026-07.py` (UFFT repository).

---

## 1. The Remaining Gap

Papers #56 and #57 (v2.0) established placement theorems for the fermion sector (chiral structure forced by T² = −4·I, band labelling fixed by B+V=D plus the Eg-coupling identification) and the Higgs sector (A₂u uniquely carries the negative scalar torsion charge −1 under T_hex, forcing SSB). The gauge sector — the identification of Eg with the electroweak bosons and T₂g with the gluons — remained at Tier 2: physically motivated but not proved by exhaustion.

This paper closes that gap. The proof strategy is identical to Paper #57: enumerate all candidates in the spectrum, show each alternative fails on at least one structural criterion, conclude the assignment is unique.

---

## 2. The Spectrum and Its Constraints

The face Laplacian L of the truncated octahedron has six eigenvalues with the following irrep decomposition under O_h:

| Eigenvalue | Irrep | Dim | Parity | Face content (sq/hex) | T_hex charge | T (inter-type) |
|-----------|-------|-----|--------|----------------------|--------------|----------------|
| 0 | A₁g | 1 | even | 42.9%/57.1% (uniform) | +1 | not annihilated |
| r₁ ≈ 2.438 | T₁u | 3 | odd | 62.1%/37.9% | +1/3 | ±2i, cross-block (Paper #56) |
| 4 | Eg | 2 | even | 100%/0% | 0 (no hex content) | 0 (annihilated) |
| r₂ ≈ 6.562 | T₁u | 3 | odd | 37.9%/62.1% | +1/3 | ±2i, cross-block (Paper #56) |
| 7 | T₂g⊕A₁g | 3+1 | even | 0%/100% (T₂g); 4/7 sq (A₁g) | −1/3 (T₂g) | torsion-active |
| 9 | A₂u | 1 | odd | 0%/100% | −1 | 0 (annihilated) |

*Operator key (Paper #57 v2.0):* T_hex = (1/3)·A_hh on the hexagonal subgraph carries the scalar torsion charges; the inter-type T = P_sq·L·P_hex − P_hex·L·P_sq carries the chiral ±2i structure on T₁u. The ±2i eigenvectors are equal-weight superpositions of the r₁ and r₂ bands (they are not band-localised).

*Honesty note on the criteria.* C1–C4 below are informed by the Standard Model being targeted: we know the electroweak sector needs a doublet with no tree-level FCNC and the colour sector needs a confining triplet, so we test for those properties. The strength of the exhaustion argument is that the criteria, once granted, are satisfied by exactly one assignment; it is not a derivation of the criteria themselves from the geometry.

The constraints relevant to gauge boson identification:

**(C1) Even parity.** Gauge bosons are spin-1 fields. On the lattice, they are even under the sublattice exchange (square ↔ hexagonal face relabeling within O_h). Odd-parity modes (T₁u, A₂u) are fermion and Higgs candidates respectively (Papers #56, #57). Only even modes are gauge candidates: A₁g(0), Eg, T₂g, A₁g(7).

**(C2) Torsion annihilation for the electroweak sector.** The electroweak gauge bosons do not change quark or lepton generation (there are no flavour-changing neutral currents at tree level in the SM). On the foam, generation is a T₁u quantum number. The operator that mixes T₁u bands is the torsion operator T. A gauge mode that preserves generation must be annihilated by T.

**(C3) Torsion activity for the colour sector.** Gluons carry colour charge and mediate transitions between colour states. On the foam, the torsion operator T acts nontrivially on colour-carrying modes. The colour sector must be torsion-active.

**(C4) Dimension matching.** The electroweak sector SU(2)×U(1) has 3+1 = 4 gauge bosons. Before SSB: 2 charged (W±) + 1 neutral (W³) + 1 hypercharge (B). After SSB: 2 charged (W±) + 1 massive neutral (Z) + 1 massless (γ). The colour sector SU(3) has 8 gluons = C_A²−1 generators acting on C_A = 3 colour directions.

---

## 3. Theorem 58.1 — Eg Is the Unique Electroweak Candidate

**Theorem 58.1 (Electroweak Placement).** *Of all even-parity modes in the face Laplacian spectrum, Eg is the unique candidate for the electroweak boson sector.*

**Proof.** The even-parity modes are: A₁g(0), Eg, T₂g, A₁g(7). We test each against the electroweak criteria.

**A₁g at λ = 0 — excluded.** Dimension 1 (singlet). Cannot provide a charged boson pair. The zero eigenvalue means zero mass — this is the massless photon/graviton mode (the only massless mode in the spectrum). It does not carry a gauge charge; it couples universally to all 14 faces. If A₁g(0) were the entire electroweak sector, there would be no W bosons and no weak force. Excluded by dimension (requires at least 2 for a charged pair) and by the massless eigenvalue.

**T₂g at λ = 7 — excluded.** Dimension 3, even, with exactly 100% hexagonal face content and 0% square content (the square subspace decomposes as A₁g ⊕ Eg ⊕ T₁u only; T₂g does not occur on the 6 squares). The torsion operator T acts nontrivially on T₂g — T₂g is torsion-active (shown by direct computation: the T₂g torsion block has nonzero entries). This violates criterion C2: an electroweak mode must be torsion-annihilated to prevent tree-level flavour-changing neutral currents. Additionally, zero square content means T₂g modes are confined to the bubble interior and do not propagate through the void (square) interface at all. The electroweak force, which couples preferentially to left-handed fermions (62% square content, Paper #57), must live on the square faces to achieve this coupling. Excluded by torsion activity and face content.

**A₁g at λ = 7 — excluded.** Dimension 1 (singlet). Same exclusion as A₁g(0) by dimension: cannot provide a charged pair. Additionally, λ = 7 is a massive mode, so it cannot serve as the hypercharge boson B (which is massless before SSB). Excluded by dimension.

**Eg at λ = 4 — the unique remaining candidate.** Dimension 2, even parity. ✓ Torsion annihilation: T · v_Eg = 0 exactly for all v ∈ Eg (proven in Paper #56 and verified to machine precision). ✓ Face content: 100% square, 0% hexagonal — Eg lives entirely on the void interface, providing maximal coupling to T₁u(r₁) (left-handed, 62% square content) and reduced coupling to T₁u(r₂) (right-handed, 38% square content). ✓ Eigenvalue: λ_Eg = 4 equals the degree of the square faces (each square borders 4 hexagons) and equals √(r₁r₂), the geometric mean of the fermion eigenvalues — a structural connection to the fermion sector. ✓

No other mode satisfies all criteria simultaneously. Eg is the unique electroweak candidate. □

**Remark on the charged/neutral structure.** The 2 Eg modes provide the charged W± pair. The neutral component W³ arises from the Eg–A₁g(0) mixing sector: the square-face projection of the A₁g(0) mode is the hypercharge direction, and Eg–A₁g mixing after SSB produces the massive Z and the massless photon γ. The total electroweak boson count is 2 (charged, from Eg) + 2 (neutral, from mixing) = 4, matching SU(2)×U(1).

---

## 4. Theorem 58.2 — T₂g Is the Unique Colour Candidate

**Theorem 58.2 (Colour Placement).** *Of all even-parity modes in the face Laplacian spectrum, T₂g is the unique candidate for the colour (strong force) sector.*

**Proof.** After Theorem 58.1 assigns Eg to the electroweak sector, the remaining even-parity modes are: A₁g(0), T₂g, A₁g(7).

**A₁g at λ = 0 — excluded.** Dimension 1. The colour sector requires dimension ≥ 3 (SU(3) has 3 colour charges and 8 = C_A²−1 gluons). A singlet cannot carry colour charge. Excluded by dimension.

**A₁g at λ = 7 — excluded.** Dimension 1. Same argument. The A₁g at λ = 7 is the colour-singlet trace mode — it transforms trivially under the colour sector. Excluded by dimension.

**T₂g at λ = 7 — the unique remaining candidate.** Dimension 3, even parity. ✓ Torsion-active: the torsion operator T acts nontrivially on T₂g, providing the inter-generation mixing required for colour interactions. ✓ Face content: exactly 100% hexagonal (the square subspace carries no T₂g component) — the T₂g modes are confined to the bubble surface, the geometric statement of colour confinement: gluons do not propagate through the void (they are not observed as free particles). ✓ The 3 T₂g directions provide C_A = 3 colour charges, yielding C_A²−1 = 8 generators of SU(3) acting on the colour triplet. ✓

No other mode satisfies the criteria. T₂g is the unique colour candidate. □

**Remark on C_A = 3.** The colour number C_A = 3 is independently derived from the face structure: C_A = F_hx/F − 1 = 8/14 − 1 ... [correction: C_A = dim(T₂g) = 3, matching the three torsion directions of the hexagonal subspace]. The number of gluons C_A²−1 = 8 matches the eight generators of SU(3). The A₁g(7) singlet is the colour-singlet trace, completing the T₂g⊕A₁g decomposition at eigenvalue 7 to total dimension 4.

---

## 5. The Weinberg Angle — Exact Formula, Exact Identity, Open Derivation

**Result 58.3 (Weinberg Angle Formula — Tier 2).** *The Weinberg angle at the on-shell (LEP effective) scale is:*

*sin²θ_W = (Δ − C_A√Δ) / (Δ + C_A) = (17 − 3√17) / 20 = 0.23153*

*Every quantity is a cell integer (Δ = 17, C_A = 3). The formula matches the LEP effective value at 0.00σ. Its derivation from the Eg–A₁g mixing geometry is incomplete; the status is a precise match with a structural identity, not a theorem.*

**What is established.** The mixing angle involves the two sectors placed by Theorem 58.1: Eg (weak, 100% square content) and A₁g(0) (electromagnetic, square content F_sq/F = 3/7), coupled through the fermion sector T₁u(r₁), whose square content is s₁ = (1 + 1/√Δ)/2 = (√Δ + 1)/(2√Δ) ≈ 62.1%.

**The exact identity.** The formula is algebraically equivalent to:

cos²θ_W = C_A(√Δ + 1)/(Δ + C_A) = 2·C_A·√Δ·s₁/(Δ + C_A)

That is: the cosine-squared of the Weinberg angle is the T₁u(r₁) square content s₁, weighted by C_A√Δ (the colour number times the spectral gap) and normalised by Δ + C_A. This identity is exact and ties the Weinberg angle directly to the same eigenvector content that controls chirality (Paper #57 v2.0). It is the structural fingerprint the eventual derivation must reproduce.

**What is NOT established.** The naive overlap products do not give the formula. Taking g² ∝ s₁ (fermion–Eg overlap) and g'² ∝ s₁·(3/7) + (1−s₁)·(4/7) (fermion–A₁g overlap over both face types) yields sin²θ_W = 0.437, not 0.232. Version 1.0 of this paper acknowledged this ("this naive product misses the eigenvalue weighting"), then presented an intermediate spectral expression that evaluates to 1/(1+√17) ≈ 0.195 — also not the result — before asserting the final formula via an unspecified "heat kernel expansion". That presentation was a placeholder, not a proof, and is withdrawn in this version.

**The open problem, stated precisely.** Derive the weighting that takes the placed sectors (Eg, A₁g(0), T₁u(r₁)) to the coupling ratio g'²/(g² + g'²) = (Δ − C_A√Δ)/(Δ + C_A); equivalently, derive the factor C_A√Δ multiplying s₁ in the identity above, and the normalisation Δ + C_A. Until that step exists, Result 58.3 is Tier 2: an exact cell-integer match with a proven structural identity and an unproven mixing derivation.

**Experimental comparison:**
- LEP effective leptonic sin²θ_eff = 0.23153 ± 0.00016 → **0.00σ**
- MS-bar sin²θ_W(M_Z) = 0.23122 ± 0.00004 → **7.75σ** (scheme difference; the physical shift between the effective and MS-bar definitions is 0.00031)

The scheme identification (foam formula = on-shell LEP effective) is physically motivated (§17.2 of *From Foam to Fermions*: the single-cell computation at k = 0 contains no virtual-momentum loops to subtract) but, like the mixing derivation, is not proved from first principles. Both belong to the lattice-to-continuum programme.

---

## 6. The D₃ Result: Gauge Symmetry at the Cell Level

### 6.1 Computation

We computed the representation matrices of O_h 90° rotations (C₄ operations around the x, y, z axes) projected onto the 2-dimensional Eg subspace, using the standard basis {u, v} = {3z²−r², x²−y²}.

The results:

D(R_z^{90°}) = [[1, 0], [0, −1]]

D(R_x^{90°}) = [[−1/2, −√3/2], [−√3/2, 1/2]]

D(R_y^{90°}) = [[−1/2, √3/2], [√3/2, 1/2]]

**Key properties:**

(i) All three matrices have determinant −1 and eigenvalues {+1, −1}. They are **reflections**, not rotations. Each squares to the identity: D² = I.

(ii) The products D_x · D_y, D_y · D_z, D_z · D_x are rotations by 120° (trace = −1, (D_x D_y)³ = I).

(iii) **All three commutators are identical:**

[D_x, D_y] = [D_y, D_z] = [D_z, D_x] = √3 · J

where J = [[0, −1], [1, 0]] is the standard antisymmetric unit.

### 6.2 Interpretation

The Eg subspace carries the **dihedral group D₃ ≅ S₃** (order 6), not SU(2). The three C₄ rotations of O_h act as reflections on Eg because Eg descends from the j = 2 angular momentum sector: a 90° physical rotation maps x²−y² → −(x²−y²) (a sign flip, not a rotation in the Eg plane).

**SU(2) requires** three generators with cyclic commutators: [J_a, J_b] = iε_{abc} J_c. The degenerate commutator structure (all three commutators identical) violates this. The Casimir eigenvalue J² = 3I corresponds to j(j+1) = 3, giving j = (−1+√13)/2 ≈ 1.303, which is not an integer or half-integer and therefore not a valid SU(2) representation.

**This result is not a problem for the framework.** The SU(2) gauge group in the Standard Model is a continuous symmetry. The truncated octahedron has only discrete O_h symmetry. The continuous gauge group emerges in the continuum limit as the BCC lattice recovers continuous rotational symmetry — exactly as in standard lattice gauge theory, where the lattice has only discrete gauge links and the continuous gauge group appears in the continuum limit.

The placement theorems (Theorems 58.1 and 58.2) work by exhaustion of the discrete spectrum and do not require SU(2) at the cell level. The emergence of SU(2) from D₃ in the continuum limit is part of the lattice-to-continuum programme (Gap 2).

### 6.3 Why D₃ → SU(2) in the Continuum

The D₃ group on a single cell becomes SU(2) on the lattice through the standard mechanism:

(i) **O_h → O(3) in the continuum.** The BCC lattice with O_h point symmetry flows to full rotational symmetry O(3) as the lattice spacing a → 0. The first lattice artefact appears at O(a⁴) from the quartic invariant x⁴+y⁴+z⁴ (established by standard lattice QCD arguments).

(ii) **Eg → fundamental of SU(2).** The Eg irrep of O_h, which carries D₃, is the restriction of the j = 2 representation of SO(3) to the octahedral subgroup. On the lattice, the link variables U_{ij} connecting neighbouring cells transform under the PRODUCT representation of O_h on the two cells. The product Eg ⊗ Eg decomposes as A₁g ⊕ A₂g ⊕ Eg, and the A₁g singlet provides the gauge-invariant plaquette action. In the continuum limit, this becomes the standard Wilson gauge action for SU(2), with the coupling g² determined by the eigenvalue ratio.

(iii) **The dihedral D₃ structure carries enough information.** D₃ is a subgroup of SU(2) (specifically, it is the binary dihedral group in its lift to SU(2)). The three reflections become the three Pauli matrices σ_x, σ_y, σ_z when the discrete symmetry is embedded in the continuous group. The degenerate commutator structure at the cell level splits into the correct cyclic structure [σ_a, σ_b] = 2iε_{abc}σ_c when intermediate lattice points are included.

The precise proof of D₃ → SU(2) belongs to the lattice-to-continuum programme and is not claimed as complete here.

---

## 7. Complete Placement Summary

With Theorems 57.1, 57.2, 58.1, and 58.2, the particle–irrep assignments are established by exhaustion (given the selection criteria of Section 2):

| Irrep | Assignment | Proof | Status |
|-------|-----------|-------|--------|
| A₁g(0) | Photon/gravity | Only zero eigenvalue (massless) | Tier 1 (Thm 4.1) |
| T₁u(r₁) | Left-handed fermions | Only odd triplet; labelling per Cor. 57.2a | Tier 1 given Eg-coupling identification |
| Eg | Electroweak bosons | Only even doublet; T·v = 0; 100% square | **Tier 1 (Thm 58.1)** |
| T₁u(r₂) | Right-handed fermions | Galois conjugate of r₁; labelling per Cor. 57.2a | Tier 1 given Eg-coupling identification |
| T₂g | Gluons (colour) | Only even triplet; torsion-active; hex-confined | **Tier 1 (Thm 58.2)** |
| A₁g(7) | Colour-singlet trace | Only remaining singlet at λ = 7 | Tier 1 |
| A₂u | Higgs | Only negative T_hex charge (−1) | Tier 1 (Thm 57.1 v2.0) |

Result 58.3 (the Weinberg angle formula) is deliberately excluded from this table: it is a Tier 2 match with an open derivation (Section 5).

**The identification conjecture is closed** (given the Section 2 criteria and the Eg-coupling identification for the chirality labelling). The particle–irrep map is unique: no alternative assignment is compatible with the face Laplacian spectrum.

The remaining open question is the lattice-to-continuum proof (Gap 2): the demonstration that the long-wavelength effective field theory of the BCC foam is the Standard Model, not merely that the single-cell spectrum matches the SM particle content.

---

## 8. What Remains Tier 2

With the placement theorems established, the Tier 2 items reduce to:

| Observable | Status | What's needed |
|-----------|--------|--------------|
| sin²θ_W = (17−3√17)/20 | Tier 2 (Result 58.3) | Mixing-weight derivation of C_A√Δ·s₁ normalisation (Section 5) |
| α⁻¹ = 137.036... | Tier 2 | Heat kernel derivation rigour; Cs/Rb resolution |
| α_s = 0.11799 | Tier 2 | Torsion Green's function computation |

The fine structure constant α and strong coupling α_s remain Tier 2 because their derivations involve the heat kernel expansion and torsion Green's function respectively — multi-step calculations whose individual steps are verified but whose connection to the cell geometry is less direct than the placement theorems. Promoting these to Tier 1 requires the lattice-to-continuum programme.

---

## 9. Numerical Verification

The following Python script verifies all key computations in this paper:

```python
import numpy as np

# Build truncated octahedron face Laplacian
sq = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], dtype=float)
hx = np.array([[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],
               [-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]], dtype=float)/np.sqrt(3)
normals = np.vstack([sq, hx])

A = np.zeros((14,14))
for i in range(6):
    for j in range(6,14):
        if hx[j-6][np.argmax(np.abs(sq[i]))] * sq[i][np.argmax(np.abs(sq[i]))] * np.sqrt(3) > 0:
            A[i,j] = A[j,i] = 1
for i in range(6,14):
    for j in range(i+1,14):
        if np.sum(np.abs(hx[i-6]*np.sqrt(3) - hx[j-6]*np.sqrt(3)) > 0.5) == 1:
            A[i,j] = A[j,i] = 1

L = np.diag(A.sum(axis=1)) - A
eigvals, eigvecs = np.linalg.eigh(L)
print(f"Spectrum: {np.round(eigvals, 4)}")

# Find Eg eigenvectors
idx_Eg = np.where(np.abs(eigvals - 4) < 0.01)[0]
E_g = eigvecs[:, idx_Eg]
print(f"Eg square content: {np.sum(E_g[:6]**2):.6f} (should be 2.0)")
print(f"Eg hex content: {np.sum(E_g[6:]**2):.6f} (should be 0.0)")

# Torsion annihilation
P_sq = np.zeros((14,14)); P_sq[:6,:6] = np.eye(6)
P_hx = np.zeros((14,14)); P_hx[6:,6:] = np.eye(8)
T = P_sq @ L @ P_hx - P_hx @ L @ P_sq
for i in range(2):
    print(f"|T·e_Eg{i}| = {np.linalg.norm(T @ E_g[:,i]):.2e} (should be 0)")

# D₃ representation matrices
def face_perm(R):
    P = np.zeros((14,14))
    rot = (R @ normals.T).T
    for i in range(14):
        for j in range(14):
            if np.allclose(rot[i], normals[j], atol=1e-8):
                P[j,i] = 1; break
    return P

Rz = np.array([[0,-1,0],[1,0,0],[0,0,1]], dtype=float)
Rx = np.array([[1,0,0],[0,0,-1],[0,1,0]], dtype=float)
Ry = np.array([[0,0,1],[0,1,0],[-1,0,0]], dtype=float)

for name, R in [("Rz90",Rz),("Rx90",Rx),("Ry90",Ry)]:
    D = E_g.T @ face_perm(R) @ E_g
    print(f"D({name}): det={np.linalg.det(D):.4f}, D²=I: {np.allclose(D@D, np.eye(2))}")

Dz = E_g.T @ face_perm(Rz) @ E_g
Dx = E_g.T @ face_perm(Rx) @ E_g
Dy = E_g.T @ face_perm(Ry) @ E_g
comm_xy = Dx@Dy - Dy@Dx
comm_yz = Dy@Dz - Dz@Dy
comm_zx = Dz@Dx - Dx@Dz
print(f"All commutators equal: {np.allclose(comm_xy, comm_yz) and np.allclose(comm_yz, comm_zx)}")
print(f"(DxDy)^3 = I: {np.allclose((Dx@Dy) @ (Dx@Dy) @ (Dx@Dy), np.eye(2))}")

# Weinberg angle
Delta = 17; C_A = 3
sw2 = (Delta - C_A*np.sqrt(Delta)) / (Delta + C_A)
print(f"sin²θ_W = {sw2:.5f} (should be 0.23153)")
```

All results verified to machine precision. The script runs in under 1 second.

---

## 10. Conclusion

The gauge sector of the Standard Model is not assumed — it is forced by the geometry of the truncated octahedron, given the selection criteria of Section 2. The Eg irrep is the unique electroweak candidate (Theorem 58.1) and T₂g is the unique colour candidate (Theorem 58.2) by exhaustion of all even-parity modes against structural criteria (torsion behaviour, face content, dimensionality). The Weinberg angle formula sin²θ_W = (17 − 3√17)/20 matches the LEP effective value at 0.00σ and satisfies the exact identity cos²θ_W = 2C_A√Δ·s₁/(Δ + C_A); its derivation from the mixing geometry remains open (Result 58.3, Section 5).

The continuous gauge group SU(3)×SU(2)×U(1) emerges in the continuum limit. At the single-cell level, the Eg subspace carries the dihedral group D₃ ≅ S₃, not SU(2) — a result we report as a computational finding, not a problem. The relationship D₃ → SU(2) in the continuum limit follows standard lattice gauge theory arguments but has not been proved in full rigour for this specific system. This belongs to the lattice-to-continuum programme (the remaining open question for the framework).

With this paper, the complete particle–irrep map of the framework is established as a set of theorems. The identification conjecture is closed.

---

*Priority Date: 20 February 2026 · UFFT Paper #58 · April 2026*

## References

[1] Luke Martin, *UFFT Paper #56, Torsion T1u Theorems*. DOI: 10.5281/zenodo.19484354.
[2] Luke Martin, *UFFT Paper #57, Necessity of the Standard Model (v2)*. DOI: 10.5281/zenodo.21323321.
[3] Luke Martin, *UFFT Paper #58, Gauge-Sector Placement (v1, superseded)*. DOI: 10.5281/zenodo.19484967.

*AI Disclosure: Numerical computations performed with Claude (Anthropic). All theoretical arguments and physical identifications: Luke Martin.*

**B + V = D**

*Unified Foam Field Theory · Paper #58 · DOI: 10.5281/zenodo.21323498 · Priority Date: 20 February 2026*

*B + V = D*
