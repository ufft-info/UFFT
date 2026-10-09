import FaceGraph.Theorem31

/-!
# Half flux: the signless Laplacian (Theorem 6.4 of the note at q = 12), machine-checked

At flux π per plaquette the all-negative gauge turns the magnetic Laplacian into the signless Laplacian `Sfin = D + A`.
The same symmetry-adapted basis `Pfin` as for Theorem 3.1 brings it to a block diagonal with blocks
A1g [[4, 4], [3, 9]], Eg diag(4, 4), T1u [[4, 4], [1, 7]] × 3, T2g diag(5, 5) and (T2g, A2u) diag(5, 3).
-/

open Matrix Polynomial

def Sfin : Matrix (Fin 14) (Fin 14) ℚ :=
  !![4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0;
     0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1;
     0, 0, 4, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0;
     0, 0, 0, 4, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1;
     0, 0, 0, 0, 4, 0, 1, 0, 1, 0, 1, 0, 1, 0;
     0, 0, 0, 0, 0, 4, 0, 1, 0, 1, 0, 1, 0, 1;
     1, 0, 1, 0, 1, 0, 6, 1, 1, 0, 1, 0, 0, 0;
     1, 0, 1, 0, 0, 1, 1, 6, 0, 1, 0, 1, 0, 0;
     1, 0, 0, 1, 1, 0, 1, 0, 6, 1, 0, 0, 1, 0;
     1, 0, 0, 1, 0, 1, 0, 1, 1, 6, 0, 0, 0, 1;
     0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 6, 1, 1, 0;
     0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 6, 0, 1;
     0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 6, 1;
     0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 6]

def blkS : Fin 7 → Matrix (Fin 2) (Fin 2) ℚ :=
  ![!![4, 4; 3, 9], !![4, 0; 0, 4], !![4, 4; 1, 7], !![4, 4; 1, 7], !![4, 4; 1, 7], !![5, 0; 0, 5], !![5, 0; 0, 3]]

def BS : Matrix (Fin 14) (Fin 14) ℚ := Matrix.reindex e72 e72 (Matrix.blockDiagonal blkS)

lemma SP : Sfin * Pfin = Pfin * BS := by rw [← Matrix.mulᵣ_eq, ← Matrix.mulᵣ_eq]; decide +kernel

lemma S_conj : Sfin = Pfin * BS * Qfin := by
  calc Sfin = Sfin * (Pfin * Qfin) := by rw [PQ, mul_one]
    _ = (Sfin * Pfin) * Qfin := by rw [mul_assoc]
    _ = Pfin * BS * Qfin := by rw [SP]

lemma blkS0 : (blkS 0).charpoly = X ^ 2 - 13 * X + 24 := by
  rw [show blkS 0 = !![4, 4; 3, 9] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS1 : (blkS 1).charpoly = (X - 4) ^ 2 := by
  rw [show blkS 1 = !![4, 0; 0, 4] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS2 : (blkS 2).charpoly = (X - 3) * (X - 8) := by
  rw [show blkS 2 = !![4, 4; 1, 7] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS3 : (blkS 3).charpoly = (X - 3) * (X - 8) := by
  rw [show blkS 3 = !![4, 4; 1, 7] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS4 : (blkS 4).charpoly = (X - 3) * (X - 8) := by
  rw [show blkS 4 = !![4, 4; 1, 7] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS5 : (blkS 5).charpoly = (X - 5) ^ 2 := by
  rw [show blkS 5 = !![5, 0; 0, 5] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring
lemma blkS6 : (blkS 6).charpoly = (X - 5) * (X - 3) := by
  rw [show blkS 6 = !![5, 0; 0, 3] from rfl, cp2]; simp [Polynomial.C_ofNat]; ring

theorem charpoly_BS :
    BS.charpoly = (X - 8) ^ 3 * (X - 5) ^ 3 * (X - 4) ^ 2 * (X - 3) ^ 4 * (X ^ 2 - 13 * X + 24) := by
  unfold BS
  rw [Matrix.charpoly_reindex, charpoly_blockDiagonal, Fin.prod_univ_seven,
    blkS0, blkS1, blkS2, blkS3, blkS4, blkS5, blkS6]
  ring

/-- **Theorem 6.4 of the note, the half-flux case q = 12.** -/
theorem charpoly_Sfin :
    Sfin.charpoly = (X - 8) ^ 3 * (X - 5) ^ 3 * (X - 4) ^ 2 * (X - 3) ^ 4 * (X ^ 2 - 13 * X + 24) := by
  rw [S_conj, ← charpoly_BS]
  have h := Matrix.charpoly_units_conj Punit BS
  rw [← Matrix.coe_units_inv] at h
  exact h

#print axioms charpoly_Sfin
