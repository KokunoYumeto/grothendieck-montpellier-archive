# Shortening research notes

Agent: /root/shortening, GPT-6 Astra Pro, effort not exposed by runtime.
Date: 2026-11-24 (UTC); root retains authoritative run start.

## Checked source definitions

- OpenAI attached source, §2, lines 203–211: finite sum identity, cost includes
  runs to terminals, local computation free, strict inequality
  `w + 2D log2 A < 2Dm`.
- Same source, lines 223–231: multiplicity-profile compression, selector
  words sent to terminals, internal copies do not need selector.
- Anthropic, Definition A.1, p. 19: enlarged cover-subadditive,
  multiplicative spectral points, not merely normalized additive spectrum.
- Anthropic, Lemma A.2, p. 19; Definition A.4, p. 20; Theorem A.6,
  pp. 20–21. The duality used is on all tensors on the fixed party set.

## Results written in shortening.tex

- SH-01: one network cannot shorten diameters; field-independent affine
  hyperplane integration proof.
- SH-02: rigorous fixed-vertex profile compression, all characteristics.
- SH-03: homogeneous selector inequality valid for every price, including
  pointwise limits of arbitrarily rescaled spectral metrics.
- SH-04: strict shortening implies a finite Euclidean nonprice and excludes
  flatness. This removes the apparent scaling obstruction in prompt Fact 5.
  Contraction follows conditionally on the attached alternative theorem.
- SH-05: no shortening and attached duality imply a price bounded above by
  Euclidean distance on any finite ball configuration, saturating all
  coordinate diameters. Quantitative duality construction written fully.
- SH-06: compactness yields such a price on the whole unit ball.

## Open gates

- SH-07 now supplies CAT(0) rigidity by root's independent inductive
  roundness-two / flat-square proof. It yields an isometric ball of radius
  2^{-(D-1)/2}.
- SH-08 proves strict shortening iff failure of flatness, conditional on
  the attached duality A.6 and price embedding C.3. SH-09 reduces Q1c to
  mutual exclusion of flatness and contraction, using alternative D.2.
- No explicit strict shortening, nor a no-shortening theorem over C or F2,
  has been obtained by this agent.
- Source crossing identity gives a critical quadratic tradeoff; its
  symmetric profile has bridge exponent sqrt(2), exactly the Euclidean
  first-order threshold for four orthogonal terminals. Merely citing it
  gives no strict shortening. Additional layouts or a strict improvement
  of that tradeoff would be necessary for this route.

## Further lemma under investigation

Every nontrivial enlarged spectral point on a party set appears to be a
power `psi^alpha` of a normalized additive Strassen spectral point, with
`alpha = g_phi(I)`. A direct-sum multiplicity expansion gives the exact
power mean law. This would alternatively prove SH-03 through the terminal
unit-tensor exponent and Lemma A.2. Do not mark this checked until the
proof is fully written and independently verified.


## CND graph gate and a direct-restriction obstruction (21:25 UTC onward)

SH-17 reduces inclusion of every price in CND distance kernels exactly to subexponential covers H_r^N by copies of G_r^N for every r, with G_r=K_{r,r} and H_r=two disjoint K_r graphs. Repeated labels handle arbitrary rational zero-sum coefficient vectors. The Mat3(F2) character witness already tests r=256. No such cover has been found.

SH-18 gives exact routing capacity r/[2(r−1)] and explicit coefficient-0/1 restriction H_r^r <= G_r^{2(r−1)}. Thus r=2 is rate-one attainable after two copies; routing is strictly insufficient for r>=3.

SH-19 proves H_3(q) is not a restriction of G_3(q), for any q>1 and any field. Group matching L_i,R_i, contract their q-state diagonal wire, and obtain invertible q4-dimensional maps between two M_{q²} tensors. Matrix-multiplication fixed-party isotropy forces edgewise factorization. Local operator Schmidt ranks are at most q, but each of the three crossed-to-parallel edge pairings forces the product of endpoint operator Schmidt ranks to be at least q². Multiplying gives q6<=q3, contradiction. This does not exclude sums of restrictions or asymptotically negligible source overhead. Primary theorem: Burichenko 2016, author reprint arXiv:2210.16565v1, Proposition5 p5, proof §8 pp12–13, arbitrary field. Root independent review requested.

The initial Clifford–Pauli route has an additional elementary capacity bound matching routing: source K_{r,r} edge width N has global L:R stabilizer entropy r²N. A full-rank local stabilizer map to output width (r−1)M discards rN−(r−1)M stabilizer degrees at each of 2r vertices. Each local Pauli postselection lowers that entropy by at most1. Hence M/N<=r/[2(r−1)]. This excludes rate one for r>=3 within exact stabilizer restrictions, but is not used as an obstruction to covers. Fattal et al. 2004 Theorem1 p3 and Eq.(6) p2 provide the canonical form/entropy background. This note is exploratory until incorporated with a fully specified class of maps.

## Eight-point CND witness (after checkpoint02)

SH20 improves the 512-point obstruction to the span of A=E11, B=E22 and C=[[0,0,1],[0,0,1],[1,1,0]]. Its ranks are [0,1,1,2,2,3,3,2]. The parity character has signed rank counts [1,−2,−1,2], giving λ+=2sqrt3−sqrt2−2>0, hence four positive and four negative labels suffice. Every proper subset is strictly CND: translation lets it omit zero, the six other nonconstant Fourier eigenvalues are <−1, λ+<1/6, and Fourier coefficients sum to zero, so Cauchy gives negativity. This proves absence of 5/6/7-point witnesses within these eight points, including unequal real coefficients; it is not a global minimality statement. Both exploratory search and canonical exact certificate have programs/input/output.

Border extension of SH19 remains open. A local orbit section near the grouped matrix-multiplication target gives F(t)=g(t)h(t), g(t)→I and h(t) in the matrix-multiplication isotropy group. The gauge h(t) can diverge and mix the physical L:R factors, so physical operator-Schmidt rank cannot be passed through that decomposition by rank closedness. Molnar et al. (2018), arXiv1804.04964v1, Theorem2 p13 and Theorem4 pp16–17 concern exact equality of injective/normal PEPS and do not assert fixed-graph image closedness or uniformly bounded gauges.

## Effective r4 consequence and exact all-r obstruction

SH21 extends the exact SH19 obstruction to all r>=3 by reducing each edge of the grouped K_r automorphism to rectangular matrix-multiplication isotropy. Product operator-Schmidt ranks force q^{r(r−1)}<=q^r. The robust/asymptotic gap remains.

SH22a records the real linear equality-system version of Anthropic D2 Steps4–7 in full; positivity is unnecessary for its rank-one kernel. SH22b makes the r4 graph-cover gate imply an explicit contraction constant at matrix size3: D3²<=(3−2^-523336)D1². Normalized near-equality implies every squared quadrilateral residual is small; Reshetnyak controls opposite-side discrepancies. A square integer subsystem on130816 variables has inverse row norm<2^(2N) by cofactor/Hadamard bounds, yielding uniform approximation to the rank metric. The eight-point positive witness survives errors1/256. Root independently checked this constant chain. This is a conditional theorem: existence of the needed subexponential covers of H4^N by G4^N is still undecided.

## Global small-width exclusions (21:51 UTC onward)

SH23 proves no strict shortening at widths1,2,3 in any dimension and over any field. A sign cut separates one terminal of every diameter from the other. Weighted maxflow paths have length at least sqrt2, giving cost>=sqrt2*integer_mincut; summing projections over all sign directions gives cost>=2*average_mincut. For width3, selector and individual bounds leave only two terms. Each sign-cut target rank then forces both term ranks to saturate the individual cap, while the averaged cut bound contradicts cost<4D. This uses arbitrary network layouts and is not restricted to hubs. Primary Ford-Fulkerson1956 Theorem1 p400 was visually inspected.

SH24 proves no planar width4 shortening. Parent derived the exact Crofton weights sqrt2-1 on each singleton terminal cut and2-sqrt2 on each adjacent cut. For two terms of cost<12, integer capacities and target rank256 force opposite low flattening ranks8, high ranks>=248, and every local rank16. Crofton gives at least4+6sqrt2>12. The remaining term count A3 is ruled out for all D by the individual mincut bound and integer capacities. Thus the smallest width still undecided is m4,A2,D>=3.

The q2 complex grouped K33 border search used eight random complex initializations, analytic gradients verified to error<4e-12, and2500 L-BFGS iterations per restart. Best squared normalized overlap was approximately0.25, with no exact/border identity. It is only exploratory local optimization; parameter scaling can cause weak gradient stopping criteria. Full input, program, results and best parameters are preserved.

## Width four is globally excluded (22:04 UTC onward)

SH25 establishes sign-cut ceiling profiles kappa=ceil(log2 rank), bounded by integer mincuts and 8-Lipschitz on axis flips at width4. Mixed cuts at folded Hamming distance h obey rS(s)+rU(t)>=16^(D-h), by fixing mismatched diameter endpoints. Frame costs below6D force a low cut kappaS<=2D-1. This directly excludes D3,D4,D5 with weighted profile sums36>35,97>95,240>239.

SH26a proves a general dimension bound for A terms: (log2A)^2(D-1)^2 < (A-1)m²D/2. Complement-even sign-cut profiles have variance<=m²D/2 by the degree>=2 Walsh Poincare inequality. Their means are strictly belowD(m-log2A); Cantelli plus the covering of sign cuts by at least one large term proves the bound. At m4,A2 it excludes D>=10.

For D6..9, coordinate-permutation averages reduce the necessary threshold profile inequalities to192,224,320,360 real variables. Exact rational Farkas certificates prove infeasibility; common denominators4410,11926,26846,127447. The generator uses scipy only to propose weights; saved Fraction verification checks nonnegativity and exact zero-variable/-1-constant sums. Parent separately wrote rt_verify_rank_profile_certificates.py, reconstructing every row from labels and validating layer-pair existence without importing our generator or invoking a solver. All four independently passed. SH26c consequently proves no strict shortening at ANY widthm<=4, in any dimension and over every field. This remains a bounded-width result; no claim on m>=5.

## Width-five parameter reduction

SH27 excludes all term counts A>=3 at width5. Continuous/rank-flow bounds leave A3 dimensions3..5 and A4 dimension2; integer sign-cut budgets and folded-cube geometry exclude them. For A3, high-capacity occurrences required acrossallcuts exceed those permitted perterm; the folded4-cube isK44 and folded5-cube is5-regular triangle-free. Planar A2 also fails: its Crofton cost exceeds (42+27sqrt2)/5>16. A2 inD3 fails by budget47 and10-Lipschitz rank ceilings. General Cantelli excludesD>=15. Thus residual width5 parameters are exactly A2,D4..14 within current bounds. No existence is claimed.

Full integer profile optimization reports infeasible m5A2D4,D5,D6, but these are exploratory solver results until an exact proof/certificate is extracted. D7 reached a time limit without a profile. Radial continuous dual-certificate searches at m5,D2..8 found no certificate; those outcomes concern the dual feasibility problem, not a tensor identity.

## Width-five further exclusions after checkpoint03

SH28a excludes D4 by a short matching argument on K44. For absolute minimum10/11, excess above per-cut baseline20+t is only14/6. Cross-edges between the two full-rank sets have a matching4 (or3 with one exceptional both19 cut); mixed slicing forces each matching edge to spend at least14-t, impossible. Cases t<=9 follow directly from low-cut envelopes.

SH28b excludes D5,D7,D9 using complete integer minimum branches, with63 selected exact rational Farkas certificates in sh_width5_single_minimum_coverage.json. Parent independent verifier passed all selected files. Certificates use optional global-minimum constraints on both terms, justified by selecting the absolute minimum before relabeling and translating. Some numerical proposals required exact box-row correction after rational rounding; every final certificate cancels exactly and givesRHS-1.

A two-minimum extension averages over S_h times S_(D-h). The D6 residual minimum15 splits into13 admissible choices of the other minimum and its distance; all13 have exact certificates. Independent orbit-level verification is requested before treating this as a completed paper theorem. Larger residual cases are running.

## Seven-party hypermetric gate

SH29 deletes one negative parity point from the eight-point rank-metric witness. The inherited4plus/3minus vector has sum1 and Q=6lambda>6/25. The same stability threshold2^-523336 survives because42/256<6/25. Thus one seven-party subexponential cover K43^N ->(K4+K3)^N would imply explicit contraction. This is a hypermetric, not zero-sum CND, inequality and does not conflict with SH20 proper-subset CND. Root and exponent agent independently checked.

At equal resource powers, exact K_{r,r-1}(q) ->K_r(q)+K_{r-1}(q) is impossible over every field: left local maps are square and invertible; the product of right full-row-rank maps preserves a global left:right rank q^{(r-1)(r-2)}>1, against targetrank1. Price geometry agent's capacity theorem strengthens this to complex border non-restriction. Neither rules out subexponential covers.

## Global width-five exclusion complete

SH28c records the full two-minimum orbit proof and all439 admissible case certificates. Dimensions6,8,10,11,12,13,14 require13,21,30,54,83,76,162 cases respectively; every case passed exact rational verification and an independently written full-cube orbit checker. Parent final rt_verify_width5_coverage.py rechecked273 selected radial certificates plus439 two-minimum certificates, all285 possible first-minimum branches forD5..14, SHA256 identities, and every pruned integer rank inequality.

SH28d now states the unconditional all-field/all-dimension theorem: strict shortening requires m>=6. This uses arbitrary networks, not a hub class. The unbounded-width question remains open. The next check is whether the m6 planar rank/Crofton relaxation is feasible; if it is, further finite-width optimization requires a new invariant rather than more of the same inequalities.

## Width-six rank relaxation is feasible

SH30 gives an exact abstract planar two-term profile at width6: singleton ranks64, adjacent ranks(32,4064)/(4064,32), other balanced rank128. All target/slice rank sums, sign-profile budgets and Lipschitz bounds pass. Even replacing every Crofton log rank by its integer ceiling gives10+7sqrt2≈19.8994949<199/10<20. Hence the current rank/Crofton inequalities cannot prove the next width exclusion alone. No tensor with these simultaneous ranks, tensor identity, or network is constructed. Further work now targets the seven-party subexponential cover gate rather than extending the same finite LP calculations.


## Exact pentagon cover and first compression obstruction (after checkpoint04)

SH31 gives a fully explicit integer identity covering H_q=K3(q) times K2(q) by1+binom(q,2) restrictions ofG_q=K32(q). Its core is delta_xy delta_uv = delta_xv delta_yu + sum_(a<b) J_ab[x,u]J_ab[y,v]. Atq2 this is a minimum two-term exact cover over every field, with all local maps in{-1,0,1}. Both full tensors atq2/q3 were checked coefficientwise; programs/input/output and map tables are preserved. Tensoring the binary identity gives A=q=2^N, so log2A=N; this does not supply the subexponential pentagon or seven-party gate.

SH32 refutes a tempting exact same-graph type compression: W=S tensor U+U tensor S is not a restriction ofK32(4). All singleton ranks are full(16,16,16,4,4), but global left:right rank is10 in odd characteristic and6 in characteristic2, versus forced16 for any such restriction. The core has unit singleton minors. The global matrix is an injective multiple of R tensor I+I tensor R, R=vv^T-I,v=(1,0,0,1). The exact coefficient/rank certificate covers all65536 entries with448nonzeros. This does not contradict SH02, which introduces selector wires and permits extra resources, nor does it obstruct more general asymptotic or border covers.

The numerical search that led toSH31 is retained separately; the proof no longer depends on its floating-point fidelity. Root is pursuing an integer-network strengthening of the width6 planar obstruction through Hirai's locking theorem; the continuous capacity profile itself is attained by a half-integer terminal graph.


## Positive-overhead amplification gates

SH33 weakens the sufficient contraction gate substantially. A single finite K43(q)->K4(q)+K3(q) cover with log_q A<=1/128 already implies the same explicit Mat3 contraction; an unbounded sequence with that positive exponent also suffices. This uses normalized scale s bounded by a six-edge spanning tree of near-rank distances, s<13/2, and lambda>49/1000. The exact residual margin is227/16000.

More promisingly, duplicate each of the eight rank-metric witness points t times. The balanced graph defect grows as t², while zero distances among duplicate labels leave the spanning-tree scale bound s<15/2 unchanged. Any one cover K_(r,r)(q)->Kr(q)+Kr(q), r=4t, with log_q A<=r²/2048 implies contraction. Thus a family log_q A=o(r²), even at fixed q2, is sufficient. Factorial matching sums A=2^{O(r log r)} would meet this gate if an exact identity can be constructed. No such identity has been proved yet.


## Numerical searches after the exact binary identity

The q3 pentagon factorized evaluator tried A2 (three starts,1000 iterations) andA3 (four starts,3000 iterations), best fidelities.4182498769 and.6274025508. The seven-party q2 K43->K4+K3 two-term search used two750-iteration starts, best fidelity.1171874099. All gradient checks passed to<5e-12, all runs hit iteration limits, and no identity was found. These are failed local searches, not nonexistence proofs. All programs, exact inputs, JSONL traces, summaryJSON and bestNPZ tables are saved.

Root independently re-proved SH31's integer identity, SH32's global ranks10/6, and all ofSH33's positive-overhead/replication argument. The normalization and duplicate-party operations were explicitly checked. The next substantive construction target is a balanced binary graph cover with log2 term count o(r²), for example a factorial matching expansion. No such expansion has been justified; naive Gaussian/Clifford restrictions cannot by themselves remove the quadratic global bipartite entanglement while discarding only2r qubits.


## Integer width-six geometry and a failed packing route

SH34a gives an explicit integer graph: direct AD=BC3, AC=BD2, plus a unit binary tree with cherries AD/BC. At h=(1-1/sqrt3)/2 and internal points(h,-h),(-h,h), all singleton mincuts are6, adjacent cuts12/5, other balanced8, and exact cost8+7sqrt2+sqrt6>20. Zero gradients of a convex length objective certify this fixed topology's minimum. It is not a tensor identity and not a universal lower bound.

SH34b carefully verifies all source/sink cuts: terminaldegrees6, singleton cuts6 and ABcut12 give an integral12-flow fromABtoCD. Terminal balance forces AC=BD=z,AD=BC=6-z. Every ADcut5 has zero net divergence, hence even used capacity at most4 and at leastone unused unit; z<=2. Ifz2, all four diagonalpaths cross once and the others never cross. This parity observation alone does not extract a spanning residual.

SH35 refutes the same-graph residual-packing conjecture. Use paddingAD=BC3, a private unit AD/BC binarytree, and a separate private unitK4 with capacity2 terminalspokes. Terminaldegree6 and cutprofile(singletons6,AB12,AD5,AC12) hold exactly. A proposed packing of3AD,3BC,2AC,2BD paths plus a connected fourterminal remainder saturates everyterminal, forcing everypath and remainder tree into one terminalbridge. If remainder is binarytree, K4 must route2AC+2BD, impossible since eachprivate degree3 cannot support endpointload2 plus transit. If remainder isK4, binarytree must routebothAC andBD through its unit middleedge. Thus no packing. Exactcut/cost enumeration and independent MILP infeasibility are saved in sh_residual_packing_counterexample.*; the proof is combinatorial.

This is not a sub20 network: placeprivateK4 vertices atcenter, and its cost is8+7sqrt2+sqrt6. Moreover arbitrarypositions ofprivateK4 allow a cost-nonincreasing replacement by capacity2 star: some privatecenter has2*sumdistance<=sumK4edges by averaging, then triangle inequality accounts for spokes. It preserves the gadget cutfunction and permits2AC+2BD. Therefore a cost-reducing replacement theorem remains possible even though same-graph packing is false.

Exploratory search scope: integer network alternation over2/4/6 internal vertices,3 starts each,18 accepted iterations foundbest20.348984679394846. The critical abstract packing search generated151 feasiblegraphs with<=5 internalvertices and checked explicitpackings for each. SH35 uses6 internalvertices. All programs,inputs,outputs preserved; these searches imply no global nonexistence.


## Planar critical networks and fractional residual flows

SH36a adds exact parity: floor(lambdaAD/2)+floor(lambdaAC/2)>=m for terminaldegrees m, singletoncutsm, ABcut2m. Thus at m6,L5 the other balancedcut is at least8. Geometric planarization is cost-nonincreasing and only increases mincuts; terminalleaf attachment restores singleton6/AB12. A sub20 graph must retainADcut5. In a disk-planar graph with cyclic terminals, every alternating ACcut has value12: one side lacks a connection between its two terminals by planar separation, and its two terminalcomponents each haveboundary>=6. Root independently checked. Realcapacitiesstillattain19.89949 withAD=BC3.5 pluscap2.5centralstar, so integerwidth remainsessential.

SH36b records the weaker sufficient gate: fractional demands3AD+3BC+2AC+2BD plus a whole connected residual cost at least8+7sqrt2+sqrt6. Only existence of the residual remains open. For a chosen unit treeT, necessaryandsufficient residual cutconstraints are deltaT(U)<=c(deltaU)-d(delta terminalsubset) for EVERY graphcut, by four-terminal fractional flowcut sufficiency (Schrijver1991 Cor2p37, K4conditionp32). Terminalminimumslacks are1,2,1,6 for singletons,AB,AD,AC in the cofacialcase. No theorem currently guarantees a suitable tree.

The SH35 graph admits this weaker fractional packing exactly: reservebinarytree; usepadding; privateK4routesoppositepairswithdirectedgesandhalfcycles. Further22 generatedcriticalgraphs with6/7 internalverticespassed exact rationalpackchecks. Thus the weakerroute survives currentexamples; finite testsare notproof. A possibleplanarproof cuts along anADmincut of5unitports and aims for median-port tripods on both sides. All necessary linkagecuts still need verification.


## Decisive critical integer-gap proof: SH37

The residual-packing conjecture is no longer needed. Double integer capacities and apply Hirai's locking theorem to the four singletons and two adjacent cuts, a3crossfreefamily. Divideby2. Terminaldegree6,singles6,H12,L5 force half-integral commodity valuesAD=BC7/2,AC=BD5/2. For netflows f_i, use terminaldirection calibrationu1=u2=(-1,-1)/sqrt2,u3=(-1,0),u4=(0,-1). Totalcalibration10+7sqrt2. On each edge alpha=2fmod2 and integercapacity force excess at leastceil(|alpha|/2)-.5sumalpha_i|u_i·t|, after removing integerparts of|f_i|. Everyalpha except0,1100 has gapgamma=1-sqrt(2+sqrt2)/2.

QuotientF2^4/<1100> hasindependentterminalchargesX atA,C andY atB,D. Each connected supportcomponent haszerocharge, soAcomponentmustcontainC. Supportlength>=2, including anyzero-length edges. Hence universalintegernetworkcost>=10+7sqrt2+2gamma=12+7sqrt2-sqrt(2+sqrt2)>20; lastcomparisonuses160²-2*113²=62. This is field-independent and does not require graphplanarity. Exactall16angular/sign/parity certificate sh_parity_calibration.* saved. Root independentlychecked fullproof; priceagent separatelychecked geometry/parityportion. Applyingtoallm6D2A2networkprofiles awaits parent's final parameter audit.


## General odd-cut gap and planar width seven

SH37 now has a general statement: terminaldegree/singletons b, highcut2b, oddlowcutL imply cost>=2sqrt2*b+(2-sqrt2)*L+2-sqrt(2+sqrt2). The paritycharges are unchanged because2b-L andL are odd. AtL=2b-7, this exceeds the A2shorteningbudget4b-4 by the constant0.051735871589....

SH38 proves all-field planar strictshortening requireswidth>=7, and two-summandplanarstrictshortening requireswidth>=8. ForA2, attachwidthmoutputleaves, forceoppositehighceil2m byrankandframe, henceactualhighcut2m andalllocalsm. ContinuouscostallowsL<=2m-7; parityremovesboundary, leavingL<=2m-8. Atm6 mixedslicefails; atm7 strictPGslice129>128fails. ForA3m6, exactbudget<53/3 givesH12=>L1,H11=>L3. Somehigh12mustexist bytwo-cutranktotal8192; rank<=2crosscutresidualbound2016forcesanoppositehigh12; then thirdtermhasbothranks>=2014, ceilings11+11 andcost>=22, contradiction. Parentindependentlycheckedall withthe53/3fix. Theglobalfirstwidth remains6 inD>=3; planarfirstwidth7, withA2excludedthere.

Disk-planar numericalpackingsearch found34 feasiblegraphsundergeometricobjectives withallpackings verified, bestcost20.48051495. Adversarialrandomobjectivesfounda14-vertexcandidate(noactualcostbelow20) whose fractional-flow/integral-residualMILP isreported infeasible. Noexactinfeasibility certificateyet, so this is only exploratory. ItdoesnotaffectSH37, whichbypassespacking.

## SH39/40: rectangular folds and width-six D3 exclusion

SH39 proves all-field rectangular crossing inequalities and their strict Clifford threshold. SH40 uses the four-cut tight-frame budget to exclude m=6,D=3,A=2 for arbitrary networks. Root independently audited the full proof, including the geometric sum bound, on 2026-11-25 before checkpoint07. Stable labels: lem:rectangular-fold-constraints; thm:width-six-dimension-three. Numerical profile searches are distinguished from exact exclusions: unbranched radial dual status2 means no certificate found, while the human SH40 proof is complete.

## SH41: width-six dimension-four exclusion

The complete all-field proof excludes m6,D4,A2 using rectangular folds and the folded four-cube K4,4. It treats all minimum ceilings0..15 analytically. Root independently checked the proof, including the colored matching cases and bounded-incidence edge selection for the5+3 partition. Stable label: thm:width-six-dimension-four. The fifteen exact radial certificates are supplementary; the result does not depend on numerical infeasibility.

## SH42: independently certified dimensions five and six

Theorem thm:width-six-dimensions-five-six excludes m6,A2,D5/D6 over every field and arbitrary layouts. D5 uses18 radial and17 two-minimum exact Farkas certificates; D6 uses17 radial and121 two-minimum certificates. Root independently reconstructed all rows and folded-cube geometry and verified complete branch coverage; outputs rt_unbalanced_D5_verification.json and rt_unbalanced_D6_verification.json record PASS. No solver infeasibility status is a premise.

## SH43: dimension-seven exclusion independently verified

The m6,A2,D7 exclusion has21 radial plus76 two-minimum exact certificates, with260 directly checked integer prunes. Root separately reconstructed every row, every new rectangular prune, and full minima0..27 coverage; inputs/outputs rt_unbalanced_D7_verification.json record PASS. The remaining width-six two-summand dimensions are8..19. D8 currently has57 completed certificates from an interrupted batch, not complete coverage.

## SH46: width-six three-summand dimension-three exclusion

Complete all-field proof:2970 minimal high-rank-pattern branches,2967 exact integer propagation contradictions, and a direct arithmetic contradiction for the three t6/7/8 double-full survivors. Root independently reconstructed the branch coverage, all4364 semantic deductions, and the survivor proof. Theorem label thm:width-six-dimension-three-three-summands. Programs/inputs/outputs and independent verification are cited in shortening.tex. The earlier AND LP/MILP searches are exploratory only. Remaining width-six A3 dimensions are4..16.

## SH47: dimensions eight and nine independently excluded

Complete exact certificate coverage excludes m6,A2,D8/D9 over every field and arbitrary layouts. Root separately reconstructed all row semantics, including Singh bounds, and every branch/prune. Theorem label thm:width-six-dimensions-eight-nine. Remaining width-six gates are A2,D10..19 and A3,D4..16.


## SH49/50: operational LU route and exact limitations

The27 binary weight matrices of the36-to37 stabilizer-rank witness all have rank<=1. Their rank-difference metric is exactly l1: nonzero ab^T maps to(e_a,e_b)/2, zero maps to0. The actual data give30 half-cut metrics and351 exact pair checks. Thus these weights cannot witness any one-term graph-resource advantage, even through arbitrary local preparation/distillation; the weighted stabilizer-rank increase remains a valid failure of that proposed monotone outside graph tensors.

Any grouping making both LU states graph tensors without loss also gives identical edge multiplicities, since cut entropies recover2b_ij=E_i+E_j-E_ij. Actual advantage must therefore use an irreversible preparation/distillation step. The systematic CSS graph-state model is explicit: pivots1,2,3,4,8,16;70 bipartite core-leaf edges; target adds11 core edges. This is a graph-state description, not an EPR graph tensor. Program/input/output sh_lu_operational_reduction.* preserves exact data. Parent requests operational conversion or rigorous route obstruction, not merely non-l1 replacement weights.


## SH51: standard LU preparation blocked for every metric

An exact414-path rational certificate routes uniform demand2/27 between all351 pairs in the70-edge preparation graph. The generator found numerical optimum1/13 but the proof uses only the explicit positive fractions and exact edge loads<=1. A separate checker reconstructs the graph from all64 original support words, verifies all paths and demands/capacities, and imports no discovery or optimization code.

For any grouping gamma and pseudometric d, define pi_i=(1/27)sum_v d(i,gamma(v)). Then d(i,j)<=pi_i+pi_j andsum_i n_i pi_i<=(cost of preparation). Any A-term cover of an EPR graph by restrictions of N-copy27-qubit states has singleton widths b_i<=N n_i+log2A. Hence outputcost<=N preparationcost+log2A sum_i pi_i. This blocks every one-term or subexponential-cover metric advantage from the standard70-edge template, including arbitrary grouping and arbitrary maps after the LU. Alternate cheaper preparations or sums of layouts remain open.

The bounded LC/pivot check found66-edge preparation throughLC(15),LC(1),LC(15), but it also admits an exact410-path2/27 all-pairs routing. SH51 therefore blocks that preparation too. Search scope90000 singleLC moves+96000 pivots is preserved; minimum66 is an observed count, not a lower bound. The LU operational route is now paused in favor of full-multiplicity dense Cauchy covers.


## SH52: central spin projectors already fail at r4

On each three-port local space, retain the two multiplicity covectors e1-e2,e2-e4 at weight1 and their bit-complements at weight2. Use weights1,1,2,2 on each clique. All covectors annihilateSym3, so any local scalar combination of the spin3/2 and spin1/2 projectors acts as a scalar after projection. The24 projected crown tensors span rank22 overQ; target raises rankto23. An explicit20-coordinate integer functional annihilates all24 and takesvalue16 on target. A separate no-linear-algebra boundary verifier confirms every value. Therefore any number of central-projector-only terms fails overC (and char>3). This is a route limitation, not a main-gate reduction: noncentral action on the two-dimensional multiplicity spaces is necessary and remains untested globally. Mod2 the target lies in this projected span, so this witness gives no F2 obstruction.

SH52b repairs the characteristic-two test by retaining both spin weights at every party. A16-coordinate binary functional kills all24 full-mixed crowns and evaluates1 on target. An independent boundary-only checker confirms it. InF2 usecyclic projectorS=I+C+C², not divisionby6. BothC andF2 therefore require genuinely noncentral multiplicity action. Explicit local transposition matrices generate allMat2 overchar!=3, so the remaining issue is a small global cover, not availability of local operators.

A genuine noncentral full-all-mixed-sector construction attempt used48terms(two per crown class) with arbitrary real2x2 multiplicity maps, identically onboth spin weights. After161iterations/80seconds bestrelative squaredresidual=.01401756627140251; no identity or impossibility. Two gradientchecks passed<1.1e-11. Exactarrays,trace,bestNPZ and dependency/einsumdiagnostics are preserved. Other spinsectors were not fitted.


## Operational correction: legacy search stop

At03:35 UTC root observed continuing D10 output. Fresh exec ps calls inspect only their own sandbox namespace, so the earlier negative process inventory did not establish absence of old persistent sessions. Two old legacy drivers (D10 andD11) were identified from their fresh-child parent cmdlines and stopped at case boundaries, at03:35:59 and03:38:27 respectively. Each worker verified the exact driver and dimension-specific input before signaling its own parent; neither stopping child wrote a case result. Acknowledgements and the original generator are preserved. No mathematical row or certificate semantics changed. New bounded construction sessions record session IDs and explicit stop sentinels.


## SH53: dimension ten independently excluded

Root completed and independently verified the full m6,A2,D10 certificate family:26radialcertificates,405two-minimum certificates,1149prunes. First minima0..24and39 are radial; all marked branches for25..38 covered. Authoritative output rt_singh_D10_verification.json records exact semantic reconstruction, Fraction cancellation, hashes and full coverage. Theorem labelthm:width-six-dimension-ten. Remaining width-six gates A2,D11..19 andA3,D4..16.

## SH54: polynomial-cost total-spin projection

OverC the SU2 invariant projector on d binary ports is a positive sum of at mostbinom(d+3,3)+1 operatorsg^tensor d. Proof uses homogeneous monomials in four real quaternion coordinates and elementary finite convex elimination. Every summand is party-local. After gauging EPR edges to epsilon, H_r is fixed by left projection; d=r(r-1), so multiplying cover count byO(r6) preserves the SH33o(r2) gate. Forq=2^N, d=Nr(r-1), givingO(N3r6), zero additional log_q exponent atfixedr. This enlarges the construction ansatz but doesnotprovide the missing projected identity. EX independently checked the proof.

The explicit24-quaternion r4 effective-spin projector is verified exactly overQ(i), including local intertwiners and all24projectedcrowns. NoF2averaging claim. Numerical variable projection reached.0009475329570313699withoutspinprojection and6.245644609848444e-7withit, using48noncentralterms inallmixedsector. Neither iszero; coefficients grow, so neither identity norborderclaim. Full-coordinate checks andallmaps retained.


## SH55: second-moment geometry closes bulk ranges

For every network, kappa(s)=ceil log2 max(1,signcutrank) is bounded byhalf the summed absolute projected wire variation. MinkowskiL2 therefore givesE kappa²<=w²/4, strictly strongerthan onlyE kappa<=w/2. Evenness and12-Lipschitz signcube profiles givevariance<=18D atwidth6. Combiningthe momentbudget withCantelli andintegerthreshold6D-1 excludesA2,D>=17 andA3,D>=13. Rootindependentlycheckedthe fullproofincludingD13exactradicalbounds. RemainingA2D11..16,A3D4..12. The new exactlinear thresholdrow isquadratic_budget, coefficientorbitweight*(2k-1), RHS D²(m-1)²M-1. Oldcertificate modelandoutputs remainunchanged.


## SH55c andSH56: two-summand width-six gate reduced to one dimension

The coupled same-cut dichotomy givesZ1Z2<=1 forZ_j=6D-kappa_j. Covariancebounds implya1a2<=18D+1, while the two geometric momentbounds implya1+a2>9D/4 forD>=15 andeach a_j>D. Hencea1a2>5D²/4>18D+1. Rootindependentlycheckedthe complete analyticexclusion forD>=15.

Moment-row radialcertificates independently verifiedbyroot excludeD11,D12,D13with44,48,52fullminimumbranches. D11uses31old+13newcertificates;D12/13areentirelynewmodel. SH56citesrt_moment_D{D}_verification.json. Remainingm6gates:A2D14only;A3D4..12. D14radialmodelleaves43,44,45uncertified; nofeasibilityclaim. D15/16radialdiagnosticsarepreservedbutirrelevanttoanalyticproof. Allbatchwritersfinishedbeforecheckpoint11freeze.

## SH55d: every two-summand width-six case is excluded

The same-cut rank condition restricts the integer deficit pair to the two coordinate axes and (1,1). Along each sign-cube edge the combined squared change is at most145, except an opposite-axis transition with both endpoint totals at most12, when288 suffices. Thus joint even-cube Poincare gives VarSum <= D(145+143p)/8. The geometric moment bounds give mean total B>9D/4, so p<5D/[8(D-2)], while covariance forces VarSum>(5/2)D²-2. Clearing denominators gives160D³-2195D²+2192D+256>0 forD>=13, with value9317 at13. Root and exponent_audit independently checked every step. Together with the earlier verified finite cases, this excludes m6,A2 for all dimensions and all fields, with arbitrary layouts. The D14 numerical diagnostics are retained but unnecessary. Residual width-six range is A3,D4..12. No shortening identity or final contraction/flat classification is claimed.

## SH57: exponential moments exclude three terms in dimension twelve

An integer quadratic majorant bounds2^(k-N) by(k-a)^2/(N-a)^2+2^(-(N-a)) wheneverN-a>=32. AtD12, every rank-ceiling profile has variance<=216 and second moment<2809. For mean<=40, usea=floor(mean), giving normalized expected rank<217/1024+2^-32. For mean>=40, usea40 and intersect the variance and second-moment bounds; the centered moment is<337, yielding expected normalizedrank<337/1024+2^-32<1/3. Three such profiles contradict the pointwise rank-sum condition. Exponent_audit found the argument; shortening and root independently checked it. SH57 is analytic, all-field, and allows arbitrary layouts. Remaining width-six cases are A3,D4..11.

## SH58: complete dimension-four moment proof tree

Adding the exact second-moment row sum kappa²<=2496 to the existing D4 mixed-cut propagation closes all28 normalized roots (globalminimum0..13 and two basepatterns). The complete retained tree has7013nodes,1286splits,5727contradictions and127524integerdeductions. Root independently reconstructed every necessary inequality, update, branchpattern, omittedpattern, childbox and coverage condition without generator or optimizer imports. The exact certificate hash and full audit are in outputs/rt_three_term_moment_D4_verification.json. This is an all-field, arbitrary-layout exclusion ofm6,A3,D4; prior incomplete searches remain nonproof diagnostics.

## SH59: Harper isoperimetry closes dimensions eight through eleven

After fixing the last sign, even rank-ceiling profiles retain their distribution onQ_(D-1). One ofthree highsets {kappa>=6D-1} hasdensity>=1/3. The12-Lipschitz bound gives kappa²>=(max(0,6D-1-12distance))². Harper's initial-simplicial-segment theorem minimizes every closed neighborhood, hence gives an exact lower second moment. Primary statement: Raty2020, arXiv1806.11061v2p2 Theorem1 andfollowingparagraph. Exact positive gaps forD8..11 are12299/576,20223/256,450299/2304,2637959/9216. Root checked the source and independently recomputedBFS/directHamming distances andinitial-segmentneighborhoods; exponent_audit separately recomputedalllayers. Programs/inputs/outputs sh_harper_rank_moments, rt_harper_moment_bounds, ex_harper_layers_independent retained. A pasted progress-message layer list accidentally included dictionarykeys; authoritativeJSONandallnumericmargins werecorrect and the typo was promptly corrected before manuscriptwriting. Residual width-six cases now A3,D5,6,7 only.

## SH60 and SH60b: complete exclusion of every width at most six

The all-level tail-count model selects one profile whose average rank upper bound is at least one third of the target. Its integer tails q_k and threshold indicators y_(k,v) satisfy monotonicity, strict geometric first/second moments, a linear exponential-rank row, and all neighborhood implications. Ordinary Harper neighborhoods suffice forD6/D7; D5 uses the actual folded cube, whose growth was exhaustively computed on all65536vertex subsets and independently recomputed. Six D5 fixed-top-count cases, eleven D6 cases (including q36=q35=10), and twenty-two D7 cases have exact nonnegative rational Farkas contradictions. Exponent_audit independently reconstructed all39cases and every row, growth value, cancellation, RHS−1, hash and coverage condition without importing generators or solvers.

D6's two direct moment prunes are22752>22471 and22564>22471. The second hand-pasted value22634 was corrected in the explanatory input/output scope strings, preserving the coefficient list and old/new hashes in outputs/sh_D6_tail_metadata_correction.json; the authoritative coverage manifest was regenerated before the final independent audit. The theorem uses only the corrected exact values.

Combining these cases with SH55d, SH57–59, the earlier low-dimensional exclusions, and RT-W6-PARAM gives SH60b: over every field, all dimensions, all finite summand counts, and arbitrary finite layouts, strict shortening requires width at least seven. Planar two-summand shortening requires width at least eight. The unrestricted shortening question and the flat/contracting classification remain open. No width-seven search was launched before checkpoint12.

## Additional bounded diagnostics preserved this cycle

The folded-neighborhood integer probe sh_folded_cube_neighbourhood_probe produced exact example sets with closed-neighborhood sizes14(D5,K6),26(D6,K11),52(D7,K22). Numerical lower bounds/statuses are exploratory and are not used in SH60. The missing reproduction script for the earlier K4 mixed-sector coefficient diagnostic is now programs/sh_cauchy_clique_multiplicity_structure.py; it exactly checks256targetcoordinates,32spin coefficients, ranks4/3, and determinant−(2z−1)^3 against saved arrays. An initial endian-order comparison failure was corrected and documented without changing any source coefficient. This supplies reproducibility, not a new cover identity.
