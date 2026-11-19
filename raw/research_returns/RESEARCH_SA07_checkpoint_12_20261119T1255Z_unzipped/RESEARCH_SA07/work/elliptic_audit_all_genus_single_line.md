# Independent audit of F.3.32

**Verdict: PASS for the full stated scope.** Independently read the complete proof in `work/F3_32_integrated_text.tex`, its actual invariant-input map in `work/LM6_A22_all_genus_single_line_invariant_reduction.tex`, the full-profinite witness construction F.3.31, and the source passages identified below. This audit is separate from the root's standalone final recomputation. No elliptic splitting assertion is inferred.

## 1. Actual invariant input and specialization

The space being projected is the actual finite-dimensional degree-six universal image intersected with the line-tangency subspace. Both are stable under the specified Levi subgroup. In characteristic zero the trivial-isotypic projector preserves each submodule and has `q e_S = q`, because the target representation is trivial. It is not asserted to come from one Galois element. The full symplectic projector is used only after the scalar equations, where preservation of tangency is unnecessary.

The positive constrained blocks have independently checked dimensions 3,3,1,0. Their tensor reconstruction includes the explicit nonzero multiplicity factor, so the program's normalization spans exactly the same rational space. At most three W-pairs occur in each positive block; the invariant-tensor independence hypothesis therefore holds for every complement genus s>=3. The five pure vectors were independently identified with the five source vectors by the exact matrix of determinant 5 in `elliptic_audit_levi_input.md`. The 525 coefficient identities and nonzero detector determinant were checked there. The source dimension and detector give the same specialization in the smallest required complement genus, not merely in a formal stable diagram space.

The raw pure determinant in (UC.2) has the positive coefficient 3538944. This agrees with the earlier source-to-program determinant calculation: dividing the signed source determinant by 5 gives coefficient -3538944, and the determinant of the raw-to-source sign matrix is -1. All displayed factors are nonzero for integer s>=3.

## 2. Necessary equations and the actual maps

The seven scalar functionals are applied to actual brackets `[D,delta]`, where delta is the displayed geometric degree-one Johnson derivation and D lies in the actual universal image. The previously established normalizer map puts each such bracket in the actual degree-seven geometric image. The ES and R vanishing results are therefore used on their asserted domain. The R formula uses the exact five terms of MSS2026 Proposition 4.1. Its transfer below the printed stable range is through extension of a boundary mapping class by the identity, extension of its derivation by zero, and the contraction identity `R_G(i^tensor9 T)=i R_g(T)`. The symplectic inclusion is injective. This is a map-level transfer, not a stable decomposition asserted in low genus.

The cyclic scalar functional sums all seven rotations. It is thus well-defined on the cyclic quotient even for periodic words. The derivation tensor convention, reconstruction by contraction with its first slot, and both ordered compositions of the bracket agree with the independently computed literal six-letter realization. That independent check used no diagram-gluing plan and verified all 60 detector, 36 R and 48 ES values at s=2. The symbolic evaluation uses at most four W-pairs. Each closed component has an independent handle choice; choices on different components need not be distinct. This proves the signed `2s` factor per loop used by the polynomial evaluator.

Only necessity of the seven equations is used. Completeness of the mixed normalizer equations is never required.

## 3. Polynomial identity and return to the quotient

The two columns J are contraction vectors of the two actual geometric brackets already checked in genus three. Their embedding into larger symplectic spaces preserves these literal contractions. Direct exact linear algebra gives ranks 2 and 3 for J and L and `LJ=0`, hence `ker L = im J`.

I independently typed all 21 displayed entries of the reduced polynomial matrix N0 and checked `N0 M7 = d0 L K` against the retained scalar polynomial rows. All 36 differences vanish in QQ[s]. The exact formula `d0(3+t)=9(9+2t)(53+30t+4t^2)` has positive coefficients and is positive for every integer t>=0. Thus the identity applies over every Q_l, including primes dividing the integer denominators, because the specialized nonzero rational scalar is invertible in Q_l. This is an exact polynomial check, not sampled interpolation.

If D has the seven vanishing rows, its five contractions lie in the span of the two actual brackets. Apply the full symplectic projector. The source five-detector map is injective on the resulting invariant space, and the fixed raw-to-source sign matrix is invertible. Equality of the five coordinates therefore gives actual equality with a linear combination of projected geometric brackets. The quotient kills those brackets and commutes with both projections. This proves the asserted single-line vanishing on the original actual universal image.

## 4. Full profinite arithmetic application

The F.3.31 witness first applies Nakamura1994 Lemma 2.1.4 to the full class of finite groups, choosing an actual finite cover and a prime with nonzero proper homology. It does not assume a prime quotient of the initial element is already nontrivial. Passing to the arithmetic normal core and taking the necessary l-power preserves that class under proper pushforward. Rational tangential descent and filling to one cusp are actual arithmetic maps. The same curve supplies the nonzero universal degree-six quotient via Nakamura1996 Lemma 4.5 and the printed rank table.

The chosen arithmetic element fixes the nonzero degree-one class; its normalizer exponent is consequently one. The strict representative differs from the normalizer lift by an inner automorphism. Removing its degree-one centralizing contribution uses a power of the full logarithm, or equivalently the BCH group operation, before comparing higher degrees. The primitive centralizer then kills degrees 2 through 5, and degree 7 is exactly `D(a)=[Z6,a]`. Thus the very same nonzero quotient class lies in the single-line tangency space, giving the contradiction proved above.

For cusp inertia, the explicit UT3(Z/l^n) substitutions send the commutator generator to `1+E13` of exact order l^n. A nonzero profinite cusp exponent has a nonzero l-component for some l, so its maximal pro-l image is nontrivial. Hence `I intersect R = 1` by the actual maps. Conjugation preserves this conclusion. This establishes precisely the stated original curve and its finite base changes. The general affine theorem is audited separately as F.3.33.

## 5. Primary passages and computation records

- MSS2015 arXiv v2: Phi sign convention p7, invariant-tensor independence Proposition 2.1 p8, explicit five vectors pp25--26, Proposition 7.2 pp26--27. These were reopened during the input audit; p27 was visually read. Do not substitute a later version's numbering.
- MSS2026 arXiv:2608.17673v1 Proposition 4.1, pp10--11: the actual R formula and vanishing on the Johnson image. The source presents its proof as a sketch; the audit retains that source status and supplies the precise stabilization map needed here.
- Nakamura1994 Lemma 2.1.4, printed pp96--97: the full-class proper-homology detector, reread in the original text.
- Nakamura1996 printed pp115--116, especially (4.3), (4.4), Lemma 4.5 and Corollary 4.6: visually reopened in this audit. The degree-six rank is one; finite base change and arbitrary-number-field applicability are explicit.
- Earlier independent exact records: `check_levi_pure_specialization.py`, `check_levi_scalar_word_realization_es.py`, `check_levi_selected_polynomial_identity.py`, with their separate `.out/.json` records. These are not recounted as newly executed.
- New displayed reduced-identity record: `work/code_elliptic/check_reduced_levi_identity.py/.out/.json`. The complete standalone recomputation `check_all_genus_single_line.py` is registered and rerun by root; this audit does not duplicate that run or its timing.

New reduced-identity run: exit code 0, elapsed 1.666405871 seconds, UTC start 2026-11-19T11:16:17.214454+00:00.
