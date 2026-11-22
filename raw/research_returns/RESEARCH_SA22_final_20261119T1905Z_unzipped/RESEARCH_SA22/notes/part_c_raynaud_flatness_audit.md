# Independent audit: Raynaud's exact W condition and the Picard application

Reviewer: GPT-6 Astra Pro, subagent `part_c_algebra`, 19 November 2026. This audit was completed independently of the author of the new deduction and reported to the parent and `part_b_cycles` before 15:20 UTC. It concerns `thm:B3-raynaud-flatness` and the newly added universal degree-zero conclusion in `thm:B3-picard`. **Outcome: passed; no mathematical correction requested.**

## Actual original passages read

The original mathematical text was read in the saved publisher previews, not inferred from a later citation:

- Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, LNM119 (1970), printed pp.14–15: Lemmas II.1.1–II.1.2 and Definition II.1.3. I actually viewed `qa/part_b_raynaud_image_direct_14.png` and `_15.png` and checked the transcription in `sources/part_b_raynaud_chapter2_preview.txt`.
- The same original, printed p.37: Lemma III.1.1 and Definition III.1.2. I actually viewed `qa/part_b_raynaud_picard_37.png` and checked `sources/root_raynaud_picard_preview.txt`. The p.38 text was read, but no visual reading of p.38 is claimed in this independent audit. Proposition III.1.4 and the incomplete III.1.5 are not inputs to the deduction audited here.
- Raynaud, *Spécialisation du foncteur de Picard*, Publ. Math. IHÉS38 (1970), §1.4, printed pp.28–29, in `sources/raynaud_picard1970.txt`, together with the introduction and the existing theorem application. The new use of §1.4 is the square-zero recovery of exact W.
- The full new proof and source accounting in `notes/part_b_raynaud_thesis_derivation.md`, and the current proofs in `sections/part_b.tex`.

The advertised publisher previews are `https://page-one.springer.com/pdf/preview/10.1007/BFb0059508` and `https://page-one.springer.com/pdf/preview/10.1007/BFb0059509`; the original Picard article is `https://www.numdam.org/item/PMIHES_1970__38__27_0/`. This audit used the already saved original files and images; it made no new network requests and did not rerun a rendering program. Acquisition URLs, hashes and measured retrieval times remain in the B/root provenance records. No whole-book reading or independent viewing of the unprovided II.2.9 text is claimed.

## 1. Exact representation and quantifiers

The property used in the theorem represents the direct-image functor for **all quasi-coherent coefficient modules**, naturally, and after **every base change**. For a base change `g:T→S` and quasi-coherent `M` on `T`, the relevant expression is

`(f_T)_*(F_T ⊗ f_T^*M) ≅ Hom_{O_T}(g^*Q,M)`.

It is not merely a statement about the single coefficient module `O_T`, and it does not assume that `g` or `M` is flat. Original II.1.1–II.1.2 provide precisely this universality and the identification of the representing module after base change. On affine schemes the reason is elementary: for `A→B` and a `B`-module `M`, the affine projection from `X_B` to `X` identifies the relevant pushed-forward tensor product with the coefficient module viewed over `A`, and

`Hom_A(Q,M) = Hom_B(B⊗_A Q,M)`.

The construction glues by the natural uniqueness of a representing module. The manuscript preserves the **finite-presentation** hypothesis supplied by II.1.3; this is needed in the subsequent sheaf-localization and neighborhood argument.

## 2. The local algebra replacing the unseen II.2.9 dependency

Let `(A,m)` be local and let `Q` be a finite `A`-module. Suppose the canonical map

`Hom_A(Q,A)⊗_A k → Hom_k(Q/mQ,k)`

is surjective, where `k=A/m`. Choose elements `q_1,…,q_r` whose residue classes form a basis of `Q/mQ`. Nakayama gives a surjection `ψ:A^r→Q`. Surjectivity of the dual base-change map permits lifts of a residue dual basis to `A`-linear functionals `φ_i:Q→A`: each finite linear combination in the tensor product can be lifted by choosing lifts of its residue coefficients. The evaluation matrix `(φ_i(q_j))` is the identity modulo `m`, hence is invertible over `A`. Replacing the functionals by the inverse-matrix combination gives `φψ=id_{A^r}`. Thus `ψ` is injective as well as surjective, and `Q` is free. The case `r=0` is exactly Nakayama and causes no exception.

This proof does not require `A` noetherian or `Q` flat. It proves the particular algebraic step actually needed from II.2.9, without pretending that the original II.2.9 page was opened. The converse, that a finite free module has the stated dual base-change isomorphism, follows immediately by evaluating on a basis.

For a finitely presented sheaf `Q`, stalkwise freeness gives local freeness: choose a map from a finite free module which is an isomorphism at the chosen stalk, kill its finitely generated cokernel after shrinking, and then kill its finitely generated kernel after a further shrinking. Finite presentation supplies the kernel finiteness at this step. Sheaf-Hom localization is valid for the same reason. Hence the local matrix argument proves the global finite-locally-free criterion used in III.1.1.

## 3. Canonical degree-zero base change

Under exact W, the canonical degree-zero base-change map is identified with

`g^*(Q^∨) → (g^*Q)^∨`.

Thus arbitrary degree-zero base change implies the residue-field maps used in the preceding argument, and finite local freeness conversely makes every displayed map an isomorphism. The proof concerns the canonical comparison, not the existence of some abstract isomorphism between modules. The manuscript therefore derives exactly the original Lemma III.1.1 statement, with the definition of cohomological flatness in dimension zero from III.1.2 when the stated flatness hypothesis on `F` holds.

## 4. Proper Picard application and square-zero algebras

The original Picard article §1.4 represents the appropriate global-section functor by a linear scheme `V(Q)`, with a finitely presented representing module, under the properness, finite-presentation and flatness hypotheses stated there. To recover exact W for an arbitrary `B`-module `M`, apply this representing functor to the square-zero `B`-algebra `B⊕M` and take the kernel of its reduction to `B`. The affine projection and the split module decomposition identify the geometric kernel with the sections of `O_{C_B}⊗_B M`; the representing-side kernel is `Hom_B(Q_B,M)`. This construction is natural in `M`, in restriction to affine opens and in base change, so it gives the required sheaf version of W. No flatness of `M` is used.

For the regular proper relative curve over a DVR in `thm:B3-picard`, the necessary finite-presentation assumptions hold; the DVR is noetherian and the proper morphism is of finite presentation. The article's representing theorem remains an explicitly cited original input. It is not claimed to have been reproved from the preview alone.

The order of the remaining argument is essential and is correct in the manuscript: the `δ=1` condition and the cited Picard criterion first give cohomological flatness; the W criterion then makes `Q` locally free. Only after that may `Q^∨≅O` imply `Q≅O` and the universal identity `(f_T)_*O_{C_T}≅O_T`. Bare fixed-base equality `f_*O_C=O_S` would not eliminate torsion in `Q` and is not used as if it did. The resulting identity is the canonical unit, as follows from the original representation and base-change maps.

## Scope and status

The relevant original thesis passages are genuinely used in a complete deduction. The named-source requirement is not reduced to a bibliographic citation, nor is it expanded into an invented requirement to read the whole book. The proof of the needed local step is complete even though the original II.2.9 text is not opened. The new universal H0 application is consistent with, and follows after, the pre-existing cohomological-flatness criterion; it does not strengthen the Picard theorem without its hypotheses.

This audit adds no new theorem and runs no finite mathematical program. Existing result IDs are `B.3.17.flatness` and `B.3.17`; the exact named-source ID is `B.required_source.RaynaudThesis1970`.
