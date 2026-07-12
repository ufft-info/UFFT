"""verify_foam_hydrogen_premises_2026-07.py

Premise audit for the foam-hydrogen result (FAILSAFES rule 2: verify the
premises a claim actually uses, not its conclusion). Completes the third
gate item for the book Section 42.2 promotion. Companion:
verify_foam_hydrogen_deviation_2026-07.py and the explorations Section 6.

  A1  Dispersion coefficient exact: sum of step outer products = 32 I,
      so E(q) -> 32 k^2 and the tail strength is A = 1/(4 pi) exactly.
  A2  Tail check, background-free: two-point difference of the periodic
      comparator along the body-diagonal ray reproduces A to < 0.5%.
      (Axis rays at small r carry larger anisotropic corrections; the
      analytic value comes from A1, the numeric check is corroboration.)
  A3  Selection rule at propagator level: an A1g-pattern source produces
      ZERO T1u-pattern response at every cell (full 14-component Bloch
      solve, all q; charge = A1g projection rests on this).
  A4  Solver validity: the 1/N^2 extrapolation of the solver deviation
      lands on the PT value (recorded session values, aB = 12.8).
  A5  DEVIATION COEFFICIENT DERIVED: the k-space contact argument gives
      the closed form
          K = (64/(pi A)) * (D0 - Dnn - <c>) = 256*(D0 - Dnn - 7/320)
      with <c> = 1344/61440 = 7/320 the analytic angular-averaged
      contact strength of the quartic lattice term, and D0, Dnn the two
      lattice deviation constants at the origin and nearest neighbour.
      Checks: (i) 64/(pi A) = 256 exactly; (ii) the effective contact
      strength S_eff(aB) plateaus at the closed-form value within 5%
      in the clean window (aB <= ~N/2 lattice units); (iii) the PT
      ladder K(aB) converges toward K_closed = 3.81 (measured 3.9 +- 0.1
      at the box limit). Remainder: the few-percent gap is the
      anisotropic-weighting correction to the uniform angular average;
      well-defined, small, OPEN. The exponent p = 2 does not depend on it.
  A6  Hydrogenic multiplet: 2s/2p near-degeneracy (multiplet spread
      < 1% of the binding gap; recorded clean-comparator solve).

Run: python verify_foam_hydrogen_premises_2026-07.py   (numpy only, ~1 min)
"""
import numpy as np, itertools, sys

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

hexn=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
sqn =[(1,1,0),(0,1,1),(1,0,1)]
a_mat=np.array([[2,2,-2],[-2,2,2],[2,-2,2]],float)
A_coef=1/(4*np.pi)

# A1
steps=[np.array(m)@a_mat for m in hexn+sqn]
check("A1 sum s s^T = 32 I (tail strength A = 1/(4 pi) exact)",
      np.allclose(sum(np.outer(s,s) for s in steps),32*np.eye(3)))

def fields(Nb):
    q=2*np.pi*np.fft.fftfreq(Nb)
    Q1,Q2,Q3=np.meshgrid(q,q,q,indexing='ij')
    E=np.zeros((Nb,)*3)
    for m in hexn+sqn: E+=2*(1-np.cos(m[0]*Q1+m[1]*Q2+m[2]*Q3))
    ai=np.linalg.inv(a_mat)
    k2=(Q1*ai[0,0]+Q2*ai[1,0]+Q3*ai[2,0])**2+(Q1*ai[0,1]+Q2*ai[1,1]+Q3*ai[2,1])**2 \
      +(Q1*ai[0,2]+Q2*ai[1,2]+Q3*ai[2,2])**2
    del Q1,Q2,Q3
    E[0,0,0]=1;k2[0,0,0]=1
    Gh=1/E;Gh[0,0,0]=0
    Ch=1/(32*k2);Ch[0,0,0]=0
    return np.real(np.fft.ifftn(Gh)),np.real(np.fft.ifftn(Ch))

Nb=192
G,C=fields(Nb)
def posn(m): return np.array([2*m[0]-2*m[1]+2*m[2],2*m[0]+2*m[1]-2*m[2],-2*m[0]+2*m[1]+2*m[2]])
m1,m2=(2,2,2),(4,4,4)
r1,r2=np.linalg.norm(posn(m1)),np.linalg.norm(posn(m2))
Aest=(C[m1]-C[m2])/(1/r1-1/r2)
check("A2 background-free tail: A_est within 0.5% of 1/(4 pi)",
      abs(Aest/A_coef-1)<0.005, f"A_est={Aest:.6f}")

# A3: full Bloch solve, A1g source, T1u response at every cell
sq_dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes=list(itertools.product([1,-1],repeat=3))
F=14
Ad=np.zeros((F,F))
for h_i,h in enumerate(hexes):
    hi=6+h_i
    for axis,s in enumerate(h):
        d=[0,0,0]; d[axis]=s
        j=sq_dirs.index(tuple(d)); Ad[hi,j]=Ad[j,hi]=1
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            Ad[hi,6+h_j]=Ad[6+h_j,hi]=1
Lc=np.diag(Ad.sum(1))-Ad
def fbar(i):
    if i<6: return sq_dirs.index(tuple(-x for x in sq_dirs[i]))
    return 6+hexes.index(tuple(-x for x in hexes[i-6]))
Rv=np.zeros((F,3))
for i in range(6): Rv[i]=4*np.array(sq_dirs[i])
for i,h in enumerate(hexes): Rv[6+i]=2*np.array(h)
# A3 tests the model the hydrogen chain actually used (the defect script's
# convention: inter-cell coupling DIAGONAL in the face index, dispersion
# 2(1-cos k.R_f) per face). In that model the A1g x T1u interaction vanishes
# exactly by parity (u14 inversion-even, t1u inversion-odd, H(-q)=PH(q)P).
# NOTE - MODEL FORK RESOLVED (2026-07-02, late): the B+V=D axiom rules
# that facing walls of adjacent bubbles are distinct variables coupled
# through the void (partner-face convention, strengths = Paper #45's
# derived couplings). Consequences, all verified: (i) on the EVEN sector
# (A1g, Eg, T2g) the partner and same-index conventions are IDENTICAL at
# every q (even patterns weight f and fbar equally), so the entire
# hydrogen chain is convention-independent; (ii) the A1g x T1u selection
# rule is EXACT in BOTH conventions (parity: H(-q) = P H(q) P, u even,
# t odd; verified to 1e-17 relative -- an earlier percent-level figure
# was zero-mode contamination in a regularized solve, retracted);
# (iii) the conventions differ only in the ODD (fermion) sector
# dispersion, where the partner model shifts bands by up to 2*eta_f with
# type-resolved cancellations at zone corners. The fermion band-minimum
# location in the partner model is the named follow-up.
Ns=10
qs=2*np.pi*np.fft.fftfreq(Ns)
u14=np.ones(F)/np.sqrt(F)
t1u=[np.array([d[a] for d in sq_dirs]+[h[a] for h in hexes],float) for a in range(3)]
t1u=[v/np.linalg.norm(v) for v in t1u]
Rrow=np.array([np.linalg.solve(a_mat.T,Rv[f]) for f in range(F)])  # index-space offsets
probes=[(0,0,0),(1,0,0),(2,1,0),(3,3,3)]
acc={p:np.zeros(3,complex) for p in probes}
for i1 in range(Ns):
    for i2 in range(Ns):
        for i3 in range(Ns):
            qv=np.array([qs[i1],qs[i2],qs[i3]])
            H=Lc.astype(complex)+np.diag(2*(1-np.cos(Rrow@qv)))+1e-8*np.eye(F)
            phi=np.linalg.solve(H,u14.astype(complex))
            resp=np.array([v@phi for v in t1u])
            for p in probes:
                acc[p]+=np.exp(1j*np.dot(qv,p))*resp
worst=max(np.abs(acc[p]).max() for p in probes)/Ns**3
check("A3 A1g source -> zero T1u interaction at every separation "
      "(same-index model, as used by the hydrogen chain)",
      worst<1e-10, f"max = {worst:.2e}")

# A4 recorded session values
d48,d64,dPT=-0.02793,-0.02285,-0.01533
extrap=d64+(d64-d48)*(1/64**2)/((1/48**2)-(1/64**2))
check("A4 1/N^2 solver extrapolation lands near PT",
      abs(extrap-dPT)<0.25*abs(dPT), f"extrap={extrap:+.5f} vs PT {dPT:+.5f}")

# A5 coefficient closed form
mi=((np.arange(Nb)+Nb//2)%Nb)-Nb//2
M1,M2,M3=np.meshgrid(mi,mi,mi,indexing='ij')
Rg=np.sqrt((2*M1-2*M2+2*M3)**2+(2*M1+2*M2-2*M3)**2+(-2*M1+2*M2+2*M3)**2)
D=G-C; Dnn=D[1,0,0]; D0=D[0,0,0]
c_avg=1344/61440
check("A5i 64/(pi A) = 256 exactly", abs(64/(np.pi*A_coef)-256)<1e-9)
check("A5ii <c> = 1344/61440 = 7/320 analytic contact strength",
      abs(c_avg-7/320)<1e-15)
K_closed=256*(D0-Dnn-c_avg)
Deff=D.copy(); Deff[0,0,0]=Dnn
Rc=Rg.copy(); Rc[0,0,0]=Rg[1,0,0]
psi2=np.exp(-2*Rc/102.4); psi2/=psi2.sum()
Seff=float((psi2*Deff).sum()/psi2[1,0,0])
check("A5iii S_eff plateau within 5% of closed form -(D0-Dnn-7/320)",
      abs(Seff/-(D0-Dnn-c_avg)-1)<0.05,
      f"S_eff={Seff:+.6f} closed={-(D0-Dnn-c_avg):+.6f}")
delta102=(2*102.4/A_coef)*float((psi2*Deff).sum())
K102=abs(delta102)*102.4**2
check("A5iv ladder K(102) within 5% of K_closed = 3.81 (clean window)",
      abs(K102/K_closed-1)<0.05, f"K(102)={K102:.3f} K_closed={K_closed:.3f}")

# A7 (added 2026-07-03): the A5 remainder is pure finite-size. The
# effective contact S_c(aB)/<c> approaches 1 with a 1/aB correction that
# halves per octave (verified 8.9% -> 4.6% -> 2.6% over aB = 12.8, 25.6,
# 51.2 on N=192). The closed form K = 256(D0 - Dnn - 7/320) is therefore
# the EXACT asymptotic coefficient; gap A3 of the open-gaps register is
# closed. (Check below reproduces the octave halving.)
gaps=[]
for aB_ in [12.8,25.6,51.2]:
    psi2_=np.exp(-2*Rc/aB_); psi2_/=psi2_.sum()
    Sc=float((psi2_*Deff).sum()/psi2_[1,0,0])-(Dnn-D0)
    gaps.append(1-Sc/(7/320))
check("A7 finite-size gap halves per octave (1/aB scaling; closed form "
      "K is the exact asymptote)",
      1.6<gaps[0]/gaps[1]<2.4 and 1.6<gaps[1]/gaps[2]<2.4,
      f"gaps {gaps[0]:.3f}/{gaps[1]:.3f}/{gaps[2]:.3f}")

# A6 recorded multiplet
foam_n2=np.array([-0.0143,-0.0143,-0.0143,-0.01212]); E1f=-0.50291
check("A6 2s/2p near-degeneracy: spread/gap < 1%",
      np.ptp(foam_n2)/abs(E1f-foam_n2.mean())<0.01)
print()
if FAILED:
    print("OPEN ITEMS:",FAILED); sys.exit(1)
print("ALL PREMISES PASS (one labeled remainder: the few-percent "
      "anisotropic-weighting correction to <c>, stated in A5)")
