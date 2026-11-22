# Focused audit: does C.1(d) determine the two functor maps?

19 November2026, renewed review by GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode, agent `part_c_algebra`. This is a targeted re-examination of my earlier proof, not a claim of a second author. Parent requested explicit scrutiny of possible circularity, arbitrary/non-additive functors, base change, local nilpotence, and the two maps separately.

## Verdict and exact scope

**No mathematical gap or missing class of module functors was found.** `C-functor-criterion` gives necessary and sufficient image conditions and all fibres for the two maps actually written on044. Its conditions concern finite polynomial logarithms, module linearity, and a linear extension problem; none assumes the requested exponential representation. These can be made completely explicit on universal algebras, as proved below. This supplies a non-circular criterion for every arbitrary functor under the stated Q-algebra hypothesis. It does not claim a finite algorithm for an arbitrary, possibly infinitely specified functor, or replace the question by quasicoherent functors.

The original ordinary domain is the set of **uniformly nilpotent elements of the natural-endomorphism ring**, not the larger set of endomorphisms that are nilpotent separately on each vector. The quasicoherent theorem subsequently determines the ordinary map's bijectivity in that familiar class exactly: all locally nilpotent endomorphisms must be uniformly nilpotent. Formal exponential has no nilpotence requirement on its input. These are distinct assertions and are not conflated.

## Original and source checks actually made

- I displayed/read original044 again: `qa/cote68_C1-44.png`, printed/archivefolio43. Its two displayed arrows are End_K(M) to Hom_gr(formalGa,Aut(M)), and N(End_K(M)) to Hom_gr(Ga,Aut(M)); the NB asks whether these are bijections. The subsequent scheme-globalization paragraph is separate.
- I rendered/displayed/read original043: `qa/part_c_functor_scan043.png`, printed/archivefolio42. The definition gives a module M(K') over every K' and semilinear transition maps; it imposes no tensor-base-change or quasicoherence condition. The ordinary domain N(End_K(M)) is already explicit there. The reading agrees with `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_68_033-056+162-1+162-6_transcription.tex:388–416`.
- Current proof read in full: `sections/part_c.tex`, `C-functor-criterion`, `C-functor-counter`, and `C-qcoh`, including definitions of the internal endomorphism functor. The initial K-is-a-commutative-Q-algebra convention is essential. Repeating it at the new functor subsection would be a harmless clarity improvement, not a new hypothesis or source correction.
- The already opened Milne *Basic Theory of Affine Group Schemes*, version1.00(2012), ChapterVIII Example2.1 and footnote1, printedp113, was reopened as original web text (`turn232319709view1/2`, lines5231–5282). It confirms the arbitrary-module locally nilpotent statement over a Q-algebra. The same opened source's ChapterI Yoneda lemma2.1, printedp18, appears at lines743–765; the elementary universal evaluations below are also proved directly, so no new external premise is needed.
- Exact inherited ID: `SA22-10 (68/044)`, originally `inputs/RESEARCH_SA22_study/study/CHECK_EVENTS.tsv:22`. The old reader event also concerns the separate scheme-globalization correction; this audit does not relabel that assertion as the functor classification.

## Base-change and non-additivity audit

Write E(R)=End_R(M_R), where M_R is the restriction to R-algebras and each component of an endomorphism is linear over its own algebra. A map R→S induces E(R)→E(S) by restriction. It is a ring homomorphism and is semilinear for scalar multiplication. Thus a polynomial identity, nilpotence bound, logarithm, or equality λu passes along every base change. No formula E(R)=R⊗E(K), no flatness, and no faithfulness of restriction is assumed.

In particular, ρ_K(1) is an element of **E(K), the whole natural-endomorphism ring**; it is not just the operator on the single module M(K). Recovering u from its logarithm therefore does not assume that an endomorphism is detected on K-points. Such a detection assertion would be false for arbitrary functors; it is not in the proof. The original word “module functor” does require additive semilinear transition maps, but it does not require that the algebra-variable functor preserve sums, products, exact sequences, or tensor base change. The proof covers this full scope, including reduced-ring and Kähler-differential examples.

## An equivalent explicit test on universal algebras

This reformulation demonstrates the criterion's content without mentioning exponential-image membership on its right-hand side. All restriction/evaluation maps below are the existing maps of E.

### Ordinary map

Put P=K[t]. An ordinary action is uniquely determined by g=ρ_P(t)∈E(P)^×. The exact conditions on g to be an action are

\[
 g(0)=1,\qquad g(s+t)=g(s)g(t)\quad\text{in }E(K[s,t]).
\]

Here each expression is obtained along the indicated polynomial substitution. Indeed, for λ∈R naturality forces ρ_R(λ)=g(λ) via the unique map P→R,t↦λ; conversely these substitutions define a natural group action from the two identities.

For such g the exact ordinary-image test is

\[
 (g-1)^m=0\text{ for some }m,\qquad
 \log g=t\,\bigl((\log g)(1)\bigr)_P.
\]

Every term is specified ring arithmetic: a nilpotence test, a finite polynomial logarithm, evaluation at1, and scalar multiplication. The subscript P denotes restriction of the resulting element of E(K). If the test holds, u=(log g)(1) is nilpotent, because evaluation is a ring map and log g is a nilpotent polynomial in g−1. The inverse exp–log identity gives g=exp(tu_P); substitution supplies the required action everywhere. Conversely an exponential has both displayed properties. This proves the test and recovers its unique preimage. Hence the ordinary map is bijective exactly when **every unit g satisfying the two action identities passes these two algebraic tests**.

One universal nilpotence bound on g suffices for every R and λ by substitution. The test is in E(P), not merely End_P(M(P)); the latter weaker test would silently omit arbitrary further base extensions.

### Formal map

Put P_n=K[t]/(t^{n+1}), n≥0, and

\[
 B=\varprojlim_n E(P_n),\qquad
 D:E(K)\longrightarrow B,\quad D(u)=(t u_{P_n})_{n\ge0}.
\]

The limit uses restriction along the quotient maps P_{n+1}→P_n. It is a K-module and D is a specified K-linear map depending only on M.

A formal action is exactly a compatible family g_n∈E(P_n)^× with g_0=1 and

\[
 g_{i+j}(s+t)=g_i(s)g_j(t)
 \quad\text{in }E\bigl(K[s,t]/(s^{i+1},t^{j+1})\bigr)
 \quad(i,j\ge0).
\]

For any nilpotent λ∈R, choose n with λ^{n+1}=0 and substitute t↦λ in g_n. Compatibility makes this independent of n. The displayed law is sufficient because (s+t)^{i+j+1}=0 in that two-variable ring; it specializes to every pair of nilpotent elements. Conversely every formal action yields these identities by its naturality and group law.

The image test is now:

1. Each g_n−1 is nilpotent in E(P_n), with a bound allowed to depend on n.
2. The compatible family b=(log g_n) has **zero class in the explicit linear cokernel coker(D)**.

Nilpotence of all g_n−1 is equivalent to the original criterion's nilpotence at every (R,λ), by the same substitutions. Finite logarithms commute with restriction, so b belongs to B. If b=D(u), finite exp–log identities give g_n=exp(tu_{P_n}) and hence the prescribed action at every nilpotent scalar. Conversely an exponential gives b=D(u). The formal fibres are exactly the cosets of ker(D), and

\[
 \ker D=\{u:\lambda u_R=0\text{ for every }R,
                 \lambda\in\operatorname{Nil}(R)\}=H(M).
\]

This proves a fully explicit description of both obstructions: the family must admit its finite logarithms, and a specific **linear** obstruction class must vanish. Formal bijectivity is precisely injectivity of D and vanishing of these classes for every compatible unit family satisfying the displayed addition identities. This is not a claim that all elements of B must lie in im(D); imposing that stronger condition would change the answer.

The existing “O-linear extension” condition is equivalent to this cokernel test. An extension is determined by its value u at1 and gives exactly t u_{P_n}; conversely any solution of D(u)=b gives the extension λ↦λu_R. Thus the reformulation does not hide an extra existence hypothesis or weaken a quantifier.

## Why the obstructions are substantive

The existing reduced-ring example has H(M)≠0 and demonstrates a genuine injectivity failure. The existing R⊕Ω_(R/Q) action has square-zero differences but its logarithm is not the required scalar-linear extension, demonstrating a genuine surjectivity obstruction even when logarithms exist. The quasicoherent infinite-module example separates local nilpotence from the uniform nilpotence in the original ordinary domain.

Also, without adding any new premise, one can see that formal values need not automatically be unipotent: take M(R) to be the free R-module on the set Nil(R), with transition maps induced on basis elements, and let a nilpotent λ act by translation of that basis. This is a natural linear action. For R=Q[ε]/(ε²), the basis elements jε are distinct for all integersj. The coefficient of the basis vector mε in (ρ(ε)−1)^m applied to the basis vector0 is1. Thus no positive power vanishes. This symbolic infinite-basis argument is not a finite computational certificate and no finite test was run. It illustrates why the nilpotence condition cannot simply be deleted.

## Suggested exposition, not a reopened mathematical gate

The current statement is a satisfactory complete iff/image/fibre answer to the literal task. An unnumbered equivalent-universal-tests paragraph would make that completeness easier to inspect and remove the possible impression that “extends” simply restates the desired exponential representation. Its proof is the direct substitution argument above. No status change is warranted. A separate geometric or finite-presentation classification of all possible module functors is not an additional requirement found on044 or in C.1(d).

## Two local precision corrections identified

The proof before this audit said that exp(λu_R)−1 is “u_R times an invertible polynomial.” Literally that is false when λ is not invertible, for example λ=0 and nonzero nilpotent u. The exact identity is exp(λu_R)−1=λu_R q(λu_R), where q(0)=1 and q(λu_R) is invertible. The existing uniform-nilpotence conclusion follows immediately from this correct factorization; no conclusion or hypothesis changes.

The final logarithm-additivity sentence should describe the **nonunital** commutative subalgebra generated by the two commuting nilpotent operators, or the ideal they generate in the unital commutative algebra. If their powers of orders r and s vanish, every monomial of degree at least r+s−1 vanishes. A unital subalgebra itself need not be nilpotent. This is a wording repair of the finite polynomial-log argument, not an additional assumption. Both corrections were sent to the parent for coordination before modifying active TeX.

At the parent's explicit instruction, both precision corrections and the repeated standing Q-algebra hypothesis were applied; the universal-polynomial/truncated-polynomial explanation and its proof were inserted into the existing theorem's proof. The complete edit was reread in `sections/part_c.tex:207–345`, stable at16:51:41UTC. The theorem label, CSV row identity and mathematical status remain unchanged. No extra numbered result or review-movement claim was created.

## Actual program scope

The only new program was the source renderer `code/part_c_functor_audit_source_page.py`, rendering original PDFpage43 once. Start2026-11-19T16:46:04.899805UTC; measured internal elapsed0.48791543100378476s. Output: `code/part_c_functor_audit_source_page_output.json`. Zero network requests, zero mathematical finite/numerical checks. Original044 was viewed from its already-saved image. No prior certificate was rerun.
