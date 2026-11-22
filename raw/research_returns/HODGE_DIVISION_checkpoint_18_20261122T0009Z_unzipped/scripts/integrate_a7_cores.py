"""Integrate the fully reviewed transitive A7-cover exclusion."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
proof='research/a7_cores/a7_section.tex'
bib='research/a7_cores/a7_bibitems.tex'
reviewed='647b2870393b00b531be6cfb2efde3b1b9079a9d188653b66b10a32def71c71a'
p=R/proof
assert hashlib.sha256(p.read_bytes()).hexdigest()==reviewed
s=p.read_text()
old=('New root derivation, with an author whole-proof reading completed.\n'
     'The complete GAP spectrum computation and a separate exact Python\n'
     'reconstruction passed. Independent whole-proof review is pending.')
new=('New root derivation. The complete proof and all source scopes were\n'
     'read by the author and an independent reviewer; both checks passed.\n'
     'The complete GAP spectrum computation, the separate exact Python\n'
     'reconstruction and an independently written polynomial-Fourier\n'
     'certificate passed. The independent audit is recorded in\n'
     '\\texttt{A7\\_CORE\\_PEER\\_AUDIT.md}.')
assert old in s
p.write_text(s.replace(old,new))
canonical=hashlib.sha256(p.read_bytes()).hexdigest()
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id']!='Q2bh' for r in rows)
(R/'research/gates_before_a7.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{agents/g34_eightfolds/bireflection/csp6_odd/csp6_section.tex}'
assert anchor in s and proof not in s
s=s.replace(anchor,anchor+'\n'+r'\input{'+proof+'}')
anchor=r'\input{agents/g34_eightfolds/bireflection/csp6_odd/csp6_bibitems.tex}'
assert anchor in s and bib not in s
s=s.replace(anchor,anchor+'\n'+r'\input{'+bib+'}')
old=('in all degrees by D-BI-08, D-EX and D-UP. Long-shape tensor constructions\n'
     'and the remaining small exceptional alternating covers require separate\n'
     'arguments.')
new=(r'in all degrees by D-BI-08, D-EX and D-UP. D-A7-01--03 excludes'+ '\n'
     r'every transitive $A_7$-cover core in the nonsplit problem, including'+ '\n'
     r'the double, triple and sixfold covers and all compatible normalizers.'+ '\n'
     r'The sole standard-factor exception is excluded by its actual split'+ '\n'
     r'polarization in the single-factor case and a scalar-multiplier budget'+ '\n'
     r'in the tensor case. Long-shape tensor constructions for $n\ge15$'+ '\n'
     'still require separate arguments.')
assert old in s;s=s.replace(old,new);p.write_text(s)
for row in rows:
    if row['id']=='Q2i':
        old='long-shape tensor cases and residualA7/covers remain.'
        new=('D-A7-01--03 excludes every transitive A7 core, including all double/triple/sixfold covers, '
             'full compatible normalizers and larger inducing fields. The complete57-row1884-spectrum certificate '
             'leaves only standard outer reflections; the actual multiplier budget excludes standard tensors, '
             'and BI08 excludes the single standard factor by actual splitness. Long-shape tensor cases for n>=15 remain.')
        assert old in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate']=row['finding_ids_or_current_gate'].replace(old,new)
rows.append(dict(zip(fields,['Q2bh','Prompt target2; residual transitive A7-cover supplier gate',
 'Can any transitive A7 quasisimple central-product core supply a nonsplit rank-nine source?',
 'refuted',
 'D-A7-01--03: all nonlinear universal6.A7 rows and all compatible6.A7.2 extensions,57rows1884nonscalar spectra, give quarter support outside the ordinary standard row. Standard tensors satisfy e<=27/4<36; the single standard row forces actual split polarization by D-BI08. Other cores satisfy e<=6, and all degree4/6 endpoints cost at least24>2e+6. Transitivity and nonsplit hypotheses explicit. Whole author/peer proof and source audits PASS; independent polynomial-Fourier certificate PASS.'])))
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-A7-01--03','targeted proof check',
  'Root whole-proof reading completed before peer audit; reviewed mathematicalSHA'+reviewed+'. Root now read the entire independent whole-proof audit, PASS, including universal-cover lifting, nonsplit cyclic-extension relation, standard-row identification, actual scalar extraction, transitivity, and single-factor actual splitness. Only status wording changed for canonicalSHA'+canonical+'.',
  proof+'; agents/g34_eightfolds/bireflection/A7_CORE_PEER_AUDIT.md'),
 ('D-A7 complete GAP and Python certificates','computation or formal certificate',
  'Actual full GAP export/scan PASS57rows1884nonscalar spectra,tool wall1.250305s, including orthogonality/powermaps/fusion. Separate root Python PASS0.087247s using previously reviewed Ramanujan helper, not a third new arithmetic algorithm. All selection/spectra/endpoints checked. InputSHA185c2a90af296395c33ad8c7c5e839fadba5fffaeda3aacac2d99c8d20c906ab. Only exceptions extensionrows3/4,class26,standarddegree6,support1.',
  'research/a7_cores/export.g; research/a7_cores/scan.json; research/a7_cores/check.py; research/a7_cores/checked.json'),
 ('D-A7 independent whole-proof and exact audit','independent re-proof',
  'Peer /root/g34_eightfolds recorded actual completed audit19:29:43UTC. Full mathematical proof, author programs, source scopes and dependencies read. Independently written cyclotomic-polynomial Fourier arithmetic imports no root helper/selected rows/scan; actualPASS57rows1884spectra1.901178s. All outer selection and small endpoints reconstructed. Root read full report; no new construction of the original ATLAS tables claimed.',
  'agents/g34_eightfolds/bireflection/A7_CORE_PEER_AUDIT.md; agents/g34_eightfolds/bireflection/audit_a7_core.py; agents/g34_eightfolds/bireflection/audit_a7_core.json'),
 ('A7 universal covers and automorphisms','used and rechecked in this run',
  'Root freshly read HHM2015 Chapter4 opening paragraph numberedp31, and official ATLAS-derived6.A7/6.A7.2/A7/A7.2 pages. GAP ExtensionInfo(A7)=[6,2] actually queried. The A7.2 record explicitly identifies S7 and Aut(A7). Orders15120/30240,classes40/35,stored normal fusion checked. Webversion1.3.10May2025 is distinguished from actual package1.3.11. Exact identifiers are locators; no invented printed ATLAS page. Peer independently reread same original scopes.',
  'research/a7_cores/a7_bibitems.tex; agents/g34_eightfolds/bireflection/sources/HissHusenMagaard2013.pdf'),
 ('D-BI08 and D-AST01 in A7 endpoint','used and rechecked in this run',
  'Root reread entire scalar_standard_section.tex and D-AST section. BI08 permits larger inducing field initially and forces actual polarization splitness; AST every-power trace proof holds alln>=3. The n7 normalizer assertion is separately proved using AutA7=S7. Independent peer reread both exact scopes. No statement of arbitrary nontransitive mixtures or exclusion of split single-standard case.',
  'agents/g34_eightfolds/bireflection/scalar_standard_section.tex; research/a7_cores/a7_section.tex')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
(R/'research/a7_cores/ATTEMPTS.md').write_text('''# A7 calculation and residual alternating leads

The first inventory call mistakenly requested ExtensionInfoCharacterTable on the extension table A7.2. GAP reported no applicable method, despite process exit0. This failure was detected from the actual output; the inventory was corrected to query the simple A7 table, and the succeeding export and all assertions completed. Optional-package startup warnings do not constitute a successful mathematical check; the exact completed assertions and outputs do.

Before this finite endpoint, the root searched for general alternating genus estimates. Guralnick--Shareshian, Memoirs AMS189(886), DOI10.1090/memo/0886, was found only through abstracts and subsequent citations; the original full theorem was not read or used. An MSRI original-source URL timed out. A negative character-ratio project advertised as in preparation was not treated as a theorem. A possible permutation-genus-to-Specht deduction failed: large aggregate genus does not itself bound every irreducible multiplicity. None of these searches is counted as movement.

The successful finite proof treats exactly transitive A7-cover cores in the nonsplit source gate. It does not claim to exclude arbitrary nontransitive mixed representation labels. Original ATLAS data are cited mathematical inputs; the new claims are complete exact inequalities and their actual period-budget consequence.
''')
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## The transitive A7-cover supplier gate is closed\n\n'+now+' — Q2bh refuted and Q2i strictly reduced. D-A7-01--03 excludes all A7 double/triple/sixfold-cover cores in the transitive nonsplit setting, after whole author/peer proof and source audits and a separate independent polynomial-Fourier certificate. The standard scalar reflection exception is handled by actual splitness for one factor and the multiplier budget for several. No arbitrary nontransitive-product theorem is claimed. Integration is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('''\n## The residual A7 covers no longer supply the nonsplit gate\n\nD-A7-01--03 removes every transitive A7 quasisimple core, including its double, triple and sixfold covers, from the necessary rank-nine source gate. Complete exact spectra control all compatible normalizers; the standard exceptions require and receive a separate geometric and scalar-multiplier argument. The ordinary long-shape tensor cases for n>=15 remain open.\n\nThe restriction concerns actual finite covers and weight-one multiplicity variations; its integer identities lie in the representation ring and use the exact finite-etale/SGA and scheme-spreading framework already located in the paper. It narrows the condition-A cycle-supplier gate at cote16 scan050. It produces no new cycle, detector bound, condition-I positivity statement, Cayley-Hamilton projector, or motivic L-value estimate. The single standard-factor exclusion uses the actual polarization, not a formal invariant form.\n''')
p=R/'research/frameworks.tex';s=p.read_text();assert 'D-C3-01--03' in s
p.write_text(s.replace('D-C3-01--03','D-C3-01--03, D-A7-01--03'))
out={'date_utc':now,'integrated':['D-A7-01--03'],'whole_reviewed_math_sha256':reviewed,'canonical_sha256':canonical,
     'bib_sha256':hashlib.sha256((R/bib).read_bytes()).hexdigest(),'new_refuted_row':'Q2bh','main_gate':'Q2i'}
(R/'research/a7_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
