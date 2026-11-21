"""Execute the first scheduled review only after the actual three-hour mark."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib

r=Path(__file__).resolve().parent
now=datetime.now(timezone.utc)
due=datetime(2026,11,21,2,0,tzinfo=timezone.utc)
if now<due:
    raise SystemExit('The first scheduled review is not yet due.')
out=r/'PROGRESS_REVIEW_01.md'
if out.exists():
    raise SystemExit('Refusing to overwrite a completed scheduled review.')
rows=list(csv.DictReader((r/'QUESTIONS.tsv').open(),delimiter='\t'))
head=f'''# Scheduled progress review 01

Actual review time: {now.isoformat()}. Scheduled deadline: 2026-11-21 02:00 UTC /03:00 CET. This is the first review after the approximately23:00 UTC start; no earlier interim ledger entry was counted as a scheduled review.

Reviewer: /root, GPT-6 Astra Pro; effort not exposed; run GCT_NSRH_20261121.

## Decision: movement; continue

The baseline is the start-of-run open task and the dated earlier gates in LEDGER.md. This first review assesses the whole initial three-hour interval. It does not count formatting, final-text matching, citation repair, or packaging as mathematical movement.

Substantive changes meeting the user's rule include:

- The main conditional sign reduction is strictly broader: F24 removes common input parity in favor of real signed visible Euler coefficients at even path lengths, with the exact finite-extension visibility qualification. F32 proves the admissible countable version and identifies when reciprocal duality forces finiteness.
- The proposed finite all-extension normalized-word comparison is closed negatively by F26. F35 supplies a complete scalar stack alternative and computes exactly why its unbounded dual fails the second spectral bound. These are resolved specified comparison rows, not a universal impossibility claim.
- The previously missing actual rank-three tensor action, joint left/right positivity and bar are supplied by F21/F43. The relative smooth corner and perfect coefficient lift are supplied by F44. F46 supplies exact pure Weil End/Hom data and coherent projective-line objects with both actions and both crossed collision extensions. The remaining existence question in this example is therefore the designated arithmetic, path and basis comparison, rather than every possible pure coefficient realization.
- F45 closes the actual unnormalized word-trace projective/Lefschetz realization question and refutes the stronger specified summand-preserving positive SL2-kernel model.
- The attached homogeneous PH1 target is closed negatively by the precisely checked prior Kahle–Michałek theorem. F37 closes the stated listed-row two-row rectangular witness problem. General multiplicity inequalities and designated canonical positivity remain open.

The global GCT target is not claimed proved or refuted. No unidentified nonstandard RH is silently substituted by the modern noncommutative Weil conjecture. New reports F48–F50 are still being developed/reviewed and are not needed to justify this review's movement decision.

Consecutive scheduled reviews without movement: **0**. Next scheduled review: **2026-11-21 03:00 UTC /04:00 CET**. Stop only after two consecutive scheduled reviews without movement, unless the session ends.

## Every current question and gate

The table includes closed rows as well as every open row, so the state and scope of each treated question are explicit.

| ID | State | Current gate or proved boundary |
|---|---|---|
'''
def cell(s):return s.replace('|','/').replace('\n',' ')
table='\n'.join('| '+cell(x['id'])+' | '+cell(x['state'])+' | '+cell(x['current_gate'])+' |' for x in rows)
out.write_text(head+table+'\n')
(r/'QUESTIONS_at_review_01.tsv').write_bytes((r/'QUESTIONS.tsv').read_bytes())
state={'last_review_number':1,'last_review_utc':now.isoformat(),'movement':True,'consecutive_no_movement':0,'next_review_utc':'2026-11-21T03:00:00+00:00','decision':'continue','record':out.name,'questions_sha256':hashlib.sha256((r/'QUESTIONS.tsv').read_bytes()).hexdigest()}
(r/'REVIEW_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
with (r/'LEDGER.md').open('a') as f:
    f.write('\n## '+now.isoformat()+' — first scheduled three-hour progress review\n\nMovement: yes. Consecutive no-movement reviews:0. The full row-by-row review is PROGRESS_REVIEW_01.md, with the exact question snapshot QUESTIONS_at_review_01.tsv. Mathematical changes counted are the signed/countable sign criterion, resolved normalized trace comparison, actual joint-action/relative-smooth/pure-coefficient realizations, projective word motives and the precisely scoped effective-rule results. Packaging, proof-record updates and citation corrections are not counted. Research continues; next scheduled review03:00UTC.\n\n'+table+'\n')
with (r/'RUN_METADATA.md').open('a') as f:
    f.write('\nFirst scheduled review completed at '+now.isoformat()+'. Movement yes; consecutive no-movement count0. Next review03:00UTC; checkpoint05 due02:45UTC. See PROGRESS_REVIEW_01.md.\n')
(r/'STATUS_TIME.txt').write_text('WORK IN PROGRESS\nSnapshot UTC: '+now.isoformat()+'\nPaper F01–F47 complete and checked; F48–F50 active reports.\nScheduled review01: movement yes, no-movement count0. Next review03:00UTC; next checkpoint05 at02:45UTC after checkpoint04.\n')
print(json.dumps(state))
