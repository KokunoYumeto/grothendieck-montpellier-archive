from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parents[1];mono=base.parent/'monodromy'
author=mono/'outputs/ppav_two_rank_one_polar_uniform_minor.json';before=hashlib.sha256(author.read_bytes()).hexdigest()
src=mono/'code/ppav_two_rank_one_polar_uniform_minor.py';own=base/'code/independent_author_ppav_two_rank_one_polar_uniform_minor.py';own.write_bytes(src.read_bytes())
exec(compile(own.read_text(),str(own),'exec'),{'__file__':str(own),'__name__':'__main__'})
assert hashlib.sha256(author.read_bytes()).hexdigest()==before
out=json.loads((base/'outputs/ppav_two_rank_one_polar_uniform_minor.json').read_text())
assert out['unit_pivot_count']==77 and out['full_81_minor']=='b^4'
assert out['deleted_original_triples']==[[1,2,3],[3,4,5],[3,5,6]]
