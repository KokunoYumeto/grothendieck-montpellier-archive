# Independent checks for Codex29, scans188–217

These are reconstructions made in this run. They are not transcriptions, and they do not explain why the author cancelled or abandoned a passage. Source locators and literature matches are in `claims.json`. The finite computations in `programs/exact_checks.py`, saved in `outputs/exact_checks.txt`, check algebra and examples; the arguments below supply the conceptual steps.

## 1. The symmetric homotopy coefficient, scan188

Put
\[
\phi_n(x)=\frac1n\sum_{k=0}^{n-1}\frac{e_k(x)}{\binom{n-1}{k}},
\]
where the source's \(p_k\) is interpreted as the elementary symmetric polynomial \(e_k\). For a nonempty set \(J\) of coordinate indices, put \(q=|J|\) and set the variables in \(J\) to zero. Then
\[
\phi_J=\int_0^1t^{q-1}\prod_{k\notin J}\bigl(t+(1-t)x_k\bigr)\,dt.
\]
Indeed, the coefficient of a monomial of degree \(k\) is the beta integral \((n-1-k)!k!/n!=1/(n\binom{n-1}{k})\). Differentiating \(t^q\prod_{k\notin J}(t+(1-t)x_k)\) and integrating gives
\[
q\phi_J+\sum_{k\notin J}(1-x_k)\phi_{J\cup\{k\}}=1.
\]
The same calculation with no prefactor gives
\[
\sum_j(1-x_j)\phi_{\{j\}}=1-\prod_jx_j.
\]
These prove the coefficient identities for every \(n\), beyond the exact checks for \(n\le8\).

For the analytical interpretation, take smooth forms on a neighbourhood of a closed polydisc (or product of suitably regular compact planar domains), positively orient each boundary, and interpret the source's area differential as \(dt\wedge d\bar t\). Cauchy–Green supplies \(T_j\partial_{\bar z_j}=1-U_j\), \(\partial_{\bar z_j}T_j=1\), and \(\partial_{\bar z_j}U_j=0\) in the interior. Operators in different variables commute. In the source's formula for \(P\), cross terms cancel with the alternating exterior signs; the remaining coefficient on a positive-degree form is exactly the first identity above. Thus \(\bar\partial P+P\bar\partial=1\) in positive degrees and \(P\bar\partial=1-U_1\cdots U_n\) on functions. This is conditional on identifying the unexplained \(\psi_n\) with the preceding \(\phi_n\). The manuscript displays only the function identity, and the whole block is cancelled.

## 2. Pullback along a summand, scans191–192

If \(X=A\amalg B\), universality of finite coproducts gives \(Y=(Y\times_XA)\amalg(Y\times_XB)\). A functor preserving finite coproducts carries this decomposition to a disjoint decomposition of schemes compatible with \(r(X)=r(A)\amalg r(B)\). Therefore the inverse image of \(r(A)\) in \(r(Y)\) is \(r(Y\times_XA)\). This proves the requested restricted pullback lemma. It neither says nor needs that \(r\) preserve arbitrary pullbacks.

R2 then detects emptiness: a nonempty object has distinct zero and whole summands, whereas an empty realization has only one clopen. It detects connectedness because complementary decompositions correspond bijectively. The rank-piece question at192 is made an explicit axiom at191; it is not inferred from these observations.

## 3. The cancelled faithfulness equivalence, scan194

Let \(S=\operatorname{Spec}\bar k\), let \(G=C_2\), and use finite \(G\)-sets. Realize \(X\) as the disjoint union of \(\bar k\)-points indexed by \(X/G\). For an étale \(S'\), which is a disjoint union of points, take the product of this category over the components and realize componentwise. This is a stack with exact cartesian pullback.

The orbit functor is a left adjoint, so finite sums and equivalence-relation quotients are preserved (R1). Invariant subsets of a \(G\)-set are exactly unions of orbits, giving the clopen bijection (R2). Covering invariant subsets form an effective-descent family of finite \(G\)-sets; this is checked componentwise (R3). Every target orbit belongs to one rank piece of an equivariant map, so the realized rank pieces cover (R4). Nevertheless, the regular two-element \(C_2\)-set has two equivariant automorphisms, and both induce the identity of its one-point orbit scheme. Thus R2 does not imply faithfulness of \(r\).

Peer `/root/review_31` independently read the source and checked this whole-site construction. This is a counterexample to a cancelled assertion, not evidence for the historical reason for its cancellation.

## 4. Scheme-valued gluing needs effectiveness, scans199–200

The source explicitly uses the **prestack** of schemes. Let \(k'/k\) be a quadratic Galois extension. Stacks Project Example65.14.2 (tag03FN), opened and checked in this run, constructs a nonschematic algebraic space \(X\) whose base change to \(k'\) is the affine line with doubled origin, a scheme \(Z\). One presentation is the quotient of \(U=\operatorname{Spec}k'[x]\) by the étale relation
\[
R=\Delta(U)\amalg\Delta'(U\setminus\{0\}).
\]
Its generic field is \(k(x)\), while its unique point over zero has residue field \(k'\). If it were a scheme, its local ring there would be a one-dimensional étale local domain over \(k[x]_{(x)}\), hence a discrete valuation ring inside \(k(x)\) with \(x\) noninvertible; the corresponding \(x\)-valuation has residue field \(k\), a contradiction. After \(k'\)-base change the two origins split.

Take the local model \((Z,G=1)\). The trivial action is admissible. Its local ramification category has terminal object realized by \(Z\). The descent isomorphisms for \(Z\), including their cocycle, induce the overlap equivalences required on199. Were the claimed gluing always effective as a scheme-valued ramification datum, its terminal object would be realized by a scheme descending \(Z\). No such scheme exists. The failure is already at the realization of the terminal object, irrespective of finer cover theory.

Consequently one must require effective descent of the geometric realizations, impose a condition ensuring it (for example an appropriate affine descent setting), or allow algebraic-space-valued realizations. Merely stackifying the category of local models does not extend a representation into the prestack of schemes. The general construction on200 also needs existence and admissibility of its colimits/quotients. The explicit finite Kummer charts are affine and do not exhibit this obstruction. Peer `/root/review_31` independently read199–200 and tag03FN and confirmed this reduction.

## 5. Divisor equations, root gerbes and the Chern obstruction, scan201

Let \(D\) be an effective Cartier divisor, let \(n\) be invertible on the base, and choose local equations \(a_\alpha\). The source's arrow \(a_\alpha\to a_\beta\) is a unit \(\zeta_{\alpha\beta}\) with
\(a_\beta=a_\alpha\zeta_{\alpha\beta}^{n}\). With \(e_\alpha=1/a_\alpha\) as a local frame of \(L=\mathcal O(D)\), the trivial root object over the patch has \(1^{\otimes n}\mapsto e_\alpha\). Multiplication by \(\zeta_{\alpha\beta}\) is an isomorphism from the alpha root to the beta root because \(\zeta_{\alpha\beta}^ne_\beta=e_\alpha\). Thus the source's gerbe is the gerbe of nth roots of \(L\).

Under the standard convention using comparison arrows from beta to alpha, use \(u_{\alpha\beta}=\zeta_{\beta\alpha}\). The cocycle \(u_{\alpha\beta}u_{\beta\gamma}u_{\alpha\gamma}^{-1}\) lies in \(\mu_n\) and represents the Kummer boundary \(\delta[L]\in H^2(S,\mu_n)\). The product made from the forward arrows is its inverse; this is an arrow convention, not an ink correction. Neutrality is equivalent to existence of a line bundle \(M\) with \(M^{\otimes n}\cong L\). Products of divisors give the product band and the tuple of classes.

Cadman's author PDF, Example2.4.3, explicitly identifies the line-bundle root gerbe with this Kummer boundary. Stacks03PK supplies the étale sequence for invertible n and the fppf sequence without that restriction. The manuscript's \(H^{2|1}\) doubt is therefore mathematically resolved toward degree2, while the scan remains undecided.

The root **stack of the pair** \((L,s_D)\) also includes a section of the root. Locally it is \([\operatorname{Spec}A[t]/(t^n-a)/\mu_n]\), and it is isomorphic to the base off \(D\). For the source's desired relaxation, if n is invertible at every point of D, the open locus where n is invertible and the complement of D cover S. On the first open the stack is Deligne–Mumford, and on the second it is the scheme itself. This proves the support-only condition by gluing. For example, on \(S=\operatorname{Spec}\mathbb Z\), with \(D=(2)\) and n=3, the stack is already trivial near characteristic3, whereas the line-bundle root gerbe still has \(\mu_3\) inertia there. The fppf root gerbe and the pair root stack must not be conflated.

Scans101 and103 of the Pro29 source seek precisely the comparison between a pulled-back group-extension class and this divisor/normal-bundle Chern class. Both ends were read. Grothendieck–Murre's1971 book has an opened introduction describing the self-intersection class and a verified §6 title “Comparison of two 2-cohomology classes”, pp82–96; chapter metadata alone is not treated as verification of its detailed theorem.

## 6. Two readings of G5 and the countable-set test, scans210–212

Let CountSet be a small skeleton of the category of countable sets. It has finite limits and disjoint universal finite coproducts (G1–G2), and each map factors as a surjection followed by a complemented inclusion (G3). Surjections are effective descent even in this category: the usual descended quotient of a countable set remains countable. The terminal singleton is connected and supplies G4; essential smallness supplies G0.

If G5 means a summand **over \(Y'\)**, the only nonempty connected sets X and Y are singletons. Their pullback is \(Y'\to Y'\), of rank1, and it cannot contain two copies of \(Y'\) over \(Y'\). Thus N=1 works. CountSet is nevertheless not a Galois category, since its countably infinite object has infinitely many disjoint nonzero summands. This refutes the proposed characterization under the intended rank interpretation suggested by212.

If “summand” is instead read in the unsliced category, CountSet fails G5: take \(X=Y=1\), \(Y'=\mathbb N\). For every finite N, Hilbert hotel gives \(\mathbb N\cong\mathbb N\times\{1,\ldots,N+1\}\), so the forbidden object is even the whole pullback. Accordingly, the example does **not** refute the unsliced version. Peer31 detected this distinction and independently checked both branches. A finite computation cannot decide this infinitary issue.

G0–G4 alone cannot characterize finite Galois categories, regardless of the reading of G5. Nor does CountSet admit a finite-set functor preserving finite coproducts: \(\mathbb N\cong\mathbb N\amalg1\) would force a finite cardinal m to equal m+1. This confirms that the proposed finite-functor replacement is a genuine finiteness condition.

## 7. The weaker finite-set functor criterion on216

Assume G0–G3 exactly as printed, and let F preserve finite limits and finite coproducts and reflect isomorphisms, with values in finite sets. First every monomorphism is a complemented inclusion: its G3 factorization has an effective-descent map that is also monic, hence an isomorphism. F detects the initial object because F(0)=empty and conservativity applies to 0→X. It follows that1 is connected and that every object has at most |F(X)| disjoint nonzero summands; recursively splitting terminates in a finite connected decomposition. Equalizers also show that F is faithful.

For X with n=|F(X)|, form P inside X^n by removing every partial diagonal. Finite intersections of complemented subobjects exist. Then F(P) is the nonempty set of all bijections \([n]\to F(X)\), including the singleton frame for n=0. The evaluation map \(P\times[n]\to P\times X\) and the symmetric-group action map \(P\times\mathfrak S_n\to P\times P\) become bijections under F, hence are isomorphisms by conservativity.

Crucially, any map p with F(p) surjective is **universally effective descent**: after any pullback, its F-image remains surjective. Factor that pullback by G3 through a complemented subobject I→T. Its F-image must be all of F(T), so the inclusion is an isomorphism by conservativity. This applies to P→1. Thus the frame construction gives actual universal effective-descent trivializations of all objects, proving the local-finite-triviality condition on209 without assuming quotient preservation of F.

For completeness, this also supplies the finite-colimit part of the classical theorem. Trivialize a finite diagram simultaneously and refine its finite coefficient maps by complementary decompositions; equivalently take a nonempty connected component of a common frame object. Over such a component the diagram is a diagram of finite constant sets. Its finite colimit, with its canonical descent datum, descends along the universal effective-descent cover. This constructs the finite colimit in C, universally under pullback. The resulting quotient maps are universal effective epimorphisms; after the same connected cover they are surjections of finite constant sets, and F of the cover is nonempty. F therefore carries them to surjections and the finite-set coequalizers. F is exact.

This matches the classical Galois-category theorem of SGA1 V4.1 and the current Stacks58.3.6–10. Mathew2016 Definition5.15 and Proposition5.19 give a modern published version of the local-triviality-to-finite-colimit step. His bounded-rank convention must not be used to identify every unbounded multigaloisian category in209 with one of his categories.

Peer31 supplied the finite-frame idea; the F-surjectivity/universal-descent argument and completion are this agent's reconstruction. The source itself only states the equivalence on216.

## 8. Functor criteria and the zero-object obstruction on217

For an exact functor between Boolean finite-cover categories, detecting0 implies faithfulness by applying it to an equalizer and its complement. It implies conservativity by factoring a map through its image and examining the complement and the relative diagonal. Conversely, faithfulness distinguishes the two characteristic maps of a nonzero object, so it detects0. For full faithfulness, subobject bijectivity lifts graphs and then their isomorphic projections. In the other direction, any subobject has a characteristic map to \(1\amalg1\); full faithfulness lifts that map, and left exactness lifts the subobject. This supplies the target u(X) demanded by the scan217 formula.

The last assertion, however, omits a cover condition from the definition of subordination. Let u:FinSet→Fin(C2)-Set give trivial actions. It is exact and fully faithful. Every target object becomes empty after pullback to u(0), hence is subordinate to u(0) in the definition on193. Yet the regular C2-set is not in the image. The asserted equivalence criterion is therefore false literally. Scan202 already inserts a covering condition in its definition of generators.

A safe refinement requires a dominating image object that covers1. In connected Galois categories, descent of finite trivial objects then proves essential surjectivity. In products of Galois categories, use the corresponding componentwise descent and gluing. For an arbitrary finite-locally-constant category without such componentwise effective gluing, an additional boundedness/gluing condition is needed; merely saying “piecewise constant” is not a substitute for that hypothesis. This scope qualification is retained in CL-SA12-840.

## 9. Multiple-point arithmetic on214

For a map from an n-dimensional smooth source to an (n+d)-dimensional smooth target, the transverse locus of m distinct preimages has expected dimension
\(mn-(m-1)(n+d)=n-(m-1)d\).
With three source slots there are five equality partitions: one with three blocks, three with two blocks and one with one block. Their expected dimensions are n−2d, n−d and n. Thus the source's bound n−|E|d is incompatible with its asserted equality at the maximal partition; n−(|E|−1)d is the matching arithmetic. The bottom example n=3,d=1 gives1 and2 as printed. None of this proves the closure assertions for the undefined “net” maps. The other occurrence at C29-05 scan114, line83, is a hypothesis of a different theorem and supplies no definition.
