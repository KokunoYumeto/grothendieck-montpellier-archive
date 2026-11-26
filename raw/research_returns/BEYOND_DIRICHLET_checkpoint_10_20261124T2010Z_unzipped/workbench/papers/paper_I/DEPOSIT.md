# Deposit sheet

## Title

**The 3-primary K-groups of Q(ω, ∛269) in every degree — After Schneider and Jaulent–Michel**

The author line is intentionally empty.

## Abstract

Schneider’s description of wild kernels by cyclotomic coinvariants, developed in logarithmic form by Jaulent and Michel, reduces even algebraic K-groups to arithmetic in a cyclotomic tower. For E = Q(ω, ∛269), where ω is a primitive cube root of unity, we determine

\[
K_{2e}(\mathcal O_E)_{(3)}\simeq\mathbf Z_3[\omega]/(\omega-1)^{5+2v_3(e)+\mathbf1_{e\equiv2\pmod3}}
\qquad(e\ge1)
\]

from finite logarithmic class-group certificates in degrees six, nine, and eighteen. A ray-class genus calculation determines the residual cyclotomic module, a short specialization lemma uses the first-layer logarithmic bound, and a labelled action on a cyclic group of order nine determines the exceptional residue class. We also prove the precise length-one correction between the character-valued strict group over Q(ω) and the ordinary strict group over E, including vanishing of the former at weight zero. A finite theta estimate proves positivity of the associated completed cubic Hecke function on the real axis. An appendix also computes the faithful seven-primary cyclotomic class module and every continuous cyclotomic strict specialization. A further appendix determines the one-prime ramified module: it has a linear characteristic factor whose values are unbounded along positive integer weights, while the matched strict lengths remain one. The text and programs were produced by GPT-6 Astra in ChatGPT Pro mode and checked by separate instances of the same model as recorded in the workbench; no human verification is claimed.

## Subject

Algebraic number theory: algebraic K-theory of number rings, logarithmic class groups, cyclotomic Iwasawa theory, and one explicit nonabelian cubic Hecke factor.

Suggested MSC 2020: **11R70** (primary); **11R23, 11R29, 11R37, 11M41** (secondary).

## Keywords

Even algebraic K-groups; wild kernels; logarithmic class group; strict Selmer group; cyclotomic twist; pure cubic field; Iwasawa module; Hecke L-function; theta positivity; certified number-field computation.

## Main results and limits

Theorem 1.1 is an unconditional every-degree formula for the 3-primary even K-groups of this one field, together with the two distinct strict-group formulas and the weight-zero character-group vanishing. Theorem 1.2 proves strict positivity of the completed relative Hecke function at every real argument, and positivity of the uncompleted function at every positive real argument. Proposition 7.2 also proves that the split cyclotomic module is finite and that the first logarithmic layer has additive type C9 × C9 × C3 × C3. Proposition C.1 determines the ordinary class groups C7 and C7 × C7 and a fundamental cubic unit. Theorem 1.3 proves exact seven-primary class stability and the strict specialization O7/(7,u−1) for every continuous cyclotomic character. Its full proof and every exact witness are printed in Appendix D of the main PDF and in the accompanying editable extract; integral principal weights give O7/7O7, and primitive wild twists have the stated exact normalized cost.

Theorem 1.4 determines the one-prime module and local/global-unit quotient as Z7[[T]]/(T−a), with v7(a)=1, and identifies the natural unit inclusion as multiplication by seven. Its full proof and the finite local-unit matrices are printed in Appendix E. Every characteristic generator has valuation 1+v7(e−e*) at principal weight e, with e* a seven-adic unit; the values are unbounded on positive integers while the strict length remains one. No identification with a particular normalized Katz function is assumed.

The three-primary finite arithmetic inputs are proved in Section 6 and Appendices A–C; Appendix D contains the complete seven-primary proof and finite certificate. The proof invokes the published comparison, duality, cyclotomic descent, class-field-theoretic, and Hecke analytic theorems cited with exact locators. It grants no unproved rank, class-number, or numerical hypothesis. No conclusion about the nonreal zeros or the generalized Riemann hypothesis is asserted. The uncompleted function has the usual trivial zeros; real positivity of the completed function does not remove those trivial zeros.

## Note on method

The text and programs were produced by GPT-6 Astra in ChatGPT Pro mode. The recorded checks distinguish a statement-only partial reconstruction from source-based proof audits, targeted checks by separate instances of the same model, fresh complete arithmetic computations, and two full-paper readings. The initial statement-only work did not independently reconstruct the full finite Iwasawa argument. A second same-model worker subsequently reconstructed the complete argument from the statement and the four explicitly granted finite arithmetic assertions, without reading this paper or the attached proofs. Its ray-class calculation and shorter specialization lemma were then checked separately and integrated; the arithmetic assertions were independently discharged by the standalone computations. The exact degree-nine action and the compact degree-eighteen bound were freshly executed from standalone programs without imported binary number-field data. The ordinary-class proof uses a separately authored exact ideal-relation calculation and rigorous interval arithmetic; the theta proof has independent coefficient constructions and an integer tail certificate. No human verification is claimed, and no formal proof-assistant verification is claimed.

The original text and programs are dedicated to the public domain under **CC0 1.0 Universal**; cited external publications retain their rights. The workbench address is https://github.com/KokunoYumeto/zeta-and-l-functions-workbench and the project record address is https://github.com/KokunoYumeto/mathematics-workbenches. The standalone project and its evidence accompany this deposit; the note does not assert that newly created files have already been published to either remote repository.

The seven-primary supplement has a separate full finite certificate: exact units and residue characters, two regulator implementations, independently produced bounded cubic-twist L-values, and a rational-isolation argument using Friedman’s regulator bound. A further same-model worker reconstructed the complete class-stability-to-Selmer argument from the two granted finite class-group inputs before reading the proposed proof. Its record was then target-checked. The full BNF class output from candidate generation remained uncertified and is not a theorem input.

## The eight opening requirements

| Requirement | Exact place in the paper | What the reader finds |
|---|---|---|
| 1. Title and named programme | Title, with subtitle “After Schneider and Jaulent–Michel” | The field, coefficient prime, all-degree assertion, and credit for the cyclotomic/logarithmic programme. |
| 2. Abstract beginning, result, and production statement | Abstract: first sentence, displayed formula and following sentences, final sentence | Named starting work, explicit theorem and finite arithmetic method, significance of the corrections, analytic scope, model and no-human statement. |
| 3. Complete main theorems and meaning | Sections 1.1–1.2, Theorems 1.1–1.4, and paragraphs immediately following | Full field and coefficient conventions, three-primary module formulas, weight zero, summation formula, real positivity, seven-primary class stability with exact strict local conditions and coefficient normalization, and the one-prime module with its moving-center valuation formula. |
| 4. Why the result matters | Section 1, first and second paragraphs; Section 2, final mechanism | One explicit nonabelian field has every even 3-primary K-group determined from finite data; ordinary class vanishing is separated from nonzero wild kernels and the exceptional residue class is explained. |
| 5. Exact division of credit | Title; abstract; Section 1, first paragraph; Sections 3, 5, 6, and 9 at the cited theorem locators | Schneider and Jaulent–Michel carry cyclotomic descent; Weibel and Kolster–Movahhedi carry comparison/duality; Belabas–Jaulent carry certified logarithmic algorithms; Louboutin–Munsch carry the finite partial-sum idea. The ray genus calculation, power-series specialization argument, oriented arithmetic, complete witnesses, and field-specific theta certificate are written out here. |
| 6. Earlier and recent context | Section 1, paragraphs 1–3; bibliography; Section 9 | Classical comparison and descent, logarithmic computation, real theta positivity, Dunn–Radziwiłł’s conditional prime Gauss asymptotic, and OpenAI’s dated 2026 first-moment and zero-free-half-plane theorems. The latter analytic results are context, not dependencies of the K-group formula or the real positivity proof. |
| 7. Scope and remaining open statements | Section 1 after the context paragraph and Theorem 1.2; Section 8 “Explicit groups and scope” | The K-theoretic assertion concerns coefficient prime three and one field; the separate seven-primary result has its exact faithful-character scope. Completed and uncompleted real positivity are distinguished, and no nonreal-zero theorem or general rank conclusion is claimed. |
| 8. Prose proof overview | Section 2, headed “Proof overview”, before the detailed proofs | Local correction, residual cyclicity, genus generator bound, exact ray genus quotient, two annihilator ideals, specialization of the exponent-nine relation, cyclotomic scalar four, and the separate positive-kernel proof. |

## Authors whose work is carried or discussed

| Author(s) | Work and precise role |
|---|---|
| Peter Schneider | *Über gewisse Galoiscohomologiegruppen* (1979): historical cyclotomic wild-kernel framework; the precise twist/control formulation used here is checked in Jaulent–Michel. |
| Jean-François Jaulent and Alexis Michel | *Approche logarithmique des noyaux étales sauvages des corps de nombres* (2006), Definition 1, Proposition 2, Theorem 3: logarithmic cyclotomic descent and twist convention. |
| Charles A. Weibel | *The K-book* (2013), Chapter VI, Theorem 8.2, Corollary 8.3, Example 8.3.1: integral and residual étale K-theory comparison. |
| Manfred Kolster and Abbas Movahhedi | *Galois co-descent for wild kernels and capitulation* (2000), Section 1: wild-kernel global-to-local sequence. |
| Karim Belabas and Jean-François Jaulent | *The logarithmic class group package in PARI/GP* (2016), especially Lemma 3.8: algorithm and exact stopping criterion. |
| Chia-Fu Yu | *Ambiguous class number formulas* (2014), Theorem 1.1: ordinary ambiguous class formula used in the genus argument. |
| J. S. Milne | *Algebraic Number Theory* (2020), Theorem 4.3; *Class Field Theory* (2020), class-number residue formula, ray-class theory and cyclic Hasse norm theorem: arithmetic background with explicit locators in the paper. |
| Stéphane Louboutin and Marc Munsch | *On positive real zeros of theta and L-functions associated with real, even and primitive characters* (2013), Theorem 4, pp. 646–647: finite partial-sum positivity method, adapted to the linear Hecke kernel. |
| Bjorn Poonen | *Tate’s thesis* (2015), Theorems 5.16 and 5.22(b),(c), pp. 34–39: complete primary exposition/proof of Hecke continuation and functional equation. |
| Alexander Dunn and Maksym Radziwiłł | *Bias in cubic Gauss sums: Patterson’s conjecture* (2024), Theorem 1.1, arXiv v3 p. 3: neighboring conditional prime Gauss-sum theorem, cited for context. |
| Takashi Fukuda | Remarks on Z_p-extensions of number fields (1994), Theorem 1(1), p. 264: exact stability after equality in two consecutive layers. The required one-prime case is also proved directly in the supplement. |
| Eduardo Friedman | Analytic formulas for the regulator of a number field (1989), Theorem B, pp. 599–600: the unconditional regulator lower bound used to isolate the rational class-number-to-unit-index quotient. |
| Karl Rubin | The “main conjectures” of Iwasawa theory for imaginary quadratic fields (1991), equation (5), p.36, and Theorem 5.3(v), pp.40–41: the one-prime class-field sequence and absence of finite submodules. |
| Romyar Sharifi | Iwasawa Theory, Corollaries 1.3.9 and 1.3.12, Remark 1.3.21 and Proposition 3.2.20: finite norm and split-class inverse-limit control. |
| OpenAI | *An unconditional first moment for cubic Gauss sums* (2026-09-25), Theorem 1.1, p. 1; *The quasi-Riemann hypothesis* (2026-09-30), Theorem 1.1, p. 4: neighboring analytic statements, opened and read for precise context; neither is imported into this paper’s proofs. |

## Editable deliverable

`main.tex` contains the paper, all exact witnesses, the complete oriented-action program, and the inline bibliography. `BUILD.md` states the clean build and arithmetic commands. `programs/` contains standalone fresh programs and `evidence/` contains the recorded successful outputs. The main PDF contains every proof and exact witness. Its editable source includes the local proof and bibliography files shipped inside the project. The supplement_seven directory is a complete separate editable project with its own full proof, bibliography, exact data, analytic certificate, portable verifiers, and build instructions. The author lines remain empty.

The current main PDF has 43 pages. Its new Appendix E is built from the local source seven_universal_norms.tex and depends only on the complete finite data already printed in Appendix D and the explicitly cited published theorems. Both appendices are included in the main PDF. The full new proof received targeted same-model review, the copied portable local-index verifier passed, and all 43 pages were inspected after a fresh three-pass build.
