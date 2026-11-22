# Independent review of cubic excision and the matched norm system

Reviewer: /root/lean_chain, GPT-6 Astra Pro; effort not exposed.

**Verdict: PASS for the complete proofs and their stated scope.** This review concerns the exact files and hashes below. It does not assert a computed nonzero norm class, a source-to-independent-jet theorem, or a new arithmetic vanishing result.

| File | SHA-256 |
|---|---|
| unitary_audit/reducible_comparison/cubic_excision_norm.tex | 01439511120c0efb43f67db781dd0480ba5bfbe886653253b1c907eb122a333f |
| unitary_audit/reducible_comparison/cubic_shuffle_comparison.tex | 71a0e713fa6b9dd282d043a27cfc75b35398afc26472dfab7213478b8b9174ad |

Both files were read in full, including the entire new lifting argument, the exact fixed-system comparison, and the final scope paragraphs. The earlier cubic_excision_review_stage1.json is retained as the record of the intermediate review, when norm matching was still pending.

## 1. Relative obstruction and excision

The mapping-fibre description uses the actual unramified inflation maps. Starting with the two triangles with common first term RΓ(U,j!M), it gives the local gluing triangle for U = Spec Z[1/p] and V = Spec Z[1/pD]. Removing the finite-field degree-two cocycles leaves exactly the specified local primitives modulo unramified local degree-one classes. It does not discard the local correction at a prime dividing D.

At p, forgetting the primitive is valid because the permitted local space is the full degree-one group and the local degree-two group vanishes: its Cartier dual has character ω^(1−e), which is nontrivial because e is even and p is odd. The infinite-place terms have no positive-degree p-cohomology. Thus CE.1 identifies the actual quotient of pairs, with its natural map, rather than only comparing dimensions.

Over F = Q(μ_p), the Kummer sequence and the Brauer local invariant sequence give CE.2. There is one prime above p, it is principal, and one local invariant with total sum zero is zero. The coefficient identification by ζ contributes the extra cyclotomic character, producing precisely δ = ω^(1−e). There is no quotient by primes over D.

The pullback to K = EF is handled by functoriality and ideal-class norm and extension. The proof does not call U_K → U an étale cover at primes dividing D. On the E-positive, δ-component, the prime classes and Brauer terms at p vanish and norm/extension have compositions 2 and 1+c. The displayed projector followed by one-half norm is therefore the correct inverse on this component.

## 2. Why the matched-system repair is sufficient

The terminology “binomial proper system” alone is not used as a converse assertion that every specified last column is produced by a literal Sharifi norm representative. The revised proof uses the additional zero-absolute-Bockstein hypothesis. In the application, that hypothesis is proved either by the local-global Brauer injection or by the fact that the actual class lies in the Picard subgroup and becomes zero over the generic field.

After the first lift of the specified f₂ to the quotient by I³, the successive obstruction restricts to zero over G_L, where the full regular module has trivial action. The absolute cyclic norm-residue exact sequence writes this obstruction as χ cup γ_n. Subtracting γ_n x^(n−1) kills it. The sign in CE.10 agrees with the declared differential. Since every subsequent correction has degree at least two, the specified truncation modulo I² is preserved. Lifting a zero-cochain removes any remaining discrepancy of representatives.

The resulting full regular-module cocycle is constructed on the absolute Galois group. Its coefficient at the identity on G_L gives the Kummer class y by Shapiro. Equivariance makes the coefficient at σ^j the character of σ^j y, exactly the map in Sharifi's Lemma 3.1 with its inversion pairing. This checks the sign and the actual Kummer-dual embedding used in (4.2), rather than just an abstract isomorphism of the two modules.

The lift-σ normalization in Lemma 4.1 is legitimate: the excess over the constant augmentation is in xR, hence is removed by a regular-module coboundary. It gives the matrix X+v(σ)E34, with the same specified truncated cohomology class and Bockstein. Dividing the norm representative by a base-field scalar makes its norm equal to the chosen B₀ exactly. The associated norm-element cocycle is supported on x^(p−1) and does not affect the truncation.

On G_Ω, the truncated cocycle is zero. Thus the regular cocycle has values in I². Sharifi's Lemma 3.3 places D^(1) in the annihilator of that ideal for the same pairing, so D^(1)y has a p-th root in Ω. This supplies the required proper norm condition.

Crucially, the higher coefficients of the full cocycle need not descend to the group with restricted ramification. The argument neither makes D^(2)y a p-th power in Ω nor forces the finite-ramification transgression to vanish.

## 3. Exact class and scope

For the matched norm representative, Sharifi's Proposition 4.2 gives the class of that specified system as the exact transgression of D^(2)y. Equation (5.2) in the complete proof of Theorem 5.4 gives the exact negative norm-ideal class. The prime-to-p scaling introduced in that proof can be canceled in the coefficient group. The exceptional boundary is absent because the repeated length is two and p>3.

The already checked cochain comparison makes the raw ordinary obstruction three times this binomial-system class. The projected formula CE.11 is consequently the exact equality with −3 times the norm-ideal class for a matched y. For an unmatched proper representative, CE.7 correctly retains the lower-product quotient.

The actual quadratic family is literally unramified over K at the primes dividing D, after the local conjugation in the carried mixed quadratic construction. Hence its polynomial binomial coordinates descend to G_(K,p). The corresponding acceptable cubic local lift is also unramified there. This is the needed compatibility between the raw p-only class and the relative class; a statement only about vanishing inertia cohomology would not have sufficed.

The result provides an exact comparison and a sufficient criterion after evaluation. No matched y, ideal, or nonzero value is calculated. The separate source-to-jet and general finite-coefficient-field issues remain explicit.

## 4. Primary-source reading record

The foundational theorems are imported. The following complete relevant passages, including the proofs specified here, were read; this is not a claim to have re-proved or checked the entire primary books and papers.

- Sharifi, author version dated 26 July 2006: Lemma 3.1 and its full proof, printed pp. 13–14; the complete Lemma 3.3 and proof, pp. 14–15; Section 4 conventions and complete Lemma 4.1 and Proposition 4.2, pp. 17–22; Theorem 5.4 and its entire proof, pp. 26–27, especially exact equation (5.2). PDF SHA-256: 85438ce984f10afb941cbd8277e7a5becd832eea15a99f52655fc8913b471234.
- Lam–Liu–Sharifi–Wake–Wang: Definition 3.3.2, complete Lemma 3.3.3 and Theorem 3.3.4 proofs, author pp. 24–27; the binomial discussion and Section 4.3, pp. 30–32; Definition 6.1.2 and the following absolute-Galois paragraph, p. 48, and the complete proof of Proposition 6.1.5, p. 49. PDF SHA-256: e92f4dc6460653a8b9bcb4249655731b07bae5cde465ab6ea4887cd75c2317c3.
- Milne, Arithmetic Duality Theorems, second edition: I.2.14 and proof, pp. 36–37; II.0.1 relevant exact sequences and proof, pp. 140–141; II.0.8–0.10 relevant full complex-level construction and proof, pp. 145–148; II.1.1 and proof, p. 149; II.2.1 and Remark II.2.2, pp. 163–165; complete II.2.3–2.4 and complex-level proof, pp. 166–168; complete II.2.9 comparison proof, pp. 170–172. PDF SHA-256: 2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31. The relevant official addendum correction, revised 26 October 2025, p. 1, for printed p. 168 line 5 was also checked. No whole-addendum review is claimed.

No new Lean kernel build or new numerical computation is claimed by this review. The existing eleven-check shuffle certificate was previously read and replayed; the new norm-matching lemma is a mathematical argument checked against the above primary passages.
