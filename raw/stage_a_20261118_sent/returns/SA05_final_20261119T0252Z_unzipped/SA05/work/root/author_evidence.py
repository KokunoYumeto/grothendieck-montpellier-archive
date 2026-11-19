#!/usr/bin/env python3
"""Serialize the actual search/check ledger; this program makes no research judgments."""
import csv,json
from pathlib import Path
from author_literature import refs
P=Path(__file__).resolve().parent
claims=json.loads((P/'claims.json').read_text());items=json.loads((P/'items.json').read_text())
RR={r['key']:r for r in refs}
families={
 'PURE':('Pure categories, equivalence relations, level and coniveau',
  'Jannsen numerical equivalence semisimplicity; Grothendieck standard conjectures; Bloch Ogus coniveau; motivic category level base extension',
  'R001,R008,R010,R013,R014,R015,R018,R019,R020',
  'Jannsen Theorem1 and Bloch–Ogus statements opened; own1969 work checked by cote11b; later abelian2026 scope read. Numerical semisimplicity is separated from faithful realizations and geometric support assertions.'),
 'TAN':('Tensor reconstruction, neutralization and descent',
  'Deligne Milne Tannakian2.11 2.20 2.23 3.2 6.22; Deligne categories tannakiennes dimension criterion; Ziegler filtered fibre splitting; Kahn Galois descent motivic theories',
  'R001,R002,R003,R005,R006,R007,R009,R013,R015,R023',
  'Primary exact theorems read, including corrected DM6.22. Deligne criterion is7.1, not the earlier search’s8.17. Ziegler4.13–4.14 is fpqc-local. Kahn’s checked version has5.10 and§10, not old-note numbering.'),
 'FROB':('Frobenius, effectivity, Tate and Lie data',
  'Milne motives finite fields effectivity Weil numbers; MathOverflow effective motive Frobenius integral; Tate semisimple conjecture current2026; Galois Lie algebra motivic group dimension filtration',
  'R008,R011,R013,R016,R017,R018,R019,R020,R021',
  'MO used as a lead, with conclusions based on primary Milne/Tate/current papers. Milne1994 exact conditional effectivity statement read. No theorem matching the naive pi1 filtration found in this bounded search; not a proof of historical absence.'),
 'SIX':('General bases, six operations, purity and continuity',
  'Cisinski Deglise triangulated categories mixed motives2.4.50 14.4.1 constructibility continuity; Nori Ayoub motives general base heart; absolute purity regular immersion',
  'R002,R004,R005,R009,R015,R018,R023',
  'CD2.4.50,14.4.1 and introductory scope theorems read from the primary PDF. Triangulated results are not silently promoted to an abelian heart; complete-formalism base hypotheses are retained.'),
 'WEIGHT':('Weight bounds and coefficient counterexamples',
  'Deligne WeilII3.3.5 lisse lower bound; Legendre trace formula Stacks03VA; smooth proper weights; ordinary cohomology lisse weight upper bound; mixed Hodge local fibres',
  'R007,R009,R015,R016,R017,R018',
  'WeilII weight statements and Stacks exact all-extension trace formula opened. Root duality and SNC proofs checked independently by cote12c. Constant coefficients and arbitrary lisse coefficients are not conflated.'),
 'POS':('Hodge and motivic polarizations',
  'Deligne Milne polarization4.10 4.11 graded5.12; Hodge tensors Mumford Tate; Hodge standard conjecture abelian varieties2026',
  'R001,R006,R007,R009,R018,R019,R020,R023',
  'DM polarization and graded-form definitions read. New CM and abelian consequences distinguished from arbitrary complex varieties and arbitrary complex abelian Hodge conjecture. The2026 full proofs are not independently audited.'),
 'BIR':('Scissors, birational motives and geometric reconstruction',
  'Howe curves isomorphic unpolarized Jacobians; Enriques motive unirational; Larsen Lunts stable birational; Kahn Sujatha birational motives; Gillet Soule descent motives; relative L functions weights birational',
  'R008,R010,R011,R015,R016,R017,R018,R019,R020,R021,R023',
  'Exact primary statements opened. The initial arXiv1304.6059 hit was Bondarko–Sosnilo and not used as Kahn–Sujatha; corrected to0902.4902. Howe parameter conditions and Enriques coefficient/equivalence scope checked. No exact draft-relative-L theorem found.'),
 'ENDO':('Endomorphism K0, determinant and lambda conventions',
  'Almkvist Grothendieck ring category endomorphisms1974; Weibel K-book rational Witt7.4.3; finite projective endomorphism category lambda symmetric series',
  'R012,R013,R015,R016,R017,R023',
  'Weibel II Application7.4.3 exact statement read. Backward original Almkvist DOI failed; marked unverified, not treated as opened. Field kernel, lambda sign and characteristic-p ghost examples independently proved/computed.'),
 'ABS':('Absolute, Weil-étale and arithmetic cohomology',
  'Geisser Weil etale rational splitting7.1; arithmetic duality finite field invariants coinvariants; motivic Ext Yoneda effaceability Ind motives; Cisinski Deglise heart',
  'R002,R012,R015,R017,R018,R023',
  'Geisser1.1–1.3 and7.1 read with conjectural inputs. Milne duality and CD formalism checked in their scopes. These are not identified wholesale with the manuscript’s simultaneous axioms.'),
 'ARITH':('Abelian schemes, Kummer, Sha, Brauer and duality',
  'Milne arithmetic dualityII2.1 II5.1; Weil Chatelet local fields1970 addendum1972; Kato Trihan BSD positive characteristic; Brauer Tate Shafarevich comparison correction; abelian scheme rational section regular base extension',
  'R011,R012,R015,R017,R018,R020,R021,R022,R023,R024',
  'Local1972 addendum, Kato–Trihan exact conditional theorem, Milne correction notice, ADT residue and abelian-scheme statements, Robert2.3.16 and SGA7IX2.2.9 read. General Sha finiteness not inferred from them. Recent BSD search hits not opened are not used.'),
 'REUSED':('Reused EGA algebra fragment',
  'EGAIV3 11.9.3 11.9.6 11.9.7 11.9.10 generic localization free module; schematic dominance base change',
  'cote11a primary EGA search ledger and source comparison',
  'All three attached variants compared; cote11a opened EGAIV3. SA05-C95 is merged into the precisely referenced SA05-C1061 in the consolidated data. No unrelated CD theorem is used as evidence.'),
 'HISTORY':('Documentary dates, titles and the weight-level introduction',
  'Grothendieck weights niveaux1964 introduction Montpellier motives; Numdam Grothendieck Lefschetz standard conjectures publication; author bibliographies',
  'R008,R013,R014,R018,R019',
  'The attached B12-01 introduction itself supports a retrospective1964 attribution. No exact published version was identified; it is not classified as own later published work, nor used to date every leaf.'),
 'MODERN':('Earlier-run modern comparisons and period boundaries',
  'Choudhury Gallauer Nori Ayoub Galois groups9.1; Ayoub anabelian presentation motivic Galois group2026; Huber Galois theory periods5.14',
  'R001,R002,R003,R004,R005,R006,R007,R009,R025,R026',
  'Primary statements and author bibliography opened. PID coefficients retained for CG; Ayoub enriched-functor theorem kept separate from derived triviality and bare profinite groups; Huber distinguishes the period conjecture from the formal torsor theorem.')
}
batch_descriptions={
 1:'Tannakian and Nori/Ayoub primary sources; supersingular obstruction leads.',
 2:'Ayoub current-year and Kahn descent; CD and Huber primary leads.',
 3:'DM theorem locators and CG9.1; further supersingular lead.',
 4:'Ayoub PDF/bibliography, Huber; CD HTML endpoint failed.',
 5:'Ayoub11–13, Huber5.10–5.15, DM6.22/2.23; CD PDF.',
 6:'Deligne dimension criterion searched initially under wrong8.17; Ziegler and Serre leads.',
 7:'Deligne primary mirror; Ayoub author bibliography; Ziegler arXiv and Weil sources.',
 8:'zbMATH-domain standard-conjecture search; MathOverflow effectivity/Enriques leads; Numdam weights/niveaux.',
 9:'Deligne corrected7.1, Ziegler4.13, CD14.4.1; Ayoub wording/date metadata search.',
 10:'Howe, Dolgachev, Larsen–Lunts and Goren–Lauter primary PDFs.',
 11:'Milne AV, Tate1966, Faltings1983; exact surface and stable-birational scopes.',
 12:'Milne ADT and local duality1970/1972; Geisser; Kato–Trihan and Almkvist leads.',
 13:'Grothendieck1969 PDF initially without OCR; Jannsen, Hua, Kahn; Deligne1968, Weibel and Bloch–Ogus.',
 14:'Grothendieck screenshot response without actual pixels was not counted as viewed; Deligne/Bloch–Ogus PDFs; Weibel and zbMATH metadata.',
 15:'Weibel, Kato–Trihan full text, Milne correction page, zbMATH403; mistaken KS arXiv hit; WeilII exact statements.',
 16:'Backward Kahn–Sujatha, Gillet–Soulé, finite-field motives, Almkvist; corrected Weibel7.4.3; Kato/Weil exact locators.',
 17:'Correct KS0902.4902, GS9507013, Milne1994; Almkvist DOI failure; targeted theorem finds.',
 18:'Current2026 Tate/standard/Sha and relative-L searches; Tate and CD exact statements; new abelian-result leads.',
 19:'Milne current bibliography/report, Cadoret–Hui–Tamagawa and Balkan–Schreieder primary sources; CM result search.',
 20:'Initial regular-section extension search weak results; Howe metadata, recent BSD leads; CM primary mirror opened.',
 21:'Stronger primary regular-base extension search; Howe author bibliography and arXiv history; bounded BSD follow-up.',
 22:'Robert abelian-variety notes and SGA7IX translation opened.',
 23:'Exact regular-section locators plus local primary reads of DM polarization, CD scope, GS and KS.',
 24:'Full Milne1982 author correction notice read, including indices, p-primary refinements and conditional equivalence.',
 25:'Ayoub primary PDF reopened; direct Remark13 string find failed because of extraction boundary.',
 26:'Ayoub Theorem11 and Remarks12–13 read in full around lines564–596; fixed-object six-functor construction distinguished from the expected constructible equivalence.'}

def write(name,rows,fields):
 with (P/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
rows=[]
for x in claims:
 fid=x['search_ids'][0];f=families[fid.removeprefix('ROOT-')]
 rr=[RR[k] for k in x['refs'] if k in RR]
 if x['id']=='SA05-C95':rr=[]
 rows.append(dict(search_id='SEARCH-'+x['id'],family_id=fid,date='2026-11-19',claim_id=x['id'],family=f[0],
  queries_normalized=f[1],venues='Primary author repositories; arXiv; Numdam; EGA/SGA and Grothendieck works; author bibliographies; MathOverflow leads; bounded zbMATH-domain lookup and direct403 failure',
  raw_batches=f[2],outcome=f[3]+' Claim-specific conclusion: '+x['fate'],
  opened_refs=';'.join(r['key'] for r in rr if r['note']=='verified'),opened_urls=';'.join(r['url'] for r in rr if r['note']=='verified'),
  verification_extent=' | '.join(r['key']+': '+r['locator']+' — '+r['verification'] for r in rr),
  limits='Queries are normalized recorded terms, not a claim to reproduce every exact keystroke. A family search can serve several explicitly mapped claims. No negative search proves absence; statement reading is not an independent proof.'))
write('search_log.tsv',rows,list(rows[0]))
write('search_batches.tsv',[{'batch':f'R{n:03d}','date':'2026-11-19','description':d,'raw_workspace_file':f'searches/R{n:03d}.json'} for n,d in batch_descriptions.items()],['batch','date','description','raw_workspace_file'])
write('reference_ledger.tsv',refs,list(refs[0]))

def esc(t):return str(t).replace('\\',r'\textbackslash{}').replace('{',r'\{').replace('}',r'\}')
bib=[]
for r in refs:
 fields={k:r[k] for k in ['author','title','year','url','note']}
 fields['howpublished']=r['publication'];fields['annote']=r['locator']+'; '+r['verification']+'; first circulation: '+r['first_circulation']
 bib.append('@misc{'+r['key']+',\n'+',\n'.join('  '+k+' = {'+esc(v)+'}' for k,v in fields.items())+'\n}')
(P/'references.bib').write_text('\n\n'.join(bib)+'\n')

events=[]
who='GPT-6 Astra Pro; active effort inherited from session (not separately exposed); SA05/root'
def event(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for x in items:
 event(x['id'],'carried as background without fault found','Source/provenance comparison only, not a mathematical proof. Item check: '+x['check']+'. '+x['check_reason'])
for x in claims:
 event(x['id'],'used and rechecked in this run','Read the manuscript passage and compared the exact quantifiers/hypotheses with the mapped opened sources. This event is a text and statement comparison, not a full proof audit. '+x['fate'])
 if x.get('refined_statement'):
  event(x['id'],'refuted, with the refined statement\'s id','Literal statement refuted under the interpretation and hypotheses specified in root_checks.md and the claim. Refined statement: '+x['refined_statement']+'. '+x['computation'])
independent={
 6:'§1 finite simple-constituent decomposition',13:'§1 Rep of a finite group separates End(1) from group connectedness',
 18:'§1 quaternion division algebra cannot embed in M2(Q)',28:'§1 central cocharacter versus nontrivial sl2 commutator',
 38:'§1 faithful exact functor detects already constructed kernels and cokernels',39:'§1 tensor-unit consistency',
 46:'§1 trace/duality and exterior powers',49:'§2 integral Tate parity',53:'§2 finite-length K0 simple basis',54:'§2 Tate shift on simple basis',
 55:'§2 degree and Laurent consistency',56:'§2 primitive-zero boundary',57:'§2 Tate strings do not specify multiplication',
 65:'§3 nondominant section-retraction contradiction',68:'§3 Howe hypotheses plus curve factorization and Riemann–Hurwitz',
 69:'§3 Enriques rational homological Tate decomposition and nonunirationality',70:'§3 nonruledness of the author’s supersingular product; not ring-map injectivity',
 74:'§4 P1 weight contradiction',75:'§4 exact all-extension Legendre trace and duality',76:'§4 twisted Legendre arithmetic invariant',
 80:'§4 Kronecker bounded-polynomial proof',81:'§4 infinite unipotent counterexample',83:'§4 double-centralizer scope',
 85:'§4 analytic Lie invariants equal invariants under an open subgroup',86:'§4 SL2/GL2 associative envelope',87:'§4 Frobenius multiplicative-independence dimension example',
 90:'§5 direct limit of degree-multiplication maps on Q',93:'§5 invariant/coinvariant natural map and Jordan obstruction',
 98:'§5 Kummer exact-sequence consequence with explicit limit hypotheses',101:'§5 discrete-lattice quotient',103:'§5 finite torsion lost by rationalization',
 104:'§5 constant-Jacobian rational degree-two term',105:'§5 the same term obstructs blanket vanishing',
 110:'§5 normalized local-invariant residue sequence',111:'§4 SNC incidence, Frobenius and Hochschild–Serre',
 115:'§6 orthogonal splitting conditional on nondegenerate restriction',116:'§6 End h1(E) Hodge types',117:'§6 twisted self-duality and Schur decomposition',
 118:'§6 finite length versus projectivity over Z',119:'§6 complete field-case determinant kernel',120:'§6 symmetric/exterior series',
 121:'§6 reciprocal factor exponents',122:'§6 formal logarithmic derivative',123:'§6 characteristic-p ghost counterexample',124:'§6 Jordan information loss',125:'§6 weight/Euler parity'}
for n,e in independent.items():event(f'SA05-C{n}','independent re-proof',e+'. Complete argument is in root_checks.md; published input theorems are explicitly cited and not reproved wholesale.')
computation_ids=[7,28,29,32,49,55,56,68,70,74,75,76,81,86,87,93,96,110,111,114,116,119,120,121,122,123,124,125,141,143,147,148,149,151,155,156,157,158,160,161,162,163,164]
for n in computation_ids:
 event(f'SA05-C{n}','computation or formal certificate','Executed programs/root_certificates.py; exact symbolic/matrix/finite examples and their limits are recorded in programs/outputs/root_certificates.json and root_checks.md. A finite sample is not promoted to a universal theorem or a Lean certificate.')
for r in refs:
 event(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',
  r['verification']+'. Exact checked extent: '+r['locator']+'. '+('The URL was opened; this does not certify the whole source proof.' if r['note']=='verified' else 'Original source not opened; no theorem is certified from it.'))
write('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
(P/'outputs').mkdir(exist_ok=True)
summary={'claims_with_search_rows':len(rows),'families':len(families),'references':len(refs),'check_events':len(events),'independent_argument_events':len(independent),'computation_events':len(computation_ids)}
(P/'outputs'/'evidence_build.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary))
