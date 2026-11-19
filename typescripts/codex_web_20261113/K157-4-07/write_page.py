from pathlib import Path
from datetime import datetime, timezone
import csv

OUT = Path(__file__).resolve().parent
ORDER = list(range(98,107)) + list(range(108,115))

def save_page(scan, body, rows, apparatus, sheet_kind='text', hand='Grothendieck'):
    page = OUT / 'pages' / f'K157-4-07_157-4_scan{scan:03d}.tex'
    assert scan in ORDER and not page.exists()
    assert all((OUT/'pages'/f'K157-4-07_157-4_scan{n:03d}.tex').exists() for n in ORDER[:ORDER.index(scan)])
    assert body.startswith('\\scanpage{'+str(scan)+'}')
    page.write_text(body.rstrip()+'\n')
    with (OUT/'K157-4-07_inventory.csv').open('a', newline='') as f:
        w=csv.writer(f)
        for k,(kind,position,words) in enumerate(rows,1):
            w.writerow(['157-4',scan,sheet_kind,hand,f'{scan:03d}-{k:02d}',kind,position,words,'yes'])
    with (OUT/'K157-4-07_doubts.md').open('a') as f:
        f.write(f'\n## First reading — scan {scan}\n\n'+apparatus.rstrip()+'\n')
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with (OUT/'progress.log').open('a') as f:
        f.write(f'scan {scan:03d} done {stamp}\n')
    print(f'scan {scan:03d} done {stamp}; {len(rows)} inventory elements')
