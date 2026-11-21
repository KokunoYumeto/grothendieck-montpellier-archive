# A weaker general-prime gate: nonvanishing on each pole divisor

Researcher `/root/tripod_integral`, GPT-6 Astra Pro; effort not exposed. 21 November 2026. This is a short extension of the checked multi-even proof. It does not claim that an additional prime satisfies the new condition.

## 1. Exact condition and deduction

Retain the arithmetic notation, Vandiver hypothesis, compact basis and companion errors from `work/multieven_pole_proof.md`. In particular each even component T_e of H_ab is cyclic over Lambda and finite free over Z_p, q_e(z) is the characteristic polynomial of gamma, and E_e gives bounded integral quadratic transforms C_(e;a,b)(T_1,T_2). Let L/Q_p split all q_e, with valuation ring O_L and uniformizer pi. Every root alpha lies in1+pi O_L.

Replace the unit-constant cup condition by the following test:

**Pole-NV.** For every even character e and every distinct root alpha of q_e, there is an ordered odd pair (a,b), with a+b=e modulo p−1, such that

    C_(e;a,b)(T, alpha/(1+T)−1) != 0

as a power series over O_L (or equivalently over its bounded-denominator localization).

Equivalently, for D_alpha=(1+T_1)(1+T_2)−alpha, at least one of the matching numerators does not lie in the prime ideal (D_alpha) of O_L[[T_1,T_2]][1/pi]. The equivalence is the explicit quotient substitution used in the checked proof. The pair may depend on alpha, even for a fixed e. No simplicity of alpha as a root is required.

**Deduction K17-POLE-NV.** If p is an odd Vandiver prime satisfying Pole-NV for its actual companion errors, then Omega_p^*=Omega_p.

### Complete proof of the extension

The arithmetic module construction, compact free basis, actual rational realization, companion identity and partial-fraction decomposition in the checked general proof do not use the unit cup hypothesis. They give formal even letters with leading kernels

    C_(e;a,b)(T_1,T_2) / D_alpha^k,

for every root alpha and 1<=k<=its multiplicity. They also give bounded coefficient measures after the finite scalar extension and linear change of letters. The finite excluded-weight argument avoids denominator zeros on the test grid, whose Cartesian tails retain interior accumulation points.

Suppose a nontrivial kernel element exists. Take its first assigned Magnus degree; choose a nonzero colored tiling with the maximum number of even letters; and for fixed pair positions and (e,alpha) colors choose a componentwise maximal pole-order vector, exactly as in the checked proof. At each selected pair choose the odd target types supplied by Pole-NV for that particular root. The singleton types are fixed by the chosen coefficient pattern.

Set S_j=(1+T_j)(1+T_(j+1))−alpha_j along the disjoint selected pairs, and pass to the Laurent series ring over the fraction field K_base of the remaining bounded-denominator power-series ring. The same classification of all other denominators shows they are analytic in the S_j unless they are the selected root denominator at that same pair position. Wrong-character terms vanish identically. Extract the coefficient of product S_j^(−k_j).

Maximality of the number of pairs and componentwise maximality of the order vector isolate exactly the chosen pattern. Its coefficient is its nonzero measure transform A in the unpaired variables times the product of the restrictions

    C_(e_j;a_j,b_j)(T_j, alpha_j/(1+T_j)−1).

Each restriction is nonzero by Pole-NV. The variables from distinct pairs are independent, the unpaired-variable ring embeds in the base ring, and that ring is a domain. Thus their product with A is nonzero in K_base. The checked proof only needed this nonzero product; it did not need those restrictions to be units. This contradicts the vanishing coefficient and proves injectivity on H. The cyclotomic character and functorial rational realization then prove the kernel-field equality. QED.

The entire additional deduction is the replacement of a unit in the residue/base field by a nonzero element of that field. All topology, completeness, multiplicity, character and coefficient-separation steps remain those of the checked general proof.

## 2. Why this is weaker than unit cup nonvanishing

If some C_(e;a,b) has p-adic unit constant term, it is a unit in Z_p[[T_1,T_2]]. Its image under every pole-divisor substitution is still a unit. Thus the odd mod-p cup condition proves Pole-NV simultaneously at all roots, as used for every odd p<1000.

The converse analytic implication fails. For example, the bounded analytic numerator C=p has zero reduction modulo p, but restricts to the nonzero constant p on every pole divisor. More generally, a numerator may have no unit constant and still be nonzero on each divisor. Pole-NV therefore requires less of the actual quadratic relation data than the unit cup test. This formal example is not an arithmetic prime or a Galois counterexample; no prime satisfying Pole-NV but failing the cup hypothesis has been established here.

For repeated roots the condition deliberately asks for nonzero restriction, not just a numerator that is globally nonzero. If the numerator is divisible by D_alpha, some highest pole orders cancel. A nonzero formal series away from the divisor would then be insufficient for the existing separation proof. Pole-NV excludes precisely that cancellation on at least one matching odd pair for each cyclic generalized-eigenvalue component.

## 3. Independence of routine basis choices

Fix gamma and the character convention. The condition is unchanged by the ordinary choices of cyclic lifts and odd Lambda bases used in the construction.

First replace a cyclic lift y_e by another lift of the same abelian class. Their quotient is in the closed commutator subgroup of H. In target length2 its contribution is an analytic bounded measure transform A_(a,b); commutator terms involving an even letter have length at least3, so only the two odd-orbit terms contribute. Hence

    B'_e = B_e + A,       C'_e = C_e + q_e(z) A,

where z=(1+T_1)(1+T_2). On a root divisor z=alpha the restrictions agree.

More generally choose another cyclic generator of T_e. It has the form b_e(gamma)v_e for a polynomial b_e whose class is a unit in Z_p[gamma]/(q_e). Expressing its lift as a product of the companion basis elements, up to a closed commutator word, gives

    B'_e = b_e(z) B_e + A,
    C'_e = b_e(z) C_e + q_e(z) A.

At z=alpha, the restrictions differ by the nonzero scalar b_e(alpha); it is nonzero because b_e is a unit in the finite cyclic module algebra. Thus Pole-NV is unchanged, including when q_e has repeated roots.

Finally an odd character component is free rank one over Lambda. A different Lambda basis multiplies its normalized linear moments by f_a(T), where f_a belongs to Lambda^times. Such a power series has unit constant term and no zero anywhere in the open unit disc. Normalizing the target odd letters accordingly divides C_(e;a,b) by f_a(T_1)f_b(T_2), up to the analytic commutator corrections already considered. These factors remain nonzero units on every pole divisor. Nonvanishing is preserved.

The splitting field is also immaterial: nonzero power series remain nonzero after scalar extension, and the roots merely become available for the displayed decomposition. There is no assertion here of invariance under changing the chosen cyclotomic generator; one can fix chi(gamma)=1+p throughout, as in the checked theorem.

## 4. Remaining arithmetic question

For primes not already covered, the sharpened task is to show that, for each cyclic even Iwasawa component and each root of its characteristic polynomial, its quadratic companion-error functions do not all vanish identically on the corresponding multiplicative divisor. This concerns the actual nonlinear Gamma action on the cyclotomic-kernel free pro-p group. A class-group order, the characteristic polynomial alone, or Vandiver does not supply these functions or their restrictions.

The condition is an explicit second-Magnus-layer test. It does not require computing every higher relation, but it is not presently verified here in the remaining prime range. If it fails for some root, the source direction might still be detected in larger target generator length; the present argument gives no negative conclusion about the original kernel.
