# The actual automorphism preserving all affine integral homology lattices

19 November 2026. Work proof. This treats continuous automorphisms of the actual free profinite group and the original integral lattices of its finite covers. The compactified-Jacobian condition in E.2.22 is retained separately in AF8.

## AF1. The embedded completion and the exact kernel

Let F be a discrete free group of finite rank r, with specified free generators x_1,...,x_r, and let G be its profinite completion. For every open normal subgroup N of G set

\[
 K_N=F\cap N,\quad A_N=K_N/[K_N,K_N],\quad
 D_N=\overline{[K_N,K_N]}^{G},\quad
 Q_N=G/N=F/K_N,\quad
 \Gamma_N=F/[K_N,K_N],\quad P_N=G/D_N.
\]

The exact discrete extension is

\[
 1\longrightarrow A_N\longrightarrow\Gamma_N\longrightarrow Q_N
 \longrightarrow1. \tag{AF.1}
\]

Here A_N is finite-rank free abelian. The group Gamma_N is residually finite: an element outside A_N is separated by Q_N, while a nonzero element of A_N is separated by Gamma_N/m A_N for some positive integer m. The subgroup m A_N is normal in Gamma_N, and this quotient is finite. Consequently

\[
 F\cap D_N=[K_N,K_N],\qquad
 \Gamma_N\hookrightarrow P_N=\widehat{\Gamma_N}. \tag{AF.2}
\]

The equality of completions follows directly from finite quotients: a finite quotient of F factors through Gamma_N precisely when it kills [K_N,K_N], hence precisely when its extension to G kills D_N. The full profinite topology on A_N is induced from Gamma_N, since all m A_N are normal of finite index in Gamma_N. Thus

\[
 1\longrightarrow\widehat A_N\longrightarrow P_N\longrightarrow Q_N
 \longrightarrow1,\quad
 N/D_N=\widehat A_N,\quad
 \Gamma_N\cap\widehat A_N=A_N. \tag{AF.3}
\]

Also D_N is the closed commutator subgroup of N: K_N is dense in N and the commutator map is continuous.

Define the actual subgroup

\[
 \mathcal H=\bigcap_N \pi_N^{-1}(\Gamma_N)\subset G,
 \qquad \pi_N:G\longrightarrow P_N. \tag{AF.4}
\]

For M contained in N, D_M is contained in D_N, so both P_M→P_N and Gamma_M→Gamma_N are defined and surjective. The actual maps give

\[
 G\xrightarrow{\sim}\varprojlim_N P_N,\qquad
 \mathcal H\xrightarrow{\sim}\varprojlim_N\Gamma_N. \tag{AF.5}
\]

For the first isomorphism, compatible coordinates define nested nonempty compact cosets of D_N in G. Their intersection is one point because D_N is contained in N and the open normal N have trivial intersection. The second assertion is its restriction. On the right in the second assertion give each Gamma_N the discrete topology. It is the completion of F for the topology with neighborhoods [K_N,K_N]; F is dense because its projection to every Gamma_N is onto. This topology need not equal the topology induced from G. E.2.27 supplies a specified element of H outside every profinite conjugate of F when r=2.

A specific characteristic cofinal chain may be used throughout: N_n is the intersection of the kernels of all continuous homomorphisms G→S_a for a≤n. There are finitely many such maps for each n, because the images of the r generators specify them. Thus N_n is open and characteristic in G, the chain is cofinal, and every continuous automorphism of G preserves each N_n and D_Nn. Cofinality gives the same H as (AF.4).

## AF2. Its image in every actual cover lattice

For any open subgroup U of G, not necessarily normal, let F_U=F∩U and Lambda_U=F_U^ab. The finite-cover comparison gives U^ab=Lambda_U tensor Zhat. Then

\[
 \operatorname{ab}_U(\mathcal H\cap U)=\Lambda_U. \tag{AF.6}
\]

For the nontrivial inclusion, take z in H∩U and choose normal N contained in core_G(U). Since pi_N(z) is in Gamma_N, choose f in F with z f^{-1} in D_N. The latter is contained in U and in the kernel of ab_U. Thus f belongs to F_U and ab_U(z)=ab_U(f). The opposite inclusion follows from F_U⊂H∩U. This identifies the original geometric integral lattice, not an arbitrarily chosen abstract lattice.

An inner automorphism ad(g), g in G, preserves these lattices between its corresponding covers. Choose f in F∩gU; then g=f u with u in U, so gUg^{-1}=fUf^{-1}. Inner conjugation by u acts trivially on U^ab, and ad(f) is the actual discrete change-of-basepoint map. Hence ad(g) carries Lambda_U onto Lambda_gUg^{-1}.

## AF3. One local conjugator, with the exact coefficient module

Let alpha be a continuous automorphism of G, and use the characteristic chain. Suppose its action on N^ab=widehat A_N carries A_N onto A_N for a given N in that chain. It induces an automorphism alpha_N of P_N. The discrete groups Gamma_N and alpha_N(Gamma_N) both contain A_N as their exact intersection with widehat A_N and map onto Q_N.

Set V_N=widehat A_N/A_N, as an abstract abelian group. This is a Q-vector space: multiplication by a positive integer m is surjective because any profinite vector has an integral representative modulo m; it is injective because an integral vector divisible by m in every Z_p is divisible by m in Z. The exact sequence

\[
 1\longrightarrow V_N\longrightarrow P_N/A_N\longrightarrow Q_N
 \longrightarrow1 \tag{AF.7}
\]

is split by Gamma_N/A_N. The image of alpha_N(Gamma_N) supplies another complement. Relative to the first complement, their difference is a 1-cocycle c:Q_N→V_N. The averaging formula

\[
 v=|Q_N|^{-1}\sum_{q\in Q_N}c(q),\qquad c(q)=v-qv \tag{AF.8}
\]

shows that conjugation by a lift of -v in widehat A_N carries the second complement to the first. Both subgroups before quotienting contain A_N, so that same conjugation carries alpha_N(Gamma_N) exactly onto Gamma_N. Thus the actual local solution set

\[
 S_N=\{u\in P_N:\operatorname{ad}(u)\alpha_N(\Gamma_N)=\Gamma_N\}
 \tag{AF.9}
\]

is nonempty. It is an orbit for left multiplication by B_N=Norm_PN(Gamma_N), hence equals B_N times any fixed solution. The quotient P_N/A_N is used algebraically only; no Hausdorff topology or compactness of S_N is asserted.

## AF4. The normalizer is explicit

Let Z_N=(widehat A_N)^Q_N. It is central in P_N. Then

\[
 B_N=\Gamma_N Z_N. \tag{AF.10}
\]

Indeed, for b in P_N choose gamma in Gamma_N with the same image in Q_N; write b=gamma a with a in widehat A_N. Since gamma already normalizes Gamma_N, b normalizes it exactly when

\[
 (q-1)a\in A_N\quad\hbox{for every }q\in Q_N. \tag{AF.11}
\]

Choose an integral basis of A_N and stack the integer matrices q−1 into one matrix M. The right hand side Ma in (AF.11) is an integral vector. An integer linear system Mz=c with c integral that has a solution over Zhat also has one over Z: put M in Smith normal form; each nonzero diagonal divisor divides the corresponding integral coordinate in every Z_p, hence in Z, and the zero rows require that coordinate to vanish. Therefore there is a_0 in A_N with Ma_0=Ma. It follows that a−a_0 lies in Z_N. This proves (AF.10), including the reverse inclusion.

## AF5. Actual surjectivity of normalizer transition maps

Use the regular cover of the bouquet of r oriented circles associated with K_N. Its vertices are Q_N and its positively oriented edges are (q,j), from q to q x_j. Its integral chain complex identifies A_N=H_1 with the kernel of the boundary map on the free edge module; there are no 2-cells. A Q_N-invariant edge chain has one constant coefficient for each label j. Every such chain has zero boundary. Consequently

\[
 A_N^{Q_N}=\bigoplus_{j=1}^{r}\Z e_j^N,\qquad
 Z_N=\bigoplus_{j=1}^{r}\widehat\Z e_j^N,
 \quad e_j^N=\sum_{q\in Q_N}(q,j). \tag{AF.12}
\]

The completed equality follows directly from the same permutation coordinates, so no interchange of an infinite limit with cohomology is being assumed.

For M contained in N, the actual cover map sends each edge (q,j) to its image edge under Q_M→Q_N. Thus

\[
 e_j^M\longmapsto [N:M]e_j^N. \tag{AF.13}
\]

In particular, Z_M→Z_N has image d Z_N, where d=[N:M]. Since Gamma_M→Gamma_N is onto and Gamma_N contains the integral invariant cycles A_N^Q_N, (AF.12) gives

\[
 B_M\longrightarrow B_N\quad\hbox{surjective}. \tag{AF.14}
\]

Explicitly, for gamma z in Gamma_N Z_N, lift gamma to Gamma_M. Choose an integral invariant cycle z_0 representing the coordinates of z modulo d, lift z_0 through Gamma_M, and lift z−z_0 through Z_M using (AF.13). Multiplying these three lifts gives the required element of B_M. These are literal group maps, since the Z_N are central.

## AF6. One global inner conjugator

Assume alpha preserves A_N for every N in the characteristic chain. The maps P_M→P_N carry S_M into S_N: both the source Gamma_M and its alpha image project onto the corresponding Gamma_N groups. They are surjective on solution sets. To see this, take a desired s_N in S_N and any t_M in S_M. Its image t_N lies in S_N, and s_N t_N^{-1} lies in B_N. Lift this element to b_M in B_M by (AF.14). Then b_M t_M is a solution over M mapping exactly to s_N.

Choose a compatible sequence s_N along the countable cofinal chain. Equation (AF.5) produces a single actual h in G with those coordinates. Therefore beta=ad(h) alpha satisfies beta_N(Gamma_N)=Gamma_N for every N, whence

\[
 \beta(\mathcal H)=\mathcal H. \tag{AF.15}
\]

This proves compatibility of the conjugators. It does not apply compactness to their nonclosed solution sets; it uses the proved surjective transition maps, followed by compactness only for compatible closed cosets of D_N in G.

Conversely, if beta preserves H, then beta(H∩U)=H∩beta(U) and (AF.6) proves exact preservation of Lambda_U for every open U. Inner conjugation preserves those lattices by AF2. We have proved the following equivalent conditions on an actual continuous alpha in Aut(G):

1. Alpha carries every integral affine-cover lattice Lambda_U onto Lambda_alpha(U).
2. Alpha carries A_N onto A_N for every N in the specified characteristic cofinal chain.
3. There exists one h in G such that ad(h) alpha preserves H.

In subgroup notation this is the exact identity

\[
 \mathscr I_{\mathrm{aff}}
   =\operatorname{Inn}(G)\,
      \operatorname{Stab}_{\operatorname{Aut}_{\mathrm{cont}}(G)}(\mathcal H).
 \tag{AF.16}
\]

No assertion that H equals F is made; E.2.27 proves the contrary. No assertion that every automorphism of H is induced by a continuous automorphism of G is made: the stabilizer in (AF.16) is explicitly taken inside the latter automorphism group.

## AF7. A finite-generator form of the aligned condition

For an actual alpha in Aut_cont(G),

\[
 \alpha(\mathcal H)=\mathcal H
 \quad\Longleftrightarrow\quad
 \alpha(x_j)\in\mathcal H\quad(1\leq j\leq r). \tag{AF.17}
\]

Only the reverse implication needs proof. For every characteristic N, the condition on the generators gives alpha_N(Gamma_N) contained in Gamma_N. It also carries A_N into A_N because A_N=Gamma_N∩widehat A_N and alpha preserves widehat A_N. The resulting integral matrix on A_N has invertible completion, since alpha acts as an automorphism on N/D_N. Its determinant is an integer unit in every Z_p, hence equals +1 or −1. Thus alpha_N maps A_N onto itself. Its map on the finite Q_N is an automorphism; a subgroup of Gamma_N containing A_N and mapping onto Q_N is all of Gamma_N. Hence alpha_N(Gamma_N)=Gamma_N for every N, and (AF.5) proves the claim.

This is a characterization within actual automorphisms of G. It does not assert that arbitrary tuples in H freely generate G or extend to its automorphisms.

## AF8. The remaining proper-lattice and Galois maps

For a finite cover Y with smooth compactification C and finite cusp set D, the exact integral homology sequence is

\[
 0\longrightarrow B_Y\longrightarrow H_1(Y,\Z)
   \longrightarrow H_1(C,\Z)\longrightarrow0,
 \qquad B_Y=\Z[D]/\Z\!\left(\sum_{d\in D}d\right). \tag{AF.18}
\]

The boundary basis maps to the oriented cusp loops, and the single relation is their sum. These free abelian groups admit integral splittings. Under selected splittings, an actual profinite homology map preserving Bhat has the block matrix

\[
 \begin{pmatrix}P&T\\0&S\end{pmatrix},
 \quad T\in\operatorname{Hom}(H_1(C,\Z),B_{Y'})\otimes\widehat\Z.
 \tag{AF.19}
\]

When the boundary permutation/cyclotomic block P and the proper-homology block S are integral isomorphisms, the full affine map is integral exactly when T is integral. Changing either splitting by an integral homomorphism changes T by an integral homomorphism, so its class modulo the integral Hom group is an intrinsic vanishing obstruction. For the actual sigma in Gamma_Fcm, the cyclotomic character is one and the boundary map P is the cusp permutation. E.2.22 supplies integrality of S. It does not, from those two block equations alone, give T=0 modulo integral Hom. The remaining map to prove is the vanishing of these actual boundary-extension classes for the one Galois automorphism, simultaneously over all covers and their maps. No freedom to choose unrelated T's or conjugate targets is asserted here.

Even after the affine condition is obtained, (AF.16) gives preservation of the explicit larger completion H up to one actual inner conjugator. The further assertion that this specific peripheral-preserving Galois automorphism is represented by a discrete surface automorphism remains to be proved. The element construction E.2.27 cannot supply that assertion; it constructs no such automorphism.

## Source audit relevant to the final map

The proof AF1–AF7 is elementary, with every completion, normalizer, and transition map constructed above. Bux–Ershov–Rapinchuk, *The congruence subgroup property for Aut F2*, original GGD5 (2011), pp.327–353, was opened at https://ems.press/content/serial-article-files/29591 . Its pp.330–331 contain the exact relation-module sequence underlying the cover graph, but its main theorem is injectivity of the profinite completion of Out(F2) into Out(G), not surjectivity onto the stabilizer in (AF.16).

Yuksel, *Detecting Free Group Automorphisms via Virtual Homology Representations*, arXiv:2501.13803v2, 3 February 2025, was opened in full at https://arxiv.org/pdf/2501.13803 . Theorem1.2 p3 begins with an actual endomorphism F→F; Theorem1.5 p4 begins with an element of Out(F). Their homology tests apply through those displayed maps. AF.16 supplies an automorphism of H inside G, so the still-required input for those particular theorems is an actual representative mapping F to F. This source reading establishes the exact input map, not an assertion that no other theorem can address it.
