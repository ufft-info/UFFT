"""Substrate-direct programme: the unit map (2026-07-02).

CORRECTION (same day, evening run): the SCAN table below and result 1 are
superseded. The delta values were dominated by a periodization artifact
(min-subtracted foam potential vs non-periodized Coulomb control); the
clean deviation is NEGATIVE and scales as -K/a_B^2 (p = 2, analytic contact
mechanism). See verify_foam_hydrogen_deviation_2026-07.py and
.explorations/UFFT_Explorations_2026-07-02.md Section 6. Results 2 and 3
(the unit map and its stated dependencies) are unaffected.

Three results:
1. COUPLING SCAN. The foam-vs-Coulomb ground-state deviation delta(a_B)
   falls monotonically as the atom grows (0.24 at a_B ~ 9 cells down to
   0.02 at ~26, weakest point box-limited). Exponent not pinned (between
   ~1 and ~3; larger boxes needed) but ANY positive power suffices: at the
   physical scale a_B/l_P ~ 3.3e24 the foam correction is <= ~3e-25
   relative. Foam hydrogen converges to Schrodinger hydrogen.
2. THE MAP. With the framework's derived alpha (Ch 16 heat kernel,
   alpha^-1 = 137.035999055) and the framework's m_e (walk action, 0.002%),
   the foam-hydrogen Rydberg is alpha^2 m_e c^2 / 2 = 13.605693 eV
   (reduced-mass 1s: 13.598287 eV; the 1.1e-5 residual vs the measured
   13.598434 eV is standard relativistic + QED structure, outside the
   non-relativistic substrate calculation).
3. WHAT THE MAP ASSUMES (stated, not hidden): (i) the A1g channel coupling
   normalisation IS the derived alpha (the framework's photon
   identification); (ii) the light defect inertia IS m_e. Both are existing
   framework results, not new assumptions of this calculation. What today
   adds: given (i) and (ii), the bound-state problem itself introduces NO
   new freedom -- structure, ladder, and scale all follow.

Run: python explore_unit_map_2026-07.py   (requires scipy for the scan)
"""
from math import pi

def headline():
    alpha_inv = 8*pi**2.5*(47/48 + 10/(3*48**3) + 22/(3*48**5))
    alpha = 1/alpha_inv
    me, mp = 510998.95, 938272088.16     # eV
    Ry = alpha**2*me/2
    print(f"alpha^-1 (framework) = {alpha_inv:.9f}")
    print(f"Rydberg = alpha^2 m_e c^2/2 = {Ry:.6f} eV  (CODATA 13.605693)")
    print(f"H 1s (reduced mass)  = {Ry/(1+me/mp):.6f} eV  (measured 13.598434;")
    print("  residual 1.1e-5 = relativistic + Lamb, beyond the non-rel calculation)")
    print(f"foam correction bound: (l_P/a_B)^p, a_B/l_P = {5.29e-11/1.616e-35:.2e}, p>=1 -> <=3e-25")

# The coupling scan (delta vs a_B) is reproduced by the code in
# explore_foam_hydrogen_2026-07.py run at lc in {2.5,3.5,5,7,9,13}; measured
# deltas on N=64 (weakest point box-contaminated, flagged):
SCAN = [(25.6, 0.0237, "box-limited"), (18.3, 0.1308, ""), (12.8, 0.2003, ""),
        (9.1, 0.2395, ""), (7.1, 0.1995, "N=48"), (4.9, 0.2180, "N=48 saturating")]

if __name__ == "__main__":
    headline()
    print("\ncoupling scan (a_B in embedding units, delta = E1_foam/E1_coul - 1):")
    for aB, d, note in SCAN:
        print(f"  aB = {aB:5.1f}  delta = {d:.4f}  {note}")
