# Original-image audit: cote 18, scans 42–49 and 51

Checker: GPT-6 Astra, agent period_generation. Date: 19 November 2026.

Source actually inspected: `work/source_records/Montpellier_cote18_original.pdf`.
The PDF has 62 pages. In this audit, “PDF page” is one-based. PDF page 51
is the source designated scan 051 in the frozen transcription and bears
the manuscript/website number 50. Analogously PDF page 45 bears 44.

No frozen transcription has been edited.

## MGEN-1. The place-recovery phrase on scan 051

I inspected `tmp/manuscript_qa/cote18_pdf51.png`, then rendered a four-times
scale clip directly from PDF page 51, rectangle `(145,575,580,735)` in PDF
points. The resulting file is
`tmp/manuscript_qa/cote18_pdf51_recovery_detail.png`.

The source visibly retains the qualifications that the chosen changes
depend on the motive and that the recovery assertion is probable. For the
word between `une place v` and `bien déterminée`, my visual judgment
favours an affirmative reading `est`, with compressed `soit` also
plausible, over `pas`. The available pen strokes do not give me sufficient
confidence to eliminate the frozen `est|pas` alternative. This is a new
image-based assessment, not a resolved transcription or a proof of the
mathematical assertion. The published analysis should retain the
uncertainty and should not quote the sentence as a settled assertion of
injectivity.

## MGEN-2. The field K on scan 045

I inspected the full rendered originals for every PDF page 42–49. These
are stored as `tmp/manuscript_qa/cote18_pdfNN_generation.png`. I additionally
rendered PDF page 45 at four-times scale on rectangle `(105,65,575,335)`;
the result is `tmp/manuscript_qa/cote18_pdf45_K_detail.png`.

The local sequence contains:

- 42: heading concerning variation of a discrete lattice with a complex
  place and a transcendence criterion; no field generators.
- 43: Betti/de Rham/finite comparison problem list; no definition of the
  field in the later bound.
- 44: reused English typescript about direct images, restrictions and
  singularities. Its K-symbols occur in module/sheaf maps and are not
  explicitly connected to the subsequent field bound.
- 45: the elliptic product, the group displayed up to isogeny with
  dimension 7, its Borel expression of dimension 5, and the bound on K.
  There is no intervening definition of K on this page. The second
  numerical glyph looks more like 5 than 4 to this checker, but the
  frozen alternative `5|4` is retained.
- 46: reused Haar-measure typescript; no definition connecting to 45.
- 47: integral Betti lattices, comparison torsors and product local
  fields; no identification of the K from 45.
- 48: upside-down reused valuation/ramification typescript; no connecting
  definition.
- 49: Galois modifications, the strengthened Tate expectation and the
  generic-point lemma; no identification of K from 45.

The earlier scan 011 **does** explicitly define a comparison field
`K=k(alpha,beta)=k(beta,gamma)=k(gamma,alpha)`. Therefore the phrase
“the supplied pages do not define K” is too broad. The supported finding
is narrower: the local pages 42–49 do not define the K used in 45 or
explicitly identify it with the earlier comparison field. No inference
that the two occurrences must differ is made. Identifying them and
deriving the asserted dimension bound require an explicit mathematical
map, which has not been supplied by this image inspection.

## Related independent mathematical checks

The same checker independently verified A.4.18–19 from the current TeX
and Tang's original preprint `arXiv:1510.01357v3`: Definition 2.3.1 and
Theorem 2.3.3 on p. 7, Corollary 5.2.3 and its proof on p. 23. The
coefficient field in the conclusion is the rational endomorphism algebra,
and the nontrivial-idempotent contradiction for an elliptic curve is
valid. The stated weighted density matches the source. The nonzero
imaginary entry of the Betti projector, algebraic scalar extraction,
semilinear Frobenius matrix calculation, and the point count and
irreducibility at 5 were checked directly. No substantive correction was
found. One referent in the density proof was clarified by the parent.
