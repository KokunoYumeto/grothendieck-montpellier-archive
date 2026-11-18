# Cote 139 · Readings and doubts

## Notation table

| Feature | Where checked | What is visible | LaTeX treatment |
| --- | --- | --- | --- |
| Capital and small-cap inscription | 2, right of the neck, single line | A tall M followed by smaller O R L O N on a gently falling baseline. No accent, stop or leading initial. | `\textsc{Morlon}` at the observed angle |
| Small raised device | 2, coat, close to the lower rim | A short upstroke, an almost closed loop, a central short stroke and a projection to the right. There is no secure alphabetic or numeric value. | Drawn in TikZ inside `\figure`, at the observed position |
| Circular capital letters | 3, rim from the lower left clockwise | `ACADEMIE DES SCIENCES DE L'INSTITUT DE FRANCE`. The I is a short-width upright. Both Es of ACADEMIE have bare tops. | Individually rotated capital-letter nodes in a single `\figure` |
| Apostrophe | 3, rim, between L and I | A separate raised, high tick | `\textquoteright` in its own rotated node |
| Central capitals | 3, centre lines 1, 2 and 4 | `MEDAILLE`, `EMILE PICARD`, `GROTHENDIECK`. There is no acute accent over any E. | Upright capital letters, with the word spacing and line positions recovered from the medal |
| Larger initial and smaller capitals | 3, centre line 4 | The A of ALEXANDRE reaches the height of the surname. LEXANDRE is visibly shorter. This parallels the two heights in MORLON on scan 2. | `A\scalebox{0.78}{LEXANDRE}` in the same type family |
| Separator rule and radial device | 3, centre line 3 and foot of rim | Straight divider below the title. A separate rayed ornament lies between FRANCE and ACADEMIE. | Native TikZ paths, each in its original position |
| Numerals | 3, centre line 5 | `1977`, with a short oblique lead-in on the 1 and a top bar followed by a diagonal on each 7 | `1977` in text mode |
| Pinpoint beside K | 3, end of centre line 4 | A small point a little above the foot of the letter, in a patch of surface marks | `\unsure{{}\|.}`. The empty candidate means no punctuation. |

## Doubtful readings

| Scan | Approximate line | Preferred reading | Other reading | Confidence | What the mark and its context show |
| --- | --- | --- | --- | --- | --- |
| 3 | Centre 4, immediately after the K of GROTHENDIECK | No punctuation, represented by the empty first candidate in `\unsure{{}\|.}` | Full stop `.` | Medium for no punctuation, low for a stop | A faint, detached pinpoint lies slightly above the foot of K on the edge of a rough patch. The brighter point below and to its left belongs to the leg of K. The surrounding short inscriptions have open endings. |

## Slips kept as written

None. The bare capital Es in ACADEMIE, MEDAILLE and EMILE are visible features of the lettering.

## Abbreviations

None. The apostrophe in L'INSTITUT marks the elision of the article.

## Legibility and inventory

Both scans are photographs of a medal. The six letters of MORLON and the large inscriptions on scan 3 are legible. The smaller capitals of ALEXANDRE are more worn, especially along the lower strokes. The point at the end of the surname is the least certain textual detail. The little loop on the coat, the rayed ornament and the interruption at the right rim are reproduced as shapes. The vector drawings approximate the relief and the most visible surface marks.

The inventory uses `text` for these photographs of the subject of the cote and `unknown` for the hand. The signature is itself in relief. The photographs do not identify a manuscript hand.

## Witness check

Hua batch-01 covers its pages 1–2. Its page 2 corresponds to scan 3. Scan 2 had no text marked for consultation.

| Scan | Line | Frozen reading | Witness reading | What the photograph shows on rereading | Result |
| --- | --- | --- | --- | --- | --- |
| 3 | Centre 4, after K | `\unsure{{}\|.}` (no punctuation, or a stop) | Hua batch-01 reads `GROTHENDIECK` without a following stop (page 2, source line 50). | The leg of K ends in one bright point. A fainter detached point sits just to its right and slightly higher, inside a band of uneven surface. The crop still allows both readings. | Unchanged. The witness reading was already the first candidate. |
