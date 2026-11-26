"""Compare independent slips with their collated passages, using the page files.
Run from any directory. The first-pass passage and reading remain in the TSV.
The audited anchor is checked against the current page. A witness revision may
change the anchor; the exact final passage then appears in the last column.
"""
import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def read(name):
    with (ROOT/name).open(newline='') as fd:
        return list(csv.DictReader(fd,delimiter='\t'))

def cell(s):
    return s.replace('|',r'\|').replace('\n',' ')

def main():
    blind_rows=read('K106-01_blind.tsv')
    slips={(r['scan'],r['place']):r['what the crop shows'] for r in blind_rows}
    rows=read('K106-01_collation.tsv')
    assert len(slips)==len(rows)==len(blind_rows)
    assert set(slips)=={(r['scan'],r['place']) for r in rows}
    differences=[]
    for row in rows:
        n=row['scan']
        page=ROOT/'pages'/f'K106-01_106_scan{n}.tex'
        source=page.read_text().splitlines()
        assert source[0]==rf'\scanpage{{{int(n)}}}'
        current_line=int(row['audited line'])
        current=source[current_line-1]
        if 'exact final line' in row:
            assert current==row['exact final line'],(page,current_line)
        else:
            assert current==row['exact audited line'],(page,current_line)
        blind=slips[n,row['place']]
        first=row['first reading']
        if ' '.join(blind.split())!=' '.join(first.split()):
            differences.append([f'{n} / {row["first line"]}',row['place'],first,blind,row['settlement'],f'{n}, L{current_line}'])
    lines=['# Blind readings and their settlements','',
           f'{len(rows)} independent slips were compared with the page files. {len(differences)} differed from the first reading. Each slip concerns the words, marks or arrows named in its Place column. A difference can concern a letter, an arrow, a cancellation or where an insertion belongs. The readings of diagrams give vertices and arrows in linear order. The collation TSV preserves each exact first-pass and audited line. The last column identifies the delivered page-file line. Later witness decisions concerning the same reading are identified in the settlement.','',
           '| Scan / first line | Place | First reading | Blind reading | Settlement on the crop | Page line |',
           '|---|---|---|---|---|---|']
    for row in differences:
        formatted = [cell(field) for field in row]
        for i in (2, 3):
            formatted[i] = chr(96) + formatted[i] + chr(96)
        lines.append('| ' + ' | '.join(formatted) + ' |')
    (ROOT/'K106-01_blind_compare.md').write_text('\n'.join(lines)+'\n')
    print(f'{len(rows)} slips; {len(differences)} differences; all current page anchors verified.')

if __name__=='__main__':
    main()
