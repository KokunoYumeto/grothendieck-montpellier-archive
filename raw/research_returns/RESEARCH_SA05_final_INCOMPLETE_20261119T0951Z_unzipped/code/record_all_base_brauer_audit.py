"""Record the completed arbitrary-base Brauer proof audit and its actual scope."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
events = [
 ('lem:B-unit-cup-generation',
  'Root read the full proof. For an open of a smooth projective variety, boundary divisor relations are rational units because Pic0(Fbarp) is torsion; unit Kummer classes split the weight-zero quotient. The remaining H1 has weight−1. Proper alteration trace and norm descend the assertion. Root opened Riou Corollary3.1.2, Proposition2.5.13 and the full degree proof in Lemmas3.5.8–10; the initial lemma is restricted to quasi-projective T to retain the source ample hypotheses. The arithmetic cup map fills the Hochschild–Serre term and, under surface Tate, VellBr; finite cotype gives a finite cokernel.'),
 ('lem:B-unit-cup-kernel',
  'Root read the complete valuation proof and independently opened Colliot–Thelene–Skorobogatov2019 section1.4.1, Proposition1.4.5 and the following residue formula, author p37. That proposition refers its proof elsewhere; the exact statement and cup-residue formula were read. Normal projective models of the generic fields give a finite full-rank valuation matrix on the unit lattice. Residue-field constant degrees multiply its rows without changing rank. Smith form bounds the cup kernel, including singular, nonreduced and nonseparated bases.'),
 ('thm:B-all-bases-Brauer-units',
  'Root independently derived the uniform finite-error algebra and then read D’s full written theorem. A finite affine cover followed by projective alterations gives a finite-type h-cover with quasi-projective smooth terms; the etale-to-v degree-two injection and Jaffe bound its kernel. Rational unit equalizer descent has only a finite Smith-form defect on Qell/Zell. Uniform N,M,L give LMN a minus an actual base unit cup in the finitely generated kernel. The quotient A/C maps with finitely generated kernel and finite image into a finite-cotype quotient, hence is finitely generated. Its torsion is Br[ell-infinity]/C, which is finite. The converse is the proper-surface Kummer criterion. No nonproper H2 torsion-free saturation hypothesis remains.'),
 ('cor:B-all-bases-relative-Brauer',
  'Root checked the direct unit argument: equal global units give f*C_S=C_X, so the relative ell-Brauer cokernel is a quotient of finite Br(X)[ell-infinity]/C_X. Root opened and read Stacks36.32.5–6, tag0E0L, including the derived-base-change proof over arbitrary bases; proper flat finitely presented morphisms with geometrically reduced connected fibres have f_*O=O universally. The curve-family converse is the already audited pencil reduction. This avoids replacing full H2(Gm) by torsion in Leray.'),
]
path = ROOT / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
added = 0
for identifier, outcome in events:
    if not any(row['statement_id'] == identifier and row['outcome'] == outcome for row in rows):
        rows.append(dict(statement_id=identifier, date=now,
                         who='GPT-6 Astra / root / current run',
                         type='targeted proof check', outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

heading = '## Arbitrary-base Brauer saturation removed'
entry = '''

## Arbitrary-base Brauer saturation removed

The separate singular, nonproper base-image gate in B.3 is now removed. Under divisor Tate for all smooth projective surfaces over finite extensions of F_p, arithmetic character cups with global units generate Br′(S)[ell-infinity] up to a finite group for every finite-type F_p-scheme S, with ell≠p. More precisely, full H2_et(S,Gm) tensor Z_(ell), modulo the divisible unit-cup image, is finitely generated. The proof uses a finite-type h-cover by smooth quasi-projective alteration opens, the degree-two perfection/v-descent injection, a finite valuation-matrix bound on the cup kernel, and a uniform finite-error unit equalizer. It neither assumes full H2 is torsion nor discards the arithmetic contribution on an open base.

For any morphism identifying global units, the relative ell-primary Brauer cokernel is consequently finite. This includes every smooth proper curve family with geometrically connected fibres over every finite-type base, including singular, nonreduced and nonseparated ones. The converse follows from the earlier pencil family. Thus both universal prime-to-p questions in B.3 now have exactly the surface-Tate gate, equivalently the already proved single H3(F0 P3_Fbarp,Qell(2)) invariant gate. The conjecture itself remains unresolved. The literal unrestricted full-Brauer assertion remains refuted by the explicit characteristic-two family.

This is a substantive removal of the remaining base-image obstruction after formal review01. The intermediate proper-base theorem and integral torsor-lattice theorem remain valid and are retained as separately scoped results. The root, B and D checks are recorded individually; the source record distinguishes statements opened from complete proofs read. No novelty or priority is claimed.
'''
for filename in ['PROGRESS_LEDGER.md', 'RESEARCH_SA05_report.md']:
    path = ROOT / filename
    if heading not in path.read_text():
        path.write_text(path.read_text() + entry)
result = {'recorded_at': now, 'root_events': len(rows), 'new_events': added,
          'formal_review': False, 'seconds': round(time.monotonic() - started, 6)}
(ROOT / 'code/record_all_base_brauer_audit_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
