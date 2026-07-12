"""verify_weinberg_triad_normalization_2026-07-03.py

A1 (Weinberg mixing weight) campaign, run of 2026-07-03 (later run, after the
void-protection theorem). Companion: .explorations/UFFT_Explorations_2026-07-03.md
Section 6; obstruction chain in verify_Weinberg_obstruction_2026-07.py (P4-P13);
triad in verify_void_protection_2026-07-03.py.

WHAT THIS RUN ESTABLISHES. Result 58.3 splits by Galois parity (P13):

    sin^2(theta_W) = Delta/(Delta+C_A)  -  C_A*sqrt(Delta)/(Delta+C_A)
                     \___ even (rational) ___/   \___ odd (sqrt17) ___/

The DENOMINATOR / even normalization is derived here from the void-protected
generation triad; the ODD numerator remains obstructed to the chiral filling.

  V1  Triad reconstruction: the three protected face-center vacua reproduce
      the void-protection theorem geometry (pairwise |overlap| = 1/2,
      Bargmann invariant = +1/8 real, square content s1 each). Same triad.

  V2  NORMALIZATION IDENTIFICATION (the run's positive result, Tier 2 identity):
      each vacuum has Delta * n_z^2 = 1 exactly (n_z = -1/sqrt(Delta),
      void-protected), so summed over the triad
          C_A := Delta * sum_gen n_z^2 = N_gen = 3,
      and the Weinberg normalization is the triad's total dipole strength
          Delta + C_A = Delta * (1 + sum_gen n_z^2) = 20.
      Void-invariant: holds for arbitrary eta_sq, eta_hx (checked at physical,
      arbitrary, and zero couplings). Galois-even (rational), band-blind.
      Tier 3 reading (flagged, not asserted): the normalization integer that
      enters Result 58.3 as C_A here equals the generation count N_gen; whether
      this coincides for a reason with the colour reading of C_A (torsion
      ladder 12/4, A1g rotation theorem) is left open.

  V3  Even/odd split is exact with the triad-derived denominator:
      sin^2 = Delta/(Delta+C_A) - C_A*sqrt(Delta)/(Delta+C_A), C_A=3, Delta=17.

  V4  P14 (triad-level obstruction, Tier 1): every single-particle chirality
      expectation <vac|C|vac> = 0, on BOTH Galois branches (r1 and r2).
      The Galois-odd datum (which band is left-handed) is not present in the
      triad's single-particle data. The odd numerator C_A*sqrt(Delta) is not
      accessible from triad geometry; it requires the root-selecting chiral
      filling (P13 unchanged). Consistent with P9/P10.

STATUS after this run: A1 denominator/normalization DERIVED from the triad
(Galois-even half). A1 odd numerator OPEN (needs the chiral vacuum, ML3).
Result 58.3 stays Match-Gate FAIL-standalone until the odd part is derived.

Run: python verify_weinberg_triad_normalization_2026-07-03.py  (~20 s)
"""
import itertools, sys
import numpy as np
import sympy as sp

FAILED=[]
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

# ---------------------------------------------------------------- geometry
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
Pperm=np.zeros((F,F))
for f in range(F): Pperm[f,fbar(f)]=1

def vac_at(axis, esq, ehx, root=r1):
    ee=np.array([esq]*6+[ehx]*8)
    q=np.zeros(3); q[axis]=np.pi
    X=np.zeros((F,F),complex)
    for f in range(F): X[f,fbar(f)]=ee[f]*np.exp(1j*np.dot(q,Rrow[f]))
    H=L.astype(complex)+np.diag(ee)-X
    w,V=np.linalg.eigh(H)
    cand=[i for i in range(F) if abs(w[i]-root)<1e-6]
    if not cand: return None
    i0=min(cand,key=lambda i: np.real(V[:,i].conj()@Pperm@V[:,i]))
    return V[:,i0]/np.linalg.norm(V[:,i0])

e_sq=np.exp(-2*np.sqrt(2)); e_hx=np.exp(-np.sqrt(6))
s1=(np.sqrt(17)+1)/(2*np.sqrt(17))

# ---------------------------------------------------------------- V1 triad
triad=[vac_at(ax,e_sq,e_hx) for ax in range(3)]
ov=np.array([[abs(triad[i].conj()@triad[j]) for j in range(3)] for i in range(3)])
barg=(triad[0].conj()@triad[1])*(triad[1].conj()@triad[2])*(triad[2].conj()@triad[0])
sc=[float(np.sum(np.abs(v[:6])**2)) for v in triad]
check("V1 triad reproduces void-protection geometry: |overlap|=1/2, "
      "Bargmann=+1/8 real, square content=s1",
      np.allclose(ov-np.eye(3)*(1-0.5), 0.5) and abs(barg-0.125)<1e-9
      and abs(barg.imag)<1e-9 and all(abs(x-s1)<1e-12 for x in sc))

# ---------------------------------------------------------------- V2 normalization
rows=[]
for (esq,ehx) in [(e_sq,e_hx),(0.11,0.37),(0.0,0.0)]:
    tri=[vac_at(ax,esq,ehx) for ax in range(3)]
    nz=[float(np.sum(np.abs(v[:6])**2)-np.sum(np.abs(v[6:])**2)) for v in tri]
    rows.append(17*sum(n*n for n in nz))
check("V2 C_A = Delta*sum_gen n_z^2 = 3 = N_gen, void-invariant "
      "(physical, arbitrary, zero couplings)",
      all(abs(c-3.0)<1e-9 for c in rows),
      f"Delta*sum n_z^2 = {[round(c,10) for c in rows]}")
D=sp.symbols('Delta',positive=True)
check("V2 symbolic: Delta*n_z^2 = 1 for n_z = -1/sqrt(Delta) (per vacuum)",
      sp.simplify(D*(-1/sp.sqrt(D))**2 - 1)==0)

# ---------------------------------------------------------------- V3 split
S17=sp.sqrt(17); CA=sp.Integer(3); Dv=sp.Integer(17)
sin2=(17-3*S17)/20
check("V3 normalization Delta+C_A = Delta*(1+N_gen/Delta) = 20",
      sp.simplify((Dv+CA) - Dv*(1+3/Dv))==0 and (Dv+CA)==20)
check("V3 even/odd split: sin^2 = Delta/(Delta+C_A) - C_A*sqrt(Delta)/(Delta+C_A)",
      sp.simplify(Dv/(Dv+CA) - CA*sp.sqrt(Dv)/(Dv+CA) - sin2)==0)

# ---------------------------------------------------------------- V4 P14 obstruction
Psq=np.diag([1.]*6+[0.]*8)
T=Psq@L@(np.eye(F)-Psq)-(np.eye(F)-Psq)@L@Psq
C=T/(2j)                                   # chirality operator (T/2i)
chi_r1=[abs(np.real(v.conj()@C@v)) for v in triad]
triad_r2=[vac_at(ax,e_sq,e_hx,root=r2) for ax in range(3)]
chi_r2=[abs(np.real(v.conj()@C@v)) for v in triad_r2 if v is not None]
check("V4 P14: single-particle chirality expectation <vac|C|vac> = 0 on "
      "BOTH Galois branches (odd part not in triad geometry)",
      max(chi_r1)<1e-9 and (len(chi_r2)==3 and max(chi_r2)<1e-9),
      f"max|<C>| r1={max(chi_r1):.1e}, r2={(max(chi_r2) if chi_r2 else float('nan')):.1e}")
# the achiral Bargmann phase is the same statement: no chirality contrast
check("V4 Bargmann invariant real (+1/8): bare triad achiral, so a "
      "band-symmetric (Galois-even) triad sum cannot carry sqrt(17)",
      abs(barg.imag)<1e-12 and abs(barg.real-0.125)<1e-9)

print()
if FAILED:
    print("OPEN/FAIL:", FAILED); sys.exit(1)
print("TRIAD NORMALIZATION DERIVED; ODD NUMERATOR REMAINS OPEN (chiral filling)")
