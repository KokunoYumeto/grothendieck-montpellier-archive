# Unchecked, withheld prolate counting inference

This file records an unresolved source reconciliation. It is not a proved result and must not be promoted into the theorem module or an assertion that the published theorem is false.

The author-hosted March3,2022 CM draft, https://alainconnes.org/wp-content/uploads/PNAS_030322.pdf , section5, Theorem5.1, equation(33), p6, takes lambda=sqrt(2) and counts eigenvalues of **positive imaginary part less than E of 2 slash-D**. The proof specifies that these are `+2i sqrt(-mu)` for negative eigenvalues mu of the restricted operator denoted `W'_sa+`, with `|mu| < (E/2)^2`. It prints

`N(E) ~ [E/(2*pi)]*(log(E/(2*pi))-1) - log(E)/(2*pi) + O(1)`.

The following paragraph calls the logarithmic term a refinement of the semiclassical estimate. The source uses the asymptotic symbol `~`, so one must also fix its intended strength before treating the formula as an additive O(1) expansion. The introduction equation(2) only gives the coarser logarithmic-error statement. The earlier arXiv version https://arxiv.org/pdf/2112.05500 , Theorem6.1, prints the leading expression with O(1) and no displayed logarithmic correction.

RRJT2025, https://doi.org/10.5802/crmath.780 , Theorem14, gives an imaginary-axis spectral characterization with parity exchange. AC-S12 computes the corresponding regular half-line Liouville differential expression exactly. It does not by itself transport the relevant CM domain. Reconciling the refined asymptotic with that domain correspondence would require reading the cited Sturm--Liouville counting results and proving the appropriate endpoint and remainder hypotheses. That verification has not been completed.

A tempting inference was that, **if** the exact count being compared really obeyed the additive expansion `F(E)-log(E)/(2*pi)+O(1)`, whereas the zeta count under A is `F(E)+o(log E)`, an ordered shift of about1 might follow. We have deliberately withheld both this shift claim and any exact-isospectrality exclusion based on it. Matching only leading counting asymptotics gives neither equality of spectral points nor that shift. The precise parity, multiplicity, spectral restriction, lambda, square-root scaling, asymptotic notation, and version must first be reconciled.
