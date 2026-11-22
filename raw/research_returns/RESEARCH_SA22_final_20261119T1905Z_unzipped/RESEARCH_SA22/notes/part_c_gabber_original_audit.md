# Independent audit: original Gabber theorem and subject 21

Reviewer: GPT-6 Astra Pro, `part_c_algebra`, 19 November 2026, completed and reported at 15:20 UTC. **Outcome: passed.** This is an independent audit of the new original-source application in `thm:B3-21`, not a claim to have independently reproved Gabber's full rigidity theorem.

## Evidence actually inspected

I separately displayed and visually read both original publisher-preview images:

- `qa/part_b_gabber_preview_325.png`: title, journal/year, definition of a henselian pair and equivalent conditions (a), (b), (c).
- `qa/part_b_gabber_preview_326.png`: complete Theorem 1 and its surrounding qualifications, followed by Remark 1.1 and the beginning of Lemma 1.1.

The saved original is `sources/part_b_gabber_current_preview.pdf`, with text in the matching `.txt` file. The original printed pages are 325–326 of O. Gabber, *Affine analog of the proper base change theorem*, Israel J. Math.87 (1994),325–335. The public preview URL is `https://page-one.springer.com/pdf/preview/10.1007/BF02773001`; the precise historical advertised-link and current-host provenance is preserved in `notes/part_b_gabber_original_derivation.md`. Its recorded PDF hash is `400895d1ea24f5dee20df5e28e604b76468ab6d3c679c7fb20baa4523a94f519`.

I also read that complete derivation note and the integrated `thm:B3-21` proof and source-scope paragraph. No new source request or source-processing program was run for this audit. The existing images were actually displayed one at a time; the successful visual reading, rather than a tool placeholder or OCR alone, is the evidence for the inequality below.

## Original hypotheses and exact locator

Original Theorem 1 on p.326 says **every integer q≥0**. The lower bar is visible in the image; OCR which produces `q>0` is inaccurate. The theorem concerns every torsion abelian sheaf on the small étale site of `Spec A`, and the canonical restriction to `Spec(A/I)`, when `(A,I)` is a henselian pair.

The complete definition on p.325 starts with an arbitrary commutative ring `A` and an ideal `I`. There is no noetherian condition or finite-generation assumption on `I` in the definition or theorem, and there is no constructibility, local-constancy or prime-invertibility restriction on the torsion sheaf. Original condition (b) is the bijection `Idem(B)→Idem(B/IB)` for **every finite A-algebra B**. Original condition (a) explicitly includes `I⊂Rad(A)`.

The source itself distinguishes nontorsion coefficients immediately after the theorem. The current manuscript does not promote its briefly described nontorsion example into a separately proved counterexample, so that abbreviated discussion is not an unfilled proof dependency.

## Independent check of the full manuscript deduction

Write (i) for the henselian-pair condition, (ii) for the isomorphism in degree zero for every torsion abelian étale sheaf on `X=Spec A`, and (iii) for that isomorphism in every degree.

1. **(i)⇒(iii)** is exactly the original Theorem 1, p.326. The ring, ideal, sheaf category, coefficient restriction, map and quantifiers all match. No modern generalization is silently attributed to the original.
2. **(iii)⇒(ii)** is the instance `q=0`, which is explicitly within the original theorem.
3. **(ii)⇒(i):** for an arbitrary finite `A`-algebra `B`, let `f:Spec B→X` and take `F=f_* underline(Z/2Z)`. This direct image is killed by two and is therefore a permitted torsion abelian étale sheaf. The degree-zero proper-base-change theorem for the finite morphism identifies `i^*F` with the corresponding direct image on `Spec(B/IB)`. Global sections of the constant two-element sheaf are clopen decompositions and hence idempotents; this identification respects reduction modulo `IB`. Thus (ii) gives exactly original condition (b), p.325. Proper base change is an independent cited input; the argument is not a circular use of the henselian-pair theorem being characterized.

The Jacobson-radical qualification is also verified directly in the integrated proof. If a maximal ideal `m` did not contain `I`, then `B=A/m` would be a finite `A`-algebra with `IB=B` and `B/IB=0`. The distinct idempotents zero and one of the nonzero field `B` would become equal, contradicting the required injectivity. Thus no hidden assumption `I⊂Rad(A)` is missing.

The additional consequence about an I-adically complete ring is separately sourced to the opened henselian-pair lemma. It is not attributed to an extra hypothesis in Gabber's theorem. The fixed-sheaf counterexample uses `Gm_C`, its point `1`, and `Z/nZ` with `n>1`: degree-zero restriction is an isomorphism on the two connected schemes, while the Kummer torsor gives nonzero degree one on `Gm_C` and none on the point. The universal sheaf quantifier is therefore correctly retained.

## Prompt coverage and limitations

The prompt at line192 requires the subject21 derivation from Gabber1994 and Fujiwara1995; line231 lists the Gabber original among the required sources. It does **not** prescribe §5, Corollary1 as the only permissible locator. The opened complete main Theorem1 and p.325 criterion directly supply the needed Gabber input. Consequently the relevant Gabber original-source gate is closed by this passage and checked deduction.

The original full proof and the later §5, Corollary1 have not been opened, and no contrary claim is made. The complete modern proof in Stacks is a separately opened source. Fujiwara's completion-complement theorem is distinct and its original-source requirement is unchanged by the Gabber retrieval. This audit therefore closes no Fujiwara gate and makes no statement about an unseen original corollary.

No theorem text required correction. No finite mathematical program was run. The existing result ID is `B.3.21`; the evidence is an independent exact-hypothesis and proof-application check, not a routine computational rerun.
