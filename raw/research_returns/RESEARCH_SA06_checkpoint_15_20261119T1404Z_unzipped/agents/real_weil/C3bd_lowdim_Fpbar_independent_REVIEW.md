# Independent review of C.3bd

**Current verdict, after substantive repair: PASS at 2026-11-19 12:31:59 UTC.** The initial review below is retained as history. Its Step 2 endorsement of a further projective resolution preserving the chosen open was too quick: parent identified that projectivity and regular-open preservation cannot be combined merely from separate existence statements. That inference was withdrawn. The owner replaced it with the explicit principalization argument described in the final addendum below, which has now passed a fresh full typed and primary-source check. The statement was not registered on the basis of the withdrawn inference.

**Outcome: full mathematical and targeted primary-source audit PASS.** Completion: **2026-11-19 12:25:18 UTC**. Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06 `/root/real_weil`; inherited effort setting not separately exposed. This is an independent agent review, not an independent-model claim or a re-proof of the cited resolution algorithms.

Read the complete `agents/frobenius/C3_lowdim_Fpbar_top_draft.tex`, its separate bibliography `C3_lowdim_Fpbar_references.bib`, and the retained standalone build program and JSON. No mathematical correction is requested. The statement is restricted to the algebraizable normal strict-local germs described in the theorem, over the algebraic closure of a finite field, in local dimensions two and three. It proves rational top Chow vanishing, hence its ordinary quotient vanishes, in every positive characteristic. It does not assert a higher-dimensional resolution theorem.

## Proof check

1. Strict henselization preserves the excellent normal local hypotheses and the specified residue field. A regular source is handled by its ordinary blow-up: the exceptional projective space is smooth and its negative divisor is relatively ample, so C.3bc applies directly.

2. For a singular closed point, the regular-open preservation is explicit. In Kollár–Witaszek's construction the first resolution preserves the regular puncture; the rank-one sheaf is invertible there, so its Proj modification is the identity there; the dominating fibre-product component has the same open; the final regular resolution is chosen to preserve that open. The projectivity issue on schemes over an affine base is supplied by their Corollary 3 and proof, rather than being silently inferred from local projectivity in the Cossart–Piltant theorem alone.

3. The reduced exceptional locus has dimension at most two. Cossart–Jannsen–Saito Corollary 0.4 applies to this reduced closed subset of the regular excellent ambient scheme and produces a regular projective modification, an isomorphism outside the subset, whose complete reduced inverse image is SNC. The proof of that corollary also gives regularity of the new ambient scheme. This avoids an invalid assumption that an arbitrary composite of log resolutions automatically preserves all previous SNC data.

4. The intermediate regular scheme is locally factorial and hence satisfies the Q-factorial hypothesis of Kollár–Witaszek Lemma 6. It gives an ample exceptional divisor for the second morphism. Adding a sufficiently large pullback of the first relatively ample divisor gives a divisor ample for the composite, supported over the closed point. This is the same relative-ampleness composition used in their Lemma 8.

5. The sign is proved, not assumed. For a large positive integer n, global generation of O(nF), together with normal Hartogs, embeds I=f_*O(nF) as a coherent ideal of R. Its generated image is exactly I O_Z=O(nF) inside the common rational function field; since I consists of regular functions, this fractional invertible ideal lies in O_Z. Thus -nF is effective. If I=R, the relatively ample bundle is trivial, forcing all projective fibres to be zero-dimensional. Proper quasi-finiteness makes f finite; finite birationality to normal R makes it an isomorphism, contradicting the singular closed point. Therefore I is proper and m-primary. Its pullback vanishes precisely on the whole closed fibre, so every SNC exceptional component occurs with a strictly positive coefficient in -nF. The restriction nF|_E is ample. These are exactly the hypotheses used in C.3bc.

6. The application of C.3bc is now legitimate with d=N-1. Our earlier complete independent audit of C.3bc is retained separately. No conclusion over an arbitrary transcendental algebraically closed field, no integral finiteness claim, and no higher-dimensional resolution assertion is added.

## Primary sources freshly opened and read

- **Cossart–Piltant:** full current 320-page author PDF, arXiv:1412.0868v2, 8 January 2019, <https://arxiv.org/pdf/1412.0868>. Read Theorem 1.1, author pp. 3–4, including regular-locus preservation, strict normal-crossings inverse image and affine-cover projectivity; read Remark 1.4. No independent audit of the entire 320-page resolution algorithm is claimed.
- **Kollár–Witaszek:** full four-page author PDF, arXiv:2102.03162v1, 5 February 2021, <https://arxiv.org/pdf/2102.03162>. Read Theorem 1, Corollary 3, Lemmas 6–8 and proofs §§9,12. These are author-version locators. The owner's published metadata is distinguished from the author PDF actually inspected in this review.
- **Cossart–Jannsen–Saito:** full 169-page author PDF, arXiv:0905.2191v2, 18 February 2013, <https://arxiv.org/pdf/0905.2191>. Read Theorem 0.3 and Corollary 0.4 with its complete proof, printed author pp. 3–5. Corollary 0.4 permits any-dimensional regular excellent ambient scheme and a reduced closed subscheme of dimension at most two.
- **Stacks, Proposition 28.27.13(7), Tag 01Q3:** <https://stacks.math.columbia.edu/tag/01Q3>, full statement and proof freshly read. It provides eventual global generation for powers of an ample invertible sheaf on this quasi-compact separated scheme.
- **Stacks, Remark 31.17.2, Tag 0BCS:** <https://stacks.math.columbia.edu/tag/0BCS>, full remark freshly read. It gives normal Hartogs on a punctured local spectrum of dimension at least two.

## Program and document scope

Read `code/build_lowdim_Fpbar.py` and `output/C3_lowdim_Fpbar_build.json`. The recorded owner run started 2026-11-19T12:24:25.366411+00:00, took **2.996580011000333 seconds**, had four zero return codes, no recorded warnings, and produced a three-page 106492-byte PDF. This is document verification only. I did not independently rerun it, and no finite computation is substituted for the geometric proof.

## Final addendum: simultaneous projectivity and puncture preservation

The owner rewrote the first construction in `C3_lowdim_Fpbar_top_draft.tex`. I read the entire replacement and the unchanged remaining proof, completing the new audit at **12:31:59 UTC**.

Apply Cossart–Piltant Theorem 1.1 only to the affine base S. Its projectivity and regular-locus clauses then hold simultaneously, giving the regular projective Z1/S unchanged over the puncture U. For a relatively ample H1, take L1=(pi1)_*H1 and L2=Hom(L1,O_S), as in Kollár–Witaszek. Over U the first map is the identity and L1 is a line bundle. The second Proj is also unchanged there.

Let M be the torsion-free quotient of pi1^*L2. The regular scheme Z1 is locally factorial, so its rank-one reflexive hull M** is invertible. The inclusion M into M** defines a coherent ideal J=M tensor (M**)^(-1). It is the unit ideal on U and at every codimension-one point: over a DVR a finite torsion-free rank-one module equals its double dual.

For dimension three, **Cossart–Piltant Proposition 4.4, printed author p. 141**, principalizes a nonzero ideal on a regular excellent threefold by finitely many blow-ups in regular integral centres contained in the locus where the successive total ideal is not locally principal. I freshly opened and read this exact statement and its short proof in the current v2 primary PDF. Every centre therefore lies outside U, and the resulting scheme remains regular and projective over Z1.

For dimension two, the support of O/J is a finite set of closed codimension-two points, all over the closed point of S. **Stacks Lemma 54.4.1, Tag 0AHH**, gives principalization by point blow-ups over that finite set. I freshly opened and read its full statement and proof at <https://stacks.math.columbia.edu/tag/0AHH>. Its regular-local-dimension-two hypotheses hold at every point in the support.

After principalization, the pullback of L2 has the invertible quotient J O_Z0 tensor the pullback of M**. The Proj universal property gives Z0 to the second Kollár–Witaszek modification. Thus the regular projective Z0, unchanged over U, directly dominates both required modifications; **Kollár–Witaszek Lemma 8** supplies the ample exceptional divisor without resolving any new nonaffine fibre-product component. This is the missing conjunction, now proved by the explicit construction.

The owner also sharpened the next paragraph to embedded-resolve the **entire reduced closed fibre**, rather than an ambiguously narrower exceptional locus. Cossart–Jannsen–Saito Corollary 0.4 applies exactly to that subset. The relative-ampleness and Hartogs/m-primary sign proof then proceeds as already checked. No further mathematical correction is required.

The earlier build timing above belongs to the earlier document version. It is not a claim that this revised text was independently compiled by me; the owner is responsible for its new retained build.
