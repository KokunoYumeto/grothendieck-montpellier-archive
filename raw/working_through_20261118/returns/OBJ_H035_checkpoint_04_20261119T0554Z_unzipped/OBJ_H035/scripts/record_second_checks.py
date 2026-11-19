"""Record completed second checks; do not infer checks from file existence."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run'
false = {5, 8, 10, 14, 15, 21}
with (root / 'CHECK_EVENTS.tsv').open('a') as output:
    writer = csv.writer(output, delimiter='\t')
    for n in range(1, 22):
        result = ('Literal assertion refuted; corrected theorem independently checked'
                  if n in false else
                  'Second mathematical check completed for the explicitly stated reconstruction')
        writer.writerow([f'H035.{n}', stamp, who,
                         'targeted proof check — independent second pass from hypotheses',
                         result, f'research/SECOND_CHECKS.md H035.{n}; PROOFS.tex H035.{n}'])
    for key, result, where in [
        ('EGAIII1', '4.5.1–4.5.3, pp.138–139: coherent Ext and formal completion; proper support matched', 'research/printed_checks/EGA_III_1_135.png and _136.png'),
        ('BourbakiTopIX', 'IX §3 no.2 Proposition 6, pp.TG IX.29–30: nontrivial absolute values; positive power; proof checked', 'research/printed_checks/Bourbaki_Topologie_5_10_149.png and _150.png'),
        ('Stacks02OB', 'Lemma 30.20.4(1),(3) give the pro-isomorphism needed before taking inverse limits', 'https://stacks.math.columbia.edu/tag/02OB; PROOFS.tex H035.34'),
        ('H035.39', 'Dense-open upgrade proves composition axiom (vi), also on reducible quotients; completion remains open', 'PROOFS.tex H035.39'),
    ]:
        writer.writerow([key, stamp, who, 'used and rechecked in this run', result, where])
with (root / 'progress.log').open('a') as output:
    output.write(f'second checks H035.1–21; composition reduced to completion {stamp}\n')
print('Recorded 21 second checks and 4 exact-source/reduction checks at', stamp)
