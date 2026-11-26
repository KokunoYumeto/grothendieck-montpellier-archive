"""Compare independently recorded observations with located spans in the TeX pages."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def rows(name):
    with (ROOT / name).open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def normalize(s):
    # Only the first candidate in a marked reading participates in collation.
    while (match := re.search(r'\\unsure\{', s)):
        start = match.end()
        depth, end = 1, start
        while end < len(s) and depth:
            depth += (s[end]=='{') - (s[end]=='}')
            end += 1
        if depth:
            raise ValueError('unclosed doubt')
        s = s[:match.start()] + s[start:end-1].split('|')[0] + s[end:]
    s=s.replace(r'n^{\circ}','n°').replace(r'\overline',r'\bar')
    s=re.sub(r'\\(?:deleted|inserted|handwritten|text|uline|uuline|left|right)(?![A-Za-z])','',s)
    s=s.replace(r'\operatorname','').replace(r'\mathrm','').replace(r'\,','').replace(r'\;','')
    s=s.replace(r'\ne ','≠').replace(r'\neq ','≠').replace('’',"'")
    return re.sub(r'[\s\x24{}]','',s)

def found(observation, passage):
    if observation=='[punctures]':
        return r'\hfill ....' not in passage
    if observation=='[blank]':
        return r'\quad' in passage
    return all(normalize(part) in normalize(passage) for part in observation.split(' || '))

def cell(s):
    return s.replace('|',r'\|').replace('\n',' ')

def main():
    blind=rows('K60-06_blind.tsv')
    locs={(c['scan'],c['place']):c for c in rows('K60-06_blind_collation.tsv')}
    discrepancies=[]; current=[]; covered=set()
    for item in blind:
        key=(item['scan'],item['place']); mapping=locs[key]; covered.add(key)
        n=int(key[0]); p=ROOT/'pages'/f'K60-06_60_scan{n:03}.tex'
        lines=p.read_text().splitlines()
        span=list(map(int,mapping['source_lines'].split('-')))
        text='\n'.join(lines[span[0]-1:span[-1]])
        observation=item['what the crop shows']
        if mapping['first_reading_if_different']:
            discrepancies.append([*key,observation,mapping['first_reading_if_different'],mapping['ink_and_settlement']])
        if not found(observation,text):
            current.append([*key,observation,mapping['ink_and_settlement'] or 'See the witness collation for this location.'])
    if covered!=set(locs):raise ValueError('Unpaired locations in collation')
    report=['# Blind comparison','',f'{len(blind)} located observations on {len(set(x[0] for x in covered))} scans. Differences below compare the independent observations with the first transcription. The last table tests the current page files. Editorial uncertainty and spacing do not themselves constitute a difference. Two entries also index proposals written in the precomparison word lists (the ending in 66, 6b and the crossed opening of 69).','']
    for title,head,data in [('First transcription versus blind reading',['Scan','Place','Blind reading','First reading','Settlement'],discrepancies),('Blind observations absent from the current located span',['Scan','Place','Blind reading','Settlement or subsequent check'],current)]:
        report+=['## '+title,'']
        if data:
            for row in [head,['---']*len(head),*data]:
                report.append('| '+' | '.join(map(cell,row))+' |')
            report.append('')
        else:report+=['None.','']
    (ROOT/'K60-06_blind_compare.md').write_text('\n'.join(report))
    print(f'{len(blind)} observations, {len(discrepancies)} differences from first transcription, {len(current)} absent from current spans')
if __name__=='__main__':
    main()
