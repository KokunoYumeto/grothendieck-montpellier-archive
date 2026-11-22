"""Record root's complete recognition/source audit; no finite certificate."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

root = Path(__file__).resolve().parents[1]
path = 'parts/C/post26_research/D_non_natural_alternating_primitive_models.tex'
sha = hashlib.sha256((root / path).read_bytes()).hexdigest()
assert sha == '9dfea2c79ad13c264be3f1e39192b5dc9044e1df38307c7e7c3c4d065336f31a'
out = root / 'parts/D/post26_research/audit_C_non_natural_alternating_models_root.json'
assert not out.exists()
record = dict(
    actor='root', model='GPT-6 Astra Pro', effort='setting not independently exposed',
    run='SA12 run1', recorded_utc=datetime.now(timezone.utc).isoformat(),
    path=path, sha256=sha, verdict='PASS', type='targeted proof check',
    labels=['D:non-natural-alternating-primitive-models'],
    actual_file_scope='Entire saved statement, every proof paragraph and scope remark, the complete alternating_automorphism_source_verification_C.txt note and full new bibliography entry read.',
    certificate_scope='Complete proof and primary-source verification; no finite numerical certificate.',
    checks=[
        'The alternating automorphism input is verified with its exact exception. For an order-three element of type3^a, equality with the centralizer of one3-cycle gives the recorded factorial equation; its only nontrivial equality is a=2,m=6. The a>=3 induction is strict.',
        'The orientation-independent generated subgroup orders3,9,12,60 distinguish equal supports and overlaps0,2,1. The A4 case follows from transitivity and order divisibility; in A5, orders15 and30 are excluded exactly as stated. This repairs the incorrect overlap sentence in the source.',
        'Consecutive3-cycle generators recover point stabilizers. Once an adjusted automorphism fixes every stabilizer, conjugation equivariance and the faithful action on those stabilizers force it to be the identity. This avoids an unverified induction base.',
        'For m!=6, the S_m permutation model has dimension m; for A6 the action of Aut(A6) on its360 elements is faithful. The displayed constant64 and d_m<=64 log|A_m| are valid.',
        'Using the full center-free nonabelian socle gives trivial normal centralizer. The block-permutation realization of its actual automorphism group has dimension at most c log|G|, without a semisimplicity assumption.',
        'The exact Maroti trichotomy gives the polylogarithmic-dimension small-order branch, fixed Mathieu exceptions, and alternating subset/product actions. The k=ell=1 product case is precisely the excluded natural A_N/S_N action.',
        'Each standard product ambient group has two faithful actions: its degree-N subset-product action and its rank-m ell block-permutation matrix action. They need not have the same conjugacy relations, and the proof does not identify them.',
        'For k>=2, Q>=2m^2/5 and ell^2<=Q^(ell-1), giving rank squared<=5N/2. For k=1,ell>=2, the stated induction gives rank squared<=4N. At most N^3 parameter triples occur. These are proofs for all integers, not extrapolated numerical checks.',
        'The prior intrinsic subgroup/stabilizer catalogue supplies actual degree-N permutation models with logarithmic size O(log^8(N+1)). Its matrix cost O(log^4(N+1)), plus the product models, meets the required O(N log(N+1)) bounds after one fixed enlargement of the constant.',
        'Insertion into the checked hereditary wreath criterion is in the finite-puncture scope. It leaves natural alternating/symmetric actions and uncovered cross-characteristic or affine families outside the claim. No modular permutation-module uniqueness or new original-divisorial hereditary assertion is used.'
    ],
    fresh_primary_reads=[
        dict(url='https://sites.math.rutgers.edu/~lyons/math555/nnotes.pdf', locator='Printed pp42-44: Theorem11.2; Lemmas11.3-11.6; full written Theorem11.7 proof.', scope='All relevant written arguments read. The source leaves11.4 as an exercise and has an inaccurate overlap sentence; root independently verified the retained repair. No A6 outer-automorphism description is used.'),
        dict(url='https://sites.math.rutgers.edu/~lyons/', locator='Official Richard Lyons homepage.', scope='Author identity checked.'),
        dict(url='https://www.renyi.hu/~maroti/primitive.pdf', locator='Theorem1.1, author p2, and complete written Section2, pp4-8.', scope='Full written proof read; recursively cited CFSG/O Nan-Scott, minimal-degree theorems, tables and omitted numerical checks remain Known. Only the trichotomy is used here.')
    ],
    source_note='Exact earlier intrinsic-catalogue, automorphism-model and hereditary-wreath proof audits are reused; no new opening of every recursive source is claimed.',
    mathematical_corrections=[],
    movement_scope='Recognition inside the same enlarged tower criterion. It is not an additional independent movement and closes no requested row.'
)
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(path=str(out.relative_to(root)), sha256=sha, verdict='PASS')))
