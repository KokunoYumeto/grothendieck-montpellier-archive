# Second-source visual check of the five emendation candidates

Agent: `/root/archive_binomial`; model: GPT-6 Astra Pro, inherited; reasoning effort: not exposed by the runtime. Date: 2026-11-21 UTC. The three parent-supplied image files were independently viewed during the current turn; the completed reading was recorded at 00:53:14 UTC.

## Provenance and scope

The supplied ZIP contained text transcriptions, not these manuscript images. The parent subsequently downloaded the official public [cote 54 PDF](https://grothendieck.umontpellier.fr/54.pdf) and [cote 47 PDF](https://grothendieck.umontpellier.fr/47.pdf), then rendered the images in `research/archive_originals/`. I directly viewed only:

- `cote54_pdf05.png`;
- `cote54_diagram_detail.png`;
- `cote47_chern_detail.png`.

The parent checked the page correspondence against the supplied transcriptions: official PDF pages 5 and 7 of cote 54 correspond to supplied scan005 and scan007; PDF page 9 of cote 47 corresponds to supplied scan009. The official/manuscript archive labels are respectively 4, 6 and 8. Do not impose the different PDF-page/printed-label offset as a rule for the names in the supplied transcription files.

## Independent visual results

| Existing candidate ID | Diplomatic reading visible in the public image | Mathematical emendation | Confidence and classification |
|---|---|---|---|
| ABA-TN01 | The subscript in the B-cohomology term is visibly A. | Replace by B in the intended Hodge-cohomology expression. | High visual confidence. The supplied reading faithfully represents the autograph; this is a mathematical emendation, not a confirmed transcription error. |
| ABA-TN02 | The upper-right vertex after the Verschiebung arrow is visibly V. | The codomain in the standard Frobenius/Verschiebung diagram is A. | High visual confidence. Again an autograph slip/emendation candidate rather than a transcription error. |
| ABA-TN03 | The quadratic denominator is visibly `2 chi`. | With numerator `chi(chi-1)` and the stated generating series, it must be `2 chi^2`. | High visual and algebraic confidence, conditional on retaining the generating formula. The supplied transcription is faithful here. |
| ABA-TN04 | The cubic denominator is visibly `3! chi^2`. | With the displayed numerator it must be `3! chi^3`. | High visual and algebraic confidence, under the same condition. The supplied transcription is faithful here. |
| ABA-TN05 | The superscript in the general denominator is small and faint; it is compatible with `n-1`. | The displayed generating series forces the denominator `n! chi^n`. | Medium visual confidence in the exact original exponent; high confidence in the conditional algebraic correction. Preserve a qualified diplomatic reading. |

The zero restricted-p-operation interpretation is not changed by these readings. The unsigned final Chern integrality expression remains excluded from forced corrections: it differs from the Chern class by an integral factor/sign, so its weaker integrality claim can still be true.

## Consequence for the deliverable

Preserve the supplied diplomatic text and identify the five rows as mathematical emendation candidates, with the public-image evidence in a separate provenance field. Earlier check records truthfully said that no manuscript pixels had yet been inspected; they should remain historical records. This new visual check supersedes any present-tense implication that the five entries are established transcription mistakes. The parent, who owns the current root table and paper, is applying that classification change. This agent did not edit `DP_MULT.tex` or overwrite the parent's current transcription table.
