# Unreviewed higher odd-symplectic lead

This is exploratory reasoning, not a checked theorem or an input to any canonical section. Recorded during the C3 work, before the assigned A7 peer audit. It appears capable of excluding all mixed higher symplectic cores Sp2n(q), n≥4, odd q≥7, leaving q3/5. Every step below still needs a full written proof and independent audit.

## Candidate uniform support

Let c(q)=1/(sqrt(q)-1), the exact published Gluck unipotent ratio for q>4. Define

delta(q)=(1-1/q)(1-1/q^3)(1-c(q))/2.

For q7, c(7)<14/23 because1369<1372. Thus delta(7)>9234/55223>1/6. The full source budget would then force e≤165669/181<916.

## Elementary degree lower bound, avoiding a new degree classification

The line-parabolic Heisenberg group Q in Sp2n(q) has center Fq and irreducible representations with nontrivial central character of degree q^(n-1). A nontrivial irreducible Sp representation has central kernel only, so some nontrivial Q-center character occurs. The GL1 torus scales that center by all squares in Fq*, with orbit size(q-1)/2 on nonzero additive characters. Therefore a≥q^(n-1)(q-1)/2. Its minimum at n4,q7 is1029, already greater than916. This should have a short direct Heisenberg proof.

## Inner support via prime projective powers

Take a noncentral semisimple projective-prime-order power h of an arbitrary inner element. For odd prime r one may choose h of actual orderr; for projective order2, h² is scalar and its natural actual order may be4. Nontrivial unipotent powers are handled directly by the published trace bound.

If h has a stable isotropic R and the induced symmetric-shear action is nontrivial, its nonfixed Fq<h>-subspace U is elementary abelian, has order at leastq, and h permutes every nontrivial dual weight in prime-length orbits. Averaging c(q) over U gives support at least(1-1/q)(1-c(q))/2.

The symmetric-square action can be trivial only when h|R is scalar±I (for inner h). Choose an invariant hyperbolic pair extending a line in R by coprime-order averaging. On its complement W, h acts noncentrally relative to that scalar. The moving symplectic subspace W0 gives a Heisenberg subgroup Q0 of order at leastq³, with center fixed by h and fixed-point-free action on Q0/Z. Every nontrivial linear Q0-weight has a prime-length orbit. Each nonlinear Q0-isotypic block is a Schrödinger representation tensored with multiplicity, and the h-intertwiner is scalar times its finite Weil operator tensored with a multiplicity operator. Gérardin's already checked trace formula bounds the latter support by at least(1-1/q)/2. Averaging c(q) over Q0 bounds its trivial multiplicity by c+(1-c)/|Q0|. This gives delta(q) on the entire representation. Need write exact right/left action and treat actualorder4 carefully; the scalar±I exceptional shear case should only occur for actual odd order or actualorder2, so this issue appears harmless.

If h stabilizes no nonzero isotropic space, primary decomposition has only self-reciprocal factors, each multiplicityone. The centralizer is a product of norm-one tori, size at most(q+1)^n. Column orthogonality and the elementary degree bound should give a much stronger support bound than delta(7) for n≥4,q≥7. Check exact base inequality and monotonicity.

## Full normalizers

For prime q≥7, Out is diagonalC2. A compatible outer T whose square is nontrivial inner inherits the inner support. Otherwise take a natural GSp lift h with h²=cI and nonsquare multiplier mu=±c. It should always stabilize an isotropic R on whose normalized symmetric-shear space S↦A S A^t/mu the action is a nontrivial involution. If c is square, use a natural eigenspace; if c is nonsquare, view the natural space over E=Fq(sqrt(c)), with alternating E-form when mu=c and Hermitian E/Fq-form when mu=-c. For n≥4 each has an isotropic E-line. The eigenproducts ±c in Sym²R ensure a nonzero minus subspace. Its elementary U has order at leastq and h acts by inversion. Weight pairs yield support at least(1-1/q)(1-c(q))/2, stronger than delta(q). This needs the full elementary field/form proof.

For composite q≥25, the inner bound followed by the general scalar-aware commutator gives delta(q)/2. At q25 this is(9/50)(15624/15625)>delta(7); all factors are increasing. Thus arbitrary outer field actions are covered.

For q9 the already written C3 projective semilinear-involution descent works in every natural dimension2n. Inner or inner-diagonal squares transfer the inner delta(9) bound. Pure field involutions are conjugated by a similitude to Frobenius; the GLn row subgroup has9^(n-1) characters,3^(n-1) fixed, and c9=1/2, giving support at least(1-3^(-(n-1)))/4≥13/54. Mixed diagonal-field class with inner-trivial square is impossible by the same norm argument as C3. Both bounds exceed delta(7). No selfduality assumption is needed.

If these arguments survive full review, all compatible normalizers for every oddq≥7,n≥4 have the common support9234/55223. Tensor permutations retainquarter and factorwise spectra convolve. The actual sixfold Hurwitz budget forces e<916 while every factor has degree≥1029. No classification of all character degrees, no ESD premise and no equality of character fields would be needed. q3/5 are genuinely outside the proposed quantitative bound.
