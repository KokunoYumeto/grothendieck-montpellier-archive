# Independent written audit of the exterior-power trait criterion

19November2026, approximately08:58UTC. Part D independently read the
complete actual `part_c/c4_exterior_trait_criterion.tex`, including its
two final repairs. Full mathematical/written-proof pass for:

- `c:exterior-weight-criterion`;
- `c:universal-trait-weight-equivalence`;
- `c:single-endpoint-insufficient`;
- `c:trait-exterior-scope`.

The graded Jordan-string construction, independence proof and dimension
telescoping identity are correct without Frobenius semisimplicity. The
full wedge of any homogeneous length-L string gives a nonzero invariant
in weight L times its centre; the determinant average therefore forces
all centres to equal the proposed weight. Conversely, with f=N and
[e,f]=h, a lowest vector z of Cartan weight a satisfies
f e^k z=−k(a+k−1)e^(k−1)z. For maximal t with e^t z nonzero, k=t+1
gives a=−t. This supplies the required exterior invariant bound without
an unmentioned decomposition theorem.

The first written version's common-extension wording could have silently
presumed strict semistability survives ramified base change. The actual
revised text uses a separate field L_r for each semistable alteration,
after a fixed extension K0 already making the original representation
unipotent. Each kernel is unchanged under L_r/K0, and Frobenius powers
transport each inequality back separately. No common regular model is
assumed. This correction was independently identified by Parts C and D.

Rapoport–Zink weights in [0,2j] give N^(j+1)=0. The geometric permutation
operator contributes the Koszul sign, so the displayed exponent j+1
indeed selects the ordinary exterior power. The middle-degree reduction
uses actual split summands, via hard-Lefschetz inverse after a complete
intersection, or the H0 factor of a projective-space padding. It does
not rely on purity being inherited by arbitrary unsplit WD submodules.
Finite-inertia descent and the all-local-fields quantifier are correctly
retained.

The formal j=4 example has the stated compatible symmetric pairing,
determinant weight16 and first invariant bound, while its length-two
high string produces the exterior weight10>8 witness. No geometric
realization is claimed. This written check did not rerun the certificate
or independently reopen the newly cited Taylor–Yoshida source. The
universal equivalence is for the explicitly normalized trait endpoint;
it does not by itself assert the arbitrary-morphism C.4 conclusion.
