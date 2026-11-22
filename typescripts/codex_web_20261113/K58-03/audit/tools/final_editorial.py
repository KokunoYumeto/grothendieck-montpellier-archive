from pathlib import Path
from collections import defaultdict
import csv,re,datetime,shutil
root=Path('out')
p=root/'K58-03_mathnotes.md';notes=p.read_text()
notes=notes.replace('quotienting the index by the indicated loss of \\(n\\) gives','subtracting the indicated \\(n\\) generators from the index gives')
notes=notes.replace('## What the pages do','All scan references are to the supplied facsimiles of Montpellier, fonds Alexandre Grothendieck, cote 58. The archival order interleaves manuscript leaves with two separate typescripts.\n\n## What the pages do')
p.write_text(notes)
p=root/'K58-03_notes.md';s=p.read_text()
s=s.replace('- **25.** “une réduction facile (?)”','- **25.** “Le lemme 4 nous ramène alors à vérifier le / Lemme 5” introduces the local task that the next leaves take up. “une réduction facile (?)”')
s=s.replace('The abbreviation for the condition is difficult to distinguish.','The abbreviation for the condition is difficult to distinguish. Higher on the leaf, “inutile” stands beside the inserted degree-\\(n+1\\) clause.')
s=s.replace('“Couples de Lefschetz-Grauert”, (X,Y)','“Couples” or “Couple de Lefschetz-Grauert”, followed by a pair whose first letter reads x or X')
s+= '\nFaint fragments of the paper watermark, identified in the supplied archival instructions as “EXTRA STRONG”, and reversed lettering from the opposite face are visible on the manuscript leaves. The legible mathematical text is on the writing face.\n'
p.write_text(s)
p=root/'K58-03_audit.md';s=p.read_text()
s=s.replace('The blind comparison retains the original page sources separately.','The blind comparison retains the original page sources separately. Each timed section preserves its contemporary decisions. The supplementary entries and the witness table identify subsequent refinements. The index lines were checked against the final positional register, excluding letters inside LaTeX command names.')
s=s.replace("The page ends at d'où une.",'At this stage the last group was provisionally read as d’où une. The dated supplementary crop comparison and the later witness check supersede that reading.')
indexed=defaultdict(list)
for r in csv.DictReader((root/'audit/indexed_i_j.tsv').open(),delimiter='\t'):indexed[r['scan']].append(r)
scan=None;out=[]
for line in s.splitlines():
 m=re.match(r'^## Scan (\d+)\s*$',line)
 if m:scan=m[1]
 if line.startswith('**Indexed or raised i and j.**'):
  regs=indexed[scan]
  line='**Indexed or raised i and j.** '+(' · '.join('formula '+r['formula ordinal']+', '+r['position']+' '+r['letter']+' in '+chr(96)+r['script content']+chr(96) for r in regs) if regs else 'None.')
 out.append(line)
s='\n'.join(out)+'\n';p.write_text(s)
p=root/'K58-03_hand_log.md';s=p.read_text().replace('The comma of (X,Y) descends as a short vertical stroke.','The comma between the two letters descends as a short vertical stroke. The first crossed letter is shorter than Y and its case is open.')
p.write_text(s)
who='GPT-6.2 Astra at reasoning effort max (ChatGPT Work), run K58-03'
date=datetime.datetime.now(datetime.timezone.utc).date().isoformat()
events=[
('S20-colon (Slips, scan 20)','used and rechecked in this run','The domain and codomain on the leaf make the composition of the barred extension with lambda inverse a map V to W. The visible two-dot operator remains in the transcription.'),
('S27-local-indices (What the pages do, scans 25 and 27)','computation or formal certificate','Substituted K=n+k in the two displayed index relations. Both differences simplify to zero. The local theorem itself was transcribed.'),
('M1 (Remarks of the model, scan 27)','computation or formal certificate','Symbolic integer calculation with n and k verifies K−n=k under K=n+k. The obscured replacement bound in the hyperplane corollary was not used.'),
('S34-boundary-degrees (What the pages do, Remarque 2)','used and rechecked in this run','The display on 34 has isom for i≤n and inj for i=n+1. Compared it with the two degree cases named below the diagram on 35.'),
('S35-central-degrees (What the pages do, induction)','computation or formal certificate','Substitution at i=n−1 and i=n in i+1 gives n and n+1 in the central column. This checks the indices alone.'),
('M2 (Remarks of the model, scans 34 and 35)','used and rechecked in this run','Compared the central exponents in the diagram, the two cases, and the criterion on the preceding sheet.'),
('M2 (Remarks of the model, scans 34 and 35)','computation or formal certificate','The two symbolic specializations of i+1 agree with the boundary degrees. Output in audit/degree_checks.tsv.')]
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 wr=csv.writer(f,delimiter='\t');wr.writerow(['statement id','date','who','type','outcome'])
 for name,kind,outcome in events:wr.writerow([name,date,who,kind,outcome])
for name in ['witness_crops.py','witness_register.py','mkwitness_panels.py','grid.py']:
 shutil.copyfile('work/'+name,root/'audit/tools'/name)
