from pathlib import Path
import tarfile, subprocess
base=Path(__file__).resolve().parents[1]
ps=base/'sources'/'B_pursuing_stacks'
ps.mkdir(exist_ok=True)
with tarfile.open(base/'sources'/'B_pursuing_stacks_source.tar') as t:
    for m in t.getmembers():
        assert (ps/m.name).resolve().is_relative_to(ps.resolve())
    t.extractall(ps,filter='data')
print('Pursuing Stacks source files:',*[str(p.relative_to(ps)) for p in ps.rglob('*') if p.is_file()],sep='\n')
for name in ['B_may1970','B_steenrod_epstein1962']:
    subprocess.run(['pdftotext','-layout',str(base/'sources'/f'{name}.pdf'),str(base/'sources'/f'{name}.txt')],check=True)
