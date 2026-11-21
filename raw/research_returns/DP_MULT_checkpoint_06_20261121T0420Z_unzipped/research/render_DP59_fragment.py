#!/usr/bin/env python3
"""Faithfully turn the frozen complete DP59 proof into an intended TeX fragment."""
from pathlib import Path
import re,subprocess
here=Path(__file__).resolve().parent
memo=(here/'theta_translate_span_DP59.md').read_text()
parts=re.split(r'^## ([0-9]+)\. (.+)\n',memo,flags=re.M)
sections={int(parts[i]):(parts[i+1],parts[i+2]) for i in range(1,len(parts),3)}
def tex(s):
 out=subprocess.run(['pandoc','--from=markdown+tex_math_single_backslash','--to=latex','--wrap=none'],input=s,text=True,check=True,capture_output=True).stdout
 out=out.replace('\\tightlist\n','')
 def code(m):
  content=m.group(1)
  if '/' in content or '.lean' in content:
   content=content.replace('\\_','_').replace('\\textbackslash{}','\\')
   return '\\path{'+content+'}'
  return m.group(0)
 out=re.sub(r'\\texttt\{([^{}]*)\}',code,out)
 return out
out='\\subsection{The integral span of permitted theta translates}\n\n'
out+='\\begin{theorem}[DP59: permitted translates contain explicit sharp witnesses]\\label{DP59}\n'+tex(sections[1][1])+'\\end{theorem}\n\n'
out+='\\paragraph{Exact inputs and source interfaces.}\n'+tex(sections[2][1])+'\n\\begin{proof}\n'
for n in range(3,9):
 title,body=sections[n]
 out+='\\emph{'+title+'.}\n'+tex(body)+'\n'
out+='\\end{proof}\n'
for old,new in {
 'Its existence is proved in §8.':'Its existence is proved in the arithmetic-realization part of the proof.',
 'the uniqueness in §4 applies':'the uniqueness of symmetric finite-order lifts proved above applies',
 'as used in §1.':'as used in the statement.',
 'already verified in §3.':'verified in the first part of the proof.',
 'https://pazuki.perso.math.cnrs.fr/index\\_fichiers/Mumford66.pdf .':'\\url{https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf}.',
 'pages289 and297':'pages 289 and 297'
}.items():
 out=out.replace(old,new)
(here/'DP59_integrated_fragment.tex').write_text(out)
print('Saved complete intended DP59 fragment; whole-proof preservation reading is still required.')
