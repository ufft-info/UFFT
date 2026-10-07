#!/usr/bin/env python3
"""
plot_face_graph_flux_sweep.py  (2026-10-08)

Figure 1 of "The face-adjacency graph of the truncated octahedron" (Draft 5), produced from first
principles so that the figure, its data and the paper have one documented route (fourth audit, R2).

Steps, each a named check:
  1. read flux_gauge_certificate.json written by verify_face_graph_flux_exact_2026-10-06.py (same directory);
  2. build the integer plaquette-edge incidence M (24 x 36) from the certificate's oriented plaquettes;
  3. solve for an INTEGER lift k of the uniform-flux gauge: M k = (1, ..., 1, -23) with k = 0 on the
     certificate's spanning tree (the compensating -23 at plaquette 0 is the Dirac string; every oriented
     plaquette then carries the holonomy exp(2 pi i q / 24) in sector q)                             [EXACT]
  4. check that k reduces modulo 4 to the certificate's q = 6 exponents up to a vertex gauge, and that
     exp(2 pi i 6 k / 24) reproduces the q = 6 holonomy i on every plaquette                           [EXACT]
  5. for q = 0..24 diagonalise Delta_q = D - A_q numerically; check the three trace moments against their
     closed forms tr = 72, tr^2 = 456, tr^3 = 3264 - 144 cos(pi q / 12) (the third from the fourth audit,
     checked here), the q -> 24 - q symmetry, and the exact q = 6 and q = 12 spectra                   [NUMERIC, 1e-9]
  6. write face_graph_magnetic_sweep.csv (q, 14 sorted eigenvalues) and draw face_graph_fig_flux_spectrum.pdf
     from that CSV: sorted eigenvalues joined level by level, visual guides only (as the caption says).

NumPy, matplotlib (Agg). Exit status nonzero on any failed check. Run without -O.
"""
import csv, json, math, os, sys
import numpy as np
FAILED = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok: FAILED.append(name)
here = os.path.dirname(os.path.abspath(__file__))
cert = json.load(open(os.path.join(here, "flux_gauge_certificate.json")))
edges = [tuple(e) for e in cert["edges"]]; plaq = cert["oriented_plaquettes"]; tree = {tuple(e) for e in cert["tree_edges"]}
F = 14; eidx = {e: i for i, e in enumerate(edges)}
check("1 certificate read: 14 faces, 36 edges, 24 oriented plaquettes, 13 tree edges", len(edges) == 36 and len(plaq) == 24 and len(tree) == 13)
M = np.zeros((24, 36), dtype=np.int64)
for p, fs in enumerate(plaq):
    for a in range(3):
        i, j = fs[a], fs[(a+1) % 3]; M[p, eidx[(min(i, j), max(i, j))]] = 1 if i < j else -1
check("2 incidence: every edge lies in exactly two plaquettes with opposite orientation (column sums zero)", (M.sum(0) == 0).all() and (np.abs(M).sum(0) == 2).all())
b = np.ones(24, dtype=np.int64); b[0] = -23
free = [k for k, e in enumerate(edges) if e not in tree]
N = M[1:, free].astype(float)                     # 23 x 23; plaquette 0 is implied by the sum rule
det = round(np.linalg.det(N))
check("3 the free-edge system is unimodular (|det| = 1), so the lift is integer", abs(det) == 1, f"det {det}")
sol = np.linalg.solve(N, b[1:].astype(float)); k = np.zeros(36, dtype=np.int64); k[free] = np.round(sol).astype(np.int64)
check("3 integer lift satisfies M k = (-23, 1, ..., 1) exactly", (M @ k == b).all() and np.allclose(sol, np.round(sol), atol=1e-9))
# 4 consistency with the certificate's q = 6 exponents (mod 4, up to vertex gauge) and holonomy
k6 = np.array(cert["phase_exponents_mod4_q6"], dtype=np.int64)
res6 = (M @ k6) % 4
check("4 certificate q = 6 exponents have residue 1 mod 4 on every plaquette", (res6 == 1).all())
A6_lift = np.zeros((F, F), complex); A6_cert = np.zeros((F, F), complex)
for (i, j), kk, k6k in zip(edges, k, k6):
    A6_lift[i, j] = np.exp(2j*np.pi*6*kk/24); A6_lift[j, i] = np.conj(A6_lift[i, j])
    A6_cert[i, j] = 1j**int(k6k); A6_cert[j, i] = np.conj(A6_cert[i, j])
hol = [np.prod([A6_lift[fs[a], fs[(a+1) % 3]] for a in range(3)]) for fs in plaq]
check("4 the lift at q = 6 gives holonomy i on all 24 oriented plaquettes (plaquette 0 included)", np.allclose(hol, 1j))
deg = np.array([4]*6 + [6]*8, float)
w_lift = np.linalg.eigvalsh(np.diag(deg) - A6_lift); w_cert = np.linalg.eigvalsh(np.diag(deg) - A6_cert)
check("4 the lift and the certificate gauge are isospectral at q = 6 (gauge-equivalent connections)", np.allclose(w_lift, w_cert, atol=1e-12))
# 5 sweep
rows = []; spectra = []; worst = 0.0
for q in range(25):
    A = np.zeros((F, F), complex)
    for (i, j), kk in zip(edges, k):
        A[i, j] = np.exp(2j*np.pi*q*kk/24); A[j, i] = np.conj(A[i, j])
    L = np.diag(deg) - A; ev = np.linalg.eigvalsh(L); spectra.append(ev); rows.append([q] + [f"{x:.12f}" for x in ev])
    mom = [ev.sum(), (ev**2).sum(), (ev**3).sum()]; exp_ = [72, 456, 3264 - 144*math.cos(math.pi*q/12)]
    worst = max(worst, max(abs(a - b_) for a, b_ in zip(mom, exp_)))
check("5 trace moments tr = 72, tr^2 = 456, tr^3 = 3264 - 144 cos(pi q/12) for q = 0..24 (max residual < 1e-9)", worst < 1e-9, f"{worst:.2e}")
check("5 symmetry q -> 24 - q (max deviation < 1e-12)", max(np.abs(spectra[q] - spectra[24-q]).max() for q in range(25)) < 1e-12)
r1, r2 = (9 - math.sqrt(17))/2, (9 + math.sqrt(17))/2
check("5 q = 6 spectrum is r1^3, 3^4, r2^3, 8^3, 9", np.allclose(spectra[6], sorted([r1]*3 + [3]*4 + [r2]*3 + [8]*3 + [9]), atol=1e-9))
s73 = math.sqrt(73)
check("5 q = 12 spectrum is (13-sqrt73)/2, 3^4, 4^2, 5^3, 8^3, (13+sqrt73)/2", np.allclose(spectra[12], sorted([(13-s73)/2] + [3]*4 + [4]*2 + [5]*3 + [8]*3 + [(13+s73)/2]), atol=1e-9))
check("5 exactly 13 distinct spectra among q = 0..12 (pairwise max difference > 1e-6)", all(np.abs(spectra[p] - spectra[q]).max() > 1e-6 for p in range(13) for q in range(p+1, 13)))
# 6 CSV and figure
csv_path = os.path.join(here, "face_graph_magnetic_sweep.csv")
with open(csv_path, "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["q"] + [f"eigenvalue_{i}" for i in range(1, 15)]); w.writerows(rows)
data = np.array([[float(x) for x in r] for r in list(csv.reader(open(csv_path)))[1:]])
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7.2, 4.2))
for lev in range(1, 15): ax.plot(data[:, 0], data[:, lev], "-", color="0.35", lw=0.9)
for lev in range(1, 15): ax.plot(data[:, 0], data[:, lev], "o", color="black", ms=2.6)
for q0 in (6, 12, 18): ax.axvline(q0, color="0.8", lw=0.7, zorder=0)
ax.set_xlim(0, 24); ax.set_xticks(range(0, 25, 2)); ax.set_xlabel(r"charge $q$ (flux $2\pi q/24$ per plaquette)"); ax.set_ylabel(r"eigenvalues of $\Delta_q$")
ax.set_title("Magnetic face Laplacian of the truncated octahedron: 14 eigenvalues against uniform flux", fontsize=9)
fig.tight_layout(); fig_path = os.path.join(here, "face_graph_fig_flux_spectrum.pdf"); fig.savefig(fig_path); plt.close(fig)
check("6 CSV written (25 rows x 14) and figure drawn from it", data.shape == (25, 15) and os.path.getsize(fig_path) > 1000, f"{os.path.basename(csv_path)}, {os.path.basename(fig_path)}")
print()
if FAILED:
    print(f"FAILED ({len(FAILED)}):"); [print("   ", f) for f in FAILED]; sys.exit(1)
print("ALL PASS  (conditional; exit status 0)")
