# Compressed marked KOH trees: an actual binary-part witness rule

Author/checker: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Result and encoding convention

The known Pak–Panova–Swanson marked-tree rule can be encoded by polynomial-length natural witnesses for
\[
g((nk-r,r),(n^k),(n^k)),\qquad
n,k\ge1,\quad 0\le r\le nk/2,
\]
when the rectangular partitions are supplied as their explicit lists of k binary parts. The compression contracts the only potentially long chains in the source trees and records their lengths in binary. It is bijective, preserves every leaf and mark, and has a polynomial-time verifier that never expands a long chain.

The witness length is
\[
O\!\left(k^2\log(k+1)+k\log(nk+1)\right).
\tag{K0}
\]
This is polynomial in the explicit partition input length. It is not claimed polynomial in \(\log n+\log k+\log(r+1)\) when the rectangles themselves are compressed to two integers. Nor does it establish the old ordinary Ehrhart PH1: known two-row rectangular rays already fail that stronger property.

The PPS combinatorial interpretation is a known result. The run-compression, exact bijection, size proof and verifier below are the deductions checked in this note. No priority over previous encoding arguments is claimed, and no formal-kernel proof is claimed.

## 1. Exact primary source and version

Primary paper: Igor Pak, Greta Panova and Joshua P. Swanson,
*A combinatorial interpretation for certain plethysm and Kronecker coefficients*,
arXiv:2511.02312v3.

https://arxiv.org/abs/2511.02312v3
https://arxiv.org/pdf/2511.02312v3

The arXiv record lists v3 as revised 27 July 2026. Local PDF:
primary_sources/Pak_Panova_Swanson_trees_v3.pdf, SHA-256
613040c2ec259527bfe4b45e5b8f67fbd4a12b468fefc1428b38ebafa0a3f360.
Layout text SHA-256
391520d2e2ca63ab02df97988e57b700311cd4620f59c214b67d3c2c4ceb6cd8.

Exact v3 locators:

| Item | Locator |
|---|---|
| Two-row coefficient/partition-difference identity | Lemma 1.3, p.2 |
| Numerical dynamic-programming discussion | Section 2.2, p.5 |
| KOH local tree definition | Definition 3.2, p.6 |
| Leaf-product expansion | Proposition 3.4, p.6 |
| Integer marking inequalities | Lemma 4.2, p.9; Definition 4.4, p.10 |
| Exact count of the rectangular Kronecker coefficient | Theorem 4.5, p.10; also Theorem 1.1, p.1 |

The previously downloaded author-hosted 12-page PDF is the 4 November 2025 manuscript. The KOH local formulas are unchanged. The v3 proof of Lemma 4.2 corrects the earlier printed subscript to \(k_{t-1}\). The general plethysm trees are renamed GOS in v3; their extension is not needed for the KOH theorem here.

We use the published/source counting theorem as literature. This report does not claim an independent proof of the underlying KOH identity, the full O'Hara construction or the general GOS theorem.

## 2. Source objects in the exact form needed

A source KOH vertex has a label \((\mu,a,b)\), with \(a\ge0\), \(b\ge1\), and \(\mu\vdash b\). Leaves have \(b=1,\mu=(1)\). At a nonleaf, for each distinct part j of \(\mu\), in increasing j order, there is one child of type
\[
a_j=(a+2)j-2Q_j(\mu),\qquad
b_j=m_j(\mu),
\quad
Q_j(\mu)=\sum_s\min(j,\mu_s).
\tag{K1}
\]
All child a-values must be nonnegative. The root has type \((n,k)\).

Write the leaves in the prescribed depth-first order as \(a_1,\ldots,a_t\), and let
\[
\sigma=nk-\sum_{i=1}^t a_i.
\]
The source marks \(u_1,\ldots,u_t\) satisfy
\[
0=u_1\le\cdots\le u_t=r-\sigma/2,
\qquad
u_{i+1}-u_i\le
\min\left(\sum_{j\le i}a_j-2u_i,\ a_{i+1}\right).
\tag{K2}
\]
By PPS Theorem 4.5 the number of these marked trees is the coefficient in the opening statement.

## 3. The only nodes that can preserve b-mass

Call an internal node a repeat node if
\[
\mu=(1^b),\qquad b\ge2.
\]
Equation (K1) then gives one child with
\[
b'=b,\qquad a'=a-2(b-1).
\tag{K3}
\]

For every other internal node,
\[
\sum_j b_j=\sum_j m_j(\mu)=\ell(\mu)\le b-1,
\tag{K4}
\]
because a partition of b has b parts precisely when it is \((1^b)\).
Thus every internal node that is not a repeat strictly loses total b-mass among its children.

Contract every maximal consecutive run of repeat nodes. Its length is an integer h, and (K3) makes the whole run the single update
\[
(a,b)\longmapsto(a-2h(b-1),b).
\tag{K5}
\]
This update is valid exactly when its endpoint a-value is nonnegative: along the run a decreases by the fixed positive quantity \(2(b-1)\).

The surviving rooted tree, called the skeleton, contains only leaves and nonrepeat internal nodes. For each surviving node record the length h of the preceding contracted run on its incoming edge, including a possible initial run above the skeleton root. A leaf has b=1, so its incoming repeat count must be zero: a repeat run preserves b≥2 and therefore cannot itself end at a b=1 leaf.

## 4. Exact bijection and uniqueness

### Compression

Given any finite source tree:

1. Identify its repeat vertices by the partition test \(\mu=(1^b)\).
2. Delete each maximal run and record its length before the next surviving node.
3. Retain every surviving partition label, the ordered child relation and every leaf mark.

The root input and the surviving partition choices determine all a- and b-labels by (K1) and (K5). Deleting unary chains does not change the order of surviving children or the depth-first leaf order. Therefore it does not alter \(\sigma\) or any condition in (K2).

### Expansion

Conversely, take a skeleton with a nonnegative repeat count h before each node, and verify its recursive types as follows. Start at \((n,k)\). At a node of incoming type \((a,b)\):

- If b=1, require h=0, require a leaf labeled \(\mu=(1)\), and assign its leaf label a.
- If b≥2, first set \(\widetilde a=a-2h(b-1)\) and require \(\widetilde a\ge0\). Require the surviving partition \(\mu\vdash b\) to differ from \((1^b)\). Generate its children in the increasing order of the distinct j using (K1) with \(\widetilde a\), and require their a-values to be nonnegative.

Replace the recorded h by precisely h successive repeat vertices, whose a-values are
\(a,a-2(b-1),\ldots,a-2(h-1)(b-1)\), followed by the surviving vertex at \(\widetilde a\). This constructs one finite source tree. Every expanded label satisfies the source local rule. If the retained marks satisfy (K2), it is a source marked tree.

The expansion is unique. Its repeat chains have the recorded lengths and its surviving nodes are required to be nonrepeat, so all reconstructed chains are maximal. Compressing it returns the same skeleton and counts. Expanding the compression of an original tree recovers every original vertex label. Hence the two operations are mutually inverse.

The source tree has no unspecified child permutations: its children are ordered by increasing distinct part j. Fixing this order and the source depth-first leaf order prevents representation multiplicities from redundant serializations.

## 5. Skeleton size and arithmetic bit bounds

### At most k surviving vertices

Let the skeleton have h internal nodes and t leaves. Every leaf has b-value one. Summing
\[
b_v-\sum_{w\text{ child of }v} b_w
\]
over internal skeleton vertices telescopes to \(k-t\). By (K4) every summand is at least one. Thus
\[
h\le k-t,\qquad h+t\le k.
\tag{K6}
\]
This includes k=1, when the skeleton consists of a single leaf.

Each surviving partition is a partition of some b≤k; it has at most k parts, each at most k. An explicit part-list description therefore takes \(O(k\log(k+1))\) bits per node and \(O(k^2\log(k+1))\) bits in total.

### All numerical labels fit in logarithmic space

There is a direct useful identity behind the source's product bound. Put
\[
\beta(\mu)=\sum_{s\ge1}(s-1)\mu_s.
\]
Since the rows of \(\mu\) are decreasing,
\[
\sum_j m_j(\mu)Q_j(\mu)
=\sum_{r,s}\min(\mu_r,\mu_s)
=\sum_s(2s-1)\mu_s
=b+2\beta(\mu).
\]
Consequently (K1) gives
\[
\sum_j a_jb_j
=(a+2)b-2(b+2\beta(\mu))
=ab-4\beta(\mu)\le ab.
\tag{K7}
\]
All terms on the left are nonnegative in a valid tree. By induction every vertex obeys
\[
0\le ab\le nk.
\tag{K8}
\]
In particular every a-label and every leaf label is at most nk. The number of repeats in a contracted run satisfies
\[
0\le h\le \frac{a}{2(b-1)}\le nk,
\]
so it also has \(O(\log(nk+1))\) bits.

Repeated application of (K7) shows \(\sum_{\rm leaves}a_i\le nk\), hence \(\sigma\ge0\). From (K2), every mark is between zero and r≤nk/2. Thus all marks have \(O(\log(nk+1))\) bits.

There are at most k repeat counts and k marks. Tree punctuation and lengths use only \(O(k\log(k+1))\) more bits. These bounds prove (K0).

No numerical expansion of an n-sized integer, a long partition of b>k, or a run with h vertices is used.

## 6. A polynomial-time verifier and a precise #P conclusion

Choose one canonical binary serialization: prefix the number of skeleton nodes, list their records in preorder, list each partition in decreasing order using canonical binary integers, and append leaf marks in the fixed depth-first order. The record arities are determined by the distinct parts of the partition, so the tree parses uniquely. Require any fixed-length witness padding to be zero.

A verifier performs the following operations:

1. Parse the coefficient input and check it is an equal-rectangle/two-row instance with n,k≥1 and 0≤r≤nk/2.
2. Reject a skeleton with more than k vertices or any field exceeding the bounds above.
3. Starting at \((n,k)\), check (K5), the partition condition and every child type (K1), without expanding a run.
4. Require b=1 exactly at leaves, and require zero repeat count before a leaf.
5. Recover the ordered leaf labels, compute \(\sigma\), and test every integral marking condition (K2).

Every step uses only polynomially many operations on integers of polynomial bitlength. For clarity, the verifier may also reject whenever a derived type violates \(0\le ab\le nk\); (K7) proves no valid source tree is thereby lost. Input-invalid or size-invalid strings are simply rejected.

Under the explicit-list partition encoding, the input length L is at least k and contains the binary lengths of n and r. Hence (K0) is bounded by a fixed polynomial in L, and the verifier runs in polynomial time in L. Canonical serialization and the exact compression/expansion bijection give exactly one accepting witness per source marked tree. PPS Theorem 4.5 then proves
\[
g((nk-r,r),(n^k),(n^k))
=\#\{\text{accepted compressed witnesses}\}.
\tag{K9}
\]
Thus this restricted Kronecker counting problem belongs to #P for binary-encoded parts with explicitly listed rows. This is a natural witness rule obtained without first evaluating the coefficient.

The claim is not a polynomial-time algorithm for the coefficient: a polynomial-time witness test may still have exponentially many accepted witnesses. Nor is it a claim about a more compressed input consisting only of the binary integers n,k,r.

## 7. Why compression is necessary in the stated source format

There is already an exponential-length literal tree on the familiar two-by-two-factor parity ray.

Set \(n=2s\), \(k=2\), \(r=2s\), with s≥1. At b=2 the only partition choices are \((1,1)\) and \((2)\). Repeating \((1,1)\) j times reduces a from 2s to \(2s-2j\). Choosing \((2)\) then ends the tree in one leaf labeled
\[
a_{\rm leaf}=2(2s-2j)=4s-4j.
\]
Thus \(\sigma=4j\). A one-leaf marking has \(u_1=0\), and (K2) forces
\[
0=r-\sigma/2=2s-2j,
\]
so j=s. This is the unique marked source tree for the input.

It has s repeat vertices, one final \((2)\)-vertex and one leaf: s+2 vertices in all. Its explicit tree encoding has length \(\Omega(s)\), while the three partition inputs \((2s,2s)\) have total bitlength \(O(\log s)\). Merely saying that the source local checks are efficient does not provide polynomial-length binary witnesses.

Its compressed skeleton has two vertices and repeat count s, so it has \(O(\log s)\) bits and passes the verifier. The compression gives a concrete repair in the exact source objects. It also recovers the known coefficient value one on this even parity ray; it is not a new formula for that value.

## 8. Limits: plethysm encoding and PH1 are separate

The equal-rectangle input explicitly lists k rows, which is essential to the bound in (K0). The related plethysm coefficient
\(a^\lambda_{(n),(k)}\) can have both one-row arguments given in only \(O(\log n+\log k)\) bits. The same O(poly(k,log n)) witness bound is then not automatically polynomial in its input length. In fact the separate report agent_plethysm_dimension_gate.md gives an explicit output-length obstruction for the wholly binary plethysm convention. No analogous #P claim is made here for that convention.

The known rule also does not supply ordinary Ehrhart PH1. The skeleton is a discrete variable, the local partition choices vary with it, and the recursions include fixed offsets. The verifier has not produced one fixed bounded rational polytope whose integral dilation counts all stretched inputs, let alone VI's specified dimension and separation properties.

This distinction has an actual known counterexample in the same broad family: Kahle–Michałek, EJC 25(1) (2018), P1.41, Theorem 5 and Remark 6, p.4, together with the rectangular identification on p.6, give a two-row/equal-rectangle stretching ray that is not an ordinary Ehrhart function. The PPS rule still counts positive objects on that ray, and (K9) still supplies short witnesses in the explicit-row encoding. Therefore the failure to infer old PH1 from the tree rule is substantive, not merely lack of an implementation.

No claim is made about canonical bases, nonstandard structure constants, a theta lift, multiplicity-free restriction, or an orbit-closure obstruction. The achieved gate is a verified positive combinatorial witness rule for this actual restricted rectangular Kronecker family.

## 9. Proof-check record

Read directly: v3 Section 2.2, Definition 3.2, Remark 3.3, Proposition 3.4, Lemma 4.2, Definition 4.4 and Theorem 4.5, with comparison to the initial author manuscript where relevant.

Fully proved in this note: classification of b-preserving nodes, exact compression and unique expansion, the telescoping node bound, energy identity (K7), all numerical and partition bit bounds, polynomial verification, uniqueness of accepted strings, the literal-tree lower-length example, and the precise encoding limits.

Cited as known: the KOH identity and PPS's equality between marked trees and the representation-theoretic coefficient; Kahle–Michałek's prior ordinary-Ehrhart obstruction. These cited complete research proofs were not independently certified here. A fresh independent review of the present deductions is requested separately.

