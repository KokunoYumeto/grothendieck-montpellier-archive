# A33 proof audit: quintic transfer to ordinary genus two

Date: 2026-11-21. Author/reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Source and status

Canonical source: `A33_QUINTIC_ORDINARY_REDUCTION.tex`.

Current SHA256: `7862f2921fd6af6c98b000c51d967b17a0327a02f403d2c8eb15b55672dcd3c6`.

**Author whole-proof reread: PASS.** I read the complete written proof after drafting, then checked each narrow correction listed below. This is an author check, not an independent review or formal verification.

The root investigator independently read the entire preceding version, SHA256 `9b1577793de71cc98911aa3bac497ebcff13003594bc30415bede16d17ef7b21`, and reported PASS, requesting the normal-core wording correction below. Independent final-source reviews were requested from row_audit and effective_galois; their outcomes must be recorded from their actual messages or retained audits, not inferred here.

## What the theorem proves

The universal finite-field genus-two point-section assertion in characteristic two reduces to its ordinary genus-two case. The arithmetic quotient remains the whole absolute Galois group; only the geometric fundamental group is replaced by its maximal pro-odd quotient.

The proof uses one arbitrary connected cyclic degree-five étale cover of the original curve. Its reflection quotient has genus two and has 2-rank either zero or two. In the rank-zero alternative, the original cyclic cover already has new 2-rank zero. In the ordinary alternative, two morphisms to the same ordinary genus-two quotient separate the lifted points. No universal theta-incidence assertion or Hooley-based proof of the ordinary case is claimed.

## Complete check of the five steps

1. **Lift and local genus computation.** Hyperelliptic inversion takes the defining order-five line bundle to its inverse, so a lift inverts the cyclic deck group. Its square is a rotation fixed by inversion, hence is the identity. On each five-point fibre above an original hyperelliptic branch point, a reflection has exactly one fixed point. There are no other fixed points. The étale map to the original curve identifies completed local rings at these points and preserves the involution action. Thus the total different of the reflection quotient is the original hyperelliptic different, namely six. With genus of the cover equal to six, Riemann–Hurwitz gives quotient genus two. This is valid for ranks zero, one, and two, not only the rank-one branch pattern.

2. **Prym isogeny and rank dichotomy.** The reflection-quotient pullback image and its deck translate are two-dimensional abelian subvarieties in the new Prym. Their norms to the original Jacobian vanish because those homomorphisms are fixed by hyperelliptic inversion and are therefore killed by two. On their scheme-theoretic intersection, both reflections act identically; their product generates the order-five rotation group. The sum-of-decks norm identity therefore kills that intersection by five. It is finite, so addition gives the explicit isogeny from the square of the genus-two quotient Jacobian to the four-dimensional Prym. On the geometric étale 2-torsion of the Prym, there are no invariant vectors under the degree-five rotation: the norm sum is zero but acts as multiplication by five, hence as the identity on such an invariant vector. The only nontrivial simple `F2[C5]` module has dimension four. Consequently the new 2-rank is zero or four, and the quotient rank is zero or two. This argument does not rely on a hidden semilinear-character convention.

3. **One common arithmetic lift.** All cover, deck, reflection, and point data descend to one finite constant extension. The chosen rational point makes its fibre split. For the normal index-five geometric subgroup, the intersection of the five conjugates of the kernel of an additional odd quotient gives a normal quotient of odd order upstairs. Thus the subgroup has its full pro-odd topology. A fixed path representing actual section conjugacy lifts to a fixed path with one rational endpoint over the second original point. These are the same two lifted points for both quotient maps. The argument is stronger than merely making separate choices satisfying an abelian Kummer condition.

4. **The zero-rank endgame.** Equality of the lifted sections implies that their Abel difference is rational 2-primary. The connected image of rotation minus identity is exactly the new Prym: the norm identity gives one inclusion, and the polynomial identity for five minus the deck sum gives the reverse inclusion using surjectivity of multiplication by five. The new Prym has no nonzero geometric 2-primary point in this case, so the Abel difference is rotation-invariant. The resulting principal four-point divisor has simple poles and gives a separable degree-two pencil. The resulting hyperelliptic curve of genus six cannot have a free order-five automorphism: its unique genus-zero quotient has a fixed point whose fibre has at most two points. This checks the contradiction without assuming that an inseparable degree-two map is a hyperelliptic pencil.

5. **The ordinary two-map endgame.** Both the reflection map and its composition with a deck generator induce maps on the arithmetic groups in question. The maps themselves may be ramified; pullback of finite étale odd covers still has odd monodromy. Ordinary genus-two injectivity applied to the two pushed section collisions identifies both pairs of quotient images. If the lifted points differed, one would equal the reflection of the other and also its conjugate-reflection image. The resulting order-five rotation square would fix a point of the étale cover, which is impossible. This removes the hyperelliptic-pair ambiguity left by a single quotient map.

## The finite canonical-class corollary

For a prescribed original point, the universal ordinary hypothesis can be replaced by the two actual A29 canonical-class hypotheses at its two displayed image points. At a Weierstrass point a reflection can be chosen to fix the lift, so the first quotient fibre is a singleton and only one target hypothesis is needed. The argument does not claim that these target classes necessarily have a suitable primary component.

Pulling a target A29 cover back to the degree-five cover is legitimate: pullback preserves étaleness, and a connected component has odd cyclic geometric monodromy. Its normal closure over the original curve is again odd because its group embeds in an extension of an odd product by the cyclic group of order five. The double quotient is used only as a morphism for pullback and functoriality, not as a forbidden étale double-cover step in the original pro-odd tower.

## Source coverage and corrections

I read complete recovered A1 B.40, complete recovered successor A.37, and complete recovered successor A.4. B.40 already contains the cubic reflection/local-different/Prym-isogeny machinery. A.37 supplies the related elliptic quotient obstruction and the precise warning about reflection twists. A.4 explicitly proves that one common lift has equal point sections, rather than only a primary Abel difference. These are credited in the source. Row_audit independently searched the available recovered text and reported these as the closest predecessors, without finding the exact quintic ordinary-case reduction. This is a limited recovered-source comparison, not a bibliographic priority claim.

The final delta from the initially reviewed source has four parts: (i) the normal-core argument now explicitly concerns the normal index-five subgroup, avoiding an overbroad statement about arbitrary odd-index subgroups; (ii) the isogeny is written as the actual map from `J_E × J_E`; (iii) successor A.4 is explicitly credited; and (iv) the two display line breaks in DR.1 were corrected. No proof conclusion changed.

No numerical search or new finite computation is required for A33. The elementary unit order modulo five is verified directly in the proof. The source is complete, while the residual ordinary existence gate is deliberately left explicit.

## Real multiplication refinement and completed independent reviews

The root investigator proposed the further restriction to ordinary genus-two Jacobians with Rosati-invariant real multiplication by the full quadratic integer ring of discriminant five. The complete additional proof is now in Step 2, equations DR.7a–DR.7c. With `T=v_* sigma v^*`, the pullback–norm identity gives `v^*T=(sigma+sigma^(-1))v^*`. Its quadratic expression is the deck sum, which vanishes on the Prym. The finite kernel of pullback therefore forces `T^2+T−1=0` as a homomorphism. Irreducibility over the rationals and the absence of integer torsion in the endomorphism ring prove injectivity of the quadratic integer ring. Adjointness of norm and pullback, together with reflection conjugation, gives `T^dagger=T`. All these endomorphisms are defined over the one finite field containing the cover data.

The author checked this complete delta. The root investigator and row_audit each subsequently reported PASS for this RM5 delta at the current `7862...` hash. Row_audit also independently whole-read the preceding final `8cd443...` version, rather than only its normal-core correction. Effective_galois subsequently reported an independent whole-proof PASS on the complete final `7862...` source, including the RM5 refinement and the canonical-class corollary. These actual review messages are distinct from the author check; their own event fragments and retained audits remain the primary record of their work. The final target hypothesis is therefore the ordinary genus-two real multiplication case, not the unrestricted higher-genus A1 theorem.
