# K17: direct orientation attack on the remaining K12 cells

Date: 2026-11-21 UTC. /root/vandiver_k, GPT-6 Astra Pro.
Reasoning effort not exposed. Status: checked restricted lemmas and
explicit remaining classification gates; no full chain vanishing.

## 1. Exact cell dimension and the data actually available

DEKM, current author PDF, §1.2.1 pp.3--4, defines X_N^* as the quotient
of the positive semidefinite cone by positive homotheties, and Σ_j as
projective cells of dimension j. Definition 2.1 p.6 defines perfection
rank r as dim span{v v^t}. Thus a degree-twelve projective cell has
perfection rank thirteen. Its number s of minimal-vector pairs need
not be silently identified with r.

Table 3 p.14, and the exact repository snapshot, have the following
configuration counts indexed by perfection rank:

| lattice rank | perfection ranks and known counts |
| --- | --- |
| 8 | r=8:13; r=9:106; r=10:783; r=11:6167; r=12:50645 |
| 9 | r=9:44; r=10:759; r=11:13437; r=12:unknown |
| 10 | r=10:283; r=11:16062; r=12:unknown |

Table 4 p.15 repeats those counts with an indexing convention that
must be handled carefully: its initial thirteen rank-eight objects
have eight independent minimal-vector pairs, hence projective dimension
seven by §1.2.1. The explicit homology theorem and rank spectral-sequence
reduction are kept as their quoted source statements; no extra
chain-degree vanishing is inferred from that table or a filename.

Theorem 2.5 p.7 proves s=r under the assumption s<=N+5. It does not
state the converse implication from a small value of r-N. Section 3.3
p.13 explicitly says simpliciality is established for r=N+1,N+2 and
expected, but not established there, for r=N+3,N+4. These latter values
are precisely r=13 at N=10 and N=9. A general argument must therefore
handle this issue rather than assume thirteen minimal-vector pairs.

Importantly, §3.3 gives a direct low-rank enumeration procedure: a
rank-r configuration contains a rank-(r-2) configuration and two
rank-(r-1) configurations extending it; enumerate their incidence
orbits and test unions for realizability. This bypasses enumerating
all 2,237,251,040 rank-nine perfect forms. It still requires new,
complete rank-twelve and rank-thirteen low-rank configuration data.

## 2. A decomposition lemma that is valid but not exhaustive

Suppose the minimal class is a direct sum C' + Z + Z, with the two
rank-one factors having the common minimal norm. The integral map
interchanging the two factors fixes every other minimal-vector ray
and interchanges their two rank-one quadratic forms. The span of
these two forms is a direct summand of the span of all the rank-one
forms. Hence this map has determinant -1 on that span. It preserves
the radial direction positively, so reverses the orientation of the
projective cell as well. Such a cell contributes zero to the localized
Voronoi chain group since 2 is a unit in R.

A single extra Z factor does not give this conclusion: changing its
sign fixes its quadratic ray and is orientation preserving on the
cell. Nor does small perfection excess force two rank-one factors.
For N>=5 the lattice Z^N+Z(1/2,...,1/2), with the standard Euclidean
norm, has exactly the minimal vectors ±e_i and perfection rank N,
but the support of its glue code is all N coordinates. It is primitive
in DEKM's minimal-class extension sense (§2.2.2). Its actual
coordinate permutations do give orientation reversers, but that is
an additional symmetry argument, not a decomposition conclusion.

## 3. The maximal-index-one cells can all be removed

### 3.1 Quadratic independence for a simple unimodular system

Lemma. Let V=[v_1 ... v_s] be a full-row-rank totally unimodular
integer matrix, with nonzero columns distinct up to sign. Then the
quadratic forms v_i v_i^t are linearly independent over the real numbers.

Proof. First, the reduced columns vbar_i in F_2^N are nonzero and
distinct. A nonzero TU column has an entry ±1, so is nonzero modulo
two. If two columns agree modulo two, they have the same support.
If their signs do not agree up to one common sign, two rows give a
two-by-two minor ±2, contradicting total unimodularity. Thus agreement
modulo two would make them equal up to sign.

Suppose sum_i a_i v_i v_i^t=0, with a_i real. For a binary row vector
b in F_2^N, call C(b)={i:b vbar_i=1} its cut. Consider a minimal
nonempty cut C, meaning there is no smaller nonempty cut contained
in it. The complementary column set has binary rank exactly N-1.
Its rank is at most N-1 since b annihilates it. If its rank were at
most N-2, adjoining one column from C would still span a proper
subspace; a nonzero functional annihilating that larger subspace
would give a nonempty proper subcut of C, a contradiction.

Total unimodularity makes the rank of every column subset the same
over Q and F_2. Choose N-1 complementary columns spanning that
hyperplane and one column from C. They form a unimodular basis.
Let φ be the integral linear functional zero on the first N-1 basis
vectors and one on the last. Expressing any column in this basis
uses only coefficients 0,±1, by the maximal-minor formula. The
functional φ is zero precisely off C and is ±1 on C: a column of C
is outside the binary hyperplane and hence outside its rational lift.
Applying the quadratic relation to φ gives sum_(i in C) a_i=0.

Every nonempty cut is a disjoint union of minimal nonempty cuts.
Indeed, subtract a minimal cut contained in it in the binary row
space; this removes that support, and repeat. Hence sum_(i in C(b))
a_i=0 for every b. Equivalently,

    sum_i a_i - sum_i a_i (-1)^(b vbar_i) = 0 for every b in F_2^N.

Multiply by (-1)^(b vbar_j) and sum over b. The distinct nonzero
binary columns give distinct nonconstant characters, so orthogonality
yields -2^N a_j=0. Every a_j is zero, proving the lemma.

This proof uses only integer minors, binary linear algebra, and the
finite character orthogonality identity; no unproved simpliciality
assertion for general nonunimodular configurations is used.

### 3.2 An orientation-reversing integral involution

Lemma. Let v_1,...,v_s in a rank-N lattice Λ be representatives of
the complete set of distinct minimal-vector pairs defining a
well-rounded cell. Suppose:

1. every linearly independent N-subset is a Z-basis of Λ;
2. with c=s-N, one has s>c(c+1)/2+1.

Then the associated cell has an orientation-reversing element of
GL(Λ). In particular this kills every maximal-index-one
degree-twelve cell at N=9 and N=10: the preceding lemma gives
s=r=13, and c=4 or c=3.

Proof. In a basis chosen among the v_i, the matrix V of the vectors
is [I_N A]. Assumption 1 implies every square minor of A is 0 or ±1,
by completing it with identity columns to an N-by-N minor. Therefore
V is totally unimodular. Its integral relation lattice is the row
lattice of B=[-A^t I_c]; this matrix is totally unimodular too, by
transposition and the same complementary-minor argument.

Heller's bound says that a rank-c unimodular column system has at
most c(c+1)/2 distinct nonzero column directions. Here parallel
primitive columns are equal up to sign. If B has at most one zero
column, assumption 2 forces two nonzero columns equal up to sign.
After changing the sign of one v_i if necessary, these two B columns
are equal. The coordinate transposition P interchanging them fixes
every row of B. It consequently preserves ker(V:Z^s->Λ) and descends
to an integral involution g of Λ. It exchanges v_i,v_j and fixes
every other v_k, up to the harmless sign choices.

If B has at least two zero columns, interchange any two of them;
the same proof applies. In both cases g interchanges exactly two
quadratic rays and fixes all the others. The quadratic-independence
lemma makes these forms a basis of their span, so the determinant is -1. Removing the
positive radial direction preserves this sign, proving the lemma.

Heller source: I. Heller, *On linear systems with integral valued
solutions*, Pacific J. Math. 7 (1957), 1351--1364, Theorem (4.2)
and its complete proof, pp.1358--1360. The theorem bounds the signed
Dantzig set by c(c+1), so the bound on directions is half that value.
Its lattice interpretation is stated in §6 p.1364. Primary PDF:
https://msp.org/pjm/1957/7-3/pjm-v7-n3-p07-p.pdf . The full proof
of (4.2), including the projection lemma and the minimal-dependence
argument, was read for this check. The rest of the lemma above was
reconstructed directly by integral linear algebra.

## 4. Why this does not prove the full two-rank vanishing

Hypothesis 1 has not been established for all target configurations;
in fact nontrivial index codes occur already among
the known perfection-rank-N cells (DEKM Table 2). A permutation of
minimal-vector rays need not preserve an overlattice.

This last obstruction is explicit. In dimension N>=6, let
Λ=Z^N+Z((e_1+...+e_5)/2), with the standard Euclidean norm. Its
minimal vectors are exactly ±e_i: every nonintegral vector has at
least five half-integral coordinates, hence squared norm at least
5/4. Interchanging e_1 and e_6 permutes those minimal-vector rays,
but does not preserve Λ, since it changes the unique nonzero glue
coset. Thus a rational series-pair permutation cannot be treated as
an integral stabilizer without checking the actual index code.
This is an obstruction to that inference, not a counterexample to
orientation vanishing; other coordinate transpositions stabilize
this example.

The lemma can prune a future low-rank enumeration. It
removes every maximal-index-one cell, but does not remove the
nonunimodular or potentially nonsimplicial
configurations, and no complete list of the remaining cases has
been produced. No K12 vanishing follows here.

## Actual check status

The decomposition, quadratic-independence, and unimodular involution
lemmas have complete proofs above and were read back. The entire relevant DEKM §2.1,
§2.2.2, §3.3, Tables 3--4 and the definitions were checked. The
ordinary lattice counterexample to automatic code preservation was
verified directly by its coset coordinates and Euclidean norm.
There is no claim of a new exhaustive cell enumeration.
