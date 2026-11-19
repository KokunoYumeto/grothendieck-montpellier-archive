# SA08 hunches (sweep 3)

From the readings of the two SA08 readers, both Claude Opus 5.5 at effort max:
- a1f628dde2f29df92, scans 2-141, file `readings/136_002-141.md`; its hunches are marked R1;
- aa2156d1c23970b0d, scans 142-281, file `readings/136_142-376.md`; its hunches are marked R2.

Integrated by a34c04448e8299803 (Claude Opus 5.5 at effort max) on 19 Nov 2026. Locators marked "(to verify)" are
unverified.

**H1 (R1-H1). The binomial bridge.**
- **The hunch:** C^{••}_DRpd(X, Z), with its parameter T, is the associated graded for the degree filtration of a
  cochain model built from integer-valued polynomials on the simplices.
- **Grounds:**
  - gr Int(Z) ≅ Γ_Z(T) (the Pro notes R052);
  - T is the constant section 1;
  - T = 1 gives Sullivan's forms over k ⊗ Q (CE008).
- **Literature:** Toën, Épijournal 2020; Horel, "Binomial rings and homotopy theory"; H. Cartan, "Théories
  cohomologiques", Invent. Math. 35 (1976), the published account of the lecture. All to verify.

**H2 (R1-H2). The weight-zero corner is a strictly commutative cocycle algebra.**
- ⊕_q Λ^qΨ = ⊕_q K(k,q) is a strictly alternating simplicial ring whose homotopy ring is the divided-power algebra.
- **The hunch:** the missing data (E) of scan 77 can be taken from it, which would complete "structures sur DR"
  without new choices.

**H3 (R1-H3). Why "Non" for cosimplicial sets (scan 91).**
- In Δ̂, Φ = i_{0*}(Z) is coinduced from [0]. In the cosimplicial topos the right adjoint of evaluation at [0] is the
  constant functor, so the candidate collapses to Z.
- **What a proof needs:** a cohomological obstruction to any universally flasque Φ ⊃ Z there.

**H4 (R1-H4). Universal flasqueness implies contractibility.**
- **The hunch:** acyclicity on every slice Δ̂/X forces π_* = 0.
- **Consequence:** this would repair scan 100's argument without "projectif".

**H5 (R1-H5). The product convention.**
- Remark a) holds with cochains of unbounded weight and fails with finite weights.
- **The hunch:** the "virtual PD de Rham complexes" (scan 13) should be defined with completed (product) weights, and
  the shadow theory checked there.

**H6 (R2-H1). Dating of scans 144-188.**
- **Grounds:** the printout of 16 Aug 1982 at folio 142, and the parallels with Pursuing Stacks §§117-139.
- **The hunch:** the coalgebra yoga and the automorphism sheets were written in 1982-83, not at the 1976 lecture.
- **Limit:** the grounds are suggestive, not decisive.

**H7 (R2-H2). The PD de Rham cohomology over k{T} is a PD-Rees algebra.**
- **The hunch:** H^*_DRpd(X; k{T}, (T), T) ≅ ⊕_i H^i(X; k) ⊗_k I^{[i]} as graded k{T}-algebras, with
  I^{[i]} = span{T^{(p)}: p ≥ i}.
- **Grounds:** the weightwise comparison (scan 233), with the action of T and the products T^{(p)}T^{(q)} =
  c_{pq}T^{(p+q)}.
- **Consequences:**
  - the shadows of SA08-7 are exactly these modules;
  - T = 1 over Q gives H^*(X; k).
- Michel Hua's register entry "136-pd-de-rham-shadows" is credited.

**H8 (R2-H3). His "Non" to the Steenrod hope is probably right for the B-part of Ω.**
- With condition (M), the characteristic-2 part of Ω is an additive group of derivations.
- First-order deformations along dX_0 tend to be homotopic to the identity, by Cartan's formula.
- **The hunch:** Ω acts on cohomology only through Δ.

**H9 (R2-H4). The décalage question (scan 229) and K136-03. Settled in wave 2.**
- The décalage on scan 362 is the Quillen-Illusie one, checked (CE-F10).
- It answers 229 in the case L = M[1].
- The one exception is the Sym/Λ sequence of 362, which is not exact over Z (CO-F04).

**H10 (R2, wave 2: H5). The operations of Ω land in the algebra 𝒜 of scan 374, not in the Steenrod algebra.**
- **Grounds:** if the corrected Ω acts on the PD de Rham cohomology over F_p by operations, these have coefficients in
  G_a. They lie in the algebra 𝒜 of 374, where P^0 acts as Frobenius and not as 1.
- **Consequence:** Ω should be compared with 𝒜, rather than with the Steenrod algebra of his hope on 182.
- This is an inference, not on the pages.

**H11 (R2, wave 2: H6). Scans 374-376 follow Breen's computation of Ext(G_a, G_a)** (Publ. IHÉS 48, 1978; to verify).
- This could date or place the unattributed notes of 362-376.
- The attribution stays open, as in Michel Hua's project.

**H7, update (wave 2).** The PD-Rees form of H*_DRpd now has two independent sources:
- wave 1's derivation from scan 233;
- the Pro notes N72-N73 of MPL_136_235-281, which state the module structure and check the ring arithmetic.

It is still an inference, not on the pages.
