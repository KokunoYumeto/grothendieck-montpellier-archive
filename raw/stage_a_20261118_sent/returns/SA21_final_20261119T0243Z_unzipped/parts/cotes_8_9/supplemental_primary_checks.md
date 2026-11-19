# Narrow checks requested by root

Completed on 19 November 2026 by GPT-6 Astra Pro, inherited effort, `/root/cotes_156_8_9`. Retrieval scripts, metadata and locator output are retained. The externally retrieved full PDFs, their extracted text and rendered page images are research inputs and should be excluded from the final ZIP; the scripts reproduce them. The PDF skill was used to inspect the mathematical notation visually.

## 1. SGA4 II: exact gluing criterion

**Canonical key:** `SGA4II`. J.-L. Verdier, *Topologies et faisceaux*, Exposé II of SGA4, Tome 1, LNM 269 (1972).

**Opened authoritative editorial copy:** <https://www.normalesup.org/~forgogozo/SGA4/02/02.pdf>. Header version `71766d9`, dated `2024-07-30 10:46:55 +0800`. This is an editor's retypesetting, not a first-printing facsimile. The newer host returned503; the older editor directory and its actual PDF links returned200.

Corollary2.4 is on PDF page4, zero-based page3, beside original marginal page8. For a category with a pretopology, a presheaf is a sheaf exactly when each covering family's usual section/pairwise-overlap diagram is an equalizer. The separated version requires injectivity of the first map. The displayed product and fiber-product subscripts were checked visually. This confirms the narrow formal comparison used for VIII's gluing discussion. It does not establish the custom atelier restriction hypotheses.

Local verification: `primary/sga4_II.txt` lines176–185; `primary/passage_locations.json`; rendered page4 inspected.

## 2. SGA4 IV: sober reconstruction and specialization

**Canonical key:** `SGA4IV`. A. Grothendieck and J.-L. Verdier, *Topos*, Exposé IV, same volume and editorial version.

**Opened copy:** <https://www.normalesup.org/~forgogozo/SGA4/04/04.pdf>. Sections4.2.1–4.2.2 occur on PDF pages20–21, zero-based19–20, with original marginal pages336–338. The usable results are the universal sobrification, its isomorphic lattice of opens, and the corresponding sheaf-topos reconstruction up to sobrification. The specialization convention is

\[
x\le y\iff\overline{\{x\}}\subseteq\overline{\{y\}}\iff x\in\overline{\{y\}}.
\]

Both closure bars are visible in the rendered formula. In modern terminology this is a preorder on an arbitrary space, and a partial order for a T0 space.

**Concrete error excluded from our use.** The editorial PDF itself contains the assertion that every space whose points are closed is sober. Therefore the same sentence in the web transcription cannot be blamed uniquely on that website. This check does not determine its first-printing origin. The assertion is false: an infinite cofinite space is T1 and irreducible, but has no generic point, since every singleton is closed. This counterexample is our elementary check, not a claim from the cited source. The legitimate sobrification construction is unaffected by that erroneous example sentence.

Local verification: `primary/sga4_IV.txt` lines960–1000; rendered pages20–21 inspected. No broad theorem is inferred from the informal phrase that practical spaces are usually sober.

## 3. Esquisse: comparison of Isom spaces is in section5

**Opened original requested PDF:** <https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf>.

The displayed comparison

\[
\operatorname{Isom}_{T}(X,Y)\longrightarrow\operatorname{Isom}_{T'}(X,Y)
\]

and the distinction between a bijection of components and a homotopy equivalence occur in **§5, printed page29**, continuing on printed page30. The PDF page is25 in one-based counting, or24 in zero-based counting. Section5 starts on PDFpage20/printedpage24. Section6 begins only on PDFpage29/printedpage33. Its later discussion of higher isotopy categories is separate.

The context proposes an axiomatic comparison theorem for two moderate theories and says that its axioms remain tentative; the author has not proved the comparison from them. It must therefore remain a programme statement, not be promoted into an established result. This corrects root item `SA21-88` (source entry110) where the displayed Isom comparison had been assigned to §6.

Local verification: `primary/EsquisseFr.txt` lines1022–1073, section boundaries833 and1218; rendered PDFpage25 inspected. Exact locations are programmatically recorded in `primary/passage_locations.json`.

## 4. Supplemental source/counterexample check

Root claim `C-SA21-2-017`, refinement `R-SA21-side-contraction`, was independently checked against the Pro source and the finite tripod model. The complete hypothesis check is in `proof_audits.md` §M. The connected regularly immersed contracted arm contains the original A endpoint, so its image becomes an interior cut point and Fic c fails. The U/X ink ambiguity is retained. Root owns the finite graph computation.
