from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(x['id'] in {'MT-M30', 'MT-S504'} for x in rows)
with (root / 'section.tex').open('a') as f:
    for name in ['idele_restriction_splitting.tex', 's5_relative_central_gate.tex']:
        f.write('\n' + (root / name).read_text())
rows.extend([
    dict(id='MT-M30', statement='Unconditionally, restriction of the exponential-Schwartz idele-class space to norm-one ideles has a continuous compact-equivariant right inverse valued in the closed centered theta ideal. Its kernel quotient is the full arithmetic quotient. Restricted compact tests detect every omitted spectral zero or lowered multiplicity; full-versus-strip trace equality on these tests is equivalent to retaining the full zero divisor.', input='neither; classical Hecke continuation and functional equation, unconditional uniform conductor/gamma/Jensen estimates of MT-M28, and actual full-jet kernel identity MT-M24/M27; A or M only for subsequent positivity on convolution squares', status='proved here; removes the restricted-test-domain gate. The projection need not preserve positivity or compact support; independent geometric narrow-strip equality remains unproved.', where_the_proof_is='GRH_NIGHT.tex MT-M30; work/root/idele_restriction_splitting.tex; Meyer2005 Theorem5.8 authorpp43–44 and Theorem5.11p47; Masullo§1.4.6p30/§1.7.2pp34–35/Thm12.5.1.1pp519–520 original images inspected by author', where_it_lives='CX-Q46/Q-MAS-GEOMETRIC-NARROW; actual arithmetic quotient comparison in cote1scans79–80/111–112 and SA23geo-H-lidskii; geometric equality remains the exact zero-location gate'),
    dict(id='MT-S504', statement='In Calegari’s specified S5 family, M_H plus ord_1/2 ζ_H≤ord_1/2 ζ_F+ord_1/2 Lη implies full Artin automorphy, holomorphy and GRH. The inequality then becomes equality. The unresolved sufficient-condition gate is a positive even relative central order m5≥2, allowing arbitrary base-factor central zeros.', input='Masullo (conditional), the local hypotheses of MT-S501, Calegari2013 Theorem1.1/Lemmas4.8–4.9, and the displayed relative central-order condition; Fröhlich–Queyrut only for the even-order refinement', status='proved here: strictly sharper sufficient gate than MT-S502. Positive central order is not asserted to prevent automorphy; it leaves this route unsettled.', where_the_proof_is='GRH_NIGHT.tex MT-S504; work/root/s5_relative_central_gate.tex; Calegari arXiv:1112.1152v1 comment after Theorem1.2p2, Lemmas4.8–4.9pp10–11 and final Theorem1.2 proofp11', where_it_lives='Q-S5-CENTRE and S5 branch of Q-ARTIN-POS; isolates the rank-five Artin motive by the finite-cover permutation identity; cote1/SGA5 trace-divisor programme')
])
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed', 'GRH_NIGHT_20261121', kind, outcome])
event(root / 'events.tsv', 'MT-M30', 'targeted proof check', 'Read the whole proof, including every uniform estimate, quotient/topology argument and final trace criterion. Checked quarter-integer gamma-ratio bounds and principal pole removal, Mellin normalization at2−a, logarithmic tail split and polynomial L2 lower bound, first-factor ideal membership without an involution assumption, character summation and compatible levels, cutoff density, continuous quotient functional extension, isolation of omitted full-jet blocks and polar-term sign. No gap found. Closed-ideal membership only; support/positivity preservation not claimed.')
event(root / 'events.tsv', 'MT-S504', 'targeted proof check', 'Read the whole new proof after drafting. Checked all-prime permutation factorization, signed meromorphic central orders, Brauer/M off-centre nonvanishing, finite nonzero gamma factors on(0,1), impossibility of a comparison pole when m5≤0, Calegari finite-exception exact-match conclusion for both twists, all irreducible dimensions, post-holomorphy equality and real-representation parity. No gap found. Failure of the sufficient condition is not an obstruction to automorphy.')
event(base / 'work/checks/source_events.tsv', 'CALEGARI13', 'used and rechecked in this run', 'Fresh arXiv:1112.1152v1 read: Theorems1.1–1.2 and exact p2 comment, character tablep3, and full Lemma4.8/Lemma4.9/final Theorem1.2 proofspp10–11. The comparison ratio and finite local correction are checked. Earlier automorphic construction remains a cited classical input, not a fresh full-paper audit.')

sources = json.loads((root / 'sources.json').read_text())
for s in sources:
    if s['id'] == 'CALEGARI13':
        s['locator'] += '; MT-S504 additionally uses arXiv:1112.1152v1 comment after Theorem1.2p2, Lemmas4.8–4.9pp10–11, final Theorem1.2 proofp11'
        s['inspection'] += ' Root freshly read those exact v1 statements and the full final three proofs; initial automorphic construction retains classical credit.'
        s.setdefault('web_refs', []).extend(['turn172573709view0', 'turn705239082view0', 'turn545647806view0'])
(root / 'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2)+'\n')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; qs=list(reader)
for q in qs:
    if q['id']=='Q-S5-CENTRE':
        q['state']='proved sharper reduction MT-S504: M plus m5=ord ζ_H−ord ζ_F−ord Lη≤0 forces automorphy and m5=0. This removes every base-factor central zero from the earlier ζ_H(1/2)≠0 test. Only m5≥2 even leaves this sufficient route unsettled; it does not preclude automorphy.'
    elif q['id']=='Q-ARTIN-POS':
        q['state'] += ' The specified S5 branch now has the strictly smaller MT-S504 relative central-order gate m5≥2; central zeros inherited from ζ_F or Lη no longer obstruct this sufficient route.'
    elif q['id']=='Q-MAS-GEOMETRIC-NARROW':
        q['state']='current exact gate after MT-M30: prove the source’s geometric equality to every narrow-strip trace on compact tests vanishing at norm one independently of zero location. MT-M30 unconditionally splits that test restriction through the closed theta ideal and proves any omitted zero has such a compact witness; thus no restricted-test-domain or positivity-test admissibility obstruction remains. MT-M27 is unconditional wide-strip trace, MT-M28 is narrow trace under M, MT-M29 is the conditional graded determinant comparison. None supplies the independent geometric equality.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(qs)
with (root / 'implications.md').open('a') as f:
    f.write('\n## Restricted tests and the exact S5 relative factor\n\nMT-M30 removes the norm-one restriction from the arithmetic quotient comparison unconditionally: every class has a representative vanishing on norm-one ideles, and compact such tests detect every missing spectral contribution. This does not establish the draft’s geometric trace identity; it identifies that equality as the remaining exact zero-location gate. No positivity or support preservation is asserted for the projection.\n\nMT-S504 replaces the S5 condition ζ_H(1/2)≠0 by the weaker relative-order inequality ord ζ_H≤ord ζ_F+ord Lη. Thus central zeros from the two other factors no longer count against this route. Under M the inequality gives all Artin automorphy and then becomes equality; a remaining positive even rank-five order is an unresolved sufficient-condition gate, not a counterexample to automorphy.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — restricted-test gate closed; S5 gate reduced\n\nMT-M30 passed a full root proof reading and closes the test-domain comparison unconditionally. MT-S504 passed a complete post-draft reading and strictly reduces Q-S5-CENTRE by subtracting the two known base-factor central orders. Both are registered after checkpoint5. These are actual gate changes for review2, not packaging or row-count movement.\n')
print(json.dumps(dict(date=now,root_rows=len(rows),added=['MT-M30','MT-S504'])))
