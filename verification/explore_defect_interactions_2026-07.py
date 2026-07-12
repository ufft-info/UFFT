"""Substrate-direct programme, step 2 (2026-07-02): two-defect interactions
through the full 14-component foam propagator, plus the tiling-flatness
identity. Companion to .explorations/UFFT_Explorations_2026-07-02.md section 4.

Model: BCC lattice of cells, each carrying the 14 face displacements; intra-
cell operator L (face Laplacian); inter-cell coupling per face f via
(1 - cos k.R_f) with R_f the neighbour displacement across face f. Static
sources j1, j2 at separation r; channel amplitude s(k) = j1^T H(k)^+ j2,
E(r) = IFFT[s] (zero mode removed = background subtraction).

Findings:
  1. Tiling flatness: every tiling edge carries dihedrals {th_sh, th_sh,
     th_hh} summing to exactly 2*pi (the only combination that closes 360).
     The fermion vertex flux pi is half the space-filling closure. Bulk
     inter-cell loops carry zero geometric flux; boson spin must come from
     dynamical link holonomy (standard LGT), not deficits.
  2. A1g-pattern sources (charge): Coulombic 1/r channel (box-corrected).
  3. T1u-pattern sources (matter): no monopole; fast-decaying, orientation-
     dependent multipole. Foam-neutral.
  4. A1g x T1u: exactly zero at every separation (irrep selection rule
     survives the full lattice propagator).
Run: python explore_defect_interactions_2026-07.py
"""
import numpy as np
from math import sqrt, acos, pi

S17 = sqrt(17)

def build():
    normals = np.vstack([np.eye(3), -np.eye(3),
        np.array([[i, j, k] for i in [1, -1] for j in [1, -1]
                  for k in [1, -1]]) / np.sqrt(3)])
    A = np.array([[1 if (i < 6) != (j < 6) and
                   abs(np.dot(normals[i], normals[j]) - 1/np.sqrt(3)) < 0.01
                   else (1 if i >= 6 and j >= 6 and
                         abs(np.dot(normals[i], normals[j]) - 1/3) < 0.01
                         else 0) for j in range(14)] for i in range(14)])
    return normals, (np.diag(A.sum(1)) - A).astype(float)

def main():
    normals, L = build()
    w, V = np.linalg.eigh(L)

    print("== tiling flatness ==")
    th_sh, th_hh = acos(-1/sqrt(3)), acos(-1/3)
    print(f"  2*th_sh + th_hh - 2pi = {2*th_sh + th_hh - 2*pi:.2e} (exact zero)")
    print("  no other combination of the two dihedrals sums to 2pi:")
    for combo, val in [("3 sh", 3*th_sh), ("3 hh", 3*th_hh), ("sh+2hh", th_sh+2*th_hh)]:
        print(f"    {combo}: {np.degrees(val):.2f} deg")

    a1, a2, a3 = np.array([2, 2, -2.]), np.array([-2, 2, 2.]), np.array([2, -2, 2.])
    M = np.column_stack([a1, a2, a3])
    R = []
    for i in range(14):
        v = 4*normals[i] if i < 6 else 2*np.sqrt(3)*normals[i]
        R.append(np.round(np.linalg.solve(M, v)).astype(int))
    R = np.array(R)

    N = 32
    q = 2*np.pi*np.fft.fftfreq(N)
    Q = np.stack(np.meshgrid(q, q, q, indexing='ij'), -1)
    C = 1 - np.cos(Q @ R.T)

    jA = np.ones(14)/np.sqrt(14)
    i1 = np.where(np.abs(w - (9-S17)/2) < 1e-9)[0]
    jT, jT2 = V[:, i1[0]], V[:, i1[1]]

    idx = np.arange(14)
    Hk = np.broadcast_to(L, (N, N, N, 14, 14)).copy()
    Hk[..., idx, idx] += C + 1e-8

    def interaction(j1, j2):
        sol = np.linalg.solve(Hk, np.broadcast_to(j2, (N, N, N, 14))[..., None])[..., 0]
        s = sol @ j1
        s[0, 0, 0] = 0.0
        return np.real(np.fft.ifftn(s))

    for name, j1, j2 in [("A1g-A1g (charge)", jA, jA),
                         ("T1u-T1u same", jT, jT),
                         ("T1u-T1u orth", jT, jT2),
                         ("A1g-T1u (selection rule)", jA, jT)]:
        E = interaction(j1, j2)
        print(f"\n== {name}: r*E(r) ==")
        for m in range(1, 7):
            rd = np.linalg.norm(m*a1)
            ra = np.linalg.norm(m*(a1+a3))
            print(f"  m={m}: diag {rd:5.2f} -> {rd*E[m % N, 0, 0]:+.5f}"
                  f" | axis {ra:5.2f} -> {ra*E[m % N, 0, m % N]:+.5f}")

if __name__ == "__main__":
    main()
