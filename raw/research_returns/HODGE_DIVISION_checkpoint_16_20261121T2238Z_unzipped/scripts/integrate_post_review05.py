"""Integrate four complete findings after actual whole-proof reviews."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
proofs={
 'agents/g34_eightfolds/bireflection/linear_weil_section.tex':'fd19cb225ea0c284d89dddadfb07ca3f6622cf84eb373473138ca5780b37b053',
 'agents/imprimitive/lie_small_fields/g2_triality_section.tex':'3c099689c794302e80e0a12d2123e605045fda12935672568b706e52d7fb1067',
 'agents/sixfolds/rm_curvilinear_quantization_obstruction_section.tex':'8793f538a746d0e5f2fb77fd4eafb633dafeb50844bba49f0f5b9347779444bf',
 'research/ordinary_alternating_three_quarters.tex':'9903e06b3603613f6193488b0cd9774d20492848541a53686fbb60a158a6e5cc',
}
for p,h in proofs.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,(p,h)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not any(x['id'] in {'Q2aw','Q2ax','Q2ay','Q5q'} for x in rows)
now=datetime.now(timezone.utc).isoformat()
(R/'research/gates_before_post_review05_integration.json').write_text(json.dumps({x['id']:x for x in rows if x['id'] in {'Q2i','Q5i'}},indent=2)+'\n')
p=R/'research/ordinary_alternating_three_quarters.tex';s=p.read_text()
s=s.replace('New root derivation, with an author whole-proof reading, submitted\nfor independent review.', 'New root derivation, with an author whole-proof reading and an\nindependent whole-proof review by /root/g34\\_eightfolds, both PASS\non 21 November 2026. The independent arithmetic reconstruction passed.')
p.write_text(s)
main=R/'HODGE_DIVISION.tex';s=main.read_text()
insertions=[
 ('agents/g34_eightfolds/bireflection/twisted_lie_section.tex','agents/g34_eightfolds/bireflection/linear_weil_section.tex'),
 ('agents/imprimitive/lie_small_fields/sp4_3_core_section.tex','agents/imprimitive/lie_small_fields/g2_triality_section.tex'),
 ('research/ordinary_alternating_sharp_obstruction.tex','research/ordinary_alternating_three_quarters.tex'),
 ('agents/sixfolds/rm_local_quantization_obstruction_section.tex','agents/sixfolds/rm_curvilinear_quantization_obstruction_section.tex'),
 ('agents/g34_eightfolds/bireflection/twisted_lie_bibitems.tex','agents/g34_eightfolds/bireflection/linear_weil_bibitems.tex'),
 ('agents/imprimitive/lie_small_fields/symplectic_weil_bibitems.tex','agents/imprimitive/lie_small_fields/g2_triality_bibitems.tex'),
]
for anchor,path in insertions:
 a='\\input{'+anchor+'}';assert a in s and path not in s
 s=s.replace(a,a+'\n\\input{'+path+'}')
old='D-BI-22 excludes all Suzuki,\nRee and Tits cores.'
new='D-BI-22 excludes all Suzuki,\nRee and Tits cores. D-BI-23 excludes every transitive linear-Weil\ncore of $\\operatorname{SL}_n(q)$ for $n\\ge3$, in all field sizes.\nD-G2T-01--03 excludes all $G_2(q)$ with $q\\ge3$ and all\n${}^3D_4(q)$ with $q\\ge2$, including mixed factors and all compatible\nouter automorphisms.'
assert old in s;s=s.replace(old,new)
old='Thus a remaining large ordinary\nalternating core has a longer first row or column; its factor\nrepresentation extends to a real Specht representation and its full\ninducing image is essentially self-dual.'
new='Its remaining large ordinary\nfactors extend to real Specht representations and their full inducing\nimage is essentially self-dual. HD-ALT-04 further forces every\ntransitive ordinary factor label to have a row or column longer than\n$3n/4$: the complete normalizer bound gives $e\\le64$, whereas\neach factor has degree at least $125$.'
assert old in s;s=s.replace(old,new)
old='with a nonreduced module at every nontrivial point remain in that local\nclass.'
new='with a nonreduced module at every nontrivial point remain in that local\nclass. SF-E820 further excludes every nontrivial point at which both\nmodules are free over the same curvilinear Artinian quotient, of any\nlength. It constructs actual rank-thirty-two balanced nonreduced\nexamples of equal signed local length and excludes them by two\nfirst-order local quantization obstructions.'
assert old in s;s=s.replace(old,new)
main.write_text(s)
for x in rows:
 if x['id']=='Q2i':
  s=x['finding_ids_or_current_gate']
  a='All sporadic, allA1, allSuzuki/Ree/Tits cores are excluded (D-SPOR,D-BI21/22).'
  b='All sporadic, all A1, all Suzuki/Ree/Tits, all transitive linear-Weil SL_n(q) (n>=3), and all G2(q>=3)/3D4(q>=2) cores are excluded (D-SPOR,D-BI21/22/23,D-G2T01--03); the last result permits mixed factors.'
  assert a in s;s=s.replace(a,b)
  a='HD-ALT03 forces any remaining ordinaryAn,n>=15,to have a row/column>ceil(n/2); its factors extend to real Specht modules and the inducing image is ESD.'
  b='HD-ALT03 forces all remaining ordinary An,n>=15 factors to extend to real Specht modules, so the inducing image is ESD. HD-ALT04 further forces every transitive factor label to have a row/column>3n/4; its excluded range gives e<=64 against factor degree>=125.'
  assert a in s;s=s.replace(a,b);x['finding_ids_or_current_gate']=s
 if x['id']=='Q5i':
  s=x['finding_ids_or_current_gate']
  a='The actual rank36 nonpure balanced construction fails this test.'
  b='The actual rank36 nonpure balanced construction fails this test. SF-E820 excludes all nontrivial modifications with both modules free over a common curvilinear Artinian quotient, of any length; actual rank32 equal-length nonreduced balanced extensions are constructed and excluded.'
  assert a in s;s=s.replace(a,b)
  s=s.replace('nonreduced equal-length point modifications,','nonreduced equal-length point modifications outside the common-curvilinear-free case,')
  x['finding_ids_or_current_gate']=s
newrows=[
 ['Q2aw','Prompt target2; linear Weil normal cores','Can a transitive linear-Weil SL_n(q) core support actual period rank nine?','refuted','D-BI-23a/b/23: all n>=3 and all field sizes excluded, with all scalars, compatible outers and transitive tensor permutations. Published GL function model plus new SL restriction and character bounds; complete endpoint24 rows/1288 spectra. No non-Weil or unitary assertion.'],
 ['Q2ax','Prompt target2; G2 and triality normal cores','Can G2(q>=3) or 3D4(q>=2) normal cores support actual period rank nine?','refuted','D-G2T-01--03: all fields, mixed central-product factors and all compatible outers excluded. Generic all-q bound from318 row types/9242 rational polynomial comparisons, plus239 rows/11502 exact small-cover spectra. Published complete table input explicit.'],
 ['Q2ay','Prompt target2; long ordinary alternating shapes','Can a transitive ordinary An core have all row/column lengths at most3n/4?','refuted','HD-ALT-04a/b for n>=15: Cauchy-refined content bound gives all-normalizer nu>=7a/64; real-factor multiplier argument forces e<=64 against factor degree>=125. Larger inducing fields allowed if their character field contains original imaginary K.'],
 ['Q5q','Prompt target5; nonreduced balanced point modifications','Can equal-length free modules over a common curvilinear quotient repair weak semiregularity?','refuted','SF-E820: both local balanced bivector deformations force proportional bracket forms, contradicting the nonzero Jacobian socle wedge. All lengths and ranks covered. Actual rank32 equal-module balanced sheaves have Ext dimension6m²ell and are excluded; arbitrary Artinian modules remain.'],
]
rows.extend(dict(zip(fields,row)) for row in newrows)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-BI-23a/b/23','targeted proof check','Read whole proof, entire endpoint checker, revised source paragraph and independent peer report. PASS SL orbit irreducibility, scalar projector estimates, actual triple-cover/all-cyclic-outer coverage, all-field inequalities, real-case multiplier, tensor and actual intermediate-cover arguments. Final reviewedSHAfd19cb225ea0c284d89dddadfb07ca3f6622cf84eb373473138ca5780b37b053.','research/root_review_linear_g2_curvilinear.md; agents/imprimitive/audit_linear_weil/PEER_AUDIT.md'),
 ('D-BI-23 endpoint spectra','computation or formal certificate','Earlier fresh root execution passed24 selected rows/1288 complete spectra/minimum nu8 and all five fusions. This reruns reviewed exact code; independent sibling reconstruction is a separate event.','agents/g34_eightfolds/bireflection/linear_weil/check_linear_weil.py; check_linear_weil.json'),
 ('Gerardin1977 Prop4.2;BreuerCTblLibXpls2.6-4/2.7-4/11.5-7','used and rechecked in this run','Freshly read original published Prop4.2 and whole proof pp82--83. Read ATLAS warning and independently verified structural inputs via Breuer exact multiplier construction with printedATLASp23 attribution, full outer group/three involution types, and diagonal/field/graph descriptions. HHM exceptional list is not mislabelled as a full multiplier-structure table.','https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields; https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc2/chap2.html; chap11_mj.html'),
 ('D-G2T-01--03','targeted proof check','Read whole canonical proof/bibliography/source log, GAP exporter, source extractor, formal-phase parser, Fraction checker and small-cover checker. PASS complete all-field coverage, phase/shift bound, all normalizers, mixed tensor argument and e<=24 contradiction. Peer independent whole audit also read. FinalSHA3c099689c794302e80e0a12d2123e605045fda12935672568b706e52d7fb1067.','research/root_review_linear_g2_curvilinear.md; agents/g34_eightfolds/bireflection/G2_TRIALITY_PEER_AUDIT.md'),
 ('D-G2T exact certificates','computation or formal certificate','Actually reran frozen source extraction, all318 row types/9242 inequalities and all239 small rows/11502 full spectra; PASS. Runtime-in-certificate hash defect identified and repaired without changing mathematics; deterministic coefficient hash568425a2cf62e62dbe24709a3372d9bd182946e0a53ae74e7fed45ba640dcd13. Root read the exact repair; author two regeneration checks recorded separately.','agents/imprimitive/lie_small_fields/build_generic_input.py; parse_generic_bounds.py; check_generic_polynomials.py; check_g2_triality_small.py'),
 ('GenericCharacterTables complete inventory/cyclotomic definition','used and rechecked in this run','Fresh root full inventory read for all11 invoked table types and full mathematical generic-cyclotomic definition. All admissible phases have modulus1, and the listed full ordinary tables exhaust the claimed congruence/characteristic cases. Original inaccessible Chang-Ree/Deriziotis-Michler full proofs not claimed read; official complete mathematical tables remain explicit premises.','https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/; https://oscar-system.github.io/GenericCharacterTables.jl/stable/cyclo/'),
 ('SF-E820','targeted proof check','Read complete frozen Markdown, entire author certificate and all296 lines of canonical TeX; independent complete G34 report also read. PASS quotient-valued R-linearity, lifted nonlinear bracket equations, unit/invertibility, proportionality and nonzero socle wedge, exact rank32 construction and all scope limits. CanonicalSHA8793f538a746d0e5f2fb77fd4eafb633dafeb50844bba49f0f5b9347779444bf.','research/root_review_linear_g2_curvilinear.md; agents/sixfolds/rm_curvilinear_quantization_obstruction_section.tex'),
 ('SF-E820 exact arithmetic','computation or formal certificate','Actually read and executed author certificate: PASS generic16-variable Jacobian mixed-wedge identity, Artin socle endpoints and full rank32 balanced character/self-Euler1024. This is not a computational proof of module lifting; that received whole-proof review.','agents/sixfolds/rm_curvilinear_quantization_certificate.py; rm_curvilinear_quantization_certificate_output.json'),
 ('HD-ALT-04a/b','targeted proof check','Whole author proof reread; independent whole G34 report read. PASS Cauchy improvement, transitivity/split-factor reduction, nontrivial multiplier over larger character field and exact e<=64 contradiction. Only review header changed after independent mathematical hash9903e06b3603613f6193488b0cd9774d20492848541a53686fbb60a158a6e5cc.','research/ordinary_alternating_three_quarters.tex; agents/g34_eightfolds/bireflection/ORDINARY_ALTERNATING_THREE_QUARTERS_PEER_AUDIT.md'),
 ('HD-ALT-04 arithmetic','computation or formal certificate','Actually wrote and executed exact content/hook/ratio checker on98625 partitions n15--36,97213 eligible and14252 newly beyond half-size region. PASS formulas, polynomial positivity and degree budget; (11,4) is a concrete strict-gate witness of degree910. All-n conclusion uses written proof, not finite extrapolation.','research/alternating_three_quarters_certificate.py; alternating_three_quarters_certificate.json'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Post-review05: four independently checked gate reductions\n\n'+now+' — Q2aw/Q2ax/Q2ay/Q5q refuted. Linear-Weil cores are excluded in every field size; all G2 and triality cores are excluded, including mixed factors. The large ordinary alternating gate now requires row/column>3n/4. Balanced sheaves with a locally free hull cannot have a nontrivial common-curvilinear-free point kernel/cokernel, even with equal local lengths; actual rank32 extensions are constructed and excluded. Whole proofs, source boundaries and exact arithmetic have root and independent sibling checks. These properly reduce Q2i/Q5i. The deterministic certificate repair is documentation quality only and is not separately counted as movement. No formal hourly review is being performed in this entry.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('\n## Further all-field monodromy and curvilinear restrictions\n\nD-BI23 and D-G2T01--03 remove entire additional finite-monodromy supplier families from the remaining nonsplit-sixfold question. HD-ALT04 forces an ordinary alternating Young shape beyond three quarters of its degree. Their proofs are finite-representation and actual variation-factorization obstructions; no dimension count is promoted to dominance. SF-E820 is a local coherent K-theory/first-order Hochschild obstruction for any common curvilinear Artinian quotient; it supplies actual failed balanced objects and a strict refinement of the nonpure seed gate. In the Grothendieck programme these all narrow condition A supplier existence, cote16 scan050. They do not create cycles from condition I, scan049/cote44Theorem4, or alter the resultant/Cayley--Hamilton projector of scans048--049. The usual finite-local-system and cycle/spreading interpretation applies; no new weight, motivic L-value or unconditional general Hodge-conjecture assertion is inferred.\n')
out={'integrated':['D-BI23','D-G2T01--03','SF-E820','HD-ALT04'],'date_utc':now,
     'reviewed_proof_hashes':proofs,'alt04_final_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(R/'research/post_review05_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
