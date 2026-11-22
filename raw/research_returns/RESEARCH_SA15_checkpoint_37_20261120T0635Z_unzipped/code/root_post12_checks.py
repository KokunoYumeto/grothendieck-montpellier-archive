"""First root executions of newly used finite certificates after CP12."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/monodromy/code/supersingular_level3_kernel_orbits.py'
author=w/'agents/monodromy/outputs/supersingular_level3_kernel_orbits.json'
destination=w/'outputs/root_supersingular_level3_kernel_orbits.json'
assert not destination.exists(), 'Preserve the first root execution'
before=author.read_bytes();original=Path.write_text
def write(path,data,*args,**kwargs):
 if path.resolve()!=author.resolve():raise RuntimeError('Unexpected certificate write')
 return original(destination,data,*args,**kwargs)
capture=io.StringIO()
try:
 Path.write_text=write
 with redirect_stdout(capture):
  exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
finally:Path.write_text=original
assert author.read_bytes()==before
(w/'outputs/root_supersingular_level3_kernel_orbits.stdout.txt').write_text(capture.getvalue())
out=json.loads(destination.read_text())
print(json.dumps({k:out[k] for k in ['status','automorphism_group_order','affine_group_order','triple_orbits','elapsed_seconds']},indent=2))
