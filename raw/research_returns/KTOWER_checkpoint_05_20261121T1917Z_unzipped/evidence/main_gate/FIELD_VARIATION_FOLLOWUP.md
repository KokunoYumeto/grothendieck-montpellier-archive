# Field variation follow-up: exact useful result and remaining scope

Date: 2026-11-21 UTC. Author/reviewer: `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed, run KTOWER. This report records the new search requested after the earlier Wiles/Bruinier/Burungale–Sun/Ono–Skinner/CLW scope audit. It does not repeat or strengthen those earlier conclusions.

## Positive arithmetic result

**KT-EXPLICIT-TWO-UNIT-FAMILY**, proved in `explicit_two_unit_family.tex`, is an actual uniform partial result. For every prime ell>=7 with ell=3 mod4, write ell±2=m_±u_±² with m_± square-free and set D_±=−4m_±. Both are fundamental discriminants prime to ell. For every e=(ell−3)/2+(ell−1)t, t>=0, both fields make B1(chi_D) and B1(chi_D omega^e) units. Exactly one field is split at ell and the other inert. The twists have order (ell−1)/2>2. No original-weight bound is imposed.

The third condition is exactly the unit condition on B_(ell−2,chi_D)/(ell−2), or equivalently B1(chi_D omega^(−2)). It is not proved uniformly. No additional local splitting conditions are claimed, and even a three-unit field requires separate automorphic congruence exclusion results for the main application.

The useful primary input is Y. Benmerieme–A. Movahhedi, *Multi-quadratic p-rational Number Fields*, JPAA225 (2021),106657, DOI10.1016/j.jpaa.2020.106657. The precise checked version is arXiv2007.04864v1, 9 July2020, https://arxiv.org/pdf/2007.04864v1. A downloaded byte copy and extracted text are under `literature/field_variation_followup/Benmerieme_Movahhedi_2020.*`. Locators: Cor2.2 p5 and its preceding derivation pp4–5; Prop3.2 and full proof pp11–12; Eq3.2 and explanation p12; Th4.1 p14; Prop4.4 and full proof p15. The minus-field assertion is explicitly in the first paragraph of Prop4.4's proof. Imported Coates and p-adic L-function theorems have not been independently re-proved.

Lean independently whole-read the new theorem and its cited arithmetic proofs. Root independently whole-read the theorem, the plus-field arithmetic source and Th4.1, and requested the primitive-character/Euler-factor clarification and a sharper class-number estimate from Th4.1; both are implemented. The class-number estimate includes square cases m=1 and ell7. Root's separate minus-field source check is not claimed here without its own reported completion.

## Exact finite computation

**KT-BERNOULLI-PREFIX-FORMULA** in `bernoulli_prefix_formula.tex` is an elementary rearrangement of the defining first Bernoulli sum; no originality claim is made. It evaluates the residue using O(f+ell) operations rather than O(f ell).

`explicit_two_unit_certificate.py/.json` gives **KT-EXPLICIT-TWO-UNIT-FINITE-CHECK**: all1135 primes ell=3 mod4 from7 through20000 and both fields have a nonzero third residue. The output contains all2270 rows. This is a bounded exact result, not an empirical all-prime assertion. The script reconciles72 cases with the direct conductor f ell sum moduloell² and12 cases with exact rational Bernoulli polynomials. Row SHA256:8328795e4544c175eaa37953962b681aee08ecb2b7aa9cf787aea3660994a472. Independent formula/code review is requested separately; do not confuse it with the already completed infinite-family proof review.

## Naito and CM extension variation

H. Naito, *Indivisibility of class numbers of totally imaginary quadratic extensions and their Iwasawa invariants*, JMSJ43(1991),185–194, primary https://www.jstage.jst.go.jp/article/jmath1948/43/1/43_1_185/_pdf . The main theorem is on p185; its complete proof is §3, pp189–191. For an odd ell satisfying ell∤w_F zeta_F(−1), it gives infinitely many CM quadratic extensions K/F with ell∤h(K)/h(F), and every prime of F above ell nonsplit. It neither assumes ell∤h(F) nor concludes ell∤h(K). The extensions are arbitrary CM quadratic extensions of F; they are not required to equal F·Q(sqrt(D)) for rational D.

The original theorem, its surrounding definitions and full §3 proof have been read. The entire 1994 erratum, JMSJ46(1994),725–726, DOI10.2969/jmsj/04640725, https://www.jstage.jst.go.jp/article/jmath1948/46/4/46_4_725/_pdf , has also been read. It withdraws the general Proposition in §4 of the1991 paper that attempted to promote a single seed to infinitely many extensions; it repairs the stated numerical examples. It does not withdraw the main theorem with ell∤w_F zeta_F(−1).

The relative/full distinction is material: extension and norm compose to multiplication by2 on the ell-primary class group of F. Since ell is odd, that class group injects into the plus part for K/F and survives any conclusion only about the relative class number.

For a real subfield F0 of Q(mu_ell) of degree d, let r=ord(omega^e). Restriction to G_F0 changes that residual order to r/gcd(r,d). The distinct-character condition survives exactly when r/gcd(r,d)>2. Thus a smaller F0 can retain the condition, but Naito's ordinary relative class group does not thereby control the two remaining nontrivial cyclotomic-character components. At the full real cyclotomic subfield the residual even cyclotomic twists become trivial, so the existing distinct-character unitary argument cannot be transferred unchanged.

D. Byeon, JNT79(1999),249–257, https://www.math.snu.ac.kr/~dhbyeon/09_ci.pdf , quotes Naito as Th3.1 p251. Lemma4.1 pp251–252 treats the real cyclotomic base for a regular prime. Its Problem2 pp255–256 explicitly distinguishes special rational-radicand CM extensions from arbitrary extensions. These statements were read through the publisher-quality web PDF extraction; the local download returned503, so there is no local-byte or fresh visual-review claim.

## Other checked scopes

| Primary result | What it supplies | Why it does not supply the full requested three-unit field |
|---|---|---|
| Benmerieme–Movahhedi Cor2.15, p9, complete displayed proof read | Infinitely many ell-rational CM quadratic extensions of a real multiquadratic ell-rational F, assuming ell>=7 and ell∤w2(F)zeta_F(−1) | The extensions need not descend from rational discriminants; a multiquadratic base does not encode the required higher-order Teichmüller character. The explicit Prop3.2/4.4 specialization above is the useful part. |
| Takai, JNT186(2018),162–179, Th1 pp164/172, DOI10.1016/j.jnt.2017.09.024 | A conditional quantitative relative-class-number result with quadratic Hecke local conditions; the prime is fixed and the hypothesis is an explicit nonzero coefficient sum | It still ranges over arbitrary CM extensions of F. For F=Q(mu_ell)^+, the stated inequality ell>2[F:Q]+1 is impossible. The separately stated sufficiently-large-prime corollary fixes F first. Primary web text was checked; no full-paper proof or visual PDF check is claimed. |
| Chattopadhyay–Saikia, arXiv2012.01202v2, Th1 p2 and Prop2 pp2–3, https://arxiv.org/pdf/2012.01202 | Simultaneous class-number nondivisibility for pairs of real quadratic fields at the prime3, using the Nakagawa–Horie refinement | It treats prime3 and ordinary quadratic characters, outside the current GD prime/character regime. The cited original Nakagawa–Horie proof has not been freshly read. |
| Chida, ActaArith116(2005),99–114, Th1.2 p100, https://www.impan.pl/shop/en/publication/transaction/download/product/82115 | Simultaneous complex central-value nonvanishing for several GL2 cusp forms, from a common minimal-valuation seed at a place above2 | It is not a fixed odd-ell simultaneous unit theorem for the Dirichlet values here. Only the complete theorem statement and its definitions were read, not the whole proof. |
| Choi–Lee, RMS9(2022),65, publisher abstract, DOI10.1007/s40687-022-00361-z | A single modular GL2 central-value unit set at ell>=5, ell prime to the odd level, has a stated restricted finite-support alternative | This is a single cusp-form result with ell prime to its level, not the simultaneous nonquadratic Dirichlet characters of conductor divisible byell. No full-theorem proof review is claimed. |

The search found the explicit two-unit theorem above. The checked statements do not supply the remaining third unit for arbitrary ell and e with prescribed extra local conditions. This is a scope conclusion about those statements, not a claim that no suitable theorem exists anywhere.
