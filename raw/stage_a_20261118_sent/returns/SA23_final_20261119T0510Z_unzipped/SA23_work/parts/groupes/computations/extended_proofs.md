# Extended verification arguments

These arguments are reconstructions made in this run. They are not additions to the historical transcription. A finite test below verifies its stated witness; it never substitutes for the unrestricted argument. Bibliographic keys refer to the opened sources in `references.bib`.

## C-SA23-groupes-003: relative and ambient monicity

For an adjunction $L\dashv R$, the comparison on morphisms from $X$ to $Y$ is the map induced by the unit $\eta_Y:Y\to RLY$. Faithfulness of the restriction to a full subcategory $E'$ says precisely that these maps are injective for $X,Y\in E'$. It tests monicity only against objects of $E'$. Ambient monicity tests against every object of $E$, a stronger requirement.

In the seven-arrow category saved by the program, $T$ is terminal and $E'=\{Y,T\}$ is full and thin. The functor $E\to1$ therefore restricts faithfully to $E'$, and the right adjoint selects $T\in E'$. Nevertheless $h:Y\to T$ equalizes the distinct arrows $f,g:Z\to Y$. The program checks the category axioms, terminality, restricted faithfulness and the unequal pair. The historical parenthesis may have meant relative monicity; that interpretation is retained rather than declared an ink error. [RiehlContextOnline, Lemma 4.5.11 for the global adjunction criterion.]

## C-SA23-groupes-010–011: the inverse-pairing sign

Work in a symmetric monoidal category, using coherence to suppress associators. For an invertible object $L$, tensor cancellation identifies automorphisms of $L^{\otimes2}$ with scalars in $\operatorname{Aut}(1)$. Write its self-commutor as the scalar $\epsilon(L)$. Symmetry gives $\epsilon(L)^2=1$. Each adjacent transposition of equal factors contributes this scalar; hence a permutation contributes $\epsilon(L)^{\operatorname{parity}(\sigma)}$, with parity in $\{0,1\}$.

Let $\phi:L\otimes L'\xrightarrow{\sim}1$, define $\phi_{\rm rev}=\phi c_{L',L}$, and define $\psi:L'\otimes L\to1$ by $\phi\otimes1_L=1_L\otimes\psi$. Naturality of symmetry with respect to $\phi$ gives

\[
\phi\otimes1_L=(1_L\otimes\phi)c_{L\otimes L',L}
=\epsilon(L)(1_L\otimes\phi)(1_L\otimes c_{L',L})
=1_L\otimes(\epsilon(L)\phi_{\rm rev}).
\]

Cancellation of tensoring with $L$ proves $\psi=\epsilon(L)\phi_{\rm rev}$. An odd superline has $\epsilon=-1$: normalized evaluation has value $1$, its reversed pairing has value $-1$, and $\psi$ again has value $1$. This proves the sign, rather than merely observing it in one model. The program checks adjacent-generator parity through six factors and the scalar example. The exponent written as “sign” must be interpreted as parity, not as the numerical values $+1,-1$.

## C-SA23-groupes-016: semilinear conjugation

Fix the convention that the semilinear action is $\rho(\sigma)\circ\sigma$, with $\sigma$ acting on coefficients. A tensor grading represented by $j$ is invariant exactly when

\[
\rho(\sigma)\,\sigma(j(t))\,\rho(\sigma)^{-1}=j(t).
\]

Rearrangement gives $\sigma(j)=\rho(\sigma)^{-1}j\rho(\sigma)$. In the program $j=S\operatorname{diag}(1,t)S^{-1}$ and $\rho=S\bar S^{-1}$, with $S=\left(\begin{smallmatrix}1&i\\0&1\end{smallmatrix}\right)$. Exact symbolic subtraction is zero in the correct direction and nonzero for the opposite conjugation. This establishes a convention-dependent identity. It does not supply the admissibility or comparison theorem missing from the next historical paragraph. [Ziegler2015, Theorem 3.6; compare Liu2013, Theorem 2.2.1 only under its crystalline hypotheses.]

## C-SA23-groupes-023: capturing data at a transfinite stage

Let $\kappa$ be regular and larger than the number of arrows in every allowed diagram shape and in each prescribed test category. A diagram involving fewer than $\kappa$ objects, arrows and relations in a $\kappa$-stage union is represented before some stage: take the supremum of the fewer than $\kappa$ stages at which its data occur. Equality of morphisms, a natural transformation, or an inverse with its two identities is handled by including its witnesses in the same list. The supremum is still below $\kappa$.

The cardinal inequality alone does not give this conclusion. With $\pi=\aleph_\omega$, the countable stages $\aleph_n$ are unbounded, although the size of the indexing list is less than $\pi$. This is the exact gap in the first version. The later requirement that the index be “grand devant” the bound supplies the missing cofinality condition. This repair proves the iteration step only after the successor construction has its stated universal properties; it does not construct the omitted $K$. [Kelly1982, Theorem 5.35; LackTendas2023 for rank conventions.]

## C-SA23-groupes-032: locally constant objects and filtered colimits

Let $C=\{0,1\}^{\mathbb N}$ and $p=(0,0,\ldots)$. Let $V_n$ be the clopen cylinder where the first $n$ coordinates are zero, and set $U_n=C\setminus V_n$. The subterminal sheaves $U_n$ are locally constant, while their filtered union $C\setminus\{p\}$ is not clopen and hence is not locally constant at $p$.

For a counterexample using constant objects themselves, take constant two-element sheaves and let the $n$-th transition fix the first element everywhere, while sending the second to the first on $U_n$ and fixing it on $V_n$. This is a sheaf morphism because both pieces are clopen. At $p$ all transitions are identities, so the colimit stalk has two elements. At any other point the transitions eventually collapse, so the colimit stalk has one element. The colimit is neither constant nor locally constant. A geometric full property category must survive this filtered-colimit test; a structured theory with additional chosen data has different morphisms.

## C-SA23-groupes-039–040: zero-dimensional rings and noetherian fppf tests

For a commutative ring, a unit/nilpotent decomposition of every $f$ immediately gives dimension zero: in every prime quotient, a nonzero $f$ belongs to the unit component and is invertible. Conversely, in a zero-dimensional affine spectrum (D(f)) is clopen, hence defined by an idempotent $e$. On $eA$, $f$ is a unit; on ((1-e)A), it is in every prime, so some power is zero. It follows that $f^nA=eA$ for large enough $n$. If powers stabilize, $f^n=f^{n+1}g$ shows directly in each prime quotient that nonzero $f$ is invertible, giving the converse.

The fppf question is different. The exact opened noetherian classification says that a noetherian fppf-local ring is an algebraically closed field. Such field-valued points cannot see a nonzero nilpotent. Thus every test point of $\operatorname{Spec}(\mathbf F_p[\varepsilon]/\varepsilon^2)$ factors through its reduced closed point. This closed immersion is not an fppf covering sieve: a faithfully flat ring map is injective and cannot kill $\varepsilon\ne0$. Equivalently the inclusion $(\varepsilon)\hookrightarrow A$, after tensoring with $A/(\varepsilon)$, becomes a zero map from a nonzero one-dimensional module. The saved finite-ring checks verify these concrete identities for $p=2,3,5$. [Schroer2016, Proposition 4.4 and Corollary 4.5; publication 2017.]

## C-SA23-groupes-044: the irreducibility/coherence distinction

For $n\ge2$, let $A_n=k[x,y]/(xy,x^n,y^n)$. Each $A_n$ has a single prime ((x,y)), so its spectrum is irreducible. In a nonprincipal ultraproduct, the classes of $x$ and $y$ are each nonnilpotent: for every fixed exponent $m$, their $m$-th powers are nonzero for all $n>m$. Their product is zero. Thus the nilradical of the ultraproduct is not prime.

This disproves a coherent axiomatization of the same class in the given ordinary ring signature, since such first-order axioms are preserved by ultraproducts. It does not by itself prove that no Morita-equivalent presentation in a different signature has a coherent classifying topos. The source’s inserted “coherent” and its component-structure ambiguity remain separate reading questions.

## C-SA23-groupes-046–048 and 096: decomposition equations

Suppose $e^2=e$, $f^n(1-e)=0$, $g(1-e)=0$, and $fg=e$. Then $g=eg$, and $f$ is invertible with inverse $g$ on the $e$-component, while $f$ is nilpotent on its complement. If ((e',g')) is a second solution, then

\[
e(1-e')=f^ng^n(1-e')=0,
\]

and symmetrically $e'(1-e)=0$, so $e=e'$. Uniqueness of the inverse on that component gives $g=g'$. This is the general monomorphism proof. The finite enumeration over $\mathbf Z/m\mathbf Z$ tests at most one solution, not existence for every $f$.

Setting $e=1$ gives the unit scheme; setting $e=0$ gives $f^n=0,g=0$. Their disjoint affine-scheme coproduct is therefore the represented $D_n$. A map from a disconnected affine test scheme may meet both summands, explaining why the corresponding representable is not their coproduct in presheaves.

For the quasi-inverse presentation $x^2y=x,xy^2=y$, set $e=xy$. Exact polynomial reduction gives $e^2=e$, $ex=x$, $ey=y$. The $e$-part has $xy=1$; the complementary part has $x=y=0$. The ring is consequently $\mathbf Z[t,t^{-1}]\times\mathbf Z$. If $b,c$ are two quasi-inverses of $a$, then $b=b^2a=b^2a^2c=(ab)^2c=abc$, and likewise $c=abc$, proving uniqueness.

The universal absolutely flat reflection (T(A)) changes the spectrum to its constructible topology and retains residue fields. A map inducing a bijection of spectra and isomorphisms of all residue fields becomes an isomorphism after this reflection: the induced continuous bijection of compact Hausdorff constructible spectra is a homeomorphism, and the stalk maps are isomorphisms of fields. Conversely the displayed quasi-inverse map itself has that spectrum/residue-field property. This proves the orthogonality comparison under the stated commutative-ring conventions. [Olivier1967, Proposition 5; Stevenson2014, Proposition 3.3 and Theorem 3.9; CaramelloJohnstone2009, §1.]

For C047, the internal/global distinction has a separate counterexample. In $\mathbf{Set}^{\mathbb N}$, take component rings (k[t]/t^{n+1}). Each is local and zero-dimensional. In the global product, $f=(t,t,\ldots)$ is not nilpotent, and on no nonzero idempotent component is it a unit. The source’s sectionwise reading is therefore stronger than its internal local condition.

## C-SA23-groupes-050–051: pro-objects and the rational locus

For a profinite set $P=\varprojlim P_i$, evaluation of the associated limit of representables on a finite discrete test set $X$ is $\operatorname{Hom}_{\rm Set}(X,P)$. Any function of underlying sets therefore gives a natural transformation on these tests; continuity is lost. For example the function on Cantor space taking value $1$ only at the all-zero sequence is not continuous but induces such a natural transformation. The naive functor from pro-finite sets to these presheaves is not fully faithful.

The arithmetic example is sharper. A nonzero finite-type $\mathbf Z$-algebra has a maximal residue field of positive characteristic, so cannot contain $\mathbf Q$. Therefore the limit of the representable open loci where all positive integers are inverted has empty value on every nonempty finite-type affine $\mathbf Z$-scheme. Its presheaf behaves like the empty affine, whereas the theory of $\mathbf Q$-algebras is nontrivial. The latter is obtained by imposing every inversion axiom in the theory, not by declaring that presheaf limit an open subtopos. [StacksJacobson, Lemma 10.35.19.]

## C-SA23-groupes-056–058: component bounds and torsors

A bound of $n$ on the number of nonzero orthogonal idempotents in a partition of $1$ forces the Boolean algebra of idempotents to be finite with at most $n$ atoms. Indeed, successively splitting any non-atom yields a strictly larger finite partition; the bound forces the process to stop. Its atoms give the connected factors. Merely saying “at most $n$ atoms” without finiteness would be wrong: an infinite atomless Boolean algebra has no atoms.

For exact rank, repeat the idempotent endomorphism $F:k^n\to k^n$, $F(a_1,\ldots,a_n)=(a_1,\ldots,a_1)$. The colimit of a repeated idempotent is its image: the inclusion and retraction give a cocone, and every compatible cocone is constant on each idempotent fibre. Thus the colimit is $k$. This refutes filtered-colimit closure of the full exact-$n$-component property for $n\ge2$. It does not refute a theory with a chosen decomposition and only decomposition-compatible arrows.

If a given decomposition has $n$ connected nonzero factors, its orderings form an $S_n$-torsor. The torsor identities survive inverse image because finite limits and epimorphisms do. That observation does not prove that the source’s construction of the sheaf of *all* decompositions, through a largest connected-factor locus, commutes with arbitrary inverse image. That remains the precise residual claim.

## C-SA23-groupes-060–064 and 112: module tests

The directed module system $\mathbf Z\xrightarrow{2}\mathbf Z\xrightarrow{2}\cdots$ has colimit $\mathbf Z[1/2]$. Every stage is free of rank one and faithfully flat. The colimit is not finitely generated and has zero tensor product with $\mathbf Z/2$, so is not faithfully flat. It is not projective: a projective abelian group is free, while every element here is divisible by every power of $2$. The maps are module maps, not unital algebra maps. The same multiplication-by-$2$ map, after tensoring with $\mathbf Z/2$, is zero and nonmonic, so this tensor functor is additive but not left exact.

For ordinary injectivity, every vector space is injective as a module over its field. Pull back $k$ to the constant sheaf on the circle. It embeds as the first-coordinate local system in the rank-two local system with monodromy $N=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$. An invariant retraction would have row ((1,b)), but $(1,b)N-(1,b)=(0,1)$. No such retraction exists. Thus the constant sheaf is not an injective sheaf of modules. This addresses categorical injectivity; it does not assign a meaning to an unspecified internal injectivity predicate.

For the tensor-invertibility test, let evaluation $M\otimes_A M^*\to A$ be an isomorphism and write its inverse image of $1$ as $\sum m_i\otimes\phi_i$. The finitely many values $\phi_i(m_i)$ generate $A$. On an open (D(s)) where one is a unit, put $F=(M^*)_s$ and normalize so $\phi(m)=1$. Then $M_s=A_s m\oplus N$, with $N=\ker\phi$, and $F$ contains $A_s\phi$ as a direct summand, split by evaluation at $m$. Consequently $N\otimes A_s\phi\cong N$ embeds as a direct summand in $M_s\otimes F$ and lies in the kernel of the localized evaluation isomorphism. Injectivity forces $N=0$. A finite such open cover proves that $M$ is finite locally free of rank one. This argument never identifies $F$ with $\operatorname{Hom}_{A_s}(M_s,A_s)$ before finite projectivity is known. The ega owner independently checked this local splitting argument and found no missing finiteness hypothesis.

Global cyclicity still fails. In $\mathbf Z[\sqrt{-5}]$, $I=(2,1+\sqrt{-5})$ satisfies $I^2=(2)$, as the saved integral linear combinations show. It is invertible, with inverse (I/2), but not principal: its norm is $2$, and $a^2+5b^2=2$ has no integer solution. The program’s bounded norm check is exhaustive because that equation forces $b=0$ and $|a|\le1$. [StacksFlatness; StacksInvertible.]

## C-SA23-groupes-066 and 068–069: two cardinal counterexamples

The functor $F(X)=X^{\mathbb N}$ preserves $\aleph_1$-filtered colimits of sets. Every countable list of representatives, and every countable list of equalities between them, has a common later stage. For arbitrarily large singular cardinals $\lambda$ of countable cofinality, König’s theorem gives $\lambda^{\aleph_0}>\lambda$. A set of size $\lambda$ is $\lambda^+$-presentable, but its image under $F$ is not. Thus preservation of presentable objects does not hold at every sufficiently large regular rank. The standard sharply-larger-cardinal theorem has different quantifiers. [LackTendas2023, Definitions 2.3 and Propositions 2.5–2.6.]

For the stronger filtration bound, let $C$ be a small skeleton of countable sets and let $X$ have singular cardinality $\lambda$ of countable cofinality. Suppose $X$ has an $\aleph_1$-directed presentation by objects of $C$, with a cofinal family of at most $\lambda$ stages. The images of those stages give a family $A_\alpha$, $\alpha<\lambda$, cofinal among the countable subsets of $X$: countably many chosen representatives have a common upper stage. Choose cardinals $\lambda_n<\lambda$ increasing cofinally to $\lambda$. The union of the first $\lambda_n$ countable sets has size less than $\lambda$, so choose $x_n$ outside it. The countable set $\{x_n:n\in\mathbb N\}$ is contained in no $A_\alpha$, a contradiction. This proves the failure of the stated bound without an unproved cardinal-arithmetic assumption.

Ordinary filteredness cannot replace $\aleph_1$-directedness: the countable idempotent chain used to split a retract is filtered, but the set of all its stages has no upper bound. Nor does a bound by $\mu^\nu$ imply a bound by $\mu$. The source’s questioned exponent estimate is retained as a genuine gap.

## C-SA23-groupes-071: the empty object in Set opposite

Fix a regular infinite $\kappa$. If $X$ has at least two elements, choose a set $S$ with $|S|\ge\kappa$ and the inverse system $2^J$ over $J\subset S$, $|J|<\kappa$. Its limit is $2^S$. A function detecting just the all-zero sequence cannot factor through any of these coordinate projections. Therefore $\operatorname{Hom}_{\rm Set}(-,X)$ fails the required cofiltered-limit comparison.

For $X=\varnothing$, use $Y_J=\operatorname{Inj}(J,\kappa)$ for $J\subset\kappa^+$, $|J|<\kappa$, with restriction maps. All $Y_J$ are nonempty, and the index is $\kappa$-cofiltered in the inverse-system convention. Its limit would be an injection $\kappa^+\to\kappa$, so is empty. The comparison for Hom into the empty set has empty source and singleton target. A singleton $X$, by contrast, gives the constant singleton Hom functor and is presentable. Since filtered colimits in the opposite of a family consisting only of singletons again give a singleton, these objects cannot generate Set opposite. [For the separate Ab-opposite result, Beke2000, Remark 3.3, with the accessible-opposite theorem it cites.]

## C-SA23-groupes-083–085, 093–095 and 101: recovery requires the correct completion

For small finitely complete $R$, a left-exact functor $R\to\mathbf{Set}$ is a filtered colimit of covariant representables. A finitely presentable model has its identity factor through one representable stage, hence is a retract of it. Equalizers split idempotents in $R$, so that retract is representable. This gives $\operatorname{Lex}(R,\mathbf{Set})_{\rm fp}\simeq R^{\rm op}$. The finite-limit hypothesis is doing real work.

For $L\dashv U:S'\to S$, the comparison $\operatorname{Hom}(La,-)=\operatorname{Hom}(a,U-)$ proves that $U$ preserves filtered colimits exactly when $L$ preserves finite presentability, since finitely presentable $a$ form a strong generator. Putting this condition on $U$ is wrong: Groups→Set preserves filtered colimits, while the finitely presented group $\mathbf Z$ has an infinite underlying set. The manuscript itself corrects the adjoint later.

Finite-product theories recover only the appropriate Cauchy/Morita presentation. Every finite set is a retract of an even finite set, so the opposite categories of all finite sets and of even finite sets have equivalent Set models but are not equivalent theories before completion. For the separate detection question in $R=\mathrm{FinSet}^{\rm op}$, the object $1$ is a retract of $2$, and every object is a finite product of $1$. Natural transformations between product-preserving functors are therefore determined at $2$. Yet the product closure of $2$ consists of sizes $2m$, not $2^m$, and misses $1$ and $3$.

Finite presentables are generally closed under finite colimits and retracts, not finite limits. For $A=k\oplus V$, $V^2=0$, with $V$ countably infinite-dimensional, multiplication by a nonzero $x\in V$ is an endomorphism of the finitely presented module $A$. Its kernel is $V$, which is not finitely generated because the action on it factors through $k$. The finite-dimensional approximations in the program illustrate the kernel calculation; the infinite-dimensional argument proves the claim.

For the finite-product theory $R=(\text{finite free abelian groups})^{\rm op}$, ordinary models are all abelian groups. Flat functors are filtered colimits of representables, corresponding to filtered colimits of finite free abelian groups, hence torsion-free groups. The model $\mathbf Z/2$ is therefore not a point of the proposed presheaf classifier. Finally, a faithful structure-forgetting functor on all internal group models does not make the induced classifier inverse image faithful: every group is inhabited, so that classifier morphism factors through the proper inhabited-object open of the object classifier. Its inverse image is not conservative. A faithful functor reflects monomorphisms and epimorphisms; between topoi, which are balanced, it therefore reflects isomorphisms. This proves the failure of faithfulness. [AdamekLawvereRosicky2003; MakkaiPitts1987; SGA4I1972, IV Exercise 7.6; StacksFlatness, Lazard’s theorem.]

## C-SA23-groupes-106–107: variance and the fixed-object classifier

For a left-exact site functor $f_0:C\to E$, the comma category of pairs $(c,U\to f_0c)$ is cofiltered: finite products and equalizers are supplied by the corresponding limits in $C$. A contravariant stack on $C$ must therefore be extended using the opposite indexing category. Its bicategorical Kan extension gives a prestack, and stackification is an additional step. Replacing the 2-colimit by a colimit of sets or omitting stackification loses descent data. [StacksPullback, Lemmas 8.12.5–8.12.10.]

If $B\to B_I$ records the underlying family of the classified structure and $X\to B_I$ classifies chosen objects $E_i\in X$, the bicategorical pullback $B\times_{B_I}X$ has the required universal property. A morphism $Y\to B\times_{B_I}X$ is a pair of morphisms to $B,X$ and an invertible comparison of their underlying $I$-families. This comparison is exactly the specified family of underlying-object isomorphisms. Existence of the 2-pullback is an external topos theorem, not proved by merely drawing its square. [SGA4I1972, IV 9.1.6$d$; Vickers2017, Theorems 5.11–5.12 for the checked arithmetic-universe formulation.]

## C-SA23-groupes-109–110: finiteness and absence of points

The filtered union $k[x_1,\ldots,x_n]\to k[x_1,\ldots,x_{n+1}]\$ gives $k[x_1,x_2,\ldots]$. Its ideal generated by all variables is not finitely generated, so it is not noetherian. This defeats the full-property geometric interpretation for the usual noetherian finiteness conditions. Alternative nonnoetherian definitions of regularity, CM or Gorenstein are not supplied by the fragment and are not decided here.

For artinianness and finite idempotent sets, use the Boolean rings $\mathbf F_2^{2^n}$ with coordinate-duplication embeddings. Their union is the ring of clopen cylinder subsets of Cantor space. The strictly decreasing cylinders $V_n$ give strictly decreasing principal ideals, so this ring is not artinian. Every element is idempotent and there are infinitely many.

Let $B$ be a nontrivial complete atomless Boolean algebra, such as the regular-open algebra of the real line. A point of its locale is a frame map $p:B\to2$. Let $b=\bigvee\{x:p(x)=0\}$. Preservation of arbitrary joins gives $p(b)=0$, so $a=\neg b\ne0$. Every nonzero $c\le a$ must have $p(c)=1$; if $0<c<a$, then both $c$ and $a\wedge\neg c$ map to $1$, contradicting preservation of their zero meet. Thus $a$ would be an atom. There is no such point, while $0\ne1$ proves the sheaf topos nondegenerate. [Barr1974, opening argument.]

## C-SA23-groupes-114: the intrinsic representability question

For a weighted bilimit $L$ in a 2-category $\Delta$, its universal equivalence evaluated at $R$ says exactly that $\Delta(R,-)$ preserves that bilimit. This proves the proposed necessary condition directly.

A sufficient theorem needs more. Under the precise finite bi-accessibility and bilimit hypotheses of DiLibertiOsmond2025, Theorem 5.2.3, a pseudofunctor $T:\Delta\to\mathbf{Cat}$ preserving weighted bilimits and bifiltered bicolimits has a left biadjoint $L$. Evaluating the biadjunction at the terminal category yields $\Delta(L1,C)\simeq\mathbf{Cat}(1,T(C))\simeq T(C)$. This is a conditional representing object. No argument on the manuscript page verifies those hypotheses for its arbitrary doctrine, and no unconditional converse is asserted here.
