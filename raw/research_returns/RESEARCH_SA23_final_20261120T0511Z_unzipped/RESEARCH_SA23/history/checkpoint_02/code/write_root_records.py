"""Persist the root agent's explicitly reviewed Part A records and input check."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parents[1]
data=[
('01','Formal smoothness implies projective differentials, and retracts of formally smooth algebras are formally smooth','Proved','root_A12','', '22/022–025','The square-zero derivation lifting argument and the retract comparison are written in full.'),
('02','A separated local ring cannot have a projective module with a nonzero infinitely t-divisible element','Proved','root_A12','','22/023','Embed a projective module into a free module and use coordinatewise t-adic separation.'),
('03','The formal exponential exp(t) is transcendental over K(t) in characteristic zero','Proved','root_A12','','22/023','A minimal monic polynomial and its derivative force a nonzero rational function a to satisfy a prime equals d times a, which its pole order forbids.'),
('04','For characteristic-zero k contained in K and n positive, K[[t1,...,tn]] is never discretely formally smooth over k; its differentials are not projective','Proved','root_A12','SA23-A-01;SA23-A-02;SA23-A-03','22/023','No finite-dimensionality assumption on Omega K/k is needed. The nonzero infinitely divisible differential is d(exp(t1))−exp(t1)dt1.'),
('05','The positive-dimensional manuscript reading is proved; a reading including dimension zero is false','Refuted','root_A12','SA23-A-04','22/023','Dimension zero is a separable characteristic-zero field extension and is formally smooth. The original scan was visually inspected; no priority claim.'),
('06','Infinite-dimensional coefficient differentials obstruct discrete formal smoothness of a positive-dimensional power series ring','Proved','root_A12','SA23-A-01','22/024–025','Fresh free-module coordinates and coefficientwise derivations prove the obstruction; independent agent audit passed.'),
('07','Infinite absolute p-rank still obstructs formal smoothness when the relative differential dimension is finite','Proved','root_A12','SA23-A-02','22/022','An infinite p-independent coefficient series has nonzero infinitely divisible differential; finite coefficient-compositum argument checked.'),
('08','In characteristic p and positive dimension, discrete formal smoothness holds exactly when K/k is separable and K has finite absolute p-rank','Proved','root_A12','SA23-A-01;SA23-A-06;SA23-A-07','22/022','Both necessities and a finite p-monomial presentation with canonical p-power lifts are proved. Independent algebra audit passed.'),
('09','A finite relative p-basis alone does not suffice over an arbitrary imperfect base','Refuted','root_A12','SA23-A-07;SA23-A-08','22/022','Take k=K=Fp(s1,s2,...); the relative p-basis is empty but absolute p-rank is infinite. Under a perfect base the finite relative criterion is valid.'),
('10','An explicit one-dimensional noetherian domain has infinitely many cuspidal maximal local rings and only its generic point regular','Proved','root_A4','','22/020–021','Finite-character localization of infinitely many cusps. Fresh-variable ideal argument proves the exact spectrum and noetherianity.'),
('11','The formally smooth fibre locus of a flat map of noetherian rings need not be open','Refuted','root_A4','SA23-A-10','22/020','Fp to the infinite-cusp ring is flat; the locus is its nonopen generic point. Finite-presentation repair is SA23-A-13.'),
('12','The flat locus of a homomorphism between noetherian rings need not be open','Refuted','root_A4','SA23-A-10','22/021','Frobenius on the same ring is flat only generically; an explicit cusp syzygy proves failure at every maximal ideal, including p=2.'),
('13','Finite presentation restores openness of the flat locus and of the formally smooth fibre locus for a flat morphism','Known','root_A4','','22/020–021','Opened Stacks Theorem37.15.1, Lemma10.137.16 and Lemma33.12.6; source hypotheses and pointwise fibre comparison verified.'),
('14','For a noetherian adically formally smooth map, the cotangent complex on every adic quotient is a projective module in degree zero','Proved','root_A3','','22/013–014','Projectivity follows by continuous derivation lifting; completed local regularity and residue-field detection eliminate higher cotangent homology.'),
('15','Cotangent Ext groups of positive degree vanish for finite complete coefficients over a noetherian adically formally smooth algebra','Proved','root_A3','SA23-A-14','22/014','Derived inverse limit of Hom from projective quotient differentials; transition maps are surjective.'),
('16','Every noetherian adically complete formally smooth algebra lifts over a square-zero thickening, uniquely up to reduction-preserving isomorphism, with both forms of formal projectivity preserved','Proved','root_A3','SA23-A-14;SA23-A-15;SA23-A-18;SA23-A-19','22/013–014','AQ obstruction and ambiguity groups vanish; flatness, noetherianity, completeness and formal smoothness of the lift proved. Automorphisms are the stated derivations. Independent full audit passed.'),
('17','Opened complete-local and pseudo-finite-type lifting results are special cases and do not by themselves cover the general adic question','Known','root_A3','','22/014','EGA0IV19.7.2 and19.7.3; Perez Rodriguez2008 Definition1.3 and Corollary4.3. Exact hypotheses compared.'),
('18','Topological formal projectivity lifts through a noetherian square-zero flat deformation','Proved','root_A3','','22/013–015','Continuous Hom represented by a filtered colimit of Ext; low-degree change of rings and Artin–Rees make the Tor obstruction pro-zero.'),
('19','Strict formal projectivity with a basis of projective quotients also lifts through that deformation','Proved','root_A3','','22/013–015','Split quotient tower, arbitrary-rank idempotent lifting, complete product reconstruction, nilpotent Nakayama and explicit inverse continuity. Initial V0=B0 fixes tail indexing.'),
]
headers=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
rows=[]
for sid,statement,status,section,depends,pages,notes in data:
    rows.append(dict(zip(headers,[f'SA23-A-{sid}',statement,status,f'sections/{section}.tex',depends,pages,notes])))
with (root/'notes'/'root_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=headers);writer.writeheader();writer.writerows(rows)
eh=['statement_id','date','who','type','outcome','where']
events=[dict(zip(eh,['RUN-INPUTS','2026-11-20','GPT-6 Astra (OpenAI), ChatGPT Pro mode, root','computation or formal certificate','Original ZIP extracted once; 42 files, 1678214 bytes; input SHA256 recorded','code/00_unpack.py;logs/00_unpack.txt']))]
for row in rows:
    typ='used and rechecked in this run' if row['status']=='Known' else 'targeted proof check'
    events.append(dict(zip(eh,[row['id'],'2026-11-20','GPT-6 Astra (OpenAI), ChatGPT Pro mode, root',typ,row['notes'],row['where_proved']])))
events.append(dict(zip(eh,['RUN-CHECK-EVENT-ERRATUM','2026-11-20','GPT-6 Astra (OpenAI), ChatGPT Pro mode, root','targeted proof check','Checkpoint01 auto-labelled all Part A records independent re-proof, including source remarks and Known results. This was too broad. Current records distinguish targeted proof checks from used-and-rechecked sources; independent agent audits remain separately attributed. The immutable checkpoint is retained.','code/aggregate_registries.py;notes/root_CHECK_EVENTS.tsv'])))
for sid,outcome in [
    ('SA23-17','Original Definition4.7 noetherian adic scope checked on scan13; square-zero lift proved in SA23-A-16, preserving both explicit projectivity conditions'),
    ('SA23-18','Both general openness questions refuted by SA23-A-11 and SA23-A-12; finite-presentation repair SA23-A-13'),
    ('SA23-19','Infinite coefficient-differential obstruction rechecked; characteristic-zero presumption settled SA23-A-04; characteristic-p reading refined by SA23-A-08 and SA23-A-09')]:
    events.append(dict(zip(eh,[sid,'2026-11-20','GPT-6 Astra (OpenAI), ChatGPT Pro mode, root','used and rechecked in this run',outcome,'sections/root_A12.tex;sections/root_A3.tex;sections/root_A4.tex'])))
with (root/'notes'/'root_CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=eh,delimiter='\t');writer.writeheader();writer.writerows(events)
result={'root_statements':len(rows),'root_events':len(events)}
(root/'logs'/'root_records.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
