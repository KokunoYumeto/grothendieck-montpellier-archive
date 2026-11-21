# Independent whole-proof review: A27 all-extension augmentation obstruction

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Source reviewed in full: `work/row_audit/RANK_ONE_AUGMENTATION_OBSTRUCTION.tex`.
Source SHA256: `35e6cd0752198cbcd1e93eb634a44167007978c80d2a9568f2e2ba286c97acfd`.

## Outcome

PASS. The entire proof, all finite rows, and the full independent verifier were read. The verifier was copied into this reviewer's own work directory and rerun successfully; its JSON is byte-identical to the author's retained certificate. No source or final-paper edits were made. This is a mathematical review plus exact finite arithmetic reproduction, not a proof-assistant verification or an exhaustive search through covers.

## Frobenius input and factorization

The Artin–Schreier pole orders 3 and 1 give genus two and 2-rank one. The model's two branch points are rational. The direct finite-field enumeration checks 6 and 28 points over F4 and F16. In the larger field the proposed u = z^2+z satisfies u^2+u+1=0. The usual genus-two functional equation then gives the asserted polynomial T^4+T^3+6T^2+4T+16, whose factorization into A=T^2-T+4 and B=T^2+2T+4 is exact.

The two quadratic trace recurrences, the formulas |J(F_(4^m))|=e_m h_m and N_m=4^m+1-t_m-w_m, and the root bounds were checked. Since t_1=1 and t_m=t_(m-1)-4t_(m-2), t_m is 1 modulo 4 for all m>=1. Thus 4 divides e_m. The primary Milne source was reopened at https://jmilne.org/math/xnotes/AVs.pdf, Theorem 19.1(a)-(c), printed pages 40-41, including the Frobenius-kernel and characteristic-polynomial proof of (a)-(b). It supplies the stated Jacobian point-count convention and determinant formula. Web references: turn583736515view0 and turn583736515view1. This does not claim to reprove all background Weil theory.

## The block argument and all eligible primes

The key possible issue was whether fixed vectors can mix the two quadratic factors. They cannot for r>=5: Res(A,B)=36, so A and B are coprime modulo r. Cayley–Hamilton and Bezout decompose J[r] into ker A(F) and ker B(F). Since the total characteristic polynomial is exactly AB and the factors are coprime, these spaces each have dimension two and characteristic polynomials A and B, respectively. This argument does not need either factor to be separable; in particular r=5 is covered.

On the B-space, (F-2)B(F)=0 gives F^3=8. If a nonzero vector is fixed by F^m, then F^(3m) on that vector is both 1 and 8^m, so 2^(3m)=1 modulo r. Primitivity of 2 gives r-1 divides 3m.

If the total rational r-torsion dimension is at least two and the B-space contributes no fixed vector, the entire two-dimensional A-space is fixed by F^m. Its determinant is 4^m, so r-1 divides 2m. This proves the universal r<=3m+1 bound for all eligible r>=5 with torsion dimension at least two. The prime r=3 is correctly excluded from this decomposition and treated independently by the rank-four bound 3^4.

For torsion dimension one, an odd prime divisor of e_m is at most e_m/4, using 4|e_m. The displayed comparison with N_m is valid once sqrt(Q)>=8. Otherwise the prime divides h_m. The identity h_m=det(1-F^m on the B-space) modulo r makes that block have a fixed vector, so the preceding r-1|3m argument applies. The zero-dimensional case has quotient size one. Thus every odd primitive-root prime, including primes not dividing the group order and the exceptional prime 3, is accounted for.

## Induction and finite range

The m=10 numerical anchor is 31^4=923521 < 1044481=L_10. The identity L_(m+1)-4L_m=8*2^m-3 is positive, whereas the polynomial bound grows by at most (34/31)^4<2. The induction is therefore strict for every m>=10. In the one-dimensional case the comparison is equivalent to 3(s^2-6s+1)>0, valid for s>=8; its use at m>=10 is safely within range.

For m=1,...,9, complete factorization and exact orders of 2 give precisely the written eligible-prime lists. The bound r^min(4,v_r(|G|)) is valid since the rank is at most four and cannot exceed the r-adic valuation of the finite group order. Every tabulated bound is strictly below N_m. Primes not dividing |G| have quotient size one and are included by the table's convention.

## Certificate inspection and rerun

The full `work/row_audit/verify_A27_independent.py` was read. It imports no census or exploratory arithmetic code. It enumerates all affine y-solutions in two explicitly represented fields, uses a quartic companion matrix and exact Bareiss determinants for the nine point-count rows, uses complete trial division and direct modular order iteration, and checks both induction anchors. Its finite primality tests involve only small integers; the full trial-division loop itself also ensures complete factorization.

Verifier SHA256: `bb48c6297c8fe5ebeb5c74a3913b8ec9ce110cae4f29c60d24f483c7b20619f1`.
Certificate SHA256, both author output and this reviewer's byte-identical rerun: `7c3f28efd6ab0b4a000a2b6b43563e0c8762d2a390e1edfc63f30168ad951d16`.
Rerun files: `work/gt_certificates/positive_rank_theta/A27_review_rerun/`.

## Exact scope

This curve defeats both sufficient numerical inequalities in A26 over every constant extension. The proof does not claim nonexistence of an actual rational relative-class-number witness, geometric theta torsion, or a primitive-zero cover. It does not weaken or contradict A26's conditional implication.
