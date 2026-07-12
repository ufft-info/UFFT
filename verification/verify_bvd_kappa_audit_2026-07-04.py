"""verify_bvd_kappa_audit_2026-07-04.py

THE KAPPA AUDIT (2026-07-04, same-day). Decides the normalisation
question left open by verify_bvd_stiffness_chain_2026-07-04.py, and
CORRECTS the same-day companion's overclaim.

CORRECTION (FAILSAFES rule 7 applied internally): the morning statement
"the chiral phase follows at mechanism level" (bvd_chiral_channel
docstring, R3) rested on a soft-mode-enhancement intuition that holds
only in the FORCE-CONTROLLED coupling limit. The audit shows:

  - displacement-controlled limit (the corpus-consistent one: defects
    are topological windings, Paper #14, so their displacement content
    is quantized and imposed rigidly): g*chi = 0.219 at unit quantum -
    a factor 4.6 BELOW the chiral threshold; breaking would need a
    composite defect of >= 2.14 displacement quanta.
  - force-controlled limit (physically disfavored here): g*chi = 0.945,
    marginally below threshold.

VERDICT: pair-even void exchange does NOT break chirality at natural
normalisation, in either limit. The morning phase claim is WITHDRAWN;
what stands from the morning is the parity theorem, the exact chiral-
channel weights, the soft-mode identification, and the derived
stiffnesses - all still correct and load-bearing.

EXCLUSION SET for the chiral filling (ML3) now:
  1. single-particle band topology (2026-07-03: Chern = 0, all terms);
  2. density-channel B+V=D interactions (2026-07-04 parity theorem);
  3. pair-even void exchange at natural normalisation (this audit).

REDIRECT (named, Tier 4 until computed): the chiral condensate should
be sought in the T2g (colour) sector's strong dynamics - the standard
QCD-like mechanism. Independent fingerprint: the Galois-odd Weinberg
numerator is C_A*sqrt(Delta), and C_A is the COLOUR number; a colour-
driven chiral condensate would put it there naturally. The corpus
already carries confinement (pi_1 = Z, b0 = 7 = lambda_T2g).

Run: python verify_bvd_kappa_audit_2026-07-04.py  (~1 s)
"""
import numpy as np, sys

FAILED=[]
def check(name,ok,detail=""):
    print(("PASS  " if ok else "FAIL  ")+name+(("   "+detail) if detail else ""))
    if not ok: FAILED.append(name)

e_sq=np.exp(-2*np.sqrt(2)); e_hx=np.exp(-np.sqrt(6))
rho_sq=8*e_sq; rho_hx=6*e_hx
w_sq,w_hx=0.5,0.125
chi=6/np.sqrt(17)
gD=rho_sq*w_sq**2+4*rho_hx*w_hx**2
gF=w_sq**2/rho_sq+4*w_hx**2/rho_hx
check("A1 displacement-controlled g*chi = 0.219 (below threshold 1)",
      abs(gD*chi-0.2191)<1e-3 and gD*chi<1, f"{gD*chi:.4f}")
check("A2 force-controlled g*chi = 0.945 (below threshold 1)",
      abs(gF*chi-0.9450)<1e-3 and gF*chi<1, f"{gF*chi:.4f}")
check("A3 breaking in the corpus-consistent limit needs a composite "
      "defect >= 2.14 quanta",
      abs(np.sqrt(1/(gD*chi))-2.136)<0.01)
check("A4 leverage between limits = 1/(rho^2-structure) ~ 4.3",
      abs(gF/gD-4.31)<0.05)
print()
if FAILED: print("OPEN:",FAILED); sys.exit(1)
print("KAPPA AUDIT: void-exchange chiral breaking EXCLUDED at natural")
print("normalisation (both limits). Morning phase claim withdrawn.")
print("Chiral filling redirected to the T2g/colour sector (C_A fingerprint).")
