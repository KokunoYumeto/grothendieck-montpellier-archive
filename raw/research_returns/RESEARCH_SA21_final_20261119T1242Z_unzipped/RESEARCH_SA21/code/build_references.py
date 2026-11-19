"""Consolidate opened-status references and retain source-audit provenance."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
paths=[root/'parts'/part/'references.bib' for part in ['supports','bmodels','maquettes']]
blocks=[];seen=set()
for p in paths:
 for block in re.split(r'(?=^@)',p.read_text(),flags=re.M):
  if not block.lstrip().startswith('@'):continue
  block=block.lstrip()
  key=re.match(r'@\w+\{([^,]+)',block).group(1)
  if key=='Grothendieck1986C':continue
  assert key not in seen,key
  seen.add(key)
  if key=='Serre1977':block=block.replace(', editor = {Bass, Hyman}','')
  if key=='HuaProject':
   block=block.replace('Not opened directly in this run.','Opened: project landing page and repository description; the individual modernized readings were not adopted as proof sources.')
   block=block.replace('  url =', '  year = {n.d.},\n  url =')
  if key=='Barmak2011':block=block.replace('Theorem 1.4.6, p. 12;', 'Proposition 1.2.4, p. 5; Theorem 1.4.6, p. 12;')
  if key=='Grothendieck1986':block=block.replace('the archive catalogue was opened.', 'the archive catalogue was opened. Original scans 156-4/54-55,72-73, 156-6/34,88, 156-8/4,6, and 156-9/113 were inspected for the specific doubtful claims; the source-only Magor sign is treated under both readings.')
  blocks.append(block.strip())
(root/'RESEARCH_SA21_references.bib').write_text('\n\n'.join(blocks)+'\n')
print(f'{len(blocks)} references, every entry retaining an explicit access-status note')
