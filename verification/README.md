# UFFT Verification Suite

Every quantitative claim in the UFFT corpus is intended to be reproducible
from the scripts in this directory. Each script is standalone, prints
PASS/FAIL per check where applicable, and exits nonzero on failure. If you
find a claim in a paper or in the canonical documents that is not covered
by a script here, that is a defect: please report it.

## Quick start

    pip install -r requirements.txt      # numpy, sympy, scipy
    python UFFT_Master_Verification_v10.py

Python 3.10+. No network access required. Runtimes on a laptop range from
seconds to about one minute per script.

## Core scripts

| Script | Verifies | Runtime |
|---|---|---|
| `UFFT_Master_Verification_v10.py` | The main observable table: sigma-values computed fresh from cell integers against quoted experimental values | ~10 s |
| `19079730_UFFT_Spectrum_Verification.py` | The face-adjacency graph, its Laplacian spectrum {0, r1^3, 4^2, r2^3, 7^4, 9}, and the O_h irrep decomposition | ~5 s |
| `face_laplacian_matrix.py` | Explicit 14x14 face-adjacency matrix A and L = D - A with Paper #63 face labels (hexagons 1-8, squares 9-14); prints both and checks the spectrum | ~1 s |
| `MatchGate_2026-07.py` | The rival-count gate for numerical matches: for each claimed match, how many distinct cell-integer expressions land within 1 sigma at the achieved accuracy. PASS/FAIL verdicts here are recorded properties of the claims, not script errors | ~1 min |
| `verify_FtF_audit_2026-07.py` | The 2026-07 audit corrections to the book and Core Framework (torsion operator split, sum rules, term sizes) | ~10 s |

## Paper-specific verifiers

| Script | Paper |
|---|---|
| `Paper68_Reconciliation_Theorem.py` | #68 cell-integer identities and the single-cell obstruction |
| `verify_Paper48_irrep_block_O_k2_fit.py` | #48 irrep block structure |
| `verify_Paper69_Rb_denominator.py` | #69 R_b denominator from operator perturbation theory |
| `verify_Paper70_interior_projector.py` | #70 interior-projector 6/7 identity |
| `verify_Paper71_solar_angle_NLO.py` | #71 solar-angle NLO self-energy |
| `verify_Paper72_Oh_irreps.py` | #72 Dirac operator, generation count, Pauli structure |
| `Quark_Walk_Action_Reproducibility.py` | quark walk-action exponents |
| `Symanzik_Matching_BCC.py` | lattice-to-continuum matching orders |

## Open-problem verifiers (negative results and constraints)

| Script | Content |
|---|---|
| `verify_Weinberg_obstruction_2026-07.py` | 44 checks around the open Weinberg mixing-weight derivation (Paper #58 v2 Result 58.3): exact identities and structural lemmas, obstruction theorems that exclude entire construction classes (rationality of gap-cancelled responses, boson-sector field content, time-reversal-invariant seas, Galois band conjugacy), and error checks on published forms. The derivation itself remains open; these checks pin down where it cannot live | ~40 s |
| `verify_foam_hydrogen_deviation_2026-07.py` | The foam-vs-Coulomb bound-state deviation: image-free lattice-minus-continuum comparator, suppression exponent p = 2 with its analytic contact mechanism, solver cross-checks. Supersedes an earlier scan whose sign was wrong (documented inside) | ~40 s |
| `verify_void_protection_2026-07-03.py` | The void-protection theorem: the fermion band minimum at each zone face-center is void-invariant in energy (r1) and eigenvector (pure-L, n_z = -1/sqrt17) for arbitrary void couplings; three face-centers give three protected vacua (the generation triad, pairwise overlaps 1/2, Bargmann +1/8) | ~1 min |
| `verify_weinberg_triad_normalization_2026-07-03.py` | The Galois-even half of Result 58.3 derived from the void triad: Delta+C_A = Delta(1+sum_gen n_z^2) = 20 with C_A = N_gen = 3 (void-invariant), plus P14 (single-particle chirality expectation vanishes on both Galois branches, so the odd numerator C_A*sqrt(Delta) is not in triad geometry and needs the chiral filling). Denominator derived; odd numerator still open | ~20 s |
| `verify_me_walk_firstorder_exclusion_2026-07-03.py` | Paper #74 C74.4 (m_e walk action): the first-order walk class is excluded (per-step action s* = 2.3827 is not ln of any single-step rate; it is quadratic in the T1u spectral spread, hence a two-step/second-order amplitude), plus two Tier-1 lemmas (step count = cycle rank - 1; denominator 16 = Vieta product r1 r2). C74.4 stays Tier 4 | ~10 s |
| `verify_ml3_irreducible_2026-07-03.py` | ML3 capstone: the B+V=D coupling is irreducible. The Dirac vacuum energy E_vac(m) = -sum sqrt(|d|^2+m^2) runs away monotonically in the condensate depth m, so least-energy / zero-point alone picks no finite condensate; only the interaction cost m^2/2g stabilises it and the minimum tracks g. Proves that the condensate magnitude is irreducibly the B+V=D four-fermion coupling - the axiom fixes the chiral phase but not its size (FtF line 635, "single physical input", now proven at the mechanism level) | ~40 s |
| `verify_foam_helium_2026-07-03.py` | Substrate-direct helium: the two-electron ground state from foam alpha+m_e reaches -77.49 eV variational (98.1% of experiment -79.005), first ionization 24.58 vs 24.59 eV. The e-e repulsion and nucleus-electron attraction are the same A1g channel (one coupling alpha), so the repulsion strength is forced, not fitted. Multi-electron correlation is standard QM on foam constants; conditional on alpha (sound) + m_e (gap A2) | ~1 s |
| `verify_ml3_coupling_2026-07-03.py` | ML3 step 3 (rev2, corrected after self-audit). The earlier "near-critical / couplings straddle g_c" claim is WITHDRAWN as dimensionally unsound (Y is a dimensionless coupling, T^2 is energy^2, g_c is energy - not commensurate). What stands: g_c ~ mean|d| = the fermion gap is near-tautological; the foam's four-fermion torsion coupling in consistent units is UNDETERMINED (needs the B+V=D vertex, which the corpus treats axiomatically, FtF line 635). Steps 1-2 (no-go + threshold) stand; step 3 does not decide the phase | ~1 s |
| `explore_ml3_audit_fullchern_2026-07-03.py` | Robustness audit of ML3 step 1: the full multi-band (non-abelian) Chern of the occupied T1u subspace on the full 14-dim H(k) is 0 for all torsion values - confirms the single-particle no-go is NOT a 2x2-projection artifact | ~1 min |
| `verify_ml3_njl_2026-07-03.py` | ML3 step 2 (interaction-driven chirality). The canonical Nambu-Jona-Lasinio mechanism for generating the torsion condensate <T>: torsion susceptibility chi = mean(1/|d|) is finite (gapped), so a critical coupling g_c = 1/chi ~ 2.06 exists; the NJL gap equation gives chiral-symmetric below g_c and a torsion condensate above. g_c ~ mean|d| ~ |T| = 2 (near-flat band), so the foam sits near its own critical coupling (suggestive, not claimed). Open (step 3): the foam's actual torsion coupling from the B+V=D vertex, and whether it exceeds g_c | ~30 s |
| `verify_ml3_chirality_2026-07-03.py` | ML3 (the chiral vacuum; the A1-Weinberg odd part and the Paper #59 chiral-fermion problem are one object). The foam T1u chirality is NOT band-topological: the single-particle Bloch block is real (d_y=0) and gapped (no Dirac points), and the Chern number is 0 for every single-particle torsion term (uniform mass and Wilson k-dependent alike; the Wilson curvature cancels in +-pairs, Nielsen-Ninomiya). Single-particle topology is ruled out; the chirality is necessarily interaction-driven, order parameter = the inter-type torsion condensate <T>. Geometric root of the P4-P14 obstruction chain | ~30 s |
| `verify_higgs_quartic_2026-07-03.py` | B1/B2 (Higgs quartic), reconciled with book Section 12.3: lambda_tree = 1/F_hx = 1/8 (the forced on-site A2u quartic) plus the universal NLO sqrtD/((V-F)(E-V)) = sqrt17/120 gives lambda = (120+sqrt17)/960 = 0.12930 at -0.25 sigma. Match-Gate FAIL-standalone (214 rivals); weight rests on the universal sqrtD/N overdetermination. The earlier -2/147 A1g7-exchange "bare quartic" framing is withdrawn (it is a distinct sub-channel, not the NLO) | ~5 s |

## Exploration scripts

`explore_*.py` are research working scripts (lattice Green's functions,
defect interactions, foam-hydrogen solvers, unit map). They reproduce the
exploratory results they document, including headers noting where earlier
findings were corrected. They are kept as run, not polished.

## Conventions

Faces of the truncated octahedron are indexed 0-5 (squares, along +-x,
+-y, +-z) and 6-13 (hexagons, sign octants). The face Laplacian is
L = D - A on the face-adjacency graph (24 square-hexagon adjacencies,
12 hexagon-hexagon). r1, r2 denote (9 -+ sqrt(17))/2. Experimental values
are quoted in-script with their sources (PDG, CODATA, Planck) so every
sigma is auditable.
