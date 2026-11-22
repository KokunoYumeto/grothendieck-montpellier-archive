# H11 full affineness: second targeted audit

GPT-6 Astra (OpenAI), /root/bce, 20 November 2026, 15:57 UTC.
This is a repeat audit by the same delegated AI agent, not independent provenance.

## Exact theorem proved

Let S be integral noetherian with dim(S) <= 1. Let X and Xprime be proper S-schemes and f:Xprime -> X a surjective S-morphism. There is a nonempty open V of S over which f* on fppf Picard functors is affine. No flatness, normality, or projectivity of the original families is required. They may be imposed after shrinking when needed. The theorem does not assert the arbitrary higher-dimensional-base variant in SGA6 XII Remark1.7.

## Source checks

1. Original SGA6 XII, Theorem1.1 and Corollary1.2, printed p596, PDF page599: exactly proper schemes over integral noetherian S and a surjective morphism; after shrinking, pullback is quasi-affine of finite presentation and each Picard functor is a separated group scheme locally of finite presentation. The original scan was downloaded and visually opened. PDF https://library.slmath.org/books/sga/sga/pdf/sga6.pdf ; local sources/SGA6_slmath.pdf. Printed pp597–598 confirm the field-case kernel-quotient proof and the all-base open question; they impose no hidden flatness on Theorem1.1.
2. SGA3 VI_B Proposition11.11, printed pp402–403, retyped PDF49: a finite-type quasi-affine group over a field is affine. https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp6B.pdf
3. Stacks06PH, Lemma80.11.7: free action of flat lfp group on algebraic space has an algebraic-space quotient and the map is an fppf torsor. All hypotheses hold after generic flatness of finite-presentation K.
4. Stacks0418, Lemma67.51.1: every separated locally quasi-finite map of algebraic spaces is representable by schemes. No finite-type hypothesis on the full source over S is added.
5. SGA3 VI_B Corollary1.4.2, printed pp325–326, retyped PDF5: a quasi-compact monomorphism of group schemes locally of finite type over an Artinian local base is a closed immersion. We apply only over the residue fields. Quasi-compactness is essential and proved, not inferred from injectivity.
6. SGA3 XVI Lemma4.2, printed pp521–522, retyped PDF19: over a locally noetherian base of dimension1, a separated quasi-finite morphism between locally finite-type schemes is affine if every map on an S-fibre is finite. There is no dimension restriction on the target. https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo16.pdf

## Proof gates rechecked

K=ker(u) is a group scheme of finite presentation since u is quasi-affine of finite presentation; it is quasi-affine as the base change by the identity section. Its generic fibre is affine. Affineness spreads out because K/S is finitely presented: choose an affine generic model, spread it and the inverse isomorphisms, then shrink. Generic flatness also applies since K has finite type. All shrinkings are finitely many and preserve a nonempty open.

Translation by K on P is free. Thus Q=P/K exists and p:P->Q is an affine fppf K-torsor of finite presentation. The induced v:Q->Pprime is a monomorphism on fppf sheaves because K is the whole kernel of u.

The morphism v is locally of finite presentation: this is fpqc local on the source and descends along p. It is quasi-compact: for any quasi-compact open W in Pprime, the quasi-compact u^{-1}(W) surjects onto v^{-1}(W). Monomorphisms are separated; lfp monomorphisms are locally quasi-finite. Hence v is separated quasi-finite of finite presentation. Stacks0418 makes it representable, and since Pprime is a scheme Q is a scheme.

Each v_s is a quasi-compact monomorphism of lft group schemes over a field; VI_B1.4.2 says it is a closed immersion and hence finite. All inputs to XVI4.2 are now checked. Therefore v is affine; p is affine; u=v*p is affine.

## Result

No gap found in the full one-dimensional statement. section additional_leads.tex contains the complete proof as Theorem H11.G. The preceding normal-case proof is redundant for status but useful as a separate route.
