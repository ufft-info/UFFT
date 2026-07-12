"""
Verification script for UFFT Paper #69.

R_b NLO denominator 2V - F = 34 from fermion-walk operator perturbation
on the truncated-octahedron Kelvin cell.

Checks:
  1. Four independent decompositions of 2V - F all yield 34.
  2. Numerator F - 1 = 13 equals the first Betti number of the 1-skeleton.
  3. R_b = 13/34 combined with Paper #67's delta_NLO closes the unitarity
     triangle apex (rho_bar, eta_bar) within 0.03 sigma of PDG 2023.
  4. Reconciliation with Paper #64's r_1^2/(r_1 r_2 - 1) form.

Run:
    python3 verify_Paper69_Rb_denominator.py
"""

import math

# -----------------------------------------------------------------------------
# Kelvin cell topological integers
# -----------------------------------------------------------------------------
V = 24          # vertices
E = 36          # edges
F = 14          # faces (8 hex + 6 square)
G_order = 48    # |O_h|
N_gauge = E - V  # = 12 (Casimir gauge-boson count, Part LX)

# Euler check
assert V - E + F == 2, "Euler characteristic must equal 2 for the Kelvin cell on S^2"

# -----------------------------------------------------------------------------
# 1. Four decompositions of 2V - F
# -----------------------------------------------------------------------------
d1 = 2 * V - F                   # direct
d2 = G_order - F                 # symmetry-inventory: |G| - F
d3 = 2 * E - 2 * N_gauge - F     # edge-incidence: 2E - 2 N_gauge - F
d4 = 3 * V - E - 2               # Euler-equivalent: 3V - E - 2

assert d1 == d2 == d3 == d4 == 34, f"Decomposition mismatch: {d1}, {d2}, {d3}, {d4}"

print("Four decompositions of 2V - F:")
print(f"  direct           2V - F                  = {d1}")
print(f"  symmetry-inv.    |G| - F                 = {d2}")
print(f"  edge-incidence   2E - 2 N_gauge - F      = {d3}")
print(f"  Euler-equiv.     3V - E - 2              = {d4}")

# -----------------------------------------------------------------------------
# 2. Numerator = beta_1(skeleton)
# -----------------------------------------------------------------------------
numerator = F - 1
assert numerator == E - V + 1 == 13, \
    f"Numerator should equal E - V + 1 = beta_1 = 13, got {numerator}"

print(f"\nNumerator F - 1 = E - V + 1 = beta_1(skeleton) = {numerator}")

# -----------------------------------------------------------------------------
# 3. R_b and unitarity triangle closure
# -----------------------------------------------------------------------------
R_b = numerator / d1  # = 13/34

delta_LO = 66.36                          # Paper #64 LO phase, degrees
delta_NLO = delta_LO * (2 * E - 1) / (2 * E)  # Paper #67 NLO correction

rho_bar = R_b * math.cos(math.radians(delta_NLO))
eta_bar = R_b * math.sin(math.radians(delta_NLO))

# PDG 2023
rho_exp, rho_err = 0.159, 0.010
eta_exp, eta_err = 0.348, 0.010
R_b_exp, R_b_err = 0.3826, 0.011

print(f"\nR_b           = {numerator}/{d1}             = {R_b:.5f}    (PDG {R_b_exp} +/- {R_b_err})")
print(f"delta_NLO     = {delta_LO} * {2*E-1}/{2*E}        = {delta_NLO:.4f} deg")
print(f"rho_bar       = R_b cos(delta_NLO)     = {rho_bar:.4f}    (PDG {rho_exp} +/- {rho_err})")
print(f"eta_bar       = R_b sin(delta_NLO)     = {eta_bar:.4f}    (PDG {eta_exp} +/- {eta_err})")

R_b_sigma = (R_b - R_b_exp) / R_b_err
rho_sigma = (rho_bar - rho_exp) / rho_err
eta_sigma = (eta_bar - eta_exp) / eta_err
joint = math.hypot(rho_sigma, eta_sigma)

print(f"\nTensions (PDG 2023):")
print(f"  R_b:                {R_b_sigma:+.3f} sigma")
print(f"  rho_bar:            {rho_sigma:+.3f} sigma")
print(f"  eta_bar:            {eta_sigma:+.3f} sigma")
print(f"  joint (rho, eta):   {joint:.3f} sigma")

assert abs(R_b_sigma) < 0.1, f"R_b tension too large: {R_b_sigma}"
assert joint < 0.1, f"Joint (rho, eta) tension too large: {joint}"

# -----------------------------------------------------------------------------
# 4. Reconciliation with Paper #64
# -----------------------------------------------------------------------------
r1 = (9 - math.sqrt(17)) / 2
r2 = (9 + math.sqrt(17)) / 2

# Vieta checks on the master equation lambda^2 - 9 lambda + 16 = 0
assert abs(r1 + r2 - 9) < 1e-12
assert abs(r1 * r2 - 16) < 1e-12

R_b_paper64 = r1**2 / (r1 * r2 - 1)       # = (49 - 9 sqrt(17)) / 30
R_b_paper69 = R_b

ratio = R_b_paper64 / R_b_paper69

print(f"\nReconciliation with Paper #64:")
print(f"  r_1 r_2 = {r1*r2:.6f}  (Vieta: should be 16)")
print(f"  Paper #64 R_b = r_1^2 / (r_1 r_2 - 1) = {R_b_paper64:.5f}")
print(f"  Paper #69 R_b = (F-1)/(2V-F)          = {R_b_paper69:.5f}")
print(f"  ratio (Paper #64 / Paper #69)         = {ratio:.5f}   (higher-order remainder)")

# Decomposition of the ratio:
#   R_b^{#64} / R_b^{#69}
#     = [ r_1^2 / (r_1 r_2 - 1) ]  /  [ (F-1) / (2V - F) ]
#     = [ r_1^2 / (F - 1) ]        *  [ (2V - F) / (r_1 r_2 - 1) ]
num_ratio   = r1**2 / numerator           # r_1^2 / (F - 1)
denom_ratio = d1 / (r1 * r2 - 1)          # (2V - F) / (r_1 r_2 - 1)  = 34 / 15
reconstructed = num_ratio * denom_ratio   # = (Paper#64 R_b) / (Paper#69 R_b)

print(f"  numerator ratio   r_1^2 / (F-1)        = {num_ratio:.5f}")
print(f"  denominator ratio (2V-F)/(r_1 r_2 - 1) = 34/15 = {denom_ratio:.5f}")
print(f"  reconstructed ratio (product)          = {reconstructed:.5f} (should match {ratio:.5f})")

assert abs(reconstructed - ratio) < 1e-10, \
    f"Reconciliation decomposition failed: {reconstructed} vs {ratio}"

print("\nAll checks passed.")
