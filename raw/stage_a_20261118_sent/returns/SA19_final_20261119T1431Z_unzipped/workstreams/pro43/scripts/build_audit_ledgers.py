"""Write trace ledgers from the hand-authored audit and explicit proof mapping.

This program formats records. It makes no note verdict or literature judgment.
"""
from pathlib import Path
import json,csv,re
from collections import Counter
B=Path(__file__).resolve().parents[1]
W=B.parents[1]
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; inherited reasoning effort not exposed; SA19/pro43'
items=json.loads((B/'items.json').read_text())
claims=json.loads((B/'claims.json').read_text())
problems=json.loads((B/'problems.json').read_text())
entries=list(csv.DictReader((B/'entries.tsv').open(),delimiter='\t'))
bib=(B/'references.bib').read_text()
bibparts=re.split(r'(?=@\w+\{)',bib)
refs={}
for s in bibparts:
 m=re.match(r'@\w+\{([^,]+),',s)
 if m: refs[m[1]]=s

groups=[]
def group(nums,searches,query,result,reading,files):
 groups.append(dict(nums=list(nums),sources_searched=searches,query_or_locator=query,
                    result=result,primary_reading=reading+' Saved retrievals: '+files))
group(range(1,13),'arXiv;Numdam;Grothendieck Tohoku;Suzuki author papers',
 'Weil/Greenberg/Néron cohomology comparison; proalgebraic Ext and ind-rational continuity; Grothendieck composite spectral sequence',
 'Suzuki2013 Thm2.1.5 and Suzuki2014 §§2.4,3.4 provide precise replacements; unidentified manuscript site remains conditional. The infinite-Witt continuity was explicitly withdrawn.',
 'Exact theorem hypotheses read; Tohoku Thm2.4.1 read, not §4.2 outside the partial PDF. Independent formal proof in computations§1.',
 '01–04;15;19–21')
group(range(13,23),'arXiv;Numdam;Milne author monograph and bibliography;Serre primary paper',
 'Local finite-flat duality; Serre local class field theory; geometric versus ordinary local degree; Lang descent',
 'Serre1961 §4 Thm1; Suzuki2013 Thms2.6.1,2.7.1; Suzuki2014 Thm5.2.2.1 and §10. Broader all-affine/all-degree claims and Witt quotient remain unverified as specified.',
 'Primary text and coefficient restrictions read; unknown symbols not supplied from later broad subject matches.',
 '01–04;10;19–21;28')
group(range(23,34),'arXiv;Numdam;Stacks official project;Milne primary monograph',
 'Kummer Artin–Schreier alpha_p; multiplicative Ext Tate module; geometrized local G_m/Z',
 'Exact finite coefficient identities and perfected Tate-module formula found; distinction between internal sheaves and geometric points retained.',
 'Suzuki2014 §2.4,Prop3.4.3;Stacks03PK,0A3J;MilneIII§§5–6 read. Independent derivations computations§§3–4.',
 '03–04;19–23')
group(range(34,42),'Numdam;Serre primary PDF;arXiv Suzuki component-pairing papers',
 'Decomposition inertia normal closure; Grothendieck component pairing; bidual completion; semiabelian Tate rank',
 'Normal-closure mechanism proved directly; component pairing settled for perfect residue field by Suzuki. Product splitting not inferred. Rank2a+t restricted to l≠p.',
 'Serre§§4–5 and SuzukiTheoremA/§2.4 read; no exact theorem fixes the contradictory scan114 indices.',
 '02–04;10;19–21')
group(range(42,46),'arXiv;Numdam;Ribeiro and Rosengarten author primary PDF;Breen references backward',
 'Ext abelian scheme G_m higher vanishing; Breen1975 range; filtered coefficient limits',
 'Ribeiro–Rosengarten Thm4.3 gives internal Ext²(A,G_m)=0 over arbitrary base, with Ext³ counterexamples. Finite Kummer settles only stated low degrees; μ∞ continuity is not inferred.',
 'Full primary PDF relevant theorem/proof and introduction read; exact topology and older-proof caveat checked.',
 '05–08')
group(range(46,53),'arXiv;Milne primary monograph;Suzuki local cohomology results',
 'Geometric H¹ abelian variety divisibility; Kummer direct limit; H² finite-flat vanishing; derived-to-degree-zero comparison',
 'SuzukiProp3.4.3 supplies the geometric degree bound and divisibility implication; unidentified Q,N and replacement of derived T(A) remain explicit problems.',
 'Exact theorem and Kummer maps read/re-proved in computations§§7–9.',
 '19–21')
group(range(53,57),'Numdam;SGA2 primary re-edition;Matlis original journal PDF;Stacks references backward',
 'Local duality Ext support thickening colimit; formal functions completion; Matlis injective hull endomorphism',
 'SGA2V2.1,VI2.3,IX2.1 and Matlis3.7/3.10/4.3 are exact matches with hypotheses. Arbitrary underived limits and nonfinite first arguments excluded.',
 'Primary locators and relevant proof context read; DVR computation independently re-proved, with finite matrix outputs.',
 '13;16–18;21;26')
group(range(57,62),'arXiv;Milne bibliography;Artin–Milne original paper;Tohoku',
 'Curve finite-flat duality cohomological bound trace; finite type modulo theta; ArtinMilneCor4.9',
 'Finite-flat duality and trace verified; undefined theta and blanket all-sheaf bound not identified.',
 'Suzuki2018Theorem3.1.3,Props2.7.6–7 and Artin–Milne§4 including Cor4.9 p124 directly read, the latter by OCR plus visual verification.',
 '03–04;11;15;22–23;26;ArtinMilne_pages')
group(range(62,76),'Stacks official project;arXiv;Numdam Oda;SGA1;Artin–Milne;primary backward references',
 'Curve Kummer Picard Brauer; Artin–Schreier semilinear Frobenius; Abel–Jacobi abelian fundamental group; Oda Cartier/Dieudonné',
 'Exact finite geometric tables and étale Jacobian comparison located; full relative p-row remains conditional on its realization. Supersingular counterexample refutes literal full-J[p] identification.',
 'Stacks03PK,03RN,0A3J,0A3L;SGA1IX5.8;OdaCor1.3,Def3.5,Prop3.13,Thm3.19,Cor5.11 read. Search-engine2 then engine1 exact relative-R²G_m follow-up found no stronger theorem within checked sources.',
 '01–02;22–23;25–26;29;33–34')
group(range(76,84),'SGA2 primary;arXiv Suzuki;Stacks localization leads',
 'Codimension-one purity; henselian completion; extension by zero; dual localization triangles',
 'Precise prime-to-p purity and finite-flat localization results located; unrestricted sheaf comparison fails, and the unshifted ordinary box has a degree-zero counterexample.',
 'SGA2I2.8,XIV2.3;Suzuki2014Prop3.4.6,5.2.2.2;Suzuki2018Prop2.6.2,2.7.6–7,Remark2.7.9 read. Independent stalk/sequence check.',
 '11;16–18;21')
group(range(84,90),'Atiyah primary PDF and Celebratio bibliography;zbMATH Open attempted;MathOverflow leads;Cambridge publisher;author-uploaded Sigrist–Suter',
 'Thom Complexes intrinsic join Df diagonal Delta; Stiefel sections James numbers; Adams Walker; Sigrist Suter quaternionic; backward reference lists',
 'Exact reused-source match established. Complex and quaternionic numerical programmes settled in later works; no exact resolution of Df/Delta map equality located. zbMATH an0124.16301 returned403 twice, not a negative result.',
 'Atiyahpp308–310 full text;Adams–Walker publisher theorem extract only;Sigrist–Suter main theorem andThm2.6 full primary author copy. Bibliography metadata distinguished from proof.',
 '09–11;14;24;27–30;31')
group(range(90,98),'Numdam EGAIII/IV;Stacks;MathOverflow;exact EGA question searches;backward references',
 'EGA12.2.3(vi) universal openness S1 multiplicity; associated prime M/tM one-dimensional component; connected components15.5; proper direct images; missing CM numbering',
 'Exact flat multiplicity theorem and explicit1966 remaining question located; later exact resolution not found. Proper connected-component results and EGAIII3.2.1 matched. Missing1.1(ii)/2.6 remains unidentifiable.',
 'EGAIV3pp179–183,233–236;EGAIII1pp116–117 directly read. MO225534 points to the flat EGA theorem, not the universally-open extension. Independent counterexample only to inequality⇒flat.',
 '09–10;16–17;24–27;31–32')
group(range(98,100),'Numdam EGAIII1;official Stacks leads',
 'Euler Poincare finite length complex; projective Euler polynomial all integer twists',
 'EGAIII1OIII11.10.2 andIII2.5.2–3 exactly match; zero sheaf excludes unconditional strict positivity.',
 'Primary proof and all-integer statement read; symbolic proof and finite exact matrix example retained.',
 '09–10;17;computations§20')
group(range(100,104),'Stacks official project;Numdam EGA;Grothendieck bibliography/reference trails',
 'Polynomial localization regularity over imperfect fields; flat local dimension depth EGA6.3.1; unspecified propertyP',
 'Stacks00OO,00OG,0338 give exact proofs. EGAIV2 locator followed through Stacks, not original PDF. Missing property list remains unspecified.',
 'Official proofs read in full relevant paragraphs; no inseparable-base-change shortcut used.',
 '12–13;31–32')
group([104,111],'Stacks official project;SGA1 descent references',
 'Faithfully flat unit map pure injection ideal contraction B/A flat',
 'Equivalent criteria verified with flatness; quotient reading necessary. Tor proof independently supplied.',
 'Stacks00HP and00H9 relevant proofs read; computations§24.',
 '12–13')
group(range(105,111),'Numdam Cartan seminar;Grothendieck Tohoku primary extract;soft/fine sheaf source searches',
 'Soft sheaf ring partition unity; arbitrary integer functions tensor embedding; fine extension by zero; typescript239 provenance',
 'Cartan1951XV/XVI exact theorem matches; source239 authorship/provenance not established. Local support and paracompact Hausdorff hypotheses retained.',
 'CartanXV§§5–6,XVIp4 andTohoku§3.3p159 read. Independent partition/tensor/stalk proof in computations§21.',
 '12;14–15')

mapped={}
for g in groups:
 for n in g['nums']:
  assert n not in mapped
  mapped[n]=g
assert set(mapped)==set(range(1,112))
log=[]
for c in claims:
 n=int(c['id'].rsplit('-',1)[1]);g=mapped[n]
 log.append(dict(date=DATE,claim_ids=c['id'],sources_searched=g['sources_searched'],
                 query_or_locator=g['query_or_locator']+'; exact witnesses: '+','.join(c['refs']),
                 result=c['fate'],primary_reading=g['primary_reading']))
log.append(dict(date=DATE,claim_ids='SA19-53–56',sources_searched='Cambridge primary Saito1979;companion manuscript c44',
 query_or_locator='Proposition3.4;Theorem3.6;Proposition4.4,pp109–113',result='Incidence/Picard construction and Betti bound matched; duality only up to isogeny, and Pro43 scope absence retained.',
 primary_reading='Direct primary text and bound proof read; duality proof referred by Saito to another source. Saved retrievals33–34.'))
log.append(dict(date=DATE,claim_ids='all111;all80items',sources_searched='zbMATH Open;arXiv;MathOverflow;Numdam;EGA;SGA;author bibliographies',
 query_or_locator='Repository coverage summary, not a claim that every repository was searched for every trivial lemma',
 result='Named repositories used for relevant families; zbMATH access403 recorded. Atiyah and Milne bibliographies opened. Exact primary theorem texts, not search snippets, support positive fates. No classD assigned from unsuccessful search.',
 primary_reading='Raw retrieval JSON01–34 and local PDFs/OCR retained. Negative outcomes mean exact fate not located in this bounded audit, not an exhaustive literature proof.'))
with (B/'research_log.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['date','claim_ids','sources_searched','query_or_locator','result','primary_reading'],delimiter='\t');w.writeheader();w.writerows(log)

events=[]
def event(ident,kind,outcome):events.append(dict(statement_id=ident,date=DATE,who=WHO,type=kind,outcome=outcome))
for i in items:
 event(i['id'],'used and rechecked in this run',
       'Documentary comparison of every listed source entry with its actual transcription passage and doubts: '+i['check']+'. '+i['check_reason']+' This event records a text/scope check, not mathematical proof. No second-pass changes exist for this package.')
for c in claims:
 event(c['id'],'used and rechecked in this run',
       'Read actual43/'+','.join(map(str,c['scans']))+' lines'+c['lines']+'; separated status='+c['status_on_pages']+'. Literature search mapped in research_log.tsv; '+c['fate']+' Reading/matching a theorem is not an independent proof of the theorem.')
proofmap={
 1:[2,3,9,10,11,12,25,57],2:[8],3:[19,23,29,30,31,32],4:[27,28],5:[34,35],6:[41],
 7:[42,43,45],8:[47,50],9:[51],10:[56],11:[62,64,65],12:[67,68],13:[69,75],14:[71],
 15:[72,73],16:[78,80,82],17:[83],18:[87],19:[92,93,94],20:[98,99],
 21:[105,106,107,108,109,110],22:[],23:[101,102],24:[104,111]}
for sec,nums in proofmap.items():
 for n in nums:
  event(f'CL-SA19-{n:03d}','independent re-proof',
        f'computations.md §{sec}: independent derivation of the precisely stated implication/model, retaining all explicit coefficient/category and hypothesis limits. This does not resolve an undefined handwritten category or provide an ink decision.')
event('SA19-3','independent re-proof','computations.md §22: prime-valuation proof for Q× and Z[1/6]×; examples belong to the earlier run, not the manuscript.')
for n,sec in [(8,2),(56,10),(67,12),(68,12),(71,14),(87,18),(93,19),(98,20),(99,20),(106,21)]:
 event(f'CL-SA19-{n:03d}','computation or formal certificate',
       f'scripts/calculations.py and outputs/calculations.txt, corresponding to computations.md §{sec}. Exact finite calculations passed; finite examples are explicitly not proofs of infinite categorical statements.')
for n,refined,proof in [(71,'CL-SA19-070','supersingular elliptic curve with full E[3] rank9 but trivial étale3 quotient'),
                         (83,'CL-SA19-082','P1/A1 example with degree-zero support0 and open cohomologyZ/l'),
                         (93,'CL-SA19-092','R⊕k example: lengths2≥1 and nonzero t-torsion')]:
 event(f'CL-SA19-{n:03d}','refuted, with refined statement id',
       'Literal interpretation refuted by '+proof+'; refinement='+refined+'. Every stated model hypothesis checked in computations.md. No manuscript emendation is made.')
for key,part in refs.items():
 ann=re.search(r'annotation=\{(.*?)\}\s*\n\}',part,re.S)
 text=ann.group(1) if ann else 'Opened source/metadata as stated in bibliography; no unrecorded theorem verification claimed.'
 typ='carried as background without fault found' if key in ['MilneBibliography','AtiyahBibliography'] else 'used and rechecked in this run'
 event(key,typ,text)
for p in problems:
 event(p['id'],'used and rechecked in this run',
       'Merged author question(s) checked against the occurrences and opened primary sources: '+p['state_of_art']+' No unsupported reason for abandonment or proof of present openness inferred.')
event('CL-SA19-680','targeted proof check','Cross-review of root proofs_C16.md: Frobenius shifts and the covariant Ext¹(Ga,alpha_p) argument verified. Found the missing Ext² term in the contravariant alpha_p→Ga argument; parent corrected the proof to invoke its independently opened one-dimensionality theorem. This child did not independently open that additional source. See cross_review.md.')
event('CL-SA19-681','targeted proof check','Cross-review: Hom(Ga,A)=0 and pGa=0 give Ext¹(Ga,A[p])≅Ext¹(Ga,A) by the stated long exact sequence; no alpha_p-source or mu_p-source conclusion inferred.')
event('CL-SA19-652','targeted proof check','Cross-review: finite Dieudonne extension has F(M),V(M) in the kernel, killed there by both operators, hence pM=FV(M)=0 before choosing a k-basis. Labelled alpha_p self-extensions give additive k²; not middle-group isomorphism classes. See cross_review.md.')
with (B/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

idx=json.loads((W/'source_audit/page_index.json').read_text())
coverage=[]
companion={'16':{19,21,23,28,30,37,39,41,52,56},'44':set(range(2,10)),
           '54':set(range(2,8)),'47':set(range(2,9))|{11}}
rootfaces={89,90,92,93,143,144,145,161,162}
for p in idx:
 own=p['file'].endswith('MPL_43_094-142_transcription.tex')
 cross=p['cote'] in companion and int(p['scan']) in companion[p['cote']]
 codex=p['cote']=='43' and int(p['scan']) in rootfaces and '/codex/' in p['file']
 if own or cross or codex:
  coverage.append(dict(cote=p['cote'],scan=p['scan'],source=p['file'],line_start=p['line_start'],line_end=p['line_end'],
                       reading='complete face read; actual passages, not keyword verdict',
                       purpose='assigned full audit' if own else 'two-endpoint link verification',date=DATE))
with (B/'reading_coverage.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['cote','scan','source','line_start','line_end','reading','purpose','date'],delimiter='\t');w.writeheader();w.writerows(coverage)

assert len(entries)==89 and len({r['entry_id'] for r in entries})==89
assert {r['entry_id'] for r in entries}=={f'MPL_43_094-142#{n}' for n in range(1,90)}
assert all(r['item_id'] in {i['id'] for i in items} for r in entries)
assert all(set(c['refs'])<=set(refs) for c in claims)
assert all(set(p['refs'])<=set(refs) for p in problems)
assert sum(r['purpose']=='assigned full audit' for r in coverage)==46
assert all(r['verdict'] and r['reason'] for r in entries)
counts=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),
            verdicts=dict(Counter(r['verdict'] for r in entries)),item_kinds=dict(Counter(i['kind'] for i in items)),
            claim_classes=dict(Counter(c['class'] for c in claims)),claim_statuses=dict(Counter(c['status_on_pages'] for c in claims)),
            readings=len(list(csv.DictReader((B/'readings.tsv').open(),delimiter='\t'))),
            links=len(list(csv.DictReader((B/'links.tsv').open(),delimiter='\t'))),references=len(refs),
            check_events=len(events),research_rows=len(log),complete_faces_read=len(coverage),assigned_faces_read=46)
(B/'outputs/audit_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
print('Coverage, referential-integrity and entry-bijection checks passed. Judgments were hand-authored; validation does not replace reading.')
