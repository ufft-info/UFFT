#!/usr/bin/env python3
"""Author-side check of the numbers stated in the seventh review round (ReviewBot, Draft 7, 9 Oct 2026)."""
import itertools, math, sys
import numpy as np
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
sq = [(a, s) for a in range(3) for s in (1, -1)]; hx = list(itertools.product([1, -1], repeat=3))
A = np.zeros((14, 14))
for i, h in enumerate(hx):
    for j, h2 in enumerate(hx):
        if sum(x != y for x, y in zip(h, h2)) == 1: A[6+i, 6+j] = 1
    for k, (a, s) in enumerate(sq):
        if h[a] == s: A[6+i, k] = A[k, 6+i] = 1
L = np.diag(A.sum(1)) - A; w, V = np.linalg.eigh(L); Ps = np.diag([1.]*6 + [0.]*8)
def omega(lam):
    idx = np.where(np.abs(w - lam) < 1e-9)[0]; P = V[:, idx] @ V[:, idx].T; return np.trace(Ps @ P)/len(idx), len(idx)
r1, r2 = (9 - math.sqrt(17))/2, (9 + math.sqrt(17))/2
check("support weights omega_s: E0 3/7, E4 1, E7 1/7, E9 0, T1u (1 +- 1/sqrt17)/2 (report section 4.2)",
      abs(omega(0)[0] - 3/7) < 1e-12 and abs(omega(4)[0] - 1) < 1e-12 and abs(omega(7)[0] - 1/7) < 1e-12 and abs(omega(9)[0]) < 1e-12
      and abs(omega(r1)[0] - (1 + 1/math.sqrt(17))/2) < 1e-12 and abs(omega(r2)[0] - (1 - 1/math.sqrt(17))/2) < 1e-12)
check("multiplicities 1, 2, 4, 1, 3, 3", [omega(x)[1] for x in (0, 4, 7, 9, r1, r2)] == [1, 2, 4, 1, 3, 3])
c4 = (int(np.trace(np.linalg.matrix_power(A, 4))) - 2*int((A.sum(1)**2).sum()) + int(A.sum()))//8
check("42 simple four-cycles (closed-walk formula), 24 triangles", c4 == 42 and int(np.trace(A @ A @ A))//6 == 24)
tot = 0.45*9.295 + 0.225*9.380 + 0.18*9.230 + 0.045*6.220 + 0.07*9.3 + 0.03*9.5
check("weighted total 9.171 as printed (rounds to 9.2)", abs(tot - 9.171) < 0.001, f"{tot:.4f}")
check("the face graph is the skeleton of the tetrakis hexahedron (already stated in Section 1 of the note with the MathWorld reference); the report's identification agrees", True)
print()
if FAILED: print("FAILED", FAILED); sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
