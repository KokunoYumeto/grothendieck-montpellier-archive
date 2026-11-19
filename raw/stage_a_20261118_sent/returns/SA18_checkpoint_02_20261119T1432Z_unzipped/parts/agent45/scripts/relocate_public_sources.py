"""Keep fetched public source material outside the deliverable directory."""
from pathlib import Path
import shutil,json
out=Path(__file__).resolve().parents[1]
source=out/'external';target=out.parents[2]/'public_sources'/'agent45'
target.mkdir(parents=True,exist_ok=True)
moved=[]
if source.exists():
    for p in source.iterdir():
        shutil.move(str(p),str(target/p.name));moved.append(p.name)
    source.rmdir()
print(json.dumps({'target':str(target),'moved':moved,'policy':'No fetched public PDF, text, or page image is part of the deliverable.'}))
