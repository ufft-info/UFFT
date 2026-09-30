"""
face_laplacian_matrix.py

Explicit face-adjacency matrix A and face Laplacian L = D - A of the
truncated octahedron (Kelvin cell), as referenced in Paper #63,
Appendix B (DOI 10.5281/zenodo.19624955).

Face labels follow Paper #63: faces 1-8 are hexagons, faces 9-14 are
squares (printed 1-based; stored 0-based in the arrays).

  hexagons 1-8  : outward normals (sx, sy, sz), each s = +-1
  squares  9-14 : outward normals +x, -x, +y, -y, +z, -z

Adjacency (two faces share a cell edge):
  hex-hex : normals differ in exactly one sign        (12 edges)
  hex-sq  : the hexagon's sign on the square's axis
            matches the square's sign                  (24 edges)
  sq-sq   : never                                      (0 edges)
Total 36 edges = E of the truncated octahedron.

Checks (PASS/FAIL, nonzero exit on failure):
  1. 14 faces, 36 edges, hexagon degree 6, square degree 4
  2. spectrum of L = {0^1, r1^3, 4^2, r2^3, 7^4, 9^1}, r1,2 = (9 -+ sqrt17)/2,
     to 1e-12
  3. r1, r2 are the roots of the master equation lambda^2 - 9 lambda + 16 = 0
"""
import itertools
import sys

import numpy as np

hex_normals = [np.array(s) for s in itertools.product((1, -1), repeat=3)]
sq_normals = []
for axis in range(3):
    for sign in (1, -1):
        v = np.zeros(3, dtype=int)
        v[axis] = sign
        sq_normals.append(v)

N_HEX, N_SQ = 8, 6
F = N_HEX + N_SQ
A = np.zeros((F, F), dtype=int)

for i in range(N_HEX):
    for j in range(i + 1, N_HEX):
        if np.sum(hex_normals[i] != hex_normals[j]) == 1:
            A[i, j] = A[j, i] = 1

for i in range(N_HEX):
    for k, s in enumerate(sq_normals):
        axis = int(np.flatnonzero(s)[0])
        if hex_normals[i][axis] == s[axis]:
            j = N_HEX + k
            A[i, j] = A[j, i] = 1

D = np.diag(A.sum(axis=1))
L = D - A

r1 = (9 - np.sqrt(17)) / 2
r2 = (9 + np.sqrt(17)) / 2
expected = np.sort([0.0] + [r1] * 3 + [4.0] * 2 + [r2] * 3 + [7.0] * 4 + [9.0])

fails = 0


def check(name, ok):
    global fails
    print(("PASS " if ok else "FAIL ") + name)
    fails += 0 if ok else 1


def show(M, title):
    labels = [f"H{i+1}" for i in range(N_HEX)] + [f"S{k+9}" for k in range(N_SQ)]
    print(title)
    print("     " + " ".join(f"{l:>3}" for l in labels))
    for l, row in zip(labels, M):
        print(f"{l:>4} " + " ".join(f"{x:>3}" for x in row))
    print()


if __name__ == "__main__":
    show(A, "Face-adjacency matrix A (H = hexagon, S = square; Paper #63 labels)")
    show(L, "Face Laplacian L = D - A")

    edges = int(A.sum()) // 2
    deg = A.sum(axis=1)
    check("14 faces", F == 14)
    check(f"36 edges (got {edges})", edges == 36)
    check("12 hex-hex edges", int(A[:N_HEX, :N_HEX].sum()) // 2 == 12)
    check("24 hex-square edges", int(A[:N_HEX, N_HEX:].sum()) == 24)
    check("hexagon degree 6", np.all(deg[:N_HEX] == 6))
    check("square degree 4", np.all(deg[N_HEX:] == 4))

    ev = np.sort(np.linalg.eigvalsh(L.astype(float)))
    print("Eigenvalues of L:", np.round(ev, 12))
    err = float(np.max(np.abs(ev - expected)))
    check(f"spectrum {{0, r1^3, 4^2, r2^3, 7^4, 9}} (max error {err:.1e})", err < 1e-12)
    check("r1, r2 solve lambda^2 - 9 lambda + 16 = 0",
          abs(r1**2 - 9 * r1 + 16) < 1e-12 and abs(r2**2 - 9 * r2 + 16) < 1e-12)

    print(f"\n{'ALL PASS' if fails == 0 else f'{fails} FAIL'}")
    sys.exit(1 if fails else 0)
