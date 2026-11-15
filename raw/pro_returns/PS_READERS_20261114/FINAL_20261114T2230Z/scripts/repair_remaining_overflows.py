"""Install four local source-layout repairs from the measured proof overflows."""
from pathlib import Path
import json
from build_readers import normalize, repair_diagram_separators, repair_macro_layout, preserve_front_lineation

P=Path(__file__).resolve().parents[1]
path=P/'records/TYPESETTING_PATCHES.json'
patches=json.loads(path.read_text())
def add(key,ident,before,after,problem,action):
    patches[:]=[p for p in patches if p['id']!=ident]
    patches.append(dict(key=key,id=ident,before=before,after=after,problem=problem,action=action))

add('ps_134-4_034','LAYOUT-1344-034-contractibility',
    r'\xout{the homotopy}\inserted[typed]{contractibility}',
    r'\xout{the homotopy}\allowbreak{}\inserted[typed]{contractibility}',
    'The adjacent cancelled phrase and its typed replacement caused a 9.6828 pt diplomatic paragraph overflow.',
    'Permit a zero-width line break between the cancelled phrase and its replacement; retain the printed text and both layers.')
add('ps_134-4_036','LAYOUT-1344-036-definition',
    r'\deleted{to \xout{\unsure{defin}}}\inserted{definition}',
    r'\deleted{to \xout{\unsure{defin}}}\allowbreak{}\inserted{definition}',
    'The nested cancellation followed by its replacement caused an 11.59152 pt diplomatic paragraph overflow.',
    'Permit a zero-width line break after the nested cancelled phrase, preserving its doubt mark and the following insertion.')
add('ps_134-6_092','LAYOUT-1346-092-special-case',
    r'hence B=A and $A^\wedge',
    'hence B=A and\\newline\n$A^\\wedge',
    'The unbreakable inline equivalence caused a 13.2669 pt diplomatic overflow.',
    'Begin the inline equivalence on the next line after and; preserve the formula and its following cancellation. The initial internal breakpoint did not remove the measured overflow.')

key='ps_134-6_095'
s=(P/'checked_pages'/(key+'.tex')).read_text()
s=preserve_front_lineation(repair_macro_layout(repair_diagram_separators(normalize(s,key,[]),key,[]),key,[]),key,[])
start=s.index(r'\[ (75)')
end=s.index(r'\]',start)+2
before=s[start:end]
after=before.replace(r'\textcolor{black}{\begin{array}{ll}',r'\textcolor{black}{\begin{array}{l}',1)
after=after.replace(r'\quad d) & ',r'\quad\begin{array}{ll} d) & ',1)
dend=r'\underline{\mathrm{Hom}}(L,F) \\[2ex]'
assert after.count(dend)==1
after=after.replace(dend,r'\underline{\mathrm{Hom}}(L,F)\end{array} \\[2ex]',1)
old=r'''\mathrm{Hom}(L,F) : \hand{\mathcal{A}}_{ab}{}^{o} \hand{\rightarrow \mathcal{M}} \ \text{ commutes to small in-} \\
 & \phantom{\text{The functor } L \mapsto \mathrm{Hom}(L,F) : \mathcal{A}_{ab}{}^{o} \rightarrow \mathcal{M}} \ \text{ verse limits} \\
e') & \text{Similar statement as e) for } \hand{L \mapsto} \underline{\mathrm{Hom}}(L,F) \ : \ \hand{\mathcal{A}}_{ab}{}^{o} \hand{\rightarrow \mathcal{A}_{\mathcal{M}}}.'''
new=r'''\mathrm{Hom}(L,F) \\
 & : \hand{\mathcal{A}}_{ab}{}^{o} \hand{\rightarrow \mathcal{M}} \ \text{ commutes to small in-} \\
 & \text{verse limits} \\
e') & \text{Similar statement as e) for } \\
 & \hand{L \mapsto} \underline{\mathrm{Hom}}(L,F) \ : \ \hand{\mathcal{A}}_{ab}{}^{o} \hand{\rightarrow \mathcal{A}_{\mathcal{M}}}.'''
assert after.count(old)==1
after=after.replace(old,new,1)
add(key,'LAYOUT-1346-095-formulaire',before,after,
    'Display (75) exceeded the line by 178.40779 pt diplomatically, 83.32445 pt with apparatus and 75.39445 pt in the reading form. Mixed one-cell nested groups and a two-cell outer row inflated the table width; the prose in e/e-prime was also unbreakable.',
    'Use one outer alignment column and a separate two-column row for d; break the e and e-prime entries at the functor/type/prose boundaries and remove a purely invisible phantom indent. Preserve every label, brace, formula, cancellation and doubtful reading; no scaling is applied.')
path.write_text(json.dumps(patches,indent=2)+'\n')
print(json.dumps({'local_layout_patches':len(patches),'new_repairs':4}))
