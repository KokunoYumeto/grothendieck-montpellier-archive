# The actual compactified-homology completion

19 November 2026. Work proof for the precise proper-homology condition of E.2.22. This establishes its actual automorphism and inner-conjugator maps. It does not prove the proper-to-affine implication or identify a discrete Galois representative.

## PC1. The discrete and profinite quotients

Let X=P1(C) minus {0,1,infinity}, F=<x,y>=pi1_top(X), and G=Fhat, with z=(xy)^(-1). For an open normal N of G, let K_N=F∩N, let Y_N be its actual pointed regular cover, and let C_N be its smooth compactification. Define

\[
 A_N^c=H_1(C_N,\Z),\qquad
 L_N=\ker(K_N\longrightarrow A_N^c),\qquad
 J_N=\overline{L_N}^{G},
\]

\[
 \Gamma_N^c=F/L_N,\qquad P_N^c=G/J_N,\qquad Q_N=G/N.
 \tag{PC.1}
\]

The subgroup L_N is generated in K_N by its commutator subgroup and all actual oriented cusp loops. More explicitly, if d_t is the order of t in Q_N for t=x,y,z, its additional generators are the words f t^(d_t) f^(-1) for coset representatives f of Q_N/<t>. Their conjugacy choices do not affect L_N. Deck transformations permute the cusps; therefore L_N is normal in F.

There is an exact sequence

\[
 1\longrightarrow A_N^c\longrightarrow\Gamma_N^c
       \longrightarrow Q_N\longrightarrow1. \tag{PC.2}
\]

A_N^c is finite-rank free abelian. The elementary residual-finiteness proof used in E.2.28 applies: elements outside A_N^c are separated by Q_N, and its nonzero elements by Gamma_N^c/m A_N^c. Hence

\[
 F\cap J_N=L_N,\quad
 \Gamma_N^c\hookrightarrow P_N^c=\widehat{\Gamma_N^c},\quad
 N/J_N=\widehat A_N^c,\quad
 \Gamma_N^c\cap\widehat A_N^c=A_N^c. \tag{PC.3}
\]

No torsion-freeness of Gamma_N^c is asserted or needed. Its peripheral elements usually have finite order.

If M⊂N, inclusion of cover groups sends commutators to commutators and a cusp loop over Y_M to a positive integral power of a cusp loop over Y_N. Consequently L_M⊂L_N and J_M⊂J_N. The transition maps Gamma_M^c→Gamma_N^c and P_M^c→P_N^c are therefore defined and surjective.

Set

\[
 \mathcal H_c=\bigcap_N (\pi_N^c)^{-1}(\Gamma_N^c)\subset G.
 \tag{PC.4}
\]

Since J_N⊂N, compatible compact cosets show exactly as before that

\[
 G\simeq\varprojlim_N P_N^c,\qquad
 \mathcal H_c\simeq\varprojlim_N\Gamma_N^c. \tag{PC.5}
\]

Each projection of H_c onto Gamma_N^c is surjective, because F⊂H_c already maps onto it. Giving the discrete quotients their discrete topologies makes H_c the completion of F for the neighborhoods L_N. This is a specified embedded subgroup, not a replacement of the original geometric lattices.

## PC2. The original proper lattice of every cover

For every open U of G, let C_U compactify its actual cover and set Lambda_U^c=H1(C_U,Z). Under the actual map from U to its compactified abelianization,

\[
 \operatorname{ab}_U^c(\mathcal H_c\cap U)=\Lambda_U^c.
 \tag{PC.6}
\]

Indeed, choose N⊂core_G(U). The actual filling homology map kills L_N and hence J_N. For w∈H_c∩U choose f∈F with w f^(-1)∈J_N. Since J_N⊂U, the word f belongs to F∩U, and its proper homology class equals the class of w. Conversely F∩U surjects onto the original proper homology lattice.

Inner conjugation preserves these lattices between the corresponding covers: for g∈G choose f∈F∩gU, write g=f u with u∈U, and use that conjugation by u is trivial on the proper abelianization. This is the same actual change-of-basepoint map as for affine homology.

## PC3. The decisive zero-invariant calculation

The finite group Q_N acts by deck transformations on all the preceding lattices. For the affine cover, its invariant graph cycles are exactly

\[
 e_x=\sum_{q\in Q_N}(q,x),\qquad
 e_y=\sum_{q\in Q_N}(q,y).
\]

Both are actual invariant boundary cycles: summing the x-cusp cycles gives e_x, and summing the y-cusp cycles gives e_y. Thus the map from boundary invariants onto affine H1 invariants is surjective over Q. Averaging over the finite group makes the rational invariant functor exact. The boundary-to-affine-to-proper exact sequence therefore gives

\[
 (A_N^c\otimes\Q)^{Q_N}=0. \tag{PC.7}
\]

Equivalently, this is the actual quotient C_N/Q_N=P1 in rational H1, with the branch points retained in the boundary computation. Since A_N^c is free abelian, stack the integral matrices q−1. Their kernel over Q is zero; Smith normal form then shows their kernel over Zhat is also zero, because multiplication by a nonzero integer is injective on Zhat. The same injective matrix remains injective over every Q_l; this also proves the exact zero fixed-space assertion on each actual l-adic realization. Hence

\[
 (\widehat A_N^c)^{Q_N}=0. \tag{PC.8}
\]

The normalizer computation in E.2.28 is applicable to the actual extension (PC.2): if a profinite vector has all differences (q−1)a integral, Smith normal form gives an integral vector with those same differences. The residual vector is invariant. By (PC.8) it is zero. Thus

\[
 \operatorname{Norm}_{P_N^c}(\Gamma_N^c)=\Gamma_N^c.
 \tag{PC.9}
\]

This gives the global equality

\[
 \operatorname{Norm}_{G}(\mathcal H_c)=\mathcal H_c. \tag{PC.10}
\]

For if g normalizes H_c, its coordinate at every N normalizes the surjective image Gamma_N^c, hence belongs to Gamma_N^c by (PC.9). Therefore g∈H_c. The reverse inclusion holds because H_c is a subgroup.

## PC4. Actual peripheral-preserving automorphisms

Consider a continuous automorphism alpha of G that permutes the conjugacy classes of the three procyclic peripheral subgroups and sends each chosen generator to a conjugate of a unit power of the corresponding generator. Actual geometric Galois automorphisms have this property, with the cyclotomic unit. Use the characteristic cofinal chain from E.2.28. Then alpha fixes each N and preserves J_N: it carries the closed normal subgroup generated by the commutators and cusp powers of N onto itself. The finite order of a cusp generator in Q_N is preserved by the corresponding finite quotient automorphism, and a unit power generates the same closed cusp subgroup.

Thus alpha induces an actual automorphism alpha_N of P_N^c. Suppose it carries A_N^c onto itself. The quotient V_N=widehat A_N^c/A_N^c is uniquely divisible, by the explicit residue/divisibility argument of E.2.28. The two complements Gamma_N^c/A_N^c and alpha_N(Gamma_N^c)/A_N^c in P_N^c/A_N^c differ by a cocycle Q_N→V_N. Averaging produces an actual local conjugator in widehat A_N^c.

Let

\[
 S_N^c=\{u\in P_N^c:\operatorname{ad}(u)
          \alpha_N(\Gamma_N^c)=\Gamma_N^c\}.
 \tag{PC.11}
\]

It is a nonempty orbit for left multiplication by Gamma_N^c, namely Gamma_N^c times any one solution, by (PC.9). For M⊂N, the transition maps carry S_M^c into S_N^c and are surjective: pick any solution over M, compare its image with the desired solution over N, and lift their ratio through the surjection Gamma_M^c→Gamma_N^c. A compatible sequence along the countable cofinal chain therefore gives one h∈G via (PC.5). It satisfies

\[
 (\operatorname{ad}(h)\alpha)(\mathcal H_c)=\mathcal H_c.
 \tag{PC.12}
\]

Conversely (PC.6) and the inner-conjugation comparison prove that (PC.12) implies exact integral proper-homology transport on every open cover. We have proved the equivalence of:

1. Alpha preserves the actual proper integral homology lattices of every finite cover.
2. It does so on the one characteristic cofinal chain.
3. There is one actual h∈G satisfying (PC.12).

The set of all global aligning conjugators is exactly

\[
 \{h\in G:h\alpha(\mathcal H_c)h^{-1}=\mathcal H_c\}
       =\mathcal H_c h_0, \tag{PC.12a}
\]

for any one solution h_0. Indeed, h is another solution exactly when h h_0^(-1) normalizes H_c, which by (PC.10) means h h_0^(-1)∈H_c. Thus the aligning coset in H_c\G is uniquely specified. This uses the actual global self-normalizer, not only the finite-level normalizers.

This directly applies to the actual alpha_sigma in E.2.22, including sigma∈Gamma_Fcm. No affine boundary-extension vanishing is assumed.

For a peripheral-preserving beta, the aligned condition beta(H_c)=H_c is also equivalent to beta(x),beta(y)∈H_c. The proof is the finite-generator argument of E.2.28 with the actual groups (PC.3): generator membership gives beta_N(Gamma_N^c)⊂Gamma_N^c; its integral matrix on A_N^c has invertible completion and hence determinant ±1; its finite quotient map is onto. It follows that beta_N(Gamma_N^c)=Gamma_N^c at every level. The zero-rank case has the unique automorphism of the zero lattice and causes no exception.

## PC5. The two completions differ explicitly

Since D_N⊂J_N, the actual quotient maps give

\[
 \mathcal H_{\mathrm{int}}\subset\mathcal H_c. \tag{PC.13}
\]

Every profinite peripheral power belongs to H_c. For example, x has finite order dividing d_x in Gamma_N^c, so x^a has the same coordinate as an integer power at each level for every a∈Zhat. This proves x^Zhat⊂H_c, and similarly for y and z.

Choose the explicit unit a∈Zhat with 2-adic coordinate −1 and every odd-prime coordinate 1. It is not an integer: its 3-adic coordinate would force that integer to be 1, contradicting its 2-adic coordinate. Then x^a belongs to H_c but not to H_int: the latter's image in G^ab=Zhat^2 is contained in Z^2 (take N=G), whereas x^a has first coordinate a. Thus (PC.13) is strict.

This element distinction is not an automorphism or Galois counterexample. In particular, actual sigma∈Gamma_Fcm has cyclotomic character one and sends a cusp generator to a conjugate of the same generator, not to x^a with this different profinite unit exponent.

## PC6. The exact remaining comparison

The proper-to-affine question has the following typed form. For the actual peripheral Galois automorphism alpha_sigma, condition (PC.12) has been proved equivalent to the proper-lattice premise. The remaining assertion is the existence of another actual inner adjustment preserving H_int as in E.2.28. Equivalently, it is the corresponding inclusion of these two conjugacy-stabilizer conditions inside the actual Galois image, with cyclotomic character one. Strict inclusion of the two embedded subgroups in (PC.13) alone proves neither implication nor its failure.

The local boundary-extension block in E.2.28 is the exact homological obstruction to this implication. The construction here gives a direct compactified-homology automorphism model and its self-normalizer; it supplies no vanishing theorem for that block and no discrete surface representative. In particular it is not counted as closing or strictly shrinking the original E.2 separation gate.
