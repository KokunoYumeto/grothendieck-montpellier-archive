"""Structural validation and truthful check-event serialization after manual review."""
from pathlib import Path
import csv,json,re,collections,hashlib,datetime
W=Path(__file__).resolve().parents[1]
items=json.loads((W/'items.json').read_text());claims=json.loads((W/'claims.json').read_text());problems=json.loads((W/'problems.json').read_text())
for i in items:
    if i['id']=='SA09-121':
        i['reconstruction']='The D8 counterexample is the earlier run’s idea, independently recomputed here. This run also supplies a geometric counterexample: the nine-punctured rational line in claim CL-SA09-138E-010 has full geometric automorphism group C3, and a graph section over Q(sqrt(-3)) centralizes that kernel without being normal. Its 504 Möbius candidates are exhaustively checked with exact fractions.'
    if i['id']=='SA09-139':
        i['statement']='For the natural G_Q-module μ_n, 0→μ_n/μ_n(Q)→Z¹(G_Q,μ_n)→H¹(G_Q,μ_n)→0 is exact. At n=2 the first term is zero, so an extra Z/2 kernel over this fixed quotient is false. At the Tate-module limit the written direct sum is also false as an abstract abelian group: Z¹(G_Q,Zhat(1)) is torsion-free while its Kummer H¹ quotient contains the nonzero order-two class of -1.'
        i['reconstruction']='The finite exact sequence is the earlier run’s reconstruction; the cancelled denominator leaves no completed manuscript replacement. This run adds the inverse-limit torsion argument in CL-SA09-138E-021. The finite n=2 witness tests the actual extension maps; the limit witness rules out an abstract splitting as well.'
(W/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
entries=list(csv.DictReader((W/'entries.tsv').open(),delimiter='\t'))
assert len(entries)==102
assert {r['entry_id'] for r in entries}=={f'MPL_138_001-045#{i}' for i in range(1,103)}
assert len({r['entry_id'] for r in entries})==102
byid={i['id']:i for i in items}
assert len(byid)==70
for i in items:
    assert i['id']=='SA09-'+str(104+min(int(s.rsplit('#',1)[1]) for s in i['sources']))
for r in entries:assert r['item_id'] in byid and r['entry_id'] in byid[r['item_id']]['sources']
assert set(s for i in items for s in i['sources'])=={r['entry_id'] for r in entries}
for c in claims:
    assert all(i in byid for i in c['items'])
    assert c['class'] in 'ABCDEF'
assert len(claims)==48 and len({c['id'] for c in claims})==48
assert len(problems)==10
bibkeys=set(re.findall(r'@\w+\{([^,]+),',(W/'references.bib').read_text()))
for x in claims+problems:
    for r in x['refs']:assert r.split(':',1)[0] in bibkeys,(x['id'],r)
search=list(csv.DictReader((W/'search_log.tsv').open(),delimiter='\t'))
assert {r['claim_id'] for r in search}=={c['id'] for c in claims}
readings=list(csv.DictReader((W/'readings.tsv').open(),delimiter='\t'));assert len(readings)==40

who='GPT-6 Astra Pro; inherited effort (not separately exposed); SA09/cote138_early'
events=[]
def event(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for i in items:
    event(i['id'],'used and rechecked in this run','Source comparison: '+i['check']+'. '+i['check_reason']+' This event certifies comparison with the actual transcription; by itself it is not a proof of the mathematical assertion.')
nonproof={2,8,20,23,37,43}
for c in claims:
    n=int(c['id'].split('-')[-1]);comp=c['computation']
    if n not in nonproof:
        event(c['id'],'independent re-proof',comp.get('method',comp.get('output','Exact argument given in synthesis.md.'))+' The scope is the explicitly stated mathematical formulation; no scan reading is decided. For incomplete claims only the identified finite/standard part is checked.')
    else:
        event(c['id'],'used and rechecked in this run',c['fate']+' This records the stated theorem/hypothesis match or the bounded incomplete-source finding, not an independently proved new theorem.')
    if comp.get('program'):
        event(c['id'],'computation or formal certificate','Exact reproducible computation: '+comp['program']+'; '+comp.get('output','outputs/computations.json')+'. '+comp.get('limit','Finite checks support only the explicitly described finite assertions; general conclusions use the stated proof or opened theorem.'))
    if c['status_on_pages']=='false as stated':
        refined=comp.get('refined_statement_id',c['id']+' (corrected formulation in its statement field)')
        event(c['id'],'refuted, with the refined statement\'s id','Refined statement: '+refined+'. '+comp.get('counterexample',comp.get('method','Counterexample and exact qualification in synthesis.md and computations output.')))
event('SA09-154','independent re-proof','The degree-nine connected cover of the three-punctured sphere has free rank 1+9(2-1)=10. Its compactification has genus one; filling nine punctures imposes the peripheral quotient and leaves a rank-two abelian fundamental group. This compares the actual open/proper objects, not an unspecified isomorphism between their towers.')
event('SA09-168','independent re-proof','Since G_Q acts on M=T² by scalar units, every Zhat-linear automorphism commutes with it; the linear centralizer is GL2(Zhat). No lift to the centralizer of the full outer action is deduced.')
for key in sorted(bibkeys):
    if key.startswith('Project'):
        event(key,'used and rechecked in this run','Opened exact local manuscript/return/referee passages recorded in project_endpoint_audit.md and verified_project_links.tsv. Verification is textual correspondence and reported review scope, not independent re-proof of external project results. The root session materialized the linked Library archive; target file hashes are preserved.')
    elif key=='PeruccaSgobba2019':
        event(key,'used and rechecked in this run','After repository failures, opened the World Scientific publisher preview at ResearchGate. Theorem1.1 on printed p.1617 gives the uniform Kummer degree bound over an arbitrary number field, with exact finite-generation/torsion-free/rank hypotheses. Statement and publication dates read; full proof not opened or independently re-proved.')
    elif key in {'Ihara1986','IharaInvent1986','MontpellierCatalog2026'}:
        event(key,'used and rechecked in this run','Opened bibliographic/catalogue record only. The exact limitations and locators are in reference_verification.md; no unread theorem is certified.')
    else:
        event(key,'used and rechecked in this run','Opened the exact primary passages listed in reference_verification.md and references.bib; compared their hypotheses with the claims using them. This event does not mean that every proof in the cited work was re-proved. Schinzel1977 was read as a theorem statement; EGAIV3 §8.8 was read including proof.')
event('CL-SA09-138E-020','independent re-proof','Independently checked the deduction from the published uniform finite Kummer degree bound to full affine finite index: each mod-n affine index is at most C[K:Q], and compactness identifies the inverse-limit index with the supremum of the finite quotient indices. This event is only for that deduction, not a re-proof of Perucca–Sgobba Theorem1.1.')
with(W/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)

root=W.parents[2]
source_paths=[root/'source/SA09_notes/pro/MPL_138_001-045_notes.md',root/'source/SA09_notes/pro/MPL_138_001-045_doubts.md',root/'source/SA09_texts/pro/MPL_138_001-045_transcription.tex']
hashes=[]
for p in source_paths:
    if p.exists():hashes.append(dict(path=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
report={'entry_count':len(entries),'item_count':len(items),'verdicts':dict(collections.Counter(r['verdict'] for r in entries)),'claim_count':len(claims),'classes':dict(collections.Counter(c['class'] for c in claims)),'statuses':dict(collections.Counter(c['status_on_pages'] for c in claims)),'problem_count':len(problems),'readings':len(readings),'search_rows':len(search),'references':len(bibkeys),'check_events':len(events),'source_hashes':hashes,'schema_and_coverage':'PASS'}
(W/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
