from pathlib import Path
import csv
base=Path(__file__).resolve().parents[1]
s=(base/'paper_B.tex').read_text()
a=(base/'additions_B_post02.tex').read_text()
b=a.index('\\subsubsection*{Statement B.2h')
a1=a[a.index('\\subsubsection*{Statement B.1e'):b]
a2=a[b:]
s=s.replace('\\subsection{A uniform curve and a uniform bound for first cohomology}',a1+'\n\\subsection{A uniform curve and a uniform bound for first cohomology}')
s=s.replace('\\subsection{B.3:',a2+'\n\\subsection{B.3:')
s=s.replace('setting.  Hence $P_W/P_T$',r'setting \cite[Theorems 5.14, 5.28 and 5.39]{MilneAG2022B}.  Hence $P_W/P_T$')
(base/'paper_B.tex').write_text(s)
f=base/'results_B.csv'
with f.open(newline='') as x: rows=list(csv.DictReader(x))
for id,stmt,status,deps,notes in [('B.1e','Pic^tau birational invariance with geometrically normal source and regular target over arbitrary characteristic-p fields','Proved under stated hypotheses','B.1b; Raynaud1970 Proposition6.2.1; finite subgroup detection over k','Geometric integrality imposed for the statement; finite separable rational-point extension is justified.'),('B.2h','Full Pic^tau stabilization over every perfect ground field','Proved','B.2g; Stacks0CCJ finite Galois descent','Cofinal stable model is constructed by the normalized graph of finitely many conjugate geometric models.'),('B.2i','The marked proper geometrically normal model category is always filtered','Refuted','Explicit birational graph over F_p(a,b); imperfect_graph_certificate_B.py','Both models are smooth projective rational threefolds. This refutes filteredness, not Picard constancy for a nonfiltered category.')]:
 rows.append(dict(id=id,statement=stmt,status=status,where_proved='paper_B.tex Statement '+id,depends_on=deps,manuscript_pages='29/071-075',notes=notes))
with f.open('w',newline='') as x:
 w=csv.DictWriter(x,fieldnames=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writeheader();w.writerows(rows)
with (base/'CHECK_EVENTS_B.tsv').open('a') as x:
 for id,typ,out in [('B.1e','targeted proof check','Finite separable extension supplies a rational point while preserving normality/regularity; Raynaud Leray edge quotient and finite k-subgroup detection prove the arbitrary-field regular-target extension.'),('B.2h','targeted proof check','Geometric stabilized model descends to finite Galois extension of perfect field; normalized conjugate graph has effective descent by opened Stacks0CCJ. Marking, geometric normality and cofinality checked.'),('B.2i','refuted, with the refined statement\'s id','Two smooth rational threefold models have normalized graph regular over k but geometrically nonnormal at codimension one; every normal common refinement retains that local ring. This is only a filteredness counterexample.'),('B.2i','computation or formal certificate','imperfect_graph_certificate_B.py checks 24 symbolic assertions for p=2,3,5, all passed in0.050912s using SymPy1.14.0; proof of regularity/nonfilteredness is in paper.')]:
  x.write(id+'\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\t'+typ+'\t'+out+'\n')
print('Integrated B.1e, B.2h and B.2i with synchronized results/checks; imperfect constancy remains unresolved.')
