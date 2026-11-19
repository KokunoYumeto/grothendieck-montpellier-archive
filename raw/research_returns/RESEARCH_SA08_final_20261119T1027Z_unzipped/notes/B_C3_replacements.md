# C3: strict replacement routes and their exact obstructions

2026-11-19. GPT-6 Astra (OpenAI), automorphisms parallel agent.
This is an investigation of proposed constructions. No assertion below
refutes the common-source or terminal-groupoid conjecture for the whole
integral category.

## 1. The category being tested

Let $S=\Gamma_{\mathbb Z}(T)$, with $T$ of weight one and cochain degree zero.
The source conditions are the uniform eventual vertical resolution condition
in the attached transcription
input/RESEARCH_SA08_transcriptions/transcriptions/MPL_136_095-141_transcription.tex:573--607
and the eventual horizontal acyclicity condition at lines617--629.
The cochain degree is nonnegative and the differential raises it.
Both conditions must hold in each fixed cochain degree in all sufficiently
large weights; the vertical bound is uniform in simplicial degree.
All morphisms preserve the coefficient algebra, the two degrees, and the
strict PD structure.

Write $F$ for the standard theory and, for $N>1$, put
$A_N=S+F^{\text{weights}\geq N}$. This is the standard tail subtheory:
in weights below $N$ it has only the constant coefficient algebra, and in
weights at least $N$ it has all of $F$. Products and divided powers preserve
the indicated subobject. It is admissible, and the inclusion $A_N\to F$
is an actual morphism. It is consequently not a counterexample to
connectedness. Its horizontal degree-zero algebra has homotopy
$\pi_0(A_N^0)=S/I_N$, where $I_N$ is the full weight tail at least $N$,
and no higher homotopy.

## 2. A proved obstruction to free linear-disk replacements

Here “free” has a deliberately restricted meaning. A free linear-disk
PD DGA over $S$ is the free strictly graded commutative PD algebra on a
direct sum of cochain disks
$D^q(w)=(\mathbb Zx^q\xrightarrow{1}\mathbb Zy^{q+1})$
of specified nonnegative weights, with the coefficient algebra $S$
central and closed. On even generators the algebra is divided power;
on odd generators it is exterior. In the positive-weight version this
is the free object on graded sets for the algebraic theory of strict
PD DGAs. It is not an arbitrary semifree DGA with decomposable
generator differentials.

**Proposition C14.** There is no simplicial object $P$ whose individual
simplicial levels are free linear-disk PD DGAs, which satisfies eventual
vertical exactness, and which admits a degreewise surjective morphism
$P\to A_N$.

**Proof.** Suppose some level contains a disk with odd $q$.
The corresponding factor is
$D=S\otimes\Lambda(x)\otimes\Gamma(y)$ with $dx=y$ and $dy=0$.
Setting all other free generators and their differentials to zero
gives a cochain-DGA retraction onto this factor. For every $m\geq2$,

$$
d\bigl(x\gamma_{m-1}(y)\bigr)=m\gamma_m(y).
$$

Thus $H^{m(q+1)}(D)$ contains the direct summand
$(S/mS)\gamma_m(y)$. Already $m=2$ gives nonzero classes
$T^{[r]}\gamma_2(y)$ for all $r\geq0$, in the fixed cochain degree
$2(q+1)$ and unbounded weights. The retraction makes these classes
survive in the free algebra. This contradicts eventual vertical
exactness, even for this one simplicial level. No odd-to-even disk
can therefore occur.

In a free algebra on the remaining even-to-odd disks, every degree-one
element is a sum of terms $a\,dx$, where $a$ has cochain degree zero
and $x$ is a degree-zero disk generator. Higher even-degree
generators contribute no degree-one terms. Consider the weight-$N$
part of its image in $A_N$. If $\operatorname{wt}(x)<N$, the image of
$x$ is in the constant coefficient algebra and its differential
vanishes. If $\operatorname{wt}(x)=N$, the coefficient $a$ has weight
zero, so its image is also a scalar; the image of $a\,dx$ is closed.
Terms with larger weight cannot occur. This deals explicitly with
products of degree-zero and degree-one generators: those products
can have nonzero differentials in general, but not in this weight
in this target.

In simplicial degree two choose cumulative coordinates $X,Y$ for
$F_2=S\{X,Y\}\otimes\Lambda(dX,dY)$. The element
$X^{[N-1]}dY$ belongs to $A_N^{N,1}$ and satisfies

$$
d\bigl(X^{[N-1]}dY\bigr)=X^{[N-2]}dX\,dY\ne0.
$$

It cannot lie in the image just described. This contradicts
surjectivity in weight $N$, form degree one, simplicial degree two.
$\square$

**Scope.** The canonical free/cotriple simplicial resolution in the
algebraic theory has free linear-disk terms and a degreewise
surjective augmentation, so it cannot be an admissible replacement
of $A_N$. The same obstruction applies to any resolution with those
two properties. A trivial fibration in the usual horizontal model
structure is degreewise surjective, so a replacement built in this
specific free form also fails.

The proposition does not cover retracts of free objects. It does not
cover semifree DGAs whose generator differentials involve earlier
generators or decomposable terms. It does not rule out a common
source whose comparison maps are not trivial fibrations. In
particular it is not a general assertion that no useful cofibrant
subcategory can exist.

## 3. A rigorous PD extension detecting an additional possible obstruction

The following algebraic construction is proved independently of any
cotangent-complex interpretation. Fix a prime $p>N$. Let $J_p$ be the
subgroup of $S$ generated by $T^{[n]}$ for all $n\geq N$, $n\ne p$,
and by $pT^{[p]}$. Then $J_p$ is a PD ideal.

To check the ordinary ideal property, the only product needing
attention is a product landing in weight $p$. Its coefficient is
$\binom pa$, divisible by $p$ for $0<a<p$. A weight-zero scalar
preserves the prescribed subgroup. For the PD property, a monomial
term of $\gamma_m(a)$ of weight $p$, for $a\in J_p$ and $m\geq2$,
has coefficient

$$
\frac{p!}{\prod_d (d!)^{m_d}\prod_d m_d!},
\qquad
\sum_d d\,m_d=p,\quad \sum_d m_d=m,\quad d\geq N.
$$

Every denominator factorial has argument strictly below $p$:
$d<p$ and $m_d\leq p/N<p$. Hence the coefficient is divisible
by $p$. Terms of other weights at least $N$ already belong to
$J_p$. A summand involving the generator $pT^{[p]}$ cannot
contribute to weight $p$ when $m\geq2$. The addition and scalar
axioms now verify the PD property for arbitrary finite sums.

Consequently

$$
E_p=S/J_p\longrightarrow R=S/I_N
$$

is a strict PD algebra extension. Its kernel is
$M_p=\mathbb F_pT^{[p]}$, all products of two kernel elements and
all higher divided powers on the kernel are zero, and its
positive-weight coefficient action is zero. There is no
$S$-algebra section: the image of the coefficient $T^{[p]}$ is zero
in $R$ and nonzero in $E_p$.

The evident special-PD conormal candidate

$$
I_N\big/\bigl(I_N^2+
\langle\gamma_m(a):a\in I_N,\ m\geq2\rangle\bigr)
$$

has a nonzero class in weight $p$, detected by its quotient map
to $M_p$. This calculation holds at unbounded prime weights.
No exact order is asserted: although
$T\,T^{[p-1]}=pT^{[p]}$, the first factor $T$ does not lie in
$I_N$, so that identity by itself does not put $pT^{[p]}$
in the displayed denominator.

The ordinary Beck-module cotangent complex of PD algebras is not
automatically the special PD cotangent complex: it can carry
additional Frobenius operations. An initial attempt to identify
the preceding conormal module with its first homology therefore
left a real identification gate. The proof below bypasses that
identification completely.

### 3a. A direct obstruction to de Rham of a free horizontal resolution

**Proposition C15 (independently audited).** Let $Q\to R=S/I_N$
be a cellular free simplicial PD $S$-algebra resolution. Here
cellular means obtained from $S$ by successively adjoining free
PD simplex generators along their simplicial boundaries, with
the augmentation a weak equivalence in each weight. Then

$$
\pi_1\bigl(\Omega^1_{\rm PD}(Q/S)\bigr)^p\ne0
\qquad\text{for every prime }p>N.
$$

In particular the relative special PD de Rham algebra
$\mathrm{DR}_{\rm PD}(Q/S)$ fails eventual horizontal
acyclicity in form degree one.

**Proof of the module comparison.** Put
$\Omega=\Omega^1_{\rm PD}(Q/S)$ and
$L=R\otimes_Q\Omega$. The special differential module is
defined by the usual additive and Leibniz relations and
$d\gamma_m(a)=\gamma_{m-1}(a)\,da$ on the PD ideal.
In a free PD algebra its basis consists of the differentials
of its free generators.

Filter $\Omega$ by the simplicial stages at which the free
generators of $Q$ were adjoined. After extension of coefficients
to the final algebra $Q$, adjoining a generator of simplicial
dimension $n$ adds one module cell; its boundary is the
differential of the prescribed algebra boundary. The quotient
of two successive stages is

$$
Q\otimes_{\mathbb Z}
\bigl(\mathbb Z[\Delta^n]/\mathbb Z[\partial\Delta^n]\bigr),
$$

shifted by the weight of that generator. Each filtration
inclusion is split in each simplicial degree as a $Q$-module:
free generators provide the splitting. The corresponding
filtration of $L$ has quotient with $R$ replacing $Q$.
The quotient comparison is a weak equivalence. Indeed
normalization and Eilenberg--Zilber reduce it to tensoring the
weightwise quasi-isomorphism $NQ\to NR$ with the bounded
free complex of the indicated simplicial cell. Exact
sequences, induction over successor stages, and exactness of
filtered colimits over limit stages prove
$\Omega\to L$ a weak equivalence. This is a cell-filtration
proof of the required base-change assertion, not a claim
that every levelwise free simplicial module is cofibrant.

**Proof of the nonzero homology.** The group
$H_0(NL)$ represents special PD derivations $R\to M$ over
$S$, by the coequalizer defining $\pi_0Q=R$. Every such
derivation is zero because $S\to R$ is surjective. Hence
$H_0(NL)=0$.

Use the extension $E_p\to R$ constructed above. Freeness gives
an $S$-PD lift $\alpha:Q_0\to E_p$ of the augmentation
$Q_0\to R$. The two composites $\alpha d_0,\alpha d_1$
from $Q_1$ to $E_p$ have the same image in $R$. Their
difference

$$
\delta=\alpha d_0-\alpha d_1:Q_1\longrightarrow M_p
$$

is a special PD derivation. For products this follows from
$M_p^2=0$. For divided powers it follows from
$\gamma_m(e+u)-\gamma_m(e)=\gamma_{m-1}(e)u$ for
$u\in M_p$, since all higher divided powers of $u$ vanish.
Thus $\delta$ is represented by an $R$-linear map
$L_1\to M_p$. It is normalized because $d_0s_0=d_1s_0$,
and its cochain coboundary is zero by the simplicial
identities.

If $\delta$ were a derivation coboundary, say
$\delta=h d_0-h d_1$ for a special derivation
$h:Q_0\to M_p$, then $\alpha-h:Q_0\to E_p$ would again
be an $S$-PD algebra map. It would coequalize
$d_0,d_1:Q_1\rightrightarrows Q_0$ and so descend to
an $S$-PD section $R\to E_p$. Such a section was proved
impossible. Therefore

$$
H^1\operatorname{Hom}_{R,\mathrm{graded}}(NL,M_p)\ne0.
$$

This forces $H_1(NL)^p\ne0$. Here is the elementary
argument, including the grading. If $H_1(NL)^p=0$,
the cocycle $\delta$ kills the whole kernel of
$d:(NL)_1^p\to(NL)_0^p$. Since $H_0(NL)=0$, this
differential is surjective in every weight. Hence
$\delta$ factors through a map $h:(NL)_0^p\to M_p^p$.
Set $h=0$ in other weights. It is $R$-linear: for a
positive-weight $a\in R$ and $z$ in the necessary lower
weight, choose a preimage of $z$ under $d$ and use the
$R$-linearity of $\delta$ and the zero positive-weight
action on $M_p$. The factorization makes $\delta$ a
coboundary, a contradiction. The already proved
comparison $\Omega\to L$ finishes the proof.
$\square$

The argument uses only special square-zero extensions with
zero higher PD operations on their kernels. It does not
equate general Beck modules with ordinary $R$-modules.
It rules out exactly the proposal “freely resolve the
coefficient tail horizontally, then take its relative
PD de Rham algebra.” It does not cover a nonfree
replacement carrying additional relations or higher
cochain generators.

## 4. Other checked routes and exact failed steps

- A transferred vertical model structure with free linear-disk
  cofibrations fails the required preservation of acyclic disks:
  the odd-to-even calculation above is already a counterexample.
  This does not rule out a different model structure or different
  class of cofibrations.
- A general horizontal simplicial model structure for an
  algebraic theory exists; its free replacement is not thereby
  an object satisfying the manuscript's eventual vertical
  condition.
- Independently marked PD disks in any set of weights are
  already ruled out as a global repair by the exact theorem in
  notes/D_Cintegral_source_obstruction.md. Over $\mathbb Z$ the
  sole admissible source in that whole elementary family is
  one weight-one disk marked by $\pm T$.
- Weightwise nonlinear corrections remain a possible route, but
  their simplicial lifting problem is not solved by degreewise
  projectivity. A projective simplicial cover lifts through a
  degreewise surjection onto cycles; the kernel of that cover
  need only be degreewise projective. Its next lift can have an
  Ext obstruction against a cycle object. A lift into all forms
  need not be closed. The topos agent has isolated this same
  obstruction; no compatibility proof has been supplied.
- A cofree construction using products of whole DGAs makes
  horizontal objects contractible but enlarges vertical
  $H^0$ to products of $S$. The extra idempotents cannot be
  removed by a derivation, so the linear coinduction argument
  from the special weight-one category does not transfer.
- A Tate resolution in cochain degrees at most zero has the
  wrong direction for this problem. Reindexing also reverses
  the required de Rham differential and is not a solution.
- Strict E-infinity or derived comparison does not supply a
  strict PD common source unless a rectification and eventual
  bound theorem is separately established.

## 5. Primary-source checks for this investigation

Dokas--Frankland--Ikonicoff, arXiv:2403.18049, full source
sources/B_quillen_pd_source/DividedPowerAlg_20250108_arxiv.tex:
line424 fixes a field for the operadic PD results; lines450--516
give the general algebraic-category/Beck-module preliminaries
and the standard free simplicial resolution; lines1917ff and
1967ff describe the extra operation and differential relations
in the commutative PD case. These preliminaries support the
existence of a horizontal resolution, but do not prove that it
satisfies either eventual condition here. They do not identify
the special PD conormal candidate without further work.

Caradot--Lin, arXiv:2511.22614v1, primary HTML opened at
https://arxiv.org/html/2511.22614v1:
lines85--103 use the notation Cplx-plus for complexes in
nonpositive cochain degrees, and Theorem3.13 (lines514--528)
constructs a resolution in those degrees. This is not the
needed nonnegative de Rham replacement. Proposition3.10
(lines435--439) cannot be used as stated for arbitrary
surjective maps of differential complexes: a degreewise free
complex is not a projective object in the category of
complexes. Explicitly take $I'=D^0(\mathbb Z)$, $I=\mathbb Z[0]$,
and the surjective cochain map $I'\to I$. The square-zero
DGPD algebras $\mathbb Z\oplus I'\to\mathbb Z\oplus I$
have zero higher PD operations on their square-zero ideals.
The identity $\mathbb Z[0]\to I$ has no closed lift to $I'$.
This diagnoses that particular claimed lifting step; it is
not an assertion about the remaining results of the paper.
The full v1 source was then downloaded to
sources/B_caradot_lin2025_source/For_arxiv.tex and checked:
line227 states the degree convention, lines931--936 contain
the lifting proposition and its faulty implication, and
lines1122--1129 state the nonpositive Tate resolution.
The nearby earlier quasi-isomorphism hypothesis is inside
deleted source text, not in Proposition3.10.

## 6. Independent audits and finite arithmetic certificate

The shadows agent independently checked C15's PD ideal,
special derivation cocycle, derivative-cell filtration,
base change, and final H0/H1 argument. The root agent
then independently read and checked both C14 and C15.
Both audits accepted the explicitly limited scope.
The topos agent separately checked the non-split
extension detector. The formal paper version is
sections/B_C3_replacements.tex.

code/B_check_prime_pd_ideal.py checks integer coefficients
for every prime p<=43 and every 2<=N<=min(8,p-1).
All 79 pairs, 1,520 binomial-product coefficients, and
35,431 mixed PD partition coefficients pass. The full
receipt, including individual pairs and exact sample
integers, is logs/B_prime_pd_ideal_checks.json; recorded
runtime is 0.14087375499730115 seconds.
These computations corroborate the symbolic prime
argument; they do not replace it or test global C3.

Current smallest gate: construct a non-elementary strict PD
replacement with coherent vertical primitive lifting and
uniform eventual bounds, or find an invariant of every
admissible morphism that disproves the global uniqueness
assertion. No such construction or counterexample is claimed.
