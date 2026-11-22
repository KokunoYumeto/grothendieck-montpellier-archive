# Independent review of root C.3z

Reviewer: `/root/real_weil`, 19 November 2026; final full review at 07:44 UTC.
Reviewed file: `research/sections/C3_completion_algebraization.tex`.
Outcome: **passes after the explicit final-step scope repair recorded below**.

## Exact proof checks

The completion of the excellent normal local domain remains normal and
has regular puncture. A nonmaximal completed prime cannot contract to the
maximal ideal, because the closed fibre of completion is the residue
field. Regularity ascends along the regular completion map. The given
coefficient field and finitely many cotangent generators supply the
power-series presentation. The perfect-field formal Jacobian criterion
supplies the hypothesis of Artin's isolated-singularity algebraization.

Approximation of the algebraic model's finite equations modulo the
square of the maximal ideal gives an actual map to the original
henselian ring. Its completed map is surjective by the cotangent-space
criterion and successive polynomial approximation. Since both complete
domains have the same finite dimension, its prime kernel is zero. Thus
the actual map, and not merely a chosen jet, induces an isomorphism of
completions. Faithfully flat descent of regular maps proves that the
model map is regular. Base changing a proper regular alteration and
selecting a connected component meeting the generic fibre gives exactly
the proper regular integral alteration required in C.3w.

Every subsequent step of C.3w only needs the excellent henselian
coefficient-field ring, that alteration, proper formal existence, and
general henselian G-ring approximation. The formal-unit gerbe,
whole-family approximation, proper-curve rigidity and codimension-one
finite-flat norm arguments retain their hypotheses. No universal actual
family on a whole abelian local-Picard subgroup is inferred.

The first version's final invocation of C.3q needed a scope repair:
C.3q explicitly assumed an essentially-finite-type model for its local
Neron-Severi and full-kernel inputs. I flagged this, and then read the
entire revised step 5. The repair is correct. On every finite-type
coefficient algebra D, the henselized tensor pairs for R and its
completion have canonically identical completions
`lim_n (R/m^n) tensor_k D`. Elkik applies to their ideal complements.
The natural presheaf bijections survive etale sheafification, and
finite-type affine test objects give the represented group-scheme
isomorphism by Yoneda. Repeating for the algebraic model identifies
identity components and transfers the finite-generation statement for
the local Neron-Severi point group. A pointwise completion bijection
alone would not suffice, and is not what the revised proof uses.

For the finite-type kernel inside the reduced source identity
component, prime-to-p torsion injectivity excludes all such torsion
points. Chevalley's theorem then gives a unipotent reduced identity
component; divisibility lifts component torsion, so the component group
is p-primary. A p-power kills the whole reduced group. Its nilpotent
thickening is affine. In a faithful closed matrix representation, the
entries of the remaining multiplication matrix minus the identity lie
in the nilradical. A sufficiently large p-power annihilates the matrix
power. Thus a p-power kills the entire group scheme, including possible
mu_p factors. The subsequent faithfully flat descent of multiplication
and proper abelian image are exactly the valid argument of C.3q.
Point realization from C.3w now yields actual ordinary surjectivity.
There is no need to algebraize the pair (R,f) simultaneously.

## Primary sources freshly inspected

- Artin (1969), Theorem 3.8, printed p.32, including direct image
  inspection; proof and Theorem 3.9, pp.33–34.
- Hauser–Woblistin (2021), Proposition 2.5; Section 2's perfect-field
  assumption and explicit formal ring `k[[t,y]]`.
- Stacks 07NT, 07QY, 07BY and 06AD, exact statements and needed proofs.
- Milne, *Algebraic Groups* (CUP 2022 author text), Theorem 4.9 and
  Corollary 4.10, printed p.87, including the Hopf-algebra proof of the
  faithful closed representation for a possibly nonreduced group.
- Re-read the complete separately proved local-Picard functor comparison
  in C.3p and all stages of C.3w. The earlier opened Elkik and Boutot
  source scopes are preserved.

The canonical check events are in this agent's `CHECK_EVENTS.tsv` under
`C.3z` and `C.3z primary scope`. No computational experiment is used to
establish this general extension theorem.
