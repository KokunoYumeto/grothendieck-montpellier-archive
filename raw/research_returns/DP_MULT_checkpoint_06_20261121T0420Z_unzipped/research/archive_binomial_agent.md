# Archive and binomial-ring report

Agent: `/root/archive_binomial`; model: GPT-6 Astra Pro, inherited; reasoning effort: not exposed by the runtime. Run: DP_MULT_20261121. Client date: 2026-11-21 (Europe/Berlin). Work began 2026-11-20 UTC and continued across midnight Berlin. This report is for integration by the parent, not an independent final package.

## 1. Conclusions first

1. Cote 54 scan 7 does **not** assert that the invariant derivation on an abelian variety has zero restricted p-power. Its box concerns the **vector-group kernel** `t_A^vee` in the Hodge extension `S_A`. It has zero restricted p-power for every abelian variety, ordinary or supersingular. Suggestion 2's identification of the boxed statement with the vanishing Hasse invariant is false.
2. The reconstruction question in cote 54 scan 7 has an existing answer over a perfect field: Oda, Corollary 5.11 (1969), printed p.131, identifies `H^1_dR(A)` with the contravariant Dieudonne module of `A[p]`, respecting `F,V` and the Hodge filtration. This is independent of RH or GRH. Oda explicitly identifies it as Grothendieck's conjecture.
3. The exact binomial/homotopy statement is affirmative: integral cochains represented by the **cosimplicial** ring `n |-> Map(X_n,Z)` have degreewise binomial operations and identity Adams operations; for connected nilpotent finite-type spaces this object recovers the space by derived maps to Z (Horel, Theorem 5.4). This was already a theorem in 2024.
4. The finite-difference calculus of integer-valued polynomials has an exact divided-power associated graded. Ordinary differentiation nevertheless fails to preserve integer-valued polynomials. These assertions give a precise algebraic bridge and an explicit limitation: they do not identify this construction with the invariant-derivative valuation bound on a formal group.
5. The formal disc ring `Z_p[[t]]` does not itself have the identity as a Frobenius lift, because `t^p-t` is not divisible by p. It is not a binomial ring. A positive local derivative bound does not by itself specify a crystal, a PD ideal on `(t)`, or a global theta-function stratification.

## 2. What the archive actually says

### Cote 54, scans 3, 5, 6, 7

Scan 3 sets `B=A^vee`, `t_B=H^1(A,O_A)`, and `t_A=H^0(A,Omega_A^1)^vee`. It defines

`S_A : 0 -> t_A^vee -> H^1_dR(A) -> t_B -> 0`.

It then constructs the universal vector extension of A with vector kernel `t_B^vee`, and says its tangent extension is `S_B` and is transposed to `S_A`. Thus the kernel in the box of scan 7 is the Lie algebra of an additive vector group, not `Lie(A)` equipped with its own restricted operation.

Scan 5 asks to compare these extensions and dualities with Cartier duality of `A[p]` and `B[p]`. Its `F^A=Gr(t_A)` is `ker(F_A:A->A^(p))`, of degree `p^g`, inside `A[p]`, of degree `p^(2g)`. Here `Gr` is the height-one group attached to a restricted Lie algebra; it is not assumed to be an alpha_p group. The assertion that `F^A` and `F^B` are orthogonal concerns the Cartier pairing.

Scan 6 contains unrelated flattening material ("Proposition A"). This is an interleaved verso, not a missing step in the Cartier argument. The official Montpellier inventory itself warns that versos often contain unrelated mathematical work. No conjectural chronological date should be inferred from a verso's text.

Scan 7 returns to the Frobenius--Verschiebung diagrams and the exact sequence

`0 -> A[F] -> A[p] -> D(B[F]) -> 0`.

It observes that `S_A` is an extension of abelian restricted Lie algebras with zero p-operation on `t_A^vee`, hence determines an extension of radicial groups of height at most one; it asks whether this extension can be recovered from `A[p]`.

### ABA-1. Correct interpretation of the boxed p-power statement (checked)

**Statement.** Let k have characteristic p, let A/k be an abelian variety, B its dual, and consider the tangent extension of the universal vector extension of B. The restricted p-operation is zero on the vector kernel `H^0(A,Omega_A^1)=t_A^vee`, without any condition on the Hasse invariant of A. Therefore the boxed assertion in cote 54 scan 7 is not equivalent to supersingularity of an elliptic A.

**Proof.** The invariant vector fields of `G_a^g` are the constant derivations `sum a_i d/dx_i`. The summands commute. In characteristic p their p-th power is `sum a_i^p (d/dx_i)^p=0`, since each p-fold derivative of a monomial has a factor divisible by p. A homomorphism of smooth groups induces a map of restricted Lie algebras, so the vector kernel in the extension carries this zero operation. This applies to every A. In contrast, the invariant vector field `x d/dx` on `G_m` satisfies `(x d/dx)^p=x d/dx` in characteristic p (on x^n, both sides act by n modulo p). Over an algebraic closure, the Frobenius kernel of an ordinary elliptic curve is `mu_p`; in particular its Lie p-operation is nonzero. Ordinary elliptic curves still have the same additive vector kernel in their universal extension. Thus the two assertions are distinct. QED.

**Exact framework locator.** SGA 3, Expose VII_A, 6.3--6.4 for the restricted operation, 7.2, 7.3, 7.4 and the summary 8.1 for the height-one group/restricted-Lie equivalence. The original re-edition has a cross-reference in 8.1 to "theoreme 7.4.1", but the theorem heading is 7.4 and 7.4.1 is a proof subsection. Use VII_A, 7.2--7.4 and 8.1 to avoid a numbering ambiguity. Current Gille--Polo edition: Remark 7.5 explicitly states the equivalence.

### ABA-2. Cartier sequence and reconstruction (checked application of cited theorems)

**Statement.** Let k be perfect of characteristic p and let B=A^vee. The sequence in cote 54 scan 7 is canonical. Moreover the filtered F,V-module

`0 -> H^0(A,Omega_A^1) -> H^1_dR(A) -> H^1(A,O_A) -> 0`

is functorially recoverable from A[p]. With the restricted p-operation on the middle vector space defined by its p-semilinear Frobenius, this also recovers the corresponding restricted-Lie extension and hence the associated height-one group extension.

**Proof.** Cartier duality of isogeny kernels identifies `D(B[F])` with `A^(p)[V]`. The restriction of `F_A:A->A^(p)` to A[p] has kernel A[F] and is fppf-surjective onto A^(p)[V], because `[p]=V_A F_A` and F_A is fppf-surjective. This proves the displayed group-scheme sequence, as well as the orthogonality in scan 5: `B[F]` is the kernel of the map dual to the relevant quotient, so its annihilator is A[F]. The isogeny-kernel Cartier pairing and its functoriality are Oda Theorem 1.1 and Corollary 1.3.

Now let `M=M(A[p])` be the contravariant Dieudonne module. Oda Corollary 5.11 gives a canonical F,V-compatible isomorphism `M -> H^1_dR(A)` with `VM=ker(F)=H^0(A,Omega_A^1)`; the quotient is `H^1(A,O_A)`. The abelian restricted Lie algebra associated with a p-semilinear endomorphism F is the underlying abelian Lie algebra with `x^[p]=F(x)`. Since `FV=0` on M, its subspace VM has zero p-operation.

For completeness, the operation F here really is the restricted operation on the universal extension, not an arbitrarily chosen semilinear map. Use the standard realization of `E(B)` as the group of algebraically trivial line bundles on A rigidified at the origin and equipped with integrable connection. This realization is Mazur--Messing, chapter I, 2.6, Propositions 2.6.7, 3.2.3, 4.2.1 and (4.6.3); the combined statement and these exact locators are also recorded in Oh--Shimizu, *Moduli stacks of crystals and isocrystals*, Theorem 9.6 and Remark 9.7, pp.94--95 of the 2025 preprint. A tangent vector is represented by transition functions `1+epsilon f_ij` and connection forms `epsilon omega_i`, hence by the de Rham Cech cocycle `(f_ij,omega_i)`.

The symbolic p-power construction of SGA 3 VII_A, 6.2--6.3 tensors p copies of this infinitesimal point, with independent square-zero parameters `epsilon_1,...,epsilon_p`, then sends the elementary symmetric functions `sigma_1,...,sigma_(p-1)` to zero and `sigma_p` to epsilon. The tensor product has transition functions `product_j(1+epsilon_j f_ij)=sum_r sigma_r f_ij^r`, and connection forms `sigma_1 omega_i`. The specified substitution therefore gives `(f_ij^p,0)`. This is exactly de Rham Frobenius, as defined by Oda, Definition 5.3. It proves the claimed identification of restricted operations. Finally apply the equivalence of SGA 3 VII_A, 7.2--7.4 and 8.1 to recover the height-one group extension. QED.

**Scope.** This application is over a perfect field, where classical Dieudonne theory applies. It is not a reconstruction of an arbitrary W(k)-deformation or of an arbitrary integral theta trivialization from the bare mod-p restricted Lie algebra. The full p-divisible group, its deformation/filtration, and the integral function are additional data in the derivative estimate.

**Duality convention.** Oda Theorem 3.19, printed p.89, identifies Cartier duality with Dieudonne duality, interchanging F and V. In integral crystalline or ell-adic realizations the Poincare pairing is valued in `W(k)(-1)` or `Q_l(-1)`. Accordingly `H^1(B) ~= H^1(A)^vee(-1)` as realizations. The plain underlying de Rham vector-space duality of scan 3 does not require adding a Tate twist to the manuscript transcription.

### Cote 4: what is relevant, and what the local bound does not settle

- Scan 3, equation (8.1.1), asks for **derived** crystalline--de Rham base change. The corresponding universal-coefficient sequence (8.1.2) has the Tor term in `H^(i+1)_crys`. This is the correct framework for integral lattices; passing only to rational F-isocrystals loses this torsion.
- Scans 5--6, 8.4.2 and Lemma 8.4.3, extract the Frobenius-bijective stable part. The exact functor `V |-> V_ss` on finite-dimensional semilinear spaces over a perfect field and the fact that Frobenius acts by zero on positive-degree differential forms prove the stable-part identification with `H^i(X,O_X)`. The supplied proof is mathematically sound as stated for proper schemes of finite type for which these finite-dimensional cohomology groups are being used.
- Scan 7, (8.5.1)--(8.5.5), retains the corrected p-torsion term. The text visibly deletes an earlier formula involving another w. One must not revive deleted formulas from earlier scans as settled assertions.
- Scans 9--10, 8.5.9, pass to etale F_p local systems in a family. Scan 12, 8.6, asks irreducibility/full monodromy and resulting point-count congruences. A derivative estimate on one formal summand does not furnish such a local system, compute its monodromy, prove an integral weak Lefschetz theorem, or prove a motivic-level assertion.

The comparison and crystalline formalism were established independently of Alpoge: Berthelot, *Cohomologie cristalline*, LNM 407, V.3.6 (derived perfect-crystal/base-change statement as identified by Illusie); Oda Corollary 5.11 for degree-one abelian comparison; Mazur--Messing for the integral Dieudonne comparison. Illusie's primary historical exposition *Grothendieck at Pisa*, section 3.2, author-PDF pp.9--11, gives the exact locators and explains the necessary correction from the initial infinitesimal site to PD thickenings. His section 4.2(iv), author-PDF pp.16--17, discusses the universal extension and Messing's construction of the Dieudonne crystal.

### ABA-7. What "divided powers" does and does not say here (checked obstruction)

EGA IV_4, Theorem 16.11.2, printed p.54, constructs the coordinate operators `partial^[n]` with `partial^[m] partial^[n] = binom(m+n,m) partial^[m+n]`. This integral coordinate calculus and the associated graded distribution algebra are a valid Grothendieck framework for the parent's formal-group calculation. They do **not** imply that the powers of a given invariant vector field divided by n! preserve the integral ring.

For a torsion-free ring R in which p is not a unit, `(t)` in `R[[t]]` cannot have divided powers: the PD identity `p! gamma_p(t)=t^p` would force the coefficient of t^p in gamma_p(t) to be `1/p!`, which is not in R. One instead passes to a PD envelope. Likewise a scalar valuation estimate on Taylor coefficients is not the datum of a crystal. A crystal requires compatible pullback identifications on a PD site (or, in a smooth coordinate presentation, an integrable topologically quasi-nilpotent connection with the required compatibilities).

Exact modern reference: Stacks Project, Proposition 60.17.4, tag 07JH, and its precise hypotheses in Section 60.17, tag 07J7. Illusie, section 3.2, p.11, distinguishes `gr(Diff)` (a divided-power algebra) from `gr(PD-Diff)` (an ordinary polynomial algebra). The presence of the word "PD" in the second name should not cause these two algebras to be interchanged.

## 3. Suggestion 9: precise affirmative statement and limits

### Existing results with exact locators

Borger's supplied source *Lambda-rings and the field with one element* defines the lambda-space formalism in section 1.1 ("General Lambda-spaces") and the point in section 2.1. Its introduction and section 1.1 identify a lambda-structure on a Z-flat scheme with commuting Frobenius lifts. The supplied source does not state the subsequent integral homotopy theorem.

Elliott, *Binomial rings, integer-valued polynomials, and lambda-rings*, J. Pure Appl. Algebra 207 (2006), 165--185, Theorem 4.1, characterizes torsion-free binomial rings by the Fermat congruences `a^p=a (mod p)` for all primes. Proposition 8.3 proves that a lambda-ring with all Adams operations identity is binomial (including automatic torsion-freeness). The free binomial ring on one generator is `Int(Z)`; see Proposition 2.1 and Lemma 2.2. Theorem 4.1 and Lemma 2.2 are explicitly cross-confirmed in Horel, Remark 1.3 and Proposition 2.2. The free-ring assertion is also stated in Elliott's own *Birings and plethories of integer-valued polynomials*, Actes des rencontres du CIRM 2, no.2 (2010), 53--58, opening discussion on p.53; Proposition 1 there concerns the right adjoint represented by `Int(Z)`. The full proof of Elliott 2006 was not independently audited in this agent run; do not label it as such. An elementary proof of the torsion-free Fermat criterion is supplied next.

Horel, *Binomial rings and homotopy theory*, J. reine angew. Math. 813 (2024), 283--305: Theorem 3.7 constructs the model structure on cosimplicial binomial rings; Theorem 5.4 recovers connected nilpotent finite-type spaces; Theorem 6.1 identifies Bousfield--Kan Z-completion for connected finite-type spaces; Proposition 8.1 and Notation 8.4 give binomial affine homotopy types. The author PDF has these on pp.7,13,13--15,17--19 respectively.

Earlier, Ekedahl, *On minimal models in integral homotopy theory*, Homology, Homotopy and Applications 4, no.2 (2002), 191--218, Theorem 2.9, constructed minimal special numerical models of connected nilpotent finite-type spaces. Lemma 2.8 identifies maps up to numerical homotopy with maps up to ordinary homotopy for the stated numerical spaces; Proposition 2.2 and Corollary 2.3 relate numerical spaces to cosimplicial numerical-polynomial rings. These exact statements were inspected in arXiv:math/0107004v2, pp.3,6--7. Horel's introduction, p.2, explains his debt to this work but does not claim an exact comparison theorem between the two constructions. Horel's Theorem 5.4 is the direct locator for the derived binomial-cochain assertion used here.

### ABA-3. Explicit binomial lambda-structure (checked elementary form)

**Statement.** If R is a torsion-free commutative ring, the following data are equivalent: a binomial-ring structure, and a special lambda-ring structure with every Adams operation the identity. When either exists it is unique, with `lambda^n(a)=binom(a,n)` and `lambda_t(a)=(1+t)^a`. A ring map between two binomial rings automatically respects the operations. Equivalently, by Elliott Theorem 4.1, `a^p-a in pR` for every a and every prime p.

**Proof of the Fermat criterion.** Write `P_n(X)=product_(i=0)^(n-1)(X-i)`. If R is binomial, then `P_p(a)=p! binom(a,p)` lies in pR. The polynomial identity `P_p(X)=X^p-X` modulo p implies `a^p-a in pR`.

Conversely assume all Fermat congruences. Fix n, a prime p, and `e=v_p(n!)`. For each maximal ideal m containing p, the local ring `S=R_m/pR_m` satisfies `z^p=z`. In any such nonzero local ring a nonunit z satisfies `z(1-z^(p-1))=0`, and the second factor is a unit; hence z=0. Thus S is a field. Since every element is a root of `X^p-X`, this field is exactly `F_p`. Starting with any `a in R_m`, choose its residue digit in `{0,...,p-1}`, divide the difference by p in `R_m`, and repeat e times. This constructs an integer b with `a-b in p^e R_m`. Consequently `P_n(a)-P_n(b) in p^e R_m`, while `P_n(b)` is divisible by n! in Z (including negative b). Therefore `P_n(a) in p^e R_m`. At maximal ideals not containing p the same membership is automatic because p is a unit. Ideal membership can be checked after localization at all maximal ideals, so `P_n(a) in p^e R`. Doing this for every prime dividing n! and using the pairwise comaximality of their powers gives `P_n(a) in n!R`. Torsion-freeness makes the quotient unique and identifies it with `binom(a,n)` in `R_Q`. This proves the criterion without a p-adic completeness or noetherian hypothesis.

**Proof of the lambda assertions in this torsion-free form.** Embed R in `R_Q`. In a special lambda-ring Newton's formula is

`d/dt log(lambda_t(a)) = sum_(m>=1) (-1)^(m-1) psi^m(a) t^(m-1)`.

If all Adams operations are identity, the right-hand side is `a/(1+t)`. With constant term one, the unique solution in `R_Q[[t]]` is `(1+t)^a`; hence its coefficients are the binomial polynomials and already lie in R. Conversely, if these polynomials lie in R, the formal series `(1+t)^a` obeys the special lambda identities: after embedding in `R_Q`, each identity is a rational polynomial identity in finitely many scalar variables; it holds for all nonnegative integer values, where it is the identity for ranks of exterior powers, and hence holds identically. Newton's formula gives `psi^m=id`. Uniqueness follows from the same formula. If `f:R->S` is a ring map and both are binomial, multiply `f(binom(a,n))` and `binom(f(a),n)` by n!; the results agree, so torsion-freeness of S proves equality. QED.

One must distinguish **identity Frobenius lifts on a torsion-free ring** from the mere congruences on a torsion ring. `F_p` satisfies the latter (the other primes are units), but is not a binomial ring in the torsion-free sense. The lambda-ring theorem includes all lambda identities, which are strictly more than specifying the residue congruences without flatness.

### ABA-4. Integer finite differences and the divided-power associated graded (checked)

**Statement.** Let `B=Int(Z)={f in Q[x] : f(Z) subset Z}` with its degree filtration `B_(<=n)`. Put `b_n(x)=binom(x,n)`. Then

1. `B_(<=n)=direct_sum_(i=0)^n Z b_i`.
2. `gr B ~= Gamma_Z(u)` as graded Hopf algebras, sending the symbol of b_n to `u^[n]`.
3. `Delta f(x)=f(x+1)-f(x)` preserves B and `Delta b_n=b_(n-1)` (with `b_(-1)=0`).
4. Ordinary differentiation does not preserve B: `d b_2/dx=x-1/2` is not integer-valued.
5. The binomial Frobenius lift `psi^p=id` gives the arithmetic p-derivation `delta_p(a)=(a-a^p)/p`, but this is not an ordinary derivation.

**Proof.** The Newton interpolation formula expresses a rational polynomial f of degree at most n as `sum_(i=0)^n (Delta^i f)(0) b_i`. This is checked by evaluating at the integers 0,...,n, where its coefficient matrix is triangular with diagonal one, or inductively using `Delta b_i=b_(i-1)`. If f is integer-valued, every coefficient `(Delta^i f)(0)` is an integer. Conversely each b_i is integer-valued on Z, including negative integers via `binom(-m,i)=(-1)^i binom(m+i-1,i)`. This proves (1) and (3).

The product `b_m b_n` has degree m+n and leading coefficient `1/(m! n!)`. Therefore its expansion in the integral basis from (1) has top coefficient `binom(m+n,m)`. This gives the divided-power multiplication on gr B, with a free rank-one summand in each degree, proving the algebra isomorphism in (2). Vandermonde's polynomial identity gives the coproduct

`b_n(x+y)=sum_(i+j=n) b_i(x)b_j(y)`.

It agrees with the coproduct on `Gamma_Z(u)`, and the counit is evaluation at zero. Substitution `x |-> -x` preserves B and induces the antipode `u^[n] |-> (-1)^n u^[n]` on the associated graded, proving the Hopf assertion. Claim (4) follows by evaluating the derivative at zero.

For (5), Elliott's Fermat congruences ensure `delta_p(a)` lies in R for any binomial ring R, and torsion-freeness makes it unique. Direct expansion gives

`delta_p(a+b)=delta_p(a)+delta_p(b)+(a^p+b^p-(a+b)^p)/p`,

`delta_p(ab)=a^p delta_p(b)+b^p delta_p(a)+p delta_p(a)delta_p(b)`.

These are the p-derivation identities. For example `delta_p(p)=1-p^(p-1)` is nonzero, whereas every ordinary derivation kills every integer. Thus it is a distinct arithmetic operation. QED.

The bridge in (2) is exact, but it is an associated-graded bridge, not an isomorphism of the filtered multiplication with the ordinary divided-power multiplication before passing to gr.

### ABA-5. Cosimplicial binomial cochains recover integral homotopy types (checked application)

**Statement.** For any simplicial set X the cosimplicial ring `A_X^n=Map(X_n,Z)` has a canonical degreewise special lambda-structure with `psi^p=id`. Its normalized additive cochain complex is integral simplicial cochains. If X is connected, nilpotent, and of finite type, the evaluation map

`X -> RMap_cBRing(A_X,Z)`

is a weak equivalence; hence for such X,Y,

`Map(X,Y) ~= RMap_cBRing(A_Y,A_X)`.

**Proof.** Every `A_X^n` is a product of copies of Z. Apply binomial coefficients pointwise. Pullback of functions along each simplicial operator preserves these operations, so the rings form a cosimplicial binomial ring. Its additive normalization is precisely the standard complex of integer-valued normalized simplicial cochains, by the definitions of cofaces and degeneracies. Horel Theorems 3.7 and 5.4 apply to this object and give the claimed unit equivalence. The mapping-space assertion follows by the derived adjunction `X |-> A_X` to derived maps into Z, followed by the unit equivalence for Y. QED.

**Boundary of the claim.** This is not the assertion that the cup-product differential graded algebra is a strictly commutative ordinary binomial ring. The cosimplicial structure and its derived mapping spaces are essential. For a merely connected finite-type X, the same unit is Z-completion, by Horel Theorem 6.1; it need not be an equivalence without the nilpotence condition. No statement about arbitrary spaces or arbitrary integral cohomology rings is being made.

### ABA-6. The homotopy statement does not imply the formal-group multiplicity bound (checked countermodels to the naive identifications)

**Statement.** The following identifications are false: (i) a formal disc over Z_p automatically is a binomial scheme with identity Frobenius lifts; (ii) the binomial operations on numerical polynomials give integral ordinary derivatives; (iii) the zero p-operation in cote 54 scan 7 characterizes supersingularity. Consequently these identifications cannot serve as a proof transferring the homotopy theorem to the derivative bound.

**Proof.** In `Z_p[[t]]`, the coefficient of t in `t^p-t` is -1, so `t^p-t` is not in `p Z_p[[t]]`. The identity is not a Frobenius lift, proving (i). Assertion (ii) is contradicted by ABA-4(4); (iii) is contradicted by ABA-1. These counterexamples refute the stated identifications. They do not prove that no richer comparison construction is possible; they prove that such a construction needs additional data and a theorem beyond Suggestion 9. QED.

## 4. Cotes 16 and 47, H8: scope and arithmetic checks

### ABA-8. Integral exterior divided powers do not imply integral hard Lefschetz (checked)

Cote 16 scan 14 constructs an integral exterior algebra and its Lefschetz operators. For a symplectic basis write `xi=sum e_i wedge f_i`; because the degree-two summands commute and square to zero,

`xi^m/m! = sum_(|S|=m) product_(i in S) (e_i wedge f_i)`

is integral. This is a different concrete divided-power calculation from the height-dependent formal-group estimate. Its existence alone does not imply integral hard Lefschetz isomorphisms: for n=3 on the span of the three `e_i wedge f_i`, multiplication by xi has, against complementary two-element subsets, matrix `J-I`, whose determinant is 2. This is a direct block of `L:Lambda^2 M -> Lambda^4 M`: no other exterior basis monomial can contribute to a monomial made of two complete pairs. Thus L is not an integral isomorphism, although it is a rational one. This agrees with the smallest test in H8. It does not prove H8(iv)'s assertion about the index of an integral order, or identify step-8 theta lifts with Lefschetz strings. Those are separate claims, not consequences of the local formal-group bound.

Cote 47 scan 9 asks about the Fourier transform of a line bundle at the K-theory level, and writes rational Chern character and total Chern-class formulas. Its total-Chern expansion has forced algebraic coefficient inconsistencies listed below. Even after correcting them, the rational formulas and a conjecture of integral cycle divisibility cannot be promoted by the formal-group estimate; they live in Chow/K-theoretic realizations and require their own integral correspondence arguments.

The cotes 133, 153, 136--137 and bridge B7 are mentioned in the supplied suggestions but their pages or precise B7 statement were not supplied. Do not invent scan locators, a statement of B7, or a claim that those archive questions are closed. The precise Horel/Int(Z) statements above support the proposed theme and identify exactly what is established.

**Later public-source follow-up (2026-11-21 UTC):** the preceding sentence describes the original supplied inputs. A bounded public-archive retrieval subsequently located the binomial operations in cote153 PDF page3/archive page2, and the rational-homotopy/PD motivation with extra base data in cote136 PDF pages4--6/archive pages3--5. See `public_archive_q5e_sources.md` and event ABA-CE21 for exact scope, source images and remaining limits. Public originals for cotes47 and54 were also retrieved by the parent and visually checked; the five correction candidates must now be classified as mathematical emendations of faithful or qualified diplomatic readings, not established transcription errors. See `transcription_public_visual_check.md` and ABA-CE20. Earlier no-pixels check events remain truthful historical records.

## 5. Candidate transcription corrections

No original manuscript pixels were present in the ZIP. The following are mathematical requirements/candidates for second-pass comparison, **not certified readings of unseen scans**. A mathematical inconsistency may come from Grothendieck's own draft or from transcription; it does not distinguish those causes.

| cote | scan | locator in supplied text | record | mathematically required | reason | confidence |
|---|---|---|---|---|---|---|
|54|005|first displayed duality|`H^q(B,Omega_A^p)`|`H^q(B,Omega_B^p)`|The differential sheaf must be on B; the next sentence identifies `H^0(B,Omega_B^1)` and the exterior-algebra duality.|Certain type correction; no pixel check.|
|54|007|top Frobenius--Verschiebung diagram, upper right object|`V` as possible reading in `unsure{V|A}`|`A`|The arrows are `A --F--> A^(p) --V--> A`; V is the arrow, not its codomain.|Certain mathematical reading; no pixel check.|
|47|009|quadratic term of ct expansion|`chi(chi-1)/(2chi) D'^2`|`chi(chi-1)/(2chi^2) D'^2`|Expansion of `(1-D'/chi)^chi`; equivalently coefficient `(chi-1)/(2chi)`.|Certain coefficient correction conditional on displayed generating formula; manuscript/transcription cause unknown.|
|47|009|cubic term of ct expansion|`chi(chi-1)(chi-2)/(3!chi^2) D'^3`|`chi(chi-1)(chi-2)/(3!chi^3) D'^3`|Same binomial expansion.|Same.|
|47|009|general degree-n ct coefficient|denominator `n!chi^(n-1)` with numerator beginning chi|denominator `n!chi^n` with that numerator|Same binomial expansion.|Same.|
|47|009|last displayed integrality coefficient|denominator `k!chi^(k-2)` after cancelling chi|No forced correction. Use `k!chi^(k-1)` only if the intended coefficient is exactly the kth Chern class.|The recorded unsigned expression is `(-1)^k chi c_k`, hence chi times the true kth Chern coefficient up to sign. It is still a valid, weaker integrality consequence when chi is integral.|Interpretive second-pass note only; not a mathematically forced correction.|

Do not put the boxed `t_A^vee` into this table as a transcription error: it is correct; the error is in the subsequent interpretation in Fable's suggestion.

## 6. Exact source URLs and inspection status

- Oda, primary paper: https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf . Inspected text of Theorem 1.1, Corollary 1.3, Theorem 3.19, definitions 5.3/5.6/5.8, and Corollary 5.11. Web refs `turn719472831view0`, `turn843316127view0`, `turn437518963view0`, `turn437518963view1`, `turn437518963view2`.
- SGA 3 VII_A, official Gille--Polo re-edition: https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp7A-13oct24.pdf and original-preserving version https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp7A.pdf . Inspected restricted Lie equivalence locators. Web refs `turn153557905view0`, `turn153557905view1`, `turn716981109view2`, `turn716981109view3`.
- EGA IV_4 original: https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf . Search returned exact Theorem 16.11.2 and formulas from printed p.54; direct open exceeded the tool's size limit. Web ref `turn920400821search4`. Independently cross-checked in Gieseker, *Flat vector bundles and the fundamental group in non-zero characteristics*, Proposition 0.2, https://www.numdam.org/item/ASNSP_1975_4_2_1_1_0.pdf (web ref `turn920400821view0`).
- Illusie, primary historical account: https://www.imo.universite-paris-saclay.fr/~luc.illusie/Illusie-Pisa5.pdf . Inspected section 3.2 and 4.2(iv). Web refs `turn478460392view1`, `turn395466598view2`, `turn153557905view3`.
- Horel, author PDF: https://geoffroy.horel.org/binomial.pdf ; DOI https://doi.org/10.1515/crelle-2024-0039 . Inspected definitions, model-structure statement, Theorems 5.4 and 6.1 and adjacent arguments. Web refs `turn651769823view0`, `turn396711068view1`, `turn396711068view2`, `turn396711068view4`.
- Elliott 2006: https://doi.org/10.1016/j.jpaa.2005.09.003 . Original abstract inspected; theorem numbers cross-confirmed from primary later papers, not a full proof audit. Elliott author survey https://www.numdam.org/item/10.5802/acirm.34.pdf .
- Elliott survey metadata and free-ring opening were directly checked at https://www.numdam.org/item/10.5802/acirm.34.pdf (web ref `turn255231880view0`); the correct pages are 53--58. Proposition 8.3 of Elliott 2006 is explicitly cited by Harman--Snowden, *Oligomorphic groups and tensor categories*, Theorem 5.12, https://link.springer.com/article/10.1007/s00222-026-01452-2 (web ref `turn849553071search1`).
- Ekedahl author preprint https://arxiv.org/pdf/math/0107004 . Inspected Proposition 2.2, Corollary 2.3, Lemma 2.8 and Theorem 2.9; web refs `turn174427788view0`, `turn622980917view0`, `turn622980917view2`. Published-paper metadata independently confirmed by the publisher scan search result `turn639473792search13`; the theorem locators quoted here were read in the preprint.
- Universal extension as line bundles with integrable connection: Mazur--Messing LNM 370 (1974), chapter I, as cross-confirmed in Oh--Shimizu, *Moduli stacks of crystals and isocrystals*, Theorem 9.6 and Remark 9.7, https://arxiv.org/pdf/2504.14801 . Inspected the theorem and exact original-source references, web refs `turn639473792view0`, `turn639473792view1`. The latter is a primary research preprint reporting the classical result, not a new result being attributed to 2025.
- Crystals/connection equivalence: https://stacks.math.columbia.edu/tag/07JH and https://stacks.math.columbia.edu/tag/07J7 . Inspected hypotheses and Proposition 60.17.4. Web refs `turn716981109view1`, `turn395466598view1`.
- Montpellier inventory: https://grothendieck.umontpellier.fr/archives-grothendieck/ . Used only to confirm the unrelated-verso warning; no manuscript-image claims. Web ref `turn852137828view0`.

The parent must open/search any web source itself before using its web citation in the user-facing chat. Ordinary bibliography URLs and exact mathematical locators in the paper are supplied above.

## 7. Check-event notes (agent-local; parent to merge)

Findings/application proofs ABA-1 through ABA-8 were read in full and checked by their author in this run. These are self-checks, not independent or formal verification. The detailed events are recorded in the neighboring file `archive_binomial_check_events.tsv`, with actual UTC times, client date, checker/model, scope, outcome and limitations. No Lean/formal verification or computer proof of these assertions has been run. A citation reading is not an independent re-proof of Oda, Horel, Ekedahl, Elliott, SGA 3 or crystalline comparison. Any subsequent independent parent check must be added as a separate actual event.



**Second public-source closure (2026-11-21 UTC):** exact official pixels now locate the remaining passages: cote133 PDF6/archive5 (binomial augmentation and the open λ-product/composition question), PDF27–29/archive26–28 (composition and λ/representation operations), and cote137 PDF38–39/archive37–38 (tensor/Γ cochain structures and the explicit homotopy-reconstruction question). See `public_archive_q5e_second_pass.md`, its pixel metadata and ABA-CE54–55. The historical source mapping is established; the precise B7 comparison remains unsupplied, and no theorem is invented from these questions.
