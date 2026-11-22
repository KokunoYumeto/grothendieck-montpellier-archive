# Independent targeted audit of the finite-field extension

Agent dieudonne, RESEARCH_SA17_FINISH-20261119,
GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Exact UTC audit and execution events are in checks_C_finite_fields_audit.tsv.

Read the complete sections/C_finish_finite_fields.tex and its bibliography.
Both numbered statements pass. This is a targeted audit of root's proof,
not an independent re-proof count.

## Canonical indices and exhaustive finite operations

At fixed(n,d), all tuples over F_q form a finite specified set. The dual
coalgebra relations are exact coaction identities; centralizer idempotents
detect decomposability in the rational group category; lexicographic least
GL_n(F_q)-conjugates give one specified representative. Minimal coefficient
degree is invariant and prevents repetitions between different d. There is
therefore no remaining unspecified isomorphism quotient.

For an indecomposable finite-dimensional module, its finite-dimensional
endomorphism algebra is local. A module endomorphism is a unit in that
algebra exactly when its underlying linear matrix is invertible: the inverse
of an invertible equivariant map remains equivariant. Its finite list of
nonunits is consequently the radical and can be enumerated. The quotient
division algebra is finite and hence commutative.

Independently opened the primary sources:

- Michael Artin, Noncommutative Rings(1999), TheoremIII.4.4, printedp29,
  including the argument using conjugate maximal subfields and the finite
  group covering lemma: https://math.mit.edu/~etingof/artinnotes.pdf .
- Sergeichuk, arXiv1011.3142v1, Section3, Lemma3.1(a),(b), finite quadratic
  and hermitian forms: https://arxiv.org/pdf/1011.3142 .
  Also read the complete corresponding local source passage at
  ../external_sources/Sergeichuk1011.3142_source/paper.tex, lines1210--1234.

## Transfer signs and the actual generators

If q has sign epsilon and adjoint *, then (q a)^t=epsilon q a*.
Thus a*=epsilon a makes q a symmetric. For a residue element c satisfying
sigma(c)=epsilon c, the lift a=(b+epsilon b*)/2 has residue c and exactly
this adjoint symmetry. Since c is nonzero in the residue division field,
a is invertible. This verifies root's unitary generator, including epsilon=-1.
For symmetric type with sigma=1, a=(b+b*)/2 lifts a nonsquare c and yields
the second rank-one multiplicity class. For alternating type, H(U) represents
one symplectic multiplicity plane. Non-self-dual pairs also give H(U).

The finite-field symmetric classification uses dimension and determinant
square class; its split group completion is Z plus Z/2. This is not the
Witt group, whose answer can instead involve Z/4. Alternating forms have
one class in each even dimension; unitary and skew-unitary forms have one
class in every allowed dimension, with a nonzero anti-invariant scalar
converting the signs. Thus the stated free and two-torsion factors are correct.

Actual underlying multiplicities bound all remaining form choices: one
determinant bit for each nonempty symmetric isotypic component and no
extra bit for the other types. The residue-form theorem guarantees that
one of the constructed finite candidates is isometric to the actual result.
Exhaustive equivariant GL_N(F_q) search finds it and terminates. Dimension
strictly decreases on every idempotent split. Tensor entries and exterior
minors have the claimed finite degree bounds, including when the exterior
index is divisible by the characteristic. Virtual operations then require
only finitely many such actual calculations.

## Characteristic-three form example

For S=Sym2(F3^3), the independently checked coordinate-coalgebra calculation
gives End(S)=F3[I,K], K^2=0. The operator K is self-adjoint for Q(A,B)=tr(AB).
Every equivariant unit is aI+bK with a nonzero and norm a^2I+2abK.
Its residue norm is1, so Q cannot be carried to2Q. The nilpotent term in
Q(cI+dK) can be removed by choosing b, leaving the nonzero residue c as
the exact two-valued invariant. The transpose-product of the displayed
2x2 rotation is2I, giving Q+Q isometric to2Q+2Q.

The determinant invariant here is that of the residual endomorphism field,
not the ordinary dimension-six Gram determinant. The latter would not
distinguish these forms, since multiplying by2 changes that determinant by
2^6=1 in F3. Root's proof uses the correct residual invariant.

Independently reran code/C_finish_finite_field_forms.py with only the log
destination changed. The rerunnable copy is
code/B_finish_C_finite_forms_recheck.py and its output is
logs/B_finish_C_finite_forms_recheck.json. All6 units and6 nonsingular
invariant symmetric forms were enumerated; all36 action comparisons give
exactly two orbits of size3; the rank12 double-sum congruence passes.
This uses the full coordinate-Hopf-algebra centralizer result, not a
centralizer calculated from a sample of finite-field group points.
