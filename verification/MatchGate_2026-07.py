import numpy as np
from math import sqrt, pi, log
S17 = sqrt(17)
N = 20
c = np.arange(-N, N+1, dtype=float)
vals = (c[:,None] + c[None,:]*S17).ravel()
with np.errstate(divide='ignore', invalid='ignore'):
    R = (vals[:,None]/vals[None,:]).ravel()
R = R[np.isfinite(R)]
R = np.unique(np.round(R, 12))          # DISTINCT values only
print(f"distinct family values: {len(R):,}")

def hits(target, tol_rel):
    return int(np.count_nonzero(np.abs(R - target) <= abs(target)*tol_rel))

alpha = 1/(8*pi**2.5*(47/48 + 10/(3*48**3) + 22/(3*48**5)))
a = alpha
targets = [
    ("sin2_thetaW_eff", (17-3*S17)/20, 0.23153, 0.00016),
    ("mH_over_mZ", 18/(9+S17), 125.25/91.1876, 0.17/91.1876),
    ("tan2_theta12", S17/9, 0.4430, 0.0200),
    ("Koide_Q", 2/3, 0.666661, 0.000007),
    ("lambda_H_NLO", (120+S17)/960, 125.25**2/(2*246.21965**2), 2*0.17/125.25*0.12938),
    ("DM_ratio", 3*(1+2*sqrt(3))/2**(4/3), 5.36, 0.06),
    ("np_over_me", (6+S17)/4*(1+a*S17/360), 1.29333236/0.51099895, 1e-6/0.511),
    ("eta_B_x1e10", (a**3/648*(1+S17/220))*1e10, 6.104, 0.058),
    ("ln_MP_v", (122+45*S17)/8, log(1.220890e19/246.21965), 38.44*1.1e-5),
]
print(f"{'target':16s} {'nom sig':>8s} {'tol':>8s} {'distinct hits':>13s}  verdict (PASS<=3, CAUTION<=30, FAIL>30)")
for name, pred, exp, sig in targets:
    dev = abs(pred-exp)/sig
    tol = max(abs(pred-exp), sig)/abs(exp)
    h = hits(exp, tol)
    v = "PASS" if h<=3 else ("CAUTION" if h<=30 else "FAIL")
    print(f"{name:16s} {dev:7.2f}s {tol:8.1e} {h:13d}  {v}")
exp_a, sig_a = 137.035999046, 0.000000027
tol = max(abs(1/alpha-exp_a), sig_a)/exp_a
print(f"{'alpha_inv':16s} {abs(1/alpha-exp_a)/sig_a:7.2f}s {tol:8.1e} {hits(exp_a, tol):13d}  (alpha formula outside family; 0 rivals)")
