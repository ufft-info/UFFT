"""Exact third-moment identity in Z[z]/(z^24-1); numerical cross-checks.
The proof that cos(pi*q/12) is strictly decreasing for q=0,...,12 is
analytic and given in the accompanying report, not inferred from floats.
"""
from pathlib import Path
import json
import sympy as s
import numpy as np
p=Path(__file__).resolve().parent
cert=json.loads((p/'verification_results.json').read_text())['q6_certificate']
edges=[tuple(e) for e in cert['edges']];faces=cert['oriented_faces']
M=s.zeros(24,36)
for r,(i,j,k) in enumerate(faces):
 for u,v in [(i,j),(j,k),(k,i)]: M[r,edges.index(tuple(sorted((u,v))))]=1 if u<v else -1
seen={0};tree=[]
while len(seen)<14:
 for c,(i,j) in enumerate(edges):
  if (i in seen)!=(j in seen):tree.append(c);seen.update([i,j])
free=[c for c in range(36) if c not in tree]
N=M[:23,free];assert abs(N.det())==1
sol=N.inv()*s.ones(23,1);k=s.zeros(36,1)
for c,v in zip(free,sol):assert v.is_Integer;k[c]=v
assert M*k==s.Matrix([1]*23+[-23])
exponents={}
for (u,v),n in zip(edges,k):exponents[u,v]=int(n)%24;exponents[v,u]=-int(n)%24
# Every length-three closed walk, counted with its starting point and orientation.
coeff=[0]*24
for i in range(14):
 for j in range(14):
  for l in range(14):
   if (i,j) in exponents and (j,l) in exponents and (l,i) in exponents:
    coeff[(exponents[i,j]+exponents[j,l]+exponents[l,i])%24]+=1
assert coeff==[0,72]+[0]*21+[72]
deg=[sum(i==u for u,v in exponents) for i in range(14)]
assert deg==[4]*6+[6]*8
assert sum(deg)==72
assert sum(d*d+d for d in deg)==456
constant=sum(d**3+3*d*d for d in deg);assert constant==3264
spectra=np.loadtxt(p/'magnetic_sweep.csv',delimiter=',',skiprows=1)[:,1:]
residuals=[]
for q,ev in enumerate(spectra):
 expected=[72,456,3264-144*np.cos(np.pi*q/12)]
 residuals.extend(abs(np.sum(ev**n)-expected[n-1]) for n in [1,2,3])
assert max(residuals)<1e-9
out={'exact_trace_A3_coefficients_mod_z24_minus_1':coeff,
 'exact_trace_L3':'3264 - 72*(z + z^23), z^24=1',
 'distinct_spectra':'exactly 13, by strict monotonicity of cosine on [0,pi]',
 'isospectral_classification':'q and p are isospectral iff q = p or -p modulo 24',
 'max_numeric_moment_residual':float(max(residuals)),
 'status':'ALL MOMENT CHECKS PASSED'}
(p/'moment_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
