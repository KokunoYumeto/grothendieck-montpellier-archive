"""Integrate the whole-reviewed all-even-field higher symplectic theorem."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R = Path(__file__).resolve().parents[1]
proof = 'agents/imprimitive/lie_small_fields/higher_even_symplectic_all_fields_section.tex'
reviewed = 'ab4898d2725c48b0993539ead8e56c27b9630f0433aee185514c48ab1546ae18'
canonical = '542df27baf0e3810906e03585b967d1cebaf083302b2df85ffc13232a616e837'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest() == canonical
now = datetime.now(timezone.utc).isoformat()
q = R/'QUESTIONS.tsv'
rows = list(csv.DictReader(q.open(), delimiter='\t'))
fields = list(rows[0])
assert all(x['id'] != 'Q2bf' for x in rows)
(R/'research/gates_before_all_even_hes.json').write_text(json.dumps({x['id']: x for x in rows if x['id'] == 'Q2i'}, indent=2)+'\n')

p = R/'HODGE_DIVISION.tex'
s = p.read_text()
anchor = r'\input{agents/imprimitive/lie_small_fields/higher_even_symplectic_section.tex}'
assert anchor in s and proof not in s
s = s.replace(anchor, anchor+'\n'+r'\input{'+proof+'}')
a = 'Other small-field higher-rank Lie representations remain outside these\nexclusions.'
b = r'''D-HES-04--06 then excludes every higher symplectic core
$\operatorname{Sp}_{2n}(q)$ with $n\ge4$ and $q$ even, allowing mixed
ranks and fields, all compatible outer operators, scalars and factor
permutations. Its uniform normalizer support $7e/64$, together with the
nontrivial bilinear multiplier, forces $e\le64$; the actual factor
degrees exclude every case. The $q=4$ field-involution endpoint is
proved by explicit symplectic descent and dual-weight pairs. Other
small-field higher-rank Lie representations remain outside these
exclusions.'''
assert a in s
s = s.replace(a, b)
p.write_text(s)

for x in rows:
    if x['id'] == 'Q2i':
        a = 'Other small-field higher-rank Lie cores remain.'
        b = ('D-HES-04--06 excludes all Sp(2n,q) cores n>=4 over every even field, '
             'including mixed ranks/fields and all compatible outer/scalar/permutation operators. '
             'The q4 field-involution descent and common support7/64 force degree<=64, '
             'below every remaining single-factor minimum and below35^2 for mixed products. '
             'Other small-field higher-rank Lie cores remain.')
        assert a in x['finding_ids_or_current_gate']
        x['finding_ids_or_current_gate'] = x['finding_ids_or_current_gate'].replace(a,b)
rows.append(dict(zip(fields, [
    'Q2bf', 'Prompt target2; higher symplectic cores over all even fields',
    'Can any mixed product of Sp(2n,q), n>=4 and q even, support the actual rank-nine source?',
    'refuted',
    'D-HES-04--06: all ordinary representations and all compatible normalizers have common support7/64; explicit F4/F2 symplectic descent handles the field-involution endpoint. The multiplier budget gives e<=64; factors have degrees>=35, >=378 atq4, >=511 atq>=8, and the sharperq2 exclusion applies. Root and independent-peer whole-proof checks PASS. The corrected published unipotent bound is1/(sqrt(q)-1).'
])))
with q.open('w', newline='') as f:
    w = csv.DictWriter(f, fields, delimiter='\t')
    w.writeheader()
    w.writerows(rows)

events = [
    ('D-HES-04--06', 'targeted proof check',
     'Root read and checked the complete mathematical proof at'+reviewed+' and read the whole independent G34 audit. Final canonical reread confirms only review status changed. PASS all-even elementary subgroups, elliptic Hermitian trace estimate, commutator normalizer bound, exact F4 symplectic descent, dual-weight involution support, mixed tensor permutation support, form multiplier and actual intermediate-cover period budget. No missing GM1998 estimate is used.',
     proof+'; agents/g34_eightfolds/bireflection/HIGHER_EVEN_SYMPLECTIC_ALL_FIELDS_PEER_AUDIT.md'),
    ('D-HES all-even exact certificate', 'computation or formal certificate',
     'Root read the complete author checker and actually reran it: PASS0.441622seconds, 28 semilinear twists, 6336 descent-vector identities and69904 dual-trace pairings, plus the65 frozen Sp6(4) degree polynomials with minimum378. Dimensions2/4 exhaust vectors; dimension8 uses fixed vectors and512 deterministic samples for each of4 twists. Independent peer separately checked60 Sp2(F4) matrices,10 cocycles,160 descent identities and4096 dual-weight pairings in0.019795seconds. Finite checks supplement the universal written proof.',
     'agents/imprimitive/lie_small_fields/check_higher_even_all_fields.py; agents/imprimitive/lie_small_fields/check_higher_even_all_fields.json; agents/g34_eightfolds/bireflection/audit_higher_even_all_fields.json'),
    ('Liebeck2017 Theorem2.4(i), radical correction', 'used and rechecked in this run',
     'Root freshly inspected the rendered original-author numberedp4 after reading definitionsp2 and the full theorem statementpp3--4. The bound is1/(sqrt(q)-1), not1/sqrt(q-1). The original q8<1/2 proposal was rejected before canonical freeze; the valid comparison1/(sqrt(8)-1)<9/16 follows from625<648. The q2 andq4 uses of3/4 are unaffected. No fresh reading of Gluck1995 original proof is claimed.',
     'https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf; agents/imprimitive/lie_small_fields/cache/Liebeck2017_p4.png'),
    ('Li-Xia2022 Section2.2.2 Table2.1', 'used and rechecked in this run',
     'Root read the entire relevant paragraph and Table2.1 on author numberedp14 from the actual author-v3 PDF, SHA4ef16aa4308f8c487a06e9c8e84ece77247d0e763146f0215d8e109e443e3a93. For PSp(2n,q) outside(n,p)=(2,2), the stated outer group is C_(2,q-1) times C_f, giving C2 atq4,n>=4. AMS publication metadata independently verified. Web arXiv access failed; the successful original read was local. Classification is cited, not newly proved.',
     'agents/imprimitive/lie_small_fields/cache/LiXia2022_author_v3.pdf; https://doi.org/10.1090/memo/1375'),
    ('D-HES-06 previously checked source inputs', 'carried as background without fault found',
     'Gow1981 reality, the complete Schur multiplier classification, the verified Sp8/Sp10 ATLAS endpoints and complete D-ESC Sp6(4) minimum-degree input remain as previously checked with exact locators. This integration is not a new rereading of those whole source proofs. The separately computed Sp12 table is redundant.',
     proof+'; agents/imprimitive/lie_small_fields/higher_even_symplectic_bibitems.tex')
]
with (R/'research/root_check_events.tsv').open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for sid, typ, out, ev in events:
        w.writerow([sid, now, '/root', 'GPT-6 Astra Pro', 'inherited; not externally exposed', 'HODGE_DIVISION', typ, out, ev])
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## Every higher symplectic core in even characteristic\n\n'+now+' — Q2bf refuted and Q2i strictly reduced after complete root/peer proof reviews. D-HES-04--06 excludes every higher symplectic core over every even field, including arbitrary mixed ranks/fields and compatible normalizers. The q4 field involution is handled explicitly; the common support bound7/64 and nontrivial bilinear multiplier force e<=64, excluding all factors. The source radical correction is preserved in the audit trail. This is integration, not an hourly review. Odd symplectic and the remaining higher Lie cores remain active.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('''\n## All even-field higher symplectic sources are excluded\n\nD-HES-04--06 removes an entire remaining infinite family of finite-cover suppliers for the nonsplit sixfold problem. The result covers mixed fields and ranks and the actual full compatible normalizer, rather than only core elements or a designated representation. Its proof combines explicit symplectic geometry over finite fields, representation-ring weight multiplicities, and the Euler/period budget of the actual intermediate cover. It does not supply a detecting cycle or a new detector bound in the unresolved components.\n\nThis is a stricter existence gate for condition A, cote16 scan050 (SIGN_NEXT SN-C03/C04). The scheme-spreading, finite-cover and weight-one etale interpretation is exactly that recorded in the framework section, with its SGA/EGA locators. The positivity/division step remains condition I, cote16 scan049 and cote44 scan002/footer1 Theorem4; the projector remains the Cayley-Hamilton inverse of cote16 scans048--049. The representation support calculation does not assert a new motivic or L-function estimate and changes no established integral detector constant.\n''')
p = R/'research/frameworks.tex'
s = p.read_text()
assert 'D-HES-01--03' in s
p.write_text(s.replace('D-HES-01--03', 'D-HES-01--06'))
out = {'date_utc': now, 'integrated': ['D-HES-04--06'], 'whole_reviewed_math_sha256': reviewed,
       'canonical_sha256': canonical, 'main_gate': 'Q2i', 'new_refuted_row': 'Q2bf',
       'uniform_normalizer_support': '7/64', 'degree_ceiling': 64,
       'published_bound': '1/(sqrt(q)-1), q>=8; 3/4 atq4'}
(R/'research/all_even_hes_integration.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out))
