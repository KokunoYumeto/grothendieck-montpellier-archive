from pathlib import Path
from collections import Counter
import csv, importlib.util,sys,shutil
p=Path('out');sys.path.insert(0,str(p))
from tex_elements import arguments,stamp
rr=list(csv.DictReader((p/'audit/frozen_places.tsv').open(),delimiter='\t'))
checks={'20':'The two vertically separated marks between the maps in the last formula support the colon.','21':'The hypothesis, its grouping stroke, the oblique reference and the conclusion ending in absurde were compared.','22':'Checked the separate prime, brackets and edge loss and the position of the fibre insertion in the quotation.','23':'Two distinct left rules span different portions of the statement. The fibre dimension and its connectivity bound have different offsets.','24':'The grave accent in procèdera, the pen intersection and the paired indices were compared.','25':'Compared formellt, the pen rule and the bracketed marginal expansion with its insertion point.','26':'The heading, ring homomorphism, pen symbols in the displayed inclusion, and the parenthetical correction were checked.','27':'Reinspected the last bound on the large crop. The overwritten initial group before lieu does not disclose a complete replacement expression.','28':'Checked the case of the crossed letter in the last line and its relation to the larger Y.','30':'Two horizontal arms distinguish the prime-marked F in the insertion. The short shaft is visibly headless.','31':'The square bracket, n and upper inequality are on different writing levels. The bracket belongs around the restored bound.','32':'Checked the opening of Fermés against the heading of scan 33 and followed both marginal arrows back to their origin.','33':'The interlinear dans X has its own two letters at the end. The qualification at the second LG still has two plausible readings.','34':'Compared the star-like label and alpha, and the two arguments in the rotated note.','35':'Compared both ends of all horizontal shafts, both positions of the tilde labels and the hatted C/G at lower right.'}
sp=importlib.util.spec_from_file_location('blind_compare',p/'K58-03_blind_compare.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
tot,dx,pending=m.compare(p/'audit/first_pass');assert not pending
with (p/'K58-03_audit.md').open('a') as f:
 print('\n## Additional image comparisons before the freeze\n',file=f)
 for sn,obs in checks.items():print(f'- Scan {sn}. {obs}',file=f)
 print('\n## All localized blind differences and their disposition\n',file=f)
 print('The first-pass and independent readings are given in full in K58-03_blind_compare.md. The following is the decision register for the same places. Later supplementary readings above can further refine a decision.\n',file=f)
 print('| Scan | Place | Decision after visual comparison |\n|---|---|---|',file=f)
 for a,b,_,_,c in dx:print('| '+' | '.join(m.esc(t) for t in (a,b,c))+' |',file=f)
for path in sorted((p/'pages').glob('*.tex')):
 n=str(int(path.stem[-3:]));loc=[r for r in rr if r['scan']==n]
 terms=list(arguments(path.read_text(),{'unsure','illegible'}))
 assert [(x[2],x[3]) for x in terms]==[(r['type'],r['frozen reading']) for r in loc],n
 (p/'audit/frozen_pages').mkdir(exist_ok=True);shutil.copyfile(path,p/'audit/frozen_pages'/path.name)
for nm in ['apparatus.py','package.py','late_edit.py','refine_places.py','finishfreeze.py']:
 shutil.copyfile('work/'+nm,p/'audit/tools'/nm)
print(len(rr),tot,len(dx),len(pending))
