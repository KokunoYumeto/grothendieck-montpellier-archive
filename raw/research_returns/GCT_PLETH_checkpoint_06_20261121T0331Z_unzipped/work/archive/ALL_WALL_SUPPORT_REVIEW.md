# Independent complete audit of outer-five support

Statement **A-060**, reviewing G-031,
`work/root/all_five_row_support_report.md`, all NW.1–NW.8,
every section and all 344 catalog rows, the graph algorithm,
the fixed evaluator and its full data index.
Checked 21 November 2026 by GPT-6 Astra Pro,
run `/root/archive_audit`; effort setting not exposed.

**Complete proof PASS.** An independent reconstruction of every
finite field in the graph also passes. The finite proof of
exhaustion handles the interaction of both stable end axes;
it does not require normalization to commute with increments.
The resulting support decision covers every outer partition
of five and every output partition.

## 1. Actual normalization maps and their signs

Removing \(d=\lambda_5\) full columns uses the determinant
factor and carries the balanced permutation action to the
effective label \(\mu\) or \(\mu^t\) according to
the parity of \(d\). For gaps \(g=(a,b,c,e)\), the
normalized shape and inner degree are exactly NW.4.

Its second-row excess is
\[
\lambda_2^0-n_0=(-a+3b+2c+e)/5.
\]
Thus the first stability inequality is the exact order-zero
region of G-027. Its full section module is
\(\operatorname{sgn}^{b+c+e}
S_{(b+c+e,b+c,b)}\mathfrak h_5\), independently of \(a\).
Increasing \(a\) by five increases the first row by five and
the inner degree by one. Multiplication by
\(u=\prod_iX_{i1}\), together with the common section-space
identification, is the actual isomorphism in this direction.
In particular steps of ten preserve the whole multiplicity vector.

The exterior-column perfect pairing in width
\(H=a+b+c+e\) sends the balanced module to the dual of
the reversed-gap module, with sign \(\operatorname{sgn}^H\).
Its first stability condition is
\(e\ge a+2b+3c\). A step of ten in \(e\) is two
first-axis steps for that complementary shape and changes
\(H\) by an even number. It therefore preserves every
original outer label. A step of five changes the determinant
sign; the report correctly retains ten in its normalizer.

The lower bound one preserves a positive one-axis support
coordinate. Subtracting multiples of ten leaves the face and
weighted congruence unchanged, and each such subtraction is
the inverse of the stated stable isomorphism. Adding the two
stability inequalities forces \(b=c=0\) and \(a=e\).
Thus the only double-axis case is precisely the diagonal case
treated in the proof.

## 2. Independent proof of the finite seed and monoid bounds

On a fixed proper nonempty support, write each positive gap
as \(1+p_i+2t_i\). A componentwise minimal solution
\(u\le t\) to the weighted congruence has total at most
four: any five indexed weights have six prefix sums modulo five,
so two coincide and give a nonempty zero-sum subvector. Removing
it preserves the congruence and contradicts minimality.

An indecomposable nonzero solution of the homogeneous congruence
has total at most five. For a longer vector, the same argument
applied to five of its weights gives a proper nonempty zero-sum
subvector, hence a decomposition. Recursive subtraction gives
generation by all the minimal solutions in this bounded range.

These arguments prove the completeness of the finite enumeration,
not merely its agreement with sampled inputs. My independent
loops recover all **172** parity-minimal seeds and all **58**
face-specific generators over the fourteen supports. For a
generator \(h\), the partition
\(\eta_i=\sum_{j\ge i}h_j\) has size divisible by five.
G-024's explicitly constructed invariant section of weight
\(2\eta\) therefore gives the actual embedding for
\(g\mapsto g+2h\). It preserves each outer multiplicity,
so a fully positive point remains fully positive along every
subsequent generator path.

## 3. Independent proof of exhaustion, including both axes

A deficient input reached from a seed cannot have passed through
a fully positive point, by the preceding embeddings. A deficient
normalized point is a retained node. Every unnormalized preimage
is either that node or a point on one of its stable ten-step rays.

Suppose the current input is \(z+10q e_j\), where \(z\)
is a retained node and \(j\) is one of its stable axes. After
adding \(2h\), it becomes \(w+10q e_j\), with
\(w=z+2h\). The threshold deficit grows by at most
\(2\cdot3\cdot|h|\le30\). Thus all unstable initial
values have \(q<Q\), with exactly the cutoff NW.7 and
\(Q\le3\). Every such value and the endpoint \(q=Q\)
are literally among the saved ray checks.

For \(q\ge Q\), the chosen axis remains stable and its
threshold depends only on the fixed other coordinates. Its
residue modulo ten is unchanged. The other stable axis can
also apply only at \(b=c=0,a=e\). At that tie, the
priority normalization fixes the vector. Every subsequent step
in either original direction normalizes back to it. Therefore
the normal form is constant for the entire remaining ray,
including the priority-switch endpoint. This is a direct proof
of the needed infinite statement; the finite next-step assertion
in the code agrees with it.

Every point or ray transition consequently either exits to full
positivity or reaches another retained deficient node. Induction
along the finite generator decomposition proves that every
deficient input is a retained point or stable-ray point. Conversely
every retained point has a deficient vector, and the actual
stable isomorphisms give the same vector on its rays. Thus the
normal-form table is exactly the deficient set. Its individual
zero labels, after determinant conversion, prove NW.3.

This independent reasoning was completed before reading the
parent's finished proof. The entire finished NW.1–NW.8 proof,
including the equality discussion and converse, was then read
and agrees in every step.

## 4. Complete independent finite character reconstruction

`check_all_wall_support_independent.py` uses an independent
enumeration of seeds and generators, then reconstructs the full
queue and every bounded ray transition. Its character engine
uses integer single-cycle Jacobi–Trudi determinants and two-cycle
Jacobi–Trudi interpolation over \(\mathbf F_{257}\), rather
than the root's residue/Laurent closed formulas.

For the larger shapes, the explicit determinant-complement map
reduces the inner degree, with its exact permutation sign.
Original degrees reach 67; the smaller complementary degree
never exceeds 22. Thus the interpolation degrees are at most
44, below 257. The already proved two-double-cycle bound
\(n+1\le23\) and three-two-cycle bound 10 make centered
residue reconstruction unique. The first bound follows from the
two rank-two Schur factors after the even/odd alternant split;
the second from the ten possible three/two alternant selections.
These bounds were audited with the earlier G-025 proof and are
used only to certify exact integer recovery here.

Every trace and multiplicity field agrees. The executed totals
are:

| Quantity | Independent checks |
|---|---:|
| Proper nonempty supports | 14 |
| Seeds | 172 |
| Face-specific generators | 58 |
| Deficient nodes | 344 |
| Point transitions | 1896 |
| Bounded ray cases | 2084 |
| Raw/normalized class equalities | 27860 |
| Distinct gap vectors evaluated | 2414 |
| Distinct class traces evaluated | 16898 |

The root's 2218 distinct normalized evaluated vectors also agree
with the union of its seed, node and target fields. The larger
independent count includes every raw target as well. The complete
receipt, per-face counts, arithmetic scope and hashes are in
`ALL_WALL_SUPPORT_INDEPENDENT_RECEIPT.json`.

## 5. Printed catalog, evaluator and every remaining case

The full manuscript catalog was read and then independently
parsed. Every one of its **344** rows has exactly the zero
labels and stable axes of the verified graph. Every full TSV
row and every JSON index row also agrees. The statistics are
158 isolated points and 196 ray bases, counting both directions
at double-axis nodes.

`check_all_wall_catalog_independent.py` verifies the actual
evaluator on all 2414 audited vectors with both determinant
parities: **33796** support entries pass, and all **7560**
entries for which it returns exact multiplicities agree. A
further **42** determinant and excess-length entries pass.
The complete receipt is `ALL_WALL_CATALOG_INDEPENDENT_RECEIPT.json`.

The zero gap vector is the actual determinant line and gives
only the effective trivial outer label, including degree zero.
The strict positive-gap rule is exactly the previously completely
audited G-028 rule and has the stated two ray families and two
additional trivial-label exceptions. For length greater than
five, the Young projector inclusion into five symmetric factors
and repeated Pieri force the coefficient to zero. These three
cases and the fourteen proper nonempty supports partition every
input, so the decision is complete.

The lookup and a fixed number of arithmetic operations give a
bounded arithmetic-operation count and polynomial bit cost.
The procedure asserts support everywhere and exact multiplicities
on its catalog preimages; it does not claim that every positive
coefficient outside the catalog equals a catalog value. The
subsequent canonical-rank comparison uses the exact previously
audited R-031 law with the correct source/target order.
