#!/usr/bin/env python3
"""Idempotent organization of the parent-owned A.1--A.4 source."""
from pathlib import Path
p = Path(__file__).resolve().parents[1]/"sections"/"part_A1234.tex"
s=p.read_text()
if r"\section{A.4." not in s:
    action_start=s.index(r"\begin{corollary}[The intrinsic multiplicative action]")
    action_end=s.index(r"\begin{proposition}[Cusp norm and decorations]",action_start)
    action=s[action_start:action_end]
    s=s[:action_start]+s[action_end:]
    orange_start=s.index(r"\begin{theorem}[The orange-slice model fails]")
    orange_end=s.index(r"\section{A.3.",orange_start)
    orange=s[orange_start:orange_end]
    s=s[:orange_start]+s[orange_end:]
    s += "\n"+r"\section{A.4. The letter to Bers and its intrinsic replacement}"+"\n\n"+orange+action
needle=r"\input{sections/C_A2e_collar.tex}"
if needle not in s:
    i=s.index(r"\section{A.3.")
    s=s[:i]+needle+"\n\n"+s[i:]
s=s.replace("Koebe's\nquarter theorem gives",r"Koebe's"+ "\n"+r"quarter theorem \citep[Appendix, pp.~10--13]{C_Siu2005} gives")
s=s.replace("Mondello's Theorem 5.4 now gives",
            r"Mondello's Theorem~5.4 \citep[p.~660]{C_Mondello2011} now gives")
s=s.replace("Penner's decoration construction uses exactly these",
            r"Penner's decoration construction \citep[\S1]{Penner1987} uses exactly these")
s=s.replace("Thus declaring $\\partial_q$ to have norm\none is independent of the choice.",
            "Thus declaring $\\partial_q$ to have norm\none is independent of the choice. This is the norm of\n"+r"\citet[Definition~1 and Lemma~2]{Wolpert2007}.")
s=s.replace("apply the\nequal-adjacent-interval condition to $H$ at $0$, and use\n$H^2=\\mathrm{id}$ and the same condition on either half.",
            "write $a(t)=|H(t)|$, so $H(-t)=a^{-1}(t)$.\nThe equal-adjacent-interval condition gives\n$K^{-1}\\le a(t)/a^{-1}(t)\\le K$. If $a(t)\\ge t$, then\n$a^{-1}(t)\\le t$ and $a(t)\\le Kt$; the reverse case gives\n$a(t)\\ge t/K$. Thus both $a(t)$ and $a^{-1}(t)$ are\ncomparable to $t$.")
p.write_text(s)
print("Root A sections organized; collar section included.")
