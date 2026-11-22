# Cote 84: integration (reader R4, Claude Opus 5.5 at effort max, 19 Nov 2026)

## STUDY

**Extent.**
- Every transcribed mathematical scan was read: 2-122 and the even scans 124-192.
  - 2-111 in the Codex-web folders K84-01 to K84-07.
  - 112-193 in the Pro packages (GPT-6 Astra, ChatGPT Pro mode), with the two witnesses compared scan by scan from 97.
- The typescript backs (84/5, 7 and the odd scans 125-193, Récoltes et Semailles, October 1984) were identified, not read.
- The stage-A dossier (GPT-6 Astra, ChatGPT Pro mode) was checked where used.
- The checks are 20 check events (re-proofs, sympy, a witness comparison) and 13 corrections.

**Dating.** The mathematics of 124-192 is on the backs of the October 1984 typescript, so it dates from late 1984 or later. That fits cotes 79 (1982 or later) and 81 (1981 or later).

**What the cote is.** A sustained theory of quadratic covers over an arbitrary base, aimed at "invariants d'Arf-Stiefel-Whitney généralisés" (title sheet 84/43).

1. **Binary forms (84/9-42, a draft).**
   - Similitude structures ↔ subalgebras 𝒜 ⊃ O of End(E).
   - The quadratic algebra 𝒜_Q of a binary form ("l'invariant d'Arf").
   - Equivalences: (E, Q) primitive ↔ (𝒜, invertible 𝒜-module) ↔ (X', Λ'), which is Kneser's and Wood's correspondence.
   - The uniqueness of the canonical involution, and reflections.
   - Two corrections: a sign he flagged himself (Q_u = x ∧ u(x)), and a topology margin, fppf ≠ étale for non-étale A in characteristic 2 (the dossier's example, rechecked).
2. **Quadratic covers through (L, P_1, Q) (84/44-62).**
   - When 2 is regular, covers ↔ (L, δ, T_0) with T_0² ≡ δ (4). This is the (L, D, b_0) classification of cote 77, so my cote 77 question belongs here.
   - The explicit 𝒜 = {(b, r)} with N = (b² - r²δ)/4.
   - Characteristic 2: covers as torsors under G_T = ker(u ↦ u² + Tu).
3. **The contracted product (84/63-66, 84/87-106, 172-192).**
   - b = b_1b_2 and c = b_2²c_1 + b_1²c_2 - 4c_1c_2, with u = 2u_1u_2 + b_2u_1 + b_1u_2 (checked by sympy). This is cote 83's ∗-composition.
   - Th. (84/90): the admissible form with Q(y_1 ∗ y_2) = Q_1δ_2 + Q_2δ_1 + 4Q_1Q_2, proved for all points. δ = δ_1δ_2.
   - The product is the fixed ring of σ_1 ⊗ σ_2 iff 2O + b_1O + b_2O = O (checked over Z).
   - The relative trace and norm, and "quasi-quadratic" algebras.
4. **χ-trivialized extensions (84/66-87, 124-170).** A monoidal structure on extensions with a χ-retraction. In his final convention b = π(x), b_{x_1∗x_2} = b_1 ⊗ b_2 ("Il n'y a pas plus simple !").
   - The sign questions of 130-140 stand as decided in sweep 2: the plus convention, a missing χ, and "2 - χ = 1", corrected by himself on 152.
   - New: the "signe étrange" of 134-136 is consistent. It is exactly what makes his map Φ: E → Hom^!(E, L) (-id on L) multiplicative.
5. **Three quadratic algebras (84/4, 111-122).**
   - The seven quadratic and seven rank-4 subalgebras of A_1 ⊗ A_2 ⊗ A_3.
   - Quasi-biquadratic systems, and the étale case with the lemma of 120 (false as written, corrected in sweep 2).
6. **A graded monoid with parities (84/2, 54-56).** Even triples (L, δ, T_0), odd pairs (L, δ), β(L, δ) = (L, 4δ, 0). Associativity reduces to two identities, which hold.

**Links.**
- Cote 77 (SA04-25): the (L, D, b_0) classification.
- Cote 83 (SA01): the ∗-product and the λ-split extensions.
- Within SA02: SA02-1 ↔ SA02-4 at χ = 2, and SA02-14 ↔ the parity product.

## HUNCHES

- **H84-1.** Cote 84 is a characteristic-free theory of quadratic covers and of their monoid under the contracted product. Its targets are Arf and Stiefel-Whitney invariants of quadratic forms over bases where 2 is not invertible (84/43; "Arf(E) ... plus fin que c_1(E) (si 2 non inv. sur X)", 84/2).
  - Modern counterparts to compare: Voight, "Discriminants and the monoid of quadratic rings" (2016; the same product, Construction 3.14); Loos, graded discriminant algebras (1997); Wood (2011); Dallaporta (2025, 2 regular). All locators to be checked.
  - His graded parity monoid and the χ-trivialized extensions may give a Stiefel-Whitney-type invariant of a rank-n form as an element of the graded monoid, finer than the discriminant when 2 is not invertible. That is what 84/2 sketches.
- **H84-2.** The "signe étrange" (134-136) and the sign in the odd-odd product of 84/2 may be one phenomenon: a Koszul sign of the odd part.
  - The stage-A dossier notes that in Loos's odd-odd formula the discriminant is minus four times the product, where Grothendieck has plus four. Here the sign comes from the anti-identification -id: L → Hom(M, L) (SA02-R84-16).
  - Test: write the duality E ↦ Hom^!(E, L) as a monoidal functor and compare its sign with Loos's symmetry.

## PACKAGES

- **P-R4-5. Quadratic covers over an arbitrary base: cotes 77 and 84 as one theory.** This takes over P-R4-1 of the SA04 readings, the cote 77 question that moves into SA02's prompt.
  - Questions:
    - (a) Prove in full the classification of quadratic covers: by (L, D, b_0) = (L, δ, T_0) with T_0² ≡ δ (4) where 2 is regular (77/53-64, 74-86; 84/44-56); by (L, P_1, T, α) in characteristic 2 (84/57-58); by (L, P_1, Q) in general (84/59-62). Compare with Voight 2016, Wood 2011, Loos 1997 and Dallaporta 2025.
    - (b) The contracted product: the integral formula, the kernel Ann(2, b_1, b_2)·U of A → A_1 ⊗ A_2, the fixed-ring criterion 2O + b_1O + b_2O = O, and the Theorem of 84/90.
    - (c) χ-trivialized extensions: one coherent sign convention (the plus convention; the sign of the dual, SA02-R84-16), and the coherence constraints.
    - (d) The generalized Arf-Stiefel-Whitney invariants announced on 84/43. What is "Arf(E)" for a quadratic form of rank n over a base with 2 not invertible, how is it finer than c_1(E), and how does it relate to Loos's graded discriminant algebra (H84-2)?
  - Why it matters: a complete characteristic-free theory of quadratic covers and their products, with the Arf invariant over Z. This is his stated aim (84/43), and it joins cotes 77, 83 and 84.
  - Strongest reduction on the page:
    - the explicit formulas, all checked (SA02-R84-07, -08, -10, -11, -17);
    - the Theorem of 84/90, proved;
    - the Proposition of 84/86, checked over Z;
    - the classification statement of 84/49 when 2 is regular.
  - Material: K84-01 to K84-07 (2-111); MPL_84_097-145 and MPL_84_146-193; `c84a.py` in reader R4's scratchpad; cote 77 (K77-02 to K77-06); the SA01 readings of cote 83; the stage-A dossier's comparisons (Voight, Loos, Wood, Dallaporta).
