#!/usr/bin/env python3
"""Serialize actual supplementary searches and manually checked source scopes."""
from pathlib import Path
import csv,json,datetime
W=Path('/workspace/scratch/26604d0a9a98/work/cotes6_7')
date=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; SA15-20261119/cotes6_7'
def tsv(name,rows,fields):
 with (W/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
queries=[]
files=[f'sga_search_{n}.json' for n in range(1,5)]+['sga_search5.json','sga_search6.json']
for i,name in enumerate(files,1):
 d=json.loads((W/'outputs'/name).read_text());q=d['query']
 engine='system1' if 'system1_search_query' in q else 'system2'
 for j,x in enumerate(q.get('system1_search_query',q.get('system2_search_query',[])),1):
  channel='general exact-claim / primary-source discovery'
  for a,b in [('zbmath','zbMATH'),('arxiv','arXiv'),('numdam','Numdam'),('mathoverflow','MathOverflow')]:
   if a in x['q']:channel=b+' via search';break
  queries.append(dict(query_id=f'R67-SGA-Q{i}.{j}',statement_id='SGA7-IX-5.13.1' if i<6 else 'Breuil2000 bibliographic identity',query=x['q'],channel=channel,engine=engine,result_file='outputs/'+name,outcome='No exact subsequent resolution of the full remark identified; checked theorem ingredients and limitations are described in sga7_pcase_audit.md.' if i<6 else 'Official journal record resolves volume152 against author-bibliography typo151.'))
tsv('sga7_query_log.tsv',queries,['query_id','statement_id','query','channel','engine','result_file','outcome'])
refs=[
 dict(key='Breuil2000',type='article',fields=dict(author='Christophe Breuil',title='Groupes p-divisibles, groupes finis et modules filtrés',journal='Annals of Mathematics',volume='152',number='2',year='2000',pages='489--549',doi='10.2307/2661391',eprint='math/0009252',archivePrefix='arXiv',url='https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/p-divisibles.pdf'),scope='Author full PDF Theorem5.3.2, Corollaries5.3.3–5.3.4 and proof read. p>2, k⊂Fbar_p retained. Primary journal metadata checked independently. This theorem is an ingredient, not a literal answer to SGA7 IX5.13.1.'),
 dict(key='Fontaine1994VIII',type='article',fields=dict(author='Jean-Marc Fontaine',title='Exposé VIII: Représentations ℓ-adiques potentiellement semi-stables',journal='Astérisque',volume='223',year='1994',pages='321--347',publisher='Société mathématique de France',url='https://www.numdam.org/item/AST_1994__223__321_0.pdf'),scope='Introduction hypotheses,2.1.3,2.3.2–2.3.4 read. Exactness and inertia/monodromy criteria used in an explicitly original deduction; no claim this paper states the filtration-length question.'),
 dict(key='Raynaud1974',type='article',fields=dict(author='Michel Raynaud',title='Schémas en groupes de type (p,...,p)',journal='Bulletin de la Société Mathématique de France',volume='102',year='1974',pages='241--280',url='https://www.numdam.org/article/BSMF_1974__102__241_0.pdf'),scope='§2.1 pp259–260 and Proposition2.3.1 with proof pp261–263 read: finite-flat subquotients and levelwise extension criterion in mixed characteristic.')]
for r in refs:r['fields']['note']='verified'
with (W/'sga7_references.bib').open('w') as f:
 for r in refs:
  f.write('@'+r['type']+'{'+r['key']+',\n')
  for k,v in r['fields'].items():f.write('  '+k+' = {'+v+'},\n')
  f.write('}\n\n')
evidence=[
 dict(key='SGA7-IX-5.13.1',url='https://grothendiecksga.com/read/sga7/fr/9-5.html',locator='5.11–5.13.1; emphasis on5.12,5.12.1,5.13(c),5.13.1',result='Opened original French rekeyed text; all hypotheses read. Exact length question distinct from abelian semistable reduction.',tool_ref='turn320701669view0',evidence_file='outputs/sga7_IX5.txt'),
 dict(key='Breuil2000',url=refs[0]['fields']['url'],locator='Author version pp51–52, Theorem5.3.2, Corollaries5.3.3–5.3.4 and proof; bibliography[Ra]',result=refs[0]['scope'],tool_ref='turn300209304view0',evidence_file='outputs/sga_open4.json'),
 dict(key='Breuil2000',url='https://annals.math.princeton.edu/articles/11849',locator='Official article header and DOI',result='Volume152,issue2,2000,pp489–549,DOI10.2307/2661391 verified. Author page volume151 conflicts and is rejected.',tool_ref='turn556827728view0',evidence_file='outputs/sga_open9.json'),
 dict(key='Breuil2000',url='https://arxiv.org/abs/math/0009252',locator='Abstract, journal reference and version history',result='First submission1September2000; published-version metadata152(2)489–549; exact p>2 and residue-field restriction confirmed.',tool_ref='turn914197975view0',evidence_file='outputs/sga_open8.json'),
 dict(key='Fontaine1994VIII',url=refs[1]['fields']['url'],locator='Introduction;2.1.3;2.3.2–2.3.4, especiallyp337',result=refs[1]['scope'],tool_ref='turn739425594view0;turn894287221view1;turn953663428view1',evidence_file='outputs/sga_open3.json;outputs/sga_find2.json;outputs/sga_open7.json'),
 dict(key='Raynaud1974',url=refs[2]['fields']['url'],locator='§2.1 pp259–260;Prop2.3.1 pp261–263',result=refs[2]['scope'],tool_ref='turn953663428view0;turn894287221view0',evidence_file='outputs/sga_open7.json;outputs/sga_find2.json'),
 dict(key='BrinonConrad2009',url='https://math.stanford.edu/~conrad/papers/notes.pdf',locator='Theorem5.2.1;Proposition9.3.1 and Corollary9.3.2',result='Auxiliary exactness and inertial base-change explanation read; final deduction instead cites Fontaine original.',tool_ref='turn739425594view1;turn723263948view3',evidence_file='outputs/sga_open3.json;outputs/sga_find1.json'),
 dict(key='ConradKisinSurvey',url='https://math.stanford.edu/~conrad/papers/luminy.pdf',locator='Theorem4.3.2 pp42–43, proof and following discussion',result='p>2 equivalence and connected p=2 limitation read. Not used to assert a complete arbitrary p=2 result.',tool_ref='turn739425594view2',evidence_file='outputs/sga_open3.json'),
 dict(key='MO191643',url='https://mathoverflow.net/questions/191643/the-generic-fiber-pullback-for-p-divisible-groups-in-characteristic-p',locator='Question and answer citing deJong1998',result='Opened adjacent full-faithfulness lead; it does not settle filtration-length descent and is not entered as a positive resolution.',tool_ref='turn320701669view1',evidence_file='outputs/sga_open1.json'),
 dict(key='Grothendieck1966',url='https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf',locator='p102;PDFpage8;lines340–365',result='Published abelian Hodge-extension/finite-p-torsion paragraph independently read for root noteE.27. Unavailable cote54 not identified.',tool_ref='turn311853704view0',evidence_file='outputs/sga_open5.json')]
(W/'sga7_reference_evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
events=[
 dict(statement_id='P78-C035',date=date,who=who,type='used and rechecked in this run',outcome='Read5.12–5.13.1 and adjacent hypotheses; arbitrary BT/strict filtration/length bound distinguished from abelian5.13(c).'),
 dict(statement_id='P78-C071',date=date,who=who,type='targeted proof check',outcome='Read Fontaine2.1.3/2.3.2–4, Breuil5.3.2 and5.3.4proof, Raynaud§2.1/2.3.1; exact hypotheses compared. Full original classification proofs not independently reproved.'),
 dict(statement_id='P78-C071',date=date,who=who,type='independent re-proof',outcome='Present-run descent lemma, sum-of-conjugates induction and saturated-lattice recovery written in sga7_pcase_audit.md. Proves only finite K/Q_p and p>2 integrally; rational crystalline-filtration proof works every p. Not attributed to a literal later theorem.'),
 dict(statement_id='Grothendieck1966',date=date,who=who,type='used and rechecked in this run',outcome='Exact p102 paragraph independently opened for rootE.27; published bibliographic endpoint confirmed. Cote54 absent; Oda endpoint belongs to root verification, not rechecked here.')]
tsv('sga7_check_events.tsv',events,['statement_id','date','who','type','outcome'])
claim=dict(id='P78-C071',items=['P78-I036'],cote=['8'],scans=['8:032'],lines=['SA15_texts/pro/MPL_7_061-072+8_001-078_transcription.tex:1416–1426'],his_statement='bonne réduction virtuelle d’échelon n (parent question; the restricted theorem below is not attributed to the manuscript)',statement='Let K be a finite extension of Q_p with p>2 and X a p-divisible group over K. Suppose X has a finite filtration by strict p-divisible subgroups whose graded groups extend over O_K. If, after a finite extension L/K, X_L admits such a filtration with at most n nonzero graded groups, then X already admits such a filtration with at most n over K.',status_on_pages='present-run refinement of the open p-case question P78-C035; no proof or finite-local-field restriction is attributed to the page',computation='Complete non-computational proof in sga7_pcase_audit.md: finite unipotent inertia on D_pst gives the potentially-crystalline descent lemma; summing Galois conjugates of a first crystalline layer and induction descends the length; saturated intersections with the specified Tate lattice and Raynaud finite-flat subquotients/levelwise extension recover strict integral BT filtrations.',**{'class':'B'},fate='Present-run deduction from Fontaine1994VIII2.1.3/2.3.2–4, Breuil2000 Theorem5.3.2 and Corollary5.3.4 proof, Raynaud1974§2.1/Proposition2.3.1. These established later results supply the exact ingredients. No opened paper is claimed to state the full filtration-length descent assertion literally.',fate_date={'ingredient_publications':['1974','1994','2000'],'breuil_first_arxiv':'2000-09-01','present_run_deduction':'2026-11-19'},present_status='As of2026-11-19: proved here for finite K/Q_p and p>2. The rational crystalline-filtration assertion is proved for every p. Integral p=2 and unrestricted henselian traits are not certified by this audit. No exact subsequent resolution of SGA7IX5.13.1 in full generality was identified; this documentary residual is not a claim of modern openness.',refs=['Fontaine1994VIII','Breuil2000','Raynaud1974'],confidence='high',search_family='VGR',search_history=[q['query_id'] for q in queries],origin='present-run refinement',parent='P78-C035',proof_origin='SA15-20261119/cotes6_7; independently reviewed by root in this run; not an additional manuscript claim',source_status='Root checked the manuscript source; this agent independently checked the published SGA7 formulation and primary theorem ingredients.')
(W/'supplementary_root_claims.json').write_text(json.dumps([claim],ensure_ascii=False,indent=2)+'\n')
tsv('supplementary_root_search_by_claim.tsv',[dict(claim_id=claim['id'],origin=claim['origin'],families='VGR',query_ids=';'.join(claim['search_history']),opened_reference_keys=';'.join(claim['refs']),exact_match_or_limit=claim['fate'])],['claim_id','origin','families','query_ids','opened_reference_keys','exact_match_or_limit'])
ref_supp=[]
for r in refs:
 fields=dict(r['fields']);fields['note']='verified'
 ev=[dict(url_opened=e['url'],locator=e['locator'],read_scope=e['result'],tool_reference=e['tool_ref'],date='2026-11-19',evidence_file=e['evidence_file']) for e in evidence if e['key']==r['key']]
 ref_supp.append(dict(key=r['key'],type=r['type'],fields=fields,evidence=ev,limits=r['scope']))
(W/'reference_supplement.json').write_text(json.dumps(ref_supp,ensure_ascii=False,indent=2)+'\n')
out=dict(query_rows=len(queries),additional_verified_reference_identities=len(refs),check_events=len(events),root_link_rows=1,full_remark_literary_resolution='not identified; no assertion of modern openness',proved_special_case='finite K/Q_p, p>2; integral strict BT filtration length descends')
(W/'outputs/build_sga_audit_output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False))
