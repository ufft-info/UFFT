import Mathlib.LinearAlgebra.Matrix.Charpoly.Basic
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Block
import Mathlib.Data.Matrix.Block
import Mathlib.Data.Matrix.Reflection
import Mathlib.Logic.Equiv.Fin.Basic

/-!
# The face-adjacency graph of the truncated octahedron: Theorem 3.1, machine-checked

`Lfin` is the combinatorial Laplacian of the face graph Γ (faces 0..5 the squares +x,-x,+y,-y,+z,-z;
faces 6..13 the hexagons in the order of `itertools.product([1,-1], repeat=3)`), exactly as in the note
and in `verification/verify_face_graph_paper_2026-10-06.py`.

The proof follows the note's own argument: a change of basis `Pfin` to the symmetry-adapted basis
(orbit sums, the Eg pair, the three T1u pairs, the T2g triple and the A2u singlet) brings `Lfin` to the block
diagonal `Bfin` with seven 2 × 2 blocks, and the characteristic polynomial of a block diagonal matrix is the
product of the blocks' characteristic polynomials.
-/

open Matrix Polynomial

def Lfin : Matrix (Fin 14) (Fin 14) ℚ :=
  !![4, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0;
     0, 4, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1;
     0, 0, 4, 0, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0;
     0, 0, 0, 4, 0, 0, 0, 0, -1, -1, 0, 0, -1, -1;
     0, 0, 0, 0, 4, 0, -1, 0, -1, 0, -1, 0, -1, 0;
     0, 0, 0, 0, 0, 4, 0, -1, 0, -1, 0, -1, 0, -1;
     -1, 0, -1, 0, -1, 0, 6, -1, -1, 0, -1, 0, 0, 0;
     -1, 0, -1, 0, 0, -1, -1, 6, 0, -1, 0, -1, 0, 0;
     -1, 0, 0, -1, -1, 0, -1, 0, 6, -1, 0, 0, -1, 0;
     -1, 0, 0, -1, 0, -1, 0, -1, -1, 6, 0, 0, 0, -1;
     0, -1, -1, 0, -1, 0, -1, 0, 0, 0, 6, -1, -1, 0;
     0, -1, -1, 0, 0, -1, 0, -1, 0, 0, -1, 6, 0, -1;
     0, -1, 0, -1, -1, 0, 0, 0, -1, 0, -1, 0, 6, -1;
     0, -1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, -1, 6]
def Pfin : Matrix (Fin 14) (Fin 14) ℚ :=
  !![1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0;
     1, 0, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, -2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0;
     1, 0, 0, -2, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0;
     0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1;
     0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 1, -1, -1, -1;
     0, 1, 0, 0, 0, 1, 0, -1, 0, 1, -1, -1, 1, -1;
     0, 1, 0, 0, 0, 1, 0, -1, 0, -1, -1, 1, -1, 1;
     0, 1, 0, 0, 0, -1, 0, 1, 0, 1, -1, 1, -1, -1;
     0, 1, 0, 0, 0, -1, 0, 1, 0, -1, -1, -1, 1, 1;
     0, 1, 0, 0, 0, -1, 0, -1, 0, 1, 1, -1, -1, 1;
     0, 1, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1, -1]
def Qfin : Matrix (Fin 14) (Fin 14) ℚ :=
  !![1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8;
     1/4, 1/4, -1/4, -1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1/12, 1/12, 1/12, 1/12, -1/6, -1/6, 0, 0, 0, 0, 0, 0, 0, 0;
     1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1/8, 1/8, 1/8, 1/8, -1/8, -1/8, -1/8, -1/8;
     0, 0, 1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1/8, 1/8, -1/8, -1/8, 1/8, 1/8, -1/8, -1/8;
     0, 0, 0, 0, 1/2, -1/2, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, 1/8, -1/8, 1/8, -1/8, 1/8, -1/8;
     0, 0, 0, 0, 0, 0, 1/8, 1/8, -1/8, -1/8, -1/8, -1/8, 1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, 1/8, -1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8;
     0, 0, 0, 0, 0, 0, 1/8, -1/8, -1/8, 1/8, -1/8, 1/8, 1/8, -1/8]

/-- The seven 2 × 2 blocks: A1g (orbit sums), Eg, T1u × 3, T2g pair, and (T2g, A2u). -/
def blk : Fin 7 → Matrix (Fin 2) (Fin 2) ℚ :=
  ![!![4, -4; -3, 3], !![4, 0; 0, 4], !![4, -4; -1, 5], !![4, -4; -1, 5], !![4, -4; -1, 5],
    !![7, 0; 0, 7], !![7, 0; 0, 9]]

/-- `Matrix.blockDiagonal` puts the block index second, so the index type is `Fin 2 × Fin 7`; the equivalence
`(i, k) ↦ i + 2k` places block `k` at rows and columns `2k, 2k + 1` of `Fin 14`. -/
def e72 : Fin 2 × Fin 7 ≃ Fin 14 := (Equiv.prodComm (Fin 2) (Fin 7)).trans finProdFinEquiv

/-- The block diagonal form on `Fin 14`. -/
def Bfin : Matrix (Fin 14) (Fin 14) ℚ := Matrix.reindex e72 e72 (Matrix.blockDiagonal blk)

/-- The three finite identities behind the change of basis. -/
lemma LP : Lfin * Pfin = Pfin * Bfin := by rw [← Matrix.mulᵣ_eq, ← Matrix.mulᵣ_eq]; decide +kernel
lemma PQ : Pfin * Qfin = 1 := by rw [← Matrix.mulᵣ_eq]; decide +kernel
lemma QP : Qfin * Pfin = 1 := by rw [← Matrix.mulᵣ_eq]; decide +kernel

def Punit : (Matrix (Fin 14) (Fin 14) ℚ)ˣ := ⟨Pfin, Qfin, PQ, QP⟩

lemma L_conj : Lfin = Pfin * Bfin * Qfin := by
  calc Lfin = Lfin * (Pfin * Qfin) := by rw [PQ, mul_one]
    _ = (Lfin * Pfin) * Qfin := by rw [mul_assoc]
    _ = Pfin * Bfin * Qfin := by rw [LP]

/-- Characteristic polynomial of a block diagonal matrix. -/
lemma charpoly_blockDiagonal {o n R : Type*} [Fintype o] [DecidableEq o] [Fintype n] [DecidableEq n]
    [CommRing R] (M : o → Matrix n n R) :
    (Matrix.blockDiagonal M).charpoly = ∏ k, (M k).charpoly := by
  unfold Matrix.charpoly
  rw [← Matrix.det_blockDiagonal]
  congr 1
  ext ⟨i, k⟩ ⟨j, l⟩
  by_cases hk : k = l
  · subst hk
    by_cases hij : i = j
    · subst hij; simp [Matrix.blockDiagonal_apply]
    · simp [Matrix.blockDiagonal_apply, hij]
  · simp [Matrix.blockDiagonal_apply, hk, Prod.ext_iff]

/-- Characteristic polynomial of an explicit rational 2 × 2 matrix. -/
lemma cp2 (a b c d : ℚ) :
    (!![a, b; c, d] : Matrix (Fin 2) (Fin 2) ℚ).charpoly = X ^ 2 - C (a + d) * X + C (a * d - b * c) := by
  rw [Matrix.charpoly_fin_two]
  simp [Matrix.trace_fin_two, Matrix.det_fin_two]

lemma blk0 : (blk 0).charpoly = X * (X - 7) := by
  rw [show blk 0 = !![4, -4; -3, 3] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk1 : (blk 1).charpoly = (X - 4) ^ 2 := by
  rw [show blk 1 = !![4, 0; 0, 4] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk2 : (blk 2).charpoly = X ^ 2 - 9 * X + 16 := by
  rw [show blk 2 = !![4, -4; -1, 5] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk3 : (blk 3).charpoly = X ^ 2 - 9 * X + 16 := by
  rw [show blk 3 = !![4, -4; -1, 5] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk4 : (blk 4).charpoly = X ^ 2 - 9 * X + 16 := by
  rw [show blk 4 = !![4, -4; -1, 5] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk5 : (blk 5).charpoly = (X - 7) ^ 2 := by
  rw [show blk 5 = !![7, 0; 0, 7] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blk6 : (blk 6).charpoly = (X - 7) * (X - 9) := by
  rw [show blk 6 = !![7, 0; 0, 9] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring

theorem charpoly_Bfin :
    Bfin.charpoly = X * (X - 9) * (X - 7) ^ 4 * (X - 4) ^ 2 * (X ^ 2 - 9 * X + 16) ^ 3 := by
  unfold Bfin
  rw [Matrix.charpoly_reindex, charpoly_blockDiagonal, Fin.prod_univ_seven,
    blk0, blk1, blk2, blk3, blk4, blk5, blk6]
  ring

/-- **Theorem 3.1 of the note.** -/
theorem charpoly_Lfin :
    Lfin.charpoly = X * (X - 9) * (X - 7) ^ 4 * (X - 4) ^ 2 * (X ^ 2 - 9 * X + 16) ^ 3 := by
  rw [L_conj, ← charpoly_Bfin]
  have h := Matrix.charpoly_units_conj Punit Bfin
  rw [← Matrix.coe_units_inv] at h
  exact h

#print axioms charpoly_Lfin
