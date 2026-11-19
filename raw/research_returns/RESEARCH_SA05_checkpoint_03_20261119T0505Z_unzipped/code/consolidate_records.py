#!/usr/bin/env python3
"""Consolidate current source bibliographies, numbered statements and events.

Individual part ledgers are retained.  This script does not promote an open
item to proved: the canonical index takes the scoped status in its TeX source.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]

def aliases():
    path=ROOT/'part_d/bibliography_alias_suggestions.tsv'
    if not path.exists():return {}
    with path.open(newline='') as f:
        return {r['duplicate_key']:r['canonical_key'] for r in csv.DictReader(f,delimiter='\t')}


def group(text,start,left='{',right='}'):
    assert text[start]==left
    depth=1;i=start+1
    while i<len(text):
        if text[i]=='\\':i+=2;continue
        if text[i]==left:depth+=1
        elif text[i]==right:
            depth-=1
            if not depth:return text[start+1:i],i+1
        i+=1
    raise ValueError('Unclosed group')


def field(entry,name):
    match=re.search(r'\b'+re.escape(name)+r'\s*=\s*\{',entry,re.I)
    if not match:return ''
    return group(entry,entry.index('{',match.start()))[0]

def set_field(entry,name,value):
    match=re.search(r'\b'+re.escape(name)+r'\s*=\s*\{',entry,re.I)
    if match:
        a=entry.index('{',match.start());_,b=group(entry,a)
        return entry[:a+1]+value+entry[b-1:]
    return entry[:-1].rstrip().rstrip(',')+',\n '+name+'={'+value+'}}'

def bibliography():
    paths=['part_a/references.bib','part_b/part_b_sources.bib',
           'part_b/b4_algorithm.bib','part_b/b3_singular.bib',
           'part_c/references.bib','part_d/part_d.bib',
           'part_d/contextual_sources.bib']
    raw={};duplicates=[];alias=aliases()
    for rel in paths:
        text=(ROOT/rel).read_text()
        for match in re.finditer(r'@\w+\s*\{',text):
            opening=text.index('{',match.start())
            body,end=group(text,opening)
            key=body.split(',',1)[0].strip()
            entry=text[match.start():end]
            if key in raw:
                duplicates.append(key);continue
            raw[key]=entry
    buckets={}
    for key in raw:buckets.setdefault(alias.get(key,key),[]).append(key)
    records={};merged={}
    for canonical,keys in buckets.items():
        base=raw[canonical] if canonical in raw else raw[keys[0]]
        base=re.sub(r'^(@\w+\s*\{)[^,]+',lambda m:m.group(1)+canonical,base,count=1)
        notes=list(dict.fromkeys(field(raw[k],'note') for k in keys if field(raw[k],'note')))
        value=' '.join(notes)
        def wrap(m):
            if value[max(0,m.start()-5):m.start()]=='\\url{':return m.group()
            url=m.group().rstrip('.,;')
            return '\\url{'+url+'}'+m.group()[len(url):]
        value=re.sub(r'https?://[^\s{}]+',wrap,value)
        records[canonical]=set_field(base,'note',value)
        if len(keys)>1:merged[canonical]=keys
    (ROOT/'RESEARCH_SA05_references.bib').write_text('\n\n'.join(records.values())+'\n')
    return dict(bibliography_entries=len(records),duplicate_keys_skipped=duplicates,duplicate_works_merged=merged)

def literature():
    """Preserve primary-source opening evidence while normalizing part schemas."""
    alias=aliases();records={};by_url={}
    bib=(ROOT/'RESEARCH_SA05_references.bib').read_text()
    for match in re.finditer(r'@\w+\s*\{',bib):
        opening=bib.index('{',match.start());body,end=group(bib,opening)
        key=body.split(',',1)[0].strip();entry=bib[match.start():end]
        note=field(entry,'note');url=field(entry,'url')
        status='not obtained' if re.search(r'not (?:opened|obtained)',note,re.I) else ('opened' if re.search(r'opened',note,re.I) else 'opening annotation pending')
        records[key]=dict(source=key,title=field(entry,'title'),status=status,url_or_path=url,
                          exact_locator=note,retrieval_evidence='Annotated owner bibliography',use_or_attempt='See exact locator and item proof scope')
        if url:by_url.setdefault(url.rstrip('/'),[]).append(key)
    inputs=[('B','part_b/part_b_LITERATURE_CHECK.tsv'),('C','part_c/sources.tsv'),
            ('D','part_d/LITERATURE_CHECK.tsv')]
    def add(a,b):return '; '.join(dict.fromkeys(x for x in [a,b] if x))
    for owner,rel in inputs:
        path=ROOT/rel
        if not path.exists():continue
        with path.open(newline='') as f:
            for row in csv.DictReader(f,delimiter='\t'):
                raw=row.get('source',row.get('key',''));url=row.get('url_or_path',row.get('url',''))
                candidates=[raw,owner+raw,'c_'+raw]
                key=next((alias.get(k,k) for k in candidates if alias.get(k,k) in records),None)
                if key is None and len(by_url.get(url.rstrip('/'),[]))==1:key=by_url[url.rstrip('/')][0]
                if key is None:key=alias.get(raw,raw)
                mapped=dict(source=key,title=row.get('title',''),status=row.get('status',''),url_or_path=url,
                    exact_locator=row.get('exact_locator',row.get('locators',row.get('exact_results',''))),
                    retrieval_evidence=add(rel,row.get('retrieval','')),
                    use_or_attempt=row.get('use_or_attempt',row.get('use_or_limitation','')))
                if key not in records:records[key]=mapped
                else:
                    for name,value in mapped.items():
                        if name!='source':records[key][name]=add(records[key][name],value)
    for rel in ['part_d/literature_title_supplement.tsv','ROOT_LITERATURE_TITLES.tsv']:
        supplement=ROOT/rel
        if supplement.exists():
            with supplement.open(newline='') as f:
                for row in csv.DictReader(f,delimiter='\t'):
                    key=alias.get(row['source'],row['source'])
                    if key in records and not records[key]['title']:records[key]['title']=row['title']
    fields=['source','title','status','url_or_path','exact_locator','retrieval_evidence','use_or_attempt']
    with (ROOT/'LITERATURE_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(records.values())
    return dict(literature_records=len(records),literature_annotation_gaps=[k for k,r in records.items() if 'pending' in r['status']])


def expand(path):
    text=path.read_text()
    pattern=re.compile(r'\\input\{([^}]+)\}')
    result=[];last=0
    for match in pattern.finditer(text):
        result.append((path,text[last:match.start()]))
        child=ROOT/match.group(1)
        if not child.suffix:child=child.with_suffix('.tex')
        result.extend(expand(child));last=match.end()
    result.append((path,text[last:]))
    return result


def statements():
    metadata=[]
    for rel in ['part_b/part_b_results.csv','part_c/results.csv','part_d/results.csv']:
        with (ROOT/rel).open(newline='') as f:metadata.extend(csv.DictReader(f))
    numbers={}
    aux=ROOT/'build/RESEARCH_SA05_paper.aux'
    if aux.exists():
        for match in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux.read_text()):
            numbers[match.group(1)]=(match.group(2),match.group(3))
    rows=[];warnings=[]
    pattern=re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|definition|example|question|remark)\}')
    for part in 'abcd':
        for path,text in expand(ROOT/f'sections/part_{part}.tex'):
            for match in pattern.finditer(text):
                env=match.group(1);pos=match.end()
                while pos<len(text) and text[pos].isspace():pos+=1
                title=''
                if text[pos:pos+1]=='[':title,pos=group(text,pos,'[',']')
                end=text.index('\\end{'+env+'}',pos)
                body=text[pos:end]
                label=re.search(r'\\label\{([^}]+)\}',body)
                if label:identifier=label.group(1)
                else:
                    identifier=part.upper()+':unlabelled:'+hashlib.sha256((env+title+body).encode()).hexdigest()[:10]
                    warnings.append('Missing stable label: '+identifier+' '+title)
                matches=[r for r in metadata if r['id']==identifier or identifier in r.get('where_proved','')]
                statusmatch=re.search(r'\\status\s*\{',body)
                if statusmatch:
                    opening=body.index('{',statusmatch.start());status,stop=group(body,opening)
                    body=body[:statusmatch.start()]+body[stop:]
                elif matches:status=matches[0]['status']
                else:
                    status='Definition' if env=='definition' else 'Status annotation pending'
                    warnings.append('Missing scoped status: '+identifier)
                body=re.sub(r'\\label\{[^}]+\}','',body)
                body=re.sub(r'%[^\n]*','',body)
                statement=re.sub(r'\s+',' ',(title+': ' if title else '')+body).strip()
                deps=sorted(set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',body))-{identifier})
                loc=f'{env.title()} {numbers.get(identifier,("pending build",))[0]}; {path.relative_to(ROOT)}'
                pages='; '.join(dict.fromkeys(r['manuscript_pages_settled'] for r in matches))
                if part=='a':pages='15:2–14'
                notes='; '.join(dict.fromkeys(r['notes'] for r in matches))
                rows.append(dict(id=identifier,statement=statement,status=status,where_proved=loc,
                                 depends_on=';'.join(deps),manuscript_pages_settled=pages,
                                 notes=notes or 'Scoped statement status; consult the item ledger for the original task.'))
    fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
    assert len({r['id'] for r in rows})==len(rows),'Duplicate theorem labels'
    with (ROOT/'RESEARCH_SA05_results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    return dict(numbered_statements=len(rows),index_warnings=warnings)


def events():
    paths=['part_a/check_events.tsv','part_b/part_b_CHECK_EVENTS.tsv',
           'part_c/CHECK_EVENTS.tsv','part_d/CHECK_EVENTS.tsv']
    extra=ROOT/'ROOT_CHECK_EVENTS.tsv'
    if extra.exists():paths.append('ROOT_CHECK_EVENTS.tsv')
    rows=[];seen=set()
    fields=['statement_id','date','who','type','outcome']
    for rel in paths:
        with (ROOT/rel).open(newline='') as f:
            for row in csv.DictReader(f,delimiter='\t'):
                key=tuple(row.get(k,'') for k in fields)
                if key not in seen:rows.append(dict(zip(fields,key)));seen.add(key)
    crosswalk=ROOT/'part_d/statement_label_crosswalk.tsv'
    if crosswalk.exists():
        with crosswalk.open(newline='') as f:
            for row in csv.DictReader(f,delimiter='\t'):
                linked=dict(statement_id=row['exact_label'],date=row['date'],who=row['who'],
                            type=row['type'],outcome=row['outcome'])
                key=tuple(linked[k] for k in fields)
                if key not in seen:rows.append(linked);seen.add(key)
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    return dict(check_events=len(rows),explicit_cross_reference_records=sum('cross-reference' in r['outcome'].lower() or 'cross reference' in r['outcome'].lower() for r in rows))


result=bibliography()
if '--bib-only' not in sys.argv:
    result.update(statements());result.update(events());result.update(literature())
(ROOT/'code/consolidate_records_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
