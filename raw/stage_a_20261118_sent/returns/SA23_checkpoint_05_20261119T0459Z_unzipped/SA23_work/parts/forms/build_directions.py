import json
from pathlib import Path
P=Path(__file__).parent
D=[]
def a(rank,title,interest,feasible,items,claims,problems,known,residual,step):
 D.append({'rank':rank,'title':title,'interest':interest,'feasible_progress_in_one_run':feasible,'items':items.split(';'),'claims':claims.split(';'),'problems':problems.split(';'),'known':known,'residual':residual,'first_step':step})
a(1,'Recover the precise flat-conormal theorem attributed to Quillen',5,3,'SA23-885;SA23-890','C-SA23-forms-069;C-SA23-forms-074','MP-SA23-forms-61','Finite-projective Lie–Rinehart/PBW and formally smooth infinitesimal-groupoid correspondences are established.','The adic category with merely flat conormal, duality topology and cohomology comparison have not been matched exactly.','Set up an affine Q-algebra test with a flat nonprojective module, and trace Quillen bibliographies/correspondence for the exact1968 theorem before attempting a proof.')
a(2,'Produce a diplomatic concordance of the quadratic correction',5,5,'SA23-819;SA23-825','C-SA23-forms-020;C-SA23-forms-026','MP-SA23-forms-18;MP-SA23-forms-23','SGA7XVII3.3 and2.5 distinguish nondegenerate conormal behavior from ordinary Lefschetz singularities.','The translation and corrected cote25 witnesses preserve different adjectives, not one silently repaired statement.','Align cote24scan48 with cote25scans139–141 and158–160, then make a rank/characteristic table using the exact quadratic forms and Hessians.')
a(3,'Identify the finite-etale multisection counterexample',4,3,'SA23-813','C-SA23-forms-014','MP-SA23-forms-11','The projective hyperplane construction is established; both typed witnesses explicitly contrast proper nonprojective families.','The intended concrete smooth proper nonprojective counterexample and cancellation extent are not identified.','Follow EGA quasi-section and proper nonprojective family references backwards, keeping finite-etale over a Zariski neighborhood distinct from an arbitrary etale neighborhood.')
a(4,'Separate coefficient detection from derived-local-system equivalence',5,5,'SA23-843;SA23-844','C-SA23-forms-037;C-SA23-forms-038;C-SA23-forms-080','MP-SA23-forms-32;MP-SA23-forms-33','The fixed-Q converse fails on Moore spaces; constant abelian cohomology alone fails on an acyclic noncontractible complex.','The strongest topos theorem requires an exact coefficient-category and local Ext hypothesis.','Write the integral criterion and its R-local variant side by side; prove full faithfulness and essential surjectivity by bounded Postnikov induction under explicit local Ext assumptions.')
a(5,'Clarify the three bordism splitting questions',4,5,'SA23-854;SA23-855;SA23-858','C-SA23-forms-048;C-SA23-forms-049;C-SA23-forms-052','MP-SA23-forms-40;MP-SA23-forms-41;MP-SA23-forms-43','Additive and homotopy-ring sections exist; E-infinity and all-Gysin compatible versions fail; the written submanifold/Sq criterion is false.','A useful restricted Gysin class or intended normal-framing convention has not been specified.','Make the RP2 and superimposed normal-bundle examples the first tests, then inspect the two typed margins before formulating a restricted universal property.')
a(6,'Repair the depth and fixed-base exceptional-locus criteria',4,4,'SA23-817;SA23-822;SA23-823;SA23-824;SA23-833;SA23-835','C-SA23-forms-018;C-SA23-forms-023;C-SA23-forms-024;C-SA23-forms-025;C-SA23-forms-082;C-SA23-forms-084','MP-SA23-forms-20;MP-SA23-forms-22;MP-SA23-forms-64;MP-SA23-forms-66','Benoist and Poonen–Slavov give exact modern depth/equidimensionality bounds; the fixed-divisor blowup obstruction is elementary.','Damaged codepth strata and weaker morphism hypotheses prevent identification of the full manuscript iff statements.','State each legible implication separately and test necessity on depth2 threefold points, tangent quadric sections and blowups before reconstructing any missing criterion.')
a(7,'Write an annotated history of the specific etale Adams proof',4,5,'SA23-864;SA23-867;SA23-868','C-SA23-forms-058;C-SA23-forms-061;C-SA23-forms-062','MP-SA23-forms-47;MP-SA23-forms-49','The attached proof matches Quillen1968; Friedlander1973Thm5.3 and6.8 complete its complex route; Quillen1971 is different.','The broader proSF representability conjecture is not settled simply by the Adams theorem.','Build a numbered conjecture-to-theorem concordance with exact completion-prime, rank and fundamental-group hypotheses; establish first-circulation dates only from dated primary evidence.')
a(8,'Reconstruct higher abelian mapping groupoids',4,4,'SA23-847;SA23-848;SA23-850','C-SA23-forms-041;C-SA23-forms-042;C-SA23-forms-044','MP-SA23-forms-35;MP-SA23-forms-36;MP-SA23-forms-38','Strict abelian n-categories yield chain complexes after globularity; general Picard groupoids retain a self-commutor; K-theory needs exact/enhanced data.','The manuscript does not specify weak higher morphisms or the mapping-object truncation.','Work out n=2 with explicit complexes and a nonzero Ext1 example, then compare the chosen weak-morphism model with truncated RHom and the Picard epsilon invariant.')
a(9,'Give a minimal correction sheet for the formal de Rham notes',3,5,'SA23-882;SA23-883;SA23-889','C-SA23-forms-066;C-SA23-forms-067;C-SA23-forms-073','MP-SA23-forms-54;MP-SA23-forms-55','The rank3 exterior differential and rank1 curved connection give exact counterexamples.','Only the ink can determine whether the missing conditions are transcription losses or manuscript gaps.','Prepare a future scan checklist containing the two counterexamples and the degree/sign constraints, without changing the source text.')
for d in D:
 d['id']=f"D-SA23-forms-{d['rank']:02d}"
 d['record_type']='ranked direction from authorial problem'
 d['editorial_tasks']=[]
# Keep the former direction identifier for the accepted global consolidation;
# it is now an editorial component of hyp03, not a new authorial problem.
E=[D[2]];E[0]['former_rank']=E[0].pop('rank');E[0]['problems']=[]
E[0]['editorial_tasks']=['ED-SA23-forms-11']
E[0]['record_type']='editorial follow-up outside Stage6'
E[0]['reason_outside_stage6']='The source asserts that counterexamples exist; it does not ask for a construction or defer that proof.'
D=[d for d in D if d['id']!='D-SA23-forms-03']
for d in D:
 if d['id']=='D-SA23-forms-06':
  d['problems']=['MP-SA23-forms-20','MP-SA23-forms-22','MP-SA23-forms-64']
  d['editorial_tasks']=['ED-SA23-forms-66']
  d['residual']='The actual source questions concern R_k necessity, fixed-base sections and the wider morphism bound; the normalization assertion and damaged adjective are editorial dependencies.'
(P/'directions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
(P/'editorial_directions.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
s=['# Ranked directions: cotes24 and162-5','', 'Scores run from1(low) to5(high). These are tasks for a later run; none is developed beyond the checks already in the dossier.','']
for d in D:
 s += [f"## {d['rank']}. {d['title']}",'',f"Interest {d['interest']}/5; progress feasible in one run {d['feasible_progress_in_one_run']}/5.",'','Sources: '+', '.join(d['items']+d['claims']+d['problems'])+'.','',d['known']+' '+d['residual'],'','First step: '+d['first_step'],'']
 if d['editorial_tasks']:s+=['Editorial dependencies: '+', '.join(d['editorial_tasks'])+'.','']
s+=['## Editorial follow-up outside Stage6','']
for d in E:
 s += ['### '+d['title'],'','Stable direction identifier: '+d['id']+'.',
       'Sources: '+', '.join(d['items']+d['claims']+d['editorial_tasks'])+'.','',
       d['reason_outside_stage6'],'',d['known']+' '+d['residual'],'',
       'First step: '+d['first_step'],'']
(P/'directions.md').write_text('\n'.join(s)+'\n')
print(len(D),'ranked directions and',len(E),'editorial direction saved')
