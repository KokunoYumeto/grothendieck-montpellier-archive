#!/usr/bin/env python3
"""Check the names and normal core fusions of root's retained L3(4) input.

This is structural input QA, not an independent character-spectrum scan.
"""
import hashlib
import json
from pathlib import Path
import time

start = time.perf_counter()
base = Path(__file__).resolve().parents[4]
source = base/'research/a2_cores/small_inputs.json'
raw = source.read_bytes()
data = json.loads(raw)
tables = {t['name']: t for t in data['tables']}
cores = ['L3(4)', '2.L3(4)', '3.L3(4)', '4_1.L3(4)',
         '4_2.L3(4)', '6.L3(4)', '12_1.L3(4)', '12_2.L3(4)']
names = []
fusions = []
for core in cores:
    names.append(core)
    suffixes = ['.2_1', '.2_2', '.2_3']
    if core in ['L3(4)', '3.L3(4)']:
        suffixes += ['.3', '.6']
    for suffix in suffixes:
        name = core+suffix
        names.append(name)
        C, E = tables[core], tables[name]
        assert E['core'] == core
        fusion = [i-1 for i in E['fusion']]
        assert len(fusion) == len(C['sizes'])
        assert fusion[0] == 0 and fusion.count(0) == 1
        assert all(C['orders'][i] == E['orders'][j]
                   for i, j in enumerate(fusion))
        aggregate = {}
        for i, j in enumerate(fusion):
            aggregate[j] = aggregate.get(j, 0)+C['sizes'][i]
        assert all(total == E['sizes'][j] for j, total in aggregate.items())
        assert sum(aggregate.values()) == C['order']
        d = int(suffix.split('_')[0][1:])
        assert E['order'] == d*C['order']
        fusions.append({'core': core, 'extension': name, 'index': d})
assert len(names) == len(set(names)) == 36
assert all(name in tables for name in names)
assert len(fusions) == 28
result = {
    'status': 'PASS', 'elapsed_seconds': round(time.perf_counter()-start, 6),
    'input_path': str(source), 'input_sha256': hashlib.sha256(raw).hexdigest(),
    'covered_tables': names, 'covered_table_count': 36,
    'normal_fusions_checked': fusions, 'normal_fusion_count': 28,
    'scope': 'Name, order, identity-kernel, element-order and normal-class-size consistency; no character-spectrum scan.',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()
                  if k not in ['covered_tables','normal_fusions_checked']}, indent=2))
