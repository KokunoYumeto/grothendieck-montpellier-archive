# B.5. Comparison axioms and homotopy descent

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. We claim no priority. We read the supplied second-pass transcriptions of cote 151, scans 003, 005, 011--015, 017--018, and independently inspected the original scans 003, 005 and 017 at enlarged resolution. The last subscript in the bottom relation of 005 remains visually unresolved; its mathematical alternatives are evaluated separately. No independent ink reading is claimed for the other scans.

Let $A$ be a small ordinary category, $\mathcal X$ a Grothendieck topos, and $\varphi:A\to\mathcal X$ a functor. Put $U_a=\varphi(a)$ and $\widehat A=\operatorname{Fun}(A^{\mathrm{op}},\mathbf{Set})$. Its cocontinuous extension is

$$L=\varphi_!: \widehat A\to\mathcal X,\qquad L(F)=\int^{a\in A}F(a)\cdot U_a.$$

Here the dot denotes copower. For a finite diagram $F:J\to\widehat A$, write $c_F:L(\lim_JF)\to\lim_JL(F)$ for the canonical comparison. An object $U$ of $\mathcal X$ represents the slice topos $\mathcal X/U$, not its set of global sections. This distinction is essential for interpreting the requested homotopy colimit.

## B5.1. The forest statement and the full condition

**Status: Proved.** Hyp 1, 2 and $2'$ of 151/011--014 are respectively the epimorphicity of

$$L(1)\to1,\qquad L(ya\times yb)\to U_a\times U_b,$$

and

$$L(ya\times_{yc}yb)\to U_a\times_{U_c}U_b$$

for every cospan $a\to c\leftarrow b$ in $A$. These are equivalent to $c_F$ being epic for all diagrams indexed by the free category on a finite oriented forest, including the empty forest. This is an equivalence with a collection of tests; it does not assert that every indexing category which is not a forest fails. For example, a category with an initial object has its limit given by evaluation there.

**Proof.** The category of elements gives $L(F)=\operatorname{colim}_{(a,s)\in A/F}U_a$. The coproduct of its terms maps epimorphically onto that colimit. Thus the image of each representable comparison is exactly the image of the covering family of cones written in the manuscript. Hyp $1'$ is tautological because the slice contains the identity of its target.

For completeness we prove the extension to arbitrary presheaves. Work locally in $\mathcal X$. An element of $L(F)$ is represented by $(a,x,s)$ with $x\in U_a$ and $s\in F(a)$, and equality is locally witnessed by a finite zigzag of coend relations. In the internal category $E_\varphi$, an object is $(a,x)$ and an arrow $(a,x)\to(b,z)$ is $f:a\to b$ such that $\varphi(f)x=z$. Hyp 2 says any two objects locally have a common predecessor; Hyp $2'$ says a cospan locally has a commutative completing square. Every finite zigzag locally admits a commuting cone: induct on its edges, composing a cone leg at a forward step and using a completing square at a backward step. For disconnected diagrams combine the cones by Hyp 2. Only finitely many covering refinements are used.

Given an element of $L(G)\times_{L(F)}L(H)$, represent its two entries locally. Their images are connected by such a zigzag. The cone replaces them by representatives at a common object with equal images in $F$, hence by an element of $G\times_FH$. This proves the pullback comparison is epic for arbitrary presheaves; products use the same argument without the equality zigzag. A tree limit is obtained by deleting leaves and successively taking pullbacks: a leaf which is a target contributes no new variable, and a leaf which is a source gives a pullback over the adjacent vertex. The comparison factors through a pullback comparison and a base change of the earlier epimorphism. Products treat components; Hyp 1 treats the empty forest. The converse uses the empty diagram, the discrete pair, and the cospan. The argument uses the local meaning of epimorphisms, not enough points. $\square$

**Full condition.** All the finite comparisons are epic if and only if $L$ is left exact (flatness of $\varphi$).

**Proof.** Let $M=\lim_JF$ and $c:L(M)\to N=\lim_JL(F)$. Add two cone vertices to $J$, both carrying $M$ and its canonical cone. The enlarged diagram has limit $M\times_M M=M$. After $L$ its limit is $L(M)\times_NL(M)$, so its comparison is the diagonal of $c$. That diagonal is epic by hypothesis and monic automatically, hence invertible. Therefore $c$ is monic and, by the original hypothesis, epic; it is an isomorphism. This also treats empty $J$. The converse is immediate. $\square$

This independently rechecks SA10-R151a-15, -16, -17, -19, -21 and -22. The single dot on 151/015 is not the empty diagram: it always yields an identity comparison. For Hyp 1 it must be the empty diagram, as in SA10-K151a-05.

## B5.2. A finite counterexample

**Status: Refuted, corrected by B5.1.** Hyp 1, 2 and $2'$ neither imply full (Hyp) nor suffice for homotopy descent over a point.

**Proof.** Take $A=BC_2$ and $\varphi(*)=\{*\}$. Then $L$ takes a $C_2$-set to its orbit set. Products compare surjectively by choosing representatives. For a pullback of equivariant maps, representatives of two orbits with the same image orbit can be adjusted by a group element so their images agree; therefore all pullback comparisons are surjective. On the regular $C_2$-set, however, the identity and translation by the nonidentity element have empty equalizer, while their maps on the one-point orbit set coincide. Its equalizer comparison is $\varnothing\to\{*\}$. Finally, $\operatorname{hocolim}_{BC_2}\{*\}=BC_2$. Its normalized simplicial chain complex over $\mathbf F_2$ has one generator in degrees 1 and 2 and zero boundary between them, so $H_1=\mathbf F_2$ and it is not contractible. The finite program verifies all four cospans, eight completing squares, the failed equalizer, and the homology obstruction. $\square$

This independently rechecks SA10-R151a-20 and SA10-K151a-04; the example was already in the supplied material.

## B5.3. The symmetric group nerve: distinguish three realizations

**Status: Proved, with a correction to ambiguous uses of realization.** Let $\mathsf F$ be nonempty finite sets and all maps, $A=\mathsf F^{\mathrm{op}}$, and $G$ a discrete group. Put $U(S)=G^S/G$ for simultaneous left multiplication. Hyp 1, 2 and $2'$ hold, and

$$\operatorname{hocolim}_{\mathsf F^{\mathrm{op}}}U\simeq BG.$$

For $G\ne1$, full (Hyp) fails. The ordinary simplicial restriction also realizes to $BG$. In contrast, the literal symmetric coend realization with affine simplices is contractible for finite $G$.

**Proof.** We have $U(1)=*$. Concatenation of representatives proves the product condition. A cospan in $A$ is opposite to $P\leftarrow R\to Q$ in $\mathsf F$, whose pushout represents its pullback in $A$. If tuple orbits on $P,Q$ have the same restricted orbit on $R$, translate one representative so the restrictions agree. They descend to a tuple on the pushout. This proves the condition for every cospan, including noninjective maps. For the two coordinate maps $2\rightrightarrows1$ in $A$, the equalizer is $1\to2$. Its image under $U$ is $*\to G$, but the equalizer after $U$ is all of $G$.

Put $T(S)=G^S$. Its category of elements is cofiltered: it is nonempty, concatenation gives common predecessors, and parallel tuple maps are equalized by quotienting their finite coordinate set by the required identifications. The tuple values agree on those identifications precisely because the two arrows have the same target tuple. The quotient remains nonempty. A cofiltered category has contractible nerve: give a common predecessor to the vertices of any finite subcomplex, then successively equalize the finitely many edge compatibility equations to obtain a cone. This contracts maps from finite simplicial spheres.

The $G$-action on this element category is free on objects, and on nerve simplices, since tuples are nonempty. Choosing a representative of the initial tuple uniquely lifts a whole chain. Thus $N(E_U)=N(E_T)/G$, a free contractible simplicial $G$-space modulo $G$, hence $BG$. The category-of-elements nerve is the simplicial replacement computing a homotopy colimit. Restricting to $\Delta^{\mathrm{op}}$ gives the homogeneous bar construction $G^{n+1}/G$.

For finite $G$, the symmetric realization of $T$ is instead the simplex $\Delta(G)$: equal labels merge their barycentric weights, leaving a probability vector on $G$. Coends commute with orbit quotients, so the symmetric realization of $U$ is $\Delta(G)/G$. The affine contraction to the invariant barycenter is equivariant, hence contracts the quotient. For $C_2$ this is an interval modulo reflection. $\square$

The program verifies 16 product comparisons (input cardinalities at most 4), 1,528 cospans (all three cardinalities at most 3), and 6,871 compatible target pairs for $C_2$. The pushout proof, not the bounded computation, proves the all-cardinality statement. The earlier statement "the symmetric nerve realizes to $BG$" is correct for homotopy colimit or ordinary simplicial realization; it is false for the naive symmetric coend.

## B5.4. Classification of flat symmetric systems

**Status: Proved.** Flat functors $\mathsf F^{\mathrm{op}}\to\mathcal X$ are exactly the systems $S\mapsto E^S$ with $E\to1_{\mathcal X}$ epic. In sets, $E$ is a nonempty set.

**Proof.** Let $E=\varphi(1)$. The object $n$ is the product of $n$ copies of $1$ in $A$. Yoneda and left exactness of $L$ give the canonical isomorphism $\varphi(n)\cong E^n$, naturally for all coordinate maps. Hyp 1 gives an epimorphism $\coprod_{n\ge1}E^n\to1$, which factors through $E\to1$, proving inhabitedness. Conversely, the internal tuple category of an inhabited $E$ is locally nonempty, has common predecessors by concatenation, and equalizes parallel arrows by the coordinate quotient used above. It is locally cofiltered. The coend is internally a filtered colimit of evaluations: finitely many representatives can be moved to one index, and finitely many equalities made simultaneously true at a further index. This proves both surjectivity and injectivity of every finite-limit comparison. All arguments use finitely many local refinements and apply to any Grothendieck topos. $\square$

This independently proves SA10-R151a-29 without relying on its unchecked textbook locator.

## B5.5. Flatness, forest comparisons, and Verdier hypercovers

**Status: Refuted for the proposed "strictly between" description.** A hypercover condition agreeing with Verdier's cannot in general lie between the manuscript's forest conditions and flatness.

For $A=\Delta^{\mathrm{op}}$, the ordinary Cech nerve $U_n=\{0,1\}^{n+1}$ of a cover of a point is a hypercover, and its realization is the contractible nerve of the indiscrete groupoid on two objects. Yet Hyp $2'$ fails. Take in $\Delta$ the span $[0]\leftarrow[1]\to[2]$, with the first map constant and the second selecting endpoints 0,2. The corresponding fiber product contains $(0,(0,1,0))$. A cocone must have a monotone map $[2]\to[m]$ with equal endpoint values, hence a constant map. Every tuple lifted from a completing cone is therefore constant in those three positions. The displayed element has no lift. In particular full (Hyp) fails as well.

Conversely, $\Delta[1]$ is a flat functor on $\Delta^{\mathrm{op}}$: its extension is evaluation at $[1]$. It is not a hypercover of a point, because its degree-one matching map omits the ordered pair of vertices $(1,0)$. Thus even flatness and Verdier's condition are incomparable for ordinary simplicial indexing.

The failure of "between" persists for symmetric indexing. Put $U(S)=\operatorname{Cont}(\Delta(S),\mathbf R)$, with maps by affine precomposition. Every continuous boundary map to $\mathbf R$ extends to the simplex by coning from the barycenter and interpolating to zero; compactness gives continuity at the barycenter. Hence the ordinary simplicial restriction is a hypercover of a point. For the finite-set span $1\leftarrow2\to3$, with the right map selecting vertices 0,2, take zero on $\Delta^0$ and

$$b(t_0,t_1,t_2)=t_1(t_0-t_2).$$

They agree on edge 02. Any amalgamating finite-set map identifies vertices 0,2, so its affine map takes $(1/2,1/2,0)$ and $(0,1/2,1/2)$ to the same point. A lifted function must have equal values there; $b$ has values $1/4,-1/4$. Thus Hyp $2'$ fails. Exact rational computation checks this obstruction on 30 amalgams; the argument proves it for every target cardinality.

There is nevertheless a one-way implication specific to symmetric indexing: full (Hyp) implies the hypercover condition. By B5.4 its system is $U(S)=E^S$ with $E\to1$ epic. The simplicial restriction is the Cech nerve of this epimorphism; every positive matching map is an isomorphism. The symmetric continuous-simplex example just given proves the converse false. Thus ordinary flatness and hypercovers are incomparable, whereas symmetric flatness is strictly stronger than hypercovers; in either case hypercovers need not satisfy the forest conditions.

Over sets there is also an explicit ordinary-index classification: flat functors $\Delta^{\mathrm{op}}\to\mathbf{Set}$ are precisely nerves of nonempty linear orders. Indeed a flat functor is a filtered colimit of the covariant representables $\operatorname{Hom}_{\Delta^{\mathrm{op}}}([n],-)=\Delta[n]$. A filtered colimit of finite ordinals and monotone maps is a linear order: comparisons and antisymmetry are witnessed at a common stage. Nerves commute with filtered colimits, since finite strings use finite limits of sets. Conversely a linear order is the filtered union of its nonempty finite suborders. The filtered-colimit characterization follows from the cofiltered element-category argument in B5.4. $\square$

This corrects lines 61--68, 78--83, and lines 303--309. The assertion that the comparison scheme lies strictly between forest conditions and flatness is not a valid requirement for the desired Verdier comparison.

## B5.6. Exact general homotopy-colimit criterion

**Status: Proved under the stated interpretation.** Let $\mathscr X$ denote either the associated 1-localic infinity-topos or its hypercompletion; fix this choice in each formula. Regard $U_a$ as 0-truncated objects of $\mathscr X$. Form

$$B_\varphi{}_n=\coprod_{a_0\to\cdots\to a_n}U_{a_0},\qquad
H_\varphi=|B_\varphi|=\operatorname{colim}_{a\in A}U_a.$$

The first face uses $U_{a_0}\to U_{a_1}$, inner faces compose arrows, the last face drops the last arrow, and degeneracies insert identities. The augmentation $\epsilon:H_\varphi\to1$ is the terminal comparison of the derived colimit extension $\mathbf L\varphi_!:\mathcal P(A)\to\mathscr X$, since $1_{\mathcal P(A)}=\operatorname{colim}_{a\in A}y(a)$.

There is a canonical map

$$\operatorname{colim}_{a\in A}\Pi_\infty(\mathscr X/U_a)\longrightarrow\Pi_\infty(\mathscr X).\tag{B5.6.1}$$

It is an equivalence of pro-spaces if and only if for every space $K$ the canonical map

$$\operatorname{Map}_{\mathscr X}(1,\Delta K)\longrightarrow
\lim_{a\in A^{\mathrm{op}}}\operatorname{Map}_{\mathscr X}(U_a,\Delta K)\tag{B5.6.2}$$

is an equivalence. It suffices that $\epsilon$ be an equivalence. Full ordinary (Hyp) suffices for this stronger assertion even before hypercompletion; the forest conditions do not, by B5.2. Full (Hyp) is not necessary, by B5.5.

**Proof.** A constant object in the slice over $U$ is $U\times\Delta K\to U$, and therefore

$$\operatorname{Map}_{\operatorname{Pro}(\mathcal S)}(\Pi_\infty(\mathscr X/U),K)
=\operatorname{Map}_{\mathscr X}(U,\Delta K).$$

Maps from the colimit of slice shapes to $K$ give the limit on the right of (B5.6.2), which is $\operatorname{Map}_{\mathscr X}(H_\varphi,\Delta K)$. Shape is the functor $K\mapsto\Gamma\Delta K$, and pro-spaces are fully faithfully represented by these functors. This proves the exact criterion and its sufficient condition.

Under full (Hyp), B5.1 makes $L$ left exact; it is cocontinuous and has right adjoint $V\mapsto[a\mapsto\operatorname{Hom}(U_a,V)]$. Thus it is the inverse image of a geometric morphism $\mathcal X\to\widehat A$. The universal property of the associated 1-localic infinity-topos (HTT Proposition 6.4.5.7 [@B56HTT Proposition 6.4.5.7]) first extends this to $\mathcal X_\infty\to\mathcal P(A)$. Its inverse image agrees with $\varphi$ on representables and hence is the derived colimit extension into $\mathcal X_\infty$. It preserves the terminal object. If $\mathscr X=\widehat{\mathcal X_\infty}$, compose this inverse image with hypercompletion, which preserves colimits and finite limits. This proves $H_\varphi=1$ for either choice without asserting that the hypercompletion is itself 1-localic. $\square$

In the hypercomplete choice, $H_\varphi=1$ is equivalent to the augmented simplicial replacement being a local weak equivalence. After local fibrant replacement this can be tested by local relative homotopy fillings of all finite simplicial boundaries (Dugger--Hollander--Isaksen Proposition 3.1 [@B56DHI2004 Propositions 3.1--3.2]); strict local fillings characterize a local acyclic fibration (Proposition 3.2). These are higher coherence conditions, not the ordinary forest comparisons.

**Exact Artin--Mazur interpretation.** Require $\mathcal X$ locally connected, and let $q:\operatorname{Pro}(\mathcal S)\to
\operatorname{Pro}(\operatorname{Ho}\mathcal S)$ be the canonical functor. The hypercover pro-homotopy type is $$\operatorname{AM}(\mathcal X)\cong
q\bigl(\Pi_\infty(\widehat{\mathcal X_\infty})\bigr).
\tag{B5.6.3}$$ Indeed Barnea--Harpaz--Horel Theorem 6.0.4, printed pp. 625--626, identifies the derived topological realization with the shape of the *hypercompleted* infinity-topos [@B56BHH2017]. Barnea--Schlank Definition 8.2, Proposition 8.4 and Remark 8.5(2), printed pp. 62--65 of the opened preprint, identify its image under $q$ with the Artin--Mazur construction for every locally connected topos [@B56BarneaSchlank2015]. Their Remark 8.5(3) separately records the further localization used by Artin--Mazur; applying that localization preserves all isomorphisms proved here.

Thus (B5.6.1), formed in pro-spaces using the hypercomplete choice and then sent through $q$, is the precise single-diagram comparison with $\operatorname{AM}(\mathcal X)$. It is an isomorphism in $\operatorname{Pro}(\operatorname{Ho}\mathcal S)$ if and only if, for every space $K$, the map $$\pi_0\operatorname{Map}_{\widehat{\mathcal X_\infty}}(1,\Delta K)
\longrightarrow
\pi_0\!\left(\lim_{a\in A^{\mathrm{op}}}
\operatorname{Map}_{\widehat{\mathcal X_\infty}}(U_a,\Delta K)\right)
\tag{B5.6.4}$$ is a bijection. To prove this, a pro-space $P=(P_i)$ satisfies $\operatorname{Hom}(qP,K)=\operatorname{colim}_i[P_i,K]
=\pi_0\operatorname{Map}(P,K)$, since filtered colimits commute with $\pi_0$. Pro-objects of $\operatorname{Ho}\mathcal S$ are fully faithfully detected by their set-valued functors of maps to constant objects. Apply this to the already formed comparison (B5.6.1). The limit in (B5.6.4) is a limit of spaces taken *before* $\pi_0$. We neither interchange these operations nor claim that $q$ preserves the colimit in (B5.6.1). The mapping-space equivalences (B5.6.2) imply (B5.6.4), but the latter alone is not asserted to recover them.

For the full, possibly nonhypercomplete shape, use (B5.6.2) with $\mathscr X=\mathcal X_\infty$. A local weak equivalence or a hypercover alone supplies the hypercomplete version, and does not by itself justify that full-shape conclusion. It also suffices for the protruncated comparison, because truncated constant objects are hypercomplete. Full ordinary (Hyp) supplies the stronger terminal-object descent before hypercompletion, as proved above. These are distinct targets, rather than implicit identifications of pro-homotopy objects and pro-spaces; see also HTT Example 7.1.6.9 [@B56HTT].

## B5.7. Verdier matching as comparisons of representables

**Status: Known, with the precise derivation given.** Define

$$M_nU=\lim_{\varnothing\ne S\subsetneq\{0,\ldots,n\}}U_{|S|-1},\qquad M_0U=1,$$

with face restriction arrows. The conditions $U_n\to M_nU$ epic for all $n\ge0$ are the hypercover conditions. The realization is infinity-connected in $\mathcal X_\infty$ and terminal after hypercompletion. This is HTT Definition 6.5.3.2, Lemma 6.5.3.11 and Theorem 6.5.3.12 [@B56HTT] (or DHI Definition 4.2 and Proposition 3.2).

For $A=\Delta^{\mathrm{op}}$ and $n\ge2$, the limit in $\widehat A$ of the representables of all proper nonempty faces of $[n]$ is $y[n]$. Consequently its comparison $c_F$ is precisely $U_n\to M_nU$. Degrees zero and one must be added separately. For $A=\mathsf F^{\mathrm{op}}$ the same statement holds for all $n\ge1$, so all positive-degree matching conditions are the corresponding boundary comparisons, with degree zero $U(1)\to1$.

**Proof of the representable identity.** Compatible maps from all proper faces into an ordinal determine the vertex images. For $n\ge2$, every pair of vertices lies in a proper face; the images are therefore monotone, determining a unique map from $[n]$. At $n=1$ the two vertex images need not be monotone. For finite sets, no monotonicity restriction occurs, and compatible vertex maps determine a unique function also in the two-vertex case. Yoneda turns these colimit properties into the asserted limits. $\square$

The inclusion $j:\Delta^{\mathrm{op}}\to\mathsf F^{\mathrm{op}}$ is homotopy final. For any nonempty $S$, the comma category $(S\downarrow j)$ is the category of nonempty ordered tuples in $S$ and monotone restriction maps. Choose $s\in S$. Prepending $s$ defines an endofunctor with natural transformations to the identity (drop the first entry) and to the constant tuple $(s)$ (select the first entry). Its nerve is contractible. The cofinality criterion HTT Theorem 4.1.3.1 applies. Thus symmetric matching conditions compute the homotopy colimit over all finite-set maps, not only the ordinary simplicial subcategory.

## B5.8. Every matching degree is independently needed

**Status: Proved.** For every $m\ge0$ there is a simplicial set with all matching maps except the $m$th surjective and with noncontractible realization. The example extends to symmetric indexing by all nonempty finite sets.

**Proof.** For $m=0$, take the empty simplicial set: every positive matching target is empty. For $m=1$, take the constant two-point set: only the diagonal map to its square fails, since all higher simplex boundaries are connected.

For $m\ge2$, let $n=m-1$ and define $K_n(k)=Z^n(\Delta^k;\mathbf F_2)$ with cochain pullback maps. A simplicial map $T\to K_n$ is precisely a normalized $n$-cocycle on $T$: its values on $n$-simplices form the cochain and the $(n+1)$-simplex relation is the cocycle equation. Hence the $k$th matching map is

$$Z^n(\Delta^k;\mathbf F_2)\to Z^n(\partial\Delta^k;\mathbf F_2).$$

For $k<n$ both groups vanish; for $k=n$ the target vanishes. At $k=n+1$, the target consists of arbitrary values on the $n+2$ boundary $n$-faces; the image is the codimension-one subspace whose sum is zero. For $k>n+1$, every $n$- and $(n+1)$-simplex already belongs to the boundary, so restriction is an isomorphism. Thus only degree $m$ fails.

The normalized Moore complex of $K_n$ is $\mathbf F_2$ in degree $n$ and zero otherwise: a normalized element vanishes on all specified faces, and in degree $n+1$ the cocycle equation forces the remaining face to vanish; above that degree all $n$-faces already lie in vanishing faces. Its homotopy group $\pi_n$ is therefore $\mathbf F_2$, by Curtis, Theorem 3.7 (printed p. 131) [@B56Curtis1971]. This is also the cocycle model of the Dold--Kan object of $\mathbf F_2[n]$; normalization is the equivalence of Stacks Theorem 14.24.3 (019G) [@B56StacksDK]. For the symmetric extension, define the same cocycles on the abstract simplex on a finite set; an arbitrary vertex map induces a normalized simplicial chain map, sending a face with repeated image vertices to zero. Over $\mathbf F_2$ this construction is independent of ordering. It gives the same ordinary simplicial restriction, hence the same homotopy colimit by B5.7. The finite code checks 32 matching comparisons for $1\le n\le4$, $0\le k\le7$, with precisely the stated failures. $\square$

## B5.9. Component sets alone cannot reconstruct the homotopy type

**Status: Refuted, corrected by B5.6 and the hypercover pro-system.** No condition requiring even all ordinary comparisons to be isomorphisms can ensure $\operatorname{hocolim}_A\pi_0(U_a)$ models the Artin--Mazur type without a condition on the pieces.

**Proof.** Take $A$ terminal, $\mathcal X=\operatorname{Sh}(S^2)$ and $U_*=1_{\mathcal X}$. Then $L:\mathbf{Set}\to\operatorname{Sh}(S^2)$ is constant-sheaf inverse image, so it preserves finite limits. But $\pi_0(U_*)=*$, and its homotopy colimit is a point; the sphere has $H^2(S^2;\mathbf Z)=\mathbf Z$. The correct single-diagram formula uses slice shapes. Component sets can replace them when each canonical map $\Pi_\infty(\mathscr X/U_a)\to\pi_0(U_a)$ is an equivalence and the diagram is homotopy effective: replace each object by that equivalent pro-space in B5.6. In general Artin--Mazur retains the cofiltered pro-system of all hypercovers and their component simplicial sets. Even the constant terminal hypercover is not generally a single model of the shape. $\square$

## B5.10. An explicit all-index local filling criterion

**Status: Known criterion, derived here in the required form.** The exact stronger condition $H_\varphi=1$ in the hypercomplete infinity-topos has an explicit test using the original $U_a$, finite limits, coproducts and a sequential colimit. It does not require one to guess boundary objects in the arbitrary category $A$.

Let $N=B_\varphi$ be the simplicial replacement from B5.6; equivalently it is the nerve of the internal element category, whose objects are $\coprod_aU_a$ and whose arrow object is $\coprod_{a\to b}U_a$. For a finite simplicial set $K$, let $[K,N]$ be the object of simplicial maps, expressed as a finite limit using the nondegenerate simplices of $K$. Put

$$R_n=\operatorname*{colim}_{r\ge0}[\operatorname{Sd}^{r}\Delta^n,N],$$

with the transition maps induced by the standard last-vertex subdivision maps. Here colimits and finite limits are in $\mathcal X$, and $\operatorname{Sd}$ is barycentric subdivision. Then the following are equivalent:

1.  $H_\varphi\to1$ is an equivalence after hypercompletion.

2.  The simplicial replacement $N\to1$ is a local weak equivalence.

3.  For every $n\ge0$, the following explicit map is an epimorphism in $\mathcal X$:

$$\operatorname*{colim}_{r\ge0}[\operatorname{Sd}^{r}\Delta^n,N]
\longrightarrow
\operatorname*{colim}_{r\ge0}[\operatorname{Sd}^{r}\partial\Delta^n,N].\tag{B5.10.1}$$

For $n=0$ the right side is terminal. Since filtered colimits commute with finite limits in a Grothendieck topos, the right side is precisely $M_nR$. Thus (3) is an ordinary epimorphic matching-map scheme on the explicitly derived simplicial object $R$. It says that every finite boundary admits a filling locally after sufficiently many subdivisions. The required subdivision number may vary over the covering family; no assertion of algorithmic decidability is made.

**Proof.** Present $\mathcal X$ by a small site, and regard $N$ as a simplicial sheaf there. Apply $\operatorname{Ex}^{\infty}$ sectionwise to obtain a simplicial presheaf $F$. For every object of the site, $F$ is a Kan complex and $N\to F$ is a weak homotopy equivalence, by Kerodon Propositions 3.3.6.7 and 3.3.6.9 (Tags 00ZH and 00ZK) [@B56KerodonExInfinity]. Therefore $N\to F$ is a local weak equivalence, and $F$ is locally fibrant. Dugger--Hollander--Isaksen Proposition 3.2, reformulated as their equation (3.4) [@B56DHI2004], says that $F\to1$ is a local weak equivalence if and only if every map $F_n\to[\partial\Delta^n,F]$ is a local epimorphism: its local fibration hypothesis is automatic here. Sheafification preserves finite limits and colimits. Sheafifying these maps gives precisely (B5.10.1), by the subdivision--extension adjunction and finite presentation of the boundaries. This proves (2) equivalent to (3), independently of the chosen site. The local model category presents the hypercompletion, so (1) is equivalent to (2). This last restriction matters: local weak equivalence gives an infinity-connected augmentation in a nonhypercomplete topos, not necessarily an equivalence there. $\square$

This supplies an effective mathematical description for every small $A$, in addition to the direct sufficient condition on the manuscript's $c_F$ in B5.1 and the sharper boundary schemes of B5.7. The weaker forest scheme fails by B5.2--B5.3. Omitting any dimension from the strict matching scheme fails by B5.8, in ordinary and symmetric indexing. Conditions for shape equivalence alone can be weaker than universal local descent; their precise criteria are B5.6.2 for pro-spaces and B5.6.4 for the original pro-homotopy category. In particular, (B5.10.1) is necessary and sufficient for the stronger local descent assertion, not a claimed necessary condition for equality only of shapes.

## Scope of the comparison result

The answer separates the literal ordinary comparisons, the universal local descent condition, and the Artin--Mazur target. All finite ordinary comparisons epic is exactly flatness and suffices even before hypercompletion; the forest subcollection fails. The boundary comparisons in ordinary and symmetric indexing give Verdier hypercovers, with every matching degree indispensable. For arbitrary indexing, (B5.10.1) is an explicit necessary-and-sufficient higher local descent criterion after hypercompletion. For equality only of shapes, (B5.6.2) is the exact criterion; for the original Artin--Mazur pro-homotopy type, (B5.6.3)--(B5.6.4) give the exact locally connected interpretation. A universal minimal subset of the ordinary finite diagram shapes for every possible $A$ is not asserted or needed for these results.

# B.6. Finite-set presentations {#b.6.-presentations-of-the-category-of-nonempty-finite-sets}

Composition is written right to left. Let $\mathsf F$ have skeleton $n=\{1,\ldots,n\}$, $n\ge1$. The manuscript generators in 151/017 are the permutations $\mathfrak S_n$, the inclusion $\delta_n:n\to n+1$ of the first $n$ elements, and $K_n:n+1\to n$ which fixes $1,\ldots,n$ and sends $n+1$ to $n$. Let $i_n$ extend a permutation by fixing the last element, and let $t_n=(n\ n+1)\in\mathfrak S_{n+1}$.

## B6.1. The proposed global presentation is incomplete

**Status: Refuted, with an explicit finite witness extending to all degrees.** The four displayed relation families of 151/017 do not present $\mathsf F$. Adding both global invariance families boxed in 151/005, even generalized to all degrees, still does not suffice.

The four families, with the inclusions made explicit to fix types, are

$$K_n\delta_n=\mathrm{id},\qquad
\delta_n\sigma=i_n(\sigma)\delta_n\quad(\sigma\in\mathfrak S_n),$$ $$i_{n-1}(\sigma)K_n=K_n i_n i_{n-1}(\sigma)\quad(\sigma\in\mathfrak S_{n-1}),\qquad K_n t_n=K_n.$$

The additional families are

$$(n+1\ n+2)\delta_{n+1}\delta_n=\delta_{n+1}\delta_n,
\qquad K_nK_{n+1}(n\ n+1)=K_nK_{n+1}.$$

**Countermodel.** Interpret these contravariantly in sets. Put $E_1=\{0\}$ and $E_n=\{0,1\}$ for $n\ge2$, and let every permutation act trivially. Put $p_1=\delta_1^*:E_2\to E_1$ equal to the unique map and $d_1=K_1^*:E_1\to E_2$ equal to the inclusion of $0$. For every $n\ge2$, put $p_n=d_n=\mathrm{id}_{\{0,1\}}$. The retraction equation is $p_nd_n=\mathrm{id}_{E_n}$, which holds. All equivariance and invariance equations hold because every permutation acts trivially.

In actual finite sets, however, one has the typed equation between maps $2\to2$

$$\boxed{(1\ 2)K_2(1\ 3)\delta_2=\delta_1K_1.}\tag{B6.1.1}$$

Both sides are constant with value $1$: the middle composite on the left sends both elements to $2$, and the leading transposition sends that value to $1$. In the contravariant model, the left side is $p_2d_2=\mathrm{id}_{E_2}$ and the right side is $d_1p_1$, constant with value $0$. They differ at $1$. Thus (B6.1.1) does not follow from the proposed presentation, even after both invariance families are added. Only the three objects $1,2,3$ are needed to witness the failure; the model is defined in every degree. The program checks 412 instances of the stated relations through cardinality six and the displayed missing relation. The all-degree proof is the preceding definition, not that finite bound. $\square$

Visual inspection of original 151/017 (PDF page 17, printed p. 16) reads the two lower bounds as $n\ge2$ and $n\ge3$, respectively. The alternative bounds in the supplied transcription cannot fix the failure: the omitted smallest symmetric groups are trivial, and the countermodel satisfies either reading. The margin's $p_{n+1}|\rho_{n+1}$ denotes the idempotent $\delta_nK_n$. Reading it as a permutation would be mathematically false, since this map has image of size $n$.

## B6.2. A complete replacement is available in the primary literature

**Status: Known, with a direct translation to the manuscript generators.** Grandis, *Finite sets and symmetric simplicial sets*, §3 and Theorem 4.2 [@B56Grandis2001], gives a complete presentation of finite cardinals by all elementary cofaces, codegeneracies and adjacent transpositions, subject to the cosimplicial, symmetric-group and mixed interchange relations. His §5 restricts the presentation to nonempty finite cardinals. Thus a complete corrected presentation is obtained by adding all these translated relations to the manuscript generators.

Here are explicit substitution words, including their arities. Write $c_i^{(m)}=(i\ i+1\ \cdots\ m)\in\mathfrak S_m$, with $c_m^{(m)}=1$. For the coface $d_i^{(n)}:n\to n+1$ omitting $i$, and the codegeneracy $e_i^{(n)}:n+1\to n$ identifying $i,i+1$, set $$d_i^{(n)}=c_i^{(n+1)}\delta_n\quad(1\le i\le n+1),\qquad
 e_i^{(n)}=c_i^{(n)}K_n\bigl(c_i^{(n+1)}\bigr)^{-2}
       \quad(1\le i\le n).
 \tag{B6.2.1}$$ Adjacent transpositions are $s_i=(i\ i+1)$, already present in the symmetric groups. The first word fixes positions before $i$ and moves every later old position one step to the right. In the second word, the source permutation fixes $k<i$, sends $i,i+1$ to $n,n+1$, and sends $k>i+1$ to $k-2$; $K_n$ merges the last two, and the output cycle puts the merged value back in position $i$. Thus these are exactly the indicated finite-set maps. Crucially, the last words recover the old generators literally: $d_{n+1}^{(n)}=\delta_n$ and $e_n^{(n)}=K_n$.

For a completely explicit enlarged relation scheme, use (B6.2.1) in all the following formulas, whenever their arities are positive and well typed; dimension superscripts are suppressed: $$d_i d_j=d_{j+1}d_i\ (i\le j),\qquad
 e_j e_i=e_i e_{j+1}\ (i\le j),$$ $$e_jd_i=
 \begin{cases}
 d_i e_{j-1},&i<j,\\
 1,&i=j\text{ or }i=j+1,\\
 d_{i-1}e_j,&i>j+1;
 \end{cases}$$ $$s_i^2=1,\quad s_i s_{i+1}s_i=s_{i+1}s_i s_{i+1},\quad
 s_i s_j=s_j s_i\ (i<j-1),$$ $$\begin{array}{lll}
 s_i d_j=d_j s_i &(i<j-1),&s_i e_j=e_j s_i\quad(i<j-1),\\
 s_i d_i=d_{i+1},&&s_i e_i=e_{i+1}s_i s_{i+1},\\
 s_i d_j=d_j s_{i-1}&(i>j),&s_i e_j=e_j s_{i+1}\quad(i>j),
 \end{array}
 \qquad e_i s_i=e_i.
 \tag{B6.2.2}$$ These are Grandis's (3), (10), (12), (13), with indices shifted from zero-based to one-based notation. The omitted mixed cases follow by $s_i^2=1$, exactly as in Grandis. The group equations are redundant if the complete groups $\mathfrak S_n$ and their multiplication laws are retained as the manuscript prescribes.

We verify carefully that no unspoken defining equations are missing. Let $P$ be Grandis's presented category on positive cardinals and let $Q$ be the category on the manuscript generators with their group laws, the valid manuscript equations, and all of (B6.2.2) after the substitutions (B6.2.1). Substitution defines a functor $F:P\to Q$, because every defining relation of $P$ has explicitly been imposed in $Q$. This functor is surjective on every hom-set: its image contains $\delta_n$ and $K_n$ literally and contains all adjacent transpositions, which generate each of the already imposed symmetric groups. The finite-set interpretation gives $G:Q\to\mathsf F$, because every imposed relation holds for these functions. The composite $GF$ is the standard interpretation of Grandis's generators and is an isomorphism by Theorem 4.2 and §5.

For faithfulness of $G$, choose lifts $u,v$ in $P$ of two parallel arrows of $Q$. Equality of their $G$-images gives $GF(u)=GF(v)$, hence $u=v$, and hence equality of the arrows in $Q$. Fullness follows from the same composite. Thus $Q\cong\mathsf F$, with exactly the requested old generators. This proof does not assume that generator substitutions are inverses without checking their defining equations. The auxiliary script `check_B6_translation.py` verifies all 168 coface and codegeneracy words for $1\le n\le12$; the explicit coordinate argument above proves the formulas in every arity. We make no minimality claim for this enlarged relation list.

Exact locator: Grandis, *Theory and Applications of Categories* **8** (2001), no. 8, 244--252; §3, printed pp. 247--248; Theorem 4.2, p. 249; §5, p. 250. The full primary PDF was opened and downloaded. No novelty is claimed for this replacement.

## B6.3. The corrected low-degree presentation is complete

**Status: Proved for the corrected 151/005 reading; refuted for the explicitly identified alternatives.** The final relations of 151/005 present the full subcategory $\mathsf F_{\le3}^{\mathrm{op}}$, provided the last subscript is $1$. They do not do so if that subscript is $3$, or if the erroneous relation on 151/003 is retained uncorrected.

Write the three objects $E_0,E_1,E_2$ for cardinalities $1,2,3$, respectively, and abbreviate

$$p=p_0:E_1\to E_0,\quad d=\delta_0:E_0\to E_1,
\quad q=p_{12}:E_2\to E_1,\quad e=\delta_1:E_1\to E_2.$$

The groups are $\mathfrak S_2$ and $\mathfrak S_3$. In the coordinate interpretation, let

$$\sigma(x,y)=(y,x),\quad \rho(x,y,z)=(y,z,x),
\quad\sigma_1(x,y,z)=(x,z,y),\quad\sigma_3(x,y,z)=(y,x,z).$$

Thus $\sigma_i$ fixes coordinate $i$. The corrected list is

$$pd=1,\quad \sigma d=d,\quad qe=\sigma,\quad q\rho e=dp,
\quad q\rho^2e=1,$$ $$\sigma_1e=e,\quad q\sigma_3=\sigma q,\quad ged=ed\ (g\in\mathfrak S_3),
\quad pq\sigma_1=pq,$$

together with the group equations. The coordinate maps

$$p(x,y)=x,\quad d(x)=(x,x),\quad q(x,y,z)=(x,y),\quad e(x,y)=(y,x,x)$$

satisfy them. These maps and the permutations generate all maps between sets of cardinalities at most three, by elementary inclusion and retraction factorization. Hence the presented category $Q$ maps surjectively on hom-sets to $\mathsf F_{\le3}^{\mathrm{op}}$.

We now prove injectivity by a terminating reduction and exact hom-set bounds. First combine adjacent permutations. A path which rises from $E_1$ to $E_2$ and immediately returns has a segment $qge$. Every $g\in\mathfrak S_3$ is $\rho^i h$ with $h\in\langle\sigma_1\rangle$. Since $he=e$, the three relations $q\rho^ie\in\{\sigma,dp,1\}$ eliminate this segment. A path rising from $E_0$ to $E_1$ and returning has a segment $p\sigma^\epsilon d=p d=1$. These replacements terminate: order words first by the number of $q,e$ transitions and then by the number of $p,d$ transitions. A first replacement lowers the first count; a second lowers the second without increasing the first.

Every surviving path descends in height and then ascends, with at most one valley. Paths through $E_0$ are constant maps: on the output side $\sigma d=d$ and $ged=ed$ erase all output permutations. On the input side, there is one form from $E_0$, at most two forms $p\sigma^\epsilon$ from $E_1$, and at most three forms $pqh$ from $E_2$, because $pq\sigma_1=pq$. A path with valley $E_1$ from $E_2$ to $E_2$ is $ge\sigma^\epsilon qh$. The stabilizer relation $\sigma_1e=e$ leaves three choices for the coset of $g$; the equation $q\sigma_3=\sigma q$ moves the two-element left stabilizer of $h$ into the central $\sigma^\epsilon$, leaving three choices for its coset. Thus there are at most $3\cdot2\cdot3=18$ forms of rank two. The same calculation gives at most six rank-two maps each from $E_1$ to $E_2$ or from $E_2$ to $E_1$. Finally there are at most two invertible forms at $E_1$ and six at $E_2$.

Collecting these bounds, with source cardinality indexing rows and target cardinality columns, gives

$$\begin{pmatrix}1&1&1\\2&4&8\\3&9&27\end{pmatrix}.$$

The entries are exactly $a^b=|\operatorname{Hom}_{\mathsf F^{\mathrm{op}}}(a,b)|$. Since the functor was already surjective on each hom-set, each bound is attained and it is bijective on each hom-set. It is the identity on objects, hence an isomorphism of categories. The program enumerates all 56 maps, verifies this matrix, checks the rank decomposition and every corrected relation. The reduction proof supplies completeness, which checking the relations in the target alone would not establish. $\square$

The doubtful alternatives must remain separate. On 151/005, the last relation is transcribed $p_0p_{12}\sigma_{\text{unsure }1|3}=p_0p_{12}$. The $1$ reading is the corrected presentation just proved. The $3$ reading says that first-coordinate and second-coordinate projections agree, and is false already on $(0,1,0)$. On 151/003, the transcribed $\sigma_3e=e$ is false: the two maps have coordinate values $(x,y,x)$ and $(y,x,x)$. The final list on 151/005 instead has $\sigma_1e=e$, which is true. Retaining every literal 151/003 equation together with 151/005 therefore gives a false presentation. These checks confirm the mathematical correction SA10-K151a-01 and complete the earlier partial verification SA10-R151a-08. Independent inspection of original 151/003 (PDF page 3, printed p. 2) confirms the boxed subscript $3$; inspection of the middle box on 151/005 (PDF page 5, printed p. 4) confirms subscript $1$. The final 151/005 subscript is a dense short mark and remains visually unresolved between the two supplied readings. Thus the mathematical conclusions for both readings are retained; no paleographic certainty is claimed for that final mark.

## Source and computation record

The companion files are `CHECK_EVENTS_B56.tsv`, , , , , and its `.out` file. CPU timings and complete finite outputs are in the output files. Every bounded check is separated above from its all-size proof. Sources consulted but not opened successfully are not used as premises.
