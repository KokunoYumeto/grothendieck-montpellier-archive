# Merges the readings of a sweep-3 wave-1 topic into its folder (sweep3/SA<nn>/), in the form of sweep3/SA05/.
# Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026.
# Usage: python -I -B merge_wave1.py SA04 <header.md>
#   header.md: the topic's opening text (title, sources, readers, unread stretches); it heads STUDY.md.
# Tables: every readings/<stretch>_<TABLE>.tsv is concatenated (rows replaced by id where an id repeats).
# Texts: the "## STUDY", "## HUNCHES" and "## PACKAGES" sections of readings/<stretch>_INTEGRATION.md go into STUDY.md,
# HUNCHES.md and RESEARCH_PACKAGES.md, one block per stretch, between <!-- reading:<stretch> --> markers.
import os, re, sys
D = 'C:/Users/user/Documents/results_register/horizontal/sweep3/' + sys.argv[1] + '/'
R = D + 'readings/'
header = open(sys.argv[2], encoding='utf-8').read().rstrip('\n') + '\n'
stretches = sorted({f[:-len('_INTEGRATION.md')] for f in os.listdir(R) if f.endswith('_INTEGRATION.md')})
for T in ('CHECK_EVENTS', 'CORRECTIONS', 'DEPENDS', 'DELIVERABLES'):
    head, rows, seen = None, [], {}
    for s in stretches:
        p = R + s + '_' + T + '.tsv'
        if not os.path.exists(p):
            continue
        lines = [l for l in open(p, encoding='utf-8').read().split('\n') if l.strip()]
        if head is None:
            head = lines[0]
        for l in lines[1:]:
            key = l.split('\t')[0] if T in ('CHECK_EVENTS', 'CORRECTIONS') else l
            if key in seen:
                rows[seen[key]] = l
            else:
                seen[key] = len(rows); rows.append(l)
    with open(D + T + '.tsv', 'w', encoding='utf-8', newline='') as f:
        f.write(head + '\n' + ''.join(r + '\n' for r in rows))
    print(T, len(rows), 'rows')
sec = {'STUDY': [], 'HUNCHES': [], 'PACKAGES': []}
for s in stretches:
    t = open(R + s + '_INTEGRATION.md', encoding='utf-8').read()
    parts = re.split(r'(?m)^## (STUDY|HUNCHES|PACKAGES)\s*$', t)
    for i in range(1, len(parts) - 1, 2):
        sec[parts[i]].append('<!-- reading:%s -->\n### From the reading %s\n\n%s\n<!-- /reading:%s -->\n'
                             % (s, s, parts[i + 1].strip(), s))
title = header.split('\n')[0].lstrip('# ').strip()
open(D + 'STUDY.md', 'w', encoding='utf-8', newline='').write(header + '\n' + '\n'.join(sec['STUDY']))
open(D + 'HUNCHES.md', 'w', encoding='utf-8', newline='').write('# ' + title + ': hunches\n\n' + '\n'.join(sec['HUNCHES']))
open(D + 'RESEARCH_PACKAGES.md', 'w', encoding='utf-8', newline='').write('# ' + title + ': research packages\n\n' + '\n'.join(sec['PACKAGES']))
print('stretches', stretches, '; words', {k: sum(len(x.split()) for x in v) for k, v in sec.items()})
