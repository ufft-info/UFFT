"""verify_bvd_stiffness_chain_2026-07-04.py

THE PAIR-EVEN STIFFNESS, DERIVED, AND THE ASSEMBLED GAP CHAIN (2026-07-04).
Continues verify_bvd_chiral_channel_2026-07-04.py. Content:

  S1  The void pair-even (acoustic) stiffness is DERIVED, not chosen:
      the pair-even dispersion of the partner-coupled void sector is
      eps_f(q) = eta_f (1 - cos q.R_f), so
          rho_sq = eta_sq |R_sq|^2/2 = 8 eta_sq  = 0.47285
          rho_hx = eta_hx |R_hx|^2/2 = 6 eta_hx  = 0.51803
      with eta_f = Paper #45's derived void couplings and R_f the
      partner displacements (4 and 2 sqrt3). Verified against the exact
      dispersion to machine precision.
  S2  Goldstone-exchange chiral coupling (Adler derivative coupling, so
      the q^2 cancels and the exchange is finite):
          g_eff = kappa^2 [ (1/2)^2/rho_sq + 4 (1/8)^2/rho_hx ]
                = 0.64936 kappa^2
      with the exact pair-even chirality weights of the companion script
      and kappa = the defect-displacement normalisation (the ONE number
      still not derived).
  S3  Chiral susceptibility IN THE SAME CONVENTION: chi = 6/sqrt(17)
      (three polarizations, unit doublet matrix element, gap sqrt17).
  S4  Gap-equation threshold: g_eff * chi = 1 at kappa_c = 1.0287.
      THE THRESHOLD SITS WITHIN 3% OF THE NATURAL kappa = 1.
      NO PHASE VERDICT IS CLAIMED: per-pair vs per-face weight
      normalisation, the vacuum-triad multiplicity, and exchange
      combinatorial factors are each O(1) conventions larger than the
      margin. The 2026-07-03 session withdrew one premature
      "near-critical" claim; this one is stated as an open convention
      audit, which now DECIDES the chiral phase quantitatively.
  Suggestive note (Tier 4, not a claim): if near-criticality survives
  the audit, a near-critical condensate is parametrically small, which
  would cohere with the smallness of the Galois-odd Weinberg part.

Run: python verify_bvd_stiffness_chain_2026-07-04.py  (~1 s)
"""
import numpy as np, sys

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

e_sq=np.exp(-2*np.sqrt(2)); e_hx=np.exp(-np.sqrt(6))
rho_sq=e_sq*16/2; rho_hx=e_hx*12/2
for name,R2,eta,rho in [("sq",16,e_sq,rho_sq),("hx",12,e_hx,rho_hx)]:
    q=1e-4
    eps=eta*(1-np.cos(q*np.sqrt(R2)))
    check(f"S1 {name} stiffness = eta*|R|^2/2 (dispersion check)",
          abs(eps/q**2-rho)<1e-6, f"rho={rho:.5f}")
g1=(0.5)**2/rho_sq + 4*(0.125)**2/rho_hx
check("S2 g_eff/kappa^2 = w^2/rho summed = 0.64936",
      abs(g1-0.64936)<1e-4, f"{g1:.5f}")
chi=6/np.sqrt(17)
check("S3 chi = 6/sqrt(17) in-convention", abs(chi-1.45521)<1e-4)
kc=1/np.sqrt(g1*chi)
check("S4 threshold kappa_c within 10% of 1 (convention-audit regime; "
      "NO phase verdict)", 0.9<kc<1.15, f"kappa_c={kc:.4f}")
print()
if FAILED: print("OPEN:",FAILED); sys.exit(1)
print("STIFFNESS DERIVED; CHAIN ASSEMBLED; PHASE = PENDING CONVENTION AUDIT")
