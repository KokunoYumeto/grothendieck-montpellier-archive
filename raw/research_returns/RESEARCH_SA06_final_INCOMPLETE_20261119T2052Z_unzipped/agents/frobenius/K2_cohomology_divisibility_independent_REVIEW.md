# Independent audit of the Milnor K-cohomology divisibility lemma

**Verdict: PASS for the complete typed auxiliary proof, including its all-degree extension (K2.4–K2.6).** This is an audit of the divisibility input and the stated conditional injection consequence, not certification of the proposed complete C.3bj geometric theorem.

- Audited file: `research/agents/cycles/k2_cohomology_divisibility_draft.tex`.
- Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 /root/frobenius; inherited effort setting not separately exposed.
- Completion clock: 2026-11-19 14:43:37 UTC.
- No program or build rerun is claimed.

## Re-derivation

For a smooth connected projective S, localization for P^d×S and its hyperplane identifies the kernel of restriction to A^d×S with an image of G^{a−1,b−1}(P^{d−1}×S). Affine homotopy identifies the open group with G^{a,b}(S), and projection pullback supplies actual lifts of all these classes. Consequently the claimed surjection (K2.5) holds integrally, with both index shifts as written.

For a blow-up between smooth varieties, proper pushforward preserves both indices because source and target have equal dimension. The class b−π*π_*b restricts to zero on the common complement. This uses only open base change for proper pushforward and the explicitly local pullback construction. Localization then gives the exceptional contribution G^{a−1,b−1}(E). No projective-bundle or blow-up direct-sum formula is silently assumed.

For degree (1,2), P² contributes one k* and the six point blow-ups contribute six more; P^m contributes one further k* exactly when m≥1. Thus the displayed count 7+ε_m is correct. On a smooth proper curve H¹(K₂^M) is a quotient of the direct sum of its closed-point k* groups. Each such group is divisible over an algebraically closed field. Direct sums and quotients preserve divisibility.

For the higher statement, the base curve has divisible G^{a,a+1} in all a: it is k* for a=0, the preceding quotient for a=1, and zero above dimension one. The projective-space surjection preserves this property by induction on d. A product blow-up at {q}×S has exceptional divisor P¹×S, so the blow-up surjection preserves the property as well. Six successive point blow-ups construct each cubic-surface factor. Iteration proves the exact asserted all-degree diagonal divisibility for products of cubic surfaces, projective space, and the curve, in every characteristic.

The degree-two Milnor–Quillen identification is made only on the smooth variety. In its Gersten complex the field groups K₂, K₁, K₀ and all their residues coincide. The proof does not claim a comparison on the nonreduced thickening, or a higher-degree comparison.

The final sheaf-injection implication is exact: H²(J) is killed by p if J is, and the preceding connecting map from a p-divisible H¹ must vanish. This implication separately requires the relative-sheaf and product compatibility supplied by the companion relative Milnor lemma.

## Primary sources actually opened and read in this audit

1. Rost, M. (1996), *Chow groups with coefficients*, Documenta Mathematica 1, 319–393, full 76-page author-hosted PDF: https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf. Freshly read Proposition 4.1(3), printed p.351; Section 5, p.356 localization sequence and grading convention; Remark 5.4, p.357; Corollary 6.5 and its pullback/product discussion, p.360; Proposition 8.6 with proof, p.370; Section 12 construction and exact open-restriction identity preceding Theorem 12.1, p.382, and Proposition 12.2, p.383. These are the precise integral operations used by the proof.
2. Author corrections: https://www.math.uni-bielefeld.de/~rost/chowcoeff.html, opened in full. The unused double-deformation flatness assertion on p.377 and signs in (14.3)–(14.4) are not used in the localization generation proof.
3. The all-characteristic cubic-surface description was freshly read earlier in this same run for C.3bi in Huybrechts's author notes, Chapter 4, Lemma 2.1 and Proposition 2.4, pp.177–178. It is reused here, not claimed as a second fresh opening in this audit.
4. Kerz's integral smooth Gersten input is reused from the established exact source audit, rather than newly opened in this short check.

## Scope

No field restriction beyond the stated algebraically closed field is introduced. The argument proves divisibility, not unique divisibility. It provides no automatic lifting of Chow classes across a nonreduced scheme and no conclusion about the complete proposed local restriction counterexample without its remaining geometric and product checks.
