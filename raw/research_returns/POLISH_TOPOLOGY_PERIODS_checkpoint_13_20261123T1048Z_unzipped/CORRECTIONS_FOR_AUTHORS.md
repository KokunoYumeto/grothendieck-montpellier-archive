# Corrections for authors — research records, not messages

No author has been contacted. Each item is limited to the consulted version and locator. Corrections of external statements stay outside the research papers.

## CORRECTIONS_FOR_AUTHORS_paper02_Elliott.md

# The two conjectured nonflat integer-valued polynomial modules

Recorded 2026-11-23. GPT-6 Astra, ChatGPT Pro mode; numerical effort not exposed. No human has checked this note and no author has been contacted.

## Exact consulted version and claim

Jesse Elliott, *Presentations and module bases of integer-valued polynomial rings*, arXiv:1109.3921v1, introduction, printed p.2. The consulted21-page PDF displays the arXiv date19September2011 and the internal date8March2021. Its introduction records conjectured nonflatness of Int(D) over D for D=F_2[[T^2,T^3]] and D=F_2+TF_4[[T]], and describes that conjecture as open. Root reopened and read this exact paragraph on23November2026. This note is restricted to the consulted statement; it does not assert that every later publication has identical wording.

Source: https://arxiv.org/pdf/1109.3921. Downloaded304601bytes; SHA-256 c144fb04cca2f04acbac2a69760e8ee73b9a323d68e6e8e4dcd228e290611795. Pages used: title/internal version p.1 and introduction p.2. The primary PDF remains outside the returned files.

## Opposite conclusion and proof

Both displayed modules are projective, hence flat, by the complete finite-conductor argument in Paper2, Theorem12.2 (label result-29), pp.46–47 of the reviewed85-page version, specialized explicitly in Corollary15.5 (result-51), p.60. That theorem assumes a discrete valuation ring V with finite residue field and a unital subring R containing a power t^mV. It proves projectivity of Int(R) over R; it includes finite residue extensions and arbitrary conductor gaps. Its proof constructs the Newton interpolation module, the finite congruence-value pullback, and an explicit infinite-rank patching stabilization. Its preceding Lemma12.1 (result-28) proves the required projective pullback by column-finite elementary matrix lifts, rather than assuming finite generation of the polynomial module. The complete proofs are in the standalone paper.

For the first ring take V=F_2[[t]], m=2 and R=F_2+t^2V. Every integer at least2 is a nonnegative combination of2 and3, so R=F_2[[t^2,t^3]] exactly. For the second take V=F_4[[t]], m=1 and R=F_2+tV. In either case t^mV is contained in R, the residue field of V is finite, and V is a discrete valuation ring. The fraction field of R is that of V: v=(t^m v)/t^m for every v in V. All hypotheses of the finite-conductor theorem are therefore met. It follows that Int(R) is projective. A projective module is a direct summand of a free module; tensoring the split summand decomposition proves that it is flat. Thus neither ring gives the conjectured nonflat example.

The counterargument is not an inference that a sufficient condition has failed, and is not based on a finite calculation. It is the positive projectivity proof at the exact two examples. Both have one normalization branch. The separate two-branch counterexamples discussed elsewhere do not alter this conclusion.

## Review and routing

The finite-conductor and patching proofs received the full targeted source/current audit; the positive classification direction also has the separately frozen reconstruction recorded in paper02_B054_blind_attempt_register_agent.md. Root's exact-scope disposition is paper02_root_scope_review_081.md. The reviewed TeX hash isc90f73931c189e3208cfbf3f21ab1691d9de3f152de397f8fad13ede95fc56cf. These locators match the released85-page build of2026-11-23T09:51:18Z.

The explicit published-conjecture correction is routed to this record. The general projectivity theorem, its two positive examples and neutral source credit remain in the research paper. The released85-page revision removes the explicit corrective wording after complete visual QA of the affected pages. No external notification or claim of priority is made.


## CORRECTIONS_FOR_AUTHORS_paper03.md

# Specialization issue in a consulted Bhowmik–Pathak preprint

Prepared 23 November 2026 by GPT-6 Astra in ChatGPT Pro mode. No human has checked this note. It has **not been sent to the authors**. This material is excluded from Paper 3.

## Version and precise claim

Tapas Bhowmik and Siddhi S. Pathak, *A note on transcendence of special values of functions related to modularity*, arXiv:2408.00271v1 (1 August 2024), Theorem 1.11, p. 3; proof in §3.5, pp. 17–18. The author's currently available 18-page copy has the same statement and proof step. Both complete PDFs were fetched and read in this preparation:

* https://arxiv.org/pdf/2408.00271v1 — SHA256 `58604953a3679a03b781eb5d267af16b2ffe89aeac85c24fe9223f8edcf51a20`.
* https://www.cmi.ac.in/~siddhi/TranscModFn.pdf — SHA256 `f2e14bf53aad20cf8fd83b0fa3607954d972d0e7da4b8b582f04449461395273`.

The theorem asserts a lower bound of three for the transcendence degree of the field generated by q=exp(2πiτ), a nonconstant modular form f(τ), a nonconstant modular function g(τ), and a nonconstant positive-depth meromorphic quasimodular expression F(τ), with algebraic Fourier coefficients. The stated specialization conditions exclude poles and require f(τ) and F(τ) to be nonzero. They do not require a positive-depth coefficient to remain nonzero after evaluation.

The journal publication is *Acta Arithmetica* **218** (2025), 1–23, DOI https://doi.org/10.4064/aa240128-7-9. The official metadata page was opened. Its download link redirected to the publisher's homepage; the journal PDF was not obtained. **This note confirms a problem in the two consulted preprint copies; it does not assert that the published 23-page version has identical wording.** Before sending any correction, the final published text and any erratum should be compared by someone with access.

## Exact counterexample

Take τ=i, f=E4, g=j, and

\[
F_0=1+\frac{E_2E_6}{E_4^2}.
\]

This version has weight zero and depth one, so it also accommodates a restrictive reading of the word “function.” Its coefficient E6/E4² is a nonzero meromorphic modular form of weight -2. All Fourier coefficients are rational. The first terms of the normalized Eisenstein series are E2=1-24q+…, E4=1+240q+…, E6=1-504q+…, giving F0=2-1008q+…; hence it is nonconstant.

At the fixed point i, the weight-six transformation under τ↦-1/τ gives E6(i)=i⁶E6(i)=-E6(i), so E6(i)=0. The identity E4³-E6²=1728Δ and the nonvanishing of Δ in the upper half-plane give E4(i)≠0 and j(i)=1728. Every required value is finite, f(i)≠0, and F0(i)=1≠0. Nevertheless

\[
\overline{\mathbf Q}(e^{-2\pi},E_4(i),j(i),F_0(i))
=\overline{\mathbf Q}(e^{-2\pi},E_4(i)),
\]

whose transcendence degree is at most two. No numerical approximation or unproved transcendence assertion is needed.

The source's weight-four alternative F4=E4+E2E6/E4 also works under the wider usage of “quasimodular function”: F4=2-528q+…, F4(i)=E4(i)≠0. The new certificate program checks both first coefficients by exact arithmetic. The weight-zero version above avoids dependence on this terminology.

## Where the proof needs an additional condition

The displayed argument in §3.5 first proves algebraicity of the four chosen values over the field of q,E2,E4,E6, and then asserts equality of transcendence degrees. That first algebraicity statement proves only one inequality. Recovering E2 from a quasimodular expression requires its specialized polynomial in E2 to have positive degree. Positive depth as a function does not ensure this: in the example, every positive-depth coefficient vanishes at i. The additional nonvanishing of the whole expression does not prevent that collapse.

## A sufficient repaired statement

Let f be a nonzero meromorphic modular form of integer weight k≠0, g a nonconstant modular function, and F=Σ(r=0 to d) f_r E2^r, where f_r has weight w-2r. Work on a common congruence subgroup and assume algebraic Fourier coefficients. At τ require f,g,and all f_r to be finite, f(τ)≠0, and **at least one f_r(τ)≠0 for r≥1**. Then the field of q,f(τ),g(τ),F(τ) and the field of q,E2(τ),E4(τ),E6(τ) have the same transcendence degree. Nesterenko's theorem gives the lower bound three.

Here is a proof of the equality, independent of the failed specialization step. A nonconstant function g on the compact modular curve gives a finite morphism to the projective line. Consequently every modular function finite at τ has value algebraic over Qbar(g(τ)). This applies also at a transcendental value, through the residue-field extension at the generic point. Put δ=Δ(τ)≠0. The finite nonzero modular function f^12/Δ^k has algebraic value over that field, and k≠0 implies that δ is algebraic over Qbar(f(τ),g(τ)). The same field contains j(τ), E4(τ), E6(τ) algebraically, using E4³=jδ and E6²=(j-1728)δ. For each nonzero f_r(τ), the ratio f_r^12/Δ^(w-2r) shows that f_r(τ) is algebraic over this field; zero values need no argument. The polynomial Σ f_r(τ)X^r-F(τ) is nonconstant by the additional hypothesis and vanishes at E2(τ). Thus E2(τ) is algebraic over the chosen-value field. Conversely the finite morphism j and the same weight-ratio identities make f(τ),g(τ),and all f_r(τ) algebraic over Qbar(E4(τ),E6(τ)); adjoining E2 recovers F. Adjoining q preserves the equality of transcendence degrees.

This is a sufficient repair, not a claim of minimal hypotheses or priority. The lower-bound input is Y. V. Nesterenko, *Modular functions and transcendence questions*, *Sbornik: Mathematics* **187** (1996), 1319–1348, Theorem 1, p. 1320, DOI https://doi.org/10.1070/SM1996v187n09ABEH000158. The repair does not replace E2 by its nonholomorphic completion E2*. In particular it supplies no proof of the unresolved elliptic Hodge-splitting converse.


## paper07_event_domain_prefetch_correction.md

# Pre-comparison correction to the refinement example

Date: 2026-11-23T05:38:54.256543+00:00

The BM-domain and BM-refinement target proofs remain unread. The frozen note incorrectly called At13 vacuous without excluding the empty refinement. The correction is elementary: for nonzero P the premise is impossible, as written; for P=0 and F nonzero, choose the witness H=F itself, which refines F, is disjoint from 0 and is not disjoint from itself. If F=0 there is no witness premise. Thus both explicit models do satisfy At13. No change to the complete BM-domain proof or the declared partial refinement scope is needed. The original frozen file is preserved unchanged.

