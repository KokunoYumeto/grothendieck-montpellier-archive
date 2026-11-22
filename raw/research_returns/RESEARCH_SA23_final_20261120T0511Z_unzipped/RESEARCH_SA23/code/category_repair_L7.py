from pathlib import Path
p=Path('RESEARCH_SA23/sections/category_L.tex');s=p.read_text();a=s.index('\\begin{proposition}[Proved: the formal Poincare lemma')
s=s[:a]+r'''\begin{proposition}[Proved: the finite-order and derived formal Poincare lemma]\label{cat:L7}
Filter the relative de Rham complex of the source map by total order,
where an augmentation-ideal factor and a one-form both have order one.
Let $K_n$ be its quotient by total order greater than $n$.
The augmentation $K_n\to A$ is a quasi-isomorphism for every $n$.
The same statement holds for the linearized complex of any stratified
coefficient module, with augmentation to that module.
Consequently
\[
 R\!\varprojlim_n K_n\simeq A
\]
in the derived category of sheaves, and likewise with coefficients.
For modules over a ring the ordinary inverse-limit complex also
computes this derived limit.  For arbitrary sheaves that last assertion
requires a derived-limit-acyclicity hypothesis on the degreewise
towers and is not asserted without it.
\end{proposition}
\begin{proof}
Translation in the groupoid identifies relative one-forms with the
completed pullback of $P$: restriction to the identity and translation
back are inverse by the groupoid identities.  On total order $N$,
Lemma~\ref{cat:L3} therefore identifies the graded complex with
\[
 \left(\operatorname{Sym}_A^{N-q}P\otimes_A\Lambda_A^qP\right)_{0\leq q\leq N},
 \qquad d(u)=du,\quad d(du)=0.
\]
Let $\iota$ be the degree-minus-one derivation on
$\operatorname{Sym}_AP\otimes_A\Lambda_AP$ that sends $du$ to $u$
and kills polynomial generators.  The graded commutator satisfies
$d\iota+\iota d=N$ on total order $N$: both sides are derivations
and agree on the generators.  For $N>0$, division by $N$ gives a
canonical contracting homotopy, defined without a basis or any choice.
Order zero is $A$ in degree zero.
The complex $K_n$ has a finite filtration by these graded pieces.
The long exact sequences of cohomology for its successive short exact
sequences prove $K_n\to A$ a quasi-isomorphism by finite induction.
This argument is valid inside the topos and makes no infinite sequence
of local choices.

A stratification identifies the two pulled-back coefficient modules.
Use that identification to trivialize the coefficient connection along
the source.  The graded homotopy above tensored with $M$ remains a
contracting homotopy; no flatness of $M$ is needed.  The same finite
filtration argument proves the coefficient statement.
The augmentations are compatible with the transition maps.
Applying the derived inverse-limit functor to this levelwise
quasi-isomorphism gives the claimed isomorphism with the derived limit
of the constant system $A$, which is $A$.
For ordinary modules, the degreewise transition maps are surjective.
A countable surjective tower of modules has no higher derived limits:
the standard difference map $\prod M_n\to\prod M_n$ is surjective
by recursively lifting its coordinates, and its kernel is $\lim M_n$.
Thus the ordinary complex computes the derived limit in that case.
This recursive argument is not valid for arbitrary sheaf epimorphisms;
we have expressly avoided using it there.
\end{proof}

\begin{proposition}[Proved: the precise connection with the crystalline starting theorem]\label{cat:L8}
For a flat formal groupoid, let its formal descent site mean the site
of the nilpotent jets of its simplicial nerve, with the topology
induced from the base and all simplicial and jet-transition maps.
A crystal on this site means a module cartesian for these transition
maps.  Such crystals are exactly stratified modules and hence, by
Theorem~\ref{cat:L6}, modules with integrable coalgebroid connection.
The finite-order resolution and its derived completion are those of
Proposition~\ref{cat:L7}.

More concretely, if $X\to S$ is a smooth morphism of
$\mathbf Q$-schemes and the groupoid is the formal completion of
$X\times_SX$ along its diagonal, this equivalence is the usual
crystalline starting equivalence: crystals of $\mathcal O$-modules
on the nilpotent infinitesimal site of $X/S$ are equivalent to
$\mathcal O_X$-modules with integrable $S$-connection.
In characteristic zero the nilpotent divided-power crystalline site
has the same objects, because divided powers are uniquely
$x^{[n]}=x^n/n!$.
\end{proposition}
\begin{proof}
A cartesian module on the nerve restricts in degree zero to an
$A$-module $M$.  The two maps from degree one to degree zero identify
its degree-one value with the two pullbacks of $M$; their comparison
is a stratification at each jet order.  The degree-two cartesian
compatibility is its cocycle identity, and the degeneracy is its
unit identity.  Conversely these identities identify the value at
every degree and every jet with the appropriate pullback of $M$;
associativity gives all higher compatibilities.  These two
constructions are mutually inverse on objects and on morphisms.
Theorem~\ref{cat:L6} proves the first equivalence, and
Proposition~\ref{cat:L7} supplies its formal Poincare resolution in
the stated pro/derived sense.

For the assertion about the usual infinitesimal site, an object is a
nilpotent closed immersion $U\hookrightarrow T$ over $S$, with $U$
open in $X$; coverings are open coverings of $T$.
Smoothness gives locally a lift $f:T\to X$ of $U\to X$.
The pullback $f^*M$ is independent of that lift in the required
canonical sense: two lifts $f,g$ agree on $U$, so the pair $(f,g)$
factors through a finite jet of the diagonal formal groupoid, and
its pullback of the stratification gives
$f^*M\simeq g^*M$.  For three lifts the cocycle identity gives the
compatibility of these identifications.  They therefore glue over
open covers of $T$, are independent of the local lifts and are
compatible with all morphisms of infinitesimal thickenings.  We obtain
a crystal.  In the reverse direction evaluate a crystal on $X$ and
on the diagonal jets; its cartesian isomorphisms give the
stratification.  Local lifting shows these operations are inverse,
because every value on $(U,T)$ is recovered as $f^*M$.
The same argument applies to module morphisms and tensor products.

For completeness the divided-power assertion uses the identity
$n!\gamma_n(x)=x^n$, forced by the divided-power axioms.  Since $n!$
is invertible, it forces the displayed formula; that formula satisfies
all axioms and is finite on nilpotent elements.  Hence adding divided
powers supplies no extra datum here.
The margin on 162-5/031 is thus justified by an actual formal descent
site and, for smooth schemes, by the ordinary crystalline site.  The
arbitrary-flat integration theorem itself uses coalgebroids as in
Theorem~\ref{cat:L5}; no unjustified ordinary inverse-limit exactness
in an arbitrary topos is needed.
\end{proof}
'''
p.write_text(s);print('Repaired L7; added L8',len(s))
