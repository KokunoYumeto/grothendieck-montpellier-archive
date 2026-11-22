#!/usr/bin/env python3
"""Inventory saved Part B program/command records without rerunning checks."""
from pathlib import Path
from collections import Counter
import csv,json,time
start=time.monotonic();root=Path(__file__).resolve().parents[1];code=root/'code'
scopes={
 'part_b_finite_checks':'Exact algebra:7776 exponent candidates,126 quintic monomials,114 allowed;5 Groebner charts; divisor-square and2x2 radical; p3/p7 Hasse calculations,2 discriminants;4 identities for the symbolic infinite socle family.',
 'part_b_input_corrections':'Attached-input row export; checks actual path existence and every recorded line number, not truth by computation.',
 'part_b_inventory':'Export of28 numbered subjects plus9 Pour memoire rows; resolves manuscript theorem line locations.',
 'part_b_structural_audit':'Bib-key/label/reference/result-row consistency; not a proof checker.',
 'part_b_kleiman_ocr':'18 original Kleiman1994 pages rendered and OCRed; visual theorem reading separately recorded.',
 'part_b_archive_volumes':'Six public catalogue queries; bibliographic discovery only.',
 'part_b_oa_discovery':'Six Crossref/OpenAlex/SemanticScholar public DOI metadata requests.',
 'part_b_repository_discovery':'Six HAL/OpenAIRE/Fatcat public DOI requests; metadata and access status only.',
 'part_b_public_archives':'Four public Wayback availability requests; no private archive files.',
 'part_b_fetch_named_metadata':'Eight public OpenAlex/HAL/OpenAIRE/InternetArchive metadata requests for Lieberman1968 and Raynaud LNM119; no restricted content files.',
 'part_b_cern_record':'One advertised CERN public catalogue request; HTTP200 contains an Anubis automated-access challenge, not the record; no challenge execution or bypass.',
 'part_b_ihes_archive_search':'Advertised public IHES historical-preprint archive: actual search form and keyword/collection searches; global flag reuses observed form for exact-title searches across Item/File records. Only metadata HTML, not restricted content.',
 'part_b_hal_title_search':'Four HAL title searches without DOI restriction, allowing older preprints/theses without journal identifiers; public metadata only.',
 'part_b_special_fibre_checks':'Three exact blowup-chart monomial substitutions;15 assertions for SNC supports, torus determinants and vertical multiplicities. Global component geometry and cover comparison are proved in the manuscript.',
 'part_b_raynaud_public_snapshots':'Three public CDX queries returned empty JSON, but two used unsupported interior-wildcard URL matching; those are not valid exhaustive DOI/ISBN absence searches. Corrected queries are separately recorded. No restricted original-file request.',
 'part_b_public_book_catalogue':'One ordinary public author-catalogue request at an advertised route; HTTP403, no altered headers, retry, original-book request or file download.',
 'part_b_mit_thesis_catalogue':'One public MIT repository homepage read; actual search form action and query control inspected; no login or original file.',
 'part_b_mit_thesis_search':'Two public searches using the actually opened MIT form; both returned HTTP202 with zero bytes, so no search results were read and no zero-result inference is made.',
 'part_b_raynaud_title_catalogue':'One new title query using the actual public GET form from C\'s opened catalogue; HTTP403, stopped; no repeated author URL or altered headers.',
 'part_b_raynaud_page175_archive_initial':'Two public CDX metadata queries were started, then interrupted before result collection after a wildcard-scope problem was found; elapsed runtime not recorded. No source-content request.',
 'part_b_gabber_historical_urls':'Three public CDX requests; one unsupported interior-wildcard query broadened to103907domain records, saved outside deliverable and inspected locally; target DOI absent in returned rows is not an exhaustive absence theorem. IHES author prefix yielded18records.',
 'part_b_filtered_cdx':'Four corrected public CDX queries use documented host/domain matching plus explicit original-field regex filters,30-row and2MiB response caps. All timed out; no absence claim inferred.',
 'part_b_gabber_archived_index':'One public author-directory snapshot actually returned by CDX; metadata/catalogue HTML only, with1MiB cap; no unrelated files or correspondence requested.',
 'part_b_gabber_archived_index_initial':'Initial successful public HTTP200 response contained gzip bytes that the utility decoded incorrectly as UTF8; no catalogue text was read in this attempt. The corrected retry is separately recorded and performs ordinary gzip decoding, not access-control evasion.',
 'part_b_lorenzini_archive':'Two public CDX metadata searches restricted to the former author prefix and exact paper.html URL actually cited in Lorenzini2017; explicit prefix/exact matching, regex filter and bounded response.',
 'part_b_lorenzini_archived_catalogue':'One actual2017 public author-catalogue capture read;363 text lines and actually advertised links saved; no book download in this utility.',
 'part_b_raynaud_page175':'Follow one replacement-page PDF link actually advertised in the opened2017 scholarly catalogue;5MiB cap and explicit PDF-type validation. Visual reading identifies a modern scholarly retyping, not a publisher scan or full book; DefinitionXI2.1 complete, PropositionXI2.2 partial.',
 'part_b_gabber_title_repository':'One public OpenAIRE title/author search without DOI/year/OA restriction, allowing the1981 preprint and analog/analogue spelling variants; bounded25record/2MiB metadata result, no original content request.',
 'part_b_raynaud_archived_catalogue_metadata':'One exact public historical-catalogue metadata query for an observed author URL; returned an empty capture list, not a current denied-endpoint retry; no original file requested.',
 'part_b_raynaud_chapter2_preview':'Two sequential ordinary requests: DOI-resolved public chapter landing, then its actually advertised unchanged public preview link. Originalpp14-15 fetched and visually read, exactW definition and base-change proof; no subscription PDF or preview-limit change.',
 'part_b_gabber_advertised_preview':'One ordinary current publisher metadata request; actual HTML has no advertised public PDF preview. No guessed preview endpoint or subscription PDF requested.',
 'part_b_gabber_historical_preview':'Exact public CDX query for the observed article landing followed by one actually returned2018HTML capture. This exposes an explicit public Download preview PDF href; no source PDF requested by this utility.',
 'part_b_gabber_original_preview':'One unchanged public preview URL explicitly advertised in the opened2018publisher landing; validates actual response type and retains outcome without bypass, retry or preview-parameter changes.',
 'part_b_gabber_preview_migration':'Two independent requests: exact public archive metadata for the advertised old preview, and expressly logged stale-host repair to the actually known current public preview service, with the advertised path unchanged. Originalpp325-326 obtained; no subscription route or preview-limit change.',
 'part_b_pfluger_jubilee_catalogues':'Three independent public title-only/1907-1958 metadata queries, no Indian/Mathematical/year restriction on title queries; GoldenJubilee initially250of601, JubileeCommemoration17, exact span0; no content request.',
 'part_b_pfluger_jubilee_pagination':'Two public metadata pages for the actual601-hit query;601total rows deduplicate to505identifiers, so coverage explicitly incomplete and corrected separately.',
 'part_b_pfluger_jubilee_complete':'One bounded sorted public metadata snapshot,650row cap, resolves actual unstable pagination and yields601distinct identifiers.44broad candidates and undated text titles inspected; no original file request.',
 'part_b_pfluger_generic_jubilee_identity':'One actually returned generic-title item identity and file-access metadata read; identifies unrelated1937Hindi education volume. Publicly advertised files recorded but not requested.',
 'part_b_lieberman_variants_web':'One bounded3-query code-mode web batch: Liebermann/Liberman, homologic title variant, distinct institutional repository domains. No new original route or content-file request; actual query code preserved in .js.',
 'part_b_kleiman_dependency_render':'Four original Kleiman1968 pages rendered by an inline Python command and visually read for field conventions, Theorem2A11, isogeny input and Pontryagin/cup proof. Exact executed inline code preserved afterwards; no mathematical finite test.',
 'part_b_c2_full_scope_render':'Six original cote68 sheets rendered for independent visual audit of017 axioms,021 completeness and022 saturation; zero network requests and no mathematical finite test.',
 'part_b_lieberman_archival_queries1':'One bounded3-query web batch for offprints, IHES/Montpellier archives and Nachlass collections; no new original source or restricted-file request.',
 'part_b_lieberman_ihes_public':'Two new public IHES Item/File queries through the previously inspected ordinary form; author2hits,title0; no source-content file requested.',
 'part_b_lieberman_ihes_documents':'Two actual advertised IHES record links opened by web tool; both are HTML catalogue pages despite.pdf URL suffix, identifying different works rather than Lieberman1968.',
}
aliases={'part_b_fetch_sources_initial':'part_b_fetch_sources','part_b_fetch_required_sga_mirrors':'part_b_fetch_required_sga','part_b_ihes_archive_global':'part_b_ihes_archive_search','part_b_ihes_archive_1981':'part_b_ihes_archive_search'}
ad_hoc={
 'part_b_archive_followup':'Logged command record:four public issue/collection/catalogue metadata results; standalone executed script not saved.',
 'part_b_archive_metadata':'Logged command record:three public InternetArchive metadata results; standalone executed script not saved.',
 'part_b_archived_landing':'Logged command record:first failed public Wayback landing request; standalone executed script not saved.',
 'part_b_archived_tags':'Logged command record:successful archived HTML fetch and metadata-tag extraction; code retained in session tool log, no original standalone script.',
 'part_b_kleiman1994_fetch':'Logged command record:one original18-page PDF fetch, size/hash/page check; no original standalone script.',
 'part_b_wayback_followup':'Logged command record:public CDX and public landing snapshot requests; no original standalone script.',
 'part_b_raynaud_archive':'Logged command record:one public InternetArchive metadata request for Raynaud LNM119; private PDF/OCR and encrypted lending files identified but not requested; no original standalone script.',
}
rows=[]
for p in sorted(code.glob('part_b*output.json')):
 stem=p.stem.removesuffix('_output')
 if stem=='part_b_program_inventory':continue
 d=json.loads(p.read_text());program=aliases.get(stem,stem);script=code/(program+'.py')
 origin='code/'+script.name if script.exists() else ad_hoc.get(stem,'Logged command record; original standalone script not saved.')
 if (code/(program+'.js')).exists():origin='Executed code-mode JavaScript, preserved in code/'+program+'.js; requires tool runtime'
 if stem=='part_b_lieberman_variants_web':origin='Executed code-mode JavaScript, preserved in code/part_b_lieberman_variants_web.js; requires tool runtime'
 if stem=='part_b_kleiman_dependency_render':origin='Original inline Python command; exact executed code preserved afterwards in code/part_b_kleiman_dependency_render.py'
 records=d if isinstance(d,list) else d.get('results',d.get('records')) if isinstance(d,dict) else None
 if records is None and stem in ['part_b_archive_followup','part_b_archive_volumes']:records=list(d.values())
 count=str(len(records))+' saved records' if isinstance(records,list) else 'one saved result object'
 if stem=='part_b_finite_checks':count='126/114 monomials;5 charts; symbolic checks as described'
 if stem=='part_b_kleiman_ocr':count=str(d['pages_ocr'])+' pages OCRed'
 if stem=='part_b_inventory':count=str(d['inventory_rows'])+' historical rows'
 if stem=='part_b_input_corrections':count=str(d['input_rows'])+' input rows'
 if stem=='part_b_structural_audit':count=f"{d['statements']} statements;{d['ledger_rows']} result rows;{d['bib_entries']} bibliography entries"
 if stem=='part_b_lieberman_variants_web':count='3 actual queries in one timed tool call'
 if stem=='part_b_kleiman_dependency_render':count='4 source pages rendered and visually read'
 if stem=='part_b_c2_full_scope_render':count='6 source pages rendered and visually read; existing017 images reused'
 if stem=='part_b_lieberman_archival_queries1':count='3 actual queries in one timed tool call'
 if stem=='part_b_lieberman_ihes_documents':count='2 actual record-open commands in one timed tool call'
 if isinstance(d,dict) and 'elapsed_seconds' in d:runtime=str(d['elapsed_seconds'])+' s recorded elapsed'
 elif isinstance(d,dict) and 'runtime_seconds' in d:runtime=str(d['runtime_seconds'])+' s recorded elapsed'
 elif isinstance(records,list) and any('elapsed_seconds' in z for z in records if isinstance(z,dict)):
  timed=[z['elapsed_seconds'] for z in records if isinstance(z,dict) and 'elapsed_seconds' in z]
  runtime=f"{sum(timed):.9f} s sum of {len(timed)} individual durations; total wall time not recorded"
 else:runtime='Not recorded; no retrospective estimate supplied'
 scope=scopes.get(program,'Source-file retrieval/identification; downloaded/existing/error outcomes are retained in the raw manifest.' if program.startswith('part_b_fetch') else ad_hoc.get(stem,'Record utility; see raw result.'))
 status=[]
 if isinstance(records,list):
  c=Counter(str(z.get('status',z.get('fetch_status','error' if z.get('error') else 'metadata'))) for z in records if isinstance(z,dict))
  status=[f'{k}:{v}' for k,v in sorted(c.items())]
 rows.append([p.name,origin,scope,count,runtime,'; '.join(status)])
rows.extend([
 ['Logged Raynaud p175 source inspection','Logged PyMuPDF command; session record and notes/part_b_source_followup_20261119.md','Render/extract the recovered scholarly retyping; not an original publisher scan and not a mathematical test.','1 page','0.275457466 s recorded command elapsed','DefinitionXI2.1 complete; PropositionXI2.2 partial; not used as source closure'],
 ['Logged Raynaud III source inspection','Logged PyMuPDF command; session record and notes/part_b_raynaud_thesis_derivation.md','Render/read original publisherpreviewpp37-38; no separate historical script is invented.','2 pages','0.368257199 s recorded command elapsed','LemmaIII1.1/DefinitionIII1.2 completely read; III1.4 read but not used; III1.5 partial'],
 ['Logged Raynaud II source inspection','Logged PyMuPDF command; session record and notes/part_b_raynaud_thesis_derivation.md','Render/extract original publisherpreviewpp14-15; exactW and base-change representation read.','2 pages','0.338208832 s recorded command elapsed','LemmasII1.1-II1.2/DefinitionII1.3 read; not a finite mathematical test'],
 ['Logged Gabber original source inspection','Logged PyMuPDF command; session record and notes/part_b_gabber_original_derivation.md','Render/extract original publisherpreviewpp325-326; exact main theorem and henselian-pair definition read.','2 pages','0.15393232899805298 s recorded command elapsed','Theorem1 q>=0 and condition(b) read; laterSection5/full original proof not claimed read'],
])
with (root/'checks/part_b_results.csv').open(newline='') as f:result_count=len(list(csv.DictReader(f)))
with (root/'checks/part_b_events.tsv').open(newline='') as f:event_count=len(list(csv.DictReader(f,delimiter='\t')))
rows.append(['part_b_update_checks.py','code/part_b_update_checks.py','Deterministic owned CSV/TSV export; does not run mathematical proofs.',f'{result_count} result rows;{event_count} events','Not recorded; no retrospective estimate supplied','Exact attached SA22-0 ID retained; new IDs distinguished'])
rows.append(['part_b_program_inventory.py','code/part_b_program_inventory.py','Reads saved records and writes this inventory; no mathematical or network check rerun.',str(len(rows))+' earlier output/utility records','Recorded in code/part_b_program_inventory_output.json',''])
fields=['artifact','executed_program_or_record','scope','count','runtime','recorded_outcomes']
with (root/'checks/part_b_program_inventory.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(fields);w.writerows(rows)
md=['# Part B: programs, command records and exact computational scope','','This inventory covers every saved Part B program/output record; ordinary file reads and editing commands are not mathematical tests. Historical fetch manifests distinguish downloaded, already-existing, and error records: a20-row file manifest is not necessarily20 new HTTP requests. The current source of each saved utility is supplied. Earlier ad-hoc commands are identified as command records, rather than inventing nonexistent historical program files. No missing runtime is reconstructed from file timestamps.','','## Mathematical verification','','`code/part_b_finite_checks.py` completed in0.11084066100011114seconds. It exhausts6^5=7776 candidate exponent tuples, obtains126 degree-five monomials and114 vanishing on both prescribed skew lines, and computes Groebner basis[1] in all5 projective Jacobian charts. It also checks the divisor-square relation modulo a^2=b^2=0, the2-by-2 radical model, characteristic3 and7 Hasse coefficients, both characteristic7 discriminant factors, the toric exponent rank/relation, and all4 annihilator identities for the symbolic infinite family. It does not compute Chow groups, certify a generic-point existence statement, or prove global cohomological theorems. Those arguments are in the manuscript. No finite-check rerun was made for this reporting request.','','## Every saved program and command record','','The machine-readable complete table is `checks/part_b_program_inventory.tsv`.','','| Output or utility | Executed program or record | Scope and count | Runtime |','|---|---|---|---|']
for name,origin,scope,count,runtime,outcomes in rows:
 md.append('| '+name+' | '+origin+' | '+scope+' '+count+(' Outcomes: '+outcomes if outcomes else '')+' | '+runtime+' |')
md+=['','## Reproducibility limits','','The archive-followup, metadata, landing, tags, Kleiman-fetch and Wayback-followup JSONs were produced by ad-hoc commands. The saved JSONs preserve their actual URLs and outcomes; the exact original command is not asserted to be a file in code/. Commands still visible in the session log can be read there. Earlier source-page renders without recorded timing are not assigned a retrospective duration. The four later Raynaud/Gabber PyMuPDF source-inspection commands have their actual recorded durations explicitly listed above; no standalone historical script is invented for them. The18-page Kleiman OCR is a separately saved script with its own191.54938155499985second timing.','','The original SGA batch first recorded six403 responses in12.40092979900146seconds. A new advertised public mirror route then fetched four collections successfully in93.05661828400116seconds (individual fetch/processing times are retained). No headers, credentials, authentication or access controls were altered. Downloading a source is not reading every proof in it; bibliography notes state the actual opened passages.']
(root/'notes/part_b_program_scope.md').write_text('\n'.join(md)+'\n')
out={'inventory_rows':len(rows),'elapsed_seconds':time.monotonic()-start,'no_mathematical_tests_rerun':True}
(code/'part_b_program_inventory_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
