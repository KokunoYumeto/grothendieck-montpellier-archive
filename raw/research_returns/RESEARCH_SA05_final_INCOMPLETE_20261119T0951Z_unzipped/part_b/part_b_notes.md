# Part B research notes

Status: **INCOMPLETE research checkpoint, 2026-11-19, updated at approximately 04:45 UTC.**
The main section is `../sections/part_b.tex`. Statements and task statuses are
in `part_b_results.csv` and `part_b_ITEM_STATUS.tsv`; check and source records
are in `part_b_CHECK_EVENTS.tsv` and `part_b_LITERATURE_CHECK.tsv`.

## Conventions

Q(1) has weight -2. A rational l-adic Tate twist is used only on a scheme on which l is invertible, unless a specified syntomic or flat replacement is named. Weil-etale, motivic, ordinary etale, compactified Artin-Verdier, and compact-support groups are distinct throughout.

## Initial source checks (2026-11-19)

Read manuscript transcriptions 12:60,62-65,67,71,73-80,82,84 and 15:173-174,177-178, plus relevant proof summaries of R5/R6. Root subsequently inspected the manuscript image at12:79 and confirmed its explicit regular-base hypothesis. Other paleographic assertions are limited to the source actually inspected.

Geisser (2004), arXiv:math/0404425, Theorem 1.2, explicitly requires the conjunction of Tate surjectivity, semisimplicity at 1, and Beilinson rational=numerical equivalence for a full comparison theorem for Weil-etale motivic complexes. The prompt lists only the first two. This is a missing hypothesis, not a known counterexample to Beilinson.

Flach-Morin (2018), author PDF flach-morin-169.pdf, opened. Its Artin-Verdier compactified, compact-support, and Weil-Arakelov complexes must be separated before interpreting 15:173.

## Proved and refuted components

### B.1: finite fields

The finite-point calculation is complete, including negative twists in the etale convention Z(n)=Q/Z'(n)[-1], and the restriction factor e_q maps to m e_qm. The natural direct limit of the rational degree-one lines over finite extensions is Q. Therefore the combination of this continuity with the higher-cohomology vanishing asserted over the algebraic closure is false already at the point. This is an actual refutation, distinct from the following missing-hypothesis issue.

Geisser's Theorem 8.4 uses his full Conjecture 8.3: Tate cycle classes, semisimplicity at one, and rational=numerical equivalence. The prompt names only the first two. The assertion that those two imply the third is **not refuted here**; it is the exact remaining gate for identifying actual Weil-etale motivic cohomology with the asserted l-adic groups. An artificial numerical-category cohomology would change the question. The unconditional all-twist results for dimension at most one and the abelian-divisor case are checked using Geisser 9.3/9.5 and Lichtenbaum 6.1.

Limited uniqueness is proved only for normalized additive graded functors on a fixed semisimple pure numerical category. No uniqueness of a topology, integral theory, triangulated enhancement, or six operations follows from that argument. The arbitrary-theory uniqueness portion remains separate.

### B.2: number rings

The full rational continuous cohomology table is expressed with exact defects delta_0 (Leopoldt) and delta_n for n<0 (the strict positive-twist p-adic regulator kernel, equivalently the relevant Schneider vanishing). These defects are not silently set to zero. Positive twists use Borel/Soule; n=1 uses Kummer and local invariant sums. Rational coefficients remove real two-torsion, but the integral duality later retains it.

Bloch-Kato Definition 5.1 imposes f at places in the arithmetic open, and g at omitted places. In particular an omitted l-adic place has g, not automatically f. With that definition the degree-one common rational spaces are unconditional: S-units in twist one, the relevant rational K eigenspace in twists >=2, and zero in twists <=0. The latter zero statement must not be confused with the full-cohomology Schneider defect. Higher H_f^i require a specified Selmer complex. The paper specifies one for the proper ring and a rational localization extension for the open ring; a subgroup condition in degree one is insufficient to define the whole higher complex.

The all-degree table is now explicit in cor:B-Hf-all-degrees. Proper-ring H_f^2 is the dual complementary H_f^1, and H_f^3 is dual complementary H^0. At removed places, twist one retains both local valuation H^1 and local-invariant H^2, giving ker(Q^S→Q) and coker(Q^S→Q). Other twists do not change. Root independently audited all degrees. Fontaine1992 §§4.4–4.5 was opened and its formulas rendered: the source supplies two exact degree-two sequences with the same ends, giving a vector-space isomorphism after splittings, not automatically a canonical derived self-duality. The text now states that choice explicitly. No Leopoldt/Schneider vanishing is needed for any finite-condition Tate group.

The corrected arbitrary-pure-motive comparison is stated as the model-image Bloch-Kato conjecture and Fontaine1992 §§6.5–6.7 f-admissibility (prescribed finite-dimensional motivic H_f^0/H_f^1 and the realization isomorphisms c0/c1 for every ell), not proved. The later full Fontaine–Perrin-Riou paper remains unobtained. Scholbach's Remark 6.2 explicitly excludes the crystalline conditions. His Theorems 6.8/6.11/6.13 use the assumed mixed-motive t-structure and weight formalism. Ordinary motivic cohomology in that framework has neither the finite-field degree-one unit class nor the Weil-etale Spec Z degree-three fundamental class. The attached special-L-value paper also retains its numerical=rational and Beilinson-Parshin gates. The attached Adrien Morin constructible-sheaf paper treats n<=0 for constructible integral sheaves (Theorem A and main theorem), not all positive motivic twists.

### B.3: arithmetic abelian schemes

Gonzalez-Aviles and Tan's unconditional Main Theorem gives the right pro-Selmer term. Restricting support to removed places gives an exact sequence ending in that dual pro-Selmer term, with **no terminal surjectivity assertion**. The exact corank is d+s-t, where d=sum_{v|l}[K_v:Q_l]dim A, s=corank Sha_l, and t is the rank of the local image of the pro-Selmer group. Even if Sha_l is finite, t is the local closure rank of Mordell-Weil, not its abstract rank.

The algebraic two-descent computation certifies the requested X0(11) model y^2+y=x^3-x^2-10x-20 has rank zero, torsion Z/5, and no 2-Selmer group. Its good model over Z[1/11l] has H^1(S,E)[l∞] infinite for every l by the global Euler characteristic; at l=2 the exact corank is one. No analytic rank or BSD is used. The curve y^2+y=x^3+x^2-2x has certified rank two and zero Sha[2]; on Z[1/(2*389)] its d=1,s=0,t=1 gives corank zero, whereas the proposed d-r+s would be negative.

Restoring vanishing of the local torsor classes above l gives a finite kernel exactly when Sha_l is finite. Kummer then proves equivalence with A(K) tensor Q_l = H_f^1(K,V_l A). This is an equivalence with a conjectural finiteness assertion, not a proof of general Sha finiteness.

The arithmetic Brauer question is refuted as well: S=Spec Z[1/22], X=E_S. The section splits relative Pic as E x Z, proper base change and Kummer kill the 2-primary relative R^2 Gm, and Milne II2.1/Remark2.2(a) gives H^3(S,Gm)=0. The quotient Br(X)/Br(S) has 2-primary corank one. The proof explicitly uses that all Brauer groups and H^1(S,E) are torsion before taking primary parts, so no non-2-primary extension is discarded.

### B.3: finite-field equivalences over every finite-type base

The former Hochschild–Serre gap is now repaired, without assuming full Frobenius semisimplicity or general Tate. The key lemma splits the algebraic divisor image in H²(Ybar,Q_l(1)) for every smooth separated finite-type Y/Fq. In the smooth projective case use the nondegenerate divisor intersection form. For a smooth open, the kernel of restriction is generated by boundary divisors and remains inside the algebraic subspace, while the quotient beyond weight zero has weights at least one. Disjoint spectra give an actual Galois splitting. A proper generically finite smooth alteration then descends a retraction by pullback, the retraction upstairs, and trace divided by the degree. Agent C independently checked every step and the cofiniteness qualification.

For an abelian scheme A/S, apply this to its total dual B=A^t. The eigenvalue a of multiplication [a] on H²(Bbar,Q_l(1)) identifies H¹(Sbar,V_lA); the same eigenspace of divisor classes is the geometric Kummer image of A(Sbar)^completion_l. The relative Picard section obstruction is split by the zero section. Thus the geometric Kummer sequence splits as a Galois representation. The arithmetic/geometric H¹(A) comparison has finite kernel and cokernel, and all the manuscript's regular-base finiteness/Kummer equivalences follow. The constant case is unconditional by Tate's Hom theorem. General nonconstant finiteness is still the stated Tate/BSD gate; proving the equivalence is not an affirmative answer to finiteness.

The relative-curve step is now proved **without a section**, still over a regular separated finite-type base. A separable closed point of the generic fibre gives a Cartier closure and a line bundle L of positive fibre degree d. Deligne1968 Proposition2.4/(2.5) splits rational Leray. The relative Picard degree sequence has d-torsion boundary, and the Brauer obstruction to lifting a relative line bundle is killed by d via restriction/corestriction and Br(S) injection into Br(K). After removing the base Picard part and degree class, the middle Chern class image is exactly the Kummer image of J(S). Therefore V_l(Br(Y)/imBr(S)) = V_lH¹(S,J). Cofiniteness turns this into the required finiteness equivalence. With a section the l-primary edge sequence is integral. Agent C independently audited the full proof and confirmed it.

A source error is explicitly repaired: Keller2016 Lemma2.17 claims the closure of a generic-fibre closed point is finite over the base. On S=A² over a finite field, in P¹[u:v]×S, the generic point [x:y] closes to uy−vx=0, the blowup of the origin. Its fibre at the origin is P¹. The corrected argument needs the Cartier line bundle and constant degree, not a finite multisection. No assertion using that false closure claim is carried forward.

For the precise nonzero degree-two assertion at 12:78, take C/F2 given by y²+y=x³−x²−10x−20, A=C×C→C, and l=3. Exact point counting gives #C(F2)=5, Frobenius t²+2t+2, and centralizer dimension2. Kummer and Hochschild–Serre identify V3H²(C,A) with End_F2(C)⊗Q3, of dimension2. The dual Tate module formula requires its twist; an omitted twist would give the wrong comparison.

Root's all-base argument now removes the singular, nonreduced, and nonseparated scope gate for the finite-field Kummer chain. A finite affine cover followed by alterations gives a jointly surjective smooth separated V→S_red. Sections inject modulo torsion by the closed equalizer argument. Lang–Neron gives a finite free quotient with finite Galois action; ell torsion embeds in finitely many Pruefer groups, so rational completion agrees with tensoring sections. Average a projection N_V→N_S and compose with the smooth-base Kummer retraction. Nilpotent thickening errors are bounded p-primary and disappear for ell different fromp. Cofiniteness, arithmetic norms, and the weight-minus-one H0 term give finite kernel/cokernel of the arithmetic/geometric torsor comparison. I independently checked the complete written proof and opened Conrad2.1/7.1 and deJong4.1/4.2. It is included as sections/b3_singular.tex.

An optional singular-base example shows why the relative-curve degree argument itself cannot simply drop regularity: glue two P2 overF2 along E:y2z+yz2+x3+x2z=0, and glue E×P2 along E×E by translation by id_E. The boundary of id_E has infinite order in H1(S,E×S), and Pic^d of the genus-one torsor has class ±d alpha; hence every global line bundle has degree0. Stacks0B7M,0CYY(4),0H74 prove scheme existence, smoothness, and local triviality; agentD audited the full argument. This is not a claim of an infinite Brauer quotient. Its finite cubic and ring-algebra checks are in singular_genus_one_checks.py/.txt. The July2026 singular-NS preprint arXiv2607.11777 was found but not obtained and is not used.

### B.4: all rational twists, integral structure, and exact gate

The complete rational FM table is proved: nonzero only at (n,i)=(0,0),(1,3), positive odd n>=3 in degree one, and negative even n<=-2 in degree two. The degree-three line is the dual completion of motivic degree zero; ordinary motivic Spec Z cohomology in twist one is entirely zero. Integral generators are supplied by the audited effective construction below, with its literal cycle/boundary output convention.

Both manuscript integral tables miss a Z/2: units in twist one degree one, and their dual in twist zero degree three. FM Section5.8.3 gives an all-degree structural table. The paper writes explicit root-of-unity torsion w_n and the real-place two-torsion terms; C_n=H_et^2(Spec Z,Z(n)) is now determined by a terminating finite presentation below, not left as an unnamed arithmetic input.

For every odd p, Kummer descent to Q(zeta_p) proves H²(Z[1/p],Z_p(m))/p = A[1−m]/p. Therefore all positive odd-twist p-primary C_m vanish iff the p-instance of Vandiver holds. The current February2026 partial-regularity paper has been opened; it proves a density-one restricted-range result, not full Vandiver. **The p=37 check is now certified:** PARI2.19.1 returns class group [1,[]] for the degree18 maximal real cyclotomic subfield and bnfcertify(B,1)=1; the documentation proves the actual class group is a quotient of the computed group, which suffices when that group is trivial. The computation also gives v37(B32/32)=1. The longer full-unit-certification run was interrupted and is retained as an unused partial output.

The finite groups C_m are no longer left as an unnamed arithmetic input. Root's `sections/b4_algorithm.tex` gives a terminating all-prime presentation for their odd-primary parts: Soulé2003 Theorem3 supplies an explicit finite prime bound; a local different bound and a Minkowski primitive-element argument bound all Galois extensions needed for crossed cocycles; a finite congruence matrix computes H¹_c(Z[1/l],Z/l^r(1−m)); Artin–Verdier duality gives C_m/l^r; equality of successive orders detects the full exponent and eventually occurs. I independently audited the bound, finite presentation, local trivializations, duality, and termination. The section is included in Part B. This is an explicit algorithm, not an assertion of uniform vanishing or practical feasibility.

The 2-primary groups and their generators are completely specified: C_m[2∞]=Z/2 for positive even m and zero for odd m>=3. For even m the generator is the Bockstein of the order-two inclusion of the Kummer class of −1. Rognes–Weibel Lemma5.5 and Propositions6.12–6.13 give this directly for etale cohomology; localization at2 contributes only odd-order finite-field groups. The extra real-place terms in the Weil-etale table remain separate from C_m.

The primitive free-generator construction in `sections/b4_generators.tex` is included and passed independent root and PartD audits. Enumerate actual rational admissible real-proper higher Chow correction cycles satisfying Kerr–Yang Theorem3.3, whose existence precedes their explicit formulas. Clear their literal denominators by D_m and multiply by (m−1)!; the regulator is d_m(2^{m−1}−1)zeta(m). FM equation(88), Proposition5.35, and the functional equation give the exact index D_m(2^{m−1}−1)|C_m|. Enumerate an integral cycle gamma and chain eta with boundary eta=2(h gamma−xi). Existence follows from that index and the order-two torsion; any solution is primitive modulo torsion. Admissibility, faces, and boundary identities use finite polynomial ideal calculations; the real-properness condition uses the precise Kerr–Li footnote4 finite family and CAD. The exact height enumeration is specified. Geisser2004 Dedekind Theorem1.2(2)/3.2 and Voevodsky2011 Theorems6.16/6.18 were opened directly to certify localization and the integral low-degree comparison.

### New source error: the explicit Kerr–Yang cycle formula cannot be accepted

Kerr–Li2020, published p.548 and footnote10, corrects the first weight4 construction of Kerr–Yang2018: its last component W2 is cubically degenerate, so the proposed total cycle is not closed. The all-weight lemma now proves that every displayed uniform Section4D W2 term is degenerate: every coordinate other than the final v−1 (subtraction, not inverse) is homogeneous of degree zero in (u,v), and u=s v makes the last coordinate an independent cube factor. We do not use Theorem4.2 as an integral closed-cycle certificate. No full all-weight boundary formula is claimed; the precise proved defect is separated from that stronger assertion.

The normalization must also be checked independently: Theorem3.8 gives Li_m(−1)=−(1−2^{1−m})zeta(m), and naive use of the later printed epsilon coefficients can produce a nonintegral putative index (5/4 in the diagnostic weight5 calculation with C5=1). That diagnostic alone is not a disproof of an integral cycle assertion, because its actual coefficient denominators and normalization must be accounted for. The repaired proof therefore searches the actual correction chain, clears its literal denominators, and independently matches the Beilinson lattice; it does not use the later epsilon formulas. Earlier provisional claims accepting all explicit Theorem4.2 chains were superseded and are not carried into a proof.

Localization away from twist one is proved within the same rational absolute theory. Zeta orders require the Weil-Arakelov compact-support archimedean contribution: negative even twists have real lines in degrees one and two, twist one in degrees two and three, and all other twists have zero real groups. The weighted Euler expression then gives all integer orders. The bare rational Weil-etale ranks would give a wrong value at twist three.

### B.5: finite theorem and rational scope

Geisser-Schmidt Theorem4.6, Lemma3.7, and Theorem3.9 give finite duality for every regular finite-type Z-scheme with the exact degree 2d+1 and etale motivic Z/m(d). Only when m is invertible may this be replaced by mu_m^{tensor d}. Tate-modified support at real places is necessary even for algebraic properness. The p-primary smooth-curve check uses log de Rham-Witt and Milne II7.11; etale mu_p is not an acceptable replacement.

The literal nonseparated scope is now also handled, with its compact-support convention explicit. Use a finite affine cover and the alternating Cech chain totalization of the usual Tate-modified compact-support complexes on the separated intersections. Functorial cochain models make the diagrams and refinement maps precise. Refinement and ordinary Mayer–Vietoris prove cover independence. The exact j! simplex resolution computes the dual Ext by Cech cochains, and the local trace maps glue to the required shift2d+1. PartD independently read both the proof and GS3.5/Cor3.6/Lemma3.7/4.6 and found no gap. No nonseparated compactification is assumed.

Rational duality is proved for every Tate twist on compactified number rings, their specified localization/compact-support extensions, and smooth projective finite-field curves. Finite etale Galois descent now extends it to every finite-monodromy Artin–Tate coefficient. A precise conditional proposition identifies the number-ring gate for a general prescribed motivic dual pair: f-admissibility c0/c1 for M and M dual twist1 is necessary and sufficient for the specified graded rational dual completion and all Selmer comparisons. This does not construct a six-operation motivic category or prove those realization conjectures. The arbitrary-pure-motive assertion still contains Sha finiteness for abelian motives.

## Computations and reproducibility

`code/x011.gp` and `output/x011.txt` contain the two algebraic descents, models, discriminants, conductors, torsion groups, and small-prime point counts. PARI2.19.1 was built from the official release; build script and log are retained. `code/vandiver37_quotient.gp` and `output/vandiver37_quotient.txt` contain the completed unconditional class-group certificate (about47ms). `code/vandiver37.gp` and its output retain the unused interrupted full-unit certification. `code/finite_field_checks.py` and its output contain the F2 point count, centralizer computation, and an abstract Jordan obstruction model, explicitly not claimed to be geometric. No stochastic analytic-rank estimate is used as a proof.

`download_primary_sources.py` records URLs, byte counts, and SHA256 values in `output/download_primary_sources.json` and the source directory's download log. Primary PDFs are kept under `primary_sources/part_b`. Exact source opening/failed retrieval status is in the literature TSV. Fontaine-Perrin-Riou and the original Schneider article are not falsely marked obtained; the original Bloch-Kato definition and Nickel's explicit formulation provide the sources actually used.

## Remaining gates and approaches tried

1. B.1: tried direct l-adic comparison and numerical-category replacement; the first requires Beilinson, the second changes theory. All low-dimensional cases checked; the general implication remains.
2. B.2: separated full Galois cohomology, finite local subgroup, and dual Selmer completion; regulator defects are now exact. General pure-motive comparison remains conjectural.
3. B.3: arithmetic universal statements refuted with explicit curves. The finite-field chain is proved for every finite-type base. The section-free relative-curve equivalence is proved at each prime different from the characteristic in the regular scope actually written at12:79. The **literal unqualified whole-Brauer quotient assertion is now refuted in characteristic2** by the explicit constant supersingular example recorded below. Actual general prime-to-characteristic nonconstant finiteness still means Tate/BSD; this distinct assertion is the remaining gate.
4. B.4: all finite arithmetic terms and primitive integral free classes have explicit terminating presentations/constructions, independently audited. This item is proved in that effective sense. Vandiver is only a gate to a uniform zero formula, not to the algorithm.
5. B.5: finite duality and Tate/Artin–Tate rational cases are complete. General number-ring graded dual completions have the exact c0/c1 gate for the prescribed motivic dual pair; an actual functorial rational absolute category and arbitrary-motive realization remain additional requirements, not consequences of a formal completion.


## 04:25 UTC continuation: audited B4 completion and stronger B1 boundary

The primitive integral generator search in `sections/b4_generators.tex` passed independent audits by root and Part D. D's complete note is `part_d/b4_generator_third_audit.md`. The exact finite predicate for real-proper cycles follows Kerr–Li footnote 4; integer coefficients are cleared from the actual supported correction chain, with no dependence on the broken general formulas of Kerr–Yang §4. The Beilinson regulator is the one in Flach–Morin §5.8.3. Kerr–Yang Lemma 2.8's extra factor two converts to Borel normalization and must not be inserted again. The output is a polynomially described cycle over Q with integer coefficients, whose localization preimage is an integral-base motivic class; it does not claim that taking a raw Z-closure of those equations gives an admissible cycle. The finite arithmetic C_m presentation plus this primitive-cycle construction now gives B4 as an effective presentation/construction, not a uniform Vandiver assertion.

Opened Kahn's published 2003 paper, *Équivalences rationnelle et numérique sur certaines variétés de type abélien sur un corps fini*, https://www.numdam.org/item/ASENS_2003_4_36_6_977_0.pdf (26 pages). Exact results: Definition 1 p978; Theorem 1.4, Proposition 1.5 p981; Lemma 1.9, Theorem 1.10 p982; Corollary 2.2 p982; Theorem 3.6 pp988–990; Corollary 3.8 pp990–991; Theorems 5.1–5.2 pp998–1000.

The currently opened van Hoften–Sempliner Theorem I (CM Hodge) and Milne1999 Theorem7.1 remove Tate as a hypothesis for all finite-field abelian varieties. Kahn then supplies the essential additional rational=numerical step for every abelian-type Chow motive, plus all integral Weil-etale comparisons and finite generation in all twists. This extends B1 substantially beyond divisors without silently assuming general Beilinson.

For arbitrary X, Kahn5.2 gives an exact obstruction: under strong Tate, universal comparison/finiteness is equivalent to absence of a nonzero Chow motive P with numerical image zero. Explicitly, choose an abelian-type N numerically isomorphic to M, lift inverse maps f,g, and use nilpotence of u=1_N-fg to replace f by (1+u+...+u^{r-1})f. Then M=N⊕P with P numerical phantom. This proves the reduction; it does not prove P=0. Added `thm:B-abelian-type` and `prop:B-phantom-gate` with scoped statuses.

## 05:18 UTC continuation: the full Brauer question is refuted

Root noticed that the literal question at12:79 and in B.3 has no primary qualifier, while the surrounding boxed conjecture explicitly assumes ell invertible on S. This distinction produces a complete new counterexample:

S=Spec F2[t], E:Y²Z+YZ²=X³, X=E×S.

The curve is smooth, has E(F2)=Z/3, and ker(F:E→E)=alpha2. The kernel is checked directly in coordinates u=X/Y,v=Z/Y: its algebra is F2[u]/u², and the invariant-differential calculation makes its Hopf law additive. Every A1→E map is constant, so Frobenius is bijective on E(S). The exact fppf sequence injects

H¹(S,alpha2)=F2[t]/F2[t²]=directsum_{r≥0} F2[t^{2r+1}]

into H¹(S,E)[2]. The classes are explicitly the alpha2 torsors w²=t^{2r+1}, extended along a↦[a:1:0].

The section splits Rf_*Gm=Gm⊕C, with C in degrees at least1. Since tau≤1 C=Pic_rel[−1] and tau≥2 C has no degree-one hypercohomology, H¹(S,Pic_rel) injects into H²(X,Gm) in the kernel of section pullback. Pic_rel=E⊕Z. Consequently the alpha2 classes give actual independent order-two Brauer classes modulo Br(S), not merely an infinite quotient with unspecified torsion lifts. There is no use of prime-to-p proper base change, no need to vanish R²f_*Gm, and no inference from separate primary finiteness to finiteness of the whole group.

Root and Part D independently audited this argument and passed it. D supplied the direct formal-group verification; root independently found an ordinary Artin–Schreier alternative but the simpler supersingular proof is the one integrated. The primary source Conrad2006 Examples3.13,3.16–3.17,4.4 was opened for the Frobenius/Cartier-duality calculation and VF=[p]. The complete theorem is `sections/b3_characteristic_counterexample.tex`, label `thm:B-Brauer-characteristic`, included in Part B. The exact script/output are `code/characteristic_brauer_counterexample.py` and `output/characteristic_brauer_counterexample.txt`, runtime0.048279s.

**Status movement:** the literal whole-torsion Brauer question over finite-field bases changed from unresolved to refuted. The corrected ell different from p equivalence remains proved; universal finiteness for that prime-to-characteristic assertion remains unresolved and is not claimed refuted by this example.

## 05:18 UTC continuation: an independently checked failed B3 approach

Opened Kahn2025, *An approach to the Tate conjecture for surfaces over a finite field*, Theorem1.1, Proposition2.1, Corollary3.3 and Sections3.2.2–3.2.4. The explicit surface U=(E−O)×Gm overF2 for E:y²+y=x³+x+1 has PicU0, but selected divisors on the normalized constant covers have Picard order5^r even though the H¹ restriction is split surjective. The r1 case has closed divisor x²+x+1=0, residueF16, pointP=(v²+v,v) for v⁴+v+1=0, and a cover of degree4prime to5. The full normalization is essential: after shrinking, the removed −P can kill the selected class. The unbounded family uses pi⁴=−4 and orbitdegree4·5^{r−1}; geometric residue invariants also have order5^r. It disproves an automatic principalization step and a uniform exponent bound for this construction, not existence of a different successful neighbourhood. The ruled surface itself satisfies Tate.

Complete note `b3_kahn_principalization_attempt.md`; theorem `sections/b3_kahn_attempt.tex`, label `prop:B-Kahn-principalization`; exact script/output `code/kahn_principalization_counterexample.py` and its output. PartD checked the Frobenius and normalization scope. This side-result does **not** count as movement of the prime-to-characteristic Tate/BSD gate.

For B1, opened Geisser1998 Theorem3.3 and Gregory2023 AppendixA. The former needs rational=numerical equivalence in the universal motivic scope, not just the already-known equality on the ordinary Chow groups of one surface. Gregory's extra surface classes do not establish general Parshin for arbitrary surfaces. No new reduction of the universal phantom gate is claimed from these sources.

## 05:37 UTC continuation: smaller B1 and B3 gates, and the completed B2 formulation

The new `prop:B-diagonal-Chow-gate` proves a strict reduction in the index set of the still-unresolved B1 cycle assertions. Under the fixed universal Tate and eigenvalue-one semisimplicity hypotheses, Balkan–Schreieder Corollary1.3 reduces each dimension bound to codimensions i≤ceil(d/2). Their full §7.4 proof was opened: Theorem7.1 translates the bounded range to a birational cohomology vanishing, and affine cohomological dimension supplies the upper range. The elementary split injection z↦z×h^t with t=d−2i+1≥0, followed by projection pushforward, then reduces the universal assertion to codimension m on dimension2m−1 varieties only. The first case is codimension2 threefolds; no claim says that this first case alone settles higher dimensions. Root independently read and passed the written proof and the source. The existing surface-phantom warning remains: an endomorphism of a surface lives on its square and is not controlled by ordinary Chow equality on the surface itself.

The new root theorem `thm:B-relative-surface-gate` reduces the intended universal ell≠p Brauer quotient assertion, for smooth separated bases and smooth projective geometrically connected relative curves, to divisor Tate on smooth projective surfaces. It is already equivalent to curve families with a section over opens of P1. The owner independently checked the full proof: the arithmetic H1(Gamma,H1) term must be retained on nonproper schemes; the relative geometric H1 quotient is pure weight1 by fibre evaluation and becomes weight−1 after twist; Kummer finite cotype then gives actual torsion quotient finiteness. The pencil section extends over P1 and removes the base Brauer ambiguity, while regularity gives injection into the function-field Brauer group. Finite-constant descent uses restriction/corestriction with a finite killed-by-degree kernel even when ell divides the degree. Part D opened Kahn2023 Theorems6,8 and Morrow2019 Proposition4.1/Lemma4.2/Theorem4.3; their exact scopes and Kahn's positive-characteristic Picard caution are retained. This equivalence does not itself prove surface Tate and is not silently extended to singular or nonseparated bases.

The literal B2 request asks for a precise conjectural general comparison and its two specializations, not a proof of all Bloch–Kato conjectures. `def:B-corrected-comparison-package` supplies enhanced rational arithmetic categories, regulator maps, finite-field Weil cones and the full Tate–Beilinson clause, arithmetic c0/c1 f-admissibility for prescribed model/intermediate-extension data, dual completion, the correct retained-f/removed-g local conditions, and an explicit additional conjectural localization/gluing clause. `prop:B-comparison-specializations` proves its finite-field consequence via Geisser7.1/8.4 and its unconditional all-Tate number-ring specialization via the earlier dual-completion calculation. Root passed this formulation and the specializations. Universal category/realization existence is still conjectural; the general B5 proof request remains unresolved.

`prop:B-Scholbach-finite-support` now gives a literal counterexample to identifying Scholbach's ordinary Hom theory with the full absolute theory. For i:SpecFp→SpecZ and N=i_*unit, adjunction and Scholbach Definitions1.3/1.7 and Axioms1.1/1.8 give H1=K_-1(Fp)Q=0, whereas continuous Qell cohomology, ell≠p, is Hom_cont(Zhat,Qell)=Qell and the Weil class is Qe_p. Both root and D independently checked the argument. This does not refute the source's actual conditional generic f-comparison, and its crystalline omission is still recorded.

A fresh all-K3 Kuga–Satake search produced a stale public index claim. The primary current PDF is instead a one-page withdrawal notice dated2026-10-06, citing a stabilization-trace sign error. It is saved as `primary_sources/part_b/openai_kuga_satake2026.pdf`, and no claimed K3 theorem from that withdrawn manuscript is used. This has no bearing on the separately opened later van Hoften–Sempliner CM-Hodge theorem.

## 05:55 UTC continuation: the full all-base abelian-scheme gate is surface Tate

The proof drafted during CP04 freeze is now integrated as `lem:B-proper-section-descent` and `thm:B-all-bases-surface-gate` in `sections/b3_all_bases_surface_gate.tex`. Root and D read and passed the entire draft before CP04; the first formal review already counted this mathematical movement. Its post-checkpoint integration is not a second movement.

For a proper surjection T→S, an actual equalizer section b:T→A has graph image Z finite and universally homeomorphic to S. Kelly's uniform Frobenius factorization gives h:S→Z with gh=F_S^r and hg=F_Z^r. The resulting section of A^(p^r), followed by Verschiebung, descends [p^r]b. Integer denominator clearing and killing the actual torsion Čech difference prove the equalizer over Q. Flat extension Q→Qell then proves it over Qell; arbitrary Qell coefficients are never cleared by an integer. Nilpotent reduction changes sections only by bounded p-primary groups.

Under divisor Tate for surfaces, Kahn–Morrow gives divisor Tate on the total dual abelian scheme over any smooth separated base. Multiplication-by-m splits its degree-two cohomology into the base, section, and relative Néron–Severi eigenvalues 1,m,m². The m-summand is precisely H¹ of the Tate-module sheaf, and its divisor image is the Kummer image of sections. This proves invariant Kummer surjectivity on smooth bases.

For a separated singular base, take a proper smooth alteration cover. Proper Čech descent identifies the kernel on H¹ with E2^(1,0). This is a subquotient of H⁰ of the Tate-module sheaf on overlaps; finite closed-point evaluation makes it pure of weight−1 even on singular overlaps. It therefore has no Frobenius invariants. A pulled-back invariant cohomology class is Kummer, its sections agree on overlaps by the already-proved singular-base Kummer injection, and the new proper equalizer lemma descends the section. Subtraction kills the remaining invariant class. Nilpotent thickening and a finite affine open cover extend the result to nonreduced and nonseparated bases.

Consequently divisor Tate for all smooth projective surfaces over finite extensions of Fp is equivalent to finiteness of H¹(S,A)[ell∞] for every finite-type Fp-scheme S and every abelian scheme A/S. The converse already follows from Jacobians of pencil families with section over opens of P1. The gate is still unresolved; the theorem proves an exact reduction in the full requested all-base scope.

Opened exact new primary results: Kelly2018 Proposition3, Lemma18, Corollaries19–20; Stacks29.42.10,29.10.2,29.47.9,37.44.1 and85.36.3–6. Both independent auditors opened the Frobenius factorization and cohomological descent sources. C separately read and passed the complete regular relative-curve proposition during the freeze; D completed the full primary-source audit of the B1 diagonal reduction and B2 Scholbach counterexample.

The optional arbitrary-singular-base relative-curve Brauer assertion needs more than this abelian-scheme theorem. A genus-one Picard-degree obstruction can be non-torsion, and quotienting H¹(S,A) by its integer span requires a bound on ell-division. D is developing an integral lattice argument. Even after that, Leray's base term is H²(S,Gm)/δ Pic_rel(S), and H²(S,Gm) need not be torsion on singular S; non-torsion base classes becoming torsion in this quotient must be controlled separately. These issues are not silently identified with the proved all-base abelian-scheme reduction.

The exact Raynaud XIII.2.6 full chapter was sought, but its publisher page indicates subscription content and the direct PDF request returned HTML. It is recorded as not obtained. An opened primary replacement is Stacks Remark110.74.2 and Lemma110.74.3: dual-Picard extension proves generic-point injectivity of H¹ for an abelian scheme over a regular noetherian integral base in every dimension, and the field cohomology is torsion. This source has been supplied to D for the lattice proof.


## 06:20 UTC continuation: all arbitrary-base Brauer scope gates close

The new unit-cup theorem is an exact conditional equivalence, not a proof of surface Tate. For every finite-type S over F_p, including singular, nonreduced, nonproper and nonseparated schemes, put A_S=H²_et(S,Gm) tensor Z_(ell) and let C_S be the arithmetic cyclic-cup image of units(S) tensor Q_ell/Z_ell. Under divisor Tate for surfaces, A_S/C_S is finitely generated. Consequently Br(S)[ell infinity]/C_S is finite. The full H² group is permitted to have a free lattice; no full-H² finiteness assertion is made.

The proof has three independent inputs. First, perfection plus Bhatt–Scholze line-bundle v-descent gives a degree-two etale-to-v injection and bounds the restriction kernel for a finite-type perfected v-cover by Pic(T1)[1/p] and units(T2)[1/p]. Jaffe's Theorem10.11 and Proposition10.8 give finite generation. Second, smooth quasi-projective T has unit-cup generation modulo finite error under surface Tate: boundary localization identifies units with the whole weight-zero part of H¹(Tbar,Qell(1)), Pic⁰(Fbar) is torsion, and alteration trace sends Kummer units to norms. Riou's ample hypotheses are explicitly satisfied. Third, units on any finite-type base have a finite-kernel cyclic-cup map: divisorial residues on generic fields give a full-rank valuation matrix, with finite constant-field degrees.

For the chosen finite affine plus projective alteration h-cover T→S, rational descent gives the exact unit equalizer. Smith normal form bounds its defect on Pruefer coefficients. Fixed integers L,M,N then give LMN a−c_S(v) in the finitely generated restriction kernel for every a in A_S. Since C_S is divisible, the induced map A_S/C_S→A_T/q*C_S has finitely generated kernel and bounded torsion image in a finite-cotype group. Thus A_S/C_S is finitely generated. Part D wrote the full finite-error proof; I independently read and passed it, and root independently passed both this proof and the smooth unit-cup lemma. Part C independently checked the trace/norm input and opened Riou. I personally opened the exact Riou locators and Colliot–Thelene–Skorobogatov residue formula.

For a smooth proper geometrically connected f:X→S, Stacks Lemma36.32.6 gives f_*O_X=O_S after arbitrary base change, even for nonreduced S. Hence units(X)=units(S), so C_X comes from Br(S). The actual ell-primary Brauer cokernel is therefore finite. The regular pencil converse already proves this universal assertion implies surface Tate. This closes the singular/nonproper relative-Brauer base-image gate without using a positive-degree line bundle or replacing H²(Gm) by torsion in Leray. The characteristic-primary counterexample E×A1/F2 remains separate.

The independent integral torsor-lattice proposition is also integrated: H¹(S,A) tensor Z_(ell) is finitely generated under surface Tate for every finite-type base. Its actual Cech torsor cocycle has p-primary kernel by finite universal-homeomorphism graph descent and Frobenius–Verschiebung. Therefore the relative Picard H¹ has finite ell torsion even when the degree torsor has infinite order. Root and D read and passed the full written proof and exact Stacks regular-torsor source.

The B1 rational blow-up test-class restriction is included with explicit split exceptional maps. It tests only codimension2m on smooth projective rational (4m−1)-folds, even blow-ups of projective space along (2m−1)-folds. The first threefold CH² gate appears inside a rational sevenfold CH⁴ gate. Arbitrary centres encode the original obstruction; this is not counted as new substantive movement and does not prove first-case injectivity.

Literature comparison: Geisser–Morin's author PDF (published JNT238,2022,444–463) was opened, including its Artin-conjecture introduction and relevant propositions. Its Br notation means full H²; our torsion convention is kept explicit. The Gupta–Krishna2026 publisher introduction supplies Theorems1.1–1.5, including reduced projective surface and logarithmic Hodge–Witt duality results; the full PDF has not yet been obtained, so these are leads, not proof inputs. No novelty claim is attached to our conditional reduction. Jaffe Proposition10.8 was opened as a statement referring its proof elsewhere; Theorem10.11's full proof sketch was read.

## 06:51 UTC continuation: whole-prime closure and the intrinsic surface gate

The complete CP05 prime-uniform proof note is now integrated in `sections/b3_prime_uniform.tex`. Its smooth-source lemma proves one finite cokernel for arithmetic unit cups across all primes different from the characteristic, rather than only finite primary cokernels. On a smooth compactification, the Hochschild–Serre kernel is controlled by the finite-action unit lattice and the finite H¹ of the geometric Picard group; Qin2021 Theorem5.2 supplies the geometric across-prime finiteness. A fixed-degree alteration, integral Riou trace and norm compatibility descend the result. The global finite-error argument now works over Z[1/p], and divisibility of the cup image reduces every fixed-exponent quotient to finite-coefficient étale cohomology. Root and D independently read and passed the complete typeset proof, including the constant-field rescaling and the nonseparated h-cover scope.

The new corollary also proves whole-prime finiteness for abelian-scheme torsors under the same surface-Tate hypothesis. For B=A dual, the zero section splits Rf_*Gm=Gm⊕K with K in degrees at least1. Canonical truncation Pic(B/S)[−1]→K injects H¹ of the relative Picard sheaf into actual H²(B,Gm), in the kernel of section pullback. Thus torsion classes have actual Brauer representatives disjoint from the base image. Inversion is minus1 on Picard-zero and plus1 modulo Picard-zero, so the kernel from H¹(S,A) is killed by2 and is finite by finite-coefficient Kummer theory (or zero in the prime-to-p group when p=2). No locally constant Néron–Severi assertion is needed. This proves H¹(S,A)[p′] finite and H¹(S,A)[1/p] finitely generated for every finite-type base under surface Tate; the converse remains the already proved pencil reduction. The exact Picard-zero source scope was checked in Robert §2.3.2/Thm2.3.7, Moonen chapterVII Lemma7.16 and Corollaries7.23/7.25, and BLR §8.4. BLR's projectivity hypothesis is retained; its statement is not silently used for nonprojective abelian schemes.

D supplied and root audited the fixed-field Yuan reduction to smooth projective surfaces with H¹(O)=0. I independently read the complete proof and the author version of Yuan Theorem1.6 and §§4.1–4.2, including both Serre-vanishing degrees and the finite-field Bertini density argument. The fixed-prime lemma obtains all-prime divisor Tate from the invariant Néron–Severi intersection pairing and the prime-independent Frobenius polynomial, without assuming full Frobenius semisimplicity. The original cited Nguyen and degeneration proofs were not separately reopened and are recorded honestly.

The final corollary strengthens that same construction to an intrinsic canonical class. If Yuan's model has dimension2, pad it by P1, preserving H¹(O) and the generic Picard-zero. Retain a smooth threefold W until the final cut Y in |L^d|. The same arbitrarily large d simultaneously gives smoothness, the necessary coherent-cohomology injections, very ample canonical bundle by adjunction, arbitrary lower bounds for K² and pg, and positive c2 with K²/c2 arbitrarily close to1. The exact Chern polynomials are written in the proof. Root and D read the complete corollary and independently passed every step. Stacks Lemma29.40.8 and §37.63 item(2) were opened for very ampleness and the short exact conormal sequence. This is one bundled refinement, including all numerical thresholds; varying N or epsilon is not later mathematical movement. The restricted Tate assertion itself remains unresolved.

The new labels are `lem:B-unit-cup-prime-uniform`, `thm:B-Brauer-prime-uniform`, `cor:B-torsors-prime-uniform`, `lem:B-surface-Tate-prime`, `thm:B-irregularity-zero-surface-gate`, `rem:B-irregularity-zero-source-scope`, and `cor:B-canonical-surface-gate`. Their statement rows, actual audit events, and exact-label crosswalks are present. A separate formal polynomial/bookkeeping certificate is saved as `code/check_uniform_integration.py` and its output; it is not represented as a proof of any conjectural vanishing.
## Paired arithmetic coranks (2026-11-19 07:06 UTC)

The new `prop:B-paired-corank` gives two abelian surfaces over the same
`Spec Z[1/(2*11*37*389)]`, both of dimension two and Mordell–Weil rank two,
with the same entire primary Sha group (zero), but arithmetic 2-primary
cohomology coranks one and zero. They are `E389 × E11` and `E37 × E37`.
This substantiates the necessity of the local closure contribution already
identified in the exact corank theorem; it is not counted as movement on a
universal conjecture.

The complete algebraic certificate is `code/paired_corank.gp` with output
`output/paired_corank.txt`; the initial malformed multiline-GP attempt and
its failure output are retained separately. PARI 2.19.1 proves the ranks by
matching lower and upper two-descent bounds. More strongly, every explicit
quartic in each computed two-Selmer basis has the rational point `(0,1)`;
the supplied rational maps are checked by polynomial identities. Thus
Sha[2] vanishes directly, and consequently all 2-primary Sha vanishes.
The third `ellrank` entry was checked in the official manual: it measures
`Sha[2]/2 Sha[4]`, so it was not used as an unsupported shortcut.
Silverman IV.6.4(b), p.132, and VII.2.2, p.191, were opened in full and give
the depth-two formal logarithm used to prove the local closure ranks.
Agent D read the entire proof and saved output and passed them; that
independent check does not claim to reimplement PARI's descent algorithm.

## Source scope update before checkpoint 06

Root has read all mathematical Sections 1–4 of the live 25-page
van Hoften–Sempliner primary preprint: Hazama's codimension-two reduction,
the auxiliary CM construction, the Liu/BMM/GQT statements as cited,
doubling and constant-term nonvanishing, and the finite Fourier
decomposition. No error was found in this scope audit. This is a complete
reading of the preprint's argument, not an independent reproof of all its
external inputs, and it gives no general nonabelian positivity transfer.
Root's detailed record is `ROOT_CURRENT_SOURCE_RECHECK.md` and
`code/record_checkpoint_06_research.py`.

## Simply connected surface reduction (2026-11-19 07:44 UTC)

`thm:B-simply-connected-surface-gate` is now integrated in
`sections/b3_simply_connected_surface_gate.tex`. It reduces divisor Tate,
over each unchanged finite field, to geometrically étale simply connected
surfaces with H¹(O)=0 and very ample canonical bundle, retaining all
previously proved numerical tails in the same statement. It therefore
narrows the common universal B3 prime-to-p torsor/Brauer gate, while the
restricted Tate assertion itself remains unresolved.

The proof first makes the geometric fundamental group of Yuan's total
abelian model an abelian quotient, then finite prime-to-p by Kummer and
Artin–Schreier. Its rational section descends the geometric universal cover
over the original field. Prime-to-p dual isogeny differentials preserve the
ample Hodge bundle. Applying Yuan4.5 to the identical covered generic
abelian variety rebuilds a model with H¹(O)=0; this vanishing is not
assumed to survive the finite cover. Birational invariance and ample-cut
Lefschetz then preserve the trivial fundamental group, and the original
abelian factor survives in the final generic Jacobian.

Root, C and D each read the full standalone proof and passed; root also
read the full typeset theorem and strictness paragraph. Exact SGA, Stacks,
BLR and Yuan passages and read scopes are in the source ledger. The
strictness family uses the free diagonal C_r action with weights 0,1,2,3
on the Fermat surface of prime degree r=5 (r=7 in characteristic5).
Its quotient has H¹(O)=0 and geometric π₁=C_r. Padding by P¹ and a high
ample cut imposes the old canonical and numerical conditions while
preserving this nontrivial group. `code/fermat_free_action.py` and
`output/fermat_free_action.txt` give the exact finite eigenvalue/fixed-point
checks. The geometric quotient and fundamental-group proof are separate
from that computation. The new reduction remains a candidate for formal
review03; it is not pre-counted as movement in the component ledger.

