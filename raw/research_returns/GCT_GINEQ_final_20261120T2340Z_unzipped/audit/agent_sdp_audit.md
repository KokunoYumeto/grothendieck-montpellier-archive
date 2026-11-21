# Independent-agent audit of tensor-norm notes

Auditor: `/root/grothendieck_sdp`, GPT-6 Astra Pro; reasoning effort not exposed.
Run: GCT_GINEQ. Date: 2026-11-20 UTC (2026-11-21 Europe/Berlin).
Source audited: full proof portions N-01 through N-07 of
`/workspace/scratch/df09d7aab1e9/work/agent_tensor_norms.md`.

Actual check type: targeted full-proof check by a different agent, with
coefficient derivations and exact symbolic arithmetic performed by hand.
This is not formal verification and is not labelled a blind independent
reproof. No gap was found in the audited proofs.

## N-01 — PASS

The minimal support spaces are the images of mode flattenings; the commuting
orthogonal projectors fix the tensor. The projective norm is unchanged on
restricting to these spaces because both inclusion and the orthogonal
projection tensor product are contractive. Expanding along all but one
factor gives exactly `prod_{i!=j} q_i` orthogonal coefficient vectors, so
Cauchy-Schwarz gives the nuclear bound with the square root and the
largest coefficient gives the spectral bound. The exponents `2/(d-1)`
and ceiling operations are correct. `q_i<=border_rank` follows from minors;
the domination by `max q_i` therefore holds over the stated fields. The
real-norm statement for a real tensor's complex border rank is also valid:
the proof factors through the equal real/complex matrix support ranks.

## N-02 — PASS

The exact norms have the asserted coordinate normalization. The trace
bound works over R and C, and the self-dual witness yields nuclear norm
`n^3`. The factorwise basis identification in the tensor product really
produces `M_nm`; there is no unproved appeal to tensor nuclear norm
multiplicativity. The comparison `8^k / 7^k -> infinity` refutes every
fixed multiplicative repair for both ordinary and border rank. Ordinary
flattening rows have disjoint support of size n and norm sqrt(n), giving
all `n^2` singular values as stated.

## N-03 — PASS

The W-state norm rescaling was checked directly against the supplied
Friedland--Lim source near lines 599--635: its normalized C tensor has
spectral norm `2/3`, real nuclear norm `sqrt(3)`, complex nuclear norm
`3/2`. Multiplication by `sqrt(3)` gives exactly the audited values.
The two-dimensional slice pencil has determinant `-x^2`; only one
projective line of rank-one matrices is present, preventing CP rank two.
The difference-quotient tensors have two independent first factors and
two independent squared factors for nonzero t. For `t=1/100`, the tail
norm bound `sqrt(3t^2+t^4)<=2t`, the strict inequality
`2/sqrt(3)<6/5`, and `7500>2*3721` are exact. Thus the explicit rational
tensor refutes all three ordinary-rank comparisons, with no limiting
argument needed for this last conclusion.

## N-04 — PASS

The normalized simple-atom parameter set is compact over either field;
complex phases can indeed be absorbed into one unit factor. The finite
sum image is compact. The dual witness bounds the total projective mass,
and bounded individual terms force a rank-at-most-r limit. To state the
strongest precise conclusion, the maximum term norm (and total term norm)
must tend to infinity along any fixed-r decomposition sequence converging
to a rank-greater-than-r tensor; a bounded subsequence already contradicts
compactness. The weaker wording 'unbounded' in the notes is valid.

## N-05 — PASS

The identity tensor `e tensor I_m` refutes the displayed spectral-denominator
formula, and `I_m` refutes the displayed matrix inequality. The corrected
flattening comparisons follow from expanding each right singular vector
as a matrix SVD with Hilbert norm one and nuclear norm at most
`sqrt(min(q_2,q_3))`. The contraction duality proof of the spectral
comparison uses Hilbert-unit matrices and is valid over both fields.
No top-singular-term replacement assumption is made. This audit checked
the mathematical counterexamples and corrected proof; it did not
independently re-typeset the external paper's equation numbering.

## N-06a — PASS

A partial matching between two k-subsets has k! bijections and k! orders
of its k pairs, hence `(k!)^2` row coordinates per block. The complementary
block has `((n-k)!)^2` columns. Its sign factorization is the Laplace sign
identity, checked independently in S-08. The singular value is
`k!(n-k)!/n!=1/binom(n,k)` and the number of disjoint blocks is
`binom(n,k)^2`. Their squared singular values sum to one. The same
flattening rank lower-bounds both CP and Waring border rank, since a
pure power is in particular a simple tensor.

## N-06b — PASS

For the determinant average, multiplying by the row-sign product forces
all n row occupancies odd. With total degree n they all equal one. The
single supporting permutation then also forces distinct columns; its
uniform probability is `1/n!`. The surviving coefficient is therefore
`sgn(sigma)n^(-n/2)/n!`, exactly `n^(-n/2) S_det`.
For the permanent average, row and column signs independently force
all row and column occupancies to equal one. The coefficient is
`n^(-n)`, exactly `(n!/n^n) S_per`. The proposed matrices have Frobenius
norm one. The spectral maxima from Banach plus determinant/CLL agree
with `I/sqrt(n)` and `J/n`, and norm duality supplies matching nuclear
lower bounds. All normalizations and real/complex uses are consistent.

## N-07 — PASS

The row determinant assertion uses a cited rank upper bound; conditional
on that quoted known bound the amplification is immediate and correctly
stated. The permanent upper bound also has the correct symmetric
polarization count. The recurrence
`A_(n+1)/A_n=(1+1/n)^n/2 >=9/8` for `n>=2` is correct; its third binomial
term is `(n-1)/(2n)>=1/4` before division by two. In the symmetric
determinant sign average, globally negating row signs changes both the
weight and the pure power by `(-1)^n`, so duplicate summands pair off.
For the permanent, the analogous row and column actions are independent
and give fourfold redundancy. Thus the term counts are `n!2^(n-1)` and
`4^(n-1)`. Dividing the full tensor norm ratios by these Waring upper
bounds gives `A_n` and `A_n^2`, so the conclusions for Waring rank, CP
rank, and their border ranks all follow. Real Waring decompositions here
allow signed scalar coefficients, as explicitly required for even degree.

## Authoring-agent SDP proof check

After writing, I read S-01--S-06 and S-08 in full. The Gram dual trace
argument, SVD comparison `S(A)>=||A||_*`, rank-sensitive dimension
reduction, and signability arguments all pass. S-05 was also checked by
exact SymPy rational arithmetic, exhaustive evaluation of 16 sign inputs,
and symbolic expansion of its SOS identity; output is in
`agent_sdp_checks_result.json`. S-07 is the same amplification as N-02,
which has now received this full-proof audit. The Banach-space dictionary
was checked against the explicit definitions: Q is epsilon on ell_1
factors, S is gamma_2^*, and the dual comparison is
`gamma_2<=pi_infinity<=K_G gamma_2`.

## Bound on claims about proof checking

The classical Grothendieck theorem, Banach theorem, CLL inequality,
Strassen decomposition, cited determinant rank bound, and numerical
constant records are used as literature. Source statements and their
applications were checked as described, but their entire original proofs
or large numerical certificates were not independently rerun in this
audit. Those events must not be recorded as formal verification or as a
fresh proof of the cited theorem.
