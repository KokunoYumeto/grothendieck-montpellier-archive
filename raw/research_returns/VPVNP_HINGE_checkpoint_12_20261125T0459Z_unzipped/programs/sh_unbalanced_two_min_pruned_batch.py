#!/usr/bin/env python3
"""Enumerate two-minimum branches, pruning only exact SH39 inequalities."""
import json
import subprocess
import sys
from pathlib import Path

from sh_unbalanced_two_minimum_certificate import rectangular_violation


def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    work = Path(__file__).resolve().parents[1]
    D, m = config['dimension'], config['width']
    cases, pruned = [], []
    for t in config['first_minima']:
        for y in range(t, (m-1)*D):
            for h in range(D//2+1):
                base = dict(first=t, second=y, distance=h)
                p = 2**(m*(D-h))
                if 2**t + 2**y < p:
                    pruned.append(base | dict(reason='mixed-cut rank sum bound'))
                    continue
                if h and 2**(m*h) > m*(D-h)+1 and 2**t + 2**y <= p:
                    pruned.append(base | dict(reason='strict rectangular sum bound'))
                    continue
                witness = rectangular_violation(t, y, D, m, h) if h else None
                if witness:
                    pruned.append(base | dict(reason='rectangular inequality', witness=witness))
                    continue
                stem = f'sh_unbalanced_two_min_D{D}_m{m}_t{t}_y{y}_h{h}'
                cfg = dict(dimension=D, width=m, low_value=t, other_low_value=y,
                           marked_distance=h, seconds=config.get('seconds_per_case', 30))
                inp = work / 'inputs' / (stem+'.json')
                inp.write_text(json.dumps(cfg, indent=2))
                cases.append((stem, inp))
    log = work / 'outputs' / f'sh_unbalanced_two_min_D{D}_m{m}_pruned_batch.jsonl'
    with log.open('w') as stream:
        for stem, inp in cases:
            out = work / 'outputs' / (stem+'.json')
            existing = json.loads(out.read_text()) if out.exists() else {}
            if 'verification' in existing:
                row = dict(case=stem, exit=0, reused=True, certificate=True)
            else:
                run = subprocess.run([sys.executable,
                    str(work/'programs/sh_unbalanced_two_minimum_certificate.py'),
                    str(inp), str(out)], capture_output=True, text=True)
                result = json.loads(out.read_text()) if out.exists() else {}
                row = dict(case=stem, exit=run.returncode, certificate='verification' in result,
                           output=run.stdout.strip(), error=run.stderr[-4000:])
            stream.write(json.dumps(row)+'\n'); stream.flush()
            if row['exit'] or not row['certificate']:
                print(json.dumps(row), flush=True)
    manifest = dict(config=config, cases=[s for s,_ in cases], pruned=pruned,
                    complete=True, certified=sum('verification' in json.loads(
                        (work/'outputs'/(s+'.json')).read_text())
                        for s,_ in cases if (work/'outputs'/(s+'.json')).exists()))
    (work/'outputs'/f'sh_unbalanced_two_min_D{D}_m{m}_pruned_manifest.json').write_text(
        json.dumps(manifest, indent=2))
    print(json.dumps({k:v for k,v in manifest.items() if k not in ('cases','pruned')} |
                     dict(cases=len(cases), pruned=len(pruned))), flush=True)


if __name__ == '__main__':
    main()
