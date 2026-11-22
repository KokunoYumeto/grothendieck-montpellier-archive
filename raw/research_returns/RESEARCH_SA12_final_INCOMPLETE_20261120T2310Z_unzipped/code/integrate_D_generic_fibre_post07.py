"""Record the all-dimensional generic-fibre reduction completed before checkpoint08."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
record = root / 'code/output/integrate_D_generic_fibre_post07.json'
if record.exists():
    raise SystemExit('Refusing to duplicate this integration.')
now = datetime.now(timezone.utc).isoformat()
p = root / 'code/assemble.py'
s = p.read_text()
for prefix in ["('D.1',", "('D.2(ii)',"]:
    old = next(line for line in s.splitlines() if line.startswith(prefix))
    new = old.replace('Incomplete in general; ', 'Incomplete in general; generic-fibre criteria in every dimension, vertical boundaries and projective geometric generic normalization proved; ', 1)
    marker = "','D:"
    new = new.replace(marker, "','D:generic-fibre-generation; D:vertical-boundary-all-dimensions; D:projective-generic-normalization; D:", 1)
    s = s.replace(old, new)
target = 'D.1/D.2(ii) remain open in full. '
replacement = ('D.1/D.2(ii) remain open in full. The fibration reduction now works in every dimension: '
    'the image of the geometric generic fundamental group is closed and normal by the arithmetic '
    'exact sequence and connected-cover localization. If that image is finitely generated and '
    'the open meets every fibre, the full open group is finitely generated. For fixed-boundary '
    'quotients, finite generation of the normal geometric generic fixed-boundary group suffices, '
    'with whole omitted fibres allowed. Thus every vertical boundary on a proper normal scheme '
    'mapping to a curve has finitely generated fixed-boundary quotient; when the vertical boundary '
    'has codimension at least two, its full open group is finitely generated. More generally every '
    'boundary is covered when the geometric generic fibre has projective normalization, after '
    'the stated Stein factorization. A single fixed base open comes from the retained smooth '
    'locus, and the finitely many remaining full or wild inertia images are bounded by component '
    'multiplicities. ')
assert target in s
s = s.replace(target, replacement, 1)
p.write_text(s)
entry = f'''

## All-dimensional generic-fibre reduction: {now}

The completed labels D:generic-fibre-generation, D:vertical-boundary-all-dimensions, and D:projective-generic-normalization have full actual-file audits by root, B and D, in addition to C's authored proof. Root and the independent readers opened Stacks0BTX and056V with their proofs. Root and C also reread the full original SGA1 X Theorem2.9 pp273--274. All pure-normalization, topological-invariance and tame-DVR dependencies were checked in the preceding all-boundary proof.

The arithmetic exact sequence over the base function field makes the geometric generic image normal. Restriction to the generic fibre is surjective on fundamental groups because a connected cover of a normal integral open stays integral upon localization. The retained relative smooth locus supplies ONE base open, independent of the finite cover, on which each descended base cover is unramified. At the finitely many remaining points, multiplicities bound the full inertia when a component is retained, and the wild inertia for the original fixed-boundary quotient. Killing those finite images gives a quotient of a proper or tame curve group.

The resulting criteria hold in every dimension, without requiring the open morphism to be proper. They cover every vertical boundary on a normal proper scheme mapping to a curve; the full open group is covered when the open meets every fibre, automatically for a vertical codimension-at-least-two boundary. They also cover every original boundary when the normalization of the geometric generic fibre is projective. This is a further reduction of both D gates. It does not supply an arbitrary global morphism to a curve or control newly extracted horizontal valuations of a rational pencil.

The scope audit also confirms that a normal proper surface with a morphism to a curve need not be projective: Schroer1999 printedpp3--4, sections2.2--2.5, constructs the two-centre normal nonprojective scheme over P1, with Pic(P1) mapping bijectively to its Picard group. B reread the primary PDF and C independently reproduced the nontorsion-difference Picard calculation. That earlier explicit mutation case is not counted again as new movement; the broader fibration criteria are the new statements.

The previously inspected173-page build54 is being superseded by a new complete build containing these three proofs. Its visual verification record is preserved as an intermediate record; only the final verified PDF hash will be used in checkpoint08. Only general D.1, D.2(ii), and residual L8 remain requested open. The report remains INCOMPLETE.
'''
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md', 'parts/D/ROOT_POST_REVIEW03_NOTES.md']:
    with (root / name).open('a') as f:
        f.write(entry)
old = root / 'qa/pdf_verified_checkpoint08_build54.json'
if not old.exists():
    old.write_text((root / 'qa/pdf_verified.json').read_text())
old_render = root / 'qa/checkpoint08_build54_render.json'
if not old_render.exists():
    old_render.write_text((root / 'qa/checkpoint08_render.json').read_text())
record.write_text(json.dumps({'utc': now, 'new_audited_statements': 3,
    'strict_gate_reductions': ['all-dimensional vertical boundaries', 'all original boundaries with projective geometric generic normalization', 'generic-fibre generation criterion'],
    'open_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual']}, indent=2) + '\n')
print(record.read_text())
