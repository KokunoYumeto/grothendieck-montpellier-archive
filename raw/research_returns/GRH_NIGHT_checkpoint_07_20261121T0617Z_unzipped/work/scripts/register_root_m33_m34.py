from pathlib import Path
from datetime import datetime, timezone
import csv
import json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] in {'MT-M33', 'MT-M34'} for r in rows)
with (root / 'section.tex').open('a') as f:
    for name in ['narrow_euler_invertibility.tex', 'cutoff_strictness_obstruction.tex']:
        f.write('\n' + (root / name).read_text())
rows.extend([
    dict(id='MT-M33', statement='Every centered finite Euler translation product is a bounded automorphism of the actual weighted strip space whenever its Euler zero line is separated from that strip. Its theta-image quotient is then zero. The nonzero zero-line local circle module, with the precise norm twist, has no nonzero bounded translation intertwiner in either direction with a closed invariant subquotient of that strip space.', input='neither; explicit operator-norm Neumann series, actual Masullo norms and centering, MT-M31/M32 local quotient. The full compact-group version also requires compact-translation invariance.', status='proved here; excludes a bounded module-identification route for every centered width alpha<1/2, including zero width. Does not exclude a separately justified non-equivariant cutoff construction.', where_the_proof_is='GRH_NIGHT.tex MT-M33; work/root/narrow_euler_invertibility.tex; source norm9.2.2.31original416, completion10.1.1.3original434; transition11.1.2.1p480/11.2.2.1pp489–491/11.3.2.1pp495–496', where_it_lives='Q-MAS-GEOMETRIC-NARROW; local Euler module to narrow global trace comparison in cote1scans79–80/111–112 and MasulloCh11; exact compact-invariance and norm-twist conventions retained'),
    dict(id='MT-M34', statement='A genuine one-prime closed Euler condition disappears under every finite positive or two-sided radial cutoff: the actual cutoff images of the proper quotient kernel and full space are equal. The exact least lift norm grows as (log Lambda)^((s−1)/2), with distinct explicit one-tail and two-tail constants. This gives a counterexample to Masullo11.1.2.1(2) in its actual rational theta completion, even after the MT-M31 closure repair.', input='neither; explicit weighted periodization and minimum-norm lift; MT-M24/M25 unconditional actual theta density and MT-M31/M32 exact local closure; original PDF428/480/482 visually checked', status='proved here: literal cutoff-strictness assertion refuted. Strong convergence requires an additional bounded-lift hypothesis, which is proved sufficient and shown quantitatively false here. M_H remains a separate conditional endpoint.', where_the_proof_is='GRH_NIGHT.tex MT-M34; work/root/cutoff_strictness_obstruction.tex; originalMasullo9.3.3.3p428,11.1.2.1(2)p480 and proof after11.1.2.16p482', where_it_lives='Q-MAS-CUTOFF-STRICTNESS and Q-MAS-GEOMETRIC-NARROW; local closed-point quotient versus finite-cutoff images in cote1scans79–80/111–112; precise downstream11.3.2.1pp495–496 and12.5.1.1p520 dependency')
])
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed', 'GRH_NIGHT_20261121', kind, outcome])

event(root / 'events.tsv', 'MT-M33', 'targeted proof check', 'Read the whole proof after drafting, including both inverse series, weighted translation bound, exact T_a and V_y signs, actual theta closure, quotient polynomial and both intertwiner directions. Clarified fixed-character scope and the full compact extension with compact-translation invariance. No gap found; geometric-cutoff route remains separate.')
event(root / 'events.tsv', 'MT-M34', 'targeted proof check', 'Read the complete new proof after drafting and directly viewed original PDF428/480/482. Checked actual image equality using an outside period lift, density through bounded cutoffs, exact fiberwise minimum, uniform lattice-tail asymptotic and both constants, bounded-lift criterion, Q/trivial-character specialization, theorem hypotheses, and exact strictness refutation. No gap found. Earlier actual theta-density proofs remain explicit antecedents; no audit of the rest of the draft claimed.')
event(root / 'events.tsv', 'Masullo11.1.2.1(2)', "refuted, with the refined statement's id", 'Original definitions428, theorem480 and proof482 visually read. MT-M34 gives equality for every finite positive/two-sided cutoff in an actual Q theta sector satisfying all theorem hypotheses, while the uncut inclusion is strict. Strong convergence does not provide bounded lifts; exact divergent correction norm is proved. This is not a refutation of M_H.')
event(base / 'work/checks/source_events.tsv', 'Masullo9.3.3.3/11.1.2.1', 'used and rechecked in this run', 'Root visually read original PDF428/480/482 in full for the relevant definitions, every strictness hypothesis, cutoff-space closure convention, and inference after11.1.2.16. Source-definition images retained as evidence. Targeted source reading only.')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields = rd.fieldnames
    qs = list(rd)
for q in qs:
    if q['id'] == 'Q-MAS-GEOMETRIC-NARROW':
        q['state'] += ' MT-M33 rules out nonzero bounded centered-module intertwiners into narrow closed invariant subquotients. MT-M34 refutes the literal finite-cutoff strictness used by11.3.2.1, even after closure repair: actual cutoff images are equal and their required lifts diverge at an exact rate. A replacement geometric-kernel/cutoff-limit construction is therefore required, rather than the source strong-convergence inference.'
qs.extend([
    dict(id='Q-MAS-NARROW-EULER-TRANSPORT', source_locator='Masullo11.1.2.1p480;11.2.2.1pp489–491;11.3.2.1pp495–496; norms416/434', question='Can the centered nonzero local Euler circle quotient be identified by a bounded translation module map with a narrow closed invariant Hilbert subquotient?', state='refuted MT-M33 for every strip separated from the centered Euler zero line: the target Euler product is invertible, while the source centered module is annihilated by it. Both intertwiner directions vanish. A non-equivariant geometric cutoff construction remains a separate route.'),
    dict(id='Q-MAS-CUTOFF-STRICTNESS', source_locator='Masullo11.1.2.1(2)original480; proofafter11.1.2.16original482; cutoff9.3.3.3original428', question='Does the strict uncut local Euler inclusion remain strict along a subsequence of finite positive/two-sided cutoffs under all source hypotheses?', state='refuted MT-M34 in the actual Q trivial-character sector with S={infinity}, empty and one-prime index sets, s≥2. Both cutoff closures are equal for every Lambda>1. Exact minimum lift norms diverge with proved one-/two-tail constants; a bounded-lift condition, absent here, would justify the strong-limit inference.')
])
# Preserve the established four-column question schema.
for q in qs:
    if 'source_locator' in q and 'source_locator' not in fields:
        source_field = next(k for k in fields if k not in {'id', 'question', 'state'})
        q[source_field] = q.pop('source_locator')
with path.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(qs)

with (root / 'implications.md').open('a') as f:
    f.write('\n## Local quotients and finite radial cutoffs\n\nMT-M33 proves that a separated centered strip inverts every finite local Euler operator. The corrected zero-line circle module therefore cannot enter that strip as a nonzero bounded invariant subquotient with the required centered action. MT-M34 then checks the actual alternative used in the draft: finite positive and two-sided cutoffs erase the one-prime quotient condition completely. Its counterexample satisfies every hypothesis of11.1.2.1(2), checked against original PDF428/480/482. The escaping correction has an explicit diverging norm, identifying why strong convergence alone fails.\n\nFor cote1scans79–80/111–112, the repaired local Poisson trace remains available, but the draft’s passage from that quotient to a geometric global trace needs a replacement cutoff-limit argument. These results refute specific intermediate claims; the Hecke-GRH statement remains the designated conditional hypothesis for catalogue deductions.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — bounded local transport excluded; cutoff strictness refuted\n\nMT-M33 and MT-M34 received complete root readings. The original cutoff definitions and full strictness theorem hypotheses were directly inspected in images428/480/482. The corrected local quotient survives, but every finite source cutoff has equal images in the rational example. The exact lift norm supplies the missing quantitative condition. No assertion about the truth or falsity of M_H is made.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added=['MT-M33', 'MT-M34'])))
