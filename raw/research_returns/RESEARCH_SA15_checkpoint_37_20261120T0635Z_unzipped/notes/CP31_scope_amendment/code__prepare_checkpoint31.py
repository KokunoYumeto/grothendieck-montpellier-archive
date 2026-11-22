"""Integrate audited CP31 promotions, preserving each actual build attempt."""
from pathlib import Path
import subprocess,sys,json,datetime,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
required=['agents/reduction_descent/B_first_wild_diagonal_projection.tex', 'agents/reduction_descent/B_first_wild_cyclotomic_quotient.tex', 'sections/A_theta_torsion_avoidance.tex', 'agents/monodromy/principal_theta_Cartier_bridge.tex', 'agents/obstructions_crystals/A4_Moore_singular_parameters.tex', 'agents/monodromy/ppav_twisted_Cartier_Moore.tex']
for optional in ['agents/reduction_descent/B_p5_tame_full_first_layer.tex']:
    p=w/optional
    if p.exists() and '\\status{Candidate' not in p.read_text():required.append(optional)

for rel in required:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
def run(name):subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
for name in ['consolidate.py','number_statements.py','merge_registers.py',
             'source_census.py','export_agent_programs.py','update_current31.py']:
    run(name)
attempt=1
while (w/f'outputs/checkpoint31_build_attempt{attempt:02d}').exists():attempt+=1
folder=w/f'outputs/checkpoint31_build_attempt{attempt:02d}'
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
    run('merge_registers.py');run('update_current31.py')
record={'integration_started_utc':stamp,
        'complete_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'promoted_files':required,'build_exit_code':result.returncode,
        'actual_build_snapshot':str(folder.relative_to(w)),'attempt':attempt}
dest=w/f'outputs/checkpoint31_integration_attempt{attempt:02d}.json'
assert not dest.exists();dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));raise SystemExit(result.returncode)
