# Primary oscillator source audit

Statement **A-059**. Checked 21 November 2026 by GPT-6 Astra Pro,
run `/root/archive_audit`; effort setting not exposed.

Primary source: T. Basile, E. Joung, K. Mkrtchyan and M. Mojaza,
*Dual Pair Correspondence in Physics: Oscillator Realizations and
Representations*, arXiv:2006.07102v2, subsequently JHEP 09 (2020) 020,
DOI 10.1007/JHEP09(2020)020.
https://arxiv.org/pdf/2006.07102v2

The web PDF fetch returned a disabled-fetch error. A direct request
to that same primary URL then returned an actual 952017-byte PDF,
saved as `OSCILLATOR_DUALITY_2020V2.pdf`; extracted text is saved
alongside. This audit read the text and mathematical formulas,
without claiming new visual inspection of the page images.

## Exact passages read

- §5.1, (5.7)–(5.20), printed pp.28–29: compact oscillator
  realization, central shifts, Young conditions and Cauchy duality.
- Entire §5.2, (5.21)–(5.30), printed pp.29–31: the
  \(U(M_+,M_-)\), \(U(N)\) differential operators, minimal
  oscillator state, contraction conditions and mixed highest weight.
- Appendix A, (A.21)–(A.28), printed pp.76–77, together with
  the surrounding derivation: the mixed tensor, exterior-column
  contraction and the resulting complementary highest weight.
- The representation convention (1.16), printed p.7; the
  explicit cover discussion (2.12)–(2.18), printed p.10; and
  (2.23)–(2.25), printed p.11. These specify the source's use
  of double-cover compact groups and its half-integral weights.

## Statements established by these passages

The differential operators in (5.21) have diagonal shifts
\(+N/2\) in the positive block and \(-N/2\) in the
negative block. The compact partner (5.22) has scalar diagonal
shift \((M_+-M_-)/2\). The contraction equations (5.28)
identify the mixed traceless tensor of (5.29), whose unshifted
highest weight is
\[
(\ell_1,\ldots,\ell_p,0,\ldots,0,-m_q,\ldots,-m_1).
\]
The exterior-column Levi–Civita contraction in (A.25) is the
actual map to the polynomial highest weight obtained after a
determinant twist; (A.26)–(A.28) display that weight explicitly.
The strict range \(p+q<N\) proposed for T-052 lies within
all the dimensional inequalities used in this passage.

The source explicitly includes the covering-group convention.
Its symbols must retain that convention when the displayed
half-integral generators are used literally. For example a
positive-block vacuum coordinate of weight \(N/2\) acquires
\((-1)^N\) around the corresponding \(2\pi\) circle. This
is an exact monodromy calculation, and (2.12)–(2.18) explains
the analogous issue in the source. A proposed unshifted action
or an honest-group identification needs its actual changed
generators and integration, rather than suppressing the shifts.
No objection to the source's stated cover convention is claimed.

## A precise equality-boundary correction

The sentence immediately before (A.23), printed p.76, says that
traceless tensors vanish at \(p+q\ge N\). At equality this
is false. For \(N=2\), let \(e_1,e_2\) be the standard
basis and \(e_1^*,e_2^*\) its dual. The actual contraction
\[
\mathbf C^2\otimes(\mathbf C^2)^*\longrightarrow\mathbf C,
\qquad v\otimes\phi\longmapsto\phi(v)
\]
kills the nonzero tensor \(e_1\otimes e_2^*\). It has
the two one-box symmetries, so \(p=q=1\) and \(p+q=N\).
It is the highest vector of weight \((1,-1)\) for the usual
upper-triangular convention. Thus the equality claim is refuted
by the displayed morphism. The source's later paragraph before
(A.28) correctly permits \(p+q\le N\), as does (A.21).
The intended T-052 range is strict and does not use the rejected
equality sentence.

This is a source audit and an explicit boundary correction. It
does not certify the entire new T-052 construction, which had
not yet been supplied when these checks were recorded.
