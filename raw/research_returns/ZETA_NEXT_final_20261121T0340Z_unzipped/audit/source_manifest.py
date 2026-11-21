#!/usr/bin/env python3
import csv,hashlib
from pathlib import Path
base=Path(__file__).resolve().parents[1]
workspace=base.parent
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

with (base/'audit/INPUT_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path_relative_to_workspace','bytes','sha256'])
    for root in [workspace/'upload',workspace/'source']:
        for p in sorted(root.rglob('*')):
            if p.is_file():w.writerow([str(p.relative_to(workspace)),p.stat().st_size,sha(p)])

with (base/'audit/PRIMARY_CACHE_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['path_relative_to_work','bytes','sha256','status'])
    for p in sorted(base.rglob('*')):
        if p.is_file() and (p.suffix.lower() in ['.pdf','.png'] or
           (p.suffix=='.txt' and (p.parent.name in ['literature','sources'] or p.name in
            ['Borger_Lambda.txt','Huber_1994.txt','Scholze_PerfectoidSpaces.txt','Ito_Mieda_2020.txt']))):
            status='unused corroboration; omitted from final package' if 'Ito_Mieda' in p.name else 'research cache; omitted from final package, recover using source URLs'
            w.writerow([str(p.relative_to(base)),p.stat().st_size,sha(p),status])

rows=[
('Stark','https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0023/PPN356556735_0023.pdf',
 'Invent.Math.23(1974)135–152; volume scans142–159; Lem3 pp139–140; Lem4 eq11 pp140–141; eq7 p139; Lem7 p143; Lem8 p145; Lem9 pp145–146; Thm1prime eq24–25 p148',
 'Primary facsimile visually inspected at used locators; original proof of Lemmas8–9 read.'),
('GarciaLee','https://arxiv.org/pdf/2007.10313',
 'v4 (12March2021); eq1 p2; §3 pp16–17',
 'Primary text read, explicit C4 cross-check and class-number normalization.'),
('MilneANT','https://www.jmilne.org/math/CourseNotes/ANT.pdf',
 'v3.08(2020), Theorem4.3 printedp70/PDFp72','Exact source statement read.'),
('NC-Louboutin2001','https://doi.org/10.4153/CJM-2001-045-5',
 'Theorem1(1) p1195; §3 eq21 p1200','Primary paper read at used statements; relative formula visually checked.'),
('NC-Wei2021','https://arxiv.org/abs/2111.00617',
 'v1; Prop5.3 and proof pp19–20; Prop5.4 proof p21','Primary statements and applied estimate read.'),
('NC-YuanZhang2018','https://doi.org/10.4007/annals.2018.187.2.4',
 'Normalization p534; Theorem1.1 p535','Primary normalization and averaged formula checked.'),
('NC-GRPeriods2014','https://doi.org/10.4171/CMH/322',
 'Theorem1.1 p345; §2.3 pp351–352','Primary bound, normalization and product additivity checked.'),
('NC-GRPol2014','https://lmbp.uca.fr/~gaudron/art13.pdf',
 'Duke163(2014); constants p2058; pair convention p2059; Theorem1.4 p2060',
 'General-dimensional theorem and constants checked, including image.'),
('NC-Tsimerman2018','https://doi.org/10.4007/annals.2018.187.2.2',
 '§2.2 and Prop2.2 p382; Lem4.1 p384; Theorems4.2/5.2 p385; §6.3 Thm6.1/§6.5 p388',
 'Primary used statements and short ideal/definition-field arguments read; scope of counting input checked.'),
('NC-Remond2017','https://www-fourier.univ-grenoble-alpes.fr/~remond/5783.pdf',
 'Opening convention; Thm1.1/1.2 authorpp1–2; Prop2.3 p6; §7 preceding Lem7.5 pp17–18',
 'Primary statements checked for same-field and maximal-order scope; no reproof of source theorem.'),
('NC-Binyamini2020','https://arxiv.org/pdf/1809.05302',
 'v2(27May2021); §1.2 Theorem1 p2; §1.4 pp3–4',
 'Exact effective modular-curve replacement and original o-minimal scope checked.'),
('Alpoge','https://alpo.ge/remark.pdf',
 'Supplied step20 p4; ALPOGE_Main.lean endpoints; predicates in ALPOGE_Statements.lean',
 'Supplied theorem status accepted; endpoint files read, no IA01 re-audit or Lean rebuild.'),
('Masullo','supplied MASULLO_the-music-of-the-primes.pdf',
 '§1.2 PDFp12 unnumbered; empty intended Theorem13.3.1.2 PDFp522; §14.1.2 PDFp528',
 'Conditional claim; exact documentary status carried from ZETA_TWO MDOC01.'),
('Anderson1986','https://www.numdam.org/item/CM_1986__57_2_153_0.pdf',
 '§5.3 p178; Cor5.7.2/Rem5.7.3 p181','Carried through ZETA_TWO CM01; source proof not reread.'),
]
for branch in ['lambda','noncm']:
    for r in csv.DictReader((base/branch/'SOURCES.tsv').open(),delimiter='\t'):
        rows.append((r['key'],r['url'],r['locator'],r['scope']))
with (base/'audit/SOURCES.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['key','url_or_supplied_file','exact_locator','verification_scope']);w.writerows(rows)
print('Recorded input and source-cache fingerprints;',len(rows),'source entries.')
