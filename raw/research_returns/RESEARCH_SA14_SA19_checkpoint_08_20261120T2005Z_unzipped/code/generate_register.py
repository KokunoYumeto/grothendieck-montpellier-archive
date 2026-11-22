"""Generate the complete numbered K register from the current audited result rows."""
from pathlib import Path
import csv,re,json,datetime
root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'RESEARCH_SA14_SA19_results.csv').open()))
math={'τ':r'\tau','δ':r'\delta','π':r'\pi','α':r'\alpha','μ':r'\mu',
      'λ':r'\lambda','θ':r'\theta','η':r'\eta','κ':r'\kappa','Γ':r'\Gamma',
      'Ω':r'\Omega','≥':r'\geq','≤':r'\leq','≠':r'\ne','→':r'\to',
      '↔':r'\leftrightarrow','∞':r'\infty','⊂':r'\subset','⊕':r'\oplus',
      '⊗':r'\otimes','∈':r'\in','∨':r'\vee','ℓ':r'\ell','∏':r'\prod',
      '²':'{}^2','³':'{}^3','⁴':'{}^4','⁰':'{}^0','¹':'{}^1','∗':'{}^*','̃':r'\sim'}
esc={'&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}',
     '~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}
def tex(s):
    return ''.join(('\\ensuremath{'+math[c]+'}') if c in math else esc.get(c,c) for c in s)
out=[r'\section{Numbered statement register}\label{sec:K}',
     'This register lists every current result row, including unresolved parent tasks.',
     'The identifiers are stable across the report, calculations and check-event table.',
     'The full typed statements, diplomatic French quotations and proofs occur at the',
     'locations given below. A proved special case does not change an unresolved parent',
     'task to proved. Historical attempts are retained with their dated verification state.',
     r'\begingroup\small\raggedright']
for n,r in enumerate(rows,1):
    out += [r'\par\medskip\noindent\textbf{K.'+str(n)+'. '+tex(r['id'])+' --- '+tex(r['status'])+r'.}\par',
            tex(r['statement'])+'.',
            r'\par\emph{Statement/proof location:} '+tex(r['where_proved'] or 'See the item discussion; no completed proof is claimed.')+'.']
    if r['manuscript_pages_settled']:
        out += [r'\emph{Manuscript reference:} '+tex(r['manuscript_pages_settled'])+'.']
    if r['notes']: out += [r'\par '+tex(r['notes'])]
out += [r'\endgroup']
(root/'sections/K.tex').write_text('\n'.join(out)+'\n')
result={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'rows':len(rows),'output':'sections/K.tex','source':'RESEARCH_SA14_SA19_results.csv'}
(root/'code/generate_register_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
