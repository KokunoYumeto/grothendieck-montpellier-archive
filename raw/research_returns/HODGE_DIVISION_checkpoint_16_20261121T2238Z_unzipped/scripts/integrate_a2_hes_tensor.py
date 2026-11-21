"""Integrate only the whole-reviewed A2, finite HES, and tensor results."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
proofs={
 'research/a2_cores/a2_section.tex':'7ca6bcfa77cfe087b22a4511eadd7f51e9acf442ee895e8c2ae28e6ee3958035',
 'agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_coverage.tex':'cb92926a5cacd03e216d5799e88f10e3807e545c0110e60c3d40b59cf197efea',
 'agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex':'2df001a02737dda0ff6bbec37bc1e61fd8754bb74128ed1473dc35aa48caa870',
 'agents/sixfolds/rm_tensor_surface_obstruction_section.tex':'03ea639b7dd4aa4a3aa88abb2b885ff20a0f6b433e3d53470e01b494606e3e80',
 'agents/sixfolds/rm_unequal_slope_compensation_section.tex':'7fb6992b7d7eb29e2ba1b91b62f29febfb25df474599488ba31a56a63e5a44e1',
}
for name,h in proofs.items():
 assert hashlib.sha256((R/name).read_bytes()).hexdigest()==h,name
q=R/'QUESTIONS.tsv'
rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
newids={'Q2bc','Q2bd','Q5t','Q5u'}
assert not any(x['id'] in newids for x in rows)
now=datetime.now(timezone.utc).isoformat()
(R/'research/gates_before_a2_hes_tensor.json').write_text(json.dumps({x['id']:x for x in rows if x['id'] in {'Q2i','Q5i'}},indent=2)+'\n')
main=R/'HODGE_DIVISION.tex';s=main.read_text()
insertions=[
 ('agents/imprimitive/lie_small_fields/even_symplectic_section.tex',[
  'agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_coverage.tex',
  'research/a2_cores/a2_section.tex',
  'agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex']),
 ('agents/sixfolds/rm_coupled_surface_obstruction_section.tex',[
  'agents/sixfolds/rm_unequal_slope_compensation_section.tex',
  'agents/sixfolds/rm_tensor_surface_obstruction_section.tex']),
 ('agents/imprimitive/lie_small_fields/even_symplectic_bibitems.tex',[
  'agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_bibitems.tex',
  'research/a2_cores/a2_bibitems.tex',
  'agents/imprimitive/lie_small_fields/higher_even_symplectic_bibitems.tex']),
 ('agents/sixfolds/rm_coupled_surface_bibitems.tex',[
  'agents/sixfolds/rm_tensor_surface_bibitems.tex']),
]
for anchor,paths in insertions:
 a='\\input{'+anchor+'}';assert a in s
 assert all(path not in s and (R/path).exists() for path in paths)
 s=s.replace(a,a+''.join('\n\\input{'+path+'}' for path in paths))
a='precise non-Eisenstein degree-seven exclusion. Other small-field\nhigher-rank Lie representations remain outside these exclusions.'
b=r'''precise non-Eisenstein degree-seven exclusion. D-A2-01--03 excludes
all ordinary quasisimple $\operatorname{PSL}_3(q)$ and
$\operatorname{PSU}_3(q)$ cores for $q\ge3$, including mixed fields
and types. L34-1--3 supplies the exceptional $\operatorname{PSL}_3(4)$
normalizer coverage by the published thirty-six bicyclic classes;
the computed universal table is only a redundant check.
The successful $\operatorname{PSL}_3(2)=\operatorname{PSL}_2(7)$
case is explicitly outside that exclusion. D-HES-F excludes arbitrary
mixed products of $\operatorname{Sp}_8(2)$, $\operatorname{Sp}_{10}(2)$
and $\operatorname{Sp}_{12}(2)$, with all normalizing scalars and factor
permutations. Other small-field higher-rank Lie representations remain
outside these exclusions.'''
assert a in s;s=s.replace(a,b)
a='''nonsplit examples. Unequal degrees, other support classes, nonreduced
or singular surface modules, and more general derived couplings remain
open.'''
b=r'''nonsplit examples. SF-US constructs an actual unequal-degree unit
surface extension and a positive integral split hull with the entire
balanced character; all constant bivectors have explicit local
nullhomotopies. This construction is not a semiregular seed.
SF-E823 excludes every actual global tensor product $H\otimes M_0$
with that unit extension, arbitrary locally free positive-rank $H$,
and rational $B$ giving the balanced character. A derived partial trace
forces a nonzero cubic character obstruction to vanish. This includes
unstable and nonsplit hulls, without requiring an action on either
factor separately. Genuinely different global gluing, other unequal-degree
extensions, other support classes, nonreduced or singular surface modules,
and more general derived couplings remain open.'''
assert a in s;s=s.replace(a,b);main.write_text(s)
for x in rows:
 if x['id']=='Q2i':
  a='Other small-field higher-rank Lie cores remain.'
  b='D-A2-01--03 excludes all ordinary quasisimple PSL3(q)/PSU3(q) cores q>=3, including mixed types/fields; L34-1--3 proves the exceptional36-class normalizer coverage. PSL3(2)=PSL2(7) remains explicitly outside. D-HES-F excludes all mixed products of Sp8(2),Sp10(2),Sp12(2), including scalars/permutations. Other small-field higher-rank Lie cores remain.'
  assert a in x['finding_ids_or_current_gate'];x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace(a,b)
 if x['id']=='Q5i':
  a='Remaining: unstable bundles,'
  b='SF-E823 excludes every actual global tensor H times the unequal-degree unit surface extension M0, for every positive-rank locally free H and rational B giving the balanced character, without a factorwise finite action. SF-US constructs an actual positive integral full-character example and local nullhomotopies, but no seed. Remaining: unstable bundles,'
  assert a in x['finding_ids_or_current_gate'];x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace(a,b)
  x['finding_ids_or_current_gate']=x['finding_ids_or_current_gate'].replace('outsideE818/E821/E822 (including unequal-degree,','outsideE818/E821/E822/E823 (including genuinely different global gluing, other unequal-degree,')
newrows=[
 ['Q2bc','Prompt target2; complete A2/2A2 normal cores','Can ordinary quasisimple PSL3(q) or PSU3(q) cores with q>=3 support actual period rank9?','refuted','D-A2-01--03 with L34-1--3: all mixed types/fields, cyclic-center quotients and compatible outer normalizers excluded. Generic46row types386cells, finite47tables1603rows141024spectra34fusions; published36 bicyclic classes handle PSL3(4). PSL3(2) is explicitly outside.'],
 ['Q2bd','Prompt target2; complete higher even-symplectic finite cores','Can a mixed product of Sp8(2),Sp10(2),Sp12(2) support the required period rank?','refuted','D-HES-F:756 complete rows271785 entries, reality plus nontrivial bilinear multiplier and two half-rank inertias force e<=6 against minimum35. Official Sp12 table is attributed to Koehler; no separate refereed construction source claimed. This theorem uses no GM1998 bound.'],
 ['Q5t','Prompt target5; actual tensor hull repairs of unequal-degree unit surface extension','Can any global tensor H times M0 with balanced character be weakly equivariant semiregular?','refuted','SF-E823: global derived partial trace, B-shear and BF evaluation force the nonzero cubic obstruction of M0 to vanish. Covers arbitrary positive-rank locally free H, unstable/nonsplit, and action on tensor product alone. Does not infer a tensor product from local unit matrices.'],
 ['Q5u','Prompt target5; unequal-degree surface unit model','Does the unit extension admit an actual positive integral compensated character and all local bivector deformations?','proved','SF-US: actual global3-term resolution and unit extension; all local star-product homotopies;16 positive integral line-bundle multiplicities, total rank522387689472, entire balanced character at q=1/2. Root arithmetic rerun PASS. This construction alone is not counted as a main-gate reduction; SF-E823 excludes every global tensor hull repair.'],
]
rows.extend(dict(zip(fields,row)) for row in newrows)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-A2-01--03','targeted proof check','Root read and checked the complete authored proof, all generic extractor/certificate code, complete GAP exporter and finite checker, and whole independent G34 report. Canonical status-only revision recorded. PASS full mixed-core/scalar/outer statement, proper small-field exception and exact endpoint budget.','research/a2_cores/a2_section.tex; agents/g34_eightfolds/bireflection/A2_CORES_PEER_AUDIT.md'),
 ('D-A2 exact generic and finite arithmetic','computation or formal certificate','Actual retained root checks PASS46nontrivial row types386cells and47tables1603selected rows141024spectra34fusions; finite runtime4.122447seconds. Peer independently selected rows/reconstructed spectra in4.334442seconds using its prior cyclotomic helper; this is not a third independent Fourier algorithm.','research/a2_cores/generic_certificate.json; research/a2_cores/small_checked.json'),
 ('Simpson-Frame1973;corrected GCT;HHM Chapter5Table1','used and rechecked in this run','Fresh root original SF construction/restriction text and exact table locators read; printed Table1b OCR is not claimed entrywise checked. All four frozen official generic headers/corrections read, including central characters, parameter moduli and Geck corrections. Original Geck1990 full text was not accessible. HHM full exception paragraph/Table1 p35 freshly read.','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0DA5E003E1F9E8B176D638EFD3080556/S0008414X00050513a.pdf/the-character-tables-for-sl3-q-su3-q2-psl3-q-psu3-q2.pdf; https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/; https://www.math.rwth-aachen.de/homes/Gerhard.Hiss/Preprints/ImIrrMod.pdf'),
 ('L34-1--3','targeted proof check','Root read entire normalizer proof, complete multiplier checker and full independent imprimitive audit. PASS cyclic extension with nonsplit power relation, explicit isoclinism transfer of implementing matrices,20kernels8orbits36pairs and arbitrary actual normalizer coverage. This is not a general identical-character-table claim under isoclinism.','agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_coverage.tex; agents/imprimitive/audit_l34_normalizer/PEER_AUDIT.md'),
 ('L34 exact multiplier arithmetic','computation or formal certificate','Root actually reran complete checker:20cyclic-center kernels8orbits36kernel/cyclic-subgroup pair orbits PASS0.01109seconds. Peer separately reconstructed abstract D12 action.','agents/g34_eightfolds/bireflection/l34_normalizers/check_multiplier.py'),
 ('Breuer-Malle-OBrien2017 Section3.3/3.3.1 Lemma3.1','used and rechecked in this run','Root read full invoked original section and lemma, author pp5--6, from frozen original PDF. It covers36bicyclic classes. Source C4 label discrepancy recorded; both quotient types and all .2 extensions are retained, so coverage does not depend on selecting the disputed label.','agents/g34_eightfolds/bireflection/l34_normalizers/normalizer_coverage.tex; sources/BreuerMalleOBrienAtlas.txt'),
 ('D-HES-F','targeted proof check','Root whole proof/code review and final whole canonical reread PASS; full independent756row peer report read. Covers all mixed products with arbitrary scalars/permutations. The Sp12 provenance was corrected to Koehler before integration and remains explicit.','agents/imprimitive/lie_small_fields/higher_even_symplectic_finite_section.tex; agents/g34_eightfolds/bireflection/HIGHER_EVEN_SYMPLECTIC_FINITE_PEER_AUDIT.md'),
 ('D-HES-F exact arithmetic','computation or formal certificate','Root actually reran expanded complete checker:756rows271785entries PASS0.403seconds. Independent peer reconstruction PASS0.585070seconds. Exact maxima3/5,17/31,11/21 are rationally attained. Full character-table construction is an identified input, not rederived by these checks.','agents/imprimitive/lie_small_fields/check_sp2n2.py; agents/g34_eightfolds/bireflection/audit_higher_even_symplectic_finite.json'),
 ('Gluck-Magaard2006 p25;CTblLib S12(2)','used and rechecked in this run','Fresh root primary p25 paragraph on trivial outer groups/multipliers read. Official complete S12 table record freshly read;477classes and Koehler attribution verified. The public page is generated from1.3.10; retained local package1.3.11, without conflation.','https://www.academia.edu/29518749/Absolute_Fourth_Moments_and_Finiteness_of_Linear_Groups; https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/S12%282%29.html'),
 ('SF-US','targeted proof check','Whole actual construction, local homotopy proof, author scripts and all314canonical lines read. PASS extension unit/global resolution, torsion/hull/defect, exact local star correction,16positive multiplicities and full character. No finite action, global homotopy or semiregularity is inferred.','agents/sixfolds/rm_unequal_slope_compensation_section.tex'),
 ('SF-US exact computations','computation or formal certificate','Root actually reran both certificates: local symbolic homotopy PASS0.30225seconds; full positive integral hull computation completed PASS at scale16, rank522387689472. Earlier negative scales4/8 retained.','agents/sixfolds/rm_unequal_slope_local_homotopy_output.json; agents/sixfolds/rm_unequal_slope_compensation_output.json'),
 ('SF-E823','targeted proof check','Root whole frozen draft and full277line canonical proof read; full independent imprimitive report read. PASS global derived partial trace, Atiyah tensor identity, rational B complex-cohomological shear, finite-action forgetting and nonzero cubic contradiction. Scope is actual global tensor products only.','agents/sixfolds/rm_tensor_surface_obstruction_section.tex; agents/imprimitive/audit_tensor_surface/PEER_AUDIT.md'),
 ('SF-E823 exact exterior calculation','computation or formal certificate','Root author-certificate rerun PASS0.35075seconds: full symbolic character, both cap kernels/cubic obstructions and512B-shear basis checks. Peer separately used sorted exterior tuples/different B matrix and passed512checks0.203seconds. These finite checks do not establish derived partial trace on their own.','agents/sixfolds/rm_tensor_surface_certificate_output.json; agents/imprimitive/audit_tensor_surface/PEER_AUDIT.md'),
 ('Buchweitz-Flenner2008 Th5.1.3 Prop5.2.2 Cor5.2.3','used and rechecked in this run','Fresh root read complete Th5.1.3 proof authorpp24--25, complete Prop5.2.2 proof p26 and Cor5.2.3 p27; negative-At exponential convention checked. Prior whole6.2.1/6.3.2/6.4.2/6.4.4 reading remains recorded for E819, not claimed fresh here.','https://arxiv.org/pdf/math/0606730'),
]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Complete A2, finite higher symplectic and tensor-surface integration\n\n'+now+' — Q2bc/Q2bd/Q5t refuted after whole root and independent peer reviews. Q2i strictly shrinks by all A2/2A2 cores q>=3 and the three finite higher symplectic groups; Q5i strictly shrinks by every actual tensor repair H times M0, independently of the hull splitting. Q5u records the actual positive-character construction/local homotopies but is explicitly not counted alone as gate movement. The elementary all-rank symplectic replacement and non-tensor gluing remain active drafts, not checked conclusions here. This integration is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('''\n## Complete rank-three cores and global tensor obstruction\n\nD-A2-01--03 and L34-1--3 remove every ordinary quasisimple PSL3(q)/PSU3(q) supplier for q>=3, with the successful PSL3(2) case explicitly preserved. Cyclic-center covers and nonsplit cyclic-outer powers are handled at the level of actual implementing matrices. D-HES-F excludes the three complete finite higher even-symplectic core families, and mixed products, by exact complete character inputs and a bilinear-multiplier budget. These results constrain finite covers and weight-one variations; none supplies a missing cycle or infers a period rank merely from parameter counts.\n\nSF-US gives actual integral positive objects in the lambda-ring/K-theory calculation: a coherent perfect unit surface extension and a positive integral hull of rank522387689472 with the entire balanced character. The local bivector homotopies truly exist. SF-E823 nevertheless excludes every global tensor repair by derived partial trace and published Hochschild/Atiyah evaluation. Thus the obstruction is global and independent of stability or splitting. The actual remaining route must change global gluing or the specified extension model, not only the tensor hull. No balanced semiregular seed for DEG_L S-14 is asserted.\n\nThese restrictions concern the supplier-existence part of condition A, cote16 scan050 (SIGN_NEXT SN-C03/C04). Positive norm/degree steps retain condition I, cote16 scan049 and cote44 scan002/footer1 Theorem4. The resultant projector remains the Cayley-Hamilton inverse of cote16 scans048--049. The framework section supplies exact scheme-spreading, lambda-ring, K-theory, SGA finite-cover/etale and weight locators for these findings. Nothing here establishes a motivic L-value bound, a ghost under GHOSTS B03, or a new general Hodge-conjecture implication.\n''')
framework=R/'research/frameworks.tex';s=framework.read_text()
s=s.replace('D-ESC, HD-SPIN','D-ESC, D-A2, L34, D-HES-F, HD-SPIN')
s=s.replace('SF-E811--822 concerns','SF-US and SF-E811--823 concern')
framework.write_text(s)
out={'integrated':['D-A2-01--03','L34-1--3','D-HES-F','SF-US','SF-E823'],'date_utc':now,'canonical_proof_hashes':proofs}
(R/'research/a2_hes_tensor_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
