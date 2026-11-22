from pathlib import Path
import hashlib,json,itertools
base=Path('RESEARCH_SA15_work/agents/reduction_descent'); mono=base.parent/'monodromy'
author=mono/'outputs/ppav_supersingular_polar_uniform_lie.json'; before=hashlib.sha256(author.read_bytes()).hexdigest()
src=mono/'code/ppav_supersingular_polar_uniform_lie.py'; own=base/'code/independent_author_ppav_supersingular_polar_uniform_lie.py';own.write_bytes(src.read_bytes())
exec(compile(own.read_text(),str(own),'exec'),{'__file__':str(own.resolve()),'__name__':'__main__'})
assert hashlib.sha256(author.read_bytes()).hexdigest()==before
out=json.loads((base/'outputs/ppav_supersingular_polar_uniform_lie.json').read_text());assert out['unit_pivot_count']==81 and out['remaining_columns']==[] and out['remaining_rows']==[list(itertools.combinations(range(9),3)).index(tuple(int(i)-1 for i in t)) for t in ['467','478','578']]+[84]
