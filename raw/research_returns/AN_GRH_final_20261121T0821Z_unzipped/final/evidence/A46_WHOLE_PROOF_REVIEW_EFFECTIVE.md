# A46 independent whole-proof review

Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Date: 2026-11-21T06:09:17.157838+00:00.
Source: `work/gt_certificates/positive_rank_theta/A46_PRIMITIVE_SIGN_CRITERION.tex`.
Source SHA256: `f708446fd0e7af24f61625fc6ea68bd1c019ce1dcfb132958e71d6cc3ceb3ae8`.

PASS. I read the entire statement, prior-result scope, all five proof steps, and the final effect-on-gates paragraph. No mathematical gap was found.

The primitive projector is the actual integral Ramanujan-sum endomorphism, invariant under arithmetic automorphisms of the cyclic deck group. Its image is defined over the stated field; multiplying the rational collision class by this endomorphism therefore uses the rational primitive hypothesis before any constant extension. The group-ring identity nA=A p_n then kills the geometric A-difference because n is prime to p.

The subset-product support of A consists of distinct elements in the different prime-primary components, with integer coefficients plus or minus one. The resulting divisor has d=2^omega(n) simple zeros and d simple poles on two disjoint free deck orbits, so its function is separable in every characteristic. The Poonen field bound and elementary odd-n inequality exclude e=1. Faithfulness and the orbit-multiplicity argument prove freeness of the induced odd group on the intermediate curve.

For the new step, a zero fibre of the intermediate map is reduced. Each original deck orbit maps injectively to the intermediate curve, so the fibre has at most two points and e=2. The separable quadratic involution is normalized by G and therefore commutes with G. It exchanges the two original full orbits. The exact formulas tau(P')=sigma^j(Q') and tau(Q')=sigma^(-j)(P') follow from involutivity and commutation. Since f is fixed, comparison on the free P' orbit gives A sigma^(-j)=-A in the integral group ring. Iteration through the odd order of sigma^j gives A=-A, contradicting torsion-freeness and the nonzero subset expansion. This integer-sign argument remains valid in characteristic two. No elliptic genus calculation or Deuring–Shafarevich assumption is needed.

The geometric rank-zero consequence preserves its hypothesis under every finite constant extension, so descent and pointing are justified. The rational criterion is kept over its stated field and the full arithmetic fundamental group remains unchanged. The final scope does not claim a universal supply of such covers.

This is an independent mathematical reading by a second same-model agent, not formal proof-assistant verification. The Poonen exact result was already checked in the A34 audit; this event does not claim a fresh independent reread of every cited background theorem. I suggested replacing the repeated published Poonen induction with its exact applicability citation, matching the user's request for known results; that is an exposition change, not a mathematical defect.

## Final citation-only delta

Final source SHA256 `490219c87e7d801776092ec7974d2fb128fabdcb7af1daea9411514b9597d6eb`. I inspected the full exact diff from the reviewed f708446f source: only the repeated Poonen induction was replaced by the precise Corollary2.3 applicability sentence, with the controlled-field integer u=d/e. The theorem, new sign argument, all arithmetic hypotheses, and conclusions are unchanged. The citation-only delta passes; the independent whole-proof verdict applies to this final source.
