# Exact curve-cover reduction and remaining recognition map

## CC-1 / E.2.22: proved reduction

Full proposed TeX is `work/E_curve_cover.tex`. For sigma in Gamma_Fcm,
actual integral Tate transport for all abelian varieties is equivalent
to the same property for Jacobians of all compactifications of connected
finite etale covers of P1 minus {0,1,infinity}.

The exact quotient J(C) -> A is integrally surjective. The curve comes
from Milne's successive smooth ample sections, whose inverse images
under finite surjective etale isogenies remain smooth and connected.
A proper finite-index image Lambda' on H1 would yield the algebraic
isogeny A/H -> A, H=(Lambda'/n)/Lambda_A in A[n]. Its pullback to C has
trivial deck monodromy and degree greater than one, contradiction.
Both q_* and (sigma q)_* are surjective on the actual lattices, so
rho_A q_* Lambda_J=(sigma q)_* rho_J Lambda_J
=(sigma q)_* Lambda_sigmaJ=Lambda_sigmaA.

Belyi supplies C as such a compactification. The actual Galois action
on the profinite free group sends each open subgroup U to sigma U.
Quotient of U^ab by peripheral inertia gives the completed compactified
H1, and Abel--Jacobi identifies this with the actual Jacobian Tate
module, carrying the specified integral H1 lattice. All maps are natural.
Inner independence is exact: for h in profinite Pi and open U choose
p in discrete Pi with h in pU. On U^ab, conjugation by h equals that by p,
which is an actual change of topological path and preserves the lattice.

## Opened primary sources and access record

* Milne, *Jacobian Varieties*, corrected author version June 12, 2021:
  https://www.jmilne.org/math/xnotes/JVs.pdf . Theorem 10.1 p.33,
  Lemma 10.3 p.34, proof pp.34-35. Root independently read and passed the
  exact integral-surjectivity upgrade. Only finite **surjective etale
  isogenies** are used from the source's broad wording about finite maps.
* Belyi, *Another proof of three points theorem*, MPIM 1997/46,
  dated April 25, 1997. Theorem 1 p.1 and old proof pp.1-2 actually read;
  bar over Q verified in rendered p.1.
  https://archive.mpim-bonn.mpg.de/id/eprint/3134/2/preprint_1997_46.ps .
  Local PS/PDF/TXT: `work/sources_generation/belyi1997.*`.
  The MathNet 1980 PDF endpoints redirected or returned 403 and were
  **not** counted as opened. The primary 1997 text reproduces the
  original constructive proof over Qbar and suffices for the exact use.
* Matsumoto--Tamagawa, *Mapping-class-group action versus Galois action
  on profinite fundamental groups*, MPIM 1997/92. Theorem 1.1 p.2,
  proof p.3; Theorems 2.1-2.2 p.2 and Remark 2.1 p.3 read.
  https://archive.mpim-bonn.mpg.de/id/eprint/2601/2/preprint_1997_92.ps .
  Local PS/PDF/TXT: `work/sources_generation/matsumoto_tamagawa1997.*`.
* Boggi--Zalesskii, arXiv:1111.2373v5, June 13, 2024:
  https://arxiv.org/pdf/1111.2373 . Definition 2.1 pp.2-3,
  Theorem 2.3 p.4, Proposition 4.1 pp.11-12, Remark 4.2 p.12,
  Theorem 4.3 p.12, Theorem 5.5 p.14 read. Their completed Reidemeister
  pairing is preserved up to orientation by every profinite automorphism;
  Galois orientation is cyclotomic. The simple/disjoint curve criteria
  in Theorems 2.3/4.3 take discrete curve classes as input.
* Lochak, author `bfl.pdf`, Section 3.3 pp.14-16; Theorem 7.1 p.34,
  proof p.36; Proposition 7.3 p.37:
  https://webusers.imj-prg.fr/~pierre.lochak/textes/bfl.pdf .
  The pants-prostack theorem requires the actual coherent prostack map.

## Exact remaining recognition map

The actual integral homology condition in E.2.22 has not been shown
to land in the procongruence mapping-class image. Matsumoto--Tamagawa's
intersection theorem is an exact terminal theorem once membership is
established, but no such membership is asserted. Galois elements already
preserve the completed pairings (cyclotomic multiplier one here), so
replacing the integral-lattice condition by completed pairing preservation
does not establish the missing map. No equality of geometric, discrete,
profinite or procongruence automorphism groups is assumed.

This is an equivalent formulation of the all-abelian residual criterion,
not a completed separation theorem for the explicit quartic place-pair
or for the full pure-motive category.
