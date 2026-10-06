#!/usr/bin/env python3
"""Exact spectra of the magnetic face Laplacian at flux pi/2 and pi per vertex-plaquette.
Builds a tree gauge with edge phases in {1,i,-1,-i} (resp. {+1,-1}) and computes the
characteristic polynomial exactly with sympy over Gaussian integers."""
import itertools, math, sys, numpy as np, sympy as sp
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import importlib.util, os
    _spec = importlib.util.spec_from_file_location("vf", os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify_face_graph_paper_2026-10-06.py"))
    _vf = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_vf)
    faces_truncated_octahedron, face_graph = _vf.faces_truncated_octahedron, _vf.face_graph
    # (was: from verify_face_graph_paper import faces_truncated_octahedron, face_graph
V, F = faces_truncated_octahedron(); A = face_graph(V, F); n = 14
Vn = np.array(V, float); cent = [Vn[f].mean(0) for f in F]
# plaquettes: vertices of the cell; faces around a vertex, ordered counterclockwise seen from outside
plaq = []
for v in range(24):
    fs = [i for i in range(n) if v in F[i]]; nrm = Vn[v]/np.linalg.norm(Vn[v])
    a = np.array([1,0,0.]) if abs(nrm[0]) < 0.9 else np.array([0,1,0.])
    u = np.cross(nrm, a); u /= np.linalg.norm(u); w = np.cross(nrm, u)
    fs.sort(key=lambda i: math.atan2(np.dot(cent[i]-Vn[v], w), np.dot(cent[i]-Vn[v], u))); plaq.append(fs)
edges = sorted({tuple(sorted((i, j))) for i in range(n) for j in range(n) if A[i, j]}); eidx = {e: k for k, e in enumerate(edges)}
M = np.zeros((24, 36))
for p, fs in enumerate(plaq):
    for a in range(3):
        i, j = fs[a], fs[(a+1) % 3]; M[p, eidx[tuple(sorted((i, j)))]] = 1 if i < j else -1
# spanning tree (BFS)
import collections
tree = set(); seen = {0}; q = collections.deque([0])
while q:
    x = q.popleft()
    for y in range(n):
        if A[x, y] and y not in seen: seen.add(y); tree.add(tuple(sorted((x, y)))); q.append(y)
free = [k for k, e in enumerate(edges) if e not in tree]
def gauge(units_per_plaq, modulus):
    """solve M k = units_per_plaq on the free edges (tree edges = 0); return integer k mod modulus"""
    b = np.full(24, float(units_per_plaq)); b[0] -= 24*units_per_plaq   # Dirac string: total flux 0, each plaquette still ≡ 1 unit mod the modulus
    Mf = M[:, free]
    k, res, rank, _ = np.linalg.lstsq(Mf, b, rcond=None)
    assert np.allclose(Mf @ k, b), "inconsistent"
    kf = np.round(k); assert np.allclose(k, kf, atol=1e-8), "non-integer gauge"
    kk = np.zeros(36, int); kk[free] = kf.astype(int) % modulus
    assert np.all((M @ kk - b) % modulus == 0)
    return kk
x = sp.symbols('x')
import json
def holonomy_check(kk, modulus):
    """every oriented triangle must carry exactly 1 unit of flux mod modulus (1 unit = 2pi/modulus)"""
    flux = M @ kk
    return all(int(round(v)) % modulus == 1 for v in flux)
certificate = {"vertex_order": [list(map(int, v)) for v in V], "faces": [[int(i) for i in sorted(f)] for f in F],
               "edges": [list(e) for e in edges], "oriented_plaquettes": plaq, "tree_edges": sorted(list(e) for e in tree)}
def exact_charpoly(kk, unit):
    H = sp.zeros(n, n)
    for (i, j), k in zip(edges, kk):
        H[i, j] = unit**int(k); H[j, i] = sp.conjugate(unit**int(k))
    Lm = sp.diag(*[int(d) for d in A.sum(1)]) - H
    return sp.factor(sp.expand(Lm.charpoly(x).as_expr()))
fails = 0
k2 = gauge(1, 2); k4 = gauge(1, 4)
print("holonomy check, flux pi  (every triangle = -1):", holonomy_check(k2, 2))
print("holonomy check, flux pi/2 (every triangle =  i):", holonomy_check(k4, 4))
fails += (not holonomy_check(k2, 2)) + (not holonomy_check(k4, 4))
c12 = exact_charpoly(k2, sp.Integer(-1)); c6 = exact_charpoly(k4, sp.I); c0 = exact_charpoly(np.zeros(36, int), sp.Integer(1))
print("flux pi per plaquette (signs +-1):", c12)
print("flux pi/2 per plaquette (phases i^k):", c6)
print("flux 0:", c0)
exp12 = sp.factor((x-8)**3*(x-5)**3*(x-4)**2*(x-3)**4*(x**2-13*x+24))
exp6 = sp.factor((x-9)*(x-8)**3*(x-3)**4*(x**2-9*x+16)**3)
exp0 = sp.factor(x*(x-9)*(x-7)**4*(x-4)**2*(x**2-9*x+16)**3)
for name, got, want in (("q=12", c12, exp12), ("q=6", c6, exp6), ("q=0", c0, exp0)):
    ok = sp.expand(got - want) == 0; print(("PASS " if ok else "FAIL ") + name + " characteristic polynomial"); fails += (not ok)
certificate["phase_exponents_mod4_q6"] = [int(v) for v in k4]
certificate["phase_exponents_mod2_q12"] = [int(v) for v in k2]
certificate["charpoly_q6"] = str(sp.expand(c6)); certificate["charpoly_q12"] = str(sp.expand(c12))
cert_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flux_gauge_certificate.json")
with open(cert_path, "w") as fh: json.dump(certificate, fh, indent=1)
print("certificate written:", cert_path)
print("ALL PASS" if fails == 0 else f"{fails} FAIL"); sys.exit(1 if fails else 0)
