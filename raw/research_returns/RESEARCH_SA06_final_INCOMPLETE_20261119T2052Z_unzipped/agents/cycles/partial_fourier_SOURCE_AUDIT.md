# C.4ab primary-source and search-scope audit

Only the specified statements/proofs were read; no full-paper independent proof claim is intended.

1. Mukai1981, full published23-page PDF, section1 formula1.4 and Theorem2.2 at printed156: integral derived Poincare functor. Exact source URL and SHA below. Browser refs turn426689033view0 and turn118378504view0.
2. Yoshioka2001, full38-page authorv2: section2.1 equations2.3,2.6-2.8, printed authorp5 (PDFindex4), including the actual page image turn118378504view3. The initial draft's p4 locator was corrected after real_weil's independent source read. Browser refs turn426689033view1 and turn556819259view0. The proof uses general Riemann-Roch in precisely its relative Fourier form; no WIT or positive-rank hypothesis is introduced.
3. Bastianelli-Pirola-Stoppino2010, full36-page authorv2: Proposition4.1 identifies the target as F3; Proposition4.5 and its complete proof give the finite degree3 morphism; section5 equation5.1 identifies the residual fibre product. Browser refs turn426689033view2 and turn118378504view2. The prior Albanese calculation alone was not used as a Fourier obstruction.
4. Kahn2026, Divided powers on abelian varieties, arxiv2602.11135v2: introduction through Proposition2.6 and AppendixB.6-B.7. Theorem1.7 and Corollary1.8 concern etale Chow projectors. Question1.11 and the ordinary comparison prevent a false integral-cycle inference. Browser refs turn324075281view0 and turn514342808view1/2. This is a source-scope observation, not an imported ordinary projector theorem.
5. Voisin2024, published PAMQ PDF: Definition1.9 and the Mumford-Tate-general discussion, printed2473, freshly read in turn118378504view1 and turn556819259view1. Its exact published numbering is retained.

## Other searches, not theorem inputs

- Bruin-Kulkarni2025, full primary On (2,2)-decomposable genus4 Jacobians, section7: square-gluing Jacobian loci are proper surfaces in the three-dimensional genus2 moduli space for the specified markings. This did not supply a generic type-(1,2) construction.
- Honigs-Graham McDonald-Peter McDonald2608.23779: primary arxiv abstract read; PDF and HTML retrievals returned DisabledError in this pass. No theorem from its inaccessible body is asserted.
- Gounelas-Huybrechts2510.20474v2: primary introduction/TheoremsA-B read. Universal Brauer-Severi varieties are classifying spaces; their universality is not the existence of a universal zero-cycle over the abelian surface.
- Voisin2025, Algebraic Geometry12(6)888-901, primary introduction and Lemma1.5 read. Representable CH0 examples have Albanese factoring through a curve; the non-universal-zero-cycle example does not provide the needed Brauer-Severi obstruction for this type-(1,2) surface.

## Actual source retrieval

```json
{
  "utc": "2026-11-19T12:14:20.547593+00:00",
  "runtime_seconds": 9.344331139996939,
  "sources": [
    {
      "name": "mukai1981_partial_fourier",
      "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf",
      "final_url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf",
      "status": "downloaded",
      "bytes": 1903728,
      "sha256": "062dd13ffac9249fd248f0cca061ff5e41918e8087f688ae30cb7a4f1c86be1c",
      "path": "/workspace/scratch/0b428c83d30f/research/agents/cycles/sources/mukai1981_partial_fourier.pdf",
      "pdftotext_returncode": 0,
      "pdftotext_stderr": "",
      "runtime_seconds": 7.500624289998086
    },
    {
      "name": "yoshioka2001_partial_fourier",
      "url": "https://arxiv.org/pdf/math/0009001",
      "final_url": "https://arxiv.org/pdf/math/0009001",
      "status": "downloaded",
      "bytes": 579594,
      "sha256": "ee095858a35a037e2b851a2e8bdc3f73764ab81d36759b47c56c73ac6bc19aa9",
      "path": "/workspace/scratch/0b428c83d30f/research/agents/cycles/sources/yoshioka2001_partial_fourier.pdf",
      "pdftotext_returncode": 0,
      "pdftotext_stderr": "",
      "runtime_seconds": 9.342241352998826
    },
    {
      "name": "bps2010_partial_fourier",
      "url": "https://arxiv.org/pdf/0912.3377",
      "final_url": "https://arxiv.org/pdf/0912.3377",
      "status": "downloaded",
      "bytes": 448602,
      "sha256": "31f88fcda294145dd28ce2a57ed6a12568764e2f32f90754f64b5a8ebe1203c9",
      "path": "/workspace/scratch/0b428c83d30f/research/agents/cycles/sources/bps2010_partial_fourier.pdf",
      "pdftotext_returncode": 0,
      "pdftotext_stderr": "",
      "runtime_seconds": 9.319665068003815
    },
    {
      "name": "kahn2026_divided_powers",
      "url": "https://arxiv.org/pdf/2602.11135",
      "final_url": "https://arxiv.org/pdf/2602.11135",
      "status": "downloaded",
      "bytes": 683397,
      "sha256": "7a3c5abca22e76dbfe4d7ff8b72410b7e40c10243ad025bba3d94693f36ae883",
      "path": "/workspace/scratch/0b428c83d30f/research/agents/cycles/sources/kahn2026_divided_powers.pdf",
      "pdftotext_returncode": 0,
      "pdftotext_stderr": "",
      "runtime_seconds": 9.341172199005086
    }
  ]
}
```
