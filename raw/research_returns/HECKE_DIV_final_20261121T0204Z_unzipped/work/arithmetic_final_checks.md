# Independent final checks: M2–M4 and P0–P3

Run HECKE_DIV_20261121; date 2026-11-21. Checker /root/arithmetic, GPT-6 Astra Pro, inherited effort setting not exposed. This records a targeted independent proof check of the saved claims, not a full check of Markman's paper or a formal verification.

Read in full: `work/markman.md` (including M6's qualifications) and `work/root_findings.md`. Also read the active Markman source definitions and arguments at `source/LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex`, lines 3069–3244 (twisted sheaves, determinant normalization, Atiyah class and kappa), and lines 3778–3862 (the complete relevant genus-four seed example and the partial-normalization alternative). The source text was supplied locally, so these locators refer to the actual inspected text.

## Verdict and one hypothesis correction

M2 and M3 pass as stated. M4 passes with the intended abelian-fibre hypothesis made explicit: replace its opening “smooth projective family” by “smooth projective family of abelian varieties,” or by an abelian scheme. Its use of M2 is not justified for arbitrary smooth projective fibres, since the multiplication-by-r argument is specific to abelian varieties. This correction was sent to the parent before completion of the audit.

P0–P3 pass at the targeted proof-check level. I additionally recomputed the projector eigenvalue identities and the B,D constants independently, using integer-pair arithmetic in Z[omega]. No mismatch was found.

## FM2. The twisted denominator calculation

Let alpha be the actual mu_r-valued Cech cocycle twisting B. On a complex abelian variety A, comparison with constant Z/r cohomology and the exterior-algebra description of torus cohomology give

    [r]^* : H^2(A,mu_r) -> H^2(A,mu_r),  alpha |-> r^2 alpha = 0.

This kills the mu_r class itself, not merely its image in the analytic Brauer group. After refining to an appropriate analytic cover, [r]^*alpha is the coboundary of a mu_r-valued 1-cochain. Multiplying the gluing maps of [r]^*B by its inverse yields an ordinary coherent sheaf E. The cochain is locally constant and holomorphic.

The determinant assertion survives this change of gluing exactly: multiplying a rank-r gluing map by a scalar b multiplies its determinant by b^r=1. Thus det(E) remains isomorphic to [r]^*det(B), and is trivial under the hypothesis. For a non-locally-free coherent sheaf, “determinant” here means the determinant of its perfect complex (equivalently the usual determinant line for the relevant reflexive sheaf), not the unmodified top exterior-power sheaf if that sheaf is not locally free. The statement in M2 already uses det(B), so no change to its conclusion is needed.

Naturality of kappa is legitimate with Markman's definition. The twisted Atiyah class is defined using the first infinitesimal neighbourhood of the diagonal. Locally constant scalar cochains have zero differential, so the untwisting equivalence identifies that class with the ordinary Atiyah class of E. The finite étale pullback by [r] is compatible with the Atiyah construction and with its trace. Consequently

    ch_p(E) = [r]^* kappa_p(B) = r^(2p) kappa_p(B),

because det(E) and det(B) are trivial. There is no missing B-field correction: killing only an O^× Brauer class by arbitrary holomorphic cochains would require more care, whereas the mu_r-valued trivialization used here preserves both the determinant and the Atiyah class.

GAGA makes E algebraic if it was initially obtained analytically. Since A is smooth projective, E has the usual integral algebraic Chern classes through its class in K_0(A). Newton identities with c_1(E)=0 give

    ch_2(E)=-c_2(E),
    ch_3(E)=c_3(E)/2,
    ch_4(E)=(c_2(E)^2-2c_4(E))/12.

Hence the multipliers r^4, 2r^6, and 12r^8 are correct. They produce classes in the image of integral Chow groups under the cycle-class map; they do not bound degrees of effective decompositions.

For r=96, a fresh integer calculation gives

    2 * 96^6 = 1,565,515,579,392.

This applies to the fixed determinant-trivial twisted characteristic section kappa_3 and its ordinary isogeny pullbacks. It does not by itself give that denominator for an arbitrarily normalized fourfold Weil class; M6 correctly retains the rational correspondence and coefficient factors.

## FM3. Trace splitting and the genus-four quotient obstruction

The Chern-character product can be checked without assuming local freeness. F_d is perfect on the smooth fourfold, so its derived dual has Chern character obtained by alternating the degrees. For

    ch(F_d)=1+x−(d/2)x^2−(d/6)x^3+(d^2/24)x^4,

the x^4 coefficient of ch(F_d)^vee ch(F_d) is (d^2+d)/3. Since integral x^4=24 and Td(X)=1, its Euler characteristic is 8d(d+1).

G-invariance of the subscheme gives the ideal sheaf its canonical G-linearization. The free translation quotient q:X->Y is finite étale, and descent yields J=I_Zbar with q^*J=I_Z. In characteristic zero the invariants functor is exact, so the descent spectral sequence gives

    Ext_Y^i(J,J) = Ext_X^i(I_Z,I_Z)^G.

Riemann–Roch and etaleness give chi(J,J)=chi(I_Z,I_Z)/(d+1)=8d. Twisting by O(Theta) preserves self-Ext and does not require a G-linearization of O(Theta) to define the transported G action used in this assertion.

For the trace splitting, J is perfect of rank one. The scalar-unit map O_Y -> RHom(J,J), followed by derived trace RHom(J,J) -> O_Y, is multiplication by the virtual rank, which is one. Therefore H^i(O_Y) splits into Ext_Y^i(J,J) for every i. In particular e_1>=4. Rank-one torsion-free simplicity gives e_0=1; Serre duality gives e_4=1 and e_3=e_1. Hence

    e_2 = 8d+2e_1−2 >= 8d+6.

The fourfold semiregularity target has dimension 6+16+6=28. For d>=3, the source has dimension at least 30, so its restriction cannot be injective. Removing the trace summand leaves source dimension at least 8d and target dimension 22, still too large at d=3. At d=3 the full source has dimension at least 102, and the invariant source at least 30; both numbers were freshly recomputed.

These are valid obstructions for the specified ideal seed and its descended sheaf. They do not establish failure for the different partial-normalization complex, an Orlov external-square transform, or every possible genus-four construction. M3 states these limits correctly.

## FM4. Globalization with N fixed before applying Baire

Under the abelian-fibre correction, M2 gives exactly the same N_p at every point of the analytic open. No simultaneous choice of the untwisting cochains is needed. Each resulting integral Chow class admits a finite signed effective representative. Thus the countably many closed bounded-degree loci with this fixed N_p cover the analytic open. Baire and irreducibility force one such locus to be the whole base. This proof invokes the separately checked bounded-Chow lemma; it does not assert boundedness or existence of a global family of the original sheaves.

## FP0–FP3. Checks of the root's quantitative reductions

P0: the flat Lefschetz decomposition of a flat (p,p) class makes its Hodge star flat in cohomology, so its polarized L2 norm is constant. Translation-invariant harmonic representatives have pointwise norm equal to their L2 norm divided by sqrt(V). The comass bound and Wirtinger normalization volume(Z)=degree(Z)/(g−p)! give exactly the stated multiplier inequality. This concerns integral signed cycles and positive integral N; it does not clear arbitrary rational coefficients automatically.

P1: the extreme K-character summands are exactly W. Conjugation makes q0 and R integral rational polynomials; their coprimality gives the stated interpolation projector. It acts algebraically on the fixed cohomological degree through graph correspondences. Pullback by iota(a)^j has cycle-degree multiplier 7^(nj). The assertion of idempotence is correctly restricted to the relevant homological summand.

P2: the graph polarization is I+B^dagger B and its top intersection is n! times its determinant. Both chosen unitary B's therefore have degree n!2^n. Their extreme Weil periods differ by conjugate(omega), giving independent rational Weil projections. On the special-unitary orbit, the class multiplier and degree multiplier of the cleared isogeny are both m^(2n), as stated. General unitary determinant rotation is explicitly retained rather than incorrectly treated as a rational scalar.

P3: W is primitive because wedging an extreme exterior form with the mixed-character polarization is zero. Its middle Hodge–Riemann form is positive and equals the squared L2 norm. Character pairings make the projector orthogonal for the intersection form. The displayed norm bound therefore places delta_n P[Z] in a finite ball of the fixed integral Weil lattice. Multiplication by a^(2n) has no rational eigenline, so v,Tv span W for every nonzero rational v. Clearing finitely many coefficients yields the asserted uniform N and D'.

The nonenumerative determinant formula is also correct. In the positive metric T is an orientation-preserving similarity with complex eigenvalue a^(2n); thus its oriented area with v has absolute value |Im(a^(2n))| ||v||^2. Converting metric area to determinant coordinates divides by sqrt(det G). Since Im(u+v_a omega)=sqrt(3)v_a/2, this gives exactly the stated formula. Coordinate determinants are nonzero integers, and Cramer's rule gives denominator divisibility by d_t times such an integer; the stated least-common-multiple bound follows. If the subset T is empty the conclusion is vacuous and one need not form a maximum over an empty set.

## Independent arithmetic output

The fresh script used pair multiplication (a,b)(c,d)=(ac−bd,ad+bc−bd), representing a+b omega. It evaluated each numerator polynomial by Horner's rule at all lambda_r, rather than importing the root's projector computation. Every extreme evaluation was delta_n and every intermediate evaluation zero; every eigenvalue was distinct. It separately summed absolute coefficients times 7^(nj).

| n | a^(2n) as (1,omega) coordinates | B_n | n!2^n B_n |
|---|---|---:|---:|
| 2 | (39,55) | 3590815550 | 28726524400 |
| 4 | (-1504,1265) | 497657009489489182584908205353846834744 | 191100291643963846112604750855877184541696 |

## Check events for the parent

| ID | Type | Outcome and scope |
|---|---|---|
| M2 | targeted proof check | Full saved proof and active source definition read. Cech mu_r trivialization, perfect determinant, Atiyah naturality, GAGA and Newton denominators checked independently. Passes. |
| M2-N96 | computation or formal certificate (computation only) | Fresh integer evaluation of 2*96^6. Passes. |
| M3 | targeted proof check | Full saved proof and complete genus-four source example read. Derived trace split, quotient Euler scaling, descent invariants, simplicity, Serre duality and target dimension checked. Passes for stated ideal seed. |
| M4 | targeted proof check | Full saved proof read. Passes after stating abelian fibres explicitly; uses separately checked closed bounded-Chow loci. |
| P0 | targeted proof check | Full proof read; flat Hodge star, pointwise norm, volume factorial and multiplier inequality verified. Passes. |
| P1 | targeted proof check | Full proof read; eigenspaces, projector correspondence and pullback degrees verified. Passes. |
| P2 | targeted proof check | Full proof read; graph periods, polarization determinant, independent Weil projections and special-unitary scaling verified. Passes. |
| P3 | targeted proof check | Full proof read; primitive positivity, orthogonality, finite lattice ball, complex multiplication, determinant/Cramer bound and converse verified. Passes. |
| P1/P2 constants | computation or formal certificate (computation only) | Independent integer-pair eigenvalue evaluation and weighted degree sums; all listed constants match. |
| Final check note | targeted proof check | Complete note reread after writing; scope and the M4 correction retained. |

## IR1. Independent check of input regularity 445

The complete note `work/markman_regularity.md` was read. Its strengthened number is correct, as is the earlier weaker bound6763.

For an Abel–Jacobi curve in the embedding X→P26 by3Θ, its Hilbert polynomial is9t−2. Its Gotzmann representation has nine linear terms summing to9t−27 and then25 constant terms, so its Gotzmann number is34. Thirteen pairwise disjoint translates have ideal regularity at most13·34=442: at each stalk at most one of the thirteen factor ideals is nonunit, so their tensor product equals their product and their intersection. Sidman's tensor-regularity proposition applies successively, since every factor is locally free outside a one-dimensional set.

The sheaf i_*O_X(Θ) is3-regular. Its three nontrivial checks are Kodaira vanishing for7Θ,4Θ,Θ; higher groups vanish by support dimension. The higher Tor sheaves of I_(Z/P26) with i_*O_X(Θ) are supported on Z, so Sidman's Proposition1.5 gives regularity at most445 for their tensor product. Its surjection onto i_*I_(Z/X)(Θ) has kernel supported on Z; H^(j+1) of that kernel vanishes for j≥1. Thus the quotient is445-regular.

For completeness, the tensor proposition's cohomological mechanism was independently checked against Sidman's full proof. Tensor a linear locally free resolution of the first regular sheaf by the second. The termwise regularities force the desired hypercohomology to vanish. In the second spectral sequence, a positive-degree cohomology group of the zeroth homology has no incoming differential from positive homological degree; its possible outgoing differentials land in H^(i+r)(Tor_(r−1)), which vanish because those Tor sheaves have support dimension at most1. It therefore survives to zero. This verifies the exact hypothesis used here rather than assuming unrestricted subadditivity of regularity.

The input evaluation kernel is locally free because the curve union is a local complete intersection of codimension2, so its ideal has projective dimension at most1. Its449-regularity also checks: in degree1 the evaluation map requires multiplication surjectivity at twist448, supplied by445-regularity; all higher degrees follow from the long exact sequence and positivity. Direct substitution into27t³+27t²−108t−12 gives N=2,384,568,978 at t=445.

Primary-source check: Sidman, J. (2001/2002), *On the Castelnuovo–Mumford regularity of products of ideal sheaves*, arXiv:math/0110184v2, Lemma1.4, Proposition1.5, Corollary1.6, PDF pp.3–5. The entire proofs of those results were read at https://arxiv.org/pdf/math/0110184, web locator `turn982296028view0`. Gotzmann's regularity theorem is a cited input; the two decompositions were independently recomputed. For the whole union,117 linear terms sum to117t−6669, followed by6643 constants, giving6760 and hence the weaker6763 quotient bound. Neither number assumes a bound for a Fourier–Mukai transform; that separate output calculation is now in `work/markman_output_regularity.md`.

## MOT1. Checked homological Tate-summand lemma

Let A have dimension2n and let W⊂H^(2n)(A,Q) be its primitive rational Weil plane. Let P be an algebraic rational projector with image W in this degree. The assertion is in the category of pure rational motives modulo Betti homological equivalence:

    all classes of W are algebraic
        iff (h^(2n)(A),P) ≅ Q(−n)⊕Q(−n).

For the forward direction choose algebraic codimension-n cycles z1,z2 whose classes w1,w2 form a rational basis. The positive Hodge–Riemann Gram matrix is

    G_ij=(−1)^n∫_A w_i w_j.

It is invertible. Define the algebraic dual cycles by

    z^i=(−1)^n Σ_j (G^(-1))_(ji) z_j.

Then ∫_A w_k cl(z^i)=δ_(ki). The maps from the two Tate summands into the projected motive are given by the projected cycles Pz_i; the reverse maps are the intersection functionals with z^i, composed with P. Their two composites are the identity on the Tate sum and P on the projected middle cohomology. They are therefore identities in the homological category, whose morphisms are defined by quotienting correspondences by their cohomology classes. This proves the isomorphism. Conversely the images of the two Tate basis maps under a motive isomorphism are algebraic cycles spanning W.

The sign (−1)^n in the dual cycles is necessary with the positive Gram convention above. One can equivalently use the unmodified intersection matrix and omit both signs. This statement gives neither an integral splitting nor an effective representative, and it bounds no coefficient or degree.

There is one projector qualification. P1 from the root's polynomial calculation acts idempotently on H^(2n), but need not be an idempotent on the entire cohomology. To define the displayed pure summand one first composes with the algebraic Künneth projector π_(2n). In the homological category that projector is constructed directly, for any integer b>1, by

    π_(2n)=Π_(0≤j≤4n,j≠2n)([b]^*−b^j)/(b^(2n)−b^j),

since [b]^* has eigenvalue b^j on H^j. The two polynomials commute. Alternatively the product correspondence Σ_i z^i×z_i itself gives the desired middle-degree Tate projector. The equality with P is asserted modulo homological equivalence, not rational equivalence.

| ID | Type | Outcome and scope |
|---|---|---|
| IR1 | targeted proof check | Complete input regularity note read; Gotzmann34/6760, disjoint-ideal equality, full Sidman tensor/Tor proof, support-one quotient, and evaluation kernel449 all checked. Both445 and6763 pass. |
| MOT1 | targeted proof check | Complete construction of the two inverse motive maps, Gram sign, pure-degree projection, and converse checked. Passes in rational Betti-homological motives only. |
