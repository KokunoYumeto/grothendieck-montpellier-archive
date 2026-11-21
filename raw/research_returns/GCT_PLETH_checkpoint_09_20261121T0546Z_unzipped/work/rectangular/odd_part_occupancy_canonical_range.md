# Odd-part occupancy and an actual canonical-map bound

## R-049. A refined bound for every tail

Let \(a,n\ge2\), let \(\nu\) be a nonempty partition of
size \(D\) and width \(t=\nu_1\ge2\), and require
\(\lambda=(an-D,\nu)\) to be a partition.
Let \(o\) be the number of odd parts of \(\nu\), counted
with multiplicity, and put
\[
\epsilon=t\bmod2,\qquad
q=\left\lceil\frac{o-\epsilon}{3}\right\rceil,\qquad
M(\nu)=\left\lfloor\frac{D+t-q}{2}\right\rfloor.
\tag{OO.1}
\]
Then \(q\ge0\), \(M(\nu)\ge t\), and for every \(n\ge M(\nu)\)
the actual normalized map
\[
h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^aV)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^nV)
\]
is surjective on its entire \(\lambda\)-isotypic component:
\[
\boxed{\operatorname{mult}_\lambda\operatorname{im}h_{n,a}
       =a_{a,n}^{\lambda}.}
\tag{OO.2}
\]
The assertion holds over every characteristic-zero field
and in all finite dimensions. The component is zero below
dimension \(\ell(\lambda)\).

For \(a,n\ge M(\nu)\), the actual map is an isomorphism on
this component, with the formal centered-moment multiplicity
(TM.5). The explicit proof below supplies every restriction
and polarization morphism. It includes R-048's one-row
ranges and produces improvements of arbitrarily many rows
on the positive family in §5.
The starting numerical bound in R-046 is explicitly attributed
there to Sarkar Theorem 6.4; no historical priority claim
is made here.

## 1. The actual centered and uncentered restriction maps

For \(S\ge s\ge1\), set
\[
E_S=\mathbb Q^S,\quad
\bar e_S=S^{-1}\sum_{i=1}^S e_i,\quad
W_S=\mathbf1^\perp,\quad P_Se_i=e_i-\bar e_S,
\]
and analogously at \(s\). Define the following linear map:
\[
\widetilde q:E_S\longrightarrow E_s,\qquad
\widetilde q(e_i)=
 \begin{cases}e_i,&i\le s,\\ \bar e_s,&i>s.\end{cases}
\tag{OO.3}
\]
It satisfies, by direct summation,
\[
\widetilde q(\bar e_S)=\bar e_s,\qquad
\widetilde q(P_Se_i)=
 \begin{cases}P_se_i,&i\le s,\\0,&i>s.\end{cases}
\tag{OO.4}
\]
Thus its restriction to \(W_S\) is exactly the orthogonal
transpose \(q:W_S\to W_s\) of zero-padding used in TM.12.
The map (OO.3) is equivariant for \(S_s\) acting on the first
\(s\) rows, and therefore sends \(S_S\)-invariants to
\(S_s\)-invariants after taking exterior powers.

Fix \(T=\mathbb Q^t\), and write
\[
C_s=(\Lambda(E_s\otimes T))^{S_s},\qquad
B_s=(\Lambda(W_s\otimes T))^{S_s}.
\]
The specified vector \(\bar e_s\) identifies the literal
trivial-line factor with \(T\), giving
\[
C_s=\Lambda T\otimes B_s.
\tag{OO.5}
\]
Under these actual decompositions, (OO.3) induces precisely
\[
\Lambda(\widetilde q\otimes1)|_{C_S}
 =1_{\Lambda T}\otimes
          \bigl(\Lambda(q\otimes1)|_{B_S}\bigr).
\tag{OO.6}
\]
In particular this statement uses the displayed averaged
extra-row images, not coordinate deletion.

The centered map in (OO.6) sends every row power sum to
its counterpart with scalar one, by (OO.4).
The finite signed row-orbit spanning proof TM.8/TM.12
therefore makes it surjective, and so the uncentered map
is surjective as well. There is the actual graded
\(GL(T)\)-equivariant injection
\[
\ker(B_S\to B_s)_D
 \hookrightarrow \ker(C_S\to C_s)_D,\qquad v\longmapsto1\otimes v.
\tag{OO.7}
\]

The row-orbit decomposition of \(C_s\) is
\[
C_s=
\bigoplus_{\substack{e_0+\cdots+e_t=s\\e_i\ge0}}
 \bigotimes_{i\ {\rm even},\,i\ge2}
       \operatorname{Sym}^{e_i}(\Lambda^iT)
 \ \otimes\
 \bigotimes_{i\ {\rm odd}}
       \Lambda^{e_i}(\Lambda^iT).
\tag{OO.8}
\]
It comes from ordered-row exterior multiplication and
rational symmetrization with the literal Koszul signs;
the \(e_0\) unit factor is one-dimensional.
For a fixed tuple of nonempty row counts, the same module
occurs at every \(s\ge k=\sum_{i\ge1}e_i\).
It follows that the character difference
\([C_S]-[C_s]\) is exactly the sum of the row-orbit module
characters with \(s<k\le S\).
Surjectivity of (OO.6) makes this the character of its kernel.
We use this equality of characters; those omitted row-orbit
modules are not asserted to be literal kernel summands
for the particular map (OO.3).

## 2. The alternating highest-weight bound for each occupied tuple

For a rational \(GL(T)\) highest weight
\(\alpha=(\alpha_1,\ldots,\alpha_t)\), define
\[
A(\alpha)=\alpha_1-\alpha_2+\alpha_3-\cdots
                         +(-1)^{t-1}\alpha_t .
\tag{OO.9}
\]
The paired-row decomposition OI.8, proved there by explicit
upper-unipotent Pfaffian elimination, says that every
constituent of \(\operatorname{Sym}^{e_2}(\Lambda^2T)\)
has \(A(\alpha)=0\).
Tensoring with \(\det T\) adds \(\epsilon\) to this number.

Consider one nonzero summand of (OO.8), of scalar degree
\(D\), with \(k\) occupied rows. Its singleton factor is
\(\Lambda^{e_1}T\), with \(e_1\le t\). Put \(u=t-e_1\).
The perfect exterior pairing gives the actual isomorphism
\[
\Lambda^{e_1}T=\det T\otimes\Lambda^uT^*.
\tag{OO.10}
\]
Every other factor at \(i\ge3\), whether symmetric or
exterior, injects into
\((\Lambda^iT)^{\otimes e_i}\) by its normalized averaging
or signed averaging projector. Thus each constituent of
the row-orbit module occurs in
\[
\det T\otimes\Lambda^uT^*\otimes
 \operatorname{Sym}^{e_2}(\Lambda^2T)
 \otimes\bigotimes_{i\ge3}(\Lambda^iT)^{\otimes e_i}.
\tag{OO.11}
\]
All these are explicit tensor maps.

The exterior Pieri maps add a vertical \(i\)-strip;
their dual maps remove a vertical \(u\)-strip.
They are the column insertion or contraction maps followed
by the rational Young projectors. The dual version also
follows immediately from (OO.10) and the usual exterior
Pieri map, with its determinant twist retained.
Each added or removed box changes (OO.9) by \(1\) or \(-1\).
Starting from a paired constituent in (OO.11), every possible
final highest weight \(\gamma\) therefore satisfies
\[
A(\gamma)\le
 \epsilon+u+\sum_{i\ge3}i e_i.
\tag{OO.12}
\]
This argument applies as written to the intermediate
rational highest weights as well; their individual last
entries need not be nonnegative.

The exact degree and occupancy identities are
\[
D=e_1+2e_2+\sum_{i\ge3}i e_i,\qquad
k=e_1+e_2+\sum_{i\ge3}e_i,
\]
hence
\[
D+t-2k=u+\sum_{i\ge3}(i-2)e_i.
\tag{OO.13}
\]
For every \(i\ge3\), \(i\le3(i-2)\), and \(u\le3u\).
Equations (OO.12)–(OO.13) imply
\[
\boxed{A(\gamma)\le\epsilon+3(D+t-2k).}
\tag{OO.14}
\]

For \(\gamma=\nu^t\), the alternating sum \(A(\gamma)\)
is exactly \(o\): a row of \(\nu\) of length \(j\)
contributes \(1-1+\cdots+(-1)^{j-1}\), equal to one
at odd \(j\) and zero at even \(j\).
Thus every row-orbit module containing \(S_{\nu^t}T\)
has
\[
D+t-2k\ge
 \left\lceil\frac{o-\epsilon}{3}\right\rceil=q,
\qquad
k\le M(\nu).
\tag{OO.15}
\]
This is the asserted occupied-row bound.

Finally \(o\ge\epsilon\), since the largest part supplies
an odd part when \(t\) is odd.
After removing one largest part, the remaining degree
\(D-t\) bounds the number \(o-\epsilon\) of remaining
odd parts. Therefore
\[
0\le q\le o-\epsilon\le D-t,\qquad
M(\nu)\ge t.
\tag{OO.16}
\]
This includes \(q=0\) and all small parameter endpoints.

## 3. Faithful centered evaluation at the refined row count

For \(S\ge s\ge M(\nu)\), (OO.15) says that no omitted
row-orbit term in the character difference \(C_S-C_s\)
contains \(S_{\nu^t}T\) in degree \(D\).
The kernel character in §1 has zero multiplicity there.
The actual injection (OO.7) gives the same vanishing for
the centered kernel.

Skew Cauchy identifies that multiplicity map with
\[
S_\nu(q):(S_\nu W_S)^{S_S}
          \longrightarrow(S_\nu W_s)^{S_s}.
\tag{OO.17}
\]
It is therefore an isomorphism.
In the ordinary Cauchy decomposition the map is again
the identical Schur map \(S_\nu(q)\), because the tensor
Young projectors commute with every tensor power of \(q\).

Take \(S\ge\max(s,D)\). The centered power-sum evaluation
\(p_S\) of TM.6 is an isomorphism through degree \(D\),
by the full equality-partition triangular-basis proof.
Its generator identity with \(q\) is scalar one.
Consequently
\[
\boxed{p_s\text{ is an isomorphism on the }S_\nu
       \text{ component for every }s\ge M(\nu).}
\tag{OO.18}
\]
No dimension comparison is used without the specified
surjection and its kernel.

## 4. The actual canonical map

For \(n\ge M(\nu)\ge t\), every \(S_\nu W_a\) invariant
extends to its homogeneous highest polynomial by TM.4.
The separate row-degree bound \(t\) follows from the
column antisymmetrizer, exactly as in TM.4/OI.15.

The normalized opposite canonical map is the literal
composition
\[
h_{a,n}|_\nu=p_n\Psi_nE_a.
\tag{OO.19}
\]
The independent-row polarization \(E_a\) is injective,
including after \(L(1)=1\) and mean-zero restriction,
by TM.14.
The split-moment substitution \(\Psi_n\) is the complete
set-partition expression TM.16/OI.17. Its degree-\(d\)
leading coefficient is
\((-1)^{d-1}(d-1)!/(n)_d\), nonzero for \(2\le d\le t\),
and its other terms use lower-degree generators.
It is the explicit triangular automorphism proved in
TM.17. The final factor is injective on the precise
component by (OO.18).
Thus the composition is injective on the entire
highest multiplicity space, with no scalar omitted.
The scalar-one transpose identity SR.5–SR.6 proves
(OO.2). Applying it in both directions gives the
two-sided isomorphism range stated at the beginning.

## 5. Positive hook families with unbounded row improvement

Let
\[
r\ge1,\quad a\ge r+2,\quad u,v\ge0,\quad
t_0=\frac{r^2+3r+4}{2},\quad t=t_0+2u+3v.
\tag{OO.20}
\]
For every
\[
n\ge t+\left\lfloor
                \frac{r-\lceil r/3\rceil}{2}\right\rfloor
\]
the actual map reaches the complete target component
\[
\boxed{\lambda=(an-t-r,t,1^r),\qquad
 \operatorname{mult}_\lambda\operatorname{im}h_{n,a}
 =a_{a,n}^{\lambda}\ge1.}
\tag{OO.21}
\]
These statements hold in every dimension at least \(r+2\).
The partition is automatic:
\(n\ge t\), \(a\ge r+2\), and
\(an-t-r\ge(r+1)t-r\ge t\).

Here is the actual invariant tensor proving positivity.
On \(E=W_a\), with coordinates \(x_i\) satisfying
\(\sum_i x_i=0\), put
\[
p_d(x)=\sum_{i=1}^a x_i^d,\qquad
\Omega_r=\iota_x(dp_2\wedge dp_3\wedge\cdots\wedge dp_{r+2}).
\tag{OO.22}
\]
The symbol \(\iota_x\) is contraction with the Euler
vector \(x\). This polynomial \(r\)-form is invariant
under \(S_a\), has coefficient degree \(t_0\), and
satisfies \(\iota_x\Omega_r=0\).

To identify its exact Schur module, exterior Pieri gives
\[
\operatorname{Sym}^{t_0}E^*\otimes\Lambda^rE^*
=S_{(t_0+1,1^{r-1})}E^*
 \oplus S_{(t_0,1^r)}E^*.
\]
Contraction \(\iota_x\) maps the first summand nontrivially
to the equal Schur summand in
\(\operatorname{Sym}^{t_0+1}E^*\otimes\Lambda^{r-1}E^*\):
on its highest polynomial
\(x_1^{t_0}dx_1\wedge\cdots\wedge dx_r\), the
\(x_1^{t_0+1}dx_2\wedge\cdots\wedge dx_r\) term is nonzero.
The second Schur summand is absent from that codomain,
so contraction kills it.
Complete reducibility and the displayed multiplicity-one
Pieri maps show
\[
\ker\iota_x=S_{(t_0,1^r)}E^*.
\tag{OO.23}
\]
The rational invariant dot form identifies \(E^*\) with
\(E\) as an \(S_a\)-module.

For an explicit nonzero evaluation take \(a_0=r+2\),
\(x_i=i-(a_0+1)/2\) on the first \(a_0\) rows and
zero thereafter. Let \(b_j=e_j-e_{a_0}\).
The value on \(b_2,\ldots,b_{a_0-1}\) is
\[
\begin{aligned}
\Omega_r(x)(b_2,\ldots,b_{a_0-1})
 &=x_1\det\bigl[d(x_j^{d-1}-x_{a_0}^{d-1})\bigr]_{
                   2\le d\le a_0,\ 1\le j<a_0}\\
 &=(-1)^{a_0}\frac{a_0-1}{2}\,a_0!\!
                   \prod_{1\le i<j\le a_0}(x_j-x_i)\ne0.
\end{aligned}
\tag{OO.24}
\]
To check the second equality, factor \(x_j-x_{a_0}\)
from each column; the remaining row polynomials are monic
of degrees zero through \(a_0-2\), so their determinant
is the Vandermonde on \(x_1,\ldots,x_{a_0-1}\).
The remaining factors give the displayed sign and \(a_0!\).
All \(x_j-x_i=j-i\) are nonzero. This calculation also
proves nonvanishing after adding zero rows.

Multiply (OO.22) by \(p_2^u p_3^v\).
Both scalar polynomials are nonzero on \(E\) for \(a\ge3\),
and the polynomial form module is free over its integral
domain of coefficients. The product is therefore nonzero,
still horizontal, with coefficient degree \(t\).
The same exact contraction argument gives
\(S_{(t,1^r)}E^*\). Evaluating the form on \(r\)
auxiliary centered columns realizes its highest polynomial:
raising a later column into the first inserts \(x\)
and gives zero; raising between the later columns repeats
an exterior argument and gives zero.
This specifies the actual highest-vector map.

Its separate row degrees are at most \(t\) by the Young
column bound. Homogenization TM.4 supplies a nonzero
target highest vector in every asserted inner degree.
For \(\nu=(t,1^r)\), its odd-part count is
\(o=r+(t\bmod2)\), so \(q=\lceil r/3\rceil\).
Formula (OO.1) is exactly the bound in (OO.21).

In particular, choose any \(s\ge0\) and set
\[
r=6s+2,\qquad
t=18s^2+21s+7+2u+3v,\qquad
a\ge6s+4,\qquad n\ge t+2s .
\tag{OO.25}
\]
Then (OO.21) is a positive full-image family.
The previous uniform threshold for its tail is
\(t+3s+1\); the displayed actual-map proof reaches
\(s+1\) additional rows below that value.
For example \(s=1,u=v=0,a=10,n=48\) gives the literal
positive component \((426,46,1^8)\).

## 6. Transport and independent finite checks

All maps above are rational. The two mean vectors in
(OO.3), the exact exterior duality, Young projectors,
invariant averages and triangular moment inverses have
nonzero denominators in the displayed ranges.
Naturality extends the result to each supporting finite
rank and every characteristic-zero field.

The exact geometric map is the Chow pullback R-037
EP.3–EP.5, with scalar-one degree piece EP.4.
The frame-torsor and representation-\(K_0\) transport
is the fixed dictionary R-036 §5:
SGA 6 VI Theorem 3.3; SGA 6 V Proposition 4.2,
Definition 4.4, Proposition 4.8 and Corollary 4.9;
SGA 3 I §4.5 and Propositions 4.7.2–4.7.3;
EGA II 2.4.1–2.4.2 and 2.5.2/2.5.4.

The independent script verify_odd_part_occupancy_stability.py
compares the literal standard-representation Schur average
at \(M(\nu)\) with the separately expanded formal moment
character for every tail of degree two through fourteen
and width at least two.
All **493** comparisons pass; **248** use an improved
row count, and **58** of those have positive multiplicity.
The exact receipt is ODD_PART_OCCUPANCY_STABILITY_CHECK.tsv.
These checks concern character values. The actual rank
is proved by (OO.3)–(OO.7), (OO.17) and (OO.19).

The separate script verify_odd_part_hook_form.py evaluates the
literal contracted wedge of power-sum differentials and independently
compares its determinant with (OO.24), for \(r=1,\ldots,10\)
and row counts \(a=r+2,r+4\).
All **20** exact nonzero scalars pass, including the added-zero-row
realization. The receipt is ODD_PART_HOOK_FORM_SCALAR_CHECK.tsv.

