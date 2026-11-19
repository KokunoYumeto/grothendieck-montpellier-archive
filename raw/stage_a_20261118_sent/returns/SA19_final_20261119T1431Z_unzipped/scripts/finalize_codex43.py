"""Serialize manually reviewed chronology, proof corrections and source coverage.

This script does not adjudicate source entries or infer results from keywords.
All substantive changes below are explicit research decisions of the root reader.
"""
from pathlib import Path
import json,csv
B=Path(__file__).resolve().parents[1]
W=B/'workstreams/codex43'
claims=json.loads((W/'claims.json').read_text())
dates={}
def years(ns,text):
    for n in ns: dates[n]=text
years(range(601,610),'Classical material explicitly attributed on the sheets; precise first circulation not established. Checked in Milne, version 4.03, 6 August 2020. The undated sheets do not independently establish priority.')
years([602],'Chevalley published May 1951; first circulation not established.')
years([609],'Generalized Jacobians: contemporary exposition by Koszul, March 1954; Serre book 1959. Deligne exposition of the classical local symbol published 1991. These dates are not dates of the manuscript.')
years([610,611,626,630],'Serre proalgebraic framework: received 2 May 1960, issue 1960; local formal-curve theorem: submitted 12 October 2011, published 30 December 2013. Exact unrestricted manuscript assertion not identified as settled. Ribeiro–Rosengarten first circulated 20 June 2025, revised 28 July 2026, for its explicitly narrower Ext results.')
years([612,673],'Cartier note presented 12 June 1967 and published 1967; Oort–Oda manuscript received 21 November 1966, published January 1968. No exact earlier circulation established for the manuscript formulation.')
years([613,615],'Classical continuous group-cohomology calculation; exact first appearance not established. Literal overstatement checked in this run on 19 November 2026.')
years([614,632,664,665,667],'Serre: received 2 May 1960, issue dated 1960 (legal deposit first quarter 1961). SGA3 seminar 1962–1964, first publication 1970. Manuscript date remains unknown; no priority inference.')
years([616,619,621,622],'Yekutieli first arXiv version 2 May 2002, publication 2003. Braunling–Groechenig–Wolfson first arXiv version 19 October 2015, publication 2016; revised text read dated 9 October 2017. These are matched constructions, not proof of influence or exact identity with every manuscript topology.')
years([617,618],'Matlis received 10 April 1958, revised 9 June 1958, published 1958. EGA IV3 published 1966. The failure of the unrestricted Hom–colimit passage is independently checked in this run, 19 November 2026.')
years([620],'The sign rule is standard homological algebra; no first discovery date established. The opened Yekutieli preprint circulated 2 May 2002 and was published 2003. The inconsistent displayed signs are checked on 19 November 2026.')
years([623,624,625,647],'SGA2 seminar 1962; original publication 1968; corrected reedition 2005. Modern Stacks statements checked 19 November 2026. The dates of these manuscript sheets are not supplied.')
years([627,634],'No exact all-quantifier formulation identified by the searches as of 19 November 2026. Related frameworks: Serre 1960; SGA1 seminar 1960–1961, publication 1971; Tate congress report 1962, proceedings 1963.')
years([628,629,631,641,643,656,666],'SGA1 seminar 1960–1961, original publication 1971; EGA IV3 publication 1966; SGA3 seminar 1962–1964, publication 1970. Exact dates vary by theorem as stated in the fate and reference locators; no earlier manuscript date is inferred.')
years([633,635,636,637,639,640,675,676],'Tate report delivered at the 1962 Stockholm congress and published in the proceedings in 1963. General Tate–Shafarevich finiteness is not thereby established. Later category-specific refinements are dated in their reference records.')
years([638],'The sheet cites Shatz 1962, whose exact original result was not independently opened. Verified modern scope: Suzuki first preprint 2014, publication 2020, Theorem 5.2.2.1; Tate congress report 1962/publication 1963 does not alone cover all infinitesimal p-coefficients.')
years([642,644,645,646],'Serre original lectures/book 1968; opened reprint 1989. These sources verify the finite-model/finite-type statement, not an arbitrary infinite-base-extension assertion. Literal unrestricted readings checked 19 November 2026.')
years([648,649,650,658,660,662,663],'SGA3 seminar 1962–1964; first publication 1970; Gille–Polo reedition 2011, opened PDFs corrected 13 October 2024. Later editor additions are not attributed to the earlier manuscript.')
years([651,652],'Oort book published 1966; publisher metadata checked but complete book unavailable. Oort–Oda received 21 November 1966, published January 1968. The labelled finite extension computation is independently verified here.')
years([653,654,655,674],'Classical Barsotti–Weil/extension results are distinguished from higher internal Ext. Oort–Oda received 21 November 1966, published January 1968. Ribeiro–Rosengarten first arXiv submission 20 June 2025, revised 28 July 2026; announced to appear in Algebraic Geometry.')
years([657],'Grothendieck, Chevalley seminar 1956–1958, Exposé 7, pp. 8–9; a more precise circulation date was not established.')
years([659,668,669,670,671],'Gabriel published 1962; SGA3 first publication 1970; Oort–Oda received 21 November 1966, published January 1968. The false unrestricted socle criterion and its explicit refinement are checked in this run, 19 November 2026.')
years([661],'Barr received 31 July 1973, published 1974. Kihara received 5 January 2016, online 23 April 2016, issue June 2016. Neither is an unrestricted finite-free approximation theorem over every ring.')
years([672],'Oort–Oda received 21 November 1966 and published January 1968; the Dieudonné ring presentation is on p. 82. No priority claim for these undated sheets.')
years([677,678,679],'Classical local-symbol framework described in Serre 1959; Deligne detailed exposition published 1991. The final manuscript independence check has no exact identified completion as of 19 November 2026; strict-unit repair checked in this run.')
years([681],'Oort extension category published 1966; Hazewinkel–Oort report 7213 dated 29 May 1972. The finite-kernel deduction is an independent exact-sequence check made 19 November 2026, not a claimed new theorem.')
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    if n in dates:c['fate_date']=dates[n]
    c['refs']=['GrothendieckChevalley1956' if r=='GrothChevalley7' else r for r in c['refs']]
    if n==628:
        c['refs'].append('Stacks04GK')
        c['fate']+=' Stacks Project Lemma 10.153.7, tag 04GK, gives a fully opened proof of finite-étale equivalence for every henselian local ring and its residue field.'
    if n==638:
        c['refs'].append('Suzuki2014')
        c['fate']='The explicit finite-flat residue blocks are independently checked. Suzuki2014 Theorem5.2.2.1 supplies general finite-flat local duality in its declared realization. Tate1963 alone excludes the full infinitesimal p-primary range; Shatz1962 is a source citation on the sheet, not an independently verified primary theorem in this dossier.'
    if n==660:
        c['fate']='SGA3 Exposé VIB Proposition11.13 proves exactly that an affine group scheme over a field is the projective limit of algebraic quotient groups, with faithfully flat transition maps. The field coalgebra proof is independently reconstructed in C12; this does not settle an arbitrary-ring generalization.'
    if n in {628,638,660}: c['present_status']='As of 19 November 2026: '+c['fate']
(W/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
problems=json.loads((W/'problems.json').read_text())
for p in problems:
    if p['id']=='MP-SA19-131':
        p['state_of_art']+=' Galet2026 Theorem A treats finite étale coefficients over higher local fields with char(k₂)=0; it is a precise modern analogue, not the unrestricted manuscript theorem.'
        p['refs'].append('Galet2026')
(W/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
extra=r'''
@misc{Stacks04GK,
 author = {{The Stacks Project Authors}}, title = {Lemma 10.153.7: Finite étale algebras over a henselian local ring},
 year = {2026}, howpublished = {The Stacks Project, tag 04GK},
 url = {https://stacks.math.columbia.edu/tag/04GK}, note = {verified},
 annote = {Statement and full proof opened 19 November 2026. Access year is not the original discovery date.}
}
@misc{Galet2026,
 author = {Galet, Antoine}, title = {Arithmetic duality for finite Galois modules over two-dimensional local fields of mixed characteristic},
 year = {2026}, eprint = {2512.00886}, archivePrefix = {arXiv},
 doi = {10.48550/arXiv.2512.00886}, url = {https://arxiv.org/html/2512.00886v3}, note = {verified},
 annote = {Record and full-text Theorem A opened; not the entire 72-page proof. First submitted 30 November 2025; v3, 2 September 2026. The title changed between versions.}
}
'''
bp=W/'references.bib'
if '@misc{Stacks04GK,' not in bp.read_text():bp.write_text(bp.read_text()+extra)
# Metadata audit of all supplied folders, based on the manually read scope ledger.
pages=json.loads((B/'source_audit/page_index.json').read_text())
manual={
 'K43-01':('Class-field cohomology; Artin–Takagi statements','Scans 1–4 and 10 contain headings; no secure authorial date or total page count. Archive pencil numbering is not authorial pagination.'),
 'K43-03':('Fundamental two-extension; Witt vectors; admissibility; flags','No authorial date established. Title/brief-heading evidence retained in the supplied short notes; no bibliographic date is promoted to a manuscript date.'),
 'K43-04':('Injective modules; flag and path algebra','Supplied transcription read in full. Its short notes describe an earlier incomplete checking session; this is not evidence that scans were checked in this run.'),
 'K43-05':('Topological path algebra; local Jacobians; Weil cohomology','The transition from Zariski to proposed Weil cohomology is explicit. No secure date established.'),
 'K43-06':('Local duality; radicial groups; proposed Weil site; Tate sheets','Scans 85/87 are reused bibliography; publication dates on them do not date adjacent handwritten sheets. Scans 143/144 are supplied in this folder after 93.'),
 'K43-07':('Tate global duality; l-adic representations; Lie algebras','No short notes file supplied, but every transcription face was read. Scans 145/146 continue the English duality material.'),
 'K43-08':('Support Ext; Hom and Ext tables; primitive torsors; F,V','Scan 164 explicitly labels Ext in the geometric case. Canceled entries remain canceled. No authorial date established.'),
 'K43-09':('Formal and affine groups; coalgebras; pro-categories','Field and arbitrary-ring questions are separated. No authorial date established.'),
 'K43-10':('Length categories; formal modules; Tate–Lang pairings','Covers/headings on 198/203 do not supply a new mathematical theorem. Last sheet 208 is an archival label, not proof of a 208-page authorial count.')}
rows=[]
for folder,(topic,note) in manual.items():
    pp=[x for x in pages if x['file'].endswith(folder+'_transcription.tex')]
    rows.append([folder,'43',','.join(str(x['scan']) for x in pp),len(pp),'entire supplied transcription read',topic,note])
rows.insert(1,['K43-02','43','17–31 (listed range; no file)',0,'listed in TOPIC.md but absent from ZIP','Unavailable source','No reconstruction or verdict is invented for its missing pages.'])
for folder,cote,topic,note in [
 ('MPL_43_094-142',43,'Local/curve duality and reused typescripts','46 supplied faces. Catalogue cote43 says207 pages; supplied scan labels reach208. Neither count is silently corrected.'),
 ('MPL_16+47+54+44',16,'Lefschetz/standard conjectures and reused sheets','54 supplied faces:1,3–23,25–56. Second pass applies only to this cote and scans1–53. Letter dates4.1.67 and6.1.1966 retained separately.'),
 ('MPL_16+47+54+44',47,'Fourier transform','Contextual cote; not mislabeled cote44 merely because the package index says44.'),
 ('MPL_16+47+54+44',54,'de Rham/Dieudonné comparison and EGA flatness sheets','Contextual cote. Reused printed sheets do not date the neighboring handwritten material.'),
 ('MPL_16+47+54+44',44,'Intermediate Jacobians and cycle equivalences','Catalogue says8 pages;9 supplied scan markers. The 1964 letter supplies a genuine date; exact day retained only where readable.')]:
    pp=[x for x in pages if x['file'].endswith(folder+'_transcription.tex') and int(x['cote'])==cote]
    rows.append([folder,str(cote),','.join(str(x['scan']) for x in pp),len(pp),'entire supplied transcription read',topic,note])
with (B/'SA19_folder_coverage.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['folder','cote','available_scans','faces','reading_status','contents','title_date_count_notes']);w.writerows(rows)
print(json.dumps({'root_claims':len(claims),'chronologies_specific':len(dates),'folder_records':len(rows),'new_references':['Stacks04GK','Galet2026'],'proof_correction':'C16 contravariant degree-two term explicitly retained'},ensure_ascii=False))
