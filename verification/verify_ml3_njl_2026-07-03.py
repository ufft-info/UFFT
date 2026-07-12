"""verify_ml3_njl_2026-07-03.py

ML3 step 2 (the interaction-driven chiral vacuum). Step 1
(verify_ml3_chirality_2026-07-03.py) ruled out single-particle band topology:
the foam T1u chirality must be interaction-driven, order parameter = the
inter-type torsion condensate <T> (equivalently <C>, C = T/2i = -sigma_y).

This run computes the canonical mechanism (Nambu-Jona-Lasinio) for generating
<T> != 0: a torsion-channel four-fermion interaction of strength g, mean-field
chirality mass m*C, Dirac sea = lower band e0 - sqrt(|d|^2 + m^2).

  N1  torsion susceptibility chi = mean_k[1/|d(k)|] is FINITE (the sector is
      gapped, min|d| ~ 2.05), so there is a CRITICAL coupling
      g_c = 1/chi ~ 2.06. Chiral symmetry breaking is NOT automatic.
  N2  gap equation 1/g = mean_k[1/sqrt(|d|^2+m^2)]: m = 0 for g <= g_c
      (chiral-SYMMETRIC), m > 0 for g > g_c (CHIRAL). Standard NJL transition.
  N3  g_c ~ mean|d| ~ fermion gap ~ |T| = 2 (the T1u torsion strength), because
      the fermion band is nearly flat (spread < 1%). SUGGESTIVE only: the foam
      sits near its own critical coupling; not claimed as derived.

The chirality polarization <C> != 0 is exactly what the Weinberg odd part
needs (P9: g_V/g_A measures the vacuum chirality polarization). So this is
on-target for A1 and for the emergence-bridge chiral fermions.

OPEN (step 3): the foam's ACTUAL torsion four-fermion coupling g, from the
B+V=D displacement-constraint vertex. Whether g > g_c decides whether the
foam is chiral. Since the SM is chiral, g > g_c is a falsifiable requirement.

Run: python verify_ml3_njl_2026-07-03.py  (~30 s)
"""
import itertools, sys
import numpy as np

FAILED=[]
def check(n,ok,d=""):
    print(("PASS  " if ok else "FAIL  ")+n+(("   "+d) if d else ""))
    if not ok: FAILED.append(n)

sq=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hx=list(itertools.product([1,-1],repeat=3)); F=14
Ad=np.zeros((F,F),int)
for hi_,h in enumerate(hx):
    hi=6+hi_
    for ax,s in enumerate(h):
        d=[0,0,0]; d[ax]=s; Ad[hi,sq.index(tuple(d))]=Ad[sq.index(tuple(d)),hi]=1
    for hj_,h2 in enumerate(hx):
        if hi_<hj_ and sum(a!=b for a,b in zip(h,h2))==1: Ad[hi,6+hj_]=Ad[6+hj_,hi]=1
L=np.diag(Ad.sum(1))-Ad
def fbar(i):
    if i<6: return sq.index(tuple(-x for x in sq[i]))
    return 6+hx.index(tuple(-x for x in hx[i-6]))
amat=np.array([[2,2,-2],[-2,2,2],[2,-2,2]],float)
Rv=np.zeros((F,3))
for i in range(6): Rv[i]=4*np.array(sq[i])
for i,h in enumerate(hx): Rv[6+i]=2*np.array(h)
Rrow=np.array([np.linalg.solve(amat.T,Rv[f]) for f in range(F)])
es=np.exp(-2*np.sqrt(2)); eh=np.exp(-np.sqrt(6))
def Hk(kv):
    ee=np.array([es]*6+[eh]*8); X=np.zeros((F,F),complex)
    for f in range(F): X[f,fbar(f)]=ee[f]*np.exp(1j*np.dot(kv,Rrow[f]))
    return L.astype(complex)+np.diag(ee)-X
def pol(ax):
    a=np.zeros(F); b=np.zeros(F)
    for i,dd in enumerate(sq): a[i]=dd[ax]
    for i,h in enumerate(hx): b[6+i]=h[ax]
    return np.stack([a/np.linalg.norm(a),b/np.linalg.norm(b)],1).astype(complex)
Bs=[pol(a) for a in range(3)]
n=16; ks=np.linspace(-np.pi,np.pi,n,endpoint=False)
dm=[]
for kx in ks:
    for ky in ks:
        for kz in ks:
            H=Hk(np.array([kx,ky,kz]))
            for B in Bs:
                blk=B.conj().T@H@B
                dm.append(np.hypot(np.real(blk[0,1]),0.5*np.real(blk[0,0]-blk[1,1])))
dm=np.array(dm); chi=np.mean(1.0/dm); gc=1.0/chi
check("N1 torsion susceptibility chi=mean(1/|d|) finite (gapped, min|d|>2); "
      "critical coupling g_c=1/chi exists",
      dm.min()>2.0 and 0.4<chi<0.6, f"min|d|={dm.min():.3f} chi={chi:.4f} g_c={gc:.4f}")
def gap_m(g):
    if g<=gc*(1+1e-9): return 0.0
    lo,hib=0.0,50.0
    for _ in range(80):
        m=0.5*(lo+hib)
        if np.mean(1.0/np.sqrt(dm**2+m**2))>1.0/g: lo=m
        else: hib=m
    return 0.5*(lo+hib)
m_below=gap_m(0.5*gc); m_at=gap_m(gc); m_above=gap_m(1.5*gc)
check("N2 NJL transition: m=0 for g<=g_c (symmetric), m>0 for g>g_c (chiral)",
      m_below<1e-6 and m_at<1e-3 and m_above>1e-2,
      f"m(0.5gc)={m_below:.3f} m(1.5gc)={m_above:.3f}")
check("N3 g_c ~ mean|d| ~ |T|=2 (near-flat band, spread<1%): foam near "
      "critical (SUGGESTIVE, not claimed)",
      abs(gc-dm.mean())/dm.mean()<0.02 and abs(gc-2.0)<0.1,
      f"g_c={gc:.3f} mean|d|={dm.mean():.3f}")

print()
if FAILED: print("OPEN/FAIL:",FAILED); sys.exit(1)
print(f"ML3 step2: NJL torsion-condensate mechanism available; g_c={gc:.3f}; "
      "foam chiral iff its B+V=D torsion coupling exceeds g_c (step 3)")
