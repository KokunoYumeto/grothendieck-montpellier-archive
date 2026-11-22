# Independent review of essential self-duality reduction

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21. No Lean kernel build was run.

The whole proof in `unitary_audit/reducible_comparison/essential_selfdual_reduction.tex` was read and checked. PASS at SHA256 `07e408de70dd8c88974b645fdb4548095780d52fef4d5fbb45f2d6510f7e76af`.

For the first assertion, the exact ordered inertia characters multiply to one at every p-adic place, while R is unramified away p. The determinant is therefore a character of the finite ideal class group. Its residual value is one, so its finite image consists of principal-unit roots of unity and has p-power order. The hypothesis p not dividing h(E) kills that image. The proof does not assume actual determinant one merely from residual determinant one.

For essential self-duality, determinant one implies that the twisting character has cube equal to one. The inertia-character multiset identifies its restriction with one of `1, epsilon^e, epsilon^-e`. The latter two have infinite order, so the restriction is trivial. The global residual multiset then identifies its reduction with one of `1, omega^e, omega^-e`. The latter two are ramified at p because p is unramified in E and the exponent is nonzero modulo p-1. Therefore the reduced twist is trivial, and reduction is injective on cube roots of unity as p>3. This handles the possible order-three residual cyclotomic character without silently excluding that case.

The actual-source corollary correctly combines the exponent-2e unit's Type II exclusion with the exponent-e unit's self-dual Type I exclusion. Its assertion about a nonzero strict Selmer length uses the carried actual TwoPt existence argument, not an inference from the ambient automorphic spectrum. The remaining source is nonessentially self-dual stable rank three; the proof gives no emptiness or Selmer-length conclusion for that class.
