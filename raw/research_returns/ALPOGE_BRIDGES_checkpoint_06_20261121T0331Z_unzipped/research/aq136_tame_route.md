# Integral cote 136: the remaining whole-object step in the tame route

This is a route audit, not a proof or refutation of the original integral common-source or terminal-localization assertion. It supplements the checked semilocal theorem AQ-136-SEMILOCAL. The strict category and uniform admissibility are those recovered from official cote136 physical111–121, mathematical rectos only.

## The exact elementary disk calculation

Let `D=Lambda_k(a) tensor Gamma_k(b)`, with form degrees `|a|=1`, `|b|=2`, equal positive weight `m`, `da=b`, and `db=0`. The PD ideal contains the positive even elements. In positive degrees the entire cochain complex is the direct sum, over `r>=1`, of

`k a b^[r-1] --r--> k b^[r]`,

in form degrees `2r-1,2r` and common weight `mr`. Indeed the special differential rule gives `d(b^[r])=0`, and Leibniz gives `d(a b^[r-1])=b b^[r-1]=r b^[r]`. These monomials form the free graded k-basis. Consequently

`H^(2r-1)(D)=k[r]` and `H^(2r)(D)=k/rk`,

at weight `mr`; `H^0(D)=k`. Here `k[r]` is the kernel of multiplication by r. Over `Z[1/d!]` the augmentation ideal is therefore acyclic through form degree `2d`; over a nonzero ring with a nonunit prime p, its degree `2p` class survives. This calculation is elementary and does not assume a transferred model structure for strict PD differential algebras.

## Why admissibility does not demand full disk acyclicity

Let B be the checked standard integral theory. It has a simplicial augmentation `B→k` obtained by sending every positive-weight generator to zero. Regard D as a constant simplicial algebra and form the strict PD fibre product `C=B×_k D`, with coefficient map `S→B→C` and the D-component given by `S→k→D`. As a bigraded module, C is B plus the positive-degree augmentation ideal of D. For each fixed form degree q, that ideal is supported in only one weight, namely `m ceil(q/2)`. Thus beyond that weight the entire simplicial row equals B's row, and beyond the finitely many weights affecting a fixed vertical degree its vertical cohomology equals B's. The uniform-in-simplex vertical bounds and the horizontal tail acyclicity therefore hold. Hence C is an admissible integral theory.

Nevertheless `b^[p]` is a nonzero vertical cohomology class of C over Z, in weight `mp` and form degree `2p`. Therefore a proposed fully vertically acyclic PD replacement containing an element x mapped to a cannot map to this C: the closed element `gamma_p(dx)` would be exact in the replacement but its image is the nonzero class `b^[p]`. This is only an obstruction to the prescribed fully acyclic replacement. The object C itself receives the obvious admissible map from B, and so this example is not an obstruction to the original common-source or localization question. It is consistent with the earlier intake's reported failures of prescribed delayed bar primitives; no novelty claim is made.

## The missing passage from finite degree to one object

Finite-degree constructions over successively localized coefficient rings do not yet give one integral source. Three requirements remain to be supplied by an actual relative construction:

1. Strict maps between whole PD differential algebras, preserving every divided power, both gradings, the coefficient algebra, all simplicial identities, and the specified target maps. A family of separately chosen truncated comparisons supplies none of these transitions automatically.
2. For each fixed form degree q, one weight bound valid at every sufficiently late stage and at every simplex. Bounds that grow without limit with the stage or prime do not pass to an admissible limit.
3. Control of coefficient multiples of every residual fixed-degree defect. Multiplication by `T^[n]` increases weight without increasing form degree. Leaving a defect above a proposed form cutoff at its first weight does not prove that its coefficient multiples remain outside every later admissibility range.

The first issue is most delicate in relative degree zero: killing a vertical H1 class by a new degree-zero generator can create closed degree-zero combinations. Their images in the two targets must have the same coefficient residue. The pointwise torsion example does not prove that a simplicially coherent obstruction exists, but it prevents assuming this compatibility without a lemma.

No relative all-degree extension lemma establishing these properties has been proved here. Ordinary tensor targets and free-zero-form special-de-Rham constructions are already excluded in the separately checked AQ-136-TENSOR and AQ-136-DERHAM-CELLS scopes. Positive-form cells that kill only sufficiently high coefficient multiples remain a distinct possible route; their admissibility and coherent target lifts are not yet established.

## Literature scope inspected

The publisher's primary landing page for Cartan (1976), *Théories cohomologiques*, *Inventiones Mathematicae, 35*, 261–271, confirms DOI https://doi.org/10.1007/BF01390140 and the article metadata. The complete article remains behind the observed subscription access page; no inaccessible theorem has been used as a proof.

The already inspected Guillén Santos–Navarro–Pascual–Roig (2008) comparison is in contravariant monoidal functors and does not itself preserve the strict weight/PD category. Its precise scope is recorded in `research/root_136_routes_audit.md`. No improvement of the original integral status is attributed to either bibliographic lookup.
