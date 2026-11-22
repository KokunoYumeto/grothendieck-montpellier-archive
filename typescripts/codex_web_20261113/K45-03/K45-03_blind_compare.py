"""Reproduce the blind collation against the actual page fragments."""
import csv, re
from pathlib import Path
D=Path(__file__).resolve().parent
KEY='K45-03'
def normalized(s):
    def groups(t):
        p=r'\\(unsure|deleted|inserted|uline|uuline|margin|handwritten|text|mathbin|mathrm|operatorname|textsuperscript)\{'
        m=re.search(p,t)
        if not m:return t
        i=m.end();d=1
        while i<len(t) and d:
            if t[i]=='{' and t[i-1]!='\\':d+=1
            elif t[i]=='}' and t[i-1]!='\\':d-=1
            i+=1
        v=t[m.end():i-1]
        if m[1]=='unsure':v=v.split('|')[0]
        return t[:m.start()]+groups(v)+groups(t[i:])
    s=groups(s)
    s=re.sub(r'\\arrow\[r\]\s*\\&\s*',lambda _:r'\to ',s)
    s=re.sub(r"\\ast(?![A-Za-z])", "*", s)
    s=re.sub(r"\\(?:longrightarrow|rightarrow)(?![A-Za-z])", lambda _:r"\to",s)
    s=re.sub(r'\\(?:begin|end)\{[^}]+\}','',s)
    s=re.sub(r'\\(?:qquad|quad|,|;|!| |left(?![A-Za-z])|right(?![A-Za-z]))',' ',s)
    return re.sub(r'\\(?:[()\[\]])|[$&{}~\s]','',s)
def table(p):
    with p.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f,delimiter='\t'))
def esc(s):return s.replace('|','\\|').replace('\n',' ')
def restore_first_pages():
    """Invert the two recorded edit sequences, then verify each original snapshot."""
    from hashlib import sha256
    audit=table(D/(KEY+'_audit_edits.tsv'))
    witness=table(D/(KEY+'_witness_edits.tsv'))
    snapshots={}
    for scan in dict.fromkeys(r['scan'] for r in audit):
        page=(D/'pages'/f'{KEY}_45_scan{int(scan):03}.tex').read_text()
        for r in reversed([x for x in witness if int(x['scan'])==int(scan)]):
            pos=int(r['final_character_offset'])
            old,new=r['frozen_span'],r['final_span']
            assert page[pos:pos+len(new)]==new, (scan,pos,'witness')
            page=page[:pos]+old+page[pos+len(new):]
        changes=[x for x in audit if x['scan']==scan]
        for r in reversed(changes):
            if not r['frozen_offset']: continue
            pos=int(r['frozen_offset'])
            old,new=r['first_span'],r['frozen_span']
            assert page[pos:pos+len(new)]==new, (scan,pos,'audit')
            page=page[:pos]+old+page[pos+len(new):]
        assert sha256(page.encode()).hexdigest()==changes[0]['first_page_sha256'], scan
        snapshots[scan]=normalized(page)
    return snapshots



def main():
    blind=table(D/(KEY+'_blind.tsv'))
    ledger={(r['scan'],r['place']):r for r in table(D/(KEY+'_collation.tsv'))}
    snapshots=restore_first_pages()
    pages={};lines=[];graphic_notes=[];agree=0;pending=0
    for b in blind:
        n=b['scan'];key=(n,b['place'])
        if n not in pages:pages[n]=normalized((D/'pages'/f'{KEY}_45_scan{int(n):03}.tex').read_text())
        r=ledger.get(key)
        if r is None:pending+=1;continue
        expected=r['first_page_span'];pos=int(r['first_page_offset'])
        initial=snapshots[n][pos:pos+len(expected)]
        if initial!=expected:raise ValueError((key,'initial page differs at recorded position'))
        second=normalized(b['what_the_crop_shows'])
        anchor=r['audited_page_span'];current=pages[n]
        if anchor not in current:
            later=r.get('post_witness_span','')
            if not later or later not in current:raise ValueError((n,b['place'],'page anchor absent',anchor))
        if initial==second:
            agree+=1
            if r['decision']!='Same strokes and sequence.':
                graphic_notes.append('| '+' | '.join(esc(x) for x in [n,b['place'],r['decision']])+' |')
        else:
            first=r.get('first_display') or initial
            if normalized(first)!=initial:raise ValueError((key,'first display does not match locator'))
            first_cell='`'+first+'`' if first else 'No entry in the initial fragment'
            shown=[n,b['place'],first_cell,'`'+b['what_the_crop_shows']+'`',r['decision']]
            lines.append('| '+' | '.join(esc(x) for x in shown)+' |')
    body=['# K45-03 · Blind collation','',f'{len(blind)} independently entered readings. {agree} agreements, {len(lines)} differences, {pending} awaiting collation.','',
          'The entries below compare the blind reading with the initial page. The comparison reconstructs all 13 original first-pass fragments from the delivered pages and both edit ledgers, verifies their SHA-256, and reads each initial span at its recorded character offset in the normalized fragment. The companion collation table holds the character offsets and final-page anchors. The comparison ignores whitespace, presentation commands and grouping braces. The initial spans preserve a visible cancellation when it explains the difference. See the audit for the full state of the ink and the Witness check in K45-03_doubts.md for later decisions.','',
          '| Scan | Place | First page | Blind reading | Settlement from the crop |','| --- | --- | --- | --- | --- |',*lines,'','## Additional observations where the letters agree','',
          'These entries record strike status, placement or residual uncertainty. They are included in the agreement count above.','',
          '| Scan | Place | Decision |','| --- | --- | --- |',*graphic_notes]
    (D/(KEY+'_blind_compare.md')).write_text('\n'.join(body)+'\n')
if __name__=='__main__':main()
