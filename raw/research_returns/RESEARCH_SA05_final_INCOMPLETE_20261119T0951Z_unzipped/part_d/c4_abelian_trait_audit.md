# Independent check of the abelian-type local weight endpoint

19 November 2026. This checks the deduction supplied by Part C
from its opened SGA7 I, Exposé IX statements; it does not assert an
independent rereading here of the entire original SGA7 scan.

For a semistable abelian variety over a local field with finite
residue field of cardinality q, put U=V_ell(A), V=U^I and let W be
the toric Tate subspace. With geometric Frobenius, the weights on
W, V/W and U/V are respectively -2, -1 and 0. Semistable
monodromy has N²=0 and ker N=V. A polarization identifies
im N=V^perp=W, hence the induced map between the two outside
graded pieces is an isomorphism with the required Tate twist.
This is precisely purity of the Weil--Deligne representation U
of weight -1, and of H¹(A) of weight +1.

Tensor products, duals, Tate twists and invariant direct summands
preserve Weil--Deligne purity: decompose the associated graded
SL₂ modules into strings; a string's centre has the prescribed
weight, and the kernel of N is its lowest-weight end. Thus a pure
weight-j motive built from abelian H¹ and Artin motives has all
weights of ker N at most j. Full inertia invariants are a
Frobenius-stable subspace of ker N, so satisfy the same bound.

The finite-extension descent requires a precise power argument.
Choose a normal finite extension L/K where the generators are
semistable and the finite Artin part is killed. Choose a positive
integer a such that a chosen geometric Frobenius φ_K satisfies
φ_K^a∈W_L; taking only the residue degree without considering
the finite inertia coset is not justified. On ker N and on the
monodromy-graded pieces, inertia of L is trivial. Therefore the
eigenvalues of φ_K^a have absolute values q^(a w/2) with the
weights w supplied over L. Taking a-th roots gives the same
weights for φ_K. This proves descent of the stated inequality.

The deduction is valid for ell different from the residue
characteristic, including ell=2 and residue characteristic2.
It is a local trait statement for pure abelian-type motives. It
does not prove the analogous claim for an arbitrary sheaf
R^i f_* on an arbitrary base, and it does not resolve the general
local-invariant-cycle or weight-monodromy conjecture. The 2026
rationality theorem is not needed for this particular endpoint.
