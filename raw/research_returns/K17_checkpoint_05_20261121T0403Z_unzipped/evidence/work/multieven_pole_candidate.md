# Candidate generalization: cyclic even Iwasawa modules and higher poles

Historical candidate, 21 November 2026. **Subsequently passed two independent whole-proof audits and parent review.** The clean checked version is work/multieven_pole_proof.md. The candidate wording and audit stages below are retained for provenance. This note extends the checked one-even-generator argument at37. It does not yet change the main report's all-prime status. Researcher `/root/tripod_integral`, GPT-6 Astra Pro; effort not exposed.

## 1. Conditional arithmetic statement

Let p be an odd prime satisfying Vandiver. Put F=Q(mu_p), K=Q(mu_(p^infinity)), Omega=maximal pro-p extension of F unramified outside p, P=Gal(Omega/F), H=Gal(Omega/K), Gamma=Gal(K/F), and Lambda=Z_p[[Gamma]].

Assume that the cup product of the odd-character summand of H^1(P,F_p) with itself spans H^2(P,F_p). Equivalently, for every nonzero even relation character e, some coefficient of an odd–odd commutator [x_a,x_b] in its cup-normalized initial relator is nonzero modulo p. This condition does not require a chosen cyclotomic-unit basis. Under Vandiver, surjectivity of the cup pairing on all p-units implies this condition by the parity lemma in section6 below.

**Proposed deduction:** the tripod kernel field equals Omega.

There is no lambda=1 assumption and no assumption that the characteristic polynomials have distinct roots. The added work is a partial-fraction change of the degree-two Magnus letters, followed by extraction of a multi-Laurent coefficient. All scalar extensions occur in finite-dimensional letter spaces at a fixed source degree; bounded denominator control is retained.

## 2. Arithmetic structure of H_ab under Vandiver

Write M=H_ab and r=(p-1)/2. The already checked Iwasawa1981 theorem and Ferrero–Washington give that H is free pro-p. Hence M has no Z_p-torsion. Weak Leopoldt gives rank_Lambda M=r. Kummer duality makes M+ a torsion Lambda-module, and mu=0 makes it finitely generated over Z_p. Thus M+ is finite free over Z_p.

For clarity on this last implication, Sharifi's Kummer comparison identifies M+ up to finite kernel and cokernel with the involution/Tate twist of X_infinity−. Ferrero–Washington gives mu=0 for X_infinity−, making it finitely generated over Z_p. A finite kernel or cokernel preserves that finite generation; the absence of Z_p-torsion in M then makes M+ free of finite rank. This is not an assertion that Lambda-torsion is p-torsion.

The minimal generating set in McCallum–Sharifi §8 pp22–23, under Vandiver, has gamma, one x_a for each odd character a, and one y_e for each even character e in M_even. The split abelianization sequence

    0 -> M_Gamma -> P_ab -> Gamma ->0

and Nakayama show that M− has r minimal Lambda generators. Its Lambda rank is r, so the surjection Lambda^r->M− has zero kernel, as in the checked37 proof. More precisely each odd character component is free rank one:

    M− = direct sum_(a odd mod p−1) Lambda e_a.                    (G1)

Each even component T_e=M^(e) is a cyclic Lambda-module, finite free over Z_p. Let lambda_e=rank_Zp T_e>0, and choose a cyclic generator v_e. Let q_e(z) be the characteristic polynomial of gamma on T_e. Gamma acts through a finite p-group modulo p, so

    q_e(z) = (z−1)^(lambda_e) modulo p.                            (G2)

The vectors v_e,gamma v_e,...,gamma^(lambda_e−1)v_e form a Z_p-basis. Indeed Cayley–Hamilton makes their Z_p-span stable under gamma and gamma^(-1); gamma is a unit, so the constant coefficient of q_e is a unit. This finite generated span is compact and closed. It therefore contains the Lambda-span of v_e, which is T_e. A surjection from Z_p^(lambda_e) to the free module T_e of the same rank is an isomorphism.

Choose actual lifts x_a,y_e in H, and put

    y_(e,j)=gamma^j y_e gamma^(-j),   0<=j<lambda_e,
    x_(a,t)=gamma^t x_a gamma^(-t),  t in Z_p.

The compact generating-space/projectivity argument from the checked37 proof now gives a free compact basis of H consisting of all x_(a,t) and all isolated y_(e,j): its abelianization is exactly (G1) plus the finite bases of the T_e. Its universal free pro-p source maps onto H, has an isomorphism on abelianizations, and a projective section whose Frattini-surjective closed image is the whole source.

The lifts may be chosen as exact nonlinear Delta eigenlifts using Sharifi Lemma2.1 (galstr.pdf pp3–4), with gamma commuting with Delta. In particular

    delta x_a delta^(-1) = x_a^(omega(delta)^a),
    delta y_e delta^(-1) = y_e^(omega(delta)^e).

The Gamma conjugates y_(e,j) have the same exact eigenproperty. This choice preserves prescribed abelian eigenspace classes by the averaging construction, and unit adjustments preserve the Frattini classes relevant to the cup coefficients.

## 3. Companion errors and the exact unit numerator

Write

    q_e(z) = z^(lambda_e) − sum_(j=0)^(lambda_e−1) c_(e,j) z^j.

Choose the product in increasing j and define

    E_e = (gamma^(lambda_e) y_e gamma^(−lambda_e))
          (product_j y_(e,j)^(c_(e,j)))^(−1).

By the characteristic-polynomial identity in M, E_e belongs to the CLOSED commutator subgroup of H. Its quadratic Magnus coefficients in the odd orbit letters give measures and integral transforms C_(e;a,b)(T_1,T_2).

We need the precise consequence

    for each e, some C_(e;a_e,b_e)(0,0) is a p-adic unit.             (G3)

Here is a multi-relator justification, replacing the one-relator scalar argument used at37.

Let F_free be free pro-p on gamma,x_a,y_e (only j=0 among the even generators). Substitute the conjugate words gamma^j y_e gamma^(-j) for y_(e,j) and the compact orbit words for x_(a,t). The compact free universal property gives the required substitution for each E_e. The semidirect product P has one defining relator R_e per even e:

    R_e = gamma^(lambda_e) y_e gamma^(−lambda_e)
          (product_j y_(e,j)^(c_(e,j)))^(−1) E_e^(−1).

To verify this presentation, an assignment of gamma,x_a,y_e into a pro-p target satisfying all R_e determines images of every compact generator of H. Compatibility with gamma is automatic for the x orbits and for y_(e,j) when j<lambda_e−1; the last compatibility in each chain is exactly R_e. The map therefore extends to H semidirect Gamma. This proves the presentation by its universal property.

Let R be its closed relation subgroup. The exact nonlinear eigenlifts allow Delta to act on F_free by fixing gamma and sending x_a and y_e to their indicated unit powers. These are finite-order automorphisms of the free pro-p group. The quotient map to P is Delta-equivariant, so Delta preserves R.

Now abelianize the kernel of F_free->Gamma. Its free relative abelianization is

    A_free = direct sum_a Lambda X_a direct sum_e Lambda Y_e.

The image of R_e in A_free is EXACTLY q_e(gamma)Y_e: E_e is a closed commutator word in the compact H-basis and therefore has zero relative abelianization before passing to the arithmetic quotient. Consequently the image R_linear of R is

    R_linear = direct sum_e q_e(gamma) Lambda Y_e,                  (G4)

a free Lambda-module with one generator of Delta-character e for each e. Normal conjugation by gamma acts on A_free by gamma, and conjugation by the other generators acts trivially there, so (G4) indeed describes the entire closed image.

Linearization induces a surjection

    R / closure(R^p [R,F_free])
       -> R_linear/(p,T)R_linear.                                 (G5)

The source is generated by the classes of the #M_even defining relators; the target has that dimension. Thus (G5) is an isomorphism. It is Delta-equivariant, and the class of R_e has character e.

McCallum–Sharifi's cup-normalized character-e relation therefore has class equal to a nonzero scalar times R_e in (G5). All relators lie in the Frattini subgroup of F_free. Passing to descending p-central degree2 annihilates R^p and [R,F_free], so the same comparison holds for initial quadratic terms. The companion product itself involves only y_e and its gamma conjugates. Modulo degree3 it cannot contribute an odd–odd bracket [x_a,x_b]. The odd–odd coefficient of R_e is therefore minus the corresponding coefficient in the augmentation of E_e, namely minus C_(e;a,b)(0,0), up to the fixed commutator convention. The assumed nonzero cup coefficient proves (G3).

This uses only generation and equivariance of the relation-space quotient; it makes no claim that the full relation module is free or that the presentation is aspherical.

## 4. Target quadratic coefficients and partial fractions

Use the actual continuous dense rational tripod representation rho:H->U(Q_p), Hain–Matsumoto and Brown, with free odd target letters s_m. Make gamma lie in a Levi torus by the same positive-weight conjugation as in the checked37 proof. Delta then also acts by its weight characters. Normalize s_m weightwise so the linear coefficient of rho(x_(a,t))-1 is u^(mt) for matching m and zero otherwise. Each normalizing coefficient is nonzero by density. Each y_(e,j) has target length at least2 by parity.

For a target pair (m,n), put z=u^(m+n). Let B_(e,j;m,n) be the coefficient of s_m s_n in rho(y_(e,j))-1. The actual conjugate definition gives

    B_(e,j;m,n) = z^j B_(e,0;m,n).

Taking length2 in E_e gives

    q_e(z) B_(e,0;m,n)
        = C_(e;a,b)(u^m−1,u^n−1),    a=m mod(p−1), b=n mod(p−1).   (G6)

The leading length2 component of each y_(e,j) has Delta-character e. Hence the B coefficients vanish for a+b !=e modulo p−1. Equation(G6) then makes C_(e;a,b) vanish on the entire corresponding Cartesian weight grid; the successive analytic identity theorem forces C_(e;a,b)=0 as a power series. Thus wrong-character numerators vanish identically, and every unit pair in (G3) satisfies a_e+b_e=e.

To avoid every division at a zero denominator, let W be the finite set of positive integers w for which u^w is a root of some q_e. It is finite because u has infinite order. Restrict every test weight m to be larger than max(W union {0}). Then no pair sum m+n meets W. In each fixed odd residue class, the tails m=a+(p−1)p^n still have an interior accumulation point and suffice for every analytic identity used below.

Let L/Q_p be a finite extension splitting all q_e, and O_L its valuation ring with uniformizer pi. By (G2), every root alpha satisfies alpha−1 in the maximal ideal of O_L. Write its multiplicity as n_(e,alpha). The strictly proper rational functions

    z^j/q_e(z),  0<=j<lambda_e,

have the alternative L-basis

    1/(z−alpha)^k,
    alpha a root of q_e,  1<=k<=n_(e,alpha).

This is the ordinary partial-fraction decomposition, including repeated roots. Apply its constant invertible change of basis to the degree-two source Magnus LETTERS y_(e,j). This is not a change of actual pro-p generators or a claim that L-coefficients are integral. It is a linear change in a finite-dimensional subspace of the completed associative coefficient algebra over L. It preserves the first nonzero assigned degree, and at every fixed degree changes bounded O_L-valued measures only by a finite common denominator.

In the new formal letters Y_(e,alpha,k), the leading target kernel is

    C_(e;a,b)(T_1,T_2) / ((1+T_1)(1+T_2)−alpha)^k.                (G7)

All isolated even letters still have assigned degree2, all compact odd orbit letters degree1. The measure-valued Magnus embedding remains injective after this scalar extension and invertible degree-preserving linear change.

## 5. Colored pair tilings and multi-Laurent coefficients

Suppose g!=1 lies in ker rho and let d be its first nonzero assigned Magnus degree after the letter change. Its coefficients are bounded L-valued measures. A source word is again an ordered tiling of d positions into singleton odd letters and paired even letters, but now every pair is colored by (e,alpha,k).

For fixed target residue classes, its coefficient identity has the form

    sum_patterns A_pattern(T_i : singleton positions)
       product_pairs C_(e;a_j,a_(j+1))(T_j,T_(j+1)) / D_(j,alpha)^k =0,

where D_(j,alpha)=(1+T_j)(1+T_(j+1))−alpha. At a finite arithmetic weight cutoff, substitution and continuity are justified as in the checked37 proof. Clearing all denominators turns this into a bounded-coefficient analytic identity on the Cartesian odd-weight grid. The successive one-variable identity theorem, now over L, makes it an identity of power series. We work in

    R_L = O_L[[T_1,...,T_d]][1/pi],

not the ring allowing arbitrary unbounded L-coefficient denominators.

Choose a nonzero coefficient pattern with a maximum number of even letters. Fix its pair positions J and its (e,alpha) colors. Among the nonzero patterns with these positions and these colors choose a pole-order vector (k_j) that is maximal under the componentwise partial order. Such a vector exists because the set is finite. At each chosen pair assign target types (a_e,b_e) from (G3), and at each singleton assign its source orbit type. Every selected C numerator is then a unit.

Introduce independent variables

    S_j=D_(j,alpha_j),   j in J.

Because the pairs are disjoint and alpha_j−1 is topologically nilpotent, the substitutions

    T_(j+1) = (alpha_j+S_j)/(1+T_j)−1

give an isomorphism of formal O_L power-series rings. Retain as base variables all unpaired T_i and one left variable T_j from each pair. Let K_base be the fraction field of their bounded-denominator power-series ring. Our identity embeds into multivariate Laurent series over K_base in the S_j, with a finite lower bound on each exponent.

Why all the other denominators are analytic there:

- At the same pair position, a different root alpha' gives S_j+(alpha_j−alpha'), whose constant term is nonzero in K_base.
- At a different position, its two variables belong to different blocks of the chosen tiling. After S_j=0, the two remaining block variables are independent; their product is not identically the specified root. That constant term is again nonzero in K_base.
- A different even character at a selected position contributes zero for the assigned target types, because the sum of those types fixes e.

These denominators therefore have inverses in K_base[[S_j:j in J]]. They supply no negative S exponents. Every selected C numerator remains a nonzero unit after setting all S_j=0.

Extract the coefficient of

    product_(j in J) S_j^(−k_j).

A pattern missing a selected pair, or using a different root there, has pole order0 in that variable and cannot contribute. A pattern properly containing J has more even letters and its coefficient is zero by maximality. Among patterns with the same positions and root colors, an order vector k' can contribute only if k'_j>=k_j for every j, because all numerators and extra denominator inverses have nonnegative S exponents. The Pareto-maximal choice excludes every strict such vector. Hence only the selected pattern contributes.

Its contribution is

    A_pattern(unpaired variables)
      times product_(j in J) C_(e_j;a_ej,b_ej) evaluated at S=0.

It is nonzero: the unpaired-variable coefficient ring embeds in K_base, and every C factor is a unit. Contradiction. If there are no even pairs, the same argument is simply the ordinary odd-moment separation.

This establishes injectivity under the stated arithmetic cup hypothesis, subject to whole-proof audit.

## 6. Scope and source gate

The group-theoretic/analytic extension handles multiple even characters, nonsplit eigenvalues, and repeated roots. It does not require extra conjectures about simplicity of p-adic L-function zeros. The cyclic Lambda structure per even character is where Vandiver is used, together with the minimal arithmetic generator statement. If Vandiver fails, a matrix/noncyclic-module extension is not covered here.

The exact source is Sharifi, Iwasawa theory and the Eisenstein ideal, Duke137(2007), arXiv math/0501236v4: Theorem1.2 printed p2 and Corollary5.9 printed p27 prove surjectivity of the cup pairing on p-units for every odd p<1000. Theorem5.7 is the stated exact Magma modular-symbol computation used in this proof. It is cited, not rerun here.

**Parity bridge (root-owned proof independently read here).** Let E=O_F[1/p]^times/(O_F[1/p]^times)^p. For a p-unit v, v/c(v) is a global unit all of whose conjugates have absolute value1, and hence a root of unity. The elementary proof is that the monic polynomials of its positive powers have bounded degree and bounded integer coefficients; only finitely many roots occur, so two powers coincide. Thus E− is the one-dimensional space of mu_p. The Kummer sequence 0->E->H^1(P,mu_p)->A[p]->0 and Vandiver A+=0 give E+=H^1(P,mu_p)+. The Brauer term vanishes because F is totally imaginary with a single omitted finite prime, so H^2(P,mu_p^2)=A tensor mu_p is a plus space. Mixed parity cups vanish; E− wedge E− vanishes because E− is one-dimensional and p is odd. Consequently surjectivity on E cup E is precisely surjectivity on E+ cup E+. Untwist both inputs and the target to obtain surjectivity from H^1(P,F_p)− cup itself onto H^2(P,F_p). Minimal-presentation cup duality then supplies the unit odd–odd coefficient in every relation eigenspace. Character indices satisfy a+b=e modulo p−1: x_a has character omega^a, its Kummer dual omega^(1−a), and the relevant twisted target character is omega^(2−e).

Buhler–Harvey, Irregular primes to 163 million, arXiv0912.2121v2 p1, verifies Vandiver throughout all primes below163,577,356; in particular every odd prime below1000 meets it. This source was freshly opened as turn120784695view0. Combining that cited verification, Sharifi's theorem, the parity bridge, and the conditional pole theorem yields the proposed corollary

    Omega_p^*=Omega_p for every odd prime p<1000.

The all-odd-p<1000 corollary remains pending the whole-proof audits of this generalization. It does not rely on a computation of lambda-invariants or a simple-root assertion.

Primary inputs already used: Iwasawa1981 Theorem2 pp273–274; Sharifi Iwasawa notes Theorems3.3.3–3.3.4, Proposition3.4.7, Corollary3.4.8; McCallum–Sharifi pairing.pdf §8 pp22–23 and §9 pp24–25; Sharifi galstr.pdf Lemma2.1 pp3–4; Hain–Matsumoto actual-image comparison and Brown rational Deligne–Ihara with exact locators in the checked pro2 and37 notes.
