"""Serialize the actual search record and manually assigned claim/search coverage.

The semantic assignments below were written by the reviewer. They are not keyword
classification. Search results are inventoried as titles, URLs and retrieval IDs;
the raw calls preserve the exact requests and returned text for local audit.
"""
import json,re,csv
from pathlib import Path
P=Path(__file__).parent
B={
1:'Initial targeted searches for constructibility over universally Japanese bases, exact birational Pic^tau invariance, Grothendieck–Murre9.2.3 and stationarity of birational fundamental groups. Déglise primary notes and SGA sources emerged; modern AI transcriptions were only leads.',
2:'Alternative formulations of birational Picard invariance, formal tame comparison and point-supported distributions. No exact normal-source nonreduced Pic^tau theorem or N385 provenance was identified.',
3:'Opened Déglise Theorems1.1–1.4, LSS arXiv record, Stacks0C6S and Kleiman. The constructibility theorem is exact; Pic[n] invariance became a target for independent checking, not trusted background.',
4:'Opened SGA1 primary reedition, SGA3 VIII primary reedition, ESS arXiv, Grothendieck–Murre publisher contents and Esnault–Kindler record. Bibliographic and theorem-text access are distinguished.',
5:'Named-service searches including zbMATH, Numdam, MathOverflow and the alleged distribution/Bourbaki385 source. Found Picard bibliographic leads; no exact fate of the unrestricted model questions.',
6:'Opened Bourbaki236 and Néron–Samuel metadata, SGA1 X finiteness/hyperplane passages and SGA3 Hom representability footnote. The Picard metadata is not an exact theorem proof.',
7:'Read ESS and Esnault–Kindler precise scope, Grothendieck–Murre chapter structure, and Kleiman Remark5.8. Finite-kernel curve restriction is weaker than an arbitrary nonreduced birational Picard isomorphism.',
8:'Followed author/bibliography leads to KLOS and Rülling–Saito. Their smooth/classical Picard results were separated from the manuscript normal-source infinitesimal problem.',
9:'Further MathOverflow/zbMATH and N385 queries gave no exact theorem or source identification. This is a bounded negative search, not evidence of novelty or current openness.',
10:'Opened tame-ramification and proper-homotopy framework; found SGA7 and author bibliography leads. An AI transcription of SGA7 was not accepted as primary proof evidence.',
11:'Opened author publication list and followed ESS/LSS primary links. Used this to check stronger modern finiteness assertions in the earlier context.',
12:'Opened ESS author PDF and SGA3 exactness passages. LSS publisher URL returned403; its arXiv record remained available. The failed publisher access is not labelled a checked proof.',
13:'Opened SGA3 VIII§§2–3, SGA1 X2.8–2.12, KLOS, Rülling–Saito Cor11.24, Esnault–Kindler and its erratum. Exact good-compactification, smooth/fibred, Lef/Leff and ample-complete-intersection hypotheses retained.',
14:'Targeted Picard and formal-comparison searches followed by KLOS10.3.4–5,10.3.9,10.3.13. Classical birational Cl0 and the normal morphism-Albanese were distinguished; no nonreduced stabilization conclusion inferred.',
15:'Opened Bourbaki236 primary PDF, Stacks0C6R units/Picard exact sequence and04DY nil-invariance. Named-service searches for the formal comparison did not expose the final theorem text.',
16:'SGA7 web parser rejected the large PDF; direct fetch later succeeded and the Raynaud pages were read visually. Grothendieck collected bibliography, Lipman1974 and Esnault–Kindler exact theorem were opened. Grothendieck–Murre full publisher PDF remained inaccessible.',
17:'Read the Esnault–Kindler erratum, purity, Kunz/Frobenius, reflexive extension, Kummer, Lipman§2.4 and Kleiman proper Pic^tau passages. These constrain the reconstructed proofs but do not fill omitted hypotheses.',
18:'Additional searches on boundary-tame finite generation, partition H1 finiteness and regular-locus Picard comparison; opened tame, connected-cover and Bertini framework. No blanket FG/FP identification made.',
19:'Further N385, zbMATH SGA7 and MathOverflow Picard searches; opened SGA7 publisher metadata. The reused distribution source and exact omitted draft propositions remained unlocated.',
20:'Targeted generic-fibre descent and reduced-fibre adjective searches. Found Katz–Lang as a later primary route; Stacks proper homotopy, normalization and proper-target rational-map inputs were read with their scopes.',
21:'Revisited Déglise exact statements, ESS tame-curve input and LSS dates. Opened Milne cohomology, Conrad Picard curves and Moonen Tate modules as precise background for finite coefficients and Picard rank.',
22:'Queries for Katz–Lang generic exactness, Picard invariance, formal9.2.3 and distributions. Located the author-hosted Katz–Lang scan; opened the blowup definition and an SGA1 homotopy passage.',
23:'Named-service/formal-étale searches and exact Stacks Artin–Schreier, unramified and specialization pages. Katz–Lang primary PDF opened. Specialization direction and object-versus-morphism lifting distinguished.',
24:'Targeted divisor localization, supersingularity, EGAI10.12.3 and Schwartz searches. Located the exact Katz–Lang Lemma2 and primary Sutherland/Schwartz/EGA leads.',
25:'Opened EGAI bibliographic metadata, Schwartz1947 primary PDF, Sutherland primary PDF, formally étale definition and Stacks divisor chapter. EGA metadata alone did not certify the numbered proposition.',
26:'Read Katz–Lang proof and divisor-class presentation; EGAI PDF exceeded web parser size. Read Schwartz§1 only as historical background, not as identification of N385.',
27:'Read Katz–Lang Lemma2 proof and§2 elementary-fibration references in full at the targeted passage. Smooth-surjective normal-base version is exact; broader reduced-fibre wording remains unresolved. Divisor localization proof checked separately.',
28:'Targeted primary search for Mumford theta groups and Weil pairing to make the elliptic nonsplitting example algebraic before formal completion.',
29:'Opened Mumford1966 and Moonen theta-group chapter. Read symmetric multiplication formula, group extension and commutator definitions.',
30:'Read Mumford§1 Theorem1 pp293–294 and Moonen8.24–8.25. Nondegenerate theta commutator supports the explicit finite tame covering, whose formal completion was then checked independently.',
31:'SGA4I PDF URL exceeded the web parser size. The parent-fetched original PDF was read visually at I8.13.2–4 and8.3.2–3. Exact categorical hypotheses saved in SGA4_8133_check.md; this is an auxiliary check for root scans105/183.',
32:'Reopened exact SGA1 X2.10–2.11 for the cross-package Bertini audit. The proper normal hyperplane theorem does not alone justify arbitrary local-property clauses or naive iteration through nonnormal special sections.',
33:'Targeted local Bertini, geometric-unibranch and morphisme net searches. Relevant SGA2/EGA and later Zhang leads appeared; no exact combined draft local-property theorem was identified from primary text. Root was advised to retain classC for that combined claim.',
34:'Targeted Jouanolou1983 locators and book access. Publisher/library metadata did not expose the book; Poonen’s primary talk slides gave a useful exact-quantifier lead.',
35:'Opened Poonen’s8 May2020 slides and Stacks Bertini chapter; located the Poonen–Slavov primary research paper. No conclusion was drawn from its abstract alone.',
36:'Opened Poonen–Slavov author PDF and located Theorems1.5/1.8; reopened Stacks37.32.3 and its algebraic proof. Theorem1.5’s equidimensional-fibre assumption was not omitted.',
37:'Read Poonen–Slavov Theorem1.8 and Lemma7.1 with§7 proof. The exceptional-divisor hyperplanes form a proper locus, so image dimension≥2 gives generic geometric irreducibility for arbitrary morphisms. This exactly supplies the corrected generic statement needed for root240 and earlier67.',
38:'Searched publication and circulation dates for Poonen–Slavov; located arXiv2001.08672 and publisher metadata.',
39:'Opened arXiv record confirming first23 January2020 and revised4 August2020. Publisher article URL redirected to an inaccessible endpoint; print issue metadata is reported only as a search lead.'
}
M={}
def assign(ns,bs):
 for n in ns: M[n]=bs
assign([1,2],[1,20,22,24,25,26,27])
assign([3,4,5],[1,3,5,6,15,18,21])
assign([6,7,8,9],[1,4,6,7,18,20,21,22,27])
assign([10],[1,18,20,22,24,27])
assign([11,12,13,14,15,17],[4,6,7,8,11,12,13,16,17,18,21])
assign([16],[4,6,13,21])
assign([18,19,20,21,22,23,24,25],[6,7,13,17,18,22,24,32,33])
assign([21],[6,7,13,17,18,22,24,32,33,34,35,36,37,38,39])
assign([26,27,28,29,30,31,32],[1,2,5,9,17,18,20,22])
assign([33,34,35,36,37,38],[1,2,5,6,7,8,9,14,15,16,17,18,19,21])
assign([39,40,41,42],[1,2,14,17,21,23])
assign([43,44,45,46,47,48,49,52],[1,2,5,6,7,8,9,14,15,16,17,18,19,21])
assign([50],[1,14,21,24,25,27])
assign([51],[1,2,14,21,24])
assign([53,54,55,56],[4,8,13,14,15,16,17,18,19,21])
assign([57],[4,17,20,23])
assign([58,59,60],[1,4,10,14,15,16,19,20,23,25])
assign([61,62],[4,5,17,19,20,23,25])
assign([63,64,65,66,67],[10,16,19])
assign([68,69,70,71,72,73],[2,5,9,19,22,24,25,26])
assign([74,75,76,77,78,79,80],[4,6,12,13])
assign([81,82,83,84,85,86,87,88,89],[1,2,4,14,15,16,17,19,21,23,28,29,30])
assign([90,91,92,93,94],[3,14,15,16,17,19,23,24,25,26,27])
assign([95,96],[4,14,15,16,19,23,24,25,26])
assign([97,98,99,100,101,102],[1,4,5,10,14,15,16,19,23,24,25,26])
claims=json.loads((P/'claims.json').read_text())
assert set(M)=={int(c['id'].split('-')[-1]) for c in claims}
files=sorted(P.glob('web_batch_*.json'))
calls=[];results=[];refurls={};loaded=[]
for path in files:
 n=int(path.stem.split('_')[-1]);d=json.loads(path.read_text());req=d['request'];res=d['result']
 texts=[v.get('text','') for v in res.get('content',[]) if v.get('type')=='text']
 body='\n'.join(texts)
 headers=re.findall(r'^([^\n]+)\s+\((https?://[^\n]+)\)\n【([^】]+)】',body,re.M)
 for title,url,ref in headers:
  refurls[ref]=url
  results.append(dict(batch=n,title=title,url=url,ref=ref,access='failed' if title.startswith('Internal Error') else 'returned result; see request type and manual scope'))
 loaded.append((n,req,body,headers))
 for tool,args in req.items():
  if tool=='response_length': continue
  for a in args:
   calls.append(dict(batch=n,tool=tool,arguments=json.dumps(a,ensure_ascii=False),source_url=refurls.get(a.get('ref_id',''),a.get('ref_id','') if str(a.get('ref_id','')).startswith('http') else '')))
mapping=[]
for c in claims:
 n=int(c['id'].split('-')[-1]);bs=M[n]
 mapping.append(dict(claim_id=c['id'],exact_target_and_quantifiers=c['statement'],batches=[f'web_batch_{b:02}.json' for b in bs],refs=c['refs'],result=c['fate'],limits='Related claims share exact topic searches and opened passages. This is not a claim that every listed batch separately queried this full sentence. The target quantifiers were manually compared with the cited results.'))
(P/'claim_search_map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
for name,records,fields in [('SEARCH_CALLS.tsv',calls,['batch','tool','arguments','source_url']),('SEARCH_RESULTS.tsv',results,['batch','title','url','ref','access'])]:
 with (P/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(records)
out=['# Literature search and source-access log — 29a\n',
'Review date: 2026-11-19 UTC. The batches are in execution order; exact per-call clock times were not recorded and are not reconstructed from file mtimes. Every claim has a manually assigned searched target in `claim_search_map.json`. The search map carries the full quantifiers, so broad topic similarity is never the asserted basis for exact settlement.\n',
'## Method and negative-search limits\n',
'Searches used the two available web search engines, with stronger primary-source verification when needed. Named zbMATH Open, arXiv, MathOverflow and Numdam searches are preserved verbatim below. The zbMATH and MathOverflow queries were targeted web-index searches, not claims to have exhaustively queried every database record. EGA/SGA originals, author-hosted papers, publisher contents and author bibliographies were followed backwards. Modern AI translations and search snippets were leads only; no theorem-level verification rests on them.\n',
'A returned search result is not an opened source. Requests below distinguish search, open, find and screenshot. Bibliography `verified` records access, and its annote states whether theorem text, proof, metadata or only a table of contents was read. No hit, failed access, or an unavailable preliminary proposition does not establish novelty or present openness.\n',
'## Claim coverage\n']
for m in mapping:
 out+=['### '+m['claim_id']+'\n','**Exact target:** '+m['exact_target_and_quantifiers']+'\n','**Search batches:** '+', '.join(m['batches'])+'. **Opened reference keys:** '+', '.join(m['refs'])+'.\n','**Result and limit:** '+m['result']+'\n']
out+=['## Exact calls, returned sources and assessed results\n']
for n,req,body,headers in loaded:
 out+=['### Batch '+str(n)+'\n',B.get(n,'See the preserved request and scoped reference records.')+'\n','```json\n'+json.dumps(req,ensure_ascii=False,indent=2)+'\n```\n']
 if headers:
  out+=['Returned source records (titles and URLs; presence here alone does not certify opening or proof):\n']
  for title,url,ref in headers: out+=['- '+title+' — '+url+'; retrieval ID `'+ref+'`.\n']
 if any(s in body for s in ['Failed to fetch','403 Forbidden','Content length is too large','Internal Error']):
  out+=['Access failure occurred in this batch. The full diagnostic is preserved in the local raw record. No failed URL is represented as a checked theorem.\n']
out+=['## Direct PDF fetches and visual inspection\n',
'`fetch_primary.py` and `fetch_primary.out` record the successful public SGA7I download, HTTP status, byte length and SHA-256. The original PDF was read at IX7.1.5–7.2.6, printed pp402–407, and adjacent construction pages. `read_log.md` records the exact page ranges. The full copyrighted book and extracted page images remain in the excluded reference cache.\n',
'The original SGA4I PDF was supplied locally by root. This reviewer opened its URL in batch31, which the web parser rejected for size, then read the local page images at I8.13.2–4 pp136–138 and8.3.2–3 pp75–76. The trial OCR on PDF90 hung and was interrupted; no OCR text was used. Exact conclusions are in `SGA4_8133_check.md`.\n',
'`fetch_egai.py` records an additional attempt to retrieve the original EGAI PDF after the web parser size failure. Its actual completion/failure is in `fetch_egai.out`; the bibliography and reading alert are updated only if the exact original proposition is subsequently read.\n',
'Cross-package later Bertini and curve-extension endpoints were read directly as recorded in `read_log.md`; root owns their claim rows. Absent Hua, LM1, S6, RESULTS_STATE and other project documents were not searched as though their assertions were established mathematics. Their presence in earlier notes is an attributed lead only.\n']
(P/'search_log.md').write_text('\n'.join(out))
print(json.dumps(dict(claims=len(mapping),batches=len(loaded),calls=len(calls),returned_source_records=len(results)),indent=2))
