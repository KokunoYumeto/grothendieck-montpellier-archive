"""Perform the first scheduled three-hour review, preserving its dated baseline."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT=Path(__file__).resolve().parents[1]
started=time.monotonic()
now=datetime.now(timezone.utc).replace(microsecond=0)
due=datetime(2026,11,19,5,50,tzinfo=timezone.utc)
if now < due:
    raise SystemExit('The first formal review is due at05:50UTC; do not record it prematurely.')
target=ROOT/'progress/review_01.json'
if target.exists():
    raise SystemExit('Formal review01 already exists and will not be overwritten.')
with (ROOT/'ITEM_STATUS.tsv').open(newline='') as stream:
    items=list(csv.DictReader(stream,delimiter='\t'))
by_item={row['item']:row for row in items}
open_rows={
 'B.1':('Under universal Tate and eigenvalue-one semisimplicity: cycle injectivity in codimension m on every smooth projective variety of dimension2m−1, m≥2. First case(d,i)=(3,2), equivalently H4(F0 P4,Qell(3))^Gamma=0 under those hypotheses.',
         'Numerical comparison does not kill Chow phantoms. Ordinary surface Chow equality does not control endomorphisms on its square. The new published half-range reduction and split product map genuinely reduce the universal index set.'),
 'B.3':('Universal ell≠p abelian-scheme finiteness over every finite-type base, including singular/nonreduced/nonseparated bases, is equivalent to surface Tate, or H3(F0 P3_Fbarp,Qell(2))^GammaFp=0. The all-bases extension passed full B/D/root audits just before this review and is preserved as a complete proof note awaiting typeset integration. For relative-curve Brauer quotients the compiled theorem covers regular separated bases; the arbitrary singular genus-one base-image obstruction remains.',
         'The full characteristic-primary assertion is refuted explicitly. Proper-cover rational-section descent, Frobenius/Verschiebung, and the weight−1 Cech kernel remove the separate singular-base gate for abelian schemes. They do not yet control a non-torsion base H2(Gm) class that becomes torsion after pullback to an arbitrary genus-one family.'),
 'B.5':('General prescribed pure-motive rational realization and compatible arithmetic duality; already in degree1 on a number ring this includes the appropriate Sha-finiteness/Bloch–Kato comparison. Finite coefficients and Tate/Artin–Tate cases are proved.',
         'Tensoring finite torsion duality with Q gives zero. A formally defined graded dual completion does not construct the required global motivic category or prove its realization maps.'),
 'C.1(c)':('Finite necessary-and-sufficient rational cycle criteria are proved under C+ for any Weil field, effective with the stated coefficient data. Actual finite Chow vanishings remain; general K3 requires wedge^(23−rho)t2(X)=0, including Picard-rank1 K3 surfaces.',
             'Tautological parity is not forced, as E times P1 shows. An idempotent antisymmetrizer is nilpotent exactly when zero. Nilpotence on S times S does not propagate to all powers. Kuga–Satake specialization still requires algebraicity or a Chow lifting statement.'),
 'C.4':('General sharp R0 endpoint in weights j≥3. The first normalized trait case is H3 of an arbitrary semistable projective threefold over a mixed-characteristic local field; the endpoint is exactly its weight-monodromy assertion.',
         'The two extreme weight rows are now removed, proving the endpoint for j≤2 and the bound2j−2 for j≥2. The interior R^i weight envelope cannot be lowered uniformly because the Legendre symmetric-power examples attain it.'),
 'C.6':('Independence of the unramified flag for arbitrary pure motives, or an exact equivalence with a named conjecture. Abelian-type and the stated hyper-Kähler homogeneous Chow tensor cases are proved; arbitrary nonalgebraic projectors remain outside the trace argument.',
         'Finite-extension strong compatibility does not descend unramifiedness through ramification. Weight-monodromy/Fontaine compatibility supply sufficient hypotheses, not a proved converse. The literal inertia-kernel statement is stronger and already false in the Tate-curve example.'),
 'Lead B1':('The universal finite-field comparison retains the B.1 diagonal cycle gate. Arithmetic local conditions and their conjectural global completion are now precisely distinguished.',
             'The extension-degree factor is proved; literal continuity to the algebraic closure is refuted. These facts do not prove the remaining Chow vanishing.'),
 'Lead C1':('Modified-diagonal identification is proved, but the requested all-powers general K3 theorem retains the same transcendental exterior-power gate as C.1(c).',
             'Beauville–Voisin controls the small-diagonal identities; it does not by itself prove the high determinant relation. The smaller transcendental test uses divisor projectors outside the narrow ring.')
}
movement=[
 'A.3–A.5 closed their stated class, unframed-data, and signed-comparison gates in the corrected scopes during the first three hours.',
 'B.4 obtained a proved terminating determination of every requested group and generator, replacing the former unresolved finite-group/generator stage.',
 'B.1 reduced universal Chow injectivity to the odd-dimensional middle-plus-one index set.',
 'B.2 completed the requested precise conjectural formulation and its proved specializations; universal existence is not being claimed.',
 'B.3 proved the arbitrary-base equivalence chain, refuted the literal full-Brauer assertion, and reduced the regular separated prime-to-p relative-curve question to the fixed surface/single-group gate. The fully audited late proof note also gives the same surface gate for abelian-scheme finiteness over every finite-type base; it is counted in this review, not deferred to manufacture movement at the next review.',
 'C.1 removed the infinite-list and rational-Betti scope obstacles under explicit C+, while leaving the actual Chow vanishing and general K3 gate open.',
 'C.4 proved the sharp low-weight R0 endpoint and reduced the first remaining trait case to H3 weight-monodromy on threefolds.'
]
record={'review':1,'scheduled_at':due.isoformat(),'reviewed_at':now.isoformat(),
        'movement':True,'consecutive_reviews_without_movement':0,
        'movement_evidence':movement,'all_item_rows':items,
        'open_mathematical_rows':{key:{'recorded_status':by_item[key]['status'],'current_gate':value[0],
                                      'attempts_and_limits':value[1]} for key,value in open_rows.items()},
        'main_A_status':'Closed in the exact corrected/conditional scopes permitted by the task; no unconditional full Tate theorem is asserted.',
        'main_D_status':'Corrected determinations, counterexamples and the permitted exact general comparison-class equivalence are proved.',
        'B2_scope_note':'General existence is a conjectural formulation explicitly requested in B.2; it is not counted as an established general Bloch–Kato theorem or as closure of B.5.',
        'editorial_rows':{key:by_item[key] for key in ['E.1','E.2']},
        'next_formal_review':'2026-11-19T06:50:00+00:00',
        'stop_rule':'Stop after two consecutive formal reviews without an open-row status change or a strictly smaller main gate. Packaging, restatement and unrelated special cases do not count.'}
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
lines=[f'\n## Formal three-hour review01 — {now:%Y-%m-%d %H:%M:%S} UTC\n',
       'Mathematical movement has occurred. Consecutive formal reviews without movement: **0**. The programme remains incomplete. The next formal review is due06:50UTC.\n',
       'The full44-row item snapshot is preserved in `progress/review_01.json`. Every mathematically open item and Lead is listed below; conditional hypotheses are not silently treated as established.\n',
       '| Open row | Current gate / smallest instance | Attempts and exact limit |',
       '|---|---|---|']
for item,(gate,attempt) in open_rows.items():
    lines.append('| '+item+' | '+gate.replace('|','\\|')+' | '+attempt.replace('|','\\|')+' |')
lines+=['\nMovement counted in this review:\n']+['- '+entry for entry in movement]
lines+=['\nA and D remain closed only in their explicit corrected or permitted conditional scopes. B.2 now supplies the requested conjectural formulation and specializations; it does not prove existence of the general arithmetic completion. E.1/E.2 concern indexing and source audit, which do not count as mathematical movement.\n',
        'The next attacks remain the B.1 first threefold invariant, the B.3 surface invariant, general prescribed arithmetic realization, the general K3 exterior-power cycle, mixed-characteristic threefold weight-monodromy, and general unramified-flag independence. The failed routes recorded above are not promoted to refutations of these open statements.\n']
ledger=ROOT/'PROGRESS_LEDGER.md';ledger.write_text(ledger.read_text()+'\n'.join(lines))
report=ROOT/'RESEARCH_SA05_report.md'
report.write_text(report.read_text()+f'\n## Scheduled progress review01\n\nThe first formal three-hour review was completed at{now:%H:%M:%S}UTC. The dated ledger lists every mathematically open row, the smallest remaining gates, the unsuccessful approaches and the actual movements. The no-movement count is0; work continues. The complete item snapshot is `progress/review_01.json`. This is not an overall-completion declaration.\n')
result={'review':1,'reviewed_at':now.isoformat(),'open_mathematical_rows':len(open_rows),
        'all_items':len(items),'movement':True,'consecutive_without_movement':0,
        'seconds':round(time.monotonic()-started,6)}
(ROOT/'code/first_progress_review_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
