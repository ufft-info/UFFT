"""
Paper #48 lattice-to-continuum probe:
O(k^2) dispersion fit within each O_h irrep block.

For each degenerate eigenspace of the isolated-cell face Laplacian L
(irrep block B with eigenvalue lambda, multiplicity m), we compute the
m x m matrix

    M^(B)(k) = P_B [ H(k) - L ] P_B

where H(k) is the Bloch Hamiltonian for the BCC-tiled Kelvin foam and
P_B is the projector onto block B.  Near k = 0, M^(B)(k) is quadratic
in k.  The most general O_h-invariant symmetric rank-2 k-form acting on
a triplet (T_1u or T_2g) has THREE independent coefficients:

    M_ij(k) = alpha |k|^2 delta_ij                (A_1g scalar)
            + beta  k_i k_j                        (T_2g / traceless-sym)
            + gamma delta_ij k_i^2  (no sum on i)  (E_g diagonal, O_h-only)

The alpha and beta pieces are already O(3)-invariant.  The gamma piece
is the O(3)-breaking O_h-anisotropy: if gamma != 0 within the triplet,
the O(k^2) dispersion is genuinely anisotropic and Paper #48's claimed
'continuum limit = Lorentz-invariant SM kinetic term' requires either
a Symanzik-improvement counter-term or a field redefinition to absorb
gamma.

Three linearly independent directions k = k_hat h give enough data to
solve for (alpha, beta, gamma):

    [100]: eigenvalues h^2 * {alpha, alpha, alpha + beta + gamma}
    [110]: eigenvalues h^2 * {alpha, alpha + gamma/2, alpha + beta + gamma/2}
    [111]: eigenvalues h^2 * {alpha + gamma/3, alpha + gamma/3,
                              alpha + beta + gamma/3}

We use the same Bloch construction as Symanzik_Matching_BCC.py (which
takes the k-dependent diagonal form H_ii(k) = L_ii + t*(1 - cos(k.delta_i)));
the Bloch construction itself is a provisional identification from the
existing framework and is probed here — a follow-up note documents
the construction's status.

Run:
    python3 verify_Paper48_irrep_block_O_k2_fit.py
"""

import numpy as np

# -----------------------------------------------------------------------------
# Face Laplacian on the isolated Kelvin cell
# -----------------------------------------------------------------------------
hex_normals = [np.array([s1, s2, s3]) for s1 in (1, -1)
                                      for s2 in (1, -1)
                                      for s3 in (1, -1)]  # 8 hexes, +/-1 components
sq_normals = [np.array([ 1, 0, 0]), np.array([-1, 0, 0]),
              np.array([ 0, 1, 0]), np.array([ 0,-1, 0]),
              np.array([ 0, 0, 1]), np.array([ 0, 0,-1])]

A = np.zeros((14, 14))
# hex-hex: share an edge iff the integer normals differ in exactly one sign
for i in range(8):
    for j in range(i + 1, 8):
        if int(np.sum(hex_normals[i] != hex_normals[j])) == 1:
            A[i, j] = A[j, i] = 1
# hex-sq: hex i borders square j iff the square's axis component matches
for i in range(8):
    for j in range(6):
        axis = int(np.argmax(np.abs(sq_normals[j])))
        sign = int(sq_normals[j][axis])
        if int(hex_normals[i][axis]) == sign:
            A[i, 8 + j] = A[8 + j, i] = 1
L = np.diag(A.sum(axis=1)) - A

evals, evecs = np.linalg.eigh(L)
# Reference spectrum
r1 = (9 - np.sqrt(17)) / 2
r2 = (9 + np.sqrt(17)) / 2
expected = sorted([0.0, r1, r1, r1, 4.0, 4.0, r2, r2, r2, 7.0, 7.0, 7.0, 7.0, 9.0])
assert max(abs(sorted(evals)[k] - expected[k]) for k in range(14)) < 1e-10, \
    "face Laplacian spectrum mismatch"

# Group eigenvectors into blocks by eigenvalue
def block_indices(evs, target, tol=1e-6):
    return [i for i, e in enumerate(evs) if abs(e - target) < tol]

blocks = {
    "A1g(0)  [photon]":        (0.0, 1),
    "T1u(r1) [left fermions]": (r1,  3),
    "Eg(4)   [W/Z]":           (4.0, 2),
    "T1u(r2) [right fermions]":(r2,  3),
    "T2g(7)+A1g(7) [gluons+]": (7.0, 4),
    "A2u(9) [Higgs]":          (9.0, 1),
}

# -----------------------------------------------------------------------------
# Bloch Hamiltonian — same construction as Symanzik_Matching_BCC.py (provisional)
# -----------------------------------------------------------------------------
def H_bloch(kx, ky, kz, t_hex=1.0, t_sq=1.0, a=1.0):
    H = L.astype(complex)
    for i in range(8):
        delta = (a / 2.0) * hex_normals[i]
        phase = np.exp(1j * (kx*delta[0] + ky*delta[1] + kz*delta[2]))
        H[i, i] += t_hex * (1.0 - phase)
    for j in range(6):
        delta = a * sq_normals[j]
        phase = np.exp(1j * (kx*delta[0] + ky*delta[1] + kz*delta[2]))
        idx = 8 + j
        H[idx, idx] += t_sq * (1.0 - phase)
    # Hermitise (eigvalsh's symmetric-part interpretation made explicit)
    return 0.5 * (H + H.conj().T)

# -----------------------------------------------------------------------------
# Extract (alpha, beta, gamma) for a triplet block
# -----------------------------------------------------------------------------
def triplet_eigenvalues_at(kvec, U_block, h):
    """Project H(h * k_hat) - L onto the block and return sorted eigenvalues / h^2."""
    kvec = np.asarray(kvec, dtype=float)
    khat = kvec / np.linalg.norm(kvec)
    k = h * khat
    V = H_bloch(*k) - L
    M = U_block.conj().T @ V @ U_block
    M = np.real(0.5 * (M + M.conj().T))
    return np.sort(np.linalg.eigvalsh(M)) / h**2

def fit_triplet(block_name, lam, U_block, h=1e-3):
    e100 = triplet_eigenvalues_at([1, 0, 0], U_block, h)
    e110 = triplet_eigenvalues_at([1, 1, 0], U_block, h)
    e111 = triplet_eigenvalues_at([1, 1, 1], U_block, h)
    # [100] -> {alpha, alpha, alpha+beta+gamma}  (alpha twice = transverse, largest = longitudinal)
    alpha_100 = e100[0]
    long_100 = e100[2]
    # [111] -> {alpha + gamma/3 (x2), alpha + beta + gamma/3}
    trans_111 = e111[0]
    long_111 = e111[2]
    # [110] -> {alpha (x1), alpha + gamma/2, alpha + beta + gamma/2}
    e110_sorted = e110
    # Solve for (alpha, beta, gamma)
    alpha = alpha_100
    # longitudinal - transverse = beta (both at [100] and [111])
    beta_100 = long_100 - alpha_100 - (trans_111 - alpha)  # gamma fix
    # Direct: gamma = 3*(trans_111 - alpha)
    gamma = 3.0 * (trans_111 - alpha)
    beta = long_100 - alpha - gamma
    # Cross-check against [110]: predicted out-of-plane = alpha, in-plane trans = alpha+gamma/2, long = alpha+beta+gamma/2
    pred_110 = np.sort(np.array([alpha, alpha + gamma/2.0, alpha + beta + gamma/2.0]))
    resid_110 = np.max(np.abs(pred_110 - e110_sorted))
    # gamma consistency: [100] gives alpha+beta+gamma = e100[2]; [111] gives alpha+beta+gamma/3 = e111[2]
    # -> difference = (2/3) gamma
    gamma_check = 1.5 * (long_100 - long_111)
    return {
        "block": block_name,
        "lambda": lam,
        "alpha": alpha,
        "beta":  beta,
        "gamma": gamma,
        "gamma_check_[100]vs[111]": gamma_check,
        "[100]_eigenvalues": e100,
        "[110]_eigenvalues": e110,
        "[111]_eigenvalues": e111,
        "[110]_residual":    resid_110,
    }

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------
print("=" * 72)
print("Paper #48 probe: O(k^2) dispersion fit per O_h irrep block")
print("Bloch construction: diagonal-only (Symanzik_Matching_BCC.py convention)")
print("=" * 72)

for name, (lam, mult) in blocks.items():
    idx = block_indices(evals, lam)
    if len(idx) != mult:
        print(f"\n{name}: eigenvalue {lam} has {len(idx)} eigenvectors, expected {mult}  -- skipped")
        continue
    U = evecs[:, idx]
    if mult == 1:
        # 1x1: just the scalar c in M(k) = c |k|^2
        h = 1e-3
        c100 = float((U.conj().T @ (H_bloch(h, 0, 0) - L) @ U).real.item()) / h**2
        c111 = float((U.conj().T @ (H_bloch(h/np.sqrt(3), h/np.sqrt(3), h/np.sqrt(3)) - L) @ U).real.item()) / h**2
        print(f"\n{name}: lambda = {lam:.4f}, m = 1")
        print(f"  scalar c at [100] : {c100:+.6f}")
        print(f"  scalar c at [111] : {c111:+.6f}")
        print(f"  isotropy check    : |[100] - [111]| = {abs(c100 - c111):.2e}")
    elif mult == 3:
        fit = fit_triplet(name, lam, U)
        print(f"\n{fit['block']}: lambda = {fit['lambda']:.4f}, m = 3")
        print(f"  alpha (|k|^2 delta_ij)       = {fit['alpha']:+.6f}")
        print(f"  beta  (k_i k_j)              = {fit['beta']:+.6f}")
        print(f"  gamma (delta_ij k_i^2)       = {fit['gamma']:+.6f}    <-- O_h-only (O(3)-breaking)")
        print(f"  gamma cross-check [100]v[111]= {fit['gamma_check_[100]vs[111]']:+.6f}")
        print(f"  [110] residual vs 3-param    = {fit['[110]_residual']:.2e}")
        if abs(fit["gamma"]) < 1e-4:
            print(f"  -> gamma = 0  O(3)-invariant at O(k^2)")
        else:
            print(f"  -> gamma != 0  O_h -> O(3) BROKEN at O(k^2)")
    elif mult == 2:
        # Eg: under O_h, at O(k^2) there are O_h-invariant couplings
        # to {k_x^2 - k_y^2, (2 k_z^2 - k_x^2 - k_y^2)/sqrt(3)} (Eg basis) plus |k|^2 * identity.
        # Simplest numerical check: O(3) invariance demands isotropy -> both eigenvalues equal and direction-independent.
        h = 1e-3
        e100 = triplet_eigenvalues_at([1, 0, 0], U, h)
        e111 = triplet_eigenvalues_at([1, 1, 1], U, h)
        print(f"\n{name}: lambda = {lam:.4f}, m = 2")
        print(f"  [100] block eigenvalues: {e100}")
        print(f"  [111] block eigenvalues: {e111}")
        split_100 = e100[-1] - e100[0]
        print(f"  [100] internal splitting: {split_100:+.6f}    (>0 -> E_g is not isotropic at O(k^2))")
    elif mult == 4:
        # T_2g(3) + A_1g(1) at lambda=7 — just report all four eigenvalues per direction
        h = 1e-3
        e100 = triplet_eigenvalues_at([1, 0, 0], U, h)
        e111 = triplet_eigenvalues_at([1, 1, 1], U, h)
        print(f"\n{name}: lambda = {lam:.4f}, m = 4  (T_2g + A_1g — reported as block, not fit)")
        print(f"  [100] block eigenvalues: {e100}")
        print(f"  [111] block eigenvalues: {e111}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 72)
print("Closed-form check against master-equation Vieta invariants")
print("=" * 72)

# Predicted closed forms (this session, 2026-04-17)
sqrt17 = np.sqrt(17.0)
a_minus = (17.0 - sqrt17) / 272.0
a_plus  = (17.0 + sqrt17) / 272.0
b_minus = 2.0 * a_minus
b_plus  = 2.0 * a_plus
g_minus = a_minus * (5.0 + sqrt17) / 2.0
g_plus  = a_plus  * (5.0 - sqrt17) / 2.0

# Numerical fit (same algorithm as above, repeated here for self-contained assertion)
idx_r1 = block_indices(evals, r1)
idx_r2 = block_indices(evals, r2)
fit_r1 = fit_triplet("T_1u(r_-)", r1, evecs[:, idx_r1])
fit_r2 = fit_triplet("T_1u(r_+)", r2, evecs[:, idx_r2])

print(f"\n T_1u(r_-) left fermions  [numerical → closed form]")
print(f"   alpha = {fit_r1['alpha']:.8f}  vs  (17-sqrt17)/272 = {a_minus:.8f}   diff {abs(fit_r1['alpha']-a_minus):.2e}")
print(f"   beta  = {fit_r1['beta']:.8f}  vs  2 alpha          = {b_minus:.8f}   diff {abs(fit_r1['beta']-b_minus):.2e}")
print(f"   gamma = {fit_r1['gamma']:.8f}  vs  alpha*(r_+-2)   = {g_minus:.8f}   diff {abs(fit_r1['gamma']-g_minus):.2e}")

print(f"\n T_1u(r_+) right fermions [numerical → closed form]")
print(f"   alpha = {fit_r2['alpha']:.8f}  vs  (17+sqrt17)/272 = {a_plus:.8f}   diff {abs(fit_r2['alpha']-a_plus):.2e}")
print(f"   beta  = {fit_r2['beta']:.8f}  vs  2 alpha          = {b_plus:.8f}   diff {abs(fit_r2['beta']-b_plus):.2e}")
print(f"   gamma = {fit_r2['gamma']:.8f}  vs  alpha*(r_--2)   = {g_plus:.8f}   diff {abs(fit_r2['gamma']-g_plus):.2e}")

print(f"\n Chirality-crossing dual:  gamma_+/alpha_+ and gamma_-/alpha_-")
print(f"   gamma_-/alpha_-  = {fit_r1['gamma']/fit_r1['alpha']:.6f}   vs  r_+ - 2 = {r2-2.0:.6f}   (should equal r_+ - 2)")
print(f"   gamma_+/alpha_+  = {fit_r2['gamma']/fit_r2['alpha']:.6f}   vs  r_- - 2 = {r1-2.0:.6f}   (should equal r_- - 2)")

print(f"\n Vieta cross-identities over (r_-, r_+):")
print(f"   alpha_- + alpha_+ = {fit_r1['alpha']+fit_r2['alpha']:.6f}   vs  1/8  = 1/F_hx  = {1/8:.6f}")
print(f"   alpha_- * alpha_+ = {fit_r1['alpha']*fit_r2['alpha']:.8f} vs  1/272 = 1/(r_1 r_2 Delta) = {1/(16*17):.8f}")
print(f"   gamma_- + gamma_+ = {fit_r1['gamma']+fit_r2['gamma']:.6f}   vs  1/4  = 2/F_hx  = {1/4:.6f}")
print(f"   gamma_- * gamma_+ = {fit_r1['gamma']*fit_r2['gamma']:.8f} vs  1/136 = 1/(F_hx Delta) = {1/136:.8f}")

print(f"\n Angular complement (Regge dihedral deficits):")
hh = np.arccos(1.0/3.0)
hs = np.arccos(1.0/np.sqrt(3.0))
print(f"   delta_hh = arccos(1/3)   = {np.degrees(hh):.4f} deg   (12 hex-hex edges)")
print(f"   delta_hs = arccos(1/sqrt3) = {np.degrees(hs):.4f} deg   (24 hex-sq  edges)")
print(f"   delta_hh + 2*delta_hs    = {np.degrees(hh + 2*hs):.6f} deg  (should be 180 exactly)")
print(f"   identity residual        = {abs(np.degrees(hh + 2*hs) - 180.0):.2e} deg")

# Hard assertions
assert abs(fit_r1['alpha'] - a_minus) < 1e-6
assert abs(fit_r1['beta']  - b_minus) < 1e-6
assert abs(fit_r1['gamma'] - g_minus) < 1e-6
assert abs(fit_r2['alpha'] - a_plus)  < 1e-6
assert abs(fit_r2['beta']  - b_plus)  < 1e-6
assert abs(fit_r2['gamma'] - g_plus)  < 1e-6
assert abs(fit_r1['alpha'] + fit_r2['alpha'] - 1.0/8.0) < 1e-6
assert abs(fit_r1['gamma'] + fit_r2['gamma'] - 1.0/4.0) < 1e-6
assert abs(fit_r1['alpha'] * fit_r2['alpha'] - 1.0/272.0) < 1e-8
assert abs(fit_r1['gamma'] * fit_r2['gamma'] - 1.0/136.0) < 1e-8
assert abs(hh + 2*hs - np.pi) < 1e-12
print("\n All closed-form assertions passed.")

print("\n" + "=" * 72)
print("Summary")
print("=" * 72)
print("""
Interpretation:
  - For a triplet block (T_1u or T_2g), the O(k^2) O_h-invariant dispersion
    has three parameters: (alpha, beta, gamma).  alpha and beta are
    already O(3)-invariant; gamma is the O_h-only anisotropy.
  - gamma != 0 for T_1u(r_1) and T_1u(r_2) in the provisional Bloch
    construction — i.e. the fermion dispersion on the BCC-tiled foam is
    NOT O(3)-invariant at O(k^2) in this construction.
  - This is an open item for Paper #48: the continuum-limit identification
    of S = psi^dag L_T psi with the Dirac kinetic term requires either
        (i)  a Symanzik improvement counter-term to cancel gamma, or
        (ii) a field redefinition that absorbs gamma, or
        (iii) a different Bloch construction (e.g. antipodal-face coupling
              instead of same-face diagonal coupling) for which gamma = 0.

Next session: build the antipodal-face Bloch construction from the foam
action S = sum_cells psi^dag L_T psi with BCC-periodic boundary, re-run
this fit, and decide whether (iii) closes the gap or whether genuine
improvement operators are needed.
""")
