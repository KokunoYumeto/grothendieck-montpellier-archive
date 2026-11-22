from pathlib import Path
import csv

root = Path('RESEARCH_SA23')
notes = root / 'notes'
p = root / 'sections/category_I.tex'
s = p.read_text()
addition = (notes / 'category_I_good_rank.tex').read_text()
if '\\label{cat:I11}' not in s:
    marker = '\\subsection{The relative classifying topos}'
    if marker in s:
        s = s.replace(marker, addition + '\n' + marker)
    else:
        s += '\n' + addition
    p.write_text(s)

p = root / 'sections/category_J.tex'
s = p.read_text()
marker = 'Kisin~\\cite[Theorem (0.3), Corollary (2.2.6)]{catKisin2006} proves'
scope = r'''The field hypotheses of these sources match our scope.  Fontaine's
Introduction, printed p.~529, assumes a perfect residue field, not a
finite one.  Colmez--Fontaine's Introduction, p.~2 of the opened author
version, assumes a perfect field $k$ and a finite totally ramified
extension of $W(k)[1/p]$.  Kisin makes the same assumptions at the
start of his Introduction.  Thus none of the three applications here
silently narrows the manuscript to finite extensions of $\mathbf Q_p$.
These are statements at the rational or isogeny level; no assertion
about a chosen integral lattice at $p=2$ is being substituted for them.

'''
if scope not in s:
    s = s.replace(marker, scope + marker)
    p.write_text(s)

p = root / 'sections/category_L.tex'
s = p.read_text().replace(
    'of the nilpotent jets of its simplicial nerve, with the topology\ninduced from the base and all simplicial and jet-transition maps.',
    'of the nilpotent jets of its simplicial nerve, with all simplicial\nand jet-transition maps as morphisms, and coverings induced by the\nchosen topology on the base.')
p.write_text(s)

p = notes / 'category_results.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['id'] == 'cat:L5':
        row['status'] = 'Known'
        row['notes'] = 'Hypotheses derived in L3-L4; BD1.4.15 applies internally; no finite projectivity substitution'
if not any(row['id'] == 'cat:I11' for row in rows):
    rows.append(dict(zip(fields, [
        'cat:I11', 'Positive cardinal-filtration equality under the sharp-cardinal condition',
        'Proved', 'sections/category_I.tex', 'cat:I1;cat:I2;cat:I3;cat:I7;cat:I9',
        '161-2/060-062', 'Removes retract by explicit small filtered presentation; includes mu=2^c, c>=pi; distinguishes all-rank cocomplete accessibility from Fil equality'
    ])))
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

p = notes / 'category_corrections.tsv'
with p.open(newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['id'] == 'CAT-CI03':
        row['line'] = '155-164;395-412;420-439'
        row['correction'] += '; positive equality at sharp ranks, including mu=2^c, proved in I11'
        row['where_proved'] += ';cat:I11'
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
    writer.writeheader()
    writer.writerows(rows)

events = [
    ['cat:I10', '2026-11-20', 'GPT-6 Astra, root independent audit via collaboration', 'targeted proof check', 'Root audited powerset counterexample: directed countable covers force cofinality of countable subsets; mu+-presentability verified; pass'],
    ['cat:L7', '2026-11-20', 'GPT-6 Astra, root independent audit via collaboration', 'targeted proof check', 'Repaired finite total-order Euler contraction, derived constant limit and explicit ordinary-module hypothesis audited; pass'],
    ['cat:L8', '2026-11-20', 'GPT-6 Astra, root independent audit via collaboration', 'targeted proof check', 'Local smooth lifting and jet cocycles give complete infinitesimal-crystal reconstruction; pass. Topology wording clarified: simplicial/jet maps are morphisms, not declared coverings'],
    ['cat:I11', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'independent re-proof', 'Retracts removed by adjoining representative idempotent arrows and small filtered closure in C/X; exact sharp-cardinal bound retained throughout'],
    ['K161-2-04 (161-2:60)', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Positive mu=2^c assertion proved cat:I11; unrestricted equality refuted cat:I10; manuscript conventions translated by kappa=pi+'],
    ['cat:J7', '2026-11-20', 'GPT-6 Astra, inherited effort, crystalline_categories', 'used and rechecked in this run', 'Fontaine1982 p529, Colmez-Fontaine author intro p2 and Kisin author intro assume arbitrary perfect residue field and finite totally ramified K/K0; exact scope now explicit in section']
]
p = notes / 'category_CHECK_EVENTS.tsv'
old = p.read_text()
with p.open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for event in events:
        if event[-1] not in old:
            writer.writerow(event)

p = notes / 'category_references.bib'
s = p.read_text()
s = s.replace('Opened: sections 3, 5.2 and 6.2 checked on 2026-11-20', 'Opened: Introduction p529 (perfect residue field), Proposition 1.6(iii)--(iv), sections 3.6--3.7 and 3.10, 5.2 and 6.2 checked on 2026-11-20')
s = s.replace('Opened: Theorem A, section 4.1', 'Opened: Introduction p2 of author version (perfect residue field), Theorem A, section 4.1')
s = s.replace('extracted with dvi2tty; Theorem (0.3)', 'extracted with dvi2tty; Introduction (perfect residue field), Theorem (0.3)')
p.write_text(s)

p = notes / 'category_progress.md'
s = p.read_text()
s = s.replace('- cat:I6: relative classifying', '- cat:I10: cocomplete powerset counterexample resolves scan060 open Fil equality question; root audited and passed.\n- cat:I11: positive Fil equality at exact sharp-cardinal ranks, including mu=2^c, proved by removing retract through a bounded filtered presentation. All-rank cocomplete accessibility distinguished from Fil equality.\n- cat:I6: relative classifying')
s = s.replace('Tangential scan055 claims about arbitrary fibred-category colimits, prorepresentability and adjoints have not yet all received independent expanded proofs; assess whether required under I.1 scope rather than calling entire page settled.', 'The requested accessibility equivalences/cardinal hypotheses are covered by I1-I11. Tangential scan055 claims on arbitrary fibred-category colimits, prorepresentability and adjoints are not asserted as audited results.')
s += '\n## Checkpoint02 source and proof audit\n- Fontaine1982 Introduction p529, CF2000 author Introduction p2, Kisin2006 Introduction all explicitly permit arbitrary perfect residue field; scope paragraph and bibliography updated.\n- Root independently audited I1-I10, J7-J8 and L1-L8; repaired L7/L8 passed. L8 topology wording clarified.\n- L5 registry status normalized to Known, with derived-hypothesis qualification retained in notes.\n'
p.write_text(s)
print('Updated I11, source scopes, L8 topology, registry, corrections and targeted root audit events')
