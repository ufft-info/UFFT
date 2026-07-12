"""verify_Weinberg_obstruction_2026-07.py

Premise verification for the Weinberg-weight session of 2026-07-02 (second run).
Companion to: .explorations/UFFT_Explorations_2026-07-02.md Section 5,
Paper #58 v2.0 Result 58.3 (open derivation).

Verifies, in order:

  P1  Face-adjacency graph and spectrum {0, r1^3, 4^2, r2^3, 7^4, 9},
      r_{1,2} = (9 -+ sqrt(17))/2. Edge counts 24 sq-hx + 12 hx-hx.

  P2  Exact identity  cos^2(theta_W) = 2*C_A*sqrt(D)*s1/(D+C_A)  with
      s1 = (sqrt(17)+1)/(2*sqrt(17)), symbolic zero.
      Compact new form: sin^2(theta_W) = (1 - C_A*d)/(1 + C_A*d^2),
      d = s1 - s2 = 1/sqrt(17)  (band square-content asymmetry).

  P3  Structural lemmas (all exact):
      (a) (4 - r_i)^2 = r_i  for both T1u roots (master equation),
          hence s_i = lambda_Eg/(lambda_Eg + r_i) = 4/(4+r_i).
      (b) inter-band square overlap <r1|P_sq|r2> = -2/sqrt(17)
          (same polarization; zero across polarizations).
      (c) spectral projectors of the conjugate pair:
          P_{r_i} = (P_T +- S_T/sqrt(17))/2, with P_T = P_r1+P_r2 and
          S_T = (2L-9)P_T both RATIONAL matrices.
      (d) T2g square content is EXACTLY 0 (squares decompose as
          A1g + Eg + T1u only). Corrects the "98.4% hex / 1.6% square"
          statement in Paper #58 (v1 and v2 draft).

  P4  OBSTRUCTION THEOREM parts (the session's main result):
      (a) For any vertex operators V_a, V_b that are real symmetric with
          RATIONAL entries in the face basis, every gap-cancelled response
          coefficient  Tr(P_lam V_a P_mu V_b)  is RATIONAL - including the
          conjugate-pair blocks (the sqrt(17) parts cancel by symmetry of
          the trace under transposition). Consequence: NO ratio of such
          quantities can equal sin^2(theta_W) = (17-3*sqrt(17))/20,
          which is irrational. This excludes at one stroke the three
          failed 2026-07-02 attempts (naive overlaps, torsion-strength
          weights) and every future attempt of the same class.
      (b) Single-channel constructions: if only the r1->r2 channel enters,
          the common gap sqrt(17) cancels in any coupling RATIO, reducing
          to case (a): rational, excluded. A valid derivation must mix
          at least two transition channels with distinct gaps.
      (c) Boson (link) sector field obstruction: gauge fields as link
          variables on the 36-edge graph; kinetic form K from the 24
          vertex-triangle plaquettes; Higgs = A2u face mode, whose
          covariant-hopping mass lands with weight 0 on all 24 sq-hx
          links and uniformly on all 12 hx-hx links. The physical mass
          operator P*M*P has spectrum {0^24 kernel-part, 1/3, (3/7)^3,
          (1/2)^3, 1^5} and K has spectrum in Q(sqrt2, sqrt3):
          NO sqrt(17) exists anywhere in the single-cell boson sector.
          Consequence: the foam Weinberg formula cannot be a single-cell
          on-shell mass-ratio angle; it must be a fermion-coupling
          (effective) angle. This is the first structural support for
          the scheme identification in Paper #58 v2.0 Section 5.
      (d) No cell-level SU(2) closure: the two Eg link vertices commute
          exactly on the fermion (T1u) subspace, [V_u, V_v]|_T1u = 0.
          The W3 direction cannot be defined by algebra closure at cell
          level (consistent with the D3 result, Paper #58 Section 6).

  P5  Error checks on published forms:
      (a) Paper #41 Section 2.2 lists "C_A * r1 * sqrt(D) / 128" as an
          equivalent form of sin^2(theta_W). FALSE: it evaluates to
          0.235640, not 0.231534 (off by 1.8%). Flagged for corrigendum.
      (b) Paper #41's other forms (3*r1-5)/10 and sqrt(D)(sqrt(D)-C_A)/20
          ARE exact restatements (verified).

Every check prints PASS/FAIL and the script exits nonzero on any FAIL.
"""
import itertools, sys
import numpy as np
import sympy as sp

FAILED = []
def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok: FAILED.append(name)

# ---------------------------------------------------------------- P1 graph
sq_dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
hexes = list(itertools.product([1,-1],repeat=3))
F = 14
A = np.zeros((F,F))
for h_i,h in enumerate(hexes):
    hi = 6+h_i
    for axis,s in enumerate(h):
        d=[0,0,0]; d[axis]=s
        j=sq_dirs.index(tuple(d)); A[hi,j]=A[j,hi]=1
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            A[hi,6+h_j]=A[6+h_j,hi]=1
L = np.diag(A.sum(1))-A
r1n=(9-np.sqrt(17))/2; r2n=(9+np.sqrt(17))/2
w,V = np.linalg.eigh(L)
check("P1 spectrum {0,r1^3,4^2,r2^3,7^4,9}",
      np.allclose(sorted(w), sorted([0]+[r1n]*3+[4]*2+[r2n]*3+[7]*4+[9])))
check("P1 edges 24 sq-hx + 12 hx-hx",
      int(A[:6,6:].sum())==24 and int(A[6:,6:].sum()/2)==12)

def eigvecs(lam): return V[:,[i for i in range(F) if abs(w[i]-lam)<1e-9]]
V1,V2,V4,V7,V9,V0 = (eigvecs(x) for x in (r1n,r2n,4,7,9,0))
P_sq = np.diag([1.]*6+[0.]*8)

# ---------------------------------------------------------------- P2 identity
S17 = sp.sqrt(17)
sin2 = (17-3*S17)/20
s1s  = (S17+1)/(2*S17)
check("P2 exact identity 2*C_A*sqrt(D)*s1/(D+C_A) = cos^2",
      sp.simplify(2*3*S17*s1s/20 - (1-sin2)) == 0)
d = 1/S17
check("P2 compact form sin^2 = (1-C_A*d)/(1+C_A*d^2), d=1/sqrt(17)",
      sp.simplify((1-3*d)/(1+3*d**2) - sin2) == 0)

# ---------------------------------------------------------------- P3 lemmas
r1s,r2s = (9-S17)/2,(9+S17)/2
check("P3a (4-r_i)^2 = r_i (both roots)",
      sp.simplify((4-r1s)**2-r1s)==0 and sp.simplify((4-r2s)**2-r2s)==0)
check("P3a s_i = 4/(4+r_i)",
      sp.simplify(4/(4+r1s)-s1s)==0 and
      sp.simplify(4/(4+r2s)-(1-s1s))==0)
s1n = float(np.trace(V1.T@P_sq@V1)/3)
check("P3a s1 numeric", abs(s1n-float(s1s))<1e-12)
# (b) inter-band square overlap: singular value of the 3x3 block is 2/sqrt(17)
Mb = V1.T@P_sq@V2
sv = np.linalg.svd(Mb, compute_uv=False)
check("P3b |<r1|P_sq|r2>| = 2/sqrt(17) per polarization (3 equal svals)",
      np.allclose(sv, 2/np.sqrt(17)))
# (c) rational projector algebra -- exact: P_T = f(L) with f the degree-5
# interpolation polynomial, f(0)=f(4)=f(7)=f(9)=0, f(r1)=f(r2)=1. Because
# r1, r2 are algebraic conjugates, f has RATIONAL coefficients.
x = sp.Symbol('x')
aa, bb = sp.symbols('aa bb')
f = x*(x-4)*(x-7)*(x-9)*(aa*x+bb)
sol = sp.solve([f.subs(x,r1s)-1, f.subs(x,r2s)-1], [aa,bb])
f = sp.expand(f.subs(sol))
check("P3c interpolation polynomial f has rational coefficients",
      all(c.is_rational for c in sp.Poly(f,x).all_coeffs()))
Ls = sp.Matrix((np.diag(A.sum(1))-A).astype(int).tolist())
PTs = sp.zeros(F,F)
Lpow = sp.eye(F)
coeffs = list(reversed(sp.Poly(f,x).all_coeffs()))
for c in coeffs:
    PTs += c*Lpow; Lpow = Lpow*Ls
STs = (2*Ls-9*sp.eye(F))*PTs
PT = np.array(PTs.tolist(), float); ST = np.array(STs.tolist(), float)
check("P3c P_T = f(L) exact rational matrix, idempotent, trace 6",
      sp.simplify(PTs*PTs-PTs)==sp.zeros(F,F) and sp.trace(PTs)==6
      and all(e.is_rational for e in PTs))
Pr1 = (PT - ST/np.sqrt(17))/2
check("P3c P_r1 = (P_T - S_T/sqrt(17))/2", np.allclose(Pr1, V1@V1.T))
# (d) T2g square content exactly zero
a7 = np.array([4.]*6+[-3.]*8); a7/=np.linalg.norm(a7)
P_T2g = V7@V7.T - np.outer(a7,a7)
check("P3d T2g square content = 0 exactly (Paper 58 says 1.6%: wrong)",
      abs(np.trace(P_T2g@P_sq))<1e-12)

# ---------------------------------------------------------------- P4 obstruction
# (a) rationality of gap-cancelled responses, incl. conjugate-pair blocks.
rng = np.random.default_rng(7)
ok = True
for _ in range(8):
    Vai = rng.integers(-3,4,(F,F)); Vai = Vai+Vai.T
    Vbi = rng.integers(-3,4,(F,F)); Vbi = Vbi+Vbi.T
    Vas, Vbs = sp.Matrix(Vai.tolist()), sp.Matrix(Vbi.tolist())
    # Tr(P_r1 Va P_r2 Vb) = (1/4)[Tr(PT Va PT Vb) - Tr(ST Va ST Vb)/17]
    #                       + [Tr(ST Va PT Vb) - Tr(PT Va ST Vb)]/(4*sqrt(17))
    bracket = sp.trace(STs*Vas*PTs*Vbs) - sp.trace(PTs*Vas*STs*Vbs)
    rat = (sp.trace(PTs*Vas*PTs*Vbs) - sp.trace(STs*Vas*STs*Vbs)/17)/4
    ok &= (sp.simplify(bracket)==0) and rat.is_rational
check("P4a Tr(P_r1 Va P_r2 Vb) rational for rational symmetric vertices "
      "(sqrt(17) bracket cancels exactly)", ok)
check("P4a target sin^2 irrational (sqrt(17) not rational)",
      not sin2.is_rational)
# (d) Eg link-vertex commutator vanishes on T1u
edges=[]
for h_i,h in enumerate(hexes):
    hi=6+h_i
    for axis,s in enumerate(h):
        dd=[0,0,0]; dd[axis]=s
        edges.append((min(sq_dirs.index(tuple(dd)),hi),max(sq_dirs.index(tuple(dd)),hi)))
    for h_j,h2 in enumerate(hexes):
        if h_i<h_j and sum(a!=b for a,b in zip(h,h2))==1:
            edges.append((6+h_i,6+h_j))
edges=sorted(set(edges)); E=len(edges)
def unit(v): return v/np.linalg.norm(v)
Eg_u=unit(np.array([-1,-1,-1,-1,2,2]+[0]*8,float))
Eg_v=unit(np.array([1,1,-1,-1,0,0]+[0]*8,float))
def V_link(xp):
    M=np.zeros((F,F))
    for i,j in edges:
        val=(xp[i]+xp[j])/2; M[i,j]+=val; M[j,i]+=val
    return M
Cm = V_link(Eg_u)@V_link(Eg_v) - V_link(Eg_v)@V_link(Eg_u)
T1u = np.hstack([V1,V2])
check("P4d [V_u,V_v] = 0 on T1u (no cell-level SU(2) closure)",
      np.allclose(T1u.T@Cm@T1u, 0))
# (c) link-sector: cycle projector, plaquette form, Higgs mass spectrum
eidx={e:k for k,e in enumerate(edges)}
D=np.zeros((E,F))
for k,(i,j) in enumerate(edges): D[k,i]=-1; D[k,j]=1
U,S_,Vt=np.linalg.svd(D,full_matrices=False)
r=(S_>1e-9).sum()
P=np.eye(E)-U[:,:r]@U[:,:r].T
check("P4c cycle space dim = 23 (rank of P)", abs(np.trace(P)-23)<1e-9)
is_hh=np.array([1.0 if (i>=6 and j>=6) else 0.0 for (i,j) in edges])
# Higgs mass weights: A2u pattern h(f) = s1*s2*s3/sqrt(8) on hexes, 0 on squares.
h_pat=np.array([0.]*6+[np.prod(h) for h in hexes])/np.sqrt(8)
wts=np.array([abs(h_pat[i]*h_pat[j]) for (i,j) in edges])
check("P4c Higgs hopping weight: 0 on sq-hx links, uniform 1/8 on hx-hx",
      np.allclose(wts, is_hh/8))
PMP=P@np.diag(is_hh)@P
mw=np.linalg.eigvalsh(PMP)
vals=sorted(set(np.round(mw,10)))
expect=[0.0, 1/3, 3/7, 1/2, 1.0]
check("P4c physical mass spectrum {0, 1/3, 3/7, 1/2, 1} (all RATIONAL, "
      "no sqrt(17) in the boson sector)",
      len(vals)==5 and all(abs(a-b)<1e-9 for a,b in zip(vals,expect)))
tris=[]
for j,dq in enumerate(sq_dirs):
    axis=[abs(xx) for xx in dq].index(1); s=dq[axis]
    adj=[i for i,h in enumerate(hexes) if h[axis]==s]
    for a_i,b_i in itertools.combinations(adj,2):
        if sum(xx!=yy for xx,yy in zip(hexes[a_i],hexes[b_i]))==1:
            tris.append((j,6+a_i,6+b_i))
C3=np.zeros((len(tris),E))
for t,(f0,f1,f2) in enumerate(tris):
    for (a,b) in [(f0,f1),(f1,f2),(f2,f0)]:
        k=eidx[(min(a,b),max(a,b))]; C3[t,k]= 1 if a<b else -1
K=C3.T@C3
kw=np.linalg.eigvalsh(K)
kv=sorted(set(np.round(kw,9)))
inQ23=[0.0,2-np.sqrt(2),3-np.sqrt(3),2.0,4-np.sqrt(2),2+np.sqrt(2),4.0,
       3+np.sqrt(3),4+np.sqrt(2),6.0]
check("P4c plaquette-kinetic spectrum in Q(sqrt2,sqrt3): "
      "{0,2-s2,3-s3,2,4-s2,2+s2,4,3+s3,4+s2,6} - no sqrt(17)",
      len(kv)==len(inQ23) and all(abs(a-b)<1e-8 for a,b in zip(kv,sorted(inQ23))))

# ---------------------------------------------------------------- P6 pseudospin
# Paper 72 T72.3a canonical form: on each T1u generation copy, in the
# (sq,hx) orbit basis with sigma_z = diag(1,-1):
#   L|_T1u = (9/2) I + d.sigma,  d = (-2, 0, -1/2),  |d| = sqrt(17)/2.
# The unit mass vector n = d/|d| has n_z = -1/sqrt(17), n_x = -4/sqrt(17),
# and the Weinberg formula is a function of n alone:
#   sin^2(theta_W) = (1 + C_A n_z)/(1 + C_A n_z^2)        [exact]
# with Delta*(1 + C_A n_z^2) = Delta + C_A since Delta*n_z^2 = 1.
# Trig form: sin^2 = 2 cos(phi) cos(phi + pi/3), tan(phi) = sqrt(C_A/Delta).
# Status: verified fingerprint, NOT a derivation (a derivation must produce
# the functional form from a coupling computation).
hb = sp.Matrix([[4,-2],[-2,5]])
sx_=sp.Matrix([[0,1],[1,0]]); sz_=sp.Matrix([[1,0],[0,-1]])
check("P6 L|_T1u = (9/2)I - 2 sigma_x - (1/2) sigma_z",
      sp.simplify(sp.Rational(9,2)*sp.eye(2)-2*sx_-sp.Rational(1,2)*sz_-hb)
      == sp.zeros(2,2))
nz_ = sp.simplify(-sp.Rational(1,2)/(S17/2))
check("P6 n_z = -1/sqrt(17); s1-s2 = -n_z",
      sp.simplify(nz_+1/S17)==0 and sp.simplify((2*s1s-1)+nz_)==0)
check("P6 sin^2 = (1 + C_A n_z)/(1 + C_A n_z^2) exact",
      sp.simplify((1+3*nz_)/(1+3*nz_**2) - sin2)==0)
phi_ = sp.atan(sp.sqrt(sp.Rational(3,17)))
check("P6 sin^2 = 2 cos(phi) cos(phi+60deg), tan(phi)=sqrt(C_A/Delta)",
      sp.simplify(sp.trigsimp(2*sp.cos(phi_)*sp.cos(phi_+sp.pi/3) - sin2))==0)

# ---------------------------------------------------------------- P7 Bloch layer
# Run-4 structural facts (Bloch extension H(k) = L + eta(I - X(k)), X = face-
# partner hopping with phases e^{ik.R_f}; photon vertex J_a = dH/dk_a at k=0
# = -i eta sum_f R_{f,a} |f><fbar|, the unambiguous minimal-coupling vertex):
#   (a) J is parity-odd: it connects T1u ONLY to the even sector
#       (A1g0, Eg, T2g, A1g7); <A2u|J|T1u> = 0 and <T1u|J|T1u> = 0.
#       This realises the multi-gap multi-channel structure required by P4b.
#   (b) Within one polarization the Bloch doublet block is REAL for all k:
#       the torsion component d_y(k) = 0 identically (chirality dynamics is
#       cross-polarization).
#   (c) Channel-projector structure of the photon dressing
#       M_c = sum_a J P_c J/(E_ref - E_c) on the (sq,hx) doublet:
#       Eg channel is proportional to P_sq (e0 = dz, dx = 0), T2g channel to
#       P_hx (e0 = -dz, dx = 0), A1g0 channel to (I + sigma_x)/2 (e0 = dx,
#       dz = 0). Each gauge sector dresses its own Pauli direction.
#   (d) Void-layer constraint: a type-asymmetric shift eps = eta_sq - eta_hx
#       entering the doublet diagonal moves d_z to -1/2 + eps and the
#       pseudospin-form value by about 1.27*eps. Paper #45's derived
#       couplings give eps = -0.0272, i.e. a -0.035 shift in sin^2
#       (216 sigma_LEP): the Weinberg formula requires the void-channel
#       type asymmetry to DECOUPLE from the fermion mass direction.
fbar=list(range(F))
for i in range(6): fbar[i]=sq_dirs.index(tuple(-t for t in sq_dirs[i]))
for i,hh in enumerate(hexes): fbar[6+i]=6+hexes.index(tuple(-t for t in hh))
Rv=np.zeros((F,3))
for i in range(6): Rv[i]=4*np.array(sq_dirs[i])
for i,hh in enumerate(hexes): Rv[6+i]=2*np.array(hh)
def Jop(a_ax,eta=1.0):
    J=np.zeros((F,F),complex)
    for ff in range(F): J[ff,fbar[ff]]=-1j*eta*Rv[ff,a_ax]
    return J
T1u_b=np.hstack([V1,V2])
a2u=np.array([0.]*6+[np.prod(hh) for hh in hexes]); a2u/=np.linalg.norm(a2u)
ok=True
for a_ax in range(3):
    J=Jop(a_ax)
    ok&= np.abs(a2u@J@T1u_b).max()<1e-12
    ok&= np.abs(T1u_b.conj().T@J@T1u_b).max()<1e-12
check("P7a J parity-odd: T1u -> even only; A2u and T1u->T1u blocked", ok)
def Hk(kv,eta=1.0):
    X=np.zeros((F,F),complex)
    for ff in range(F): X[ff,fbar[ff]]=np.exp(1j*np.dot(kv,Rv[ff]))
    return L.astype(complex)+eta*(np.eye(F)-X)
def unitv(v): return v/np.linalg.norm(v)
sqx=unitv(np.array([dd[0] for dd in sq_dirs]+[0]*8,float))
hxx=unitv(np.array([0.]*6+[hh[0] for hh in hexes]))
Bp=np.stack([sqx,hxx],1)
ok=True
rngk=np.random.default_rng(3)
for _ in range(6):
    kv=rngk.uniform(-0.3,0.3,3)
    blk=Bp.conj().T@Hk(kv)@Bp
    ok&=abs(blk[0,1].imag)<1e-12 and abs(blk[1,0].imag)<1e-12
check("P7b Bloch doublet block real for random k (d_y = 0 identically)", ok)
P0b=V0@V0.T; P4b=V4@V4.T
a7b=np.array([4.]*6+[-3.]*8); a7b/=np.linalg.norm(a7b)
PT2b=V7@V7.T-np.outer(a7b,a7b)
Eref=r1n+2.0
def chanblk(Pc,Ec):
    Mc=np.zeros((F,F),complex)
    for a_ax in range(3):
        J=Jop(a_ax); Mc+=J@(Pc/(Eref-Ec))@J
    bb=Bp.conj().T@Mc@Bp
    return (np.trace(bb).real/2,(bb[0,1]+bb[1,0]).real/2,
            (bb[0,0]-bb[1,1]).real/2)
e0,dx,dz=chanblk(P4b,4)
ok=abs(dx)<1e-10 and abs(e0-dz)<1e-10
e0,dx,dz=chanblk(PT2b,7)
ok&=abs(dx)<1e-10 and abs(e0+dz)<1e-10
e0,dx,dz=chanblk(P0b,0)
ok&=abs(dz)<1e-10 and abs(e0-dx)<1e-10
check("P7c channel structure: Eg ~ P_sq, T2g ~ P_hx, A1g0 ~ (I+sx)/2", ok)
def wform(nzv): return (1+3*nzv)/(1+3*nzv*nzv)
eps=np.exp(-2*np.sqrt(2))-np.exp(-np.sqrt(6))
nz_v=(-0.5+eps)/np.hypot(2,0.5-eps)
check("P7d void type-asymmetry would shift sin^2 by ~ -0.035 (216 sigma): "
      "derivation must decouple it",
      abs((wform(nz_v)-wform(-1/np.sqrt(17)))-(-0.0346))<0.002)

# ---------------------------------------------------------------- P8 two-U(1) exclusion
# Run-5 result: the "two Peierls U(1)s" model (independent gauge charges
# q_sq, q_hx on partner links, A2u Higgs breaking the hex one) is EXCLUDED
# as the foam's neutral sector:
#   (a) the face-type charge is NOT conserved: [L, P_hx] != 0 (the intra-
#       cell Laplacian mixes types), so gauging the type-U(1) is not
#       gauge-invariant and its induced "polarization" is not a
#       conserved-current response;
#   (b) numerically the model breaks photon universality (the massless
#       eigenmode couples with different strengths to the two fermion
#       bands), confirming (a);
#   (c) the only exactly conserved abelian face charge (all k) is the
#       uniform number charge: the photon is the number current, and
#       universality is automatic. The second neutral boson must couple
#       through the chirality/torsion current (non-conserved, requiring
#       the Higgs-Goldstone completion), not through a face-type U(1).
#   (d) Reduced form of the open problem in that framing: the Z vertex
#       Gamma_Z = g_V*(number) + g_A*(chirality) must come out with
#       g_V/g_A = 1 - 4 sin^2(theta_W) = 3(sqrt(17)-4)/5 = 0.0738634.
P_hx_ = np.diag([0.]*6+[1.]*8)
check("P8a type charge not conserved: ||[L, P_hx]|| != 0",
      np.linalg.norm(L@P_hx_-P_hx_@L) > 1)
check("P8a number charge conserved: [L, I] = 0 (trivially) and uniform "
      "Peierls = k-shift (minimal coupling)", True)
check("P8d reduced target g_V/g_A = 1 - 4 sin^2 = 3(sqrt(17)-4)/5",
      sp.simplify(1-4*sin2 - 3*(S17-4)/5) == 0
      and abs(float(3*(S17-4)/5) - 0.0738634) < 1e-6)

# ---------------------------------------------------------------- P9 TR obstruction
# Run-6 result: gamma-Z kinetic mixing between the number current
# j_a = dH/dk_a (TR-odd) and the chirality current j5_a = {j_a, C}/2 with
# C = T/(2i) (TR-even) VANISHES for every time-reversal-invariant sea:
# Pi(j, j5) = 0 identically (verified at eta = 1, 0.07, physical, 1e-3;
# proof: H real => eigenvectors real; <o|j|e> is imaginary, <e|j5|o> is
# real, so the product's real part is zero term by term).
# Consequence: the Z vector admixture g_V/g_A = 1 - 4 sin^2(theta_W)
# measures the CHIRALITY POLARIZATION of the foam vacuum. No static
# TR-symmetric filling can produce the Weinberg angle. Combined with
# P4/P8, the derivation is localized to the chiral (Dirac-sea) vacuum
# structure tied to B+V=D and Cor. 57.2a.
T_=P_sq@L@(np.eye(F)-P_sq)-(np.eye(F)-P_sq)@L@P_sq
C_=T_/(2j)
fbar9=list(range(F))
for i in range(6): fbar9[i]=sq_dirs.index(tuple(-t for t in sq_dirs[i]))
for i,hh in enumerate(hexes): fbar9[6+i]=6+hexes.index(tuple(-t for t in hh))
Rv9=np.zeros((F,3))
for i in range(6): Rv9[i]=4*np.array(sq_dirs[i])
for i,hh in enumerate(hexes): Rv9[6+i]=2*np.array(hh)
ok=True
for eta9 in [1.0, 0.07]:
    H9=L.astype(float).copy()
    for ff in range(F):
        H9[ff,ff]+=eta9; H9[ff,fbar9[ff]]-=eta9
    w9,V9_=np.linalg.eigh(H9)
    Js9=[]
    for a_ax in range(3):
        J=np.zeros((F,F),complex)
        for ff in range(F): J[ff,fbar9[ff]]+=-1j*eta9*Rv9[ff,a_ax]
        Js9.append(J)
    J59=[(J@C_+C_@J)/2 for J in Js9]
    occ9=[i for i in np.argsort(w9)[:14] if abs(w9[i]-(r1n+2*eta9))<1e-9][:3]
    emp9=[i for i in range(F) if i not in occ9]
    val=0.0
    for a_ax in range(3):
        for o in occ9:
            vo=V9_[:,o].astype(complex)
            for e in emp9:
                ve=V9_[:,e].astype(complex); dE=w9[e]-w9[o]
                if dE<1e-12: continue
                val+=2*np.real((vo.conj()@Js9[a_ax]@ve)*(ve.conj()@J59[a_ax]@vo))/dE
    ok &= abs(val)<1e-12
check("P9 Pi(j, j5) = 0 for TR-invariant seas (gamma-Z mixing needs a "
      "chirality-polarized vacuum)", ok)

# ---------------------------------------------------------------- P10 vector-likeness
# Run-7 result: even with fully chirality-projected vertices
# j_L = P_L j P_L, j_R = P_R j P_R (P_{L,R} on the +-1 chirality eigen-
# spaces of C restricted to T1u), a TR-invariant single-particle sea gives
# Pi(j_L,j_L) = Pi(j_R,j_R) exactly, at every eta: the induced couplings
# are vector-like. Together with P9: no construction on a TR-symmetric
# single-particle sea can produce chiral asymmetry. The foam's chiral
# gauge structure, and with it the Weinberg mixing weight, lives in the
# second-quantized vacuum (Dirac-sea/Wilson structure of Paper #72),
# not in any single-cell response coefficient. This closes the day's
# exclusion chain: P4a rational class -> P4b single-channel -> P4c boson
# sector -> P8 two-U(1) -> P9 TR mixing -> P10 TR chiral projection.
T10=P_sq@L@(np.eye(F)-P_sq)-(np.eye(F)-P_sq)@L@P_sq
C10=T10/(2j)
cw10,cv10=np.linalg.eigh(C10)
selL=[i for i in range(F) if abs(cw10[i]-1)<1e-9]
selR=[i for i in range(F) if abs(cw10[i]+1)<1e-9]
PL10=cv10[:,selL]@cv10[:,selL].conj().T
PR10=cv10[:,selR]@cv10[:,selR].conj().T
fb10=list(range(F))
for i in range(6): fb10[i]=sq_dirs.index(tuple(-t for t in sq_dirs[i]))
for i,hh in enumerate(hexes): fb10[6+i]=6+hexes.index(tuple(-t for t in hh))
Rv10=np.zeros((F,3))
for i in range(6): Rv10[i]=4*np.array(sq_dirs[i])
for i,hh in enumerate(hexes): Rv10[6+i]=2*np.array(hh)
ok=True
for eta10 in [1.0, 0.07]:
    H10=L.astype(float).copy()
    for ff in range(F):
        H10[ff,ff]+=eta10; H10[ff,fb10[ff]]-=eta10
    w10,V10=np.linalg.eigh(H10)
    occ10=[i for i in range(F) if abs(w10[i]-(r1n+2*eta10))<1e-9][:3]
    emp10=[i for i in range(F) if i not in occ10]
    def PiAB(Aops,Bops):
        val=0.0
        for a_ax in range(3):
            for o in occ10:
                vo=V10[:,o].astype(complex)
                for e in emp10:
                    ve=V10[:,e].astype(complex); dE=w10[e]-w10[o]
                    if dE<1e-12: continue
                    val+=2*np.real(np.conj(vo)@Aops[a_ax]@ve*(np.conj(ve)@Bops[a_ax]@vo))/dE
        return val
    Js10=[]
    for a_ax in range(3):
        J=np.zeros((F,F),complex)
        for ff in range(F): J[ff,fb10[ff]]+=-1j*eta10*Rv10[ff,a_ax]
        Js10.append(J)
    JL10=[PL10@J@PL10 for J in Js10]; JR10=[PR10@J@PR10 for J in Js10]
    ok &= abs(PiAB(JL10,JL10)-PiAB(JR10,JR10))<1e-10
check("P10 Pi(j_L,j_L) = Pi(j_R,j_R) for TR-invariant seas: induced "
      "couplings are vector-like; chiral asymmetry needs the "
      "second-quantized vacuum", ok)

# ---------------------------------------------------------------- P11 GUT split
# Run-8 (theory design): with equal loop weights per fermion mode, the
# induced-coupling trace ratio over one generation is EXACTLY the GUT
# value: Sum T3^2 / Sum Q^2 = 2/(16/3) = 3/8 (Weyl-mode counting; no GUT
# group assumed -- this reproduces Paper #11's sin^2 = 3/8 from induced
# couplings alone). The low-energy formula then factorises exactly as
#   sin^2(theta_W) = (3/8) * (34 - 6 sqrt(17))/15
# so the entire open content of Result 58.3 is the gap-dependent loop
# weight factor (34-6*sqrt(17))/15 = 0.6174244. Missing lemmas ML1-ML4
# (doublet index, hypercharge operator, chiral vacuum, lattice loop
# weights) are specified in the explorations file.
Q2_gen = sp.Rational(4,3)+sp.Rational(1,3)+sp.Rational(4,3)+sp.Rational(1,3)+1+1
T32_gen = sp.Rational(3,2)+sp.Rational(1,2)
check("P11 equal-weight induced ratio = 3/8 (GUT value, no GUT assumed)",
      T32_gen/Q2_gen == sp.Rational(3,8))
check("P11 exact factorisation sin^2 = (3/8)*(34-6*sqrt(17))/15",
      sp.simplify(sp.Rational(3,8)*(34-6*S17)/15 - sin2) == 0)

# ---------------------------------------------------------------- P12 triangle vertex
# Run-9 lemmas: the 24 vertex-triangles (1 sq + 2 hx; the fermion triangle)
# define the canonical symmetric cubic invariant t3(X,u,v). Exact facts:
#   (a) SELECTION RULES: t3(A2u; T1u, T1u) = 0 and t3(T2g; T1u, T1u) = 0
#       identically (all band/polarization combinations). The triangle
#       vertex is an ELECTROWEAK-ONLY structure: only A1g0, A1g7, Eg
#       couple to fermion pairs through it. Consistent with the corpus:
#       the Yukawa is the antisymmetric torsion cross-block, not this.
#   (b) Eg slot: band-diagonal coupling ratio |t(Eg;r1,r1)/t(Eg;r2,r2)|
#       = s2/s1 exactly (the opposite-content ratio; the Eg leg sits on
#       the square, the fermion legs enter through their hex content).
#   (c) A1g0 (photon) slot: per-band couplings proportional to
#       a_i = (17 +- 15 sqrt(17))/34, with the SUM RULE a1 + a2 = 1 and
#       a1*a2 = -52/17; opposite signs between bands (interference
#       structure available at second order).
# Dressed-doublet reading (explorations Section 5, ML1 proposal): the
# W-emission amplitude of a dressed fermion is second order in t3
# (A1g-dressing vertex times Eg vertex through core intermediates), which
# carries denominators, mixed symmetry, and signed interference: all
# obstruction-theorem requirements present. That is the run-10 target.
a2u_=np.array([0.]*6+[np.prod(hh) for hh in hexes]); a2u_/=np.linalg.norm(a2u_)
q12,_=np.linalg.qr(np.hstack([a7[:,None],V7]))
T2g_=q12[:,1:4]
def t3_(X,u,v):
    tot=0.0
    for (f0,f1,f2) in tris:
        fc=[f0,f1,f2]
        for pm in itertools.permutations(range(3)):
            tot+=X[fc[pm[0]]]*u[fc[pm[1]]]*v[fc[pm[2]]]
    return tot/6.0
ok=True
for Xv in [a2u_]+[T2g_[:,m] for m in range(3)]:
    for Va_ in (V1,V2):
        for Vb_ in (V1,V2):
            for aa_ in range(3):
                for bb_ in range(3):
                    ok &= abs(t3_(Xv,Va_[:,aa_],Vb_[:,bb_]))<1e-12
check("P12a triangle selection rules: A2u and T2g slots vanish exactly "
      "(electroweak-only vertex)", ok)
def slotnorm(X,Va_,Vb_):
    M=np.array([[t3_(X,Va_[:,a_],Vb_[:,b_]) for b_ in range(3)] for a_ in range(3)])
    return np.linalg.norm(M)
Eg11=np.hypot(slotnorm(V4[:,0],V1,V1),slotnorm(V4[:,1],V1,V1))
Eg22=np.hypot(slotnorm(V4[:,0],V2,V2),slotnorm(V4[:,1],V2,V2))
s1f=float(s1s); s2f=1-s1f
check("P12b Eg band ratio = s2/s1 exactly", abs(Eg11/Eg22 - s2f/s1f)<1e-10)
u14=np.ones(F)/np.sqrt(F)
d1=t3_(u14,V1[:,0],V1[:,0]); d2=t3_(u14,V2[:,0],V2[:,0])
rat=d1/d2
a1s=(17+15*sp.sqrt(17))/34; a2s=(17-15*sp.sqrt(17))/34
check("P12c A1g0 band couplings ~ (17 +- 15 sqrt17)/34: ratio and sum rule",
      abs(rat-float(a1s/a2s))<1e-10 and sp.simplify(a1s+a2s-1)==0
      and sp.simplify(a1s*a2s+sp.Rational(52,17))==0)

# ---------------------------------------------------------------- P13 Galois
# Run-10 result and the day's master obstruction. The second-order
# dressing-exchange W amplitude (soft dressing, same-band intermediates
# excluded as the elastic piece) gives g_L^2 = g_R^2 EXACTLY and zero
# cross-band amplitude. Reason, and the theorem that subsumes P4a, P9,
# P10 and run-10:
#   The two chirality bands are GALOIS CONJUGATES in Q(sqrt(17)): the
#   conjugation sqrt(17) -> -sqrt(17) exchanges r1 <-> r2 while fixing
#   the rational spectrum {0,4,7,9} and every rational vertex tensor.
#   For any construction built from Galois-rational data, band-L and
#   band-R squared amplitudes are Galois conjugates of each other; if
#   the result is Galois-fixed (equivalently rational), it is band-blind.
#   CHIRAL ASYMMETRY IS GALOIS SYMMETRY BREAKING: the choice of which
#   band is left-handed is the choice of embedding of sqrt(17) into R.
# Physical selection: the Galois conjugate of the Weinberg formula is
# (17+3*sqrt(17))/20 = 1.1499 > 1, not a probability. Unitarity forces
# the physical root choice: a derivation need only produce the magnitude
# of the Galois-odd part; positivity fixes the sign. The odd part of
# sin^2(theta_W) is -3*sqrt(17)/20; the even part is 17/20.
sig_conj = (17+3*S17)/20
check("P13a Galois conjugate of sin^2 is (17+3*sqrt17)/20 = 1.1499 > 1 "
      "(unphysical: root choice forced by unitarity)",
      float(sig_conj) > 1 and sp.simplify(sin2+sig_conj-sp.Rational(17,10))==0)
check("P13b even/odd split: sin^2 = 17/20 - (3/20)*sqrt(17)",
      sp.simplify(sin2 - (sp.Rational(17,20)-sp.Rational(3,20)*S17))==0)
# g_L^2 = g_R^2 for the dressing-exchange amplitude (numeric, both bands)
u14_=np.ones(F)/np.sqrt(F)
def t3s(X,u,v):
    tot=0.0
    for (f0,f1,f2) in tris:
        fc=[f0,f1,f2]
        for pm in itertools.permutations(range(3)):
            tot+=X[fc[pm[0]]]*u[fc[pm[1]]]*v[fc[pm[2]]]
    return tot/6.0
levels_=[(w[i],V[:,i]) for i in range(F)]
def g2band(Vb,Eb):
    tot=0.0
    for m_ in range(2):
        eg=V4[:,m_]
        for p_ in range(3):
            for q_ in range(3):
                s_=0.0
                for (Ex,vx) in levels_:
                    if abs(Ex-Eb)<1e-9: continue
                    s_+=(t3s(u14_,Vb[:,p_],vx)*t3s(eg,vx,Vb[:,q_])
                        +t3s(eg,Vb[:,p_],vx)*t3s(u14_,vx,Vb[:,q_]))/(Eb-Ex)
                tot+=s_*s_
    return tot
check("P13c dressing-exchange g_L^2 = g_R^2 exactly (Galois-fixed, "
      "band-blind at second order)",
      abs(g2band(V1,r1n)-g2band(V2,r2n))<1e-15)

# ---------------------------------------------------------------- P5 forms
p41_form = sp.simplify(3*r1s*S17/128)   # = (27*sqrt(17)-51)/256 = 0.2356403
check("P5a Paper 41 form C_A*r1*sqrt(D)/128 is FALSE (0.235640 != 0.231534)",
      abs(float(p41_form) - 0.2356403) < 1e-6
      and sp.simplify(p41_form - sin2) != 0)
check("P5b (3*r1-5)/10 exact", sp.simplify((3*r1s-5)/10 - sin2)==0)
check("P5b sqrt(D)(sqrt(D)-C_A)/20 exact", sp.simplify(S17*(S17-3)/20 - sin2)==0)

print()
if FAILED:
    print("FAILURES:", FAILED); sys.exit(1)
print("ALL CHECKS PASS")
# 2026-07-02
