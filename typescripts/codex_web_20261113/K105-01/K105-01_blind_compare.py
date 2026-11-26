"""Compare each previously recorded crop reading with its first and current page block.
Run with Python 3 in any directory. The TSV preserves fuller visual notes after //.
For a focus containing ||, each separate part must occur in order in the scoped block.
"""
from pathlib import Path
import csv,json,re,unicodedata
ROOT=Path(__file__).resolve().parent
def normal(s):
    s=unicodedata.normalize('NFC',s).replace('’',"'")
    s=re.sub(r'\\(?:unsure|illegible|deleted|inserted|text|mathrm|uline|uuline|margin|handwritten|boxed|mspage|textcircled)\b','',s)
    s=re.sub(r'\\(?:longrightarrow|rightarrow|to)\b','→',s)
    s=re.sub(r'\\(?:Longrightarrow|Rightarrow)\b','⇒',s)
    s=s.replace(r'\colon',':').replace(r'\,','').replace(r'\ ','').replace(r'\!','')
    return re.sub(r'[\s~{}$]','',s)
def present(focus,tex):
    hay=normal(tex); at=0
    for frag in focus.split(' || '):
        x=normal(frag)
        p=hay.find(x,at)
        if p<0:return False
        at=p+len(x)
    return True
def main():
    locs=json.loads((ROOT/'K105-01_blind_locations.json').read_text())
    rows=list(csv.DictReader((ROOT/'K105-01_blind.tsv').open(),delimiter='\t'))
    lines=['# Blind collation','','Each crop transcription was saved before the page file was reopened. On scan 12 the crop index exposed first-pass excerpts before that record was saved. The focus is the text before ` // `. The locations file retains the first-pass fragment and its page-block index. The comparison preserves case and distinguishes glyphs, accents, subscripts, superscripts and primes. Page-state decisions and readings around the focus are also recorded in the audit.','','| Scan | Place | Independent reading | First-pass comparison | Current page | Decision from ink |','|---|---|---|---|---|---|']
    count=0; divergent=0
    for row in rows:
        n=int(row['scan']); z=row['place']; key=f'{n}/{z}'
        if key not in locs:raise ValueError('Missing locator '+key)
        entry=locs[key]; focus=row['what_the_crop_shows'].partition(' // ')[0]
        f=ROOT/'pages'/f'K105-01_105_scan{n:03}.tex'
        blocks=f.read_text().strip().split('\n\n')
        block=blocks[entry['block']]
        before=present(focus,entry['first']); after=present(focus,block)
        if not before or not after or entry['difference']:
            count+=1
            divergent+=int(not before)
            cells=[str(n),z,focus,'agrees' if before else 'differs','present' if after else 'different reading retained',entry['decision']]
            lines.append('| '+' | '.join(x.replace('|','&#124;').replace('\n',' ') for x in cells)+' |')
    lines+=['',f'{len(rows)} places were recorded. {divergent} comparison strings differ from the first pass after normalization. The table lists {count} places including differences in alternative order, undertext, punctuation or placement that a string search alone cannot measure. Entries that say “agrees” may differ outside the short comparison string.','', '## Additional readings and all page edits from the audit','','| Scan or place | Finding or change |','|---|---|']
    for scan,detail in [['2, printer heading', 'Compared print cells and spaces. The header is “3 3 -- N O D E E 3 3”. The dots previously read in the header are ground specks.'], ['2, handwritten material', 'Marked the manuscript blocks on the reused sheet as handwritten. The two live printer fragments retain their own alignment.'], ['5, Fl(A)', 'The raised terminal of l belongs to the letter. Removed the extra stop after Fl.'], ['10, inner Hom', 'At the darkest overwritten argument a small oblique oval supports a tentative alpha. Replaced the temporary word-level illegibility mark there with a doubtful mathematical symbol.'], ['12, independence of the second reading', 'The crop-location index contained first-pass excerpts before the crop TSV was saved. The page file itself was reopened after the TSV was written.'], ['16, detached conclusion', 'Matched f∈W in the separate block below the square. A prior comparison had searched for it in the preceding block.'], ['2', '3.3 -- NODE E33 → 3 3 -- N O D E E 3 3'], ['2', '\\deleted{\\unsure{asphérique}} \\qquad \\unsure{asphérique} → \\deleted{\\unsure{0-connexe}} \\qquad \\unsure{0-connexe}'], ['2', 'text{cônes gauches → text{Cônes gauches'], ['2', 'cofibrations \\inserted{entre cat. finies}, entre objets, alors est → cofibrations triviales \\inserted{entre cat. finies}, alors il est'], ['3', '\\unsure{Néanmoins} → \\unsure{Notamment|Néanmoins}'], ['3', '\\unsure{on}} or → \\unsure{ou|on}} Or'], ['3', "ce n'en est une fibration → ce n'est ni une fibration"], ['5', '\\mathrm{Fl.}(A) → \\mathrm{Fl}(A)'], ['5', 't=vu → f=vu'], ['5', 'u,v,t → u,v,f'], ['5', '\\unsure{TF\\subset} → \\unsure{TF\\subset|TF_0}'], ['5', '\\inserted{class} → \\inserted{\\unsure{class|element}}'], ['7', 'do \\deleted{only} make → do only make'], ['7', 'Consider \\deleted{bet} → Consider \\deleted{\\unsure{let|bet}}'], ['7', '\\deleted{consider} → \\deleted{Consider}'], ['10', '(i)+(ii)\\Longrightarrow → (i)\\unsure{+}(ii)\\Longrightarrow'], ['10', "\\deleted{\\unsure{\\mathrm{Hom}(i,f)}}\\inserted{\\alpha(i,f)}\\bigr) → \\inserted{\\unsure{\\mathrm{Hom}}(\\deleted{\\illegible{1}}\\unsure{i'|i},f)}\\bigr)"], ['10', 'the first hand \\unsure{member} → the first hand \\unsure{expression|member}'], ['12', '\\text{\\inserted{(Boxes)}} → \\inserted{(B_0\\times e)\\cup}'], ['12', '\\deleted{\\unsure{I\\times}}B_0 → \\deleted{\\unsure{I}}\\times B_0'], ['12', "i'\\boxtimes i\\unsure{?} → i'\\boxtimes i^{\\unsure{*|'}}"], ['12', '\\unsure{property|possibility} → \\unsure{possibility|property}'], ['13', 'UNIT=SYSTSO, → UNIT=\\unsure{SYSTSO|SYSTS0},'], ['14', "\\underbrace{(A'\\times B_0)\\times\\deleted{\\unsure{B}}I} → \\underbrace{(A'\\times B_0)}\\times\\deleted{\\unsure{B}}I"], ['14', 'using reasonable properties → using \\unsure{reasonable|reasonably} properties'], ['14', 'factorizability \\deleted{\\unsure{of}} → factorizability \\deleted{\\unsure{of|any $f$}}'], ['14', 'difficulty for factorisation  → difficulty for factorisation, '], ['16', '\\unsure{then|thu} → \\unsure{then|take}'], ['16', '\\text{ is \\unsure{such|in}} → \\unsure{\\in W|\\text{is such}}'], ['16', '$\\{0,1\\}$ in it can be \\unsure{considered|candidate} \\unsure{$\\Longleftrightarrow$} but this is \\unsure{injective|indeed} true → $\\{0,1\\}_A$ can be \\unsure{embedded|imbedded} in \\unsure{injective} $\\Longleftrightarrow$ but this is always true'], ['16', '\\boxed{(L_A\\longrightarrow e)\\in UW}\\tag*{\\textcircled{1}} → \\text{\\textcircled{1}}\\quad\\boxed{(\\overset{\\text{\\inserted{Lawvere element}}}{L}_A\\longrightarrow e)\\in UW}'], ['16', '  \\inserted{Lawvere element} → (absorbed into its attachment site)'], ['16', '\\unsure{\\underline I} → \\underline I'], ['17', 'TAILLE~MINIMUM → TAILLE~MINIMUN'], ['18', '\\inserted{equivalent \\unsure{with}} → \\inserted{equivalent \\unsure{to|with}}'], ['18', '\\margin{\\uline{to make explicit}} → \\margin{\\uline{to write explicit}}'], ['18', '\\boxed{(I\\longrightarrow e)\\in UW.\\quad\\text{for any }I\\text{ in the bunch}}\\tag*{\\textcircled{2}} → \\text{\\textcircled{2}}\\quad\\boxed{(I\\longrightarrow e)\\in UW.\\quad\\text{for any }I\\text{ in the bunch}}'], ['18', '\\boxed{\\text{monomorphisms in }W\\text{ by cobase extension}}\\tag*{\\textcircled{3}} → \\text{\\textcircled{3}}\\quad\\boxed{\\text{monomorphisms in }W\\text{ by cobase extension}}'], ['18', 'W\\ \\text{stable by direct factors}\\qquad\\text{(not \\uline{a consequence of saturation}?)}\\tag*{\\textcircled{5}} → \\text{\\textcircled{5}}\\quad W\\ \\text{stable by direct factors}\\qquad\\text{(not \\uline{a consequence of saturation}?)}'], ['18', 'bend left=55,"\\unsure{=}"\']\\arrow[r,hook,"f"\'] → bend left=55,"\\unsure{=}"\']\\arrow[r,hook,no head,"f"\']']]:
        lines.append('| '+scan+' | '+detail.replace('|','&#124;')+' |')
    lines+=['','The comparison table records decisions made at the second reading. Final changes after comparison with the attached witness are individually identified in the last section of K105-01_doubts.md.','']
    (ROOT/'K105-01_blind_compare.md').write_text('\n'.join(lines))
if __name__=='__main__':main()
