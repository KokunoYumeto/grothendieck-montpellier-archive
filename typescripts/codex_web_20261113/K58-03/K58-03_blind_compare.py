#!/usr/bin/env python3
"""Compare independent readings with the preserved pre-audit page sources.

Run from any directory. Supply --pages pages and --out another.md to test
later page sources. The anchor list disambiguates differences for which the
blind reading does not occur verbatim on the original page.
"""
import argparse
import csv
from collections import Counter
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parent
def normalize(value):
    value = value.replace('{}', '').replace('$', '').replace('\n',' ').replace('~',' ')
    value = re.sub(r'\\(?:unsure|uline|uuline|inserted|deleted)\{([^{}]*)\}', lambda m:m[1].split('|')[0], value)
    value = re.sub(r'\\(?:longrightarrow|rightarrow)',r'\\to',value)
    value = re.sub(r'\\(?:ast|star)(?![a-zA-Z])','*',value)
    value = re.sub(r'\\(?:,|;|!|quad|qquad)', '', value)
    value = re.sub(r'([_^])\{([^{}])\}', r'\1\2',value)
    return re.sub(r'\s+', '',value)
def table(name):
    p = ROOT/name
    if not p.exists(): return []
    with p.open() as f: return list(csv.DictReader(f,delimiter='\t'))
def esc(t): return t.replace('|',r'\|').replace('\n',' ')
def literal(s):
    s=esc(s)
    longest=max((len(m[0]) for m in re.finditer(chr(96)+'+',s)),default=0)
    fence=chr(96)*(longest+1)
    return fence+' '+s+' '+fence
def compare(pages, only=None):
    anchors={(r['scan'],r['place']):r for r in table('audit/anchors.tsv')}
    report=[];missing=[];tot=0
    for row in table('K58-03_blind.tsv'):
        sn,loc,candidate=row.values()
        if only and sn!=only:continue
        tot+=1
        raw=(pages/f'K58-03_58_scan{int(sn):03}.tex').read_text()
        source=normalize(raw)
        a=anchors.get((sn,loc))
        if a:
            prior=a['first excerpt']
            if prior!='[absent]' and normalize(prior) not in source:
                missing.append((sn,loc,'BASELINE ANCHOR MISSING',prior))
            elif normalize(prior)!=normalize(candidate):
                report.append((sn,loc,prior,candidate,a['decision on ink']))
        elif normalize(candidate) not in source:
            missing.append((sn,loc,'UNLOCATED',candidate))
    return tot,report,missing
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--pages',default='audit/first_pass')
    ap.add_argument('--scan');ap.add_argument('--out',default='K58-03_blind_compare.md')
    args=ap.parse_args()
    total,diffs,pending=compare(ROOT/args.pages,args.scan)
    if args.scan:
        for item in pending:print(*item,sep='\t')
        print(f'{total} readings; {len(diffs)} documented differences; {len(pending)} to locate.')
    else:
        out=['# Blind comparison','',f'Compared {total} independently recorded places with the page files in \x60{args.pages}\x60. {len(diffs)} differences and {len(pending)} unlocated readings.','','A place is a word, sign, phrase, or localized group of marks. The original excerpts and decisions are preserved for the differences. The comparison disregards whitespace, math delimiters, simple editorial wrappers, equivalent lengths of right arrows and single-character subscript braces. It retains differences in letters, pen additions when explicitly marked, order, numbers, and signs. The audit also records corrections elsewhere on the page.','','| Scan | Place | First reading | Blind reading | Decision on the ink |','|---|---|---|---|---|']
        later={(r['scan'],r['place']):r['final collation'] for r in table('audit/blind_followup.tsv')}
        for sn,place,old,blind,disposition in diffs:
            extension=later.get((sn,place),'')
            decision=disposition+' '+extension if extension else disposition
            out.append('| '+' | '.join([sn,esc(place),literal(old),literal(blind),esc(decision)])+' |')
        all_counts=Counter(r['scan'] for r in table('K58-03_blind.tsv'))
        diff_counts=Counter(r[0] for r in diffs)
        out+=['','## Counts by scan','','| Scan | Independently recorded places | Differences itemized above |','|---|---:|---:|']
        out += [f'| {n} | {all_counts[n]} | {diff_counts[n]} |' for n in sorted(all_counts,key=int)]
        out += [f'| **Total** | **{total}** | **{len(diffs)}** |','',
                'A retained uncertainty is a disposition. These counts include differences in the scope of a cancellation, an ink addition, or the way notation was encoded. They do not estimate a lexical error rate. The dated audit and the final witness table preserve the stages of the collation.']
        if pending:
            out += ['','## Unlocated readings','']+[' / '.join(row) for row in pending]
        (ROOT/args.out).write_text('\n'.join(out)+'\n')
        print(f'{total} readings; {len(diffs)} differences; {len(pending)} unlocated.')
        if pending:raise SystemExit(1)
