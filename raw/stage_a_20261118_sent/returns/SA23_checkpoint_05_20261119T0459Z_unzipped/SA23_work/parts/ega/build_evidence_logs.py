#!/usr/bin/env python3
"""Condense the actual searches and manually classified checks without redistributing sources."""
from pathlib import Path
import json,re,csv
P=Path(__file__).parent;R=P.parents[2]/'sources/external/ega/raw_search'
# Resolve the shared scratch root independently of process cwd.
R=Path('/workspace/scratch/0394364129a2/sources/external/ega/raw_search')
c=json.loads((P/'claims.json').read_text());items=json.loads((P/'items.json').read_text());bib=json.loads((P/'bibliography_records.json').read_text());bykey={x['key']:x for x in bib}
groups={
1:([18,20,21,22,26,30,34],'EGAIV1, Cartier and discriminant primary sources located; broad formal-smoothness query supplied leads, not an unrestricted discrete-topology theorem.'),
2:([18,20,21,22,26,30,34],'First metadata/HTML openings; arXiv HTML not sufficient, followed by primary PDF.'),
3:([18,20,21,22,26,30,34,53,61],'EGAIV1, Cartier Exp2 and Busé–Jouanolou PDFs opened; exact later page readings logged separately.'),
4:([14,15,17,18,19,20,21,24,25],'Separate local/adic formal smoothness from arbitrary noetherian flat-locus question; MO counterexample lead found.'),
5:([18,19,20,21,22,23,24,25],'Primary Stacks formal-smoothness hypotheses checked; no theorem for arbitrary discrete power-series extension imported.'),
6:([20,21,22,23,24,25,26,30],'Targeted formal-smoothness, flatness, and discriminant checks; exact scope retained in claim rows.'),
7:([25,30],'Discriminant coordinate character and Frobenius bad-locus route. Degree must be (r+1)(d−1)^r.'),
8:([21,23,24,25],'Bad regular locus references and infinite differential obstruction; no original Nishimura proof accessible.'),
9:([25,34],'Nishimura bibliography access failed; Cartier primary PDF independently available.'),
10:([34,49,56,71],'Regular immersion/Cohen-factorization/one-equation dimension queries; exact primary tags opened next.'),
11:([34,49,56],'Cartier Exp3 and local algebra passages; connectedness and positive Koszul degrees retained.'),
12:([1,2,3,4,5,7,8,9,10,11,12,13,49,57,58],'Jouanolou collected-works metadata and supplied complete offprints checked; modern lci comparisons do not remove residual hypotheses.'),
13:([25,34],'Cartier characteristic-zero smoothness and Brodmann–Rotthaus author bibliography. Article metadata verified; whole BR proof not read.'),
14:([25,34],'Later Cartier exposés6–8 were not found in the opened volume; Nishimura Euclid access blocked.'),
15:([25,34,55,56],'Nishimura I versus II disambiguated; BR author record and Loday structure theorem located.'),
16:([34,54,55,56,60],'Cohen factorization and characteristic-zero Hopf theorem traced through modern primary sources.'),
17:([46,47,48,62,63,64,69],'Meromorphic sheaves, approximation and effective étale descent; universal submersion alone is not upgraded to arbitrary effectiveness.'),
18:([38,39,45,87,88,89,90,91,96],'Restriction of scalars and nonprojective Hilbert/Picard programs; representability gives algebraic spaces under explicit hypotheses.'),
19:([32,33,38,39,87],'Exact Weil-restriction and Hilbert statements opened. The encountered unrelated0AL7 tag was not used as a theorem match.'),
20:([86,87,88,89,90,91,92,93,94,95,96],'Cote26 general program searches: quotient, bundle, duality and deformation questions separated by missing hypotheses.'),
21:([1,2,3,4,5,6,7,8,9,10,11,12,13,88,94],'Jouanolou authorship, nonprojective duality and sphere splitting. Relative P1 remains broader than the sphere theorem.'),
22:([47,48,86,89,90,91,95],'Unramified gluing, categorical epimorphism, and deformation queries; no unique theorem for underspecified finite-epimorphism question.'),
23:([34,87,88,89,90,91,94,95,96],'Primary Loday, Picard, free-action quotient, Raynaud and Grothendieck sphere sources opened; hypotheses retained.'),
24:([16,19,46,54,55,60],'Primary coherent-products, local lifting, meromorphic noetherian special case, and Auslander–Buchsbaum statements read.'),
25:([10,16,27,55,65],'Norms, absolutely flat rings and strict pro-Tor; determinant norm settles finite-locally-free portion, not every repartition notation.'),
26:([6,16,55,66,92,95],'Chase and Lang bibliographic leads; SGA4 VIII9.4 locator and primary Katz/Heinloth sources found.'),
27:([10,27,65,92,95],'Primary Katz and Heinloth PDFs plus norms/absolutely-flat tags opened. Ordinary deformation theorem distinguished from unrestricted one.'),
28:([6,47,48,62],'Lang and Zariski-Main searches. No exact Lang proof gap identified; ZMT hypotheses checked separately.'),
29:([39,40,41,44,45,88,95],'Oort and natural-bundle literature sought. Smooth jet-functor theorem is a category-specific analogue only.'),
30:([45,62,88,95],'Oort original PDF, ZMT and natural operations source openings.'),
31:([34,45,92,95],'Oort, Katz and Heinloth theorem locators; first Loday locator was wrong and corrected by follow-up.'),
32:([34,45,92,95],'Exact primary theorem text: Loday4.1.3, KMS14.6/14.8, Heinloth2.1.1, Oort2.2.1.'),
33:([24,25,34,45,77,95],'Oort proof context, finite-presentation flatness and finite-type CM-locus scope.'),
34:([55,71,72,74,75,78,79,80,81,82],'Exact Artin–Rees, dimension/parameters, Serre-condition, normalization and graded algebra queries.'),
35:([55,71,72,74,75,78,79,80,81,82],'Primary dimension, Hilbert-functions, Serre-condition and pro-completion pages read. Finite certificate limitations retained.'),
36:([55,56,61,88,96],'Artin–Rees strict pro-system proof read; Faltings–Chai/Raynaud publisher records and EGAIII locator sought.'),
37:([55,61,88],'EGAIII Numdam metadata opened; web PDF reader rejected size; local download attempted. Faltings–Chai metadata only.'),
38:([8,54,59,61,67,68,76,83,87,93,95],'SGA1/SGA2/FGA records and finite-étale fundamental-group theorem; no unknown-priority claims inferred.'),
39:([8,24,25,47,48,59,74,75,77,87,95],'Normalization/unramified definitions, EGAIV3 metadata and finite-presentation flatness/CM facts. Nagata bibliography403 retained.'),
40:([54,55,56,74,76,87,95],'Primary SGA2 and FGA comments opened; finite-depth and AFH bibliography searches.'),
41:([27,31,44,45,54,56,74],'Exact trace/repartition, integrability and naturality words searched; no source identifying the reused English integrability page found. Depth and AFH records opened.'),
42:([1,9,27,70,97],'Exact phrases identify Artin IX2.14 and XII6.3; secondary reconstruction used only as locator and followed with original PDF. No exact repartition/integrability attribution found.'),
43:([70,76,88,97],'SGA2 XI3.13 found; reused corollary lead then verified in original SGA4III. Oort dual search supplied no exact theorem.'),
44:([6,88,91],'Nonprojective dual and Artin bibliography queries; Brion primary paper and author notes found.'),
45:([88,91],'Brion and Robert primary-author sources opened; Artin bibliography403. Faltings–Chai proof itself still not read.'),
46:([88],'Brion§3.1 p466 and Robert2.3.2/2.3.7 explicitly distinguish dual existence from projectivity; attribution route recorded.'),
47:([76],'Web screenshot metadata returned; final ≥4 check made by local visual inspection of the downloaded primary reprint, not the missing web image.'),
48:([6,16,25,92],'Bibliographic title/DOI audit and exact Heinloth publication match. Correct Kunz bibliography is Kunz-flat.'),
49:([6,25,90,91,92],'Kunz/Lang bibliography openings403; publisher GIT metadata opened; Nagata1957 lead concerns normic-form assumptions, not yet the archive’s analytic-completion gap.')}
groups.update({50:([28,29,35,36],'Exact adjunction, Weierstrass weights, nilpotent derivation correspondence and arbitrary differential base-change queries.'),51:([28,29,35,36,37,42,43,73],'Primary conormal, Weierstrass, differential and nilpotent-derivation texts opened; exact regular-curve, thickening, descent and graded-category queries. Graded-category draft remains unidentified.'),52:([35,36,37,42,43],'Primary Stacks curve example, nilpotent-thickening definition, Amitsur descent, base-change lemma and logarithm/exponential statement opened.'),53:([35,36,42,43],'Exact source locators refined: Stacks33.12.7,10.131.12 and35.3; van den Essen publisher record verifies the backward reference metadata.')})
log=[]
for f in sorted(R.glob('search_*.json')):
 n=int(f.stem.split('_')[-1]);x=json.loads(f.read_text());cmd=x.get('commands')
 if cmd is None:
  cmd={}
  if 'queries' in x:cmd['search_query']=x['queries']
  if 'open' in x:cmd['open']=[{'ref_id':u} if isinstance(u,str) else u for u in x['open']]
  if 'find' in x:cmd['find']=x['find']
 res=x.get('result',x.get('response',{}));s=json.dumps(res,ensure_ascii=False)
 urls=[]
 for url in re.findall(r'https?[^\s"\\<>]+',s):
  url=url.rstrip(').,;:}')
  if url not in urls:urls.append(url)
 ids,note=groups.get(n,([], 'Search operation recorded; refer to exact linked claim scope.'))
 log.append(dict(id=f'S-ega-{n:03d}',date='2026-11-19',commands=cmd,claim_ids=[f'C-SA23-ega-{i:03d}' for i in ids],urls=urls,match_and_limit=note,raw_evidence=f'sources/external/ega/raw_search/{f.name} (internal cache, excluded from final ZIP)'))
# Every claim gets an inspectable fate concordance to actual searches and opened/located references.
for x in c:
 ids=[s['id'] for s in log if x['id'] in s['claim_ids']]
 log.append(dict(id='FATE-'+x['id'],date='2026-11-19',claim_ids=[x['id']],hypothesis_searched=x['statement'],search_operations=ids,refs=[dict(key=k,url=bykey[k]['url'],link_status=bykey[k]['note'],read_scope=bykey[k]['annote']) for k in x['refs']],match_and_limit=x['fate'],status_date=x['fate_date']))
# Original-page inspection events supply the exact locators which broad searches alone cannot establish.
for tag,claims,url,loc,outcome in [
 ('EGAIV1',[18,20,21,22,26,53,61],'https://www.numdam.org/article/PMIHES_1964__20__5_0.pdf','0.16.1.9;0.19.3.12 pp85–86;0.19.8.3 pp110–111;0.20.4.6 p125;0.20.4.13iv p127;0.20.5.7 p131;0.20.7.2–3 pp147–148;0.22.5.10i p204','Exact original passages compared; missing Z in printed field is real, whereas purported map-label errors in earlier comparison edition are not in this print.'),
 ('EGAIV4',[46,50,51,52,53,61],'https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf','16.1.5–6 pp6–7;19.5.5 pp206–209;20.1.3–4 pp227–228;21.2.9 p261;Liste3 IV6,8,9,12–15 pp347–348','Final immersion hypothesis, separation placement, Deligne credit, Lê correction context and published withdrawal verified.'),
 ('SGA6VII',[49],'https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf','VII1.1–1.5 pp416–421','Koszul definition and explicit replacement of EGA16.9.2 read in original scan.'),
 ('SGA4II',[66,84,85],'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf','VIII7.9.1–3 pp399–401;VIII9.4 pp410–412','Both reused source texts identified exactly, preserving categories and four surjectivity alternatives.'),
 ('SGA4III',[70,97],'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-3.pdf','IX titlep1 and2.14p23;XII titlep79 and6.2–6.3pp98–102','M.Artin authorship, finite/fp constructibility and final derived-comparison hypotheses verified; handwritten R1 still unidentified.'),
 ('EGAIII',[61],'https://www.numdam.org/article/PMIHES_1961__11__5_0.pdf','4.3.6 p133 (physicalPDF130)','False equality verified in original image; natural inclusion repairs the analytically-integral implies unibranch proof.'),
 ('SGA2',[76],'https://arxiv.org/pdf/math/0511279','XI3.13 reprintp105/originalp132;XI3.16–17 pp106–107','Dimension≥4 visually confirmed; does not certify the broader marginal Lefschetz claims without their hypotheses.')]:
 log.append(dict(id='PRIMARY-'+tag,date='2026-11-19',claim_ids=[f'C-SA23-ega-{i:03d}' for i in claims],query='Direct original-publication comparison at supplied numbered reference',urls=[url],locator=loc,match_and_limit=outcome))
for row in log:
 if row['id'].startswith('FATE-'):
  row['search_operations']=[s['id'] for s in log if (s['id'].startswith('S-') or s['id'].startswith('PRIMARY-')) and row['claim_ids'][0] in s.get('claim_ids',[])]
(P/'search_log.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in log))
# Manual check classification. Generic source reading is never called a proof check.
who='GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega'
events=[]
def E(id,typ,out):events.append(dict(statement_id=id,date='2026-11-19',who=who,type=typ,outcome=out))
for i in items:E(i['id'],'carried as background without fault found','Text concordance only: '+i['check']+'; '+i['check_reason']+' This event does not certify a proof.')
for x in c:E(x['id'],'carried as background without fault found','Complete source passage read; status and searched fate recorded. '+x['status_on_pages']+'. This baseline event is not a proof check.')
independent=[10,11,14,17,21,23,26,28,29,32,33,35,36,37,42,43,49,50,51,53,55,56,58,59,61,65,67,68,71,72,75,78,79,80,81,82]
targeted=[1,2,3,4,5,7,8,9,12,13,15,16,18,19,20,22,24,25,30,34,38,39,40,41,45,46,47,48,52,54,57,60,62,63,64,66,69,70,74,76,77,84,85,87,88,89,90,91,92,93,94,95,96]
for n in independent:E(c[n-1]['id'],'independent re-proof',c[n-1]['present_check']+' Scope: see proof_notes.md; restricted examples do not prove unrestricted versions.')
for n in targeted:E(c[n-1]['id'],('targeted proof check' if n in [16,52,54,62,66,70,84,85,95] else 'used and rechecked in this run'),c[n-1]['present_check']+' This check is limited to the stated argument or exact external hypothesis comparison, not an unqualified proof of all clauses.')
for x in c:
 if x['computation']['certificate_search_labels']:E(x['id'],'computation or formal certificate','Saved computations.py/computation_outputs.json: '+', '.join(x['computation']['certificate_search_labels'])+'. Scope and hypotheses are in each certificate; finite truncation is not an unrestricted proof.')
# The refined-statement records are embedded in the claim, so refutation links have real targets.
refined={17:'Require the comparison algebra C, rather than B alone, to meet the relevant smoothness/flatness conditions; this candidate repair needs the exact theorem hypotheses.',25:'Openness holds under the finite-presentation hypotheses of Stacks00R8; arbitrary noetherian morphisms need not have open flat locus.',26:'A kernel of absolute differentials need not descend to the smaller field even when k∩K^p=k^p; the exact counterexamples in proof_notes establish the negative assertion.',30:'For degree d forms in r+1 variables, coefficient degree is (r+1)(d−1)^r.',32:'For commuting nilpotent-near-identity elements, log(ggprime)=log(g)+log(gprime).',33:'Exponentials of nilpotent primitives are group-like; exp(x)−1 need not be primitive.',34:'Retain a connected exhaustive coalgebra filtration in the characteristic-zero enveloping reconstruction.',37:'Add nilpotence of the augmentation ideal; finite locally free associated graded alone does not imply it.',43:'Faithful flatness gives the equalizer descent assertion; infinitesimal diagonal vanishing alone is insufficient.',49:'Use Koszul acyclicity in positive degrees for the nonnoetherian regular-immersion definition.',50:'Separate finite B-subquotients from arbitrary A-subquotients; the latter need not be adically separated.',51:'A finitely presented A-algebra need not have a finitely generated kernel from A; the final EGA immersion theorem remains intact.',53:'The closed-linear-variety step is invalid for general algebra lifts; EGAIV4 withdraws0.19.3.12. No full theorem counterexample is claimed.',71:'Avoid all relevant top-dimensional components to obtain the intended one-equation dimension drop.',72:'Elements in p cannot form a nonempty system of parameters in A/p; determine the intended ambient ring on the scan.',75:'A codimension≥2 normalization comparison needs prior equality in codimension1; it does not follow from defining Z as support of B/A.',78:'Require phi psi(Aplus)=0 for the stated kernel and generation argument.',79:'Section independence holds under the augmented composition and graded hypotheses; it fails without them.',80:'Retain the preceding surjectivity condition alongside equality of Hilbert series.',81:'Literal flatness implication(i) is false; implications(ii),(iii) hold under the displayed split tensor description.'}
for n,statement in refined.items():
 x=c[n-1];rid=x['id']+'-R';x['refined_statement']={'id':rid,'statement':statement,'attribution':'present-run reconstruction, not manuscript emendation'}
 E(x['id'],'refuted, with the refined statement’s id',rid+': '+statement)
for b in bib:E(b['key'],'carried as background without fault found','Bibliographic/access and bounded use record: '+b['note']+'. '+b['annote'])
for key,scope in [('EGAIV1','Original statements and alleged defects at the listed exact pages compared.'),('EGAIV4','Final hypotheses and published errata read directly.'),('SGA4VIII','VIII7.9.1–3 and9.4 exact reused-text correspondence.'),('SGA4IX','IX2.14 finite/fp constructible direct image; different final proof.'),('SGA4XII','XII6.3 final assumptions and truncation argument.'),('SGA6VII','VII1.1–1.5 Koszul-regular definition and comparison.'),('SGA2','XI3.13 dimension≥4 visually checked.'),('Cartier1956','HA3 connected exhaustive filtration.'),('CartierExamples1956','Proposition8 injectivity only.'),('BuseJouanolou2012','Propositions4.7 and4.13 degrees.'),('Loday2008','Theorem4.1.3 connected characteristic-zero equivalence.'),('Stacks0911','Lemma15.28.3 Artin–Rees strict pro-Tor proof.'),('Oort1971','Theorem2.2.1 and proof of unpolarized formal smoothness.'),('HeinlothSchmitt2010','Proposition2.1.1 curve/reductive group hypotheses.'),('KolarMichorSlovak1993','§14.6/14.8 smooth natural bundles and finite jet groups.')]:E(key,'used and rechecked in this run',scope)
(P/'claims.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
with (P/'check_events.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
missing=[x['id'] for x in c if not any(x['id'] in s.get('claim_ids',[]) and (s['id'].startswith('S-') or s['id'].startswith('PRIMARY-')) for s in log)]
print('Search records:',len(log),'check events:',len(events),'claim search gaps:',missing)
