# Severn: independent dominance and spreading audit

Run: HECKE_DIV_20261121. Checker: /root/arithmetic, GPT-6 Astra Pro, inherited effort setting not exposed. Date: 21 November 2026. Internal working note for the parent. Read in conjunction with `work/arithmetic.md` (supplier/Brauer audit), `work/severn_monodromy.md` (independent exact monodromy reconstruction), and the root's printed-block checks. This note does not relabel a manuscript as a refereed publication.

## Source and verdict

Severn, B. (2026). *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))* (version 1.5, dated 21 October 2026). Hexagon 2610.00387v2. Primary source: https://hexagonmath.org/api/v1/works/2610.00387v2/source?path=weil-qsqrt3-v1.5.tex . The title and date are taken from the TeX itself, lines 39–44; a listing or prior title should not replace them.

I read Sections 6–9 in full and separately checked the prerequisite moduli/isogeny statements in Section 2. I found no substantive logical failure in the dominance-to-algebraicity argument. This is a targeted proof check, not a formal verification of the whole manuscript. The exact matrices must genuinely arise from the family; their abstract rank and positivity alone would be insufficient. The separate reconstruction reported in `work/severn_monodromy.md` supplies that dependency in this run.

One wording correction is needed: the limiting filtration F0 lies in the compact dual, not necessarily in the open period domain. Accordingly the tangent in `lem:tangentspan` is the tangent of the compact dual at F0. The proof is already an argument in that tangent space, and its rank conclusion at interior points is unaffected.

Exact manuscript labels checked: `subsec:moduli`, `lem:isogeny`; `lem:locus`, `thm:transfer`; `prop:herm`; `lem:gm`, `lem:localmon`, `lem:hodgetate`, `lem:tangentspan`, `prop:boundary`; `lem:g34mult` and the proof of Theorem A. Main source line ranges: 129–152, 328–374, 417–512. Web references opened by this checker include turn625270921view1, turn962517255view0, turn625270921view0 and turn970229550view0.

## SD1. Descent of the Weil plane and the finite-level issue

On a smooth PEL moduli component with a universal abelian scheme f, the K-action on R^1 f_* Q is parallel. Therefore

    W = exterior_K^(2n) R^1 f_* Q

is a rank-two rational sublocal system of R^(2n) f_* Q. Its existence on the quotient does not require choosing a global basis. The determinant representation describes its monodromy.

If a fixed flat rational section is needed, as in the bounded-division problem, one may kill this determinant monodromy by a finite étale cover. Indeed, for an integral lattice-preserving K-linear unitary monodromy element gamma, det_K(gamma) lies in O_K^× and has norm one. Integrality can be seen either on the determinant lattice or by expressing the determinant as a product of algebraic-integer eigenvalues of the integral Q-matrix; the inverse is integral as well. The unit group of an imaginary quadratic field is finite. Thus ker(det_K) has finite index. A connected finite covering of the smooth quasi-projective moduli component is algebraic and étale, and W becomes constant there. This is a sufficient argument independent of whether the particular principal congruence level already kills every root of unity.

For the manuscript's claim that all of W is algebraic, even this extra cover is unnecessary. Inclusion of a sublocal system in the span of specified flat cycle classes is invariant under transport, as used below.

The lattice used to present the moduli space is O_K-stable. An individual abelian variety whose K-action is only rational need not have that lattice. Landherr's classification gives a rational K-isometry to the fixed Hermitian space; clearing lattice denominators produces a K-linear isogeny to a fibre of the fixed family. Pullback and pushforward of cycles preserve rational algebraicity and carry its Weil plane isomorphically. Thus the passage to one moduli family does not silently assume maximal-order integral multiplication on every abelian variety under discussion.

## SD2. The countable closed-locus and Baire argument

The argument in `lem:locus` is valid for the full Weil plane, despite the absence of a globally fixed basis on the initial quotient. For each finite tuple of components of relative Hilbert schemes, take an irreducible component T of their fibre product over the moduli space and a proper resolution Ttilde -> T. The universal subschemes remain flat after this base change. Their fibre cohomology classes are global flat sections of the pullback local system. Their rational span F is therefore a sublocal system of constant rank.

On connected Ttilde, the condition W subset F is constant: parallel transport preserves both subspaces. If it holds somewhere, it holds everywhere. The proper image of a good Ttilde is closed algebraic. Every fibre with algebraic W belongs to one such image, because finitely many algebraic cycles span its two-dimensional Weil space. There are countably many tuples of Hilbert polynomials and finitely many irreducible components for each chosen finite-type scheme. Hence the algebraicity locus is a countable union of closed algebraic subsets.

In `thm:transfer`, dominance supplies an actual analytic open ball in the period-domain image. Over a simply connected source polydisc the rational Hermitian local system is marked. Its integral lattice is locally constant, so after comparison with the fixed target lattice it is commensurable with it; clearing denominators gives the required fibrewise K-linear isogenies. Algebraicity therefore holds on an analytic open subset of the target moduli component.

An analytic open subset of a complex manifold is a Baire space. If a countable collection of closed algebraic subsets covers it, at least one has interior there. In an irreducible algebraic variety a closed algebraic subset with analytic interior is the whole variety. Thus all fibres have algebraic Weil classes. This uses an open image, not merely analytic or Zariski density. All intermediate properness and connectedness requirements are present.

The same conclusion, after killing determinant monodromy and fixing the polarization, feeds the root's closed bounded-complexity loci and gives an existential uniform bound for each fixed rational flat Weil section. It does not extract a numerical least degree or denominator.

## SD3. The seventeen curves are a simultaneous maximal boundary

The distinction between a family of commuting matrices and a genuine simultaneous normal-crossing degeneration is essential. I independently checked the printed intervals combinatorially. They are

    [1,8], [1,18], [2,8], [3,8], [4,8], [5,6], [5,8], [7,8],
    [9,10], [9,12], [9,16], [9,17], [9,18], [11,12], [13,14],
    [13,16], [15,16].

They are pairwise nested or disjoint, essential (each side has at least two punctures), distinct, and no pair describes complementary copies of the same sphere curve. There are 17 = 20−3 of them. Adding the twenty singleton leaves and the root cluster [1,20] gives a tree in which every internal component has exactly three special points, counting its parent when present. Thus these curves can be realized simultaneously disjoint and define a trivalent stable 20-pointed rational curve. The independent output is `work/severn_boundary_tree_check.json`.

There are consequently seventeen independent smoothing coordinates near the boundary point of the moduli space of ordered branch points. A loop around each coordinate is the corresponding Dehn twist. The finite Hurwitz covering over the punctured polydisc is killed by a sufficiently divisible Kummer base change; since the individual return powers fix the tuple, their direct-sum sublattice is in the stabilizer. These are simultaneous statements about a single local covering, not seventeen unrelated one-parameter degenerations.

An unmarked G-cover may contribute a coefficient automorphism. Once a braid returns the generating tuple exactly, that automorphism centralizes all its entries and is central in G. On the irreducible K-representation it acts by a root of unity; a further positive power kills it. Marking a point over an exterior base point also kills this ambiguity. Taking further positive powers to kill the semisimple parts rescales logarithms by positive integers.

The sign relating all local coordinate loops to the chosen twist convention is common. In complex plumbing coordinates, a positive loop rotates the corresponding cluster in the same complex orientation for every node, including nested clusters. Reversing the chosen loop convention reverses all logarithms. One does not have independent sign choices for different nodes. This is precisely what is required to retain the definite positive cone in the argument.

The nilpotent-orbit theorem only needs the resulting polarized variation on the punctured polydisc with unipotent monodromy; no claimed special extension of the abelian scheme over its centre is required.

## SD4. Nilpotent normalization and the Hodge–Tate limit

Use M_j = log(T_j), with T_j now denoting the actual unipotent local monodromy, and u_j = exp(2 pi i z_j). The relation F(z+e_j)=T_j F(z) gives

    F(z) = exp(sum_j z_j M_j) psi(u).

There is no missing factor 2 pi i in the exponent with this definition of M_j. Such a factor would occur only with the alternative convention N_j=(2 pi i)^(-1) log(T_j). Schmid's several-variable nilpotent orbit theorem makes psi holomorphic into the compact dual at u=0.

Assume the geometric logarithms are M_j = epsilon c_j N_j, with c_j positive, and H1–H3 hold. For any positive coefficients a_j, M=sum a_j M_j kills I and has image in I. If x is nonzero in V/I, then

    S(x,epsilon Mx) = sum_j a_j c_j beta_j(x,x)

is nonzero: the beta_j are semidefinite of one sign, and their sum is definite. Hence M:V/I -> I is injective and therefore bijective. In particular im(M)=ker(M)=I and M^2=0. The monodromy filtration centred at weight one is W_0=W_1=I, W_2=V.

For the tangent argument, it suffices to take all a_j=1 and restrict the actual variation to the diagonal punctured disc. Schmid's one-variable limiting mixed Hodge theorem then gives the mixed Hodge structure (W,F0); the multivariable cone statement in CKS is stronger than needed here. The effective weight-one filtration has F0^0=V_C and F0^2=0, since those equalities persist in the compact dual. Thus pure Gr_0 can only have Hodge type (0,0), while pure Gr_2 can only have type (1,1). Consequently F0^1 intersects I_C trivially. In either selected K-eigenspace both subspaces have dimension n and

    V_C = I_C direct_sum F0^1.

This supplies the sometimes implicit effectivity justification behind the source's statement that the two graded pieces are Hodge–Tate. It is not true merely from the word 'weight one' without using the actual Hodge-filtration bounds; those bounds are available here.

Primary interfaces checked directly: Schmid (1973), Theorem (4.12), printed p.233, for the several-variable holomorphic extension; Theorem (6.16), printed p.255, for the limiting mixed Hodge structure. PDF: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/schmid.pdf . Web refs turn924360329view0, turn428414855view0 and turn428414855view1. Also checked the equivalent nilpotent-orbit/polarized-MHS interface in Cattani and Kaplan (1989), Theorem (3.13), printed p.80: https://www.numdam.org/item/AST_1989__179-180__67_0.pdf , refs turn924360329view1 and turn428414855view2. These are citations of established results, not independent proofs of their analytic theorems.

## SD5. Why rational rank sixteen gives complex tangent rank sixteen

In general Q-linear independence of matrices with entries in K does not imply their C-linear independence in one embedding. The extra structure here supplies exactly the missing inference.

Let n_I consist of K-linear infinitesimal unitary maps X with X(V) subset I and X(I)=0. Since I is maximal isotropic, the perfect pairing between V/I and I identifies

    X |-> [ (x,y) |-> S(x,Xy) ]

with the rational vector space of Hermitian forms on V/I. That space has n rational diagonal parameters and two rational parameters for each upper-diagonal pair, hence Q-dimension n^2. The logarithms lie in it because they are logarithms of unitary monodromy and satisfy the image/kernel conditions.

Under a chosen embedding K -> C, the complexification of the Hermitian-form space is all n-by-n complex matrices: diagonal matrices, real symmetric off-diagonal matrices, and the purely imaginary skew off-diagonal matrices form a real basis whose complex span is full. Equivalently, n_I tensor_Q C maps isomorphically to Hom(V_C/I_C,I_C). Thus H4 gives the required complex span, rather than merely a formal scalar-extension assertion about arbitrary Q-independent vectors.

Using V_C=I_C direct_sum F0^1 identifies this last space with

    Hom(F0^1,V_C/F0^1),

the n^2-dimensional tangent space of the compact dual. An X with zero tangent at F0 would carry F0^1 into F0^1 intersect I_C=0 and kill I_C, hence would be zero. Therefore the logarithmic tangent vectors span all this tangent space.

Translate the derivative of F(z) by exp(−sum z_jM_j). Its jth column is

    M_j . psi(u) + 2 pi i u_j (partial psi / partial u_j).

The second summand tends to zero and the first tends to M_j . F0. Choose n^2 independent limiting columns and a Grassmannian coordinate chart near F0. Their minor remains nonzero for all sufficiently small interior u. Translation is a complex-group automorphism of the compact dual, so it preserves differential rank. Also dz_j/du_j is nonzero in the punctured interior. Hence the actual period map has full complex rank n^2 there. For n=4 this is rank sixteen. Finally, the rational Lagrangian I makes the Hermitian discriminant split.

## SD6. Responsible use of Theorem A

The target assertion of Theorem A is exactly all Weil classes for split K=Q(sqrt(-3)) abelian eightfolds; it is not a statement about arbitrary eightfold Hodge classes or arbitrary imaginary quadratic fields. Sections 4–5 were separately checked in `work/arithmetic.md`, including Schoen's needed local repair and Milne's full possibly disconnected Lefschetz-group interface. Sections 6–9 have the targeted proof check above. The exact group and boundary computation has now been reconstructed by the other checker from the printed roots, cocycle basis and twist formulas, rather than merely accepted from the abstract.

At that combined scope, it is responsible to cite Theorem A as a checked manuscript input, with the manuscript version and the actual checks stated. It is not responsible to call it a refereed theorem, a machine-verified proof, or a numerical bound for cycle complexity. The classical deep inputs remain cited inputs. The supplied source was accessible; the separate optional 84-row supplier table was not needed because integral Brauer induction supplies the existence statement.

No GRH premise enters this geometric proof. Its application to the corrected closed bounded-complexity loci gives qualitative existence of a finite uniform C for each fixed flat Weil section on the fixed polarized family. Neither the source nor this audit determines an explicit numerical C or the least denominator. Quantitative extraction remains a separate task.

## Actual check events

All events below occurred on 2026-11-21 in HECKE_DIV_20261121 by /root/arithmetic, GPT-6 Astra Pro, effort unspecified.

| ID | Type | Scope and outcome |
|---|---|---|
| SD1 | independent re-proof | Determinant monodromy finite; finite étale cover trivializes W. Explicitly separates whole-plane descent from a chosen global section. Passed. |
| SD2 | targeted proof check | Complete reading of `lem:locus` and `thm:transfer`; proper Hilbert images, flat span, Baire/open-image logic, and isogeny transfer checked. No fault found. |
| SD3a | computation or formal certificate (computation only) | All seventeen intervals checked for laminarity, essentialness, distinctness and trivalent cluster tree. JSON output saved. Passed. |
| SD3b | targeted proof check | Complete reading of `lem:gm`/`lem:localmon`; simultaneous Kummer cover, central ambiguity and common orientation reconstructed. No fault found. Exact cocycle matrices delegated. |
| SD4 | independent re-proof | Positive cone gives im=ker=I; diagonal limiting MHS plus effective filtration gives complement F0^1. Passed using cited Schmid input. |
| Schmid interfaces | used and rechecked in this run | Exact primary statements (4.12) and (6.16) opened and read, including normalizations. No independent analytic proof claimed. |
| Cattani–Kaplan interface | used and rechecked in this run | Theorem (3.13) opened and read as a second primary formulation. |
| SD5 | independent re-proof | Hermitian real form dimension and complexification, tangent injectivity, normalized derivative and nonzero-minor argument checked. Passed; compact-dual wording corrected. |
| SD6 | targeted proof check | Full Section 9 deduction read after the above checks. It reduces to the audited supplier chain and independently reconstructed geometric certificate. No further logical gap found. |
| This note | targeted proof check | Entire note read sequentially after writing; scope exclusions and source locators reviewed. |

## References

Cattani, E., & Kaplan, A. (1989). Degenerating variations of Hodge structure. *Astérisque, 179–180*, 67–96. Theorem (3.13).

Schmid, W. (1973). Variation of Hodge structure: The singularities of the period mapping. *Inventiones Mathematicae, 22*, 211–319. Theorems (4.12), (6.16).

Severn, B. (2026). *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(-3))* (version 1.5; Hexagon 2610.00387v2). Sections 2 and 6–9; Appendix A intervals. Unrefereed manuscript status is retained.
