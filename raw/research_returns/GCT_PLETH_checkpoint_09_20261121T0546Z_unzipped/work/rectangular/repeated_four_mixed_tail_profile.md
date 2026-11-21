# Repeated-four mixed tails: finite multiplicities and an actual map range

## R-047. The family \((4^h,3,2^j,1)\)

Let \(h\ge1\), \(j\ge0\), and put
\[
\nu=(4^h,3,2^j,1),\qquad
D=4h+2j+4,\qquad
K=2h+j+3,\qquad
r_s=\min\{h,\max(0,s-h-j-3)\}.
\tag{RF.1}
\]
Throughout, \(\lambda=(an-D,\nu)\) is required to be a partition.
All multiplicities below are stable Schur-functor multiplicities; in a
finite-dimensional space \(V\) they apply when
\(\dim V\ge\ell(\lambda)=h+j+3\), and the entire component is zero
in smaller dimension.

For every \(a\ge2\) and \(n\ge4\), the exact target multiplicity is
\[
\boxed{a_{a,n}^{\lambda}=r_a.}
\tag{RF.2}
\]
For the normalized canonical map
\[
h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^aV)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^nV),
\]
the exact image multiplicity throughout the explicit range
\[
a,n\ge4,\qquad \max(a,n)\ge K
\]
is
\[
\boxed{\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
       =\min(r_a,r_n).}
\tag{RF.3}
\]
In particular the entire target is reached for every \(a\ge2,n\ge K\).
At \(a\ge K,n\ge4\), the actual map is injective on this component.
The statements include their zero endpoints.

The stable multiplicity \(h\) is already the
\((m_1,m_3)=(1,1)\) case of Sarkar's four-column theorem,
Theorem 7.3 in arXiv:2610.07929v2, also Theorem E of its introduction.
The complete proof and its final table were read in the retained
primary source, work/theta/sarkar/main.tex,
https://arxiv.org/src/2610.07929v2.
No historical novelty is claimed for that stable count.
The proof below establishes the complete finite profile and the
specified actual maps. Its canonical range is one row earlier than
R-046's uniform bound \(N(\nu)=2h+j+4\) for this tail.

## 1. The exact exterior layer at the last row

Use the rational spaces and maps of R-046:
\[
E_s=\mathbb Q^s,\quad W_s=\mathbf1^\perp,\quad
P_se_i=e_i-s^{-1}\mathbf1,\quad T=\mathbb Q^4,
\]
\[
C_s=(\Lambda(E_s\otimes T))^{S_s},\qquad
B_s=(\Lambda(W_s\otimes T))^{S_s}.
\]
The ordered-row exterior product, followed by rational averaging,
gives precisely TM.8. A summand with \(e_i\) occupied rows of
exterior degree \(i\) has scalar degree \(\sum i e_i\).
The singleton factor is \(\Lambda^{e_1}T\), so \(e_1\le4\).

Set \(N=K+1=(D+4)/2\). In scalar degree \(D\), a summand
occupying exactly \(N\) nonempty rows satisfies
\[
D\ge2N-e_1\ge2N-4=D.
\tag{RF.4}
\]
Thus both inequalities are equalities:
\(e_1=4\), all remaining occupied rows have degree two, and
\(e_2=N-4=2h+j\). This is the entire difference between
the row-orbit decompositions of \(C_N\) and \(C_K\) in degree \(D\):
\[
[C_{N,D}]-[C_{K,D}]
=
[\det T\otimes\operatorname{Sym}^{\,2h+j}(\Lambda^2T)].
\tag{RF.5}
\]
The equality counts actual direct summands of TM.8; it includes
their Koszul signs. For every scalar degree \(e<D\), all summands
already occur at \(K\), because
\(\lfloor(e+4)/2\rfloor\le K\).
Hence \(C_{N,e}\) and \(C_{K,e}\) have the same character.

The literal invariant splitting
\[
C_s=\Lambda T\otimes B_s
\tag{RF.6}
\]
is induced by \(E_s=\mathbb Q\mathbf1\oplus W_s\).
Degree induction, using the constant-term identity of \(\Lambda T\),
shows first that the characters of \(B_{N,e}\) and \(B_{K,e}\)
coincide for \(e<D\), then that their degree-\(D\) difference is
exactly the right side of (RF.5).

This character calculation describes the kernel of a specified map.
Zero-padding \(W_K\hookrightarrow W_N\) has rational orthogonal
transpose \(q:W_N\to W_K\), with
\[
q(P_Ne_i)=P_Ke_i\quad(i\le K),\qquad
q(P_Ne_N)=0.
\tag{RF.7}
\]
The exterior row power-sum generators therefore map with scalar
one to the same generators at row count \(K\). The finite-row
orbit proof HO.3, or TM.12, proves that
\(\Lambda(q\otimes1):B_N\to B_K\) is onto.
It follows from complete reducibility that its degree-\(D\)
kernel has precisely the character in (RF.5).

The relevant skew-Cauchy factor is
\[
\gamma=\nu^t=(h+j+2,h+j+1,h+1,h).
\tag{RF.8}
\]
By the explicit Pfaffian/standard-monomial proof HO.5,
\[
\operatorname{Sym}^{d}(\Lambda^2T)
=\bigoplus_{\substack{P\ge Q\ge0\\P+Q=d}}
 S_{(P,P,Q,Q)}T.
\tag{RF.9}
\]
Every summand in (RF.5) therefore has its first two parts equal,
and its last two parts equal. The two respective differences
of \(\gamma\) are both one. Thus the \(S_\gamma T\)-multiplicity
of the kernel of (RF.7) is zero.

R-046 gives the stable character for every row count \(s\ge N\).
The surjections (RF.7) and their composites therefore prove
that every actual restriction
\[
S_\nu(q):(S_\nu W_S)^{S_S}\longrightarrow
                 (S_\nu W_s)^{S_s},
\qquad S\ge s\ge K,
\tag{RF.10}
\]
is an isomorphism. The ordinary and exterior multiplicity maps
are this same Schur morphism: their Young projectors commute
with each tensor power of \(q\). In particular TM.6's specified
ordinary centered power-sum evaluation \(p_s\) is faithful
on the \(S_\nu\)-component for every \(s\ge K\).
Indeed choose \(S\ge\max(s,D)\); \(p_S\) is an isomorphism
there, and \(p_s=S_\nu(q)p_S\) on that component.

## 2. Stable dimension, with the exact Pieri possibilities

For completeness the stable dimension is computed through the
actual generator algebra HO.3:
\[
\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)
                  \otimes\Lambda(\Lambda^3T).
\tag{RF.11}
\]
The total degree \(D\) is even, so the exterior degree in
\(\Lambda^3T\) is zero, two, or four. Degrees zero and four
give determinant twists of paired shapes in (RF.9), and
cannot give \(\gamma\). Exterior contraction gives the actual
isomorphism
\[
\Lambda^2(\Lambda^3T)=\det T\otimes\Lambda^2T.
\tag{RF.12}
\]
With \(l\ge0\) further determinant generators, the relevant
exterior Pieri map adds a vertical two-strip to a paired shape,
then adds \(l+1\) to every part. The unequal first two and
last two parts of \(\gamma\) force the strip to occupy exactly
rows one and three. Its paired shape before this addition is
\[
(h+j-l,h+j-l,h-l-1,h-l-1).
\tag{RF.13}
\]
It is a partition with nonnegative parts precisely at
\(l=0,1,\ldots,h-1\). Each strip contributes once.
This gives exactly \(h\) copies.

These are the actual column antisymmetrization and Young
projection maps used in HO.5–HO.7. To see that the surjection
HO.3 attains this stable count, take a sufficiently large row
count in TM.8. In every fixed degree its row-orbit character
is exactly the character of \(\Lambda T\) times (RF.11).
Cancel this factor degree by degree using (RF.6), whose
degree-zero factor is the identity. The source and target
of HO.3 then have equal characters in that degree; its
already proved surjectivity makes it an isomorphism there.
Thus the stable ordinary
moment multiplicity, the stable exterior multiplicity, and
the finite invariant multiplicity at every \(s\ge K\) all
equal \(h\), by the commuting maps in (RF.10).
This also rederives the cited established stable count.

## 3. All finite row counts by the actual complement pairing

The length of \(\nu\) is \(m=h+j+2\).
For \(s\le m\), \(\dim W_s=s-1<m\), so \(S_\nu W_s=0\).
Now take \(s\ge m+1\), set \(r=s-1\), and put
\[
q=s-h-j-3\ge0.
\tag{RF.14}
\]
Complementation in the literal rectangle \(4^r\) gives
\[
\nu^c=(4^q,3,2^j,1,0^h).
\tag{RF.15}
\]

Here the comparison is the perfect Schur pairing, not a
dimension identification without a morphism.
On the column-tensor realizations, wedge the \(i\)-th column
of \(\nu\) against the \((5-i)\)-th column of \(\nu^c\);
their heights add to \(r\). Apply the rational Young
projectors on both sides, then take the product of the four
top exterior powers. This is the actual map
\[
S_\nu W_s\otimes S_{\nu^c}W_s\longrightarrow(\det W_s)^4.
\tag{RF.16}
\]
The complementary highest/lowest column tensors have nonzero
pairing. The weights are complementary in \(4^r\), so the
induced map to \((\det W_s)^4\otimes(S_{\nu^c}W_s)^*\)
is a nonzero map between irreducible modules of the same
highest weight; it is an isomorphism.
Equivalently this is the fully specified complementary
column pairing of R-020, now with rectangle width four.

The invariant rational dot form identifies \(W_s^*\) with
\(W_s\) and hence all these Schur duals equivariantly.
A permutation acts on \(\det W_s\) by its sign, so
\((\det W_s)^4\) is the trivial \(S_s\)-module.
Choose any ordered rational basis volume; sending its
fourth power to one trivializes this invariant line.
Thus (RF.16) supplies an explicit \(S_s\)-equivariant
isomorphism of the two invariant spaces.

At \(q=0\) the complement is \((3,2^j,1)\), whose invariant
space is zero at every row count by the actual
three-column surjection CT.4–CT.6. Its two possible families
are only \((2^v)\) and \((3,2^v)\).
For \(1\le q<h\), the complemented tail is the same family
with \(h\) replaced by \(q\). Its threshold is
\(K_q=2q+j+3\), and
\[
s-K_q=2h+j+3-s=K-s\ge0
       \qquad(s<K).
\tag{RF.17}
\]
The uniform layer proof in §1 was already established for
every positive \(h\), so it applies to this complemented
tail and gives dimension \(q\).
There is no inductive assumption on an unknown finite
multiplicity. At \(s\ge K\), §2 gives dimension \(h\).
Combining all four ranges yields the exact formula
\[
\dim(S_\nu W_s)^{S_s}
=\min\{h,\max(0,s-h-j-3)\}=r_s.
\tag{RF.18}
\]

## 4. Homogenization and the actual canonical map

For inner degree \(n\ge4\), every vector of
\(S_\nu W_a\hookrightarrow S_\nu E_a\) has separate
row degrees at most four. Each fixed row letter appears
at most once in each of the four antisymmetric columns.
Thus TM.4's explicit inverse homogenization
\[
f(z_1,\ldots,z_a)\longmapsto
 (\prod_i x_i)^n f(y_1/x_1,\ldots,y_a/x_a)
\tag{RF.19}
\]
extends every invariant polynomial. With the displayed
first-row partition condition, it is an isomorphism
of highest multiplicity spaces. Formula (RF.18) proves
the full target formula (RF.2).

For \(n\ge K\), the actual opposite normalized canonical
map has the exact dehomogenized factorization
\[
h_{a,n}|_\nu=p_n\,\Psi_n\,E_a.
\tag{RF.20}
\]
Here \(E_a\) is independent-row polarization, proved
injective after mean-zero normalization in TM.14;
\(\Psi_n\) is the explicit split-moment automorphism
TM.16–TM.17, with its nonzero scalar in every degree
two through four; \(p_n\) is faithful on this component
by (RF.10). Since \(K\ge5\), every denominator in
the substitution is nonzero in this entire range.

Consequently \(h_{a,n}\) is injective on its complete
\(\lambda\)-multiplicity space. The scalar-one transpose
identity SR.5–SR.6 makes \(h_{n,a}\) surjective on its
complete target component, giving rank \(r_a\).
The same argument with \(a,n\) interchanged gives rank
\(r_n\) when \(a\ge K\) and \(n\ge4\).
At \(s\ge K\), \(r_s=h\), so the two descriptions
agree on their overlap and equal (RF.3).
All zero endpoints follow from the proved dimensions.

## 5. Transport and executed verification

Every projection, invariant average, pairing and substitution
above is rational, with explicitly nonzero denominators.
The maps therefore extend to every characteristic-zero field
and, by their Young-tensor naturality, to every finite rank
supporting \(S_\lambda V\).

The actual coordinate-ring interpretation is the Chow pullback
R-037 EP.3–EP.5, with its scalar-one degree piece in EP.4.
For locally free sheaves it is the associated-bundle map on
the frame torsor from SGA 6 VI, Theorem 3.3.
The precise representation-\(K_0\) and symmetric-algebra
transport is the fixed dictionary of R-036 §5:
SGA 6 V, Proposition 4.2, Definition 4.4, Proposition 4.8
and Corollary 4.9; SGA 3 I, §4.5 and Propositions
4.7.2–4.7.3; EGA II, 2.4.1–2.4.2 and 2.5.2/2.5.4.
No new comparison without its underlying morphism is used.

The script verify_repeated_four_mixed_profile.py independently
expanded the original plethysm by the cycle index and
Murnaghan–Nakayama for every \(h=1,2,3\), \(j=0,1,2,3\),
\(h+j+3\le a\le8\), and \(n=4,5\).
All **60** coefficients agree with (RF.2); the exact receipt
is REPEATED_FOUR_MIXED_PROFILE_MN_CHECK.tsv.
These tests concern the finite coefficient formula.
The actual canonical rank is proved by (RF.7), (RF.10)
and (RF.20), rather than inferred from that coefficient check.

