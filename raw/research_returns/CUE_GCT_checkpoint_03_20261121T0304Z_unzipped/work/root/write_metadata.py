from pathlib import Path
from datetime import datetime, timezone
import csv
import json

BASE=Path(__file__).resolve().parents[2]
ROOT=BASE/'work/root'; OUT=BASE/'deliverables'
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'

def write(path,cols,rows):
    with path.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(cols);w.writerows(rows)

descriptions={
'G-01':'Burnside C2 fixed-point counterexample; universal GL character argument; representation versus augmentation distinction.',
'G-02':'i>=2 and specialization y=1; algebraic independence of terminal elementary symmetric polynomial.',
'G-03':'Parity binomial ranks; augmentation-ideal power; gamma-filtration and formal Chern-character vanishing.',
'G-04':'Homogeneous orbit map; torsion-free image; finite integer coefficient matrix and invertible-minor block elimination.',
'G-05':'Beauville plane-curve hypothesis, theta-complement existence, density, endomorphism substitution, highest-weight ideal restriction.',
'G-06':'Determinant-preserving H action, generic scalar stabilizer, dimension identity and exactly-four-row ideal deduction.',
'G-07':'Reduced divisor degree320112, determinant-character twist, projection image equality and shifted plethysm exact sequence.',
'G-08':'Unique monomial tree paths, cofactor orientation, universal homogenization and highest-weight ideal inclusion.',
'G-09':'Shared radix-chain paths, exact vertex count, padding chart, asymptotic bound and cited known exponent; complete written proof reread.'}
events=[]
for identifier,detail in descriptions.items():
    events.append([identifier,now,who,'targeted proof check','PASS whole-proof root reading: '+detail])
for identifier in [f'R-{i:02}' for i in range(1,10)]+[f'I-{i:02}' for i in range(1,13)]+[f'P-{i:02}' for i in range(1,9)]:
    events.append([identifier,now,who,'targeted proof check','PASS complete proof read by root during this run; recorded at this timestamp. Scope and remaining gate retained; no formal certification.'])
for identifier in ['G-01','G-03','G-09']:
    events.append([identifier,now,who,'computation or formal certificate','PASS finite exact computations in work/root/check_root.py and computation_results.json; finite checks, not a general formal proof.'])
events.append(['R-12',now,who,'computation or formal certificate','PASS independent Ryser subset verification of all2240 per4 and5600 per5 Jacobian evaluation entries and nonzero minors mod101; check_permanent_independent.py/results JSON. The complete new written R12 proof is awaiting root integration review.'])
events.append(['G-B01-scan019-study',now,who,'refuted, with the refined statement\'s id','The supplied study\'s asserted equivariant agreement at order2 is false; regular C2 set has fixed-point counts0 versus2. Refined statement G-01. Original ink not checked.'])
for identifier,detail in [
('G-B01','Read all five supplied transcriptions and the relevant SA17 study section. No original scans supplied; mathematical rather than paleographic audit.'),
('G-B02','Read SGA3 original ExposeI Propositions4.7.2–4.7.4 and electronic VI_B Proposition4.1; original EGA13.1.3 proof not reread.'),
('G-B03','Read electronic SGA6 V2.1/2.2/2.4,3.2/3.10,7.1/7.5 passages. VI3.2 locator corroborated but complete proof not read.'),
('G-B04','Read Serre1968 Theorem5 and sections3.7–3.8; scope is split reductive group-scheme K0.'),
('G-B05','Read relevant original FGA Expose221 Theorems3.1/3.2 and Proposition3.8.'),
('G-B06','Read EGAII2.4–2.5 electronic translation for associated graded-module sheaf. EGAIV3 13.1.3 corroborated in primary SGA3; large original PDF did not load.'),
('G-B07','Read Beauville2000 Proposition3.1(a), section3.2 and Corollary6.4 hypotheses in author PDF.'),
('G-B08','Read LLHV2024v3 Theorem2, Table2 and section4.1; visually checked reduced divisor degree320112 and half-cycle factor.'),
('G-B09','Read Boralevi etal2017 Theorem1.3 and construction/remarks in section4; known asymptotic exponent credited.'),
('G-B10','Read actual Alpoge exported declarations/predicates and four-page note as stipulated input; Masullo only suppliedindex, no numbered1.2 theorem available.')]:
    events.append([identifier,now,who,'used and rechecked in this run',detail])
write(ROOT/'check_events.tsv',['statement_id','date','who','type','outcome'],events)

questions=[]
for identifier,question,answer in [
('G-Q01','Does the second-operation identity hold equivariantly?','REFUTED by G-01; correct special-lambda formula uses psi2.'),
('G-Q02','Can the universal product formula omit its terminal exterior variable?','REFUTED by G-02; lambda^i is required.'),
('G-Q03','Can finite gamma/Chern data determine all representation multiplicities?','REFUTED by G-03; parity sums of line characters.'),
('G-Q04','Can orbit coefficient maps and specialization gates be stated integrally?','PROVED G-04; nonzero maximal minors specify the good localization.'),
('G-Q05','Can at-most-three-row multiplicity obstructions separate a padded form from the determinant?','REFUTED in the characteristic-zero same-ambient setting by G-05.'),
('G-Q06','Is the first four-row determinant-ideal sector nonempty?','PROVED G-06 for n>=4; no target nonvanishing inferred here.'),
('G-Q07','Can the four-row determinant4 coordinate multiplicities be calculated exactly?','PROVED G-07; shifted plethysm subtraction with D320112.'),
('G-Q08','Can universal low-variable determinantal constructions bound obstruction length?','PROVED G-08 and sharper G-09; exact finite bounds and O_k(m^((k−1)/2)) for k>=3.'),
('G-Q09','Can the original handwriting or missing Masullo theorem number be certified from these files?','UNRESOLVED SOURCE GATE: original scan images and the numbered Masullo1.2 statement are not supplied; no such certification is claimed.')]:
    questions.append([identifier,'Prompt Grothendieck-language requirement; paper '+identifier.replace('G-Q','G-'),question,answer])
write(ROOT/'questions.tsv',['id','source_and_locator','question','state'],questions)

notes=[
['133','006','25–26','terminal lambda^{i−1|i}','lambda^i in both factors','G-02: set the other factor to1; the top elementary symmetric polynomial is independent of earlier ones. SGA6V2.4.2 states the endpoint.','Certain mathematically; original ink not inspected','mathematical correction / unresolved visual reading'],
['133','019','10','sigma_{unsure t}(E) lambda_{−t}(E)=1','sigma_t(E) lambda_{−t}(E)=1','Linear terms cancel only with this sign convention; compare sigma_t(L)=(1−tL)^−1.','Certain mathematically; original ink not inspected','forced formal-series index'],
['133','019','13','lambda^{j|i}(E)_{1<=j<=i}','the indexed list lambda^j(E), 1<=j<=i','The displayed universal polynomial depends on the list of exterior powers, not i repeated copies of the terminal one.','High mathematical confidence; original ink not inspected','forced variable index'],
['133','019','20','(1 unsure{−|+} tL)^−1','(1−tL)^−1','Its coefficient of t must be +L.','Certain mathematically; original ink not inspected','forced sign'],
['133','019','45–53; SA17 scan19 Checked paragraph','2 lambda²(E)+E=E² treated as an equivariant identity','Valid after cardinality; in representation K0 replace E by psi²(E), and keep subset versus exterior operations distinct.','G-01 C2 free two-point set has0 fixed ordered pairs versus2 on claimed RHS; wedge² permutation module is sign, not the two-subset trivial module.','Certain mathematical refutation; not a claim that transcription misreads the ink','scope correction to mathematics/study'],
['133','028','10','xi unsure{=|in} cl_K(X)(E)','xi=cl_K(X)(E)','cl(E) is one K0 element; the stated construction takes its class as input. Membership has no defined set-valued right side here.','Very high mathematical confidence; original ink not inspected','forced relation symbol'],
['133','028','26–35','rho_i is the unit of its degree-i ring','rho_i is the trivial S_i representation, a degree-i generator for induction product, not the total graded-ring unit.','The displayed product has degree sum i alpha_i; the graded induction unit is degree0. The transcription itself is consistent when read degreewise.','Certain mathematical clarification; no proposed ink correction','scope clarification, not a misreading'],
['133','008','2','Laborde|Lazard','No new visual choice made; earlier study reports Lazard.','Neither spelling follows from the mathematics, and the original image is not attached.','Visual confidence not assessed in this run','unresolved paleography; prior report retained'],
['133','009','23–28','deleted assertion w composed alpha=1','Retain deletion; no new image emendation.','The supplied record already marks this as deleted. The earlier study reports a Stiefel–Whitney correction; it was not independently re-proved here.','No new paleographic or theorem certification','carried background only']]
write(OUT/'TRANSCRIPTION_NOTES.tsv',['cote','scan','line','our_reading','reading_required','reason','confidence','classification'],notes)
print(json.dumps({'recorded_utc':now,'root_events':len(events),'transcription_rows':len(notes)}))
