INCOMPLETE as a complete source-by-source concordance; precise mathematical results and remaining access/scope gates are separated below.

# Part D working report

AI-produced by GPT-6 Astra (OpenAI), inherited research configuration, agent /root/lie_theory. Began 19 November 2026 at 11:04 UTC; updated approximately 12:25 UTC. No priority is claimed. Parent owns final compilation, aggregation and persistence. This agent now takes A.5 separately.

## Per-task states

| Task | State | Scope / remaining gate |
|---|---|---|
| D.1 base theorem | D.001 refutes unrestricted Lie version; D.009 and D.017 prove repaired versions | Lie over every Q-scheme; group with simply connected derived subgroup over every base, including characteristics 2 and 3. |
| D.1 Picard sequences | Proved, D.010–D.011 | Normal locally noetherian base; character lattice term retained; right zeros proved; absolute groups versus relative sheaves distinguished. |
| D.1 RigKos | Proved, D.015 and D.021 | Full Z[1/h] scope; integral cyclic/Coxeter equivalence; finite étale quotient need not split. |
| D.1 letter predictions | D.012–D.014 and D.018–D.020 establish the specific predictions used | Dimension, rational fibres, opposition, subregular rank/uniqueness, and invariant-selection obstruction. Full all-orbit Jacobian tables and lists of all automorphism stabilizers are not supplied. |
| D.1 literature concordance | Substantial but partial | All requested articles and original Spaltenstein thesis opened; later LNM815 and LNM366 pages remain uninspected. |
| D.2(a) | Proved all types, D.002–D.003 | Weyl extension nonsplit exactly F4,E6,E8. Common normalizer additionally nonsplit in C_(4m). |
| D.2(b) | Proved/refuted, D.005 | Outer signs agree, negative exactly A_even. Unpinned natural line identification is false. |
| D.2(c) | Proved, D.006 | Single deleted coefficient is regular exactly at an affine node of mark one. |
| D.2(d) | Proved, D.007–D.008 | Injective only A1 and B2=C2. Borel classes: one-part or opposite-parity two-part partitions in A; only regular elsewhere. |

## Full corrections and qualifications, with input line numbers

The supplied source files are unmodified. Line numbers below refer to them.

1. `C123-01_transcription.tex` line 17, scan123/002: wcw^{-1}=c^h must read c^n. The original scan itself contains h. Thus this is an original typescript error, not an AI-transcription error. Direct image check saved as source_external/lie_theory/123_002.png. The initial report's uncertain attribution is superseded.
2. `K123-01_transcription.tex` lines58,78,81,85, scans006–007: retain the Weyl-action hypothesis and characteristic-two caveat. D.001 gives PGL2/F2 with generically degree-two incidence. This refutes an unconditional modern restatement, not the author's already-qualified discussion. D.017 gives the arbitrary-base group repair with simply connected derived subgroup.
3. Same file lines215–227 and250–295, scans011–013: absolute Pic(D)→Pic(B) has character-lattice cokernel H1(S,M), whereas its étale-sheaf version is an isomorphism. D.010 proves the canonical decomposition, the regular-locus restriction, and right exactness already for a normal locally noetherian base. The latter strengthens line295 rather than silently importing its regularity restriction.
4. Same file line250: EGA IV21.4.13 is in Errata et Addenda, liste3, item53, printed p361. Item53 is not a page number. Full hypotheses in21.4.9 and21.4.11, pp358–360, were read before applying the corollary.
5. Same file line227: P+ is the ample cone only if it means the open, strictly dominant chamber. Under the usual closed-dominant convention its boundary weights are nef. Both readings are stated. The affine-map and unit-section ampleness criterion on lines273,297 is proved without normality.
6. `K123-02_transcription.tex` line235, scan035: the author crosses out “bel et bien” and inserts “il” after “est”. The scan supports the interrogative “est-il splitté”. D.016 answers splitness negatively: for split A2/Q the quotient is Spec Q(zeta3). It is a refutation under an affirmative reading, but should not be described as an unambiguous assertion after the handwritten correction. Image saved as123_035.png. This corrects an early message by this agent.
7. Same file lines204–209, scan034, and `K123-03_transcription.tex` lines162–166, scan042: matching outer signs do not give an unpinned natural g_theta ≅ Delta. The torus acts nontrivially on the root line and trivially on the quotient line. D.005 supplies the precise invariant tensor line and the pinned comparison.
8. `K123-03_transcription.tex` lines243–246, scan047: exactly one zero coefficient does not always give a regular nilpotent. D.006 proves that the deleted highest-root mark must be one, with a complete type table.
9. Prompt R11 gives A3 as a failure of injectivity. D.007 proves A2 is already a failure, using diagrams(1,1) and(2,2), and classifies all types. This is distinct from the correct subregular positivity observation at `study/letter_to_kostant_123.md` lines57–60.
10. `C123-02_transcription.tex` line23, scan023, and that study file lines35–39: the strict subregular rank drop outside ADE is false. D.012 checks sp4 directly; D.019 derives rank r−1 in every simple complex type. Subregular uniqueness likewise holds in all types.
11. Study file lines64–67: the memory-based Steinberg attribution needs exact locators and hypotheses. In the opened 1976 original, Theorem3.5 p213 is the unrestricted inequality; Theorem4.6 p217 and Theorem6.5 p223 are equalities under the displayed hypotheses. Proposition3.1 p212 is not the equality theorem. Spaltenstein thesis II.1.17 p51 gives all-characteristic equidimensionality; II.2.5–2.7 pp53–55 state the restrictions for equality. The complex letter satisfies them.
12. Study file line82: the E8 count2,903,040 omitted one factor|W|. The exact count is **2,022,633,897,984,000**. `rigkos_counts.py` and its full output certify this and all exceptional values. An intermediate message by this agent transposed digits in the large answer; the code output and present number supersede it.
13. `C123-02_transcription.tex` line9, scan022: a distinguished class would have to be outer-invariant. D.020 proves that transpose-inverse swaps both A2 classes. Therefore no functorial selection satisfying this necessary condition exists in every type. The phrase “distinguished in some sense” itself supplies no further predicate.
14. Steinberg1976 p210 explicitly corrects an adjoint-group statement in Springer's 1969 article. This must not be conflated with the requested Springer IHES30 article of1966. The separable-universal-cover condition and its necessity are Theorem1.1 pp209–210 and Remark6.1 p222.

## Certificates and coverage

`coxeter_normalizers.py` considers every unit exponent and every possible root image of a cyclic root. Each candidate is checked for integral entries, Gram preservation, every root, the conjugation equation, and a Weyl-reduction word. It certifies the entire centralizer and every automorphism exponent. Complete matrices and words are saved, not just counts. `verify_certificates.py` regenerates all roots and intertwiners using pure Python Fraction arithmetic and the opposite wall-choice convention.

Exceptional normalizer orders are12,48,48,108,240 forG2,F4,E6,E7,E8. All lifts of5 mod12 inF4/E6 and7 mod30 inE8 are exhausted to exclude complements. C4 is the unit-group extension U16→U8; both lifts of3 mod8 have order4. Its uniform 2-adic proof covers all ranks divisible by4. Classical Weyl splittings are uniform signed-permutation constructions.

`borel_dynkin.py` tests all2^r positive weighted diagrams using a proved necessary-and-sufficient rational span criterion; every rejected diagram has an annihilator certificate. `root_claims.py` certifies highest-root marks and all explicit A2-subsystem collisions. `pinned_signs.py` checks all1440 nonzero E6 root brackets and the D4 involution/triality signs; the classical families have uniform matrix proofs.

`small_counterexamples.py` checks PGL2/F2 eigenlines and Weyl action, C4 units, the sp4 centralizer and invariant differential, and the Fourier A3 nonopposite flags. `rigkos_a2.py` enumerates all36 flag pairs and all18 Phi elements, lists both free orbits, and verifies both Galois and outer-automorphism swaps. Its Fourier conjugation is exact.

`primitive_eigenvectors.py` records every exceptional root value as a cyclotomic polynomial and its exact resultant. All norm primes divide h. This certifies every residual characteristic not dividing h, not just sampled primes. Uniform classical eigenvectors and the torus isogeny of determinant h prove the other types and the integral equivalence of the cyclic and Coxeter definitions.

All programs and full output are in `code/` and `logs/`. `results.csv` contains21 results; `checks.tsv` records the proof and computation events. No computed low-rank pattern is advertised as an unproved all-rank theorem.

## Opened primary sources

Exact URLs and access status are also in `references.bib`.

- Steinberg1965, original Numdam PDF: Th1.1–1.5 pp49–50; §§2.8–2.11 p53; §3.2 pp54–55; Th6.11 p64; Th8.1 pp70–71. All-characteristic hypotheses checked. https://www.numdam.org/item/PMIHES_1965__25__49_0.pdf
- Steinberg1976, original GDZ scan: Th1.1 pp209–210; Th3.5 p213; Th4.6 p217; Remark6.1 p222; Lemma6.2, Remark6.3 pp222–223; Th6.5 p223. https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0036/LOG_0018.pdf
- Spaltenstein1977 original Warwick thesis: II.1.7–1.12 pp45–48; II.1.16–1.17 pp50–51; II.2.1–2.7 pp52–55. Relevant proofs read in full. https://wrap.warwick.ac.uk/id/eprint/139964/1/WRAP_Theses_Spaltenstein_1977.pdf
- Brieskorn ICM1970, complete article pp279–284 downloaded from IMU: diagram and uniqueness p280; ADE deformation p282; differential p283. https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.2/ICM1970.2.ocr.pdf
- Springer1966 IHES30: §4.12 pp134–135; §5.7 and Th5.9 p138; regular versus smoothly regular retained. https://www.numdam.org/item/10.1007/BF02684358.pdf
- Hesselink1976, TheoremA p249 and §§2–5. https://pure.rug.nl/ws/files/3449114/1976MathAnnHesselink.pdf
- EGA IV4, Errata item53,21.4.9–13 pp358–361. https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf
- SlodowyLNM815 publisher previews §4.1 pp43–44 and §5.1 pp60–61. Later sections not opened. https://link.springer.com/book/10.1007/BFb0090294
- SteinbergLNM366 publisher preview pp76–77, definitions3.1–3.2. LaterIII.3.10 not opened. https://link.springer.com/book/10.1007/BFb0067854
- Fu–Juteau–Levy–Sommers arXiv1502.05770v3 §§1.4.2,1.5.1 pp3–4: subregular surface table and explicit attribution to SlodowyIV.8.3. https://arxiv.org/pdf/1502.05770
- Kostant1959 text reproduced in Collected PapersI: §§6.2–6.7 and Th8.4,8.6, original pp1023,1026. OCR gaps retained as access limits. https://dokumen.pub/collected-papers-volume-i-1955-1966-2009nbsped-9780387095820-0387095829.html
- deGraaf arXivmath/0702193 §§2–3 and Lemmas2–3. https://arxiv.org/pdf/math/0702193
- Douglass–Roehrle arXiv0802.0764 Introduction and§2.1, supplementary historical source, not a substitute for the original proof. https://arxiv.org/pdf/0802.0764

## Approaches replaced

Naive E7/E8 Weyl enumeration was replaced by the exhaustive cyclic-vector intertwiner argument. Random sl2-triple searches were rejected as exclusion certificates; the positive-diagram problem has an exact linear criterion. Generic-characteristic RigKos arguments were replaced by finite-order deformation, component-group control and cyclotomic units. Merely removing codimension two from a normal scheme does not prove Picard extension; the polynomial/Laurent divisor calculation plus faithful-flat descent supplies that missing step. Finite orbit counts do not establish arithmetic splitness; the full Galois action exposes the A2 counterexample.

## Additional independent review correction (2026-11-19)

Root observed that the scheme-theoretic connected centre need not be a torus in characteristic p (e.g. centre of SL_p is mu_p). D.017 now uses the radical torus Rad(G), with an explicit graph description of its finite flat kernel, the surjection on character groups, and the cartesian comparison as a map of K-torsors. D.009 also now uses Rad(G) for consistent notation; its characteristic-zero hypothesis made the previous notation harmless.

D.010 independent audit by singularities_duality: added the full coefficientwise argument proving that the tensor pullback of N is the divisorial module; agreement at height-one points is not used alone to assert reflexivity. Audit also checked codimension, faithful flatness, character H1, and generic Picard passages.

## 14:35 UTC: full Jacobian computation

D.022 proves all classical formulas and computes every exceptional nilpotent orbit (157 including zero) over the complex numbers. The program constructs the integral root-lattice algebras, checks every basis Jacobi identity, uses fixed algebras of pinned E6/D4 automorphisms for F4/G2, and checks the E6 minuscule representation on all3003basis pairs. Every orbit has an exact sl2triple certificate and dimension check. The invariant traces are proved to generate the invariant algebra using their nonzero regular-nilpotent differentials. Rank is the number of nonzero distinct-weight differentials. Complete157-orbit run22.196534s; independent SymPy E8(a2) check3.292757s. No sampled computation stands in for an all-type assertion.

D.023 reduces every Lie element and every simply connected group element to those tables. D.024 supplies an exact finite-center projection formula for every other isogeny; the PGL2 regularsemisimple counterexample has rank0 while its SL2lift has rank1.

Original Richardson1987 pp228--241 opened in full, including visualp239. Its only undecided entry, exponent19 forE8(a2), is filled by exact dF20(e)(E_minus_theta)=3617744486400, rank6. Two genuine printed errors onp239 corrected: regularE8 exponent27 mustbe29; subregularE8(a1) has spurious9. Notnewhistoricalpriorityclaims. The originalinput C123-02_transcription.tex line25 asks the full rankquestion; this gate is now closed in characteristiczero. The explicit remaining outer-stabilizer gate begins atA3, thenD4triality.

## 14:37 UTC: typeA outer stabilizers complete

D.025 gives every quadruple automorphism group in every typeA rank. The Fourier model identifies the pair normalizer with affine actions(p,q)->(ap+x,a^-1q+y); transposeinverse is(p_rev,-q_rev). Odd n has no outer-fixed class. For evenn the exactformula counts C2stabilizers using fixedpointfree affine involutions andCRT. A3has18classes,8C2and10trivial; A2andA4alltrivial. Exhaustivepair enumeration and independentaffineinvolution counts agree. Smallest remaining outer-stabilizer gate is D4triality,768innerclasses, followedby otherDtypes andE6. All types withtrivialOut have trivialquadrupleAut byD004.

Root independent audit ofD.022--024 PASS14:37UTC: classicalPfaffian cases, invariantgenerator proof, completefiniteLieconstruction/representation verification, WDDclassification inputs, Jordanetaleslice, finitecenterprojection. Rootreran all157orbitchecks19.758052s andindependentE8(a2)trace3.154179s withsamevalue3617744486400; originalRichardsonp239errorsvisuallyverified. AgentJSONnowhas identicalmathematicaldata withrootreruntime. Rootlogs: logs/root_all_exceptional_jacobians.txt andlogs/root_jacobian_independent.txt.
