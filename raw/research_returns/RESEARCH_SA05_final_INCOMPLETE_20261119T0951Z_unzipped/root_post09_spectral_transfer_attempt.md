# Attempt to remove the simple-spectrum hypothesis by geometric transfer

19 November 2026, after checkpoint 09. This is a bounded failed-route
argument for C.4. It does not alter the universal gate or assert that all
conceivable transfer constructions fail. No priority is claimed.

## The possible transfer and its precise obstruction

The newly proved C.4 sufficient condition asks for a squarefree
Frobenius characteristic polynomial on the whole primitive degree-two
cohomology of the union of double surfaces, over one fixed finite field.
One might try to obtain that condition by a constant-field extension,
a generically finite smooth projective alteration, or an Artin twist.
The following elementary calculation rules out these particular ways
of removing an existing eigenvalue multiplicity.

Let S and T be smooth projective geometrically connected surfaces over
F_q, and let pi:T→S be generically finite of positive degree. Fix
ample divisor classes defined over F_q. Write H_S and H_T for their
degree-two Q_ell cohomology, using geometric Frobenius F and ell≠p.
Pullback is split injective: pi_* pi^* = deg(pi) on H_S by the
projection formula. Thus the characteristic polynomial of F on H_S
divides the one on H_T in Q_ell[t].

For either surface U, its ample line has eigenvalue q, its
self-intersection is a nonzero integer, and orthogonal projection
along that line gives the F-equivariant decomposition

    H_U = Q_ell(-1) ⊕ P_U.

Consequently char(F|H_U)=(t-q) char(F|P_U). Cancelling the common
factor (t-q) in the divisibility above shows

    char(F|P_S) divides char(F|P_T).

This is a characteristic-polynomial conclusion; it does not require
the old primitive subspace to pull back into the primitive subspace
for the newly chosen ample divisor. Therefore a repeated root in the
old primitive polynomial remains repeated after such an alteration.
The same argument applies component by component to a disjoint union
of surfaces. Additional components cannot remove a repeated root.

After extension from F_q to F_(q^a), Frobenius becomes F^a. Every old
eigenvalue of algebraic multiplicity m contributes its a-th power
with multiplicity at least m; coincidences of distinct powers can
only increase multiplicity. Frobenius is invertible, so all these
eigenvalues are nonzero. This argument also covers a nonsemisimple
operator: characteristic-zero powers do not eliminate its old
eigenvalue multiplicity. Hence finite constant extension cannot
repair a nonsquarefree primitive polynomial.

Finally, let A be a nonzero Artin representation. Its Frobenius has
finite order and is semisimple over an algebraic closure of Q_ell.
For every eigenvalue beta of A, P_S⊗A contains a summand on which
F acts as beta F|P_S. An old root of multiplicity m therefore again
has multiplicity at least m. Tensoring by A, or taking a nonzero
summand selected solely on the Artin factor, cannot remove it.
This says nothing about a new algebraic projector that splits the
old multiplicity space; constructing a sufficiently positive such
projector is additional mathematical input.

## Consequence for the attempted route

The simple-spectrum proposition remains a sufficient special case.
If its primitive target already has a repeated eigenvalue, the
three operations just checked do not supply its hypothesis. The
mixed numerical-equals-homological assumption is also still required.
No assertion about the truth or falsity of geometric weight–monodromy
follows from this limited obstruction, and it is not qualifying
movement at the fifth formal review.

The only ingredients are the same cohomological push-pull identity,
ample-line projection and Frobenius conventions used and checked in
the manuscript's C.4 product/alteration transfers. This note introduces
no additional external theorem or claim of a new literature result.
