# Independent full audit of WP.1–WP.8

**PASS in the exact fixed-local-base and smooth-proper-curve scope stated by the owner.** This is an auxiliary whole-family lifting theorem. It does not prove a new component-family generation assertion, specialization theorem, or main-gate reduction.

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, `/root/cycles_continuation`; effort setting not separately exposed. No priority claim.

Reviewed in full: `../frobenius/C3_whole_proper_top_family_RESEARCH.md`, SHA256 `fcb19e667d8060364c37a7749faf6393ff4d485c346ba1ddbcf43d1ce9969478`. Freshly reread the entire determinantal, geometric flag, algebraization, and endpoint proof in C.3bn/AE.1–AE.10; reread the entire fixed-product obstruction proof FF.1–FF.4 and the previously complete cycles AE audit. No numerical program was run or needed.

## 1. Admissible finite schemes retain the required nilpotent structure

An admissible F is an actual regular immersion of length d+1 in T=D×P. Independence on the smooth reduced top stratum is an additional condition, not a replacement of F by its reduction. A split rank-d subbundle of I_F/I_F² can be chosen by the first-jet construction: the matrix rank-defect has codimension two and the support of F is finite. Nakayama on F upgrades reduced full rank to a locally split subbundle. Locally completing those d generators to a basis of I_F/I_F², and then applying Nakayama to the ideal, gives a regular-sequence generating set of I_F whose first d members are the flag equations. The remaining member cuts F as a Cartier divisor on H. This reasoning retains the thickness inherited from D.

Away from F, the same finite smooth stratification and prefix transversality used in AE apply. The flag has d independent ambient differentials at every point of its closed fibre, including any lower-dimensional strata it meets. It therefore cuts a regular surface there. The failure of regularity, failure of expected local codimension, and unwanted components are closed conditions on a scheme proper over the original local base. Any nonempty such closed subset has image containing the closed point. Hence these failures do not occur anywhere. The equation of D is a nonzerodivisor on this regular surface because the flag intersection with the full closed-fibre support has dimension one; no surface component is contained in it.

The restriction H is consequently a possibly nonreduced Cartier curve on W. The ideal of H and the maximal-ideal-adic ideal have the same support, hence cofinal powers on the noetherian proper W. No assumption that W dominates the local base, or that its fibres over P are globally flat, is needed.

## 2. The finite-class lift is integral and is an equality in perfect K0

The underlying noetherian topological space of H has dimension one, so H² of every coherent sheaf on H vanishes. In particular it vanishes for every J^n/J^(n+1), without an eventual-vanishing qualification and without any loss caused by nilpotents. The square-zero unit sequence lifts O_H(−F) at each successive thickening with no tensor power.

The same actual finite-jet algebraization argument as AE.9 applies: proper existence over the completion, algebraization of the inverse, descent to a smooth R-algebra, and henselian lifting of the specified R/m^M point for m^M O_W⊂J preserve the restriction on the entire H. They yield an actual line bundle Q on the fixed W. No modification of the parameter, ambient product, or local base is retained.

Since H is Cartier on W, pullback of j:W→Z×P along the Cartier inclusion T→Z×P is Tor-independent. Both j and its base change are regular immersions. The projection/base-change identity therefore gives

    (j_*(1−[Q]))|T = i_*(1−[O_H(−F)]) = [O_F]

in perfect K0(T), integrally. The final identity is the actual Cartier exact sequence. It is valid for the nonreduced F and H. A Cartan map, a gamma-pushforward formula, or a comparison with coherent G0 is unnecessary.

## 3. The entire gamma-(d+1) tail is covered

The previously proved AE reduction handles all products of gamma operations on virtual classes by writing virtual bundles as differences of sufficiently positive equal-rank bundles. Replacing total degree d by n=d+1 preserves this argument. The Eagon–Northcott perfect identities are exact before passing to the next gamma term.

For total codimension n, the degeneracy intersection is finite and misses every lower-dimensional stratum. Its deeper rank incidence has codimension n+i_a+2>n, so no deeper rank locus meets it. The surviving defining functions have independent differentials on the smooth top stratum. Cohen–Macaulayness and the local block reduction give an actual regular sequence on the nonreduced T, and the tensor product of the perfect resolutions is its structure sheaf. Thus the generators really are admissible F, not merely their associated zero-cycles. The rational dimension bound F_gamma^(n+1)=0 completes the generation of the entire tail.

## 4. WP.4 is an exact perfect identity on the curve

For a line bundle M on the projective Cohen–Macaulay curve C, high twists of M and O_C have sections avoiding its associated points and the finitely many bad points. Their restrictions to the smooth reduction can have simple zeros. Thus F_+ and F_- are actual effective Cartier divisors supported in the good locus, with the multiplicities inherited from C retained.

The two exact sequences 0→O_C→O_C(F_±)→O_(F_±)(F_±)→0 give the difference formula after twisting by A^(−N). Every line bundle on either finite Artinian scheme is free of rank one: choose a simultaneous residue basis by the Chinese remainder theorem and use Nakayama at every maximal ideal. Hence all the twists on the finite classes disappear in perfect K0(C), proving

    [M]−1=[O_(F_+)]−[O_(F_-)].

The composite immersion F_±→C→T is regular. Its defining d curve equations, followed by the transverse Cartier section, have d+1 independent differentials at the good reduced support. It is therefore admissible for the integral finite-class lift. This checks the additional condition needed in WP.4 rather than assuming that every finite scheme is admissible.

## 5. Whole-family base change and exact curve correction

For an AE curve C, the section W has dimension three and H=W∩T is Cartier. The entire square with T is Tor-independent because its one Cartier equation remains a nonzerodivisor on W. This condition does not depend on endpoint flatness. Thus the integral class b_C restricts on all of T to the sum of the a successive Cartier twists on C in WP.5.

Subtracting a[O_C] leaves only the finite sum of pushed-forward line-bundle differences on C. Section4 expresses each one exactly as a sum of admissible finite classes; Section2 lifts each of those integrally. Subtracting their lifts yields the literal equality (b_C−c_C)|T=a[O_C]. Division by the finite p-power a is legitimate in the rational theorem. Together with the already lifted top tail, this proves WP.1 for the prescribed class on the entire product.

## 6. The low-dimensional full-K0 consequence is justified

For d=2, first lift ranks through the point isomorphism FF.4. After clearing a common denominator, the remaining rank-zero class has a determinant line bundle on T. Applying the AE.8–AE.9 argument with W=Z×P and H=T is valid: O_D(−D) is ample on every fibre over P, relative Serre vanishing removes higher direct images for high powers, and the proper curve P has coherent cohomological dimension one. Thus H² of those high powers vanishes. The finitely many previous obstruction groups are killed by p, giving a finite power of the determinant that lifts.

A rational multiple of the lifted line-bundle difference gives the correct determinant modulo F_gamma². The rank-and-determinant description of K0/F_gamma² then leaves precisely a class covered by WP.1. This simpler argument suffices; existence of an actual line-bundle root is not needed. For d=1, lifting ranks and F_gamma¹ proves the same full surjectivity. Nilpotent invariance after rationalization transfers the conclusion between D×P and E×P as in AE.

FF.1 is an exact fixed-product cokernel statement and its proof keeps K0(Spec R×P). Combining it with the just-proved surjectivity gives K_(-1)(Spec R×P)_Q=0 for d≤2. This uses no extension of Drinfeld's henselian-local theorem to a nonlocal product.

## 7. Source-read receipt and exact limitation

Freshly opened and read the complete statement and displayed proof of The Stacks Project Authors (2026), *Grothendieck vanishing*, Proposition20.20.7, Tag02UZ, https://stacks.math.columbia.edu/tag/02UZ . Freshly read Lemma10.78.7, Tag02M9, https://stacks.math.columbia.edu/tag/02M9 , including the source's explicit indication that the proof is omitted and its CRT/Nakayama hints; the elementary rank-one proof was independently reconstructed above. Freshly reread the complete statement and proof of Lemma37.4.1, Tag0C6R, https://stacks.math.columbia.edu/tag/0C6R . Retrieval references are turn552520099view0, view1, and view2.

The complete earlier AE, FF, determinantal, gamma-filtration, formal-existence, approximation and perfect-base-change audits are reused at their exact already-checked scopes. In particular, the full TT3.14–3.18 source proofs and their supported version were freshly read earlier in this continuation for HK. No fresh complete reread of all KST, GH, Drinfeld, Popescu or Grothendieck-existence originals is claimed in this receipt.

The theorem uses the actual local R and the actual fixed smooth proper P. A transcendental scalar extension R⊗k k(u) need not remain local or henselian; a subsequent localization would change the product. Neither that replacement nor a proper compactification of an arbitrary affine family follows from WP.1. The construction still starts with an actual global class on E×P, so it does not supply such a class from independent component zero-cycles. The UK.7 component Albanese-kernel-family gate remains unchanged.

Completed: 2026-11-19T19:41:06.631254+00:00

## Complete TeX transfer check

2026-11-19T19:41:44.395776+00:00: Read the entire standalone manuscript C3_whole_proper_top_family.tex, SHA256 `6952898c6d1b5cde002d8a8f04ac20ce01c112050e5469196863e8d8a68c4acf`. PASS: it faithfully transfers WP.1–WP.8, all nonreduced-scheme and actual-product qualifications, and the complete correction proof. The rank/determinant argument alone replaces the unnecessary optional rational-logarithm discussion, with identical conclusion. No mathematical change or new source dependency. The explicit Proved heading and the no-main-movement scope are present. This receipt is a proof/source check, not a claim that cycles inspected the owner's standalone rendered pages.

## Final promotion heading check

2026-11-19T19:46:42.302024+00:00: Final C.3bu TeX SHA256 `fe8f965fabc492f1ad3f8e7a3109d8faf854a24b447f17d18c4403a4cdf54c93`. Replacing only its first status comment and two-line promoted heading with the exact previously read heading reconstructs SHA256 `6952898c6d1b5cde002d8a8f04ac20ce01c112050e5469196863e8d8a68c4acf`. This verifies that the promotion changed no mathematical or scope prose. The complete prior PASS therefore applies to the final manuscript. Owner visual QA is recorded separately.
