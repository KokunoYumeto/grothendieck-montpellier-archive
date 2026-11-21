# SF-E823: a global obstruction to every tensor hull repair of the unit surface extension

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** complete new derivation, submitted for independent whole-proof
review. No simplicity, stability, splitting, or equivariant structure on the
hull factor is assumed. The assertion concerns actual tensor products; it is
not a claim about all sheaves with the same local extension matrix.

## 1. Statement and the actual input

Let \(X\) be a complex abelian fourfold with the genuine balanced RM data of
SF-E819: \(\theta=\theta_++\theta_-\), with each positive form supported
on its two-dimensional eigenspace. Put

\[
 v_q=\left(1-\frac q2\theta_+^2\right)
       \left(1-\frac q2\theta_-^2\right),\qquad q>0.
 \tag{E823.1}
\]

Choose \(D=k\theta\), \(k>0\), and a smooth complete intersection
\(S=D_0\cap D_1\), with both divisors in \(|D|\). Let \(M_0\) be the
actual unit extension

\[
 0\to\mathcal O_S(-2D)\to M_0\to I_S\to0,
 \qquad \operatorname{ch}(M_0)=1-2D^3+4D^4,
 \tag{E823.2}
\]

constructed in the unequal-slope compensation note. In particular its rank is
one and its first two positive-degree character components vanish. Let \(H\)
be **any locally free sheaf of positive rank** \(r\), and suppose

\[
 e^B\operatorname{ch}(H\otimes M_0)=r v_q,
 \qquad B\in\operatorname{NS}(X)_{\mathbf Q}.
 \tag{E823.3}
\]

Then \(H\otimes M_0\) is not weakly semiregular for any specified effective
coherent finite translation/tensor action in the sense of supplied S21. The
finite action need only be given on the tensor product; no compatible action
on \(H\) or \(M_0\) separately is assumed.

The complete proof below is global. The local corrected resolutions in the
compensation note give zero characteristic obstruction for every constant
bivector on every sufficiently small affine neighborhood. Thus this result
does not reassert the former local obstruction.

## 2. The partial trace and its Atiyah-class identity

Let \(F\) be any perfect complex and \(H\) a vector bundle of rank \(r\).
Tensor duality gives a canonical partial trace

\[
 \operatorname{Tr}_H:
 \operatorname{Ext}^2_X(H\otimes F,H\otimes F)
       \longrightarrow\operatorname{Ext}^2_X(F,F).
 \tag{E823.4}
\]

Explicitly, precompose with the coevaluation
\(F\to H^\vee\otimes H\otimes F\), apply the middle morphism, and
postcompose with evaluation. It is defined in the ordinary derived category
regardless of any finite action. Its value on an endomorphism supported only
on \(F\) is \(r\) times that endomorphism.

Write \(A_H,A_F\) for the Chern-normalized Atiyah classes, with
\(\operatorname{ch}(H)=\operatorname{Tr}\exp(A_H)\). Thus our \(A\) is the
negative of the class denoted \(\mathrm{At}\) in BF2008, whose
Atiyah--Chern character is \(\exp(-\mathrm{At})\). This single sign
convention is used in every formula below. Their tensor identity is

\[
 A_{H\otimes F}=A_H\otimes1+1\otimes A_F.
 \tag{E823.5}
\]

One can see this directly on a finite locally free resolution of \(F\):
choose local connections, and use the tensor connection on each term. Its
commutator with the differential is the sum of the two commutators, while
the differences on overlaps obey the identical Leibniz rule. These represent
the Atiyah classes in the total Čech/endomorphism complex, giving (E823.5)
as a derived identity. The Ext sign and the differential-form sign cancel
when the two Atiyah factors interchange; this is the usual even total-degree
convention that also gives \(\operatorname{ch}(H\otimes F)=
\operatorname{ch}(H)\operatorname{ch}(F)\).

For a rational algebraic divisor \(B\), put

\[
 A_H^B=A_H+B\operatorname{id}_H,
 \quad c_1^B(H)=\operatorname{Tr}A_H^B,
 \quad \operatorname{ch}_2^B(H)=
       \tfrac12\operatorname{Tr}(A_H^B)^2.
 \tag{E823.6}
\]

These are cohomological definitions; they require no fractional line bundle.
They are the first two components of \(e^B\operatorname{ch}(H)\).
Taking the partial trace of the square of (E823.5), with \(B\) added to
the \(H\) factor, gives the exact identity

\[
 \tfrac12\operatorname{Tr}_H(A_{H\otimes F}+B)^2
  =r\,\tfrac12 A_F^2
    +c_1^B(H)\,A_F
    +\operatorname{ch}_2^B(H)\operatorname{id}_F.
 \tag{E823.7}
\]

This is simply the three terms of the tensor square, with the two mixed
terms combined before dividing by two. In particular, a vanishing first
Chern class removes the whole mixed term in Ext, not merely its trace.

## 3. Hochschild evaluation and the rational B-field

For \(\pi\in H^0(X,\bigwedge^2T_X)\) and
\(\eta\in H^2(X,\mathcal O_X)\), the characteristic morphism in the
consistent HKR/Atiyah convention is

\[
 \rho_E(\pi+\eta)=
       \pi\mathbin{\lrcorner}\tfrac12 A_E^2
                         +\eta\operatorname{id}_E.
 \tag{E823.8}
\]

The exact characteristic/Atiyah locator is published BF2008,
Theorem5.1.3, author-copy pp24--25, Proposition5.2.2, p26, and
Corollary5.2.3, p27. The complete invoked proofs and the corollary were
freshly read for this result. The sign convention is displayed in section4.2,
p22. The trace/composition identity remains Proposition6.2.1,
Corollary6.3.2 and Theorem6.4.2, author-copy pp29--33, including the full
Proposition6.4.4 proof already read for SF-E819. The paper is published in
Advances in Mathematics217(2008),243--281, DOI10.1016/j.aim.2007.06.013;
the author copy is https://arxiv.org/pdf/math/0606730. No unrefereed
substitute is used.

For clarity, the B-field version means the following. Conjugate the Clifford
operator of \(\pi+\eta\) on Hodge cohomology by multiplication by \(e^B\).
The resulting class \(\xi_B\in HH^2(X)\) has bivector, mixed, and
\(H^2(\mathcal O_X)\) components. Expanding the square gives

\[
 \rho_E(\xi_B)=
       \pi\mathbin{\lrcorner}\tfrac12(A_E+B)^2
                         +\eta\operatorname{id}_E,
 \qquad
 c_{\operatorname{ch}E}(\xi_B)
    =e^{-B}c_{e^B\operatorname{ch}E}(\pi+\eta).
 \tag{E823.9}
\]

This is the same B-shear used in SF-E819. The equality follows by expanding
\(e^{-B}\iota_\pi e^B\): the constant, one-contraction and
zero-contraction terms match \(A_E^2/2\), \(BA_E\) and \(B^2/2\),
respectively. It is an identity of rational cohomological classes; neither
an integral B-field nor an isogeny is needed.

Combining (E823.7)--(E823.9) yields

\[
 \begin{split}
 \operatorname{Tr}_H\rho_{H\otimes F}(\xi_B)
   ={}&r\rho_F(\pi)
     +\pi\mathbin{\lrcorner}\bigl(c_1^B(H)A_F\bigr)\\
    &+\bigl(\pi\mathbin{\lrcorner}\operatorname{ch}_2^B(H)
                         +r\eta\bigr)\operatorname{id}_F.
 \end{split}
 \tag{E823.10}
\]

## 4. Balanced vanishing would force an impossible global vanishing

Take \(F=M_0\). Its first two character components vanish, so comparing
degrees one and two in (E823.3) gives

\[
 c_1^B(H)=0,
 \qquad \operatorname{ch}_2^B(H)
       =-\frac{rq}{2}(\theta_+^2+\theta_-^2).
 \tag{E823.11}
\]

Choose the nonzero invariant bivector \(\pi_+\) on the first plane and
define \(\eta_+=\pi_+\mathbin{\lrcorner}(\theta_+^2/2)\). As checked
in SF-E819, \(\pi_++q\eta_+\) annihilates the entire balanced character
\(v_q\). Thus its B-shear \(\xi_B\) lies in
\(\ker c_{\operatorname{ch}(H\otimes M_0)}\).

Suppose the tensor product were weakly semiregular for the specified finite
action. Supplied S21's invariant-evaluation/forgetting compatibility and the
published BF composition identity imply
\(\rho_{H\otimes M_0}(\xi_B)=0\) in ordinary Ext, exactly as in SF-E819.
Apply (E823.10), taking \(\eta=q\eta_+\). Both its second and third
terms vanish by (E823.11), so

\[
 r\rho_{M_0}(\pi_+)=0.
 \tag{E823.12}
\]

Since \(r>0\), this would give \(\rho_{M_0}(\pi_+)=0\). But the ordinary
BF identity says

\[
 \sigma_{M_0}\rho_{M_0}(\pi_+)
       =\pi_+\mathbin{\lrcorner}\operatorname{ch}(M_0).
 \tag{E823.13}
\]

Its component of Hodge type \((1,3)\), using (E823.2), is

\[
 -2\pi_+\mathbin{\lrcorner}D^3
       =-12k^3\eta_+\theta_-\ne0.
 \tag{E823.14}
\]

Indeed \(\theta_+^3=\theta_-^3=0\), so only
\(3k^3\theta_+^2\theta_-\) contributes to this contraction. The other
cubic term has only one holomorphic slot in the plus plane. The product
\(\eta_+\theta_-\) is nonzero because it has full antiholomorphic degree
two in the plus plane and degree \((1,1)\) in the complementary plane.
This contradicts (E823.12), proving the theorem.

## 5. Exact scope and the next genuinely different object

The proof excludes every actual tensor product \(H\otimes M_0\) satisfying
(E823.3), including unstable, indecomposable and nonsimple vector bundles
\(H\). It does not require an equivariant decomposition or a lift of the
action to either tensor factor. Thus replacing the split interpolated hull by
a nonsplit hull while keeping this tensor construction cannot produce the
desired seed.

There may be other global extension classes with the same local unit matrix
and the same hull, torsion and defect, which are not isomorphic to this tensor
product. The partial trace (E823.4) requires the actual global tensor factor;
it is not asserted for arbitrary local tensor identifications. Such genuinely
different global gluing, nonuniform local extension matrices, other slopes,
and more general derived objects remain open. The local nullhomotopies are
retained as evidence that this new obstruction is global, not a hidden
reuse of the equal-degree hypothesis.

## 6. Exact arithmetic check and limits of that check

`rm_tensor_surface_certificate.py` has actually passed. Its eight-generator
exterior algebra checks the entire compensated character for symbolic k,q,
both balanced cap kernels, and both nonzero cubic obstruction formulas. It
also checks the B-shear signs on all256 exterior basis elements for each of
the two bivectors, with the displayed exact non-diagonal integral B matrix
(512 checks). This is a finite sign check; the general-B identity and the
derived partial trace are proved in the text, not inferred from that matrix.
No computation of Ext groups, a finite action, or semiregularity is claimed.
