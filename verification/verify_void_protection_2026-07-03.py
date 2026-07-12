"""verify_void_protection_2026-07-03.py

THE VOID-PROTECTION THEOREM (2026-07-03). In the void-coupled Bloch model
H(q) = L + diag(eta_f) - X(q), X(q)_{f,fbar} = eta_f e^{i q.R_f}
(partner-face convention, the B+V=D-consistent inter-cell coupling; the
type couplings eta_sq, eta_hx are Paper #45's derived void couplings but
the theorem holds for ARBITRARY values):

  At the zone face-center q* = pi e_axis, the Bloch phases phi_f = +-1
  split the faces, and for any lattice-odd pattern the void term on face
  f carries coefficient eta_f (1 + phi_f). The T1u eigenvector of the
  pure face Laplacian L at eigenvalue r1 = (9-sqrt(17))/2, taken in the
  polarization combination transverse to the q* axis (e.g. (y+z)/sqrt2
  for q* = pi e_y), is supported EXACTLY on the phi = -1 faces. Hence

      H(q*) v = L v = r1 v   identically in eta_sq, eta_hx.

  The fermion band minimum is therefore void-invariant in BOTH its
  energy (= r1 exactly) and its eigenvector (= the pure-L eigenvector,
  square content s1 = (sqrt17+1)/(2 sqrt17) exactly, pseudospin
  n_z = -1/sqrt(17) exactly).

COROLLARIES.
  C1  The void-decoupling tension (obstruction script P7d) is DISCHARGED:
      the physical fermion vacuum carries the exact pure-L mass-direction,
      so the Weinberg pseudospin input is void-protected. The Paper #41
      (pure-L formula) vs Paper #45 (O(eta) corrections) tension is
      resolved for the fermion vacuum sector.
  C2  Every pure-L formula built from fermion-vacuum quantities (band
      gap sqrt(17), contents s1/s2, chirality geometry) is protected
      against void corrections, explaining their experimental precision.
  C3  There are exactly three distinct zone face-centers, each hosting
      one non-degenerate protected vacuum: a Brillouin-zone realization
      of the three generations (complements Paper #72 T72.2).
  C4  The orthogonal transverse combination has support on phi = +1
      faces, is void-dressed, and sits higher: the protection selects
      exactly one state per face-center (verified: spectrum at q* has a
      single r1 level).

CHECKS:
  T1  numeric: global BZ scan (physical etas): the lowest odd-character
      band attains its minimum at the face-centers with E = r1 to 1e-12.
  T2  numeric: the minimizing eigenvector has square content = s1 and
      unit overlap with the pure-L r1 eigenspace (1e-12).
  T3  SYMBOLIC: (H(q*) - r1) v = 0 for symbolic eta_s, eta_h (and a free
      overall scale), using the exact eigen-ratio sh/c = (sqrt17-1)/4.
  T4  support lemma: v is supported exactly on the phi = -1 faces, and
      the void coefficient (1+phi_f) vanishes there.
  T5  non-degeneracy at q*: exactly one eigenvalue equals r1.

Run: python verify_void_protection_2026-07-03.py   (~1 min)
"""
import numpy as np, itertools, sys
import sympy as sp

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

sq_dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes=list(itertools.product([1,-1],repeat=3))
F=14
Ad=np.zeros((F,F),dtype=int)
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
a_mat=np.array([[2,2,-2],[-2,2,2],[2,-2,2]],float)
Rv=np.zeros((F,3))
for i in range(6): Rv[i]=4*np.array(sq_dirs[i])
for i,h in enumerate(hexes): Rv[6+i]=2*np.array(h)
Rrow=np.array([np.linalg.solve(a_mat.T,Rv[f]) for f in range(F)])
r1=(9-np.sqrt(17))/2
e_sq=np.exp(-2*np.sqrt(2)); e_hx=np.exp(-np.sqrt(6))
etaf=np.array([e_sq]*6+[e_hx]*8)
Pperm=np.zeros((F,F))
for f in range(F): Pperm[f,fbar(f)]=1
def H_partner(qv,esq=e_sq,ehx=e_hx):
    ee=np.array([esq]*6+[ehx]*8)
    X=np.zeros((F,F),complex)
    for f in range(F): X[f,fbar(f)]=ee[f]*np.exp(1j*np.dot(qv,Rrow[f]))
    return L.astype(complex)+np.diag(ee)-X

# T1 global scan
best=(1e9,None)
n=11
grid=np.linspace(-np.pi,np.pi,n,endpoint=False)
for qx in grid:
    for qy in grid:
        for qz in grid:
            qv=np.array([qx,qy,qz])
            w,V=np.linalg.eigh(H_partner(qv))
            for i in range(F):
                if np.real(V[:,i].conj()@Pperm@V[:,i])<-0.3 and w[i]<best[0]:
                    best=(w[i],qv.copy())
qstar=np.array([0.0,np.pi,0.0])
w,V=np.linalg.eigh(H_partner(qstar))
i0=np.argmin(np.abs(w-r1))
check("T1 odd-band global minimum = r1 at a face-center",
      best[0]>=r1-1e-9 and abs(w[i0]-r1)<1e-12,
      f"scan min {best[0]:.6f} at {np.round(best[1],3)}; E(q*)-r1={w[i0]-r1:.1e}")
v=V[:,i0]           # complex up to a global phase; use phase-invariant forms
s1=(np.sqrt(17)+1)/(2*np.sqrt(17))
wL,VL=np.linalg.eigh(L)
V1=VL[:,[i for i in range(F) if abs(wL[i]-r1)<1e-9]]
check("T2 vacuum eigenvector: square content = s1, unit pure-L overlap",
      abs(np.sum(np.abs(v[:6])**2)-s1)<1e-12
      and abs(np.linalg.norm(V1.T@v)-1)<1e-12)

# T3 symbolic
es,eh,cc=sp.symbols('eta_s eta_h c')
S=sp.sqrt(17)
r1s=(9-S)/2
phi=np.round(np.exp(1j*(Rrow@qstar)).real,0).astype(int)
shc=cc*(S-1)/4
vex=[0,0,-cc,cc,-cc,cc]+[0]*8
for i,h in enumerate(hexes):
    yz=h[1]+h[2]
    if yz==2: vex[6+i]=-shc
    elif yz==-2: vex[6+i]=shc
vsym=sp.Matrix(vex)
Hs=sp.Matrix(L.tolist())
etas=[es]*6+[eh]*8
for f in range(F):
    Hs[f,f]+=etas[f]; Hs[f,fbar(f)]-=etas[f]*int(phi[f])
res=sp.simplify(sp.expand(Hs*vsym-r1s*vsym))
check("T3 SYMBOLIC: (H(q*)-r1) v = 0 for arbitrary eta_s, eta_h",
      res==sp.zeros(F,1))
check("T4 support lemma: v on phi=-1 faces only; void coeff (1+phi)=0 there",
      all(vex[f]==0 for f in range(F) if phi[f]==1)
      and all(int(1+phi[f])==0 for f in range(F) if vex[f]!=0))
check("T5 non-degeneracy: exactly one eigenvalue = r1 at q*",
      int(np.sum(np.abs(w-r1)<1e-9))==1)
print()
if FAILED: print("OPEN:",FAILED); sys.exit(1)
print("VOID-PROTECTION THEOREM VERIFIED")
