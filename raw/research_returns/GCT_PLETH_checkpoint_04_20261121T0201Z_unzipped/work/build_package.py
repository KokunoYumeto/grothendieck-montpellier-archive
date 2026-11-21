from pathlib import Path
import csv, json, re, subprocess, hashlib, zipfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'deliverables'
OUT.mkdir(exist_ok=True)
RUN=json.loads((ROOT/'work/run_start.json').read_text())

REPORTS=[
 ('Checked theta and positive formulas',[
 'work/theta/theta_report.md','work/root/root_report.md',
 'work/root/degree_three_report.md','work/root/invariant_polytope_report.md',
 'work/root/general_polytope_extensions.md','work/root/rank_three_presentation.md',
 'work/theta/few_columns_report.md','work/theta/width7/width7_report.md','work/theta/outer4/outer4_report.md','work/theta/end_node/end_node_report.md','work/theta/end_node/end_node_schur_report.md','work/theta/end_node/normalization_obstruction.md','work/theta/outer4/paired_rows_report.md','work/theta/outer4/proper_faces_report.md','work/theta/general_chart_report.md','work/theta/outer4/chamber_report.md','work/theta/outer4/four_fibers_report.md','work/theta/outer4/full_outer4_report.md','work/root/general_fiber_model.md',
 'work/theta/outer5/five_point_resolution_report.md','work/theta/outer5/five_point_family_report.md',
 'work/root/five_point_q_module_report.md','work/root/five_point_wedge2_report.md','work/root/five_point_symmetric_quotient_report.md',
 'work/theta/outer5/q_plus_report.md','work/theta/outer5/five_point_hook_report.md',
 'work/theta/outer5/q_plus_symmetric_report.md','work/theta/outer5/hook_all_powers_report.md',
 'work/root/five_point_three_parameter_report.md','work/root/five_point_two_row_report.md',
 'work/root/staircase_uniform_report.md','work/root/staircase_five_report.md']),
 ('Checked canonical-map and rectangular results',[
 'work/rectangular/rectangular_report.md','work/rectangular/boundary_and_prime_blocks.md','work/rectangular/polarization_boundary_report.md','work/rectangular/polarization_r4_boundary_and_geometry.md','work/theta/endpoint_check.md',
 'work/root/prime_semigroup_report.md','work/root/chow_first_row_report.md','work/rectangular/rectangular_end_lower_bound.md','work/rectangular/polarization_r6_boundary_report.md','work/rectangular/three_boundary_kernels.md','work/rectangular/boundary_truncation_model.md','work/rectangular/polarization_second_row_range.md','work/rectangular/polarization_first_row_band.md','work/rectangular/canonical_boundary_ranges.md','work/rectangular/recursive_canonical_range.md','work/rectangular/polarization_next_row_families.md','work/rectangular/canonical_below_square_families.md','work/root/current_ranges.md']),
 ('Checked archive findings and integral identities',[
 'work/archive/archive_report.md','work/archive/TENSOR_POWER_INTEGRAL.md','work/archive/STUDY_ADDITIONS.md','work/archive/PRIMARY_SCAN_FOLLOWUP.md','work/archive/ITERATE_COUNTEREXAMPLE.md','work/archive/LEFSCHETZ_FRAGMENT.md','work/archive/SCALAR_TRIANGULATIONS.md','work/archive/WITT_UNIQUENESS.md','work/archive/FIELD_CANCELLATION.md','work/archive/MIXED_CHAR_LATTICES.md','work/archive/HYPERBOLIC_CLASSES.md','work/archive/LOCAL_RING_COUNTEREXAMPLE.md','work/archive/FIVE_POINT_COX_MAP.md','work/archive/FIVE_POINT_POWERS.md']),
 ('Algebraic-geometric restatements and proof dictionaries',['work/root/geometric_dictionary.md']),
 ('Source register and verification',['work/archive/SOURCE_NOTES.md','work/root/background_register.md','work/archive/OUTER4_FREE_MODULE_REVIEW.md','work/archive/GENERAL_FIBER_REVIEW.md','work/archive/OUTER5_PROOF_REVIEW.md','work/archive/FIVE_POINT_JET_REVIEW.md','work/archive/HOOK_BUNDLE_REVIEW.md','work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md']),
 ('Unresolved questions and exact remaining gates',['work/root/remaining_gates.md']),
]

def merge_events():
    fields=['statement_id','date','who_model_effort_run','type','detail_type','outcome','how','source']
    rows=[]
    for p in [ROOT/'work/root/CHECK_EVENTS.tsv',ROOT/'work/theta/CHECK_EVENTS.tsv',ROOT/'work/rectangular/CHECK_EVENTS.tsv',ROOT/'work/archive/CHECK_EVENTS.tsv']:
        if not p.exists(): continue
        for r in csv.DictReader(p.open(newline=''),delimiter='\t'):
            rr={k:r.get(k,'') for k in fields}
            rr['who_model_effort_run']=r.get('who_model_effort_run',r.get('who',''))
            rr['source']=r.get('source','') or str(p.relative_to(ROOT))
            rows.append(rr)
    with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    return rows

def questions():
    fields=['id','source_and_locator','question','state','finding_ids_or_current_gate']
    rows=[]
    for part,files in REPORTS[:3]:
        for name in files:
            p=ROOT/name
            if not p.exists(): continue
            for line in p.read_text().splitlines():
                m=re.match(r'#+\s+([AGRTM]-\d{3})[.:]\s*(.*)',line)
                if m:
                    sid,title=m.groups()
                    state='proved in stated scope'
                    if sid in ['A-001','A-002','A-003','A-005','G-001','T-009','R-003','R-010','A-015','A-016','A-023']:
                        state='specified assertion refuted; exact replacement proved'
                    if sid.startswith('M-'): state='source audit and exact morphisms checked; open ranges retained'
                    rows.append(dict(zip(fields,[sid,name+'; '+sid,title,state,sid])))
    # Some finite-certificate reports declare their ID in a statement paragraph.
    known={r['id'] for r in rows}
    for _,files in REPORTS[:3]:
        for name in files:
            p=ROOT/name
            if not p.exists(): continue
            for sid in re.findall(r'Statement \*\*([AGRTM]-\d{3})\*\*',p.read_text()):
                if sid not in known:
                    title=next((x.lstrip('# ').strip() for x in p.read_text().splitlines() if x.startswith('# ')),sid)
                    rows.append(dict(zip(fields,[sid,name+'; '+sid,title,'proved in stated scope',sid])))
                    known.add(sid)
    aq=ROOT/'work/archive/ARCHIVE_QUESTIONS.tsv'
    if aq.exists():
        for r in csv.DictReader(aq.open(newline=''),delimiter='\t'):
            if 'question_id' in r:
                rows.append(dict(zip(fields,[r['question_id'],r.get('source_file','')+'; cote '+r.get('cote','')+'/scan '+r.get('scan',''),r.get('assertion',''),r.get('status',''),r.get('proof_id','')+'; '+r.get('result_or_exact_gate','')+'; '+r.get('scan_verification','')])))
            else:
                rows.append({k:r.get(k,'') for k in fields})
    openq=[
      ('Q-ARCH-CONTEXT','Archive 4/007; 12/041; 16/038; 79/051; 119/217','Complete the unidentified or context-dependent assertions','precise mathematical and target-definition gates','Original contexts are recovered. Remaining inputs include crystalline Lefschetz/freeness, the stated motivic self-duality map, and reconstruction from one unlabeled triangulation; see assertion-level archive rows.'),
      ('Q-EFFICIENT','Mulmuley GCT VII Problem 1.1','Uniform positive #P formula of polynomial description size','open','G-009--G-011 give terminating positive formulas; no polynomial input-size bound for Hilbert bases, Reynolds lists, or elimination.'),
      ('Q-OUTER4','G-015 flag model at m4; T-037','Evaluate every outer-degree-four Schur coefficient by a fixed small positive formula','proved','T-037 gives at most108 fixed polytopes, at most5 variables, a fixed arithmetic evaluator and exact support for every output shape.'),
      ('Q-OUTER5','G-015 flag model at m5; G-020--G-021','Evaluate the full outer-degree-five flag ideal without general elimination','open with strictly smaller central gate','G-021 proves all two-row quotient functors for c≥2k, with122 active positive terms and155 exact support exceptions. Its exact multiplication and complement pairings cover λ2+λ3≤2n or λ3+λ4≥2n. Remaining direct region: λ2+λ3>2n>λ3+λ4; evaluate its actual H1 correction and finite-group covariants.'),
      ('Q-MAP','Sra III Theorem 1.3; boundary b=(a-1)^2-1','Full canonical-map rank in remaining parameter families','open with reduced component and finite boundary gates','G-011 counts ranks effectively; G-013 gives prime-adjacent semigroup preimages; G-014 lifts every tail of size at most the coordinate degree; R-011--R-015 certify specified common-polarization boundaries. R-019--R-023 remove the full first-row boundary band and the rectangular prolongation; R-024 gives recursive second-row ranges from actual degree-five and square bases. The remaining critical annihilator injects into N_r tensor Sym^(r²-1), where N_r has first row at least r²+1 and second row at least r(r-1).'),
      ('Q-W7','Width-seven orbit calculation T-020','Small direct formula for all remaining valuation-filtered G2 invariant spaces','open','T-018 evaluates the end-node sector; G-010 gives a general finite count; evaluate the remaining boundary valuation filtration.'),
      ('Q-ALPOGE','Alpoge Remark p.4 steps 7--8; named Lean files absent','Identify the period/theta-lift object with the normalizer projector or grid-map image','input and explicit-morphism gate','No such comparison map is specified in the four-page note; T-001--T-003 construct the exact compact realization used here.'),
      ('Q-MASULLO','Prompt requested locator; no supplied work','Determine the intended Masullo theorem and map','input gate','No Masullo source or statement identifier in the 25 supplied files.'),
    ]
    rows.extend(dict(zip(fields,r)) for r in openq)
    with (OUT/'QUESTIONS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    return rows

def build_tex():
    intro=(ROOT/'work/root/paper_front.md').read_text()
    chunks=[intro]
    for part,files in REPORTS:
        chunks.append('\\part{'+part+'}\n')
        for name in files:
            p=ROOT/name
            if p.exists(): chunks.append(p.read_text())
    md='\n\n'.join(chunks)
    (ROOT/'work/paper.md').write_text(md)
    cmd=['pandoc',str(ROOT/'work/paper.md'),'-f','markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+autolink_bare_uris',
      '-t','latex','-s','--toc','--number-sections','--top-level-division=section',
      '-V','documentclass=article','-V','fontsize=10pt','-V','geometry=margin=25mm',
      '-V','mainfont=DejaVu Serif','-V','monofont=DejaVu Sans Mono',
      '-V','mathfont=Latin Modern Math',
      '-V','colorlinks=true','--include-in-header='+str(ROOT/'work/preamble.tex'),
      '--lua-filter='+str(ROOT/'work/wrap_code.lua'),'-o',str(OUT/'GCT_PLETH.tex')]
    subprocess.run(cmd,check=True,capture_output=True,text=True)

def manifest():
    rows=[]
    for p in sorted((ROOT/'work').rglob('*')):
        if not p.is_file() or '__pycache__' in str(p):continue
        if p.suffix in ['.pdf','.txt','.html','.tar','.tex','.mw'] and ('external' in p.parts or 'archive' in p.parts or 'width7' in p.parts or 'end_node' in p.parts):
            rows.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'work/consulted_source_manifest.json').write_text(json.dumps(rows,indent=2))

def package(name):
    target=ROOT/name
    if target.exists(): raise FileExistsError(target)
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for p in sorted(ROOT.rglob('*')):
            if not p.is_file():continue
            rel=p.relative_to(ROOT)
            if rel.parts[0] not in ['deliverables','work','sources','upload']:continue
            if p.suffix=='.zip' or '__pycache__' in rel.parts:continue
            if 'library_helpers' in rel.parts or p.suffix in ['.o','.pyc']:continue
            if p.suffix=='' and p.name.startswith(('check_polarization','recheck_polarization','character_')):continue
            if 'texfmt' in rel.parts:continue
            if 'public_scans' in rel.parts and 'ranges' in rel.parts:continue
            if any(part.startswith('polarization_') and part.endswith('_parts') for part in rel.parts):continue
            if p.suffix=='.input' and p.stat().st_size>20_000_000:continue
            if p.suffix in ['.aux','.log','.toc','.out','.fls','.fdb_latexmk','.xdv']:continue
            # User-provided sources remain present. External papers are cited and hashed,
            # not redistributed; all current proofs, code and certificates are included.
            if rel.parts[0]=='work' and p.suffix in ['.pdf','.txt','.html','.tar','.tex','.mw','.png']:
                if 'external' in rel.parts or ('archive' in rel.parts and not any(token in p.name for token in ['CERTIFICATE','CHECK','RECEIPT','RESULT'])) or 'braun' in rel.parts or 'series' in rel.parts:
                    continue
                if 'width7' in rel.parts and p.name not in ['METRIC_PATH_CHECK.txt']:continue
                if 'end_node' in rel.parts and p.suffix=='.pdf':continue
            if rel.parts[0]=='deliverables': arc=str(Path(name[:-4])/Path(*rel.parts[1:]))
            else:arc=str(Path(name[:-4])/rel)
            z.write(p,arc)
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        names=z.namelist()
        for n in ['GCT_PLETH.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md']:
            assert name[:-4]+'/'+n in names,n
        assert not any(n.endswith('.zip') for n in names)
    return target

if __name__=='__main__':
    import argparse
    a=argparse.ArgumentParser();a.add_argument('--package');args=a.parse_args()
    es=merge_events();qs=questions();manifest();build_tex()
    print(json.dumps({'events':len(es),'questions':len(qs),'tex_bytes':(OUT/'GCT_PLETH.tex').stat().st_size}))
    if args.package:print(package(args.package))
