# Primary-reading ledger: Hartshorne and Katz–Messing

These are records of reading published texts, not new readings of Montpellier manuscript images. The original manuscript images were not supplied. The exact citation keys are `Hartshorne1966`, `KatzMessing1974`, `Gabriel1962`, `Murfet2006` and `LuntsSchnuerer2016` in `references.bib`.

## Hartshorne, *Residues and Duality* (1966)

The complete original scan was downloaded from the Göttingen GDZ repository at https://gdz.sub.uni-goettingen.de/download/pdf/PPN496067613/PPN496067613.pdf. It is retained as `research/Hartshorne1966.pdf`. The direct text extraction contains little beyond metadata, so it was not used as if it contained the mathematical text. Published PDF pages130–147 were rendered and OCR-read; in this part of the book they correspond to printed pages119–136. The actual rendering/OCR program and outputs are saved.

The following exact passages were read with their arguments:

| Printed location | Result used | Cote-16 relevance |
|---|---|---|
| II§7, pp120–122; Proposition7.3, Corollaries7.4–7.5 | Noetherian module injectives, their decomposition and layers | c16/39, preliminary page−7, with explicit Matlis attribution |
| Proposition7.6, pp123–124 | Adjunction from the stalk to the point-supported sheaf; injectivity among all module sheaves | Exact argument counterpart to c16/37 |
| Proposition7.8 and Corollary7.9, p126 | Locally noetherian module-sheaf category and sums of injectives | Hypothesis support for global decomposition |
| Proposition7.11, p128 | Indecomposable injectives in the all-module category can involve specialization pairs | Prevents identifying every all-module injective with a quasi-coherent one |
| Proposition7.14, p130 | Affine associated-sheaf injectivity | Local-to-global comparison |
| Lemma7.16, p131 | Locality criterion for injectivity | Input to7.17 |
| Proposition7.17, pp131–132 | Equivalent injectivity, direct-sum, stalk, coherent-Ext and local conditions for quasi-coherent sheaves on a locally noetherian prescheme | Exact mathematical content of source Proposition3.4, with changed numbering |
| Theorem7.18, p133 | Injective hull of a quasi-coherent sheaf is quasi-coherent | Preservation of quasi-coherence and modern QCoh-injective comparison |
| Proposition7.20 and following discussion, pp134–136 | Finite injective-dimension context | Boundaries of the reused homological assertions |

The preliminary numbers3.1–3.4 and negative typescript page numbers do not, by themselves, identify the precise draft or its typist. This ledger establishes mathematical lineage, not an archival authorship decision.

The remark on printed p135 about uncertainty over whether injectivity in the quasi-coherent category implies injectivity in all modules must be treated historically. The previously proved quasi-coherent injective hull permits the usual splitting argument. The modern statement and proof were read explicitly in Lunts and Schnürer (2016), Theorem2.1, p912, for locally noetherian schemes; Murfet (2006), §8.2, Lemma67 and Proposition68, gives another checked pointer and refers back to Hartshorne. Gabriel (1962), IV§2, Theorem2, and VI§§1–2, especially Theorem1 on p443, were read in the parent-downloaded primary text. His relevant sheaf category is explicitly quasi-coherent. That convention cannot be dropped when stating what his theorem alone proves.

## Katz and Messing, *Some consequences of the Riemann hypothesis for varieties over finite fields* (1974)

The original author-hosted PDF was downloaded from https://web.math.princeton.edu/~nmk/old/katzmessing.pdf and retained as `research/KatzMessing1974.pdf`. All five printed pages73–77 were read through rendered OCR; the theorem and proof on printed pages76–77 were also visually inspected. The seven PDF pages include a cover and final blank. Rendering files are under `research/primary_pages/`, and the complete OCR transcript is `outputs/ocr_KatzMessing1974.txt`.

Theorem2(1) constructs the Künneth components as rational polynomials in Frobenius, independently of the cohomology theory under consideration. The proof uses the relatively prime Frobenius characteristic polynomials and Cayley–Hamilton. Theorem2(2) proves the integrality and cohomology independence of characteristic polynomials of integral correspondences under its finite-field and smooth-projective absolute-irreducibility assumptions. The proof then invokes the precise cited formal correspondence argument. These restrictions remain in CL-SA19-284. The paper does not turn the letter's general-field suggestion into a universal theorem about varieties with transcendental moduli, and does not supply all algebraic inverse-Lefschetz cycles.

The chronology is independently useful. On p73, assertionD3 attributes hard Lefschetz to Deligne. Reference1 on p77 identifies his Cambridge lectures of4–11July1973. The article records receipt on8August1973 and was published in1974. Thus this primary record documents circulation of Deligne's theorem by1973. It does not identify the first announcement date. The later full treatment is Deligne's1980 *Weil II*, Theorem4.1.1. The unverified Messing1975 bibliography lead is no longer needed to establish the earlier circulation bound.

## Remaining primary-access limitations

The Hodge1938 original article remains an unopened full-text lead, despite the exact title, opening page and DOI match. The EGAIV4 original49,852,990-byte PDF exceeded web extraction limits; two direct downloads stalled and were interrupted, with outputs preserved. Its §18.11.6–18.11.7 comparison therefore appears in `publication_comparison_leads.tsv`, outside the checked links. Metadata-level verification in `references.bib` is explicitly labelled as such and is not a proof-reading event.
