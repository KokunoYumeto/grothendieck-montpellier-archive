# Independent review: arbitrary finite Frobenius data and theta avoidance

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

**PASS under the explicitly carried A19/A37 moduli and geometric inputs.** I read the entire `geometry_tower/rm_frobenius_avoidance.tex`, the entire carried `finite_support_theta.tex` (A19), and the entire carried `rm5_finite_support_avoidance.tex` (A37). The named published moduli, descent, and Lang–Weil inputs of A37 remain accepted carried inputs; I did not independently re-retrieve their primary publications in this check. No computation or Lean kernel check is claimed.

I requested one scope clarification: the prescribed Hilbert–Blumenthal locus in KT-RM-FROB-AVOID should explicitly be **in characteristic two**. This is the locus used by A37 and the case where the actual Raynaud theta support is the degree-one translated Abel curve used by A19. With that specification, the theorem and its positive/negative corollary have the asserted scope.

## New argument checked

1. Reduction from SL2 of the quadratic local integer ring to every finite quotient is onto, including at the ramified prime five. A determinant-one matrix modulo the maximal-ideal power has a unit cofactor in each local factor; correcting the corresponding lifted entry fixes the determinant. The product of local factors and successive lifts give the required integral lift.

2. The regular determinant function `det(g^D-1)` is nonzero on the restriction-of-scalars group: a diagonal element with an infinite-order rational l-adic unit provides a nonzero value. This group is geometrically irreducible. The displayed left-translated big cell has six Q_l coordinates, and every sufficiently small integral congruence ball is Zariski dense there. A nonzero polynomial cannot vanish on a product of six open balls, by repeated one-variable root counting. Thus every prescribed congruence class admits a lift with finite determinant valuation. This argument works equally for split, inert, and ramified primes.

3. The common integer D is chosen from the full finite actions on the underlying rank-four F_l modules. No semisimplicity is assumed, including at five. Every chosen lift therefore has `G_l^D=1 mod l`.

4. Freezing the matrix modulo `l^(a_l+1)` freezes the valuation `a_l` of the determinant. Compatibility with the originally prescribed higher precision follows because the chosen G_l already lifts that data; the Chinese remainder construction has no conflict. The eventual Frobenius matrix need not have determinant exactly one over Z_l. Only its prescribed determinant-one reduction modulo L is used, and Q is chosen to be one modulo L.

5. Smith normal form, or the adjugate identity, shows that the kernel of `Phi^D-1` on the l-divisible torsion group is killed by `l^a_l`. Taking the product over the finite support bounds all mixed supported orders by N. This is an exponent bound, not an assumption that N is squarefree.

6. The generic nonzero N-torsion avoidance open comes directly from the complete A37 argument. It remains nonempty inside any prescribed nonempty ordinary open. Full joint monodromy is available at the entire integer L; independent prime-level monodromy is not being assumed. Choosing an auxiliary odd level coprime to L and then descending/enlarging the finite constant field makes the full symplectic level torsor have the required constant group.

7. Twisting that geometrically integral affine torsor by delta and using Lang–Weil in extension degrees congruent to one modulo the order of delta realizes exactly the desired finite conjugacy class. The universal curve, its specified integral Rosati action, and its actual Raynaud theta are all defined over the resulting field, with no further extension that could change Frobenius.

8. A19 applies because `Phi^D` fixes every J[l] in the support. It puts every geometric supported theta point into `J(F_(Q^D))`. The previous determinant bound kills that group's supported part by N, and the chosen finite avoidance open excludes its nonzero N-torsion. This handles every exponent and product in the prescribed support, including overlap with the modulus m. The empty-support case reduces to torsor specialization.

## Corollary and limits

The positive class is obtained from the carried actual A13 curve and the integral real multiplication of A33. Extending constants to make its torsion point and roots of unity rational preserves the positive primitive-rank-zero cover. Record its finite Frobenius action only after making that extension. Applying the new negative theorem to that recorded class gives the same finite torsion action with no supported theta point of any exponent. The proof does not assert that an arbitrary prescribed class has a positive curve.

The two fields need not have the same size and the curves need not have the same Weil polynomial. The result rules out a universally sufficient theta-incidence criterion based solely on any prescribed finite congruence precision of Frobenius and this real-multiplication action, for witnesses restricted to a prescribed finite prime support. It does not handle adaptive unbounded prime support and does not settle the universal existence of an odd cyclic cover for an individual curve.
