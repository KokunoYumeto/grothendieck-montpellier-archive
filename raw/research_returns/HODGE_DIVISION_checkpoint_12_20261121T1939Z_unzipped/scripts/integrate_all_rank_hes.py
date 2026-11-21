"""Integrate the completely reviewed elementary q=2 symplectic theorem."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
proof='agents/imprimitive/lie_small_fields/higher_even_symplectic_section.tex'
reviewed='72e295707440f2e06e39658d2b3528f61d9587227e99e6f18196b075515dbc3c'
canonical='2fb230d7598582db27e9aebd3ef540afbb81e308bef721ebc4254c620b8ca0d3'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==canonical
now=datetime.now(timezone.utc).isoformat()
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(x['id']!='Q2be' for x in rows)
(R/'research/gates_before_all_rank_hes.json').write_text(json.dumps({x['id']:x for x in rows if x['id']=='Q2i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text();anchor='\\input{agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex}'
assert anchor in s and proof not in s;s=s.replace(anchor,anchor+'\n\\input{'+proof+'}')
a='''and $\\operatorname{Sp}_{12}(2)$, with all normalizing scalars and factor
permutations. Other small-field higher-rank Lie representations remain
outside these exclusions.'''
b=r'''and $\operatorname{Sp}_{12}(2)$, with all normalizing scalars and factor
permutations. D-HES-01--03 then excludes every
$\operatorname{Sp}_{2n}(2)$ core with $n\ge4$, and arbitrary mixed products.
Its explicit elementary parabolic subgroup replaces the previously
unverified semisimple estimate. The only character-ratio premise is the
verified published unipotent bound; the essential finite endpoint inputs
are the ATLAS $\operatorname{Sp}_8(2)$ and $\operatorname{Sp}_{10}(2)$
tables. No missing Gluck--Magaard (1998) premise or separately computed
$\operatorname{Sp}_{12}(2)$ table is needed for this all-rank theorem.
Other small-field higher-rank Lie representations remain outside these
exclusions.'''
assert a in s;s=s.replace(a,b);p.write_text(s)
for x in rows:
 if x['id']=='Q2i':
  a='Other small-field higher-rank Lie cores remain.'
  b='D-HES-01--03 excludes all Sp(2n,2) cores n>=4 and arbitrary mixed products, using explicit elementary parabolic groups, verified unipotent3/4, all-eigenspace support1/8 and ESD ceiling24<35. The formerly missing GM1998 semisimple estimate and the computed Sp12 table are not premises. Other small-field higher-rank Lie cores remain.'
  assert a in x['finding_ids_or_current_gate'];x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace(a,b)
rows.append(dict(zip(fields,['Q2be','Prompt target2; full higher-rank symplectic family over F2','Can any Sp(2n,2) core n>=4, or mixed product, support the actual rank-nine source?','refuted','D-HES-01--03: fixed-point-free elementary2 subgroups in parabolics, elliptic Hermitian centralizers and all-element support1/8. Full normalizers and nontrivial form multiplier force e<=24<35. Whole root/peer checks and separate finite symbolic certificates PASS. GM1998 is not used.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-HES-01--03','targeted proof check','Whole canonical mathematical proof at72e295707440f2e06e39658d2b3528f61d9587227e99e6f18196b075515dbc3c read and independently checked by root; full G34 report read. PASS symmetric shears, characteristic-two elementary line radical, odd-order averaging, all dual weight orbits, Hermitian elliptic centralizer, all-rank strict3/4 induction, prime-order reduction, full tensor/normalizer and actual period budget. Final canonical changes are review status and redundant-input clarification only.',proof+'; agents/g34_eightfolds/bireflection/HIGHER_EVEN_SYMPLECTIC_UNCONDITIONAL_PEER_AUDIT.md'),
 ('D-HES elementary certificate','computation or formal certificate','Root read entire exact checker and actually reran it:10802shear-equivariance checks17472line products, nonzero order16 fixed-point-free subgroup with five dual3cycles, all rational averaging/induction/budget identities PASS0.380851seconds. This supplements the universal proof; it does not replace it or reprove the known character bound.','agents/imprimitive/lie_small_fields/check_higher_even_elementary.py; check_higher_even_elementary.json'),
 ('Liebeck2017 Theorem2.4(i)','used and rechecked in this run','Fresh root original-author published survey definitions on authorp2 and complete Theorem2.4(i)/(ii) statement pp3--4 read. Quasisimple simply connected scope applies. Noncentral unipotent ratio3/4 for q<=4 is the exact input; the different nonunipotent19/20 bound is not substituted. No fresh reading of Gluck1995 original proof claimed.','https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf'),
 ('Gow1981 theorem p583 Section3pp589--591','used and rechecked in this run','Fresh root original article theorem p583, inverse-conjugacy consequence, preceding lemmas and complete extracted Section3 proof text pp589--591 read. The known theorem applies to all characteristic-two symplectic groups. OCR loses some displayed matrix entries; no new entrywise reconstruction of those source matrices is claimed. Independent peer previously read complete invoked proof.','https://www.academia.edu/115642614/Products_of_two_involutions_in_classical_groups_of_characteristic_2'),
 ('D-HES-F editorial status','targeted proof check','After the full finite proof had passed root and peer review, root changed only review status and archived-source boundary paragraphs to acknowledge the actual third-table independent rerun. Mathematical proof and numerical inputs unchanged. Exact L34 identifiers were also corrected in integrated prose/registers.','agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## The all-rank q=2 symplectic gate is closed\n\n'+now+' — Q2be refuted and Q2i strictly reduced after whole root/peer proof checks. D-HES-01--03 now excludes every Sp(2n,2), n>=4, and mixed products. A new explicit elementary parabolic subgroup/weight-orbit proof removes the unverified GM1998 premise completely. Only previously checked ATLAS Sp8/Sp10 endpoints are essential. The older conditional draft is retained as a failed source-dependent approach, not a condition on the new theorem. This is integration, not an hourly review. General even q and non-tensor RM gluing remain active.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('''\n## Removal of a source gate in every higher symplectic rank over F2\n\nD-HES-01--03 closes the entire q=2 higher-rank core family, not just the three finite tables. The elementary parabolic module makes the verified unipotent character bound control every eigenspace of every odd-prime-order element. Elliptic elements are handled by their actual Hermitian centralizer. The resulting representation-ring support inequality, finite-cover variation factorization, and bilinear multiplier force degree at most24, below every allowed factor degree. No missing semisimple estimate remains.\n\nIn the project's geometry this further restricts finite covers capable of supplying a dense family of detecting cycles, hence narrows the existence gate for condition A (cote16 scan050, SIGN_NEXT SN-C03/C04). It supplies no new positivity-to-cycle inference, alters no Cayley-Hamilton projector, and claims no new L-value bound. Scheme-spreading and weight-one etale realizations have the exact framework locators already recorded; the integral/effective detector constants previously proved are unchanged.\n''')
p=R/'research/frameworks.tex';s=p.read_text().replace('D-HES-F, HD-SPIN','D-HES-F, D-HES-01--03, HD-SPIN');p.write_text(s)
out={'date_utc':now,'integrated':['D-HES-01--03'],'whole_reviewed_math_sha256':reviewed,'canonical_sha256':canonical,'source_gate_removed':'GM1998 not used','essential_finite_tables':['Sp8(2) ATLAS','Sp10(2) ATLAS']}
(R/'research/all_rank_hes_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
