#!/usr/bin/env python3
"""Compile the two contributed fragments to catch TeX errors and overflows."""
from pathlib import Path
import subprocess
import re
import time
root=Path(__file__).resolve().parents[1]
build=root/"build"
build.mkdir(exist_ok=True)
tex=r"""
\documentclass[11pt,a4paper]{article}
\usepackage[margin=26mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{longtable,booktabs}
\usepackage[authoryear]{natbib}
\usepackage{hyperref}
\hypersetup{breaklinks=true}
\setlength{\emergencystretch}{2em}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\begin{document}
\title{D and E contributions: local fragment verification}
\author{AI-produced by GPT-6 Astra (OpenAI)}
\date{19 November 2026}\maketitle
\input{../part_D.tex}
\input{../part_E456.tex}
\bibliographystyle{plainnat}
\bibliography{../references}
\end{document}
"""
(build/"fragment_check.tex").write_text(tex,encoding="utf-8")
start=time.perf_counter()
commands=[
["lualatex","-interaction=nonstopmode","-halt-on-error","fragment_check.tex"],
["bibtex","fragment_check"],
["lualatex","-interaction=nonstopmode","-halt-on-error","fragment_check.tex"],
["lualatex","-interaction=nonstopmode","-halt-on-error","fragment_check.tex"],
]
with (build/"build_commands.out").open("w",encoding="utf-8") as output:
    for cmd in commands:
        output.write("$ "+" ".join(cmd)+"\n");output.flush()
        p=subprocess.run(cmd,cwd=build,text=True,stdout=output,stderr=subprocess.STDOUT)
        if p.returncode:
            raise SystemExit(f"Failed: {cmd}; see build/build_commands.out")
log=(build/"fragment_check.log").read_text(errors="replace")
over=re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\)",log)
print("Overfull hboxes:",over)
print("Overfull hboxes >2pt:",sum(float(x)>2 for x in over))
print("Undefined references/citations:",bool(re.search("undefined",log,re.I)))
print(f"Elapsed seconds: {time.perf_counter()-start:.3f}")
