"""Assemble independently read package records with explicit editorial mergers.

No verdict is inferred from a heading, keyword, or transcription cue. The
MERGERS below are decisions made after reading the package records and the
relevant passages. Original records remain in work/ for audit. Aliases preserve
the meaning of references made before cross-package consolidation.
"""
import argparse, copy, csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ['p108', 'p116', 'p118']

MERGERS = [
    ('SA27-2', ['SA27-412', 'SA27-413'],
     'The saturation agenda recurs in 108 and the explicit localization-invertibility theorem and its presheaf corollary in 118. The different senses and logical strengths are preserved by occurrence.'),
    ('SA27-150', ['SA27-401'],
     'The same historical question about the first strong W(7)/W(7 bis) occurrence is checked against both supplied packages; absence is bounded to these texts.'),
    ('SA27-151', ['SA27-202', 'SA27-402', 'SA27-715'],
     'The same totality-versus-filteredness comparison and its Isbell–Mitchell contextual lead recur. Product/diagonal totality, final-image totality, and exactness of abelian colimits remain different predicates.'),
    ('SA27-203', ['SA27-403'],
     'The relative Theorem A chronology question is one issue. The 117 pages do not state the relative schema; the now-supplied 118 pages use common-base slices. The latter mathematical leaves are undated.'),
    ('SA27-146', ['SA27-215', 'SA27-430'],
     'The crossing-Hom collage is the same ordinary construction: an earlier-run reconstruction in the 115/116 notes and an explicit authorial construction in 118/017. It is distinguished from the Isbell envelope.'),
    ('SA27-251', ['SA27-703'], 'Same NR1 finite-monoid external-result comparison, checked against the two different manuscript packages.'),
    ('SA27-252', ['SA27-704'], 'Same NR2 cohomologically bounded Miller theorem comparison; no manuscript occurrence in either package.'),
    ('SA27-253', ['SA27-705'], 'Same NR3 cardinal Kan–Thurston/groupoid ind-object comparison; the private result is not re-proved.'),
    ('SA27-254', ['SA27-706'], 'Same NR4 sphere-retract/cardinality comparison; loop and suspension pictures do not assert this theorem.'),
    ('SA27-255', ['SA27-707'], 'Same NR5 finite RP2-poset arrow-bound comparison; no enumeration is supplied by these pages.'),
    ('SA27-256', ['SA27-708'], 'Same NR6 small-category sphere-census comparison; no minimality or uniqueness claim is on these pages.'),
    ('SA27-257', ['SA27-709'], 'Same NR7 reversible-localizer/spectral-detection comparison; the local gluing statements have different quantifiers.'),
    ('SA27-258', ['SA27-710'], 'Same NR8 reported counterexample to later strong W7; neither Hot7 nor 118 ordinary-pushout failure is that assertion.'),
    ('SA27-259', ['SA27-711'], 'Same NR9 homology-localizer/Loc7F comparison; the coefficient-specific obstruction is not present here.'),
    ('SA27-260', ['SA27-712'], 'Same NR10 path-presheaf/final-image-totality comparison; product totality is not substituted.'),
    ('SA27-261', ['SA27-714'], 'Same NR12 finite-monoid obstruction for RP2; the outside result remains an attributed lead.'),
    ('SA27-262', ['SA27-716'], 'Same known-after-all Nielsen-realization attribution; there is no manuscript occurrence or supplied private proof.'),
    ('SA27-263', ['SA27-717'], 'Same incorrect Cisinski Corollary 4.2.22 attribution; the opened final edition proves filtered-colimit closure there, not accessibility.'),
]

OVERRIDES = {
 'SA27-2': {
  'kind':'unproved claim',
  'statement':'108/003 lists saturation of W and W_A without defining the sense. 118/040–041 asserts strong saturation: a functor belongs to W if and only if it becomes invertible in W⁻¹Cat; it also asserts this for the inverse-image class W_A under the category-of-elements functor.',
  'reconstruction':'The 108 phrase alone does not identify strong saturation. In 118 the localization criterion is explicit. The telescope proof needs its fraction, factorization and filtered-union inputs; inverse-image strong saturation for W_A follows formally once W is strongly saturated.',
  'check_reason':'The repeated saturation subject is consolidated without reading the stronger 118 definition backwards into 108. Its two distinct claims and their separate proof obligations are retained in the claims map.'},
 'SA27-150': {
  'kind':'reading question',
  'statement':'The strong reverse gluing principle later named W(7 bis)/W(7) is not stated in these supplied 108–118 leaves. 117 Hot7 is a Hom-surjectivity request; 118 gives conditioned forward gluing and ordinary-pushout failures. The exact later witness is Der XII §V.2.1, manuscript pp.75–78.',
  'reconstruction':'This is a bounded chronology audit, not a claim to have found the first occurrence anywhere in the archive. The later authorial assertion is distinguished from its unwritten verification and from the unavailable private counterexample report.',
  'check_reason':'Both the positive assertions and their directions were read. The shared number seven does not identify Hot7 with later strong W7.'},
 'SA27-151': {
  'kind':'reading question',
  'statement':'No supplied leaf asserts that final-image total asphericity forces filteredness. 114 and 118 discuss product/diagonal totality; 117 has a loose total-0-asphericity fragment and a filtered-cofinality question. The earlier research comparisons and Isbell–Mitchell lead concern further predicates, including exactness of abelian colimits.',
  'reconstruction':'The later Der XII §V.2.3 definition is expressly different from the Pursuing Stacks product notion. Its separate earlier Der II proposition, counterexample and renewed conjecture are tracked at manuscript pp.36–36ter. Private research claims are retained as leads, not inserted as manuscript theorems.',
  'check_reason':'The precise occurrences support distinct definitions and questions. Aggregate context entries remain separate registers where one source entry discusses many different results.'},
 'SA27-203': {
  'kind':'reading question',
  'statement':'117 does not give the common-base relative Theorem A axiom. In 118/026 the coproduct proof uses slices over a discrete base, and 118/040 invokes L3 for slices over I. These are positive uses of the relative principle, but the defining Loc2–3 are not expanded on 118/015 and these mathematical sheets have no established 1983 date.',
  'reconstruction':'The relative schema is inferred from the proof applications, not supplied as a missing transcription. The reused notice dated 28 April 1983 cannot date the mathematics. The later explicit comparison is Der XVI §1, manuscript p.3.',
  'check_reason':'The earlier package absence remains correct within its scope. The combined dossier adds the now-supplied positive evidence from 118 without claiming priority or an exact date.'},
 'SA27-146': {
  'kind':'unproved claim',
  'statement':'For categories U,Y and H:U^op×Y→Set, their collage has the objects and internal arrows of both categories, mixed arrows U→Y given by H, and no arrows Y→U; the two actions of H give composition. Conversely a category split into a sieve U and complementary cosieve Y is recovered this way.',
  'reconstruction':'The 115 notes and the continuation after116/008 propose this as an earlier-run reconstruction;118/017 writes the crossing bifunctor and construction explicitly. The topos gluing criterion of116 and the pairing-triple Isbell envelope of115 are separate statements.',
  'check_reason':'This is one ordinary categorical object at all three occurrences. Attribution changes with the occurrence and is preserved in occurrence_details.'},
}

def tsv_read(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))

def tsv_write(path, rows, fields):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writeheader();w.writerows(rows)

def id_num(s):return int(s.rsplit('-',1)[-1])

def normalise_item(q):
    q=copy.deepcopy(q)
    c=q['cote']
    q['cote']=[str(v) for v in c] if isinstance(c,list) else re.findall(r'\d+',str(c))
    scans=q['scans']
    if q['id']=='SA27-C008' and not isinstance(scans,dict):
        # Explicitly read locators:108/003 lines31–33,114/002 lines1007,1016.
        # The local list[2,3] did not preserve the cote-to-scan association.
        scans={'108':[3],'114':[2]}
    if isinstance(scans,dict):q['scans']={str(k):[int(v) for v in vs] for k,vs in scans.items()}
    elif len(q['cote'])==1:q['scans']={q['cote'][0]:[int(v) for v in scans]}
    else:
        assert not scans, 'Do not assign ambiguous scan numbers across cotes.'
        q['scans']={}
    if not isinstance(q['lines'],list):q['lines']=[str(q['lines'])]
    return q

def occurrence(q):
    return {k:copy.deepcopy(q[k]) for k in ['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason']}

def stage1():
    original=[]; entries=[]
    for p in PARTS:
        original.extend(json.loads((ROOT/'work'/p/'items.json').read_text()))
        entries.extend(tsv_read(ROOT/'work'/p/'entries.tsv'))
    items={q['id']:normalise_item(q) for q in original}
    assert len(items)==len(original)
    aliases={q['id']:q['id'] for q in original}
    # The historical W7 source was bundled with actual Hot7 locally. Separate
    # that source membership before merging the same historical question.
    h='MPL_116+117#1'
    assert h in items['SA27-201']['sources']
    items['SA27-201']['sources'].remove(h)
    history_108=occurrence(items['SA27-150'])
    items['SA27-150']['sources'].append(h)
    items['SA27-150']['occurrence_details']=[history_108,{
        'id':'SA27-201-history','sources':[h],'kind':'reading question',
        'cote':['117'],'scans':{'117':[23]},'lines':['117/023:981–1000'],
        'his_words':'surjective sur les flèches',
        'statement':'The earlier notes correctly distinguish Hot7 from later strong reverse W7.',
        'reconstruction':'Historical comparison; actual Hot7 remains item SA27-201.',
        'check':'agrees','check_reason':'The Hom-lifting formula has a different conclusion from reverse excision.'}]
    for target, absorbed, reason in MERGERS:
        base=items[target]
        details=base.get('occurrence_details',[occurrence(base)])
        for old in absorbed:
            other=items.pop(old)
            details.extend(other.get('occurrence_details',[occurrence(other)]))
            base['sources'].extend(other['sources'])
            base['cote']=sorted(set(base['cote']+other['cote']),key=int)
            for c,ss in other['scans'].items():base['scans'][c]=sorted(set(base['scans'].get(c,[])+ss))
            base['lines'].extend(f"{','.join(other['cote'])}: {s}" for s in other['lines'])
            aliases[old]=target
        base['occurrence_details']=details
        base['merge_reason']=reason
        base['his_words']='; '.join(dict.fromkeys(str(x['his_words']) for x in details))
        if target in OVERRIDES:base.update(OVERRIDES[target])
        elif absorbed:
            base['statement']=' '.join(dict.fromkeys(x['statement'] for x in details))
            base['reconstruction']=' '.join(dict.fromkeys(x['reconstruction'] for x in details))
            base['check_reason']=' '.join(dict.fromkeys(x['check_reason'] for x in details))
    # Include the new117 occurrence in the W7 top-level locator, too.
    items['SA27-150']['cote']=sorted(set(items['SA27-150']['cote']+['117']),key=int)
    items['SA27-150']['scans']['117']=[23]
    items['SA27-150']['lines'].append('117/023:981–1000')
    source_to_item={s:q['id'] for q in items.values() for s in q['sources']}
    assert len(source_to_item)==sum(len(q['sources']) for q in items.values())
    for e in entries:
        # Same manually authored verdict, with the target already in item_id.
        if e['verdict']=='merged into':e['verdict']='merged'
        previous=e['item_id']; e['item_id']=source_to_item[e['entry_id']]
        if previous!=e['item_id']:
            if e['verdict'] in ['kept','merged']:e['verdict']='merged'
            e['reason']+=' Cross-package consolidation: '+items[e['item_id']]['merge_reason']
    order={q['entry_id']:i for i,q in enumerate(tsv_read(ROOT.parent/'source/SA27_notes/NOTES_INDEX.tsv'))}
    entries.sort(key=lambda q:order[q['entry_id']])
    data=sorted(items.values(),key=lambda q:id_num(q['id']))
    (ROOT/'SA27_items.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    tsv_write(ROOT/'SA27_entries.tsv',entries,['entry_id','item_id','verdict','reason'])
    (ROOT/'work/item_aliases.json').write_text(json.dumps({k:v for k,v in aliases.items() if k!=v},indent=2)+'\n')
    (ROOT/'work/cross_package_mergers.json').write_text(json.dumps([{'canonical_item':a,'absorbed_items':b,'reason':c} for a,b,c in MERGERS],ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'stage':1,'entries':len(entries),'package_items':len(original),'consolidated_items':len(data),'cross_package_mergers':sum(len(x[1]) for x in MERGERS),'source_membership_adjustment':'116#1 moved from actual Hot7 to the historical strong-W7 audit','verdict_generation':'Manually read package verdicts plus explicit editorial mergers; no text cue classification.'},indent=2))
    return aliases

# These aliases identify the same opened work, not different editions of it.
# The2015 and2021 Pursuing Stacks electronic editions remain separate keys.
BIB_ALIASES={
 'p108-Cisinski2006':'Cisinski2006',
 'p108-Rezk1998':'Rezk1998',
 'p108-SGA4I':'SGA4I',
 'p108-EGAIII1':'EGAIII1',
 'p108-PSPublication':'PSVolumeI2022',
 'p108-MaltsiniotisBibliography':'MaltsiniotisBibliography',
 'p108-PS':'PS2021',
 'p108-Thomason1980':'Thomason1980',
 'Cis2006Final':'Cisinski2006',
 'Cis2026MO':'Cisinski2026MO',
 'DerXIIbRoot':'DerXII5',
 'DerXIIAppRoot':'DerXIIApp',
 'DerIIRoot':'DerII',
 'DerXVIRoot':'DerXVI',
 'RezkAuthorIndex118':'RezkBibliography',
}

# Where one reader only opened metadata and another read the full primary work,
# select the record that will not understate the combined evidence. All source
# records and their differently scoped annotations remain in work/.
BIB_PREFERRED={
 'EGAIII1':'work/p108/references.bib',
 'PS2021':'work/p118/references.bib',
 'Thomason1980':'work/p118/references.bib',
}

PROBLEM_MERGERS=[
 ('MP-SA27-02','MP-SA27-224','The saturation agenda on108 and its explicit strong-saturation proof attempt on118 are one recurring open step; the ambiguity of108 is retained.'),
 ('MP-SA27-15','MP-SA27-104','The Hom/mapping-homotopy-type programme recurs from108 to the more explicit higher-arrow discussion in117; this does not merge the separate internal/global-Hom problem.'),
]

def replace_text(s, mapping):
    if not mapping:return s
    pattern=r'(?<![\w-])('+ '|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?![\w-])'
    return re.sub(pattern,lambda m:mapping[m.group(1)],s)

def recursive_replace(x,mapping):
    if isinstance(x,str):return replace_text(x,mapping)
    if isinstance(x,list):return [recursive_replace(v,mapping) for v in x]
    if isinstance(x,dict):return {k:recursive_replace(v,mapping) for k,v in x.items()}
    return x

def all_stages(aliases):
    mapping={**{k:v for k,v in aliases.items() if k!=v},**BIB_ALIASES,
             **{old:new for new,old,_ in PROBLEM_MERGERS}}
    claims=[];problems=[];readings=[];links=[];events=[]
    for p in PARTS:
        d=ROOT/'work'/p
        for name in ['claims.json','problems.json','readings.tsv','links.tsv','check_events.tsv','references.bib','search_log.tsv']:
            if not (d/name).is_file():raise RuntimeError(f'Package output not yet written: {d/name}')
        part_claims=recursive_replace(json.loads((d/'claims.json').read_text()),mapping)
        for q in part_claims:
            q=normalise_item(q);q['evidence_base']=f'work/{p}';claims.append(q)
            if q['id']=='SA27-C433':
                q['search_ids']=list(dict.fromkeys(q['search_ids']+['R011','P116-R118-01','P116-R118-02','P116-R118-03']))
            elif q['id']=='SA27-C429':
                q['search_ids']=list(dict.fromkeys(q['search_ids']+['R011']))
        part_problems=json.loads((d/'problems.json').read_text())
        for q in part_problems:q['evidence_base']=f'work/{p}'
        problems.extend(part_problems)
        readings.extend(tsv_read(d/'readings.tsv'))
        links.extend(recursive_replace(tsv_read(d/'links.tsv'),mapping))
        events.extend(recursive_replace(tsv_read(d/'check_events.tsv'),mapping))
    links.extend(recursive_replace(tsv_read(ROOT/'research/root_links.tsv'),mapping))
    events.extend(recursive_replace(tsv_read(ROOT/'research/root_check_events.tsv'),mapping))
    # Supplemental audit refinements must not be counted as authorial claims.
    refinements=[];authorial=[]
    for q in claims:
        if 'modern' in q.get('origin','').lower() or q['status_on_pages'].lower().startswith('not applicable'):
            q.setdefault('origin','modern refinement by this run');refinements.append(q)
        else:q.setdefault('origin','manuscript assertion, construction, question or hypothesis');authorial.append(q)
        q['items']=list(dict.fromkeys(q['items']))
    pmap={q['id']:q for q in problems}
    for target,old,reason in PROBLEM_MERGERS:
        a=pmap[target];b=pmap.pop(old)
        a['occurrence_details']=[copy.deepcopy(a),copy.deepcopy(b)]
        # Preserve the original occurrence representation instead of guessing
        # a scan from the occurrence's prose.
        oa=a['occurrences'] if isinstance(a['occurrences'],list) else [a['occurrences']]
        ob=b['occurrences'] if isinstance(b['occurrences'],list) else [b['occurrences']]
        a['occurrences']=oa+ob
        for field in ['as_he_states','plausible_today','why_open','worth']:
            a[field]='Earlier occurrence: '+str(a[field])+' Further occurrence: '+str(b[field])+' Consolidation scope: '+reason
        a['state_of_art']=[
            {'occurrence':target,'account':copy.deepcopy(a['state_of_art'])},
            {'occurrence':old,'account':copy.deepcopy(b['state_of_art'])}]
        a['refs']=list({json.dumps(v,sort_keys=True):v for v in a['refs']+b['refs']}.values())
        a['merge_reason']=reason
        if target=='MP-SA27-02':
            # The108 question was an editorial question about terminology; the
            #118 occurrence is the author's unfinished strong-saturation proof.
            # Preserve both origins by occurrence, and count the recurring
            #authorial proof obligation once in the main register.
            a['title']='Saturation and the strong-saturation proof'
            a['origin']='authorial unfinished proof, with an earlier terminology audit attached'
            a['origin_basis']='The authorial open step is the telescope/fraction argument on118/040–041. The108 wording alone supplied a terminology question to the earlier notes, not an additional authorial question. Original origins remain in occurrence_details.'
    context=[];modern_questions=[];author_problems=[]
    for p in pmap.values():
        p=recursive_replace(p,mapping)
        if 'historical/editorial' in p.get('origin','').lower():context.append(p)
        elif 'modern audit' in p.get('origin','').lower():modern_questions.append(p)
        else:author_problems.append(p)
    # The dictionary of aliases is itself part of the auditable deliverable.
    (ROOT/'work/problem_aliases.json').write_text(json.dumps({old:new for new,old,_ in PROBLEM_MERGERS},indent=2)+'\n')
    (ROOT/'work/reference_aliases.json').write_text(json.dumps(BIB_ALIASES,indent=2)+'\n')
    for name,data in [('SA27_claims.json',authorial),('SA27_problems.json',author_problems),
                      ('research/modern_refinements.json',refinements),('research/context_questions.json',context)]:
        (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    (ROOT/'research/modern_questions.json').write_text(json.dumps(modern_questions,ensure_ascii=False,indent=2)+'\n')
    # Exact duplicate reading alarms are folded; different alternatives at one
    # locus remain separate. No reading is chosen and no source is edited.
    readings=list({json.dumps(q,sort_keys=True):q for q in readings}.values())
    links=list({json.dumps(q,sort_keys=True):q for q in links}.values())
    tsv_write(ROOT/'SA27_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
    tsv_write(ROOT/'SA27_links.tsv',links,['kind','from','to','what','evidence','note_ids'])
    for kind,name in [('folder','folder_links'),('published work','published_links'),('our projects','project_links')]:
        tsv_write(ROOT/f'research/{name}.tsv',[q for q in links if q['kind']==kind],['kind','from','to','what','evidence','note_ids'])
    # Each package's detailed check events remain recoverable under its old IDs;
    # the master ledger points to the canonical items and reference keys.
    tsv_write(ROOT/'CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
    # Parse whole BibTeX entries using their entry starts; nested braces remain
    # untouched. Preferred records are loaded first; equivalent aliases retain
    # source versions in each package's bibliography and search ledger.
    bib_records={};provenance=[];selected_sources={}
    for path in [ROOT/'research/root_references.bib']+[ROOT/'work'/p/'references.bib' for p in ['p116','p108','p118']]:
        s=path.read_text();matches=list(re.finditer(r'(?m)^@\w+\{([^,]+),',s))
        for i,m in enumerate(matches):
            original=m.group(1);key=BIB_ALIASES.get(original,original)
            record=s[m.start():matches[i+1].start() if i+1<len(matches) else len(s)].strip()
            record=record[:record.index('{')+1]+key+record[record.index(','):]
            source=str(path.relative_to(ROOT))
            provenance.append({'original_key':original,'canonical_key':key,'source':source})
            if key not in bib_records or BIB_PREFERRED.get(key)==source:
                bib_records[key]=record;selected_sources[key]=(source,original)
    for row in provenance:
        row['selected']=selected_sources[row['canonical_key']]==(row['source'],row['original_key'])
    (ROOT/'SA27_references.bib').write_text('% Consolidated opened-reference records. Exact result checks are in the search ledgers.\n\n'+'\n\n'.join(bib_records[k] for k in sorted(bib_records))+'\n')
    (ROOT/'research/bibliography_provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n')
    search_index=[];search_locations={}
    search_paths=[ROOT/'research/root_search_log.tsv']+sorted((ROOT/'work').glob('*/*search_log.tsv'))
    for path in search_paths:
        for row in tsv_read(path):
            sid=row['search_id'];relative=str(path.relative_to(ROOT))
            assert sid not in search_locations or search_locations[sid]==relative,f'Search namespace collision {sid}'
            search_locations[sid]=relative
            search_index.append({'search_id':sid,'ledger':relative,'record':row})
    (ROOT/'research/search_index.json').write_text(json.dumps(search_index,ensure_ascii=False,indent=2)+'\n')
    tsv_write(ROOT/'research/claim_search_links.tsv',[
        {'claim_id':q['id'],'search_id':sid,'ledger':search_locations.get(sid,'MISSING')}
        for q in claims for sid in q.get('search_ids',[])],['claim_id','search_id','ledger'])
    # Update authored overview/directions citations to canonical aliases only.
    for name in ['SA27_dossier.md','SA27_directions.md']:
        path=ROOT/name
        if path.exists():path.write_text(replace_text(path.read_text(),mapping))
    print(json.dumps({'stage':'all package tables assembled','authorial_claims':len(authorial),
      'modern_refinements':len(refinements),'authorial_problems':len(author_problems),
      'context_questions':len(context),'modern_audit_questions':len(modern_questions),'readings':len(readings),'links':len(links),
      'references':len(bib_records),'check_events':len(events)},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--stage1',action='store_true');args=parser.parse_args()
    aliases=stage1()
    if not args.stage1:all_stages(aliases)
