"""Integrate the promoted CP14 results and build the complete paper."""
from pathlib import Path
import subprocess, sys, json, datetime, shutil
w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
required = [
    'agents/obstructions_crystals/A3_mixed_all_product_ranks.tex',
    'agents/obstructions_crystals/A3_mixed_nonproduct_ranks.tex',
    'agents/monodromy/supersingular_uniform_collision_exclusion.tex',
    'agents/reduction_descent/B_height_two_c3_residual_gate.tex',
    'agents/reduction_descent/B_height_two_c4_orientation_gate.tex',
    'agents/reduction_descent/B_height_two_c3_quotient_exclusion.tex',
    'agents/reduction_descent/B_height_two_c4_final_exclusion.tex']
for rel in required:
    text = (w / rel).read_text()
    assert '\\status{Candidate' not in text, rel
def run(name):
    subprocess.run([sys.executable, str(w / 'code' / name)], check=True, cwd=w)
for name in ['consolidate.py', 'number_statements.py', 'merge_registers.py',
             'source_census.py', 'export_agent_programs.py', 'update_current14.py',
             'build_paper.py']:
    run(name)
for name in ['build_summary.json', 'build_console.txt']:
    dest = w / 'outputs' / ('checkpoint14_initial_' + name)
    assert not dest.exists()
    shutil.copy2(w / 'outputs' / name, dest)
run('merge_registers.py')
run('update_current14.py')
print(json.dumps({'initial_integration_started_utc': stamp,
                  'complete_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'promoted_files': required}, indent=2))
