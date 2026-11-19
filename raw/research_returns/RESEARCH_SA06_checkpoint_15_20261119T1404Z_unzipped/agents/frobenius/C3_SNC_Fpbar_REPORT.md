# C.3bc: rational top Chow vanishing for SNC resolutions over Fpbar

Finalized 19 November 2026 after full independent proof and primary-source audits by root and real_weil. This is a restricted theorem: existence of the indicated regular projective resolution and of a positive exceptional combination with ample negative restriction remains an explicit hypothesis.

## 1. Exact result

Let R be the strict henselization at a closed Fpbar-point of a normal local ring essentially of finite type over Fpbar, of dimension d+1, d≥1. Let Z→Spec R be regular, projective, birational, and an isomorphism away from the closed point. Let the reduced exceptional fibre E=∪E_i be SNC, and suppose D=Σa_iE_i has all a_i>0 and −D|E ample. Then restriction followed by degree is an isomorphism CH^d(Z)_Q→Q^{number of components}; CH^d(Z−E)_Q=0. Consequently its ordinary quotient B^d is also zero rationally.

The proof does not identify algebraic equivalence conventions, does not lift proper families from a reducible exceptional fibre, does not compare K with KH, and does not assert resolution in arbitrary dimension. It gives no integral vanishing or extension to an algebraically closed field transcendental over Fp.

## 2. Proof and the exact source-scope correction

On a smooth m-dimensional stratum, Levine's rational comparison identifies the Adams weight w of K_n with CH^w(−,n). We use the published Theorem3.1, pp276–278. Above w=m+n there are no degree-n cycles. At w=m+n every degree-n cycle is a point of the cube over a k-point of the stratum; proper pushforward therefore gives a surjection from the direct sum of CH^n(k,n). Totaro's Theorem1, p181 identifies these field groups with Milnor K_n(k), which is torsion over Fpbar for n>0. Smooth projective CH0_Q is Q by degree, using curves through pairs of points and torsion of their Jacobian points.

For a union V=A∪B of SNC components, Geisser–Hesselholt TheoremC, printed p30 gives excision for the closed-union Milnor square after inverting p. Thomason–Trobaugh Theorem8.1, p367 patches it on finite affine covers. The resulting connecting map preserves the ordinary Adams weight, with no support or Thom shift. The precise source is the paragraph BEFORE Levine's Lemma2.1 on p258, which explicitly describes Grayson's construction for arbitrary schemes, iterated homotopy fibres, and delooping. The statement of Lemma2.1 itself has a regular-ambient hypothesis; we use only the elementary generalized-eigenspace module argument in its proof on p259. The final fragment states this distinction explicitly. Parent and peer freshly inspected that page.

An induction on dimension and component number then proves K_0(E)_Q^(d)=⊕CH0(E_i)_Q=Q^c. In the induction the predecessor K_{n+1}(A∩B) has exactly top weight (m−1)+(n+1), so it vanishes; this is the critical index calculation.

KST TheoremA and equation(1.6), author pp2–3, supply a finite detecting thickening for K0(Z). The constant-group kernel system has inclusion transition maps, so its being pro-zero implies an actual finite zero kernel. GH TheoremA, p29 and finite affine descent identify that thickening rationally with E. Smooth pointed-étale model descent and Fulton's rational Chern ring comparison, Example15.2.16(b), pp294–295, then inject CH^d(Z)_Q into Q^c.

For an ample H on E, take the exceptional curves C_j=H^{d−1}[E_j]. Their component-degree matrix M is symmetric, has nonnegative off-diagonal entries, and satisfies Ma<0. Conjugating by diag(a) makes every row sum negative, and the exact quadratic identity proves negative definiteness. Thus these exceptional curves span every component-degree vector. Localization kills all of CH^d(Z)_Q on the puncture.

## 3. Independent checks and execution record

The real_weil full independent proof/source PASS is timestamped 12:06:00.083550UTC; its detailed review is research/agents/real_weil/C3bc_SNC_Fpbar_top_independent_REVIEW.md. Parent's preliminary targeted check was received before the tool clock12:07:00UTC; its final full certification is timestamped12:12:36.242839UTC. Parent also read the separate energy lemma, its program and entire JSON without claiming a rerun. The energy lemma is not needed for this shorter component-degree proof.

The mathematical text compiled by four LuaLaTeX/BibTeX passes starting 12:05:46.712431UTC, runtime3.346874491s, four pages146550bytes. After final filename promotion and the explicit bibliography-scope correction, the final-path build started12:13:15.416834UTC and took3.016476542s, producing four pages146904bytes. Every return code was zero and there were no warnings or over/underfull boxes. The executable builder and exact current output are code/build_SNC_Fpbar.py, output/C3_SNC_Fpbar_build.out and output/C3_SNC_Fpbar_build.json. No bounded numerical calculation is being substituted for this proof. Parent's final source certification is recorded at12:12:36.242839UTC in notes/ROOT_C3bc_SNC_FPBAR_AUDIT.md.

The primary-source acquisition script code/acquire_SNC_top_sources.py and output/acquire_SNC_top_sources.json retain original start times, durations, sizes and SHA256 hashes. The published Levine PDF is 5491369bytes, SHA256 5f4de92e51f03dfb9a4708f70ed9a8f58d2c2a51e310eeb4d597be84c7450984; the Totaro PDF is773722bytes, SHA256 3447b12c9108d37528d998376051d7e60f0461584f61c1e980bdaa46ada43aee. Actual acquisition durations were99.769088048s and9.008752825s, concurrently, not estimated. Images of Levine's printed pp258 and276 were inspected.

## 4. Focused literature comparison and remaining research

We opened Binda–Krishna, Zero-cycle groups on algebraic varieties, current arXiv2104.07968v2 (11January2022), Theorem1.6 and Corollary1.7, author pp4–5. These compare normal-crossing Levine–Weibel Chow groups and motivic cohomology, and construct refined restrictions after the specified coefficient changes. We do not replace their current statement by the broader wording of the earlier version. They are neighboring results, not an asserted proof of our strict-local theorem.

We also opened Burke–Popa–Shen, Negative K-theory and Hodge theory (15September2026), Theorem9.1, pp28–31, and Lemma13.1, p40. The former concerns complex projective isolated klt threefolds, with stated Bloch-conjectural rational-singularity and additional LCI refinements; the latter concerns algebraic semilocal models and compactifications. Neither supplies invariance under henselization/completion or a positive-characteristic SNC family-lifting theorem. The separate SNC research note records their exact limitations.

These searches support no originality or priority claim. The next main question is whether rational alteration or ldh methods can replace the assumed resolution. A generically finite alteration is not an abstract blow-up that is an isomorphism off the closed point, so the KST constant-group finite-detection argument cannot simply be reused. A low-dimensional resolution corollary needs a precise existence theorem and an actual positive exceptional combination with ample negative restriction.
