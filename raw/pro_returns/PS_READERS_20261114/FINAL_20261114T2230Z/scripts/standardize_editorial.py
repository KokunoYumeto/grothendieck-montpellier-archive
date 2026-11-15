"""Apply the supplied English terminology standard to editorial prose only.

Author readings, quotations, formulas, file names and the checked pages are
excluded. Every changed editorial field is retained in an audit table.
Run only after all guide and review writers have frozen their files.
"""
from pathlib import Path
import argparse,csv,json,re
P=Path(__file__).resolve().parents[1];R=P/'records'
PROTECTED=re.compile(r'``.*?\'\'|“.*?”|‘.*?’|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)|homotopy-colimits?',re.S)
RULES=[
 (r'\bfibred\b','fibered'),(r'\bfibres\b','fibers'),(r'\bfibre\b','fiber'),
 (r'\bneighbourhoods\b','neighborhoods'),(r'\bneighbourhood\b','neighborhood'),
 (r'\bprogrammes\b','programs'),(r'\bprogramme\b','program'),(r'\bfavour\b','favor'),
 (r'\bcolours\b','colors'),(r'\bcolour\b','color'),(r'\bcancelled\b','canceled'),
 (r'\bterminal objects\b','final objects'),(r'\bterminal object\b','final object'),
 (r'\bdirect and inverse limits\b','inductive and projective limits'),
 (r'\binverse and direct limits\b','projective and inductive limits'),
 (r'\bdirect([ -])limits?\b',lambda m:'inductive'+m[1]+('limits' if m[0].endswith('limits') else 'limit')),
 (r'\binverse([ -])limits?\b',lambda m:'projective'+m[1]+('limits' if m[0].endswith('limits') else 'limit')),
 (r'\bdirect systems\b','inductive systems'),(r'\binverse systems\b','projective systems'),
 (r'\bcolimits\b','inductive limits'),(r'\bcolimit\b','inductive limit'),
 (r'\bfiltering inductive limits\b','filtered inductive limits'),
 (r'\bfibered products\b','fiber products'),(r'\bfibered product\b','fiber product'),
 (r'\bcup-products\b','cup products'),(r'\bcup-product\b','cup product'),
 (r'\bnon-empty\b','nonempty'),(r'\bnon-zero\b','nonzero'),
 (r'\baspherical\b','aspheric'),(r'\bNeron\b','Néron'),
 (r'\bNoetherian\b','noetherian'),(r'\bCartesian\b','cartesian'),
 (r'\bArtinian\b','artinian'),(r'\bHenselian\b','henselian'),
 (r'\\`etale\b','étale'),(r'\betale\b','étale')]
def plain(s):
    for pattern,replacement in RULES:s=re.sub(pattern,replacement,s)
    return s
def standard(s):
    out=[];start=0
    for m in PROTECTED.finditer(s):out.extend([plain(s[start:m.start()]),m[0]]);start=m.end()
    out.append(plain(s[start:]));return ''.join(out)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    changes=[]
    def record(path,field,identifier,before):
        after=standard(before)
        if before!=after:changes.append({'file':str(path.relative_to(P)),'field':field,'identifier':identifier,'before':before,'after':after,'reason':'Apply the supplied terminology and American editorial spelling standard outside quoted source wording and mathematics; author readings are untouched.'})
        return after
    for path in sorted((P/'guide_sections').glob('*.tex')):
        before=path.read_text();after=record(path,'editorial guide prose','whole fragment',before)
        if args.apply and before!=after:path.write_text(after)
    for path in sorted(R.glob('CHECK_DECISIONS_*.tsv'))+sorted(R.glob('TYPESETTING_FIXES_*.tsv')):
        rows=list(csv.DictReader(path.open(),delimiter='\t'))
        if not rows:continue
        fields=list(rows[0])
        for i,row in enumerate(rows,1):
            for field in ['reason','what_was_wrong','what_was_done']:
                if field in row:row[field]=record(path,field,row.get('source_id',str(i)),row[field])
        if args.apply:
            with path.open('w',newline='') as f:
                w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    for path in sorted(R.glob('MASTER_VARIANTS_*.json')):
        rows=json.loads(path.read_text())
        if not isinstance(rows,list):continue
        for i,row in enumerate(rows,1):
            if 'reason' in row:row['reason']=record(path,'reason',row.get('source_id',str(i)),row['reason'])
        if args.apply:path.write_text(json.dumps(rows,indent=2)+'\n')
    if args.apply and changes:
        out=R/'EDITORIAL_STANDARDIZATION.tsv';old=list(csv.DictReader(out.open(),delimiter='\t')) if out.exists() else []
        with out.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(changes[0]),delimiter='\t');w.writeheader();w.writerows(old+changes)
    print(json.dumps({'applied':args.apply,'changed_fields':len(changes),'files':sorted({r['file'] for r in changes})}))
if __name__=='__main__':main()
