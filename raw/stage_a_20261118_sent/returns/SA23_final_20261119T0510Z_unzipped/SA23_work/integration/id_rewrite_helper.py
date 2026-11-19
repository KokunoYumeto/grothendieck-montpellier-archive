"""Expand existing SA23 citation shorthand before applying canonical aliases.

This module performs no filesystem reads or writes when imported.

Recommended integration:
    from id_rewrite_helper import rewrite_ids
    known_ids = {x['id'] for rows in original.values() for x in rows}
    def rewrite_text(text):
        return rewrite_ids(text, aliases, known_ids)

The default expands owner-qualified problem IDs only. Pass
``kinds=('problem', 'claim', 'item')`` to safely normalize all three citation
families before merges. Every inferred tail and every member of an inferred
range must exist in known_ids (or alias keys). Unknown years and prose numbers
are left alone. A bare comma-number followed by a word is treated as prose,
even if that number happens to name a known problem; explicit dash ranges
following a full ID do not have that ambiguity.

Run this file with --test to execute its bounded unit and corpus checks. The
test routine reads source-owner registers/sections and writes only the two
requested integration QA output files, never the finalizer or owner files.
"""
from __future__ import annotations
import re
from collections import defaultdict
from functools import lru_cache

_FULL = re.compile(
    r'(?<![A-Za-z0-9_-])'
    r'(?P<full>(?P<prefix>MP-SA23-[a-z_]+-|C-SA23-[a-z_]+-|SA23-)'
    r'(?P<number>\d+)(?P<suffix>[A-Za-z]?))'
    r'(?![A-Za-z0-9_-])'
)
# ASCII '-' is allowed as a numeric range separator, but a full ID immediately
# followed by '-' is excluded above unless we recognize that range explicitly.
_FULL_RANGE_START = re.compile(
    r'(?<![A-Za-z0-9_-])'
    r'(?P<full>(?P<prefix>MP-SA23-[a-z_]+-|C-SA23-[a-z_]+-|SA23-)'
    r'(?P<number>\d+)(?P<suffix>[A-Za-z]?))'
    r'(?=$|[^A-Za-z0-9_-]|-\d)'
)
_RANGE = re.compile(r'\s*[–—-]\s*(?P<number>\d+)(?P<suffix>[A-Za-z]?)(?![A-Za-z0-9_-])')
_TAIL = re.compile(r'(?P<separator>,\s*|\s+and\s+)(?:-\s*)?(?P<number>\d+)(?P<suffix>[A-Za-z]?)(?=$|[^A-Za-z0-9_-]|-\d)')

def _kind(prefix: str) -> str:
    return 'problem' if prefix.startswith('MP-') else ('claim' if prefix.startswith('C-') else 'item')

def _citation_tail_boundary(text: str, pos: int) -> bool:
    """Reject e.g. ', 27 examples' while accepting a citation cluster's end."""
    rest=text[pos:]
    if not rest:return True
    # A physical newline ends the citation; never consume numbers in a new row.
    if re.match(r'[ \t]*\n',rest):return True
    rest=rest.lstrip(' \t')
    return (not rest or rest[0] in ',;.:)]}|`$' or
            bool(re.match(r'and\s+-?\s*\d',rest)))

@lru_cache(maxsize=16)
def _registered_index(known):
    index=defaultdict(set)
    for ident in known:
        m=_FULL.fullmatch(ident)
        if m:index[(m['prefix'],int(m['number']),m['suffix'])].add(ident)
    return index

@lru_cache(maxsize=16)
def _alias_pattern(keys):
    return re.compile(r'(?<![A-Za-z0-9_-])(?:'+'|'.join(re.escape(k) for k in sorted(keys,key=len,reverse=True))+r')(?![A-Za-z0-9_-])')

def expand_compact_ids(text: str, known_ids, *, kinds=('problem',), with_events=False):
    """Expand only registered shorthand IDs, returning text or (text, events).

    Examples: owner-08–11,27; owner-04, -06, -07; owner-06,09.
    Full repeated prefixes are already unambiguous and need no normalization.
    Suffix-bearing claim IDs can occur as individual tails but are not treated
    as numeric range endpoints. No historic/source text needs to be passed here.
    """
    if 'SA23-' not in text:return (text,[]) if with_events else text
    known=frozenset(known_ids)
    index=_registered_index(known)
    allowed=set(kinds)
    events=[]

    def lookup(prefix,number,suffix=''):
        values=index.get((prefix,int(number),suffix),set())
        return next(iter(values)) if len(values)==1 else None

    def range_ids(prefix,start,end,start_suffix='',end_suffix=''):
        if start_suffix or end_suffix or end<start:return None
        # No attempted expansion can be longer than the actual identifier set.
        if end-start+1>len(known):return None
        values=[lookup(prefix,n) for n in range(start,end+1)]
        return values if all(values) else None

    out=[];last=0;scan=0
    while True:
        m=_FULL_RANGE_START.search(text,scan)
        if not m:break
        scan=m.end()
        if m['full'] not in known or _kind(m['prefix']) not in allowed:continue
        prefix=m['prefix'];ids=[m['full']];pos=m.end();changed=False

        # An explicit full-ID range may be followed by ordinary prose.
        r=_RANGE.match(text,pos)
        if r:
            expanded=range_ids(prefix,int(m['number']),int(r['number']),m['suffix'],r['suffix'])
            if expanded:
                ids=expanded;pos=r.end();changed=True

        while True:
            tail=_TAIL.match(text,pos)
            if not tail:break
            # Do not infer an ID across a newline hidden in comma whitespace.
            if '\n' in tail['separator']:break
            ident=lookup(prefix,tail['number'],tail['suffix'])
            if not ident:break
            new_ids=[ident];end=tail.end()
            r=_RANGE.match(text,end)
            if r:
                expanded=range_ids(prefix,int(tail['number']),int(r['number']),tail['suffix'],r['suffix'])
                if not expanded:break
                new_ids=expanded;end=r.end()
            if not _citation_tail_boundary(text,end):break
            ids.extend(new_ids);pos=end;changed=True

        if changed:
            replacement=', '.join(ids)
            out.extend([text[last:m.start()],replacement]);last=pos;scan=pos
            events.append({'start':m.start(),'end':pos,'original':text[m.start():pos],
                           'expanded':replacement,'ids':ids,'kind':_kind(prefix)})
    out.append(text[last:])
    result=''.join(out)
    return (result,events) if with_events else result

def rewrite_ids(text: str, aliases, known_ids=(), *, kinds=('problem',)) -> str:
    """Expand registered shorthand, then replace complete IDs via resolved aliases.

    Alias values may be a string or a list. Alias chains should be resolved by
    the caller, as in finalize_dossier.py's existing resolve function.
    """
    if 'SA23-' not in text:return text
    text=expand_compact_ids(text,frozenset(known_ids)|frozenset(aliases),kinds=kinds)
    if not aliases:return text
    pattern=_alias_pattern(frozenset(aliases))
    def replace(m):
        # An unexpanded numeric range has an unregistered/ambiguous member.
        # Keep its original owner prefix instead of producing a false global
        # range such as MP-SA23-105–99. The alias ledger still resolves the head.
        if _RANGE.match(text,m.end()):return m.group()
        tail=_TAIL.match(text,m.end())
        if tail and _citation_tail_boundary(text,tail.end()):return m.group()
        values=aliases[m.group()]
        return values if isinstance(values,str) else ', '.join(values)
    return pattern.sub(replace,text)

def run_tests(workspace=None):
    import json
    from pathlib import Path
    w=Path(workspace) if workspace else Path(__file__).resolve().parents[1]
    # Deliberately synthetic global targets: these do not assert final numbering.
    aliases={f'MP-SA23-ega-{n:02}':[f'MP-SA23-{n+100:03}'] for n in range(1,60)}
    known=set(aliases)
    cases=[
      ('[MP-SA23-ega-06,09; ref]', '[MP-SA23-106, MP-SA23-109; ref]'),
      ('(MP-SA23-ega-04, -06, -07).','(MP-SA23-104, MP-SA23-106, MP-SA23-107).'),
      ('MP-SA23-ega-08–11,27;', 'MP-SA23-108, MP-SA23-109, MP-SA23-110, MP-SA23-111, MP-SA23-127;'),
      ('MP-SA23-ega-08–11, -27–30;', 'MP-SA23-108, MP-SA23-109, MP-SA23-110, MP-SA23-111, MP-SA23-127, MP-SA23-128, MP-SA23-129, MP-SA23-130;'),
      ('MP-SA23-ega-05, 2026 is the audit year.','MP-SA23-105, 2026 is the audit year.'),
      ('MP-SA23-ega-05, 27 examples follow.','MP-SA23-105, 27 examples follow.'),
      ('MP-SA23-ega-05, 27–30 examples follow.','MP-SA23-105, 27–30 examples follow.'),
      ('MP-SA23-ega-05–07 gives the criterion.','MP-SA23-105, MP-SA23-106, MP-SA23-107 gives the criterion.'),
      ('MP-SA23-ega-05-07;','MP-SA23-105, MP-SA23-106, MP-SA23-107;'),
      ('MP-SA23-ega-05 and -07.','MP-SA23-105, MP-SA23-107.'),
      ('MP-SA23-ega-05,\n27 examples follow.','MP-SA23-105,\n27 examples follow.'),
      ('notMP-SA23-ega-05,09;','notMP-SA23-ega-05,09;'),
      ('MP-SA23-ega-05–99;', 'MP-SA23-ega-05–99;'),
      ('MP-SA23-ega-05, -07-09;', 'MP-SA23-105, MP-SA23-107, MP-SA23-108, MP-SA23-109;'),
      ('MP-SA23-ega-05,99;', 'MP-SA23-ega-05,99;'),
    ]
    checks=[]
    for inp,expected in cases:
        actual=rewrite_ids(inp,aliases,known)
        checks.append({'input':inp,'expected':expected,'actual':actual,'passed':actual==expected})
    # Missing intermediate registered ID must prevent expanding an entire range.
    gap=known-{'MP-SA23-ega-06'}
    expanded=expand_compact_ids('MP-SA23-ega-05–07;',gap)
    checks.append({'input':'MP-SA23-ega-05–07; with06 absent','expected':'MP-SA23-ega-05–07;','actual':expanded,'passed':expanded=='MP-SA23-ega-05–07;'})
    # Merge-sensitive claim ranges are safe only when all claim IDs are supplied.
    cknown={f'C-SA23-hyp-{n:03}' for n in range(1,4)}
    ca={'C-SA23-hyp-001':['C-SA23-forms-011'],'C-SA23-hyp-002':['C-SA23-forms-012']}
    actual=rewrite_ids('[C-SA23-hyp-001–003]',ca,cknown,kinds=('claim',))
    expected='[C-SA23-forms-011, C-SA23-forms-012, C-SA23-hyp-003]'
    checks.append({'input':'[C-SA23-hyp-001–003] with first two claims merged','expected':expected,'actual':actual,'passed':actual==expected})

    actual_ids=set()
    for p in (w/'parts').glob('*/problems.json'):
        actual_ids.update(x['id'] for x in json.loads(p.read_text()))
    for p in (w/'parts').glob('*/claims.json'):
        actual_ids.update(x['id'] for x in json.loads(p.read_text()))
    for p in (w/'parts').glob('*/items.json'):
        actual_ids.update(x['id'] for x in json.loads(p.read_text()))
    paths=sorted((w/'parts').glob('*/section.md'))+[w/'integration/overview.md']
    corpus=[];all_events=[];dangling=[]
    for p in paths:
        text=p.read_text()
        expanded,events=expand_compact_ids(text,actual_ids,with_events=True)
        twice,more=expand_compact_ids(expanded,actual_ids,with_events=True)
        for e in events:
            e['file']=str(p.relative_to(w));e['line']=text[:e['start']].count('\n')+1
            all_events.append(e)
        if more or twice!=expanded:dangling.append({'file':str(p),'events':more})
        # Independent raw-pattern audit for residual compact problem tails.
        raw=re.compile(r'MP-SA23-[a-z_]+-\d+(?:\s*[–—-]\s*\d+)?(?:,\s*-?\d+(?:\s*[–—-]\s*\d+)?)+')
        for m in raw.finditer(expanded):
            residual,es=expand_compact_ids(m.group(),actual_ids,with_events=True)
            if es:dangling.append({'file':str(p),'residual':m.group(),'expands_to':residual})
        corpus.append({'file':str(p.relative_to(w)),'expansions':len(events),'idempotent':twice==expanded})
    result={'unit_tests':checks,'unit_failures':sum(not x['passed'] for x in checks),'files_checked':len(corpus),'corpus':corpus,'current_section_expansions':all_events,'dangling_valid_compact_tails':dangling,'note':'Synthetic aliases are unit-test fixtures only. No final numbering is inferred before the consolidation plan is available. No owner/finalizer file was changed.'}
    (w/'integration/id_rewrite_helper_tests.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['unit_failures','files_checked','dangling_valid_compact_tails']}))
    assert not result['unit_failures'] and not dangling,result
    return result

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--test',action='store_true');args=parser.parse_args()
    if args.test:run_tests()
