# Targeted whole-proof challenge of NX-L02

Date: 2026-11-21T04:22:15+01:00 (Europe/Berlin). Reviewer: GPT-6 Astra Pro, inherited reasoning effort (runtime level not exposed), ZETA_NEXT `/root/cm_effectivity`.

**Type:** targeted proof check, consisting of two complete readings of NX-L02, checking the hypotheses of the cited analytic results, and separately reconstructing the local algebra, valuation/gluing argument, and the final integral-to-rational passage. This is not an independent re-proof of all cited perfectoid results and is not a formal certificate.

**Outcome:** no remaining mathematical gap found in the revised proof. The revision explicitly descends the constant formal model to the noetherian base Fp[[u]], proves the completed tensor is flat over O_C, and corrects two accidental TeX control bytes. I suggested one further explanatory sentence on principal-open rational localization; the existing preceding Witt-localization construction already gives that identification. The checked NX-L02 block SHA-256 was `5b621dc2cf5ea47e28ac66aa41a677cac67a8e0ee8bd7849c87e2303e3c1d9e8` (subsequent explanatory edits should be compared with this review).

## 1. Local strict-p construction

I checked that absolute Frobenius fixes the underlying topological space even when the special fibre is nonreduced. Consequently every formal affine open is invariant under inverse image; one need not assume that the generic endomorphism is injective, surjective, finite, or flat. On the affine ring A, the filtered colimit under the Frobenius lift is p-torsion-free, since multiplication by p is injective at each stage and filtered colimits are exact. For a p-torsion-free D, division by p^n identifies the kernel of the projection of its p-completion to D/p^n with p^n times that completion. This both preserves p-torsion-freeness and identifies its reductions. Thus the completed colimit is a strict p-ring with residue B=(A/p)^perf, giving W(B).

The precise source is Scholze, *Perfectoid spaces*, Proposition5.13(i) and Remark5.14, preprint p25: the remark identifies W(B) with the unique flat p-complete Z_p deformation of a perfect Fp-algebra. I read the proposition, remark, and their surrounding deformation statements. Perfection kills nilpotents; reducedness of A/p was not silently assumed.

## 2. Completed tensor and almost-flat hypotheses

W(B) is flat over Z_p, so its base change to O_C is flat. Its p-completion stays p-torsion-free. Every nonzero scalar of the rank-one valuation ring O_C divides a power of p; hence p-torsion-free implies torsion-free over O_C, which implies flat. I checked Scholze Definition5.1(ii), Theorem5.2 and Lemma5.3(i),(ii),(iv), preprint pp21–23: these are exactly the complete flat almost-integral hypotheses needed. Reduction modulo p gives B tensor_Fp O_C/p. Reduction modulo p^(1/p) is likewise the expected tensor quotient, since p-adic and p^(1/p)-adic completions agree. Frobenius is an isomorphism from the latter quotient to the former because it is invertible on B and has precisely that property on O_C. Thus the perfectoid assertion is supported by the theorem cited, without a hidden Noetherian or finite-presentation hypothesis on B.

The characteristic-p candidate is handled by the same argument with a pseudouniformizer of O_Cflat. Its reduction agrees under O_C/p = O_Cflat/pflat. The equivalence in Theorem5.2 then identifies the tilt. Choices of matching pseudouniformizers are only a way to verify a canonical, functorial identification; the resulting tensor/perfection construction itself is independent of that choice.

## 3. Plus rings and gluing

I read Scholze Lemma6.2 and Theorem6.3, preprint p30. The open integral closures used in the proof are legitimate plus rings. Modulo topologically nilpotent elements they are the integral closures of the same image of B tensor_Fp Fpbar. The reductions of D_B and its characteristic-p counterpart modulo the maximal scalar ideal agree: reduce modulo p (respectively pflat) first, then modulo the maximal ideal. Passing to the almost saturation does not change this image. Lemma6.2 identifies these plus rings under tilting; it is not enough merely to identify R and Rflat, and the revised proof addresses the stronger requirement.

Here is the open-domain check reconstructed independently of the prose. A principal formal open D(f) gives the rational analytic domain |f|=1, since f is integral and therefore |f|≤1. In W(B), f minus the Teichmüller lift of its residue lies in pW(B), so this domain is also |[bar f]|=1. Completing after localizing at f gives the strict p-ring W(B_bar f), followed by the same completed base change. The associated perfectoid space is therefore precisely an open rational domain of Spa(R_B,R_B^+). Finite principal refinements of overlaps glue as required. This also justifies the claim that the tilt is the perfected constant model, rather than only an unrelated space with isomorphic affine rings.

## 4. Tilde-limit topology and residue fields

For each fixed formal chart, the completed tensor R_B is the completion of the integral direct limit followed by inversion of p: this can be checked modulo p^n before completion, where filtered colimits and tensor products commute. A compatible system of points of the tower supplies compatible valuations bounded by the integral ring at every stage. They are bounded on its union, with p topologically nilpotent, and hence continuous for the common p-adic topology. A bounded continuous valuation extends to the completion; conversely restriction recovers the system. Integral closure of the plus ring imposes no extra valuation bound. Rational opens are determined by finitely many inequalities and therefore make this identification a homeomorphism. Density of the direct-limit rings gives the required density on residue fields, also after taking fractions.

I read Scholze Definition7.14, Remark7.15, Proposition7.16, Theorem7.17, and Corollaries7.18–7.19, preprint pp43–44. The spaces in the tower are qcqs noetherian adic spaces, and the maps are qcqs because the algebraic variety is proper. The above construction supplies precisely Definition7.14. Corollary7.18 therefore applies to each Z/ell^a coefficient sheaf. No surjectivity of the endomorphism has been assumed; for example the finite-flat mu_p test has a collapsing generic map and the tower correctly retains only the eventual image.

## 5. Constant tilt and Galois equivariance

I read Huber1994 Remark4.6(iv), printed p544. Its proper comparison assumes locally noetherian schemes. Applying it directly to a model over the nondiscrete O_Cflat would not match that formulation. The revised proof correctly first uses X_Fp times Fp[[u]], then base changes; the displayed completed affine rings commute with this base change. The comparison is natural, so the auxiliary choice of u does not affect the semilinear Galois equivariance.

The characteristic-p tower is the base change of relative Frobenius on X_Fp. Its maps are universal homeomorphisms and give purely inseparable extensions on residue fields, exactly the hypotheses of Scholze Corollary7.19. I also checked Theorem9.7, preprint p49 (Huber Theorem3.8.1), at statement level. Proper base change and algebraic--adic comparison then identify the finite-coefficient cohomology with that over Fpbar. Every construction commutes with automorphisms of C. Inertia acts trivially on the constant model's cohomology because its action on the residue field is trivial; the residual Galois action is the correct unramified action. No claim that inertia is trivial on the entire original generic cohomology is made.

## 6. Finite coefficients to the rational summand

I checked this full passage separately. For finite M/ell^a, sufficiently large powers T^(n!) equal the projector onto the eventual image: the transient part dies and n! is divisible by the finite order on the stable image. These projectors are compatible in a, hence produce an idempotent e on the complete finitely generated Z_ell-module M. The filtered colimit of M/ell^a under T is canonically its stable factor; when describing it through eM, the stage-j map is T^(-j)e on that factor. This makes compatibility and equivariance transparent.

After the universal-coefficient exact sequence and exact filtered colimit, the right-hand groups are uniformly killed by one power of ell because the torsion of M_(i+1) is finite. The left-hand transition maps are surjective, so their lim^1 vanishes. The inverse-limit sequence is therefore exact in the needed place, and inverting ell kills the remaining bounded torsion. The Galois group commutes with T and with its limiting projector. This proves a Galois-stable direct summand, not merely an equality of Betti numbers. The argument does not incorrectly interchange a filtered colimit with rationalization; such an interchange would fail for an ell-divisible eigenvalue, and the proof avoids it.

## Verification limits

This check covers the whole new NX-L02 proof and the hypotheses of the cited local/perfectoid comparison results. It does not independently re-prove the source theorems, proper base change, or Borger's generic-fibre theorem. The latter theorem is used only subsequently in NX-L03. No formalization was performed.

## Supplemental edited-block check

2026-11-21T04:31:40+01:00 — Read the final local edits in the plus-ring, principal-open, and valuation-completion paragraphs. The quotient is now precisely the scalar ideal m_C R_B^circ (and its tilted counterpart); the principal-open calculation agrees with the independent reconstruction above; continuity is explicitly tied to the common integral direct-limit ring. No mathematical defect found. These clarifications do not alter the other previously checked arguments. Final label-through-endproof SHA-256: `03598f1ba0ec6d7aa88eafeaa8785b3e147dc452021150a30625e319dfbf8961`, matching `lambda/proof_hashes.json`. This supplemental event is a targeted check of the edited passages, not a claim to have newly reread every source theorem.
