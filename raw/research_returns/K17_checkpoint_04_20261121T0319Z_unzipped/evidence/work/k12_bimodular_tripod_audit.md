# Independent audit: rank-ten bimodular orientation pruning

Agent: /root/tripod_integral. Model: GPT-6 Astra Pro. Reasoning effort not exposed.
Date: 2026-11-21 UTC. Verdict: PASS for the precise restricted statement in
`work/k12_bimodular_attempt.md`.

I read the entire candidate and reconstructed all its lattice and
orientation steps. The hypothesis is a complete set of thirteen
minimal-vector pairs in a rank-ten lattice, generation of that lattice by
the minima, and maximal ten-vector index at most two. The result does
not establish the full rank-ten Voronoi homology vanishing.

The Smith-normal-form gcd formula makes the gcd of maximal minors one.
As their nonzero absolute values are only one or two, a determinant-one
minor must occur. Its columns give a genuine lattice basis, so V=[I A]
and B=[−A^t I_3] is an integral basis of the full relation lattice.
Complementary maximal minors agree up to sign. Thus B is rank-three
bimodular with the exact full-size-minor hypothesis needed by the source.

I freshly read the definitions on pp.1 and 3 and Theorem 1 on p.4 of
Lee–Paat–Stallknecht–Xu, *Polynomial upper bounds on the number of
differing columns of Delta-modular integer programs*, arXiv:2105.08160v5,
16 November 2022, primary URL https://arxiv.org/pdf/2105.08160v5 .
Local source: `work/k12_source_data/lee_paat_stallknecht_xu_2022.pdf`
and its extracted text. The direct web open returned DisabledError, so
the exact primary text was read locally. “Differing” means unequal up
to sign, excluding zero; nonprimitive columns are permitted. Delta(A)
bounds maximal minors, not all square minors. The theorem states
c(2,m)=(m^2+m)/2+m for every positive m, giving c(2,3)=9.
I use this published theorem as an input; I do not claim an independent
read of every proof lemma of that source.

Thirteen columns with at most nine nonzero signed classes force either
two zero columns or an equal signed pair. After a legal vector-sign
change, their transposition fixes every row of B and hence the full
relation lattice pointwise. It descends to an integral involution on
the lattice, preserving the complete set of minimal rays.

The orientation proof correctly avoids any unproved simpliciality
assumption. The real coordinate permutation has a one-dimensional
negative eigenspace. Its image in the quadratic span is the nonzero
difference v_i v_i^t−v_j v_j^t. It is nonzero because equality of these
rank-one forms would give v_i=±v_j, contrary to the distinct pairs.
Since real C_2 representations are semisimple, the quotient quadratic
span has exactly one negative eigenvalue. Its determinant is −1;
the fixed positive radial direction does not change this sign on the
projective cell.

No gap was found. The proof does not cover a proper generated
sublattice, larger indices, or more than thirteen minimal-vector pairs.
The separate glue argument is reviewed in its own record.
