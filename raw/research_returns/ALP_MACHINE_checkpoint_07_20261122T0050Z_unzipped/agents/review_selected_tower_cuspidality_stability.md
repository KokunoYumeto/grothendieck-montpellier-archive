# Independent whole-proof review of AM-R-014

Reviewer: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE, 21 November2026UTC.

## Outcome and scope

I read all of work/research/selected_tower_cuspidality_stability.md, the exact source predicates, the character and ambient definitions, and Wu's primary proposition and the relevant proof passages. The genuine tower-cuspidality implication and full smooth isotypic stability pass in the stated mathematical interpretation. This is a source-predicate verification, not a new tower theorem, a full ThetaX/D7 construction, or a proof of the other two remaining analytic predicates.

Two domain clarifications raised during review have been incorporated in the saved parent file: the actual character group restricts to either one or the relative quadratic character on the base ideles, and the smooth cusp domain has the usual rapid decay and is built from actual smooth cuspidal embeddings. These are necessary to apply the literal universal quantifiers honestly.

## 1. Literal declarations

Directly read CayleySignature.lean lines114–125 and154–202. The fourth predicate quantifies over a stable cusp submodule and every lower-target Schwartz input. Its conclusion is cuspidality, without a nonvanishing assertion. The sixth predicate asks only invariance of IsDv under finite and actual real group actions; its name does not supply a numerical real nonvanishing constant.

Directly read DataTheta.lean lines570–650. The source has an arbitrary AF module carrying full real-group actions, a cusp submodule, a typ submodule, and only YsLow_zero for the lower spaces. Consequently the choice of genuine Witt-lower targets and a full smooth ambient is an actual mathematical interpretation that the record permits. It is not forced by an auxiliary finite or zero-dimensional proof model.

## 2. Spaces and parity

For n_j=k+m−1+jt and q_j=floor((m−j)/2), the split-sign diagonal form I_(n_j−q_j)⊕−I_qj has rational Witt index exactly q_j. The explicit pairs ((a+b)/2,a−b) have isotropic norms and mutual pairing one; the real signature bounds the rational index in the opposite direction. Removing i such pairs gives precisely the listed rational lower space and all relevant maximal rational parabolics.

The embedding calculation p_j−N_j=ceil((m−j)/2)−1 is nonnegative for j<m. At j=m the target is positive of dimension N_m−1. These statements do not impose the remaining arithmetic Spaces pins.

The source car condition inserts etaT inverse at even j. Since n_j has parity j+1, and etaT has the quadratic base restriction, the displayed character has the required parity. Within the now specified character group, integral infinity type forces trivial base restriction: the other possibility has odd angular parity at every real place. Without this domain restriction, IsMu alone would not control arbitrary finite base-field characters. Removing hyperbolic planes preserves dimension parity, so the same splitting character applies throughout each lower tower.

## 3. Constant terms

Opened Wu's primary arXiv:1409.0770 PDF. Read Proposition3.1 and equations3.2–3.4 on printed p.9; its pointwise proof in3.21–3.25, printed pp.11–12; and the splitting conventions in sections1–2.2. The theta lift in equation3.1 is bilinear in the input function, so no extra Hermitian-conjugation dictionary is needed for the source's literal descending convention.

The proposition gives the lower theta lift after restriction to the smaller unitary Levi. The general linear Levi character is retained in the parent statement, and the displayed restriction has the correct normalization for compatible measures. The proof uses cuspidality to remove the positive-rank orbits and retains the zero orbit; its use of irreducibility is unnecessary for this pointwise identity.

For a general target point h, equivariance replaces the Schwartz vector by omega(h)Phi. Since the hypothesis quantifies over every Schwartz vector, it kills every translated maximal constant term. Vanishing for all maximal rational parabolics implies vanishing for every proper one by transitivity of constant terms. This remains valid for a nonclosed stable source submodule: the argument is pointwise in each cusp vector, within the specified convergence domain.

A minor wording refinement was sent to the parent: after compatible splitting characters have been fixed, the constant-term argument requires no further Hyp3 inequalities. Its TParity clause was used earlier to verify character parity.

## 4. Smooth stability

The algebraic sum of full smooth real isotypic realizations is stable under the real group. Finite translations commute with that action, so composing an equivariant realization with a finite translation gives another realization of the same type. Complex conjugation commutes pointwise with these translations, proving the exact IsDv implication.

Using only compact-finite vectors as a noncompact real-group module would be invalid. The amended full smooth moderate-growth domain avoids that issue, with the cusp convergence properties stated separately. On the positive definite side used in AM-R-013 the real representations are finite dimensional, so this refinement does not alter its algebraic finite-sum argument.

## 5. Status of references and checks

Wu is used as a known primary theorem, with the pointwise and character hypotheses directly checked. No independent proof of the tower theorem and no Lean execution are claimed. The SGA framework references are carried at the parent run's checked status; they are not used to replace Wu's analytic constant-term identity.

Primary locator: Wu, C. (2013), Irreducibility of theta lifting for unitary groups, Journal of Number Theory133(10),3296–3318; author preprint https://arxiv.org/pdf/1409.0770, Proposition3.1 and proof3.21–3.25. Retrieval refs for parent reuse: turn656881901view0 and turn840224495view0–2. The parent must open a source itself before using a web citation.

