#!/usr/bin/env python3
"""
verify_tetrakis_charpoly_2026-10-06.py   (NumPy only; exact integer arithmetic)

Independent confirmation of the Kelvin-cell face spectrum against a tabulated graph.

The face-adjacency graph of the truncated octahedron (14 faces, two faces adjacent
when they share an edge) is the tetrakis hexahedral graph: 6 vertices of degree 4
(the squares) and 8 of degree 6 (the hexagons). MathWorld tabulates its adjacency
characteristic polynomial as

    x^2 (x+1)^3 (x+3) (x^2 - 3x - 12) (x^2 - x - 4)^3 .

This script builds the cell from its vertices (all permutations of (0, +-1, +-2)),
derives the faces and the face-adjacency matrix from scratch, computes characteristic
polynomials EXACTLY with the Faddeev-LeVerrier recursion in Python integers, and checks:

  1. the adjacency characteristic polynomial equals the tabulated one;
  2. the face-Laplacian characteristic polynomial is
         x (x-9) (x-7)^4 (x-4)^2 (x^2 - 9x + 16)^3 ;
  3. the two irrational factors have the same discriminant, 17.

Exit status is nonzero on any failure. Requires numpy only (used for the integer
matrix products; everything is exact).
"""
import itertools
import sys

import numpy as np

fails = 0


def check(name, ok):
    global fails
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails += 1


# --- exact polynomial helpers (coefficient lists, highest degree first) -----------
def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def ppow(a, n):
    r = [1]
    for _ in range(n):
        r = pmul(r, a)
    return r


def charpoly(M):
    """Faddeev-LeVerrier: coefficients of det(xI - M), exact for integer M."""
    n = M.shape[0]
    M = M.astype(object)
    I = np.identity(n, dtype=object)
    coeffs = [1]
    Mk = np.zeros((n, n), dtype=object)
    c = 1
    for k in range(1, n + 1):
        Mk = M @ (Mk + c * I)
        c = -sum(Mk[i, i] for i in range(n)) // k
        coeffs.append(c)
    return coeffs


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

A = np.zeros((14, 14), dtype=np.int64)
for i in range(14):
    for j in range(i + 1, 14):
        if len(set(faces[i]) & set(faces[j])) == 2:   # share an edge
            A[i, j] = A[j, i] = 1
deg = A.sum(1)
check("degrees: squares 4, hexagons 6",
      sorted(int(d) for d in deg) == [4] * 6 + [6] * 8)
check("36 edges of the cell = 36 face adjacencies", int(A.sum()) // 2 == 36)

# --- characteristic polynomials ------------------------------------------------
adj_cp = charpoly(A)
x = [1, 0]
tabulated = [1]
for factor, power in (([1, 0], 2), ([1, 1], 3), ([1, 3], 1), ([1, -3, -12], 1), ([1, -1, -4], 3)):
    tabulated = pmul(tabulated, ppow(factor, power))
check("adjacency charpoly = MathWorld tetrakis hexahedral graph", adj_cp == tabulated)

L = np.diag(deg) - A
lap_cp = charpoly(L)
expected = [1]
for factor, power in (([1, 0], 1), ([1, -9], 1), ([1, -7], 4), ([1, -4], 2), ([1, -9, 16], 3)):
    expected = pmul(expected, ppow(factor, power))
check("face-Laplacian charpoly = x(x-9)(x-7)^4(x-4)^2(x^2-9x+16)^3", lap_cp == expected)

disc = lambda b, c: b * b - 4 * c          # discriminant of x^2 + b x + c
check("disc(x^2 - x - 4) = 17", disc(-1, -4) == 17)
check("disc(x^2 - 9x + 16) = 17", disc(-9, 16) == 17)
check("both quadratics split over the same field Q(sqrt17)", disc(-1, -4) == disc(-9, 16))

# numerical cross-check of the spectrum (floating point, for the reader)
w = np.sort(np.linalg.eigvalsh(L.astype(float)))
r1, r2 = (9 - 17 ** 0.5) / 2, (9 + 17 ** 0.5) / 2
target = sorted([0, r1, r1, r1, 4, 4, r2, r2, r2, 7, 7, 7, 7, 9])
check("numerical spectrum matches {0, r1^3, 4^2, r2^3, 7^4, 9}", np.allclose(w, target))

print()
print("adjacency charpoly coefficients :", adj_cp)
print("Laplacian charpoly coefficients :", lap_cp)
print("ALL PASS" if fails == 0 else f"{fails} FAIL")
sys.exit(1 if fails else 0)
