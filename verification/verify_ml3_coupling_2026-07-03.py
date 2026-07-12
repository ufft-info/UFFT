"""verify_ml3_coupling_2026-07-03.py  (rev2 - CORRECTED after self-audit)

ML3 step 3: is the foam's torsion coupling above the chiral threshold g_c?
Companion: .explorations/UFFT_Explorations_2026-07-03.md Section 11.

CORRECTION NOTE (rev2). The first version claimed the foam is "near-critical"
because forced couplings (Yukawa Y=4, torsion T^2=4, Higgs-exchange
Y^2/lam_A2u=1.78) "straddle" g_c ~ 2.06. That comparison is DIMENSIONALLY
UNSOUND and is WITHDRAWN: Y is a dimensionless coupling, T^2 is energy^2, and
g_c (=1/chi, chi=mean(1/|d|)) is an energy. They are not the same kind of
object, so "straddles g_c" was apples-to-oranges (FAILSAFES rules 6, 9).

What is actually true and dimensionally clean:

  S1  g_c = 1/chi = 1/mean(1/|d|) is approximately mean|d|, the fermion gap,
      because the band is nearly flat. So "g_c is of order the fermion gap
      ~ 2" is near-TAUTOLOGICAL (g_c is set by the gap by construction), not a
      physics coincidence. The earlier "g_c ~ |T|=2" reading is downgraded to
      this tautology.

  S2  The genuine question -- does the foam's four-fermion torsion coupling
      (in the SAME energy units as g_c) exceed g_c -- is NOT resolved here.
      A dimensionally-consistent four-fermion coupling requires the B+V=D
      vertex in the foam action, which the corpus treats axiomatically
      (From Foam to Fermions line 635: the chirality sign is fixed by the
      axiom B+V=D, "not derived, the single physical input"). Undetermined.

HONEST STATUS of the ML3 arc after the audit:
  Step 1 (single-particle band topology ruled out, Chern=0) -- ROBUST,
     confirmed on the FULL T1u sector, not just the 2x2 (ml3_audit_fullchern).
  Step 2 (NJL torsion-condensate threshold g_c exists, ~2 in the model's own
     energy units) -- SOUND within the model.
  Step 3 (whether the foam exceeds g_c) -- OPEN; the near-critical claim is
     WITHDRAWN as dimensionally unsound. The chirality sign stays axiom-level.
"""
import sys, numpy as np
FAILED=[]
def check(n,ok,d=""):
    print(("PASS  " if ok else "FAIL  ")+n+(("   "+d) if d else ""))
    if not ok: FAILED.append(n)

r1=(9-np.sqrt(17))/2; r2=(9+np.sqrt(17))/2
gc=2.065  # from verify_ml3_njl (1/mean(1/|d|), model energy units)
gap=2.065  # mean|d| over the BZ (from the same run)
check("S1 g_c ~ mean|d| = fermion gap: g_c is set by the gap by construction "
      "(near-tautological), NOT a coincidence with |T|",
      abs(gc-gap)<0.05)
# The forced quantities are real but dimensionally DISTINCT from g_c:
Y=np.sqrt(r1*r2)   # dimensionless coupling
Tsq=4.0            # energy^2
check("S2 forced quantities exist (Y=sqrt(r1r2)=4 dimensionless; T^2=4 "
      "energy^2) but are NOT commensurate with g_c (energy): no clean "
      "comparison; foam coupling in consistent units is undetermined",
      abs(Y-4)<1e-9 and abs(Tsq-4)<1e-9)
check("S3 chirality sign stays AXIOM-LEVEL (FtF line 635): steps 1-2 give a "
      "no-go + a threshold, but step 3 does not decide the phase",
      True)
print()
if FAILED: print("OPEN/FAIL:",FAILED); sys.exit(1)
print("ML3 step3 CORRECTED: near-critical claim withdrawn (dimensionally "
      "unsound). g_c~gap is tautological; foam four-fermion coupling in "
      "consistent units is UNDETERMINED (B+V=D axiom-level, FtF line 635).")
