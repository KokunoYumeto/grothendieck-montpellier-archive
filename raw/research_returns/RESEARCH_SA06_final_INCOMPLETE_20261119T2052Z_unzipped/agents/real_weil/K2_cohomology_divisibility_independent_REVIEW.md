# Independent review: the Milnor-cohomology divisibility lemma

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not exposed. Full mathematical reading and fresh primary-source reading were completed by the observed tool clock **2026-11-19 14:54:38 UTC**. This record was written after checkpoint16 released its filesystem freeze.

## Exact reviewed material and conclusion

Read the complete `agents/cycles/k2_cohomology_divisibility_draft.tex`, including its higher-degree extension. **PASS** for the degree-two result and the higher-degree Milnor result in their stated smooth-projective, algebraically closed-field scope. The optional degree-two Milnor–Quillen comparison is only on the smooth variety and does not identify either theory on a nonreduced thickening.

The projective-space argument has the correct localization indices: the exceptional hyperplane term for G^(a,b) is G^(a−1,b−1), while affine homotopy identifies the open term with G^(a,b) of the base and projection pullback actually lifts it. For a blow-up between smooth varieties of the same dimension, proper pushforward and the smooth-target pullback preserve the indicated bidegrees. The difference beta−pi* pi_* beta restricts to zero off the exceptional divisor by the exact open compatibilities, so localization supplies its exceptional preimage. No full blow-up direct-sum theorem has been assumed.

For degree two each exceptional H^0(K_1) is k*, and the curve H^1(K_2) is a quotient of a direct sum of k*. These groups and their quotients are divisible. In the higher-degree induction, the smooth product exceptional divisor is P^1×S, so the previous projective-space step proves divisibility of the entire exceptional term. The a=0 and negative-index cases are correctly separated. All operations retain integral coefficients and the fixed Milnor grading.

## Fresh primary inspection

Opened the complete Rost 1996 primary PDF at https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf and read the exact inputs: Proposition4.1(3), printedp351 (proper push/open pullback); Section5 pp355–356 (grading and localization); Corollary6.5 and proof p360 (Gersten sheaf cohomology); Proposition8.6 and proof p370 (affine-bundle homotopy); Section12 pp382–383 (pullback to a smooth target, locality under opens, Theorem12.1 and Proposition12.2). The author's corrections page was opened at https://www.math.uni-bielefeld.de/~rost/chowcoeff.html. Its unused false flatness remark and corrected Section14 signs do not enter the proof.

Freshly opened Kerz's full author PDF dated29April2008 and read Definition2.1 plus the excellence assumption preceding Theorem7.1, that theorem's exact regularity/field/infinite-residue hypotheses, and Theorem7.5. They are satisfied by all smooth varieties in the lemma. The all-characteristic cubic blow-up input is the already opened Huybrechts Chapter4 Proposition2.4, p178, independently checked in C3bi; no new opening of that page is claimed in this particular receipt.

No program was executed for this lemma. This is a full targeted proof/source check, not a formal proof-assistant certificate or a computational verification of all instances.
