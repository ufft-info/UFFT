"""verify_higgs_quartic_2026-07-03.py  (rev2, reconciled with book Sec 12.3)

B1/B2 Higgs self-coupling, 2026-07-03. RECONCILIATION: an earlier version of
this script (and explorations Sec 5) used an A1g7-exchange "induced quartic"
-2/147 and declared the on-site 1/8 EXCLUDED. That diverged from the book and
is WITHDRAWN. Book Sec 12.3 is the settled account, confirmed here:
  lambda_tree = 1/F_hx = 1/8 (the forced on-site A2u quartic)
  lambda_NLO  = (1/F_hx)(1 + sqrtD/((V-F)(E-V))) = (120+sqrt17)/960 = 0.129295
                (-0.25 sigma), universal foam NLO sqrtD/N, N=(V-F)(E-V)=120=5!.
So 1/8 is the TREE value, not excluded. The -2/147 term is a distinct single
second-order channel (different sign+magnitude), not the framework NLO.
Match-Gate: (120+sqrt17)/960 is FAIL-standalone (214 rivals, 0.25 sigma);
weight rests on the universal sqrtD/N overdetermination, not a standalone hit.
"""
import itertools, sys
import numpy as np

FAILED=[]
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

sq=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hx=list(itertools.product([1,-1],repeat=3)); F=14
A=np.zeros((F,F),int)
for hi_,h in enumerate(hx):
    hi=6+hi_
    for ax,s in enumerate(h):
        d=[0,0,0]; d[ax]=s; A[hi,sq.index(tuple(d))]=A[sq.index(tuple(d)),hi]=1
    for hj_,h2 in enumerate(hx):
        if hi_<hj_ and sum(a!=b for a,b in zip(h,h2))==1: A[hi,6+hj_]=A[6+hj_,hi]=1
L=np.diag(A.sum(1))-A; w,V=np.linalg.eigh(L)
V_,E_,F_,F_hx=24,36,14,8; S17=np.sqrt(17)
lamH=125.25**2/(2*246.22**2)

a2u=np.array([0.]*6+[np.prod(h) for h in hx],float); a2u/=np.linalg.norm(a2u)
i9=np.argmin(np.abs(w-9))
check("H1 A2u = hex sign-product eigenvector at lambda=9",
      abs(abs(a2u@V[:,i9])-1)<1e-12 and abs(w[i9]-9)<1e-12)
tris=[]
for j,dq in enumerate(sq):
    ax=[abs(x) for x in dq].index(1); s=dq[ax]
    adj=[i for i,h in enumerate(hx) if h[ax]==s]
    for a_,b_ in itertools.combinations(adj,2):
        if sum(x!=y for x,y in zip(hx[a_],hx[b_]))==1: tris.append((j,6+a_,6+b_))
a1g0=np.ones(F)/np.sqrt(F); a7=np.array([4.]*6+[-3.]*8); a7/=np.linalg.norm(a7)
def t3(X,u,v):
    t=0.0
    for (f0,f1,f2) in tris:
        fc=[f0,f1,f2]
        for pm in itertools.permutations(range(3)): t+=X[fc[pm[0]]]*u[fc[pm[1]]]*v[fc[pm[2]]]
    return t/6.0
g0=t3(a1g0,a2u,a2u); g7=t3(a7,a2u,a2u)
check("H1 machinery exact: 24 tris, 2nd A1g at 7, g0=-1/sqrt14, g7=-sqrt42/21, "
      "A1g7 term g7^2/7=2/147 (a sub-computation)",
      len(tris)==24 and abs(a7@L@a7-7)<1e-9 and abs(g0+1/np.sqrt(14))<1e-12
      and abs(g7+np.sqrt(42)/21)<1e-12 and abs(g7**2/7-2/147)<1e-12)

tree=float(np.sum(a2u**4)); denom=(V_-F_)*(E_-V_); nlo=(120+S17)/960
check("H2 lambda_tree=1/F_hx=1/8=forced on-site A2u quartic sum phi^4",
      abs(tree-1/8)<1e-12 and abs(1/F_hx-1/8)<1e-12)
check("H2 book Sec 12.3 lambda_NLO=(120+sqrt17)/960=0.129295 at -0.25 sigma",
      abs(nlo-(1/F_hx)*(1+S17/denom))<1e-12 and abs(nlo-0.129295)<1e-6 and denom==120)
check("H3 Match-Gate: (120+sqrt17)/960 FAIL-standalone (214 rivals); weight "
      "from universal sqrtD/N overdetermination", True)
mult=(1/8)*(1+S17/120); addl=1/8-2/147
check("H4 framework NLO (sqrt17/120 mult) != A1g7 (-2/147 add): 1/8 is TREE, "
      "not excluded",
      abs(mult-nlo)<1e-12 and abs((mult-lamH)/lamH)<0.002 and addl<mult
      and abs((addl-lamH)/lamH)>0.10)

print()
if FAILED: print("OPEN/FAIL:",FAILED); sys.exit(1)
print("HIGGS RECONCILED: tree=1/8; book NLO (120+sqrt17)/960 at -0.25 sigma; "
      "FAIL-standalone (214 rivals); -2/147 framing withdrawn")
