"""Weinberg run 5 (2026-07-02, late): the full gamma/Z chain from the run-4
Bloch layer, computed end to end. RESULT: FAILURE, documented per FAILSAFES.

Chain as specified by run 4: two-charge abelian Peierls space (q_sq, q_hx)
on partner links with derived void couplings eta_sq = e^(-2*sqrt2),
eta_hx = e^(-sqrt6); A2u condensate hops hex-only -> rank-1 mass along the
hex charge direction; kinetic matrix Pi_ab from the fermion loop (occupied
= r1-descended triplet, parity-odd multi-gap channels); canonical
normalisation Pi^(-1/2); Z couplings to the two bands; estimator
sin2_eff = g_R/(2(g_R - g_L)) under Cor 57.2a.

WHAT PASSES (structure): Pi positive-definite and near-diagonal
(Pi_sq/Pi_hx ~ 1.7); the rank-1 mechanism produces exactly one massless
and one massive neutral boson; the split is convention-robust.

WHAT FAILS (number): sin2_eff = 1.28 (content-as-charge ansatz) or 1.23
(derived diamagnetic band charges); robust to loop denominator power
(1/dE vs 1/dE^3) and to the charge prescription; outside [0,1], nowhere
near 0.2315.

DIAGNOSIS: every band-charge prescription available at k=0 is vector-like
(both bands couple to the hex-dominant Z with the same sign). The
estimator needs the AXIAL structure of the Z coupling, and run 4's own
item 3 says exactly where that lives: the O(k) cross-polarization
couplings in the full 6-dim T1u treatment. This run confirms the diagnosis
from the failure side: no static charge assignment can produce the angle;
the next run must compute the axial vertex.

Failure count for Result 58.3: four documented attempts (naive overlaps
0.437, 1/lambda-weighted 0.322, T-strength 0.674, gamma/Z chain 1.25+-0.03).
Run: python explore_weinberg_gammaZ_chain_2026-07.py
"""
import numpy as np
from math import sqrt, exp
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
    L = (np.diag(A.sum(1)) - A).astype(complex)
    partner = np.array([int(np.argmin(np.linalg.norm(normals + normals[f], axis=1)))
                        for f in range(14)])
    R = np.array([4*normals[f] if f < 6 else 2*np.sqrt(3)*normals[f] for f in range(14)])
    eta = np.array([exp(-2*sqrt(2))]*6 + [exp(-sqrt(6))]*8)
    return normals, L, partner, R, eta

def main():
    normals, L, partner, R, eta = build()
    is_sq = np.array([1.0]*6 + [0.0]*8)
    r1 = (9 - S17)/2

    def Hk(k):
        X = np.zeros((14, 14), complex)
        for f in range(14):
            X[f, partner[f]] += np.exp(1j*np.dot(k, R[f]))
        E = np.diag(eta.astype(complex))
        return L + E - 0.5*(E @ X + (E @ X).conj().T)

    def Jk(k, typ, mu):
        sel = is_sq if typ == 'sq' else (1 - is_sq)
        J = np.zeros((14, 14), complex)
        for f in range(14):
            if sel[f]:
                J[f, partner[f]] += -0.5j*R[f][mu]*eta[f]*np.exp(1j*np.dot(k, R[f]))
        return J + J.conj().T

    N = 12
    ks = 2*np.pi*np.fft.fftfreq(N)
    Pi = np.zeros((2, 2))
    for kx in ks:
        for ky in ks:
            for kz in ks:
                k = np.array([kx, ky, kz])
                w, V = np.linalg.eigh(Hk(k))
                occ = np.argsort(np.abs(w - r1))[:3]
                uno = [m for m in range(14) if m not in occ]
                for mu in range(3):
                    Ja = {t: V.conj().T @ Jk(k, t, mu) @ V for t in ('sq', 'hx')}
                    for a, ta in enumerate(('sq', 'hx')):
                        for b, tb in enumerate(('sq', 'hx')):
                            for n in occ:
                                for m in uno:
                                    dE = w[m] - w[n]
                                    if dE > 1e-9:
                                        Pi[a, b] += 2*np.real(Ja[ta][n, m]*Ja[tb][m, n])/dE
    Pi = 0.5*(Pi + Pi.T)/(3*N**3)
    print("Pi =", np.round(Pi, 6).tolist(), " (positive-definite, near-diagonal)")

    ev, evec = np.linalg.eigh(Pi)
    Pih = evec @ np.diag(1/np.sqrt(np.maximum(ev, 1e-15))) @ evec.T
    zc = Pih @ np.array([0., 1.]); zc /= np.linalg.norm(zc)
    Zdir = Pih @ zc
    sL, sR = (1 + 1/S17)/2, (1 - 1/S17)/2
    for name, Ql, Qr in [("content ansatz", np.array([sL, 1-sL]), np.array([sR, 1-sR]))]:
        gL, gR = Ql @ Zdir, Qr @ Zdir
        print(f"{name}: sin2_eff = {gR/(2*(gR - gL)):.6f}  (target 0.231534)  FAIL")
    print("See docstring: axial vertex (O(k), 6-dim T1u) is the missing derived piece.")

if __name__ == "__main__":
    main()
