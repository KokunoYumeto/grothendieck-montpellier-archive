"""Integrate only audited promotions, preserving actual build inputs and outcomes."""
from pathlib import Path
import subprocess, sys, json, datetime, shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=['agents/monodromy/mixed_three_by_b_strip_groups.tex',
          'agents/reduction_descent/B_tame_CM_gate.tex',
          'agents/reduction_descent/B_tame_residual_cycle.tex',
          'agents/obstructions_crystals/A3_mixed_positive_index_pencil.tex']
for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current19.py']:
    run(name)
folder=w/'outputs/checkpoint19_build_attempt01'
assert not folder.exists()
folder.mkdir()
shutil.copytree(w/'sections',folder/'sections')
for name in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_references.bib']:
    shutil.copy2(w/name,folder/name)
result=subprocess.run([sys.executable,str(w/'code/build_paper.py')],cwd=w)
for rel in ['outputs/build_summary.json','outputs/build_console.txt',
            'RESEARCH_SA15_paper.log','RESEARCH_SA15_paper.aux']:
    if (w/rel).exists():shutil.copy2(w/rel,folder/Path(rel).name)
if result.returncode:
    if (w/'outputs/build_failure.json').exists():
        shutil.copy2(w/'outputs/build_failure.json',folder/'build_failure.json')
else:
    for name in ['build_summary.json','build_console.txt']:
        dest=w/'outputs'/('checkpoint19_initial_'+name)
        assert not dest.exists()
        shutil.copy2(w/'outputs'/name,dest)
    run('merge_registers.py');run('update_current19.py')
record={'initial_integration_started_utc':stamp,
        'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'promoted_files':required,'build_exit_code':result.returncode,
        'actual_build_snapshot':str(folder.relative_to(w))}
(w/'outputs/checkpoint19_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
raise SystemExit(result.returncode)
