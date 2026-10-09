import FaceGraph.Theorem31
import FaceGraph.HalfFlux
import FaceGraph.QuarterFlux

/-!
# The bridge from the graph to the literal matrices (ninth review round, R2)

The other files prove statements about hand-entered matrices. This file defines the face-adjacency graph of the
truncated octahedron by its rules (Proposition 2.1 of the note) and the quarter-flux gauge (B) by its formula
(Section 6.1), builds the Laplacian, the signless Laplacian and the gauge-(B) magnetic Laplacian from those
definitions, and proves that they are the literal matrices `Lfin`, `Sfin` and `D6` of the other files. Every proof is
`decide +kernel`: the kernel evaluates both sides on all 14 × 14 index pairs.

Conventions (the same as the note and the scripts): vertex `v : Fin 14`; `v < 6` is the square `(a, σ)` with axis
`a = v / 2` and sign `σ = +1` for even `v`, `-1` for odd `v`; `6 ≤ v` is the hexagon `h = v - 6 ∈ {0, …, 7}` with
sign vector `(h₀, h₁, h₂)`, `hⱼ = +1` when the corresponding bit of `h` is 0, in the order of
`itertools.product([1, -1], repeat = 3)` (bit 2 for `h₀`, bit 1 for `h₁`, bit 0 for `h₂`).

Adjacency (Proposition 2.1): a square `(a, σ)` is adjacent to the four hexagons with `h_a = σ`; two hexagons are
adjacent when their sign vectors differ in exactly one coordinate; squares are never adjacent to squares.

Gauge (B) (Section 6.1): on the hexagon–hexagon edges the phase is 1 (the connection is flat on the cube); on the
square–hexagon edge `(a, σ) – h` the entry of the magnetic adjacency is `B = (h_b - iσ h_c)/(1 - iσ)` with
`(a, b, c)` cyclic, which equals `(h_b + h_c)/2 + iσ (h_b - h_c)/2`; the magnetic Laplacian has `-B` in the
square row and `-B̄` in the hexagon row.
-/

open Matrix

/-- Sign `hⱼ` of hexagon `h` (0–7) in coordinate `j` (0–2). -/
def hs (h j : ℕ) : ℤ := if (h / 2 ^ (2 - j)) % 2 = 0 then 1 else -1

/-- Square `s` (0–5): axis `s / 2`, sign `+1` for even `s`. -/
def sqAxis (s : ℕ) : ℕ := s / 2
def sqSign (s : ℕ) : ℤ := if s % 2 = 0 then 1 else -1

/-- Square `s` is adjacent to hexagon `h` when `h` carries the square's sign in the square's axis. -/
def sqHexAdj (s h : ℕ) : Bool := hs h (sqAxis s) = sqSign s

/-- Two hexagons are adjacent when their sign vectors differ in exactly one coordinate. -/
def hexHexAdj (h h' : ℕ) : Bool :=
  ((List.range 3).filter (fun j => hs h j ≠ hs h' j)).length = 1

/-- The adjacency rule on vertex indices 0–13. -/
def adjN (v w : ℕ) : Bool :=
  if v < 6 ∧ 6 ≤ w then sqHexAdj v (w - 6)
  else if 6 ≤ v ∧ w < 6 then sqHexAdj w (v - 6)
  else if 6 ≤ v ∧ 6 ≤ w then hexHexAdj (v - 6) (w - 6)
  else false

/-- The adjacency matrix of Γ built from the rule. -/
def Agraph : Matrix (Fin 14) (Fin 14) ℚ := fun v w => if adjN v.val w.val then 1 else 0

/-- Degrees: 4 on the squares, 6 on the hexagons. -/
def degv (v : Fin 14) : ℚ := if v.val < 6 then 4 else 6

/-- The adjacency matrix is symmetric. -/
theorem Agraph_symm : Agraphᵀ = Agraph := by decide +kernel

/-- The row sums of the rule-built adjacency matrix are the degrees 4⁶ 6⁸ (36 edges). -/
theorem Agraph_degrees : Agraph.mulVecᵣ (fun _ => 1) = degv := by decide +kernel

/-- The Laplacian built from the rule. -/
def Lgraph : Matrix (Fin 14) (Fin 14) ℚ := Matrix.diagonal degv - Agraph
/-- The signless Laplacian built from the rule. -/
def Sgraph : Matrix (Fin 14) (Fin 14) ℚ := Matrix.diagonal degv + Agraph

/-- **Bridge for Theorem 3.1**: the rule-built Laplacian is the literal `Lfin`. -/
theorem Lgraph_eq_Lfin : Lgraph = Lfin := by decide +kernel

/-- **Bridge for Theorem 6.4 at q = 12**: the rule-built signless Laplacian is the literal `Sfin`. -/
theorem Sgraph_eq_Sfin : Sgraph = Sfin := by decide +kernel

/-! ## The quarter-flux gauge (B) -/

/-- Real part of `B` on the square–hexagon edge `(s, h)`: `(h_b + h_c)/2` with `(a, b, c)` cyclic. -/
def Bre (s h : ℕ) : ℤ := (hs h ((sqAxis s + 1) % 3) + hs h ((sqAxis s + 2) % 3)) / 2
/-- Imaginary part of `B`: `σ (h_b - h_c)/2`. -/
def Bim (s h : ℕ) : ℤ := sqSign s * (hs h ((sqAxis s + 1) % 3) - hs h ((sqAxis s + 2) % 3)) / 2

/-- Real part of the gauge-(B) magnetic Laplacian built from the rules. -/
def Dre : Matrix (Fin 14) (Fin 14) ℤ := fun v w =>
  if v = w then (if v.val < 6 then 4 else 6)
  else if v.val < 6 ∧ 6 ≤ w.val then (if sqHexAdj v.val (w.val - 6) then -Bre v.val (w.val - 6) else 0)
  else if 6 ≤ v.val ∧ w.val < 6 then (if sqHexAdj w.val (v.val - 6) then -Bre w.val (v.val - 6) else 0)
  else if 6 ≤ v.val ∧ 6 ≤ w.val then (if hexHexAdj (v.val - 6) (w.val - 6) then -1 else 0)
  else 0
/-- Imaginary part: `-Im B` in the square row, `+Im B` in the hexagon row (the conjugate). -/
def Dim : Matrix (Fin 14) (Fin 14) ℤ := fun v w =>
  if v.val < 6 ∧ 6 ≤ w.val then (if sqHexAdj v.val (w.val - 6) then -Bim v.val (w.val - 6) else 0)
  else if 6 ≤ v.val ∧ w.val < 6 then (if sqHexAdj w.val (v.val - 6) then Bim w.val (v.val - 6) else 0)
  else 0

theorem Dre_eq_D6r : Dre = D6r := by decide +kernel
theorem Dim_eq_D6i : Dim = D6i := by decide +kernel

/-- **Bridge for Theorem 6.4 at q = 6**: the gauge-(B) magnetic Laplacian built from the rules is the literal `D6`. -/
theorem Dgraph_eq_D6 : ofRI Dre Dim = D6 := by
  unfold D6; rw [Dre_eq_D6r, Dim_eq_D6i]

/-- Every square–hexagon entry of the gauge has modulus one (`B` is a unit phase): `Re² + Im² = 1` on the edges. -/
theorem gauge_unit_modulus :
    ∀ s : Fin 6, ∀ h : Fin 8, sqHexAdj s.val h.val = true → Bre s.val h.val ^ 2 + Bim s.val h.val ^ 2 = 1 := by
  decide +kernel

/-! ## The statements of the note, now about the rule-built matrices -/

/-- Theorem 3.1 for the graph defined by its rules. -/
theorem charpoly_Lgraph :
    Lgraph.charpoly = Polynomial.X * (Polynomial.X - 9) * (Polynomial.X - 7) ^ 4 * (Polynomial.X - 4) ^ 2 *
      (Polynomial.X ^ 2 - 9 * Polynomial.X + 16) ^ 3 := by
  rw [Lgraph_eq_Lfin]; exact charpoly_Lfin

/-- Theorem 6.4, q = 12, for the signless Laplacian defined by its rules. -/
theorem charpoly_Sgraph :
    Sgraph.charpoly = (Polynomial.X - 8) ^ 3 * (Polynomial.X - 5) ^ 3 * (Polynomial.X - 4) ^ 2 *
      (Polynomial.X - 3) ^ 4 * (Polynomial.X ^ 2 - 13 * Polynomial.X + 24) := by
  rw [Sgraph_eq_Sfin]; exact charpoly_Sfin

/-- Theorem 6.4, q = 6, for the magnetic Laplacian defined by the adjacency rules and the gauge formula. -/
theorem charpoly_Dgraph :
    (ofRI Dre Dim).charpoly = (Polynomial.X - 9) * (Polynomial.X - 8) ^ 3 * (Polynomial.X - 3) ^ 4 *
      (Polynomial.X ^ 2 - 9 * Polynomial.X + 16) ^ 3 := by
  rw [Dgraph_eq_D6]; exact charpoly_D6

#print axioms charpoly_Lgraph
#print axioms charpoly_Sgraph
#print axioms charpoly_Dgraph
