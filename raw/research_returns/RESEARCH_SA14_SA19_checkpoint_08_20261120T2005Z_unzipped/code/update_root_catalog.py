"""Idempotently merge the root's checked statements and create a working report."""
from pathlib import Path
import csv, datetime
root=Path(__file__).resolve().parents[1]
path=root/'RESEARCH_SA14_SA19_results.csv'
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
with path.open(newline='') as f: rows=list(csv.DictReader(f))
by_id={r['id']:r for r in rows}
updates=[
('A1','Picard isomorphism for every smooth hyperplane in dimension at least four','Undecided','Part A, A1r and A4','A1r;A4','57:97','Reduced to the dimension-four case; finite multiplicative obstruction remains.'),
('A2','Injectivity and the least universal dimension','Undecided','Part A, A2b and A4b','A4b;A2b','57:97','Finite p-primary kernel; dimension two fails; dimension-three universal assertion not settled.'),
('A3','Very ample negative H1 nonvanishing and least dimension','Undecided','Part A, A3r and R3/A3t','A3r;R3','57:99-100','Existence reduces to smooth surfaces; least dimension is two if any example exists.'),
('A4','Exact finite multiplicative obstruction description of kernel and cokernel','Proved','Part A, Statement a:finite','SGA2 XII.3.4;Serre duality and vanishing','57:97','Uses the actual multiplicative tower; not just dimensions or a direct sum of additive layers.'),
('A4b','Finiteness and explicit p-power exponent for the restriction kernel and cokernel','Proved','Part A, Corollary a:pgroups','A4','57:97','Both groups for n>=4; kernel for n=3. Exponent p^e for p^e>=N+1.'),
('A4c','Picard restriction under the stated negative-cohomology vanishings','Known','Part A, Corollary a:vanishing','SGA2 XII.3.6','57:97','Hypotheses verified for smooth X when the stated vanishings hold; not supplied in A1.'),
('A3r','Any very ample H1-negative counterexample yields a smooth surface counterexample','Proved','Part A, Proposition a:surface','Serre duality;Serre vanishing;Bertini','57:100','Strict reduction of the existence gate; not an existence theorem.'),
('A1r','The universal dimension>=4 Picard isomorphism reduces to dimension four','Proved','Part A, Proposition a:fourfold','A4c;Serre duality;Bertini','57:97','Auxiliary high-degree cut preserves the original hyperplane embedding on the cut.'),
('A2b','A smooth Segre surface hyperplane has restriction kernel Z(1,-1)','Proved','Part A, Proposition a:segre','Pic(P1 x P1)','57:97','Valid in every characteristic; proves only lower bound three for a possible universal threshold.'),
('R3','Tangent of the Picard restriction kernel equals h H1(X,L^-1)','Proved','Part A, Proposition a:tangent','First-order line bundle deformation sequence','57:99-100','The equivalence K=0 iff tangent=0 requires K finite connected; generic connectedness audited separately.'),
('R4','Restriction kernel/cokernel are bounded finite p-groups in the dimensions stated','Proved','Part A, Corollary a:pgroups','A4','57:97','The phrase built from layers requires obstruction maps and extension data, not direct sums.'),
]
for values in updates:
    row=dict(zip(fields,values))
    if row['id'] in by_id: by_id[row['id']].update(row)
    else: rows.append(row);by_id[row['id']]=row
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
out=['INCOMPLETE','','| Item | Status | Statement / current gate |','|---|---|---|']
for r in rows:
    out.append('| '+r['id']+' | '+r['status']+' | '+(r['where_proved']+'; '+r['notes']).replace('|','\\|')+' |')
out += ['','## Authorship and scope','','AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. We have read supplied diplomatic transcriptions, not the manuscript scans. Statements from earlier AI readings are checked where used.','','## Working source audit','','The main Part A source checks are recorded in sections/A.tex and work/root/notes.md. Exact opened locators and version distinctions are in work/root/references.bib. Delegated Parts are preserved under work/bce, work/dgj, and work/fhi pending integration and independent review.','','## Computations and typesetting','','Source retrieval programs and output manifests are in code/. Mathematical finite checks are in the delegated code directories. LuaLaTeX and visual QA counts will be entered after the first integrated build.','','## Corrections established so far','','- SA14-H3 recalls the Bhatt–de Jong local theorem as an isomorphism up to p-power torsion. The opened Theorem 0.1 gives injectivity up to such torsion in characteristic p.','- Lauritzen–Rao has very ample nonvanishing in degree 3r−4, not degree one; its lower-degree groups vanish. It does not settle A3.','- The earlier generalized Raynaud paper is not used without Zheng’s corrections.','- R6 omitted hypotheses preceding the full Picard product in 57:286; the unrestricted product formula has a correspondence factor already when Gamma is trivial. The Pic-tau examples are being checked separately.','','## Still being investigated','','Main unresolved gates and failed approaches appear in Part A and PROGRESS_LEDGER.md. None is labelled a proof.']
(root/'RESEARCH_SA14_SA19_report.md').write_text('\n'.join(out)+'\n')
print(f'Merged {len(updates)} root entries; catalog has {len(rows)} rows.')
