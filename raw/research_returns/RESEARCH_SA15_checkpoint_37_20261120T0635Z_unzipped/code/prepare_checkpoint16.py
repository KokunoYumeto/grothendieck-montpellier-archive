"""Integrate promoted CP16 results and retain the actual initial build records."""
from pathlib import Path
import subprocess, sys, json, datetime, shutil
w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
required = [
 'agents/obstructions_crystals/A3_mixed_thin_strip_residues.tex',
 'agents/obstructions_crystals/A3_mixed_positive_index_bounds.tex',
 'agents/monodromy/supersingular_even_image_sheaf.tex',
 'agents/monodromy/supersingular_all_even_groups.tex',
 'agents/monodromy/generic_mixed_product_all_groups.tex',
 'agents/reduction_descent/B_p2_height_two_mixed_gate.tex',
 'agents/reduction_descent/B_p2_height_two_log_gate.tex',
 'agents/reduction_descent/B_p2_residual_trivial_gate.tex',
 'agents/reduction_descent/B_p2_residual_c2_gate.tex',
 'agents/reduction_descent/B_p2_residual_c3_final.tex']
for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(), rel
def run(name):
    subprocess.run([sys.executable, str(w/'code'/name)], check=True, cwd=w)
for name in ['consolidate.py', 'number_statements.py', 'merge_registers.py',
             'source_census.py', 'export_agent_programs.py', 'update_current16.py', 'build_paper.py']:
    run(name)
for name in ['build_summary.json', 'build_console.txt']:
    dest = w/'outputs'/('checkpoint16_initial_'+name)
    assert not dest.exists()
    shutil.copy2(w/'outputs'/name, dest)
run('merge_registers.py')
run('update_current16.py')
print(json.dumps({'initial_integration_started_utc':stamp,
                  'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'promoted_files':required}, indent=2))
