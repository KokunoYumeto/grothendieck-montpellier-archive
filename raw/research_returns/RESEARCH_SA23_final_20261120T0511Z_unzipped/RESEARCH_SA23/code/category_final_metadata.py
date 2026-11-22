from pathlib import Path
import csv

root = Path('RESEARCH_SA23')
notes = root / 'notes'
p = root / 'sections/category_J.tex'
s = p.read_text()
if '\\label{cat:J9}' not in s:
    s += '\n' + (notes / 'category_J_ICM_comparison.tex').read_text()
    p.write_text(s)

p = notes / 'category_references.bib'
s = p.read_text()
if 'catGrothendieckICM1970' not in s:
    s += r'''
@inproceedings{catGrothendieckICM1970,
 author={Grothendieck, Alexander}, title={Groupes de Barsotti--Tate et cristaux},
 booktitle={Actes du Congr\`es international des math\'ematiciens (Nice, 1970)},
 volume={1}, pages={431--436}, publisher={Gauthier-Villars}, address={Paris}, year={1971},
 url={https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/GroupesB-T.pdf},
 note={Opened: six-page primary facsimile, title page and section5 pp434--435, especially p435 Remarks2--3 and last paragraph; checked 2026-11-20. Distinct from the 1974 Montreal course}}
'''
p.write_text(s)

p = notes / 'category_results.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
added = [
    ['cat:I12', 'Accessible functor, strong Ind extension and small pointwise Kan extension equivalences', 'Proved', 'sections/category_I.tex', 'cat:I1;cat:I5;cat:I8;cat:I11', '161-2/055', 'Also proves full restriction equivalence for arbitrary targets with the relevant filtered colimits'],
    ['cat:J9', 'Precise comparison with the ICM1970 mysterious-functor programme', 'Known', 'sections/category_J.tex', 'catGrothendieckICM1970;catFontaine1982;catColmezFontaine2000;catKisin2006;cat:J7;cat:J8', '161-5/023-029;ICM1970/435', 'ICM section5 Remarks2-3 and CF Introductionp3/reference23 directly checked; reconstructing crystalline BT data distinguished from false all-HT extension']
]
for values in added:
    if not any(row['id'] == values[0] for row in rows):
        rows.append(dict(zip(fields, values)))
for row in rows:
    if row['id'] == 'cat:L5':
        row['notes'] += '; formal jets retained as pro-algebra; ordinary sheaf-limit effectivity not asserted'
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

events = [
    ['cat:I11', '2026-11-20', 'GPT-6 Astra, root independent audit via collaboration', 'targeted proof check', 'Root fully audited idempotent-arrow presentation, graph-cocone closure with outgoing arrows, and sharp-cardinal poset bound; pass'],
    ['cat:I12', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'independent re-proof', 'Pointwise Kan formula and restricted Yoneda turn preservation into a direct universal-property calculation; all three functor equivalences proved'],
    ['cat:J9', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Opened actual ICM1970 facsimile section5 p435 and CF Introductionp3/reference23; exact primary link and numbered modern comparison written'],
    ['SA04-R1615-02', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Historical mysterious-functor lead checked against ICM1970 section5 Remarks2-3 and CF2000 Introductionp3; precise scope cat:J9'],
    ['cat:L5', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'targeted proof check', 'Re-read original162-5/022 pro-anneau and BD1.4.15 filtered topological pro-algebra; general-topos statement now retains finite jets, with ordinary limit effectivity explicitly separate'],
    ['K161-2-04 (161-2:55)', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Original scan055 directly inspected after full PDF retrieval; I12 supplies remaining core pointwise-Kan/functor equivalences'],
    ['K161-2-04 (161-2:60)', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Original scans060-062 directly inspected; positive2^c condition and Fil/cofinal-index definition confirmed'],
    ['K161-2-07 (161-2:112)', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Original scan112 directly inspected; finite-limit relative-classifier and pseudopullback scope confirmed']
]
p = notes / 'category_CHECK_EVENTS.tsv'
old = p.read_text()
with p.open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for event in events:
        if event[-1] not in old:
            writer.writerow(event)

p = notes / 'category_corrections.tsv'
with p.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
new = [
    ['CAT-CJ06', 'inputs/RESEARCH_SA23_study/readings/C_22_23_26_161-5.md', '420', 'Dossier identified without precise primary locator as mysterious-functor programme', 'ICM1970 exact title and section5 p435 Remarks2-3 checked; CF Introductionp3/reference23 confirms link. Crystalline reconstruction distinguished from false literal all-HT extension', 'cat:J9'],
    ['CAT-CL03', 'inputs/RESEARCH_SA23_study/readings/A2_161-4_161-6_162.md', '196-206;247-254', 'Unqualified transport of completion to an arbitrary ringed topos', 'Retain manuscript pro-ring and BD formal jet system. Ordinary inverse-limit sheaf quotient effectivity is an additional hypothesis; derived-completion qualification retained', 'cat:L5;cat:L7']
]
for values in new:
    if not any(row['id'] == values[0] for row in rows):
        rows.append(dict(zip(fields, values)))
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

p = notes / 'category_progress.md'
s = p.read_text()
s = s.replace('- Original 161-2 full scan download was interrupted; retry is running with chunk log. Actual supplied transcription55–62 and112 read.', '- Original161-2 PDF retry completed:112pages,48,394,048bytes; scans055,060–062,112 directly inspected. Supplied transcription55–62 and112 read.')
s = s.replace('I1-I11', 'I1-I12')
s += '\n## Final category additions\n- I12 gives all core scan055 functor equivalences, explicitly interpreting the small left Kan extension pointwise, and the full restriction equivalence.\n- J9 compares the opened ICM1970 section5 p435 Remarks2–3 with Fontaine/CF/Kisin; CF Introductionp3/reference23 independently documents the mysterious-functor link.\n- L5 retains the original pro-ring / BD pro-algebra category. No unrestricted ordinary sheaf-limit quotient effectivity is inferred.\n- Source/search log now gives exact locators, successful and failed openings, manuscript scan witnesses, and excluded contamination.\n- Root I11 targeted proof audit passed and recorded.\n'
p.write_text(s)
print('category statement rows', len(rows), '(correction rows; statement table separately updated)')
print('Added I12 and J9; recorded scan verification, I11 root audit and precise pro-algebra scope')
