#!/usr/bin/env python3
"""Every numerical statement in the paper, checked. NumPy only (networkx for automorphism count)."""
import itertools, math, sys
import numpy as np

def faces_truncated_octahedron():
    V = sorted({tuple(a*b for a, b in zip(p, s)) for p in itertools.permutations([0, 1, 2])
                for s in itertools.product([1, -1], repeat=3)})
    F = []
    for ax in range(3):
        for s in (2, -2):
            F.append([i for i, v in enumerate(V) if v[ax] == s])
    for sg in itertools.product([1, -1], repeat=3):
        F.append([i for i, v in enumerate(V) if sum(a*b for a, b in zip(v, sg)) == 3])
    return V, F

def face_graph(V, F):
    n = len(F); A = np.zeros((n, n), int)
    for i in range(n):
        for j in range(i+1, n):
            if len(set(F[i]) & set(F[j])) == 2: A[i, j] = A[j, i] = 1
    return A

def charpoly_int(M):
    n = M.shape[0]; M = M.astype(object); I = np.identity(n, dtype=object)
    c = 1; Mk = np.zeros((n, n), dtype=object); coeffs = [1]
    for k in range(1, n+1):
        Mk = M @ (Mk + c*I); c = -sum(Mk[i, i] for i in range(n)) // k; coeffs.append(c)
    return coeffs

def pmul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out
def ppow(a, n):
    r = [1]
    for _ in range(n): r = pmul(r, a)
    return r
def prod(factors):
    r = [1]
    for f, p in factors: r = pmul(r, ppow(f, p))
    return r

V, F = faces_truncated_octahedron()
A = face_graph(V, F); n = 14
deg = A.sum(1); L = np.diag(deg) - A
sq = list(range(6)); hx = list(range(6, 14))
print("vertices 24, faces", len(F), "edges", A.sum()//2, "degrees", sorted(deg))
print("sq-hex adjacencies", A[np.ix_(sq, hx)].sum(), "hex-hex", A[np.ix_(hx, hx)].sum()//2, "sq-sq", A[np.ix_(sq, sq)].sum()//2)
# triangles and 4-cycles
A2 = A @ A; A3 = A2 @ A
tri = np.trace(A3)//6
# simple 4-cycles: (tr A^4 - 2m - 4 sum C(d,2)... ) standard formula: #C4 = (tr A^4 - sum_i d_i^2*2 + sum_i d_i)/8  -> use: tr(A^4) = 8*C4 + 2*sum d_i^2 - sum d_i
c4 = (np.trace(A3 @ A) - 2*sum(deg**2) + sum(deg))//8
print("triangles", tri, "4-cycles", c4)
print("adjacency charpoly == tabulated:", charpoly_int(A) == prod([([1,0],2),([1,1],3),([1,3],1),([1,-3,-12],1),([1,-1,-4],3)]))
print("Laplacian charpoly == x(x-9)(x-7)^4(x-4)^2(x^2-9x+16)^3:", charpoly_int(L) == prod([([1,0],1),([1,-9],1),([1,-7],4),([1,-4],2),([1,-9,16],3)]))
# signless Laplacian and normalised Laplacian for completeness
Q = np.diag(deg) + A
print("signless Laplacian charpoly:", charpoly_int(Q))
w, U = np.linalg.eigh(L.astype(float))
r1, r2 = (9-17**.5)/2, (9+17**.5)/2
def eigspace(val):
    idx = [k for k in range(n) if abs(w[k]-val) < 1e-9]; return U[:, idx]
for val in (0, r1, 4, r2, 7, 9):
    E = eigspace(val); P = E @ E.T; fr = np.trace(P[:6, :6])/E.shape[1]
    print(f"lambda={val:.4f} dim={E.shape[1]} square trace-fraction={fr:.6f}")
print("T1u square fractions closed form (1 +- 1/sqrt17)/2 =", (1+17**-.5)/2, (1-17**-.5)/2)
# orbit-uniform vector at eigenvalue 7: a on squares, b=-3a/4 on hexagons
v = np.array([1.0]*6 + [-0.75]*8); print("L v = 7 v for (1,...,1,-3/4,...):", np.allclose(L@v, 7*v), " square content", 6/(6+8*9/16))
# torsion operator T = P_sq L P_hex - P_hex L P_sq
Psq = np.diag([1]*6+[0]*8).astype(float); Phx = np.eye(14)-Psq
T = Psq@L@Phx - Phx@L@Psq
print("T antisymmetric:", np.allclose(T, -T.T))
E1, E2 = eigspace(r1), eigspace(r2); B = np.hstack([E1, E2])
T6 = B.T @ T @ B
print("T^2 on T1u ⊕ T1u = -4 I:", np.allclose(T6@T6, -4*np.eye(6)))
T21 = E2.T @ T @ E1; s = np.linalg.svd(T21, compute_uv=False); print("singular values of T21:", np.round(s, 6))
for name, val in (("A1g(0)", 0), ("Eg", 4), ("A2u", 9)):
    E = eigspace(val); print(f"T annihilates {name}:", np.allclose(T@E, 0))
E7 = eigspace(7); print("T on lambda=7 space, norm:", np.linalg.norm(T@E7).round(6))
E0 = eigspace(0); print("T on A1g(0), norm:", np.linalg.norm(T@E0).round(6), " T E0 lies in lambda=7 space:", np.allclose(E7@E7.T@(T@E0), T@E0))
# where does T send the T1u(r1) space? check T E1 lies in E2 span
proj = E2 @ E2.T; print("T E1 subset of E2:", np.allclose(proj @ (T@E1), T@E1), " T E2 subset of E1:", np.allclose(E1@E1.T@(T@E2), T@E2))
# automorphism group order
try:
    import networkx as nx
    G = nx.from_numpy_array(A)
    cnt = sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
    print("automorphism group order:", cnt)
except ImportError:
    print("networkx missing; automorphism count skipped")

# ---- the other Fedorov parallelohedra -------------------------------------------------
def spectrum_report(name, A):
    d = A.sum(1); Lc = np.diag(d) - A
    cp = charpoly_int(Lc); ev = np.round(np.linalg.eigvalsh(Lc.astype(float)), 6)
    print(f"{name}: faces {A.shape[0]}, edges {A.sum()//2}, L spectrum {sorted(ev.tolist())}")
    return cp
# cube: face graph = octahedron K_{2,2,2}
Ac = np.ones((6,6),int) - np.eye(6,dtype=int)
for i in range(3): Ac[2*i,2*i+1] = Ac[2*i+1,2*i] = 0
spectrum_report("cube", Ac)
# hexagonal prism: 2 hexagons + 6 squares in a cycle
Ah = np.zeros((8,8),int)
for i in range(6):
    j=(i+1)%6; Ah[i,j]=Ah[j,i]=1; Ah[i,6]=Ah[6,i]=1; Ah[i,7]=Ah[7,i]=1
spectrum_report("hexagonal prism", Ah)
# rhombic dodecahedron: faces <-> edges of the cube (12 rhombi), adjacent iff cube edges share a vertex: line graph of the cube = cuboctahedron graph
import itertools as it
cube_v = list(it.product([0,1],repeat=3)); cube_e = [(a,b) for a in cube_v for b in cube_v if a<b and sum(x!=y for x,y in zip(a,b))==1]
Ar = np.zeros((12,12),int)
for i,e in enumerate(cube_e):
    for j,f in enumerate(cube_e):
        if i<j and len(set(e)&set(f))==1: Ar[i,j]=Ar[j,i]=1
spectrum_report("rhombic dodecahedron", Ar)
# elongated dodecahedron: 8 rhombi + 4 hexagons. Build from the rhombic dodecahedron by inserting a belt:
# faces: 4 hexagons in a belt (cycle), each hexagon adjacent to 2 hexagons + 2 top rhombi + 2 bottom rhombi;
# top rhombi form a 4-cycle (cap) each adjacent to 2 cap neighbours and 2 hexagons; same for bottom.
Ae = np.zeros((12,12),int)
H = list(range(4)); Tp = list(range(4,8)); Bt = list(range(8,12))
for i in range(4):
    j=(i+1)%4
    Ae[H[i],H[j]]=Ae[H[j],H[i]]=1          # hex belt
    Ae[Tp[i],Tp[j]]=Ae[Tp[j],Tp[i]]=1      # top cap 4-cycle
    Ae[Bt[i],Bt[j]]=Ae[Bt[j],Bt[i]]=1      # bottom cap 4-cycle
    # each hexagon touches two top rhombi and two bottom rhombi (staggered)
    for k in (i, j):
        Ae[H[i],Tp[k]]=Ae[Tp[k],H[i]]=1; Ae[H[i],Bt[k]]=Ae[Bt[k],H[i]]=1
cp_e = spectrum_report("elongated dodecahedron", Ae)
print("elongated dodecahedron L charpoly coefficients:", cp_e)
print("truncated octahedron L charpoly coefficients:", charpoly_int(L))
print("done")
