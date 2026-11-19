# Independent adversarial audit of arbitrary triples and completion

Auditor: automorphisms parallel agent, GPT-6 Astra (OpenAI). Date: 2026-11-19.

Target: A-006–A-008 in sections/A_main.tex, inspected at lines 168–339 after the parent's build 14 checkpoint. This audit tries the specific failure mechanisms of underived sections, nonflat coefficient change, infinite simplicial sets, completion of nonflat products, and nonsplit filtrations. The assertions pass. A product-transport detail that should remain explicit is explained below: completed bar terms need not be flat, so one transports the universal homogeneous chain homotopy rather than assuming they are a new flat resolution.

## 1. Universal projective cycle resolutions

Let $B=\Gamma_{\mathbb Z}(T)$, and let $S$ be any ring equipped with the PD map $B\to S$, $T^{[a]}\mapsto\gamma_a(t)$. In simplicial degree $n$, write the relative coordinates as $U_1,\ldots,U_n$ and use

\[
A_{B,n}=B\otimes_{\mathbb Z}\Gamma_{\mathbb Z}(U_1,\ldots,U_n)
 \otimes_{\mathbb Z}\Lambda_{\mathbb Z}(dU_1,\ldots,dU_n).
\]

The ordinary PD Poincaré contraction integrates one variable at a time. It is $B$-linear and preserves total weight, because replacing $U^{[a]}dU$ by $U^{[a+1]}$ preserves the sum of polynomial and exterior weights. The augmented cochain complex is therefore split exact over $B$, in every simplicial degree, by homogeneous splittings. Its cycle modules are graded projective $B$-modules, as are all form modules. No flatness of $S$ over $\mathbb Z$ or $B$ has entered.

Normalization is an exact direct-summand operation, expressed by finite compositions and differences of faces and degeneracies in each simplicial degree. Consequently its terms remain graded projective, and

\[
NZ_S^i=(NZ_B^i)\otimes_BS,\qquad
NA_S^q=(NA_B^q)\otimes_BS.
\]

The important first equality is justified by the objectwise split exact sequences, not by a general assertion that tensor product preserves kernels.

The universal weight calculation gives homology only in the indicated homological degree:

\[
H_i(NZ_B^i)=I_i^B,\qquad
H_q(NA_B^q)=\mathbb Z,
\]

with all other homology zero. The $B$-action on the first module is the actual tail action, including the binomial coefficients, and the second module uses augmentation. Moreover $Z^i_{B,n}=0$ when $n<i$. Thus $NZ_B^i[-i]$ is an actual projective resolution of $I_i^B$, with no terms in negative homological degrees. After coefficient change it computes $E_i(S)$, giving $NZ_S^i\simeq E_i(S)[i]$.

The explicit normalized two-sided bar resolution used in A-005/A-006 has free $B$-terms: each positive bar variable and each last tail variable has a free integral basis. Its usual extra-degeneracy contraction over $\mathbb Z$ proves exactness before coefficient change. Thus its $S$-base change computes the derived tensor product even when $S$ has additive torsion.

## 2. The triangle is the tail-inclusion triangle

For $i>0$ use

\[
0\longrightarrow Z_S^{i-1}\longrightarrow A_S^{i-1}
\longrightarrow Z_S^i\longrightarrow0.
\]

Over $B$, the triangle is the rotation and shift of

\[
0\longrightarrow I_i^B\longrightarrow I_{i-1}^B
\longrightarrow\mathbb ZT^{[i-1]}\longrightarrow0.
\]

The induced map on the sole relevant homology module is the usual tail inclusion: in weights $w\geq i$ the dimension-shifting map identifies the same coefficient generator, and the additional weight $i-1$ is the quotient generator. Maps between modules concentrated in the same degree are determined by this module map, so there is no unseen extension-class ambiguity in the connecting map after shifting. Derived base change therefore gives the last arrow

\[
E_i(S)[i]\longrightarrow E_{i-1}(S)[i].
\]

The comparison maps can be chosen homogeneously. Sign conventions for the connecting maps are fixed by the coefficient normalization already used in A-003; the image formula itself is insensitive to a uniform sign.

## 3. Actual sections versus homotopy classes

This is the decisive point of A-006. Write $\mathcal Z=\operatorname{Hom}(X,Z_S^i)$ and $\mathcal B$ for the image of $\operatorname{Hom}(X,A_S^{i-1})$. Their quotient is the actual de Rham cohomology group.

The degreewise surjection $p:A_S^{i-1}\to Z_S^i$ is a Kan fibration of underlying simplicial sets. If a cocycle $z:X\to Z_S^i$ is nullhomotopic, represent a nullhomotopy as

\[
H:X\times\Delta[1]\longrightarrow Z_S^i,\qquad H|_{X\times\{0\}}=0.
\]

The inclusion $X\times\{0\}\to X\times\Delta[1]$ is a trivial cofibration for every simplicial set $X$. The zero lift at the initial endpoint therefore extends through $p$. At the final endpoint its lift is an actual map $a:X\to A_S^{i-1}$ with $p(a)=z$. Hence every nullhomotopic cocycle is an actual boundary. This does not require that $A_S^{i-1}$ be contractible.

It follows that quotienting actual cocycles by actual boundaries is exactly

\[
\operatorname{coker}\bigl([X,A_S^{i-1}]\longrightarrow[X,Z_S^i]\bigr).
\]

For the injectivity direction explicitly: if $[z]$ is in the image of $[a]$, then $z-p(a)$ is nullhomotopic and hence is itself $p(b)$ for an actual $b$. Thus $z=p(a+b)$.

Linearization and Dold–Kan identify

\[
[X,V]=\operatorname{Hom}_{K(S)}(C_*(X;S),NV)
=\operatorname{Hom}_{D(S)}(C_*(X;S),NV).
\]

The normalized chain module is free on the nondegenerate simplices of $X$ in each degree and is bounded below homologically, so it is K-projective. This remains true for infinitely many simplices and arbitrarily high dimension. The corresponding Hom complex uses products over source degrees; there is no direct-sum interchange.

Apply this derived Hom functor to the preceding triangle. Exactness identifies the cokernel with precisely

\[
\operatorname{im}\left(
\mathbb H^i(X;E_i(S))\longrightarrow
\mathbb H^i(X;E_{i-1}(S))\right).
\]

This proves the passage from underived sections to the derived image without replacing sections by their derived functor. Closed zero-forms are the constant simplicial coefficient object $S$, so degree zero is ordinary $H^0(X;S)$.

## 4. Products before completion

The normalized shuffle and cycle multiplication give, after shifting,

\[
I_i^B\otimes_B^{\mathbf L}I_j^B\longrightarrow I_{i+j}^B.
\]

The source has homology only in nonnegative homological degrees, while the target is in degree zero. By the standard t-structure, maps of this type are determined by their map on $H_0$. Equivalently, a projective resolution of the source mapping to a degree-zero module factors through its degree-zero homology. A-003 identifies that map with ordinary multiplication of the two tail ideals. Thus the pairing is exactly the one represented by signed bar shuffle and tail multiplication. Derived coefficient change is symmetric monoidal, so this gives the asserted pairing for $E_i(S)$.

Products on the derived Hom groups use the chain diagonal and Alexander–Whitney comparison. They are the products induced by the original simplicial cycle multiplication: the normalization/shuffle comparisons identify those maps up to their usual chain homotopies. Every boundary multiplied by a cycle is a boundary, so the product descends through the image description and is independent of all chosen preimages.

In particular, additive torsion in $S$ does not justify replacing $E_i$ by its degree-zero homology or its image ideal. The example $S=\mathbb F_2,t=0,X=\Delta[2]/\partial\Delta[2]$ in A-009 is compatible with the formula and demonstrates why that replacement would fail.

## 5. Completion: actual chain homotopies, not a claim of flatness

Assume the topology in A-007: $S$ is complete and separated for the closed PD-tail filtration, and coefficient filtration is added to the intrinsic weight of variables and exterior generators.

The normalized cycle resolutions and bar resolutions over $B$ are graded projective resolutions of the same tails. The graded comparison theorem gives homogeneous chain maps in both directions and homogeneous chain homotopies from their composites to the identity. The map between consecutive tails is likewise respected up to a homogeneous chain homotopy.

A homogeneous $B$-linear map is filtration preserving after coefficient change. To see the relevant estimate on a generator, if an input generator has intrinsic weight $v$ and an output generator has intrinsic weight $u$, its coefficient has degree $v-u$ in $B$. Its image in $S$ lies in $F^{v-u}S$. Multiplying an input coefficient in $F^aS$ gives output total filtration at least $a+v$. A polynomial input has only finitely many outputs, so the map extends uniquely by continuity to completions. The same argument applies to every chain homotopy. Their finite algebraic identities remain equalities after completion.

The Poincaré split exact sequences are also filtration preserving and remain split exact after completion. Therefore completed cycles really are the kernels of the completed differential. Finite normalization idempotents commute with this completion, giving an actual chain-homotopy equivalence

\[
N\widehat Z_S^i\simeq\widehat E_i[i].
\]

The fibration argument of section 3 applies to the underlying completed simplicial modules. It uses only degreewise surjectivity and Kan lifting; the source of the fibration need not be projective or contractible. The source $C_*(X;S)$ is still K-projective. Hence the same derived image formula is valid, with the specifically defined completed bar complexes.

**Products need one further explicit observation.** Products of copies of an arbitrary ring need not be flat. The completed bar should not be declared K-flat merely from the shape of its terms. Instead, before completion compare the two product maps from the tensor product of the universal projective resolutions to the universal target resolution. The previous section shows their equality in the graded derived category. Their source is a bounded-below complex of graded projectives, so this equality is represented by a homogeneous chain homotopy. That homotopy is jointly filtration preserving, by the same coefficient estimate, and extends to the two completed inputs. Thus multiplication transported from completed cycles is chain-homotopic to continuous bar shuffle.

This supplies an ordinary bilinear chain pairing on the completed complexes. Composing with K-flat replacements gives the derived tensor pairing when that notation is used. No assertion of flatness of the completed terms is necessary. The induced cup product and its independence of lifts therefore remain exactly the asserted ones.

The convergence of the explicit bar differential is also correct. For an output tuple, the first-face contribution sums over an initial bar index $a$, and its coefficient is multiplied by $\gamma_a(t)\in F^aS$. The remaining face contributions have only finitely many splittings of a fixed output index. The shuffle product preserves total filtration and has the corresponding finite number of splittings below each bound.

## 6. The associated-graded argument works without a section of the residue map

Now assume that the canonical graded PD map $\Gamma_k(T)\to\operatorname{gr}_FS$ is an isomorphism, with $k=S/F^1S$. The graded complex of $\widehat E_r$ is obtained from the universal graded bar resolution by

\[
B\longrightarrow k\otimes_{\mathbb Z}B=\Gamma_k(T).
\]

Its positive homology vanishes even if $k$ has torsion. Indeed the universal resolution and its tail have free integral underlying modules; the bar exactness can be split over $\mathbb Z$ in every weight, or one can use that its only homology $I_r^B$ is $\mathbb Z$-flat. Tensoring with $k$ therefore has no extra homology. The degree-zero homology is precisely the graded tail in weights at least $r$.

The augmentation to $F^rS$ sends a degree-zero tuple to its coefficient times $\gamma_b(t)$. It is filtration preserving and its associated graded is the above isomorphism on degree-zero homology. The filtered complex is complete and separated; a degree-$h$ bar generator has weight at least $r+h$.

For a cycle $z$ of positive homological degree, choose its lowest nonzero filtration piece. Exactness of the graded complex produces a primitive for that piece in the next homological degree. Subtract its differential, raising filtration by at least one, and repeat. The successive primitives converge because their filtrations tend to infinity. Their sum has differential $z$ by continuity and separatedness. The identical argument applied to the augmented degree-zero kernel proves injectivity on degree-zero homology; successive approximation of an element of $F^rS$ proves surjectivity.

Thus the augmentation is a quasi-isomorphism

\[
\widehat E_r\longrightarrow F^rS[0].
\]

The map is canonical and respects the tail inclusions and products. The proof does not choose, or need, a ring or additive section $k\to S$. Applying derived Hom yields A-008. Consecutive-tail image groups must be retained in a nonsplit filtration: they are the conclusion of the proof, rather than silently replacing them with the whole coefficient cohomology of $F^iS$.

## Audit outcome and attempted failure mechanisms

- Nonflat coefficient change: survives because universal cycles and normalization terms are projective and the differential sequences split before tensoring.
- Underived sections: survives by the explicit relative homotopy lifting argument.
- Infinite simplicial sets: survives because normalized chains are K-projective and derived Hom is product-totalized.
- Completed products of nonflat modules: survives by completed chain-homotopy equivalences and the bilinear homotopy transport described above, without assuming K-flatness.
- Nonsplit associated-graded identification: survives by graded exactness and convergent filtration corrections, without choosing coefficient lifts multiplicatively.
- Ordinary-tail replacement without the hypothesis: fails, as A-009 correctly states; no step of A-006 or A-007 makes it.

No unresolved mathematical gap was found in A-006–A-008 under the stated topology and conventions. The explicit product-homotopy argument above is the needed justification when spelling out the phrase that the product argument applies after completion.
