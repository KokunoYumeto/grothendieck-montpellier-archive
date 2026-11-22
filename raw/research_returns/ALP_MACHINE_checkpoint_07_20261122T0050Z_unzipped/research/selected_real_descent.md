# AM-R-015: the selected real discrete-series descent and its exact first occurrence

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November2026UTC.

This finding computes the real correspondence on the actual signed
Harish--Chandra lists in the source. The insertion block has length t,
its compact sign is positive, and its exact first-occurrence invariant
is t. Every smaller target obtained by removing a positive number of
hyperbolic planes is therefore zero. The analytic consequence is the
fifth source predicate in the genuine oriented-kernel interpretation
specified below. This is an application of established real theta
theorems, with a new explicit check of the selected parameters and
the source's conjugation convention. It supplies no integral row tie
or arithmetic terminal value.

## 1. The oriented vertical kernel

The direction of the integral must be distinguished from the direction
of the Hom model. For the edge from the smaller space Y_j to the larger
space Y_(j+1), write its oriented theta kernel as
\(\theta_j(g,h;\Phi)\), with g on the smaller group. The actual downward
operator is

\[
 \mathcal D_j(\Phi,F)(g)
       =\int_{[U(Y_{j+1})]}\theta_j(g,h;\Phi)F(h)\,dh.
 \tag{R15.1}
\]

It is bilinear and has no conjugation on the kernel. Its Hilbert-space
adjoint upward operator uses the conjugated kernel. This is exactly
`IndefiniteReal/OrthogonalComplementCharacterisation.lean`, liftInt/IsIo,
lines41--55, and IsIoUp, lines78--88; `LinksChar.lean`, lines283--287,
ties ioY/ioX to that convention. `ChainParSucc.lean`, line132, is the
adjoint upward formula. The abstract downward th has reversed group
order: `BesselHermitianTheta/TiedWeil.lean`, lines131--142, specifies
the swapped characters and transpose transport without an additional
complex conjugation.

Consequently one must not replace (R15.1) by a newly chosen standard
Hom kernel from the larger space to the smaller space. That replacement
would alter the representation and its character shifts.

The small-group Hom action is contragredient. Transport it by
\(g\mapsto g^{-t}\) to the ordinary tensor dual pair, and transport
the form and additive character together. In the standard real tensor
convention of Ichino section4.1, the additive character is
\(x\mapsto e^{-2\pi i x}\). The compact weight formula is his
Lemma7.10, including the cross-character shifts. In Hom coordinates
the corresponding joint representation is

\[
       \overline{\sigma_j}\boxtimes\sigma_{j+1}
 \tag{R15.2}
\]

when the tensor correspondence pairs \(\sigma_j\) with
\(\sigma_{j+1}\). The transpose-inverse on the small factor changes
its discrete-series parameter to the contragredient parameter; this
can also be read on its compact Cartan, where every weight is negated,
followed by the compact Weyl reordering. This statement applies to
the odd and indefinite ranks as well: character changes are ratios
with trivial real restriction, while the fixed odd baseline is pinned
by the standard real compact-weight formula. It does not extrapolate
the even-only determinant-root formula of AM-DO-028 to an unspecified
odd splitting.

Explicitly, for signatures \((p,q),(r,s)\), the small Hom factor
has compact vacuum weights
\[
 \bigl(-(r-s)/2-c_{\rm big}\bigr)^{[p]};
 \bigl((r-s)/2-c_{\rm big}\bigr)^{[q]},
\]
whereas the large factor has weights
\[
 \bigl((p-q)/2+c_{\rm small}\bigr)^{[r]};
 \bigl(-(p-q)/2+c_{\rm small}\bigr)^{[s]}.
\]
These are Lemma7.10's two vacuum lists after negating the small
compact weights. Their integrality follows from the rank and
character parities. They fix the odd baseline as well as all
integer character twists. This identifies the standard genuine
splitting chosen here; it does not claim that a partial list of
abstract source axioms alone uniquely determines a real splitting.

Thus an input F with \(\overline F\) of type \(\sigma_{j+1}\)
can have downward type only \(\overline{\sigma_j}\). The parameter
calculation proving the indicated correspondence follows.

## 2. Cross-character centering of the actual lists

Fix a selected complex embedding. Retain the source hypotheses
Interlace, TParity and Centred, and write

\[
 n_j=k+m-1+jt,\qquad q_j=\lfloor(m-j)/2\rfloor,
 \qquad p_j=n_j-q_j,\qquad N_j=k+j(t+1).
 \tag{R15.3}
\]

The source odd character has half-angular weight \(h=\pm1/2\), so the
parameter \(\eta=-h\) has exactly the two values permitted by
TPar.eta_half. Let
\(\chi_i=\operatorname{car}(\mu,j+1,i)\) for this edge. Then

\[
 c_i=\operatorname{infTy}\chi_i
          =-e_j+1_{i\ \mathrm{even}}\eta.
 \tag{R15.4}
\]

If \(D_i^0\) denotes the unshifted signed list in Dpar i, the source
definition gives \(D_i=D_i^0+1_{i\ \mathrm{odd}}\eta\). Hence the two
cross-character shifts cancel exactly:

\[
       D_j-c_{j+1}=D_j^0+e_j,
       \qquad D_{j+1}-c_j=D_{j+1}^0+e_j.
 \tag{R15.5}
\]

These are the actual half-angular shifts m0/2 and n0/2 in the real
theta convention. They are not arbitrary simultaneous translations.
The rank parities and the odd half-integral h give the ordinary
Harish--Chandra lattice \(\mathbb Z+(n_i-1)/2\) on each group.

Sort each of the following lists in decreasing order:

\[
 \begin{split}
 A_j={}&\{v_l+e_j:0\le l<k-1\}
       \cup\{e_j-b_i:0\le i\le j\}\\
      &\quad\cup\bigcup_{i<j}\bigl(B_t(-e_i)+e_j\bigr),\\
 B_j={}&\{e_j-b_i:i>j,\ i-j\ \mathrm{even}\},\\
 E_j={}&\{e_j-b_i:i>j,\ i-j\ \mathrm{odd}\},\\
 B_t(0)={}&((t-1)/2,(t-3)/2,\ldots,-(t-1)/2).
 \end{split}
 \tag{R15.6}
\]

The letter E_j here is a list, not a number field. Interlace orders the
centers e_i and the b_i. Every member of A_j is positive: the v terms
lie above -b_0, the b_i terms have i<=j, and each earlier block lies
entirely above the current center by Centred. Every member of B_j and
E_j is negative. More precisely Centred gives

\[
   a\ge(t+3)/2\quad(a\in A_j),\qquad
   b,e\le-(t+3)/2\quad(b\in B_j,e\in E_j).
 \tag{R15.7}
\]

All entries are integers. They are distinct: interlacing separates
the v and b entries, while Centred separates each inserted block
from every other block and from these entries. The centered signed
lists are exactly

\[
 \begin{array}{c|c|c}
 &\text{positive signature slot}&\text{negative signature slot}\\\hline
 D_j-c_{j+1}&A_j\cup B_j&E_j\\
 D_{j+1}-c_j&A_j\cup B_t(0)\cup E_j&B_j.
 \end{array}
 \tag{R15.8}
\]

Indeed the future b-signs flip when j increases by one, the old
positive entries retain their signs, and the new block is entirely
in the positive signature slot. This also follows directly from
`DataTheta.lean`, Dpar, lines538--543.

The exact list lengths are

\[
 |A_j|=N_j,\quad |B_j|=q_{j+1},\quad |E_j|=q_j,
 \tag{R15.9}
\]

so (R15.8) has precisely the source signatures, not merely the correct
total ranks:

\[
 (p_j,q_j)=(N_j+q_{j+1},q_j),\qquad
 (p_{j+1},q_{j+1})=(N_j+q_j+t,q_{j+1}).
 \tag{R15.10}
\]

## 3. Nonzero upward correspondence and the exact downward type

Apply the sufficiently separated discrete-series case of real theta
lifting: Ichino (2022), Lemma8.2, printed p.35, with its explicit
regular-case proof citing Li (1990). The applicable separation is
\((t+1)/2\); (R15.7) is stronger. The four lists in that result are
\((A_j,B_j,\varnothing,E_j)\), and the two extra signature dimensions
are t and0, respectively, by (R15.10).

The resulting cohomological induction has compact Levi block U(t)
and one-dimensional remaining Levi factors. In the normalized
induction parameter its inserted block is zero repeated t times.
The compact Levi rho adds the distinct sequence B_t(0); all remaining
entries remain the entries in (R15.8). Equivalently, refine the compact
Levi to a compact Cartan and use induction in stages. The inequalities
(R15.7) keep this refinement in the good range and the final parameter
regular. Thus the representation is the discrete series with exactly
the second signed list of (R15.8), after restoring the shift c_j.
It is \(\sigma_{j+1}\), with parameter D_(j+1).

Therefore, in the tensor convention with these exact characters,

\[
             \theta_{p_{j+1},q_{j+1}}(\sigma_j)
                         =\sigma_{j+1}\ne0.
 \tag{R15.11}
\]

Howe duality then gives the reverse small lift

\[
             \theta_{p_j,q_j}(\sigma_{j+1})=\sigma_j.
 \tag{R15.12}
\]

Only the regular case of Lemma8.2 is used. The general theorem in
Ichino's introduction invokes a global Arthur multiplicity formula;
that general conditional input is not being used here. Its regular
case is the earlier local Li theorem, explicitly isolated in Lemma8.2.
No new proof of Li's theorem or of Howe duality is claimed.

## 4. Exact first occurrence and all lower-target vanishing

For the reverse correspondence, center the larger parameter by the
smaller-space character c_j. By (R15.8) it contains the contiguous
central block B_t(0), all in the positive signature slot. This block
is maximal: its next possible endpoints would be
\(\pm(t+1)/2\), which are absent by (R15.7). Its length is therefore
exactly t in Atobe's Definition1.6, not merely at least t.

The remaining positive entries are A_j; the remaining negative
entries in the positive slot are E_j; the negative-slot entries
are B_j, all negative. Consequently Atobe's two base indices are

\[
     k_{\sigma_{j+1}}=t,\qquad
     r_{\sigma_{j+1}}=|A_j|+|B_j|=p_j,\qquad
     s_{\sigma_{j+1}}=|E_j|=q_j.
 \tag{R15.13}
\]

Atobe (2020), Theorem1.7(2), last sentence, determines this balanced
Witt tower unconditionally for discrete series. Its permitted shifts
are precisely the nonnegative integers. The smaller targets in the
source have shift -i. Hence

\[
 \boxed{\quad
 \theta_{p_j-i,q_j-i}(\sigma_{j+1})=0
       \qquad(1\le i\le q_j).
 \quad}
 \tag{R15.14}
\]

The theorem concerns the big-theta nonvanishing criterion as well,
so these are zero intertwining spaces, not merely zeros of a chosen
Schwartz vector. The discrete-series clause is explicitly declared
unconditional on printed p.5 of Atobe's published paper. The later
correction to its separate k=-1 tempered case is irrelevant because
here k=t>=1.

For the additive-character convention, Ichino section6.2, printed
p.20, explicitly identifies Atobe's convention with his section4.1
choice, using the compact-weight comparison of Lemma7.10. His
Theorem6.1(ii) gives the same balanced-tower conclusion here: its
exceptional negative-shift possibility requires both next central
endpoints, whereas (R15.7) excludes both. Thus a change of the
additive-character sign is not being silently absorbed into the
signature labels.

## 5. Consequence for the genuine fifth source predicate

Use the genuine smooth cusp domain of AM-R-014 and the downward
orientation (R15.1). If \(\overline F\) has the prescribed real
type D_(j+1), then F has the contragredient type. Equation(R15.2),
Howe duality and (R15.12) imply that every nonzero cuspidal downward
image has contragredient real type D_j. Thus its complex conjugate
has type D_j, which is exactly IsDv at stage j.

One can justify the assertion constituent by constituent in the
cuspidal unitary spectrum: every irreducible real constituent of
the image is a quotient of the corresponding big theta module,
whose unique irreducible quotient is fixed by (R15.12). The actual
cusp inputs lie in finite sums of smooth automorphic embeddings,
as specified in AM-R-014; no decomposition of arbitrary smooth
functions is assumed. For compact-finite test data the assertion
holds on the Harish--Chandra modules and then their smooth
globalizations.

For a lower target, (R15.14) makes every such local intertwining
space zero at each chosen real place. It therefore kills the
global theta integral for every Schwartz input. Equivalently,
first use the zero Harish--Chandra theta module on dense compact
vectors and extend by continuity of the cuspidal theta integral
in the usual Schwartz/smooth-cusp topologies. The measures and
normalizing nonzero scalars do not affect this vanishing.

These are exactly the two conclusions of
`CayleySignature.RealThetaLiftDiscreteSeries`, lines186--194.
Together with AM-R-013/014, they verify five of the six analytic
predicates in the explicitly stated genuine model. The remaining
analytic predicate is ThetaUnfoldingFreeData, with its precise
Fourier--Jacobi period and factorizable witness. A full arithmetic
ThetaX/D7 instance, the odd global character pin on a repaired host,
the raw-Xi selected action and the terminal mass remain separate.

## 6. Geometric framework and source status

The signed weights, central character shifts and compact-Levi Schur
classes live in SGA3 I Proposition4.7.3/Corollary4.7.3.1 and the
carried SGA6 VI Theorem3.3 representation/flag framework. The oriented
kernel remains an actual polarized Hom/theta-group line, in the
SGA7 I VII2.7/2.9 setting, pp.169--174. Neither a virtual class nor
an isocrystal slope proves the analytic real correspondence; the
specific local theorems cited above supply that independent input.

The source lists, parity and centering are DataTheta.lean538--555
and CayleySignature.lean104--125. The rank/signature formulas are
Params.lean and the definitions sigYD/rankYD in the recovered source.
No Lean execution is claimed.

## References

Atobe, H. (2020). On the non-vanishing of theta liftings of tempered
representations of U(p,q). *Advances in Mathematics, 363*,106984.
https://doi.org/10.1016/j.aim.2020.106984 . Author repository copy:
https://eprints.lib.hokudai.ac.jp/repo/huscap/all/84508/Adv.%20math%20363_106984.pdf .
Definition1.6 and Theorem1.7, printed pp.4--5; the unconditional
discrete-series scope is explicit immediately after that theorem.

Ichino, A. (2022). Theta lifting for tempered representations of real
unitary groups. *Advances in Mathematics, 398*,108188.
https://doi.org/10.1016/j.aim.2022.108188 . Author preprint:
https://arxiv.org/pdf/2008.06174 . Section4.1 p.10; Lemma7.10
pp.30--31; regular-case Lemma8.2 p.35 and its proof. The general
conditional theorem is distinguished from this local regular case.
Theorem6.1(ii) and section6.2, printed pp.19--20, fix the balanced
tower and the additive-character convention.

Li, J.-S. (1990). Theta lifting for unitary representations with
nonzero cohomology. *Duke Mathematical Journal, 61*(3),913--937.
https://doi.org/10.1215/S0012-7094-90-06135-6 . The precise regular
case used here is read in Ichino's Lemma8.2; direct retrieval of
the original publisher text was blocked by a service security page.
No direct whole-paper reading of Li is claimed.

Review status: author whole-proof reading PASS, 2026-11-21T23:40:17.491120+00:00. Independent whole-proof review by /root/definite_oscillator also PASS, recorded separately in definite_oscillator_review_r015.md. The author reread the complete revised proof, including the explicit compact vacuum shifts, exact source down/adjoint distinction, regular local input, first-occurrence invariant and smooth-cusp scope. No arithmetic constructor or Lean build is certified.
