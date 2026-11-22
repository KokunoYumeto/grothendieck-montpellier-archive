from pathlib import Path
import csv,datetime,json,hashlib
root=Path(__file__).resolve().parents[1]
start=datetime.datetime.fromisoformat((root/'work/started_at.txt').read_text().strip())
now=datetime.datetime.now(datetime.timezone.utc)
statepath=root/'work/scheduled_reviews.json'
state=json.loads(statepath.read_text()) if statepath.exists() else []
number=len(state)+1
due=start+datetime.timedelta(hours=number+2)
if now<due:raise SystemExit('Scheduled review is not yet due; no review recorded.')
rows=list(csv.DictReader((root/'deliverables/QUESTIONS.tsv').open(),delimiter='\t'))
if number==1:
 movement=True
 basis='C44-A15/A15a strictly reduces the original universal fixed-axis gate: after any known positive cycle span, at most one residual potential Tate direction is now settled without Tate, D, semisimplicity or cycle lifting. For sixfold axes the remaining unconditioned cyclotomic multiplicity is at least3. C44-W01–W05 and W12–W13 also close the original characteristic-p TheoremW task with explicit corrected signature/lattice hypotheses and the stated unrefereed032/Milne2026 conditions. These are mathematical changes, not packaging.'
 additional='C06/C06a closes geometric lifting for every cover map and smooth incidence, but not cycle lifting. F15–F22 remove specified P18 families; the whole Fermat AJ5 finite-generation gate F07 is unchanged. The exact F07 criterion, arithmetic local countermodels, new positive subspaces, source audits and the Th5 compilation are not counted by themselves as movement. A18 constrained-centre moment work, if unfinished, remains pending and is not used in this review.'
else:
 assessments_path=root/'work/review_assessments.json'
 assessments=json.loads(assessments_path.read_text()) if assessments_path.exists() else {}
 assessment=assessments.get(str(number))
 if assessment is None:
  raise SystemExit('Later review requires an explicit assessment against the stored preceding snapshot; no review recorded.')
 prior_hash=hashlib.sha256(json.dumps(state[-1],sort_keys=True,ensure_ascii=False).encode()).hexdigest()
 if assessment.get('preceding_snapshot_sha256')!=prior_hash:
  raise SystemExit('Assessment does not identify the exact preceding review snapshot; no review recorded.')
 movement=assessment['movement']
 if not isinstance(movement,bool):raise SystemExit('Movement must be explicitly true or false.')
 basis=assessment['basis']
 additional=assessment['additional_scope']
streak=0 if movement else (state[-1]['no_movement_streak']+1 if state else 1)
record={'number':number,'scheduled_due':due.isoformat(),'actual_time':now.isoformat(),'movement':movement,'basis':basis,'additional_scope':additional,'no_movement_streak':streak,'rows':rows}
state.append(record);statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
lines=['\n## Scheduled gate review '+str(number)+'\n','Actual time: '+now.isoformat()+'. Scheduled due time: '+due.isoformat()+'.\n','Movement: **'+('YES' if movement else 'NO')+'**. Consecutive reviews without movement: **'+str(streak)+'**.\n',basis+'\n',additional+'\n','The register below snapshots every treated question. In particular every still-open original row retains its current strongest gate; auxiliary proved rows do not replace an unresolved original goal.\n','| Question | State at review | Strongest gate or completed result |\n|---|---|---|']
for r in rows:lines.append('| '+r['id']+' | '+r['state']+' | '+r['finding_ids_or_current_gate'].replace('|',' / ').replace('\n',' ')+' |')
if streak>=2:
 lines.append('\nDecision: stop the research and write the final package under the governing two-consecutive-no-movement rule. Every unresolved original row retains its gate above; stopping does not convert an open question into a proved result.\n')
else:
 lines.append('\nDecision: continue. The next formal review is due '+(start+datetime.timedelta(hours=number+3)).isoformat()+'. No stopping condition has been met.\n')
with (root/'deliverables/LEDGER.md').open('a') as f:f.write('\n'.join(lines))
print(json.dumps({'review':number,'time':now.isoformat(),'movement':movement,'no_movement_streak':streak,'rows':len(rows)}))
