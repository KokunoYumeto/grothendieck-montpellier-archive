# Independent whole-proof and whole-code review: ordinary cubic Massey condition

**PASS** for all of `unitary_audit/reducible_comparison/cubic_massey_condition.tex`, SHA-256 `cfce735be0b46a205725f250dcd9ff835b0bafe6eb3dd7454e5a3ecd041b2895`, and the complete symbolic certificate source SHA-256 `1217f8d44c5bbd824237320a4f9498447e162a92fc3dd98a9def5c75515795b4`. A fresh execution of a byte-identical source copy in `lean_chain/cubic_massey_replay` passed all fifteen identities and reconciled every report field other than the fresh timestamp. The author source/report were not changed.

## Exact equivariant lifting problem

The algebraic torus, rather than only finite residue-field scalars, gives the asserted integer weights. The five involution signs and all Galois characters agree with direct matrix conjugation. The weight-two Lie lines have the wrong involution sign for s^2 and t^2, and weight-three lines are absent. At degree two only st·Z remains; at degree three the allowed lines are s^2t·U and st^2·V. Thus the displayed logarithm contains every term in this specifically equivariant determinant-one problem. All needed exponential/logarithm denominators are units for p>3.

Although the earlier quadratic presentation used s^2=t^2=0, the same equation for w defines the stated family over the full degree-two truncation: the pure first-order directions exponentiate along individual abelian Lie lines, and there are no extra permitted pure-square logarithmic terms. No extra global lifting hypothesis is silently inserted there.

## Ordinary normalization and exact cubic identities

The local primitive of v at p is unique because its inertia character is nontrivial. The difference between two ordinary choices of w is an eta-cocycle whose localization is unramified. The already proved localization isomorphism modulo unramified classes forces that global class to be zero. The resulting global coboundary is realized by the allowed exp(st·aZ) conjugation and preserves both gradings.

The brackets are [X,Y]=Z, [X,Z]=-3U and [Y,Z]=3V. I independently expanded the cubic BCH contributions: the half-bracket terms give the first terms of Omega_+ and Omega_-, and the nested brackets give -(A-a)(Ab-Ba)/4 and +(B-b)(Ab-Ba)/4. The cochain differential convention therefore makes the raw obstruction -Omega_+, exactly as stated.

For the Massey comparison, d(uv)=-(u cup v+v cup u) and dw=-(u cup v-v cup u)/2 give the two specified defining equations. Direct expansion confirms Omega_+=-3Theta/2+d(u^2v)/4, hence the raw obstruction image is +3[Theta]/2. The symbolic certificate independently verifies these polynomial identities, both two-cocycle identities, the determinant and all involution signs. Its generic scalar characters specialize to the actual characters; it does not assume a numerical sample or a finite prime range.

## Local matching and relative obstruction

The eta·psi^-1 direction has zero global H2 and an isomorphism from global H1 to its local H1 at p. Its local H1 at q|D is zero, so the solution can be made ordinary at p and requires no additional away-prime matching.

For the rational direction, after removing the lower first-order term at p the quadratic family is upper triangular with fixed inertial diagonal. A cubic upper correction has local H2 zero and arbitrary H1 difference; this proves L_p=full H1. At q|D, the already available alpha/eta coboundary conjugations reduce the family to exp(t vY)r0, which lifts directly at every truncation. For the rational cubic coefficient, killing inertia after E is equivalent to unramifiedness over Q: the remaining inertia quotient has order at most two, prime to p. Thus L_q is exactly the unramified subspace.

The relative cochain quotient retains the local primitives and gives the exact sequence in CM.15 by subtracting a global primitive when the global cocycle is exact. Its zero class is equivalent to a global correction matching all allowed local lifts. The two cubic directions are independent modulo total degree four. Allowed changes of w or the first-order representatives induce conjugate problems and act trivially on the degree-three kernel, so the obstruction is well defined.

## Arithmetic dimension and limits

Milne's exact global orthogonality identifies the dual of the localization cokernel with dual-Selmer modulo strict Sha1. Combining its dimension with the Sha2/Sha1 pairing yields the dimension of the full dual-Selmer group. Local unramified orthogonality is applicable at q|D because q differs from p and the finite dual takes values in roots of unity that are units. I independently read the entire proof of Milne I2.6, printed30–31, as well as the previously checked I4.10(a,b) exact sequence.

The dual conditions are zero localization at p and unramifiedness elsewhere. Restriction to Q(mu_p) therefore gives the full delta=omega^(1-e) class component. The unique prime over p is principal, so every everywhere-unramified class-group homomorphism has zero local Frobenius there; prime-to-p descent preserves this vanishing. There is no quotient by primes over D because their local condition is only unramifiedness. The proof correctly claims a dimension equality, without manufacturing a canonical class-group-valued functional from two unrelated short exact sequences.

The rational Bernoulli unit suffices to annihilate this obstruction space by the already accepted Herbrand implication. It does not annihilate the original negative strict class. The displayed formulas and linear choices of primitives justify linearity in v and quadratic scaling in u.

The final boundary is essential and explicitly correct: no arithmetic nonvanishing/injectivity of the particular relative class is proved; no actual source is proved to carry the stipulated two-parameter jet; and no characteristic-zero source point follows from the cubic lift. This is a precise higher lifting criterion and obstruction-space computation, not a new Selmer bound or K-group vanishing. No Lean kernel build was performed.
