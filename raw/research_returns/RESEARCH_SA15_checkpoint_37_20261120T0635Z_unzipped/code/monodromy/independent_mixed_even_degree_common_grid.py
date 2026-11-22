"""Author-preserving rerun of the root's exact even-grid certificate."""
from pathlib import Path
import hashlib, json

agent=Path(__file__).resolve().parents[1]
work=agent.parents[1]
source=work/'code/mixed_even_degree_common_grid.py'
author=work/'outputs/mixed_even_degree_common_grid.json'
target=agent/'outputs/independent_mixed_even_degree_common_grid.json'
source_bytes=source.read_bytes(); author_bytes=author.read_bytes()
old="dest=w/'outputs/mixed_even_degree_common_grid.json'"
new='dest=Path('+repr(str(target))+')'
text=source_bytes.decode()
assert text.count(old)==1
exec(compile(text.replace(old,new),str(source),'exec'),
     {'__file__':str(source),'__name__':'__main__'})
assert source.read_bytes()==source_bytes
assert author.read_bytes()==author_bytes
out=json.loads(target.read_text())
out['author_sha256_preserved']=hashlib.sha256(author_bytes).hexdigest()
out['source_sha256_preserved']=hashlib.sha256(source_bytes).hexdigest()
out['audit_scope']='Entire original code read; output-only redirection; graph proof independently rederived; no geometric claim from finite cases.'
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'runtime_seconds':out['runtime_seconds'],
                  'author_sha256_preserved':out['author_sha256_preserved'],
                  'output':str(target)},indent=2))
