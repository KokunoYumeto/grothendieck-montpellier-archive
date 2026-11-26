# Version 2 edits of the note hexagon:2611.00940 (24 Nov 2026).
# Reads h17_note_v1_posted.tex (the posted source), writes h17_note_v2.tex.
# Every replacement must match exactly once; otherwise nothing is written.
import io, sys

SRC = "h17_note_v1_posted.tex"
DST = "h17_note_v2.tex"

R = []

# ---------------------------------------------------------------- header, date
R.append((r"""% Hexagon note H17, 23 Nov 2026. CC0 1.0.
% Mathematics: GPT-6 Astra (ChatGPT Pro mode), November 2026.
% Text (version 1): Claude Fable 5.2 at effort max, as editor; several proofs rewritten (see "Provenance and checks").""",
r"""% hexagon:2611.00940, version 2, 25 Nov 2026 (version 1: 23 Nov 2026). CC0 1.0.
% Mathematics of Sections 4 to 9: GPT-6 Astra (ChatGPT Pro mode), November 2026.
% Text: Claude Fable 5.2 at effort max, as editor; several proofs rewritten; Remark 19 and Section 10 are the
% editor's (see "Provenance and checks")."""))

R.append((r"""\date{23 November 2026 \quad CC0 1.0}""",
r"""\date{Version 2, 25 November 2026 \quad CC0 1.0}"""))

# ---------------------------------------------------------------- title (names both relations)
R.append((r"""\title{Relation (IV) of Nakamura and Schneps holds on the profinite Grothendieck--Teichm\"uller group,""",
r"""\title{Relations (III$'$) and (IV) of Nakamura and Schneps hold on the profinite Grothendieck--Teichm\"uller group,"""))

# ---------------------------------------------------------------- abstract
R.append((r"""Nakamura and Schneps (2000) defined a subgroup of the profinite Grothendieck--Teichm\"uller group $\GT$ by two""",
r"""Nakamura and Schneps (2000) defined a subgroup $\mathrm{I}\Gamma$ of the profinite Grothendieck--Teichm\"uller group $\GT$ by two"""))

R.append((r"""$\GT$. The proofs use the theorem of Boggi and Zalesskii on finite $p$-subgroups of profinite completions, the""",
r"""$\GT$. Version 2 adds three things. First, $(\mathrm{III}')$ also holds for every element of $\GT$; so
$\mathrm{I}\Gamma=\GT$, and the representations of $\mathrm{I}\Gamma$ in the automorphism groups of all profinite
mapping class groups, constructed by Nakamura and Schneps, are representations of $\GT$. Second, the questions that
Lochak (2025) asks about his groups of compatible pairs have a positive answer: these groups are $\GT$, and by his
theorem $\GT$ is then the group of inertia-preserving outer automorphisms of the procongruence mapping class group of
every surface of generic type and positive genus. Third, a correction: version 1 called the strictness of the
inclusion of $\GT$ in the larger group known, and we have found no published proof of it.
The proofs use the theorem of Boggi and Zalesskii on finite $p$-subgroups of profinite completions, the"""))

R.append((r"""of genus-zero configuration groups. Relation $(\mathrm{III}')$ is not touched. The mathematics was produced by
GPT-6 Astra (ChatGPT Pro mode); it was checked by Claude Fable 5.2 at effort max, which wrote this text and rewrote
several proofs, and by Claude Opus 5.5 at effort max as second reader. No human has checked it.""",
r"""of genus-zero configuration groups. The mathematics of version 1 was produced by
GPT-6 Astra (ChatGPT Pro mode); it was checked by Claude Fable 5.2 at effort max, which wrote this text and rewrote
several proofs, and by Claude Opus 5.5 at effort max as second reader. The additions of version 2 are by Claude
Fable 5.2 at effort max, one of them with Claude Opus 5.5 at effort max; the new theorem and its two corollaries
were checked by a second reader, Claude Opus 5.5 at effort max, in a separate run. No human has checked any of
it."""))

# ---------------------------------------------------------------- Section 1
R.append((r"""So the subgroup $\mathrm{I}\Gamma$ of Nakamura and Schneps is defined inside $\GT$ by $(\mathrm{III}')$ alone. For""",
r"""So the subgroup $\mathrm{I}\Gamma$ of Nakamura and Schneps is defined inside $\GT$ by $(\mathrm{III}')$ alone;
Theorem~\ref{thm:IIIp}, added in version 2, shows that $(\mathrm{III}')$ holds on $\GT$ as well. For"""))

R.append((r"""\subsection*{What it means, and what is not proved here}""",
r"""\subsection*{Added in version 2: relation $(\mathrm{III}')$ and the questions of Lochak}
Three statements are added. They are stated in full and proved in Section~\ref{sec:IIIp}, and their numbers follow
those of version 1, which are unchanged.

\emph{Relation $(\mathrm{III}')$} (Theorem~\ref{thm:IIIp}). For every $F=(\lambda,f)\in\GT$,
\[
 f(\tau_1\tau_3,\tau_2^2)=g(x_{45},x_{51})\,f(x_{12},x_{23})\,f(x_{34},x_{45})\qquad\text{in }\Gh_{0,[5]},
\]
where the $\tau_i$ are the standard generators, the $x_{ij}$ are the standard twists and $g\in\Fh_2$ is the element
with $f(x,y)=g(y,x)^{-1}g(x,y)$. Nakamura and Schneps prove this for Galois elements \cite[Theorem 1.1]{NS}. The
proof for all of $\GT$ takes one page: the pentagon says that the right side commutes with an involution of
$\Gh_{0,[5]}$; by the theorem of Boggi and Zalesskii it then lies in the completion of the discrete centralizer; and
an element of that group is determined by its image when the fifth point is forgotten.

\emph{The group of Nakamura and Schneps} (Corollary~\ref{cor:IG}). $\mathrm{I}\Gamma=\GT$. So the representations
of $\mathrm{I}\Gamma$ in $\Aut\Gh(\Sigma)$, which Nakamura and Schneps construct for every surface $\Sigma$ with a
quilt decomposition and prove compatible with the inclusions of subsurfaces \cite[Theorems 1.3 and 1.4]{NS}, are
representations of $\GT$.

\emph{The questions of Lochak} (Corollary~\ref{cor:Lochak}). Lochak calls two elements $F_0,F_1$ of $\GT$ a
compatible pair if the outer actions they define on a piece of type $(0,5)$ and on a piece of type $(1,2)$ of a
surface of type $(1,3)$ agree where the two pieces meet; this is one equation in $\Bh_3$
\cite[Definition 5.4]{Lo}. The compatible pairs form a subgroup of $\GT$ \cite[Proposition--Definition 5.6]{Lo},
and those with $F_0=F_1$ are the elements that satisfy (IV) \cite[pp.~58 and 60]{Lo}. He proves that the group of
compatible pairs is the group of inertia-preserving outer automorphisms of the procongruence mapping class group of
every surface of generic type \cite[Theorem 5.10]{Lo}, and asks whether every compatible pair has $F_0=F_1$, whether
the group of compatible pairs is $\GT$, and whether (IV) holds on all of $\GT$ \cite[p.~62]{Lo}. By
Theorem~\ref{thm:IV} the answer to the three questions is yes, and with his theorem
$\Out^*(\check\Gamma(S))\cong\GT$ for every surface $S$ of type $(g,n)$ with $g\ge1$, $3g-3+n>2$ and
$(g,n)\ne(2,0)$.

\subsection*{What it means, and what is not proved here}"""))

R.append((r"""them to agree. The inclusion $\GT\subsetneq\GTz$ itself is known; what is new is an explicit level-twelve character
that separates them, with this meaning.""",
r"""them to agree. The inclusion $\GT\subset\GTz$ is clear from the definitions \cite[p.~2]{DG}. Version 1 of this
note said that its strictness is known; we have found no published proof that the inclusion is strict. The research
runs behind this note contain several arguments for strictness, and the nonvanishing just quoted would be one; none
of them has been refereed. Granting them, what the character adds is an explicit level-twelve invariant that
separates the two groups, with this meaning."""))

R.append((r"""Hoshi, Minamide and Mochizuki that $\Out(\Gh_{0,m})=\GT\times\mathfrak S_m$ for $m\ge5$
\cite[Corollary C]{HMM}.""",
r"""Hoshi, Minamide and Mochizuki that $\Out(\Gh_{0,m})=\GT\times\mathfrak S_m$ for $m\ge5$
\cite[Corollary C]{HMM}. For the additions of version 2: relation $(\mathrm{III}')$, the group $\mathrm{I}\Gamma$ and
its representations are due to Nakamura and Schneps \cite{NS}; compatible pairs, the groups they form and the
theorem identifying them with automorphism groups are due to Lochak \cite{Lo}, who asked the questions answered in
Corollary~\ref{cor:Lochak}. What is added is Theorem~\ref{thm:IIIp} and the deduction of the two corollaries."""))

R.append((r"""operad of mapping class groupoids on which the subgroup of Nakamura and Schneps acts after completion; by
Theorem~\ref{thm:IV} that subgroup is cut out by $(\mathrm{III}')$ alone. We know of no earlier statement of
Theorems \ref{thm:IV}--\ref{thm:delta}; a search of arXiv and of Hexagon on 23 November 2026 found none.""",
r"""operad of mapping class groupoids on which the subgroup of Nakamura and Schneps acts after completion; by
Corollary~\ref{cor:IG} that subgroup is $\GT$. Lochak \cite{Lo} determines the automorphisms of procongruence
curve complexes and asks whether (IV) holds on $\GT$; version 1 of this note did not cite his paper. Furusho's
survey of 2002 records that it was not known whether $(\mathrm{III}')$, (IV) and other relations satisfied by Galois
elements follow from (I), (II) and (III) \cite[p.~191]{Fu}. Boggi's preprint \cite{Bo} states that $\GT$ embeds in outer automorphism groups
of profinite completions of pure mapping class groups; we come back to it in Remark~\ref{rem:context2}. We know of no
earlier statement of Theorems \ref{thm:IV}--\ref{thm:delta}; a search of arXiv and of Hexagon on 23 November 2026
found none. For Theorem~\ref{thm:IIIp} a search of 24 November found none either, with one sentence of \cite{Lo} to
be mentioned (Remark~\ref{rem:context2})."""))

R.append((r"""We do not decide whether $(\mathrm{III}')$ holds on $\GT$, whether $\Lambda_0\cdot\GQ$ acts on the tower as one
group (the question of \cite[\S8]{LNS}), or whether $\GQ=\GT$.""",
r"""We do not decide whether $\GQ=\GT$. We do not compare the actions now available for every element of $\GT$ on
mapping class groups of positive genus: that of \cite{NS}, that of \cite{LNS} on the groups with at most one marked
point, that of \cite{Lo} on procongruence completions, and the one obtained from \cite{HLS} by
Theorem~\ref{thm:Lambda}. Theorem 5.10 of \cite{Lo} and Theorems 1.3 and 1.4 of \cite{NS} are used as published; we
have not checked their proofs."""))

# ---------------------------------------------------------------- Section 2
R.append((r"""action of \cite{HLS}; the pentagon is used through \cite{HLS} and \cite{HMM}.""",
r"""action of \cite{HLS}; the pentagon is used through \cite{HLS} and \cite{HMM}.

\emph{Relation $(\mathrm{III}')$ and the questions of Lochak (version 2).} Relation $(\mathrm{III}')$ compares the
value of $f$ on a group of mapping classes that commute with an involution $\varepsilon$ of the sphere with five
marked points, the left side, with a product of values of $f$ on twists, the right side. Applying $\varepsilon$ to
the right side and using the pentagon gives the same element back; this is how Nakamura and Schneps deduce the
pentagon from $(\mathrm{III}')$, read backwards. So the right side commutes with $\varepsilon$, and by the theorem of
Boggi and Zalesskii it lies in the completion of the discrete centralizer, as the left side does. On the pure part
of that centralizer, forgetting the fifth point, which $\varepsilon$ fixes, is injective, and it sends both sides to
$f(u^2,v^2)$ (Section~\ref{sec:IIIp}). The action of $F$ on $\Gh_{0,[5]}$ is not used. Lochak's questions are then
a matter of rewriting (IV): his compatibility condition for the pair $(F,F)$ is relation (IV), because
$(uv^2)^2=(uv)^3$ is central in $B_3$."""))

# ---------------------------------------------------------------- Remark 19 and Section 10
R.append((r"""side acts by $(-1)^{a_3}$ and the right side by $(-1)^k=(-1)^{a_2}$. So $a_2(F)=a_3(F)$. \qed

\section{What remains open}""",
r"""side acts by $(-1)^{a_3}$ and the right side by $(-1)^k=(-1)^{a_2}$. So $a_2(F)=a_3(F)$. \qed

\begin{remark}\label{rem:a3}
\emph{Where the two bits are read} (added in version 2). Let $F\in H_0$. By Lemma~\ref{lem:unit} the bit $a_2(F)$
is determined by the unit $\nu_F$, that is, by the action of $F$ on
$\widehat{\mathcal L}\rtimes\mu_6=\Bh/\overline{B''}$, the profinite triangle group $(2,3,6)$, which is metabelian.
The bit $a_3(F)$ is not read there, in the following sense.
\begin{itemize}
\item[(a)] $q_{12}(A_F)=(5I)^{a_3(F)}$, where $5I$ is $I$ modulo $4$ and $-I$ modulo $3$. Indeed
$\pi_6(r)=(\zeta,\omega)$, and the equation $A\,\pi_6(r)\,A^{-1}=(\nu_F\zeta,\omega)$ has in
$(1-\omega)\widehat{\mathcal L}\rtimes\langle\omega\rangle$ the one solution $A=((\nu_F-1)\zeta/(1-\omega),1)$,
which is therefore $\pi_6(A_F)$. As $\nu_F\equiv1\bmod2$, its image under the map $\kappa$ of the proof of
Lemma~\ref{lem:unit} is trivial, so $q_{12}(A_F)$ is $\pm I$ modulo $3$; and it is $I$ modulo $4$ by
Lemma~\ref{lem:E}(b).
\item[(b)] The second derived group of $E_{12}=V_4\times\SL_2(\F_3)$ is $\{I,5I\}$, because the derived group of
$\SL_2(\F_3)$ is the quaternion group, whose derived group is $\{\pm I\}$. So $a_3(F)=1$ exactly when $q_{12}(A_F)$
is the nontrivial element of the second derived group of $E_{12}$.
\item[(c)] In $\PSL_2(\Z/12)$ the normal subgroup generated by $q(u^6)$ has order $8$ and contains the class of
$5I$, and the quotient is $\PSL_2(\Z/6)$. Indeed $U^6$ is $U^2$ modulo $4$ and $I$ modulo $3$, and the conjugates of
$U^2$ generate the kernel of $\SL_2(\Z/4)\to\SL_2(\Z/2)$, which has order $8$ and contains $-I$. Now $\pi_6$
identifies the triangle group $\langle s,r\mid s^2,r^3,(sr)^6\rangle$ with $\mathcal L\rtimes\mu_6$, and $sr=u^{-1}$;
so $\overline{B''}$ is the closed normal subgroup of $\Bh$ generated by $u^6$, and every quotient of $\Bh$ through
which both $q$ and $\pi_6$ factor is a quotient of $\PSL_2(\Z/6)$, where the class of $5I$ is trivial.
\end{itemize}
So Theorem~\ref{thm:delta} compares a bit read in the metabelian quotient $\Bh/\overline{B''}$ with a bit read, by
(a) and (b), in a second derived group, at a level that by (c) the group $(2,3,6)$ does not reach; that level is
reached by the triangle group $(2,3,12)$, the quotient of $\Bh$ by the closed normal subgroup generated by $u^{12}$,
through which $q$ factors. This is why the proof of Theorem~\ref{thm:delta} does not stay in the group $(2,3,6)$ and
passes through genus one. Statements (a) and (b) are derived here from Lemmas \ref{lem:E} and \ref{lem:unit}; the
orders in (b) and (c) were also computed by machine.
\end{remark}

\section{Relation \texorpdfstring{$(\mathrm{III}')$}{(III')} and the questions of Lochak}\label{sec:IIIp}

This section is new in version 2.

\subsection*{Relation $(\mathrm{III}')$}
Place the five marked points on a circle, in their cyclic order. Let $\tau_1,\dots,\tau_4$ be the standard
generators of $\Gamma_{0,[5]}$, where $\tau_i$ exchanges the points $i$ and $i+1$ by a half twist along the arc of the
circle between them, and for $i\in\Z/5$ let $x_{i,i+1}\in\Gamma_{0,5}$ be the twist along the boundary of a
neighbourhood of the arc from $i$ to $i+1$; so $x_{i,i+1}=\tau_i^2$ for $i\le4$. In these terms the pentagon relation
(III) is
\begin{equation}\label{eq:pentagon}
 f(x_{34},x_{45})\,f(x_{51},x_{12})\,f(x_{23},x_{34})\,f(x_{45},x_{51})\,f(x_{12},x_{23})=1
 \qquad\text{in }\Gh_{0,5}
\end{equation}
\cite[\S1]{NS}. Let $M\subset\Gamma_{0,[5]}$ be the stabilizer of the fifth point. It is generated by
$\tau_1,\tau_2,\tau_3$ and is the quotient of $B_4$ by its centre, as in (B2), and in $M$
\[
 x_{45}=(\tau_1\tau_2)^3,\qquad x_{51}=(\tau_2\tau_3)^3,
\]
the twists along the curves surrounding the points $1,2,3$ and $2,3,4$ \cite[\S1]{NS}. For $F=(\lambda,f)\in\GTz$
let $g=g_F=\beta_F^{-1}\in\Fh_2$. By Lemma~\ref{lem:rho}(a), $f(x,y)=g(y,x)^{-1}g(x,y)$, and $g$ is the only element
of $\Fh_2$ with this property: if $g'$ is another one, then $c=g'g^{-1}$ satisfies $c(y,x)=c(x,y)$, so it is fixed
by $\vartheta=\Ad(s)$, and $C_{\Bh}(s)\cap\Fh=1$.

\begin{theorem}\label{thm:IIIp}
For every $F=(\lambda,f)\in\GT$,
\[
 f(\tau_1\tau_3,\tau_2^2)=g(x_{45},x_{51})\,f(x_{12},x_{23})\,f(x_{34},x_{45})\qquad\text{in }\Gh_{0,[5]}.
 \tag{III$'$}
\]
\end{theorem}

This is the relation of \cite[Theorem 1.1]{NS}, in their notation; they prove it for Galois elements. Furusho's
survey writes the same relation in $\Bh_5$ \cite[p.~191]{Fu}; we prove it in $\Gh_{0,[5]}$, where \cite{NS} state it
and define $\mathrm{I}\Gamma$.

\begin{proof}
Let $\varepsilon\in M$ be the image of $\Delta=\sigma_1\sigma_2\sigma_3\sigma_1\sigma_2\sigma_1\in B_4$. Since
$\Delta\sigma_i\Delta^{-1}=\sigma_{4-i}$ and $\Delta^2$ generates the centre of $B_4$, the element $\varepsilon$
has order two, and $\Ad(\varepsilon)$ exchanges $\tau_1$ and $\tau_3$ and fixes $\tau_2$. So it exchanges
$x_{12}$ and $x_{34}$, fixes $x_{23}$, and exchanges $x_{45}=(\tau_1\tau_2)^3$ and
$x_{51}=(\tau_2\tau_3)^3=(\tau_3\tau_2)^3$. Put the first four points at $-a,-b,b,a$ on the real line, with
$0<b<a$, and the fifth at $\infty$; then $\varepsilon$ is the class of the rotation $\iota:t\mapsto-t$.

\emph{Step 1: the right side commutes with $\varepsilon$.} Let $R$ be the right side of $(\mathrm{III}')$. Then
$\varepsilon R\varepsilon^{-1}=g(x_{51},x_{45})\,f(x_{34},x_{23})\,f(x_{12},x_{51})$. By relation (I) and the
property of $g$,
\[
 (\varepsilon R\varepsilon^{-1})^{-1}R
 =f(x_{51},x_{12})\,f(x_{23},x_{34})\,f(x_{45},x_{51})\,f(x_{12},x_{23})\,f(x_{34},x_{45}),
\]
which is conjugate to the left side of \eqref{eq:pentagon}, hence equal to $1$. This is the computation by which
\cite[\S1]{NS} deduce (III) from $(\mathrm{III}')$, read backwards.

\emph{Step 2: the centralizer.} Let $N$ be the centralizer of $\varepsilon$ in $\Gamma_{0,[5]}$ and
$N_1=N\cap\Gamma_{0,5}$. We use the theorem of Boggi and Zalesskii \cite[Theorem A\,(iii)]{BZ}: let $p$ be a prime
and $G$ a group of finite virtual $p$-cohomological type, that is, of finite virtual $p$-cohomological dimension
and with finite cohomology in every finite $\F_p[G]$-module; if the map from $G$ to its profinite completion
$\widehat G$ induces isomorphisms on the cohomology in every discrete $\F_p[[\widehat G]]$-module in all large
degrees, then for every finite $p$-subgroup $H$ of $G$ the centralizer of $H$ in $\widehat G$ is the closure of the
centralizer of $H$ in $G$. Take $p=2$, $G=\Gamma_{0,[5]}$ and $H=\langle\varepsilon\rangle$, of order two. The
hypotheses hold: $G$ is good, and its subgroup $\Gamma_{0,5}$ of finite index is torsion-free and an iterated
extension of free groups of finite rank, the kernel of forgetting a point being free of rank three and
$\Gamma_{0,4}$ free of rank two. (This is the case $\Gamma=\Gamma_{0,[5]}$, $P=\Gamma_{0,5}$ of
Lemma~\ref{lem:BZ}(b); here $H\cap P=1$ because $\varepsilon$ is not pure.) So the centralizer of $\varepsilon$ in
$\Gh_{0,[5]}$ is $\overline N$. Its intersection with the open subgroup $\Gh_{0,5}$ is $\overline{N_1}$. So
$R\in\overline{N_1}$. The left side
$L=f(\tau_1\tau_3,\tau_2^2)$ of $(\mathrm{III}')$ lies in $\overline N$, because $\tau_1\tau_3$ and $\tau_2$ commute
with $\varepsilon$. It is pure, because $f$ lies in the closed commutator subgroup of $\Fh_2$ and the permutations
of $\tau_1\tau_3$ and $\tau_2^2$ commute. So $L\in\overline{N_1}$ as well.

\emph{Step 3: forgetting the fifth point is injective on $\overline{N_1}$.} Let $p:M\to B$ be the map that forgets
the fifth point, followed by the quotient of $\Gamma_{0,[4]}$ by its normal four-group $V$; as in
Section~\ref{sec:IV}, $p(\tau_1)=p(\tau_3)=u$ and $p(\tau_2)=v$. Let $\gamma\in N_1$ with $p(\gamma)=1$. The image of
$\gamma$ in $\Gamma_{0,[4]}$ is pure and lies in $V$, so it is trivial. Hence $\gamma$ lies in the kernel of the
forgetting map, which consists of the classes $\mathrm{Push}(c)$ that push the fifth point along a loop
$c\in\Pi=\pi_1(\mathbf P^1\setminus\{\pm a,\pm b\},\infty)$, and $c\mapsto\mathrm{Push}(c)$ is injective \cite{Bi}.
Write $\gamma=\mathrm{Push}(c)$. Then $\gamma=\varepsilon\gamma\varepsilon^{-1}=\mathrm{Push}(\iota_*c)$, so
$\iota_*c=c$. The group $\Pi\rtimes\langle\iota_*\rangle$ is the orbifold fundamental group of the quotient of
$\mathbf P^1\setminus\{\pm a,\pm b\}$ by $\iota$, a sphere with two punctures and two cone points of order two; it
is a free product $C_2*C_2*\Z$. By the subgroup theorem of Kurosh \cite{Ku}, a subgroup of a free product is a free
product of a free group and of conjugates of subgroups of the factors. The centralizer of $\iota_*$ has $\iota_*$
in its centre, and a free product of two nontrivial groups has trivial centre; so the centralizer is a single one of
these groups, and as it contains an element of order two it is a conjugate of a factor of order two. So this
centralizer is $\{1,\iota_*\}$, which meets $\Pi$ trivially. Hence $c=1$ and $\gamma=1$: the map $p$ is injective
on $N_1$. Its image contains $p(\tau_1^2\tau_3^2)=x^2$,
$p(\tau_2^2)=y$ and $p(\tau_1\tau_3\tau_2^2\tau_3^{-1}\tau_1^{-1})=xyx^{-1}$, which generate a subgroup of index
two of $F$; so $p(N_1)$ has finite index in $B$. Consequently every subgroup $K$ of finite index of $N_1$ is the
preimage in $N_1$ of the subgroup $p(K)$ of finite index of $B$; as $p$ extends to a continuous map of the
completions, $K$ is open in the topology induced by $\Gh_{0,[5]}$. Hence $\overline{N_1}$ is the profinite completion of $N_1$, the closure of $p(N_1)$ in $\Bh$ is its
profinite completion, and the map $\overline{N_1}\to\Bh$ induced by $p$ is the completion of an isomorphism: it is
injective.

\emph{Step 4: comparison.} In $B$ we have $p(x_{45})=(uv)^3=1$ and $p(x_{51})=(vu)^3=1$. So
$p(R)=g(1,1)\,f(u^2,v^2)\,f(u^2,1)=f(u^2,v^2)$, and $p(L)=f(u^2,v^2)$. By Step 3, $L=R$.
\end{proof}

\begin{corollary}\label{cor:IG}
The subgroup $\mathrm{I}\Gamma$ of Nakamura and Schneps \cite[Definition 1.1]{NS} is all of $\GT$. Consequently
their theorems on $\mathrm{I}\Gamma$ hold for $\GT$: for every surface $\Sigma$ with a quilt decomposition $Q/P$
there is a representation $\GT\to\Aut\Gh(\Sigma)$, whose class in $\Out\Gh(\Sigma)$ does not depend on the quilt
\cite[Theorem 1.3 and the text after it]{NS}; and these representations are compatible with the homomorphisms
$\Gh(\Sigma')\to\Gh(\Sigma)$ for the connected subsurfaces $\Sigma'$ made of pairs of pants of $P$
\cite[Theorem 1.4]{NS}.
\end{corollary}

\begin{proof}
$\mathrm{I}\Gamma$ is the set of the elements of $\GT$ that satisfy $(\mathrm{III}')$ and (IV). Apply Theorems
\ref{thm:IIIp} and \ref{thm:IV}.
\end{proof}

\subsection*{The questions of Lochak}
Lochak \cite{Lo} writes $\tau_1,\tau_2$ for the generators $u,v$ of $B_3$. He calls two elements
$F_0=(\lambda_0,f_0)$ and $F_1=(\lambda_1,f_1)$ of $\GT$ a \emph{compatible pair} if $\lambda_0=\lambda_1$ and there
are $a,b,c\in\Zh$ with
\begin{equation}\label{eq:pair}
 f_1(u^2,v^2)=v^{2a}\,f_0(u,v^4)\,u^{2b}\,(uv^2)^{2c}\qquad\text{in }\Bh_3
\end{equation}
\cite[Definition 5.4]{Lo}. The compatible pairs form a group, which the map $(F_0,F_1)\mapsto F_0$ identifies with
a subgroup of $\GT$ \cite[Proposition--Definition 5.6]{Lo}. He writes $\mathrm{I}\Gamma$ for it; we write
$\mathrm{I}\Gamma_{\mathrm L}$, to keep it apart from the group of \cite{NS}. Its subgroup
$\mathrm{I}\Gamma_{\mathrm L,s}$ of the pairs with $F_0=F_1$ consists of the $F\in\GT$ that satisfy
\begin{equation}\label{eq:IVL}
 f(u^2,v^2)=v^{-8\rho}\,f(u,v^4)\,u^{-4\rho}\,(uv^2)^{4\rho},\qquad\rho=\rho_2(F),
\end{equation}
which is the form in which he writes relation (IV) \cite[pp.~58 and 60]{Lo}. For a surface $S$ of type $(g,n)$ let
$\Gamma(S)=\Gamma_{g,[n]}$, let $\check\Gamma(S)$ be its procongruence completion and $\check C(S)$ the
procongruence completion of the complex of curves of $S$, and let $\Aut^*$ and $\Out^*$ refer to the automorphisms
that preserve inertia, that is, the set of conjugacy classes of the procyclic subgroups generated by twists
\cite[pp.~2 and 6]{Lo}. The surface $S$ is \emph{of generic type} if $g\ge1$, $3g-3+n>2$ and $(g,n)\ne(2,0)$.
Lochak proves that for $S$ of generic type
\begin{equation}\label{eq:Lochak510}
 \Out^*(\check\Gamma(S))=\Out(\check C(S))=\mathrm{I}\Gamma_{\mathrm L}
\end{equation}
\cite[Theorem 5.10\,ii)]{Lo}. In his closing remarks he asks whether
$\mathrm{I}\Gamma_{\mathrm L,s}=\mathrm{I}\Gamma_{\mathrm L}$; whether $\mathrm{I}\Gamma_{\mathrm L}=\GT$, in which
case everything would be decided in genus zero; and whether $\mathrm{I}\Gamma_{\mathrm L,s}=\GT$, ``that is, showing
that relation $(IV)$ is actually redundant'', so that in every genus only pentagons would be needed
\cite[p.~62]{Lo}.

\begin{corollary}\label{cor:Lochak}
\textup{(a)} $\mathrm{I}\Gamma_{\mathrm L,s}=\mathrm{I}\Gamma_{\mathrm L}=\GT$: for every $F\in\GT$ the pair $(F,F)$
is compatible, and every compatible pair is of this form.

\textup{(b)} For every surface $S$ of generic type,
$\Out^*(\check\Gamma(S))=\Out(\check C(S))\cong\GT$, and every inertia-preserving automorphism of
$\check\Gamma(S)$ is of strict lego type in the sense of \cite[Definition 5.8]{Lo}.
\end{corollary}

\begin{proof}
(a) In $B_3$ one has $(uv^2)^2=(uv)^3$ (Section~\ref{sec:IV}), and this element is central. So relation (IV) of
Theorem~\ref{thm:IV} can be written $f(u^2,v^2)=v^{-8\rho}f(u,v^4)u^{-4\rho}(uv)^{6\rho}$ with
$(uv)^{6\rho}=(uv^2)^{4\rho}$. This is \eqref{eq:IVL}, and it is \eqref{eq:pair} for $f_0=f_1=f$ with $a=-4\rho$,
$b=-2\rho$, $c=2\rho$. So $(F,F)$ is a compatible pair for every $F\in\GT$. Now let $(F_0,F_1)$ be any compatible
pair. Comparing \eqref{eq:pair} for $(F_0,F_1)$ and for $(F_0,F_0)$, and using that $(uv^2)^2$ is central, we get
\[
 f_1(x,y)=y^{\alpha}\,f_0(x,y)\,x^{\beta}\,(uv)^{3\gamma}\qquad\text{in }\Bh_3,
\]
with $x=u^2$, $y=v^2$ and $\alpha,\beta,\gamma\in\Zh$. Modulo the centre this is an equation in $\Fh$, where $f_0$
and $f_1$ lie in the closed commutator subgroup; in $\Fh^{\ab}$ it gives $\alpha=\beta=0$, and then $f_1=f_0$.
(That $F_1$ is determined by $F_0$ is also in the proof of \cite[Proposition--Definition 5.6]{Lo}, through
\cite[Proposition 5.5]{Lo}.)

(b) This is \eqref{eq:Lochak510} with (a); by \cite[Definition 5.8]{Lo} an automorphism is of strict lego type
when its pair has $F_0=F_1$.
\end{proof}

For $g\le2$ the procongruence completion is the profinite completion \cite[p.~60]{Lo}; so for the generic types of
genus one and two, Corollary~\ref{cor:Lochak}(b) is a statement about $\Gh_{g,[n]}$.

\begin{remark}\label{rem:context2}
\emph{What is used, and neighbouring statements.}
(a) Corollary~\ref{cor:Lochak}(b) uses Theorem 5.10 of \cite{Lo} as published. We have read its statement and the
definitions and propositions cited above, and we have not checked its proof, which rests on work of Boggi and Funar
on procongruence curve complexes. Corollary~\ref{cor:IG} uses Theorems 1.3 and 1.4 of \cite{NS} in the same way.
(b) Boggi's preprint \cite{Bo} states a result of the same kind as Corollary~\ref{cor:Lochak}(b) for pure mapping
class groups: for $\chi(S)<g-2$ and $(g,n)\ne(1,2)$, the group of the outer automorphisms of the procongruence
completion of the pure mapping class group that preserve the conjugacy class of the procyclic subgroup generated by a
nonseparating twist is naturally isomorphic to $\mathfrak S_n\times\GT$; and for $\chi(S)<g-2$ the group $\GT$
embeds in the corresponding group for the profinite completion \cite[abstract of version 6]{Bo}. We have read only
that abstract, and we have not compared the statements or the actions.
(c) Lochak writes that $\mathrm{I}\Gamma_{\mathrm L,s}$ ``is contained in the group'' that \cite{NS} denote by
$\mathrm{I}\Gamma$ \cite[p.~61]{Lo}. The inclusion that follows from the definitions is the opposite one, because the
group of \cite{NS} is defined by (IV) and $(\mathrm{III}')$ together. The inclusion as he states it says that (IV)
implies $(\mathrm{III}')$ on $\GT$; his paper does not mention $(\mathrm{III}')$ and gives no argument for it. By
Theorem~\ref{thm:IIIp} it holds.
(d) Lochak, Nakamura and Schneps name as a subject of future work the question whether the Lego action of
$\mathrm{I}\Gamma$ extends to the full group $\GT$, acting on the groups with one marked point as in their theorem
\cite[\S8]{LNS}. By Corollary~\ref{cor:IG} the group $\mathrm{I}\Gamma$ of that question is $\GT$. We have not
compared the action of \cite{NS} with theirs.
\end{remark}

\section{What remains open}"""))

# ---------------------------------------------------------------- What remains open
R.append((r"""\begin{enumerate}
\item Whether $(\mathrm{III}')$ holds on $\GT$. With Theorem~\ref{thm:IV} this is the question whether
$\mathrm{I}\Gamma=\GT$. The method of Section~\ref{sec:IV} applies to any locus of curves with automorphisms seen
through two forgetting maps; for $(\mathrm{III}')$ the natural loci are those of order two and five in the moduli
of five points, and we have not found the two maps.
\item Whether the action of $\Lambda_0$ and the Galois action fit into one action of $\GT$ on the tower with
marked points \cite[\S8]{LNS}. The obstruction is that the decomposition $F=F_*\sigma$ is not unique and that the
Galois action is not given by the formulas of \cite{HLS} when $\rho_2\ne0$.
\item The statements quoted in Section 1 about the character on all of $\GTz$: its extension, its vanishing on
$\GQ$ and its nonvanishing. They need their own check.
\end{enumerate}""",
r"""Version 1 listed first the question whether $(\mathrm{III}')$ holds on $\GT$; Theorem~\ref{thm:IIIp} answers it.
It listed second the question whether the action of $\Lambda_0$ and the Galois action fit into one action of $\GT$
on the tower with marked points; by Corollary~\ref{cor:IG} the action of Nakamura and Schneps is such an action,
subject to the comparison in item 1.
\begin{enumerate}
\item The comparison of the actions. For a normalized element the formulas of \cite{HLS} and the representations
of \cite{NS} should agree, since for $\lambda=1$ and $\rho_2=0$ the relation $(\mathrm{R}')$ of \cite[\S1]{NS} is
(R); for the groups with at most one marked point the action of \cite{LNS} should agree with that of \cite{NS}; and
on procongruence completions both should induce the outer action of \cite{Lo}. We have checked none of these.
\item Whether $\GQ=\GT$. By Corollary~\ref{cor:Lochak}(b) this is now the question whether every
inertia-preserving outer automorphism of the procongruence mapping class group of a surface of generic type is
Galois.
\item The statements quoted in Section 1 about the character on all of $\GTz$: its extension, its vanishing on
$\GQ$ and its nonvanishing, and with them the strictness of the inclusion $\GT\subset\GTz$. They need their own
check.
\item A check by a human reader. Theorem~\ref{thm:IIIp} and Corollaries \ref{cor:IG} and \ref{cor:Lochak} have been
checked by a second reader, Claude Opus 5.5 at effort max, and Remark~\ref{rem:a3} by its author only.
\end{enumerate}"""))

# ---------------------------------------------------------------- Provenance
R.append((r"""The mathematics is the work of GPT-6 Astra (ChatGPT Pro mode), in research runs of November 2026 on notes of
Grothendieck's \emph{La longue marche \`a travers la th\'eorie de Galois}. The runs contain two proofs of
Theorem~\ref{thm:delta}; this note follows the one through $\Lambda$.""",
r"""The mathematics of Sections 4 to 9 is the work of GPT-6 Astra (ChatGPT Pro mode), in research runs of November
2026 on notes of Grothendieck's \emph{La longue marche \`a travers la th\'eorie de Galois}. The runs contain two
proofs of Theorem~\ref{thm:delta}; this note follows the one through $\Lambda$. They also contain two proofs of
Theorem~\ref{thm:IV}. The earlier one, of 16 November 2026, is in Lochak's formulation: it proves, by the method of
Section~\ref{sec:IV}, that every element of $\GT$ forms a compatible pair with itself in the sense of
\cite[Definition 5.4]{Lo} (statements E.43 and E.44 of that run's text, in the records). Version 1 did not say
so."""))

R.append((r"""The records of the checks are at the permanent page of this work, WB-0007:""",
r"""\paragraph{Version 2 (25 November 2026).}
The statements and proofs of version 1 are unchanged. The changes are these.
\begin{itemize}
\item[\textup{(i)}] A correction in Section 1: version 1 said that the strictness of the inclusion
$\GT\subset\GTz$ is known. No published proof was found, and the sentence now says so.
\item[\textup{(ii)}] The paper of Lochak \cite{Lo}, which asks the question that Theorem~\ref{thm:IV} answers, is
cited, and the earlier proof of Theorem~\ref{thm:IV} in his formulation is recorded above.
\item[\textup{(iii)}] Relation $(\mathrm{III}')$, which version 1 listed as open, is proved
(Theorem~\ref{thm:IIIp}), with Corollaries \ref{cor:IG} and \ref{cor:Lochak} and Remark~\ref{rem:context2}.
\item[\textup{(iv)}] Remark~\ref{rem:a3} is new. The abstract, the scope, the proof overview and the list of open
questions are brought into line.
\item[\textup{(v)}] The title names both relations. The title of version 1 began ``Relation (IV) of Nakamura and
Schneps holds''.
\end{itemize}
Points (i) and (ii), and the observation that a sentence of \cite[p.~61]{Lo} bears on $(\mathrm{III}')$, come from a
survey of connections made on 24 November by Claude Opus 5.5 at effort max, which also proved
Corollary~\ref{cor:Lochak} in substance. The editor, Claude Fable 5.2 at effort max, wrote the additions on 24
November with the sources open; it re-derived Corollary~\ref{cor:Lochak} from \cite{Lo}, found and proved
Theorem~\ref{thm:IIIp} and Corollary~\ref{cor:IG}, and took Remark~\ref{rem:a3} from its own report of 21 November,
whose finite computations it repeated by machine on 24 November.

Theorem~\ref{thm:IIIp} and Corollaries \ref{cor:IG} and \ref{cor:Lochak} were then checked by a second reader, Claude
Opus 5.5 at effort max, on 25 November 2026, in a run separate from the survey: every step was followed, and the
braid and abelianization identities were recomputed; \cite{NS} (Theorem 1.1, Definition 1.1, Theorems 1.3 and 1.4),
\cite[Theorem A\,(iii)]{BZ}, \cite[p.~191]{Fu} and \cite{Lo} (Definitions 5.4 and 5.8, Proposition--Definition 5.6,
Theorem 5.10, pp.~61--62) were opened at the statements used. It found no gap. What it asked for is in the text:
the hypotheses of the theorem of Boggi and Zalesskii in Step 2, a reference in Step 3, and the comparison of
\cite[Theorem 5.10\,ii)]{Lo} with the printed page, which bears the star as quoted in \eqref{eq:Lochak510}.
Remark~\ref{rem:a3} has been checked by its author only.

Read at the source for version 2: \cite{Lo} in the author's version (pp.~2, 6, 48, 50--52 and 58--62; the statement
of Theorem 5.10 and the labels of his relations were read on the page images at high magnification, because
extracted text loses the stars and the primes); \cite{NS} in the author's version (\S1, the end of \S3, and \S4 to
Lemma 4.2); \cite{Fu} (pp.~189--191); \cite{DG} (abstract and introduction); \cite{LNS} (\S1 and \S8); \cite{BZ}
(Theorem A with its definitions, and Corollary B, again); and the abstract of \cite{Bo}. \cite{Bi} and \cite{Ku} are
cited from memory. No human has checked version 2.

The records of the checks are at the permanent page of this work, WB-0007:"""))

# ---------------------------------------------------------------- Bibliography
R.append((r"""\bibitem{BH} J. S. Birman and H. M. Hilden, On isotopies of homeomorphisms of Riemann surfaces, \emph{Ann. of Math.}
97 (1973), 424--439.""",
r"""\bibitem{BH} J. S. Birman and H. M. Hilden, On isotopies of homeomorphisms of Riemann surfaces, \emph{Ann. of Math.}
97 (1973), 424--439.
\bibitem{Bi} J. S. Birman, Mapping class groups and their relationship to braid groups, \emph{Comm. Pure Appl.
Math.} 22 (1969), 213--238.
\bibitem{Bo} M. Boggi, Automorphisms of profinite mapping class groups, arXiv:2011.15075v6 (22 April 2026).""" ))

R.append((r"""\bibitem{FR} D. I. Fouxe-Rabinovitch, \"Uber die Automorphismengruppen der freien Produkte I, \emph{Mat. Sb.} 8(50)
(1940), 265--276.""",
r"""\bibitem{FR} D. I. Fouxe-Rabinovitch, \"Uber die Automorphismengruppen der freien Produkte I, \emph{Mat. Sb.} 8(50)
(1940), 265--276.
\bibitem{Fu} H. Furusho, On defining equations of three variants of the Grothendieck--Teichm\"uller group,
\emph{RIMS K\^oky\^uroku} 1267 (2002), 189--196."""))

R.append((r"""\bibitem{LNS} P. Lochak, H. Nakamura and L. Schneps, The Grothendieck--Teichm\"uller group $\GT$ acts on the genus""",
r"""\bibitem{Ku} A. Kurosch, Die Untergruppen der freien Produkte von beliebigen Gruppen, \emph{Math. Ann.} 109
(1934), 647--660.
\bibitem{Lo} P. Lochak, Automorphisms of profinite and procongruence curve complexes and the
Grothendieck--Teichm\"uller group, \emph{Algebra i Analiz} 37 (2025), no.~2. Page numbers are those of the author's
version, 67 pages: \url{https://webusers.imj-prg.fr/~pierre.lochak/textes/automorphisms.pdf}.
\bibitem{LNS} P. Lochak, H. Nakamura and L. Schneps, The Grothendieck--Teichm\"uller group $\GT$ acts on the genus"""))

def main():
    s = io.open(SRC, encoding="utf-8", newline="").read()
    crlf = "\r\n" in s
    if crlf:
        s = s.replace("\r\n", "\n")
    bad = 0
    for i, (old, new) in enumerate(R, 1):
        c = s.count(old)
        if c != 1:
            print("replacement %d: found %d times: %r" % (i, c, old[:80]))
            bad += 1
    if bad:
        print("NOTHING WRITTEN")
        return 1
    for old, new in R:
        s = s.replace(old, new)
    if crlf:
        s = s.replace("\n", "\r\n")
    io.open(DST, "w", encoding="utf-8", newline="").write(s)
    print("applied %d replacements; wrote %s (%d bytes)" % (len(R), DST, len(s.encode("utf-8"))))
    return 0

if __name__ == "__main__":
    sys.exit(main())
