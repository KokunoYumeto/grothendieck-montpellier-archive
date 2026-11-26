"""Reproduce all original blind comparisons, then check corrective source-ledger decisions."""
from pathlib import Path
from tempfile import TemporaryDirectory
import csv,runpy,subprocess,sys
ROOT=Path(__file__).resolve().parent
TAG='K62-05'
def field(s):return s.replace('|',r'\|')
def main():
    verifier=runpy.run_path(str(ROOT/(TAG+'_verify.py')))
    with TemporaryDirectory() as tmp:
        old=Path(tmp);verifier['restore'](old)
        subprocess.run([sys.executable,'-B',str(old/(TAG+'_blind_compare.py'))],check=True)
        inherited=(old/(TAG+'_blind_compare.md')).read_text(encoding='utf-8').strip()
    lines=['# Blind readings and their comparison','',
      'The first table gives the corrective decisions on independent image readings. The full pre-comparison text and reconciliation for every scan appear in the audit. The original 210 localized readings and their contemporary two-stage report follow unchanged below. The first 33 corrective decisions led to the image-only freeze; the two slash-tag decisions followed visual comparison with the final original packet. One of the first 33 places, étant on scan 034, was subsequently resolved in the witness pass.','',
      '| Scan | Locus | Original page | Corrective current text | Source decision |','|---|---|---|---|---|']
    with (ROOT/'reaudit'/'current-decisions.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
    for r in rows:
        scan=int(r['scan']); name=f'{TAG}_62_scan{scan:03}.tex'
        current=(ROOT/'pages'/name).read_text(encoding='utf-8')
        assert r['final_tex'] in current,(scan,r['locus'])
        note=ROOT/'reaudit'/f'{scan:03}_before_comparison.md'
        assert note.is_file()
        lines.append('| '+' | '.join(field(s) for s in [r['scan'],r['locus'],'`'+r['old_tex']+'`','`'+r['final_tex']+'`',r['ink_and_context']+' ('+r['crop']+')'])+' |')
    lines+=['','Scans 029 and 035 retain their initial comparison text in full.','',inherited]
    (ROOT/(TAG+'_blind_compare.md')).write_bytes(('\n'.join(lines)+'\n').encode())
    print(f'PASS: {len(rows)} corrective decisions and all original localized comparisons reproduced.')
if __name__=='__main__':main()
