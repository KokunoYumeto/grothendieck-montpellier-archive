"""Record completed written checks; this is not a scheduled progress review."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
events = [
 ('lem:B-unit-cup-prime-uniform', 'Root read the complete typeset proof, including the alteration constant-field clarification. Arithmetic H2 of the geometric unit lattice is covered by actual arithmetic unit cups; H1 of the geometric Picard group is finite by the Pic0/Lang and finite Neron–Severi argument. The entire degree-two Hochschild–Serre filtration is used without a degeneration claim. Qin2021 Theorem5.2 supplies one finite geometric prime-to-p group; root read its full proof and its stated intermediate inputs. Integral finite-coefficient Riou traces, including inseparable generic degree and primes dividing the alteration degree, descend to Brauer torsion by generic injectivity. Projection formula and the unit norm give a fixed annihilator; divisibility and finite Kummer cohomology give actual finiteness. Separate ell-primary finiteness is not substituted for the all-prime result.'),
 ('thm:B-Brauer-prime-uniform', 'Root read the complete typeset proof and rechecked the algebra over Z[1/p]. The perfection/v-descent kernel is finitely generated over that ring; one valuation matrix and one unit-lattice equalizer supply finite defects at all primes. The fixed LMN annihilator bounds the image of A_S/C_S. Divisibility of q*C_S makes its h-torsion a quotient of the finite A_T[h], avoiding a false global finite-cotype assertion. The torsion subgroup is exactly Br(S)[p-prime]/C_S. Equal units give the relative conclusion, including every finite-type singular, nonreduced or nonseparated base. Proper surface Kummer and the pencil converse give the exact Tate equivalence.'),
 ('cor:B-torsors-prime-uniform', 'Root read the complete derived-section proof. The zero section splits Rf_*Gm as Gm plus K in degrees at least1; truncation gives an actual injection H1(S,Picrel) into H2(S,K), contained in ker e*. It therefore gives actual torsion Brauer classes, not lifts from a torsion quotient. Inversion is minus one on Pic0 and plus one on the fibrewise Neron–Severi quotient, so the connecting kernel is killed by2. Its prime-to-p part is zero for p=2 and finite by finite-etale Kummer cohomology otherwise. Arbitrary abelian-scheme duality is used, with no global projectivity or local constancy of NS asserted. The previously checked actual torsor Cech kernel argument then upgrades H1(S,A)[1/p] to a finitely generated Z[1/p] module.'),
 ('lem:B-surface-Tate-prime', 'Root read the full proof. Hodge index gives nondegeneracy of the Neron–Severi intersection pairing; averaging preserves it on finite-Galois invariants, and divisor norms give rational descent. If the invariant eigenspace is algebraic, its orthogonal complement has F-1 invertible, so eigenvalue1 has no additional generalized vectors. Independence of the degree-two Frobenius polynomial then yields prime independence and the multiplicity criterion without general Frobenius semisimplicity.'),
 ('thm:B-irregularity-zero-surface-gate', 'Root read the entire written reduction and the full published Yuan2021 preparatory section4.1 and proof section4.2, pp1994–1997, as well as Theorem1.6 p1968. The same finite field is retained: a finite-field Lefschetz pencil gives a Jacobian, Yuan splits its constant part and leaves ample Hodge bundle, the regular model has vanishing H1(O), and finite-field ample cuts yield a surface with the same vanishing whose generic Jacobian contains the required factor. The zero-dimensional factor case is treated separately. The comparison is equality of analytic and algebraic ranks, not the refined leading-coefficient conjecture. This is a proper intrinsic subclass restriction, not a source-variety encoding. Yuan’s cited Nguyen and Kunne­mann–Faltings–Chai inputs are used through his published statements and are not represented as independently opened.'),
 ('rem:B-irregularity-zero-source-scope', 'Root verified the corrected canonical Ertl–Keller–Qin bibliography key and the explicit status label. The source-scope remark separates Kahn–Morrow’s all-dimensional surface reduction from Yuan’s further H1(O)=0 restriction. The original Tate1966 refined BSD formula remains labelled conjectural; de Jong’s unpublished reduction note was not obtained. The remaining restricted Tate condition is explicitly unresolved.'),
]
path = ROOT / 'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
added = 0
for identifier, outcome in events:
    if not any(r['statement_id'] == identifier and r['outcome'] == outcome for r in rows):
        rows.append(dict(statement_id=identifier, date=now,
                         who='GPT-6 Astra / root / current run',
                         type='targeted proof check', outcome=outcome))
        added += 1
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

heading = '## Whole prime-to-p results and the irregularity-zero gate'
entry = '''

## Whole prime-to-p results and the irregularity-zero gate

The complete prime-uniform proofs are now integrated in `sections/b3_prime_uniform.tex`. Under the surface-Tate condition, the prime-to-characteristic Brauer quotient by arithmetic unit cups is one finite group on every finite-type base. Relative Brauer finiteness follows for every morphism identifying units. For every abelian scheme A/S, the entire prime-to-p subgroup of H1(S,A) is finite and H1(S,A)[1/p] is finitely generated over Z[1/p]. The zero-section splitting of the derived Picard complex gives an actual injection into Brauer classes and controls its finite 2-primary kernel; it does not assume that torsion in a quotient lifts to torsion. B, D and root each read the complete written proof.

Yuan’s published fixed-finite-field reduction is also integrated, with a full proof account and exact source locators. The remaining surface-Tate condition can be restricted to smooth projective geometrically integral surfaces satisfying H1(Y,O_Y)=0. Its prime independence is proved using the intersection pairing and the Frobenius polynomial. This is a smaller intrinsic test class and qualifies as a main-gate reduction. It does not prove the restricted conjecture. The all-prime strengthening itself retains the same Tate gate and is not separately counted as progress for the stopping rule.

Checkpoint05 was saved at its scheduled 06:35 UTC boundary with 248 included files, 72 unchanged references, and 2,348,090 ZIP bytes. Its 136-page PDF had 144 numbered statements, 568 check events (including 131 explicit cross-references, not independent checks), 148 canonical bibliography entries, and 176 literature records. Its SHA256 is ca29760d4d7867302b9e5607d9f08954f030db1468f873ab60b623d7ee420d0f. The final build had zero overfull boxes, undefined references or citations, or LaTeX/BibTeX warnings. The 33 inspected page renders were pixel-identical after the final bibliography consolidation. The prime-uniform proof notes were included there; these complete integrated statements and the new irregularity-zero proof will be included in the next scheduled checkpoint.
'''
for filename in ['PROGRESS_LEDGER.md', 'RESEARCH_SA05_report.md']:
    path = ROOT / filename
    if heading not in path.read_text():
        path.write_text(path.read_text() + entry)
result = {'recorded_at': now, 'root_events': len(rows), 'new_events': added,
          'formal_review': False, 'seconds': round(time.monotonic() - started, 6)}
(ROOT / 'code/record_prime_uniform_and_surface_audit_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
