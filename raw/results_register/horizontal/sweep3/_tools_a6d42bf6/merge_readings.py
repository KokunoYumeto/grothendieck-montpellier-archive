# Merge sub-agent readings into a topic's sweep-3 files (agent a6d42bf6, horizontal sweep 3). Idempotent.
# usage: python -I -B merge_readings.py <topic dir, e.g. .../sweep3/SA21>
# Reads <topic>/readings/<stretch>_CHECK_EVENTS.tsv, _CORRECTIONS.tsv, _DELIVERABLES.tsv, _DEPENDS.tsv (same columns as the topic tables)
# and <stretch>_INTEGRATION.md with sections '## STUDY', '## HUNCHES', '## PACKAGES'.
# TSV rows: CHECK_EVENTS/CORRECTIONS keyed on column 1 (added if new); DELIVERABLES keyed on columns 1-2 (replaced); DEPENDS appended if new.
# Markdown: each block goes into STUDY.md / HUNCHES.md / RESEARCH_PACKAGES.md between <!-- reading:<stretch> --> markers (replaced on rerun).
# Run it again after any write_tables.py run, which rewrites the TSVs from the cfg.
import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
T = sys.argv[1]; R = os.path.join(T, 'readings')
def rows(p):
    with open(p, encoding='utf-8') as f: L = [l.rstrip('\n') for l in f if l.strip()]
    return L[0], [l.split('\t') for l in L[1:]]
for name, key in (('CHECK_EVENTS', 1), ('CORRECTIONS', 1), ('DELIVERABLES', 2), ('DEPENDS', 0)):
    main = os.path.join(T, name + '.tsv')
    if not os.path.exists(main): continue
    head, base = rows(main); n_add = n_rep = 0
    for p in sorted(glob.glob(os.path.join(R, '*_' + name + '.tsv'))):
        _, new = rows(p)
        for r in new:
            k = tuple(r[:key]) if key else tuple(r)
            idx = [i for i, b in enumerate(base) if (tuple(b[:key]) if key else tuple(b)) == k]
            w = len(head.split('\t'))
            if name == 'DELIVERABLES' and len(r) < w:  # reader rows lack the later columns (translate_to, why): keep the existing cells
                r = r + (base[idx[0]][len(r):w] if idx and len(base[idx[0]]) >= w else [''] * (w - len(r)))
            if len(r) != w: print('skip (columns)', p, r[:2]); continue
            if idx and key:  # same id (or same stretch): the reader's newer row replaces the old one
                if base[idx[0]] != r: n_rep += 1
                base[idx[0]] = r
            elif not idx: base.append(r); n_add += 1
    with open(main, 'w', encoding='utf-8', newline='\n') as f:
        f.write(head + '\n'); [f.write('\t'.join(r) + '\n') for r in base]
    print(name, 'added', n_add, 'replaced', n_rep)
for p in sorted(glob.glob(os.path.join(R, '*_INTEGRATION.md'))):
    st = os.path.basename(p)[:-len('_INTEGRATION.md')]
    t = open(p, encoding='utf-8').read()
    for sec, target in (('STUDY', 'STUDY.md'), ('HUNCHES', 'HUNCHES.md'), ('PACKAGES', 'RESEARCH_PACKAGES.md')):
        m = re.search(r'(?ms)^## ' + sec + r'\s*\n(.*?)(?=^## (?:STUDY|HUNCHES|PACKAGES)\s*$|\Z)', t)
        if not m or not m.group(1).strip(): continue
        tp = os.path.join(T, target); doc = open(tp, encoding='utf-8').read()
        a, b = f'<!-- reading:{st} -->', f'<!-- /reading:{st} -->'
        block = f'{a}\n### From the reading of {st} (sub-agent; the full reading is readings/{st}.md)\n\n{m.group(1).strip()}\n{b}'
        if a in doc: doc = re.sub(re.escape(a) + r'.*?' + re.escape(b), lambda _: block, doc, flags=re.S)
        else:
            if '## From the sub-agent readings' not in doc: doc = doc.rstrip('\n') + '\n\n## From the sub-agent readings\n'
            doc = doc.rstrip('\n') + '\n\n' + block + '\n'
        open(tp, 'w', encoding='utf-8', newline='\n').write(doc)
        print('merged', st, sec, '->', target)
