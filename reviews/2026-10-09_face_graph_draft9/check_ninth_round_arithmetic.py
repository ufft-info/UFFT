#!/usr/bin/env python3
"""Author-side check of the identities stated in the ninth review round (ReviewBot, Draft 9, 9 Oct 2026).

The round's own checks: the two characteristic polynomials from the adjacency rules; the Gram identities
B*B = (9I - C^2)/2 and BB* = 4I for the printed quarter-flux gauge, with a one-entry sign perturbation breaking them;
K^T = -K, K s_a = h_a, K h_a = -4 s_a, K^2 = -12 on the orbit constants; the chain-complex ranks. Everything is
recomputed here exactly (integers, sympy over Q and Q(i)). The round also inspected the Lean sources without building
them; the bridge it asked for as R2 is FaceGraph/Graph.lean, whose theorems are listed at the end.
"""
import itertools, math, sys
import numpy as np
import sympy as sp
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
sq = [(a, s) for a in range(3) for s in (1, -1)]; hx = list(itertools.product([1, -1], repeat=3)); N = 14
A = sp.zeros(N, N)
for i, h in enumerate(hx):
    for j, h2 in enumerate(hx):
        if sum(x != y for x, y in zip(h, h2)) == 1: A[6+i, 6+j] = 1
    for k, (a, s) in enumerate(sq):
        if h[a] == s: A[6+i, k] = A[k, 6+i] = 1
D = sp.diag(*[sum(A.row(i)) for i in range(N)]); x = sp.symbols("x")
L = D - A; S = D + A
chiL = sp.factor((x*sp.eye(N) - L).det()); chiS = sp.factor((x*sp.eye(N) - S).det())
check("chi_L = x (x-9)(x-7)^4 (x-4)^2 (x^2-9x+16)^3", sp.expand(chiL - x*(x-9)*(x-7)**4*(x-4)**2*(x**2-9*x+16)**3) == 0)
check("chi_S = (x-8)^3 (x-5)^3 (x-4)^2 (x-3)^4 (x^2-13x+24)", sp.expand(chiS - (x-8)**3*(x-5)**3*(x-4)**2*(x-3)**4*(x**2-13*x+24)) == 0)
# quarter-flux gauge (B): B_{(a,s),h} = (h_b - i s h_c)/(1 - i s), (a,b,c) cyclic, for h_a = s; zero otherwise
I = sp.I
B = sp.zeros(6, 8)
for k, (a, s) in enumerate(sq):
    b, c = (a+1) % 3, (a+2) % 3
    for i, h in enumerate(hx):
        if h[a] == s: B[k, i] = sp.simplify((h[b] - I*s*h[c])/(1 - I*s))
C = A[6:, 6:]
check("Gram: B* B = (9I - C^2)/2", sp.simplify(B.H*B - (9*sp.eye(8) - C**2)/2) == sp.zeros(8, 8))
check("Gram: B B* = 4 I_6", sp.simplify(B*B.H - 4*sp.eye(6)) == sp.zeros(6, 6))
check("every nonzero entry of B is a unit phase in {+-1, +-i}", all(e == 0 or e in (1, -1, I, -I) for e in B))
Bp = B.copy(); k0, i0 = next((k, i) for k in range(6) for i in range(8) if B[k, i] != 0); Bp[k0, i0] = -Bp[k0, i0]
check("control: one sign flip in B breaks B* B = (9I - C^2)/2", sp.simplify(Bp.H*Bp - (9*sp.eye(8) - C**2)/2) != sp.zeros(8, 8))
Delta6 = sp.zeros(N, N)
Delta6[:6, :6] = 4*sp.eye(6); Delta6[6:, 6:] = 6*sp.eye(8) - C; Delta6[:6, 6:] = -B; Delta6[6:, :6] = -B.H
chi6 = sp.factor(sp.expand((x*sp.eye(N) - Delta6).det()))
check("chi(Delta_6) = (x-9)(x-8)^3 (x-3)^4 (x^2-9x+16)^3 from the gauge formula", sp.expand(chi6 - (x-9)*(x-8)**3*(x-3)**4*(x**2-9*x+16)**3) == 0)
# K relations
Ps = sp.diag(*([1]*6 + [0]*8)); Ph = sp.eye(N) - Ps; K = Ps*L*Ph - Ph*L*Ps
check("K^T = -K", K.T == -K)
ok = True
for a in range(3):
    s_ = sp.zeros(N, 1); s_[2*a] = 1; s_[2*a+1] = -1
    h_ = sp.zeros(N, 1)
    for i, h in enumerate(hx): h_[6+i] = h[a]
    ok = ok and (K*s_ == h_) and (K*h_ == -4*s_)
check("K s_a = h_a and K h_a = -4 s_a for the three axes", ok)
one_s = sp.Matrix([1]*6 + [0]*8); one_h = sp.Matrix([0]*6 + [1]*8)
check("K^2 = -12 on the orbit constants (K 1_s = 3 1_h, K 1_h = -4 1_s)", K*one_s == 3*one_h and K*one_h == -4*one_s)
# chain complex of the 24 outward-oriented triangles (as in the eighth-round checker)
edges = [(i, j) for i in range(N) for j in range(i+1, N) if A[i, j]]; eidx = {e: n for n, e in enumerate(edges)}
tri = []
for k, (a, s) in enumerate(sq):
    hs_ = [6+i for i, h in enumerate(hx) if h[a] == s]
    for i in hs_:
        for j in hs_:
            if i < j and A[i, j]:
                p0 = np.zeros(3); p0[a] = s; p1 = np.array(hx[i-6], float); p2 = np.array(hx[j-6], float)
                tri.append((k, i, j) if np.dot(p0, np.cross(p1, p2)) > 0 else (k, j, i))
d1 = sp.zeros(N, 36)
for n_, (i, j) in enumerate(edges): d1[j, n_] = 1; d1[i, n_] = -1
d2 = sp.zeros(36, 24)
def esign(u, v): return (eidx[(u, v)], 1) if u < v else (eidx[(v, u)], -1)
for n_, (u, v, w) in enumerate(tri):
    for (p, q) in ((u, v), (v, w), (w, u)):
        e, sg = esign(p, q); d2[e, n_] += sg
check("d1 d2 = 0, rank d1 = 13, rank d2 = 23, outward boundaries sum to zero", (d1*d2).is_zero_matrix and d1.rank() == 13 and d2.rank() == 23 and (d2*sp.ones(24, 1)).is_zero_matrix)
print("\n   R2 (the bridge): verification/lean/FaceGraph/FaceGraph/Graph.lean defines the adjacency rule and the gauge formula above as Lean functions and proves")
print("   Lgraph_eq_Lfin, Sgraph_eq_Sfin, Dre_eq_D6r, Dim_eq_D6i (decide +kernel), hence charpoly_Lgraph, charpoly_Sgraph, charpoly_Dgraph for the rule-built matrices.")
print()
if FAILED: print("FAILED", FAILED); sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
