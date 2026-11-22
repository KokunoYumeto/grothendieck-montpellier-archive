"""Record review18 at its actual due time, using only promoted current gates."""
from pathlib import Path
import datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-19T22:50:40+00:00')
assert datetime.datetime.now(datetime.timezone.utc)>=due
for rel in ['agents/monodromy/nonordinary_nine_theta_norm_transfer.tex',
            'agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex',
            'agents/reduction_descent/B_rational_high_line.tex']:
 assert '\\status{Candidate' not in (w/rel).read_text(),rel
movement=[
 'A.4: against review17 fixed-f0 three/five families, the uniform seven self-isogeny first enlarged the family; the complete arbitrary odd nine-theta transfer then proved every odd degree divisible by3 and EVERY even degree on each fixedf0 principal surface. The entire f0even main gate is closed, including the formerly open92. The full incoming-neighbour theorem extends allodd multiples of3 and even residues0,4mod6 (plus2) to every fixedf1 surface. These are exact geometric/arithmetic group statements with complete independent proofs; fixedf0odd11 and fixedf1odd5/even8 remain open.',
 'B.4: against review17 initial tame sectors ending at e=(p+2)(p-1), B71/B72 enlarged the sector and B73 now completely classifies the height-two index-two range:nu_min(p,e,2)=2 iff p<e<p³ forp>=5,mu_p inK,p notdividinge,perfectresidue, in the full filtered setting. At e=p-1 the index is1 and at permitted e>p³ it is at least3. All prime-to5 multiples of4 from8 through124 are now closed. This is a strict mathematical shrinkage, supported by actual finite-level quotient recovery and actual lower examples.'
]
def promoted(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
if promoted('agents/reduction_descent/B_iterated_high_quotient.tex'):
 movement.append('B.4 additionally has the complete actual-quotient induction upper boundnu_min<=n-1 whenevere<p^n,n>=3, and exactindex3 throughoutp³<e<p⁴ under the same prime-to-p height-two hypotheses. The remaining larger intervals have explicit unequal lower/upper bounds and are not called exact.')
if promoted('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex'):
 movement.append('A.4 additionally has the audited uniform larger-source cubic-component norm transfer, extending every proved odd sourcedegree e>=3 to all odd multiplesen through indecomposable incoming sources; the report records the exact resulting source families and remaining primes.')
assessment={'due_utc':due.isoformat(),'next_checkpoint_due_utc':'2026-11-19T23:05:40+00:00','movement':movement,'unresolved_refinements':[
 'GeneralA.3/A.4 remain open. The primitive mixed-polarization assertiondim imPsi_s>=2 remains unproved. The explicit unipotent quotient, Frobenius-killed class, symmetric-square cohomology and exact boundary kernel are auxiliary reductions only and are not counted as main-gate movement.',
 'Fixedf0odddegree11 and fixedf1odddegree5/even8 remain unproved. Individual principal-theta nodality for arbitrary kernels is neither asserted nor needed for the proved nine-theta transfer. Norm11 probes and finite candidate computations are not counted as theorem proofs.',
 'Higher-dimensionalB.3, absolute ramification divisible byp (including five-adice20), higher heights and exact largerB.4 intervals remain open. Any conditional induction or candidate not canonically promoted is excluded from the movement list.',
 'Source search, proof writing, numbering, compilation, visual QA and checkpoint production are not mathematical movement. This assessment is used by the actual time-gated review, not as a substitute for it.'
 ]}
p=w/'notes/review18_assessment.json';assert not p.exists();p.write_text(json.dumps(assessment,indent=2)+'\n')
subprocess.run([sys.executable,str(w/'code/update_current27.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review.py'),'18',str(p)],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_18.json').read_text())
assert r['no_movement_streak']==0 and r['movement']
text=('\n### Actual hourly review18\n\n'
 f"Actual review18 was recorded at{r['actual_utc']} against review17 at{r['baseline_actual_utc']}. "
 'The fixed-f0 even-degree gate is closed, the fixed-f1 degree families are strictly larger, '
 'and the prime-to-p height-two index-two interval is completely classified. Any further '
 'promoted extension is explicitly enumerated in the immutable actual review record. '
 'The no-movement streak is zero; disposition:Continue. Auxiliary A3 kernel calculations, '
 'unproved candidates, searches and packaging are not counted as movement. '
 'The next actual review19 and checkpoint28 are both due23:50:40UTC; checkpoint27 is due23:05:40UTC.\n')
for rel in ['notes/checkpoint27_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(text)
print(text)
