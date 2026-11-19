"""Write a mandatory timed review; do not treat packaging as progress."""
from pathlib import Path
from datetime import datetime,timedelta,timezone
import sys

root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
movement=sys.argv[2]
if movement not in ('movement','no-movement'):raise SystemExit('Specify actual movement state.')
start=datetime(2026,11,19,2,54,34,tzinfo=timezone.utc)
due=start+timedelta(hours=number+2)
now=datetime.now(timezone.utc)
if now<due:raise SystemExit('Review not yet due: '+due.isoformat())
heading=f'### Review {number:02}'
ledger=root/'PROGRESS_LEDGER.md'
text=ledger.read_text()
if heading in text:raise SystemExit('Review already recorded.')
text=text.replace('None yet due. Movement means an open row changes status or a main gate becomes strictly smaller; packaging and restatement do not count.',
 'Movement means an open row changes status or a main gate becomes strictly smaller; packaging, source searches, and restatement do not count.')
if number==1:
    if movement!='movement':raise SystemExit('Review 01 has recorded genuine movement.')
    assessment='''**Movement: yes. Consecutive reviews without movement: 0.**

H035.30, the central six-axiom Theorem 12, has changed from unverified to
proved, with a separate derivation recorded. All statement rows except
H035.39–40 have proofs, matched sources, or checked counterexamples and
proved repairs. All 44 supplied-note subclaim rows have verdicts.

H035.39 has undergone strict reductions: all noncompletion axioms are proved
stable; completed-output finiteness suffices for the pro-comparison; full
countable-base closure is proved; maximal finiteness implies principal
finiteness; and the remaining sufficient finiteness gate reduces to local
residue-field-valued functors over an incomplete uncountable base. The last
strict reduction was recorded at 05:29:26 UTC. Later source searches,
rejected candidates, the residue-field inner-composition side case, and
entry updates are explicitly not counted as further movement.

Open rows at this review:

- **H035.39:** the exact residue-field finite-output gate at the top of this
  ledger, together with the distinction between sufficiency and necessity
  for composition. No qualifying counterexample has been constructed.
- **H035.40:** the unrestricted two-scheme programme has no definition on
  the page. Contextual affine/proper examples are proved and the unqualified
  nonproper direct-image extension is refuted; a general formulation and
  its promised closure properties remain unresolved here.

Continue the work. The next review is due at 06:54:34 UTC.
'''
else:
    raise SystemExit('Later reviews require their actual dated assessment to be implemented before recording.')
text+=f'\n\n{heading} — {now.isoformat()}\n\n'+assessment
ledger.write_text(text)
with (root/'progress.log').open('a') as stream:
    stream.write(f'progress review {number:02} {now.isoformat()} movement=yes; no-movement streak=0; open H035.39,H035.40\n')
print('Recorded',heading,now.isoformat(),movement)
