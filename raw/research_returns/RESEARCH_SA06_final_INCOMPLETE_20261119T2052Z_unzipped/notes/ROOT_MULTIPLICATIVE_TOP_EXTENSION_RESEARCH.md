# Attempt to propagate the multiplicative surface quotient to higher top degree

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA06, /root, 19 November 2026, 15:04–15:10 UTC. This is an unsuccessful approach record, not a registered theorem or a progress-gate reduction.

## The tempting surface reduction is false over arbitrary coefficient fields

The residue-field-restricted theorem C.3be reduces rational top Chow vanishing to normal local surfaces and proves it over Fpbar. Replacing its torsion argument by ordinary algebraic equivalence over an arbitrary algebraically closed field does not work. The already proved C.3y has exceptional rational triangle and ordinary B1(X)=k* plus (Z/4)^2. Proper parameter curves cannot change the multiplicative gluing scalar. For fields of positive transcendence degree over Fpbar, k* tensor Q is nonzero. This is an actual counterexample to the proposed surface lemma, not merely a missing proof. The normal-surface pushforward to a higher-dimensional local scheme could annihilate its classes, so this observation does not settle the higher-dimensional top quotient.

## Why the direct projective-space product does not yield a regular puncture

C.3y starts from the triangle D(z)=z0 z1 z2 and quartic G, with G nonzero at its vertices. Its resolution is locally the hypersurface D−tau G=0 in the total space of O_P2(−1). The nonzero normal derivative at each triangle vertex makes the surface smooth.

A prospective dimension-N=m+2 Segre version uses the total space of O_{Pm×P2}(−1,−1) and equation D−tau ell(x)G=0, with ell a projective linear form. The exceptional divisor would initially be Pm times the triangle. Along a triangle vertex over ell=0 the equation is locally u v=tau w, with smooth extra coordinates. Thus the source is singular there; a simple product argument is invalid. For any positive projective twist the coefficient of tau has zeros at that vertex, so choosing a different single section cannot remove this defect.

Resolving the local model by blowing up (u,tau) gives charts u=a tau, w=a v and tau=b u, v=b w. The resulting source is smooth locally, but one exceptional component becomes the blow-up of Pm×P1 along the hyperplane H×{vertex}. The other component and their double locus Pm are unchanged locally. The new exceptional divisor on the blown-up component restricts to the hyperplane class on that double Pm and is supported away from its other attaching locus.

This creates a precise problem for the intended top-weight gluing detector. Before modification the formal product Pm×triangle has a k* contribution from its cyclic gluing, multiplied by h^m. After the local modification, the added exceptional divisor times h^(m−1) has intersection degree one on the affected double locus. Multiplying by a constant unit gives a class in the component's K1 of weight m+1 whose restriction hits that edge generator. Therefore the top-weight edge gluing that the naive product was intended to preserve is no longer protected. A global conclusion about the full resolved K-theory complex would require additional work; none is asserted. In particular we have not constructed a higher-dimensional nonzero rational Btop class.

A higher-rank vector-bundle variant instead keeps only the exceptional triangle as a curve and can make the source regular using several normal derivatives. It does not preserve the required top Adams weight: after inverting p, finite K0 detection restricts to that one-dimensional exceptional scheme, whose rational K0 has weights at most one. For N>=3 that is insufficient to detect a codimension-(N−1) class. This is another reason the surface witness alone does not propagate.

## Remaining exact gate

Construct an actual higher-dimensional regular puncture with a nonzero rational ordinary top quotient and a detector surviving the entire exceptional boundary and all fixed proper-curve families; or prove universal rational top vanishing beyond the current smooth-exceptional/cone/residue-Fpbar cases. The multiplicative surface example is a useful constraint on either approach, but it does not reduce this gate by itself.
