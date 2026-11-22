# B94 exploratory record — NOT A THEOREM, no promotion

Retained 2026-11-20 during the CP34 canonical freeze. All calculations below require a complete typed proof and independent audits. No finite computation has yet been executed for this route. These notes do not change the proved gate.

## Scope and actual matrix group

p=5, e_K=20, mu_5 in K, complete mixed characteristic with algebraically closed residue; good tame L/K degree24, v_L(5)=480. Both original parameters B_i=5b_i>20. Actual high quotients have parameters5j_i, j_i=24-b_i. Focus only layer shape(3,4). Lie commutators force W1=sl2, W2=M2. Determinant mod25 is trivial, so K=K0(mu25), and actual cyclotomic mu125/L has degree5 and upper break576. The full actual125 image should be the Iwahori group with determinant1 mod25:

[[1+5a,b],[5c,1+5d]], a,d,c mod25, b mod125,
a0+d0=u*c0 mod5, u=b mod5.

Original residual R is u; quotient residual R' is c0. On R, the original25 kernel is sl2 with coordinates(c0,a0,b1), d0=-a0. Over R' the quotient25 kernel is its opposite. The common25 field of the actual quotients is available from the actual125 comparison; no quotient125 comparison is available.

## Normality / shared diagonal proposal

Conjugation by residual upper u acts on sl2 by
 a -> a+u*c, b1 -> b1-2u*a-u^2*c, c -> c.
Conductor invariance and the +u/-u combinations give cond(a),cond(c)<=cond(b1). Diagonal and off-diagonal tame weights differ, so equal graded conductors are impossible, hence diag cond x<last off cond C. Similarly quotient diag y<its last off conductor. The same conjugation gives rho=cond_R(c0)<x and sigma=cond_R'(u)<y.

Let r=b(R/L), r'=b(R'/L). Herbrand gives rho-sigma=5(r'-r). On S=RR', the actual tracefree relation a0=-d0 identifies the diagonal characters; their conductors are5x-4rho and5y-4sigma. Thus y=x+4(r-r').

Need write the strict x>r, y>r' proof carefully: in F2/R, the lower break of an element with nonzero diagonal and zero c coordinate is D. For the outer residual coset choose lift with maximal break M. Its quotient break is phi_H(M)=r. If r>=x, then M>=D. Choose lower-root element with nonzero c; commutator with the outer lift has nonzero diagonal (possibly upper term), hence break D, contradicting [G_i,G_j] subset G_(i+j) since its break must be >=M+b(c)>D. Same opposite argument gives y>r'. Actual subgroup typing, not equality of arbitrary lifts, must be explicit.

## Mixed small-divisible / large-prime common-high proposal

Actual point field over R is C5^2 with coordinate A_i=5b_i; low displacement D0_i=125b_i, high displacement D1_i=15000-625b_i, v_E(5)=60000. Assume b1 divisible5 and b2 prime5, b1<b2, among(5,9),(5,13),(5,17),(15,19). Last line H follows from normality above. Let first lower break t=x, last u.

Prime-coordinate cases t>24b2 and t=24b2 contradict the smaller b1 coordinate as in B92 (write all coefficients/boundaries). Thus t<24b2, u=15000-630b2-4t.
For these four rows, 5u+A1-D1_1>60000+630b1-3630b2>0. Thus at last break the smaller coordinate is uniquely ordinary and K1=D1_1-u. At first break K1+t-D0_1=630b2-750b1+5t>0. If t>=24b1, all p-divisible terms also change after D0_1, contradiction. Hence 0<t<24b1, 24|t. The off character conductor is C=3000-126b2.

## Four possible immediate exclusions

(5,17): x<120; quotient pair(7,19) gives y=168 by B92's common-high lemma. Quotient residual r'=6 (prime coordinate j19 bounds r'<30 and tame congruence6 mod24). Original r congruent18 mod24. Relation gives x=192-4r. r18 gives forbidden x120; r42 gives x24 but sigma=186>y168; higher r gives negative x. Thus impossible if all normality claims above hold.

(5,13): quotient(11,19) gives y264 and r'6; x=288-4r. Positive x<120 forces r66, but sigma306>y264. Mirror rows(7,19),(11,19) interchange original and quotient at the actual25 level; do not assume quotient125.

## (5,9): nine potential profiles and terminal bounds

Quotient pair(15,19) also satisfies the mixed proposal. r'=6; write r=R. x in{24,48,72,96}; y=x+4R-24<360. With x>R, the nine possibilities are:
 R18,x24/48/72/96;
 R42,x48/72/96;
 R66,x72/96.
Original off b1 has conductor1866 over R; quotient off c1 conductor606 over R'.

E=F2*FQ has degree5^5; terminal kernel U is upper-triangular three-space(a1,b2,d1). Proposed E/L upper breaks:
 6,R,(x+4R)/5,126,(1866+4R)/5.
Lower breaks:
 l1=6; l2=5R-24; l3=5x-24;
 l4=15726-20x-100R;
 l5=170226-20x+400R.
Cyclotomic restriction conductor:
 C=psi_E/L(576)=803976-20x-2100R.

High primitive125 point: original high p25 coordinate j/5, p125 coordinate j/125. Point field degree625; adjoining R gives T_h degree3125. S_h=R*L(P25_high) has degree125. T_h/S_h=C5^2(a1,c1). E/S_h=C5^2(b1,c1), lower l4(c1),l5(b1). c1 quotient conductor=l4. Choose j_min15, giving unconditional last high-line break bound234000. Thus a1 conductor over S_h <=(234000+4l4)/5 and restriction to E yields
 B_a=1170000-4l5=489096+80x-1600R.

Low125 point extension over its25 point is C5^2(b2,d1); choose b_min5 giving d1 quotient conductor<=15600. E over the low25 point field is cyclic25 (c0 fifth-power c1), lower6,l4. Hence
 B_d=389880-4l4=326976+80x+400R.
Differences C-Ba=314880-100x-500R>0 and C-Bd=477000-100x-2500R>0 for all nine. Need derive every stabilizer, actual field intersection, and subgroup conversion, not just the numerical identities.

## (15,19): opposite arrangement

Original r=6; quotient residual r'=R. Let x denote the smaller quotient diagonal conductor, same nine(R,x) possibilities. Original diag is x+4R-24. E/L has the same listed five breaks. Original b1 occurs at l4 (global126); quotient c1 at l5. Cyclotomic C unchanged.

High primitive125: j_min5 gives high-line bound78000. Now c1 quotient conductor=(l5+4l4)/5; actual E/S_h conversion gives
 B_a=390000-4l4=327096+80x+400R.
Low primitive125: b_min15 gives d1 bound46800; E/low25 point is cyclic25 with lower l2,l5, yielding
 B_d=1170000-4l5-20l2=489576+80x-1700R.
C-Ba=476880-100x-2500R>0; C-Bd=314400-100x-400R>0.

## Other four rows / limitations

(7,15),(11,15) and quotient mirrors(9,17),(9,13) remain. Prime-small/large-divisible gives critical t=24b_small; strict regimes violate the other high-displacement bound. The critical coefficient can vanish/cancel and needs full treatment. No claim yet.

The (4,4) original full-first-layer case is not addressed. Irreducible residual cases also remain. No realization and no least-index conclusion.

## Preserved corrections to exploratory reasoning

- Pairs(7,11),(13,17) initially considered in reasoning are already the same finite special Frobenius orbit and are not surviving different-character rows. No movement counted.
- A temporary mental A=125 for b5 was corrected before any written candidate/program: A=5b, so b5 gives25 and b15 gives75. All displayed calculations in this note use the corrected values.
- No program/checker has yet been run for these profiles. No proof/audit verdict exists for this note.
