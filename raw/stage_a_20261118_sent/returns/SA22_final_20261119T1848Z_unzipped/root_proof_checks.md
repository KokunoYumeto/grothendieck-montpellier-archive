# Independent checks: cote 68, games and rearrangement

These arguments check statements actually present in the supplied transcription. They are this run's reconstructions, not additional manuscript text. Physical line numbers refer to `MPL_66+68_002-032_transcription.tex`. They do not decide any uncertain ink. Computations are reproduced by `programs/root_computations.py` and recorded in `outputs/root_computations.json`.

## G1. Reachability, terminal conventions, and ordinal ranks

Work in ZFC with a set of positions C, successors R(x), terminals C0={x:R(x)=empty}, and a partition of C\C0 by the player who moves. Fix player j and a target T contained in C0. A play is maximal if infinite or if it ends in C0; winning for j means finite termination in T. A strategy chooses a nonempty subset of R(x) at each j-position, and must win for every allowed choice, not just one compatible path.

Define F(A)=T union {j-positions with a successor in A} union {nonterminal other-player positions all of whose successors lie in A}. Its least fixed point W is the transfinite union of the iterates from the empty set, taking unions at limit ordinals. A position first entering at stage alpha+1 has a rank alpha+1. At a j-position in W choose a successor of smaller rank; at every other nonterminal position in W all successors already have smaller rank. Thus every compatible step strictly decreases rank, so no infinite compatible play exists and every maximal play ends in T. This single-valued positional strategy wins simultaneously from every member of W. Outside W, every j-successor stays outside W and every other-player nonterminal has an outside successor; a choice of such successors avoids W forever or ends at a terminal outside T. This also proves the converse and the recursive characterization.

This proof is an independent modern completion, using transfinite rank and choice; the sheets do not supply this transfinite construction. The nonterminal restriction in the universal predecessor clause is indispensable. If it is omitted, a losing terminal enters vacuously. The restart's barred complement excludes terminals, whereas the first draft's complement does not.

The statement W intersect C0=T and propagation of a winning strategy along a compatible finite prefix follow directly. The return-to-start case is repaired locally: if a chosen winning witness already reaches the patched start x0, propagation already makes x0 winning; otherwise patching introduces no return to x0. That case split needs no global acyclicity assumption. The later proposal to allow all winning successors has a separate termination issue, treated in G2.

## G2. One common winning strategy versus the greatest permissive strategy

Existence of one strategy winning everywhere on W does not imply that the union of all winning strategies is winning. With j controlling a,b, let R(a)={b,t}, R(b)={a,t}, and t a target terminal. The policy a→b,b→t wins from both a,b. So does a→t,b→a. Their union allows a,b,a,b,... and loses. All nonterminal choices are legal and each separate policy terminates in at most two moves.

There is nevertheless a precise conditional greatest strategy. Allow every move from a j-position in W to a successor in W. If the induced allowed graph has no infinite play from W, then propagation keeps every compatible play inside W; every terminal reached is in T. Hence this permissive strategy wins. The counterexample refutes the version without the termination qualification; it does not refute the manuscript's conditional version where the margin supplies that qualification.

## G3. Finite iteration and the difference between well-foundedness and finite height

Let C_i be the positions from which every finite path has at most i moves. Then C_0 is precisely the terminals and C_(i+1)={x:R(x) subset C_i}. Induction proves this characterization. Union_i C_i=C is equivalent to an N-valued strictly decreasing rank. It implies no infinite path. A finite directed graph with no infinite path has no directed cycle, and every path has at most |C|-1 edges; conversely a cycle produces an infinite path. In an infinite graph, absence of infinite paths alone need not give an N-valued rank.

For the explicit obstruction, take a root r controlled by the opponent, with one successor at the beginning of a chain of length n for every n≥1; every chain ends at a winning terminal. All maximal plays are finite and winning, but their lengths have no uniform finite bound. In the target-attractor iteration, every chain position enters at a finite stage, whereas r enters only after their union, at stage omega+1 (with the convention W_0=empty). Thus a union of only finitely indexed stages need not be all W. Every hypothesis of termination is satisfied.

If each opponent position has only finitely many successors, F preserves increasing omega-unions: the finitely many successor membership stages have a maximum. The existential clause needs no finite-branching assumption. Therefore omega iteration suffices in that case. On a finite arena, the increasing sequence stabilizes after at most |C| strict additions even if the original arena contains cycles. These are corrected sufficient hypotheses, not claims of what is written in the cancelled proof.

## G4. Compatibility, avoidance, and the restarted gluing proof

For any choice of nonempty allowed successor sets by every player, a maximal compatible play exists, using dependent choice if it does not terminate. If two distinct players have disjoint winning terminal sets, they cannot both force their own target from the same position: a play compatible with both strategies would have to end in both sets. A nonempty coalition of players with winning strategies similarly cannot force a terminal avoiding every member of the coalition. An empty coalition needs separate treatment; the contradiction has no selected player to invoke.

The restarted construction chooses, for every already-winning successor, a witnessing strategy. Its auxiliary set E must use the start of that witnessing tail, x1. If E instead means reachability from the original x0, a policy can be selected at a position it does not win from. The exact finite counterexample is in the computation output: root→a,b; each a,b can move to winning t or losing l; one witnessing policy is good at a only, the other at b only. Reading reachability from x0 allows the wrong policy to be selected at b. This raises the x0/x1 alarm; it does not change the transcription.

In the intended well-ordered selector, whenever the chosen witness changes, its index strictly decreases; a nonincreasing ordinal-index sequence along an omega-play is eventually constant. Its eventual tail then follows one fixed winning witness and must terminate. The eventual-tail argument is what blocks endless switching. Choice of a well-order and winning witnesses is a genuine set-theoretic assumption of this reconstruction.

Avoidance outside W only proves nonarrival in W. It does not turn an infinite avoiding play into a finite victory for some opponent. This distinction is necessary in the neutral/draw discussion and in the relative G*/P* classification. Nonexhaustive terminal labels also allow finite neutral outcomes.

## G5. Two-player alternation

An initiative function alpha on nonterminals extends to an alternating map C→Z/2 exactly when (i) each edge between nonterminals changes alpha and (ii) all nonterminal predecessors of any given terminal have the same alpha. Necessity is immediate. For sufficiency assign the terminal the opposite value to that common predecessor, choosing either value at an isolated terminal. This verifies the criterion without interpreting the final occurrence of alpha on terminals as already defined. A missing extension mark in that last displayed expression is a reading alarm.

## R1. Rearrangement pairing and equality

All functions below are nonnegative and finitely supported. Let f↓ be the decreasing list of values, padded by zeros. The rearrangement pairing is |f,g|=sum_k f↓_k g↓_k. The supremum over all permutations of either function is attained. A direct proof writes f=sum_i a_i 1_(A_i), g=sum_j b_j 1_(B_j), with strictly positive coefficients and nested nonempty superlevel sets in each family. For each pair, |A_i intersect B_j|≤min(|A_i|,|B_j|). Summing yields the bound, and equality holds precisely when every cross-pair A_i,B_j is nested. Since all coefficients are positive, a strict deficit in any cross-pair cannot be cancelled.

For equimeasurable functions this equality means f=g at the maximizing placement. Testing the pairing against all finite indicators gives the sum of the k largest values for every k, and successive differences recover the entire multiset. This proves the manuscript's dual test for equimeasurability.

The same layer decomposition proves f' weakly submajorized by f iff all partial sums of their decreasing lists are ordered, iff |f',g|≤|f,g| for every g≥0. With zero-based indices the first partial sum must be included: (2,0) versus (1,1) shows why tests beginning only at two entries miss the largest value. Weak submajorization is a preorder on functions; its associated equivalence is equimeasurability. It is an order only after taking that quotient. Abel summation or the level decomposition proves monotonicity in both entries and the asserted attained supremum over a submajorization class.

## R2. Convolution, peak extremality, and noncommutativity

Use (f*g)(x)=sum_y f(y)g(y^(-1)x), check(g)(x)=g(x^(-1)), left translation L_s g(x)=g(s^(-1)x), and right translation R_a f(x)=f(x a^(-1)). Thus (f*g)(s)=<f,L_s check(g)>. The unrestricted largest possible peak over rearrangements is |f,g|, also over functions weakly submajorized by f,g. Consequently the four peak-extremality criteria on scan20 are equivalent: universal peak maximization, its test at the identity, equality ||f*g||∞=|f,g|, and a translate for which the two nonempty level chains are jointly nested.

Putting g=f, equality in R1 gives check(f)=L_s f for some s. Applying inversion shows also check(f)=R_s f, so f commutes with that translation. Finite support is already a global hypothesis of the sheet; it is not a missing extra assumption for this corollary.

Peak extremality is not symmetric for arbitrary functions on a noncommutative group. In S3, take H={e,(12)}, s=(123), f=1_H, g=1_(Hs). The products have sorted profiles (2,2) and (1,1,1,1) respectively. Both rearrangement pairings equal 2. Hence (f,g) is peak-extremal and (g,f) is not. These are exact finite computations.

The manuscript's restricted symmetry is valid. If check(f)=L_a f=R_a f and check(g)=L_b g=R_b g, then check(f*g)=L_b(g*f)R_a. Thus f*g and g*f are equimeasurable. Reversing/inverting arbitrary competing factors transfers both peak and full-majorization extremality. This proof does not require arbitrary independent inner translations to preserve the condition.

## R3. Full extremality, the translation margin, and condition K

In a finite coordinate space, the set of nonnegative vectors weakly submajorized by f is the downward convex hull of its permutation orbit. One proof uses separating hyperplanes: because the set is downward closed, only nonnegative test vectors matter, and sorting them gives precisely the partial-sum inequalities in R1. Every finite collection of functions here embeds in such a finite coordinate space after padding by zeros. Positivity and bilinearity of convolution now extend the rearrangement-only criterion to all weakly submajorized competitors. Testing each resulting product against an arbitrary rearranged third factor, or against indicators of every cardinality, gives exactly the scan21 equivalent criteria. This proves the equivalence, rather than assuming the stronger criterion from peak extremality alone.

Arbitrary independent translations of the two factors cannot be inferred in a noncommutative group. In S3, (1_H,1_H) is fully extremal: total mass is 4 and every coefficient is ≤2, so its profile (2,2) majorizes every competitor. Left-translate only the second factor to 1_(sH). The profile of 1_H*1_(sH) becomes (1,1,1,1), which is not fully extremal. Outer translations, L_a f together with R_b g, are harmless because their product is L_a(f*g)R_b. All translations are harmless in an abelian group. The margin's unspecified word 'translation' is therefore an interpretive/ink alarm, not an automatically false intended statement.

If a family S is convolution closed and every pair is fully extremal, induction gives the multifactor full-majorization statement. The step applies the pair criterion to the preceding product, which remains in S. Full majorization always implies the associated peak bounds. Conversely, suppose S contains an indicator of every finite positive cardinality ≤|G| (condition K), and the multifactor peak inequalities hold. For each desired k, append a k-point indicator A in S as a last factor. The same peak property applied to the product in S and A identifies the canonical peak with |f1*...*fn,A|, the top-k sum. Varying rearrangements of A tests every top-k sum of a competing product. This proves the converse with K.

K cannot simply be dropped from the level-set argument. In Z/3 let f=(2,1,1)=delta_0+1_G and S consist of all translates of f^n, n≥0. Exact convolution gives f^n=delta_0+((4^n-1)/3)1_G. This family is convolution closed and every pair is peak-extremal. It contains singleton indicators (n=0), but not 1_G, even though G is a nonempty positive superlevel set of f. Thus the missing-cardinality problem is real.

## R4. Level closure and the final unfinished bridge

Assume S is translation closed, satisfies K, and all pairs in S are peak-extremal. For f in S and a nonempty positive superlevel E of size k, choose 1_A in S with |A|=k. The peak criterion makes a translated reflected A nested with every level of f; at cardinality k it must equal E. Self-extremality of A makes its reflection a translate of A, so 1_E belongs to S. Levels above max(f) are empty and require 0 in S; K for positive cardinalities does not supply that convention.

A finitely supported f is a positive linear combination of its distinct nonempty nested levels. Reflection up to one translation for f is equivalent to invariance of every level under the same reflected translation. The analogous expression for g yields the displayed bilinear expansion of f*g. Convolution closure places each A_i*B_j in S. It does not by itself show that the level chains of all these different products are jointly nested: the sheet explicitly says 'Supposons'. Under that additional joint-nesting hypothesis, their finitely many nonempty finite levels have a nonempty common intersection: take a member of smallest cardinality. Including the empty levels makes the claimed intersection empty. Neither the joint-nesting assumption nor surjectivity of doubling is proved by the last diagram.

## R5. The odd cyclic interval calculation for every size

This checks the finite-family assertion behind the 270 test cases, rather than inferring a theorem from the tests. Put n=2m+1, G=Z/n, E_i=[-i,i] for 0≤i≤m, and F_j=[m-j,m+1+j] for 0≤j<m, with F_m=G. E_i chains expand nonnegative symmetric functions decreasing with cyclic distance from 0; F_j chains expand the increasing ones, allowing a nonnegative constant term represented by G.

For h=1_(E_i)*1_(E_j), symmetry gives h(r)=h(-r), and for 0≤r<m,

    h(r)-h(r+1) = 1_(E_j)(r-i)-1_(E_j)(r+i+1) ≥ 0.

Indeed the cyclic distance of r-i from 0 is at most that of r+i+1: |r-i|≤r+i+1 and |r-i|≤2m-r-i, using r≤m and i≤m. This proves E*E is a nonnegative combination of the E-chain. Since F_j=G\E_(m-j-1), E*F is a constant minus an E-unimodal function and belongs to the F-cone. Likewise F*F is a constant plus E*E and belongs to the E-cone, since the actual convolution is nonnegative. Cases with a full-group factor are constant. This proves the two-family closure for every m, including composite n; no primeness is used.

The literature comparison must still distinguish this elementary two-chain closure from an unrestricted majorization theorem for all subsets of every cyclic group. Pollard's prime-order theorem and later prime-cyclic rearrangement theorems do not automatically establish the manuscript's much broader proposed family classification.
