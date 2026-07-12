"""Audit of ML3 step 1: does the FULL T1u sector (not the 2x2 projection)
carry a Chern number under a single-particle torsion term?

Multi-band (non-abelian) Fukui-Hatsugai Chern of the occupied subspace over a
2D BZ plane on the full 14-dim H(k). Occupied = the 3 lowest odd-character
bands (the r1 generation triad). Torsion perturbation m*C added to the full H,
C = T/2i Hermitian. If Chern stays 0 for all m, step 1's no-go is robust.
"""
import numpy as np, itertools
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
Psq=np.diag([1.]*6+[0.]*8)
T=Psq@L@(np.eye(F)-Psq)-(np.eye(F)-Psq)@L@Psq
C=(T/(2j))   # Hermitian chirality on full space
Pperm=np.zeros((F,F))
for f in range(F): Pperm[f,fbar(f)]=1
def Hk(kv,m):
    ee=np.array([es]*6+[eh]*8); X=np.zeros((F,F),complex)
    for f in range(F): X[f,fbar(f)]=ee[f]*np.exp(1j*np.dot(kv,Rrow[f]))
    return L.astype(complex)+np.diag(ee)-X+m*C
def occ_subspace(kv,m,nocc=3):
    w,V=np.linalg.eigh(Hk(kv,m))
    # odd-character bands: <v|Pperm|v> < 0; take the nocc lowest of those
    odd=[i for i in range(F) if np.real(V[:,i].conj()@Pperm@V[:,i])<0]
    odd_sorted=sorted(odd,key=lambda i:w[i])[:nocc]
    return V[:,odd_sorted]
def chern_plane(m,axfix=0.0,n=40):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False)
    # store occupied frames on grid
    U=[[occ_subspace(np.array([axfix,ky,kz]),m) for kz in ks] for ky in ks]
    tot=0.0
    for i in range(n):
        for j in range(n):
            u00=U[i][j]; u10=U[(i+1)%n][j]; u11=U[(i+1)%n][(j+1)%n]; u01=U[i][(j+1)%n]
            def link(a,b):
                M=a.conj().T@b; return np.linalg.det(M)/abs(np.linalg.det(M))
            F_=np.angle(link(u00,u10)*link(u10,u11)*link(u11,u01)*link(u01,u00))
            tot+=F_
    return tot/(2*np.pi)
print("Full-T1u occupied-subspace Chern over the (ky,kz) plane at kx=0:")
for m in [0.0,0.5,1.0,2.0]:
    print(f"   torsion m={m:+.1f}: Chern = {chern_plane(m):+.4f}")
print("If Chern == 0 for all m, step-1 no-go is ROBUST (full sector, not just 2x2).")
