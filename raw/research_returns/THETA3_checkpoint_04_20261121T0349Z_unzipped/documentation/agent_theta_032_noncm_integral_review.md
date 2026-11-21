# Independent review of THETA3-C01–C10

Reviewer: GPT-6 Astra Pro, sub-run `/root/theta_032`. Date: 21 November 2026 UTC. The inherited reasoning-effort label is not separately exposed. I read every proof C01–C10 in full, reconstructed the deductions below, and checked the cited source statements supporting their hypotheses. This is an independent model review, not a human review or a formal proof certificate. The deep external theorems remain cited inputs; I do not claim to have independently proved them.

## Outcome and corrections

All ten deductions pass within their stated scopes. C03 needs an explicit choice of the actual Hermitian space defining Schoen's lattice, rather than an inference from equality of its CM field. Keep the principal congruence base separate from the potentially noncongruence common cover. C05's derived-group argument is valid. C06 and C07 use the correct Li–Zhang signs and types. C10's distinction between Chow nonvanishing and ordinary Hodge classes is correct.

One source-transcription issue was found and corrected by rendering the PDF: Li–Liu II Example 1.10 assumes **r ≥ 2**, not r > 2. Likewise Theorem 1.4's auxiliary-set condition is a cardinality **at least 2**. Text extraction from this PDF drops equality bars. Printed pp.4–6 were visually checked in `work/external/LiLiu_AIPF2.pdf`; the page images are `LiLiu_Theorem1_4.png`, `LiLiu_Theorem1_5.png`, and `LiLiu_Example1_10.png` in the same directory.

## C01: the congruence H¹ obstruction

**Status: pass.** Liu, *Fourier–Jacobi cycles and arithmetic relative trace formula*, Corollary 4.20, printed pp.54–55, applies to the full Albanese for Hermitian rank n ≥ 3. At rank 2 only the endoscopic part is covered. Proposition 4.13 and Theorem 4.18 give the oscillator and CM-factor mechanisms, respectively. I previously read the full proof of Proposition 4.13 and the statement and relevant argument of Theorem 4.18; this review treats the classification and Albanese theorem as cited background.

For a simple non-CM abelian variety B, H¹(B,Q) is a simple polarizable rational Hodge structure. A nonzero morphism into a CM Hodge structure would inject it into a torus representation. Its Hodge homomorphism would then factor through a torus, contradicting non-CM. Finite sums, tensor products, duals, and Hodge subquotients of CM structures remain representations of a common torus, proving the tensor-category assertion.

The restriction to the standard congruence unitary Shimura setting and trivial-coefficient H¹ is essential. The proof does not prohibit non-CM higher cohomology or H¹ on noncongruence covers. It therefore genuinely rules out obtaining new non-CM Albanese factors merely by raising the dimension of the congruence ball.

## C02: the trace-zero selection rule

**Status: pass.** For a degree-d finite étale cover f, transfer satisfies f_*f*=d. Thus P=d⁻¹f*f_* is a rational Hodge projector, and its kernel is exactly ker f_*. For u in that kernel and three old classes,

\[
\int_Xu\smile f^*v_1\smile f^*v_2\smile f^*v_3
=\int_S f_*u\smile v_1\smile v_2\smile v_3=0.
\]

A simple non-CM sub-Hodge structure U maps trivially under f_* into a CM H¹(S), by C01's elementary argument. No Galois-cover hypothesis is used. The deduction concerns this specific four-factor pairing: one trace-zero factor cannot be detected against three old factors. It does not prohibit all periods involving non-CM classes.

## C03: common-cover construction and the exact Schoen input

**Status: pass after making the V-choice and level order explicit.**

### What the source actually supplies

Schoen, *An arithmetic ball quotient surface whose Albanese variety is not of CM type*, ERA 21 (2014), pp.132–136, states on printed p.133 that the covering lattice of his surface Y has finite index in a congruence subgroup of a unitary group defined by a rank-three Hermitian form over Q(ζ₅)/Q(√5), definite at one real place and indefinite at the other. This statement cites Yamazaki–Yoshida, §4 Theorem 1 and Proposition 4.3. Schoen then constructs a finite étale cover X₀ mapping onto the genus-one curve with equation s²=x⁴+x³+x²+x+1, whose j-invariant is 2¹¹ and which is non-CM (pp.133–134). I checked both the full-paper reproduction and the downloaded publisher PDF `work/external/Schoen_ball2014.pdf`.

The equal field alone would not identify a commensurability class. Instead **choose the arbitrary Hermitian space V permitted in 032 §4.1 to be the actual space appearing in this source statement**. Multiplying its form by a scalar a∈F× with prescribed signs at the two real places makes its signatures exactly (2,1) and (3,0). Such a exists by weak approximation. This scalar multiplication preserves the algebraic groups U(V) and SU(V), since the equation preserving a·h is the equation preserving h. The pair E=Q(ζ₅), F=Q(√5) meets 032's Galois-CM and [F:Q]≥2 assumptions.

For a lattice-preserving integral unitary group, determinants are norm-one units in O_E. Each complex conjugate has absolute value one, so Kronecker's theorem makes these determinants roots of unity; their image is finite. Passing to its kernel gives a finite-index special-unitary subgroup. Arithmetic subgroups attached to different O_E-lattices in the same rational Hermitian space are commensurable. Hence a sufficiently small principal SU level in 032 can be compared to Schoen's lattice in the same projective ball group. No unproved equality of arbitrary Hermitian local invariants is needed.

### A clean order of construction

Do not rename a noncongruence common cover as the principal base S₀. Instead write Γ_X for the lattice of X₀ and Γ₀ for a torsion-free principal congruence lattice of the chosen V, conjugating the ball realization if necessary. They are commensurable.

1. Choose a nonzero invariant differential α₀ on the non-CM elliptic curve E₀. Its pullback by a₀ is nonzero. Choose a point of X₀ at which it is nonzero and a lift z to the ball D.
2. Apply 032 Proposition 4.5, printed pp.21–22, to this point and the fixed permitted v. The values of actual finite-input theta one-forms span T*D at z. Select one β with α_z∧β_z≠0. Only finitely many inputs are needed to make this selection.
3. Choose a principal Γ_S⊂Γ₀ deep enough for the selected inputs to descend and for 032 Theorem 5.1 / Corollary 6.7 to give the rational CM-source expansion on S=Γ_S\D.
4. Put Γ=Γ_X∩Γ_S in the projective ball group, and X=Γ\D. Then X is a common finite étale cover, because Γ has finite index in each torsion-free lattice. The pullback wedge remains nonzero at the corresponding lift of z.

The maps between compact ball quotients are holomorphic finite étale maps, hence algebraic for their projective structures. This construction never asserts that Γ itself is congruence.

### Positivity, extraction, and image dimension

For ξ=a*α₀∧f*β, the local expression ξ=g dz₁∧dz₂ gives

\[
\xi\wedge\bar\xi=4|g|^2\,dx_1\wedge dy_1\wedge dx_2\wedge dy_2.
\]

Thus its integral is strictly positive. In dimension two this sign is positive without adding an i-factor.

By 032 Theorem 5.1 (statement p.26; conclusion proved in §6.3) and Corollary 6.7 (p.45), the class of β is a finite complex combination of rational Hodge-map images of U(v)₁. Holomorphic one-forms on a compact Kähler manifold are the unique holomorphic representatives of their cohomology classes, so the equality of classes is an equality of forms. At least one term has nonzero wedge with a*α₀. By the Albanese realization of 032 Lemma 2.2, multiplying the corresponding rational Hodge map by a positive integer gives the pullback of a morphism to B(v). The integer can be absorbed into the selected invariant differential.

The resulting map (a,b):X→E₀×B(v) has differential rank two on a nonempty open set because the two pulled-back one-forms have nonzero wedge. Its image is a surface. Proper pushforward of [X] gives an algebraic cycle of codimension dim B(v)−1. Pairing this pushforward with the corresponding (2,2)-form pulls back to the positive integral, so its cohomology class is nonzero.

The non-CM forms occur twice, as α and its conjugate, which is consistent with C02. Only β is obtained through the old congruence theta machine. This is a genuine mixed period and algebraic surface, but C05 explains why it does not create a previously inaccessible Hodge-conjecture case.

## C04: exact extraction and rank

**Status: pass.** An algebraic correspondence applied to an algebraic class remains algebraic. Under a nondegenerate rational form Q on T, the map T→T*, x↦Q(x,−), is an isomorphism. Therefore rank d of the test matrix is exactly the assertion that the projected algebraic classes span T. In the correspondence-algebra variant, the span of D·e cl(Z) is a D-submodule; if T is simple, nonzero is equivalent to spanning.

No geometric positivity is required for this argument. The Q² example correctly shows that nonzero scalar pairing alone cannot force a test vector into the algebraic span. It is a counterexample to an inference, not a purported nonalgebraic Hodge class. The final implication must retain the algebraicity of the projector e.

## C05: the product Hodge group

**Status: pass.** Moonen's *Notes on Mumford–Tate groups*, Example (2.6), printed p.11, explicitly states Hg(E₀)=SL₂ when End⁰(E₀)=Q, and identifies the CM elliptic case with a torus. I opened and checked the exact statement at https://www.math.ru.nl/~bmoonen/Lecturenotes/CEBnotesMT.pdf.

Let H=Hg(E₀×B)⊂SL₂×T, where T=Hg(B) is a torus. The projections of H onto the factors are surjective by the defining minimality of the Hodge group. Since H is connected reductive, a surjective algebraic-group morphism maps its derived subgroup onto the derived subgroup of its image. Consequently H^der projects onto SL₂ and trivially to T. The first projection on the subgroup SL₂×1 is an isomorphism, so a subgroup contained there with full first projection is all SL₂×1. Hence SL₂×1⊂H. Surjectivity of H→T then gives H=SL₂×T: any element above t can be multiplied by a suitable element of SL₂×1 to obtain (1,t).

This uses the actual algebraic group SL₂, not merely a projective group or a claim about Lie algebras with an uncontrolled finite central quotient. It is therefore sufficient as written. Taking SL₂-invariants kills the H¹(E₀) Künneth part and preserves H⁰(E₀) and H²(E₀). The displayed decomposition of Hodge classes follows, and the stated assumption that Hodge classes on B are algebraic supplies algebraic representatives. The conclusion is only for one E₀ factor; powers of E₀ have additional SL₂-invariant tensors and require a separate statement.

## C06: negative rank-three intersection

**Status: pass.** I checked the local field assumptions, the definition of type, and the normalization against Li–Zhang, *Kudla–Rapoport cycles and derivatives of local densities*, author PDF dated 10 September 2021, Definition 3.2.1 (p.16), Theorem 3.4.1 (p.17), Theorem 3.5.1 (p.18), and Corollary 3.5.3 (p.19). The source is now local at `work/external/LiZhang_KRProof.pdf` and `.txt`.

The following is an independent reconstruction of the computation, conditional on those cited density/intersection theorems. For Gram matrix πI₃, val(L)=3 is odd, so the ambient Hermitian space is the source's nonsplit V₃. If N⊃L is integral and ℓ=length(N/L), then val(N)=3−2ℓ≥0; hence ℓ∈{0,1}. Integrality implies N⊂L∨=π⁻¹L. A length-one enlargement is uniquely specified by a projective line represented by v mod π in L/πL, through N=L+Oπ⁻¹v. The cross pairings with L are already integral, while the new norm is integral exactly when h(v,v)∈π²O. Since h=πI₃, this is exactly isotropy of the residual line for I₃ over F_{q²}/F_q. The condition is independent of the representative v.

Every such enlarged N has determinant valuation one, so its nonnegative elementary divisors sum to one: its type is one. L itself has type three. The recurrence for zero-norm vectors is valid because a nonzero prescribed norm has q+1 preimages in F_{q²}; it gives q³+1 isotropic projective lines in rank three. Thus

\[
\begin{aligned}
\operatorname{Den}(X,L)
&=(1-X)(1+qX)(1-q^2X)+(q^3+1)X^2(1-X)\\
&=(1-X)\bigl(1+(q-q^2)X+X^2\bigr),\\
-\operatorname{Den}'(1,L)&=q+2-q^2.
\end{aligned}
\]

This is negative for q≥3. I also independently enumerated the projective charts (1,a,b), (0,1,a), and (0,0,1) over explicit quadratic fields for q=3,5,7, obtaining 28,126,344 isotropic lines and derivatives −4,−18,−40. This finite computation checks examples only; the recurrence and overlattice proof cover general q.

The arithmetic intersection in the theorem is a derived Euler characteristic. Full rank of the input lattice does not turn it into the ordinary length of a zero-dimensional scheme-theoretic intersection. The negative answer therefore refutes indiscriminate positivity in exactly the stated local setting. The source's separate vertical calculation, Lemma 6.2.1, pp.35–36, is consistent with the value. No factor log(q) belongs in Int=−Den'(1); the log(q²) factor occurs upon conversion to a Whittaker derivative in §3.3 / Remark 3.4.2.

## C07: positive self-dual-cancellation sector

**Status: pass.** The perfect pairing on the self-dual summand M implies that the orthogonal projection of every integral vector y∈N onto M's fraction space lies in M: the functional h(y,−)|M is integral and M identifies with its dual. Hence every integral enlargement splits as M⊥π⁻ʲOx. Containment requires j≥0 and integrality requires 2a+1−2j≥0, giving exactly 0≤j≤a. The remaining elementary divisor is positive odd, so every summand has type one. The polynomial and derivative are therefore precisely

\[
\operatorname{Den}(X,L)=(1-X)\sum_{j=0}^{a}X^{2j},\qquad
\operatorname{Int}(L)=a+1.
\]

This also agrees with the source's cancellation formula (3.2.1.1) and rank-one Example 3.5.2. It gives an exact local lower bound in this sector. It supplies no identification with an archimedean period until an additional local matching theorem is given.

## C08: vertical versus generic-fibre classes

**Status: pass with the word “local” retained.** At the meeting point of the section and special fibre in P¹_R the regular local parameters are a section coordinate and π; quotienting by both gives the residue field, of length one. The special fibre has empty generic fibre, so its restriction to generic Chow groups and cohomology is zero.

The special fibre is globally principal as a divisor, which does not invalidate this local intersection-length example. One should not advertise it as a nonzero global Chow intersection degree. The counterexample addresses a proposed implication from positive local vertical intersection to nonzero generic realization. The converse sentence about a specified horizontal flat cycle is correct: its generic fibre is algebraic by construction, while its identification with a particular Hodge class remains a different problem.

## C09: reciprocal degrees and products

**Status: pass.** Section 4.1, printed p.20, of Li–Zhang gives degree e_s=q^s(1+q⁻¹)=q^{s−1}(q+1) for s≥1; s=0 is a separate canonical level. Thus the geometric sum is q/(q²−1).

For partial products P_N=∏_{s≤N}t_s with v(t_s)=1/e_s, the absolute values |P_N| tend to a strictly positive number, since their valuations tend to the finite displayed sum. Any convergent sequence P_N would therefore have a nonzero limit. Then t_N=P_N/P_{N−1} would tend to one. But |t_N|<1 for every N gives |1−t_N|=1, a contradiction. This argument needs neither phases nor algebraicity assumptions on the t_s. It does not identify the actual theta derivatives with these coordinates; it rules out only the naïve convergent-coordinate-product interpretation.

## C10: the precise motivic slot and Li–Liu hypotheses

**Status: pass.** The elementary statement follows directly from the meaning of homological triviality: cl_B(Z)=0 has zero cup product against every cohomology class. Homological equivalence implies numerical equivalence, so a nonzero height cannot recover a nonzero ordinary numerical or Betti class. It can detect information retained by Chow or Abel–Jacobi realizations.

The external theorem is not asserted as independently proved here. I checked Li–Liu II, Assumption 1.3 and Theorems 1.4–1.5 (printed pp.4–5), Remark 1.9 and Example 1.10 (p.6). Theorem 1.4 gives localized homologically trivial Chow nonvanishing under its central simple-zero and local assumptions; Theorem 1.5 additionally assumes Hypothesis 4.11 to define the arithmetic theta lift and state the height formula. Remark 1.9 removes the cited Hypothesis 6.6 when S_π is empty.

The example starts with r≥2 and a modular odd symmetric power of a non-CM elliptic curve. Good reduction at every nonsplit finite place is the stated criterion for the required unitary representation, and gives S_π=∅. The relevant root sign then is (−1)^{r[F:Q]}; choosing both factors odd supplies the sign needed by the theorem. No specific elliptic curve with a verified nonzero central derivative is constructed in C10. Its claim is a framework and conditional application, not a newly certified numerical example.

For a full theorem transcription also retain Theorem 1.4's choice of an auxiliary set R containing R_π and having at least two places in R∩V_F^spl∩V_F^♥. The printed PDF confirms the inequalities are non-strict.

## Check-record boundary

The separate file `work/agent_theta_032_noncm_integral_CHECK_EVENTS.tsv` records ten independent re-proofs/reviews, the C06 finite computation, and the source/typography checks actually performed. It does not label the external density theorem, CM Albanese theorem, arithmetic theta theorem, or source-paper classifications as newly proved. The overall file inventory is changing as other agents retrieve additional source archives; no assertion of permanent source unavailability is made in this review.


## Independent continuation: C11 sharp bound and actual theta frame

Read the complete new arguments and primary Katz pages 667, 669, 672. The trace reduction is valid over the stated finite-extension DVR: the basis traces generate exactly pA, and g=p f-[p]^*(Tr(f)/p) has trace zero because the covering degree is p squared. Applying the cited Katz theorem and D^a[p]^*h(0)=p^aD^ah(0) gives the sharp uniform loss one. The example a=p squared minus one, f=T^a, attains that loss. The finite-jet extension to O_Cp and integral coordinate-change statement have the stated hypotheses.

For y squared=x cubed minus x with t=-x/y, independent differentiation gives omega=(1+4t^4)^(-1/2)dt. The Weierstrass equation gives sigma=z-z^5/60-z^9/10080+O(z^13); composition with lambda=t-2t^5/5+2t^9/3+O(t^13) gives t-5t^5/12+1411t^9/2016+O(t^13). BK Example1.9 identifies the normalized reduced theta with sigma when the weight-two Eisenstein correction vanishes; square-lattice symmetry forces that vanishing. The t9 coefficient has 7-adic valuation minus one. An independent count gives eight points over F7 and therefore supersingularity. These are full targeted mathematical checks, with the Katz theorem carried as a cited input.


## Independent continuation: C15 and C16

Read all of `paper_C15_C16.tex` and reconstructed both proofs. The directed curve-cover transfer is valid: each connected component of the etale pullback surjects onto the original connected ball surface and therefore onto the covering curve. Albanese surjectivity follows from injection on holomorphic differentials. The exact BT direction and its characteristic-zero conditional scope agree with `BT_ram2002.txt`, Definition p1, Proposition1.8 p2 and Example3.1 pp5-6. The countability argument concerns a fixed tower or a countable family of towers and does not prohibit density or the conditional assertion over Qbar.

The C16 torsion-branch construction is valid. After rebasing one branch point to the elliptic origin, pullback under odd multiplication retains branching at every torsion point. The resulting double cover is connected because it is branched. The local normalization of u^2=v^(2e) has two unramified branches over the v-disc, proving the etale claim on every sheet. The degrees are at most d N^2 over C, four over H, and 2dN^2 for the ball cover. Odd torsion is dense and finite configurations can be placed at a common odd level.

A separate Sympy computation, not the author's certificate script, verified the short Weierstrass coefficients, j(r), the primitive resultant polynomial, its irreducibility modulo11, the Bezout identity, j(E)=2048 and discriminant1458000. The proof must attribute the degree-divides-four statement to J^14641=J; this wording was corrected by the author. Milne's exact modular-polynomial and CM-integrality statements were opened and read.

For infinitely many factors, p=1 mod20 gives full rational2torsion and trace2 mod4; Hasse excludes a nonzero multiple of p, so the reduction is ordinary. The finite-flat p-torsion argument is sound: special-fiber translations equalize local lengths, henselian idempotents lift the p components, and each rank-p generic etale component supplies p points above its special point. The chosen cross ratio has positive valuation and its j negative valuation. Avoiding all rational denominator primes of earlier j-values excludes isogeny by the monic modular equation. The elementary Phi20 Euclid construction supplies suitable new primes. Stoll's exact Frobenius and torsion statements were read.

Finally, read the whole C12 function-field degree125 proof. In C16 the selected etale component maps dominantly to D1 times D2 because it surjects onto Y and hence C0 squared; the degree is at most125, followed by at most4 times4. The period is the positive integer d<=2000 with the displayed Koszul sign. Repeating the two projections gives a product of diagonal divisors, so the proof correctly does not claim an exceptional Weil component.
