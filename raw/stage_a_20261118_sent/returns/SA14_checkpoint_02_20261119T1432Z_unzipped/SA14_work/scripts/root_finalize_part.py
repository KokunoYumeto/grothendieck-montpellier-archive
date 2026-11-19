#!/usr/bin/env python3
"""Attach provenance/events to manually researched records and explicit link decisions."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];P=W/'parts/root'
claims=json.loads((P/'claims.json').read_text())
items=[]
# Exact semantic joins decided by reading both passages; no heading matching.
existing={608:'SA14-203',634:'SA14-333',642:'SA14-330',652:'SA14-651'}
conjectures={604,605,606,609,614,615,616,626,627,641,653,657,660,663,665,666,670,671,674,676,677,681,682,685,686,687}
withdrawn={610,613,633,648}
reused={636,637,638,643,645,654,675}
for c in claims:
    n=int(c['id'].rsplit('-',1)[1]); iid=existing.get(n,f'SA14-{n}')
    c['items']=[iid]
    if n in existing:continue
    kind='conjecture' if n in conjectures else 'withdrawn in the same text' if n in withdrawn else 'other' if n in reused else 'unproved claim'
    files=sorted({x['file'] for x in c['lines']})
    sources=['transcript:'+f.removeprefix('sources/') for f in files]
    for f in files:
        stem=Path(f).stem.replace('_transcription','')
        note=W.parent/'sources/SA14_notes/codex'/f'{stem}_notes.md'
        if note.exists():sources.append('codex-lead:'+str(note.relative_to(W.parent/'sources')))
    items.append({'id':iid,'sources':sources,'kind':kind,'cote':c['cote'],'scans':c['scans'],'lines':c['lines'],'his_words':c['his_statement'],'statement':c['statement'],'reconstruction':'Source-only addition from the fully read Codex transcription. Modern hypotheses, interpretations and corrections are explicitly distinguished in '+c['id']+'. No indexed Pro entry is assigned a verdict by this serialization.','check':'agrees','check_reason':'The quoted diplomatic passage and its context were read. This is documentary concordance; the mathematical qualification, refutation or literature limit is recorded separately in '+c['id']+'.','claims':[c['id']]})
(P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')

links=[]
def L(kind,a,b,what,evidence,notes=''):
    links.append(dict(kind=kind,**{'from':a,'to':b},what=what,evidence=evidence,note_ids=notes))
L('folder','57:3–13; A57-01','57:185–194; K57-05/06','Resolution quotient and cone/completion comparison','Both transcripts read. The exceptional lattice and formal Picard layers recur in the cone example; this is a checked mathematical comparison, not a claim of an explicit author citation.')
L('folder','57:3–13; A57-01','57:268,270; MPL_57_226-270','Resolution method in local Picard comparison','Both endpoints read. The analytic proof again quotients the resolved Picard group by exceptional codimension-one components.','MPL_57_226-270#60')
L('folder','57:194; K57-06','57:230–231; MPL_57_226-270','Henselian punctured completion question','The Codex cone discussion and the Hironaka letter both ask the henselian comparison; differing ideal/open hypotheses are retained in C626/C097.')
L('folder','57:194; K57-06','57:272; MPL_57_271-315','Repeated henselian punctured Picard problem','Both endpoints read and joined at the problem level; finite-order approximation and arbitrary opens are separate questions.')
L('folder','57:15–19; K57-01','57:283–287; MPL_57_271-315','Product Picard splitting and correspondences','The normalized product formula is compared with the equivariant abelian-factor calculation. The latter needs a component qualifier.')
L('folder','57:23,32; A57-02/K57-01','57:313; MPL_57_271-315','Correspondence separatedness versus representability','The letter asks general separatedness; the later question list records Raynaud for an integral-fibre assertion. These are not silently equated.')
L('folder','57:60–63; K57-03','59:20–25; K59-02','Relative Albanese from an abelian Picard subfunctor','Both constructions read; the chosen abelian subfunctor and the maximal universal recipient are distinguished.')
L('folder','57:64; K57-03','57:309–311; MPL_57_271-315','Smoothness, conormal module, and Picard flatness questions','Both endpoints read. The general characteristic-zero group criterion C686 differs from full-Picard flatness and from wild Pic^tau assertions.')
L('folder','57:71–72; K57-04','57:314; MPL_57_271-315','Numerical criteria and the tau-trivial locus','The later proof calls numbered criteria; the earlier finiteness sheet supplies overlapping numerical/NS bounds, but missing external criterion(ii) is not invented.')
L('folder','57:73–75; A57-02 typed letter','57:76–79; A57-02 handwritten duplicate','Duplicate Murre letter on proper Picard pullback and flattening','Both versions read. Contravariance and the correction to the smooth birational counterexample request were compared; the variants remain source witnesses.')
L('folder','57:116–120; MPL_57_089-132','57:169–171; K57-10','Regularity of functions and the affine-target condition','Both passages read. Different extension criteria share the need to distinguish affine and proper targets; the counterexamples are not conflated.')
L('folder','57:147,151,153; K57-08/09','58:66; MPL_58_020-067','Normalization defects, arithmetic genus and Picard affine part','Both actual formulas checked and joined in C642, with nodal specialization distinguished from general singularities.')
L('folder','57:220–221; K57-07','58:65,67; MPL_58_020-067','Projective cone, affine cone and line-bundle total space','Both endpoints read. The scheme types are kept distinct; EGAII8.7–8.8 is explicitly cited on58:67.')
L('folder','57:158–162; K57-09','57:126–129; MPL_57_089-132','Rigidification in moduli and in descent','Both endpoints checked. Projective frames and normalized isomorphism descent solve different automorphism problems; no proof of one is claimed from the other.')
L('folder','59:1–20; K59-01/02','60:3,7,11,17; MPL_60_002-035','Determinants of perfect complexes and Frobenius determinants','Both endpoints read. The relation is an editorial comparison of determinant formalism; no functional equation is inferred without duality and Frobenius hypotheses.')
L('published work','57:3–13; C601–606','R_Lipman1976, introduction/Th1.2/§5/Th7.5','Local-Artin Picard question and descent obstruction','Primary article directly credits Grothendieck’s September1969 letter and gives the relevant construction. Date applies to the identified letter, not the whole folder.')
L('published work','57:194,230–231,272; C626','R_Elkik1973, III.1 Th3,p569; corollariespp573–574','Henselian punctured comparison','Primary theorem/corollary checked; actual Picard isomorphism classes, not an equivalence of all Hom groupoids.')
L('published work','57:23,32; C674','R_Murre1966, §3(C)Th4','Representability of Corr with a separatedness hypothesis','Primary statement read: separatedness is an assumption and the general question is recorded as a problem. This is a limitation link.')
L('published work','57:20; C679','R_Murre1966, §3(A)Cor2','Flat kernel-pair quotient','The quotient factorization and finite-type/local-finite-presentation hypotheses were checked in both statements.')
L('published work','57:20; C680','R_SGA3XVII, AppIII C2.1,C3.1','Raynaud DVR affineness and quotient theorem','Primary text checked; flatness and separation must not disappear from the stated theorem.')
L('published work','57:45–49; C612','R_SGA3XI, §6 Prop6.1,Th6.2,Rem6.3','Finite-level density and transporter mechanism','Primary text opened; closedness/separation and prime-to-characteristic conditions remain explicit.')
L('published work','57:64; C686','R_SGA3VIB, Prop1.6,p327(original)','Conormal local freeness implies smoothness in characteristic zero','Exact primary proposition checked; local finite presentation along the unit is included.')
L('published work','57:68–72; C618–619','R_SGA6, XIII Th3.6,4.7,5.1–5.4','Finiteness, numerical equivalence and Betti correction','Full primary PDF read at exact printedpages635,647–652. Remark5.3 confirms b1=2dimPic and the surface Euler formula.')
L('published work','57:73–79; C620','R_SGA6, XII Th1.1,Cor1.5,Rem1.7,pp596–598','Proper-surjective pullback','Primary exact quantifiers checked: generic relative quasi-affineness and field affineness are distinct.')
L('published work','57:75,79; C621','R_StacksFlattening, tag05PS Lemma38.27.6','Universal flattening','Proper finite-presentation and finitely presented sheaf hypotheses checked; the functor is represented by a finite-presentation monomorphism under them.')
L('published work','57:148,150,152,156; C643','R_Kodaira1960, §3 Th3.1; CollectedIII article52','Identify the reused English surface proof','Actual article in publisher preview compared; theorem removes the earlier Kähler restriction. Physical edition of reused leaf not uniquely identified.')
L('published work','57:154,159,161,163; C645','R_EGAI, I6.4.12,6.5.1;0.7.5–7.6','Identify reused EGA leaves','Primary original PDF read at exact numbered statements; handwritten generator criticism remains separately checked.')
L('published work','58:3–17; C651–652','R_SGA2, XIII Th2.1 and following converse','Connectedness induction and sharp converse','Exact component bounds, connectedness quantifiers and irreducible dimension0/1 exclusions compared; reversed manuscript inequality remains an ink question.')
L('published work','58:19; C653','R_SGA2, XIII3.1; R_Suzuki2023,Th1.2','Full local fundamental-group conjecture and pro-nilpotent progress','Both primary texts opened; no passage from pro-nilpotent finite generation to full profinite finite generation is asserted.')
L('published work','59:1–5,15–20; C655–658,668','R_KnudsenMumford1976,Th1,pp24–25','Determinant of a perfect complex','Primary pages visually checked. Independent RR and basepoint calculations in root_proofs preserve determinant conventions.')
L('published work','59:10–11; C661–662','R_Beauville1986,Prop1,p648; R_Mukai1981,Th2.2','Fourier grading and square','Primary formulas checked. Cohomological sign model is not a proof of ungraded Chow codimension reversal.')
L('published work','59:20; C669','R_Mukai1981,§3 equation(3.1)','Tensor/translation identity','Primary direction checked: Φ(L⊗P_β)=t_β*Φ(L), hence the determinant Picard-class difference is +h_M(β) when h_M is defined by that pullback. A manuscript minus requires tilde=−h_M or the opposite kernel convention.')
L('published work','59:26–28; C672–673','R_Alexeev2002,§3.0.5–3.0.11','Principal theta pairs and canonical doubled class','Primary construction compared, including evaluation at zero. Arbitrary polarization-type results remain separate.')
L('published work','59:10; C660','R_Schroer2003,Th5.1; R_FringuelliPirisi2019','Franchetta questions with exact moduli hypotheses','Primary texts opened: g≥3 curve theorem and g≥4 complex abelian level theorem. Marked genus1 counterexample is retained.')
with (P/'links.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(links)

who='GPT-6 Astra Pro; effort not exposed; SA14-20261119; root'
events=[]
def E(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for i in items:E(i['id'],'used and rechecked in this run','Text concordance, not mathematical proof. '+i['check_reason'])
refuted={611,617,619,635,638,649,650,660,663,664,665,667,668,680}
reproved={601,602,603,607,608,610,612,613,625,630,632,637,639,642,644,646,647,648,655,656,658,662,664,668,675,683}
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    E(c['id'],'used and rechecked in this run','Diplomatic text and context checked; status='+c['status_on_pages']+'. Literature comparison: '+c['fate']+' Search receipts: '+', '.join(c.get('searches',[])))
    if n in refuted:
        c['refined_statement_id']=c['id']+'-R';c['refined_statement']=c['statement']
        E(c['id'],"refuted, with refined statement's id",'Literal/overbroad reading refuted; corrected formulation '+c['refined_statement_id']+' is stored in the same record. '+c['computation'])
    elif n in reproved:E(c['id'],'independent re-proof',c['computation']+' Detailed limits and proof: research/root_proofs.md.')
    else:E(c['id'],'targeted proof check','Theorem hypotheses or obstruction/formulation checked; not a full independent proof of external theorems. '+c['computation'])
checks={607:['cube_recurrence','cube_small_exponents','multiplication_binomial'],611:['noncommutative_power_counterexample'],617:['matsusaka_threshold_counterexample'],619:['abelian_surface_betti'],625:['plane_cone_completion_layers'],635:['triple_line_cech_failure','plane_cubic_hilbert_polynomial','triple_lines_flatness'],632:['conic_regular_chart','conic_vertical_intersections'],642:['normalization_picard_dimensions'],644:['stable_graph_moduli_dimension'],637:['koszul_homotopy'],658:['fourier_grr_sign'],662:['double_phi_parity'],663:['dual_polarization_primitive_counterexample'],665:['even_chi_not_twodivisible'],668:['perfect_complex_curve_rr'],664:['torsor_annihilator_gcd'],660:['universal_pointed_genus_one_counterexample'],649:['R1_without_S2_counterexample'],638:['CM_not_maximal_CM']}
for n,names in checks.items():E(f'C-SA14-{n:03d}','computation or formal certificate','Exact symbolic calculation or stated finite model in scripts/root_computations.py; outputs/root_computations.json records '+', '.join(names)+'. These are not formal geometric certificates; proofs and hypotheses are in research/root_proofs.md.')
for r in json.loads((P/'reference_details.json').read_text()):
    E(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',r['annote']+' URL: '+r['url']+'; note='+r['note']+'.')
for n in (657,669):
    E(f'C-SA14-{n:03d}','targeted proof check','Independent cross-review by lfunctions, followed by root correction: with h_M(β)=t_β*M⊗M^{-1} and the positive Poincaré kernel, the Picard-class difference is +h_M(β). The earlier modern reconstruction introduced an unjustified second minus from movement of divisor support. Corrected convention dictionary and conditional three-torsor formula are in root_proofs.md §8 and parts/lfunctions/cross_review_root_655_673.md. No source transcription changed.')
with (P/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
(P/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
(P/'item_joins.json').write_text(json.dumps({f'C-SA14-{n:03d}':i for n,i in existing.items()},indent=2)+'\n')
print(json.dumps({'root_items':len(items),'root_claims':len(claims),'checked_links':len(links),'events':len(events),'explicit_existing_item_joins':existing},indent=2))
