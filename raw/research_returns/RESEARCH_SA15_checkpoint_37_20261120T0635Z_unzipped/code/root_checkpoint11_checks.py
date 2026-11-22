"""Root reruns with complete output retained and author files untouched."""
from pathlib import Path
from contextlib import redirect_stdout
import io, json, sys

w=Path(__file__).resolve().parents[1]
cases=[
 ('agents/monodromy/code/verify_supersingular_degree_two_group.py',
  'agents/monodromy/outputs/verify_supersingular_degree_two_group.json',
  'outputs/root_verify_supersingular_degree_two_group.json'),
 ('agents/monodromy/code/verify_supersingular_degree_three_group.py',
  'agents/monodromy/outputs/verify_supersingular_degree_three_group.json',
  'outputs/root_verify_supersingular_degree_three_group.json'),
 ('agents/obstructions_crystals/code/A3_ppav_rank_checks.py',
  'agents/obstructions_crystals/code/A3_ppav_rank_checks_output.json',
  'outputs/root_A3_ppav_rank_checks.json'),
 ('agents/obstructions_crystals/code/A3_separable_rank_checks.py',
  'agents/obstructions_crystals/code/A3_separable_rank_checks_output.json',
  'outputs/root_A3_separable_rank_checks.json'),
 ('agents/reduction_descent/code/verify_supersingular_log_bound.py',
  'agents/reduction_descent/code/verify_supersingular_log_bound.output.json',
  'outputs/root_verify_supersingular_log_bound.json'),
]
write_text_original=Path.write_text
for program,author_file,root_file in cases:
    if len(sys.argv)>1 and Path(program).name not in sys.argv[1:]: continue
    author=w/author_file; destination=w/root_file
    prior=author.read_bytes()
    def redirected_write(path,data,*args,**kwargs):
        if path.resolve()!=author.resolve():
            raise RuntimeError('Unexpected write in certificate: '+str(path))
        return write_text_original(destination,data,*args,**kwargs)
    capture=io.StringIO()
    try:
        Path.write_text=redirected_write
        with redirect_stdout(capture):
            exec(compile((w/program).read_text(),str(w/program),'exec'),
                 {'__name__':'__main__','__file__':str(w/program)})
    finally:
        Path.write_text=write_text_original
    assert author.read_bytes()==prior
    result=json.loads(destination.read_text())
    (w/'outputs'/('root_'+Path(program).stem+'.stdout.txt')).write_text(capture.getvalue())
    print(json.dumps(dict(program=program,root_output=root_file,status=result.get('status'),
                         seconds=result.get('runtime_seconds',result.get('elapsed_seconds')),
                         author_output_preserved=True)))
