"""Final explicit corrections and cross-part links agreed with the reading owner."""
import json,csv,pathlib,hashlib
B=pathlib.Path(__file__).resolve().parents[1]
cs=json.loads((B/'claims.json').read_text())
cs[73]['refs']=['PE_Lojasiewicz1964','PE_Goresky1978']
cs[73]['fate']='Łojasiewicz1964 §3 Theorems1–2, printedpp463–464, gives semianalytic triangulation. Goresky1978 §5, printedp199, gives triangulation for abstract stratified objects. Together with the standard compatible Whitney/Thom–Mather stratification input for compact complex analytic spaces, explicitly carried as background, this gives finite generation. Neither a Euclidean triangulation theorem alone nor the word compact is the whole argument.'
cs[73]['present_status']='As of November2026: '+cs[73]['fate']
cs[84]['class']='C'
cs[84]['fate']='Kresch–Mathur Theorem11.11 supplies characteristic-zero Picard ML for proper algebraic schemes over a complete noetherian local base. Exposé182 §3 Theorem3 and Stacks088E give coherent formal existence for a proper algebraic model. The abstract proper formal scheme formulation additionally requires ML in that setting and construction of a compatible ample formal line bundle; the opened theorem for an already algebraic model does not alone settle that quantifier.'
cs[84]['present_status']='As of November2026: '+cs[84]['fate']
(B/'claims.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n')
rs=json.loads((B/'references.json').read_text())
for r in rs:
 if r['key']=='PE_Stacks009E':r['checked_locator']='§6.29 introductory assertion(2); Lemma6.29.1 is about filtered colimits'
 if r['key']=='PE_Stacks01AJ':r['checked_locator']='Lemma17.3.3(1); proof cites the adjunction inLemma6.26.2'
(B/'references.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n')
with(B/'references.bib').open('w')as f:
 for r in rs:
  f.write('@'+r['type']+'{'+r['key']+',\n')
  for k,v in r.items():
   if k not in['type','key','checked_locator','verification_scope']:f.write('  '+k+' = {'+v.replace('&','\\&')+'},\n')
  f.write('  annote = {'+r['checked_locator']+'. '+r['verification_scope']+'}\n}\n\n')
links=list(csv.DictReader((B/'links.tsv').open(),delimiter='\t'))
cross=[
('SA14-1–3;57:91–94,227–270','SA14-201–202;57:294,297,310','Both note packages distinguish the absent Fourier map from nearby extension and vanishing calculations.','MPL_57_089-132#1;MPL_57_089-132#2;MPL_57_226-270#1;MPL_57_226-270#2'),
('SA14-14;C-SA14-008–009;57:94','SA14-203;C-SA14-210–212;57:283–286','Product rigidification and the Poincaré mixed component are related. The later rigidification statement does not automatically compute the earlier omitted mixed class.','MPL_57_089-132#13;MPL_57_089-132#14;MPL_57_089-132#15;MPL_57_089-132#16'),
('SA14-4–6;57:91,126–131,227–270','SA14-204–206;57:275–277,283–286,291–292,306,313','Both packets contain bounded ordinary-Picard comparisons with the external higher-cycle programme. The manuscript endpoints are checked; cote44 remains unavailable.','MPL_57_089-132#3;MPL_57_089-132#4;MPL_57_089-132#5;MPL_57_226-270#3;MPL_57_226-270#4;MPL_57_226-270#5'),
('SA14-7;57:94,260,266','SA14-207;C-SA14-209;57:280–281','Lifting an ample class and rational ample rays do not prove positivity of the particular external middle-Jacobian correspondence.','MPL_57_089-132#6;MPL_57_226-270#6'),
('SA14-8;57:91–101,263','SA14-208;57:289–290,314–315','Neither local endpoint supplies the external Néron–Tate height formula. This is a checked negative concordance within the supplied archive.','MPL_57_089-132#7;MPL_57_226-270#7'),
('SA14-9,17,19;57:97–103','SA14-209;C-SA14-250;57:309(h),lines830–837','Later hyperplane questions join the earlier Picard table; dimensions and qualifiers remain explicit. The all-cycle version at cote44 is not checked.','MPL_57_089-132#8;MPL_57_089-132#20;MPL_57_089-132#21;MPL_57_089-132#22;MPL_57_226-270#8'),
('SA14-10;57:97,100,235–245','SA14-210;C-SA14-205,265,266;57:275,314–315','Later divisor-level numerical/tau equivalence is a closer match than the early infinitesimal Picard tower; it does not establish an all-codimension theorem.','MPL_57_089-132#9;MPL_57_226-270#9'),
('SA14-46,49,67,69;C-SA14-070–073,096–097;57:227–231,254–268','SA14-212–213;C-SA14-202–204;MP-SA14-201–203;57:272,lines17–39','Three completion questions continue the letter’s comparison programme. Both parts independently found the exact punctured henselian Elkik corollary; arbitrary opens and full formal comparison remain distinct.','MPL_57_226-270#11;MPL_57_226-270#12;MPL_57_226-270#13;MPL_57_226-270#19;MPL_57_226-270#20;MPL_57_226-270#21;MPL_57_226-270#51;MPL_57_226-270#54;MPL_57_226-270#55;MPL_57_226-270#56;MPL_57_226-270#58')]
links=[l for l in links if not l['evidence'].startswith('Cross-part check:')]
for fr,to,what,nids in cross:links.append(dict(kind='folder',**{'from':fr,'to':to},what=what,evidence='Cross-part check: early endpoint read by picard_early; later endpoint fully read and exact IDs confirmed by picard_lefschetz on2026-11-19. Each part retains its own source/claim check records; no external cote44/47/Hua endpoint is thereby certified.',note_ids=nids))
with(B/'links.tsv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(links)
leads=list(csv.DictReader((B/'project_leads.tsv').open(),delimiter='\t'))
for l in leads:
 if l['run_names'].startswith('SN P02/P03'):l['evidence']='The current archive endpoints57:271–274 were checked bypicard_lefschetz; see the separate folder link toSA14-212–213. The named older context note file,Hua andRS endpoints remain unavailable and quarantined.'
with(B/'project_leads.tsv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids','run_names'],delimiter='\t');w.writeheader();w.writerows(leads)
p=pathlib.Path('/tmp/SA14_Goresky1978.pdf')
if p.exists():(B/'outputs/Goresky_source_receipt.json').write_text(json.dumps(dict(url='https://www.math.ias.edu/~goresky/pdf/triangulations.pdf',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,read_pages='printed193,197,199',retrieval='curl with ordinary browser User-Agent after urllib403; primary author-hosted PDF',archive_policy='Whole external PDF kept outside deliverables; read-page evidence and source receipt retained.'),indent=2)+'\n')
print(json.dumps({'claims':len(cs),'references':len(rs),'checked_links':len(links),'quarantined_leads':len(leads),'class85':'C, abstract formal quantifier explicitly limited'}))
