# SA06 (Théorie des motifs II), sweep 3, stretch c14_c15rest: cote 14 (all scans) and cote 15 (scans 87-95, 109-126, 138, 170-206)

Merged on 19 Nov 2026 by c14_c15rest (Claude Opus 5.5 at effort max; launched by agent a28ea31fa17dd65e1, Claude Opus 5.5
at effort max, at the main session's word). Three readers, all Claude Opus 5.5 at effort max:

| Part | Reader | Scans | Text read |
|---|---|---|---|
| 1 | c14_c15rest_part1 (agent a0012f1ff34e51fa6) | cote 14, 2-58 | Pro MPL_14_002-044 (2-44) with Codex K14-01, K14-02 as witness; Codex K14-04 (45-58, no Pro) |
| 2 | c14_c15rest_part2 (agent a18fb27f7c0e6640f) | cote 14, 59-132 | Codex K14-05, K14-06 (59-86, no Pro); Pro MPL_14_087-132 (87-132) with Codex K14-07, K14-08, K14-09 |
| 3 | c14_c15rest (this reader) | cote 15, 87-95, 109-126, 138, 170-206 | Pro MPL_15_087-138; Pro MPL_15_170-194r; Pro checkpoint MPL_15_139-194 (172-178); Pro MPL_15_195-228+18_002-017 (195-206); Codex K15-03 to K15-08 and B15-01 as witnesses |

The three part files follow below unchanged, headings shifted one level. Each keeps its own labels (part 3's "P3-nn" is
row nn of c14_c15rest_part3_CHECK_EVENTS.tsv; in c14_c15rest_CHECK_EVENTS.tsv the rows come in the order part 1, part 2,
part 3). The part files stay in this folder. Sweep 3 had read cote 15, scans 34-86, 96-108 and 128-137 before (STUDY.md);
within cotes 14-15 it has not read cote 15, scans 1-33, 139-169 and 207-228.

**Counts.** 185 pages read (part 1: 54; part 2: 68; part 3: 63; reused leaves identified in one line each, not studied);
125 check events (36 + 41 + 48); 66 corrections (17 + 24 + 25); 21 hunches (c14a-H1 to H7, c14b-H1 to H7, c15-H1 to H7).

## Main findings (details and check events in the parts)

1. **The letter to Serre (14:44-47) is printed, and its conjectures, as written, are false.** It is the letter of
   27 August 1965 in the Correspondance Grothendieck-Serre (SMF 2001), pp. 232-234, headed "Thil, 27.8.1965". It states
   conjectures A, A', A'' and B for cycles modulo algebraic equivalence. On a general quintic threefold the difference of
   two lines is homologically trivial and of infinite order modulo algebraic equivalence (Griffiths 1969), so A fails at
   the very case "i = 1, n = 3" the letter names, and A', A'' and "tau-équivalence = équivalence numérique" with it. The
   refined statements are the cohomological ones the letter names as a fallback: the standard conjectures as printed in
   1968-69. The printed notes do not say so. The archive copy also differs from print ("A et B impliquent" where print
   has "B implique"; a typed N.B. on twists that print lacks). (Part 1, item 8. Checked again in the merge: the image of
   xi: C^1 -> C^2 is Q.H^2, which has non-zero degree, so it misses the difference of two lines.)
2. **The same quintic breaks the Chow-group Lefschetz programme of 14:111-117**, item ③ for cycles modulo algebraic
   equivalence (rank 1 against the Griffiths group, of infinite rank by Clemens 1983). The 0-cycle conditions he writes
   ("si équiv. rat. = équiv. d'Albanese") are exactly what Mumford (1969) and Bloch-Srinivas (1983) settled negatively;
   the "rectangle" relation of 14:118 and 14:126 fails over C (Mumford, Bloch), as his letter of 20 November 1968 records
   (Pro note Z03). (Part 2, items 9-10.)
3. **14:52-71 proves the Lefschetz standard conjecture in degree 1, l-adically, over any algebraically closed field**
   (Cor. 2.6 and Prop. 2.7, with the integral denominators of Cor. 2.4-2.5), as the letter announces on 14:51. His
   Question 2 of 14:71 (an integral cycle inverting H^(2n-1) -> H^1(B_X)) reduces to abelian varieties and there to the
   algebraicity of theta^(g-1)/(g-1)!, open for a very general principally polarized abelian variety of dimension >= 4.
   (Part 2, item 1, hunches c14b-H1, c14b-H3.)
4. **15:205 states the naive general Hodge conjecture that he refuted in 1969.** "La partie de niveau <= rho ... n'est
   autre que" the rational space intersected with a Hodge piece and its f_infinity-image. For E = C/(Z + Z tau), tau a
   non-real cubic irrationality, and F = h^1(E)^(x)3, that intersection is 5-dimensional (odd), not a Hodge
   substructure, while the level-1 part is 4-dimensional. Refined statement: the largest Q-sub-Hodge structure in the
   Hodge piece (Topology 8 (1969)). With the Steinberg typescript of 1965 reused on 15:95-109 and used on 15:191, this
   places 15:191-205 between 1965 and 1968. (Part 3, §H; hunches c15-H2, c15-H3.)
5. **Real fibre functors over finite fields (15:117-125).** Propositions 1-2 (a real fibre functor exists iff the Tate
   character is primitive; otherwise U = U^0 x mu_2, Serre's case) are right for commutative G and fail for GL_2; the
   Cor. of 15:119 is wrong as written (right: epsilon = pr_2^2, j = inj_2); the privileged polarizations i|mu_2 of 15:123
   are undefined when the slope cocharacter has even denominators, which happens even with only even degrees (q = 25,
   lambda = 15 + 20i, slope 3/2); his caveat on 15:121 is right, and a weight-0 example is supplied (Q(i, sqrt 5),
   p = 5). (Part 3, §C.)
6. **The Weil-number torus (15:88-114).** Compactness of Ker(epsilon) is the Riemann hypothesis for the generating
   Frobenius (15:90-94, re-proved both ways); "nu factors through G'" (15:112) is refuted (2 nu = phi nu'' + v_𝔭(q) j);
   lifting the weight-0 Frobenius to the norm-one torus is obstructed, up to a 2-group, by the subgroup of Cl(L)
   generated by the minus-divisors at p, which answers his "demander à Serre ?" precisely. (Part 3, §§A-B.)
7. **Ampleness (14:93-100).** The margin "critère numérique: D.C > 0, D^d > 0" is false for d >= 3; "xP > 0 => x ample?"
   is answered no by Mumford's ruled surface, and "nef . nef >= 0?" no by Debarre-Ein-Lazarsfeld-Voisin (2011).
   (Part 2, item 8.)
8. **"Calculs de cohomologie absolue des motifs de Tate" (15:172-178)** computes a theory with ℍ^0 = ℍ^1 = Z for F_q
   and H^3(Spec Z, Q(1)) = Q: the integral Weil-étale picture (hunch c15-H4); the margin "n != 0" of 15:173 should be
   n != 1, as his own 15:174 computes. A Brauer-group draft numbered §5 (15:176, 179) is his. (Part 3, §F.) The SA05
   reader read 15:172-178 independently (sweep3/SA05/readings/c15b_c12_c11.md §1.6, filed under SA05-10) with the same
   checks and correction, and answers his "[est-ce nul ??]": no, H^1(Spec Z, Q(n)) = Q for odd n >= 3 (Borel).

## How the parts connect

- One counterexample, three places: the Griffiths quintic refutes the letter's Conjecture A (14:44-47, part 1) and item ③
  of 14:112 (part 2); the cohomological fallback the letter names is what survived. The 1969 papers (Griffiths;
  Grothendieck, Topology 8) refute forms that cotes 14-15 state in 1965-68: also 15:205 (part 3).
- Effectivity: part 1's effectivity structure (14:2-15; c14a-H2: effectivity read through Frobenius integrality) is what
  15:121 ("La structure d'effectivité sur M est déterminée grâce à i") and 15:187 (the effectivity cone dual to the slope
  cocharacters of the Frobenius at closed points) carry out over finite fields (part 3).
- The generalized Hodge conjecture: part 1's c14a-H1 (M^+ = P(mu) as its motivic form) and part 3's 15:205 (its naive
  form, refuted) are the same question at two dates.
- Tate classes: part 1's "Astuce de Tate" (14:40-42), part 2's unfinished Question of 14:89 (algebraicity of classes in
  H^1(A) (x) H^1(B)(1), i.e. Tate for divisors on A x B) and part 3's Weil-number pages are one line of work (SA06-4,
  SA06-9).
- The degree-1 Lefschetz proof (14:52-71, part 2) is what the letter (14:51) announces (part 1).
- 15:117's margin "On n'utilise que les éléments de structure 1, 2, 3" refers to the numbered "éléments de structure
  motiviques" of the cancelled title of 14:2 (part 1).

## Corrections to sweep 2's placements (from the three parts)

- SA06-3 should drop 14:2-3, 6, 8-9 and add 14:17, 48, 50-58 (part 1); SA06-4 should drop 14:5-8, 19, 50-54, 56, 58
  (part 1); SA06-2 should drop 14:28, 48-49 (part 1); SA06-1 is not on 14:2-58 (it is the Pro notes' research lens).
- SA06-11 (reused leaves) should drop 14:3, 5, 21 (his pages) and 14:114 (his cancelled remark) and add 14:75-86 (parts 1-2).
- SA06-14 is on 15:170, not 15:179; SA06-16 is "absolute cohomology of the Tate motives over F_q and Spec Z, and a
  Brauer-group draft", not "curves over finite fields"; SA06-15 on this stretch is 15:182-205 (Frobenius distribution and
  the fibre functors at all places) (part 3).
- 14:43 is not blank (a faint typed impression, by Michel Hua's project a pale duplicate of the letter's first sheet); the
  40-dpi ink-profile test used to brief the readers missed it (part 1).
- 15:172-178 and 15:195-206 have Pro transcriptions (a checkpoint, and MPL_15_195-228+18_002-017), which the launch prompt
  did not list (part 3).

## Deliverable state of the stretch

| Scans | Passes | Ready for a transcription edition? |
|---|---|---|
| 14:2-44 | Pro + notes; Codex K14-01, K14-02, K14-03 | yes, after part 1's corrections C1-C10 (the Pro text misreads 14:3-15; Codex is the better witness there) |
| 14:45-47 (letter) | Codex K14-04 only; compared with print | yes, after a check of K14-04 against the image |
| 14:48-58 (Sorites) | Codex K14-04 only | no: a second reading on the image is needed |
| 14:59-86 | Codex K14-05, K14-06 only | no: the 13 handwritten pages need a second full transcription |
| 14:87-132 | Pro + notes; Codex K14-07, K14-08, K14-09 | yes, after merging the Pro doubts with the Codex readings |
| 15:87-95, 109-126, 138 | Pro + notes; Codex K15-03, K15-04, K15-05 | after collation, with the readings decided in part 3 (110, 112, 119, 121) |
| 15:170-171, 179-194 | Pro + notes; Codex K15-06, K15-07, B15-01 | after collation (170 margins, 179 numbering corrected in part 3) |
| 15:172-178 | Pro checkpoint only (no notes); Codex K15-06 | needs the final Pro pass or a second pass |
| 15:195-206 | Pro (two chats) + notes; Codex K15-08 | after collation (195, 197 decided in part 3) |

Open readings on his pages: part 3 counts 464 \unsure and 7 \illegible marks on its 36 pages of his; parts 1-2 list their
open readings by page. Every Codex folder also carries Work math notes and sheet notes.


## SA06, cote 14, scans 2-58: sweep 3 reading (sub-stretch c14_c15rest_part1)

Claude Opus 5.5 at effort max, `c14_c15rest_part1`, sweep 3 reader; launched by `c14_c15rest` (Claude Opus 5.5 at effort
max) at the word of agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max). Started 19 Nov 2026 (UTC). Written as I go:
the items appear in page order as each page is read.

Witnesses. Scans 2-44: the Pro package `MPL_14_002-044` (the text), its notes and doubts files; the Codex web returns
`K14-01` (2-15) and `K14-02` (16-30) as second witness where compared below (`K14-03`, 31-44, exists and was not
compared in this reading). Scans 45-58: the Codex web `K14-04` pages (the
text: no Pro transcription), its math notes, notes and doubts. Michel Hua's project (`transcripts/14/14.modern.tex`; his
page p = our scan p + 1) as a credited witness only. Scans 18 and 23 blank; 43 listed as blank, but see item 10; scan 1 the archive's cover sheet (not read).

### Pages, in order

#### 1. "Structure d'effectivité" (14:2-3, 5, 7, 9, 11, 13, 15): SA06-2 (cote-14 part)

**The document.** 14:2 is a title sheet: a cancelled title "Les éléments de structure motiviques & leur interprétation en
termes de groupes algébriques sur Q", replaced by "Structure d'effectivité" (both witnesses agree). The cancelled title says
what the dossier continues: structures 1°-3° on the motivic group G are not on these pages, and "4°" opens 14:3. His
handwritten sheets are the odd scans 3-15; the even scans 4-16 are their backs, a reused English typescript (item 2). The
archive sheet numbers ({1}...{14}) run with the scans.

**What he does.**
- 14:3. Structure 4°: a strictly full subcategory M^+ of the motives M (effective motives), stable under tensor products,
  sums and subobjects, containing Λ(-1), such that every E has E(-n) = E ⊗ Λ(-1)^{⊗n} effective for some n. This is
  equivalent to a cone K^+(G) in the ring of rational characters K(G) (gloss: "l'anneau des car. rat/Q"), containing 0 and
  ε, stable under multiplication, **and generated by the elements of the canonical basis (classes of irreducible
  representations over Q) that it contains** (a margin insertion after "et"; the Pro text's "et λ(?) ... Suggéré par(?)
  l'idée de la base canonique" is a misreading, decided on the scan: correction C1). Further axioms: every effective E has
  positive weight grading; margin: the structure should come from a structure of given type on G^0; margin "Axiome": for
  every i, only finitely many types of effective motives of weight i "???"; the effective motives of weight 0 are those on
  which G^0 acts trivially (the ink favours the Codex reading "En tous cas, on veut que ... soient tels que G° opère en eux
  trivialement": a requirement, not a statement). Definition: a cocharacter i: G_m,C -> G_C is effective if every effective
  E_C has its i-grading in degrees >= 0.
- 14:5. If i is effective, so are its G(C)-conjugates and its Aut(C)-conjugates, in particular ī. For a given i, the full
  subcategory P(i) (the E with E_C of nonnegative i-grading) is strictly full, stable under sums, subobjects and ⊗,
  contains 0, contains Λ(-1) if ⟨i,ε⟩ >= 0, and every E has E(-n) in P(i) for some n if ⟨i,ε⟩ > 0 (boxed). The ink reads
  E(-n), as on 14:3 (correction C2: the Pro text has E(n)). Intersections of P(i) give structures M^+ satisfying "aux
  axiomes considérés" except perhaps the last one (the twist condition).
- 14:7. The effective i correspond to conjugacy classes. With T a maximal torus, Γ = Hom(G_m,C, T_C), W = Norm(T)/T,
  W' = Aut(G,T)/T, W'/W = Aut ext(G): a cone Γ^+, invariant under W "(mais peut-être pas pr W'!)", **containing j**
  (correction C3: the Pro text reads "γ(?)"; the ink is j, as Codex reads), in the half-space ε >= 0. Γ/W =
  [Hom(G_m,G)/G](C) is the set of C-points of an unramified Q-scheme, so π_1(Q,C) acts (through a finite quotient) and the
  cone is π_1-stable.
- 14:9. Effectivity structures that are intersections of P(i) over a family of i are equivalent to "cones" in Γ' that are
  π_1-invariant, contained "strictly" in the ε-half-space (margin: "i.e. ε est 'intérieur' au cône polaire !"), contain
  "la classe de i" (the ink is i; the sense requires j: correction C4, a slip of his pen, by 14:7 and the N.B. below), and
  satisfy a saturation condition "que nous ne précisons pas ici (est-elle automatiquement satisfaite ?)". Main case:
  M^+ = P(i_1), with i_1 as in 3°. N.B.: the invariant cone generated contains j and lies in the ε-half-space, since
  i_1 ī_1 = j and ε i_1 = id. Hence a map I(G) -> Eff(G) (a cancelled "Pol" in the target).
- 14:11. "en particulier, tenant compte de 3°": I^a(G) -> Pol(G) × Eff(G), with I^a(G) glossed as "les i: G_m,C -> G_C
  définissant une polarisation, modulo action de G(R)" (the superscript looks like a; Codex reads α). Questions: is
  I(G) -> Eff(G) injective? Can the effectivity structures that come from motives always be described by one i_1, i.e.
  are they in Im I(G)? Margin N.B.: whether a structure can be described by an element of I(G) (resp. I^a(G)) is intrinsic
  to M, independent of the fibre functor. Further: look at twisting by a torsor, and at the case where G with its 4
  structures comes from a motive over a connected S with a point ξ ∈ S(Q), using the de Rham functor. "Regarder G
  commutatif ! G = Sl(2,Q) !" (the ink reads Sl, as both witnesses do; see "What is wrong"). Deeper arithmetic properties
  through Frobenius elements and the interpretation of 3° and 4° in their terms.
- 14:13. (A cancelled head: a point ξ ∈ S(k), k of characteristic 0, defines fibre functors H^**_ξ (Hodge) and H^*_ξ (de
  Rham).) The torus case: T over Q given by an admissible π-module M (free of finite type), ε ∈ M^π, "i ∈ M̌^π,
  ⟨i,ε⟩ = 2". Here i is the weight cocharacter (the j of 14:7 and 14:9; the Hodge cocharacter has ⟨i_1,ε⟩ = 1).
  Representations are the π-invariant elements of Z(M)^+. Polarization data depend only on T_R (the ink reads "ne dépend
  que du tore réel T_R", as Codex does; the Pro text "se décrit pr des str. sur T_R" is a misreading, with the same sense).
  T_R is an extension of a split S by a compact U, ε is trivial on U, so ε_S and j_S live on S, and S inherits a positivity
  structure. **Claim: dim S = 1, i.e. Ker ε is compact.** The proof he began (reduce to dim S = 2, S = G_m × G_m,
  i(λ) = (1, λ^α), ε(λ,μ) = μ^β, αβ = 2) is struck through.
- 14:15. "Détermination du groupe des caractères rationnels sur Q": T_C = D_C(M), with π the finite quotient of π_1 acting
  faithfully on M; Z(M) the virtual characters; K(T) = Z(M)^π, of finite type over Z; Z(M) is the affine ring of
  S = D_Z(M), K(T) that of D_Z(M)/π. A guess, "effective characters = those >= 0 on S(R)° ??". Then: how to define a
  motivic effectivity structure ("motivique": the Pro reading "intrinsèque" is wrong, correction C5)? The standard
  procedure is to fix i_1, i.e. i_1^*: M -> Z, which gives α: G_m,Z -> S; the condition on χ ∈ K(T) is that χ∘α ∈
  Z[t, t^-1] be a polynomial, i.e. stay finite as t -> 0 in R^*. On the finiteness of the effective characters of given
  weight: "On ne peut pas simplifier dans cette question Q pr R, car si T est de dim >= 3, la [notion|relation] de finitude
  correspondante est Fausse" (correction C6: the Pro text reads "la notion(?) de partie(?) compacte est Fausse", Codex reads
  "Cela ne tient pas simplement du calcul arithmétique Q par R"; the ink has "On ne peut pas simplifier ... de finitude
  correspondante").

**What is proved, and what I checked.**
- The closure properties of P(i) on 14:5 and the twist criterion: Λ(-1) ∈ P(i) iff ⟨i,ε⟩ >= 0, and the twist condition
  holds iff ⟨i,ε⟩ > 0, the i-degrees of a given E being bounded. Checked.
- Conjugation: G(C)-conjugates give the same degrees; for σ ∈ Aut(C), E_C = E ⊗_Q C carries the σ-conjugate grading with
  the same degrees. Checked.
- 14:7: Γ/W = [Hom(G_m,G)/G](C) (cocharacters of a reductive G_C are conjugate into T, and T-cocharacters are G-conjugate
  iff Norm(T)/T-conjugate); the Galois action factors through Gal(K/Q), K a splitting field of a maximal Q-torus. Checked
  (known). "Peut-être pas pr W'": not in general; for G = G_m (W = 1, W' = {±1}, ε = id, j = 2) the cone R_{>=0} is not
  stable under inversion. Checked.
- 14:9, margin: for a closed convex cone C, ⟨c,ε⟩ > 0 for every c ∈ C \ {0} iff ε is interior to the polar cone C^∨. This
  is what makes the twist condition survive an intersection over a finitely generated cone (a uniform n, the maximum over
  the generators). Checked. The N.B.: each conjugate σi_1 has ⟨σi_1, ε⟩ = 1 (ε is Q-rational), and j = i_1 + ī_1
  (additively) lies in the cone. Checked.
- 14:3: the cone is generated by the irreducible classes it contains (semisimplicity: subobjects are summands). Checked.
- 14:11, first question, answered (my proof): **with I(G) taken modulo G(C)-conjugation and the Galois action,
  I(G) -> Eff(G) is injective.** The W·π_1-orbit of i_1 lies on the affine hyperplane ⟨·,ε⟩ = 1; the cone it generates
  has a polytope as cross-section, whose vertices form a nonempty subset of the orbit stable under the transitive group
  W·π_1, hence the whole orbit. P(i_1) determines the dual cone (it is spanned by the weights of effective representations:
  for a dominant m in the dual cone, all weights of V(m) lie in conv(W·m)), hence the cone, hence the orbit. (CE 14:11.)
  His own definition of I(G) is in 3°, not on these pages, so the quotient is my assumption.
- 14:11, margin N.B.: two fibre functors give groups whose complexifications are isomorphic canonically up to inner
  automorphism, so the conjugacy classes of cocharacters, the P(i), and the Galois action on the classes are intrinsic.
  Checked (Deligne-Milne, Tannakian categories, LNM 900 (1982), Th. 3.2: locator unverified).
- 14:13: the claim is right. Ker(ε)(R) preserves the form ψ and commutes with the Weil element, hence preserves the
  positive definite form ψ(x, Cy) on a faithful representation: it is compact, its identity component is an anisotropic
  torus, so the split quotient S has dimension 1 (S contains the image of j, on which ε_S is λ^2). As T = j(G_m)·Ker ε
  with finite intersection, "dim S = 1" and "Ker ε compact" (identity component) are equivalent, as he says. He proves the
  same thing in cote 15 (15:84: U = Ker ε maps into the unitary group of a positive involution; STUDY.md §2). (CE 14:13.)
- 14:15: K(T) = Z[M]^π is the representation ring of T over Q (the irreducible Q-representation of a π-orbit O has
  character Σ_{χ∈O} χ: Schur index 1 for tori), finitely generated, and Spec Z[M]^π = D_Z(M)/π. Checked. The guess
  "≥ 0 on S(R)°" is refuted (his own "??"): every genuine character is positive on S(R)° = R_{>0}^r, including λ^-1,
  which is not effective, and (λ-1)^2 >= 0 there is virtual. The polynomial test is right for genuine characters
  (nonnegative coefficients, so no cancellation: χ∘α ∈ Z[t] iff ⟨i_1, m⟩ >= 0 on the support, which is π-stable).
  Finiteness: for M^+ = P(i_1), an effective character m of weight n has 0 <= ⟨σi_1, m⟩ <= n for all σ (because
  σi_1 + σῑ_1 = j), so the effective characters of weight n are finite iff the conjugates of i_1 span M̌ ⊗ Q (true when T
  is generated by the conjugates of i_1, as for the Serre group and its quotients); over R only i_1 and ī_1 remain, and
  for dim T >= 3 the set is infinite. That is his last sentence, in the ink's reading. (CE 14:15.)

**What is wrong.**
- His slips: 14:9 "la classe de i" for j (C4). On 14:13 he uses i for the weight cocharacter (⟨i,ε⟩ = 2), where 14:7 and
  14:9 write j: a notation change to annotate, not a reading to correct.
- 14:11 "G = Sl(2,Q)": SL_2 has no nontrivial character, so it cannot carry ε with ⟨j,ε⟩ = 2; with all four structures the
  natural test is GL_2 (an elliptic curve without CM, ε = det). As a test of the effectivity questions alone SL_2 is
  possible; the page does not say which he meant.
- The Pro transcription of these pages has several misreadings (C1-C3, C5, C6). The Codex web witness K14-01 has the right
  reading at each of them, and is itself wrong at 14:15 ("Cela ne tient pas simplement du calcul arithmétique").

**What is open.**
- The saturation condition (14:9) is never specified.
- The second question of 14:11: are the effectivity structures that come from motives of the form P(i_1)? For motives over
  a subfield of C, M^+ ⊂ P(μ) (μ the Hodge cocharacter) is clear, and **M^+ = P(μ) is the motivic form of the generalized
  Hodge conjecture** (a summand of h^n(X) all of whose Hodge types (p,q) have p, q >= k is N(-k) with N effective):
  Grothendieck, "Hodge's general conjecture is false for trivial reasons", Topology 8 (1969) 299-303 (locator unverified).
  Open (hunch c14a-H1).
- The Frobenius interpretation of 3° and 4° (14:11, last lines) is only announced (hunch c14a-H2).
- The axiom of finitely many types of effective motives of weight i (14:3): for P(i_1) it holds exactly when the conjugates
  of i_1 span (above); for motives in general it is a finiteness statement of its own (hunch c14a-H3).

#### 2. Reused leaves on the backs (14:4, 6, 8, 10, 12, 14, 16): SA06-11

One English typescript, "The Brauer group of a ringed space": locally separable algebras over a ringed space (X, A),
commutants, the Brauer group B(X, A). Its sections run backwards through the scans: II.9 (14:16), III.4 (14:14), III.5
(14:12), III.6 (14:10), III.7 (14:8), IV and IV.1 (14:6), IV.2 (14:4). The title is that of a paper of B. Auslander,
J. Algebra 4 (1966) (locator unverified; the Pro notes, R01, say the identity of these leaves with that paper is not
established). Not studied.

#### 3. A sign test for a family of 1-cycles on a threefold (14:17, 19, 21): SA06-3 (with SA18-14)

**Places.** 14:17 is a title sheet, "Équivalence d'Albanese et de Picard des cycles algébriques" (Codex: "Équivalences").
14:19 and 14:21 are one computation; 14:18 is blank, 14:20 and 14:22 are reused leaves (item 4).

**What he does.** A an elliptic curve, P a smooth projective connected curve, Y = A × P (he writes the dimensions as
superscripts: P^1, Y^2, X^3), Θ_0 = Δ - A×(0) - (0)×A on A × A (the divisor of the autoduality), Θ = Θ_0 × P on
A × A × P = A × Y; c = cl(L) a divisor class on Y; X the projective closure of the line bundle V(L), i: Y -> X the zero
section; z = (id_A × i)_*(Θ), a codimension-2 cycle on A × X, i.e. a family of 1-cycles on the threefold X parametrized by
A, algebraically equivalent to zero. He computes the degree of s_*(z^2) (s: A × X -> A) and finds -2·c(0,0), where
c(0,0) is the degree of c on {0} × P; with c = A × (a) (a ∈ P(k)) this is -2, and with -c it is +2: "des signes
différents !!".

**Checked (independent re-proof).** z^2 = i'_*(Θ · i'^*i'_*Θ) = i'_*(Θ^2 · c'), c' = c_1(N_{i'}) = 1_A × c (the normal
bundle of the zero section is L); s∘i' = t gives s_*(z^2) = t_*(Θ^2 c'); the projection formula gives
deg = deg(p_*(Θ^2) · c); Θ_0^2 = Δ^2 - 2(0,0) - 2(0,0) + 2(0,0) = -2(0,0), with Δ^2 = 2 - 2g = 0 and the two fibre classes
of square 0; so p_*(Θ^2) = -2 ({0} × P) on Y and deg s_*(z^2) = -2 deg(c|_{{0}×P}). Every step is right. Two typing slips
of no consequence (Pro notes A02): p_*(Θ^2) lives on Y, so "0 × 0 × P" should be "0 × P" (or c read as c' on A × Y), and
"c = A × A × (a)" is c' = A × (A × (a)).

**What it shows.** The classes of the family lie in i_*H^1(A) ⊂ H^3(X), and their self-pairing ∫_X i_*α · i_*β =
∫_Y α β c depends on the normal class c, so its sign changes with c. A positivity statement for such pairings of
algebraically trivial cycles cannot hold without the Lefschetz decomposition with respect to an ample class (H^3 of a
threefold is P^3 ⊕ ξH^1, with opposite Hodge-Riemann signs on the two parts). The Pro notes (A01) tie this to the divisor
D = r_*(p^*z·q^*z) of cote 44, scan 9, and its warning about primitive decomposition (not re-read here: sweep-3 SA18).
Nothing open on the page itself.

#### 4. Reused leaves (14:20, 22): SA06-11

A French typescript numbered "n° 391", pages -14- (14:22) and -15- (14:20), joined in the order 22 -> 20: affine
pseudo-reflections and reflections, Proposition 9 (two orthogonal symmetries in parallel hyperplanes compose to the
translation 2t), "5. Chambres dans un espace affine", Lemme 1. A Bourbaki draft on the material of Groupes et algèbres de
Lie, ch. V (locator unverified). Not studied.

#### 5. "Théorie de l'équivalence d'Albanese des cycles" (14:24-37): SA06-3

**Places.** §1 "L'anneau des classes d'équivalence d'Albanese" (14:24-30), §2 "Familles de classes de cycles mod équiv.
d'Alb." (14:31-37). Top margin of 14:24: **"Consulter Weil, Critères d'Équivalence"** (decided on the scan; the Pro text
reads "Conjectures(?) Weil, Critères d'Équivalences": correction C7), i.e. Weil, "Sur les critères d'équivalence en
géométrie algébrique", Math. Ann. 128 (1954) (locator unverified).

**What he does and what is proved.**
- Def. 1.1 (14:24): z on X smooth over k is Albanese-equivalent to 0 if z = Z(ν) for a cycle Z on X × T, T smooth
  [projective] connected, ν a 0-cycle on T of degree 0 with S(ν) = 0 in the Albanese. The ink writes S_Y(ν), also on 14:26
  (S_Y for S_T: a leftover name of the parameter variety; annotate, correction C8).
- Prop. 1.2 (14:24-28): (i) the Albanese-trivial cycles form a graded subgroup N^*(X) containing the cycles linearly
  equivalent to 0; (ii) its image N'^* is an ideal of the Chow ring A^*(X), so A'^*(X) = A^*/N'^* is a ring; (iii) f^*,
  (iv) f_* for f proper; (v) Albanese equivalence implies algebraic equivalence. Proved on the page: (i) (T × T',
  ν × a' + a × ν', with pr_1*(a × ν') = deg(ν')·a = 0) and (v); linear equivalence via T = P^1 (Alb(P^1) = 0). Left: the
  moving of Z, ν in (iii) ("à vérifier", "Nous laissons ici les détails"), (ii) "par la même méthode", (iv) "pr l'AQT(?)".
  Remark: (ii) also follows directly from the definition, z·w = (Z · pr_X^*w)(ν), when the intersections are defined.
- Scholie 1.3: the A'^* have the formal properties of the A^* (projection formula); where linear and algebraic equivalence
  agree (a point, P^n, flag varieties) so does Albanese equivalence. Right (it lies between the two).
- Th. 1.4 (14:29-30), X projective smooth connected: (i) a 0-cycle is Albanese-trivial iff it has degree 0 and
  S_X(ν) = 0; (ii) a divisor is Albanese-trivial iff it is linearly equivalent to 0. (i) "if" by T = X, Z = the diagonal; the
  "only if" cites an empty reference "[ , 1.2.]": it holds because t -> S_X(Z(t) - Z(t_0)) factors through Alb(T) as a
  homomorphism. (ii) via u: A_T -> Pic^0_X with cl Z(ν) = u(S_T(ν)). Checked both. Margin of 14:29: projectivity of T is
  used (the universal property of the Albanese for abelian targets).
- Remark 1.5 (14:29, margin): "On ignore, déjà pr les 0-cycles, si l'équiv. d'Alb. est identique à l'équivalence
  linéaire. (Vrai pr tous les cycles???)". **Answered negatively over C**: for a surface with p_g > 0 the Albanese kernel
  of CH_0 is nonzero, indeed not finite-dimensional (Mumford, "Rational equivalence of 0-cycles on surfaces", J. Math. Kyoto
  Univ. 9 (1969): locator unverified). Over the algebraic closure of a finite field the answer for 0-cycles is yes
  (CH_0^0 of a smooth projective variety over F_q is Alb(F_q), unramified class field theory of Kato and Saito: locator
  unverified); over Q̄ it is the Bloch-Beilinson expectation, open.
- Th. 1.6 (14:30): in A'^*(X) the product of two algebraically trivial classes is 0. Proof on the page: with z = Z(x) -
  Z(y), z' = Z'(x') - Z'(y'), zz' = (Z × Z')(ν) restricted to the diagonal, ν = ((x)-(y)) × ((x')-(y')), and
  S_{T×T'}(ν) = 0 (both projections of ν vanish, Alb(T × T') = Alb T × Alb T'). Checked. Margin: "On ignore si cet ν est
  lin. équiv. à 0, = si T, T' sont des courbes!" Answered: not in general over C; these ν generate the Albanese kernel of
  T × T', nonzero for two curves of genus >= 1 by Mumford's theorem (e.g. E × E). His bracketed strengthening "[l'un alg.
  équiv. à 0, l'autre num. équiv. à 0??]": with "num" replaced by τ it is Cor. 2.4 below; with homological equivalence and a
  product of 0-cycles it holds (the homomorphism Pic^0 -> Alb, D -> alb(D·z'), acts on H_1 through the class of z', which is
  0); with "num" in general it rests on Conjecture D (num = hom), open.
- Th. 2.1 (14:31-34): Z ∈ A^i_alb(X × Y) gives u_Z: A_Y(k) -> A^i_alb(X) with Z(ν) = u_Z(S(ν)); (i) u_Z depends only on Z
  modulo τ-equivalence; (ii) there are an isogeny φ: A' -> A_Y and a homomorphism family Z' on X × A' (Z'((0)) = 0) with
  u_Z∘φ = v_Z'. Proof of (ii): if a cycle U on Y × A_Y with S_Y(U(a)) = a existed, Z'(a) = Z(U(a)) would do; "on ne sait pas
  si on peut trouver U", but one can get S_Y(U(a)) = na; then Z'(S_Y(ν)) = nZ(ν) for ν of degree 0 (his "U(a) = nν" means
  equality modulo Albanese equivalence: Pro A19), and since A_Y(k) is divisible, φ = n. Proof of (i): Th. 1.6 for Z alg. ~ 0;
  for τ, mu = 0 and divisibility. Checked; the existence of U with S_Y(U(a)) = na, which he asserts without proof, holds:
  take a smooth curve C ⊂ Y with J(C) -> A_Y surjective, an abelian subvariety B ⊂ J(C) isogenous to A_Y, ψ with φ_Bψ = n,
  and the Jacobi-inversion correspondence on C × J(C) (independent re-proof). k is algebraically closed throughout
  (divisibility; Pro A05).
- Cor. 2.2 (written "2.7(?)" in the Pro text), 2.3, 2.4 (14:34): a cycle is alg. ~ 0 iff it is Albanese-equivalent to
  Z(a_0) for a homomorphism family Z on A × X (A abelian; the ink writes "diviseur", for a cycle of any codimension: Pro A20);
  P^i(X) (the alg.-trivial part of A^i_alb(X)) is divisible; ZZ' = 0 if one factor is alg. ~ 0 and the other τ-~ 0. All
  follow from 2.1; checked.
- Def. 2.5, Prop. 2.6, 2.7 (14:35): algebraic maps Y(k) -> A^i_alb(X) (factor through A_{0,alb}(Y) ≅ A_Y^*(k), and Nφ is
  induced by a cycle on X × A_Y for some N > 0); 2.6 "C'est 2.1"; 2.7: they form a group, Nφ algebraic implies φ algebraic,
  functoriality in Y and in X (for correspondences). Definitions; nothing to check beyond 2.1.
- 14:36: N.B. the algebraic families Y(k) -> A^i_alb(X) are A^i_alb(X) × Hom alg(A_Y, A^i_alb(X)); A(k) = P^α(A)
  (α = dim A, by Th. 1.4 (i)); algebraic homomorphisms P^j(X') -> P^i(X) (Nφ defined by a cycle); caution that a cycle with
  rational coefficients does not in general define a homomorphism. Right.
- 14:37: (a) "Une question plus subtile est s'ils peuvent s'inverser, quand c'est des isomorphismes". For abelian varieties
  his definition settles it: an isogeny bijective on points (purely inseparable, char p) has inverse (1/p^r)·(dual
  isogeny), so p^r φ^-1 is algebraic and φ^-1 is algebraic in his sense; for general P^i(X) it depends on representability,
  open. (b) Duality between P^i(X) and P^j(X) for i + j = n + 1: for A, B dual abelian varieties, Hom alg(A, P^i(X)) <->
  Hom alg(P^j(X), B), through the transpose ^tZ: P^j(X) -> P^1(A) ≅ B. His caveat: "il faut vérifier que P^j(X) -> B ne
  dépend que de l'application A -> P^i(X), pas du cycle Z". **I prove it** (CE 14:37): if W = Z - Z_1 gives u_W = 0, write
  any w ∈ P^j(X) as Z'(b) for a homomorphism family Z' on X × B' (Cor. 2.2, up to N and divisibility); the composite
  correspondence on B' × A is a divisor class giving a homomorphism B' -> Pic^0(A) whose dual A -> Pic^0(B') is
  a -> ^tZ'(W(a) - W(0)); the latter is Albanese-trivial, hence linearly trivial (Th. 1.4 (ii)), so both homomorphisms
  vanish and ^tW(w) = 0. The dimension count i + j - n = 1 is right. Transposition between P^i(X) -> P^i'(X') and
  P^j'(X') -> P^j(X) "Cf plus bas" is then the same argument.

**What is wrong.** C7 (the margin reference), C8 (S_Y for S_T); "Corollaire 2.7(?)" in the Pro text, where the sequence 2.1,
[2.2], 2.3, 2.4 requires 2.2 (ink not checked); "diviseur" for a cycle of codimension i (his slip).

**What is open.** Remark 1.5 and the margin of 14:30 are answered (above). Open on the pages: whether P^i(X) is
representable (an abelian variety's points), on which the inversion question of 14:37 rests (an algebraic
representative exists for codimension 2 by Murre's work of 1983-85: locator unverified); the moving
lemmas of Prop. 1.2 (iii), (iv), which are standard for smooth quasi-projective X (Fulton, Intersection theory, ch. 10-11:
locator unverified).

#### 6. "3. Homomorphisme ℓ-adique associé à une famille abélienne de cycles" (14:38-39): SA06-3

**What he does.** For Z ∈ A^i_alb(X × A), A an abelian variety: u_Z: A(k) -> A^i_alb(X) and
a(^tZ): H^{2(n-i)+1}(X)(n-i) -> H^1(A) (Z_ℓ coefficients). Claim: rationally the latter depends only on u_Z, precisely
"u_Z = 0 =>(?) a(^tZ) = 0" (his question mark); margin "A-t-on une réciproque". Proof begun: an ample curve C ⊂ A gives Z'
on X × C; H^1(A) -> H^1(C) is injective and C(k) generates A(k), so both conditions transfer to C; the Künneth
decomposition of H^N(X × C) is algebraic (the projectors of a curve: pt × C, C × pt, Δ minus both); the two outer
components give zero on both sides, so one is reduced to a cycle in the middle component. The page stops there.

**Checked.** Degrees: a correspondence of codimension i from X (dim n) to A shifts degree by 2i - 2n, so the source of
H^1(A) is H^{2(n-i)+1}(X)(n-i), as in the first display; the second display's "H^{(n-i)+1}" and the "+3(?)" of the curve
case are slips for 2(n-i)+1 (correction C10, the manuscript). The transfer to C and the Künneth reduction: right.
**The implication u_Z = 0 => a(^tZ) = 0 holds in characteristic 0** (my proof, CE 14:39): over C the homomorphism of
abelian varieties a -> AJ(Z(a) - Z(0)) into the algebraic intermediate Jacobian kills Albanese-trivial classes
(AJ(W(μ)) = AJ_W(S_T(μ)) = 0), so u_Z = 0 makes it zero, and its action on H_1 is the cohomological action of Z (Griffiths:
locator unverified); characteristic 0 reduces to C. In characteristic p the page's route (and mine) needs an ℓ-adic
Abel-Jacobi map; not settled here.

**Open.** The converse (a(^tZ) = 0 => u_Z = 0): over C it is the injectivity, on images of abelian varieties, of
P^i(X) -> J^i_a(X); not settled (hunch c14a-H5). The Pro notes (A29, A34) and Michel Hua's project ("Le Théorème 3.1 de la
page 37 est ce dont aurait besoin la vérification laissée ouverte à la page 36") read this section as the tool for the
transposition check of 14:37; item 5 proves that check without it.

#### 7. "Astuce de Tate sur les cycles décomposables" (14:40-42): SA06-4

**Places.** 14:40 is a title sheet; 14:41-42 the argument; 14:43 see item 10.

**What he does.** A an abelian variety over k algebraically closed, T_ℓ(A) a module over the pro-Lie algebra 𝔤; over
K = Q̄_ℓ assume (a) the Tate conjecture for H^2(A, Q_ℓ(1)) (algebraic classes = 𝔤-invariants) and (b) 𝔤_K acts on T_K(A)
"pseudo-algébriquement" (Frobenius eigenvalues of norm q of the form ε q^{-1/2}, ε a root of unity; margin "Pr. Tits(?), le
premier cas est un cas particulier du second"), or T_K(A) = V_1 ⊕ V_2 with each piece an eigenspace of almost every
Frobenius, with different eigenvalues. These hold for A = C^n, C an elliptic curve over a finite field: (a) "a été vérifié
pr Mumford ... au cas du produit de deux courbes elliptiques", (b) is trivial for C and stable under powers. Then for all i,
D^{2i} (decomposable classes) = H^{2i}(A, Q_ℓ(i))^alg = H^{2i}(A, Q_ℓ(i))^𝔤: the inclusions are a priori, and the
hypothesis gives equality of the ends.

**Checked (independent re-proof).** With H^1 = V_1 ⊕ V_2, Frobenius α on V_1 and β on V_2, αβ = q (for C^n) and α/β not a
root of unity, the invariants of Λ^{2i}(V_1 ⊕ V_2)(i) are exactly Λ^i V_1 ⊗ Λ^i V_2 (α^r β^s = q^i with r + s = 2i forces
r = i), which is spanned by products of invariants of degree 2, (v_1 ∧ w_1) ∧ ... ∧ (v_i ∧ w_i). In the scalar
("pseudo-algebraic") case every class of Λ^{2i}V(i) is invariant, and Λ^{2i}V is again spanned by products from Λ^2 V. So
in both cases the invariants are generated by degree-2 invariants, and (a) gives decomposability. (a) for C^n reduces to
C × C (divisor classes on C^n come from the factors and the pairs), i.e. to End(C) ⊗ Q_ℓ = End_Gal(V_ℓ C) (Deuring; Tate,
Invent. Math. 2 (1966)). The Pro notes (RT5) report that Tate 1966, p. 134, credits Mumford with the elliptic-pair case
(locator unverified by me). Known result: the Tate conjecture for powers of an elliptic curve over a finite field (Tate;
for products of different elliptic curves, Spiess, Math. Ann. 314 (1999): locator unverified).

**Wrong / open.** The exponent -1/2 is a convention (on T_ℓ the Frobenius endomorphism has eigenvalues of absolute value
q^{1/2}; -1/2 fits its inverse): an annotation, not an error. The "Tits" margin is not explained. Nothing open for powers
of one elliptic curve.

#### 8. The letter to Serre of 27 August 1965 (14:44-47): SA06-4

**The document.** Four typed pages numbered 1.-4. (14:44 dated "27.8.65", "Mon Cher Serre"; 14:47 ends "Bien à toi /
A. GROTHENDIECK" and a typed N.B.). **It is published**: Correspondance Grothendieck-Serre, ed. P. Colmez and J.-P. Serre,
Documents Mathématiques 2, SMF 2001; bilingual edition SMF/AMS (2003-2004): "A. Grothendieck, 27 août 1965", pp. 232-234,
headed "Thil, 27.8.1965", with the editor's notes 232.1, 232.2, 233.3, 233.4 on p. 280 (read in the corpus copy
`Documents/Papors/OS/Grothendieck-Serre correspondence ( etc.).djvu`, text layer; table of contents p. vii). Michel Hua's
project says the same ("Le texte intégral de la lettre est publié dans la Correspondance Grothendieck--Serre").

**What he states.** Conjecture A: C^i(X) = cycles of codimension i modulo **algebraic** equivalence, ⊗ Q; for 2i <= n,
ξ^{n-2i}: C^i(X) -> C^{n-i}(X) is an isomorphism; it suffices (unwritten verification) to prove surjectivity for
n = 2i + 1; "le premier cas qui échappe ... est i = 1, n = 3"; A implies the Lefschetz theorems for the C^i and the
cohomological hard Lefschetz, "pas même démontré pour le moment" (only weak Lefschetz is known). A follows from
Conjecture A' (for 2i >= n-1, C^i(Y) -> C^{i+1}(X) surjective, i.e. every cycle of dimension j < n/2 is τ-equivalent to the
image of a rational cycle of Y), with the caveat that the reduction seems to need A' over non-closed fields, "ou se borner à
énoncer A pour l'équivalence cohomologique (mais alors A perd le caractère 'purement géométrique' que je t'avais
promis !)". A implies Künneth for cycles, integrality theorems, the Weil conjectures except the absolute values (from B),
and is the "minimum minimorum" for motives. Conjecture B: for n = 2m, (-1)^m ε(xx') is positive definite on
P^m(X) = Ker(ξ: C^m -> C^{m+1}). Consequences claimed: τ-equivalence = numerical equivalence (= homological, squeezed
between), finite generation, injectivity C^m ⊗ Q_ℓ -> H^{2m}(X)(m), semisimplicity of motives and of the correspondence
algebra, a relative form of A, Galois semisimplicity in the Tate conjectures, intermediate Jacobians. Conjecture A''
(equivalent to A'): C^i(U) = 0 for 2i > n, U = X - Y affine; and "il est possible que ... pour toute variété ... lisse, tout
cycle cohomologiquement équivalent à 0 soit τ-équivalent à 0". Programme: deform a cycle of small dimension "pour le
pousser à l'infini".

**Checked.** The dimension count of A' (codimension i+1, dimension j = n-i-1 < n/2 iff 2i >= n-1; the print's OCR
cannot show the sign; the K14-04 reading ">=" is the one the mathematics requires); weak Lefschetz as stated (restriction
bijective for i <= n-2, injective for n-1; Gysin bijective for i >= n, surjective for n-1, by duality): right.

**What is wrong.** **The conjectures as written, modulo algebraic equivalence, are false** (refuted, with the refined
statement, CE 14:44-47): on a general quintic threefold, C^1 = Q·H while the difference of two lines is homologically
trivial and of infinite order modulo algebraic equivalence (Griffiths, Ann. of Math. 90 (1969); infinitely generated:
Clemens, Publ. IHÉS 58 (1983): locators unverified, the Pro notes RT2 cite Clemens pp. 19-20), so ξ: C^1 -> C^2 is not
onto: A fails at the very case "i = 1, n = 3" he names; A' fails there (with Y a very general hyperplane section,
NS(Y) = Z·H by Moishezon's Noether-Lefschetz theorem: locator unverified), hence A'' too; the claimed consequence "τ-équivalence = équivalence numérique" and the possibility on 14:47
fail by the same example. The refined statements are the cohomological ones he names as the fallback on 14:45, which are
the printed standard conjectures (Grothendieck, "Standard conjectures on algebraic cycles", Bombay Colloquium 1968, Oxford
1969, pp. 193-199; Kleiman, "Algebraic cycles and the Weil conjectures", Dix exposés, 1968: locators unverified; the Pro
notes RT1-RT3 give §§2-3 of the first and §§1.2.1, 1.4.7, 3.6 of the second): A(X, L) and B(X) for algebraic classes in
cohomology, Hdg(X) for all i <= n/2 (the letter's B is the middle case n = 2m), C(X) Künneth, D(X) hom = num (the letter's
"τ = num" with τ replaced by homological equivalence). The cohomological hard Lefschetz he says is unproved was proved by
Deligne (Weil II, Publ. IHÉS 52 (1980), th. 4.1.1: the editor's note 233.3, read in print). **The printed edition's notes
do not mention that the algebraic-equivalence form is refuted** (232.2 only says "Il s'agit des « conjectures standard »");
Michel Hua's project does say it ("Les conjectures de 1965, qui portent sur l'équivalence algébrique, sont donc en défaut
sous cette forme").

**The archive copy against print** (checked on the scans where marked): (i) 14:46 "D'autre part, A et B impliquent
également que la catégorie des motifs ... est semi-simple" (ink, typed) where print has "B implique" (p. 234); the
archive's "A et B" is the mathematically careful one (the involution on correspondences needs the Lefschetz decomposition);
(ii) 14:47: the typed N.B. "H^i(X) désigne la cohomologie à coefficients Q_ℓ, éventuellement tordus par une puissance
tensorielle de T_ℓ(G_m) ⊗_Z Q_ℓ, qui est omise dans les notations pour simplifier" (ink) is absent from print, which ends
with the signature; (iii) by the K14-04 reading, not checked on the image: the print writes the twists (i), (i+r) in the
generalization of A (the archive omits them, as its N.B. announces), "Note"/"Notes aussi", "En tout cas"/"En tous cas",
"correspondances"/"correspondance"; the print's place "Thil" is not on 14:44 (Pro reading "27.8.65").

**Open.** The standard conjectures in their homological form (A for i >= 2 in characteristic p, Hdg, D), open; the
"pousser à l'infini" programme has no written continuation here.

#### 9. "Sorites sur VA, Picard, Albanese" (14:48-58): SA06-3 (sweep 2 placed 50-54, 56, 58 under SA06-4)

**What he does.** 14:48 cover; 14:49-51 Résumé: abelian varieties from cycles algebraically equivalent to 0 (divisors:
B_X = Picard; 0-cycles: A_X = Albanese); a cycle Z on X × Y gives maps A(k) -> B(k) in "4 = 2×2" cases, always a
homomorphism u_Z depending only on the numerical class of Z; with rational cycles every homomorphism arises; ℓ-adically
via H^1(A_T) ≅ H^1(T), H^1(B_T) ≅ H^{2n-1}(T)(n-1); the cohomology map is an isomorphism iff u is an isogeny, so the inverse
on cohomology is then algebraic, e.g. for cup product with ample ζ_1...ζ_{n-1}: H^1(X) -> H^{2n-1}(X)(n-1); 14:51 the four
cases (III: the classical theory of divisorial correspondences; I, II, IV need inverting φ or ψ, "il faut des dénominateurs
?"). §1 (14:52-57): Th. 1.1 (a dimension-m cycle Z on X × Y gives a unique u_Z: A_Y -> A_X with S_X(Z(ϖ)) = u_Z(S_Y(ϖ))),
Cor. 1.2 (S_Y(ϖ) = 0 => S_X(Z(ϖ)) = 0), existence through the Poincaré class on B × X' and Cartier biduality, Cor. 1.3,
Lemmas 1.4, 1.5 (the moving lemma, proof omitted as "théorie d'intersections standart"), Th. 1.6 (ℓ-adic compatibility),
Cor. 1.7 (for abelian varieties: a map H^1(X) -> H^1(Y) is given by an algebraic cycle iff by a homomorphism Y -> X; u is
independent of ℓ), Rem. 1.8 (relative version over S with CK^n cycles); §2 (14:58) Prop. 2.1 (1-cycles give
B_X -> A_Y), cut off at "Cet homomorphisme".

**Checked.** Uniqueness in 1.1 (dense open U, A_Y(k) = sums from 0-cycles supported in U); the construction of u_Z; that it
depends only on the numerical class (the divisor class c on B × Y depends only on the numerical class of Z, and for divisors
numerical = τ-equivalence, while a homomorphism of abelian varieties killed by an integer is 0); the reduction 1.4 -> 1.3
through A_X(k) ≅ Pic^0(B); Cor. 1.7 from 1.6. All classical (Weil's theory of correspondences; Lang, Abelian varieties,
1959: locator unverified). Cup product with ample classes on H^1 is the known degree-1 case of the Lefschetz standard
conjecture (polarization isogeny Pic^0 -> Alb). **Cor. 1.2 is the reference left blank on 14:29** ("résulte de [ , 1.2.]",
Th. 1.4 (i)): an identification first made by Michel Hua's project ("est comblée par le Corollaire 1.2 de la page 51"),
which I confirm: it is exactly the step needed.

**Wrong.** Slips listed by K14-04 (S2: "un diviseur de degré 0" for a 0-cycle on 14:54; S3: Pic^0(A_X) for Pic^0(B) on
14:54; S5: Z_1 and Z on 14:58): I agree with S2 and S3 on the mathematics (not checked on the image).

#### 10. The sheets as documents (SA06-13), and what is actually on each scan

- 14:43 is **not blank**: under local contrast enhancement it shows rows of very faint typed text in the layout of a letter
  page (CE 14:43); Michel Hua's project calls it "un double pâle du premier feuillet" of the letter. I could not read it, so
  the identification is his (credited), not confirmed. The brief's ink-profile test misses it (correction C9).
- What is on the scans, against sweep 2's page lists: effectivity (SA06-2) = 14:2-3, 5, 7, 9, 11, 13, 15; the reused
  Brauer-group typescript = 4, 6, 8, 10, 12, 14, 16; title 17 and the sign test 19, 21 (SA06-3 with SA18-14); Bourbaki
  n° 391 = 20, 22; Albanese equivalence (SA06-3) = 24-39; Tate's trick (SA06-4) = 40-42; letter (SA06-4) = 44-47 (43 its
  pale duplicate, per Hua); Sorites (SA06-3) = 48-58. So: SA06-3's list should drop 2-3, 6, 8-9 and add 17, 48, 50-58;
  SA06-4's list should drop 5-8, 19, 50-54, 56, 58 (they are effectivity, typescript, the sign test and the Sorites);
  SA06-2's list should drop 28, 48-49 (Albanese, Sorites; 44 and 46 touch motives only through the letter's remarks);
  SA06-11's list should drop 3, 5, 21 (his handwritten pages); SA06-1 (linear against nonlinear) is not on these pages at
  all: it is the Pro notes' research lens (B01-B05), not his text.

### Hunches

- **c14a-H1.** His question "sont-elles dans Im I(G) ?" (14:11), for motives over a subfield of C with i_1 the Hodge
  cocharacter μ, is the motivic generalized Hodge conjecture: M^+ = P(μ). Grounds: M^+ ⊂ P(μ) always; equality says a summand
  of h^n(X) with Hodge types p, q >= k is N(-k), N effective (Grothendieck, Topology 8 (1969): locator unverified). Links:
  SA06-2, SA05-18 (cote 15 frame), the coniveau filtration; a characteristic-p analogue is H2.
- **c14a-H2.** The "interprétation des structures 3° et 4° en termes [des éléments de Frobenius]" (14:11) should be:
  4° (effectivity) <-> integrality of Frobenius eigenvalues and the Newton polygon lying above the Hodge polygon (Katz's
  conjecture, Mazur 1972-73: locator unverified); 3° (polarization) <-> the Weil-number conditions |λ|^2 = q^w (cote 15,
  15:100-106, SA06-9). Grounds: his sentence, and cote 15 where the Frobenius becomes an element of the motivic group.
- **c14a-H3.** The axiom "finitely many types of effective motives of weight i" (14:3) holds for P(μ) whenever G is
  generated by the conjugates of μ (the cross-section of the dual cone at weight i is then bounded); for the motivic group
  this is the Mumford-Tate property, so the axiom is a consequence of the Hodge-type conjectures. Grounds: item 1's proof
  for tori and its nonabelian extension (dominant weights in a bounded polytope).
- **c14a-H4.** Item 1's proof shows that the effectivity structure determines the conjugacy class of μ up to Galois
  action, i.e. the pair (G, Galois orbit of {μ}): the data of a Shimura-type datum and its reflex field up to conjugacy.
  Effectivity structures over Q might be the intrinsic form of "reflex fields" for motivic groups. Grounds: the vertex
  argument; Deligne's Shimura data (Corvallis 1979: locator unverified).
- **c14a-H5.** Th. 3.1's converse (14:38) is equivalent over C to: Albanese equivalence and Abel-Jacobi equivalence agree on
  algebraically trivial cycles coming from abelian families. In codimension 2 this should follow from Murre's algebraic
  representative together with a description of Ker(AJ) on CH^2_alg by Albanese kernels of surfaces; I do not know it
  proved. Links: SA06-7 (boundedness), SA18-14 (intermediate Jacobians, cote 44).
- **c14a-H6.** Th. 1.6 (alg-trivial · alg-trivial = 0 modulo Albanese equivalence, 14:30) is the first case of the
  expected multiplicativity of the Bloch-Beilinson filtration (F^1 · F^1 ⊂ F^2), with Albanese equivalence playing F^2 on
  algebraically trivial cycles. Grounds: his proof via ((x)-(y)) × ((x')-(y')), the generators of the Albanese kernel of a
  product of curves.
- **c14a-H7.** The archive copy of the letter (a typed copy with the N.B. and "A et B impliquent") and the printed text
  (from the letter Serre kept, presumably) are two states; the N.B. and the "A et B" may have been added to Grothendieck's
  copy, or dropped in print. Comparing with Serre's original would settle which; the editors' source is not stated in the
  pages I read.

### Dependencies (item ids; the page that shows each)

- SA06-2 (item 1) uses structures 1°-3° on G, which are not on these pages (the cancelled title of 14:2; "3°" on 14:9,
  14:11); its torus claim (14:13) is proved in cote 15 (15:84, SA06-9/SA06-10, STUDY.md §2); its Frobenius remark (14:11)
  points to SA06-9 (15:100-106).
- Item 3 (14:19-21, SA06-3) uses the divisor D = r_*(p^*z·q^*z) of cote 44, scan 9 (SA18-14), per the Pro notes A01.
- Item 5 (14:24-37, SA06-3) uses item 9 (Cor. 1.2 of 14:52 for Th. 1.4, 14:29); it is used by SA06-7 (cote 14,
  117-131, boundedness) and by the letter's "jacobiennes intermédiaires" (14:46, SA06-4).
- Item 6 (14:38-39) uses item 9 (Th. 1.6, 14:56) and item 5 (u_Z, 14:31).
- Item 7 (14:40-42, SA06-4) uses Tate's isogeny theorem and Deuring; its supersingular case is the N.B. of 15:96-98 (SA06-9).
- Item 8 (14:44-47, SA06-4) uses the notions of item 5 (τ-equivalence, C^i mod algebraic equivalence); it is used by
  SA06-6 (cote 14, 101-117, Lefschetz theorems for cycles) and SA06-5 (positivity), and continues the cote-16 drafts
  (scans 45-49, per the Pro notes RT3).

### Deliverable state of scans 2-58

- **Passes.** Scans 2-44: Pro `MPL_14_002-044` (frozen 15 Nov 2026), Codex web K14-01 (2-15), K14-02 (16-30), K14-03
  (31-44) with their math notes, and Michel Hua's reading (witness). Scans 45-58: Codex web K14-04 only (no Pro, no second
  transcription); the letter part is now compared with print (item 8).
- **Readings corrected here** (CORRECTIONS.tsv): C1-C6 on the effectivity pages (the Pro text is wrong at each, Codex right
  at C1-C3, C5, C6's first half), C7-C8 on 14:24, C9 on 14:43, C10 on 14:38. On 14:2-15 Codex is the better witness.
- **Open readings.** 14:3 end of the lower left margin ("supposant G connexe" (Codex) against "stable par l'action de G
  tout entier" (Pro); the ink shows "G co..."); 14:11 the superscript of I (a or α); 14:15 "notion" or "relation"; 14:19 the
  direction of the margin arrow i'; 14:53 margin "une référence"; 14:55 the transpose sign; 14:58 S_{Y(?)}; 14:43 the faint
  impression; the archive/print differences of item 8 (iii).
- **Ready for a transcription edition?** Scans 2-42 and 44: yes, once C1-C10 and the Codex readings named above are
  applied. Scans 45-47 (the letter): yes after a check of K14-04 against the image (print agrees except item 8). Scans 48-58
  (the Sorites): not yet; one witness only, needs a second reading on the image.

### Counts

54 transcribed pages read (scans 2-17, 19-22, 24-42, 44 from the Pro text with the Codex witnesses; 45-58 from K14-04), scan 43 inspected; 36 check events, 17 corrections, 7 hunches (c14a-H1 to H7). Written 19 Nov 2026 by Claude Opus 5.5 at effort max, c14_c15rest_part1.


## SA06, cote 14, scans 59-132: sweep 3 reading (sub-stretch c14_c15rest_part2)

Claude Opus 5.5 at effort max, `c14_c15rest_part2`, sweep 3 reader, launched by `c14_c15rest` (Claude Opus 5.5 at effort
max) at the word of agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max); started 19 Nov 2026. Written as the reading
goes, page by page.

Witnesses. Scans 59-86: Codex web `K14-05` (59-71, 73) and `K14-06` (74-86) are the only text (no Pro transcription).
Scans 87-132: the Pro package `MPL_14_087-132` is the text; Codex web `K14-07`, `K14-08`, `K14-09` are the second witness.
Blank scans, not read (ink measured): 72, 105, 110, 119, 125, 130. Michel Hua's project
(`transcripts/14/14.modern.tex`; his page p = our scan p + 1) is used as a credited witness only.

### Items, in page order

#### 1. SA06-3 (later part): § 2 « Application à l'algébricité de certains homomorphismes de V.A. ou d'espaces de cohomologie l-adiques », 14:59-71 (text: K14-05)

**Places.** The numbered text begins on 14:52 (« 1. Un lemme de théorie des intersections », Th. 1.1 to Rem. 1.8, read by
part 1) and § 2 begins on 14:58 (Prop. 2.1, statement). In my stretch: 14:59 end of 2.1 and its cohomological square;
14:59-61 proof and « Variante »; 14:61 a crossed-out « Corollaire 2.2 »; 14:62 Cor. 2.2 (transposition) and Prop. 2.3
(bracketed, margin « devrait remonter au N°1 »); 14:62-64 Prop. 2.4; 14:64-65 Cor. 2.5; 14:65-68 Cor. 2.6 (margin
« Th ? »); 14:68-70 Prop. 2.7; 14:71 « Questions ». Pencil sheet numbers 58-70 on scans 59-71 (sheet = scan - 1).

**What he does.** X, Y smooth projective connected over k algebraically closed, of dimensions n and m; A = Albanese,
B = Pic^00 (the reduced Picard variety), A_X = B_X^*. A 1-cycle z on X x Y gives u_Z: B_X -> A_Y with
u(cl D) = S_Y(tZ(D)) for D algebraically equivalent to 0 on X with tZ(D) defined; cohomologically u^(1) corresponds to
psi_X a(gamma(z)) phi_Y^(1), with phi_Y: H^1(A_Y) -> H^1(Y) and psi_X: H^(2n-1)(X)(n-1) -> H^1(B_X) (the action of the
Poincaré divisor). Construction (14:60): C = pi_*((1_Y x Theta).(z x 1_B)) in Z^m(Y x B_X), z(Theta(b)) = C(b), and
Th. 1.1 applied to C gives u(b) = S_Y(z(Theta(b))). Variante (14:61): u_Z is the divisorial correspondence
Theta_Y o Z o tTheta_X on B_X x B_Y (the display after it is left as « ... - »). Cor. 2.2 (14:62): t(u_Z) = u_(tZ).
Prop. 2.3 (14:62, bracketed): in the setting of 1.1, t(u_Z): B_X -> B_Y sends cl(D) to cl(tZ(D)); N.B. this should give
another proof of 1.1 through a morphism Pic_(X/k) -> Pic_(Y/k). Prop. 2.4 (14:62-64): a(gamma(z)): H^1(Y,Q_l) ->
H^(2n-1)(X,Q_l)(n-1) is an isomorphism iff u_Z is an isogeny; its inverse is then a(t gamma(D)) for a unique D in
Cl(X,Y) (x) Q, which defines u_Z^(-1); D can be integral iff u is an isomorphism; if Ker u (as a group scheme) has order N,
D = N^(-r) D_0 with D_0 integral, but not M^(-r) D_0 when M misses a prime divisor of N. Cor. 2.5 (14:64-65): the integral
version: u is an isogeny of degree prime to l iff H^1(Y,Z_l) -> H^(2n-1)(X,Z_l)(n-1)/torsion is bijective, and
H^(2n-1)(X,Z_l) is moreover torsion-free iff the map itself is bijective. Cor. 2.6 (14:65-68): for ample classes
zeta_1, ..., zeta_(n-1), cup product with eta = zeta_1...zeta_(n-1): H^1(X,Q_l) -> H^(2n-1)(X,Q_l)(n-1) is an isomorphism,
and its inverse is given by a unique element of Cl(X,X) (x) Q, independent of l. The proof goes through a curve
v: C -> X: u = v_* o (duality) o v^*, and (i) polarization <=> (ii) isogeny <=> (iii) v^* has finite kernel <=> (iv)
v_*: A_C -> A_X is surjective, the last « bien connu » for a general complete-intersection curve. Prop. 2.7 (14:68-70),
the other direction: D in A^1(X x Y) with u_D: A_Y -> B_X an isogeny gives a Q-1-cycle Z inverting a(gamma(D)), with
u_Z = u_D^(-1); proof by the squares of 14:69-70 (mu = psi_X lambda phi_X, psi_X^(-1) = lambda phi_X mu^(-1),
phi_X^(-1) = mu^(-1) psi_X lambda, mu being H^1 of the isogeny of 2.6). Questions (14:71): 1) is there always an INTEGRAL
cycle inverting H^1(A_X) -> H^1(X)? It would suffice that, for N large, the generic fibre of Sym^N(X) -> A_X have a
rational point; 2) is there always an integral cycle inverting H^(2n-1)(X)(n-1) -> H^1(B_X)? If 1) is yes, it suffices to
answer 2) for abelian varieties.

**What is proved.** 2.1 (given 1.1, 1.6, 1.7), 2.2 (« par voie cohomologique », not written out), 2.4, 2.5, 2.6 and 2.7 are
proved on the pages, up to standard facts he cites (« bien connu »: surjectivity of A_C -> A_X; intersection theory).
2.3 is only stated (« Vérification de 2.3. par AQT », the abbreviation unresolved). The crossed-out Cor. 2.2 of 14:61
(« Tout homomorphisme B_X -> A_Y est défini par un Z_1 in Cyc_1(X x Y) ») is not claimed: over Q it follows from 2.6-2.7
together with divisorial correspondences; integrally it is the kind of statement the Questions of 14:71 leave open.

**What I checked** (check events in the TSV). The construction and dimension count of 14:60; the numerical invariance of
14:61 (projection formula, then 1.1, whose own numerical invariance rests on divisors: numerical implies algebraic up to
torsion, Matsusaka, and Hom is torsion-free); Cor. 2.2 on an example (X = Y = E elliptic, Z the graph of alpha:
u_Z = alpha o lambda^(-1), t(u_Z) = alpha^dagger o lambda^(-1) = u_(tZ), since S(alpha^*([P]-[0])) = alpha^dagger(P);
no sign in Mumford's normalization); Prop. 2.4 including the denominators (an isogeny u of degree N has v with
v o u = [N]; M^r u^(-1) is a homomorphism iff Ker u is killed by M^r); Cor. 2.5 with Z_l coefficients using the sheet 14:73
(phi_Y is an isomorphism over Z_l, psi_X is onto with kernel (NS(X){l})^dual); Cor. 2.6 by an independent argument
(u = g^dual o delta o g with g = v^*, delta the Abel-Jacobi isomorphism of the curve, which is minus a principal
polarization, so u = -phi_(g^*M) is an isogeny iff g has finite kernel); the inverse formulas of 2.7; the sufficiency in
Question 1 and the reduction in Question 2.

**What is wrong.**
- 14:59, proof of 2.1: « psi_X a(gamma(z)) phi_X^(1) » (the ink has phi_X) must be phi_Y^(1): the composite starts at
  H^1(A_Y), as the square on the same page shows (author's slip; Codex S1).
- 14:63, end of 2.4: « diviseurs premiers de n » (a small n in the ink): read N = card Ker u.
- 14:64, insertion « le meilleur dénominateur possible étant donné par card Ker u »: the least denominator is the exponent
  of the group scheme Ker u (u = [2] on a g-dimensional abelian variety, char != 2: order 2^(2g), denominator 2).
  card Ker u is a possible denominator with the same prime factors, so his final clause (« ne peut être meilleur qu'une
  puissance de N », the primes of N) stands. Michel Hua's project notes the same (« le meilleur est l'exposant »).
- 14:67, (i) « L'hom B_X -> A_X = B_X^* est un hom de polarisation »: true up to a universal sign. With the identification
  Pic^0(C) -> Alb(C) of 2.1 (cl D -> S_C(D)), u_Delta for a curve is minus the principal polarization in Mumford's
  normalization (on an elliptic curve, x -> O(x - 0) is -phi_(O(0))). The equivalences (i)-(iv) hold with « u or -u is a
  polarization »; his own margin « Attention aux signes éventuels ! » (14:62) covers it.
- 14:65, Cor. 2.5: « il suffit » can be « il faut et il suffit » (given the first condition); not an error.

**What is open.** The two Questions of 14:71 (hunches c14b-H1, c14b-H2); « AQT » on 14:62.

**Readings decided on the scan** (Codex web K14-05 is the only text). 14:59: phi_X^(1) in the ink (above). 14:62:
« Corollaire 2.? » is 2.2 (renumbered after the crossed-out 2.2 of 14:61); « par AQT »: three capitals, the first retraced,
expansion unknown. 14:63: « de n ». 14:64: the boxed insertion « étant donné par card Ker u ». 14:65 margin: « Th ? C'est
un cas particulier important du "Lefschetz vach..." donnant Lefschetz des surfaces... »; the adjective's ending is not
resolved (Codex « vache(?) », Michel Hua's project « vachement »); the sense is hard Lefschetz, and for n = 2 Cor. 2.6 is
the whole hard Lefschetz theorem of a surface (the only non-trivial degree is H^1 -> H^3). 14:71: « pour n [grand, struck]
convenable (donc n grand) ».

#### 2. The sheet 14:73 (with the blank verso 14:72): Kummer, Néron-Severi torsion and H^(2n-1) (SA06-3, preliminaries)

**What he does.** X proper over k separably closed, N and l prime to the characteristic: H^1(X, mu_N) = Pic(X)[N],
0 -> Pic^0(X)[N] -> H^1(X, mu_N) -> NS(X)[N] -> 0, H^1(X, Z_l(1)) = T_l(Pic^0) (using that Pic^tau/Pic^0 is finite);
for X normal, B_X = Pic^00, A_X = B_X^*, phi_X^*: H^1(A_X, Z_l) -> H^1(X, Z_l). For X smooth of pure dimension n,
Poincaré duality gives 0 -> (NS(X)[N])^dual -> H^(2n-1)(X, Z/N) -> A_X[N](-n) = H^1(B_X, Z/N)(1-n) -> 0 and, in the
limit, 0 -> (NS(X){l})^dual -> H^(2n-1)(X, Z_l)(n-1) -> H^1(B_X, Z_l) -> 0, the last arrow a « hom algébrique » (psi_X).

**Checked.** All of it, including the twists (computation in the TSV): dualizing the Kummer sequence gives
H^(2n-1)(X, Z/N) = H^1(X, mu_N)^dual(1-n), and (B_X[N])^dual = A_X[N](-1) by the Weil pairing. phi_X^* is an isomorphism
over Z_l, not only « mod torsion » as 14:56 and 14:59 say (A_X^dual = Pic^0_red). The limit sequence as written is right.

**Wrong (minor).** At finite level the Néron-Severi term needs the twist (1-n): (NS(X)[N])^dual(1-n). He struck a « (-n) »
there and left the term untwisted; over a separably closed field the twist is invisible.

**Role.** This sheet supplies the « isom mod torsion » and the exact torsion of H^(2n-1)(X, Z_l) used in 2.1 and 2.4-2.5.
Michel Hua's project reads it with the next sheet (our 14:74) as « Deux feuillets : Picard, Albanese et cohomologie
entière ».

#### 3. SA06-3: « Relations entre Alb^0_X, Pic^00_X et H^1(X), H^(2n-1)(X) », 14:74 (text: K14-06)

**What he does.** X smooth projective connected of dimension n over k algebraically closed. Four comparisons, each
« à torsion près »: pi_1^l(Alb) <- pi_1(X)^ab(l) <- H^(2n-1)(X)(n) [« c'est tjrs surjectif ? »];
pi_1(Pic^00) = H^1(Alb)(1) -> H^1(X)(1) [« c'est tjrs injectif »]; H^1(Alb) -> H^1(X) [« tjrs injectif »];
H^1(Pic^00) = pi_1(Alb)(-1) <- H^(2n-1)(X)(n-1). Summary: representing abelian varieties by their H^1, Alb_X corresponds to
H^1(X) and Pic_X to H^(2n-1)(X)(n-1).

**Checked** (TSV). H^(2n-1)(X, Z_l)(n) = pi_1(X)^ab (x) Z_l exactly (Poincaré duality against H^1(X, Q_l/Z_l)), and
pi_1(X)^ab (x) Z_l -> T_l(Alb_X) is onto with finite kernel. The question « c'est tjrs surjectif ? » has the answer yes: a
connected étale isogeny of Alb_X pulls back to a connected cover of X, otherwise the Albanese map would lift through it
(Michel Hua's project gives the same answer). H^1(Alb) -> H^1(X) is even an isomorphism over Z_l; T_l(Pic^00) =
H^1(Alb)(1) and H^1(Pic^00) = T_l(Alb)(-1) are the Weil pairing. Nothing wrong on the page.

#### 4. SA06-3: an axiomatics of abelian varieties up to isogeny, 14:76, 78, 80-81, 83, 85 (text: K14-06)

**Places.** Handwritten on the backs of reused typescripts (14:75, 77, 79, 82, 84, 86, below), in scan order 76, 78, 80, 81,
83, 85; parts « I ① ② ③ » (76), « ① ② » (78), « 3) » (80). It continues on 14:87 and 14:89 (item 6).

**What he does.** 14:76: VA, the additive category of abelian varieties over k algebraically closed; the duality functor
A -> A^*; the contravariant functor A -> C^*(A) to graded commutative rings (cycles modulo algebraic equivalence),
C^0 = Z; dimension, additive and invariant under duality; C^n(A) = Z, « isom can, mais pas fonctoriel sauf pour isom. »;
the covariant law and the projection formula (containing the transposition formula), from which the Pontryagin product
follows formally; « Application fondamentale »: C^1(A) -> Hom(A, A^*)^alt, through C^1(A x A); N.B. « On pourrait définir
axiomatiqmt A^* par cette formule »: C^1(A x B)/(C^1(A) x C^1(B)) = Hom(A, B^*). 14:78: the faithful additive functors
A -> T_l(A) (x) Q_l and A -> H^1(A, Q_l) = Hom(T(A), Q_l); H^*(A) = Lambda^* H^1(A); the square H^1(A^*) =
Hom(H^1(A), Q_l(-1)) (« carré comm. à isom près »); the cycle class gamma_A^(2i): C^i(A) -> H^(2i)(A)(i) =
Lambda^(2i) H^1 (i), compatible with products; the top-degree identifications eta_A: Lambda^(2n) H^1(A) = Q_l(-n) and its
dual for A^*, with « vérifier s'il n'y a pas un signe ! ». 14:80-85: for u between abelian varieties, the Gysin map
u_*: H^i(A) -> H^(i+2(n'-n))(A')(n'-n) defined by transposition; u_*(1_A) is the class of the image cycle, d times the
class of the image B (d = degree of A -> B), zero if u(A) has dimension < n; in terms of u_1 = T(u): T(A) -> T(A'), it is
the decomposable multivector obtained from Lambda^(2n) u_1, normalized by the determinant isomorphism
Lambda^(2n') H^1(A') = Lambda^(2n) H^1(A) (x) Lambda^(2(n'-n)) K (K = Ker(H^1(A') -> H^1(A))); with
H^i(A) = Lambda^(2n-i) T(A)(-n) (Poincaré duality), u_* is Lambda^(2n-i) u_1 (x) Q_l(-n); hence u_*(1) determines the image
of u_1 when u_1 is injective.

**What is proved.** Nothing is claimed beyond classical facts (Weil; NS(A x B) = NS(A) + NS(B) + Hom(A, B^dual);
NS(A) = symmetric homomorphisms A -> A^dual, whose Weil forms are alternating, hence « alt »; H^* = Lambda^* H^1). The
computation of u_* from T_l(u) on 14:83-85 is correct, except for one normalization (below).

**Checked** (TSV). 14:76 statements against the classical theory; the square of 14:78; on 14:80-85 the Gysin
identification u_* = Lambda^(2n-i) u_1 (x) Q_l(-n) on A x 0 in A x E and on [m] of an elliptic curve; the normalization of
14:83 (refuted, below).

**What is wrong.**
- 14:80, « 3) Soit u: A' -> A ... définissant u_*: H^*(A) -> H^*(A') par transposition ... u_*(1_A) = d.1_A' »: with
  u: A' -> A the transpose of u^(2n) goes from H^*(A') to H^*(A) (u_*(1_A') = d.1_A). The rest of 14:80-85 uses
  u: A -> A' (u^1: H^1(A') -> H^1(A), u_1: T(A) -> T(A')): read u: A -> A' from the start (u^(2n): H^(2n)(A') -> H^(2n)(A),
  zero iff u(A) != A').
- 14:81, « la classe du cycle image u(A) in C^(n'-n)(A) »: in C^(n'-n)(A').
- 14:83, « la classe caractéristique de H^(2n)(A)(n) fois la classe cherchée u_*(1_A) ... corresponde d fois [underlined]
  la classe caractéristique de H^(2n')(A')(n') »: refuted; the factor is 1. In the same-dimension case the determinant
  isomorphism is Lambda^(2n) u^*, which sends the point class of A' to d times the point class of A (14:80 itself), so
  [pt_A] (x) u_*(1_A) = [pt_A] (x) d corresponds to [pt_A'], not to d [pt_A']; in general [pt_A] (x) d gamma(B) corresponds
  to [pt_A'] (projection formula). With « d fois » one would get u_*(1_A) = d^2 gamma(B), against 14:81 and against
  Lambda^(2n) u_1 on 14:85.
- 14:83, « N.B. d est aussi le contenu de T_Z_l(A) dans T_Z_l(A') »: only the l-primary part of d is the index of T_l(A)
  in its saturation; the prime-to-l part (and the inseparable part in characteristic p) is invisible to T_l.
- 14:83, last line « s'identifie : Lambda^(2n-1) u_1 (x) Q_l(-n) » (Codex reading): Lambda^(2n-i), as the square above it
  says.
- 14:85, « la connaissance de u_*(1) détermine l'image de u_1: T_l(A) -> T_l(A') »: true for the Q_l-image; over Z_l the
  class determines only the saturated image and the index d_l, not the image lattice.

**Open.** The sign of 14:78 (identification of the two top-degree classes through H^1(A^*) = H^1(A)^dual(-1)); it
depends on the sign convention of the Weil pairing and is not settled on the page.

#### 5. Reused typescripts in 14:75-86 (SA06-11; not in sweep 2's page list for SA06-11)

- 14:75: English typescript, page « 7 »: cogroup structures on A = K[t] (counit, associativity (3.1)), showing
  m(t) = t (x) 1 + 1 (x) t + alpha t (x) t; a page of a paper on group objects/Hopf algebras, author not identified.
- 14:77 (« - 20 - »), 14:86 (« - 21 - »), 14:84 (« - 22 - »), 14:82 (« - 23 - »), 14:79 (« - 25 - »): French typescript
  on the cohomology of sites (Čech cohomology through covering sieves, forgetting the module structure, Prop. 3.1 and
  Def. 3.2 « C-acyclique », Prop. 3.3, Def. 3.5, « N° 3. Critères d'acyclicité »), citing (2.4.14.II) and (3.5.4.III):
  in content the material of SGA 4 Exposé V (Verdier) in an early numbering (identification by content; locator
  unverified). Not studied.

#### 6. SA06-3: homomorphisms of abelian varieties and Néron-Severi groups, 14:87, 89 (text: MPL_14_087-132; second witness K14-07)

**What he does.** 14:87 « Relations entre hom. de V.A. et groupes de N.S. »: C^1(A) -> H^2(A)(1) = Lambda^2 H^1(A)(1) ->
Hom(H^1(A^*), H^1(A)) (« déduit de l'accouplement H^1(A) x H^1(A^*) -> Q_l(+1?) »), Hom(A, A^*) -> C^n(A x A^*) by the
« application "graphe" (pas additive!) », u-bar = (id, u): A -> A x A^*, its action on H^1(A x A^*) = H^1(A) + H^1(A^*)
by (id, u^1). 14:89: a homomorphism u: A -> B is known from the cohomology class of its graph, because that class
determines T_Q_l(Gamma) in T_Q_l(A x B) (14:85); likewise an abelian subvariety is known from its class;
C^1(A x B)/(C^1(A) x C^1(B)) = Hom(A, B^*) read in cohomology as Lambda^2(H^1(A) + H^1(B))(1) modulo the two factors =
H^1(A) (x) H^1(B)(1) = Hom(T_l(A), T_l(B^*)); then « Question Prouver que pour qu'une classe de H^1(A) (x) H^1(B)(1)
soit algébrique ... », cut off at the foot of the page.

**Checked.** The decomposition Lambda^2(V + W) = Lambda^2 V + V (x) W + Lambda^2 W and V (x) W(1) = Hom(T(A), T(B^*));
the determination of u by its graph class (a non-zero decomposable class determines its subspace; an abelian subvariety
is determined by its V_l). **Wrong:** the pairing H^1(A) x H^1(A^*) takes values in Q_l(-1), not Q_l(+1) (14:78 itself
writes H^1(A^*) = Hom(H^1(A), Q_l(-1)); the Pro reading carries a « (?) »; Michel Hua's project makes the same remark).
**Open:** the unfinished Question; over a finite field its natural completion (the Galois-invariant classes are
algebraic) is Tate's theorem for divisors on A x B (Tate 1966), over number fields Faltings (1983) (locators
unverified), see SA06-4.

#### 7. SA06-3 / SA06-1: « Anneaux de classes de cycles sur une variété projective non singulière sur un corps k alg. clos », 14:91 (title sheet) and 14:92

**What is on the page** (decided on the scan image). A box « théorie discrète » with A_num, A_tau, A_alg and the two
homological rings A_(Q_l-hom), A_(Z_l-hom) (a first placement of the latter two is hatched out, with a balloon « car. 0 /
en remplaçant théorie sing. entière »); arrows A_tau -> A_num and A_tau -> A_(Q_l-hom) marked « ? ≃ », A_alg ->
A_(Z_l-hom) marked « ? ≃ » with a small circled mark (Pro « t0(?) »); braces « groupe libre de type fini ? » (A_num,
A_tau), « Groupe fini ? » (kernel of A_alg -> A_tau), « V.A. ? » (kernel of A_pic -> A_alg); a box « théorie continue »
with A_lin -> A_alb -> A_pic, each marked « ≃ ? », and « flèches toutes surjectives »; on the left G_alg K -> G_top K and
CK, « flèches qui sont des isom mod torsion »; margin « Autres équivalences : l'équivalence ... r et l'équivalence de Weil
wh(?) et W définis par Liebermann ..... ».

**Status of his questions** (known results, cited; the same assessment is in Michel Hua's project, credited): A_num is
free of finite type (yes); A_tau -> A_num and A_tau -> A_hom are not isomorphisms in general (Griffiths 1969); A_tau is
not of finite type, even (x) Q (Clemens 1983); A_lin -> A_alb is not an isomorphism for 0-cycles on surfaces with p_g > 0
(Mumford 1969); the kernel of A_pic -> A_alg is an abelian variety for divisors and 0-cycles, and in codimension 2 there
is Murre's algebraic representative (1985) (all locators unverified). The finiteness of the torsion of A_alg (« Groupe
fini ? ») is classical for divisors; in codimension >= 2 I know of results producing infinite torsion phenomena (Schoen;
Totaro 2016) but have not checked which statement they prove (locator unverified). The page asks; it proves nothing.

#### 8. SA06-5: « Mumford-Nakai / Cycles algébriques amples », 14:93 (title sheet), 14:94-96, 98, 100

**What he does.** 14:94: « Th de Mumford-Nakai », X projective over a field, L invertible: a) ample <=> b) chi(F (x) L^n)
-> +infinity for every coherent F with dim supp >= 1 <=> b') the same for O_Z, Z integral of dim >= 1 <=> b'') for Z
integral of dimension 1 (resp. >= 2) some n_Z > 0 with chi(L^n (x) O_Z) >= 2 (resp. >= 1) <=> c), c'), c'') the same with
dim H^0; margins « Critère numérique (X irréd. de dim d): D.C > 0 si C courbe irréd., D^d > 0 (intersections calculées
dans CK(X)!) » and « N.B. le critère implique la condition d'amplitude de A. Weil ». 14:95: a) => b), c) « bien connu »;
the rest by induction on d through Lemma 1 (if L is ample on all integral subschemes of dimension < d, H^i(X, L^n) = 0
for i >= 2 and n >= n_0) and Lemma 2 (if moreover some L^n has a section, X -> P H^0(X, L^n) is everywhere defined and
non-constant for n >= n_0), both « cf lettre de Mumford »; Questions: can one drop the existence of a section in d), d')
(struck on 14:94)? can one drop projectivity? 14:96: for a surface, the cones P^+ (effective), Q^+ (x^2 >= 0, x.a >= 0),
R (ample) in NS: int Q^+ in P^+, hence by polarity (Q^+ self-dual) P^(+0) in Q^+; boxed: x in R <=> x.P > 0 and x^2 > 0
(Nakai); R = int(P^0), R-bar = P^0 (inside Q); Question « xP > 0 => x in R ? », reduced to a class with D^2 = 0, where
chi(nD) = chi(O) + n chi(D) and Mumford's h^0 >= chi force the linear coefficient to be negative. 14:98, 14:100: nef cones
P_i^(+0) in A^i and effective cones P_i^+ in A_i, alpha_i: A^i -> A_(d-i); Questions alpha_(d-1)(P_(d-1)^(+0)) in P_1^+ ?,
P_i^(+0).P_(d-i)^(+0) >= 0 ?, P_i^(+0) P_j^(+0) in P_(i+j)^(+0) ?; « D.C >= 0 => D^i X_i >= 0 ?? », settled for D^3 by
expanding (D' + nD)^3 with D' ample.

**Checked.** For curves over an algebraically closed field b'') and c'') say exactly deg(L|Z) > 0 (chi(O_Z) <= 1 and a
bundle of degree <= 0 on an integral curve has h^0 <= 1). The cone relations of 14:96 (Riemann-Roch for int Q^+ in P^+;
Hodge index for self-duality of Q^+; Nakai for R = int P^0): this is Kleiman's criterion for surfaces, derived from Nakai.
The cubic expansion of 14:100: D nef gives D' + nD ample for D' ample, so n^3 D^3 + O(n^2) > 0 and D^3 >= 0. The Pro
note P05's threefold (re-derived): on V = P_S(O + H) over Mumford's surface S with L strictly nef and L^2 = 0,
D = xi + pi^*L has D.C > 0 for every curve and D^3 = H^2 + 3 H.L > 0, but D^2.S_0 = L^2 = 0 on the section S_0.

**What is wrong.**
- 14:94 margin « Critère numérique: D.C > 0 ..., D^d > 0 »: for d >= 3 positivity on curves and on X does not give
  ampleness (the threefold above; Ramanujam's example, Hartshorne, Ample subvarieties 1970, I.10.8, locator unverified);
  Nakai's criterion needs (D|V)^(dim V) > 0 for every integral V. For d = 2 the margin is the criterion.
- 14:94 b''), c'') with the thresholds « >= 2 »: over a non-closed field false as stated (Pro note P02: P^1_C as an
  R-scheme, L = O); over an algebraically closed field the curve case is fine.
- 14:95, b'') => c''): b'') gives chi >= 1 at a single n_Z, while Lemma 1 controls H^i only for n >= n_0; the step needs
  chi(L^n (x) O_Z) >= 1 for some n >= n_0. Lemma 1 itself is attributed to Mumford's letter and not proved; what I can
  prove (the standard restriction argument) is that h^i(L^n) is eventually constant for i >= 2, which suffices for the
  chi -> infinity route of Nakai's proof but not for the lemma as stated.
**Open on the pages, settled since.** « xP > 0 => x in R ? »: no (Mumford's ruled surface: L.C > 0 for all curves,
L^2 = 0; Hartshorne 1970 I.10.6, locator unverified); his reduction (D^2 = 0 forces a non-positive linear coefficient,
i.e. D.K >= 0) is exactly the shape of Mumford's example (D.K = 2g - 2 > 0). « P_i^(+0).P_(d-i)^(+0) >= 0 ? » and the
product closure: no in general (Debarre-Ein-Lazarsfeld-Voisin 2011: nef classes of codimension 2 <= i <= n-2 on E^n, E with
complex multiplication, n >= 4, need not be pseudo-effective; Pro note P08). alpha_(d-1)(P_(d-1)^(+0)) in P_1^+-bar: yes,
as the dual of the pseudo-effective divisor cone is the closed movable cone of curves (Boucksom-Demailly-Paun-Peternell,
in characteristic 0; locator unverified). Pro note P06 records the parallel questions in his letter to Mumford of 31
August 1964, § 5, with Mumford's « NO ».

#### 9. SA06-6: Lefschetz conjectures for algebraic cycles, global and local, 14:102-103, 106-109, 111-117 (and the cancelled remark 14:114)

**Places.** 14:102 title sheet « conjectures de Lefschetz pour cycles Algébriques: Extension aux Jac. inter., Conjectures
locales »; 14:103 a surface and its hyperplane section; 14:106-109 « Conjectures "Lefschetz" locales »; 14:111-113
« Conjectures "Lefschetz" » (global), 14:115-116 the checks for n = 2, 3, 4, 14:117 « Notations ». 14:114 is his own
cancelled remark (sweep 2 filed it among reused leaves).

**What he does.** Notation (14:111, 117): A^i_r = Chow groups, A^i_a = cycles modulo algebraic equivalence, A^i_tau modulo
tau-equivalence; J = A_r^a (algebraically trivial part), N = A_a, 0 -> J -> A -> N -> 0, M and I the primitive parts of
N and J; « Il ne semble pas qu'il y ait une définition raisonnable de la "partie primitive" de A^*(X) ». 14:103 (X a
surface, Y a smooth hyperplane section): NS(X) -> NS(Y) = Z onto mod finite, kernel of rank rho - 1; J^1(X) -> J^1(Y)
injective « exc. p »; the kernel K of Pic X -> Pic Y meets J^1(X) in a finite group, so is of finite type; K maps into
M^1(X) -> J^1(Y)/Im J^1(X) (« partie mobile »), and « en général » this is injective mod finite, so K is finite: « Je
présume qu'il en est ainsi si les positions limites de Y dans les pinceaux plans contenant Y sont des courbes
irréductibles ». Global (14:111-112), X^n smooth projective, Y a smooth hyperplane section: ① restriction
A_r^i(X) -> A_r^i(Y) bijective for 2i <= n-2, injective for 2i = n-1 (with A^tau, A_a, A_tau consequences), injective on
A^tau for 2i = n; ② Gysin A_i(Y) -> A_i(X) bijective for 2i <= n-3, surjective for 2i = n-2 (bijective on A_a), surjective
on A_tau for 2i = n-1; ③ hard Lefschetz: E^(n-2i): A_a^i -> A_a^(n-i) and E^(n-2i+1): A_r^i(X)^tau -> A_r^(n-i+1)(X)^tau
bijective mod finite groups, hence E^p: A_r^i -> A_r^(i+p) injective mod finite for p <= n-2i, surjective mod finite for
p >= n-2i+1; ②' for the affine U = X - Y, A_i(U) = 0 (2i <= n-2), A_i^a(U) = 0 (2i = n-1); ③' for the punctured affine cone
E over X, finiteness of A_r^i(E) for 2i >= n+2 and of A_a^i(E) for 2i >= n+1, with « On doit avoir » A_a^i(E) = M_a^i(X),
A_r^i(E)^a = I^i(X) mod finite in the complementary ranges. All marked « exc. p » with question marks. Local (14:106-109),
A strictly local noetherian, X = Spec A minus the closed point, Y = X ∩ V(f), both regular, U = X - Y, N the dimension:
vanishing mod finite of N^i, J^i, A^i in high degrees; restriction J^i, N^i, A^i(X) -> (Y) bijective / injective / zero in
ranges; A^i(X) -> A^i(U) iso mod finite; Problems: define intersection forms N^i(X) x N^i(X) -> Z, a theory of vanishing
cycles, a natural complement of J^1(X) in J^1(Y) with J^1(X) = J^1(Y)^pi; « Interpréter le th. de l'index de Hodge pour
les surfaces projectives en termes de la négativité d'une certaine forme définie sur N^1(X) »; N = 2: « N^1(X) fini :
c'est le th. de Mumford-Hodge ». The checks of 14:115-116 mark many rows « OK » and several « OK si équiv. rat. = équiv.
d'Albanese », others « ? », « question "intime" », « question "numérique" ». 14:114 (cancelled): for A complete local with
equidimensional components and U = S_f, « cd U <= dim A », with a reduction to a finite extension of k[[t_1..t_n]].

**Checked** (TSV). The surface case of 14:103 (kernel rank rho - 1; injectivity of Pic^0 up to p-torsion by Lefschetz for
H^1(-, mu_l)); his presumption tested on X = P^1 x P^1, Y a conic: there K = Z.O(1,-1) is infinite, but every pencil of
conics contains line pairs, so his irreducibility condition excludes this case, consistently. The divisor cases of ① are
the Grothendieck-Lefschetz theorems (SGA 2 XII; Pic(X) -> Pic(Y) injective for n >= 3, bijective for n >= 4) and the n = 3
rows of 14:115 marked OK are right (Pic^tau via H^1 and the torsion of H^2). The punctured cone: CH^i(E) =
coker(h: CH^(i-1)(X) -> CH^i(X)) (G_m-bundle). The generic logical test of 14:108 (N = 4, ②): J^1 bijective and N^1
injective give A^1 injective, not bijective (Pro note L07).

**What is wrong** (beyond the open conjectures).
- 14:112, ③ for A_a: « E^(n-2i): A_a^i -> A_a^(n-i) bijectif mod groupes finis » fails in characteristic 0: on a general
  quintic threefold (n = 3, i = 1) E.NS(X) has rank 1 while A_a^2 contains the Griffiths group, non-torsion (Griffiths
  1969) and of infinite rank (Clemens 1983). ③ for A_r (b), surjectivity of E: CH^1 -> CH^2 on a surface): fails on a K3
  (Pro note L11; Beauville-Voisin 2004). His own 14:115 leaves the n = 3 row « A_a^1 -E-> A_a^2 » without « OK ».
- 14:113, ③': the cone has dimension n+1, not « 2n+1 » (Pro and Codex both read 2n+1); A_r^2(E) is not finite for n = 2
  when p_g(X) > 0: for a smooth quartic K3 surface X, CH^2(E) = CH_0(X)/h.Pic(X) contains the degree-zero part of
  CH_0(X) (h.Pic(X) lies in Z.c_X by Beauville-Voisin), which is uncountable (Mumford).
- 14:113: « A_r^i(U) = A_r^i(X)/Im A_r^i(Y) » must have Im A_r^(i-1)(Y) (Gysin from a divisor; Pro note L12).
- 14:113: M_a^i = Ker(L^(n-2i): A_a^i -> A_a^(n-i)) and I^i = Ker(L^(n-2i+1): J^i -> J^(n-i+1)) are the kernels of the very
  maps ③ declares bijective mod finite, so they would be finite; the primitive parts are Ker L^(n-2i+1) on A_a^i (as for
  H^(2i)) and Ker L^(n-2i+2) on J^i (as for H^(2i-1)) (both witnesses agree on the exponents; Pro note L13 for M).
- 14:115, n = 2, ③ for the J-part: written « A_r^0(X)^tau -> A^2(X) » and « A_r^1(X)^tau -id-> A_r^1(X)^tau » (both witnesses):
  the formula of 14:112 gives E^3: A^0 -> A^3 = 0 and E^1: Pic^tau(X) -> CH_0(X)^tau; the latter is bijective mod finite iff
  rational and Albanese equivalence agree for 0-cycles on X (then it is the isogeny of Cor. 2.6, 14:65), so it fails for
  p_g > 0 (Mumford). The « id » row copies the A_a pattern.
- 14:115, n = 3, ②: « A_0^r(Y) -> A_0^r(X) bijectif ... O.K. » is right only under his marginal condition « si équiv. rat.
  = équiv. Alb. »: for X = P^3 and Y a smooth quartic, CH_0(P^3) = Z while CH_0(Y) is huge (Mumford). The same condition
  governs ②' (A_0(U) = 0) for n = 2, 3, 4, which fails for p_g > 0 (Bloch-Srinivas 1983: CH_0(X) supported on a divisor
  forces H^(n,0)(X) = 0; locator unverified).
- 14:114 (cancelled): « cd U <= dim A » needs a separably closed residue field (A = k[[t]], f = t: cd k((t)) = cd k + 1).
  For strictly henselian quasi-excellent A it is Gabber's affine Lefschetz theorem (Illusie-Laszlo-Orgogozo, Travaux de
  Gabber, Exp. XV; locator unverified).

**Open.** The Chow-theoretic Lefschetz statements ① and ② for codimension >= 2 with Q-coefficients modulo the
0-cycle/Albanese obstruction (a Bloch-Beilinson consequence; known for complete intersections of small degree,
Paranjape 1994; locator unverified); the local programme in its finite-group form; his problems (intersection forms on
N^i of punctured spectra, vanishing cycles, J^1(X) = J^1(Y)^pi).

#### 10. SA06-7: boundedness, representability, zero-cycles and the generic member, 14:118, 120-121, 123, 126, 128, 131

**What he does.** 14:118: 1) numerically trivial cycles modulo rational equivalence are described by finitely many
algebraic families => num = tau and A_a^i(X) of finite type; 2) (x,y) - (x,b) - (a,y) + (a,b) « ~_a 0 »; 1) and 2) =>
the A_r^i(X)^a are abelian varieties, the products A_r^i(X)^a x A_r^j(Y)^a -> A_r^(i+j)(X x Y)^a vanish, A_0(X)^a = Alb(X),
and 2) <=> A_0(X x Y)^a = A_0(X)^a x A_0(Y)^a. 14:120: X projective, M in K(X): bounded families of locally free sheaves
(i) <=> (ii) quotients of O(-n)^N with Hilbert polynomials in a finite set <=> (iii) one fixed shift xi + gamma(A) by
quotients of one B; proofs, (ii) => (iii) unfinished. 14:121, 123: for M' in Z^i(X) (X smooth), (i) bounded, (ii)
numerically bounded with a fixed effective translate, (iii) (i-1)! zeta = c^i(xi) for a bounded M in K(X), (iv) M' in the
image of a bounded M in K^(i)(X), (v) numerically bounded; « équivalentes » struck, and 14:123 keeps (ii) => (i) <=> (iv)
=> (iii) => (v) (« R.R. » for the factor (i-1)!). 14:126: a chain 1°) products of algebraically trivial cycles vanish
<=> 1° bis) on X x Y => 2°) A_0(X)^a x A_0(Y)^a -> A_0(X x Y)^a zero <=> 2° bis) <=> 3°) the « rectangle » ~ 0 <=> 3° bis)
<=> 4°) on an abelian variety (x+y) - (x) - (y) + (0) ~ 0, i.e. x -> (x) - (0) is a homomorphism A -> A_0(A)^tau («
évid. surjectif ! ») <=> 4° bis) A_0(A)^a -> A is an isomorphism <=> 5°) for every X, A_0(X)^a -> Alb (written « Alb(A) »)
is an isomorphism; 6°) A_0(X x Y)^a = A_0(X)^a x A_0(Y)^a; a brace groups 2°-6° bis. 14:128: the proofs of 3 => 4 (push
forward by addition) and of the bijectivity of A -> A_0(A)^tau. 14:131: the generic member Y(y) of a family of
subvarieties parametrized by a rational S, with base locus C and the blow-up X' of C: boxed A(Y(y)) = Im A(X) + Im A(C),
i.e. A^i(Y(y)) = Im A^i(X) + Im A^(i-j)(C).

**Checked** (TSV). The relation in 2) on 14:118 is written « ~ » with a subscript « a » (decided on the scan); all its
consequences need rational equivalence (for algebraic or Albanese equivalence it is trivially true; Pro note Z02).
The chain of 14:126: 1° bis => 2° (top degrees), 2° <=> 3° (the classes x - a generate), 3° bis => 4° (push forward along
addition A x A -> A), 4° <=> 4° bis (Pro note Z04), 5° => 4° bis and 5° => 6° (Alb(X x Y) = Alb X x Alb Y). Not
justified on the page: 4° => 3° bis and 4° bis => 5° (a K3 surface has Alb = 0, so 4° bis says nothing about it).
14:120, (ii) => (iii): R = Ker(O(-n)^N -> G) is locally free and bounded, hence a quotient of O(-n')^(N') for one
(n', N'), and xi + gamma(O(-n)^N) = gamma(F + R) (as Pro note B02). 14:131 by an independent argument: the incidence
variety is a projective bundle over X - C, localization gives generation by CH(X) and CH(C x S), and
CH(C_k(S)) = CH(C) for S rational; the formula is for the generic member over k(S), not over its algebraic closure.

**What is wrong / settled since.** 1) is false: Mumford (1969) excludes a finite-dimensional parametrization of CH_0 of
a surface with p_g > 0 (Pro note Z01), Griffiths (1969) gives num != tau, Clemens (1983) A_a^2 not of finite type. 2)
modulo rational equivalence is false over C already for X = Y an elliptic curve (the Albanese kernel of E x E is non-zero
by Mumford and is generated by such rectangles, Bloch 1976; locators unverified); Grothendieck himself records this
failure in his letter of 20 November 1968 (Pro note Z03). Hence 4°, 4° bis, 5° fail over C for abelian surfaces; over
an algebraically closed field of transcendence degree 0 over the prime field they are Bloch-Beilinson-type conjectures.
14:126, 5°: the target is Alb(X). 14:121: K-equivalence is not defined in the dossier.

#### 11. Reused leaves in 14:87-132 (SA06-11; one line each, not studied)

- 14:88 (« - 24 - », Prop. 3.4, C-acyclicity not intrinsic), 14:90 (« - 19 - », Cor. 2.5, Čech/Cartan-Leray spectral
  sequence): the same French typescript on cohomology of sites as 14:77-86.
- 14:97: a page of editorial comments on a draft of EGA 0_IV (« paragraphe Cohen », formally smooth algebras, fields of
  representatives, « ma rédaction », a suggested order of corollaries); 14:99: typescript « 0_IV Différentielles et
  dérivations » (Prop. 1.1, Déf. 1.2, Cor. 1.3: liftings over a square-zero extension form a torsor under Dér_A(B, J));
  14:101: Lemmas B and C of the same « Cohen » draft (E_(i,n), truncated symmetric algebras).
- 14:104: typescript page « - 115 - » of a draft on the dimension formula (Cor. 1-3, formulas (13), (14)), with his
  margins (« formule hybride, donner plutôt deux formules »).
- 14:122 (typed p. 3), 14:124 (typed p. 2): a typescript on group schemes (transporters, normalizers, representability,
  a tangent-space lemma) in the S.G.A.D. setting; 14:127 (p. 25, margin « Conserver le texte ci-contre, barré par
  erreur »), 14:129 (p. 24 bis): SGA 3 Exp. XIII § 3 material (generic Cartan subgroups, Lemma 3.4), identified by the
  Pro note F12.
- 14:132: rotated pencil fragments (x^2, x^3 - y^2, k[y], k[x,y]/xy) on IHÉS stationery.

### Hunches

- **c14b-H1 (14:71, Question 2; 14:61, crossed-out Cor. 2.2).** For an abelian variety A his Question 2 asks for an
  integral 1-cycle on A x A^dual inverting psi_A: H^(2g-1)(A)(g-1) -> H^1(A^dual), i.e. an integral algebraic
  representative of the Künneth component of the Fourier class c_1(P)^(2g-1)/(2g-1)!. For principally polarized A this is
  governed by the algebraicity of the minimal class theta^(g-1)/(g-1)! (cup with it is the integral inverse of the
  Lefschetz map H^1 -> H^(2g-1) for a unimodular polarization). That class is algebraic for Jacobians (Poincaré's formula)
  and open for a very general principally polarized A of dimension g >= 4; Beckmann-de Gaay Fortman (Compositio 2023)
  tie the integral Hodge conjecture for one-cycles on abelian varieties to it and to an integral Fourier transform
  (locator unverified). The l-adic question in characteristic p is the same problem. With his reduction (Q1 + Q2 for
  abelian varieties => Q2 for X, re-proved in the TSV), the dossier poses in 1964-65 a question that is still open, and the
  crossed-out Cor. 2.2 (« Tout homomorphisme B_X -> A_Y est défini par un Z_1 ») is its integral form. Links: SA18-14
  (cote 44, intermediate Jacobians), the integral Hodge conjecture literature (Voisin; Benoist-Ottem).
- **c14b-H2 (14:71, Question 1).** Question 1 is equivalent to: the tautological point of A_X over K = k(A_X) is the
  Albanese image of a degree-zero 0-cycle on X_K; equivalently 1 lies in the right ideal I of End(A_X) formed by the
  Albanese actions u_Gamma of correspondences Gamma from A_X to X (I contains v_* Hom(A_X, J(C)) for every curve
  v: C -> X, since every homomorphism to a Jacobian is a divisorial correspondence, and has finite index). The answer is
  yes for curves (Sym^N C a projective bundle, as Michel Hua's project notes) and for abelian varieties, and whenever some
  curve has J(C) -> A_X split; in general it is open to me. It connects with Wittenberg's work on Albanese torsors and 0-cycles
  of degree one (Math. Ann. 2008) and with Voisin's universal codimension-2 cycles (locators unverified), and inside the
  dossier with the cycle U that 14:32 says one cannot a priori find (Michel Hua's project's cross-reference).
- **c14b-H3 (14:52-71).** § 1-2 of this text is a complete l-adic proof, over any algebraically closed field, of the
  Lefschetz standard conjecture in degree 1 with both directions (Cor. 2.6 and Prop. 2.7: the inverses of
  H^1 -> H^(2n-1)(n-1) and of the comparison maps are Q-correspondences, unique and independent of l), together with
  the integral bookkeeping (Cor. 2.5, the exact denominators). The margin « Th ? » shows he meant to promote it; his letter
  to Serre (14:51, « Pour inverser phi_X, on utilise le th de Lefschetz et le cas particulier des V.A. qui est trivial »)
  announces exactly this. In the printed record this is the degree-1 case of B(X) attributed to the Albanese/Picard
  theory (Grothendieck, Standard conjectures, 1969; Kleiman 1968 and 1994; Lieberman 1968; locators unverified). Worth a
  dating check against the letter of 27 August 1965.
- **c14b-H4 (14:76-89).** The axiomatic sheets assemble the toolkit (duality, cycle rings with the projection formula and
  the Pontryagin product, H^* = Lambda^* H^1, the Gysin map as Lambda T_l(u), divisorial correspondences as Hom(A, B^*),
  homomorphisms determined by graph classes) that Lieberman (1968) used to prove the Lefschetz standard conjecture for
  abelian varieties and that Beauville and Deninger-Murre later organized through the Fourier transform. The unfinished
  « Question » of 14:89 is the divisor case of the Tate conjecture for A x B (SA06-4); if these sheets predate 1966,
  Tate's theorem answers his question over finite fields.
- **c14b-H5 (14:106-109, 14:113, 14:114).** The local programme reads the Hodge index theorem as a negativity statement
  on N^1 of a punctured spectrum (N = 3: for the cone over a surface Z, N^1 is NS(Z) modulo the hyperplane class, where the
  form is negative definite: the primitive Hodge index), with Mumford's negativity for surface singularities as N = 2.
  This is a local form of the standard conjecture of Hodge type; the cancelled 14:114 (local cohomological dimension) is
  the étale-cohomological input such a local Lefschetz theory needs, now Gabber's affine Lefschetz theorem. Testing the
  local finiteness claims on cones over surfaces with p_g > 0 should refute them as in ③' (14:113), through the local
  Chow groups of the vertex (Srinivas's work on cones; locator unverified).
- **c14b-H6 (14:111-117, 14:118, 14:126).** His conditionals « si équiv. rat. = équiv. d'Albanese » isolate exactly the
  0-cycle obstruction that Mumford (1969) and Bloch-Srinivas (1983) settled negatively over C; what survives of the global
  programme is its Q-form over number fields or modulo homological equivalence, i.e. Bloch-Beilinson (Chow-theoretic
  Lefschetz, Paranjape's connectivity for low degree) and the standard conjectures B and D (his « question numérique »).
  The open logical step on 14:126 (Albanese kernels of all X from those of abelian varieties) would follow from
  Kimura-O'Sullivan finite-dimensionality plus motivic Kuga-Satake-type statements for surfaces; I know no proof.
- **c14b-H7 (14:131).** The boxed formula for the generic member through a base locus C is the mechanism of later
  Noether-Lefschetz-type computations of Chow groups of generic hypersurface sections containing a subvariety; it is
  correct over k(S) and could serve as a lemma in an edition's commentary (locator of a printed form not searched).

### Dependencies (item ids from sweep2/SA06/WHAT_IS_WHERE.md; the page that shows each)

- SA06-3 (14:59-71) uses SA06-3's § 1: Th. 1.1, Th. 1.6, Cor. 1.7 (14:52-57; cited on 14:59 « En vertu de 1.7 », 14:60
  « On applique alors 1.1 », 14:61 « de 1.6 »), and the sheets 14:73-74 (the « isom mod torsion » of 14:59 and the torsion of
  H^(2n-1) used in Cor. 2.5).
- SA06-4 (letter to Serre) -> SA06-3: 14:51 announces the inversion of phi_X by Lefschetz and the abelian case, carried out on
  14:65-70.
- SA06-3 (Cor. 2.6, 14:65) -> SA06-6: the J-part of ③ on 14:112 for i = 1 (Pic^tau -> CH_0^tau via E^(n-1)) is Cor. 2.6
  once rational and Albanese equivalence agree (14:115-116 margins).
- SA06-3 (14:92 table of equivalences) -> SA06-6 and SA06-7: the rings A_r, A_a, A_tau, A_alb of 14:111, 14:117, 14:118 and
  14:126 are the rows of the table; SA06-1 (14:92) is the same page.
- SA06-7 (14:118: « les A_r^i(X)^a sont des V.A. ») -> SA06-6: the notation J^i on 14:103-117 presupposes it.
- SA06-5 (14:96 Hodge index, cones) -> SA06-6 (14:108: the Hodge index as negativity of a form on N^1).
- SA06-3 (14:71 Question 1) <-> SA06-3 (14:32, the cycle U; Michel Hua's project).
- Across topics: SA18-14 (cote 44, 44/002-009 per the Pro notes: abelian varieties P^i, a proposed num = tau, positivity of a
  divisor correspondence) for 14:92, 14:94-100 and 14:118; SA06-4 for the Question of 14:89 (Tate classes).
- SA06-11 (reused leaves): 14:75, 77, 79, 82, 84, 86, 88, 90, 97, 99, 101, 104, 122, 124, 127, 129, 132 (sweep 2's list
  lacks 75-86 and wrongly contains 114, which is his own cancelled remark).
- SA06-12 (planning answers): the Pro notes' M01-M14 read 14:87-117 against cote 16 questions; not used here beyond the
  notation safeguard L16 (N = A_a, not numerical). SA06-13: 14:91, 14:93, 14:102 are title sheets; 14:117 is a notation
  sheet.

### Deliverable state of scans 59-132

- **Passes.** 59-86: Codex web only (K14-05: 59-71, 73; K14-06: 74-86), each with its notes, math notes, doubts and audit;
  no Pro transcription, no second witness. 87-132: Pro `MPL_14_087-132` (frozen 15 Nov 2026, notes and doubts) and Codex
  web K14-07, K14-08, K14-09 as second witness. Blank: 72, 105, 110, 119, 125, 130. This reading (sweep 3) decided on the
  scan image: 14:59, 61, 62, 63, 64, 65, 71, 73, 80, 81, 83, 92, 118, 126 (targeted crops, not full collations).
- **Open readings.** 14:62 « AQT »; 14:65 the adjective after « Lefschetz » (« vache... »); 14:63 the left member « D_0 = »;
  14:83 « classe cherchée/dernière »; 14:92 the circled mark on A_alg -> A_(Z_l-hom) and the margin « l'équivalence ... r
  ... wh(?) et W définis par Liebermann »; 14:116 « intime(?) »; 14:126 « Alb(A) » (ink not checked); the Pro doubts file
  for 87-132 (not read in full).
- **Ready for a transcription edition?** 87-132: yes after merging the Pro doubts with the K14-07/08/09 readings (two
  witnesses exist) and adding the one-line identifications of the reused typescripts. 59-86: not yet: a single
  witness; the 13 handwritten pages (59-71, 73, 74, 76, 78, 80, 81, 83, 85) need a second full transcription pass before
  an edition; the reused typescripts (75, 77, 79, 82, 84, 86) need only identification lines.
- **For the companion.** The corrections filed here (24 rows across the stretch) are mathematical, not readings; the
  substantial ones are 14:83 (factor d), 14:112-113 (③, ③', primitive exponents), 14:115 (n = 2 indices), 14:118 and
  14:126 (the 0-cycle chain), 14:94-95 (the numerical criterion and b'').


### Counts

68 transcribed pages read (scans 59-132 less the blanks 72, 105, 110, 119, 125, 130; reused typescripts identified in one
line each); 41 check events; 24 corrections; 7 hunches (c14b-H1 to c14b-H7). Claude Opus 5.5 at effort max,
c14_c15rest_part2, 19 Nov 2026.


## SA06 sweep 3, stretch c14_c15rest, part 3: cote 15, scans 87-95, 109-126, 138 and 170-206

Claude Opus 5.5 at effort max, c14_c15rest (launched by a28ea31fa17dd65e1, Claude Opus 5.5 at effort max), sweep 3
reader, 19 Nov 2026. Parts 1 and 2 (cote 14) are by the sub-readers c14_c15rest_part1 and c14_c15rest_part2 (both
Claude Opus 5.5 at effort max) and are merged into c14_c15rest.md.

**Witnesses.** 15:87-95 and 109-126, 138: Pro package MPL_15_087-138 (text), Codex web K15-03 (87-102), K15-04
(103-119), K15-05 (120-138) as second witness. 15:170-206: see the second block below. Blank (ink measured at 40 dpi,
same profile as the cote's other blanks): 15:116. P3-nn below is row nn of c14_c15rest_part3_CHECK_EVENTS.tsv. Scans 128-137 were read in sweep 3 (STUDY.md §§1-2); 15:96-108 too.

### A. 15:88-94 (his pages): Frobenius as a Zariski generator; compactness of Ker(epsilon) is the Riemann hypothesis (SA06-9)

The odd scans 87-95 are reused typescripts (section D). His pages are the even scans 88, 90, 92, 94. They come
straight after 15:84-86 (STUDY §2: the compact part of a commutative motivic Galois group) and before 15:96-106
(STUDY §1: the strong and weak conjectures on Frobenius eigenvalues), and they supply the frame that 15:100 uses.

- **15:88.** For an arbitrary band L, the coradical L' = corad(L) is commutative, gives a quotient gerbe with band L',
  i.e. an algebraic group H, and "ce qui précède" (15:84-86) gives (Ker(epsilon: H -> G_m))^0 a compact torus. Then the
  finite-field case: a category of motives with a tensor endomorphism of the identity that is "générateur"; L is then
  commutative, a group G of multiplicative type with an element f ("frobenius") generating G in the Zariski sense.
- **15:90.** The dictionary: (a) T of multiplicative type over Q with f in T(Q) generating T <=> (b) a subgroup M of
  Q̄* stable under Gal(Q̄/Q) => (c) a full subcategory of the Q-vector spaces with a semisimple endomorphism, stable
  under tensor product, sum and subobjects. A cocharacter j: G_m -> T is a Galois-invariant j*: M -> Z (a tensor
  grading); epsilon: T -> G_m with epsilon j(lambda) = lambda^alpha is a rank-1 object Lambda of degree alpha. Then
  (a) T^0/Im j compact => (b) there is q > 0 with |m| = q^(j*(m)/alpha) for all m in M <=> (c) on every object of
  degree i the eigenvalues of f have absolute value q^(i/alpha).
- **15:92.** Proof of (a) => (c): T_R^0 = U.S_R with U the maximal compact subtorus and S = Im j; f^nu = u j(x);
  eigenvalues of absolute value x^(i/nu); epsilon(f)^nu = x^alpha, so x^(i/nu) = q^(i/alpha). Then (margin "?") "on
  sait que a équivaut au fait que M est ... munissable d'une structure 'positive' du style motivique".
- **15:94.** With Q' the maximal totally real field of Q̄ (= 𝕂 of 15:128) and alpha = 2: (a) <=> every lambda in M
  has a power in Q'(i)* and lambda lambda-bar = q^(j*(lambda)). Cor.: if all conjugates of lambda have the same absolute
  value, some power lambda^r lies in Q'(i) (so the condition does not depend on the embedding). Proposition, for
  lambda in Q̄* and q > 0 rational, equivalent: (i) all conjugates have |lambda_alpha| = q^(i/2); (ii bis) a power
  lambda^n in Q'(i) with lambda^n times its conjugate = q^(in); (ii) lambda in Q'(i) and lambda lambda-bar = q^i; (iii)
  lambda is an eigenvalue of f in a representation of some (G, f, j, epsilon) with epsilon j(lambda) = lambda^2,
  Ker(epsilon) compact, epsilon(f) = q; (iv) a commutative Q-algebra with positive involution ("algèbre de Riemann"),
  f f' = q^i, and a Q-homomorphism to Q̄ sending f to lambda. Margin: a real such lambda is totally real and
  lambda = (q^(1/2))^i, "cas trivial".

**What is proved, and what I checked** (check events P3-01 to P3-08):
- (a) <=> (b) of 15:90 (re-proved): a Q-point f is a Galois-equivariant map X*(T) -> Q̄*; f generates T iff that map
  is injective; its image is M. (b) => (c): Rep_Q(T) is the category of pairs (E, phi) with phi semisimple and
  eigenvalues in M; morphisms commuting with f commute with T because f is Zariski-dense. The converse (c) => (b)
  needs the subcategory to be stable under duals too (otherwise the eigenvalues form only a monoid); his arrow is
  marked doubtful in both witnesses.
- (b) <=> (c) and (a) => (c) as on 15:92 (re-proved; T_R^0 = U.S_R holds because the maximal split subtorus maps to
  the anisotropic T^0/S, so lies in S_R, and S is not in U since epsilon j is not trivial). The absolute values are
  |x| and q = |epsilon(f)|.
- The converse (b) => (a), which 15:94 uses ("La condition a équivaut à"), re-proved: for weight-0 characters m every
  conjugate has |m| = 1, so every complex conjugation acts by -1 on X*(T^0/S) (x) Q, which is R-anisotropy.
- The Cor. of 15:94 (re-proved): if t = |lambda|^2 for all conjugates, |N(lambda)| = t^(d/2) with d = [Q(lambda):Q], so
  t^d is rational and lambda^d is a Weil number in the sense of 15:131 (STUDY §1), hence in Q'(i). A power is needed:
  lambda = 2^(1/4) has all conjugates of absolute value 2^(1/4), |lambda|^2 = sqrt 2 is irrational, lambda^4 = 2.
- The Proposition of 15:94 (re-proved): (i) <=> (ii) is 15:131-132; (ii bis) => (i) because complex conjugation is
  central on Q'(i); (iii) => (i) is the 15:92 argument (Ker(epsilon)^0 compact <=> G^0/Im j compact, since
  (Ker epsilon)^0 . Im j = G^0 with finite intersection); (i) => (iii) by taking M generated by the conjugates of lambda
  and q, j*(lambda_alpha) = i, j*(q) = 2 (well defined by taking absolute values), and this needs q != 1; (ii) <=> (iv)
  with A = Q(lambda) and complex conjugation (a commutative algebra with positive involution is a product of CM and
  totally real fields: STUDY §2).

**Wrong** (CORRECTIONS): the margin of 15:94 drops a sign: a real lambda is +-(q^(1/2))^i. In (iii), q = 1 must be
excluded. 15:92 writes x^(i/nu) for |x|^(i/nu). None of these affects the conclusions.

**Open.** 15:92's claim that (a) is equivalent to the existence of a "positive" structure of motivic type is marked
"?" by him; it is the existence of polarizations on a graded Tannakian category with commutative group, known in that
theory (Saavedra Rivano, Catégories tannakiennes, LNM 265, 1972, ch. VI; Deligne-Milne, Tannakian categories, LNM 900,
1982, §5; locators unverified). Status: known; 15:94 is the Weil-number half of the Honda-Tate frame (Tate, Sém.
Bourbaki 352, 1968; Milne, Motives over finite fields, 1994; locators unverified).

### B. 15:110-114 (his pages): the Weil-number torus G(q), the decomposition-field cocharacter and the norm-one torus G' (SA06-9)

- **15:110.** M(q) = the lambda in L (CM, Galois over Q) with lambda lambda-bar = q^i that are units away from p; M_0(q)
  (weight 0) mod torsion embeds in (Z^P)', P the primes of L over p (margin: M_0(q) = M_0(p)). Assume the primes of K
  over p split in L. A prime 𝔭 over p gives the linear form lambda -> v_𝔭(lambda), whose Galois conjugates "engendre
  M̌ mod torsion", hence a cocharacter nu_L: G_m,L -> G_L. With Gamma_𝔭 the decomposition group, L_0 = L^(Gamma_𝔭),
  K_0 = L_0 ∩ K: L_0 is the smallest field of definition of nu; the completion of L_0 at 𝔭_0 is that of "Z_ℓ" (ink);
  (L_0, 𝔭_0) is unique up to unique isomorphism (via the relative henselization of Z_(p)); L_0 is totally imaginary
  because tau𝔭 != 𝔭.
- **15:112.** (Z^P)' is the character group of G' = prod_(K_0/Q) U = Ker(prod_(L_0/Q) G_m -> prod_(K_0/Q) G_m), U the
  norm-one torus of L_0/K_0, so G'(Q) = Ker(N: L_0* -> K_0*); a homomorphism phi: G' -> G, an isogeny onto G^(0u);
  nu_(L_0) "se factorise par G'_(L_0)" via nu'. Inserted: "f_0 = f j(p^(1/2)) (de G^(0u)(Q))" lifts to G'(Q) only if
  phi is an isomorphism, i.e. M(q)/torsion = (Z^P)'.
- **15:114.** Margin "demander à Serre ?". It is not so in general, even (reading doubtful) for K_0 = Q: an example
  where Z/2 acts non-trivially on Pic(A), A the integers of L, suffices; Z/2 acts on Pic(A) "par symétrie", so Pic(A)
  not a 2-group suffices.

**Checked** (P3-09 to P3-15):
- (Z^P)' is the minus part {n : n_(tau𝔮) = -n_𝔮}: weight-0 elements have v_𝔮(u) + v_(tau𝔮)(u) = v_𝔮(u u-bar) = 0;
  the kernel of M_0(q) -> Z^P is the roots of unity (Kronecker). As a Galois module (Z^P)^- = Ind from
  Gamma_𝔭 x <tau> of Z with tau acting by -1, which is X*(R_(K_0/Q) R^1_(L_0/K_0) G_m): his G' is right
  ([L_0:K_0] = 2 because tau is central and not in Gamma_𝔭).
- The stabilizer of v_𝔭 is Gamma_𝔭 (the forms v_𝔮 are distinct on M(q) (x) Q because M_0 has finite index in
  (Z^P)^-, by 15:96); (L_0)_(𝔭_0) = Q_p because the decomposition field has e = f = 1 at 𝔭_0; L_0 is CM because tau
  is central and not in Gamma_𝔭. The Galois conjugates of v_𝔭 generate a subgroup of finite index of M̌ mod
  torsion, not always all of it (Pro note CM02b: cokernel Z/3 for Q(sqrt(-23)), p = 2).
- **15:110, "Z_ℓ": reading decided on the scan** (250 dpi): the subscript is his looped ℓ, in both witnesses; the
  mathematics needs Z_p (his slip, like the "2" for p of 15:40).
- **15:112, the inserted f_0: reading decided on the scan**: "= f j(p^(1/2))", exponent +1/2, base p. Its
  character value is epsilon(f j(p^(1/2))) = qp, not 1 (Pro note FR15), so it is not in G^(0u). The weight-zero
  Frobenius is f j(q^(-1/2)), which lies in G^(0u)(Q(sqrt q)); its square f^2 j(q^(-1)) lies in U(Q).
- The factorization of nu through G' is **refuted** (P3-13): epsilon∘phi is trivial while epsilon∘nu = v_𝔭(q) > 0.
  Refined statement: with psi(m) = (v_𝔮(m) - v_(tau𝔮)(m))_𝔮 (the map dual to phi) and nu'' the cocharacter
  n -> n_𝔭 of G', 2nu = phi∘nu'' + v_𝔭(q) j: only the weight-zero part of nu factors through G'.
- The lifting criterion (P3-14, re-proved): for the canonical weight-zero Frobenius point (the point of
  D(M_0/torsion) whose evaluation on M_0 is the inclusion), a lift f' in G'(Q) = Ker(N_(L_0/K_0)) evaluates (Z^P)^-
  into L*, each value a norm-one p-unit, hence in M_0(q), with divisor n; so every n in (Z^P)^- is a divisor of an
  element of M_0(q) and phi is an isomorphism. The necessity therefore holds, and it rests on M_0(q) being the full
  group of norm-one p-units of L, which answers the caution of Pro note FR16 (a bare isogeny such as 2: G_m -> G_m
  does have rational lifts).
- 15:114 (P3-15, re-proved): for L = L_0 imaginary quadratic and p = 𝔭 tau𝔭, the image of M_0 in (Z^P)^- = Z is
  the multiples of the order of [𝔭]^2; complex conjugation acts on Pic(A) by inversion, so non-trivial action means
  Pic(A) is not of exponent 2, and by Chebotarev some split p lies in a class of order > 2. His "Pic(A) not a
  2-group" is sufficient, not necessary (Z/4 also works). Example: Q(sqrt(-23)), p = 2, [𝔭] of order 3 (Pro FR14).
- The cokernel in general (P3-26, re-proved): for n in (Z^P)^- put 𝔞_n = prod 𝔮^(n_𝔮), so tau𝔞_n = 𝔞_n^(-1).
  n -> [𝔞_n] maps coker(M_0(q) -> (Z^P)^-) to Cl(L), with kernel inside E_K^+/N_(L/K)(E_L) (if 𝔞_n = (alpha),
  alpha alpha-bar is a totally positive unit e of K, and n is reached iff e is a relative norm of a unit; this group
  is killed by 2). So up to a 2-group the obstruction to lifting the Frobenius is the subgroup of Cl(L) generated by
  the classes of the minus-divisors at p, on which conjugation acts by inversion: the precise form of 15:114.

**Wrong** (CORRECTIONS): Z_ℓ for Z_p (110); f_0 (112); the factorization of nu (112); "engendre M̌ mod torsion"
(110, finite index only).

**Open.** None of his own beyond the "demander à Serre ?", which 15:114 answers. Status: known in substance as the
Weil-number torus with its p-adic (slope) cocharacter (Langlands-Rapoport, Shimuravarietäten und Gerben, 1987;
Milne 1994; locators unverified); his explicit norm-one torus G' and the class-group obstruction to lifting the
Frobenius are his own working of it.

### C. 15:117-125 (his pages): real fibre functors, polarizations, the finite-field cocharacter i (SA06-10)

(The Artin-Tate quotient of SA06-10 is on 15:135-137, read in STUDY §2; 15:138 is a reused errata sheet. On this
stretch SA06-10 is 15:117-125.)

- **15:117.** Margin: "N.B. On n'utilise que les éléments de structure 1, 2, 3" (the numbered "éléments de structure
  motiviques" of the cote-14 cover, 14:2: part 1 of this stretch). G connected over Q from a motivic situation M,
  U = Ker(G^0 -> G_m by epsilon). Proposition 1, equivalent: (i) U is a torus; (ii) epsilon is primitive in the
  characters of G^0; (iii) M_R has an ("unmodified") fibre functor, i.e. the gerbe 𝒢_R is not empty. Always so if M
  has even degrees (j(mu_2) = 1). Proposition 2, equivalent: (i) U = U^0 x mu_2; (ii) epsilon is a square;
  (iii) 𝒢_R is empty. Proofs: (i) => (ii) and (1 ii) <=> not (2 ii) from j with epsilon j(lambda) = lambda^2;
  (iii) => (ii) because odd-degree objects of M_R have even rank (fundamental alternating form); (i) => (iii) because
  H^2(R, T) = 0 for a compact torus T; even degrees give j = 2j', epsilon j' = id. Cor.: the even part M^pair (group
  G/j(mu_2)) has a real fibre functor.
- **15:119.** Cor. in the case of Prop. 2: "G^0 = U^0 x G_m, epsilon = pr_2, j(lambda) = inj_1(lambda)^2" (ink); the
  Tannakian structure of M_R is determined by G and the unique non-zero element of H^2(R, U) (from H^2(R, mu_2)); an
  object E of degree 1 and rank 2 generates an already R-twisted subcategory on which U^0 acts trivially. If 𝒢_R is
  not empty, its isomorphism classes form a torsor under H^1(R, U) = 2U(R) (non-canonically (Z/2)^(dim U)); each
  object gives a polarizing structure i_1: mu_2,C -> G^0_C with epsilon i_1 = id, i_1 i_1-bar = j, these form a torsor
  under 2U(R), and the map H^0(𝒢_R) -> Pol is equivariant, hence bijective (15:121: "se déterminent mutuellement").
- **15:121.** "À voir": do the automorphisms of (G^0_R, epsilon, j), of (G^0_Q, epsilon, j) or of (G, epsilon, j) act
  transitively on Pol(G)? Can a polarization, or a packet, be singled out? For motives over F_q, q = p^n: a
  distinguished conjugacy class of i: G_m,C -> G_C with i-bar i = j, epsilon i = id, given for commutative G
  (M in L CM) by lambda -> (1/n) v_𝔭(lambda), with "[v_p(lambda) v_p(lambda-bar) = v_p(lambda lambda-bar) = j*(lambda);
  v_p(q) = 1]". Boxed caveat: this form is not always integer-valued, "même sur le ss-groupe de M où j = 0" (reading
  of the Codex witness, which the ink supports), example q = p != 2, L = Q(sqrt(.)) (blotted) of class number 1,
  p = 3, 7, 11. Margin: i and its distinct conjugates (2n of them if [K:Q] = n) generate the cocharacters of G^0. An
  automorphism of G^0 respecting i is the identity; the effectivity structure of M, M_R, M_C is determined by i.
- **15:123.** Hence privileged classes of polarizing structures: the i|mu_2. The differences i - i' form "un
  sous-groupe d'indice fini de Hom(G_m,C, G^0_C)", but say nothing on the restrictions to mu_2 ("Question semble
  secondaire"); a packet of privileged real fibre functors. A canonical involution u -> u' of G from complex
  conjugation on M (central in Gal(L/Q)): the symmetry on Ker j*, the identity on Im j, complex conjugation on the
  cocharacters.
- **15:125.** It does not seem that this involution comes from an involution of the gerbe 𝒢 (no covariance with the
  conjectural fundamental element of H^2(Q, U), "qui serait d'ordre divisant 2").

**Checked** (P3-16 to P3-25):
- Prop. 1 and 2 (re-proved, for G commutative, the frame of 15:84-88): Ker(epsilon) has component group Z/k with
  epsilon = k epsilon', and k divides j*(epsilon) = 2, which gives the dichotomy; in the square case
  epsilon'(j(-1)) = -1 while epsilon' is trivial on U^0, so U = U^0 x j(mu_2); a rank-1 object of degree 1 (the
  character epsilon') cannot carry a non-degenerate alternating form, so no real fibre functor; H^2(R, S^1) =
  S^1/{z/z-bar} = 0 and H^2(R, mu_2) = Z/2 (Pro note T04 computes the same). For G not commutative Prop. 1 fails as
  written: for an elliptic curve over Q without CM, G = GL_2, epsilon = det is primitive and the Betti realization is a
  real fibre functor, but U = SL_2 is not a torus (nor compact). So the propositions are for commutative G (motives over
  finite fields, 15:88); in general (i) must read "U connected", and (i) => (iii) then needs an argument the page does
  not give.
- The torsor statements of 15:119 (re-proved): for a compact torus U, H^1(R, U) = X_*(U)/2 = 2U(R) canonically
  (x -> x(-1)); the two torsors under 2U(R) and an equivariant map give a bijection.
- **15:119, the Cor.: reading decided on the scan**: "epsilon = pr_2, j(lambda) = inj_1(lambda)^2" with subscript 1
  (both witnesses agree), after a cancelled "pr_2(lambda)^2". **Refuted, with the refinement**: Ker(pr_2) = U^0 is
  connected, which contradicts Prop. 2 (i). In the case of Prop. 2, (u, lambda) -> u j(lambda) is an isomorphism
  U^0 x G_m -> G^0 (j(-1) is not in U^0), under which epsilon = pr_2^2 (lambda -> lambda^2) and j = inj_2.
- 15:121, the cocharacter i (re-proved): with v_p normalized by v_p(q) = 1, v_p(lambda) + v_p(lambda-bar) =
  v_p(lambda lambda-bar) = j*(lambda), so i + i-bar = j and epsilon i = id. **Reading decided on the scan**: the ink has
  "v_p(lambda) v_p(lambda-bar)" with no "+"; the sum is meant.
- The caveat (computation): his example L = Q(sqrt(-p)) gives v_p(sqrt(-p)) = 1/2, a non-integral value in weight 1;
  in weight 0 it gives nothing, since 𝔭 = tau𝔭 there forces v_𝔭 = 0 on norm-one elements. A weight-0 example:
  L = Q(i, sqrt 5), p = q = 5, phi = (1 + sqrt 5)/2: N(1 + i phi) = (5 + sqrt 5)/2 . (5 - sqrt 5)/2 = 5, so
  𝔓 = (1 + i phi) is a prime over 5 with e = 2 and tau𝔓 != 𝔓, and u = (1 + i phi)/(1 - i phi) has u u-bar = 1 and
  v_p(u) = 1/2. His caveat is right.
- The restriction i|mu_2 of 15:123 (computation): it is well defined when the values of i have odd denominators
  (x -> x^d is the identity of mu_2 for d odd) and undefined when a denominator is even. Even denominators occur in the
  case of Prop. 1: L = Q(i), p = 5 = pi pi-bar, q = 25, lambda = 5 pi^2 = 15 + 20i, lambda lambda-bar = 625 = q^2, so
  i(lambda) = v_pi(lambda)/v_pi(25) = 3/2, while M has only even degrees (epsilon primitive, real fibre functors
  exist). So the "paquet de R-foncteurs fibres privilégiés" of 15:123 needs a definition when i is fractional
  (hunch c15-H2).
- "Sous-groupe d'indice fini" (15:123, re-proved): epsilon(i - i') = 0, so the differences lie in X_*(U^0), of corank 1;
  they can have finite index only there (Pro note T12 finds the same).
- The involution (re-proved): lambda-bar = q^(j*(lambda))/lambda gives c(m) = j*(m)q - m, so c acts by -1 on
  X*(U) = X*(G^0)/Zq: it is inversion on U and sends h to -h in H^2(Q, U) (Pro note T16). If 2h = 0, as he expects,
  the class is invariant, so the reason given on 15:125 is not an obstruction; what remains is whether a lift to the
  gerbe can be chosen of order 2.

**Wrong** (CORRECTIONS): the Cor. of 15:119; the missing "+" on 15:121; "même sur le ss-groupe où j = 0" with the
example Q(sqrt(-p)); the finite-index target on 15:123; the reason given on 15:125.

**Open (his).** The transitivity question of 15:121 ("À voir"); the choice of privileged polarizations (15:121-123),
which needs i integral on mu_2; the lift of the involution to the gerbe (15:125); the "élément fondamental conjectural"
of H^2(Q, U). Strongest reduction on the pages: Prop. 1-2 reduce the existence of real fibre functors to the
primitivity of epsilon; 15:119 reduces the real fibre functors to the polarizing structures (a bijection of torsors).
Status: known in substance (Deligne-Milne 1982, §§4-5, polarizations and real fibre functors; Serre's argument for
supersingular curves, 15:11, SA05-18; locators unverified); his: Prop. 1-2 in this form, the torsor bijection of
15:119-121, the cocharacter i over F_q and the canonical involution.

### D. Reused leaves in 15:87-138 of this stretch (SA06-11; identified, not studied)

- 15:87: English typescript p. 86, section VI (reflexive modules over a noetherian integrally closed domain, Theorem
  VI.5, "the thesis of the author, Chapter II, Lemma 0.1"); author unidentified (Pro notes).
- 15:89, 91, 93: French typescript leaves of SGA 4 VIII (Remarque 3.13 on conservative families of fibre functors at
  very dense sets; the end of the proof of 9.4, descent of étale sheaves), typescript pp. 42-43, 88 (locators
  unverified).
- 15:95, 109: R. Steinberg, Regular elements of semi-simple algebraic groups, Publ. Math. IHÉS 25 (1965), §§1-2,
  typescript pp. "-7-", "-10-" (identified in the Pro notes; locator unverified).
- 15:111, 113, 115, 120, 122, 124, 126: an English typescript (pp. 74-86) of the projectivity criterion of
  B. G. Moishezon, Izv. Akad. Nauk SSSR 28 (1964), 179-224: his margins cite pp. 208, 210, 213 of the original
  (identification as in the Pro notes; translator unknown).
- 15:118: an errata sheet ("Page 33", "Page 35 ... supprimer 'lisse sur k'"), with a cancelled correction compared in
  the Pro notes to SGA 3 VIII 7.13(b).
- 15:138: a Bourbaki errata sheet ("n° 505", p. 16) for Topologie générale IX (Polish, Souslin and Lusin spaces).

### Witnesses for 15:170-206

- 170-171, 179-194: Pro MPL_15_170-194r (text); Codex K15-06 (179-183), K15-07 (184-194), B15-01 (170, 171, 181, 188).
- 172-178: no page of MPL_15_170-194r; the Pro checkpoint MPL_15_139-194_checkpoint_01 (pages, doubts and inventory,
  no notes file) is the text; Codex K15-06 is the second witness.
- 195-206: the Pro package MPL_15_195-228+18_002-017 exists (its README: root and pages/ authoritative; a second Pro
  chat, `_chatB_unzipped`, is a further witness) and is the text; Codex K15-08 is the second witness. The launch
  prompt pointed at the Codex folders for 172-178 and 195-206; the Pro transcriptions were read instead.
- Covers and titles (his): 172, 180, 182, 189, 190. 181: a private administrative document (redacted in the Pro
  transcription), not read. 175: a cancelled draft (read with keepdel).

### E. 15:170 (his agenda, SA06-14)

"Foncteurs fibres motiviques, et groupes fondamentaux motiviques. À examiner:" 0) abelian varieties "à la Weil"
attached to pure motives of odd weight, Hodge-Riemann conditions; 1) extension of the groups defined by "des
présentiques" (Pro) or "des places arithmétiques" (Codex B15-01), unresolved on the image, then "Groupe fondamental
motivique" (underlined); 2) relations with class field theory; 3) the case of the spectrum of a finite field, the
motivic problem of "points" (Pro; Codex "parties") with values in R "???"; 4) the role of motivic fundamental groups
in comparing canonical lattices (Hodge: two transcendental lattices for different places, the transcendental lattice
and the Hodge lattice; l-adic: two transcendental lattices); 5) relations of 4) with his old notes; 6) L-functions,
functional equation; 7) "Structures positives" (Pro; Codex "pratiques"); 8) a topology to put on Z; 9) the Riemann
hypothesis "??", margin: Hodge-type positivity by reducing to questions on divisors, by blowing up, "ou variétés de
drapeaux ??" (Codex; Pro "ou vertu des pinceaux ??").

**Readings decided on the scan** (250 dpi): the left-margin marks stand beside the items they mark: "OK *" beside 1),
"OK" beside 3), "*" beside 4), "OK" beside 7). Both witnesses set them as margins after items 0, 2, 3 and 6, which
attaches them to the wrong items in a reading. Item 9's margin ends "ou Variétés de / drapeaux ??" (Codex right);
item 7 reads "Structures positives" (Pro right, medium confidence). The items marked OK, 1, 3 and 7, are the ones the
dossier treats: the motivic fundamental group (15:189-205), finite fields and real points (15:84-138), positivity
(15:117-125).

- **What the rest of the dossier does with it** (read): item 3 is 15:84-138 (Weil numbers, real fibre functors,
  15:117-125); item 4 is 15:191-205 (the fibre functors xi_l, xi_p, xi_infinity, xi_Z and their lattices); item 8 is
  close to the absolute cohomology of 15:172-178 (Spec Z with H^3(Spec Z, Q(1)) = Q); item 9's margin is the
  Hodge-index route to the standard conjectures (cote 14: SA06-4 to SA06-6, parts 1-2 of this stretch).
- Sweep 2 placed SA06-14 at "cote 15, scan 179": the agenda is on scan 170 (correction).
- Status: his agenda; no claims to check. "VA à la Weil" reads as Weil's intermediate Jacobians (Weil, On Picard
  varieties, Amer. J. Math. 74 (1952); locator unverified), which are abelian varieties by a Hodge-Riemann argument.

### F. 15:172-179 (his pages): "Calculs de cohomologie absolue des Motifs de Tate Z(n)" and a Brauer-group draft (SA06-16)

Sweep 2's title for SA06-16 ("étale cohomology of curves over finite fields") does not fit the pages: the objects are
F_q, Spec Z and its open subsets U, and schemes with factorial strict local rings.

- **15:173.** pi = Gal(F̄_q/F_q) = Ẑ generated by f; for a finite Z_l-module M, H^0 = Ker(1 - f), H^1 = Coker(1 - f),
  H^i = 0 for i >= 2; H^0(pi, Z_l(n)) = 0 (n != 0); H^1(pi, Z_l(n)) = Z_l/(1 - q^n) non-canonically: Z_l (n = 0), 0 if
  l does not divide 1 - q^n (n not divisible by omega_l(q), the order of q mod l), Z/l^(v_l(1 - q^n)) otherwise;
  rationally H^i(pi, Q_l(n)) = 0 (n != 0), H^0 = H^1 = Q_l (n = 0). Then the "absolute" motivic groups:
  ℍ^i(F_q, Q(n)) = 0 for n != 0; ℍ^0(F_q, Q) = ℍ^1(F_q, Q) = Q; integrally ℍ^0(F_q, Z) = ℍ^1(F_q, Z) = Z,
  ℍ^1(F_q, Z(n)) = Z/(1 - q^n) for n != 0 ("mod p-primary ?"); H^i(Spec Z, Z(1)) = Z for i = 3, else 0;
  ℍ^i(Spec Z, Z) = Z for i = 0, else 0. Margin: H^i(Spec Z, Q(n)) = H^i(U, Q(n)) for U open and "n != 0".
- **15:174.** Purity i_x^! M = i_x^* M(-1)[-2] and the localization sequence for X = Spec Z, U open, S = X - U; for
  M = Q(n): the restriction is an isomorphism for n != 1; for n = 1 the six-term sequence with Q^S twice gives
  "H^i(X, Q(1)) = 0 sauf pour i = 3, où on trouve Q !".
- **15:175.** Cancelled draft: crossed homomorphisms of Z, Z^1(Z, M) = M, B^1 = (1 - f)M, H^1(Z, M) = M/(1 - f)M.
- **15:176.** When the strict local rings are factorial, H^1(X, Div^0) = 0, whence Prop. 5.4 (under 5.1 a), X
  irreducible with generic point y): H^2(X, G_m) -> H^2(X, R_X*) -> H^2(y, G_m) = Br(y) are injective; Cor. 5.5:
  Br(X) -> Br(K) is injective; Th. 5.6 a): for X local, xi in H^2(X, G_m) lies in Br(X) iff some finite étale
  surjective X' -> X kills it.
- **15:177-178.** Local cohomology H^i_x(G_m) = Z (i = 1), 0 otherwise; H^i_S(X, G_m) = H^(i-1)(S, Z) = Z^S, 0,
  (Q/Z)^S, 0 for i = 1, 2, 3, >= 4; for Spec Z: H^0 = Z* = {+-1}, H^1 = H^2 = 0, H^3 = Q/Z (sum of invariants);
  H^0(U, G_m) = Z/2 + Z^S, H^1 = 0, H^2 = Ker((Q/Z)^S -> Q/Z), H^i = 0 (i >= 3); Kummer: H^1(U, mu_(l^n)) = (Z/l^n)^S,
  H^2 = Ker((Z/l^n)^S -> Z/l^n); H^1(U, Z_l(1)) = Z_l^S, H^2(U, Z_l(1)) = Ker(Z_l^S -> Z_l) ("petite modification l = 2
  en dim 0"); H^i(X, Q(1)) = 0, 0, 0, Q for i = 0, 1, 2, 3.
- **15:179.** For X noetherian without embedded primes, (5.1.) 0 -> G_m -> R_X* -> Div_X -> 0 (étale sheaf of Cartier
  divisors); H^p(X, R_X*) is torsion for p > 0 (crossed paragraph), so d: H^i(X, Div_X) -> H^(i+1)(X, G_m) is
  bijective mod torsion for i >= 1; margin "Donner le corollaire 5.4."; factoriality gives an isomorphism of étale
  sheaves (the page stops at the colon).

**Checked** (P3-27 to P3-34):
- 15:173 (re-proved): cohomology of Ẑ with Z_l-coefficients (cd 1, H^1 = coinvariants); the three cases of
  H^1(pi, Z_l(n)) (f acts by q^n; l | 1 - q^n iff omega_l(q) | n, for l odd; for l = 2 always). His integral values
  for F_q agree with K_(2n-1)(F_q) = Z/(q^n - 1) for n >= 1 (Quillen, Ann. of Math. 96 (1972); locator unverified)
  and with ℍ^1(F_q, Z) = Z (the Weil group Z, not Ẑ: hunch c15-H4).
- 15:174 and 178 (re-proved): with H^1(U, Q(1)) = Q^S mapping isomorphically to Q^S by valuations, and
  H^2(U, Q(1)) = Ker(Q^S -> Q) mapping injectively to Q^S, the sequence gives H^1 = H^2 = 0 and H^3(X, Q(1)) =
  Q^S/Ker(sum) = Q. For n != 1 the residue terms are the cohomology of Q(n - 1) on S, which vanishes: restriction is an
  isomorphism. **The margin of 15:173 says n != 0; the computation of 15:174 shows n != 1 is the condition**
  (for n = 1 the restriction is not an isomorphism; for n = 0 it is). Both witnesses read n != 0: his slip, corrected
  by his own next page.
- 15:177-178 (re-proved): purity for G_m on a regular one-dimensional scheme; H^2(S, Z) = H^1(S, Q/Z) = (Q/Z)^S;
  the values for Spec Z agree with Artin-Verdier (Pic Z = Br Z = 0, H^3 = Q/Z; Milne, Arithmetic Duality Theorems,
  II.2; locator unverified), the real place being the "petite modification l = 2" he reserves.
- 15:176 and 179 (re-proved): with factorial strict local rings Div = sum over codimension-1 points of (i_x)_* Z, so
  H^1(X, Div) = sum Hom_cont(Gal, Z) = 0 and H^2(G_m) -> H^2(R*) is injective; R^1 j_* G_m = 0 (Hilbert 90 on the
  strict henselizations), so H^2(X, j_* G_m) -> H^2(y, G_m) is injective (edge map). H^p(X, R*) is torsion for
  p > 0 (higher Galois cohomology is torsion), hence the bijectivity mod torsion. Known: Grothendieck, Le groupe de
  Brauer I-II, in Dix exposés (1968) (locators unverified). Th. 5.6 a) is the classical criterion (an Azumaya algebra
  over a local ring splits on a finite étale cover; conversely descent of a matrix algebra); known, same source.
- **15:179, "(1.1.)" and the margin: readings decided on the scan**: the equation number is "(5.1.)" and the margin
  "Donner le corollaire 5.4." (Codex K15-06 reads the same; the Pro text has "(1.1.)" and "donne le(?) corollaire
  3.4.(?)"). The draft is numbered §5: 179 (5.1) comes before 176 (5.3-5.6) in its order, the sheets are filed in
  reverse.

**Open (his).** "(mod p-primary ?)" on 173 (the p-part of the integral groups); "= 0 ?" for H^3(U, Q(1)) (174;
answered by 178: 0 for U != X); "[est-ce nul ??]" (174), which the SA05 reader of the same pages answers: no,
H^1(Spec Z, Q(n)) = K_(2n-1)(Z) (x) Q = Q for odd n >= 3 (Borel). 15:172-178 were read independently in
sweep3/SA05/readings/c15b_c12_c11.md §1.6 (Claude Opus 5.5 at effort max, agent a7b7747fd6dd29f87), which places them
under SA05-10 and reaches the same checks and the same correction (n != 1).

### G. 15:182-187 (his pages): "Généralités fonctoriello-catégoriques sur la distribution des frobenius dans les groupes de Galois motiviques" (SA06-15)

- **15:183.** M motives of finite type over S of finite type over Z; assume even degrees (otherwise use M^pair, as the
  Cor. of 15:117 allows); a closed point s gives "R-points motiviques" (real fibre functors) of M; fix one, with group
  G_R. Replace s by pairs s' = (s, i), i: G_m,C -> G^(s)_C "de type préférentiel" (15:121); each s' gives a real
  point of M, a class xi(s') in H^1(R, G^00_R) (G^00 = Ker(epsilon on G^0_R)), and u(s'): G(s)_R -> G_R^(xi(s'))
  compatible with epsilon and j, determined up to conjugation by G^00_R(R).
- **15:185.** A polarization pi on G^0_R, given by i: mu_2,C -> G^0_C; v(s') = u(s')_C ∘ (i(s')|mu_2); the transported
  polarization must be the one defined by the v(s'): for xi(s') constant, the polarizations of the various v(s') must
  coincide, "une condition non tautologique sur la distribution des u(s')"; but the polarizations of a real group H
  given by mu_2 -> H_C form a finite set "si G est commutatif en tous cas !" (margin "? à vérifier"). "Conformément aux
  conjectures de Tate magnifiées", the u(s') recover the effectivity structure:
- **15:187.** the cone expressing effectivity is generated by the rays defined by the v(s'): an "analytic" form of the
  fact that the eigenvalues of the Frobenius f(s') in G_R^(xi(s'))(R), in every representation, even of
  G_C^(xi(s')), are algebraic integers, "une condition arithmétique assez draconienne !".

**Checked** (P3-35 to P3-37):
- The finiteness (re-proved): for H commutative, Hom(mu_2, H_C) = 2H(C) is finite; for H not commutative it is finite
  only up to conjugation. His qualification is right.
- The effectivity cone (re-proved): a representation is effective (all Frobenius eigenvalues integral at p) iff all
  its weights pair non-negatively with every conjugate of every u(s')_C ∘ i(s'), the slope cocharacters; so the cone
  is the dual of the cone generated by these cocharacters. Rays need the cocharacters, not their restrictions v(s') to
  mu_2 (the reading "v" is doubtful in the Pro text).
- The torsor statements of 15:183 follow from 15:119 (real fibre functors form a torsor under H^1(R, U); the choice of
  i picks one): agrees, with the integrality caveat of §C (i|mu_2 needs odd denominators).

**Open (his).** The "condition non tautologique" is not stated as a theorem; "conjectures de Tate magnifiées" and the
recovery of effectivity from the u(s') are conjectural. Known in substance as the motivic Sato-Tate frame (Serre,
Propriétés conjecturales des groupes de Galois motiviques et des représentations l-adiques, in Motives, Proc. Symp.
Pure Math. 55 (1994), §13; locator unverified).

### H. 15:189-205 (his pages): "Théorie de Galois des Motifs. Généralités" and "Foncteurs fibres motiviques et groupe fondamental motivique" (SA06-15)

- **15:191.** X connected. 1°) X_red of characteristic p > 0: the fundamental pro-torsor (T_alpha) has no sections in
  general; one has (i) l-adic points xi_l^(alpha) in T_alpha(Z_l), l != p, "provenant sans doute" from points over the
  henselization Z̃_(l); (ii) a crystalline point xi_p^(alpha) in T_alpha(W_p(k)) for k perfect over X, with the
  supplementary structure F and V, semilinear (box), "DeRham-Hodge" (margin: work in the derived category, keep the
  Hodge-de Rham filtration); (iii) its reduction in T_alpha(k). Even for X = Spec F_q there are non-trivial
  obstructions in H^2(Q, G). With fibre functors inducing the canonical one on effective motives of weight 0, the
  points of T_alpha(Z_l) are "sans doute" unique up to isomorphism (Lang), likewise those of T_alpha(W_p(k)) for k
  finite, more generally k perfect of dimension <= 1 (?); in general T_alpha(k) has several classes, but perhaps
  T_infinity(k) = lim T_alpha(k) has one, the de Rham-Hodge one. Margin: relation with the "problème galoisien ??",
  "cf Manin".
- **15:193.** The xi_l depend on a geometric point up to non-unique isomorphism (pi_1(X) acts); the xi_p^alpha depend
  on a point with values in a perfect field, with no isomorphisms between different k-points ("c'est la 'partie
  continue' du H^1 préc. qui va faire des ennuis"); for k algebraically closed they are conjugate under automorphisms
  of k; pi_1(X) does not act on xi_p, the automorphisms of k over k(x) act semilinearly; F, V with FV = p. Notation:
  xi_(x̄,l), xi_(x,l), xi_(x,p), xi^0_(x,p).
- **15:195.** 2°) X dominating Spec Z: (i) xi_l in T(Z_l) for all l; (ii) xi_(x,p), xi^0_(x,p) at points of
  characteristic p, and the "connexion" between xi_(y,p) and xi_(x,p) (x) W(k), "en général pas isomorphes, sans
  doute"; (iii) at points with values in a field of characteristic 0, xi_(x,infinity) in T_alpha(k) by Hodge-de Rham,
  with two filtrations (margin: the Hodge filtration, graded pieces H^q(X, Omega^p) (reading below), proper to the de
  Rham functor and not coming from a filtration of the motive; and the arithmetic one, matching the canonical
  filtration of motives, trivial for simple motives).
- **15:197-199.** No pi_1-action on xi_(x,infinity); automorphisms of the coefficient field act semilinearly; for
  h = Q a point xi_(x,infinity) in T_alpha(Q), a trivialization of T_Q; two need not be isomorphic; no canonical, and
  perhaps no, isomorphism between xi_(x,infinity) (x) Q_l and xi_(x̄,l) (x) Q_l, "Ainsi, tout pt rat/Q définit une
  classe de coh dans H^2(Q_l, G_l^(0(alpha)))" (ink 2, see below); margin: "en fait, ils sont déjà non isom sur les
  Motifs de poids et niveau 0"; in general replace Q_l by Q_l (x) k, "particulièrement intéressant" for k a number
  field. (iv) a complex point x gives xi_(x,Z) in T_alpha(Z) (an integral lattice), with xi_(x,Z) (x) Z_l = xi_(x,l)
  and xi_(x,Z) (x) C = xi_(x,infinity), and an "involutive" isomorphism xi_(x,Z) = xi_(tau x,Z).
- **15:201.** For a real place a: the involution tau on xi_(a,Z) (not to be confused with the semilinear endomorphism of
  xi_(ā,infinity)); invariants xi_(a,infinity) in T_alpha(R), xi_(ā,infinity) in T_alpha(C), xi_(ā,Z) in T_alpha(Z).
- **15:203.** The Hodge decomposition (transcendental) is determined by the semilinear involution tau' from
  xi_(x,infinity) = xi_(x,R) (x) C, xi_(x,R) = xi_(x,Z) (x) R; for k(a) real a second one tau'' from the real de Rham
  structure; "tau = tau' tau'' = tau'' tau'" (margin "à vérifier"); tau on xi_(a,l) is the Frobenius at the real
  place, an element of pi_1(X) (margin "à vérifier").
- **15:205.** f_infinity acts on xi_(x,Z), extended linearly to tau = f_infinity. N.B.: the Hodge conjecture interprets
  the arithmetic (motivic, level) filtration in terms of the Hodge filtration and f_infinity: "La partie de niveau
  <= rho dans xi_(x,Q)(F) n'est autre que xi_(x,Q)(F) ∩ xi_(x,infinity)(F)^(rho) ∩ f_infinity xi_(x,infinity)(F)^(rho)";
  the last subspace is motivic, the two Hodge terms are not. (Continues on 207, outside this stretch.)

**Checked** (P3-38 to P3-46):
- 15:191 "no sections" (targeted check): over F_q the motivic gerbe has no Q-valued fibre functor (the supersingular
  quaternion algebra, ramified at p and infinity, cannot act on a 2-dimensional Q-space): agrees (Milne, Motives over
  finite fields, 1994; Serre's argument, 15:11, SA05-18).
- Uniqueness (re-proved, conditionally): if G_alpha has a smooth connected model over Z_l (resp. W(k)), Hensel's lemma
  gives H^1(Z_l, 𝒢) = H^1(F_l, 𝒢) = 1 by Lang, and H^1(W(k), 𝒢) = H^1(k, 𝒢_k) = 1 for k perfect of cohomological
  dimension <= 1 by Steinberg's theorem (H^1(k, G) = 0 for connected linear G; Steinberg, Publ. Math. IHÉS 25 (1965),
  Th. 1.9; locator unverified), the paper whose typescript is reused on 15:95, 97, 99, 109 (hunch c15-H2). His
  "sans doute" is the model hypothesis.
- 15:197 margin (re-proved): on Artin motives the torsor of isomorphisms between the de Rham fibre functor (x) Q_l and
  the l-adic one is the Gal(Q̄/Q)-torsor Spec(Q̄ (x) Q_l), which has no Q_l-point: they are already non-isomorphic in
  weight and level 0. Agrees.
- **15:197, "H^2(Q_l, ...)": reading decided on the scan** (250 dpi, medium confidence): the exponent is a 2. Two
  fibre functors over Q_l differ by a torsor under the automorphism group of one of them: the class lies in H^1, not
  H^2 (Pro note A04 leaves the reading open). His slip.
- 15:199 (targeted check): the Betti lattice and the comparisons xi_Z (x) Z_l = xi_l (Artin), xi_Z (x) C = xi_infinity
  (de Rham), and complex conjugation of the point: agrees (SGA 4 XI and XVI; Deligne, Valeurs de fonctions L et
  périodes d'intégrales, Proc. Symp. Pure Math. 33 (1979), §§0-1; locators unverified).
- 15:203 (independent re-proof of his "à vérifier"): F_infinity is defined on the Betti Z-lattice, so it commutes with
  tau' (conjugation of coefficients); the comparison identifies F_infinity (x) c with 1 (x) c on the real de Rham side,
  i.e. tau'' = F_infinity tau'; hence tau' tau'' = tau'' tau' = F_infinity. Agrees (Pro note A07 says commutativity
  does not follow from semilinearity alone: it follows from F_infinity being defined over Z). The Hodge decomposition
  is H^(p,q) = F^p ∩ tau'(F^q): agrees. tau on xi_(a,l) is the real Frobenius in pi_1(X) by compatibility of the Artin
  comparison with complex conjugation: agrees (same sources).
- **15:195 margin: reading decided on the scan** (medium confidence): the graded pieces read "H^q(X, Omega^p)" (the
  letter after X is a looped capital with superscript p; there is no Q), and the second filtration is
  "(arithmétique)", matching 15:205's "filtration arithmétique"; the Pro text has "H^i(X, Q_l(?))" and
  "caractéristique(?)". The mathematics needs H^q(X, Omega^p).
- **15:205, the level formula: refuted as stated, with the refined statement** (reading confirmed on the scan). With
  f_infinity F^rho = complex conjugate of F^rho (F^rho is defined over R), the formula says: the level <= rho part of
  the Betti realization is H_Q ∩ F^rho ∩ F̄^rho = H_Q ∩ F^rho, the form of Hodge's general conjecture that he
  himself refuted in 1969 (Hodge's general conjecture is false for trivial reasons, Topology 8 (1969), 299-303;
  locator unverified). A counterexample computed here: E = C/(Z + Z tau) with tau a non-real cubic irrationality
  (so E has no CM), F = h^1(E)^(x)3, weight 3, rho = 1 (types (2,1), (1,2)). With a symplectic basis alpha, beta and
  omega = alpha + tau beta, a rational vector v lies in F^1 iff <v, omega^(x)3> = 0; on the tensor basis the values are
  +-tau^k (k = 0, ..., 3), whose Q-span is Q(tau), of dimension 3. So H_Q ∩ F^1 has dimension 8 - 3 = 5, odd, hence it
  is not a Hodge substructure of odd weight and cannot come from a submotive. The level <= 1 part is the
  H^1(E)(-1)-isotypic part, of dimension 4 (MT = GL_2). Refined statement (his 1969 correction, the generalized Hodge
  conjecture, open): the level <= rho part is the largest Q-sub-Hodge structure contained in the Hodge piece.

**Wrong** (CORRECTIONS): 173 margin "n != 0" (n != 1); 179 "(1.1.)" and "corollaire 3.4" (Pro readings); 195 margin
(Pro reading); 197 "H^2" (H^1); 205 the level formula.

**Open (his).** The uniqueness of T_infinity(k) (191); the "problème galoisien" with Manin (191); the comparison of
xi_(y,p) with xi_(x,p) (x) W(k) (195); the class of a rational point over Q_l (x) k for k a number field (199).
Status: known in substance as the realizations of motives with their comparison isomorphisms and integral structures
(Deligne 1979; Fontaine-Messing and the crystalline comparison; Oda, Ann. Sci. ÉNS 2 (1969), Cor. 5.11, for H^1, as
cited in the Pro notes); his: the organisation as points of one fundamental pro-torsor at every place, the
non-isomorphism statements, and the "partie continue" warning.

### I. Reused leaves in 15:170-206 (SA06-11; identified, not studied)

- 15:171, 192, 194, 196, 198, 200, 202, 204, 206: Bourbaki "Tribu n° 59" sheets: "Systèmes de racines (20)",
  "Algèbres de Lie semi-simples (9) to (3)" and "Décisions sur les algèbres de Lie semi-simples (n° 400)", filed in
  reverse page order.
- 15:184, 186, 188: the Moishezon projectivity typescript again (pp. 70-73; margins cite pp. 202, 208).
- 15:181: a private administrative document (redacted), not mathematics.

### Hunches (part 3; "(mine)": none is a statement of the pages)

**c15-H1. The privileged polarizations of 15:121-123 and the real points of 15:183 need the slope cocharacter on a
cover.** Grounds: his caveat (15:121) that lambda -> v_𝔭(lambda)/v_𝔭(q) is not integral; i|mu_2 is defined exactly
when the denominators are odd; even denominators occur with even degrees (q = 25, lambda = 15 + 20i, slope 3/2). The
natural repair is the Weil-number protorus with its slope cocharacter defined on the protorus with character group Q,
as in the pseudo-motivic Galois group of Langlands-Rapoport (Shimuravarietäten und Gerben, J. reine angew. Math. 378
(1987)) and Milne 1994 (locators unverified); the parity of the slope denominators then decides whether a privileged
real point exists. Pages: 15:121-123, 183-185. Links: SA06-9, SA06-10, SA05-18.

**c15-H2. The reused Steinberg leaves were in his hands for a reason.** Grounds: 15:95 is Steinberg's Theorem 1.10 on
perfect fields of dimension <= 1, and 15:191 invokes exactly "k parfait de dim <= 1 (?)" for the uniqueness of the
crystalline points. Steinberg's paper is of 1965, which bounds 15:191 from below. Pages: 15:95, 97, 99, 109, 191.

**c15-H3. 15:195-205 predate his 1969 note, and that note repairs this page.** Grounds: the level formula of 15:205 is
the naive general Hodge conjecture (refuted above with a cubic tau, and by him in Topology 8 (1969)); together with
c15-H2 this places 15:191-205 between 1965 and 1968. Links: SA06-4 (the standard conjectures, the letter to Serre of
27.8.1965 in part 1), SA06-2.

**c15-H4. The "cohomologie absolue des motifs de Tate" is the integral Weil-étale cohomology.** Grounds: 15:173-178
give ℍ^0(F_q, Z) = ℍ^1(F_q, Z) = Z (étale cohomology gives Z and 0), ℍ^1(F_q, Z(n)) = Z/(q^n - 1) (Quillen's
K-groups), H^3(Spec Z, Q(1)) = Q and H^3(Spec Z, Z(1)) = Z: F_q behaves as a circle and Spec Z as a closed
3-manifold with a fundamental class, the picture of Artin-Verdier duality (1964) and of Lichtenbaum's Weil-étale
cohomology (Compositio Math. 141 (2005) for varieties over finite fields; Ann. of Math. 170 (2009) for number rings;
locators unverified). His agenda item 8, "Topologie à mettre sur Z", points the same way. Pages: 15:170, 173-178.
Links: SA06-14, SA06-16.

**c15-H5. "La partie continue du H^1" (15:193) is the moduli of F-crystals.** Grounds: isocrystals with G-structure
over an algebraically closed field are discrete (Dieudonné-Manin, his "cf Manin"; Kottwitz's B(G), Compositio
Math. 56 (1985)), while integral F-crystals vary in continuous families (Rapoport-Zink, Period spaces for p-divisible
groups, 1996); that is the obstruction he expects to the isomorphism of crystalline points at different k-points.
Links: SA15 (crystals), SA06-8 (the crystalline side of the Deuring gerbe, 15:42-56).

**c15-H6. 15:183-187 is the motivic Sato-Tate frame, with an effectivity criterion.** Grounds: Frobenius classes at
closed points placed in the compact form G^00 twisted by xi(s'), and the "condition non tautologique" on polarizations
(Serre 1994, §13; Serre, Lectures on N_X(p), 2012, ch. 8; locators unverified). His further claim, that the u(s')
recover effectivity (a motive is effective iff its Frobenius eigenvalues are integral at every closed point), is a
"conjecture de Tate magnifiée" that I know no reference for. Links: SA06-2 (the character cone of cote 14).

**c15-H7. The obstruction to lifting Frobenius to the norm-one torus is class-group theoretic.** Grounds: P3-26: up
to a 2-group, coker(M_0(q) -> (Z^P)^-) is the subgroup of Cl(L) generated by the minus-divisors at p. This is the
same group that governs which Shimura-Taniyama divisors are principal; it bears on the strong conjecture of 15:100
without powers (STUDY H4, RP-SA06-2). Pages: 15:110-114, 96-100.

### Dependencies (part 3)

| Piece | Uses | Page that shows it |
|---|---|---|
| SA06-9 (15:94) | SA06-9 (15:131-132, STUDY §1) | the Cor. needs the equivalence (a) <=> (c) of 15:131 |
| SA06-9 (15:110-112) | SA06-9 (15:96, STUDY §1) | finite index of M_0(q) in (Z^P)^- (the Proposition of 15:96) |
| SA06-9 (15:88) | SA06-9 (15:84-86, STUDY §2) | "ce qui précède prouve que (Ker epsilon)^0 est un tore compact" |
| SA06-10 (15:117) | SA06-2 (14:2) | margin "On n'utilise que les éléments de structure 1, 2, 3" |
| SA06-10 (15:117-119) | SA05-18 (15:11) | Prop. 2 is Serre's argument (no real fibre functor when epsilon is a square) |
| SA06-10 (15:119) | SA06-8 (15:52) | the rank-2 degree-1 object generating an R-twisted subcategory (the quaternionic line) |
| SA06-10 (15:121-123) | SA06-9 (15:110) | i from the valuation at 𝔭 on M(q) in L |
| SA06-15 (15:183-187) | SA06-10 (15:117-123) | M^pair, real fibre functors, i "de type préférentiel" |
| SA06-15 (15:187) | SA06-2 (cote 14) | the effectivity cone |
| SA06-15 (15:191-193) | SA15 | F, V with FV = p on the crystalline points |
| SA06-15 (15:191) | SA06-11 (15:95, Steinberg) | "k parfait de dim <= 1" |
| SA06-15 (15:205) | SA06-4 | the Hodge conjecture as a statement about the level filtration |
| SA06-14 (15:170) | SA06-9, -10, -15, -16, SA06-4 | items 3, 4, 8, 9 |
| SA06-16 (15:172-179) | nothing in SA06 | known étale cohomology (Artin-Verdier, Brauer I-II) |

### Deliverable state (part 3)

| Scans | Passes | Open readings on his pages (unsure / illegible marks) | Decided here on the scan | Ready? |
|---|---|---|---|---|
| 15:87-95 | Pro MPL_15_087-138 + notes; Codex K15-03 | 91 / 3 on 4 pages | none needed | after collation with K15-03 |
| 15:109-126, 138 | Pro MPL_15_087-138 + notes; Codex K15-04, K15-05 | 115 / 0 on 8 pages | 110 Z_l; 112 f_0; 119 inj_1; 121 no "+"; caveat box (Codex reading) | after collation; the caveat box should take the Codex reading |
| 15:170-171, 179-194 | Pro MPL_15_170-194r + notes; Codex K15-06, K15-07, B15-01 | 140 / 0 on 11 pages | 179 "(5.1.)", "corollaire 5.4" | after collation (the Pro text has the two misreadings on 179) |
| 15:172-178 | Pro checkpoint only (MPL_15_139-194_checkpoint_01: pages, doubts, inventory, no notes); Codex K15-06 | 42 / 0 on 7 pages | none | needs the final Pro pass or a second pass; the checkpoint text reads well |
| 15:195-206 | Pro MPL_15_195-228+18_002-017 (chat A, with chat B witness) + notes; Codex K15-08 | 76 / 4 on 6 pages | 195 margin; 197 "H^2"; 205 formula confirmed | after collation |

Pages read in part 3: his pages 88, 90, 92, 94, 110, 112, 114, 117, 119, 121, 123, 125, 170, 172-180, 182, 183, 185,
187, 189-191, 193, 195, 197, 199, 201, 203, 205 (36, including covers and the cancelled 175); reused leaves
identified: 87, 89, 91, 93, 95, 109, 111, 113, 115, 118, 120, 122, 124, 126, 138, 171, 184, 186, 188, 192, 194, 196,
198, 200, 202, 204, 206 (27); 181 private, 116 blank.

### Counts (part 3)

63 pages read (36 of his, including covers and the cancelled 175; 27 reused leaves identified in one line each);
48 check events; 25 corrections; 7 hunches (c15-H1 to c15-H7). Claude Opus 5.5 at effort max, c14_c15rest,
19 Nov 2026.
