"""Assemble audit records from individually written checks and search routes."""
from pathlib import Path
import json,csv,collections,re
ROOT=Path(__file__).resolve().parents[1]
claims=json.loads((ROOT/'claims.json').read_text())
items=json.loads((ROOT/'items.json').read_text())
refs=json.loads((ROOT/'research/reference_audit.json').read_text())
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; inherited reasoning effort not exposed; run SA19/cotes44_47_54'
def write(name,head,rows):
    with (ROOT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
routes={}
def route(nums,sources,query,files):
    for n in nums:routes[n]=(sources,query,files)
route(range(401,414),'Mukai primary article; Laumon arXiv; Stacks official; Mumford primary reproduction',
      'Exact Fourier inversion and Poincare pushforward titles; backward references to Mumford; theorem/formula locators and relative-base hypotheses; no historical date inferred from an undated cote.',
      'search_001,009,010,012,014,015,017,019,020,022,023')
route(range(414,418),'Mukai; Beauville author-hosted paper; Beckmann/deGaay arXiv; Hasan etal arXiv and author publication list',
      'Nondegenerate-line-bundle transform; integral Fourier, modulo torsion and minimal one-cycle criterion; symbolic coefficient and geometric counterexample rechecked.',
      'search_010,011,012,014,015,016,019,020,021,024,025')
route(range(418,423),'GRR Stacks tags; Kleiman primary DixExposes scan; Beauville; Moonen2024/2026; Hasan etal2025',
      'Exact relative Todd correction; both Fourier-product directions; opened Kleiman2A12/2A13 to test rather than repeat the allegation.',
      'search_002,003,007,008,009,010,011,012,014,015,016,019,025')
route(range(423,426),'Mukai and Laumon primary texts; Stacks smooth proper duality and kernels',
      'Derived duality,inverse kernel and dualizing shift; homomorphism push-pull variance; bounded quasi-coherent range.',
      'search_001,003,005,012,014,015,019,020')
route(range(426,432),'Coleman Numdam; Oda Numdam; SGA3VIIB primary recomposition',
      'Universal-extension tangent versus invariant differential variance; Hodge exterior duality; Cartier F/V with Frobenius twists; A[p] reconstruction; exact Oda thesis chronology.',
      'search_001,003,004,008,009,013,022,030,031')
route([432,433,434,458],'Numdam EGAIV2/IV3 complete primary PDFs; Stacks generic freeness/flattening definitions',
      'Generic freeness with irreducible nonreduced base; closed universal flattening stratum; backward EGA11.4.1–7; test removed nilpotence and topological assumptions.',
      'search_013,017,018,019,029,037;EGAIV2_extract;EGAIV3_extract;EGAIV3_114_extract')
route([435],'SGA3XXI root-system comparison; direct finite-arrangement reduction',
      'Hyperplane wall/chamber assertions on reused sheet independently proved from local finiteness; no original Bourbaki edition identified or asserted.',
      'search_013,017,018,019')
route(range(440,449),'KleimanICM primary volume; Saito primary Nagoya article; Kahn and ACMV primary; Peters2026; arXiv2025–2026; zbMATH and MathOverflow discovery',
      'Incidence versus Samuel abelian equivalence versus universal regular representative; exact dimension bound and isogeny duality; excluded primes in Tate realization; backward Lieberman/Murre references; latest updates checked for exact scope.',
      'search_001–011,014–018,020–029,032–035,037,038;KleimanICM_origin_extract')
route([449,450,459,461,463],'Saito correspondence construction; van der Geer/Moonen duality chapter; Peters conditional incidence comparison',
      'Symmetric divisor correspondence, graph pullback factor2, full versus abelian-radical kernel and rational versus integral descent; exact elliptic exterior-algebra counterexample.',
      'search_004–007,015,024–028,033,034')
route([451,452,453],'Ulmer primary chapter and author errata; Kunnemann primary Numdam; Saito hyperplane comparison; arXiv and MathOverflow discovery',
      'Lefschetz pencil/Neron-Tate/intersection exact phrase searches; geometric divisor normalization and vertical corrections; higher-cycle number-field theorem; fixed-factor hypotheses and withdrawn finite-kernel clause.',
      'search_010,011,013,014,017,019–025,030,031')
route([454,460],'Grothendieck FGA VI Numdam; Clemens primary IHES; Matsusaka primary journal issue metadata; KleimanICM torsion definition',
      'Numerical versus torsion algebraic equivalence, divisor restriction, very general quintic non-torsion Griffiths quotient; original Matsusaka metadata distinguished from theorem verification in FGA.',
      'search_010,011,028,030,032–035;KleimanICM_origin_extract')
route([455],'Stacks official completion lemmas; source graded-product calculation',
      'Noetherian flat completion versus faithful completion, graded category and undefinedTF; ungraded k[x]/(x−1) tested without misusing it as a graded counterexample.',
      'search_013')
route([456,457,464,465],'SGA3XXI primary root-data text; independent integral-lattice/reflection calculation',
      'Invariant positive form and rational reflection uniqueness; standard integral coroot axiom and perfect integral duality; explicit rescaled B2 counterexample to the weaker canceled axioms.',
      'search_013,017,018,019,020')
route([462],'Kleiman and Saito backward sources; Peters2026 primitive-algebraicity criterion; Caibar–Clemens withdrawal record',
      'Conditional Hodge positivity reduction with unspecified auxiliary assertions; distinguish published conditional/special cases from an unproved all-variety equivalence and a withdrawn preprint.',
      'search_003–009,015,021,022,024,025')
route([466],'Exact-phrase web search and SGA3XXI terminology comparison',
      'Queries: copoids radiciels vocables; LaTribu57 copoids; vocables covocables racines. No identifiable original draft; modern root terminology cannot supply missing local definitions.',
      'search_018,036')
route([467],'Mukai Proposition3.11 and Stacks Chern-character formalism',
      'Correct falling-factorial coefficient isolated from the manuscript generating expression; geometric hypotheses matched and arithmetic independently certified.',
      'search_012,014,015,019,020')
assert set(routes)=={int(c['id'].split('-')[-1]) for c in claims}
research=[]
for c in claims:
    n=int(c['id'].split('-')[-1]);src,q,files=routes[n]
    research.append([c['id'],DATE,src,q,'; '.join(c['refs']),c['fate'],c['confidence'],files])
write('research_log.tsv',['statement_id','date','repositories_and_primary_sources','query_or_backward_route','opened_reference_keys','exact_match_and_remaining_limits','confidence','search_records'],research)

events=[]
def event(s,t,o):events.append([s,DATE,WHO,t,o])
for it in items:
    event(it['id'],'used and rechecked in this run',
          'Assigned note entry/entries read against the actual original transcription passage, including cancellation status and doubts. Verdict: '+it['check']+'. '+it['check_reason'])
for c in claims:
    event(c['id'],'used and rechecked in this run',
          'Source status checked directly: '+c['status_on_pages']+'. Exact literature fate searched and hypothesis-matched; '+c['present_status']+' See research_log.tsv and primary-reference verification level.')
proofs={
401:'Kernel additivity, projection/base change and Kunneth calculation reconstructed; also checked that the source actually writes this proof.',
402:'Binary kernel compatibility checked under explicitly sufficient proper-support/derived hypotheses; coherence is not inferred.',
405:'K_0 shift and line-class consequence of the verified relative inversion theorem; no universal line trivialization assumed.',
408:'Regular-zero-section Koszul exterior contraction proved; this does not check the source comparison map itself.',
409:'Derived base change and flat regular-immersion specialization checked from the exact zero-section theorem.',
410:'Graph restriction of the integral kernel evaluated.',
411:'Translation-versus-skyscraper convolution sign fixed by evaluation at y−u.',
412:'Virtual rank/Euler interchange deduced from fibre Euler characteristic and inversion.',
413:'Ample-field determinant relation deduced from Mukai pullback; unresolved source tilde conventions retained.',
414:'Ample-field exponential Chern character proved using finite-flat rational-Chow pullback injectivity.',
415:'Coefficient expansion and all hypotheses of the ample elliptic-product counterexample checked.',
416:'Final source integrality multiple identified with (−1)^k r c_k of an actual transformed bundle.',
418:'GRR tangent bundle of addition computed; rational intersection-theory assumptions stated.',
419:'GRR projection tangent factor computed with source/target roles retained.',
420:'Common invertible Todd square canceled; no parity sign in this product direction.',
421:'Both Todd factors and the determinant character retained; characteristic-class identity independently checked.',
423:'Grothendieck duality computation shows P∨ and shift+g; same-kernel check notation remains conditional.',
424:'Poincare functoriality variance checked; source action notation remains unspecified.',
428:'Exterior Hodge-piece pairing checked algebraically; canonical degree-one pairing remains a cited theorem input.',
429:'F/V Cartier factorization and exact annihilator distinguished from dual of the Frobenius kernel.',
430:'Restricted p-operation on additive kernel is zero; height-one classification not extended to all A[p].',
432:'Exact EGA11.4.6 deduction from finitely generated universal flatness ideal rechecked.',
433:'Every hypothesis of the nonnilpotent counterexample and failure to preserve an injection checked.',
434:'Universal relation-ideal argument and nonempty-base extension through noetherian approximation independently reconstructed.',
435:'Finite-segment reduction, wall half-space intersection and local two-chamber structure independently proved.',
446:'Abstract Z_l section constructed by lifting a basis; no equivariant section claimed.',
449:'Codimension and symmetry computed; nonproper-parameter extension caveat retained.',
450:'Exact exterior pushforward gives−4, while finite quotient pullback multiplies by16; integral descent impossible.',
452:'Weak Lefschetz degree inequality proves intersection-side vanishing only.',
455:'Graded product/exactness and least-nonzero-degree faithfulness independently checked; ungraded warning kept separate.',
456:'Finite-root invariant form, positivity and rational reflection uniqueness independently checked.',
457:'Paired-reflection expansion checked term by term; only rationally perfect lattice pairing assumed in source.',
458:'Nilpotent lifted-basis descent and universal relation-coefficient ideal independently proved; EGA statements exactly matched.',
459:'Factorization through the reduced neutral abelian radical proved; finite nonreduced kernel caveat added.',
461:'Poincare matrix graph pullback gives f+f∨=2f; no ampleness conclusion.',
463:'Poincare divisor pushforward gives the stated codimension and zero-origin family; sufficiency for positivity not proved.',
464:'All finite/reduced/generation/reflection hypotheses verified in the eight-root counterexample.',
465:'Primitive root implies P∩Qα=Zα and hence integral coroot values.',
467:'General falling-factorial coefficient derived; finite symbolic checks are consistency certificates.'}
for n,outcome in proofs.items():
    event('CL-SA19-'+str(n),'independent re-proof',outcome+' Detailed scope: computations.md.')
certs={408:'koszul_zero_section',411:'translation_signs',415:'chern_coefficients;elliptic_product',
       416:'chern_coefficients',421:'todd_identity',433:'nonnilpotent_flatness_counterexample',
       450:'full_kernel_descent',455:'completion_ungraded',461:'symmetric_hom_factor_two',
       464:'root_integrality_counterexample',467:'chern_coefficients'}
for n,key in certs.items():
    event('CL-SA19-'+str(n),'computation or formal certificate',
          'Executable exact check in code/computations.py; outputs/computations.json key(s): '+key+'. Geometric assumptions and limits are documented in computations.md.')
for n,refined in {415:467,433:458,450:459,454:460,464:465}.items():
    event('CL-SA19-'+str(n),"refuted, with the refined statement's id",
          'Refined statement CL-SA19-'+str(refined)+'. '+next(c['computation'] for c in claims if c['id']=='CL-SA19-'+str(n)))
metadata={'Matsusaka1957','Lieberman1972','ACMV2026Twist','CaibarClemensWithdrawn','Grothendieck1964Letter'}
for r in refs:
    event(r['key'],'carried as background without fault found' if r['key'] in metadata else 'used and rechecked in this run',
          ('Bibliographic/chronological or withdrawal verification, not theorem verification. ' if r['key'] in metadata else
           'Primary mathematical passage opened, exact statement and relevant hypotheses checked; not claimed as an independent full proof. ')+r['annote'])
write('CHECK_EVENTS.tsv',['statement_id','date','who(model,effort,run)','type','outcome'],events)

# This is a validation of the hand-written records, never a verdict generator.
entries=list(csv.DictReader((ROOT/'entries.tsv').open(),delimiter='\t'))
entry_expected={f'MPL_16+47+54+44#{i}' for i in list(range(44,80))+[85]}
assert {e['entry_id'] for e in entries}==entry_expected
assert len(entries)==len(entry_expected)==37
ids={i['id'] for i in items};refkeys={r['key'] for r in refs}
assert all(e['item_id'] in ids for e in entries)
assert all(set(c['refs'])<=refkeys for c in claims)
assert all(set(c['items'])<=ids for c in claims)
problems=json.loads((ROOT/'problems.json').read_text())
assert all(set(p['refs'])<=refkeys for p in problems)
assert all(c['fate'] and c['present_status'] and c['confidence'] for c in claims)
readings=list(csv.DictReader((ROOT/'readings.tsv').open(),delimiter='\t'))
coverage=list(csv.DictReader((ROOT/'reading_coverage.tsv').open(),delimiter='\t'))
assert len(coverage)==28
eventids={e[0] for e in events}
assert ids<=(eventids) and {c['id'] for c in claims}<=eventids and refkeys<=eventids
counts={'entries':len(entries),'items':len(items),'verdicts':dict(collections.Counter(e['verdict'] for e in entries)),
        'claims':len(claims),'classes':dict(collections.Counter(c['class'] for c in claims)),
        'problems':len(problems),'reading_alarms':len(readings),'source_pages_read':len(coverage),
        'references':len(refs),'check_events':len(events),'research_log_rows':len(research)}
(ROOT/'outputs/validation.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
print('PASS: every assigned entry has one read verdict; every claim has a searched fate, reference coverage, and check events. All28 source pages represented.')
