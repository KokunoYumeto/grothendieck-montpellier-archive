# Write the sweep-3 TSV tables of one topic from a config module (agent a6d42bf6, horizontal sweep 3)
# usage: python -I -B write_tables.py <cfg module path> <out dir>
import importlib.util, os, sys
sys.stdout.reconfigure(encoding='utf-8')
spec = importlib.util.spec_from_file_location('cfg', sys.argv[1]); cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
out = sys.argv[2]
HEAD = {
    'DELIVERABLES': ['cote_part', 'scans', 'transcription', 'folders', 'passes', 'unsure_marks', 'unsure_per_scan', 'illegible', 'doubt_rows', 'open_readings', 'ready_for_edition', 'ready_for_translation', 'next_step'],
    'DEPENDS': ['item', 'relation', 'other', 'basis', 'where'],
    'CORRECTIONS': ['id', 'item', 'where', 'kind', 'what', 'corrected', 'evidence', 'decided_by'],
    'CHECK_EVENTS': ['id', 'date_utc', 'who', 'how', 'result', 'where'],
}
for name, head in HEAD.items():
    rows = getattr(cfg, name, None)
    if rows is None: continue
    for r in rows:
        assert len(r) == len(head), (name, r)
        assert not any('\t' in str(x) or '\n' in str(x) for x in r), (name, r)
    with open(os.path.join(out, name + '.tsv'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\t'.join(head) + '\n')
        for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
    print(name, len(rows))
