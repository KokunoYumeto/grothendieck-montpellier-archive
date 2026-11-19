# C.3bb: the divisor endpoint of the additive invariant

Status: finalized after full independent root and cycles proof/source audits.
Final proof: C3_positive_characteristic_divisor_addendum.tex.
The former draft is a comment-only supersession pointer; statement and
original check events are registered.

## Exact input and conclusion

For every algebraically closed field k of characteristic p>0 and every
N>=2, the stated excellent normal strict-local germ with regular puncture
has B1(X) surjecting onto additive k. Ordinary equivalence means actual
families on fixed products. The image has exponent p; this does not give
rational nonvanishing or a higher ordinary-restriction counterexample.
Combined with C.3ba it covers every1<=r<=N-1 integrally.

The projective input is the explicit smooth plane curve
Y^n-YW^(n-1)=Z^(n-1)W, n=p(p+1), with v=(0:0:1), infinity=(0:1:0).
The affine y derivative is minus1 and the infinity W derivative is minus1.
The plane-curve sequence gives connectedness and genus(n-1)(n-2)/2>=10.
L=omega_C has positive degree n(n-3), and the cotangent section is the
identity Omega_C tensor L^-1. There is no false choice of a global
nowhere-vanishing regular differential on a high-genus curve.

Actual selected divisors z=bt on Tot(L^-1) are constructed by the same
finite-normalization and henselian local-factor proof as C.3as. Their
conormal dlog difference is minus b dz/z; its trace has coefficient1.
The entire exceptional divisor is pulled back from C and has zero
conormal component. Ordinary divisibility kills its additive p-target.
The Segre construction of C.3ba is spelled out for r1: Cartier pullback,
H1(Pm times C,O1 external omega_C), z0 coefficient, and resolution-only
localization, with no assumed map between punctures.

## Primary sources freshly opened and read

- Stacks Lemma53.9.3, Tag0BYD, full statement and plane-curve exact-sequence
  proof: https://stacks.math.columbia.edu/tag/0BYD .
- Stacks Section53.8, Tag0BY6, especially Lemmas53.8.3-4, full statements
  and the canonical-degree/duality proof:
  https://stacks.math.columbia.edu/tag/0BY6 . The exact direct tags are
  0C19 and0C1A; the complete section containing them was read.
- Stacks Lemma33.44.14, Tag0B5X, full statement and proof that positive
  degree is equivalent to ampleness on a proper curve:
  https://stacks.math.columbia.edu/tag/0B5X .
- Stacks Section48.27, Tag0FVU, freshly reopened, especially
  Lemma48.27.1(5)-(7), the duality/trace functoriality and smooth
  differential identification: https://stacks.math.columbia.edu/tag/0FVU .
- The Segre Kunneth input Stacks33.29.1/0BED was freshly checked in C.3ba.
  The r1 cycle map is the classical Picard dlog map itself; no additional
  higher Milnor/Quillen comparison is required for this endpoint.

The new bibliography entry is C3bb_references.bib. The precise base
normalization proof and full-section contraction are inherited from
certified C.3as, whose hypotheses are independently rechecked here.

## Finite certificate and standalone verification

code/check_divisor_endpoint.py retains eight prime-specific exact curve
and derivative checks and49dimension/coefficient-extraction cases. All
pass. It explicitly separates finite-field sample checks from the
all-geometric-points derivative proof and the actual-branch theorem.
Runtime seconds: 0.0040200869989348575. Full stdout and JSON are retained.

The complete draft passed all four LuaLaTeX/BibTeX wrapper stages at
2026-11-19T11:56:35.446854UTC in2.972970834998705seconds, with zero
diagnostics. Root read the entire proof, exact program and all retained output cases,
and freshly opened all four primary Stacks sources; its full pass was
received before finalization. Cycles completed its full proof/source pass
at11:57:41.888542UTC. No independent reviewer program rerun is claimed.


Root requested the exact trace locator Lemma48.27.1(5-7) and
Remarks48.27.2-3; it is now explicit in the final text. Cycles full review
and canonical event are retained in agents/cycles/
C3bb_positive_characteristic_divisor_endpoint_independent_REVIEW.md and
the matching CHECK_EVENTS.tsv. The final renamed wrapper is recorded
separately. This is an endpoint strengthening, not a new main-gate reset.

Final renamed proof passed all four wrapper stages at2026-11-19T12:01:01.577228+00:00 in3.223562122999seconds, zero diagnostics. Original outputs and final event are retained.
