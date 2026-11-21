"""Compare the pre-opening image excerpts with the first and delivered page texts."""
import csv
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path

BASE=Path(__file__).resolve().parent
def read_tsv(name):
    with (BASE/name).open() as f:
        return list(csv.DictReader(f,delimiter='\t'))
def old_reading(p,delta):
    lines=p.read_text().splitlines(keepends=True)
    for start,end,old in reversed(delta['reverse_changes']):
        lines[start:end]=old
    first=''.join(lines)
    assert hashlib.sha256(first.encode()).hexdigest()==delta['first_sha256'],p
    return first
def norm(s):
    s=re.sub(r'% archive sheet number: (\d+)',r' folio \1',s)
    s=re.sub(r'%[^\n]*','',s)
    s=re.sub(r'\\(?:begin|end)\{[^}]*\}',' ',s)
    s=re.sub(r'\\(?:text|mathrm|operatorname|mathbin|mathrel|mathbf|mathbb|mathscr|mathcal|mathfrak|uline|underline|underbrace|underset|substack|deleted|inserted|margin|unsure|left|right|bigl|bigr|big|Big|qquad|quad)\b','',s)
    for a,b in [(r'\longrightarrow','→'),(r'\to','→'),(r'\Longrightarrow','⇒'),(r'\varepsilon','ε'),(r'\alpha','α'),(r'\varphi','φ'),(r'\partial','∂'),(r'\ldots','…'),(r'\times','×'),(r'\leq','≤'),(r'\geq','≥'),(r'\in ','∈'),(r'\longmapsto','↦'),(r'\mapsto','↦'),('...','…'),('’',"'"),('«','"'),('»','"'),('“','"'),('”','"'),(chr(96)*2,'"'),("''",'"')]:
        s=s.replace(a,b)
    return re.sub(r'[{}\s$~&\\]','',s)
def evidence(sample,source):
    if sample in source:
        return "match"
    match=SequenceMatcher(None,sample,source,autojunk=False).find_longest_match()
    if match.size<2:
        return "no shared run"
    start=max(0,match.b-match.a)
    return "near " + source[start:start+min(120,len(sample))]
def cell(s):
    return s.replace('|',r'\|').replace('\n',' ')
def row(*a):
    return '| '+' | '.join(cell(str(x)) for x in a)+' |'
items=read_tsv('K39-01_blind.tsv')
decisions=read_tsv('K39-01_blind_decisions.tsv')
witness=read_tsv('K39-01_witness_decisions.tsv')
# The identifiers refer to the marked spans of the frozen text on these scans.
# These are the blind differences for which later witness collation changed the
# result or supplied an additional candidate for the same word or sign.
linked_marks={5:{5,6,7,8}, 7:{1}, 14:{3,6}, 15:{12}, 17:{4}, 19:{9}}
deltas=json.loads((BASE/'K39-01_first_reading_delta.json').read_text())
lines=['# Blind collation','',f'{len(items)} excerpts were recorded from the images before reopening the relevant page. The {len(decisions)} editorial differences below compare those readings with the first transcription. Each decision was made on the image. On six scans a later witness decision affected the same sign or word. Those later decisions have their own table immediately below the first.','',
       'The last table on each scan lists all remaining literal differences found by the comparison script. Short expressions can occur more than once on a sheet. A line labelled “near” displays the best matching substring and can point to another occurrence. The original excerpts are preserved in the blind TSV. The table omits an excerpt only when it matches both page versions after normalization of spacing, markup and common mathematical commands.','']
for scan in dict.fromkeys(r['scan'] for r in items):
    p=BASE/'pages'/f'K39-01_39_scan{int(scan):03d}.tex'
    first=norm(old_reading(p,deltas[p.name]))
    final=norm(p.read_text())
    lines.extend([f'## Scan {scan}','','| Place | First reading | Blind reading | Decision on image |','|---|---|---|---|'])
    for d in decisions:
        if d['scan']==scan:
            lines.append(row(d['place'],d['first_reading'],d['blind_reading'],d['decision']))
    overlaps=[r for r in witness if r['Scan']==scan and int(r['Place']) in linked_marks.get(int(scan),set())]
    if overlaps:
        lines.extend(['','| Witness place | Frozen | Delivered | Ink used in the decision |','|---|---|---|---|'])
        for r in overlaps:
            lines.append(row(r['Place']+' · '+r['Manuscript lines'],r['Frozen reading'],r['Final reading'],r['Ink on reinspection']+' ('+r['Detail crop']+')'))
    lines.extend(['','| Place | Blind excerpt | First text | Delivered text |','|---|---|---|---|'])
    for r in [x for x in items if x['scan']==scan]:
        for segment in r['what_the_crop_shows'].strip().split(' · '):
            s=norm(segment)
            if not s: continue
            a,b=evidence(s,first),evidence(s,final)
            if (a,b)!=('match','match'):
                lines.append(row(r['place'],segment,a,b))
    lines.append('')
(BASE/'K39-01_blind_compare.md').write_text('\n'.join(lines)+'\n')
