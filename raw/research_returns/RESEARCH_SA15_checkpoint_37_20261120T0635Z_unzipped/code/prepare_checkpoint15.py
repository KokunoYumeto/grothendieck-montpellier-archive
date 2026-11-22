"""Integrate only promoted CP15 results and retain its full build records."""
from pathlib import Path
import subprocess,sys,json,datetime,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=[
 'agents/obstructions_crystals/A4_contact_third_value_smoothness.tex',
 'agents/obstructions_crystals/A4_uniform_tangent_triple_type.tex',
 'agents/monodromy/supersingular_uniform_tangent_triples.tex',
 'agents/monodromy/supersingular_all_odd_groups.tex',
 'agents/reduction_descent/B_p2_character_level3.tex',
 'sections/A_mixed_six_three_seed.tex',
 'agents/obstructions_crystals/A3_mixed_axis_norms.tex']
for rel in required:
 assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current15.py','build_paper.py']:
 run(name)
for name in ['build_summary.json','build_console.txt']:
 dest=w/'outputs'/('checkpoint15_initial_'+name)
 assert not dest.exists()
 shutil.copy2(w/'outputs'/name,dest)
run('merge_registers.py');run('update_current15.py')
print(json.dumps({'initial_integration_started_utc':stamp,
                  'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'promoted_files':required},indent=2))
