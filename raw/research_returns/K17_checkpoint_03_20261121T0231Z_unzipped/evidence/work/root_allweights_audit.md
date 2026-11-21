# Root whole-proof review: all-weight integral generation at 2

Reviewer: /root, GPT-6 Astra Pro; reasoning-effort label not exposed. Date: 2026-11-21 UTC. This is a mathematical proof reading, not a formal verification or priority claim.

## Verdict and scope

PASS. I read the whole candidate, the complete Newton-basis proof, the final all-weight TeX, and both independent audit accounts. I independently reconstructed the following steps. The prerequisites are the previously audited arithmetic presentation, faithful rational realization and normal form, and exact outer-filtration comparison. Those prerequisites are not replaced by an unproved integral identification.

For h=c gamma c gamma^-1, complex conjugation negates h in H_ab and commutes there with gamma, because c gamma c=h gamma. It therefore acts as minus identity on the complete Lambda module, not merely on one element. Thus c(g)g belongs to the closed commutator subgroup for every actual g.

If the previous finite generated subgroup surjects through odd weight m, the quotient through m+1 is its product with a central kernel. Equality of their closed derived images follows directly. Compactness ensures that an element in this image has an actual lift in the previous subgroup's closed derived subgroup. Applying this to c(g)g produces w0 with coefficient 2B in weight m+1. No generation or saturation assertion at that even weight is used.

The normalized rational action gives D(g)g^(-5^m) coefficient 4*5^m B in the same weight. The inner conjugating factor has weight at least3, and all BCH cross terms lie above m+1. The ordinary integer power w0^(2*5^m) therefore removes that coefficient. Right multiplication by its inverse gives the precise recursion D(g_i)=g_(i+1) w_i g_i^(5^m), without commuting factors. The unchanged commutator class yields the exact next Newton polynomial and nonzero next odd leading coordinate.

At the new odd cutoff the recursion makes the new generated subgroup D-stable. The triangular odd-diagonal matrix sends a spanning list of its Frattini quotient to a spanning list even if that list has relations. Its image is compact and closed, so Frattini surjectivity is surjectivity. Ambient invertibility then gives inverse stability. Containing h and its whole continuous Gamma orbit proves surjectivity onto the entire cutoff. This closes, rather than assumes, the inductive generation hypothesis.

I also checked the finish independently. The Newton columns reduce to T^i times units modulo2 and have increasing (2,T)-adic order. Successive binary lifting gives a compact Z2-basis. Increasing actual weights imply convergence in compact H through the faithful Hausdorff rational realization. The free pro2 group on the convergent sequence maps onto H with abelianization isomorphism; projectivity of H and Frattini theory make it an isomorphism. No infinite-rank Hopficity is used. The first weighted Magnus term is primitive; integral Hall–Lyndon saturation makes it an integral free Lie element. The actual odd leading terms define a triangular rational Lie automorphism with nonzero diagonal, so they cannot kill that first term. This identifies the actual filtration and proves both inclusions of the integral graded lattice. The separate outer-filtration theorem supplies the original tripod filtration.

The argument establishes primitive odd free generators in every weight. It does not identify them with a prescribed Soulé normalization. The even abelian summand at an odd irregular prime prevents transferring the minus-abelianization step unchanged.

## Independent intermediate class-two result

The complete class-two TeX was also read. I checked its exact group-kernel description, the class-two conjugation recurrence, the tensor Newton expansion, and the mod2 polynomial identity. The degree bound r-1 eliminates every half-integral coefficient surviving the cutoff, so the correction is an actual integral commutator. This proof is valid independently of the later all-weight induction, and was not used as an extrapolation to higher generator length.
