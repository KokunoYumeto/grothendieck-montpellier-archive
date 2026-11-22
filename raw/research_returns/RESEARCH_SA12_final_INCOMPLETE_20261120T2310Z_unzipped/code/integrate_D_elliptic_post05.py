"""Record the audited elliptic surface gate reduction after checkpoint05."""
from pathlib import Path
from datetime import datetime, timezone
import json, csv

root=Path(__file__).resolve().parents[1]
record=root/'code/output/integrate_D_elliptic_post05.json'
if record.exists():
    raise SystemExit('Already recorded.')
now=datetime.now(timezone.utc).isoformat()
p=root/'code/assemble.py';s=p.read_text()
s=s.replace("'D:fixed-boundary-small; D:pronilpotent-obstruction; D:fixed-boundary-positive", "'D:lc-elliptic-tame; D:schroer-elliptic; D:fixed-boundary-small; D:pronilpotent-obstruction; D:fixed-boundary-positive")
s=s.replace("'D:codim-two-small; D:pronilpotent-obstruction; D:fixed-boundary-positive", "'D:schroer-elliptic; D:lc-elliptic-tame; D:codim-two-small; D:pronilpotent-obstruction; D:fixed-boundary-positive")
s=s.replace('The explicit surface test uses a field with transcendence over its prime field.', 'The explicit elliptic three-point surface with trivial Picard group is now proved to have finitely generated punctured fundamental group: log-canonical positive-genus discrepancy forces tameness on a projective partial contraction. The remaining Schroer test has initial curve genus at least two and uses transcendental constants. This is a genuine exclusion of a previously open geometric instance.')
p.write_text(s)
p=root/'code/render_checkpoint.py';s=p.read_text().replace("'finite constant extensions'", "'finite constant extensions','positive-genus exceptional','elliptic three-point','minimal resolution'")
p.write_text(s)

with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write(f'''\n\n## Elliptic geometric gate removed: {now}\n\nD:lc-elliptic-tame proves that finite separable quasi-etale covers of a log canonical surface are tame at every positive-genus exceptional valuation. The elementary proof computes the different by a differential determinant, proves nonpositive discrepancies on a minimal resolution by negative definiteness, and forces discrepancy−1 on every positive-genus exceptional curve upstairs and downstairs. D:schroer-elliptic applies it to the two simple-elliptic contractions in the explicit three-point proper nonprojective surface with Pic=0. Schroer section3.1 provides a projective partial contraction retaining those two curves; all covers are tame there, so the projective fixed-boundary theorem proves finite generation. The third non-lc configuration is left as a codimension-two point. Root and B audited the full written proof.\n\nThis is a strict reduction of the residual geometric gate: that explicit elliptic instance is no longer open. The analogous higher-genus instance and the general D.1/D.2(ii) assertions remain open. The overall package stays INCOMPLETE. This is not a formal stopping review; the next review remains05:10 UTC.\n''')
with (root/'report_supplement.md').open('a') as f:
    f.write(f'''\n\n## Elliptic surface exclusion at {now}\n\nThe explicit elliptic Schroer surface with trivial Picard group and three omitted contraction points now has a proved finitely generated fundamental group. Its two simple-elliptic singularities are Gorenstein log canonical, checked by a rational differential form. Every quasi-etale cover is tame at their exceptional curves by the discrepancy/differential argument. A projective partial contraction then supplies the full finite-generation theorem. The remaining explicit construction has genus at least two; the general D assertions are not claimed. Exact source locators and the two independent actual-file audits are recorded.\n''')
with (root/'parts/D/CHECK_EVENTS_D.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['D:lc-elliptic-tame;D:schroer-elliptic',now[:10],'GPT-6 Astra; /root','independent primary-source verification after actual-file audit','Opened Stacks0BGP,0C2M,0C5R with proofs; independently opened Schroer section3.1 printedp5 (projective partial contraction of A union R2) and Cambridge Kollar2013 chapter10 preview, Theorem10.1 with explicitly arbitrary-characteristic scope. Preview exposes statement, not full proof. The algebraic derivation and complete geometric application were independently checked.'])
record.write_text(json.dumps({'utc':now,'new_proved_labels':['D:lc-elliptic-tame','D:schroer-elliptic'],'remaining':['D.1 general','D.2(ii) general','Schroer genus>=2']},indent=2)+'\n')
print(record.read_text())
