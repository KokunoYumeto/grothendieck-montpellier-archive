from pathlib import Path
p=Path(__file__).resolve().parents[1]
f=p/'paper_D.tex'; s=f.read_text()
s=s.replace('The completely arbitrary-base formulation\nis kept separate in the unresolved part.','For a completely arbitrary base, Proposition~\\ref{D:boundary-arbitrary}\nadds a necessary and sufficient constructibility condition on boundary\ncohomology. Example~\\ref{D:boundary-nonconstructible} shows why that\ncondition cannot be omitted.')
insert=r'''
\begin{proposition}[Proved: the exact criterion over an arbitrary base]
\label{D:boundary-arbitrary}
Keep $f,X,Y,j,h,G$ as above, but let $S$ be an arbitrary scheme.
Write $i:Y\hookrightarrow X$ and $g=f i$, and define the boundary
cohomology complex
\[
 C_Y(G)=Rg_*i^*Rj_*G.
\]
Then all $R^q h_*G$ are locally constant if and only if the following
two conditions hold:
\begin{enumerate}
\item Every cohomology sheaf $\mathcal H^q C_Y(G)$ is constructible
(locally on $S$).
\item The boundary hypercohomology in
\eqref{D:boundary-condition} vanishes for every geometric
specialization $\bar s\leftarrow\bar t$.
\end{enumerate}
In relative dimension one the second condition is pointwise vanishing
on the finite geometric boundary. The first condition remains necessary
on an arbitrary base, even for a relative curve.
\end{proposition}
\begin{proof}
Localization for the open--closed decomposition of $X$ gives a triangle
\[
 Rh_!G\longrightarrow Rh_*G\longrightarrow C_Y(G)\longrightarrow.
\]
The functor $Rh_!$ has constructible cohomology on an arbitrary base:
$h$ is compactifiable and of finite presentation, and
\cite[XVII, Theorem 5.3.6, p.~364]{SGA4D} applies to the finite
coefficient ring $\mathbb Z/n$. This theorem explicitly reduces the
arbitrary affine base to a noetherian one by limits; it does not impose
noetherianity on $S$. Its cohomology is locally bounded, by
\cite[XVII, Corollary 5.2.8.1, p.~358]{SGA4D}.
Constructible finite-coefficient sheaves form an abelian category
closed under extensions, locally on every scheme. The long exact
cohomology sequence therefore proves
\[
 \bigl(\mathcal H^q C_Y(G)\text{ constructible for every }q\bigr)
 \ \Longleftrightarrow\
 \bigl(R^q h_*G\text{ constructible for every }q\bigr).
\]
No boundedness assertion about $Rh_*G$ is needed: each term is governed
by a finite segment of this long exact sequence.

The proper-base-change calculation in the preceding proof did not
use its finiteness hypothesis on irreducible components. Thus condition
(2) is equivalent to all specialization maps of every $R^q h_*G$
being isomorphisms. For a constructible sheaf this is equivalent to
local constancy on an arbitrary scheme, by
\cite[IX, Proposition 2.11, p.~20]{SGA4D}.
We spell out the relevant finiteness step. At a geometric point,
finitely many generators and relations spread to an \'etale
neighborhood, giving a map from the constant finite module with the
prescribed stalk to the sheaf, which is an isomorphism at that point.
Its kernel and cokernel are constructible, so their zero loci, and
hence the isomorphism locus, are locally constructible. Because both
sheaves have isomorphic specialization maps, that locus is stable
under generization. A locally constructible generization-stable
subset of a scheme is open. Restricting to this open proves local
constancy. This proves sufficiency.

Conversely, locally constant $R^q h_*G$ have isomorphic specialization
maps. Their stalks are finite by specialization to a geometric generic
point, followed by the reduction and topological-invariance argument
in the preceding proof. They are therefore constructible. The same
localization triangle then proves constructibility of the boundary
cohomology sheaves. This proves necessity.
\end{proof}

\begin{example}[Refuted: specialization alone over an arbitrary base]
\label{D:boundary-nonconstructible}
There exist an affine characteristic-two base $S$, the smooth proper
relative curve $X=\mathbb P^1_S$, the boundary section $Y=\{\infty\}$,
and a rank-one locally constant $\mathbb F_3$-sheaf $G$ on
$\mathbb A^1_S$ such that all the boundary comparison complexes in
\eqref{D:boundary-condition} vanish, while $h_*G$ is not locally
constant. All $R^q h_*G$ for $q>0$ are zero.
\end{example}
\begin{proof}
Let $k=\overline{\mathbb F}_2$, let $K$ be an algebraic closure of
$k((t))$, and let $V$ be the valuation ring of an extension of the
$t$-adic valuation to $K$. It is a strictly henselian rank-one
valuation ring, with residue field $k$, fraction field $K$, and
exactly two prime ideals. Let $A$ be the ring of eventually constant
$k$-valued sequences indexed by the positive integers, equipped with
the eventual-value map $A\to k$. Put
\[
 R=V\times_k A,\qquad S=\operatorname{Spec}R,
 \qquad a=(t,(0,0,\ldots))\in R.
\]
The finite-support sequences form an ideal $I$ of $A$. Each coordinate
idempotent $e_n=(0,\delta_n)$ gives an isolated clopen point $n$ of
$S$ with residue field $k$. Every other prime contains all these
idempotents, hence contains $0\times I$ and corresponds to a prime of
$R/(0\times I)=V$. Thus the remaining points are a generic point
$\eta$ and its specialization $m$. Their local rings are $K$ and
$V$, respectively: localization at $m$ kills every $e_n$ since
$1-e_n$ is a unit there. Every neighborhood of $m$ contains all but
finitely many isolated points $n$, since a sequence whose eventual
value is nonzero is nonzero at all but finitely many coordinates.
Also $D(a)=\operatorname{Spec}K$.

Write $\Lambda=\mathbb F_3$, and let
$G=\mathcal L_\psi(ax)$ be the sign summand of the finite \'etale
Artin--Schreier cover $z^2-z=ax$. For $i_0:V(a)\hookrightarrow S$
and $j_0:D(a)\hookrightarrow S$, we claim
\begin{equation}\label{D:AS-duality}
 Rh_*G \simeq i_{0*}Ri_0^!\Lambda
 \simeq \operatorname{Cone}(\Lambda_S\longrightarrow
 Rj_{0*}\Lambda_K)[-1].
\end{equation}
Here no noetherian approximation of ordinary direct image is asserted.
To prove the formula, first use the universal family
$\mathcal L_\psi(cx)$ on $\mathbb A^1_x\times\mathbb A^1_c$.
Its compactly supported cohomology on every fibre $c\ne0$ is zero.
Indeed the Artin--Schreier cover is itself an affine line, whose
compactly supported cohomology is $\Lambda(-1)[-2]$, and translation
by the deck involution acts trivially on that top cohomology; its
sign summand is zero. At $c=0$ the sheaf is constant, with compact
cohomology $\Lambda(-1)[-2]$. Proper-support base change and localization
therefore identify the universal direct image with
$0_*\Lambda(-1)[-2]$. Arbitrary base change
\cite[XVII, Theorem 5.2.6, p.~357]{SGA4D} now gives
\[
 Rh_!G^\vee\simeq i_{0*}\Lambda(-1)[-2].
\]
Poincar\'e duality for a smooth compactifiable morphism over a
quasi-compact quasi-separated base is valid without noetherianity:
\cite[XVIII, Theorem 3.2.5, pp.~585--586]{SGA4D} identifies the right
adjoint of $Rh_!$ with $h^*(1)[2]$. Internal Hom adjunction, checked
\'etale locally on the base, consequently gives
\[
 R\mathcal Hom_S(Rh_!G^\vee,\Lambda)
 \simeq Rh_*G(1)[2]
 \simeq i_{0*}Ri_0^!\Lambda(1)[2].
\]
Cancelling the twist and shift proves the first isomorphism in
\eqref{D:AS-duality}; localization proves the second.

At an isolated point $n$ the latter complex is $\Lambda$ in degree
zero, since $D(a)$ is empty in that local scheme. At $m$ the strict
localization is $V$, and its intersection with $D(a)$ is
$\operatorname{Spec}K$. Both $V$ and $K$ have constant-sheaf
cohomology $\Lambda$ in degree zero and zero in higher degrees,
and the restriction map is the identity. Thus the complex has zero
stalk at $m$, and also at $\eta$. These are all points, so it is
concentrated in degree zero. Every geometric specialization map is
an isomorphism: the only nontrivial relation between distinct points
is $\eta\rightsquigarrow m$, where both stalks are zero. Nevertheless
$h_*G$ cannot be locally constant near $m$, because its stalk there
is zero and every neighborhood contains isolated points with stalk
$\Lambda$. By Proposition~\ref{D:boundary-arbitrary}, the boundary
cohomology constructibility condition fails. The same computation,
and the finite geometric boundary, show that each boundary comparison
complex itself vanishes. This proves every assertion.
\end{proof}

'''
s=s.replace('\\begin{proposition}[Known sufficient condition; proved numerical equivalence',insert+'\\begin{proposition}[Known sufficient condition; proved numerical equivalence')
f.write_text(s)
u=p/'unresolved_D.tex'; z=u.read_text(); z=z.split('\\subsection{D.10: the completely arbitrary base}')[0];u.write_text(z)
b=p/'references_D.bib'
b.write_text(b.read_text()+r'''
@book{SGA4D,
 editor={Artin, Michael and Grothendieck, Alexander and Verdier, Jean-Louis},
 title={Th\'eorie des topos et cohomologie \'etale des sch\'emas ({SGA} 4)},
 series={Lecture Notes in Mathematics},volume={269, 270, 305},
 publisher={Springer},year={1972--1973},
 url={https://www.normalesup.org/~forgogozo/SGA4/},
 note={Opened primary reedition: IX, Proposition 2.11, original p.20; XVII, Theorems 5.2.6 and 5.3.6, original pp.357 and 364, and Corollary 5.2.8.1, p.358; XVIII, Theorem 3.2.5, original pp.585--586. These statements explicitly permit arbitrary bases (locally quasi-compact quasi-separated where required).}}
''')
q=p/'code/prepare_checkpoint.py'; c=q.read_text()
c=c.replace("'D:boundary-criterion':('Boundary hypercohomology vanishing exactly characterizes local constancy','Proved under stated hypotheses','Proper base change; Stacks59.75.5-7','31/101','Locally noetherian base; pointwise boundary vanishing equivalent for curves only.'),", "'D:boundary-criterion':('Boundary hypercohomology vanishing exactly characterizes local constancy','Proved under stated hypotheses','Proper base change; Stacks59.75.5-7','31/101','Every quasi-compact open has finitely many irreducible components; pointwise vanishing equivalent for curves only.'),\n'D:boundary-arbitrary':('Exact arbitrary-base criterion: constructible boundary cohomology and vanishing specialization cones','Proved','SGA4 IX2.11; XVII5.3.6; localization; D:boundary-criterion','31/101','No noetherian or irreducible-component finiteness assumption. Boundary constructibility is essential.'),\n'D:boundary-nonconstructible':('Specialization isomorphisms do not suffice over an arbitrary base, even for a curve','Refuted','Explicit eventually-constant-sequence valuation fibre product; SGA4 XVIII3.2.5 arbitrary-base duality','31/101','A1 Artin-Schreier sheaf has nonzero isolated stalks accumulating at a zero stalk; higher direct images vanish.'),")
c=c.replace('events.extend([','events.extend([\n [\'D:alpha-strict-filtering; D:alpha-common-refinement\',\'2026-11-20T02:10Z\',\'GPT-6 Astra; /root; independent delegated audit\',\'targeted proof check\',\'Root independently checked strict parallel equalization and finite C2 product-category counterexample; no gap found. Audit received before stated timestamp.\'],\n [\'D:fixed-vs-valuation\',\'2026-11-20T02:20Z\',\'GPT-6 Astra; /root; independent delegated audit\',\'targeted proof check\',\'Root independently checked e=1, inseparable residue degree2, inertia C2, punctured fundamental group and quotient assertions.\'],\n [\'D:boundary-arbitrary; D:boundary-nonconstructible\',\'2026-11-20T02:21Z\',\'GPT-6 Astra; /root and /root/part_d; independent cross-check\',\'targeted proof check\',\'Root supplied explicit ring and boundary constructibility repair; part D independently checked every local ring, stalk, duality identity, and opened exact arbitrary-base SGA4 IX2.11, XVII5.2.6/5.3.6, XVIII3.2.5.\'],')
q.write_text(c)
(p/'notes.md').write_text((p/'notes.md').read_text()+'''\n\n## Checked update 2026-11-20 02:21 UTC: arbitrary-base D10 closed\nThe earlier remaining-work list is historical. D10 now has an exact criterion over arbitrary S: boundary direct-image cohomology is constructible and every boundary specialization cone is acyclic. SGA4 IX2.11 and XVII5.3.6 apply to arbitrary schemes, not only noetherian ones. Root's R=V x_k A example is checked using XVIII3.2.5, which explicitly assumes only qcqs base. Exact proofs are in paper_D.tex, labels D:boundary-arbitrary and D:boundary-nonconstructible. Only the stated D1/D2ii fixed-boundary finite-generation gate remains in unresolved_D.tex.\n''')
print('D10 checked proof integrated')
