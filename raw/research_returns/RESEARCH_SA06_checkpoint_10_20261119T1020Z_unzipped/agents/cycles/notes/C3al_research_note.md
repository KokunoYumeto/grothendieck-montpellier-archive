# C.3al research note before checkpoint09

Actual primary-source check clock: 2026-11-19 09:32:14 UTC.
The proof is saved separately as principal_gysin_kernel.tex. At the root's request, it is not yet integrated or entered in the results/check-event registers, so checkpoint09 retains exact compiled/register coverage.

The main observation is the integral inclusion image(i_*) in kernel(i^*) for a principal Cartier divisor. The normal line bundle is trivial, and the Cartier Gysin definition kills each cycle supported on the divisor. C.3t's already verified nonzero ordinary Gysin classes therefore give closed restriction kernels for every r>=2 and r+1<=N<=2r-1. The zero-source range is N<=r. The first remaining higher-codimension pair is (N,r)=(4,2), with remaining range N>=2r.

The root independently agreed with this inference before typing. A full typed audit is requested next.

Primary sources freshly opened in full:

- https://stacks.math.columbia.edu/tag/02T7 — entire Section42.29, including the definition, compatibility with proper pushforward and flat pullback.
- https://stacks.math.columbia.edu/tag/02T8 — Definition42.29.1, cycle supported on the Cartier divisor restricts by the first Chern class of its restricted line bundle.
- https://stacks.math.columbia.edu/tag/0B6Z — Remark42.29.6, trivial restricted line bundle makes the supported cycle's Gysin restriction zero at cycle level.
- https://stacks.math.columbia.edu/tag/0B3P — Lemma31.15.2, normal bundle equals O_X(Y)|_Y.

The new eventual bibliography key is cyStacksPrincipalGysin. It will be written after checkpoint release. No claim is made that the vanishing of Gysin images proves general injectivity.
