"""Record the actual kinds of checks performed; never promote reading to proof."""
from pathlib import Path
import json,csv
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[1]
items=json.loads((B/'items.json').read_text());claims=json.loads((B/'claims.json').read_text())
problems=json.loads((B/'problems.json').read_text());refs=json.loads((B/'source_metadata.json').read_text())
records={x['key']:x for x in json.loads((B/'outputs/computation_records.json').read_text())}
E=[]
WHO='GPT-6 Astra Pro; effort inherited/unspecified; run SA16-2026-11-19-cote64-late'
def e(s,t,o,a,scope):E.append(dict(statement_id=s,date='2026-11-19',who=WHO,type=t,outcome=o,artifact=a,scope=scope))
for i in items:
    e(i['id'],'used and rechecked in this run',
      'Read every source note in this item and compared the actual cited transcript passage. '+i['check']+': '+i['check_reason'],
      'items.json; entries.tsv','Passage comparison and attribution only. It is not an ink decision or a mathematical proof event.')
for c in claims:
    e(c['id'],'used and rechecked in this run',
      'Read the actual statement and its local argument/correction. Status on the pages: '+c['status_on_pages']+'. '+c['fate'],
      'claims.json; literature_notes.md; claim_search_coverage.tsv',
      'Claim extraction, hypotheses and searched-source comparison. Additional proof and computation events below specify their actual narrower scope.')
    if c['computation']['checks']:
        ks=c['computation']['checks']
        assert all(k in records for k in ks)
        e(c['id'],'computation or formal certificate','Exact computation groups rerun successfully: '+', '.join(ks)+'.',
          'code/recompute.py; outputs/recompute.txt; outputs/computation_records.json',
          'Only the listed symbolic, finite-group, free-word or finite-field identities. Sampled characteristics do not establish a universal theorem.')

# Explicit proof work completed, with partial comparisons labelled as such.
proofs={
 502:('1','Tensor compatibility of the scalar twist; the O(1) example refutes the literal general-module formula.'),
 503:('1','Square-compatible line isomorphisms form a μ2 torsor; inverse constructions are given.'),
 505:('1','Rigidity subclaim only: ordered level two leaves ±1 and a nonzero tangent pinning kills −1. Exact symmetric existence/descent is not proved by this event.'),
 507:('2','The fibre product has twelve elements, nontrivial central transposition lifts of order four, and presentation C3⋊C4.'),
 508:('2','Commutators generate C3; the abelianization is C4 and the centre C2.'),
 511:('1','Constructed the inverse torsor/root-line functors and checked evaluation identifies their composites.'),
 513:('1','The explicit Q0 model is trivialized after choosing i by s=1−i; this is the reconstructed example, not manuscript ink.'),
 514:('7','Two independent coordinate equations cut out the required one-dimensional kernel. No tensor-square scale follows from this alone.'),
 516:('4','Applied Riemann–Roch to the stated smooth genus-one curve and recorded the exceptional degree-one graded piece. This is a checked specialization, not a new proof of Riemann–Roch.'),
 517:('4','Pole valuation and the Leibniz rule give the filtered and graded derivations with the stated shift.'),
 518:('4','Laurent leading terms force −n, or −nc after multiplicative rescaling; coefficient one in all degrees violates Leibniz.'),
 519:('4','Combined the opened differential-kernel theorem with pole valuations to obtain the exact filtered pth-power kernel; x^p in F_(2p+1) refutes the proposed p∤n rescue.'),
 520:('4','Checked the degree-by-degree Rees kernel k[S] in characteristic zero and R^p[S] over a perfect field of characteristic p.'),
 521:('4','Pole orders and the even/odd involution give the displayed bases and shifted derivation targets.'),
 522:('4','The zero tangent vector forces x into constants and y=0; a nonzero vector is necessary for the coordinate basis.'),
 523:('4','Exhibited both coherent principal-part conventions, with leading coefficient four or one. This does not identify the missing convention or decide the ink.'),
 524:('5','Restriction to three distinct branch values is the Vandermonde map; the odd kernel is ky. The author also completes the argument on106.'),
 525:('5','Factored the cubic and compared all coefficient signs with the definitions.'),
 526:('5','Derived the coordinate-translation formula and the exact role of invertibility of three in trace-zero normalization.'),
 527:('5','Applied the derivation to the defining relation; the linear a2P and double derivative are the compatible alternatives.'),
 528:('5','Checked the smooth cubic with origin, its weighted section ring, its genus-one interpretation and all four branch points under the stated hypotheses.'),
 529:('5','Used the line-section divisor criterion for distinct finite points and checked the repeated-row counterexample. The manuscript correction is retained.'),
 530:('5','Factored the secant intersection polynomial and obtained the negative-sum formula on the exact domain x(P)≠x(Q).'),
 531:('5','Compared the affine coordinate freedom with fixed principal part and nonzero tangent vector.'),
 532:('6','Computed the descended two-torsion translation, its rational-function identity and its undivided zero-root limit.'),
 533:('6','Solved the fixed-point equations for halves of each nonzero two-torsion point; distinctness and characteristic≠2 give four halves each.'),
 534:('6','Expanded (r−u)(r−v) in the manuscript coefficients and checked the roots1,2,3 counterexample to the written signs.'),
 536:('7','The ratio v/f constructs the claimed canonical sequence comparison independently of the choice of f.'),
 537:('7','Weight−1 covariance makes φ_i(δ)δ independent of the chosen tangent basis. It does not define a connection.'),
 538:('7','Solved the cyclic-difference linear system and checked both Vandermonde signs.'),
 540:('8','Constructed the inverse maps between conjugate-transverse lines and complex structures; the formula requires φ inverse.'),
 541:('8','A faithful circle with two conjugate weights has weights±1; orientation and metric assertions are checked in their exact dimensions.'),
 542:('8','The determinant of (e1,J_ze1) is negative, confirming the authorial withdrawal and the changed line convention.'),
 543:('8','The first period ratio is antiholomorphic, whereas the second draft uses a holomorphic coordinate. The former cannot represent a holomorphic framed family with that parameter.'),
 545:('9','Derived the right framing action and checked the anti-automorphism converting it to the conventional left action.'),
 546:('9','Verified the automorphy-factor cocycle directly by multiplying determinant-one matrices.'),
 547:('9','Derived the conjugation on the translation lattice for the exact written order of operations and its semidirect-product law.'),
 548:('9','The total family over contractible H has fundamental group Z², so it is not the asserted universal covering base. The stack statement is separated.'),
 550:('9','Rank-two abelianization and the explicit generator lifts/relations were checked. This event does not claim a new proof of the full Nielsen theorem used from the opened literature.'),
 551:('9','Checked period-frame and tangent-frame transformations using the lattice model and the dual line variance.'),
 552:('9','The pair (−1,−I) fixes the framed base and acts by negation on the fibre, leaving three nonzero two-torsion fixed points after removing zero.'),
 553:('9','Checked the cancelled split-extension normal-form multiplication; no specific meaning is assigned to the nearby undefined diagram.'),
 554:('10','Unique factorization gives the signed square-class representative; the sign is retained in the radicand.'),
 555:('10','Proved the conditional DVR criterion and the higher-dimensional normal counterexample. The uncertain ring word remains undecided.'),
 556:('10','A nonsquare residue unit makes the local quadratic algebra a DVR, with purely inseparable residue extension in characteristic two.'),
 557:('10','Proved independence of b modulo m², the regularity criterion and the missing integral generator when b∈m².'),
 558:('10','Specified the T-adic completion and checked when its topology agrees with the local one. The split b=0 example separates them.'),
 559:('10','Computed the tangent cone, the v(2)=1 criterion and both equal-characteristic and ramified mixed-characteristic counterexamples.'),
 560:('11','Applied R1+S2 with all hypersurface hypotheses checked to eliminate a residual finite nonnormal set.'),
 561:('11','Proved necessity and sufficiency for generic étaleness at all rational primes; constructed the integral generator and proved the resulting order is the full normalization.'),
 562:('11','Tested full signed radicands3 and−1 against unsigned Q=1. This refutes only the unsigned interpretation; it does not decide the handwritten abbreviation.'),
 563:('11','Compared coefficients modulo four and modulo two; λ=2 separates the two written conditions.'),
 564:('11','Changed coordinates at infinity, normalized the corrected chart and checked the λ=4,x=0 counterexample to the opposite sign.'),
 565:('10','Compared the scratch quadratic with the previously derived tangent cone; ambiguous β/β² is harmless over the explicitly written F2.')}
for n,(sec,out) in proofs.items():
    e('C-SA16-'+str(n),'independent re-proof',out,'proof_notes.md, §'+sec,
      'The explicitly named assertion or subassertion only; manuscript proof status and unresolved readings remain separate.')
e('C-SA16-512','targeted proof check',
  'Read and checked the early64 quadratic-cover/root-line proof: local Legendre μ2 twists, the deck action on the tangent, and stack descent establish the geometric equivalence over arbitrary base with two invertible.',
  'proof_notes.md, §1; ../cote64_early/proof_supplement.md, §9',
  'Geometric groupoid equivalence only; the distinguished symmetric μ4 normalization and coordinate scale remain separate.')

for p in problems:
    e(p['id'],'used and rechecked in this run',
      'Read all listed occurrences and distinguished the authorial request from the current formulation. '+p['closure_status'],
      'problems.json; literature_notes.md','Open-on-pages status is not a claim that the problem remains open in modern mathematics.')

extra={
 'SA16-502':['Q0_example'],'SA16-511':['special_parameters'],'SA16-512':['special_parameters'],
 'SA16-520':['branch_coordinates'],'SA16-530':['translated_cubic'],
 'SA16-535':['secant_coefficients'],'SA16-545':['Picard_Fuchs_bridge'],
 'SA16-546':['Hasse_bridge'],'SA16-575':['modular_matrices'],
 'SA16-576':['modular_matrices'],'SA16-579':['p_curvature_bridge']}
for sid,ks in extra.items():
    assert all(k in records for k in ks)
    e(sid,'computation or formal certificate','Earlier-run mathematical addition independently rerun: '+', '.join(ks)+'.',
      'code/recompute.py; outputs/recompute.txt; outputs/computation_records.json',
      'This is a checked addition, not a formula attributed to the manuscript. The universal Hasse statement uses the separate coefficient proof, not the sample primes alone.')
e('SA16-546','independent re-proof','The binomial coefficient recurrence and coefficient extraction prove the Hasse identity for every odd prime.',
  'proof_notes.md, §12','Earlier-run bridge calculation; no historical connection identification follows.')
e('SA16-578','used and rechecked in this run','Matched zero p-curvature descent to Katz Theorem5.1 and the nilpotence bound to Theorem5.10.',
  'literature_notes.md; proof_notes.md, §12','Opened source comparison, not an independent proof of the Gauss–Manin theorem.')
e('SA16-589','used and rechecked in this run','Matched the differential-frame braid group and central generator to Hain Proposition8.2, Corollary8.3 and Remark8.4.',
  'literature_notes.md; proof_notes.md, §12','Opened source comparison, not manuscript content and not a complete independent proof of the braid-group theorem.')

for r in refs:
    if r['note']=='verified':
        e(r['key'],'used and rechecked in this run','Opened and compared: '+r['locator']+'.',
          'literature_notes.md; references.bib','Source use at the exact stated scope; this alone is not a proof audit.')
    else:
        e(r['key'],'carried as background without fault found',
          'Bibliographic lead checked; primary text unavailable. No theorem proof or historical first occurrence certified.',
          'literature_notes.md; references.bib','Unverified primary-text lead, explicitly marked in the bibliography.')
for key in ['EGAIV2','Stacks031O']:
    e(key,'targeted proof check','Read the full R1-and-S2 proof and checked the hypotheses of its use for the quadratic hypersurface.',
      'literature_notes.md; proof_notes.md, §11','Normality criterion and this application; not a check of all results in the volume.')

refinements=json.loads((B/'refinements.json').read_text())
for r in refinements:
    target=r['refines']
    # The 543 and 550 rows record a literal erroneous draft; the author’s later correction/omission is retained.
    e(target,"refuted, with the refined statement's id "+r['id'],
      r.get('qualification',r['statement']),
      'refinements.json; proof_notes.md','Only the literal or unrestricted statement specified in the refinement. This does not adjudicate uncertain ink.')
e('Hain2021:Prop3.15',"refuted, with the refined statement's id R-SA16-L64-Hain315",
  'The same literal strict C2×S3 quotient in the 2021 revision has the incompatible harmonic stabilizer. The bounded counterexample is unchanged.',
  'proof_notes.md, §3; refinements.json','This is a result-specific counterexample, not a refutation of the source’s other theorems.')

with (B/'check_events.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome','artifact','scope'],delimiter='\t')
    w.writeheader();w.writerows(E)
allcomputed=set(k for c in claims for k in c['computation']['checks'])|set(k for ks in extra.values() for k in ks)
assert set(records)<=allcomputed,(set(records)-allcomputed)
with (B/'progress.log').open('a') as f:
    f.write(datetime.now(timezone.utc).isoformat()+'\tCHECK_EVENTS\t'+str(len(E))+' truthful events; all31 computation groups represented.\n')
print('Events',len(E),'items',len(items),'claims',len(claims),'problems',len(problems),'computation groups',len(records))
