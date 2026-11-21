"""Collate the pre-file blind TSV with the corresponding blocks in the supplied page files."""
import csv
import difflib
import re
import unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def table(file):
    with (ROOT/file).open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def simplify(s):
    glyphs={'𝔤':'mathfrak g','π':'pi','γ':'gamma','α':'alpha','β':'beta','Γ':'Gamma','τ':'tau','σ':'sigma','θ':'theta','ζ':'zeta','λ':'lambda','χ':'chi','ℓ':'ell','′':"'",'→':'to','⇒':'Rightarrow','∈':'in','⊂':'subset','≃':'simeq','∩':'cap','⊗':'otimes','∀':'forall','≥':'geq','≠':'ne','ℤ':'mathbb Z','₁':'1','₀':'0','²':'2','¹':'1','…':'ldots'}
    for a,b in glyphs.items():s=s.replace(a,' '+b+' ')
    s=re.sub(r'\\(?:unsure|deleted|inserted|uline|uuline|text|margin|mspage|mathrm|operatorname)(?![A-Za-z])',' ',s)
    s=unicodedata.normalize('NFKD',s.casefold())
    return re.findall(r'[a-z0-9]+',''.join(x for x in s if not unicodedata.combining(x)))

def blocks(n):
    t=(ROOT/'pages'/f'K31-06_31_scan{n:03}.tex').read_text()
    ms=list(re.finditer(r'^% (B\d+) \| [^\n]+\n',t,re.M))
    last=re.search(r'^% archive sheet number: (.+)$',t,re.M)
    values={'B00':t[:ms[0].start()],'B99':last[1] if last else ''}
    for i,m in enumerate(ms):
        b=ms[i+1].start() if i+1<len(ms) else (last.start() if last else len(t))
        values[m[1]]=re.sub(r'^%[^\n]*\n','',t[m.end():b],flags=re.M).strip()
    return values

def esc(s):return str(s).replace('|',r'\|').replace('\n',' ')
def row(*fields):return '| '+' | '.join(esc(x) for x in fields)+' |\n'

def main():
    blind=table('K31-06_blind.tsv')
    align={(q['scan'],q['place']):q for q in table('K31-06_blind_alignment.tsv')}
    assert len(align)==len(blind)
    out=['# Blind collation\n\nThe first two columns identify an independent crop reading recorded before opening the page. Adjudications compare that reading with the first pass. A supplementary collation records distinctions found when the original blind rows were checked again against the ink after the witness phase. The final table aligns all blind rows to the returned page files. Its longest shared sequence is a mechanical aid; condensed notes, strike descriptions and mathematical notation can differ in wording even when the ink reading agrees. The witness apparatus reports any subsequent intervention separately.\n\n','## Differences and decisions\n\n',row('Scan','Place','Blind reading','First pass','Decision on the ink'),row(*['---']*5)]
    allrows=[];supplement=[];d=0
    for b in blind:
        alignrow=align.pop((b['scan'],b['place']));n=int(b['scan']);book=blocks(n)
        seg=' '.join(book[k] for k in alignrow['block'].split(','))
        assert seg.strip()
        u,v=simplify(b['what_the_crop_shows']),simplify(seg)
        assert u or b['what_the_crop_shows'].strip()
        match=difflib.SequenceMatcher(a=u,b=v,autojunk=False).find_longest_match()
        excerpt=' '.join(v[max(0,match.b-4):min(len(v),match.b+max(match.size,1)+5)])
        if alignrow['decision']:
            d+=1;out.append(row(n,b['place'],b['what_the_crop_shows'],alignrow['first_pass_if_disputed'],alignrow['decision']))
        if alignrow.get('additional_collation'):
            supplement.append(row(n, b['place'], b['what_the_crop_shows'],
                                  alignrow['reviewed_first'], alignrow['additional_collation']))
        disposition = ('see decision above' if alignrow['decision'] else
                       'see supplementary collation' if alignrow.get('additional_collation') else
                       'compared in page audit')
        allrows.append(row(n,alignrow['block'],b['place'],b['what_the_crop_shows'],excerpt or 'punctuation or symbolic marks',f'{match.size}/{len(u)}', disposition))
    assert not align
    out += ['\n## Supplementary collation of blind entries\n\n',
            'These checks clarify compressed readings, the position of a sign, or the extent of a cancellation. They were recorded after the witness check.\n\n',
            row('Scan','Place','Blind reading','First pass','Decision on the ink'),
            row(*['---']*5), *supplement]
    out+=['\n## All locations\n\n',f'{len(blind)} independent records; {d} differences or qualified readings were recorded in the independent audit, with {len(supplement)} additional decisions in the supplementary collation. The fraction gives the longest consecutive shared token sequence divided by the number of tokens in the blind record. It is not a confidence measure. The page blocks and blind TSV preserve original spellings.\n\n',row('Scan','Block','Place','Blind reading','Normalized page excerpt','Shared run','Disposition'),row(*['---']*7),*allrows]
    (ROOT/'K31-06_blind_compare.md').write_text(''.join(out))
if __name__=='__main__':main()

