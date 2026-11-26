# Price-geometry investigation

## State

Main questions Q1b and exact four/five-party Q2 classifications remain undecided. The exact three-party classification has a proof via support-functionals and upper-functional saturation. The statement that flat Euclidean configurations would themselves violate the contracting inequality is incorrect: all Hilbert-valued maps on Mat_2(F_2) satisfy the strict factor 3/2 in squared distance, and this is sharp.

## Source audit

Anthropic Definition D.1 (p.30) is D(mu) <= s D(1), where 1 <= s and s^2 < mu. The bound from CAT(0) is D(mu)^2 <= mu D(1)^2. The square roots are lost in some PDF text extraction lines; formulas must be checked against the PDF. Theorem D.2 proves NOT contracting => flat, and does not prove exclusivity.

Targeted audit of A.5, A.7-A.8, B.3, C.1-C.3, D.2 found no fault, with the dependency qualifications recorded in price_geometry_checks.tsv. This is not an audit of either full circuit lower-bound proof.

## Literature located

1. Christandl, M., Vrana, P., & Zuiddam, J. (2018 preprint version 3; later journal publication). Universal points in the asymptotic spectrum of tensors. arXiv:1709.07851v3. Upper-support axioms: Theorem 2.4, p.11. Upper/lower comparison: Theorem 2.15, p.13. Oblique-tensor exact formula: Theorem 2.19, pp.15-16. https://arxiv.org/pdf/1709.07851 .
2. Sakabe, K., Dogan, M. L., & Walter, M. (2026). Strassen's support functionals coincide with the quantum functionals. arXiv:2601.21553v1. https://arxiv.org/html/2601.21553v1 . This closes universality over C for singleton upper support, but does not change its star wire metrics.
3. Botero, A., Christandl, M., Fraser, T. C., Leigh, I., & Nieuwboer, H. (2026). On quantum functionals for higher-order tensors. arXiv:2604.18283v1. https://arxiv.org/html/2604.18283v1 . Laminar upper/lower quantum functionals do not generally coincide. New universal spectral points are anchored on robust subsemirings. Cannot treat every laminar quantum upper functional as a universal spectral point without this extension step.
4. Lytchak, A. (2026). Euclidean filling inequalities in CAT(0) spaces. arXiv:2611.13159v1, Proposition 1.4 p.4, proof Section 13.1 pp.23-25. https://borowiecki.dev/pdf/2611.13159 . Equality in integrated CAT(0) variance inequality forces flat convex hull. Root has a shorter elementary cross-polytope rigidity proof, so this reference is optional rather than a required proof dependency.

## Rigidity independent check

Suppose f:B^D -> X is 1-Lipschitz into CAT(0), preserving all D coordinate antipodal distances. Set r_1=1 and r_k=2^{-(k-1)/2}. Assume f is isometric on r_{k-1} B^{k-1}. For any unit u in the first k-1 coordinates, the four points ±r_{k-1}u, ±r_{k-1}e_k have their antipodal distances preserved. Roundness-2 and the nonexpansion inequalities force all four side distances to be sqrt(2)r_{k-1}. The flat rectangle theorem fills their convex hull isometrically. The map f coincides with this filling because it is nonexpansive and its values at the endpoints of each relevant segment are at exactly the segment length. Hence the diamond |a|+|b|<=r_{k-1} in span(u,e_k) is mapped isometrically. Every x in r_k B^k lies in such a diamond, so f preserves x,-x. For arbitrary x,y in that ball, apply roundness to x,y,-x,-y and use the Euclidean parallelogram identity to see that all four nonexpansion inequalities on the sides must be equalities. This proves the induction. It also explains why f must be defined on the whole ball: knowing only endpoint distances would require an additional convex-hull rigidity argument.

## Gates and attempted methods

- Explicit singleton support/quantum spectra yield every star metric, but cannot produce a Euclidean square. This does not classify all spectra.
- The price class is closed under positive scaling and limits. Calling it a convex cone needs proof: sums of two price metrics need not be prices (four-point l1-square counterexample conditional on established CAT(0) theorem).
- CAT(0) structure alone does not decide contraction: PG-BUILDING now proves that square root of rank difference embeds in a type-A building cone and saturates D(n)^2=n D(1)^2 for every n. Price membership is unproved.
- Hilbert spectral-gap computation refutes the proposed Euclidean-cube shortcut to exclusion. Flatness and contraction may overlap; no proof of overlap in the actual price class is supplied.
- Root and shortening agent are proving no-shortening iff flat. That still leaves contracting iff shortening open unless contraction and flatness are shown disjoint.

## Further proved reductions (2026-11-24, after first checkpoint)

- PG-SQUARE-GATE: over any field, a Euclidean square is a price if and only if every finite planar Euclidean configuration is a price, if and only if some finite price is not a tree metric. A nontripod CAT(0) triangle produces a positive-angle planar sector in a tangent cone; finite tangent metrics are scaled limits of price metrics. This does not yet yield arbitrary Euclidean dimension.
- PG-TREE-ALL: all finite tree pseudometrics are prices over every field. Wigderson-Zuiddam Theorem12.23 (Section12.7,p121) gives singleton pendant addition; cherry induction gives arbitrary trees; EX15 transfers from F(t) for finite fields. Independent confirmation by exponent agent.
- PG-TREE-CONTRACTION: tree-valued maps on Mat_n(F2) satisfy D(n)^2<=4(1-2^-n)^2D(1)^2. For n4 the explicit strict factor is s15/8. Thus square absence implies contraction with fixed explicit parameters. Full proof in tex.

The smallest unsettled metric gate remains the Euclidean square. If it is absent, the price classes on three/four/five parties are exactly tree metrics and contraction follows; if it is present, all planar Euclidean metrics are prices but higher-dimensional flatness and coexistence with contraction require further argument.

## Fixed-dimensional gate (2026-11-24 21:07 UTC)

PG-CROSSPOLY-GATE proves, for each fixed D>=2, equivalence of: Euclidean crosspolytope vertices are prices; vertices plus center are prices; every finite Euclidean D-configuration is a price; no strict shortening in dimension D. The new geometric step is CAT(0) Kirszbraun extension of the finite isometry to a nonexpansive whole-ball map, then SH07 rigidity. Thus the square is a price iff there is no strict planar shortening. Combined with PG-SQUARE-GATE and PG-TREE-ALL, strict planar shortening exists iff all finite prices are tree metrics. This leaves the binary alternative undecided.

Primary extension theorem checked: Alexander, S., Kapovitch, V., & Petrunin, A. (2011). Alexandrov meets Kirszbraun. Proceedings of the Gökova Geometry-Topology Conference 2010, 88–109. Author PDF https://www.math.toronto.edu/vtk/kiszbraun-gokova.pdf, Theorem5.4 p11 and Theorem5.1 p9 (author-PDF pagination), SHA256 a48e7597045a2f9cf250e304646b1700de1a94e4e5cbd50c160e4b59c6e4df3e, 645517bytes. Original Lang–Schroeder1997 theorem identified; its publisher fulltext was inaccessible, so the accessible primary alternate proof supplies the precise cited statement.

## Four-party gate sharpened (2026-11-24 21:20 UTC)

PG-FOUR-CORE proves that every four-point CAT(0)-embeddable metric is the sum of a planar Euclidean core metric and nonnegative singleton pendant lengths. The proof uses the sign pattern of a negative Schoenberg witness and a continuous radial pendant removal that decreases three comparison angles until their sum is2pi. Independently re-proved by exponent_audit, including the degenerate cases. PG-FOUR-CONDITIONAL therefore gives an exact conditional classification on four parties: if the square is absent, exactly tree metrics; if present, exactly all CAT(0)-embeddable metrics, equivalently the weighted quadruple inequalities. This works over every field. It still does not decide which alternative applies to C or F2.

Toyoda, T. (2020). An intrinsic characterization of five points in a CAT(0) space. Analysis and Geometry in Metric Spaces,8,114–165. https://doi.org/10.1515/agms-2020-0111. Published Definition1.1p114, Example1.2p115, Theorem1.3p115, Theorem1.7p116. Source read via publisher PDF in web tool; direct publisher download returned empty, so archived author arXiv1907.09074v3 PDF at sources/external_Toyoda_2020.pdf (726945bytes; SHA256 3d211d8cca90a6a34589610dedb9569420819fd0c3c98aa37aa9af361eafd46b). URL https://arxiv.org/pdf/1907.09074v3. No source copy is for delivery. Toyoda gives exact CAT0 embeddability also onfivepoints; a price converse onfivepoints remains under investigation.

## Five-point pendant route fails (2026-11-24 21:22 UTC)

PG-FIVE-CORE-FAIL is an explicit counterexample to extending PG-FOUR-CORE: the Euclidean3D configuration with square vertices +-e1,+-e2 and fifth point(1,0,1). Its four distances to the square are(1,sqrt3,sqrt5,sqrt3). Flat square rigidity eliminates all base pendants; the squared-distance parallelogram identity then eliminates the fifth pendant, leaving an impossible planar realization. Independently checked by exponent_audit. This does not show the metric is a nonprice. The proposed square-present characterization of allfivepartyprices by CAT0 inequalities needs another operation beyond singleton pendants.

## Invariant contraction gate (2026-11-24 21:50 UTC)

PG-IN-GATE: the Izeki-Nayatani invariant delta(X)<=delta0<1 gives D(n)^2<=4(1-2^-n)^2/(1-delta0) D(1)^2. A uniform bound for SOME complete CAT0 realization of every finite price suffices for contraction; a bad larger ambient realization does not refute this existence hypothesis. All source normalizations checked, independent algebraic re-proof by exponent_audit passed. PG-IN-BUILDING gives delta(X_n)>=1-4(1-2^-n)^2/n for our exact rank-building cones, tending to1.

Known trees/Hilbert/products have delta0, so products of trees contract withn4,s15/8 even while containing all Euclidean dimensions. Fujiwara-Toyoda2012 Theorem1.4 gives delta<=1/2 for every complete CAT0 cube complex, even dimension unbounded. Thus all such spaces contract withn8,s255sqrt2/128. This strengthens the abstract geometric compatibility of flatness and contraction but gives no actual-field example. No valid spectral product or arbitrary CAT0 gluing closure has been found.

R2 failed route: Bugar-Vrana2025 operator geometric means interpolate crossing bipartitions for LOCC upper functionals. Their exact flat-marginal/graph values are only established for alpha>=1/2. Tensor restriction spectral points correspond to alpha0 (fixed positive alpha retains probability/scalar sensitivity). No exact alpha0 graph formula or saturation of a complete-wire product follows; individual wires alone are insufficient.

R5 closure audit: duplicating a party and adding singleton pendants creates finite subsets of planes with attached trees if planar flatness is assumed. It does not establish Euclidean products or gluing two planes along a line. A8 random extension preserves old distances and bounds new distances by averaged old positions; arbitrary CAT0 spaces have analogous barycentric extension inequalities, so this alone cannot supply the missing product operation.

## Five-point non-L1 gate and low-dimensional border obstruction (2026-11-24 22:00 UTC)

PG-FIVE-NONL1: three leaves of a tripod at radius3/sqrt10 and two opposite line points at radius1/sqrt10 in T3xR give a CAT0 fivepoint metric with allcross1, withintriple6/sqrt10 andwithinpair2/sqrt10. Pentagonal L1 inequality fails: 2sqrt10>6. Since every finite Euclidean metric is L1 by averaging one-dimensional projections, adding pendants in ANY dimension cannot produce this metric. This is a geometric construction obstruction, not a price obstruction.

PG-GCT-PENT (root proposal, full proof written here): K3,2(q) does not border-restrict to K3(q) times a qwire on the two right parties forq2or3 overC. A homogeneous SL_(q^2)^3 invariant f nonzero at matrix multiplication exists by polystability. Its evaluation on alpha Kronecker beta is separately SL_q^3 invariant, so the polynomial coefficient matrix after right-party restriction has rank<=dimI_q(d). LeftGL maps multiply by a determinant character; rank-minor equations persist to singular maps and borderlimits. Target coefficient matrix f(M_q)(u dot v)^d has fullrank binom(q+d-1,d). The q2 andq3 invariant rings give strict dimension deficiencies. Exact restriction was already excluded for anyq>1 by the saturated left flattenings and combined left/right rank; the new invariant statement handles borderlimits atq2or3.

Scope: powers replace q byq^N and GHZ overhead changesformat; currentproof does not address these. No spectral price separation follows. General gate: find some nonvanishing degree-d M_q invariant with dimI_q(d)<binom(q+d-1,d). Mere polystability supplies no such bound forq>=4.

## 2026-11-24T22:07:28.899184+00:00 — all-dimensional capacity obstruction

PG-CAP-PRODUCT and PG-CAP-PENT now written in price_geometry.tex. Over C, K3,2(q) cannot border-restrict to triangle(q) times right EPR(q) for any q>=2, hence for any equal tensor power without extra resource. This strengthens the earlier q2/q3 polynomial invariant proof. Root and exponent_audit independently re-proved the capacity factorization and fixed-invariant no-continuity bypass. Primary Kempf–Ness references are Böhm–Lafuente2020 Theorem1.1p2 / Lemma5.1p9 (arxivv3) and Bürgisser etal2018 Theorem3.2p13 / AppendixApp37–38 (fullpreprint). Copies and hashes logged outside deliverable.

Essential limitation: subexponential GHZ overhead or o(N) extra source copies create rectangular left maps and destroy determinant covariance; no asymptotic rate gap or non-L1 price follows. No capacity continuity theorem is asserted or needed. Corrected Bugár first initial from G. to D. in ledger.

2026-11-24T22:11:48.291739+00:00 PG-CAP-HYPER added: allr>=3 andq>=2, K_{r,r-1}(q) cannot border-restrict to K_r(q) times K_{r-1}(q), including all equal powers. Independent derivations by root and exponent_audit. Completegraph lefttarget is balanced/critical; two selected rightvertices and fixed otheredge labels recover2x2capacity contradiction. All cutrank tests permit conversion. Overhead limitation unchanged.

## 2026-11-24T22:47:15.440415+00:00 — explicit crossing-operator regularization gate

PG-OP-GATE now in tex. Equal Kubo–Ando mean of crossing cuts12|34 and14|23 yields order-alpha BV upperFalpha. Define explicit p0(T)=limsup_alpha0Falpha(T), which is a restriction upper functional by K^(2alpha) norm-scaling disappearance. Its semiring power regularization r(T)=inf_Np0(T^N)^(1/N) is upper and power-multiplicative. For Cq=EPR13(q)*EPR24(q), q<=p0(Cq)<=q^2; saturation and CAT0 give2<=r(C2)<=2^sqrt2, and r(C2)>2 would give non-tree price hence square. Strict lower inequality remains open.

Important failed shortcut: BV Schur-copy n-limit is NOT semiring power regularization. Exact n4q2 common crossing projector P211 has EPR-pairing projection norm squared18, proving p0(C2)>=2^(3/2), above conditional price limit2^sqrt2. This actually proves a strict second-regularization drop conditional on CAT0. Program pg_crossing_operator.py saves exact rational Gram/projector/vector certificate and exploratory n3/4/5 means. Independent verifier pg_verify_crossing_certificate.py reconstructs only the certified16-vector Gram and projectors using elementary character chi211=sgn(pi)(fix(pi)-1), independently of MN/orbit enumeration. No price or all-power lower bound follows from fixed S4.

Still pursuing amplification: the candidate standard S_n irrep times a rectangular q-row irrep suggests common crossing blocks of entropy log(q)+O(1/q), with vanishing gain; this generalization has not been promoted to a proved statement; no uniform exponent gap. Tensoring fixed S4 witnesses does not preserve the grouped Schur actions. Root and exponent informed; independent gate/certificate review pending.

2026-11-24T22:49:53.135328+00:00 Independent checks passed: root full-coordinate reconstruction65536 entries and exponent rational/representation review. PG-OP-GATE fully independently re-proved by both. Added verifier locators to tex; corrected swapping explanation to Hom(sign,31 tensor31)=0, with explicit31 tensor31 decomposition. Numerical output is kept separate from exact certificate.

2026-11-24T22:52:59.883252+00:00 AEP route checked against Bugár arxiv2509.22152v1: Definition3.1 introduces fidelity smoothing before n-limit; Cor4.7 evaluates singleton spectral functionals, Remark4.8 extends entropy sums only in LOCC_q. This does not evaluate the unsmoothed alpha0 crossing operator regularization PG-OP-GATE. Source downloaded/hash logged; no theorem from it used in paper.

## 2026-11-24T23:02:12.352709+00:00 — uniform raw endpoint bound, with vanishing regularized gain

PG-OP-RAW-ALLQ is now proved: p0(C_q) >= q 2^(1/q) for every q>=2. The common crossing Schur block uses local types standard (2q-1,1) and rectangle (2^q), and common cut type (2^(q-1),1,1). The general rectangle branching proof, the no-exterior-multiplicity calculation from two-box Pieri, and the nonzero EPR-pairing projection are written in the TeX. Exponent independently checked all steps. The source is Sam's author-hosted Spring2017 notes, downloaded and hashed; exact theorem/page locators are in the source ledger.

This is explicitly only a raw p0 bound. At q=2^N its Nth root is 2*2^(1/(N 2^N)), tending to2. It therefore does not prove r(C2)>2 and does not select the square. Earlier fixed-block amplification remains invalid.

Two-party anchor investigation: a literal universal nonsingleton-cut center in WZ12.23 is impossible under the checked CAT(0) theorem: combining two crossing cut spectra gives the forbidden L1 square. Any segment-amalgamation theorem must impose overlap compatibility and cannot follow by declaring a two-party flattening an unconditional anchor. No such compatible gluing theorem has yet been proved.

## 2026-11-24T23:24:36.537946+00:00 — universal cycle-cover gap and crossing-exponent dichotomy

New conditional results PG-CYCLE-NORMALIZATION, PG-CYCLE-GAP and PG-CROSSING-EXPONENT-GAP are written in price_geometry.tex. The universal upper functional u(T) is the infimum of total weights 2^(sum binary cycle-edge exponents/2) over covers by four-cycle wire products. Its power regularization U attains the maximum enlarged spectrum value with all side logs<=1/2. Assuming the checked CAT(0)/square chain, U(C2)=2 when no square and2^sqrt2 when square. The initially tempting upward spectral rescaling was invalid; this was caught before writing and repaired by the known C4 asymptotic subrank4, which forces the unit-square external scale c<=2. Only psi^(c/2), a power<=1, is used.

The all-field C4 proof audit is explicit: integer vectors (1,0), (1,1), (0,1), (1,-1); at most 9q^2 possible global values; fiber size at least q^2/9; and a coefficient-1 monomial degeneration. Fix q: its Nth-power leading coefficient is a sum of O_q(N^3) source restrictions by grouped polynomial coefficient extraction. Then let N grow, and only afterward let q=2^m grow. No exponentially growing interpolation overhead is discarded.

Grouping any cycle cover by the smaller of its two crossing flattenings gives chi(q)<=u(Cq). Fixing equal coordinates at parties 1,3 yields a q-by-q identity matrix, proving chi>=q/2. Thus no square forces chi(q)=q^(1+o(1)), while a square plus RT-SOS and RT-SOS-UPPER forces chi(q)=q^(sqrt(2)+o(1)). This is an all-fields exponent dichotomy conditional on the checked source chains, and transfers to complex SoS length via the factor-four comparison. It does not select either branch, imply all-dimensional flatness from a plane, or apply to SoS length in characteristic two. Root independently checked the argument; exponent_audit subsequently re-proved all final prose, including the coefficient extraction, dual maximum, rank grouping, lower bound and arbitrary-q padding.

The limited Schur amplification search is exhausted: for n<=16 and q<=5, all Specht pairs satisfying <V^2, exterior^2 W>=0 produced 32 positive entropy-gain pairs, all standard-times-rectangle or the reversed pair. Searching rectangles through n=20 and q<=6 added none. Character values were independently cross-checked on all 3,582 entries up to n=10. These are diagnostics, not a proof that other common-projector constructions fail.

The segment-amalgamation route remains open. Universal nonsingleton anchors are impossible by crossing-cut roundness. Embedding tensors on party subsets by trivial legs fails ordinary direct-sum preservation, so the usual subsemiring extension theorem does not directly glue them. A.7 preserves one old price, not two pieces simultaneously. Convex-segment gluing, if proved, would make our five-point non-L1 three-page book a price whenever the square is a price.

## 2026-11-24T23:36:21.851873+00:00 — finite certificates, direct conversion, and prime specialization

PG-CYCLE-FINITE makes the universal gap a finite algebraic search: square absence is equivalent to one dyadic cycle cover of C_q with cost below q^sqrt(2). The cost set N_0+sqrt(2)N_0 is locally finite, so u(T) is a minimum. Fixed width and budget permit finitely many source formats and finite local-map polynomial systems. No bound on the needed width is given.

PG-CYCLE-AMPLIFICATION gives a direct conversion from such a cover to a strict planar shortening without the CAT(0) theorem. Group N-fold words into profiles; implement each profile using a multinomial GHZ selector and its summed cycle widths. Cycle subrank4 supplies the selector at asymptotic geometric cost 2sqrt(2) per selector bit. The multinomial inequality bounds the profile cost by 2sqrt(2)Nlog Z plus an arbitrarily small linear error; the remaining profile count has only logarithmic selector cost. The added cycle widths are explicit. Shortening independently re-proved the constants, order of limits and all-field validity.

PG-CYCLE-SPECIALIZATION: no complex square is equivalent to existence of bounded-width finite cycle certificates at infinitely many primes, and equivalently at all sufficiently large primes. A fixed number-field certificate has residue degrees bounded by d. Descent expands the first three grouped local maps and applies an F-linear coefficient functional to the fourth, adding at most d^3 restrictions per term. One fixed tensor power makes d^3 Z^N<q^(N sqrt(2)), uniformly in the prime. The converse uses finitely many formats and the Nullstellensatz. This does not decide characteristic two or claim unchanged-width descent. Exponent independently checked the descent and quantifiers.

## 2026-11-24T23:58:01.176437+00:00 — rank-one residual obstruction excludes the q=16 cycle gate

PG-CROSSCUT-RESIDUAL proves that subtracting a tensor separated across one crossing cut leaves rank at least q(q-1)/2 across the other cut. In matrix form, the kernel of I-(X maps to M X^T N) has dimension at most q(q+1)/2. Rank normalization of M reduces the equation to A=A^T B; after triangularizing B, lower entries are determined by upper entries. This works in every characteristic. Root independently re-proved it.

PG-CYCLE-DYADIC-LOWER combines that residual lemma with dyadic capacities. If a resource has clipped capacities (q^2,1), its cost is at least q and the residual cut/slice inequalities give at least 5q(q-1)/(2(q+1)) more. Without either extreme resource, the capacity ratio is at most q^2/2, which gives an even stronger elementary sum bound. Therefore u(Cq)>=q+5q(q-1)/(2(q+1)) for dyadic q>=4. At q16 this is872/17>51, whereas16^sqrt(2)<51. All dyadic certificate widths m<=4 are now excluded; m5/q32 remains open. The floating MILP was only a diagnostic and is not used in this proof.

## q32 finite-cycle exclusion (2026-11-25T00:08:07.873939+00:00)

The rank-one crosscut residual lemma strengthens to rank at most two over every field; root independently checked simultaneous left/right triangularization and the fixed-space projection. The full proof is now PG-CROSSCUT-RESIDUAL.

PG-CYCLE-Q32 proves u_F(C_32)>=135>32^sqrt2. Six high-ratio capacity types reduce the proof to205 exact rational profiles; all except one have cost lowerbound>135. The sole exception has one(512,1) and one(1,512); a dyadic excess calculation forces remainingcost>=90, hence total>=90+32sqrt2>135. Root independently checked this exceptional argument; the exact205-row table was sent for separate review. The numerical MILP was exploratory only and is not used as the certificate.

The first dyadic width not yet excluded for the strict finite-cycle gate is now m=6 (q=64), pending complete independent table review. This is a finite certificate-width exclusion, not a decision of square existence or the asymptotic gate.

## 2026-11-25T00:21:25.598125+00:00 — q64 rank-relaxation boundary

Root independently verified all205 rational q32 profiles using rt_verify_cycle_q32.py, a different recursive algorithm; full q32 theorem now passes independently.

PG-CROSSCUT-RESOURCE refines rank-one removal by the actual opposite edge dimensions, independently checked by root. Atq64,R2048,smallcut1, the residual rank isatleast3568 ratherthan2016. Nevertheless the refined relaxation admits the exact five-profile (4096,4),(4,4096),(32,32),(16,16),(8,8), cost312<threshold358.364, bothcutcapacitysums4156 andminsum64. No localmaps are known. This stops the current rank<=2 exclusion technique atq64.

Further sources checked narrowly: Cohen andYu2013, All unitaries having operator Schmidt rank2 are controlled unitaries, DOI10.1103/PhysRevA.87.022329, onlyapplies to unitaries; cannotassumeitforarbitrarySLOCCmaps. Bravyi etal2024, GeneratingkEPRpairs fromannpartyresourcestate, primary https://ir.cwi.nl/pub/34217/34217.pdf, introduction/Section2, usesclassicalroutingquantifiers anddoesnotgivea cheapC4 crossingcover. No theoremfromeitherisusedinpaper.

Pending new equality gate: if a decomposition has total cheaper-crossing ranks exactlyq, variable opposite-coordinate slices give a square linear factorization of(x dotz)I_q. Its doubled block matrix realizes q hyperbolic Clifford creation/annihilation pairs on dimension2q, forcing2^q|2q, impossibleq>=3 inanycharacteristic. This would strengthenminsumtoatleastq+1, butaloneleaves inexpensiveq64 profiles. Independent reviewrequested.

## 2026-11-25T00:24:43.023120+00:00 — strict slice bound and correctedq64 profile

PG-SLICE-CLIFFORD is provedandwritten overeveryfield: thetotal ofthecheaper crossingranks inanydecomposition ofCq isatleastq+1 forq>=3. Exponent_audit independently passed the CAR/idempotent proof, includingcharacteristic2. The earliercost312 profile withminsum64istherefore refuted. PG-CYCLE-Q64-PROFILEnowaddsa(1,1)resource: cost313,minsum65,bothcutsums4157. Itsoneunitremoval leaves4156>=4095; thusallcurrentlyprovednecessaryconstraints stillallowit. No actualcover isclaimed.

ForrectangularL(qxr),R(rxq) withr>q, LR=fI doesnotimplyRL=fI. TheCliffordproofdoesnotextendbyassertingasquarecompletion; no lowerboundbeyondq+1wasproved. PrimarysearchesofquadraticmatrixfactorizationandHopf-Stiefeltheory foundno immediatelyapplicable strongerstatement.

## 2026-11-25T00:33:14.118470+00:00 — defect-one rectangular completion

PG-RECTANGULAR-FACTOR proves ρ_F(q)>=q+2 forq>=4 overallfields; rootandexponentindependentlypassed. Withinnerwidthq+1, K=RL-fIhasrankonequadraticentries, so UFDfactorizationgivesuvT withdegrees0+2,1+1,or2+0. Constantfactorremovesonecoordinate; linearfactorscompleteasquare(q+1)-dimensionalmatrixfactorization, excludedbytheClifforddimensioncount. Generalhigher-rankKcannotbeassumedtofactorlinearly.

The same sectionrecords χ<=ρ<=2χ allfields andσ/2<=ρ<=2σ overC. Thus rectangularsuperlinearboundwouldresolveasimilarsuperlinearSoSbound; classicalsquarematrixfactorizationtheoremsdonotbypassthisopenproblem.

The q64profileisagainupdatedtoincludetheprovedbound: replaceunit(1,1)by(2,2),givingcost314,minsum66,cutsums4158. Onlyrank<=2removalisthe(2,2)term,leaving4156>=2016. Thisstilldoesnotgiveactualmapsoracover. Earliercost312/min64andcost313/min65profilesarenowbothrefutedbyprovedstrictslicebounds.

## 2026-11-25T00:41:39.827346+00:00 — audited fresh primary crossing lower bounds

Singh2026, primaryrepo Arth-Singh/crossing-lower-bounds, givesP>=4q/3(q>=3),15q/11(q>=5),67q/49(q>=7). Full4/3Remark9proofindependentlypassesownandexponentaudit; party3<->4identifiesitsPexactlywithminimumtotalcheaper-crossingranks. OurindependentprogramvalidatesEVERYcertificateinequalityandweighted sum,includingall5040permutationsforeachof71L7orbitrepresentatives. Both189-rowL5and77-rowL7certificatescancelallauxiliaryvariablesexactly. ThusaninitialAppendixAwordingsignconcernhasnoeffectandisnotreportedastheoremerror. NoLeankernelrun; sourceP4=7andn+3claimswithonlyfullLeanproofarenotused. SourcePDFandunmodifiedchecker/dataremainoutsidework;savedownnormalizedmathematicalcertificatedataandownverifierfordeliverable.

Theq64profilemustnowmeetminsum88. Fourtypes(4096,4),(4,4096),(64,64),(16,16)meetallcurrentnecessaryconstraintsatcost336<threshold358.364. Noactualmapsareknown. Newlinearboundssupersedetotalrankq+1/q+2boundsnumericallybutdo notselecttheasymptoticexponent. Theindependentrectangularfactorizationproofsretaintheirseparatescope.

## 2026-11-25T00:49:40.981334+00:00 — unbalanced crossing inequalities and q64 profile correction

Root derived, and I independently checked, r+3s>=2q and r+t^2s>=tq for 1<=t<=q, together with the transposed bounds. For all cover partitions these become the linear inequalities sum min(R,t^2 S)>=tq, and their transposes. The old cost336 profile fails already r+3s: r84,s4 gives96<128. The q64 numerical model with all t constraints is now infeasible, but an exact rational high-ratio branch certificate is being constructed before claiming an exclusion. Strong Singh certificate bounds now have independent root and exponent_audit semantic/arithmetic rerun passes; no Lean claim.

## 2026-11-25T00:53:31.464063+00:00 — exact q64 exclusion certificate

PG-CYCLE-Q64 is now written with a Fraction-only certificate: u_F(C64)>=359>64^sqrt2 over every field. Enumerate six high-ratio types (ratio>1024), with540 multiplicity vectors under rational cost359 using sqrt2>140/99. A single13-entry rational dual handles all127 remaining capacity types. Conditional high-resource rank<=2/removal bounds strengthen the cut totals. All540 branch bounds exceed359, with minimum422523176/1089165>387. programs/pg_cycle_q64_simple_certificate.py and outputs/pg_cycle_q64_simple_exact.json contain the complete exact proof, without numerical solver dependence. Independent root and exponent audits are underway. First unexcluded finite cycle width is now m7/q128 after those checks.

## 2026-11-25T00:56:04.994389+00:00 — q64 independent re-proof complete

Root independently reconstructed all133 capacity types,127 low and6 high, all540 branches by a different recursive algorithm, every removal subset, each13-row bound, and the single dual. The exact minimum and threshold comparison match. PG-CYCLE-Q64 therefore passes independent re-proof; first unexcluded finite cycle dimensionq128. Root verifier and output locators are included in the manuscript.

## 2026-11-25T00:57:52.246282+00:00 — q128 necessary-profile boundary

A thirteen-type profile survives all currently proved necessary capacity constraints at q128. Exactcost712+128sqrt2<900<128^sqrt2, bothcutcapacitysums17408, minsum176. Integer checker tests all128 unbalanced t inequalities plus(1,3), and every applicable rank<=2/refined-rank1removal. This is not a cover: no local maps constructed. Thus finitecapacityinfeasibilitydoesnot immediatelyextend theq64 theorem toq128.

## 2026-11-25T01:09:57.695161+00:00 — all-field sign-normalized border identity

Replacing every nonzero entry in Singh's q4 border(3,3) table by its sign gives an integral identity with leading scalar1, verified independently by exponent_audit. It works in characteristic2 as well; originalexcludedprimesareanormalizationartifact. Explicit12 polynomialcolumns and fullerrors E4,E5 are written. Actual cycle covers obtained by coefficient extraction have A_N=2^(N-2)(9N²+3N+4) terms, withdyadicallypadded sourcecost<=2(4sqrt3)^N; totalupperbase8sqrt3 remainsabovethreshold4^sqrt2. No tensorpoweramplificationclaim.

## 2026-11-25T01:54:16.020218+00:00 — urgent rectangular and stabilizer audits

PG-SINGH-RECTANGULAR is written with a full adaptation proof and arbitrary-decomposition/interchangeable orientation statement. Every audited certificate row separates the ambientdimensionp from the numberq of slice labels; no square assumption is used. Bounds are max(p beta(q),q beta(p)), roundedup.

Root's RT-STABILIZER-SELECTOR independently passes: local Pauli postselection restricts oldcommutationforms and adds a commonradical, so weightedrank cannotincrease. EPRformula and GHZrank<=2d give b>=Nr²/6 for balancedparitylabels. This excludes smallselector methods only when the full coherent implementation is stabilizer; arbitrary sums of stabilizer localmaps may require nonstabilizer controls.

## 2026-11-25T01:56:15.273803+00:00 — concrete r3 full-space Cauchy lifting diagnostic

The scalar Cauchy determinant identity gives r! matching-deleted graph terms only after local symmetric projection; lifting that projectedtensor alone is blocked by balancedflattening rank2^(2floor(r²/4))/r^r. Forr3, I retained all64 local symmetric/antisymmetric sectors, using I±SWAP on eachtwo-leg vertex. Exactsectorlinearalgebra gives69 nonzero terms from six matching-deletedK3,3 graphs. Full4096-coordinate check gives64H3=sum c_j*(tensorlocalprojectors)J_sigma, with coefficients±1,±2. Thus overeveryfieldofcharacteristic!=2 it is an actual69-term cover of the fulltensor, not merely the symmetricsector. It is not yet independently re-proved and gives no generalr/asymptotic bound. Rank3 symmetric projectors are not Pauli projections, so this is outside the stabilizer barrier. Program pg_cauchy_r3_sectors.py, outputs pg_cauchy_r3_sectors.json and pg_cauchy_r3_full_cover.json preserve the exact data.

Primary operator-valued sources inspected: Jing,Liu,Zhang General Capelli-type identities, arXiv2307.14573v2 (2024), published RepresentationTheory29(2025),695-717, Theorem2.1 andRemark2.3: fullgroup-algebra/Youngmatrixcoeff identities, but for Cauchy-Binet products with specific commutators, not directly the reciprocal Cauchy determinant. No valid assignment lifting the full densegraph identity has been found. OriginalPDFhash1427fda0aad96bbc7f0798dc873b2196fb3054319c959ec6e7d36ff001de80a0. Khare-Sahi2023 bosonic/fermionic immanant source found; onlyabstract read sofar.

## 2026-11-25T02:13:18.529613+00:00 — integral eighteen-term full-space identity and class rigidity

The previous69-term odd-characteristic diagnostic is superseded for this purpose by an integral18-term identity with coefficients±1. It is a full4096-coordinate identity overZ, hence every field, includingF2. Each term uses K3,3 minus one perfect matching; five binary GHZ copies suffice to coordinate all18 terms. Input pg_cauchy_r3_integral_cover.json and standalone pg_verify_cauchy_r3_integral.py are preserved. Root independently reconstructed all boundary coefficients and the six-class signed minor, PASS.

PG-CAUCHY-CLASS now proves a general-r limitation for local port-permutation lifts: symmetric quotient coordinates with left weights0,...,r−1 and right weights sigma^-1(j) force a unique staircase edge-bit matrix. The r! matching classes give a signed unit diagonal minor. Every class aggregate coefficient is(-1)^(r(r−1)/2)sgn(sigma), so no matching class can be omitted in this ansatz over any field. This is a coefficient/projection obstruction, not a cut obstruction and not a theorem for arbitrary local maps. General-r independent audit requested.

Unused matching wires provide at most one selector bit per party per tensor copy. A literal balanced18-letter profile selector needs log2(18) bits per copy, leaving external rate at least log2(18)−1. This does not exclude nonliteral algebraic profile compression. The main unresolved target is still a multiplicity-preserving general-r identity with subquadratic selector exponent, or a cheaper actual finite-cycle cover.

## 2026-11-25T02:25:32.461466+00:00 — dense regrouping, routing comparison, and precise immanant boundary

The18-term crown identity groups into13 terms by products of I,SWAP,I−SWAP,SWAP−I at separate parties. Each still uses six binary source wires; four binary selectorbits suffice. Exact expansion checker/input/output saved. This is an all-field algebraic regrouping, with independent audit requested. Separately, slicing one edge in each triangle and routing the other four along eight distinctK3,3edges yields a q²-term fullsourcecover (four atq2), with more wirecost per term. Both are finite diagnostics; neither reachesSH33.

EX31 already forbids any subquadratic general-r extension made solely of partial/permutation maps: log2A>=r(r−1)/2. Thus local dense group-algebra operators, not just a more clever port-permutation list, are needed.

Khare–Sahi2023 primary was read beyond abstract. Theorem2.2 Eq2.6(p6) is in the symmetricSegre quotient Eq2.5(p5), and fermionicTheorem3.1 Eq3.2(p13) uses nilpotent variables u_i²=v_j²=0 and onlysquarefreepowers. Neither theorem restores discarded local Schur multiplicity spaces. SourcePDF/text remainoutsidework; hash e829d86f81ed9c8eae69bef17527eab700df465cdf8acc1237f84346d7328462. The Yang–Baxter/F-matrix route has only been screened atabstract/equationlevel and no valid tensorresource assignment is currently known.

## 2026-11-25T02:31:06.301414+00:00 — one dense term per matching fails; arbitrary-LU rank extension refuted

PG-CAUCHY-COMMUTANT is written and exactly certified. It rulesout one product of local span{I,SWAP} maps per matching in the r3 Cauchylift overeveryfield. A division-free retained-partyquotient replaces characteristic-zero Schur projectors: all six972-coordinate identities hold integrally, and six explicit difference-vector minors are±1. Thus all localmaps normalize toI, afterwhichcoordinate95fails0vs1. No claim for multipletermsperclass or arbitrarylocalmaps. Root independent audit requested.

Independently verified root's27-qubit arbitrary-LUcounterexample using only the explicit input and weight matrices, a different nullspacebasis and plain-listGF2 arithmetic. PrimaryJi–Chen–Wei–Ying pp9–10Eqs18–21 matches all inputdata. All64 phase identitiesmod8 pass. Source/target weightedranks are36,37. Hence the stabilizer commutation-rank monotone cannot extend to arbitrarylocalunitaries. Three weights arezero; all are rankatmostone. No LC-inequivalence theorem is needed. Independent checker/output preserved.

## 2026-11-25T02:37:38.567915+00:00 — independent checks completed before checkpoint09

Exponent_audit independently re-proved PG-CAUCHY-CLASS, reran a different full r3commutant certificate using internaledge enumeration and permutationdeterminants, expanded the13-term dense grouping, and checked thefour-term/eight-wire routing comparison. AllPASS.

PG-CAUCHY-LIFT-NOGO is a new fullyanalytic general-r strengthening, independently re-proved byexponent_audit beforefreeze: one term permatching is impossible for everyr>=3 whenever each localmap descends to a scalar on the symmetricquotient. Retainoneparty, usearbitrarypairedtotalorders for all otherweights, and isolate a matching plus anychosenlocalbasisvector byFerrersmargins. Thus normalizedmaps mustall beI. The bareidentityreducesr->r−1 byhighestvertexall1/neighborports0 contractions andfailsatr3. This includes all dense localpermutation-algebra maps, but leavesmultipletermspermatching andarbitrarylocalmaps outside the quotient-preservingclass open.

## 2026-11-25T02:55:49.434814+00:00 — multiplicity-free operator route has a uniform ceiling

PG-OP-MULTIPLICITYFREE is written and independently checked byexponent_audit againstBessenrodt–Bowman2017 Theorem1.1 pp1–2. Every constituent of an entire multiplicity-free product of two<=q-rowSpecht types has<=4qrows, handling independentconjugations casebycase. Its crossingentropy is therefore<=log2q+2, so atq2^N all suchcertificate rootceilings tend2. This rulesout an entire extension class of the priorstd×rectangle construction, not the fulloperatorfunctional or multiplicity-bearingblocks. Nextmethod: positive commutant operators fixedby partialtranspose, with high-Schursupport; a sufficient finiteblocktest, pendingindependent algebraic check.

## 2026-11-25T03:10:58.251355+00:00 — positive partial transpose and exact finite cone limits

PG-OP-PT is written and independently re-proved by both root and exponent_audit. A nonzero PSD commutant operator X fixed by partial transpose and supported on high crossing types has positive trace, hence nonzero EPR overlap. Central X reduces to x>=0, Dx=0 with D the exact Gram matrix of P_nu−Gamma(P_nu). Character formula and p(n)n! simultaneous-conjugacy reduction are checked. This is sufficient only.

PG-OP-PT-FINITE now has six exact rational lower/upper certificates. Jacobi–Trudi character reconstruction independently matches the discovery program's MN table; integer Farkas duals rule out all strictly higher-entropy central supports, with exact entropy order from products of integer parts. The multiplicity-bearing n9/n10 cases have optimum at or below log2q: balanced333 pair exactly log2 3,333/432 atH54,3322/3322 atH541,3331/3322 atH55. No inference to noncentral or indefinite vectors, other Schur blocks, or a full p0 upper bound. A separate independent group-count reconstruction has been requested.

Structural necessity: both local row counts must grow at least q^epsilon to reach q^(1+epsilon), since every constituent has at most their product many rows. Fixed-small-row extensions have only q^(1+o(1)) ceilings. Positive partial transpose alone has not yielded a general entropy upper bound; ordinary PPT entropy inequalities point in the wrong direction. Next work must address genuinely growing-row, multiplicity-bearing operators or a direct semiring-regularization upper bound.

## 2026-11-25T03:20:25.766947+00:00 — full commutant/SoS duality identifies the operator gate

New PG-OP-SOS-DUALITY and PG-OP-COMPLETE written, independently analytically re-proved by root and exponent_audit. If no high-cut Γ-fixed symmetric commutant vector has nonzero trace, orthogonal duality gives low-supported Y with Y+ΓY=2I. Product-vector evaluation gives a complex bilinear sum-of-squares identity of length rankY. This exact finite duality removes both centrality and positivity restrictions.

For fixedq, choose a maximum-dimension <=q-row Specht module M_n>=q^n/poly_q(n). Regrouped Schur-Weyl shows g_(lambda,lambda,nu)<=dimS_nu(C^(q²)), polynomial in n, with at mostq²rows. Thus low-cut rank<=poly_q(n)2^(nh). Under a square price, RT-SOS lower bound σ_C(M)>=M^(sqrt2-o(1)) excludes low Y for every h<sqrt2log2q, producing a common high vector anew for every fixed grouped dimension. Therefore p0(Cq)>=q^sqrt2 for allq and r(C2)=2^sqrt2; without square r(C2)=2. The operator gate now equals the universalcycle gate. This does not select the value, and is complex-only. CVZ2018 primary Eq11p17 and Remark3.7Eqs12-13p19 checked for dimension estimates.

Signed central finite scope: n9 balanced333 pair has exact nonzero-trace signed witness atH4311=1.752715, greater than its positive optimumlog2 3. Program pg_verify_op_pt_signed.py and *_signed_verified.json give exact primal and row-span upper duals. This finite gain is weaker than oldstd×rectangleq3 and does not itself move the main gate.

## 2026-11-25T03:23:19.556470+00:00 — deterministic rational matrix gate

PG-OP-DETERMINISTIC now fixesq=2^N, the leastpower-of-two n satisfying an explicit integer inequality, and lexicographicallyfirst maximum-dimension <=q-rowSpecht lambda. Rational Gram-adjusted partialtranspose, commutation, highsupport andtrace1 are a prescribed rational linear system. Squarepresence forces every suchsystem consistent by finiteRT-SOS; squareabsence givesr=2 andtherefore someq withp0(Cq)<q^(5/4), forcing thatprescribed system inconsistent. Thus absence is equivalent to failure atsomeN in this fixedfamily. No arbitrarynetwork/formats or unknownn search remains inside a givenN, thoughdimensions are verylarge. Root independently approved the construction and rationalGramformulation; finaltext audit pending.

Final independent exponent_audit review at 2026-11-25T03:24:33.804052+00:00: PG-OP-SOS-DUALITY, PG-OP-COMPLETE and PG-OP-DETERMINISTIC all PASS as written. The exact source dimensions, finite integer threshold, Gram-adjusted rational equations and both branch implications were independently checked. No actual deterministic matrix instance has been solved.

## 2026-11-25T03:35:07.241447+00:00 — compressed full-space gate and Capelli construction

PG-OP-COMPRESSED is written. It uses Sym^n((Q^q)^tensor4), dimension binom(n+q^4-1,q^4-1), with both low crossing projectors annihilatingv and EPRoverlap1. Root, exponent_audit and shortening independently checked the direct dual: failure gives C_q^n=S+U, each selected cutrank<=poly_q(n)2^(nh), so RT-SOS forbids failure under square at the prescribedsize. This gives an alternate direct proof of PG-OP-COMPLETE without maxSpecht/SOS factorization. Failure yields a rational two-cut decomposition byGaussian elimination. No instance solved; this is an encoding of the existinggate.

PG-OP-CAPELLI is written with a proposed exact polynomial-in-n fixed-q construction. PrimaryItoh2012 §4.1 Eq4.1 pp13–14 supplies centrality. Highest-weight determinant evaluation and a fullywritten falling-factorial characteristic identity show that the d=q² Capelli eigenvalues distinguish allpartitions. Differentialoperators Eij=Σa x_ia∂_ja and interpolation give rationalprojectors onoccupationbasis withoutn! enumeration. Averagedorbit Gram isα!/n!, differentfromorbitSUM Gram n!/α!. Complexity ispolynomial in numericn forfixedq, with hugeq-dependentdegree, notuniformin q orpolylogn. Independent final auditrequested.

## 2026-11-25T03:45:21.808204+00:00 — explicit determinant witnesses and rectangle family

PG-OP-RECTANGLE replaces maxdimension selection by a fixed rectangle(n/q)^q in a separate valid deterministicfamily; hook formula gives the sameq^n/(n+1)^A bound. The sizeinequality forcesn>2q², so2q² dividesprescribedpower-of-two n. Root/exponent analyticchecks pass.

PG-OP-DETERMINANT constructs full symmetricpolynomials (det_b det_c)^a withnonzeroEPRoverlap and exact minimum crossingentropy h=log2(2q²)−(q²+1)/(2q²)log2(q²+1), asymptoticlogq+1. Determinanttwistingforcesallrows>=a, and rank1-b substitution shows theextremeone-row residualcomponent actually occurs. Exactinteger entropy tests and prescribeddivisibilities prove explicit compressed andRECTANGULAR solutionsatq2,4,8, witha256,256,1024. These do NOT assert feasibilityofoldmaxdimensionSpechtinstances. Firstremainingcompressed/rectangleparameterq16; determinantansatzfailsits thresholdbutthesystemremainsunresolved. Program/outputpg_determinant_gate_verification preserve exactarithmetics. No uniformregularizedgainfromthisfamily.

## 2026-11-25T03:54:13.957823+00:00 — decorated determinant witnesses solve first six instances

PG-OP-SLICE-DETERMINANT is written. W=product_i det(X_i,b,i,d) is degreeq² andnonzeroatCq. F=D_b^21 D_c^21 W^22 hasdegree64q² andcommoncrossingsupport dominatedbyeta=(21(q²+1)+22q,(21+22q)^(q−1),21^(q²−q)). Exactinteger entropycomparisonpassesq2,4,8,16,32,64; atq64 marginabout.0059004bits. Program/outputpg_decorated_determinants_verification saved, nohugepolynomial expansion. Prescribedn(q)divisible64q², so appropriatepowers areexplicitfeasibilitycertificates.

Rectangleprojectionnonzero is independently approved byroot/exponent: equivariantrestrictiontoA⊗B yieldsdetA^42q timesdiagonalmonomial productAii^22q timesdetB^64q. Afterdeterminanttwist, projectiontorectanglehasnonzeroFischerpairingwithdetA^22q. Physicalprojectorscommutecutprojectors, preservinghighsupport. Thusfirstsixcompressed ANDrectangularinstances solved; oldmaxdimensionfamilyisnotasserted. Firstremainingdyadicparameterq128. Theetaentropyboundtherefallsbelowthreshold, butdoesnotprovefailureofpolynomialorsystem. Asymptoticrawgainstillconstantc<3, nosemiringbranchselected.

## 2026-11-25T04:04:07.173747+00:00 — independent decorated checks and top-type boundary

Both independent entropy verifiers are now cited in the manuscript: the EX reconstruction uses exact integer comparisons after independent partition construction, and root uses rational logarithm bounds. Added the primary Fischer pairing locator (Möllers 2013, printed p.811) and a direct highest-weight dominance proof.

The open next step is whether the physical rectangle projection kills the extremal crossing type. The existing Fischer proof only proves nonzero total rectangle projection across all crossing types. It cannot be reused to prove that the top type of W survives. A proposed PSD/Cartan-product survival argument therefore still needs a separate nonvanishing theorem for that top rectangular component; no such theorem has been established.

## 2026-11-25T04:09:47.951304+00:00 — top-component parity diagnostic (awaiting independent check)

For U=A tensor B, let p_i=exterior_j(e_i tensor e_j). The top Cauchy component of W_q^ell has row Cartan vector product_i p_i^ell in S_((ell*q)^q)(U). Cartan multiplication is commutative; permutation matrices on A permute the p_i with no internal wedge reordering, so fix this vector. Its desired A determinant type is det^(ell*q). For q and ell both odd a transposition acts with sign minus on that type, forcing the projected top vector to vanish. This does not apply to dyadic q. It is a proposed exact illustration of why total Fischer nonvanishing cannot identify the top crossing type, not a new main-gate implication. Independent audit requested from exponent_audit.

Literature check: local BI2017 Theorem5.9(2), printedpp24–25, expresses a degree-q² unit-tensor invariant evaluation through Latin-square signs. This establishes a related cancellation phenomenon, but no exact equivalence with the present top-Cartan coefficient has been proved. Broader search found Amanov--Yeliussizov (2023), arXiv2202.11059, and Li--Zhang--Xia (2025), arXiv2111.07343; neither has yet been read for a theorem usable here. Do not cite them as establishing the missing nonvanishing.

## 2026-11-25T04:27:41.532701+00:00 — uniform multi-cut construction reaches critical exponent

PG-MULTICUT-UPPER is written with a full proof. The rectangular B.2 estimate is logR(p,q)<=sqrt(log²p+log²q)+O(log(logp+logq+2)); uniform constants follow from the classical partition asymptotic. Binary merging of actual rank factorizations produces transversal cuts and exactly at most2^(d−1) canonical orientation patterns. Balanced-tree l2 error accounting gives P_F(n,d)<=2^(d−1)n^sqrt(d)(log(n+2))^(C sqrt(d)), in every field. Exponent_audit independently re-proved all three steps.

Rossman–Zhu2026 provides the literature comparison: PT-rank definition3.4/lemma3.5p113:8, characteristic2 identity candidatep113:4, and their characteristic-not2 upper viaSoS inProp6.2/Thm6.3p113:18. Our consequence uses the supplied checked crossing identity; it is not independent validation of the claimed complexity separation. The leading exponent exactly meets the two-hub threshold, with an explicit orientation count; no selector is free and no strict shortening is inferred.

The odd-q/odd-ell top-projection diagnostic is now independently passed and briefly included. The determinant-pencil model is a sharper description of the remaining coefficient: f(Y)=product_i det(Y_i)^ell, Reynolds in the slice-index factor. Positive rectangular Kronecker multiplicity alone does not prove this vector nonzero. No new main branch has been selected.


## 2026-11-25T04:41:32.384378+00:00 — source audit complete; five-point and radial-embedding boundaries

PG-MULTICUT-UPPER has now passed independent full proof and primary-source checks by both root and exponent_audit. Rossman–Zhu's PT-rank is exactly the sum-over-transversal-cut invariant, and the new uniform bound excludes their particular characteristic-two identity candidate in the stated growing-d regime. Root added the Rossman–Zhu and Hardy–Ramanujan bibliography entries. This remains a consequence of the checked supplied B.2 identity, with critical leading exponent and no new price.

The five-point continuation still lacks a price-preserving segment amalgamation. Anthropic A.7 uses one old spectral point and retractions fixing every old party; it does not amalgamate two independently prescribed prices. Wigderson–Zuiddam Theorem12.23 supplies singleton-cut anchors, not arbitrary cuts or line gluing. The geometric CAT(0) gluing theorem alone therefore cannot certify the three-strip / tripod-times-line metric as a price. No claim of a complete five-party classification is made.

A narrow literature search did not locate a primary theorem proving that CAT(0) plus L1-embeddability (or negative type of the distance) forces a uniform Izeki–Nayatani bound. This is an unresolved route, not a claimed counterexample to such a theorem. The elementary radial-rescaling shortcut fails already on the positive real line: the Schoenberg embedding F(t)=1_[0,t] in L2 satisfies ||F(t)-F(s)||²=|t-s|. Rescaling to G(t)=sqrt(t)F(t) gives ||G(t)||=t, but for 0<s<t its squared pairwise distance is t²+s²-2s sqrt(st), strictly larger than (t-s)². Thus that construction supplies no norm-preserving 1-Lipschitz Hilbert map.

For the operator route, a dimension lower bound for a common high-cut intersection does not establish nonzero EPR overlap. Approximate concentration in both high-cut spaces does not imply an exact common vector; the small-angle obstruction remains precisely the root recoupling-gap gate. No additional determinant constant-factor example or unsupported dimension-counting claim has been promoted.


## 2026-11-25T04:45:28.577153+00:00 — conditional sharpness links the transversal bound to Q1

PG-MULTICUT-FLAT is written immediately after PG-MULTICUT-UPPER. If fixed dimension d has no strict shortening, then the identity PT-rank exponent is exactly sqrt(d). For a hypothetical unbounded exponent-improved sequence, group by the at most2^(d−1) transversal cuts and restrict to the nearest lower dyadic wire dimension. Each term is a two-hub network with terminal widths m and bridge width r*m+O(1). Hubs at +/-tau*s/sqrt(d) have normalized cost 2d sqrt(1+tau²−2tau/sqrt(d))+2r tau, whose derivative at zero is2(r−sqrt(d)). A fixed improvement beats the constant selector toll. Root independently re-proved the full argument before inclusion. This is conditional sharpness, not a converse, a selected branch, or an improved actual cover.
