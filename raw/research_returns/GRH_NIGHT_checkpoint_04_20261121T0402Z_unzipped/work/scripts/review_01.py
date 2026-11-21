"""Record the first scheduled movement review, never before the three-hour point."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv,io,json,zipfile

base=Path(__file__).resolve().parents[2]
now=datetime.now(timezone.utc)
meta=json.loads((base/'work/RUN_METADATA.json').read_text())
start=datetime.fromisoformat(meta['started_utc'].replace('Z','+00:00'))
due=start+timedelta(hours=3)
assert now>=due, f'First review is not due until {due.isoformat()}'
out=base/'work/reviews';out.mkdir(exist_ok=True)
dest=out/'review_01.json'
assert not dest.exists(), 'Never overwrite a recorded review.'
with (base/'deliverable/QUESTIONS.tsv').open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;questions=list(reader)
current={q['id']:q for q in questions}
with zipfile.ZipFile(base/'GRH_NIGHT_checkpoint_03.zip') as z:
    previous={q['id']:q for q in csv.DictReader(io.StringIO(z.read('QUESTIONS.tsv').decode()),delimiter='\t')}

movements=[
dict(question='Q-MAS-INFINITE-BASIS',kind='strictly smaller gate and closed comparison',
     reason='Checkpoint03 required a reciprocal-leading-coefficient bound for its prescribed jet basis and still lacked the particular draft map. MT-M18/M19 remove that condition for an adapted block basis and nuclear trace. MT-M24 now proves the actual Masullo smooth test-space/map comparison. The prescribed individual-jet condition remains separate and is not claimed proved.',findings=['MT-M18','MT-M19','MT-M22','MT-M24']),
dict(question='Q-MAS-FAITHFUL-POSITIVITY',kind='exact criterion and actual arithmetic obstruction',
     reason='Checkpoint03 gave the obstruction conditional on a multiple zero. MT-M20 proves an exact iff criterion and a weaker Hilbert realization without derivative bounds; NT-L17 and MT-M23 supply actual unconditional arithmetic multiple zeros, so the obstruction is realized rather than hypothetical.',findings=['MT-M20','NT-L17','MT-M23']),
dict(question='Q-ARTIN-POS',kind='strictly smaller solvable branch',
     reason='The general Heilbronn positivity gate remains, but MT-ART09 proves that the solvable branch only needs to examine high-order zeros of ζ_L/ζ_K, with exact group-dependent thresholds. Base-field zero multiplicities are removed. This is a smaller actual local gate, not a restatement of GRH.',findings=['MT-ART09'])]
for item in movements:
    key=item['question']
    item['baseline_checkpoint03']=previous[key]['state']
    item['current_state']=current[key]['state']
    assert item['baseline_checkpoint03']!=item['current_state']

record=dict(review=1,scheduled_utc=due.isoformat(),actual_utc=now.isoformat(),
            elapsed_hours=(now-start).total_seconds()/3600,
            movement=True,consecutive_reviews_without_movement=0,
            decision='Continue research; the two-consecutive-no-movement stopping condition is not met.',
            next_review_utc=(due+timedelta(hours=1)).isoformat(),
            comparison='Conservative comparison with checkpoint03; enough actual movements occur even within the last45 minutes of the first three-hour period.',
            movements=movements,all_question_count=len(questions),
            all_question_states_file='work/reviews/review_01_questions.tsv',
            unchanged_main_gates=[
              'General non-CM positive-weight GL2 GRH is not deduced from rank-one Hecke GRH.',
              'General Artin holomorphy is not proved; the special S5 central nonvanishing and nonsolvable positivity gates remain.',
              'Full GUE/pair correlation at unrestricted support and independent zero ordinates are not supplied.',
              'Canonical theta-section comparison, general cycle algebraicity and integral cohomology vanishing remain separate.',
              'General P=BPP and deterministic general integer factoring are not claimed; special algorithms retain their precise extra inputs.'
            ])
dest.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
with (out/'review_01_questions.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(questions)
(base/'work/REVIEWS.json').write_text(json.dumps([record],ensure_ascii=False,indent=2)+'\n')
lines=[f'\n### Scheduled movement review1 — {now.isoformat()}\n\n',
       '**Movement: yes. Consecutive reviews without movement: 0. Continue.**\n\n',
       'The first review is at the required three-hour point. The following comparisons use checkpoint03 as a conservative baseline; they count only actual status/gate changes, not new row counts or packaging.\n\n']
for item in movements:
    lines.append(f"- **{item['question']}**: {item['reason']}\n")
lines.append('\nThe complete state and strongest stated gate of every treated question, including every open row, are frozen in `work/reviews/review_01_questions.tsv`; the full dated comparison is `work/reviews/review_01.json`. The current-state table below remains authoritative for subsequent updates.\n\n')
lines.append('The next hourly movement review is due at **2026-11-21 05:02 UTC**. General GL2 GRH, general Artin holomorphy, unrestricted zero statistics, geometric cycle/integral comparison gates and general derandomization remain unresolved in their stated scopes.\n')
with (base/'work/root/ledger_history.md').open('a') as f:f.write(''.join(lines))
(base/'work/CHECKPOINT_STATUS.md').write_text('''# Scheduled checkpoint status

Fourth45-minute checkpoint, due2026-11-21 04:02 UTC.

Research remains in progress. The first scheduled three-hour movement review is complete: actual movement is recorded, and the consecutive no-movement count is zero. The next hourly review is due05:02 UTC. Its complete question baseline and reasoned comparison are preserved under work/reviews/.

The LaTeX paper, current six-column catalogue, all question and check registers, implications, working proofs, computations and continuation instructions are included. Every catalogue row and bibliography source has an exact-ID check event; event text distinguishes source-statement inspection, complete proof reading, classical citation, computation and retrospective metadata crosswalk.

The current paper compiled twice with XeLaTeX at03:58–03:59 UTC (195pages), with no overfull boxes, missing-character warnings or undefined references. The optional PDF has not completed a full visual review and is not included; the required paper is delivered as LaTeX. Full externally retrieved literature is excluded, with primary URLs and exact locators retained.

The unconditional adapted block synthesis and nuclear trace now apply to the actual Masullo smooth quotient. The line Hilbert completion has an exact strict jet cutoff, with an arithmetic endpoint counterexample. The actual fixed-character strip Hilbert quotient has a proved closed kernel and trace-class convolution. The remaining all-character extension and independent positivity are separate.

The CM model-existence gate is closed, exact conductor normalizations and sharper Fourier divisibility bounds are proved, and a precise nonsplit-prime Hodge period gives a uniform analytic weight-disk slope. The solvable Artin gate is narrowed to relative zeta multiplicities. Elliptic reduction and Frobenius-error law consequences retain their exact Dedekind RH inputs. General Artin holomorphy, general non-CM GL2 GRH, unrestricted zero statistics and general derandomization are not claimed.
''')
print(json.dumps({k:record[k] for k in ['review','actual_utc','movement','consecutive_reviews_without_movement','next_review_utc','all_question_count']},indent=2))
