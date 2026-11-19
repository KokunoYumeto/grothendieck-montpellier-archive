# Independent check of the finite pure-even Chow criterion

19 November 2026. We read `part_c/c1_finite_even_criterion.tex` in
full before integration. The argument passes with its stated
pure-even and characteristic-zero hypotheses. This is not an audit
of a mixed-parity extension, which remains explicitly unproved.

1. Set A=H*(X,Q) with ordinary symmetry, and retain the Tate object
   L=Q(-1). The five structure tensors have the displayed types in
   the draft: in particular the point and inverse pairing lie in
   A⊗L^(-n) and A⊗A⊗L^(-n), while the trace lies in A∨⊗L^n.
2. The GL(A)×G_m orbit closure of the rational tensor tuple has a
   rational ideal obtained by elimination after inverting the
   determinant and the second scalar. Finite generators can be
   closed inside a bounded-degree space to obtain a finite stable
   subspace E generating the ideal.
3. The group GL(A)×G_m is reductive over Q. Its defining faithful
   representation A⊕L generates all rational representations by
   mixed tensors and subquotients; semisimplicity turns the latter
   into split summands. The source checked independently is Milne,
   Algebraic Groups (2022), Theorem4.14 pp88--89 and Theorem22.42
   pp478--479, with complete proofs. Remark12.53(a)p248 extends
   this to locally finite infinite-dimensional rational modules,
   so exact invariants applies to E⊗Q[W]→I as used in the proof.
4. The inclusion E→Q[W] is the canonical covariant p_E with
   target E∨. If F is any target-valued equivariant polynomial
   vanishing at the tensor tuple, its coefficients lie in I.
   Exact invariants lifts F to T'⊗E⊗Q[W]; contraction against p_E
   recovers F. A split mixed-tensor embedding of E∨ lets this be
   expressed with finitely many ordinary tensor covariants. No
   reductivity of the stabilizer of the point is needed.
5. We opened Procesi, arXiv:2011.10820v3, Theorems1.2--1.5 pp4--5.
   These are the classical vector/covector FFT and its determinantal
   or antisymmetrizer SFT. Polarizing the coordinates of arbitrary
   tensor variables reduces the draft's covariants to exactly
   those mixed tensor statements. One does not need to substitute
   arbitrary tensors for matrix variables in the paper's different
   main theorem. The scalar A-loop is the categorical dimension d;
   the L-loop and one-dimensional symmetry are automatic for the
   actual invertible even Tate object.
6. Necessity of the two geometric identities in condition(i) follows
   from Δ·o_1=o_1o_2 and Δ²=d o_1o_2. Pushing the latter along a
   projection gives c_n(T_X)=d o. The antisymmetrizer is a sum of
   permutation-graph cycles in the permitted ring on X^(2d+2).
7. After these two identities, a connected Frobenius diagram is a
   small diagonal with handles and point insertions. A handle
   contributes c_n(T_X)=d o. Any two point insertions vanish for
   n>0; one is pushed to an external product of point classes
   using Δ_*o=o⊠o. Closed components reduce to their scalar
   degree. Thus arbitrary diagram identities reduce to the
   requested pointed-partition ring relations. This validates the
   reverse implication; it is not merely a sufficient criterion
   in a larger, unexplained category.

The result is a finite construction of cycle conditions, not an
algorithm deciding rational equivalence. Its rational orbit-ideal
data are computable from a supplied rational cup-product table. We
found no remaining gap in the stated theorem.

The auxiliary comparison with Meir2023 was also checked. His
Theorem1.2 assumes that the structure-tensor orbit is closed and
identifies a semisimple reconstructed category. It is not a
substitute for this proof for nonclosed orbits. The explicit odd
derivation certificate for E×P¹ is saved separately and explains
one obstacle to replacing the ordinary group by GL(a|b).

Opened primary URLs:

- https://www.jmilne.org/math/Books/iAG2022.pdf
- https://arxiv.org/pdf/2011.10820
- https://arxiv.org/pdf/2105.04622

Source files and SHA256 values are recorded by
`fetch_c1_audit_sources.py` and its JSON output.
