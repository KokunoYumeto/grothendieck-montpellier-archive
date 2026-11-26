"""Compare independent ink entries to first-pass page text. Run in the out folder.
The two optional deltas reverse later editorial changes before comparison.
The decisions table records human alignments at non-identical loci.
"""
from pathlib import Path
import csv,re,sys,difflib,subprocess,tempfile,shutil
from collections import defaultdict
root=Path(__file__).resolve().parent
def table(name):
 with (root/name).open(newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
def words(s):
 s=re.sub(r'\\(?:textcircled|text|mathcal|mathbb|uline|uuline|unsure|deleted|inserted|margin|underline|operatorname|begin|end|aligned|textnormal)\b',' ',s)
 return re.findall(r'[^\W_]+',s.casefold().replace('’',"'"),re.U)
def original_pages(folder):
 if len(sys.argv)>1:
  return Path(sys.argv[1]).resolve()
 p=folder/'pages'; shutil.copytree(root/'pages',p)
 for name in ('K68-01_reverse_witness.patch','K68-01_reverse_audit.patch'):
  patch=root/name
  if patch.exists() and patch.stat().st_size:
   subprocess.run(['patch','-s','-p0','-i',str(patch)],cwd=folder,check=True)
 return p
def escape(s): return s.replace('|','\\|').replace('\n',' ')
with tempfile.TemporaryDirectory() as d:
 pages=original_pages(Path(d))
 blind=table('K68-01_blind.tsv'); choices=table('K68-01_blind_decisions.tsv')
 choices_at={(r['scan'],r['place']):r for r in choices}
 report=['# Blind reading compared with the first pass','',f'{len(blind)} independent entries. The comparison first restores the page state that preceded the blind reading. A shared run of words or symbols locates an entry; brackets, case and editorial markup are ignored for alignment. The recorded ink decisions below are authoritative for the reading. A short anchor is not evidence for unaligned neighbouring letters.','','## Differences and settlements','','|Scan|Place|Blind ink|First-pass anchor|Decision on the image|','|---|---|---|---|---|']
 checks=[]; seen=set()
 for r in blind+[{'scan':a,'place':b,'what the crop shows':'Additional observation in the blind word list or page rereading'} for a,b in choices_at if not any(z['scan']==a and z['place']==b for z in blind)]:
  n=r['scan']; k=r['place']; ink=r['what the crop shows']
  page=(pages/f'K68-01_68_scan{int(n):03}.tex').read_text()
  pw=words(page); bw=words(ink); block=difflib.SequenceMatcher(None,bw,pw,autojunk=False).find_longest_match()
  anchor=' '.join(pw[block.b:block.b+block.size])
  decision=choices_at.get((n,k))
  if decision:
   old=decision['first-pass anchor']
   if old and ' '.join(old.split()) not in ' '.join(page.split()): sys.exit(f'First-pass anchor missing: {n} {k} {old}')
   seen.add((n,k)); report.append('| '+' | '.join(map(escape,(n,k,ink,old,decision['settlement'])))+' |')
  else:
   checks.append('| '+' | '.join(map(escape,(n,k,anchor or 'graphic / numeral, checked visually')))+' |')
 if seen!=set(choices_at): sys.exit('Uncompared decisions')
 report+=['','## Aligned entries with no remaining difference','','|Scan|Place|Shared first-pass anchor|','|---|---|---|']+checks
 (root/'K68-01_blind_compare.md').write_text('\n'.join(report)+'\n')
 print(len(blind),'blind entries;',len(choices),'recorded differences.')
