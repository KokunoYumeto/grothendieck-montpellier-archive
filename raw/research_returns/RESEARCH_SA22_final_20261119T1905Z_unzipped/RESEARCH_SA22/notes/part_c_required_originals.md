# Required algebra originals and precise scope

Researcher: GPT-6 Astra (OpenAI, ChatGPT Pro mode), `part_c_algebra`. Date2026-11-19. Retrieval interval began approximately13:06UTC. These source records do not create a new claim of priority.

## Knudsen–Mumford1976 — original opened

Finn Faye Knudsen and David Mumford, *The projectivity of the moduli space of stable curves. I: Preliminaries on “det” and “Div”*, Mathematica Scandinavica39 (1976),19–55, DOI10.7146/math.scand.a-11642.

- Official migrated journal page opened: `https://journals.msp.org/mscand/article/view/2000`, ref `turn660614806view0`; original PDF viewer link `turn178881246view0` did not expose readable PDF content. Official direct-download request was inaccessible (`turn280178123view0`).
- Full37-page original scan opened/downloaded from the institutional Stuttgart host: `https://pnp.mathematik.uni-stuttgart.de/lexmath/kuenzer/knudsen_mumford.pdf`, ref `turn960245670view0`. Local file `sources/knudsen_mumford1976.pdf`, SHA256 `24b8a0a0b41e3dd581998ca7134f7f867dd5cf424beaa27e128b74308b68364c`,5,474,009bytes. Actual retrieval script/output: `code/part_c_sources_fetch2.py`, `_output.json`, `_output.txt`.
- An independent author-hosted original compilation is also opened at `https://www.dam.brown.edu/people/mumford/alg_geom/papers/1976b--DetDiv%2BKnudsenSequel-GT.pdf`, ref `turn382174588view0`. It contains92PDF pages including the original article and sequels. We do not confuse sequel theorem numbering with the1976 article.
- Original exact locators: ChapterI starts printedp20. Graded lines, Koszul interchange and the degree-zero exterior determinant are onp20. The canonical determinant isomorphism of a short exact sequence and its compatibility are onpp21–22. **Definition1, pp23–24** gives determinant functors on bounded complexes of finite locally free sheaves, quasi-isomorphisms, exact-sequence compatibility, base change and normalization. **Theorem1, p25** gives existence and uniqueness up to canonical isomorphism. Rendered local page images were visually inspected; OCR is a search aid only.

### Original printed sign correction, independently checked

The displayed interchange on printedp20 has exponent `alpha(x)+beta(x)`. The correct Koszul exponent is their **product**. This is visible in the original scan, not an OCR inference. The correction is forced already by free rank-one summands: for basis vectors `e,f`, the block swap has determinant−1 because `f wedge e = - e wedge f`; the printed sum gives `(-1)^(1+1)=+1`, while the product gives−1. For ranksr,s, moving allr vectors of the first block past alls of the second usesrs elementary swaps, hence gives `(-1)^(rs)`. This sign is compatible with associativity because `r(s+t)=rs+rt`; it is symmetric because `rs=sr`. The small exact program `part_c_determinant_sign.py` verifies the2×2swap and all8parity triples; its output is attached. These checks are not claimed to verify the full determinant theorem.

### Exact relation to cote68/056 and R13

Input file `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_68_033-056+162-1+162-6_transcription.tex`, lines918–966:

| Exact location | Claim on the sheet | Checked relation to the opened source |
|---|---|---|
| lines918–926 | Fixed commutative ringk, finite free modules, isomorphisms | This is a degree-zero, fixed-affine-base subcategory of KM's locally free setting. |
| line933 | Graded rank-one free modules with Koszul commutativity | The correct sign is the product of ranks; it agrees with the intended KM convention after the printed correction above. |
| lines937–946 | Monoidal determinant functor, normalized on rank-one modules | Realized by `Delta(V)=(wedge^rank(V)V,rank(V))`, with direct-sum wedge isomorphism. It is the degree-zero normalization in KMDefinition1(v),p24. |
| lines948–966 | Independence of a complementary summand; equivalently block-unipotent automorphisms act trivially | Exactly the splitting independence behind the canonical exact-sequence isomorphism onp21. If `V=W1 directsum W2` and another splitting differs by `A:W2->W1`, its transition is block matrix `[[I,A],[0,I]]`; expanding the top wedge, every term involvingA has a repeatedW1factor and vanishes, leaving the original volume. Thus its determinant is1 over every commutative ring, with no domain assumption. |

The displayed diagram's uncertain `W|V` at line958 must have targetV, and the lower-left `V1` at line960 must beW1 for its written maps to type-check. We use the unambiguous equivalent automorphism sentence atline966 for the calculation, so no conclusion depends on choosing an unread glyph.

**Correction of scope:** promptR13's phrase “056 gives Knudsen–Mumford's axioms” is accurate only as a description of the finite-free degree-zero part. KMDefinition1 additionally includes complexes/quasi-isomorphisms and naturality across base change. The sheet does not state that entire system. We do not import KM's uniqueness theorem as a uniqueness theorem for arbitrary fixed-ring functors satisfying only the three displayed conditions. No such stronger assertion is used in PartsC1/C2.

The inherited study's `CHECK_EVENTS.tsv` has no determinant row forSA22-12/056; its neighboring exact inherited IDs are `SA22-11 (68/050-052)` and `SA22-11 (68/054)`. We do not repurpose either orientation/Stokes event as if it checked determinants. The new event is explicitly `SA22-12 (68/056; R13 determinant comparison)`; no claim is made that this full string was a previous event ID.

Exact inherited prose requiring the scope qualification is `upload/PROMPT(20261119-110314).md:113` and `inputs/RESEARCH_SA22_study/study/STUDY.md:730`. The latter explicitly says “from memory” and already points to a conditional SK1 issue. We preserve that caveat and do not assert fixed-ring uniqueness from the opened theorem.

Program scope/runtime: source download `part_c_sources_fetch2.py` made2public requests in38.455787seconds (one fullPDF, one failed local frontmatter fetch); `part_c_km_ocr.py` rendered/OCRed14pages in254.124344seconds, all subprocess returncodes0, and is a source-reading utility rather than a proof check; `part_c_determinant_sign.py` made1rank-two swap and8parity checks in0.000025618seconds using exact integers. All scripts and stdout/JSON outputs are saved. No OCR equation is accepted without the visual check.

## Gabriel1932 — retrieval history; original now opened

Update13:49UTC: the complete original article has now been retrieved from the public volume33 scan and inspected. The successful route, original theorem locators, mathematical scope and program evidence are in notes/part_c_gabriel_original.md. The failed approaches below are retained as history; the current bibliography is marked opened.

R.M.Gabriel, *The Rearrangement of Positive Fourier Coefficients*, Proceedings of the London Mathematical Society, series2,33(1)(1932),32–51, DOI10.1112/plms/s2-33.1.32. The official record says received24June1930; that is not the journal publication year.

- Original Wiley article page opened: `https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s2-33.1.32`, ref `turn960245670view2`.
- Its actual advertised PDF link18 was followed. It redirects to the abstract HTML, ref `turn283840751view2`; it is not an opened PDF.
- Oxford original landing page at `https://academic.oup.com/plms/article-abstract/s2-33/1/32/1523057` failed after redirect to the publisher's article-minimal endpoint (`turn660614806view2`). No authentication or anti-bot workaround was attempted.
- Exact-title/DOI/institutional-host and full1932second-seriesvolume33 queries, in both search engines, found metadata and citations, including the official issue TOC (`turn196042107search1`). No alternate original mathematical text was retrieved. Queries specifically for archive.org1932/second-series33 produced no original. A public archive catalogue API request failed through web retrieval (`turn793620389view0`); this is not evidence that the archive lacks the item.
- Modern papers and theses that cite Gabriel were not substituted as the original. Current C2proofs are independent; HLPChapterX original remains opened. At the time of these failed approaches Gabriel was marked not opened. That historical status was superseded by the successful public-volume retrieval and original inspection recorded in the13:49UTC update above; the current bibliography is marked opened.

## Raynaud thesis identity — metadata resolved, full theorem text not opened

At B's request, a short independent check distinguished three different1970works. The thesis requested by the prompt is **Faisceaux amples sur les schémas en groupes et les espaces homogènes**, Paris1968, published as SpringerLNM119(1970), not the Picard specialization article and not LNM169*Anneaux locaux henséliens*.

Primary institutional thesis catalogue: `https://bibliotheque.imo.universite-paris-saclay.fr/bibliotheques-numeriques/theses/Paris/`, opened `turn660614806view1`, exact Raynaud entry `turn178881246view1`, lines1546–1550: title, author and1968. That entry has no linked scan. Official publisher book page `https://link.springer.com/book/10.1007/BFb0059504` opened `turn960245670view1`, identifies LNM119 and1970. Original public front matter PDF `https://link.springer.com/content/pdf/bfm:978-3-540-36249-4/1` opened `turn283840751view0` identifies first edition1970 and second corrected printing1986; its contents distinguish the relevant chapters. Local fetch of that URL returnedHTTP400; web opening succeeded, so access status is accurately partial.

The publisher's introduction chapter, DOI10.1007/BFb0059505, was opened only as a metadata/subscription page (`turn283840751view1`); it expressly offers no SharedIt link. Exact-title public institutional searches found citations but no mathematical full text during this short task. This identifies the requested original without closing its full-text source gate. B was notified and owns integration of the corrected Raynaud bibliography record.
