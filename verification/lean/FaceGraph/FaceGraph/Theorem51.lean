import FaceGraph.Theorem31

/-!
# The inter-orbit operator K (Theorem 5.1 of the note), machine-checked on the orbit basis

`K = P_□ Δ P_⬡ - P_⬡ Δ P_□` with `P_□`, `P_⬡` the projections on the six square and eight hexagon coordinates.
The note's Theorem 5.1 is stated on the `O_h` isotypic components; here it is checked on the explicit rational basis
`Pfin` of Theorem 3.1 (columns: `1_□`, `1_⬡`; two `E_g` vectors; `(s_a, h_a)` for the three axes; three `T_{2g}` monomials;
the `A_{2u}` monomial), on which `K` acts by the block matrix `Kb`:

* `A_{1g}` plane, basis `(1_□, 1_⬡)`: `K 1_□ = 3·1_⬡`, `K 1_⬡ = -4·1_□`, so `K² = -12` there (Theorem 5.1 (4));
* `E_g`, `T_{2g}`, `A_{2u}` columns: `K = 0` (Theorem 5.1 (1));
* each `T_{1u}` plane, basis `(s_a, h_a)`: `K s_a = h_a`, `K h_a = -4 s_a`, so `K² = -4` there (Theorem 5.1 (2)).

Every identity is a product of explicit rational matrices and is decided by the kernel. What is checked here is the action
of `K` on this basis; the identification of the basis with the isotypic components is the group-theoretic part of the note
(Lemma 3.2), which is not formalised. Theorem 5.1 (3), the singular values of `K` between the two `T_{1u}` eigenspaces,
involves the irrational eigenvectors and is not formalised either.
-/

open Matrix

/-- Projection on the square coordinates (indices 0–5). -/
def Psq : Matrix (Fin 14) (Fin 14) ℚ := Matrix.diagonal ![1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
/-- Projection on the hexagon coordinates (indices 6–13). -/
def Phx : Matrix (Fin 14) (Fin 14) ℚ := Matrix.diagonal ![0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

/-- The inter-orbit operator of Section 5, as an explicit matrix: `-A_□⬡` in the square–hexagon block and
`+A_⬡□` in the hexagon–square block. -/
def K : Matrix (Fin 14) (Fin 14) ℚ :=
  !![0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1;
     0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, -1;
     0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0;
     0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1;
     1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0;
     0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

/-- `K` is the definition of Section 5: `K = P_□ Δ P_⬡ - P_⬡ Δ P_□`. -/
lemma K_def : K = Psq * Lfin * Phx - Phx * Lfin * Psq := by
  unfold K Psq Phx; simp only [← Matrix.mulᵣ_eq]; decide +kernel

/-- Blocks of `K` on the basis `Pfin`, in the block order of `blk`. -/
def kblk : Fin 7 → Matrix (Fin 2) (Fin 2) ℚ :=
  ![!![0, -4; 3, 0], 0, !![0, -4; 1, 0], !![0, -4; 1, 0], !![0, -4; 1, 0], 0, 0]
def Kb : Matrix (Fin 14) (Fin 14) ℚ := Matrix.reindex e72 e72 (Matrix.blockDiagonal kblk)

/-- Blocks of `K²`: `-12` on the `A_{1g}` plane, `-4` on each `T_{1u}` plane, `0` elsewhere. -/
def kblk2 : Fin 7 → Matrix (Fin 2) (Fin 2) ℚ :=
  ![!![-12, 0; 0, -12], 0, !![-4, 0; 0, -4], !![-4, 0; 0, -4], !![-4, 0; 0, -4], 0, 0]
def Kb2 : Matrix (Fin 14) (Fin 14) ℚ := Matrix.reindex e72 e72 (Matrix.blockDiagonal kblk2)

/-- `K` is antisymmetric. -/
lemma K_antisymm : Kᵀ = -K := by
  unfold K; decide +kernel

/-- `K` acts on the orbit basis by the blocks `kblk`: Theorem 5.1 (1), (2), (4) on explicit vectors. -/
theorem K_conj : K * Pfin = Pfin * Kb := by
  unfold K Kb; rw [← Matrix.mulᵣ_eq, ← Matrix.mulᵣ_eq]; decide +kernel

lemma Kb_sq : Kb * Kb = Kb2 := by
  unfold Kb Kb2; rw [← Matrix.mulᵣ_eq]; decide +kernel

/-- `K²` on the orbit basis: `-12` on `A_{1g}`, `-4` on `T_{1u}`, `0` on `E_g ⊕ T_{2g} ⊕ A_{2u}`. -/
theorem K_sq_conj : K * K * Pfin = Pfin * Kb2 := by
  rw [Matrix.mul_assoc, K_conj, ← Matrix.mul_assoc, K_conj, Matrix.mul_assoc, Kb_sq]

/-- `K 1₁₄ = -4·1_□ + 3·1_⬡`, which lies in the eigenvalue-7 eigenspace of `Δ` (Theorem 5.1 (1), last clause). -/
theorem K_one : K.mulVec (fun _ => 1) = ![-4, -4, -4, -4, -4, -4, 3, 3, 3, 3, 3, 3, 3, 3] := by
  unfold K; rw [← Matrix.mulVecᵣ_eq]; decide +kernel
theorem K_one_in_E7 :
    Lfin.mulVec (K.mulVec (fun _ => 1)) = (7 : ℚ) • K.mulVec (fun _ => 1) := by
  rw [K_one]; unfold Lfin; rw [← Matrix.mulVecᵣ_eq]; decide +kernel

#print axioms K_conj
#print axioms K_sq_conj
#print axioms K_one_in_E7
