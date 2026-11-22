"""Integrate only promoted CP17 proofs and retain the actual build records."""
from pathlib import Path
import subprocess,sys,json,datetime,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=['agents/monodromy/generic_nonordinary_ppav_groups.tex',
          'agents/monodromy/mixed_degree_one_uniform_full_groups.tex',
          'agents/obstructions_crystals/A3_mixed_positive_index_variation.tex',
          'agents/reduction_descent/B_tame_minimal_height_two.tex']
for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current17.py','build_paper.py']:
    run(name)
for name in ['build_summary.json','build_console.txt']:
    dest=w/'outputs'/('checkpoint17_initial_'+name)
    assert not dest.exists()
    shutil.copy2(w/'outputs'/name,dest)
run('merge_registers.py');run('update_current17.py')
print(json.dumps({'initial_integration_started_utc':stamp,
                  'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'promoted_files':required},indent=2))
