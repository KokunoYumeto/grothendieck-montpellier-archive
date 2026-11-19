"""Structural validation of manually authored evidence, not mathematical grading.
Run: python validate.py > validation_output.json
"""
import csv,json,re,hashlib
from pathlib import Path
from collections import Counter
HERE=Path(__file__).parent
ROOT=Path('/workspace/scratch/4017236f14bf')
def js(n):return json.loads((HERE/n).read_text())
def tab(n):
    with (HERE/n).open() as f:return list(csv.DictReader(f,delimiter='\t'))
C=js('claims.json');P=js('problems.json');R=js('refinements.json')
claims={x['id']:x for x in C}
assert len(claims)==len(C)==48
assert set(claims)=={f'C-SA21-9-{n:03d}' for n in range(81,129)}
assert len(P)==13 and {x['id'] for x in P}=={f'MP-SA21-9-{n:02d}' for n in range(20,33)}
assert len(R)==12 and {x['id'] for x in R}=={f'R-SA21-9E-{n:03d}' for n in range(1,13)}
required={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','status_category','computation','class','fate','fate_date','present_status','refs','confidence'}
categories={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','definition/construction','current-run refinement'}
bib=(HERE/'references.bib').read_text()
keys=re.findall(r'@\w+\{([^,]+),',bib)
assert len(keys)==len(set(keys))==26
notes=re.findall(r'(?<![A-Za-z])note\s*=\s*\{([^}]*)\}',bib)
assert len(notes)==26 and set(notes)<={'verified','unverified'},notes
for c in C:
    assert set(c)==required,(c['id'],set(c)^required)
    assert c['cote']=='156-9' and c['scans'] and c['lines']
    assert c['status_category'] in categories and c['class'] in 'ABCDEF'
    assert c['confidence'] in {'high','medium','low'}
    assert set(c['refs'])<=set(keys),(c['id'],c['refs'])
    assert c['fate_date']['searched_as_of']=='2026-11-19'
    for loc in c['lines']:
        m=re.fullmatch(r'(J156-9-\d+_transcription\.tex): scan (\d+), lines (\d+)–(\d+)',loc)
        assert m,loc
        lines=(ROOT/'sources/texts/codex'/m[1]).read_text().splitlines()
        assert 1<=int(m[3])<=int(m[4])<=len(lines),loc
        assert f'\\scanpage{{{m[2]}}}' in lines[int(m[3])-1],loc
for p in P:
    assert set(p)=={'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
    assert p['occurrences'] and set(p['refs'])<=set(keys)
for r in R:
    assert set(r['source_claim_ids'])<=set(claims)
    assert r['status_category']=='current-run refinement'
    assert r['statement'] and r['scope'] and r['certificate'] and r['verification']
coverage=tab('coverage.tsv')
assert len(coverage)==5
scans=[]
for row in coverage:
    stem=row['folder']
    for base,suffix,hashkey in [('texts','transcription.tex','transcription_sha256'),('notes','notes.md','notes_sha256')]:
        q=ROOT/'sources'/base/'codex'/f'{stem}_{suffix}'
        assert hashlib.sha256(q.read_bytes()).hexdigest()==row[hashkey]
    assert (HERE/'read_outputs'/f'{stem}.txt').exists()
    scans.extend(map(int,row['scans'].split(',')))
assert len(scans)==35 and set(scans)==set(range(105,141))-{129}
search=tab('search_log.tsv')
for c in C:assert any(c['id'] in row['claims'].split(';') for row in search),c['id']
assert sum(x['engine']!='shared documented search' for x in search)==27
events=tab('check_events.tsv')
assert len(events)==107
for item in C+P+R:assert any(e['statement_id']==item['id'] for e in events),item['id']
for e in events:
    if e['type'].startswith('refuted'):
        assert re.search(r'(?:R-SA21-|C-SA21-|MP-SA21-)',e['outcome']),e
readings=tab('readings.tsv');links=tab('links.tsv')
assert len(readings)==29 and len(links)==35
assert {x['kind'] for x in links}<={'folder','published work','our projects'}
assert all('No scan image was available or inspected' in x['evidence'] for x in readings)
O=js('finite_checks_output.json')
assert O['set_relation_classification']['relations_checked']==689
assert O['set_relation_classification']['failed_instances']==[]
for section,key in [
 ('general_spatios_corollary_failure','hypotheses'),
 ('commensurable_refinement_not_transitive','all_required_hypotheses_and_failure'),
 ('bare_morphism_kernel_not_closed','all_named_hypotheses'),
 ('faithful_external_does_not_imply_commensurability','all_external_support_hypotheses_and_failure'),
 ('commensurability_alone_not_local_subdivision_detection','all_named_hypotheses')]:
    assert all(O[section][key].values()),section
assert O['commensurable_refinement_not_transitive']['generated_cardinalities']==[8,8,18]
assert O['scan113_reconstruction']['literal_family_complement_closed'] is False
assert O['elementary_figure_pullback_not_elementary']['pullback_has_greatest_stratum'] is False
assert O['deleted_quotient_topology_equivalence']['all_eight_target_subsets_tested_for_final_Alexandrov_topology'] is True
assert O['deleted_quotient_topology_equivalence']['single_comparable_pair_lifting_for_0_le_2'] is False
assert (HERE/'finite_checks_stderr.txt').read_text()==''
for name in ['formalism_and_checks.md','narrative.md','directions.md']:
    s=(HERE/name).read_text()
    assert len(s)>1000
    assert not any(ord(c)<32 and c not in '\t\r\n' for c in s),name
counts=js('counts.json')
assert counts['claims_by_class']==dict(Counter(c['class'] for c in C))
print(json.dumps({'result':'PASS','scope':'Structural consistency and saved-certificate assertions; no automated mathematical verdicts.',
 'claims':len(C),'classes':counts['claims_by_class'],'status_categories':counts['status_category_counts'],
 'problems':len(P),'folders':len(coverage),'supplied_scans':len(scans),'missing_scan':129,
 'readings':len(readings),'links':len(links),'refinements':len(R),'check_events':len(events),
 'references':len(keys),'finite_certificate_groups':len(O)-2,'relation_instances':689,
 'new_search_queries':27,'shared_search_mappings':20},ensure_ascii=False,indent=2))
