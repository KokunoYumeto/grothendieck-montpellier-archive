# Row audit of the proposed GRH bridges

**Date:** 2026-11-21. **Auditor:** GPT-6 Astra Pro. The effort setting is not exposed and is not reconstructed. This document concerns analytic dependence and source coverage. A source register's label “Proved” is preserved as metadata; it is not an independent certification of the full mathematical proof.

## 1. What was actually available

The six attached `SORTED_*.md` files are summaries. They describe complete registers elsewhere, frequently truncate statements, and do not contain the 1,190 rows they report. The attached `BRIDGE_FLAGS.tsv` contains 575 flag records, representing 525 distinct run/statement pairs in 23 runs. Among the six selected runs it contains 166 records and 152 distinct pairs. Its categories are 456 motives/Tate-twist records, 64 purity/weight records, 53 Weil-conjecture records and two RH/GRH records. Those are overlapping flags, not an exhaustive dependency register.

The subsequent recovery produced this exact inventory:

| Run | Rows reported by summary | Full register rows recovered | Numbered main-source blocks available |
|---|---:|---:|---:|
| ANABELIAN_A1, checkpoint 03 | 121 | 121 | 121 |
| ANABELIAN_A1_SUCCESSOR, checkpoint 05 | 210 | 0 | 0 |
| ANABELIAN_SUCCESSOR, final | 157 | 157 | 157 |
| GT_TOWER_CHECK, checkpoint 10 | 180 | 0 | 0 |
| LM7_PUSH, checkpoint 09 register retained in DELTA bundle | 218 | 218 | 9 |
| LM8_PUSH, checkpoint 17 | 304 | 304 | 304 |
| **Total** | **1,190** | **800** | **591** |

The nine LM7 blocks are **E.1–E.7, E.58 and E.65**. Their exact local locators appear in `LM7_PROOF_BLOCKS.tsv`. The 582 blocks from A1, ANABELIAN_SUCCESSOR and LM8 were available for full text screening. This statement does not mean that all 582 mathematical proofs were independently re-proved. The targeted analytic passages described in the ledger were read; the remaining blocks were mechanically screened and their declared register dependencies were parsed.

There are 390 unavailable full register rows and a further 209 LM7 rows whose complete statements are available but whose proof blocks are missing. The original summaries and flags expose 47 distinct A1_SUCCESSOR identifiers and 50 GT_TOWER_CHECK identifiers. `ROW_EXCERPT_ONLY_AUDIT.tsv` lists exactly those identifiers, without fabricating a complete register.

### Deliverable files and how to interpret them

- `ROW_FULL_REGISTER_AUDIT.tsv` has **800 records**, preserving every recovered statement, original status and declared dependencies. It records proof availability, targeted audit classification, and paths to qualitative prime-selection inputs.
- `ROW_ANALYTIC_LEDGER.tsv` has **108 curated entries**. These include 101 entries for the six runs, two other flagged-run examples, three intake items, the manuscript's Artin-elementary-variety passage, and the new finding A06. Every entry identifies its evidence scope and the relevant field or cohomological object.
- `ROW_FLAG_AUDIT.tsv` preserves all **575 original flag records**. `ROW_UNIQUE_AUDIT.tsv` groups them into **525 distinct pairs**. The initial excerpt-only classifications were updated where full source was recovered.
- `ROW_SOURCE_TERM_HITS.tsv` records mechanical source hits and locations. Hits are evidence to inspect, not automatic proof dependencies.
- The declared-dependency parser finds **201 register rows** with a recorded path to one of **38 curated qualitative prime-selection inputs**: 136 LM8 rows and 65 LM7 rows. These paths include explicit reuse and register-level summary dependencies. They are not a newly certified proof DAG. The exact seed fields are retained in the full ledger.
- `ROW_CHECK_EVENTS.tsv` separates deterministic source screens and computations from targeted reading. Automatic flag screens have type **“computation or formal certificate”**, expressly limited to text/metadata; they are not called independent proof rechecks.
- `SOURCE_RECOVERY_MANIFEST.tsv` gives exact source identities, dates, byte sizes and full SHA-256 hashes, including all recovered main source files. The four compact recovered registers are also retained under `evidence/registers/`. Giant input archives should not be included in the final deliverable.

## 2. The two RH/GRH flags do not establish a conditional theorem

**LM8_PUSH A.69.** The flag points to the abbreviation “DS/RH”. The recovered proof explicitly invokes the **Deuring–Shafarevich p-rank formula and Riemann–Hurwitz genus formula**, at lines 151, 173 and 180 of `sections/A_dihedral_two_power_fixed.tex`. Here RH does not mean the Riemann Hypothesis. The argument also uses geometric special-fibre and Tate-module information; that does not change the meaning of this abbreviation.

**S6_SERIES_GRIND maps:src:F.2.36.** The supplied context says that its class and unit groups were certified with **`GRH=false`**. This is evidence that the reported computation was not run under a GRH flag. Its full proof and computational artifacts were not recovered, so this audit does not independently certify that computation.

Consequently neither of the two initial RH/GRH flags supports the claim that an existing result becomes unconditional after accepting either stipulated hypothesis. This does not establish that no analytic dependence exists elsewhere: full LM8 proofs contain many qualitative Chebotarev uses absent from those flags.

## 3. Qualitative Chebotarev already supplies the original existence statements

For a finite Galois extension L/K and a conjugacy class C, the qualitative theorem gives density |C|/|Gal(L/K)|. There is no GRH assumption in that statement. The exact statement checked here is Milne, *Class Field Theory*, v4.03, Chapter V, Theorem 3.23, printed page 164. The following are genuine quantitative enhancements: after a finite field and finite exclusion set are specified, the effective Galois section's Finding G01 supplies a least-prime bound conditional on the relevant Dedekind-zeta GRH. It does not promote an already unconditional existence result.

For each finite Galois field L/Q and excluded rational-prime set S, the precise analytic functions for that bound are

\[
\zeta_{\widetilde L}(s),\quad\zeta_{\mathbb Q}(s),\qquad
\widetilde L=L\!\left(\sqrt{\operatorname{rad}(2\prod_{p\in S}p)}\right).
\]

For a general number-field base one first takes the Q-normal closure and excludes rational primes below the original forbidden places. The stipulated Masullo hypothesis covers these zeta functions as trivial Hecke L-functions over the relevant number fields. The stipulated Alpöge Dirichlet hypothesis covers this argument when the resulting field over Q is abelian. No general Artin-holomorphy assumption is needed for the stated effective-Chebotarev theorem.

### Exact fields and row identifiers

| Run and rows | Actual finite field or predicate | Quantitative family |
|---|---|---|
| LM8 A.16 | M/Q finite Galois containing the actual normalizer field, target the class of complex conjugation | ζ_M, with the G01 exclusion compositum |
| LM8 A.20 | Any quadratic L/K; split and inert sets demonstrate the invalid density-intersection inference | Hecke over K in general; a counterexample with K=Q already lies in the Dirichlet family |
| LM8 B.20, B.22 | Q-normal closure of the specialized torsor fibre after the finite quotient, deck-constant coefficient field K and Hilbert specialization a have been chosen | ζ of that finite normal closure; no bound on a or quotient depth is supplied |
| LM8 C.30 | Q(ζ₁₂), Frobenius residue 5 | Dirichlet characters modulo 12 |
| LM8 D.1 | Q(ζ_(5^r)), Frobenius residue 1 | Dirichlet characters modulo 5^r |
| LM8 D.8 | Q(E_c[5], μ₅), completely split primes | ζ of this exact division field |
| LM8 D.11 | Field over L fixed by ker(ρ_(M(−1)) mod ℓ^(k+1)); Q-normal closure for rational primes | ζ of that normal closure |
| LM8 D.3, D.28 | Kernel field of g ↦ (s₀(g) mod 5, χ₅(g) mod 5^(r+1)); image in H₅ ⋊ (Z/5^(r+1))× | ζ of this actual Heisenberg/cyclotomic image field |
| LM8 D.44, D.48, D.62, D.63, D.65 | Joint splitting field of the finite actual Alexander module W_r and χ₅ mod 5^r; D.63 uses r+1 | ζ of this actual joint image field |
| LM8 D.58 | Q(ζ₃₀), Frobenius residue 17, excluding primes dividing c | Dirichlet characters; finite exclusions can be added to a cyclotomic modulus |
| LM8 D.60, D.61, D.66 | Kernel field of the actual finite affine homomorphism g ↦ (z(g),ρ_r(g)) | ζ of the affine image field |
| LM8 D.67, D.69, D.70, D.71, D.73 | The same construction with a finite nonabelian coefficient group H_r and its actual action; arbitrary number-field base in D.70 | ζ of the Q-normal closure of the actual nonabelian affine image field |
| LM8 D.78–D.87 | At each original finite Cartier-dual coefficient module, the actual finite affine cocycle/action field | ζ of that field, not a formal ambient affine group |
| LM8 E.1, E.2 | K=Q(i); K(P)/K for a generator P of E₆[12], of degree 16 in the source calculation | Finite-order Hecke L_K(s,χ) for Gal(K(P)/K), or ζ_K(P); not generally Dirichlet over Q |
| LM7 A.16 | Q(ζ₉,∛3), governing q≡4 or 7 mod 9 and 3 noncubic mod q | ζ of the degree-18 field; Hecke over Q(ζ₃) also describes its abelian layer |
| LM7 A.25 | Q(ζ₉), Frobenius residue 2 or 5 | Dirichlet characters modulo 9 |

LM7 A.16 and A.25 require a qualification: their full register statements are recovered, but their original proofs are missing. The fields above are reconstructed from the arithmetic predicates; this does not verify their separate pro-three group presentations. To check A.16's arithmetic density, over Q(ζ₃) the extensions adjoining ζ₉ and ∛3 are independent cubic extensions. Their compositum has degree 18 over Q. The desired conjugacy-stable set has four elements, giving 4/18=2/9. A.25's two classes out of the six units modulo 9 have density 1/3; they are disjoint from A.16's classes.

The finite affine construction matters. A cocycle z with finite action ρ defines a genuine homomorphism g ↦ (z(g),ρ(g)). If δ is in the action kernel and z(δ) is nonzero, or nonidentity in a nonabelian coefficient group, its conjugacy class in the actual finite image is nonempty. Chebotarev can detect that class. An arbitrary affine element outside the actual Galois image cannot be prescribed. The recovered LM8 proofs retain precisely this requirement.

An effective bound for each selected prime does not bound a preceding Hilbert specialization, the finite quotient needed to separate two profinite elements, the first obstruction depth in an inverse system, or the entire infinite sequence of prime choices. LM7 A.43 and B.6 already give terminating field enumerations at fixed depth using degree and discriminant bounds. They explicitly do not give a stopping rule for every positive infinite-tower instance.

## 4. Primitive roots at a fixed prime and Artin's conjecture are different inputs

ANABELIAN_A1 B.3 and ANABELIAN_SUCCESSOR A.8, A.10, A.17 and A.35 retain an explicit finite condition such as ord_ℓ(p)=ℓ−1. At a given p and ℓ, this is finite arithmetic. It implies that Φ_ℓ is irreducible over F_p and makes nontrivial character values one Frobenius orbit. These rows do not invoke Hooley to produce an ℓ satisfying all their other hypotheses.

ANABELIAN_SUCCESSOR A.12 even gives a finite genus-three counterexample where 2 is primitive modulo 3: the point-only genus-two test does not extend in that manner. A1 B.28, B.42 and successor A.36, A.41, A.44, A.77, A.80 use finite multiplicative orders or scalar Frobenius. They are not assertions of primitive-root density. A1 B.28's weak condition of sufficiently large ord_ℓ(p) can itself be met by excluding the finitely many prime divisors of finitely many p^j−1; the important geometric restrictions are separate.

For the additional assertion that a fixed nonsquare integer p is a primitive root for infinitely many primes ℓ, Hooley uses

\[
K_n=\mathbb Q(\zeta_n,p^{1/n}),\qquad n\text{ squarefree},
\]

and GRH for their Dedekind zeta functions. The theorem was checked directly in §7, printed page 47, of the Russian translation of the 1967 paper. The theorem gives an asymptotic with positive density for the ordinary arithmetic primitive-root set. These Kummer fields are generally nonabelian over Q, so this is not supplied just by Dirichlet GRH. They are covered by the stipulated all-number-field Hecke hypothesis.

That arithmetic conclusion does not prove the intake's curve-dependent theta-incidence assertion. Even two positive-density prime sets need not intersect. For example, if ℓ≡1 mod 8, both 2 and −1 are squares modulo ℓ; consequently ⟨2,−1⟩ is proper in F_ℓ×. This positive-density set is disjoint from the proposed generating condition. This is a counterexample to a density inference; it does not assert that an arbitrary curve's theta-support set is that progression. For order ℓ^a, primitivity modulo ℓ also does not automatically lift to primitivity modulo ℓ^a.

The new Finding **A06** is stronger than the logical density objection for the universal primitive-root theta condition T(C). On the explicit B.23 curve, scalar Frobenius and the genus-two difference bound reduce a hypothetical primitive-root theta point to six primes at most 704. Only 419 has 2 primitive. In H=⟨2^19 mod 419⟩=⟨119⟩, the pairs (1,418), (71,69), (350,348) all have difference 2, contradicting the two-representation bound. The independent arithmetic implementation `verify_theta_small_independent.py` checked the entire finite part successfully. The parent supplies the complete geometric proof. This curve has p-rank zero, so it is not a counterexample to A1; the positive-p-rank restricted theta question remains unresolved.

## 5. Finite-field purity and exact least-prime computations

The finite-field character-sum estimate in A1 B.3 and successor A.11 concerns finite-field L-polynomials, not analytic Dirichlet or number-field Hecke L-functions. For a nontrivial finite-order rank-one sheaf on a smooth proper curve over F_q, its H¹ eigenvalues have absolute value √q and there are 2g−2 of them. The trace bound is therefore (2g−2)√q. This gives the corrected pair estimate

\[
\sum_bN_b(N_b-1)\le\frac{N^2}{|A|}
 +\frac{|A|-1}{|A|}(2g-2)^2q-N.
\]

Deligne's *La conjecture de Weil. I*, formula (1.5.1) and Theorem (1.6), provide unconditional finite-field input. Neither stipulated number-field GRH proves the missing existence of a quotient and a prescribed base point satisfying the numerical criterion. In particular A1 B.5 and successor A.15 remain geometric existence problems, not disguised zero-location statements. Successor A.38 expressly warns that finite-field Chebotarev controls closed points of a parameter space but not prime order and simultaneous conditions on every nonzero cyclic multiple.

The genuine least-prime rows are finite arithmetic statements about specified curves or finite censuses:

- A1 B.27: least prime 191 for its fixed marked curve, with least constant degrees ten at 191 and four at 229.
- A1 B.30: least odd witness prime 5 and first field F_(3^8) for its specified quartic.
- A1 B.34: least constant degree three, and at that first field least prime 13. The source does not determine the least prime over arbitrary constant extensions.
- Successor A.19, A.24, A.31, A.72, A.74, A.91, A.92, A.93 and A.95 contain fixed-curve exclusions, witnesses or finite-census conclusions. Their scopes differ; unspecified remaining pairs are not silently assigned a least prime.
- A1 B.32 and successor A.96 explicitly leave other all-extension minima unresolved. A1 B.4 gives a finite test for one ℓ, not a termination bound on searching all ℓ. Successor A.16 rules out a universal bound depending only on (p,g).

The B.23 conductor enumeration and retained independent Bezout verifier were rerun. The enumeration reduced its conductor candidates to 191 and 229. At both conductors the verifier passed hashes, encodings, independent division-polynomial compositions, and the full polynomial identity VA·PA+VB·PB=1 over F_(2^38). The first verifier attempt encountered a missing python-flint dependency; after that dependency was supplied, the retained verifier completed successfully. It is correctly described as a rerun of the retained independent verifier, not a newly written independent implementation. The new small A06 arithmetic verifier is independently written and is distinguished in the event log.

## 6. Other false positives and inputs outside the two GRH scopes

LM8 A.32 and A.33 use Serre's qualitative open-image theorem and commutator Zariski density, already unconditionally. Their actual models are F_a/Q: y²=x³−3x+a, a=±6, with j=−216 and rad(2N)=6; the later number field L restricts these representations. Thus no descent gate remains. G06 gives, under H_M, full mod-ell image over Q for ell>964 log6+5760 and image index at most [L:Q] over L, without asserting full image over L. Unconditionally, Lombardo over Q and restriction give adelic index <[L:Q] exp(10^21483) max{1,h_F(F_a)}^(4.8·10^10), using the stable Faltings height. These numerical refinements do not alter the original qualitative conclusions. LM8 A.46–A.48 use Faltings's crystalline comparison; this is not a Faltings–Serre finite trace test. LM8 D.25 uses Faltings's finiteness of rational points, which gives neither an effective height bound nor a finite Tate-module comparison. The flagged RESEARCH_SA07 F.3.6 excerpt instead mentions a Hom theorem; its full proof remains unavailable.

LM8 A.54 chooses generators of F_41× and F_61× at two fixed places. LM8 A.55 chooses a root of unity to identify a Kummer target. LM8 D.93 uses the elementary fact that 2 generates Z_5×. None is Artin's varying-prime conjecture. LM8 D.31 uses the Artin braid action. The manuscript at `ARCHIVE_149_scan037.tex:5` says “variété élémentaire d'Artin”: this is an algebraic-geometric object, also unrelated to primitive-root distribution. The flag ledger's Artin motives, Artin–Verdier complexes and Artin–Schreier covers are kept separate as well.

GT_TOWER_CHECK C.1.21 takes the least **index** J with v_ℓ((J+4)!)≥N. It is not a least-prime assertion. Its complete proof is missing; this classification uses only the displayed definition.

The intake's D.30/D.31 discussion still needs finite ramification of an actual pulled-back Legendre Tate system, the actual local-section and modularity inputs, and exclusion of the specified finite cusp-label pattern. Qualitative prime splitting and finite-field Weil trace bounds already suffice for the displayed trace contradiction. A number-field GRH assertion does not supply those geometric or ramification hypotheses.

## 7. Source recovery, identity and remaining limits

The recovered archives are identified in full by the manifest. Their archive hashes are:

| Archive | SHA-256 |
|---|---|
| ANABELIAN_A1_checkpoint_03.zip | `1fa68af020ae052b3993721d6480029700acb9df298a96da042392682da29918` |
| ANABELIAN_SUCCESSOR_final.zip | `1e618237514008e0023791d8cff1bb935e0802f5d95ea542b6e71b9da79fdeea` |
| LM8_PUSH_checkpoint_17.zip | `455c5f3d4c64bc2b5fbdaa2b71b69deb82b98ab5c8f65c9951421d0c4178f6bf` |
| DELTA_2-3_reciprocity_of_frames_on_GT.zip | `8fb0d94909f50501503e934e1dfa2f0307e3cf63e5765f794d3f1426a169863c` |

Searches covered the exact missing checkpoint names `ANABELIAN_A1_SUCCESSOR_checkpoint_05.zip` and `GT_TOWER_CHECK_checkpoint_10.zip`, their timestamp forms `ANABELIAN_A1_SUCCESSOR_checkpoint_05_20261118T0610Z` and `GT_TOWER_CHECK_checkpoint_10_20261117T0945Z`, exact `_results.csv` names, `ANABELIAN_A1_SUCCESSOR.tsv` and `GT_TOWER_CHECK.tsv`, and broad title variants including `ANABELIAN`, `GT`, `LM7`, `A1 SUCCESSOR` and `GT TOWER`. Exact names for the earlier A1 and LM8 archives initially failed, while simpler title queries succeeded; this is why a zero result is not equated with nonexistence. The complete search responses are retained, with no signed-download URLs in the audit manifest or recorded search JSONs.

No nested archive with either missing full source was found in the recovered archives. The parent also tried the documented Personal Context route and reported the explicit tool response **“Personal context is disabled.”** That route was blocked, not searched with zero results.

The remaining concrete recovery route is to provide the two exact checkpoint archives or their standalone full registers and papers from the source folders named in the summaries. A differently titled upload with a known identity could also be retrieved. Until then, the correct result is a complete audit of the available material with a precisely enumerated coverage gap, not a claim to have checked all 1,190 proofs.

## Primary reference locators actually inspected

1. Pierre Deligne, *La conjecture de Weil. I*, Publications Mathématiques de l'IHÉS 43 (1974), 273–307, formula (1.5.1), Theorem (1.6): <https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf>.
2. J. S. Milne, *Class Field Theory*, version 4.03 (2020), Chapter V, Theorem 3.23, printed page 164: <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.
3. Christopher Hooley, *On Artin's conjecture*, J. reine angew. Math. 225 (1967), 209–220; theorem checked in the Russian translation, *Matematika* 12:1 (1968), §7, printed page 47: <https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=455&what=fullt>. The original English publisher page was access-blocked; no claim is made to have re-proved Hooley's analytic argument.

The exact effective-Chebotarev constants and their primary-source checks belong to the separate effective Galois section. Source papers cited inside the recovered registers but not opened in this audit are not counted as independently rechecked references.
