import FaceGraph.Theorem51
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp

/-!
# Proposition 4.1 of the note: the square weights of the eigenspaces

The square weight of an eigenspace `E` with orthogonal projector `P_E` is `tr(P_sq P_E) / tr(P_E)`, with `P_sq` the
coordinate projector on the six squares (`Psq` of `Theorem51.lean`). For the rational eigenvalues `0, 4, 7, 9` the
projectors are rational matrices; they are entered as literals and the kernel checks that each is a symmetric idempotent, that
`Lfin * P = λ P`, and that the traces are the multiplicities (so each is the orthogonal projector on a subspace of
the eigenspace of the right dimension; that the eigenspace has no more dimensions than the multiplicity is the
symmetric-matrix fact used in the note). `PT` is the projector on the six-dimensional `T1u` sector
`ker(L² - 9L + 16)`, and the five projectors sum to the identity. The weights are then `3/7, 1, 1/7, 0` and the
`T1u` sector as a whole has weight `1/2`.

For the two irrational eigenvalues the note's proof reduces to the `2 × 2` block `!![4, -4; -1, 5]`: for any root
`λ` of `x² - 9x + 16` in any field, `v = 4 s + (4 - λ) h` is an eigenvector of `Lfin` (checked here on the full
`14 × 14` matrix), its square part has squared norm `32` and its hexagon part `8 (4 - λ)²`, so the weight is
`4 / (4 + (4 - λ)²) = 4 / (4 + λ)`, which over a field with `s² = 17` and `λ = (9 ∓ s)/2` equals `(1 ± 1/s)/2`.
-/

open Matrix Polynomial

def P0 : Matrix (Fin 14) (Fin 14) ℚ :=
  !![1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14;
     1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14, 1/14]
def P4 : Matrix (Fin 14) (Fin 14) ℚ :=
  !![1/3, 1/3, -1/6, -1/6, -1/6, -1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     1/3, 1/3, -1/6, -1/6, -1/6, -1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     -1/6, -1/6, 1/3, 1/3, -1/6, -1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     -1/6, -1/6, 1/3, 1/3, -1/6, -1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     -1/6, -1/6, -1/6, -1/6, 1/3, 1/3, 0, 0, 0, 0, 0, 0, 0, 0;
     -1/6, -1/6, -1/6, -1/6, 1/3, 1/3, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def P7 : Matrix (Fin 14) (Fin 14) ℚ :=
  !![2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     2/21, 2/21, 2/21, 2/21, 2/21, 2/21, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, 3/7, -1/14, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, 3/7, -1/14, -1/14, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, 3/7, -1/14, -1/14, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, 3/7, -1/14, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14;
     -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7, -1/14, -1/14, -1/14, -1/14, -1/14, -1/14, 3/7]
def P9 : Matrix (Fin 14) (Fin 14) ℚ :=
  !![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, 1/8, -1/8, 1/8, -1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, 1/8, -1/8, 1/8, -1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, 1/8, -1/8, 1/8, -1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, 1/8, -1/8, 1/8, -1/8, -1/8, 1/8]
def PT : Matrix (Fin 14) (Fin 14) ℚ :=
  !![1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     -1/2, 1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, -1/2, 1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, -1/2, 1/2, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 3/8, 1/8, 1/8, -1/8, 1/8, -1/8, -1/8, -3/8;
     0, 0, 0, 0, 0, 0, 1/8, 3/8, -1/8, 1/8, -1/8, 1/8, -3/8, -1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, 3/8, 1/8, -1/8, -3/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, 1/8, 3/8, -3/8, -1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, -3/8, 3/8, 1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, -1/8, 1/8, -3/8, -1/8, 1/8, 3/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, -1/8, -3/8, 1/8, -1/8, 1/8, -1/8, 3/8, 1/8;
     0, 0, 0, 0, 0, 0, -3/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, 3/8]

/-- Square weight of a projector. -/
noncomputable def wsq (P : Matrix (Fin 14) (Fin 14) ℚ) : ℚ := (Psq * P).trace / P.trace

section projectors
lemma LP0 : Lfin * P0 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma LP4 : Lfin * P4 = 4 • P4 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma LP7 : Lfin * P7 = 7 • P7 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma LP9 : Lfin * P9 = 9 • P9 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma LPT : Lfin * (Lfin * PT) - 9 • (Lfin * PT) + 16 • PT = 0 := by
  rw [← Matrix.mulᵣ_eq, ← Matrix.mulᵣ_eq]; decide +kernel
lemma P0_idem : P0 * P0 = P0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P4_idem : P4 * P4 = P4 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P7_idem : P7 * P7 = P7 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P9_idem : P9 * P9 = P9 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma PT_idem : PT * PT = PT := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P0_symm : P0ᵀ = P0 := by decide +kernel
lemma P4_symm : P4ᵀ = P4 := by decide +kernel
lemma P7_symm : P7ᵀ = P7 := by decide +kernel
lemma P9_symm : P9ᵀ = P9 := by decide +kernel
lemma PT_symm : PTᵀ = PT := by decide +kernel
/-- Resolution of the identity. -/
lemma resolution : P0 + P4 + P7 + P9 + PT = 1 := by decide +kernel
lemma P0P4 : P0 * P4 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P0P7 : P0 * P7 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P0P9 : P0 * P9 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P0PT : P0 * PT = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P4P7 : P4 * P7 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P4P9 : P4 * P9 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P4PT : P4 * PT = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P7P9 : P7 * P9 = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P7PT : P7 * PT = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma P9PT : P9 * PT = 0 := by rw [← Matrix.mulᵣ_eq]; decide +kernel

/-- Traces: the multiplicities 1, 2, 4, 1, 6. -/
lemma tr_P0 : P0.trace = 1 := by norm_num [Matrix.trace, Fin.sum_univ_succ, P0]
lemma tr_P4 : P4.trace = 2 := by norm_num [Matrix.trace, Fin.sum_univ_succ, P4]
lemma tr_P7 : P7.trace = 4 := by norm_num [Matrix.trace, Fin.sum_univ_succ, P7]
lemma tr_P9 : P9.trace = 1 := by norm_num [Matrix.trace, Fin.sum_univ_succ, P9]
lemma tr_PT : PT.trace = 6 := by norm_num [Matrix.trace, Fin.sum_univ_succ, PT]

/-- Square traces. -/
lemma trsq_P0 : (Psq * P0).trace = 3 / 7 := by
  norm_num [Matrix.trace, Fin.sum_univ_succ, Matrix.mul_apply, Psq, P0, Matrix.diagonal]
lemma trsq_P4 : (Psq * P4).trace = 2 := by
  norm_num [Matrix.trace, Fin.sum_univ_succ, Matrix.mul_apply, Psq, P4, Matrix.diagonal]
lemma trsq_P7 : (Psq * P7).trace = 4 / 7 := by
  norm_num [Matrix.trace, Fin.sum_univ_succ, Matrix.mul_apply, Psq, P7, Matrix.diagonal]
lemma trsq_P9 : (Psq * P9).trace = 0 := by
  norm_num [Matrix.trace, Fin.sum_univ_succ, Matrix.mul_apply, Psq, P9, Matrix.diagonal]
lemma trsq_PT : (Psq * PT).trace = 3 := by
  norm_num [Matrix.trace, Fin.sum_univ_succ, Matrix.mul_apply, Psq, PT, Matrix.diagonal]

/-- **Proposition 4.1, rational part**: the square weights of `E_0, E_4, E_7, E_9` are `3/7, 1, 1/7, 0`, and the
`T1u` sector as a whole has weight `1/2`. -/
theorem weights : wsq P0 = 3 / 7 ∧ wsq P4 = 1 ∧ wsq P7 = 1 / 7 ∧ wsq P9 = 0 ∧ wsq PT = 1 / 2 := by
  unfold wsq
  rw [tr_P0, tr_P4, tr_P7, tr_P9, tr_PT, trsq_P0, trsq_P4, trsq_P7, trsq_P9, trsq_PT]
  norm_num
end projectors

section T1u
variable {F : Type*} [Field F]

/-- The `T1u` vector `4 s + (4 - λ) h` for the pair of columns `4, 5` of `Pfin` (`s = e₀ - e₁`, `h` the hexagon sign
pattern). -/
def vT1u (l : F) : Fin 14 → F := fun i => 4 * (Pfin i 4 : F) + (4 - l) * (Pfin i 5 : F)

/-- For every root `λ` of `x² - 9x + 16` in any field, `vT1u λ` is an eigenvector of `Lfin` with eigenvalue `λ`. -/
theorem vT1u_eig (l : F) (h : l ^ 2 - 9 * l + 16 = 0) :
    (Lfin.map ((↑) : ℚ → F)).mulVec (vT1u l) = l • vT1u l := by
  ext i
  fin_cases i <;>
    simp [Matrix.mulVec, dotProduct, Fin.sum_univ_succ, Lfin, Pfin, vT1u] <;>
    first | ring1 | linear_combination h | linear_combination -h

/-- Squared norm of the square part: `32`. -/
theorem vT1u_sq (l : F) : ∑ i : Fin 14, (if i.val < 6 then vT1u l i ^ 2 else 0) = 32 := by
  simp [Fin.sum_univ_succ, Pfin, vT1u]; norm_num
/-- Squared norm of the hexagon part: `8 (4 - λ)²`. -/
theorem vT1u_hx (l : F) : ∑ i : Fin 14, (if 6 ≤ i.val then vT1u l i ^ 2 else 0) = 8 * (4 - l) ^ 2 := by
  simp [Fin.sum_univ_succ, Pfin, vT1u]; ring

variable [CharZero F]

/-- The weight `32 / (32 + 8 (4 - λ)²)` equals `4 / (4 + λ)` on the roots, since `(4 - λ)² = λ` there. -/
theorem t1u_weight (l : F) (h : l ^ 2 - 9 * l + 16 = 0) (h4 : (4 : F) + l ≠ 0) :
    (32 : F) / (32 + 8 * (4 - l) ^ 2) = 4 / (4 + l) := by
  have e : (4 - l) ^ 2 = l := by linear_combination h
  rw [e, div_eq_div_iff (by intro h0; apply h4; linear_combination h0 / 8) h4]
  ring

/-- Over a field with `s² = 17`, `(9 - s)/2` and `(9 + s)/2` are the roots `r₁, r₂`. -/
theorem roots (s : F) (hs : s ^ 2 = 17) :
    ((9 - s) / 2) ^ 2 - 9 * ((9 - s) / 2) + 16 = 0 ∧ ((9 + s) / 2) ^ 2 - 9 * ((9 + s) / 2) + 16 = 0 := by
  constructor <;> linear_combination hs / 4

/-- **Proposition 4.1, `T1u` part**: `4 / (4 + r₁) = (1 + 1/s)/2` and `4 / (4 + r₂) = (1 - 1/s)/2`, `s = √17`. -/
theorem t1u_weights_sqrt (s : F) (hs : s ^ 2 = 17) :
    (4 : F) / (4 + (9 - s) / 2) = (1 + 1 / s) / 2 ∧ (4 : F) / (4 + (9 + s) / 2) = (1 - 1 / s) / 2 := by
  have hs0 : s ≠ 0 := by rintro rfl; norm_num at hs
  have h1 : (4 : F) + (9 - s) / 2 ≠ 0 := by
    intro h; have : s = 17 := by linear_combination -2 * h
    subst this; norm_num at hs
  have h2 : (4 : F) + (9 + s) / 2 ≠ 0 := by
    intro h; have : s = -17 := by linear_combination 2 * h
    subst this; norm_num at hs
  have hinv : 1 / s = s / 17 := by
    rw [div_eq_div_iff hs0 (by norm_num)]; linear_combination -hs
  rw [hinv]
  constructor
  · rw [div_eq_iff h1]; linear_combination hs / 68
  · rw [div_eq_iff h2]; linear_combination hs / 68
end T1u

#print axioms weights
#print axioms vT1u_eig
#print axioms t1u_weight
#print axioms t1u_weights_sqrt
