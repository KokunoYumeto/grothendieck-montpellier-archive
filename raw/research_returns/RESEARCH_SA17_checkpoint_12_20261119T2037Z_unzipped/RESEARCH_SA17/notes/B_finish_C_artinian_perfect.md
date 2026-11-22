# Perfect-field descent for finite coefficient algebras

Agent dieudonne; run RESEARCH_SA17_FINISH-20261119;
GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Full written draft: sections/C_finish_artinian_perfect.tex.
No priority or novelty claim.

The finite-dimensional perfect-field descent of
sections/C_finish_perfect_descent.tex extends to the category
of projective R-linear rational O_m representations for every
finite-dimensional commutative algebra R over the perfect field k.

## Exact new statements

C:finite-algebra-projectivity-descent:
projectivity reflects through field extension by an elementary
linear splitting system; Hom commutes with extension; algebraic
isomorphism reflection follows by restricting a finite extension
and Krull-Schmidt cancellation. The full R-action is always included.

C:artinian_perfect_Galois_indices:
geometric canonical templates over all local factors of R tensor kbar,
extended by zero, carry the actual Galois action including permutation
of the Artin factors. Every finite orbit gives exactly one indecomposable
projective R-representation. To ensure existence stays projective,
descend an actual projective idempotent together with the coaction
to a finite Galois L, then restrict scalars from R_L to R.
The resulting object is projective and isotypic. Primitive idempotents
of its finite-dimensional End/rad algebra give the representative.
Geometric multiplicity is the Schur index; central degree is orbit size.
Coefficient degree is preserved. The split Green ring is the explicit
Schur-weighted orbit-sum subring of the geometric one.

C:artinian_perfect_WG_reduction:
duality is Hom_R(-,R), never k-linear duality. All QSS hypotheses
hold because the category splits idempotents, has finite-dimensional
k endomorphisms and nilpotent radicals. The additive split form group
is a sum of explicit residue-division hermitian groups, plus Z for
non-self-dual pairs. Actual tensor/exterior matrices and transfer
compute the coefficient forms. This is a proved reduction, not a
claim to classify forms over arbitrary perfect fields by numerical
invariants or to possess a uniform arithmetic algorithm.

C:perfect-residue-Artin-reduction:
every Artinian ring of characteristic p>2 with perfect residue fields
falls into the preceding class factorwise. The canonical coefficient
field section is s(a)=b^(p^N), where b lifts a^(1/p^N) and
m^(p^N)=0. Independence of lift and ring-homomorphism identities are
proved directly. Characteristic p^e with e>1 and imperfect residues
are explicitly excluded.

## Sources opened and dependencies checked

Opened Stacks058S Proposition10.83.3 finite projectivity descent;
Stacks032A Theorem10.160.8 coefficient rings; Stacks0753
Lemma11.8.6 central-simple splitting.
Reread full promoted sections/C_finish_perfect_descent.tex,
including finite-extension Noether-Deuring proof and its exact
perfectness and form-arithmetic boundaries.
Reread QSS1979 original pp269--273, Theorem2.2, Corollary2.3,
Propositions2.4--2.5 and Theorems3.2--3.3.
Reread the already independently audited
sections/C_finish_artinian_algclosed.tex for its R-dual and
componentwise geometric algorithms.

Searches included finite projective faithfully flat descent and
Cohen structure theorem perfect residue coefficient field.
The results are not presented as novel.

The first four complete written proofs passed independent root and
descent_groups audits. Their two wording clarifications were applied.
The appended C:artinian_effective_C1 theorem has been sent for separate
audit; root owns compiled inclusion. Five result rows and eight own
used/rechecked events, including three used root-descent dependencies,
are saved in the separate catalogs.
No finite certificate is claimed for the general Galois/descent
proofs. All asserted reductions have complete proofs in the draft.

## Complete effective C1 nonfield strengthening

C:artinian_effective_C1 gives an actual terminating full classification
for every finite-dimensional R over an effective perfect C1 field k.
The full tuple encodes R-action and coaction. For M=k^N, projectivity
is decided by an explicit R-linear section of R^N onto M, a finite
affine linear system. This computes a projective idempotent.
Joint End has the positive semisimple-quotient certificate algorithm.
Least-code indexing is finite and decidable. The dual is the solution
space of F B_i=Q_i F, valued in R, with antipode precomposition.
Gram nondegeneracy is the k-linear determinant of M to its R-dual.
Residual C1 forms are rank/determinant or the alternating/unitary/pair
integer, with canonical square-class codes. Tensor/exterior operations
use R-projective idempotents and minors, never k-tensors or factorial
division. Concrete infinite nonclosed fixed-prime towers are covered
by the independently audited C:C1_tower_example.

## Imperfect effective C1 strengthening

C:artinian_effective_imperfect_C1 removes perfectness from the direct
recursive algorithm, under factorization access over every explicitly
presented finite tower of irreducible simple field extensions. Each
finite residue center has such a tower even when it has no primitive
element over k. C1 finite-extension stability and Brauer zero still
hold, so the same positive semisimple-quotient certificate terminates.
The remaining direct tuple, projectivity, R-duality, form and operation
steps have been checked individually to need no perfectness. The
perfect-only Galois-orbit theorems are retained unchanged. This sixth
statement is separately submitted for independent audit.
