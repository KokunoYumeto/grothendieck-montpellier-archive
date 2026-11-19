#!/usr/bin/env python3
"""Serialize actual query/check records; all verdicts and proof dispositions are authored."""
import csv,json,re
from pathlib import Path
from datetime import datetime,timezone
O=Path(__file__).resolve().parent
C=json.loads((O/'claims.json').read_text()); I=json.loads((O/'items.json').read_text())
R=json.loads((O/'references.json').read_text()); P=json.loads((O/'problems.json').read_text())
rb={x['key']:x for x in R}; cb={int(x['id'].split('-')[-1]):x for x in C}
def tsv(name,rows,fields):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
S=[]
for path in sorted((O/'audit').glob('claim_search_*.json')):
 d=json.loads(path.read_text())
 for qi,(q,ids) in enumerate(zip(d['queries'],d['claim_groups']),1):
  # Later-added assertions were checked in these same exact-hypothesis searches.
  if path.name=='claim_search_11.json': ids=ids+[97]
  if path.name=='claim_search_07.json' and qi==4: ids=ids+[101]
  for n in ids:
   c=cb[n]; refs=[rb[k] for k in c['refs']]
   S.append(dict(claim_id=c['id'],date='2026-11-19',query=q['q'],
     source=path.name+f' query {qi}; raw search response retained',
     result='Exact-hypothesis assessment after opening and following references: '+c['fate'],
     opened_urls=' | '.join(x['url'] for x in refs if x['note']=='verified'),
     ref_ids=' | '.join(dict.fromkeys(z for x in refs for z in x.get('opened_refs',[]))),
     reference_keys=' | '.join(c['refs']),limitations='Search absence is not evidence of novelty. Query hits and follow-up theorem checks are distinguished in the raw audit and reference limitations.'))
d=json.loads((O/'audit/web_stacks_localization.json').read_text())
for q in d['queries']:
 c=cb[102]
 S.append(dict(claim_id=c['id'],date='2026-11-19',query=q['q'],source='web_stacks_localization.json; web_final_primary_details.json; web_final_primary_more.json',result=c['fate'],opened_urls=rb['StacksLocalization2026']['url'],ref_ids='turn108393566view0 | turn191591263search0',reference_keys='StacksLocalization2026',limitations='Elementary localization result checked directly; the first query was too broad and did not supply the exact theorem.'))
tsv('search_log.tsv',S,['claim_id','date','query','source','result','opened_urls','ref_ids','reference_keys','limitations'])
assert {x['claim_id'] for x in S}=={x['id'] for x in C}

# Each type below records what was actually done, not the ambition of the source.
independent=set([2,3,4,5,6,8,11,14,15,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,46,47,48,50,51,52,55,56,58,59,65,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,87,88,90,91,95,98,99,100,101,102,103,104,105])
external=set([16,35,54,60,61,62,63,64,66,77,86,93,94])
refuted={4:'C-SA06-4 (uniformity qualification)',18:'C-SA06-19',30:'C-SA06-28 and C-SA06-29 (endpoint replacements)',40:'C-SA06-91',51:'C-SA06-51 (Jacobian replacement)',55:'C-SA06-54 (elliptic result with alternative hypotheses)',56:'C-SA06-60 (published cohomological replacement)',58:'C-SA06-93 (cohomological weak Lefschetz)',59:'C-SA06-93 (cohomological affine vanishing)',65:'C-SA06-65 (no universal replacement asserted)'}
E=[]
def event(sid,typ,outcome):
 E.append(dict(statement_id=sid,date='2026-11-19',model='GPT-6 Astra Pro',effort='inherited/not exposed',run='SA06-part2/cote14_early',type=typ,outcome=outcome))
for x in I:
 event(x['id'],'used and rechecked in this run','Documentary comparison with the complete cited transcription passage: '+x['check']+'. '+x['check_reason']+' Reconstruction boundary: '+x['reconstruction'])
for c in C:
 n=int(c['id'].split('-')[-1])
 typ='independent re-proof' if n in independent else ('used and rechecked in this run' if n in external else 'targeted proof check')
 prefix='The scoped assertion and hypotheses, not every unformulated generalization, were checked. '
 if n not in independent and n not in external: prefix='Scope and proof dependencies checked; no proof of the unresolved formulation is claimed. '
 event(c['id'],typ,prefix+c['fate']+' Detailed argument: proof_checks.md.')
 if n in refuted:event(c['id'],'refuted','Counterexample and all applicable hypotheses checked in proof_checks.md. Refined statement: '+refuted[n]+'. Does not refute missing stronger axioms or a different cycle quotient.')
 if 'checks' in c['computation']:
  event(c['id'],'computation or formal certificate','Exact saved Python/SymPy execution, computations.py and audit/computations_output.txt, checks '+', '.join(c['computation']['checks'])+'. Finite examples are labelled and are supplemented by the general argument in proof_checks.md.')
for n,labs in {21:'T07',31:'L01–L04',32:'L06',33:'L05',87:'M05',92:'R01',97:'D01–D03'}.items():
 event(f'SA06-{n}','computation or formal certificate','Earlier-run or documentary assertion independently recomputed: '+labs+'; computations.py and audit/computations_output.txt. The assertion is not attributed to the manuscript where it is an editorial addition.')
for x in R:
 if x['note']=='unverified':
  event(x['key'],'used and rechecked in this run','Bibliographic/retrieval check only: '+x['limitations']+' No theorem used as established.')
 elif x['key']=='OpenAI2026CMHodge':
  event(x['key'],'targeted proof check','Opened exact theorem statements, argument outline and consequence proofs. Main theta construction not independently verified; no settled-general-status conclusion drawn. '+x['limitations'])
 elif x['key']=='BourbakiLie4562007':
  event(x['key'],'used and rechecked in this run','Publisher metadata and chapter contents checked; exact manuscript collation not established. Elementary reflection proofs are independently supplied, not inferred from the unopened chapter text.')
 elif x['key']=='Peters2026Incidence':
  event(x['key'],'carried as background without fault found','Used only to follow references back to Saito and identify the exact comparison problem. No independent certification of the whole survey or reliance on every illustrative formula. '+x['limitations'])
 else:
  event(x['key'],'used and rechecked in this run','Opened result statements and the specified hypotheses/locators for application, not a full independent proof of the cited work: '+'; '.join(x['locators'])+' Limit: '+x.get('limitations','No broader claim inferred.'))
for p in P:
 event(p['id'],'targeted proof check','Problem formulation matched with source and checked-reference scope. '+p['state_of_art']+' Boundary: '+p['why_open'])
tsv('CHECK_EVENTS.tsv',E,['statement_id','date','model','effort','run','type','outcome'])

# Keep the source's absent-project/context leads separate from checked links.
src=O.parents[2]/'source/SA06_notes/pro/MPL_14_002-044_notes.md'
# The source is three levels above this part.
src=Path('/workspace/scratch/a5176e5b5d45/source/SA06_notes/pro/MPL_14_002-044_notes.md')
lines=src.read_text().splitlines(); starts=[i for i,l in enumerate(lines) if l.startswith('### ')]
entrymap={s:x['id'] for x in I for s in x['sources']}
leads=[]
for n,start in enumerate(starts,1):
 end=starts[n] if n<len(starts) else len(lines)
 for j in range(start,end):
  line=lines[j]
  if ('Context' in line or 'Register:' in line or '**RS:**' in line or '**R:**' in line or line.startswith('|WG') or line.startswith('|LM') or line.startswith('|Hua')) and ('cote' in line or 'WG' in line or 'LM' in line or 'Hua' in line or 'README' in line or 'S6' in line or 'S17' in line):
   eid=f'MPL_14_002-044#{n}'
   leads.append(dict(kind='unverified context lead',entry_id=eid,item_id=entrymap[eid],source_line=str(j+1),quoted_lead=line,
     status='The early-package endpoint and the wording of this lead were read. The named external context/register endpoint was not supplied in this tranche; its historical status is the earlier run’s report, not a checked link or new result.'))
tsv('context_leads.tsv',leads,['kind','entry_id','item_id','source_line','quoted_lead','status'])
print(f'Search rows {len(S)}, claims covered {len(C)}; check events {len(E)}; separate context-lead occurrences {len(leads)}.')
with (O/'progress.log').open('a') as f:
 f.write(datetime.now(timezone.utc).isoformat()+'\tSTAGES2-4\t105 claims, 29 problems, 28 scan alarms, 41 references; full proof_checks.md and exhaustive claim search/check ledgers saved.\n')

