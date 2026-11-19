# SA08, the de Rham notes (cote 136): sweep 3, the topic worked through

## Who did what

Integrated on 19 Nov 2026 by Claude Opus 5.5 at effort max (agent a34c04448e8299803). The readings are by two sweep-3
readers, both Claude Opus 5.5 at effort max, launched by the main session on 18 Nov at about 23:0x UTC with
`../READER_BRIEF_a34c04448e8299803.md`:
- **a1f628dde2f29df92**, scans 2-141: `readings/136_002-141.md`;
- **aa2156d1c23970b0d**, scans 142-281: `readings/136_142-376.md`. It was resumed on 19 Nov for scans 282-376:
  `readings/136_282-376.md`.

All of cote 136 is now read. This file gives the topic in order, with what is proved, checked, wrong and open. The full
checks and the readings decided on the image are in the reading files. CHECK_EVENTS.tsv has 117 rows and
CORRECTIONS.tsv 72. Item ids
are those of `../../sweep2/SA08/WHAT_IS_WHERE.md`.

## What the cote is

Cote 136 is the de Rham bundle.
- **The 1976 IHES lecture plan** (scan 3: "Complexe DR à p.d. et ombres des modules", "Plan conf. IHES en 1976")
  builds an integral, divided-power version of Sullivan's de Rham forms on simplicial sets.
- **The "shadow" theory** recovers modules and cohomology from the weighted PD cochains.
- **Later sheets:**
  - the coalgebra yoga;
  - the automorphisms of the simplicial PD algebra (the "three-data theorem");
  - a hope for Steenrod operations;
  - the four complexes of divided-power algebra.

Reused faces are placed only:
- the SGA 7 IX typescript (Grothendieck, LNM 288), on about seventy faces, page lists in the readings;
- an English typescript of Sullivan's minimal-model work (to verify);
- Manuela Stoia's "Points de Gorenstein d'un morphisme" (scans 216, 218), credited to her;
- administrative sheets of 1975 and a letter of 1971.

**Dating.**
- The 1975 substrates bound the shadow leaves from below.
- Folio 142 (scan 143) is a computer printout separator of 16 August 1982, decided on the image. It sits directly
  before "Le yoga coalgèbres" (144). Reader 2's hunch: scans 144-188 are from 1982-83, near Pursuing Stacks §§117-139.

## The PD de Rham complex of the simplices (SA08-4, SA08-6; scans 4-12, 227-241)

**The construction.**
- Sullivan's forms Q[X_0..X_n, dX_i]/(ΣX_i − 1, ΣdX_i) do not make sense over Z.
- Repair: a PD triple (S, J, t), and the universal choice S = k{T}, t = T. This gives
  C^{••}_DRpd = Γ^•Φ ⊗ Λ^•Ψ, with cochains Hom(X_*, −) (scans 6-9).
- "½-simplicial" means simplicial, with degeneracies (SA08-6).

**Checked** (reader 1, CE001-CE004):
- Φ = cosk_0(k) is contractible.
- Ψ ≃ K(k,1), and Λ^qΨ ≃ K(k,q) by décalage.
- The weight-n strand is exact.
- So H^{p,q} = H^q(X, k) for p ≥ 0, including the endpoint q = n, by dimension shifting.
- Multiplication by T^{(a)} acts by C(n+a, a), so the cup product appears weighted.

**The weightwise comparison is proved** (reader 2, scan 233, with the compressed step supplied):
H^{p,i}_DRpd(X, k) ≅ H^i(X, k) for i ≤ p, and 0 for i > p.
The completed version for a general base (scans 235-239) holds conditionally on k{T} ≅ Gr*(S).

**Remark a), T = 1 (scan 12), is proved** for his literal cochains of unbounded weight, for every simplicial set
(reader 1, CE008):
- C_DRS(X, k ⊗ Q) ≅ C^{••}_DRpd(X, k)/(T − 1).
- With finite weights it fails (the Pro notes L019).
- It was open in Michel Hua's project and in the Pro notes.

**Divided powers on shadows: the CP² test.** H^*(CP²; Z) admits no PD structure, but its shadow algebra does. The
weight parameter absorbs the factorials. This is consistent, but descent of the PD to cohomology is not proved.

**Wrong, decided on the image (all his slips):**
- scan 9: "p = 0" for p ≠ 0;
- scan 10: H° for H^q;
- scan 8: the "inclusion diagonale" arrow is k_* ↪ Φ, written right to left;
- scan 239: Γ^p(Ψ) "≃ K(k,p)" is false for p ≥ 2. It is contractible when p! is a unit, and not for k = Z or F_2;
- scan 241: the valuation criterion is corrected. The equivalence holds iff i+1 ≢ 0 mod p².

## The shadows: the rigidity of the tail (SA08-7; scans 20-45, 244-281)

**Proved on the pages and checked:**
- Lemma 1 (Kummer-Lucas), Cor. 2, Lemma 2.
- **Théorème 1** (scan 23): if C(j,i)(x_j − x_i) = 0 for j > i ≥ N, then x_i = x_N. The one-step proof through p^r − 1
  is his own "Présentation plus simple".
- Cor. 1, i.e. the recovery of M from its shadow.
- **The weighted theorem (scans 27-34)** is complete and correct once three slips are read. Michel Hua's project
  reports a Lean proof (credited; not run here).

**The Ext corollary (scan 27)** is unproved on the pages. Reader 1 checked it in the first case (k = M = F_p, i = 0,
N = 1). It holds for graded modules, and the grading is essential: ungraded, Hom(S^+, S) ⊋ S.

**Wrong:**
- **Scan 26:** the adjunction display is false as written (decided on the image). It is φ_N, the right adjoint of τ_N,
  that is fully faithful, not the inclusion.
- **Scan 26:** the negligible class is not thick.
- **Scan 45:** "∩ nN est le plus grand sous-module divisible" is false. The first Ulm submodule need not be divisible.
  The corrected statement holds; Michel Hua's footnote and the Pro notes say the same.

**Scans 244-281** (reader 2):
- The adjunction chain q ⊣ i ⊣ τ ⊣ ρ is checked.
- The three negligible classes, the essential image of φ_∞ and the Ext vanishing (265) are checked.
- The reconstruction of a complex from its shadow (267-273) is formal; its "?" on the derived unit stays open.
- The equalizer recovery and "τ_N i_* pl. fid." (275-279) are checked in wave 2; see the section on scans 282-376.
- Reader 2's hunch H2: these shadow categories study exactly the PD-Rees module P ⊗ I^{[N]}.

## Integration of forms and the de Rham theorem (SA08-9; scans 48-72)

**Checked:**
- The normalized cochains of Δ^m are Λ^{*+1}Φ ⊗ M. So the weight-zero corner of the PD complex is the cocycles:
  C^{0,q}(X) = Z^q(X; k).
- **Prop. 1, integration (scans 54-56):** a unique Stokes system, under exactly H^N(A_N) = H^{N−1}(A_N) = 0.
- The universal Stokes target (scans 65-69).
- His de Rham theorem (scans 70-72), the classical Weil-Cartan proof in his integration language.

**Wrong for arbitrary F:** "que F soit loc. constant ou non" (scan 64). The Pro notes R061 give a counterexample;
for locally constant F the statement is right.

## Faisceautisation and De Rham structures (SA08-10, SA08-5, SA08-3; scans 13-18, 74-106)

**Checked:**
- The bigraded algebra in the simplicial topos (scans 74-78).
- The weight-zero product is C(p+q, p)·cup (CE027). It is strictly alternating with no contradiction, and it is the
  weight factor of the shadows.
- The canonical p = q = 1 splitting exists and is unique.
- The theorem of scans 80-83 in a topos, including the endpoint.
- Functoriality and independence up to derived isomorphism (scan 89).
- DR_sp(X, k)_0 is a point (scans 96-98), because k{T} is an initial object.
- "flasque + plat ⇒ homotope à 0" is false (scan 100), as he says: in Δ̂ the constant k_* is Γ-acyclic and not
  contractible.

**Readings decided on the image:**
- scan 75: the ink has "pq ≠ 0", but the statement needs (p,q) ≠ (0,0);
- scan 89: Γ^*(Ψ) is his slip for Γ^*(Φ);
- scan 75 "flasque si p ≥ 0": undecided; p ≥ 1 is needed.

**Open, his own:**
- the cosimplicial topos "Non" (scan 91, double-underlined, no reason given);
- the connected groupoids "définis par deux groupes" (scans 102-106);
- the products and divided powers on DR^{0,*} (scan 77);
- minimal models, Künneth, and the operations (scans 13-18).

**SA08-3, the integral model against Sullivan,** is his question ("Mais il paraît qu'il y a des ths contre ! On va
pourtant y arriver"). The modern answers are Mandell (E∞ cochains) and the binomial route (Toën; Horel). See HUNCHES
H1.

## Generalized de Rham functors and the dual coalgebra model (SA08-35, SA08-12; scans 111-141)

**Scans 111-121** are a programme: admissible de Rham theories, and a uniqueness conjecture ("connexe et simplement
connexe ?"). Nothing is proved beyond the reduction to the simplices.

**The dual coalgebra model (scans 123-141) is checked.** It realizes the "cobigèbre à copuissances divisées" promised
on scan 15. The divided-power integral of a monomial is t^{(n+Σi)}, by Dirichlet's integral, so his "γ_{0,…,0} =? 1"
is answered yes (the Pro notes O05, re-derived).
- Slip (scan 139): Λ^n([y]') ≅ Λ^{n+1}([y_0..y_n]).

## Polynomial laws, coalgebras and comodules (SA08-24; scans 144-159)

**Checked:**
- V(N) = Spec Sym*N is fully faithful.
- Coalgebras ⟷ bilinear laws.
- Alternating ⇒ anticommutative (not conversely in characteristic 2).
- The free-coalgebra criterion: modules over the dual algebra come from comodules iff they are "rational".

**Wrong:**
- **Scan 152 (his slip, decided on the image):** "l'anti-crochet de deux antidérivations est une antidérivation"
  should be "une dérivation". On scan 222 he writes it correctly.
- **Scan 155 (a gap, corrected):** flatness of C does not give injectivity of C ⊗ k^I → C^I by his passage to the
  limit.
  - Re-proved for k noetherian.
  - In general it is a Mittag-Leffler condition (Raynaud-Gruson; to verify).
  - His free case needs no flatness and is correct.

## The automorphisms of the simplicial PD algebra: the three-data theorem (SA08-25; scans 162-212)

**The theorem (scans 162, 164).** Homomorphisms φ: 𝒜_S → 𝒜_{S'} ⟷ data (φ_0, A', (B'_i)) under three conditions:
1. φ_0 respects divided powers on t;
2. β(A') = φ_0(t);
3. (2B'_i)J' = 0.

**The missing condition.** The list omits the dX_0-component of his own relation (1):

  (M) c_{ij} B'_{i+j} = A'^{(i)} B'_j + A'^{(j)} B'_i for all i, j ≥ 1.

- It was found by the Pro notes of MPL_136_142-188 (N029-N031) and confirmed by reader 2.
- On scan 186 he concludes "B_i ∈ S{X_0} sans autre condition !". The theorem, Cor. 5, and the description of Ω inherit
  the error. Michel Hua's project reproduces the unrestricted list.
- Counterexample: over F_2, A' = X_0, B'_2 = 1.
- **Refined statement (reader 2):** (M) says that X^{(i)} ↦ B'_i is a derivation along φ_A. So:
  - over a Z-torsion-free S', every homomorphism commutes with divided powers;
  - over an F_p-algebra, the B's are free on the B'_{p^m}.
- His own vertex-reversal check on scan 192, carried one step further, gives (M) at i = j = 1.

**Further corrections:**
- **The margins of scans 170 and 172** ("vide si 2 inversible") are wrong in general. Reader 2 gives a reduced
  counterexample over F_3.
- **Ω (scan 178) is corrected:**
  - with (M) and 2B = 0, the B-part is free on B_1, B_2, B_4, … with a convergence condition;
  - it is an ind-scheme ∏_{(j,h)} ⊕_m ₂G_a, not an affine scheme;
  - the "2" before the first G_a is his slip, decided on the image.

**Readings decided on the image:**
- scan 162: no exponent i on the 2;
- scan 166: the coefficient C_{j,h} is written, so the footnote in Michel Hua's project is not borne out;
- scan 200: "est un n. div. de zéro".

**The determinant and the action on cohomology.**
- Δ(φ) = a_{10} is multiplicative.
- The converse (Δ a unit ⇒ automorphism) is unproved on the page; a proof is sketched in the reading.
- **Open:** "seules les op. évidentes (se factorisent par Δ)" (scan 180).
- **Open:** the hope for Steenrod squares from the characteristic-2 automorphisms, with his marginal "Non" (scan 182).
  This is package SA08-RP1.

**The continuation (scans 190-212):**
- the same omission of (M);
- G_k is a monoid ("groupe" struck twice);
- G_k ∩ H_k is non-trivial exactly when k has torsion, the torsion that rationalization misses;
- the semi-direct decompositions carry his "(??)" and stay open.

## The alternating PD theorem and the four complexes (SA08-15; scans 215-233)

**Scan 215** states, without proof, the free alternating PD algebra on M^0 ⊕ M^1. It is known in substance (Cartan
1954-55; Roby 1965; Berthelot LNM 407; to verify). The extension rule forces u^{(i)} = 0 for odd u and strict
commutation (checked).

**The four complexes (scans 219-221)** are checked in rank one:
- de Rham on Sym ⊗ Λ is exact over Q;
- Koszul on Sym ⊗ Λ is exact for flat M;
- PD de Rham on Γ ⊗ Λ is exact for flat M in every characteristic;
- PD Koszul is exact over Q and not in characteristic p, whence his "histoire d'opérations de Cartier" (open).

**Wrong as literally written (scan 222):** "H^n = 0 si n·1 inv.". The n is the weight, not the cohomological degree.

**His "est-ce vrai ?" on LΛ^i (scan 229)** is true for L = M[1] by décalage, which is the case he uses, and false in
general.

**Wrong (scan 229, NB b):** "Γ^i(Ψ*) et Sym^i(Ψ*) … sont des K(k,i)". The insertion "⊗Ψ*" above the line, probably
⊗^i, is the correct variant.

## The integral obstructions (SA08-11)

The weighted construction escapes the tests that sink unweighted integral commutative cochains:
- BC_2 over F_2;
- Cenkl's obstruction;
- CP².

The reasons are the shadow PD on CP² and the weight-zero product C(p+q, p)·cup.

## Scans 282-376 and the rest of 235-281 (wave 2, 19 Nov)

**Who:** reader aa2156d1c23970b0d, resumed on 19 Nov for wave 2. Its reading is `readings/136_282-376.md`, with 27
check events and 17 corrections.
- It read MPL_136_282-327 in full, K136-01 to -03 (scans 328-376) in full, and the notes and doubts of
  MPL_136_235-281.
- It compared the stopped Pro run of scans 328-370 at named points only.

**The shadows, finished (275-279):**
- The equalizer recovery of scan 275 holds for every k-module M. It is re-proved by Lucas and a finite Bézout relation;
  the Pro notes N21-N22 prove it with other indices.
- **Decided on the image (279):** the ink has τ_N, which makes "Le foncteur τ_N i_* est pl. fid." trivial. The
  substantive σ_N statement, which the line before sets up, is also true.

**Scans 282-327:**
- **Graded modules and the four adjoints q_N ⊣ i_N ⊣ τ_N ⊣ φ_N (287-299)** are checked. This is the clean version of
  244-250. The negative tail of scan 299 is checked, with its exponents corrected.
- **The universal constructions (305-318)** are checked: colimit-preserving functors Ss → A are cosimplicial objects,
  and Z(X) is universal for additive categories with colimits. Scan 318 explains why the multiplicative structures and
  Λ^i, Γ^i, Sym^i live on simplicial objects and not on chain complexes. That is also the reason for his question on
  229.
- **PD operations on Hom(A, M) out of a coalgebra (320-325)** are checked by Yoneda. On 325, "(λf)^{(p)} = λ^p f^p
  (automatique!)" is right with f^{(p)}.
- **Projective structures on curves (326-327):**
  - Decided on the image (326): b = ½(λ − λ^{-1}) is his slip, for (λ − λ^{-1})/(2i).
  - The uniformization theorem of 327 is checked.
  - **His boxed task, "Trouver une connexion intégrable (alg) canonique sur P(Ω^{-1} + Ω)",** has an obstruction. On the
    split bundle there is no holomorphic connection for g ≥ 2 (Weil-Atiyah, to verify). The intended object is the
    nonsplit jet (oper) bundle; the Pro notes N49-N50 reach the same conclusion.

**Scans 328-376:**
- **328 (checked).** Lifting the uniformizing representation to SL(2,R) gives degree g−1, the degree of a theta
  characteristic. This is the lift the oper bundle of 327 needs.
- **329-335 (checked; answers his question ① of 324 for flat A).** For a flat cocommutative coalgebra A, the iterated
  coproducts u_p satisfy both relations of his ②. So f ↦ π_p∘Γ^p(f)∘u_p is a PD structure on Hom(A, J), including the
  composition axiom he left open. A non-flat counterexample is in the Pro notes N43.
  - Slip (334): the coefficient of γ^p(γ^q(x)) has p and q swapped. γ²(γ³(x)) = 10γ⁶(x), not 15.
- **337-338.**
  - The ranks are checked.
  - "k en degré n, n+1" is his slip for n−1, n.
- **343.**
  - The recovery of a simplex from the multiplicative functor (Dedekind-Artin) is checked in outline.
  - The extension to all X ("Iso ?") is open.
- **346.** The operator algebra of the one-variable PD de Rham complex (ten relations) is checked. It is the Euler
  homotopy in operator form.
- **348-352: "½-algèbres différentielles"**, products defined when one factor is a cocycle.
  - Ex. 2 is checked.
  - His question of 352 (extension to a ½-algebra, and its indeterminacy) is open. See package SA08-RP6.
- **357-361:** Eilenberg-Zilber and the Steenrod construction. Standard statements, correct as transcribed.
- **362, the décalage, checked.** L_r Sym^i K(M, n+1) ≃ L_{r−i} Λ^i K(M, n), the Quillen-Illusie décalage. It settles
  hunch H9 and answers his question on 229 for L = M[1].
  - The first of his three Koszul sequences is not exact over Z, but nothing uses it.
- **365.** "Sq¹Sq² = Sq³ + Sq²Sq¹ (?)" is false: Adem gives Sq¹Sq² = Sq³. Michel Hua's project found this first,
  credited. The "(?)" is in the ink.
- **370.** Milnor's K_2. Michel Hua's correction "K_2(R) = H_2(E(R))" is credited and agreed.
- **373 (checked).** K(G, n) = G ⊗ Λ^nΨ_* for every n ≥ 1, which identifies the cocycle objects of the cochain model.
- **374-376.** Operations with G_a coefficients (P^0 = Frobenius) and Ext^i(G_a, G_a). These follow Breen's method and
  statements; they are not checked here (package SA08-RP5).
  - "Ext^1(G_a, G_a) = 0" is meant modulo F-torsion.

**Codicology:**
- 344, 347 and 354 are blank sheets, and 356 is a blank ruled sheet, so nothing is missing from the packages.
- 349-353 are an English typescript on minimal models and non-abelian periods, with "Theorem D: (Generalized de Rham)"
  and Chen's iterated integrals. It is placed only, to identify.
- Who wrote the notes on 357-376 stays open, as in Michel Hua's project.

**Readiness (the reader's verdicts):** no range from 235 to 376 is ready for the edition yet.
- 235-281: an image pass over 127 low rows, and a collation with K136-16 to -18.
- 282-327: a pass over the doubts, and a second witness.
- 328-370: a line-by-line collation of the Codex Work and Pro witnesses.
- 371-376: a second witness.

## How the topic connects

- The PD de Rham complex (SA08-4) is the object of the shadow theory (SA08-7) and of the faisceautisation (SA08-10).
- Cote 137 (SA09) builds its abstract home. The weightwise comparison is proved on both sides.
- The automorphism sheets (SA08-25) are where Steenrod operations were hoped for.
- The three-data theorem needs condition (M).
- The binomial-ring literature (Toën, Horel) and Mandell's theorem are the modern frame (HUNCHES H1).
- The dependencies, closed by reading, are in DEPENDS.tsv.
