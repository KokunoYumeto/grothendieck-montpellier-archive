# Independent whole-proof review: P-F22

Reviewer: GPT-6 Astra Pro, effort inherited/undisclosed, run `/root/bridges`.
Event date: 2026-11-21, final source and proof re-read completed at 00:53:58 UTC.
Draft: `work/positivity_gorenstein_collapse.tex`.

## Outcome

PASS. I read the entire proof and independently reconstructed every mathematical step. This is an actual proof-check event, not a proposed check or a historical-priority assertion.

The recurrence preserves `1+b^2+c^2=3bc`, coprimality, and avoidance of the prime three. Its selected pairs satisfy `2b<c<3b`. In the exact hypotheses of Cristofaro-Gardiner–Li–Stanley Corollary 1.5, substitution `(p,q,r,s)=(c,b,b,c)` gives the required two divisibilities and the two gcd conditions. The intercept triangle has area one half and exactly three lattice points at dilation one; its now-polynomial Ehrhart function is therefore `binom(s+2,2)`. The integral translation `Q=3P-(1,1)` gives the stated common Hilbert polynomial and series.

I recomputed the three primitive rays, checked their primitivity using coprimality with three, and checked that the three displayed facet inequalities alone imply nonnegative height and only the origin at height zero. Fundamental-parallelepiped decomposition makes the ring finite free over the ray polynomial subring, so it is a three-dimensional Cohen–Macaulay domain. The intersection of the three normal halfspace rings gives normality. Every primitive facet form takes value one on `(0,0,1)`; the interior-lattice-point translation proves that the canonical module is principal using the cited toric canonical-module theorem. The rational-singularity source has the required characteristic-zero scope.

For the canonical degree tuple, the sloping-face equation reduces exactly to `br+ct=3s`. All four cases used to rule out `0<s<b` are valid. Two parameters of degree below `b` would vanish in the two-dimensional face quotient, and one remaining parameter cannot make that quotient finite-dimensional. Thus the second entry is at least `b`. With first two entries `(1,b)`, the extreme-ray quotient of degree `c` forces the third entry to be a positive multiple of `c`. Combined with the explicit tuple `(1,b,c)`, this establishes lexicographic minimality, rather than merely existence of one system.

The conclusion has the correct scope: fixed Hilbert series and normal, Cohen–Macaulay, Gorenstein, rational-singularity hypotheses do not control canonical parameter degrees for general graded domains. No factoriality or ordinary-plethysm realization is inferred.

## Primary-source verification actually performed

- Cristofaro-Gardiner–Li–Stanley, *New examples of period collapse*, arXiv:1509.01887v1, Corollary 1.5, printed p.4. Fresh direct retrieval: `turn255124643view2` (earlier direct read `turn164195568view0`); URL <https://arxiv.org/pdf/1509.01887>. I verified both complete gcd/divisibility conditions, including the second condition across the extraction boundary.
- Danilov, *The geometry of toric varieties*, Section 4.6, printed pp.111–112, canonical module as interior monomials. Direct read in this run: `turn164195568view1`. URL <https://www.math.purdue.edu/~arapura/danilov.pdf>.
- Danilov, Section 8.2 and Proposition 8.5.1, printed pp.124–125, toric resolution and vanishing. Direct read earlier in this run, during P-F21 review: `turn122557666view1`. This source was reused without pretending to have independently proved toric resolution theory.

No change to the author's theorem file was made by this reviewer.
