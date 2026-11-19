# Copy one cote's rows of a reader's SA04 tables into another topic's readings (wave 1, agent a6d42bf6, 19 Nov 2026).
# usage: python -I -B copy_cote_rows.py <src_readings_prefix> <dst_readings_prefix> <cote>
# CHECK_EVENTS/CORRECTIONS: rows whose id has -R<cote>- or -K<cote>-; DEPENDS: rows whose item or where names
# SA01-*/cote <cote> pages (<cote>/...); DELIVERABLES: the row whose cote_part is <cote>. Header kept; nothing else changed.
import io, re, sys
src, dst, cote = sys.argv[1], sys.argv[2], sys.argv[3]
pat_id = re.compile(r'-(R|K)%s-' % re.escape(cote))
pat_pg = re.compile(r'(^|[^0-9])%s/[0-9]' % re.escape(cote))
for tab in ('CHECK_EVENTS', 'CORRECTIONS', 'DEPENDS', 'DELIVERABLES'):
    lines = io.open(f'{src}_{tab}.tsv', encoding='utf-8').read().splitlines()
    head, rows = lines[0], lines[1:]
    if tab in ('CHECK_EVENTS', 'CORRECTIONS'):
        keep = [r for r in rows if pat_id.search(r.split('\t')[0])]
    elif tab == 'DEPENDS':
        keep = [r for r in rows if pat_pg.search(r) or re.search(r'SA01-(1|3|4|6)\b', r.split('\t')[0])]
    else:
        keep = [r for r in rows if r.split('\t')[0].strip() == cote]
    io.open(f'{dst}_{tab}.tsv', 'w', encoding='utf-8', newline='\n').write('\n'.join([head] + keep) + '\n')
    print(tab, len(keep))
