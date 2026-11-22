"""Reconcile the root report with the checked all-field B.2 weak theorem."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assembler = root / 'code/assemble.py'
s = assembler.read_text()
s = s.replace(
    'h1 boundedness proved for every field; constant domination-cofinal Picard diagram refuted over an imperfect field, so the asserted equivalence is false; weak upper-cone replacement separately tracked',
    'h1 boundedness and weak upper-cone stabilization proved over every field; constant domination-cofinal Picard diagram refuted over an imperfect field')
s = s.replace(
    'B.2; B.2h; B.2i; B.2q; B:B2-cofinal-counterexample; B.2o; B.2-U',
    'B.2; B.2u; B:B2-arbitrary-field-stabilization; B.2t; B.2r; B.2q; B:B2-cofinal-counterexample; B.2i')
old = 'B.2: full scheme-theoretic Picard stabilization over perfect fields is proved, and a stable upper cone exists after one finite purely inseparable constant extension. Weak upper-cone stabilization is now also proved over the original arbitrary field in dimensions at most two, using a maximal finite-length higher-direct-image sheaf and Lipman numerical descent. Thus its remaining image-realization gate has dimension at least three over an imperfect field. A fixed alteration over finite constants bounds all pullback kernels. The stronger constant cofinal diagram is now refuted by an explicit threefold with two nonisogenous elliptic Picard branches (B.2q). Thus the literal requested boundedness/cofinal-constancy pair is decided, and its claimed equivalence fails. The weak upper-cone statement is an additional replacement introduced in this analysis; it remains explicitly tracked and is not silently counted as solved.'
new = 'B.2 is now fully decided in all three tracked formulations. Uniform h1 boundedness and weak upper-cone stabilization hold over every field and in every dimension. A fixed Galois alteration with explicit semilinear finite constants realizes invariant abelian subgroups by rational torsor maps; bad-divisor restriction kernels remove excessive abelian directions, and a degree-times-exponent bound controls the remaining finite quotient. The complete argument and its full Picard-sheaf comparison received independent actual-file audits. The stronger constant domination-cofinal diagram remains refuted by the explicit threefold B.2q. Thus the asserted equivalence with that stronger formulation is false, while the weak replacement is proved. No B.2 gate remains open.'
assert old in s
s = s.replace(old, new)
s = s.replace(
    'A:A2-all-surface-models; A:strict-model-rigidity\',\'31/085',
    'A:A2-all-surface-models; A:strict-model-rigidity; A:A2-topnormal-models\',\'31/085')
assembler.write_text(s)

ledger = root / 'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text() + '\n\n## Working update: '
    + now.strftime('%Y-%m-%d %H:%M UTC')
    + ' (after formal review02)\n\n'
    'B.2-U is now closed. The full arbitrary-field weak upper-cone theorem '
    'B.2u was integrated by PartB at04:11:20 UTC after the final targeted '
    'actual-file audit. Root and PartC checked the complete proof, and '
    'PartD separately checked its valuation, restriction and finite-quotient '
    'steps. The auxiliary semilinear Galois-alteration realization, full '
    'finite-constants Picard-sheaf comparison, and no-torus/bounded-exponent '
    'lemmas are all written and checked. The stronger cofinal constant '
    'diagram remains refuted; the weak theorem does not claim cofinality. '
    'Formal review02 accurately recorded the final audit as still underway '
    'at04:10:05. The next scheduled review remains05:10 UTC. Only A.2 and '
    'D.1/D.2(ii), with their L8 dependency, remain requested open work.\n')

report = root / 'report_supplement.md'
with report.open('a') as f:
    f.write('\n\n## All-field closure of the weak Picard stabilization assertion\n\n'
        'B.2r–u supply the complete scheme-theoretic upper-cone theorem in '
        'arbitrary dimension over every characteristic-p field. The proof '
        'retains all finite alteration constants, their semilinear group '
        'action, purely inseparable descent, arbitrary parameter schemes, '
        'and the distinction between a fixed abelian subgroup of Pic(X) '
        'and its isogenous image in the comparison group. The full written '
        'proof has root, PartC and targeted PartD audits; sources were '
        'opened at their exact locators. The strong cofinal counterexample '
        'B.2q is unaffected. No B.2 statement remains undecided.\n')
print(json.dumps({'utc': now.isoformat(), 'closed': 'B.2-U',
    'remaining_requested': ['A.2', 'D.1', 'D.2(ii)', 'L8 residual']}))
