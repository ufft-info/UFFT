"""Validate the copied author JSON certificate exactly, independently of author code."""
from pathlib import Path
import json,sympy as s
p=Path(__file__).parent/'author_evidence'
c=json.loads((p/'flux_gauge_certificate.json').read_text())
V=[s.Matrix(v) for v in c['vertex_order']];F=c['faces'];edges=[tuple(e) for e in c['edges']]
assert len(V)==24 and len(F)==14 and len(edges)==36
assert set(edges)=={(i,j) for i in range(14) for j in range(i+1,14) if len(set(F[i])&set(F[j]))==2}
cent=[sum((V[j] for j in f),s.zeros(3,1))/len(f) for f in F]
for key,unit in [('phase_exponents_mod4_q6',s.I),('phase_exponents_mod2_q12',-1)]:
 A=s.zeros(14)
 for (i,j),k in zip(edges,c[key]):A[i,j]=unit**k;A[j,i]=s.conjugate(unit**k)
 for face in c['oriented_plaquettes']:
  i,j,k=face
  assert s.Matrix.hstack(cent[i],cent[j],cent[k]).det()>0
  assert s.expand(A[i,j]*A[j,k]*A[k,i])==unit
print('Author certificate independently checked exactly: graph, outward orientations, q6 and q12 holonomies.')
