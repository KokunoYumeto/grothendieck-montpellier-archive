"""Save selected source records for the authored follow-up synthesis."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
selection = {
    'claims': [601,602,603,604,605,606,624,625,626,639,640,641,655,656,657,658,659,666,669,671,672,673,676,687,467,472,503,563,564,565,567],
    'problems': [601,603,604,605,606,624,626,641,655,658,666,669,671,672,676,414,415,416,401,402,403,404,407,408,409,410,411,412],
}
for kind, nums in selection.items():
    records = json.loads((root / f'SA14_{kind}.json').read_text())
    wanted = {f"{'C' if kind == 'claims' else 'MP'}-SA14-{n:03d}" for n in nums}
    result = []
    for rec in records:
        if rec['id'] in wanted:
            if kind == 'claims':
                fields = ('id','items','statement','present_status','refs')
            else:
                fields = ('id','title','items','claims','plausible_today','state_of_art','why_open','worth','refs')
            result.append({key: rec[key] for key in fields if key in rec})
    path = root / 'outputs' / f'directions_selected_{kind}.json'
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'{kind}: {len(result)} selected; missing={sorted(wanted - {r["id"] for r in result})}; saved {path}')
