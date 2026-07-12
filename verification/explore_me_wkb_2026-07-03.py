"""A2 construction 2: inter-vacuum WKB through the T1u band (2026-07-03).

Uses the void-protected triad: three generation vacua at the zone face-
centers q* = pi e_axis (energy r1). m_e generation as an under-barrier
amplitude between two generation vacua along the connecting q-path, through
the odd (fermion) band. WKB action

    S_WKB = INT kappa(q) dq,   kappa = sqrt( 2 m_eff (E_band(q) - r1) )

with E_band the lowest odd-character band. No target forced: report the raw
integral and compare to per-step s* = (2D+sqrtD)/16 = 2.382694 and to
S_walk = 52.41927, stating the ambiguities (m_eff, path, the 2m factor).

FINDING (2026-07-03): the inter-vacuum barrier along the face-center path is
eta-scale (about 0.021 above r1), NOT the gap sqrtD = 4.12. So the
explorations Section 3 premise ("the gap sqrtD enters as the barrier scale")
is corrected: sqrtD is the vertical band gap to r2, not the horizontal
barrier between generation minima (which is tiny). The WKB action is small
(0.4 to 4.3 depending on the arbitrary effective mass) and does not reach
s* or S_walk. Construction 2 does not close A2.
"""
import numpy as np, itertools
from numpy import trapezoid
np.set_printoptions(precision=6, suppress=True)

sq_dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes=list(itertools.product([1,-1],repeat=3)); F=14
Ad=np.zeros((F,F),int)
for h_i,h in enumerate(hexes):
    hi=6+h_i
    for axis,s in enumerate(h):
        d=[0,0,0]; d[axis]=s; j=sq_dirs.index(tuple(d)); Ad[hi,j]=Ad[j,hi]=1
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            Ad[hi,6+h_j]=Ad[6+h_j,hi]=1
L=np.diag(Ad.sum(1))-Ad
def fbar(i):
    if i<6: return sq_dirs.index(tuple(-x for x in sq_dirs[i]))
    return 6+hexes.index(tuple(-x for x in hexes[i-6]))
a_mat=np.array([[2,2,-2],[-2,2,2],[2,-2,2]],float)
Rv=np.zeros((F,3))
for i in range(6): Rv[i]=4*np.array(sq_dirs[i])
for i,h in enumerate(hexes): Rv[6+i]=2*np.array(h)
Rrow=np.array([np.linalg.solve(a_mat.T,Rv[f]) for f in range(F)])
r1=(9-np.sqrt(17))/2; r2=(9+np.sqrt(17))/2
e_sq=np.exp(-2*np.sqrt(2)); e_hx=np.exp(-np.sqrt(6))
Pperm=np.zeros((F,F))
for f in range(F): Pperm[f,fbar(f)]=1
def H_partner(qv):
    ee=np.array([e_sq]*6+[e_hx]*8)
    X=np.zeros((F,F),complex)
    for f in range(F): X[f,fbar(f)]=ee[f]*np.exp(1j*np.dot(qv,Rrow[f]))
    return L.astype(complex)+np.diag(ee)-X
def odd_band(qv):
    w,V=np.linalg.eigh(H_partner(qv))
    best=None
    for i in range(F):
        odd=np.real(V[:,i].conj()@Pperm@V[:,i])
        if odd<-0.2:
            if best is None or w[i]<best: best=w[i]
    return best

s_star=(2*17+np.sqrt(17))/16
S_walk=22*s_star
print(f"per-step s* = {s_star:.6f}, S_walk = {S_walk:.5f}, r1 = {r1:.6f}, gap sqrtD = {np.sqrt(17):.6f}")

q1=np.array([np.pi,0,0]); q2=np.array([0,np.pi,0])
N=2001
ts=np.linspace(0,1,N)
Es=np.array([odd_band(q1+(q2-q1)*t) for t in ts])
path_len=np.linalg.norm(q2-q1)
dq=path_len/(N-1)
print(f"\nband along q1->q2: E(start)={Es[0]:.6f} E(mid)={Es[N//2]:.6f} "
      f"E(end)={Es[-1]:.6f}, barrier max={Es.max():.6f}")
print(f"barrier height above r1 = {Es.max()-r1:.6f}  (gap to r2 = {r2-r1:.6f})")

under=np.clip(Es-r1,0,None)
for two_m,tag in [(1.0,"2m=1"),(2.0,"2m=2")]:
    kappa=np.sqrt(two_m*under)
    S=trapezoid(kappa,dx=dq)
    print(f"  WKB action ({tag}) over one face-center segment = {S:.6f}")
h=1e-3
Em=odd_band(q1+(q2-q1)/path_len*h); E0=Es[0]
curv=2*(Em-E0)/h**2
print(f"\nband curvature at vacuum d2E/dq2 ~ {curv:.4f} -> m_eff=1/curv={1/curv:.4f}")
if curv>0:
    kappa=np.sqrt((2/curv)*under)
  