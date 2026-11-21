# A30 proof and finite-arithmetic audit

- Date: 2026-11-21.
- Author/reader: GPT-6 Astra Pro, `/root/effective_galois`; effort not exposed.
- Final source: `work/effective_galois/A30_GENUS_THREE_POINTING_COUNTEREXAMPLE.tex`.
- Final source SHA256: `cf643b8dbc2b236ff64cebcb5bd27ba5f7b18cb320b3c5aa91a8bb82b727371e`.
- Result: **PASS after complete self-read, independently corroborated by parent and sibling whole-proof readings.** The final change after their initial readings only makes the conclusion's scope explicit. No formal verification is claimed.

## What the result proves

There is a genus-three, rank-one curve over `F4`, with a rational non-Weierstrass base point and a rational Weierstrass point, and a constant cyclic quotient of order three which detects both their difference and the based canonical class. Its pointed split connected étale cover nevertheless has even relative class number. Thus the genus-two assertion that **every** detecting quotient has odd relative class number cannot be extended with the same hypotheses. This does not exclude witnesses from other quotients or higher prime powers on the same pointed curve.

The equation is `z^2+z=1/(t^2+t)^3`. Its map to the supersingular elliptic curve `y^2+y=x^3` is given by `x=1/(t^2+t), y=z`. The elliptic quotient is branched at `(0,0)` and `(0,1)`. The based translated Lang quotient of order three has three rational points above the first and one closed degree-three point above the second. These unequal branch splitting types make the relative class number even.

## Complete mathematical checks

1. The two poles of order three give genus three and rank one. The point at `t=infinity,z=0` is unramified for the hyperelliptic double cover, while the point at `t=0` is ramified. The canonical class is four times that Weierstrass point.
2. The elliptic group over `F4` has nine points and every nonzero point has order three, proved by the tangent calculation. A quotient detecting `(0,0)` therefore exists.
3. The factor of the Lang map has constant kernel. Its image on rational points is exactly the chosen kernel subgroup, with Frobenius translation in the quotient as stated. Translating by `(0,0)` gives the desired split fibre and the degree-three branch fibre.
4. The pullback cover is geometrically connected because the geometric function-field extensions of degrees two and three are linearly disjoint. It is étale of degree three over the genus-three curve and has genus seven. Functoriality of the based Abel map identifies its rational character with the stated norm character, which is surjective because it detects the explicit point difference.
5. Every split or inert unramified degree-two Euler factor has the same reduction modulo two. A ramified factor contributes exactly `1-T^d`. This gives the zeta congruence directly as a formal power-series identity. Removing the zeta denominator gives the displayed polynomial identity; the branch degrees are `1,1` downstairs and `1,1,1,3` upstairs.
6. Isogeny invariance of the elliptic Frobenius polynomial and the Jacobian norm/pullback decomposition give the reduced relative polynomial `(1-T)(1-T^3)`. Its value at one is zero. This is an exact parity result, not a numerical estimate.
7. The same Euler argument with character values gives the two reduced factors `(1-T)(1-zeta T)` and `(1-T)(1-zeta^2 T)`. Their degree-two reductions, within degree-four characteristic-zero polynomials, exhibit precisely the term unavailable in the genus-two linear argument.
8. The general rank-one genus-two double-cover construction has independent simple-pole and triple-pole Artin–Schreier classes. Its diagonal quotient is étale of degree two; its source has genus three, rank one, and the asserted movement of Weierstrass status. Its uniqueness is the one-dimensional geometric `H^1_et(-,F2)` statement.
9. This double cover is unavailable to the geometric prime-to-two fundamental-group quotient. Independently, the difference of the two downstairs branch points has exact order two, so every pulled-back odd character kills the upstairs difference under norm. These are separate obstructions to the suggested pointing repair; neither is replaced by a claim that all possible upstairs covers fail.

## Primary inputs and exact locators

- Rachel Pries and Hui June Zhu, *The p-rank stratification of Artin–Schreier curves*, Ann. Inst. Fourier 62 (2012), Lemma 2.6, p. 712. Primary PDF: <https://www.numdam.org/item/10.5802/aif.2692.pdf>. The lower-jump setup, statement, and short proof were opened and read in this run. Retrieved references: `turn111332570view0`, `turn982868494view0`.
- J. S. Milne, *Abelian Varieties*, author notes, Theorem 19.1(a)–(c), pp. 40–41, with the Frobenius determinant explanation: <https://jmilne.org/math/xnotes/AVs.pdf>. Primary statement and explanation opened and read in this run; reference `turn982868494view1`.
- The connected Lang-cover fibre computation is also proved in the already independently checked A12. The new Euler-factor congruences are proved in full in A30 and do not depend on an uncited higher-genus symmetry theorem.

## Executed finite certificate

Script: `check_A30_finite_arithmetic.py`.

- Script SHA256: `ccab61055b398763f2e3590739011aa356cd29a23d89dc2390bbd45504d18582`.
- Result: `A30_FINITE_ARITHMETIC.json`, SHA256 `017f0f58173226bcd76dbc720abbb623a1b2e6fad21f2b67a1450495db608f82`.
- Command: `python work/effective_galois/check_A30_finite_arithmetic.py`.
- Exit status: zero; all assertions passed.

The standard-library implementation checks the field arithmetic exhaustively, enumerates the nine elliptic points, checks the group law and all associativity triples, verifies the tangent polynomial, exhibits a basis and detecting quotient, and computes the branch translation cycle types. Independent direct point enumeration on the displayed equations gives:

| Field | Elliptic quotient points | Genus-three curve points |
|---|---:|---:|
| F4 | 9 | 8 |
| F16 | 9 | 16 |
| F64 | 81 | 80 |

Newton identities and the genus-three functional equation recover `H_D=1+3T+4T^2+8T^3+16T^4+48T^5+64T^6`, with the asserted reduction `1+T`. Finite polynomial arithmetic over `F4` verifies both character factors, their product, and the upstairs reduced polynomial. These checks corroborate the small-field inputs and exact algebra. They do not construct the full isogeny in coordinates, replace the geometric proof, or constitute a formal proof certificate.

## Independent readings and final narrow change

The parent reported a whole-proof PASS for the DC-tag version with source hash `c2dc1b108ad00c3cfd8613787a0fb394a8d7c2819e9d70de8f342da19c923026`. The sibling `/root/gt_certificates` likewise reported a complete proof PASS and checked the tag rename. The only subsequent source change replaces the potentially broad opening conclusion with the explicit every-detecting-quotient conclusion and states that other quotient or higher-power witnesses are not excluded. The proof and all thirteen numbered equations are unchanged. The finite checker was rerun against the final hash above.
