# MA-RB-009: a genuine family limits the universal numerical criterion

Date: 2026-11-21.
Author and author checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

## Status

The complete298-line proof is modules/s5_endpoint_scope.tex, MA-RB.97–106. The author read every line after writing and passed the whole proof. Root independently read the entire proof and passed all construction, analytic-bound and scope steps; root owns integration.

This is a proved failure of a proposed universal numerical-exclusion route. It is not counted as a smaller shared-zero gate, a comparison counterexample, or a beta-excess example.

## Actual construction

For each prime q>5, choose the least positive a_q with q a_q≡2 modulo3 and q a_q≡1 modulo5. The polynomial

    f_q(X)=X^5+q a_q X+15q

is Eisenstein at q and strictly increasing on the real line. Thus the degree-five field has one real root and two nonreal pairs. Modulo3 it factors as X(X−1)(X+1)(X²+1), with one irreducible quadratic; modulo5 it factors as X(X²+2)(X²−2), with two irreducible quadratics. The squarefree reductions and simple-root Hensel lifting give unramified Frobenius elements of types2A and2B in the normal closure.

The transitive degree-five group containing the transposition at3 is S5. The proof uses the connected graph of conjugate transpositions, not a classification table of transitive groups. The normal closure has degree120, signature(0,60), and the exact complex-conjugation and prime-five conditions of Calegari's specified family.

Every root has q-adic valuation1/5. Hence q ramifies in the normal closure and divides its discriminant. The text spells out the discriminant trace-pairing argument. Therefore Delta_(L_q)≥q tends to infinity, and the construction gives infinitely many genuine normal closures.

## Exact analytic limitation

Set

    C0=60(1+log(2pi))+5log5+40/7,
    C_Delta=(1/2)logDelta−C0.

The discriminant-aware all-prime subtraction from RB008 is uniformly at most40/7. This follows from log(n)≤n, n^6−1≥(63/64)n^6, and the elementary integral bound for sum_(n≥2)n^(−5). The prime5 term is at most5log5. The already proved Jensen estimate and the gamma recurrence give psi(sigma)≥log(sigma)−1/sigma≥−1. Consequently Hsharp_Delta(sigma)≥C_Delta for every sigma>1.

For every fixed positive integer k and C_Delta≥18k,

    1/4−9k/C_Delta ≤ script-J_(Delta,k) < 1/4.

The lower polynomial is increasing for x=sigma−1/2≥1/2. At C_Delta≥40k this lower bound is1/40. Along the genuine constructed fields, script-J_(Delta_(L_q),k) therefore tends to1/4, and the numerical nonpositivity test is eventually false.

This proves that the currently retained Euler/gamma inequality cannot by itself provide universal exclusion under the actual family hypotheses. It says nothing about existence of the hypothetical comparison pole, either shared vanishing factor, or an off-center zero. An additional arithmetic restriction is still required.

## Checks and inherited inputs

The whole author reading checked every CRT and factorization step, the direct irreducibility proof, the Hensel interpretation in the normal closure, the connected transposition graph, the real and normal-closure signatures, the valuation and discriminant arguments, all constants in the positive prime bound, the gamma recurrence, derivative threshold18k, positive1/40 criterion, and the squeeze limit.

No finite-representation certificate, numerical zero search, or numerical minimization was performed or needed. The exact target-family locator remains Calegari's Theorem1.1 assumptions(1)–(2), supplied S5ArtinWeb.tex lines123–136. The inherited finite-cover convention is RB.91 and SGA1 ExposéV section7, with the previously recorded Deligne Artin-motive placement. Simple-root Hensel lifting and the normalized local valuation are declared classical field-theory facts; no fabricated source theorem number is attached to them.
