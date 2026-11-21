# Whole-proof audit: HD-ALT03a–c

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro,
effort inherited/unexposed, HODGE_DIVISION, 2026-11-21,
approximately17:34–17:36 UTC.

I read the entire233-line frozen proof in
`research/ordinary_alternating_sharp_obstruction.tex`, SHA-256
`fc04b494c256ef2f20aaa4d419e82358f2cd1bd265e5dcbe91b902ef671f1453`.

## The full normalizer and split constituents

For an extendible ordinary character, the simple core is faithfully
represented and every automorphism comes from S_n. Removing that
implementer leaves a scalar, so the permutation commutator argument
applies even to arbitrary scalar phases. The three cases of a cycle
of length at least three, an involution with a fixed letter, and a
fixed-point-free involution exhaust nonidentity permutations. Their
displayed commutators have exactly the asserted cycle types.

The support inequality concerns the actual rank of the commutator
minus the identity and the minimum support of the original operator;
the argument does not confuse those two quantities. The normalized
character formulas for the actual three-cycle and involution ranks
are exact, including the equality of the two nontrivial cube-root
multiplicities by conjugacy to the inverse inside A_n.

For a split restriction, an odd automorphism exchanges the two
inequivalent constituents and cannot normalize either one alone.
An odd centralizer of the implementing permutation intertwines the
two entire spectra, giving precisely the factor of two used in the
proof. Both comparison classes have odd centralizers. If no odd
centralizer exists, every cycle is odd and its length occurs once;
at n at least15, some length is at least five. The chosen even
three-cycle conjugator then gives the displayed three-cycle
commutator directly on the constituent. This avoids an assumption
about all powers of a split class.

## Content and scalar inequalities

I independently expanded the group-algebra identity for the square
of the transposition sum. An ordered factorization contributes
three to each three-cycle and two to each double transposition.
Substitution of the already reviewed content formula yields exactly
the displayed double-transposition ratio, including its coefficient
four and all denominator factors.

The row estimate uses every row length at most k. The column estimate
uses binomial(h,2) at least h−1 and at most k columns. Applying the
same reasoning after transposition bounds both signs of the content
sum. The final quadratic upper bound is exact for odd n and weaker
for even n. Dropping the nonpositive squared-content contribution
is in the correct direction. The final difference polynomial and
its positive forward difference are correct for every n at least15.
The earlier HD-ALT01 bound on the three-cycle ratio has exactly the
same balanced-shape hypothesis and is sufficient here.

## Tensor and geometric conclusion

For factor-preserving operators, a factor maximum-eigenspace bound
passes to a tensor product by conditioning on the remaining
eigenvalues. Nontrivial factor permutations have the already reviewed
stronger weighted-cycle quarter bound. Genuine scalar inertia moves
the full space. Thus the lower bound applies to every genuine branch
entry, including all outer automorphisms and scalar phases.

The actual intermediate-cover factorization rules out positive genus
at these degrees and forces at least twelve branch points with total
moving rank2e+6. It gives e at most60. The precise previously checked
GKT/Rasala statement gives Specht degree at least2n³/27 for every
balanced shape; division by two in the split case still gives factor
degree at least125. There is no dimension-only inference of dominance.

Every self-conjugate partition has longest row at most ceil(n/2).
Therefore all surviving long shapes are nonsplit restrictions of
real Specht representations. The full irreducible tensor core is
self-dual, and its unique invariant bilinear-form line forces its
entire normalizer to be essentially self-dual. This final structural
conclusion is also correct and does not assert existence.

## Sources and computation

The content-eigenvalue theorem, BNOT restriction rule, Aut(A_n)
description and precise GKT/Rasala threshold retain the primary-source
checks already recorded in the earlier independent ALT01 audit; I
have not claimed a new classification proof or a new source retrieval
in this event. No finite character table is used as a new premise.

The independent program `audit_alternating_sharp.py` imports no author
code. It checks the exact polynomial identities, all displayed
commutator constructions and Young-content inequalities for all
partitions in the retained range. This is a check of formulas; the
whole-proof argument above, not extrapolation, establishes all n and
all tensor exponents. No TeX compilation was performed.
