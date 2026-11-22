# Whole-proof review of AM-R-001, AM-R-002 and AM-R-003

Reviewer: /root/lift_accounting, GPT-6 Astra Pro; reasoning effort not exposed.
Run: ALP_MACHINE. Date: 2026-11-21 UTC.
Reviewed file: work/research/endpoint_cost_and_isotypy.md, complete text as read
in this run. Type: targeted proof check, with direct checks of the cited
source definitions. No Lean execution and no reproof of the accepted global
theorems are claimed.

## AM-R-001: PASS, one source-scope wording refinement

All terms in the rebuilt-family subtraction are correct. The changed main
term is \(MH-M'H'=(M-M')H-M'(H'-H)\), so the retained corrections,
deleted tail, endpoint tau and K differences have the right signs.
The allowance correction \(B_M-B'_{M'}\) is correct. No identification
between local place sets is needed once each side has been aggregated to
real scalar totals. The observation that a negative difference alone does
not prove failure of a threshold is also correct.

The primary source LinkG_at has, in addition to its one-sided ramp
inequality, the explicit coarse bounds
\(0\le {\rm gain}_{j,w}\le4|{\rm TT}|a/p\).
Thus the sentence “LinkG_at is a lower certificate, not an upper bound”
should be read specifically as referring to the ramp clause. Recommended
wording: “The ramp clause of LinkG_at is a lower certificate, rather than
an equality or sharp upper bound on gain.” This is a precision correction;
it changes no proof or global conclusion.

## AM-R-002: PASS

The functional image of a full finite projective lattice is a finitely
generated fractional ideal, and nonzero because the lattice spans the
domain. Localization preserves the image, so at a DVR its image is
\(\pi^s\mathcal O\). After enlarging the lattice by \(\pi^{-d}\), the
image is \(\pi^{s-d}\mathcal O\), which contains 1 precisely when
\(d\ge s\). Taking \(d\ge0\) proves the stated minimum, including
negative content exponents. Generating-row valuation is correctly the
minimum of the coefficient valuations.

For the convention conjugate-linear in the first Hermitian argument,
Riesz represents a complex-linear functional as \(z\mapsto\langle
y,z\rangle\). The minimizer \(y/\|y\|^2\) is correct. In the source
specialization, \(B(f,z)=\langle Jz,f\rangle\) is indeed linear in z
because J is conjugate-linear. Surjectivity and the transported
quotient metric give exactly \(\beta(f)=\|f\|\); the kernel qualifier
is necessary and present.

The Arakelov sign is correct: relative to the lattice \(I_f\), the
rational section 1 has divisor coefficients \(-s_\mathfrak p\), while
its quotient norm is \(\beta_\sigma^{-1}\). Arithmetic degree is
\(-\sum s_\mathfrak p\log N\mathfrak p+\sum_\sigma\log\beta_\sigma\),
so the quantity R7 is its negative after the stated degree
normalization. Counting every complex embedding gives the usual
conjugate-pair multiplicity. The product formula cancels the change
under scaling exactly.

The source coefficient formula was checked directly in
CoefModB.lean, fockB/extNormB/pairB/pairBK (18,55–62), and
Record.lean, perCl (315–329). It has the displayed factorial weights,
the reciprocal extremal Fock norm, and reciprocal finite stabilizer
order. The sum over actual invariant classes is essential; the memo
does not replace their integral lattices with the full unconstrained
polynomial module. Its inclusion-matrix correction covers a lattice
whose classwise coordinates are tied. No unimodularity assertion is
used.

This is an exact reduction of endpoint normalization to content and
dual norm once an algebraic terminal vector and its actual lattice
are supplied. It is not a construction of that vector; the memo
maintains this limit throughout.

## AM-R-003: PASS

The Galois group of \(\mathbb Q(\zeta_7)\) is cyclic of order 6.
Its only proper CM subfield is the degree-two imaginary field
\(\mathbb Q(\sqrt{-7})\), whose induced types are 124 and 356.
Type123 is therefore primitive. Milne, Complex Multiplication,
2020, Proposition 3.13, was opened directly in the primary notes:
it classifies simple CM isogeny classes by primitive CM pairs.
Combined with Proposition 3.12, it supplies geometric simplicity
of the actual J. This is an application of those cited results,
not a claim that the source's theta interface itself proves
simplicity.

Every nonzero homomorphism from simple J to an elliptic curve would
have a positive-dimensional connected kernel of dimension 2.
Every nonzero map in the reverse direction would have a
one-dimensional abelian image in J. Both contradict simplicity.
The matrix description of Hom between products therefore gives
the claimed vanishing in both directions. Poincaré complete
reducibility extends it to subvarieties and quotients.

The proof is over an algebraic closure, so finite field extensions
and changes to a named CM action do not affect it. A finite
projective module over an order acting on a characteristic-zero
elliptic curve becomes a free module over its rational
endomorphism field; clearing denominators makes its Serre tensor
isogenous to an elliptic power. Hence it cannot belong nontrivially
to the J-isotypic subcategory. The restriction to elliptic Serre
tensors is essential and is stated; no nonexistence of all
mixed-type theta correspondences follows.

## Scope of this review

All three complete proofs were read. Direct local source checks
confirm the normalizations used above. The external Milne result
was checked at statement and application level. No proof of
Milne's general classification, no whole Lean dependency audit,
and no execution of Lean took place.
