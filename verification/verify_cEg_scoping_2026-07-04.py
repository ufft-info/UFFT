"""verify_cEg_scoping_2026-07-04.py

c_Eg SCOPING RUN (Root, 2026-07-04). Executes the tractable half of the
Applied-Tech handoff brief (private applied-technology brief, not in this repository)
and PROVES the half that decides concept fate.

Split enforced by FAILSAFES: Paper 47's alpha_s closed form is itself
search-identified ("DERIVED pending formal proof", P47 section 4.2), so the
analogue-substitution forms 1-3/5 CANNOT be promoted by substitution alone.
What CAN be settled now, form-independently:

  (A) the Eg-sector lattice facts the brief asks to verify (E1-E3);
  (B) the OBSERVABILITY bound: the predicted tabletop chronometric shift
      at Stage-1 drive, maximized over ALL candidate forms and the most
      generous coupling assumptions (E4-E6). This alone decides the
      brief's promotion-or-retire table.

Run: python verify_cEg_scoping_2026-07-04.py  (~5 s)
"""
import numpy as np, itertools, sys

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

# ---- face graph of the truncated octahedron (canonical construction) ----
# squares 0..5 along +-x,+-y,+-z; hexes 6..13 at (+-1,+-1,+-1)/sqrt3
sq_n=[np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
hx_n=[np.array(v)/np.sqrt(3) for v in itertools.product([1,-1],repeat=3)]
normals=sq_n+hx_n
F=14
A=np.zeros((F,F))
for i in range(6):
    for j in range(6,14):
        if np.dot(sq_n[i],hx_n[j-6])>1e-12: A[i,j]=A[j,i]=1
for j in range(6,14):
    for k in range(j+1,14):
        if abs(np.dot(hx_n[j-6],hx_n[k-6])*3-1)<1e-9: A[j,k]=A[k,j]=1
D=np.diag(A.sum(1)); L=D-A
w,V=np.linalg.eigh(L)

# E1: lambda=4 with multiplicity 2, and its eigenvectors live on squares only
idx4=[i for i in range(F) if abs(w[i]-4)<1e-9]
sq_weight=sum(np.linalg.norm(V[:6,i])**2 for i in idx4)/len(idx4)
check("E1 Eg eigenvalue 4 has multiplicity 2, 100% square-face support",
      len(idx4)==2 and abs(sq_weight-1)<1e-12, f"mult={len(idx4)}, sq_weight={sq_weight:.12f}")

# E2: partner-face Bloch on the SC channel; Eg bandwidth
eta_sq=np.exp(-2*np.sqrt(2)); eta_hx=np.exp(-np.sqrt(6))
eta=np.array([eta_sq]*6+[eta_hx]*8)
antip={0:1,1:0,2:3,3:2,4:5,5:4,6:13,13:6,7:12,12:7,8:11,11:8,9:10,10:9}
Rf=np.array([n/np.linalg.norm(n) for n in normals])
def H(q):
    M=L.astype(complex)+np.diag(eta)
    for f in range(F):
        M[f,antip[f]]-=eta[f]*np.exp(1j*np.dot(q,Rf[f])*2)
    return M
V4=V[:,idx4]
vals=[]
for a in np.linspace(0,np.pi,9):
  for b in np.linspace(0,np.pi,9):
    for cq in np.linspace(0,np.pi,9):
      W=V4.conj().T@H(np.array([a,b,cq]))@V4
      vals+=list(np.linalg.eigvalsh(W))
vals=np.array(vals)
bw=(vals.max()-vals.min())/eta_sq
W0=np.linalg.eigvalsh(V4.conj().T@H(np.zeros(3))@V4)
check("E2 Eg band (degenerate-block projection): bandwidth = 2 eta_sq exactly, "
      "q=0 block = 4 exactly (void cancels, Paper 45 antipodal map)",
      abs(bw-2.0)<1e-9 and np.allclose(W0,4), f"bw/eta_sq = {bw:.12f}")

# E3: static Green's function kernel is gapped: correlation length ~ 1/sqrt(lambda_Eg/eta)
# 1D chain surrogate along <100>: G(r) ~ exp(-r/xi), cosh form: gap 4, hop eta_sq
# lattice: xi = 1/arccosh(1 + lambda/(2 eta))
xi=1/np.arccosh(1+4/(2*eta_sq))
check("E3 Eg propagator is SHORT-RANGED: xi = "+f"{xi:.4f}"+" cell edges (<1)",
      xi<1.0, "massive kernel; no long-range Eg field at tree level")

# ---- (B) observability: form-independent ceiling ----
# Stage-1 drive (brief section 6): 40 kHz on 485 g Bi cell. GENEROUS numbers:
G=6.674e-11; c=2.998e8; lP=1.616e-35; MPc2=1.956e9  # J
E_drive=1.0          # J stored acoustic energy (ceiling; realistic ~0.04 J)
r=0.05               # m, clock standoff
v_s=2000.0           # m/s sound speed in Bi
lam_ac=v_s/40e3      # acoustic wavelength ~ 5 cm

# E4: Newtonian (derived-in-corpus) channel: foam reproduces Newton tail =>
# a phonon field of energy E gravitates as E. Chronometric shift:
df_newton=G*E_drive/(c**4*r)*c**2/1  # dPhi/c^2 = G E /(c^2 * c^2 r)... careful:
df_newton=G*E_drive/(c**4*r)
check("E4 Newtonian channel at Stage-1 drive: df/f = "+f"{df_newton:.2e}",
      df_newton<1e-40, "vs clock floor 1e-19: 24 orders below")

# E5: anomalous channel ceiling: response LINEAR in source amplitude
# (partner-face model is linear; E2/E3), so total source bounded by drive
# energy in Planck units TIMES the mode-overlap form factor. Most generous:
# ONE power of (lP/lambda_acoustic), c_Eg at the LARGEST candidate (Form 1).
cEg_max=4-2*np.log(2)/(2*np.pi)   # 3.7794 (Form 1, strongest candidate)
ceiling=cEg_max*(E_drive/MPc2)*(lP/lam_ac)
check("E5 anomalous ceiling (max form, k=1 form factor): df/f <= "+f"{ceiling:.2e}",
      ceiling<1e-40, "even ONE lP/L power + Form 1 is ~23 orders below clocks")

# E6: no coherence loophole: linear response in total amplitude means N-cell
# coherent states cannot exceed the E_drive/MPc2 budget; and E_drive is
# itself LESS THAN ONE foam quantum:
check("E6 total Stage-1 drive energy = "+f"{E_drive/MPc2:.1e}"+" foam quanta (<1)",
      E_drive/MPc2<1, "the whole bench drive is half a billionth of one quantum")

print()
if FAILED: print("OPEN:",FAILED); sys.exit(1)
print("VERDICT (form-independent): the brief's decision table lands in the")
print("Form-4/6 ROW REGARDLESS of which closed form c_Eg takes: predicted")
print("tabletop df/f <= 1e-42 vs clock floor 1e-19. C2 (chronometry) and C3")
print("(spacetime lens) RETIRE as tabletop/near-term concepts. The internal")
print("closed form for c_Eg remains OPEN pending the Paper-47 alpha_s formal")
print("derivation (P47 4.2); it is now decoupled from any bench decision.")
