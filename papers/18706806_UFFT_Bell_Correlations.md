# UFFT Paper #2 — Void-Pair Conservation as the Physical Mechanism of Quantum Entanglement and Bell Correlations

**Unified Foam Field Theory — Part VIII**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | luke@webenvy.com.au |
| ORCID | 0009-0006-3716-5951 |
| Date | February 2026 |
| Series | Unified Foam Field Theory |
| Paper | #2 of 63 |
| Framework | v10 |
| Status | Complete |
| Tier | 2 |
| DOI | 10.5281/zenodo.18706806 |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, quantum entanglement, Bell theorem, hidden variables, singlet state, EPR paradox, void-pair conservation

**Note:** The void-pair model introduced here was later formalized as H = L + ηV in Paper #45 [DOI: 10.5281/zenodo.19307111], which derives the boson-fermion parity from antipodal symmetry. The three-particle cascade prediction (Section 5) remains a primary falsifiable prediction of the framework.

---

## Abstract

We propose that quantum entanglement is the physical manifestation of void-pair conservation in a quantized vacuum foam. A displacement event D (the creation of one bubble and one complementary void) is the fundamental ontological object. The bubble and void are two addresses of one event, not two correlated objects. This model escapes Bell's theorem because D is inherently non-local and resists the factorization Bell's proof requires. The antipodal symmetry of the void-pair selects the quantum singlet state, which produces the experimentally confirmed correlation E(a,b) = -cos(θ). A testable prediction for three-particle connected foam topologies is proposed.

---

## 1. Introduction

Bell's theorem [1] demonstrates that no local hidden variable theory can reproduce the correlations predicted by quantum mechanics for entangled particles. Experimental tests [2,3] have confirmed the quantum mechanical predictions to high precision.

However, Bell's proof depends on a specific mathematical structure: the correlation function must be expressible as an integral over local hidden variables. We present a physical model in which the fundamental object (the displacement event D) is inherently non-local and therefore does not admit the factorization Bell's proof requires.

---

## 2. Void-Pair Conservation

### 2.1 Axiom Zero

We postulate a single axiom:

**B(x) + V(x') = D**  [Axiom Zero, Void-Pair Conservation]

Every displacement event D in the vacuum foam creates exactly one bubble B at position x and one complementary void V at position x'. The displacement event D is the fundamental object. B and V are its endpoints.

### 2.2 Ontological Status

Critically, D is **not** two separate objects that happen to be correlated. D is **one** object with two addresses. The bubble and void are not created independently and then correlated, they are created as a single event that happens to have two spatially separated manifestations.

---

## 3. Escape from Bell's Theorem

### 3.1 Bell's Factorization Requirement

Bell's theorem requires the correlation function to be writable as:

**E(a,b) = ∫ A(a,λ)·B(b,λ)·ρ(λ)·dλ**  [Equation 1]

where λ is a local hidden variable that determines the measurement outcomes at both detectors, and the functions A and B depend only on the local measurement setting and the hidden variable.

### 3.2 Why D Resists Factorization

The displacement event D is defined by its extension between both endpoints simultaneously. It is not a property that can be assigned to one location, it is inherently a relation between two locations.

Attempting to factor D into local parts:
- D cannot be written as D_A ⊗ D_B where D_A contains only information at x and D_B contains only information at x'
- The void V is defined relative to the bubble B, they are antipodal complements
- The "hidden variable" λ = D cannot be localized

The foam escapes Bell not by finding a flaw in the theorem but by providing an ontological category that Bell's proof was not designed to test.

---

## 4. The Singlet State from Antipodal Symmetry

### 4.1 Selection by Symmetry

The void is the antipodal complement of the bubble, opposite in every direction. What quantum state satisfies perfect anti-correlation in every measurement direction simultaneously?

**|D⟩ = (1/√2)(|↑↓⟩ - |↓↑⟩)**  [Equation 2]

This is the unique two-particle state with this property. It is not assigned arbitrarily, it is selected by the antipodal symmetry of the void-pair.

### 4.2 Correlation Function

From the singlet state:

**E(a,b) = ⟨D|(σ_a ⊗ σ_b)|D⟩ = -cos(θ_ab)**  [Equation 3]

where θ_ab is the angle between measurement directions a and b.

### 4.3 Numerical Verification

| Angle θ | E(a,b) predicted | QM prediction | Match |
|---------|------------------|---------------|-------|
| 0° | -1.000 | -1.000 | ✓ |
| 45° | -0.707 | -0.707 | ✓ |
| 90° | 0.000 | 0.000 | ✓ |
| 135° | +0.707 | +0.707 | ✓ |
| 180° | +1.000 | +1.000 | ✓ |

The void-pair model exactly reproduces quantum mechanical predictions at all angles.

---

## 5. Testable Prediction: Three-Particle Cascade Topology

### 5.1 The Cascade State

For three particles created from a single topologically connected void-pair cascade (not three independent pair creations), the model predicts a specific entangled state:

**|Ψ_foam⟩ = (1/√2)(|010⟩ - |101⟩)**  [Equation 4]

This is neither a GHZ state nor a W state, it is a topologically distinct entanglement class forced by the cascade geometry.

### 5.2 Experimental Discriminator

The sharpest discriminator is the three-particle X⊗X⊗X correlator:

| State | ⟨X⊗X⊗X⟩ |
|-------|---------|
| GHZ | +1 |
| W | 0 |
| Foam cascade | **-1** |

A single measurement setting distinguishes all three states.

### 5.3 Falsification Condition

⟨X⊗X⊗X⟩ ≠ -1 falsifies the foam cascade topology. Any result consistent with GHZ (+1) or W (0) falsifies it.

---

## 6. Discussion

### 6.1 What the Model Explains

The void-pair model answers the question: **what is the physical thing that quantum mechanics is describing?**

Standard quantum mechanics tells us *what* the correlations are. The void-pair model proposes *why* the correlations take that form: because entangled particles are not two correlated objects but two addresses of one non-local object.

### 6.2 Relation to ER=EPR

The void-pair model bears resemblance to the ER=EPR conjecture [5], which proposes that entangled particles are connected by microscopic wormholes. The foam model achieves a similar unification: the displacement event D is the fundamental connection, and entanglement is its quantum mechanical manifestation.

---

## 7. Conclusion

The void-pair model provides a physical mechanism for quantum entanglement:

1. The displacement event D is fundamentally non-local
2. Bell's factorization cannot be applied
3. The singlet state is selected by antipodal symmetry
4. All quantum mechanical correlations follow

The model makes a specific testable prediction for three-particle cascade states that can be distinguished from GHZ and W states by a single measurement.

---

## References

### UFFT Papers
- Paper #1 — Gravitational Suppression of Quantum Decoherence. DOI: 10.5281/zenodo.18706756

### External References
- [1] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika*, 1(3), 195-200.
- [2] Aspect, A., Grangier, P., & Roger, G. (1982). Experimental realization of EPR-Bohm Gedankenexperiment. *Physical Review Letters*, 49(2), 91-94.
- [3] Hensen, B. et al. (2015). Loophole-free Bell inequality violation. *Nature*, 526, 682-686.
- [4] Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of "hidden" variables. *Physical Review*, 85(2), 166.
- [5] Maldacena, J. & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik*, 61(9), 781-811.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, theory, and direction: Luke Martin. AI role: mathematical verification, dimensional analysis, document structuring.

---

*Unified Foam Field Theory · Paper #2 · DOI: 10.5281/zenodo.18706806 · Priority Date: 20 February 2026*

*B + V = D*
