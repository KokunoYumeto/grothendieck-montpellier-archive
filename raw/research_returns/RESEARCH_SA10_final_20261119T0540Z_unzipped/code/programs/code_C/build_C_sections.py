#!/usr/bin/env python3
"""Build the C contribution, preserving separately audited TeX proof inputs.
Only C-owned outputs are changed. This is a reproducible typesetting step.
"""
from pathlib import Path
import re, subprocess, csv, json
W=Path(__file__).resolve().parents[1]
source=W/'agent_C.md'
s=source.read_text()
parts={}
for m in re.finditer(r'^## (C([1-5])\.(\d+))[^\n]*\n',s,re.M):
 end=re.search(r'^## ',s[m.end():],re.M)
 body=s[m.end():m.end()+end.start()] if end else s[m.end():]
 body=body.split('\nAI-produced by GPT-6 Astra')[0]
 parts[m.group(1)]=(int(m.group(2)),int(m.group(3)),m.group(0),body)
sections={1:'Deployment, simultaneous cones, and exit categories',2:'Projection control and Thom--Mather data',3:'Corners, flags, and moduli incidences',4:'Pro-neighbourhoods, holinks, and cohomology',5:'The consequence margins in TOP, PL, and smooth'}
short={
'C1.01':'Refuted: weak conical data do not imply fibrancy',
'C1.02':'Proved under fibrancy: the complete Segal object',
'C1.03':'Proved: the simultaneous-cone construction',
'C1.04':'Proved under the corrected hypotheses: incidence groupoids',
'C2.01':'Refuted: the bare intersection axioms imply transitivity',
'C2.02':'Proved: the projection-control repair',
'C2.03':'Proved: one radius level does not determine control',
'C2.04':'Refuted: the bare recapitulation is Thom--Mather data',
'C2.05':'Known, with derivation: the smooth resolution theorem',
'C3.01':'Refuted: precylindrical alone implies a manifold',
'C3.02':'Proved: Boolean intervals of flags',
'C3.03':'Refuted on coarse moduli: contractions remove isotropy',
'C3.04':'Proved: the exact local corner criterion',
'C4.01':'Proved for finite metric HSS: the germ comparisons',
'C4.02':'Proved: the relative holink comparison',
'C4.03':'Proved: the finite cover spectral sequence',
'C4.04':'Refuted: HSS alone gives conical collars',
'C4.05':'Proved with proper controlled collars: germ and face',
'C4.06':'Proved: the canonical normal-crossings comparison',
'C5.01':'Proved: the component order under local path connectivity',
'C5.02':'Refuted in all three categories: automatic transversality',
'C5.03':'Refuted in TOP: automatic manifold fibres',
'C5.04':'Refuted in TOP: automatic manifold faces',
'C5.05':'Proved for PL bundles and smooth submersions',
'C5.06':'Refuted in PL and smooth: raw fibrancy suffices',
'C5.07':'Refuted in TOP: connected components suffice',
'C5.08':'Proved and refuted: the matrix and category digression',
}
page={
'C1.01':'150/023,036,039','C1.02':'150/039,067-070','C1.03':'150/043','C1.04':'150/039-043;151/044',
'C2.01':'150/065-066','C2.02':'150/065-066','C2.03':'150/065-066','C2.04':'150/065-066','C2.05':'150/065-066',
'C3.01':'150/028-030','C3.02':'150/028-029,039','C3.03':'150/039;151/044','C3.04':'150/021,023,028-030',
'C4.01':'150/073-084: (51),(56),(57),(69)','C4.02':'150/079-084','C4.03':'150/083-084: (73)','C4.04':'150/023,036','C4.05':'150/039,073-084','C4.06':'147/173-177: (286)-(294)',
'C5.01':'150/068-071','C5.02':'150/062-063','C5.03':'150/051,063','C5.04':'150/051,067','C5.05':'150/051,062,063,067,070-071','C5.06':'150/051,063','C5.07':'150/068-071','C5.08':'150/051,062,063,067,070-071'}
dep={
'C1.01':'Explicit two-stratum mapping-cylinder example','C1.02':'Homotopy pullbacks of Hurewicz fibrations; finite grading','C1.03':'Explicit three transition families; recursive collar pushout','C1.04':'C1.02-C1.03;C1.B1-B3;C2.05;C3.03;A.1',
'C2.01':'Finite twist certificate; primary150/065','C2.02':'C2.01 subset and projection identities','C2.03':'Explicit two-retraction formula','C2.04':'One-stratum Cantor example','C2.05':'Albin2016 Th6.3;ALMP Props2.2-2.7;ABP Th2.10,2.13;Mather section7',
'C3.01':'Cantor product collar','C3.02':'Finite subset argument;flag program','C3.03':'Looijenga Th8.11,9.13,Prop9.16;Mobius program;local homology','C3.04':'Specified collar product charts;C2.05;C5.03-C5.04',
'C4.01':'Quinn Prop3.2 and finite intersection descent','C4.02':'Quinn Prop3.2;fixed homotopy;path shortening','C4.03':'Finite actual open cover;flabby double complex;derived limits','C4.04':'Quinn p452;explicit shrinking hedgehog','C4.05':'C2.05;C4.01;C1.B2a;proper variable-radius tubes','C4.06':'Primary147/173-177;adapted normal derivative;positive scaling;kernel contraction',
'C5.01':'Proper local immersion;path lifting;bounded lower intervals','C5.02':'Explicit smooth and PL corner maps','C5.03':'Cannon Th1.5,Cor3.6;Poincare sphere suspension','C5.04':'C5.03;quadrant collar;local homology','C5.05':'PL link criterion;smooth submersion charts;C5.01','C5.06':'Zeeman p347;Milnor Th9.1,PropA;Ferry Th1;boundary-spin and height models','C5.07':'Bing Example1;explicit ray compactification;full Hurewicz lifting','C5.08':'C5.01-C5.07;invariance of domain;primary margin scans'}
chunks=[];last=0;rows=[]
for ident,(part,num,heading,body) in sorted(parts.items(),key=lambda x:(x[1][0],x[1][1])):
 if part!=last:
  chunks.append(f'# C.{part}. {sections[part]}\n');last=part
 if ident=='C1.04': chunks.append('\\input{C1_collage_B}\n')
 chunks.append(f'## {ident} — {short[ident]}\n\n'+body)
 if 'Refuted' in heading: status='Refuted; corrected statement proved'
 elif 'Proved and refuted' in heading: status='All listed readings proved or refuted; exact scope stated'
 elif 'Known' in heading: status='Known with explicit derivation'
 else: status='Proved under stated hypotheses'
 rows.append([ident,short[ident],status,'C_sections.tex: '+ident,dep[ident],page[ident],'Exact category, finiteness, and ambiguity specified in statement'])
md='\n\n'.join(chunks)
# Normalize the few old plain-text formulas before the generic Unicode pass.
md=md.replace('Σ_d′',r'\(\Sigma_{d\prime}\)').replace('Σ_d',r'\(\Sigma_d\)')
md=md.replace('H¹(C,T_C)',r'\(H^1(C,T_C)\)').replace('H⁰(C,2K_C)',r'\(H^0(C,2K_C)\)')
md=md.replace('C₀→N(C)₁^eq',r'\(C_0\to N(C)_1^{\mathrm{eq}}\)')
md=md.replace('B×[0,δ)^k',r'\(B\times[0,\delta)^k\)').replace('R^d',r'\(\mathbb R^d\)').replace('x^k',r'\(x^k\)')
(W/'C_paper_source.md').write_text(md)
res=subprocess.run(['pandoc','-f','markdown+raw_tex+tex_math_single_backslash','-t','latex','--wrap=none'],input=md,text=True,capture_output=True,check=True)
tex=res.stdout
symbols={'Σ':r'\Sigma','Π':r'\Pi','π':r'\pi','α':r'\alpha','δ':r'\delta','ε':r'\epsilon','θ':r'\theta','ι':r'\iota','×':r'\times','→':r'\to','←':r'\leftarrow','≤':r'\le','≥':r'\ge','∈':r'\in','⊂':r'\subset','∩':r'\cap','∪':r'\cup','∞':r'\infty','∂':r'\partial','∐':r'\coprod','⨿':r'\amalg','∘':r'\circ','≅':r'\cong','∼':r'\sim','±':r'\pm','∑':r'\sum','·':r'\cdot','′':r'\prime','−':'-'}
sup=dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻','0123456789-'))
sub=dict(zip('₀₁₂₃₄₅₆₇₈₉ᵢⱼₖ','0123456789ijk'))
for ch,cmd in symbols.items():tex=tex.replace(ch,r'\ensuremath{'+cmd+'}')
tex=re.sub('['+''.join(sup)+']+',lambda m:r'\ensuremath{{}^{'+''.join(sup[c] for c in m.group())+'}}',tex)
tex=re.sub('['+''.join(sub)+']+',lambda m:r'\ensuremath{{}_{'+''.join(sub[c] for c in m.group())+'}}',tex)
tex=tex.replace('Č',r'\v{C}').replace('§',r'\S{}')
tex='% AI-produced by GPT-6 Astra (OpenAI), 2026-11-19. Generated by code_C/build_C_sections.py.\n'+tex
(W/'C_sections.tex').write_text(tex)
with (W/'RESULTS_C.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writerows(rows)
print(json.dumps({'statements':len(parts),'tex_bytes':len(tex.encode()),'remaining_non_ascii':sorted(set(c for c in tex if ord(c)>127)),'outputs':['C_paper_source.md','C_sections.tex','RESULTS_C.csv']}))
