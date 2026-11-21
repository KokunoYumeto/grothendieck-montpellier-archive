"""Compare the independent readings with the original, audited and current page blocks."""
import csv,re,html,unicodedata
from pathlib import Path
R=Path(__file__).resolve().parent
def rows(s):
    with (R/f'K36-01_{s}.tsv').open() as f:return list(csv.DictReader(f,delimiter='\t'))
def cell(t):return '<code>'+html.escape(' '.join(t.split())).replace('|','&#124;')+'</code>'
def simple(t):
    t=unicodedata.normalize('NFC',t)
    t=re.sub(r'\\(?:qquad|quad|,|;|!|:| )',' ',t)
    t=re.sub(r'\\(?:mathrm|mathsf|operatorname|handwritten|inserted|uline|underline|text|mspage|unsure)\b','',t)
    return re.sub(r'[\s{}$]','',t)
def current(s):
    z=re.split(r'\n\n% ([^\n]+)\n',s);v={}
    for i in range(1,len(z),2):
        body='\n'.join(l for l in z[i+1].splitlines() if not l.startswith('%')).strip()
        if body.startswith(r'\hrule'):continue
        v[str(len(v)+1)]=body
    for key,pattern in [('M',r'\\mspage\{(.*?)\}'),('F',r'% archive sheet number: ([^\n]+)')]:
        m=re.search(pattern,s);v[key]=m[1] if m else ''
    return v
def run():
    blocks={(r['scan'],r['block']):r for r in rows('reading_blocks')}
    alignment={r['place_id']:r for r in rows('blind_alignment')}
    decisions=rows('blind_decisions');blind=rows('blind')
    report=['# Blind reading and visual collation','','The register contains independent notes made from the images before reopening each page. They use abbreviated descriptions for drawn arrows and superposition. The first table for each leaf lists the revised passages and the crop decisions, including readings deliberately retained against the blind observation. The alignment gives the adopted reading and locates its historical transcription for every independent entry. Multiple punctuation signs in a blind note sometimes just separate the objects observed. “Verbal or graphical comparison” means there is a literal difference or a difference of notation. The block register retains the two complete readings for inspection. The current page column detects any later witness change.','','Historical readings: K36-01_reading_blocks.tsv. Independent readings: K36-01_blind.tsv.']
    for tag in sorted({r['scan'] for r in blind}):
        pp=next((R/'pages').glob(f'*{tag}.tex'));now=current(pp.read_text());report+=['',f'## Scan {int(tag)}','']
        d=[x for x in decisions if x['scan']==tag]
        report+=[d[0]['ink_decision'],'','| First pass | Settled on the independent reading |','|---|---|']
        for x in d[1:]:report+=['| '+cell(x['before'])+' | '+cell(x['after'])+' |']
        if len(d)==1:report+=['| No change | Same reading on both passes |']
        report+=['','| Independent place | Physical block | Comparison with first pass | Change in block after visual reading | Decision from the crop | Current page vs. audited block |','|---|---|---|---|---|---|']
        for r in [y for y in blind if y['scan']==tag]:
            id=r['place'].split()[0];record=alignment[id];idx=record['physical_blocks'].split(',');items=[blocks[tag,i] for i in idx]
            old=' '.join(v['first_pass'] for v in items);new=' '.join(v['after_visual_review'] for v in items);fresh=' '.join(now[i] for i in idx)
            flag='Reading occurs in first pass' if simple(r['what_the_crop_shows']) in simple(old) else 'Verbal or graphical comparison'
            report+=['| '+r['place']+' — '+cell(r['what_the_crop_shows'])+' | '+', '.join(x['position'] for x in items)+' | '+flag+' | '+('Revised; see above' if old!=new else 'Retained')+' | '+html.escape(record['ink_resolution'])+' | '+('Same' if fresh==new else 'Witness-stage change')+' |']
    (R/'K36-01_blind_compare.md').write_text('\n'.join(report)+'\n')
if __name__=='__main__':run()
