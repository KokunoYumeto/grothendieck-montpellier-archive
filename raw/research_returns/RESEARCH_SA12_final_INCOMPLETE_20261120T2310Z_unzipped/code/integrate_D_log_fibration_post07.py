"""Record the full fixed-boundary fibration theorem and explicit source calculation."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
record = root / 'code/output/integrate_D_log_fibration_post07.json'
if record.exists():
    raise SystemExit('Refusing to duplicate this integration.')
now = datetime.now(timezone.utc).isoformat()
p = root / 'code/assemble.py'
s = p.read_text()
old = next(line for line in s.splitlines() if line.startswith("('D.1',"))
new = "('D.1','Incomplete in general; every boundary on a proper normal surface mapping to a curve and mixed Q-factorial/lc/formally graded surface boundaries proved; all fixed-boundary quotients small with all-open pronilpotent generation','D:surface-map-all-boundaries; D:log-fibration-criterion; D:weighted-graded-boundary; D:formal-cone-fixed-boundary; D:negative-curve-tame; D:mixed-fixed-boundary; D:surface-mixed-boundary; D:lc-surface-boundary; D:finite-exceptional-wild; D:fixed-boundary-small; D:cohomology-crown-criterion; D:uniform-H1-obstruction; D:fixed-boundary-positive; D:boundary-neighborhood; D:finite-field-surfaces; D:fixed-vs-valuation; D:fixed-boundary-gate'),"
s = s.replace(old, new)
target = 'D.1/D.2(ii) remain open in full. Every proper normal surface admitting a nonconstant morphism to a proper curve now has a finitely generated fundamental group after any finite puncture.'
replacement = 'D.1/D.2(ii) remain open in full. Every proper normal surface admitting a nonconstant morphism to a proper curve now has a finitely generated fixed-boundary tame quotient for every proper closed boundary. In particular, its full fundamental group is finitely generated after any finite puncture. The arbitrary-boundary proof allows whole omitted fibres and inseparable horizontal components: a finite purely inseparable base change and normalization produce a smooth pointed generic curve, preserve the etale site, and pull back every originally tame cover. The logarithmic homotopy sequence supplies a finitely generated normal fibre image, while the p-part of each base inertia image divides every fibre multiplicity and is therefore finite. Killing these finitely many wild images reduces the base quotient to a tame curve group.'
assert target in s
s = s.replace(target, replacement)
target = 'This disproves universal single-curve tameness, but does not refute finite generation.'
replacement = 'This disproves universal single-curve tameness, but does not refute finite generation. The covering surface itself has one genus-two exceptional curve of square -2. The weighted inequality excludes every further wild quadratic cover, including covers with more complicated source resolutions; purity and proper henselian comparison then compute its strict-local maximal pro-two quotient as trivial and that of the original surface as cyclic of order two. No bound on nonabelian wild inertia follows from that computation.'
assert target in s
s = s.replace(target, replacement)
p.write_text(s)
entry = f'''

## Full curve-fibration boundary theorem and wild-source calculation: {now}

D:log-fibration-criterion and D:surface-map-all-boundaries are proved with full independent actual-file and exact primary-source audits. Every proper closed boundary on every normal proper surface admitting a nonconstant morphism to a proper curve is now covered. The pure base changes address both geometric normality of the generic curve and inseparable horizontal points. The finite radicial normalization preserves the etale site and takes each new boundary divisor to an original boundary divisor; the exact DVR base-change theorem preserves tameness. The proper log homotopy theorem supplies a finitely generated normal tame-fibre image. At each bad fibre, the p-part of descended inertia divides the p-part of every component multiplicity, whether the component is retained or belongs to the original boundary. One open subgroup kills all these finite wild images and is a quotient of a tame curve group. This is a strict D.1 gate reduction beyond the earlier vertical finite-puncture theorem.

D:wild-genus2-source and D:wild-genus2-pro2 compute the resolution and local pro-two groups of the explicit fierce example. The source has one smooth genus-two exceptional curve of square -2 and discrepancy -2, and its resolution maps finitely to the target resolution, inducing relative Frobenius on the exceptional curves. The inequality for a single positive-genus target curve rules out every wild quadratic cover of this source without restricting its source resolution. Purity and proper henselian comparison reduce the possible quadratic covers to the exceptional curve, whose Frobenius on H1(O) is nilpotent. Thus the two strict-local maximal pro-two quotients are1 and C2. The complete22-assertion chart/Frobenius certificate passed and was independently rerun. This is an auxiliary calculation; it does not close a general finite-generation row or establish finite full wild inertia.

Root independently read the complete two new fragments. Exact opened sources include Hoshi2006 Proposition2.1 and Theorem2.3 pp13--16 and PropositionA.10 pp57--58; Stacks0BXT,0B8Y,04DY,0EXY,0EYD for the log-fibration reduction; and Stacks0EGH,0BMB,0A48 for the explicit source. D independently audited both files and their primary inputs. C also audited the source calculation. The new source keys remain unique in the combined bibliography.

The main unresolved rows remain general D.1, general D.2(ii), and the dependent L8 component. A remaining normal surface in either geometric gate cannot admit a nonconstant morphism to a proper curve and must also avoid the other proved projective-modification and local-singularity criteria. General rational pencils on resolutions do not satisfy the theorem automatically: extracted horizontal exceptional valuations need not be tame under the original boundary condition. The report remains INCOMPLETE. Formal review04 and checkpoint08 are due06:10 UTC.
'''
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md', 'parts/D/ROOT_POST_REVIEW03_NOTES.md']:
    with (root / name).open('a') as f:
        f.write(entry)
record.write_text(json.dumps({
    'utc': now, 'new_audited_statements': 4,
    'certificate_programs_after_inventory_update': 21,
    'strict_gate_reduction': 'D.1 every fixed boundary on every proper normal surface mapping to a curve',
    'auxiliary_only': ['explicit fierce source resolution', 'exact two strict-local pro-two quotients'],
    'open_requested_rows': ['D.1 general', 'D.2(ii) general', 'L8 residual']
}, indent=2) + '\n')
print(record.read_text())
