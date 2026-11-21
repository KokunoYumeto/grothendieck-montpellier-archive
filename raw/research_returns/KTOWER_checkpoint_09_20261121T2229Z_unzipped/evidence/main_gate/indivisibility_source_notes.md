# Indivisibility route: primary-source scope notes

Root reading, 21 November 2026. GPT-6 Astra Pro; effort setting not exposed.
These are research audit notes pending integration into the next paper revision.
They supply no simultaneous auxiliary-unit existence theorem and are not progress-review movement.

## Kimura's displayed construction

Primary: Iwao Kimura, *Indivisibility of special values of zeta functions associated to real quadratic fields*, RIMS Kôkyûroku Bessatsu B4 (2007), Theorem 3.1 and its proof, printed pp.11–15; Corollary3.3 on p.16. Official PDF:
https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B4/pdf/B04_001.pdf .
The full Theorem3.1 proof was read in extracted text. Printed pp.11,14,15 were additionally inspected as rendered images. The local PDF hash is 55cab47cab314efa794c59cf57a5c39df5d317837d0a3d611d0d379ff0cf37ee.

Two displayed steps need additional justification before using the asserted p-ramified discriminant conclusion here.

First, the form in the proof is depleted at p. Its Fourier support consists of indices prime to p. The later sieves and U_l,V_l operations, with l distinct from p, preserve that support. A nonzero coefficient H(r,nl) obtained at the end therefore has p∤nl. Writing nl=Df², its fundamental discriminant D is also prime to p. The displayed conclusion D_l=d_l lp is not obtained from this coefficient construction as written. This observation does not prove that the theorem's assertion is false, and no such claim is made.

Second, equation(3.6) is U_l G_r=c V_l G_r, where

    a=l^(r−1), b=l^(2r−1), c=1−a+b.

At the selected index D0*l³, the normalized U coefficient is

    1+b+b²−a−ab,

and the V coefficient is c. The comparison needed to contradict (3.6) is consequently

    (1+b+b²−a−ab)−c²
      = a(1−l^r)(1−a).

The printed comparison instead subtracts c, which establishes U≠V under its stated condition l^r≠1 but does not itself contradict U=cV. Requiring also l^(r−1)≠1 repairs this particular coefficient comparison whenever an admissible residue can be chosen. It does not repair the separate discriminant-support step. This is a check of the displayed proof, not a counterexample to its theorem.

The existing KTOWER Jacobi construction already supplies a different bounded one-unit family. Neither source gives the simultaneous same-discriminant third unit required here.

## Other readings in this bounded attempt

Ono1999: Theorem2 statement and the initial construction were read; no whole-proof audit is claimed here. Byeon2003: the opening Theorems1–2 and the quoted Naito statement were read; the full proof was not audited. These concern an individual quadratic-field indivisibility condition. No transfer to the present pair of twisted units is asserted. Exact retrieval URLs and hashes are in `literature/indivisibility_scope/retrieval.json`.

The separate complete scoped search for the selected quadratic modular-symbol coefficient is recorded by lean_chain in `QUADRATIC_SYMBOL_NONVANISHING_SCOPE.md`. Its conclusion is limited to the searched primary sources; it is not a claim of nonexistence of an applicable theorem.
