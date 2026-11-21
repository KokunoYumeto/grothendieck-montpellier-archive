# THETA3: non-CM and integral-model investigations

Author/checker: GPT-6 Astra Pro, sub-run `/root/noncm_integral`; reasoning effort inherited and not separately exposed. Date: 21 November 2026 (UTC; also 21 November in Europe/Berlin). These are research notes for the parent, not claims of Lean verification. Every proof below was reread in full; finite checks are separately described. Known results are inputs, not newly proved findings. The labels C01–C10 denote proved refinements or deductions of this run; no priority claim is intended for elementary lemmas or explicit special cases.

## 1. Exact source boundary and principal sources

The original attachment tree contains 032 and its companion, van Hoften–Sempliner, Milne, Markman LaTeX, Alpöge's note and a Lean map, but not the full Lean archive. The parent subsequently fetched Grothendieck archive scans independently; no claim about an unread scan is made in this note. I used no Masullo claim.

Primary external sources actually opened:

* Y. Liu, *Fourier–Jacobi cycles and arithmetic relative trace formula (with an appendix by Chao Li and Yihang Zhu)*, Cambridge Journal of Mathematics 9 (2021), 1–147. https://yhzhumath.github.io/FJ.pdf . Exact relevant locators: Theorem 1.1, p.5; Theorem 4.18, pp.52–54; Corollary 4.20, pp.54–55. The Hermitian rank is denoted n in that paper; the ball dimension is n−1. At rank n≥3 the whole Albanese has a CM isogeny decomposition. At rank n=2 the assertion is only about its endoscopic part. This sharpens the sketch's memory-based obstruction, and proves that merely increasing the ball dimension does not produce non-CM H1 at congruence level.
* C. Schoen, *An arithmetic ball quotient surface whose Albanese variety is not of CM type*, Electronic Research Announcements in Mathematical Sciences 21 (2014), 132–136. Main unnumbered Theorem, p.132; construction, pp.133–134. Publisher: https://www.aimsciences.org/article/doi/10.3934/era.2014.21.132 . The exact publisher PDF was located in its HTML citation metadata, downloaded, and read in full: https://www.aimsciences.org/data/article/export-pdf?id=c7b42190-d5e0-438a-951d-fb0c3a35cd03 ; local `work/external/Schoen_ball2014.pdf`. It constructs a finite étale cover of an arithmetic compact ball quotient with a non-CM elliptic quotient. The ambient field is Q(zeta_5)/Q(sqrt(5)); the elliptic quotient has j=2^11. Its particular rank-three Hermitian space must be selected in 032, rather than inferring commensurability from the field alone. This is a genuine noncongruence escape from the H1 obstruction, already known in 2014.
* C. Li and W. Zhang, *Kudla–Rapoport cycles and derivatives of local densities*, JAMS 35 (2022), 705–797; author PDF dated September 10, 2021, https://www.math.columbia.edu/~chaoli/KRProof.pdf . Cite author-PDF page numbers where given. Local assumptions and definitions: §1.2, pp.3–4; Theorem 1.2.1 = Theorem 3.4.1, p.17; density polynomial: Theorem 3.5.1, p.18, and Corollary 3.5.3, p.19; quasi-canonical cycles §4.1, p.20; horizontal decomposition Theorem 4.2.1, p.21; Theorem 6.1.3, p.34; negative vertical contribution Lemma 6.2.1, pp.35–36. (The web zero-based PDF page index is one less.)
* I. Vollaard and T. Wedhorn, *The supersingular locus of the Shimura variety of GU(1,n−1) II*, arXiv:0804.1522v2. https://arxiv.org/pdf/0804.1522 . The displayed uniformization is (5.4.2), p.34 of the opened PDF. Its Introduction, p.4, records the Fermat-curve components for n=3,4. The supersingular locus in rank3 has positive dimension, so it is not literally a finite definite Shimura set.
* C. Li and Y. Liu, *Chow groups and L-derivatives of automorphic motives for unitary groups, II*, Forum Math. Pi 10 (2022), e5. Author PDF https://www.math.columbia.edu/~chaoli/AIPF2.pdf . Assumption 1.3; Theorems 1.4 and 1.5, pp.4–5; Remark 1.6(2), pp.5–6; Corollary 1.7 and Remark 1.9, p.6; Example 1.10, pp.6–7. The arithmetic inner-product formula requires the stated modularity hypothesis on generating functions. The nonvanishing theorem 1.4 has the stated technical Hypothesis 6.6, removable when S_pi is empty by Remark 1.9. The cycles are homologically trivial; the output is not a nonzero ordinary Hodge class.

The attached van Hoften–Sempliner paper independently supplies the rank3 CM decomposition in Proposition 3.1.7, Theorem 3.1.11 and §3.1.12. The attached 032 supplies the exact cotangent spanning statement in Proposition 4.5, pp.21–22, and rational CM extraction in Theorem 5.1, p.26, with common-level version Corollary 6.7, p.45.

## 2. Non-CM source: the exact obstruction and an actual escape

### THETA3-C01. H1 obstruction at all congruence ball dimensions at least two

**Statement.** Let X be a smooth projective congruence unitary ball quotient in the setup of Liu, Hermitian rank m≥3. Let B be a simple complex abelian variety not of CM type. Then

    Hom_Hdg(H1(B,Q), H1(X,Q)) = 0.

The same assertion applies to the character-generated H1 subspace of any smooth projective X whenever that subspace is a sum of images of CM Hodge structures. Iterating sums, tensor products, duals, and Hodge subquotients of CM Hodge structures does not supply a non-CM H1 summand.

**Proof.** Liu Corollary 4.20 states that Alb(X) is isogenous to a finite product of CM abelian varieties at a fixed sufficiently small level. Hence H1(X,Q) is a polarizable Hodge structure with commutative Mumford–Tate group. A quotient or sub-Hodge structure of a CM Hodge structure is CM: the Hodge homomorphism on the subquotient factors through an image of the same torus. A nonzero Hodge map from the simple Hodge structure H1(B,Q) is injective, because its kernel is a rational sub-Hodge structure and simplicity follows from the equivalence between abelian varieties up to isogeny and polarizable weight-one rational Hodge structures. It would realize H1(B,Q) as a CM substructure, a contradiction. Finally, a finite collection of CM structures is controlled by a product of tori. Their tensor category is again controlled by a torus, proving the last assertion. ∎

**Boundary.** Do not remove the congruence hypothesis. Schoen's theorem explicitly contradicts that extension. Do not claim that every higher cohomology class on a congruence ball quotient has CM source: this statement concerns H1/Albanese and the indicated tensor subcategory.

### THETA3-C02. Trace-zero selection rule on a noncongruence cover

**Statement.** Let f:X→S be a finite étale cover of connected smooth projective complex surfaces of degree d. Then

    H1(X,Q) = f*H1(S,Q) ⊕ ker(f_*:H1(X,Q)→H1(S,Q)).

For u in the trace-zero summand and v1,v2,v3∈H1(S,Q),

    integral_X u cup f*v1 cup f*v2 cup f*v3 = 0.

If H1(S,Q) is CM and U⊂H1(X,Q) is a non-CM simple sub-Hodge structure, then U lies in the trace-zero summand.

**Proof.** The transfer/projection formula gives f_*f*=d id on H1(S,Q). Thus d^(-1)f*f_* is a projector, with image f*H1(S,Q) and kernel ker f_*. For the period, apply the projection formula to obtain integral_S (f_*u) cup v1 cup v2 cup v3=0. The restricted map f_*|U is a Hodge morphism into a CM structure and hence vanishes by the argument in C01. ∎

**Consequence.** A four-factor period with exactly one non-CM new factor and three old theta factors cannot be the next step. At least two new factors are required. This excludes a specific tempting extension, while allowing the positive construction C03 below.

### THETA3-C03. A mixed non-CM/CM theta period on a common finite cover

**Hypotheses.** Let S0=Gamma0\D be a compact congruence ball surface in the exact setup of 032 §4. Let X0 be a compact ball surface commensurable with S0, admitting a nonconstant morphism a0:X0→E0 to a non-CM elliptic curve. Passing to a common finite cover is permitted. For the Schoen exemplar choose 032's otherwise arbitrary V to be the specific Hermitian space over E=Q(zeta_5), F=Q(sqrt(5)) supplied on Schoen p.133, multiplying its form by a scalar of F with suitable real signs to obtain (2,1) at the active place and (3,0) at the other place. Arithmetic unitary determinants have finite image here: integral norm-one units in a CM field form a finite group, and an arithmetic subgroup is commensurable with an integral one. Thus a further finite cover passes to SU(V). Choose the principal S0 in this commensurability class. Equality of the CM fields alone would not suffice. Fix any permitted CM sign function v in 032 with v(1)=1.

**Statement.** There is a common finite étale cover X of X0 and a sufficiently deep principal cover S of S0, a nonzero invariant holomorphic one-form alpha0 on E0, and a theta form beta on S belonging to the complex span of rational CM source maps from U(v), such that, writing a:X→E0 and f:X→S,

    xi = a*alpha0 wedge f*beta != 0,
    integral_X xi wedge conjugate(xi) > 0.

There are in addition a CM abelian variety B(v), a morphism b:X→B(v), and a holomorphic form gamma on B(v) for which a*alpha0 wedge b*gamma is nonzero. Therefore (a,b):X→E0×B(v) has a two-dimensional image and produces an algebraic image-surface correspondence.

**Proof.** Keep S0 principal. The pullback alpha of a0*alpha0 to D is nonzero, since a0 is nonconstant, so choose a point x where alpha_x !=0. Proposition 4.5 of 032 says that finitely many actual finite Schwartz inputs have theta one-form values spanning T_x^*D. Since that cotangent space has dimension2, some beta has beta_x independent of alpha_x. The finite list descends to a sufficiently deep principal cover S of S0. Refine that principal cover once more using 032 Theorem5.1/Corollary6.7 so that beta has its rational CM-source expansion. Now form X from the intersection of the torsion-free commensurable lattices defining X0 and S, choosing a connected component. This is a common finite étale cover and preserves the nonzero wedge at a lift of x. Thus xi is a nonzero holomorphic2-form on the projective surface X. In local holomorphic coordinates xi=g dz1 wedge dz2, xi wedge conjugate(xi) is a nonnegative real volume form, strictly positive wherever g !=0 (the usual complex orientation). Its integral is strictly positive.

By CM extraction, [beta] is a finite complex sum of h_j(u_j), where h_j:U(v)→H1(S,Q) are rational Hodge maps and u_j lie in the selected (1,0) line. On a compact Kähler manifold holomorphic1-forms are the unique holomorphic representatives of their classes, so this expansion holds for the forms. If every alpha wedge f*h_j(u_j) were zero then alpha wedge f*beta would be zero, contradiction. Choose one nonzero term. A positive integer multiple of h_j is induced by an algebraic morphism S→B(v), by the Albanese argument of 032 Lemma2.2. Compose with f to obtain b. If (a,b) had image dimension≤1 then its differential would have rank≤1 on a dense open set, forcing the wedge to vanish identically. Thus its image dimension is2. Proper pushforward yields (a,b)_*[X]∈CH^{1+dim B(v)−2}(E0×B(v))_Q and the nonzero pairing detects its class. ∎

**What this does and does not settle.** It explicitly attains a non-CM source in a four-one-form period, using two new forms alpha and conjugate(alpha), and two CM forms beta and conjugate(beta). It does not obtain the corresponding forms from an adelic theta lift on the noncongruence subgroup; only the old factor remains theta. It does not identify a previously unknown Hodge tensor as algebraic. The image cycle is genuine but its target has only one non-CM elliptic factor; its Hodge classes are already controlled by known factors, as explained in C05. The next substantive non-CM gate is an algebraic projector and enough independent tests on a non-divisor Hodge summand, C04.

### THETA3-C04. Exact extraction and rank gate beyond the CM embedding lines

**Statement.** Let A be a smooth projective variety, let T⊂H^{2p}(A,Q)(p) be a d-dimensional rational subspace of Hodge classes, and suppose an algebraic correspondence acts as a projector e onto T. Let Z1,...,Zr be algebraic cycles of codimension p. Fix a basis t1,...,td of T and a nondegenerate rational bilinear form Q on T. Form

    M_ij = Q(e cl(Z_i), t_j).

If rank(M)=d, then every class of T is algebraic. If an algebra D of algebraic correspondences preserves T, the same conclusion follows from one cycle Z provided the D-orbit of e cl(Z) spans T. For a simple D-module T this is equivalent to e cl(Z)!=0.

**Proof.** Since e is algebraic, every e cl(Z_i) is an algebraic class. Nondegeneracy of Q identifies T with its dual, so row rank d is equivalent to these algebraic vectors spanning T. The orbit variant is the same argument applied to the finite-dimensional orbit span; it is generated by algebraic correspondences applied to an algebraic cycle. A nonzero submodule of a simple module is the whole module. ∎

**Why the scalar period alone is insufficient.** In Q² with the ordinary dot product, the algebraic candidate span W=Q(1,0) pairs nontrivially with (1,1), although (1,1) is not in W. This is a linear-algebra counterexample to the inference, not an example of a nonalgebraic Hodge class. In 032 Proposition3.1 the pure embedding-line divisors provide the required extraction: those pure line pairs are algebraic after scalar descent. For a general non-CM H1 the polarization supplies a sum of rank-one tensors, not the individual holomorphic eigenline projector. One must prove the actual projector/rank statement for the proposed non-CM summand.

### THETA3-C05. Why one non-CM elliptic factor adds no new Hodge-conjecture case

**Statement (formal consequence with explicit hypotheses).** Let E0 be a non-CM elliptic curve and B a CM abelian variety for which the rational Hodge conjecture holds. Then all Hodge classes on E0×B are algebraic. More precisely, under the Künneth decomposition,

    Hdg^p(E0×B) = 1 tensor Hdg^p(B) ⊕ [pt] tensor Hdg^{p−1}(B),

where Hdg^p(Y) means the rational (0,0)-classes in H^{2p}(Y,Q)(p), and [pt] is the generator of H²(E0,Q)(1).

**Proof.** Use the classical background facts Hg(E0)=SL(H1(E0,Q)) and Hg(B) a torus T. The connected Hodge group H of the product projects surjectively to both factors. Its derived subgroup projects surjectively to SL2 and trivially to T. Being a subgroup of SL2×1 with full projection to SL2, it equals SL2×1. The quotient H/(SL2×1) maps onto T; thus H=SL2×T. The only SL2-invariants in H*(E0,Q)=Q⊕H1(E0,Q)⊕Q(−1) occur in degrees0 and2. Taking invariants in Künneth gives the displayed decomposition. Each invariant is represented by the pullback of a cycle on B, or by a point on E0 times a cycle on B. ∎

This is not claimed as a new theorem. For the classical Hodge-group assertion use B. Moonen, *Notes on Mumford-Tate groups* (Centre Emile Borel, March1999), §2, Example(2.6), https://www.math.ru.nl/~bmoonen/Lecturenotes/CEBnotesMT.pdf (opened in this run). It follows equally from reductivity and the fact that a proper connected reductive subgroup of SL2 is a torus, together with the CM criterion of attached032 Lemma2.3.

## 3. Integral models: conventions and two exact local computations

Use local notation k0 for a finite extension of Q_p, p odd, residue cardinality q; to avoid conflict with the global CM field write k/k0 for its unramified quadratic extension, O=O_k, uniformizer pi. The following uses precisely Li–Zhang's unramified, principally polarized Rapoport–Zink space N_n of signature(1,n−1), and its nonsplit rank-n special quasi-homomorphism space V_n. For a full-rank O-lattice L⊂V_n,

    Int(L)=chi(N_n, O_{Z(x1)} tensor^L ... tensor^L O_{Z(xn)}).

This is a derived Euler characteristic, not the ordinary length of the scheme-theoretic intersection. Its definition is independent of the basis x_i. Li–Zhang Theorem1.2.1/3.4.1 states Int(L)=−d Den(X,L)/dX at X=1. Their normalized polynomial (Theorem3.5.1) is

    Den(X,L)= sum_{L subset N subset N^vee} X^{2 length_O(N/L)} m(t(N);X),
    m(t;X)=product_{i=0}^{t−1}(1−(−q)^i X).

Here t(N) is the number of positive elementary divisors, and val(L) is the determinant valuation. The nonsplit space has odd determinant valuation. The normalized polynomial is fixed by

    Den((−q)^{−k}, L)=Den(<1>^{n+k},L)/Den(<1>^{n+k},<1>^n).

No omitted logarithm occurs in Int=−Den'(1). If converted to a local Whittaker derivative, Li–Zhang Remark3.4.2 introduces log(q²) and the explicit product of unramified factors. These constants must not be dropped when comparing any analytic norm.

### THETA3-C06. A full-rank negative intersection: diag(pi,pi,pi)

**Statement.** In the above unramified local model take n=3 and L with Hermitian Gram matrix pi I3. Then

    Den(X,L)=(1−X)(1+(q−q²)X+X²),
    Int(L)=q+2−q²<0.

In particular q=3 gives Int(L)=−4. This refutes the universal claim that these local arithmetic intersections are positive ordinary lengths, including full-rank intersections in the correct Rapoport–Zink model.

**Proof.** The determinant valuation of L is3, hence odd, so its ambient Hermitian space is the required nonsplit V3. Every integral overlattice N has determinant valuation

    val(N)=3−2 length_O(N/L)>=0.

It follows that length_O(N/L) is0 or1. The length0 term is L, of type3. A length1 overlattice lies between L and L^vee=pi^(−1)L and is of the form

    N=L+O pi^(−1)v,

where v mod pi spans a line in L/pi L. It is integral exactly when the line is isotropic for the nondegenerate Hermitian form I3 over F_{q²}/F_q. Indeed its pairings with L are already integral, and the one additional condition is h(v,v)∈pi²O, equivalently the residual norm is0. Distinct residual lines give distinct overlattices. For any such N the determinant valuation is1, so its elementary divisors are(0,0,1) and its type is1.

For completeness count the isotropic lines. Let a_r be the number of vectors in F_{q²}^r with sum of coordinate norms0. The norm map has one preimage of0 and q+1 preimages of every nonzero element. Therefore a_1=1 and

    a_r=(q+1)q^{2r−2}−q a_{r−1}.

This gives a_2=q³+q²−q and a_3=q⁵−q³+q². Remove the zero vector and divide by q²−1, the number of nonzero vectors on a line. The number of isotropic lines is

    (q⁵−q³+q²−1)/(q²−1)=q³+1.

Insert these overlattices into the exact density formula:

    Den(X,L)
      =(1−X)(1+qX)(1−q²X)+(q³+1)X²(1−X)
      =(1−X)(1+(q−q²)X+X²).

Differentiation at1 gives −Den'(1)=q+2−q². Li–Zhang's local identity gives the asserted Int. For odd q≥3, q²−q−2=(q−2)(q+1)>0, hence Int<0. ∎

**Independent numerical check.** `work/check_integral_lattices.py` enumerates projective isotropic lines over explicit F_{q²}=F_q[sqrt(d)] for q=3,5,7,11. It independently obtains28,126,344,1332 and Int=−4,−18,−40,−108. The polynomial coefficient computation also agrees. This verifies finite examples, not the general local theorem.

**Meaning.** Determinant positivity at definite signature cannot be transferred to arbitrary local intersection numbers without specifying the homological degree, derived signs, and local cycle combination. Positivity of representation densities at the interpolation values (−q)^−k also does not imply positivity of −Den'(1): the displayed polynomial is a counterexample in the precise arithmetic setting.

### THETA3-C07. A positive local sector with an exact lower bound

**Statement.** Let M be a self-dual Hermitian O-lattice of rank n−1 and let x be orthogonal to M with h(x,x)=pi^{2a+1}, a≥0. Put L=M orthogonal-sum O x. In the nonsplit local model,

    Den(X,L)=(1−X) sum_{j=0}^a X^{2j},
    Int(L)=a+1>=1.

**Proof.** Every integral overlattice N⊃L decomposes orthogonally as M⊕(N∩M_k^perp). To see this, project any y∈N onto M_k using the perfect pairing on M. Since h(y,M)⊂O, its projection belongs to M. Subtract that projection to obtain the claimed splitting. Every lattice in the one-dimensional complement is pi^(−j)O x for some integer j. Containment of O x gives j≥0; integrality gives2a+1−2j≥0, so0≤j≤a. Each such overlattice has length j and exactly one positive elementary divisor, because2a+1−2j is positive odd. Each contributes X^{2j}(1−X). Sum and differentiate at1 to obtain a+1, then use Li–Zhang. ∎

Here the positive value agrees with the genuine rank-one deformation-length interpretation after cancellation of the self-dual lattice, as in Li–Zhang §2.11 and Example2.4.3/Example3.5.2. The proof above does not need to assume that interpretation. This is a completely normalized integral nonvanishing certificate; it is not a lower bound for the different 032 archimedean mixed period unless a separate matching theorem identifies its local factors.

## 4. The next integral step: separate horizontal and vertical terms

Li–Zhang Theorem4.2.1 decomposes the horizontal part of a rank-(n−1) special cycle as primitive quasi-canonical lifting cycles indexed by integral overlattices of type≤1. Their Theorem6.1.3 identifies the horizontal intersection function with the correspondingly separated horizontal density derivative. Thus the signed total derivative C06 is not the stopping point: the cited source itself provides the finer decomposition needed to ask whether a proposed contribution survives in characteristic zero. A future comparison to Alpöge step2 should match a finite, explicit collection of quasi-canonical components and its local theta normalization, rather than identifying an infinite valuation sum with a geometric intersection.

### THETA3-C08. Positive vertical intersection does not detect a generic cycle

**Statement.** Even a positive ordinary local intersection of algebraic cycles on an integral model does not imply a nonzero generic-fibre cycle class. Conversely, if an actual horizontal flat cycle and its realization comparison are given, its generic class is algebraic by construction; the issue is identification with the desired Hodge class.

**Proof/counterexample.** Let R be a DVR with uniformizer pi, and X=P1_R. Let F be its special fibre and H a section. They intersect properly at one point, with local ring quotient R/(pi), so the intersection length is1. But F has empty generic fibre, hence restricts to0 in the Chow group and cohomology of X_K. This gives the claimed counterexample. For a flat horizontal closed cycle Z⊂X of the required relative codimension, its generic fibre Z_K is a closed algebraic cycle. Its cycle class specializes compatibly in a smooth proper family, but positivity of an unrelated vertical intersection does not identify cl(Z_K) with any chosen rational Hodge tensor. ∎

The basic-locus comparison likewise retains a geometric factor. Vollaard–Wedhorn (5.4.2) is

    I(Q) \ (N_red × G(A_f^p)/K^p) ≅ M^ss.

It is not an equality of M^ss with a finite Shimura set: in rank3 the Rapoport–Zink factor supplies Fermat curves. Definite mass formulas can count indexing data/components, while local intersection theory depends on the retained Rapoport–Zink geometry.

### THETA3-C09. The coefficient in sketch1.6 is an arithmetic identity, not an infinite product of lifting coordinates

**Statement.** If e_s=q^{s−1}(q+1), then

    sum_{s>=1} 1/e_s = q/(q²−1).

However, if t_s are elements of C_p with normalized valuations v(t_s)=1/e_s, the infinite product product_{s>=1} t_s does not converge in C_p.

**Proof.** The sum is a geometric series. Its partial sums are bounded and tend to the displayed finite positive value. Therefore the absolute values of the partial products tend to a nonzero number, so convergence of the products could not have limit0. A convergent sequence of nonzero partial products with nonzero limit would have successive ratios t_s→1. But v(t_s)>0 implies |t_s|<1, hence |1−t_s|=1 for every s, so this is impossible. ∎

Li–Zhang §4.1 gives the quasi-canonical extension degree q^s(1+q^−1)=e_s. Thus the coefficient is indeed the sum of reciprocal extension degrees in the unramified setting. The proof does not establish that the theta-derivative divisibility in Alpöge step2 is obtained from these coordinates, and it rules out the naïve literal convergent-product interpretation. A finite divisor or determinant identity is the remaining gate.

**Primary Gross source and finite deformation calculation.** Gross, *On canonical and quasi-canonical liftings*, original MPI/SFB85-30 preprint appended to Gross–Zagier, https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf , Proposition5.3(2),(3), manuscript p.9 (PDF page77, zero-based index76; proof pp.9–11). The original scan was visually inspected, not only its OCR. In the unramified quadratic case it states that the level-s lift is defined over W_s of degree e_s=q^{s−1}(q+1) and its formal modulus t_s has W_s-valuation1. With base valuation v(pi)=1, where pi is the base uniformizer, this gives v(t_s)=1/e_s. The canonical modulus t_0 belongs to pi W. Therefore v_{W_s}(t_s−t_0)=1, since e_s>1. In the one-parameter deformation ring W[[t]], the intersection of the quasi-canonical branch t↦t_s with the canonical section t=t_0 is W_s/(t_s−t_0), of ordinary length1 over W_s (and over W when the common residue field is algebraically closed). By contrast the branch's finite-flat degree is e_s and the base-normalized modulus valuation is 1/e_s. These are three different invariants. For finite S, v(product_{s=1}^S t_s)=q(1−q^{−S})/(q²−1); completing whole Galois orbits instead gives v(product_{s=1}^S Norm_{W_s/W}(t_s))=S. Both formulas follow by additivity and total ramification, and neither asserts a theta-section identity.

### THETA3-C10. Non-CM arithmetic theta lifts exist in the cited framework, but occupy a different motivic slot

**Statement.** If a theta cycle Z is homologically trivial, no nonzero ordinary Hodge class is detected by its cohomological pairings; nonzero height supplies information beyond the homological/numerical realization.

**Proof.** Homological triviality means cl_B(Z)=0. Cup product with any Betti class is therefore0. The same holds for the corresponding étale realization. A nonzero height, if established, can show Z nontrivial modulo rational equivalence, but cannot change cl_B(Z). ∎

Li–Liu II Example1.10 explicitly allows π associated to Sym^{2r−1}, r≥2, of a non-CM elliptic curve under its modularity and local hypotheses; good reduction at every nonsplit finite place gives S_pi empty, and when r[F:Q] is odd their theorem applies without the cited technical Hypothesis6.6. The equality bar in r≥2 was checked against the actual PDF image by the theta032 agent; web extraction had dropped it. Their Theorem1.4 produces nonzero localized CH^r_hom from a simple central zero; Theorem1.5 gives the height formula under the additional generating-series modularity hypothesis. This is an exact existing extension to non-character input on unitary groups. In Grothendieck's language it concerns cycles invisible in the homological/numerical quotient, and motivic extension data/Abel–Jacobi phenomena. To attack a non-CM Hodge class, one must still construct the algebraic correspondence carrying the relevant nontrivial realization and satisfy C04's extraction gate.

## 4A. A precise local bridge to the exponent in Alpöge step2

### THETA3-C11. Height-two formal derivatives: the exact slope and infinitely many sharp values

**Statement.** Let p be an odd prime, Q=p², and let pi be an element of C_p with normalized valuation v_p(pi)=1. Put

    ell(T) = sum_{r>=0} T^{Q^r}/pi^r,
    E(Z) = ell^{-1}(Z),
    D = ell'(T)^{-1} d/dT.

For every f(T) in O_{C_p}[[T]] and every integer a>=1,

    v_p(D^a f(0)) >= v_p(a!) − (a−1)/(p²−1)
                  = ap/(p²−1) + 1/(p²−1) − s_p(a)/(p−1),

where s_p(a) is the sum of the base-p digits of a, and v_p(0)=+infinity. Moreover, D^p is zero after reduction modulo p. The bound is sharp infinitely often: for f(T)=T and a=Q^r (r>=0), equality holds and

    v_p(D^{Q^r} T(0)) = (Q^r−1)p/(p²−1).

In particular the coefficient p/(p²−1)=1/p+1/p³+... in Alpöge step2 arises from a precise local formal-group estimate with an explicit logarithmic digit-sum error. This statement does not assert that an arbitrary analytic theta section, in its stated analytic normalization, has an integral coefficient function in this formal frame.

**Proof of the lower bound.** Choose beta in C_p with beta^{Q−1}=pi. Then v_p(beta)=1/(Q−1). The scaled logarithm

    L(T)=ell(beta T)/beta
        =sum_{r>=0} pi^{(Q^r−1)/(Q−1)−r} T^{Q^r}

has integral coefficients and linear coefficient1: its r-th exponent is

    (Q^r−1)/(Q−1)−r = 1+Q+...+Q^{r−1}−r >=0

for r>=1. Recursive inversion of a formal power series whose linear coefficient is1 works over any commutative ring. Its inverse U(T)=E(beta T)/beta therefore belongs to T O_{C_p}[[T]] and has linear coefficient1. Since f is integral,

    f(E(beta T))−f(0)=f(beta U(T))−f(0) belongs to beta T O_{C_p}[[T]].

The logarithmic coordinate Z=ell(T) rectifies the derivation: the formal chain rule gives d(f(E(Z)))/dZ=(Df)(E(Z)). Hence

    f(E(Z))=sum_{a>=0} D^a f(0) Z^a/a!.

The coefficient of T^a in f(E(beta T)) has valuation at least v_p(beta). It is beta^a D^a f(0)/a!, so

    v_p(D^a f(0)) >= v_p(a!)−(a−1)/(Q−1).

Legendre's formula v_p(a!)=(a−s_p(a))/(p−1) gives the displayed expression. Since s_p(a)<=(p−1)(1+floor(log_p a)), the error is explicitly O(log a), with no unspecified theta- or curve-dependent constant in this formal calculation.

**Proof of nilpotence modulo p.** Since Q=p² and v_p(pi)=1,

    ell'(T)=sum_{r>=0} (Q/pi)^r T^{Q^r−1}

is an integral unit congruent to1 modulo p. Thus D reduces to d/dT on (O_{C_p}/p)[[T]]. The p-th iterate of d/dT is zero: on every monomial, the product of p consecutive integer factors is divisible by p. This remains true when the coefficient ring is nonreduced. Hence D^p is zero modulo p.

**Proof of sharpness.** For r=1 the exponent in L is0; for every r>=2 it is positive. Modulo the maximal ideal of O_{C_p}, therefore, L(T) reduces to T+T^Q. In characteristic p the formal series

    V(T)=sum_{j>=0} (−1)^j T^{Q^j}

satisfies V(T)+V(T)^Q=T, so it is the inverse of T+T^Q. Formal inversion commutes with reduction because it uses only integral coefficient recursion. Thus the coefficient of T^{Q^r} in U(T) is a unit. Since E(Z)=beta U(Z/beta), its Z^{Q^r}-coefficient has valuation exactly −(Q^r−1)/(Q−1). Apply D^a T(0)=a![Z^a]E(Z). For a=Q^r, s_p(a)=1, yielding

    v_p(D^a T(0))=(a−1)/(p−1)−(a−1)/(p²−1)
                  =(a−1)p/(p²−1).

This proves both sharpness and the equality claimed. ∎

**Coordinates and the CM elliptic application.** The displayed logarithm is a permitted coordinate for a height-two Lubin–Tate formal group with uniformizer pi. Bannai–Kobayashi, *Integral structures on p-adic Fourier theory*, Ann. Inst. Fourier66(2016), pp531–532, Proposition3.5 and its proof, first use exactly sum T^{q^r}/pi^r and then pass to general integral parameters. An integral change of parameter with unit linear coefficient preserves integrality of f; the corresponding normalized invariant derivations differ by a constant unit under the formal-group isomorphism, so valuations of iterates agree. In their CM elliptic application, §5 pp543–544, p is odd inert and the elliptic curve has good supersingular reduction, and its formal group is the height-two Lubin–Tate group attached to pi=−epsilon p. The proof just given works with that pi, without assuming epsilon=−1.

There are actual nontrivial functions satisfying the integrality hypothesis in this primary source. On p546, with b prime to p, they set

    wp_b(z)=wp(z)−b²wp(bz),
    phi(t)=wp_b(lambda(t)) in O_K[[t]],

and similarly an integral modified zeta function. Their Proposition5.5, pp546–547, identifies the invariant derivatives and Fourier moments with the modified Bernoulli–Hurwitz values; Theorem5.1 on p544 (Katz's theorem, re-proved in their §5) gives the stronger floor(np/(p²−1)) divisibility after the stated modification. These are existing CM elliptic applications of the same local slope, not a claim that C11 newly proves Katz's theorem or all raw theta-section integrality.

The coefficient also equals the normalized valuation of a Lubin–Tate period: Schneider–Teitelbaum, *p-adic Fourier theory*, Lemma3.4(b), states v_p(Omega_LT)=1/(p−1)−1/(e(q−1)); putting e=1 and q=p² gives p/(p²−1). Their Appendix supplies its period calculation. This p-adic Omega_LT must not be confused with the complex period Omega_C in Alpöge's normalization.

**Exact remaining frame gate.** A theta function is a section of a line bundle. Extending that line bundle as an invertible sheaf over the formal integral neighborhood gives some integral frame, but the invariant derivative of a section depends on the chosen frame or connection. The required comparison is an equality between the analytically normalized derivatives D^a theta(0)/Omega_C^a and the iterates D_G^a f(0) of an integral coefficient function in a specified compatible frame. Existence of an arbitrary integral trivialization does not establish this equality. A horizontal or cubical analytic frame need not be integral.

Here is an explicit jet obstruction. In the formal characteristic-zero germ C_p[[T]], take the trivial line bundle with section1 and frame e. For fixed a>=1 and any integer M>0, replace the frame by e'=(1+p^{−M}T^a)e. Both frames agree at the origin; the section has the same empty divisor, but its new coefficient is f'=(1+p^{−M}T^a)^{−1}, for which D^a f'(0)=−a!p^{−M}. Its valuation can be arbitrarily negative. The new frame is a generic formal frame, not an integral frame; precisely that distinction defeats an inference from divisor data or the value at the origin alone. This is a formal-germ example and makes no assertion that the frame is invertible on the whole rigid open unit disc.

Even an integral Cartier divisor does not determine exact derivative values. Fix2<=a<Q. The integral functions f_N(T)=T(1+p^N T^{a−1}) all define the same Cartier divisor(T), have the same first derivative at0, but D^a f_N(0)=a!p^N, because E(Z)=Z+O(Z^Q). Their a-th derivative valuations vary with N. The universal lower bound C11 still applies; the example rules out recovering precise higher jets from the divisor alone.

## 5. Current gates, approaches tried, and suggested use in the main paper

1. **Non-CM H1 through the original congruence theta machine:** refuted as a route, by C01 and Liu Cor4.20 for every ball dimension≥2. Trying higher-dimensional balls does not reduce this gate. Switching to U(1,1) at the source and staying in H1 of a higher-dimensional congruence ball cannot avoid the same target obstruction.
2. **Noncongruence cover:** succeeds in admitting non-CM H1 by Schoen; C02 shows exactly why one-new-factor periods fail; C03 succeeds with a paired new factor and a transverse old theta form. This is a concrete positive construction. Remaining gate is C04 for a genuinely exceptional non-CM Hodge summand, not merely existence of a nonzero period.
3. **Non-character arithmetic theta:** known existing success under the Li–Liu hypotheses. It produces homologically trivial cycles, so it addresses an extension/height problem rather than the Hodge cycle-class image. The reduction C10 prevents conflating those outputs.
4. **Integral comparison:** C06 refutes indiscriminate positivity and C07 identifies a rigorously positive explicit sector. The finer horizontal/vertical decomposition of Li–Zhang, not an unqualified length assertion, is the next usable tool. Need an actual local matching of the 032/Alpöge test data with the selected lattice sector and an algebraic horizontal correspondence.
5. **Sketch1.6:** reciprocal-index sum proved; identification with theta-derivative divisibility remains unproved. Naïve infinite-coordinate product is refuted by C09. Finite quasi-canonical divisor identities and Li–Zhang horizontal density formula are a concrete reduced target.
6. **Global definite/intregral coherence:** delegated to definite_bridge to avoid duplicate work. Important caveat already sent: odd-rank unitary groups can be isomorphic for scalar-multiple Hermitian forms; finite Hermitian isometry data and Weil splittings must be tracked, not only abstract groups.

## 6. Checks actually performed

Every proof C01–C11 was reread from hypotheses to conclusion after drafting. C03 was checked specifically for: common-cover construction, nonzero differential, finite versus infinite collection of Schwartz inputs, further level passage preserving the wedge, rational Hodge-map realization, and the image-dimension argument. C06 and C07 were checked against the precise Li–Zhang normalization, odd determinant valuation, type and index conventions; the finite counting script then checked q=3,5,7,11 independently. No independent human verification, Lean compilation, or machine proof of these statements is claimed. C05 uses the classical Hodge-group assertion cited to Moonen Example(2.6); this source was subsequently opened and the locator verified. The C06 value is also consistent with the separate horizontal/vertical calculation in the proof of Li–Zhang Lemma6.2.1: when a3=1, it gives (q+1)+(1−q²).
