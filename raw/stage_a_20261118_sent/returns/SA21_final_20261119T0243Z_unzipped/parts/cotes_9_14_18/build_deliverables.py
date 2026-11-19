"""Serialize manually read/assigned IX14–18 records. No automated verdicts."""
import csv,json,re,hashlib
from pathlib import Path
from collections import Counter
from claim_records import CLAIMS,GROUPS,ROOT
from problem_records import PROBLEMS
OUT=Path(__file__).parent
def js(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def tsv(name,fields,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
js('claims.json',CLAIMS);js('problems.json',PROBLEMS)
(OUT/'references.bib').write_text((OUT.parent/'cotes_6_7/references.bib').read_text()+'\n'+(OUT/'references_new.bib').read_text())
coverage=[]
for n in range(14,19):
    stem=f'J156-9-{n:02d}';p=ROOT/'sources/texts/codex'/f'{stem}_transcription.tex';q=ROOT/'sources/notes/codex'/f'{stem}_notes.md'
    scans=[int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',p.read_text())]
    coverage.append(dict(folder=stem,cote='156-9',scans=','.join(map(str,scans)),
      transcription_lines=len(p.read_text().splitlines()),notes_lines=len(q.read_text().splitlines()),
      transcription_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),notes_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),
      reading='Every transcription line and short note directly read; saved line-numbered read_outputs and read_log. Codex notes have no Stage1 verdict rows.',
      claims=';'.join(c['id'] for c in CLAIMS if any(stem in line for line in c['lines'])),
      limits='No scan images supplied; transcribed scan129 absent. Scans110/112 canceled reused R&S material; scan114 uncanceled reused R&S added notes; all read and kept separate from atelier theory. Scan140 completely canceled.'))
tsv('coverage.tsv',list(coverage[0]),coverage)
searchrows=[]
for p in sorted(OUT.glob('search_S9E_*.json')):
    raw=json.loads(p.read_text());sid=raw['id'];req=raw['request']
    groups=[name for name,g in GROUPS.items() if sid in g['searches']]
    cids=[c['id'] for c in CLAIMS if any('Search family: '+g+';' in c['present_status'] for g in groups)]
    for engine in ('system1_search_query','system2_search_query'):
        for query in req.get(engine,[]):
            searchrows.append(dict(search_id=sid,date='2026-11-19',query=query['q'],engine=engine,scope=';'.join(groups),claims=';'.join(cids),
              result='Full combined tool results in '+p.name+'. Exact matches and limits recorded per claim; absence of a matching returned hit is bounded negative evidence only.',
              followup='Primary opened sources in open_O9E_*.json; mathematical statements from search snippets alone are not used. Correction full text, Foulis original and R&S exact added-note endpoint inaccessible/unverified as recorded.'))
for name,g in GROUPS.items():
    for sid in g['shared_searches']:
        searchrows.append(dict(search_id=sid,date='2026-11-19',query='Shared exact query rows retained in ../cotes_6_7/search_log.tsv and corresponding search_S67_*.json',engine='shared documented search',scope=name,
          claims=';'.join(c['id'] for c in CLAIMS if 'Search family: '+name+';' in c['present_status']),result=g['scope'],followup='This is an explicit reuse of a completed search family, not a claim to have issued another query.'))
tsv('search_log.tsv',['search_id','date','query','engine','scope','claims','result','followup'],searchrows)

WHO='GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7'
events=[]
def event(cid,kind,outcome): events.append(dict(statement_id=cid,date='2026-11-19',who=WHO,type=kind,outcome=outcome))
independent={
 81:'Relation graph fiber characterization; arbitrary-set proof §2.',82:'Singleton images partition E′ iff a total inverse image; §2.',
 83:'A missing output singleton is exactly a nonzero transpose-kernel element.',84:'Intersection preservation plus zero reflection gives faithful disjointness; §2.',
 85:'Surjectivity of g iff inverse image reflects empty set.',87:'De Morgan and monotonicity imply all meets, top and orthogonality.',
 88:'Exact IX90 conjugacy plus both complement identities gives opposite adjunctions and mutual inverse maps.',89:'ker v=↓C(u1); no orthomodularity required.',
 90:'Any d⊥b with b∨d=c lies below c∧Cb; converse immediate.',91:'Three orthogonal pieces with the two local decomposition equations generate Boolean8 or a degeneracy.',
 92:'Identification with orthomodularity; commuting-family argument using Janowitz Lemma1(v) stated explicitly in proof file.',
 96:'Injective powerset partition map and minimal complete Boolean image proved.',97:'Outside atom must be nonzero; otherwise omit it.',
 99:'Nonzero b below two orthogonal parents would be self-orthogonal, impossible.',100:'Boolean common refinement criterion proved with the outside-atom correction.',
 102:'Earlier residue lies below a predecessor ancestor; later residue is orthogonal to it.',109:'Only the maquette case proved: δ=inequality gives ordinary set complement.',
 112:'A figure restricts open refinement to equality, using compatibility and irreflexivity.',
 117:'Injective direct images preserve arbitrary unions/nonempty intersections and fail whole-space complement exactly when nonsurjective.',
 118:'For f′ injective, direct-injection case iff f bijective iff transpose preserves complement; graph proof §2.',
 120:'Basepoint-preserving relation homomorphisms compose; checked all zero conventions.',123:'Universal maquette deletion, including non-ideal N and incidence across N, §6.',
 125:'Only fiber/total support equivalence proved within one complete Boolean subortholattice.',
}
computed={81:'set_relation_classification',82:'set_relation_classification',83:'set_relation_classification',84:'set_relation_classification',85:'set_relation_classification',
 86:'general_spatios_corollary_failure',93:'orthomodular_does_not_force_Boolean',94:'P4_comparability_counterexample',95:'scan113_reconstruction',
 103:'residual_lemma_missing_hypothesis',105:'commensurable_refinement_not_transitive',106:'faithful_external_does_not_imply_commensurability',
 116:'elementary_figure_pullback_not_elementary',118:'set_relation_classification',121:'bare_morphism_kernel_not_closed',
 126:'commensurability_alone_not_local_subdivision_detection',128:'deleted_quotient_topology_equivalence'}
for c in CLAIMS:
    n=int(c['id'].split('-')[-1])
    if n not in independent and n not in computed:
        event(c['id'],'carried as background without fault found','Complete source and short note read; this records use, not an independent proof. '+c['status_on_pages'])
    if n in independent:event(c['id'],'independent re-proof',independent[n]+' See formalism_and_checks.md; applies only to explicitly stated subclaims.')
    if n in computed:event(c['id'],'computation or formal certificate','check_ix_examples.py → finite_checks_output.json#'+computed[n]+'. Exhaustive finite Python certificate; scope qualifications are part of the output, not formal proof-assistant verification.')
event('C-SA21-9-114','targeted proof check','Checked the displayed Sousat argument assuming the stated prefigure compatibility; unresolved cancellation/restoration is retained in readings.tsv.')
event('C-SA21-9-121','independent re-proof','Kernel lowerness follows from0 being bottom for open refinement; the distinct support-closedness assertion is countertested separately.')
event('C-SA21-9-127','targeted proof check','Only surjectivity from nonzero X° and fiber coverage checked directly; maximality equivalence carried with source divisibility, not independently certified in full.')
for n,r,scope in [(86,1,'unrestricted complement implication'),(103,7,'standalone residual criterion without decomposition; not the γ²-strengthened reading'),(105,8,'transitivity of the proposed commensurable-discrete-figure refinement'),(106,5,'faithful⇒γ³ question, negative answer under exact faithful definition'),(116,9,'elementary preservation for the full-figure pullback'),(121,10,'automatic orthoclosedness under bare provisional hom conditions'),(126,11,'conditional derivability from commensurability alone; named source axiom remains uncertain'),(128,12,'general finite-poset equivalence only; source block canceled')]:
    event(f'C-SA21-9-{n:03d}','refuted, with the refined statement\'s id',f'R-SA21-9E-{r:03d}: {scope}; see refinements.json and full finite certificate.')
for p in PROBLEMS:event(p['id'],'carried as background without fault found','Problem formulation and all listed occurrences read; state-of-art comparison and exact unresolved limits documented in this record. Not an independent proof event.')
reference_events={
 'Janowitz1963':'Primary PDF pp1241–1242: orthomodular identity, Lemma1(i)–(v), adjoint framework read and used with stated hypotheses.',
 'Massas2023':'Previously opened primary PDF Theorems2.29–2.30 reused for powerset/downset duality; no new whole-paper verification claimed.',
 'Ore1944':'Previously opened primary text reproduction Theorem8 and polarity section reused; host summary is not a source of mathematical claims.',
 'LindenhoviusVetterlein2023':'Previously opened Example3.3 P4 and Lemma3.4 reused; the P4 computation independently rechecked in this part.',
 'HardingNavara2011':'Primary PDF opened; Boolean subalgebra definitions and MO2 passage inspected; reconstruction theorems not used as atelier results.',
 'PasekaVetterlein2025':'Primary published text opened, Lemmas3.7–3.8 and exact adjoint definition inspected; Proposition6.10 not used because v3 announces a correction.',
 'Jenca2026':'Primary arXivv1 Example2.6 and publisher PDF opened; exact P4 non-Dacey example independently rechecked. Incomparability classification is only a limited comparison.',
 'JencaCorrection2026':'Publisher metadata and abstract only verified; full corrected theorem inaccessible. No mathematical correction content carried as established.',
 'Stacks04VB':'Opened and read Definition4.27.1 and Lemma4.27.2; general calculus-of-fractions conditions distinguished from atelier hypotheses.',
 'Brameret1961':'Opened primary Numdam text, §II; historical orthogonal-adjoint framework checked, but OCR-missing formulas not used.',
 'Foulis1960':'Original fetch failed; only a backward bibliographic lead from opened sources, no original result checked.',
 'GabrielZisman1967':'Original book not obtained; Stacks citation toI§2 checked, not original contents.',
 'CSGUnpublished':'Previously opened primary bibliography reused: VGF remains catalogued among unpublished works; does not prove absence of later related results.',
 'Malgoire2002':'Previously opened primary seminar notice reused; it is evidence of a2002presentation, not an exact published theorem.',
 'CruzMorales2021':'Previously opened arXiv primary essay §4 reused as historical context only, not a technical solution.',
 'SGA4II':'Previously opened ExposéII definitions1.1,2.1 reused as limited site/sheaf comparison, not identification of atelier supports.',
 'Esquisse1997':'Previously opened §5 reused for stratified-topology motivation; not a proof of the proposed intrinsic constructible-support algebra.'}
for key,what in reference_events.items():event(key,'used and rechecked in this run' if key in {'Janowitz1963','PasekaVetterlein2025','HardingNavara2011','Jenca2026','Stacks04VB'} else 'carried as background without fault found',what)

if (OUT/'ancillary_records.py').exists():
    from ancillary_records import READINGS,LINKS,REFINEMENTS
    tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],READINGS)
    tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],LINKS)
    js('refinements.json',REFINEMENTS)
    for r in REFINEMENTS:event(r['id'],r['check_type'],r['verification'])
else:READINGS=[];LINKS=[];REFINEMENTS=[]
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
counts=dict(claims=len(CLAIMS),claims_by_class=dict(Counter(c['class'] for c in CLAIMS)),status_category_counts=dict(Counter(c['status_category'] for c in CLAIMS)),
  problems=len(PROBLEMS),folders=len(coverage),supplied_scans_read=sum(len(c['scans'].split(',')) for c in coverage),
  readings=len(READINGS),links=len(LINKS),own_refinements=len(REFINEMENTS),check_events=len(events),
  new_search_queries=sum(r['engine']!='shared documented search' for r in searchrows),shared_search_mappings=sum(r['engine']=='shared documented search' for r in searchrows),missing_supplied_scan='156-9 scan129')
js('counts.json',counts);print(json.dumps(counts,ensure_ascii=False,indent=2))
