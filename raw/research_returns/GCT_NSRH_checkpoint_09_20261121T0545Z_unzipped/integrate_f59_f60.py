"""Integrate reviewed purity/source refinements and F59/F60 once."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

r = Path(__file__).resolve().parent
targets = {
 'finding_F57_pure_complex.tex':'f325c80aeb83cf64fdcb83da05e559d257481b816e39db7041d4af1044c20155',
 'finding_F57_F58_source_gate.tex':'f4ded9c74a63a1eda1dd0e20cc4011588d93bbd540ee890139afecbf5a3482cc',
 'finding_F59.tex':'0bc2b46346e1dc1cdb8680ff0462bbf41e199bd344c87945742c9428a80153ae',
 'finding_F59_frobenius.tex':'8c5944021f382e24c6d4c4a62f65708b441c1b759bf82829f9748b26cc999303',
 'finding_F60.tex':'30461c370c3282c33033e0304d7f5e139d79425a9d738fae154aaa7adfc42c6f',
}
parts = {}
for name, sha in targets.items():
    p=r/name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==sha, name
    parts[name]=p.read_text().split('% Separate paragraph for Part III.',1)
p=r/'GCT_NSRH.tex'; s=p.read_text()
assert r'\label{f:boundedkernelcharactergate}' not in s
needle=r'\subsection{Strict Laurent positivity and the source\'s changing cells}'.replace("\\'", "'")
assert s.count(needle)==1
s=s.replace(needle,parts['finding_F57_pure_complex.tex'][0].rstrip()+'\n\n'+needle)
needle=r'\subsection{A normalization that cannot be a finite Frobenius trace}'
assert s.count(needle)==1
core=parts['finding_F59.tex'][0]
old='The remaining problem is descent of a coupled finite\ngraded complex with the actual quadratic isomorphism,\nfollowed by coherent higher nonstandard relation maps.'
new='At this stage the test leaves descent of a coupled finite\ngraded complex with the actual quadratic isomorphism unresolved.\nThe following finite-fiber strengthening closes that remaining\ncase in every ordinary type-A rank, before any higher\nnonstandard relation maps need to be considered.'
assert old in core; core=core.replace(old,new)
addition='\n\n'.join([parts['finding_F57_F58_source_gate.tex'][0].rstrip(),core.rstrip(),parts['finding_F59_frobenius.tex'][0].rstrip(),parts['finding_F60.tex'][0].rstrip()])
s=s.replace(needle,addition+'\n\n'+needle)
needle=r'\section{Archival audit and the Fable leads}\label{sec:archive}'
assert s.count(needle)==1
dictionary='\n\n'.join(parts[name][1].strip() for name in targets)
s=s.replace(needle,dictionary+'\n\n'+needle)
assert r'\bibitem{EWLocalized}' not in s
s=s.replace(r'\end{thebibliography}',(r/'finding_F59_bib.tex').read_text().strip()+'\n'+r'\end{thebibliography}')
s=s.replace('findings A01 and F01--F58,','findings A01 and F01--F60,')
old='A signed or derived action comparison, a source-prescribed higher categorical presentation and designated simple/global labels remain.'
new='The pure-point refinement also excludes a single pure derived trace for the actual rank-four word or the disappearing cell coefficient under the specified weight-one variable. F59 excludes every bounded ordinary type-A Soergel lift of the actual generator with its cohomologically degree-zero quadratic coefficient. F60 excludes bounded finite-state complex kernels if full cohomology retains the actual finite algebra relations with degree-zero scalar grading objects; even one specified rank-one module relation cannot lift in the displayed isomorphism form. These results still permit triangle-only relations, nontrivial coefficient complexes, and geometric convolution without a matrix-cohomology character functor. The source itself allows signed vanishing factors: no strict named-generator effectivity or pure raw point-coefficient axiom may be substituted for VIII Conjecture 3.4. A compatible realization of those signed/factored operations, a source-prescribed higher categorical presentation and designated simple/global labels remain.'
assert old in s; s=s.replace(old,new)
p.write_text(s)

q=r/'QUESTIONS.tsv'
with q.open(newline='') as f:
    rd=csv.DictReader(f,delimiter='\t'); fields=rd.fieldnames; rows=list(rd)
for x in rows:
    if x['id']=='Q1':
        x['current_gate']+=' The exact source audit distinguishes VIII signed/factored normalized positivity from an unasserted unsigned action axiom for named right generators.'
    if x['id']=='Q3-GCT':
        x['finding_ids']+=',F59,F60'
        x['current_gate']='Actual fixed-parameter pure perverse End/Hom, coherent all-degree tensor maps, opposite-sign paths and rank-three graded relation kernels with bar exist. Independent local/dual bounds and designated simple/global bases remain. F57/F58 exclude strict named-generator effectivity on the full rank-four extra simple and in the two-row source-cell basis; F57 also excludes pure raw point-complex traces under the specified weight convention. F59 excludes all bounded ordinary type-A Soergel lifts with the actual ambient class and degree-zero quadratic coefficient. F60 excludes bounded finite-state complex kernels retaining the full actual algebra on cohomology with degree-zero scalar coefficients. The remaining signed/factored route must supply actual relation triangles or nontrivial coefficient complexes, or geometric convolution without that character functor, together with the exact source basis and specialization comparison. VIII does not assert the stronger unsigned named-generator premises.'
        x['approaches_tried']+='; exact pure-complex sign criterion; source generator/basis audit; bounded ordinary-Hecke localization and coinvariant Frobenius fiber; full-cohomology finite-algebra character; actual rank-one word relation'
        x['next_step']='Construct actual signed/factored geometric operations or test nontrivial scalar coefficient complexes; identify designated canonical labels and prove independent varying-coefficient weight bounds.'
    if x['id']=='Q3-RANK4-EFFECTIVE-SIMPLE':
        x['finding_ids']='F57,F60'
        x['current_gate']+=' The exact pure-point criterion (-1)^w f(-v) effective excludes a bounded complex of any single weight, not just one parity. F60 also excludes a bounded-kernel repair preserving full actual relations on cohomology with degree-zero scalar coefficients. Mixed nonproper pushforwards and triangle-only relations remain distinct.'
        x['next_step']='Construct a mixed/nonproper signed action with actual maps, or specify a different canonical operator comparison; the source does not assert unsigned effectivity for all named generators.'
    if x['id']=='Q3-CELL-POSITIVITY':
        x['current_gate']+=' The coefficient c0 has an explicit mixed compact realization on Gm²; it cannot be a single-pure-weight point Euler trace under v=q^(n/2). The pure coefficient sheaf before pushforward remains possible.'
    if x['id']=='Q6': x['current_gate']=x['current_gate'].replace('F01–F58','F01–F60')
newrows=[
 ['Q3-PURE-POINT-COMPLEX','F57 refinement; BBD5.1.5/5.1.8/5.1.11/5.1.13–14; Milne18.4b/22.1/22.3b/24.1','Can bounded pure complexes repair the actual negative trace and disappearing cell coefficient?','EXACT_CRITERION_PROVED; SPECIFIED_PURE_POINT_COMPARISONS_REFUTED','F57','For an integral Laurent f under v=q^(n/2), a bounded pure point complex of weightw exists exactly when (-1)^w f(-v) is effective. The actual word and c0 fail for everyw. RΓc(Gm²,Ql(1)) realizes c0 as mixed point cohomology; its source coefficient is pure. State-potential pure kernels would give pure closed words and are excluded on the specified extra simple.','Finite Vandermonde; unique cohomology degree at each weight; continuous Weil lines; torus localization/Kunneth; telescoping state potentials','Construct the intended nonproper operation and actual relation maps, or separate normalized positive factors from raw mixed coefficients.'],
 ['Q3-BOUNDED-ORDINARY-HECKE','F59; EW§§3.3–3.5/6.4; EWLocalized§1.1/Thm1.6/§2.1; Rouquier§3','Does an arbitrary bounded ordinary-Hecke lift of the actual generator satisfy its categorical quadratic?','REFUTED_FOR_ALL_BOUNDED_TYPE_A_LIFTS_WITH_THE_SPECIFIED_COEFFICIENT','F59','No bounded ordinary type-A Soergel complex with Eulerclass b⊗b+(b−δ)⊗(b−δ) satisfies X⊗X≃(1(2)⊕1²⊕1(-2))⊗X. Central coinvariant quotient, exact finite-Frobenius duality and minimality force left-free H0; codimension-two graph support then requires2a(v)=v²+2+v^-². Arbitrary bounded differentials are covered.','Generic amplitude; arbitrary direct-sum cones; coupled Rouquier test; central quotient; all-type-A Artin/Frobenius basis; lower amplitude duality; graded minimality; graph splitting','Test a cohomologically nontrivial scalar coefficient complex, a localization changing the finite fiber, or a different geometric category with an explicit original-action comparison.'],
 ['Q3-BOUNDED-KERNEL-RELATIONS','F60; IV Prop11.8 p61 and §11.8 p67; actual F57 word','Can bounded finite-state complexes retain the actual finite-algebra relations and negative Euler word trace?','REFUTED_UNDER_FULL_COHOMOLOGY_RELATIONS; SINGLE_WORD_ISOMORPHISM_ALSO_REFUTED','F60','Any finite-dimensional constant algebra representation over F[z±] has constant character. Full cohomology kernels factoring through the actual algebra with scalar parameter fixed therefore have nonnegative word traces, contradicting N#. Independently the rank-one word equation W²=πW cannot lift as K²⊕E_-K≃E_+K with degree-zero E±, since π(3)<0.','Constant annihilating polynomial; finite graded Kunneth; exact full-relation hypothesis; rank-one module annihilator; zero-reflecting positive evaluation','Use actual relation triangles or nontrivial coefficient complexes, or prove a geometric convolution comparison outside finite-state cohomology multiplication; smaller-rank presentation checks alone are insufficient.']
]
for row in newrows: rows.append(dict(zip(fields,row)))
assert len({x['id'] for x in rows})==len(rows)
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t'); w.writeheader(); w.writerows(rows)

now=datetime.now(timezone.utc).isoformat()
def sha(name): return hashlib.sha256((r/name).read_bytes()).hexdigest()
events=[
 ('F57-PURE-COMPLEX-FINAL','/root','targeted proof check','Read entire report and entire final fragment; independently reconstructed Vandermonde degree/sign test, converse, torus cohomology and state-potential corollary. Previously read exact BBD/Milne primary contexts. PASS.','agent_pure_point_complex_trace.md; finding_F57_pure_complex.tex'),
 ('F57-PURE-COMPLEX-FRESH','/root/grothendieck_dictionary','independent re-proof','Actual reviewer whole-proof reconstruction and full final fragment match including original Milne citation delta PASS.','agent_F57_pure_point_review.md'),
 ('F57-F58-SOURCE-GATE','/root','targeted proof check','Entire report and final fragment read, all new elementary arguments reconstructed; source assertions remain attributed to the precisely located original source audit. Strict stronger hypotheses are not substituted for published signed positivity. PASS.','agent_named_generator_positivity_gate.md; finding_F57_F58_source_gate.tex'),
 ('F57-F58-SOURCE-GATE-FRESH','/root/rectangular_and_theta','independent re-proof','Actual reviewer complete report and fragment reconstruction plus supplied primary source-context checks; final nonclosure and basis-mixing deltas PASS. Published full table not recomputed.','REVIEW_NAMED_GENERATOR_GATE_THETA.md'),
 ('F59-CORE-COMPLETE','/root','targeted proof check','Entire report and final fragment read and reconstructed, including arbitrary complementary cones, generic support and coupled Rouquier graded failure; PASS. Integration changes only the residual-open transition to point to the checked strengthening.','agent_soergel_derived_gate.md; finding_F59.tex'),
 ('F59-CORE-FRESH','/root/rectangular_and_theta','independent re-proof','Actual reviewer full mathematical reconstruction, primary-source contexts and whole fragment match PASS.','REVIEW_SOERGEL_DERIVED_THETA.md'),
 ('F59-FINITE-FIBER-COMPLETE','/root','targeted proof check','Read and independently reconstructed entire final report and all369 fragment lines: central generators/IM=MI; actual quotient homotopy relation; nonzero Euler fiber; top and dual bottom amplitude; self-injective finite projective dimension; left-only minimality; all-type-A triangular monic Frobenius proof; derived graph splitting and integral contradiction. PASS.','agent_soergel_frobenius_closure.md; finding_F59_frobenius.tex'),
 ('F59-FINITE-FIBER-FRESH','/root/rectangular_and_theta','independent re-proof','Actual reviewer full proof reconstruction and whole final-fragment match PASS; exact scope and corrected graded functional hypotheses retained.','REVIEW_SOERGEL_FROBENIUS_THETA.md'),
 ('F60-COMPLETE','/root','targeted proof check','Author reread entire final report and fragment, reconstructing all arguments. Constant character needs no semisimplicity; optional module isomorphism does. Full relation hypothesis and separate module-annihilator isomorphism are explicit. PASS.','agent_bounded_kernel_character_gate.md; finding_F60.tex'),
 ('F60-FRESH','/root/rectangular_and_theta','independent re-proof','Actual reviewer complete report reconstruction, IV primary source checks and entire final fragment match PASS after semisimple-scope correction.','REVIEW_BOUNDED_KERNEL_CHARACTER_THETA.md'),
 ('CITED-EW-LOCALIZATION-ROUQUIER','/root/grothendieck_dictionary and /root/rectangular_and_theta','used and rechecked in this run','Both actual source reviewers read original ordinary-Soergel/localization/Rouquier contexts with exact locators; not an independent re-proof of the cited general theorems. Full details in core report and review.','agent_soergel_derived_gate.md; REVIEW_SOERGEL_DERIVED_THETA.md'),
]
with (r/'CHECK_EVENTS.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,who,typ,out,names in events:
        loc='; '.join(n+' SHA256 '+sha(n) for n in names.split('; '))
        w.writerow([sid,now,who,'GPT-6 Astra Pro','not exposed','GCT_NSRH_20261121',typ,out,loc])
with (r/'LEDGER.md').open('a') as f:
    f.write(f'\n## {now} — pure-complex/source refinements and F59/F60 integrated\n\nFull proofs and separate PartIII dictionaries are integrated after complete root and independent checks. The raw actual trace and disappearing coefficient fail the exact pure-point sign rule; the torus example shows the distinct nonproper mixed alternative. VIII’s signed/factored constants are explicitly distinguished from strict named-generator effectivity. F59 now closes every bounded ordinary type-A Soergel lift with the actual ambient class and degree-zero quadratic coefficient, not only direct-sum candidates. F60 closes full-cohomology finite-state relation lifts and one explicit module-word isomorphism. Remaining routes are actual relation triangles, nontrivial scalar coefficient complexes, or geometric convolution outside the finite-state cohomology character, with designated basis and independent weight estimates. These refinements postdate review03 and were not counted there. The PDF is pending rebuild.\n')
with (r/'IMPLICATIONS.md').open('a') as f:
    f.write('\n## Pure complexes and the bounded derived alternatives\n\nA bounded pure point complex imposes cohomological parity on every visible Laurent coefficient: under v=q^(n/2), weightw requires (-1)^w f(-v) to be effective. The actual rank-four word and c0 fail this exact criterion. Pure source coefficients remain possible on nonproper geometry: the explicit compact pushforward of Ql(1) on Gm² has Euler trace c0 and mixed cohomology. This distinction uses BBD5.1.8 and proper-pushforward weight bounds, with Milne18.4b/22.1/22.3b/24.1 fixing the torus calculation.\n\nVIII Conjecture3.4 itself allows signed vanishing factors, and its printed rank-three table includes a negative raw constant. The class of such factored coefficients is not closed under addition, so a negative word trace is not a refutation of that conjecture. The needed comparison must state which generators are effective and how the designated cells are realized.\n\nF59 rules out all bounded ordinary type-A Soergel lifts of the actual generator with the ordinary degree-zero coefficient forδ². An actual central coinvariant quotient and algebraic finite-Frobenius duality force a single free cohomology module; its codimension-two graph splitting requires half of a Laurent polynomial with odd extreme coefficients. F60 independently rules out bounded finite-state complex kernels whose full cohomology retains the actual finite-algebra relations with unchanged scalar grading. A single actual rank-one word relation also fails in its stated ordinary-isomorphism form. These are categorical comparison obstructions, not arithmetic RH counterexamples.\n\nThe remaining geometric route must supply relation triangles, a nontrivial coefficient complex, or a convolution without the finite-state cohomology character, and still identify the designated basis and independent weight bounds. The framework is EGAI1.3.7/1.3.8/1.4.1, SGA6I4.7–4.8, SGA3I4.7.2–3/cote90 scan17 and the coefficient K0 language of SGA6V2–3/cote133 scan18. None of these anchors is cited as containing the new obstructions, and no lambda-ring structure on the noncommutative algebra is claimed.\n')
readme=r/'README.md'; txt=readme.read_text().replace('integrates F01–F58','integrates F01–F60')
txt+='\nCurrent additions throughF60: exact pure-point trace criterion and mixed torus witness; source signed/factored positivity audit; all-bounded ordinary type-A Soergel quadratic obstruction; bounded finite-state full-cohomology relation obstruction and explicit one-word test. Complete proofs and separate dictionaries are integrated. The earlier PDF-status notes are historical; STATUS_TIME.txt records the current build state.\n'
readme.write_text(txt)
(r/'STATUS_TIME.txt').write_text('WORK IN PROGRESS\nSnapshot UTC: '+now+'\nTeX integrates F01–F60 with full reviewed proofs and separate dictionaries; PDF awaits this integration rebuild.\nReview03 at04:00:17UTC: movement yes, no-movement count0. Next review05:00UTC; checkpoint07 due04:15UTC.\nPending main gate: actual signed/factored geometry or nontrivial coefficient-complex relations, designated canonical labels and independent local/dual weight bounds. F61 pure rank-three derived kernels are in separate review.\n')
manifest_path=r/'EXTERNAL_INPUT_MANIFEST.json'
manifest=json.loads(manifest_path.read_text()); known={x.get('local_research_input') for x in manifest}
for stem in ['Elias_Williamson_Hodge_2014','Elias_Williamson_Localized_2022','Rouquier_Braid_2004']:
    for ext in ['pdf','txt']:
        src=r/'primary_sources'/f'{stem}.{ext}'
        if src.exists() and str(src.relative_to(r)) not in known:
            manifest.append({'local_research_input':str(src.relative_to(r)),'bytes':src.stat().st_size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'redistributed':False,'locator_reference':'F59; agent_soergel_derived_gate.md and REVIEW_SOERGEL_DERIVED_THETA.md; exact bibliography locators in GCT_NSRH.tex'})
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
print('Integrated throughF60; question rows',len(rows),'mainSHA256',sha('GCT_NSRH.tex'))
