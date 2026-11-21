# Independent complete review of THETA3-C19

**Reviewer:** GPT-6 Astra Pro, run `/root/theta_032`, 21 November 2026. The inherited effort label is not separately exposed. This is an independent mathematical proof check, not a Lean or computer-algebra certificate.

**Text read:** the whole of `work/paper_C19.tex`, including every displayed equation, followed by the author's explicit CM-embedding normalization. I also reread the relevant C18 common-frame and Bell-polynomial arguments. **Result: PASS at the hypotheses and normalization stated in C19.** The small request to specify the algebraic differential and the matching CM embedding was sent to the author and has been accepted.

## 1. Invariant derivations and completion of the CM action

The argument works over the possibly nonreduced ring R/pR. An invariant derivation is determined by its tangent value, so the p-th iterate is H times D. The CM pullback relation gives `(a^p-a)H=0`; the chosen residue in F_(p²) outside F_p makes the first factor a unit even over R/pR. Thus D^p maps the entire integral power-series ring into p times that ring. Iteration gives the stated floor(k/p) operator bound.

The estimate `[p^r](t) in (p,t)^(r+1)` follows by substitution, since `[p](u)=pu+O(u²)`. For a-b divisible by p^r, the formal-group addition identity makes the difference of the two endomorphism series lie in the same ideal. The (p,t)-adic completion therefore supplies the local CM action. In a ramified DVR, this topology remains equivalent to the usual maximal-ideal/formal-parameter topology; convergence of every fixed coefficient is p-adic. Composition and addition are continuous for the topology being used.

The Teichmüller average has derivative one and is an integral coordinate change because p²-1 is a unit. In that coordinate, all roots of unity act linearly and the normalized logarithm has its first possible nonlinear term in degree p². Accordingly, translation Hasse operators equal D^j/j! only for j<p². The proof never makes this identification for its high-index operators.

## 2. Torsion, translation operators, and trace-zero iteration

The special fiber's geometric p-torsion is an F_(p²)-module with at most p elements. Hence it has only its identity, and all characteristic-zero p-torsion lies in the formal group. The generic p-torsion is one-dimensional over F_(p²); the linear Teichmüller action makes its nonzero coordinates exactly ζξ. Weierstrass preparation then gives a monic torsion polynomial X^(p²)-βX with β=-p/α and α a unit. This does not require the full multiplication series to be a polynomial.

Each translation Hasse operator preserves R[[X]], commutes with all the others and with D, and is continuous for the uniform p-adic topology. Evaluation at formal torsion points converges coefficientwise because their coordinates lie in the maximal ideal. The grouped torsion power-sum series has coefficients of valuation tending uniformly to infinity. Its operator H is therefore integral and convergent, commutes with D and the torsion trace, and preserves the trace-zero submodule.

On that submodule the identity D^(p²-1)=p^p u(1+H) has u a unit: v_p((p²-1)!)=p-1. Iteration is legitimate because the new vectors remain trace-zero. For 0≤r<p²-1, v_p(r!)=floor(r/p)=floor(rp/(p²-1)); combining the quotient and remainder gives the exact trace-zero slope in C19. All factorial and sign constants check.

## 3. Exact trace ideal and the general integral-function estimate

For A=R[[S]] and B=R[[X]], S=[p](X), the extension is finite free of rank p². Preparation of `[p](X)-S`, together with the invariant differential identity, gives P'_S=pv with v a unit in B. Lagrange interpolation proves Tr(b/P'_S)=the top coefficient of b in its representative of degree below p². Substitution of vb proves Tr(B)⊂pA, and b=v^(-1)X^(p²-1) attains p. Thus the trace ideal is exactly pA.

The algebra trace pulled back to B equals the sum of translations by p-torsion: after adjoining the torsion its p² distinct roots are F(X,u). Hence g=pf-[p]^*(Tr(f)/p) is trace-zero. Invariant differentiation of the pullback contributes the factor p^n. Since floor(np/(p²-1))≤n, the strong integral-function bound follows with loss one. The example f=t^(p²-1) gives precisely (p²-1)! at the relevant derivative, proving the asserted uniform sharpness.

## 4. The de Rham calculation of e2*

In the specified integral short Weierstrass model, η=xω has only its double pole at the origin. The principal part is the exact differential d(-1/t). The two regular representatives and that transition function define an integral Čech-de Rham class. Its image in H¹(O) has Serre-duality pairing ±1 with ω, so (ω,η) is an integral basis. The Hodge exact sequence used here follows for a relative curve because exact differentials have zero residue.

The CM action has matrix `[a]^*ω=aω`, `[a]^*η=bar(a)η+cω`, with c integral; the second diagonal entry follows from the degree multiplier of the cup pairing. The analytic periods of η are the negatives of sigma quasiperiods. Consequently η+e2*ω is the conjugate CM eigenclass and c=(bar(a)-a)e2*. The denominator is a unit at an inert prime, proving both algebraicity and integrality. This argument neither replaces R/pR by its reduction nor assumes an unproved integral Hodge splitting.

## 5. The actual reduced theta normalization and its weaker slope

The reduced normalization is exp(-e2*z²/2)σ(z), with derivative one at the origin. The Fock translate has the same quadratic factor in z times C18's specified translated sigma function. Thus all tame translated sections share the exact factor Q=exp(-e2*λ²/2)σ(λ)/t. Equal tensor degrees cancel it.

For log Q, the only new low-order jet relative to C18 is l₂=-e2*, now proved integral. All odd jets vanish, and the higher even jets are derivatives of the integral rational function B=D²log(σ(λ)/t). The additional Bell inequality at j=2 is valid. The remaining inequalities and denominator estimates are exactly the already checked C18 argument. Exponential Bell polynomials have integer coefficients for every integer tensor degree, including negative degrees. Convolution with an arbitrary integral v and the invariant-derivative congruence give the stated weak slope 1/(p²-1), while degree zero has the stronger slope p/(p²-1).

The proof correctly distinguishes these two slopes. It does not claim raw reduced theta is an integral power series, nor that an arbitrary normalization satisfies the same derivative estimate.

## 6. Primary-source checks

- Read Bannai–Kobayashi, arXiv:math/0610163v4, Example 1.9, printed pp.10–11, directly in the local text: the Hermitian multiplier, sigma quasiperiod formula, reduced normalization, and derivative-one normalization are as used.
- Read Conrad, *Minimal models for elliptic curves*, Definition 5.1 and Example 5.3, printed p.13, in the local author text: an abelian scheme is the Néron model of its generic fiber, and the mapping property extends endomorphisms. Group-law identities extend by uniqueness.
- Visually read Katz, *Divisibilities, congruences, and Cartier duality*, printed pp.671–673, including equations (3.1)–(3.8), Theorem 3.11 and the proof of Part I. The comparison and attribution in C19 are accurate. C19 proves the extension it needs using its exact torsion polynomial and high translation operators; it does not assert Katz's stronger Cartier congruences.

The use of relative Serre duality, Weierstrass preparation, the characteristic-zero formal logarithm, and the basic degree/separability facts for elliptic multiplication is cited mathematical background. The new implications and calculations above were independently reconstructed in full.

## 7. Subsequent formal-module and independent-product addition

I read the complete appended paragraph after the original full review. **PASS at its stated strict one-dimensional height-two hypotheses.** The Teichmüller averaging, prepared p-torsion orbit, factorial identity, trace ideal and trace projection remain valid for p=2 and p=3. No sigma or de Rham claim at those primes is inferred. The proof gives coefficientwise operator divisibility, since the trace-zero iteration is an operator identity and D^n[p]^*=p^n[p]^*D^n holds before evaluation. Applying the one-variable result coefficientwise in the other independent variables is legitimate, and commuting invariant derivations multiply the p-divisibilities. No arbitrary higher-dimensional formal group is treated as a product without the stated integral idempotent decomposition.
