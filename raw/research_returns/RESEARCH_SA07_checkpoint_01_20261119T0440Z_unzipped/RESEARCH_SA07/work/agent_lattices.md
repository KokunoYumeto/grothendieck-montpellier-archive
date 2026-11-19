# Betti lattices, adelic genericity, and the comparison cocycle

AI-produced by GPT-6 Astra (OpenAI), research subtask
`/root/period_generation`, 19 November 2026. No priority claim. This file
supplies Part D and supplements A.5. It uses `agent_generation.md` as the
location of GEN-1 through GEN-5. Mathematical results below have explicit
scopes; the exact field called `K` on 18:45 remains unidentified by the
supplied pages.

## LAT-1. The three finite coefficient rings and the Betti lattice map

**Status: Proved definitions and topology checks.** Set
\[
\widehat{\mathbf Z}=\prod_\ell\mathbf Z_\ell,
\qquad
\mathbf A_f=\widehat{\mathbf Z}\otimes_{\mathbf Z}\mathbf Q
=\prod_\ell'\mathbf Q_\ell,
\qquad
R_{\mathrm{all}}=\prod_\ell\mathbf Q_\ell.
\]
The restricted product is with respect to \(\mathbf Z_\ell\). Its
topology makes \(\widehat{\mathbf Z}\) compact and open. Give
\(R_{\mathrm{all}}\) the product topology. The displayed inclusions
\(\widehat{\mathbf Z}\hookrightarrow\mathbf A_f\hookrightarrow
R_{\mathrm{all}}\) are ring maps. The second is a proper inclusion:
\((1/\ell)_\ell\) belongs to its target and not its source. It is
continuous and its image is dense, but it is not a homeomorphism onto
its image with the induced topology: every product neighborhood of zero
allows a nonintegral coordinate at some prime outside its finite set of
restrictions, while \(\widehat{\mathbf Z}\) is open in \(\mathbf A_f\).

For an affine algebraic group \(G/\mathbf Q\), choose a faithful integral
model away from finitely many primes. Then \(G(\mathbf A_f)\) is the
restricted product of \(G(\mathbf Q_\ell)\) with respect to the compact
open integral subgroups. A change of model alters only finitely many of
these choices and gives the same restricted topology. For
\(G=\operatorname{GL}_m\) the group
\(G(\widehat{\mathbf Z})=\prod_\ell\operatorname{GL}_m(\mathbf Z_\ell)\)
is compact and open there.

In the literal full product \(\prod_\ell\operatorname{GL}_m(\mathbf Q_\ell)\)
there is no compact open subgroup when \(m>0\). Indeed, an open
neighborhood of the identity contains unrestricted factors at every
prime outside a finite set. Its projection onto any such factor is the
whole noncompact \(\operatorname{GL}_m(\mathbf Q_\ell)\), whereas the
continuous image of a compact set is compact. Thus the compact-open
lemma of 18:49 cannot be used in that product topology for the elliptic
groups. The statement becomes useful in the restricted topology just
defined. The literal product on 18:47 and the integral product written
in the margin of 18:51 are retained as transcription data; neither is
silently replaced by \(\mathbf A_f\).

For an abelian variety \(A/k\), with \(k\) algebraically closed of
characteristic zero and \(v:k\hookrightarrow\mathbf C\), define
\[
L_v=H^1(A_v(\mathbf C),\mathbf Z),\qquad
T_\ell=H^1_{\mathrm{et}}(A,\mathbf Z_\ell).
\]
These groups are torsion-free. Integral comparison gives canonical
maps
\[
c_{v,\ell}:L_v\otimes\mathbf Z_\ell\xrightarrow{\sim}T_\ell,
\qquad
L_v\longrightarrow\prod_\ell T_\ell,quad
x\longmapsto(c_{v,\ell}(x))_\ell.
\tag{LAT-1.1}
\]
The first map follows by applying SGA4, Exposé XVI, Théorème 4.1 to
\(A_v\), with coefficients \(\mathbf Z/\ell^r\), and passing to the
inverse limit. Betti \(H^1\) is free because the analytic space is a
real torus; the finite inverse systems satisfy the Mittag–Leffler
condition. Geometric étale base change identifies the algebraically
closed realizations. Tensor products, duality, cup products, and
algebraic correspondences are preserved by these comparisons.

The second map is injective and its completion is an isomorphism onto
\(\prod T_\ell\). In particular its image is dense in this compact
module: after identifying \(L_v\) with \(\mathbf Z^{2\dim A}\), this
is precisely the Chinese remainder theorem. It is not a discrete
subgroup of the finite adelic space. Calling it a lattice refers to
its abstract full-rank integral structure, not discreteness in that
topology. The archimedean component on 18:53 is what allows the usual
discrete diagonal lattice interpretation.

For a general rational motive an integral lattice requires additional
data (for example a specified geometric presentation and lattices on
its projectors). There cannot be an additive tensor functor from the
entire rational category to nonzero finite free \(\mathbf Z\)-modules:
the mutually inverse morphisms \(n\operatorname{id}\) and
\(\frac1n\operatorname{id}\) would have to give an integral inverse to
\(nI\), for \(n>1\). All rational torsors below are defined without
that problem. Integral counterexamples below use only actual varieties,
integral homology, and isogenies, so their morphisms act integrally.

## LAT-2. Exact quotient and the dimension bound of 18:47–49

**Status: Proved.** Let \(\mathcal T=\langle M\rangle\) be a neutral
Tannakian category over \(\mathbf Q\), with a tensor generator and
Betti fibre functors \(\xi,\xi_1,\ldots,\xi_n\). Put
\[
G=\operatorname{Aut}^{\otimes}(\xi),\quad d=\dim G,
\quad P_i=\operatorname{Isom}^{\otimes}(\xi,\xi_i).
\]
Each \(P_i\) is a right \(G\)-torsor. There is a canonical algebraic
isomorphism of the fpqc quotient with an affine scheme,
\[
V:=(\prod_{i=1}^nP_i)/G
\xrightarrow{\sim}
\prod_{i=2}^n\operatorname{Isom}^{\otimes}(\xi_1,\xi_i),
\qquad
(p_i)\longmapsto(p_i p_1^{-1})_{i\ge2}.
\tag{LAT-2.1}
\]
The map is unchanged when each \(p_i\) is composed on the right with
the same \(g\). Conversely, fpqc-locally choose \(p_1\); for given
relative isomorphisms \(q_i\), put \(p_i=q_i p_1\). A different
\(p_1\) changes the tuple by exactly the diagonal action. These
inverse constructions prove the quotient claim, including its
representability. Each factor on the right is a torsor of dimension
\(d\), so
\[
\dim V=(n-1)d.
\tag{LAT-2.2}
\]

The comparison maps (LAT-1.1), rationalized, give
\(p_{i,\ell}=c_{i,\ell}^{-1}c_{0,\ell}\) and therefore a canonical
relative point \(q_\ell\in V(\mathbf Q_\ell)\). At every prime
\[
\operatorname{trdeg}_{\mathbf Q}\mathbf Q(q_\ell)
\leq(n-1)d.
\tag{LAT-2.3}
\]
Indeed evaluation on the coordinate ring has a prime kernel and its
image is a finitely generated domain whose fraction field is
\(\mathbf Q(q_\ell)\); its dimension is at most \(\dim V\).
Taking only the underlying vector spaces replaces the isomorphism
torsors by \(\operatorname{GL}_m\)-torsors, giving the written bound
\((n-1)m^2\). The map from (LAT-2.1) to that larger relative
isomorphism scheme is induced by forgetting the tensor equations.

A point over the product ring \(R_{\mathrm{all}}\), or over
\(\mathbf A_f\), does not by itself define a field of coordinates.
One precise joint invariant is the Krull dimension of
\[
A_q=\operatorname{im}\bigl(\mathbf Q[V]\to R_{\mathrm{all}}\bigr).
\]
It is still at most \((n-1)d\). Its kernel need not be prime. For
example, in \(\mathbf G_m(\widehat{\mathbf Z})\), take the component
at \(2\) to be \(1\) and every other component to be \(2\). The
coordinate algebra is \(\mathbf Q\times\mathbf Q\). Thus calling
this joint invariant the transcendence degree of a field would require
an additional convention.

Conversely the tuple \(x_\ell=\ell+1\in\mathbf Z_\ell^\times\)
has each component rational, of transcendence degree zero, while
evaluation \(\mathbf Q[x,x^{-1}]\to\prod\mathbf Q_\ell\) is
injective: a nonzero Laurent polynomial cannot vanish at infinitely
many distinct rational numbers. Its joint coordinate algebra has
dimension one. These two exact evaluation maps prevent an interchange
of joint and componentwise genericity.

For connected \(G\), equality in (LAT-2.3) is exactly injectivity of
evaluation on \(\mathbf Q[V]\), namely genericity of that relative
point. Coincident places give the identity relative point and degree
zero; for \(d>0,n>1\) the bound is strict. The unit motive has \(d=0\)
and equality for every system. LAT-3 and LAT-4 prove maximal attainment
after Galois changes for the non-CM elliptic cases in the question.
They do not classify every prescribed tuple of places for every
motive; that broader demand remains an unresolved item of the prompt.

## LAT-3. The compact-open genericity lemma, including joint genericity

**Status: Proved, in the restricted adelic topology.** Let
\(G/\mathbf Q\) be connected affine of finite type,
\(U\subset G(\mathbf A_f)\) a compact open subgroup, and
\(a\in G(\mathbf A_f)\). The set of \(x\in Ua\) whose every
component is generic in \(G\) over \(\mathbf Q\) has full Haar
measure in this coset, in particular is nonempty. The same statement
for \(G^r,U^r,a\) gives a tuple of \(r\) components jointly generic
at every prime. Separate genericity of each member would not suffice
for that conclusion; applying the lemma to the product supplies it.

Here is a proof. The nonzero elements of \(\mathbf Q[G]\) form a
countable set. Fix one of them, \(f\), and one prime \(\ell\). The
zero set of \(f\) in any open subset of \(G(\mathbf Q_\ell)\) has
Haar measure zero. To verify this last statement, use analytic
coordinates on the smooth group. A nonzero regular function cannot
be identically zero on an analytic open set: its image in the
completed local ring is nonzero, since the local ring injects into
its completion, and analytic coordinates identify that completion
with a formal power series ring. A nonzero convergent power series
has a measure-zero zero set. In one variable its zeros are isolated
on sufficiently small discs (use the first nonzero Taylor term, or
the usual finite-zero assertion on a closed disc). Inductively in
the number of variables, expand in the last variable. The locus
where all coefficient functions vanish is contained in the zero
set of one nonzero coefficient and has measure zero by induction;
outside that locus the one-variable assertion and Fubini apply.
A countable cover by charts gives the claim.

The projection \(U_\ell\) of \(U\) is compact and open in
\(G(\mathbf Q_\ell)\). Openness follows because projection of a
basic adelic neighborhood is open. The push-forward of normalized
Haar measure on \(U\) is normalized Haar measure on \(U_\ell\).
Thus the set of \(u\) with \(f((ua)_\ell)=0\) has measure zero.
There are only countably many pairs \((\ell,f)\). Their union has
measure zero; its complement proves the result. Translation is an
algebraic and analytic isomorphism, so it preserves the zero-set
arguments. The proof also works on any locally nonempty torsor, with
its transported Haar measure, because the local comparison maps are
isomorphisms of smooth varieties.

Let \(\Gamma_M\) be the continuous adelic Galois image for a chosen
integral realization. A finite-index image in
\(G(\widehat{\mathbf Z})\) is open here: continuity makes the image
compact and hence closed, and the complement of one of finitely many
closed cosets is closed. With the relative frames written as
\(a_i=g_i g_1^{-1}\), independent changes of the places give
\((u_i a_i)_{2\le i\le n}\), with \(u_i\in\Gamma_M\). Applying
the product lemma chooses them jointly generic for every \(\ell\).
Choose preimages \(\sigma_i\) of the \(u_i\); an automorphism of
the algebraic closure of the field of definition extends to the
ambient algebraically closed field after choosing a transcendence
basis. This proves exactly the implication stated on 18:49–51.

## LAT-4. Unconditional elliptic products: exact theorem inputs

**Status: Known input plus the derivation of LAT-3.** For a number field
\(K\) and a non-CM elliptic curve \(E/K\), Serre's original 1972
paper, §4.4, Théorème 3, p.299, states that the adelic image is open
in \(\prod_\ell\operatorname{GL}(T_\ell E)\). The original French
page was read as an image, not inferred from a search snippet. Its
Théorème 3′ on the same page gives the equivalent bounded-index
formulation at finite levels. Thus LAT-3 applies with
\(G=\operatorname{GL}_2\), \(d=4\): after independently changing
\(n-1\) places galoisiennement, every \(\ell\)-component has
transcendence degree \(4(n-1)\) over \(\mathbf Q\).

For two curves, Serre §6.1, Théorème 6, p.324, has an extra hypothesis
which must be retained when stating the historical theorem: the two
systems of \(\ell\)-adic representations do not become isomorphic
over any finite extension. Its conclusion is openness in the group
of pairs with equal determinants. Serre explicitly calls equivalence
of that hypothesis with geometric non-isogeny probable in the
following remark. Faltings, *Endlichkeitssätze für abelsche Varietäten
über Zahlkörpern*, §5, Satz 4 and Korollar 2, pp.360–361, now supplies
that implication. If the systems became isomorphic over a finite
extension \(K'/K\), Korollar 2 over \(K'\) would make the curves
\(K'\)-isogenous, contradicting geometric non-isogeny.

For \(r\ge2\), Lombardo, *An explicit open image theorem for products
of elliptic curves*, Theorem 1.1, gives finite index for geometrically
pairwise non-isogenous non-CM curves over a number field in
\[
\Delta_r(\widehat{\mathbf Z})=
\{(g_1,\ldots,g_r)\in\operatorname{GL}_2(\widehat{\mathbf Z})^r:
\det g_i=\det g_j\text{ for all }i,j\}.
\tag{LAT-4.1}
\]
This includes \(\ell=2\); the paper treats that prime separately in
its proof. The common determinant is forced by the Weil pairing, as
its Remark 1.2 explains. The corresponding connected rational
motivic group is \(\Delta_r\), because the Hodge classes on products
of elliptic curves are generated by the divisor/endormorphism
constraints (KSV Proposition 5.14). It has dimension \(3r+1\).
Applying LAT-3 gives equality
\[
\operatorname{trdeg}_{\mathbf Q}\mathbf Q(q_\ell)
=(n-1)(3r+1)\quad\text{for every prime }\ell
\]
for suitably modified places. This proves Lead H6 in its number-field
scope. No assumption of rational approximation in \(\Delta_r\) is
needed for this genericity conclusion.

## LAT-5. Which connected affine groups have the approximation property?

**Status: Known criterion, with exact reductions and explicit elliptic
tests.** For a connected affine group \(G/\mathbf Q\), the density
\(G(\mathbf Q)\subset G(\mathbf A_f)\) holds precisely when its
reductive quotient by the unipotent radical is semisimple and simply
connected and each of its nontrivial \(\mathbf Q\)-simple factors has
noncompact real points. A trivial reductive quotient is allowed.

The exact source chain is Kneser, *Starke Approximation in algebraischen
Gruppen I* (1965), Satz 1, p.191, and Hilfssätze 2.3–2.5, pp.193–194,
together with Platonov, *The problem of strong approximation and the
Kneser–Tits conjecture for algebraic groups* (1969), Theorem A, p.1140,
and its 1970 addendum, especially §2. Kneser's necessary conditions
make the radical unipotent and the semisimple quotient a product of
simply connected simple factors. His quotient, product, and
restriction-of-scalars lemmas reduce both directions to those
factors. Platonov's theorem, with the correction in the addendum,
supplies sufficiency for each noncompact factor. This identifies the
actual quotient maps and products used in the criterion; it is not
an extrapolation from connectedness alone.

For the groups needed here an elementary proof is available on the
derived factors. The additive group \(\mathbf Q\) is dense in
\(\mathbf A_f\): multiply the finitely many required approximations
by a common denominator and use the Chinese remainder theorem.
For \(\operatorname{SL}_2\), the polynomial maps
\[
x\longmapsto\begin{pmatrix}1&x\\0&1\end{pmatrix},\qquad
x\longmapsto\begin{pmatrix}1&0\\x&1\end{pmatrix}
\]
therefore put their adelic images in the closure of
\(\operatorname{SL}_2(\mathbf Q)\). They generate
\(\operatorname{SL}_2(\mathbf A_f)\). One way to check generation
is Gaussian elimination over the restricted product: for a matrix
with first column \((a,c)\), choose an integral adelic \(t\) so
that \(a+tc\) is a unit at every sufficiently large prime (one of
the residue choices works), and choose arbitrary suitable local
values at the remaining finitely many primes. This makes
\(a+tc\in\mathbf A_f^\times\). Eliminate the lower entry and then
the upper off-diagonal entry; a diagonal matrix
\(\operatorname{diag}(u,u^{-1})\) is a product of elementary
matrices, by the usual two-by-two identity. The same construction
works factor by factor for \(\operatorname{SL}_2^r\).

For \(\mathbf G_m\) the failure is explicit. A rational number which
is a unit in every \(\mathbf Z_\ell\) is \(1\) or \(-1\).
The adelic open set of units everywhere with residue \(2\pmod5\)
at the prime 5 contains neither. Consequently
\(\mathbf Q^\times\) is not dense in \(\mathbf A_f^\times\).
The common determinant map
\[
\Delta_r\longrightarrow\mathbf G_m
\]
has the explicit section
\(t\mapsto(\operatorname{diag}(t,1),\ldots,
\operatorname{diag}(t,1))\). The inverse image of that nonempty
adelic open set is nonempty and has no rational point. Thus the
full groups \(\operatorname{GL}_2\) and \(\Delta_r\) occurring in
LAT-4 do not have the approximation property, even though their
derived groups \(\operatorname{SL}_2^r\) do. This proves the exact
effect of the determinant quotient.

## LAT-6. The equivalence in the margin: two precise readings

**Status: Both implications resolved after specifying the quantified
statement; the manuscript's undefined word remains a textual gate.**
Let \(L=G(\mathbf A_f)\), let \(H\subseteq G(\widehat{\mathbf Z})\)
be a compact Galois image, and assume \(G(\mathbf Q)\) is dense in
\(L\).

For the **all-frame commensurability statement**
\[
\text{every coset }Ha\ (a\in L)\text{ meets }G(\mathbf Q),
\qquad\text{equivalently }L=H G(\mathbf Q),
\tag{LAT-6.1}
\]
openness of \(H\) is equivalent to the statement. One implication
uses density and the fact that \(Ha\) is open. Conversely,
\(G(\mathbf Q)\) is countable, so (LAT-6.1) writes the locally
compact Baire space \(L\) as a countable union of closed cosets of
\(H\). Some coset has interior, hence \(H\) is open. Since
\(G(\widehat{\mathbf Z})\) is compact, this is the finite-index
condition there. No generic-point lemma is needed for this reverse
argument. The proof quantifies over all adelic frames; applying it
only to frames known to arise from places requires a separate
surjectivity/density assertion about that family.

For the **componentwise-generic statement**, the reverse implication
is false for algebraic group actions, even with strong approximation.
Take \(G=\operatorname{SL}_2\) and
\[
H=\prod_\ell H_\ell,\qquad
H_\ell=\{g\in\operatorname{SL}_2(\mathbf Z_\ell):
g\bmod\ell\text{ is upper triangular}\}.
\]
Every \(H_\ell\) is open in its local group, but
\([\operatorname{SL}_2(\mathbf Z_\ell):H_\ell]=\ell+1\), so \(H\)
is closed of infinite index and is not adelically open. Nevertheless
the product Haar argument of LAT-3 applies in every coset of
\(H^r\): each projection is open, so all countably many algebraic
zero sets have measure zero. Every coset contains a tuple jointly
generic at every prime. LAT-5 proves strong approximation for this
\(G\). This is an explicit group-theoretic counterexample; no
unproved claim that this particular subgroup is a motivic Galois
image is made.

There is also a genuine motivic failure of the converse without the
approximation premise. Let \(M=\mathbf Q(-2)\) over \(\mathbf Q\).
Its tensor group is \(\mathbf G_m\). The map from the category
generated by \(\mathbf Q(-1)\) restricts on groups to
\(t\mapsto t^2\). Thus its finite Galois image is
\[
H=(\widehat{\mathbf Z}^{\times})^2
=\prod_\ell(\mathbf Z_\ell^\times)^2.
\tag{LAT-6.2}
\]
Cyclotomic surjectivity follows from
\(\operatorname{Gal}(\mathbf Q(\mu_N)/\mathbf Q)
=(\mathbf Z/N\mathbf Z)^\times\) at every finite level. Each local
square subgroup is open, while the global index is infinite:
reduction modulo any \(r\) distinct odd primes gives a quotient
\((\mathbf Z/2\mathbf Z)^r\). The same product-measure argument
gives joint genericity in every coset, including all frames obtained
by changing places. It follows that the stated finite-index
“strengthened Tate” input is itself false for arbitrary tensor
motives under this integral group convention. The finite central
isogeny \(t\mapsto t^2\) explains the obstruction explicitly.

The manuscript does not define “indépendance des réseaux” in the
margin. Equations (LAT-6.1) and the componentwise-generic property
are two exact possible formulations, and the preceding proofs give
different reverse-implication outcomes. Neither outcome may be
silently substituted for the unformulated sentence.

## LAT-7. The field `K` and Lead H5

**Status: source reconstruction incomplete; the proposed automatic
filtration argument is refuted in its two-embedding interpretation.**
The supplied 18:42 heading, 18:43 list, and 18:45 calculation never
give generators or a universal property for \(K\). Page 18:45 only
states the numerical bound after the dimensions of \(G\) and \(B\).
The canceled normalized-point conjecture on 18:12 does not identify
this \(K\). A text search through the supplied cote-18
transcriptions did not find a defining sentence connecting it to
18:45. The uncertainty \(\leq\unsure{5|4}\) over \(k(\pi)\) is
therefore retained. A determination of the exact numerical
\(\operatorname{trdeg}_kK\) cannot be supplied from these data.

The correct dimension computation for a **specified flag fibre** is
as follows. For two nonisogenous non-CM elliptic factors,
\[
G=\{(g_1,g_2)\in\operatorname{GL}_2^2:
\det g_1=\det g_2\},\quad\dim G=7.
\]
The stabilizer of one line in each standard two-dimensional factor
consists of upper-triangular matrices with the same determinant. Its
dimension is \(3+3-1=5\). Thus the orbit map
\(G\to\mathbf P^1\times\mathbf P^1\) has fibres of dimension five.
For two flags defined over \(k\), the scheme of elements taking one
to the other is a \(B\)-torsor and any of its points has coordinate
transcendence degree at most five over \(k\). On fixing the common
determinant it has dimension four. These statements are proved by
the displayed equations; they do not identify the manuscript's
undefined \(K\) with the field of a point in one of those fibres.

The precise maps for two embeddings show the missing step in H5.
For \(v,w:k\hookrightarrow\mathbf C\), write
\(D_v=H^1_{\mathrm{dR}}(A/k)\otimes_{k,v}\mathbf C\) and similarly
\(D_w\). If \(w=\sigma v\), coefficient transport
\[
\beta_\sigma:D_v\longrightarrow D_w,\quad x\otimes z\longmapsto
x\otimes\sigma z
\]
is \(\sigma\)-semilinear and takes \(F_v\) to \(F_w\).
Composing with comparison gives the semilinear map
\(c_w^{-1}\beta_\sigma c_v\) between Betti realizations. It does
not supply a complex-linear stabilizer element for one fixed flag.

This is not merely an absent proof: a natural linear two-lattice
formulation has explicit counterexamples. Take
\(k=\overline{\mathbf Q(t)}\), and choose algebraically independent
\(u,v\in\mathbf C\) over \(\overline{\mathbf Q}\). Extend
\(t\mapsto u\) and \(t\mapsto v\) to embeddings of \(k\).
Let
\[
E_t:y^2=x(x-1)(x-t),\qquad
E_*:y^2=x^3-x+1,\qquad A=E_t\times E_*.
\]
The Legendre formula
\(j(E_t)=256(1-t+t^2)^3/[t^2(1-t)^2]\) shows that
\(j(E_u),j(E_v)\) are algebraically independent: each of \(u,v\)
is algebraic over its own \(j\)-value. They are not isogenous.
Indeed every finite subgroup of \(E_u\) is defined over the
algebraic closure of \(\mathbf Q(u)\), so every elliptic quotient
is also defined there and has \(j\) algebraic over
\(\mathbf Q(u)\); the algebraic independence excludes \(E_v\).
The varying factors have no CM because their \(j\)-values are
transcendental. The fixed curve has
\(j(E_*)=-6912/23\), a nonintegral rational number, whereas CM
\(j\)-values are algebraic integers; it too has no CM. Neither
varying factor is isogenous to the fixed curve, by the same finite
kernel argument. Hence this is a product of precisely the type
specified in H5.

Choose algebraic de Rham bases adapted to the filtrations; in those
coordinate spaces both filtrations are the standard pair of lines.
Suppose a complex-linear element of \(G\) carried the two Betti
lattices commensurably and preserved those lines. Conjugating it by
the two comparison maps would give a rational Hodge isomorphism
between the Betti realizations, compatible with the two algebraic
factor projectors. Its first component would be a rational Hodge
isomorphism \(H^1(E_u,\mathbf Q)\simeq H^1(E_v,\mathbf Q)\), and
hence an isogeny. For completeness, the last implication is
elementary: dualize to homology, identify the curves with
\(\mathbf C/\Lambda\) and \(\mathbf C/\Lambda'\); preservation
of the Hodge line makes the real-linear extension complex-linear,
and clearing denominators gives a complex-linear map carrying
\(\Lambda\) into \(\Lambda'\). It induces a nonzero isogeny,
contradiction.

Thus no filtration-preserving linear comparison carries these
lattices commensurably. H5's asserted automatic passage to a
parabolic is false for that explicit two-embedding meaning. A
different definition of \(K\) could encode a different comparison,
but it must be supplied and mapped to the flag fibre before the
dimension-five computation can apply. Equality “for generic data”
also lacks a parameter space and a specified field in the lead;
the missing original definition remains a gate rather than a
numerical theorem.

## LAT-8. The cocycle, its descent, and change of place

**Status: Proved for the specified rational tensor torsor.** Let
\(\mathcal T/\mathbf Q\) be neutral with a tensor generator,
\(D:\mathcal T\to\operatorname{Vec}_F\) the de Rham functor,
and \(B_v:\mathcal T\to\operatorname{Vec}_{\mathbf Q}\) Betti.
Set
\[
G_D=\operatorname{Aut}^{\otimes}(D),\qquad
P_v=\operatorname{Isom}^{\otimes}(D,B_v\otimes F),
\]
with right action on the source, and let \(p_v\in P_v(\mathbf C)\)
be comparison. Deligne–Milne, Theorem 3.2, supplies this affine
\(G_D\)-torsor over \(F\); finite type follows from the tensor
generator. Define
\[
\varphi_v(\sigma)=(\sigma p_v)^{-1}p_v,\qquad
\psi_v(\sigma)=p_v^{-1}\sigma p_v.
\]
Direct multiplication gives
\[
\varphi_v(\tau\sigma)=\tau(\varphi_v(\sigma))\varphi_v(\tau),
\qquad
\psi_v(\tau\sigma)=\psi_v(\tau)\tau(\psi_v(\sigma)).
\]
These are the two conventions on 18:57. The map
\(\sigma\mapsto(\psi_v(\sigma),\sigma)\) is a homomorphism into
\(G_D(\mathbf C)\rtimes\operatorname{Aut}(\mathbf C/F)\) with
\((a,\tau)(b,\sigma)=(a\tau(b),\tau\sigma)\). GEN-4 gives an
explicit \(\mathbf G_m\) calculation proving that its projection
to the first factor need not be an ordinary homomorphism.

The fpqc descent datum can be written without relying on an
unjustified automorphism-descent assertion for a transcendental
extension. Over \(R=\mathbf C\otimes_F\mathbf C\), let \(p_1,p_2\)
be the two pullbacks of \(p_v\), and put
\(z_{12}=p_1^{-1}p_2\in G_D(R)\). On the triple tensor product,
\[
z_{12}z_{23}=z_{13}.
\]
The trivializations \(h\mapsto p_i h\) of \(P_{v,R}\) differ by
left multiplication by \(z_{12}\). Evaluating
\(a\otimes b\mapsto a\sigma(b)\) yields
\(z_{12}\mapsto p_v^{-1}\sigma p_v=\psi_v(\sigma)\).
Thus the written cocycle is the automorphism restriction of the
actual tensor-product descent datum of the already constructed
isomorphism torsor. This verifies the “À vérifier / OK” identification
on 18:59 in the stated category and comparison direction.

Choose a closed point \(p_0\in P_v(F')\) over a finite extension
\(F'/F\). Writing \(p_v=p_0g\), for automorphisms fixing \(F'\)
one obtains the corrected coboundary
\[
\varphi_v(\sigma)=(\sigma g)^{-1}g.
\]
Existence of \(p_0\) follows from finite type and the existence of
the complex point; this finite extension is for trivialization,
not an unnoticed alteration of the base in a genericity claim.

For change of place, assume a rational tensor isomorphism
\(a:B_v\xrightarrow{\sim}B_w\) has been specified. Define the
complex-linear de Rham comparison
\[
g=p_w^{-1}a p_v.
\]
It carries the associated Betti rational structures to each other;
it carries the integral lattices exactly when \(a\) is integral on
them. Since \(a\) is rational, \(\sigma a=a\), and
\[
\begin{aligned}
\sigma(g)\varphi_v(\sigma)g^{-1}
&=(\sigma p_w)^{-1}a(\sigma p_v)
 (\sigma p_v)^{-1}p_v p_v^{-1}a^{-1}p_w\\
&=(\sigma p_w)^{-1}p_w
=\varphi_w(\sigma).
\end{aligned}
\tag{LAT-8.1}
\]
This proves the boxed 18:62 formula. At a finite place the action
on a frame is conjugation by \(\rho_\ell(\sigma)\), so its formula
reduces to
\(\rho_\ell g_\ell\rho_\ell^{-1}\rho_\ell g_\ell^{-1}
=\rho_\ell\), exactly as written. The premise that the requisite
integral tensor isomorphism exists is addressed next.

## LAT-9. A CM counterexample to the integral comparison on 18:55

**Status: Proved.** Put \(K=\mathbf Q(\sqrt{-5})\),
\(\mathcal O=\mathbf Z[\sqrt{-5}]\), and
\(I=(2,1+\sqrt{-5})\). This is an invertible ideal of norm two
which is not principal. If it were \((a+b\sqrt{-5})\), its norm
would give \(a^2+5b^2=2\), which has no integer solution.

The elliptic curves \(\mathbf C/\mathcal O\) and
\(\mathbf C/I\), with their indicated \(\mathcal O\)-actions,
have algebraic models. CM reciprocity produces an automorphism of
\(\mathbf C\) fixing \(K\) that carries the first CM curve to
the second, compatibly with the labelled \(K\)-action. Precisely,
Milne's *The Fundamental Theorem of Complex Multiplication* (2007),
Theorem 3.13, describes the transported lattice as multiplication
by the finite idele representing the ideal class; for an imaginary
quadratic field the reflex field is \(K\) and the reflex norm is
the identity. Choose an idele in the class of \(I\), and extend
its Artin automorphism to \(\mathbf C\). The inverse-ideal
convention is immaterial here: \(I^2=(2)\), so the two ideal
classes agree. The relation \(I^2=(2)\) follows either by multiplying
the generators or by inclusion and the equal norm four.

For the two places thus obtained, covariant integral Betti
homology of the same algebraic CM motive has \(\mathcal O\)-module
structures isomorphic to \(\mathcal O\) and \(I\). A natural
integral comparison commuting with the endomorphisms would be an
\(\mathcal O\)-linear isomorphism between these modules. The image
of \(1\) would generate \(I\), contradiction. The same obstruction
holds in cohomology: taking \(\mathbf Z\)-duals replaces the ideal
class by its inverse, which is again the same nontrivial class.

The exact rational comparison exists because
\(\mathcal O\otimes\mathbf Q=I\otimes\mathbf Q=K\); multiplication
by any nonzero element of \(K\) identifies these one-dimensional
\(K\)-spaces. Every local completion of \(I\) is principal, so
the local integral modules are isomorphic. Those exact maps explain
why the rational and local assertions do not supply the integral
isomorphism asserted on 18:55. This is an obstruction already on
the object and its integral endomorphisms, hence on any integral
tensor comparison of a category containing them.

This example changes the algebraic field of definition under the
two embeddings. The separate same-algebraic-part Legendre example
being developed in Part E strengthens the obstruction there; it
is not required for the unrestricted two-place claim on 18:55.

## LAT-10. Euclidean closure, the openness expectation, and a Tate counterexample

**Status: Proved; the universal 18:61 expectation is false.** First
record the exact topological version of GEN-2. If \(F\subset\mathbf C\)
is countable, \(X/F\) is affine of finite type, and
\(Z=\overline{\{p\}}^{F\text{-Zar}}\), then
\[
\overline{\operatorname{Aut}(\mathbf C/F)\cdot p}^{\mathrm{Eucl}}
=Z_{\mathbf C}(\mathbf C).
\tag{LAT-10.1}
\]
Indeed the orbit is exactly the set of \(F\)-generic points of
\(Z\): their coordinate fields are isomorphic over \(F\), and
the isomorphism extends to \(\mathbf C\) by algebraic closures
and transcendence bases. There are countably many proper
\(F\)-subvarieties. Each has empty interior in every geometric
irreducible component of \(Z_{\mathbf C}\); containing one
component would, by conjugacy, force containment of all and hence
of \(Z\). Their complement is dense in the complex topology by
Baire, on the smooth loci and then on the whole variety. This
proves (LAT-10.1), including the case of several geometric
components.

Applying the complex algebraic isomorphism
\(D_p:x\mapsto x^{-1}p\) to (LAT-10.1) gives
\[
\overline{\operatorname{im}\varphi_p}^{\mathrm{Eucl}}
=D_p(Z_{\mathbf C})(\mathbf C),
\tag{LAT-10.2}
\]
the same algebraic locus as in GEN-2.

For a number-field motive, the finite-part representation factors
through the algebraic Galois group, so
\(\operatorname{Aut}(\mathbf C/\overline{\mathbf Q})\) acts
trivially on it. When the comparison point is generic over
\(\overline{\mathbf Q}\), each fibre over an attained finite
Galois value has dense complex image: compose one lift of that
value with automorphisms fixing \(\overline{\mathbf Q}\), and
apply (LAT-10.1) to the resulting generic point. This argument
uses an orbit description, not continuity of field automorphisms
in the usual complex topology. If \(\Gamma_f\) is the compact
finite image, the total closure is exactly
\[
\Gamma_f\times G(\mathbf C).
\tag{LAT-10.3}
\]

Take now \(M=\mathbf Q(-2)\) over \(\mathbf Q\). The comparison
period is \((2\pi i)^2\), which is transcendental. Thus its
\(\mathbf G_m\)-torsor point is generic. By LAT-6 the finite
image is \(H=(\widehat{\mathbf Z}^\times)^2\), closed of
infinite index. Formula (LAT-10.3) proves that the closure of
the actual total image is
\[
H\times\mathbf C^\times
\subset\widehat{\mathbf Z}^\times\times\mathbf C^\times.
\tag{LAT-10.4}
\]
It is a subgroup, but it is not open. This is a genuine motivic
counterexample to the universal “sous-groupe ouvert” expectation,
with connected group, minimum field of definition \(\mathbf Q\),
and \(\pi\) transcendental over that field. No period conjecture
is needed. The isogeny \(t\mapsto t^2\) again identifies the
precise obstruction.

For the specifically non-CM elliptic \(h^1(E)\) over a number
field, the finite image is already open by Serre. Here the
open-subgroup closure assertion is equivalent to full period
genericity, by the following exact argument. If that closure is
an open subgroup of the finite compact factor times
\(\operatorname{GL}_2(\mathbf C)\), its projection onto the
complex factor is an open subgroup. The projection is also
closed, because projection along a compact factor is closed.
The complex group is connected, so that projection is the whole
group. Equation (LAT-10.2) then forces the period locus to be
the full torsor. Conversely full genericity gives
(LAT-10.3), and Serre makes it open. Thus an unconditional
affirmative answer for this particular motive would settle the
non-CM elliptic period conjecture excluded in A.4(a). The
general expectation has the explicit counterexample (LAT-10.4);
the non-CM elliptic specialization remains this named unresolved
gate.

## LAT-11. The unfinished qualification involving pi

**Status: exact necessity proved; sufficiency refuted.** Whenever the
category contains \(\mathbf Q(-m)\), \(m\ne0\), restriction of
tensor isomorphisms gives a surjective morphism from the period
torsor to its Tate comparison torsor. The comparison coordinate
there is \((2\pi i)^m\). A generic point maps to a generic point
under this dominant morphism. Consequently genericity of the
full comparison point implies that \(\pi\) is transcendental
over the algebraic extension \(F(i)\), and hence over \(F\).
This is the exact Tate quotient underlying the margin on 18:59.

Minimum transcendence degree of a field of definition does not
itself force this condition. For example use the explicit
\(j\)-model of GEN-5 with \(j=\pi\), over \(F=\mathbf Q(\pi)\).
It cannot be defined up to isogeny over a number field, since
\(j\) is transcendental. Its determinant period is algebraic
over \(F(i)\), so its comparison point is not generic there.

The condition is not sufficient either. GEN-5 gives an actual
CM comparison over \(F=K_1(a+a^{-1})\) for which \(\pi\) remains
transcendental, while one CM period coordinate is quadratic over
\(F\). The exact period locus has transcendence degree one
over \(F\), instead of the CM torsor's dimension two. Adding
the non-CM factor with \(j=a+a^{-1}\) makes the given field
minimum in the degree-one category and keeps the obstruction.
The finite two-value character of its actual cocycle also
prevents its complex closure from being open, irrespective of
the finite-part image. Thus the written qualification is a
necessary Tate-factor check, not a complete repair for arbitrary
transcendental fields of definition.

## LAT-12. Scope of the remaining place-recovery question

The frozen alternatives `est|pas` on 18:51 require the full category,
the equivalence relation on places, and whether the integral lattice
is included. The fixed-object genericity and commensurability
statements proved above do not decide a recovery theorem for the
entire variable-object category. The exact naturality obstruction
in LAT-9 already rules out unrestricted integral isomorphism of
all two-place functors. Part E is the parent task's location for
the same-algebraic-part construction and for the positive and
negative recovery readings. No claim of a complete general
classification is made here.

## Source access, theorem locators, and check events

| Source | Exact use and access |
|---|---|
| Supplied 18:42,43,45,47,49,51,53,55,57,59,61,62 transcriptions | Read in full; `K` definition not found; doubtful glyphs retained; LAT-1,2,7,8,10 |
| SGA4, Tome 3, Exposé XVI, Théorème 4.1 | Laszlo retypeset primary text, PDF p.156, printed p.149, original margin p.233; finite-coefficient Betti–étale comparison; primary locator verified by triangle subtask |
| Serre 1972 | Original official PDF downloaded; p.299 Théorème 3 and p.324 Théorème 6 visually read in rendered images; no translation numbering substituted |
| Faltings 1983 | Opened §5, Satz 4 p.360, Korollar 1 and 2 p.361; representation-isogeny implication |
| Lombardo, *An explicit open image theorem for products of elliptic curves* | Author PDF opened, Theorem 1.1 and Remark 1.2, PDF p.1; all-prime group (LAT-4.1) |
| Kneser 1965 | Complete original journal volume downloaded; article pp.190–203; pp.190–194 visually read, especially Satz 1 and Hilfssätze 2.3–2.5 |
| Platonov 1969 and 1970 addendum | English primary journal versions opened; Theorem A p.1140; addendum §2 corrects type-A part, §5 corrects exceptional part |
| Deligne–Milne, *Tannakian Categories* | Corrected 2012 primary version, original numbering; Prop.2.21, Thm3.2, Thm6.20, Prop6.21; exact torsor/descent and degree-one scope |
| Milne, *The Fundamental Theorem of Complex Multiplication* (2007) | Proof article opened, Theorems 3.2,3.10,3.13; exact idele-to-lattice conjugation in LAT-9 |
| Rapinchuk 2013 survey | Used only to locate primary Kneser/Platonov references; not the proof authority for the criterion |
| Pete Clark English translation of Serre | Read for navigation; numbering differs from original; original images control final references |

Primary URLs and web reference IDs for parent reopening:

- SGA4: https://www.math.polytechnique.fr/~laszlo/sga4/SGA4-3/sga43.pdf ;
  triangle ref `turn109184195view2`.
- Serre: https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf ;
  `turn442298666search6`; local original `sources_generation/serre1972.pdf`;
  images `serre1972-p42.png` (p.299), `serre1972-p67.png` (p.324).
- Faltings: https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf ;
  `turn875980263view0`, `turn700267791view1`.
- Lombardo: https://people.dm.unipi.it/lombardo/files/ProductsEC.pdf ;
  `turn493653534view0`.
- Kneser: https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0218/PPN243919689_0218.pdf ;
  `turn524023182search26`; web PDF timed out, direct download succeeded;
  images `kneser-vol-p195.png`–`kneser-vol-p199.png` correspond to article
  pp.190–194.
- Platonov: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2220&what=fullteng ;
  `turn816765066view0`.
- Addendum: https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2446&what=fullteng ;
  `turn875980263view2`, `turn700267791view0`.
- Deligne–Milne: https://www.jmilne.org/math/xnotes/tc.pdf ;
  `turn493653534view1`, `turn725178137view0`, `turn229772981view1`.
- Milne CM proof: https://www.jmilne.org/math/articles/2007c.pdf ;
  `turn191219646view0`, `turn858004232view0`, `turn858004232view1`.

The exact algebra checks in `code_generation/check_lattices.py` and
`check_lattices.out` verify the chosen \(j\)-model, the period-coordinate
involution, the norm-two ideal obstruction, finite square-index
quotients, and the group dimensions. They do not purport to test
transcendence numerically.

| Claim/check | Date | Checker | Kind | Outcome |
|---|---|---|---|---|
| LAT-1 product and restricted topology | 2026-11-19 | GPT-6 Astra | direct proof and explicit tuple | Distinct ring maps/topologies verified; compact-open issue exposed |
| LAT-2 quotient | 2026-11-19 | GPT-6 Astra | explicit inverse fpqc maps | Dimension bound proved with componentwise invariant specified |
| LAT-3 genericity lemma | 2026-11-19 | GPT-6 Astra | independent proof | Countable Haar-null union; product version proves joint genericity |
| LAT-4 Serre hypotheses | 2026-11-19 | GPT-6 Astra | original image check | Theorem3 p299; Theorem6 p324 needs representation non-isomorphism, supplied by Faltings |
| LAT-5 approximation | 2026-11-19 | GPT-6 Astra | primary source + explicit matrices | Full connected-affine criterion; determinant counterexample |
| LAT-6 margin reverse implication | 2026-11-19 | GPT-6 Astra | Baire proof and counterexamples | All-frame commensurability iff openness; genericity converse fails in formal groups |
| LAT-7 K/H5 | 2026-11-19 | GPT-6 Astra | text search and elliptic construction | K still undefined; automatic parabolic argument refuted |
| LAT-8 descent/change formula | 2026-11-19 | GPT-6 Astra | tensor-product descent datum | Exact torsor identification and boxed formula proved |
| LAT-9 integral CM comparison | 2026-11-19 | GPT-6 Astra | reciprocity + ideal norm check | Integral assertion false; rational and local maps stated |
| LAT-10 open closure | 2026-11-19 | GPT-6 Astra | Tate-square counterexample | Universal expectation false even over Q |
| LAT-11 pi qualification | 2026-11-19 | GPT-6 Astra | dominant Tate quotient + GEN-5 | Necessary, insufficient; minimum field condition does not repair it |

**Exact unresolved gates carried to the parent report:** the meaning and
generators of 18:45 `K`; arbitrary prescribed-place equality in LAT-2;
the intended definition of “indépendance” in the 18:51 margin; the
non-CM elliptic specialization of the 18:61 openness assertion; and
the general variable-motive place-recovery theorem beyond the cases
handled in Part E. The universal openness assertion itself is
resolved negatively by the Tate-square example.
