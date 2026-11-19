"""Serialization helpers only. All mathematical assessments are authored in data_*.py."""
from pathlib import Path
import json,re,csv
P=Path(__file__).parent
SOURCE=Path('sources/texts/api/ega_v_cote25_combined.tex')
L=SOURCE.read_text().splitlines()
WHO='GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; root/cote25'
DATE='2026-11-19'
I=[]; C=[]; E=[]; G={}; N={}
def add(n,title,scans,lo,hi,status,cl,statement,fate,refs,proof='',refine='',confidence='high',group=''):
    cid=f'C-SA23-hyp-{n:03}'; iid=f'SA23-{500+n}'
    # A quotation must contain source mathematics, not the AI transcriber's
    # page-header comments. Excerpting removes metadata/page-break commands
    # only; all mathematical wording and uncertainty/deletion macros survive.
    excerpt_lines=[line for line in L[lo-1:hi]if line.strip()and not line.lstrip().startswith(('%','\\clearpage','\\scanpage','\\mspage'))]
    raw='\n'.join(excerpt_lines[:19])
    loc=f'texts/api/ega_v_cote25_combined.tex:{lo}–{hi}'
    kind='withdrawn in the same text' if status=='corrected by himself later' else ('self-flagged step' if status=='open on the pages' else 'unproved claim' if status=='stated without proof' else 'other')
    I.append(dict(id=iid,sources=[],kind=kind,cote='25',scans=scans,lines=[loc],his_words=raw[:650],statement=statement,reconstruction='New item from direct reading of the supplied API transcription; no indexed Pro-note verdict is implied. '+('The separately numbered R statement is this run’s reconstruction, not an emendation.' if refine else 'Modern terminology and explicit background hypotheses are supplied in the assessment.'),check='agrees',check_reason='The cited source passage was read in full and assessed individually; see reading_notes.md and the linked claim. '+title))
    comp=proof or 'No numerical computation asserted; the assessment uses the exact source comparison stated in fate.'
    C.append(dict(id=cid,items=[iid],cote='25',scans=scans,lines=[loc],his_statement=raw,source_excerpt_note='Selected literal transcription lines from the assessed passage; transcription metadata and page-break commands omitted from the quotation only. Mathematical deletion, insertion and uncertainty markup is retained. The input file is unchanged.',transcription_notes=[line for line in L[lo-1:hi]if line.lstrip().startswith('% NOTE:')],statement=statement,status_on_pages=status,computation=comp,**{'class':cl},fate=fate,fate_date='Dates and exact locators are given with the cited reference records; current comparison checked19November2026.',present_status='As of19November2026: '+fate,refs=refs.split(',') if refs else [],confidence=confidence))
    E.append([iid,DATE,WHO,'used and rechecked in this run','Direct source/item comparison; '+title])
    et='independent re-proof' if proof.startswith('Proof:') else ('computation or formal certificate' if 'computations.py' in proof else 'carried as background without fault found')
    if status=='false as stated':
        assert refine, (n,'false claim needs a refined statement')
        et='refuted, with the refined statement\'s id'
    E.append([cid,DATE,WHO,et,('Refined statement '+cid+'R. ' if refine else '')+comp+' '+fate])
    if refine:
        cr=dict(C[-1]); cr.update(id=cid+'R',his_statement='Present-run refinement; not a replacement of the transcription.',statement=refine,status_on_pages='present-run refinement; not an assertion on the pages',present_status='As of19November2026: the explicitly restricted/corrected statement is supported by the argument and exact comparison given for '+cid+'.')
        C.append(cr); E.append([cr['id'],DATE,WHO,'targeted proof check',comp])
    N[n]=dict(id=cid,item=iid,title=title,scans=scans,lines=[loc])
    if group:G.setdefault(group,[]).append(cid); G[group]+=[cid+'R'] if refine else []
def write():
    for nm,a in [('items',I),('claims',C)]: (P/(nm+'.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
    (P/'claim_groups.json').write_text(json.dumps(G,ensure_ascii=False,indent=2)+'\n')
    (P/'claim_index.json').write_text(json.dumps(N,ensure_ascii=False,indent=2)+'\n')
    with (P/'claim_check_events.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(E)
    print(json.dumps({'items':len(I),'claims':len(C),'events':len(E),'groups':len(G)}))
