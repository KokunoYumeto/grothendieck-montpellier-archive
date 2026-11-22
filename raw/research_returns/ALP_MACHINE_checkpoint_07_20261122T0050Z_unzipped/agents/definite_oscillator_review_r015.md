# Independent whole-proof review of AM-R-015

Reviewer: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator,
21 November2026UTC; inherited reasoning effort not separately exposed.

**Outcome: PASS in the stated genuine oriented-kernel model.**
The review covers every section of
`work/research/selected_real_descent.md`, its source-convention
transport, the exact signed-list calculation, the regular local
theta theorem, the first-occurrence invariant, and the passage to
the genuine smooth cuspidal domain. It does not certify an
arithmetic ThetaX/D7 construction or the obstructed literal
unramified odd global character.

## Source convention

I read the literal `liftInt`, `IsIo`, `IsIoUp`, `chrStep`, the
chain ties in `StepsOnto` and `LinksChar`, `Step.up`, and
`TiedWeil.om_swap`, `splitFac`, `th`, `PhiYupTied`. The exact paths
and formulas are recorded in
`definite_oscillator_review_indefinite_conjugation.md`.

They confirm that the downward integral is bilinear in the
unbarred smaller-first kernel and the larger-group input. Its
adjoint uses the conjugated kernel. The rank-reversing abstract
WA presentation uses the transpose swap with swapped characters,
not a new fixed-orientation Hom model. This validates the direction
used in R15.1–2.

For the real tensor pair with signatures \((p,q),(r,s)\), denote
the opposing half-angular character shifts by \(c_{\rm big}\)
and \(c_{\rm small}\). The vacuum portion of the compact-weight
formula after the small-factor inverse transpose is

\[
 \begin{array}{c|c}
 K_{\rm small}&
 (-(r-s)/2-c_{\rm big})^{[p]};
 ((r-s)/2-c_{\rm big})^{[q]}\\
 K_{\rm big}&
 ((p-q)/2+c_{\rm small})^{[r]};
 (-(p-q)/2+c_{\rm small})^{[s]}.
 \end{array}
\]

This follows directly from Ichino's Lemma7.10 by applying
inverse transpose to the small compact group. It supplies the
odd baseline as well as the even case; parity makes these
weights integral. In particular the character shift changes
sign on the small Hom factor and retains its sign on the big
factor. It is consistent with the source's rank-dependent
`splitFac` and with R15.5. The claim is about the standard genuine
real splitting transported in R015, not an inference that every
abstract action satisfying a partial set of source axioms is
already that splitting.

## Parameter calculation

The ranks satisfy \(n_j\equiv j+1\pmod2\). Thus the source
character attached to even j has the odd-space half shift,
whereas Dpar itself has its extra half shift at odd j.
Subtracting the opposing attached character therefore gives
the two cancellations R15.5 exactly.

I checked the lists directly against DataTheta.lean538–554.
The future-b signs alternate, and passing from j to j+1
exchanges the two future negative lists. The old inserted
blocks stay in the positive signature slot. The new block
has t terms in that slot. Counting gives
\(|A_j|=N_j\), \(|B_j|=q_{j+1}\), \(|E_j|=q_j\).
The centering inequalities exclude all entries within the
closed central interval extending to \(\pm(t+1)/2\), outside
the new block. Interlacing puts every old block on the
positive side of the new center; a block cannot cross zero
because the full block is subject to Centred. The other
entries have the signs claimed in R15.7. Hence the list is
regular and has exactly the displayed signatures.

## Local analytic input

I directly opened and read Ichino's primary preprint,
arXiv:2008.06174v2, section4.1, Theorem4.1(i), the normalized
cohomological-induction convention in section3.4,
Lemma7.10, and the complete statement and proof of Lemma8.2.
The regular-case lemma uses Li's local result directly.
Its bound is \((m-n+1)/2=(t+1)/2\), below the actual
\((t+3)/2\) bound. The extra signature dimensions are t
and zero. The normalized compact-Levi zero block has
infinitesimal-character contribution
\(((t-1)/2,\ldots,-(t-1)/2)\), because the remaining rho
is the compact-Levi rho. This verifies the upward discrete
series identification and the reverse identification by
Howe duality without invoking the paper's general
Arthur-formula-dependent theorem.

I also directly read Atobe's primary repository copy,
Definition1.6 and Theorem1.7 with the paragraph immediately
after it, printed pp.4–5. The central block is maximal
because its next endpoints \(\pm(t+1)/2\) are absent.
His invariants are consequently exactly
\((k_\lambda,r_\lambda,s_\lambda)=(t,p_j,q_j)\).
The balanced Witt tower criterion gives zero for every
negative common shift, exactly the lower targets in R15.14.

There is an explicit cross-paper convention check:
Ichino section6.2, printed p.20, states that Atobe's
choice of additive character agrees with his section4.1
choice. His Theorem6.1(ii) has a possible shift-minus-one
exception only when both next central endpoints occur;
R15.7 excludes that condition independently. Thus neither
the unspecified notation for Atobe's additive character
nor the corrected tempered exceptional cases introduce
a gap in this application.

## Global representation scope

The input is restricted to the actual smooth cusp domain
specified in AM-R-014. Projecting a cuspidal image onto
an irreducible real constituent gives an irreducible
quotient of the corresponding big theta module. Howe
duality fixes its type. Complex conjugation then gives
the literal IsDv type in CayleySignature.lean123–125.
For lower targets the entire local big theta module is
zero; this kills every compact-finite Schwartz component
and then the full theta integral by its continuous
smooth globalization. This is stronger than vanishing
of one chosen local test vector and is exactly the
second clause of the fifth analytic predicate.

These observations justify R015 in its explicitly chosen
genuine analytic model. They do not identify its arithmetic
row, its finite raw Xi, an integral terminal detector, or
an unchanged elliptic constructor. No Lean compilation
or direct whole-paper review of Li1990 was performed.

## Primary references checked

Atobe, H. (2020). On the non-vanishing of theta liftings of
tempered representations of U(p,q). *Advances in Mathematics,
363*,106984. https://doi.org/10.1016/j.aim.2020.106984 .
Repository copy:
https://eprints.lib.hokudai.ac.jp/repo/huscap/all/84508/Adv.%20math%20363_106984.pdf .
Definition1.6, Theorem1.7 and its unconditional discrete-series
qualification, pp.4–5; tensor/splitting conventions, section3.

Ichino, A. (2022). Theta lifting for tempered representations
of real unitary groups. *Advances in Mathematics,398*,108188.
https://doi.org/10.1016/j.aim.2022.108188 .
https://arxiv.org/pdf/2008.06174 . Sections3.4,4.1,6.2;
Theorem4.1(i), Theorem6.1(ii), Lemma7.10 and Lemma8.2.
