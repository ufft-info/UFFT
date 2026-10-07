#!/usr/bin/env python3
"""
run_face_graph_checks.py  (2026-10-08)

The complete reproduction recipe for "The face-adjacency graph of the truncated octahedron" (Draft 5), in one
command (fourth audit, R2). From the repository root:

    python3 verification/run_face_graph_checks.py

It runs, in order, propagating any nonzero exit status:
  1. verification/verify_face_graph_paper_2026-10-06.py        (ordinary spectrum harness; networkx optional)
  2. verification/verify_face_graph_flux_exact_2026-10-06.py   (exact q = 6 and q = 12; writes flux_gauge_certificate.json)
  3. verification/plot_face_graph_flux_sweep.py                (integer-lift sweep q = 0..24, moments, CSV and Figure 1)
  4. every auditors' suite reviews/2026-10-07_face_graph_*/run_all.py, each executed in a temporary copy of its
     directory in which author_evidence/flux_gauge_certificate.json (where that file exists) has been replaced by the
     certificate freshly written in step 2, so that the independent certificate checker validates the CURRENT
     certificate and not an archived one. The original review directories are not modified.

Requirements: Python 3.10+, NumPy, SymPy, matplotlib; networkx optional (automorphism enumeration). The checkers use
assertions: run with ordinary python3, never with -O.
"""
import os, shutil, subprocess, sys, tempfile
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
if sys.flags.optimize:
    print("Run without -O: the checkers use assertions."); sys.exit(2)
def run(cmd, cwd, label):
    print(f"\n==== {label}\n     {' '.join(cmd)}  (cwd {os.path.relpath(cwd, root) or '.'})", flush=True)
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode:
        print(f"FAILED: {label} (exit {r.returncode})"); sys.exit(r.returncode)
for name in ("verify_face_graph_paper_2026-10-06.py", "verify_face_graph_flux_exact_2026-10-06.py", "plot_face_graph_flux_sweep.py"):
    run([sys.executable, os.path.join(here, name)], here, name)
cert = os.path.join(here, "flux_gauge_certificate.json")
if not os.path.exists(cert):
    print("flux_gauge_certificate.json was not written"); sys.exit(1)
reviews = os.path.join(root, "reviews")
suites = sorted(d for d in os.listdir(reviews) if d.startswith("2026-10-07_face_graph_") and os.path.exists(os.path.join(reviews, d, "run_all.py"))) if os.path.isdir(reviews) else []
if not suites:
    print("no auditors' suites found under reviews/"); sys.exit(1)
for d in suites:
    src = os.path.join(reviews, d)
    with tempfile.TemporaryDirectory() as tmp:
        dst = os.path.join(tmp, d); shutil.copytree(src, dst)
        ev = os.path.join(dst, "author_evidence", "flux_gauge_certificate.json")
        if os.path.exists(ev):
            shutil.copyfile(cert, ev); note = "fresh certificate substituted"
        else: note = "no certificate checker in this suite"
        run([sys.executable, os.path.join(dst, "run_all.py")], dst, f"reviews/{d}/run_all.py ({note})")
print("\nALL FACE-GRAPH CHECKS PASSED: author scripts, figure route, and every auditors' suite against the fresh certificate.")
