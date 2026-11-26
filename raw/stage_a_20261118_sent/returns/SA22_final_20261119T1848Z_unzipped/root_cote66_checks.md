# Cote 66: checks of implications used in the literature comparison

Checked on 19 November 2026 by GPT-6 Astra Pro, effort not exposed, run SA22-20261119/root. The sheet is a research list, with later insertions and cancellations. The checks below test precise modern interpretations; they do not add missing hypotheses to its ink. Bibliographic access and exact locators are recorded in `parts/root/source_evidence.tsv`.

## C66-1. One constant-sheaf H0 comparison does not imply all cohomology

Let X=P¹ over C and let Y be a C-rational point with its closed immersion in X. For the constant finite sheaf F=Z/lZ, l a prime, restriction H⁰(X,F)→H⁰(Y,F) is an isomorphism: both spaces are connected and both groups are Z/lZ. But H²(X,F)=Z/lZ(-1), whereas H²(Y,F)=0. The latter calculation is the standard cohomology of projective space; it appears in the opened Milne lectures, §16 Example16.3. Thus a criterion using an H⁰ isomorphism for this one F is false. The example does **not** refute a condition quantified over an appropriate entire category of sheaves or a henselian-pair condition. The sheet's quantifier must be read on the scan. Gabber's affine henselian-pair theorem is compared only with its actual hypotheses, not with this false one-sheaf criterion.

## C66-2. A product of algebraically trivial divisors can be nonzero

The first question at scan5 explicitly asks whether the product of two algebraically trivial cycles is rationally trivial. Take A=E×E for a complex elliptic curve E with origin0. For P,Q∈E(C), set a=[P]-[0] and b=[Q]-[0] in CH¹(E). Their pullbacks to A are algebraically trivial divisors. Their intersection product is

    a×b = [(P,Q)]-[(P,0)]-[(0,Q)]+[(0,0)] in CH₀(A).

There exist P,Q for which this class is nonzero. Suppose otherwise. Then every point class is [(P,0)]+[(0,Q)]-[(0,0)], so every degree-zero class is a sum of classes on the two axes. Abel's theorem CH₀(E)⁰≅E(C) reduces each axis sum to one point difference. Consequently every degree-zero class on A would have the form [(P,0)]+[(0,Q)]-2[(0,0)], a fixed finite-dimensional family contained in the image of Sym²(A)×Sym²(A)→CH₀(A)⁰. This contradicts precisely the finite-dimensionality condition(2) discussed in Mumford1969 pp195–196, because A has a nonzero holomorphic two-form. Thus some product a×b is not rationally equivalent to zero.

This argument uses integral Chow groups and exactly the literal product-of-two question. It does not claim rational-coefficient nonvanishing, a nonzero self-square D², or a computed pair of named points. Those stronger assertions would require an additional torsion or differential-form argument and are not needed here. The implication was independently reviewed in this run.

Thus the example satisfies the actual hypotheses of the product question: both factors are algebraically trivial, and their product is not rationally trivial. The equivalence relations are explicitly supplied by this question; they do not need reconstruction. Only the attachment of the neighboring Mumford margin to the first or the second question remains a textual scope issue.

## C66-3. Albanese equivalence need not imply rational equivalence

For a smooth complex projective K3 surface S, H⁰(S,Ω²_S)≠0 and H¹(S,O_S)=0, so Alb(S)=0. Mumford's theorem supplies nontrivial degree-zero Chow classes, indeed a failure of finite-dimensional parametrization. Every degree-zero class has zero Albanese image because the target is zero. Therefore the map CH₀(S)⁰→Alb(S) is not injective. A smooth quartic in P³ is a concrete class of such surfaces; no particular points are asserted to give a nonzero difference without proof. The sheet's adjacent note attributing a negative answer to Mumford is matched to this mathematical result, with his paper communicated28November1968 and published1969. It does not by itself date the original1964 list or every insertion.

## C66-4. Threefold and fourfold cycle questions have different targets

For smooth complex projective threefolds, the cited Griffiths phenomenon concerns homologically trivial1-cycles whose class modulo algebraic equivalence is nonzero; Voisin's Theorem3.1 records the very-general-quintic case, even modulo torsion. Such a cycle is numerically trivial because its cohomology class is zero. This supplies a negative answer if the uncertain τ on scan4 denotes algebraic equivalence modulo torsion. It says nothing about an uninterpreted τ.

The neighboring fourfold question compares numerical and homological equivalence of2-cycles. It is a different comparison. The complex projective case with rational Betti coefficients is included in the low-dimensional Hodge-manifold result attributed to Lieberman1968 in the opened Brown–Walker paper. This run checked that attribution and its hypotheses, not Lieberman's inaccessible original proof. It is invalid to transfer this conclusion to an arbitrary positive-characteristic base merely by keeping the dimension4. That broader reading belongs to standard conjectureD; the bounded November2026 search did not identify a general solution. The sheet itself does not state a coefficient field or a fixed Weil cohomology.

## C66-5. Affine cohomological dimension is a bound, not acyclicity

For a variety X over an algebraically closed field, Milne's opened Theorem15.1 gives cd(X)≤2dim X, and cd(X)≤dim X if X is affine. The latter permits positive-degree cohomology and must not be paraphrased as vanishing of all Hⁱ for i>0. For instance G_m over C has H¹(G_m,Z/lZ)≠0, as follows from the Kummer cover t↦t^l. The cover is finite étale, connected and nontrivial, so its Z/lZ torsor class is nonzero. This is an independent diagnostic for the wording in the memorandum, not a claim that the manuscript asserts acyclicity.

## C66-6. Historical and categorical conditions retained

The Geisser2008 version of the number-ring duality statement is conditional on Beilinson–Lichtenbaum; the later Voevodsky theorem is separately opened and cited before treating that condition as discharged. Triangulated motivic six functors do not automatically supply an abelian category of all mixed motives with the desired t-structure. Ramis–Ruget duality involves the indicated topologies and associated separated spaces. Neutral Tannakian reconstruction requires an exact faithful fibre functor, rigidity and the stated ground-field condition. These are targeted statement checks against the opened sources, not independent re-proofs of those deep theorems.

## Scope of this proof file

There is no numerical computation on the cote66 thesis-list sheets to rerun. The calculations here are symbolic elementary consequences used to delimit literature matches. Historical reasons for abandonment are recorded only when the sheet or an opened source says so. No research direction listed for future work is developed here.
