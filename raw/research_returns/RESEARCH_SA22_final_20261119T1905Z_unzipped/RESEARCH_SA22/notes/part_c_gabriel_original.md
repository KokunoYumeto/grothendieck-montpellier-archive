# Gabriel1932: original retrieved, read and scoped

Date:19November2026,13:43–13:49UTC. Researcher: GPT-6 Astra (OpenAI, ChatGPT Pro mode; inherited effort not separately exposed), agent part_c_algebra.

## Retrieval and provenance

The earlier unsuccessful Wiley/Oxford/institutional searches are retained in part_c_required_originals.md. A new ordinary public Internet Archive catalogue request succeeded. Searching only year1932 had found volume34. Searching volume33 instead located the journal volume catalogued as1931–1932; this explains why the earlier year-only query missed it.

The public metadata record is sources/gabriel1932_london-mathematical-society-proceedings_1931-1932_33_metadata.json. It advertises the ordinary PDF and OCR with no private flag and no access-restricted-item flag. An ordinary request to that advertised download URL returned HTTP200, following only the server's own redirect. No authentication, private file, encrypted lending file, alternate-host workaround or restriction bypass was used.

Full original URL: https://archive.org/download/london-mathematical-society-proceedings_1931-1932_33/london-mathematical-society-proceedings_1931-1932_33.pdf

The full volume is saved as sources/gabriel1932_volume33.pdf,28,691,408bytes,SHA256 b1df300eb9954052fbb4cbf1c0994e3bfd61fe777ec8c426aef102b2d08d3089. The article is PDFpages40–59, printedpp32–51, extracted as sources/gabriel1932.pdf. Its text and nine rendered original pages are saved alongside it. The extracted-file hash is in code/part_c_gabriel_article_extract_output.json.

The web retrieval tool still reports that URL inaccessible (turn265035093view0), but the successful ordinary HTTP response, complete local PDF and original page images are recorded. This is opened original content, not merely metadata.

The official publisher's1932 publication year was independently rechecked in turn192811562search0, turn192811562search1 and turn192811562search5. The article's1930 running headings are the meeting/read date. The volume title page also gives1932, although OCR misreads the digits as1982.

## Exact mathematical passages inspected

Printedp32, §1 defines a symmetric multiset: every value other than its maximum has even multiplicity, and its maximum has odd multiplicity. A strictly symmetric arrangement additionally puts a maximum at index0 and has equal values at indices n and −n. All unnamed sums have total index zero.

Printedp33 defines two alternating descending arrangements, in the orders (0,1,−1,2,−2,...) and (0,−1,1,−2,2,...). They are reflections. The same page explicitly explains why putting every factor in the same biased arrangement cannot maximize every zero-sum convolution. Printedp34 also rejects a permutation-asymmetric alternative.

**Theorem1, printedp34**, with proof in §§2–3,pp34–38: for three finite nonnegative sequences, with the third value multiset symmetric in the stated sense, the zero-sum convolution is bounded above by arranging the first sequence in one alternating order, the second in the opposite order and the third symmetrically. Reflecting the first two choices gives the same bound. Section2 reduces to0–1 sequences through a linear fractional expression; §3 counts triple intersections of three families of parallel lines in the plane r+s+t=0. The statement, hypotheses, notation and reduction were inspected on original images; damaged OCR equations were not trusted.

**Theorem2, printedp38**, with proof onpp38–39: two arbitrary finite nonnegative sequences and any further finite number of symmetric multisets satisfy the corresponding inequality. The induction uses the prior case and the symmetric decreasing order of the convolution of the symmetric factors.

The Fourier-moment consequences are in §6,pp41–42. Equality cases begin§7,p42 and continue through Theorems5–7,pp46–51. These later results are not imported as premises for C2 or an arbitrary-group classification.

## Relation to the research task

The new unnumbered paragraph after C-K-replacement in sections/part_c.tex cites exactly §1,pp32–34,Theorem1,p34,andTheorem2,p38. In modern notation the three-factor bound is (a*b*c)(0) ≤ (a⁺*b⁻*c*)(0), with opposite alternating orders and the stated symmetric-multiset hypothesis on c.

The original does not assert the arbitrary-group cone implication refuted by C-K-counter. Its parity-sensitive arrangements on the integers cannot be substituted for the literal axioms of68/017 or arbitrary factors in the generated convolution cone. The independent C2 counterexample and exact majorization replacement remain the proof inputs. The literal Gabriel named-source retrieval obligation is now complete.

## Programs actually run and limits

| Program | Scope/count | Runtime |
|---|---|---:|
| part_c_sources_fetch3.py |2ordinary requests, including year1932 catalogue |19.678302092s total |
| part_c_gabriel_catalog.py |1volume33 query and3public metadata records |28.259687334s |
| part_c_gabriel_fetch.py |1ordinary public PDF download,HTTP200 |19.526593716s |
| part_c_gabriel_locate.py |Text extraction from582-page volume; locatedPDF40–59 |11.505312518s |
| part_c_gabriel_article_extract.py |Extract20article pages;render9pages;all subprocesses0 |15.762695708s |

All scripts and stdout/JSON outputs are in code/. These are source-reading utilities, not proof tests. Metadata for irrelevant first-series1901 volume33 was inspected but its content was not downloaded. The volume and extracted article are different files of one source.
