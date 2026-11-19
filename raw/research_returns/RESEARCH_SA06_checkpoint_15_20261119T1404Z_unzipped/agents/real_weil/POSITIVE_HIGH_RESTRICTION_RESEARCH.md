# Remaining higher ordinary restriction in positive characteristic

Research note, 2026-11-19. Owner: `/root/real_weil`.
**Status: no new proved restriction theorem or counterexample in the remaining high ranges.** This note records the precise source input, unsuccessful reductions, and the missing step. It is not a statement-register entry and does not count as main-gate movement.

## 1. Exact remaining range

For codimension r>=2, the paper has explicit rational ordinary restriction kernels for r+1<=N<=2r (C3aw/ay), and rational ordinary restriction-surjectivity failures for r+2<=N<=2r+1 (C3at/av), over specified transcendental algebraically closed extensions of Fpbar. The unresolved universal high ranges are therefore injectivity for N>=2r+1 and surjectivity for N>=2r+2. The ordinary subgroup is defined by actual fixed-product curve families. Over Fpbar itself all ordinary algebraically trivial classes are torsion; their rationalization is zero. An example over a transcendental algebraically closed extension is needed for a rational failure.

C3as/ba/bb give additive exponent-p quotients of the quotient by ordinary algebraic equivalence. They kill the ordinary subgroup by its p-divisibility. They therefore cannot supply any of the remaining rational ordinary kernels or cokernels.

## 2. The exact formal weak Lefschetz input

**Opened primary source:** Morrow (2019), *K-theory and logarithmic Hodge-Witt sheaves of formal schemes in characteristic p*, Annales scientifiques de l'ENS 52(6),1537--1601, DOI10.24033/asens.2415. Full published PDF:
https://www.numdam.org/item/ASENS_2019__52_6_1537_0.pdf

Freshly read: §6.5 p1593, Theorem6.18 and its complete proof pp1597--1598, Remark6.19 p1598; also Theorem0.7 and the hypotheses of Theorem0.1.

For X smooth projective of dimension d over a perfect field of characteristic p and Y a smooth ample divisor, Theorem6.18 proves that

    lim_s H^i_Zar(Y_s,K_n) -> H^i_Zar(Y,K_n)

has kernel and cokernel annihilated by a power of p if i+n<d-1. In particular its cohomological Chow version is an isomorphism after inverting p for 2n<d-1. Section6.5 explicitly defines CH^n(Y_s)=H^n_Zar(Y_s,K_n); on the nonregular thickenings these are not the usual groups of cycles. The proof uses continuous cohomology and controls the relevant lim^1 term. It supplies neither actual cycles on X nor an actual family on X times a proper parameter curve.

**Inference for the present problem.** Even in a smooth projective ample-divisor reduction, the remaining map from actual Chow classes to the formal cohomological system must be analyzed separately. Moreover, the arbitrary strictly local pair in the question does not automatically come from the ample-divisor setup of this theorem. Neither hypothesis should be suppressed.

## 3. Compatible K0 classes versus an algebraized object

**Opened primary source:** Morrow, *A Variational Tate Conjecture in crystalline cohomology*, author PDF,30pages:
https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow,%20M.,%20Variational%20Tate.pdf
Published metadata independently checked at https://ems.press/journals/jems/articles/16358 : JEMS21(11)(2019),3467--3511, DOI10.4171/JEMS/907. The theorem numbers and page locators below refer to the opened author version, not an uninspected published PDF.

Read Theorem0.6/3.3 and Corollary3.4 with proof, author pp3,18--20. Over a smooth proper scheme over k[[t1,...,tm]], the all-codimension theorem characterizes lifting a special-fibre K0 class to (lim K0(Y_s))[1/p] by a crystalline Chern-character condition. Corollary3.4 gives an actual Picard-group lift, using the separate algebraization isomorphism Pic(X)=lim Pic(Y_s). The author explicitly identifies this as the extra step for line bundles. The higher-codimension theorem does not assert K0(X) surjects onto lim K0(Y_s), or that arbitrary compatible classes admit compatible bounded-rank bundle representatives.

**Inference.** Proper formal GAGA is an equivalence for compatible coherent objects; a compatible sequence of their Grothendieck-group classes is different data. One cannot invoke that equivalence before constructing the required compatible objects. Even after producing a K0 class, preserving ordinary equivalence requires an actual family over the fixed proper parameter curve, rather than separate pointwise lifts.

## 4. Why the existing successful constructions do not immediately extend

### 4.1 Absolute differential detector

The complex C3ao construction uses absolute differential forms from the coefficient field. For an algebraically closed field k of characteristic p, every element is a pth power and therefore Omega^1_(k/Fp)=0. Its absolute differential detector vanishes after perfection. A characteristic-p square-zero conormal invariant can instead be additive p-torsion, as in C3as, but then divisibility annihilates every ordinary class and rationalization removes the detector. This is a coefficient obstruction, not an omitted sign or normalization.

**Stronger exact obstruction to the literal product construction (checked 2026-11-19).** Suppose an actual divisor class a on the regular puncture satisfies p^e a=0, and let lambda be an ordinary algebraically trivial class for which the intersection product is defined. Ordinary algebraic equivalence through actual proper-curve families is p^e-divisible: represent lambda as a finite sum of correspondence images of degree-zero divisors on smooth proper curves, use surjectivity of multiplication by p^e on their Jacobians over the algebraically closed field, and push the resulting preimages forward through the same actual families. Thus lambda=p^e mu for another ordinary class mu, and

    a · lambda = a · (p^e mu) = (p^e a) · mu = 0

**integrally**. In particular, if the nil-Pic class in a characteristic-p analogue of C3ao is p-primary torsion, its product with the first Pic0 factor already vanishes; multiplying further factors cannot repair this. The cone rigidity theorem C3ax implies exactly this p-primary property for a divisor class restricting trivially to the exceptional divisor. This argument does not merely say that the differential detector or rationalization loses the class: it says that the proposed ordinary product class itself is zero. It does not assert that every possible characteristic-p ordinary restriction kernel is zero.

### 4.2 Frobenius and coherent deformation bounds

At each fixed nilpotent order, a Frobenius power can annihilate suitable deformation obstructions. This does not provide one power valid at all orders for an arbitrary vector-bundle family. Replacing a bundle V by Frob^{e*}V changes End(V), and the Serre-vanishing threshold for End(Frob^{e*}V) can depend on e. No uniform estimate was obtained here. The successful line-bundle family argument in C3az uses End(L)=O, which is independent of L and permits a fixed finite obstruction range. That step has not been established for higher Chow-family representatives.

### 4.3 Critical incidence example times a projective space

The C3ay relation comes from a regular zero scheme of rank r-1 on its incidence divisor; the zero scheme maps to finitely many points of the elliptic curve, so the chosen Pic0 class restricts trivially there. Increasing the ambient projective factor while retaining codimension r generally makes that base/zero scheme positive-dimensional over the elliptic curve. The Pic0 class no longer restricts trivially, so the crucial annihilator relation is lost. Taking a section independent of the new factor either fails ampleness/isolated-cone requirements or fails to retain the required regular puncture. No high-dimensional kernel follows from that product operation.

There is a precise dimension obstruction for the same elementary annihilator method. Let T have dimension t, let A be ample, and use m+1 sections to form an incidence divisor in P^m times T. A class obtained from the regular rank-m zero locus has the form A^m lambda in codimension r, so lambda has positive codimension c=r-m and m<=r-1. If the sections have no common zero, they define a finite morphism T to P^m: any positive-dimensional fibre would contain a curve on which A has degree zero. Therefore t<=m and the local cone dimension N=m+t+1 is at most 2r-1. If their regular base locus B has codimension m+1, the sufficient condition that lambda restricts to zero on B simply by dimension is

    dim B = t-m-1 < c = r-m,

equivalently t<=r. This gives N<=2r. Thus extending this construction into N>=2r+1 requires a genuine new restriction-vanishing assertion for lambda on the positive-dimensional base locus; dimension and the top-Chern identity alone cannot supply it. This is a limitation of this method, not a universal positive Lefschetz theorem.

### 4.4 Prime-to-p torsion and algebraic representatives

The local étale Lefschetz theorem controls finite covers and certain prime-to-p torsion. It does not, on its own, show that the kernel of a homomorphism from Jacobian points to an arbitrary higher Chow group is the point group of a closed subgroup scheme. Higher ordinary cycle groups need not have the degree-one local Picard representability used in C3n/w/z. Consequently density of prime-to-p torsion is not by itself a proof of the high-codimension rational restriction assertion.

### 4.5 Families on henselized products

Finite-presentation descent gives a cycle or bundle on an étale neighborhood of a henselized product. It does not automatically give a cycle on the fixed ordinary product. Compactifying a parameter curve and applying Zariski Main can introduce extra finite branches; a trace/norm argument has to control their cycle contributions at both parameter values. No such general higher-cycle transfer was proved here. The local Picard construction and the actual-family proof in C3w must not be promoted to an unproved higher Chow statement.

## 5. A higher-rank restriction theorem and its exact limit

The published Bhatt--de Jong paper was freshly reopened through
https://www.numdam.org/item/10.24033/asens.2228.pdf
(The older Numdam filename URL returned an access error.) Theorem0.2, printed p834, states: a vector bundle on a normal projective variety of dimension at least three in characteristic p that is trivial on an ample divisor becomes trivial after sufficiently high Frobenius pullback.

This controls an actual bundle with an actual trivialization after restriction. A zero element in a higher Chow group, or in K0 of the divisor, is not such a trivialized bundle. Converting arbitrary K0 relations into that input would require an additional argument; the theorem is not used here as a blanket injectivity statement for K0 or Chow groups. Existing bibliography key: D_BhattDeJong2014.

## 6. Actual divisor-family lifting on a smooth exceptional divisor

The following is a direct extension of the already audited line-bundle argument in C3az, useful for excluding another proposed counterexample method. It is not a claim about arbitrary higher cycles and is not counted as a separate main-gate advance.

Let R be an excellent henselian local k-algebra in characteristic p, with residue field k, and let Z be projective over R. Suppose the entire reduced closed fibre is a smooth effective Cartier divisor E with ample conormal L=O_Z(-E)|_E. For a **smooth proper curve** P/k and an actual line bundle F on E×P, some finite p-power F^{p^e} is the restriction of an actual line bundle on Z×P. The exponent can be bounded in terms of E,L alone. The curve-parameter hypothesis is essential to the proof.

Indeed, put E_n=V(O_Z(-nE)). The square-zero ideal of E_n×P in E_{n+1}×P is L^n boxtimes O_P. The Picard obstruction is in

    H²(E×P, L^n boxtimes O_P)
      = H²(E,L^n) tensor H⁰(P,O_P)
        ⊕ H¹(E,L^n) tensor H¹(P,O_P).

Serre vanishing makes both summands zero for all n>=n0, for one n0 depending only on E,L. Before n0 each obstruction group has exponent p; the obstruction homomorphism sends the pth tensor power of a partial lift to zero. Successively taking pth powers at these finitely many stages produces a compatible system restricting to F^{p^e}, e<=n0-1. Beyond n0 every step lifts without a further power. There is no unbounded exponent hidden in this construction.

The E-adic and closed-fibre-adic topologies are cofinal. Proper formal existence over the complete ring Rhat algebraizes the resulting compatible line bundle, together with its inverse, on Z_Rhat×P. The regular completion map R→Rhat is a filtered colimit of smooth R-algebras by Popescu. Finite-presentation descent puts the algebraized line bundle on one Z_A×P. The residue map A→k lifts to A→R because R is henselian and A is smooth. Pullback along this lift gives an actual line bundle on Z×P with the prescribed F^{p^e} restriction. Every parameter in this argument remains the fixed actual curve P.

The exact source inputs and their hypotheses are those freshly checked in C3az Step3: Stacks Lemma37.4.1 (Picard obstruction), Lemma30.24.3 (proper formal existence), Lemma15.51.14 (regular completion), Theorem16.12.1 (Popescu), Lemma32.10.3(2) (limit descent of line bundles), and Lemma15.13.3 (smooth henselian lifting), together with coherent Künneth and Serre vanishing. Frobenius independently checked this extension and explicitly confirmed the curve-parameter restriction.

In the algebraizable regular-resolution setting where the C3az K-theory argument gives K0(Z)[1/p]→K0(E)[1/p] injective, determinant consequently makes Pic(Z)[1/p]→Pic(E)[1/p] an isomorphism. The actual family lifting also identifies their ordinary Picard subgroups after inverting p. Using the rational Chern character in that same stated setting, the divisor-generated rational Chow subrings are identified, and products having an ordinary Pic0 factor lift as actual ordinary cycle families. Thus replacing a complex obstruction by an exceptional K3-divisor class times a Pic0 class cannot produce a rational obstruction here merely from failure of that divisor or Pic0 family to extend.

For a higher-dimensional parameter P there is an additional summand H⁰(E,L^n) tensor H²(P,O_P), which need not vanish. No uniform arbitrary-parameter lifting is asserted. More importantly, a general ordinary higher cycle is not necessarily a product of divisor classes on E. Lifting its supporting correspondence, rather than just these line-bundle factors, remains the substantive gap.

## 7. Search record and precise stopping point

Queries included local Lefschetz with Chow/positive characteristic; Chow groups and absolute integral closure; algebraically trivial higher cycles and Lefschetz; formal K0 algebraization and variational Tate. Both search systems were used; conclusions here rely only on the primary PDFs above, not snippets or secondary discussions. The accessible results give the formal half and specific line-bundle/vector-bundle cases. No claim is made that this search proves absence of later work.

Retained download program and timings: `code/fetch_higher_restriction_sources.py`, its `.out`, and `output/higher_restriction_sources_manifest.json`. New bibliography entries are in `higher_restriction_references.bib`.

The current proof gap is concrete: construct or obstruct actual higher cycle families on the strictly local puncture while retaining their prescribed restriction, with one finite rational denominator. Formal existence, p-adic compatible classes, and an additive exponent-p detector do not settle that problem.

## 8. What surface reduction does and does not prove for the ordinary top quotient

Let R be an excellent henselian local domain of dimension N>=2 with an algebraically closed coefficient field k mapping isomorphically to the residue field. Set X=Spec(R) minus its closed point. For each prime q with dim(R/q)=2, let T_q be the finite normalization of R/q and let U_q be its puncture. The normalization is a henselian local domain, with residue field k; it is a normal surface and U_q is regular. Every prime p with dim(R/p)=1 contains such a q, by catenarity. A prime P of T_q over p/q has height one, and the finite map U_q→X pushes [P] to the positive finite multiple [kappa(P):kappa(p)] [p]. Hence the direct sum of these proper pushforwards is surjective:

    direct_sum_q CH¹(U_q)_Q -> CH^{N-1}(X)_Q.

This assertion also descends to the quotients by ordinary algebraic equivalence. Indeed a finite map U_q→X times the SAME smooth proper parameter curve is proper; pushforward of the actual cycle family commutes with the refined restrictions at the two parameter points. The identity follows directly from the proper-pushforward/divisor formula, or from its Cartesian refined-pullback version. No henselized parameter product or pointwise algebraization is substituted. Thus

    direct_sum_q B¹(U_q)_Q -> B^{N-1}(X)_Q

is surjective in this coefficient-field setting. This gives a genuine reduction, but not a general vanishing theorem.

Over k=Fpbar, the surface terms vanish rationally: the strengthened C3be proof uses finite K0 detection, nilpotent invariance, determinant, and the negative exceptional intersection matrix to prove this for arbitrary excellent henselian normal surfaces, including mixed characteristic. This agent's complete independent proof/source audit passed at12:54:25UTC; the separate detailed review and canonical check events are in `C3be_surface_reduction_independent_REVIEW.md` and its matching event file. The Chow pushforward argument then avoids resolutions in the ambient dimension entirely. The resulting ambient theorem allows any excellent henselian local domain; normality of the ambient ring is unnecessary.

**Supersession of the preceding dated scope.** The final certified C3be
uses the entire finite semilocal normalization and proves the assertion
for **every excellent local domain with residue field Fpbar**, including
mixed characteristic. Henselianity is no longer an assumption. The
preceding12:54:25 assessment is retained only as audit history; the
same-ID nonhenselian refinement was independently passed at13:06:03UTC,
as recorded below and in the dedicated review.

For a transcendental algebraically closed k, C3y already supplies a normal surface with B¹(U)_Q containing k* tensor Q. Therefore one cannot finish the general top-quotient problem by declaring every surface Picard class ordinarily algebraically trivial modulo exceptional divisors. In a general reducible exceptional curve, the connected Picard group is semiabelian, and its torus extension need not split up to isogeny over such a field. The proper abelian images relevant to actual ordinary families must not be replaced by the whole connected Picard functor. Establishing that the pushforwards of the remaining surface classes vanish in a higher-dimensional ambient puncture is an additional assertion, not a consequence of the displayed surjection.

The separate Frobenius note `C3_SNC_energy_lemma.tex` proves a useful but limited statement when a projective SNC exceptional divisor of dimension d>=2 has an ample negative exceptional combination: the degree-unit double-stratum K1 restriction map is surjective, by an explicit weighted intersection identity. Thus preserving a dual-complex loop does not preserve that gluing obstruction. Higher-stratum classes, their lifting from K0(E) to K0(Z), and actual proper-curve family relations on Z remain separate questions. For coefficient Milnor K_a(k) with a>=2, the explicit proper-curve K2 construction in `TOP_QUOTIENT_RESEARCH.md` eliminates symbols under ordinary K-theoretic evaluation; it does not by itself lift the resulting relation to an actual Chow family on Z.

The exact newly opened source locators for the surface reduction are Stacks54.14.5 Tag0BGP (arbitrary excellent normal surface resolution), 54.15.6 Tag0BIC (embedded SNC by point blowups), 36.38.5 Tag0FDJ and 17.26/17.26.1 Tag0B37 (K0 and determinant), 15.106.23 Tag092X (integral domains over henselian local rings), 42.19.3 Tag02RX and 42.20.3 Tag02S2 (localization and proper pushforward), KST TheoremA/(1.6) authorpp2–3, and Geisser–Hesselholt TheoremA printedp29. The last theorem assumes p is nilpotent, so it applies on each finite closed-fibre thickening even if the ambient local ring has mixed characteristic. The known finite-type surface statement is Tanaka (2014), Theorem4.5 printedpp42–43; Esser (2023), Theorem2.4 proof in the clean five-page author PDF pp4–5, explicitly proves torsion of the henselian local class group. The six-page annotated Esser file has a different pp5–6 locator and is not silently identified with the clean version.

**Same-ID refinement, fully audited at13:06:03UTC.** C3be now removes henselianity. The surface proof never used it. The finite normalization of a general surface quotient is semilocal; a common multiple of each Weil divisor is Cartier at every maximal localization, hence globally, and Pic of a semilocal ring is zero. Freshly checked Stacks02M9,0EBM,02JW and02SI supply exactly this argument and its inherited Chow indexing. The optional extension from Fpbar to any algebraic extension of Fp has only been noted as a follow-up; it is not part of the presently certified statement.

## 9. A finite support-lifting obstruction for restriction in characteristic p

This records the precise K-theoretic reduction proposed by the parent and checked here. It is not a solution of the high-codimension question and is not a new numbered result.

Let R be a noetherian local Fp-domain, let Z→Spec(R) be projective with Z regular and with an isomorphism off the closed point, and let E be the reduced exceptional fibre. Put X=Z−E. For 0≠f in the maximal ideal set D=Z×_R R/(f), and suppose Y=D−E is regular. No henselianity is needed for the following argument. Write j:D→Z and i:E→Z. All K groups in this paragraph are perfect-complex K groups; G0 denotes coherent K theory.

The enlarged centre V(f) still gives an abstract blowup square, since Z→Spec(R) is an isomorphism away from that centre. KST TheoremA and(1.6) give

    K0(R) → {K0(R/f^b)}_b ⊕ K0(Z) → {K0(D_b)}_b,

where D_b=Z×_R R/(f^b). Both local base-ring K0 groups are Z, and quotienting the diagonal graph yields a pro-monomorphism from the constant group K0(Z). Its decreasing kernel system has inclusion transition maps, so one finite b detects K0(Z). For that finite b, GH TheoremA and finite affine Zariski descent identify K0(D_b)_Q with K0(D)_Q: the immersion is nilpotent and p=0 on every affine chart. Consequently j*:K0(Z)_Q→K0(D)_Q is injective. The finite detecting level is important: no uniform p-exponent over an infinite tower is asserted or needed for this injection.

G-theory localization on regular Z gives

    G0(E)_Q --i_*--> K0(Z)_Q → K0(X)_Q → 0.

Perfect-complex localization on D gives

    K0(D on E)_Q → K0(D)_Q → K0(Y)_Q.

Therefore, identifying K0(Z)_Q with its image under j*, the restriction kernel is precisely

    ker(K0(X)_Q → K0(Y)_Q)
      ≅ ( j*K0(Z)_Q ∩ im[K0(D on E)_Q→K0(D)_Q] )
          / j*i_*G0(E)_Q.

The denominator is indeed contained in the numerator: exceptional classes vanish on Y. Both directions follow by choosing a lift in K0(Z), using exactness on D, and changing the lift by i_*G0(E). Thus the issue is a finite support-lifting problem on the whole singular fibre D, not failure to detect a class at any finite infinitesimal order.

The numerator cannot be silently replaced by coherent classes on E. A supported perfect class on the generally singular D has additional perfect-complex information; the map K0(D)→G0(D) need not be injective. Derived restriction of an exceptional coherent sheaf involves Tor terms, so replacing it by its ordinary sheaf restriction also changes the problem. No argument has shown that every class in this intersection is the restriction of an exceptional G0 class on Z, either in the high Adams weights or on the subgroup obtained from actual ordinary families. The usual rational Chern-character comparison with Chow must separately have its regular algebraizable/finite-model hypotheses verified before a weight-r reformulation is made. The formula by itself gives no dimension bound, no high-codimension injectivity, and no actual-family surjectivity.

Primary inputs are the already opened KST TheoremA/(1.6), Geisser--Hesselholt TheoremA, and Thomason--Trobaugh localization and Zariski descent. The exact localization applications here are to perfect complexes with support on D and to coherent sheaves on regular Z respectively; they are not interchanged.

## 10. Integral ordinary p-torsion: a distinct but unfinished lead

The high rational ranges in Section1 remain open in this work. An
integral-only counterexample would nevertheless have to be distinguished
from them. An abstract group calculation supplies a possible source of
ordinary p-torsion, but does not by itself give a geometric example.

Let E be an ordinary elliptic curve over an algebraically closed field of
characteristic p, and let G be a nonzero extension of E by Ga. Such
extensions are classified by H1(E,O_E). Write V:E^(p)→E for Verschiebung.
Since [p]^*=0 on H1(O), whereas relative Frobenius is bijective on that
space in the ordinary case, V^*=0. The pullback extension therefore
splits and gives a group morphism j:E^(p)→G over V. Its scheme kernel is a
subgroup of the étale group ker(V) of order p. If it were all of ker(V),
j would descend to a section of G→E, contradicting nontriviality.
Consequently j is a closed immersion, and its proper abelian image B has

    B intersect Ga = j(ker V) ≅ Z/p.

Frobenius independently checked this abstract calculation. No claim is
made that the extension is already the local Picard group of a pair in
the question. In particular, a split cone has a retraction and a split
Picard extension; there is no such nonzero proper-abelian intersection
with its vector factor. A genuinely nonsplit neighborhood is necessary.

The smallest suggested geometric test is r=2,N=5. One can try a
deformation of the cone with exceptional variety
V=P1×W×C, where W is a smooth quartic K3 carrying a line D, C is an
ordinary smooth plane quartic, and L=O_P1(1) external O_W(1) external K_C.
Replacing the split cone equation by F_C+t ell H_C, as in C3m, gives a
candidate nontrivial first neighborhood. The desired kernel direction
would lie in ell H1(V,O_V) inside H1(V,L). To obtain a counterexample one
must prove all of the following for this actual pair: the relevant
nontrivial vector extension is its actual local Picard extension; its
separable p-isogeny kernel is realized by actual ordinary line-bundle
families; the selected line bundle restricts to zero on the punctured
divisor; and its product with the nondivisible divisor class D remains
nonzero in CH2 of the source puncture. None of those four geometric
claims has been certified for this candidate.

The elementary obstruction in Section4.1 does not kill this proposed
product: its second factor is a Néron--Severi divisor, rather than an
ordinary divisible Picard class. However, the naive conormal dlog
detector has a new serious limitation. In a nonsplit square-zero
neighborhood the sequence with conormal term
L tensor Omega1_V and quotient Omega2_V need not split. Its connecting
map is contraction with the neighborhood's Kodaira--Spencer class.
For a direction a=c_kappa(omega) and a divisor pulled back from a factor
on which kappa is zero, the expression a cup c1(D) is the connecting
image of omega wedge c1(D). Thus that expression can vanish in the
absolute differential cohomology used by the split-neighborhood proof.
A relative K-theory or logarithmic de Rham--Witt argument would have to
control its additional boundary maps; the split conormal detector from
C3ao cannot simply be reused. This is a method limitation, not a proof
that the proposed cycle is zero.

Additional searches retrieved the local Picard torsion theorem in
Stacks52.26.1/0F29, whose depth(A/f)>=2 hypothesis forces injectivity on
torsion. Any candidate must either satisfy that hypothesis and therefore
fail as a Picard-kernel construction, or explicitly lie outside it. No
example is inferred from a theorem stated only after inverting p.
