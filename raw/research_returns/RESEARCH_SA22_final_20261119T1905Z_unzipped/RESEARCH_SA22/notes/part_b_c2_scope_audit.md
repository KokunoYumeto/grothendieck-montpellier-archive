# Independent C.2(b) task-to-answer scope audit

Auditor: GPT-6 Astra (OpenAI), `part_b_cycles`. Date:19 November2026. Requested by the parent during the checkpoint05 build freeze. This is an independent reading and proof audit, not a new movement claim or a new finite computation. No active C TeX or bibliography file was edited.

## Evidence actually read

- Prompt `upload/PROMPT(20261119-110314).md`, lines200–204, especially202: determine which finite and discrete groups carry a system satisfying the axioms and whether the two-torsion extension is forced.
- Original manuscript scan017, archive foliation16, in `sources/cote68.pdf`; the full image `qa/cote68_scan017.png` and rotated bottom `qa/cote68_scan017_bottom_rotated.png` were both visually read in this audit.
- Unchanged supplied transcription `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_66+68_002-032_transcription.tex`, lines536–571. The original image, not merely this transcription, controls the reading.
- Current `sections/part_c.tex`: the typed axiom paragraph, `C-literal-class`, `C-extension`, and the C4 counterexample's additional completeness assertions.

## What the original actually supplies

The uncancelled setup writes a group G-tilde, a map rho:G-tilde→G labelled **hom.**, and i:{}_2G≃ker(rho). It then assigns a family A(g-tilde) contained in the finite subsets of G and defines the associated cone of nonnegative indicator combinations. The displayed conditions are inclusion-chain, reflection/translation symmetry, convolution closure in the product-index cone, torsion equivariance, and pairwise translation alignment. Two separate clauses bear the label(d). The last line is the unfinished bracket `[i.e. union A_g` without a completed assertion.

I find **no completed cardinality-fullness condition, no maximality/faithfulness condition, and no requirement that every index fibre contain a nonempty finite subset**. These conditions cannot be supplied from the incomplete bracket. The top half of the page discusses cyclic interval examples; it does not turn those examples' cardinalities into an additional completed universal axiom in the bottom setup.

The rho arrow is not an unambiguous epimorphism symbol, and the word written is hom. The classification is nevertheless unchanged if surjectivity is required, because its constructed rho is a projection onto G. The extension-independence proof can likewise be restricted to projections H×G→G, with arbitrary H, so it does not depend on allowing a nonsurjective map.

The source uses an undefined B-family in the convolution clause as transcribed. C explicitly declares the type-correct A-family reading. The existence constructions also satisfy a two-family reading by choosing B=A. No extra nonempty/full condition is recoverable from that notational ambiguity.

## Exact classifications under the stated readings

| Reading | Classification | Reason |
|---|---|---|
| The four core chain/symmetry/convolution/alignment axioms, without prescribing a kernel | Every finite or arbitrary discrete group G | The trivial indicator system exists for any homomorphism. A surjective, nonzero version is given below. |
| Those axioms plus i:T≃ker(rho), with T={t in G:t^2=e} using multiplication inherited from G, and the written torsion equivariance | Exactly the groups whose involutions commute pairwise, equivalently T is a subgroup | Necessity is the well-typing of a group isomorphism; C's T×G construction proves sufficiency. |
| The preceding reading with rho additionally required surjective | The same class | The constructed rho(t,g)=g is already surjective. |
| The abelian setting with the usual two-torsion subgroup | Every finite and every arbitrary discrete abelian group | T is automatically a subgroup and C's proof applies, without a finiteness/countability assumption. |

For the first row, a uniform construction with a nonzero cone is G-tilde=G, rho=id, A_e={{e}}, and A_g empty for g≠e. Every nonzero atom product is delta_e*delta_e=delta_e in the required identity fibre; all other products are zero, symmetry holds, and alignment is vacuous except for equal singletons. Thus the core axioms themselves impose no commutativity-of-involutions restriction. The restriction in the second row must remain described as part of the explicit kernel typing.

The term **literal interpretation** in C's theorem is an explicitly stated mathematical convention, not an independently established paleographic definition of {}_2G for every nonabelian group. The usual inherited two-torsion group is unambiguous for abelian G. For a general nonabelian G the set of all involutions need not be closed under multiplication; the source does not define a different group law on that set. Therefore the theorem correctly begins by declaring its convention, and its concluding prose correctly says that failure of closure makes the intended group isomorphism ill-typed, not that the four core axioms have yielded a new obstruction. Abbreviated report wording should retain that convention. This is a source-typing qualification, not a missing proof of the theorem as stated.

An alternative use of the symbol for, for example, the two-torsion of the centre would be a different defined problem; the image does not say that. No classification under an invented alternative is silently asserted.

## Independent proof check of C-literal-class

Let T be a subgroup of G consisting of elements of order dividing2. For s,t in T, (st)^2=e if and only if st=ts, so T is elementary abelian. It is not necessary that T be central in G.

Set G-tilde=T×G, rho(t,g)=g, i(t)=(t,e). The kernel is exactly T×{e}, giving the declared isomorphism. For g=e set A_(t,e)={{t}}, and for g≠e use an empty family. In a nonempty fibre the symmetry centre is rho(t,e)=e, and {t}^{-1}={t}. Two nonzero atoms convolve as delta_t*delta_s=delta_(ts), whose index is (ts,e). Multiplying the index by i(u) changes the singleton to {ut}, exactly its left translation by u. Two singleton families align by translation ts^{-1}. Zero cones contribute zero products and impose no alignment obstruction. All required hypotheses are satisfied. This proof uses no finite enumeration and works for every cardinality of the discrete group.

There is also no fragility about the phrase **nonempty family**. If it means merely a family with at least one member, replace each off-kernel empty family by {emptyset}, and, if desired, put {emptyset,{t}} in each kernel fibre. Every family is then nonempty; the cones and all nonzero calculations are unchanged, and the empty set is comparable with every set. A stronger requirement that *every family have a nonempty member* is different. That stronger requirement is not written and is not covered by the general infinite-group classification. It must not be slipped into or out of the answer through the ambiguous word nonempty.

## Independent proof check of C-extension

The four core axioms do not determine the kernel: choose any projection H×G→G and all families {emptyset}. This already preserves surjectivity, with arbitrary H. If a nonzero cone is desired in this kernel-free question, give every index over e the singleton family {{e}} and the remaining indices the zero family; convolution products of nonzero atoms stay over e. Hence the logical independence does not rely on a zero system alone.

After imposing the kernel isomorphism, C's two examples over G=C2 have index groups C4 and C2×C2. The listed singleton fibres occur precisely over e; the other fibres contain G. The identities delta_s*delta_t=delta_(s+t), G*delta_t=G, and G*G=2G verify the cone conditions. Translation by the nontrivial torsion element exchanges the two singleton fibres and fixes the G-only fibres, giving equivariance. Families align, both possible positive cardinalities occur, and both maps rho are surjective. The index groups have exponents4 and2, so they are not isomorphic. Thus even these stronger finite examples do not determine a unique extension. The existing C finite certificate covers these displayed systems; no new finite check was run in this audit.

## Conclusion and integration scope

No missing completed axiom or proof gap was found. The current theorem's explicit interpretation and the extension-independence argument correctly discharge C.2(b) at the level of the axioms actually completed on the sheet. An unrestricted claim that arbitrary-group involutions already form a group would be false, but the current theorem does not make that claim. The useful reporting distinction is: **core axioms: all groups; exact inherited two-torsion kernel: precisely the well-typed class; abelian case: all groups in that category**. Cardinality-complete/nonzero-every-fibre classification is not an uncompleted obligation unless separately imposed; the source does not impose it. No new INCOMPLETE mathematical gate is warranted by this audit.
