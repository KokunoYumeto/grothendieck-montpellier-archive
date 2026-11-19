"""Serialize manually checked links and isolate reported project provenance.

The source-context extraction at the end preserves literal note paragraphs. It
does not infer a link's mathematical validity from a heading or keyword.
"""
from pathlib import Path
import json,csv,re
P=Path('/workspace/scratch/7feb9690b71f/SA08_work/work/late')
rows=[]
def L(a,b,relation,ids,kind='within cote136',refs='',scope='Both supplied transcription passages read; mathematical relationship checked at the stated level.'):
 rows.append(dict(link_id=f'SA08-LL{len(rows)+1:03}',kind=kind,source_locator=a,target_locator=b,relation=relation,statement_ids=ids,reference_keys=refs,verification=scope))
L('136/233; MPL_136_189-234 tex1481–1488','136/235; D10–46','The definition of the completed coefficient PD ring and its tail ideals continues directly into the filtered simplex construction. The graded-free hypothesis is added on235.','SA08-403;SA08-C201;MP-SA08-60')
L('136/27–29; MPL_136_002-046 tex699–790','136/252,265; D741–787,1309–1342','Same positive-degree binomial tail-rigidity theorem and induced-target higher-Ext assertion, restated through finite adjunctions. The special proof requires exact L; the abstract underived-composite argument is insufficient.','SA08-430;SA08-431;SA08-C215;SA08-C222;MP-SA08-63;MP-SA08-66')
L('136/26–27; MPL_136_002-046 tex695–698','136/256–257; D888–959','Same elementwise eventually annihilated negligible class; in characteristic p its extension closure fails. The localizing Serre closure of bounded modules is a different repaired category.','SA08-469;SA08-C217;SA08-C287;MP-SA08-64')
L('136/137; MPL_136_095-141 tex1099–1166','136/235–239; D10–46,96–115,146–152','Earlier dualized Stokes/integration and later filtered comparison share the coefficient PD simplex construction. These later pages do not themselves supply a new integration theorem.','SA08-403;SA08-C204;MP-SA08-60',scope='Both endpoints read. This is a structural comparison, not a claimed literal cross-reference or an identification of all degree conventions.')
L('136/139–141; MPL_136_095-141 tex1201–1271,1304–1362','136/251; D666–689','Completed PD quotient and top-form integration are earlier constructions;251 gives a cancelled scaled coefficient-change attempt X_i,dX_i↦λX_i,λdX_i. Compatibility would require checking the weight normalization.','SA08-410;SA08-C210;MP-SA08-62',scope='Both endpoints read; the link is the explicit coefficient/weight dependence, not an established commutative integration diagram.')
L('136/235; D39–46','136/239–241; D172–239','The graded-free PD hypothesis is tested by the p-adic specialization. Odd-prime cofinality does not imply free associated graded; at p=2 positive ideals stabilize.','SA08-406;SA08-407;SA08-C206;SA08-C207;MP-SA08-61')
L('136/237; D85–88','136/237–239; D92–115,146–152','The unfiltered formula is deleted and replaced by a filtered comparison in a stated range. No reason for the cancellation is supplied.','SA08-404;SA08-C204')
L('136/247; D398–467','136/249; D510–601','The cancelled odd/even divided-power construction continues through scalar, factorial and Pascal checks. The yy′=0 restriction remains essential.','SA08-408;SA08-C208;SA08-C209;MP-SA08-62')
L('136/253; D795–836','136/324; E1922–1933','The cancelled cohomology-PD proposal uses a coefficient ideal; the later Hom-convolution question also concerns an ideal. Cohomological descent is additional to existence of cochain/ideal powers.','SA08-411;SA08-489;SA08-C211;SA08-C255;MP-SA08-62;MP-SA08-85')
L('136/252; D721–789','136/283,287; E28–125,266–321','The four finite adjoints q⊣i⊣τ⊣ρ are restated with left/high and right/low cutoff conventions. Variance and ambient grading must be aligned.','SA08-415;SA08-C212;SA08-C214;MP-SA08-63')
L('136/263; D1211–1269','136/265–269; D1309–1363,1384–1418,1436–1468','The abstract derived inference is applied to PD tails and then revised toward derived recovery. The special PD result is true using exact L, though the abstract implication is false.','SA08-C221;SA08-C222;SA08-C223;SA08-C224;MP-SA08-66')
L('136/256–257; D888–959','136/267,273; D1384–1418,1552–1569','Three possible infinite cutoff constructions—bounded quotient, elementwise-tail class, and localizing Serre closure—must be distinguished before section functors or derived recovery are compared.','SA08-469;SA08-C217;SA08-C218;SA08-C225;SA08-C287;MP-SA08-64')
L('136/277; D1660–1705','136/299; E688–707','The universal coefficient presentation is continued by the negative-degree binomial recurrence. Its representing group is Q; resulting coefficients are Hom_Z(Q,M), not M⊗Q.','SA08-484;SA08-C230;SA08-C239;SA08-C286;MP-SA08-72')
L('136/279; D1731–1803','136/281,285; D1827–1910,E157–218','The dual coalgebra/tensor and cofree cotensor discussion continues through completion and stabilization attempts. Ordinary cofree cotensor is valid, while infinite intersections and completed products need separate hypotheses.','SA08-C231;SA08-C232;SA08-C233;SA08-C234;SA08-C235;MP-SA08-73;MP-SA08-74')
L('136/275; D1584–1625','136/295; E564–605','The earlier tensor/internal-Hom existence questions are sharpened to a C-valued right-adjoint construction. Products and kernels give the ordinary additive right Kan extension. The doubtful differential enhancement is separate.','SA08-C227;SA08-C228;SA08-C236;SA08-C237;MP-SA08-70;MP-SA08-75')
L('136/302–305; E744–923','136/311–314; E1169–1472','Free presheaf cocompletion is the ordinary universal construction behind free additive chains and abelianization. It is not yet a homotopy localization or a multiplicative classifier.','SA08-C240;SA08-C241;SA08-C246;SA08-C248;SA08-C249;MP-SA08-77;MP-SA08-79')
L('136/306–307; E975–1026','136/315–318; E1485–1683','The additive Karoubian normalization equivalence supplies the operation programme, but the author explicitly flags projector availability, variance, and native versus transported multiplication.','SA08-C242;SA08-C250;SA08-C251;MP-SA08-78;MP-SA08-81')
L('136/309–310; E1118–1144','136/318; E1681–1683','Unfixed totalization signs and the tensor warning are distinct obstacles: the Koszul sign repairs a commuting bicomplex, while the native tensor discrepancy requires transport or chain equivalence.','SA08-482;SA08-C245;SA08-C251;MP-SA08-78')
L('136/320–323; E1685–1918','136/324–325; E1919–1970','Yoneda translates natural Gamma/Hom operations into divided coproduct maps; universal direct-sum inclusions encode addition. The final existence/uniqueness questions still require exact naturality and index ranges.','SA08-C252;SA08-C253;SA08-C254;SA08-C255;SA08-C256;SA08-C257;MP-SA08-84;MP-SA08-85;MP-SA08-86')
L('136/326; E1978–2057','136/327; E2061–2162','Real/complex group conventions and principal-parts sketches precede the pointed disc torsor and the split-bundle connection problem. The author cancels the full group in favor of a stabilizer and changes analytique to top.','SA08-C260;SA08-C261;SA08-C262;SA08-C263;SA08-C264;MP-SA08-87')

# Exact donor leaves. PDF pagination is published page+5, independently checked.
sgas=[
 ('236','D53–83','13.5.12 and14.1','506','SA08-C268'),
 ('238','D121–141','13.5.5–13.5.8','504–505','SA08-C267'),
 ('240','D180–199','13.5.3','503','SA08-C266'),
 ('242','D241–247','13.5 opening/relative GAGA','500','SA08-C265'),
 ('260','D1062–1104','8.3','417','SA08-C269'),
 ('262','D1186–1204','Proposition7.5','412','SA08-C288'),
 ('264','D1270–1307','6.2.1','394','SA08-C270'),
 ('266','D1366–1382','7.1.5–7.1.6 and7.2 opening','402','SA08-C271;SA08-C272'),
 ('268','D1420–1434','7.1.3 continuation','401','SA08-C273'),
 ('270','D1470–1486','7.1.3 formal quotient','400','SA08-C271'),
 ('272','D1535–1548','6.4 trace continuation','399','SA08-C274'),
 ('274','D1549–1581','6.4 p-adic comparison','398','SA08-C274'),
 ('276','D1626–1645','10.5','445','SA08-C276'),
 ('278','D1708–1729','9.3 compatibility','426','SA08-C277'),
 ('280','D1807–1826','3.5.2 and3.6 opening','351','SA08-C278'),
 ('282','E2–27','Corollary3.8','353','SA08-C279'),
 ('284','E126–156','3.5 equivalences','350','SA08-C279'),
 ('286','E219–265','9.3 blended extension','421','SA08-C277'),
 ('288','E322–353','9.2 continuation','420','SA08-C277'),
 ('290','E401–426','9.2 pairing/transvections','419','SA08-C277;SA08-C279'),
 ('296','E606–629','9.1 Tate dependency','418','SA08-C275'),
 ('298','E657–667','Theorem3.6 proof','352','SA08-C278'),
 ('300','E710–730','12.8.3 Picard argument','478','SA08-C280')]
for scan,line,sec,page,ids in sgas:
 L(f'136/{scan}; {line}',f'SGA7I ExposéIX §{sec}, publishedpp{page}',
   'Exact donor-text match; 1972 publication predates the live1975–1976 PD compilation. Missing surrounding hypotheses are retained from the published section, not invented from the fragment.',ids,'his published work','late_SGA7IX',
   'Archive transcription and original SGA7PDF/OCR passage read. Original formula images inspected where needed; no archive ink was available. Original PDF page=published+5.')

L('136/235–239,273; D10–46,96–115,146–152,1571; earlier note D#74','Cartan1976 §5Th3p267,§6p268,§7pp269–271','Exact weighted integral cohomology comparison, with flat-cycle/extendability hypotheses and binomial product factor. Cartan explicitly records the12Dec1975 lecture and the gcd1 recovery argument. The manuscript says compatible avec multiplication at D1571; the weighted-product/gcd deduction is the earlier run’s note#74, not the module-rigidity recurrence on275.','SA08-C204;SA08-C284;MP-SA08-60','later literature','late_Cartan1976','Both endpoints read in full relevant passages; exact original publication pages inspected.')
L('136/237–239; D96–115,146–152','Garvin etal1998 Th4.1p175,Th4.2p176,Remark3.3p175','Arbitrary simplicial-set fixed-length comparison holds in strict p<q. It does not certify the manuscript inclusive boundary or an arbitrary completed coefficient ring.','SA08-C204;MP-SA08-60','later literature','late_Garvin1998','Full8-page original read; explicit bound and counterexample to(q+1)-extendability checked.')
L('136/253; D795–836','Richter2009 Def7.4 andTh7.5pp249–251; Stacks09PFDef23.6.5 warning','Boundary compatibility is needed for divided powers to descend to homology; differential compatibility alone is insufficient.','SA08-C211;MP-SA08-62','later literature','late_Richter2009;late_Stacks09PF')
L('136/305; E876–923','Kelly1982/2005 Th4.51pp67–68','The ordinary presheaf free-cocompletion universal property supplies the categorical content of Proposition1, with cocompleteness and size assumptions.','SA08-C241;MP-SA08-77','later literature','late_Kelly1982')
L('136/315–318; E1485–1683','Kelly1982/2005 Th5.35pp99–100','Free completion under a specified small class of colimits gives a precise model for the operation-category programme; variance and projector assumptions still need to be supplied.','SA08-C250;MP-SA08-81','later literature','late_Kelly1982')
L('136/318; E1681–1683','Richter2009 Th7.1pp248–249; Schwede–Shipley2003 IntroTh1.1','Transported monoidal structure under Dold–Kan and associative model equivalences are precise later developments. They do not identify native integral commutative dg algebras with simplicial commutative algebras.','SA08-C251;MP-SA08-78','later literature','late_Richter2009;late_SchwedeShipley2003')
L('136/324; E1922–1933','SGA4III XVII5.5.2.4–5p374;5.5.2.6–8p375','For flat modules Gamma^n agrees with symmetric invariant tensors; this yields the flat divided-coproduct convolution proof. The assembled Hom theorem is our reconstruction, not stated verbatim there.','SA08-C255;SA08-C256;SA08-C285;MP-SA08-85','published input','late_SGA4XVII;late_Lundkvist2008','Original SGA4PDF377–378 rendered and inspected; exact theorem and direct-sum/base-change passages read.')
L('136/306,311–312; E946–966,1169–1224','Ekedahl2002Th2.9pp6–7; Horel2024Th5.4–6.1p13,§8.4–8.5p19; Toën2020Th4.1p11,§5p13','Numerical/binomial and affine homotopy reconstructions have explicit nilpotence/finite-type/connectivity hypotheses and richer input. They bound the general programme; none identifies the manuscript PD category.','SA08-C243;SA08-C246;SA08-C247;MP-SA08-79','bounded later comparison','late_Ekedahl2002;late_Horel2024;late_Toen2020','Exact primary theorem passages read; only the stated bounded comparisons are asserted.')
L('136/326–327; E2016–2057,2148–2156','Biswas–Hurtubise–Roubtsov2021 Lemma2.2,Prop2.4,Cor2.6pp6–8','The nonsplit jet extension0→L→J1(L^-1)→L^-1→0, L²=K, is an exact oper comparison. It is not an emendation of the written direct sum.','SA08-501;SA08-C264;MP-SA08-87','bounded later comparison','late_BHR2021')
L('136/327; E2079–2082,2148–2156','Dumas2009 §2p7,§§3.2–3.3pp10–12','Uniformization supplies the analytic Fuchsian projective structure; projective structures form an affine H0(K²)-space. This does not yield a connection on the literal split holomorphic bundle.','SA08-C263;SA08-C264;MP-SA08-87','later literature','late_Dumas2009')
L('136/300; E710–730','Stacks0D24Prop99.11.8','A precise Picard algebraic-space theorem needs flat proper finite presentation and universal O_T≅f_*O. Scheme representability is a stronger conclusion.','SA08-C280','later literature','late_Stacks0D24')
L('136/239; D154–170','136/346; codex/K136-02 tex306–315',
  'Both passages ask what Gamma^p(Psi) is. The exact normalized quadratic complex has boundary multiplication by2; it is not an ordinary K(k,2). The doubtful Pi/K name on239 and the question marks on346 remain diplomatic readings.',
  'SA08-C205;SA08-C958;MP-SA08-60','within cote136','late_BMT2016',
  'Both full transcription passages independently read; programs/late_quadratic_normalization.py and the separate root quadratic calculation agree. No manuscript scan was supplied.')

# Correct cross-reference IDs against the actual claim map. The relationships
# above are human-authored; this only expands already assigned problem links.
fix_claims={
 8:['SA08-408','SA08-C209'],
 15:['SA08-C227','SA08-C228','SA08-C237','SA08-C238'],
 16:['SA08-C240','SA08-C241','SA08-C245','SA08-C247','SA08-C248'],
 17:['SA08-C242','SA08-C243','SA08-C250','SA08-C251'],
 18:['SA08-482','SA08-C244','SA08-C251'],
 51:['SA08-455','SA08-456','SA08-457','SA08-458','SA08-C289','SA08-C290']}
problem_rows=json.loads((P/'problems.json').read_text())
for pos,row in enumerate(rows,1):
 ids=fix_claims.get(pos,[s for s in row['statement_ids'].split(';') if not s.startswith('MP-')])
 for problem in problem_rows:
  if any(s in problem['claims'] for s in ids):ids.append(problem['id'])
 row['statement_ids']=';'.join(dict.fromkeys(ids))

def write(name,data):
 with (P/name).open('w') as f:
  w=csv.DictWriter(f,list(data[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
write('links.tsv',rows)

# Explicit project links are kept apart from proved archive/publication links.
projects=[]
def Pj(notes,local,external,runs,relation):
 projects.append(dict(project_link_id=f'SA08-PL{len(projects)+1:03}',source_entries=notes,local_locator=local,reported_external_locator=external,reported_runs=runs,reported_relation=relation,verification='Local manuscript endpoint and note attribution checked. External context file not supplied independently in this consolidation; external endpoint remains an explicitly unverified lead, not a result.'))
Pj('D#1,D#3,D#4,D#14,D#52','235–239,244–281','Pursuing StacksVI§124p521; ps_chapters_VI_VII/ps6.tex lines3965–3980','WG2§2.4#5;WG2§Week#3;WG H6;GALOIS E.11','A later realization-functor programme mentions PD de Rham complexes; it does not prove the local filtered comparison or reinstate the deleted unfiltered assertion.')
Pj('D#50','281;D1827–1910','PSVI§111pp450–451,lines370–404','WG H6;GALOIS E.11','Coalgebra exponential comparison is a universal coalgebra construction, not an assertion that the exponential is an algebra morphism.')
Pj('D#51,E#56','239,275,279,299,318','PSVI§119pp500–502,lines2951–2988; W2example','follow-ups@304;WG2§2.4#5','The failed schematic/integral comparison and binomial retreat are different from the PD cohomology theorem and from the local binomial-tail rigidity proof.')
Pj('D#53','235–239,275','PSVI§127pp535–536,lines4716–4749','WG H6;GALOIS G.6','Reported fpqc sheafification does not identify a de Rham site in these leaves.')
Pj('D#54,E#58','273,275,279–281,283,311–312','PSVII§139pp590–591,lines1716–1768','gap g1048;follow-ups@305;GALOIS E.11;GALOIS G.6;WG H6','Additive envelopes with a natural diagonal may retain operations; no equivalence with bare derivators or proof of multiplicative recovery is supplied.')
Pj('E#54','305,313–314','PSVII§134pp557–559eq1–8;§136pp565–566','follow-ups@305;GALOIS E.11;GALOIS G.6','Derived abelianization Lp_!^ab and its localization are further constructions, not the ordinary free-cocompletion theorem.')
Pj('E#55','318,320–324','PSVI§111pp455–456,(y′)','follow-ups@304;follow-ups@305','The later nonlinear divided-power warning requires resolutions; it cannot be reduced to the native-versus-transported tensor distinction.')
Pj('E#57','312,315–318','PSVI§120pp506–507; Hua invariant additif universel','follow-ups@305','Analyzers are a conceptual continuation lead; composition and its universal category are not completely constructed here.')
Pj('E#59','314,327','PSVI§122pp511–513','follow-ups@305','The augmentation-one universal abelian torsor requires local inhabitation; it is not the projective/disc torsor on327.')
Pj('D#1,D#24,E#16,E#17','252–277,287–299','notes/RESULTS_STATE.md123–127; Hua findings136-shadow-full-faithfulness','Commutator-IO/grothendieck-project;Lean card holds more generally','The register supplies a conjecture/unsearched status and statement-level intake, not a formal proof. This run independently proves the nonnegative tail and exact-L claims.')
Pj('E#17','287–299','R17–21,293–299; MPL_121_001-048Q1; MPL_152+120Q1-06','module-shadows register','Exact graded-module comparison is possible, but the source definition in the other cote is unavailable. Tubulure is not established as a synonym.')
Pj('E#18,E#51','326–327','R20–21,294,457; MPL_133B10(cote133/009,028–029)','WG2§2.4#5','Possible integrality/connection cross-cote lead; scan137 of cote136 is not cote137. No application to cote137 or Fourier-transform Chern classes is established.')
Pj('E#46–E#53,E#84','326–327','hua_project/136.modern.tex2174–2196; geometry subsection','Michel Hua project AI-produced modernization','Projective-curve identification is useful, but its group, pointing, split-bundle and Euler statements exceed or compress the current source. Parent separately checks the supplied328 continuation.')
Pj('D#1,E#5','302–307','Pursuing Stacks/full-Delta comparison; reported Delta_inj studies','PRETOT A.12;TOTASPH C.10;TOTEX2 D.1–D.2','Results about Delta_inj do not transfer from the historical word demi-simplicial; the current definition includes degeneracies.')
write('project_links.tsv',projects)

# Lossless extraction of all explicit context/register paragraphs: a provenance
# appendix, not another set of mathematical verdicts. Every entry was read.
provenance=[]
for fn in sorted(P.glob('*entries_source.json')):
 for e in json.loads(fn.read_text()):
  paragraphs=e['text'].split('\n\n')
  selected=[p for p in paragraphs if any(marker in p for marker in ['**Context', '**Register:', '**RESULTS_STATE:', '**R:**'])]
  if selected:
   provenance.append(dict(entry_id=e['entry_id'],note_line=e['note_line_start'],reported_context='\n\n'.join(selected),status='Literal note provenance retained; external project endpoints unavailable independently. Same-cote endpoints checked elsewhere are not automatically certified by this extraction.'))
write('project_context_provenance.tsv',provenance)
print(json.dumps({'checked_links':len(rows),'isolated_project_leads':len(projects),'literal_context_entries':len(provenance)},indent=2))
