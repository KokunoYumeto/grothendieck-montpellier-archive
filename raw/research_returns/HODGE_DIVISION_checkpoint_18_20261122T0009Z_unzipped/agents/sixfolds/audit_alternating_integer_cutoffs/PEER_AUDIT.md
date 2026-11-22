# Independent whole-proof audit: HD-ALT09

**Outcome: PASS. No mathematical correction requested.**

Reviewer: GPT-6 Astra Pro, `/root/sixfolds`; inherited reasoning effort is
not exposed. This is an independent review of the complete new corollary,
not a claim to have independently reproved every earlier source theorem.

## Frozen object and actual reading

The reviewed file is
`research/alternating_remaining_integer_cutoffs_section.tex`, SHA256
`6f45816c177be7398add519ed47bc679a81b65839eb6d6e1f777f2976e1505be`.
I read its complete proof, endpoint argument, table and final scope
paragraph. I also read every line of the author's
`research/check_alternating_integer_cutoffs.py` and all of the actual
`research/alternating_integer_cutoffs_checked.json` output. The author
program was not rerun by me and its output was not overwritten.

The author's output reports a successful first run at
2026-11-21T23:05:53.109494+00:00, internal time 0.05410051599756116 seconds,
with 4,426 exact rejected integer cases. Those are author-reported
computational metadata, distinct from the independent run below.

## Input interfaces

I reread the entire current ALT07 and ALT08 sections. ALT08 had already
received my separate complete proof audit, recorded in
`audit_alternating_conductor/ALT08_PEER_AUDIT.md`. The present corollary uses:

1. ALT07's strict long-row bound
   `k < (1-sqrt(3/5))*n/2` and its universal necessary inequality with
   `h=2`.
2. ALT08's exact conductor alternatives `h=4` when eight divides the
   original quadratic discriminant, and `h=p-1` for an odd discriminant
   prime `p>=5`.
3. The nonstandard-label degree floor `e >= n(n-3)/2`, where `e` is the
   actual inducing degree. It is a lower bound and stays valid under
   positive tensor powers. No replacement by an upper bound is made.
4. The accepted single-factor and all-count standard/two-box exclusions.

For item 4 I checked the actual statement interfaces of HD-AST-09 and
HD-AST-12, and D-ATT-06 and D-ATT-09. Their scope includes every relevant
tensor count, `n>=15`, the transitive ordinary core and the original
non-Eisenstein quadratic field contained in the inducing character field.
The two-factor standard theorem even has the stronger all-field scope.
I read the complete D-ATT-04--06 section and the complete D-ATT-09 proof;
for HD-AST-09/12 I checked their statements, actual representation/field
hypotheses and source setup. The single-factor D-UP-03 and D-EX-03
statements and their field/inducing interfaces were reread. These
predecessors remain accepted proved inputs; I do not claim fresh full
independent audits of all their proofs in this event.

Consequently a surviving oriented ordinary label has `k>=3`, not merely
`k>=1`. There is no unseen extension to projective/spin alternating
representations, a nontransitive tensor core, or the Eisenstein case.
The class-number-one field list is the problem's existing input. Its
elementary discriminant substitutions were checked directly below; no
fresh class-number-one classification proof is being claimed.

## Independent reconstruction of the universal argument

The ALT07 strict bound excludes `n<=26` because
`13*(1-sqrt(3/5))<3`; squaring the two positive sides reduces this to
`3*169>5*100`. Thus `n>=27`.

For `3<=k<n/4`, the derivative of `k(n-1-k)` with respect to `k` is
`n-1-2k>n/2-1>0`. Hence replacing `k` by three decreases the left side
of the necessary inequality. The resulting contradiction is therefore
valid for every surviving tail, not only the two-row tail-three label.

Put `m=5h`. All denominators multiplied in ALT9.3--4 are positive:
`m>=10`, `n>=27`, and `n-1,n-2,n-3>0`. Direct multiplication gives the
stated polynomial

`F = 5n(n-3)[3m(n-4)-(n-1)(n-2)]-6m(n-1)(n-2)`.

Its coefficient in `m` is positive. Indeed `(n-3)(n-4)>n` for
`n>=27`, so the positive term is greater than `15n^2`, and the term
subtracted is less than `6n^2`. If `n<=3m-2`, one therefore has
`F(n,m)>=F(n,(n+2)/3)`. The latter expands to

`3n^3-63n^2+158n-8`

and then to

`3(n-27)^3+180(n-27)^2+3317(n-27)+17380`.

Every term is nonnegative and the constant is positive. This proves
the strict inequality ALT9.3 throughout the claimed interval. The
degree floor supplies `3/(5e)<=6/[5n(n-3)]`, with the correct direction,
so the inequality contradicts ALT9.1. Integrality yields
`n>=3m-1=15h-1`. This is a universal proof for every integer `h>=2`;
the numerical checking grid is not used to extrapolate it.

## Endpoint, table, and exact meaning of minimality

At `n=3m-1`, the numerator
`3m(n-4)-(n-1)(n-2)` is exactly `-6`. Thus ALT9.6 is correct and is
strictly negative. For the actual ordinary partition `(n-3,3)`, the
hook degree is `n(n-1)(n-5)/6`. Subtracting the required degree floor
amounts to the nonnegative factor `(n-7)(n-2)`, and `n>=29` gives
`3<n/4`. Every positive tensor power still satisfies the inequality,
because its beta is already below the limiting term `1/(5h)`.

Even the sharper long-row inequality is consistent at these endpoints:
`3m(n-3)<n^2` at `n=3m-1`. This is not needed for the corollary's
stated minimality but confirms there is no endpoint conflict with the
shape inequalities imported in the proof.

The eight discriminants are `-4,-8,-7,-11,-19,-43,-67,-163`. The
corresponding choices of `h` are `2,4,6,10,18,42,66,162`, and the lower
endpoints are respectively `29,59,89,149,269,629,989,2429`. All table
entries and all endpoint hook degrees were independently checked.

“Smallest” or “sharp” here means the smallest integer allowed by these
numerical necessary conditions after the already accepted exclusions.
It does not assert a generating inertia tuple, a cover, period rank
nine, dominance, an algebraic cycle, or an optimal eventual theorem
about actual sources. The proof and concluding scope paragraph preserve
that distinction correctly. The corollary is a numerical presentation
of already established gates, **not additional standalone movement**.

## Independent exact supplement

`independent_check.py` was written independently and imports no author
code. It uses rational polynomial arithmetic implemented as coefficient
tuples, rather than the author's symbolic algebra package. It verifies
the universal shifted-polynomial and endpoint identities, directly
checks all 193,522 rejected integer pairs for `2<=h<=162`, checks the
endpoint shape inequality for every such `h`, and computes all eight
displayed endpoint degrees from the hook product of the actual Young
diagram, rather than assuming the two-row formula.

The first actual independent run passed at
2026-11-21T23:13:21.140734+00:00, internal time
0.056067402998451144 seconds. Script SHA256:
`01cc13498caf4e7283f4c2aef34b7a7a3e023e2e31f92a77cfaa04797688deb6`.
All output was read. There was no failed run or mathematical amendment.
The adjacent JSON retains exact inputs, hashes, counts, field rows and
the finite-versus-universal scope boundary.

## Conclusion

Complete new proof, source interfaces, arithmetic, endpoint interpretation,
table and exact supplements: **PASS**. No theorem widening or repair is
requested. The earlier published and reviewed background retains its
explicit input status; this audit introduces no new external theorem,
unrefereed source, geometric existence assertion or seed construction.
