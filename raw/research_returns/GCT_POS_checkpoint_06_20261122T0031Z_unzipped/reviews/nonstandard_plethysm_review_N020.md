# Complete mathematical proof review of N-020

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS, with explicit computational scope.** Read all of
`sign_fibre_structure.tex`. The full actual-order basis/table and the
listed exact rank and trace identities are retained as the author's
and root's certified computational inputs. This review does not claim
an independent replay of the 12996-product table or ambient rank matrix.
It independently reconstructs every mathematical deduction from those
inputs, including the small cell table itself.

The polynomial two-dimensional model satisfies the actual-order relations
because it is generically conjugate to the certified GT model and has
entries in the torsion-free polynomial matrix ring. Thus specialization
does not invert D. Its generator images and products give the whole
matrix summand, and subtraction from the unit separates the scalar
summand, proving the stated surjectivity.

For x in ker Phi, the entire sequence Tr(L_x^m) vanishes by the regular
trace identity, since every power stays in the kernel. Newton's identities
through degree114 force characteristic polynomial t^114. Applying
Cayley–Hamilton to the identity gives x^114=0. The same holds for ax for
every a, so the geometric-series inverse of 1−ax gives exactly the
Jacobson-radical criterion. The reverse inclusion follows from the
semisimple quotient. This correctly uses the regular trace, not the
different ambient symmetrizing functional. The augmented-matrix rank
assertion implies the ambient kernel is inside this radical, hence the
ambient quotient has radical dimension109−59=50 and semisimple quotient5.

The displayed monic alternating-word reductions were algebraically
reconstructed. Generic polynomial independence follows from independence
after specialization: divide any alleged polynomial dependence by the
largest common power of D before reducing at zero. Thus the abstract
rank-three fibre and its inclusion have dimension10, independently of
the smaller ambient image.

At D=0, a²=b²=0 and ababa−babab=4(aba−bab). The correction
h1=ababa/4, h2=babab/4 converts the length-seven products into
16h1 and16h2; all sixteen entries of the displayed cell table agree
with the matrix images (4E12,16E11,16E22,16E21). The local identity
e=(h12+h21)/16 is therefore exact. The idempotent1−e annihilates the
cell, and its quotient image is (1,0), giving the asserted actual
semisimple section. No unwarranted ideal claim about the cell is made.

The weighted cyclic identity follows by expanding the threefold trace
against its monomial Gram matrix. The slot action R has order3; the
generator-swap permutation commutes with it and preserves the weights.
Word reversal induces the displayed reflection and conjugates R to R².
These verify the precise C3, C6 and D3 coefficient-tensor symmetries.

Finally, the proposed full-basis extension fails already at
(i,j,k)=(1,h12,h12): its left coefficient is1, while h12²=16h12 has
zero coefficient at pi(1), since pi fixes h12 and is injective. The
separate ambient-rank obstruction is also basis invariant. Both are
correctly scoped to the specified labels/functional, not to every
possible cyclic trace construction or to the unknown E(4) basis.

No primary-literature priority audit is claimed here; the author's
separate bounded audit supplies that part. The abstract fibre, ambient
image, and unspecified E(4) fibre remain explicitly distinct.
