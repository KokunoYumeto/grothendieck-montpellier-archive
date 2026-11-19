"""Read-only author-output-preserving reruns after checkpoint11."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,sys
w=Path(__file__).resolve().parents[1]
cases=[('agents/reduction_descent/code/verify_elliptic_inertia_conjugacy.py',
        'agents/reduction_descent/code/verify_elliptic_inertia_conjugacy.output.json',
        'outputs/root_verify_elliptic_inertia_conjugacy.json'),
       ('agents/reduction_descent/code/verify_discriminant_tame_character.py',
        'agents/reduction_descent/code/verify_discriminant_tame_character.output.json',
        'outputs/root_verify_discriminant_tame_character.json'),
       ('agents/obstructions_crystals/code/A3_ordinary_all_rank_checks.py',
        'agents/obstructions_crystals/code/A3_ordinary_all_rank_checks_output.json',
        'outputs/root_A3_ordinary_all_rank_checks.json')]
original=Path.write_text
for program,author_file,root_file in cases:
 if len(sys.argv)>1 and Path(program).name not in sys.argv[1:]:continue
 author=w/author_file;destination=w/root_file;before=author.read_bytes()
 def write(path,data,*args,**kwargs):
  if path.resolve()!=author.resolve():raise RuntimeError('Unexpected certificate write')
  return original(destination,data,*args,**kwargs)
 capture=io.StringIO()
 try:
  Path.write_text=write
  with redirect_stdout(capture):
   exec(compile((w/program).read_text(),str(w/program),'exec'),{'__name__':'__main__','__file__':str(w/program)})
 finally:Path.write_text=original
 assert author.read_bytes()==before
 (w/'outputs'/('root_'+Path(program).stem+'.stdout.txt')).write_text(capture.getvalue())
 result=json.loads(destination.read_text())
 print(json.dumps(dict(program=program,status=result.get('status'),elapsed_seconds=result.get('elapsed_seconds'),
                      full_output=root_file,author_output_preserved=True)))
