"""Audit source coverage, one-master generation, apparatus identity and PDF links."""
from pathlib import Path
import csv,collections,hashlib,json,re
import fitz
from build_readers import group,select_variant,link_marks,texescape
P=Path(__file__).resolve().parents[1];R=P/'records';D=P/'readers'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read_tsv(path):return list(csv.DictReader(path.open(),delimiter='\t'))
def calls(s,name,n):
    result=[]
    for m in re.finditer(r'\\'+name+r'\{',s):
        args=[];pos=m.end()-1
        for _ in range(n):a,pos=group(s,pos);args.append(a)
        result.append(args)
    return result
meta=json.loads((P.parent/'inputs/text/records/PAGES_PS.json').read_text())
meta.sort(key=lambda m:(m['text']=='brown',int(m['cote'].split('-')[1]),int(m['site'])))
expected_keys=[m['key'] for m in meta];lookup={m['key']:m for m in meta}
expected_urls={f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{m['cote']}.pdf#page={m['pdf_page']}":m for m in meta}
checked={x.stem for x in (P/'checked_pages').glob('*.tex')}
coverage=json.loads((R/'COVERAGE_AUDIT.json').read_text())
changes=read_tsv(R/'CHANGES_EN.tsv');change_by_id={r['source_id']:r for r in changes}
master=(D/'PS_EN_master_annotated.tex').read_text()
blocks=re.findall(r'(?ms)^%% BEGIN SOURCE ([^\n]+)\n(.*?)\n%% END SOURCE \1\n',master)
body=master[master.index('\\begin{document}'):]
issues=[];source_results=[];variant_ids=[];source_link_expectations={}
if checked!=set(expected_keys):issues.append('Checked source key set differs from the706-page metadata.')
if [k for k,s in blocks]!=expected_keys:issues.append('Master source order/coverage differs from archive metadata.')
expected_source_calls=[[m['key'],m['cote']+'/'+str(m['site']),f"https://grothendieck.umontpellier.fr/web/viewer.html?file=../{m['cote']}.pdf\\#page={m['pdf_page']}"] for m in meta]
if calls(body,'pssource',3)!=expected_source_calls:issues.append('Ordered source keys, scan labels or archive URLs differ from metadata.')
for key,annotated in blocks:
    raw=(P/'checked_pages'/(key+'.tex')).read_text();diplomatic=select_variant(annotated,0);corrected=select_variant(annotated,1)
    exact=diplomatic==raw
    if not exact:issues.append('Diplomatic branch differs from canonical checked source: '+key)
    scan=calls(diplomatic,'scanpage',1);m=lookup[key];expected_scan=m['cote']+'/'+str(m['site'])
    if scan!=[[expected_scan]]:issues.append('Scan mark differs from metadata: '+key)
    variants=calls(annotated,'var',4)
    for before,after,kind,sid in variants:
        variant_ids.append(sid);c=change_by_id.get(sid)
        if c is None or (c['typescript_reading'],c['corrected_reading'],c['kind'])!=(before,after,kind):issues.append('Variant/change-log mismatch: '+sid)
        if not c or not c['reason'].strip() or not c['evidence_id'].strip():issues.append('Variant lacks reason or source evidence ID: '+sid)
    diplomatic_marks=link_marks(diplomatic);corrected_marks=link_marks(corrected)
    apparatus_marks=link_marks(''.join(before+after for before,after,kind,sid in variants))
    source_link_expectations[key]={'diplomatic':diplomatic_marks,'reading':corrected_marks,'corrected_apparatus':{name:corrected_marks[name]+apparatus_marks[name] for name in corrected_marks}}
    source_results.append({'key':key,'checked_sha256':sha(P/'checked_pages'/(key+'.tex')),'diplomatic_branch_exact':exact,'diplomatic_marks':diplomatic_marks,'corrected_running_marks':corrected_marks,'apparatus_marks':apparatus_marks,'variants':len(variants)})
manifest_path=R/'BUILD_MANIFEST.json'
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else []
if [m['key'] for m in manifest]!=expected_keys:issues.append('Link-count build manifest lacks the complete ordered source set.')
for m in manifest:
    if m.get('expected_link_marks')!=source_link_expectations.get(m['key']):issues.append('Manifest link expectations differ from independently selected source branches: '+m['key'])
entries=calls(body,'psentry',6)
entry_ids=[x[0] for x in entries]
if len(set(variant_ids))!=len(variant_ids):issues.append('Duplicate master variant IDs.')
if variant_ids!=[c['source_id'] for c in changes]:issues.append('Master variants and change-log sequence differ.')
if entry_ids!=variant_ids:issues.append('Apparatus does not have exactly one entry per master variant in order.')
for sid,num,kind,before,after,reason in entries:
    c=change_by_id[sid]
    if kind!=texescape(c['kind']) or reason!=texescape(c['reason']):issues.append('Apparatus kind/reason differs from master change record: '+sid)
    if before not in [c['typescript_reading'],'$'+c['typescript_reading']+'$']:issues.append('Apparatus old reading mismatch: '+sid)
    if after not in [c['corrected_reading'],'$'+c['corrected_reading']+'$']:issues.append('Apparatus corrected reading mismatch: '+sid)
rights="The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down."
credit='AI-transcribed by Claude Opus 5.5 (Anthropic, effort high); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic)'
brown="The translation in the appendix is R. Brown's, prepared with assistance from L. Breen and J-L. Loday, as his note says; the rights in it belong to its translator or his heirs."
forms={};pdfs={}
for stem in ['PS_EN_diplomatic','PS_EN_corrected_apparatus','PS_EN_reading','PS_EN_master_annotated','PS_GUIDE']:
    tex=D/(stem+'.tex');s=tex.read_text();same=True if stem=='PS_GUIDE' else s[s.index('\\begin{document}'):]==body
    if not same:issues.append('Form body differs from the single annotated master: '+stem)
    external=re.findall(r'\\(?:input|include|includegraphics)\s*\{([^}]+)\}',s)
    if external:issues.append('Standalone source has external file dependencies: '+stem)
    if any(x not in s for x in [rights,credit,brown]):issues.append('Required verbatim credits/rights missing: '+stem)
    if 'WORKING EDITION:' in s or 'WORKING GUIDE:' in s:issues.append('Working-status label remains: '+stem)
    logs=sorted((P/'logs').glob(stem+'_readers_run*.json'))
    build=json.loads(logs[-1].read_text()) if logs else {}
    if build.get('source_sha256')!=sha(tex) or build.get('exit')!=0 or build.get('source_changed_during_build'):issues.append('Current source lacks a matching successful build: '+stem)
    if build.get('widest_pt',999)>2 or build.get('missing_character_lines',1):issues.append('Unresolved build typography gate: '+stem)
    if build.get('link_mark_count_mismatches') or build.get('unexpected_link_mark_keys'):issues.append('Logical link-count mismatch: '+stem)
    if stem!='PS_GUIDE':
        required_link_fields={'shipped_logical_link_marks','nested_marks_sharing_an_outer_link','link_mark_count_mismatches','unexpected_link_mark_keys'}
        absent=sorted(required_link_fields-set(build))
        if absent:issues.append('Build lacks required logical link-count evidence: '+stem+' ('+', '.join(absent)+')')
        mode='diplomatic' if stem=='PS_EN_diplomatic' else 'reading' if stem=='PS_EN_reading' else 'corrected_apparatus'
        expected={(key,name):count for key,modes in source_link_expectations.items() for name,count in modes[mode].items()}
        expected_totals={name:sum(count for (key,kind),count in expected.items() if kind==name) for name in ['scanpage','unsure','illegible']}
        reported=build.get('shipped_logical_link_marks')
        if not isinstance(reported,dict) or {name:reported.get(name,0) for name in expected_totals}!=expected_totals:issues.append('Shipped logical link totals differ from source branches: '+stem)
        logpath=P/build['log'] if isinstance(build.get('log'),str) else None
        marks=re.findall(r'PS-LINK-SHIP\|(scanpage|unsure|illegible)\|([^|\s]+)\|(\d+)\|(outer|nested)',logpath.read_text()) if logpath is not None and logpath.exists() else []
        if not marks:issues.append('Successful build has no independently readable shipped link markers: '+stem)
        observed=collections.Counter((key,kind) for kind,key,number,scope in marks)
        discrepancies=[{'key':key,'kind':kind,'expected':expected.get((key,kind),0),'observed':observed[(key,kind)]} for key,kind in sorted(set(expected)|set(observed)) if observed[(key,kind)]!=expected.get((key,kind),0)]
        if discrepancies:issues.append('Per-source shipped link markers differ from source branches: '+stem)
        if build.get('nested_marks_sharing_an_outer_link')!=sum(scope=='nested' for kind,key,number,scope in marks):issues.append('Nested link-marker count differs from build log: '+stem)
    forms[stem]={'source_sha256':sha(tex),'master_body_identical':same,'standalone_external_dependencies':external,'latest_build_record':str(logs[-1].relative_to(P)) if logs else None}
    pdfpath=D/(stem+'.pdf')
    if not pdfpath.exists():issues.append('Missing PDF: '+stem);continue
    if build.get('pdf_sha256')!=sha(pdfpath):issues.append('Current PDF hash differs from its successful build record: '+stem)
    pdf=fitz.open(pdfpath);uris=[];invalid=[];distinct_by_cote=collections.defaultdict(set);links_by_cote=collections.Counter()
    for number,page in enumerate(pdf,1):
        for link in page.get_links():
            uri=link.get('uri')
            if not uri:continue
            uris.append(uri)
            if 'grothendieck.umontpellier.fr/web/viewer.html?' in uri:
                m=expected_urls.get(uri)
                if m is None:invalid.append({'page':number,'uri':uri})
                else:
                    cote='Brown (134-2)' if m['text']=='brown' else m['cote'];distinct_by_cote[cote].add(uri);links_by_cote[cote]+=1
    archive={u for u in uris if 'grothendieck.umontpellier.fr/web/viewer.html?' in u}
    if stem!='PS_GUIDE' and archive!=set(expected_urls):issues.append('Archive link targets do not cover exactly706 source pages: '+stem)
    if invalid:issues.append('Archive links have invalid source targets: '+stem)
    pdfs[stem]={'pdf_sha256':sha(pdfpath),'pages':len(pdf),'uri_annotations':len(uris),'archive_annotations':sum(u in expected_urls for u in uris),'distinct_source_pages':len(archive),'distinct_pages_by_cote':{k:len(v) for k,v in distinct_by_cote.items()},'archive_annotations_by_cote':dict(links_by_cote),'invalid_archive_links':invalid,'logical_shipped_marks':build.get('shipped_logical_link_marks',{}),'nested_marks_sharing_a_source_link':build.get('nested_marks_sharing_an_outer_link',0)}
guide=json.loads((R/'GUIDE_MANIFEST.json').read_text())
if not guide.get('complete') or not guide.get('numbered_sections_in_complete_source_order'):issues.append('Guide is not complete in source section order.')
if not coverage.get('complete'):issues.append('Source review coverage audit is not complete.')
replay=json.loads((R/'CHANGE_REPLAY_AUDIT.json').read_text())
if replay['pages']!=706 or replay['equal_pages']!=706:issues.append('Recorded physical edits do not yet reconstruct every checked source.')
result={'complete':not issues,'issues':issues,'source_pages':len(blocks),'master_variants':len(variant_ids),'apparatus_entries':len(entries),'forms':forms,'pdfs':pdfs,'source_results':source_results,'guide_paragraphs':len(guide['paragraphs']),'guide_numbered_sections':guide.get('numbered_sections')}
(R/'FINAL_STRUCTURE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['source_results','forms','pdfs','guide_numbered_sections']}))
