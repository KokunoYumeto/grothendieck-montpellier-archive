"""Compile the delivered fragment in a temporary standard mathematical wrapper."""
from pathlib import Path
import subprocess, tempfile, shutil
root=Path(__file__).resolve().parents[1]
build=Path(tempfile.mkdtemp(prefix='H035_latex_',dir=root.parent))
wrapper=r'''\documentclass[11pt]{article}
\pdfmapfile{+lm.map}
\pdfmapline{+msam5 MSAM5 <msam5.pfb}
\pdfmapline{+msam7 MSAM7 <msam7.pfb}
\pdfmapline{+msam10 MSAM10 <msam10.pfb}
\pdfmapline{+msbm5 MSBM5 <msbm5.pfb}
\pdfmapline{+msbm7 MSBM7 <msbm7.pfb}
\pdfmapline{+msbm10 MSBM10 <msbm10.pfb}
\pdfmapline{+eufm5 EUFM5 <eufm5.pfb}
\pdfmapline{+eufm7 EUFM7 <eufm7.pfb}
\pdfmapline{+eufm10 EUFM10 <eufm10.pfb}
\pdfmapline{+eufb5 EUFB5 <eufb5.pfb}
\pdfmapline{+eufb7 EUFB7 <eufb7.pfb}
\pdfmapline{+eufb10 EUFB10 <eufb10.pfb}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage[margin=25mm]{geometry}
\usepackage{hyperref}
\newcommand{\coker}{\operatorname{coker}}
\newcommand{\im}{\operatorname{im}}
\newcommand{\Spec}{\operatorname{Spec}}
\newcommand{\Hom}{\operatorname{Hom}}
\newcommand{\Ext}{\operatorname{Ext}}
\newcommand{\Tor}{\operatorname{Tor}}
\begin{document}
\input{PROOFS.tex}
\end{document}
'''
(build/'check.tex').write_text(wrapper)
shutil.copy2(root/'PROOFS.tex',build/'PROOFS.tex')
if not subprocess.run(['kpsewhich','pdflatex.fmt'],stdout=subprocess.DEVNULL).returncode==0:
 init=subprocess.run(['pdftex','-ini','-etex','-interaction=nonstopmode','-halt-on-error','-jobname=pdflatex','pdflatex.ini'],cwd=build,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 (root/'scripts/pdflatex_format_build.log').write_text(init.stdout)
 print('Local format initialization:',init.returncode)
 if init.returncode:raise SystemExit(init.returncode)
result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','check.tex'],cwd=build,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(root/'scripts/latex_compile.log').write_text(result.stdout)
print('Compiler: pdfLaTeX; standard wrapper; temporary build:',build)
print('Exit code:',result.returncode)
for line in result.stdout.splitlines():
 if line.startswith('!') or 'Undefined control' in line or 'Overfull' in line or 'Missing character' in line or 'Output written' in line: print(line)
raise SystemExit(result.returncode)
