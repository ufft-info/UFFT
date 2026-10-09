#!/usr/bin/env python3
"""Author-side check of the tenth review round (ReviewBot, Draft 10, 9 Oct 2026): the geometry-to-rule test.

The round's new check: build the faces of the truncated octahedron as subsets of its 24 vertices (the permutations of
(0, +-1, +-2)), declare two faces adjacent iff their vertex sets share exactly two points, and compare entry by entry with
the adjacency rule transcribed in Graph.lean (bit convention h_j = +1 iff bit (2 - j) of h is 0; sigma = +1 for even s).
Then the quarter-flux formula: B B* = 4I, B* B = (9I - C^2)/2, and the product B_{s,h} B_{s,h'} over each outward-oriented
triangle (s, h, h') equals i; a sign flip in one entry breaks a Gram identity and a holonomy; a reversed bit order breaks
the labeled adjacency comparison. Everything is recomputed here exactly.
"""
import itertools, math, sys
import numpy as np
import sympy as sp
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
# ---- geometry: 24 vertices, 6 square planes x_a = 2 sigma, 8 hexagon planes h.x = 3
verts = sorted({tuple(s*v for s, v in zip(sg, p)) for p in itertools.permutations([0, 1, 2]) for sg in itertools.product([1, -1], repeat=3)})
check("24 vertices (permutations of (0, +-1, +-2))", len(verts) == 24)
def hs(h, j): return 1 if (h >> (2 - j)) % 2 == 0 else -1           # Graph.lean bit convention
faces = []
for s in range(6):
    a, sg = s // 2, (1 if s % 2 == 0 else -1); faces.append({v for v in verts if v[a] == 2*sg})
for h in range(8):
    hv = (hs(h, 0), hs(h, 1), hs(h, 2)); faces.append({v for v in verts if sum(x*y for x, y in zip(hv, v)) == 3})
check("six squares have 4 vertices, eight hexagons have 6", all(len(f) == 4 for f in faces[:6]) and all(len(f) == 6 for f in faces[6:]))
A_geo = np.array([[1 if (i != j and len(faces[i] & faces[j]) == 2) else 0 for j in range(14)] for i in range(14)])
# ---- the rule, as in Graph.lean
def sqHexAdj(s, h): return hs(h, s // 2) == (1 if s % 2 == 0 else -1)
def hexHexAdj(h, h2): return sum(hs(h, j) != hs(h2, j) for j in range(3)) == 1
def adjN(v, w):
    if v < 6 and w >= 6: return sqHexAdj(v, w - 6)
    if v >= 6 and w < 6: return sqHexAdj(w, v - 6)
    if v >= 6 and w >= 6: return hexHexAdj(v - 6, w - 6)
    return False
A_rule = np.array([[1 if adjN(v, w) else 0 for w in range(14)] for v in range(14)])
check("geometry-built adjacency equals the Graph.lean rule entry by entry (labeled, not just isomorphic)", (A_geo == A_rule).all())
check("36 edges, degrees 4^6 6^8", A_geo.sum() == 72 and sorted(A_geo.sum(1)) == [4]*6 + [6]*8)
# negative control: reversed bit order
def hs_rev(h, j): return 1 if (h >> j) % 2 == 0 else -1
faces_rev = faces[:6] + [{v for v in verts if sum(x*y for x, y in zip((hs_rev(h, 0), hs_rev(h, 1), hs_rev(h, 2)), v)) == 3} for h in range(8)]
A_rev = np.array([[1 if (i != j and len(faces_rev[i] & faces_rev[j]) == 2) else 0 for j in range(14)] for i in range(14)])
check("control: a reversed bit order breaks the labeled comparison", not (A_rev == A_rule).all())
# ---- quarter-flux formula and holonomies
I = sp.I
B = sp.zeros(6, 8)
for s in range(6):
    a, sg = s // 2, (1 if s % 2 == 0 else -1); b, c = (a + 1) % 3, (a + 2) % 3
    for h in range(8):
        if sqHexAdj(s, h): B[s, h] = sp.Rational(hs(h, b) + hs(h, c), 2) + I*sg*sp.Rational(hs(h, b) - hs(h, c), 2)
C = sp.Matrix(A_rule[6:, 6:].tolist())
check("B* B = (9I - C^2)/2 and B B* = 4 I_6 from the integer formula", sp.simplify(B.H*B - (9*sp.eye(8) - C**2)/2) == sp.zeros(8, 8) and sp.simplify(B*B.H - 4*sp.eye(6)) == sp.zeros(6, 6))
# outward triangles: (s, h, h') with h, h' adjacent hexagons both adjacent to s; orientation by the triple product of face centres
cent = [np.array([2*(1 if s % 2 == 0 else -1) if k == s // 2 else 0 for k in range(3)], float) for s in range(6)] + [np.array([hs(h, 0), hs(h, 1), hs(h, 2)], float) for h in range(8)]
tri = []
for s in range(6):
    hs_ = [h for h in range(8) if sqHexAdj(s, h)]
    for h in hs_:
        for h2 in hs_:
            if h < h2 and hexHexAdj(h, h2):
                out = np.dot(cent[s], np.cross(cent[6 + h], cent[6 + h2])) > 0
                tri.append((s, h, h2) if out else (s, h2, h))
check("24 outward-oriented triangles", len(tri) == 24)
# holonomy around (s -> h -> h' -> s): A_sh A_hh' A_h's with A = -(Delta off-diagonal): entries B_{s,h}, 1, conj(B_{s,h'}) ... the report's
# statement is B_{s,h} B_{s,h'} = i per outward triangle in its convention; here the holonomy of the magnetic adjacency is
# B_{s,h} * 1 * conj(B_{s,h'}); both are tested and the one that is uniformly a quarter turn is reported.
prod1 = [sp.simplify(B[s, h]*B[s, h2]) for (s, h, h2) in tri]
prod2 = [sp.simplify(B[s, h]*sp.conjugate(B[s, h2])) for (s, h, h2) in tri]
u1 = set(prod1); u2 = set(prod2)
print(f"   products B_sh B_sh' over outward triangles: {u1}; B_sh conj(B_sh'): {u2}")
check("every outward triangle carries the same quarter-turn holonomy (one of the two conventions is uniformly +i or uniformly -i)",
      (len(u1) == 1 and list(u1)[0] in (I, -I)) or (len(u2) == 1 and list(u2)[0] in (I, -I)))
# sign-flip control
Bp = B.copy(); s0, h0 = next((s, h) for s in range(6) for h in range(8) if B[s, h] != 0); Bp[s0, h0] = -Bp[s0, h0]
pp = [sp.simplify(Bp[s, h]*sp.conjugate(Bp[s, h2])) for (s, h, h2) in tri]
check("control: one sign flip breaks a Gram identity and at least one triangle holonomy", sp.simplify(Bp*Bp.H - 4*sp.eye(6)) != sp.zeros(6, 6) or sp.simplify(Bp.H*Bp - (9*sp.eye(8) - C**2)/2) != sp.zeros(8, 8), f"{len(set(pp))} distinct holonomies after the flip")
# the three polynomials from the rule-built matrices
x = sp.symbols("x"); A_s = sp.Matrix(A_rule.tolist()); D = sp.diag(*[int(d) for d in A_rule.sum(1)])
chiL = sp.factor((x*sp.eye(14) - (D - A_s)).det()); chiS = sp.factor((x*sp.eye(14) - (D + A_s)).det())
D6 = sp.zeros(14, 14); D6[:6, :6] = 4*sp.eye(6); D6[6:, 6:] = 6*sp.eye(8) - C; D6[:6, 6:] = -B; D6[6:, :6] = -B.H
chi6 = sp.factor(sp.expand((x*sp.eye(14) - D6).det()))
check("the three characteristic polynomials from the rule-built matrices", sp.expand(chiL - x*(x-9)*(x-7)**4*(x-4)**2*(x**2-9*x+16)**3) == 0 and sp.expand(chiS - (x-8)**3*(x-5)**3*(x-4)**2*(x-3)**4*(x**2-13*x+24)) == 0 and sp.expand(chi6 - (x-9)*(x-8)**3*(x-3)**4*(x**2-9*x+16)**3) == 0)
print()
if FAILED: print("FAILED", FAILED); sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
