#!/usr/bin/env python3
"""Integrate verified results after checkpoint07; safe to repeat."""
from pathlib import Path
import csv, json, shutil

root=Path(__file__).resolve().parents[1]
p=root/'RESEARCH_SA08_C3_D031_paper.tex';s=p.read_text()
for anchor,new in [('A_single_disk_gate','A_single_disk_localization_obstruction'),
                   ('A_single_disk_localization_obstruction','A_countable_gate'),
                   ('A_countable_gate','A_three_disk_gate'),
                   ('A_deep_tail_H2','B_p3_second_repair'),
                   ('B_p3_second_repair','B_odd_prime_second_repair'),
                   ('A_mixed_cell_cleanup','A_integral_mixed_cleanup'),
                   ('A_integral_mixed_cleanup','A_global_prism'),
                   ('A_global_prism','A_reference_controlled_completion')]:
    line='\\input{sections/'+new+'}'
    old='\\input{sections/'+anchor+'}'
    if line not in s:
        assert old in s and (root/'sections'/f'{new}.tex').exists()
        s=s.replace(old,old+'\n'+line)
line='\\input{sections/A_reference_truncation_obstruction}'
anchor='\\input{sections/A_reference_controlled_completion}'
if line not in s:
    assert anchor in s
    s=s.replace(anchor,anchor+'\n'+line)
p.write_text(s)

fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p=root/'notes/A_root_results.csv'
with p.open(newline='') as f:rows=list(csv.DictReader(f))
for r in rows:
    if r['id']=='A-CS':
        r['depends_on']='A-001–006; A-S09-24; A-S09-27; A-S09-29'
        r['notes']='A-S09-29 reduces the common-source assertion exactly to sources and targets internal to E_omega^[d], the countable single-disk class. Target pair can have the same P(N); source may have another cutoff. Actual inclusions and replacements, all uniform exactness bounds and properness are proved. The restricted assertion remains undecided.'
    if r['id']=='A-TL':
        r['depends_on']='A-001–006; A-S09-24; A-S09-29; A-S09-30'
        r['notes']='A-S09-30 gives an all-arrow localization equivalence with F_3,omega^[d]: countable objects with first skeleton P_r(N), r=1,2,3 constant across weights, global comparison through d, and rows through d+2 exact from N. This is proper in C_omega^[d]. Actual pair/triple/fold diagrams prove all finite-word and relation comparisons. Terminality there remains undecided.'
if not any(r['id']=='A-S09-29' for r in rows):
    rows.append(dict(zip(fields,[
        'A-S09-29',
        'Countable actual subobjects preserve the free first skeleton and all exactness ranges in finite diagrams; their full inclusions induce equivalent localizations, giving proper countable internal gates for both integral questions',
        'Proved','sections/A_countable_gate.tex; A-S09-29',
        'A-S09-24; A-S09-27; actual countable PD closure and finite localization witnesses; Stacks0CRM method with full added-structure proof',
        'No new manuscript transcription',
        'Common-source gate E_omega^[d]; terminal gate C_omega^[d]. Uncountable square-zero K(V,2) in weight b<N and form d+1 proves properness. Both independent full referees passed; support/flatness retained.'
    ])))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

p=root/'notes/A_root_CHECK_EVENTS.tsv'
with p.open(newline='') as f:events=list(csv.DictReader(f,delimiter='\t'))
new=[
 ('A-S09-28','targeted proof check','Full written proof checked19:54:56UTC, then doubled-skeleton extension checked20:10UTC: exact PD indecomposable quotient, prime coefficient formula, scalar germ and orientation independence, actual psi over G, and r i1=r i2=id; h i1=id; h i2=u. This kills the same class inside C^[d].'),
 ('A-S09-29','targeted proof check','Authored and checked exact countable finite-diagram closure: finite monomial index extraction, all normalized witnesses, original uniform cutoffs, fixed countable vertices, finite equality-witness localization proof and typed internal-source comparisons; actual uncountable square-zero properness. Both independent full referees passed20:07–20:09UTC.'),
 ('A-S09-30','targeted proof check','Full proof checked20:12:34UTC: all single/pair/triple copy maps and fold, exact comparison cocycle, actual Phi_N on finite-object full subcategories, internal projection naturality, finite-word fullness and finite-relation faithfulness, countable whole-skeleton closure, both properness witnesses and support/flatness.'),
 ('C34','used and rechecked in this run','Reopened supplied B_C3_truncated_repairs.tex at20:11UTC for exact hypothesis scope: strict truncated PD-DGA isomorphism in every weight and simplex with target-map agreement remains required. Only the full under-P map and outgoing differential at the truncation boundary are dropped. Reference-controlled low-form additions have not been shown to meet this hypothesis.'),
]
known={(e['statement_id'],e['type'],e['outcome']) for e in events}
with p.open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,result in new:
        if (sid,typ,result) not in known:
            w.writerow([sid,'2026-11-19','GPT-6 Astra (OpenAI), Pro mode, RESEARCH_SA08_C3_D031/root',typ,result])

p=root/'RESEARCH_SA08_C3_D031_report.md';s=p.read_text()
s=s.replace('A-S09-27 reduces this exactly to sources and targets internal to the proper smaller class E^[d]: one first-skeleton disk per weight from a cutoff N, global coefficient exactness through d, and rows through d+2 exact from N. The target pair can share N; the source has its own cutoff. This restricted assertion remains undecided.','A-S09-29 reduces this exactly to countable sources and targets internal to E_omega^[d], retaining the single-disk first skeleton, global comparison through d and rows through d+2 exact from its cutoff. Target pair can share N; source may have another cutoff. This restricted assertion remains undecided.')
s=s.replace('A-S09-24 proves equivalence with the all-arrow localization of C^[d] for every fixed finite d. Terminality there remains undecided.','A-S09-29 proves equivalence with the all-arrow localization of the proper countable subcategory C_omega^[d]. Terminality there remains undecided. A-S09-28 supplies an explicit obstruction to substituting the single-disk localization.')
s=s.replace('A-S09-29 proves equivalence with the all-arrow localization of the proper countable subcategory C_omega^[d]. Terminality there remains undecided. A-S09-28 supplies an explicit obstruction to substituting the single-disk localization.','A-S09-30 proves equivalence with the all-arrow localization of F_3,omega^[d]: countable objects with one, two or three first-skeleton disks per weight, global comparison through d, and the specified common row cutoff. Terminality there remains undecided.')
more=[
 '| A: countable internal reductions | Proved | A-S09-29 constructs countable subobjects of finite diagrams, preserves the chosen free first skeleton and every exactness range, and proves the two localization equivalences and strict properness. |',
 '| A: single-disk localization comparison | Refuted | A-S09-28 detects an explicit nonidentity endomorphism by prime-weight scalar germs and kills that same endomorphism by a doubled-skeleton diagram in C^[d]. |',
 '| A: three-copy terminal-localization reduction | Proved | A-S09-30 constructs strict pair and triple comparison diagrams, proves functorial transport and finite-word equivalence, and gives the proper countable gate F_3,omega^[d]. |',
 '| A: integral mixed-cell cleanup | Proved in simplex two | A-S09-31 constructs integral simultaneous repairs through form three with a compatible localized carrier, unchanged first skeleton, and the stated actual target maps. It includes no all-simplex positive-degree comparison. |',
 '| A: full prism and actual common reference | Proved over Z_(2) | AT26 supplies every prism face and an actual strict path map for the specified global free-cell presentation, with the reference at endpoint zero. |',
 '| A: reference-controlled finite-range completion | Proved with verified application | AT27 constructs all-simplex repairs and simultaneous horizontal restoration from the actual reference/path data of AT26. It gives comparison through degree three in that application; the strict C34 truncation isomorphism remains unconstructed. |',
 '| A: next prime-three period and repair | Proved | A-L20 gives the first pure-tail arity-two H3=Z/3 class, proves its survival under the preceding H2 repair and all based saturation, and proves that every admissible target map in the stated range extends across its actual repair. |',
 '| A: specified next repair at every odd prime | Proved | A-L21 gives the surviving order-p H3 class and a zero relative period for every actual target map at every odd prime, with the displayed simultaneous K(2) repair. The arbitrary-prime proof uses the actual resolution column and two exact identities; it includes no convergence assertion for later classes. |',
 '| A: reference paths imply prescribed strict truncations | Refuted | AT28 gives an explicit strict PD path from the section-projection to the identity on the AT12 target, with a fully admissible common reference, while AT12 still excludes the prescribed truncation agreement at every odd prime. |',
]
anchor='| B: exact v4 statement and conventions |'
for row in more:
    if row not in s:s=s.replace(anchor,row+'\n'+anchor)
compute='| A_single_disk_prime_germ_certificate.py | 12,197 exact coefficient and endomorphism checks; cutoffs2–6 and prime weights through23 for all normalized PD monomials, with the stated extra endomorphism range | 0.03525488199375104 |'
if '| A_single_disk_prime_germ_certificate.py |' not in s:
    s=s.replace('| B_prime_transfer_certificate.py |',compute+'\n| B_prime_transfer_certificate.py |')
s=s.replace('with the stated extra endomorphism range | 0.03525488199375104 |','with the stated extra endomorphism range | 0.016267184997559525 (latest run; first run0.03525488199375104) |')
compute2='| B_p3_second_repair_probe.py | Complete arity-two degree-two lattices in unshifted weights1–13; 13 weight cases, nontrivial ranks1,1,6, the exact order-three factor, two named differential identities and minors2,-12 | 0.011249552000663243 |'
if '| B_p3_second_repair_probe.py |' not in s:
    s=s.replace('| B_prime_transfer_certificate.py |',compute2+'\n| B_prime_transfer_certificate.py |')
compute3='| B_odd_prime_second_repair_certificate.py | Complete low-weight arity-two lattices at p=3,5,7 in13,41,85 weight cases (139 total), all named identities, nonboundary detectors and unit/order-p minors | 0.05639083599089645 |'
if '| B_odd_prime_second_repair_certificate.py |' not in s:
    s=s.replace('| B_prime_transfer_certificate.py |',compute3+'\n| B_prime_transfer_certificate.py |')
compute4='| A_integral_reference_homotopy_certificate.py | 141,947 finite checks of the actual coordinate-selector homotopy, its PD/cochain equations and simplicial naturality in the recorded ranges | 0.094451979 |'
if '| A_integral_reference_homotopy_certificate.py |' not in s:
    s=s.replace('| B_prime_transfer_certificate.py |',compute4+'\n| B_prime_transfer_certificate.py |')
marker='## Post-checkpoint07 record and retained-PDF audit'
if marker not in s:
    s+='''\n'''+marker+'''\n\nThe A-CS notes cell in checkpoint07's consolidated CSV retained the earlier C^[d] gate, although the A-S09-27 row, report and integrated proof already recorded E^[d]. That notes cell is corrected in the current register; the checkpoint ZIP is unchanged. A-S09-29 subsequently gives the countable gates stated in the current outcome table.\n\nAll13 retained standalone QA PDFs were rebuilt from the corrected section sources, with their citation and repeated-pass steps completed. This replaces an older partial closed-boundary PDF and resolves the older descent-wrapper citation warning. Their final logs have zero overfull boxes, zero undefined references and zero LaTeX warnings. All45 pages were rendered in the verification run; build plus render took32.046229675004724 seconds. We viewed the first and final page of each PDF in a26-page contact sheet, with no clipping or overlap found. The main154-page PDF remains the separately checked build38 until the next integrated build. Detailed per-file times and final log counts are in logs/standalone_pdf_verification.json. Earlier diagnostic stdout logs are retained as historical records.\n'''
p.write_text(s)

p=root/'logs/standalone_pdf_verification.json'
if p.exists():
    a=json.loads(p.read_text());a['visual_inspection']='Root viewed the first and final page of all13 retained PDFs in the26-page contact sheet at20:10UTC; no clipping, overlap or missing glyphs observed.'
    p.write_text(json.dumps(a,indent=2)+'\n')
    shutil.copyfile(root.parent/'qa_standalone_committed/contact.png',root/'qa/standalone_contact.png')
