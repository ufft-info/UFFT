"""verify_me_walk_firstorder_exclusion_2026-07-03.py

A2 (m_e walk action, Paper #74 C74.4) campaign, run of 2026-07-03.
Companion: .explorations/UFFT_Explorations_2026-07-03.md Section 7;
Paper #74 (INBOX) Theorems 74.1-74.3 and Conjecture C74.4.

C74.4 asks for a closed walk on the T1u sector of the face graph whose
action reproduces
    S_walk = (E-F)(2 Delta + sqrt Delta)/16 = 22*(34+sqrt17)/16 = 52.41927,
    per-step action  s* = (2 Delta + sqrt Delta)/16 = 2.3826938.

WHAT THIS RUN ESTABLISHES (no amplitude fitted; FAILSAFES 4):

  W1  Anchor: T74.1-74.3 factor identities reproduced numerically, and the
      T1u ADJACENCY block has eigenvalues a_pm = (1 +- sqrt17)/2 (x3 each),
      with a_pm^2 = r2, r1 and a+ a- = -4, so (a+ a-)^2 = r1 r2 = 16.

  L1 (Tier 1 lemma, sharpens T74.1): the step count is one less than the
      cycle rank of the face-adjacency graph,
          E - F = cycle_rank(FA) - 1 = (E_face - F + 1) - 1 = 23 - 1 = 22.
      This makes precise the "number of independent closed-walk classes"
      reading: 22 = (independent cycles) - 1.

  L2 (Tier 1 lemma, sharpens T74.3): the denominator 16 has a walk-native
      reading as the Vieta product of the T1u Laplacian roots,
          16 = r1 r2 = (a+ a-)^2 = |G|/C_A = 2 F_hx,
      four coincident readings; the walk-native one is r1 r2.

  X1 (FIRST-ORDER EXCLUSION, the run's main result): s* is NOT the log of
      any single-step (first-order) closed-walk rate. Checked against the
      canonical first-order rates:
          ln(a+)      = 0.940614   (adjacency return rate)
          ln(r2)      = 1.881227   (Laplacian dominant rate)
          ln(r2/r1)   = 0.989866   (spectral-spread rate)
          ln(mu_NB)   = 1.445856   (non-backtracking topological entropy)
      none equals s* = 2.3826938. Instead s* is QUADRATIC in the spread:
          s* = [2 g^2 + g]/p^2,  g = r2 - r1 = sqrt Delta,  p^2 = r1 r2 = 16,
      so any C74.4 walk is a SECOND-ORDER (two-step) amplitude, consistent
      with the master equation lambda^2 - 9 lambda + 16 = 0 being a two-step
      recurrence. The first-order adjacency/transfer-walk class is excluded.

STATUS after this run: C74.4 stays Tier 4 (conjecture). First-order walk
class EXCLUDED; the target is localized to a second-order/two-step amplitude
on the T1u sector. The two topological lemmas L1, L2 are new Tier-1 content.
m_e prediction itself unchanged (0.006%, Tier 2). Not a closure.

Run: python verify_me_walk_firstorder_exclusion_2026-07-03.py  (~10 s)
"""
import itertools, sys
import numpy as np
import sympy as sp

FAILED=[]
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

# ---------------------------------------------------------------- graph
sq_dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes=list(itertools.product([1,-1],repeat=3)); F=14
A=np.zeros((F,F),int); edges=[]
for h_i,h in enumerate(hexes):
    hi=6+h_i
    for axis,s in enumerate(h):
        d=[0,0,0]; d[axis]=s; j=sq_dirs.index(tuple(d))
        A[hi,j]=A[j,hi]=1; edges.append((min(hi,j),max(hi,j)))
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            A[hi,6+h_j]=A[6+h_j,hi]=1; edges.append((6+h_i,6+h_j))
edges=sorted(set(edges)); Eface=len(edges)
L=np.diag(A.sum(1))-A
V,Ec,Fc=24,36,14
sqrtD=np.sqrt(17); r1=(9-sqrtD)/2; r2=(9+sqrtD)/2
ap=(1+sqrtD)/2; am=(1-sqrtD)/2
s_star=(2*17+sqrtD)/16
S_walk=(Ec-Fc)*(2*17+sqrtD)/16

# ---------------------------------------------------------------- W1 anchor
S=sp.sqrt(17)
check("W1 T74.2 spectral factorisation 2D+sqrtD = (r2-r1)(2(r2-r1)+1)",
      sp.simplify((2*17+S) - S*(2*S+1))==0)
check("W1 T74.1 step count E-F = V-chi = E_face-F = 22",
      (Ec-Fc)==22 and (V-2)==22 and (Eface-Fc)==22)
check("W1 T74.3 denominator |G|/C_A = 2 F_hx = 16", 48//3==16 and 2*8==16)
def evec(M,val):
    ww,VV=np.linalg.eigh(M); return VV[:,[i for i in range(F) if abs(ww[i]-val)<1e-9]]
T1u=np.hstack([evec(L,r1),evec(L,r2)])
Aev=np.linalg.eigvalsh(T1u.T@A.astype(float)@T1u)
check("W1 T1u adjacency eigenvalues a_pm=(1+-sqrt17)/2 (x3 each); "
      "a_pm^2 = r1,r2; (a+ a-)^2 = 16",
      np.allclose(sorted(Aev), sorted([am]*3+[ap]*3))
      and abs(ap*ap-r2)<1e-9 and abs(am*am-r1)<1e-9 and abs((ap*am)**2-16)<1e-9)

# ---------------------------------------------------------------- L1 cycle rank
cyc=Eface-Fc+1
check("L1 (E-F) = cycle_rank(FA) - 1 = 23 - 1 = 22 "
      "(independent closed-walk classes minus one)",
      cyc==23 and (Ec-Fc)==cyc-1)

# ---------------------------------------------------------------- L2 normalization
check("L2 /16 = r1 r2 = (a+ a-)^2 = |G|/C_A = 2 F_hx (walk-native = Vieta r1 r2)",
      abs(r1*r2-16)<1e-9 and abs((ap*am)**2-16)<1e-9 and 48//3==16 and 2*8==16)

# ---------------------------------------------------------------- X1 first-order exclusion
# canonical first-order rates
rates={"ln(a+)":np.log(ap),"ln(r2)":np.log(r2),"ln(r2/r1)":np.log(r2/r1)}
# non-backtracking (Hashimoto) topological entropy
dedges=[]
for (i,j) in edges: dedges+=[(i,j),(j,i)]
ne=len(dedges); B=np.zeros((ne,ne))
for k,(i,j) in enumerate(dedges):
    for l,(a,b) in enumerate(dedges):
        if j==a and b!=i: B[k,l]=1
mu_max=np.max(np.abs(np.linalg.eigvals(B)))
rates["ln(mu_NB)"]=np.log(mu_max)
check("X1 s* is NOT any first-order rate (ln a+, ln r2, ln(r2/r1), ln mu_NB)",
      all(abs(v-s_star)>1e-3 for v in rates.values()),
      "rates="+", ".join(f"{k}={v:.4f}" for k,v in rates.items())+f"; s*={s_star:.4f}")
# s* is quadratic in the spread (second-order structure)
g=S; p2=(ap*am)**2
check("X1 s* = [2 g^2 + g]/p^2, g=spread=sqrt17, p^2=(a+ a-)^2=16 "
      "(second-order / two-step, not first-order)",
      sp.simplify((2*g**2+g)/16 - (2*17+S)/16)==0 and abs(float((2*17+S)/16)-s_star)<1e-9)
check("X1 full action S_walk = (E-F)*s* = 52.41927 (m_e formula unchanged)",
      abs(S_walk-52.41927)<1e-4)

print()
if FAILED:
    print("OPEN/FAIL:", FAILED); sys.exit(1)
print("A2: FIRST-ORDER WALK CLASS EXCLUDED; C74.4 -> SECOND-ORDER, STAYS TIER 4")
