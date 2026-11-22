"""Build the two fully audited late CP19 promotions; retain both build histories."""
from pathlib import Path
import subprocess,sys,shutil,json,datetime
w=Path(__file__).resolve().parents[1]
for rel in ['agents/monodromy/mixed_degree_three_norm_groups.tex','agents/reduction_descent/B_tame_CM_neighborhood.tex']:
    assert (w/rel).exists() and '\\status{Candidate' not in (w/rel).read_text(),rel
for name in ['consolidate.py','number_statements.py','merge_registers.py','source_census.py','export_agent_programs.py','update_current19.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
folder=w/'outputs/checkpoint19_build_attempt02';assert not folder.exists();folder.mkdir()
shutil.copytree(w/'sections',folder/'sections')
for name in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_references.bib']:
    shutil.copy2(w/name,folder/name)
result=subprocess.run([sys.executable,str(w/'code/build_paper.py')],cwd=w)
for rel in ['outputs/build_summary.json','outputs/build_console.txt','RESEARCH_SA15_paper.log','RESEARCH_SA15_paper.aux']:
    if (w/rel).exists():shutil.copy2(w/rel,folder/Path(rel).name)
if result.returncode and (w/'outputs/build_failure.json').exists():
    shutil.copy2(w/'outputs/build_failure.json',folder/'build_failure.json')
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'build_exit_code':result.returncode,'snapshot':str(folder.relative_to(w))}
(w/'outputs/checkpoint19_addendum_build.json').write_text(json.dumps(record,indent=2)+'\n')
if not result.returncode:
    for name in ['merge_registers.py','update_current19.py','verify_program_paths19.py']:
        subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
print(json.dumps(record,indent=2));raise SystemExit(result.returncode)
