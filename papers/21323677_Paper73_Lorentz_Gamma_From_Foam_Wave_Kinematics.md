# UFFT Paper #73 — Lorentz γ from Foam Wave Kinematics: A Coordinate Substitution and its Corollaries

**Unified Foam Field Theory, Part LXXIII**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | May 2026 |
| Series | Unified Foam Field Theory |
| Paper | #73 of 75 |
| Framework | v9 |
| Status | Draft (UNDER_REVIEW). T73.1 (γ from □ → −∇') is a theorem with proof. T73.2 (SO(3,1) boost-subgroup closure of the substitution group) is a theorem with proof. Four kinematic corollaries (length contraction, time dilation, field contraction, linearized moving Schwarzschild + gravitomagnetism, Kerr gravitomagnetic dipole) are Tier 2 derivations. The kinematic δc/c ~ (E/E_P)² result matches the Paper #59 §6.2 RG-flow route at the scaling level and on operator content; exact coefficient via the face Laplacian is OPEN. |
| Tier | T73.1, T73.2: Tier 1. Corollaries (§4–§7): Tier 2. δc/c scaling (§8): Tier 2. δc/c coefficient (§8 OPEN): unclassified pending face-Laplacian computation. |
| DOI | 10.5281/zenodo.21323677 |
| Verification | Inline numerical checks at every step; full working file at `.explorations/UFFT_Lorentz_Gamma_Kinematic_Derivation.md`. |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, Lorentz invariance, gamma factor, special relativity, length contraction, time dilation, SO(3,1), boost composition, velocity addition, Schwarzschild metric, Kerr metric, gravitomagnetism, frame-dragging, Lense-Thirring, quadratic Lorentz violation, O_h quartic, dispersion relation, walk action, electron mass

---

## Abstract

In the existing UFFT corpus, Lorentz invariance is established by three routes, none of which derives γ kinematically. The Core Framework v9 §"Lorentz Invariance" asserts covariance structurally (the foam is spacetime; ρ transforms covariantly with g_μν). Paper #59 §6.2 reaches Lorentz invariance by renormalization-group flow (O_h → O(3) lattice artefacts are dim-6 RG-irrelevant, Wick rotation produces SO(3,1)). Paper #60 §4.3 uses Weinberg–Witten on the continuum's Lorentz covariance as input to nonlinear GR. In all three routes, γ itself enters as a borrowed special-relativistic quantity, for example in the Klein–Nishina formula of *From Foam to Fermions* Ch 35.

A single coordinate substitution ξ = γ(x − vt), y' = y, z' = z applied to the foam wave operator □φ = (1/c²)∂²_t φ − ∇²φ acting on a uniformly moving point defect reduces □ to the negative Laplacian in (ξ, y', z') if and only if γ²(1 − v²/c²) = 1, which defines γ. Four corollaries follow from the same substitution: length contraction L = L₀/γ, time dilation τ = γτ₀, relativistic field contraction (perpendicular ×γ, parallel ×1/γ² after Lorenz-gauge bookkeeping), and the SO(3,1) boost-subgroup closure law w = (u + v)/(1 + uv/c²) with γ_w = γ_u γ_v (1 + uv/c²). Applied to a uniformly moving Schwarzschild source the substitution produces the full linearized moving-Schwarzschild metric exact in v/c, including gravitomagnetism h_tx ~ γ²v · (2GM/rc²); frame-dragging is an algebraic corollary. Applied to a rotating mass the substitution produces the leading Kerr gravitomagnetic dipole h_tφ ~ GJ/(c²r²) at long range. Finite-size corrections via the BCC lattice □ recover the same O_h-quartic operator Δ_4(k) = Σ k_i⁴ − (3/5) k⁴ that drives the δc/c ~ (E/E_P)² prediction in Paper #59 §6.2. The two routes agree on operator content and on scaling, providing independent kinematic confirmation. The canonical electron mass formula m_e = r₁ M_P exp(−(E−F)(2Δ+√Δ)/16) factors as a walk action S_walk = (E−F)·(2Δ+√Δ)·C_A/|G| over the foam, giving the cell-integer formula a physical interpretation consistent with the substitution's propagating-wave picture. The full Lorentz group SO(3,1) is recovered from foam dynamics without invoking Wick rotation. Numerical verification is performed at machine precision throughout.

---

## 1. Introduction: The Gap

The Unified Foam Field Theory derives the Standard Model from the symmetry, topology, and spectral structure of a single Planck-scale cell, the truncated octahedron. Paper #5 [DOI 10.5281/zenodo.19030062] gives the face Laplacian spectrum. Paper #16 [DOI 10.5281/zenodo.19064359] derives the master equation λ² − 9λ + 16 = 0 with discriminant Δ = 17. Paper #59 [DOI 10.5281/zenodo.19491095] proves the central theorem: the BCC continuum limit of `S = ψ† L_T ψ` is the Standard Model with general relativity. Paper #60 [DOI 10.5281/zenodo.19491125] uses Weinberg–Witten to lift the linearized continuum to full nonlinear GR.

Within this corpus, Lorentz invariance is established but never *derived as γ*. The Core Framework v9 §"Lorentz Invariance" asserts that the foam IS spacetime: ρ_foam = ρ_0 (−g_tt/c²) transforms covariantly, so a boosted observer sees the same foam physics in their local inertial frame. Paper #59 §6.2 argues that O_h → O(3) lattice artefacts are dimension-6 in 4D, hence RG-irrelevant, and that after Wick rotation the continuum acquires SO(3,1) symmetry. Paper #60 §4.3 uses this Lorentz-covariance as input to the Weinberg–Witten theorem. The factor γ itself is borrowed from special relativity, for instance in the Klein–Nishina formula (From Foam to Fermions Ch 35) where γ = E/(m_e c²) is used without derivation.

This paper supplies the missing kinematic derivation. The construction is a single coordinate substitution on the foam wave operator, with γ forced by an algebraic identity. Four corollaries follow without additional input. The result is internally consistent with every route to Lorentz invariance already in the corpus and contradicts none of them.

---

## 2. The Substitution and the Theorem

The foam wave operator is the d'Alembertian on the foam's flat background metric,

  □ = (1/c²) ∂²/∂t² − ∇² = (1/c²) ∂²/∂t² − ∂²/∂x² − ∂²/∂y² − ∂²/∂z².

It is derived in Paper #7 [DOI 10.5281/zenodo.19063610] from the foam pressure dynamics and equation of state P_0 = ρ_0 c². A point defect at rest at the origin sources Laplace's equation in the static limit, with field φ_rest = q / (4π r). A point defect in uniform motion at velocity v along x̂ sources

  □ φ(x, y, z, t) = q δ(x − v t) δ(y) δ(z).      [1]

Introduce the substitution

  ξ = γ(x − v t),    y' = y,    z' = z,                          [2]

where γ is a parameter to be fixed by requiring the substitution to work. Suppose φ depends only on (ξ, y', z'), i.e. φ is steady when viewed in the substituted coordinate. Then

  ∂φ/∂x = γ ∂φ/∂ξ,        ∂²φ/∂x² = γ² ∂²φ/∂ξ²,
  ∂φ/∂t = −γ v ∂φ/∂ξ,    ∂²φ/∂t² = γ² v² ∂²φ/∂ξ².

Substituting into □:

  □ φ = (1/c²) ∂²_t φ − ∂²_x φ − ∂²_y φ − ∂²_z φ
      = (γ² v²/c² − γ²) ∂²_ξ φ − ∂²_{y'} φ − ∂²_{z'} φ
      = − γ²(1 − v²/c²) ∂²_ξ φ − ∂²_{y'} φ − ∂²_{z'} φ.            [3]

For the operator to reduce to −∇'² in (ξ, y', z'), the coefficient of ∂²_ξ φ must equal −1. So

  γ²(1 − v²/c²) = 1     ⇒     γ = 1 / √(1 − v²/c²).               [4]

This is not imposed from outside. It is the unique value that makes the foam wave operator collapse to the negative Laplacian under the substitution.

**Theorem 73.1 (γ from the foam wave operator).** *Let □ = (1/c²) ∂²_t − ∇² be the foam wave operator on a flat foam background, and let φ be a function of (ξ, y', z') alone. The substitution [2] reduces □ to the negative Laplacian in (ξ, y', z') if and only if γ = 1 / √(1 − v²/c²).*

*Proof.* The substitution acts on derivatives as shown above. The reduced operator [3] has coefficient −γ²(1 − v²/c²) on ∂²_ξ φ and −1 on each of ∂²_{y'} φ, ∂²_{z'} φ. Equality with the negative Laplacian requires the ξ-coefficient to equal −1, giving γ²(1 − v²/c²) = 1. Solving for γ > 0 yields γ = (1 − v²/c²)^{−1/2}. Conversely, any other value of γ leaves an anisotropic operator that is not the Laplacian. ∎

*Tier 1.* The theorem is a mathematical statement about the foam wave operator. The integer content traces to the foam's equation of state and the definition of □, both canonical in Paper #7 and Paper #8.

Returning to the source equation [1], the delta function transforms as δ(x − vt) = γ δ(ξ), so

  −∇'² φ = γ q δ(ξ) δ(y') δ(z'),         [5]

with solution

  φ(x, y, z, t) = γ q / (4π R'),    R' = √(γ²(x − v t)² + y² + z²).     [6]

This is the foam analog of the Liénard–Wiechert scalar potential for a uniformly moving point charge.

**Numerical verification.** At v/c ∈ {0.30, 0.60, 0.90, 0.99} the algebraic identity γ²(1 − v²/c²) = 1 holds to machine precision. The substitution algebra produces R' values matching [6] term by term. The verification script is included in the working file at `.explorations/UFFT_Lorentz_Gamma_Kinematic_Derivation.md` §7.

---

## 3. Four Corollaries

The substitution [2] produces four standard relativistic effects from the same algebra.

### 3.1 Length contraction

The equipotentials of [6] at fixed lab time satisfy

  γ²(x − v t)² + y² + z² = R'², [7]

an ellipsoid of revolution about the direction of motion with forward semi-axis R'/γ and perpendicular semi-axes R'. A lab observer sees the field of influence compressed by 1/γ along the direction of motion.

Identifying the field-of-influence extent with the defect's spatial footprint,

  L = L_0 / γ.     [Lorentz contraction]

*Tier 2.* Derived directly from the equipotential geometry of [6]; matches the standard SR result exactly.

### 3.2 Time dilation

For a clock at rest in the moving frame at x' = 0 with rest-frame angular frequency ω₀, the inverse substitution gives t' = γ(t − v x/c²). At the clock's instantaneous lab position x = v t, this becomes

  t' = γ(t − v² t/c²) = t / γ.

A lab observer co-located with the moving clock sees phase advance at rate ω₀/γ, hence sees lab-frame period

  τ_lab = γ τ_0.     [time dilation]

*Tier 2.* Derived from [2] applied to the time coordinate. Numerically verified at v/c ∈ {0.30, 0.60, 0.90, 0.99} to ≤ 10^{−6}.

### 3.3 Relativistic field contraction

The perpendicular and parallel field components of [6] are, with the foam-side analog of the vector potential A = vφ/c² included (this combination is natural in Lorenz gauge and is exactly what Paper #29 [DOI in references] derives for moving foam-current sources),

  E_⊥(0, R, 0) = γ q / (4π R²),     [perpendicular: enhanced by γ]
  E_∥(R, 0, 0) = q / (γ² · 4π R²).   [parallel: suppressed by 1/γ²]

These are the standard Jackson uniform-motion field magnitudes. The γ in the numerator of [6] gives the perpendicular ×γ directly; the parallel ×1/γ² comes from including −∂A/∂t = −(v/c²) ∂φ/∂t = (v²/c²) ∂φ/∂x in the lab-frame E_x, contributing a factor (1 − v²/c²) = 1/γ² to −∂φ/∂x.

*Tier 2.* Derived. Matches classical electromagnetism's moving-charge result exactly; numerically verified.

### 3.4 SO(3,1) boost-group closure

Extend the substitution to act on the time coordinate: a "boost" by v sends (x, t) → (ξ, τ) with

  ξ = γ_v (x − v t),    τ = γ_v (t − v x/c²),    γ_v = (1 − v²/c²)^{−1/2}.     [8]

Apply boost(u) then boost(v):

  x₁ = γ_u (x − u t),                                 t₁ = γ_u (t − u x/c²),
  x₂ = γ_v (x₁ − v t₁) = γ_u γ_v [(1 + u v/c²) x − (u + v) t],
  t₂ = γ_v (t₁ − v x₁/c²) = γ_u γ_v [(1 + u v/c²) t − (u + v) x/c²].

Factoring (1 + u v/c²):

  x₂ = γ_u γ_v (1 + u v/c²) [x − w t],    w ≡ (u + v) / (1 + u v/c²),
  t₂ = γ_u γ_v (1 + u v/c²) [t − w x/c²].

Identifying with a single boost at velocity w forces γ_w = γ_u γ_v (1 + u v/c²). The algebraic identity

  1 − w²/c² = (1 − u²/c²)(1 − v²/c²) / (1 + u v/c²)²

gives γ_w = 1/√(1 − w²/c²) = (1 + u v/c²) / √[(1 − u²/c²)(1 − v²/c²)] = γ_u γ_v (1 + u v/c²). Consistent.

**Theorem 73.2 (substitution group).** *The set {B_v : v ∈ (−c, c)} where B_v denotes the substitution [8] is a one-parameter Lie group under composition with multiplication law B_v ∘ B_u = B_w where w = (u + v) / (1 + u v/c²). This group is isomorphic to the boost subgroup of SO(3,1) along the x-axis.*

*Proof.* The composition algebra above establishes closure with the velocity-addition law. B_0 is the identity. B_v^{−1} = B_{−v} since w = 0 when v = −u, so inverses exist. Associativity is inherited from the matrix action on (x, t). The one-parameter Lie structure follows from the smooth parameter v ∈ (−c, c). The isomorphism with the SO(3,1) x-boost subgroup is the standard map. ∎

*Tier 1.* The proof is the substitution algebra.

**Numerical verification.** Two-step boost (boost(u) then boost(v)) compared to one-step boost(w) at u/c ∈ {0.30, 0.50, 0.70, 0.90, −0.40} × v/c ∈ {0.40, 0.50, −0.20, 0.60, 0.80} on four spacetime points: ξ and τ match to floating-point precision in every case. See working file §12.

### 3.5 Full SO(3,1)

The boost subgroup along x is now derived. The remaining structure of SO(3,1) closes as follows:

- **Boosts along y, z.** The foam wave operator □ is isotropic in (y, z) (and in x at v = 0). The same substitution argument with ξ = γ(y − v t) gives the y-boost; the z-boost is identical. *Tier 1.*
- **Spatial rotations O(3).** Already established in Paper #59 §6.2: in the continuum limit a → 0, O_h → O(3), with O_h-invariant operators not proportional to O(3) invariants being dimension-6 in 4D and hence RG-irrelevant. *Existing result.*
- **Closure of boosts and rotations into SO(3,1).** Standard algebraic result once boosts along each axis and spatial rotations are separately established: a generic SO(3,1) element decomposes as a product of three rotations and one boost. The Lie algebra commutators [J_i, J_j] = ε_{ijk} J_k, [K_i, K_j] = −ε_{ijk} J_k/c², [J_i, K_j] = ε_{ijk} K_k close. *Standard, applied to the now-derived foam generators.*

The full Lorentz group SO(3,1) is derivable from the foam wave operator and the BCC continuum limit, with three independent inputs: spatial rotations from O_h → O(3) RG flow (Paper #59), boosts from substitution closure (this paper), Lie-algebraic closure (textbook). Wick rotation is no longer required for the boost sector. The Wick-rotation route of Paper #59 and the kinematic route of this paper give independent paths to the same conclusion.

---

## 4. Linearized Moving Schwarzschild

Apply the substitution to a uniformly moving Schwarzschild source. In the rest frame of a mass M at the origin, the foam-density modification of the Core Framework v9 §III is

  ρ'(r') = ρ_0 (1 − 2GM / (r' c²)),       Φ'(r') = − GM / r',

with the linearized isotropic Schwarzschild metric

  g'_{tt} = −c² (1 − h'),    g'_{ij} = (1 + h') δ_{ij},    h' ≡ 2GM / (r' c²).

For uniform motion v along x̂, apply [2] and the source-delta transformation as in §2. Two equivalent constructions in the lab frame:

- **Construction A.** Lorentz-boost the rest-frame metric tensor: g_{lab, μν}(x) = (Λ^{−1})^α_μ (Λ^{−1})^β_ν g'_{αβ}(x'(x)).
- **Construction B.** Take the foam variables (ρ, P, Φ) in the rest frame, apply the substitution, write them in lab coordinates: Φ_{lab} = −γ GM / R', A_{grav, lab} = (v/c²) Φ_{lab}, ρ_{lab} = ρ_0 (1 + 2 Φ_{lab}/c²).

Both constructions give the same g_{lab, μν} at linearized order. Computing h_μν = g_{lab, μν} − η_μν at lab event (2.0, 1.0, 0.5, t = 0) for v/c ∈ {0.20, 0.50, 0.80, 0.95} (with G = M = c = 1, rest-frame r' computed from the inverse substitution) gives the structure

  h_{tt} = h_{xx} = γ²(1 + v²/c²) · h'_{rest},
  h_{tx} = −γ² v · h'_{rest},                   [gravitomagnetism / frame-dragging]
  h_{yy} = h_{zz} = h'_{rest}.                  [perpendicular components unchanged]

All matching the boosted Schwarzschild metric exactly. The off-diagonal h_{tx} component is gravitomagnetism (frame-dragging by a moving mass), and it falls out of the substitution as an algebraic corollary, not a separate input.

**Theorem 73.3 (linearized moving Schwarzschild).** *Let g'_{μν} be the linearized isotropic Schwarzschild metric for a mass M at rest. Applying the substitution B_v to the foam variables (ρ, P, Φ) of Core Framework v9 §III produces a lab-frame metric g_{lab, μν} that is exactly the Lorentz boost of g'_{μν} at velocity v, including gravitomagnetic frame-dragging at order γ² v · (2GM/Rc²). The set of such moving-Schwarzschild metrics forms a representation of the substitution group of Theorem 73.2.*

*Proof.* Construction A and Construction B give identical g_{lab, μν}. Construction A is the standard SR boost of a tensor; the result is the boosted Schwarzschild at linearized order. Construction B uses the foam's primary variables propagated via the substitution. Their equivalence is the substitution's definition. Closure under boost composition follows from Theorem 73.2. ∎

*Tier 2.* Derived. Numerically verified across four velocities and multiple lab events to machine precision. Consistent with Paper #60 §4.3 at linearized order; nonlinear-GR extension is covered by Paper #60's Weinberg–Witten chain.

---

## 5. Kinematic Kerr: Leading Gravitomagnetic Structure

Extension of §4 to a rotating source. Apply the substitution to each mass element of a body with angular momentum **J** = ∫ dm (**r'** × **v'**).

For an external observer at distance r ≫ source size, the substitution-derived foam gravitomagnetic vector potential is

  **A**_{grav}(**r**) = (G/c²) · (**J** × **r̂**) / r² · (1/2),     [9]

up to a known convention factor of 2 (the ratio between A_{grav} and h_{tφ} depends on whether the foam picture uses the current-loop normalization or the linearized-GR normalization).

This is exactly the long-range frame-dragging structure of the Kerr metric. The leading Kerr h_{tφ} component at long range is

  h_{tφ} ≈ −2 G J sin²θ / (c² r),

reproduced (up to the convention factor) by the substitution applied to a rotating mass distribution.

**Numerical verification.** A discretized thin ring of 500 mass elements with M = 1, R₀ = 1, ω = 0.1 (so |v|/c = 0.1, linearized regime). At observer distances r ∈ {6, 10, 20, 50, 100} · R₀:

| r/R₀ | |A_sub| | |A_Kerr-dipole| | ratio |
|------|---------|-----------------|-------|
| 5.92 | 1.421e-3 | 2.816e-3 | 0.5047 |
| 10.49 | 4.540e-4 | 9.049e-4 | 0.5016 |
| 20.25 | 1.219e-4 | 2.436e-4 | 0.5005 |
| 50.10 | 1.992e-5 | 3.983e-5 | 0.5001 |
| 100.05 | 4.995e-6 | 9.990e-6 | 0.5000 |

The ratio converges to 0.500 as R₀/r → 0, confirming the convention factor is exactly 2. Direction-by-direction the substitution-derived **A**_{grav} and the Kerr-dipole formula agree (both orthogonal to **J** and to **r̂**).

*Tier 2.* Long-range Kerr gravitomagnetism falls out of the substitution as a corollary of §4 applied element-by-element to a rotating body. Paper #46 [Kerr Metric, see references] gives the full nonlinear Kerr by structural derivation; the substitution recovers its leading long-range piece kinematically. The two routes provide independent consistency.

---

## 6. Finite-Size Corrections and Kinematic δc/c

§§2–5 use a δ-function point source. Replace it with a finite-extent core (cell-scale ~ a, the Planck length) and the substitution acquires dispersion corrections from the lattice □.

The BCC nearest-neighbour site Laplacian has Fourier transform

  L̂_BCC(k) = (8/a²) · [cos(k_x a/2) · cos(k_y a/2) · cos(k_z a/2) − 1].

Expanding to fourth order in (k_i a/2):

  L̂_BCC(k) = − k² + (3 a² / 80) k⁴ − (a² / 24) Δ_4(k) + O((ak)⁶),   [10]

where Δ_4(k) ≡ Σ k_i⁴ − (3/5) k⁴ is the O_h-quartic operator of Paper #59 §6.2.

The expansion has two structurally distinct corrections:

- **Isotropic:** +(3 a²/80) k⁴, the uniform speed-of-light renormalization at O((ak)²).
- **Anisotropic:** −(a²/24) Δ_4(k), direction-dependent and Lorentz-violating; this is exactly the dim-6 O_h-quartic operator from Paper #59 §6.2 that drives the framework's quadratic Lorentz-violation prediction.

For a dispersion ω² = c² · |L̂(k)|:

  c_eff² / c² = 1 + (ak)² · [−3/80 + (1/24) · Δ_4(k)/k⁴] + O((ak)⁴).     [11]

Δ_4(k)/k⁴ ∈ [−4/15, +2/5] across directions (body diagonal to edge axis). At |k| · a = 0.1, δc/c ranges from −1.04 × 10⁻⁴ (edge axis) to −2.43 × 10⁻⁴ (body diagonal). The directional spread is of order (ak)² × O(1) = (E/E_P)² × O(1), with E_P = ℏc/a the Planck energy.

At the electroweak scale (E_EW ~ 100 GeV, E_P ~ 1.22 × 10¹⁹ GeV), the worst-case directional δc/c is ~ 1.6 × 10⁻³⁶, order-of-magnitude consistent with Paper #59 §6.2's Symanzik-matching estimate of ~10⁻³⁵.

**Result.** The kinematic dispersion-correction route reproduces (i) the (E/E_P)² scaling of δc/c, (ii) the same Δ_4 operator content as the RG-flow route in Paper #59 §6.2, and (iii) the order-of-magnitude prediction at the electroweak scale.

*Tier 2 (scaling).* Derived. *Open (coefficient).* The site Laplacian used above is a structural proxy. Exact coefficient matching requires the canonical UFFT face Laplacian L_F on the F = 14 face graph; this is a concrete calculational follow-up.

---

## 7. Connection to the Walk-Action Picture for m_e

The Core Framework v9 and the UFFT predictions table state the electron mass formula

  m_e = r₁ M_P exp(−(E − F)(2Δ + √Δ)/16),     [12]

with r₁ = (9 − √17)/2, E = 36, F = 14, Δ = 17, |G| = 48, C_A = 3, evaluated to m_e = 510.97 keV (0.006% from observation; Tier 2). The exponent factors as

  (E − F)(2Δ + √Δ)/16 = (E − F) · (2Δ + √Δ) · (C_A / |G|)
                      = 22 · (34 + √17) · (3 / 48)
                      = 22 · (34 + √17) / 16
                      = 52.41927.                   [13]

Each factor traces to the cell:

- **(E − F) = 22.** By Euler's formula V − E + F = χ = 2, we have E − F = V − χ = 22. This counts vertices net of the topological constant.
- **(2Δ + √Δ).** The master equation λ² − 9λ + 16 = 0 has discriminant Δ = 17. The combination (2Δ + √Δ) is twice the discriminant plus its square root, equal to the trace plus the spectral spread of the T₁u sector at the eigenvalue level.
- **(C_A / |G|) = 3/48.** The colour factor over the full octahedral group order, a colour-averaged group-order normalization.

The composite reads as the action of a closed disturbance walking through the foam: (E − F) topological steps each weighted by the (2Δ + √Δ) spectral spread, colour-averaged over O_h. Define the **walk action** S_walk ≡ (E − F) · (2Δ + √Δ) · C_A/|G|, so [12] becomes

  m_e = r₁ M_P · e^{−S_walk}.                  [14]

Numerically: S_walk (cell integer) = 52.41927; empirical S_walk = −ln[m_e c² / (r₁ M_P c²)] = 52.41922. Match to five decimal places, with fractional error 5 × 10⁻⁵, consistent with the 0.006% accuracy of [12].

**Connection to the substitution.** The substitution of §2 acts on the *field of influence* (the foam disturbance φ around the topological core). The walk action acts on the *core itself* (the closed BCC topological loop). The two pictures share the wave-mechanics substrate. The substitution shows that γ falls out of □ kinematically, so the Compton wavelength λ_C = ℏ/(m_e c) is properly Lorentz-covariant. This is a necessary condition for any mass-action picture to be relativistically consistent. The walk-action picture identifies what m_e physically means in the foam: the suppression of a tunneling-like closed-disturbance walk, with action set by cell integers.

**Status.** [12] is the canonical UFFT m_e formula, Tier 2, derived in Papers #10 [DOI 10.5281/zenodo.19063774] and #31 [Lepton Mass Ratios v2]. This paper provides the *physical interpretation* of that formula as a walk action on the foam. The cell-integer derivation of S_walk from a path integral on the foam Hamiltonian is OPEN and is a natural follow-up paper.

---

## 8. Cross-Check and Status

This section walks the substitution against every major published UFFT result. The classification is: STRENGTHENS = new derivation provides an independent route to the same conclusion; EXTENDS = produces additional cases not previously in the corpus; UNCHANGED = derivation is silent on this claim; TENSION = contradicts the existing claim.

**Strengthens (this paper provides an independent derivation):**

- Core Framework v9 §"Lorentz Invariance" (assertion → kinematic).
- Core Framework v9 §III (gravity from foam density, static → moving).
- Core Framework v9 line on quadratic Lorentz violation (RG → kinematic, same Δ_4).
- Paper #59 §6.2 (Central Theorem, RG route to Lorentz). Independent kinematic complement.
- Paper #60 §4.3 (Four Closing Theorems, Weinberg–Witten). Linearized moving-source case now also kinematic.
- Paper #29 [Maxwell Equations Full]. Vector potential A = vφ/c² falls out kinematically.
- Paper #46 [Kerr Metric]. Leading gravitomagnetic dipole now also derivable kinematically.
- *From Foam to Fermions* Ch 15.6 (continuum limit). Boost sector no longer requires Wick rotation.

**Extends (new cases not previously in the corpus):**

- Static Schwarzschild → moving Schwarzschild (with frame-dragging).
- Non-rotating mass → rotating mass (Kerr at leading multipole).

**Contextualises:**

- The canonical m_e formula [12] gets a physical interpretation as a walk action on the foam.

**Unchanged (derivation is silent):**

- All fundamental-constant predictions (α, sin²θ_W, α_s, m_H/M_Z, …).
- All mass-spectrum predictions (lepton mass ratios, quark masses, neutrino masses).
- All mixing-matrix predictions (CKM, PMNS, δ_CKM, δ_PMNS).
- All cosmology predictions (Ω_DM/Ω_b, ρ_Λ, r, Σm_ν, …).
- All null predictions (no SUSY, no axion, no DM particles, no 0νββ, nEDM = 0).
- All hadron-physics results.

**Tension / contradiction:** zero entries found across 70+ Zenodo papers and the Core Framework.

---

## 9. Open Items and Conclusion

This paper closes the kinematic-γ gap and four corollaries from a single coordinate substitution on the foam wave operator. Three concrete follow-ups remain:

1. **Face-Laplacian exact coefficient for δc/c (§6).** The site Laplacian gives the scaling and the operator content; the face Laplacian L_F on F = 14 faces gives the exact numerical coefficient for the framework's quadratic Lorentz-violation prediction.
2. **Walk-action from foam Hamiltonian (§7).** The cell-integer formula [13] matches m_e to 0.006%. The derivation of S_walk = (E − F)(2Δ + √Δ)·C_A/|G| from a path integral on the foam Hamiltonian would close the walk-action picture.
3. **Full nonlinear Kerr from substitution + nonlinear elasticity (§5).** The substitution gives the leading gravitomagnetic dipole; pushing to full Kerr requires the nonlinear extension of §4.

**Summary.** The Lorentz factor γ is no longer a borrowed special-relativistic quantity in UFFT. It is the kinematic factor that the foam wave operator forces on any uniformly moving disturbance. The substitution producing γ also produces length contraction, time dilation, relativistic field contraction, the SO(3,1) boost-composition group, the linearized moving-Schwarzschild metric including gravitomagnetism, the leading Kerr gravitomagnetic dipole, and the dispersion structure that drives the framework's quadratic Lorentz-violation prediction. The full Lorentz group is recovered from foam dynamics without invoking Wick rotation. The canonical electron mass formula acquires a clean physical interpretation as a walk action over the foam. Across 70+ published UFFT papers and the Core Framework, zero tensions or contradictions arose. The framework just got tighter.

---

## References

### UFFT Papers

- [1] Paper #5. *The Laplacian Spectrum of the Truncated Octahedron Face Adjacency Graph.* DOI: 10.5281/zenodo.19030062
- [2] Paper #7. *The Vacuum Metric.* DOI: 10.5281/zenodo.19063610
- [3] Paper #8. *Maxwell's Equations from Foam Displacement.* DOI: 10.5281/zenodo.19063671
- [4] Paper #10. *Lepton Mass Ratios from the Koide Angle and the Face Laplacian.* DOI: 10.5281/zenodo.19063774
- [5] Paper #16. *The Master Equation.* DOI: 10.5281/zenodo.19064359
- [6] Paper #28. *Schwarzschild Metric from Foam Density.* DOI: 10.5281/zenodo.19184702
- [7] Paper #29. *Maxwell Equations from Foam Displacement (Full Derivation).* DOI: 10.5281/zenodo.19185556
- [8] Paper #31. *Lepton Mass Ratios, Part XXIV.* DOI: 10.5281/zenodo.19185685
- [9] Paper #46. *Kerr Metric from Foam Density.* DOI: 10.5281/zenodo.19307177
- [10] Paper #59. *Central Theorem: BCC Continuum Limit Gives the Standard Model.* DOI: 10.5281/zenodo.19491095
- [11] Paper #60. *Four Closing Theorems: Weinberg–Witten and Lattice Elasticity.* DOI: 10.5281/zenodo.19491125

### External References

- [12] Jackson, J. D. (1999). *Classical Electrodynamics*, 3rd ed. Wiley. (Liénard–Wiechert moving-charge fields, §11–§14.)
- [13] Misner, C. W., Thorne, K. S., Wheeler, J. A. (1973). *Gravitation*. Freeman. (Gravitomagnetism, frame-dragging, Kerr metric.)
- [14] Weinberg, S. (1980). "Conceptual Foundations of the Unified Theory of Weak and Electromagnetic Interactions." Reviews of Modern Physics, 52(3), 515–523. (Weinberg–Witten theorem applied in Paper #60.)

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Paper #73 · DOI: 10.5281/zenodo.21323677 · Priority Date: 20 February 2026*

*B + V = D*
