from pathlib import Path
import csv, json, time
start=time.perf_counter()
root=Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
paper=root/'sections/part_c.tex'
s=paper.read_text()
if '\\label{c:abelian-point-classification}' not in s:
    marker='\\begin{theorem}[The narrow K3 ring already detects finite-dimensionality]'
    s=s.replace(marker,(root/'part_c/c1_chow_extensions.tex').read_text()+'\n'+marker)
if '\\label{c:k3-stable-range}' not in s:
    marker='\\begin{example}[An explicit genus-three failure]'
    addition=(root/'part_c/c1_k3_stable_range.tex').read_text()
    addition+='\nThe current-source search also checked the official withdrawal notice of the October 2026 paper claiming the Hodge conjecture for all K3 products \\citep{c_k3withdrawal2026}. We exclude that withdrawn proof. Even a valid homological Kuga--Satake splitting alone would leave the Chow nilpotence step just identified.\n\n'
    s=s.replace(marker,addition+marker)
if '\\label{c:r7-audit}' not in s:
    marker='\\subsection{C.3:'
    at=s.index(marker)
    s=s[:at]+(root/'part_c/r7_audit.tex').read_text()+'\n'+s[at:]
paper.write_text(s)
bib=root/'part_c/references.bib'
if '@article{c_beauville1986,' not in bib.read_text():
    bib.write_text(bib.read_text()+'\n'+(root/'part_c/c1_new_sources.bib').read_text())
path=root/'part_c/results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows={r['id']:r for r in reader}
new=[
('c:abelian-point-classification','On an abelian variety the all-powers relations hold exactly for point classes, modulo torsion in the point','Proved over every algebraically closed field','Theorem','Fourier inversion; Poincare homogeneity; primitive logarithm; OSullivan6.2.6','11:51-57; C.1(c)','Includes positive characteristic and2; necessity already the T2 group-like relation.'),
('c:curve-chow-criterion','All-powers relations for a curve are equivalent to the one modified-diagonal vanishing','Proved over every algebraically closed field','Proposition','c:pair-ranks; theta^(g+1)=0; Jacobian autoduality; Fu-Laterveer-Vial3.1/3.5','11:51-57; C.1(c)','For g>=2 uniquely o=K/(2g-2); for g0,1 every rational degree-one class works.'),
('c:surface-chow-criterion','For a complex surface with b1=0 the all-powers criterion is M_o=0 plus Kimura finite-dimensionality','Proved equivalence','Proposition','Orthogonal matching presentation; Chow projectors; Kimura exterior dimension','11:51-57; C.1(c)','Does not assert finite-dimensionality; o necessarily H^2/deg(H^2).'),
('c:k3-stable-range','Unconditional narrow K3 tautological injectivity for k<=45 and min(d,k-d)<=22','Proved','Corollary','Beauville-Voisin local identities; orthogonal matching independence','11:51-57; C.1(c)','First unproved universal determinant occurs at k46,d23; codimension is2d.'),
('c:r7-audit','R7 signs, level splitting, rigidity, and effective internal-Hom counterexample rechecked','Used and rechecked; counterexample confirmed','Remark','Supplied reading2.1-2.3 and12:150-158; Tate category computation','12:150-158; R7','No homological realization faithfulness on Chow motives inferred from the conditional construction.'),
]
for ident,statement,status,kind,deps,pages,note in new:
    rows[ident]=dict(zip(fields,[ident,statement,status,'sections/part_c.tex, '+kind+' label '+ident,deps,pages,note]))
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows.values())
path=root/'part_c/CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); efields=reader.fieldnames; events=list(reader)
for ident,statement,status,kind,deps,pages,note in new:
    row=dict(zip(efields,[ident,'2026-11-19','GPT-6 Astra (OpenAI), /root/part_c','targeted proof check',status+': '+note]))
    if row not in events:events.append(row)
for ident,kind,note in [
('c:abelian-point-classification','independent re-proof','Root independently checked the Fourier-log eigenvalue argument; Part C checked the arbitrary-characteristic extension from Mukai2.2 and Poincare identities.'),
('c:k3-gate','targeted proof check','Current system1 searches included 2026 K3 finite-dimensionality, Kimura, Chow and revised AI repository; official Oct6 K3 Hodge withdrawal opened; no universal Chow vanishing obtained.'),
('R7','used and rechecked in this run','Read supplied reading2.1-2.3; effective Tate internal Hom is0 before inversion andQ(1) after; sign and rigidity requirements verified.')]:
    row=dict(zip(efields,[ident,'2026-11-19','GPT-6 Astra (OpenAI), /root/part_c',kind,note]))
    if row not in events:events.append(row)
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=efields,delimiter='\t');w.writeheader();w.writerows(events)
report={'labels_added':[r[0] for r in new],'result_rows':len(rows),'events':len(events),'runtime_seconds':round(time.perf_counter()-start,6)}
(root/'code/part_c/integrate_c1_extensions_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
