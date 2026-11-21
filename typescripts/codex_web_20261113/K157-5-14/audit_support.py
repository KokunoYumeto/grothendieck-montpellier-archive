"""Bookkeeping for a completed human visual audit; does not inspect images."""
from pathlib import Path
import re
from workflow import OUT,TASK,utc,log,inventory

def finish(scan, report):
    page=OUT/'pages'/f'{TASK}_157-5_scan{scan:03}.tex'
    s=page.read_text()
    entries=[]
    for m in re.finditer(r'(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
        kind='inline' if m.group(1) is not None else ('display' if m.group(2) is not None else 'diagram')
        value=next(x for x in m.groups() if x is not None)
        entries.append((kind,' '.join(value.split())))
    now=utc()
    with (OUT/f'{TASK}_audit.md').open('a') as f:
        f.write('\n\n### Comparison, corrections, and visual checks\n'+report.strip()+'\n\n### Formula inventory checked against the ink\n')
        for i,(kind,value) in enumerate(entries,1):f.write(f'{i}. {kind}: `{value}`\n')
        if not entries:f.write('none\n')
        f.write('\nEnd: '+now+'\n')
    inventory()
    log(f'scan {scan:03} audited {now}')
    print(f'Scan {scan}: audit saved; {len(entries)} formula/diagram entries; {now}.')
