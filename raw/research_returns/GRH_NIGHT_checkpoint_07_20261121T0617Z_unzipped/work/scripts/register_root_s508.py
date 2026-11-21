from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
now = datetime.now(timezone.utc).isoformat()
rows = json.loads((root / 'rows.json').read_text())
assert not any(r['id'] == 'MT-S508' for r in rows)
with (root / 'section.tex').open('a') as f:
    f.write('\n' + (root / 's5_single_hecke_gate.tex').read_text())
rows.append(dict(
    id='MT-S508',
    statement='In the Calegari S5 family, let B be the single quadratic Hecke factor over the degree-six F20 field, C the rational quadratic factor, and A the specified cuspidal GL5 comparison. Assuming only B has no off-centre real zeros in(0,1), their central orders satisfy beta>=b+n. Equality, equivalently beta<=b+n, is equivalent to a finite exceptional set and exact all-place transfer of both rank-five factors. Thus the remaining comparison gate is the positive central excess beta-b-n.',
    input='One additional conditional real-zero assertion R_B for a single quadratic Hecke function; universal Masullo M_H is sufficient but stronger. Classical Calegari local hypotheses and constructed comparison retained. No Alpoge input needed for the central-order/automorphy theorem; A_D+R_B gives the real-axis Artin holomorphy corollary.',
    status='proved here relative to the exact classical comparison; complete author/root proof readings and source checks. Full GRH for B plus equality gives GRH for C and W; other factors need their separate zero-location inputs. No universal Artin holomorphy or Hecke GRH is proved.',
    where_the_proof_is='GRH_NIGHT.tex MT-S508; work/root/s5_single_hecke_gate.tex; Calegari publisher PDF Theorem4.7p12,Lemma4.8pp13-14,LandauLemma4.9p14,Lemma4.10pp14-15,finalTheorem1.2proofp15',
    where_it_lives='Q-S5-CENTRE; Q-S5-SINGLE-HECKE; Q-ARTIN-POS; MT-S504/505/507; exact central divisor of the degree-six quadratic pushforward eta+W compared with the specified automorphic rank-five numerator'
))
(root / 'rows.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([
            sid, now, '/root', 'GPT-6 Astra Pro', 'not exposed',
            'GRH_NIGHT_20261121', kind, outcome])

event(root / 'events.tsv', 'MT-S508', 'targeted proof check',
      'Read the whole written proof and all corollaries. Checked H/F quadratic, all-prime B=C*L_W, actual completed quotient orientation, exact gamma factors/signature, beta-b-n order, both infinite/finite exceptional-set branches, twist comparison without a second Hecke input, real-axis corollary and separate GRH scopes. Root freshly read publisher Lemmas4.8-4.10 and the full final comparison proof; author independently inspected original pp13-15 images. No gap found. Finite bad-prime reciprocal mismatch is explicitly corrected rather than imported.')
event(base / 'work/checks/source_events.tsv', 'CALEGARI13', 'used and rechecked in this run',
      'Root freshly opened the primary publisher-author PDF and read the complete relevant text of Lemma4.8, LandauLemma4.9 including exclusion of abscissa0, Lemma4.10 including ramified-twist local comparison, and finalTheorem1.2proof on pp13-15. This supports the precise single-Hecke transfer. The earlier automorphic construction is a cited classical input, not re-proved. Author original-image inspection verifies the finite polynomial reciprocal typo and corrected actual quotient.')
sources = json.loads((root / 'sources.json').read_text())
for s in sources:
    if s['id'] == 'CALEGARI13':
        s['locator'] += '; MT-S508 uses publisher Theorem4.7p12,Lemma4.8pp13-14,LandauLemma4.9p14,Lemma4.10pp14-15 and finalTheorem1.2proofp15'
        s['web_refs'] += ['turn863683406view0', 'turn863683406view1', 'turn863683406view2']
        s['inspection'] += ' Root read the full publisher comparison/Landau/final proofs for MT-S508. The finite bad-prime polynomial ratio on p13 is corrected using the explicitly defined completed quotient; its real-interval nonvanishing is unchanged.'
(root / 'sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n')

path = root / 'questions.tsv'
with path.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t')
    fields, qs = rd.fieldnames, list(rd)
for q in qs:
    if q['id'] == 'Q-S5-CENTRE':
        q['state'] = ('proved sharper exact comparison criterion MT-S508: only R_B, the no-off-centre-real-zero condition for the single degree-six quadratic Hecke factor B, is needed. For beta=ord B, b=ord L_eta and n=ord of the specified known cuspidal GL5 numerator at1/2, beta>=b+n; equality (equivalently beta<=b+n) holds iff the exceptional set is finite iff both rank-five factors match at every place. The remaining gate is beta-b-n>=1. Universal M supplies R_B but is stronger; A_D is unnecessary for this comparison theorem. MT-S504 is the n-discarding sufficient special case. No claim that failure of this specified comparison criterion rules out every possible automorphic realization.')
    if q['id'] == 'Q-ARTIN-POS':
        q['state'] += ' MT-S508 weakens the real-axis exclusion input to A_D plus the single quadratic-Hecke real-zero condition R_B and refines the specified automorphic comparison gate to the excess beta-b-n, retaining central zeros of the known numerator.'
qs.append(dict(
    id='Q-S5-SINGLE-HECKE',
    source_and_locator='MT-S504/505; Calegari publisher Lemmas4.8-4.10pp13-15 and finalTheorem1.2proofp15',
    question='Which individual Hecke input suffices for the S5 comparison, and can zeros of the automorphic numerator be retained in its central gate?',
    state='proved MT-S508: R_B for one quadratic Hecke factor over the degree-six F20 field suffices; beta>=b+n and equality is exactly the all-place comparison condition. The quadratic twist needs no second Hecke input. A_D+R_B gives real-axis holomorphy; full GRH_B plus equality locates zeros of C and W only. Other zero-location inputs remain separate.'
))
with path.open('w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    wr.writeheader()
    wr.writerows(qs)
with (root / 'implications.md').open('a') as f:
    f.write('\n## A single Hecke function and the automorphic central excess\n\nMT-S508 reduces the analytic input for the specified Calegari comparison to the real zeros of one quadratic Hecke L-function over a degree-six field. It retains the known GL5 numerator order n: beta>=b+n, and equality is equivalent to exact transfer of both rank-five factors. The remaining central excess is beta-b-n, replacing the earlier sufficient test beta<=b. A_D+this single real-zero input also replaces universal M in the real-axis holomorphy consequence. Full zero-location conclusions for the remaining factors remain separate.\n')
with (root / 'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — one-Hecke S5 comparison criterion\n\nMT-S508 passed entire author and root proof readings with the exact publisher comparison proofs rechecked. The analytic family and central-order gate both shrink; the conditional status and local hypotheses remain explicit.\n')
print(json.dumps(dict(date=now, root_rows=len(rows), added=['MT-S508'])))
