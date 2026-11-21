# Implications for the programme

Run TRACE_DET_20261121 — 21 November 2026 (Europe/Berlin).

The convention throughout is the one requested in the prompt: the supplied Alpöge RH and Dirichlet-GRH statements are cited as theorems. This audit does not revalidate their complete Lean proof. Every consequence requiring Masullo’s general-Hecke GRH or his spectral/arithmetic trace theorems remains conditional on the particular draft claim and its hypotheses. “Does not follow” below means that the cited result supplies no construction of the additional structure; it is not a logical-independence theorem.

## 1. The main determinant proposal changes substantially

The literal Fable identification is refuted. Its finite Fourier operator is not positive, and its open-path sums are not its trace powers. The corrected identity is

\[
S_k=a^*A^{k-1}a=\operatorname{Tr}(A^{k-1}aa^*),\qquad
\sum_{k\ge1}S_kz^{k-1}
=-\left.\partial_u\log\det(I-zA-u aa^*)\right|_{u=0}.
\]

This is a useful finite determinant relation with a rank-one insertion; it supplies neither the Xi spectrum nor positivity of the operator. DET-01, DET-02 and DET-08 give complete checks. DET-03 also rules out identifying any one fixed polynomial determinant with the nonpolynomial Xi determinant. It leaves limiting families outside the refutation.

The actual Lean definitions inspected give stronger evidence than the toy alone. StatementG defines finite Hermitian pairing minors and a signed Gram determinant. DET-06 satisfies all stated input conditions with a positive signed value 3 but an indefinite Gram matrix with eigenvalues 1 and −3. StatementE and StatementDS define a finite ordered Capelli polynomial and its highest-weight value; DET-07 identifies the exact variable shifts and hypotheses. The exterior-power/period identities in SumIoPrAlt, ProductMoment and FirstNormAddSubsetIndicatorLe establish a real finite determinant connection. None of these displayed objects is by definition a positive trace-class Xi operator.

The actual theorem exports are `Formalism/FormalDegreeBessel/FinalG.lean:21–22`. DET-10 independently proves their finite sign mechanism from the cited Gram identity: in every nonsingular case the Gram matrix has exactly r+1 positive and r+1 negative eigenvalues, so the signed determinant is the product of their absolute values. The k=0 case is necessarily singular. This is a balanced-inertia statement, not positivity of that matrix.

The inspected RH endpoint is now positively identified, rather than inferred from failed keyword searches. DET-09 follows the source to a scalar smoothed von Mangoldt bound on arbitrarily large power windows and a scalar meromorphic Laplace transform. The residue numerator is a finite positive weighted sum of zero multiplicities; the denominator is rho(1−rho). It guarantees nonzero residues, and positive real residues at real poles in (0,1). It does not state positivity of a Hilbert-space operator. This gives a genuine scalar Landau counterpart to Fable’s intuition while refuting its asserted Fourier/Fredholm interpretation.

The surviving operator question is now narrower. DET-15 constructs actual finite Bessel convolution operators on a common infinite-dimensional Hilbert space and proves exact trace-norm convergence for all summable weights. The zero-based choice gamma_j^-2 realizes B plus zero and the Xi determinant without RH; the stipulated theorem makes those weights positive. DET-16 then specifies the same weights and their full multiplicities from the prime-sum scalar through Fourier averages, under RH. The arithmetic scalar-kernel reconstruction is therefore closed. What remains is the historical determinant correspondence and a direct transfer of the finite source sign to that operator or kernel, whose positivity criterion is itself RH-equivalent. DET-05 supplies the general sufficiency theorem, while DET-13 supplies a separate positive-kernel route. The present audit does not prove that every future direct identification is impossible.

The remaining exact historical identifications of the note’s unnamed Stepanov determinant, W(1_S), and the complete step-7 period determinant are tracked in QUESTIONS.tsv and LEDGER.md. They must not be silently replaced by the particular source-neighborhood examples that were found.

## 2. Changes to SA23 and cote 1

| Prior row or claim | Finding and consequence | Exact home |
|---|---|---|
| SA23 §4.1(1), no trace-class determinant for unsquared Xi | Confirmed in the stated ordinary Fredholm/affine-variable form by B-02. Regularized determinants and unbounded generators remain possible. | Cote 1/79, eigenvalue summability and Fredholm zeros; Titchmarsh, Theorems 2.12 and 9.4. |
| SA23 §4.1(2), diagonal B for Xi(sqrt(w)) | Confirmed and made concrete by B-01, on l2 of zero pairs and by a continuous sine-series kernel on L2(0,1). The construction takes zeros as input. | Cote 1/78–80 supplies the abstract determinant mechanism; the Xi application is SA23’s, not a construction written on those sheets. |
| SA23 §4.1(3), RH gives positivity and power traces | Confirmed for the designated normal B. Every realization with the same determinant has the same power traces but need not be selfadjoint; DET-04 is an explicit counterexample. Zero remains in the compact spectrum, and there is no uniform positive lower bound. | Cote 1/79, coefficient comparison with the positive modulus, versus the operator itself. |
| SA23 §4.1(4), Li coefficients | Preserve the obstruction to an S1 operator with unpaired eigenvalues 1/rho. Refute a broader “no trace-class expression” reading: B-03 gives lambda_n=Tr P_n(C), C=B(I+B/4)^−1 and P_n(x)=2−2T_n(1−x/2). Under RH, P_n(C) is positive and lambda_n>0. | Li 1997, §1, Theorem 1; cote 1/79–80; SGA 6, V, exterior powers and Adams logarithmic identity. |
| geo-H-genus | ARC-01 gives the complete corrected coefficient-majorant/genus-zero argument, including origin zeros, nonzero-function hypothesis, radial domination and the three-rotation contradiction. | Cote 1/111–112; Hadamard factorization as the cited background step. |
| geo-H-bounds | The trace-class summability and minimal-type mechanism is used in checked special forms. The original geometry_H.tex proof is not included in this intake and is not claimed to have been reread here. | Supplied SA23 §1.H and §4.1; cote 1/78–79. |
| geo-H-lidskii and geo-H-1956-reconstruction citation gate | The exact published Fredholm zero/invertibility locators were checked: Grothendieck 1956, chapter II §4, Theorem 2 p.354 and Theorem 4 p.359. This closes that locator issue, not an unperformed replay of the original reconstruction proof. | La théorie de Fredholm, Bull. SMF84 (1956), 319–384. |
| Archive growth example | ARC-02 replaces order1 by order1/alpha for product(1−z/n^alpha), alpha>1. | Cote 1/110, lines2–3. |
| Archive sequence threshold and product | ARC-03 replaces limsup by liminf and proves equality with the power-summability threshold. ARC-04 supplies the initial factor/index convention and arbitrary-threshold rescaling. | Cote 1/113, lines8 and17–22. |
| Archive norm/domain readings | ARC-05 fixes the positive modulus and Hilbert–Schmidt norm readings, and restricts the attained support supremum to the actual domain U. | Cote 1/78, (15)–(17); 1/81 item3; 1/110 line1. |

No result here changes the separate Fuglede–Kadison determinant questions on cote 1/28–30, the higher-multiplicity divided-power programme, the Hodge-index prompt, or the K-groups prompt. Those were outside the requested scope and have not been silently marked solved.

## 3. Fable suggestion 3: retain the estimate, replace the operator interpretation

The original suggestion specifies prime q. TOY-01 proves its estimate with k≥2 and extends it to finite fields of prime-power order. The shorter phrase “on Z/q” needs a correction when q is composite:

\[
|R_k|\le q^{(k-1)/2}\|t\|_2^2\|t\|_\infty^{k-2}
\sum_{h=1}^{q-1}\gcd(h,q)^{(k-1)/2}.
\]

The q=4, k=3, t=1 counterexample is exact and sharp for the corrected expression. At k=1 the displayed original formula also fails. The included computation corroborates 144 finite prime-field cases; the universal statements rest on the written character-orthogonality and operator-norm proof.

TOY-02 refutes an inference from positive scalar coefficients or even positive traces of all powers to positive operator spectrum. It does not refute the actual scalar Landau argument or a cohomological no-cancellation theorem with weight and factorization hypotheses. DET-09 records the additional scalar data present in the inspected endpoint.

For t=1 the count belongs to the affine finite-field scheme Q_k=0. A sheaf-theoretic trace interpretation requires t itself to be realized as a constructible l-adic trace function; arbitrary real nonnegative weights do not automatically provide such a sheaf. The exact comparison is SGA 5, III, Corollaries 4.7–4.8, and III B, Corollary 1.3.1. Exterior powers belong to the lambda-operation formalism of SGA 6, V, Definition 2.1, Example 2.2(b), Lemma 2.2.1 and (7.1.1). They are not the divided-power multiplicity mechanism of another prompt.

## 4. Masullo: the affirmative comparison and its limits

Theorem 10.3.2.1 explicitly asserts Schatten1 operators on Hilbert quotients. Conditional on that theorem, MAS-01 is a genuine application of cote 1, with ordinary Fredholm determinants and trace-of-powers expansions. It would be wrong to dismiss the claim as only a formal Schauder-basis trace. The orbital bases of Chapter7 and the quotient Markushevich basis of Theorem10.2.2.1 are distinct objects.

The arithmetic formula is Theorem12.5.1.1, pp.519–520, equations(12.5.1.1)–(12.5.1.3). Its vanishing requirement on C_F^1 excludes all nonzero convolution squares, by MAS-03. Thus the theorem as stated is not directly a test on the Weil positive cone. The strip parameter I is unquantified in the theorem itself; the intended arbitrary positive-width range comes from §§1.2.1 and1.4.5–1.4.8 and remains an explicit qualification.

Theorem13.3.1.1 is a separate central-line formula with capped multiplicities and Mellin-jet vanishings. Its correction instruction and the empty heading13.3.1.2 prevent citing the latter as a completed numbered GRH theorem. The broad general-Hecke GRH conclusion is retained as the draft’s introductory claim, conditional on it.

MAS-BOUND proves that the boundary derivative condition forced by the displayed norm is 2m<s−1, not a non-strict endpoint. The corrected count is min(N,max(0,ceil((s−1)/2))). At s=3 the m=1 mode diverges logarithmically. The difference matters only when a zero’s multiplicity reaches the extra printed order. This is an actual endpoint correction; it does not assert such a zero exists and does not by itself refute the full proposed GRH deduction.

MAS-06 provides a noncompact full weighted convolution example even for an admissible test. It explains why quotient nuclearity and a cutoff geometric trace cannot be interchanged with an uncut full-space trace. MAS-02 also refutes identifying the entire test-function family with one fixed Xi determinant: the zero test already gives determinant1. That separate question is now answered by MAS-10: conditional only on the draft’s full spectral-annihilator theorem, a Green-resolvent transform on the actual centered theta quotient has the ordinary Xi determinant. Section 10 gives the construction and the obstruction to positivity in that metric.

After GRH, unitary centered zero characters yield the nonnegative Weil quadratic sum in MAS-04. This is an Alpöge consequence for zeta and Dirichlet functions and conditional on Masullo for all Hecke functions of all number fields. It does not make the weighted translation action unitary or establish positive selfadjointness in its original quotient metric (MAS-05).

## 5. Exactly what the six programmes now assert

| Programme | Consequence through the cited RH result | Additional structure not supplied by that implication |
|---|---|---|
| Weil | The global zero quadratic form is nonnegative. After the two pole vanishings, the corresponding uncentered local distribution sum has the opposite sign. Connes–Consani AppendixC PropositionC.1 is the exact criterion used. | A geometric realization by arithmetic correspondences, intersections or a positive arithmetic kernel. The local archimedean compression inequality in that paper’s Introduction Theorem1 is already unconditional. |
| Li | All lambda_n>0 for n≥1; B-03 supplies an actual positive trace-class polynomial form after pairing zeros. Li1997 §1 Theorem1. | An arithmetic realization of that paired operator independently of its zero input; no identification with the finite automorphic determinants has been shown. |
| Nyman–Beurling | The indicator(0,1] belongs to the L2(0,infinity) closed span of integer-dilation fractional-part functions. Baez-Duarte, arXiv:math/0205003v1, Theorem1.1. | Particular prescribed approximants or rates need their own theorems. The criterion is no longer an open RH-equivalent assertion; do not replace it by false whole-space density. |
| de Branges | Every positive shift Xi(z+i epsilon) is Hermite–Biehler, with positive reproducing kernels and abstract canonical-system existence. Suzuki, Proposition1.2 and the stated equations. | A specified arithmetic Hamiltonian or kernel. Bare abstract existence is not left open. The older Conrey–Li-refuted positivity conditions remain false, not consequences of RH. |
| Connes | The RH-equivalent global cutoff asymptotic in the applicable zeta and Dirichlet sectors becomes true. Use the author PDF, VIII Theorem5/(16), with the number-field analogue after(37). General Hecke sectors remain Masullo-conditional. | A new direct geometric proof, an ordinary uncut scaling trace, and an identification with B. Established local/semilocal formulas must not be relabeled conjectural. |
| Deninger | A zero-coded selfadjoint ordinate operator and Theta+Theta*=I can be constructed (PRG-DEN-MODEL). The zero-location consequence of a proposed positive cup/star theory holds. | Functorial arithmetic cohomology, flow, cup product, positive star pairing, duality, regularized determinant and distributional trace formulas, and K-theory comparisons. Deninger2005 §3,(2)–(11),Proposition3.2,Theorem3.3. |

The general-number-field extensions in this table have precisely the conditional scope of Masullo’s draft. Neither RH for zeta nor Dirichlet GRH implies the general Hasse–Weil statement for arbitrary schemes over Z.

## 6. The finite-field comparison corrects the positivity dictionary

For a smooth proper geometrically connected curve C/F_q, the actual l-adic cohomology supplies

\[
Z(C,T)=\frac{\det(1-TF\mid H^1)}{(1-T)(1-qT)},\qquad
\operatorname{Tr}(F^n\mid H^1)=1+q^n-\#C(\mathbf F_{q^n}).
\]

The exact sources are SGA5 III B Corollary1.3.1, p.143, and WeilI(1.5.1),(1.5.3),(1.5.4). Purity is WeilI Theorem(1.6). It fixes the complex absolute values of H1 eigenvalues to sqrt(q). A diagonal complex realization of the normalized semisimple spectrum is unitary. It need not be positive, and the numerical normalization is not a canonical half Tate twist.

The curve y2=x3−x over F3 gives eigenvalues ±i sqrt3, so PRG-FF refutes positivity even up to a nonzero scalar. Its alternating cup pairing is a q-similitude, but the separate matrix diag(1,q) shows that a q-similitude identity alone does not imply purity. Polarization, weights and positive-operator structure must be kept distinct.

The common Grothendieck language here is exterior powers, determinants, traces, duality and weights. It does not furnish an EGA/FGA theorem constructing a number-field Hilbert space, a new crystal or a divided-power envelope. Exact text locators are supplied where a real comparison exists; no locator is fabricated for a construction absent from those texts.

## 7. Editorial action

TRANSCRIPTION_NOTES.tsv contains the required mathematical readings, including alternatives that may represent an implicit normalization rather than a misread glyph. Every manuscript attribution still needs the second pass against original images. Neither the generic word “constant” on scan112 nor the alternative square roots uu* and u*u on scan79 is forcibly changed: the checked mathematics does not justify those particular editorial claims.

## 8. Further main-question reductions after checkpoint01

**DET-11 strengthens the scalar endpoint comparison.** With C=B(I+B/4)^−1, the ordinary determinant satisfies det(I−s(1−s)C)=2xi(s), and xi′/xi=(2s−1)Tr[C(I−s(1−s)C)^−1]. Combining this with the actual source Mellin theorem (LandauTheorems/mellinGchiModOne.lean115–118) expresses the source’s smoothed prime-sum Laplace transform by that fixed resolvent trace plus explicit gamma and pole terms. Every normalization and convergence condition is proved and independently checked. Thus the connection is more than a common residue denominator. It remains zero-based: the missing identification is now specifically the passage from the upstream finite period/determinant construction to that fixed operator, rather than the existence of a resolvent representation for the scalar endpoint.

**STEP7-01 makes the interlacing selector concrete.** The determinant of the threshold matrix 1_(u_i>lambda_j) is0 or1 and tests exactly the inspected InterlaceS predicate, under strict decrease and absence of cross equalities. This matrix was constructed by the audit, not located as the historical determinant. In the nonzero case it is upper triangular with ones above the diagonal, and for size at least2 it is not selfadjoint. The source’s half-integral difference condition supplies the essential exclusion of cross equalities.

**STEP7-02 records genuine positive period operators.** Under the actual normalized IsBeL factorization, be(v,v) is the positive rank-one operator eta↦<l(v),eta>l(v), with determinant1−z||l(v)||². These factorizations and their domain/representation assumptions are retained; the cited period-positivity statement takes them as hypotheses. This affirmative positivity must be distinguished both from the balanced indefinite Gram form and from the Xi operator. The actual exterior-period sum also retains its signs, complex kappa factors and formal degrees; its coefficients must not be replaced by0/1.

The deeper source routes additionally checked the release archive’s normalized timestamps and lack of October development history, actual finite-field quadratic point counts, jet-to-ideal-power implications, exact period coefficient relations and interlacing declarations. Those routes are documented in the evidence notes. They do not recover the missing historical W/S/declaration dictionary, and are not counted as closing that gate.

## 9. The two-indicator test and the actual scalar are now connected exactly

STEP6-01–03 prove the complete dictionary for an explicitly normalized Weil quadratic form. If f=1_(0,1] ± X^eta1_(0,1/X], a=X^(eta-1/2), A has the paired ordinates and C=(A²+1/4)^−1, then W_std(f)=2Tr[C((1+a²)I±2a cos(A logX))]. Its cross term is exactly Gz(X)−b(X), with b(X)=log(2pi)−sum_(n>=1)X^(-2n)/(2n(2n+1)), using Ramaré’s corrected Lemma2.1. The plus test gives a lower bound on Gz; the minus test gives the upper bound. A complete global one-sided Landau proof recovers Re(s)>1−eta for0<eta<=1/2; ateta1/2 the specified family is RH-equivalent. This reconstructs the numerical shape of note step6, while leaving the historical W’s linear/quadratic convention, normalization, amplitude and the actual weighted-character/window specialization explicit.

## 10. The actual Masullo–Xi ordinary determinant gate closes

**MAS-10 identifies an operator on the actual quotient.** Conditional only on the full spectral-jet description in Masullo’s Theorem10.2.2.1, choose the actual centered zeta quotient for I=[−1/2,1/2] and s>1. The weighted Green convolution with kernel exp(−mu|u|)/(2mu), mu>1/2+s/4, induces K on that quotient. A numerical-range sector estimate, complete jet flags and Gram–Schmidt prove K is trace class: its positive real part has a finite orthonormal diagonal sum, and the sector bounds its imaginary part by a bounded factor between two Hilbert–Schmidt square roots. This is not an inference from summable eigenvalues alone.

The rational transform R=K(I−mu²K)^−1 is trace class and independent ofmu. Reflection u↦−u gives a canonical even summand, on which R_plus has one reciprocal-square eigenvalue per reflection pair, with full zero multiplicity. Cote1 therefore yields det(I−wR_plus)=Xi(sqrt(w))/Xi(0). This construction uses neither RH nor the draft’s separate nuclearity theorem: every nontrivial zero lies strictly inside the chosen full critical strip, the complex Green eigenvalues have positive real parts, and their absolute values are summable. It is conditional on the draft’s actual spectral quotient claim, not an unconditional construction of arithmetic cohomology.

**MAS-09 shows why this determinant identity is still not a positivity identity.** In the stated weighted quotient, even evaluation vectors have strictly positive mutual correlations. Under RH, distinct real reciprocal-square eigenvalues thus have nonorthogonal adjoint eigenvectors. A multiple zero supplies a Jordanchain; if all zeros are simple, the zero density forces coalescing normalized eigenvectors. Either prevents bounded similarity to a selfadjoint operator. If RH fails, a nonreal eigenvalue already prevents it. Thus this particular actual quotient realization cannot be made positive by a bounded change to an equivalent Hilbert norm. The positive diagonal B remains a different realization.

MAS-07 also rules out obtaining the designated multiplier from one compact smooth test, by uniform Mellin decay in the strip. MAS-08 constructs the heat operators and their inverse-square transform under the draft’s test-operator nuclearity statement; MAS-10 supersedes the provisional small-time trace-norm gate by a direct Green proof. The historical intermediate gate in the evidence notes is explicitly labeled superseded. These results refine the Connes/Masullo analytic quotient comparison; they do not supply Deninger’s functorial arithmetic cohomology, a cup/star polarization, or the missing Alpöge period-matrix identification.


## 11. The finite determinant bridge now has both direct obstructions and concrete positive alternatives

DET-12 rules out the actual rank-zero signed Gram scalar as a positive Hilbert Gram kernel, a positive-type group function, a positive trace-class coefficient of a unitary representation, or a pointwise limit of such kernels. Its two-point matrix has zero diagonal and positive off-diagonal entries. A three-point calculation also rules out its direct interpretation as a squared Hilbert distance. The valid positivity is different: the balanced-inertia determinant line is positive, and on the nonzero-leading-minor chart a Lorentz projection gives an explicit squared norm in a positive space depending on the source data. The whole ambient signed exterior space remains indefinite for k>=2. These are precise finite Hermitian/exterior statements, not a rejection of the actual source sign theorem.

DET-13 supplies an explicit positive transform of that very scalar: the inverse power (1+Gf/(TTprime))^-a, a>0, is a normalized Berezin kernel. This positivity is a known result (Neretin, Theorem3.8 and section4.4), whose exact relation to the source determinant is proved here. Integrating its unit-vector projections against any finite positive Radon measure gives a positive trace-class operator and explicit positive finite Gram determinant approximants. The ordinary Fredholm determinant is the integral series of principal Gram minors. This construction uses no zeta zeros or RH, but its measure and Xi spectral identity are not supplied by the source determinant sign.

DET-14 gives a second affirmative route directly from the actual SideFam period maps and their positive formal degrees. It forms A_I=sum t_nu d_nu be_nu(v_nu,v_nu) on the common target, with an exact positive Gram determinant. For a compatible infinite series, the trace-class condition is exactly the summability of t_nu d_nu||l_nu(v_nu)||². The inspected existence export has finite-dimensional target, and the actual Num hypothesis bounds q0 at fixed ga,h; thus this specific realization cannot yield an infinite Xi determinant without changing data and targets. Its integrated L2 isometry is not by itself a sum of point evaluations. These restrictions apply to that finite target; DET-15 below gives a different fixed infinite-dimensional model. The signed exterior-period expansion has separate signs and complex coefficients and must not be silently replaced by the constructed positive Gram expansion.

These findings sharpen the comparison with cote1/78-80 and SGA6 V exterior powers. They do not create an arithmetic cohomology, a crystal or a motive by terminology, and they do not settle the unnamed historical W/S/declaration correspondence.

## 12. The actual Bessel model realizes B and its finite approximants

DET-15 closes the common-space and operator-existence questions for a source Bessel model. The precise source is BesselModelProjectorOnLineStatement.lean7–8 and its proof71–137, with Std, Side, IsEll and quotient-measure hypotheses retained. Its normalized coefficient eta_u=sqrt(d) l(sigma(.)u) is an isometric representation vector in the common closed Bessel L2 model, and the actual convolution is the positive rank-one projection eta_u eta_u*. The underlying group has infinite measure by explicit Lorentz-boost bands; Schur orthogonality then forces the representation space to be infinite dimensional. Consequently one fixed set of side data supplies infinitely many orthogonal source projections.

For every complex l1 sequence beta, T_beta=sum beta_j P_j is normal and trace class, with exact trace-norm tail sum_(j>N)|beta_j|, trace sum beta_j, product determinant, and an explicit almost-everywhere absolutely convergent matrix kernel in product L2. The special weights gamma_j^-2 give B plus zero and det(I−wT_beta)=Xi(sqrt(w))/Xi(0) without RH. Under the cited theorem those finite and limiting operators are positive. Thus the fixed finite target of DET-14 is not a general obstruction to a source-model Xi realization.

The construction also exposes the sign issue. Positivity of each rank-one projection does not imply positivity of arbitrary complex weights. A zero-independent choice such as2^-j gives a positive trace-class operator, but has a different determinant. The unweighted orthogonal family has divergent trace. DET-16 supplies the Xi weights from the arithmetic scalar under RH, as described below; historical matrix correspondence and a direct finite-sign proof remain separate. Cote1/78–80 applies literally to these S1 operators; SGA6 V supplies the finite exterior coefficients. This does not identify the analytic model with an l-adic realization or motive over Spec Z.

## 13. Fixed Hecke characters now have an actual quotient determinant

MAS-11 extends the MAS-10 Green construction to every fixed unitary Hecke character, still conditional only on Masullo’s full spectral-annihilator theorem10.2.2.1. The strip half-width is chosen greater than1/2, so no boundary nonvanishing theorem is needed. The completed function uses the primitive finite factors, all archimedean gamma factors and the conductor; pure norm characters have their two poles removed. Masullo’s Definition3.2.1.2 already includes the archimedean factors, so this is the correct completed zero set for the spectral quotient.

The Green operator is S1 by the same sector proof. Removing the entire finite central Riesz block gives the inverse-square operator R_chi with the full noncentral zero multiplicities. Let f_chi(z) be the central-zero-removed completed function at1/2+z, and let a_chi=f_chi(0). Its ordinary determinant is the normalized partner product f_chi(i sqrt(w)) f_(chi inverse)(i sqrt(w))/(a_chi a_(chi inverse)). The expression is entire because the product is even. The labeled character-pair even space has this same determinant; the full pair has its square. For a globally self-dual character, the internal even space has the half determinant f_chi(i sqrt(w))/a_chi. Central nonvanishing and simple zeros are not assumed.

This closes an analytic character-sector determinant step, without GRH or the draft’s separate nuclearity theorem. It does not establish positivity in the original quotient norm, nor identify this quotient with a rank-one l-adic sheaf or a functorial arithmetic cohomology. The relevant Grothendieck comparison remains cote1’s trace ideal and determinant formalism, with the exact finite-field cohomological comparison treated separately.


## 14. The Hecke quotient obstruction survives central removal

MAS-12 proves that the actual character inverse-square operator from MAS-11 is not boundedly similar to a selfadjoint operator. The statement is conditional on the spectral-annihilator theorem only and uses neither GRH nor simplicity of the zeros. It also holds on the labeled partner-even space and, for a globally self-dual character, on the internal even space.

The proof separates the possible obstructions. A zero off both centered coordinate axes gives a nonreal eigenvalue. A retained multiple zero gives a genuine Jordan chain because the derivative of −z^-2 is nonzero away from the removed center. In the remaining simple-axis case, Stirling’s formula makes the logarithm of the normalized partner product grow as [F:Q] x log x along the positive real axis. A uniformly separated simple imaginary spectrum could grow only as O(x) in that product, so arbitrarily close distinct large ordinates must occur. Their normalized adjoint evaluation vectors approach each other in the actual weighted quotient metric. Removing the finite central dual-jet span contributes a term tending to zero and does not remove this obstruction.

An invertible bounded similarity to a selfadjoint operator would take those vectors to orthogonal vectors with uniformly positive norms, contradicting their convergence to each other. Hence positive eigenvalues under the appropriate zero-location theorem do not make this quotient operator positive. The determinant agreement with a positive diagonal or Bessel-model realization does not give a boundedly invertible intertwiner. Cote1 supplies the ordinary trace and determinant comparison, while the required Hilbert metric structure remains a distinct issue; no positive cup/star geometry is constructed by this analytic identity.

## 15. The arithmetic scalar reconstructs the full Xi operator under RH

DET-16 defines k(t)=exp(−|t|/2)[G_zeta(exp|t|)−b(exp|t|)] directly from the actual prime-ramp scalar and its explicit archimedean correction. The following are equivalent: RH, boundedness of k, and positivity of every finite matrix [k(t_j−t_i)]. The exact Weil dilation family q_t(x)=exp(−t/2)1_(0,exp(t)] has this matrix as its Gram form. The converse uses the proved global one-sided Landau lemma; it does not assume that the historical undefined W has this normalization.

Under the stipulated RH, Cesaro Fourier averages of k recover its positive atom mass a(lambda). The exact explicit formula proves that m(lambda)=(lambda²+1/4)a(lambda) is a positive integer equal to the full zero multiplicity. Thus both the frequencies and the integer fiber dimensions are specified by the arithmetic scalar, without an input list of zeros. This is a mathematical reconstruction by infinite averages, not a finite numerical extraction algorithm.

The cyclic Hilbert space L2(mu_K) has only one dimension at each distinct signed atom. Atom masses are state weights; they are not ordinary trace multiplicities. Its positive-frequency inverse-square operator gives the reduced simple-zero determinant, which equals G only if all zeros are simple. Replacing each positive atom by C^m restores the full ordinary Fredholm determinant. The resulting C_K has trace k(0)/2=lambda1, B_K=C_K(I−C_K/4)^−1, det(I−wB_K)=G(w), and det(I−s(1−s)C_K)=2xi(s).

Those recovered weights can be placed on the actual DET-15 Bessel projections with exact trace-norm tails and the stated measurable kernel. This closes the scalar arithmetic reconstruction and the source-model realization under RH. The remaining task is a historical finite-matrix correspondence and a direct proof of the sign through that correspondence. Kernel positivity is itself RH-equivalent, so this construction is not an independent proof from the finite signed determinant. Its analytic selfadjoint generator also refines the formal spectral model in PRG-DEN-MODEL, without constructing Deninger’s arithmetic cohomology.

## 16. A genuine prime trace does not identify the Xi determinant

DET-15(d) follows an actual source instantiation: constructed Haar and quotient measures, normalized vectors and Bessel maps enter the large-gap local data, and the amplitude proof explicitly invokes the rank-one projector theorem. This retains the complete standing/global hypotheses. The source does not leave those local operators as unused abstract predicates.

DET-17 combines these projectors with the source von Mangoldt coefficients. The operator A(s)=sum_(n>=2)Lambda(n)n^-s P_n is normal and S1 for Re(s)>1, has trace −zeta_prime/zeta(s), and is positive with positive finite source-convolution approximants for real s>1. Its determinant is the product of 1−w Lambda(n)n^-s.

At s=2 this product cannot be G, even after a fixed nonzero rescaling or a zero-free entire multiplier. Its zero count is at most sqrt(R log R), because n²/Lambda(n)<=R forces n²<=R log R. The Xi determinant has asymptotic zero count sqrt(R)log(R)/(4pi). The mismatch uses the classical zeta zero count and the elementary bound Lambda(n)<=log n, with neither RH nor the prime number theorem. This answers a concrete alternative arithmetic weighting; it does not prove that all other weightings fail.

Infinite 0/1 weights and fixed nonzero formal-degree weights are also excluded by noncompactness. Requiring a positive compact weight operator to commute with the full irreducible representation forces it to vanish. These exact restrictions should accompany any proposed direct period-to-Xi construction; the arbitrary model embedding in DET-15 does not carry a claim of representation invariance.


## 17. The natural Bessel boost cannot be the arithmetic flow

DET-19 gives a concrete covariance obstruction from the actual source Decay hypothesis. The middle-coordinate Lorentz boost has Euclidean operator norm exp(|t|). All source matrix coefficients on the dense orbit span therefore decay exponentially, and density plus unitarity makes every Hilbert-space coefficient tend to zero at infinity. Trace-norm finite-rank approximation gives the same conclusion for every S1 trace coefficient.

The arithmetic cosine kernel does not tend to zero at infinity, even without assuming RH in that conclusion: vanishing would imply boundedness, hence RH by DET-16, and its nonzero Cesaro atom masses would then contradict vanishing. Thus it cannot be a vector coefficient or S1 trace coefficient of that natural boost. The boost has no nonzero finite-dimensional invariant subspace and no nonzero compact commutant; under RH every bounded intertwiner from the arithmetic pure-point model into it is zero. Exact coefficient covariance transfers these assertions to the closed isometric Bessel image, without asserting an ambient quotient-L2 translation action.

The Bessel-model Xi operator still exists, with the already proved finite source-convolution approximants and determinant. It does not commute with this boost, and its arithmetic flow is a different action. The obstruction is specific to that natural covariance proposal; it is not a general nonexistence theorem for arithmetic realizations. A historical scalar sign certificate could also suffice without any flow identification: an actual positive-normalized determinant equal to 2k(0)+2k(log X) would give the STEP6 lower bound and its Landau consequence. The missing datum remains the exact source determinant and specialization realizing that formula.


## 18. The actual rational character endpoint has an ordinary determinant after integer multiplication

DET-18 treats the source’s actual primitive finite family, whose nontrivial weights are1 or1/(3o+1), with zeta weight1. Set M=2(3o+1). The normalized completed product of F_zeta^M and (F_chi F_(chi inverse))^(M alpha_chi/2) is entire, symmetric under s->1−s, and equal to det(I−s(1−s)C_LM) for an explicit diagonal normal S1 operator. All exponents are integers. The construction uses neither GRH nor Masullo’s draft spectral theorem.

For each noncentral reflection pair, the eigenvalue is1/[rho(1−rho)] with multiplicityM S_rho. At the central point, eigenvalue4 has multiplicityM S_half/2: the central half is required because s(1−s)=1/4−(s−1/2)². The weighted completed logarithmic derivative is (2s−1)/M times the ordinary resolvent trace. DET-18 gives the exact actual Mellin transform on Re(s)>1, including conductor and gamma terms, zeta pole corrections and the constants Lprime(1,chi)/L(1,chi), and recovers the source residue S_rho/[rho(1−rho)]. Thus the weighted-character scalar representation is closed as well as the earlier zeta-only case.

Without integer multiplication, an ordinary determinant exists exactly when every noncentral S_rho and the central S_half/2 are nonnegative integers. The actual inverse-closed family simplifies the half-average, but positivity alone does not prove those divisibility conditions. No actual fractional residue is asserted. The divisor-level minimal multiplier is the least common multiple of the stated denominators and divides2(3o+1). The exact operator criterion for the retained family is GRH iff0<=C_LM<=4I; positivity alone would permit a real off-center zero with eigenvalue above4. Scaling the trace by1/M also cannot generally be implemented by scaling the operator by1/M, as the second moments show.

This is the analytic counterpart of integer multiplicities in an ordinary determinant and its exterior-power coefficients (cote1/78–80; SGA6 V(7.1.1)). Clearing rational weights produces an integral effective spectral divisor; it does not construct a sheaf or cohomological realization. The remaining correspondence is the original finite period/determinant family and its sign, including the source’s window specialization—not the existence of an ordinary representation of the completed weighted scalar.
