"""Add only the recovered Deligne hard-Lefschetz deferred-proof request.

The manual source and exact primary-page comparisons are recorded here. The
historical sentence does not contain the modern theorem's hypotheses. No scan
is emended and no additional research direction is generated.
"""
from pathlib import Path
import csv,json,hashlib

P=Path(__file__).resolve().parent
W=P.parents[1]
DATE='2026-11-19'
CID='C-SA23-ega-098';IID='SA23-1321';PID='MP-SA23-ega-60'
SOURCE='sources/texts/codex/K23-03_transcription.tex'
WORDS=(W.parent/SOURCE).read_text().splitlines()[235]
REFS=['EGA_KatzSGA7XVIII1973','EGA_DeligneWeilII1980']
MODERN=('The historical sentence requests a proof of the named theorem without specifying a base field, coefficients or smoothness/projectivity hypotheses. '
        'The exact terminology in SGA7 XVIII5.2.2 identifies the standard hard-Lefschetz interpretation: for X smooth projective of pure dimension n over an algebraically closed field k, '
        'an ample invertible sheaf L, and a prime l different from char(k), cup product with c1(L)^i gives an isomorphism '
        'H^(n-i)(X,Q_l) -> H^(n+i)(X,Q_l(i)) for every i>=0. This precise statement is the later matched theorem, not a transcription of hypotheses from the letter.')
FATE=('SGA7II XVIII5.2.2 and5.2.2.1, printed pp281–282, use exactly the name Lefschetz vache for the cup-product isomorphisms and still conjecture the smooth case. '
      'The exposé is by N.Katz, expressly based on succinct Grothendieck notes (printed p254). '
      'Deligne, La conjecture de Weil II, Theorem4.1.1 and proof4.1.2–4.1.4, printed pp217–218, establish the stated smooth-projective Q_l theorem. '
      'The letter is dated17October1966; SGA7II was published1973; WeilII was received1June1979 and published in volume52(1980), with Numdam catalogue date28December1980. '
      'No exact first-circulation date is established. ClassB records establishment by another author relative to Grothendieck: Pierre Deligne, who also wrote the attached letter. Neither letter nor theorem is attributed to Grothendieck.')

def load(name):return json.loads((P/name).read_text())
def dump(name,x):(P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def upsert(rows,rec,key='id'):
    return [x for x in rows if x[key]!=rec[key]]+[rec]

claim={
 'id':CID,'title':'Deligne’s deferred proof request for the théorème de Lefschetz vache',
 'source':SOURCE,'cote':'23','scans':'60','lines':'230–236','items':[IID],
 'author':'Pierre Deligne; letter to A.Grothendieck dated17October1966',
 'his_words':WORDS,'his_statement':WORDS,'statement':MODERN,'modern_statement':MODERN,
 'status_on_pages':'explicit proof request deferred for that year; no proof or theorem hypotheses supplied',
 'page_status':'explicit proof request deferred for that year; no proof or theorem hypotheses supplied',
 'status_category':'open on the pages','record_origin':'source question or deferred mathematical step',
 'verification_origin':'Present-run exact terminology and primary theorem comparison; not a new proof of hard Lefschetz and not an assertion that the letter states the modern quantifiers.',
 'computation':{'kind':'no manuscript computation to redo; exact source and theorem comparison','code':None,'output':None,'certificate_search_labels':[],
                'proof':'parts/ega/proof_notes.md, section Recovered Deligne hard-Lefschetz request'},
 'class':'B','classification':'B','fate':FATE,'literature_fate':FATE,
 'fate_date':'Source letter1966-10-17; SGA7II publication1973; WeilII received1979-06-01, publication1980 (Numdam catalogue1980-12-28); first circulation not established',
 'present_status':('As of19November2026, the exact smooth-projective rational l-adic interpretation is established by Deligne’s theorem. '
                   'The historical line has no more detailed quantifiers, and no integral-coefficient, nonprojective or standard-conjecture extension is attributed to it.'),
 'present_check':('The source line and its date were reread. SGA7II physical pages260,287–288 and WeilII physical pages82–83 were visually inspected. '
                  'WeilII factors the cup product through a hyperplane section, identifies the middle image with monodromy invariants, and uses complete reducibility plus its elementary invariant-pairing lemma. '
                  'Those cited global inputs are accepted as the published proof; they are not reproved by this bounded check.'),
 'refs':REFS,'references':REFS,'confidence':'medium',
 'confidence_detail':'High for the named-theorem identification; medium for reconstructing the unexpressed scope of the1966 request.',
 'source_scope_limit':'Only the name and the deferred proof request occur in the historical sentence. Modern quantifiers are separately stated from the checked publications.',
 'source_quotation_status':'The transcription offers Lefschetz/Lefchetz as a spelling alternative; the name vache and the deferred request are unambiguous.'
}
item={'id':IID,'sources':[],'kind':'other','subkind':'additional Codex subject; recovered explicit deferred proof request; no Stage1 entry',
      'cote':['23'],'scans':['60'],'lines':[SOURCE+':230–236'],'additional_sources':[SOURCE],
      'his_words':WORDS,'statement':'Deligne’s17October1966 deferred hard-Lefschetz proof request',
      'reconstruction':'Distinct from the local parafactorial/Lefschetz margin assertions. Exact named-theorem identification is supported by SGA7XVIII; the letter itself supplies no theorem hypotheses.',
      'claims':[CID],'check':'agrees','check_reason':'Recovered from a previously fully read source and confirmed by a targeted logged reread; no indexed-note verdict or fabricated occurrence is created.'}
problem={'id':PID,'title':'Deligne’s deferred hard-Lefschetz proof request','claims':[CID],
 'occurrences':[{'source':SOURCE,'cote':'23','scan':'60','line':'230–236'}],
 'as_he_states':'In his letter of17October1966, Deligne says he will not attempt to prove the named théorème de Lefschetz vache that year and hopes Grothendieck finds someone who will. The sentence supplies no further hypotheses.',
 'plausible_today':MODERN,'state_of_art':FATE,
 'why_open':'The source explicitly defers Deligne’s attempt for that year and asks that someone else undertake it. It states no mathematical reason for the deferral; the subsequent mention of convalescent EGA reading is not treated as a causal explanation.',
 'worth':'Worth retaining as a dated historical request with a later exact theorem match; the standard smooth-projective Q_l theorem is settled and does not warrant a new proof task here.',
 'refs':REFS,'date':DATE,'record_type':'authorial mathematical problem','origin':'authorial explicit deferred mathematical proof step',
 'origin_class':'explicit authorial proof request','count_as_authorial_mathematical_problem':True,
 'source_cue':WORDS,
 'source_cue_locations':[{'source':SOURCE,'lines':'230–236'}],
 'source_cue_literal':[WORDS],'source_scope_limit':claim['source_scope_limit'],
 'historical_explanation_limit':'No reason for later omission or abandonment is inferred from the surrounding letter.',
 'source_author':'Pierre Deligne','source_date':'1966-10-17'}

dump('claims.json',upsert(load('claims.json'),claim))
dump('items.json',upsert(load('items.json'),item))
dump('problems.json',upsert(load('problems.json'),problem))
categories=load('status_categories.json');categories[CID]='open on the pages';dump('status_categories.json',categories)

bibliography=[
 {'key':REFS[0],'kind':'incollection','author':'Nicholas Katz','title':'Étude cohomologique des pinceaux de Lefschetz, SGA7II, ExposéXVIII',
  'booktitle':'Groupes de monodromie en géométrie algébrique, II','series':'Lecture Notes in Mathematics','volume':'340','publisher':'Springer','year':'1973','pages':'254--327',
  'url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf','note':'verified',
  'annote':'Original PDF visually inspected19November2026: author/notes credit printedp254, definition and conjectureXVIII5.2.2–5.2.2.1 pp281–282 (physical260,287–288). Katz is printed author, based on succinct Grothendieck notes. The exact name Lefschetz vache matches Deligne’s1966 phrase; the publication does not prove that the letter intended every later stated hypothesis. Publication1973; exact first circulation not established.'},
 {'key':REFS[1],'kind':'article','author':'Pierre Deligne','title':'La conjecture de Weil : II','journal':'Publications Mathématiques de l’IHÉS','volume':'52','year':'1980','pages':'137--252',
  'doi':'10.1007/BF02684780','url':'https://www.numdam.org/item/PMIHES_1980__52__137_0/','note':'verified',
  'annote':'Metadata opened and original PDF visually inspected19November2026. Theorem4.1.1 and proof4.1.2–4.1.4, printedpp217–218 (physical82–83), give smooth projective pure-dimensional hard Lefschetz for an ample class over an algebraically closed field and Q_l coefficients, l different from the characteristic; Tate twists are suppressed after a chosen trivialization. Received1June1979; volume publication1980; Numdam catalogue date28December1980. These are not established first-circulation dates. Global weight/semisimplicity inputs were not reproved in this run.'},
]
bibs=load('bibliography_records.json')
for b in bibliography:bibs=upsert(bibs,b,'key')
dump('bibliography_records.json',bibs)
def brace(s):return str(s).replace('{','\\{').replace('}','\\}')
(P/'references.bib').write_text('\n'.join('@'+b.get('kind','misc')+'{'+b['key']+',\n'+',\n'.join('  '+k+' = {'+brace(v)+'}' for k,v in b.items() if k not in ['key','kind'])+'\n}\n' for b in bibs))

def tab(name):return list(csv.DictReader((P/name).open(),delimiter='\t'))
def write_tab(name,fields,rows):
    with (P/name).open('w') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(rows)
links=tab('links.tsv');fields=list(links[0]);links=[x for x in links if x['from']!=CID]
links.extend([
 {'kind':'published work','from':CID,'to':REFS[0]+' XVIII5.2.2–5.2.2.1, pp281–282','what':'Exact named-theorem and conjectural-scope correspondence','evidence':'Original PDF author page254 and theorem-definition pages281–282 visually read; historical sentence supplies name only.','note_ids':''},
 {'kind':'published work','from':CID,'to':REFS[1]+' Theorem4.1.1, pp217–218','what':'Later theorem by the source author Deligne for the precise smooth-projective Q_l interpretation','evidence':'Original PDF physical82–83 visually read; exact base, pure dimension, ample class and rational coefficient hypotheses retained.','note_ids':''},
])
write_tab('links.tsv',fields,links)

events=tab('check_events.tsv');fields=list(events[0]);tag='Recovered Deligne hard-Lefschetz request:'
events=[e for e in events if not e['outcome'].startswith(tag)]
def event(ident,kind,outcome):
    events.append({'statement_id':ident,'date':DATE,'who':'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega','type':kind,'outcome':tag+' '+outcome})
event(IID,'text concordance and subject consolidation','K23-03 physical lines230–236, scan60, read with the17October1966 date; separate additional subject, no indexed note entry.')
event(CID,'source and literature hypothesis comparison','Exact named-theorem match with SGA7XVIII5.2; WeilII4.1.1 hypotheses and proof route read. Historical wording and modern reconstruction remain separate; no independent proof of hard Lefschetz claimed.')
event(PID,'source provenance audit','The literal future-year deferral and request for another prover make this an authorial mathematical step. No mathematical cause of deferral is inferred.')
event(REFS[0],'primary source opened and inspected','OriginalPDF printed254,281–282 visually inspected; Katz authorship and Grothendieck-notes credit retained;1973 publication distinguished from unspecified first circulation.')
event(REFS[1],'primary source opened and inspected','Numdam metadata and originalPDF printed217–218 visually inspected;1979receipt and1980publication recorded separately; proof depends on published global inputs not redone here.')
write_tab('check_events.tsv',fields,events)

log=[json.loads(s) for s in (P/'search_log.jsonl').read_text().splitlines()]
newlog=[
 {'id':'S-ega-LV-001','date':DATE,'commands':{'system2_search_query':[{'q':'"Deligne" "Lefschetz vache"'},{'q':'"théorème de Lefschetz vache"'}]},'claim_ids':[CID],
  'urls':['https://grothendiecksga.com/read/sga7/fr/18-5.html','https://grothendiecksga.com/read/sga7/fr/18-introduction.html'],
  'match_and_limit':'Exact phrase located in SGA7XVIII5.2.2. Secondary encyclopedia/blog results were not used as mathematical evidence. Online transcription was checked against originalPDF pages281–282.'},
 {'id':'S-ega-LV-002','date':DATE,'commands':{'system1_search_query':[{'q':'Deligne La conjecture de Weil II 4.1.1 Lefschetz 1980 site:numdam.org'},{'q':'"Lefschetz vache" "5.2.2" SGA 7'}]},'claim_ids':[CID],
  'urls':['https://www.numdam.org/item/PMIHES_1980__52__137_0/','https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf','https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf'],
  'match_and_limit':'Opened Numdam metadata. WebPDF open failed because13.5MB exceeds service limit, then local originalPDF was downloaded and inspected. Theorem4.1.1 on printed217 and proof through4.1.4 on218 match the stated Q_l interpretation; no integral-coefficient or nonprojective extension is attributed to the letter. The archive.numdam.org DOI landing page returned502; the www.numdam.org item page succeeded.'},
 {'id':'FATE-'+CID,'date':DATE,'claim_id':CID,'search_operations':['S-ega-LV-001','S-ega-LV-002'],
  'exact_hypotheses':'Letter names theorem only. Matched standard interpretation: smooth projective pure dimension n over algebraically closed k; ample L; rational l-adic coefficients with l != char(k).',
  'opened_sources':[{'url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf','locator':'XVIII5.2.2–5.2.2.1 pp281–282; author creditp254','what_matched':'Exact name and cup-product definition; smooth case conjectural in this publication.'},
                    {'url':'https://www.numdam.org/item/PMIHES_1980__52__137_0/','locator':'metadata; originalPDF Theorem4.1.1/proof4.1.2–4.1.4 pp217–218','what_matched':'Later established theorem, source authorDeligne, exact coefficients and geometry.'}],
  'fate':FATE,'limit':'The letter does not state the modern quantifiers; first circulation is not established. No broader standard conjecture is manufactured from its short name.'}
]
newids={r['id'] for r in newlog};log=[r for r in log if r.get('id') not in newids]+newlog
(P/'search_log.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in log))

heading='## Recovered Deligne hard-Lefschetz request'
proof='''\n## Recovered Deligne hard-Lefschetz request\n\nK23-03:230–236 is Deligne’s letter of17October1966. The author defers a proof of the named theorem and hopes another person undertakes it; no proof, computation or detailed hypotheses occur there. The name is identified by SGA7IIXVIII5.2.2–5.2.2.1, printedpp281–282. The author page254 says N.Katz, based on succinct Grothendieck notes. The definition concerns powers of an ample hyperplane class on rational l-adic cohomology; the smooth case is still conjectural there.\n\nDeligne’s1980WeilII4.1.1, printedp217, states the smooth projective pure-dimensional ample-class theorem over an algebraically closed field with l different from its characteristic. The text suppresses Tate twists after choosing a trivialization. Pages217–218 reduce to the nondegeneracy of the intersection pairing on the image of a smooth hyperplane section, identify that image with monodromy invariants, and invoke complete reducibility. The elementary4.1.4 step is checked as follows: split a semisimple representation V as V^pi plus a complement W with no trivial quotient. Invariance forces W to be orthogonal to V^pi, so nondegeneracy on V forces nondegeneracy on V^pi. This verifies that local linear-algebra step only; the global weights/semisimplicity and invariant-cycle inputs are published dependencies, not reproved here.\n\nThe exact source request and the modern theorem are different evidence layers. No integral-coefficient, nonprojective or standard-conjecture extension is inferred. There is no source calculation requiring numerical code, and no new finite certificate is fabricated. Primary locators: EGA_KatzSGA7XVIII1973; EGA_DeligneWeilII1980.\n'''
p=P/'proof_notes.md';s=p.read_text()
if heading in s:s=s[:s.index(heading)].rstrip()+'\n'
p.write_text(s+proof)

cache_paths=[W/'external/SGA7II.pdf',P/'external/Deligne_WeilII_1980.pdf']
dump('lefschetz_request_check.json',{'source':SOURCE,'lines':'230–236','source_date':'1966-10-17','item':IID,'claim':CID,'problem':PID,
 'primary_checks':[{'key':REFS[0],'printed_pages':[254,281,282],'physical_pages':[260,287,288],'status':'visually inspected'},
                   {'key':REFS[1],'printed_pages':[217,218],'physical_pages':[82,83],'status':'visually inspected; proof route and exact hypotheses checked'}],
 'external_cache_excluded_from_zip':[{'path':str(p.relative_to(W)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in cache_paths],
 'no_new_source_computation':True,'no_new_direction':True,'classification_note':'B: established by another author relative to Grothendieck, namely Deligne, also author of the attached letter. Neither letter nor theorem is attributed to Grothendieck.'})
print(json.dumps({'item':IID,'claim':CID,'problem':PID,'bibliography':REFS,'claims':len(load('claims.json')),'items':len(load('items.json')),'problems_before_origin_overlay':len(load('problems.json')),'links':len(links)},indent=2))
