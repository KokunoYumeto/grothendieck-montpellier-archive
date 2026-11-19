#!/usr/bin/env python3
"""Bibliographic records and concise, reproducible search trace; no copied articles."""
import json,re,csv
from pathlib import Path
P=Path(__file__).resolve().parent
R=[]
def b(key,typ,title,author,year,url,locator,searches,**fields):
    d=dict(key=key,type=typ,title=title,author=author,year=year,url=url,note='verified',annote='Opened in this run. '+locator,**fields);R.append((d,searches))
b('BorelSerre1958','article','Le théorème de Riemann-Roch','Armand Borel and Jean-Pierre Serre','1958','https://www.numdam.org/article/BSMF_1958__86__97_0.pdf','Intro identifies Princeton autumn1957; §§2–5, §7 p113, §17 Proposition16. The article presents Grothendieck’s theorem; publication authorship is Borel and Serre.',[1,2,6,7,8,9,10],journal='Bulletin de la Société Mathématique de France',volume='86',pages='97--136',doi='10.24033/bsmf.1500')
b('GrothendieckChern1958','article','La théorie des classes de Chern','Alexander Grothendieck','1958','https://www.numdam.org/article/BSMF_1958__86__137_0.pdf','§4,2°, pp147–149. Received1June1958, which is not asserted as first circulation.',[4,6],journal='Bulletin de la Société Mathématique de France',volume='86',pages='137--154')
b('GrothendieckRRR1957','incollection','Classes de faisceaux et théorème de Riemann-Roch','Alexander Grothendieck','1971','https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf','SGA6 Exposé0 Appendix§3, pp28–32, formulas1.14–1.30 andProp1.2. Primary introductionpVIII identifies the mimeographed Princeton1957 report; 1971 is the reprint date.',[1,3,4,9,11],booktitle='Théorie des intersections et théorème de Riemann-Roch (SGA6)',series='Lecture Notes in Mathematics',volume='225',publisher='Springer')
b('SGA6','book','Théorie des intersections et théorème de Riemann-Roch (SGA6)','Pierre Berthelot and Alexander Grothendieck and Luc Illusie','1971','https://link.springer.com/book/10.1007/BFb0066283','Seminar1966–67. Original scanned edition separately downloaded and visually read, including introductionpVIII and Exposé0 pp1–3. Editors listed in author field for compact interoperability.',[1,3,4,9,11,12],series='Lecture Notes in Mathematics',volume='225',publisher='Springer',doi='10.1007/BFb0066283')
b('SGA6V','incollection','Généralités sur les lambda-anneaux','Pierre Berthelot','1971','https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf','ExposéV§6, especially6.5.3,6.6.1,6.8–6.14, printedpp349–359; original scans read, not an unverified web reconstruction. Printed authorship is Berthelot.',[1,3,4,9,11,12,13],booktitle='SGA6',series='Lecture Notes in Mathematics',volume='225',pages='297--364',publisher='Springer')
b('SGA4VII','incollection','Site et topos étales d’un schéma','Alexander Grothendieck','1972','https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf','ExposéVII5.11–5.13, printedpp363–364, exact original pages inspected. Seminar1963–64; physicalPDF page=printed page+2 in this copy.',[6],booktitle='Théorie des topos et cohomologie étale des schémas, tome2 (SGA4)',series='Lecture Notes in Mathematics',volume='270',publisher='Springer')
b('SGA4VIII','incollection','Foncteurs fibres, supports, étude cohomologique des morphismes finis','Alexander Grothendieck','1972','https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf','ExposéVIII1.1–1.2, printedpp367–368; authorship onp366 and complete integral/surjective/radicial hypotheses visually checked.',[6],booktitle='Théorie des topos et cohomologie étale des schémas, tome2 (SGA4)',series='Lecture Notes in Mathematics',volume='270',publisher='Springer')
b('PedriniWeibel1994','article','Divisibility in the Chow group of zero-cycles on a singular surface','Claudio Pedrini and Charles Weibel','1994','https://numdam.org/item/AST_1994__226__371_0/','AppendixA, p404: rank/Picard description in dimension≤1, with backward reference to Thomason–Trobaugh10.8. OriginalPDF appendix visually read.',[12],journal='Astérisque',volume='226',pages='371--409')
b('Mackall2020','article','Universal additive Chern classes and a GRR-type theorem','Eoin Mackall','2020','https://arxiv.org/pdf/2006.14664','Proposition2.1 andTheorem4.1 checked. arXivv1 submitted25June2020; journal publication15October2020. The all-bundle/projective-bundle universal problem differs from the selected-family manuscript problem.',[1,2,3,4,7,10],journal='Journal of Algebra',volume='560',pages='1173--1189',doi='10.1016/j.jalgebra.2020.06.018',eprint='2006.14664',archivePrefix='arXiv')
b('AlonsoEtAl2023','article','Relative perfect complexes','Leovigildo Alonso Tarrío and Ana Jeremías López and Fernando Sancho de Salas','2023','https://arxiv.org/html/2112.09680v4','Prop3.5,Prop3.11,Cor4.2,Th6.1,§6.9/Prop6.10 opened. First arXiv17December2021; v4 dated2May2023; journal2023.',[2,3,4,6,11],journal='Mathematische Zeitschrift',volume='304',pages='Paper42',doi='10.1007/s00209-023-03294-7',eprint='2112.09680',archivePrefix='arXiv')
b('Quillen1973','incollection','Higher algebraic K-theory: I','Daniel Quillen','1973','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf','§5 Theorem4, printedp104. The introduction explicitly calls the Grothendieck-group cases already well known; no first-priority date inferred.',[8,9],booktitle='Algebraic K-theory I',series='Lecture Notes in Mathematics',volume='341',pages='77--139',publisher='Springer')
b('Serre1977','book','Linear Representations of Finite Groups','Jean-Pierre Serre','1977','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf','Primary PDF downloaded after web-reader size rejection. §§7.1–7.3, pp54–59:Prop18,Prop19,projection formulaRemark3,andProp22 proof.',[7,8],series='Graduate Texts in Mathematics',volume='42',publisher='Springer')
b('Atiyah1966','article','Power operations in K-theory','Michael F. Atiyah','1966','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahk.pdf','Article reprinted in the1967 K-Theory volume, §§1–3 inspected. Received10January1966 is a receipt date, not a verified circulation date. Complex topological scope retained.',[7,8,9],journal='Quarterly Journal of Mathematics',volume='17',pages='165--193',doi='10.1093/qmath/17.1.165')
b('BFM1975','article','Riemann-Roch for singular varieties','Paul Baum and William Fulton and Robert MacPherson','1975','https://www.numdam.org/article/PMIHES_1975__45__101_0.pdf','§0.1–0.2,I§6,II§1–3,IV§5–6. Received20August1974; publication28December1975. These are not asserted as first circulation.',[5,6,7,8,10,11,12,13],journal='Publications Mathématiques de l’IHÉS',volume='45',pages='101--145')
b('FultonGillet1983','article','Riemann-Roch for general algebraic varieties','William Fulton and Henri Gillet','1983','https://www.numdam.org/article/BSMF_1983__111__287_0.pdf','p288 Riemann–Roch Theorem, especiallyproperty(3); separated finite-type schemes over an arbitrary field, proper maps. Received14December1982; publication1983.',[12,13],journal='Bulletin de la Société Mathématique de France',volume='111',pages='287--300')
b('Ram2011','misc','Bilinear, sesquilinear and quadratic forms','Arun Ram','2011','https://math.soimeme.org/~arunram/Notes/sesquilinearContent.html','Definitions of bimodule sesquilinearity and adjoint/matrix maps. Page says last update11June2011. This is a modern convention source, not identification of the reused typed leaves.',[12,13])
b('GrothBibliography2026','misc','Published Works','CSG Istituto Grothendieck','2026','https://csg.igrothendieck.org/published-works/','Bibliographic discovery source checked19November2026, especiallyCSG40 andSGA6. Mathematical claims checked in the original works.',[6,7])
for tag,title,loc,searches in [
 ('0955','Derived torsion','Lemma47.10.1; noetherian ring required.',[5,6]),
 ('06UP','Triangulated subcategories of the derived category','Lemma13.17.4; applied to finite modules inside the torsion category, not torsion inside all modules.',[5,6]),
 ('08E0','Derived category of coherent modules','Lemma36.11.8; regular schemes, quasi-compact converse.',[5,11]),
 ('0FET','Localized Chern characters','Remark42.56.11; supported perfectK0 to a rational bivariant target; base assumptions retained.',[4,5]),
 ('02O1','Higher direct images along projective morphisms','Lemma30.16.2, relative Serre vanishing.',[10]),
 ('0BDM','Applications of cohomology and base change','Lemmas36.32.1–36.32.4, especiallyflatness and local-freeness hypotheses.',[10,11]),
 ('0AYQ','Degrees on curves','Definition33.44.1 and degree/Euler-characteristic conventions for proper curves.',[10]),
 ('0C44','Normalization of one dimensional schemes','Lemmas33.41.1–33.41.2; normalization and finite defect on reducedNagata curves.',[7,8]),
 ('0307','Integral closure commutes with localization','Lemma10.36.11; denominator-clearing proof read.',[7,8]),
 ('090P','Valuation rings','Lemma10.50.11; normal-domain intersection in its fraction field.',[7,8]),
 ('0AFV','Unique factorization domains are normal','Lemma10.120.11.',[7]),
 ('0BD2','Norms','Lemma31.18.6; finite locally free norm as determinant, arbitrary base change.',[10,11])]:
    b('Stacks'+tag,'misc',title,'The Stacks Project Authors','2026','https://stacks.math.columbia.edu/tag/'+tag,loc+' Checked19November2026; stable tag is authoritative if section numbering changes.',searches)
for key,title,url,date in [
 ('MO108409','Lambda-ring structure defined for a graded ring in Fulton–Lang’s book','https://mathoverflow.net/questions/108409/lambda-ring-structure-defined-for-a-graded-ring-in-fulton-langs-book','2012'),
 ('MO132982','The graded pieces of the gamma filtration of Quillen K-theory and Chow groups','https://mathoverflow.net/questions/132982/the-graded-pieces-of-the-gamma-filtration-of-quillen-k-theory-and-chow-groups-of','2013')]:
    b(key,'misc',title,'MathOverflow contributors',date,url,'Search lead only. Not used as a substitute for the opened SGA6 and other primary results. Different gamma/topological comparisons must not be conflated.',[8,13])
lines=[]
for d,_ in R:
    key=d['key'];typ=d['type'];fields={k:v for k,v in d.items()if k not in ['key','type']}
    lines.append('@'+typ+'{'+key+',\n'+',\n'.join('  '+k+' = {'+v.replace('}','\\}').replace('{','\\{')+'}'for k,v in fields.items())+'\n}\n')
(P/'references.bib').write_text('\n'.join(lines))
(P/'reference_checks.json').write_text(json.dumps([d for d,_ in R],ensure_ascii=False,indent=2)+'\n')
claims=json.loads((P/'claims.json').read_text())
refmap={d['key']:s for d,s in R}
log=[]
for f in sorted(P.glob('search_*.json')):
    raw=json.loads(f.read_text());n=int(f.stem.split('_')[-1]);texts=[v.get('text','')for v in raw['result'].get('content',[])if v.get('type')=='text'];results=[]
    for text in texts:
        for block in text.split('--------------------------------------------------------------------------------'):
            m=re.search(r'^\s*(.*?)\s*\((https?://[^\n]+)\)\s*\n【([^】]+)】',block,re.M)
            if m:results.append({'title':m.group(1),'url':m.group(2),'retrieval_ref':m.group(3),'fetch_failed':'Failed to fetch'in block})
    mapped=[x['id']for x in claims if any(n in refmap.get(k,[])for k in x['refs'])]
    log.append({'id':f'root-search-{n:03}','date':'2026-11-19','requests':raw['args'],'result_metadata':results,'claim_ids':mapped,'interpretation':'This is a search/read trace. A returned title is not a matched fate; exact matches and limitations are in claims.json and reference_checks.json.'})
for x in claims:
    log.append({'id':'root-fate-'+x['id'],'date':'2026-11-19','claim_ids':[x['id']],'search_batches':sorted({f'root-search-{n:03}'for k in x['refs']for n in refmap.get(k,[])}),'opened_primary_refs':x['refs'],'match':x['fate'],'limits':x['present_status']})
log.append({'id':'root-primary-scan-reads','date':'2026-11-19','sources':[
 {'key':'SGA6V','url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf','printed_pages':'349–351,353–359','method':'Direct primaryPDF download; visually inspected rendered pages; no reliance on unofficial reconstructed HTML.'},
 {'key':'GrothendieckRRR1957','url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf','printed_pages':'VIII;28–36','method':'Original scans inspected;VIII establishes1957report provenance.'},
 {'key':'SGA4VII','url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf','printed_pages':'363–365','method':'Original scans inspected.'},
 {'key':'SGA4VIII','url':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf','printed_pages':'366–369','method':'Original scans inspected.'},
 {'key':'PedriniWeibel1994','url':'https://numdam.org/item/AST_1994__226__371_0.pdf','printed_pages':'404','method':'Original scan inspected.'},
 {'key':'Serre1977','url':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf','printed_pages':'54–59','method':'PrimaryPDF direct download, text and exact propositions read.'}],
 'search_limit':'Direct zbMATH query an:0091.33004 returned403. Domain-targeted zbMATH searches were attempted forBorel–Serre andMackall; weak/no hits are not evidence of undeveloped mathematics. Broader MathOverflow searches yielded related gamma/topological questions, not exact selected-family identifications. Backward references fromMackall→SGA6,Alonso→Illusie,BFM→Grothendieck andJouanolou,Pedrini–Weibel→TT were used only to the extent explicitly opened.'})
with(P/'search_log.jsonl').open('w')as f:
    for x in log:f.write(json.dumps(x,ensure_ascii=False)+'\n')
with(P/'reference_check_events.tsv').open('w')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome'])
    for d,_ in R:w.writerow([d['key'],'2026-11-19','GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root','used and rechecked in this run',d['annote']+' This records source and hypothesis comparison, not a complete independent proof of the work.'])
missing=sorted({r for x in claims for r in x['refs']}-set(refmap));assert not missing,missing
print(json.dumps({'references':len(R),'search_batches':len(list(P.glob('search_[0-9]*.json'))),'fate_trace_rows':len(claims),'unmapped_refs':missing}))
