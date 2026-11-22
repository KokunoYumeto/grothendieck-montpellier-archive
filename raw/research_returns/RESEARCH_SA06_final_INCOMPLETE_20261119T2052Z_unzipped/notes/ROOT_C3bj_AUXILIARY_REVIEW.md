# Independent checks for the unregistered direct Milnor approach

AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, `/root`, 19 November 2026, 14:40–14:45 UTC. This record certifies the auxiliary arguments actually read; it does not register a higher-dimensional or all-prime local counterexample.

## Divisibility of the preceding Milnor cohomology group

Root independently read the complete degree-two proof in agents/cycles/k2_cohomology_divisibility_draft.tex and its subsequently appended all-degree induction. The assertion is that H^a(P^m×W1×...×Ws×C,K^M_(a+1)) is divisible, for any smooth projective connected curve over an algebraically closed field, smooth cubic surfaces, and all nonnegative a,m,s. This is a statement about Zariski sheaf cohomology; a decomposition of K1 does not imply it.

The proof needs only generation maps. For P^d×S, localization at its hyperplane and affine homotopy give a surjection from G^(a,b)(S) plus G^(a-1,b-1)(P^(d-1)×S). The restriction of the first summand lifts every class on A^d×S. For a blow-up of smooth varieties, an arbitrary class b differs from pullback of its proper pushforward by a class supported on the exceptional divisor, because the morphism is an isomorphism on its complement. Localization supplies the second generator group G^(a-1,b-1)(E). This argument does not require a complete blow-up decomposition or a global identity pi_*pi^*=1.

The base curve has only H0(K1)=k* and H1(K2), the latter a quotient of a direct sum of k*, on the indicated diagonal. Both are divisible. Projective-space induction preserves this property. A cubic surface is obtained by six blow-ups of P2 at distinct points; after product with S each exceptional divisor is P1×S. Induction on the number of these blow-ups and then the number of cubic factors proves the statement. Every displayed shift lowers the cohomological and Milnor indices together, preserving their difference one. Direct sums and quotients of divisible abelian groups are divisible. The proof is integral in every characteristic.

Root freshly opened Rost's complete primary PDF and actually read Section5, p.356 (localization with the preceding grading conventions); Corollary6.5, p.360 and the following pullback/product compatibility; Proposition8.6 with its proof, p.370; Proposition4.1(3) with its proof, p.351; and Section12, p.382 (pullback construction and locality on open subsets). The author's corrections page was also opened. Neither the unused erroneous flatness remark nor the corrected Section14 sign formulas enter this generation argument. The additional identification of the naive Milnor sheaf with its Gersten sheaf uses the already opened Kerz theorem in its infinite-field scope, not an assertion about arbitrary nonreduced schemes.

Outcome: PASS for the full typed auxiliary induction. No higher Milnor–Quillen comparison is asserted.

## Canonical relative Milnor differential quotient

Root independently read agents/frobenius/K2_relative_Milnor_all_characteristics.tex in full at14:43:04UTC. Its central argument was also independently derived by root and communicated before the typed file was read. It applies to a square-zero thickening E of a smooth k-variety V with invertible ideal I, in every characteristic.

The sheaf J_r=ker(K_r^M(E)->K_r^M(V)) is generated locally by symbols with an entry1+i. Units and downstairs Steinberg relations lift modulo the nilpotent ideal. Multilinearity therefore shows pJ_r=0 in characteristic p, including p2. This uses the naive unit-symbol Milnor ring directly and makes no comparison with Quillen theory on E.

Formal smoothness splits the local algebra extension. On that local splitting, Omega_E restricted to V is Omega_V plus I, with i mapping to di. Thus the canonical conormal sequence is short exact even though the square-zero immersion is not a regular immersion. Its rank-one kernel gives a canonical isomorphism from I tensor Omega_V^(r-1) to the kernel of the r-th exterior-power projection. Ordinary dlog on Milnor symbols, restricted to V, takes every relative class into that kernel. The resulting canonical quotient sends {1+i,u2,...,ur} to i tensor dlog(ubar2) wedge ... wedge dlog(ubarr). No choice of a splitting or ideal frame remains. A stalkwise differential da is a multiple of dlog of the unit a, or of1+a when a is a nonunit, proving surjectivity. There is no division by p, two, or a factorial.

For actual line bundles, an endpoint trivialization on V gives transition functions1+a_ij. Their product with divisor transitions has relative symbol cocycle {1+a_ij,g_jk}, and the quotient sends it to the coherent cup a cup dlog(D|V). A nonzero coherent image proves that its class in H2(J2) is nonzero. No acyclicity assertion for the chosen J2 cover is needed: the Čech cocycle maps canonically into sheaf cohomology, compatibly with the coherent image. The preceding divisibility theorem kills the boundary H1(K2^M(V))->H2(J2), giving the required injection into absolute H2(K2^M(E)).

Outcome: PASS for the all-degree relative quotient and the stated degree-two product compatibility. The optional Dennis–Stein paragraph is a separate check and is not needed for this Milnor proof.

## What is still needed for the proposed C.3bj

The full combined local theorem must still state and verify the all-prime quartic and cubic geometry, smooth incidence choices, the actual proper-curve family, higher-neighbourhood uniqueness, target vanishing, the integral exceptional Chow relation, and Milnor cycle-class compatibility on the actual strict-local resolution. The exact source for the last compatibility is being separately opened and audited by the owners. Only after the combined typed proof and independent reviews will its local counterexample be registered.

For higher codimension r>=3 the same auxiliary lemmas are available, but the exceptional Chow boundary is a separate obstruction. One cannot silently reuse the r2 injectivity argument on Pic(V) for CH^(r-1)(V). For a projective-space factor of dimension at least r-1 the coefficient recurrence gives integral injectivity of multiplication by its tautological class plus an ample class; smaller projective-space dimensions require a new argument. The relative detector alone is not a proof that a class survives on the puncture.
