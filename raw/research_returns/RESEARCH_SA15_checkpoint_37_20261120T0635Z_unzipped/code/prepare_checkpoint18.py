"""Integrate promoted CP18 proofs and preserve the first actual build records."""
from pathlib import Path
import subprocess, sys, json, datetime, shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=['agents/monodromy/mixed_degree_two_uniform_full_groups.tex',
          'agents/reduction_descent/B_tame_norm_square_boundary.tex',
          'agents/reduction_descent/B_tame_primitive_norm_orbits.tex']
for optional_name in ['A3_mixed_positive_index_bundles.tex','A3_mixed_positive_index_trace_radicals.tex']:
    optional=w/'agents/obstructions_crystals'/optional_name
    if optional.exists() and '\\status{Candidate' not in optional.read_text():
        required.append(str(optional.relative_to(w)))
for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current18.py','build_paper.py']:
    run(name)
for name in ['build_summary.json','build_console.txt']:
    dest=w/'outputs'/('checkpoint18_initial_'+name)
    assert not dest.exists()
    shutil.copy2(w/'outputs'/name,dest)
run('merge_registers.py')
run('update_current18.py')
record={'initial_integration_started_utc':stamp,
        'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'promoted_files':required}
(w/'outputs/checkpoint18_integration.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
