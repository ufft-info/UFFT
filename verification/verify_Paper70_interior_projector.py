"""
Verification script for Paper #70.

Confirms:
 1. Face Laplacian of the Kelvin cell has spectrum {0, r_1, 4, r_2, 7, 9}
    with multiplicities (1, 3, 2, 3, 4, 1) per Paper #5 / Paper #53.
 2. The interior-spectrum projector P_int = projector onto im L ∩ im(9I - L)
    has rank 12 = F - chi.
 3. tr(P_int) / F = 12 / 14 = 6/7 exactly.
 4. P_int = I - P_A1g - P_A2u numerically to ~1e-15.
 5. The A_2u eigenvector tracks the hex-subgraph bipartition (signed product
    of hex-face coordinates) exactly.

Run:
    python3 verify_Paper70_interior_projector.py
"""

import numpy as np
from itertools import combinations
from collections import Counter

# --- Build the face-adjacency graph of the truncated octahedron ---
faces = []
face_type = []   # 0 = square, 1 = hex
for axis in range(3):
    for sign in (+1, -1):
        c = [0, 0, 0]; c[axis] = 2 * sign
        faces.append(tuple(c)); face_type.append(0)
for sx in (+1, -1):
    for sy in (+1, -1):
        for sz in (+1, -1):
            faces.append((sx, sy, sz)); face_type.append(1)

N = 14
A = np.zeros((N, N))
for i, j in combinations(range(N), 2):
    d2 = sum((faces[i][k] - faces[j][k]) ** 2 for k in range(3))
    if d2 in (3, 4):
        A[i, j] = A[j, i] = 1.0
deg = A.sum(axis=1)
L = np.diag(deg) - A

# --- (1) Spectrum check ---
eigs = np.round(np.linalg.eigvalsh(L), 4)
spec = Counter(eigs.tolist())
r1 = (9 - np.sqrt(17)) / 2
r2 = (9 + np.sqrt(17)) / 2
expected = Counter({0.0: 1, round(r1, 4): 3, 4.0: 2, round(r2, 4): 3, 7.0: 4, 9.0: 1})
assert spec == expected, f"Spectrum mismatch: {spec} vs {expected}"
print(f"Spectrum: {dict(sorted(spec.items()))}")

# --- (2)(3) Interior-spectrum projector ---
w, V = np.linalg.eigh(L)
P_int = sum(
    np.outer(V[:, i], V[:, i])
    for i in range(N)
    if 1e-6 < w[i] < 9 - 1e-6
)
assert abs(np.trace(P_int) - 12) < 1e-10
print(f"tr(P_int) = {np.trace(P_int):.6f}  (expected 12)")
print(f"tr(P_int) / F = 12 / 14 = 6/7 = {np.trace(P_int) / N:.6f}")

# --- (4) P_int equals I - P_A1g - P_A2u ---
a1g = V[:, [i for i, wi in enumerate(w) if abs(wi) < 1e-8][0]]
a2u = V[:, [i for i, wi in enumerate(w) if abs(wi - 9) < 1e-8][0]]
P_A1g = np.outer(a1g, a1g) / np.dot(a1g, a1g)
P_A2u = np.outer(a2u, a2u) / np.dot(a2u, a2u)
P_complement = np.eye(N) - P_A1g - P_A2u
err = np.linalg.norm(P_int - P_complement)
print(f"‖P_int − (I − P_A1g − P_A2u)‖_F = {err:.2e}")
assert err < 1e-10

# --- (5) A_2u ↔ hex bipartition ---
hex_sign_product = [int(np.prod(faces[6 + i])) for i in range(8)]
a2u_norm = a2u / np.max(np.abs(a2u))
# Fix overall sign so hex-sign products give +1 consistently
if a2u_norm[6] * hex_sign_product[0] < 0:
    a2u_norm = -a2u_norm
products = [float(a2u_norm[6 + i] * hex_sign_product[i]) for i in range(8)]
print(f"A_2u hex components × hex sign products: {[round(p, 4) for p in products]}")
assert all(abs(p - 1.0) < 1e-8 for p in products), products

# --- Kernel of L(L - 9I) = span(A_1g, A_2u) ---
M = L @ (L - 9 * np.eye(N))
zero_mult = sum(1 for e in np.linalg.eigvalsh(M) if abs(e) < 1e-6)
print(f"dim ker(L(L - 9I)) = {zero_mult}  (expected 2)")
assert zero_mult == 2

print("\nAll Paper #70 projector and bipartite-structure checks pass.")
