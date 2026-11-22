# Independent C.2 classification and replacement audit, 19 November 2026

Auditor: GPT-6 Astra (OpenAI), `part_b_cycles`. This extends the earlier `part_b_c2_scope_audit.md` by checking the surrounding sheets 015–022 and all hypothesis transitions in the current replacement and classification proofs. It does not change C's TeX, rerun a mathematical certificate, or claim new source-retrieval progress.

## Verdict

**No proof gap or omitted completed 017 axiom was found in the current statements.** The exact classification is valid under its declared inherited-multiplication interpretation of the two-torsion symbol. The all-groups conclusion holds for the four core axioms alone; with the written kernel isomorphism the class is exactly the groups whose elements of order dividing two form a subgroup. The current theorem does not classify systems with additional cardinality completeness, translation saturation, or a nonempty set in every index fibre. Those stronger requirements must not be attached to its conclusion in a summary.

The two source-interpretation choices are explicit, not hidden: the undefined second family in the convolution clause is identified with the first, and `{}_2G` is interpreted as `{t:t^2=e}` with multiplication inherited from G. The manuscript does not independently define an alternative group law on this set for arbitrary nonabelian G. Thus the classification is a complete answer to the expressly typed version of the completed 017 axioms, rather than an unconditional paleographic claim about an undefined alternative notation.

## Evidence actually inspected

- Prompt `upload/PROMPT(20261119-110314).md`, lines 200–204: C.2(a) expressly names axioms a)–d) of 017; C.2(b) asks which finite and discrete groups carry a system satisfying the axioms; C.2(c) asks the symmetry question in general.
- Actual `sources/cote68.pdf`, scans 015, 016, 017, 019, 020, 021, 022. The existing full/rotated 017 images were reused; six other sheets were rendered in this audit and visually inspected. Scan 018 is the unrelated printed face identified in the supplied transcription. The lower 017 setup, the bracketed completeness condition on 021, and the separate saturation passage on 022 were read from the images, not inferred from an editorial lead.
- Supplied `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_66+68_002-032_transcription.tex`, especially the passages at lines 375–571, 574–716, and 717–790. The image controls ambiguous readings.
- Current `sections/part_c.tex`, lines 366–735: `C-rearrangement`, the typed axioms, `C-chain-true`, `C-K-counter`, `C-K-replacement`, `C-literal-class`, `C-extension`, and `C-symmetry` with the finite packed-pair corollary.

## Which assumptions occur where

| Original passage | Actual role | Current use |
|---|---|---|
| 015–016 | Examples and convolution scratch work; no completed additional universal classification axiom | No missing general hypothesis was recovered here. |
| 017, lower setup | Group homomorphism, two-torsion/kernel identification, inclusion chains, reflection symmetry, product-index cone closure, torsion equivariance, and pairwise translation alignment | These are precisely the typed axioms preceding `C-chain-true`. |
| 017, final bracket | An unfinished `[i.e. union A_g` | It supplies no completed fullness, surjectivity, faithfulness, maximality, or nonzero-every-fibre assertion. |
| 019–020 | Finite-support rearrangement and majorization; pretassé equality and symmetry question | Used without assuming a countable enumeration of G. |
| 021, corollary (c) | Explicit bracket: an indicator of each positive finite cardinality at most `card G` belongs to S | Retained in `C-K-replacement`, where it is needed for the three-factor-to-all-partial-sums direction. It is not silently imposed on 017 existence. |
| 022, separate paragraph | “Quitte à saturer S” and subsequent supposition of translation stability, nonempty `S_0`, and a new construction from superlevels | A later additional construction. The current 017 classification does not use or claim this saturation. |

In particular, the upper cyclic examples on 017 do not turn their cardinalities into a universal axiom in the lower setup. The arrow is labelled `hom.`; even if surjectivity is requested, the classification construction already has it.

## Classification and nonemptiness

The complete scope table is:

| Hypotheses | Proven class, for finite or arbitrary infinite discrete G |
|---|---|
| Four core chain/reflection/convolution/alignment axioms | Every group |
| Core plus the written equivariance and a group isomorphism from the inherited two-torsion set to `ker rho` | Exactly those G for which that set is a subgroup, equivalently all involutions commute pairwise |
| Previous row plus surjective rho and at least one nonzero cone | Same class |
| Previous row plus every indexed family is nonempty as a family | Same class: off-kernel families may be `{emptyset}` |
| Abelian groups with their usual two-torsion subgroup | Every finite and every infinite discrete abelian group |

Necessity in the second row is the typing of the required group isomorphism. For `s^2=t^2=e`, the condition `(st)^2=e` is equivalent to `st=ts`, so closure is exactly the displayed commutation condition. Sufficiency is checked without a cardinality assumption: use `Gtilde=T×G`, projection rho, and the singleton family `{{t}}` over `(t,e)`, with the zero family over `(t,g)` for `g != e`. The only nonzero atom products are `delta_t*delta_s=delta_ts`. Reflection has centre e; multiplying the index by `i(u)` translates the atom by u; two singleton families align by `ts^{-1}`. T need not be central in G. Replacing off-kernel empty families by `{emptyset}` retains every condition and makes every family nonempty.

“A nonempty family” and “a family containing a nonempty set” are distinct. The general infinite-group theorem does not impose the latter in every fibre. In the finite case even that extra condition causes no additional existence obstruction: put the single nonempty set G in every fibre of `T×G`; `1_G*1_G=|G|1_G`, and reflection, translation and alignment preserve G. This observation is not used to imply an unproved analogous classification for infinite groups.

For the stripped core an explicit surjective, nonzero system is `Gtilde=G`, `rho=id`, the family `{{e}}` over e and zero families elsewhere. Thus “all groups” cannot be transferred to the kernel-prescribed problem. For arbitrary core kernels, use projections `H×G→G`; all families `{emptyset}` work, or put `{{e}}` over each index above e for a nonzero system.

## Why the later saturation would be a genuinely stronger problem

There is a short exact obstruction to conflating these scopes. Suppose the 017 core axioms are retained and their union S is additionally translation stable and contains one singleton indicator. Then S contains every `delta_g`. If `delta_g` lies in `C_a`, reflection gives `rho(a)=g^2`: equivalently, in any positive indicator expansion of a singleton, every nonzero atom must be that singleton. For `delta_g in C_a` and `delta_h in C_b`, product-index closure gives `delta_gh in C_ab`, and reflection then implies

`(gh)^2 = rho(ab) = rho(a)rho(b) = g^2h^2`.

Cancelling g on the left and h on the right gives `hg=gh`. Hence such a saturated system with a singleton can occur only on an abelian group. This proves that importing the 022 saturation and the 021 cardinality-one condition can change the existence problem. No such import occurs in `C-literal-class`; the example is a scope boundary, not an additional task obligation or a classification of all stronger systems.

## Replacement theorem and finite/infinite transitions

`C-chain-true` uses only the four core axioms. Finite positive combinations of nested indicators have nested superlevel sets from the same chain. Reflection of `g in C_b` converts the alignment translate `s*g` to `delta_(s rho(b))*check(g)`, in the correct order even for a nonabelian group. Bilinearity proves `C_a*C_b` is contained in `C_ab`.

The C4 counterexample has no vacuity loophole: every family contains nonempty sets, every positive cardinality is represented, rho is surjective with exactly the written two-torsion kernel, and the table verifies the cone conditions. Its three-factor inequality is false, `4 <= 3`; its two-factor partial-sum inequality also fails. The hand proof was reread, but its existing finite program was not rerun.

In `C-K-replacement`, all-pairs tassé implies the n-factor claim by induction using convolution stability. The latter implies K by the first partial sum. Conversely, for each finite k the assumed indicator of size k supplies the third test factor; invert the k locations of the largest values of `f'*g'` and pad by zero-valued locations when necessary. Evaluation at e is exactly the k-th partial sum. K and rearrangement then bound it by the corresponding partial sum of `f*g`. The argument requires no ordering of all elements of G, countable exhaustion, convergence assertion, or finite size of G. Every function involved has finite support; for a finite group k is restricted to its cardinality. The theorem's cardinality assumption is therefore exact and is not discharged by the sparse literal classification construction.

The general symmetry criterion also has no finite-only step. For any noncommuting a,b the two displayed two-point functions give convolution maxima 5 and 4. The collision checks are group identities, not a finite enumeration; conversely abelian convolution commutes. The separate S3 tassé certificate is an example, not the proof of the all-group pretassé criterion.

## Extension independence and conclusion

The two kernel-prescribed systems over C2 have index groups C4 and C2×C2. Both have surjective rho, the specified torsion equivariance, every positive cardinality, and nonempty sets in every family. The displayed singleton/full-group products verify all cone requirements. Their exponents differ, so the extensions cannot be isomorphic. This proves nonuniqueness even under those extra finite conditions; it does not claim that imposing the kernel has ceased to be part of the setup.

No TeX correction or new mathematical INCOMPLETE gate is justified by this audit. Report wording must retain the inherited-two-torsion convention and the distinction between completed 017 axioms, 021 completeness, and 022 saturation. The stronger classifications are neither proved nor silently claimed.

Source-preparation utility: `code/part_b_c2_full_scope_render.py`, six pages, zero network requests, **1.6813246509991586 seconds** recorded in its matching JSON. No mathematical finite check was run. New audit events are saved separately in `checks/part_b_c2_full_scope_events.tsv`.
