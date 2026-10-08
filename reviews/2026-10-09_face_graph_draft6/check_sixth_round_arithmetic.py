#!/usr/bin/env python3
"""Author-side check of the arithmetic stated in the sixth review round (ReviewBot, Draft 6, 8 Oct 2026).
Every number the report asserts about the face graph is recomputed here from the adjacency rule alone."""
import itertools, math, sys
import numpy as np
from fractions import Fraction
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
sq = [(a, s) for a in range(3) for s in (1, -1)]; hx = list(itertools.product([1, -1], repeat=3)); V = sq + hx
A = np.zeros((14, 14), int)
for i, h in enumerate(hx):
    for j, h2 in enumerate(hx):
        if sum(x != y for x, y in zip(h, h2)) == 1: A[6+i, 6+j] = 1
    for k, (a, s) in enumerate(sq):
        if h[a] == s: A[6+i, k] = A[k, 6+i] = 1
d = A.sum(1); D = np.diag(d); L = D - A
check("14 vertices, 36 edges, degrees 4^6 6^8", A.sum() == 72 and sorted(d) == [4]*6 + [6]*8)
tri = int(np.trace(A @ A @ A)//6)
trA4 = int(np.trace(np.linalg.matrix_power(A, 4))); c4 = (trA4 - 2*int((d**2).sum()) + int(d.sum()))//8
check("24 triangles; tr A^4 = 1032, sum d^2 = 384, sum d = 72, hence c4 = 42", tri == 24 and trA4 == 1032 and (d**2).sum() == 384 and d.sum() == 72 and c4 == 42)
check("tr D^3 = 2112 and 3 tr(D A^2) = 1152, so the charge-independent part of tr Delta_q^3 is 3264", int(np.trace(D@D@D)) == 2112 and 3*int(np.trace(D@A@A)) == 1152)
w = np.linalg.eigvalsh(L.astype(float)); r1, r2 = (9-math.sqrt(17))/2, (9+math.sqrt(17))/2
check("Laplacian spectrum 0, 9, 7^4, 4^2, ((9 +- sqrt17)/2)^3", np.allclose(sorted(w), sorted([0, 9] + [7]*4 + [4]*2 + [r1]*3 + [r2]*3), rtol=0, atol=1e-10))
check("fourth moment at q = 0 is 22344", abs((w**4).sum() - 22344) < 1e-6, f"{(w**4).sum():.6f}")
# K on the orbit-constant plane: K 1_s = 3 1_h, K 1_h = -4 1_s, so K^2 = -12 I there
Ps = np.diag([1]*6 + [0]*8); Ph = np.eye(14) - Ps; K = Ps @ L @ Ph - Ph @ L @ Ps
one_s = np.array([1]*6 + [0]*8, float); one_h = np.array([0]*6 + [1]*8, float)
check("K 1_s = 3 1_h and K 1_h = -4 1_s (orbit-constant plane), so K^2 = -12 I there", np.allclose(K @ one_s, 3*one_h) and np.allclose(K @ one_h, -4*one_s))
# spanning trees by exact cofactor
M = [[Fraction(int(L[i, j])) for j in range(1, 14)] for i in range(1, 14)]
def det(M):
    M = [r[:] for r in M]; n = len(M); s = Fraction(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None: return Fraction(0)
        if p != i: M[i], M[p] = M[p], M[i]; s = -s
        s *= M[i][i]
        for r in range(i+1, n):
            f = M[r][i]/M[i][i]
            for c in range(i, n): M[r][c] -= f*M[i][c]
    return s
check("spanning trees 101,154,816 = 9 * 7^4 * 4^2 * 16^3 / 14", det(M) == 101154816 and Fraction(9*7**4*4**2*16**3, 14) == 101154816)
# the report's own weighted total
rows = [(0.45, 9.25), (0.225, 9.26), (0.18, 9.24), (0.045, 6.22), (0.07, 9.30), (0.03, 9.50)]
tot = sum(a*b for a, b in rows)
print(f"   report's category table: weights sum {sum(a for a,_ in rows):.3f}; weighted total recomputed {tot:.4f} (report states 9.123, rounded 9.1)")
check("weighted total rounds to the stated 9.1 (the third decimal differs: 9.125 here vs 9.123 printed; the per-category contributions printed sum to 9.124)", round(tot, 1) == 9.1)
print()
if FAILED: print("FAILED", FAILED); sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
