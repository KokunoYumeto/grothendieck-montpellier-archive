"""Record actual post-checkpoint08 reads, without upgrading universal gates."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
checks=[
 ('c:exterior-weight-criterion','part_c/c4_exterior_trait_criterion.tex',
  'Root read the complete revised fragment at clock-confirmed08:57–08:58UTC. The homogeneous Jordan basis, non-Frobenius-stable wedge witness, determinant average, elementary sl2 kernel calculation and lack of a semisimplicity hypothesis all pass. Root did not independently reopen Taylor–Yoshida in this audit.'),
 ('c:universal-trait-weight-equivalence','part_c/c4_exterior_trait_criterion.tex',
  'Root checked the complete written geometric transfers: N^(j+1)=0 from the semistable weight range; ordinary exterior powers with the Koszul-adjusted permutation; independent alteration fields L_r; degree-divided trace; finite-extension weight comparison; cohomological middle-degree retraction. The result is a universal trait equivalence, not a proof of WM or a complete arbitrary-morphism transfer.'),
 ('prop:B-fixed-open-ramification-obstruction','sections/b1_fixed_open_ramification.tex',
  'Root read the exact integrated TeX after the earlier standalone proof audit. The support-triangle degrees, weight-minus-one and weight-minus-two invariant exactness, divisor Tate plus Kummer comparison, projective-bundle motivic vanishing and flat-tensor quotient all pass. No survival under subsequent shrinking is asserted; no new independent reopening of owner purity sources is claimed.'),
 ('C6:conductor-scalar-scope','part_d/post08/conductor_and_euler_factor_scope.md',
  'Root read the complete written note. The N-kernel filtration yields a perfect inertia-cochain module with K0 class dim(V)[F]; the F-linear identity and commuting-idempotent traces ignore N, also in one degree and after periodization. The vertical blowup of P2 changes the special-fibre Euler scalar by2 while generic inertia remains trivial. Root did not independently open the five new source PDFs; their exact owner read scopes are retained.'),
 ('C4:Zhang-invariant-cycle-source','root_post08_zhang_audit.md',
  'Root opened and read Zhang2009.07089v3 section1.1 definitions and pairings pp8–9, complete Theorem1.3.1 proof pp14–16 and complete PropositionA.1.1 proof pp37–38; PDFp9 visually inspected. The invariant-cycle equivalence passes using supported localization duality and correcting the final proof display X_s to X_eta. Its H_psi is not defined as the geometric inertia-invariant image.'),
 ('C4:Zhang-pairing-counterexample','root_post08_zhang_audit.md',
  'Root constructed and checked the explicit curve y2=x(x−1)(x−5) overQ5, blowup charts and two rational P1 components with two transverse nodes. Hsupport1=0 and dimHpsi1=1, so the displayed alternating psi pairing is zero. The valid quotient-versus-kernel supported duality is proved separately. The exact polynomial certificate passed after the implementation-format corrections recorded in its run history. The claim concerns only the inspected v3 wording, not an uninspected published version.'),
]
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
for label,filename,outcome in checks:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label,date=now,who='GPT-6 Astra / root / current run',
                         type='targeted proof check',outcome=outcome))
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)

path=root/'ITEM_SCOPE_ADDITIONS.json'
scopes=json.loads(path.read_text())
new_scopes={
 'B.1':(['prop:B-fixed-open-ramification-obstruction'],
        ' On the specified two-boundary open in P4, the comparison cokernel is exactly im(G) intersect ker(cl) on its threefold components. This fixed-open formula neither proves vanishing nor proves survival under further shrinking.'),
 'C.4':(['c:exterior-weight-criterion','c:universal-trait-weight-equivalence','c:single-endpoint-insufficient','c:trait-exterior-scope'],
        ' The universal middle-degree trait endpoint is equivalent to weight–monodromy; an individual j-fold has a finite exterior-power test with r<=j+1. Both universal assertions remain unresolved, and the arbitrary-morphism transfer is separately scoped.'),
 'C.6':([], ' The inspected conductor formulas do not supply the missing ordinary inertia-invariant dimension: their additive derived-inertia scalar trace ignores the nilpotent rank even after a supplied homogeneous projector.')
}
for item,(labels,extra) in new_scopes.items():
    row=scopes.setdefault(item,dict(statement_ids=[],scope_append=''))
    row['statement_ids']=list(dict.fromkeys(row['statement_ids']+labels))
    if extra.strip() not in row['scope_append']:row['scope_append']+=extra
path.write_text(json.dumps(scopes,indent=2,ensure_ascii=False)+'\n')

note='''

## After checkpoint08: finite exterior tests and remaining method obstructions

The complete exterior-power criterion now proves that the universal middle-degree trait endpoint is equivalent to weight–monodromy. For an individual j-fold, the tests use ordinary exterior powers of orders at most j+1, realized as Galois direct summands on actual powers. Semistable alterations are made over separate extension fields for each power; no ramified base change is assumed to preserve a regular model. Root and both independent readers checked the written proof. This equivalent universal gate is not counted as a strictly smaller gate under the review rule.

The integrated fixed-open B1 comparison identifies its cokernel with a rational Chow Gysin obstruction on explicit threefold boundary components. The further moving-support and completion attempts still do not give uniform control under shrinking. Their exact failures are retained in the part notes; no rational Chow kernel is killed by a torsion or completion theorem alone.

The new conductor-source audit includes the October2026 Kisin result and the twisted Beraldo–Pippi formula. A supplied homogeneous projector does remove alternating degrees, but the specific additive trace over the inertia-cochain algebra still records the dimension of that summand, not the kernel dimension of monodromy. The full categorical object is not declared information-free. This is a proved limitation of the attempted scalar argument, not a refutation of C6.

The Zhang source audit independently checks the local invariant-cycle equivalence. It also supplies an explicit regular semistable elliptic model disproving the unconditional perfect-pairing wording for H_psi on p9 of the inspected arXivv3. A separate local subscript error in the invariant-cycle proof is corrected. The valid supported quotient-kernel duality is retained. These bounded source corrections do not refute weight–monodromy or the checked invariant-cycle theorem, and do not change an open universal row.

Formal review04 remains a no-movement review with consecutive count1. The next formal review is scheduled for09:50UTC (10:50Europe/Berlin); another review without qualifying movement invokes the user's stopping rule. Checkpoint09 remains scheduled for09:35UTC (10:35Europe/Berlin), with no intervening ZIP.
'''
for filename in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md','ROOT_CURRENT_SOURCE_RECHECK.md']:
    p=root/filename;s=p.read_text()
    if '## After checkpoint08: finite exterior tests' not in s:p.write_text(s+note)
out=dict(recorded_utc=now,checks=[dict(statement_id=l,file=f,
         sha256=hashlib.sha256((root/f).read_bytes()).hexdigest(),outcome=o) for l,f,o in checks],
         qualifying_movement=False,
         scope='Actual proof and source-read scopes only; no formal review is executed by this script.')
(root/'code/record_root_post08_audits_output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(recorded_utc=now,checks=len(checks),qualifying_movement=False),indent=2))
