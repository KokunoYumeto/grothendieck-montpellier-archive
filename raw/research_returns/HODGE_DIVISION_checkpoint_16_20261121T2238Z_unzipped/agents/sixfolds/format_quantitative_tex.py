"""Convert the full research note to TeX, preserving every paragraph.

The note's original displays are already TeX.  Plain-text inline mathematical
tokens are normalized before Pandoc parses Markdown, so pullback stars are
never accidentally treated as emphasis.  This is an editorial utility, not a
mathematical certificate.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
source = (ROOT / "quantitative_cm_seed.md").read_text()

special = {
    "j*Θ=2θ_product": r"j^*\Theta=2\theta_{\mathrm{prod}}",
    "P=2^2048": r"P=2^{2048}",
    "#(C−C)∩J[q]≤108q⁴": r"\#((C-C)\cap J[q])\le108q^4",
    "Σ_{p|N}1/p<1/500": r"\sum_{p\mid N}1/p<1/500",
    "N/p_min": r"N/p_{\min}",
    "p_min>P": r"p_{\min}>P",
    "I_ZH⊠I_−ZH": r"I_{Z_H}\boxtimes I_{-Z_H}",
    "e^(−a_dz)P_d(z)": r"e^{-a_d z}P_d(z)",
    "H_dt=0": r"H_d t=0",
    "Q_u,Q_−u": r"Q_u,Q_{-u}",
    "Q_uQ_−u=−4d": r"Q_uQ_{-u}=-4d",
    "−ab(Q_u+Q_−u)": r"-ab(Q_u+Q_{-u})",
    "D_CM(m)": r"D_{\rm CM}(m)",
    "S_ij": r"S_{ij}",
    "VS_k≤D_CM(m)": r"VS_k\le D_{\rm CM}(m)",
    "D^−r": r"D^{-r}",
    "L^−1": r"L^{-1}",
    "L_T^−1": r"L_T^{-1}",
    "M_i=D^−r⊗h^(R−i)": r"M_i=D^{-r}\otimes h^{R-i}",
    "R³π_*L^−1": r"R^3\pi_*L^{-1}",
    "C^(2)→Θ": r"C^{(2)}\to\Theta",
    "C×C→C^(2)": r"C\times C\to C^{(2)}",
    "C×C→C^(2)≅Θ⊂J": r"C\times C\to C^{(2)}\simeq\Theta\subset J",
    "[[0,−d],[d,0]]": r"\bigl(\begin{smallmatrix}0&-d\\d&0\end{smallmatrix}\bigr)",
    "[[2,2],[2,−2]]": r"\bigl(\begin{smallmatrix}2&2\\2&-2\end{smallmatrix}\bigr)",
    "H^(6−i)(Y,L(−qH_b))": r"H^{6-i}(Y,\mathcal L(-qH_b))",
    "H^(6−i)(C×A,L_C(−qH_b))": r"H^{6-i}(C\times A,\mathcal L_C(-qH_b))",
    "H^i(T,ω_T⊗L_T^−1⊗f*O(qH_b))=0": r"H^i(T,\omega_T\otimes\mathcal L_T^{-1}\otimes f^*O(qH_b))=0",
    "T_g=t_{a_g}*⊗P_g": r"T_g=t_{a_g}^*\otimes P_g",
    "T′_g=t_{a′_g}*⊗[r]*P_g": r"T'_g=t_{a'_g}^*\otimes[r]^*P_g",
    "t_{a′_g}*[r]*=[r]*t_{a_g}*": r"t_{a'_g}^*[r]^*=[r]^*t_{a_g}^*",
    "T′=T×_{A,[s]}A": r"T'=T\times_{A,[s]}A",
    "EGAIV₃11.3.1)": r"EGA IV$_3$, 11.3.1)",
}

char_map = {
    'Θ':r'\Theta ', 'θ':r'\theta ', 'α':r'\alpha ', 'γ':r'\gamma ',
    'δ':r'\delta ', 'κ':r'\kappa ', 'ω':r'\omega ', 'π':r'\pi ',
    'μ':r'\mu ', 'χ':r'\chi ', 'Σ':r'\sum ', 'Δ':r'\Delta ',
    '≤':r'\le ', '≥':r'\ge ', '∈':r'\in ', '⊂':r'\subset ',
    '→':r'\to ', '↦':r'\mapsto ', '×':r'\times ', '⊗':r'\otimes ',
    '⊕':r'\oplus ', '⊠':r'\boxtimes ', '∩':r'\cap ', '≅':r'\simeq ',
    '⟨':r'\langle ', '⟩':r'\rangle ', '−':'-', '±':r'\pm ',
    '√':r'\sqrt ', '′':"'", '∫':r'\int ', '…':r'\ldots ',
}
supers = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789')
subs = str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789')
exclude = {'HODGE_DIVISION','HECKE_DIV','DEG_L'}
math_chars = r'[_^=<>α-ωΑ-Ω⁰¹²³⁴⁵⁶⁷⁸⁹₀-₉∈≤≥→↦⊂⊕⊗⊠−±′×̂∫√]'

def tex_math(t):
    if t in special:
        return special[t]
    t = t.replace('Ĵ',r'\widehat{J}').replace('Â',r'\widehat{A}')
    t = re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+',lambda m:'^{'+m[0].translate(supers)+'}',t)
    t = re.sub(r'[₀₁₂₃₄₅₆₇₈₉]+',lambda m:'_{'+m[0].translate(subs)+'}',t)
    t = re.sub(r'\^\(([^()]*)\)',r'^{\1}',t)
    t = re.sub(r'\^−([0-9a-zA-Z]+)',r'^{-\1}',t)
    t = re.sub(r'\^([0-9]{2,})',r'^{\1}',t)
    t = t.replace('Q_−u','Q_{-u}').replace('D_CM','D_{\\rm CM}')
    t = t.replace('p_min','p_{\\min}')
    # Every star in a mathematical inline token here denotes a dual or pullback.
    t = t.replace('*','^*')
    for old,new in char_map.items():
        t = t.replace(old,new)
    t = t.replace('#',r'\#')
    for op in ['Pic','NS','Ext','Perf','FM','Stab','ker','diag','binom','pd','exp','gcd']:
        t = re.sub(r'(?<![A-Za-z\\])'+op+r'(?=[(^{_])',lambda m:r'\operatorname{'+m[0]+'}',t)
    t = re.sub(r'(?<![A-Za-z\\])ch(?=[_{])',lambda m:r'\operatorname{ch}',t)
    return t

def convert_token(t):
    if t in exclude or t.startswith(('http:','https:','arXiv:','DOI')):
        return t
    if t == 'EGAIV₃11.3.1)':
        return special[t]
    # Keep ordinary prose suffixes outside the mathematical token.
    suffix=''
    for end in ['-degree','-fibre,','-stable']:
        if t.endswith(end):
            t,suffix=t[:-len(end)],end
            break
    trailing=''
    while t and t[-1] in ',.;:':
        trailing=t[-1]+trailing
        t=t[:-1]
    matched = bool(re.search(math_chars,t) or re.search(r'[A-Za-z\]]\*',t)
                   or re.search(r'^[A-Za-z]+\([^ ]*\)$',t)
                   or re.search(r'^[A-Za-z]+\[[^ ]*\]$',t)
                   or re.search(r'^[A-Za-z]+\+[A-Za-z]+$',t))
    # Mathematical single-letter variables are kept as math in running text.
    matched = matched or bool(re.fullmatch(r'[CDEFGHJKLMNPQRTUVWXYZbcdefghijkmnpqrstuvxyz]',t))
    if not matched:
        return t+trailing+suffix
    return '$'+tex_math(t).strip()+'$'+trailing+suffix

out=[]
display=False
for line in source.splitlines():
    if line.lstrip().startswith(r'\['):
        display=True
    if display:
        out.append(line)
        if line.lstrip().startswith(r'\]'):
            display=False
        continue
    if line.startswith('#'):
        out.append(line)
        continue
    # Preserve strong-emphasis markers before processing the mathematical text.
    placeholders={}
    def protect(m):
        key='BOLDPLACEHOLDER'+str(len(placeholders))
        placeholders[key]=m[0]
        return key
    line=re.sub(r'\*\*.*?\*\*',protect,line)
    line=''.join(convert_token(tok) if not tok.isspace() else tok
                 for tok in re.split(r'(\s+)',line))
    for key,val in placeholders.items():
        line=line.replace(key,val)
    out.append(line)

normalized='\n'.join(out)+'\n'
md=ROOT/'quantitative_cm_seed_math.md'
md.write_text(normalized)
result=subprocess.check_output(['pandoc','-f','markdown+tex_math_single_backslash+tex_math_dollars',
                                '-t','latex',str(md)],text=True)
result=result.replace('\\tightlist\n','')
result=result.replace('\\section{Explicit regularity',
                      '\\section{Explicit regularity',1)
for n in range(1,6):
    result=re.sub(r'(\\subsection\{SF-QC0'+str(n)+r'\.[\s\S]*?\})\\label\{[^}]*\}',
                  r'\1\\label{SF-QC0'+str(n)+'}',result,count=1)
result='% Generated from the full note by format_quantitative_tex.py; no proof paragraphs omitted.\n'+result
(ROOT/'quantitative_cm_section.tex').write_text(result)
print(f'Wrote {len(result.splitlines())} TeX lines; source {len(source.splitlines())} Markdown lines.')
