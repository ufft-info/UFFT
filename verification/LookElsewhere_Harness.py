"""
UFFT Look-Elsewhere Harness
============================

Peer-review question: given the integers that UFFT allows in its formulas
({V, E, F, |G|, C_A, Delta, F_hx, F_sq, r1, r2, sqrt(Delta), pi, ...}), how
many dimensionless combinations of small complexity fall close to a given
experimental target? If many do, a single "0.3 sigma" match is meaningless
because the search space is large. If very few do, the match is content-
bearing.

This script implements a brute-force enumeration over a well-defined finite
family of candidate formulas and reports, for each experimental target, the
hit density: P(a random simple formula is within tolerance t of the target).

Formula family enumerated
-------------------------
    candidate(a, b, c, d) = (a + b * sqrt(Delta)) / (c + d * sqrt(Delta))

with a, b, c, d drawn from the integer set

    I = { -N, -(N-1), ..., -1, 0, 1, ..., N }  for some bound N,

plus a separate sub-family of sin and cos of rational multiples of pi:

    sin(p * pi / q),  cos(p * pi / q),  with 1 <= p, q <= Q.

Both families contain the concrete UFFT matches as elements (e.g. the
Weinberg angle (17-3*sqrt(17))/20 corresponds to a=17, b=-3, c=20, d=0 with
N = 20, and the Cabibbo angle sin(pi/14) lies in the sin-family at p=1,
q=14). The family is therefore fair to UFFT -- we are counting hits in a
space that contains UFFT's own moves.

The script computes, for each published UFFT result, the fraction of the
search space within tolerance t of the experimental value. This fraction
is the look-elsewhere factor: to a first approximation, the "true"
significance of a UFFT match is the nominal sigma divided by the hit
density times the search-space size.

Run:    python LookElsewhere_Harness.py
Deps:   numpy, math   (stdlib only in current form)
"""

from __future__ import annotations
import math
from fractions import Fraction
from dataclasses import dataclass

sqrt17 = math.sqrt(17)

# ---------------------------------------------------------------------------
# Enumeration bounds
# ---------------------------------------------------------------------------
#   N  = max absolute integer in (a + b sqrt(17)) / (c + d sqrt(17)).
#        N = 26 is large enough to contain every UFFT numerator/denominator
#        we have published (the largest, for dark energy, is 6/7; for
#        m_H/M_Z it is 18/(9+sqrt(17)); for sin^2 theta_W it is
#        (17 - 3 sqrt(17))/20).  N = 20 gives ~1.4 M formulas; N = 30
#        gives ~7 M.  We use N = 20 by default.
N_DEFAULT = 20
#   Q = max denominator in sin/cos family, e.g. sin(pi/14), cos(2 pi / 9).
Q_DEFAULT = 20

TOL_DEFAULT = 1e-3   # a match within 0.1 % of the target counts as a hit

# ---------------------------------------------------------------------------
# Targets from UFFT's own prediction list (Core Framework, selected lines)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Target:
    name: str
    value: float
    ufft_formula_value: float      # UFFT's own predicted number
    tol: float = TOL_DEFAULT

TARGETS = [
    Target("sin^2 theta_W (effective)", 0.23122, (17 - 3 * sqrt17) / 20),
    Target("Omega_DE / Omega_tot",      0.685,   6.0 / 7.0),
    Target("m_H / M_Z",                 1.3716,  18.0 / (9 + sqrt17)),
    Target("lambda_Cabibbo (LO)",       0.22500, math.sin(math.pi / 14)),
    Target("tan^2 theta_12 (solar)",    0.4528,  sqrt17 / 9),
    Target("Koide Q",                   2.0/3.0, 2.0 / 3.0),
    Target("delta_PMNS / delta_CKM",    3.000,   3.0),
    Target("A Wolfenstein",             0.826,   (19 + sqrt17) / 28),
    Target("alpha_inv",                 137.035999084,
           137.035999055),  # UFFT geometric series result, paper 16
]

# ---------------------------------------------------------------------------
# Family 1: rational-in-sqrt(17) enumeration
# ---------------------------------------------------------------------------
def enumerate_rational_sqrt17(N: int):
    """Yield (a,b,c,d, value) with value = (a + b sqrt17)/(c + d sqrt17)."""
    for c in range(-N, N + 1):
        for d in range(-N, N + 1):
            denom = c + d * sqrt17
            if abs(denom) < 1e-9:
                continue
            for a in range(-N, N + 1):
                for b in range(-N, N + 1):
                    num = a + b * sqrt17
                    yield a, b, c, d, num / denom

def count_family1_size(N: int) -> int:
    # (2N+1)^4 minus denom-zero lattice lines
    total = (2 * N + 1) ** 4
    # lines c = -d sqrt(17) have NO integer solutions except c=d=0, so we
    # only strike out c=d=0
    return total - (2 * N + 1) ** 2   # strike all (a,b,0,0) pairs

# ---------------------------------------------------------------------------
# Family 2: sin/cos of pi * p/q
# ---------------------------------------------------------------------------
def enumerate_trig(Q: int):
    """Yield trig values at rational multiples of pi."""
    seen = set()
    for q in range(2, Q + 1):
        for p in range(1, 2 * q):
            v_sin = math.sin(p * math.pi / q)
            v_cos = math.cos(p * math.pi / q)
            key_sin = round(v_sin, 10)
            key_cos = round(v_cos, 10)
            if key_sin not in seen:
                seen.add(key_sin)
                yield ("sin", p, q, v_sin)
            if key_cos not in seen:
                seen.add(key_cos)
                yield ("cos", p, q, v_cos)

# ---------------------------------------------------------------------------
# Hit-density computation
# ---------------------------------------------------------------------------
def hit_density_family1(target_value: float, N: int, tol: float) -> tuple[int, int]:
    hits = 0
    tried = 0
    for a, b, c, d, v in enumerate_rational_sqrt17(N):
        tried += 1
        rel = (v - target_value) / target_value if target_value != 0 else v - target_value
        if abs(rel) <= tol:
            hits += 1
    return hits, tried

def hit_density_family2(target_value: float, Q: int, tol: float) -> tuple[int, int]:
    hits = 0
    tried = 0
    for kind, p, q, v in enumerate_trig(Q):
        tried += 1
        if target_value == 0:
            rel = v
        else:
            rel = (v - target_value) / target_value
        if abs(rel) <= tol:
            hits += 1
    return hits, tried

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main(N: int = N_DEFAULT, Q: int = Q_DEFAULT, tol: float = TOL_DEFAULT):
    print("=" * 78)
    print("UFFT LOOK-ELSEWHERE HARNESS")
    print(f"Family 1: (a + b sqrt(17)) / (c + d sqrt(17)), |a|..|d| <= {N}")
    print(f"Family 2: sin(p pi/q), cos(p pi/q), 2 <= q <= {Q}")
    print(f"Tolerance: relative error <= {tol:.1e}")
    print("=" * 78)

    # Pre-compute family sizes
    F1_total_expected = count_family1_size(N)
    # Family 2: 2 trig fns * sum_{q=2..Q} (2q - 1) unique vals approx
    F2_total_expected = sum(2 * (2 * q - 1) for q in range(2, Q + 1))

    print(f"Family 1 size (approx): {F1_total_expected:,}")
    print(f"Family 2 size (raw)   : {F2_total_expected:,}")
    print()

    header = (f"{'Target':<30} {'exp value':>12} {'UFFT':>12} "
              f"{'F1 hits':>9} {'F1 rate':>10} {'F2 hits':>9} {'F2 rate':>10}")
    print(header)
    print("-" * len(header))

    for t in TARGETS:
        h1, n1 = hit_density_family1(t.value, N, tol)
        h2, n2 = hit_density_family2(t.value, Q, tol)
        rate1 = h1 / n1 if n1 else 0.0
        rate2 = h2 / n2 if n2 else 0.0
        print(f"{t.name:<30} {t.value:>12.6f} {t.ufft_formula_value:>12.6f} "
              f"{h1:>9,} {rate1:>10.2e} {h2:>9,} {rate2:>10.2e}")

    print()
    print("Reading the numbers")
    print("-------------------")
    print("F1 rate ~ 10^-k means: roughly 1 in 10^k formulas of the form")
    print("(a + b sqrt17)/(c + d sqrt17) with |coeffs| <= N lies within")
    print("the stated tolerance of the experimental value. For a claim")
    print("with nominal significance sigma, the look-elsewhere-corrected")
    print("significance is approximately sigma - sqrt(2 ln(1/rate)). If")
    print("the rate is 10^-3, the correction subtracts ~3.7 sigma worth")
    print("of 'lookability', i.e. UFFT's match is only interesting if it")
    print("is accurate far beyond the search-space density.")
    print()
    print("Content-bearing matches are those where the UFFT prediction is")
    print("inside the tolerance AND the hit-density is small AND the formula")
    print("is fixed in advance by an independent principle (not a post-hoc")
    print("search). This script addresses the first two conditions; the")
    print("third is a matter of the derivation chain outside this code.")

if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT
    Q = int(sys.argv[2]) if len(sys.argv) > 2 else Q_DEFAULT
    tol = float(sys.argv[3]) if len(sys.argv) > 3 else TOL_DEFAULT
    main(N=N, Q=Q, tol=tol)
