#!/usr/bin/env python3
"""Integrate the frozen, independently checked determinant-source supplement.

No mathematical certificate is rerun. Preserve the exact pre-integration
sources, append fresh component aliases only, and retain historical events.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import time

root=Path(__file__).resolve().parents[1]
begin=time.perf_counter()
now=datetime.now(timezone.utc)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected={
 'notes/C_KnudsenMumford_sign_fragment.tex':'d6dbc83a97741ade21f2ab4efd93e42eda483309629989b771db5a60052fa3ac',
 'notes/C_KM_results_proposal.csv':'5d8ddbeca850e983d4efdb27ab9f43cba035c9362c9c658b87e0f1d96a81ad61',
 'notes/C_KM_CHECK_EVENTS_proposal.tsv':'7d9ab26c0643d287fa5c539a476bd47d5b3044a526be379006bb806d5a53a9fa',
}
for name,digest in expected.items():assert sha(root/name)==digest,name
result_path=root/'C_results.csv'
event_path=root/'C_CHECK_EVENTS.tsv'
root_event_path=root/'ROOT_CHECK_EVENTS.tsv'
part=root/'sections/part_C.tex'
new_rows=list(csv.DictReader((root/'notes/C_KM_results_proposal.csv').open()))
new_events=list(csv.DictReader((root/'notes/C_KM_CHECK_EVENTS_proposal.tsv').open(),delimiter='\t'))
assert len(new_rows)==5 and len(new_events)==14
assert {r['id'] for r in new_rows}=={f'C.{i}' for i in range(42,47)}
old_rows=list(csv.DictReader(result_path.open()))
assert not ({r['id'] for r in old_rows}&{r['id'] for r in new_rows})
from A567_normalize_check_events import ALLOWED_TYPES
assert all(e['type'] in ALLOWED_TYPES for e in new_events)
label_checks={
 'C:graded-determinant-sign':'PASS: root checked integral-degree coherence, exterior block permutation signs, complement comparison and the exact characteristic-zero counterexamples. Original cote68/056 and reproduced1973letter p41 were actually viewed; original p20 sign crop was independently viewed. The full proof and source-scope limits were read. No whole-letter or orientation/Stokes re-proof is claimed.',
 'C:determinant-ordinary-basechange':'PASS: root checked every scheme/map, properness and finite Tor dimension, ordinary fibre-product identification, cochain degrees and the graded-degree obstruction. The first printed determinant-pullback comparison remains distinct from the second false assertion. The certificate output was read, not rerun.',
 'C:determinant-basechange-repair':'PASS: root checked the exact affine universal-perfect-complex iff, the R-free resolution after forgetting the A-action, local affine reduction, conservative pushforward and projection formula, and proper noetherian perfection. Full Stacks08IB/08EU/0B6G/08EV statements and proofs were separately opened and read.',
 'C:determinant-trace-splitting':'PASS: root checked kernel/cokernel exactness over arbitrary commutative rings, positive-rank unit criterion, F2 nonzero kernel and the two-generator centralizer obstruction. The exact finite outputs were read without rerunning the programs.',
 'C:determinant-incidence':'PASS: root checked quotient-line convention, coevaluation and arbitrary base change, the P(K dual) incidence model, coordinate versus unit charts, independent-factor Koszul regularity and the empty rank-one case. Every claim has its proof in the integrated fragment.',
}
who='GPT-6 Astra (OpenAI), inherited reasoning effort, run /root, ChatGPT Pro mode'
root_events=[{'statement_id':label,'date':now.isoformat(),'who':who,'type':'targeted proof check',
              'outcome':outcome+' See notes/ROOT_determinant_integration_audit.md; auxiliary correction, no task-gate movement.'}
             for label,outcome in label_checks.items()]
root_events.append({
 'statement_id':'C:graded-determinant-sign','date':'2026-11-19',
 'who':'GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/geometry_a567, ChatGPT Pro mode',
 'type':'independent re-proof',
 'outcome':'PASS: original pp19-22 directly read; the explicitly typed split three-by-three exact diagram gives opposite nonzero wedges for the printed sum rule. The product rule repairs it. Actual reproduced1973letter pp40-42 checked and bounded erratum search recorded. No failure is inferred from the double-swap identity, which holds. Full independent proof: notes/A567_Knudsen_sign_independent_audit.md.'
})
insertion='\n\\subsection{Graded determinants: the requested source and its qualifications}\n\\input{notes/C_KnudsenMumford_sign_fragment.tex}\n'
assert 'C_KnudsenMumford_sign_fragment.tex' not in part.read_text()
targets=[result_path,event_path,root_event_path,part]
history=root/'notes/determinant_integration_before'
assert not history.exists()
for path in targets:assert path.read_bytes().endswith(b'\n'),path
history.mkdir()
before={str(path.relative_to(root)):sha(path) for path in targets}
for path in targets:
    dest=history/path.relative_to(root)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(path.read_bytes())

def append_rows(path,rows,delimiter):
    fields=list(rows[0])
    with path.open() as f:assert next(csv.reader(f,delimiter=delimiter))==fields
    buf=io.StringIO(newline='')
    writer=csv.DictWriter(buf,fieldnames=fields,delimiter=delimiter)
    writer.writerows(rows)
    with path.open('a',newline='') as f:f.write(buf.getvalue())

append_rows(result_path,new_rows,',')
append_rows(event_path,new_events,'\t')
append_rows(root_event_path,root_events,'\t')
with part.open('a') as f:f.write(insertion)
note='''# Root integration audit: determinant source qualifications

Date and exact frozen hashes are in `logs/ROOT_determinant_integration.json`.
Root read all five complete proofs, the added proper-perfection paragraph,
the three certificate outputs, the B exact-text/source-context audits, and
the A567 original sign-context proof. The original cote68 scan056 and the
reproduced1973letter p41 were directly inspected by root; A567 and C's
separate three-page letter readings are recorded under their own scopes.
Root also opened and read Stacks08IB,08EU,0B6G,08EV with their full proofs.

The exact proposal files remain unchanged. Five fresh component aliases
C.42--C.46 and fourteen proposed canonical-type check events are appended,
together with five actual root targeted checks and the A567 independent
re-proof event. No historical event is rewritten or promoted. The original
SA22-12 determinant identifier is preserved in the new event's outcome;
no alias is introduced that would remap a prior event. The complete source
supplement is included by the PartC file, after its existing material.

All three source corrections and their proved replacements are in the
paper. The ordinary base-change counterexample is kept distinct from the
determinant functor's own pullback coherence; the trace decomposition is
kept distinct from the valid incidence construction. The manuscript's
finite-free determinant requirements are not expanded into a claim about
all later perfect-complex axioms. No source-access gate changes, and no
certificate was rerun for integration.

Pre-integration component and PartC bytes are retained under
`notes/determinant_integration_before/`. A fresh bibliography merge,
canonical consolidation, LuaLaTeX build and actual image inspection are
required before publication of the changed paper.
'''
(root/'notes/ROOT_determinant_integration_audit.md').write_text(note)
record={
 'started_utc':now.isoformat(),'finished_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-begin,
 'frozen_proposal_hashes':expected,'added_component_rows':5,
 'added_component_events':14,'added_root_record_events':len(root_events),
 'source_hashes_before':before,
 'source_hashes_after':{str(path.relative_to(root)):sha(path) for path in targets},
 'mathematical_certificates_rerun':False,'task_gate_movement':False,
 'publication_state':'Fresh build and actual visual QA required.'
}
(root/'logs/ROOT_determinant_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
