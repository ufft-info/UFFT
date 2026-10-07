"""Exact Draft 3-specific geometry, generator, and elongated-graph checks."""
from itertools import permutations,product
from fractions import Fraction
from pathlib import Path
import sympy as s,json
V=sorted({tuple(a*b for a,b in zip(p,t)) for p in permutations([0,1,2]) for t in product([-1,1],repeat=3)})
H=list(product([-1,1],repeat=3));S=[(a,t) for a in range(3) for t in [-1,1]]
for h in H:
 F=[v for v in V if sum(a*b for a,b in zip(h,v))==3]
 assert len(F)==6
 assert tuple(sum(Fraction(v[a],6) for v in F) for a in range(3))==h
 assert sum(Fraction(3,2)*a*a for a in h)==Fraction(9,2)
B=s.Matrix(6,8,lambda j,k:s.expand((H[k][(S[j][0]+1)%3]-s.I*S[j][1]*H[k][(S[j][0]+2)%3])*(1+s.I*S[j][1])/2) if H[k][S[j][0]]==S[j][1] else 0)
gens={'quarter_turn_z':s.Matrix([[0,-1,0],[1,0,0],[0,0,1]]),'third_turn_xyz':s.Matrix([[0,0,1],[1,0,0],[0,1,0]])}
out={'centroid':'h, not 3h/2','generators':{}}
for name,g in gens.items():
 P=s.zeros(8)
 for j,h in enumerate(H):P[H.index(tuple(g*s.Matrix(h))),j]=1
 R=s.expand(B*P*B.H/4)
 assert s.expand(R*B-B*P)==s.zeros(6,8)
 mapping=[]
 for j in range(6):
  dest=[i for i in range(6) if R[i,j]!=0];assert len(dest)==1
  mapping.append({'from':S[j],'to':S[dest[0]],'phase':str(R[dest[0],j])})
 out['generators'][name]=mapping
x=s.symbols('x');prodpoly=1
for z in [1,s.I,-1,-s.I]:
 inv=1/z if isinstance(z,s.Expr) else s.Rational(1,z)
 L=s.Matrix([[6-z-inv,-1-z,-1-z],[-1-inv,4-z-inv,0],[-1-inv,0,4-z-inv]])
 cp=s.factor(L.charpoly(x).as_expr());prodpoly*=cp
 out['elongated_z_'+str(z)]=str(cp)
assert s.expand(prodpoly-x*(x-2)*(x-4)**2*(x-6)**3*(x-8)*(x*x-10*x+20)**2)==0
out['status']='ALL EXACT SUPPLEMENTARY CHECKS PASSED'
Path(__file__).with_name('supplement_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
