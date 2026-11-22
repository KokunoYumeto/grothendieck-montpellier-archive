from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] == 'MT-M35' for r in rows)
with (root / 'section.tex').open('a') as f:
    f.write('\n' + (root / 'finite_euler_cutoff_collapse.tex').read_text())
rows.append(dict(id='MT-M35', statement='For every nonzero finite translation polynomial, multiplying its range by any bounded cutoff supported in a half-line gives the full cutoff image after closure. In the actual rational zero-line theta sector, every finite-prime cutoff stage and their cofinal intersection is the full cutoff space, while the uncut cofinal intersection is zero. The literal Schwartz-image identification in Masullo11.1.2.1(3) is also full in this example and is not separately refuted.', input='neither; exact endpoint propagation for finite difference equations, bilinear weighted duality, continuous Fourier transforms for s>1, and MT-M24/M25 unconditional actual theta density', status='proved here: finite-product closed cutoff-image collapse and exact failure of cutoff/prime-exhaustion interchange. Actual image surjectivity is asserted only in MT-M34’s one-factor case.', where_the_proof_is='GRH_NIGHT.tex MT-M35; work/root/finite_euler_cutoff_collapse.tex; originalMasullo11.1.2.1(1)–(3)/11.1.2.3–7p480 and cutoffs9.3.3.3p428', where_it_lives='Q-MAS-GEOMETRIC-NARROW and Q-MAS-CARVING-INTERCHANGE; exact local Euler quotient/finite radial cutoff distinction for cote1scans79–80/111–112; downstream geometric-kernel comparison remains separate'))
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')

def event(path, sid, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed', 'GRH_NIGHT_20261121', 'targeted proof check', outcome])

event(root / 'events.tsv', 'MT-M35', 'Read the entire proof after drafting. Checked combined-shift endpoint propagation in both directions, null-set handling, bilinear transpose without conjugation, equality of annihilators and closures, actual theta-density transfer, nonzero Euler endpoint coefficients, nested cofinal stages, L1/Fourier continuity and dense frequency grids, Fourier uniqueness, and exact part(3) Schwartz image with the below-cutoff integral repair. No gap found. General finite-product statement is closure equality only; literal part(3) is not refuted.')
event(base / 'work/checks/root_peer_reviews.tsv', 'AG-FROB-Z', 'Read complete new proof. Checked prime-modulus Dirichlet input scope and exact cited Bach–Sorenson5.3 bound, congruent Frobenius eigenvalues, integral product-cycle comparison, separate coefficient/base finite sets and p>ell argument. No gap found. Numerical constant retained as a located classical theorem, not a root rerun of its computation.')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t'); fields=rd.fieldnames; qs=list(rd)
for q in qs:
    if q['id'] == 'Q-MAS-GEOMETRIC-NARROW':
        q['state'] += ' MT-M35 proves collapse for every finite Euler product after cutoff and full cutoff cofinal intersection versus zero uncut intersection in the actual rational sector; an interchange of these constructions cannot supply the needed comparison.'
qs.append(dict(id='Q-MAS-CARVING-INTERCHANGE', source_and_locator='Masullo11.1.2.1(1)–(3)/11.1.2.3–7original480; MT-M34', question='Do closed finite radial cutoffs preserve the cofinal prime-Euler intersection and its nontrivial quotient structure?', state='refuted as an interchange principle by MT-M35 in the actual Q theta sector for s>1: every finite-cutoff stage and its cofinal intersection is full cutoff space, while the uncut cofinal intersection is zero. The source’s separate part(3) Schwartz-image closure is also full in this example, so that assertion is not separately refuted.'))
with path.open('w', newline='') as f:
    wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows(qs)
with (root / 'implications.md').open('a') as f:
    f.write('\nMT-M35 extends the cutoff diagnosis to every finite Euler product, without commensurability of logarithms: endpoint propagation makes the closed cutoff image full. In the actual rational theta model, exhausting all primes before cutoff leaves zero, while taking each finite cutoff closure first leaves the full cutoff space. The source’s part(3) Schwartz image agrees with the latter and is not an additional counterexample. For cote1scans79–80/111–112 the unresolved comparison must respect this distinction between closures and limiting operators.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — finite-product cutoff closure and cofinal limits\n\nMT-M35 passed a full root reading. It proves all finite-product cutoff closures full and the uncut cofinal intersection zero in the actual Q sector. The original part(3) comparison was checked constructively and remains consistent in this example. AG-FROB-Z received a full root proof reading; its classical explicit prime constant is not independently recomputed.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added=['MT-M35'])))
