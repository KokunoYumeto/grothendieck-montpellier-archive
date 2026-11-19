# Original SGA 7 I: the Barsotti–Tate/Néron extension passage

## Primary witness and exact pagination

The SLMath/MSRI scan is available at `https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf`. It is the photographic original, not the AI-edited text edition. Direct download succeeded; the web extractor rejected its size. The file has528 PDF pages and37,362,787 bytes, SHA256 `17286b0f0bec451068e0a5fa2c39e93de28e7c1ecee6739487cfac11c03c8dab`. It is held outside the deliverable at `/tmp/SA04_a_external/SGA7I_SLMath.pdf`.

The relevant pages are:

| PDF page | Printed continuous page | Internal IX page | Passage |
|---|---|---|---|
| 387 | 382 | 64 | Theorem5.8, Corollary5.9 |
| 388 | 383 | 65 | Remark5.9.1 and start of proof of5.9 |
| 389 | 384 | 66 | End of proof; Lemma5.9.2 and representability footnote |
| 390 | 385 | 67 | Proof of lemma; Corollary5.10 and first part of proof |
| 391 | 386 | 68 | End of proof; Remark5.11 |

OCR was used for navigation and reading. The page images387,388,390,391 were also visually inspected to verify the page numbers, quantifiers and characteristic restriction. The retrieval and OCR programs are `programs/a_fetch_external.py` and `programs/a_ocr_external.py`; their saved metadata outputs are `outputs/a_fetch_SGA7I_SLMath.txt` and `outputs/a_ocr_SGA7I_SLMath_385_392.txt`. The publisher page independently verifies LNM288 and1972 publication; no date is assigned to the archive manuscripts.

## Exact hypotheses and implications

**Theorem 5.8 (M. Raynaud), printed page 382.** Let $A_K$ be an abelian scheme with semistable reduction over the function field of a henselian trait $S$. Let $\ell$ be a prime. When $\ell=p$, the statement explicitly assumes $\operatorname{char}K=0$ so that Tate's theorem [33, Theorem 4] is available. With $X_\eta=T_\ell(A_K)$ and its fixed part $X_\eta^f$, every morphism from the generic fibre of a Barsotti–Tate pro-$\ell$-group over $S$ into $X_\eta$ factors through $X_\eta^f$.

**Corollary 5.9, same page.** In the associated ind-group formulation, every homomorphism $F_\eta\to A_\eta$, with $F$ a Barsotti–Tate ind-$\ell$-group over $S$, extends uniquely to $F\to A$, where $A$ is the Néron model. The text emphasizes that the source need not be smooth. The characteristic restriction from 5.8 remains in force.

**Remark5.9.1, printedp383.** Raynaud proves5.9 without semistability, for every Néronian group scheme (A/S), and without assuming (S) henselian. Its generic fibre need not be abelian. The reduction to the special case of5.8 invokes an unpublished property in the construction of Néron models. This is an exact published assertion of the broad target-group extension, but the unpublished input is not reproduced in this passage. The remark does not delete the characteristic restriction needed for Tate.

**Proof and Lemma5.9.2, printedpp383–385.** The proof reduces to a BT group with connected special fibre using the connected/étale sequence. The quotient by the fixed part extends as an ind-étale group; Tate full faithfulness extends the generic map to that quotient, and connected-to-étale vanishing makes it zero. Lemma5.9.2 treats a group extension with smooth quotient, a map from its kernel into a Néronian group, and a compatible generic map. It assumes representability of the pushout extension. A sufficient finite-locally-free-local splitting/quasi-projectivity condition is stated; a footnote says unpublished Raynaud results make representability automatic. The proof then uses smoothness and the Néronian property. Neither unpublished assertion has been independently proved in this audit.

**Corollary 5.10, printed page 385.** An abelian variety over the function field of a trait has good reduction exactly when its Barsotti–Tate pro-$\ell$-group extends. For $\ell=p$, it again explicitly assumes $\operatorname{char}K=0$. The text identifies this with the conjecture in [8, 4.9], i.e. the trait case of the Grothendieck 1966 extension question. This does not settle the full higher-dimensional base question merely by being stated for traits.

**Remark 5.11, printed page 386.** The author expressly says that 5.8, 5.9, 5.10 and 5.13 would hold without the restriction on $\operatorname{char}K$ once Tate's theorem was proved without it. De Jong's 1998 generic full-faithfulness theorem, used with its 1999 erratum, supplies precisely that later input. The published dependency is direct evidence of this connection.

## Implication for the root register

The c100 Néronian-target assertion in C-SA04-672 now has an exact primary publication counterpart: Corollary5.9 plus Remark5.9.1, with the retained characteristic qualification and the explicit later-removal dependency in5.11. C-SA04-673's connected/étale and Tate steps have the corresponding printed proof onpp383–385. The broader result may be described as published by Grothendieck with Raynaud attribution, completed in the characteristic issue by de Jong; the general Néron-model property and automatic representability are cited unpublished inputs, not independently certified here. The manuscript's own status on its pages is unchanged by this literature identification.

The AI-edited SGA page supplied a discovery lead only. The findings above rest on the original scan. This upgrades only the specifically inspected passages; it is not a claim to have collated the whole SGA volume or every paragraph cited elsewhere.

The OCR files are `/tmp/SA04_a_external/SGA7I_SLMath_ocr/p387.txt` through `p391.txt`; corresponding page images use the same names with `.png`.
