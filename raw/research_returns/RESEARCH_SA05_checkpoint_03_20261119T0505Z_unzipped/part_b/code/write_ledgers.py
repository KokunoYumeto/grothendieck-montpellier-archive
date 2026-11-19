"""Rebuild the Part B checkpoint ledgers from explicit audit records."""
from pathlib import Path
from datetime import datetime, timezone
import csv

ROOT=Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work/part_b')
STAMP=datetime.now(timezone.utc).isoformat(timespec='seconds')
WHO='GPT-6 Astra (OpenAI), Pro research run, agent /root/part_b'
event_path=ROOT/'part_b_CHECK_EVENTS.tsv'
old_event_dates={}
if event_path.exists():
 with event_path.open(newline='') as f:
  for e in csv.DictReader(f,delimiter='\t'):
   old_event_dates[(e['statement_id'],e['who'],e['type'],e['outcome'])]=e['date']

class PreservingEventWriter:
 def __init__(self,stream): self.writer=csv.writer(stream,delimiter='\t')
 def writerow(self,row):
  row=list(row)
  if len(row)==5 and row[0]!='statement_id':
   row[1]=old_event_dates.get((row[0],row[2],row[3],row[4]),row[1])
  self.writer.writerow(row)

rows=[
('B.1','All requirements under Tate plus semisimplicity','PARTLY REFUTED; UNIVERSAL COMPARISON UNRESOLVED','thm:B-Geisser-gate','Geisser 7.1,8.4; Conj8.3','12:60-73;15:173','The literal continuity and algebraically closed vanishing requirements contradict the finite-point computation. The compatible universal comparison has exactly the numerical-Chow-phantom gate under Tate and semisimplicity. All abelian-type cases are proved using the current external CM Hodge theorem.'),
('B.1-point','Finite point values and restriction e_q to m e_qm','PROVED','prop:B-e','Geisser7.1; finite-field K theory','12:71;15:173','Negative twists use Q/Z prime-to-characteristic shifted by -1; l=p cyclotomic convention excluded.'),
('B.1-gate','Full Weil-etale comparison implies rational=numerical equality','KNOWN; DERIVATION CHECKED','thm:B-Geisser-gate','Geisser8.4','12:63-64','Universal three-part Geisser T implies comparison and finite generation.'),
('B.1-abelian-type','Every twist for all smooth projective varieties of abelian Chow type','PROVED FROM CURRENT EXTERNAL THEOREM','thm:B-abelian-type','vanHoftenSempliner2026TheoremI; Milne1999Thm7.1; Kahn2003Thms1.10,3.6,Cor3.8','12:60-73;15:173','Current CM Hodge theorem implies all-abelian Tate. Tate passes to abelian-type projectors; Kimura nilpotence supplies rational=numerical, so every integral comparison and finite generation follow, including logarithmic p-adic coefficients.'),
('B.1-phantom','Universal comparison under Tate and semisimplicity iff numerical Chow phantoms vanish','PROVED EQUIVALENCE; UNIVERSAL VANISHING UNRESOLVED','prop:B-phantom-gate','Kahn2003Thms5.1-5.2 especially viquater','12:60-73','Explicit splitting M=N+P with N abelian-type and P numerical phantom; nilpotence on N corrects the lifted inverse. This is an exact remaining obstruction, not a proof phantoms vanish.'),
('B.1-small','All twists for smooth projective curves and points; abelian divisors','PROVED','B.1 unconditional paragraph','Geisser9.3,9.5; Lichtenbaum6.1','12:71-73;15:173','Separate from arbitrary-dimensional all-twist assertion.'),
('B.1-closure','Higher algebraically closed vanishing versus continuity of e','REFUTED','prop:B-continuity','Finite point restriction calculation','12:65,71','The direct limit of the degree-one rational lines is Q, not zero.'),
('B.1-uniqueness','Uniqueness of every theory satisfying 1-4','UNRESOLVED AS STATED; LIMITED UNIQUENESS PROVED','B.1 uniqueness paragraph','Semisimple numerical category','12:60-64','Additive graded functor on fixed semisimple pure category only, normalized by e; no integral/topos/six-functor uniqueness asserted.'),
('B.2','All arithmetic Tate groups and comparisons; arbitrary pure motive','ALL TATE DEGREES PROVED; GENERAL REALIZATION CONJECTURAL','B.2','Borel; Soule; BK; Fontaine4.4-4.5,6.5-6.7; Poitou-Tate','12:63-64','Full groups retain the exact Leopoldt/Schneider parameters. Every Tate degree of the specified finite/geometric Selmer complex has a common Q-space, with higher comparison splittings explicit. General prescribed motivic realization is Fontaine f-admissibility; the compatible finite-field comparison retains the separate phantom gate.'),
('B.2-full','Full continuous rational Tate groups in every twist','PROVED WITH NAMED DEFECT PARAMETERS','thm:B-full-tate','Kummer; Euler characteristic; PT; Borel-Soule','12:63-64','Negative-twist defect is strict positive-twist regulator kernel; no unproved vanishing asserted.'),
('B.2-local','Bloch-Kato local e/f/g spaces for Q_l(n)','KNOWN; DERIVATION CHECKED','B.2 local table','BK3.8,Example3.9,Definition5.1','12:63-64','At omitted l-adic places use g for the arithmetic-open definition; distinguish f.'),
('B.2-Hf1','One rational space for degree-one finite-condition Tate cohomology','PROVED','prop:B-Hf-tate','BKDefinition5.1; Kummer; Borel-Soule','12:63-64;15:173','S-units for n1, Adams K eigenspaces n>=2, zero n<=0.'),
('B.2-higher','Higher finite-condition groups for a specified Selmer complex','PROVED FOR SPECIFIED CONSTRUCTION','cor:B-Hf-all-degrees','Poitou-Tate; Fontaine4.4-4.5; FM3.12','12:67;15:174','Complete all-degree/all-twist Q table. Two Poitou-Tate exact sequences give degree2 through chosen splittings, not a claimed canonical derived duality. At removed places twist1 includes full local H2, yielding invariant kernel/cokernel.'),
('B.2-general4','Corrected comparison for every pure motive and finite-type base','CONJECTURAL','B.2 equation B.18','BKConjecture5.3','12:63-64','A blanket implication to B1 still needs the separate finite-field Beilinson gate.'),
('B.2-Scholbach','Scholbach f-cohomology satisfies full corrected requirement4','NOT PROVED BY SOURCE','B.2 Scholbach paragraph','Remark6.2; Thm6.8,6.11,6.13','12:60-64','Source omits crystalline condition and assumes mixed-motive t-structure axioms; ordinary motivic groups lack odd Weil-etale classes.'),
('B.3','All arithmetic and finite-field abelian-scheme assertions','EQUIVALENCES PROVED IN FULL STATED SCOPE; UNIVERSAL FINITENESS REMAINS TATE/BSD','B.3','Cassels-Tate; Kummer; divisor splitting; computation','12:74-80','Arithmetic counterexamples complete; finite-field Kummer chain proved for every finite-type base, including nonreduced and nonseparated bases. Section-free relative-curve equivalence proved under the regularity explicitly present on12:79. General finiteness remains Tate/BSD.'),
('B.3-corank','Support exact sequence and corank d+s-t','PROVED','thm:B-Sha-corank','Gonzalez-Aviles-Tan MainTheorem and(6)','12:75','t is local closure rank of pro-Selmer, not abstract Mordell-Weil rank.'),
('B.3-rank','Replace local closure rank t by MW rank r','REFUTED','B.3 E389 example','Certified two-descent; local formal logarithm','12:75','E389 y2+y=x3+x2-2x has r2,s0,d1,t1; d-r+s=-1 impossible.'),
('B.3-X011','H1(S,A)[l∞] always finite with l inverted','REFUTED','B.3 X011 example','x011.gp; global Euler characteristic','12:75','E=X0(11), S=Z[1/(11l)]; infinite every l, exact corank1 at l2.'),
('B.3-restored','Restored local kernel finite iff Sha_l finite iff rational-points equality','PROVED EQUIVALENCE','B.3 equation B.21','Kummer; BKExample3.11,Prop5.4','12:74-75','Finiteness itself remains a Sha conjecture in general.'),
('B.3-Brauer-arithmetic','Br(S) to Br(relative curve) surjective modulo finite groups','REFUTED OVER ARITHMETIC BASES','prop:B-Brauer-arithmetic','MilneII2.1,Remark2.2(a); Leray; X011','12:79','S=Z[1/22], X=E_S; quotient2-primary corank1. Primary decomposition of torsion quotient is explicitly justified.'),
('B.3-finite-chain','Finite-field chain through geometric invariants and BSD','PROVED FOR REGULAR FINITE-TYPE BASE; PROPER BSD','prop:B-finite-chain-proper','YuanThm1.2 proof; BalkanSchreiederLem2.2,3.11,Prop4.10; Keller2.7.19','12:76-80','Algebraic divisor subspace splits on smooth open via Hodge index, weights, alteration trace. [a] eigenspace on total dual abelian scheme splits geometric Kummer; cofiniteness promotes rational isomorphism to finite kernel and cokernel.'),
('B.3-all-bases','Finite-field Kummer chain on arbitrary finite-type bases','PROVED','thm:B-finite-chain-all-bases','Smooth-cover pullback; LangNeron; Maschke; nilpotent thickening','12:74-80','Section space embeds in the finite-Galois section representation of a jointly surjective smooth alteration cover. Averaging a linear projection and composing its Kummer retraction proves the splitting without hypercover descent.'),
('B.3-sections-completion','Section groups modulo torsion and their rational ell-adic completion','PROVED','lem:B-sections-reduced','Conrad2006Thms2.1,7.1; deJong1996Thm4.1','12:74-80','Reduced-base section injection and LangNeron give finite free quotient; ell torsion embeds in finitely many Pruefer groups, so completion rationalization agrees with tensor Qell.'),
('B.3-singular-degree','Automatic positive-degree line bundle on a relative curve over a singular base','REFUTED BY EXPLICIT OPTIONAL EXTENSION','ex:B-singular-infinite-period','Closed-immersion pushout; smooth henselian lifting; Picard torsor class','12:79 scope qualification','S is two P2 overF2 glued along the explicit smooth elliptic cubic. Translation by id_E glues a proper smooth genus-one torsor of infinite period. Pic^d has class d alpha, so every line bundle has degree0. This is not a Brauer-infinitude counterexample and lies outside the regular scope of12:79.'),
('B.3-divisor-split','Divisor image is a Galois direct summand on every smooth open','PROVED','lem:B-divisor-splitting','Yuan1.2 proof; BalkanSchreieder2.2,3.11,4.10','12:77-79','Unconditional; full Frobenius semisimplicity and Tate are not needed.'),
('B.3-relative-curve','Relative curve Brauer/Jacobian finiteness equivalence without a section','PROVED FOR REGULAR FINITE-TYPE BASE','prop:B-relative-curve','Deligne1968Prop2.4; rational Kummer; divisor degree','12:79','A Cartier closure supplies degree d, not a finite multisection. Rational Leray and Picard identify the quotient Tate module; cofinite torsion gives equivalence modulo finite groups.'),
('B.3-Keller-error','Closure of generic-fibre point is finite over higher-dimensional base','REFUTED','B.3 source-error remark','Explicit graph uy-vx=0 in P1 times A2','12:79 source audit','Keller2016Lemma2.17 fails: closure is blowup of origin, with whole P1 fibre. The repaired proof uses line-bundle degree, not quasi-finiteness.'),
('B.3-H2-example','Manuscript degree-two abelian sheaf group can be infinite','PROVED BY EXPLICIT EXAMPLE','B.3 final example','Tate1966; finite_field_checks.py','12:78','For C/F2 with y2+y=x3-x2-10x-20 and constant A=CxC, ell3, V3H2(C,A) has dimension2. Dual abelian Tate module needs twist minus1.'),
('B.4','All integral twists and explicit generators on SpecZ','PROVED AS EFFECTIVE PRESENTATION AND CONSTRUCTION','prop:B-integral-structure','FM5.8.3; Kurihara1.5','15:173-178','Rational table complete; every finite C_m now has a terminating arithmetic presentation including 2-primary generators; primitive integral free generators now have an audited terminating cycle-and-boundary search; no uniform Vandiver vanishing is claimed.'),
('B.4-rational','Every rational Weil-etale group on compactified SpecZ','PROVED','thm:B-SpecZ-Q','FMCor3.12; BorelProp12.2','15:174','Nonzero exactly (n,i)=(0,0),(1,3), positive odd n>=3 i1, negative even n<=-2 i2.'),
('B.4-integral01','Manuscript integral twist0 and twist1 tables','REFUTED; CORRECTED','prop:B-integral-errors','FM5.8.3','15:173','Missing Z/2 in twist1 degree1 and twist0 degree3.'),
('B.4-2primary','All 2-primary C_m and a specified generator','PROVED','B.4 two-primary proposition','RognesWeibelLemma5.5,Props6.12-6.13','15:173-178','Even m: Z/2 generated by Bockstein of Kummer minus1; odd m>=3: zero. This is ordinary etale motivic C_m, not K_{2m-2} without real correction.'),
('B.4-rational-generators','Rational Beilinson generator and effective integral saturation','PROVED AS EFFECTIVE CONSTRUCTION','thm:B-primitive-generator','KerrYang2018Thms3.3,3.8; FM(88),Prop5.35','15:174','Existence and regulator survive the explicit-formula source error. Search actual admissible corrections, clear their denominators, compute exact index from special values, then enumerate an integral primitive cycle with a bounding-chain certificate.'),
('B.4-odd-algorithm','Finite invariant factors and cohomological generators for every odd-primary C_m','PROVED','thm:B-effective-odd-torsion','Soule2003Thm3; ArtinVerdier duality; finite Galois enumeration','15:174','Root proof independently audited: explicit prime and field bounds, crossed-cocycle matrix, compact-support duality, successive-order stop criterion. Not a uniform Vandiver vanishing claim.'),
('B.4-KerrYang-error','Degeneracy of every uniform Section4D W2 term','PROVED SOURCE-FORMULA DEFECT','lem:B-KY-degenerate','KerrLi2020p548footnote10; direct homogeneity proof','15:174 source audit','KerrLi confirms first K7 W2 is degenerate and cycle not closed. Every uniform Section4D W2 is homogeneous in u,v except final coordinate v minus1; substitution u=sv proves its degeneracy for all weights. No complete all-weight boundary formula is asserted or used.'),
('B.4-Vandiver37','Vandiver at irregular prime37','COMPUTATION CERTIFIED','ex:B-Vandiver37','PARIbnfcertify flag1','15:174','Class group of maximal real cyclotomic subfield is a quotient of computed trivial group; v37(B32/32)=1 confirms irregularity. All positive odd-twist C_m have zero37-primary part.'),
('B.4-structure','Structural integral formula all i,n','KNOWN; REEXPRESSED AND CHECKED','prop:B-integral-structure','FM5.8.3; cyclotomic character','15:173-178','Explicit roots-of-unity torsion and real2 terms; finite C_m have explicit terminating arithmetic presentations.'),
('B.4-Vandiver','Odd positive twist p-primary vanishing iff Vandiver','PROVED EQUIVALENCE','prop:B-Vandiver','KuriharaCor1.5; Kummer descent','15:174','All odd m>=3 for each fixed odd p; current 2026 partial-regularity source does not prove universal assertion.'),
('B.4-localization','Rational absolute localization away from twist1','PROVED FOR SPECIFIED THEORY','B.4 localization paragraph','Point calculation; Gysin triangle','15:173','Exclusion is n!=1. Do not identify ordinary motivic theory with Weil-etale completion.'),
('B.4-zeta','Order of zeta at all integers from corrected ranks','PROVED','B.4 equations B.24-B.25','FM5.8.3; regulator; functional equation','15:174','Compactly supported Weil-Arakelov real ranks required; bare Weil-etale weighted Euler expression fails at n3.'),
('B.5','Absolute duality in full rational pure-motive generality','FINITE AND ARTIN-TATE CASES PROVED; GENERAL RATIONAL REALIZATION CONJECTURAL','B.5','GS4.6; FM3.22; Lichtenbaum5.4; Fontaine6.5','12:67','Finite coefficients include vertical characteristic-primary torsion and real Tate modification. All rational Tate and finite-monodromy Tate coefficients on number rings and curves are proved. For prescribed general motivic spaces, the number-ring dual-completion comparison is exactly f-admissibility for M and M dual twist1.'),
('B.5-finite','Finite coefficient absolute duality for regular finite-type schemes','PROVED','thm:B-finite-duality','GS4.6,Lemma3.7,Thm3.9; MilneII7.6,7.11','12:67','Use etale motivic Z/m(d) if m noninvertible and Tate-modified real compact support.'),
('B.5-nonseparated','Finite absolute duality on nonseparated regular finite-type schemes','PROVED FOR OPEN-COVER COMPACT SUPPORT','prop:B-finite-duality-nonsep','GS3.5,Cor3.6,Lemma3.7,4.6; finite Cech descent','12:67','Functorial finite alternating compact-support Cech chain totalization is cover-independent by refinement. The exact j! simplex resolution computes the dual Ext totalization. Real modifications glue termwise; no nonseparated compactification is assumed.'),
('B.5-Tate','Rational duality all Tate twists on number rings and curves','PROVED','thm:B-rational-duality','FM3.12,3.22; Lichtenbaum5.4,6.1; Geisser9.5','12:67;15:174','Open number-ring complex specified by localization and compact support; arbitrary M remains separate.'),
('B.5-Artin-Tate','Rational duality for every finite-monodromy Tate coefficient','PROVED','cor:B-Artin-Tate-duality','Finite etale Galois descent; all-Tate duality; Maschke','12:67','Finite cover, invariant projector, restriction/corestriction for local conditions, and averaged perfect evaluation give all twists on number rings and proper finite-field curves.'),
('B.5-general-gate','General number-ring dual completion iff prescribed c0/c1 realizations for the dual pair','PROVED EXACT EQUIVALENCE; REALIZATION CONJECTURAL','prop:B-general-rational-gate','Fontaine6.5-6.7; Poitou-Tate','12:67','Direct-sum dual completion is sufficient and necessity is its degree0/1 comparison. No six-operation motivic category or canonical higher comparison is silently asserted.'),
('Lead B1','Finite Weil-etale identification and arithmetic finite-condition correction','PARTIAL; FULL LEAD UNRESOLVED','B.1-B.2','B.1-gate; B.2-Hf1','12:60-80','Factor n proved; Tate+semisimplicity alone missing Beilinson; BK correction degree1 precise.'),
('Lead B2','Degree3 fundamental class, dual Borel lines, trivial-zero shape','PROVED WITH ARCHIMEDEAN COMPLETION','B.4-B.5','FM3.12,3.22,5.8.3','15:174','Duality Q(1)[3] valid for specified compactified theory, not ordinary motivic cohomology.'),
('R5-audit','Inherited point/tables/localization claims','CORRECTED','B.1;B.4','Opened primary sources and transcriptions','15:172-178','Integral two-primary omissions; ordinary-motivic versus Weil-etale distinction; negative finite-field notation repaired.'),
('R6-audit','Inherited arithmetic comparison and boxed finiteness claims','CORRECTED AND PROVED IN STATED SCOPES','B.1-B.3','Primary reproof and certified descent','12:63-80','Q0 fixed-base counterexample is not the varying X[1/ell] task; the latter is refuted with Q1 S-units. Regular-base finite-field comparison repaired; degree2 nonzero example computed; missing Beilinson remains.')
]
with (ROOT/'part_b_results.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']);w.writerows(rows)
with event_path.open('w',newline='') as f:
 w=PreservingEventWriter(f);w.writerow(['statement_id','date','who','type','outcome'])
 for r in rows:
  kind='refuted, with corrected statement in same section' if r[2].startswith('REFUTED') else ('targeted proof check' if 'UNRESOLVED' in r[2] or 'CONJECTURAL' in r[2] else 'used and rechecked in this run')
  w.writerow([r[0],STAMP,WHO,kind,r[2]+': '+r[6]])
 w.writerow(['B.3-X011',STAMP,WHO,'computation or formal certificate','PARI2.19.1 unconditional ellrank [0,0,0,[]], torsion5; code/x011.gp and output/x011.txt.'])
 w.writerow(['B.3-rank',STAMP,WHO,'computation or formal certificate','PARI2.19.1 unconditional ellrank [2,2,0,...] for conductor389 curve; same code/output.'])
 w.writerow(['B.3-divisor-split',STAMP,'GPT-6 Astra agent /root/part_c','independent proof check','Confirmed boundary kernel lies in NS; distinct weights split; proper generically finite trace preserves divisor classes; e1 r e1 retracts geometric Kummer once e1N=M is proved; cofiniteness retained.'])
 w.writerow(['B.3-all-bases',STAMP,WHO,'independent proof check','Read full root sections/b3_singular.tex. Checked reduced equalizer injection, finite-free quotient via LangNeron, Pruefer torsion completion, finite-image Galois action and Maschke, nilpotent p-primary invariance, arithmetic norms, weight-minus1 H0, and cofinite torsion comparison. No functorial hypercover retractions or proper section descent assumed.'])
 w.writerow(['B.3-relative-curve',STAMP,'GPT-6 Astra agent /root/part_c','independent proof check','Full section-free proof checked: Cartier degree-d class, Deligne2.4, d-torsion Brauer obstruction via restriction/corestriction, middle Chern image equals Kummer image, cofiniteness, and integral section-case edge. Use separable generic point explicitly.'])
 w.writerow(['B.4-odd-algorithm',STAMP,WHO,'independent proof check','Root algorithm checked against Soule2003: prime bound, local different bound, Minkowski polynomial enumeration, finite mapping-cone cocycle presentation, AVdual and equal-successive-orders termination.'])
 w.writerow(['B.4-rational-generators',STAMP,'GPT-6 Astra agents /root and /root/part_d','independent proof checks','Both independent audits passed. D note part_d/b4_generator_third_audit.md; exact real-proper predicate, actual coefficient denominators, Beilinson regulator normalization, index formula, integer-coefficient Q-cycle localization, and exponent-two saturation certificate checked.'])
 w.writerow(['B.4-KerrYang-error',STAMP,WHO,'computation or formal certificate','code/source_and_graph_checks.py and output/source_and_graph_checks.txt: symbolic u=sv degeneracy at n4,5,6; Keller blowup charts and F2 fibres; naive epsilon regulator diagnostic explicitly not used as standalone disproof.'])
 w.writerow(['B.4-Vandiver37',STAMP,WHO,'computation or formal certificate','PARI2.19.1 bnfcertify(B,1)=1 and B.clgp=[1,[]]. Actual class group is quotient of trivial group. Full-unit-certification run interrupted as unnecessary; uncertified partial output retained and not used.'])
 w.writerow(['B.3-H2-example',STAMP,WHO,'computation or formal certificate','Point count5 overF2, trace-2, companion matrix centralizer dimension2 overQ3. code/finite_field_checks.py and output/finite_field_checks.txt.'])
 w.writerow(['B.3-singular-degree',STAMP,'GPT-6 Astra agent /root/part_d','independent proof check','Closed-immersion scheme pushout exists by Stacks0B7M; smoothness by0CYY(4); strict-local smooth lifting proves torsor triviality; End(E) injects into H1; Pic^d has class plus/minus d alpha. No Brauer infinitude inferred.'])
 w.writerow(['B.3-singular-degree',STAMP,WHO,'computation or formal certificate','code/singular_genus_one_checks.py and output/singular_genus_one_checks.txt: gradient ideal Groebner basis x2,y2,z2; all5 projectiveF2 points; exact fibre-product multiplication identity.'])
 w.writerow(['B.2-higher',STAMP,'GPT-6 Astra agent /root','independent proof check','All Tate twists and degrees pass; added local dual-cone calculation and the two exact degree2 sequences. Fontaine source yields a vector-space identification after splitting, not an automatic canonical derived comparison; that scope is explicit.'])
 w.writerow(['B.5-finite',STAMP,WHO,'targeted source and proof check','Reopened GS4.6, Lemma3.7 and Thm3.9. Global base Q allows every finite primary coefficient, including vertical p; the derived Z/m shift gives2d+1. Milne logarithmic-Witt curve example checks characteristic-primary and p2 boundary.'])
 w.writerow(['B.5-nonseparated',STAMP,'GPT-6 Astra agent /root/part_d','independent proof check','Read written proposition and exact GS3.5,Cor3.6,Lemma3.7,4.6. Confirmed qc separated intersections, chain degree minusr versus dual Cech plusr, simplex resolution, cycle-complex open restriction, finite real Tate totalization, and refinement independence. Added functorial cochain models to make diagrams and cones precise.'])

label_map={
 'prop:B-e':'B.1-point',
 'thm:B-Geisser-gate':'B.1-gate',
 'prop:B-continuity':'B.1-closure',
 'thm:B-abelian-type':'B.1-abelian-type',
 'prop:B-phantom-gate':'B.1-phantom',
 'thm:B-full-tate':'B.2-full',
 'prop:B-Hf-tate':'B.2-Hf1',
 'cor:B-Hf-all-degrees':'B.2-higher',
 'thm:B-Sha-corank':'B.3-corank',
 'ex:B-X011':'B.3-X011',
 'prop:B-Brauer-arithmetic':'B.3-Brauer-arithmetic',
 'lem:B-divisor-splitting':'B.3-divisor-split',
 'prop:B-finite-chain-proper':'B.3-finite-chain',
 'prop:B-relative-curve':'B.3-relative-curve',
 'rem:B-Keller-closure-error':'B.3-Keller-error',
 'lem:B-sections-reduced':'B.3-sections-completion',
 'thm:B-finite-chain-all-bases':'B.3-all-bases',
 'ex:B-singular-infinite-period':'B.3-singular-degree',
 'ex:B-H2-constant':'B.3-H2-example',
 'thm:B-SpecZ-Q':'B.4-rational',
 'prop:B-integral-errors':'B.4-integral01',
 'prop:B-integral-structure':'B.4-structure',
 'prop:B-two-primary':'B.4-2primary',
 'thm:B-effective-odd-torsion':'B.4-odd-algorithm',
 'thm:B-primitive-generator':'B.4-rational-generators',
 'lem:B-KY-degenerate':'B.4-KerrYang-error',
 'prop:B-Vandiver':'B.4-Vandiver',
 'ex:B-Vandiver37':'B.4-Vandiver37',
 'thm:B-finite-duality':'B.5-finite',
 'prop:B-finite-duality-nonsep':'B.5-nonseparated',
 'thm:B-rational-duality':'B.5-Tate',
 'cor:B-Artin-Tate-duality':'B.5-Artin-Tate',
 'prop:B-general-rational-gate':'B.5-general-gate'
}
with event_path.open(newline='') as f:
 prior_events=list(csv.DictReader(f,delimiter='\t'))
with (ROOT/'part_b_LABEL_CHECKS.tsv').open('w',newline='') as f, event_path.open('a',newline='') as g:
 cross=csv.writer(f,delimiter='\t');alias=csv.writer(g,delimiter='\t')
 cross.writerow(['statement_label','original_statement_id','original_date','who','type','outcome','mapping_note'])
 for label,original in label_map.items():
  matching=[e for e in prior_events if e['statement_id']==original]
  if not matching: raise ValueError('No original event for '+label)
  for e in matching:
   note='Crosswalk only; original check date and type retained; no new recheck asserted.'
   cross.writerow([label,original,e['date'],e['who'],e['type'],e['outcome'],note])
   alias.writerow([label,e['date'],e['who'],e['type'],
                   'Cross-reference to original event '+original+' (not a new check): '+e['outcome']])

sources=[
('Conrad2006','opened personally and audited','https://math.stanford.edu/~conrad/papers/Kktrace.pdf','Theorems2.1,7.1','LangNeron and trace for arbitrary finite-type-base section completion'),
('deJong1996','opened personally and audited','https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf','Theorem4.1;Remark4.2','Smooth alteration cover after finite affine cover of arbitrary finite-type base'),
('Fontaine1992','opened author PDF and rendered formulas','https://www.imo.universite-paris-saclay.fr/~fontaine/bourbakiblochkato.pdf','Sections4.4-4.5,6.5-6.7;pp214-216,221-223','Local/global finite complexes and precise c0/c1 f-admissibility precursor to joint FPR; no claim later full article obtained'),
('GeisserDedekind2004','opened','https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf','Theorems1.2(2),3.2','Integral motivic-etale comparison and higher-Chow localization for primitive generator search'),
('Voevodsky2011','opened','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Voe-mot.pdf','Theorems6.16-6.18;pp436-437','Norm-residue theorem removes conditional hypothesis in Geisser comparison'),
('StacksClosedPushout','opened','https://stacks.math.columbia.edu/tag/0B7M','Lemma37.67.8','Genus-one torsor scheme exists by gluing two closed immersions'),
('StacksPushoutMorphisms','opened','https://stacks.math.columbia.edu/tag/0CYY','Lemma37.67.9(4)','Smoothness of the genus-one scheme over the base pushout'),
('StacksSmoothLift','opened','https://stacks.math.columbia.edu/tag/0H74','Lemma15.13.3','Smooth sections lift across henselian pairs'),
('Ferrand2003','opened auxiliary source','https://www.numdam.org/item/BSMF_2003__131_4_553_0.pdf','Sections5.4,6;Theorem7.1(iii)','Pinching and proper nonprojective examples; final proof uses direct Stacks closed-immersion lemmas instead'),
('Bhatt2014','opened auxiliary primary preprint','https://arxiv.org/pdf/1404.7483v1','Examples4.12-4.13','Characteristic-zero infinite-order torsor and Gm cohomology examples motivated singular-base search; not used as proof over a finite field'),
('Kahn2003','opened','https://www.numdam.org/item/ASENS_2003_4_36_6_977_0.pdf','Def1;Thms1.4,1.10,3.6,5.1-5.2;Prop1.5;Lemma1.9;Cor2.2,3.8','Full abelian-type comparison; exact phantom-motive equivalence under strong Tate'),
('vanHoftenSempliner2026','opened','https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf','TheoremI;Section1.1.3','External current theorem, not claimed independently proved in this research; implies all-abelian Tate through Milne7.1'),
('Milne1999','opened','https://www.jmilne.org/math/articles/1999bP.pdf','Theorem7.1','CM Hodge implies all-abelian finite-field Tate'),
('Geisser2004','opened','https://arxiv.org/pdf/math/0404425','7.1;8.4;9.3;9.5;Conj8.3','Missing Beilinson gate and finite-field values'),
('Lichtenbaum2005','opened','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E70A59FA79C01CDBCD940699A72A6F59/S0010437X04001150a.pdf/the-weil-etale-topology-on-schemes-over-finite-fields.pdf','5.4;6.1','Curve integral/rational duality'),
('Lichtenbaum2009','opened','https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n2-p05-p.pdf','5.11;6.3;introduction','Higher-degree issue precludes blind identification with FM theory'),
('FlachMorin2018','opened','https://ems.press/content/serial-article-files/26429?nt=1','Cor3.12;Thm3.22;Section5.8.3','All rational and structural integral number-ring groups'),
('BlochKato1990','opened','https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf','Prop3.8;Examples3.9,3.11;Def5.1;Conj5.3;Prop5.4','f/g local distinction and Sha equivalence'),
('FontainePerrinRiou','not obtained','https://www.imo.universite-paris-saclay.fr/~bernadette.perrin-riou/bpr-rech/liste-publi.html','Expected III.3.1.4; not cited as opened','Exact-title searches plus both author publication pages; BK original provides the local definition actually used'),
('MilneADT2006','opened','https://www.jmilne.org/math/Books/ADTnot.pdf','I4.10,I6;II2.1,2.2(a),3.1,7.6,7.7,7.11','Poitou-Tate; real places; Brauer support; finite duality'),
('MilneAddendum2025','opened','https://www.jmilne.org/math/Books/add/ADT2006.pdf','p1','Regular flat extension references GS'),
('Borel1974','opened','https://www.numdam.org/article/ASENS_1974_4_7_2_235_0.pdf','Prop12.2','Rational K ranks'),
('Nickel2022','opened','https://link.springer.com/article/10.1007/s00029-021-00717-3','Thm3.2;Lemma3.4;Conj3.5;Remarks3.7-3.10;Lemma3.11','Precise Schneider comparison; original source not obtained'),
('Schneider1979','not obtained','Original cited in Nickel2022 bibliography','Uber gewisse Galoiscohomologiegruppen, Math.Z.168,181-205','Original not downloaded; use explicit opened Nickel formulation'),
('RognesWeibel2000','opened','https://sites.math.rutgers.edu/~weibel/archive/papers-dir/RognesWeibel.pdf','0.4;0.6;Lemma5.5;Props6.12-6.13','Direct computation of ordinary motivic C_m[2infinity] and its generator; K-theory real corrections kept separate'),
('Kurihara1992','opened','https://www.numdam.org/item/CM_1992__81_2_223_0.pdf','Lemma1.2;Cor1.5;Prop2.1','Vandiver eigenspace equivalence'),
('Scholbach-fcohomology','opened','https://arxiv.org/pdf/1003.1219','Remark6.2;Thm6.8,6.11,6.13','Crystalline condition omitted; t-structure axioms conditional'),
('Scholbach-specialL','opened supplied TeX and published PDF','https://jakobscholbach.github.io/reprints/Special%20L-values%20of%20geometric%20motives.pdf','Axiom1.6;Conj1.10,4.1;Thms4.5,4.8; supplied labels motcomp,numrat','Arakelov pairing retains numerical=rational and Beilinson-Parshin gates; published2017metadata verified'),
('AdrienMorin-constructible','opened supplied TeX and arXivv1','https://arxiv.org/pdf/2411.07896','TheoremA;Thm2.8;Thm8.3;supplied label thm:main;n<=0','Constructible integral sheaves and negative twists do not replace arbitrary positive motivic complexes'),
('GeisserSchmidt2018','opened','https://www.mathi.uni-heidelberg.de/~schmidt/papers/poitou-highdim.pdf','Lemma3.7;Thm3.9;Thm4.6;eq2.12-2.13','All finite duality with exact coefficient shifts'),
('GonzalezAvilesTan2007','opened arXiv; publisher PDF not obtained','https://arxiv.org/pdf/math/0608587','MainTheorem;eq6','Unconditional pro-Selmer Cassels-Tate sequence; publisher download403'),
('Keller2019','opened','https://ems.press/content/serial-article-files/26477?nt=1','Thm2.7.19;Remark2.7.20(d)','Higher-dimensional proper-base BSD equivalence'),
('Keller2016','opened','https://www.timo-keller.de/articles/TateShafarevich.pdf','Thm2.14;Cor2.16;Section4.2','Relative Jacobian/Brauer; caution Lemma2.17 finite-multisection argument not used'),
('Keller2021','opened','https://www.timo-keller.de/articles/Shap.pdf','Cor2.5;Thm3.14;Thm4.1;Thms5.3,5.5','Purity and alteration descent, p-primary qualifications'),
('Qin2024','opened','https://link.springer.com/content/pdf/10.1007/s00209-024-03487-8.pdf','Prop2.4-2.5;Lemma2.6;Thm1.1','Curve-base arithmetic/geometric Sha comparison'),
('Yuan2020','opened','https://arxiv.org/pdf/2011.12897','Thms1.2,1.3;Lemma3.1','Proper arithmetic/geometric Brauer comparison and splitting'),
('BalkanSchreieder2026','opened','https://link.springer.com/content/pdf/10.1007/s00029-026-01142-0.pdf','Lemma2.2;Lemma3.11;Prop4.10-4.11;Thms1.1-1.2','Open divisor splitting and separate finite-field conjectural gates'),
('Tate1966','opened','https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf','MainTheorem Section1;Lemma1;Thm1(a)','Constant abelian-scheme finiteness and centralizer example'),
('Deligne1968','opened','https://www.numdam.org/item/PMIHES_1968__35__107_0.pdf','Thm1.5;Remark1.10;Prop2.4 and(2.5),pp111-112','Section-free relative-curve Leray splitting'),
('KerrYang2018','opened','https://msp.org/akt/2018/3-2/akt-v3-n2-p01-p.pdf','Thms3.3,3.8;Remark3.4;Sections4C-D audited','Existence and regulator are used; explicit Section4 formula has degeneracy defect, independently checked against KerrLi2020; no unverified integral cycles used'),
('KerrLi2020','opened publisher PDF and arXiv','https://msp.org/pjm/2020/306-2/pjm-v306-n2-p06-p.pdf','p548 and footnote10;Theorem5.3;Proposition5.2','Published correction: KY first K7 cycle not closed; integral regulator and corrected low-weight cycles'),
('Basu2014','opened','https://www.math.purdue.edu/~sbasu/raag_survey2011_final-sep4-2014.pdf','Theorem2.1;Section2.1.2','CAD and effective semialgebraic tests; original BPR book links failed503; no algorithm complexity claim'),
('Seidenberg1974','opened','https://scispace.com/pdf/constructions-in-algebra-3zcc352k1e.pdf','numbered statements5,6,36,46','Effective ideal operations over Q; official AMS endpoint403; primary mirror opened'),
('Collins1975','opened','https://link.springer.com/content/pdf/10.1007/3-540-07407-4_17.pdf','Section3;Theorem8;DECOMP;ELIM','Exact semialgebraic dimension and real-proper tests'),
('BesserDeJeu2003','opened','https://www.numdam.org/article/ASENS_2003_4_36_6_867_0.pdf','Thm1.12;Remark1.13;intro pp868-869','Auxiliary cyclotomic rational-generator check; no conjecture required for number fields'),
('Sakugawa2021','opened','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B08F41641AF6FEE54CED590D02D5288B/S0008414X20000073a.pdf/generalized-beilinson-elements-and-generalized-soule-characters.pdf','Thm1.1;MainTheorem','Beilinson rational cyclotomic element and its Soulé-character realization'),
('PARI-bnfcertify2026','opened','https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html','bnfcertify documentation, flag1','Certifies actual class group is quotient of computed group; sufficient for trivial computed classgroup'),
('Chen-et-al2026','opened','https://arxiv.org/pdf/2602.05090','Thm1.1;partial Vandiver corollary','Partial regularity density-one theorem is not full Vandiver'),
('Elkies2021','opened','https://people.math.harvard.edu/~elkies/M263.21/index.html','October13 lecture','Explicit X0(11) model'),
('PARI2026','opened','https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html','ellrank documentation','Certified algebraic rank bounds, no analytic/BSD inference')]
with (ROOT/'part_b_LITERATURE_CHECK.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['source','status','url_or_path','exact_locator','use_or_attempt']);w.writerows(sources)
with (ROOT/'part_b_ITEM_STATUS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['item','status','current_gate','next_attack'])
 for item in ['B.1','B.2','B.3','B.4','B.5','Lead B1','Lead B2']:
  r=next(r for r in rows if r[0]==item);w.writerow([item,r[2],r[6],{'B.1':'Attack the exact numerical-Chow-phantom obstruction; all abelian-type cases are already established.','B.2':'All Tate calculations and local-complex audit complete; attack the prescribed general motivic c0/c1 realization and its independent finite-field phantom gate.','B.3':'All-base chain now proved; investigate exact general nonconstant finiteness/Tate-BSD gate without claiming its truth.','B.4':'Proved as an effective presentation and primitive-cycle construction; no efficiency or uniform Vandiver vanishing assertion.','B.5':'Attack prescribed general motivic f-admissibility for dual pairs; retain the distinction between graded dual completion and a full absolute category.'}.get(item,'Integrate proved component statements; retain unresolved scope.')])
print('Wrote',len(rows),'statement rows and',len(sources),'source rows at',STAMP)
