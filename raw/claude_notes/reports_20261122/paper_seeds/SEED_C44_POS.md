# Paper seed: Grothendieck's 1964 positivity programme (C44_POS final, with JAC1964, SIGN_NEXT, HODGE_SIGN, SA14/SA19)

Seed by Claude Opus 5.5 at effort high (agent a8d753525905811ab), 22 Nov 2026, for the main session (Claude Opus 5.5 at
effort max). The research runs are GPT-6 Astra (ChatGPT Pro mode); the runs record their effort as "not exposed".

One paper: the whole cluster answers one document.

Paths used below:
- `RR` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns`
- `P` = `RR\C44_POS_final_20261122T1020Z_unzipped\C44_POS.tex`
- `J` = `RR\JAC1964_checkpoint_06_20261121T0521Z_unzipped\JAC1964.tex`
- `S` = `RR\SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped\SIGN_NEXT.tex`
- `H` = `RR\HODGE_SIGN_final_20261121T0057Z_unzipped\HODGE_SIGN.tex`
- `D` = `RR\RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped\sections\J.tex`
- `T` = `<local>/Documents\grothendieck_archive_transcription_20261110\text_of_record\pages\44`

Who checked, as abbreviated in the tables:
- **O-h**: Claude Opus 5.5 at effort high, agent a8d753525905811ab.
- **O-sn**: Claude Opus 5.5 at effort high, the SIGN_NEXT intake agent (abcaba9b).
- **O-hs**: Claude Opus 5.5 at effort high, the HODGE_SIGN intake agent.
- **O-max**: Claude Opus 5.5 at effort max, agent a262249a0710a599b.
- **run**: GPT-6 Astra (ChatGPT Pro mode), effort not exposed, in its own check events.

"Proof read" is a targeted proof check: the proof was read and its steps followed, with cited theorems taken as cited.
"Statement" means that we read only the statement.

---

## Title

**Grothendieck's 1964 positivity programme: counterexamples, corrections, and fourfolds whose every power satisfies the
standard conjecture of Hodge type**

## The document it answers

In 1964 Grothendieck wrote a "Programme de travail" of seven theorems on cycles algebraically equivalent to zero
(Montpellier archive, cote 44; transcription opened, scans 002, 004, 006, 008, 009):

- **Th. 1–3 (scan 002).** Such cycles of codimension i on X^n, modulo "Albanese equivalence", form an abelian variety P^i.
  It has dimension at most half the Betti number b_{2i-1}, and P^i is canonically dual to a complementary one. The index
  on scan 002 is uncertain. The letter on scan 008 gives n+1−i.
- **Th. 4 (scan 002, marked "Hodge").** For n = 2m−1 the self-duality of P^m is given by a polarization.
- **Th. 5 (scan 004, marked "Néron").** Let Y be the generic member of a hyperplane pencil on X whose fibres are
  geometrically integral. If Z.Y and Z'.Y are algebraically equivalent to zero, their Néron–Tate pairing is (−1)^m Z.Z'.
  He struck out "au signe près ??" and noted that this should follow from a more general statement on fibrations and has
  a local variant.
- **Th. 6 (scan 004, marked "Lefschetz").** Restriction P^i(X) → P^i(Y) is an isogeny for 2i ≤ n−1, has the fixed part as
  image for 2i = n, and is surjective for 2i ≥ n+1.
- **Th. 7 (scan 006, marked "Matsusaka").** Numerical equivalence equals τ-equivalence.
- **The letter to Serre of 12 August 1964 (scans 008–009).** It reduces the positivity theorem of Hodge, modulo unproved
  steps, to the positivity of D = r_*(p*z · q*z). A note in its margin says that the primitive decomposition must be
  taken into account.

The programme predates the standard conjectures as printed (Bombay 1968, published 1969; from memory) and is an early
form of them: Th. 4 and Th. 5 are statements of Hodge type, Th. 6 of Lefschetz type.

---

## Main theorem (no unrefereed or unpublished theorem as input)

It has two forms. The first is proved in the return, and we read the proof of each of its steps. The second is stronger.
It follows from proofs we read, and is the statement the paper should carry once the prompt has written it out.

### As the return proves it

Let E: y² = x³ − x, and let H be the sum of the six coordinate theta divisors on E^6. For every sufficiently large
integer t there are infinitely many primes p ≡ 3 (mod 4) with the following property. (The primes are those outside a
finite set, which depends on t, on the chosen family and on one auxiliary ℓ.) Over the algebraic closure of F_p there
are infinitely many smooth fourfolds B ⊂ E^6, each defined over a finite field, each the intersection of two members
D₀, D of |tH| and the axis of the Lefschetz pencil they span, forming a Zariski-dense set of closed points of a
one-parameter family, such that:

1. **Hodge type, on every power.** For every N ≥ 1, every ℓ ≠ p and all positive rationals ρ_i, the standard conjecture
   of Hodge type holds for (B^N, Σ ρ_i pr_i* h), where h = tH|_B. One B serves for all N. On B itself it holds for every
   rational ample class.
2. **The other conjectures, on every power.** The standard conjecture of Lefschetz type holds on B^N. Numerical and
   ℓ-adic homological equivalence coincide for every ℓ ≠ p. The Tate conjecture holds in every codimension over every
   finite extension of the field of definition, with the rank equal to the order of the pole. Frobenius is semisimple.
   The algebra of cohomological correspondences of degree zero on B has a positive adjoint trace and is semisimple.
   This last point is what Grothendieck's letter of 6 January 1966 (cote 16, scan 049) wants from positivity.
3. **The algebraic classes that the ambient variety does not see.** The algebraic part of ker(H⁴(B) → H⁸(E^6)) is one
   line Qw, with ∫w² = 6t² − 1/(4t²) > 0. That kernel has dimension 3600t⁶ − 165.
4. **The corrected Th. 5, with positivity.** Let Y be the generic fibre, a fivefold over the rational function field in
   one variable over the algebraic closure of F_p. Every class in CH³(Y) ⊗ Q homologically equivalent to zero has an
   admissible extension to the blow-up of E^6 along B. The signed intersection height on this whole group is positive
   semidefinite. Its radical is exactly the image H₀ of the homologically trivial cycles of the total space. The quotient
   is canonically isometric to A ⊥ Qw, with form −∫zz′ on the primitive algebraic classes A of codimension 3 on E^6 and
   +∫ww′ on the line. The quotient form is positive definite.

### In general form (INT-C44-2: deduced by O-h on 22 Nov from proofs we read; not written out by the run, not independently checked)

Let p be any odd prime, r ≥ 2, and X a supersingular abelian variety of dimension 2r+2 over the algebraic closure of F_p,
with a very ample class H. Let Z_1,…,Z_s be disjoint smooth connected r-dimensional subvarieties, where s is congruent to
binom(2r+2, r) modulo 2. Translates of one abelian r-fold will serve, in any number. For every sufficiently large t
there is a Zariski-dense set of closed axes B ⊂ X of Lefschetz pencils in |tH|, all containing the Z_i, such that:

- for every N and every product polarization, B^N satisfies the standard conjecture of Hodge type, and also Lefschetz
  type, numerical equals homological for every ℓ ≠ p, and Tate in every codimension over every finite extension;
- the algebraic part of ker(H^{2r}(B) → H^{2r+4}(X)) is exactly the span of the s projected centres, with positive
  definite signed form;
- the signed height on all of CH^{r+1}(Y)_hom ⊗ Q of the generic pencil member is positive semidefinite, with radical
  exactly H₀;
- for r = 2, Hodge type holds on B for every rational ample class.

So in every odd characteristic and every even dimension at least 4 there are smooth projective varieties, not abelian
and with unbounded middle Betti number, that satisfy all the standard conjectures and the Tate conjecture on every
power (Hodge type for product polarizations). The centres need not lift. For p ≡ 3 (mod 4), r = 2 and s = 1 one may take
the surface of C44-A14, which has no lift to characteristic 0.

**Proof, by the steps that replace A13 in A30.**
1. A06 (P 973–1127) gives the pencils and a positive, constant Gram matrix G of the projected centres. A05 (P 362–453)
   lifts each embedded axis to a mixed-characteristic trait. No lift of the centres is used.
2. A18 (P 3920–4184) gives geometric monodromy O(W) on their complement in odd characteristic, by the fourth moment and
   one reflection, without a model in characteristic 0. So no finite set of primes is excluded. By the rank formula A03b
   the parity of s makes rank W even.
3. Frobenius on W is rational, pure and independent of ℓ, with bounded p-adic valuations. There are finitely many
   possible relation lattices, so a dense set of closed points has Frobenius generating a maximal torus of SO(W). Steps
   2–3 of A30 then apply word for word, with q_W replaced by (−1)^r q_W.
4. All even cohomology of every power of X is spanned by divisor products, X being supersingular. Step 4 of A30 applies
   on the lift from A05: the Lefschetz inverses are algebraic, and Milne 2002 gives the sign on the special fibre.
5. Step 5 of A30 applies with tensor powers of G in place of those of β. The blocks are orthogonal and the remaining
   sign is (−1)^j on the ambient factor. B, D, Tate and semisimplicity follow as in step 6. H9-T7 and A42b give the
   height, and A30a the case r = 2.

**What it implies.** In positive characteristic there are varieties that are not abelian, with middle Betti number as
large as one likes, for which all of these conjectures hold on all powers at once. For their pencils Grothendieck's
"Néron" theorem becomes true after correction, sign included.

**What it doesn't say.**
- Nothing about an arbitrary closed axis, or about characteristic 2. In the first form, nothing about the finitely many
  excluded primes for a given t.
- On B^N with N > 1, Hodge type is proved for product polarizations only.
- Item 4 is about the geometric intersection height. Its identification with a Néron–Tate pairing on an intermediate
  Jacobian is a separate input: Kahn, and Chen's preprint arXiv 2512.22788.
- "Not abelian" refers to the variety (b₁ = 12 in the first form, 4r+4 in the general one, against 4r for an
  abelian variety of that dimension). We don't claim that its motive is not of abelian type.
- No claim of historical novelty. The literature search is still to be done.

**The proof in four steps (first form).**
1. A one-parameter family of axes through E²×0 has orthogonal geometric monodromy on the complement W of the ambient
   classes and of w (SGA 7, Weil II). This survives reduction at almost every prime.
2. There is a dense set of closed points where Frobenius generates a maximal torus of SO(W). Invariant tensors in powers
   of W are then generated by pairings twisted by powers of Frobenius, which are algebraic.
3. Their intersection form is a tensor power of Tr(a ā) on the product of CM fields Q[Φ]. It is positive, by the Weil
   conjectures alone. This is the idea of the paper: where Frobenius is as generic as possible, Weil's Riemann
   hypothesis gives Hodge positivity.
4. On the ambient part, every class is a Lefschetz class of a supersingular power, where positivity is Milne's theorem
   of 2002. The height statement follows from the orthogonal blow-up decomposition.

**Inputs, all cited as published.** Weil conjectures and Weil II Th. 4.4.1; SGA 1 XIII 2.9–2.12; SGA 7 II XV, XVII 2.5,
XVIII, XIX 3.4; Katz–Messing; C. Chin, JAMS 17 (2004), Th. 5.7; Tate 1966; Milne, *Polarizations and Grothendieck's
standard conjectures*, Ann. of Math. 155 (2002), Remarks 3.7–3.8 (its unconditional part); Kleiman 1994, Prop. 5-1 and
Th. 5-6; Entin, IMRN 2021, Th. 3. All of these were opened by the run by its own record, and none by us for this seed.

| Part | Statement | File and lines | Who checked, and how |
|---|---|---|---|
| Selection of closed points | C44-A12 | P 2479–2590 | run; O-h proof read, 22 Nov |
| Family, class, monodromy, item 3 | C44-A13 | P 2627–2946 | run; O-h proof read, norm, ranks and Hodge number recomputed by hand |
| The square | C44-A28 | P 27076–27466 | run; O-h proof read |
| Items 1 and 2 | C44-A30 | P 27722–28166 | run; O-h proof read |
| General form: centres and Gram matrix | C44-A06 | P 973–1127 | run; O-h proof read |
| General form: monodromy | C44-A18 | P 3920–4184 | run; O-h proof read, Katz's Th. 1.4.6 taken as cited |
| General form: embedded lift | C44-A05 | P 362–453 | run; O-h proof read |
| Every ample class on B | C44-A30a | P 28169–28258 | run; O-h proof read |
| Injective specialization | JAC-P07 | J 2724–2798 | run; O-h proof read |
| The height isometry | H9-T7 | J 2868–3054 | run; O-h proof read |
| Item 4 | C44-A42b, applied to A13 | P 15091–15264 | run; O-h proof read; the application to A13's family is this intake's one-line deduction |

Programs: the run's certificate `work\scan_w\axis_rank_one_arithmetic.json`, and two of our own in
`<local>/Documents\reports_20261122\overnight_intake\C44_POS\`, with their outputs beside them:
`checks_own.py` (the class, norm, ranks and Hodge number of A13; J5; the Cartier–Manin matrix of J2a; rational
singular points for J6C) and `cert_rank.py` (the rank-64 tensor of A14; the parities). All passed. We did not run the
run's code. No independent re-proof exists yet.

---

## Why it matters

- It says, clause by clause, which of Grothendieck's seven statements of 1964 are refuted as written or in a stated
  modern reading, which corrected statements are proved, and which are still open. In two cases he saw the repair himself: the primitive decomposition (scan 008) and the
  fibration with a local term (scan 004).
- The standard conjecture of Hodge type in characteristic p is known in few cases beyond surfaces (from memory). Here it holds on all
  powers of explicit fourfolds, and the source of positivity is visible.
- The height pairing of higher-codimension cycles over function fields gets a proved sign in characteristic p, on whole
  groups of homologically trivial cycles.

Works continued, corrected or refuted:

| Work, statement and page | Relation | Citation |
|---|---|---|
| Grothendieck, cote 44, scans 002–009 | corrected and refuted as tabulated below | source opened |
| Grothendieck, cote 16, scans 048–050, letter of 6.1.1966 | scan 050's Proposition corrected; scan 049's consequence realized | source opened in the earlier intake |
| Grothendieck, *Standard conjectures on algebraic cycles*, Bombay 1968, pp. 193–199 | continued | from memory |
| H. Saito, Nagoya Math. J. 75 (1979), Th. 3.6 pp. 112–114, Prop. 3.4 pp. 109–110, Prop. 4.4 | gives P^i for incidence equivalence, Th. 1–3 | from memory, with the runs' locators |
| Kleiman, Dix exposés 1968, 2A11; 1994, Prop. 5-1 p. 17, Th. 5-6 p. 19 | continued | from memory, with the runs' locators |
| Milne, Ann. of Math. 155 (2002), Remarks 3.7–3.8 | continued from Lefschetz classes to axes | from memory, with the run's locators |
| Ancona, Invent. Math. 223 (2021), Th. on abelian fourfolds and Prop. 3.15 | the fourfold signature argument is his | from memory, with the run's locator |
| Ito–Ito–Koshikawa and Koshikawa, squares of K3 surfaces | nearest known results on powers; to be compared | from memory |
| S.-W. Zhang, arXiv 1001.4788, Th. 1 | characteristic-0 primitive height sign | from memory, opened by the run |
| B. Kahn, *Refined height pairing*, arXiv 2009.00533v7, Th. 4.14 p. 31, 6.2, 6.6 pp. 38–42 | normalization of heights | from memory, opened by the run; its refereed status is to be verified |
| S. Bloch, J. reine angew. Math. 350 (1984), Th. 4.1 p. 104 | refutes Th. 7 in characteristic 0 | from memory, with the run's locator |

---

## The other results, in the order of the argument

### I. Results with no unrefereed input: the paper is built on these

**1. Th. 1–3, in the incidence reading.** Saito's quotient exists in every codimension and characteristic, with the bound
and an isogeny duality (SA14 J1i, D 104–316; statement).

**2. Th. 3 can't be integral for the universal regular quotient.** For the generic genus-3 hyperelliptic Jacobian in
characteristic 5, no isomorphism Ab² → (Ab²)^∨ is induced by intersection: a translation family would force an isogeny
of degree 8 from A, whose A[2] is irreducible (**J2a**, D 442–741; O-max proof read; O-h proof read). This does not
refute the isogeny duality of the incidence quotient. One input to open: Achter–Pries 2006, Th. 3.4, on monodromy.

**3. Th. 4 is false without the primitive part, for both signs.** This confirms his own margin.
- E×P¹×P¹ in every characteristic, with form [[0,λ],[λ,0]] (**J2b**, D 317–440; O-max and O-h proof read).
- E³, with two families of signs ±2 (**JAC-P03**, J 754–819; O-h proof read).

**4. Th. 4 on the primitive part, unconditional cases.**
- **Statement (JAC-T4.1, T4.3).** For an abelian variety A of dimension 2m−1 with ample h, let d_B be the incidence
  correspondence on B = P^m(A)_prim. The assertion is that ((−1)^m/2)Δ*d_B is ample.
- **Characteristic 0:** true, by Hodge–Riemann in place of the conjecture in T4.2 (J 1478–1688; O-h proof read, the
  degree identity derived).
- **Characteristic p, new here (INT-C44-1):** true whenever A over the algebraic closure of F_p is isogenous to a power
  of one elliptic curve E, every supersingular A included. Derived by O-h, 22 Nov; not independently checked. Proof:
  - Nondegeneracy of d_B makes H¹(B) a Frobenius subquotient of H^{2m−1}(A)(m−1). Slopes in [0,1] then leave only the
    eigenvalues of E (in the supersingular case only supersingular ones), so B is isogenous to a power of E by Tate.
  - The symmetric homomorphism ψ of the divisor is therefore a Hermitian matrix over End⁰(E). It is positive
    semidefinite as soon as its degree on each elliptic curve E′ ⊂ B is nonnegative, because Hom(E,B) ⊗ Q is dense over R.
  - On E′ that degree is ((−1)^m/2)∫ξ² on E′×A, which is isogenous to a power of E. All its algebraic classes are
    Lefschetz classes (the argument of C44-A42b), and ξ is primitive for θ + h. Milne 2002 gives the sign.
  - ψ is an isogeny, so semidefinite is definite, and the class is ample.

**5. Th. 5 is false as displayed, in three independent ways.** In each, the left side is 0.
- Split quadric fourfold over the algebraic closure of F₃, four explicit planes: the restrictions vanish as cycles and
  Z.Z′ = 2 (**J5**, D 884–1037; O-max proof read; O-h proof read). This is the most elementary.
- Quadric pencils in every characteristic and every m ≥ 2: (−1)^m Z² = 2, one unit at each node (**H9-C1**, J 1884–2050;
  O-h recomputed while reading).
- P²×P² with a flag-threefold pencil: the corrected value is 0 = 3 − (1+1+1) (**AR-01**, H 798–891; O-hs proof read.
  **SN-44-04**, S 4676–4767; O-sn rederived).

**6. The corrected Th. 5.** For admissible extensions, h = (−1)^m(deg x₀y₀ − Σ a_s^t M_s^{-1} b_s), under orthogonality
to the radical of each vertical form (**H9-T1**, J 2051–2117, O-h proof read; equal to **SN-44-01**, S 4322–4441, O-sn
proof read). At an ordinary node the local form is (−1)^m ν(D)ν(D′) (**SN-44-02**, S 4442–4546, O-sn). Injective
specialization suffices for no correction (**H9-T2**, J 2118–2209, O-h proof read), which at an ordinary double point
is the same as a nonzero vanishing cycle, by the local specialization sequence (**SN-44-03**, S 4547–4675, stated over
C, O-sn followed the argument; in every characteristic by SGA 7 II XV, as in C44-T05). Synthesis: **C44-T05**, P 33249–33408, O-h read.

**7. Pencils on abelian varieties.** The whole height group modulo H₀ is A_X ⊥ A_B, with form (−1)^m on the ambient
primitive classes and (−1)^{m−1} on A_B = ker κ_* on the axis (**H9-T7** with **JAC-P07**, as above). Consequences:
- positive in characteristic 0 for every axis (**H9-T8a**, J 3095–3155; statement);
- for m = 2, semipositive in every characteristic over the algebraic closure of a finite field, by the surface index
  theorem and Ancona's fourfold theorem. JAC1964 H9-T8 (J 3055–3094) assumes OpenAI 032 here, which is more than
  semipositivity needs. This is this intake's deduction; Ancona's statement is to be opened before use;
- for X a power of an elliptic curve, positive as soon as the axis form is (**C44-A42b**, O-h proof read);
- on any axis, A_B is exactly the part of the primitive middle classes not coming from X (**C44-A01**, P 134–211;
  O-h proof read of the decomposition).

**8. What happens after a base change.** On cycles homologically trivial on the fibre, semipositivity fails after finite
covers: an explicit class on an E⁴ pencil has height −12d³, next to a direction +4d (**H9-T17**, J 4229–4559; O-h
recomputed). The negative class is of Lefschetz type (alb(hz) ≠ 0). The identity in 6 is untouched. What must be
restricted to the Albanese-primitive domain is the positivity. In characteristic 0 that restricted positivity is Zhang's
theorem.

**9. Positive families of axes.**
- Any prescribed disjoint smooth centres on any abelian variety in odd characteristic occur on dense sets of closed
  axes of high degree whose whole algebraic kernel is positive (**C44-A06**, P 973–1127, and **A18**, P 3920–4184:
  O-h proof read. **A18a**, P 4185–4262: read; in odd residual rank it uses A15 and A16, read only as statements).
- The sign follows from a known positive span with at most one more potential Tate direction (**A15**, P 3579–3919;
  statement).
- Families with extra symmetry have residual potential rank as large as one likes (**A19–A26**, P 4485–7586), and
  quaternion criteria give families in every characteristic, 2 included (**A34–A42a**, P 10394–15090; statement).

**10. Positivity without lifting.** For every p ≡ 3 (mod 4) there is a surface in E⁴ with no lift to characteristic 0
(**A14**, P 3182–3578, O-h proof read and tensor rank recomputed; **A14b**, P 23336–23534, statement). On suitable axes
in E^6 through it the primitive class w spans the algebraic kernel and has positive square. Yet it is the specialization
of no algebraic class on any smooth projective lift of B of ramification e ≤ 5 (p = 3) or e ≤ 3p (p ≥ 7) (**A29, A31s,
A31t**, P 8551–8671, 20710–21508; statement). So in that range the sign can't be obtained by lifting the class. That
exclusion rests on the chain A22–A31r, which we haven't read: it is not yet checked by us.

**11. Cote 16, scan 050, corrected.** C(X) ⟺ C(Y) + R₀(T,W) + G_{L,0}(T,W), with T = X×X and the missing Lefschetz
factor restored (**SN-C03, C04**, S, C04 at 334–362; O-sn proof read). It holds on the axes of the main theorem
(**C44-A28a**, P 27466–27555; statement). Trace data alone can't give scan 049's positivity (**SN-14**, S 670–; O-sn proof read).

**12. Th. 6.** The middle clause is false without a smooth axis: a cubic fourfold over the algebraic closure of F₅ has
P² = 0, and the generic member of an integral pencil has a constant elliptic factor, detected by a composite [−2]
(**J6C**, D 1408–1638; O-max and O-h proof read). With a smooth axis it holds in codimension 2 (**J6P**, D 1176–1357;
statement). Up to isogeny every clause holds whenever B(X) holds, so for abelian X in every characteristic (**JAC-P02**,
J 630–751, the middle clause with a smooth axis; statement).

**13. Th. 7** is false in characteristic 0 (**JAC-P05**, J 871–916, and **SA14 J1-Th7**, D 742–810; statement). The
phenomenon is classical since Griffiths 1969.

**14. Two by-products.** The sharp bound deg(Z·Z′) ≤ deg(h^rZ)deg(h^{g−r}Z′)/(r!(g−r)!χ(L)) on abelian varieties in
every characteristic (**C44-W12**, P 33022–33100; statement). Every finite map of a smooth curve to P¹ lifts as a map
(**C44-C06, C06a**, P 24924–25121; statement).

### II. Results that need unrefereed inputs: a separate, marked last section

The inputs are OpenAI family 032 (Hodge for CM abelian varieties; human proof by van Hoften–Sempliner, Hexagon
2610.00259) with Milne's report (Hexagon 2611.00244). The report gives Cor. 8.3 (Tate for abelian varieties over finite
fields) and Cor. 8.4 (Hodge type for all abelian varieties). Its §3.6 prints the primitive form without (−1)^r; use the
signed form.

| Statement | Content | Needs | File | Check |
|---|---|---|---|---|
| JAC-T4.3, T4.5 | Th. 4 on the primitive part, every abelian variety, every field, every characteristic | Cor. 8.4 in char. p | J 1600–1719 | O-h proof read |
| C44-W10, W11 | Th. 4 with a relative abelian injection; all odd Fermat hypersurfaces in good characteristic | Cor. 8.4 | P 32618–33021 | statement |
| C44-W06, W08 | Th. 4 through finite abelian covers and specialization | Cor. 8.4 | P 32050–32295 | statement |
| C44-W09 | geometric abelian type | also Milne 2022, Prop. 4.2, not re-established | P 32296–32343 | statement |
| H9-T4, T6a, T13 | Th. 4 for generic sections | Cor. 8.4 | J 2270–2723, 7151–7380 | statement |
| H9-T7, general X | height sign equivalent to the axis sign | Cor. 8.4 | J 3047 | O-h proof read |
| JAC-P09 | generic axes of degree d ≥ 3 have positive height | Cor. 8.4 | J 3156–3305 | statement |
| JAC-P15, H9-T14 | Th. 7 over finite fields for abelian type | Cor. 8.3 and Kahn 2003, Th. 1.10 | J 945–1124, 7508– | statement |
| JAC-P16 | geometric abelian type: standard conjectures, hence Th. 6 | Cor. 8.4 | J 1125–1358 | statement |
| C44-W05, a scope note | in characteristic p at a split prime a "signature (n,n)" read on the Lie algebra of a bad order does not make the Weil plane Tate; require balance of the p-divisible group (W04) | none | P 32004–32048 | O-h proof read |
| SN-11 | semisimplicity on products of abelian varieties | 032 | S 479– | O-sn proof read |
| C44-W02–W04, W13 | detector and division bounds in characteristic p | 032 and Milne | P 31687–32003 | statement |
| C44-C01–C05 with H9-T18–T26 | signs after covers | the ambient sign only; the monodromy parts need none | P 24235–24923 | statement |

Néron–Tate readings of the height need Kahn and Chen's preprint (SN-44-01, SN-44-06).

---

## The research question for the prompt

**Theorem to prove or refute.** Let X be an abelian 2m-fold over the algebraic closure of F_p, m ≥ 3, and B = D₀ ∩ D a
smooth intersection of two divisors of one ample class. Then (−1)^{m−1}∫w² ≥ 0 for every algebraic w in
ker(H^{2m−2}(B) → H^{2m+2}(X)), with strict inequality for w ≠ 0.

This would make corrected Th. 5 positive for every abelian pencil (unconditionally when X is a power of an elliptic
curve) and, by C44-A01, would prove Hodge type for every such B where it is known for X.

**Gate, as it stands.** For every axis, m ≥ 3, with two or more potential Tate directions outside a known positive span
and no extending orthogonal, totally real or quaternion block. C44-A17 and A17b prove that determinants at all ℓ and
weak admissibility do not decide rank 2 or 3. The central crystalline formula C44-A33 needs a certificate of the full
central cycle space. A transfer to abelian H¹, uniform over a family, is excluded on a full-monodromy family (A32).
Lifting the class is open above the stated ramification and can't be assumed.

**Routes not tried in the run, as far as its question register and statements show (its ledger was not searched).**
1. Reduce every ambient to the supersingular one. Specialize (X, B) to a supersingular abelian variety with smooth or
   semistable axis. There the ambient sign is a theorem, so only the axis is left (compare H9-T8b, which specializes to
   finite fields only).
2. Make C44-A06 uniform. Over the bounded Chow variety of cycles of degree at most D, find t₀(D) beyond which the signed
   Gram form on all their primitive projections is positive, intersecting cycles included (excess bundles in place of
   c_top of the normal bundle).
3. Move a class to a generic point of its own locus. The sign is constant on a connected family where the class stays
   algebraic. Compute the monodromy on that locus's residual system and apply the one-direction criterion A15 there.
4. Extend the torus argument to smaller Frobenius tori. Classify the tori whose invariants in W^{⊗2} are still spanned
   by graphs and known centres, and prove the sign there.

**The first steps for the prompt.** Write out and check the general main theorem (INT-C44-2) and Th. 4 for powers of an
elliptic curve (INT-C44-1). Then attack the question above. With the A14 centre, INT-C44-2 and A31s/A31t together give
one fourfold with Hodge type and Tate on all powers and a primitive algebraic class with no lift in the stated
ramification range, once the A31 chain is checked.

---

## Before publication

- Statement-level items above get a proof check or go into the paper's part of unchecked findings.
- Literature search (Hexagon included): Hodge type on all powers, torus arguments of Zarhin type, Th. 4 on incidence
  Picard varieties.
- Scan 004 is to be looked at beside the transcription before Th. 5 is quoted.
- Use the text of record: "ensemblistement", "Connu tel quel", "isogénie". J.tex still reports older conflicting
  readings at these three places.

## LaTeX sources to attach

- `P`, `J`, `S`, `H`, `D`, with `RR\RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped\RESEARCH_SA14_SA19_references.bib`.
- `T\44_scan002.tex`, `44_scan004.tex`, `44_scan006.tex`, `44_scan008.tex`, `44_scan009.tex`, and cote 16 scans 036,
  048–050 from the text of record.
- `<local>/Documents\field_experts\intake_20261121\intakes\` the intakes and check events of JAC1964 (both
  parts), SIGN_NEXT (both parts), HODGE_SIGN and C44_POS.
- arXiv e-prints: math/0103175 (Milne 2002), math/0206147 (Chin), 1805.05454 (Entin), 1806.03216 (Ancona), 2009.00533
  (Kahn), 1001.4788 (Zhang), 2512.22788 (Chen), math/0206203 (SGA 1).
- For section II only: 032 and its companion, van Hoften–Sempliner and Milne's report, as in prompt 40's ZIP.

## Never to GitHub: other people's work

- **Inside the C44_POS return**, three extracted texts of publications:
  - `RR\C44_POS_final_20261122T1020Z_unzipped\work\arithmetic\ent2022_issue.txt` (a journal issue of Essential Number Theory);
  - `RR\C44_POS_final_20261122T1020Z_unzipped\work\arithmetic\geisser_hasse_2019.txt` (Geisser, Nagoya Math. J. 236);
  - `RR\C44_POS_final_20261122T1020Z_unzipped\work\arithmetic\shioda_katsura1979.txt` (Shioda–Katsura, Tôhoku Math. J. 31).
- Every attached e-print, PDF or extracted text of the authors above, Saito, Kleiman, Bloch, Katz, SGA and Weil II.
- 032, van Hoften–Sempliner, Milne's report and Markman, as attached to prompts 40 and 51.
- **Inside SIGN_NEXT**, under `RR\SIGN_NEXT_checkpoint_02_20261121T0430Z_unzipped\work\`:
  - `singular_fibres\sga7-i-page340.png`, `page341` and `page347`–`page353`: nine page images of SGA 7 I;
  - `critical_lefschetz\cote16_scan048.png` and `cote16_scan050.png`: scans of the archive;
  - the cached third-party sources `critical_lefschetz\pu_source_cache\`, `integral_fock\cited_sources\`,
    `integral_fock\theta_review\source_cache\` and `singular_fibres\arithmetic_review\source_cache\`.
- **Inside HODGE_SIGN**, under `RR\HODGE_SIGN_final_20261121T0057Z_unzipped\`: `sources\ALPOGE_remark.pdf`,
  `ALPOGE_remark_extracted.txt`, `note_page3.png` (not identified; hold it back) and `evidence\lean_source\`.

## Workbench

Motives and algebraic cycles: standard conjectures, heights, intermediate Jacobians.
