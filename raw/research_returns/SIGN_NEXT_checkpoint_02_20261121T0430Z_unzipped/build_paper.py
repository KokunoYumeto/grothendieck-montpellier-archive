"""Build the self-contained SIGN_NEXT.tex from audited contributions."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
parts=[
 ROOT/'work/root/preamble_and_introduction.tex',
 ROOT/'work/critical_lefschetz/contribution.tex',
 ROOT/'work/root/root_contribution.tex',
 ROOT/'work/integral_fock/contribution.tex',
 ROOT/'work/root/arithmetic_scope.tex',
 ROOT/'work/singular_fibres/arithmetic_review/true_stabilizer_and_full_local_bound.tex',
 ROOT/'work/singular_fibres/arithmetic_review/untwisted_model_obstruction.tex',
 ROOT/'work/critical_lefschetz/single_family_m2.tex',
 ROOT/'work/critical_lefschetz/diamond_fourier_anchor.tex',
 ROOT/'work/singular_fibres/arithmetic_review/pointwise_inert_valuation.tex',
 ROOT/'work/root/exterior_index_formula.tex',
 ROOT/'work/singular_fibres/contribution.tex',
 ROOT/'work/root/boundaries.tex',
 ROOT/'work/root/bibliography.tex',
 ROOT/'work/singular_fibres/bibliography.tex',
]
text='\n\n'.join(p.read_text() for p in parts)
kernel=(ROOT/'work/integral_fock/kernel_intertwiner.tex').read_text()
text=re.sub(r'\\input\{[^}]*kernel_intertwiner\.tex\}',lambda _:kernel,text)
# Recursively flatten the remaining local proof components.
while re.search(r'\\input\{([^{}]+)\}',text):
 def include(match):
  p=ROOT/match.group(1)
  if not p.exists():raise FileNotFoundError(p)
  return p.read_text()
 text=re.sub(r'\\input\{([^{}]+)\}',include,text)
# If the agent has not yet inserted the include, place it before heights.
if 'Statement IF-08' not in text:
 anchor=r'\section{Cote 44:'
 index=text.index(anchor)
 text=text[:index]+kernel+'\n\n'+text[index:]
text=text.replace(r'C_{\mathrm{Gr}}',r'C_{\mathrm G}')
# Let TeX break source paths without altering mathematical text.
def source_path(match):
 s=match.group(1)
 if '/' in s or len(s)>18:
  return r'\path{'+s.replace(r'\_','_')+'}'
 return match.group(0)
text=re.sub(r'\\texttt\{([^{}]+)\}',source_path,text)
text+='\n\\end{thebibliography}\n\\end{document}\n'
(ROOT/'SIGN_NEXT.tex').write_text(text)
print('Built SIGN_NEXT.tex:',len(text),'characters; source files:',len(parts))
