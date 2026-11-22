from pathlib import Path
p=Path(__file__).resolve().parents[1]
f=p/'paper_D.tex';s=f.read_text()
start=s.index('The manuscript writes only ``Prop. 5 ...``') if 'The manuscript writes only ``Prop. 5 ...``' in s else -1
old=r'''The manuscript writes only ``Prop. 5 ...'' at this point; there is no
complete assertion whose missing hypotheses can be recovered uniquely.
Proposition~\ref{D:prop5} states the construction explicitly and supplies
its required hypotheses. Quasi-compactness in the proof is doing real
work: a bare filtered union of categories need not satisfy descent for
an infinite clopen covering of a non-quasi-compact realization.
'''
new=r'''The manuscript writes only ``Prop. 5 ...'' at this point; there is no
complete assertion whose missing hypotheses can be recovered uniquely.
The natural assertion that the preceding filtered system, under just
the conditions actually written on 29/196--197, always defines a
ramification datum is false. In particular, connectedness of the
common quotient is not a substitute for the hypothesis used in
Proposition~\ref{D:prop5}: connectedness can be lost after restriction
to an \'etale open of the base.

\begin{example}[Refuted: the unqualified filtered construction behind Proposition 5]
\label{D:prop5-counterexample}
There is a quasi-compact noetherian base $S$ and an inverse system
$(Z_i,G_i)$ with every $Z_i$ and $Z_i/G_i$ connected, admissible
finite-group actions, surjective transition homomorphisms, and
$Z_i=Z_j/\ker(G_j\to G_i)$, for which the \'etale stackification
of the filtered categories in Proposition~\ref{D:prop5} fails R3.
The obstructing descent datum uses only rank-two objects.
\end{example}
\begin{proof}
Let $k$ be an algebraically closed field, and put
$S=\operatorname{Spec}k[t]$. We first construct a connected
non-quasi-compact scheme $B\to S$. For each $m\in\mathbb Z$ take
\[
 Q_m=\operatorname{Spec}
 k[u_m,v_m,(u_m-1)^{-1},(v_m-1)^{-1}]/(u_mv_m),
 \qquad t=u_m(u_m-1)+v_m(v_m-1).
\]
Glue $D(v_m)\subset Q_m$ to $D(u_{m+1})\subset Q_{m+1}$ by
$u_{m+1}=1-v_m$. The displayed formulas for $t$ agree. These
are open gluings with no triple intersections, so they define a
scheme. Each $Q_m$ is connected and meets $Q_{m+1}$; thus $B$ is
connected. Geometrically it is an infinite chain of affine lines,
with the point $1$ of one line identified with the point $0$ of the
next. One can also check separatedness directly: the overlap-ring
map from the tensor product of two adjacent chart rings is
surjective, since the two chart rings together provide
$v_m$, $v_m^{-1}$ and $(v_m-1)^{-1}$.

For $T=D(t)\subset S$, all nodes are removed and
\[
 B_T=\coprod_{n\geq1}E_n,
 \qquad E_n\simeq\operatorname{Spec}k[x,x^{-1},(x-1)^{-1}],
 \qquad t=x(x-1),
\]
where we choose a bijection from the integer-indexed components to
the positive integers. Each $E_n\to T$ is finite flat surjective
of degree two: its algebra is given by the monic equation
$x^2-x-t=0$, and $t$ invertible implies both $x$ and $x-1$
invertible.

Set $G_i=(\mathbb Z/2)^i$ and $Z_i=B$, with trivial actions.
The transition maps of schemes are identities and the homomorphisms
$G_j\to G_i$ are coordinate projections. All actions are admissible;
the stated connectedness and quotient conditions are immediate.
In the category over $T$, the clopen components $E_n$ are subobjects
of the terminal object already at level zero, and their realizations
cover $B_T$. On the subobject $E_n$ take the constant two-sheet
cover on which $G_n$ acts by its $n$th-coordinate character.
Regarded as an object over $B_T$, it has rank two on $E_n$ and
rank zero elsewhere, hence is piecewise constant. On all pairwise
intersections the objects are empty, so they carry a descent datum.

There is no glue at a common finite level $i$. Choose $n>i$ and
pass to a level at least $n$ to compare the proposed restriction
with the prescribed object. The $n$th-coordinate involution acts
trivially on every object inflated from level $i$, and nontrivially
on the prescribed two-sheet cover. No equivariant isomorphism can
exist. Nor can \'etale stackification on $T$ repair this: after any
nonempty \'etale base change $T'\to T$, every $E_n\times_TT'$
is still nonempty by finite faithful flatness. Any locally chosen
finite level therefore has the identical contradiction with some
$n$ larger than that level. This disproves effectiveness of the
disjoint clopen descent datum required by R3.

This example satisfies the connectedness and global bounded-rank
conditions discussed on 29/196--197. Those leaves impose
quasi-compactness on $S$, but no such hypothesis on $r(e)=B$ or the
$Z_i$; 29/191 explicitly allows realizations in all schemes over
the base. Thus the additional condition in
Proposition~\ref{D:prop5} is substantive. An alternative construction
would have to complete the filtered categories also for these
clopen descent data, rather than only for \'etale descent on $S$.
\end{proof}
'''
assert old in s
s=s.replace(old,new);f.write_text(s)
f=p/'code/prepare_checkpoint.py';s=f.read_text();s=s.replace("'D:G5-Zsets':", "'D:prop5-counterexample':('Unqualified filtered construction behind unwritten Proposition5 fails R3 even with connected Zi and affine noetherian S','Refuted','Explicit infinite nodal chain; increasing elementary abelian groups; unbounded coordinate characters','29/191,196-197','Rank2 descent objects; every etale base refinement retains every component. Restricted finite-realization repair D:prop5 remains proved.'),\n'D:G5-Zsets':")
s=s.replace('events.extend([', '''events.extend([
 ['D:prop5-counterexample','2026-11-20T02:43Z','GPT-6 Astra; /root/part_c; independent delegated audit','targeted proof check','C checked chart gluing and t compatibility, finite surjective components after D(t), coordinate-character obstruction and persistence under etale stackification; checked source29/191 and196-197 imposes only baseS quasi-compactness. Prop5 itself remains unwritten; refutation concerns its natural unqualified filtered construction.'],''');f.write_text(s)
print('Prop5 literal-scope obstruction integrated')
