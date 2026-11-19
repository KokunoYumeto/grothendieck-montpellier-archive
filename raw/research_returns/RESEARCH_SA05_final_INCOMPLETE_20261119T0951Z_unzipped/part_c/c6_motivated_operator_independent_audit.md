# Independent audit of whole-product motivated operators and graph ranks

Recorded 19 November 2026, 07:45 UTC, by /root/part_c; complete geometric-fragment audit appended at 07:48 UTC.
We read every line of root_motivated_operator_note.md and root_rank_diagram_note.md. The operator and linear-algebra constructions pass. The simultaneous-alteration and inertia construction is being written separately by Part D and is not silently assumed in this audit.

## Complete written theorem and simultaneous-model audit

At 07:48 UTC we read every line of part_d/c6_motivated_rank_reduction.tex, including all four proof steps and the abelian-strata corollary. The complete argument passes. We also directly reread Saito's Proposition 2.4.4, which allows arbitrary relative dimensions and correspondence codimension, the complete transport-of-structure proof of Lemma 3.2 (author pp. 36–38), and the conjugate-alteration setup and proof of Lemma 3.3 (pp. 38–39). André's section 2.1 setup and Definition 1 (printed pp. 13–14) explicitly use auxiliary smooth projective schemes over the original field K, so no unsupported descent of a geometrically chosen presentation is used.

One common finite Galois local extension suffices for the finitely many whole-product vertices, because Saito's Corollary 1.2.6 permits every extension containing a suitable extension. Taking all conjugates of each chosen semistable model gives a semilinear action on a disjoint union and an equivariant alteration map. The degree-divided pull-push projector identifies the original cohomology with its image. This does not assert descent of a semistable integral model through a ramified extension.

For an original inertia element, the induced automorphism of the finite residue field is the identity. Its action on the closed strata is therefore represented by algebraic isomorphisms and permutations, with the fixed signs caused by ordering intersections. Saito's transport diagram has that algebraic map on E1 and the chosen original inertia element on the abutment. The dependence of the latter on the lift is not discarded: only E1 factors through the finite Galois quotient before monodromy is shown to vanish.

For the normalized vertex H^(i+2r)(Z)(r), the weight-b row has entries E1^(a,b+2r)(r) and its relevant cohomology occurs at the common index a=i-b. All elementary maps and graph constraints are consequently maps of finite complexes of one weight. Appending N^s uses the target E1^(a+2s,b-2s+2r)(r-s), which still has weight b and the correct abutment degree. We do not treat N as a generic algebraic correspondence.

The finite-field rank hypothesis applies to every resulting finite algebraic block after the explicit projective-space padding from the algebraic-projector proposition. The graph lemma determines the rank of the motivated expression on E2 without a chain-level inverse or idempotent. Generalized Frobenius weight spaces split the abutment, and FNF^(-1)=q^(-1)N identifies the actual monodromy ranks with sums of graded ranks without assuming Frobenius semisimplicity or weight–monodromy.

Finally, once those ranks give N=0 for every coefficient prime, the common semistable extension kills inertia on the image of the motivated projector. For each element of the remaining finite inertia quotient, the same graph construction controls its difference from the identity on every weight-graded piece. Vanishing at one prime gives vanishing at all primes. Its action is then both unipotent and finite order, hence the identity in characteristic zero. This is descent at the original place, and it uses no unproved trace formula for motivated correspondences.

The abelian-strata corollary requires actual algebraic presentations for every auxiliary stratum used by the motivated expression. The current abelian Tate theorem and homological–numerical coincidence supply a common semisimple category and algebraic image projectors for the finite blocks. This rank argument does not assert positivity of an arbitrary geometric primitive pairing transported from an abstract abelian motive.

The resulting theorem remains a sufficient-conjecture implication. It does not prove the finite-field rank conjecture, its converse from local unramifiedness independence, or that every absolute-Hodge projector is motivated.

## Primitive strings and normalizations

For a primitive vector of degree $i$ and string length $n=d-i$, the coefficient formulas give

$$
T^2(L^kp)=L^kp,\qquad
TLT(L^kp)=k(n-k+1)L^{k-1}p.
$$

Indeed the two factorial ratios multiply to $k(n-k+1)$; both primitive signs cancel. Consequently $[\Lambda,L]$ acts on $L^kp$ by $n-2k=d-(i+2k)$. These formulas independently verify the normalization rather than appealing to the discrepant sentence in André.

The Weyl product $\exp(L)\exp(-\Lambda)\exp(L)$ sends $L^kp$ to
$(-1)^k k!/(n-k)!\,L^{n-k}p$. For $m=i+2k$, the parity identity

$$
\frac{m(m+1)}2+\frac{i(i+1)}2\equiv k\pmod2
$$

proves the input-degree sign in the note. The sign polynomial is correctly placed on the right of the Weyl operator.

For $\mathbb P^2$, the unnormalized Lefschetz involution gives $SLS(L)=1$, while the stated Hodge involution gives $TLT(L)=2$. Thus the printed identification cannot be used with the preceding definitions. The needed normalized identity has been proved directly, so this specific discrepancy causes no gap in the present construction. It does not refute the algebra-generation assertion of André's Proposition 1.2.

## Factor recovery on a whole product

André's product formula writes the global Hodge involution as
$D(T_X\otimes T_Y)$, where $D$ acts on bidegree $(m,n)$ by $(-1)^{mn}$. Partial Lefschetz operators and factor involutions preserve the parity of each degree; hence they commute with $D$, and $D^2=1$. This proves

$$
TL_XT=\Lambda_X\otimes1,\qquad
TL_YT=1\otimes\Lambda_Y.
$$

The displayed interpolation polynomial has denominator $r-m$, exactly the difference between the eigenvalues $d_X-m$ and $d_X-r$. It therefore gives the factor-degree projector, including when some degrees vanish. Combining it with the Weyl operator gives the factor Hodge involution as a finite expression in algebraic partial cup products and the global involution of the whole product.

This step does not construct an algebraic generic Künneth projector. It constructs an operator expression on cohomology. Its role is precisely to avoid assuming tensor compatibility on an E1 page.

## Hard Lefschetz inverses and the motivated action

For $j\le d$, the map

$$
Q_j=L(L^{d-j+2})^{-1}L^{d-j+1}
$$

is the identity on $LH^{j-2}$ and zero on the primitive kernel. The Hard-Lefschetz inverse has exactly the source and target shown in the note, and the Tate twists cancel. Iterating on the recovered lower-degree vector gives the entire primitive decomposition. For $j>d$, the initial Hard-Lefschetz inverse brings the problem to degree $2d-j$. The coefficient formula then recovers the global $T$ from finitely many algebraic maps and inverses of specified Hard-Lefschetz isomorphisms.

The finite inhomogeneous expressions are legitimate when each normalized group $H^{i+2r}(Z)(r)$ is a separate vertex. One then selects a specified total degree by taking the corresponding block, not by assuming an algebraic cohomological projector on the generic variety. Finite-field projective-space padding later turns every finite block matrix into one algebraic correspondence on a fixed cohomological degree.

For a motivated endomorphism represented by
$\operatorname{pr}_{12*}(\alpha\cup T_P\beta)$, the relation $b=a+d$ is the correct codimension condition. Exterior multiplication by $\beta$, application of $1\otimes T_P$ on the larger whole product, diagonal pullback, cup product with $\alpha$, and final pushforward give the usual action on $H^i(U)$. The final degree is $i$ and the final twist is zero. The factor-star construction above handles the only initially nonalgebraic tensor operation.

## Graph constraints and passage to E2

For any finite constraint matrix $R$ and output projection $\pi$,

$$
\dim \pi(\ker R)=\operatorname{rank}(R,\pi)-\operatorname{rank}R
$$

follows directly from rank-nullity. Encoding an inverse by $by-x=0$ requires invertibility only on the specified image spaces. After alteration, the additional equations $(q-1)x=0$ impose these image conditions. Neither a chain-level inverse nor an E1 idempotent is required. The actual relations hold on E2, where the corresponding maps are the associated-graded cohomology maps.

For an ordinary chain map the displayed block-rank identity computes the induced rank on cohomology. This was independently re-proved in our earlier audit of the algebraic C6 reduction. Combining the two identities controls any finite inverse expression using only finite algebraic block ranks on E1.

For an expected-weight-$i$ normalized vertex, its weight-$b$ part occurs in row-complex cohomological degree $i-b$. All vertices used for the motivated projector therefore align. A final $N^s$ target must instead be shifted by $2s$, exactly as in the previously audited algebraic proof. This is a row-complex shift, not an assertion that monodromy is a degree-zero generic motivic correspondence.

## Primary source check

We reopened André's complete primary PDF, https://www.numdam.org/item/PMIHES_1996__83__5_0.pdf, and read printed pp. 10–14: §1.1 definitions; the relevant §1.2 identities and Proposition 1.2 proof; §1.3 and the full Lemma 1.3.2 proof; Definition 1 in §2.1. Definition 1 explicitly permits either the Lefschetz or Hodge involution, so the proof may choose the latter. The formula statements were also requested as original-page screenshots. We do not claim a full reread of the paper or of the later deformation theorem.

The finite matrix checks reported by root are consistency checks, not a substitute for the primitive-string and graph proofs above. The remaining geometric audit must construct common semistable models for the entire finite diagram and realize the finite inertia actions on conjugate strata. That step is not implied merely by the operator identities.
