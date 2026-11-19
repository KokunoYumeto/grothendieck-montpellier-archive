"""Events describe checks actually performed, never inferred proof completion."""
from pathlib import Path
import json,csv,datetime
P=Path(__file__).resolve().parents[1]
items=json.loads((P/'items.json').read_text());claims=json.loads((P/'claims.json').read_text());refs=json.loads((P/'references.json').read_text())
rows=[];who='GPT-6 Astra Pro; effort inherited/not exposed; run SA06-part2/cote14_late'
def add(ident,typ,outcome):rows.append(dict(statement_id=ident,date='2026-11-19',who=who,type=typ,outcome=outcome))
for x in items:
 add(x['id'],'used and rechecked in this run','Full assigned note and source passage read, including cancellations, margins and omnibus subcontent. Attribution verdict: '+x['check']+'. '+x['check_reason']+' No scan consulted and no reading changed.')
for x in claims:
 add(x['id'],'targeted proof check','Targeted statement/hypothesis and source-locator comparison, not an independent proof of each cited deep theorem. '+x['fate'])
 if x['status_on_pages']=='false as stated':
  add(x['id'],'refuted, with refined statement id','Refined statement retained under '+x['id']+'; the source transcription is unchanged. '+x['fate']+' General reasoning, where applicable, is in computation_notes.md.')
 if 'checks'in x['computation']:
  add(x['id'],'computation or formal certificate','Executed code/recompute.py; exact saved output audit/recompute_output.json; checks '+', '.join(x['computation']['checks'])+'. The general mathematical argument and finite-test limitations are written in computation_notes.md.')

independent={
200:'Graph nonadditivity via the elliptic degree-two component.',203:'Numerical quotient embeds in a finite integer intersection lattice.',209:'Cofinal covers and preserved fibre products identify the Čech complexes; apply the site acyclicity criterion.',
212:'Difference of square-zero lifts is a derivation; converse expansion.',215:'Polynomial-degree reduction over a field; antipode denominator argument.',217:'P¹_C as an R-scheme has χ=h0=2 for O but O is not ample.',
222:'Strictly nef threefold construction on P(O⊕A), including every curve and a nonample section.',223:'Continuity of divisor intersection polynomials along D+εH.',226:'Riemann–Roch with D²=0; the coefficient interpretation is conditional.',227:'Exact cubic expansion.',
236:'Split exact-sequence countermodel; not a geometric refutation without further hypotheses.',238:'Deduction of failure of CH0 Gysin surjectivity from the published Mumford theorem.',239:'Finite NS image versus published infinite-dimensional rational Griffiths group.',240:'K3 Pic0=0 versus nonzero CH0 degree-zero.',241:'Deduction using Mumford and Beauville–Voisin; their theorems remain background.',
242:'Codimension shift forced by proper pushforward; exact localization retained.',243:'Dimension and G_m-bundle localization of the punctured cone; primitive exponent checked.',
248:'Algebraic rectangle relation follows by a connected family; rational relation contradicted using Mumford.',249:'Conditional additivity/Albanese-inverse reasoning, not universal injectivity.',251:'Bounded locally free kernels after a common quotient; a second common twist may be needed.',252:'Leading Chern-character/Newton-identity factorial and sign; undefined K-equivalence retained.',
253:'G_m/μ2 over R distinguishes fppf quotient from quotient of point sets.',254:'Generic-fibre generation for a pencil with regular codimension2 base; not general j.',255:'Real Laurent-series field counterexample; C2 periodic cohomology gives all degrees.',259:'Norm/diagonal composite is [d], dominant by character lattices even inseparably.',
261:'Numerical invariance of the one-cycle-induced homomorphism via Poincaré divisor correspondences.',265:'Minimal denominator is the annihilator exponent of the finite kernel group scheme, not its order.',266:'Integral Tate-module cokernel is the ℓ-primary geometric kernel; prime-support criterion.',
270:'Exact equivalence of H1 inverse and universal0cycle; rational generic-section sufficiency; application of published/preprint counterexamples.',271:'Integral Künneth subtraction, full sign calculation and deduction from the exact integral Fourier/Hodge theorem and newer counterexample.',
272:'Kummer exact sequence under invertible N and divisible global units.',273:'Passing to Tate modules kills finite NS torsion; Pic0 and Alb variance kept.',
279:'Top wedge determines a rational subspace, not an integral image lattice.',280:'Distinct ℓ-adic lattices with the same determinant wedge.',281:'Complementary-degree exponent from trace duality.',282:'Cup-product sign under graded transposition, with conventions explicit.',283:'Algebraic equivalence of degree-zero0cycles on connected smooth projective varieties; not rational equivalence.'}
for n,reason in independent.items():add('C-SA06-'+str(n),'independent re-proof',reason+' Full argument in computation_notes.md; a derived consequence may use the named deep theorem as background.')
for ident,checks in {'SA06-254':['sl2_strings'],'SA06-255':['Tate_unit_test'],'SA06-256':['Tate_unit_test'],'SA06-257':['twist_naturality'],'SA06-262':['finite_error_vs_rational'],'SA06-265':['nodal_cubic_duality']}.items():
 add(ident,'computation or formal certificate','Earlier-run idea independently recalculated in code/recompute.py; outputs '+','.join(checks)+'. General argument in computation_notes.md; not attributed to the source page.')
for r in refs:
 v=r.get('verification','')
 shared='shared' in v.lower()or'cote14_early'in v or'root'in v.lower()
 typ='carried as background without fault found'if shared else'targeted proof check'
 add('REF:'+r['key'],typ,'Primary-source provenance: '+v+' Checked locators: '+' | '.join(r.get('locators',[]))+'. Limits: '+r.get('limitations','No claim of independently re-proving the full cited work.'))
add('ENDPOINTS:cote16,44,47,54','used and rechecked in this run','The exact selected source endpoints listed in contextual_endpoint_audit.md were read in full; reused printed leaves and unfinished steps distinguished. This is an endpoint audit, not an exhaustive new consolidation of those cotes.')
add('PROJECT_ENDPOINTS:RESULTS_STATE','carried as background without fault found','Complete retrieved RESULTS_STATE.md read. Endpoint labels/statuses/truncated excerpts checked; external project proofs and unchecked WG guesses are not endorsed. Parent separately checks full LM/FLAGGED/Hua sources.')
fields=['statement_id','date','who','type','outcome']
with(P/'CHECK_EVENTS.tsv').open('w',newline='')as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
with(P/'progress.log').open('a')as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tCHECK_EVENTS_SAVED\t{len(rows)} actual source, proof, computation and carried-background events.\n')
print({'check_events':len(rows)})
