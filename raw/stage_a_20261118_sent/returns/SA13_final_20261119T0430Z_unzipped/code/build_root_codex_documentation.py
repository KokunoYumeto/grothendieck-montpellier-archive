"""Write manually specified reference/search audits and root Codex check events.

The mathematical reviews are authored in the claim and proof files. This script
only serializes that audit and checks its coverage; it does not infer verdicts.
"""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[2]; O=R/'deliverable/shards/root_codex'
refs=[]
def B(key,typ,title,author,year,url,scope,**kw):
 refs.append(dict(key=key,type=typ,title=title,author=author,year=year,url=url,note='verified',annotation=scope,**kw))
B('RC_SGA7I','book','Groupes de monodromie en géométrie algébrique I (SGA7 I)','Grothendieck, Alexander and Raynaud, Michel and Rim, Dock Sang','1972',
 'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf',
 'Original facsimile opened; I printed10–20 and pertinent depth/monodromy passages read and visually checked where OCR was doubtful. Exact locators: I(3.1.2),3.3,4.5–4.11,5.1–5.5. Section5 identifies the lecture as1968-11-19. The printed3.4 nilpotence bound itself has an off-by-one problem; modern corrected bounds are separately cited.',series='Lecture Notes in Mathematics',volume='288')
B('RC_SGA2','book','Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA2)','Grothendieck, Alexander and Raynaud, Michèle','1968',
 'https://arxiv.org/pdf/math/0511279',
 'Author-edited retypeset source opened, arXiv2005-11-10. XIV5.2–5.6,6.2–6.3 and editorial footnotes6–7 read. Minimal number of ideal generators, not arithmetic rank, defines geometric depth;5.5 has the separable residue-field fibre hypothesis. Original seminar1962; original publication1968; reedition2005. No date is inferred for the archival draft.',eprint='math/0511279',archivePrefix='arXiv')
B('RC_MRaynaud1974','article','Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental','Raynaud, Michèle','1974',
 'https://www.numdam.org/article/ASENS_1974_4_7_1_29_0.pdf',
 'Original24-page article opened; III1.2–1.3,pp48–49 read for exact nonabelian depth and base hypotheses. Does not certify an arbitrary excellent-base extension.',journal="Annales scientifiques de l'École Normale Supérieure",volume='4e série,7',number='1',pages='29--52',doi='10.24033/asens.1260',zbl='0317.14006')
B('RC_Orgogozo2003','article','Altérations et groupe fondamental premier à p','Orgogozo, Fabrice','2003',
 'https://www.numdam.org/article/BSMF_2003__131_1_123_0.pdf',
 'Original25-page article opened; Corollary4.5 p138 is the field-extension invariance locator, not4.6;4.7–4.9 and Theorems4.10–4.11 p143 read. Received2002-01-25,accepted2002-03-22. No earlier public circulation established.',journal='Bulletin de la Société Mathématique de France',volume='131',number='1',pages='123--147',doi='10.24033/bsmf.2438',zbl='1083.14506')
B('RC_Illusie2003','article','Perversité et variation','Illusie, Luc','2003',
 'https://link.springer.com/article/10.1007/s00229-003-0407-z',
 'Publisher record opened. Original first pages also read in primary reproduction https://studylibfr.com/doc/350158/perversit%C3%A9-et-variation : intro pp271–272 explicitly states the scope of2.6,2.7,2.10; §1 proof and start of§2 read. Full §2 proofs were not accessible there; no whole-paper proof check asserted. Received2003-02-01,published online2003-09-23.',journal='Manuscripta Mathematica',volume='112',pages='271--295',doi='10.1007/s00229-003-0407-z')
B('RC_Illusie2021','article','Grothendieck and vanishing cycles','Illusie, Luc','2021',
 'https://www.imo.universite-paris-saclay.fr/~illusie/Illusie-Grothendieck-nearby-cycles12.pdf',
 'Author36-page text opened; §1 conventions,2.3,2.7–2.8,6.3,6.5 read. Based on talks2015-06-17 and2015-11-13; publication2021. Its2021 description of open problems is supplemented by2026 author material, not treated as a current exhaustive survey.',journal='Annales de la Faculté des Sciences de Toulouse',volume='30',pages='83--115',doi='10.5802/afst.1667')
B('RC_DeligneMilne1982','incollection','Tannakian Categories','Deligne, Pierre and Milne, James S.','1982',
 'https://www.jmilne.org/math/xnotes/tc.pdf',
 'Corrected author version dated2012-08-15 opened. Proposition2.8,Remark2.10,Theorem2.11,Propositions2.20–2.21 read; fibre functor and faithful-flatness hypotheses retained. Original publication1982, not2012.',booktitle='Hodge Cycles, Motives, and Shimura Varieties',series='Lecture Notes in Mathematics',volume='900',pages='101--228')
B('RC_Lazard1965','article','Groupes analytiques p-adiques','Lazard, Michel','1965',
 'https://www.numdam.org/item/PMIHES_1965__26__5_0/',
 'Original bibliographic record and its backward references opened. The large PDF exceeded the web retrieval limit; no claim to a full original-proof audit. Compact linearity is checked through the2025 primary proof. The1965 original date controls, despite a modern introduction referring to1968.',journal="Publications Mathématiques de l'IHÉS",volume='26',pages='5--219',doi='10.1007/BF02684303',zbl='0139.02302')
B('RC_CasalsZozaya2025','article','Linearity of compact R-analytic groups','Casals-Ruiz, Montserrat and Zozaya, Andoni','2025',
 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0FA5C90BD9DDF78773494D19EF14B939/S0013091524000634a.pdf/linearity-of-compact-r-analytic-groups.pdf',
 'Full8-page publisher PDF opened. Theorem2.1 and its proof of faithful linearity for uniform pro-p groups, followed by finite-index induction, read. Received2024-01-11,published online2025-03-21. The wider R-analytic theorem is not conflated with the classical Q_p case.',journal='Proceedings of the Edinburgh Mathematical Society',volume='68',pages='787--794',doi='10.1017/S0013091524000634')
B('RC_StacksLimits','misc','The Stacks Project: limits of schemes and finite presentation','The Stacks Project Authors','2026',
 'https://stacks.math.columbia.edu/tag/01ZM',
 'Tag01ZM read with01ZO and07RP (all opened). Finite-presentation objects and morphisms descend under affine qcqs limits, and the étale property descends. Accessed2026-11-19; applies to the stated qcqs hypotheses.')
B('RC_StacksFundamental','misc','The Stacks Project: fundamental groups and normal schemes','The Stacks Project Authors','2026',
 'https://stacks.math.columbia.edu/tag/0BQI',
 'Tag0BQI opened and read for dense-open fundamental-group surjectivity with the normal/geometrically unibranch hypotheses. Limit statements use RC_StacksLimits and descent of finite étale covers; this single tag is not claimed to state every pro-object construction.')
B('RC_MilneCFT','misc','Class Field Theory','Milne, James S.','2020',
 'https://www.jmilne.org/math/CourseNotes/CFT.pdf',
 'Author version4.03,2020-08-06 opened; I Theorem4.16 and4.17,pp49–50 read for Kronecker–Weber and the conductor/inertia qualification. Historical theorem used as background, not a new manuscript result.')
B('RC_Tate1966','article','Endomorphisms of abelian varieties over finite fields','Tate, John','1966',
 'https://link.springer.com/article/10.1007/BF01404549',
 'Publisher record opened; exact integral Hom theorem also checked in Gajda–Petersen Theorem2.3. Publisher month/received-date fields conflict, so only publication year1966 is used. No full original-proof audit.',journal='Inventiones Mathematicae',volume='2',pages='134--144',doi='10.1007/BF01404549')
B('RC_Faltings1983','article','Endlichkeitssätze für abelsche Varietäten über Zahlkörpern','Faltings, Gerd','1983',
 "https://math.uchicago.edu/~drinfeld/Deligne's_conjecture_Manin_conf/Faltings_argument/Faltings.pdf",
 'Original18-page facsimile opened; §1 pp349–350 states the number-field semisimplicity/endomorphism consequences and Lemma1 extends homomorphisms over normal bases. Finitely generated-field scope is checked in the modern theorem and its history, not assumed from the title.1984 complements distinguished.',journal='Inventiones Mathematicae',volume='73',pages='349--366',doi='10.1007/BF01388432')
B('RC_Zarhin2011','misc','Homomorphisms of abelian varieties over geometric fields of finite characteristic','Zarhin, Yuri G.','2011',
 'https://arxiv.org/pdf/1012.5083',
 'Author preprint opened; introduction pp1–2 and references p10 read for historical attributions and distinct field hypotheses. First submitted2010-12-22; retrievedv3 dated2011-10-11. The paper’s own geometric-field results are not substituted for the arithmetic Tate theorem.',eprint='1012.5083',archivePrefix='arXiv')
B('RC_MoretBailly1985','book','Pinceaux de variétés abéliennes','Moret-Bailly, Laurent','1985',
 'https://www.numdam.org/item/AST_1985__129__1_0/',
 'Original Numdam facsimile obtained and read by p3; XII0.1 p239 and XII2.4–2.5 pp244–245 checked. XII2.5 gives integral Tate Hom and rational semisimplicity for the stated function fields over a finite field. XII2.4 explicitly calls Mori’s characteristic2 input unpublished; no earlier circulation date invented. Root inspected the supplied primary extraction; full source is not redistributed.',series='Astérisque',volume='129')
B('RC_GajdaPetersen2022','article','Local to global principles for homomorphisms of abelian schemes','Gajda, Wojciech and Petersen, Sebastian','2023',
 'https://arxiv.org/pdf/2207.09345',
 'Author24-page v2 opened; Theorem2.3 p6 and Lemma3.4 p10 read, including normal-base Hom proof. First arXiv2022-07-19, revised2023-04-11. Publisher https://link.springer.com/article/10.1007/s11856-023-2542-4 opened: received2022-02-06,publication2023-12-22,issueNovember2023. Reference key retains preprint year.',journal='Israel Journal of Mathematics',volume='257',pages='281--312',doi='10.1007/s11856-023-2542-4',eprint='2207.09345',archivePrefix='arXiv')
B('RC_WeilII1980','article','La conjecture de Weil: II','Deligne, Pierre','1980',
 'https://www.numdam.org/item/PMIHES_1980__52__137_0/',
 'Publisher/Numdam record opened; original full facsimile obtained by p2 and relevant extracted text read by root, notably Corollaries3.3.4–3.3.6 p206. The source proves weights, not unconditional ranks of every algebraic correspondence across ell. Received1979-06-01,publication1980-12-28.',journal="Publications Mathématiques de l'IHÉS",volume='52',pages='137--252',doi='10.1007/BF02684780',zbl='0456.14014')
B('RC_vanDobben2020','article','The equivalence of several conjectures on independence of ell','van Dobben de Bruyn, Remy','2020',
 'https://epiga.episciences.org/6931/pdf',
 'Full27-page primary paper opened; introduction pp2–3 and Theorem1 p3 read. First arXiv2018-08-01 independently verified at https://arxiv.org/abs/1808.00119 ; received2019-06-12,final2020-08-01,accepted2020-09-02,published2020-11-30. Exact equivalence of conjectures, not an unconditional solution.',journal='Épijournal de Géométrie Algébrique',volume='4',number='16',doi='10.46298/epiga.2020.volume4.5570',eprint='1808.00119',archivePrefix='arXiv')
B('RC_WanZhang2025','misc','Betti number bounds for varieties and exponential sums','Wan, Daqing and Zhang, Dingxin','2025',
 'https://zhangdingxin.gitlab.io/math/pdf/betti.pdf',
 'Current47-page author PDF opened2026-11-19; §1.1 p2 explicitly retains general singular/nonproper compact-support Betti independence as open. First arXiv2025-01-22. Search found a2026 publisher article, but opening returned403; its exact publication metadata is not certified here.',eprint='2501.12623',archivePrefix='arXiv')
B('RC_ItoZou2026','misc','Semisimplicity, Purity and Mumford–Tate Conjecture for hyper-Kähler Varieties','Ito, Kazuhiro and Zou, Haitao','2026',
 'https://www.math.uni-bielefeld.de/~hzou/papers/semisimplicity/',
 'Author HTML preprint dated2026-10-06 opened. TheoremsA/2.5,B/4.4,C/5.8 checked for exact hyper-Kähler and b2 restrictions. Preprint status retained; no inference that general weight–monodromy is solved.')
B('RC_MumfordGIT','book','Geometric Invariant Theory','Mumford, David and Fogarty, John','1982',
 'https://dokumen.pub/geometric-invariant-theory-2nbsped-3540112901-9783540112907.html',
 'Primary-source reproduction opened by p4 and root. Retrieved Chapter2 §1 pp49–53: Definition2.2,Theorem2.1,Propositions2.2–2.3 and Iwahori proof steps. An OCR gap afterp53 prevents full collation of the coordinate continuation and Proposition2.4 or independent confirmation ofp55 pagination. Proposition2.4 is identified by the appendix cross-reference; Appendix2A p156 corrects the positive-characteristic lifting via ramified extension. The first printed reduction cites Theorem1.19, confirming that marginal correction; the orbit-closure reduction still cites Theorem1.14, so the references must not both be replaced. The1982 comparator preserves much1965 text; it does not date the archival printed sheets or assign authorship to Grothendieck.',edition='2',publisher='Springer-Verlag')

def esc(x):return str(x).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
with (O/'references.bib').open('w') as f:
 for r in refs:
  f.write('@'+r['type']+'{'+r['key']+',\n')
  for k,v in r.items():
   if k not in ['key','type']:f.write('  '+k+' = {'+(str(v) if k in ['url','doi'] else esc(v))+'},\n')
  f.write('}\n\n')
(O/'reference_audit.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')

searches=[
 ('RC-S01','600–602,605–606','SGA7 I 4.5 profondeur locale cycles évanescents; Illusie perversité variation 2003 2.6 2.7 2.10','SGA7 I original; SGA2; Illusie2003 original intro; Illusie2021 author text','Local depth/generization proof and lci trait range matched.2003 supplies later arbitrary-trait scope; support/perversity qualification retained.'),
 ('RC-S02','603–604','SGA2 XIV profondeur géométrique localisation morphisme plat nombre minimal générateurs; site:mathoverflow.net geometric depth étale; site:zbmath.org Perversité et variation','SGA2 original reedition; Illusie2003; Numdam bibliography and indexed zbMATH/MO searches','Definition and separable-fibre invariance matched; exact all-noetherian localization/flat-map removal not located. Search absence is bounded evidence, not proof of openness.'),
 ('RC-S03','607–608','Michèle Raynaud 1974 Théorèmes Lefschetz faisceaux ensembles groupes III1.3; Orgogozo altérations groupe fondamental','Raynaud1974 original; SGA2 editorial references; Orgogozo2003 bibliography backwards','Exact nonabelian depth/base restrictions read. Not promoted to the full excellent-local-base proposal.'),
 ('RC-S04','609–613','Grothendieck nearby vanishing cycles purity variation cone inertia Tate twist; Illusie perversité variation','SGA7 I original; Illusie2003 §1/introduction; Illusie2021 §1; continuous-cohomology calculation','Cone, purity and inertia degrees rederived. The missing Tate twist is independently forced; unread signs stay scan alarms.'),
 ('RC-S05','614–618,623','SGA7 I5.3 groupe fondamental action potentiellement modérée; Orgogozo2003 4.11; prime-to-p fundamental group field extension','SGA7 I5.2–5.3; Orgogozo2003 Cor4.5,Th4.10–4.11; arXiv/Numdam/SGA indexed search','Exact potential-tameness theorem and finite presentation matched; finite-generation condition in Aut compactness retained.'),
 ('RC-S06','619–622,624–626','Grothendieck monodromie courbes stables chemins Kummer SGA7 I5.4; Bertini section square ample','SGA7 I5.1–5.5 and its original references; Orgogozo2003','Stable-curve and node proof matched. The specific square-of-ample-bundle suggestion is not proved by a sufficiently-large-power Bertini theorem.'),
 ('RC-S07','627–630,636','site:mathoverflow.net compact p-adic analytic group linear Lazard; site:zbmath.org Lazard Groupes analytiques p-adiques1965; compact R-analytic groups linearity','Numdam Lazard metadata/backward bibliography; Casals-Ruiz–Zozaya2025 primary proof; MO search used only as leads','Classical compact linearity and local Lie integration matched.1965 date comes from original metadata; modern source’s1968 historical shorthand not copied.'),
 ('RC-S08','631–635,637–641','Deligne Milne Tannakian categories2.11 2.21 proalgebraic completion profinite; algebraic envelope analytic Lie rational components','Deligne–Milne corrected author text; Lazard record; own normalizer counterexample','Fibre-functor recovery and component quotient verified. General rational-component implication false; cancelled central-extension passage remains not uniquely identifiable.'),
 ('RC-S09','642–648,650','site:stacks.math.columbia.edu fundamental group limits finite presentation normal dominant finite index; arithmetic models pro group ell adic representations','Stacks01ZM,01ZO,07RP,0BQI; EGA/SGA limit provenance; Tannakian source','Finite-presentation statements matched. Own finite-field model counterexample distinguishes analytic dimension1 from unbounded algebraic dimension.'),
 ('RC-S10','649,651–653','Gajda Petersen local global principles homomorphisms abelian schemes2.3 3.4 Tate; Zarhin Mori Tate characteristic2; Kronecker Weber conductor','Gajda–Petersen exact primary; Zarhin1012.5083 bibliography backwards to Moret-Bailly1985; Tate publisher; Faltings original; MilneCFT','Exact field/base scope established. Mori publication1985 and absence of a certified earlier circulation date recorded. Model-progroup deduction labelled reconstruction.'),
 ('RC-S11','654–657','van Dobben de Bruyn independence ell standard conjecture ranks correspondences Theorem1; WeilII weights Cech normal crossings','DeligneWeilII original; VDB2020 pp2–3; arXiv1808.00119 history; Wan–Zhang current author§1.1','Weight degeneration and compactification identifications established; general rank independence conditional, still open in exact broad scope.'),
 ('RC-S12','658–661','SGA7 I3.1.2 normal crossings Rj nearby cycles exterior powers; Illusie1994 3.1.2 3.2 weight spectral sequence','SGA7 I printed10–11; Illusie1994 pp34–35 independently read by p2; exact audit retained','Arithmetic Rj has r generators; geometric nearby cycles have r−1. Geometric residue cohomology and Knr abutment restored; E3 is necessary.'),
 ('RC-S13','662–663','independence ell Betti numbers singular nonproper varieties Wan Zhang open (recency365); weight monodromy hyper Kahler Ito Zou2026; inertia invariants purity Tate curve','VDB2020; Wan–Zhang author PDF; Illusie2021; Ito–Zou2026 primary; Tate uniformization input in p2 audit','Literal invariant/coinvariant purity refuted. General independence/weight-monodromy not confused with the hyper-Kähler preprint. Fresh2026 search performed.'),
 ('RC-S14','664–670','Mumford Fogarty Geometric Invariant Theory1982 2.3 2.4 Iwahori proper action one parameter subgroup','Primary1982 source reproduction; p4 exact edition collation; supplied printed leaves read completely','GIT source identified as reused printed work. Original hypotheses and nontrivial1PS condition retained; no archival authorship inference.')
]
def tsv(name,fields,rows):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv('search_log.tsv',['search_id','claim_range','queries','sources_opened','result','date'],[dict(zip(['search_id','claim_range','queries','sources_opened','result','date'],list(x)+['2026-11-19'])) for x in searches])
claims=json.loads((O/'claims.json').read_text());items=json.loads((O/'items.json').read_text())
events=[];who='GPT-6 Astra Pro; configured effort not exposed; SA13 part2/root'
for c in claims:
 proof=c['computation'].get('proof')
 typ='targeted proof check' if proof else 'carried as background without fault found'
 result=('Scope-limited derivation in '+proof+'; named deep input is used as background, not reproved.' if proof else 'Full manuscript passage and exact source scope compared; no independent proof of the external theorem claimed.')
 if c['status_on_pages']=='false as stated':
  typ='refuted, with the refined statement’s id';result='Literal formulation refuted by the fully checked counterexample in '+str(proof)+'. The corrected scope is separately stated in this same claim record; related refinements C-SA13-638,648,663 as applicable.'
 events.append(dict(statement_id=c['id'],date='2026-11-19',who=who,type=typ,outcome=result))
for i in items:events.append(dict(statement_id=i['id'],date='2026-11-19',who=who,type='carried as background without fault found',outcome='All listed transcription passages read in full; item is a source synthesis. Proof status belongs to the linked claim events; reading alone is not counted as a proof.'))
for r in refs:events.append(dict(statement_id=r['key'],date='2026-11-19',who=who,type='carried as background without fault found',outcome=r['annotation']))
for n in [605,610,612,625,626,635,642,647,648,654,658,659,660,661,663,665,669]:events.append(dict(statement_id=f'C-SA13-{n:03}',date='2026-11-19',who=who,type='computation or formal certificate',outcome='code/root_codex_compute.py completed; outputs/root_codex_computations.json all_checks_passed. Finite arithmetic checks only; universal scope comes from the separate proof note.'))
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
assert {s for c in claims for s in c['search_ids']} <= {x[0] for x in searches}
print(json.dumps({'references':len(refs),'search_groups':len(searches),'claims_with_searched_fate':len(claims),'events':len(events)}))
