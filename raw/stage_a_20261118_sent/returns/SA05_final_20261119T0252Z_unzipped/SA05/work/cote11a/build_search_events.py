"""Search coverage and actual check events; no claim verdict is inferred from a heading."""
import csv,json,pathlib
R=pathlib.Path('SA05/work/cote11a');date='2026-11-19';who='GPT-6 Astra Pro; inherited parent effort; SA05/cote11a'
claims=json.loads((R/'claims.json').read_text());items=json.loads((R/'items.json').read_text());refs=json.loads((R/'references_metadata.json').read_text());refmap={r['key']:r for r in refs}
queries=json.loads((R/'web/search_queries.json').read_text());queries.update(json.loads((R/'web/search_queries_extra.json').read_text()))
extra={
 'S11A-25':'Grothendieck algèbres bivariantes simpliciales jauge Hua',
 'S11A-26':'site:zbmath.org Grothendieck correspondence Poincare Frobenius algebra motives',
 'S11A-27':'site:arxiv.org "bivariant" "Frobenius" algebra finite sets',
 'S11A-28':'site:mathoverflow.net Frobenius algebra finite sets diagonal correspondence',
 'S11A-29':'"EGA" "7.5.1" "propriété" "local"',
 'S11A-30':'"EGA" "7.9.8" "intègre"',
 'S11A-31':'SGA3 tome2 ExposéIX4.2 nilpotent densité schématique pdf',
 'S11A-32':'site:webusers.imj-prg.fr EGAII.pdf "4.5.2"',
}
# These exact query strings were executed in the earlier saved batches web_a31,a38,a29,a34.
queries.update({k:{'q':v} for k,v in extra.items()})
details={
1:('Search service system2; Stacks primary pages',['Stacks0FFZ','Stacks0FGS'],'Exact correspondence identities found and opened. Variance and even-Chow hypotheses compared, not merely topic matched.','web_s01.json'),
2:('Search service system2; Stacks primary pages',['Stacks0FG9'],'Object, Hom and Karoubian constructions opened; distinguishes completion from the manuscript kernel category.','web_s01.json'),
3:('Search service system2; Kock author/book sources',['Kock2003','Stacks0FGS','Hua2026'],'Exact Frobenius statement and finite-set presentation opened. No exact completed nonadditive theory located.','web_s01.json'),
4:('Search service system2; arXiv; backward Hironaka bibliography',['EncinasHauser2002','Stacks0AZC','Kleiman1968','Hironaka1964Lead'],'Found primary characteristic-zero resolution formulation; original Hironaka proof not opened. Pushforward degree rule checked separately.','web_s01.json'),
5:('Search service system2; full GIT mirror; publisher metadata',['GIT1982','GIT1994Metadata'],'Matching exact GIT statements and attached continuations read. Main3.6 OCR incomplete; Appendix proof read.','web_s02.json'),
6:('Search service system2; arXiv; Annals',['Kempf1978','RamosCuevas2013','BateMartinRoehrle2010'],'Exact optimality and quasi-state theorems compared; subcomplex result verified at abstract extent only.','web_s02.json'),
7:('Search service system2; arXiv primary SGA1 text',['SGA1'],'ExposéVIII exact descent results opened; bibliographic shorthand resolved.','web_s02.json'),
8:('Search service system2; Numdam and primary EGA PDFs',['EGAIV3','SGA3II'],'This repeat query gave limited exact hits; earlier direct/search-followed PDF retrieval opened exact11.9/11.10 statements. No broad metadata claim substitutes for those passages.','web_s02.json; web_a24.json; web_a25.json; web_a26.json'),
9:('Search service system2; arXiv; EGA; Stacks',['Murayama2022','EGAIV2','Stacks0BPZ'],'Repeat query coverage poor; prior primary Murayama PDF was opened atCor4.1/Remark4.2. Fiberwise and total-space integrality separated; literal nilpotents refuted. Final backward check opened EGA6.5.5(ii), whose algebraic-node witness differs from the draft complete-real witness.','web_s03.json; web_a19.json; web_a20.json; web_a21.json; web_a48.json; web_a49.json'),
10:('Search service system2; arXiv; EGA backward references',['Murayama2022','EGAIV2','MOFormalFibersLead'],'Modern exact permanence hypotheses opened. Original EGA7.5/7.9 access incomplete; Murayama backward references followed to available primary material.','web_s03.json; web_a19.json; web_a22.json; web_a23.json; web_a42.json'),
11:('Search service system2; Numdam EGAIV2',['EGAIV2'],'Repeat title query weak; exact indexed PDF3.4.1–3.4.6 separately opened and compared with the cancelled fragment.','web_s03.json; web_a20.json; web_a21.json'),
12:('Search service system2; exact French formalism search',['Hua2026','Kock2003','Stacks0FFZ'],'No broad completion of the exact stable-system/nonadditive formalism found. A precise restricted special-object theorem was found throughS11A-25. Negative search is bounded, not absence proof.','web_s03.json; web_a31.json'),
13:('Search service system2; original French SGA3/EGA',['SGA3II','EGAIV3'],'Direct primary PDF exact lemma opened. Local freeness of successive ideal layers found explicitly; draft ordinary lemma refuted.','web_s04.json; web_a29.json; web_a30.json'),
14:('Search service system2; primary papers and author bibliography',['Grothendieck1969','Kleiman1968','GrothBibliography'],'Exact published letter definitions, lowering convention and inverse-algebraicity statements opened. Missing cote16 endpoint prevents archive dictionary verification.','web_s04.json; web_a10.json; web_a11.json; web_a12.json; web_a31.json'),
15:('Search service system2; Numdam primary Oda paper',['Oda1969'],'Corollaries5.11–5.12 and dissertation-date footnote read; no all-degree or arbitrary-base extension inferred.','web_s04.json; web_a41.json; web_a43.json'),
16:('Search service system2; Milne author notes; Stacks',['Milne2013','Stacks0FHA','Kleiman1968','SGA5Lead'],'Exact construction and compatibility statement opened. Milne omits the long proof; SGA5 desired section was not retrieved.','web_s04.json; web_a17.json; web_a18.json'),
17:('Search service system1; exact bivariant-monoid and kernel search',['Hua2026','Kock2003','Stacks0FYP'],'No verified exact completion of the manuscript monoid proposal found. Broad kernel results are not substituted; the explicit K-class comparison was followed byS11A-21.','web_s05.json'),
18:('Search service system1; Hexagon exact identifier',['Hua2026','HuaPinnedAppendix','HuaPinnedLean'],'This repeat identifier query missed the paper. EarlierS11A-25 found it and both primary versions were actually opened. Pinned GitHub source remained unavailable; Lean not run.','web_s05.json; web_a31.json; web_a32.json; web_a33.json'),
19:('Search service system1; primary EGAII PDF',['EGAII1961'],'Repeat combined query poor; earlier exact search plus indexed find/open retrieved4.5.2 and4.6.13 with hypotheses/proofs.','web_s05.json; web_a34.json; web_a35.json; web_a36.json; web_a37.json'),
20:('Search service system1; zbMATH Open',['Oda1969','OdaZblLead'],'Search attempted; direct zbMATH record returned403. Numdam original supplies the theorem evidence. No review text was read.','web_s05.json'),
21:('Search service system2; Stacks primary pages',['Stacks0FYP','Stacks0G0F'],'Exact perfect-kernel preservation and composition results opened; formal passage toK0 checked under explicit hypotheses.','web_s06.json; web_a44.json'),
22:('Search service system1; Springer official metadata',['GIT1994Metadata','GIT1982'],'Verified authors and second-edition1982 chronology; theorem verification remains the separately opened book text.','web_s07.json'),
23:('Search service system1; Numdam bibliographic search',['SGA3II'],'This bibliographic query did not yield a useful exact primary metadata page. Earlier original French PDF supplied the lemma.','web_s07.json'),
24:('Search service system1; SGA lemma exact-term search',['SGA3II'],'Returned English translations; these were not used as primary theorem authority. Exact French source had already been opened.','web_s07.json'),
25:('Search service system2; exact formalism and author search',['Hua2026'],'Found the November2026 primary v1/v2 paper, then opened exact theorem/proof and exclusions.','web_a31.json; web_a32.json; web_a33.json'),
26:('Search service system2; zbMATH-targeted search',['Kock2003','Hua2026'],'No exact usable zbMATH theorem match for this manuscript formalism. Recorded as a search-coverage limit; exact primary alternatives opened.','web_a31.json'),
27:('Search service system2; arXiv-targeted search',['Kock2003','Hua2026'],'No exact all-degree or nonadditive theorem match found. Restricted paper comparison and textbook primary formalism supply only their stated scope.','web_a31.json'),
28:('Search service system2; MathOverflow leads',['MOFrobeniusLead','Kock2003'],'Classification/trace discussion opened as a lead; no result is certified from forum discussion.','web_a31.json; web_a32.json'),
29:('Search service system1; EGA exact-section search',['EGAIV2','Murayama2022'],'No exact accessible original7.5.1 text retrieved. Opened modern theorem gives a bounded comparison, not verbatim identity.','web_a38.json'),
30:('Search service system1; EGA backward theorem search',['EGAIV2','Murayama2022'],'Relevant backward leads found, but original7.9.8 not opened beyond indexed access limit. Exact modernCor4.1 and its limitations retained.','web_a38.json'),
31:('Search service system1; primary SGA3 PDF',['SGA3II'],'Found and opened exact French LemmaIX4.2 and proof; essential local-freeness hypothesis retained.','web_a29.json; web_a30.json'),
32:('Search service system1; primary EGAII PDF',['EGAII1961'],'Found exact primary PDF and used indexed find/open to retrieve4.5.2 and4.6.13.','web_a34.json; web_a35.json; web_a36.json; web_a37.json')}
# Additional searches are attached to the exact families actually investigated.
for c in claims:
 cid=int(c['id'].split('C')[-1])
 additions=[]
 if 1001<=cid<=1036 or cid in [1084,1085,1087]: additions+=['S11A-26','S11A-27','S11A-28']
 if cid in [1010,1011,1021,1022,1023,1024,1027,1029,1030,1031,1032,1033,1034,1035]: additions+=['S11A-25']
 if 1037<=cid<=1059:additions+=['S11A-22']
 if cid in [1062,1063,1065,1066,1067,1090]:additions+=['S11A-29','S11A-30']
 if cid in [1077,1089]:additions+=['S11A-23','S11A-24','S11A-31']
 if cid in [1044,1059]:additions+=['S11A-32']
 c['search_ids']=list(dict.fromkeys(c['search_ids']+additions))
(R/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
searchrows=[]
for sid,q in sorted(queries.items()):
 n=int(sid.split('-')[-1]);venue,keys,outcome,logs=details[n]
 ids=[c['id'] for c in claims if sid in c['search_ids']]
 searchrows.append(dict(search_id=sid,date=date,venue=venue,query=q['q'],claim_ids=';'.join(ids),outcome=outcome,opened_refs=';'.join(keys),opened_urls=';'.join(refmap[k]['url'] for k in keys if refmap[k]['note']=='verified'),verification_extent=' | '.join(k+': '+refmap[k]['extent']+' '+refmap[k]['limitations'] for k in keys),raw_log=logs))
events=[]
def event(sid,typ,outcome):events.append(dict(statement_id=sid,date=date,who=who,type=typ,outcome=outcome))
for i in items:event(i['id'],'carried as background without fault found','Source provenance and entry-to-passage comparison for this refined item; not a mathematical proof. '+i['check_reason'])
refuted={1016,1024,1032,1062,1077}
for c in claims:
 cid=int(c['id'].split('C')[-1])
 if cid not in refuted:event(c['id'],'carried as background without fault found','Exact statement and attribution reviewed; fate searched via '+','.join(c['search_ids'])+'. This event alone is not a proof. '+c['fate'])
for r in refs:
 typ='used and rechecked in this run' if r['note']=='verified' and r['key'] not in ['GrothBibliography','GIT1994Metadata','SGA5Lead','RamosCuevas2013','MOFrobeniusLead','MOFormalFibersLead'] else 'carried as background without fault found'
 event(r['key'],typ,r['extent']+' '+r['limitations']+(' Access unavailable; no theorem adopted.' if r['note']=='unverified' else ''))
proofgroups=[
 ([1001,1002,1003,1004,1006,1008],'§1','Conditional even/ungraded named-projection proof under the stated product/graph/diagonal exchange axioms.'),
 ([1009],'§1','Trace-pairing proof with central/even kernel; arbitrary graded reorderings not silently ignored.'),
 ([1013,1014,1015,1018,1033],'§6','Closure, converse via graph actions and intersections checked, conditional on the named symmetry and corrected-target assumptions.'),
 ([1019,1020,1021,1025,1026,1027,1028,1030],'§2','Pairing proof, degree/parity identity or commutative product universal property with exact finite-projective and trace hypotheses.'),
 ([1031],'§4','Restricted special commutative reconstruction proved with multiplicative gauges; no unrestricted theorem.'),
 ([1034],'§5','Comultiplication/counit identities follow by adjoints of multiplication/unit under perfect pairings.'),
 ([1082,1083,1085],'§7','General elementary inverse, lowering-string and block-corner identities re-proved; no absent archive witness certified.'),
 ([1040],'§8','Termwise finite-weight maximum inequality independently re-proved.'),
 ([1073],'§9','DVR valuation and localization show failure to preserve an infinite zero intersection.'),
 ([1087],'§10','Formal passage of the explicitly defined exact perfect-kernel functor to K0, with proper-flat-finite-presentation hypothesis.')]
for ids,section,desc in proofgroups:
 for cid in ids:event(f'SA05-C{cid}','independent re-proof','proof_checks.md '+section+': '+desc)
targeted={1005:'§1 tensor/base-change proof, even convention only',1007:'§1 diagram routes reduced to graph action and transposition, not a formal certificate',1017:'§6 resolution-to-cycle-generation argument; resolution theorem itself used, not reproved',1022:'§2 diagnosed withdrawn all-degree formula; only convention-specific parity checked',1023:'§2 tensor-square adjoint calculation',1035:'§4–5 restricted full-faithfulness comparison; broad degenerate theory not proved',1036:'§5 cohomological model; no A^0=k inferred',1043:'§8 nonempty-set qualification and rational-bound argument, not proof of rational attainment',1044:'§8 uniform numerical inequality and EGA relative twist hypotheses',1049:'§8 negative-parallel-ray obstruction in character separation',1051:'finite root/weight proof structure compared with read GIT passage',1052:'Kempf Lemma5 and read weight/parabolic setup; finite tests only supplement',1058:'attached cone/greedy-flag continuation and independent-set Appendix proof compared',1060:'published support-induction passage compared; missing draft hypotheses retained',1064:'§9 complete real node and finite étale complexification counterexample',1067:'§9 domain-ascent exclusion compared to Murayama Remark4.2',1089:'§9 tensoring a jointly injective family with locally free nilpotent layers; published induction checked'}
for cid,desc in targeted.items():event(f'SA05-C{cid}','targeted proof check',desc+'. See proof_checks.md/reference_checks.tsv for exact extent.')
calc={1001:'dual-number convolution sample',1002:'dual-number diagonal identity',1004:'symbolic kernel matrix action',1020:'all8 parity cases',1021:'dual-number tensor pairing',1022:'64 parity cases under explicit tensor-trace convention',1025:'all8 projection-sign parity cases',1027:'scalar-gauge identities',1028:'symbolic degree equation',1032:'56 set maps and1618 composition/naturality checks for sizes≤3, plus general proof in prose',1034:'dual-number counits/coassociativity/cocommutativity',1040:'49 finite weight examples; general proof separate',1044:'27 exact rational uniform bounds',1051:'625 two-weight samples, not universal root proof',1052:'625 finite parabolic-weight samples only',1064:'exact complex factorization',1077:'Groebner reductions show nonzero ε killed after inverting x',1082:'rational matrices and Cayley–Hamilton inverse',1083:'four lowering identities for m=0,…,15; general coefficient proof separate',1085:'symbolic2×2 corner'}
for cid,desc in calc.items():event(f'SA05-C{cid}','computation or formal certificate','Executed check_calculations.py; saved calculation_output.txt: '+desc+'. This is exact arithmetic, not a Lean certificate.')
for cid,new,desc in [
 (1016,'SA05-C1017','At a point, single f_*1 values do not contain−1; take the additive span.'),
 (1024,'SA05-C1023','All-isomorphism scalar-gauge Cartesian square has exchange1≠2; tensor-square/explicit-exchange refinement.'),
 (1032,'SA05-C1031','Partition power system has singleton dimension1 and two-point dimension2; specialness and multiplicative gauges are needed.'),
 (1062,'SA05-C1090','Identity on Q[ε]/ε² meets the literal unreduced hypotheses; intended normal-base question is separate.'),
 (1077,'SA05-C1089','S=Spec Q[x,ε]/(ε²,xε), Z=D(x) meets ordinary draft hypotheses and fails density; locally free nilpotent layers supply the published refinement.')]:
 event(f'SA05-C{cid}',"refuted, with the refined statement's id",'Refined statement: '+new+'. '+desc+' Every stated counterexample hypothesis is checked in proof_checks.md.')
event('SA05-1039',"refuted, with the refined statement's id",'Refined statement: SA05-C1043. The literal “every subsetS” existential attainment assertion fails for S=∅; the qualified claim requires nonemptyS and direction space.')

def write(name,rows,fields):
 with (R/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
write('search_log.tsv',searchrows,['search_id','date','venue','query','claim_ids','outcome','opened_refs','opened_urls','verification_extent','raw_log'])
write('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
print(f'Search rows={len(searchrows)}; searched claims={sum(bool(c["search_ids"]) for c in claims)}; check events={len(events)}')
