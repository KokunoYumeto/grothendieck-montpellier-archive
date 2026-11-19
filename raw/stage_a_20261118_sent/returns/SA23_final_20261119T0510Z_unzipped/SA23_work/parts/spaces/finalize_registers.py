from pathlib import Path
import json,csv,re,runpy,collections
P=Path(__file__).parent
ns=runpy.run_path(str(P/'build_claims.py'));cs=ns['claims'];its=list(ns['items'].values())
R=json.loads((P/'reference_checks.json').read_text())
for c in cs:
 if c['id']=='C-SA23-spaces-035':
  c['refs'].append('spaces_Lawvere1963');c['fate']+=' Lawvere, 2004 reprint pp79–80, independently discusses the product obstruction for division rings and generalized inverse algebraic structure; this is a precise conceptual parallel, not a claim that his displayed ring map is literally printed there.'
 if c['id']=='C-SA23-spaces-081':
  c['refs']+=['spaces_Kollar2011','spaces_Witaszek2022']
  c['fate']='The affine versus geometric quotient warning is established (Stacks Groupoids example-quotient-projective-line). Finite locally free equivalence relations are effective: Stacks39.23.9 tag03BM. Mere finiteness does not imply effectivity: Raicu appendix§50 in Kollar2011 pp252–254 gives finite scheme-theoretic relations on A² strictly smaller than the quotient fiber product. Kollar Theorem6 proves geometric quotient existence for finite set-theoretic relations on algebraic spaces essentially of finite type over Noetherian F_p-schemes. Witaszek2022 Theorem1.4 extends existence over excellent bases for separated finite-type algebraic spaces provided the characteristic-zero quotient already exists separated finite type. The manuscript does not specify which notion its “OK” intends. The general characteristic-zero scheme-theoretic existence question is Question8 in Kollar2011; this search did not locate a resolution as of19Nov2026, which is not a certification that it remains open.'
  c['computation']+=' Published Raicu example is used as a counterexample to effectivity; its computer algebra certificate was not rerun here and is labelled background evidence, not a new computation.'
 for n in ['028','029','030','019','020']:
  if c['id']==f'C-SA23-spaces-{n}':c['fate']+=' Exact original SGA IV 1.2,4.2 or Exercise7.6 loci are recorded in reference_checks.json; selected printed pages were visually checked.'
 c['fate_date']='As of19November2026. '+ ' | '.join(r+': '+R[r]['year']+'; '+R[r]['annotation'].split(';')[-1] for r in c['refs'])+'. Manuscript is undated here; no priority inferred.'
 c['present_status']='As of19November2026: '+c['fate']
(P/'claims.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n');(P/'items.json').write_text(json.dumps(its,ensure_ascii=False,indent=2)+'\n')
# Tables retain manual grouping. Update problem states from refined claim register.
ps=json.loads((P/'problems.json').read_text());by={c['id']:c for c in cs}
for p in ps:
 cc=[by[x['claim']] for x in p['occurrences']]
 p['state_of_art']=' '.join(c['id']+': '+c['fate'] for c in cc)
 p['refs']=sorted({r for c in cc for r in c['refs']})
(P/'problems.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
queries=[
('system1',['SGA 4 produit topos bifaisceaux produit espaces topologiques quasi compact voisinages','Grothendieck topos product E presheaf category functor category product topoi SGA'],['spaces_Lafforgue2024','spaces_SGA4I'],'Product-site theorem found; arbitrary inverse-image formulas require sheafification.'),
('system2',['"produit de topos" "bifaisceaux"','"SGA 4" "Produits" "topos"','"localic product" "countably many" "discrete" spatial'],['spaces_Lafforgue2024','spaces_Heckmann2015'],'Ordinary local compactness matched; locally closed compact-point refinement not independently named.'),
('system2',['"Spatiality of countably presentable locales" pdf','"product" "discrete locales" "spatial"','site:laurentlafforgue.org Mondovi 2024 toposes product'],['spaces_Heckmann2015','spaces_Lafforgue2024'],'Exact publisher abstract and slides47–48 opened. Countable product application proved independently.'),
('system2',['site:stacks.math.columbia.edu immersion fpqc local target not quasi compact','site:stacks.math.columbia.edu descent ampleness faithfully flat quasi compact projective quasi projective','site:stacks.math.columbia.edu flat base change closure quasi compact morphism image'],['spaces_StacksImmersion','spaces_StacksAmple','spaces_StacksClosure','spaces_StacksDescent'],'Exact hypotheses read in Stacks raw source and stable tags. Arbitrary immersions require correction.'),
('system1',['SGA 4 IV 4.2.3 espaces sobres topos','SGA 4 IV 7.1 presheaves points foncteurs filtrants','Lawvere functorial semantics algebraic theories 1963 2004 pdf'],['spaces_SGA4I','spaces_Lawvere1963'],'Original SGA facsimile and TAC reprint opened; translations used only as locator leads.'),
('system2',['SGA 4 tome 1 pdf 269 Grothendieck Verdier','site:stacks.math.columbia.edu "Morita" "End" "finite locally free"','site:stacks.math.columbia.edu "formally smooth" "fpqc"'],['spaces_SGA4I','spaces_Morita','spaces_StacksFormal'],'SGA PDF mirror obtained; formal smoothness exact lemma found after backward label search.'),
('system1',['site:stacks.math.columbia.edu "formal smoothness" "fpqc" "target"','site:stacks.math.columbia.edu "Morita" "modules" "matrix"','site:stacks.math.columbia.edu "very ample" "faithfully flat"','site:stacks.math.columbia.edu "absolutely flat" "x" "y"'],['spaces_StacksFormal','spaces_Morita','spaces_StacksAmple','spaces_StacksRegular'],'General Morita source metadata found; local matrix-unit proof supplied, not falsely attributed to an unread theorem number.'),
('system2',['"SGA4-1.pdf"','"formally smooth" "faithfully flat" "descends"','"Morita" "locally free" "endomorphism" topos','"absolutely flat" "Stacks project"'],['spaces_SGA4I','spaces_StacksFormal','spaces_Morita','spaces_StacksRegular'],'SGA original downloaded via SLMath; Orgogozo503 and alternate404 failures retained below.'),
('system2',['Lawvere functorial semantics algebraic theories 2004 reprints tac 5 pdf','site:stacks.math.columbia.edu "faithfully flat" "projective" "Theorem 10.95"','site:stacks.math.columbia.edu "Morita" "Brauer"','site:stacks.math.columbia.edu "relative ampleness" "35.25"'],['spaces_Lawvere1963','spaces_StacksFormal','spaces_Morita','spaces_StacksAmple'],'Arbitrary projectivity descent, not only finite projectivity, checked in formal-smoothness proof.'),
('system2',['site:stacks.math.columbia.edu "descent-formally-smooth"','site:stacks.math.columbia.edu "Let $R \\to S$ be a ring map" "formally smooth" "faithfully flat"','site:stacks.math.columbia.edu "Morita equivalence"','site:stacks.math.columbia.edu "Lemma 35.25.4"'],['spaces_StacksFormal','spaces_Morita','spaces_StacksAmple'],'Exact primary labels followed rather than relying on snippet.'),
('system2',['Morita 1958 Duality for modules applications theory rings with minimum condition pdf','site:stacks.math.columbia.edu "projective" "not" "Zariski" "quasi-projective"','site:stacks.math.columbia.edu "Lemma 29.26.16"','site:stacks.math.columbia.edu "Lemma 35.25.4" "ample"'],['spaces_Morita','spaces_StacksProjective','spaces_StacksAmple'],'Repository1958 verified; Hironaka blowup counterexample read. The broad projectivity statement is not confused with a specified ample bundle.'),
('system1',['Kollar finite equivalence relations schemes quotients 2008 arxiv exact hypotheses','site:zbmath.org Grothendieck Verdier SGA 4 théorie topos 269','site:mathoverflow.net product topoi discrete locales spatial countable','site:stacks.math.columbia.edu quotient finite equivalence relation affine finite not flat'],['spaces_Kollar2011','spaces_StacksQuotient','spaces_SGA4I','spaces_Heckmann2015'],'Kollar exact distinctions and Raicu appendix found. MO398371 gives same Cantor counterexample; used as search lead, own proof and SGA primary used for mathematics. zbMATH query supplied no independent usable record.'),
('system1',['"Kollár" "Question 8" "equivalence" quotient','"finite scheme-theoretic equivalence relations" "quotient" 2025 2024 2023','"scheme-theoretic equivalence relation" "geometric quotient" conjecture'],['spaces_Kollar2011','spaces_Witaszek2022'],'Recency3650 on first query. No resolution of general characteristic-zero scheme-theoretic existence located; do not call it certified open in2026. Cambridge2025 release is not a new theorem.'),
('system2',['Witaszek 2022 theorem 1.4 finite equivalence relations mixed characteristic quotients arxiv','"Kollar" "Question 8" "scheme" "quotient" solution'],['spaces_Witaszek2022','spaces_Kollar2011'],'Primary arXiv PDF Theorem1.4 read; excellent/separated/finite-type and existing rational-fiber quotient assumptions retained.')]
logs=[]
for i,(engine,qs,refs,outcome) in enumerate(queries,1):
 logs.append({'id':f'S-spaces-{i:03d}','date':'2026-11-19','engine':engine,'queries':qs,'claims':[c['id'] for c in cs if set(c['refs'])&set(refs)],'sources':[{'key':r,'url':R[r]['url'],'locator':R[r]['annotation'].split(';')[0]} for r in refs],'outcome':outcome})
for r,v in R.items():
 logs.append({'id':f'R-spaces-{r}','date':'2026-11-19','engine':'direct primary-source open / local text search','query':v['annotation'].split(';')[0],'claims':[c['id'] for c in cs if r in c['refs']],'url':v['url'],'locator':v['annotation'],'outcome':'Link opened or raw primary source downloaded; exact scope is annotation. Local elementary work is executed code, not an external literature hit.'})
logs.append({'id':'S-spaces-access-limits','date':'2026-11-19','engine':'direct-open','queries':['https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-IVo.pdf','https://zbmath.org/?q=an%3A0118.36206','https://par.nsf.gov/servlets/purl/10429755'],'outcome':'Orgogozo503: original obtained instead from SLMath; zbMATH403: Numdam primary metadata supplies Zbl identifier but review itself not read; NSF502: Witaszek arXiv PDF opened instead. Morita PDF429: only repository metadata verified. These access failures are not negative mathematical evidence.'})
(P/'search_log.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in logs))
who='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner spaces'
ev=[]
for c in cs:
 typ='targeted proof check'
 if c['class']=='F':typ='carried as background without fault found'
 if any(s in c['computation'].lower() for s in ['counterexample','negative answer','f₂×f₃']):typ='refuted, with refinement in same claim'
 ev.append([c['id'],'2026-11-19',who,typ,c['computation']])
for i in its:
 ev.append([i['id'],'2026-11-19',who,'used and rechecked in this run','Manually consolidated mathematical subject; detailed hypothesis/proof checks in '+','.join(c['id'] for c in cs if i['id'] in c['items'])+'. This is not an indexed Pro-entry verdict.'])
for r,v in R.items():ev.append([r,'2026-11-19',who,'used and rechecked in this run','Bibliographic/link and hypothesis matching only; '+v['annotation']])
for n in json.loads((P/'compute_checks.output.json').read_text()):ev.append([n,'2026-11-19',who,'computation or formal certificate','Executed exact program; see compute_checks.py/output. Scope limited to displayed identity or finite case.'])
with (P/'check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(ev)
with (P/'links.tsv').open(newline='') as f:ls=list(csv.reader(f,delimiter='\t'))
ls.append(['folder','161-3 scans4,7,3a:1–52,184–225;161-4 scan18,4b:1–79','161-6 scan23,K161-6-02_transcription.tex:374–430','Functor-category product and direct-image question recur on a wholly cancelled sheet.','Both endpoints directly read; cancellation status preserved; does not validate false projection membership criterion.','unindexed Codex notes; cross-owner misc'])
with (P/'links.tsv').open('w',newline='') as f:csv.writer(f,delimiter='\t').writerows(ls)
print('Finalized',len(cs),'claims;',len(its),'items;',len(ps),'problems;',len(ev),'check events;',len(logs),'search/read audit events')
runpy.run_path(str(P.parents[1]/'integration/apply_bt_spaces_problem_origins.py'))['apply_owner']('spaces')
runpy.run_path(str(P/'audit_publication_classes.py'))['save_audit']()
