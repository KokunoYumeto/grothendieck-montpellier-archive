"""Build the reviewable report from actual statement, source, input and run records."""
from pathlib import Path
import csv,json,re,time
from datetime import datetime,timezone
T=time.perf_counter();R=Path(__file__).resolve().parents[1]
review_path=R/'notes/progress_review_state.json'
review=json.loads(review_path.read_text()) if review_path.exists() else None
stopping_rule_met=bool(review and review['no_movement_streak']>=2)
delivery_stage=('This is the final disposition after two consecutive scheduled hourly reviews without substantive movement. The package remains incomplete; stopping under that rule does not turn unmet source or documentation requirements into completed work.' if stopping_rule_met else 'This is a scheduled intermediate checkpoint, not a final completion claim.')
old=(R/'notes/report_history_checkpoint_02.md').read_text()
aux=(R/'logs/RESEARCH_SA22_paper.aux').read_text()
nums={m[1]:(m[2],m[3]) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux)}
results=list(csv.DictReader((R/'RESEARCH_SA22_results.csv').open()))
labels={x['id'] for x in results}
def refs(s):
 for lab in sorted(labels,key=len,reverse=True):
  if lab in nums:
   n,p=nums[lab];s=re.sub(r'(?<![\w:-])'+re.escape(lab)+r'(?![\w-])',f'{n} (`{lab}`, p.{p})',s)
 return s
rows=[]
for line in old.splitlines():
 if line.startswith('| ') and not line.startswith('| Item') and not line.startswith('|---'):
  v=[x.strip() for x in line.strip('|').split('|')]
  if len(v)==3 and (v[0].startswith(('A.','B.','C.')) or re.fullmatch('L[1-9]',v[0])):rows.append(v)
changes={
'A.2(e)':('Proved exact metric equation; blanket monotonicity Refuted','A2-collar-general, A2-collar-shape, A2-collar-explicit: unique nonlinear boundary-value relation; completely specified n=10000, epsilon=10^-14 collar, direct supersolution and exact certificates.'),
'A.3':('Corrected statements Proved under explicit seam hypotheses','A3-boundary-chart, A3-welding, A3-rectifiable, A3-graph, A3-slit, A3-L5: sufficient QS existence, removable uniqueness, vertex compatibility, both ambiguous073 readings.'),
'A.5':('Theorem Proved; overbroad proposition Refuted','A5-groupoid, A5-six-points, A5-moduli: characteristic5 exception; characteristic3 exceptional inertia24; characteristic2 degeneration explicitly checked.'),
'A.6(a)':('Framed reconstruction and precise specialization Proved; unrestricted readings Refuted','A6-anabelian, A6-procyclic, A6-three-classes, A6-model-system, A6-model-specialization, A6-tame-specialization, A6-intrinsic-tame, A6-wild-counterexample, A6-node-character, A6-frobenius-counterexample. All-DVR tests define an intrinsic tame category before a model exists; every existing proper log-regular model realizes the same category in mixed characteristic. All-cover and strict reconstruction-preservation readings are refuted. No arbitrary mixed-characteristic model-existence theorem is asserted.'),
'A.7':('Classification Proved with corrected scope','A7-gluing-modules, A7-domain-counterexample, A7-PID-count, A7-real-classification, A7-ratio-j, A7-real-topology. Connectedness alone does not repair the arbitrary-ring claim.'),
'B.1':('Characteristic-zero Proved; positive-characteristic deduction Known; first claim Refuted','thm:B1a-betti, thm:B1a-etale, thm:B1b-abelian, thm:B1c. The all-prime abelian result explicitly uses the opened 2026 Broe preprint.'),
'B.1(b)':('Known abelian result with checked deduction; exact method criterion and Fermat extension Proved; Ancona-only inference has a gap','prop:B1b-criterion, prop:B1b-gap, thm:B1b-abelian, prop:B1b-scope, B1b-correspondence, B1b-blowup, B1b-fermat. Algebraic Lefschetz projections and positivity on homological primitive algebraic classes specify the domain of this argument. Numerical positivity alone does not verify that condition.'),
'B.1(c)':('Refuted with complete generic construction','thm:B1c: generic quintic containing two specified skew lines, 114 coefficients, exact smoothness certificate, both doubtful glyph readings treated.'),
'B.2':('Both claims Refuted; exact positive replacement Proved','lem:B2-mumford, thm:B2-square, prop:B2-kernel: algebraically trivial divisor D on E times E, D^2 nonzero in CH^2; Albanese-kernel question separately treated.'),
'B.3':('All28 plus9 strongest proved formulations supplied; Fujiwara original-source reading remains INCOMPLETE','thm:B3-21, thm:B3-fujiwara and the 37-row inventory below. Gabber1994 original definition p325 and Theorem1 p326 now opened and directly applied; Fujiwara1995 original remains unopened. Modern completion-complement derivation is complete.'),
'L4':('Unqualified one-direction wording Refuted; full replacement Proved','A2-cap-limit, A2-explicit-limits, A2-nonbox, A2-independence. Fixed compactification and relative growth direction are indispensable; Koebe is the one-dominant-end limit.'),
'L5':('Proved under smooth-diffeomorphism/isometric-seam reading','A3-L5, A3-welding, A3-graph, A3-slit: nonzero derivative or explicit seam compatibility is retained.'),
'L7':('Correct stack/coarse distinction Proved','A5-moduli, A5-groupoid: quotient stack versus coarse line over Z[1/2,i]; exceptional inertia in characteristic3 is24.'),
'L9':('Known classification with complete independent derivation and original comparison','A7-real-classification, A7-PID-count, A7-real-topology. Alling–Greenleaf1971 Section1.9 pp60–66, especially Theorem1.9.8 and its table, now directly checked and matched to the lattice parameters.')}
changes.update({
'A.1':('Global isomorphisms and raw isotopy descent Refuted; exact actual-cut and geodesic replacements Proved','A1-global-refutation, A1-graph-range, A1-toric-domain, A1-toric-noninjective, A1-toric-full-discs, A1-toric-nondescent. Fixed-target imbalance changes the underlying welded four-pointed surface for all but finitely many phases in the specified family; the unequal seam and its own geodesic give different raw tensors in the same X. Geodesic replacement is the well-defined positive convention.'),
'A.1(a)':('Refuted; exact corrected range and noninjective toric fibers Proved','A1-global-refutation, A1-graph-range, A1-toric-noninjective: labelled nodal(0,4), q=17 versus cap bound16; corrected range 0<abs(q)<16; radius pairs(1,1) and(2,1/2) give the same tensor with distinct actual cuts.'),
'A.1(b)':('Refuted in every positive-complexity stable type; exact models Proved','A1-graph-range, A1-bordered-shadow-range, A1-bordered-shape-image, A1-toric-domain, A1-toric-full-discs, A1-zero, A1-cut-not-algebraic: equal-length tangent isomorphism; broader toric tangent kernel dimensionE and global real-E-dimensional fibers; both orbifold fundamental-group comparisons proved; zero-complexity exception.'),
'A.1(c)':('Global inverse Refuted; all requested local source identifications checked','A1-welding-plumbing, A1-kra-comparison, A1-wolpert-comparison, A1-first-order, A1-hinich-counterexample, A1-Earle-Marden-original. Joint original draft8/24/11 opened and explicit local construction derived; the prompt did not restrict its request to the distinct2012 chapter.'),
'A.6(b)':('Corrected presentations Proved with notation alternatives','A6-matrix-presentations, A6-four-punctures, A6-binary-S3, A6-projective-line, A6-birman, A6-presentation-types.'),
'C.1':('Exact corrected statements Proved; universal overstatements Refuted','C-exp-log, C-filtered, C-differential, C-other-autos, C-intertwine, C-functor-criterion, C-functor-counter, C-qcoh.'),
'C.2':('Exact literal-axiom classification Proved; ConditionK and symmetry overstatements Refuted','C-chain-true, C-K-counter, C-K-replacement, C-literal-class, C-extension, C-symmetry, C-packed-asymmetry.')})
for row in rows:
 if row[0] in changes:row[1:]=changes[row[0]]
extra=[
('A.4 orange model','Refuted; corrected asymptotic statement Proved','A4-orange-extremal, A4-orange-jets, A2-explicit-limits'),
('A.4 enlarged space/action','Known with derivation; action Proved','A4-grafting, A4-action: all mixed cusp strata, intrinsic monoid action, fixed sets and deformation retraction'),
('A.5 theorem089','Proved','A5-normalizer, A5-groupoid; every algebraically closed characteristic other than2, with descent in A5-moduli'),
('A.5 proposition086','Refuted in characteristic5; corrected theorem Proved','A5-six-points, A5-faces; 120-element PGL2(F5) stabilizer and five Klein groups'),
('A.6(a),049(a)','Proved under framed-logarithmic interpretation; ordinary-group reading Refuted','A6-ordinary-counterexample, A6-kummer, A6-graphic, A6-normal-kummer, A6-anabelian'),
('A.6(a),049(b)','Bare criterion and automatic-cyclotomic parenthesis Refuted; exact corrected recovery and character Proved','A6-procyclic, A6-cyclotomic-detection, A6-node-character. The node inertia character is cyclotomic times the branch-interchange sign; the explicit rational nonsplit nodal cubic verifies the failure.'),
('A.6(a),049(c)','Precise model/reconstruction statements and mixed-characteristic tame comparison Proved; all-cover, chosen-fibre and strict-preservation readings Refuted','A6-model-system, A6-model-specialization, A6-special-fibre-counterexample, A6-tame-specialization, A6-intrinsic-tame, A6-wild-counterexample, A6-frobenius-counterexample. The intrinsic all-DVR category is defined without a model. Any two existing proper log-regular models realize that same tame subcategory through explicit valuative comparison; no common regular refinement or general mixed-characteristic resolution is assumed.'),
('A.6(a),NB048','Literal trichotomy Refuted; geometric classes specified','A6-three-classes'),
('B.2 square','Refuted','thm:B2-square; D is a divisor on E times E and its square is a nonzero zero-cycle class'),
('B.2 second question','Refuted; kernel structure Proved','thm:B2-square, prop:B2-kernel'),
('B.1(b) argument domain','Proved under explicit independent hypotheses, with explicit geometric members','prop:B1b-criterion, prop:B1b-scope, B1b-correspondence, B1b-blowup, B1b-fermat: exact domain of the componentwise-definiteness proof; abelian and Fermat cubic fourfold seeds, forms, correspondence transfers and smooth blowups verify membership. No exhaustive geometric isomorphism classification is asserted.'),
('B.3 subject21','Proved modern statements; direct-original obligation INCOMPLETE','thm:B3-21, thm:B3-fujiwara; henselian restriction and completion-complement rigidity separated')]
# Insert extra task rows after their parent where possible; all required original rows retained.
for e in extra:
 parent=e[0].split(' ')[0].split(',')[0]
 idx=next((i+1 for i,r in enumerate(rows) if r[0]==parent),len(rows));rows.insert(idx,list(e))
lines=['INCOMPLETE','','## Outcome table','','| Item | Outcome and scope | Numbered statement / remaining gate |','|---|---|---|']
for a,b,c in rows:lines.append('| '+a+' | '+b+' | '+refs(c)+' |')
lines += ['','# Research report','','AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed. We distinguish mathematical statements proved under their written hypotheses from the separate requirement to fetch specified originals. '+delivery_stage,'',
'## Current mathematical conclusions and remaining requirements','',
'The main unrestricted global surgery claim is false already for labelled nodal type(0,4): the tensor17 exceeds the cap-product bound16. The equal-length geodesic model has an exact graphwise range and an invertible real tangent map. The broader model with actual toric seams and independent paired lengths has the same tensor/shadow range, but one real fiber coordinate per edge: the difference of the squared paired lengths. Its tangent kernel therefore has dimensionE. Both models have the proved orbifold fundamental-group comparison. Full external disc shapes impose the separate matching-shape criterion and are not assigned those unrestricted real fibers. Arbitrary-cut and external-only admissibility readings have additional explicit failures. The natural full cut cover in type(0,4) is not algebraic of finite type; the zero-complexity case is treated separately.','',
'Raw toric surgery also fails to descend to isotopy classes in a fixed conformal surface. The proof constructs a four-point plumbing family, computes its exact cubic crossratio coefficient, and obtains a nonzero difference between balanced and unbalanced caps. Its phase is specified exactly by a least-positive-integer rule, whose existence is proved analytically; no numerical value of that integer is claimed. The unequal seam and its own geodesic then give different raw tensors in the same surface. Geodesic replacement supplies the separate well-defined convention.','',
'The capping theorem gives injectivity and the full open convex logarithmic image by weighted Strebel support inequalities on every fixed pointed compactification. Relative growth directions determine the limit. The collar theorem includes a fully specified analytic sign-changing counterexample, not just an infinitesimal heuristic. Part C gives exact algebraic criteria and complete finite counterexamples. Part B supplies all 28 subjects and nine Pour mémoire headings under the prompt\'s strongest-proved-statement alternative. Broad historical headings are not represented as universal solutions of motives, positive-characteristic resolution, or every SGA2 problem.','',
'For the arithmetic specialization question, all-DVR finite Kummer–étale extension tests define an intrinsic Galois category for every variety in the written scope, before a model is available. An existing proper log-regular model and its strict special log fibre realize that same tame category. The paper separately proves the wild-cover obstruction, the cyclotomic-times-branch-sign formula at a nonsplit node, and the relative-Frobenius counterexample to preserving strict reconstruction under reduction. None of these comparisons asserts general mixed-characteristic resolution or recovery of a special scheme from its tame group.','',
'The requested joint Earle–Marden comparison is checked from the actual original author manuscript dated24August2011. Its local exponential, sewing, collar and normal-tensor formulas are derived directly, with the draft misprints identified. No global chart theorem is inferred. The distinct2012 published chapter remains unopened, but was not specified as the sole acceptable source. Gabber1994 original pp325–326 now supply its exact henselian-pair definition and complete main Theorem1 statement; their direct application and the finite-algebra converse discharge that original-source requirement. Its later Section5 Corollary1 and full original proof are not claimed read. The prescribed Fujiwara1995 original remains outstanding; the modern completion-complement deduction is complete and separately identified. The live bibliography-status inventory below records the remaining named historical sources and does not count a later citation as an opening of an original.','',
'The all-prime positive-characteristic abelian-fourfold theorem explicitly uses Broe2026 as a preprint. We opened its theorem statements and checked the deduction here; we do not claim an independent verification of its entire proof. Ancona2021 alone supplies positivity on the numerical quotient and does not remove the homological radical.','',
'The B1(b) argument-domain statement uses independently stated algebraic Lefschetz and homological-positivity hypotheses. It determines precisely where the componentwise-definiteness proof applies; it is not an assumption that numerical and homological equivalence already agree. Geometric families and transfer constructions verify membership in that domain. A classification of every geometric isomorphism type is neither claimed nor introduced as an extra unresolved obligation.','',
'## What we read','',
'The attached ZIP was unpacked once. Its28 text files were treated as research inputs, not proof certificates. We read the full prompt, study, hunches, packages, relevant correction/dependency/check-event tables, readings and transcriptions. The unchanged attached files are omitted from this archive. The official Montpellier PDFs were retrieved separately because no scan PDFs were attached.','',
'Original images used for mathematical decisions include67/048–052,065–066,073–082,086–087,089–092,100–101;66/004–005;68/015–017,019–022,044–046. Exact image decisions and retained ambiguities are in the check-event and correction records. A read of a transcription is not presented as a new palaeographic decision. In particular, both interpretations of the doubtful073 normalization and24 first-question glyph are treated. The actual nongeodesic-cut and polar-rescaling passages079–082 motivated the explicit unequal-length toric model.','',
'Opened sources are identified individually below, with exact locator and scope. Downloaded is not synonymous with read. We distinguish full text, selected original passages, a publisher preview, metadata, and unsuccessful access. The source manifest records hashes/URLs of recreatable public caches; the checkpoint preserves authored notes, scripts and logs. Full non-user source-page extracts and copied web prose are treated as reading caches. Their source URLs, locators, result identities, original hashes, command counts and measured timings remain in the delivery records; field-level normalization manifests preserve the exact provenance. Mathematical certificate outputs and authored proof/audit text are retained. The source-cache audit distinguishes these raw originals from the supplied manuscript material and our generated PDF inspection images.','',
'### Search for prior studies','',
'We searched both web engines for studies of cotes66–68 and the surgery/plumbing/capping claims; inspected Michel Hua\'s project and the Cercle Scientifique Grothendieck letter transcription; and opened Fırat2023 for the radius-variation identity. We retain the input\'s credit to Michel Hua\'s project for the quarter-bound, orange-model and marking arguments. The current search does not establish absence of earlier work or any priority. Exact queries, URLs and limits are in notes/root_literature_search.md.','',
'## Complete B.3 inventory','',
'This table lists the exact proved scope for every historical heading; the detailed theorem contains the hypotheses and deduction.','',
'| Item | Result | Status | Statement | Opened source locator / qualification |','|---|---|---|---|---|']
for r in csv.DictReader((R/'checks/part_b_inventory.tsv').open(),delimiter='\t'):
 labs=re.findall(r'(?:thm|prop|lem):[\w-]+',r['where_proved']);loc=r['source_locators']+'; '+r['scope_notes']
 lines.append('| '+' | '.join([r['item'],r['statement'],r['status'],refs('; '.join(dict.fromkeys(labs))),loc.replace('|','\\|')])+' |')
lines+=['','## Programs, scope, counts and runtime','','Every retained program and associated output is inventoried below. Exact finite certificates verify their specified instances; floating-point samples are diagnostics only. Source-fetch, bibliography, record-generation, OCR and build scripts are not mathematical proof verifiers. A missing historical runtime is explicitly marked; it is not reconstructed by guessing.','',
'### Root mathematical certificates','','| Program | Scope and complete count | Recorded seconds |','|---|---|---|',
'| part_a_certificates.py | Five exact rational assertions: two jets, annulus inclusions/extremal bounds, tensor17 versus16 | 0.000244686 |',
'| part_a_collar_checks.py | Four symbolic local moving-boundary identities; no global numerical PDE claim | 0.781925 |',
'| part_a_plumbing_checks.py | Seven exact assertions; explicit Hinich parameters, derivative0 and nonzero second derivative | 0.142639 |','']
for name in ['part_c_program_scope.md','part_a567_program_scope.md','part_b_program_scope.md']:
 p=R/'notes'/name
 if p.exists():lines+=['### '+name,'',p.read_text(),'']
# Inventory all executed source/admin scripts and their recorded outputs, extracting only saved time fields.
def walk_time(x,path=''):
 out=[]
 if isinstance(x,dict):
  for k,v in x.items():
   if any(t in k.lower() for t in ['second','elapsed','runtime']) and isinstance(v,(int,float)):out.append((path+k,v))
   elif isinstance(v,(dict,list)):out+=walk_time(v,path+k+'.')
 elif isinstance(x,list):
  for i,v in enumerate(x):out+=walk_time(v,path+str(i)+'.')
 return out
recorded_runs={}
def saved_run(script, seconds, locator, kind='measured wall time'):
 if isinstance(seconds,(int,float)):
  recorded_runs.setdefault(Path(script).name,[]).append((kind+': '+locator,seconds))
for p in sorted((R/'code').glob('root_timed_build_*_output.json')):
 d=json.loads(p.read_text());saved_run(d['driver'],d.get('elapsed_seconds'),str(p.relative_to(R)))
for p in sorted((R/'code').glob('root_refresh_records_*_output.json')):
 d=json.loads(p.read_text())
 for run in d.get('results',[]):saved_run(run['script'],run.get('seconds'),str(p.relative_to(R)))
for p in sorted((R/'code').glob('root_save_checkpoint_*_output.json')):
 d=json.loads(p.read_text());saved_run('code/root_save_archive.py',d.get('seconds'),str(p.relative_to(R)),'prepared archive save, measured wall time')
timing=R/'code/part_a567_timing_audit.json'
if timing.exists():
 for run in json.loads(timing.read_text()):saved_run(run['script'],run.get('wall_seconds'),str(timing.relative_to(R)),'recorded timing-only rerun')
timing=R/'code/part_c_finalize_audits_output.json'
if timing.exists():
 for run in json.loads(timing.read_text()).get('timed_reruns',[]):saved_run(run['script'],run.get('wall_seconds_including_python_startup'),str(timing.relative_to(R)),'recorded timing-only rerun')
timing=R/'checks/part_a567_historical_runtime_audit.csv'
if timing.exists():
 for run in csv.DictReader(timing.open()):
  if run.get('recorded_seconds'):
   saved_run(run['script'],float(run['recorded_seconds']),run['existing_log_locator'],run['measurement_scope'])
inventory=[]
for p in sorted((R/'code').iterdir()):
 if p.suffix not in {'.py','.sh','.js'}:continue
 outs=[x for x in sorted((R/'code').glob(p.stem+'*')) if x!=p and x.suffix not in {'.py','.sh','.js'}]
 times=[];counts=[]
 for o in outs:
  try:
   data=json.loads(o.read_text());times+=walk_time(data)
   if isinstance(data,dict):
    for k,v in data.items():
     if any(t in k.lower() for t in ['attempt','assertion','count','events','rows','candidate']) and isinstance(v,(int,float,str)):counts.append(k+'='+str(v))
   elif isinstance(data,list):counts.append('output records='+str(len(data)))
  except Exception:
   for m in re.finditer(r'"(?:seconds|elapsed_seconds)"\s*:\s*([\d.]+)',o.read_text(errors='replace')):times.append(('seconds',float(m[1])))
 times+=recorded_runs.get(p.name,[])
 kind=('mathematical certificate / diagnostic' if any(t in p.stem for t in ['checks','certificates','collar_explicit','char2_edge','char3_inertia','extensions','b3_audit']) else 'source, metadata, build or archive utility')
 tv='; '.join(f'{k}:{v:.6g}s' for k,v in times[:5])
 if len(times)>5:tv+=f'; {len(times)} saved individual timing values in outputs'
 if not tv:tv='not recorded in a machine-readable output; see retained command/build log'
 inventory.append(dict(program=str(p.relative_to(R)),scope=kind,counts='; '.join(counts) or 'scope recorded in program and named note',runtime=tv,outputs='; '.join(str(x.relative_to(R)) for x in outs)))
lines+=['### All retained program files','','| Program | Role / recorded count | Recorded runtime | Output |','|---|---|---|---|']
for x in inventory:lines.append('| '+x['program']+' | '+x['scope']+'; '+x['counts']+' | '+x['runtime']+' | '+(x['outputs'] or 'retained logs/; script may be newly written pending execution')+' |')
with (R/'checks/program_inventory.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(inventory[0]));w.writeheader();w.writerows(inventory)
lines+=['','### Historical timing limitations','',
 'Some early failed prototypes, failed source requests and administrative commands did not retain an elapsed-time measurement. Those missing historical runtimes are explicitly marked in the inventory and detailed scope notes. A later measured rerun is labelled as such and is not presented as the duration of the original execution. No value has been inferred from file timestamps or invented. The two failed A567 main-check prototypes and the failed IAS request retain this limitation. This is a reporting limitation separate from the outstanding original-source readings; bookkeeping and timing reconciliation do not count as movement in the substantive reviews.','']
lines+=['','## Corrections to the supplied files','','No attached input was overwritten. The following exact file/line tables distinguish new corrections, refinements and independently confirmed readings. A statement corrected in our own draft is separately documented in audit notes and is not falsely assigned an input line.','']
for p in sorted((R/'checks').glob('*_corrections.tsv')):
 lines+=['### '+p.name,'','| Attached file | Line(s) | Earlier claim / reading | Correction or confirmed scope | Statement |','|---|---|---|---|---|']
 for x in csv.DictReader(p.open(),delimiter='\t'):
  vals=[x[k] for k in ['input_file','input_lines','claim_or_reading','correction','statement_ids']]
  vals[-1]=refs(vals[-1]);lines.append('| '+' | '.join(v.replace('|','\\|').replace('\n',' ') for v in vals)+' |')
for name in ['part_c_input_audit.md','part_a34_secondary_audit.md','part_c_required_originals.md','root_original_followup_03.md','part_b_a6_scope_audit.md','part_b1b_class_secondary_audit.md','root_toric_scope_resolution.md','root_post_review03_proof_audit.md','part_b3_complete_scope_audit.md','part_c_a6_adversarial_scope_audit.md','root_intrinsic_tame_audit.md','root_a2_b2_c1_precision_audit.md','part_c_functor_criterion_scope_audit.md','root_muse_lieberman_audit.md','part_b_lieberman_ihes_followup.md','part_a567_lieberman_public_collections_audit.md','part_c_pfluger_distinct_public_audit.md','root_fujiwara_ihes_audit.md','root_source_route_followup09.md','part_a567_pfluger_insa_audit.md','part_a567_pfluger_failed_ocr_assessment.md','part_b_fujiwara_dukespace_route.md','part_c_lieberman_cambridge_audit.md','part_b_a2_regularity_audit.md','root_available_file_title_check.md','part_a567_pfluger_article_registry_audit.md','part_c_lieberman_zbmath_audit.md','root_core_semantic_routes.md','part_b_fujiwara_ndl_duplicate_route.md']:
 p=R/'notes'/name
 if p.exists():lines+=['### Supporting proof or source audit: '+name,'',p.read_text(),'']
for name in ['part_c_lieberman_books_audit.md', 'part_b_b1b_final_handoff_audit.md', 'part_a567_toric_handoff_consistency.md', 'part_c_refuted_polarity_audit.md', 'root_refuted_record_wording.md', 'root_fujiwara_japan_repositories.md', 'part_b_lieberman_course_route.md', 'part_a567_pfluger_tifr_audit.md', 'part_a567_remaining_originals_openrepo_audit.md', 'root_fatcat_delayed_availability.md', 'part_b_lieberman_cambridge_delayed.md']:
 p=R/'notes'/name
 if p.exists():lines+=['### Supporting proof or source audit: '+name,'',p.read_text(),'']
named_cache=R/'code/part_c_normalize_named_source_cache_output.json'
if named_cache.exists():
 lines+=['### Targeted source-cache normalization before checkpoint10','',
 'The remaining15 raw retrieval blocks in one partially normalized Pfluger query record and33 description fields in the first OpenAIRE response were replaced by provenance pointers. The exact original bytes remain in the external source cache. The saved restoration checks prove that every unselected JSON value, the two previous cache stubs and all separators are unchanged; the metadata-only second OpenAIRE page is byte-identical. Indented serialization increased the first response\'s byte size despite removing its selected prose, which is recorded rather than described as size reduction. No mathematical program, proof, source status or prior archive changed. This cache correction is not substantive movement.', '',
 '```json',named_cache.read_text().strip(),'```','']
handoff_source_note=R/'notes/root_b1_handoff_sources.md'
if handoff_source_note.exists():lines+=['### Primary-source wording at handoff','',handoff_source_note.read_text(),'']
lines+=['## Bibliography: actual opened scope','','The .bib contains every source entry with its opened/not-opened note. The following inventory reproduces those notes, including previews and missing original texts. Theorems actually used are cited at the point of use in the paper.','', '| Key | Source title | Opened scope and exact locator |','|---|---|---|']
def field(s,key):
 m=re.search(r'\b'+key+r'\s*=\s*\{',s,re.I)
 if not m:return ''
 i=m.end();start=i;depth=1
 while i<len(s) and depth:
  depth+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[start:i-1]
bib=(R/'RESEARCH_SA22_references.bib').read_text()
for m in re.finditer(r'@\w+\s*\{([^,]+),',bib):
 start=m.start();i=m.end();depth=1
 while i<len(bib) and depth:depth+=(bib[i]=='{')-(bib[i]=='}');i+=1
 s=bib[start:i];lines.append('| '+m[1]+' | '+field(s,'title').replace('|','\\|')+' | '+field(s,'note').replace('|','\\|')+' |')
lines+=['','## Verification and typesetting','','The latest machine audit is reproduced here. This is a record-consistency test, not a theorem prover.','', '```json',(R/'logs/records_audit.json').read_text().strip(),'```','',
'Earlier full compilation found two overfull boxes above2pt (26.38113pt and5.72717pt). Both were corrected. Checkpoint02 build09 had zero overfull boxes, zero undefined references/citations and zero missing-character diagnostics. Pages1,15,26,40,53,58,59,65,69,70,74,76,89,96 were rendered and inspected, including former overflow locations;65 and69 were checked again after the proof-audit corrections. Later build QA is appended below from its saved record.','']
for p in sorted((R/'logs').glob('typesetting_checkpoint_*.json')):lines+=['### '+p.name,'','```json',p.read_text().strip(),'```','']
current_qa=R/'logs/typesetting_current.json'
if current_qa.exists():lines+=['### Current build verification','','```json',current_qa.read_text().strip(),'```','']
review_text=('The latest substantive review was completed at '+review['review_time']+'. '+review['summary']+' Consecutive reviews without movement: '+str(review['no_movement_streak'])+'. Next review: '+review['next_review']+'.' if review else 'The first substantive review is due15:04 Europe/Berlin (14:04UTC), then hourly. No no-movement count has yet been assigned.')
live_path=R/'notes/live_source_requirements.json'
if live_path.exists():
 live=json.loads(live_path.read_text())
 review_text+=' The separate live source register currently has '+str(len(live['remaining']))+' outstanding originals: '+', '.join(live['remaining'])+'. It records '+', '.join(live['closed_since_review1'])+' as closed since review1; these updates do not rewrite the dated review1 snapshot.'
math_path=R/'notes/live_mathematical_scope_gaps.json'
if math_path.exists():
 math_live=json.loads(math_path.read_text())
 math_open=[x for x in math_live if not x['status'].startswith('closed:')]
 review_text+=' The current mathematical-scope register has '+str(len(math_open))+' open rows. Closures after a dated review are preserved with their actual timestamps and are counted only at the next scheduled review; the earlier snapshot is not rewritten.'
lines+=['## '+('Final disposition' if stopping_rule_met else 'Progress reviews and continuation state'),'','The run started19 November2026 at12:04 Europe/Berlin (11:04UTC). '+review_text+' PROGRESS_LEDGER.md preserves every dated state and exact remaining gate.','']
if stopping_rule_met:
 lines+=['We stop under the user\'s explicit two-consecutive-no-movement rule. The two final reviews found no changed open row and no strictly smaller main-question gate. Further negative searches, proof rereads, typesetting and packaging were not counted as movement. The final package remains INCOMPLETE because the three prescribed original readings are outstanding and some historical execution durations were not recorded. No inaccessible original, unknown runtime, blanket solution of a broad historical programme, or unrestricted specialization statement is represented as verified.','',
 'If the work is resumed with additional source access, the first concrete steps are to read Pfluger1960 pp401–412, the relevant Lieberman1968 mathematical statement and hypotheses, and Fujiwara1995 Corollary6.6.4 or an equally explicit original comparison; then compare those statements with the proved formulations already in Part I. The earlier attempts, their exact limits and the current strongest proved statements are retained above. Historical runtimes that were never measured cannot be recovered by guessing or by relabelling a later rerun.','']
else:
 lines+=['Continue by obtaining the named missing original passages through lawful public or authorized routes; checking their exact hypotheses against the proved replacements; closing any further scope issue found by independent audit; and rebuilding the report/CSV/events/PDF after source changes. No request to stop or to approve continuation has been made. A final package is not represented as complete while a required row remains unfulfilled.','']
(R/'RESEARCH_SA22_report.md').write_text('\n'.join(lines))
summary=dict(outcome_rows=len(rows),numbered_statements=len(results),program_files=len(inventory),report_bytes=(R/'RESEARCH_SA22_report.md').stat().st_size,seconds=time.perf_counter()-T)
(R/'code/root_reconcile_report_output.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
