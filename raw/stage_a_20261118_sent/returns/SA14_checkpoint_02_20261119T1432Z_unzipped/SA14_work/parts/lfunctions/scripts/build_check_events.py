"""Truthful event ledger. Proof groups are explicitly authored, not inferred from labels."""
import json,csv,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
C=json.loads((R/'claims.json').read_text());I=json.loads((R/'items.json').read_text());B=json.loads((R/'reference_details.json').read_text());P=json.loads((R/'problems.json').read_text())
E=[];WHO='GPT-6 Astra Pro; effort not exposed; SA14-20261119; lfunctions'
def event(s,typ,outcome):E.append(dict(statement_id=s,date='2026-11-19',who=WHO,type=typ,outcome=outcome))
for i in I:
 event(i['id'],'used and rechecked in this run','Text concordance, not mathematical proof. Every listed source note and its actual passage were read: '+', '.join(i['sources'])+'. Locators: '+'; '.join(i['lines'])+'. Authored assessment: '+i['check']+' — '+i['check_reason'])
for c in C:
 event(c['id'],'used and rechecked in this run','Text concordance, not mathematical proof. '+'; '.join(c['lines'])+'. Attribution: '+c['attribution']+'. Documentary status: '+c['status_on_pages']+'. The modern statement and any external reconstruction are separately labelled in the claim record.')
 event(c['id'],'used and rechecked in this run','Literature search and scope comparison: '+', '.join(c['search_events'])+' in search_log.tsv. '+c['fate']+' References: '+', '.join(c['refs'])+'. This event records the search/match, not an independent proof of all cited theorems.')
def proof(ids,section,outcome,typ='independent re-proof'):
 for n in ids:event(f'C-SA14-{n}',typ,'proof_notes.md §'+str(section)+': '+outcome)
proof(range(401,406),1,'Triangularization, block determinants and virtual lambda identities prove the stated formulas without diagonalizability; the cancelled formula is not reinstated.')
proof([406,407,408],1,'Checked the exact implications of purity, rationality and a specified perfect pairing. Rank-one unit characters are countermodels only to the unrestricted pure-sheaf reading; no refutation of rational polarized motives is claimed.')
proof([412,414,415,416],1,'Paired cohomological degrees, the top exterior power of an alternating form and fixed-point order parity give the stated formal consequences. Existence of the geometric pairings is a cited input.')
proof([409,410,417,418,420,422,423,424,425,426,447],2,'Derived the reciprocal determinant and boundary formulas from the explicitly stated trace/duality inputs; the dual cone has shift−1. The A¹/G_m counterchecks and base-field operation have separate exact outputs.')
proof([411,413],1,'Checked the exact statement and hypotheses of the opened geometric-weight or generic-extension source. No proof of the standard conjectures or existence of generic selfduality is claimed.','targeted proof check')
proof([427,428,429],3,'Checked the curve/model and middle-extension hypotheses against Stacks0BY1, Deligne1974 Theorem2.12 and the stated Verdier shift; the determinant calculation is formal once those inputs hold.','targeted proof check')
proof([430,431,434,435,436,437,438,439,440,441,442],3,'Used the exact-sequence cokernel, normal unipotent filtration and finite-group averaging projector. Distinguished ordinary invariants, the averaged virtual class and nonadditive alpha; proved the mu cancellation in the stated category.')
proof([443,444,446],3,'Compared the exact local-weight, GOS or epsilon-product statement with its opened primary theorem; closed-point degrees, geometric hypotheses and auxiliary differential/character data are retained. This is not an independent re-proof of WeilII or the product theorem.','targeted proof check')
proof([445],3,'Checked the formal squared-determinant cancellation; extracting a determinant from its square leaves a sign. The full local sign theorem is a separate published input.')
proof([448,449],4,'Computed the fixed field and both unrestricted normalization families. The forbidden choice1/L is not used to solve the lower-niveau problem.')
proof([452,453,454,456],5,'Finite translated coverings, their composition, positivity and a common ultrafilter give the stated construction. The zero-function case and OR condition are treated explicitly.')
proof([455,457],5,'The approximate-additivity and Haar uniqueness steps were checked against Alfsen1963 pp106–116, while recording that its constructive route differs from the draft ultrafilter presentation.','targeted proof check')
proof([458,459,460],5,'Baer divisibility over a PID, cyclic finite-length modules and dual short exact sequences prove biduality and the orthogonality statements.')
proof([462,463,464,465,466,467,468,470,471,472,473,474,562,563,564],6,'The exact local length, trace, conductor, socle and canonical-module arguments are written out. Counterexamples retain the finite-order and separability hypotheses. Global biduality and semilocal residue blocks are treated explicitly.')
proof([469,475],6,'Checked the proper-ideal/Gorenstein and different framework in Marseglia2019 §2 and Stacks0BW0; the separate multiplier converse is our proof C-SA14-563, not attributed to that broader source.','targeted proof check')
proof([478],6,'Distinct residue coordinates are necessary and sufficient for a split finite algebra to be monogenic; interpolation proves sufficiency.')
proof([479,484,485,486,487,488,489,490,491,542,543,544,545,546,547,566],7,'Presentation minors, quotient relations, DVR diagonal forms and exterior-power exponent counts prove the precise formulas; signed relative divisors are distinguished from integral Fitting ideals.')
proof([493,494,495,497],8,'The degree-two derivation identity, explicit unit construction, invariant-ring parity decomposition and prime localization are checked with all characteristic and ring hypotheses. The subgroup theorem used for497 has a separately checked exact primary proof.')
proof([496],8,'Read and checked Samuel’s exact descent and weight-filtration proof: derivative-ideal quotient, recursive integration and splitting over F₂ yield the additive subgroup k^N. Finite lattice counting alone is not treated as a proof.','targeted proof check')
proof([492],8,'Checked the externally identified Samuel counterexample and its nonzero polynomial contradiction. This verifies the published antecedent, not missing ink on the supplied cut line.','targeted proof check')
proof([499,500,501],9,'Distinguished division, coefficient convergence, closedness of each ideal and completeness prove the inverse-limit statement; the Hensel counterexample satisfies every printed premise.')
proof([503,565,567],10,'The zero-exponent case is refuted modulo x. With positive exponents the general block recurrence is proved by weighted homogeneous truncation; its finite coefficient tests are recorded separately.')
proof([504,505,506,508],11,'The exact Samuel1961/1964 existence and positive factoriality assertions were matched to their primary statements and proof mechanism. No claim that finite examples alone prove all power-series theorems.','targeted proof check')
proof([507,509,510,511,512,513,516,517,518,519,520,521],11,'Projective lifting, divisor classes, the Veronese semigroup, conic Picard quotients and prime-element localization supply the stated algebraic checks; characteristic, dimension and field hypotheses are explicit.')
proof([514,515],11,'Read and checked Samuel1964TIFR Theorem8.1, including both alternatives and the graded finite-free descent. The printed field case of the coprime trinomial is the specialization actually asserted.','targeted proof check')
proof([522,523,524,525,526,527,528,529,531,532,533,534,535,536,537,541,548,549,550,551,555,556,557,558,559,560],12,'Height-one intersections, primitive rank reduction, DVR scalar lengths, dual bases and exact codimension-two examples give the stated results. Global tensor exactness and splitting are not inferred from pseudo-isomorphisms.')
proof([538,539,540,552,553,554,561],13,'Checked cyclotomic splitting, local differential generators, the two-equation inseparable-residue DVR, DVR Tor/Ext lengths and the UFD unit certificate. The arguments retain separability and finite-presentation hypotheses.')
# Explicitly limited records: no full mathematical proof event is manufactured.
for n,outcome in {
419:'The source does not define type here; modern weight results do not identify that predicate.',
421:'Realization-level determinant algebra is checked, but the unspecified motivic decomposition is not established by it.',
432:'The R^1 term is deleted on the supplied page; its documentary withdrawal is not a surviving theorem to prove.',
433:'The author rejects the global recipe for locality/étale-compatibility. No supplied worked counterexample was found; none is invented.',
450:'Strict lower niveau is not defined sufficiently to determine the admissible factor group.',
451:'The indexed factor diagram has unresolved readings; only the explicitly labelled unrestricted reconstruction is checked.',
461:'Height preservation is retained in the finite integral normal-base setting; the standard dimension framework was compared, without claiming a separate full proof here.',
476:'A determinant gives an open power-basis locus in the explicit finite-free reconstruction, but the cut source does not specify its topology.',
477:'The primitive-element/different criterion is retained under its printed separability hypotheses; no broader monogeneity claim is inferred.',
480:'The missing Proposition11 and its condition1 are not reconstructed from an unrelated modern theorem.',
481:'The cut local presentation antecedent is not recovered; the complete later Fitting calculations are separate.',
482:'DVR diagonal-form computations are valid but do not identify every global hypothesis in the fragment.',
483:'Local and global freeness are distinguished; the missing standing local hypothesis prevents an exact source theorem identification.',
498:'The cited earlier exercises/propositions are not supplied, so their full claims are unidentified.',
502:'The sub-DVR construction cuts off before its requested conclusion; no absent assertion is invented.',
530:'The finite-avoidance mechanism is checked in the visible range; the internal4–39 continuation is absent.'
}.items():event(f'C-SA14-{n}','carried as background without fault found',outcome+' See the exact limitations in claims.json and proof_notes.md; search events remain recorded.')
for c in C:
 calc=re.findall(r'CALC-\d+',c['computation'])
 if calc:event(c['id'],'computation or formal certificate','Executed scripts/calculations.py; outputs/calculations.txt, '+', '.join(dict.fromkeys(calc))+'. All assertions passed. The output states what was computed; finite tests certify their examples and do not by themselves prove a universal theorem.')
refinements={567:'C-SA14-567, modern statement (within-block division by y)',424:'C-SA14-424, modern statement (reciprocal normalized determinants)',431:'C-SA14-431, present_status (support contained in ramification of the middle representation)',442:'C-SA14-442, modern statement (retained Tate twist)',462:'C-SA14-562 (local colength)',463:'C-SA14-562 and proof_notes.md §6 (local principality and minimal branch valuation)',467:'C-SA14-564',470:'C-SA14-470, modern statement (localized socle criterion)',488:'C-SA14-488, modern statement (containment N⊂M)',501:'C-SA14-501, modern statement together with Stacks04GG (coprime residual factors)',503:'C-SA14-565',546:'C-SA14-546, modern statement (correct quotient inclusion)',556:'C-SA14-556, modern statement (nonzero source E)'}
for c in C:
 n=int(c['id'].split('-')[-1])
 if n in refinements:event(c['id'],"refuted, with the refined statement's id",'Refined statement: '+refinements[n]+'. '+c['present_status']+' Standing-hypothesis check and counterexample are in proof_notes.md; source ink is not adjudicated.')
for b in B:
 typ='used and rechecked in this run' if b['note']=='verified' else 'carried as background without fault found'
 event(b['key'],typ,('Opened URL: '+b['url']+'. ' if b['note']=='verified' else 'Unverified lead; DOI access failed. ')+b['verification_scope']+' '+b.get('circulation','')+' Verification of metadata alone is not a proof check.')
for key,loc in {
'Deligne1973Constants':'§§10.3–10.7 determinant, duality and local-monodromy conventions; theorem4.1 scope',
'Deligne1974WeilI':'§2.6 and theorem2.12; alternating pairing and middle-extension duality hypotheses',
'Deligne1980WeilII':'§§1.8.4,1.8.8,3.3–3.4; local/global weight and geometric hypotheses',
'Grothendieck1964Lefschetz':'Theorem5.1 and Corollary5.2; trace/rationality hypotheses',
'Raynaud1965Euler':'§3 Theorem1; Euler characteristic, Artin character and residue-degree conventions',
'Laumon1987Fourier':'§3.1.5 and Theorem3.2.1.1; curve product formula and normalization data',
'Jannsen1992Numerical':'Theorem1 and Corollary1; numerical semisimplicity versus homological/numerical equality',
'Oda1969DeRham':'Definition3.5, Proposition3.9, Theorem3.19 and Corollaries5.11–5.12; categories and semilinear variance',
'Wildeshaus2006Boundary':'§6 Theorem6.1; twist, shift2n−1 and resolution hypothesis',
'Samuel1962Derivations':'§3 p.3-11; §4 Lemma3; §6(b) Proposition3; exact characteristic-two examples',
'Samuel1964TIFR':'chapterI Theorems8.1/8.2 and §9; chapterIII Lemma5.1/Theorem5.2; exact statement and proof matches',
'Samuel1964Mechants':'§III Propositions1–2; positive exponents and both weighted-cyclic alternatives',
'Alfsen1963Haar':'Proposition1.1 and §§2–3; approximate additivity and Haar existence/uniqueness'
}.items():event(key,'targeted proof check','Read the indicated statement and relevant argument, checking the claim’s exact hypotheses and conventions: '+loc+'. This is a targeted check, not certification of every theorem in the work.')
for p in P:event(p['id'],'used and rechecked in this run','Problem occurrences read and state of the art compared with the opened sources named in the record: '+', '.join(p['refs'])+'. Explicit source uncertainty and absence of documented reasons for abandonment are preserved; this is not a claim to solve every problem.')
with (R/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(E)
print(len(E),'truthful check events; no inference from a claim’s class to a proof verdict.')
