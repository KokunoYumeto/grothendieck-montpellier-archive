"""Serialize the final hand-reviewed source, research and verification audit.
This program joins manually written assessments; it does not infer correctness.
Run after build_indices.py and computations/check_misc.py.
"""
import csv,json,re
from collections import Counter
from pathlib import Path
from build_problems import claims,problems,OUT,write
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner misc'

def update(n,refs=None,fate=None):
    a=claims[n-1]
    if refs:a['refs']=list(dict.fromkeys(a['refs']+refs))
    if fate:a['fate']=fate

update(13,['QiaochuYuan2017'],'QiaochuYuan2017, section In characteristic zero, explicitly proves the arbitrary-module classification over a Q-algebra by locally nilpotent endomorphisms, including polynomial translations. Milne2017 Theorem4.8 is the field-valued rational-representation framework. Neither permits a uniform exponent for arbitrary M.')
for n in [11,12,14,15,16,17,18,19,39]: update(n,['QiaochuYuan2017'])
update(23,['Zhao2017'],'Zhao2017, checked v2 dated10August2022, Corollary2.4 printedp7 gives m!(Da)^m=0 for D^m=0. OverQ, polarization gives the ideal power bound. The identification of this ideal with the automorphism difference ideal and the commutator deduction are supplied here. Necessity is false, as C-SA23-misc-025 shows. The corresponding exact result in the2017 first version was not inspected.')
update(20,['MathlibPolynomialNilpotent'])
for n in range(30,37): update(n,['Freed2013'])
update(32,fate='Freed2013 Exercises2.6 and2.9, equations2.7 and2.11, pp15–16 give the determinant-sign orientation torsor and exact-sequence model, with quotient-before-subspace order. The exact archival axioms and existence/uniqueness of a normalized morphism are independently checked here; KnudsenMumford1976 supplies graded determinants.')
update(33,fate='Freed2013 equation2.7 explicitly gives the sign(det) orientation character. The omitted generation argument extending the manuscript parabolic calculation to all GL_n(R) is independently checked here.')
update(58,['LiedtkeSatriano2025'],'Esquisse1997 §4 pp21–25 describes the arithmetic program. Ji2023 §3.1 Proposition3.1 verifies explicit good-prime matrix specializations, excluding2,5 for his icosahedron formulas. LiedtkeSatriano2025 Theorem4.7 concerns excellent-Dedekind bases and linearly reductive group schemes, and Theorem5.2 classifies already fppf-locally conjugate subgroups by normalizer torsors. These are precise related results, but neither proves the page’s unrestricted étale-local SO3 configuration statement. Its configuration, quadratic-form and base hypotheses still require identification.')
update(52,['LiedtkeSatriano2025'])
claims[51]['fate']+=' LiedtkeSatriano2025 Proposition7.1 makes Aut(mu_n) constant étale; that is not a claim that mu_n itself is étale.'
for i in [1,2]:
    problems[i]['refs'].append('QiaochuYuan2017')
    problems[i]['state_of_art']+=' QiaochuYuan2017 explicitly proves the module-functor classification over arbitrary Q-algebras and distinguishes local from uniform nilpotence.'
problems[3]['refs'].append('Zhao2017')
problems[3]['state_of_art']+=' The checked2022 revision of Zhao2017, Corollary2.4 p7, supplies m!(Da)^m=0 when D^m=0; polarization yields the required ideal nilpotence.'
for i in [4,5,6]:
    problems[i]['refs'].append('Freed2013')
    problems[i]['state_of_art']+=' Freed2013 pp15–16, Exercises2.6 and2.9, gives the explicit orientation torsor and exact-sequence model; its quotient-first convention is recorded rather than conflated with the manuscript convention.'
problems[16]['refs'].append('LiedtkeSatriano2025')
problems[16]['state_of_art']+=' LiedtkeSatriano2025 Theorems4.7 and5.2 are nearby arithmetic group-scheme results with different hypotheses and fppf-local conclusions; neither settles the exact configuration statement.'
write()

# Exact passages actually inspected, with the scope of the check stated separately.
R={
'MontpellierCatalog':('Cote68 footnote58 and catalogue entry; cote161-6 entry','Official catalog identifies the literary title tentatively as preparatory to R&S or Réflexions mathématiques; bracket dates and whole-dossier page counts checked.','These are catalog estimates, not authorial dates on supplied leaves; no scans opened.'),
'MathlibPolynomialNilpotent':('Polynomial.isUnit_iff_coeff_isUnit_isNilpotent and Polynomial.not_isUnit_of_natDegree_pos_of_isReduced','The documented theorem says a polynomial unit over a reduced commutative ring has no positive-degree coefficient.','Documentation inspected, no Lean execution or manuscript theorem certificate claimed.'),
'AptSimon2021':('Theorems14 and17, printedpp16–18','Well-founded win/lose and three-outcome determinacy; terminal conventions compared.','Finite-game bounds are not assumed; no first-priority claim.'),
'Milne2017':('Theorem4.8; Proposition14.32 and Corollary14.33, pp288–290','Locally finite representations and characteristic-zero unipotent exponential framework.','Finite-type group schemes over a field; arbitrary Q-algebra arguments are independent.'),
'DuboulozLiendo2014':('Preprint Theorem2.1, printedp5; author bibliography publication entry','Semi-affine rational integrability plus global local nilpotence; Ga/LND setting.','Not the stalkwise-local-nilpotence hypothesis of the manuscript.'),
'QiaochuYuan2017':('In characteristic zero; coefficient recurrence and translation example','Exact classification of Ga actions on arbitrary module functors over Q-algebras by locally nilpotent endomorphisms.','Author exposition, not a peer-reviewed publication; formal functor counterexample independently proved.'),
'Zhao2017':('Checked v2,10August2022: Corollary2.4 printedp7; Theorem4.3 and Corollary4.4','The relation D^m=0 implies m!(Da)^m=0; nilradical consequences separately checked.','2017 first-version text fetch failed, so no claim that the exact corollary already appeared there.'),
'Stacks09CH':('Definition10.133.1; Example10.133.5','Recursive differential-operator definition; derivations have order at most1.','Difference-ideal criterion is our direct deduction.'),
'EGAIV4':('Definition16.8.1 pp39–40; Proposition16.8.8 pp42–43; Theorem16.11.2 p54; Theorem16.12.2 p55','Principal-parts/commutator equivalence and differential smoothness basis read in original French PDF.','1967 publication is not ordered against undated individual sheets.'),
'Freed2013':('Exercises2.6 and2.9, equations2.7 and2.11, §2.8, pp15–16','Determinant orientation torsor, sign determinant and short-exact-sequence orientation model.','Exercise statements used as a model; exact manuscript axioms independently re-proved; quotient-first convention differs.'),
'KnudsenMumford1976':('Originalpp20–21','Graded invertible lines, Koszul symmetry and exact-sequence determinant maps.','Does not assert uniqueness under the sheet’s abbreviated weak normalization.'),
'MuroTonksWitte2015':('Definition1.2.3; introduction on1973 Grothendieck letter','Modern determinant functor coherence and distinct Grothendieck question identified.','No transfer of its universal theorem to incomplete archival axioms.'),
'SimoesPereira2016':('Full exposition and arXiv submission history','A5 and the60 rotations; geometric group identification.','Our exact coordinates and full graph group120 are independently checked.'),
'Ji2023':('§3.1 Proposition3.1, printedp5; §2 normalizations','Good-prime rotational matrix specializations; excludes2,5 in the icosahedron case.','Does not prove all-base étale-local existence or conjugacy.'),
'Stacks03PK':('Lemmas59.28.1 and59.28.3','Étale Kummer theory when n is invertible; general fppf statement.','The fixed-ring computation needs no division by2 and is independently checked.'),
'LiedtkeSatriano2025':('Theorems4.7 and5.2 pp16–19; Proposition7.1 p21','Local conjugacy under stated arithmetic restrictions; normalizer torsors for already locally conjugate subgroups; Aut(mu_n) constant étale.','SL2/group-scheme and fppf claims are not the unrestricted SO3 configuration/étale claim.'),
'Lafforgue2024':('Slides47–48','Product-topos site generated by factor covers; locally compact comparison with spaces.','Does not identify the missing frame axiom e; direct-image Kan formula independently checked.'),
'SageRibbonGraphs':('Permutation description; boundary and genus examples/methods','Ribbon graphs thicken to oriented surfaces; boundary cycles determine genus.','Official documentation read, no Sage computation claimed.'),
'Yagasaki2000':('Theorem1.1 and Corollary1.1, p1','Local extension and principal restriction bundles for proper embeddings of compact PL polyhedra.','Relative and compact-polyhedron hypotheses retained before using the homotopy exact sequence.'),
'Yagasaki2002':('Abstract and main homotopy-type classification','Components depend on image fundamental group under connectedness and exceptional-case restrictions.','Not a substitute for the graph isotopy or whole mapping-class stabilizer theorem.'),
'Epstein1966':('Theorem6.3, printedp99','Properly homotopic surface homeomorphisms are isotopic under the stated boundary/base-point conditions.','Not an exact graph-embedding theorem; exceptional surface hypotheses must be retained.'),
'FarbMargalit2011':('Author books pages','Bibliographic identity only.','Theorem8.1 not inspected; no theorem check is claimed.'),
'ColinMesmay2014':('arXiv-version Theorem14 PDFp14; Lemma5 PDFp8; Corollaries15–16','Finite graph embeddings in a compact oriented surface: oriented congruence plus cycle homotopy characterizes isotopy. Extended map classifies congruence.','Author final version renumbers the theorem4. Original Ladegaillerie article not read.'),
'Ladegaillerie1984':('ColinMesmay2014 references/introduction; CSG bibliography; thesis list','Publication identity and later attribution of the graph-isotopy characterization.','Original article unverified; result checked through the later independent proof.'),
'Esquisse1997':('§3 pp13–14; §4 pp21–25; publisher metadata','Direct retrospective graph-isotopy and arithmetic-polyhedra links; written1984, published1997.','Historical narrative does not date individual sheets; arithmetic program is not proof of a universal theorem.'),
'RecoltesNote94':('Note94, manuscriptpp399–401, HTML transcription','Author’s retrospective dates1974,summer1975,May1976 for Ladegaillerie work.','HTML not collated to scans; subjective publication-delay account not independently adopted.'),
'Larson2008':('Author introduction; collected-works publication metadata','Historical route to Zermelo game results.','Original1913 paper not read; not used for priority.'),
'CSGBibliography':('Ladegaillerie1974 and1984 entries','Bibliographic backward tracing.','No original proof read through this list.'),
'GrothendieckTheses':('Entry12, Ladegaillerie','Thesis bibliographic connection.','No original thesis inspected.')}
bib=(OUT/'references.bib').read_text()
records=[]
for key,(locator,checked,limit) in R.items():
    m=re.search(r'@\w+\{'+re.escape(key)+r',\n(.*?)(?=\n\}\n)',bib,re.S)
    assert m,key
    u=re.search(r'url=\{([^}]+)\}',m.group(1))
    verified='note={verified}' in m.group(1)
    records.append(dict(key=key,url=u.group(1) if u else None,opened=verified,date=DATE,locator=locator,checked=checked,limit=limit,mathematical_passage_checked=key not in ['MontpellierCatalog','FarbMargalit2011','Ladegaillerie1984','CSGBibliography','GrothendieckTheses','Larson2008','RecoltesNote94']))
(OUT/'reference_checks.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
refmap={a['key']:a for a in records}

# Each query was issued; IDs were assigned manually before searching.
# Per-claim outcomes below are the manually authored dossiers, not keyword verdicts.
audit_files=['audit_games_exp','audit_derivation','audit_determinant_icosa','audit_topos_graph','audit_surface_arithmetic','audit_named_channels']
logs=[]
for stem in audit_files:
    a=json.loads((OUT/'external'/f'{stem}.json').read_text())
    for q in a['batch']['qs']:
        ids=[f'C-SA23-misc-{i:03d}' for i in q['ids']]
        refs=list(dict.fromkeys(k for i in q['ids'] for k in claims[i-1]['refs']))
        logs.append(dict(date=DATE,action='literature search and followed-source assessment',query=q['q'],claim_ids=ids,source_channels='Web search; primary papers/author pages and listed mathematical repositories followed as relevant',opened_matches=[refmap[k] for k in refs if refmap[k]['opened']],unopened_originals=[k for k in refs if not refmap[k]['opened']],outcomes={f'C-SA23-misc-{i:03d}':claims[i-1]['fate'] for i in q['ids']},limits='The listed matches include subsequent follow-up opens, not a claim that every URL was returned by this exact query. Exact nonmatches and hypothesis restrictions are retained. No unsuccessful search is evidence of nonexistence.'))
# Preserve actual final exact opens and failed attempts separately.
for url,ids,outcome in [
('https://qchu.wordpress.com/2017/11/26/the-representation-theory-of-the-additive-group-scheme/',[11,12,13,14,15,16,17,18,19,39],'Opened full coefficient proof and exact Q-algebra/arbitrary-module theorem, including translation example; added precise classification source.'),
('https://arxiv.org/pdf/1701.06124',[23,24],'Opened v2; Corollary2.4 p7 supplies m!(Da)^m=0. Exact specialization and polarization independently checked.'),
('https://arxiv.org/pdf/1701.06124v1',[23],'Failed DisabledError; did not inspect first-version theorem wording.'),
('https://arxiv.org/abs/1701.06124',[23],'Failed DisabledError; no complete submission-history verification through this page.'),
('https://www.numdam.org/item/PMIHES_1967__32__5_0/',[21,22,25,26,27],'Catalog opened; complete original PDF downloaded and read at exact locators16.8.1,16.8.8,16.11.2,16.12.2.'),
('https://arxiv.org/pdf/2506.21210',[52,58,59],'Opened Theorems4.7,5.2 and Proposition7.1; exact restrictions exclude a direct solution of the all-base icosahedron configuration claim.'),
('https://arxiv.org/abs/2506.21210',[58],'Submission26June2025 verified; no journal reference shown.'),
('https://arxiv.org/pdf/1310.2745',[62,64,66,68,69,70],'Full independent proof opened. Theorem14 and Lemma5 match finite graphs and compact oriented surfaces with oriented congruence; exact hypotheses retained.'),
('https://link.springer.com/article/10.1007/s00454-013-9555-4',[69],'Publication metadata opened: online30October2013; journal issueJanuary2014.'),
('https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf',[49,58,59,66,69],'Full French text opened; §3 pp13–14 and §4 pp21–25 give exact author retrospective links.'),
('https://linguista.cn/library/persons/recoltes-et-semailles-i/p3chap5/?lang=fr',[69],'Note94 HTML transcription opened at manuscriptpp399–401; not ink-collated; author retrospective dates separated from independently established history.'),
('https://www.laurentlafforgue.org/Cours_Lafforgue_Mondovi_Septembre_2024.pdf',[53,60,61],'Slides47–48 opened: product-topos generated topology and space comparison. No automatic rectangular-grid refinement inferred.'),
('https://people.math.harvard.edu/~dafr/bordism.pdf',[30,31,32,33,34,35,36],'Exercises2.6/2.9 and equations2.7/2.11, pp15–16 opened; quotient-before-subspace convention retained.'),
('https://projects.lsv.ens-paris-saclay.fr/topology/?page_id=1224',[53],'Opened author electronic-book supplement on failure of O to preserve products. Not used to claim an exact counterexample to the unfinished archival axiom e.'),
('https://cfc.nankai.edu.cn/_upload/article/files/ca/07/264e89bc4d9bb418a6d91d482b90/cd26d6f4-5e7f-41b7-aeb8-8d083b67d6d3.pdf',[57,72,73,74],'Opened Li–Lu–Zhang coset-graph Lemmas3.1–3.2, p5. Finite simple graph hypotheses are narrower; general loop/nonloop formulas re-proved here. Publication identity not established, so not used as a final exact theorem citation.')]:
    logs.append(dict(date=DATE,action='opened exact source or recorded fetch failure',query=None,url=url,claim_ids=[f'C-SA23-misc-{i:03d}' for i in ids],outcome=outcome))
logs.append(dict(date=DATE,action='documentary title search',query='"Grothendieck" "Les épousailles"',item_ids=['SA23-342','SA23-343'],claim_ids=[],opened_url='https://grothendieck.umontpellier.fr/archives-grothendieck/',outcome='Official catalog cote68 footnote58 identifies the same title as tentatively preparatory to R&S OR Réflexions mathématiques. This does not settle the work identity.'))
logs.append(dict(date=DATE,action='documentary title search',query='"Les épousailles" "XVIII" "1982"',item_ids=['SA23-342','SA23-343'],claim_ids=[],outcome='No exact independently checked identification. The visible82 remains pagination, not a date.'))
logs.append(dict(date=DATE,action='opened exact source',query=None,url='https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Nilpotent.html',claim_ids=['C-SA23-misc-020'],outcome='Documentation verifies the precise reduced-ring polynomial-unit lemma named by the earlier notes. No Lean certificate executed.'))
# Source-channel access limits actually encountered.
logs.append(dict(date=DATE,action='channel and access audit',claim_ids=[c['id'] for c in claims],query=None,outcome='zbMATH-targeted searches were issued; some returned external bibliographies rather than an accessible review. A direct EGA zbMATH lookup returned403. Original Ladegaillerie1984 article and1974 C.R. notes were not opened; original-note Gallica attempts failed. SGA searches supplied related site/product leads; no exact original SGA product proposition was checked, so the claim uses Lafforgue’s opened slide47 and an independent adjunction proof. MathOverflow questions88529 and248866 were opened as leads, with their cited primary literature followed. Numdam EGA original PDF was successfully read. ArXiv and author bibliographies supplied exact versions. A separate Récoltes PDF was incomplete and was not used.'))
(OUT/'search_log.jsonl').write_text(''.join(json.dumps(a,ensure_ascii=False)+'\n' for a in logs))
assert set(c['id'] for c in claims)<=set(i for a in logs if a.get('query') for i in a['claim_ids'])

# Refined statements remain separate from the false literal claim.
refuted=[3,13,19,22,25,26,27,29,42,47,52,56,57,59,63,65,67,68]
partial=[20,36,37,53,58]
refinements=[]
for n in refuted:
    a=claims[n-1]
    refinements.append(dict(id='R-'+a['id'],source_claim=a['id'],statement=a['statement'],reason=a['computation']['proof_or_check'],qualification='For mixed true/false claims this retains the explicit corrected scope, not the false literal assertion.'))
(OUT/'refinements.json').write_text(json.dumps(refinements,ensure_ascii=False,indent=2)+'\n')
events=[]
def event(s,t,o):events.append(dict(statement_id=s,date=DATE,who=WHO,type=t,outcome=o))
items=json.loads((OUT/'items.json').read_text())
for a in items:event(a['id'],'used and rechecked in this run','Textual collation of the actual indexed note and its actual transcription passage: '+a['check']+'. '+a['check_reason']+' This is a documentary comparison; mathematical checks have separate claim events.')
for n,a in enumerate(claims,1):
    if n in refuted:
        event(a['id'],'refuted, with the refined statement\'s id','Refined statement R-'+a['id']+'. '+a['computation']['proof_or_check'])
    elif n in partial:
        event(a['id'],'targeted proof check',a['computation']['proof_or_check']+' The whole literal or unfinished claim is not certified.')
    elif n in [60,61,64,69,71]:
        event(a['id'],'used and rechecked in this run',a['computation']['proof_or_check']+' Exact source hypotheses compared; no full independent re-proof of the cited major theorem is claimed.')
    else:event(a['id'],'independent re-proof',a['computation']['proof_or_check'])
    if a['computation']['code']:
        event(a['id'],'computation or formal certificate','Executed '+a['computation']['code']+'; saved '+a['computation']['output']+'. Symbolic and finite checks support the displayed instances; no formal proof assistant certificate is claimed.')
    event(a['id'],'targeted proof check','Literature fate and quantifier comparison: '+a['fate']+' References: '+', '.join(a['refs'])+'.')
for a in refinements:event(a['id'],'used and rechecked in this run',a['reason'])
for a in records:
    t='targeted proof check' if a['mathematical_passage_checked'] else 'carried as background without fault found'
    event(a['key'],t,a['locator']+': '+a['checked']+' Limit: '+a['limit'])
for a in problems:event(a['id'],'used and rechecked in this run','Authorial flag and drafting status collated. '+a['state_of_art']+' No cause for abandonment inferred beyond the stated evidence.')
with (OUT/'check_events.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

# Our-project leads are deliberately isolated in addition to the combined required table.
with (OUT/'links.tsv').open() as f: links=list(csv.DictReader(f,delimiter='\t'))
for name,kind in [('project_links.tsv','our projects'),('verified_links.tsv',None)]:
    rows=[r for r in links if (r['kind']==kind if kind else r['kind']!='our projects')]
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(rows)
counts=dict(entries=53,items=len(items),claims=len(claims),problems=len(problems),readings=sum(1 for _ in (OUT/'readings.tsv').open())-1,links=len(links),references=len(records),search_events=len(logs),check_events=len(events),claim_classes=dict(Counter(c['class'] for c in claims)),claim_statuses=dict(Counter(c['status_on_pages'] for c in claims)))
(OUT/'counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
