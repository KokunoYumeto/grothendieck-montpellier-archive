"""Independent reruns of the checkpoint10 finite certificates.

Keep the author's output intact and retain root output separately.  These
checks verify the stated finite algebra, not the geometric proofs.
"""
from pathlib import Path
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
PYTHON='/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3'
CASES=[
 ('agents/monodromy/code/level3_theta_tensor_checks.py',
  'agents/monodromy/outputs/level3_theta_tensor_checks.json',
  'outputs/root_level3_theta_tensor_checks.json'),
 ('agents/reduction_descent/code/verify_height_two_character_gate.py',
  'agents/reduction_descent/code/verify_height_two_character_gate.output.json',
  'outputs/root_verify_height_two_character_gate.json'),
 ('agents/obstructions_crystals/code/A3_mixed_generic_checks.py',
  'agents/obstructions_crystals/code/A3_mixed_generic_checks_output.json',
  'outputs/root_A3_mixed_generic_checks.json'),
 ('agents/monodromy/code/ordinary_ppav_group_checks.py',
  'agents/monodromy/outputs/ordinary_ppav_group_checks.json',
  'outputs/root_ordinary_ppav_group_checks.json'),
]
for program,author_output,root_output in CASES:
    if len(sys.argv)>1 and Path(program).name not in sys.argv[1:]:
        continue
    author=ROOT/author_output
    original=author.read_bytes()
    try:
        run=subprocess.run([PYTHON,str(ROOT/program)],cwd=ROOT,
                           capture_output=True,text=True,check=True)
        result=json.loads(run.stdout)
        (ROOT/root_output).write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'program':program,'root_output':root_output,
                          'result':result}))
    finally:
        author.write_bytes(original)
