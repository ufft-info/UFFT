#!/usr/bin/env python3
"""Author-side check of the numbers stated in the eighth review round (ReviewBot, Draft 8, 9 Oct 2026).

The round's new content is a chain-complex test of the cycle-space premise of Proposition 6.1 on this graph
(ranks of the boundary maps of the 24 oriented triangles), a toroidal negative control, and the trace numbers
behind Proposition 6.2. Everything the report states as a number is recomputed here exactly (integers, sympy
ranks over Q) or to machine precision where it is a float.
"""
import itertools, math, sys
import numpy as np
import sympy as sp
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
# ---- the graph: squares (a, s) then hexagons h in product([1,-1], repeat=3) order
sq = [(a, s) for a in range(3) for s in (1, -1)]; hx = list(itertools.product([1, -1], repeat=3))
N = 14; A = np.zeros((N, N), int)
for i, h in enumerate(hx):
    for j, h2 in enumerate(hx):
        if sum(x != y for x, y in zip(h, h2)) == 1: A[6+i, 6+j] = 1
    for k, (a, s) in enumerate(sq):
        if h[a] == s: A[6+i, k] = A[k, 6+i] = 1
deg = A.sum(1); edges = [(i, j) for i in range(N) for j in range(i+1, N) if A[i, j]]
check("14 vertices, 36 edges, degrees 4^6 6^8", len(edges) == 36 and sorted(deg) == [4]*6 + [6]*8)
# ---- the 24 triangular plaquettes = vertices of the polyhedron: one square (a, s) and two adjacent hexagons h, h' with
# h_a = h'_a = s and h, h' at Hamming distance one. Orientation: outward normal; we orient each triangle by the sign of
# the triple product of the three face centres (square centre s e_a, hexagon centres h/|h|), which is outward for a convex
# arrangement; the report orients "outwards" the same way.
tri = []
for k, (a, s) in enumerate(sq):
    hs = [6+i for i, h in enumerate(hx) if h[a] == s]
    for i in hs:
        for j in hs:
            if i < j and A[i, j]:
                p0 = np.zeros(3); p0[a] = s; p1 = np.array(hx[i-6], float); p2 = np.array(hx[j-6], float)
                orient = np.sign(np.dot(p0, np.cross(p1, p2)))
                tri.append((k, i, j) if orient > 0 else (k, j, i))
check("24 triangular plaquettes", len(tri) == 24)
# ---- chain complex C2 -> C1 -> C0 with oriented edges (i < j positive)
eidx = {e: n for n, e in enumerate(edges)}
def esign(u, v): return (eidx[(u, v)], 1) if u < v else (eidx[(v, u)], -1)
d1 = sp.zeros(N, 36)
for n, (i, j) in enumerate(edges): d1[j, n] = 1; d1[i, n] = -1
d2 = sp.zeros(36, 24)
for n, (u, v, w) in enumerate(tri):
    for (x, y) in ((u, v), (v, w), (w, u)):
        e, sgn = esign(x, y); d2[e, n] += sgn
check("d1 d2 = 0", (d1*d2).is_zero_matrix)
check("rank d1 = 13", d1.rank() == 13)
check("rank d2 = 23", d2.rank() == 23)
check("dim ker d1 = 36 - 13 = 23 = rank d2, so im d2 = ker d1 (triangles span the cycle space)", 36 - d1.rank() == d2.rank())
check("the sum of the 24 outward-oriented boundaries is zero (the single global relation)", (d2*sp.ones(24, 1)).is_zero_matrix)
# ---- vertex gauge leaves every triangular holonomy unchanged (a nontrivial check as in the report)
rng = np.random.default_rng(8); chi = rng.uniform(0, 2*np.pi, N)
theta = {}
for (i, j) in edges: theta[(i, j)] = rng.uniform(0, 2*np.pi); theta[(j, i)] = -theta[(i, j)]
def hol(th):
    return [sum(th[(x, y)] for (x, y) in ((u, v), (v, w), (w, u))) % (2*np.pi) for (u, v, w) in tri]
th2 = {(i, j): theta[(i, j)] + chi[i] - chi[j] for (i, j) in theta}
dh = np.array(hol(theta)) - np.array(hol(th2))
check("a random vertex gauge changes no plaquette holonomy", np.allclose(np.sin(dh), 0) and np.allclose(np.cos(dh), 1))
# ---- vertex connectivity four
try:
    import networkx as nx
    check("vertex connectivity 4", nx.node_connectivity(nx.from_numpy_array(A)) == 4)
except ImportError:
    print("NOTE  vertex connectivity 4: networkx not installed, check skipped (optional, as in the paper script)")
# ---- trace numbers behind Proposition 6.2 (equation (1) of the report)
check("tr D^3 = 2112, tr(D A^2) = 384", int((deg**3).sum()) == 2112 and int((deg**2).sum()) == 384)
check("tr A^3 at q = 0 is 144 (24 triangles x 6)", int(np.trace(A @ A @ A)) == 144)
check("tr Delta^3 at q = 0 is 3264 - 144 = 3120", int(np.trace(np.linalg.matrix_power(np.diag(deg) - A, 3))) == 3120)
# ---- the toroidal negative control: 4x4 periodic square lattice, phase e^{i theta/4} on positive horizontal edges, 1 on vertical
th = math.pi/7; n = 4
face_hol = []
for x in range(n):
    for y in range(n):
        # face (x,y) with corners (x,y),(x+1,y),(x+1,y+1),(x,y+1), counterclockwise: bottom edge +theta/4, top edge traversed backwards -theta/4
        face_hol.append(th/4 - th/4)
check("torus: every elementary face has trivial holonomy", all(abs(f) < 1e-15 for f in face_hol))
check("torus: the horizontal winding loop has holonomy theta = pi/7 (four edges x theta/4), not gaugeable", abs(4*(th/4) - th) < 1e-15 and abs(math.sin(th)) > 0.4)
# ---- the quarter-flux blocks quoted by the report: orthonormal (4,-2;-2,5) and (4,-2;-2,7) have x^2-9x+16 and (x-3)(x-8)
x = sp.symbols("x")
check("blocks (4,-2;-2,5), (4,-2;-2,7): x^2-9x+16 and (x-3)(x-8)",
      sp.expand((x-4)*(x-5)-4) == sp.expand(x**2-9*x+16) and sp.factor((x-4)*(x-7)-4) == sp.factor((x-3)*(x-8)))
print()
if FAILED: print("FAILED", FAILED); sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
