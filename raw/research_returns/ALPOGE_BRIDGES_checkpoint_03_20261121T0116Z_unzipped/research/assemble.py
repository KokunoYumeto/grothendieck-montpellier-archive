"""Assemble a self-contained checkpoint manuscript and normalized registers.
This script never makes or saves a checkpoint ZIP; that operation is timed separately.
"""
from pathlib import Path
import csv, datetime, re, subprocess

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research'; D=ROOT/'deliverables'; D.mkdir(exist_ok=True)
modules=['archive_questions.tex','consequences_criteria_Tate2026.tex',
         'consequences_criteria_abelian_group.tex','consequences_criteria_cross_cycles.tex',
         'root_springer_archive.tex','source_cote123_rational.tex','consequences_criteria_apposition.tex',
         'root_effectivity.tex','root_group_rank.tex','consequences_criteria_adjoint_rank.tex','root_henselian.tex',
         'root_deligne.tex','root_core.tex','root_weight_criterion.tex',
         'consequences_criteria_WM_formality.tex',
         'consequences_criteria_stable_curve.tex','consequences_criteria_RESIDUE.tex',
         'root_linear_archive.tex','source_cote1348_counit.tex','source_cote1348_purity.tex','source_cote1348_fp.tex','source_cote1348_compact_unit.tex',
         'root_methods.tex','consequences_criteria.tex',
         'consequences_criteria_GT_addendum.tex','source_and_masullo.tex',
         'source_masullo_numeric.tex','source_masullo_kernel.tex','source_K_bridge.tex']
body=(R/'frontmatter.tex').read_text()
for name in modules:
    if (R/name).exists(): body+='\n% BEGIN '+name+'\n'+(R/name).read_text()+'\n% END '+name+'\n'
body+=(R/'unresolved.tex').read_text()
body+=(R/'root_references.tex').read_text()
for name in ['archive_bibliography.md']:
    if (R/name).exists():
        text=subprocess.run(['pandoc','-f','gfm','-t','latex',str(R/name)],capture_output=True,text=True,check=True).stdout
        body+='\n'+text
if (R/'source_and_masullo.md').exists():
    note=(R/'source_and_masullo.md').read_text().split('## 5. Exact bibliographic inputs')[-1]
    text=subprocess.run(['pandoc','-f','gfm','-t','latex'],input='## Source-route references\n'+note,capture_output=True,text=True,check=True).stdout
    body+='\n'+text
body+='\n\\end{document}\n'
# Put bare URLs in breakable URL commands; existing href/url arguments remain intact.
body=re.sub(r'(?<!\{)(https?://[^\s{}]+)',lambda m:'\\url{'+m.group(1).rstrip('.')+'}'+('.' if m.group(1).endswith('.') else ''),body)
# Module-local bibliography headings are not cross-reference targets.
body=body.replace('\\label{references}','')
body=body.replace(r'\mathrm{\acute et}',r'\text{ét}')
body=body.replace(r'\mathrm{\acute{e}t}',r'\text{ét}')
body=re.sub(r'\\texttt\{([A-Za-z0-9_\\.\-]+)\}',lambda m:r'\nolinkurl{'+m.group(1).replace(r'\_','_')+'}',body)
body=body.replace('[leftmargin=*,label={}]','[leftmargin=0pt,labelsep=0pt,label={}]')
body=body.replace('[style=nextline,leftmargin=0pt]','[style=nextline,leftmargin=0pt,labelwidth=0pt,labelsep=0pt]')
# Retrieval identifiers belong in the audit notes, not in the paper's bibliography.
body=re.sub(r'(?<![A-Za-z])turn\d+(?:search|view|fetch)\d+', '', body)
(D/'ALPOGE_BRIDGES.tex').write_text(body)

header=['statement_id','date_utc','who','model','effort','run','type','outcome','method','source_locator']
paths=[R/'initial_input_checks.tsv']+sorted(R.glob('*[Cc][Hh][Ee][Cc][Kk]*.tsv'))
rows=[];seen=set()
for p in paths:
    if not p.exists():continue
    for v in csv.DictReader(p.open(),delimiter='\t'):
        stamp=v.get('date_utc',v.get('date',''))
        if stamp:
            try:stamp=datetime.datetime.fromisoformat(stamp.replace('Z','+00:00')).astimezone(datetime.timezone.utc).isoformat()
            except ValueError:pass
        who=v.get('who','');run=v.get('run','')
        if not run:
            match=re.search(r'run=([^;]+)',who)
            run=match.group(1) if match else p.stem
        out={k:v.get(k,'') for k in header}
        out.update(date_utc=stamp,who=who,model=v.get('model','GPT-6 Astra Pro'),effort=v.get('effort','not exposed'),run=run)
        key=tuple(out[k] for k in header)
        if key not in seen:rows.append(out);seen.add(key)
with (D/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=header,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

qh=['id','who_asked','source_locator','question_as_stated','state','finding_ids_or_gate','bridges_used','source_kind']
qr=[]
for p in [R/'root_questions.tsv',R/'archive_questions.tsv']:
    if not p.exists():continue
    for v in csv.DictReader(p.open(),delimiter='\t'):
        # Agent register uses its own explicit headings; preserve extra fields in source file.
        aliases={'id':['id','question_id'],'who_asked':['who_asked','who','author'],
                 'source_locator':['source_locator','source_and_locator','source'],
                 'question_as_stated':['question_as_stated','original_question','question','statement'],
                 'state':['state','status'],'finding_ids_or_gate':['finding_ids_or_gate','finding_ids','gate'],
                 'bridges_used':['bridges_used','bridge','bridges'],'source_kind':['source_kind']}
        out={k:next((v[a] for a in aa if a in v),'') for k,aa in aliases.items()}
        
        if not out['who_asked']: out['who_asked']='Grothendieck / intake author (see source)'
        if v.get('remaining_gate'): out['finding_ids_or_gate']+='; remaining gate: '+v['remaining_gate']
        qr.append(out)
with (D/'QUESTIONS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=qh,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(qr)
print({'tex_words':len(body.split()),'check_events':len(rows),'questions':len(qr)})
