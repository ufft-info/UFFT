#!/usr/bin/env python3
"""
verify_face_graph_flux_exact_2026-10-06.py  (revision 2, 2026-10-07)

Exact spectra of the magnetic face Laplacian of the truncated octahedron at flux pi/2 (q=6)
and pi (q=12) per vertex-plaquette. Design: numerical candidate generation for the gauge
(least squares on the tree-gauge equations), then an EXACT certificate: integer phase
exponents, integer holonomy residues, and a sympy characteristic polynomial over Z[i].

Revision 2 answers the referee's software audit of 2026-10-07: integer incidence matrix,
integer modular holonomy check (no floating rounding in the certificate step), documented
certificate keys (the 14 magnetic-matrix vertices are the FACES of the polyhedron; the 24
polyhedron vertices are the plaquettes), source/version fields, conditional PASS, nonzero
exit on failure. Imports the ordinary script from the same directory.
"""
import itertools, math, sys, os, json, collections, io, contextlib
import numpy as np, sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import importlib.util
    _here = os.path.dirname(os.path.abspath(__file__))
    _spec = importlib.util.spec_from_file_location("vf", os.path.join(_here, "verify_face_graph_paper_2026-10-06.py"))
    _vf = importlib.util.module_from_spec(_spec)
    try:
        _spec.loader.exec_module(_vf)
    except SystemExit as e:                       # the ordinary harness exits 1 if any of ITS checks fail
        if e.code: print("ordinary verification script FAILED; aborting"); sys.exit(1)
faces_truncated_octahedron, face_graph = _vf.faces_truncated_octahedron, _vf.face_graph

FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)

V, F = faces_truncated_octahedron(); A = face_graph(F); n = 14
Vn = np.array(V, float); cent = [Vn[f].mean(0) for f in F]
# plaquettes = polyhedron vertices; the three faces at a vertex, ordered counterclockwise seen from outside
plaq = []
for v in range(24):
    fs = [i for i in range(n) if v in F[i]]; nrm = Vn[v]/np.linalg.norm(Vn[v])
    a = np.array([1, 0, 0.]) if abs(nrm[0]) < 0.9 else np.array([0, 1, 0.])
    u = np.cross(nrm, a); u /= np.linalg.norm(u); w = np.cross(nrm, u)
    fs.sort(key=lambda i: math.atan2(np.dot(cent[i]-Vn[v], w), np.dot(cent[i]-Vn[v], u))); plaq.append(fs)
check("every polyhedron vertex lies on exactly three faces (triangular plaquettes)", all(len(p) == 3 for p in plaq))
edges = sorted({(i, j) for i in range(n) for j in range(i+1, n) if A[i][j]}); eidx = {e: k for k, e in enumerate(edges)}
check("36 edges", len(edges) == 36)
# INTEGER incidence matrix plaquette x edge, orientation +1 if traversed i->j with i<j
M = [[0]*36 for _ in range(24)]
for p, fs in enumerate(plaq):
    for a in range(3):
        i, j = fs[a], fs[(a+1) % 3]; M[p][eidx[(min(i, j), max(i, j))]] = 1 if i < j else -1
Mnp = np.array(M, float)
# spanning tree (BFS from face 0); tree edges carry exponent 0
tree = set(); seen = {0}; q = collections.deque([0])
while q:
    x0 = q.popleft()
    for y in range(n):
        if A[x0][y] and y not in seen: seen.add(y); tree.add((min(x0, y), max(x0, y))); q.append(y)
free = [k for k, e in enumerate(edges) if e not in tree]
check("spanning tree has 13 edges, 23 free edges", len(tree) == 13 and len(free) == 23)

def gauge(modulus):
    """CANDIDATE GENERATION (numerical): solve M k = b for exponents on the free edges, where every
    plaquette carries one unit (2pi/modulus) of flux, with a Dirac string at plaquette 0 so the total
    flux on the closed surface is zero. Returns integer exponents mod modulus."""
    b = np.ones(24); b[0] -= 24
    k, *_ = np.linalg.lstsq(Mnp[:, free], b, rcond=None)
    assert np.allclose(Mnp[:, free] @ k, b, atol=1e-9), "gauge equations inconsistent"
    kf = np.round(k); assert np.allclose(k, kf, atol=1e-8), "non-integer gauge solution"
    kk = [0]*36
    for idx, val in zip(free, kf): kk[idx] = int(val) % modulus
    return kk
def holonomy_residues(kk, modulus):
    """EXACT: integer flux per plaquette mod modulus."""
    return [sum(M[p][e]*kk[e] for e in range(36)) % modulus for p in range(24)]

x = sp.symbols('x')
def exact_charpoly(kk, unit):
    H = sp.zeros(n, n)
    for (i, j), k in zip(edges, kk):
        H[i, j] = unit**int(k); H[j, i] = sp.conjugate(unit**int(k))
    Lm = sp.diag(*[sum(A[i]) for i in range(n)]) - H
    return sp.expand(Lm.charpoly(x).as_expr())

print("== magnetic certificate ==")
k2, k4 = gauge(2), gauge(4)
check("holonomy, flux pi   (q=12): every plaquette residue = 1 mod 2  [integer check]", all(r == 1 for r in holonomy_residues(k2, 2)))
check("holonomy, flux pi/2 (q=6):  every plaquette residue = 1 mod 4  [integer check]", all(r == 1 for r in holonomy_residues(k4, 4)))
c12 = exact_charpoly(k2, sp.Integer(-1)); c6 = exact_charpoly(k4, sp.I); c0 = exact_charpoly([0]*36, sp.Integer(1))
exp12 = sp.expand((x-8)**3*(x-5)**3*(x-4)**2*(x-3)**4*(x**2-13*x+24))
exp6 = sp.expand((x-9)*(x-8)**3*(x-3)**4*(x**2-9*x+16)**3)
exp0 = sp.expand(x*(x-9)*(x-7)**4*(x-4)**2*(x**2-9*x+16)**3)
check("q=12 charpoly = (x-8)^3 (x-5)^3 (x-4)^2 (x-3)^4 (x^2-13x+24)  [exact, sympy over Z]", sp.expand(c12-exp12) == 0)
check("q=6  charpoly = (x-9) (x-8)^3 (x-3)^4 (x^2-9x+16)^3           [exact, sympy over Z[i]]", sp.expand(c6-exp6) == 0)
check("q=0  charpoly = x (x-9) (x-7)^4 (x-4)^2 (x^2-9x+16)^3        [exact]", sp.expand(c0-exp0) == 0)
check("q=6 characteristic polynomial has integer coefficients (Hermitian over Z[i])", all(c.is_integer for c in sp.Poly(c6, x).all_coeffs()))

certificate = {
    "source": "verify_face_graph_flux_exact_2026-10-06.py revision 2 (2026-10-07), github.com/ufft-info/UFFT verification/",
    "conventions": {
        "magnetic_matrix_vertices": "the 14 FACES of the truncated octahedron, indexed as in 'faces' (0-5 squares, 6-13 hexagons)",
        "plaquettes": "the 24 POLYHEDRON vertices; each is a triangle of the face graph (three faces meet at a vertex)",
        "plaquette_orientation": "faces listed counterclockwise as seen from outside the polyhedron",
        "edge_orientation": "edge (i,j) with i<j carries phase unit^k from i to j and its conjugate from j to i",
        "gauge": "spanning tree from face 0 carries exponent 0; Dirac string at plaquette 0 (total flux zero on the sphere)",
        "unit": "q=6: unit = i (flux pi/2 per plaquette); q=12: unit = -1 (flux pi per plaquette)",
    },
    "polyhedron_vertices": [list(map(int, v)) for v in V],
    "vertex_order": [list(map(int, v)) for v in V],   # legacy alias of polyhedron_vertices, kept so earlier external checkers still run
    "faces": [[int(i) for i in sorted(f)] for f in F],
    "face_labels": ["sq+x", "sq-x", "sq+y", "sq-y", "sq+z", "sq-z"] + ["hx" + "".join("+" if s > 0 else "-" for s in sg) for sg in itertools.product([1, -1], repeat=3)],
    "edges": [list(e) for e in edges],
    "oriented_plaquettes": plaq,
    "tree_edges": sorted(list(e) for e in tree),
    "phase_exponents_mod4_q6": k4,
    "phase_exponents_mod2_q12": k2,
    "charpoly_q6": str(c6), "charpoly_q12": str(c12),
}
cert_path = os.path.join(_here, "flux_gauge_certificate.json")
with open(cert_path, "w") as fh: json.dump(certificate, fh, indent=1)
print("certificate written:", cert_path)
print()
if FAILED:
    print(f"FAILED ({len(FAILED)}):"); [print("   ", f) for f in FAILED]; sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
