# A41 whole-proof review

Date: 2026-11-21. GPT-6 Astra Pro; effort not exposed; /root/row_audit.

**PASS.** Read the complete author source at SHA256 `c046d444a2e779c15cf7c719d4a44736c38c73e8f75ccb8ae18ac500a7d210a7`, including the final free-orbit strengthening to at least55 good lifts and eleven split source points per parameter. This is a targeted whole-proof reading, not a separately authored independent re-proof or formal verification. The parent proposal was also checked before the final source was written. No correction is required.

## Exceptional-parameter bound

Use F1={P0}×E for a vertical fibre and F2=E×{Q0} for a horizontal fibre. The critical locus Z is the fibre product of two separable degree-two canonical maps E→P1, one composed with the projectivized differential of T. It is the pullback of the diagonal, an effective Cartier divisor of numerical class 2F1+2F2. Its projections are generically etale, so it is generically reduced. A Cartier divisor in the smooth product is Cohen–Macaulay, and therefore has no embedded associated primes; generically reduced plus this property implies reduced. Thus the reduced curve used in the original A40 Step3 has the same class, with no discarded multiplicity.

For h(P,Q)=Tz_P−2z_Q and L=h*O_J(TTheta), the vertical degree is 4(Theta dot TTheta)=12, by multiplication-by-two pullback on the Neron–Severi group, valid also in characteristic two. The horizontal degree is Theta squared=2, because T is an automorphism. Consequently L dot Z=2·12+2·2=28.

A40 Step3 proves that h maps no irreducible component of Z into TTheta. The pullback restriction therefore defines a zero-dimensional effective Cartier intersection on Z of total degree28. Every off-vertical singular parameter arises from a point in its support, and t is uniquely determined by h(P,Q)=Tz_t. There are at most28 such parameters. At the vertical component, the only remaining exclusions are preimages under the degree-two Gauss map of three transformed branch values, at most6 geometric points. Hence at most34 parameters are excluded. This counts parameters, not distinct isomorphism classes of covers.

## Fixed finite field and simultaneous failure of all reflection detectors

For A13, E, B and the integral symmetric T are defined over F2; choose for instance a rational Weierstrass theta characteristic B. Since #E(F128)=129, at least95 F128 parameters give the smooth A40 curve D. The projection involutions and their product are defined over F128, so D, its cyclic quotient C, and all maps are defined there. The A40 decomposition J_D isogenous to J_E squared times J_C is defined over that field. A13 has trace0 at every odd extension of F2, in particular over F128. Thus #D(F128)=#C(F128). The genus-two Weil bound implies #C(F128)≥84: an integer trace≥46 would have square at least2116, exceeding16·128=2048.

For each of the five maps v1 sigma^j:D→E, the inverse image of the three Weierstrass points has at most6 geometric points. The union for all five maps therefore has at most30 rational points. At least54 rational points P' avoid that union. For any such P', put P=pi(P'). The degree-five fibre is rational and split. All five reflection images lie in E(F128) and are non-Weierstrass, so A38 gives exact canonical order4159 for each. The corresponding multiplicative order of2 is2079, odd, so A29's detector cannot apply to any of them. Fixed geometric divisor classes retain their exact order under all subsequent constant extensions.

The five maps account for all five reflection subgroups. Changing the lift within this same split fibre merely permutes the five images. A quotient identification differing by an automorphism of E preserves canonical-class order and the Weierstrass set. Thus both-image selection, reflection selection and lift selection within this one cover cannot force an A29 detector. Changing the cyclic degree-five cover remains outside this conclusion; no rank-one source or Weierstrass source point is asserted.

## Final written-source additions checked

The good subset of D(F128) is invariant under the constant C5 deck group, which acts freely. Its size is therefore a multiple of5, so a lower bound54 implies a lower bound55. Distinct orbits give distinct source points under the degree-five quotient, hence at least11 rational split source points for each of at least95 good parameters. No claim of95 distinct isomorphism classes is made.

The statement distinguishes a counting existence proof in a defined family from an individually enumerated parameter/covering equation. It also explicitly retains the possible change of quintic cover, other criteria, and the unspecified source two-rank/Weierstrass status.

## Primary source and related narrow check

Reopened Milne, Abelian Varieties, Corollary6.6 p.9 and read its complete displayed proof, together with the stated consequence in Remark12.13 p.24: multiplication by n acts by n squared on the Neron–Severi group, in arbitrary characteristic. This supports the factor4 in the vertical restriction. Primary URL: https://jmilne.org/math/xnotes/AVs.pdf ; retrieval reference turn949831702view0. The genus-two Weil statement is the cited MilneJV Theorem11.1, already checked in the A40 source review; no new full proof of the Weil theorem is claimed.

The A40 background-only update to SHA256 883b929b9b8b633340ea0c75452ba0d7d885c092bc2f2b17d5a1374545fa641d was also read and checked against the previously opened Kumar–Mukamel primary §§2–3. Its exact scope distinction is correct. This was a citation/context delta, not an additional whole reading of A40.

## Final citation-only update

The final source at SHA256 `5523c5a2550a1118c6f523493e6a16da3dddfd6fa9acee0b6660e682e59599e1` adds only the exact MilneAV Corollary6.6/Remark12.13 citation after the multiplication-by-two pullback assertion. Read this added sentence and verified its locator against the primary source above: PASS. No mathematical change and no additional whole-proof reading.
