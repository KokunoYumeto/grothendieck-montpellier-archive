#!/usr/bin/env python3
"""Read-only structural validation of the consolidated SA05 deliverable.

Usage:
  python SA05/programs/validate_final.py --draft
  python SA05/programs/validate_final.py
  python SA05/programs/validate_final.py --archive SA05.zip

Only programs/outputs/validate_final[_draft].{json,txt} are written. The
validator never changes a source, verdict, mathematical claim or top-level
deliverable. It checks recorded relationships and coverage, not the truth of
mathematics or whether a human/model actually read an exposed passage.

Draft mode reports missing final prose and specifically documented pending
refinement integrations as PENDING. Other integrity failures remain errors.
Strict mode is the default. External source access is never retried here.
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
WORKSPACE = BASE.parent
OUT = BASE / 'programs' / 'outputs'

REQUIRED = [
    'SA05_dossier.md', 'SA05_entries.tsv', 'SA05_items.json',
    'SA05_claims.json', 'SA05_problems.json', 'SA05_readings.tsv',
    'SA05_links.tsv', 'SA05_directions.md', 'SA05_references.bib',
    'CHECK_EVENTS.tsv', 'progress.log',
]
SUPPORT = [
    'SA05_aliases.json', 'reference_aliases.json', 'SA05_reference_ledger.json',
    'SA05_reference_ledger.tsv', 'SA05_searches.tsv', 'SA05_project_leads.tsv',
    'SA05_unavailable_archive_leads.tsv', 'SA05_unverified_reference_leads.tsv', 'counts.json',
]
FINAL_PROSE = {'SA05_dossier.md', 'SA05_directions.md'}
TSV_FIELDS = {
    'SA05_entries.tsv': ['entry_id','item_id','verdict','reason'],
    'SA05_readings.tsv': ['cote','scan','line','reading','alternative','evidence','weight','confidence'],
    'SA05_links.tsv': ['kind','from','to','what','evidence','note_ids'],
    'SA05_project_leads.tsv': ['kind','from','to','what','evidence','note_ids'],
    'SA05_unverified_reference_leads.tsv': ['kind','from','to','what','evidence','note_ids'],
    'SA05_unavailable_archive_leads.tsv': ['kind','from','to','what','evidence','note_ids','run_names','status'],
    'CHECK_EVENTS.tsv': ['statement_id','date','who','type','outcome'],
    'SA05_searches.tsv': ['scope','search_id','claim_ids','record_json'],
    'SA05_reference_ledger.tsv': ['key','title','year','url','note','aliases','witness_count','checked_scopes'],
}
JSON_FIELDS = {
    'items': ['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
    'claims': ['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
    'problems': ['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'],
}
ITEM_KINDS = {'conjecture','unproved claim','unpursued implication','idea of the earlier run',
              'reading question','self-flagged step','withdrawn in the same text',
              'title, date or page count','other'}
ITEM_CHECKS = {'agrees','overstates','understates','misreads','not on the page'}
VERDICTS = {'kept','merged','merged into item','corrected','withdrawn','rests on a misreading'}
EVENT_TYPES = {'targeted proof check','independent re-proof','computation or formal certificate',
               'used and rechecked in this run','carried as background without fault found',
               "refuted, with the refined statement's id"}
ID_PATTERNS = {'items':r'SA05-\d+', 'claims':r'SA05-C\d+', 'problems':r'MP-SA05-\d+'}
ID_RE = re.compile(r'(?<![A-Za-z0-9_])(?:MP-SA05-\d+|SA05-C\d+|SA05-\d+)(?![A-Za-z0-9_-])')
ENTRY_RE = re.compile(r'MPL_\d+_[0-9+_-]+#\d+')
CLAIM_TOKEN_RE = re.compile(r'SA05-C\d+(?:\.[A-Za-z_][A-Za-z_0-9]*)?')
AUDIT_FIELDS = {'aliases','source_occurrences','parallel_formulations','source_partition_notes',
                'original_source_attribution','inherited_search_ids','source_search_records',
                'premerge_statement_id','original_ids','old_ids'}


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def parse_bib(text):
    """Parse the generated BibTeX, respecting nested braces and escapes."""
    out = []
    pos = 0
    while (m := re.search(r'@(\w+)\s*\{\s*([^,\n]+),', text[pos:])):
        kind, key = m.group(1), m.group(2).strip()
        i = pos + m.end()
        fields = {}
        while True:
            while i < len(text) and (text[i].isspace() or text[i] == ','):
                i += 1
            if i >= len(text):
                raise ValueError('Unclosed BibTeX record ' + key)
            if text[i] == '}':
                i += 1
                break
            fm = re.match(r'([A-Za-z_][\w-]*)\s*=\s*', text[i:])
            if not fm:
                raise ValueError('Invalid field in ' + key + ': ' + text[i:i+60])
            field = fm.group(1)
            i += fm.end()
            if i >= len(text):
                raise ValueError('Missing value in ' + key)
            if text[i] == '{':
                i += 1
                start, depth = i, 1
                while depth:
                    if i >= len(text):
                        raise ValueError('Unclosed field ' + key + '.' + field)
                    if text[i] == '\\':
                        i += 2
                        continue
                    if text[i] == '{': depth += 1
                    elif text[i] == '}': depth -= 1
                    i += 1
                value = text[start:i-1]
            elif text[i] == '"':
                i += 1
                start = i
                while i < len(text) and text[i] != '"':
                    i += 2 if text[i] == '\\' else 1
                if i >= len(text): raise ValueError('Unclosed quote in ' + key)
                value = text[start:i]
                i += 1
            else:
                start = i
                while i < len(text) and text[i] not in ',}': i += 1
                value = text[start:i].strip()
            if field in fields:
                raise ValueError('Duplicate field ' + key + '.' + field)
            fields[field] = value
        out.append({'key':key,'entry_type':kind,**fields})
        pos = i
    return out


class Audit:
    def __init__(self, draft=False, archive=None):
        self.draft, self.archive = draft, archive
        self.issues, self.raw, self.data = [], {}, {}
        self.details = {}
        self.metrics = {}
        self.aliases = {}
        self.refaliases = {}
        self.indexes = {}
        self.original_ids = set()
        self.pending_pairs = {}
        self.refkeys = set()
        self.expected_entries = set()

    def issue(self, code, message, *, severity='error', pending=False, **context):
        if pending and self.draft: severity = 'pending'
        self.issues.append({'severity':severity,'code':code,'message':message,**context})

    def load(self):
        for name in REQUIRED + SUPPORT:
            path = BASE / name
            if not path.is_file():
                self.issue('missing_file','Required deliverable/support file is absent.',file=name,
                           pending=name in FINAL_PROSE)
                continue
            blob = path.read_bytes()
            self.raw[name] = blob
            if not blob.strip():
                self.issue('empty_file','Deliverable is empty.',file=name,pending=name in FINAL_PROSE)
                continue
            try:
                text = blob.decode('utf-8-sig')
                if name.endswith('.json'):
                    self.data[name] = json.loads(text)
                elif name.endswith('.tsv'):
                    reader = csv.DictReader(io.StringIO(text,newline=''),delimiter='\t')
                    rows = list(reader)
                    self.data[name] = rows
                    expected = TSV_FIELDS[name]
                    if reader.fieldnames != expected:
                        self.issue('tsv_schema','TSV columns/order differ from the declared schema.',
                                   file=name,actual=reader.fieldnames,expected=expected)
                    for n,row in enumerate(rows,2):
                        if None in row or any(v is None for v in row.values()):
                            self.issue('tsv_width','Row has extra or missing cells.',file=name,row=n)
                elif name.endswith('.bib'):
                    self.data[name] = parse_bib(text)
                else:
                    self.data[name] = text
            except (UnicodeError,ValueError,csv.Error) as exc:
                self.issue('parse_error',str(exc),file=name)
        self.details['input_snapshot'] = {n:{'bytes':len(b),'sha256':sha(b)} for n,b in self.raw.items()}

    def rows(self,name):
        value = self.data.get(name,[])
        return value if isinstance(value,list) else []

    def canonical(self, value, references=False):
        mapping = self.refaliases if references else self.aliases
        seen = set()
        while value in mapping:
            if value in seen:
                self.issue('alias_cycle','Alias cycle.',value=value,references=references)
                return value
            seen.add(value)
            value = mapping[value]
        return value

    def schemas_and_aliases(self):
        config = self.data.get('SA05_aliases.json',{})
        refconfig = self.data.get('reference_aliases.json',{})
        self.refaliases = refconfig.get('aliases',refconfig) if isinstance(refconfig,dict) else {}
        for kind,fields in JSON_FIELDS.items():
            name = 'SA05_' + kind + '.json'
            rows = self.rows(name)
            if not isinstance(self.data.get(name),list):
                self.issue('json_schema','Top-level JSON must be a list.',file=name)
            ids = []
            for n,record in enumerate(rows):
                if not isinstance(record,dict):
                    self.issue('json_record','Record must be an object.',file=name,row=n)
                    continue
                ident = record.get('id','')
                ids.append(ident)
                missing = [f for f in fields if f not in record]
                if missing: self.issue('required_fields','Required fields absent.',file=name,id=ident,missing=missing)
                if not isinstance(ident,str) or not re.fullmatch(ID_PATTERNS[kind],ident):
                    self.issue('id_format','Invalid record ID.',file=name,id=ident)
                for f in fields:
                    if f not in record: continue
                    value = record[f]
                    listfields = {'sources','items','scans','lines','refs','occurrences'}
                    if f in listfields:
                        if not isinstance(value,list): self.issue('field_type','Expected a list.',file=name,id=ident,field=f)
                    elif f == 'cote':
                        if not isinstance(value,(str,int,list)): self.issue('field_type','Invalid cote type.',file=name,id=ident)
                    elif f == 'computation':
                        if not isinstance(value,(str,dict,list)): self.issue('field_type','Invalid computation type.',file=name,id=ident)
                    elif not isinstance(value,str):
                        self.issue('field_type','Expected a string.',file=name,id=ident,field=f)
                textfields = {'statement','his_words','his_statement','check_reason','status_on_pages','fate',
                              'fate_date','present_status','title','as_he_states','plausible_today','state_of_art','worth'}
                for f in textfields & set(fields):
                    if not record.get(f): self.issue('empty_required_content','Required content is empty.',file=name,id=ident,field=f)
                if kind == 'items':
                    if record.get('kind') not in ITEM_KINDS: self.issue('item_kind','Unknown item kind.',id=ident,value=record.get('kind'))
                    if record.get('check') not in ITEM_CHECKS: self.issue('item_check','Unknown item check.',id=ident,value=record.get('check'))
                if kind == 'claims':
                    if record.get('class') not in set('ABCDEF'): self.issue('claim_class','Invalid claim class.',id=ident,value=record.get('class'))
                    if record.get('confidence') not in {'high','medium','low'}: self.issue('claim_confidence','Invalid confidence.',id=ident,value=record.get('confidence'))
                    if not record.get('items'): self.issue('claim_items','Claim has no item anchor.',id=ident)
                    if not re.search(r'2026[-–/]11|November\s*2026',record.get('present_status',''),re.I):
                        self.issue('status_date','Present status is not explicitly dated November2026.',id=ident)
                if kind == 'problems' and not record.get('occurrences'):
                    self.issue('problem_occurrences','Problem has no occurrence.',id=ident)
            dup = [k for k,n in collections.Counter(ids).items() if n>1]
            if dup: self.issue('duplicate_ids','Duplicate record IDs.',file=name,ids=dup)
            self.indexes[kind] = {r['id']:r for r in rows if isinstance(r,dict) and isinstance(r.get('id'),str)}
            mapping = config.get(kind,{}) if isinstance(config,dict) else {}
            if not isinstance(mapping,dict):
                self.issue('alias_schema','Alias section must be an object.',kind=kind)
                mapping = {}
            self.aliases.update(mapping)
            for p in (BASE/'work').glob('*/'+kind+'.json'):
                try:
                    for r in json.loads(p.read_text()):
                        if isinstance(r,dict): self.original_ids.add(r.get('id',''))
                except (ValueError,OSError): pass
        all_ids = set().union(*(set(x) for x in self.indexes.values()))
        if len(all_ids) != sum(len(x) for x in self.indexes.values()):
            self.issue('cross_kind_id_collision','An ID is used by more than one record type.')
        for kind in JSON_FIELDS:
            for old,new in config.get(kind,{}).items():
                resolved = self.canonical(old)
                if old in self.indexes[kind]: self.issue('alias_still_live','Alias source remains a live record.',kind=kind,old=old)
                if resolved not in self.indexes[kind]: self.issue('alias_target','Alias target does not resolve to a live record of its type.',kind=kind,old=old,new=new,resolved=resolved)
            for ident,r in self.indexes[kind].items():
                for old in r.get('aliases',[]):
                    if self.canonical(old) != ident: self.issue('record_alias_mismatch','Record alias does not map back to this record.',id=ident,alias=old)
        if config.get('references',{}) != self.refaliases:
            self.issue('reference_alias_map_mismatch','Two supplied reference alias maps disagree.')

    def pointer(self,value,kind,context,audit=False):
        if not isinstance(value,str):
            self.issue('pointer_type','Pointer must be a string.',value=value,**context)
            return False
        resolved = self.canonical(value)
        if resolved not in self.indexes[kind]:
            self.issue('dangling_pointer','Record pointer does not resolve.',kind=kind,value=value,resolved=resolved,**context)
            return False
        if value != resolved and not audit:
            self.issue('noncanonical_live_pointer','Live pointer uses an alias.',kind=kind,value=value,canonical=resolved,**context)
        return True

    def entries_and_pointers(self):
        path = WORKSPACE/'sources/notes/NOTES_INDEX.tsv'
        if not path.exists():
            self.issue('missing_source_index','Original NOTES_INDEX.tsv is required beside the deliverable.',file=str(path))
            return
        expected = list(csv.DictReader(io.StringIO(path.read_text()),delimiter='\t'))
        ids = [r.get('entry_id','') for r in expected]
        self.expected_entries = set(ids)
        if len(expected)!=380 or len(self.expected_entries)!=380:
            self.issue('source_index_count','NOTES_INDEX must contain exactly380 unique IDs.',rows=len(expected),unique=len(self.expected_entries))
        rows = self.rows('SA05_entries.tsv')
        actual = [r.get('entry_id','') for r in rows]
        if len(rows)!=380 or len(set(actual))!=380 or set(actual)!=self.expected_entries:
            self.issue('entry_coverage','Entry verdicts must equal the exact380 original IDs, once each.',
                       rows=len(rows),unique=len(set(actual)),missing=sorted(self.expected_entries-set(actual)),unexpected=sorted(set(actual)-self.expected_entries),duplicates=[k for k,n in collections.Counter(actual).items() if n>1])
        if actual != ids:
            self.issue('entry_order','Entry order differs from NOTES_INDEX.',severity='warning')
        auditrows = []
        source_to_items = collections.defaultdict(list)
        for ident,item in self.indexes['items'].items():
            sources = item.get('sources',[])
            if len(sources)!=len(set(sources)): self.issue('duplicate_item_source','Item repeats a source ID.',id=ident)
            for source in sources:
                source_to_items[source].append(ident)
                if source not in self.expected_entries: self.issue('unknown_item_source','Item source is absent from NOTES_INDEX.',id=ident,source=source)
        for n,r in enumerate(rows,2):
            item = r.get('item_id','')
            ok = self.pointer(item,'items',{'file':'SA05_entries.tsv','row':n})
            contains = r.get('entry_id') in self.indexes['items'].get(self.canonical(item),{}).get('sources',[])
            if ok and not contains: self.issue('entry_source_reciprocity','Entry primary item does not list that entry among its sources.',entry_id=r.get('entry_id'),item_id=item,row=n)
            if r.get('verdict') not in VERDICTS: self.issue('verdict_value','Unknown verdict.',row=n,value=r.get('verdict'))
            if not r.get('reason','').strip(): self.issue('empty_verdict_reason','Entry has no reason.',row=n)
            auditrows.append({'entry_id':r.get('entry_id'),'primary_item':item,'verdict':r.get('verdict'),'primary_item_lists_source':contains,'all_source_items':source_to_items.get(r.get('entry_id'),[])})
        missing_sources = self.expected_entries-set(source_to_items)
        if missing_sources: self.issue('unrepresented_index_sources','Index entries appear in no item source list.',ids=sorted(missing_sources))
        for ident,c in self.indexes['claims'].items():
            for item in c.get('items',[]): self.pointer(item,'items',{'id':ident,'field':'items'})
            for old in c.get('refines',[]): self.pointer(old,'claims',{'id':ident,'field':'refines'})
            if c.get('refined_statement'): self.pointer(c['refined_statement'],'claims',{'id':ident,'field':'refined_statement'})
        for ident,p in self.indexes['problems'].items():
            for claim in p.get('claims',p.get('claim_ids',[])): self.pointer(claim,'claims',{'id':ident,'field':'claims'})
            for n,occ in enumerate(p.get('occurrences',[])):
                if isinstance(occ,dict):
                    if occ.get('item'): self.pointer(occ['item'],'items',{'id':ident,'field':'occurrences','occurrence':n})
                    for source in occ.get('sources',[]):
                        if source not in self.expected_entries: self.issue('occurrence_source','Problem occurrence has unknown source entry.',id=ident,source=source)
                elif not isinstance(occ,str) or not occ.strip():
                    self.issue('occurrence_type','Occurrence must be a nonempty locator string or object.',id=ident,occurrence=n)
        self.details['entry_audit'] = auditrows
        self.details['unindexed_items'] = [{'id':i,'lead_sources':r.get('lead_sources',[]),'cote':r.get('cote'),'scans':r.get('scans'),'lines':r.get('lines')} for i,r in self.indexes['items'].items() if not r.get('sources')]
        self.details['unavailable_location_records'] = [{'id':i,'class':r.get('class'),'kind':r.get('kind'),'explanation':r.get('check_reason',r.get('present_status',''))} for kind in ('items','claims') for i,r in self.indexes[kind].items() if not r.get('scans') or not r.get('lines')]
        self.metrics['source_packages'] = dict(collections.Counter(r.get('package') for r in expected))

    def bibliography(self):
        bib = self.rows('SA05_references.bib')
        keys = [r.get('key','') for r in bib]
        self.refkeys = set(keys)
        dup = [k for k,n in collections.Counter(keys).items() if n>1]
        if dup: self.issue('duplicate_bib_keys','BibTeX repeats keys.',keys=dup)
        ledger = self.rows('SA05_reference_ledger.json')
        ledger_index = {r.get('key'):r for r in ledger if isinstance(r,dict)}
        tsv = self.rows('SA05_reference_ledger.tsv')
        tsv_index = {r.get('key'):r for r in tsv}
        if self.refkeys!=set(ledger_index) or self.refkeys!=set(tsv_index):
            self.issue('reference_ledger_keys','BibTeX and reference-ledger key sets disagree.',bib_count=len(self.refkeys),json_count=len(ledger_index),tsv_count=len(tsv_index),bib_without_json=sorted(self.refkeys-set(ledger_index)),json_without_bib=sorted(set(ledger_index)-self.refkeys))
        if len(ledger_index)!=len(ledger) or len(tsv_index)!=len(tsv): self.issue('duplicate_ledger_keys','Reference ledger repeats a key.')
        for r in bib:
            key = r['key']
            for field in ['author','title','year','url','note']:
                if field not in r: self.issue('bib_field','Required bibliography field absent.',key=key,field=field)
            if r.get('note') not in {'verified','unverified'}: self.issue('bib_note','Invalid reference verification note.',key=key,note=r.get('note'))
            if r.get('note')=='verified' and not (r.get('url','').strip() or r.get('doi','').strip()):
                self.issue('verified_without_link','Verified reference lacks an opened-link/DOI field.',key=key)
            if self.canonical(key,True)!=key: self.issue('noncanonical_bib_key','BibTeX retains a reference alias.',key=key,canonical=self.canonical(key,True))
            lr,tr = ledger_index.get(key,{}),tsv_index.get(key,{})
            for field in ['title','year','url','note']:
                if field in lr and str(lr[field])!=str(r.get(field,'')): self.issue('bib_ledger_value','BibTeX and JSON ledger differ.',key=key,field=field)
                if field in tr and str(tr[field])!=str(r.get(field,'')): self.issue('bib_tsv_value','BibTeX and TSV ledger differ.',key=key,field=field)
            if lr:
                witnesses = lr.get('source_witnesses',[])
                if not witnesses: self.issue('missing_reference_witness','Reference ledger has no source witness.',key=key)
                if tr and str(len(witnesses))!=tr.get('witness_count'): self.issue('reference_witness_count','Reference witness count differs.',key=key)
                for w in witnesses:
                    if self.canonical(w.get('key',''),True)!=key: self.issue('reference_witness_alias','Witness key does not resolve to canonical record.',key=key,witness=w.get('key'))
        for old,new in self.refaliases.items():
            if self.canonical(old,True) not in self.refkeys: self.issue('reference_alias_target','Reference alias has no canonical bibliography target.',old=old,new=new)
        usages = []
        for kind in ('claims','problems'):
            for ident,r in self.indexes[kind].items():
                for key in r.get('refs',[]):
                    resolved = self.canonical(key,True)
                    if resolved not in self.refkeys: self.issue('dangling_reference','Unknown reference key.',id=ident,key=key)
                    elif key!=resolved: self.issue('noncanonical_live_reference','Live refs array contains an alias.',id=ident,key=key,canonical=resolved)
                    usages.append({'record':ident,'key':key,'canonical':resolved})
        self.details['reference_usages'] = usages
        self.metrics['references'] = len(bib)
        self.metrics['reference_notes'] = dict(collections.Counter(r.get('note') for r in bib))

    def embedded_ids(self):
        all_live = set().union(*(set(v) for v in self.indexes.values()))
        historical = []
        def walk(value,path,audit=False):
            if isinstance(value,dict):
                for k,v in value.items(): walk(v,path+[str(k)],audit or k in AUDIT_FIELDS)
            elif isinstance(value,list):
                for n,v in enumerate(value): walk(v,path+[str(n)],audit)
            elif isinstance(value,str):
                for token in ID_RE.findall(value):
                    resolved = self.canonical(token)
                    if resolved not in all_live:
                        if audit and token in self.original_ids:
                            historical.append({'path':'.'.join(path),'id':token,'status':'preserved original audit ID'})
                        else: self.issue('embedded_dangling_id','Embedded record ID does not resolve.',path='.'.join(path),id=token,audit=audit)
                    elif token!=resolved:
                        historical.append({'path':'.'.join(path),'id':token,'canonical':resolved,'status':'alias resolves'})
                for entry in ENTRY_RE.findall(value):
                    if entry not in self.expected_entries: self.issue('embedded_unknown_entry','Embedded source entry ID is absent from NOTES_INDEX.',path='.'.join(path),entry_id=entry)
        for kind in JSON_FIELDS:
            walk(self.rows('SA05_'+kind+'.json'),['SA05_'+kind+'.json'])
        for name in ['SA05_entries.tsv','SA05_readings.tsv','SA05_links.tsv','SA05_project_leads.tsv','SA05_unavailable_archive_leads.tsv','SA05_unverified_reference_leads.tsv','CHECK_EVENTS.tsv']:
            walk(self.rows(name),[name],name=='SA05_entries.tsv')
        for name in FINAL_PROSE:
            if name in self.data: walk(self.data[name],[name])
        self.details['resolving_historical_ids'] = historical

    def searches_and_events(self):
        searches = self.rows('SA05_searches.tsv')
        searched = collections.defaultdict(list)
        search_tokens = collections.defaultdict(set)
        raw_alias_uses = []
        for n,row in enumerate(searches,2):
            try: record = json.loads(row.get('record_json',''))
            except ValueError:
                self.issue('search_record_json','Search record_json is not valid JSON.',row=n)
                continue
            if not isinstance(record,dict):
                self.issue('search_record_type','Search record_json must be an object.',row=n)
                continue
            if not row.get('search_id'): self.issue('search_identifier','Search row has no identifier.',row=n)
            for label,fields in [('query',['query','queries','queries_normalized','queries_or_actions']),('venue',['venue','venues','method']),('outcome',['outcome','observed_result'])]:
                if not any(record.get(f) for f in fields): self.issue('search_required_content','Search record lacks '+label+'.',row=n,search_id=row.get('search_id'))
            tokens = {row.get('search_id'),record.get('search_id'),record.get('family_id')}-{None,''}
            mapped = ID_RE.findall(row.get('claim_ids',''))
            for cid in mapped:
                if not cid.startswith('SA05-C'):
                    self.issue('search_nonclaim','claim_ids contains a non-claim ID.',row=n,id=cid)
                    continue
                self.pointer(cid,'claims',{'file':'SA05_searches.tsv','row':n})
                canon = self.canonical(cid)
                searched[canon].append({'row':n,'scope':row.get('scope'),'search_id':row.get('search_id')})
                search_tokens[canon].update(tokens)
            # Original query records remain audit copies; their old IDs/keys may resolve through aliases.
            for field in ['claim_id','claim_ids','original_claim_ids']:
                for cid in ID_RE.findall(str(record.get(field,''))):
                    if cid.startswith('SA05-C') and self.canonical(cid) not in self.indexes['claims']:
                        self.issue('search_audit_claim','Original search claim ID does not resolve.',row=n,id=cid)
            for field in ['opened_refs','reference_keys']:
                values=record.get(field,[])
                if isinstance(values,str): values=[v.strip() for v in re.split(r'[;|]',values) if v.strip()]
                for key in values:
                    canonical=self.canonical(key,True)
                    if canonical not in self.refkeys: self.issue('search_reference','Search audit references unknown key.',row=n,key=key)
                    elif key!=canonical: raw_alias_uses.append({'row':n,'original_key':key,'canonical_key':canonical})
        events = self.rows('CHECK_EVENTS.tsv')
        event_by_id = collections.defaultdict(list)
        for n,row in enumerate(events,2):
            ident=row.get('statement_id','')
            target=self.canonical(ident)
            if target==ident: target=self.canonical(ident,True)
            if target not in set().union(*(set(v) for v in self.indexes.values())) | self.refkeys:
                self.issue('event_statement','Check event names an unknown statement/reference.',row=n,id=ident)
            elif ident!=target: self.issue('noncanonical_event_statement','Check event uses an alias as live statement_id.',row=n,id=ident,canonical=target)
            event_by_id[target].append(n)
            if row.get('type') not in EVENT_TYPES: self.issue('event_type','Invalid check-event type.',row=n,value=row.get('type'))
            for f in ['date','who','outcome']:
                if not row.get(f,'').strip(): self.issue('event_required_content','Check-event field is empty.',row=n,field=f)
            if row.get('date') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}(?:T.*)?',row['date']):
                self.issue('event_date','Check-event date has unexpected format.',row=n,value=row['date'])
        coverage=[]
        for ident,c in self.indexes['claims'].items():
            sr=searched.get(ident,[]);er=event_by_id.get(ident,[])
            if not sr: self.issue('claim_without_search','Claim has no mapped SA05_searches row.',id=ident)
            if not er: self.issue('claim_without_event','Claim has no CHECK_EVENTS row.',id=ident)
            missing_tokens=[s for s in c.get('search_ids',[]) if s not in search_tokens.get(ident,set())]
            if missing_tokens: self.issue('declared_search_not_mapped','Declared search ID/family is not present on a row mapped to this claim.',id=ident,search_ids=missing_tokens)
            coverage.append({'claim_id':ident,'searches':sr,'event_rows':er,'declared_search_ids':c.get('search_ids',[]),'unmatched_declared_search_ids':missing_tokens})
        for ident in self.indexes['items']:
            if ident not in event_by_id: self.issue('item_without_event','Item has no check event.',id=ident)
        for key in self.refkeys:
            if key not in event_by_id: self.issue('reference_without_event','Bibliography key has no reference-result/provenance check event.',key=key)
        self.details['claim_coverage']=coverage
        self.details['original_search_reference_aliases']=raw_alias_uses
        self.metrics['claims_with_searches']=sum(bool(x['searches']) for x in coverage)
        self.metrics['claims_with_events']=sum(bool(x['event_rows']) for x in coverage)
        self.metrics['event_types']=dict(collections.Counter(r.get('type') for r in events))
        self.refutations(events)

    def refutations(self,events):
        correction_path=BASE/'work/cote11b/event_target_corrections.json'
        corrections={}
        if correction_path.exists():
            try: corrections=json.loads(correction_path.read_text())
            except ValueError: self.issue('refinement_map_parse','Cannot parse independently reviewed correction map.')
        reviewed_pairs={}
        for source,row in corrections.items():
            subject=self.canonical(source);target=self.canonical(row.get('refined_id',''))
            reviewed_pairs[(subject,target)]={'file':str(correction_path.relative_to(BASE)), 'reason':row.get('reason','')}
            self.pending_pairs[subject]=target
        # This cross-item pair was independently read in the present audit.
        reviewed_pairs[('SA05-C1024','SA05-C1023')]={
            'file':'work/cote11a/proof_checks.md',
            'reason':'The scalar-gauge counterexample refutes unrestricted Cartesian exchange; C1023 is the explicitly narrower tensor-square exchange theorem. The source claim fate names this exact refinement.'}
        def itemset(ident):
            if ident in self.indexes['items']: return {ident}
            return set(self.indexes['claims'].get(ident,{}).get('items',[]))
        def sources(ident):
            return {s for i in itemset(ident) for s in self.indexes['items'].get(i,{}).get('sources',[])}
        audit=[]
        for n,row in enumerate(events,2):
            if row.get('type')!="refuted, with the refined statement's id": continue
            subject=self.canonical(row.get('statement_id',''))
            text=row.get('outcome','')
            pat=r'(?:refined\s+(?:statement|formula)|refinement/correct\s+scope)\s*(?::|=|in)?\s*(SA05-C\d+(?:\.[A-Za-z_][A-Za-z_0-9]*)?)'
            targets=list(dict.fromkeys(re.findall(pat,text,re.I)))
            if not targets:
                candidates=list(dict.fromkeys(CLAIM_TOKEN_RE.findall(text)))
                targets=[t for t in candidates if t!=subject]
            pending=subject in self.pending_pairs
            if not targets:
                self.issue('refutation_missing_target','Refutation event has no explicit distinct refinement target.',row=n,subject=subject,pending=pending)
            for raw in targets:
                valid_format=bool(re.fullmatch(r'SA05-C\d+',raw))
                target=self.canonical(raw)
                exists=target in self.indexes['claims']
                shared_items=sorted(itemset(subject)&itemset(target))
                shared_sources=sorted(sources(subject)&sources(target))
                reverse=[self.canonical(x) for x in self.indexes['claims'].get(target,{}).get('refines',[])]
                declared=self.indexes['claims'].get(subject,{}).get('refined_statement')
                declared=self.canonical(declared) if declared else None
                manual=reviewed_pairs.get((subject,target))
                relation=bool(shared_items or shared_sources or subject in reverse or declared==target or manual)
                if not valid_format: self.issue('refutation_pseudo_target','Refutation target is a field/pseudo-ID, not a claim ID.',row=n,subject=subject,target=raw,pending=pending)
                if not exists: self.issue('refutation_dangling_target','Refinement target does not exist as a live claim.',row=n,subject=subject,target=raw,pending=pending)
                if subject==target: self.issue('refutation_self_target','Refuted statement points to itself as refinement.',row=n,subject=subject,pending=pending)
                if exists and subject!=target and not relation:
                    self.issue('refutation_unrelated_target','No shared item/source, explicit reverse relation or reviewed cross-item relationship supports this target.',row=n,subject=subject,target=target,pending=pending)
                source_statement=self.indexes['claims'].get(subject,{}).get('statement',self.indexes['items'].get(subject,{}).get('statement',''))
                target_statement=self.indexes['claims'].get(target,{}).get('statement','')
                if exists and source_statement and source_statement.strip()==target_statement.strip():
                    self.issue('refutation_identical_statement','Target repeats the same statement text.',row=n,subject=subject,target=target,pending=pending)
                audit.append({'row':n,'subject':subject,'raw_target':raw,'canonical_target':target,'target_exists':exists,'target_is_self':subject==target,'valid_id_format':valid_format,'shared_items':shared_items,'shared_entry_sources':shared_sources,'target_refines_subject':subject in reverse,'source_declares_target':declared==target,'reviewed_cross_item_relationship':manual,'documented_expected_target':self.pending_pairs.get(subject),'outcome':text})
        self.details['refutation_targets']=audit
        self.details['refutation_validation_limit']='Relevance checks establish recorded structural relationships and retain independently reviewed cross-item reasons. They do not prove equivalence or truth of the mathematical statements.'
        self.metrics['refutation_events']=sum(r.get('type')=="refuted, with the refined statement's id" for r in events)

    def links_and_directions(self):
        links=self.rows('SA05_links.tsv');projects=self.rows('SA05_project_leads.tsv');unavailable=self.rows('SA05_unavailable_archive_leads.tsv')
        unverified_refs=self.rows('SA05_unverified_reference_leads.tsv')
        for name,rows in [('SA05_links.tsv',links),('SA05_project_leads.tsv',projects),('SA05_unavailable_archive_leads.tsv',unavailable),('SA05_unverified_reference_leads.tsv',unverified_refs)]:
            for n,r in enumerate(rows,2):
                if r.get('kind') not in {'folder','published work','our projects'}: self.issue('link_kind','Unknown link kind.',file=name,row=n)
                for f in ['from','to','what','evidence']:
                    if not r.get(f,'').strip(): self.issue('link_empty','Link field is empty.',file=name,row=n,field=f)
                for entry in ENTRY_RE.findall(r.get('note_ids','')):
                    if entry not in self.expected_entries: self.issue('link_note_id','Link cites an unknown note ID.',file=name,row=n,entry_id=entry)
                if name=='SA05_project_leads.tsv' and r.get('kind')!='our projects': self.issue('project_table_kind','Project table contains a non-project link.',row=n)
                if name=='SA05_unavailable_archive_leads.tsv' and not r.get('status','').strip(): self.issue('unavailable_link_status','Unavailable archive lead lacks status.',row=n)
                if name=='SA05_links.tsv' and r.get('kind')!='our projects' and re.search(r'^(?:UNAVAILABLE|UNVERIFIED|UNATTACHED)\b',r.get('to',''),re.I):
                    self.issue('unavailable_in_checked_links','Unavailable endpoint is in the checked-link table.',row=n)
        normalize=lambda row:json.dumps({f:row.get(f,'') for f in TSV_FIELDS['SA05_links.tsv']},sort_keys=True,ensure_ascii=False)
        projected=collections.Counter(normalize(r) for r in links if r.get('kind')=='our projects')
        if projected!=collections.Counter(normalize(r) for r in projects): self.issue('project_projection','Separate project table differs from project rows in the main link table.')
        checked=[r for r in links if r.get('kind')!='our projects']
        self.metrics['link_classification']={
            'declared_checked_total':len(checked),
            'declared_checked_folder':sum(r.get('kind')=='folder' for r in checked),
            'declared_checked_published':sum(r.get('kind')=='published work' for r in checked),
            'separate_unavailable_archive_leads':len(unavailable),
            'separate_unverified_reference_leads':len(unverified_refs),
            'project_leads':len(projects),
            'distinct_rows_across_main_and_separate_leads':len(links)+len(unavailable)+len(unverified_refs),
            'note':'Counts follow the manually assigned tables/kinds. Project rows are a separate projection and are not double-counted. This does not mechanically certify that both passages were read.'}
        text=self.data.get('SA05_directions.md')
        if isinstance(text,str):
            pattern=re.compile(r'^#{1,4}\s+(?:(?:Rank|Direction|Priority)\s+)?(\d+)\s*[.:)—–-]?\s+.+$',re.M|re.I)
            headings=list(pattern.finditer(text))
            if not headings:
                headings=list(re.finditer(r'^(\d+)\.\s+\S.+$',text,re.M))
            directions=[]
            if not headings: self.issue('direction_structure','No ranked direction blocks could be identified; use numbered headings or numbered list blocks.',pending=self.draft)
            for i,h in enumerate(headings):
                block=text[h.start():headings[i+1].start() if i+1<len(headings) else len(text)]
                ids=set(ID_RE.findall(block))
                found={kind:sorted(x for x in ids if x in self.indexes[kind]) for kind in JSON_FIELDS}
                for kind in JSON_FIELDS:
                    if not found[kind]: self.issue('direction_anchor','Direction lacks a live '+kind+' citation.',rank=h.group(1),heading=h.group(0),pending=self.draft)
                directions.append({'rank':int(h.group(1)),'heading':h.group(0),'anchors':found})
            ranks=[r['rank'] for r in directions]
            if ranks and (len(ranks)!=len(set(ranks)) or ranks!=sorted(ranks)):
                self.issue('direction_rank','Direction ranks are repeated or unordered.',ranks=ranks)
            self.details['directions']=directions
            self.metrics['directions']=len(directions)
        for name in FINAL_PROSE:
            text=self.data.get(name,'')
            if isinstance(text,str) and re.search(r'(?im)^#{1,3}\s+.*(?:\bprovisional\b|\(draft\)|\bTODO\b)',text):
                self.issue('provisional_final_prose','Final prose has an explicit provisional/TODO heading.',file=name,pending=self.draft)

    def source_integrity(self):
        ledger_checks=[]
        for path in sorted((BASE/'work').glob('*/reading_log.tsv')):
            try:
                rows=list(csv.DictReader(io.StringIO(path.read_text()),delimiter='\t'))
            except (OSError,csv.Error): continue
            for n,row in enumerate(rows,2):
                old=row.get('sha256','')
                filename=row.get('file','')
                if not old or not filename: continue
                p=Path(filename)
                if not p.is_absolute(): p=WORKSPACE/p
                actual=sha(p.read_bytes()) if p.is_file() else None
                ok=actual==old
                ledger_checks.append({'ledger':str(path.relative_to(BASE)),'row':n,'file':filename,'saved_sha256':old,'actual_sha256':actual,'unchanged':ok})
                if not ok: self.issue('saved_source_hash','File differs from an existing saved reading-ledger hash or is unavailable.',ledger=str(path.relative_to(BASE)),row=n,file=filename,expected=old,actual=actual)
        zip_checks=[]
        original_hashes=set()
        for label in ['notes','texts']:
            attachment=WORKSPACE/'upload'/('SA05_'+label+'.zip')
            if not attachment.is_file():
                self.issue('missing_source_attachment','Original attachment unavailable for full byte-preservation check.',file=str(attachment))
                continue
            with zipfile.ZipFile(attachment) as z:
                for info in z.infolist():
                    if info.is_dir(): continue
                    original=z.read(info)
                    expected=sha(original);original_hashes.add(expected)
                    p=WORKSPACE/'sources'/label/info.filename
                    actual=sha(p.read_bytes()) if p.is_file() else None
                    same=expected==actual
                    zip_checks.append({'archive':attachment.name,'member':info.filename,'file':str(p.relative_to(WORKSPACE)),'original_sha256':expected,'actual_sha256':actual,'unchanged':same})
                    if not same: self.issue('attachment_source_changed','Extracted source bytes differ from the supplied attachment or the file is absent.',file=str(p.relative_to(WORKSPACE)),expected=expected,actual=actual)
        self.original_source_hashes=original_hashes
        self.details['saved_hash_ledger_checks']=ledger_checks
        self.details['original_attachment_hash_checks']=zip_checks
        self.metrics['source_integrity']={'saved_ledger_rows_checked':len(ledger_checks),'saved_ledger_unique_files':len({r['file'] for r in ledger_checks}),'original_attachment_files_checked':len(zip_checks),'unchanged_attachment_files':sum(r['unchanged'] for r in zip_checks),'source_bytes_modified':sum(not r['unchanged'] for r in zip_checks)}

    def counts_and_packaging(self):
        computed={
            'entries':len(self.rows('SA05_entries.tsv')), 'items':len(self.indexes['items']),
            'claims':len(self.indexes['claims']), 'problems':len(self.indexes['problems']),
            'readings':len(self.rows('SA05_readings.tsv')), 'links':len(self.rows('SA05_links.tsv')),
            'project_leads':len(self.rows('SA05_project_leads.tsv')),
            'separate_unavailable_archive_leads':len(self.rows('SA05_unavailable_archive_leads.tsv')),
            'separate_unverified_reference_leads':len(self.rows('SA05_unverified_reference_leads.tsv')),
            'events':len(self.rows('CHECK_EVENTS.tsv')), 'search_rows':len(self.rows('SA05_searches.tsv')),
            'verdicts':dict(collections.Counter(r.get('verdict') for r in self.rows('SA05_entries.tsv'))),
            'item_kinds':dict(collections.Counter(r.get('kind') for r in self.indexes['items'].values())),
            'claim_classes':dict(sorted(collections.Counter(r.get('class') for r in self.indexes['claims'].values()).items())),
            'claim_statuses':dict(collections.Counter(r.get('status_category',r.get('status_on_pages')) for r in self.indexes['claims'].values())),
        }
        counts=self.data.get('counts.json',{})
        for key,value in computed.items():
            if key in counts and counts[key]!=value: self.issue('counts_mismatch','counts.json differs from actual tables.',field=key,recorded=counts[key],actual=value)
        if 'directions' in counts and counts['directions']!=self.metrics.get('directions'): self.issue('direction_count_mismatch','Direction count differs.',recorded=counts['directions'],actual=self.metrics.get('directions'))
        self.metrics.update(computed)
        log=self.data.get('progress.log','')
        timestamps=re.findall(r'2026-11-19(?:T\d{2}:\d{2}:\d{2}Z| \d{2}:\d{2}:\d{2} UTC)',log)
        self.details['progress_log']={'timestamped_records':len(timestamps),'first_timestamp':timestamps[0] if timestamps else None,'last_timestamp':timestamps[-1] if timestamps else None,'note':'Content/stage completion remains an author assertion; timestamps are only structurally checked.'}
        if not timestamps: self.issue('progress_timestamp','No UTC timestamp found in progress.log.')
        self.details['packaging_prerequisites']={name:{'exists':(BASE/name).is_file(),'bytes':(BASE/name).stat().st_size if (BASE/name).is_file() else None} for name in REQUIRED}
        if not self.archive:
            self.details['archive_validation']={'performed':False,'reason':'No --archive path supplied. Required package member names were checked in the deliverable directory.'}
            return
        archive=Path(self.archive)
        if not archive.is_absolute(): archive=WORKSPACE/archive
        if not archive.is_file():
            self.issue('archive_missing','Requested archive does not exist.',file=str(archive))
            return
        archive_report={'performed':True,'file':str(archive),'sha256':sha(archive.read_bytes()),'members':[]}
        try:
            with zipfile.ZipFile(archive) as z:
                names=z.namelist()
                if len(names)!=len(set(names)): self.issue('archive_duplicates','ZIP repeats a member path.')
                for req in REQUIRED+['programs/validate_final.py']:
                    if 'SA05/'+req not in names: self.issue('archive_required_member','Required member missing from ZIP.',member='SA05/'+req)
                for name in names:
                    parts=Path(name).parts
                    if name.startswith('/') or '..' in parts: self.issue('archive_unsafe_path','Unsafe ZIP member path.',member=name)
                    if name.endswith('.zip') or 'upload' in parts or 'sources' in parts:
                        self.issue('archive_attachment_or_nested_zip','ZIP contains an attachment/source folder or nested archive.',member=name)
                    if not name.endswith('/'):
                        digest=sha(z.read(name))
                        if digest in getattr(self,'original_source_hashes',set()): self.issue('archive_original_source_bytes','ZIP embeds unchanged supplied source bytes.',member=name)
                        archive_report['members'].append({'name':name,'sha256':digest,'bytes':z.getinfo(name).file_size})
                manifest_name='SA05/ARCHIVE_MANIFEST.json'
                if manifest_name in names:
                    manifest=json.loads(z.read(manifest_name))
                    listed=set()
                    for row in manifest.get('entries',[]):
                        name='SA05/'+row['path'];listed.add(name)
                        if name not in names: self.issue('manifest_missing_member','Manifest lists absent member.',member=name)
                        elif sha(z.read(name))!=row.get('sha256'): self.issue('manifest_hash','ZIP member hash differs from manifest.',member=name)
                    extra=set(names)-listed-{manifest_name}
                    if extra: self.issue('manifest_unlisted','ZIP members are absent from manifest.',members=sorted(extra))
                    archive_report['manifest_entries']=len(listed)
                else: self.issue('archive_manifest','Packaging manifest is missing.')
        except (zipfile.BadZipFile,ValueError,KeyError) as exc:
            self.issue('archive_parse',str(exc))
        self.details['archive_validation']=archive_report

    def run(self):
        self.load()
        self.schemas_and_aliases()
        self.entries_and_pointers()
        self.bibliography()
        self.embedded_ids()
        self.searches_and_events()
        self.links_and_directions()
        self.source_integrity()
        self.counts_and_packaging()
        for name,blob in self.raw.items():
            p=BASE/name
            if not p.exists() or p.read_bytes()!=blob:
                self.issue('input_changed_during_validation','Consolidated input changed while validation ran; rerun against a stable generation.',file=name,pending=True)
        tally=collections.Counter(i['severity'] for i in self.issues)
        status='FAILED' if tally['error'] else ('DRAFT_PENDING' if tally['pending'] else 'PASSED')
        report={
            'validator':'SA05/programs/validate_final.py','schema_version':1,
            'validator_sha256':sha(Path(__file__).read_bytes()),
            'generated_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
            'mode':'draft' if self.draft else 'strict','status':status,
            'issue_counts':{k:tally[k] for k in ['error','pending','warning']},
            'metrics':self.metrics,'issues':self.issues,'details':self.details,
            'limits':[
                'This program validates structure, recorded links, coverage and unchanged source bytes. It does not generate or verify a mathematical verdict.',
                'Search coverage means an actual saved search record maps to the claim; it does not certify that the search was exhaustive or that a referenced theorem proves the claim.',
                'Refutation relevance uses shared provenance, explicit refinement links and independently authored cross-item review reasons; mathematical scope still requires the recorded human/model reading.',
                'Original IDs in preserved audit copies may resolve through documented aliases. Live structured pointers and refs must be canonical.',
            ],
        }
        OUT.mkdir(parents=True,exist_ok=True)
        stem='validate_final_draft' if self.draft else 'validate_final'
        serialized=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
        (OUT/(stem+'.json')).write_text(serialized)
        text=[f'SA05 STRUCTURAL VALIDATION: {status}',f"UTC: {report['generated_utc']}",f"Mode: {report['mode']}",
              'Issue counts: '+json.dumps(report['issue_counts']),
              'Actual counts: '+json.dumps(self.metrics,ensure_ascii=False,sort_keys=True), '', 'DETAILED ISSUES']
        text += [json.dumps(i,ensure_ascii=False,sort_keys=True) for i in self.issues]
        if not self.issues: text.append('None.')
        text += ['', 'Detailed coverage, source hashes, per-event refinement targets, source snapshot and archive checks are retained in '+stem+'.json.', '', 'LIMITS']+report['limits']
        rendered='\n'.join(text)+'\n'
        (OUT/(stem+'.txt')).write_text(rendered)
        history=OUT/'validation_runs'
        history.mkdir(exist_ok=True)
        runstamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        (history/(runstamp+'_'+stem+'.json')).write_text(serialized)
        (history/(runstamp+'_'+stem+'.txt')).write_text(rendered)
        print('\n'.join(text[:5]))
        print('Reports:',str(OUT/(stem+'.json')),str(OUT/(stem+'.txt')))
        return 1 if tally['error'] or (tally['pending'] and not self.draft) else 0


def main():
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--draft',action='store_true',help='Report known unfinished final prose/refinement integrations as pending.')
    parser.add_argument('--archive',help='Also inspect the final ZIP members and packaging manifest.')
    args=parser.parse_args()
    return Audit(args.draft,args.archive).run()


if __name__=='__main__':
    sys.exit(main())
