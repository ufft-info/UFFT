"""
Verify face Laplacian spectra for all five Fedorov parallelohedra.
v2: corrected adjacency for rhombic dodecahedron and elongated dodecahedron.
"""
import numpy as np
from numpy.linalg import eigvalsh

def face_laplacian(adj):
    D = np.diag(adj.sum(axis=1))
    return D - adj

def print_spectrum(name, F, eigs, adj, expected_trace=None):
    print(f"=== {name} (F={F}) ===")
    print(f"Eigenvalues: {np.round(eigs, 6)}")
    degs = adj.sum(axis=1)
    unique_degs = sorted(set(degs))
    deg_str = ", ".join(f"{int(d)}×{int(np.sum(degs==d))}" for d in unique_degs)
    print(f"Degrees: {deg_str}")
    print(f"Trace: {int(np.trace(face_laplacian(adj)))}" + (f" (expected {expected_trace})" if expected_trace else ""))
    # Check eigenvalue multiplicities
    rounded = np.round(eigs, 4)
    unique_eigs = []
    for e in sorted(set(rounded)):
        mult = np.sum(rounded == e)
        unique_eigs.append((e, int(mult)))
    print(f"Spectrum: " + ", ".join(f"{e:.4f}^{m}" for e, m in unique_eigs))

    # Check for irrationals
    all_integer = all(abs(e - round(e)) < 0.001 for e in eigs)
    print(f"All integer eigenvalues: {all_integer}")
    print()
    return unique_eigs

# ============================================================
# 1. CUBE (F=6)
# 6 square faces, each adjacent to 4 others (all except its opposite)
# ============================================================
cube_adj = np.array([
    #  +x -x +y -y +z -z
    [0, 0, 1, 1, 1, 1],  # +x adj to +y,-y,+z,-z
    [0, 0, 1, 1, 1, 1],  # -x adj to +y,-y,+z,-z
    [1, 1, 0, 0, 1, 1],  # +y adj to +x,-x,+z,-z
    [1, 1, 0, 0, 1, 1],  # -y adj to +x,-x,+z,-z
    [1, 1, 1, 1, 0, 0],  # +z adj to +x,-x,+y,-y
    [1, 1, 1, 1, 0, 0],  # -z adj to +x,-x,+y,-y
], dtype=float)
eigs_cube = np.sort(eigvalsh(face_laplacian(cube_adj)))
print_spectrum("CUBE", 6, eigs_cube, cube_adj, "24")

# ============================================================
# 2. HEXAGONAL PRISM (F=8)
# 2 hexagons (top/bottom, deg 6) + 6 rectangles (sides, deg 4)
# ============================================================
hp_adj = np.zeros((8,8))
for i in range(2,8):
    hp_adj[0,i] = hp_adj[i,0] = 1
    hp_adj[1,i] = hp_adj[i,1] = 1
for i in range(6):
    j = (i+1) % 6
    hp_adj[2+i, 2+j] = hp_adj[2+j, 2+i] = 1
eigs_hp = np.sort(eigvalsh(face_laplacian(hp_adj)))
print_spectrum("HEXAGONAL PRISM", 8, eigs_hp, hp_adj, "36")

# ============================================================
# 3. RHOMBIC DODECAHEDRON (F=12)
# 12 rhombic faces. Face normals = cuboctahedron vertices =
# permutations of (±1,±1,0). Each face degree 4.
# Two faces adj iff dot product of normals = +1 (distance √2 on cuboctahedron)
# ============================================================
rd_normals = []
for i in range(3):
    for s1 in [1,-1]:
        for s2 in [1,-1]:
            n = [0,0,0]
            n[(i+1)%3] = s1
            n[(i+2)%3] = s2
            rd_normals.append(n)

rd_adj = np.zeros((12,12))
for i in range(12):
    for j in range(i+1,12):
        dot = sum(rd_normals[i][k]*rd_normals[j][k] for k in range(3))
        if dot == 1:  # NOT |dot|==1; only +1 gives shared edge
            rd_adj[i,j] = rd_adj[j,i] = 1

eigs_rd = np.sort(eigvalsh(face_laplacian(rd_adj)))
print_spectrum("RHOMBIC DODECAHEDRON", 12, eigs_rd, rd_adj, "48")

# ============================================================
# 4. ELONGATED DODECAHEDRON (F=12)
# Also called elongated rhombic dodecahedron or Bilinski dodecahedron variant.
# 4 hexagonal faces + 8 rhombic faces (Fedorov's version)
# OR equivalently described as having D_{2h} symmetry.
#
# Actually, the Fedorov elongated dodecahedron has:
# - 4 rhombic faces of one type (the "belt")
# - 4 rhombic faces of another type (top cap)
# - 4 rhombic faces of another type (bottom cap)
# All 12 faces are rhombi, each with 4 edges, so degree 4.
#
# The simplest construction: take the rhombic dodecahedron and
# stretch along one axis. The symmetry reduces from O_h to D_{4h}.
#
# Face normals of the elongated dodecahedron (D_{4h} version):
# Belt (4 faces): (±1,±1,0) — same as RD, in xy-plane
# Top cap (4 faces): (±1,0,1), (0,±1,1)  — pointing up
# Bottom cap (4 faces): (±1,0,-1), (0,±1,-1) — pointing down
#
# Adjacency: each belt face adj to 2 top cap + 2 bottom cap = 4
# Each cap face adj to 2 belt + 2 same-hemisphere cap = 4
# Actually this gives degree 4 for all faces.
# ============================================================

# Let's construct carefully.
# Belt faces: normals (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0)
# Top faces: normals (1,0,1), (-1,0,1), (0,1,1), (0,-1,1)
# Bottom faces: normals (1,0,-1), (-1,0,-1), (0,1,-1), (0,-1,-1)

ed_normals = [
    # Belt (indices 0-3)
    (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0),
    # Top cap (indices 4-7)
    (1,0,1), (-1,0,1), (0,1,1), (0,-1,1),
    # Bottom cap (indices 8-11)
    (1,0,-1), (-1,0,-1), (0,1,-1), (0,-1,-1)
]

# For the elongated dodecahedron, the adjacency is different from RD
# because the stretching changes which faces share edges.
# Two faces share an edge iff they meet along a ridge.
# In the elongated case with D_{4h} symmetry:
#
# Belt-Top adjacency: belt (a,b,0) adj to top (c,0,1) if they share
# a sign: belt(1,1,0) adj to top(1,0,1) and top(0,1,1)
# Belt-Bottom: same pattern with z=-1
# Top-Top adjacency: top(1,0,1) adj to top(0,1,1) and top(0,-1,1)
# Bottom-Bottom: same pattern
# Belt-Belt: NOT adjacent (after elongation, belt faces don't share edges)

ed_adj = np.zeros((12,12))

# Belt-Top: belt (a,b,0) adj to top faces that share the a or b component
# belt(1,1,0) → top(1,0,1), top(0,1,1)
# belt(1,-1,0) → top(1,0,1), top(0,-1,1)
# belt(-1,1,0) → top(-1,0,1), top(0,1,1)
# belt(-1,-1,0) → top(-1,0,1), top(0,-1,1)
belt_top = [
    (0, 4), (0, 6),   # (1,1,0) → (1,0,1), (0,1,1)
    (1, 4), (1, 7),   # (1,-1,0) → (1,0,1), (0,-1,1)
    (2, 5), (2, 6),   # (-1,1,0) → (-1,0,1), (0,1,1)
    (3, 5), (3, 7),   # (-1,-1,0) → (-1,0,1), (0,-1,1)
]
for i,j in belt_top:
    ed_adj[i,j] = ed_adj[j,i] = 1

# Belt-Bottom: same pattern
belt_bot = [
    (0, 8), (0, 10),  # (1,1,0) → (1,0,-1), (0,1,-1)
    (1, 8), (1, 11),  # (1,-1,0) → (1,0,-1), (0,-1,-1)
    (2, 9), (2, 10),  # (-1,1,0) → (-1,0,-1), (0,1,-1)
    (3, 9), (3, 11),  # (-1,-1,0) → (-1,0,-1), (0,-1,-1)
]
for i,j in belt_bot:
    ed_adj[i,j] = ed_adj[j,i] = 1

# Top-Top: adjacent pairs within top cap
# (1,0,1)-(0,1,1), (1,0,1)-(0,-1,1) are adjacent? No, only consecutive around cap.
# Top cap forms a cycle: (1,0,1)→(0,1,1)→(-1,0,1)→(0,-1,1)→(1,0,1)
top_cycle = [(4,6), (6,5), (5,7), (7,4)]
for i,j in top_cycle:
    ed_adj[i,j] = ed_adj[j,i] = 1

# Bottom-Bottom: same cycle
bot_cycle = [(8,10), (10,9), (9,11), (11,8)]
for i,j in bot_cycle:
    ed_adj[i,j] = ed_adj[j,i] = 1

# Verify degrees: should be 4 for belt (2 top + 2 bot), 4 for caps (2 belt + 2 cap)
eigs_ed = np.sort(eigvalsh(face_laplacian(ed_adj)))
spec_ed = print_spectrum("ELONGATED DODECAHEDRON (construction 1)", 12, eigs_ed, ed_adj, "48")

# ============================================================
# Alternative: maybe belt faces ARE adjacent to each other.
# In the standard Fedorov elongated dodecahedron, the belt
# consists of 4 faces forming a band around the equator.
# These belt faces DO share edges with their cyclic neighbors.
# Let me try with belt-belt adjacency too.
# ============================================================
ed_adj2 = ed_adj.copy()
# Belt cycle: (1,1,0)→(1,-1,0)→(-1,-1,0)→(-1,1,0)→back
# Wait, that's a cycle of length 4. Which pairs share edges?
# In a prism-like belt: (1,1,0) adj to (1,-1,0) and (-1,1,0)
belt_cycle = [(0,1), (1,3), (3,2), (2,0)]
for i,j in belt_cycle:
    ed_adj2[i,j] = ed_adj2[j,i] = 1

eigs_ed2 = np.sort(eigvalsh(face_laplacian(ed_adj2)))
spec_ed2 = print_spectrum("ELONGATED DODECAHEDRON (construction 2, belt-connected)", 12, eigs_ed2, ed_adj2, "not sure")

# ============================================================
# Let me try yet another approach: the elongated dodecahedron
# has 12 faces where some are pentagons and some are quadrilaterals.
# Fedorov's elongated dodecahedron actually has:
# 4 faces that are hexagons and 8 faces that are quadrilaterals
# OR 8 pentagons + 4 rectangles, depending on the exact form.
#
# Actually, the standard Fedorov classification gives:
# Elongated dodecahedron = hexagonal truncated trapezohedron
# It has 2 hexagonal faces + 12 quadrilateral faces... no wait.
#
# Let me just try: the Fedorov elongated dodecahedron has
# F=12, and the standard description says:
# It's obtained by elongating the rhombic dodecahedron along a 4-fold axis.
# This splits 4 of the 12 rhombic faces into 4 rectangular faces
# and inserts a belt of 4 new rectangular faces... no, F stays at 12.
#
# OK, the key insight is the elongated dodecahedron has the same
# face count (12) as the rhombic dodecahedron. The difference is
# in the face shape and adjacency.
#
# Let me use the definitive source: the elongated dodecahedron
# has 8 vertices of degree 3 and 4 vertices of degree 4, with
# 12 faces (8 pentagons of one type and 4 rhombi).
#
# ACTUALLY: Some references say F=12 with all 12 faces being
# quadrilaterals (rhombi of two types). Let me just verify with
# the simplest valid construction.
# ============================================================

# Construction 3: All 12 faces are quadrilaterals, all degree 4.
# This matches F=12, all degrees 4, total edges in face graph = 24, trace = 48.
# Construction 1 already gives this! Let me check if it has irrationals.

print()
print("=== CHECKING FOR IRRATIONAL EIGENVALUES ===")
for name, eigs in [("Cube", eigs_cube), ("Hex prism", eigs_hp),
                    ("Rhombic dod", eigs_rd), ("Elongated dod v1", eigs_ed),
                    ("Elongated dod v2", eigs_ed2)]:
    residuals = [abs(e - round(e)) for e in eigs]
    has_irrational = any(r > 0.01 for r in residuals)
    print(f"{name:25s}: irrational = {has_irrational}")
    if has_irrational:
        irr = [e for e in eigs if abs(e - round(e)) > 0.01]
        if len(irr) >= 2:
            s = irr[0] + irr[-1]  # sum of smallest and largest irrational
            p = irr[0] * irr[-1]
            disc = s*s - 4*p
            print(f"  Irrational eigenvalues: {np.round(irr, 6)}")
            print(f"  Sum = {s:.6f}, Product = {p:.6f}")
            print(f"  Minimal poly: λ² - {s:.4f}λ + {p:.4f} = 0")
            print(f"  Discriminant = {disc:.4f}")

# ============================================================
# 5. TRUNCATED OCTAHEDRON (F=14) — already verified, repeat for completeness
# ============================================================
print()
sq_normals = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hex_normals = [(s1,s2,s3) for s1 in [1,-1] for s2 in [1,-1] for s3 in [1,-1]]

trunc_adj = np.zeros((14,14))
for si in range(6):
    sn = sq_normals[si]
    axis = [k for k in range(3) if sn[k] != 0][0]
    sign = sn[axis]
    for hi in range(8):
        hn = hex_normals[hi]
        if hn[axis] == sign:
            trunc_adj[si, 6+hi] = trunc_adj[6+hi, si] = 1

for i in range(8):
    for j in range(i+1,8):
        ni, nj = hex_normals[i], hex_normals[j]
        diff = sum(1 for k in range(3) if ni[k] != nj[k])
        if diff == 1:
            trunc_adj[6+i, 6+j] = trunc_adj[6+j, 6+i] = 1

eigs_trunc = np.sort(eigvalsh(face_laplacian(trunc_adj)))
print_spectrum("TRUNCATED OCTAHEDRON", 14, eigs_trunc, trunc_adj, "72")

r1 = (9 - np.sqrt(17)) / 2
r2 = (9 + np.sqrt(17)) / 2
print("MASTER EQUATION: λ² - 9λ + 16 = 0")
print(f"r₁ = {r1:.10f}, r₂ = {r2:.10f}")
print(f"r₁+r₂ = {r1+r2} = 9 = 3²  ✓")
print(f"r₁×r₂ = {r1*r2} = 16 = Δ-1  ✓")
print(f"Δ = 17 (prime)  ✓")
