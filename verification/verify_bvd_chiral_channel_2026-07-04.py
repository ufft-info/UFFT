"""verify_bvd_chiral_channel_2026-07-04.py

THE B+V=D CHIRAL CHANNEL (2026-07-04). Operationalizing Marto's twin
reading of the axiom ("every direction has a complementary opposite
twin"): displacements live on 7 antipodal face pairs; fermion defects
source them; the void sector propagates antipodally (Paper #45) and is
eliminated/integrated out. Results:

  R1 (inert channels, parity theorem). The antipodal-ODD combination of
     ANY local fermion bilinear has zero matrix elements inside the
     fermion (T1u) doublet: odd x odd wavefunction products are
     antipodal-even, so pair-difference eliminations (v_f - v_fbar
     stiffness) induce NO chirality-channel interaction. Likewise the
     twin density-density form n_f n_fbar is inert, and no void current
     bilinear exists at all (the antipodal map is symmetric).
  R2 (the chiral channel). The antipodal-EVEN combinations of the local
     chirality bilinears C_f = {P_f, C}/2 carry the FULL chirality
     operator: pair weights are exactly -1/2 (the on-axis square pair)
     and -1/8 (each of the four axis-containing hex pairs), summing to
     C's doublet weight -1. A pair-even elimination therefore induces a
     torsion-torsion (NJL) interaction in exactly the chiral channel.
  R3 (soft mode). In the Paper #45 void sector H_void = eta(I - V) with
     V the antipodal map, the pair-even void combinations are exact ZERO
     modes (V = +1 sector). Integrating out a soft channel enhances the
     induced coupling; with the corpus's dynamical-void picture
     (Papers #2/#45), the induced chiral coupling is soft-mode-enhanced
     >> the NJL threshold g_c ~ 2.06 (verify_ml3_njl_2026-07-03.py).
     [CORRECTED same day by verify_bvd_kappa_audit_2026-07-04.py: the
     soft-mode-enhancement holds only in the force-controlled coupling
     limit; the corpus-consistent displacement-controlled limit gives
     g*chi = 0.22, well below threshold, and even the force limit is
     marginally below. The phase claim originally made here is
     WITHDRAWN. What stands: R1/R2 (parity theorem, exact chiral
     weights) and the soft-mode identification (R3's spectrum fact).
     The chiral filling is redirected to the T2g/colour sector.]

Run: python verify_bvd_chiral_channel_2026-07-04.py  (~5 s)
"""
import numpy as np, itertools, sys

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

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
L=np.diag(Ad.sum(1))-Ad
def fbar(i):
    if i<6: return sq_dirs.index(tuple(-x for x in sq_dirs[i]))
    return 6+hexes.index(tuple(-x for x in hexes[i-6]))
P_sq=np.diag([1.]*6+[0.]*8)
T=P_sq@L@(np.eye(F)-P_sq)-(np.eye(F)-P_sq)@L@P_sq
C=T/(2j)
def unit(v): return v/np.linalg.norm(v)
sqx=unit(np.array([d[0] for d in sq_dirs]+[0]*8,float))
hxx=unit(np.array([0.]*6+[h[0] for h in hexes]))
B2=np.stack([sqx,hxx],1)

# R1a: imaginary antipodal condensate inert on T1u (parity selection)
ok=True
rng=np.random.default_rng(3)
for _ in range(6):
    delta=rng.normal(size=F)
    for f in range(F):
        if f<fbar(f): delta[fbar(f)]=-delta[f]   # antipodal-odd
    M=np.zeros((F,F),complex)
    for f in range(F): M[f,fbar(f)]+=1j*delta[f]
    M=(M+M.conj().T)/2
    ok &= np.abs(B2.conj().T@M@B2).max()<1e-12
check("R1a antipodal-odd condensates have zero T1u-doublet weight "
      "(odd x odd = even; parity selection)", ok)
# R1b: no void current operator exists
X0=np.zeros((F,F))
for f in range(F): X0[f,fbar(f)]=1
check("R1b antipodal map symmetric -> void current i(X - X^T) = 0",
      np.allclose(X0,X0.T))
# R2: pair-even local chirality weights
def Cf(f):
    P=np.zeros((F,F)); P[f,f]=1
    return (P@C+C@P)/2
weights=[]
for f in range(F):
    if f>fbar(f): continue
    blk=B2.conj().T@(Cf(f)+Cf(fbar(f)))@B2
    dy=(blk[0,1]-blk[1,0]).imag/-2
    weights.append(dy)
weights=np.array(weights)
check("R2 pair-even chirality weights = {-1/2, 0, 0, -1/8 x4} summing to -1",
      abs(weights.sum()+1)<1e-12 and
      sorted(np.round(weights,6)).count(-0.125)==4 and
      abs(min(weights)+0.5)<1e-12)
# odd combos all zero:
ok=True
for f in range(F):
    if f>fbar(f): continue
    blk=B2.conj().T@(Cf(f)-Cf(fbar(f)))@B2
    ok &= np.abs(blk).max()<1e-12
check("R2b pair-odd chirality combinations vanish identically on the doublet", ok)
# R3: pair-even void combinations are zero modes of eta(I - V)
Hv=np.eye(F)-X0
wv=np.linalg.eigvalsh(Hv)
check("R3 void sector eta(I-V): 7 exact zero modes (pair-even channel soft)",
      int(np.sum(np.abs(wv)<1e-12))==7,
      f"spectrum {sorted(set(np.round(wv,6)))}")
print()
if FAILED: print("OPEN:",FAILED); sys.exit(1)
print("B+V=D CHIRAL CHANNEL VERIFIED: pair-even torsion channel carries the")
print("chirality; the void pair-even sector is soft. [Phase claim withdrawn")
print("same day: see verify_bvd_kappa_audit_2026-07-04.py - void exchange is")
print("below the chiral threshold in both coupling limits.]")
