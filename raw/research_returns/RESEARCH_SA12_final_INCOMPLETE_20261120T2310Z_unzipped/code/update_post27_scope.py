"""Record the completed bounded-period enlargement without a formal review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
p = root / 'code/assemble.py'
s = p.read_text()
before = hashlib.sha256(s.encode()).hexdigest()
replacements = [
    ('; twisted projective hereditary counting remains open',
     '; this theorem concerns ordinary representations'),
    ('Checkpoint26 is the latest created and delivered archive; checkpoint27 is scheduled20:25UTC.',
     'Checkpoint27 is the latest created, verified and delivered archive; checkpoint28 and review19 are scheduled21:10UTC.'),
    ('Arbitrary projective crowns outside the earlier tame criteria remain open.',
     'This linear result does not itself give a projective crown estimate.'),
    ('The exact projective-cost diagnostic is retained separately as research, and hereditary projective counting remains open.',
     'The exact projective-cost diagnostic is retained separately as research; this refinement alone does not prove a hereditary projective count.'),
    ('Local order-action lifting retains a specified lower jet; simultaneous global Morita-unit and overlap effectivity is still a separate obligation.',
     'Local order-action lifting retains a specified lower jet; simultaneous global Morita-unit and overlap effectivity requires the subsequent separate theorem.'),
    ('hereditary projective constants for arbitrary finite covers, uncovered cross-characteristic Lie families',
     'unbounded-period hereditary projective constants for arbitrary finite covers, uncovered cross-characteristic Lie families')
]
for old, new in replacements:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
marker = "for supplement in ['report_supplement.md','PROGRAM_RUNS.md']:"
assert s.count(marker) == 1
addition = '''if any(row['id']=='D:bounded-period-hereditary-projective-growth' for row in rows):
    report.extend(['','## Current developments after checkpoint27','',
    'The completed bounded-period theorem proves q^(A_R,B t r^2) ambient PGL_r(F_q) conjugacy classes on every connected degree-t punctured cover of a fixed complete excellent normal local surface, whenever the geometric Brauer period is at most a fixed B. Scalar coefficient order remains unrestricted. Actual canonical full orders and Hom modules have degree-linear budgets; a rank-M² anchor for M<=B gives bounded-rank fixed algebra data. The new simultaneous Morita-Frobenius theorem corrects actions, balanced arrows, inverses and overlap cocycles over arbitrary coefficient rings, retaining the stated lower jet. Algebraization is restricted to the stated proper complete Noetherian bases. Morita reconstruction takes place only on the puncture.',
    'Actual determinant ratios and nonnegative multidegrees give finite generated determinant lists. Whole-cycle Hom complexes with two variable object ends provide O_R,B(ftr²) variables and bounded-degree equations. Generated fixed-determinant unit-Isom schemes are etale with clopen class images, including the noncanonical objects in this atlas. The same retained finite marking identifies every original canonical punctured class with its constructed realization. No intermediate-lattice cohomology or relative root-stack hull flatness is inferred.',
    'The faithful ordinary projective crown consequence allows arbitrary permutation quotients with its explicit bounded residual outer index and quadratic simple-order comparison. The multiplier condition is implied by gcd(r,q-1)<=B or by the stated compatible central lift. Its generator estimate retains max{2,d(P),c_R+2}. The count, object/comparison prerequisites and crown closure form one prospective main-gate reduction for review19, not separate events. Unbounded-period hereditary projective counting, projective semilinear counting beyond the earlier tame scope, unrestricted alternating multiplicities and full finite generation remain open. No requested outcome closes.'])
'''
s = s.replace(marker, addition + marker)
outcome_marker = "report=['INCOMPLETE','','# Research report: SA12'"
if outcome_marker not in s:
    raise AssertionError('Exact requested-outcome output marker must be checked before insertion.')
outcome_addition = '''if any(row['id']=='D:bounded-period-hereditary-projective-growth' for row in rows):
    bounded_period_hereditary_scope='; for every fixed geometric Brauer-period bound B, ordinary PGL_r(F_q) classes on every degree-t complete punctured surface cover satisfy q^(A_R,B t r²), with unrestricted scalar coefficient order; faithful projective crowns satisfying the stated multiplier, bounded outer-index and quadratic-order hypotheses allow arbitrary permutation quotients and retain d(P)'
    bounded_period_hereditary_labels='D:finite-Morita-Frobenius-object-effectivity; D:generated-Morita-unit-Isom-openness; D:bounded-period-hereditary-projective-growth; D:bounded-period-arbitrary-quotient-projective-crowns'
    outcomes=[(item,state+bounded_period_hereditary_scope,locator+'; '+bounded_period_hereditary_labels) if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
'''
s = s.replace(outcome_marker, outcome_addition + outcome_marker)
p.write_text(s)
record = dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
              source='code/assemble.py', before_sha256=before,
              after_sha256=hashlib.sha256(s.encode()).hexdigest(),
              formal_review_performed=False, archive_created=False,
              requested_status_changes=[],
              scope='Completed bounded-period ordinary projective count and its crown closure; all other gates retained.')
(root/'code/output/post27_scope_update.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
