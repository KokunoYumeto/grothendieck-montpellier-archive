"""Generate the algebra subagent's mergeable results and check-event fragments."""
from pathlib import Path
import csv
import re

root=Path(__file__).resolve().parents[1]
descriptions={
 'SA23-B1-1':'Minimal Cohen factorization is exactly Deligne\'s complete-local factorization with degrees zero and one preserved',
 'SA23-B1-2':'Finite-module complexes over a Noetherian ring commute with ideal-adic reduction on homology as pro-objects',
 'SA23-B1-3':'Deligne pro-Tor comparison for finite A-module N and finite B-module M under a local Noetherian homomorphism',
 'SA23-B2-1':'Arbitrary lifts of a finite residue regular sequence to an Artinian local base give a free quotient',
 'SA23-B2-2':'Every algebraic field extension has a triangular polynomial presentation whose arbitrary Artinian lifts are flat',
 'SA23-B2-3':'Scope of the algebraic-extension construction and literature search; no priority claim',
 'SA23-C-1':'Literal vanishing in Koszul degree zero is false for a proper ideal',
 'SA23-C-2':'Koszul regularity implies quasi-regularity for arbitrary rings and arbitrary modules',
 'SA23-C-3':'Generator invariance, flat ascent, fpqc descent, and composition of Koszul-regular immersions',
 'SA23-C-4':'Split-conormal converse transitivity when both ambient ideals are Koszul regular',
 'SA23-C-5':'Local idealization gives a regular sequence (x,y) whose reverse is not regular and refutes the other unrestricted converse',
 'SA23-C-6':'Exact Noetherian local scope and the homology-finiteness replacement for Nakayama',
 'SA23-C-7':'Deligne Sym-Tor characterization of regular ideals over a Noetherian ring',
 'SA23-C-8':'Ext vanishing below generator number implies module Koszul regularity without finiteness; ordinary regularity in the Noetherian local finite case',
 'SA23-D-1':'Finite solvability of affine linear equations in Artinian modules implies simultaneous solvability',
 'SA23-D-2':'Closed quotients of complete pro-Artinian rings remain complete pro-Artinian',
 'SA23-D-3':'EGA zero-IV 19.3.12 lifting theorem is true; square-zero compactness and closed powers repair its proof',
 'SA23-D-4':'Deligne nonlinear compactness example refutes the printed proof step but not EGA zero-IV 19.3.12',
 'SA23-G-1':'Exact three-way flatness classification under good graded conditions',
 'SA23-G-2':'Four-element dual-number algebra refutes A/K flat implies C/B flat under very good conditions',
 'SA23-G-3':'Section independence and Hilbert criterion with the explicit composite-augmentation hypothesis',
 'SA23-G-4':'Finite counterexamples to omitted augmentation and to Hilbert inequality from splitting alone',
}
pages={'B1':'23/060-063','B2':'23/062','C':'23/053-054;063-064',
       'D':'23/044-065','G':'23/096-098'}
rows=[]
events=[]
for path in sorted((root/'sections').glob('algebra_*.tex')):
    content=path.read_text()
    found=re.findall(r'\\begin\{(theorem|lemma|proposition|example|remark|corollary)\}\[([^]]+)\]\\label\{(SA23-[^}]+)\}',content)
    for environment,title,identifier in found:
        prefix=identifier.split('-')[1]
        status='Known' if title.startswith('Known') else 'Refuted' if title.startswith('Refuted') else 'Proved under stated hypotheses' if 'stated' in title or 'explicit hypothesis' in title else 'Proved'
        if identifier in {'SA23-C-1','SA23-C-5','SA23-D-4','SA23-G-2','SA23-G-4'}:
            status='Refuted'
        statement=descriptions.get(identifier,title)
        rows.append([identifier,statement,status,str(path.relative_to(root)),'',pages.get(prefix,''),title])
        kind='used and rechecked in this run' if identifier=='SA23-B1-1' else 'targeted proof check' if environment=='remark' else 'independent re-proof'
        events.append([identifier,'2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters',kind,statement,str(path.relative_to(root))])
events.extend([
 ['SA23-G-2','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','computation or formal certificate','Exhaustive dual-number ring laws (64 triples, 16 pairs); 16+32 balancing relations; nonzero one-dimensional source maps to zero','code/algebra_finite_checks.py;logs/algebra_finite_checks.txt'],
 ['SA23-G-4','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','computation or formal certificate','Both finite dual-number counterexamples verified over F2','code/algebra_finite_checks.py;logs/algebra_finite_checks.txt'],
 ['SA23-A-06','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','targeted proof check','Fresh-coordinate proof checked independently: split reduction injective; infinitely many coefficient differentials give new unit coordinates; lowest t-order cannot cancel','sections/root_A12.tex'],
 ['SA23-A-07','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','targeted proof check','Finite coefficient compositum obstruction to B=k A^p for infinite absolute p-rank checked','sections/root_A12.tex'],
 ['SA23-A-08','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','targeted proof check','Finite absolute p-basis presentation and canonical p-power lift through a square-zero ideal checked; separability gives required injection','sections/root_A12.tex'],
 ['SA23-D-3','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, root; communicated 00:37 UTC','targeted proof check','Root independently checked original pp85-86 and complete repair: C-linear Artinian affine equations, finite solvability, closed-power tower, topological comparison all valid','sections/algebra_D.tex'],
 ['K23-03 (23:53)','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','used and rechecked in this run','Nonpermutable local example and fpqc locality independently established; one additional hoped-for unrestricted converse is false, SA23-C-5','sections/algebra_C.tex'],
 ['K23-03 (23:60)','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','targeted proof check','Polynomial compactness counterexample remains correct; any inference that EGA zero-IV 19.3.12 is false is refuted by SA23-D-3','sections/algebra_D.tex'],
 ['K23-05 (23:96-97)','2026-11-20','GPT-6 Astra (OpenAI), inherited effort, algebra_letters','targeted proof check','Conditional graded statement re-proved with augmentation and surjectivity hypotheses made explicit; final manuscript reading awaits scan','sections/algebra_G.tex'],
])
for name,header,data,delimiter in [
 ('algebra_results.csv',['id','statement','status','where_proved','depends_on','manuscript_pages','notes'],rows,','),
 ('algebra_CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','where'],events,'\t')]:
    with (root/'notes'/name).open('w',newline='') as stream:
        writer=csv.writer(stream,delimiter=delimiter)
        writer.writerow(header)
        writer.writerows(data)
print('Numbered results',len(rows),'check events',len(events))
