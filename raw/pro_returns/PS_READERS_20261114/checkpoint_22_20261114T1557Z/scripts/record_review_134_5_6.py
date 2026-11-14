#!/usr/bin/env python3
"""Commit only explicitly authored, visually inspected review records."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
dest=ROOT/'PS_READERS_WORK/review_notes/134_5_6.jsonl'
existing={json.loads(x)['key'] for x in dest.read_text().splitlines() if x.strip()}
records=[]
for file in sys.argv[1:]:
    r=json.loads((ROOT/file).read_text());assert r['key'] not in existing
    assert r['both_halves_viewed'] is True
    s=(ROOT/'inputs/text/transcription/ps_pages'/f"{r['key']}.tex").read_text()
    for old,new,reason in r['changes']:
        assert s.count(old)==1,(r['key'],old,s.count(old));s=s.replace(old,new,1)
    # These exact word selections are supplied only after inspecting their strokes.
    for body in r.pop('hand_underlines',[]):
        token=r'\uline{'+body+'}'
        while True:
            hits=[m for m in re.finditer(re.escape(token),s)
                  if s[max(0,m.start()-6):m.start()]!=r'\hand{']
            if not hits:break
            m=hits[0];a=s.rfind('\n',0,m.start())+1;b=s.find('\n',m.end())
            if b<0:b=len(s)
            old=s[a:b];new=s[a:m.start()]+r'\hand{\uline{\textcolor{black}{'+body+r'}}}'+s[m.end():b]
            assert s.count(old)==1,(r['key'],old)
            r['changes'].append([old,new,'Restore the scan-confirmed handwritten underline; the selected word or phrase is typed.'])
            s=s.replace(old,new,1)
    if r.pop('hand_overlines',False):
        while True:
            hits=[m for m in re.finditer(r'\\overline\{',s)
                  if s[max(0,m.start()-6):m.start()]!=r'\hand{']
            if not hits:break
            m=hits[0];end=m.end();depth=1
            while depth:
                if s[end]=='{' and s[end-1]!='\\':depth+=1
                if s[end]=='}' and s[end-1]!='\\':depth-=1
                end+=1
            a=s.rfind('\n',0,m.start())+1;b=s.find('\n',end)
            if b<0:b=len(s)
            body=s[m.end():end-1]
            old=s[a:b];new=s[a:m.start()]+r'\hand{\overline{\textcolor{black}{'+body+r'}}}'+s[end:b]
            assert s.count(old)==1
            r['changes'].append([old,new,'Restore the scan-confirmed handwritten bar while keeping its typed expression plain.'])
            s=s.replace(old,new,1)
    # The selector list is supplied separately for each already inspected page.
    for token in r.pop('hand_tokens',[]):
        while True:
            hits=[m for m in re.finditer(re.escape(token)+r'(?![A-Za-z])',s)
                  if s[max(0,m.start()-6):m.start()]!=r'\hand{']
            if not hits:break
            m=hits[0];a=s.rfind('\n',0,m.start())+1;b=s.find('\n',m.end())
            if b<0:b=len(s)
            old=s[a:b];new=s[a:m.start()]+r'\hand{'+token+'}'+s[m.end():b]
            assert s.count(old)==1,(r['key'],old)
            r['changes'].append([old,new,'Restore the scan-confirmed handwritten mathematical sign; the typed terms remain plain.'])
            s=s.replace(old,new,1)
    records.append(r);existing.add(r['key'])
with dest.open('a') as f:
    for r in records:f.write(json.dumps(r)+'\n')
