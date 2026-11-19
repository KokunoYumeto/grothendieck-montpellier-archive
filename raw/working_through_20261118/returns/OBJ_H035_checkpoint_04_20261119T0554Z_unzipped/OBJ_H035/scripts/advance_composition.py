"""Record the countable-base closure proof and the smaller arbitrary-base gate."""
from pathlib import Path
from datetime import datetime,timezone
import csv

root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
new=r'''
\textbf{A stronger completion comparison, proved in this run.}
The following four arguments replace the nonartinian continuity gate above.
They do not use constructible rank or the generic parameter condition.

\emph{(A) Exact inverse limits over a complete local ring.}
Let $B$ be complete noetherian local and $D=\operatorname{Hom}_B(-,E)$,
where $E$ is the injective hull of its residue field. On finite modules
Matlis biduality gives $DDN=N$ (Stacks Proposition 47.7.8, tag 08Z9).
Consequently, for every inverse system of finite $B$-modules,
\[
 \lim_n N_n=D\bigl(\operatorname*{colim}_n D(N_n)\bigr).
\]
Since $D$ and filtered direct limits are exact, inverse limits are exact
on inverse systems whose terms are finite $B$-modules. This assertion
does not assert Mittag--Leffler stabilization of the original systems.
For a fixed $r$ it also gives
\[
 \operatorname{im}(\lim_n N_n\longrightarrow N_r)
 =\bigcap_{n\geq r}\operatorname{im}(N_n\longrightarrow N_r).
\]
Indeed apply exactness to the kernels and images of the maps to $N_r$.

\emph{(B) Detection of pro-zero systems by local completions.}
Let $C$ be noetherian and $N_n$ an inverse sequence of finite
$C$-modules. If $\lim_n(N_n\otimes_C\widehat{C_q})=0$ for every
prime $q$, then $\{N_n\}$ is pro-zero. To prove this, fix $r$ and put
$J_n=\operatorname{im}(N_n\to N_r)$ for $n\geq r$. The descending
closed subsets $\operatorname{Supp}J_n$ stabilize, since
$\operatorname{Spec}C$ is noetherian. If the stable closed set is
nonempty, choose one of its generic points $q$. For all sufficiently
large $n$, $(J_n)_q$ is a nonzero finite-length module. These descending
submodules of the finite-length $(J_{n_0})_q$ stabilize at a nonzero
module. Faithful flatness preserves it in $\widehat{C_q}$, contradicting
(A) and the zero inverse limit there. Thus some $J_n=0$, as required.
If every $N_n$ is supported in $V(I)$, it suffices to test $q\in V(I)$.
The finite-length assertion uses that a generic point of the stable
support has no smaller prime in that support after localization.

\emph{(C) Finite output implies the required pro-comparison.}
Let $A$ be noetherian, $I\subset A$, $C=\widehat A_I$, and $M$ a
finite $C$-module. Suppose $G$ is additive, $A$-linear, finitary, finite
on finite $A$-modules, and satisfies (iii a) at every prime of $A$.
If $W=G(M)$ is finite over $C$, then the natural map is a pro-isomorphism
\[
 \{W/I^nW\}_n\longrightarrow\{G(M/I^nM)\}_n.                 \tag{39.1}
\]
In particular this conclusion does not require assuming (iii b) for $G$.
The induced action of $C$ on values makes the restriction of $G$ to
$C$-modules a finitary $C$-linear functor. Flat scalar extension thus
commutes with it by H035.2. Both terms of (39.1), and its kernel and
cokernel, are finite $C$-modules: $M/I^nM$ is finite over $A/I^n$.

For $q\in V(IC)$ let $p=q\cap A$. Then $q=pC$ and
$C/p^rC=A/p^r$, because $I^r\subset p^r$ and completion is exact
on finite modules. Localizing and completing yields
\[
 B=\widehat{C_q}=\widehat{A_p}.
\]
Put $M_B=M\otimes_C B$, and write $\mathfrak m_B$ for the maximal
ideal of $B$. Apply (iii a) to each finite $B$-module $M_B/I^nM_B$.
Commutation of the two inverse limits gives, naturally,
\begin{align*}
 \lim_n G(M_B/I^nM_B)
 &=\lim_n\lim_r G(M_B/(I^n+\mathfrak m_B^r)M_B)\\
 &=\lim_r\lim_n G(M_B/(I^n+\mathfrak m_B^r)M_B)\\
 &=\lim_r G(M_B/\mathfrak m_B^rM_B)=G(M_B).
\end{align*}
For fixed $r$ the inner system is constant once $n\geq r$.
The finite $B$-module $W\otimes_C B$ is $I$-adically complete:
exactness in (A) applied to its quotients proves surjectivity to their
limit, while $I\subset\mathfrak m_B$ and Krull intersection prove
injectivity. Hence the limit of (39.1) after tensoring with $B$ is
an isomorphism. By (A), the limits of its kernel and cokernel vanish.
These error systems are supported in $V(IC)$; (B) makes them pro-zero.
This proves (39.1).

\emph{(D) Countability supplies finite output for every ideal completion.}
Assume additionally that $A$ is countable and that $G$ satisfies the
$I$-completion comparison on the finite $C$-module $M$. Then
\[
 W=G(M)=\lim_n V_n,\qquad V_n=G(M/I^nM),
\]
is complete metrizable for the inverse-limit topology with discrete
levels. Each $V_n$ is finite over $C$; finite length is not required.
Every finite $C$-submodule $L$ of $W$ is closed in this topology.
Here is the point that replaces the earlier artinian-level argument.

Let $w$ lie in the closure of $L$, and let $q$ be a maximal ideal of
$C$. Since $IC\subset\operatorname{Jac}(C)$, $q\in V(IC)$, and
the ring $B=\widehat{C_q}$ above is a faithfully flat completion of
$C_q$. There is a natural continuous map
\[
 W\longrightarrow W\otimes_C B
 =G(M_B)=\lim_r G(M_B/\mathfrak m_B^rM_B).
\]
Continuity follows because the $r$th coordinate factors through $V_r$:
$I^rM$ maps into $\mathfrak m_B^rM_B$. The image of the finite
$B$-module $L\otimes_C B$ in this last limit is closed. Indeed, its
coordinate images are finite $B$-modules, and (A) makes the map from
the constant inverse system $L\otimes_C B$ onto the inverse system
of these images surjective on limits. A point in the closure is
precisely a compatible family in these images. Thus $w\otimes1$
belongs to $L\otimes_C B$. Faithful flatness shows that the class
of $w$ in $(W/L)_q$ vanishes. This is true at every maximal ideal,
so that class vanishes and $w\in L$.

For each finite $A$-module $N$, the evaluation image
\[
 E_N=\operatorname{im}\bigl(\operatorname{Hom}_A(N,M)
              \otimes_A G(N)\longrightarrow W\bigr)
\]
is finite over $C$. A finite presentation of $N$ realizes its Hom
module as a submodule of a finite sum of copies of $M$, and $G(N)$
is finite over $A$. Countability of $A$ gives countably many
isomorphism classes of such $N$, by their finite presentation matrices.
The finite sums $E_1\subset E_2\subset\cdots$ of the corresponding
images are finite closed $C$-submodules. Finitarity gives
$W=\bigcup_j E_j$. Baire's theorem, with the nested-ball proof already
given above, makes some $E_j$ open. It contains $\ker(W\to V_n)$
for some $n$; hence $W/E_j$ is a quotient of a submodule of the
finite $C$-module $V_n$. It is finite, and therefore so is $W$.
Applying (C) gives the pro-comparison (39.1).

\textbf{Countable-base composition theorem (ours).}
The full affine composition assertion holds for every countable
noetherian $A$ in the reconstructed class. For (iii a), use the
countable local-completion lemma at $A_p$. For (iii b), use (D)
with $I=(a)$ and then (C). Applying the outer functor $F$ levelwise
to (39.1), and using its completion axiom on the now finite completed
module $W$, gives
\[
 F(G(M))=F(W)=\lim_n F(W/I^nW)
          =\lim_n F(G(M/I^nM)).
\]
Functorial application preserves a pro-isomorphism, and inverse limits
send isomorphic pro-objects to isomorphic modules. The same argument
applies at maximal completions. The other axioms were proved stable
at the beginning of this section. This completes all axioms for
countable $A$, without replacing the broad class by coherent functors.

\textbf{Strictly smaller arbitrary-base gate.}
For arbitrary noetherian $A$, it now suffices to establish finite
generation of $G(M)$ over each completion when $M$ is finite over that
completion. Argument (C) then supplies the needed principal
pro-comparison; the local version follows from the artinian-level
argument. All finite evaluation images are closed, by (D), without
countability. What remains unproved is the step from their possibly
uncountable union to finite generation. Baire alone does not justify
that step. This is a sufficient gate, not an assertion that failure
of finite generation by itself refutes composition.
'''

p=root/'PROOFS.tex'
s=p.read_text()
needle='\\textbf{Rejected counterexample.}'
assert s.count(needle)==1
s=s.replace(needle,new+'\n'+needle)
s=s.replace('The only remaining affine axiom is completion. The unresolved issue is',
'''The only remaining affine axiom is completion. At this earlier stage of the
argument the unresolved issue was''')
s=s.replace('This section is deliberately a working state, not a proof certificate.',
'''The stronger arguments below settle this for countable bases and reduce
the remaining general problem to finite output on completed modules.
The unrestricted assertion remains a working state.''')
p.write_text(s)

with (root/'STATEMENTS.tsv').open() as f:reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
row=next(r for r in rows if r['id']=='H035.39')
row['statement']='Prospective constructible-functor programme. Our exact affine question takes additive A-linear functors Mod(A)→Mod(A), with A a noetherian quotient of a regular noetherian ring, satisfying H035.30(i),(iii a,b),(iv),(v),(vi), and asks whether composition satisfies the same axioms. All noncompletion axioms are stable. Full closure is proved for countable A, Dedekind domains and artinian rings. For arbitrary A it suffices to prove finite generation of G(M) over every local or principal completion when M is finite over it; finite output implies the required pro-comparison. This remaining finite-output gate is open.'
row['status']='open — arbitrary-base completed-output finiteness gate; countable-base composition proved'
row['reconstruction']='Additivity, A-linearity and the affine class are explicit reconstructions. The countable-base theorem and finite-output reduction are this run’s additions, not statements read into the page.'
with (root/'STATEMENTS.tsv').open('w') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

with (root/'research/COMPOSITION_ATTEMPTS.md').open('a') as f:
 f.write('\n\n## '+stamp+' — Countable-base closure and a smaller general gate\n\n')
 f.write('PROOFS.tex, H035.39 arguments (A)–(D), now give a full countable-base proof. Exact inverse limits of finite modules over complete local rings follow from Matlis biduality. A finite inverse system is pro-zero if its limit vanishes after every completed localization: stabilize its support and test a generic point. Those facts prove the formal pro-comparison whenever the completed output is finite. All finite evaluation images are closed even for a nonartinian principal-adic tower, by testing closure at every completed maximal localization. Countability plus Baire then makes the output finite. No Mittag–Leffler assertion is made for a nonartinian tower.\n\nThe strongest remaining sufficient gate for arbitrary bases is completed-output finite generation. Baire does not handle the uncountable cover. Earlier attempts that stopped at nonartinian continuity are superseded by this argument. A failure of this sufficient finiteness property would not alone be a counterexample to composition.\n')

with (root/'progress.log').open('a') as f:f.write('H035.39 countable-base proof and smaller general gate recorded '+stamp+'\n')

(root/'CONSEQUENCES.tsv').write_text('tag\tstatement_id\trelation\tevidence\n')
with (root/'research/RESULTS_AUDIT.md').open('w') as f:
 f.write('# Results attachment audit\n\nThe entry was frozen at 2026-11-19T04:57:19.455652Z before the results were opened at 2026-11-19T04:57:32.469591+00:00. The preserved pre-results entry and its SHA-256 are in research/ENTRY_BEFORE_RESULTS.md and research/ENTRY_BEFORE_RESULTS.sha256.\n\nThe extracted RESULTS_CITING.tsv contains its header and zero data rows. README.md explicitly records zero citing rows. CONSEQUENCES.tsv therefore contains only its four-column header. No relationship or research claim has been inferred from the empty register. This is a documentary inventory check, not a mathematical check event for a nonexistent result.\n')
print('Recorded stronger H035.39 argument; updated its statement row; recorded empty results register.')
