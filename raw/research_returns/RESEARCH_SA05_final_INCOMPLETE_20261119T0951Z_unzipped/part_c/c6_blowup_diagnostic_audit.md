# Independent audit of the two-component blowup diagnostic

Recorded 19 November 2026, 08:33 UTC, after the complete written audit. We independently read every line of Part D's
`post07/bgv_semistable_blowup_diagnostic.md` and checked the following arguments.
This is an audit of a failed converse method, not a geometric counterexample to
coefficient-prime independence and not a smaller universal gate.

Let a smooth projective variety \(X/k\), with \(k\) finite, have codimension
\(c\geq1\) in \(\mathbf P^N_k\). Its regular immersion in
\(\mathbf P^N_{W(k)}\) has local ideal \((p,t_1,\ldots,t_c)\) after an étale
localization: independent local equations for the smooth embedding extend to
an étale coordinate system. The blowup charts are smooth over \(W(k)\) in the
\(p\)-chart and have equation \(p=t_i v\) in a \(t_i\)-chart. They are regular
and flat, with reduced transverse special-fibre components. The generic
fibre remains \(\mathbf P^N_K\).

The two components and their intersection are the strict transform
\(Y_1=\operatorname{Bl}_X\mathbf P^N_k\), the exceptional projective bundle
\(E=\mathbf P_X(N_{X/\mathbf P^N_{W(k)}})\), and
\(D=\mathbf P_X(N_{X/\mathbf P^N_k})\). The normal exact sequence need not
split. Its subbundle inclusion suffices to identify \(D\) and the restricted
relative hyperplane class. The projective-bundle formula therefore proves
\(H^m(E,\mathbf Q_\ell)\twoheadrightarrow H^m(D,\mathbf Q_\ell)\) for every
\(m\) and every \(\ell\ne p\). Dualizing the restriction in the complementary
degree gives the Gysin injection
\(H^{q-2}(D)(-1)\hookrightarrow H^q(E)\); it also gives injectivity into the
two-component direct sum.

The fixed-weight Rapoport–Zink row consequently has injective first and
surjective last differential:

\[
H^{q-2}(D)(-1)\longrightarrow H^q(Y_1)\oplus H^q(E)
\longrightarrow H^q(D).
\]

There are no triple intersections, so the two outer \(E_2\)-columns vanish.
The middle column is the cohomology of the Tate generic fibre by convergence;
equivalently the displayed blowup and projective-bundle multiplicities cancel.
This argument uses no weight–monodromy conjecture.

After a transverse relative complete-intersection cut, the maps
\(D'\to E'\to X\) remain compatible. The pullback of any cycle class from
\(X\), and its product by any class restricted from \(E'\), is therefore in
the restriction image. These particular classes vanish in the outer
restriction cokernel which is the target of the sole possible monodromy
block. No assertion is made about newly created primitive cohomology or
about the impossibility of another construction.

The exact source dependency is the previously opened Rapoport–Zink
Satz 2.10 and formula (2.11), printed pp. 40–41. The local charts, normal-bundle
argument, projective-bundle surjectivity, duality, and cut-class cancellation
were checked directly here. This audit does not assert that arbitrary cycles
on the residue variety lift to the generic fibre.
