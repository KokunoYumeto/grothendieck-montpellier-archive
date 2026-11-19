# The precise Ext corollary at scan 27: two verified coefficient regimes

Source: `pro/MPL_136_002-046_transcription.tex`, lines 729–733. This concerns a tail of the divided-power algebra as source and an **induced** target \(M\otimes_k S\). It is not the assertion that arbitrary shadows have no higher Ext. Checker: GPT-6 Astra Pro; runtime effort not exposed; SA08/root; 2026-11-19.

Let \(S=\Gamma_k(T)\), graded by \(\deg T^{(a)}=a\). Let \(I_d=S_{\geq d}\), for \(d\geq0\). Graded Hom and Ext below mean degree-zero morphisms after a specified shift; equivalently one can fix an arbitrary internal degree \(t\) throughout. The manuscript uses \(d=N-i\) and a shift by \(-i\), with \(i\geq0\).

## Proposition checked here

If \(k\) is an \(\mathbb F_p\)-algebra, then for every \(k\)-module \(M\), every \(d\geq0\), every fixed internal degree \(t\), and every \(n>0\),
\[
 \operatorname{Ext}_{\mathrm{Gr}S}^{n}(I_d,M\otimes_k S(t))=0.
\]
Moreover the restriction map from \(\operatorname{Hom}_{\mathrm{Gr}S}(S,M\otimes S(t))\) to the corresponding Hom from \(I_d\) is an isomorphism. The statement also holds over a \(\mathbb Q\)-algebra in the nonnegative internal-degree regime used on scan27; higher Ext vanishes there for every shift because the tail is free.

This is a proof of restricted cases of the existing claim. It does not establish the manuscript's arbitrary-commutative-base assertion. In particular, no passage through arbitrary coefficient colimits is made.

## Proof in characteristic p

For \(r\geq0\), let \(A_r\subset S\) be the span of \(T^{(a)}\) for \(0\leq a<p^{r+1}\), and set \(D_r=p^{r+1}-1\). This span is a subalgebra in characteristic \(p\): if two indices in this interval add outside it, the binomial coefficient in their product vanishes modulo \(p\). Equivalently, with units used to rescale the generators,
\[
 A_r\simeq k[x_0,\ldots,x_r]/(x_0^p,\ldots,x_r^p),\qquad\deg x_j=p^j.
\]
The remaining divided-power digits give a graded \(k\)-free algebra \(B_r\) with \(S\simeq A_r\otimes_k B_r\). In particular \(S\) is free over \(A_r\).

The coefficient-of-\(T^{(D_r)}\) functional gives a graded perfect pairing on \(A_r\). Indeed the only potentially nonzero complementary-degree pairing is
\[
 T^{(a)}T^{(D_r-a)}=\binom{D_r}{a}T^{(D_r)},
\]
and each \(\binom{D_r}{a}\) is a unit modulo \(p\), since every base-\(p\) digit of \(D_r\) is \(p-1\). Thus \(A_r\) is graded Frobenius over \(k\), with top degree \(D_r\). The finite computation in `root_tail_ext_checks.json` checks these complementary coefficients and closure for several primes and truncations; the digit argument proves them in general.

Put \(Q=S/I_d\). It is a finite graded free \(k\)-module, supported in degrees \(0,\ldots,d-1\), with the evident \(A_r\)-action. Put \(Y=M\otimes_k S\). Frobenius duality and the finite rank of \(A_r\) identify \(Y\), as an \(A_r\)-module, with a coinduced module whose underlying coefficient module has its lowest degree shifted upward by \(D_r\). More explicitly the pairing identifies
\[
 A_r\otimes_k(M\otimes_k B_r)
 \simeq \operatorname{Hom}_k(A_r,M\otimes_k B_r)[\text{top-degree shift}].
\]
To fix the grading explicitly, if \(B=M\otimes_k B_r\), put \(C_j=B_{j-D_r}\). The degree-zero isomorphism sends \(a\otimes b\) to the function \(x\mapsto\lambda(ax)b\), where \(\lambda\) is the top-degree functional. Thus \(C\) starts in degree \(D_r\). An element representing a degree-\(t\) homomorphism from \(Q\) must have degree at least \(D_r\), while the input degree plus \(t\) is at most \(d-1+t\). This convention was independently checked by SA08/early against the telescope argument.

The usual coinduction adjunction, or a graded free \(A_r\)-resolution whose underlying terms are \(k\)-free, therefore gives
\[
 \operatorname{Ext}_{\mathrm{Gr}A_r}^{n}(Q,Y(t))=0\quad(n>0).
\]
Here the corresponding Ext over \(k\) is zero because \(Q\) is \(k\)-free, not because \(M\) is injective. This point permits arbitrary \(M\) and arbitrary \(\mathbb F_p\)-algebra \(k\). The same duality gives
\[
 \operatorname{Hom}_{\mathrm{Gr}A_r}(Q,Y(t))=0
 \quad\text{once }D_r>d-1+t.
\]

Consider \(P_r=S\otimes_{A_r}Q\), with the transition maps induced by the inclusions \(A_r\subset A_{r+1}\). Their colimit is \(Q\), because the union of the \(A_r\) is \(S\). Freeness of \(S\) over \(A_r\) gives derived adjunction
\[
 \operatorname{Ext}_{\mathrm{Gr}S}^{n}(P_r,Y(t))
 \simeq\operatorname{Ext}_{\mathrm{Gr}A_r}^{n}(Q,Y(t)).
\]
Apply Hom and Ext to the standard telescope exact sequence
\[
 0\longrightarrow\bigoplus_rP_r\xrightarrow{1-\mathrm{shift}}
 \bigoplus_rP_r\longrightarrow Q\longrightarrow0.
\]
Higher Ext from either direct sum vanishes, since it is the product of the vanishing Ext groups from its summands. The resulting inverse-system Hom groups are eventually zero in each fixed internal degree. Their inverse limit and first derived inverse limit are therefore zero. It follows that
\[
 \operatorname{Ext}_{\mathrm{Gr}S}^{n}(Q,Y(t))=0\qquad(n\geq0).
\]
Finally use \(0\to I_d\to S\to Q\to0\). Since \(S\) is graded free, the long exact sequence gives the Hom restriction isomorphism and the claimed vanishing of higher Ext from \(I_d\).

## Rational case

If all positive integers are units in \(k\), then \(S\simeq k[T]\), and \(I_d=T^dS\) is a free graded module. Higher Ext into any target vanishes. In nonnegative internal degree, multiplication by \(T^d\) identifies the relevant Hom with the corresponding component of the induced target, exactly as required by the scan27 corollary. For negative internal degrees the Hom statement has a different behavior, consistent with the negative-tail discussion elsewhere; no all-shift Hom assertion is made here.

## What this does not prove

The Frobenius subalgebras used above rely on characteristic \(p\), and the principal ideal argument relies on all factorials being invertible. An arbitrary base ring need satisfy neither condition. A base-change or dévissage proof would have to control infinite products and derived limits in graded Hom. A mere proof of the degree-zero Hom rigidity theorem does not supply this control. Nagpal–Snowden's complete-base/finitely-presented-target results are relevant later work, but their hypotheses are different; their counterexample with a non-induced target is not a counterexample to this manuscript corollary.
