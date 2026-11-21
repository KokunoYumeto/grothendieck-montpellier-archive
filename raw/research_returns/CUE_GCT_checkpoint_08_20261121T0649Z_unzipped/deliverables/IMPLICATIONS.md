# Implications and the remaining mathematical work

## GCT and P versus NP

The unrestricted asymptotic separation and polynomial ROABP hitting-set requests remain open in this run. The results establish exact bridges, restricted multiplicity identities, and smaller construction gates; no P versus NP separation or general PIT derandomization is claimed.

The moment-to-character bridge is exact after the correct Fourier projection. R01–R09 give the rectangular restriction identity, swap/tableau expressions, positive projector and Gram formulas, an exact ratios kernel for squared rectangular multiplicities, and the quotient numerator required for an orbit closure. Positive finite CUE dimensions alone do not force positive individual coefficients. R03 provides explicit counterexamples, and R04 shows why separate power-eigenvalue distributions do not determine the joint moments in plethysm.

The determinant boundary can be treated exactly in restricted sectors. All multiplicities with at most three rows equal their ambient plethysm multiplicities (G05). For determinant size four and at most four rows, G07 gives an exact subtraction by a determinant twist of degree D=320112. The certified permanent projection in R12 fills the quaternary coefficient space, so the same shifted plethysm term is exactly the permanent-minus-determinant multiplicity difference. In degree D+s the weight (D+4s,D,D,D) has difference one. This is a multiplicity obstruction in a fixed matrix-size case, not an occurrence obstruction or an asymptotic permanent lower bound.

R13 gives exact finite Jacobian certificates for quaternary permanent dominance in every size 1 through16 and a dimension exclusion for all larger sizes. R15–R22 give algebraic lower bounds on the quaternary permanent image dimension and prove four-row multiplicity gaps in an unbounded range of genuine padding. G10 supplies an explicit degree threshold. G11 strengthens the conclusion to the specified rectangular outer shape (nd/4)^4 on an explicit degree progression, including n=m+1 for every m>=8. R22 lowers the uniform threshold to every integer m>=2025 and m<n<4m/3, giving the exact eventual range for four-row outer rectangles. Its dimension estimate reaches every fixed ratio n/m<sqrt(2), eventually, including the necessarily nonrectangular sector above4/3. G13 gives a much smaller finite first-gap bound, with logarithm O(n²logn), while G11 retains its separate every-degree progression. G12 excludes these rectangular gaps for n>=4m/3 and makes the padded rectangular multiplicities zero when the inequality is strict. The new statements concern the location and multiplicities of representations, and do not improve the established quadratic border-determinantal-complexity lower bound; exact source context is retained in the paper. G08–G09 give explicit universal low-variable determinantal constructions, hence exclude low-row multiplicity obstructions above their displayed padding bounds. The asymptotic uniform-representation exponent in G09 is credited to Boralevi et al. (2017); the finite construction and GCT transfer are stated separately.

Hoza's graph isolation gives polynomial hitting sets for independent path variables (I01). General ROABPs require preserving the monomial quotient and coefficient dependence. I03–I04 identify the sufficient coefficient-flag and matroid-cone conditions; I14 gives a weaker joint-span condition. Exact exponent-filter simulation, exact energy cubature, fixed affine decoders and naive specialization have proved, construction-specific limitations. None of these is a lower bound against all polynomial ROABP hitting sets. I21 and its endpoint refinement I30 give a complete checked polynomial hitting set for width at most three in one unknown variable order, with six interpolation pairs, over any characteristic with the explicit working-field convention. I29 treats words with a single allowed singular interval rank. I31 uses full matrix cones to prove polynomial-size hitting sets for every fixed width, with a pair budget controlled by the number of distinct interval ranks. The rank-profile and cone mechanisms are credited to the recent unrefereed Liu preprint, and only the independently proved original-coordinate statements are used. The remaining uniform target is polynomial in the width as well as length and degree. The precise matrix-invariant consequence is the conditional implication I08; it needs growing widths, so its general antecedent remains unresolved.

Purity supplies useful objects once their functions and geometric complexity are controlled: sparse multilinear hitting sets, sparse isolating weights, curve restrictions and trace-space Gram bounds. P09–P10 show that polynomial hitting sets can have exponentially poor coefficient-energy conditioning, so near-isometric energy recovery is a stronger and unsuitable general surrogate. P11 proves that an explicit common algebraic evaluation point and an explicit integer hitting set are polynomially interconvertible in the stated rational-coefficient model. P12 and the general encoding P13 construct the common algebraic point, integral hitting curve, and exact trace-dual span recovery. The six-pair width-three map gives field degree (nD+1)^13. I31 gives the same construction for every fixed width with degree (nD+1)^(2K_R+1); its dependence on growing width is still too large. The construction is unconditional and uses the checked rank-profile map. The general-width arithmetic encoding remains open.

## Consequences for Grothendieck's programme

The common intrinsic objects are representation K_0 classes, integral orbit-coefficient maps, their determinantal rank strata, torus-induced coefficient filtrations and their special fibers. Analytic Haar or Gaussian covariance identifies the same image ranks over C. The positive Hermitian realization is not automatically an integral algebraic positivity statement or a motive. The separate dictionary in the paper supplies an exact locator and proof transport for each finding. The newer results add reductive invariant quotients and explicit Veronese algebras for the rectangular gaps, an integral cocharacter degeneration for their padding exclusion, local Artin rank charts for width-three preservation, and a finite flat arithmetic algebra with an explicit trace-dual basis.

Cote133 scan019 needs a categorical distinction: two-subsets, exterior squares and cardinality are different operations. The regular two-point C2-set refutes the equivariant reading of 2λ²(E)+E=E². The special-λ identity has ψ²(E) in place of E; augmentation recovers the numerical relation. This also corrects the supplied study's claim that the two equivariant descriptions agree. Scan006's universal product formula must include the terminal λ^i variable. The sign and index readings forced by the formal identities are listed in TRANSCRIPTION_NOTES.tsv.

No original scan image was supplied, so these are mathematical corrections and confidence assessments, not claims to have re-read the ink. The earlier study's name decision on scan008 and unrelated archive conclusions are retained with their original attribution. The finite symmetric-group lattice question is not silently resolved by Serre's theorem for split reductive group schemes.

## Analytic status

Alpöge's RH and Dirichlet GRH are accepted as stipulated theorem inputs. Supported Montgomery pair correlation and the explicitly Dirichlet-GRH-dependent Hughes–Rudnick first-zero conclusions are thereby discharged. Hughes–Rudnick's analytic mean, variance and restricted moments were already unconditional when complex ordinates were permitted. The actual support and uniformity limits are retained.

Masullo's claimed general Hecke GRH is used conditionally. The supplied index does not give a numbered theorem for the prompt's §1.2 claim. General cuspidal GL2 and symmetric-square GL3 target RH in ILS is distinct from one-dimensional Hecke-character GRH. The full arithmetic moment recipe, unrestricted correlation and spectral-chaos constructions retain their own missing hypotheses, explicitly named in the paper's dependency table.

## Audit

CHECK_EVENTS.tsv records actual complete proof readings, independent-agent reviews, finite integer/modular computations and source checks. These are model-assisted mathematical checks and reproducible finite certificates. They are not a claim of formal verification of the manuscript or a rebuilt Lean theorem archive. The ledger records actual checkpoint and review times; packaging is not counted as mathematical movement.


### First-jet refinement and dense interpolation limitation

G14 strengthens the necessary first-row condition for any four-row multiplicity obstruction against a degree-m form padded to degree n: lambda1 must be at least d(n-m)+2. The first-jet dominance is proved; the second- and third-jet target was subsequently resolved by G15 below. I26 refutes centered interpolation with a constant number of pairs as a uniform-in-width rank-test construction: its necessary pair count grows at least logarithmically with width. This is a limitation of that map, not a lower bound against general hitting sets; the displayed counterexamples admit simple cocharacter detection.


### Third jets and the strengthened obstruction boundary

G15 resolves the higher-jet target left open in G14. The full third-jet map of quaternary degree-m determinant images is dominant for every m; for m>=4 no fourth full jet can be dominant. Consequently every positive four-row padded-form multiplicity gap has lambda1>=d(n-m)+4. If its outer shape is rectangular, divisibility forces d(4m-3n)>=16. The proof uses explicit sl2 covariants and a positive Jacobi inverse-power norm, with no additional RH or general Lefschetz assumption. I27 rules out the specified coherent-seed filtering repair. I28 first reduced the width-three sampler to eight pairs; I30 subsequently reduces it to six. These constant improvements do not discharge the general-width gate.


### Exact arithmetic ranks and the rank-spectrum construction

R21 gives an explicit least-positive-eigenvalue bound for an integral Gram matrix and a compressed coefficient kernel whose weight-block ranks recover orbit-closure multiplicities by Weyl extraction. For every fixed ambient dimension, its exact bit complexity is polynomial in the numerical degree and coefficient bit length. Its exponent depends on the ambient dimension, so it is not a uniform polynomial GCT algorithm. Integral entries can be rounded at absolute error below one half; the much finer bound in the theorem concerns direct spectral thresholding and is not asserted to be necessary for exact integer recovery.

I31 sets d_w=w²−1 and d_s=(2ws−1)(2 max_{t>s} d_t+1) over the allowed rank set R, and proves that centered SV_K hits the class for K=sum_{s in R}d_s. With L allowed rank levels, K<=2w²(4w²)^(L−1). A bounded L therefore gives polynomially many interpolation pairs in w, while the displayed finite grid still raises the degree-length budget to that pair count. For all rank levels the present proof has K=2^{O(w log w)}. It closes the original-coordinate fixed-width gate, with full proofs of stable-block deletion and cone-preserving restrictions, and leaves both uniform width control and efficient sampling as substantive remaining requirements.


### Explicit nonrectangular labels beyond the rectangular boundary

G16 proves that every dimension-certified padded pair with n>m>=3 has a positive multiplicity gap at the exact shape (d(n−m)+md/4,md/4,md/4,md/4), with 4 dividing md. It gives both a first successful degree bounded by a number whose logarithm is O(n²logn) and an explicit progression on which every degree works. Unlike the rectangular family, this construction has no additional n<4m/3 stability condition. The proof adjoins an auxiliary dual line: the degree-d invariant space of the Segre-Veronese cone extracts exactly this Schur multiplicity, and the dual line cancels the padding weight at an explicit stable Fermat tensor. The dimension criterion itself is unchanged, so this does not extend the separation into the unrestricted asymptotic GCT regime.

For the certified pair (m,n)=(15,20), it gives shapes (35r,15r,15r,15r) at successful degrees d=4r. For (m,n)=(16,22), it gives shapes (10d,4d,4d,4d). Ordinary four-row rectangles are excluded in both cases by G12. The same label family applies to R20's unbounded nonrectangular strip.


### Exact four-row stretched-direction criterion

G17 extends G16 to every rational direction in the four-row partition simplex. For a pair satisfying dim(P_m4)+3>2n²+2, fix nu partition ns. Some positive stretch j has a padded-permanent multiplicity exceeding the determinant multiplicity exactly when nu4>0 and nu1>(n−m)s. If a condition fails, every stretch is excluded. If both hold, the theorem supplies an effective first-stretch bound and an explicit progression of successful stretches. The auxiliary partial-flag cone extracts just the selected Schur component and has an explicit stable point. This classifies stretched directions for the certified pairs; it does not decide positivity at an arbitrary individual stretch or extend the underlying dimension range.

### A refuted compression gate and a dense sampling construction

I32 proves that exponential dependence on width is necessary for preserving the entire matrix image cone by retaining original coordinates at every preserved common center. Its exact minimum is 3·2^(w−2)−2 positions, even though all interval ranks are already correct. One dense interpolation pair detects the displayed scalar, so the counterexample directs the next construction toward weaker invariants or dense sampling rather than establishing a general PIT lower bound. I33 gives n+1 polynomial-magnitude prime cocharacters for differences of two dense products, over every characteristic. It supplies an exact width-two counterexample to the raw family's product closure, then repairs that failure by a single interpolating curve. The restricted class already has polynomial PIT in the literature; the new proof and explicit family do not settle general growing-width cancellation.


### Every sufficiently large stretch, and an effective converse

G18 removes the progression restriction from G17, including rectangular directions. For every fixed nu partition ns with nu4>0 and nu1>(n−m)s, both orbit-closure multiplicities are positive at every stretch j>=beta². If c_m+3>2n²+2, the permanent multiplicity exceeds the determinant multiplicity for every j>=E(4u(pE)^(u−1)+1), with the quantities explicitly defined in G17. The proof varies the padding linear form to remove all projective automorphisms while staying in a common stable open. Separation of closed orbits then makes the degrees of nonzero common invariant sections relatively prime. An effective numerical-semigroup argument supplies every large degree, and multiplication transfers the standard-Veronese bounds to every residue.

For any fixed strict direction, the ratio of permanent to determinant multiplicities equals kappa_nu times j^(c_m−2n²+1)(1+O(1/j)), with kappa_nu>0. If 2n²>4m²−2m+3, in particular if n>=sqrt(2)m, determinant multiplicities eventually exceed the permanent multiplicities at every stretch, with a displayed effective threshold. Equality of dimensions still requires comparison of quotient degrees or lower Hilbert coefficients. This is a fixed-direction statement and does not establish orbit containment or settle finite-degree obstructions with changing labels.

Every fixed four-row direction eventually has no occurrence obstruction: the determinant multiplicity is eventually positive in the strict region, while the earlier containment arguments give the opposite weak multiplicity inequality on the two excluded faces at every stretch. The positive gaps proved here are therefore necessarily multiplicity obstructions after enough stretching.

### Weaker isolation conditions that survive dense substitution

I34 proves that a local coefficient-matrix nullity bounded by c in a sum of separated products is handled by changing at most max(1,c) coordinates of one prime cocharacter. The family jointly preserves coefficient spans over the working extension. All sums of at most three products need just one changed coordinate; a tensor-rank-four example is killed by every entire one-coordinate cylinder. Sampling still has an exponent depending on unbounded local nullity.

P14 proves that a scalar ROABP with every factor of rank one or full rank is hit by a common center plus w−1 interpolation pairs. A rank-one factorization splits the output, after clearing pivots, into nonzero scalar bridges; the same dense map preserves all bridges simultaneously. This covers every width-two ROABP with one pair, with established width-two PIT and rank-one splitting explicitly credited to AGKS. The construction preserves coefficient rows, while general intermediate-rank matrix contractions remain unresolved. The corresponding arithmetic point follows directly from P13 with K=w−1 over the rational coefficient model.


### The dimension bound reaches every fixed ratio below its ceiling

R22 proves 4m²−20m^(3/2)+2 <= dim(P_m4) <= 4m²−2m+2 for m>=99. Its arbitrary-size staircase uses one simultaneous pencil deformation. A common integer choice of the untwisted motif parameters works for all required bidegrees; coprime-factor intersections and exact Schur determinants prove the simultaneous row/column ranks. The proof does not add ranks from unrelated pencils or extrapolate a finite list of computations.

For every fixed 1<rho<sqrt(2), all integers m<n<=rho*m are dimension-certified once m>=max(99,ceil(100/(2−rho²)²)). In particular the exact eventual rectangular range m<n<4m/3 holds for every m>=2025. More finely, m>=169 and m<n<=sqrt(2)*m−4sqrt(m) suffice. G17–G18 then classify all four-row stretched directions and compare every sufficiently large stretch. The row/column torus ceiling forbids this dimension argument from passing n>=sqrt(2)*m, and G18 gives eventual determinant dominance along each fixed strict direction there. The unresolved dimension transition is confined to an O(sqrt(m)) strip below that ceiling. The unrestricted GCT regime with superlinear padding, changing directions, and efficient Schur-Gram minors remains open.

The additional G17 quantitative corollary bounds log2(j_*) by log2(u+1)+u*log2(p)+(2u+1)*log2(beta). This is O(n^5 log(s+1)+n²log n), and O_s(n²log n) for fixed s. The stretch, original coordinate degree and label entries thus have polynomial binary length in n and log(s+1). Their bounded description length is separate from an efficient algorithm finding or certifying the multiplicity gap.


### The exact remaining dimension defect is homological

R23 proves c_m=4m²−2m+2−epsilon_m, where epsilon_m is the degree-m dimension of Tor_1^R(R/J_m,S), J_m is the permanent gradient ideal, and S is a general four-variable linear restriction. All lower-degree Tor_1 pieces vanish generically. The complete full-variable linear-syzygy theorem supplies exactly2m−2 relations, which remain independent on the section; every additional differential relation is measured by this one Tor piece. R13 gives positive exact defects for sizes3 through16, so simply restricting the known full-variable resolution would be invalid. A full regular-sequence argument is also obstructed by the known gradient-ideal height. The required degree-m vanishing for m>=17 remains unproved.

P15 closes a tested simplification negatively: one ordinary centered interpolation pair fails for an explicit minimum-width-three polynomial at four fourth-root Lagrange nodes, even though every transition factor and interval product is invertible. The same quadratic gives balanced rational-evaluation counterexamples at harmonic rational nodes, including a subset of the standard integer grid. The paper separates those coordinate conventions. These counterexamples leave the proved six-pair width-three map and the general-width target intact.


### Exact sizes17 and18, and a constructive induction gate

R24 proves c17=1124 and epsilon17=0. R25 gives a conditional induction with the exact increment8m+2, obtained from first- and second-derivative columns on a ternary section and coordinated third-order tangent cancellations in one bordered quaternary pencil. Its fully checked size17 antecedent proves c18=1262 and epsilon18=0. Thus the exact-dimension target is now a uniform rank condition for every m>=18; no extrapolation from the finite certificates is made. New padded dimension-certified pairs include(17,n),18<=n<=23, and(18,n),19<=n<=25. The endpoint directions(41r,17r,17r,17r) at(17,23), and(46r,18r,18r,18r) at(18,25), lie beyond the rectangular padding boundary and are covered by G17/G18.

### A concrete rectangular copy and its positive energy

G19 packages the classical smooth-section discriminant separator as one explicit rectangular highest-weight polynomial with exact Haar energy and an integer Gaussian expectation at least1 on the permanent, while both vanish on the determinant. Its cubic instance has degree80 and weight(48^5); the displayed five-variable permanent slice has a completely specified Macaulay smoothness certificate, reconstructed independently entry by entry. Four-row determinant-cubic equations vanish identically, so five rows are minimal for such a specified equation. This does not infer a gap between total multiplicities of that isomorphism type: the full isotypic restriction ranks remain separate data. The same discriminant vanishes on every positively padded form, so it does not supply an asymptotic GCT separation.

In Grothendieck's language, this is a determinant-character line on a coefficient scheme, a closed projective incidence image, and one Schur submodule with two different restriction maps. EGAII5.4.1 and5.5.3 supply the exact properness locators; the SGA3/SGA6 dictionary retains the full representation information rather than only its rank. The finite smoothness minor gives a principal open arithmetic certificate. No pure sheaf or motive is inferred from the positive compact norm.

### The remaining seed-composition requirement

I35 proves that scalar boundary preservation only needs equality of rank-one annihilator base loci. It can hold after generic matrix rank drops, and an existential2r−1-dimensional test space suffices. Independent seed sets compose over the rational function field of all other variables, with the displayed sampling exponent. Reusing seeds is a distinct diagonal pullback and can kill the result even when every separate block preserves its entire coefficient span. The explicit multiplicative-corner obstruction also rules out a lift that both makes a rank-r reset rank one and recovers an arbitrary matrix entry by one fixed linear readout. The unresolved constructive target is synchronization for the actual neighboring boundary functions, with budgets polynomial jointly in the original width and length.


### Centering cannot be omitted from the two-pair refinement

P16 gives eighteen explicit algebraic nodes over a field of degree at most72 and a nonzero degree16 multilinear polynomial of minimum ROABP width three in every variable order, killed by ordinary uncentered SV2. The proof starts with four rational functions on disjoint pole sets satisfying one exact quadratic relation, then reverses the multilinear coefficient basis and applies the exact Lagrange diagonal rescaling. Every resulting transition factor is generically invertible. P14 therefore proves that the centered SV2 map hits the very same polynomial. This separates the two maps concretely and blocks an attempted removal of the center. It does not decide centered SV2 for rank-two resets, nor assert failure for arbitrary preassigned interpolation nodes. The construction also explains why an unbalanced rational-map reduction needs additional structure: its large-degree ideal elements can have width three.


### One pair preserves maximal minors of singular-factor words

I36 proves that a centered one-pair interpolation map is dominant on every coordinate pair. Exterior powers turn the maximal minors of a word of generic-rank-at-most-r factors into a rank-one matrix word; after exact pivot clearing, its contractions factor into univariate and adjacent bivariate polynomials. They all survive that same map. This supplies the complete rank-two-preservation stage for width-three words with singular variable-dependent factors. Adding the already checked four-pair rank-one completion gives centeredSV5, with exact evaluation bound (D+1)((n−1)D+1)^5 binom(D+5,5), in every characteristic with the stated working-field convention. The bound for unrestricted width three remains six pairs, and the proposed two-pair bound remains open. The integer arithmetic encoding P13 consequently has exponent11 on this singular-factor rational subclass, by direct substitution K=5 in its proved formula; the general width-three exponent remains13.


### Linear defect and a constant remaining padding strip

R26 replaces the earlier O(m^(3/2)) permanent-image defect bound by the uniform exact inequality 0≤epsilon_m≤6(m−18), m≥18. Its proof uses seventeen independently verified finite character cores, algebraically valid normalized cut limits, exact vertex insertions, and the R25 border increment. Consequently c_m≥4m²−8m+110 and every integer pair m<n with n²≤2(m−1)²+53 is dimension-certified for the G17/G18 strict-direction conclusions. The remaining uncertainty near the four-variable dimension ceiling has bounded additive width in n. Combining the bound with the exact small-size certificates proves the exact four-row rectangular padding range m<n<4m/3 for every m≥14, with G12 excluding its complement. This sufficient threshold is not claimed optimal. The whole main asymptotic GCT separation and polynomial positive extraction are still open.

### Two centered pairs for affine singular width-three words

I37 proves centeredSV2 for all nonzero multilinear width-three words whose variable-dependent factors are affine and generically singular, in arbitrary unknown order and every characteristic. The exact grid has (D+1)((n−1)D+1)^2 binom(D+2,2) points. Its key argument splits an irreducible scalar across no rank-one interior interval, preserves all rank-two intervals at a one-pole center, and then forces every adjacent passive excursion to vanish if two-pole annihilation were assumed. The rational arithmetic encoding P13 therefore has degree at most(nD+1)^5 on this class. The earlier singular-factor result I36 still applies to arbitrary individual degree with exponent11, while unrestricted width three retains exponent13. Variable-dependent full-rank factors can transmit the passive state and remain a concrete obstruction to extending this new proof. The general growing-width polynomial PIT and associated matrix-invariant normalization targets remain unresolved.


### Isolated invertible affine factors also need only two pairs

I38 extends I37 to width-three affine words in which no two consecutive variable-dependent factors are generically invertible, after constant factors have been absorbed. The one-pole center dominates every three coordinates, so it preserves the rank-one exterior-square connectors through one invertible factor. Its two tangent directions force the bandwidth-two Hessian to vanish in every characteristic. The exact sample count and P13 arithmetic exponent5 are unchanged. The adjacency promise survives the required irreducible multilinear specialization. Longer full-rank runs and nonlinear singular factors remain outside this proof; the growing-width main gate is unchanged.


### Exact dimension closes the four-row transition

R27 proves dimP_(m,4)=min{binom(m+3,3),4m²−2m+2} in every size. In particular the graded Tor defect vanishes for everym≥17. A fixed124x91 boundary coefficient matrix, its first two epsilon coefficients and the Toeplitz ranks84/172/262 certify four first-order and two second-order directions. All33852 entries were independently regenerated. The proof separately establishes the first-order upper bound4, the agreement of projected and full quotients, and insertion to all sizes; the computation is not extrapolated.

G20 consequently settles the exact eventual sign in every fixed strict four-row direction. For m≥17 the permanent side is larger exactly when n²≤2m²−m+1, and the determinant side is larger exactly when n²≥2m²−m+2. No integer equality case remains; the finite smaller sizes are tabulated. The four-row rectangular range m<n<4m/3 holds uniformly fromm14. This threshold is sharp for eventual dominance: m13,n17 and direction(17^4) give ratio kappa*j^(−17), hence eventual determinant dominance. No conclusion excludes every isolated earlier-degree gap in that example.

G21 extends the image dimension to all ambient variable counts r≥4: for m≥17 it is r m²−2m+2. Independent cofactors yield a disjoint tangent block of dimensionm² for each extra variable. The specified Tor1 pieces through degreem vanish. This does not compute higher-row multiplicities or establish exactness of the whole restricted resolution.

### Two failed mixed-word repairs are now explicit

I39 gives an irreducible multilinear affine width3 scalar on seventeen specified nodes whose strict internal rank2 interval falls to rank1 under ordinary centeredSV1; the scalar is nevertheless hit by that same map. It also gives a nonzero semiseparable Hessian family satisfying the three tangent kernels and the additional-pole quadratic identity, while explicitly failing fixed-polynomial Hessian integrability. These counterexamples block the proposed intermediate invariants, not the centeredSV2 sampler. The full scalar annihilation condition and the coordinate-ring constraints remain essential. General growing-width polynomial PIT, its matrix-invariant normalization consequence, and the unrestricted GCT separation remain open.


### Higher-row strict directions and a preserved affine isolation invariant

For n>m>=17 and4<=r<=m, every fixed partition direction nu ofsize ns with nu_r>0 and nu_1>(n−m)s has both multiplicities positive at every sufficiently large integer stretch. Their ratio has exponent r m²−(r−2)n²−2m+r−1. G23 proves that this integer never vanishes and gives explicit thresholds for either sign. G22 constructs the common stable tensor by an ordered Fourier frame and exact one-parameter initial weights; R28 removes all projective symmetries by a cyclic product-plus-power family and a generic padding line. This extends the asymptotic comparison beyond four rows, but does not give a polynomial positive extraction algorithm, decide every finite degree, or prove a superlinear-padding lower bound.

P17 excludes balanced two-pair multilinear width-three annihilators through eight variables and all cubic annihilators through ten. I40 then closes nine variables by retaining the Borel character of each coefficient-support determinant line. Each square full-rank affine core consumes its whole rank from a total character budget; weight one permits only isolated full-rank cores and falls under I38. The exact finite balanced grid has at most(n+1)² binom(D+3,3) points with the stated working-field size. The next small balanced case is a translation-invariant ten-variable quartic of weight two. No joint polynomial bound in growing width follows.

The Grothendieck transport uses split torus character lattices, Borel-stable support bundles, determinant exterior operations, cocharacter initial terms, Cartan cone coordinate algebras and projective invariant quotients. These are exact dictionaries to the listed SGA3, SGA6, EGA and FGA locators; they do not identify complex moment-map witnesses with integral arithmetic points or supply missing original archive scans.


### Rectangular equality boundaries are also controlled

G24 completes the higher-row rectangular comparison for m>=17 and4<=r<=m. Eventual positive gaps occur exactly for m<n<r m/(r−1). At equality the padded invariant algebra injects into the lower-variable permanent invariant algebra; its Hilbert growth is strictly smaller than the determinant invariant algebra, with an explicit every-degree threshold. Above equality the padding cocharacter sends every form to zero and every positive-degree permanent rectangle vanishes. Forr4 the earlier all-degree weak boundary exclusion remains valid; forr>=5 G24 proves an eventual statement and does not rule out individual earlier-degree gaps. Nonrectangular boundary faces and rows beyondm remain the next comparisons.


### Strict directions through2m−2 rows and a degree-two direction with exponent one

R29 supplies the common stable and projectively free point through2m−2 rows, using a prescribed-spectrum product lemma and an orthogonal sum of two products. G25 extends every exact sign and explicit constant of G23. Among the added rowsr>m, positive eventual gaps occur precisely atr=n=m+1. The partitionnu=(3,2^(m−1),1) withs2 is an explicit such direction for everym>=17; its ratio is asymptotic tokappa*j in degree2j. This is a comparison of total multiplicities. It does not assert every earlier degree or a superlinear-padding lower bound. G24 retains its exact eventual rectangular range throughm rows.

I41 closes the homogeneous common-translation-invariant weight-two width-three case and then all balanced two-pair width-three inputs through ten variables, in every characteristic and unknown order. Its new connector has a nonzero square coefficient that survives one-pole evaluation; the three tangent directions kill the resulting bandwidth-three Hessian. The finite balanced grid remains(n+1)² binom(D+3,3). Arbitrary center slopes and ordinary unweighted centeredSV2 are not promoted to this entire class. The general growing-width polynomial sampler remains open.


### Every fixed direction throughm rows has an eventual classification

G26 proves that on the equality face lambda1=ad, a padded multiplicity is at most the permanent multiplicity of the tail partition in one fewer variable. Below that face it vanishes. For n>m>=17 and4<=r<=m, the lower enhanced quotient has strictly smaller dimension than the determinant quotient, and separate no-scaling points give an explicit threshold valid at every integer stretch. Thus eventual positive gaps in every fixed full-row direction occur exactly when the padding inequality is strict and the G23 integer dimension exponent is positive. This closes nonrectangular equality faces in this range as well as rectangles. R30 and the G25 endpoint addendum extend the strict-direction classification through2m rows. They do not settle larger-row boundary faces, changing directions or the superlinear-padding complexity separation.

P18 gives20(n+1)² balanced samples for an arbitrary-length trilinear three-block width-three class; a smallest unrestricted cubic counterexample has at most two shared boundary variables. I42 shows that the actual rank-one reset structure removes the Hessian obstruction through four invertible cores in all characteristics and five outside characteristic2. Its seven-/eight-node abstract examples show these thresholds are exact for that algebraic criterion; they are not polynomial annihilator counterexamples. Saturated determinant budgets supply the rank-preservation hypothesis for the stated irreducible higher-weight classes. The next weight-three gate is a shorter nonsaturated two-core connector.


### All cubic balanced width-three instances are resolved

P19 removes the variable-count restriction from the cubic theorem. Its proof forces a smallest counterexample to have a three-coordinate support transversal, which is impossible for the third exterior power of the Vandermonde kernel. The uniform sampler has20(n+1)² points in every characteristic over the stated working field. Reversal and lowest-component inheritance restrict any remaining width-three annihilator to homogeneous degrees4 throughn−4. This is a genuine degree reduction, without a polynomial-in-growing-width PIT conclusion.

R31 identifies a residual scalar character that prevents the current two-product common family from furnishing a no-scaling closed point in certain strict2m+1-row directions. The obstruction is internal to that family. New common families or separate stable constructions on the two full cones are still available approaches.


### Nonrectangular directions and weight-three tensors

R32 and G27 extend the complete eventual nonrectangular classification through2m−1 rows for m≥17. A nonrectangular auxiliary flag provides period one on the determinant comparison algebra. The lower tail algebra may remain periodic: every nonzero residue has a large complementary degree, which is enough for the upper Hilbert bound. This closes additional equality and below-face directions without assuming generic rectangular freeness or equality of two degree semigroups.

I43 proves the balanced two-pair sampler for every homogeneous translation-invariant multilinear width-three tensor of weight n−2D≤3. A Grassmann-line input restricts its actual adjacent support enough to make the middle compound affine, and all connector and endpoint tests use one shared parameter field. Combined with the full cubic theorem, this proves the sampler for every multilinear width-three input on at most11 variables. The next general weight4 and growing-width PIT questions remain distinct.


### Generic stabilizers and all short torus-chain connectors

R33/G28 remove the need for a lower stable point in the boundary comparison. The exact tangent kernel and nonzero Plucker coordinates force a generic projected permanent to have finite projective stabilizer whenever4<=q<m². Quotient fibers then give only an upper dimension bound, which suffices. The complete eventual nonrectangular classification reaches2m rows; on/below-face comparison extends to r<=min(2n−2,m²). Generic finite stabilizers are never identified with closed or stable orbits.

I44 classifies every minimal singular anchor into a three-weight torus chain. A quadratic residue condition then proves one-pole rank preservation through five full-rank cores. Combined with the sharp reset criterion, this resolves all weights≤4 in every characteristic and≤5 outside characteristic2, and hence all multilinear width-three inputs on≤12 variables or≤13 outside characteristic2. General growing-width sampling and characteristic2 weight5 remain open.
