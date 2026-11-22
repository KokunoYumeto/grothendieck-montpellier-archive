# Raynaud LNM119: original cohomological-flatness criterion and B3 relevance

Status at15:00UTC: original printed pages14–15 and37–38 have now been fetched through explicitly advertised public publisher previews and visually read independently by `part_b_cycles`. LemmasII.1.1–II.1.2 and DefinitionII.1.3 supply the exact W-condition and its base-change compatibility; complete LemmaIII.1.1 and DefinitionIII.1.2 supply the cohomological-flatness criterion relevant to B3subject17. The parent independently read the original pages and complete deduction, verified the square-zero recovery of exactW and the post-delta=1 universal-base-change application, and approved integration. No subscription-content endpoint or preview limit was altered; the full book is not claimed read.

**Correction of an overstrong audit gate.** The task requires relevant original mathematical passages and the derivation that uses them; it does not require reading every page of the complete book. Earlier notes' wording that a whole-book or complete-mathematical-text recovery was necessary was too strong. A mere unrelated definition/retyped page175 would not have fulfilled the intended use. Original LemmaIII.1.1, used in the precise Picard/cohomological-flatness context below with its now-opened definitions, supplies the relevant original mathematics. The parent reviewed and approved the complete deduction; the relevant named-source requirement is now discharged. The missing full book is then an access limitation, not a remaining task gate.

## Opened original text

The public publisher URL, actually advertised by its chapter landing page, is https://page-one.springer.com/pdf/preview/10.1007/BFb0059509 . The parent saved `sources/root_raynaud_picard_preview.pdf` and `.txt`; the independent visual readings are `qa/part_b_raynaud_picard_37.png` and `_38.png`. Their ad-hoc two-page rendering took0.368257199seconds as reported by the executor; it is a source inspection, not a mathematical computation. The parent records its own fetch request and duration separately.

On p37, LemmaIII.1.1 assumes f:X→S quasicompact and quasiseparated, F quasicoherent satisfyingW(II.1.3), and its finite-presentation representing moduleQ. It proves equivalence between arbitrary base change for f_*F and local freeness ofQ. DefinitionIII.1.2 adds S-flatness ofF to call it cohomologically flat in dimension0; then Q is the dual of the finite locally free module f_*F. For F=O_X and f_*O_X of rank1, the natural O_S→f_*O_X is an isomorphism, and the source calls the equality universal.

PropositionIII.1.4 on p38 is also complete, but it invokes S-purity and II.2.5/II.2.11. This audit does not claim its full generality without those dependencies. LemmaIII.1.5 is incomplete in the preview and is not used. Neither item is needed for the proof below.

## Exact finite-module lemma replacing the unaccessed II.2.9 dependency

Let(A,m,k) be a commutative local ring andQ a finitely generated A-module. If the natural map

Hom_A(Q,A)⊗_A k → Hom_k(Q⊗_A k,k)

is surjective, thenQ is finite free.

Choose q_1,...,q_r whose reductions are a k-basis ofQ/mQ. They generateQ by Nakayama. Lift the dual basis to A-linear functionals φ_i:Q→A; surjectivity of the displayed tensor map supplies these lifts because residue-field coefficients can themselves be lifted toA. The matrixM=(φ_i(q_j)) reduces to the identity, hence has invertible determinant in the local ring. Replacing the functionals by M^{-1}(φ_i) gives an A-linear map φ:Q→A^r whose composition with the surjection ψ:A^r→Q, e_j↦q_j, is the identity. The mapψ is therefore both injective and surjective, henceQ≅A^r. If r=0, Nakayama givesQ=0. No Noetherian hypothesis or flatness hypothesis onQ is used.

Thus the finite-presentation version quoted by Raynaud on p37 has a complete independent proof here. We need not claim that the original page containing II.2.9 was opened.

## Exact condition W from original pp14–15

The fetched public preview is https://page-one.springer.com/pdf/preview/10.1007/BFb0059508 , an actual link parsed from the normal DOI-resolved publisher landing. The saved files are `sources/part_b_raynaud_chapter2_preview.pdf` and `.txt`; visual readings are `qa/part_b_raynaud_image_direct_14.png` and `_15.png`. The PDF has114,876bytes, two pages, SHA25656f45bc0588d2b6c39bab0e5ed1119082aa97753582fe7b9fdd9b5c7a3663776. The ordinary metadata landing took47.133687964seconds, the advertised unchanged preview link7.253124695seconds, and the whole program54.528921686seconds. The ad-hoc rendering/text inspection took0.338208832seconds as reported by the executor. Full records: `code/part_b_raynaud_chapter2_preview.py` and matching output.

For f:X→S quasicompact and quasiseparated, F quasicoherent, the source defines

W(S,F): M ↦ f_*(F⊗f^*M)

on quasicoherent O_S-modules. LemmaII.1.1 says that local representation on an affine cover by quasicoherent modules is equivalent to representation after every base change, and identifies the base-changed representing module with g^*Q. LemmaII.1.2 supplies the affine argument; DefinitionII.1.3 on p15 requires in addition thatQ be finitely presented. Thus a safe explicit universal form of W is:

For every g:T→S and quasicoherent O_T-moduleM,

(f_T)_*(F_T⊗f_T^*M) ≅ Hom_{O_T}(g^*Q,M),

naturally inM, with Q finitely presented and quasicoherent onS.

The affine base-change compatibility has no hidden flatness assumption on g. For S=SpecA, T=SpecB and a B-moduleM, the affine projection X_T→X identifies the underlying A-module of sections with those of F⊗_A M. Representation overA then gives Hom_A(Q,M)=Hom_B(B⊗_A Q,M). This identifies Q_T with B⊗Q. The source then glues over affine covers using uniqueness of representing objects. Both the statement and its proof are visible in pp14–15. The continuation of RemarkII.1.4 and the later representability theoremII.1.5 are outside this preview and are not claimed read.

My preliminary draft used only the sections functor on S-schemes as a shorthand. The exact source hypothesis is the module-functor statement above; this corrected version is used in the final deduction.

## Complete base-change criterion under exact W

Let f:X→S be quasicompact and quasiseparated, letF be quasicoherent, and assume exact W as just stated with its finite-presentation moduleQ. Then the following are equivalent:

1. For every g:T→S, the canonical morphism g^*(f_*F)→(f_T)_*F_T is an isomorphism.
2. Q is finite locally free.

Set M=O_T in the defining representation. It gives (f_T)_*F_T≅Hom_{O_T}(g^*Q,O_T), and in particular f_*F≅Q^∨. Under these identifications the base-change morphism is the canonical dual-base-change map g^*Q^∨→(g^*Q)^∨. IfQ is locally free of finite rank, that map is an isomorphism, proving2⇒1.

Conversely, fix s∈S, localize at s, and apply1 toT=Specκ(s). Finite presentation ensures localization of Hom. The resulting dual-base-change map is surjective, so the preceding local algebra lemma makesQ_s free. A finitely presented quasicoherent module that is free at each stalk is locally free in a neighbourhood of every point: lift a finite basis at the stalk, use a finite presentation to kill its finitely many relations after shrinking, and shrink again so the resulting map is surjective. Thus1⇒2.

The lemma establishes exactly III.1.1, including the local algebra step that the original abbreviates by citing II.2.9. WhenF is also S-flat, DefinitionIII.1.2 calls these conditions cohomological flatness in dimension0. No Noetherian condition onS is used in this criterion.

The finite-presentation qualification is material: it is what permits passage from free stalks to locally free neighbourhoods and from Hom sheaves to their localizations. It is not silently omitted or supplied by the source's unrelated PropositionIII.1.4.

## Precise use for B3 subject17

The existing theorem `thm:B3-picard` concerns a proper flat regular relative curve C/S over a DVR with perfect residue field, with f_*O_C=O_S. In the already opened original Picard article, Raynaud1970, Theorem8.2.1 pp66–67, condition(iv) is **cohomological flatness and d'=1**. Under the stated regularity/perfectness assumptions, that condition is equivalent to δ=1 and to representability/separatedness of Pic^0, exactly as the manuscript proves.

Consequently when those equivalent conditions hold, the source's global-sections representing moduleQ is locally free by the original thesis criterion. SinceQ^∨≅f_*O_C≅O_S, necessarilyQ≅O_S. The same criterion now gives, for every base change T→S, a canonical equality

(f_T)_*O_(C_T) ≅ O_T.

This strengthens the B3#17 conclusion by making its coherent base-change content explicit. It also distinguishes the original fixed-base assumption f_*O_C=O_S from its universal version; they are not silently identified without cohomological flatness. The global-sections representability input in this proper setting is separately recorded in the already opened Picard article §1.4 pp28–29 (f proper of finite presentation;F of finite presentation and S-flat), which cites EGAIII7.7.6 and the thesisII.1.5. The criterion itself retains the explicit W hypothesis. For this proper relative-curve application it is satisfied: §1.4 gives a finite-presentation Q whose linear scheme V(Q) represents global sections universally. To recover exact W, on each affine T=SpecB and every B-moduleM evaluate this sections representation on the square-zero algebra B⊕M and take the kernel of reduction toB. The left kernel is Γ(C_T,O_(C_T)⊗f_T^*M), because the projection from the square-zero base change is affine; the right kernel is Hom_B(Q_T,M). Naturality identifies them. This establishes the required module-functor representation and its base-change compatibility. The existence theorem for the proper case remains a named known input from the opened original article §1.4, not a claimed new proof of all EGAIII7.7.6.

This is a mathematically relevant use of the named original thesis within the precise subject17 result, not an unrelated definition added to satisfy a checklist. No claim that pp37–38 alone prove the complete relative Picard representability theorem is made; that theorem remains derived from the separately opened original article, with its exact conditions.


## Integration completed

The theorem `thm:B3-raynaud-flatness` and its complete proof are integrated in `sections/part_b.tex`; `thm:B3-picard` now includes the justified universal-H0 conclusion. The bibliography marks the selected original passages opened, without claiming a whole-book reading. The old mathematical-text-unopened paragraph is replaced. The owned ledger adds B.3.17.flatness and records the source/application checks. No new finite mathematical check is required or claimed.
