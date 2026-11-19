"""Serialize the hand-read, hand-authored VI–VII consolidation.

This script performs only formatting, source-locator resolution and coverage
accounting. It does not infer verdicts from headings, keywords or statistics.
Run from any working directory with Python3.
"""
import csv,json,re,hashlib
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
from claim_records import CLAIMS,EVENTS,GROUPS,ROOT
from problem_records import PROBLEMS
from status_categories import STATUS_CATEGORIES

OUT=Path(__file__).parent
def write_json(name, data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def tsv(name, fields, rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        w.writeheader();w.writerows(rows)

assert len({c['id'] for c in CLAIMS})==len(CLAIMS)
assert all(c['lines'] and c['fate'] and c['refs'] for c in CLAIMS)
assert set(STATUS_CATEGORIES)=={c['id'] for c in CLAIMS}
for claim in CLAIMS:
    claim['status_category']=STATUS_CATEGORIES[claim['id']]
write_json('claims.json',CLAIMS)
write_json('problems.json',PROBLEMS)

coverage=[]
for cote,count in [(6,12),(7,14)]:
    for n in range(1,count+1):
        stem=f'J156-{cote}-{n:02d}'
        p=ROOT/'sources/texts/codex'/f'{stem}_transcription.tex'
        q=ROOT/'sources/notes/codex'/f'{stem}_notes.md'
        s=p.read_text(); ns=q.read_text()
        scans=[int(x) for x in re.findall(r'\\scanpage\{(\d+)\}',s)]
        attached=[c['id'] for c in CLAIMS if any(stem in x for x in c['lines'])]
        coverage.append(dict(folder=stem,cote=f'156-{cote}',scans=','.join(map(str,scans)),
            transcription_lines=len(s.splitlines()),notes_lines=len(ns.splitlines()),
            transcription_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),notes_sha256=hashlib.sha256(q.read_bytes()).hexdigest(),
            reading='complete direct model reading of every supplied transcription line and short note; line-numbered output saved',
            claims=';'.join(attached),limits='No scans supplied. VII scans2–9 absent from supplied files.' if cote==7 else 'No scans supplied.'))
tsv('coverage.tsv',list(coverage[0]),coverage)

# Search logs retain original tool results and exact queries. A query family can
# serve several mathematically connected records; this mapping is explicit.
searchrows=[]
for p in sorted(OUT.glob('search_S67_*.json')):
    raw=json.loads(p.read_text()); sid=p.stem.replace('search_','').replace('_','-')
    queries=raw.get('queries',[])
    if not queries:
        req=raw.get('request',raw.get('args',{}))
        for key in ('system1_search_query','system2_search_query'):
            queries.extend(x['q'] for x in req.get(key,[]) if 'q' in x)
    if not queries:
        queries=['See complete raw tool request/result in '+p.name+'; query transcription retained in research log.']
    groups=[k for k,v in GROUPS.items() if sid in v['searches']]
    claims=[c['id'] for c in CLAIMS if any('Search family: '+g+';' in c['present_status'] for g in groups)]
    for q in queries:
        if isinstance(q,dict): q=q.get('q',str(q))
        searchrows.append(dict(search_id=sid,date='2026-11-19',query=q,
            scope=';'.join(groups),claims=';'.join(claims),
            result='Full results and source identifiers: '+p.name+'. Exact matches and limits are recorded per claim; no-hit status is bounded, not an absence proof.',
            followup='Opened primary results in open_O67_*.json; original Raney, deJongh–Troelstra, Dacey and some EGA/zbMATH access attempts failed as documented.'))
tsv('search_log.tsv',['search_id','date','query','scope','claims','result','followup'],searchrows)

# Replace default carried-background events for the statements actually proved
# or refuted, rather than representing complete reading as proof verification.
independent={
 'C-SA21-6-010':'Lowerness preserves all ambient joins bounded by a member of the subfamily and the elementary decomposition; At3 expressly excluded.',
 'C-SA21-6-013':'Complete-homomorphism inverse-image theorem independently proved in formalism_and_checks.md §2, including empty operations.',
 'C-SA21-6-023':'Restriction is an inverse-image operation on deployments; all unions/intersections preserved.',
 'C-SA21-6-039':'Triangle boundary edge subdivision has4vertices/edges, while one2-simplex boundary has3; unchanged elementary filler impossible.',
 'C-SA21-6-040':'Finite-generation/complete-prime stationarity proof in formalism_and_checks.md §3; initial analyst suspicion withdrawn.',
 'C-SA21-6-044':'Minimal containing sets define a reflexive transitive relation; injectivity gives antisymmetry.',
 'C-SA21-7-017':'For ≪=≤, L1 iff M is discrete, L2 iff minima are cofinal below all elements; the unqualified only-L1 sentence is false.',
 'C-SA21-7-021':'A⊆A⊥⊥, triple-polar identity, closure idempotence and lattice operations checked algebraically.',
 'C-SA21-7-022':'Disjointness detection by Λ makes restriction/closure inverse on orthoclosed subsets.',
 'C-SA21-7-023':'Complete distinct-locus graph gives A⊥=L\\A and all subsets closed.',
 'C-SA21-7-026':'Inverse image preserves all powerset Boolean operations.',
 'C-SA21-7-028':'Disjointness iff represented set-disjointness proves the support order implications.',
 'C-SA21-7-030':'Singleton witnesses prove complement separation, every subset is a represented union, and complete Boolean isomorphism follows.',
 'C-SA21-7-047':'Every vertex of a positive-dimensional simplex belongs to its boundary, so the locus-based open support is empty.',
 'C-SA21-7-049':'Only the L1 consequence independently checked: empty interior makes δ(X,X) vacuously true, contradicting irreflexivity. Other equivalence directions carried from manuscript.',
 'C-SA21-7-051':'With lowerness included, finite principal ideals and finite compatible unions force exactly the finite compatible lower subsets.'}
computed={
 'C-SA21-6-011':'lower_subfamily_At3_failure',
 'C-SA21-6-015':'trivial_order_At8_counterexample',
 'C-SA21-6-016':'naive_figure_pullback_counterexample',
 'C-SA21-7-004':'square_simplex_counterexample',
 'C-SA21-7-033':'two_strand_grid_computation',
 'C-SA21-7-043':'path_graph_local_support_counterexample',
 'C-SA21-7-044':'path_graph_local_support_counterexample',
 'C-SA21-7-045':'path_graph_local_support_counterexample'}
events=[e for e in EVENTS if e['statement_id'] not in independent and e['statement_id'] not in computed]
for cid,what in independent.items():
    events.append(dict(statement_id=cid,date='2026-11-19',who='GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7',type='independent re-proof',outcome=what))
for cid,key in computed.items():
    events.append(dict(statement_id=cid,date='2026-11-19',who='GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7',type='computation or formal certificate',outcome='check_finite_examples.py → finite_checks_output.json#'+key+'. Finite exhaustive Python calculation, not proof-assistant certification; limitations stated in formalism_and_checks.md.'))
for cid,refined in [('C-SA21-6-011','C-SA21-6-011 (Sousat2 repair in statement)'),('C-SA21-6-015','C-SA21-7-017'),('C-SA21-6-016','C-SA21-6-016 (open-preimage repair explicitly analyst-owned)'),('C-SA21-7-004','C-SA21-7-004 (Boolean-interval comparison in statement)'),('C-SA21-7-043','C-SA21-7-043 (orthomodular-law qualification)'),('C-SA21-7-045','MP-SA21-7-13 (additional-hypothesis problem)')]:
    events.append(dict(statement_id=cid,date='2026-11-19',who='GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7',type='refuted, with the refined statement\'s id',outcome='Written generality refuted by saved finite certificate. Refined statement/problem: '+refined+'.'))
reference_events={
 'Ore1944':'Primary article text opened in reproduction after AMS failed; Theorems1–2 pp495–496, section4 p500, Theorem8 p503 checked. Host AI title/summary not used as mathematical evidence.',
 'Speed1968':'Opened original publisher PDF; §4 CorollaryC pp726–727 and §5 final corollary p730 checked. Historical terminology read in its displayed complete-prime context.',
 'Massas2023':'Opened author/repository PDF; Theorems2.29–2.30 p14 checked; older references followed but some originals blocked.',
 'LindenhoviusVetterlein2023':'Opened published article; Example3.3 exact P4 graph and six closed sets checked; Lemma3.4 Dacey criterion checked; publication and arXiv dates separated.',
 'Janowitz1963':'Opened original MSP PDF; p1241 orthomodular identity checked; older than manuscript.',
 'Stanley1991':'Opened author-hosted original PDF; §1 p319 Boolean principal interval definition checked; does not prove weak manuscript criterion.',
 'Lojasiewicz1964':'Opened Numdam original PDF; §3 Theorems1–2 pp463–464 checked; no unique unchanged-exterior extension claimed.',
 'Baro2010':'Opened author preprint PDF dated4October2007; Theorem4.3 p14 checked; journal2010 and digitization2014 distinguished.',
 'SGA4II':'Opened scholarly edition of primary ExposéII; Definitions1.1 and2.1 checked as formal comparison only.',
 'Esquisse1997':'Opened primary French text; §5 pp25–27 checked for stratified dévissage and noncanonical choices; no exact atelier claim matched.',
 'CSGUnpublished':'Opened catalogue; VGF1986 cotes156-1–9 listed as unpublished, not proof of absence of all related later work.',
 'Malgoire2002':'Opened primary IMAG seminar notice dated3October2002; exposition of VGF vocabulary, not a publication of an exact theorem.',
 'CruzMorales2021':'Opened arXiv abstract/history and PDF §4; conceptual/history discussion, not exact At/ML/Prat/Mag resolution.'}
for key,outcome in reference_events.items():
    events.append(dict(statement_id=key,date='2026-11-19',who='GPT-6 Astra Pro; inherited effort; /root/cotes_156_6_7',type='used and rechecked in this run',outcome=outcome))
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)

# Ancillary manually authored tables are imported only after they exist.
try:
    from ancillary_records import READINGS,LINKS
except ModuleNotFoundError:
    READINGS=[];LINKS=[]
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],READINGS)
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],LINKS)

counts={'claims':len(CLAIMS),'claims_by_class':dict(Counter(c['class'] for c in CLAIMS)),
        'problems':len(PROBLEMS),'folders':len(coverage),'readings':len(READINGS),'links':len(LINKS),
        'search_query_rows':len(searchrows),'check_events':len(events),
        'supplied_scans_read':198,'missing_supplied_scans':'156-7 scans2–9 absent from supplied files'}
write_json('counts.json',counts)
with (OUT/'progress.log').open('a') as f:
    f.write(datetime.now(timezone.utc).isoformat()+'\tSerialized hand-authored VI–VII records; '+json.dumps(counts,ensure_ascii=False)+'\n')
print(json.dumps(counts,indent=2,ensure_ascii=False))
