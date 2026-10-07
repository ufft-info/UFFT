"""Exact quarter-flux block proof and magnetic symmetry; requires SymPy and NumPy.
All mathematical matrix assertions use SymPy exact arithmetic.
Run verify_baseline.py separately for the original spectrum/table checks.
"""
from itertools import product, combinations, permutations
from pathlib import Path
import json, sympy as s
H=list(product([-1,1],repeat=3));S=[(a,t) for a in range(3) for t in [-1,1]]
I=s.I
C=s.Matrix(8,8,lambda j,k:int(sum(a!=b for a,b in zip(H[j],H[k]))==1))
B0=s.Matrix(6,8,lambda j,k:int(H[k][S[j][0]]==S[j][1]))
def entry(j,k):
 a,t=S[j]; h=H[k];b=(a+1)%3;c=(a+2)%3
 return s.expand((h[b]-I*t*h[c])*(1+I*t)/2) if h[a]==t else 0
B=s.Matrix(6,8,entry)
assert all(z in [0,1,-1,I,-I] for z in B)
assert B.H*B==(9*s.eye(8)-C*C)/2
assert B*B.H==4*s.eye(6)
assert B0.H*B0==(C+s.eye(8))*(C+3*s.eye(8))/2
A=s.zeros(14);A[:6,6:]=B;A[6:,:6]=B.H;A[6:,6:]=C
D=s.diag(*([4]*6+[6]*8));L=D-A
A0=s.zeros(14);A0[:6,6:]=B0;A0[6:,:6]=B0.T;A0[6:,6:]=C;L0=D-A0
xyz=[tuple(t if a==k else 0 for k in range(3)) for a,t in S]+H
faces=[]
for i,j,k in combinations(range(14),3):
 if A[i,j] and A[j,k] and A[k,i]:
  if s.Matrix([xyz[i],xyz[j],xyz[k]]).det()<0:j,k=k,j
  assert s.expand(A[i,j]*A[j,k]*A[k,i])==I
  faces.append((i,j,k))
assert len(faces)==24
W={k:s.Matrix(8,0,[]) for k in range(4)}
for k in range(4):
 W[k]=s.Matrix.hstack(*[s.Matrix([s.prod(h[a] for a in J) for h in H]) for J in combinations(range(3),k)])
 assert C*W[k]==(3-2*k)*W[k]
 assert s.expand((B*W[k]).H*(B*W[k]))==(32*s.eye(W[k].cols) if k in [1,2] else s.zeros(W[k].cols))
for k in [1,2]:
 # Unnormalized columns X=B h and Y=h. Exact block: [[4,-1],[-4,3+2k]].
 X=s.expand(B*W[k]).col_join(s.zeros(8,3)); Y=s.zeros(6,3).col_join(W[k])
 assert s.expand(L*X-4*X+4*Y)==s.zeros(14,3) and s.expand(L*Y+X-(3+2*k)*Y)==s.zeros(14,3)
# Six-dimensional explicit unitary intertwiner in normalized bases, verified via raw bases.
X0=(B0*W[1]).col_join(s.zeros(8,3));X=s.expand(B*W[1]).col_join(s.zeros(8,3));Y=s.zeros(6,3).col_join(W[1])
F=s.diag(*([0]*14));F[:6,:6]=B*B0.T/4;F[6:,6:]=W[1]*W[1].T/8
E0=X0.row_join(Y);E=X.row_join(Y)
assert s.expand(F*E0-E)==s.zeros(14,6) and s.expand(E0.H*E0-E.H*E)==s.zeros(6) and s.expand((L*F-F*L0)*E0)==s.zeros(14,6)
x=s.symbols('x');a,b=s.symbols('a b',real=True)
f1=x*x-(7*a+2*b)*x+8*a*(a+b);f2=x*x-(7*a+4*b)*x+8*a*(a+2*b)
cp6=(x-9)*(x-8)**3*(x-3)**4*(x*x-9*x+16)**3
assert s.expand(L.charpoly(x).as_expr()-cp6)==0
# Exact proper rotations and a genuine monomial magnetic representation.
reps=[];perms=[]
for p in permutations(range(3)):
 for t in product([-1,1],repeat=3):
  g=s.zeros(3)
  for k in range(3):g[k,p[k]]=t[k]
  if g.det()!=1:continue
  dest=[H.index(tuple(g*s.Matrix(h))) for h in H]
  P=s.zeros(8)
  for j,k in enumerate(dest):P[k,j]=1
  R=s.expand(B*P*B.H/4)
  assert R.H*R==s.eye(6) and R*B==B*P
  assert all(sum(R[j,k]!=0 for k in range(6))==1 for j in range(6))
  P0=s.zeros(6)
  for j,(axis,sgn) in enumerate(S):
   v=s.zeros(3,1);v[axis]=sgn;v=g*v
   axis2=next(k for k in range(3) if v[k]);sgn2=int(v[axis2]);jj=S.index((axis2,sgn2));P0[jj,j]=1
   assert R[jj,j]!=0
  U=s.diag(R,P);assert U*L==L*U
  assert s.expand((U*F-F*s.diag(P0,P))*E0)==s.zeros(14,6)
  reps.append(R);perms.append(P)
assert len(reps)==24
for i in range(24):
 for j in range(24):
  k=next(k for k in range(24) if perms[k]==perms[i]*perms[j])
  assert reps[i]*reps[j]==reps[k]
# Exact weighted identities on both 3-dimensional cube sectors.
Da=s.diag(*([4*a]*6+[3*a+3*b]*8));Aa=s.zeros(14);Aa[:6,6:]=a*B;Aa[6:,:6]=a*B.H;Aa[6:,6:]=b*C;La=Da-Aa
for k in [1,2]:
 X=s.expand(B*W[k]).col_join(s.zeros(8,3));Y=s.zeros(6,3).col_join(W[k])
 assert s.expand(La*X-4*a*X+4*a*Y)==s.zeros(14,3) and s.expand(La*Y+a*X-(3*a+2*k*b)*Y)==s.zeros(14,3)
out={'status':'ALL EXACT ASSERTIONS PASSED','B_real':s.re(B).tolist(),'B_imag':s.im(B).tolist(),'square_order':S,'hexagon_order':H,'faces':faces,'q6_charpoly':str(s.factor(cp6)),'gram_identity':'B^*B=(9I-C^2)/2; BB^*=4I','proper_rotations_verified':24,'group_products_verified':576,'weighted_q6_charpoly':str((x-3*a)*(x-3*a-6*b)*f1**3*f2**3)}
Path(__file__).with_name('deeper_results.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(out['status']);print(out['gram_identity']);print('24 proper rotations and 576 group products checked exactly; explicit intertwiner checked.')
