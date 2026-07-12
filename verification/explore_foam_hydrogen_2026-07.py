"""Substrate-direct programme, step 3 first pass (2026-07-02): bound states
of a light A1g-charged defect in the foam Coulomb well of a heavy one.

CORRECTION (same day, evening run): the "1s deepened ~2x / alkali-style
quantum defect" finding below is WITHDRAWN. It came from comparing a
min-subtracted periodized foam potential against a non-periodized Coulomb
control. With both potentials periodized identically (image-free k-space
comparator) the deviation is negative, percent-level, and scales as
-K/a_B^2. The 1/r fingerprint (near-degenerate 2s/2p) and the solver
validation stand. See verify_foam_hydrogen_deviation_2026-07.py and
.explorations/UFFT_Explorations_2026-07-02.md Section 6.

Method: discrete Schrodinger problem on the BCC cell lattice. Kinetic
operator = the A1g channel's own hopping structure (8 hex + 6 sq
neighbours). Potential = -lam * G(r), with G the image-corrected lattice
Green's function of the A1g channel (self-energy at r=0 replaced by a hard
core -- two defects never share a cell). Sparse Lanczos for the lowest
levels. Control: identical solver with ideal -lc/r.

Findings (N=48 solver box, G from N=96):
  CONTROL (ideal 1/r): E1 = -0.310 vs Rydberg prediction -0.330 (6%);
    E1/<E2> = 3.85 (Coulomb: 4.0); near-degenerate 2s/2p multiplet.
    Method validated.
  FOAM potential (tail-matched): excited multiplet hydrogen-like
    (2s -0.0570, 2p -0.0513 x3: near-degenerate = the 1/r fingerprint);
    1s deepened ~2x relative to pure Coulomb by the foam's near-zone
    enhancement -- an alkali-style quantum defect concentrated on
    low-n s states. This is a foam-specific, in-principle-testable
    deviation signature.
  OPEN: absolute Rydberg check requires the unit map (coupling
    normalisation between lam and 4*pi*alpha, defect inertia vs m_e) and
    larger boxes / weak-coupling extrapolation for the 1s.
Run: python explore_foam_hydrogen_2026-07.py   (requires scipy)
"""
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh

hexn = [(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
sqn  = [(1,1,0),(0,1,1),(1,0,1)]
a1, a2, a3 = np.array([2,2,-2.]), np.array([-2,2,2.]), np.array([2,-2,2.])

def greens(Nb):
    q = 2*np.pi*np.fft.fftfreq(Nb)
    Q1,Q2,Q3 = np.meshgrid(q,q,q,indexing='ij')
    Ek = np.zeros((Nb,Nb,Nb))
    for m in hexn: Ek += 2*(1-np.cos(m[0]*Q1+m[1]*Q2+m[2]*Q3))
    for m in sqn:  Ek += 2*(1-np.cos(m[0]*Q1+m[1]*Q2+m[2]*Q3))
    Ek[0,0,0]=1; Gk = 1/Ek; Gk[0,0,0]=0
    return np.real(np.fft.ifftn(Gk))

def solve(N, Vgrid, k=14):
    ii, jj, kk = np.meshgrid(np.arange(N),np.arange(N),np.arange(N),indexing='ij')
    site = (ii*N*N + jj*N + kk).ravel()
    rows, cols, dat = [site], [site], [np.full(N**3, 14.0)]
    for d in [np.array(m) for m in hexn]+[-np.array(m) for m in hexn] \
           + [np.array(m) for m in sqn]+[-np.array(m) for m in sqn]:
        nb = (((ii+d[0])%N)*N*N + ((jj+d[1])%N)*N + ((kk+d[2])%N)).ravel()
        rows.append(site); cols.append(nb); dat.append(np.full(N**3, -1.0))
    H = csr_matrix(coo_matrix(
        (np.concatenate(dat+[Vgrid.ravel()]),
         (np.concatenate(rows+[site]), np.concatenate(cols+[site]))),
        shape=(N**3,)*2))
    return np.sort(eigsh(H, k=k, which='SA', return_eigenvectors=False))

def main():
    N, Nb = 48, 96
    gbig = greens(Nb)
    mi = ((np.arange(Nb)+Nb//2)%Nb)-Nb//2
    M1,M2,M3 = np.meshgrid(mi,mi,mi,indexing='ij')
    rb = np.linalg.norm(M1[...,None]*a1+M2[...,None]*a2+M3[...,None]*a3, axis=-1)
    A_true = np.mean((gbig*rb)[(rb>10)&(rb<20)])
    print(f"tail strength A = {A_true:.5f}")

    ii, jj, kk = np.meshgrid(np.arange(N),np.arange(N),np.arange(N),indexing='ij')
    m1 = ((ii+N//2)%N)-N//2; m2 = ((jj+N//2)%N)-N//2; m3 = ((kk+N//2)%N)-N//2
    r = np.linalg.norm(m1[...,None]*a1+m2[...,None]*a2+m3[...,None]*a3, axis=-1)
    r[0,0,0] = np.linalg.norm(a1)

    lc = 6.5
    vals = solve(N, -lc/r)
    b = vals[vals < -0.005]
    print(f"CONTROL 1/r: E1={b[0]:.4f} (Ry pred {-(1/64)*lc**2/2:.4f}); "
          f"E1/<E2> = {b[0]/np.mean(b[1:5]):.3f}; n2 = {np.round(b[1:5],4)}")

    gpot = gbig[m1%Nb, m2%Nb, m3%Nb].copy()
    gpot[0,0,0] = gbig[1,0,0]
    gpot -= gpot.min()
    vals = solve(N, -(lc/A_true)*gpot)
    b = vals[vals < -0.005]
    print(f"FOAM: E1={b[0]:.4f}; E1/<E2> = {b[0]/np.mean(b[1:5]):.3f}; "
          f"n2 = {np.round(b[1:5],4)}; 2s-2p defect = {b[1]-np.mean(b[2:5]):+.4f}")

if __name__ == "__main__":
    main()
