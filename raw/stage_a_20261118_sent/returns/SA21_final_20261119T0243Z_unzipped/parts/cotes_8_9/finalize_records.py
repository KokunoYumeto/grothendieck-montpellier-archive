"""Serialize manual search/check records, then validate artifact bookkeeping.
This program does not infer mathematical verdicts from source text.
"""
from pathlib import Path
import csv,json,re,hashlib,collections
P=Path(__file__).parent
claims=json.loads((P/'claims.json').read_text())
problems=json.loads((P/'problems.json').read_text())
mapping=json.loads((P/'claim_search_map.json').read_text())
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; inherited effort (not separately exposed); /root/cotes_156_8_9'

searches=[
('S01','web_001.json','Web search, engine1; exact French topic names',
 'Grothendieck "magasins" "géométrie des formes" | "ateliers" "multistrates" | "Vers une géométrie des formes"',
 'Archive/CSG inventory and Malgoire2002 seminar discovered; no exact mathematical theorem located. Discovery is not a proof of absence.'),
('S02','web_002.json','Primary catalogue/seminar and MO discovery pages opened',
 'https://imag.umontpellier.fr/?idseance=509&page_id=526 | https://csg.igrothendieck.org/unpublished-works/ | MathOverflow question82087 | https://iut-theory.org/divers/unpworks.pdf',
 'Catalogue and2002 seminar identify programme; MO used as discovery, not authority. Linked partial transcription covers I–VII and does not establish VIII/IX claims.'),
('S03','web_003.json','Web search, engine2; polarity and named-database discovery',
 'Ore1944 Galois connexions complete lattices orthocomplemented | site:arxiv.org orthogonality spaces orthoclosed subsets complete ortholattice Dacey | site:numdam.org Grothendieck "géométrie des formes" | site:zbmath.org Grothendieck "formes" "1986"',
 'Birkhoff1948 and Jenča2022/2023 located. Numdam/zbMATH here are domain-restricted web-index searches, not exhaustive direct database queries.'),
('S04','web_005.json;web_012.json','Web search, engine1; named sources and direct zbMATH attempt',
 'site:zbmath.org "Grothendieck" "géométrie des formes" | site:arxiv.org "Grothendieck" "ateliers" | site:numdam.org "géométrie des formes" | site:mathoverflow.net "Vers une géométrie des formes" | open https://zbmath.org/?q=ti%3A%22geometrie+des+formes%22',
 'Archive/catalogue/Malgoire/MO discovered; no exact custom theorem. Direct zbMATH endpoint inaccessible. The bounded searches do not certify comprehensive zbMATH coverage.'),
('S05','web_004.json','Primary books and arXiv article opened',
 'Birkhoff1948 scanned book, chV | https://arxiv.org/abs/2206.08113 | https://arxiv.org/pdf/2206.08113',
 'Double-polar lattice construction checked against Birkhoff; Jenča proper-interval model and theorem hypotheses inspected. Point-stratum claims do not automatically match.'),
('S06','web_006.json','Web search, engine1; later work and reference-following',
 '"The notion of space in Grothendieck" Cruz Morales | orthogonality spaces adjointable maps complete ortholattices Vetterlein Paseka arxiv | Ehrhard finiteness spaces finite intersection orthogonality2005',
 'Paseka–Vetterlein2025 and Ehrhard2005 located; Jenča citations/definitions inspected. CruzMorales historical reception handled by root, not counted as a theorem source.'),
('S07','web_008.json','Web search; exact custom support/compactology terms',
 'Grothendieck "ateliers" "supports" "spatios" | Grothendieck "magasins" "compactologie"',
 'No exact publication of the independent face/refinement or compact-stratum axioms located.'),
('S08','web_008.json','Web search; graph and SGA4 primary-source discovery',
 'Serre Trees1980 graph involution without fixed points definition2.1 pdf | site:numdam.org SGA4 exposéII préfaisceaux faisceaux1972; find Paseka–Vetterlein Lemma3.7/Theorem6.7',
 'Classical graph definition and SGA formal gluing comparison pursued; modern adjointability hypotheses separated from mere orthogonality preservation.'),
('S09','web_009.json','Web search plus exact primary passages',
 '"Finiteness spaces" Ehrhard filetype:pdf2005 finiteness orthogonal | "Serre" "Trees" "2.1 Graphs" filetype:pdf | "SGA4" "II" "faisceau" "equalisateur"; open Birkhoff chV§5 and Paseka–Vetterlein closure lemmas',
 'Author PDF, graph book and sheaf text located; finite-intersection analogy is not an atelier theorem.'),
('S10','web_011.json','Web search; exact refinement/compactology variants',
 '"Grothendieck" "magasins" "polyédral" | "Grothendieck" "ateliers" "raffinement" supports | "Grothendieck" "compactologie" "figures"',
 'No exact matching custom theorem located. Negative outcome is limited to those terms and consulted sources.'),
('S11','web_010.json;web_011.json','Primary graph verification and CW discovery',
 'Open https://studylib.net/doc/28421844/trees and https://link.springer.com/book/10.1007/978-3-642-61856-7; query Bjorner "Posets, regular CW complexes and Bruhat order" pdf; find Serre2.1',
 'Serre I§2.1 Definition1,p13 verified with publisher1980 metadata; CW theorem located for later exact inspection.'),
('S12','web_014.json','Web search; English and alternative custom terms',
 '"Grothendieck" "magasin" "support" faithful | "Grothendieck" "set-theoretic figures" | "spatial workshops" Grothendieck | "orthogonality" "magasins"',
 'No exact atelier theorem located. Orthoset papers were compared by hypotheses rather than terminology alone.'),
('S13','web_012.json;web_013.json;web_015.json;web_016.json','Primary CW article and metadata verification',
 '"Posets, regular CW complexes" "pdf" Bjorner1984 | "S0195669884800128"; open CORE PDF and DOI; open article body https://www.academia.edu/83782917/Posets_Regular_CW_Complexes_and_Bruhat_Order; find Proposition3.1',
 'CORE/DOI fetch failed; actual article OCR body was opened and checked at Definition2.1,p8, Proposition3.1,p11. Regular CW face-poset theorem is precise but not the unspecified oriented-maquette equivalence.'),
('S14','web_007.json;web_009.json;web_012.json;web_014.json;web_015.json;web_016.json','Later primary theorems checked, not just abstracts',
 'https://arxiv.org/pdf/2501.04482; https://arxiv.org/abs/2501.04482; https://link.springer.com/article/10.1007/s10773-025-06031-4; https://arxiv.org/pdf/2206.08113; https://arxiv.org/abs/2206.08113; https://www.irif.fr/~ehrhard/pub/finite.pdf',
 'PV Lemma2.3, Proposition2.4, Lemma2.9, Definition3.1, Lemmas3.5–3.7, Theorem6.7 checked. Jenča §4/Lemma4.1/Theorems4.10,4.12 checked, including boundedness. Ehrhard§1,p4 checked. Publication dates distinguished from circulation; PV arXiv journal-year discrepancy resolved by publisher2025.'),
('S15','web_012.json;primary/passage_locations.json;primary_supplements_output.txt','SGA4 exact-locator comparison and primary editorial-PDF verification',
 'https://grothendiecksga.com/read/sga4/fr/II-2.html; https://www.normalesup.org/~forgogozo/SGA4/02/02.pdf; ExposéII Corollary2.4, PDFp4/marginalp8, editorial version71766d9 dated2024-07-30',
 'Sheaf equalizer formula independently corroborated by opening and rendering the official editor PDF. This is a modern editorial reedition, not an original-printing facsimile. No exact theorem about custom atelier restrictions is claimed. See supplemental_primary_checks.md.'),
('S16','web_017.json','Web search, engine1; supplementary metric/faithfulness/quotient/EGA terms',
 '"Grothendieck" "géométrie des formes" "EGA" | "Grothendieck" "magasins" "métrique" | "Grothendieck" "ateliers" "pleinement fidèle" | "Grothendieck" "magasins" "quotient"',
 'Only general archive, catalogue and exposition results; no EGA identity or metric/quotient/full-faithfulness theorem located. EGA is not treated as an exact source for these custom constructions.')]
with (P/'search_log.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['search_id','date','mode','queries_and_opens','result_and_limit','claim_ids','raw_output'],delimiter='\t');w.writeheader()
    for sid,raw,mode,q,result in searches:
        ids=[cid for cid,a in mapping.items() if sid in a['search_ids']]
        w.writerow(dict(search_id=sid,date=DATE,mode=mode,queries_and_opens=q,result_and_limit=result,claim_ids=';'.join(ids),raw_output=raw))

events=[]
def E(cid,typ,outcome):events.append({'statement_id':cid,'date':DATE,'who':WHO,'type':typ,'outcome':outcome})
for c in claims:
    E(c['id'],'carried as background without fault found','Full source passage read and occurrence/status recorded. This event is not a proof check. Source status: '+c['status_on_pages']+'. Exact literature comparison in claims.json and claim_search_map.json.')
for p in problems:
    E(p['id'],'used and rechecked in this run','Question wording and precise source qualifiers checked; state_of_art distinguishes opened source results from missing hypotheses. No assertion that the question is an externally recognized open problem.')
for cid in ['C-SA21-8-034','C-SA21-9-022','C-SA21-9-025']:
    E(cid,'independent re-proof','Double-polar closure, arbitrary joins/meets and orthocomplement proved directly, including null elements; proof_audits.md §A. No distributivity inferred.')
E('C-SA21-9-028','independent re-proof','Join-density proves beta(S)perp=beta(CS), all closed sets principal in this representation, and ordered face-deployments recover the original spatial figures; proof_audits.md §B. Does not use failed general sorite.')
E('C-SA21-9-030','targeted proof check','Mere disjointness preservation proves only the inclusion in proof_audits.md §C. The author’s injection refutes complement equality but does not refute closure equality.')
for cid,section in [('C-SA21-8-018R','D'),('C-SA21-8-045R','E'),('C-SA21-8-030R','G'),('C-SA21-9-030R','C')]:
    E(cid,'computation or formal certificate','Exact finite structure and all claimed premises checked in computations.py/computations_output.txt; proof_audits.md §'+section+'. This is a finite counterexample certificate, not a proof assistant formalization.')
for original,refined,outcome in [
 ('C-SA21-8-018','C-SA21-8-018R','Comparable pairs disjoint plus deployment injectivity does not imply common-face pairwise disjointness.'),
 ('C-SA21-9-024','C-SA21-8-018R','The same weak face-axiom substitute does not suffice unless spatial-figure well-typedness supplies the missing premise.'),
 ('C-SA21-8-045','C-SA21-8-045R','Printed singleton cosupport omits Sab; whole-figure counterexample remains correct.'),
 ('C-SA21-8-030','C-SA21-8-030R','Monotone elementary assignment need not preserve compatibility, so a compatible join-preserving extension may not exist.'),
 ('C-SA21-9-030','C-SA21-9-030R','Disjointness-preserving bijection between two tiny orthosets fails double-polar closure compatibility.')]:
    E(original,"refuted, with the refined statement's id",refined+': '+outcome+' Only the specifically identified substatement is refuted.')
E('C-SA21-8-009R','independent re-proof','Four-stratum model satisfies original axioms and L1 but violates L2; every premise checked by hand in proof_audits.md §L.')
E('C-SA21-8-009',"refuted, with the refined statement's id",'C-SA21-8-009R refutes unrestricted L1⇒L2. L2⇒L1 remains valid; the author’s practical-class qualification is not contradicted.')
E('C-SA21-8-026','independent re-proof','Exact infinite natural-number-tail construction separates partition, saturation and order detection; proof_audits.md §F, symbolic formulas also recorded by computations.py.')
E('C-SA21-8-043','independent re-proof','For fixed n-vertex flag, independent choice of n−1 edges proves2^(n−1); source component decomposition retains its stated proof-sketch status. proof_audits.md §I.')
E('C-SA21-8-043','computation or formal certificate','Counts for n1–6 recomputed as1,2,4,8,16,32; computations_output.txt.')
E('C-SA21-8-051','computation or formal certificate','Example with edgesab,bc,cd and verticesa,c,e realizes all five degree/presence types; computations_output.txt.')
E('C-SA21-9-012','computation or formal certificate','Total-chain test models n1,2,3 give8,32,128 support classes. This verifies these finite cases only, not the general arbitrary-poset theorem.')
E('C-SA21-9-018','targeted proof check','Rational-coordinate triangle example verifies failure of cosupport carrier closure; large-residual carrier argument checked. proof_audits.md §H.')
E('C-SA21-8-033','used and rechecked in this run','Source’s2July retraction checked against unrevised scan73 assertion. No independent topological-corde counterexample is claimed here; proof_audits.md §J.')
E('C-SA21-8-038','targeted proof check','Full-faithfulness support/Boolean argument checked only for subsets of one allowed figure; no global distributivity conclusion. proof_audits.md §J.')
E('MP-SA21-8-12','targeted proof check','P4 example supplied by cotes_156_6_7 independently checked against VIII68–71 and VIII86. A private point outside the middle-vertex support is uncovered by supports orthogonal to that vertex, so faithfulness does not imply full faithfulness. No extra computation rerun; finite certificate belongs to R-SA21-9E-005. proof_audits.md §N.')
E('C-SA21-8-035','used and rechecked in this run','Exact hypotheses matched to PV2025 Lemma2.3 by using the lieu interior-shadow subset for each stratum; this is theorem matching, not an independent proof of all atelier structure.')
E('C-SA21-2-017','targeted proof check','At root request, independently checked source Fic a–d and literal side-containment replacement. Closed connected regularly immersed tripod arm containingA contracts to an interior vertex, violating endpoint-complement connectedness. proof_audits.md §M; root owns finite graph program.')
E('C-SA21-2-017',"refuted, with the refined statement's id",'R-SA21-side-contraction: exact finite tripod verifies every literal premise, including connectedD; preservation requires an extra endpoint-avoidance or endpoint-regularity/connectedness condition. U/X reading ambiguity is retained.')

refs={
 'Birkhoff1948':'Opened scanned primary book; chIV§5 Theorem9 and Corollary pp54–56 and §6 Theorem10,p56. General polarity proof also independently reconstructed.',
 'Serre1980':'Opened primary book OCR I§2.1 Definition1,p13 and publisher metadata; vertices, oriented-edge reversal and source/target match exactly; no dimension-two result inferred.',
 'Bjorner1984':'Opened actual primary article OCR body at Definition2.1,p8 and Proposition3.1,p11; regular CW hypotheses retained; CORE/DOI fetch failures documented.',
 'Jenca2023':'Opened arXiv full text and metadata; §4 interval-only construction,Lemma4.1,Theorems4.10 and4.12 checked. Theorem4.12 requires bounded P. First circulation16June2022,publication2023.',
 'PasekaVetterlein2025':'Opened full primary PDF and publisher article; Lemma2.3,Proposition2.4,Lemma2.9,Definition3.1,Lemmas3.5–3.7,Theorem6.7 checked. First circulation8January2025,publication27May2025,v3October2025. Publisher corrects arXiv journal-year metadata.',
 'Ehrhard2005':'Opened author preprint dated20October2003 §1,p4 and journal publication page15July2005; finite-intersection polarity is a comparison, not a custom compactology theorem.',
 'SGA4I1972':'Initial exact transcription ExposéII Definition2.1,Corollary2.4 checked; subsequently corroborated in official editorial PDF, recorded under SGA4II.',
 'SGA4II':'Official editor PDF version71766d9 dated2024-07-30 opened and rendered; Corollary2.4 onPDFp4/marginalp8 exact sheaf equalizer verified. Formal pattern only, not custom atelier theorem.',
 'SGA4IV':'Official editor PDF sameversion opened/rendered at4.2.1–4.2.2,PDFpp20–21/marginalpp336–338. Sobrification and specialization formula verified. False closed-point-space sobriety example excluded; general specialization is a preorder unlessT0.',
 'Malgoire2002':'Opened official3October2002 seminar notice; programme presentation verified, no exact theorem result stated.',
 'CSGUnpublished':'Opened institute catalogue entry;1986 manuscript cotes156-1–9 identified. Catalogue description is not theorem evidence.',
 'MontpellierSA21':'Opened official archive inventory; source identification verified, handwritten scans not examined in this run.'}
for key,outcome in refs.items():E(key,'used and rechecked in this run',outcome)
E('SA21-88','used and rechecked in this run','Esquisse primary PDF rendered: Isom comparison and pi0 versus homotopy at section5,printedp29/PDFp25(one-based),continuationp30. Section6 begins printedp33/PDFp29. supplemental_primary_checks.md.')
for sid in ['R-SA21-support','R-SA21-restriction','R-SA21-cones','R-SA21-polyhedra','R-SA21-rives','R-SA21-sheaves']:
    E(sid,'targeted proof check','Independent review of root argument at its expressly limited scope; no concrete flaw found. Supporting details and exclusions in root_proof_review.md. Not a formal certificate or a rerun of external theorems.')
with (P/'check_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

# Pure data and locator checks below; no new mathematical testing.
claimfields={'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'}
problemfields={'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
assert all(set(c)==claimfields for c in claims)
assert all(set(p)==problemfields for p in problems)
assert len({c['id'] for c in claims})==len(claims)
assert len({p['id'] for p in problems})==len(problems)
assert set(mapping)=={c['id'] for c in claims}
assert all(c['class'] in 'ABCDEF' and c['fate'] and c['refs'] for c in claims)
assert all(p['state_of_art'] and p['worth'] and p['refs'] for p in problems)
bibkeys=set(re.findall(r'@\w+\{([^,]+),',(P/'references.bib').read_text()))
usedrefs=set(k for c in claims for k in c['refs'])|set(k for p in problems for k in p['refs'])
assert usedrefs<=bibkeys,usedrefs-bibkeys
knownsearch={s[0] for s in searches}
assert all(set(a['search_ids'])<=knownsearch for a in mapping.values())
root=Path('/workspace/scratch/4017236f14bf/sources')
locerrors=[]
for obj in claims+problems:
    locs=obj.get('lines',[]) if 'lines' in obj else [x['file']+':'+x['lines'] for x in obj['occurrences']]
    for loc in locs:
        file,rest=loc.split(':',1)
        n=len((root/'texts'/'codex'/(file+'_transcription.tex')).read_text().splitlines())
        for a,b in re.findall(r'(\d+)[–-](\d+)',rest):
            if not 1<=int(a)<=int(b)<=n:locerrors.append([obj['id'],loc,n])
assert not locerrors,locerrors
coverage=list(csv.DictReader((P/'coverage.tsv').open(),delimiter='\t'))
assert len(coverage)==24
readings=list(csv.DictReader((P/'readings.tsv').open(),delimiter='\t'))
links=list(csv.DictReader((P/'links.tsv').open(),delimiter='\t'))
assert all(l['kind'] in ['folder','published work','our projects'] for l in links)
manifest=[]
for row in coverage:
    folder=row['folder'];textfile=root/'texts'/'codex'/(folder+'_transcription.tex');notefile=root/'notes'/'codex'/(folder+'_notes.md')
    manifest.append({'folder':folder,'transcription_lines':len(textfile.read_text().splitlines()),'notes_lines':len(notefile.read_text().splitlines()),'transcription_sha256':hashlib.sha256(textfile.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256(notefile.read_bytes()).hexdigest(),'read_output':'read_outputs/'+folder+'.txt'})
(P/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
report={'claims':len(claims),'claims_by_class':dict(collections.Counter(c['class'] for c in claims)),'claims_by_source_status':dict(collections.Counter(c['status_on_pages'] for c in claims)),'problems':len(problems),'readings':len(readings),'links':len(links),'coverage_folders':len(coverage),'scan_markers':len(json.loads((P/'scan_locator_map.json').read_text())),'bibliography_entries':len(bibkeys),'search_records':len(searches),'check_events':len(events),'validation':'PASS: exact schemas, nonempty assessments, unique IDs, all refs real keys, all claim search IDs present, locator ranges within files,24 full-read folders.'}
(P/'audit_output.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
