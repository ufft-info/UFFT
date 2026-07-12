"""
Verification script for UFFT Paper #71.

The PMNS solar angle NLO from gauge-loop self-energy shifts on the T1u
eigenvalue pair of the truncated-octahedron face-Laplacian spectrum.

Checks:
  1. Cell-integer identities for V, E, F, N_gauge (Euler characteristic).
  2. Three independent decompositions of the NLO denominator 144.
  3. Vieta identities from the master equation lambda^2 - 9 lambda + 16 = 0.
  4. LO formula tan^2 theta_12 = (r2 - r1) / (r1 + r2) = sqrt(17)/9.
  5. Symmetric shift r1 -> r1 + eps, r2 -> r2 - eps preserves the Vieta sum.
  6. NLO formula tan^2 theta_12 = (sqrt(17)/9)(1 - sqrt(17)/144) identity.
  7. Residuals vs PDG 2024 global fit: LO +0.56 sigma, NLO +0.074 sigma.
  8. 2-epsilon factor emerges from symmetric-splitting geometry (144 = 288/2).

Run:
    python3 verify_Paper71_solar_angle_NLO.py

Runtime: ~instant. Standard library only (math module).
"""

import math

# -----------------------------------------------------------------------------
# 1. Cell-integer identities
# -----------------------------------------------------------------------------
V = 24           # vertices
E = 36           # edges
F = 14           # faces
F_hx = 8         # hexagonal faces
F_sq = 6         # square faces
G_order = 48     # |O_h|
Delta = 17       # master discriminant
C_A = 3          # colour number

assert V - E + F == 2, "Euler characteristic must equal 2"
assert F_hx + F_sq == F, "Face count mismatch"

N_gauge = E - V  # Paper #60 Part LX: non-trivial vertex-walk irreps
assert N_gauge == 12, f"N_gauge should be 12, got {N_gauge}"

print("Cell-integer identities:")
print(f"  V = {V}, E = {E}, F = {F}  (Euler: V - E + F = {V - E + F})")
print(f"  F_hx = {F_hx}, F_sq = {F_sq}")
print(f"  N_gauge = E - V = {N_gauge}  (8 gluons + W+ + W- + Z + gamma)")
print(f"  Delta = {Delta} (master discriminant)")
print(f"  C_A = {C_A}")

# -----------------------------------------------------------------------------
# 2. Three decompositions of the NLO denominator 144
# -----------------------------------------------------------------------------
d1 = V * N_gauge // 2          # loop-combinatorial: (vertex insertions x gauge species) / 2
d2 = (E - V) ** 2              # gauge-pair: N_gauge^2
d3 = V * F_sq                  # vertex x square-face

assert d1 == d2 == d3 == 144, f"144 decomposition mismatch: {d1}, {d2}, {d3}"

print("\nThree decompositions of NLO denominator 144:")
print(f"  loop-combinatorial  V * N_gauge / 2  = {V}*{N_gauge}/2 = {d1}")
print(f"  gauge-pair product  (E - V)^2        = {E-V}^2    = {d2}")
print(f"  vertex x squares    V * F_sq         = {V}*{F_sq}     = {d3}")

# -----------------------------------------------------------------------------
# 3. Vieta identities from master equation lambda^2 - 9 lambda + 16 = 0
# -----------------------------------------------------------------------------
r1 = (9 - math.sqrt(Delta)) / 2
r2 = (9 + math.sqrt(Delta)) / 2

sum_r = r1 + r2
diff_r = r2 - r1
prod_r = r1 * r2

assert abs(sum_r - 9) < 1e-12, f"Vieta sum: {sum_r} != 9"
assert abs(diff_r - math.sqrt(Delta)) < 1e-12, f"Vieta diff: {diff_r} != sqrt(17)"
assert abs(prod_r - 16) < 1e-12, f"Vieta product: {prod_r} != 16"
assert abs(sum_r - C_A ** 2) < 1e-12, f"Sum should equal C_A^2 = 9"
assert abs(prod_r - (F + 2)) < 1e-12, f"Product should equal F + 2 = 16"

print("\nVieta identities (master equation lambda^2 - 9 lambda + 16 = 0):")
print(f"  r1 = (9 - sqrt(17))/2 = {r1:.6f}   (lower T1u, left-chirality)")
print(f"  r2 = (9 + sqrt(17))/2 = {r2:.6f}   (upper T1u, right-chirality)")
print(f"  r1 + r2  = {sum_r}   (= C_A^2)")
print(f"  r2 - r1  = {diff_r:.6f}   (= sqrt(Delta))")
print(f"  r1 * r2  = {prod_r}   (= F + 2)")

# -----------------------------------------------------------------------------
# 4. LO formula tan^2 theta_12 = (r2 - r1)/(r1 + r2) = sqrt(17)/9
# -----------------------------------------------------------------------------
tan2_LO = (r2 - r1) / (r1 + r2)
closed_form_LO = math.sqrt(Delta) / (C_A ** 2)
assert abs(tan2_LO - closed_form_LO) < 1e-12, "LO closed form mismatch"

print("\nLO solar angle (Paper #35):")
print(f"  tan^2 theta_12^LO = (r2 - r1)/(r1 + r2) = sqrt({Delta})/{C_A**2} = {tan2_LO:.5f}")

# -----------------------------------------------------------------------------
# 5. Self-energy shift epsilon = Delta / (V * N_gauge)
# -----------------------------------------------------------------------------
eps = Delta / (V * N_gauge)   # 17 / 288
assert abs(eps * 2 - math.sqrt(Delta) / 144 * math.sqrt(Delta)) < 1e-12 or \
       abs(2 * eps * (C_A ** 2) / math.sqrt(Delta) - math.sqrt(Delta) / 144) < 1e-12

print(f"\nOne-loop self-energy shift:")
print(f"  epsilon = Delta / (V * N_gauge) = {Delta}/{V*N_gauge} = {eps:.6f}")

# Symmetric shifts preserve Vieta sum exactly
r1_nlo = r1 + eps
r2_nlo = r2 - eps
sum_nlo = r1_nlo + r2_nlo
diff_nlo = r2_nlo - r1_nlo

assert abs(sum_nlo - 9) < 1e-12, f"Vieta sum NOT preserved by symmetric shift: {sum_nlo}"
print(f"  r1 -> r1 + eps = {r1_nlo:.6f}")
print(f"  r2 -> r2 - eps = {r2_nlo:.6f}")
print(f"  r1_nlo + r2_nlo = {sum_nlo} (Vieta sum preserved exactly)")
print(f"  r2_nlo - r1_nlo = {diff_nlo:.6f} (splitting shrunk by 2*eps)")

assert abs(diff_nlo - (math.sqrt(Delta) - 2 * eps)) < 1e-12

# -----------------------------------------------------------------------------
# 6. NLO formula tan^2 theta_12 = (sqrt(17)/9)(1 - sqrt(17)/144)
# -----------------------------------------------------------------------------
tan2_NLO_direct = (r2_nlo - r1_nlo) / (r1_nlo + r2_nlo)
tan2_NLO_formula = (math.sqrt(Delta) / (C_A ** 2)) * (1 - math.sqrt(Delta) / 144)
tan2_NLO_factored = (math.sqrt(Delta) - 2 * eps) / 9

assert abs(tan2_NLO_direct - tan2_NLO_formula) < 1e-12, \
    f"NLO direct vs formula mismatch: {tan2_NLO_direct} vs {tan2_NLO_formula}"
assert abs(tan2_NLO_direct - tan2_NLO_factored) < 1e-12

print("\nNLO solar angle (this paper):")
print(f"  tan^2 theta_12^NLO (direct)   = (r2_nlo - r1_nlo)/9 = {tan2_NLO_direct:.6f}")
print(f"  tan^2 theta_12^NLO (factored) = (sqrt(17)/9)(1 - sqrt(17)/144) = {tan2_NLO_formula:.6f}")
print(f"  All three computations agree to machine precision.")

# -----------------------------------------------------------------------------
# 7. Residuals vs PDG 2024
# -----------------------------------------------------------------------------
obs = 0.443
err = 0.027

sigma_LO = (tan2_LO - obs) / err
sigma_NLO = (tan2_NLO_direct - obs) / err
tightening = abs(sigma_LO) / abs(sigma_NLO)

print("\nResiduals vs PDG 2024 global fit (tan^2 theta_12 = 0.443 +/- 0.027):")
print(f"  LO   : {tan2_LO:.5f}  -> {sigma_LO:+.3f} sigma")
print(f"  NLO  : {tan2_NLO_direct:.5f}  -> {sigma_NLO:+.3f} sigma")
print(f"  Tightening factor: {tightening:.1f}x")

assert abs(sigma_NLO) < 0.2, f"NLO residual too large: {sigma_NLO} sigma"
assert tightening > 5, f"Tightening insufficient: {tightening}x"

# -----------------------------------------------------------------------------
# 8. Product identity under NLO shift
# -----------------------------------------------------------------------------
prod_nlo = r1_nlo * r2_nlo
prod_predicted = 16 + eps * math.sqrt(Delta) - eps ** 2
assert abs(prod_nlo - prod_predicted) < 1e-12, \
    f"Product identity failed: {prod_nlo} vs {prod_predicted}"

print(f"\nNLO product identity (separate prediction):")
print(f"  (r1+eps)(r2-eps) = {prod_nlo:.6f}")
print(f"  = 16 + eps*sqrt(17) - eps^2 = {prod_predicted:.6f}  (algebraic check)")

print("\nAll checks passed.")
