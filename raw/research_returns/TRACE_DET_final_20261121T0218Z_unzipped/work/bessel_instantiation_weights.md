# DET-15 source instantiation and DET-17 prime weights

Run TRACE_DET_20261121. Date 21 November 2026 UTC. Agent /root/step1_history_route, GPT-6 Astra Pro; effort setting not exposed. Source paths in this note are relative to work/external_lean/lean/src. This is a source-interface and mathematical consequence audit, not a Lean build, a recursive certification of imports, or an audit of the stipulated RH/Dirichlet theorems.

## Result

The actual final period construction supplies the local data used in DET-15. It constructs quotient measures and local Bessel maps, proves their positive finite quotient norm, obtains the multiplicity-one and decay inputs, and then constructs the normalized IsEll functional. The actual projector theorem is invoked in that construction. Thus the retained DET-15 local hypotheses have a concrete instantiation route within the source's standing global setting. This statement retains the global standing setting and its ties; it does not claim that an arbitrary D7 or HidaSetting is inhabited without those inputs.

The weighting gate can be made more precise in two directions.

1. The direct unweighted, infinite 0/1, and nonzero constant formal-degree choices cannot yield a compact operator on the DET-15 orthogonal family. A nonzero positive compact operator commuting with the whole irreducible source representation is also impossible. These are proved obstructions to those particular choices, not a claim that the source forces them.
2. The source already uses the nonnegative summable coefficients Lambda(n)n^(-sigma), sigma>1. Combining those coefficients with the actual DET-15 projections gives a positive trace-class family with trace -zeta'(sigma)/zeta(sigma). This combination is newly constructed here; the inspected source exports do not themselves state the combination. At sigma=2 its determinant is provably different from G(w)=Xi(sqrt(w))/Xi(0), even after any fixed nonzero rescaling of w. Its zero count is O(sqrt(R log R)), whereas G has asymptotically sqrt(R)log(R)/(4pi) zeros in |w|<=R. This is DET-17.

The remaining arithmetic identity is therefore specific: a source-selected weighting, or a different specified source operator, must have the required Xi spectrum/determinant. Positivity, summability, an arithmetic trace, or the availability of an actual common period Hilbert space does not supply that identity.

## 1. Concrete instantiation of the DET-15 local data

### 1.1 The global construction really chooses the local measures and maps

The theorem GlobalTheory.Core.Deg.exists_termLoop_of_standingHypotheses in
Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsTermLoopOfStandingHypotheses.lean:59–119
starts with D, SizeData2, a HidaSetting X, Full X, FinX, the source SIso, a word u, Ties D, StandingHypotheses, ConcTie, and the displayed size thresholds. It does not assume GoodW and GoodS as additional free predicates. Its proof:

- installs the source DecLow and CoefWeightedLoc results at61–62;
- obtains GapHyp from the standing hypotheses at63;
- obtains Choice X 1 through choiceExists at66;
- obtains WuBessel C through the actual BesselOfW/multiplicity-one and local-factor results at67–69;
- constructs GoodW for locW C u u tau at70–72;
- constructs GoodS for locS hB u u tau at73–74;
- feeds these concrete data to locB and loopTermOfN at104–113.

The measures are genuine fields of the constructed Choice, not unnamed existential hypotheses suppressed in notation:

Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LocWSOf.lean:78–91 defines Choice with the transport matrices, the translated lowest-type vector, normalized compact Haar measures muW, and quotient measures nuS together with their IsQuotMeas proofs. The actual existence proof is
Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Choice.lean:574–611.
It chooses the transport at577, the lowest-type translation at578–592, compact Haar probabilities at596–603, and quotient measures at604–610, then constructs Choice.mk at611. In particular, the quotient measure condition is produced by quotMeasExists at607–609.

LocWSOf.lean:109–121 defines the actual locW object from those fields. Its GoodW proof at138–145 retains both quotient identities. The predicate GoodW itself is
Formalism/SharpRestriction/CuspSpanNormBounds/NormalizedLocalScale.lean:127–135:
the compact types, middle support, positive-norm values tied to Tr D u, group/compact Haar measures, the normalized unipotent measure, and both quotient measures.

LocWSOf.lean:153–157 defines WuBessel with an actual Bessel map B and the equality of its translated vector with the original local period function. The definitions at159–175 choose B, choose the translated base vector, define the quotient-norm normalization cOf, and rescale the second side. The actual locS object is built at200–207. Its degree is D.dsig tau by209–210. Its GoodS proof at225–229 uses the constructed Bessel maps and GoodSRest.

GoodSRest contains, explicitly, the discrete-series condition, a smooth nonzero base vector, cOf>0, both quotient-norm identities, and formal degree (LocWSOf.lean:212–223). The final proof
RootLatticeThresholds/IsLowUnitHBaseVector.lean:23–27
supplies it from GapHyp, dsigTie, and WuBessel. The immediate helper
RootLatticeThresholds/ChoiceFinal.lean:17–22
uses the nonzero finite quotient norm for both sides. Its other theorem at13–15 supplies WuBesselOfLoc from reproduction under translation and the gap result. The local-factor assembly is explicit in
RootLatticeThresholds/LocFactorAll.lean:15–17,77–79.

The theorem
Development/AbelianVarietyTheory/Proofs/FlagMeasures/BesselMultiplicityOneLargeGapAndWhittakerBessel.lean:9–10
provides UniqGap and BesselOfW by the named source results. The short body was read; the complete proofs of those imported results were not re-audited here.

### 1.2 The final analytic application supplies Std, Side, and IsEll

The local analytic inputs are exact predicates, not a guess from theorem names:

- Development/AbelianVarietyTheory/Definitions/SemilocalFrames/DegVand.lean:51–55 defines LocIn as both MultOne assertions and decay on DD(A.sigma,A.v0) with exponent 2(2r+k+1)^5.
- The same file59–63 defines BSch as the quotient L2 norm scaling identity for every smooth vector.
- FlagMeasures/AmplitudeMultOneDecayOfLargeGapHypotheses.lean:45–78 proves LocIn from the source gap hypothesis, including the actual restriction of the low-type decay estimate at77–78.
- FlagMeasures/SchurAlongFamily.lean:26–33 supplies BSch through besselMap_multipleIsometry_largeGap. Its theorem schur_along_family at37–57 actually combines that BSch with LocIn and the Schur bound.
- DecoratedLatticeProofs/SchurAtRecordGap.lean:54–70 supplies the final sufficiently-large threshold version. It obtains the gap input from uniqGap_and_besselOfW at56, the uniform Schur theorem at57, and the local inputs at59; it invokes the two exact inputs at68–70. The hypotheses retained there are Ties D and the displayed standing/numerical hypotheses through adm11.

For a concrete W,A built above and satisfying these final numerical thresholds, set

  k=D.R.k, r=D.R.rS, n=2r+k+1,
  sigma=A.sigma,
  w0=A.v0/||A.v0||,
  a=2n^5,
  muG=W.muG,
  muS=muProd(W.muW,W.muN),
  nu=W.nuS,
  z=W.z, pi=W.pi,
  c_j=2D.host.ka/(D.host.g(0)D.host.g(1)).

The source chooses a positive Haar density cH and sets

\[
d=\frac{A.\mathrm{deg}}{c_H\,\operatorname{volUn}(n)}>0.
\]

These are exactly the objects constructed in
FlagMeasures/MeasurableBcWeight.lean:193–234:
SideIrr is assembled at203–206, cH is chosen at208–209, the Schur identity with this d is obtained at211–212, and normalized StdSm is assembled at222–226. Both quotient identities are obtained at198–199. The source converts psiS to the constant psiGen at228–231 and supplies both quotient norm-scaling identities at233–234. The subsequent actual call to the exported amplitude theorem is at261–263. The alternate final uniform proof makes the same construction at
DecoratedLatticeProofs/AmplitudeSchurBoundUniformConstants.lean:27–55, especially StdSm at45–48 and the call at52–55.

Finally the full proof
FlagMeasures/LintegralHilbertSchmidtNormSqBesselAmplitudeLe.lean:44–119
constructs

\[
\ell:\ H\longrightarrow W_p,\qquad
\operatorname{IsEll}(z,\psi,\pi,\mu_S,\sigma,DD(\sigma,w_0),\ell).
\]

It uses c0=A.cN>0 and the actual quotient norm c0 dim(Wp)>0. It constructs NonVan from the nonzero square-integrable Bessel function at73–83 and calls
exists_besselMap_rankOne_factorisation_translateSpan at84.
The scalar normalization is

\[
B(\sigma(g)A.v_0)=t\,\ell(\sigma(g)w_0),\qquad
|t|^2=A.cN\,\dim(W_p)\,d.
\]

The proof invokes the actual besselModel_projector_on_line export at105 to establish that normalization. Its following amplitude theorem at121–144 calls the IsEll constructor on both sides at124–126. Thus DET-15's source objects are used inside the final period-norm application, not merely available in an unrelated abstract lemma.

This establishes a conditional construction from the source's actual global setting and numerical regime. No assertion here removes the standing global hypotheses or claims a fresh independent existence proof for their entire upstream arithmetic construction.

## 2. What the inspected weighting exports actually say

The audit followed definitions and exact uses. It did not infer absence from filenames.

| Inspected source | Exact locator | Content relevant to the weighting gate |
|---|---|---|
| CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/TensorWeightedBesselSum.lean | 21–62, full theorem read | Finite Fintype-indexed tensor decomposition. Scalar st(I)=ep(I) kappa1 conjugate(kappa0) s. |
| CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/TensorWeightedBesselGap.lean | 65–81, full file read | Finite orbital-integral identity with tau(I)=ep(I) kappa1 conjugate(kappa0) s/sI(I), or a zero term. It is an identity between finite sums of amplitudes. |
| Development/AbelianVarietyTheory/Definitions/Jets/SumIoPrAlt.lean | 88–94 | TensH explicitly permits ep(I)=1 or -1. Its orthogonality is in the displayed signed tensor form. |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/BlockProjectionBesselStatement.lean | 9–10 | Exact finite sum coefficient ep(I) kappa1 conjugate(kappa0) fdegH(RI(I)). No assertion that these are nonnegative rank-one projector eigenvalues. |
| Development/AbelianVarietyTheory/Definitions/Jets/SideFam.lean | 36–45 | Positive formal degree and Bessel-map factorization for n1(nu)<=q0. This is a finite bounded lattice-shift family at fixed q0, as proved in DET-14. |
| CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/FamilyFunctionalCoefficient.lean | 21–62, full proof read | Produces finite-cutoff coefficient functions with norm \(\lvert s(\nu)\rvert=d_g(\nu)\) when both sides are nonzero and zero functions outside the cutoff. It does not supply an infinite decaying weight sequence on DET-15's vector index. |
| CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/TensorMomentWeightedStatement.lean | 16–17 | A finite Fintype moment inequality for \(\lvert\beta(I)\rvert^2\lVert y\rVert^2\) and a spatially weighted quotient norm. |
| CompanionTheory/AutomorphicTheory/PieriRules/ThetaBesselIsometries/DualTensorCayleyWeightedStatement.lean | 18–19 | A finite tensor/Cayley transport statement, indexed by Fin(2r+k+1). |
| ReciprocityTheory/ReductiveGroups/DiscreteSeries/FormalDegree/CoefLoc.lean | 11–27, full file read | CoefWeightedLoc means spatial integrability of a matrix coefficient multiplied by a matrix-norm power. It is not a summability condition over projector eigenvalues. |
| CompanionTheory/AutomorphicTheory/BesselWaveGrids/WeightedUniformRotatedOfExpansion.lean | 16–27 | The displayed weight multiplies an orbital norm at a point and is a power of a finite minor. Only the displayed definitions and theorem interface were used, not a complete proof audit of this long file. |

The table displays complete source paths. All source paths remain relative to the public mirror root specified at the start.

This source material supplies useful finite identities and analytic estimates. No inspected export in this table identifies its coefficient with gamma_j^(-2), or proves that an infinite sum of these actual projectors has determinant G. This is a bounded statement about the interfaces read, not a claim that no such theorem exists anywhere in the 175187-file mirror.

## 3. Direct obstructions to natural constant and 0/1 choices

Let eta_j be the actual orthonormal model functions obtained in DET-15 and P_j=eta_j eta_j*. If an operator T has T eta_j=beta_j eta_j and |beta_j|>=epsilon>0 for infinitely many j, then the images of those unit vectors satisfy

\[
\|T\eta_i-T\eta_j\|^2=|\beta_i|^2+|\beta_j|^2\ge2\epsilon^2\quad(i\ne j).
\]

They have no convergent subsequence, so T is not compact. In particular an infinite 0/1 choice gives an infinite-rank projection, and a nonzero constant formal-degree scalar gives a noncompact operator. The partial sums with N selected unit weights have trace N, and the difference between two nested distinct partial sums has norm 1 and trace norm equal to the number of newly selected terms. They therefore cannot converge in trace norm or operator norm to a trace-class limit. A finitely supported 0/1 choice gives only a finite-rank determinant polynomial.

The formal degree d is constant when the representation and Haar measure are fixed: that is exactly the source Schur/formal-degree identity used in DET-15. Multiplying all P_j by d or 1/d therefore does not introduce decay in the vector index.

There is a related representation-theoretic obstruction. Let C>=0 be compact on the original infinite-dimensional irreducible H and suppose C sigma(g)=sigma(g) C for every g. If C were nonzero, its top eigenvalue lambda=||C||>0 would have a nonzero finite-dimensional eigenspace. Commutation makes this closed eigenspace invariant under every sigma(g). Irreducibility makes it all H, contradicting infinite dimension. Thus C=0.

This last statement applies if a proposed weighting is required to commute with the whole source representation. No such commutation condition is silently imposed on the arbitrary weighted operators of DET-15 or on the actual tensor coefficients. It rules out only that additional proposed route.

An independent checker (/root/masullo_spectral_bridge, 21 November 2026) independently supplied the same separated-vector and top-eigenspace arguments. The check was mathematical, not a Lean replay.

## 4. DET-17: actual prime-weighted trace-class operators and their mismatch

### 4.1 Actual source coefficients

Write Lambda(n) for the usual von Mangoldt function, with Lambda(0)=Lambda(1)=0. The source proves and uses

\[
\sum_{n\ge2}\Lambda(n)n^{-\sigma}<\infty,\qquad
\sum_{n\ge2}\Lambda(n)n^{-s}=-\frac{\zeta'(s)}{\zeta(s)}
\quad(\Re s>1).
\]

Exact locators:

- Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ExplicitFormula/PerronTruncOf.lean:45–52 constructs the positive real summable majorant;53–60 bounds the complex Dirichlet terms by it. Its special line cLine(u)>1 is shown at8–12, and its proof invokes the general LSeriesSummable_vonMangoldt result at46.
- Formalism/ZeroFreeRegion/ZetaLogDerivativeBounds/NormLogDerivLeLamF.lean:10–31 defines the positive sum and verifies term-by-term Lambda(n)/n^sigma;14–15 invokes the log derivative and absolute summability statements. This complete file was read.
- Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/mellinGchiModOne.lean:168–193 uses absolute summability to interchange the prime ramp and Mellin integral and then invokes the same exact zeta log-derivative identity at191–193.
- Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ExplicitFormula/PerronSumBound.lean:173,190–195 explicitly uses 0<=Lambda(n)<=log n; positivity is also used in PerronTruncOf.lean:85–86.

The trivial upper bound also proves the needed summability independently: choose epsilon=(sigma-1)/2>0. For x>=1, log x<=x^epsilon/epsilon; hence Lambda(n)n^-sigma<=epsilon^-1 n^(-(sigma+1)/2), and the exponent is greater than one.

### 4.2 Construction, exact normalization, and trace

Keep one concrete local source model from section1 and the actual DET-15 projections, now indexed by n>=2. Define

\[
A(s)=\sum_{n\ge2}\Lambda(n)n^{-s}P_n\qquad(\Re s>1).
\]

This is a new combination of the source arithmetic coefficients with the source convolution projections. The inspected exports do not themselves choose the indexing of the model vectors by positive integers or state this operator identity.

Because the P_n are mutually orthogonal rank-one projections, the singular values of the diagonal sum are the numbers |Lambda(n)n^-s|, with zeros omitted. Consequently

\[
\|A(s)-A_N(s)\|_1
=\sum_{n>N}\Lambda(n)n^{-\Re s},
\qquad
\operatorname{Tr}A(s)
=\sum_{n\ge2}\Lambda(n)n^{-s}
=-\frac{\zeta'(s)}{\zeta(s)}.
\]

For real sigma>1 every A_N(sigma) and A(sigma) is positive. The finite operator A_N is the bounded extension of the actual source convolution with coefficient

\[
e_{N,s}(g)=\sum_{2\le n\le N}\Lambda(n)n^{-s}
\,eFun(\mu_G,\sigma_{\rm rep},u_n)(g).
\]

There is no extra factor d: eFun already has the formal-degree factor, and DET-15 normalized each summand to P_n with trace one. The infinite operator has the product-L2 integral kernel

\[
K_s(x,y)=\sum_{n\ge2}\Lambda(n)n^{-s}\eta_n(x)\eta_n(y)^*,
\]

by DET-15's absolute almost-everywhere and product-L2 kernel proof. No assertion of an unproved infinite group-convolution coefficient is needed.

The ordinary determinant is

\[
D_s(w)=\det(I-wA(s))
=\prod_{n\ge2}\bigl(1-w\Lambda(n)n^{-s}\bigr).
\]

The product converges locally uniformly in w because the coefficients are absolutely summable. It has no zeros except those contributed by its nonzero factors: away from the finitely many large factors, the absolutely convergent logarithm series defines a nonvanishing tail. All multiplicities are counted by the number of coincident factors.

This exact positive arithmetic trace is a log derivative of zeta in the parameter s. It is not an assertion that the w-determinant D_s is the completed zeta function, nor that A(s) is the resolvent of a single operator in the Xi parameter. Those are distinct identities.

### 4.3 A complete obstruction at sigma=2, with no PNT or RH

At sigma=2 the determinant's zeros are exactly

\[
w_n=\frac{n^2}{\Lambda(n)}
\]

for n with Lambda(n)>0, i.e. prime powers, counted with factor multiplicity. Let N_2(R) count those zeros in |w|<=R. Every counted n>=2 satisfies

\[
n^2\le R\Lambda(n)\le R\log n<Rn,
\]

so n<R. For sufficiently large R,

\[
n^2\le R\log R,\qquad
N_2(R)\le\lfloor\sqrt{R\log R}\rfloor.
\]

Counting all integers rather than only prime powers is an upper bound, so no prime number theorem enters. Repeated determinant zeros do not cause a problem because the count already counts every contributing n.

For comparison, let N_zeta(T) count nontrivial zeros rho with 0<Im rho<=T, including multiplicity. Titchmarsh, The Theory of the Riemann Zeta-Function, second edition, Theorem9.4,(9.4.3),p214 gives

\[
N_\zeta(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

The local scan work/programme_sources/TitchmarshZeta.txt:7458–7483 was read for this exact formula and its positive-height convention; the formula was already cited in B-01. Put gamma=-i(rho-1/2), so a zero of G occurs at w=gamma^2. The functional equation pairs rho and 1-rho, one at each sign of the imaginary part, with the same multiplicity. Moreover 0<Re rho<1 gives

\[
(\Im\rho)^2\le|\rho-\tfrac12|^2
\le(\Im\rho)^2+\tfrac14.
\]

Thus, allowing an irrelevant bounded number of possible real zeros,

\[
N_\zeta(\sqrt{R-1/4})\le N_G(R)
\le N_\zeta(\sqrt R)+O(1).
\]

It follows that

\[
N_G(R)\sim\frac{1}{4\pi}\sqrt R\log R.
\]

Since sqrt(R log R)/(sqrt R log R)=1/sqrt(log R) tends to zero, D_2 and G cannot be equal. For any fixed a!=0, the number of zeros of D_2(a w) in |w|<=R is N_2(|a|R)=O_a(sqrt(R log R)), so no such rescaling repairs the identity. The same comparison also excludes multiplying by any zero-free entire prefactor. This conclusion uses neither RH nor PNT.

## 5. Search and read scope

Saved logs:

- work/bessel_instantiation_loc_search.txt: actual GoodW/GoodS and Schur usages in the inspected definition and DecoratedLatticeProofs scopes.
- work/bessel_instantiation_defs_search.txt and work/bessel_instantiation_formalism_search.txt: exact definition/constructor discovery. Irrelevant similarly named predicates were not used.
- work/bessel_instantiation_construct_search.txt: successful matches from the initial bounded constructor search. That call also used a nonexistent Formalism/L2* glob, whose error appeared in the tool result. This was corrected by searching the actual Formalism tree, and no conclusion rests on the failed glob.
- work/bessel_instantiation_final_search.txt and work/bessel_instantiation_gap_search.txt: actual final callers and gap/local-factor constructor locators.
- work/bessel_weight_projector_search.txt: 99 exact rconv/eFun and projector/kernel matches in the specified period, Hermitian-curvature, Siegel-lattice, FlagMeasures, and AutomorphicTheory scopes. Relevant statements were opened and read; this was not a complete proof read of all99 matches.
- work/bessel_weight_arithmetic_search.txt: an initial broad term search that also matched unrelated substrings such as exists. No absence inference is made from it.
- work/bessel_weight_arithmetic_exact_search.txt: exact-symbol search over ThetaBesselIsometries, FlagMeasures/Bessel* files, and BesselPeriodGGP found no matching arithmetic bridge symbols. This only locates the boundary of that bounded search.
- work/bessel_weight_sum_search.txt: broad summability discovery, including the genuine neighboring explicit-formula prime coefficients.
- work/bessel_weight_sum_tensor_search.txt: exact summability/trace-ideal token search restricted to ThetaBesselIsometries; no matches. Its mathematical interpretation comes from the actual finite Fintype theorem interfaces read above, not token absence.
- work/bessel_weight_lambda_bound_search.txt: exact source uses of Lambda(n)<=log n.

The mathematical source interfaces and the new proofs are recorded separately in work/bessel_instantiation_weights_events.tsv. Integration-ready text is in work/paper_bessel_weights.tex. The complete saved TeX and note were reread after writing; no mathematical fault was found. Subsequent wording fixes make abbreviated TeX paths explicit, replace Markdown table pipes in absolute-value notation, and accurately describe the failed search glob; those changes were checked separately.
