#!/usr/bin/env python3
"""Apply the manually reviewed final English word-space repairs, with proofs."""
from pathlib import Path
from datetime import datetime, timezone
import difflib, json, re, shutil, subprocess

from build_readers import EDITION, validate_translation
from edition_core import arguments_at, extract_variants, math_fragments, read_tsv, resolve_variants, sha256, write_tsv


def branch_space(text, source_id, leading=False):
    found=[]
    for match in re.finditer(r'\\var\{', text):
        args,_,end,offsets=arguments_at(text,match.start(),'var')
        if args[3]==source_id:found.append((args,offsets))
    assert len(found)==1,(source_id,len(found))
    args,offsets=found[0]
    old=args[1];new=(' '+old) if leading else (old+' ')
    start=offsets[1]
    return text[:start]+new+text[start+len(old):],old,new,text.count('\n',0,start)+1


def main():
    target=EDITION/'records/en_final_word_boundaries'
    target.mkdir(exist_ok=True)
    marker=target/'COMPLETED.json'
    if marker.is_file():
        print('The recorded final English boundary repairs have already run.');return
    for src,name in [('en_boundary_candidates.json','CANDIDATES.json'),('en_boundary_middle_review.json','MIDDLE_REVIEW.json'),('en_punctuation_candidates.json','PUNCTUATION_CANDIDATES.json')]:
        shutil.copyfile(EDITION/'review_work'/src,target/name)
    review=json.loads((target/'MIDDLE_REVIEW.json').read_text())
    actions=list(review['definite_findings'])
    punctuation=[
        (36,'(S$_k$):on F)','(S$_k$): on F)'),
        (71,'S,with components','S, with components'),
        (77,'$P^r_k$,of dimensions','$P^r_k$, of dimensions'),
        (77,'nonempty,not containing','nonempty, not containing'),
        (79,'P(k),such that','P(k), such that'),
        (108,',which characterizes',', which characterizes'),
        (113,'not);now since','not); now since'),
        (115,'bundle,namely','bundle, namely'),
        (121,'unique,and equal','unique, and equal'),
        (180,' ,by $u',' , by $u'),
    ]
    punct_variants={
        (71,'S,with components'):'ega25_25_071-v0006',
        (77,'$P^r_k$,of dimensions'):'ega25_25_077-v0002',
        (77,'nonempty,not containing'):'ega25_25_077-v0016',
        (79,'P(k),such that'):'ega25_25_079-v0007',
        (115,'bundle,namely'):'ega25_25_115-v0014',
        (121,'unique,and equal'):'ega25_25_121-v0022',
    }
    for site,before,after in punctuation:
        actions.append(dict(site=site,before=before,after=after,variant_id=punct_variants.get((site,before)),candidate='punctuation',reason='Insert the ordinary English prose space after the retained punctuation, within the existing corrected branch when the following clause is an insertion; preserve all letters, punctuation and mathematical fragments.'))
    originals={};changed={};rows=[];stamp=datetime.now(timezone.utc).isoformat()
    for action in actions:
        key=f"ega25_25_{action['site']:03d}"
        if key not in originals:
            originals[key]=(EDITION/'master_pages/en'/(key+'.tex')).read_text()
            changed[key]=originals[key]
        before_text=changed[key]
        if action.get('variant_id'):
            after_text,before,after,line=branch_space(before_text,action['variant_id'],leading=action['variant_id']!='ega25_25_012-v0006')
        else:
            before,after=action['before'],action['after']
            assert before_text.count(before)==1,(key,before,before_text.count(before))
            line=before_text.count('\n',0,before_text.index(before))+1
            after_text=before_text.replace(before,after)
        assert re.sub(r'\s+','',before)==re.sub(r'\s+','',after),(key,'non-space edit')
        changed[key]=after_text
        rows.append(dict(key=key,line=line,variant_id=action.get('variant_id') or '',before=before,after=after,reason=action['reason'],reviewer='GPT-6 Astra / middle and edition_pipeline' if action.get('candidate')!='punctuation' else 'GPT-6 Astra / edition_pipeline',reviewed_utc=stamp))
    for key,after in changed.items():
        before=originals[key]
        assert math_fragments(before)==math_fragments(after),(key,'raw mathematical fragments changed')
        assert list(extract_variants(before))==list(extract_variants(after)),(key,'variant IDs changed')
        for side in (0,1):
            assert math_fragments(resolve_variants(before,side))==math_fragments(resolve_variants(after,side)),(key,side)
        validate_translation(key,(EDITION/'master_pages/fr'/(key+'.tex')).read_text(),after)
    proof=[]
    for key,after in changed.items():
        before=originals[key]
        (target/('before_'+key+'.tex')).write_text(before)
        (target/('after_'+key+'.tex')).write_text(after)
        (target/(key+'.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='master_pages/en/'+key+'.tex (before)',tofile='master_pages/en/'+key+'.tex (after)')))
        (EDITION/'master_pages/en'/(key+'.tex')).write_text(after)
        proof.append(dict(key=key,before_sha256=sha256(before),after_sha256=sha256(after),only_whitespace_changed=True,math_both_branches_identical=True,variant_ids_identical=True,exact_diff='records/en_final_word_boundaries/'+key+'.diff'))
    for row in rows:
        row.update(before_master_sha256=sha256(originals[row['key']]),after_master_sha256=sha256(changed[row['key']]))
    write_tsv(EDITION/'records/EN_FINAL_WORD_BOUNDARIES.tsv',rows)
    subprocess.run(['python',str(EDITION/'scripts/check_translation.py'),*sorted(changed),'--record','--note','Final independently reviewed English-only word-space repairs; exact mathematical fragments, both variant branches, all IDs and source marks preserved. See EN_FINAL_WORD_BOUNDARIES.tsv and records/en_final_word_boundaries/ exact diffs.'],check=True,stdout=subprocess.DEVNULL)
    marker.write_text(json.dumps(dict(utc=stamp,actions=len(rows),pages=len(changed),proof=proof,retained_physical_mark_cases=review['uncertain_spacing_dispositions'],note='Only the recorded definite English boundaries were changed. Source checked pages, French masters, formulas, layer marks and IDs remain unchanged.'),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(actions=len(rows),pages=len(changed),keys=sorted(changed))))


if __name__=='__main__':main()
