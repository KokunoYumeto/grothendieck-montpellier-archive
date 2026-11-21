# Independent review of the global mixed cup obstruction

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21. No Lean kernel build was run.

PASS after reading the entire `global_mixed_cup.tex` at SHA256 `f3872ccd0441efea705fd42674ac4968523942a2bfd056ab19e5562f78918e35`. The conclusion is a second-order **characteristic-p Artin deformation**, with the specified local ordinary condition. It is not a characteristic-zero point of the global source, a construction through all higher orders, or a vanishing theorem.

## Cohomology and exact ramification scope

The set is exactly `S={infinity,p} union {q:q divides D}`. The a=0 auxiliary bridge supplies h(E) prime to p and the zero class component with character eta omega in E(mu_p). I reread the whole bridge proof, including the eigenspace orientation and CM unit mirror argument. Restricting a strict dual class to E(mu_p) embeds it into the Hom space of that **same** character, so the strict dual group is zero. There is no inverse-character mistake.

Finite-module Poitou–Tate duality therefore kills Sha² for eta. All local H² groups vanish at the specified S: eta omega is nontrivial on inertia at p through omega and at q|D through eta; odd p kills higher real cohomology. Thus the full global H² is zero. The global Euler characteristic of the odd eta character gives H¹ dimension one.

At p, the quotient of H¹ by its unramified part has dimension one for either splitting sign. Its global kernel restricts to an everywhere-unramified homomorphism over E. At q|D, both H⁰ and H² for eta vanish, so local H¹ is zero by the away-p local Euler characteristic. Class number prime to p kills the remaining global kernel. This proves the localization isomorphism, with no claim after adding arbitrary extra ramification primes.

## Matrix and local-condition audit

The adjoint semidirect characters of `X=E12+E23`, `Y=E21-E32`, and `[X,Y]=diag(1,-2,1)` are respectively eta psi, psi inverse, and eta. Direct finite BCH expansion gives the displayed cup-difference equation. Since the cube of the maximal ideal `(s,t)` is zero, all exponential/logarithm formulas terminate and use only invertible small denominators.

I checked the gauge formula explicitly. Conjugation by `exp(t d Y)` with `v(g)=beta(g)d-d` kills the negative first-order cocycle and changes the mixed coefficient to `w - d(1+beta)u/2`. The new coefficient is an eta cocycle. The localization isomorphism permits adding a global eta cocycle to make its local class unramified. Eta is trivial on p-adic inertia, so coboundaries vanish there; the actual inertial mixed coefficient is therefore zero. The resulting family is upper triangular with the exact specialized diagonal.

At each q|D, local H¹ for both eta psi and eta vanishes. Successive near-identity conjugations remove the positive and mixed terms; the negative term is unramified by its stated strict hypothesis. The resulting representation is identity on inertia intersected with G_E, and conjugating back preserves identity. This establishes the actual away-E inertia claim.

The fact that a nonzero positive class exists follows from the odd global Euler characteristic. A negative strict class remains a hypothesis, equivalent to a piece of the original unresolved problem. The calculation proves that the first mixed obstruction and its ordinary correction cannot supply a contradiction under the class-number unit; it does not assume or establish the negative class's existence.

## Exact primary statements inspected

Milne, *Arithmetic Duality Theorems*, second edition (2006), preserved author PDF `unitary_audit/reducible_comparison/primary/milne_ADT_2006.pdf`:

* Chapter I, page 48: definition of the restricted-ramification Galois group and S-integers.
* Pages 56–57: definitions of Sha and Cartier dual, and Theorem 4.10(a), finite-module pairing with order invertible in S-integers.
* Page 28: Corollary 2.3, including finite H²/H⁰ local duality.
* Page 31: Theorem 2.8, local Euler characteristic, with its coefficient-order hypothesis.
* Pages 66–68: finite-S setup, Theorem 5.1 and Remark 5.2(c), including the ordinary real H⁰ normalization.

These complete statements and nearby definitions were read for scope. The foundational proofs of arithmetic duality and Euler characteristics are imported, not claimed freshly reconstructed.

## Noncritical-scope clarification

The exact final diff was independently read. Current proof SHA-256 `b92014e58b47287a056f1bdf1264eeea536088f4d7234a745ce431702d85ff9a` adds that all nonzero differences among e,0,-e are even and hence cannot equal1 modulo p-1, an even integer. This correctly supplies the cited residual noncriticality and imposes no characteristic-zero crystalline-point condition on the Artin coefficient ring. The theorem statements and calculations are unchanged. PASS.
