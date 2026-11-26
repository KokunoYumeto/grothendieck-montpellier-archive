"""Reconstruct the first-pass readings at registered positions and collate them."""
from pathlib import Path
import csv, json, re
root=Path(__file__).resolve().parent
def records(file):
    p=root/('K58-05_'+file+'.tsv')
    if not p.exists():return []
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))
def simplified(s):
    # Compare ink readings. Retain editorial state, font, primes and indices.
    s=re.sub(r'\\unsure\s+(?=[A-Za-z])', '', s)
    def choices(x):
        pos=x.find(r'\unsure{')
        if pos<0:return x
        beg=pos+8;idx=beg;depth=1;sep=None
        while idx<len(x) and depth:
            c=x[idx]
            if c=='{':depth+=1
            elif c=='}':depth-=1
            elif c=='|' and depth==1 and sep is None:sep=idx
            idx+=1
        if depth:raise ValueError(x)
        return choices(x[:pos]+x[beg:(sep if sep is not None else idx-1)]+x[idx:])
    s=choices(s)
    # Canonicalise positioning instructions with no ink of their own.
    s=s.replace(r'\mathop{\vphantom{\sum}}\limits','{}')
    s=re.sub(r'\\textsuperscript\{([a-z0-9])\}', r'^{\1}',s)
    s=s.replace(r'^{\prime}',"'").replace('′',"'").replace('φ',r'\varphi').replace('ⁿ','^{n}').replace('≤',r'\leq').replace('≥',r'\geq')
    s=re.sub(r'_\{?([a-zA-Z])\}?\^(\{[^{}]+\}|[a-zA-Z0-9])',r'^\2_{\1}',s)
    s=re.sub(r'\\(?:mathord|displaystyle|scriptsize|bigl|bigr|qquad)\b','',s)
    s=s.replace(r'\\',' ').replace(r'\ ',' ').replace('&','').replace(r'\[','[').replace(r'\]',']')
    for a,b in [(r'\longrightarrow',r'\to'),(r'\rightarrow',r'\to'),(r'\operatorname',''),(r'\mathrm',''),(r'\mathrel',''),(r'\text{','{'),(r'\quad',''),(r'\,',''),(r'\!',''),(r'\colon',':'),(r'\widehat',r'\hat'),(r'\widetilde',r'\tilde')]:s=s.replace(a,b)
    return re.sub(r'[\s{}$~]+','',s).replace('’',"'")
def md(s):return '<code>'+s.replace('&','&amp;').replace('<','&lt;').replace('|','&#124;').replace('\n',' ↵ ')+'</code>'
def main():
    edits=records('audit_revisions')
    pos={(r['scan'],r['place']):r for r in records('collation')}
    cache={};output=[];count=0;diff=0
    for b in records('blind'):
        k=(b['scan'],b['place']);r=pos.get(k)
        if r is None:continue
        n=b['scan']
        if n not in cache:
            s=(root/'pages'/f'K58-05_58_scan{int(n):03}.tex').read_text()
            for e in reversed([e for e in edits if e['scan']==n]):
                i,j=int(e['start']),int(e['end'])
                assert s[i:j]==json.loads(e['current_json']),('unexpected edited span',n,i)
                s=s[:i]+json.loads(e['first_pass_json'])+s[j:]
            cache[n]=s
        first=cache[n][int(r['start']):int(r['end'])]
        count+=1
        if simplified(first)!=simplified(b['what_the_crop_shows']):
            diff+=1
            output.append('| '+n+' | '+k[1]+' | '+md(b['what_the_crop_shows'])+' | '+md(first)+' | '+r['ink_and_decision'].replace('|','&#124;')+' |')
    title='# Blind comparison\n\nThe script read '+str(count)+' registered positions. '+str(diff)+' differed after ignoring spaces, grouping, equivalent arrow spellings and secondary candidates. A marked deletion, insertion, double stroke or change of index remains significant. The comparison uses the first-pass page text reconstructed from the final file and the recorded edits. The scan audit also records corrections found outside the blind list.\n\n'
    head='| Scan | Place | Independent reading | First pass | Resolution on the crop |\n|---|---|---|---|---|\n'
    (root/'K58-05_blind_compare.md').write_text(title+head+'\n'.join(output)+'\n')
    print(count,'locations;',diff,'differences')
if __name__=='__main__':main()

