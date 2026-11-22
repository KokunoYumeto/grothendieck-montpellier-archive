from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, sys

base=Path(__file__).resolve().parents[2]
out=base/'deliverable'
def read(name):
    with (out/name).open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
rows,questions,events=map(read,['CONSEQUENCES.tsv','QUESTIONS.tsv','CHECK_EVENTS.tsv'])
ids=[r['id'] for r in rows]
qids=[q['id'] for q in questions]
known={e['statement_id'] for e in events}
assert len(ids)==len(set(ids)) and len(qids)==len(set(qids))
assert not set(ids)-known
assert all(len(r)==6 and all(v is not None for v in r.values()) for r in rows)
canonical={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert {e['type'] for e in events}<=canonical
logpath=base/(sys.argv[1] if len(sys.argv)>1 else 'work/build_checkpoint07_pass4.txt')
log=logpath.read_text()
pages=re.findall(r'Output written on GRH_NIGHT.pdf \((\d+) pages\)',log)
assert pages and '\n! ' not in log
record=dict(time=datetime.now(timezone.utc).isoformat(),rows=len(rows),questions=len(questions),events=len(events),duplicates=[],missing_events=[],event_types={t:sum(e['type']==t for e in events) for t in sorted(canonical)},compilation=dict(log=str(logpath.relative_to(base)),pages=int(pages[-1]),overfull_boxes=log.count('Overfull'),undefined_references='There were undefined references' in log,rerun_requested='Rerun to get cross-references right' in log),proof_scope='Every newly registered proof has its actual author/whole-reading events. Classical results retain exact citation and scoped inspection. CX-ALG-008/009 retain the earlier documented alias/classical exceptions. Unregistered RS and boundary-PD routes are explicitly research notes.',optional_pdf='Omitted: full visual QA not performed.')
(base/'work/checks/checkpoint07_register_audit.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(base/'work/CHECKPOINT_STATUS.md').write_text(f'''# Scheduled checkpoint and review status

Checkpoint7 is the scheduled06:17UTC snapshot on2026-11-21. It contains{len(rows)} catalogue consequences,{len(questions)} questions and{len(events)} check events. The immutable ZIP records its own exact creation time and manifest. Earlier checkpoint ZIPs remain unchanged and are not nested.

Research is IN PROGRESS. Movement review3 completed06:03:06UTC against the frozen second review and found actual gate changes; the consecutive no-movement count remains0. The next review is07:02UTC. The next checkpoint after this one is07:02UTC as well. The two-consecutive-no-movement stopping rule remains in force.

The required LaTeX source compiled successfully at{pages[-1]}pages; the exact build validation is in checkpoint07_register_audit.json. The optional PDF is omitted because complete visual QA has not been performed.

MT-M36/37 check and repair normalization interfaces and exclude a single compatible indentation as an external-prime lift. A canonical trace-diagonal contraction now tests a specified varying-level repair. The independent geometric narrow-strip trace identity remains open.

MT-S506/507 give A_D-only S5 pole support and the complete exact monomial cone, with common-zero and relative-order gates. ExpandedMT-S508 needs only one quadratic-Hecke real-zero condition for the exact central comparison, half-plane exceptional-prime summability and real-axis holomorphy; fullGRH_B transfers to the knownGL5 numerator before exact transfer closes. Every such Hecke input remains conditional.

The geometry catalogue now includes exact integral inverse cycles on elliptic products, separate integral Fourier obstructions including an explicit nonzero2-torsion CM defect, and a precisely indexed independent K8(Z) theorem with Tate-twist consequences. General theta-cycle/LM6 comparisons remain gates.

NT-E14–16 give finite-field elliptic isogeny detection, including a fully proved polynomial input-time Q-isogeny decision under a finite degree-at-most384 Dedekind-RH family. NT-E17/18 give A_D-only polynomial CM recognition from bounded modular correspondences, with dense input encoding and no added ring-class Hecke hypothesis. Faster heuristic algorithms retain their extra assumptions.

The next unregistered routes and exact source-reading scope are preserved in work/checks/checkpoint07_pending_routes.md. They are not counted as checked findings.
''')
print(json.dumps(record,ensure_ascii=False,indent=2))
