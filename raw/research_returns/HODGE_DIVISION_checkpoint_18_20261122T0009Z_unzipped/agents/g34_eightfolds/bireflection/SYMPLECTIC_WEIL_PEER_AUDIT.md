# Whole-proof audit: D-SPW-01–03

**Result: PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro,
effort inherited/unexposed, HODGE_DIVISION, 2026-11-21, approximately
17:11–17:13 UTC. The complete revised proof was read, not merely its
statements or numerical output.

Reviewed file: `agents/imprimitive/lie_small_fields/symplectic_weil_section.tex`.
Reviewed SHA-256:
`20fd3f9fa781e7184c44095ce8ee2fcd43b8c69ff39fca97c142c3e927a7daac`.

## Published inputs actually checked

1. Gérardin, *Weil representations associated to finite fields*, J. Algebra
   46 (1977), 54–101: Theorem 2.4(a), pp.63–64; the Schrödinger formulas in
   its proof; Theorem 4.4(c), pp.84–85; Corollary 4.4(a), p.85, including
   its complete irreducibility/parity proof. These passages of the original
   article were read through the primary-article transcription at
   <https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields>.
   The trace formula and irreducibility are appropriately treated as
   published inputs, not claimed as new results.
2. Taylor, *Action of automorphisms on irreducible characters of symplectic
   groups*, §§1.5 and12.5. The exact version independently opened was
   <https://arxiv.org/pdf/1612.03138>, displaying arXiv1612.03138v1,
   9 December2016. In this version §1.5 is on numbered p.2 and §12.5 spans
   numbered pp.21–22. The latter explicitly supplies the entire automorphism
   group, and §1.5 explicitly excludes graph automorphisms in odd
   characteristic. The author's p.24 locator refers to the later author
   version at
   <https://personalpages.manchester.ac.uk/staff/jay.taylor/files/preprints/action-automorphisms-symplectic.pdf>.
   The sibling author supplied that exact locator; my attempt to fetch
   this later PDF timed out, so the independently read version remains
   arXiv v1. The two versions' pagination is not interchanged.
3. Hiss–Husen–Magaard, Chapter5, preceding paragraph and complete Table1,
   numbered p.35, freshly reread in the retained primary PDF text. This
   specifically explains why PSp4(3), in characteristic three, has no
   exceptional multiplier. None of the odd-characteristic symplectic
   groups in the theorem requires an additional exceptional cover.

The original proof of the general finite-simple-group automorphism
classification was not independently reproved. Its precise published
specialization in Taylor was read.

## Mathematical checks

### D-SPW-01

The full Weil absolute-trace identity applies over both the original
finite field and its prime field. Two Heisenberg intertwiners for the same
symplectic transformation differ by a scalar; unitary normalization makes
that scalar have modulus one. The parity conjugate implements the same
central transformation and has the same nonzero trace1, so its scalar is
exactly one. This justifies the parity commutation used later.

The restriction-of-scalars model is correct: quotienting the original
Heisenberg center by the kernel of its trace character gives precisely
the prime-field Heisenberg model. Both linear Weil extensions restrict
to extensions of that same irreducible Heisenberg representation.
Their quotient is a one-dimensional character of Sp2n(q), which is
trivial since n≥2 and q is odd. No unstated functoriality of Weil
representations is needed.

### D-SPW-02

For a noncentral natural symplectic matrix, the positive- and
negative-one primary spaces are nondegenerate alternating. Thus an
eigenspace of dimension2n−1 exhausts the entire generalized primary
space and leaves no opposite eigenvalue. The displayed convexity bound
on the two trace contributions follows, including its n=2 endpoint.
The inequality |tr(T)|≥a−2ν(T) allows the largest eigenspace to have any
eigenvalue; it does not confuse ordinary moving rank with projective
support.

All inner bounds, both small q=3 exceptions, and their integer ceilings
check. The nonsquare diagonal automorphism changes the transvection
Gauss-sum term while leaving the parity-twisted trace1. Perfectness
eliminates a possible projective-equivalence character, so this really
excludes diagonal normalizers of a fixed constituent.

For a character with trace parameter a, the explicitly defined
t=a^((p−1)/2) satisfies t²=a^p/a. Consequently S=tσ preserves the
prime-field trace symplectic form and implements the desired field
automorphism. The identity S^f=±1 is valid. Its Weil intertwiner commutes
with parity, proving that field automorphisms preserve each constituent;
therefore a diagonal-field product cannot cancel the diagonal exchange.

For gS^k, the minimal-linear-relation argument correctly bounds both
the positive- and negative-one fixed spaces over the fixed field by2n.
It works for an arbitrary semilinear map of this form, not just a pure
Frobenius. The prime-field trace formula then gives the displayed
2q^(n/2)/(q^n−1) bound. Every actual normalizer differs by a scalar from
one of these intertwiners after lifting to the universal perfect cover.
Finite order permits a common invariant positive form, so using unitary
trace inequalities here is justified.

### D-SPW-03

The tensor-product eigenspace bound and the previously reviewed
weighted-cycle argument cover all factor permutations. Scalar inertia
has full moving rank. The actual intermediate-cover factorization,
including a larger inducing field, is used correctly: genus one gives
at most six parameters and genus at least two is numerically impossible
for e≥4. Rank nine therefore forces genus zero, at least twelve genuine
branch points, and moving sum2e+6.

The one-fifth bound gives e≤15 before the finite enumeration. Integer
ceilings leave only4,5,9,10,15. Two factors already have degree at least16.
The complete single-factor enumeration q^n≤31 leaves only the
Sp4(3) degrees4 and5. No inference of dominance from a dimension
equality, and no nonsplit-polarization or character-field-equality
assumption, has entered this argument.

## Independent computation

`audit_symplectic_weil.py` was written without importing the author
program and executed successfully. Its JSON retains the reviewed proof
hash. It independently checks the rational radical bounds, all relevant
integer ceilings, the complete prime-power list after the proved cutoff,
and the two surviving degrees. This is a finite arithmetic certificate;
the unbounded trace and semilinear statements are established by the
whole-proof reading above, not by finite sampling.

## Scope

The conclusion covers precisely odd-characteristic symplectic Weil
constituents and their compatible full normalizers, including central
quotients and mixed tensor products of such factors. It makes no claim
about non-Weil constituents, even characteristic, or the two remaining
low-dimensional factors. No TeX compilation was performed.
