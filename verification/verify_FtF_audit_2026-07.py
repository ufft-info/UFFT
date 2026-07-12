"""Reproduces every computation in FtF_Audit_2026-07-02.md, plus the
corrected claims shipped in Papers #57-#59 v2.0 (July 2026).

Audit of From_Foam_to_Fermions.md, 2026-07-02.
Requires: numpy, mpmath. Run: python verify_FtF_audit_2026-07.py
"""
import numpy as np
from math import pi, sqrt, log, acos

S17 = sqrt(17)

def build_L():
    normals = np.vstack([np.eye(3), -np.eye(3),
        np.array([[i, j, k] for i in [1, -1] for j in [1, -1]
                  for k in [1, -1]]) / np.sqrt(3)])
    A = np.array([[1 if (i < 6) != (j < 6) and
                   abs(np.dot(normals[i], normals[j]) - 1/np.sqrt(3)) < 0.01
                   else (1 if i >= 6 and j >= 6 and
                         abs(np.dot(normals[i], normals[j]) - 1/3) < 0.01
                         else 0) for j in range(14)] for i in range(14)])
    return (np.diag(A.sum(1)) - A).astype(float), A


def main():
    L, A = build_L()
    w, V = np.linalg.eigh(L)

    print("== spectrum ==")
    print(np.round(w, 4))
    expected = sorted([0, 4, 4, 9] + [7]*4 + [(9-S17)/2]*3 + [(9+S17)/2]*3)
    assert np.allclose(sorted(w), expected), "spectrum mismatch"

    print("\n== alpha and 16.2 term sizes (F3, fixed in book) ==")
    pref = 8 * pi**2.5
    t = [47/48, 10/(3*48**3), 22/(3*48**5)]
    print("alpha^-1 =", pref * sum(t))
    for k, tk in enumerate(t, 1):
        print(f"  term {k} contributes {pref*tk:.9g}")
    print("  k=3 term if kept: (2/3)/48^7 * pref =", pref*(2/3)/48**7)

    print("\n== C2 Petermann (verified) ==")
    try:
        from mpmath import mp, zeta, mpf, ln as mln, pi as mpi
        mp.dps = 20
        C2 = mpf(197)/144 + mpf(3)/4*zeta(3) - mpf(1)/2*mpi**2*mln(2) + mpi**2/12
        print("C2 =", C2, "(known -0.328478965579...)")
    except ImportError:
        print("mpmath not installed; skipped")

    print("\n== dihedral identity (verified) ==")
    s = 2*acos(-1/sqrt(3)) + acos(-1/3)
    print("sum =", s, " 2*pi =", 2*pi, " diff =", abs(s - 2*pi))

    print("\n== F1: inter-type torsion operator on the six irreps ==")
    Psq = np.diag([1.]*6 + [0.]*8)
    Phx = np.eye(14) - Psq
    T = Psq @ L @ Phx - Phx @ L @ Psq
    for target, name in [(0, "A1g(0)"), (4, "Eg"), (7, "T2g+A1g(7)"), (9, "A2u")]:
        for i in np.where(np.abs(w - target) < 1e-9)[0]:
            v = V[:, i]
            print(f"  {name:11s} |T v| = {np.linalg.norm(T@v):.2e}"
                  f"  sq content = {np.linalg.norm(Psq@v)**2:.4f}")
    print("  -> T annihilates A2u and Eg; does NOT annihilate A1g(0).")
    idx = np.where(np.abs(w**2 - 9*w + 16) < 1e-9)[0]
    B = V[:, idx]
    M = B.T @ (T @ T) @ B
    print("  T^2 on T1u eigs:", np.round(np.linalg.eigvalsh((M+M.T)/2), 6), "(-4 verified)")

    print("\n== T_hex: corrected scalar torsion operator (Papers 57-59 v2.0) ==")
    ev_hex = np.linalg.eigvalsh(A[6:, 6:] / 3.0)
    print("  T_hex eigs:", np.round(ev_hex, 4), "(expect -1, -1/3 x3, +1/3 x3, +1)")
    assert abs(ev_hex[0] + 1) < 1e-12 and abs(ev_hex[-1] - 1) < 1e-12
    for target, name, expect in [(0, "A1g(0)", "+1"), (9, "A2u", "-1")]:
        for i in np.where(np.abs(w - target) < 1e-9)[0]:
            v = V[:, i][6:]
            tau = v @ (A[6:, 6:]/3.0) @ v / (v @ v)
            print(f"  {name}: T_hex charge = {tau:+.6f} (expect {expect})")

    print("\n== corrected Thm 57.2: chirality eigenvectors 50/50 across bands ==")
    i1 = np.where(np.abs(w - (9-S17)/2) < 1e-9)[0]
    i2 = np.where(np.abs(w - (9+S17)/2) < 1e-9)[0]
    Bt = np.hstack([V[:, i1], V[:, i2]])
    Tred = Bt.T @ T @ Bt
    print(f"  band-diagonal block norms: {np.linalg.norm(Tred[:3,:3]):.1e},"
          f" {np.linalg.norm(Tred[3:,3:]):.1e} (0 = purely cross-block)")
    evv, evec = np.linalg.eig(Tred)
    frac = sorted(np.linalg.norm(evec[:3, k])**2 for k in range(6))
    print("  r1-band content of chirality eigenvectors:", np.round(frac, 4), "(expect 0.5)")

    print("\n== Result 58.3 exact identity (Paper 58 v2.0) ==")
    s1 = (1 + 1/S17)/2
    lhs = 1 - (17 - 3*S17)/20
    rhs = 2*3*S17*s1/(17+3)
    print(f"  cos^2 = {lhs:.10f}  2*C_A*sqrt(D)*s1/(D+C_A) = {rhs:.10f}  diff = {abs(lhs-rhs):.1e}")

    print("\n== F2: v1.0 overlap algebra (shown broken, removed from Paper 58) ==")
    sA = 3/7
    g2, gp2 = s1, s1*sA + (1-s1)*(1-sA)
    print("  naive algebra gives:", gp2/(g2+gp2))
    print("  formula value:      ", (17 - 3*S17)/20, " -> derivation still open")

    print("\n== F4: 44.5 insphere claim (fixed in book: radial gap) ==")
    Vcell = 32.0
    r_in = sqrt(3)
    Vsph = 4/3*pi*r_in**3
    print(f"  insphere smaller by volume: {(1-Vsph/Vcell)*100:.1f}%")
    print(f"  radial gap to square walls: {(1-sqrt(3)/2)*100:.1f}% (the correct 13.4%)")
    S = 6*2 + 8*(3*sqrt(3))
    V_A = 4/3*pi*(S/(4*pi))**1.5
    print(f"  isoperimetric deficit: {(1-Vcell/V_A)*100:.1f}%")

    print("\n== F5: hexagon subgraph cycle rank (fixed in book) ==")
    e = int(A[6:, 6:].sum())//2
    print(f"  8 nodes, {e} edges, cycle rank = {e-8+1} (six 4-cycle faces, 5 independent)")

    print("\n== sum rules (verified) ==")
    Rup, Iup = (188, 88, 146), (-40, 9, 14)
    Rdn, Idn = (56, 71, 173), (-5, 3, -7)
    print("  sum I_up  =", sum(Iup), "(-17)  sum I_down =", sum(Idn), "(-9)")
    print("  R diff    =", sum(Rup)-sum(Rdn), "(122)  R_down sum =", sum(Rdn), "(300)")

    print("\n== misc reproductions (verified) ==")
    a = 1/(pref*sum(t))
    print("  eta       =", a**3/648*(1+S17/220))
    print("  mH/mZ     =", 18/(9+S17), " measured", 125.25/91.1876)
    print("  lam_NLO   =", (120+S17)/960, " obs", 125.25**2/(2*246.22**2))
    print("  DM ratio  =", 3*(1+2*sqrt(3))/2**(4/3))
    print("  n-p (MeV) =", 0.51099895*(6+S17)/4*(1+a*S17/360))
    print("  ln(MP/v)  =", (122+45*S17)/8, " vs", log(1.22e19/246.22))


if __name__ == "__main__":
    main()
