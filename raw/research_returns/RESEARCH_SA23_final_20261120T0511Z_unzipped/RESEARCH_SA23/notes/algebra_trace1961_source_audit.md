# Grothendieck's 1961 trace note: original-source audit

Checked by algebra_letters at 2026-11-20 03:16:57 UTC. Parent requested this distinct route after the 1972 thematic report's bibliography [8 bis] was identified.

## Source and access

A. Grothendieck, *The trace of certain operators*, **Studia Mathematica 20** (1961), no. 2, pp. 141–143, DOI **10.4064/sm-20-2-141-143**.

- Publisher metadata opened: https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/20/2/94856/en/publishing-house/journals-and-series/studia-mathematica/all/20
- Independent Mathdoc metadata opened: https://geodesic.mathdoc.fr/articles/10.4064/sm-20-2-141-143/
- Original journal-image mirror actually downloaded: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-Trace-ope.pdf
- The mirror was discovered in a real PDF link annotation on physical p. 6 of https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG-bibliotex.pdf ; its URL was not guessed.
- Local source: `sources/algebra_history_trace1961_original.pdf`, 668167 bytes; SHA256 `199cfef5128787d4a725452f955addd436c71ac99bed4494d8a937688213d1b1`.
- Two physical PDF spreads: physical 1 has printed p. 141 on the right and a blank left page; physical 2 has printed pp. 142–143. All three printed pages were read visually from the rendered original, not from a modern transcription.
- The source contains no embedded text. The empty extracted text was not treated as a negative search.
- Direct web-reader access to the ICM copy and the publisher's download endpoint each returned 403. Those restricted routes were stopped. The separately published Circle mirror was obtained by ordinary unauthenticated download; the web reader's error on that mirror did not prevent the successful local HTTP 200 retrieval.

## Dated documentary evidence

The opening paragraph of printed p. 141 presents the paper as Grothendieck's answer to a letter from **R. Sikorski**, whose problem asks for equality of three cyclic trace expressions. It does not print the letter's date or identify an older enclosure.

At the bottom of printed p. 143 the journal prints:

> Reçu par la Rédaction le 20. 6. 1960

The bibliography contains the metric tensor-product résumé (São Paulo 8, 1956, pp. 1–79). Immediately below it, the author adds a reference to P. Cartier's February 1961 Bourbaki exposé 211, explaining that the reference was added during correction of proofs. No separate composition date or date of Sikorski's initiating letter is printed.

The receipt line dates submission of this paper. The paper gives direct evidence of the author's use of the full Hilbert-space trace theorem in a contribution received in 1960, subject to the ordinary distinction between the received manuscript and the subsequently corrected published text. The explicitly acknowledged proof-stage addition concerns the Cartier reference. **Neither the receipt nor this publication dates the cote 1 sheets.**

## Exact mathematical passage and comparison with cote 1

Printed p. 142, **Proposition (2), proof, remark (a)**, asserts that the eigenvalues of a nuclear operator on a Hilbert space form a summable sequence whose sum is the operator's trace. It uses this assertion as an input: no proof of that Hilbert assertion is supplied there.

The surrounding argument concerns an operator factoring through a Hilbert space. Remark (b) transfers the nonzero eigenvalues between opposite compositions; remark (c) combines this fact with the Hilbert trace assertion to obtain the special-operator property. Corollaries then establish cyclic trace identities for operators satisfying Hilbert-factorization/integrality conditions. Printed p. 143 applies them to Sikorski's three-operator question.

This is an explicit statement/use of the full Hilbert theorem, not merely the narrower two-thirds-nuclear Banach theorem. The note has **no Fredholm determinant, genus-zero assertion, three-sector Phragmén–Lindelöf argument, or identification of an earlier manuscript**. Its factorization/cyclic-trace argument therefore does not identify the specific genus-zero proof in cote 1.

## What this settles, and what it leaves open

The note prevents treating a broad statement that Grothendieck's main functional-analysis period ended in 1953 or 1955 as a date bound on every later functional-analysis text. It establishes a further dated publication in this subject and a concrete source of correspondence with Sikorski.

It does **not** identify the date, physical origin, or priority of the cote 1 argument. The narrowly justified follow-up is a public original letter, or an item-level archival description of the Sikorski–Grothendieck exchange, explicitly identifying an older proof/enclosure. Mere topic overlap would not suffice.

## Reproducibility and records

- Retrieval/annotation extraction: `code/algebra_history_retro36.py`; outputs `logs/algebra_history_retro36.json` and `.txt`.
- Source retrieval and all-page rendering: `code/algebra_history_retro38.py`; outputs `logs/algebra_history_retro38.json` and `.txt`. Runtime 18.244298 seconds.
- Original renders: `sources/algebra_history_trace1961_original_p001.png` and `_p002.png`; both displayed successfully and read.
- Web search/open records: `notes/algebra_history_web71.json`–`web77.json`.
- Bibliography key: **algGrothendieckTrace1961** in `notes/algebra_retrospective_references.bib`.
