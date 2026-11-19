"""Bounded read-only integration QA. Writes only its own integration reports.

The assembler prefix is evaluated only up to (but excluding) its first output
write, and only to inspect in-memory aliases/merged records. No finalizer or
source-owner file is modified. Original source records are compared by IDs and
field unions; this is structural verification, not new mathematical adjudication.
"""
from pathlib import Path
import json,re,ast,hashlib,collections,copy

W=Path(__file__).resolve().parents[1]
overview=W/'integration/overview.md'
program=W/'programs/finalize_dossier.py'
text=overview.read_text();code=program.read_text()
tree=ast.parse(code)
prefix=[]
for node in tree.body:
    # First actual write is the loop dumping the three integrated JSON registers.
    if not isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
        calls=[n for n in ast.walk(node) if isinstance(n,ast.Call)]
        if any(isinstance(n.func,ast.Name) and n.func.id in {'dump','write_tsv'} for n in calls):
            break
    prefix.append(node)
# No filesystem mutation may occur in a top-level node of this prefix.
for node in prefix:
    if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):continue
    for n in ast.walk(node):
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute):
            assert n.func.attr not in {'write_text','write_bytes','unlink','rename','replace'},ast.unparse(n)
ns={'__file__':str(program.resolve()),'__name__':'integration_readonly_qa'}
exec(compile(ast.Module(body=prefix,type_ignores=[]),str(program), 'exec'),ns)
data=ns['data'];original=ns['original'];aliases=ns['aliases'];plan=ns['PLAN']

explicit_keys='AC_GrothPTT1955 AC_GrothFredholm1956 AC_Dodds1995 AC_Ricard2018 GrothendieckRRR1957 SGA6V Mackall2020 FultonGillet1983 EGAIV1 Stacks00TH Stacks0593 EGAIV4 EGAIII SGA6VII FGA Artin1969 PoonenSlavov2022 Benoist2011 SGA7II Conrad2014 spaces_SGA4I spaces_StacksImmersion spaces_StacksProjective forms_HopkinsSinger forms_Szymik forms_Friedlander bt_GrothCrystals1968 bt_Serre1979 AptSimon2021 Milne2017 Freed2013 ColinMesmay2014 Yagasaki2000 Esquisse1997 RecoltesNote94'.split()
# Derive a second inventory from all known keys actually occurring in the text.
bib={}
for p in (W/'parts').glob('*/references.bib'):
    s=p.read_text()
    chunks=re.split(r'(?m)(?=^@\w+\s*\{)',s)
    for chunk in chunks:
        m=re.match(r'^@\w+\s*\{\s*([^,\s]+)',chunk)
        if not m:continue
        note=re.search(r'\bnote\s*=\s*\{([^}]*)\}',chunk)
        bib.setdefault(m[1],[]).append({'file':str(p.relative_to(W)),'note':note[1] if note else None})
present_known=sorted(k for k in bib if re.search(r'(?<![A-Za-z0-9_])'+re.escape(k)+r'(?![A-Za-z0-9_])',text))
explicit_keys=sorted(set(explicit_keys)|set(present_known))
key_checks=[{'key':k,'exists':k in bib,'records':bib.get(k,[])} for k in explicit_keys]

coverage=json.loads((W/'outputs/source_coverage_summary.json').read_text())
scan_total=sum(coverage['retained_scan_labels_by_cote'].values())
corpus={'transcriptions':coverage['transcriptions'],'inspected_files':coverage['files'],
        'physical_lines':coverage['transcription_lines'],'retained_scan_labels':scan_total,
        'overview_counts_match':coverage['transcriptions']==45 and coverage['files']==91 and coverage['transcription_lines']==38685 and scan_total==905,
        'owned_scope_match':{'1':coverage['retained_scan_labels_by_cote']['1']==105,'21':coverage['retained_scan_labels_by_cote']['21']==27,'22':coverage['retained_scan_labels_by_cote']['22']==29,'23':coverage['retained_scan_labels_by_cote']['23']==91,'26':coverage['retained_scan_labels_by_cote']['26']==10}}

# Verify every merge has retained all witnesses, including repeated target specs.
witness_checks=[];lost=[]
mutated_raw_witnesses=[];conflicting_overrides=[]
for kind in ['items','claims','problems']:
    final={r['id']:r for r in data[kind]}
    original_by={r['id']:r for r in original[kind]}
    grouped=collections.defaultdict(list)
    for spec in plan.get(kind[:-1]+'_merges',[]):grouped[spec['target']].extend(spec['sources'])
    for target,sources in grouped.items():
        canonical=aliases.get(target,[target])
        assert len(canonical)==1,(kind,target,canonical)
        record=final[canonical[0]]
        expected=set([target]+sources)
        observed={r['id'] for r in record.get('source_records',[])}
        missing=sorted(expected-observed)
        row={'kind':kind,'target':target,'canonical':canonical[0],'expected_witnesses':sorted(expected),'retained_witnesses':sorted(observed),'missing':missing}
        witness_checks.append(row)
        if missing:lost.append(row)
        for witness in record.get('source_records',[]):
            if witness != original_by.get(witness['id']):
                mutated_raw_witnesses.append({'kind':kind,'target':target,'witness':witness['id']})
    by_target=collections.defaultdict(list)
    for spec in plan.get(kind[:-1]+'_merges',[]):by_target[spec['target']].append(spec)
    for target,specs in by_target.items():
        values=collections.defaultdict(list)
        for spec in specs:
            for field,value in spec.get('overrides',{}).items():values[field].append(value)
        for field,variants in values.items():
            if len({json.dumps(v,sort_keys=True,ensure_ascii=False) for v in variants})>1:
                conflicting_overrides.append({'kind':kind,'target':target,'field':field,'values':variants})

entries=[x for p in ns['P'] for x in ns['read_tsv'](p/'entries.tsv')]
ambiguous_entries=[{'entry':e['entry_id'],'target':ns['resolve'](e['item_id'])}
                   for e in entries if len(ns['resolve'](e['item_id']))!=1]

# Canonical identifier arrays must not contain comma-joined identifiers.
array_hazards=[];scalar_hazards=[]
frozen={'source_records','source_record_id','original_id','original_ids','aliases','his_words','his_statement','integration_record_before_update'}
def walk(obj,path=()):
    if isinstance(obj,dict):
        for key,value in obj.items():
            if key in frozen:continue
            np=path+(key,)
            if key in {'claim','problem','item','claim_id','problem_id','item_id'} and isinstance(value,str):
                ids=re.findall(r'(?:C-SA23-[a-z_]+-\d+[A-Za-z]?|MP-SA23-\d+|SA23-\d+)',value)
                if len(ids)>1 and ', ' in value:scalar_hazards.append({'path':'.'.join(map(str,np)),'value':value,'ids':ids})
            if key in {'items','claims','problems','claim_ids','problem_ids','item_ids'} and isinstance(value,list):
                for i,v in enumerate(value):
                    if isinstance(v,str) and re.search(r'(?:C-SA23-|MP-SA23-|SA23-)\S+, ',v):array_hazards.append({'path':'.'.join(map(str,np+(i,))),'value':v})
            walk(value,np)
    elif isinstance(obj,list):
        for i,value in enumerate(obj):walk(value,path+(i,))
walk(data)

# Inspect ID-shaped fields even when an owner uses a less common field name.
# Frozen witness/provenance blocks are intentionally allowed to use source IDs.
canonical_ids={r['id'] for rows in data.values() for r in rows}|{r['id'] for r in ns['original_editorial']}
generic_scalar_hazards=[];generic_array_hazards=[]
def walk_exact_ids(obj,path=()):
    if isinstance(obj,dict):
        for key,value in obj.items():
            if key in frozen or key in {'original_claim_id','original_problem_id','original_item_id'}:continue
            np=path+(key,)
            if isinstance(value,str):
                tokens=value.split(', ')
                if len(tokens)>1 and all(t in canonical_ids for t in tokens):
                    generic_scalar_hazards.append({'path':'.'.join(map(str,np)),'value':value})
            walk_exact_ids(value,np)
    elif isinstance(obj,list):
        for i,value in enumerate(obj):
            np=path+(i,)
            if isinstance(value,str):
                tokens=value.split(', ')
                if len(tokens)>1 and all(t in canonical_ids for t in tokens):
                    generic_array_hazards.append({'path':'.'.join(map(str,np)),'value':value})
            walk_exact_ids(value,np)
walk_exact_ids(data)
for owner_path in ns['P']:
    for filename in ['directions.json','editorial_tasks.json','document_records.json']:
        if (owner_path/filename).exists():
            walk_exact_ids(ns['rewrite'](json.loads((owner_path/filename).read_text())),(owner_path.name,filename))

all_item_ids={r['id'] for r in data['items']};all_claim_ids={r['id'] for r in data['claims']};all_problem_ids={r['id'] for r in data['problems']}
unknown=[]
for c in data['claims']:
    for ident in c.get('items',[]):
        if ident not in all_item_ids:unknown.append({'record':c['id'],'field':'items','id':ident})
for p in data['problems']:
    for ident in p.get('claims',[]):
        if ident not in all_claim_ids:unknown.append({'record':p['id'],'field':'claims','id':ident})

def loc(needle):
    pos=text.find(needle)
    return text[:pos].count('\n')+1 if pos>=0 else None

findings=[
 {'id':'OV-01','severity':'minor','file':'integration/overview.md','line':loc('arbitrary-small-p power-monotonicity assertion'),'issue':'C-analysis_curves080 is explicitly a conjectural question on the pages, not an asserted proved theorem. The overview correctly reports its refutation but can make the source status clearer.','suggested_change':'Replace “arbitrary-small-p power-monotonicity assertion” by “unrestricted power-monotonicity conjecture”.','evidence':['parts/analysis_curves/claims.json:C-SA23-analysis_curves-080','parts/analysis_curves/status_categories.json:C-SA23-analysis_curves-080']},
 {'id':'OV-02','severity':'minor','file':'integration/overview.md','line':loc('AC_Ricard2018, Theorem3.2'),'issue':'The constant-one sufficient parameter range comes from Ricard’s introduction; Theorem3.2 gives the all-p estimate with a constant and does not prove monotonicity. The claim register already distinguishes this.','suggested_change':'Use “AC_Ricard2018, Introduction and Theorem3.2”.','evidence':['parts/analysis_curves/claims.json:C-SA23-analysis_curves-080.literature_locator']},
 {'id':'OV-03','severity':'minor','file':'integration/overview.md','line':loc('parts/*/reference_checks.json'),'issue':'Not every owner has reference_checks.json. In particular ega uses bibliography_records.json, external source checks and the search log; analysis_curves uses reference_details.json.','suggested_change':'Replace the named wildcard with “the individual reference annotations, primary-source check records and search_log.jsonl files”.','evidence':['parts/ega/bibliography_records.json','parts/analysis_curves/reference_details.json','parts/spaces/reference_checks.json']},
 {'id':'OV-04','severity':'optional precision','file':'integration/overview.md','line':loc('leads to the express withdrawal'),'issue':'The letter criticism and later withdrawal match exactly. The supplied evidence does not separately document the editorial causal chain.','suggested_change':'“is matched by the express withdrawal” preserves the verified comparison without implying more historical documentation.','evidence':['parts/ega/claims.json:C-SA23-ega-053','parts/ega/problems.json:MP-SA23-ega-26']},
 {'id':'OV-05','severity':'minor','file':'integration/overview.md','line':loc('even for a question now solved, an editorial request'),'issue':'This sentence includes editorial requests in the problem index, whereas the opening convention and the latest provenance audit put editorial requests in SA23_editorial_tasks.json.','suggested_change':'Say “even for a question now solved or a formulation too incomplete to identify; editorial requests have their own separate register”.','evidence':['programs/finalize_dossier.py:original_editorial','integration/overview.md:opening register conventions']},
]
findings=[f for f in findings if f.get('line') is not None]
if scalar_hazards or array_hazards:
    findings.append({'id':'ID-02','severity':'must fix before final serialization','file':'programs/finalize_dossier.py','issue':'One-to-many aliases are expanded correctly in fields named items/claims/problems, but scalar occurrence.claim fields and other ID-array names can become comma-joined strings instead of valid identifiers.','suggested_change':'For occurrence.claim, retain the original source identifier and add a canonical claims array, or duplicate the occurrence once per target. Expand claim_ids/item_ids/problem_ids arrays with resolve as for claims/items/problems. Do not convert prose fields into arrays.','scalar_examples':scalar_hazards[:10],'array_examples':array_hazards[:10]})

review={
 'date':'2026-11-19','reviewer':'GPT-6 Astra Pro, owner ega; bounded final integration QA',
 'overview_sha256':hashlib.sha256(text.encode()).hexdigest(),
 'finalizer_sha256':hashlib.sha256(code.encode()).hexdigest(),
 'plan_sha256':hashlib.sha256((W/'integration/consolidation_plan.json').read_bytes()).hexdigest(),
 'explicit_bibliography_keys_checked':len(key_checks),'missing_explicit_keys':[r['key'] for r in key_checks if not r['exists']],
 'bibliography_key_checks':key_checks,'corpus_coverage':corpus,
 'major_findings_assessment':'The overview’s analysis/curves, EGA correction and detached cocharacter summaries agree with the completed source assessments. Read root/forms/hyperplanes/spaces/bt sections support their corresponding major findings; misc subject comparisons were checked against its completed section and earlier direct review. The groupes section was not yet present at the initial review; its detached-leaf claims016–017 were independently read and checked. No major mathematical misstatement was identified in the overview.',
 'findings':findings,
 'merge_qa':{'groups_checked':len(witness_checks),'lost_witnesses':lost,'checks':witness_checks,'mutated_raw_witnesses':mutated_raw_witnesses,'conflicting_repeated_target_overrides':conflicting_overrides,'indexed_entries_checked':len(entries),'ambiguous_entry_targets':ambiguous_entries,'array_id_hazards':array_hazards,'scalar_id_hazards':scalar_hazards,'generic_scalar_id_hazards':generic_scalar_hazards,'generic_array_id_hazards':generic_array_hazards,'unknown_main_array_ids':unknown,'finalizer_output_files_written':False},
 'helper':'integration/id_rewrite_helper.py','helper_tests':'integration/id_rewrite_helper_tests.json',
 'files_modified':'Only integration/id_rewrite_helper.py and this review program/reports. No owner register, overview or finalizer was edited.'
}
(W/'integration/overview_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'bibliography_keys':len(key_checks),'missing_keys':review['missing_explicit_keys'],'coverage_ok':corpus['overview_counts_match'],'merge_groups_checked':len(witness_checks),'lost_witness_groups':len(lost),'scalar_id_hazards':len(scalar_hazards),'array_id_hazards':len(array_hazards),'unknown_main_array_ids':unknown,'findings':[{'id':f['id'],'severity':f['severity']} for f in findings]},ensure_ascii=False))
