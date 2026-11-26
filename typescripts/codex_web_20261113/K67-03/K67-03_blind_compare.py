"""Compare the independent crop readings to the page text. Run from any folder.

Use --record N during the audit, immediately after recording a blind page,
before making changes. A normal run regenerates the complete comparison.
The final-place register locates each reading in the delivered page as well.
"""
import argparse, csv, re, unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent
P = 'K67-03_'
def read_rows(name):
    with (BASE/(P+name)).open(newline='') as src:
        return list(csv.DictReader(src, delimiter='\t'))

def normalized(s):
    # First candidates only. Nested braces inside math font and accent macros count.
    start = re.compile(r'\\unsure\{')
    while m := start.search(s):
        j=m.end(); level=1
        while j<len(s) and level:
            if s[j] in '{}' and s[j-1]!='\\':
                level+=1 if s[j]=='{' else -1
            j+=1
        s=s[:m.start()]+s[m.end():j-1].split('|')[0]+s[j:]
    s=unicodedata.normalize('NFC',s).replace('’',"'")
    s=re.sub(r'\\(?:text|mathrm|texttt|uline|uuline|left|right|bigl|bigr|biggl|biggr|displaystyle|big|mspage|margin|inserted|deleted|mathbin|quad|qquad)(?![A-Za-z])','',s)
    s=s.replace('\\overline','\\bar').replace('\\widetilde','\\tilde').replace('\\widehat','\\hat')
    s=s.replace('\\longrightarrow','\\to').replace('\\rightarrow','\\to').replace('\\iff','\\Longleftrightarrow')
    s=s.replace('\\,','').replace('\\;','').replace('\\!','').replace('\\ ','')
    s=re.sub(r'\\[\[\]]','',s)
    s=re.sub(r'\\(?:begin|end)\{(?:aligned|array|gathered)\}','',s)
    return re.sub(r'[\s{}$&~]','',s)
def cell(s):
    return s.strip().replace('\n',' ').replace('|',r'\|')
def compare():
    ap=argparse.ArgumentParser();ap.add_argument('--record',type=int);args=ap.parse_args()
    places={(r['scan'],r['place']):r for r in read_rows('places.tsv')}
    findings=[]
    final_places={}
    final_only=[]
    if not args.record:
        final_places={(r['scan'],r['place']):r for r in read_rows('final_places.tsv')}
        if final_places.keys()!=places.keys():
            raise ValueError('The first and final location registers differ.')
        for (n,k),r in final_places.items():
            page=(BASE/'pages'/f'K67-03_67_scan{int(n):03}.tex').read_text()
            pos=sum(map(len,page.splitlines(keepends=True)[:int(r['source_line'])-1]))+int(r['column'])
            if page[pos:pos+int(r['length'])]!=r['final_reading']:
                raise ValueError(f'Final page span differs on scan {n}, {k}')
    for b in read_rows('blind.tsv'):
        n,k,s=b.values()
        if (n,k) not in places: raise ValueError(f'Unknown blind place {n} {k}')
        t=places[n,k]; ref=t['first_reading']
        if args.record==int(n):
            page=(BASE/'pages'/f'K67-03_67_scan{int(n):03}.tex').read_text()
            offset=sum(map(len,page.splitlines(keepends=True)[:int(t['source_line'])-1]))+int(t['column'])
            if page[offset:offset+int(t['length'])]!=ref:
                raise ValueError(f'Comparison target no longer at first-pass location on {n} {k}')
        # Each part is a separately readable run on the crop. Compare it at
        # this site only. Context on either side of a shorter run is allowed.
        ns=normalized(ref)
        parts=[normalized(part) for part in s.split(' ⫶ ')]
        if not all(part in ns for part in parts if part):
            findings.append((n,k,s,ref))
        if final_places:
            current=normalized(final_places[n,k]['final_reading'])
            if not all(part in current for part in parts if part):
                final_only.append((n,k,s))
    decisions={}
    res=BASE/(P+'blind_decisions.tsv')
    if res.exists():
        decisions={(r['scan'],r['place']):r['settlement'] for r in read_rows('blind_decisions.tsv')}
    lines=['# Blind comparison','','The first reading is the text of the page at the time its blind entries were committed. Each registered span was verified at its original line and column. Braces, layout wrappers, spacing and alternate LaTeX spellings of the same mark are ignored. The first candidate is compared. The symbol ⫶ separates independent runs of ink on one crop. A shorter reading checks only that run. Differences in stroke state or placement discovered by visual review are also included. The settlement records the crop decision at the independent audit. The delivered span shows the final wording, including any later decision at an already marked place. Its line number is in the last column. The complete text of every final span is also kept verbatim in K67-03_final_places.tsv and verified against the actual page on each run.','',
           '| Scan | Crop | Independent reading | First-pass span | Settlement on the image | Delivered span | Final TeX line |','|---|---|---|---|---|---|---|']
    items={(n,k):(s,t) for n,k,s,t in findings}
    for b in read_rows('blind.tsv'):
        n,k,s=b.values()
        if (n,k) in decisions and (n,k) in places: items.setdefault((n,k),(s,places[n,k]['first_reading']))
    for (n,k),(s,t) in sorted(items.items(),key=lambda item:(int(item[0][0]), int(places[item[0]]['source_line']), int(places[item[0]]['column']))):
        lines.append('| '+' | '.join(map(cell,[n,k,s,t,decisions.get((n,k),'pending visual settlement'),final_places.get((n,k),{}).get('final_reading',''),final_places.get((n,k),{}).get('source_line','')]))+' |')
    if final_places:
        extra=[(n,k,s) for n,k,s in final_only if (n,k) not in items]
        explanations={
            ('38','quasi'):'The independent word quasi agreed with the first transcription. In the finished line the hand ends after u with a stop, giving qu. inv.; the witness check later settled only aussi.',
            ('41','la'):'The blind entry agreed with the first transcription that the deleted word was unreadable. At the marked witness comparison, a tall l and a following loop allowed tentative la, still deleted.'
        }
        lines.extend(['','## Additional differences from the delivered page','',
                      'At the following sites the independent reading agreed with the first-pass text, then the page changed.','',
                      '| Scan | Crop | Independent reading | Delivered span | Settlement | Final TeX line |','|---|---|---|---|---|---|'])
        for n,k,s in extra:
            r=final_places[n,k]
            lines.append('| '+' | '.join(map(cell,[n,k,s,r['final_reading'],explanations.get((n,k),'consult the audit for this scan'),r['source_line']]))+' |')
        lines+=['',f'{len(places)} independent placements checked against the final pages. {len(items)} sites in the comparison with the first pass. {len(extra)} further differences are visible only against the delivered text.']
    (BASE/(P+'blind_compare.md')).write_text('\n'.join(lines)+'\n')
    if args.record:
        for n,k,s,ref in findings:
            if int(n)==args.record: print(k,':',ref.replace('\n',' ')[:450])
    else: print(f'{len(items)} sites in comparison table')
if __name__=='__main__':
    compare()

