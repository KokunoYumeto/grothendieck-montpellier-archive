"""One-time editorial reordering of the initial A.1/A.2/A.4 draft."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'sections'/'part_a14.tex'
s=p.read_text()
def block(start,end):
    global s
    a=s.index(start); b=s.index(end,a)
    out=s[a:b]; s=s[:a]+s[b:]
    return out
cusp=block('\\begin{proposition}[Known with derivation: cusp norms', '\\begin{theorem}[Proved: metric comparison')
collar=block('\\begin{theorem}[Proved: metric comparison', '\\begin{proposition}[Refuted, with rechecked extremal')
orange=block('\\begin{proposition}[Refuted, with rechecked extremal', '\\begin{lemma}[Proved: the tensor')
orangejet=block('\\begin{corollary}[Refuted: fixed concentric', '\\subsection{The canonical bundle')
grafting=s[s.index('\\subsection{The canonical bundle'):]
s=s[:s.index('\\subsection{The canonical bundle')]
cut=s.index('\\section{A.2.')
parts={'part_a1.tex':s[:cut],
       'part_a2.tex':s[cut:]+'\n\\subsection{Cusp norms and the collar question}\n'+cusp+collar,
       'part_a4.tex':'\\section{A.4. The letter to Bers}\n'+orange+orangejet+grafting}
for name,body in parts.items():
    dest=ROOT/'sections'/name
    if dest.exists(): raise RuntimeError('This editorial script is one-time only: '+name)
    dest.write_text(body)
master=ROOT/'RESEARCH_SA22_paper.tex'
m=master.read_text().replace('GPT-6 Astra\\OpenAI','GPT-6 Astra\\\\OpenAI')
m=m.replace('\\IfFileExists{sections/part_a14.tex}{\\input{sections/part_a14.tex}}{}',
            '\\input{sections/part_a1.tex}\n\\input{sections/part_a2.tex}')
m=m.replace('\\IfFileExists{sections/part_a3.tex}{\\input{sections/part_a3.tex}}{}',
            '\\input{sections/part_a3.tex}\n\\input{sections/part_a4.tex}')
master.write_text(m)
p.rename(ROOT/'notes'/'part_a14_initial_draft.tex')
print('Moved A.1, A.2, A.4 into separate numbered sections; fixed title line break.')
