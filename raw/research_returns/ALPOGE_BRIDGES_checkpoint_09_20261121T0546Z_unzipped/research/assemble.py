"""Assemble a self-contained checkpoint manuscript and normalized registers.
This script never makes or saves a checkpoint ZIP; that operation is timed separately.
"""
from pathlib import Path
import csv, datetime, re, subprocess

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'research'; D=ROOT/'deliverables'; D.mkdir(exist_ok=True)
modules=['archive_questions.tex','consequences_criteria_integral_albanese.tex','root_separated_parameters.tex','consequences_criteria_albanese_literature.tex','consequences_criteria_Tate2026.tex',
         'consequences_criteria_abelian_group.tex','consequences_criteria_abelian_germs.tex','consequences_criteria_rational_descent.tex','consequences_criteria_rational_basechange.tex','consequences_criteria_integral_slope_descent.tex','consequences_criteria_finite_descent.tex','consequences_criteria_prime_field_descent.tex','consequences_criteria_noncyclic_descent.tex','consequences_criteria_local_descent_obstruction.tex','root_descent_prime_support.tex','consequences_criteria_uniform_descent.tex','consequences_criteria_descent_profile.tex','root_class_number_descent.tex','consequences_criteria_cross_cycles.tex','consequences_criteria_cycle_certificates.tex','consequences_criteria_fermat_certificates.tex','consequences_criteria_separated_hypersurfaces.tex',
         'consequences_criteria_rational_spectral_target.tex','consequences_criteria_proper_parity.tex','consequences_criteria_effective_target.tex','consequences_criteria_one_way_certificate.tex','consequences_criteria_chow_generation.tex','consequences_criteria_quadric_fibrations.tex','consequences_criteria_quadric_equivalence.tex','consequences_criteria_supersingular_cycles.tex','consequences_criteria_supersingular_liftings.tex','root_quadric_discriminant.tex',
         'root_springer_archive.tex','source_cote123_rational.tex','consequences_criteria_apposition.tex','consequences_criteria_apposition_general.tex','root_exceptional_opposition.tex','root_g2_opposition.tex','consequences_criteria_exceptional_minuscule.tex',
         'root_effectivity.tex','root_group_rank.tex','consequences_criteria_adjoint_rank.tex','root_henselian.tex',
         'root_comparison.tex','root_adelic_genericity.tex','root_deligne.tex','root_core.tex','root_weight_criterion.tex',
         'consequences_criteria_WM_formality.tex',
         'consequences_criteria_stable_curve.tex','consequences_criteria_RESIDUE.tex',
         'root_linear_archive.tex','source_cote1348_counit.tex','source_cote1348_purity.tex','source_cote1348_fp.tex','source_cote1348_compact_unit.tex','source_cote1348_realization.tex','source_cote1348_grothendieck.tex','source_cote1348_no_ab5.tex','source_cote1348_no_ab4.tex','source_cote1348_low_degree.tex','source_cote1348_ab4.tex','source_cote1348_countable.tex','source_cote1348_additive_counterexample.tex','source_cote1348_tensor_obstructions.tex','source_cote1348_ext_tensor.tex','source_cote1348_chain_counit.tex','source_cote1348_product_interval.tex','source_cote1348_split_interval.tex','source_cote1348_projective_tensor_failure.tex',
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
# Repair Pandoc's text-mode tilde inside a bare URL before wrapping it.
# A tilde in a URL is literal, not a text accent command followed by a space.
body=re.sub(r'(https?://[^\s{}]*?)\\textasciitilde\s+',r'\1~',body)
# Put bare URLs in breakable URL commands; existing href/url arguments remain intact.
def wrap_bare_url(match):
    value=match.group(1)
    trailing='.' if value.endswith('.') else ''
    value=value.rstrip('.').replace(r'\%', '%').replace(r'\_', '_').replace(r'\#', '#')
    return r'\url{'+value+'}'+trailing
body=re.sub(r'(?<!\{)(https?://[^\s{}]+)',wrap_bare_url,body)
# Module-local bibliography headings are not cross-reference targets.
body=body.replace('\\label{references}','')
# Repeated generated heading labels carry no mathematical reference. Remove
# them only when unreferenced; retain any genuine cross-reference for review.
from collections import Counter
for label,count in Counter(re.findall(r'\\label\{([^{}]+)\}',body)).items():
    if count<=1: continue
    referenced=re.search(r'\\(?:ref|eqref|autoref|pageref|nameref|cref|Cref)\{'+re.escape(label)+r'\}',body)
    referenced=referenced or (r'\hyperref['+label+']' in body)
    if not referenced: body=body.replace(r'\label{'+label+'}','')
body=body.replace(r'\mathrm{\acute et}',r'\text{ét}')
body=body.replace(r'\mathrm{\acute{e}t}',r'\text{ét}')
body=re.sub(r'\\texttt\{([A-Za-z0-9_\\./\-]+)\}',lambda m:r'\nolinkurl{'+m.group(1).replace(r'\_','_')+'}',body)
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
        # One source event may explicitly name several statements. Expand its
        # semicolon list for lookup, retaining the same date/type/method; this
        # is normalization of that event, not an invented additional check.
        for statement in out['statement_id'].split(';'):
            normalized=out.copy();normalized['statement_id']=statement.strip()
            key=tuple(normalized[k] for k in header)
            if key not in seen:rows.append(normalized);seen.add(key)
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
