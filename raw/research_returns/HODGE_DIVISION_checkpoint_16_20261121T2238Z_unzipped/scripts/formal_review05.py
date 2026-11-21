"""Fifth substantive review; immutable comparison with actual review04 gates."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,json
R=Path(__file__).resolve().parents[1]; sp=R/'RUN_STATE.json';state=json.loads(sp.read_text());now=datetime.now(timezone.utc)
start=datetime.fromisoformat(state['start_utc']);due=start+timedelta(hours=7)
if now<due:raise SystemExit(f'Not due until {due.isoformat()}; no review written.')
if state.get('formal_reviews_completed')!=4:raise SystemExit('Requires completed review04 exactly; no replay.')
rows=list(csv.DictReader((R/'QUESTIONS.tsv').open(),delimiter='\t'));byid={r['id']:r for r in rows}
for name,expected in {'Q2ao':'refuted','Q2aq':'refuted','Q2ar':'proved','Q2as':'proved','Q2at':'proved','Q2au':'refuted','Q2av':'refuted','Q5n':'refuted','Q5o':'refuted','Q5p':'proved'}.items():assert byid[name]['state']==expected,(name,byid[name]['state'])
opened=[r for r in rows if r['state'] in ('active','open','unchecked')]
assert {r['id'] for r in opened}=={'Q2i','Q5i'}
text=f'\n## Formal movement review05 — {now.isoformat()}\n\nFifth formal review, due{due.isoformat()}, compared substantively with review04 at16:39:10UTC.\n\n'
text+='''**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main gates have strictly shrunk.

For Q2i, D-BI-21 excludes all A1 simple cores and D-BI-22 excludes all Suzuki/Ree/Tits cores, with universal-cover and outer-normalizer scope made explicit. D-SPW-01--03 excludes every odd-characteristic symplectic Weil case except a single Sp4(3) factor of degree4 or5; D-SPW-04 extends that final endpoint to every representation of the transitive small core in the nonsplit non-Eisenstein problem. HD-ALT-02 plus D-AST-01--03 excludes every ordinary alternating core8<=n<=14. HD-ALT-03 excludes balanced Young shapes for all n>=15 without ESD or determinant restrictions and proves that every remaining large ordinary alternating core is a real long-shape/ESD case. These are proper reductions beyond the alternating and small-Lie alternatives at review04. The intermediate HD-ALT-01 restriction has been strictly strengthened, not counted twice as an independent final gate.

For Q5i, SF-E817 excludes every nonzero finite point defect with locally free hull, without stability or simplicity. SF-E818 eliminates surface and curve defects when that hull has a stable locally free equal-slope filtration. SF-E819/E819R reaches actual nonpure coherent sheaves: locally free hull with finite kernel/cokernel requires equal lengths at each point, and every nontrivial local modification must have a nonreduced defect module. This is a proper restriction on the singular/coherent gate at review04. The rank36 example is an actual balanced coherent sheaf, but it fails semiregularity and is explicitly not a successful seed.

SF-E815R's stronger End bound63, full-primary-source substitutions, finite failed searches, the sharpness witness for a single bivector, consolidation of current-gate wording, and packaging are not counted as movement. The linear/unitary Weil and G2/triality investigations are still work in progress at this review and are not counted before complete proof checks.

### Every open row at this review

| Row | State | Strongest proved reduction and remaining gate |
|---|---|---|
'''
for r in opened:text+=f"| {r['id']} | {r['state']} | {r['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
text+='''
### Main-question gates

- **Target1, Gaussian principal fourfolds:** complete checked polarization, actual published rank4 dominance and explicit integral detector/quadratic division constants. No new open gate.
- **Target2, class-number-one sixfolds with every determinant:** all split families, all Eisenstein determinants, and Gaussian signed determinant class3 have numerical bounds. Other nonsplit determinants remain unresolved. The finite-cover supplier gate is now restricted by the exact exceptional low-degree profiles and the stronger core/shape exclusions above; original-field descent, actual rank9, and cycle supply are still necessary for every surviving profile. The genuine balanced-RM eightfold seed remains the non-curve alternative.
- **Target3, Eisenstein split eightfolds through G34:** complete published-input reconstruction, actual rank16, integral algebraic suppliers/transfer and effective fixed-order/polarization constants. No unrefereed Severn theorem is a premise.
- **Target4, natural imprimitive sources:** exact signature criterion, all-family nondominance and sharp n5 maxima15/14 remain proved. The exact terminating rank procedure is proved per specified Nielsen component; only the explicitly documented examples and finite certificates have been executed. No unbounded table is claimed.
- **Target5, actual perfect-complex construction for n3 or n4:** the n3 request is fulfilled by the checked actual perfect complex and coherent numerical variant. The additional genuine balanced-RM n4 construction remains open, with the stronger stability, derived-class and local-modification restrictions stated in Q5i. No failed balanced candidate is called a seed.

All findings counted here have recorded whole-proof readings. Independent arithmetic checks are distinguished from reruns and from cited complete character tables. The E819 trace/evaluation composition is now cited directly to published Buchweitz--Flenner2008 Theorem6.4.2; the specified finite-action compatibility retains its supplied DEG_L S21 status. Conditional Markman, Severn and032 claims retain their original statuses. The current98-file included TeX graph passes source-integrity checks; no successful TeX compilation is claimed.

Continue research on the smaller nonsplit-source and balanced-RM construction gates. Next formal review is due2026-11-21T18:38:55+00:00. No stopping rule is triggered.
'''
with (R/'LEDGER.md').open('a') as f:f.write(text)
state.update(last_review=now.isoformat(),formal_reviews_completed=5,consecutive_reviews_without_movement=0,next_review_utc=(start+timedelta(hours=8)).isoformat());sp.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({'review':5,'time_utc':now.isoformat(),'movement':True,'open_rows':[r['id'] for r in opened],'consecutive_no_movement':0}))
