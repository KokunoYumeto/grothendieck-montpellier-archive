"""Insert the measured final census and apply reviewed canonical IDs to prose."""
from pathlib import Path
import csv,json,re,collections
OUT=Path(__file__).resolve().parents[1]
counts=json.loads((OUT/'outputs/census.json').read_text())
def tv(name):
    with (OUT/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
aliases={x['retired_id']:x['canonical_id'] for x in tv('ID_ALIASES.tsv')}
def canonical(x):
    while x in aliases:x=aliases[x]
    return x
pat=re.compile(r'(?<![A-Za-z0-9-])(?:MP-SA03-\d+|CL-SA03-\d+|SA03-\d+)(?!\d)')
range_pat=re.compile(r'(?<![A-Za-z0-9-])((?:CL-|MP-)?SA03-)(\d+)[––](\d+)')
def expand_alias_range(m):
    prefix,first,last=m.groups();start=int(first);end=int(last)
    if end<start:return m.group()
    width=len(first) if first.startswith('0') else 0
    vals=[prefix+str(i).zfill(width) for i in range(start,end+1)]
    if not any(x in aliases for x in vals):return m.group()
    mapped=list(dict.fromkeys(canonical(x) for x in vals))
    chunks=[];run=[]
    for value in mapped:
        if run and (value.rsplit('-',1)[0]!=run[-1].rsplit('-',1)[0] or int(value.rsplit('-',1)[1])!=int(run[-1].rsplit('-',1)[1])+1):
            chunks.append(run);run=[]
        run.append(value)
    if run:chunks.append(run)
    return ', '.join(r[0] if len(r)==1 else r[0]+'–'+r[-1].rsplit('-',1)[1] for r in chunks)
for filename in ['SA03_dossier.md','SA03_directions.md']:
    path=OUT/filename;text=range_pat.sub(expand_alias_range,path.read_text())
    text=pat.sub(lambda m:canonical(m.group()),text)
    path.write_text(text)
def table(mapping,left='Category'):
    return '| '+left+' | Count |\n|---|---:|\n'+'\n'.join('| '+k+' | '+str(v)+' |' for k,v in mapping.items())
summary={
 'Indexed entries, each with exactly one verdict':counts['entries'],
 'Canonical items, including additional Codex-only material':counts['items'],
 'Canonical claim and explicit refinement records':counts['claims'],
 'Problem records, including resolved historical questions':counts['problems'],
 'Reading flags to decide on the scans':counts['readings'],
 'Ranked research directions':counts['directions'],
 'Two-endpoint-checked links':counts['confirmed_links'],
 'Separate unverified archive/publication leads':counts['link_leads'],
 'Separate earlier-project leads':counts['project_leads'],
 'Bibliography records':counts['bibliography_records'],
 'Check events':counts['check_events']}
verdicts={k:counts['verdicts'].get(k,0) for k in ['kept','merged','corrected','withdrawn','rests on a misreading']}
kinds={k:counts['item_kinds'].get(k,0) for k in ['conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other']}
classes={k:counts['claims_by_class'][k] for k in 'ABCDEF'}
statuses={k:counts['claims_by_status'].get(k,0) for k in ['proved there','proof sketched','stated without proof','corrected by himself later','false as stated / as transcribed','open on the pages']}
bib=(OUT/'SA03_references.bib').read_text();verification=collections.Counter(re.findall(r'\bnote\s*=\s*\{(verified|unverified)\}',bib))
body='''<!-- CENSUS_START -->
These are counts of the final canonical tables. Local part files preserve their
original audit identifiers and are not additional canonical records.

'''+table(summary,'Record')+'''

### Entry verdicts

'''+table(verdicts)+'''

The verdicts sum to 321. A corrected entry can also contain a reading alarm;
the absence of a separate “rests on a misreading” verdict does not mean that no
misreading was diagnosed. Corrections and source-check reasons state the exact
issue without deciding uncertain ink.

### Item kinds

'''+table(kinds)+'''

### Claims by literature class

'''+table(classes,'Class')+'''

A and D are zero under the conservative policy in §1. Zero A is not a finding
that Grothendieck never published these results: a matching publication does
not by itself date an undated sheet. Zero D is not a finding that every question
was solved: exact scope gaps are specified in C and unidentifiable fragments
in F. E includes transparently attributed standard and reused printed material.
The complete fate and dated present-status text, rather than the letter alone,
states whether a literal assertion is established, refuted, unresolved, or
still awaiting an exact historical comparison.

### Claims by source-status group

'''+table(statuses)+'''

The status grouping preserves the full qualified `status_on_pages` field in
`STATUS_GROUPS.tsv`. “False as stated / as transcribed” distinguishes a
mathematical failure of a literal witness from an authenticated error in the
author's live text. The open/unfinished group includes three cancelled drafts,
CL-SA03-1016, CL-SA03-1018 and CL-SA03-1066; their records explicitly identify
the withdrawal, and they are not presented as live conjectures. A modern
refinement can have its own claim ID, explicitly labelled as editorial, so
the 487 records are not a count of 487 independent propositions authored by
Grothendieck.

### Coverage and audit totals

'''+f'''All {counts['claims']} canonical claims have a documented search route and an
actual part search log. There are {counts['searches']} search-log records; these
include grouped searches, individual operations and documented access failures,
so they are not asserted to be {counts['searches']} distinct mathematical results.
The bibliography has {verification['verified']} opened-link records marked verified and
{verification['unverified']} records marked unverified. Repeated works can have separate
inspector keys; 195 is a count of bibliography records, not distinct works.

The 16 reviewed aliases comprise 12 item merges, one claim merge and three
problem merges. Before those aliases the seven audit parts contain 392 items,
488 claim records and 168 problems. All 321 indexed entries retain their
original stable source IDs. The final integrity report checks the exact-once
mapping, source ranges, referenced IDs, actual search-log coverage, reference
flags, check events and direction anchors. The source-byte audit confirms that
all 59 supplied files remain unchanged. These mechanical checks supplement
the recorded readings and mathematical checks; they do not replace them.
<!-- CENSUS_END -->'''
path=OUT/'SA03_dossier.md';text=path.read_text()
if '<!-- FINAL_CENSUS -->' in text:text=text.replace('<!-- FINAL_CENSUS -->',body)
else:text=re.sub(r'<!-- CENSUS_START -->.*?<!-- CENSUS_END -->',lambda m:body,text,flags=re.S)
path.write_text(text)
print(json.dumps({'census_inserted':True,'counts':counts},ensure_ascii=False,indent=2))
