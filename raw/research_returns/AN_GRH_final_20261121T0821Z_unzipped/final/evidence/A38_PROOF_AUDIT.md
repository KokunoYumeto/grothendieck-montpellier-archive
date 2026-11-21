# A38 author proof and finite-arithmetic audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Exact scope and result

**PASS — author whole-proof read**, not an independent review. I read the complete statement, proof, and scope paragraphs of `A38_RM5_BAD_CANONICAL.tex`, SHA256 `d7b29854fc840c976e7ca03a4fec4ad79df1e87196df1ed2cc899de53d49d19e`.

The proof concerns the previously certified A13 curve over F2, with the integral Rosati-invariant O5 action supplied by the separately checked A33 supplement. It proves that every one of its 126 non-Weierstrass F128-rational points has canonical class of exact order 4159. Since the exact multiplicative order of 2 modulo 4159 is the odd integer 2079, none of these fixed canonical classes satisfies the sufficient good-prime condition of A29, over F128 or after a constant extension.

The proof does **not** claim that any of these pointed curves is a prescribed-point image in the rank-one quintic transfer of A33. It also does not claim a point-section collision: the geometric theta witness in A13 remains available. No inverse dihedral construction is used in this statement.

## Whole-proof checks

1. The three simple Artin--Schreier poles give genus two and two-rank two, with exactly the three rational Weierstrass points above 0, 1, and infinity. The A13 Frobenius polynomial is carried from its checked certificate; its opposite root pairs give the vanishing odd trace used for the F128 curve count.
2. Pairing opposite eigenvalues at the odd extension degree seven gives the Jacobian count `(1-beta1^7)(1-beta2^7)`, with beta roots of `Z^2-Z+4`. The recurrence gives trace -251, hence order 16636 = 4*4159.
3. The three nonzero differences of the rational Weierstrass points give all geometric two-torsion points. Therefore the rational two-primary subgroup, of total order four, is already `(Z/2)^2`; there is no rational element of order four.
4. For any Weierstrass W, `kappa_R = 2[W-R]`, so the two-primary component is zero. For non-Weierstrass R the class is nonzero, since `2R ~ K` means that `2R` is a canonical hyperelliptic fibre and thus R is ramified. Primality of 4159 proves the exact order.
5. A fixed geometric divisor class retains its exact order under extension of constants. No new primary component of that fixed class can appear.
6. The explicit point encoded `(3,54)` is verified independently by the finite-field script; its exact canonical order follows from the divisor argument, not from a claimed Jacobian-divisor calculation.
7. The curve is defined over F2, so the twist identification in the final scope paragraph is literal and does not hide an imperfect-field assumption.

## Exact new finite certificate

I read all of `verify_RM5_bad_canonical.py` and executed it. Script SHA256: `106ceb42a28a665d5d91aeff9db95d65614545dbfb94cf97aa97f6d1290cb5f5`. Output SHA256: `4a28d100324056707964c0aa989c998beca30f2c67dcd6416b28b6dfef93c6d9`.

The script implements F128 directly as F2[a]/(a^7+a+1), checks an inverse for every one of the 127 nonzero residue classes (thereby also certifying this quotient is a field), enumerates every affine nonbranch solution, and retains all 126 coordinate pairs. Adding the three branch points gives 129. It verifies the displayed point `(3,54)`, the recurrence and Jacobian count, primality by trial division through 64, and the exact-order residues

`2^2079=1`, `2^693=2554`, `2^297=1245`, `2^189=102` modulo 4159.

These exclude the proper prime-divisor reductions of 2079 = 3^3*7*11. This is a new independent finite-field and modular calculation, not an additional implementation of Jacobian arithmetic or a formal proof assistant verification.

## Primary locators checked

- J. S. Milne, *Jacobian Varieties*, 12 June 2021 author version, Theorem 11.1, printed p.35 and its immediate derivation from Proposition 11.2: https://jmilne.org/math/xnotes/JVs.pdf . Reopened and read, including the displayed proof in the retrieved pp.35--37 section. Retrieval reference: `turn346662546view0`.
- J. S. Milne, *Abelian Varieties*, Theorem 19.1(b), Jacobian rational-order product: https://jmilne.org/math/xnotes/AVs.pdf . This is the same primary point-count input already read in the earlier A13/A33/A36 work; no newly claimed complete reread of the entire chapter.
- The A13 numerical polynomial and the A33 integral-RM5 construction are previously checked inputs, explicitly identified in the source. Independent whole-proof readers have been requested for A38; their eventual events are separate from this author audit.
