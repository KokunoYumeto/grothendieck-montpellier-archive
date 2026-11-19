# Finite exterior tests and the universal trait endpoint

Written and audited on 19 November 2026 after checkpoint 08.
The complete proof is in part_c/c4_exterior_trait_criterion.tex.
This is an exact equivalence and a finite witness construction, not a proof
of geometric weight–monodromy or a claim of a smaller unresolved universal gate.

## Proof checkpoints

We construct homogeneous Jordan strings by the graded spaces
\(K_L=\ker N\cap\operatorname{im}N^{L-1}\). Complements of \(K_{L+1}\) in
\(K_L\), and homogeneous lifts of their bases, give independent strings;
the rank-difference identity proves that they exhaust the whole module.
No Frobenius-stable choice of an individual string and no Frobenius
semisimplicity are assumed.

The full ordinary exterior product of a length-\(L\) string of centre \(c\)
is a nonzero vector in \(\ker N\) of weight \(Lc\). The finite family of
exterior invariant bounds makes all centres at most the proposed centre.
The determinant weight makes their length-weighted average exactly that
centre, so each equals it. The converse is proved directly using the
lowering/raising commutator: a lowest vector of Cartan weight \(a\), with
maximal nonzero raising iterate \(e^t z\), satisfies \(a=-t\leq0\).

For geometric degree \(j\), the nonzero terms in the Rapoport–Zink row
satisfy \(b\geq2s\geq\max(0,2b-2j)\), hence \(0\leq b\leq2j\).
Monodromy lowers weights by two, so \(N^{j+1}=0\).
On a \(j\)-fold, the product of \(r\) copies is an \(rj\)-fold and its
middle cohomology contains the required ordinary exterior power. The
geometric permutation projector is antisymmetric for even \(j\) and
symmetric for odd \(j\); the formula includes the Koszul factor explicitly.
No Chow–Künneth projector is needed for this cohomological direct-summand
statement.

The first draft incorrectly compressed the semistable-model transfer by
putting finitely many choices over a common further extension. Both C and D
identified the missing ramified-base-change argument. The repaired proof
uses one field \(L_r\) for each power and transports each invariant bound
back to a fixed field over which the original representation is already
unipotent. It makes no assertion that ramified base change preserves
regularity of a semistable integral model.

The reduction from arbitrary cohomological degree to middle degree uses
an actual split cohomological weak-Lefschetz inclusion, with retraction
\((L^{n-j})^{-1}i_*\), or a projective-space padding when \(n<j\).
Purity is transferred only through a direct summand, not through an
arbitrary subrepresentation.

## Exact formal diagnostic

The example over \(K=\mathbf Q_2\), with coefficient field \(\mathbf Q_3\),
has Frobenius weights \(6,4,4,2\) and two length-two strings of centres
\(5,3\). Its invariant weights are \(4,2\), and it has determinant weight
\(16\) and the required symmetric pairing, yet it is not pure of weight
\(4\). Its second exterior power has a nonzero invariant of weight \(10\),
exceeding \(8\). The exact code and output are:

- code/part_c/check_c4_exterior_witness.py;
- code/part_c/check_c4_exterior_witness_output.json.

The certificate checks the Frobenius-monodromy relation, the pairing,
nilpotence, ranks, and the induced exterior map. No geometric realization
of this representation is asserted.

## Literature and audit scope

A primary-focused search used “weight monodromy exterior powers criterion”,
“Weil Deligne exterior power pure kernel monodromy”, and “monodromy
determinant Jordan weights purity”. It located Taylor and Yoshida,
*Compatibility of local and global Langlands correspondences*, whose
Lemma 1.4(1), (2), (5), in the opened author version, pp. 6–7, records
related purity, finite-extension and determinant arguments. We read the
complete lemma and proof, and its preceding Weil–Deligne definitions.
We do not claim novelty or identify the paper's automorphic theorem with
the geometric universal conjecture. The source is retained as
part_c/sources/taylor_yoshida2006_author.pdf with the SHA256 acquisition
manifest in code/part_c/fetch_taylor_yoshida_source_output.json.

D read every line of the repaired fragment and independently passed its
mathematical proof. D did not claim to have independently opened
Taylor–Yoshida in that audit. Root read the complete repaired fragment;
the reception was recorded at the clock-confirmed 08:57–08:58 UTC, after
correcting an earlier estimated timestamp. Owner, root and D all retain
the trait-only scope and the universal incomplete status.
