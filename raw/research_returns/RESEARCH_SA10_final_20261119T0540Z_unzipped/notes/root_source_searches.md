# Root source searches and readings

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026.

No claim of novelty or priority is made. The following searches were made before treating a derived statement as a contribution of this run.

## Main gluing theorem

- Queries: “Ayala Francis Tanaka Local structures stratified spaces unzipping 1409.0501”; “SGA 4 Exposé IV 9 recollement topoi faisceaux fermé ouvert”; “SGA4 IV 9.5 recollement topos foncteur exact gauche”; “Local structures on stratified spaces Unzip Theorem”.
- Opened AFT arXiv v6 PDF, especially Corollary 7.3.7, Theorem 7.3.8, Proposition 7.3.10, Proposition 8.2.3. The earlier author-hosted 85-page version was also opened but numbering in the paper uses v6, 92 pages.
- Opened SGA4 tome1 revised primary PDF (2015) Exposé IV 9.5.1–9.5.7 and 9.6; full PDF fetched locally. A search result/English transcription was used to locate the source, not as sole authority.
- Tried arXiv source retrieval in the web tool; it returned DisabledError. The cote150 subrun successfully fetched the source via urllib. This access distinction is recorded rather than calling the failed open a successful reading.
- Queries for an exact deletion criterion: “sheaves diagram open subsets colimit topos simply connected nerve stalk descent”; “colimits topoi simply connected”; “descent open sets groupoidification”. These found related descent and simply-connected-limit literature, but no exact source for A1.5 was identified in the search. A1.5 therefore carries its complete direct proof, without a priority claim.

## Stable graph infima

- Queries: “stable graphs moduli curves poset common refinement meet semilattice genus 1 4”; “stable graphs poset lattice intersections boundary strata moduli curves common refinement”.
- Opened and fetched Johannes Schmitt, The moduli space of curves (30 September 2020), Proposition 4.14, Section 6.1 and Section 7.3. These establish the geometric interpretation of contractions and boundary strata. The classification in A4.5 was independently derived and checked by the attached enumeration; the actual EXIT_TOWER paper is not among the supplied files.

## Original manuscript

- Opened the Montpellier archive index, whose HTML links point to /147.pdf, /150.pdf and /151.pdf via its PDF viewer.
- Fetched /151.pdf (27,695,508 bytes; SHA256 in fetch_primary_A.out). Download required 632.859 seconds; it succeeded without replacing the source by an AI modernization.
- Visually inspected original PDF page 71. The handwritten insertion explicitly says “mais pas” before the open-immersion parenthesis. This confirms the supplied second-pass transcription and corrects STUDY.md line 221 and the premise of task A.2.
- Direct read: second-pass 151/047–075 in full; 150/039–043 in full; study/STUDY.md relevant lines 140–165, 190–260, 300–325 and the map's EXIT_TOWER summary.
- The 151/060 symbol S versus Sigma is immaterial to A1.3: both readings use the explicitly displayed union defining that symbol. In the example all such lower unions are R. The doubtful strict/non-strict cutoff in the explanatory pseudo-partition is not used.

## Category decisions

- We do not apply the shape functor to a bicategorical colimit of ordinary topoi and infer an infinity-categorical shape colimit.
- We do not identify a pro-topos with its ordinary inverse limit.
- For infinite index families, Cech degree q is one synchronized pro-coproduct; no infinite-product/filtered-colimit interchange is used.
