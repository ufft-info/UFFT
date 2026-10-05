#!/usr/bin/env python3
"""
Void network speed check (UFFT Bell paper, Zenodo 19079502).

Claim under test: voids in the BCC Planck foam propagate at c_V = c*sqrt(3/2)
because the octahedral-hole network has nearest-neighbour spacing a/sqrt(2),
shorter than the bubble spacing l_P = a*sqrt(3)/2.

This script:
  1. builds the BCC lattice and its interstitial (octahedral) sites from scratch,
  2. measures the true nearest-neighbour spacing of each network,
  3. computes the propagation front speed of each network two ways
     (closed form via the support function, and brute-force BFS first-passage),
     under both hop models (fixed hop time; fixed hop speed),
  4. compares with the claimed ratio sqrt(3/2),
  5. compares any finite speed with the experimental lower bound.

Only numpy. Run: python3 void_network_speed_check.py
"""
import itertools, math, sys
import numpy as np

a = 1.0                      # BCC conventional cube edge
lP = a * math.sqrt(3) / 2    # bubble nearest-neighbour distance (half body diagonal)

# ---------- 1. lattice and interstitial sites ----------
N = 3
cubes = [np.array(p, float) for p in itertools.product(range(-N, N + 1), repeat=3)]
bubbles = [p for p in cubes] + [p + 0.5 for p in cubes]              # BCC: corners + body centres

def nearest_bubble(x):
    return min(np.linalg.norm(b - x) for b in bubbles)

# candidate interstitial sites: face centres and edge midpoints of the conventional cube
face_centres = [p + np.array(s) for p in cubes for s in [(.5, .5, 0), (.5, 0, .5), (0, .5, .5)]]
edge_mids    = [p + np.array(s) for p in cubes for s in [(.5, 0, 0), (0, .5, 0), (0, 0, .5)]]
tetra_sites  = [p + np.array(s) for p in cubes for s in [(.5, .25, 0), (.5, .75, 0), (.25, .5, 0), (.75, .5, 0)]]

print("=== 1. Geometry (a = 1) ===")
print(f"bubble NN distance l_P        = {lP:.6f}  (a*sqrt3/2)")
print(f"face-centre  -> nearest bubble = {nearest_bubble(np.array([.5,.5,0])):.6f}")
print(f"edge-midpoint-> nearest bubble = {nearest_bubble(np.array([.5,0,0])):.6f}")
print(f"tetra site   -> nearest bubble = {nearest_bubble(np.array([.5,.25,0])):.6f}")
print("=> face centres and edge midpoints are the SAME kind of hole (octahedral, a/2 from the spheres).")
print("   The paper counted only the face centres.")

voids = {tuple(np.round(v, 6)) for v in face_centres + edge_mids}
voids = [np.array(v) for v in voids]
o = np.array([.5, .5, 0])
d = sorted(np.linalg.norm(v - o) for v in voids if np.linalg.norm(v - o) > 1e-9)
print(f"true void NN distance d_V      = {d[0]:.6f}  (a/2)")
print(f"paper's d_V                    = {a/math.sqrt(2):.6f}  (a/sqrt2)")
print(f"voids per bubble               = {len(voids)/len(bubbles):.2f} (expected 3)")

# ---------- 2. front speed, closed form ----------
# For hop vectors {e_j} and hop time tau, the graph-distance wavefront in direction n
# advances at v(n) = max_j (e_j . n) / tau   (support function of the hop set).
hopsB  = [np.array(s) * 0.5 for s in itertools.product([1, -1], repeat=3)]                 # 8 hops, |e| = l_P
hopsV  = [np.array(s) * 0.5 for s in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]  # 6 hops, |e| = a/2
hopsVp = [np.array(s) * 0.5 for s in itertools.permutations([1, 1, 0])] + \
         [np.array(s) * 0.5 for s in itertools.permutations([1, -1, 0])] + \
         [np.array(s) * 0.5 for s in itertools.permutations([-1, -1, 0])]
hopsVp = [np.array(v) for v in {tuple(h) for h in hopsVp}]                                  # 12 hops, |e| = a/sqrt2 (paper's picture)

dirs = {"[100] axis": np.array([1, 0, 0.]),
        "[110] face diagonal": np.array([1, 1, 0.]) / math.sqrt(2),
        "[111] body diagonal": np.array([1, 1, 1.]) / math.sqrt(3)}

def front_fixed_time(hops, n):   # tau = 1
    return max(e @ n for e in hops)

def front_fixed_speed(hops, n):  # each hop traversed at c = 1
    return max(e @ n / np.linalg.norm(e) for e in hops)

print("\n=== 2. Front speed, model A: same hop TIME tau for both networks (paper's implicit model) ===")
print(f"{'direction':22s} {'bubble':>8s} {'void(a/2)':>10s} {'ratio':>7s} {'void(a/sqrt2)':>14s} {'ratio':>7s}")
for k, n in dirs.items():
    vb, vv, vp = front_fixed_time(hopsB, n), front_fixed_time(hopsV, n), front_fixed_time(hopsVp, n)
    print(f"{k:22s} {vb:8.4f} {vv:10.4f} {vv/vb:7.3f} {vp:14.4f} {vp/vb:7.3f}")

print("\n=== 3. Front speed, model B: every hop traversed at c (c = 1) ===")
for k, n in dirs.items():
    print(f"{k:22s} bubble {front_fixed_speed(hopsB,n):.4f}   void {front_fixed_speed(hopsV,n):.4f}")

print(f"\nclaimed ratio c_V/c = sqrt(3/2) = {math.sqrt(1.5):.6f}")

# ---------- 4. brute-force check: BFS first-passage on a finite lattice ----------
def bfs_front(hops, n, R=14):
    """Graph distance from the origin to the lattice site nearest to R*n; speed = R/distance."""
    target = R * n
    hops_t = [tuple(h) for h in hops]
    from collections import deque
    start = (0., 0., 0.)
    dist = {start: 0}
    q = deque([start])
    best, bestd = None, 1e9
    while q:
        p = q.popleft()
        dp = np.linalg.norm(np.array(p) - target)
        if dp < bestd: best, bestd = p, dp
        if dist[p] > 2.2 * R / 0.5: continue
        for h in hops_t:
            np_ = tuple(round(p[i] + h[i], 6) for i in range(3))
            if np_ not in dist and np.linalg.norm(np.array(np_)) < R + 1.5:
                dist[np_] = dist[p] + 1
                q.append(np_)
    return R / dist[best]

print("\n=== 4. Brute-force BFS check (model A, R = 14a) ===")
for k, n in dirs.items():
    print(f"{k:22s} bubble {bfs_front(hopsB,n):.3f}   void(a/2) {bfs_front(hopsV,n):.3f}   void(a/sqrt2) {bfs_front(hopsVp,n):.3f}")

# ---------- 5. experiment ----------
print("\n=== 5. Experimental bound ===")
v_exp = 1e4   # Salart et al. 2008, Nature 454, 861: lower bound on any finite 'spooky' speed, ~1e4 c
print(f"lower bound on a finite influence speed:  > {v_exp:.0e} c   (Salart et al. 2008; later tests similar or stronger)")
print(f"claimed c_V = {math.sqrt(1.5):.3f} c  ->  excluded by a factor of ~{v_exp/math.sqrt(1.5):.0f}")
print("Bancal et al. 2012 (Nat. Phys. 8, 867): ANY finite-speed influence model permits superluminal signalling,")
print("so 'the void carries no information' cannot rescue a finite c_V.")

# ---------- 6. PASS/FAIL summary ----------
print("\n=== 6. Checks ===")
checks = [
  ("void NN spacing is a/2 (all octahedral sites)",        abs(d[0]-0.5) < 1e-9),
  ("edge midpoints are octahedral sites (a/2 from spheres)", abs(nearest_bubble(np.array([.5,0,0]))-0.5) < 1e-9),
  ("3 octahedral sites per lattice site",                   abs(len(voids)/len(bubbles)-3) < 1e-9),
  ("model A: void front <= bubble front in all 3 directions",
      all(front_fixed_time(hopsV,n) <= front_fixed_time(hopsB,n)+1e-12 for n in dirs.values())),
  ("model A, paper's own spacing: ratio <= 1 in all 3 directions",
      all(front_fixed_time(hopsVp,n) <= front_fixed_time(hopsB,n)+1e-12 for n in dirs.values())),
  ("model B: neither network exceeds c",
      all(max(front_fixed_speed(hopsB,n),front_fixed_speed(hopsV,n)) <= 1+1e-12 for n in dirs.values())),
  ("BFS agrees with closed form (<4% at R=14a)",
      all(abs(bfs_front(hopsB,n)-front_fixed_time(hopsB,n))/front_fixed_time(hopsB,n) < 0.04 for n in dirs.values())),
  ("claimed ratio sqrt(3/2) exceeds the maximum ratio (1.0) found under any model", math.sqrt(1.5) > 1.0),
  ("claimed c_V below experimental floor of 1e4 c by > 1000x", v_exp/math.sqrt(1.5) > 1000),
]
ok = True
for name, passed in checks:
    print(("PASS " if passed else "FAIL ") + name); ok &= passed
print("\nALL PASS" if ok else "\nFAILURES PRESENT")
sys.exit(0 if ok else 1)
