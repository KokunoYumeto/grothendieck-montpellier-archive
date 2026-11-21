"""Collate the independent crop TSV with the first-pass snapshots and outgoing fragments."""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def visible(s):
    while True:
        m=re.search(r'\\(?:unsure|uuline|uline)\{',s)
        if not m:break
        j=m.end();depth=1;end=None
        while j<len(s) and depth:
            c=s[j]
            if c=='{' and s[j-1]!='\\':depth+=1
            elif c=='}' and s[j-1]!='\\':depth-=1
            elif c=='|' and depth==1 and end is None and s[m.start():].startswith('\\unsure'):end=j
            j+=1
        if depth:break
        s=s[:m.start()]+s[m.end():end if end is not None else j-1]+s[j:]
    return re.sub(r'\s+','',s.replace('~',' ').replace('$','').replace(r'\,','').replace(r'\!',''))
def cell(s):return '\u0060'+s.replace('|',r'\|').replace('\n',' ')+'\u0060'

def normalized(s):
    s = visible(s).replace(r'\S', '§')
    equivalents = {
        'Washnitzer--Monsky':'Washnitzer-Monsky', r'\text{ou }':'ou', r'\text{ou}':'ou',
        r'\mathrm{STRAT}':'STRAT', r'\longrightarrow':r'\to', r'\rightarrow':r'\to',
        '«':chr(96)*2, '»':"''", '’':"'", '---':'--', r'\textsuperscript{t}':'ᵗ',
        r'\mathrm{crist.}':'crist.',
    }
    for old,new in equivalents.items():
        s=s.replace(old,new)
    s=re.sub(r'([_^])\{(\\[A-Za-z]+|[A-Za-z0-9*])\}',r'\1\2',s)
    return re.sub(r'(\\(?:mathbb|mathscr|mathcal|mathrm))\{([A-Za-z])\}',r'\1\2',s)

def checked_in(tokens,page):
    return all(t in page for t in tokens)

def run():
    evidence=json.loads((ROOT/'K7-04_blind_evidence.json').read_text())
    with (ROOT/'K7-04_blind.tsv').open() as f:
        blind=list(csv.DictReader(f,delimiter='\t'))
    by_scan={}
    layouts=[]
    issues=[]
    for row in blind:
        n,key,reading=(row[k] for k in ('scan','place','what_the_crop_shows'))
        page=(ROOT/'pages'/f'K7-04_7_scan{int(n):03}.tex').read_text()
        first='\n'.join(evidence['first_pass'][n])
        item=evidence['differences'].get(n,{}).get(key)
        equivalent=evidence['layout_equivalences'].get(n,{}).get(key)
        if item:
            if normalized(item['first']) not in normalized(first):
                issues.append((n,key,'first-pass excerpt not found'))
            if item['final'] not in page:
                issues.append((n,key,'outgoing text at this locus has changed'))
            by_scan.setdefault(n,[]).append([key,cell(reading),cell(item['first']),
                                              item['settlement'],cell(item['final'])])
        elif equivalent:
            if not (checked_in(equivalent['first'],first) and checked_in(equivalent['final'],page)):
                issues.append((n,key,'constituent of equivalent notation not found'))
            layouts.append([n,key,equivalent['settlement']])
        else:
            if normalized(reading) not in normalized(first):
                issues.append((n,key,'initial discrepancy has no disposition'))
            if normalized(reading) not in normalized(page):
                issues.append((n,key,'outgoing reading needs a local comparison'))
    total=sum(map(len,by_scan.values()))
    report=['# Blind collation','',
            f'{len(blind)} image-only entries were saved before the first-pass pages were opened. {total} differences in wording, notation or placement are listed below. Each table gives the audit-stage decision and the literal passage in the outgoing page. Later witness changes are visible in the last column.','',
            'The evidence file contains the first-pass snapshots and the alignments for nonliteral matches. The script checks them against the blind TSV and the delivered page files. For ordinary matching it ignores spaces, typographic equivalents and the difference between a first candidate printed alone and the same candidate in a doubt mark. Small excerpts can also occur elsewhere on a page; the scan and location in the TSV identify the particular inscription.','']
    for n in range(47,61):
        report.extend([f'## Scan {n}',''])
        rows=by_scan.get(str(n),[])
        if rows:
            report.extend(['| Place | Blind reading | First-pass reading | Decision on the crop | Outgoing text at the locus |',
                           '|---|---|---|---|---|'])
            report.extend('| '+' | '.join(r)+' |' for r in rows)
        elif n==48:
            report.append('The blind entries agree with the preferred readings of the initial page. During subsequent collation, tonal enhancement revealed the separate pencil calculation. The upper sign over the last X was later resolved as capital sigma in the witness check; the blind TSV preserves its g reading.')
        elif n==50:
            report.append('The independent entries agree with the first candidates. Collation established a gap between the two underlines in the definition. The witness-stage decision on the final s of « Relations » is recorded in the doubt register.')
        else:report.append('No divergent entry.')
        report.append('')
    report.extend(['## Agreements requiring local alignment','',
                   '| Scan | Place | Why the entries agree |','|---|---|---|'])
    report.extend('| '+' | '.join(row)+' |' for row in layouts)
    if issues:
        report.extend(['','## Items requiring review',''])
        report.extend('- '+' · '.join(i) for i in issues)
    else:report.extend(['','All blind entries accounted for. All stored outgoing excerpts and equivalent notation anchors were found on their respective pages.'])
    (ROOT/'K7-04_blind_compare.md').write_text('\n'.join(report)+'\n')
    return issues

if __name__=='__main__':
    errors=run()
    for err in errors:print(*err,sep='\t')
    sys.exit(bool(errors))
