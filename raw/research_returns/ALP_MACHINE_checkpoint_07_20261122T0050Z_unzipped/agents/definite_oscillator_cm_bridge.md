# ALP_MACHINE — primitive CM reduced theta and the integral-frame boundary

Author: GPT-6 Astra Pro, `/root/definite_oscillator`, inherited effort not separately exposed, 21 November 2026 UTC. New consequences below are labelled AM-DO-011–016. Root's AM-R-004 and the supplied THETA3/DP_MULT results retain their own proof statuses. This note does not instantiate `PinX`, `ClsK.Core`, a primitive trace-one kernel, or the requested lift family.

## Literature actually read

Bannai, K., & Kobayashi, S. (2010). Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers. *Duke Mathematical Journal, 153*(2), 229–295. https://doi.org/10.1215/00127094-2010-024. The mathematical text read in this run is arXiv:math/0610163v4 (11 December 2007), https://arxiv.org/pdf/math/0610163, specifically Definition1.8 pp10–11; §2.1 and Proposition2.1 pp19–21; Theorem2.9 pp25–26; §2.3, condition(28), Lemma2.13 and Propositions2.14–2.15 pp27–29. Published bibliographic metadata was checked on Bannai's own publication page.

The used conclusions are: a reduced theta germ on a CM abelian variety has algebraic coefficients in algebraic eigen-differential coordinates, if its divisor and normalized leading value are algebraic and its line is admissible; prime-to-p torsion translations have an algebraic comparison; formal-parameter integrality requires the stated CM ordinarity condition and an arithmetic unit normalization. Those are cited theorems, not new theorems rederived in this run.

The supplied THETA3 C11 already provides an actual reduced-theta counterexample to automatic integral formal coefficients, and C19 treats integral de Rham CM splittings and derivative estimates. They are carried, not re-proved. In particular C11's y²=x³−x example at good supersingular p=7 has normalized reduced theta coefficient1411/2016 at formal degree9, of valuation−1. This is a concrete warning against promoting a generic algebraic/Chern comparison to an integral one.

## AM-DO-011. The exact R004 completion is a reduced theta, with algebraic coefficients

Carry AM-R-004's actual Jacobian J of y²=x⁷−1, E=Q(ζ7), Φ={1,2,3}, algebraic differential coordinates u_i=∫ω_i, u=Pz, normalized period matrix τ, and Y=Imτ. For κ≥1 write

    θκ(z)=Σ_(n∈Z³) exp(πiκ nᵗτn+2πiκ nᵗz),
    Fκ(u)=exp(πκ zᵗY⁻¹z/2) θκ(z)/θκ(0).

The carried quantitative result gives θκ(0)≠0. Define

    Hκ(z,w)=κ zᵗY⁻¹ conjugate(w),
    ακ(a+τb)=(−1)^(κ aᵗb),  a,b∈Z³.

Then Fκ is exactly the reduced theta function for the Appell–Humbert data(Hκ,ακ), normalized to value1 at0. It is not merely proportional to an unspecified reduced theta after an omitted quadratic exponential.

### Full calculation of the multiplier

Direct reindexing gives

    θκ(z+a+τb)/θκ(z)
      =exp(−πiκ bᵗτb−2πiκ bᵗz).

For λ=a+τb, multiplication by the completion factor changes the linear coefficient in z to

    πκ zᵗ(Y⁻¹λ−2ib)=πκ zᵗY⁻¹ conjugate(λ)=πHκ(z,λ).

The difference between the resulting constant term and πHκ(λ,λ)/2 is

    (πκ/2)λᵗY⁻¹(λ−conjugate(λ))−πiκ bᵗτb
       =πiκ λᵗb−πiκ bᵗτb=πiκ aᵗb.

Therefore

    Fκ(u+Pλ)=ακ(λ) exp(πHκ(z,λ)+πHκ(λ,λ)/2) Fκ(u),

which is precisely Bannai–Kobayashi Definition1.8. Since ακ²=1, its semicharacter meets their finite-order hypothesis. The completion's constant is1 at the origin, so its value normalization is the stated one. This proves the assertion. ∎

### Admissibility and algebraicity

In the first-argument-linear Appell–Humbert convention used here, Im Hκ is minus κ times the R004 alternating form

    E_R4(x,y)=Tr_(E/Q)((ζ−ζ⁻¹)x conjugate(y)/7).

The sign can be checked on the symplectic periods: Im Hκ(a_i,b_j)=−κδ_ij, while E_R4(a_i,b_j)=δ_ij. The sign convention has no effect on admissibility. For every a∈E, direct substitution gives E_R4(ax,y)=E_R4(x,conjugate(a)y), and therefore the same equality for Im Hκ. This verifies Φ-admissibility in the exact sense of Bannai–Kobayashi §2.1. Its algebraic invariant differentials are the specified ω_i=x^(i−1)dx/y, and the CM action x↦ζx is defined over E.

For κ=1 the associated symmetric theta line and its divisor are defined over E: AM-DO-012 below identifies every possible symmetric representative with one of the E-rational hyperelliptic theta characteristics. With F1(0)=1, Proposition2.1 applies directly and gives

    F1(u1,u2,u3) ∈ E[[u1,u2,u3]].               (DO11.1)

Here the conclusion concerns the coefficients in the algebraic differential coordinates u, including the ordinary factorial denominators inherent in a Taylor expansion. It does not identify the theta-null period θ1(0) itself as algebraic.

For κ>1 one must also descend the selected section line, since an arbitrary complex section of L^κ need not be algebraic up to scalar. In this case the descent is explicit. Let Hκ⊂J[κ] be the subgroup represented by (κ⁻¹Z³)/Z³. Translation z↦z+a/κ fixes θκ. These translations have commuting finite-order lifts to the theta group of L^κ, and the corresponding joint character space in H⁰(J,L^κ) has dimension1. For example the usual κ³ theta-series basis has joint eigencharacters indexed by j∈(Z/κZ)³, and θκ is its j=0 vector. Choose the matching algebraic lifts after a finite torsion-field extension. Such lifts are algebraic: starting from any algebraic isomorphism for a torsion translation, requiring its finite power to equal1 only adjoins a root of an algebraic number; the remaining exact finite commutator relations are the same finite theta-group relations. The chosen simultaneous eigenspace is the kernel of algebraic linear operators and hence is an algebraic line. Its divisor is therefore defined over a finite number field Kκ. Proposition2.1 gives Fκ∈Kκ[[u]]. This argument gives a finite descent for each κ, not a level-uniform field-degree or coefficient-height bound.

## AM-DO-012. A nonzero even theta value is a unit at every good prime for this Jacobian

Work over R=Z[ζ7,1/14], with the smooth projective hyperelliptic curve C:y²=x⁷−1. Let W_j=(ζ^j,0), j=0,…,6, and let ∞ be its unique point at infinity. The branch sections are pairwise disjoint over R because only7 ramifies in their differences, and2 is inverted. The standard relative hyperelliptic model is smooth and proper over R. For a subset S of the seven finite branch points with s=|S|≤3, put

    D_S=Σ_(j∈S) W_j+(2−s)∞.

Every geometric fiber has the following exact theta-characteristic classification and cohomology:

    S=∅:             h⁰(O(D_S))=2,
    |S|=1 or2:       h⁰(O(D_S))=1,
    |S|=3:           h⁰(O(D_S))=0.              (DO12.1)

There are1+7+21+35=64 such characteristics, and they exhaust all of them. In particular the35 non-effective characteristics remain non-effective in every residue characteristic other than2 and7.

### Full proof of the classification and cohomology calculation

The differential dx/y has divisor4∞, so K_C∼4∞. Also div(x−ζ^j)=2W_j−2∞. Hence2D_S∼4∞ and every D_S is a theta characteristic.

For distinct S,T with cardinalities at most3, the difference of their associated two-torsion points is represented, using2(W_j−∞)∼0, by

    Σ_(j∈S△T) W_j−|S△T|∞.

Suppose this is principal for a nonempty U=S△T of size at most6. Its divisor is invariant under the hyperelliptic involution ι. If f has that divisor, then ι(f)/f is constant and its square is1. Since the characteristic differs from2, either f∈k(x) or f=y r(x) with r∈k(x). A rational function in x has even order at every branch point, contradicting the required order1 at j∈U. A function y r(x) has odd order at every one of the seven finite branch points, contradicting the required order0 at a point outside U. Thus all64 points are distinct. A genus-three Jacobian has64 geometric two-torsion points in characteristic different from2, and the theta characteristics form their torsor by addition to2∞; the list is complete.

Now compute H⁰(O(D_S)) directly. The space is stable under ι, so every permitted function decomposes into its even and odd parts f=u(x)+y v(x), each still permitted. The even part has no finite poles, since a pole at W_j would have even order at least2 while D_S permits only1. Thus u is a polynomial. Its pole order2deg u at∞ must be at most2−s. This gives dimension2 when s=0, dimension1 when s=1 or2, and dimension0 when s=3.

For the odd part all finite poles must occur among S, and each possible denominator x−ζ^j occurs to exponent at most1. Therefore

    y v(x)=y Q(x)/∏_(j∈S)(x−ζ^j)

for a polynomial Q, unless the odd part is zero. Its order at∞ is2s−7−2deg Q. To be a section of O(D_S), this order must be at least s−2. It would follow that2deg Q≤s−5, impossible for s≤3. The odd part is therefore zero. This proves(DO12.1) over every indicated geometric fiber. ∎

### The actual algebraic unit rigidification

For |S|=3, Riemann–Roch gives h¹(O(D_S))=0 too, because deg D_S=g−1=2 and h⁰=0. There is an actual relative theta section on the Jacobian attached to D_S, and its value at the identity is a unit over R. One can see the unit without choosing a transcendental theta null.

Let p:C×_R J→J, let P be the rigidified Poincaré line on C×J, and let M=P⊗pr_C^*O(D_S). Take the effective divisor B=6∞. The line M(B) has fiber degree8, hence H¹=0 on every fiber. Thus p_*M(B) and p_*(M(B)|_B) are locally free of the same rank6, and the determinant of their restriction map is the usual determinant-of-cohomology theta section. At the identity, its kernel and cokernel are H⁰(O(D_S)) and H¹(O(D_S)), both zero on every fiber. The restriction map there is an isomorphism. Its determinant is therefore a unit and supplies the canonical rigidification of the theta line at0 in which the section has value1. This constructs the integral section and its unit value; no assertion that a Chern formal trivialization is integral has been used.

The symmetric principal theta line in R004 must correspond to one of these theta characteristics. Its theta value at0 is nonzero, by R004's exact estimate, so its characteristic has h⁰=0 and therefore belongs to the35 triples. It can consequently be modeled by the corresponding D_S over R with this unit rigidification. An explicit S is unnecessary for the conclusion, although it can be recovered from the finite level-two theta characteristic. The isomorphism to the complex R004 representative is fixed by the principal polarization and the rigidification; the resulting normalized reduced germ remains exactly F1.

### Explicit branch half-period data in the R004 basis

This calculation makes the finite level-two comparison concrete. Use root's basis a0=γ0,a1=γ2,a2=γ4 and b0=γ1+γ3+γ5,b1=γ3+γ5,b2=γ5. Then the branch points have the following half-periods, with a point denoted(ε;δ) when its z coordinate is(ε+τδ)/2:

| Point | ε | δ |
|---|---|---|
| W0 | 000 | 100 |
| W1 | 100 | 100 |
| W2 | 100 | 010 |
| W3 | 110 | 010 |
| W4 | 110 | 001 |
| W5 | 111 | 001 |
| W6 | 111 | 000 |
| ∞ | 000 | 000 |

To prove the first row, integrate on the real path∞→W0 with y=√(x⁷−1):

    ∫∞^W0 ω_i=−B(1/2−i/7,1/2)/7.

The gamma reflection identities give

    B(1/2−t,1/2)/B(t,1/2)=tan(πt).

Divide by root's c_i=−2i_C B(i/7,1/2)(ζ^i−1)/7. The quotient is−1/[2(1+ζ^i)]=(ζ^i+ζ^{3i}+ζ^{5i})/2, using(1+ζ)^(−1)=−ζ−ζ³−ζ⁵. Thus AJ(W0−∞)=b0/2. The identity AJ(Wj−W0)=½Σ_(k<j)γ_k follows by taking half the difference of the two sheet-symmetric branch paths λ_j−λ_0. Expanding γ0=a0, γ1=b0−b1, γ2=a1, γ3=b1−b2, γ4=a2, γ5=b2 modulo2 gives every row. This proves the table. No unverified Riemann-constant convention is used to name the triple S of θ[0;0].

## AM-DO-013. An actual pullback family with fixed normalization and ordinary integrality

Let L,s be the integral symmetric theta line and unit-rigidified section from AM-DO-012 matching F1. For every M≥1, the section [M]^*s lives in [M]^*L≃L^(M²), using the rigidified symmetric theorem-of-the-cube isomorphism. Its exact normalized reduced germ is

    G_M(u)=F1(Mu).                              (DO13.1)

It has value1 at0, lies in E[[u]], and satisfies

    M^(−|α|) ∂^α G_M(0)=∂^α F1(0).             (DO13.2)

From AM-R-004's bound at κ=1 one therefore obtains

    |G_M(u)|<49 exp((πM²/2)Σ_i |u_i|²/G_i),

and exactly the same level-normalized derivative bound as R4.11. This is a different actual section family from θ_(M²)(z); the equality(DO13.2) states its chosen normalization and makes no claim that it equals a primitive trace-one kernel.

Proof. Pullback along[M] acts on the universal cover by u↦Mu. Its Appell–Humbert Hermitian form is M²H1, and its semicharacter is α1(Mλ)=α1(λ)^(M²), so the reduced multiplier is that of the specified symmetric tensor power. The germ is therefore the displayed pullback, with no additional nonconstant factor; the value normalization fixes the constant. The chain rule proves(DO13.2), and substitution in the carried κ=1 estimate proves the bound. ∎

At a good prime p≠2,7 satisfying Bannai–Kobayashi condition(28), let λ(t) be the formal logarithm in an integral parameter system. The section's arithmetic divisor avoids0, and its normalized value is1. Proposition2.14, applied with local defining function f=1, gives

    F1(λ(t)) ∈ O_v[[t1,t2,t3]]^×.              (DO13.3)

For all M, the formal multiplication map[M](t) has integral coefficients, including when p divides M. Since λ([M](t))=Mλ(t), composition gives

    G_M(λ(t))=F1(λ([M](t)))∈O_v[[t]]^×.

Thus this family has exact uniform formal integrality at the stated ordinary primes. Prime-to-p torsion translations have the further explicit algebraic/integral comparison of Bannai–Kobayashi Theorem2.9 and Proposition2.15; their theta-group lifts, local divisor functions and torsion field are still part of the datum.

For the primitive type Φ={1,2,3} of Q(ζ7), condition(28) at an unramified rational prime is equivalent to p≡1(mod7). Indeed let D=<p>⊂(Z/7Z)^× be its decomposition group. The ideals occurring in Φ(p) and conjugate(Φ)(p) are disjoint exactly when ΦD and conjugate(Φ)D are disjoint. Since their union is the whole six-element group, this is equivalent to Φ being a union of D-cosets, or DΦ=Φ. Its stabilizer is trivial: multiplication by2 sends3 to6; by3 sends2 to6; by4 sends1 to4; by5 sends1 to5; by6 sends1 to6. Hence D={1}, equivalently p≡1(mod7). This calculation concerns the exact hypothesis of the cited theorem; it does not assert non-integrality at every other prime.

## AM-DO-014. What the CM Hodge splitting does and does not settle

Over a number field containing E and the endomorphisms, H¹_dR(J) is the sum of six one-dimensional E-eigenlines. Its Hodge subspace is the sum of the three Φ-eigenlines. The sum of the other three eigenlines is the unique E-stable complement. Indeed any other complement is the graph of an E-linear map from that sum to the Hodge subspace, and such a map is zero because their eigencharacters are disjoint. After base change to C the anti-holomorphic Hodge summand has precisely those complementary characters, so it is this same complement.

At a good prime not dividing7, after a finite base change splitting O_E⊗O_v, the same idempotents are integral, because the CM algebra is étale there. The Hodge subbundle is saturated in the de Rham lattice. Each of its eigenparts has either full rank1 or rank0, so saturation makes it respectively the entire eigenline lattice or zero. Thus the complementary sum gives an integral E-stable module splitting as well. These assertions prove the proposed comparison of the linear Hodge splittings.

They do not prove that the generic formal horizontal section of a connection, the formal exponential of a Lie splitting, or a chosen Chern/reduced theta frame is an integral formal object. The supplied C11 and C19 already establish this distinction for actual CM elliptic theta functions. It is therefore not enough to invoke uniqueness of the E-linear Hodge complement to discharge all integral-frame hypotheses of the mixed-type arithmetic constructor. The generic algebraicity needed here is independently justified by the exact reduced multiplier and Bannai–Kobayashi Proposition2.1; the ordinary integrality is the narrower result(DO13.3).

For the requested bridge to `I.J.V.thMoved` and `PinX`, the remaining tasks are exact and separate: identify the actual primitive/trace-one section and its fixed theta-group translates with this CM model; match the selected local coordinates, determinant roots, additive character and periods; establish the prescribed finite-place derivative or divided-power bounds for the tied family at the nonordinary primes actually used; and prove the all-polynomial kernel identity with the specified volumes and terminal rows. None is implied by a unit theta value at0 or by an algebraic normalized germ alone.

## AM-DO-015. The exact line-class and parity gate, and its torsion-translation repair

For this paragraph carry ALP-LIFT-07's identification of the R004 zero characteristic with D135=W1+W3+W5−∞ and of the trace-one line Lw0 with the unique ζ-invariant symmetric principal line L0 attached to2∞. Let t be their nonzero two-torsion displacement. In root's period coordinates it has

    t=(ε+τδ)/2,  ε=(1,0,1),  δ=(1,1,1).        (DO15.1)

Thus L1=L_D135=t_t^*L0 and t_t^*L1=L0. The source's actual arithmetic `Level` requires M odd: `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean`, lines53–62, field `odd`, line56. Its `SAB.prim`, line82, also fixes the trace-one line by the cube identity. The actual file was fetched and read in this run; this is not inferred only from the convenient example M=29^e.

Let N=L1⊗L0^(−1), a nontrivial element of Pic⁰(J)[2]. For every M,

    [M]^*N=N^M,
    [M]^*L1 ≃ L0^(M²) ⊗ N^M.                 (DO15.2)

Consequently the value-one pullback family F1(Mu) lies in L0^(M²) for even M, but remains in a different line for odd M. Theta-group actions on L0^(M²), including those in `IsVtOver`, preserve that line and cannot by themselves change its Pic⁰ class. Even M is therefore a valid geometric way to remove this particular twist, but it does not instantiate the current arithmetic `Level`.

Proof. Pullback by[M] on Pic⁰ is multiplication by M, so[M]^*N=N^M. The symmetric rigidified multiplication isomorphism gives[M]^*L0=L0^(M²). Their tensor product proves(DO15.2). As N has exact order2, N^M is trivial exactly for even M. A theta-group action is, by definition, an automorphism of sections of its specified line via an isomorphism of a translate of that same line. It does not identify two different Pic⁰ classes. This proves the stated obstruction to that direct substitution. ∎

### Repair by changing the base section to the actual trace-one line

There is a precise algebraic torsion translation that fixes the line issue without changing the odd arithmetic level. Let H(z,w)=zᵗY⁻¹ conjugate(w), Q(z)=πzᵗY⁻¹z/2, and write F1 also for its expression in z. Define the normalized reduced translation

    Σ(z)=exp(−πH(z,t)−πH(t,t)/2) F1(z+t).       (DO15.3)

This is Bannai–Kobayashi's U^M_t convention, equations(14) and following pp14–15. Since t_t^*L1=L0, it is a nonzero section of the actual trace-one line L0. It vanishes at0, with the expected effective even theta characteristic; it is not asserted to have value1 there.

Its exact theta-series formula is

    Σ(z)=−i · exp(Q(z))
          θ[δ/2; ε/2](z;τ) / θ[0;0](0;τ).    (DO15.4)

To check the constant, substitute t=(ε+τδ)/2. The linear part of Q(z+t)−πH(z,t)−Q(z) is πiδᵗz. Its constant part after subtracting πH(t,t)/2 is(πi/4)(δᵗτδ+εᵗδ). By the definition of a theta characteristic,

    θ[δ/2;ε/2](z;τ)
      =exp(πiδᵗτδ/4+πiδᵗz+πiδᵗε/2) θ(z+t;τ).

The quotient of these two exponentials is exp(−πiεᵗδ/4)=−i because εᵗδ=2. This proves(DO15.4), including its scalar.

Bannai–Kobayashi Theorem2.9 applies to this two-torsion translation and shows that the coefficients of Σ in the algebraic u=Pz coordinates are algebraic over E(J[16]); an extra root-of-unity convention for U_t rather than U^M_t changes only the stated finite torsion scalar. This is a generic algebraic statement. We do not infer that every coefficient, or its chosen integral-frame scalar, is a unit at a nonordinary prime.

The SAME Gaussian constant49 is preserved. Indeed R004 gives |F1(z+t)|<49 exp(πH(z+t,z+t)/2). Taking the absolute value of the exponential in(DO15.3) subtracts πReH(z,t)+πH(t,t)/2; the cross terms cancel exactly, leaving

    |Σ(u)|<49 exp((π/2)Σ_i |u_i|²/G_i).         (DO15.5)

For every allowed odd M=29^e from carried DP59, set Σ_M(u)=Σ(Mu). This is literally[M]^*Σ in L0^(M²). The standard rigidified multiplication isomorphism, with t′=t=0 and the identity theta action, verifies the generic `IsVtOver` clauses, exactly as in DP59(c). Its normalized derivatives satisfy

    M^(−|α|) ∂^αΣ_M(0)=∂^αΣ(0),

and the R004 level-independent Cauchy bound holds with the same49. This gives an actual algebraic base section, in the correct trace-one line, and an actual generic permitted pullback family. It still does not prove membership of the selected row in an iterated automorphic theta image, any prescribed nonzero positive-degree jet, or the global `PinX.mv` identity for every moved lattice.

## AM-DO-016. A literal finite Schwartz input and the retained CM period

The trace-one section in(DO15.4) has a concrete theta input. Fix the classical additive-character convention with ψ_∞(x)=exp(2πix), so ψ_f(r)=exp(−2πir) on rational r. Put α=δ/2 and β=ε/2, and define the finite Schwartz function on A_f³ by

    φ_t(q_f)=−i·1_(α+Zhat³)(q_f) ψ_f(−q_fᵗβ). (DO16.1)

This is locally constant and compactly supported. Its values on rational points q=n+α are−i exp(2πi(n+α)ᵗβ), hence algebraic fourth roots of unity. Its rational theta sum is exactly

    Σ_(q∈Q³) φ_t(q) exp(πi qᵗτq+2πi qᵗz)
       =−i θ[α;β](z;τ).                        (DO16.2)

Multiplying by the actual Chern completion gives

    exp(Q(z)) Θ(φ_t;z,τ)=θ[0;0](0;τ)·Σ(z).     (DO16.3)

All derivatives of(DO16.3) follow from normally convergent theta series. Thus in this explicit one-fiber Schrödinger/Chern convention the analytic-to-normalized-algebraic comparison constant is precisely

    c0=θ[0;0](0;τ),  |c0|>5/8.                (DO16.4)

It has not been set to1. The phase−i is part of the finite input, so no phase is omitted from c0. The finite input is a phase and a half-lattice translation of the standard input1_Zhat³, hence belongs to its finite Heisenberg orbit. It is supported in (1/2)Zhat³ and invariant under2Zhat³, so its finite Schrödinger support/period quotient is (1/2)Z³/2Z³. This is a modulus4 statement for the input function, not a claimed level4 stabilizer for the full metaplectic group action.

Proof. Compact support and local constancy follow from the coset of the compact open subgroup Zhat³ and the finite-conductor additive character. At a rational point the stated product formula for ψ gives its displayed value. Its support on Q³ is precisely α+Z³, so writing q=n+α identifies the sum term by term with the defining series for the theta characteristic. This proves(DO16.2), and substitution of(DO15.4) proves(DO16.3). The inequality in(DO16.4) is carried R004. ∎

This is a genuine fiberwise theta equality with an explicit finite input and an explicit retained period. It is more than an assertion of abstract nonvanishing. It is still less than the required common arithmetic `ClsK.Core` for the whole family. In particular the recovered Alpöge convention is `IsStdChar ψ (-1)`; a comparison with it must track the conjugate additive character and the associated polarization or coordinate convention. Nor have the other moved CM lattices, their covolumes, the fixed all-degree branching maps or the terminal mass matrix been identified by(DO16.3). A common scalar for one fixed Heisenberg module does not supply these further identities.
