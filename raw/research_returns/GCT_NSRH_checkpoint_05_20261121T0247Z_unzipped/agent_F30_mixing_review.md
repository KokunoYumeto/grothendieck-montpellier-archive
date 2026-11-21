# Fresh full review of the F30 mixing supplement

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed.
Date: 21 November 2026 UTC.
Target: `agent_nonstandard_tower_mixing.md`, complete Sections 1--6.
SHA256: `7722d1cf31b8804bd18f55e58c968a2158eeb0f03db4b8dad0f7a399e7a03d7e`.

**Result: PASS.** Every new argument in the supplement was read and independently reconstructed. The existing rank-three block decomposition and generic branching decomposition are used as the explicitly identified prior inputs, rather than represented as newly proved here. This review does not certify a later generated main-paper supplement until its text is compared.

## Source and fixed-action checks

The complete statement of Blasiak, arXiv:1201.2209v2, Theorem 5.1, printed p.14, was reread in the local primary text. It explicitly says split semisimple and identifies the restriction of a distinct-pair tensor product as an irreducible. For the pair `(3,1),(2,2)`, this gives the endomorphism field `K`, not merely some unspecified division algebra. The F19 localization denominators are units in `Q[v,v^-1]_(v-1)`, so its three regular block idempotents apply in the supplement's ring. No colliding-branch difference is inverted.

The ordinary parabolic projector commutes with the whole ordinary parabolic tensor algebra, hence with the actual rank-three nonstandard generators. Its two complementary summands are stable. Applying the three regular block idempotents inside the rank-four complement gives the claimed rank-one, rank-one, rank-two free summands. This separates the second matrix-type plane without an impermissible spectral projector through the collision.

## Independent compression and graph calculation

For `w=(1,1,1,-3)`, `||w||²=12`. The three transpositions in the first three letters have compression scalar one; each transposition involving the fourth letter has dot product `−4` with `w`, hence scalar `−1/3`. In the standard representation of the three pairings, each of these two sets maps to the complete set of three transpositions of `S3`, whose class sum is zero. Thus the compression of the full `S4` transposition sum to `E` is zero.

The two specialized constituents are `(3,1)` and `(2,1,1)`; their content sums are `2` and `−2`. Therefore `Z²=4`. Since `Z` is an `S3` intertwiner and has zero `E` component, it carries `E` isomorphically to the unique standard summand `F` of the complement, and carries `F` back to `E`. Consequently `J=Z/2` is an involutive exchange. Direct substitution gives `Z(x±Jx)=±2(x±Jx)`, and the branching of the two classical constituents identifies their standard planes as exactly the two graphs. No positivity of a matrix or a pure basis is inferred from this exchange.

## Integral regularity and exact limitation

The actual rank-two idempotent `e=P1/D` is regular because `D(1)=4`. Its restrictions to the two free standard-type planes have projective rank-one images and complements, so bases can be chosen with nonzero reductions. Since `J` is rational and commutes with the specialized rank-two action, constant rational units align the matching reduced lines. The two mixing matrices have determinant `−2`, a unit in the specified ring. This proves a regular basis change in the original lattice; it uses non-diagonal mixing across different penultimate summands, exactly the freedom left open by the F30 obstruction.

Any endomorphism commuting with the full nonstandard action becomes scalar on the split-simple generic fiber. Since the module is free over the local domain, an integral scalar matrix has scalar in that domain. Thus the integral commutant is precisely `R`, and its specialization maps diagonally into `k×k`. The special projectors cannot lift as commuting endomorphisms. This is compatible with the mixed basis: its groups span free direct summands whose specializations are classical constituents, but these summands are not stable under the full generic action.

The scope is correct: one fixed tower-rank-four module, a regular basis construction, and an exact commutant/base-change defect. There is no claimed uniform algorithm, canonical basis, positive structure constants, or stable generic splitting.
