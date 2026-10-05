#!/usr/bin/env python3
"""
verify_tetrakis_charpoly_2026-10-06.py

Independent confirmation of the Kelvin-cell face spectrum against a tabulated graph.

The face-adjacency graph of the truncated octahedron (14 faces, two faces adjacent
when they share an edge) is the tetrakis hexahedral graph: 6 vertices of degree 4
(the squares) and 8 of degree 6 (the hexagons). MathWorld tabulates its adjacency
characteristic polynomial as

    x^2 (x+1)^3 (x+3) (x^2 - 3x - 12) (x^2 - x - 4)^3 .

This script builds the cell from its vertices (all permutations of (0, +-1, +-2)),
derives the faces and the face-adjacency matrix from scratch, and checks:

  1. the adjacency characteristic polynomial equals the tabulated one;
  2. the face-Laplacian characteristic polynomial is
         x (x-9) (x-7)^4 (x-4)^2 (x^2 - 9x + 16)^3 ,
     i.e. Spec(L) = {0, ((9-sqrt17)/2)^3, 4^2, ((9+sqrt17)/2)^3, 7^4, 9};
  3. the two irrational factors have the same discriminant, 17.

Exit status is nonzero on any failure. Requires numpy and sympy.
"""
import itertools
import sys

import numpy as np
import sympy as sp

fails = 0


def check(name, ok):
    global fails
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails += 1


# --- cell from scratch ---------------------------------------------------------
V = sorted({tuple(a * b for a, b in zip(p, s))
            for p in itertools.permutations([0, 1, 2])
            for s in itertools.product([1, -1], repeat=3)})
check("24 vertices", len(V) == 24)

faces = []
for ax in range(3):                      # 6 squares: x = +-2, y = +-2, z = +-2
    for s in (2, -2):
        faces.append([i for i, v in enumerate(V) if v[ax] == s])
for sg in itertools.product([1, -1], repeat=3):   # 8 hexagons: +-x +-y +-z = 3
    faces.append([i for i, v in enumerate(V)
                  if sum(a * b for a, b in zip(v, sg)) == 3])
check("14 faces (6 squares, 8 hexagons)",
      len(faces) == 14 and sorted(len(f) for f in faces) == [4] * 6 + [6] * 8)

A = np.zeros((14, 14), int)
for i in range(14):
    for j in range(i + 1, 14):
        if len(set(faces[i]) & set(faces[j])) == 2:   # share an edge
            A[i, j] = A[j, i] = 1
deg = A.sum(1)
check("degrees: squares 4, hexagons 6",
      sorted(int(d) for d in deg) == [4] * 6 + [6] * 8)
check("36 edges of the cell = 36 face adjacencies", int(A.sum()) // 2 == 36)

# --- characteristic polynomials ------------------------------------------------
x = sp.symbols("x")
M = sp.Matrix(A)
adj_cp = sp.expand(M.charpoly(x).as_expr())
tabulated = sp.expand(x**2 * (x + 1)**3 * (x + 3) * (x**2 - 3 * x - 12) * (x**2 - x - 4)**3)
check("adjacency charpoly = MathWorld tetrakis hexahedral graph",
      sp.expand(adj_cp - tabulated) == 0)

L = sp.diag(*[int(d) for d in deg]) - M
lap_cp = sp.expand(L.charpoly(x).as_expr())
expected = sp.expand(x * (x - 9) * (x - 7)**4 * (x - 4)**2 * (x**2 - 9 * x + 16)**3)
check("face-Laplacian charpoly = x(x-9)(x-7)^4(x-4)^2(x^2-9x+16)^3",
      sp.expand(lap_cp - expected) == 0)

check("disc(x^2 - x - 4) = 17", sp.discriminant(x**2 - x - 4, x) == 17)
check("disc(x^2 - 9x + 16) = 17", sp.discriminant(x**2 - 9 * x + 16, x) == 17)

# what is exact is the shared splitting field Q(sqrt17)
r1, r2 = sp.solve(x**2 - 9 * x + 16, x)
a1, a2 = sp.solve(x**2 - x - 4, x)
check("both quadratics split over Q(sqrt17)",
      all(sp.simplify(r - sp.nsimplify(r, [sp.sqrt(17)])) == 0 for r in (r1, r2, a1, a2)))

print()
print("adjacency :", sp.factor(adj_cp))
print("Laplacian :", sp.factor(lap_cp))
print("ALL PASS" if fails == 0 else f"{fails} FAIL")
sys.exit(1 if fails else 0)
