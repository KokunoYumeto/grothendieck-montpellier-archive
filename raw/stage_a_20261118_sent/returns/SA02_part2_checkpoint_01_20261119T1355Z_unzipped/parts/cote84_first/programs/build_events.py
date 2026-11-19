"""Serialize actual check events; event types are manually assigned below."""
from pathlib import Path
import csv,json
P=Path(__file__).resolve().parent.parent
WHO='GPT-6 Astra Pro; effort=not exposed; SA02 current run'
events=[]
def ev(id,typ,outcome):events.append({'statement_id':id,'date':'2026-11-19','who':WHO,'type':typ,'outcome':outcome})
for it in json.loads((P/'items.json').read_text()):
 ev(it['id'],'used and rechecked in this run','Textual scope only: all source entries and cited actual transcription passages were read and compared. Verdict '+it['check']+'. '+it['check_reason'])
cs={int(c['id'].split('-')[-1]):c for c in json.loads((P/'claims.json').read_text())}
# Explicit lists distinguish algebra certificates, independent arguments and source reading.
formal=[5,7,8,9,10,16,23,32,33,34,35,36,38,39,40,41,44,45]
proof=[1,4,6,11,12,13,14,15,17,18,19,20,21,22,24,26,27,28,30,31,37,42,43,46,51,52,54,55,56]
targeted=[2,3,25,29,47,48,49,50,53]
for n in formal:
 ev(f'CL-SA02-{n:03}','computation or formal certificate',cs[n]['computation'])
for n in proof:
 ev(f'CL-SA02-{n:03}','independent re-proof',cs[n]['computation'])
for n in targeted:
 ev(f'CL-SA02-{n:03}','targeted proof check',cs[n]['computation'])
for n,refined in [(16,'CL-SA02-052'),(28,'CL-SA02-056'),(33,'CL-SA02-032'),(35,'CL-SA02-036'),(41,'CL-SA02-038'),(45,'CL-SA02-031')]:
 ev(f'CL-SA02-{n:03}','refuted, with the refined statement\'s id','Literal or conditional broad reading fails as recorded in the explicit counterexample. Refined or narrowed statement: '+refined+'. No scan reading changed.')
for n in sorted(cs):
 ev(f'CL-SA02-{n:03}','used and rechecked in this run','Literature hypotheses compared against the claim; see claim_searches.tsv and reference_checks.md. Class '+cs[n]['class']+' is a bounded literature judgment, not a priority claim. '+cs[n]['fate'])
ev('CL-SA02-703','targeted proof check','Independent check of root proofs.md P03: F2(t) dual-number norm a² makes t x² primitive, and x²=t^−1 has no solution over a separable algebraic extension but does over a finite free purely inseparable extension. The fppf/étale distinction is sound.')
ev('CL-SA02-729','targeted proof check','Independent check of root P03: in characteristic2 dual numbers, conjugation is identity, so u/bar(u)=1 but every1+bε has norm1. The unrestricted Hilbert90-like surjection fails.')
for n in [713,714]:
 ev(f'CL-SA02-{n}','targeted proof check','Independent check of root P07: tangent functor2M∩M[2] is not left exact on0→M[2]→M→2M→0 forM=A/4A when2 is nonzero and nonunit. For parity-congruent roots, useδ=T²+4c and finite free x²+Tx−c=0, z=T+2x; this ensures the root satisfies the congruence.')
with(P/'CHECK_EVENTS.tsv').open('w')as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print('Wrote',len(events),'check events with explicitly scoped event types')
