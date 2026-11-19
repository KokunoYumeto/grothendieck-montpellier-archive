# Independent checks: cote 29, second package and Codex continuations

These are the reviewers' arguments, not reconstructed manuscript prose. Physical line locators are in the item and claim tables. Finite calculations in `programs/exact_checks.py` support the explicit examples; they do not stand in for the universal arguments below.

## 1. Arithmetic action, extensions, and the self-intersection cokernel

In F4((u))/F2((t)), t=u^3, let tau(u)=zeta*u for a primitive cube root zeta in F4 and let F act on coefficients by squaring while fixing u. Then F*tau*F^{-1}=tau^2. The extension has ramification index3 and residue degree2, so its degree6 group is C3 semidirect C2. Tame inertia need not be central in an arithmetic group. This tests an earlier-run extrapolation, not a centrality claim proved on scan96.

For an abelian central extension of Z² by Z, the integral upper-unitriangular 3-by-3 matrices give a nontrivial central commutator of the two standard lifts. Thus pi_2=0 for the underlying torus does not imply splitting. This is an obstruction-theoretic diagnostic, not a fully specified formal-neighborhood counterexample.

Write T^(p')=product_(ell≠p) Z_ell(1), or all primes in characteristic0. Multiplication by a nonzero integer d has cokernel product_(ell≠p) Z/ell^{v_ell(d)}, cyclic of order the prime-to-p part of |d|. For d=0 the cokernel is T^(p') itself. The sign changes neither cokernel. A square integral multiplicity matrix is an isomorphism on T^(p')^r exactly when its determinant is a unit at every ell≠p, equivalently ±p^a; in characteristic0 this is ±1. This follows from the adjugate formula in one direction and reduction modulo a prime divisor in the other. Rectangular matrices need a separate rank/Smith-normal-form statement.

The polynomial x³−4x+1 has no rational root and discriminant229, positive and nonsquare. Its splitting field has group S3 and is totally real. Squarefree discriminant gives only finite ramification at229, with inertia of order2; consequently it is tame there. This supplies nonabelian tame extensions even when real places are required to stay real. It does not determine a general arithmetic tame group or its pi_2.

## 2. The cancelled monodromy lemma

Suppose F,G are invertible endomorphisms of a d-dimensional vector space over any field, q>1 an integer, and FGF^{-1}=G^q. Over an algebraic closure the finite multiset of eigenvalues of G is invariant under lambda↦lambda^q. Its underlying finite set is permuted, so for a common positive m, lambda^{q^m}=lambda for every eigenvalue. Invertibility gives lambda^{q^m−1}=1. Hence every eigenvalue of G^N is1 for N=q^m−1, and (G^N−1)^d=0. No cancellation mark invalidates this proof. Without invertibility, G=diag(0,1), F=1 gives G=G^q but is not quasi-unipotent in this sense.

The phrase semidirect product of Z by Z with multiplication by q cannot literally describe a group action on Z when q>1. One can use the appropriate prime-to-q completion, or Z[1/q], but those are editorial alternatives, not selected readings.

## 3. H² and minimal pointed torsors

For 0→A→B→C→0 in finite abelian coefficients, the long exact cohomology sequence contains H¹(X,C)→H²(X,A)→H²(X,B)→H²(X,C). Thus the vanishing of H¹(X,C) for every such C makes H² left exact. A prorepresentability conclusion additionally uses the chosen coefficient category and size convention. An identification with a geometric pi_2 is a separate theorem.

For an admissible finite group over a base S, let U1,U2 be infinitesimal kernels with finite étale quotients. The composite U1→G/U2 has image in the identity section: its inverse image is clopen and contains every geometric point of U1. Thus U1⊂U2, and symmetry gives equality. No reducedness of S is used. By contrast, pointed rigidity of infinitesimal torsors does use reducedness: on S=Spec k[epsilon]/epsilon², the alpha_p sections0 and epsilon differ but have identical geometric values.

The manuscript's restricted category must not be replaced by all finite flat S-groups. In characteristic p, Eq(0,[t]:alpha_p→alpha_p) over k[t] has algebra k[t,T]/(T^p,tT). Generic fibre length1 and special fibre lengthp show nonflatness.

## 4. The cusp counterexample, with every relevant hypothesis

Let k be algebraically closed of characteristic p and A=k[x,y]/(y^p−x^{p+1})=k[w^p,w^{p+1}]. The base S=Spec A is reduced, integral and connected, and has the cusp k-point x=y=0. The alpha_p torsor P=Spec A[z]/(z^p−x) is finite free of rankp and pointed by z=0 above the cusp. It is nontrivial: x is not a p-th power in A, since its p-th root in k(w) is w and w is absent from the semigroup algebra.

It is minimal with respect to finite flat subgroup reductions. A finite flat closed subgroup of alpha_p has constant rank on S. Over the generic field its only possible ranks are1 andp. Rank1 is the identity; rankp forces equality by a surjection between locally free modules of the same rank. A reduction to the identity would trivialize P.

The two S-group maps0 and[x] on alpha_p are distinct. Under[x], the torsor class x maps to x^{p+1}=y^p, so both pushforwards are pointed-trivial (the trivializing root y vanishes at the cusp). Their coincidence reduction is

    A[z]/(z^p−x,xz−y) = k[z], with x=z^p and y=z^{p+1}.

This is the normalization; its generic rank is1 and its fibre length at the cusp isp. It is not flat. The example refutes an unrestricted variable-base minimality/injectivity statement. It does not lie in the restricted category of constant k-group morphisms: [x] is not constant. Nor does it meet an assumption that all the equalizers remain finite flat. These exclusions are essential.

## 5. CRT and the connected-base monic-factor theorem

Comaximal ideals satisfy J∩J'=JJ': for a+b=1, a∈J,b∈J', an element c in the intersection is ca+cb in JJ'. The converse fails for J=(x), J'=(y) in k[x,y]. The elimination computation confirms the intersection (xy), while every element of J+J' vanishes at the origin.

Let A be a nonzero connected ring, J+J'=A[T], and JJ'=(P) with P monic of degree n. CRT gives B=A[T]/P=B1×B2, where Bi=A[T]/Ji is finite projective over A as a direct summand of the free module B. Connectedness makes the ranks r1,r2 constant. Let Qi be the characteristic polynomial of multiplication by T on Bi. Cayley–Hamilton puts Qi(T) in Ji; the block characteristic polynomial gives Q1Q2=P. The surjection A[T]/Qi→Bi is a surjection of finite locally free modules of the same rank and hence is an isomorphism, locally over every prime. Thus Ji=(Qi). Monic division gives uniqueness. This supplies the missing existence argument without pretending the fragment contains it.

Connectedness cannot be dropped. For A=k×k, put J=k[T]×(T), J'=(T)×k[T]. Their product is generated by the monic pair (T,T), and they are comaximal. A global monic generator would have the same degree in both factors, whereas J has degrees0 and1.

## 6. Missing neighborhood data in the gluing proposal

Let S=A¹_k with infinitely many closed points (take k=Q or an algebraically closed infinite field), generic point eta and fixed closed point c. Over Spec O_(S,c) use that entire local scheme; over each other closed point s use Spec k(S), an open subscheme of the local DVR; at eta use Spec k(S). These local schemes are étale and agree over the common generic point. If they were localizations of one global étale S-scheme, its image would be {eta,c}, which is not open. Every étale map is open. Hence compatibility only over local schemes is insufficient. The source's inserted extension to neighborhoods is not cosmetic. This does not refute the formulation retaining suitable neighborhood models and compatibility.

## 7. Quotients of étale schemes and the nodal example

For a finite étale X/Y of positive constant rankn, the open-and-closed subscheme P of X^n consisting of tuples with distinct coordinates is an S_n-torsor: each geometric fibre has n! such tuples. Its quotient by the stabilizer S_(n−1) is X. This proves the source's construction, with Galois understood as a torsor and without assuming P connected. When X is connected, a connected component of P gives a torsor under a subgroup of S_n.

The broad scan157 statement needs separation or a finite-cover restriction. Let X be the affine line with doubled origin, étale over Y=A¹. The involution exchanging the origins and acting identically on the common punctured line has nontrivial stabilizer on the punctured line and trivial stabilizer at the origins. The trivial-stabilizer locus is not open. Thus the claimed clopen locus fails for arbitrary nonseparated étale X/Y. The source's phrase quasi-affine and its tentative restriction to the finite case expose the missing scope.

A proper irreducible nodal rational curve over an algebraically closed field has cyclic étale covers of every positive degree: glue n copies of its normalization P¹ in a cycle, identifying the two branches consecutively. Étale-locally at each node the map is an isomorphism on the nodal local model. Degree p is allowed in characteristic p. Thus the graph contribution to pi_1 is the full Z-hat, not Z-hat with its p-component deleted. This is a correction to the displayed ordinary-étale group, subject to checking whether a prime-to-p convention was omitted in the transcription.

## 8. The finite-type conclusion on scan187

The last proof arrow cannot be used literally. For an open immersion U⊊Y with Y normal, the normalization of Y has no Y-map onto U. This already disproves the claimed universal arrow from the normalization of X' onto the birational quasi-finite X''.

A valid proof of the intended finite-type statement uses normalization and Zariski's main theorem in the other direction. Work over an affine noetherian Nagata base and treat each of the finitely many irreducible components of X with its reduced structure. Its function field is finite over that of its image closure; the normalization Z of that image in this finite extension is finite over the image closure. Normalize the component of X. Locally finite type over a Nagata scheme makes this normalization finite locally, and its dominant birational locally quasi-finite separated map to normal Z is an open immersion (the local form of Zariski's main theorem). An open of noetherian Z is quasi-compact, hence so is the original component by surjectivity of normalization. Finitely many components give quasi-compactness of X. Locally finite type plus quasi-compact is finite type. The published references for the normalization and open-immersion steps are recorded in the claim's fate; the erroneous displayed arrow is separately listed for scan inspection.

## 9. The topological representability counterexample on scan183

Set A_n=N^n with surjective prefix projections, K=lim A_n=N^N, and F(I)=colim_n Hom(A_n,I). The colimit is filtered. It commutes with finite limits, since each Hom(A_n,-) does and filtered colimits of sets commute with finite limits. Since K→A_n is surjective, F(I) embeds into functions K→I and consists exactly of functions depending on a single fixed finite prefix. If such a function lies in every F(I_alpha) for subsets I_alpha⊂I, its image lies in their intersection, using the same representative. Thus F preserves even arbitrary intersections, not merely filtered ones. Every projection K→A_n is surjective.

Give K the product topology of discrete N and I=N the discrete topology. The function f(x)=x_(x_0+1) is continuous: around each x, first fix x_0=m and then the coordinate m+1. It cannot factor through any A_n: take x_0=y_0=n and identical first n coordinates, but change the coordinate n+1. The two values differ. This meets all three displayed conditions a,b,c and refutes the claimed sufficiency for ordinary continuous functions.

For the inverse-limit uniformity, uniform continuity to a discrete set does require one fixed finite prefix, so that repaired formulation is true in this example. If every A_n is finite, compactness of K makes every continuous map to a discrete set factor through a finite stage, giving the familiar profinite repair. Neither alternative is substituted for the source wording. A second reviewer independently checked this argument during the run.

## 10. Rational structures and root constructions

For a finite-dimensional subspace W⊂K^n, choose a nonzero coordinate minor and write W as the graph of a matrix over K. The subspace descends to an intermediate field k exactly when the graph coefficients lie in k; they are ratios of the Plücker coordinates with that minor as denominator. Their generated field is therefore the minimal field of definition, independent of the chosen chart. For a multilinear map between vector spaces with specified rational structures, rationality is equivalent to rationality of its finitely many coefficients when the source factors have finite dimension. Images and inverse images of rational subspaces are rational by Gaussian elimination over k. The sign in the graph equation is minus; the numerical example in the code only exhibits the error, while this argument supplies the general criterion.

The root stack of (A¹,0) at an invertible n is [A¹_z/mu_n], t=z^n. The stabilizer is trivial off0 and mu_n at0. A root gerbe of the trivial line bundle is Bmu_n×A¹ and has mu_n everywhere. These different stabilizer patterns prevent their identification. The fppf Kummer root algebra A[z]/(z^n−a), for a unit a, is finite free and faithfully flat for any positive n. It is étale when n is invertible, since z and n z^{n−1} are units. These are the precise local calculations used in the modern comparison.
