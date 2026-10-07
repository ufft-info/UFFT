"""Independent checks of Martin's October 2026 face-graph draft. Python + NumPy."""
from itertools import product, combinations
from fractions import Fraction as F
import json
import numpy as np
from pathlib import Path
out={}
def poly(factors):
    p=[1]
    for f,m in factors:
        for _ in range(m):
            q=[0]*(len(p)+len(f)-1)
            for i,a in enumerate(p):
                for j,b in enumerate(f):q[i+j]+=a*b
            p=q
    return p
def char(R,I=None):
    R=np.array(R,dtype=object); n=len(R)
    I=np.zeros((n,n),dtype=object) if I is None else np.array(I,dtype=object)
    X=np.eye(n,dtype=object);Y=np.zeros((n,n),dtype=object); t=[0];c=[1]
    for k in range(1,n+1):
        X,Y=X@R-Y@I,X@I+Y@R
        assert np.trace(Y)==0
        t.append(int(np.trace(X)))
        num=-sum(c[j]*t[k-j] for j in range(k));assert num%k==0;c.append(num//k)
    return c
def graph(n,edges):
    A=np.zeros((n,n),dtype=object)
    for i,j in edges:A[i,j]=A[j,i]=1
    return A
def check(name,A,factors):
    L=np.diag(np.sum(A,axis=1))-A
    p=char(L); assert p==poly(factors),name
    out[name]={'vertices':len(A),'edges':int(np.sum(A)//2),'laplacian_coefficients':p}
    return L
S=[(a,s) for a in range(3) for s in [-1,1]];H=list(product([-1,1],repeat=3))
edges=[(i,6+j) for i,(a,s) in enumerate(S) for j,h in enumerate(H) if h[a]==s]
edges += [(6+i,6+j) for i,j in combinations(range(8),2) if sum(a!=b for a,b in zip(H[i],H[j]))==1]
A=graph(14,edges);edges=[(i,j) for i,j in combinations(range(14),2) if A[i,j]]
L=check('truncated_octahedron',A,[([1,0],1),([1,-9],1),([1,-7],4),([1,-4],2),([1,-9,16],3)])
assert char(A)==poly([([1,0],2),([1,1],3),([1,3],1),([1,-3,-12],1),([1,-1,-4],3)])
tri=[t for t in combinations(range(14),3) if all(A[i,j] for i,j in combinations(t,2))]
assert len(tri)==24
cycles=sum(int((A@A)[i,j])* (int((A@A)[i,j])-1)//2 for i,j in combinations(range(14),2))//2
assert cycles==42
P=np.diag([1]*6+[0]*8).astype(object);K=P@L-L@P
assert np.array_equal(K.T,-K)
# Exact representation blocks in raw coordinate bases.
for axis in range(3):
    s=np.array([sgn if a==axis else 0 for a,sgn in S]+[0]*8,dtype=object)
    h=np.array([0]*6+[v[axis] for v in H],dtype=object)
    assert np.array_equal(L@s,4*s-h) and np.array_equal(L@h,-4*s+5*h)
    assert np.array_equal(K@K@s,-4*s) and np.array_equal(K@K@h,-4*h)
# Numerical projector weights are supplementary, not exact certificates.
e,V=np.linalg.eigh(np.array(L,dtype=float)); weights=[]
for target,m,w in [(0,1,3/7),((9-17**.5)/2,3,(1+1/17**.5)/2),(4,2,1),((9+17**.5)/2,3,(1-1/17**.5)/2),(7,4,1/7),(9,1,0)]:
    mask=abs(e-target)<1e-8; assert sum(mask)==m
    got=float(np.sum(V[:6,mask]**2)/m);assert abs(got-w)<1e-12
    weights.append([target,m,got])
out['weights']=weights
# Oriented spherical triangular faces; unnormalized radial coordinates suffice.
xyz=[tuple(s if a==k else 0 for k in range(3)) for a,s in S]+H
faces=[]
for i,j,k in tri:
    if np.linalg.det(np.array([xyz[i],xyz[j],xyz[k]],dtype=float))<0:j,k=k,j
    faces.append((i,j,k))
B=[[0]*len(edges) for _ in faces]
for r,(i,j,k) in enumerate(faces):
    for u,v in [(i,j),(j,k),(k,i)]:B[r][edges.index(tuple(sorted((u,v))))]=1 if u<v else -1
assert all(sum(row[c] for row in B)==0 for c in range(36))
seen={0};tree=[]
while len(seen)<14:
    for c,(i,j) in enumerate(edges):
        if (i in seen)!=(j in seen):tree.append(c);seen.update([i,j])
free=[c for c in range(36) if c not in tree]
M=[[F(B[r][c]) for c in free]+[F(1)] for r in range(23)]
for c in range(23):
    p=next(r for r in range(c,23) if M[r][c]);M[c],M[p]=M[p],M[c]
    d=M[c][c];M[c]=[v/d for v in M[c]]
    for r in range(23):
        if r!=c:
            d=M[r][c];M[r]=[v-d*w for v,w in zip(M[r],M[c])]
phase=[0]*36
for c,row in zip(free,M):assert row[-1].denominator==1;phase[c]=int(row[-1])%4
assert all(sum(b*p for b,p in zip(row,phase))%4==1 for row in B)
for q,mult,factors in [(6,1,[([1,-9],1),([1,-8],3),([1,-3],4),([1,-9,16],3)]),(12,2,[([1,-8],3),([1,-5],3),([1,-4],2),([1,-3],4),([1,-13,24],1)])]:
    R=np.diag(np.sum(A,axis=1));I=np.zeros((14,14),dtype=object)
    for (i,j),p in zip(edges,phase):
        re,im=[(1,0),(0,1),(-1,0),(0,-1)][(p*mult)%4]
        R[i,j]=R[j,i]=-re;I[i,j]=-im;I[j,i]=im
    got=char(R,I);assert got==poly(factors)
    out['magnetic_q'+str(q)]={'coefficients':got}
out['q6_certificate']={'vertex_order':{'squares':S,'hexagons':H},'edges':edges,'phase_exponents_mod4':phase,'oriented_faces':faces}
check('cube',graph(6,[(i,j) for i,j in combinations(range(6),2) if i//2!=j//2]),[([1,0],1),([1,-4],3),([1,-6],2)])
check('hexagonal_prism',graph(8,[(i,(i+1)%6) for i in range(6)]+[(i,j) for i in range(6) for j in [6,7]]),[([1,0],1),([1,-3],2),([1,-5],2),([1,-6],2),([1,-8],1)])
ce=[(i,j) for i,j in combinations(range(8),2) if sum(a!=b for a,b in zip(H[i],H[j]))==1]
check('rhombic_dodecahedron',graph(12,[(i,j) for i,j in combinations(range(12),2) if set(ce[i])&set(ce[j])]),[([1,0],1),([1,-2],3),([1,-4],3),([1,-6],5)])
ee=[(base+i,base+(i+1)%4) for base in [0,4,8] for i in range(4)]+[(i,base+j) for i in range(4) for base in [4,8] for j in [i,(i+1)%4]]
check('elongated_dodecahedron',graph(12,ee),[([1,0],1),([1,-2],1),([1,-10,20],2),([1,-4],2),([1,-6],3),([1,-8],1)])
out['status']='All assertions passed. Exact characteristic polynomials; numerical projector weights.'
Path(__file__).with_name('verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
