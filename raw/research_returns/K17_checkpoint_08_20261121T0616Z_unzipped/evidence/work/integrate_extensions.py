from pathlib import Path
import csv, hashlib
from datetime import datetime, timezone

base=Path(__file__).resolve().parent.parent
work=base/'work'; out=base/'K17_package'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

path=out/'QUESTIONS.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
new=[
['Q2-R8-NONSIMPLICIAL','DHS2015 Thm1.1(ii); Berge-Martinet Cor6.9; Martinet5.2,10.1 and2014 appendix','Can every nonsimplicial rank8 projective-degree12 cell be eliminated, including ambient glue?','proved','K17-K12-R8-NONSIMPLICIAL; K17-K12-EXCESS5','Circuit equality gives Watson rank6 core; saturation and corrected rank8 index bound leave only binary glue. Every admissible class has an integral orientation reverser;192 exact classes checked. Simplicial cells remain.'],
['Q2-R8-INDEX5','Martinet2001 section11 and complete Table11.1 pp45-48;2014 appendix','Which minimum-frame indices and quotient types can remain at rank8?','proved','K17-K12-R8-INDEX5','Every residual cell has exactly13 minimum pairs and every minimum-basis index at most5. An explicit necessary frame-quotient list is proved from the source minimum-count column. This is not a complete cell or boundary classification.'],
['Q3-CUBIC','Actual Gamma action on the free pro-p group; WWE ordinary Prop2.2.6','Can pole separation accommodate cyclic odd Iwasawa torsion?','proved','K17-CUBIC-ODD','Conditional algebraic criterion with one cyclic module per character, Pair-NV and explicit Triple-NV. Full compact group and repeated roots retained; disjoint divisor extraction separates nested pair/triple poles. Arithmetic Triple-NV remains unproved and no new prime is asserted.']
]
known={r['id'] for r in rows}
for r in new:
    if r[0] not in known: rows.append(dict(zip(fields,r)))
for r in rows:
    if r['id']=='Q2-NEWDEG' and 'K17-K12-R8-NONSIMPLICIAL' not in r['finding_ids_or_current_gate']:
        r['finding_ids_or_current_gate']+='; K17-K12-R8-NONSIMPLICIAL; K17-K12-R8-INDEX5'
        r['detail']+=' Rank8 now reduces to simplicial13-pair cells of maximal minimum-basis index<=5, with a finite necessary frame-quotient list; no residual boundary computation is claimed.'
    if r['id']=='Q3-IRREG' and 'K17-CUBIC-ODD' not in r['finding_ids_or_current_gate']:
        r['finding_ids_or_current_gate']+='; K17-CUBIC-ODD'
        r['detail']+=' A conditional cubic companion criterion handles cyclic odd torsion if Pair-NV and Triple-NV hold; these extra arithmetic inputs are not verified, so it adds no prime.'
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)

events=[
('K17-CUBIC-ODD','targeted proof check','PASS conditional criterion; no arithmetic Triple-NV verification','Entire final TeX read in two consecutive pieces; compact basis, bounded rational changes, parity, resonances, actual companions, all nested-divisor cases and invariance checked. Independent full audit read. SHA256 '+hashlib.sha256((work/'odd_torsion_cubic_section.tex').read_bytes()).hexdigest()),
('K17-K12-R8-TEX-ROOT','targeted proof check','PASS final entire proof','Read complete final rank8 TeX, matching prior whole MD/code/source audit and192-class exact rerun; independent archive audit received. Only nonsimplicial chain generators removed.'),
('K17-K12-EXCESS5-ROOT','targeted proof check','PASS','Entire inflation/excess-five TeX read; fixed cone incidence convention gives dJ=-Jd and J^2=0 after invert2; no contraction inferred. Source attribution EVGS retained; subsequent all-glue theorem cited.'),
('K17-K12-R8-INDEX5','targeted proof check','PASS complete short deduction','Entire proof and MD read, plus complete Martinet section11 setup and Table11.1 pp45-48. All retained/excluded rows checked against13-pair cap; corrected global index input retained. Published coverage cited, not rerun.'),
('SRC-MARTINET-MINIMUM-TYPES','used and rechecked in this run','PASS','Freshly read section11 pp45-48 in full, including minimum-configuration meaning of s and every row of both table parts. No claim to rerun the classification.'),
('SRC-RECENT-STEINBERG2026','used and rechecked in this run','No replacement integral endpoint found in the inspected statements','Retrieved primary Patzt-Willwacher2610.12263 and Pal-Payne2609.38735 PDFs. Read PW introduction/TheoremsA-C pp2-4 and PP introduction/Thm1.1 pp1-2. Rational Hopf/graph results do not supply the required localized integral vanishing. Full proofs not audited or used.')
]
with (work/'root_checks.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,result,scope in events:
        w.writerow([sid,now,'GPT-6 Astra Pro; effort not exposed; K17 root',typ,result,scope])

with (out/'LEDGER.md').open('a') as f:
    f.write('\n### Checked rank-eight reduction and conditional cubic extension — '+now+'\n\n')
    f.write('K17-K12-R8-NONSIMPLICIAL removes every nonsimplicial rank8 endpoint cell, including ambient glue. Root read final full TeX after the earlier complete proof/code/source check and exact192-class replay; archive independently passed the whole proof and sources. K17-K12-R8-INDEX5 then bounds every residual minimum-frame index by5 and gives the exact necessary quotient types from Martinet section11/Table11.1. The residual rank8 gate is now only simplicial13-pair cells with these small frame quotients. This strictly shrinks the main K12 chain gate, but is not an H5 or K12 vanishing.\n\n')
    f.write('K17-CUBIC-ODD is fully checked as a conditional algebraic theorem, with root and independent tripod whole-proof readings. It handles cyclic odd torsion character by character, including repeated roots, under explicit pair and triple nonvanishing conditions. No arithmetic Triple-NV is supplied. It is not counted as a weaker arithmetic all-prime gate by itself. The norm-compatible unit bridge is under active investigation.\n\n')
    f.write('Fresh October2026 Steinberg/graph papers were retrieved from primary arXiv PDFs. Their inspected main statements concern rational Hopf structures and rational K-theory; they do not settle the localized integral endpoint. Full source proofs were not audited or used. The next scheduled review remains04:15:36UTC, next checkpoint04:00:36UTC.\n')
with (out/'IMPLICATIONS.md').open('a') as f:
    f.write('\n## Further endpoint reductions and the cubic criterion\n\n')
    f.write('K17-K12-R8-NONSIMPLICIAL eliminates all nonsimplicial rank8 degree12 cells, even with proper ambient glue. K17-K12-R8-INDEX5 confines surviving cells to13 minimum pairs and frame index at most5, with an explicit necessary quotient list. These narrow the remaining K12 computation; they do not assert full H5GL8 or K12 vanishing. Together with the rank10 trimodular classification, the current exact chain reductions are stronger than those at the first scheduled review.\n\n')
    f.write('K17-CUBIC-ODD supplies a fully proved conditional separation criterion for one cyclic odd Iwasawa torsion component per character. Pair-NV and a specified class-three Triple-NV replace the earlier absence of odd torsion. The latter remains arithmetic data to be proved, and even cyclicity/pair nonvanishing outside Greenberg remain explicit hypotheses. This theorem adds no unconditional prime to LM6 A45 and does not prove or disprove Greenberg.\n')
with (out/'RESUME.md').open('a') as f:
    f.write('\nFurther checked progress '+now+': rank8 all-nonsimplicial theorem and index<=5 necessary frame-type list are now integrated, with full root/author and archive checks. Cubic criterion K17-CUBIC-ODD is integrated after Greenberg, with root/author/tripod whole reads; arithmetic Triple-NV not proved. Rank10 properindex3 glue currently has an exploratory26-class reduction, not yet promoted; tripod is certifying minima and boundaries. Archive pursues universal norm-compatible units to Pair-NV. Build uses3passes via work/build_pdf.py, not default pdflatex.\n')
print('Integrated checked extensions and metadata')
