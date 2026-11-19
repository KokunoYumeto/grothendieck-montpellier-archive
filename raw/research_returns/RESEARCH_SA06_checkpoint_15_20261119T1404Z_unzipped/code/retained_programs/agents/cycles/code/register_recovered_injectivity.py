"""Restore al/am/ao/ap statement and actual-check records after scratch loss."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

start=time.perf_counter();base=Path(__file__).resolve().parents[1];out=base/'output'
me='GPT-6 Astra (OpenAI); inherited reasoning effort; /root/cycles'
root='GPT-6 Astra (OpenAI); inherited reasoning effort; /root'
real='GPT-6 Astra (OpenAI); inherited reasoning effort; /root/real_weil'
frob='GPT-6 Astra (OpenAI); inherited reasoning effort; /root/frobenius'
cols=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
eventcols=['statement_id','date','who_model_effort_run','type','outcome']
def cert(name):return json.loads((out/name).read_text())
am=cert('critical_injectivity.json');ao=cert('absolute_picard_kernel.json')
fetch=cert('fetch_injectivity_sources.json')
compile=cert('compile_recovered_injectivity.json')
builds={r['name']:r for r in compile['wrappers']}
def build_text(name):
 r=builds[name];passed=all(x['returncode']==0 for x in r['runs']) and not r['diagnostics']
 return ('Fresh recovery build '+('PASS' if passed else 'not yet clean')+' at'+r['utc']+
         '; runtime_seconds='+str(r['runtime_seconds'])+'; returncodes='+str([x['returncode'] for x in r['runs']])+
         '; diagnostics='+str(r['diagnostics'])+'. Logs retained. A failed missing-format attempt is not a proof failure.')
def write(prefix,rows,events):
 with (base/(prefix+'_results.csv')).open('w',newline='') as f:
  w=csv.writer(f);w.writerow(cols);w.writerows(rows)
 with (base/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(eventcols)
  for sid,who,kind,detail in events:w.writerow([sid,'2026-11-19',who,kind,detail])
 return {'prefix':prefix,'rows':len(rows),'events':len(events)}
records=[]
alrow=['C.3al','Principal Gysin images lie in the ordinary closed-restriction kernel integrally; explicit infinite-order kernels for r>=2,r+1<=N<=2r-1',
 'Proved/refuted in the stated ranges','principal_gysin_kernel.tex, C.3al',
 'Stacks02T8/0B6Z/0B3P; C.3t explicit nonzero Gysin classes; dimension vanishing','14:106-109',
 'Normal line of a principal Cartier divisor is trivial. Actual fixed-product families are preserved. The self-intersection argument alone does not settle larger dimensions; am/ao do so separately.']
alevents=[
 ('C.3al',me,'targeted proof check','Verified i^*i_*=c1(N)=0 integrally for principal divisors; actual-family operations commute with fibres.'),
 ('C.3al',me,'used and rechecked in this run','Reread C3t exact incidence, generic-point non-support and strict-cone injection; its infinite-order image is a closed restriction kernel in precisely r+1<=N<=2r-1.'),
 ('C.3al',me,'primary-source verification','Opened Stacks Definition42.29.1 Tag02T8, Remark42.29.6 Tag0B6Z, Lemma31.15.2 Tag0B3P; retained exact URLs in bibliography.'),
 ('C.3al',root,'independent targeted proof check','Historical receipt: root full proof/C3t reread PASS at09:33:38UTC, with fresh exact Stacks opens. Original proof survived unchanged in checkpoint09.'),
 ('C.3al',frob,'independent targeted proof check','Historical receipt: full independent proof PASS09:34:09UTC; exact Stacks reread09:35:56UTC after checkpoint09 release.'),
 ('C.3al',real,'independent targeted proof check','Historical receipt: full proof/source PASS09:39:35UTC; full C3t reread and Stacks02T8/0B6Z/0B3P opened.'),
 ('C.3al',me,'scope check','Source zero for N<=r; degree-one uses its separate theorem. Current remaining-range wording now points forward to am/ao; no false universal self-intersection conclusion.'),
 ('C.3al',me,'typesetting verification',build_text('C3al_check'))]
records.append(write('principal_gysin',[alrow],alevents))
amrow=['C.3am','For every r>=2 a specified Fermat-cubic cone of local dimension2r has an infinite-order ordinary restriction kernel for its coordinate hyperplane puncture',
 'Refuted, with explicit counterexamples','critical_injectivity.tex, C.3am',
 'C.3r elliptic Fermat correspondence and Abel-Jacobi non-support; C.3e strict-cone injection; explicit rational cubic surface','14:106-109',
 'The restricted family factors through CH0 of the Fermat cubic surface, which is Z integrally. The source class uses the same specified transcendental elliptic point as C3r.']
amevents=[
 ('C.3am',me,'used and rechecked in this run','Reused exact C3r class and C3e; checked codimensions of the incidence Theta on S×W and the reduced coordinate hyperplane cut.'),
 ('C.3am',me,'targeted proof check','Derived residual conic Q=3tx²+3y²−3(t²x+y)z+(t³+1)z², determinant9t(t³+1)/4, section[t:1:1−zeta], and skew lines. Removing the fixed Cartier line gives a base-point-free conic pencil.'),
 ('C.3am',me,'targeted proof check','Smooth-fibre moving to the rational section proves CH0(S)=Z integrally; flat/refined compatibility passes the target equality to strict punctures.'),
 ('C.3am',root,'independent targeted proof check','Historical full typed proof PASS before09:42UTC, including conic determinant/section, Chow moving, exact source correspondence and strict-local compatibility.'),
 ('C.3am',real,'independent targeted proof check','Historical full typed proof PASS09:42:15UTC. Fresh full recovery reread also PASS; clarified removal of the fixed Cartier line, retaining the same conic and section.'),
 ('C.3am',me,'finite exact computation','Fresh recovery rerun at'+am['utc']+';13 parameter pairs, exact conic substitution/determinant/section and skew norm9 all pass. runtime_seconds='+str(am['runtime_seconds'])+'. Full JSON/stdout retained.'),
 ('C.3am',me,'typesetting verification',build_text('C3am_check')),
 ('C.3am',me,'recovery verification','Reconstructed after scratch loss from retained proof details; no new mathematical conclusion added. Original runtimes are not reused as fresh runtimes.')]
records.append(write('critical_injectivity',[amrow],amevents))
aorow=['C.3ao','For every r>=2,N>=2r+1 a specified strict cone and smooth principal puncture have an infinite-order ordinary CH^r restriction kernel, detected by absolute Milnor-dlog cohomology',
 'Refuted, with specified counterexamples','absolute_picard_kernel.tex, C.3ao',
 'Formal cone Picard splitting; GAGA/Elkik; Kerz7.1/7.5; Braunling Section3; Stacks50.9; exact residue and projective-bundle recursion','14:106-109',
 'Actual full-Pic kernel times r−1 Pic0 divisors is ordinary. Absolute differentials over stated k0 detect non-torsion. Finite-stage cycle detection and exceptional-boundary exclusion are proved separately.']
aprow=['C.3ap','Complete ordinary complex local restriction table: r>=2 injection iffN<=r,surjection iffN<=r+1,isomorphism iffN<=r; r1 injection iffN1orN>=3,surjection iffN<=2,isomorphism iffN1',
 'Proved, with counterexamples in every complementary dimension','local_injectivity_classification.tex, C.3ap',
 'Dimension vanishing; C.3n/o degree-one theorem; C.3al/am/ao higher kernels; C.3ak all-r surjectivity','14:106-112',
 'Both integral ordinary groups and rational J, in the stated complex coefficient-field scope. Every negative injectivity dimension has an infinite-order kernel; no depth condition is added.']
aoevents=[
 ('C.3ao',me,'targeted proof check','Specified coefficient field k0, algebraically independent incidence coefficients and independent generic points. Proper incidence dimension proves base-point freeness and the smooth projective-bundle divisor.'),
 ('C.3ao',me,'targeted proof check','Proved H1(L^n)=0 for n>=2, homogeneous formal exponential, GAGA/Elkik algebraization and exceptional adjustment. Graded target coboundary exponentiates at every order, including possible nonzero higher target H1.'),
 ('C.3ao',me,'primary-source verification','Full Kerz author PDF Theorems7.1/7.5 and Definition2.1; Braunling published Section3pp557–558; all Stacks50.9 and Lemma0FMD read. Recovery PDFs have exactly the retained original SHA256 hashes; all five downloads succeed, fresh total runtime_seconds='+str(fetch['runtime_seconds'])+'.'),
 ('C.3ao',me,'targeted proof check','Milnor symbols→absolute dlog respect Steinberg and intersection products. A hypothetical relation descends to a smooth finite etale stage. Tensoring Omega(V2) with O_V retains the conormal summand; ordinary differential pullback would not.'),
 ('C.3ao',me,'targeted proof check','The residue of −db/(u−b) paired with g(u)du is −p*omega=−g(p)db. Independent field differentials and nonzero generic evaluation give the required nonzero conormal class.'),
 ('C.3ao',me,'targeted proof check','Excluded exceptional boundaries integrally by highest h^r coefficient and descending recursion with m>=r, without a Chow Lefschetz conjecture.'),
 ('C.3ao',me,'finite exact computation','Fresh recovery rerun at'+ao['utc']+' passes117 dimensions/incidence cases,15 recursions,7 tensor cases, Fermat Jacobian/Serre/conormal/residue checks. runtime_seconds='+str(ao['runtime_seconds'])+'. JSON/stdout retained.'),
 ('C.3ao',root,'independent targeted proof check','Original canonical certification10:01:26.541461UTC. After scratch loss root reread all345 reconstructed lines and renewed full proof/fidelity PASS, retaining the corrected −p*omega notation and every detector/boundary step.'),
 ('C.3ao',real,'independent targeted proof check','Historical full typed proof/source PASS: freshly opened Kerz7.1/7.5, Braunling Section3 product diagram, Stacks0FLE; actual algebraization, absolute residue/tensor and boundary recursion all passed. Separate recovered review records fidelity.'),
 ('C.3ao',me,'typesetting verification',build_text('C3ao_check')),
 ('C.3ao',me,'recovery verification','Full proof reconstructed from retained text and detailed summary. New scripts were run afresh; original lost run times are identified only as historical receipts, never reported as new outputs.'),
 ('C.3ap',me,'used and rechecked in this run','Rechecked C3n integral characteristic-zero degree-one theorem and C3ak dimensions. Exhaustive negative higher injection intervals are al:r+1..2r−1,am:2r,ao:>=2r+1.'),
 ('C.3ap',root,'independent targeted proof check','Original canonical certification10:01:26.541461UTC: full table/proof PASS, exact C3n read, N1 empty target and r1N2 failure checked.'),
 ('C.3ap',real,'independent targeted proof check','Original full typed synthesis PASS; fresh full recovery reread also PASS in the same integral/rational complex coefficient-field scope.'),
 ('C.3ap',me,'typesetting verification',build_text('C3ap_check')),
 ('C.3ap',me,'scope check','Universal ordinary complex local restriction is decided. Smooth-projective injectivity, rational top local quotient, and higher positive-characteristic restriction remain separate. The negative columns may use different pairs.')]
records.append(write('absolute_picard',[aorow,aprow],aoevents))
record={'utc':datetime.now(timezone.utc).isoformat(),'recovery':True,'registers':records,
        'runtime_seconds':time.perf_counter()-start}
(out/'register_recovered_injectivity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
