"""Numerical check of all 25 plotted charges, from an exactly solved flux gauge."""
from pathlib import Path
import json,csv
import numpy as np
import sympy as s
p=Path(__file__).parent
cert=json.loads((p/'verification_results.json').read_text())['q6_certificate']
edges=[tuple(e) for e in cert['edges']];faces=cert['oriented_faces']
M=s.zeros(24,36)
for r,(i,j,k) in enumerate(faces):
 for u,v in [(i,j),(j,k),(k,i)]:M[r,edges.index(tuple(sorted((u,v))))]=1 if u<v else -1
seen={0};tree=[]
while len(seen)<14:
 for c,(i,j) in enumerate(edges):
  if (i in seen)!=(j in seen):tree.append(c);seen.update([i,j])
free=[c for c in range(36) if c not in tree]
N=M[:23,free];assert abs(N.det())==1
sol=N.inv()*s.ones(23,1);k=s.zeros(36,1)
for c,v in zip(free,sol):assert v.is_Integer;k[c]=v
assert M*k==s.Matrix([1]*23+[-23])
rows=[];worst=0.;spectra=[]
for q in range(25):
 A=np.zeros((14,14),complex)
 for (i,j),v in zip(edges,k):A[i,j]=np.exp(2j*np.pi*q*int(v)/24);A[j,i]=A[i,j].conjugate()
 L=np.diag([4]*6+[6]*8)-A;ev=np.linalg.eigvalsh(L);spectra.append(ev)
 expected=[72,456,3264-144*np.cos(2*np.pi*q/24)]
 errors=[abs(np.sum(ev**n)-expected[n-1]) for n in [1,2,3]]
 worst=max(worst,*errors);assert max(errors)<1e-9
 if q not in [0,24]:assert ev[0]>0
 rows.append([q,*ev])
assert max(np.max(abs(spectra[q]-spectra[24-q])) for q in range(25))<1e-12
with (p/'magnetic_sweep.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['q']+['eigenvalue_'+str(i) for i in range(1,15)]);w.writerows(rows)
print('25 charges checked numerically; all moment and conjugation tests passed. Worst moment residual:',worst)
