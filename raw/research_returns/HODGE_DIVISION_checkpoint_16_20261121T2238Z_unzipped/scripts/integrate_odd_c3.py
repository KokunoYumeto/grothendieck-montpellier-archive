"""Integrate the fully reviewed complete odd rank-three symplectic result."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
proof='agents/g34_eightfolds/bireflection/csp6_odd/csp6_section.tex'
bib='agents/g34_eightfolds/bireflection/csp6_odd/csp6_bibitems.tex'
canonical='5f60952a684ac63ae6df6be85193ecb422688f23e1eb1aca1bcfbaa0eb6f4aba'
reviewed='3aec637863bd7c2e7773af72805b518b3f909ab64d1235b9aeeed2a09f5116eb'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==canonical
now=datetime.now(timezone.utc).isoformat()
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id']!='Q2bg' for r in rows)
(R/'research/gates_before_odd_c3.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{agents/imprimitive/lie_small_fields/higher_even_symplectic_all_fields_section.tex}'
assert anchor in s and proof not in s
s=s.replace(anchor,anchor+'\n'+r'\input{'+proof+'}')
anchor=r'\input{agents/imprimitive/lie_small_fields/higher_even_symplectic_bibitems.tex}'
assert anchor in s and bib not in s
s=s.replace(anchor,anchor+'\n'+r'\input{'+bib+'}')
a='proved by explicit symplectic descent and dual-weight pairs. Other\nsmall-field higher-rank Lie representations remain outside these\nexclusions.'
b=r'''proved by explicit symplectic descent and dual-weight pairs.
D-C3-01--03 excludes every ordinary quasisimple
$\operatorname{PSp}_6(q)$ core for odd $q\ge3$, including mixed
fields and all compatible outer, scalar and factor-permutation actions.
The complete similitude table, careful Clifford restriction and
projective semilinear descent at $q=9$ give uniform normalizer support
$3e/16$, forcing $e\le24$ and excluding every endpoint. No selfduality
premise is needed. The generic full-table premise is explicitly
L\"ubeck's dissertation and its official mathematical implementation,
not a separately refereed journal table. Other small-field higher-rank
Lie representations remain outside these exclusions.'''
assert a in s;s=s.replace(a,b);p.write_text(s)
for row in rows:
    if row['id']=='Q2i':
        a='Other small-field higher-rank Lie cores remain.'
        b=('D-C3-01--03 excludes every ordinary PSp6(q) quasisimple core for oddq>=3, '
           'allowing mixed fields and full normalizers. Complete CSp6 data, correct possibly reducible restriction, '
           'and q9 semilinear-involution descent give common support3/16 and e<=24, excluding every endpoint. '
           'No ESD premise is used; the generic table is explicitly a dissertation/official-data input. '
           'Other small-field higher-rank Lie cores remain.')
        assert a in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate']=row['finding_ids_or_current_gate'].replace(a,b)
rows.append(dict(zip(fields,['Q2bg','Prompt target2; all odd rank-three symplectic normal cores',
 'Can any mixed product of quasisimple PSp6(q) cores, q odd>=3, supply the actual rank-nine source?',
 'refuted',
 'D-C3-01--03:8811 all-parameter complete-CSp6 coefficient inequalities, careful Clifford restriction/semisimple fusion, q9 projective symplectic descent and81 dual weights,228 finite rows31428 spectra. Full normalizer support3/16 forces e<=24, versus>=169 for products and>=62 forq>=5; q3 quarter bound excludes min13. Both central kernels, all outer/scalar/permutation actions and larger inducing fields included. Whole root/peer proof/source/code checks PASS.'])))
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-C3-01--03','targeted proof check',
  'Root read the entire new mathematical proof and all precision amendments at'+reviewed+', then final status-only changes at'+canonical+'. Entire independent imprimitive audit read. PASS cyclic-inertia extension and two-constituent restriction, all semisimple primary centralizers, prime/composite cases, q9 projective involution rescaling/form descent without diagonal invariance, row weights, full outer coverage, tensor permutations and actual period budget. All exact source/code scopes separately recorded.',proof+'; agents/imprimitive/audit_odd_c3/PEER_AUDIT.md'),
 ('D-C3 generic and small exact certificates','computation or formal certificate',
  'Root read the full generic/extraction/parser and finite exporter/checker, plus all reused Fourier helpers. Actual generic8811 inequalities PASS0.664839s; after requested source-to-input equality assertions were added, final root rerun PASS2.484827s, comparing every original entry/degree/class length/class pair. Actual finite228rows31428spectra rerun PASS0.897714s, inputSHA055640d09bc5b5f2d7518d5227b65cfd22879ce3d7dd0b4b50877e1bd1bc59d2. Peer independently used new flint AST arithmetic and its distinct cyclotomic-polynomial Fourier routine:PASS2.862127s. These check new inequalities on complete cited data, not a new construction of the source tables.',
  'agents/g34_eightfolds/bireflection/csp6_odd/check_generic.py; agents/g34_eightfolds/bireflection/csp6_odd/check_small.py; agents/imprimitive/audit_odd_c3/independent_check.py'),
 ('D-C3 q9 descent certificate','computation or formal certificate',
  'Root read complete F9 checker and actually reran:PASS0.479204s,5760 invertible2x2 matrices,240 projective-involution cocycles,5760 fixed symplectic bases,19440 vector decompositions,6561 dual pairings and81/9/36 weight counts. Independent peer separate F9 tuple arithmetic PASS0.242371s. Finite matrices are dimension2 witnesses; the universal six-dimensional proof was read and checked mathematically, not inferred from enumeration.',
  'agents/g34_eightfolds/bireflection/csp6_odd/check_f9.py; agents/imprimitive/audit_odd_c3/check_f9_independent.py'),
 ('Luebeck1993 CSp6 complete-table scope','used and rechecked in this run',
  'Root freshly read every line of original-author Introductionpp3--4, complete construction overviewSection2.2pp18--21 andSection9pp78--79 from actual local original text; PDFSHA5d336441c90390b3f2072ed7ceaaacdfb83776549954d9d830dbabe4967af070. The complete electronic ordinary table is distinguished from the printed unipotent appendix and from a complete odd-Sp6 table. Full underlying construction was not rederived. Official GCT C3 full/unipotent inventory and neighboring C2 error warning freshly read. Web PDF opening failed onapplication/x-pdf; local read succeeded. Dissertation status remains explicit.',
  'agents/imprimitive/lie_small_fields/cache/Luebeck1993.pdf; https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/'),
 ('CTblLib 2.S6(3) and2.S6(3).2','used and rechecked in this run',
  'Root freshly opened both official table records, verifying ATLAS provenance, orders9170703360/18341406720, classes141/138 and stored fusion. Web metadata isversion1.3.10 generatedMay2025, actual exported package1.3.11. No independent construction of the ATLAS tables claimed.',
  'https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6(3).html; https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6(3).2.html'),
 ('D-C3 reused classification and geometric inputs','carried as background without fault found',
  'HHM2015 Chapter5Table1p35, Li-Xia2022Section2.2.2Table2.1p14, Liebeck2017Theorem2.4(i) with denominator sqrt(q)-1, and D-BI01 actual intermediate-cover factorization are used exactly as previously read and checked. No new root whole-source reading of those classifications or original Gluck proof is claimed. No reality theorem is a premise.',
  'agents/g34_eightfolds/bireflection/csp6_odd/SOURCES.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## The complete odd rank-three symplectic gate is closed\n\n'+now+' — Q2bg refuted and Q2i strictly reduced after whole root/peer proof, source and code reviews. D-C3-01--03 excludes all ordinary quasisimple PSp6(q), oddq>=3, including mixed fields and full normalizers. The q9 endpoint is resolved by projective semilinear descent and actual dual weight pairs; no selfduality premise is used. Complete electronic generic table provenance and dissertation status remain explicit. This is integration, not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('''\n## All ordinary odd rank-three symplectic suppliers are excluded\n\nD-C3-01--03 closes the entire odd-characteristic rank-three symplectic family, beyond the previously treated Weil representations. It controls the actual full normalizer after carefully allowing a reducible similitude restriction. The q9 field operator is treated directly, so no reality assertion or essentially self-dual hypothesis is needed. The inequality is applied to the actual finite intermediate cover and its period-map factorization; it is not an abstract parameter-count sufficiency claim.\n\nThese are representation-ring and finite-cover restrictions on the condition-A supplier gate at cote16 scan050. Their scheme, SGA finite-etale and weight-one realization placements have the exact framework locators already recorded. The result creates no detecting cycle, changes none of the proved integral constants, and supplies no new condition-I, Cayley-Hamilton, weight or motivic L-value inference. The generic full-table premise is accurately identified as a dissertation/official-data input, separately from the published ATLAS finite endpoints and published classification/character-ratio inputs.\n''')
p=R/'research/frameworks.tex';s=p.read_text();assert 'D-HES-01--06' in s
p.write_text(s.replace('D-HES-01--06','D-HES-01--06, D-C3-01--03'))
out={'date_utc':now,'integrated':['D-C3-01--03'],'whole_reviewed_math_sha256':reviewed,
     'canonical_sha256':canonical,'bib_sha256':hashlib.sha256((R/bib).read_bytes()).hexdigest(),
     'new_refuted_row':'Q2bg','main_gate':'Q2i','generic_table_source_status':'dissertation and official complete data'}
(R/'research/odd_c3_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
