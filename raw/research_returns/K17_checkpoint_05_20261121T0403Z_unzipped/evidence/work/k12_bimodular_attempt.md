# K17: a further rank-ten orientation pruning at maximal index two

Date: 2026-11-21 UTC. /root/vandiver_k, GPT-6 Astra Pro.
Reasoning effort not exposed. Status: independently audited restricted
deduction; see `k12_bimodular_tripod_audit.md`, 2026-11-21;
no exhaustive classification and no full K12 vanishing.

## Statement

Let Λ be a rank-ten lattice whose complete minimal-vector set consists
of thirteen pairs ±v_1,...,±v_13. Assume these vectors generate Λ and
every independent ten of them generate a sublattice of index at most
two. Then their Voronoi cell has an orientation-reversing element of
GL(Λ). In particular this removes the thirteen-pair, minimum-generated,
maximal-index-two portion of the remaining rank-ten target cells.

The assumption that the minimal vectors generate the full lattice is
substantive. Also, this statement does not assert that every target
rank-ten cell has exactly thirteen minimal-vector pairs.

## Proof

Write V for the 10-by-13 integral matrix of the vectors in a basis of Λ.
The gcd of its maximal minors is the index of their generated lattice,
which is one by assumption. Since every nonzero maximal minor is ±1
or ±2, at least one is ±1. Use the corresponding ten minimal vectors
as a lattice basis; after reordering, V=[I_10 A]. The relation lattice
ker(V:Z^13->Λ) is the row lattice of the rank-three integral matrix

    B=[-A^t I_3].

Every 3-by-3 minor of B is, up to sign, a complementary 10-by-10
minor of V. Thus B is bimodular: its maximal minors have absolute
value at most two.

Lee--Paat--Stallknecht--Xu, Theorem 1, gives at most

    c(2,3)=(3^2+3)/2+3=9

nonzero columns distinct up to sign in a rank-three bimodular matrix.
Their definition of "differing" is equality up to sign, not equality
up to arbitrary rational scaling, and their bound includes nonprimitive
columns. Since B has thirteen columns, it therefore has either two
zero columns or two nonzero columns equal up to sign. Change one
vector sign if needed so that the latter pair is equal, and let P
be the coordinate transposition exchanging the selected two columns.
Then BP=B, so P fixes the relation lattice pointwise. It descends
to an integral involution g on Λ and exchanges exactly two
minimal-vector rays while fixing all other rays.

This reverses the orientation even without assuming that all thirteen
quadratic forms are independent. Indeed, the permutation module R^13
has a one-dimensional negative eigenspace spanned by e_i-e_j. Its
equivariant image in the real quadratic span is
v_i v_i^t-v_j v_j^t, which is nonzero because the two minimal-vector
pairs are distinct. Therefore the quadratic span has exactly one
negative eigendirection. The remaining eigendirections have eigenvalue
one, so the determinant is -1. The positive radial direction is fixed,
and the same orientation sign holds on the projective cell. This proves
the claim.

## Primary bound and exact reading scope

J. Lee, J. Paat, I. Stallknecht, L. Xu, *Polynomial upper bounds on
the number of differing columns of Δ-modular integer programs*,
arXiv:2105.08160v5, 16 November 2022:
https://arxiv.org/pdf/2105.08160 .

- Definition of differing columns: p.3, a!=±a', excluding zero.
- Theorem 1: p.4, c(2,m)=(m²+m)/2+m for every positive m.
- Full top-level proof of Theorem 1: §4, pp.17--19, with cases for
  primitive and nonprimitive columns.

The definition, theorem statement, and complete §4 proof were read.
That proof invokes earlier combinatorial lemmas; those have not all
been independently re-proved in this run. The bound is cited as known
background, rather than claimed as a newly audited proof of the full
26-page paper. The complete lattice deduction above was read back
and independently reconstructed.

The older Oxley--Walsh sufficiently-large-rank theorem should not be
substituted for this bound at rank three. Their introductory summary
also hides exceptional small ranks in the primitive-column variant;
the precise Lee et al. theorem above is the appropriate statement.

## Residual cases

This lemma does not cover a maximal-index-two lattice for which the
minimal vectors generate an index-two sublattice. In that situation
the same transposition can act on the generated sublattice without
preserving the additional glue coset, exactly the issue demonstrated
in `k12_orientation_attempt.md`.

For rank nine and thirteen minimal-vector pairs, the analogous relation
matrix has rank four. The numerical bound is c(2,4)=14, so thirteen
columns do not force a repeated signed pair. That case remains open
in this attack. Larger indices and potentially larger numbers of
minimal-vector pairs also remain.
