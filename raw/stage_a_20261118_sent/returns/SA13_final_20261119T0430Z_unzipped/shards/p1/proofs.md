# Independent mathematical checks: MPL 33:098–146

These are modern reconstructions of the supplied text. They do not settle uncertain handwriting. A proof here is independent only to the extent explicitly stated. `outputs/p1_computations.json` contains exact finite checks; finite enumeration never proves a statement for all rings, schemes, or primes. Bibliographic keys resolve in the consolidated bibliography.

## flat-adjunction

In the category of modules on a commutative ringed topos, tensor–internal-Hom adjunction gives
Hom(M, Hom(F,I)) = Hom(M tensor F,I). If tensoring by F is exact and I is injective, the right-hand side is exact contravariantly in M, so Hom(F,I) is injective. Conversely suppose this holds for every injective I. For a monomorphism M→N, the map Hom(N tensor F,I)→Hom(M tensor F,I) is onto for every injective I. Injectives cogenerate the abelian category, so M tensor F→N tensor F is monic. Tensor is already right exact, proving flatness. This uses global Hom to test injectivity; confusing it with internal exactness would leave a gap.

Enough flats follows from the usual site presentation by free modules on objects, extended by zero. Resolving successively and totalizing the resulting bounded-above double complex yields a flat resolution in D-minus. This is the standard site construction, not a new proof of its foundational existence. Pullback is scalar extension after inverse image; inverse image is exact on underlying sheaves, so pullback preserves flatness. Resolutions then give monoidality and composition of derived pullback. The elementary assertion that f_* sends injectives to injectives requires exactness of its left adjoint f^*. Without it the derived adjunction remains valid, but this shortcut does not.

## amplitudes

If an exact-left functor has right-derived functors only in degrees 0 through c, the hypercohomology spectral sequence has E2 terms R^pF(H^qK) with 0≤p≤c. For H^qK=0 outside [a,b], its abutment is zero outside [a,b+c]. For compact supports the checked bound is c=2d, giving cohomological interval [a,b+2d]. The manuscript's homological indexing reverses the endpoints: [N,M] becomes [N−2d,M]. This is the source of the apparent sign reversal on scans140–142.

For flat complexes with term intervals [a,b] and [c,d], total tensor has interval [a+c,b+d]. A flat input makes ordinary external tensor compute derived external tensor. If one of the two cohomology families in the Künneth spectral sequence is flat, the higher Tor terms vanish; this is a filtration statement before one claims a canonical direct-sum splitting.

Fixed Tor-amplitude bounds can be tested at all stalks in a topos with enough points, because exactness is stalkwise. Existence of some finite bound at each stalk does not supply one uniform bound. For example take the disjoint union of Spec(k[t_1,…,t_n]) over all n≥1, and on its nth component the residue module at the origin. Its Tor dimension is n there, so every stalk has finite Tor dimension but no global uniform interval exists. The draft's fixed interval hypothesis is essential.

## periodic-tor

Let A=Z/ell² and k=A/(ell). Multiplication by ell on A has image and kernel both ell A. Thus the augmented complex …→A→A→A→k→0, with every differential multiplication by ell, is a free resolution. After tensoring with k, or applying Hom_A(−,k), every differential is zero. Therefore Tor_i(k,k)=Ext^i(k,k)=k for every i≥0. The finite calculation checks ell=2,3,5,7, while this argument proves all primes.

The two-term complex [A --ell→ A] is nevertheless perfect, since its terms are finite free. Its two nonzero cohomology modules are k, neither projective. The identity has supertrace 1−1=0. Consequently trace must be attached to the perfect complex and not defined by requiring its individual cohomology modules to be projective.

## perfectness

Use cohomological indexing. A pseudo-coherent ring complex has a bounded-above resolution by finite free modules. If it has Tor amplitude bounded below by a, truncate this resolution at a sufficiently low degree: dimension shifting makes the remaining syzygy flat. Pseudo-coherence makes that syzygy finitely presented. Finitely presented flat modules are projective, so the truncated resolution is a bounded finite-projective representative. Conversely such a representative is visibly pseudo-coherent with finite Tor amplitude. This is the exact ring criterion of Stacks15.76.2; its sheaf form is local, and global existence of a single finite-projective representative needs additional hypotheses.

Shifts, cones, finite sums and tensor products of bounded finite-projective complexes stay in that class. The perfect category is also closed under direct summands, as the cited criterion shows. A bounded acyclic complex of projectives is split contractible: split the surjection onto its last nonzero term and proceed backwards. The boundedness is indispensable for this elementary induction.

## graded-traces

For a bounded finite-projective complex P, define tr(u)=sum_i (−1)^i tr(u^i). If u=dh+hd is null-homotopic, write its ith term d^{i−1}h^i+h^{i+1}d^i. Rectangular cyclicity tr(AB)=tr(BA) pairs the first summand in degree i with the second in degree i−1 with opposite signs. All terms cancel. A bounded acyclic projective complex is contractible, so its endomorphism traces vanish. Passing through the cone of a quasi-isomorphism gives independence of bounded projective model.

For a strictly commuting square of chain maps, the induced endomorphism of Cone(f) is block triangular on target^i direct-sum source^{i+1}; its supertrace is tr(target)−tr(source). This proof does not apply to an arbitrary endomorphism of a distinguished triangle whose commutativities exist only in the derived category. See the counterexample below.

The signed flip on total tensor is x tensor y ↦ (−1)^{ij} y tensor x for elements of degrees i,j. Degree-zero maps then satisfy tr(u tensor v)=tr(u)tr(v), since (−1)^{i+j}=(−1)^i(−1)^j. The finite output checks a concrete three-degree example and the cancellation of a rectangular homotopy. Dual P^vee=Hom(P,A) has reversed degrees and the usual signed differential. Evaluation and coevaluation identify Hom(P,M)=P^vee tensor M and P with P^vee-vee. Composition–evaluation identifies Hom(P,Q)^vee with Hom(Q,P). Its degree-zero pairing is tr(vu)=tr(uv). These are statements about finite-projective models, not arbitrary flat modules.

## triangle-counterexample

Put R=Q[epsilon]/(epsilon²). Let A=R in degree1; B=[R --epsilon→ R] in degrees0,1; C=R in degree0. The natural inclusion A→B and projection B→C give a triangle A→B→C→A[1]. Take a=1+epsilon on A and b=c=1. The first square commutes up to the homotopy h:B^1→B^0 equal to1, since the difference is epsilon in degree1. The second square commutes strictly. The connecting map is multiplication by epsilon, and epsilon(1+epsilon)=epsilon, so the last square commutes as well. These maps therefore give an endomorphism of the triangle in D(R).

Yet tr(A,a)=−1−epsilon, tr(B,b)=0, and tr(C,c)=1. The additivity defect tr(A)+tr(C)−tr(B)=−epsilon is nonzero. The exact dual-number calculation records each equality. This checks the stronger assertion imported by the earlier notes; it is not attributed to Grothendieck's strict cone assertion. Stacks110.65 gives the same phenomenon, and Illusie's chronology attributes the historical counterexample to Ferrand in1968.

## artin-schreier

For k algebraically closed of characteristic p, Artin–Schreier exactness and vanishing of positive quasi-coherent cohomology on affine space identify H¹_et(A²_k,F_p) with k[x,y]/{h^p−h}. Pullbacks from the two factors are represented by polynomials in x alone and y alone. Suppose xy=a(x)+b(y)+h^p−h. Restrict to the monomial orbit x^{p^r}y^{p^r}, r≥0. If c_r is the coefficient of that monomial in h, comparison yields −c_0=1 and c_r=c_{r−1}^p for r≥1. Hence all c_r are nonzero. A polynomial has only finitely many nonzero coefficients, contradiction. Other monomial orbits do not interfere. This proves failure already in H¹, independently of the uncertain H¹/H² reading.

The program records the nonzero terminal obstruction for primes2,3,5 and several proposed finite truncations. It is a consistency check of the recurrence; the finite-support argument proves the general claim.

## ordinary-projection

Let j:G_m→A¹ over an algebraically closed field and Λ a finite field. Put M=j_!Λ. At the origin M has zero stalk, so (Rj_*Λ) tensor^L M has zero stalk in every degree. But j^*M=Λ and the strict-local punctured neighborhood of the origin has nonzero H⁰ with constant Λ, so Rj_*(j^*M) has nonzero H⁰ stalk there. The ordinary projection morphism cannot be an isomorphism. Perfect or suitably locally constant target hypotheses restore the positive formulas; a compact-support theorem cannot simply be relabeled with f_*.

## determinant-series

Over a characteristic-zero coefficient field, for a finite-dimensional endomorphism F,
log det(1−tF)=−sum_{m≥1}tr(F^m)t^m/m in the formal power-series ring. This follows after scalar extension from eigenvalues, or from the formal derivative identity followed by matching constant terms. Inserting the alternating cohomological trace identity into the logarithm of the Euler product and exponentiating gives product_i det(1−tF_i)^{(−1)^{i+1}}. Finitely many finite-dimensional cohomology groups make it a rational function. This formal calculation does not prove the geometric trace theorem or an independence-of-ell assertion. Those are separately cited.

## adic-trace

For a bounded finite-free Z_ell complex with chain endomorphism, reduction of its supertrace modulo ell^r equals the supertrace of the reduced complex. Thus the compatible finite-level traces determine one element of Z_ell. The same statement for a perfect complex follows locally from a finite-projective model and independence of that model. Merely having finite cohomology at each level does not justify an unproved interchange of derived inverse limits, cohomology and trace. The supplied draft explicitly asks for this additional work; this certificate proves only compatibility in the displayed perfect situation.

## trace-finiteness

Finite Tor amplitude without pseudo-coherence does not make an object dualizable. An infinite-rank free module over a field is flat but its identity has no finite categorical trace in the ordinary category of vector spaces. Therefore the missing pseudo-coherence hypothesis matters at scan144.

For the deletion of “bounded” at scan146, an unbounded representative is not itself a counterexample to existence of the intrinsic trace of a perfect object. Take the direct sum, over n≥0, of the identity complex [A→A] in degrees −2n−1,−2n. It is degreewise finite free, bounded above, contractible and represents zero. Its intrinsic trace is zero. The termwise infinite alternating rank sum has partial sums0 and1 and is undefined without an extra summation convention. This checks the danger of the literal termwise reading, while preserving the valid interpretation via a bounded perfect replacement.

## ramification

The typed ramification leaves omit the definitions and earlier sections to which their symbols r, diagonal ideals and transporters refer. Accordingly this review verifies their visible reductions conditionally rather than claiming an independent proof of the entire theorem. For a tower of finite field extensions, degrees multiply. For finite modules over a domain, generic rank is unchanged by faithfully flat completion when the generic decomposition is handled componentwise. Combining these facts with the multiplicity formulas below validates the visible numerical substitutions where hypotheses are supplied. It does not identify the unspecified invariant r or prove the missing Lemmas2.1–2.2 from no definitions.

The candidate Auslander–Rim paper is supported by title and related contemporary references, but the primary paper was not accessible for exact collation in this run. This is why several claims remain classF, with explicit missing input, rather than being assigned to that paper on resemblance alone.

## multiplicity

If R→S is flat local and S/m_RS has finite length, tensor a composition series of a finite-length R-module M with S. Each successive quotient becomes S/m_RS; exactness yields length_S(M tensor_R S)=length_R(M) length_S(S/m_RS). If a finite free resolution F of M is available, reduction modulo a residue field gives the Euler identity sum_i(−1)^i length Tor_i = sum_i(−1)^i rank(F_i) times the residue-field factor. This is finite Euler characteristic, not an unjustified sum over an infinite resolution.

Hilbert–Samuel multiplicity must be indexed by a fixed ambient dimension when modules of smaller support occur. The d-dimensional leading coefficient vanishes for modules of dimension<d. The usual associativity formula with generic lengths then holds. If “multiplicity” instead means each module's own intrinsic-dimensional leading coefficient, a generic-rank formula can fail: for a DVR R, the module k has own-dimensional multiplicity1 but generic rank0. Likewise the finite R-algebra R×k has rank1; summing each factor's intrinsic multiplicity gives2. The supplied typed Lemma2.6 needs the conventions of its missing §1. This is a mathematical convention alarm, not an assertion that its original author made an error. Stacks43.15 fixes an exact modern convention.

The finite difference calculation checks that the dth forward difference of n^d is d!; this is the polynomial basis underlying the leading-coefficient normalization. The proof is by successive degree reduction, each difference multiplying the leading coefficient by its current degree.

## regular-local

For an n-dimensional regular local ring with residue field k, its associated graded ring for the maximal ideal is k[X_1,…,X_n]. Thus length(R/m^s) counts monomials of total degree<s and equals binomial(n+s−1,n); length(m^s/m^{s+1})=binomial(n+s−1,n−1). The program checks35 small cases; stars-and-bars proves the formula for all n,s. The associated-graded identification is the standard regular-local theorem, used here explicitly.

Normalization of a one-dimensional noetherian domain in a finite extension of its fraction field is a Dedekind domain with finite fibers over the original spectrum, even without assuming the normalization finite as a module. Over a local base it is semilocal. A finite-rank projective module over a semilocal ring is free, so its invertible ideals are principal. This proves the semilocal-PID consequence with the hypotheses of Stacks10.120.18 and10.78.7.

Noetherian local completion is faithfully flat. Hence I R-hat intersect R=I. If a finitely generated ideal becomes principal in the completed local ring, its minimal number of generators can be read modulo the maximal ideal and is at most1 before completion; Nakayama gives principality. No equality R=R-hat is implied.

## coefficient-field

Equicharacteristic alone does not give a coefficient field. Let R=Q[x,y] localized at the maximal ideal (x²−2,y). It is regular local of dimension2 with residue field Q(sqrt(2)). A coefficient field would embed sqrt(2) into its fraction field Q(x,y), but Q is algebraically closed in this purely transcendental extension, impossible. Completeness supplies the missing hypothesis in the Cohen theorem.

Even a regular local ring already containing its residue field need not be a power-series ring: Q[x,y]_(x,y) is countable, while Q[[x,y]] is uncountable. Its completion is the latter ring. The manuscript's R≅k[[x,y]] must be read with a completion hypothesis or as an equality for R-hat. The supplied transcription is left untouched.

## weierstrass

In a complete equicharacteristic regular local ring k[[x_1,…,x_n]], the classical Weierstrass preparation theorem applies to a series regular in x_1 of order b. Its distinguished polynomial is monic of degree b in x_1; the unit and polynomial are unique. The page's homogeneous induction for uniqueness is valid: at the first degree where two factors differ, the difference in polynomial parts has x_1-degree<b whereas the product of the initial monic degree-b form with a nonzero correction has x_1-degree≥b. Contradiction. Existence is a use of the classical preparation theorem, not independently proved by this paragraph.

The statement involving a “tangential” parameter cannot be reversed silently. For z=t=x_2 in k[[x_1,x_2]], no factorization z=x_2^s times a unit with s=0 is possible; divisibility is visible directly. The exact intended tangential/non-tangential clause needs the scan and preceding conventions.

## blowup

For the dimension-n assertion, choose regular parameters x,y₂,…,y_n of R.
At a point over the closed point of the x-chart, the ambient polynomial
ring R[T₂,…,T_n] localized at that point is regular of dimension2n−1.
The n−1 equations xT_i−y_i have independent linear classes in its maximal
ideal modulo its square: the coefficient of y_i distinguishes each one.
They therefore form part of a regular system of parameters. Their quotient
is regular local of dimension n. Its quotient by x is the localization
of k[T₂,…,T_n] at a maximal ideal and has dimension n−1; hence x is a
nonzero parameter. Inverting x identifies the equations with T_i=y_i/x,
and x-torsion-freeness identifies this local quotient with the required
localization of R[m/x]. This proves the general n statement of C-SA13-072,
including possibly non-rational closed points of the exceptional divisor.
The maximal-ideal condition is essential for retaining dimension n.

On the x-chart of the blowup of m=(x,y), write T=y/x. If an element has order at least s, divide its degree-s homogeneous expansion by x^s; each monomial x^{s−j}y^j becomes T^j. Terms of higher order remain in the extended maximal ideal. This gives the page's membership and strict-transform calculation. Conversely the order filtration detects whether x^s divides the transformed expression. The regularity of the chart localized at a point of the exceptional divisor follows from its presentation R[T]/(xT−y), with maximal ideal generated by x and a lift of the irreducible residue polynomial in T; dimension is2 and the minimal number of generators is2. For a rational point the latter polynomial is T−a. Changing the chosen regular parameter changes the chart, not the blowup glued from the Rees algebra.

The finite-field direction check on the page is elementary for binary quadratics over F2: a nonzero ax²+bxy+cy² cannot vanish at all three points of P¹(F2), since the values are a,c,a+b+c. The program checks all seven possibilities. No analogous assertion for arbitrary degrees over arbitrary finite fields is inferred.

## cyclic-generators

For a surjection of finite cyclic groups of orders m and n, with n dividing m, let u modulo n be a generator. Put v=n times the product of primes p dividing m for which p does not divide u, and put w=u+v. If p divides m and u, then p does not divide n, so p does not divide v and therefore not w. If p divides m and does not divide u, then p divides v and not w. Thus gcd(w,m)=1 and w≡u mod n. Every generator lifts to a generator. The exact enumeration checks45,150 cases with m≤300; the prime-by-prime argument proves the general statement.

## etale

Flatness, finite presentation and a finite separable residue-field extension at a point do not suffice for étaleness. Q→Q[epsilon]/epsilon² is flat of rank2 and finitely presented and has residue extension Q/Q, but Omega=(Q[epsilon]/epsilon²)/(epsilon) d epsilon is nonzero. The geometric fiber is nonreduced. The correct fiber criterion requires the fiber to be étale, equivalently geometrically reduced and zero-dimensional at the relevant point, together with flatness and local finite presentation. This is Stacks29.37.8/59.26.2 and EGAIV's étale criterion.

An étale universally injective morphism is an open immersion (Stacks41.14.1). Mere injectivity on a selected set of ordinary points is not a replacement for universal injectivity. The supplied typed topos fragment on scan145 continues on subsequent supplied sheets; its assessment is completed in the p2 shard rather than pretending this one page defines all its notation.
