"""Consolidate authored prose and validate the C audit against immutable indices.

This performs formatting and structural validation only. It does not generate
mathematical judgments or infer a verdict from a heading.
"""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib

ROOT=Path('/workspace/scratch/594d1dc856a9')
PART=ROOT/'SA04_work/parts/c'
PK='MPL_93_221-236+161-5'

def loadtsv(p):
    with p.open() as f:return list(csv.DictReader(f,delimiter='\t'))

# The first prose block was written through a transport that escaped some
# TeX delimiters twice and stripped others. Preserve commands, restore math.
text=(PART/'analysis.md').read_text().split('## 6. Determinant norms')[0].rstrip()
for a,b in [(r'\\[','$$'),(r'\\]','$$'),(r'\\(','$'),(r'\\)','$')]:
    text=text.replace(a,b)
text=text.replace(r'\(','(').replace(r'\)',')')
parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^\n$]*\$|\x60[^\x60]*\x60)',text)
restored=0
for i in range(0,len(parts),2):
    s=parts[i];out=[];pos=0
    while pos<len(s):
        if s[pos]!='(':
            out.append(s[pos]);pos+=1;continue
        start=pos;depth=1;pos+=1
        while pos<len(s) and depth:
            if s[pos]=='(':depth+=1
            elif s[pos]==')':depth-=1
            pos+=1
        if depth:raise AssertionError(('unbalanced legacy math delimiter',s[start:start+100]))
        out.append('$'+s[start+1:pos-1]+'$');restored+=1
    parts[i]=''.join(out)
text=''.join(parts)

start=text.index('Likewise, an operator represented')
end=text.index('\n## 3.',start)
text=text[:start]+r'''Likewise, an operator represented by an $\mathcal O$-linear map $P^i(E)\to F$ kills the specified horizontal generators exactly when it kills their $\mathcal O$-span. It therefore factors uniquely through $P^i(E)/\mathcal O\delta_i(E)$. For $M=E/N$, the same argument uses $\rho_i:E\to P^i(M)$ and gives $\Phi_i=P^i(M)/\mathcal O\rho_i(E)$. This is the ordinary universal property of a quotient, with the chosen left module structure. It proves C-SA04-416. [Scans 232–233, lines 279–306; EGAIV4 §16.8.4.]

The next assertion is distinct: the $\Phi_i$ form a strict projective system, determined by $M$ and $\rho_\infty$. The canonical transition $P^i(M)\to P^{i-1}(M)$ is surjective and sends $\rho_i(E)$ onto $\rho_{i-1}(E)$. It therefore induces a surjection $\Phi_i\to\Phi_{i-1}$. The compatible map $\rho_\infty$ determines each finite-order image and hence every quotient and transition. This proves C-SA04-417, which is expressly stated at scan 233, lines 308–312. It does not assert the converse integrability characterization: the source's next line 313 leaves additional conditions unspecified, and that separate issue remains C-SA04-418.
''' +text[end:]
if 'Choosing the homotopy data can change the class' not in text:
    marker='The caption placing'
    k=text.index(marker)
    text=text[:k]+r'''Choosing the homotopy data can change the class, as the indexed note already observes. Take an abelian sheaf $G$ with a torsor $P$ of nonzero class in $H^1(X,G)$, put $K'=\mathbf Z[0]$, $K''=G[1]$, and $u=0$. The differential in $\underline{\operatorname{Hom}}^\bullet(K',K'')$ is zero. Both $k=0$ and $k=1_G$ satisfy the additive compatibility. The first roof is zero; the second is the connecting morphism of the extension $0\to G\to\bar G\to\mathbf Z\to0$, hence is the nonzero torsor class, up to the shift convention. This supplies the precise canonicity qualification C-SA04-422; it is not a claim that the manuscript gives this example.

'''+text[k:]
text=text.rstrip()+'\n\n'+(PART/'proof_checks.md').read_text().strip()+'\n'
(PART/'analysis.md').write_text(text)

items=json.loads((PART/'items.json').read_text())
claims=json.loads((PART/'claims.json').read_text())
problems=json.loads((PART/'problems.json').read_text())
entries=loadtsv(PART/'entries.tsv')
readings=loadtsv(PART/'readings.tsv')
links=loadtsv(PART/'links.tsv')
events=loadtsv(PART/'CHECK_EVENTS.tsv')
searches=loadtsv(PART/'search_log.tsv')
index=loadtsv(ROOT/'source/SA04_notes/NOTES_INDEX.tsv')
expected={r['entry_id'] for r in index if r['package'] in [PK,'MPL_98']}
assert len(expected)==107
assert len(entries)==len({r['entry_id'] for r in entries})==107
assert {r['entry_id'] for r in entries}==expected

schemas={
 'items': 'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
 'claims': 'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
 'problems': 'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
    assert len(data)==len({r['id'] for r in data}),name
    for r in data:
        assert set(r)==set(schemas[name]),(name,r['id'],set(r)^set(schemas[name]))
        assert all(r[k] not in [None,'',[]] for k in schemas[name]),(name,r['id'])
itemids={r['id'] for r in items};claimids={r['id'] for r in claims}
itemmap={r['id']:r for r in items}
for r in entries:
    assert r['item_id'] in itemids
    assert r['entry_id'] in itemmap[r['item_id']]['sources'],r
    assert r['verdict'] in ['kept','corrected','withdrawn','rests on a misreading'] or r['verdict'].startswith('merged into item ')
kindset={'conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other'}
checkset={'agrees','overstates','understates','misreads','not on the page'}
statusset={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
for r in items:
    assert r['kind'] in kindset,(r['id'],r['kind'])
    assert r['check'] in checkset
    assert set(r['sources'])<=expected
for r in claims:
    assert set(r['items'])<=itemids
    assert r['status_on_pages'] in statusset,(r['id'],r['status_on_pages'])
    assert r['class'] in set('ABCDEF')
    assert r['confidence'] in {'high','medium','low'}
for r in problems:
    for o in r['occurrences']:
        assert o['claim'] in claimids
        assert set(o['items'])<=itemids

# Exact quoted words must occur in the declared line span, in the declared cote
# and scan. Composite range statements are deliberately checked as unions.
cache={};pagecache={}
def number_set(s):
    nums=set()
    for lo,hi in re.findall(r'(\d+)(?:-(\d+))?',s):
        nums.update(range(int(lo),int(hi or lo)+1))
    return nums
for r in items:
    path,span=r['lines'].split(':',1)
    if path not in cache:
        cache[path]=(ROOT/'source'/path).read_text().splitlines()
        cote=scan=None;pages=[]
        for line in cache[path]:
            m=re.search(r'\\cotefile\{([^}]+)\}',line)
            if m:cote=m[1]
            m=re.search(r'\\scanpage\{([^}]+)\}',line)
            if m:scan=int(m[1])
            pages.append((cote,scan))
        pagecache[path]=pages
    lines=cache[path];allowed=number_set(span)
    assert allowed and max(allowed)<=len(lines),(r['id'],span)
    quote=r['his_words'].removesuffix('...')
    loc=[n for n in allowed if quote in lines[n-1].strip()]
    assert loc,(r['id'],'quote outside declared line spans',quote)
    cotes=set(r['cote'].split(';'));scans=number_set(r['scans'])
    assert any(pagecache[path][n-1][0] in cotes and pagecache[path][n-1][1] in scans for n in loc),(r['id'],'quote cote/scan mismatch',loc)

bib=(PART/'references.bib').read_text()
keys=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M))
assert len(keys)==len(re.findall(r'^@\w+\{',bib,re.M))
for r in claims+problems:assert set(r['refs'])<=keys,(r['id'],set(r['refs'])-keys)
assert len(re.findall(r'  note = \{(?:verified|unverified)\}',bib))==len(keys)
assert len(searches)==len({r['claim_id'] for r in searches})==len(claims)
assert {r['claim_id'] for r in searches}==claimids
for r in searches:assert r['searches'] and r['primary_checks'] and r['result']
for r in links:
    assert r['kind'] in {'folder','published work','our projects'}
    assert set(r['note_ids'].split(';'))<=expected,(r['note_ids'])
    if r['kind']=='our projects':assert 'LEAD ONLY' in r['evidence']
types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
for r in events:
    assert r['type'] in types,(r['statement_id'],r['type'])
    assert r['statement_id'] in itemids|claimids|keys|{'C-SA04-620','C-SA04-647','C-SA04-648'},r['statement_id']
    if r['type']=="refuted, with the refined statement's id" and r['statement_id'] in claimids:
        claim=next(c for c in claims if c['id']==r['statement_id'])
        assert claim['status_on_pages']=='false as stated',(r['statement_id'],'refutation event attached to nonfalse source claim')

comp=(ROOT/'SA04_work/outputs/c_computations.txt').read_text()
assert 'All asserted symbolic identities and finite counterexample checks passed.' in comp
labels=set(line.split(' ',1)[0] for line in comp.splitlines())
for r in claims:
    m=re.search(r'labels ([^.]+)\.',r['computation'])
    if m:
        for label in m[1].split(','):assert label.strip() in labels,(r['id'],label)
for fn in ['c_manin_check.json','c_review_genus2.json']:
    result=json.loads((ROOT/'SA04_work/outputs'/fn).read_text());assert result,fn

required=['entries.tsv','items.json','claims.json','problems.json','readings.tsv','links.tsv','directions.md','references.bib','CHECK_EVENTS.tsv','analysis.md','search_log.tsv']
for name in required:assert (PART/name).stat().st_size>0,name
assert r'\\(' not in text and r'\\[' not in text
summary={
 'date':'2026-11-19','indexed_entries':len(entries),'items':len(items),
 'MPL98_composite_parents':8,'MPL98_nested_items':89,'claims':len(claims),
 'problems':len(problems),'readings':len(readings),'references':len(keys),
 'verdicts':dict(Counter('merged' if r['verdict'].startswith('merged') else r['verdict'] for r in entries)),
 'item_kinds':dict(Counter(r['kind'] for r in items)),
 'claim_statuses':dict(Counter(r['status_on_pages'] for r in claims)),
 'claim_classes':dict(Counter(r['class'] for r in claims)),
 'links':dict(Counter(r['kind'] for r in links)),
 'archive_leads':len(loadtsv(PART/'archive_leads.tsv')),
 'claim_search_rows':len(searches),'actual_discovery_queries':len(loadtsv(PART/'search_requests.tsv')),
 'check_events':len(events),'analysis_words':len(text.split()),
 'restored_legacy_math_delimiters':restored,
 'result':'All index, exact-schema, vocabulary, identifier, source-quote locator, reference, search, link and saved-computation checks passed.',
 'files':{name:hashlib.sha256((PART/name).read_bytes()).hexdigest() for name in required}}
(PART/'VALIDATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
