#!/usr/bin/env python3
"""Assemble a readable report without converting scoped results into completion."""
from pathlib import Path
import csv,json,re,datetime
root=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
stamp=now.astimezone(datetime.timezone(datetime.timedelta(hours=1))).strftime('%d %B %Y, %H:%M Europe/Berlin')
final_path=root/'logs/final_status.json'
final_status=json.loads(final_path.read_text()) if final_path.exists() else None
if final_status:
 assert final_status['status']=='INCOMPLETE'
 review=json.loads((root/final_status['stopping_review_path']).read_text())
 assert review['stop_required'] is True and review['consecutive_stagnant_reviews']>=2
 status_sentence=('This is the final INCOMPLETE report for this run. Research stopped at '
                  +final_status['research_stopped_utc']+' after two consecutive scheduled reviews without qualifying movement. '
                  'The remaining typesetting, verification and delivery implement that required stop; the report does not claim full completion.')
else:
 status_sentence='This is a continuing research checkpoint, not a final completion claim.'
rows=list(csv.DictReader((root/'RESEARCH_SA22_results.csv').open()))
byid={r['id']:r for r in rows}
def ids(labels):
 out=[]
 for label in labels.split(','):
  label=label.strip(); row=byid.get(label,{})
  n=re.search(r'Printed (\w+) ([^;]+)',row.get('notes',''))
  out.append((n.group(1).title()+' '+n.group(2)+' ' if n else '')+'`'+label+'`')
 return '; '.join(out)

def cell(value):
 """Keep literal mathematics and registry separators inside one Markdown cell."""
 return str(value).replace('|',r'\|').replace('\n',' ')

def typesetting_summary():
 build=json.loads((root/'logs/integrated_build_summary.json').read_text())
 qa=json.loads((root/'logs/paper_visual_qa.json').read_text()) if (root/'logs/paper_visual_qa.json').exists() else {}
 prefix=('The compiler history is preserved under `logs/build_runs/`. Initial integration reported two overflows: '
         '37.58698pt in the collar energy display and12.18524pt in the Dolbeault numerator. Both were split in their source. ' +
         'Checkpoint05 integration initially added two overfull boxes,0.34938pt and26.9502pt (one above2pt); the lifting-theorem sentence and long certificate paths were revised. ' +
         'Checkpoint06 integration briefly reported6.6833pt while citations were unresolved; the resolved final result is0.7931pt, within the required2pt limit. Actual visual QA also caught stale contents references, so an additional pass was required and the publication gate now rejects remaining rerun warnings. ' +
         'Checkpoint07 integration first exposed a missing display terminator and unescaped underscores in two bibliography notes; these source syntax defects were corrected and the failed build logs retained. Its citation-unresolved passes contained two overfull boxes,0.7931pt and6.6833pt, of which one exceeded2pt. After the bibliography and references resolved, the final build contains one overfull box of0.7931pt on page97 and none above2pt. All six contact sheets and full-resolution pages97 and101–109 were actually inspected, including the changed material. ')
 prefix+=('Checkpoint09 integration initially reported two overflows: the retained0.7931pt line and a new80.84181pt certificate-filename paragraph on page159, so one exceeded2pt. The two long filenames were split into separate list entries with breakable paths, without changing any statement, proof or computation. The original audited fragment and failed publication-gate build are preserved. ')
 if (root/'logs/ROOT_final_typesetting_cleanup.json').exists():
  prefix+=('The first post-stop publication build exposed four font-fallback warning entries for the bold tensor-unit notation and one skipped-bookmark-level warning. Publication formatting then used the Unicode bold digit and made the first A.2(a) heading a subsection directly under its section. The mathematical content, labels and statuses are unchanged; exact pre-edit bytes and the unapproved render record are preserved in the final-typography records. ')
 counts=(f"The latest {len(build.get('passes',[]))}-pass build ({build.get('started_utc','time not recorded')}) reports "
         f"{build.get('overfull_count','unknown')} overfull boxes, {build.get('overfull_above_2pt','unknown')} above2pt, "
         f"{len(build.get('undefined_warnings',[]))} undefined-reference/citation warnings, and "
         f"{len(build.get('missing_glyphs',[]))} missing-glyph warnings, with "
         f"{len(build.get('rerun_warnings',[]))} remaining rerun warnings. ")
 if build.get('passes') and build['passes'][-1].get('log'):
  final_pass=(root/build['passes'][-1]['log']).read_text(errors='replace')
  counts+=(f"The complete final-pass log additionally contains {final_pass.count('LaTeX Font Warning:')} font-fallback warnings, "
           f"{final_pass.count('Package hyperref Warning:')} hyperref warnings, and "
           f"{final_pass.count('Package unicode-math Warning:')} unicode-math/mathtools compatibility notices. "
           'The compatibility notices identify the selected bracket/colon command definitions; they are retained in the log and are not represented as missing glyphs or unresolved references. ')
 same=bool(build.get('pdf_sha256')) and build.get('pdf_sha256')==qa.get('pdf_sha256')
 if same and str(qa.get('inspection','')).startswith('PASS'):
  visual=(f"The {qa.get('pdf_pages')} page PDF was rendered on pages "
          +', '.join(map(str,qa.get('rendered_pages',[])))+'. '+qa.get('inspection','')+' ')
 else:
  visual='Visual inspection of this latest build is pending; an earlier inspection does not approve a changed PDF. '
 changed=build.get('source_changed_during_build',[])
 integrity=('The included TeX and bibliography hashes were identical before and after all compilation passes. '
            if 'source_changed_during_build' in build and not changed else
            'Source consistency must be checked before publication. ')
 return prefix+counts+visual+integrity+'Exact build and visual records are in `logs/integrated_build_summary.json` and `logs/paper_visual_qa.json`.'

outcomes=[
('A.1(a)','Refuted; complete corrected fibre proved','A:04,A:04-exact-image','Unrestricted tensor17 has no preimage; exact fixed-normalization image0<|q|<16.'),
('A.1(b)','Refuted globally; exact graph image, tangent map and fundamental-group comparison proved','A:alltypes,A:fullcaps,A:graph-radius-domain,A:graph-pi-one,A:bordered-radius-algorithm','All stable types; complexity-zero(0,3), self-node(1,1), cusp faces and orbifold conventions included.'),
('A.1(c)','Proved local comparison and corrected moving-cap inverse; global identification refuted','A:cap-plumbing-equation,A:plumbing-sources,A:EarleMarden-local,A:hinich-explicit','Kra/Wolpert/Hubbard–Koch and the complete primary Appendix proof of Earle–Marden comparison opened. Unopened2012 chapter is a bibliographic limitation, not a missing proof of this comparison.'),
('A.2(a)','Refuted; stronger single-cap determination proved','A:single-cap-all-lengths,A:single-cap-with-cusps,A:pants-cap-dependence','One positive cap determines all boundary lengths. Explicit pants Taylor coefficients differ.'),
('A.2(b)','Proved','C:A2b-energy,C:A2b-support-integral,C:A2b-image','Injective in every fixed cusp face; full logarithmic image given by all JS support inequalities. Independent audit passed.'),
('A.2(c)','Proved with the necessary multivariable limit distinction','C:A2b-strebel-limit,C:A2b-pants-extremes','Arbitrary relative growth yields JS cells for limiting squared-length weights; zero-weight caps collapse. One dominant pants end gives Koebe slit and radius4.'),
('A.2(d)','Proved','A:grafting,A:cuspnorm','Canonical cusp tangent norm, all horocycle decorations, exact length bundle and section; physical cap radii are not free decoration parameters.'),
('A.2(e)','Refuted for arbitrary collars; equidistant comparison proved','A:collar,C:A2e-nonmonotonicity','An explicit high-frequency analytic inward collar produces both metric signs; variational PDE proof covers every compact hyperbolic bordered surface.'),
('A.3; Théorème4, Lemma4B, Scholie073','Corrected statements proved','A:welding,A:slit,A:fold,A:L5','Whole-bank QS, fold-distance comparability and removable seam hypotheses retained; existence and uniqueness distinguished.'),
('A.4; orange model','Refuted; corrected canonical model proved','A:orange','Hua-project extremal-length argument credited and rederived with exact constants; correct model is implicit cap/length parametrization.'),
('A.4; enlarged Teichmüller space and action','Proved','A:grafting,A:action','Nonnegative boundary lengths, cuspidal faces, intrinsic multiplicative action and normalization section.'),
('A.5; Theorem089','Proved for characteristic different from2','A:fourpoint-groupoid','Includes characteristic5; retains the Klein subgroup rather than only its six-point set.'),
('A.5; Proposition086','Refuted at characteristic5; corrected theorem proved','A:octahedron,A:octahedron-certificate','Characteristic3 included;120-element exceptional stabilizer and five relevant Klein subgroups checked exactly.'),
('A.5; L7','Corrected stack/coarse statement proved','A:unordered-stack','Unordered stack and coarse j-line kept distinct; exact label is indexed in component register if the local heading changes.'),
('A.6(a);049(a)','Proved under stated arithmetic hypotheses','A:tensor-log-comparison,A:Kummer-faithfulness,A:log-graphicity,A:tangential-anabelian,A:nodal-q-test','Finitely generated field overQ, stable log curve and standard tangential normalization; independent source audit passed.'),
('A.6(a);049(b)','Literal criterion refuted; graph-theoretic replacement proved','A:inertia-maximality','Finite-index subgroups defeat the literal all-procyclic criterion; no unsupported maximality repair.'),
('A.6(a);049(c)','Intrinsic definition, uniqueness and full polycurve existence proved','A:compactification-obstruction,A:polycurve-coarse-compactification,A:anabelian-compactification-definition,A:intrinsic-anabelian-compactification,A:polycurve-four-dimensional-anabelian,A:log-specialization-higher','Every characteristic-zero hyperbolic polycurve has the canonical normal pair. Arithmetic reconstruction is established for strongly hyperbolic Artin neighbourhoods in all dimensions and arbitrary hyperbolic polycurves when either dimension is at most four, by Hoshi2014 TheoremB/Corollary3.18. Log specialization retains its model/prime hypotheses.'),
('A.6(a);NB048','Literal conjugacy-class claim refuted; topological-kind correction proved','A:three-types','Primitive slopes give infinitely many conjugacy classes; mapping-class orbits are a different relation.'),
('A.6(b);050–051 presentations','Proved with corrected labels and arithmetic interpretation','A:SL-GL-presentations,A:four-puncture-MCG,A:Birman,A:reflection-generators,A:arithmetic-quilts,A:real-Galois-obstruction','Arithmetic quilt action and change-of-basepoint formulas derived; extension to one fixed real group refuted with its exact real-place replacement.'),
('A.7;097–098 classification','Proved with corrections','A:real-elliptic','Real lattice types, square and hexagonal exceptions; ratio3, notsqrt3.'),
('A.7;100 count','Proved under the necessary proviso; omitted proviso refuted','A:pid-involutions','The stated PID/count hypotheses are retained; discriminant−11 yields three nonsplit classes.'),
('A.7;101 topology and H1','Proved','A:real-topology','Boundary and connectedness conventions, real locus and real Galois cohomology kept distinct.'),
('B.1(a)','Proved','B:betti,B:num-basechange,B:charzero','Rational Betti and every permitted l-adic prime over every characteristic-zero field.'),
('B.1(b)','Abelian statement proved from opened preprint; exact applicability class determined','B:ancona-scope,B:abelian,B:criterion','Broe2026 v1, Kahn and Ancona specialization. The class for the same positivity argument is given by a necessary-and-sufficient block-form criterion, with verified geometric families.'),
('B.1(c)','Refuted','B:tau','Image-verified tau reading; very general quintic and difference of two lines.'),
('B.2; product/square question','Refuted; full E×E kernel-generation replacement proved','B:trace,B:square,B:alb-kernel','Explicit elliptic curve and geometric generic pair; nonvanishing proved by trace forms.'),
('B.2; Albanese question','Refuted','B:square,B:alb-kernel','The same integral cycle is nontorsion in the Albanese kernel.'),
('B.3;28 subjects and Pour mémoire', 'Strongest proved catalogue statements supplied for all entries; two original-source obligations remain separately', 'B:nori-finite-flat,B:nori-base-change-counterexample,B:Lie-comparison-counterexample,B:Lie-comparison-integral-counterexample,B:integral-affinization,B:unipotent-homotopy,B:formal-homotopy,C:piecewise-graph-category,C:piecewise-group-fullness,C:piecewise-group-algebraization,C:absolute-flat-piecewise,C:absolute-flat-group-algebraization,B:finite-Greenberg-piecewise,B:uniform-partition-obstruction,B:finite-cover-partition-obstruction,B:complete-Greenberg-points,B:perfect-Greenberg-cohomology,B:Witt-localization-witness', 'Subject11 now has full finite-piecewise category/group-object comparisons, exact finite Greenberg realization, an explicit infinite partition obstruction persisting under finite-surjective additive sheafification, complete Greenberg points for arbitrary schemes, and perfect-test relative cohomology with smooth/finite-flat calculations. The modern sites, perfection, bounded-output and acyclicity hypotheses are explicit. These answer the permitted strongest-statement alternative; no equality of all historical sites or lexical identity of morcelés is asserted. The ordinary BLR functor alone is not equated with the archival partition functor. Subject15 likewise has precise Toën/Nori/Mondal–Reinecke statements and later-candidate refutations. Both original Gabber/Fujiwara source obligations remain in the next row. All28subjects and Pour-mémoire entries have exact locators and stated scopes.'),
('B.3; subject21 original-source derivation','General torsion assertion refuted; strongest stated positive replacements proved; original-source audit incomplete','B:henselian,B:henselian-general,B:H1-gate,C:torsion-degree-two-reduction,C:henselian-noetherian-pair-comparison,C:henselian-noetherian-closedpoint-criterion,C:henselian-affine-closed-fibre,C:Nagata-input,C:Goldman-branches,C:subject21-torsion-counterexample,B:nontorsion-rigidity,B:constant-integer-rigidity,B:Fujiwara,U:henselian-comparison','A completely constructed nonnoetherian nonseparated qcqs pair has universal H0 comparison but fails H1 comparison for every nonzero finite constant cyclic group. Nagata1952 with its1955 correction, proper graph closure and finite partial normalizations verify all hypotheses. Two affine examples separately refute unrestricted coefficients. Positive torsion comparison is proved for affine closed subschemes in quasi-separated pairs and all separated finite-type models over arbitrary noetherian henselian ring pairs. In the latter class universal H0 is exactly the closed-point condition. The original Gabber1994/Fujiwara1995 passages remain unobtained; this source obligation is separate from the now closed general mathematical gate.'),
('C.1(a)','Proved','C:filtered','Every commutative rational base algebra; no Noetherian or finite-module hypothesis.'),
('C.1(b)','Proved; exact criterion and nonexponential cases given','C:differential,C:conormal,C:squarezero,C:counterexamples','Uniform unipotence of the conormal action is necessary and sufficient; explicit nilpotence bound.'),
('C.1(c)','Proved','C:intertwine','Arbitrary modules and elementwise locally nilpotent operators; no global Hom nilpotence assumption.'),
('C.1(d)','Universal assertions refuted; exact image/fibre criteria proved','C:module-actions,C:functor-criterion,C:functor-counterexamples,C:functor-basechange,C:functor-separate-obstructions','All functors tested actionwise; finite-free base-extension hypothesis suffices. No unclaimed isomorphism classification of arbitrary functors.'),
('C.2(a)','Refuted; exact extra extremality condition proved','C:K-counterexample,C:K-repair','Full nondegenerate C4 certificate satisfies all axioms yet violates K.'),
('C.2(b)','Literal printed data classified; stronger coverage claims separated','C:group-classification,C:integer-system,C:classification-scope,C:C3-coverage-obstruction','Both readings of G[2], infinite groups, covariance and nonforced kernel condition. Exhaustive C3 certificate.'),
('C.2(c)','Refuted; reversal and abelian symmetry proved','C:symmetry','Both pretasse and tasse fail symmetry onS3; exact finite enumeration attached.'),
('L1','Proved','B:betti,B:charzero','Complete algebraic Lefschetz decomposition, numerical witness and descent.'),
('L2','Refuted; corrected inverse/image proved','A:04,A:fullcaps,A:graph-radius-domain','Local plumbing does not establish unrestricted global moduli isomorphism.'),
('L3','Proved in the precise decoration sense','A:cuspnorm,A:action','Cusp norms identify decoration fibres; actual cap radii retain coupled support constraints.'),
('L4','Corrected and proved','A:pants-cap-dependence,C:A2b-strebel-limit,C:A2b-pants-extremes','General JS projective limit; pants Koebe slit; nonbox and coupled cap dependence.'),
('L5','Proved','A:L5','The later smooth gluing arguments do not use rectifiable existence.'),
('L6','Corrected reconstruction, compactification and arithmetic interpretation proved','A:tangential-anabelian,A:polycurve-coarse-compactification,A:intrinsic-anabelian-compactification,A:polycurve-four-dimensional-anabelian,A:arithmetic-quilts,A:real-Galois-obstruction','The broad historical connection is supported; exact theorems require the stated tangential, log-geometric and arithmetic inputs. Hoshi2014 supplies arbitrary-polycurve arithmetic reconstruction through dimension four. Two independent compactification audits passed.'),
('L7','Corrected moduli statement proved','A:unordered-stack','Relative stack and coarse space distinguished; characteristic3/5 handled.'),
('L8','Refuted; exact corrected statements proved','C:K-counterexample,C:K-repair,C:group-classification','Closure of ordered cones does not imply ConditionK.'),
('L9','Proved with stronger corrections','A:real-elliptic,A:pid-involutions,A:real-topology','Connectedness alone does not repair the earlier eigenspace claim over general 2-regular rings.')
]

lines=['INCOMPLETE','','# Research report','','AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode. We claim no priority.','','Updated: '+stamp+'. '+status_sentence,'','## Outcome table','','| Item | Outcome | Statements | Exact scope / remaining gate |','|---|---|---|---|']
unknown=set()
for item,status,labels,note in outcomes:
 for label in labels.split(','):
  if label.strip() not in byid:unknown.add(label.strip())
 lines.append('| '+' | '.join(map(cell,[item,status,ids(labels),note]))+' |')
lines += ['','## Individual thesis subjects and Pour mémoire','','The following rows record the exact statement presently established. They do not silently enlarge its hypotheses. The fuller gate audit follows in its own section.','','| Entry | Statement | Status and exact scope |','|---|---|---|']
for n in range(1,29):
 label=f'B:subject{n}';r=byid.get(label,{})
 extra={11:',C:piecewise-graph-category,C:piecewise-group-fullness,C:piecewise-group-algebraization,C:absolute-flat-piecewise,C:absolute-flat-group-algebraization,B:finite-Greenberg-piecewise,B:uniform-partition-obstruction,B:finite-cover-partition-obstruction,B:complete-Greenberg-points,B:perfect-Greenberg-cohomology,B:Witt-localization-witness',15:',B:nori-finite-flat,B:Lie-comparison-counterexample,B:Lie-comparison-integral-counterexample,B:integral-affinization,B:unipotent-homotopy,B:formal-homotopy',16:',B:nori-finite-flat,B:nori-base-change-counterexample',17:',B:Picard-general,B:Picard-double-fibre',21:',B:H1-gate,C:torsion-degree-two-reduction,C:henselian-noetherian-pair-comparison,C:henselian-noetherian-closedpoint-criterion,C:henselian-affine-closed-fibre,C:Nagata-input,C:Goldman-branches,C:subject21-torsion-counterexample,B:nontorsion-rigidity,B:constant-integer-rigidity',23:',B:regular-pullback'}.get(n,'')
 lines.append('| '+' | '.join(map(cell,['Subject '+str(n),ids(label+extra),r.get('status','Not yet registered')+'; '+r.get('notes','')]))+' |')
for n in range(1,10):
 label=f'B:PM{n}';r=byid.get(label,{})
 extra=',B:local-Hurewicz' if n==9 else ''
 lines.append('| '+' | '.join(map(cell,['Pour mémoire '+str(n),ids(label+extra),r.get('status','Not yet registered')+'; '+r.get('notes','')]))+' |')
lines += ['','## What we read','','Every bibliography entry has an explicit opened/not-opened marker. Source-specific locators and access limitations are retained in the following records:','','- `notes/A567_sources.md`: octahedral, real elliptic, anabelian and presentation sources.','- `notes/B_catalogue_sources.md` and `notes/B_research_log.md`: all thesis-subject sources and verified manuscript readings.','- `notes/C_report.md`: algebra, inequalities and original-scan reading audit.','- `notes/ROOT_subject11_integration_audit.md` and the B/C Greenberg audits: exact category, partition, complete-point, relative-cohomology and source-coordinate checks; all historical limits retained.','- `A_references.bib`: plumbing, cusp normalization and welding sources, with exact opened sections.','- `notes/source_file_manifest.json` and `logs/*fetch*`: exact source hashes and successful/failed retrieval routes.','','Root independently reopened and checked Kahn Definition1/Theorem1, Ancona Corollary3.19 and Broe introduction/Section8; the A6 arithmetic source chain; Liu Lemma1.7/Theorem3.4; Mondello Theorem5.4 and collar appendix; Kra Theorems1–3; Hubbard–Koch Theorems9.11/10.1 and its complete Appendix; Wolpert Expansion4.2/Example4.3; Obitsu–Wolpert Theorems4/6; Hinich Sections2.1–2.3; Hamilton Section2; Lind Lemma6; and Rupflin Lemma2.9. Exact source editions are in the bibliography.','','## Computations, scope, counts and run times','','All finite mathematical examples have exact-arithmetic programs. Numerical pants calculations illustrate the analytic proof and do not replace it. Program-specific outputs are authoritative for enumerated scope and runtime; helper and build programs are administrative.','']
read_index = lines.index('## Computations, scope, counts and run times')
lines[read_index:read_index] = [
 'Additional original-source readings since checkpoint07 are documented in `notes/B_classic_sources_audit.md` (the verified1934 HLP chapterX, distinct from the unopened1952edition), the updated A567 source record (the recovered Nakamura1990 and Ihara–Nakamura1997 originals), and `notes/ROOT_source_audits_checkpoint08.md` (root\'s exact, narrower independent inspection). Their mathematical scopes and edition distinctions remain explicit.',
 '',
 'The current Pfluger publisher restriction and the restricted/dark Alling–Greenleaf and Lehto–Virtanen catalogue records are documented in `notes/ROOT_Pfluger1960_source_followup.md` and `notes/ROOT_classical_books_catalogue_followup.md`. These are opened metadata, not original theorem readings. The two remaining Gabber1994/Fujiwara1995 direct derivations are separate from these broader requested-source access limitations.',
 '',
 'Subsequent source coverage is recorded in `notes/B_Gabriel1932_source_audit.md` (the complete original Gabriel article, distinct from Gabber), `notes/A567_Birman_public_source_audit.md` (preview and errata; the relevant chapter remains unopened), and `notes/ROOT_Knudsen_Raynaud_source_audit.md` (selected original Knudsen–Mumford pages and only the two-page original Raynaud ChapterXI preview). Partial readings are not expanded into full-source or proof claims.',
 '',
 'The later complete Knudsen–Mumford reading finished at20:54:37UTC and covers all37 original printed pages19–55; `notes/C_KnudsenMumford1976_full_reading.md` records both the source proof text and its explicit omitted arguments/dependencies. The earlier selected-page reading remains accurate dated history. Independent original-context checks are in `notes/A567_Knudsen_sign_independent_audit.md` and `notes/B_KM1976_basechange_trace_audit.md`. The reproduced1973letter was read only on PDFpages40–42 of the identified43-page version; no handwritten-original, whole-letter or whole-paper reading is claimed. The auxiliary corrections have complete proofs and finite certificates in the paper and do not change either remaining task gate.',
 '',
 'The complete original Kleiman1994chapter, printed pp.3–20, was directly read; its exact Lefschetz and positivity locators and the unsuccessful original Lieberman1968 routes are in `notes/B_Lieberman_Kleiman1994_sources.md`. Lieberman remains explicitly not opened. `notes/ROOT_SGA45_SGA5_source_audit.md` records successful original SGA4½/SGA5 downloads and only the stated title, introduction, guide and contents readings. Those limited readings are not used as substitutes for body theorems or full-volume proofs.',
 '',
 'The post-review04 original-source attempts are preserved in `notes/ROOT_original_source_followup_2040.md`, `notes/B_Gabber_IA_collection_inventory.md`, and `notes/B_CORE_BASE_public_catalogue_audit.md`. These include a complete bounded public journal-catalogue inventory, actual dissertation records for a different Fujiwara work, and an observed catalogue challenge. No unavailable original theorem was relabelled as read.',
 '',
 'The later bounded discovery rechecks are recorded in `notes/ROOT_originals_discovery_recheck_2104.md`, `notes/ROOT_originals_discovery_recheck_2119.md`, and `notes/C_originals_route_assessment_2126.md`. One actual GDZ phrase-hit ambiguity was then resolved in `notes/C_Fujiwara_Crelle433_resolution.md`: it is an unrelated Akahori1992 article, whose original title and complete fourteen-entry bibliography were inspected. It supplies no Fujiwara manuscript identifier or original theorem passage. The two public requests, exact limited reading scopes, and an initial import failure before any request are preserved without promoting them into mathematical checks. Both original-source obligations remain unchanged.',
 '',
]
# Inspect saved program outputs; never execute the research programs here.
from C_program_provenance import computation_table
lines += computation_table(root)
lines += ['','## Typesetting audit','',typesetting_summary(),'','## Corrections with attachment locators','','Root corrections:','','1. `study/STUDY.md`, lines317–325: a nonzero nodal tensor is a normal direction/first-jet datum, not an unrestricted global finite plumbing parameter. The claimed historical resolution by plumbing does not establish the maps in the question; tensor17 refutes surjectivity.','2. `study/STUDY.md`, lines277–293, especially293: replacing rectifiable by single-bank quasisymmetric is insufficient at a slit tip. Whole-bank quasisymmetry, equivalently the added fold-distance comparison, is necessary. The example h(t)=t² separates these conditions.','3. `study/STUDY.md`, lines302–304 and418–429: the full conformal-radius image is the strict JS support domain; injectivity is proved, free Euclidean-disc surjectivity is false. A single actual positive cap determines all lengths.','4. `study/HUNCHES.md`, lines138–181: the pants one-dominant-length slit limit and nonbox conjecture are proved; the all-topology limit is a one- or multi-pole JS domain according to relative growth, not a universally planar slit.','5. `study/HUNCHES.md`, lines74–85: smooth welding suffices after073, but this does not establish the global section6 maps; the latter have independent tensor-image and partial-admissibility obstructions.','6. `PROMPT(20261119-143949).md`, lines86–88 (R8): the sheet itself writes15.1. without year;1984 is a reasoned archival dating, not an inscribed year.','', "7. Corrected primary source arXiv1311.0051v6, Section2.3 pp8–9 and Remark18.3 pp99–100: the printed Witt tuple lies in the localization under the source's standard coordinates. B:Witt-localization-witness supplies a correct excluded tuple and full universal proof. The valid strict-localization assertion and corrected infinite Greenberg theorem remain intact. The source-specific note and147-check certificate are retained.",'', 'Detailed A567 and PartC corrections retain every additional source file and line locator in the appended reports. The B source ledger records tau, alb., morcelés, artinien and SGA1962 original-image readings.','','## Residual gates and attempts','','The following is the current full B gate audit; no item below is silently declared complete:','']
correction_position=next(i for i,line in enumerate(lines) if line.startswith('Detailed A567 and PartC corrections'))
lines[correction_position:correction_position]=[
 '8. `PROMPT(20261119-143949).md`, line111, R13; original cote68, scan056: the finite-free determinant and free-complement invariance clause is verified in '+ids('C:graded-determinant-sign')+'. This prototype does not contain all bounded-complex/perfect-complex, true-triangle and derived-pullback coherence data of the later Knudsen–Mumford definitions. No new check of the separate orientation/Stokes clauses is claimed by this event.',
 '',
 '9. Knudsen–Mumford1976, printed pp.20,46,52: the printed sum exponent, unrestricted classical base-change assertion and scalar/trace-zero splitting require the explicit corrections proved in '+ids('C:graded-determinant-sign,C:determinant-ordinary-basechange,C:determinant-basechange-repair,C:determinant-trace-splitting,C:determinant-incidence')+'. The exact finite certificates report90,35 and22 passing assertions at their stated scopes. The determinant construction and its qualified applications are not refuted by these ancillary defects; the paper proves the valid replacement statements.',
 '',
]
gate=root/'notes/B_gate_audit.md'
if final_status:
 legacy_intro='The following is the current full B gate audit; no item below is silently declared complete:'
 assert lines.count(legacy_intro)==1
 lines[lines.index(legacy_intro)]='The following earlier B gate audit is preserved as dated history. The final outcome table, canonical register and stopping-review assessment state the current results and remaining obligations:'
 lines += ['The research phase stopped under the required review rule at '+final_status['research_stopped_utc']+'. Exactly two direct original-source derivations remain, grouped in the one numbered Open question `U:henselian-comparison`. Their exact scopes and the two actual review times are recorded in `logs/final_status.json` and the linked final assessment. The following earlier gate-audit entries are preserved dated history; the current outcome table and canonical register govern the final state.','']
if gate.exists():lines += [gate.read_text()]
lines += ['','## Component proof, source and correction records','']
for name in ['notes/A567_progress.md','notes/A567_sources.md','notes/C_report.md']:
 p=root/name
 if p.exists(): lines+=['### '+name,'',p.read_text(),'']
event_count=sum(1 for _ in csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
access_path=root/'SOURCE_ACCESS_EVENTS.tsv'
access_count=sum(1 for _ in csv.DictReader(access_path.open(),delimiter='\t')) if access_path.exists() else 0
lines += ['## Register and checkpoint integrity','',
 f'The canonical result register has {len(rows)} rows, one per numbered statement actually included by the master TeX source. Component IDs remain aliases in its notes and the event log. The current mathematical check register has {event_count} events using the exact requested categories; {access_count} retrieval-only events are preserved verbatim in `SOURCE_ACCESS_EVENTS.tsv`. Their relocation does not delete an event or turn an unavailable source into a mathematical check. The original pre-normalization register, complete mapping, corrected refinement pointers and conservation checks are retained in the A567 normalization records. An administrative inventory check is never represented as a mathematical proof. Earlier immutable checkpoint ZIPs are not nested in later ZIPs.']
if final_status:
 lines += ['', 'The latest preserved checkpoint at the research stop was `'+str(final_status['latest_checkpoint'])+'`. The separate final archive is named `'+final_status['final_archive_name']+'`; its actual content inventory and validation accompany the final packaging record. Earlier checkpoint archives remain unchanged. The final save receipt necessarily follows archive creation and is not represented as a self-contained hash of its own archive.']
(root/'RESEARCH_SA22_report.md').write_text('\n'.join(lines)+'\n')
(root/'logs/report_inventory.json').write_text(json.dumps({'updated_utc':now.isoformat(),'outcome_rows':len(outcomes),'missing_outcome_labels':sorted(unknown),'final_mode':bool(final_status),'numbered_statements':len(rows),'canonical_check_events':event_count,'source_access_events':access_count},indent=2))
print(json.dumps({'outcome_rows':len(outcomes),'missing_outcome_labels':sorted(unknown)},indent=2))
