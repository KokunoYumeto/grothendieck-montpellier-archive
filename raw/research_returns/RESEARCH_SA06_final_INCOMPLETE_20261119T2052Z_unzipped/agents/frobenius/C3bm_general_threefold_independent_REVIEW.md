# Independent full audit of C.3bm

Completed 19 November 2026 at 17:09:54 UTC. Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, run `/root/frobenius`; effort setting not exposed.

Reviewed the entire proposed `research/sections/C3_general_threefold_presentation.tex`, all four proof steps, both displayed quotients, and its final scope paragraph. **Full proof PASS.** This is an exact reduction, not a proof that the remaining quotient vanishes.

## Geometry and its field scope

The affine-cover projectivity clause of Cossart–Piltant, current arXiv v2 Theorem 1.1, author pp. 3–4, gives a projective regular modification preserving the regular puncture. This is a single simultaneous assertion; no improper conjunction of separate existence theorems is being used. On the regular resolution, the rank-one torsion-free pullback of the dual pushforward sheaf embeds in its invertible reflexive hull. The quotient ideal is the unit ideal on the puncture and at codimension-one points. Proposition 4.4, author p. 141, principalizes it by regular-centre blowups in the successive nonprincipal loci. Hence the resulting common model remains regular, projective, and unchanged over the puncture, and its invertible quotient gives the required map to the second Proj.

Kollár–Witaszek Lemma 8 applies directly to this actual common model. Birational maps satisfy its generically purely inseparable hypothesis with degree one, and the first regular model is locally factorial. The full reduced closed fibre has dimension at most two. Cossart–Jannsen–Saito Corollary 0.4 and its proof produce a regular projective embedded modification for which the entire reduced inverse image, not merely a selected exceptional locus, is SNC. Kollár–Witaszek Lemma 6 and the relative ampleness composition restore an ample Cartier divisor supported over the closed point. None of these arguments uses the residue field being algebraic over a finite field.

The normal Hartogs/global-generation argument fixes the sign and full support. The pushforward of the generated ample exceptional line bundle is a coherent ideal of the base ring under its rational-function trivialization. Its pullback equals that invertible subsheaf of the structure sheaf, so the negative of the exceptional divisor is effective. The ideal cannot be the unit ideal in the singular case: a trivial relatively ample bundle would force all projective fibres to be zero-dimensional, hence a finite birational map to a normal base would be an isomorphism. Thus it is primary to the closed point. Every exceptional divisorial valuation is then positive, giving all coefficients of D strictly positive. The regular-base case is separately handled by the ordinary point blowup.

The ample restriction to the reduced fibre E extends to the nilpotent thickening D by Stacks Lemma 30.17.5, Tag 09MS. This verifies the exact ample-conormal hypothesis of EL; it is not enough merely to have a nef conormal on the unweighted fibre.

## Endpoint comparison and indexing

The constructed data meet every hypothesis of the already independently audited EL and EP. The finite-model argument preserves the regular projective resolution and all finitely many perfect objects and cycle operations; smooth rational Chern-character identities therefore apply after descent. The point restriction identifies CH^2(Z)_Q with F_gamma^2 K_0(E)_Q. EL identifies the ordinary relation subgroup with actual proper-curve perfect-family endpoint differences on E. It does not claim that the whole perfect family extends to Z. Ordinary cycle localization and closure of actual cycle families give the first quotient exactly.

No proof step substitutes coherent G-theory for perfect K-theory on the singular exceptional surface. In particular, the definition of J_K retains all compatibility across double and triple strata.

## Degree-zero refinement

For a perfect family on E times a connected proper parameter curve, the degree of its ch_2 restriction to each smooth component is constant by proper pushforward and compatibility with the two refined fibres. Thus J_K lies in the componentwise degree-zero subgroup.

For C_j=H|E_j, the degree vector of its exceptional pushforward is the j-th column of M_ij=deg(E_i E_j H). Symmetry follows because H is the restriction of one line bundle on E; off-diagonal entries are nonnegative. Writing D=sum a_i E_i with all a_i>0, ampleness of -D gives Ma<0. The matrix diag(a) M diag(a) has nonnegative off-diagonal entries and strictly negative row sums. Its displayed quadratic identity is negative for every nonzero real vector, including when the incidence graph is disconnected. Hence M is invertible over Q. Exceptional cycles therefore remove every degree coordinate. Intersecting the exceptional image with S_0 gives exactly the second denominator; no implicit injectivity of the degree map is assumed.

## Primary-source checks actually performed in this audit

- Fresh local reread of the complete pertinent statements: Cossart–Piltant arXiv1412.0868v2, Theorem 1.1 and affine-cover clause, author pp. 3–4; Proposition 4.4 with its short proof, p. 141.
- Fresh local reread of Kollár–Witaszek arXiv2102.03162v1, Lemmas 6 and 8 and their complete proofs, author pp. 2–3.
- Fresh local reread of Cossart–Jannsen–Saito arXiv0905.2191v2, Corollary 0.4 and complete proof, author p. 5.
- Fresh web opening and full reading of Stacks Proposition 28.27.13, Tag 01Q3; Remark 31.17.2, Tag 0BCS; and Lemma 30.17.5, Tag 09MS, including its proof. Exact nilpotent-ampleness URL: <https://stacks.math.columbia.edu/tag/09MS>.
- EL and EP were fully audited separately in this run; their source dependencies are reused, not falsely described as freshly reopened in this particular audit.

The full resolution algorithms are cited primary inputs; no independent reproduction of those algorithms is claimed. No independent build or computation was run for this audit. The theorem remains confined to the explicitly stated algebraizable isolated normal threefold branch in positive characteristic. It neither closes the intrinsic SNC quotient nor extends to characteristic zero or unresolved higher-dimensional geometry.

