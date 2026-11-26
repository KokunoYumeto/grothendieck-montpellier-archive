# Exponent and field audit

Status: ongoing research; Q3 is not settled in its unrestricted interpretation.

## Checked original statements

- EX-01: 4/3 is the optimal exponent of Anthropic E.10's parameter inequalities.
- EX-02: the OpenAI expander computation yields 5/4 with its stated selector charge.
- EX-03: exact global two-hub bounds for orthogonal diameter terminals: fan-in saving at most 2m; no shortening at bridge width h >= m sqrt(c).
- EX-04: these bounds prove an exact 5/4 barrier for equal-width orthogonal diameters, two hubs, and a selector budget with log A = Omega(k).
- EX-05: binary-seed convexity certificates for the cross-polytope have minimum cost sqrt(k). This is not a lower bound on actual spectral unit-tensor exponents.
- EX-06: finite-extension descent of strict shortening, independently checked by /root/shortening.
- EX-07: existence of strict shortening depends only on characteristic, using fixed-layout polynomial equations, Zariski's lemma, then EX-06.
- EX-08: a complex shortening would descend to a rational one and transfer to all but finitely many prime characteristics.
- EX-09: supplied B7.1--B7.3 are valid fixed-instance separation arguments but do not decide characteristic two or universal price claims.

Full proofs: exponent_audit.tex.

## Routes tried and remaining gaps

1. Optimize the given two direct cases. Completed; gives the stated exponents but not an unrestricted supremum.
2. Allow arbitrary hub motion in the orthogonal model. Completed globally by the geometric median of orthogonal points and the convex supporting hyperplane at the origin; no small-displacement assumption remains.
3. Improve E.9 by a different binary midpoint tree. Refuted within that certificate class by a trace/Cauchy lower bound sqrt(k).
4. Extend to arbitrary endpoint geometries. Substantially advanced by EX-16--19: Banaszczyk vector balancing connects the binary selector certificate to a balanced-cut resultant, and a new exact global saving bound handles arbitrary antipodal directions. The exact exponent supremum is 4/3 for the explicitly defined all-cut, binary-selector, integer-width, arbitrary-two-hub model; a universal claim beyond this model remains unjustified.
5. Use B7 to pass to characteristic two. Not valid without controlling exceptional primes. Replaced by characteristic invariance within a characteristic and an almost-all-primes shortening corollary.

## External references inspected

Hoory, S., Linial, N., & Wigderson, A. (2006). Expander graphs and their applications. Bulletin of the American Mathematical Society, 43(4), 439--561. https://doi.org/10.1090/S0273-0979-06-01126-8. Primary author-hosted search result: https://www.math.ias.edu/~avi/PUBLICATIONS/ABSTRACT/hlw06ab.pdf. No downloaded file yet; exact theorem/page not used in a new proof.

The original expander lower-bound construction is cited to the attached OpenAI source, rather than silently treating an unchecked expander citation as independently verified.

## Further checked reductions

EX-10 gives alpha=1+1/(2(1+beta)) from an endpoint-selector scale O(k^beta). EX-11/12 show cut-based graph-rank inequalities cannot force sqrt(k) selector scale: all such tests give at most 1+1/sqrt(2). EX-13--15 prove price cones depend only on characteristic by constant-cover descent and Strassen spectral extension.

Independent checks passed for price_geometry's all-fields tree inclusion via WZ singleton anchors and its tree contraction factor mu=4,s=15/8. Its file owns those proofs.

The ALP2026 explicit higher-mode anchor examples provide tree wire metrics. Their existence of new spectral points is not evidence of non-tree price metrics. Liu2026 Hexagon2611.00972v1 was discoverable in primary search but direct full-text retrieval was blocked (HTTP403); its proof has not been checked or used.

## Broader exponent barrier (EX-16--19)

Completed full proofs in exponent_audit.tex. For a graph with maximum local bit load B, arbitrary antipodal unit endpoint directions, and binary-seed selector certificate cost C:

- EX-16: some balanced cut has resultant O(BC), by a zonotope-to-ellipsoid reduction and Banaszczyk's vector-balancing theorem. A second balanced cut has resultant at most sqrt(BW), where W is total edge load.
- EX-17: for opposite hubs, some balanced cut has exact global free fan-in saving at most 472B. This uses Banaszczyk to balance one principal direction and control the transverse resultant, then an exact lower bound on Euclidean distance. No small-displacement approximation is used.
- EX-18: charging at least a*k*C for all balanced cuts forces kC=O(B); useful bridge width is O(B min(C,sqrt(k))), hence O(B^(4/3)). Complete-network geometry attains the exponent, conditional on the attached flat-case reduction.
- EX-19: independently placed arbitrary two hubs still have exponent supremum 4/3 for positive integer edge widths. Root supplied the sorted adjacent pairing idea; this agent checked the mixed-block issue, supplied its two-regime repair, and wrote the full proof. Matrix Rademacher concentration yields some balanced cut with exact global saving O(B log d). Integer widths imply d<=W<=kB/2. Selector feasibility and C>=2 imply log d=O(log B), so h=O(B^(4/3)*(log(2+B))^(1/3)). This excludes every fixed exponent above 4/3 while preserving the attained 4/3.

The binary selector debit is a model condition, not a proved lower bound on the actual spectral GHZ exponent. More hubs, genuinely stronger selector bounds, different circuit decompositions, or non-antipodal target layouts remain outside this theorem. Positive real widths tending to zero leave a log d factor unless direction count is separately bounded.

Independent checks by /root/shortening passed for EX-16--19, including all norm, matrix variance, mixed-block, balance, and exponent computations. Parent /root independently verified the cited Rademacher tail theorem and the exact norm inequality.

## Additional reference verification

Dadush, D., Garg, S., Lovett, S., & Nikolov, A. (2019). Towards a constructive version of Banaszczyk's vector balancing theorem. Theory of Computing, 15(15), 1--58. https://doi.org/10.4086/toc.2019.v015a015. Theorem 1.1, p.2, states the exact Banaszczyk theorem used. Original source: Banaszczyk, W. (1998). Balancing vectors and Gaussian measures of n-dimensional convex bodies. Random Structures & Algorithms, 12(4), 351--360.

Tropp, J. A. (2012). User-friendly tail bounds for sums of random matrices. Foundations of Computational Mathematics, 12(4), 389--434. https://doi.org/10.1007/s10208-011-9099-z. Exact source used: author preprint/arXiv1004.4389, Theorem 4.1 and inequality (4.4), p.14; Theorem 1.2, p.4, gives the one-sided version. PDF downloaded and hashed. Both the formula and the Rademacher extension sentence were read.

PG-EDGE-RIGIDITY independently checked: full-unit normalization forces the embedded triple's unit exponent to equal one when one wire is saturated; ALP v2 Proposition8.1 then puts the third party on the saturated edge, and CAT(0) uniqueness puts all parties on one interval. This does not show all prices are lines, because a price cannot in general be freely renormalized to have saturated normalized diameter.

## Further selector route and cross-checks

EX-20 extends the 4/3 supremum barrier to all pointwise-averaging certificates whose seeds have at most a fixed number q of points and whose seed debit is at least the image diameter. An explicit binary refinement costs at most q-1 times the original debit. This includes stronger three-party seed estimates; they cannot improve the exponent through averaging alone.

EX-21 records a different failed route: the constant-mass cut mixture places the normalized cross-polytope endpoint profile in the convex hull of ordinary flattening profiles, so every linear wire-exponent inequality is insufficient to force a growing selector scale. Geometric means of flattening ranks do not yield a valid spectral extension. An explicit pair of wires has functional values sqrt2,sqrt2, but direct-sum value3; this violates both cover subadditivity and the additional monomial-dominance hypothesis of ALP2026 Theorem3.9 p21 by a fixed exponential factor.

Independent checks additionally passed for PG-CROSSPOLY-GATE, PG-FOUR-CORE, PG-FIVE-CORE-FAIL, RT-SOS-UPPER, and the root graph-image border-substitution limitation. Their owning files contain the complete statements and proofs; these checks are recorded with scope in the event ledger.

## Robustness of the exact graph restriction obstruction

Independently checked SH-19, including the crossed edge pairing identity and all operator-Schmidt rank inequalities. No border or asymptotic extension follows from its proof. EX-22 adds two precise warnings: MM_q cannot restrict exactly to GHZ_(q^2) at any equal-size power, yet its asymptotic subrank is q^2 (WZ Theorem4.22 p58); and an explicit six-term degeneration of MM_2 retains full local flattening ranks but lies outside its restriction image. The latter example does not have SH-19's stronger same-blocked-orbit hypothesis.

The minimal canonical form paper, arXiv2209.14358v1, was read at Theorem4.11 p23, Proposition4.20 p30, and Section7 p45. Its local uniform gauge-orbit theorem requires all contraction graphs, and nonuniform fixed-graph canonical forms are explicitly left for future work. Molnar et al.1804.04964v1 gives exact injective/normal gauge equivalence, not bounded-gauge or relative-closedness estimates. Landsberg-Qi-Ye1105.4449v2 Theorem3.0.3 pp4-5 demonstrates critical-cycle nonclosedness. None was used to assert a robust K3,3 obstruction.

The variable-size refinement of EX-20 gives h=O((q-1)^(1/3) B^(4/3) (log B)^(1/3)), with constants independent of q. Thus subpolynomial-size seed gadgets remain inside the 4/3 exponent barrier; an improvement by epsilon requires seed size at least order B^(3epsilon)/log B within the stated averaging model.

Foundational checks passed for PG-SAT, arbitrary-field stars and three-party metrics, and the finite-building sqrt(rank) realization. Their detailed proofs remain in price_geometry.tex.

## Arbitrary common-origin radii (EX-23)

The Q3 exponent barrier now covers every target wire segment passing through a common origin, with arbitrary and possibly unequal endpoint radii. Positive integer widths, arbitrary graphs, independently placed two hubs, and the all-balanced-cut selector debit akC remain assumptions. The proof introduces simultaneous matrix covariance whitening within Banaszczyk vector balancing, combines O(log B) radial bands, and obtains h=O_a(B^(4/3)log B). Root independently re-proved the full argument and constants. The matching equal-radius construction remains available under the original flat-case reduction.

For seeds of size q, with original average debit K0, the proof uses K0 to set the radial cutoff and binary-refined cost Cprime<=(q-1)K0 only in the resultant estimate. This yields h=O_a((q-1)^(1/3)B^(4/3)log B), uniformly in q.

The Bugár-Vrana geometric-mean interpolation route was also inspected. Its exact evaluation on graph tensors with flat marginal spectra is established only for norm-homogeneity parameter alpha>=1/2, while restriction-monotone spectral points correspond to alpha=0. The required matching lower bound at that endpoint is not provided by their theorem. This route has not improved the actual spectral GHZ selector scale.

## Seed refinement and the seven-point gate

EX-24 improves the binary-refinement factor for a q-point seed from q-1 to min(q-1,sqrt(2(q-1))). The construction uses an unbiased Rademacher binary reconstruction around the seed centroid. Consequently the equal-radius and arbitrary-common-origin barriers have q^(1/6), rather than q^(1/3), dependence. A fixed power improvement epsilon requires q at least order B^(6epsilon)/(log B)^6 in the radial model. This remains a certificate-model statement, not an actual spectral GHZ lower bound.

EX-25 records a rigorous failed approach: all 65,935,860 orbit-reduced distinct pentagons in Mat3(F2) were tested using integer upper bounds, with every upper bound negative. The general reason is stronger and has a short independent proof: the square root of every pseudometric satisfies every pentagonal inequality. Deza and Maehara (1990), Theorem1 pp664-665 and Corollary2 p667, additionally show every six-point square-root metric is L1. The original article was read through a full-text mirror; no unobserved downloaded PDF or hash is claimed.

Root then deleted one negative-character point from SH20. Independent re-proof gives a seven-point odd-hypermetric quadratic form6(2sqrt3-sqrt2-2)>6/25, with four plus and three minus coefficients. The previous stability error42/256 is smaller than6/25, so the same explicit contraction factor survives if the K4,3-to-K4-disjoint-K3 asymptotic-cover gate holds. Shortening owns this theorem as SH29. Six-point L1 embeddability shows this seven-point witness is minimal in point count for any L1 inequality on any submetric of sqrt(rank), without claiming minimality for arbitrary spectral obstructions.

Independent audits passed for the new all-dimensional capacity border obstruction and its K_(r,r-1) generalization, now in price_geometry.tex. The crucial steps are multiplicativity from critical orbit-closure minimizers, invertibility forced by equal local dimensions and full target flattenings, and the capacity slice minor. Polynomial invariants bound diagonal capacities away from zero while norms force off-diagonal capacities to zero; capacity continuity is not assumed. Extra asymptotic width or a GHZ cover destroys the invertible-square-map argument, so neither result settles the asymptotic cover gate.

## Arbitrarily many star hubs (EX-26)

The 4/3 fixed-power barrier now also covers r=2^t star-connected hubs, with r dividing the vertex count, unit antipodal endpoints, integer widths, and an all-equal-partition selector debit ak(log2 r)C. The bound is uniform in r: h=O_a(B^(4/3)(1+log(2+B)/log r)^(1/3)). The free-saving partition uses random permutations within sorted principal-coordinate blocks, a total transverse-energy bound, and matrix Bernstein. Separate partitions control all group resultants by O(BC) or2B sqrt(k/r). Parent independently re-proved the entire argument; shortening independently checked the partition lemmas. General bridge trees and arbitrary radii are outside this additional theorem.

The crossing-operator R2 gate in price_geometry.tex also passed an independent audit. A preserved exact-rational verifier checks the16-dimensional common-projector certificate and its squared norm18. The raw endpoint upper functional has value at least2^(3/2) on the opposite-wire product, but the required semiring power regularization can lower this value. Its strict lower bound above2 is still open; the raw finite-block certificate is not a price.

## Arbitrary fixed connected hub graphs (EX-27 and EX-28)

EX-27 first extended the method to a fixed labelled tree under uniform angular curvature and sufficient average width per group. Exact-size permutations and a Doob sampling-without-replacement argument gave simultaneous interval bounds; tree summation by parts absorbed the residual after grouping consecutive hubs. Tropp2011 Theorem1.2/Corollary1.3 supplied the matrix Freedman estimate. Root independently re-proved this complete scoped argument.

EX-28 removes both extra geometric hypotheses. A recursive sorted-pair partition keeps every dyadic principal-coordinate discrepancy at most2B and is a valid adaptive pipage output for each fixed dyadic block. Harvey–Olver2014 final Theorem3.11 allows an arbitrary symmetric shift outside the two logarithms, giving the needed centered matrix Bernstein estimate for PSD blocks, including the lower tail by reversing the swap parameter. Positive semidefinite vector lifts and full curvature whitening yield simultaneous matrix and resultant controls. Averaging both objects over consecutive groups makes every tree-edge residual depend on only two partial blocks. The matrix residual costs twice its operator norm per unit bridge length; together with the vector residual this gives the6M absorption bound.

The conclusion is h=O_a(B^(4/3)log(2+rB)^(2/3)+B log(2+rB)log r), for r=2^t>=2 dividing k, unit antipodal endpoints, positive integer widths, and the prescribed selector debit ak(log2 r)C. Both root and shortening independently re-proved the complete argument and constants. For any fixed M>0 and r<=B^M, the fixed-power supremum is4/3 in this model, using the earlier two-hub construction for attainment. Fixed-size seeds are permitted; a growing q-point seed adds rho_q^(1/3)=O(q^(1/6)) to the first term.

Deleting edges to a fixed spanning tree extends the result to every fixed connected labelled hub graph with all bridge widths at least h. The statement bounds the minimum bridge width and requires feasibility for every labelled equal partition, assigning groupj to hubj. The graph, labels and assignment are fixed before that partition is selected. A graph or permutation chosen after seeing the partition, arbitrary radii with many hubs, and a better actual spectral selector are not covered. The remaining distinction between a certificate debit and the actual spectral GHZ cost is therefore still substantive.

## Radial many-hub completion and adaptive graphs (EX-29 and EX-30)

EX-29 extends the fixed labelled graph result to arbitrary endpoint radii on segments passing through one common origin. A paired Banaszczyk halving keeps group sizes exact and simultaneously controls five blocks per radius band. Covariance whitening gives the PSD recursion ||M_child−M_parent/2||<=K sqrt(R||M_parent||); its complete geometric summation has constants5 and5. Bandwise radial clipping is compatible with tree variation because its radius factor cancels. Separate averaging scales for the radius bands absorb half the bridge cost, while the remaining band objective is bounded both by its free-saving estimate and by its certificate flow. Optimizing these two bounds gives h=O_a(log²B log(rB)[B^(4/3)+B log r]), hence O_a,M(B^(4/3)log³B) for r<=B^M. Both root and shortening independently re-proved the full argument. The dimension in the bootstrap is explicitly the span of retained directions after radial truncation.

EX-30 allows the graph and assignment to depend on the partition, at a cost of a factor r: h=O_a(r B^(4/3)[logB log(rB)]^(2/3)/(log2r)^(1/3)). Its two partitions use all-subset resultant bounds, so no fixed preorder is needed. It follows that subpolynomially many adaptive hubs and subpolynomial seed sizes still have fixed-power upper exponent4/3. Root and shortening independently verified the proof and quantifiers. Attainment in all these supremum statements remains conditional on the supplied flat-case reduction used in EX18. Polynomially many adaptive hubs, target segments without a common intersection, and an actual spectral selector cheaper than the charged certificate remain open in this analysis.

## Cycle-cover normalization, arithmetic and crossing exponent

The new PG cycle-cover chain passed an independent audit. A coefficient-one integer-energy degeneration shows asymptotic subrank4 for the binary four-cycle over every field. Taking each source dimension fixed before the tensor-power limit permits an O(N³) coefficient cover; the connected source supplies its polynomial GHZ overhead in o(N) extra copies. This gives the normalization c<=2 for a unit-square price c*d_psi.

The universal cycle-cover regularization therefore has exactly two possible values on the opposite-wire tensor:2 when the square is absent and2^sqrt2 when present, conditional on the checked price-space chain. Grouping each cover term by its smaller crossing cut rank yields chi<=u, while an opposite-party slice gives chi>=q/2. Together with RT-SOS and RT-SOS-UPPER this produces crossing exponent exactly1 orsqrt2, without deciding which case occurs. A finite strict cover can also be amplified directly into a planar shortening using multinomial profiles and cycle resources for their GHZ selectors.

Finally, no complex square is equivalent to bounded-width finite cycle certificates for infinitely many primes, and equivalently for all sufficiently large primes. Forward specialization uses a number-field witness, residue degree at most d, and d³ four-party coefficient descent independent of tensor power. One fixed power absorbs that overhead uniformly. The converse follows because bounded width and strict cost allow finitely many source formats, so Nullstellensatz excludes all but finitely many primes if no complex solution exists. This does not decide the prime2 case.


## Sparse covers, geometric limitations and low-party folds (EX31--35)

EX31 proves the canonical-basis sparsity obstruction A(uv)^r>=q^(r(r-1)/2), including border covers. It excludes partial-permutation and polynomially sparse matching shortcuts at the growing-party gate, while leaving dense local maps unrestricted. EX32 gives a pointwise-closed CAT0 metric family containing all finite Euclidean and tree configurations yet satisfying a strict rank-step contraction. It is explicitly a geometric model, not an actual spectral-price class, and therefore identifies why tensor-specific information is essential for mutual exclusion.

EX33 proves and sharply attains the finite-characteristic cross-commutator bound p^n<=d² without same-side commutation. Thus the proposed polynomially large family of Weyl pairs cannot exist. EX34 shows every folding of the balanced Krr-to-two-Kr problem into at most three superparties permits an exact conversion, and every folding into at most four permits one after tensor square. The four-group proof uses explicit half-integral two-commodity routing; its cross-capacity slacks are perfect squares. Any asymptotic obstruction must retain at least five superparties.

EX35 independently verifies the classical binary four-cycle sextic and evaluates it at crossed Bell pairs. It gives a one-copy border obstruction in every characteristic other than two, although the tensor-square conversion exists over every field. The exact expansion has144 monomials, all coefficients +/-1 and gcd1, so dividing by2 cannot repair the vanishing target value in F2. No characteristic-two border conversion is asserted. The parent independently re-proved EX31--35.

The balanced Krr border gate is still unresolved. All cross-pair blocked maps must be invertible near the target, but existing exact PEPS gauge theorems do not provide the required simultaneous bounded original-edge gauges. Christandl et al.2024 Theorem21 assumes acyclic hypergraphs and does not close this cyclic-network gap. Eleven exploratory modular Jacobian evaluations for binary four-cycle MPS had rank15; the stronger primary BDG theorem identifies its degree-six hypersurface. No numerical rank observation is used to infer dominance or membership.

The independently checked PG equality-slice lemma also proves that a q-dimensional identity slice cannot factor with total cheaper-cut rank exactlyq for q>=3: a square factorization would give a2q-dimensional module for the2q-generator CAR algebra, whose nonzero modules have dimension divisible by2^q. This argument is valid in characteristic2. No rectangular-factorization strengthening was established.


## Explicit characteristic-two border conversion (EX36)

The characteristic-two branch left open by EX35 is now resolved by an explicit polynomial family. With E=diag(0,1), X the2x2 exchange matrix, local slices A=(I,tE), B=(I,X), C=(tE,I), D=(I,X), the integer contraction equals2*1[a=0,c=1]*delta(b,d) +t*delta(a,c)*delta(b,d)+t²*1[(a,b,c,d)=(1,0,0,0)]. Modulo2 this is tP+t²U, so the same-field border conversion exists over every characteristic-two field. Exact conversion remains impossible over every field: a rank-one member of the first matrix pencil forces the opposite pencil proportional if the target is crossed Bell pairs. Parent and shortening independently verified both arguments.

The image-closure statement also has an independent exact certificate. The sextic is irreducible over algebraic closure F2: connected SL2^4 invariance forces any proper factorization to have a quadratic invariant factor; the unique such factor is H, but an explicit binary H-zero point has sextic value1. The quadratic unipotent constraint system has rank7 on the8 allowed monomials. A displayed15x15 Jacobian minor has integer determinant−1. Thus the15-dimensional image closure is the irreducible sextic hypersurface. These checks, the polynomial family, and all their data are preserved in the updated ex_cycle_sextic program/input/output trio.

This provides a concrete counterexample to relative closedness based solely on invertibility of all adjacent two-site blocked maps, in characteristic2. It does not decide the complex version or balanced K33 conversion, and it does not improve an asymptotic exponent because the tensor-square routing conversion already holds over every field.

Independent checks also passed for PG's corank-one linear-factorization extension, and for Singh2026 Remark9's all-field4n/3 lower bound after swapping parties3 and4. No unexecuted Lean proof or outline-only theorem is counted as independently verified.


## Balanced border exclusion by overlapping orbit tangents (EX37)

A new all-field theorem excludes G_r(q)=Krr(q) degenerating in one term to H_r(q)=twoKr(q), for everyr>=4 and everyq>=2. Grouping any perfect matching gives a critical complete-graph tensor with q²-dimensional edges. The source image closure lies in every corresponding grouped orbit closure, while H belongs to each open orbit. Their common tangent is computed by splitting each edge-state space as<I> plus a complement. A pair of active edge subsets survives every matching exactly when their sets of incident vertices have total size>r. Forr>=4 this leaves precisely the ordinary physical tangent of H. The source image is irreducible and contains distinct deleted-matching graph orbits of that same dimension, yielding a contradiction. An explicit gauge-family dimension sandwich proves the orbit dimensions and separability in every characteristic, without invoking a blanket isotropy theorem. Parent and shortening independently re-proved the full analytic argument.

Forr3,q2, the common tangent has dimension154. A fixed binary parameter point has Jacobian rank160 modulo2 and101; a preserved155x155 minor has determinants1 and95 respectively. Thus the border exclusion also holds overC andF2. The six site images each have dimension32, each five-site sum138, so quotient maps isolate22 dimensions per site. Tensor-product points yield rank at least132*32^(N-1), exceeding the common tangent dimension atq=2^N for everyN>=2. Reductionmod101 transfers that Jacobian lower bound to characteristic0. This extends the binary result to every equal-size tensor power.

The main asymptotic cover gate remains open. Indeed ordinary first-order grouped-orbit tangents become entirely uninformative for two terms: each grouped secant contains H+tT for every tensorT in a nondegenerate orbit cone, making its tangent atH the full ambient space. Higher-order information is required to control selector overhead or sums of restrictions.

The finite-field trace and tangent certificates are original verified computations, not numerical optimization claims. Their exact inputs, retained minors and outputs are preserved in the ex_cycle_sextic and ex_balanced_tangent program/data trios.

### 2026-11-25 01:07:56 UTC — independent EX37 certification

Root independently reconstructed the complete integer Jacobian and matched its hash, both modular ranks, the selected minor residues, and all site/five-site ranks. The independent verifier is `programs/rt_verify_balanced_tangent.py`, with output `outputs/rt_balanced_tangent_verification.json`. Root and shortening independently checked the binary-power quotient extension; root also checked the secant-tangent failure boundary. These results exclude a single equal-size border conversion, not the asymptotic cover gate.

### 2026-11-25 01:52:42 UTC — causal coding and stabilizer selector boundaries

EX38 proves the exact deterministic-code-to-graph-tensor transfer over every tensor scalar field, separately from the alphabet of the code. It then proves that every causal linear code respects every increasing concave transform of matrix-rank distance over its coding field: inject vertex-matrix mismatch errors along edges, factor the boundary mismatch through their image spaces, and use generic compression plus the discrete concave expansion. Root and shortening independently re-proved this. The new all-field realization of the specific SH20 eight-point metric makes the barrier applicable to that witness in every coding characteristic, without claiming a cross-characteristic realization of all binary matrix-rank metrics.

The new Zhang–Li–Li paper was downloaded from arXiv and its scalar-code definition and reversible integer mechanism were read. Its full construction and Lean proof are not adopted as checked theorems. Jain et al.2005 Theorem4 also blocks a direct classical causal specialization to the balanced complete-bipartite code at unit rate.

I independently verified RT-STABILIZER-SELECTOR in full, including postselection, arbitrary weighted matrices, common radicals, GHZ rank, and the exact rank-distance defect. It forces b>=Nr²/6 for4|r. The global Clifford/Pauli selector search was therefore stopped. Its programs and complete diagnostic states are preserved under ex_stabilizer names; no negative numerical result is treated as an impossibility proof. The known four-term r3 routing seed verifies the search implementation's target test. A sum of separately chosen Clifford local maps need not admit Clifford selector control, so general coherent covers remain outside this barrier.

### 2026-11-25 02:15:56 UTC — nonconcurrent geometry and adaptive-topology boundary

EX39 is a concrete countermodel to extending the fixed-tree4/3 barrier to existentially chosen adaptive singleton-hub trees. A B-regular bipartite graph, endpoints±1, and a type-dependent two-star hub tree have fan cost0 and only one positive-length bridge. The exact cost calculation allows h=Theta(kB), hence h=Theta(B^(M+1)) whenk=Theta(B^M). This is not an actual circuit decomposition; it demonstrates why that quantifier cannot be omitted. Root independently audited the construction.

EX40 proves the equal-length two-hub4/3 upper barrier with completely arbitrary segment centers. The crucial spring relaxation uses only each target difference vector. Crossed-edge curvature is a quadratic Rademacher chaos, but exposing opposite-pair signs gives a martingale with variance<=BQ/2, and full whitening gives<=B/(2q). Root checked the entire proof.

EX41 permits arbitrary positive lengths: the same proof gives a3/2 ceiling, and the aspect-ratio bound retains4/3 for bounded or subpolynomial length spread. The remaining full4/3 gap is simultaneous principal control and quadratic cut-curvature concentration across radial scales; the existing linear-matrix Banaszczyk argument cannot simply be substituted.

A disk-full write temporarily truncated the owned TeX. It was restored from checkpoint08, and removing the new EX39 insertion was verified to recover the checkpoint bytes exactly. All subsequent manuscript/ledger writes are atomic.


## 2026-11-25T02:28:44Z: EX42 removes the arbitrary-length two-hub gap

The quadratic cut-curvature obstacle is resolved by a two-stage auxiliary-partition construction. First use independent vertex signs solely to choose U,V with sufficient crossed-edge curvature in every retained dyadic length band. Sign U by the existing Banaszczyk selector/principal/transverse/count blocks. Conditional on these signs, each V vertex has a symmetric signed incident UV-curvature matrix H_v. The UV contribution to the final cut is exactly one half of Q_UV minus its signed H_v sum, so curvature is now a linear signing constraint. Weighted Cauchy gives sum H_v² <= BQ_UV and full-whitened variance <= B/q. A second Banaszczyk application on V handles those matrix blocks together with the vector/count blocks. All covariance estimates hold uniformly in the U signs. No independent-sign concentration is claimed for the final signing.

Safe constants in the written proof yield simultaneous resultant <=100mBC/r_j and free spring saving <=2^23(m²+m ell)Br_j. The old truncation, dyadic minimum sum, and integer-load logarithmic bootstrap give h=O_a(B^(4/3)log(2+B)) with completely arbitrary positive segment lengths and centers, exactly two hubs, and prescribed binary certificate debit akC for every balanced cut. Attainment remains conditional on the supplied flat-case circuit reduction. Actual spectral selector normalization and additional/adaptive hubs are outside this result. Parent and shortening are checking the complete written proof; both independently passed the decoupling mechanism.


## 2026-11-25T02:32:47Z: independent Cauchy ansatz audits

PG-CAUCHY-CLASS passes by a direct all-r Ferrers-margin re-proof, including its all-field symmetric quotient. PG-CAUCHY-COMMUTANT passes both algebraically and by an independent integer program. The new ex_verify_crown_commutant.py enumerates internal edge assignments instead of the source checker's boundary-entry products, checks5832 quotient coordinates, computes six unit determinants by permutation expansion, and verifies the unit bare-sum discrepancy. Output ex_crown_commutant_independent.json. This excludes the six-term local permutation-algebra lift only; it is not a general dense-cover lower bound.


## 2026-11-25T02:53:28Z: EX43 endpoint-only actual selector gate

EX42 has now passed both root and shortening's full independent audits. EX43 makes a separate reduction of the actual spectral selector question. Define Gamma_k as the minimum scaling factor realizing the Euclidean cross-polytope on2kparties by an ordinary normalized spectral point. Spectral compactness plus the spanning-tree unit restriction proves attainment whenever this metric is a price. Iterating AnthropicA.7 with the original GHZ tensor and all old wires in the anchor preserves both the metric and g(P)=1; this normalization survives the midpoint completion by compactness. A balanced-block square-only rigidity proof improves the usable flat-ball radius to2^(-ceil(log2k)/2), so after endpointscale1/2 all E.10 hubs lie inside it. Roundness additionally preserves distances from the original endpoints outside that ball to the hubs. The same scale and original partialGHZ value therefore realize the entire required hub family.

Consequently Gamma_k=O(k^beta), for all sufficiently largek, implies the direct exponent1+1/[2(1+beta)], conditional on the supplied circuit reduction. This is now a question only about ordinary spectra on the2kendpoints. No improved Gamma growth bound is proved: E.9 givesGamma<=sqrtk, andGamma>=1. Root independently re-proved the full statement and passed it. Sources A.7/E.8 and AKP2011Theorem5.4p11 were read directly.

## EX44: finite-cover dual for endpoint normalization (2026-11-25 03:17 UTC)

For the complete endpoint wire tensor W_k and resource costs m times the product of r_e^(d_e/t), the power-regularized minimum cover cost equals the direct wire cost exactly when Gamma_k<=t. A strict finite cheaper cover of some power witnesses Gamma_k>t. Normalization p_t(1)=1 follows from all resource costs>=1, even when t<1; saturation at W_k (without anchoring GHZ) forces every wire bound, and the full-unit exponent alpha<=1 gives ordinary scale t*alpha<=t. This is an exact dual reformulation of EX43, not a new bound or review movement.

## 2026-11-25 03:21 UTC: full multiplicity operator audit

Independently proved the new PG operator/SOS duality step, including the real symmetric commutant annihilator, complex symmetric rank factorization, and explicit fixed-q polynomial Kronecker multiplicity bounds from Schur-Weyl. Conditional on the square price and the checked RT-SOS chain, this supplies nonzero-trace high common-crossing vectors at every h<sqrt2 log2q for all large Schur powers, and hence the missing uniform p0 lower bound. This identifies the regularized operator gate with the existing square dichotomy but does not select a branch.

The finite positive central tests also now have an independent complete group-word enumeration. The new Heap/reversed-representative verifier checks5378 exact class-conditioned sums across six cases and rechecks all positive witness/dual arithmetic with Fraction. See programs/ex_verify_pt_word_counts.cpp/.py and outputs/ex_pt_word_counts_independent.json.

## EX45: actual-selector two-hub ceiling

The3/2 ceiling uses only a common selector debit akG withG>=largest target length, not a binary averaging certificate. An actual scaled partial-GHZ exponent has this lower bound by restriction to each endpoint wire. EX41 free saving<=20000BLell forcesk=O(BlogB); the separate balanced resultant bound givesh<=B sqrt(k/2). Thus exactly two arbitrary hubs, arbitrary segment centers/lengths, and the stated common debit admit no fixed power>3/2. This is not an unrestricted circuit-method ceiling because the akG debit and two-hub decomposition remain explicit assumptions. Conditional4/3 attainment yields an interval[4/3,3/2] in this expanded model.

## EX46: actual selectors with arbitrary endpoint geometry and fixed many-hub graphs

A weighted geometric median removes the remaining common-origin restriction for the3/2 ceiling. Subgradient equilibrium supplies the zero total resultant used by EX28, even when some endpoints coincide with the median. The exact endpoint norm lower bound has denominator4R, whereR is maximum median radius; targetcost<=median star cost, so the median relaxation is an upper bound on available saving. All EX28 covariance and near-line arguments use only the listed v/H hypotheses, which hold with traceA<=W. Thus actualG>=endpointdiameter>=R yieldsh=O(B^(3/2)log(2+rB)/sqrt(log2r)+B log2r log(2+rB)). Fixed labelled polynomially many connected hubs retain fixed-power ceiling3/2. The ak(logr)G selector debit and every-labelled-equal-partition requirement remain assumptions. Shortening independently passed the substantive proof.

## Adaptive actual-selector countermodel clarification

EX39 now explicitly uses the ordinary flattening price on its two locations, scaled2, so actualG=2. For k=2B^M and h=W/2, the abstract cost remains below target at the postulated2aklogk selector charge. The same flattening shows any real cover needs logA>=W-h, making actual bridge-plus-selector cost at least target. Thus the geometry countermodel persists with known selector normalization, but the required cheap algebraic identity is impossible.

## EX47: subpolynomial adaptive actual-selector model

The median free-saving bound survives arbitrary later topology choices. An independent local-swap partition controls every group-subset resultant by rB sqrt(s), so every connected graph selected after the partition has bridge threshold at most that value. Thus h=O(rB^(3/2)sqrt(log(2+rB)/log2r)). Subpolynomially many adaptive hubs retain3/2 fixed-power ceiling; polynomially growing adaptive hubs remain outside this conclusion, and EX39 explains why an unrestricted geometric barrier cannot simply omit topology quantifiers.

## EX48: graph-certified seed refinements

Any finite pointwise average of seeds whose normalized graph loads satisfy every terminal cut admits a binary refinement at at most twice its cost. Goemans–Williamson's Steiner cut-LP factor2 supplies a tree, then randomizing its edge-cut increments preserves the seed pointwise. Thus the cross-polytope cost remains at least sqrt(k)/2 even with arbitrarily many seed and auxiliary vertices. All existing prescribed-binary-debit exponent barriers transfer with a constant change. This does not lower-bound actual Gamma or compel an actual selector to pay this certificate cost. The primary source and the full proof are now EX48; shortening independently checked the LP and binary conversion.

## Shared deficit and exponential-moment audits

SH55d's precise145/143 shared-edge inequality independently passes and excludes all width-six two-term dimensions at least13. An independent threshold13 version also passes. The new integer quadratic majorant supplied to shortening excludes the three-term dimension12 case from E kappa²<2809 and Var kappa<=216: E2^(kappa-72)<337/1024+2^-32<1/3. Shortening independently passed it and owns SH57. Neither proof assumes ranks equal network capacities.

## Independent top-tail certificate audit: dimensions 5, 6, and 7

The standalone semantic verifier `programs/ex_verify_top_tail_certificates.py` does not import or execute either generator. It reads only the certificate data and reconstructs each used inequality from its mathematical label: indicator boxes, tail-count/level monotonicity, 12-Lipschitz neighborhood propagation, integer second moment, exponential rank average, and fixed top counts. Every rational Farkas multiplier is nonnegative. All 39 certificates have every variable coefficient cancel exactly and right-hand side exactly -1. The independent report is `outputs/ex_top_tail_certificates_independent.json`; it hashes every certificate and the current corrected D6 metadata.

Folded Q5 growth is independently enumerated over all 65,536 subsets for every radius, using quotient distance min(Hamming,5-Hamming) on four-bit representatives. Ordinary Q5/Q6 growth is independently computed from all-pairs Hamming distances of simplicial initial segments; its universal extremality uses Harper's theorem. The remaining top-tail ranges are pruned by exact squared-moment lower bounds: D5 gives8064>7802; D6 gives22752>22471, or22564>22471 in the refined q36=10,q35>=11 branch; D7 gives61884>61173. The D6 cap follows strictness: the real bound22472 gives integer cap22471. Thus each dimension has complete branch coverage. The failed unrefined q36=10 solver result is never treated as a certificate.

The same interval also independently checked the ordinary Harper layer computations for D8..12 and the all-field multi-cut B2/PT-rank upper bound in PG-MULTICUT-UPPER. The latter reaches the Euclidean exponent sqrt(d), excludes the particular Rossman-Zhu F2 identity candidate in their stated growing-d regime, and supplies no shortening or circuit separation.

## Sharp square obstruction for graph-certified seeds

For P2={±e1/2,±e2/2}, every graph certificate with all terminal-separating cuts at least rho has normalized Euclidean cost at least sqrt2. For a planar direction u(theta), integrating threshold cuts gives sum_e b_e |<u,Delta_e>| >= rho times the directional width of the terminal convex hull. Integrating theta from0 to pi gives twice the graph length on the left and rho times the perimeter on the right. The P2 square has perimeter2sqrt2. A half-loaded boundary cycle attains this fractional-cut bound.

The same lower bound survives any pointwise average of such seeds: first project each seed graph to the target plane, which only decreases cost; expected directional width is at least the width of the expected labeled terminal positions, since max and negative min are convex. Thus no graph-certified seed averaging can prove Gamma2<sqrt2. This does not prove Gamma2=sqrt2 for actual spectral selectors. A proposed multiplicative endpoint inequality Gamma_(kl)<=Gamma_k Gamma_l also remains unproved; A7 provides no arbitrary product closure of spectra.
