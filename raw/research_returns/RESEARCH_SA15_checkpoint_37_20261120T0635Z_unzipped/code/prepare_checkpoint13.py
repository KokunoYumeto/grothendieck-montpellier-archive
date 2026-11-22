"""Integrate only promoted CP13 mathematics and build the reviewable paper."""
from pathlib import Path
import subprocess,sys,json,datetime,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=[
 'agents/obstructions_crystals/A3_ordinary_arbitrary_embedding.tex',
 'agents/obstructions_crystals/A3_supersingular_all_rectangular_ranks.tex',
 'agents/monodromy/supersingular_global_tangent_triples.tex',
 'agents/monodromy/supersingular_level3_collision_reduction.tex',
 'agents/monodromy/supersingular_uniform_contact.tex',
 'agents/monodromy/supersingular_uniform_source_smoothness.tex',
 'agents/reduction_descent/B_height_two_scalar_residual_gate.tex',
 'agents/reduction_descent/B_height_two_c4_residual_gate.tex']
for rel in required:
    text=(w/rel).read_text()
    assert '\\status{Candidate' not in text, rel
def run(name):
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current13.py',
             'build_paper.py']:
    run(name)
for name in ['build_summary.json','build_console.txt']:
    dest=w/'outputs'/('checkpoint13_initial_'+name)
    assert not dest.exists()
    shutil.copy2(w/'outputs'/name,dest)
run('merge_registers.py');run('update_current13.py')
print(json.dumps({'initial_integration_started_utc':stamp,
                  'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'promoted_files':required},indent=2))
