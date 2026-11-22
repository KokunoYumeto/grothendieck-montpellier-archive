"""Compare independent crop readings with located passages.
Run python K58-04_blind_compare.py. Nothing in pages/ is modified.
"""
import csv
import difflib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREFIX = 'K58-04'


def table(name):
    with (ROOT / f'{PREFIX}_{name}.tsv').open(encoding='utf8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def tokens(source):
    """Ignore typesetting and editorial wrappers, retaining literal ink tokens."""
    source = source.replace(r'\operatorname{\underline{Hom}}','Hom')
    source = source.replace(r'\varnothing','∅').replace(r'\emptyset','∅')
    source = source.replace(r'\widehat',r'\hat')
    source = source.replace(r'\longrightarrow',r'\to').replace(r'\rightarrow',r'\to')
    source = source.replace(r'\longleftarrow',r'\gets').replace(r'\leftarrow',r'\gets')
    source = source.replace(r'\displaystyle','').replace(r'\qquad',' ').replace(r'\quad',' ').replace(r'\,',' ')
    source = re.sub(r'\\(?:uuline|uline|inserted|margin|deleted|handwritten|mathrm|text|operatorname|underline|texttt|mspage|emph)(?![A-Za-z])','',source)
    # The first candidate is the reader's adopted reading. Nested math braces
    # must not truncate an alternative or the text following the command.
    while r'\unsure{' in source:
        start=source.rindex(r'\unsure{')
        i=start+len(r'\unsure{'); level=1; bar=None
        while i<len(source) and level:
            c=source[i]
            if c=='{' and source[i-1]!='\\':level+=1
            if c=='}' and source[i-1]!='\\':level-=1
            if level==1 and c=='|' and bar is None:bar=i
            i+=1
        source=source[:start]+source[start+len(r'\unsure{'):bar if bar is not None else i-1]+source[i:]
    return re.findall(r'\\[A-Za-z]+|[^\W\d_]+|[0-9]+|[^\s{}$]',source,re.UNICODE)


def compare(source,reading):
    base,asked=tokens(source),tokens(reading)
    if not asked:return False,''
    width=len(asked)
    for i in range(max(0,len(base)-width+1)):
        if base[i:i+width]==asked:return True,' '.join(asked)
    lo=max(1,width-max(3,width//4)); hi=min(len(base),width+max(3,width//4))
    if lo>hi:return False,' '.join(base)
    starts={0}
    for bpos,word in enumerate(base):
        for rpos in (j for j,w in enumerate(asked) if w==word):
            starts.update(range(max(0,bpos-rpos-2),min(len(base),bpos-rpos+3)))
    best=(-1.,0,min(width,len(base)))
    for i in sorted(starts):
        for size in range(lo,min(hi,len(base)-i)+1):
            score=difflib.SequenceMatcher(None,asked,base[i:i+size],autojunk=False).ratio()
            if score>best[0]:best=(score,i,size)
    _,start,length=best
    return False,' '.join(base[start:start+length])


def escaped(s):
    return ' '.join(s.split()).replace('|',r'\|').replace('<','&lt;').replace('>','&gt;')


def main():
    blind={(r['scan'],r['place'].split(':')[0]):r['what the crop shows'] for r in table('blind')}
    later=[]
    changes_by_crop={}
    for item in table('witness'):
        decision=item['instruction (= retain, ! resolve, + append)']
        if decision[0] not in '!+':
            continue
        final=(decision[1:] if decision.startswith('!') else
               item['frozen'][:-1]+'|'+decision[1:]+'}')
        locus=Path(item['crop']).stem.split('-')[1]
        label=f"{item['scan']} {locus}, item {item['item']}"
        changes_by_crop.setdefault((item['scan'],locus),[]).append(item['item'])
        later.append([label,item['frozen'],final,item['ink and decision']])
    lines=['# Blind readings against the transcription','',
           'Each blind entry was recorded before reopening its page file. An entry tests the named part of the anchored passage. The comparison ignores editorial wrappers and some equivalent LaTeX commands. It retains accents, case, indices and punctuation. A difference can concern wording, the extent of a deletion, the bounds of the excerpt, or the way a drawing or a formula was keyed. The nearest first-pass sequence is the script’s alignment, not a proposed emendation. Offsets in the accompanying TSV count Unicode characters from zero in the distributed UTF-8 page.','',
           'The image finding records the independent second reading. The last column reports whether the blind tokens can be found verbatim after normalization in the distributed passage. Numbered items point to later witness decisions in the same crop. Their final readings and ink evidence follow the first table.','',
           '| Scan and place | Comparison | Blind reading | Nearest first-pass sequence | Finding on the image during independent audit | Match in distributed passage |',
           '|---|---|---|---|---|---|']
    differences=0;token_differences=0;visual_only=0;seen=set()
    for r in table('reading_spans'):
        key=(r['scan'],r['place'])
        if key in seen:raise ValueError(f'Duplicate location {key}')
        seen.add(key)
        page=(ROOT/'pages'/f'{PREFIX}_58_scan{int(r["scan"]):03}.tex').read_text()
        current=page[int(r['start']):int(r['end'])]
        if current!=r['distributed_passage']:raise ValueError(f'Stale location {key}')
        phrase=blind[key]
        original,nearest=compare(r['first_passage'],phrase)
        now,_=compare(current,phrase)
        visual=r['visual_difference']=='yes'
        if not original or visual:
            differences+=1
            token_differences+=int(not original)
            visual_only+=int(original)
            reason='visual' if original else ('tokens and visual' if visual else 'tokens')
            status='yes' if now else 'see image finding'
            refs=changes_by_crop.get((key[0],key[1].split('.')[0]),[])
            if refs:
                status+=' · later item(s) '+', '.join(refs)
            lines.append('| '+' | '.join(map(escaped,[f'{key[0]} {key[1]}',reason,phrase,nearest,r['disposition'],status]))+' |')
    if set(blind)!=seen:raise ValueError('A blind reading lacks an anchored comparison')
    visual_label='visual comparison' if visual_only==1 else 'visual comparisons'
    lines[2:2]=[f'{len(seen)} entries compared. {token_differences} differed from the first pass in the token comparison. The table includes {visual_only} further {visual_label} where the wording matched. All {differences} dispositions follow.','']
    lines+=['','## Later decisions in the marked passages','',
            'These decisions follow the independent freeze. They identify every place where the witness comparison resolved a previously marked reading or added an alternative. Items are numbered within each scan. The doubts register also records all the places left as they stood.','',
            '| Scan, crop and item | Independent frozen reading | Distributed reading | Evidence on the image |',
            '|---|---|---|---|']
    lines+=['| '+' | '.join(map(escaped,row))+' |' for row in later]
    (ROOT/f'{PREFIX}_blind_compare.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print(f'{len(seen)} entries; {token_differences} token differences; {visual_only} visual-only comparisons; {len(later)} later decisions.')


if __name__=='__main__':main()

