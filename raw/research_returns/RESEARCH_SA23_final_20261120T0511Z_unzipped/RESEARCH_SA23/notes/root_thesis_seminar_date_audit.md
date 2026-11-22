# Thesis, Schwartz seminar and publication-history routes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run
SA23-20261120, 20 November 2026. We claim no priority.

## Question and result

We seek a dated identification of cote 1 physical pages 79–80 and 111–112,
or of their distinctive trace/genus-zero proof. The sources below supply
specific catalogue and drafting leads, but none of the passages inspected
identifies those leaves. This is a bounded result. In particular, a date
for a thesis, course or related Bourbaki draft is not automatically a date
for an undated proof in the Montpellier dossier.

## Original thesis catalogue

We opened the primary SUDOC record at
https://www.sudoc.fr/108391841 and its explicitly advertised alternate
RDF representation, https://www.sudoc.fr/108391841.rdf . The record gives
1953, Paris: Faculté des sciences, one volume of 130 folios, 30 cm, and a
doctoral thesis at the Université de Paris (1896–1968), Faculté des
sciences. Its title contains the catalogue spelling “popologiques”.
The record supplies no digital thesis link. We did not open the original
thesis or identify its 130 folios with the cote 1 dossier. The record's
creation and modification timestamps are catalogue metadata only.

The canonical HTML is 1,494 bytes, SHA256
171f64f207ea1cd1b8befe270480d0c8934c5c420b41dbe3759c3c9e98013e3a.
The alternate RDF is 4,011 bytes, SHA256
906a46df76a0446c3edbbdd206223c2ccb02361761d7313794e92f3509adae11.
The latter has the generic local suffix `.html`; its actual content is
RDF, not a visually opened thesis. Exact-title and folio-count searches
gave no publicly opened original thesis. Algebra is following this
specific catalogue route independently; its additional results belong
to its own dated audit.

## Original Schwartz seminar, 1953–1954

We opened the complete volume contents at
https://www.numdam.org/volume/SLS_1953-1954__1_/ and read all 24 titles.
We then downloaded the two relevant original PDFs:

* Introduction: https://www.numdam.org/item/SLS_1953-1954__1__A1_0.pdf .
  We directly displayed physical page 2, original printed page III, at
  width 1600 pixels. It explains the seminar's substantial dependence on
  Grothendieck's thesis, then forthcoming through the AMS, and distinguishes
  other contributions. It does not identify the target sheets.
* Laurent Schwartz, *La théorie des opérateurs nucléaires*, exposé 12,
  17 February 1954, printed pages 1–7:
  https://www.numdam.org/item/SLS_1953-1954__1__A13_0.pdf . We searched the
  complete native text and directly displayed physical pages 2 and 4,
  printed pages 1 and 3, at width 1600 pixels. The first defines the
  tensor trace. The latter's eigenvalue criterion explicitly assumes a
  Hermitian operator. It therefore does not give a proof of the general
  nonnormal trace-class identity merely by the displayed eigenvalue sum.
  We do not claim to have visually read all seven article pages.

The introduction has two physical PDF pages, 133,446 bytes, SHA256
5ee4c8ea53b1b60eef4da7bf16330dc49304f70b7b8560b37a55db8cf50182f0.
The nuclear-operator article has eight physical PDF pages, 841,296 bytes,
SHA256 0afc693476c381a7544ce64a6f14ed38c97869565c586c27b89ca014ff43345c.
The three actually viewed images and measured render logs retain the
physical page numbers. These readings have not supplied a manuscript date.

## Paumier's original historical research as a finding aid

We retrieved Anne-Sandrine Paumier's 2014 thesis, *Laurent Schwartz
(1915–2002) et la vie collective des mathématiques*, Université Pierre
et Marie Curie, from the author's IHES page:
https://www.ihes.fr/~/paumier/docs/these_PAUMIER.pdf . This 455-page PDF is
7,788,500 bytes, SHA256
1e669a5b639eb340af278cd7bb00c964cd54e5f2aaf3269b1a60c5dddf3e6a3b.
We searched the full native extraction for trace/Fredholm/genus-zero,
Lidskii and early Grothendieck correspondence terms, and read the 493-line
saved context extraction. We also read the complete extracted context
around printed page 64. We have not visually read all 455 pages.

The concrete new locator is printed page 64, footnote 73: Bourbaki
rédaction 179, archive identifier nbr_082, *Produits tensoriels
topologiques*, May 1953, with a pencilled Schwartz attribution. This is
a lead to an original draft with a date attribution. At the time of this
initial check, the category agent was assigned to locate the draft and
check whether it actually identifies or contains the proof at issue.
That inspection is now complete: the public archived scan contains a
catalogue cover and eight typed pages, all visually read by that agent,
and no trace or genus-zero argument. Root separately displayed the cover,
first typed page and enlarged margin, confirming the visible wording
“Schwartz” and “mai53”; annotation authorship and inscription time remain
unverified. The full source path, hash and content map are in
`notes/category_bourbaki_nbr082_date_audit.md`.
Neither its subject nor Paumier's locator alone
establishes a date for cote 1. Other relevant contexts, including printed
pages 158–165, concern the published nuclear-space work without an
identification of the crossed-out sheets.

## Brazilian follow-up after the inventory inspection

We opened Circe Mary Silva da Silva's research article, *A construção de
um Instituto de Pesquisas Matemáticas nos Trópicos – o IMPA*, Revista
Brasileira de História da Matemática 4(7) (2004), 37–67, through the public
publisher web extraction:
https://www.rbhm.org.br/index.php/RBHM/article/download/241/227/473 . We
read the relevant course discussion at printed pages 43–46 and references
at page 66. A local PDF request returned HTTP 406; we do not claim a local
PDF inspection. The cited courses and Lyra/Gama correspondence do not
identify a trace-proof enclosure in the passages checked. The archival
references there are not item-level shelfmarks for these sheets.

We also opened the official IMPA memory and history pages and followed
the actual public activity-report link:
https://impa.br/arquivo_base/sobre/acesso-a-informacao/relatorios-de-atividades/ .
That page lists 1997–2007 activity reports and directs later reporting to
the management-report area. It does not link the 1955 original identified
in the CNPq inventory. This is a finding about this page's displayed list,
not a claim that the 1955 report has been lost or is absent elsewhere.
The original report remains unopened.

## Reproducibility and movement assessment

Raw web batches are `notes/root_history_web16.json` through
`notes/root_history_web30.json`. The final batch initially exceeded the
conversation output budget; it was subsequently read from the saved JSON,
so its results were not silently assumed. Fetch batches
`logs/root_history_fetch05.json` and `logs/root_history_fetch06.json`
record all successes and failures, hashes and measured runtimes.
`code/fetch_public_sources.py` and `code/render_source_pages.py` are the
saved utilities. The Paumier search pattern and resulting context are
retained in `notes/root_paumier2014_keyword_contexts.txt` and the saved
command/source records.

No open row has changed status and the remaining gate is not strictly
smaller. The next discriminating evidence is still a dated identification
of the particular leaves or proof. New catalogue endpoints, the related
1953 draft locator and these source qualifications are not counted as
movement under the user's stopping rule.
