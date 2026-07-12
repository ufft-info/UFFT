#!/usr/bin/env python3
"""
Paper #68 — Verification of Theorem 3.6 (reconciliation of the two
cell-integer rewritings of 197/144).

Tests:
 (1)  The identity 2(F-2)^2 - lambda_T2g * (F-1) == F^2 + 1 with
      lambda_T2g = 7 holds if and only if F ∈ {1, 14}.
 (2)  For the five Fedorov parallelohedra, evaluate both sides of
      (2 N_gauge^2 - 7 (F-1)) / N_gauge^2  vs  (F^2 + 1)/(E-V)^2
      and report whether they coincide with 197/144 = 1.36805...
 (3)  For the truncated octahedron, verify
      197/144 = (2 * 144 - 7 * 13) / 144 exactly via Fraction arithmetic.

This is a closed mathematical test (no physics input). It does NOT
establish the direct foam-diagram derivation of 197/144 — that
calculation remains open per Paper #68 Lemmas 3.1–3.3, 3.5.

Usage:
    python Paper68_Reconciliation_Theorem.py

Exit codes:
    0 if all three tests pass
    1 otherwise
"""

from fractions import Fraction
import sys

# -------------------------------------------------------------------------
# Cell data (Fedorov parallelohedra, F = number of 2-faces)
# -------------------------------------------------------------------------
#
# For each cell we record (V, E, F). Euler: V - E + F = 2 is enforced.
# Face Laplacian spectra are cell-specific and NOT all assumed to include
# a T_{2g}-like eigenvalue at 7 — this is a property of the truncated
# octahedron only (confirmed by direct diagonalisation, see Paper #5 and
# Spectral_Uniqueness_Fedorov_Parallelohedra.md for the five-cell audit).

fedorov_cells = {
    "cube":                   {"V":  8, "E": 12, "F":  6},
    "hexagonal prism":        {"V": 12, "E": 18, "F":  8},
    "rhombic dodecahedron":   {"V": 14, "E": 24, "F": 12},
    "elongated dodecahedron": {"V": 18, "E": 28, "F": 12},
    "truncated octahedron":   {"V": 24, "E": 36, "F": 14},
}

# The T_{2g} eigenvalue in the face Laplacian of the truncated octahedron.
# This is a specific cell property (see Paper #5).
LAMBDA_T2G_TRUNCATED_OCT = 7

# -------------------------------------------------------------------------
# Test 1 — the algebraic identity (F-1)(F-14) = 0 ⇔ the two rewritings agree
# -------------------------------------------------------------------------

def test_identity_roots():
    """Verify 2(F-2)^2 - 7(F-1) = F^2 + 1 iff F ∈ {1, 14}."""
    print("Test 1 — (F-1)(F-14) = 0 reconciliation")
    print("-" * 60)
    passing = []
    failing = []
    for F in range(1, 31):
        lhs = 2 * (F - 2) ** 2 - 7 * (F - 1)
        rhs = F ** 2 + 1
        match = (lhs == rhs)
        if match:
            passing.append(F)
        else:
            failing.append(F)
    expected_pass = [1, 14]
    ok = (passing == expected_pass)
    print(f"  F for which 2(F-2)^2 - 7(F-1) == F^2 + 1: {passing}")
    print(f"  Expected: {expected_pass}")
    print(f"  Result: {'PASS' if ok else 'FAIL'}")
    print()
    return ok


# -------------------------------------------------------------------------
# Test 2 — across Fedorov cells, which forms evaluate to 197/144?
# -------------------------------------------------------------------------

def test_fedorov_survey():
    """
    For each Fedorov cell, compute:
      * naive form  (F^2 + 1) / (E - V)^2
      * (hypothetical) structural form (2(E-V)^2 - 7(F-1))/(E-V)^2
        — this form uses lambda_{T_{2g}} = 7 which is ONLY the correct
          face-Laplacian eigenvalue for the truncated octahedron.
          For other cells we evaluate the formula anyway as a test of
          the F = 14 singleton property.

    We expect BOTH forms to give 197/144 only for the truncated octahedron.
    """
    print("Test 2 — Fedorov-cell survey of the two rewritings")
    print("-" * 60)
    target = Fraction(197, 144)
    header = f"  {'cell':<24} {'F':>3} {'(F^2+1)/(E-V)^2':>22}   {'(2(E-V)^2-7(F-1))/(E-V)^2':>30}"
    print(header)
    all_ok = True
    for name, cell in fedorov_cells.items():
        V, E, F = cell["V"], cell["E"], cell["F"]
        assert V - E + F == 2, f"Euler failed for {name}"
        EmV = E - V
        naive = Fraction(F * F + 1, EmV * EmV)
        structural = Fraction(2 * EmV * EmV - 7 * (F - 1), EmV * EmV)
        naive_match = (naive == target)
        struct_match = (structural == target)
        marker_naive = " *" if naive_match else "  "
        marker_struct = " *" if struct_match else "  "
        print(f"  {name:<24} {F:>3} {str(naive):>20}{marker_naive}   {str(structural):>28}{marker_struct}")
        # Only the truncated octahedron should match both
        if name == "truncated octahedron":
            if not (naive_match and struct_match):
                all_ok = False
        else:
            if naive_match or struct_match:
                all_ok = False
    print()
    print(f"  Target 197/144 = {target} ≈ {float(target):.6f}")
    print(f"  Only the truncated octahedron satisfies both rewritings: {'PASS' if all_ok else 'FAIL'}")
    print()
    return all_ok


# -------------------------------------------------------------------------
# Test 3 — exact rational-arithmetic check for the truncated octahedron
# -------------------------------------------------------------------------

def test_exact_identity():
    """Verify 197/144 = (2*144 - 7*13)/144 exactly using Fraction arithmetic."""
    print("Test 3 — exact rational identity for the truncated octahedron")
    print("-" * 60)
    V, E, F = 24, 36, 14
    N_gauge = E - V  # 12
    beta1 = F - 1    # 13
    lhs = Fraction(197, 144)
    rhs_structural = Fraction(2 * N_gauge ** 2 - LAMBDA_T2G_TRUNCATED_OCT * beta1,
                              N_gauge ** 2)
    rhs_naive = Fraction(F ** 2 + 1, N_gauge ** 2)
    print(f"  N_gauge = E - V = {N_gauge}")
    print(f"  beta_1(skeleton) = F - 1 = {beta1}")
    print(f"  lambda_T2g = {LAMBDA_T2G_TRUNCATED_OCT}")
    print(f"  (2 N^2 - lambda * beta_1) / N^2 = {rhs_structural}")
    print(f"  (F^2 + 1) / (E - V)^2           = {rhs_naive}")
    print(f"  Target 197/144                  = {lhs}")
    ok = (lhs == rhs_structural == rhs_naive)
    print(f"  Result: {'PASS' if ok else 'FAIL'}")
    print()
    return ok


# -------------------------------------------------------------------------

def main():
    results = [
        test_identity_roots(),
        test_fedorov_survey(),
        test_exact_identity(),
    ]
    print("=" * 60)
    if all(results):
        print("All three tests PASS.")
        print()
        print("Conclusion:")
        print("  * The identity 2(F-2)^2 - 7(F-1) = F^2 + 1 holds only for")
        print("    F in {1, 14}. Among the five Fedorov parallelohedra,")
        print("    only the truncated octahedron satisfies it.")
        print("  * The naive '(F^2 + 1)/(E-V)^2' form is a cell-specific")
        print("    coincidence, not a general structural predictor.")
        print("  * The Paper #27 form (2 N^2_gauge - lambda_T2g * beta_1)")
        print("    / N^2_gauge is the structurally meaningful rewriting.")
        print()
        print("This verification does NOT establish the direct foam-diagram")
        print("derivation of 197/144 — that calculation remains the genuine")
        print("open problem of Paper #68 (Lemmas 3.1-3.3, 3.5).")
        return 0
    else:
        print("One or more tests FAILED.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
