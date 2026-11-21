"""One-time integration after full author, root, and independent peer reviews."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json

R=Path(__file__).resolve().parents[1]
proofs={
 'agents/g34_eightfolds/bireflection/unitary_weil_section.tex':'d7895c494434ccde3126d2484153f050290e8dfbc2959450fdf6d25cd6e0d36b',
 'agents/imprimitive/lie_small_fields/even_symplectic_section.tex':'3b1c3e960db80f461f64e3316462119c03b16a9311b8108a0f908547d403ab3f',
 'agents/sixfolds/rm_surface_cone_obstruction_section.tex':'97c65ebc38d008ea5da2f1087334be33d544d731326743eb89052098d5692be7',
 'agents/sixfolds/rm_surface_cone_torsionfree_addendum_section.tex':'d2700411b009bb63bc74065103b9fec157553f0419f9a088e84c2a3ef08e17aa',
 'agents/sixfolds/rm_coupled_surface_obstruction_section.tex':'e5319863ae1c91330293d5ca051b30cb95d385d78343cc4c33087c08c376d7a5',
}
for name,h in proofs.items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==h,name
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not any(x['id'] in {'Q2ba','Q2bb','Q5r','Q5s'} for x in rows)
now=datetime.now(timezone.utc).isoformat()
(R/'research/gates_before_unitary_even_surface.json').write_text(json.dumps({x['id']:x for x in rows if x['id'] in {'Q2i','Q5i'}},indent=2)+'\n')
main=R/'HODGE_DIVISION.tex';s=main.read_text()
insertions=[
 ('agents/g34_eightfolds/bireflection/linear_weil_section.tex',['agents/g34_eightfolds/bireflection/unitary_weil_section.tex']),
 ('agents/imprimitive/lie_small_fields/g2_triality_section.tex',['agents/imprimitive/lie_small_fields/even_symplectic_section.tex']),
 ('agents/sixfolds/rm_curvilinear_quantization_obstruction_section.tex',[
  'agents/sixfolds/rm_surface_cone_obstruction_section.tex',
  'agents/sixfolds/rm_surface_cone_torsionfree_addendum_section.tex',
  'agents/sixfolds/rm_coupled_surface_obstruction_section.tex']),
 ('agents/g34_eightfolds/bireflection/linear_weil_bibitems.tex',['agents/g34_eightfolds/bireflection/unitary_weil_bibitems.tex']),
 ('agents/imprimitive/lie_small_fields/g2_triality_bibitems.tex',['agents/imprimitive/lie_small_fields/even_symplectic_bibitems.tex']),
 ('agents/sixfolds/rm_local_quantization_bibitems.tex',[
  'agents/sixfolds/rm_surface_cone_bibitems.tex','agents/sixfolds/rm_coupled_surface_bibitems.tex']),
]
for anchor,paths in insertions:
 a='\\input{'+anchor+'}';assert a in s
 assert all(path not in s and (R/path).exists() for path in paths)
 s=s.replace(a,a+''.join('\n\\input{'+path+'}' for path in paths))
a='representations in the nonsplit non-Eisenstein problem. Other small-field\nhigher-rank Lie representations remain outside these exclusions.'
b='''representations in the nonsplit non-Eisenstein problem.
D-BI-24 reduces all transitive ordinary unitary-Weil cores, in all
field sizes, to the single $\\operatorname{PSU}_4(2)$ degrees five
and six; only five remains in that nonsplit scope.
D-ESC-01--03 excludes all even-characteristic $\\operatorname{Sp}_4(q)$
and $\\operatorname{Sp}_6(q)$ cores in the main nonsplit problem.
For $q\\ge4$ its theorem also permits mixed ranks and field sizes;
the separate transitive $\\operatorname{Sp}_6(2)$ endpoint uses the
precise non-Eisenstein degree-seven exclusion. Other small-field
higher-rank Lie representations remain outside these exclusions.'''
assert a in s;s=s.replace(a,b)
a='''positive-dimensional torsion or defects outside SF-E818, and overlapping
class sets in at least three cohomology degrees.'''
b='''positive-dimensional torsion or defects outside the following surface
restrictions, and overlapping class sets in at least three cohomology
degrees. SF-E821/E821a proves that a genuine local surface summand in
a balanced complex has mixed RM tangent type and zero pairing with
each squared eigenpolarization. This excludes the entire rank-sixteen
ample-surface cone family, even with an arbitrary torsion-free
quotient. SF-E822 also excludes genuinely coupled coherent surface
modifications when the smooth integral support has class
$k^2\\theta^2$ and its torsion and defect bundles have equal rank and
equal polarization degree. In particular it excludes all such repairs
preserving the entire hull character, including actual rank-thirty-two
nonsplit examples. Unequal degrees, other support classes, nonreduced
or singular surface modules, and more general derived couplings remain
open.'''
assert a in s;s=s.replace(a,b);main.write_text(s)
for x in rows:
 if x['id']=='Q2i':
  a='Other small-field higher-rank Lie cores remain.'
  b='D-BI24 reduces all transitive ordinary unitary-Weil cores to single PSU4(2) degree5/6, with only5 in the stated nonsplit scope. D-ESC01--03 excludes all even-characteristic Sp4/Sp6 cores in the main problem, allowing mixed ranks/fields for q>=4 and using BI17 only for the transitive Sp6(2) degree7 endpoint. Other small-field higher-rank Lie cores remain.'
  assert a in x['finding_ids_or_current_gate'];x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace(a,b)
 if x['id']=='Q5i':
  a='Remaining: unstable bundles,'
  b='SF-E821/E821a excludes every actual local surface summand with a positive squared-eigenpolarization pairing, including the constructed rank16 balanced cones and any torsion-free quotient. SF-E822 excludes equal-rank/equal-degree vector-bundle torsion/defect repairs on smooth integral surfaces of class k²theta², including genuinely coupled rank32 examples and every same-entire-character repair of a balanced hull. Remaining: unstable bundles,'
  assert a in x['finding_ids_or_current_gate'];x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace(a,b)
  x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace('positive-dimensional torsion/defects outsideE818,','positive-dimensional torsion/defects outsideE818/E821/E822 (including unequal-degree, other support classes, nonreduced/singular support or broader derived couplings),')
newrows=[
 ['Q2ba','Prompt target2; ordinary unitary-Weil normal cores','Can a transitive ordinary unitary-Weil core outside the known PSU4(2) endpoint support actual rank nine?','refuted','D-BI24a/b/24: all q and n>=3, except nonsimple PSU3(2), reduce to a single PSU4(2) degree5/6. Non-Eisenstein nonsplit scope retains only5 by D-SPW04. New finite endpoint17rows754spectra; no non-Weil assertion.'],
 ['Q2bb','Prompt target2; complete even-characteristic Sp4/Sp6 cores','Can an even-characteristic rank2 or rank3 symplectic core supply the remaining nonsplit family?','refuted','D-ESC01--03: generic83 nontrivial row types/4549 exact inequalities and104 small rows/3442 spectra exclude all stated cores. q>=4 allows mixed ranks/fields; q2Sp6 is transitive and its final degree7 exclusion has exactly BI17 scope.'],
 ['Q5r','Prompt target5; actual balanced surface cones','Can a local ample-surface summand yield a balanced weakly semiregular complex, including singular torsion-free quotient cones?','refuted','SF-E821/E821a: two local first-order coisotropy equations force mixed RM tangent type and both squared-eigenpolarization integrals0. Actual rank16 gluable balanced cones with support class k²theta² are constructed and excluded. Torsion-free quotients split generically in codimension2.'],
 ['Q5s','Prompt target5; genuinely coupled same-character surface repairs','Can equal-rank/equal-degree surface torsion and defect repair a balanced locally free hull on an ample surface?','refuted','SF-E822: intrinsic local equation E A_pi=P_pi Id, uniqueness/gluing, and degree-zero determinant imply normal bivectors proportional, contradicting their independent positive norm on class k²theta². Covers unequal isomorphism classes of bundles with equal rank/degree and all same-character repairs. Actual coupled rank32 sheaves are constructed and excluded. Unequal degrees remain open.'],
]
rows.extend(dict(zip(fields,row)) for row in newrows)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-BI24a/b/24','targeted proof check','Read the complete proof, complete GAP exporter and Python checker, entire independent peer report, and final source-domain additions. PASS all-q orbit irreducibility, character/stabilizer estimates, exceptional-lift comparison on perfect SU, three complete endpoints, total tensor/multiplier budget and precise remaining5/6 scope.','agents/g34_eightfolds/bireflection/unitary_weil_section.tex; agents/imprimitive/audit_unitary_weil/PEER_AUDIT.md'),
 ('D-BI24 finite endpoint','computation or formal certificate','Actually reran reviewed exact checker:17 selected rows754 spectra4 normal fusions PASS, input0c84735f987b0bea3a9fea197002d4cb28af2cdae9a165bad8bce3bf6f91a117; runtime0.059644seconds. Independent peer reconstruction is separately logged.','agents/g34_eightfolds/bireflection/check_unitary_weil.py; check_unitary_weil.json'),
 ('Gerardin1977 Th4.9.2;GLOST4.3;Yang2023 Lem6','used and rechecked in this run','Fresh root read of full Gerardin Th4.9.2 proof(a)--(e), pp99--100; §3.1 and Th3.3(a triple-prime) statement verify even-q domain. Fresh full GLOST§4.3 projector subsection and Yang§2.2 Lem6 with following field/graph convention read. No fresh whole-proof claim for Gerardin Th3.3 construction or GLS classification.','https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields; https://www.ma.imperial.ac.uk/~mwl/burnside.pdf; https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=9698&wshow=paper'),
 ('D-ESC01--03','targeted proof check','Whole theorem and all code read, including exact source extractor/checkers and GAP exporter; full independent G34 report read. PASS corrected complete table scope, all-normalizer/mixed-core argument and exact restricted Sp6(2) endpoint. Only review header changed after reviewed2fd6be44c6023f9debf6803401cb5db1532051c65e03b62d74b9e6b0b02645b9.','agents/imprimitive/lie_small_fields/even_symplectic_section.tex; agents/g34_eightfolds/bireflection/EVEN_SYMPLECTIC_PEER_AUDIT.md'),
 ('D-ESC exact arithmetic','computation or formal certificate','Earlier actual root reruns in this review interval passed83 nontrivial types4549 all-q inequalities and104 rows3442 complete spectra. The independent peer checks original expressions and Fourier spectra separately.','agents/imprimitive/lie_small_fields/check_even_symplectic_generic.py; check_even_symplectic_small.py'),
 ('Enomoto1972;Luebeck1993;corrected GCT Sp4.0/Sp6.0','used and rechecked in this run','Fresh original Enomoto complete-table purpose p75, §4 startp80 and completenessp85 read; official correction notice is essential. Fresh original Luebeck Introductionpp3--4, complete §2.2pp18--21 and §9pp78--79 read locally. Dissertation is not called refereed; whole ordinary Sp6.0 is distinguished from unipotent-only uniSp6.0.','https://ir.library.osaka-u.ac.jp/repo/ouka/all/8596/ojm09_01_07.pdf; https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/CharTabCSp6.pdf; https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/'),
 ('SF-E821/E821a','targeted proof check','Read entire frozen drafts, all461 canonical TeX lines, complete author certificate and independent peer report. PASS local characteristic naturality/coisotropy, mixed tangent criterion, torsion-free generic projective-dimension splitting, explicit reduced surface construction, section vanishing, full character and negative Ext.','agents/sixfolds/rm_surface_cone_obstruction_section.tex; rm_surface_cone_torsionfree_addendum_section.tex; agents/imprimitive/audit_surface_cone/PEER_AUDIT.md'),
 ('SF-E821 arithmetic','computation or formal certificate','Actually executed author certificate in this review interval; PASS entire rank16 character/Koszul identity/self-Euler256k^4 and12 restriction matrices. Peer independently reconstructed eight-generator exterior identity and16 face types.','agents/sixfolds/rm_surface_cone_certificate.py; rm_surface_cone_certificate_output.json'),
 ('Stacks regular local resolution00O7/00NT/00NG','used and rechecked in this run','Fresh root whole statements/proofs of Proposition10.110.1 and its two stated dependencies read for E821a. Finite-module resolution suffices; no infinite-module global-dimension claim.','https://stacks.math.columbia.edu/tag/00O7; https://stacks.math.columbia.edu/tag/00NT; https://stacks.math.columbia.edu/tag/00NG'),
 ('SF-E822','targeted proof check','Read whole frozen draftbf9dec6e831599b53db853306b2d0c44867175ed36620c75fd7bed25c0c1b95c, all357 canonical lines, complete author certificate and full independent report. PASS actual resolution at detE zeros, right-module sign, intrinsic equation, uniqueness/gluing, degree-zero determinant, adjunction norm, GRR and actual nonsplit extension.','agents/sixfolds/rm_coupled_surface_obstruction_section.tex; agents/g34_eightfolds/bireflection/COUPLED_SURFACE_PEER_AUDIT.md'),
 ('SF-E822 symbolic identities','computation or formal certificate','Actually executed full author certificate: ranks1/2/3, arbitrary symbolic f/g/E and all6 bivector coefficients, exact star-square bottom-P Id, no E derivatives, reduced homotopy-E A and exterior norm Gram2I PASS. All-rank/globalization conclusions are separately reviewed proofs.','agents/sixfolds/rm_coupled_surface_certificate.py; rm_coupled_surface_certificate_output.json'),
 ('Stacks Bertini33.47.3/37.32.4','used and rechecked in this run','Fresh root read complete smoothness lemma proof and smooth irreducible hyperplane remark, applied twice to the previously verified3theta embedding. No new audit of all referenced earlier Bertini dependencies claimed.','https://stacks.math.columbia.edu/tag/0FD4; https://stacks.math.columbia.edu/tag/0G4G'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Unitary, even symplectic and surface reductions integrated\n\n'+now+' — Q2ba/Q2bb/Q5r/Q5s refuted after whole root and independent peer checks. The current Q2i gate removes the full ordinary unitary-Weil series except its existing rank5 endpoint, and all even Sp4/Sp6 in the exact main scope. Q5i now excludes ample local surface summands (even with torsion-free quotient) and genuinely coupled equal-rank/equal-degree vector-bundle surface repairs. Actual failed rank16 and rank32 objects establish that these are concrete proper restrictions. Unequal-slope compensation, high-rank Sp(2n,2), and full A2/2A2 calculations are still work in progress and are not asserted settled here. This is an integration entry, not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('''\n## Further complete core families and actual surface obstructions\n\nD-BI24 and D-ESC01--03 narrow the finite-monodromy supplier gate Q2i: all ordinary unitary-Weil cores reduce to the existing small rank5 profile in the precise nonsplit scope, while complete even symplectic rank2/rank3 cores are excluded. These are statements about actual covers, integral representation rings and their weight-one variation, with finite scalar and compatible outer actions retained. They do not assert a period rank from a branch-count inequality.\n\nSF-E821/E821a/E822 are geometric obstructions for actual perfect complexes and coherent sheaves on the RM fourfold. The first forces genuine local surface summands to have mixed RM tangent type. The second handles a genuinely nonsplit surface torsion/defect extension and uses its intrinsic Koszul class, not an assumed deformation of the hull map. Equal polarization degree is essential. The actual excluded rank16 cones and rank32 coupled sheaves have full balanced characters, but supply no successful seed for DEG_L S-14. Published BF2008 supplies trace/evaluation; supplied DEG_L S-21.6--8 supplies the exact coherent finite-action compatibility.\n\nFor Grothendieck's programme these restrict supplier existence for condition A, cote16 scan050, with SIGN_NEXT SN-C03/C04 unchanged. Their positive pairings are uses of condition I, cote16 scan049 and cote44 scan002/footer1 Theorem4; positivity does not create cycles. They do not alter the resultant/Cayley--Hamilton projector of cote16 scans048--049. The exact scheme-spreading, lambda-ring/K-theory, finite-cover, etale-realization and weight locators in the paper's framework section apply to each of these findings. No new motivic L-value estimate, ghost, or general Hodge-conjecture implication is claimed.\n''')
framework=R/'research/frameworks.tex';s=framework.read_text()
s=s.replace('The source exclusions D-BI-01--17, D-EX-01--03, D-UP-01--03,\nD-R5-01--04 and HD-E8IF1',
 'The source exclusions D-BI-01--24, D-SPOR, D-SPW, D-G2T,\nD-ESC, HD-SPIN, HD-ALT, D-AST, D-EX-01--03, D-UP-01--03,\nD-R5-01--04 and HD-E8IF1')
s=s.replace('SF-E811--816 concerns actual bundles and perfect complexes on a','SF-E811--822 concerns actual bundles, coherent sheaves and perfect complexes on a')
framework.write_text(s)
out={'integrated':['D-BI24','D-ESC01--03','SF-E821/E821a','SF-E822'],'date_utc':now,'canonical_proof_hashes':proofs}
(R/'research/unitary_even_surface_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
