#!/usr/bin/env python3
"""Record the first actual timed review; never count a future review as done.

Later reviews require a fresh proof-based comparison with this saved snapshot.
This utility creates no checkpoint and makes no mathematical status inference.
"""
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import csv,io,json,zipfile
ROOT=Path(__file__).resolve().parent.parent
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,6,55,tzinfo=timezone.utc)
assert now>=due,'First timed review is not due yet'
state_path=ROOT/'PROGRESS_REVIEW_STATE.json'
assert not state_path.exists(),'First timed review already recorded'
with (ROOT/'audit_claims.csv').open() as f: current=list(csv.DictReader(f))
archive=ROOT.parent/'RESEARCH_SA07_checkpoint_02.zip'
with zipfile.ZipFile(archive) as z:
 name=next(x for x in z.namelist() if x.endswith('/audit_claims.csv') and '/work/' not in x)
 prior={x['assertion_id']:x for x in csv.DictReader(io.StringIO(z.read(name).decode()))}
changes=[]
for row in current:
 before=prior[row['assertion_id']]['status']
 if before!=row['status']:changes.append((row['assertion_id'],before,row['status']))
expected={'I.P33.03','I.B05.01','II.MB15.02','II.P16.02','II.P06.01','II.SF21.01'}
assert expected<={x[0] for x in changes}
assert all(next(r for r in current if r['assertion_id']==x)['status']=='REFUTED' for x in expected)
gates={
'A.2 / H2':'The joint-image dimension formulas and real-model refutation are proved. Determine unconditional exact dimensions for the remaining actual period points, with the named period-conjecture implication kept in its stated direction.',
'A.3':'For an elliptic curve over Qbar not isogenous to its conjugate, determine whether an irreducible Q-relation of equal bidegrees(d,d),d>=2 can hold for its actual tau and conjugate(tau). Rational-function relations have been excluded.',
'A.4c / H1':'Exclude nonzero algebraic normalized h for an actual non-CM elliptic curve, already E*:y^2=4x^3-4x-1. The exact growth minimization, G-function, denominator and division-polynomial results leave this gate unchanged.',
'B / global readings':'The named local comparison categories and their exact functors are treated. The unspecified global pseudo-motive category and essential image remain to be constructed; each missing original edition has its own source record.',
'C.1':'Determine the complete geometric essential image of the stated Hodge-pair functor. The abelian image and explicit exclusions are proved, with their restriction maps.',
'D.1-D.2 / H5':'Classify all equality cases of the relative-position bound, and determine the generators/base field intended by K on18:45 before assigning its transcendence degree.',
'E.2 separation':'Finite labelled tests cover every totally real field, every CM field and every cubic field, with the additional generalized-dihedral scope. For arbitrary number fields the exact full-integral transporter gate is image(Aut_tensor omega_Q,Z -> Gal(Qbar/Q))={1,c}. The explicit quartic alpha^4-alpha-1=0 remains. Its CM-abelian/Artin comparison is constructed; its extension to all pure integral data remains to be determined. The projective Tate identities in E.2.9 are necessary constraints.',
'E.2 plain image':'Determine which plain integral torsor classes arise from complex places. No global integral lift is inferred from a rational point or finite congruence solvability.',
'E.3 enriched image':'The specified proposed bijection is refuted by actual full-category deformations; determine the complete geometric essential image for the precisely named enriched target.',
'F.3':'The remaining mathematical obligations and retained documentary/readings are itemized in the complete current assertion table below. The fixed-alpha model identification and LM6 A.22 subgroup step remain explicit.',
'G / H4':'The dated May1966 Tate letter and Nice1970/printed1971 passage are checked. Determine the individual date of manuscript leaf18:5 and its chronological ordering; no dossier-wide date is assigned to that leaf.'
}
counts={}
for r in current:counts[r['status']]=counts.get(r['status'],0)+1
berlin=now.astimezone(ZoneInfo('Europe/Berlin')).strftime('%d %B %Y %H:%M:%S')
lines=['','## Timed review01 — '+berlin+' Europe/Berlin','',
'Actual review time: '+now.isoformat()+'. This is the first timed review, after approximately three hours of work. The preceding working snapshots were not timed stagnation reviews.','',
'**Movement: YES. Consecutive timed reviews without movement:0.** The preserved checkpoint02 assertion table supplies a documentary baseline within this review interval. The following six formerly OPEN or DOCUMENTARY-GAP rows now have checked refutations:','',
'| Assertion | Baseline state | Current state |','|---|---|---|']
for ident,before,after in changes:lines.append(f'| {ident} | {before} | {after} |')
lines+=['',
'The first interval also reduced the A.3 relation gate to equal bidegrees at least(2,2), and established E.2 separation for the totally real, CM and cubic cases. No later theta/growth side result is counted as movement in H1. The fresh original-source evidence and the CM/quartic construction retain the exact unsettled obligations stated below. Packaging and typesetting do not count as movement.','',
'### Main questions at this review','', '| Main question | Strongest proved reduction and remaining obligation |','|---|---|']
for key,value in gates.items():lines.append(f'| {key} | {value} |')
lines+=['','### Every unresolved or retained-reading assertion at this review','',
'Counts: '+', '.join(f'{k}={v}' for k,v in sorted(counts.items()))+'. The complete307-row table remains audit_claims.csv. READING records preserved textual evidence; it is not counted as a newly solved mathematical question.','',
'| Assertion | State | Exact obligation or reading |','|---|---|---|']
for r in current:
 if r['status'] in {'OPEN','READING','DOCUMENTARY-GAP'}:
  note=r['remaining_obligation_or_scope'].replace('|','/').replace('\n',' ')
  lines.append(f"| {r['assertion_id']} | {r['status']} | {note} |")
lines+=['','Next timed review due approximately07:55UTC (08:55 Europe/Berlin). The two-consecutive-no-movement stopping rule has not been met. Continue work on the unresolved gates.','']
with (ROOT/'PROGRESS_LEDGER.md').open('a') as f:f.write('\n'.join(lines))
state={'review_number':1,'actual_utc':now.isoformat(),'movement':True,'consecutive_no_movement':0,'next_due_utc':'2026-11-19T07:55:00+00:00','counts':counts,'changed_rows_since_checkpoint02':changes,'main_gates':gates,'assertion_states':{r['assertion_id']:r['status'] for r in current}}
state_path.write_text(json.dumps(state,indent=2)+'\n')
report=ROOT/'RESEARCH_SA07_report.md';text=report.read_text()
text+='\n\n## First timed review — '+berlin+' Europe/Berlin\n\nThe first timed review records movement: six previously open or documentary assertion rows now have checked refutations, and the A.3 and E.2 gates narrowed during this first interval. The ledger contains the complete current unresolved-row table and the exact remaining gate for every main question. Consecutive timed reviews without movement:0. The next review is due at08:55 Berlin. The non-CM h gate remains unresolved, and this package remains INCOMPLETE.\n'
report.write_text(text)
print(json.dumps({'review':1,'actual_utc':now.isoformat(),'movement':True,'changed_rows':changes,'unresolved_rows':sum(counts.get(x,0) for x in ['OPEN','READING','DOCUMENTARY-GAP']),'next_due_utc':state['next_due_utc']}))
