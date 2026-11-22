# Independent review of F64: canonical weight extraction and flag convolution

Reviewer: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Date: 2026-11-21 UTC.

## Frozen target and verdict

Full report read: agent_weight_extraction_gate.md, SHA256
386d3a2786bfa299b8ed9231bc766463e4110bb56853709393cb0b9e5216e3c5.

Verdict: **PASS, no mathematical correction requested.** This is a manual whole-proof reconstruction and primary-context check, not a formal proof or a numerical experiment. No master artifact was edited.

Dependency actually read and reconstructed: the flag-correspondence, torsor, Chern-triangle and hypercohomology calculations in agent_nonproper_torus_kernel.md (F62), current SHA256
b70ed1e87088267222e206f1e1fec8147f288f816846462f5d495b902f87398a.
The present check does not assert a new independent audit of every archival citation in F62.

## Exact proof reconstruction

1. The operation G(A)=direct sum over r,w of gr^W_w pH^r(A)[-r] is a well-defined additive operation on the mixed category. Functoriality follows by applying perverse cohomology and the functorial weight filtration. Its definition supplies no triangulated exactness or monoidality. The report correctly claims only preservation of the Euler class and stalk Euler traces.

2. Open restriction is perverse t-exact and preserves both weight bounds, since j^*=j^!. Restricting the weight filtration gives the unique weight filtration of the restricted perverse sheaf. Thus j^*G=G j^* is valid. This use is restricted to the open immersion.

3. Let P=B[2] and Q=I[1]. These are perverse of weights 2 and 1. The shifted localization triangle is H[2] -> P -> Q[1] -> H[3]. Its perverse long exact sequence gives exactly
0 -> Q -> H[2] -> P -> 0,
with every other perverse cohomology group zero. The weights identify this exact sequence as the canonical weight filtration, not a chosen arbitrary splitting.

4. Consequently G(H)=B direct sum I[-1]. Expanding its convolution square gives precisely
B direct sum B[-1]^2 direct sum B(-1)[-2] direct sum I[-2].
Here B*B=B tensor RΓ(P1,E), while I is the unit. After open restriction, ordinary H^0 is E_O.

5. Independently, the actual open restriction of H*H is K from the line-bundle torsor. Its two ordinary cohomology sheaves are H^1K=E_O and H^2K=E_O(-1). On the smooth surface O, E_O[2] is perverse, so
pH^3(K)=E_O[2], pH^4(K)=E_O(-1)[2].
The indices 3 and 4, rather than 1 and 2, are essential and correct. The associated perverse weight pieces already have weights 2 and 4. Restoring the shifts produces E_O[-1] direct sum E_O(-1)[-2], whose ordinary H^0 is zero. This proves the claimed nonisomorphism without invoking a trace distinction.

6. For perverse splitting alone, P(H)=H, whereas its convolution square restricts to the nonsplit K and P(H*H) restricts to the split two-degree object. The actual Chern class is nonzero: on O=(P1)^2 minus the diagonal,
H^2(O,E(1)) is spanned by h_x modulo h_x+h_z, and c1(O(1,-1))=2h_x.
This proves the nonsplitting over the geometric base. Ordinary cohomology splitting fails by the same calculation. The dimension comparison 2 versus 4 follows directly from the Chern triangle and the two-dimensional total cohomology of O.

7. The intermediate extension j_!*E_O[2]=E_Y[2] is correct because the constant local system extends to smooth irreducible Y. The source/target distinction is retained: B is a valid different chosen kernel, not an extraction already shown to preserve the original relation.

8. The exact-functor no-go uses the actual K0 identity
[H]^2=(L-1)[H]+L[I], with L=[E(-1)[-2]].
An exact strong-convolution functor preserving I, Tate twists, shifts, and H -> B would send this to [B]^2=(L-1)[B]+L[I]. Since actual B*B=(L+1)B, this forces 2[B]=L[I]. Open restriction yields 2[E_O]=0, contradicted by generic Euler rank. Every functor hypothesis used by the argument is explicitly listed.

9. The positive B iteration is correct: all middle P1 factors are independent, and all parenthesizations identify with the same product correspondence. Hence B^{*r}=RΓ((P1)^{r-1},E) tensor B with the actual associativity maps. This is a known proper construction and does not make G or perverse splitting strong monoidal on the original open-kernel category.

## Primary contexts checked in this review

Local original BBD text was read in the following complete relevant contexts:

- Discussion preceding Proposition 4.2.5, printed pp108–109: smooth pullback shifted by relative dimension is perverse t-exact.
- Lemma 4.3.2 and proof, printed pp112–113: the middle extension of a lisse sheaf that extends over a smooth irreducible variety.
- Section 5.1.8, printed pp126–127: shift convention for weights and the smooth/lisse cohomology criterion.
- Section 5.1.14, printed p128 and continuation: the relevant weight-operation framework.
- Theorem 5.3.5 with Lemma 5.3.6 and proof, printed pp136–137: unique finite weight filtration and strict functoriality.

The report's use of these statements matches their exact scope. The kernel associativity and projective-cohomology inputs were reconstructed in the displayed example; the detailed Milne archival audit is inherited from the separately checked F62 record.

## Scope preserved

The conclusion concerns the specified canonical splitting procedures and unchanged convolution. It does not exclude Rees constructions, filtered enhancements, or operations retaining extension and differential data. It does not identify these standard flag kernels with designated IV/VIII canonical objects. Equality of all Euler traces remains compatible with the proved nonisomorphism. No new archival positivity or nonstandard-purity theorem is asserted.

## Final generated-fragment match

The complete finding_F64.tex was subsequently read directly, from its subsection heading through the final separate dictionary paragraph. Frozen SHA256:
c5e45c35a4428179c7075f899bfd753c68ded2e489ee82461a19808fc55713cd.

Verdict: **whole-fragment match PASS**. The TeX retains every report proof: the perverse localization exact sequence, unique weight filtration, both convolution restrictions and their cohomological indices, the perverse and ordinary splitting counterexamples, the exact K0 functor obstruction, and the coherent proper B iteration. All assumptions on the exact strong-convolution functor and all nonstandard/source scope boundaries remain explicit.

The final placement delta adds the separate Part III marker and names the dictionary paragraph “The weight-extraction test in Grothendieck's language.” It makes no mathematical change. The added Milne citation cluster is consistent with the previously checked F62 framework; no independent re-audit of every Milne page is claimed here.

This is a direct whole-text review, not merely a diff or a search-based check. The isolated syntax compile was performed by the author and is not counted as a new reviewer execution in this record.

