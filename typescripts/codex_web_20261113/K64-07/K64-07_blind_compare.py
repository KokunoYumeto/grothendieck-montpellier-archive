"""Reproduce the blind concordance from the TSV records and the delivered pages."""
from pathlib import Path
import csv
from html import escape
import re

ID='K64-07'
fields=['scan','place','first_pass_excerpt','audit_excerpt','present_page_excerpt','resolution']
def norm(text):
    """Compare first candidates, retaining indices, accents, signs and all state marks."""
    while r'\unsure{' in text:
        start=text.rfind(r'\unsure{')
        begin=start+len(r'\unsure{')
        i=begin; depth=1
        while i<len(text) and depth:
            if text[i]=='{' and text[i-1]!='\\':depth+=1
            elif text[i]=='}' and text[i-1]!='\\':depth-=1
            i+=1
        text=text[:start]+text[begin:i-1].split('|')[0]+text[i:]
    text=re.sub(r'\\(mathbb|mathrm|mathcal|mathfrak|underline|widetilde)\s*\{([a-zA-Z])\}',r'\\\1 \2',text)
    text=re.sub(r'([_^])\{([a-zA-Z0-9*])\}',r'\1\2',text)
    text=re.sub(r'\\(underline|mathcal|mathbb|mathfrak)\{(\\[A-Za-z]+)\}',r'\\\1\2',text)
    text=re.sub(r'\$([0-9]+)\$',r'\1',text)
    text=re.sub(r'([_^])\{(\\[A-Za-z]+)\}',r'\1\2',text)
    for space in (r'\,',r'\;',r'\:',r'\!','\\ '):
        text=text.replace(space,'')
    return ''.join(text.replace('~',' ').split())
def tsv(path):
    with path.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def cell(s):return s.replace('|','&#124;').replace('\n',' ')
def compare(folder):
    blind={(r['scan'],r['place']):r['what_the_crop_shows'] for r in tsv(folder/f'{ID}_blind.tsv')}
    rows=tsv(folder/f'{ID}_blind_targets.tsv')
    if len({(r['scan'],r['place']) for r in rows})!=len(rows):raise ValueError('Duplicate locator')
    lines=[]; pages={}
    for r in rows:
        scan=r['scan']; place=r['place']; original=r['first_pass_excerpt']; b=blind[scan,place]
        if scan not in pages:pages[scan]=norm((folder/'pages'/f'{ID}_64_scan{int(scan):03d}.tex').read_text(encoding='utf-8'))
        if norm(r['present_page_excerpt']) not in pages[scan]:raise ValueError(f'Unmatched final passage {scan} {place}')
        if norm(b)!=norm(original):
            excerpts = [original, b, r['audit_excerpt'], r['present_page_excerpt']]
            cells = [cell(scan), cell(place)]
            cells += ['<code>'+cell(escape(t,quote=False))+'</code>' for t in excerpts]
            cells.append(cell(r['resolution']))
            lines.append('| '+' | '.join(cells)+' |')
    md=['# Blind comparison','',f'{len(rows)} located readings compared. {len(lines)} differ from the first pass.','', 'The original and audit excerpts are retained in the alignment TSV. The script also locates every accepted excerpt in the delivered page. The table gives the blind-audit decision and the excerpt after the subsequent witness check. It compares the first candidate inside an uncertainty mark and ignores LaTeX spacing and equivalent single-letter grouping.','', '| Scan | Place | First pass | Blind reading | Reading after audit | Delivered excerpt | Decision in the blind audit |','|---|---|---|---|---|---|---|',*lines]
    (folder/f'{ID}_blind_compare.md').write_text('\n'.join(md)+'\n',encoding='utf-8',newline='\n')
    return len(lines)
if __name__=='__main__':print(compare(Path(__file__).resolve().parent))

