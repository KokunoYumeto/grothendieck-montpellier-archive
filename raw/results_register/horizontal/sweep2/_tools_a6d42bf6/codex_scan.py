# Compact view of Codex sheet-note gap entries of a topic (agent a6d42bf6, horizontal sweep 2)
# usage: python -I -B codex_scan.py SA04 [n1] [n2]
import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gap_tools import gap, flat
topic = sys.argv[1]; n1 = int(sys.argv[2]) if len(sys.argv) > 2 else 170; n2 = int(sys.argv[3]) if len(sys.argv) > 3 else 150
MON = r'(?:janv|févr|fevr|mars|avril|avr|mai|juin|juil|août|aout|sept|oct|nov|déc|dec)[a-zéû]*\.?'
for g in gap(topic):
    if not g['entry_id'].startswith('codex:'): continue
    b = flat(g['body'])
    if g['heading'].lower().startswith(('tit', 'titles')):
        dates = sorted(set(re.findall(r'\b\d{1,2}\.?\s*' + MON + r'\s*(?:19)?\d{0,2}|\b(?:19[4-9]\d)\b|\b\d{1,2}\.\d{1,2}\.\d{2}\b', b, re.I)))[:6]
        quotes = re.findall(r'[“«"]([^”»"]{4,80})[”»"]', b)[:3]
        print(f"{g['entry_id']}|T|{g['words']}w|dates={dates}|q={quotes}|{b[:n2] if not quotes else ''}")
    else:
        neg = bool(re.match(r'(none|no step|aucun|nothing)', b, re.I)) or b.lower().startswith('none')
        hot = re.findall(r'(faux|erreur|C.est faux|incorrect|false|wrong|contradict)', b, re.I)
        print(f"{g['entry_id']}|S|{g['words']}w|{'NONE ' if neg else ''}{'HOT:' + ','.join(sorted(set(h.lower() for h in hot))) + ' ' if hot else ''}|{b[:n1]}")
