"""Integrate audited CP27 promotions, preserving each actual build attempt."""
from pathlib import Path
import subprocess,sys,json,datetime,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=['agents/reduction_descent/B_first_level_mixed_boundary.tex',
          'agents/reduction_descent/B_rational_high_line.tex',
          'agents/reduction_descent/B_iterated_high_quotient.tex']
required.extend(['agents/obstructions_crystals/A3_mixed_positive_index_unipotent.tex',
                 'agents/obstructions_crystals/A3_mixed_positive_index_boundary_kernel.tex'])
required.append('agents/monodromy/nonordinary_nine_theta_norm_transfer.tex')
required.append('agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex')
required.append('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex')
for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current27.py']:
    run(name)
attempt=1
while (w/f'outputs/checkpoint27_build_attempt{attempt:02d}').exists():attempt+=1
folder=w/f'outputs/checkpoint27_build_attempt{attempt:02d}'
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
    run('merge_registers.py');run('update_current27.py')
record={'integration_started_utc':stamp,
        'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'promoted_files':required,'build_exit_code':result.returncode,
        'actual_build_snapshot':str(folder.relative_to(w)),'attempt':attempt}
dest=w/f'outputs/checkpoint27_integration_attempt{attempt:02d}.json'
assert not dest.exists();dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));raise SystemExit(result.returncode)
