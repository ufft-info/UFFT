#!/usr/bin/env python3
"""
verify_face_graph_paper_2026-10-06.py  (revision 2, 2026-10-07)

Every numerical statement in "The face graph of the truncated octahedron" (Draft 2/3),
checked as a test harness: every advertised claim is an explicit check, failures are
accumulated, and the exit status is nonzero if any positive assertion fails.

Revision 2 answers the referee's software audit of 2026-10-07:
  * ALL PASS is now conditional on every check; exit status 1 on any failure.
  * Claims labelled EXACT use integer (Python int) arithmetic and exact equality;
    claims labelled NUMERIC state their tolerance.
  * All five Fedorov face-graph Laplacian factorizations are asserted, not printed.
  * Projector weights are compared to their closed forms at 1e-12.
  * Expected NEGATIVE facts (K does not annihilate the constant vector) are reported as
    notes, not as passes of a positive claim.
  * The Faddeev-LeVerrier recursion asserts divisibility before each division.

NumPy only; networkx is optional (automorphism count).
"""
import itertools, sys
from fractions import Fraction
import numpy as np

FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
def note(name, detail=""):
    print("NOTE  " + name + (("   " + detail) if detail else ""))

# ---------------------------------------------------------------- geometry (exact ints)
def faces_truncated_octahedron():
    V = sorted({tuple(a*b for a, b in zip(p, s)) for p in itertools.permutations([0, 1, 2])
                for s in itertools.product([1, -1], repeat=3)})
    F = []
    for ax in range(3):
        for s in (2, -2): F.append([i for i, v in enumerate(V) if v[ax] == s])
    for sg in itertools.product([1, -1], repeat=3):
        F.append([i for i, v in enumerate(V) if sum(a*b for a, b in zip(v, sg)) == 3])
    return V, F
def face_graph(F):
    n = len(F); A = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if len(set(F[i]) & set(F[j])) == 2: A[i][j] = A[j][i] = 1
    return A

# ---------------------------------------------------------------- exact linear algebra
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def charpoly_int(M):
    """Faddeev-LeVerrier over Z; asserts divisibility at every step."""
    n = len(M); I = [[int(i == j) for j in range(n)] for i in range(n)]
    Mk = [[0]*n for _ in range(n)]; c = 1; coeffs = [1]
    for k in range(1, n+1):
        Mk = matmul(M, [[Mk[i][j] + c*I[i][j] for j in range(n)] for i in range(n)])
        tr = sum(Mk[i][i] for i in range(n))
        assert tr % k == 0, f"Faddeev-LeVerrier: trace {tr} not divisible by {k}"
        c = -tr // k; coeffs.append(c)
    return coeffs
def pmul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out
def prod(factors):
    r = [1]
    for f, p in factors:
        for _ in range(p): r = pmul(r, f)
    return r

# ================================================================ 1. the graph
V, F = faces_truncated_octahedron()
A = face_graph(F); n = 14
deg = [sum(r) for r in A]
L = [[(deg[i] if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
Q = [[(deg[i] if i == j else 0) + A[i][j] for j in range(n)] for i in range(n)]
sq, hx = list(range(6)), list(range(6, 14))
print("== 1. graph (EXACT) ==")
check("24 vertices, 14 faces", len(V) == 24 and len(F) == 14)
check("36 edges", sum(deg)//2 == 36)
check("degrees 4^6 6^8", sorted(deg) == [4]*6 + [6]*8)
check("24 square-hexagon, 12 hexagon-hexagon, 0 square-square adjacencies",
      sum(A[i][j] for i in sq for j in hx) == 24
      and sum(A[i][j] for i in hx for j in hx)//2 == 12
      and sum(A[i][j] for i in sq for j in sq) == 0)
A2 = matmul(A, A); A3 = matmul(A2, A); A4 = matmul(A3, A)
trA3 = sum(A3[i][i] for i in range(n)); trA4 = sum(A4[i][i] for i in range(n))
check("24 triangles", trA3 % 6 == 0 and trA3//6 == 24)
c4num = trA4 - 2*sum(d*d for d in deg) + sum(deg)
check("42 four-cycles", c4num % 8 == 0 and c4num//8 == 42)
try:
    import networkx as nx
    G = nx.Graph([(i, j) for i in range(n) for j in range(i+1, n) if A[i][j]])
    aut = sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
    check("automorphism group order 48", aut == 48, f"found {aut}")
except ImportError:
    note("automorphism count skipped (networkx not installed)")

# ================================================================ 2. characteristic polynomials
print("\n== 2. characteristic polynomials (EXACT) ==")
check("adjacency charpoly = x^2 (x+1)^3 (x+3) (x^2-3x-12) (x^2-x-4)^3",
      charpoly_int(A) == prod([([1,0],2),([1,1],3),([1,3],1),([1,-3,-12],1),([1,-1,-4],3)]))
check("Laplacian charpoly = x (x-9) (x-7)^4 (x-4)^2 (x^2-9x+16)^3",
      charpoly_int(L) == prod([([1,0],1),([1,-9],1),([1,-7],4),([1,-4],2),([1,-9,16],3)]))
check("signless Laplacian charpoly = (x-8)^3 (x-5)^3 (x-4)^2 (x-3)^4 (x^2-13x+24)",
      charpoly_int(Q) == prod([([1,-8],3),([1,-5],3),([1,-4],2),([1,-3],4),([1,-13,24],1)]))
check("discriminants 57 and 17 (adjacency), 17 (Laplacian), 73 (signless)",
      9+48 == 57 and 1+16 == 17 and 81-64 == 17 and 169-96 == 73)

# ================================================================ 3. exact block identities on raw vectors
print("\n== 3. orbit blocks on raw coordinate vectors (EXACT) ==")
def mv(M, v): return [sum(M[i][j]*v[j] for j in range(n)) for i in range(n)]
def lin(a, u, b, w): return [a*x + b*y for x, y in zip(u, w)]
K = [[(L[i][j] if (i < 6 and j >= 6) else (-L[i][j] if (i >= 6 and j < 6) else 0)) for j in range(n)] for i in range(n)]
check("K = P_sq L P_hx - P_hx L P_sq is antisymmetric", all(K[i][j] == -K[j][i] for i in range(n) for j in range(n)))
one_sq = [1]*6 + [0]*8; one_hx = [0]*6 + [1]*8
check("A1g plane: K 1_sq = 3 1_hx, K 1_hx = -4 1_sq  (so K^2 = -12 I there)",
      mv(K, one_sq) == [3*x for x in one_hx] and mv(K, one_hx) == [-4*x for x in one_sq])
check("Delta_A1g block: L(1_sq + 1_hx) = 0 and L 1_sq = 4 1_sq - 3 1_hx",
      mv(L, lin(1, one_sq, 1, one_hx)) == [0]*n and mv(L, one_sq) == [4]*6 + [-3]*8)
okT = True
for ax in range(3):
    s = [0]*n; s[2*ax] = 1; s[2*ax+1] = -1
    h = [0]*n
    for k, sg in enumerate(itertools.product([1, -1], repeat=3)): h[6+k] = sg[ax]
    okT &= mv(L, s) == lin(4, s, -1, h) and mv(L, h) == lin(-4, s, 5, h)
    okT &= mv(K, mv(K, s)) == [-4*x for x in s] and mv(K, mv(K, h)) == [-4*x for x in h]
check("T1u blocks, all three axes: L s = 4s - h, L h = -4s + 5h, K^2 s = -4s, K^2 h = -4h", okT)
v7 = [4]*6 + [-3]*8          # orbit-uniform eigenvector at 7, scaled to integers
check("orbit-uniform vector (4,..,4,-3,..,-3) has L-eigenvalue 7", mv(L, v7) == [7*x for x in v7])
check("its square content is 6*16/(6*16+8*9) = 4/7", Fraction(6*16, 6*16+8*9) == Fraction(4, 7))
note("K does not annihilate the constant vector (expected negative; not a claim of the paper)",
     f"K 1 = {mv(K, [1]*n)}")

# ================================================================ 4. numerical spectral checks
print("\n== 4. eigenspaces and projector weights (NUMERIC, tolerance 1e-12 unless stated) ==")
Lf = np.array(L, float); w, U = np.linalg.eigh(Lf)
r1, r2 = (9-17**.5)/2, (9+17**.5)/2
def eigspace(val, tol=1e-9):
    idx = [k for k in range(n) if abs(w[k]-val) < tol]; return U[:, idx]
expected = {0: (1, 3/7), r1: (3, (1+17**-.5)/2), 4: (2, 1.0), r2: (3, (1-17**-.5)/2), 7: (4, 1/7), 9: (1, 0.0)}
for val, (dim, wsq) in expected.items():
    E = eigspace(val); P = E @ E.T
    fr = np.trace(P[:6, :6])/E.shape[1] if E.shape[1] else float("nan")
    check(f"lambda={val:.4f}: multiplicity {dim}, square weight {wsq:.6f}",
          E.shape[1] == dim and abs(fr - wsq) < 1e-12, f"got mult {E.shape[1]}, weight {fr:.12f}")
Kf = np.array(K, float)
E1, E2 = eigspace(r1), eigspace(r2); B = np.hstack([E1, E2])
K6 = B.T @ Kf @ B
check("K^2 = -4 I on T1u(r1) + T1u(r2)", np.allclose(K6 @ K6, -4*np.eye(6), atol=1e-12))
check("K maps T1u(r1) into T1u(r2) and back", np.allclose(E2 @ E2.T @ (Kf @ E1), Kf @ E1, atol=1e-12)
      and np.allclose(E1 @ E1.T @ (Kf @ E2), Kf @ E2, atol=1e-12))
check("K annihilates Eg (lambda=4)", np.allclose(Kf @ eigspace(4), 0, atol=1e-12))
check("K annihilates A2u (lambda=9)", np.allclose(Kf @ eigspace(9), 0, atol=1e-12))
E7 = eigspace(7); u7 = np.array(v7, float); u7 /= np.linalg.norm(u7)
T2g = E7 - np.outer(u7, u7 @ E7)          # lambda=7 space minus its A1g (orbit-uniform) line
check("K annihilates the T2g summand of the lambda=7 space", np.allclose(Kf @ T2g, 0, atol=1e-12))
E0 = eigspace(0)
check("K sends A1g(0) into the lambda=7 space (A1g exchange)", np.allclose(E7 @ E7.T @ (Kf @ E0), Kf @ E0, atol=1e-12))
sv = np.linalg.svd(E2.T @ Kf @ E1, compute_uv=False)
check("singular values of K_21 are (2,2,2): K_21 = 2U", np.allclose(sv, 2, atol=1e-12), f"{np.round(sv, 12)}")

# ================================================================ 5. the five Fedorov parallelohedra
print("\n== 5. Fedorov face-graph Laplacians (EXACT factorizations) ==")
def lap(Aint):
    m = len(Aint); d = [sum(r) for r in Aint]
    return [[(d[i] if i == j else 0) - Aint[i][j] for j in range(m)] for i in range(m)]
Ac = [[int(i != j and i//2 != j//2) for j in range(6)] for i in range(6)]            # octahedron graph
Ah = [[0]*8 for _ in range(8)]                                                          # hexagonal prism
for i in range(6):
    j = (i+1) % 6; Ah[i][j] = Ah[j][i] = 1; Ah[i][6] = Ah[6][i] = 1; Ah[i][7] = Ah[7][i] = 1
cv = list(itertools.product([0, 1], repeat=3))                                          # rhombic dodecahedron = L(cube)
ce = [(a, b) for a in cv for b in cv if a < b and sum(x != y for x, y in zip(a, b)) == 1]
Ar = [[int(i != j and len(set(ce[i]) & set(ce[j])) == 1) for j in range(12)] for i in range(12)]
Ae = [[0]*12 for _ in range(12)]                                                        # elongated dodecahedron
H4, Tp, Bt = list(range(4)), list(range(4, 8)), list(range(8, 12))
for i in range(4):
    j = (i+1) % 4
    for a, b in ((H4[i], H4[j]), (Tp[i], Tp[j]), (Bt[i], Bt[j])): Ae[a][b] = Ae[b][a] = 1
    for k in (i, j):
        Ae[H4[i]][Tp[k]] = Ae[Tp[k]][H4[i]] = 1; Ae[H4[i]][Bt[k]] = Ae[Bt[k]][H4[i]] = 1
fedorov = [
    ("cube                   x (x-4)^3 (x-6)^2",            Ac, [([1,0],1),([1,-4],3),([1,-6],2)]),
    ("hexagonal prism        x (x-3)^2 (x-5)^2 (x-6)^2 (x-8)", Ah, [([1,0],1),([1,-3],2),([1,-5],2),([1,-6],2),([1,-8],1)]),
    ("rhombic dodecahedron   x (x-2)^3 (x-4)^3 (x-6)^5",     Ar, [([1,0],1),([1,-2],3),([1,-4],3),([1,-6],5)]),
    ("elongated dodecahedron x (x-2) (x-4)^2 (x-6)^3 (x-8) (x^2-10x+20)^2", Ae,
         [([1,0],1),([1,-2],1),([1,-4],2),([1,-6],3),([1,-8],1),([1,-10,20],2)]),
    ("truncated octahedron   x (x-9) (x-7)^4 (x-4)^2 (x^2-9x+16)^3", A,
         [([1,0],1),([1,-9],1),([1,-7],4),([1,-4],2),([1,-9,16],3)]),
]
for name, Aint, fac in fedorov:
    check(name, charpoly_int(lap(Aint)) == prod(fac))

# ================================================================ verdict
print()
if FAILED:
    print(f"FAILED ({len(FAILED)}):"); [print("   ", f) for f in FAILED]
    sys.exit(1)
print("ALL PASS  (every line above marked PASS is a conditional assertion; exit status 0)")
