"""Execute estimate mode only and audit its preservation manifest."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time, zipfile

base=Path(__file__).resolve().parents[1]
program=base/'code/geometry_final_package.py'
estimate_path=base/'notes/geometry_final_package_estimate_cp04.json'
plan_path=base/'notes/geometry_final_package_plan_cp04.json'
argv=[sys.executable,str(program),'--estimate','--estimate-report',str(estimate_path),'--plan-report',str(plan_path)]
before=sorted(str(p) for p in base.parent.glob('*.zip'))
start=time.perf_counter()
run=subprocess.run(argv,capture_output=True,text=True)
elapsed=time.perf_counter()-start
(base/'logs/geometry_final_package_cp04_estimate_output.json').write_text(run.stdout)
(base/'logs/geometry_final_package_cp04_estimate_stderr.txt').write_text(run.stderr)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'activity':'packaging only; not mathematical movement','argv':argv,'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),'elapsed_seconds':elapsed,'returncode':run.returncode,'zip_paths_unchanged':before==sorted(str(p) for p in base.parent.glob('*.zip')),'archive_created':False,'formal_stopping_rule_evaluated':False}
if run.returncode==0:
 plan=json.loads(plan_path.read_text())
 estimate=json.loads(estimate_path.read_text())
 rows=plan['checkpoint_members']
 coverage=[]
 for checkpoint in plan['checkpoints']:
  number=checkpoint['checkpoint']
  with zipfile.ZipFile(base.parent/checkpoint['archive']) as archive:
   original=set(archive.namelist())
  mapped={r['original_member'] for r in rows if r['checkpoint']==number}
  coverage.append({'checkpoint':number,'archive_entries':len(original),'mapped_entries':len(mapped),'exact_entry_union':original==mapped,'mapped_logs':sum('/logs/' in r['original_member'] for r in rows if r['checkpoint']==number),'mapped_code':sum('/code/' in r['original_member'] for r in rows if r['checkpoint']==number)})
 current={r['path']:r for r in plan['current_files']}
 required=['RESEARCH_SA23_paper.tex','RESEARCH_SA23_paper.pdf','RESEARCH_SA23_results.csv','RESEARCH_SA23_references.bib','RESEARCH_SA23_report.md','PROGRESS_LEDGER.md','CHECK_EVENTS.tsv']
 aliases=[r for r in plan['current_files'] if not r['canonical_current_path']]
 omissions=plan['current_omissions']
 cache_files=[r for r in omissions if r['reason']=='retrievable_source_cache' and not r['path'].endswith('/')]
 record.update(estimate_created_utc=estimate['created_utc'],checkpoint_coverage=coverage,required_current_paths={p:current.get(p) for p in required},current_logs=sum(p.startswith('logs/') for p in current),current_code=sum(p.startswith('code/') for p in current),current_aliases=len(aliases),source_or_program_aliases=[r for r in aliases if r['path'].endswith(('.tex','.py','.sh'))],excluded_source_files=len(cache_files),excluded_source_files_with_hash=sum('sha256' in r for r in cache_files),omitted_files_changed_during_inventory=[r for r in omissions if r.get('changed_during_omission_inventory') or r.get('disappeared_during_plan')],estimated_total_archive_bytes=estimate['estimated_total_archive_bytes'],estimated_with_reserve_bytes=estimate['estimated_with_reserve_bytes'],headroom_with_reserve_bytes=estimate['delivery_limit_bytes']-estimate['estimated_with_reserve_bytes'],policy_conflicts=estimate['policy_conflicts'],files_changed_during_plan=estimate['files_changed_during_plan'],ledger_is_included='PROGRESS_LEDGER.md' in current,final_branch_run=False)
 record['manifest_mapping_checks_pass']=all(x['exact_entry_union'] for x in coverage) and all(p in current for p in required) and not record['policy_conflicts'] and not record['files_changed_during_plan']
else:
 record['stderr']=run.stderr
(base/'logs/geometry_final_package_cp04_audit.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
print(json.dumps(record,ensure_ascii=False,indent=2))
sys.exit(run.returncode)
