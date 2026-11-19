"""Write final evidence/link/direction registers from explicit reviewed mappings."""
import json,csv,collections
from pathlib import Path
D=Path(__file__).resolve().parent
C=json.loads((D/'claims.json').read_text());B={int(c['id'].rsplit('-',1)[1]):c for c in C}
R=json.loads((D/'reference_details.json').read_text())
Q=json.loads((D/'search_queries.json').read_text())
log=[]
for q in Q:
 ids=[B[n]['id'] for n in q['claims']]
 refs=list(dict.fromkeys(k for n in q['claims'] for k in B[n]['refs']))
 for j,x in enumerate(q['queries'],1):
  log.append(dict(id=q['id']+'-'+str(j),date=q['date'],engine=q['engine'],query=x['q'],claims=ids,results=q['results'],opened_sources=[dict(key=k,url=R[k]['url'],locator=R[k]['locator'],matched=R[k]['scope']) for k in refs],limits='This is an exact final targeted query in addition to the earlier search trail. Results are discovery leads; only the separately opened primary sources and independent proofs establish the fate. A source grouped here need not have appeared in this one query. No negative novelty conclusion follows from missing hits.'))
for c in C:
 log.append(dict(id='AC-FATE-'+c['id'].rsplit('-',1)[1],date='2026-11-19',type='exact hypothesis match after search',claim=c['id'],query_ids=[q['id'] for q in Q if int(c['id'].rsplit('-',1)[1]) in q['claims']],opened_sources=[dict(key=k,url=R[k]['url'],locator=c['literature_locator']) for k in c['refs']],matched=c['fate'],not_matched=c.get('literal_fault','Published match is restricted to the hypotheses and locators stated; no blanket priority or manuscript-date claim.'),confidence=c['confidence']))
log.extend([
 dict(id='AC-ACCESS-ZBL',date='2026-11-19',query='site:zbmath.org "Grothendieck" "Réarrangements"',url='https://zbmath.org/?q=an%3A0161.33603',result='Numdam Zbl link opened; access returned403. Search did not furnish an independent exact review. Numdam metadata and the full primary paper were read instead.',claims=[B[n]['id'] for n in [21,22,23,24,44,48,57,68,73]]),
 dict(id='AC-ACCESS-MO',date='2026-11-19',query='site:mathoverflow.net "eigenvalues" "singular values" "dominate"',url='https://mathoverflow.net/questions/185412/do-singular-values-dominate-eigenvalues/185445',result='Search result identified the Weyl/Horn lead. No forum answer is used as the proof source; Tam2010 primary proof and the independent weighted cycles were checked.',claims=[B[34]['id'],B[83]['id']]),
 dict(id='AC-BIB-CSG',date='2026-11-19',query='Grothendieck published works Fredholm réarrangements produits tensoriels',url='https://csg.igrothendieck.org/published-works/',result='Opened bibliography: CSG14 Fredholm1956, CSG24 Bourbaki113, CSG12 Memoirs16. Followed exact primary works; bibliography alone does not settle theorem matching.',claims=[B[n]['id'] for n in [21,28,31,35,37,57,81,84]]),
 dict(id='AC-BIB-CIRCLE',date='2026-11-19',query='Grothendieck produits tensoriels topologiques espaces nucléaires memoirs16 1955 pdf',url='https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG-bibliotex.pdf',result='Opened published-work bibliography and followed Memoirs16 lead. The image-only published text was visually read at II pp.13,20–21. Front matter explicitly gives copyright1955 and fourth printing1966; chapterII physical page is printed+201.',claims=[B[37]['id'],B[81]['id']]),
 dict(id='AC-EGA-COMPARISON',date='2026-11-19',query='Exact published comparison: EGA versus SGA2 for the cote21 torsion and depth arguments',url='https://arxiv.org/pdf/math/0511279',result='After reading the actual cote21 arguments, SGA2 IV and XIV are the direct matches, not an unspecified EGA theorem. EGA bibliography and previously checked EGA volumes supply context only; no exact EGA claim is invented.',claims=[B[n]['id'] for n in range(1,20)]),
])
with (D/'search_log.jsonl').open('w') as f:
 for row in log:f.write(json.dumps(row,ensure_ascii=False)+'\n')

links=[]
def link(kind,a,b,what,evidence,notes=''):
 links.append(dict(kind=kind,**{'from':a,'to':b},what=what,evidence=evidence+(' Subjects: '+notes if notes else ''),note_ids=''))
for c in C:
 for k in c['refs']:
  link('published work',c['source']+'; cote'+c['cote']+'; scans'+c['scans']+'; lines'+c['lines'],k+'; '+R[k]['url']+'; '+c['literature_locator'],c['fate'],'Both source passage and stated external locator read. '+R[k]['scope'],','.join(c['items']))
folder_pairs=[
(25,82,'Same sum/product minimax statement; scan144 makes the indices legible but its codimension proof needs the opposite signs.'),
(26,27,'The tensor basis construction continues into the Hilbert–Schmidt identification.'),
(28,70,'Nonzero SVD data do not imply equality of zero eigenspaces; the later explicit unitary-equivalence question has a weighted-shift counterexample.'),
(31,35,'Normalized exterior Hilbert powers feed the mixed fundamental-form coefficient1/n!.'),
(36,44,'K1-03 scan79 restates determinant domination with the correct inequality, correcting the earlier equality display in K1-02.'),
(37,60,'The unproved nonnormal trace reduction is followed by genus-zero/minimal-type lemmas intended for the analytic proof.'),
(38,66,'Later two-sided mixed Cauchy–Schwarz supplies a detailed proof route for the earlier mixed coefficient bound.'),
(40,83,'The strongest-sum language and individual-eigenvalue question concern distinct notions of sharpness; neither implies a pointwise eigenvalue/singular-value bound.'),
(52,55,'The later operator summary restores the correct norm-order direction from the earlier sequence summary.'),
(54,55,'The full operator-dual proof restores the polar and variance omitted in summary lines.'),
(58,59,'The order/genus reminders are continued across K1-04 to K1-05; the order1 remark is corrected by the later reciprocal calculation.'),
(59,62,'Same product-zero order calculation, with the later valid reciprocal exponent.'),
(65,69,'K1-06 scan127 margin calls the earlier S holomorphic; this supports distinguishing modern entire holomorphy from bounded type.'),
(67,68,'The valid determinant theorem uses the two-sided mixed bound, not the false one-sided strengthening.'),
(72,75,'The analytic spectral estimate depends on Hölder; the later independent dyadic/generating-function proof closes that dependency.'),
(76,81,'Finite nonzero spectral clusters are combined with summable tails for a precise whole-list topology.'),
(79,80,'The adjacent monotonicity question is stronger than operator-norm Hölder; the claimed equivalence is false.'),
(84,85,'The excluded-eigenvalue formula proves positivity although the adjacent unsigned/decreasing summand argument fails.'),
(10,11,'The local torsion representation is extended globally by ind-representation, not by unrestricted evaluation on O.'),
(13,15,'K21-01 definitions and margin continue into K21-02 pointwise sheaf-depth proof.'),
(15,17,'The category-valued analogue reuses noetherian induction but adds a real effective-descent requirement.'),
]
for a,b,t in folder_pairs:
 def loc(n):
  c=B[n];return c['source']+'; cote'+c['cote']+'; scans'+c['scans']+'; lines'+c['lines']+'; '+c['id']
 link('folder',loc(a),loc(b),t,'Both supplied passages read in full; link is a mathematical continuation/comparison unless explicitly a correction. No missing intervening leaf is supplied.',','.join(dict.fromkeys(B[a]['items']+B[b]['items'])))
with (D/'links.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(links)
(D/'other_project_links.tsv').write_text('kind\tfrom\tto\twhat\tevidence\tnote_ids\n')
(D/'other_project_links.md').write_text('# Other-project leads\n\nNone occur in the context-free Codex notes assigned here. This is an empty quarantined table, not an assertion that all mathematics is unrelated to other projects. No La Longue Marche, Dérivateurs, S6 or prior-run connection has been invented from subject resemblance. Core Pro-note leads remain separately recorded in parts/ega.\n')

directions=[]
def direction(rank,title,interest,feasible,items,claims,problems,known,residual,first):
 directions.append(dict(id=f'D-SA23-analysis_curves-{rank:02}',rank=rank,title=title,interest=interest,feasible_progress_in_one_run=feasible,items=[f'SA23-{x}' for x in items],claims=[B[x]['id'] for x in claims],problems=[f'MP-SA23-analysis_curves-{x:02}' for x in problems],known=known,residual=residual,first_step=first))
direction(1,'Determine the sharp boundary of fractional-power monotonicity',5,4,[419],[77,79,80],[20],'Constant-one comparison proves monotonicity from s to r when p>=s; an exact positive2×2 example refutes unrestricted all-p monotonicity.','The exact optimal parameter region or dimension-dependent exceptions beyond this sufficient range are not determined by the present counterexample.','Start a separate task with the saved2×2 rational family and Ricard introduction; state a fixed p,s,r optimization problem before testing whether every p<s admits a counterexample.')
direction(2,'Reconstruct the published and archival spectral-continuity proof',5,5,[410,411,415,419],[33,37,60,64,76,81],[9,10],'Finite Riesz clusters, all-p tail matching, and the Hilbert trace formula are established; Reinov supplies exact1955 locators.','The chronological relationship and precise Sigma(p) convention require direct comparison with the original published formulation and any missing manuscript definition.','Compare cote1 scans67,71,111–112,119,147–148 against Memoirs16 II13 and II21 Remark4; produce a statement/proof/date concordance without inferring dates from mathematics alone.')
direction(3,'Write the categorical depth companion with exact descent hypotheses',5,5,[405,406],[13,14,15,16,17,18,19],[4,5],'Noetherian sheaf local-to-global depth is valid; arbitrary fibred-category P3 is false; stacks and torsors supply effective descent.','The surjectivity-only margin and any weakening of noetherian/retrocompact hypotheses need a chosen formulation.','Place the three-point prestack counterexample beside the draft’s gluing step, then align Zariski localizations with SGA2 XIV’s strict étale localizations in a hypothesis table.')
direction(4,'Separate scalar and multivariable subadditivity questions',4,4,[412,413],[40,41,42,43,44],[11,12],'Normalized continuous nonnegative one-variable trace subadditivity is equivalent to concavity; published concavity gives partial sums; Horn gives complete finite sum feasibility.','The manuscript multivariable request and strongest-possible language are not precise residual conjectures.','Extract exactly which functions of n singular values the margin allows, fix normalization and monotonicity, and compare the resulting smallest-dimensional problem with Fack–Kosaki4.7 and Fulton15.')
direction(5,'Recover the meaning and provenance of the entire l1 example',4,4,[415,416],[58,61,64,65],[15,16],'The sum n!e_n is entire but unbounded on the unit ball, with uniform Taylor radius1; scalar order and liminf repairs are settled.','The exact historical meaning of entière and the first published occurrence of this particular example remain unidentified.','Read the scan containing pas une fonction entière together with the later holomorphic margin and search Grothendieck’s analytic-function papers for the exact coefficient series, keeping H and Hb terminology separate.')
direction(6,'Build a normalization and polar-duality companion',4,5,[409,410,414],[28,31,35,51,52,53,54,55,56,57],[7,8,14],'SVD, normalized exterior powers, minimal/maximal ideals and polar trace duality are established; the source contains several mutually correcting summaries.','Ink is needed to decide whether missing polar signs, swapped factors, and the unlocated Non! are transcription faults or manuscript slips.','Create a single notation table with domain/codomain, finite/maximal completion and polar gauge; adjudicate only the listed scan alarms and attach the exact finite certificates.')
direction(7,'Publish a compact operator-counterexample appendix for the dossier',4,5,[411,413,417,419,420],[36,42,45,47,49,67,70,80,82,83,85],[13,17,20,21,22],'All listed literal failures have exact scalar,2×2, cyclic or compact block examples with hypotheses checked.','Presentation and archival sign adjudication remain; these examples are not claimed as new historical discoveries.','Turn the existing certificate outputs into a source-linked appendix of minimal examples, keeping each false formula separate from its valid surrounding theorem.')
direction(8,'Make the torsion-functor global extension precise',4,5,[401,402,403,404],[1,2,4,5,6,7,8,10,11,12],[1,2,3],'Finite representation, co-I-adic systems and supported ind-representation hold; the global O-evaluation formula fails.','The draft’s general abelian-target ambitions require explicit existence and exact-colimit assumptions, rather than another claim of unrestricted representability.','Write the finite, all-module and torsion statements in parallel, prove the category-of-elements transition, and compare each with SGA2 IV before proposing any larger target category.')
direction(9,'Resolve trace fragments and proof dependencies',3,4,[407,408,417,418],[20,21,22,23,24,68,71,72,73,74,75],[6,18],'Published Bourbaki113 and Fack–Kosaki identify the semifinite framework; the independent exterior/dyadic Hölder route removes circularity.','The fragment’s b, cutoff conventions and missing references need scan/source alignment; arbitrary C*-traces cannot be silently upgraded.','Compare HC1-01 scans4,12,15,24,27,35 with Bourbaki113 §§2–5, then draw a proof-dependency table for determinant, p-subadditivity, spectral bounds and Hölder.')
(D/'directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')
text=['# Ranked directions — cotes 1 and 21\n','These are separate future tasks. Mathematical checks already needed to adjudicate the source are complete; none of the residual programmes below is developed here. Ratings use1–5, with5 highest.\n']
for x in directions:
 text.extend([f"## {x['rank']}. {x['title']}\n",f"Interest **{x['interest']}/5**; progress feasible in one run **{x['feasible_progress_in_one_run']}/5**.\n",'Items: '+', '.join(x['items'])+'. Claims: '+', '.join(x['claims'])+'. Problems: '+', '.join(x['problems'])+'.\n','Known: '+x['known']+'\n','Residual: '+x['residual']+'\n','First concrete step: '+x['first_step']+'\n'])
(D/'directions.md').write_text('\n'.join(text))
print(json.dumps(dict(search_records=len(log),links=len(links),directions=len(directions)),indent=2))
