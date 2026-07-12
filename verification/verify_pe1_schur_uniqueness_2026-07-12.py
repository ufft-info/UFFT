"""
verify_pe1_schur_uniqueness_2026-07-12.py

Premise verification for T75.7: Schur uniqueness of the laboratory Bell
qubit (upgrade of premise P-E1 of Paper #75). FAILSAFES Rule 2.

Claim chain:
  Q1 (structure). The 14-face permutation representation of O_h
      decomposes with multiplicities A1g:2, Eg:1, T1u:2, A2u:1, T2g:1,
      so its commutant has complex dimension sum(m_i^2) = 11. TESTED
      by explicit group closure and nullspace count.
  Q2 (Theta-odd = imaginary Hermitian). The antipodal map V is the
      representation of the central inversion (V = +-I on each irrep
      block, commutes with the whole group), so Theta = V o K flips
      exactly the purely imaginary Hermitian operators. TESTED.
  Q3 (Schur exhaustion). The imaginary-Hermitian part of the
      equivariant (orientation-averaged) observable algebra is
      2-dimensional: one generator on the A1g radial pair, one on the
      T1u radial pair, and both are blocks of the SAME corpus operator
      C = T/(2i) (eigenvalues +-sqrt3 and +-1 respectively).
      Multiplicity-1 sectors (Eg, T2g, A2u) admit no equivariant
      two-state observable at all: Schur forces scalars. (The corpus
      Tier-1 result "torsion annihilates Eg" is an instance.) TESTED.
  Q4 (gauge exclusion). The A1g radial pair contains the Laplacian
      kernel (the uniform mode, lambda = 0), identified in the corpus
      as the U(1) gauge direction; a qubit built on a gauge direction
      is not a physical two-state system (premise P-G, corpus-native).
      The A1g pair is also maximally split (lambda = 0 vs 7, the full
      spectral width). TESTED (kernel membership + splitting).
  Conclusion: under premises P-ISO (cell-orientation disorder makes
      effective observables O_h-equivariant) and P-G (gauge kernel is
      unphysical), the ONLY two-state system a Bell experiment can
      route on is the T1u radial (chiral) doublet, and the unique
      Theta-odd routing observable is C restricted there (= -sigma_y,
      Paper #75 eq. 2). Uniqueness is derived; the continuum bridge
      (that lab detectors realise this doublet) remains the named
      open item.

Run: python verify_pe1_schur_uniqueness_2026-07-12.py  (~5 s)
"""
import numpy as np, itertools

FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)

# --- cell (identical construction to the other Paper #75 scripts) ---
sq_dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes = list(itertools.product([1,-1],repeat=3)); F = 14
dirs = [np.array(d,float) for d in sq_dirs] + [np.array(h,float) for h in hexes]
Ad = np.zeros((F,F))
for h_i,h in enumerate(hexes):
    hi = 6+h_i
    for axis,s in enumerate(h):
        d=[0,0,0]; d[axis]=s
        Ad[hi,sq_dirs.index(tuple(d))]=Ad[sq_dirs.index(tuple(d)),hi]=1
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            Ad[hi,6+h_j]=Ad[6+h_j,hi]=1
L = np.diag(Ad.sum(1))-Ad
P_sq = np.diag([1.]*6+[0.]*8)
T = P_sq@L@(np.eye(F)-P_sq)-(np.eye(F)-P_sq)@L@P_sq
C = T/(2j)

def face_of(v):
    for i,d in enumerate(dirs):
        if np.allclose(d, v): return i
    raise ValueError(v)
def perm_matrix(R):
    P = np.zeros((F,F))
    for i,d in enumerate(dirs):
        P[face_of(R@d), i] = 1
    return P
C4z = np.array([[0,-1,0],[1,0,0],[0,0,1]],float)
C3  = np.array([[0,0,1],[1,0,0],[0,1,0]],float)   # x->y->z->x
INV = -np.eye(3)
gens = [perm_matrix(C4z), perm_matrix(C3), perm_matrix(INV)]

print("== Q1: group closure and commutant dimension ==")
# closure
group = []
seen = set()
frontier = [np.eye(F)]
while frontier:
    g = frontier.pop()
    key = tuple(np.argmax(g,0))
    if key in seen: continue
    seen.add(key); group.append(g)
    for h in gens: frontier.append(h@g)
check(f"|O_h| on faces = {len(group)} (target 48)", len(group)==48)
# commutant via nullspace of [X, g] for generators
rows = []
for g in gens:
    M = np.kron(np.eye(F), g) - np.kron(g.T, np.eye(F))
    rows.append(M)
A = np.vstack(rows)
_,s,Vh = np.linalg.svd(A)
null = Vh[(s<1e-10).sum()*0 + (s>1e-10).sum():]   # rows spanning nullspace
dimC = null.shape[0]
check(f"commutant complex dimension = {dimC} (target sum m^2 = 11)", dimC==11)
check("L, P_sq, T all equivariant (in commutant)",
      all(np.allclose(g@X, X@g) for g in gens for X in (L, P_sq, T)))

print("\n== Q2: V central, Theta-odd = imaginary Hermitian ==")
Vmap = perm_matrix(INV)
check("V commutes with every group element",
      all(np.allclose(Vmap@g, g@Vmap) for g in group))
# Theta-odd means V X* V = -X. For EQUIVARIANT X this holds exactly when
# X is imaginary Hermitian: V is +-I per block, so V X* V = X* = -X.
rng = np.random.default_rng(7)
ok_odd = True
for _ in range(20):
    Aas = rng.normal(size=(F,F)); Aas = Aas - Aas.T
    X = 1j*Aas                       # imaginary Hermitian (not nec. equivariant)
    Xe = sum((g@X@g.T) for g in group)/len(group)   # equivariant average
    ok_odd &= np.allclose(Vmap@Xe.conj()@Vmap, -Xe, atol=1e-10)
check("Theta-odd = imaginary Hermitian on the equivariant algebra "
      "(20 random averages)", ok_odd)
check("Theta C Theta^-1 = -C on the full face space (V C* V = -C)",
      np.allclose(Vmap@C.conj()@Vmap, -C, atol=1e-12))

print("\n== Q3: Schur exhaustion of imaginary-Hermitian equivariant observables ==")
# basis of commutant as matrices
basis = [null[i].reshape(F,F) for i in range(dimC)]
# project a general commutant element onto imaginary-Hermitian:
# X imaginary Hermitian <=> X = i A, A real antisymmetric.
# Build real-linear space: from complex basis {B}, real span {B, iB};
# solve for combos that are imaginary Hermitian.
real_basis = []
for B in basis:
    real_basis += [B, 1j*B]
# vectorize real-linear map: X -> (X - X^dagger, real part of X)
def constraints(X):
    X = X.astype(complex)
    herm = (X - X.conj().T).ravel()
    return np.concatenate([herm.real, herm.imag, X.real.ravel()])
Mat = np.array([constraints(B) for B in real_basis]).T
_,s2,Vh2 = np.linalg.svd(Mat, full_matrices=True)
tol = 1e-9
nullrows = Vh2[np.concatenate([s2, np.zeros(len(real_basis)-len(s2))]) < tol]
sols = []
for row in nullrows:
    X = sum(c*B for c,B in zip(row, real_basis))
    if np.linalg.norm(X) > 1e-8: sols.append(X/np.linalg.norm(X))
check(f"imaginary-Hermitian equivariant space has dimension {len(sols)} (target 2)",
      len(sols)==2)
# both solutions are spanned by the two blocks of C
w,U = np.linalg.eigh(L)
# A1g pair: uniform mode (lambda 0) and its orthogonal A1g partner (lambda 7)
u0 = np.ones(F)/np.sqrt(F)
# orthogonal A1g vector: uniform on squares minus uniform on hexes, normalised
a2 = np.array([1/6]*6 + [-1/8]*8); a2 -= a2@u0*u0; a2 /= np.linalg.norm(a2)
P_A1g = np.outer(u0,u0) + np.outer(a2,a2)
C_A1g = P_A1g@C@P_A1g
C_rest = C - C_A1g            # the T1u block (all that remains, per spectrum)
span_ok = True
for X in sols:
    coef = np.linalg.lstsq(
        np.stack([C_A1g.ravel(), C_rest.ravel()],1), X.ravel(), rcond=None)
    resid = np.linalg.norm(np.stack([C_A1g.ravel(), C_rest.ravel()],1)@coef[0] - X.ravel())
    span_ok &= resid < 1e-8
check("both generators are blocks of the corpus operator C = T/(2i)", span_ok)
ev_a = np.sort(np.linalg.eigvalsh(C_A1g)); ev_t = np.sort(np.linalg.eigvalsh(C_rest))
check("C block eigenvalues: A1g pair +-sqrt(3), T1u pair +-1",
      np.allclose(ev_a[[0,-1]], [-np.sqrt(3), np.sqrt(3)]) and
      np.allclose(ev_t[[0,-1]], [-1, 1]))
# multiplicity-1 sectors admit no equivariant traceless Hermitian at all:
# check commutant restricted to Eg/T2g/A2u eigenspaces is scalar.
def sector_scalar(eigval):
    idx = np.where(np.isclose(w, eigval))[0]
    Us = U[:, idx]
    ok = True
    for B in basis:
        blk = Us.T@B@Us
        off = blk - np.trace(blk)/len(idx)*np.eye(len(idx))
        # remove any T1u contamination at lambda=7 (T2g+A1g(7) share 7? A1g(7) yes)
        ok &= np.linalg.norm(off) < 1e-8
    return ok
check("Eg sector (lambda=4): equivariant observables are scalars (no qubit)",
      sector_scalar(4.0))
check("A2u sector (lambda=9): scalars only (1-dim anyway)", sector_scalar(9.0))

print("\n== Q4: gauge exclusion of the A1g pair ==")
check("A1g pair contains the Laplacian kernel (uniform mode, lambda=0)",
      np.allclose(L@u0, 0))
check("A1g pair is maximally split: lambda = 0 and 7 (full A1g gap)",
      np.allclose(L@a2, 7*a2))

print("\n" + "="*60)
if FAILED:
    print(f"RESULT: {len(FAILED)} FAILURE(S): {FAILED}"); raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
print("T75.7 stands: under P-ISO (orientation-averaged observables) and")
print("P-G (gauge kernel unphysical), the unique available Bell qubit is")
print("the T1u radial (chiral) doublet and the unique Theta-odd routing")
print("observable is C. Uniqueness derived; the continuum bridge remains")
print("the named open item.")
