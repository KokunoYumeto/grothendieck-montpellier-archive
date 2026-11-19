"""Record the exact cross-part claims and problems consulted for selection."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
claim_nums = [3,6,8,9,10,11,12,13,17,20,22,25,70,71,79,80,81,88,89,90,94,95,97,98,99,100,111,112,116,140,141,142,205,206,207,208,216,217,243,244,251,252,258,293,294,295,296,297,298,300,301,302,303,307,498,502]
problem_nums = [1,2,3,6,7,8,10,28,29,32,35,36,37,39,40,43,44,49,54,204,205,208,215,216,221,242,243,244,245,246,248,249,250,251]
lines=[]
for kind,nums,prefix in [('claims',claim_nums,'C'),('problems',problem_nums,'MP')]:
    records={r['id']:r for r in json.loads((root/f'SA14_{kind}.json').read_text())}
    for n in nums:
        rec=records[f'{prefix}-SA14-{n:03d}']
        if kind=='claims':
            lines.append(f"{rec['id']} | {', '.join(rec['items'])} | {rec['statement']}")
        else:
            lines.append(f"{rec['id']} | {rec['title']} | {rec['plausible_today']}")
out=root/'outputs'/'directions_core_inventory.txt'
out.write_text('\n'.join(lines)+'\n')
print(f'Saved {out}; {len(lines)} records.')
