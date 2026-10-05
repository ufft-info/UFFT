# Void Network Geometry and Bell Non-Locality: Withdrawal of the c√(3/2) Propagation Speed

**Unified Foam Field Theory — Part XXXIII**

| Field | Value |
|-------|-------|
| Author | Luke Martin |
| Affiliation | Independent Researcher |
| Location | Newcastle, New South Wales, Australia |
| Email | hello@ufft.info |
| ORCID | 0009-0006-3716-5951 |
| Date | October 2026 (v2.0); original March 2026 (v1.0) |
| Series | Unified Foam Field Theory |
| Paper | unnumbered record (Part XXXIII) |
| Framework | v9 |
| Version | 2.0 |
| Status | Central result of v1.0 (c_V = c√(3/2)) WITHDRAWN. Mechanism superseded by Paper #45 [DOI: 10.5281/zenodo.19307111] and Paper #75 [DOI: 10.5281/zenodo.21323993]. Retained as the record of the correction. |
| Tier | §2 (lattice geometry): Tier 1, exact. §3 (front-speed theorem): Tier 1, exact. §4 (exclusion of any finite influence speed): external results (Salart 2008; Bancal 2012). |
| DOI | 10.5281/zenodo.23157808 (v2.0); v1.0: 10.5281/zenodo.19079502; concept: 10.5281/zenodo.19079501 |
| Verification | verify_void_network_speed_2026-10-05.py (geometry, front speeds by closed form and by breadth-first search, experimental comparison) |
| GitHub | https://github.com/ufft-info/UFFT |

**Keywords:** UFFT, truncated octahedron, face Laplacian, foam lattice, BCC lattice, octahedral interstitial sites, Bell non-locality, no-signalling, void channel, correction

---

## Abstract

Version 1.0 of this record claimed that the octahedral-void network of the BCC Planck foam has nearest-neighbour spacing l_P√(2/3), shorter than the bubble spacing l_P, and that voids therefore propagate at c_V = c√(3/2) ≈ 1.22c, supplying a finite-speed mechanism for Bell non-locality. That result is withdrawn. Two errors are identified. First, the void spacing is wrong: BCC has three octahedral holes per lattice site, at the face centres and the edge midpoints of the conventional cube, and the nearest-neighbour spacing of the full void network is a/2, not a/√2. Second, the speed ratio is inverted: with a common hop time a shorter hop is slower, not faster. The propagation front of each network is computed exactly (support function of the hop set, confirmed by breadth-first search). Under a common hop time the void front never exceeds the bubble front in any direction (ratio 1 along ⟨100⟩, 1/2 along ⟨110⟩, 1/3 along ⟨111⟩); under a common hop speed both networks reach exactly c in their fastest direction. No model yields a ratio above 1. Independently, any finite influence speed is excluded: experiment bounds such a speed above roughly 10⁴ c (Salart et al. 2008), and Bancal et al. (2012) prove that every finite-speed influence model permits superluminal signalling, so "the void carries no information" cannot rescue a finite c_V. The surviving content is the lattice geometry of the two networks. The mechanism of Bell correlations in UFFT is the one already published in Paper #45: the void channel of H = L + ηV is the antipodal map through the incompressible bulk, with no propagation and no speed, and no-signalling follows from incompressibility. The pair state is derived in Paper #75.

---

## Changes in this version

- Title changed to state the withdrawal.
- Abstract rewritten. The v1.0 abstract is reproduced in §1 for the record.
- §2 (geometry) corrected: all six octahedral sites per cube are counted; d_V = a/2.
- §3 replaces the v1.0 "speed ratio" (c_V = c·l_P/d_V) with the propagation-front theorem and the computed table.
- §4 added: exclusion of any finite influence speed by experiment and by the Bancal et al. theorem.
- §5 (v1.0 "Physical Mechanism", "Predictions", "Relation to Previous Papers") withdrawn and replaced by a pointer to Paper #45 and Paper #75.
- Header brought to the current paper standard. Verification script added.

---

## 1. What version 1.0 claimed

For the record, the v1.0 abstract read:

> We derive a geometric mechanism for Bell non-locality from the Planck-scale BCC foam structure of Unified Foam Field Theory (UFFT). Under the identification B = Planck spheres, V = octahedral interstitial voids, D = truncated octahedra (Kelvin cells), the void network has nearest-neighbour spacing l_P√(2/3) — shorter than the bubble network spacing l_P. This gives void propagation speed c_V = c√(3/2) ≈ 1.22c from pure BCC geometry, with zero free parameters. When a displacement event D creates a bubble B at x and a void V at x′, the void half of the pair propagates through geometrically shorter paths, arriving at distant locations before the bubble. Since V carries no information — only topological identity — no-signalling is preserved.

The derivation was: bubble spacing l_P; void spacing d_V = a/√2 = l_P√(2/3); hence c_V = c × (l_P/d_V) = c√(3/2). Each of the two steps after the first is wrong, as §2 and §3 show. The claim is withdrawn in full. Nothing downstream in the corpus takes c_V as an input; the correction is confined to this record, to the two summary lines in the Core Framework that quoted it, and to the papers index.

---

## 2. Lattice geometry (corrected)

Take the BCC conventional cube of edge a, with lattice sites (bubble centres) at the corners and the body centre. The bubble nearest-neighbour distance is the half body diagonal,

l_P = a√3/2.

The octahedral interstitial sites of BCC are the points equidistant from six neighbouring lattice sites. There are two crystallographically equivalent families: the face centres, (a/2, a/2, 0) and permutations, and the edge midpoints, (a/2, 0, 0) and permutations. Both lie exactly a/2 from the nearest lattice site. Counting per cube: six faces each shared by two cubes give 3, twelve edges each shared by four cubes give 3, so there are 6 octahedral sites per cube and 3 per lattice site. (The tetrahedral sites, at (a/2, a/4, 0) and permutations, lie a√5/4 ≈ 0.559a from the nearest lattice site and are a distinct family.)

Version 1.0 counted the face centres only. The nearest neighbour of a face-centre site is not another face centre at a/√2; it is an edge midpoint at a/2. With all octahedral sites included the void network has nearest-neighbour spacing

d_V = a/2 = 0.500a   (v1.0: a/√2 = 0.707a).

In units of l_P: d_V = l_P/√3. The hop vectors of the void network are the six axial vectors (±a/2, 0, 0) and permutations; the hop vectors of the bubble network are the eight body-diagonal vectors (±a/2, ±a/2, ±a/2).

All of this is checked numerically in the verification script (sites built from scratch; distances measured; 3 voids per bubble confirmed).

---

## 3. Propagation fronts (the speed ratio, done correctly)

A disturbance that hops from site to site advances, in direction n̂, at the rate set by how far each hop carries it along n̂. For a network with hop vectors {e_j} and a common hop time τ, the graph-distance front in direction n̂ moves at

v(n̂) = max_j (e_j · n̂) / τ,

the support function of the hop set. This is the standard first-passage result for a lattice with a fixed hop time; it is confirmed in the verification script by breadth-first search on a lattice of radius 14a, which agrees with the closed form to the discretisation error.

**Theorem 3.1 (common hop time).** With τ the same for both networks, the void front never exceeds the bubble front.

*Proof.* For the bubble hops, v_B(n̂) = (a/2)(|n_x| + |n_y| + |n_z|)/τ. For the void hops, v_V(n̂) = (a/2) max(|n_x|, |n_y|, |n_z|)/τ. Since max ≤ sum, v_V ≤ v_B for every n̂, with equality only along the coordinate axes. ∎

| Direction | bubble front | void front (true a/2 hops) | ratio | void front (v1.0 a/√2 hops) | ratio |
|---|---|---|---|---|---|
| ⟨100⟩ axis | 0.500 | 0.500 | 1.00 | 0.500 | 1.00 |
| ⟨110⟩ face diagonal | 0.707 | 0.354 | 0.50 | 0.707 | 1.00 |
| ⟨111⟩ body diagonal | 0.866 | 0.289 | 0.33 | 0.577 | 0.67 |

(Units a/τ.) Even with the v1.0 spacing the ratio never exceeds 1.

**Theorem 3.2 (common hop speed).** If instead every hop is traversed at c, each network reaches exactly c in its own fastest direction (bubbles along ⟨111⟩, voids along ⟨100⟩) and less than c elsewhere.

*Proof.* v(n̂) = c · max_j (e_j · n̂)/|e_j| ≤ c, with equality when n̂ is parallel to some hop. ∎

The v1.0 formula c_V = c·(l_P/d_V) has the ratio inverted: it assigns a higher speed to the network with the shorter hop. Under a common hop time the shorter hop is the slower one; under a common hop speed neither network is faster. The two networks differ in anisotropy, not in speed. There is no hop model under which the void network propagates faster than the bubble network, and the number √(3/2) does not arise.

---

## 4. Any finite influence speed is excluded

Even had the geometry supported it, a finite c_V is ruled out on two independent grounds.

**Experiment.** If Bell correlations were carried by an influence travelling at a finite speed v in some preferred frame, there would be measurement configurations in which neither detection event could reach the other in time, and the correlations would drop to the local bound. Salart et al. (2008) searched for this and found no drop, bounding v above roughly 10⁴ c for any reasonable choice of frame; later tests (Cocciaro et al.; Yin et al. 2013) give bounds of the same order or stronger. A speed of 1.22c is excluded by a factor of about 8000.

**Theorem.** Bancal, Pironio, Acín, Liang, Scarani and Gisin (2012) prove that any model in which quantum correlations arise from causal influences propagating at a finite speed, however large, allows faster-than-light signalling at the level of observable statistics. The v1.0 argument that "the void carries no information, so no-signalling is preserved" (v1.0 §3.3) therefore cannot hold for a finite c_V: the theorem concerns the structure of finite-speed models, not the nature of the carrier. The only influence speed consistent with no-signalling is the limit in which there is no finite speed at all.

Both results point the same way as the lattice geometry: there is no finite-speed void mechanism.

---

## 5. What stands, and where the mechanism now lives

Nothing in the corpus takes c_V as an input. The results that the v1.0 paper was meant to serve are unaffected:

- the identification of entangled particles as the two endpoints of one displacement event D, with the conservation law B + V = D as the entanglement constraint (Paper #2, DOI 10.5281/zenodo.18706806; v2.0 DOI 10.5281/zenodo.21331868);
- the escape from Bell's factorisation, on the ground that D is a single extended object and not a local hidden variable (Core Framework Part VI);
- the derived pair state, the antiunitary twin map Θ = V∘K, Tsirelson saturation, and the uniqueness of the laboratory qubit (Paper #75, DOI 10.5281/zenodo.21323993).

The mechanism is the one published in Paper #45 (DOI 10.5281/zenodo.19307111). The axiom B + V = D maps to the two-channel Hamiltonian H = L + ηV. The wall channel L is the face Laplacian: local, causal, speed c, one cell per Planck time. The void channel ηV is the antipodal map through the incompressible bulk (P = ρc²): the void appears on the antipodal face by pressure conservation, with no traversal and no speed. No-signalling follows from incompressibility: no wave propagates through the bulk, so the void channel has zero capacity for directed information and non-zero capacity for correlation. That is the structure the Bancal theorem permits.

The geometry of §2 survives as a statement about the lattice: the void sites of the BCC foam form a network of their own, with spacing a/2 and axial hops. It has no bearing on the speed of anything.

The open question, named here so that it is not mistaken for closed: Paper #45 states that the antipodal constraint holds across the pair without traversal. Why the conservation law B + V = D holds across the whole foam at once, rather than cell by cell, is the existence half of the continuum bridge that Paper #75 names as open (its header and §9). The present correction does not close it; it removes a wrong answer to it.

---

## 6. Conclusion

The claim that voids propagate at c√(3/2) is withdrawn. The void spacing in BCC is a/2, not a/√2; the front-speed ratio of the void network to the bubble network is at most 1 in every direction under any hop model; and any finite influence speed is excluded by experiment (Salart 2008) and by theorem (Bancal 2012). Bell correlations in UFFT have no propagation speed. They are a property of the single displacement event D, carried by the void channel of H = L + ηV (Paper #45), with the pair state derived in Paper #75.

Status line for the Core Framework: **Void network speed. WITHDRAWN** (v2.0 of this record, October 2026). Mechanism: Paper #45 void channel.

---

## References

[1] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. Physics Physique Fizika, 1(3), 195–200.

[2] Salart, D., Baas, A., Branciard, C., Gisin, N., & Zbinden, H. (2008). Testing the speed of 'spooky action at a distance'. Nature, 454, 861–864.

[3] Bancal, J.-D., Pironio, S., Acín, A., Liang, Y.-C., Scarani, V., & Gisin, N. (2012). Quantum non-locality based on finite-speed causal influences leads to superluminal signalling. Nature Physics, 8, 867–870.

[4] Yin, J., et al. (2013). Lower bound on the speed of nonlocal correlations without locality and measurement choice loopholes. Physical Review Letters, 110, 260407.

[5] Martin, L. (2026). Void-Pair Conservation and Bell Correlations (Paper #2). DOI: 10.5281/zenodo.18706806; v2.0 DOI: 10.5281/zenodo.21331868.

[6] Martin, L. (2026). The Void Channel: H = L + ηV (Paper #45). DOI: 10.5281/zenodo.19307111.

[7] Martin, L. (2026). The Born Rule from Imprint Statistics and the Entangled Pair State from the Antiunitary Twin Map (Paper #75). DOI: 10.5281/zenodo.21323993.

[8] Martin, L. (2026). The Unified Foam Field Theory: Core Mathematical Framework. DOI: 10.5281/zenodo.18706756.

---

## AI Disclosure

This paper was developed in collaboration with Claude (Anthropic). Ideas, framework, direction, and physical interpretation: Luke Martin. AI role: numerical computation and document composition.

UFFT Core Framework: github.com/ufft-info/UFFT

---

*Unified Foam Field Theory · Part XXXIII · DOI 10.5281/zenodo.23157808 · Priority Date: 20 February 2026*

*B + V = D*
