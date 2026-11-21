# Independent review of the local mixed-root family

Reviewer `/root/lean_chain`; GPT-6 Astra Pro; effort not exposed.
21 November 2026. Reviewed hashes and time are recorded in
`local_mixed_paths_review_manifest.json`.

**PASS** after reading the complete `KT-LOCAL-MIXED-ROOT-PERSISTENCE`
proof in `../unitary_audit/reducible_comparison/local_mixed_paths.tex`.
The conclusion is local: the specified two directions occur together
on the actual local ordered ordinary component. It supplies no global
lift, no global normalization, no exclusion of global source points,
and no strict Selmer bound.

For V=K(eta chi^e), the unramified quadratic character is crystalline,
Fil^0 is zero, and H^0 is zero. The Bloch–Kato dimension formula gives
one dimension over the coefficient field. Local duality gives H^2=0,
since the dual twist has exponent 1−e, and local Euler characteristic
gives the same dimension for H^1. This proves equality of the two
cohomology spaces. The argument applies with a finite coefficient
extension by viewing the representation over Q_l and dividing the
dimensions by the coefficient degree.

In residual coefficients the dual inertia exponent 1−e is odd and
cannot be divisible by the even number l−1. Thus residual H^2 vanishes.
The successive integral cohomology maps are surjective; differences
between chosen representatives are corrected by lifting zero-cochains.
The inverse-limit cocycle is continuous because all its finite reductions
are continuous. No characteristic-zero lifting of an arbitrary global
class is used.

For the matrix in LM.3, the upper-right entry is s times a cocycle in
the character delta=eta chi^e. Multiplication gives exactly
u(gh)=u(g)+delta(g)u(h). Equivalently the matrix is
`(1+s u(g)E) diag(delta(g),1)`, which makes the subsequent adjoint
tangent normalization explicit.

In the ordered basis (E,lambda H,F), lambda^2=−1/2, the trace form is
K from HS.4. The identity theta(A)=DAD for every adjoint matrix makes
`(A(g)D^{j(g)},eta(g))` an exact GG3 homomorphism. Its upper triangular
diagonal is `(chi^e,1,chi^{-e})`: multiplying by D cancels the two eta
factors even in the nonsplit unramified quadratic case. Direct bracket
calculation gives `ad(E)=−2lambda(E12+E23)`, a unit multiple of the
positive twisted root.

For Y=E21−E32, Y^3=0. Thus the two exponentials used for conjugation
are genuine degree-two integral polynomials, since two is a unit.
Conjugation in the semidirect group differentiates to
`w(Y−ad(r0(g))Y)`, the source coboundary convention. In particular
the eta outer action has not been omitted. Strict finite local classes
in the negative rational coefficient are coboundaries by the previously
audited local H^0 argument.

The decisive component argument is the explicit formal construction,
not an inference from the existence of crystalline specializations.
Before the second conjugation the family is Borel-valued with exactly
the prescribed inertial diagonal. The conjugating matrix is congruent
to one over the complete local coefficient algebra O[[s,t]]. Therefore
the actual functor represented in `KT-ORDINARY-INTEGRAL-COMPONENT`
contains this family and its map kills I_t. I reread that complete
lemma, including its framed twelve-parameter description and equality
of the prime kernels, together with the complete antecedent
`KT-ORDINARY-ON-BASE-COMPONENT` proof. These are already audited inputs;
no new Lean kernel execution is claimed.

Characteristic-zero specializations are also crystalline: LM.1 gives
crystallinity of the two-dimensional extension, tensor/dual/subobject
closure gives it for the adjoint on ker eta, and conjugation preserves
it. This is consistent with, and additional to, the direct integral
component argument.

For primary scope, I read Berger's author `barcelone.pdf`, Section 5,
Theorem 5.1 (the stated local duality and Euler characteristic theorem),
and the complete displayed fundamental-exact-sequence derivation in
Section 16, pages 14–15. Those passages support precisely the
characteristic-zero cohomology assertions here, including the
unramified twist. I do not claim a fresh proof of local Tate duality or
of the foundational period-ring exact sequence. The finite local
duality theorem is the same previously audited imported input used in
the ordinary-component obstruction calculation.
