"""Assemble reviewed stream registers; no source verdicts are inferred here.

All semantic edits below are the explicit, manually agreed consolidations in
parts/a/cross_merge_recommendations.md and parts/b/root_review_merge_proposals.md.
"""
from pathlib import Path
import json,csv,re,hashlib,datetime,collections
W=Path(__file__).resolve().parents[1]; ROOT=W.parent; F=W/'final';F.mkdir(exist_ok=True)
def j(path):return json.loads(path.read_text())
def ts(path):return list(csv.DictReader(path.open(),delimiter='\t'))
def write_tsv(path,fields,rows):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
def unique(xs):
 seen=set();out=[]
 for x in xs:
  k=json.dumps(x,sort_keys=True,ensure_ascii=False)
  if k not in seen:seen.add(k);out.append(x)
 return out
items=[];claims=[];problems=[];entries=[];readings=[];links=[];events=[]
for stream in ['a','b','c','root']:
 p=W/'parts'/stream
 items+=j(p/'items.json');claims+=j(p/'claims.json');problems+=j(p/'problems.json')
 if (p/'entries.tsv').exists(): entries+=ts(p/'entries.tsv')
 readings+=ts(p/'readings.tsv');links+=ts(p/'links.tsv');events+=ts(p/'CHECK_EVENTS.tsv')
items+=j(W/'parts/b/root_supplement_items.json');claims+=j(W/'parts/b/root_supplement_claims.json');problems+=j(W/'parts/b/root_supplement_problems.json')
readings+=ts(W/'parts/b/root_supplement_readings.tsv');events+=ts(W/'parts/b/root_supplement_events.tsv')
readings+=ts(W/'parts/a/c100_witness_readings.tsv')
events+=ts(W/'parts/root/reference_events.tsv')
for patch in ts(W/'parts/b/cross_reference_item_locator_patch.tsv'):
 it=next(x for x in items if x['id']==patch['item_id'])
 assert it['lines']==json.loads(patch['old_lines_json']),patch['item_id']
 it['lines']=json.loads(patch['new_lines_json'])
next(x for x in claims if x['id']=='C-SA04-448')['fate_date']=next(x for x in claims if x['id']=='C-SA04-448')['fate_date'].replace('deJongErratum','deJongErratum1999')

# Exact source-entry reassignment; no whole-item alias for the bundled SA04-217.
e=next(x for x in entries if x['entry_id']=='MPL_93_047-091#205')
e['item_id']='SA04-153';e['verdict']='merged';e['reason']+=' Final cross-stream consolidation: repeats the integral projective-invariance assertion already inSA04-153/C-SA04-122; scan80 occurrence retained.'
ia=next(x for x in items if x['id']=='SA04-153');ib=next(x for x in items if x['id']=='SA04-217')
ia['sources']=unique(ia['sources']+['MPL_93_047-091#205']);ia['scans']=unique(ia['scans']+[80]);ia['lines']+=['pro/MPL_93_047-091_transcription.tex:1286–1292']
ia['statement']+=' The scan80 substitutions multiply by a base unit, add a base section, or invert an invertible coordinate; they restate the same relative projective invariance.'
ib['sources']=[x for x in ib['sources'] if x!='MPL_93_047-091#205'];ib['lines']=['pro/MPL_93_047-091_transcription.tex:1294–1297']
ib['his_words']='df=dg ⇒ G(f,g)=0'
ib['statement']='In characteristiczero, equalitydf=dg locally implies thatf−g is a base constant and the Schwarzian difference vanishes. For the integral Hasse invariant in characteristics2 and3, equality of ordinary differentials alone is too weak: t andt+t^p have unit first derivative and nonzero integral invariant.'
ib['check_reason']='The note already distinguishes the characteristiczero deduction from small-characteristic failure. The repeated projective-invariance entry#205 was reassigned toSA04-153; only#206 remains here.'
ca=next(x for x in claims if x['id']=='C-SA04-122');cb=next(x for x in claims if x['id']=='C-SA04-217')
ca['scans']=unique(ca['scans']+[80]);ca['lines']+=['pro/MPL_93_047-091_transcription.tex:1286–1292']
ca['his_statement']+='; G(t,as)=G(t,s), G(t,s+b)=G(t,s), G(t,1/s)=G(t,s), with base coefficients.'
ca['fate']+=' Consolidated repeated scan80 occurrence formerlyC-SA04-217; the all-base certificate, not merely the characteristiczero citation, proves its invariance.'
ca['refs']=unique(ca['refs']+cb['refs'])
claims=[x for x in claims if x['id']!='C-SA04-217']
ce=next(x for x in claims if x['id']=='C-SA04-218');ce['lines']=['pro/MPL_93_047-091_transcription.tex:1294–1297'];ce['his_statement']='df=dg ⇒ G(f,g)=0'

# Consolidate the same relative reconstruction question, retaining exact scope.
p=next(x for x in problems if x['id']=='MP-SA04-164');q=next(x for x in problems if x['id']=='MP-SA04-201')
p['occurrences']=unique(p['occurrences']+q['occurrences'])
p['as_he_states']='For the flat finitely presented relative setting with geometrically connected fibres, the section/radicial substitute and tentative Noetherian condition of scan191, representations of the specified strict pro-étale groupΠ should recover coherent relatively étale-trivial stratified objects satisfying the stated fibrewise quotient condition. The surrounding rank-one and enlarged-monodromy distinctions are separate subclaims.'
p['plausible_today']=q['plausible_today']+' Do not replace the historical enlarged group by an ordinary profinite group on nonnormal bases.'
p['state_of_art']='C-SA04-698 gives the exact source formulation. DosSantos2007 §2.4 Proposition13 treats a regular scheme over an algebraically closed field; Lara2019 Theorem3.1 treats a proper reduced-connected-fibre setting with near exactness. Neither proves the complete relative equivalence on the page.'
p['refs']=unique(p['refs']+q['refs']);problems=[x for x in problems if x['id']!='MP-SA04-201']

# The supplementary counterexample answers the same manuscript problem.
p=next(x for x in problems if x['id']=='MP-SA04-168');q=next(x for x in problems if x['id']=='MP-SA04-204')
p['occurrences']=unique(p['occurrences']+q['occurrences'])
p['refs']=unique(p['refs']+q['refs'])
problems=[x for x in problems if x['id']!='MP-SA04-204']

# Bibliographic aliases refer to the same works, with union of verification notes.
ref_alias={
 'BDeligne1970':'Deligne1970','BDumas2009':'Dumas2009',
 'BEGAIV4Metadata':'EGAIV4','REGAIV4':'EGAIV4',
 'RGroth1966':'Groth1966','RdeJongICM1998':'deJongICM1998',
 'RSGA7I':'SGA7I','deJongErratum':'deJongErratum1999',
 'BKatz1970Supplement':'Katz1970',
 'BGrothendieckBibliography':'GrothPublishedWorks',
 'BKempf1978Followup':'RKempf1978','BKempf1976PreprintFollowup':'RKempf1976',
 'BHaboush1975Followup':'RHaboush1975','BSastrySeshadri2011Followup':'RSastrySeshadri2011',
 'BBateMartinRohrleTange2013Followup':'RBate2013','BRamosCuevas2013Followup':'RRamosCuevas2013'
}
id_alias={'C-SA04-217':'C-SA04-122','MP-SA04-201':'MP-SA04-164','MP-SA04-204':'MP-SA04-168'}
def remap(v):
 if isinstance(v,str):
  v=v.replace('SA04_texts/','')
  for a,z in id_alias.items():v=re.sub(re.escape(a)+r'(?![0-9])',z,v)
  return v
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
items,claims,problems,entries,readings,links,events=[remap(v) for v in (items,claims,problems,entries,readings,links,events)]
for c in claims+problems:c['refs']=unique([ref_alias.get(x,x) for x in c['refs']])
for e in events:
 e['statement_id']=ref_alias.get(e['statement_id'],e['statement_id'])
 if e['type'] in {'refuted','refuted, with the refined statement’s id','refuted, with the refined statement id'}:
  e['type']="refuted, with the refined statement's id"
 if e['statement_id']=='SA04-217':e['outcome']+=' Historical event on the formerly bundled item: entry#205 now belongs toSA04-153; retained item217 concerns only#206. See ID_ALIASES.tsv.'
for e in entries:
 if e['verdict'].startswith('merged'):e['verdict']='merged'
 if e['verdict'].startswith('kept'):e['verdict']='kept'

# Remove only the manually identified duplicate reading of scan212 equation4.1.
same=[i for i,x in enumerate(readings) if x['cote']=='93' and str(x['scan'])=='212' and ('Pcip' in x['reading'] or 'Pcin' in x['alternative'])]
if len(same)>1:
 keep=same[-1]
 for i in same[:-1]:readings[keep]['evidence']+=' '+readings[i]['evidence']
 readings=[x for i,x in enumerate(readings) if i not in same[:-1]]

def bibparse(s):
 result=[];pos=0
 while True:
  m=re.search(r'@([A-Za-z]+)\s*\{\s*([^,]+),',s[pos:])
  if not m:break
  typ,key=m[1],m[2].strip();i=pos+m.end();start=i;depth=1
  while i<len(s) and depth:
   if s[i]=='\\':i+=2;continue
   if s[i]=='{':depth+=1
   elif s[i]=='}':depth-=1
   i+=1
  body=s[start:i-1];pos=i;fields={};at=0
  while at<len(body):
   fm=re.search(r'([A-Za-z][A-Za-z0-9_]*)\s*=\s*',body[at:])
   if not fm:break
   name=fm[1].lower();k=at+fm.end()
   if k>=len(body):break
   if body[k]=='{':
    a=k+1;k+=1;d=1
    while k<len(body) and d:
     if body[k]=='\\':k+=2;continue
     if body[k]=='{':d+=1
     elif body[k]=='}':d-=1
     k+=1
    value=body[a:k-1]
   elif body[k]=='"':
    a=k+1;k+=1
    while k<len(body) and body[k]!='"':k+=2 if body[k]=='\\' else 1
    value=body[a:k];k+=1
   else:
    a=k
    while k<len(body) and body[k]!=',':k+=1
    value=body[a:k].strip()
   fields[name]=value;at=k
  result.append((typ,key,fields))
 return result
bs=[W/'parts'/p/'references.bib' for p in ('a','b','c','root')]+[W/'parts/b/root_supplement_references.bib',W/'parts/b/git_followup.bib']
bib={};bibprovenance={}
for path in bs:
 for typ,key,fields in bibparse(path.read_text()):
  canonical=ref_alias.get(key,key);oldnote=fields.get('note','')
  # Formatting only: each supplementary source was opened, as its original note records.
  if oldnote not in ('verified','unverified'):
   fields['annote']=(fields.get('annote','')+' '+oldnote).strip()
   fields['note']='unverified' if oldnote.lower().startswith('unverified') else 'verified'
  if canonical not in bib:bib[canonical]=(typ,fields)
  else:
   base=bib[canonical][1]
   for k,v in fields.items():
    if k not in base or not base[k]:base[k]=v
    elif k=='annote' and v not in base[k]:base[k]+=' Additional stream verification ('+key+'): '+v
    elif k=='url' and v!=base[k]:base['annote']=base.get('annote','')+' Additional opened URL: '+v+'.'
   if fields['note']=='verified':base['note']='verified'
  bibprovenance.setdefault(canonical,[]).append({'key':key,'file':str(path.relative_to(W))})
for k,(typ,f) in bib.items():
 if k=='RDeligne1968':f['title']='Courbes elliptiques : Formulaire d’après J. Tate'
output=[]
for key in sorted(bib):
 typ,fields=bib[key];output.append('@'+typ+'{'+key+',\n'+''.join('  '+k+' = {'+v+'},\n' for k,v in fields.items())+'}\n')
(F/'SA04_references.bib').write_text('\n'.join(output))
(F/'BIBLIOGRAPHY_PROVENANCE.json').write_text(json.dumps(bibprovenance,ensure_ascii=False,indent=2)+'\n')

def nkey(x):return int(re.search(r'(\d+)$',x['id'])[1])
for name,data in [('items',items),('claims',claims),('problems',problems)]:
 data.sort(key=nkey);(F/f'SA04_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
index=ts(ROOT/'source/SA04_notes/NOTES_INDEX.tsv');order={x['entry_id']:i for i,x in enumerate(index)}
entries.sort(key=lambda x:order.get(x['entry_id'],10**9))
write_tsv(F/'SA04_entries.tsv',['entry_id','item_id','verdict','reason'],entries)
write_tsv(F/'SA04_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
write_tsv(F/'SA04_links.tsv',['kind','from','to','what','evidence','note_ids'],links)
write_tsv(F/'SA04_project_leads.tsv',['kind','from','to','what','evidence','note_ids'],[x for x in links if x['kind']=='our projects'])
events=unique(events)
write_tsv(F/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
write_tsv(F/'ID_ALIASES.tsv',['old_id','canonical_id','reason'],[
 {'old_id':'C-SA04-217','canonical_id':'C-SA04-122','reason':'Exact repeated integral projective-invariance assertion; scan80 added.'},
 {'old_id':'MP-SA04-201','canonical_id':'MP-SA04-164','reason':'Same relative enlarged-monodromy reconstruction question; exact scope retained.'},
 {'old_id':'MP-SA04-204','canonical_id':'MP-SA04-168','reason':'Same rational-Verschiebung-lift question; supplementary source occurrence and counterexample retained.'},
 {'old_id':'MPL_93_047-091#205 -> SA04-217','canonical_id':'SA04-153','reason':'Only this source-entry association changed; item217 retained for#206.'}])

required={
 'items':set('id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()),
 'claims':set('id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()),
 'problems':set('id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split())}
errors=[]
for name,seq in [('items',items),('claims',claims),('problems',problems)]:
 ids=[v['id'] for v in seq]
 if len(ids)!=len(set(ids)):errors.append(name+' duplicate IDs')
 for v in seq:
  if set(v)!=required[name]:errors.append(f"{v['id']}: field mismatch {set(v)^required[name]}")
itemids={x['id'] for x in items};claimids={x['id'] for x in claims};problemids={x['id'] for x in problems};refids=set(bib)
enums={'kind':set(['conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other']),
 'check':set(['agrees','overstates','understates','misreads','not on the page']),
 'status_on_pages':set(['proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'])}
for v in items:
 for k in ('kind','check'):
  if v[k] not in enums[k]:errors.append(v['id']+': invalid '+k+'='+v[k])
for v in claims:
 if v['status_on_pages'] not in enums['status_on_pages']:errors.append(v['id']+': invalid status '+v['status_on_pages'])
 if v['class'] not in list('ABCDEF'):errors.append(v['id']+': invalid class')
 if v['confidence'] not in ['high','medium','low']:errors.append(v['id']+': invalid confidence')
 for i in v['items']:
  if i not in itemids:errors.append(v['id']+': missing item '+i)
for v in claims+problems:
 for key in v['refs']:
  if key not in refids:errors.append(v['id']+': missing reference '+key)
idx=[x['entry_id'] for x in index];out=[x['entry_id'] for x in entries]
if len(out)!=432 or collections.Counter(idx)!=collections.Counter(out):errors.append('NOTES_INDEX coverage is not exactly432 one-to-one')
src_to_item={}
for v in items:
 for src in v['sources']:src_to_item.setdefault(src,[]).append(v['id'])
for e in entries:
 associated=src_to_item.get(e['entry_id'],[])
 # The eight MPL98 entries are explicitly composite headings. Their89 leaf
 # analyses keep the parent's stable ID as provenance; only the umbrella has
 # an indexed verdict. This reviewed fan-out is not extra entry coverage.
 if e['entry_id'].startswith('MPL_98#'):
  if e['item_id'] not in associated:errors.append(e['entry_id']+': missing composite parent association')
 elif associated!=[e['item_id']]:errors.append(e['entry_id']+': item/source association mismatch '+str(associated))
 if e['verdict'] not in ['kept','merged','corrected','withdrawn','rests on a misreading']:errors.append(e['entry_id']+': invalid verdict '+e['verdict'])
for key,(typ,fields) in bib.items():
 if fields.get('note') not in ('verified','unverified'):errors.append('bad note '+key)
 if fields.get('note')=='verified' and not (fields.get('url') or fields.get('doi')):errors.append('verified reference without opened link '+key)
counts={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links),'events':len(events),'references':len(bib),
 'verdicts':dict(collections.Counter(x['verdict'] for x in entries)),
 'item_kinds':dict(collections.Counter(x['kind'] for x in items)),
 'claim_classes':dict(collections.Counter(x['class'] for x in claims)),
 'claim_statuses':dict(collections.Counter(x['status_on_pages'] for x in claims)),
 'link_kinds':dict(collections.Counter(x['kind'] for x in links)),
 'reference_verification':dict(collections.Counter(v[1]['note'] for v in bib.values()))}
report={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':counts,'errors':errors,'passed':not errors}
(W/'outputs/assembly_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(F/'VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
