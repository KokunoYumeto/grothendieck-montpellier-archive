# Proper-parameter localization and its exact residue limitation

**Status:** unregistered auxiliary research; no main-gate movement is claimed.  
**Author:** GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, run `/root/frobenius_continuation`; inherited effort setting.  
**Written:** 2026-11-19T19:01:30.299663+00:00.

The purpose of this note is to identify precisely what the affine-parameter compactification route proves after C.3bt. It does not identify affine-parameter and proper-parameter equivalence. In particular, a nonzero obstruction below is not a surviving class in the final quotient: other proper families or component-family corrections may remove it.

## 1. Setup and a support-purity statement with a direct proof

Let k be algebraically closed of characteristic p>0, and let E be the projective SNC surface in C.3bt. All groups in this note have rational coefficients. Let P be a smooth connected projective k-curve, B a nonempty finite reduced set of k-points, and U=P\B. Denote by K(E×P on E×B) the actual nonconnective K-spectrum of perfect complexes with the indicated support. For each b∈B the closed immersion

    i_b : E = E×{b} → E×P

is regular of codimension one, so its perfect proper pushforward exists. It gives a natural equivalence

    ⊕_{b∈B} K(E)_Q  →  K(E×P on E×B)_Q.                 (PL.1)

This is not an application of regular-ambient dévissage to the singular scheme E×P. Here is the proof in the precise available SNC scope. Apply the every-degree rational closed-union descent of ET.6/UK.2 both to E×P and to E×U. Finite homotopy limits commute with the fibre defining support K-theory. The support spectrum is therefore the totalization of the corresponding support spectra for the smooth strata E_i, C_e and the individual triple points. On each smooth stratum Y, the scheme Y×P is regular; Quillen dévissage identifies K(Y×P on Y×B) with ⊕_B K(Y). The comparison maps are the actual i_b pushforwards. Their compatibility with all stratum pullbacks follows from the Tor-independent base-change squares: the equations of the parameter fibres lie in the P factor and remain non-zero-divisors on every stratum. Thus these stratum equivalences form a map of the actual coherent descent diagrams, including their geometric nullhomotopies. Their totalization is (PL.1).

For this proof, one may first treat a single b and then use excision for the disjoint supports. Equivalently, on a parameter coordinate chart the same equivalence follows from rational A¹-invariance for this SNC E (itself obtained by closed-union descent from the regular strata), the Bass fundamental theorem, and the elementary zero-section diagram in Thomason–Trobaugh Exercise9.13. The stratum proof above is sufficient and does not assume a purity theorem for arbitrary singular schemes.

Localization now gives an exact sequence of actual groups

    K0(E×P)_Q → K0(E×U)_Q
       --∂_B→ ⊕_{b∈B} K_{−1}(E)_Q
       --Σ(i_b)_*→ K_{−1}(E×P)_Q.                       (PL.2)

Consequently an actual affine-parameter class α extends as a K0 class to the fixed proper product E×P exactly when every residue b_b=∂_b(α) is zero. No assertion about extending an individual representative complex is needed; the relation group is defined using actual perfect K0 classes.

## 2. The Adams weight shift is one, not zero

Set

    V(E) = { e∈K_{−1}(E)_Q : ψ²(e)=2e }.

Suppose α∈K0(E×U)_Q is pure Adams weight two. Its residues in (PL.2) belong to V(E).

To check this without imposing semisimplicity on negative K-theory, work locally at b with a parameter z. Under (PL.1), i_b* is external multiplication by the Koszul support class [O_b]. That support class has Adams eigenvalue two: it is the localization boundary of z, and ψ²(z)=z²=2z in additive K1 notation. Product compatibility gives

    ψ²(i_b*e)=2 i_b*(ψ²e).

Naturality of raw-support localization gives ψ²(i_b*b_b)=4 i_b*b_b for the residue of α. Because (PL.1) is an isomorphism, this implies 2ψ²b_b=4b_b, hence ψ²b_b=2b_b. The argument proves an eigenvector assertion for these residues and uses no decomposition of all K_{−1}(E).

Every residue tuple has sum zero:

    Σ_{b∈B} b_b = 0 in V(E).                            (PL.3)

Indeed exactness of (PL.2) makes its total pushforward to E×P zero. The projection π:E×P→E is proper and perfect, and π_*i_b* is the identity. Applying π_* proves (PL.3).

## 3. Corrections by negative K-classes times parameter units

For e∈V(E) and a unit f∈O(U)^*, nonconnective exterior product gives an actual class

    e ⊠ f ∈ K0(E×U)_Q

of Adams weight two. Its residues are

    ∂_b(e⊠f) = ord_b(f)e.                               (PL.4)

This is the module compatibility of localization, or directly the localization boundary of the unit f on the regular parameter curve followed by exterior product with e. Possible uniform sign conventions can be absorbed into e; fix the convention in which the boundary of a uniformizer is the positive point class.

Let o,t∈U(k). Every component restriction of e vanishes, because K_{−1}(E_i)=0 for a regular component. Hence

    (e⊠f)_t − (e⊠f)_o
       = e·(f(t)−f(o))

lies in the component-map kernel in S(E). C.3bt proves that this endpoint difference belongs to J_K(E). In fact each endpoint product separately lies in that kernel. Thus subtracting these particular open-parameter corrections does not change the final proper-family quotient.

This is the precise way C.3bt interacts with compactification. It permits us to change an affine family by negative-K-times-unit terms. It does not assert that an arbitrary residue tuple can be cancelled by such terms.

## 4. The residual tensor obstruction for this correction method

Choose p0∈P(k). For a pure weight-two α, define

    Ω_P(α) = Σ_{b∈B} b_b ⊗ [O_P(b−p0)]
      ∈ V(E) ⊗_Q (Pic0(P)(k)⊗_Z Q).                   (PL.5)

Equation (PL.3) makes this independent of p0. Enlarging B by points where α already extends does not change it. The tensor is an ordinary abstract tensor of rational vector spaces; no unproved Somekawa or motivic identification is implicit.

If Ω_P(α)=0, then the endpoint difference α_t−α_o belongs to J_K(E).

**Complete proof.** The finitely many residues span a finite-dimensional subspace W of V(E). Choose a rational basis e_1,…,e_r and write b_b=Σ_j n_{jb}e_j with n_{jb}∈Q. Equation (PL.3) gives Σ_b n_{jb}=0 for each j. Since a vector-space inclusion W→V(E) stays injective after tensoring, Ω=0 says that every rational degree-zero divisor

    D_j = Σ_b n_{jb}[b]

has zero image in Pic0(P)(k)⊗Q. Clear the finitely many denominators and then multiply by an integer that kills the resulting finitely many torsion line-bundle classes. There are therefore positive integers N_j and rational functions f_j on P with

    div(f_j)=N_j D_j.

Their divisors are supported in B, so f_j is a unit on U. By (PL.4), the actual correction

    β = Σ_j (e_j/N_j)⊠f_j

has exactly the residues of α. Thus α−β extends by (PL.2) to a class x∈K0(E×P)_Q. Apply the finite Adams-weight-two projector to x. Its two endpoint restrictions are unchanged, because α−β already has pure weight two. This produces an actual gamma-two perfect family on the fixed E×P, so its endpoint difference lies in J_K(E). Section3 puts the endpoint difference of β in J_K(E) as well. Their sum is α_t−α_o, as required.

Conversely, for the restricted class of corrections used in Section3, (PL.4) and the divisor sequence show that the residues can be cancelled if and only if Ω=0. This restricted necessity must not be confused with necessity for belonging to J_K(E): the latter permits many more families and corrections.

## 5. Finite covers do not remove a nonzero Ω

Let f:Q→P be a finite map of smooth connected projective curves and pull α back over Q\f^{-1}(B). Flat pullback gives

    ∂_q(f*α)=e(q/b)b_b  for q over b.

Thus the tensor obstruction is

    Ω_Q(f*α)=(id_V⊗f*)Ω_P(α).                          (PL.6)

The norm of line bundles satisfies Nm_f(f*L)=L^{deg f}. Consequently

    (id_V⊗Nm_f)Ω_Q(f*α)=(deg f)Ω_P(α).

With rational coefficients, nonzero Ω_P therefore cannot become zero merely by finite pullback. This applies equally to inseparable finite maps of smooth curves: they are finite flat, the ramification/length factors are retained, and the norm pull-push formula has the same degree. The statement concerns this particular tensor obstruction, not the final quotient.

## 6. What an affine component graph supplies

Move component zero-cycles away from the double boundary. A point difference on a smooth component E_i can be realized on a smooth projective curve A⊂E_i transverse to all double curves and avoiding triple points. Delete the finitely many boundary-intersection points B⊂A. The graph in E×U, U=A\B, lies in the regular locus of E; it is a closed regular immersion of codimension two there and its structure sheaf, extended by zero, is perfect on all of E×U. Its weight-two projection is therefore an actual affine-parameter family with the required component endpoint point difference.

At a transverse boundary point b mapping to c∈C_e, the residue is the closed-union boundary of the point class [O_c] on that edge, with the sign determined by the incidence convention. This follows from the natural square comparing parameter localization with the two-branch closed-union fibre sequence. All triple restrictions in this local computation are zero by disjoint support, because A avoids the triple points. One can verify the formula by first extending the graph to the smooth component E_i×A: its edge restriction is the point class [O_c]⊠[O_b], and the boundary of that support class is the claimed negative-K residue. The order of the two connecting maps fixes a common sign.

These residues depend on the selected graph A→E_i, not on the two endpoint points in U. Hence Ω is unchanged when those endpoints are changed. In particular, merely asking that their difference be Albanese-trivial on E_i does not supply a proof that Ω=0. The initial support-purity/weight calculation leaves a genuine additional condition to establish.

For a finite sum of graph families, take a smooth proper common parameter curve through the desired endpoint tuples in the product of their parameter curves and remove all preimages of the finitely many boundary points. The sum of the pullbacks gives one actual affine-parameter class. The preceding residue analysis still applies; no proper extension is automatic.

## 7. Remaining routes and exact limitations

The elementary corrections in Section3 account only for principal parameter divisors with constant negative-K coefficients. An actual global affine family on E×U whose component endpoint differences vanish has endpoint difference in the C.3bt kernel, although its component values over U need not be constant; such a correction may alter Ω. A family initially constructed only on the individual components must first be glued over U before its global residues or Ω are defined. Producing enough actual affine corrections of this kind is the unresolved step.

The Poincare construction on A×Jac(A), restricted to a curve in ker(Jac(A)→Alb(E_i)) when the desired endpoint is Albanese-trivial, gives edge classes of the form

    Σ_{q∈A∩C_e} [q]⊠c1(N_q).

Normalizing their component degrees and Albanese coordinates leaves the explicit product-type obstruction already recorded in `agents/real_weil/COMPONENT_ALBANESE_KERNEL_RESEARCH.md`. Calling it a reciprocity pairing does not prove it is zero. No general Somekawa comparison, proper-part localization theorem, or representability assertion is used in this note.

The marked K1 interpolation in C.3bt has a different freedom: it constructs a variable unit g after choosing all relevant divisor supports and prescribes g=1 there. A fixed graph's residues in (PL.2) have already been determined by its boundary intersections. Repeating the marked-unit argument does not by itself vary those residues or the line-bundle tensor Ω.

Neither Ω≠0 nor failure of this compactification method proves nonvanishing of B². For example, C.3bt already kills the final quotient for every allowed rational-component model, including the NP nonzero-period model, regardless of whether a selected affine family extends.

## 8. Primary-source and search audit

The following exact primary passages were freshly opened in this continuation window, rather than inferred from search snippets.

1. **Thomason, R. W., & Trobaugh, T. (1990).** *Higher algebraic K-theory of schemes and of derived categories.* In *The Grothendieck Festschrift*, Vol.III, pp.247–435. Primary full PDF: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf . Fresh read scopes: Theorem7.1 with its complete displayed proof, printedp364; Theorem7.4 with its complete displayed proof, pp365–366; Theorem6.6 and its complete displayed proof, pp361–362; its explicit dependence on Sections6.1–6.4 is retained rather than claiming those whole sections were newly re-read. Also read the full statements and instructions of Exercise9.13, pp381–382, including its zero-section/Nil comparison. Exercise9.13 is an exercise, not a published full proof; the SNC support argument in Section1 above is supplied directly. Theorem7.3 with its short proof-reduction was also read. Exact retrieval references: `turn192510282view0`, `turn192510282view1`, `turn617244643view0`, `turn617244643view1`, `turn617244643view2`, `turn782331468view0`.
2. **Geisser, T., & Hesselholt, L. (2011).** *On relative and bi-relative algebraic K-theory of rings of finite characteristic.* *Journal of the American Mathematical Society,24*(1),29–49. Primary published PDF: https://math.mit.edu/~larsh/papers/025/bounded.pdf . Fresh opening and reading of TheoremsA/C on pp29–30, reference `turn782331468view1`. Their complete previously audited proof scopes and the scheme-gluing argument from ET.6 are reused; no new full-proof reading is claimed here. The theorem is used for the already established rational SNC descent, not misquoted as a general homotopy-invariance statement.
3. The regular-stratum dévissage, localization, projection and Tor-independent base-change inputs reuse the exact Quillen/Thomason–Trobaugh primary-proof audits retained in C.3bq, C.3br and C.3bt. The supported Koszul weight calculation is given explicitly in Section2. The arbitrary-scheme Adams/delooping compatibility is the already audited Levine1994 p258 paragraph preceding Lemma2.1, not that lemma's regular-only ambient statement.
4. The new search block queried the exact phrases “algebraic equivalence” with “K-theory” and “proper”; “perfect complexes” with “algebraic equivalence”; “Chow”, “normal crossings” and “algebraic equivalence”; and “K_0”, “proper curves” and “algebraic equivalence”. Targeted followups used “Levine-Weibel”, “proper parametrization”, “modulus” and “Albanese”. Search output again found Friedlander–Walker’s affine-curve formulation and singular-cycle/motivic comparison papers. No theorem was imported from those snippets. No literature-absence, novelty or priority claim is made.
5. The other component-family researcher reports a fresh complete reading of Kohrita2017v2 §3.4, pp27–32. It gives the proper-parameter algebraic-part definition and universal proper-regular quotient results, but no general localization/exactness theorem for that subgroup. That report is a peer source-scope report, not a new full source reading by this continuation reviewer. The retained exact audit is `agents/real_weil/INTRINSIC_TOP_SOURCE_SCOPE.md`.

No finite computation can establish the general support-purity, residue or tensor arguments above. No program was run to certify them. The note remains unregistered until its owner and independent reviewers decide whether any piece merits incorporation; even a successful audit of this mechanism alone does not meet the main-gate movement criterion.

## Independent audit receipt

At 2026-11-19T19:05:05.356163+00:00, the component-family reviewer reported a complete independent reconstruction of PL.1–6 and mathematical PASS for the full note. The requested clarification in Section7 was adopted: an initially componentwise family requires actual affine gluing before Ω is defined. This is a clarification of the exploratory correction route, not a change to PL.1–6. The full peer receipt is maintained under `agents/real_weil`. Root also reports a full independent reconstruction and PASS.
