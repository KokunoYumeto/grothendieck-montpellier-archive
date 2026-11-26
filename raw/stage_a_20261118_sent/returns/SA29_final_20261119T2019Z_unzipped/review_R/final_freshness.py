"""Apply the final source-read November 2026 literature comparison.

These are explicitly authored additions from opened primary statements, not
inferences from search headings. Safe to repeat after the earlier serializers.
"""
from pathlib import Path
import csv,json
O=Path(__file__).resolve().parent
KEY='BasualdoBonattoRobertson2026'
DATE='2026-11-19'
URL='https://arxiv.org/html/2606.01466v2'
WHO='GPT-6 Astra Pro; effort not independently observable; SA29 part2 final literature check'
def load(name):return json.loads((O/name).read_text())
def save(name,value):(O/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def append_once(text,suffix):return text if suffix in text else text+' '+suffix
claims=load('claims.json')
additions={
 'C-SA29-333':'BasualdoBonattoRobertson2026, v2 Theorem4.9 p41 and Proposition6.14 p57, supplies a faithful Nakamura–Schneps subgroup action on the completed surface modular operad and its profinite homotopy1-type tower. Proposition6.22 p61 compares that tower with the full étale homotopy model only after genus≤1 truncation. This gives a further framework, not the missing dictionary for these particular paths.',
 'C-SA29-334':'The additional 2026 modular-operad comparison is scoped in C-SA29-333 and audit/BBR2026_report.md; it does not identify this manuscript subdivision.',
 'C-SA29-340':'The additional 2026 modular-operad presentation is a later comparison framework (C-SA29-333); it does not supply the author’s blank table entries.'}
for c in claims:
 if c['id']in additions:
  c['fate']=append_once(c['fate'],additions[c['id']])
  if KEY not in c['refs']:c['refs'].append(KEY)
  c['fate_date']['additional_comparator']='First arXiv submission2026-05-31; v2 submission2026-10-08; opened PDF internal date2026-10-12. No earlier circulation or journal publication established.'
save('claims.json',claims)
problems=load('problems.json')
for p in problems:
 if p['id']in ['MP-SA29-105','MP-SA29-109']:
  suffix='The 2026 preprint BasualdoBonattoRobertson2026 adds the scoped modular-operad results recorded in C-SA29-333: v2 Theorem4.9 p41, Proposition6.14 p57, and genus≤1 comparison in Proposition6.22 p61. It does not identify these manuscript configurations.'
  p['state_of_art']=append_once(p['state_of_art'],suffix)
  if KEY not in p['refs']:p['refs'].append(KEY)
save('problems.json',problems)
checks=load('reference_checks.json')
checks=[c for c in checks if c['key']!=KEY]
checks.append(dict(key=KEY,type='misc',author='Luciana Basualdo Bonatto and Marcy Robertson',title='Galois actions on surfaces and a higher genus Grothendieck–Teichmüller group',year='2026',url=URL,
 locator='v2 Theorem4.9 p41; Proposition6.14 p57; Lemma6.17 pp59–60; Proposition6.22 p61; Corollary6.23 p62',
 verified='Primary arXiv version history, PDF and HTML opened. Exact statements and hypotheses read; no independent re-proof of the paper. NS subgroup is not silently replaced by full GT; higher-genus homotopy1-types are not identified with the full étale homotopy model.',
 tool_ref='Root:turn689082020view0;turn314806728view0;turn314806728view1;turn314806728view2;turn314806728view3. Full bounded report:audit/BBR2026_report.md'))
save('reference_checks.json',checks)
bib=O/'references.bib'
if '@misc{'+KEY+',' not in bib.read_text():
 with bib.open('a')as f:f.write('''
@misc{BasualdoBonattoRobertson2026,
  author = {Basualdo Bonatto, Luciana and Robertson, Marcy},
  title = {Galois actions on surfaces and a higher genus Grothendieck--Teichm{\\\"u}ller group},
  year = {2026},
  howpublished = {arXiv:2606.01466v2, preprint},
  doi = {10.48550/arXiv.2606.01466},
  url = {https://arxiv.org/html/2606.01466v2},
  annote = {First arXiv submission31 May2026; v2 submission8 October2026; PDF internal date12 October2026. Submission dates do not establish earlier circulation. No journal publication verified.},
  note = {verified}
}
''')
def read_tsv(name):
 with(O/name).open(newline='')as f:return list(csv.DictReader(f,delimiter='\t'))
def write_tsv(name,rows,fields):
 with(O/name).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
queries=[
 ('C-SA29-33','"congruence subgroup" "mapping class" 2026','web_33.json','Refreshed the checked Boggi2026 primary comparator; quotient/CSP restrictions retained.'),
 ('C-SA29-311;C-SA29-333','"Grothendieck Teichmuller" "2026" "Lochak" "Nakamura" "Schneps"','web_33.json','No broader conclusion substituted for the already opened full-profinite action theorem and its stated compatibility limits.'),
 ('C-SA29-333;C-SA29-334;C-SA29-340','"2606.01466" Grothendieck','web_33.json','Located the new modular-operad preprint; the later primary openings supersede initial inaccessible endpoints.'),
 ('C-SA29-333;C-SA29-334;C-SA29-340','"Basualdo Bonatto" "Robertson" "Galois actions on surfaces" pdf','web_34.json','Search led to a primary repository and author-page route; actual arXiv v2 statements subsequently opened.'),
 ('C-SA29-333;C-SA29-334;C-SA29-340','open arXiv2606.01466; find Theorem4.9, Proposition6.14, Lemma6.17, Proposition6.22 in v2','web_36.json;web_37.json','Exact groupoid/monoid action and genus≤1 comparison checked; no manuscript move dictionary inferred.')]
rows=[r for r in read_tsv('search_log.tsv') if r['source']!='Final November2026 primary-source check']
for ids,q,receipt,result in queries:
 opened_url={'C-SA29-33':'https://link.springer.com/article/10.1007/s40863-026-00558-y','C-SA29-311;C-SA29-333':'https://arxiv.org/abs/2602.12462'}.get(ids,URL)
 row=dict(claim_ids=ids,source='Final November2026 primary-source check',query=q,opened_url=opened_url+'; root receipts '+receipt,result=result,exact_match='Scoped modern comparator only; literal manuscript status and claim class unchanged.')
 if row not in rows:rows.append(row)
write_tsv('search_log.tsv',rows,['claim_ids','source','query','opened_url','result','exact_match'])
events=read_tsv('CHECK_EVENTS.tsv')
for sid in [KEY,*additions,'MP-SA29-105','MP-SA29-109']:
 row=dict(statement_id=sid,date=DATE,who=WHO,type='used and rechecked in this run',outcome='Final primary-source comparison: '+KEY+' v2 exact theorem statements and hypotheses read; see audit/BBR2026_report.md. No independent re-proof and no identification of the manuscript’s missing local paths or incidence data.')
 if row not in events:events.append(row)
write_tsv('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
out={'claim_additions':list(additions),'problem_additions':['MP-SA29-105','MP-SA29-109'],'reference_added':KEY,'search_rows_added':len(queries),'event_rows_added':6,'scope':'Manuscript classes/statuses unchanged; first-submission, revision and internal PDF dates distinct.'}
save('final_freshness_output.json',out)
print(json.dumps(out,ensure_ascii=False,indent=2))
