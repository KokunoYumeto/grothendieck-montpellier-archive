"""Serialize manually assessed literature-search families and literal tool trails."""
from pathlib import Path
import json,csv,re
B=Path('/workspace/scratch/7feb9690b71f/SA08_work');P=B/'work/late'
claims=json.loads((P/'claims.json').read_text())
families=[]
def S(n,subject,raw,opened,match,boundary,result):
 sid=f'L{n:02}'
 families.append(dict(search_id=sid,date='2026-11-19',claims=';'.join(c['id'] for c in claims if sid in c['searches']),subject=subject,raw_logs=';'.join(f'research/late_web_{i:03}.json' for i in raw),opened_sources=opened,hypothesis_match=match,excluded_inference=boundary,outcome=result))
S(1,'Filtered integral de Rham comparison and weighted cup products',[4,7,8,9,23,25,29,30,31],
 'Cartan1976 originalpp267–271 in work/reference_pdfs/invent35.pdf; Garvin1998 entirepp169–176 in work/late/Garvin1998.pdf; Cenkl1989§5pp31–32.',
 'CartanTh3 requires flat cycles; §6 weakens one extension axiom and retains multiplicativity conditions. §7 gives weight r versus degree n, binomial product and gcd1 recovery. GarvinTh4.1–4.2 covers arbitrary simplicial sets with strict p<q; Remark3.3 refutes(q+1)-extendability.',
 'Neither theorem alone proves the arbitrary completed coefficient setting or the manuscript inclusive endpoint. Cenkl obstruction uses its explicit axioms; diagram/E-infinity models are outside a blanket no-go reading.',
 'Exact weighted developments identified. Lecture12Dec1975, CartanDec1976, Miller preprint known by proof stage and1978 publication, Garvin1998. Early initial403 records superseded by full successful Garvin download. A final quadratic audit corrects C205: Gamma²(Psi) is k --2→ k, not ordinary K(k,2); overQ it is acyclic. BMT2016Prop3.5/Cor3.6p270 opened and matched to this derived nonlinear context.')
S(2,'p-adic PD tail ideals and Legendre minima',[17,23],
 'Stacks07GK Example23.2.3 and ordinary PD axioms; supplied239–241 read fully.',
 'The source confirms canonical gamma_n(pa)=p^na^n/n!, integrality and ordinary PD structure. Legendre summation, p=2 stabilization, odd-prime cofinality and the zero graded piece are independently computed in proofs§1.',
 'A cofinal filtration is not the same as a free associated graded. The exact tail-minimum formula was not identified as a named later theorem.',
 'Standard PD input verified; exact local arithmetic settled by symbolic proof plus saved finite audit. Search nonidentification is not a priority claim.')
S(3,'Odd extension, coefficient change and cohomological PD descent',[2,5,6,9,14,23,24,26,28],
 'Stacks07GK,07H1,09PFDef23.6.5 and following warning; Richter2009Def7.4,Th7.5pp249–251; Roby1968pp99,105–108; Cartan1976§7.',
 'Ordinary PD axioms and flat base-change existence are explicit. Differential compatibility alone does not imply powers of boundaries are boundaries. Richter includes that extra condition in the chain setting.',
 'The CP² obstruction applies only if powers descend to the whole positive even integral cohomology ideal. It does not refute operations restricted to coefficient ideals or weights. Cancelled coefficient maps need continuity separately.',
 'Exact descent boundary identified. Cancelled odd-extension residuals and the coefficient scalar relation independently checked; no general extension theorem assigned.')
S(4,'Finite truncation adjunctions and C-valued right Kan extension',[2,3,4,6,7,8,27],
 'Kelly1982/2005§4.13,Th4.50pp60–67; Stacks015Z,07D8; source finite-adjoint propositions.',
 'The small preadditive category of degrees turns restriction into the stated Kan extensions. Complete abelian targets supply cotensors/ends from products and kernels. Exact inclusion implies its right adjoint preserves injectives.',
 'Ordinary Kan extension does not settle the differential/derived enhancement on295; an opposite category also reverses grading/action conventions. Left adjoints need not be left exact.',
 'Exact ordinary categorical mechanism verified; finite adjoints re-proved directly and q counterexample checked. Differential and variance ambiguities retained.')
S(5,'One-generator PD tail rigidity, exact coefficient adjoint and negative degrees',[1,3,7,10,11,12,17,19,20,21],
 'Kelly adjunction formalism; Roby1963 metadata and SGA4XVII5.5.2.3–8 originalpp374–375; Gabriel1962 source metadata; Ekedahl2002, Horel2024 and Toën2020 exact bounded comparisons.',
 'The nonnegative and negative coefficient presentations were checked directly. Prime-local cofinal rows ell^r−1 prove exact L over arbitrary k. The negative representing group is Q, yielding Hom_Z(Q,M).',
 'Later numerical/binomial/affine models do not state the same cutoff formula. Hom_Z(Q,M) is not M tensor Q and evaluation at1 need not be injective.',
 'No exact later printed cutoff theorem identified in these recorded searches. Existing manuscript tail/Ext assertion is nevertheless proved in the memo and independently peer-checked. No novelty or current-open claim follows from this bibliographic limit.')
S(6,'Negligible classes, Gabriel localization and section at infinity',[1,2,4,6,7,17],
 'Gabriel1962 Numdam metadata; Stacks02MN definition andLemma12.10.6; actual256–259 and early26–27 source passages.',
 'Serre exact quotient requires extension closure; a Grothendieck localization additionally requires the specified localizing class. The elementwise-tail class fails extension closure over Gamma_Fp. Localizing Serre closure of bounded nonnegative modules gives a repaired recovery statement.',
 'The replacement class is not identified with the manuscript class, and the filtered-colimit formula for the section functor is not established by the abstract localization theorem.',
 'Literal class obstruction independently proved. Exact repaired quotient theorem established in proof§7; intended infinite quotient and finiteness/cofinality assumptions remain to be specified.')
S(7,'Derived composition and induced-target Ext vanishing',[2,4,17],
 'Stacks015M derived-composition acyclicity criterion and015Z exact-left-adjoint/injective lemma; manuscript261–273.',
 'The abstract equality phi tau i=i does not imply Rphi tau i=i. The triangular-category counterexample preserves the additional exact right kappa condition. For Gamma tails, exact L supplies the missing injective preservation and verifies the special assertion.',
 'Underived full faithfulness and cohomology-object acyclicity do not alone compute a derived section. The infinite localization still needs its own precise category.',
 'General formal inference refuted; exact finite special case repaired and re-proved over arbitrary coefficients, with independent parent/early checks. This is verification of an existing assertion, not a new research direction.')
S(8,'Multiplicative recovery, tensor/internal Hom and the T diagram',[5,6,9,10,11,12,14,19,20,21,25],
 'Richter2009Th7.1; Schwede–Shipley2003IntroTh1.1; Richter–Sagave2020Th1.1; Mandell2006 exact theorem checked by parent; Horel/Ekedahl/Toën primary theorems.',
 'These establish specified transported tensors, algebra-model equivalences or structured homotopy reconstructions. The weighted product compatibility in Cartan has binomial factors and cofinal-weight recovery.',
 'None supplies the missing monoidal quotient for an undefined C_infty or determines the untyped T-diagram on277. Faithfulness is not fullness; ordinary chain equivalence is not an enriched diagonal equivalence.',
 'Precise bounded analogues identified. The local multiplicative recovery remains a formulation/coherence problem; the T-arrow itself is not identifiable enough for a unique fate theorem.')
S(9,'Coalgebra duality, cotensor, completion and descending intersections',[1,3,4,7,10,11,17],
 'Roby/SGA4 divided-power structure inputs; MathOverflow100323 and239815 opened only as terminology/search leads; Kelly end formalism; manuscript279–285.',
 'The cofree cotensor identity follows directly from counit and coaction without flatness. The flat primitive coalgebra Z⊕Q and P_i=2^iZ show failure of unrestricted tensor/intersection exchange. Unbounded denominators show failure of ordinary tensor/product exchange.',
 'MO discussions are not cited as exact theorems proving these identities. The counterexample is to the proposed general interchange principle, not a proof that every particular recursive V(s) construction fails.',
 'Elementary boundaries re-proved. No exact later theorem identified for the under-specified completed exponential or recursion. Topology, continuity and the ambient coalgebra category remain undefined.')
S(10,'Yoneda, free presheaf cocompletion, abelianization and operation categories',[1,2,3,4,6,7,8,9,19,27,30,31,32],
 'Kelly1982/2005Th4.50–4.51pp67–68 andTh5.35pp99–100; Stacks019G; manuscript302–318.',
 'For a small indexing category, a cocomplete target admits the usual category-of-elements extension. Ab-enriched cocompletion is the corresponding additive statement. Selected small colimit shapes give Kelly free F-cocompletion.',
 'The arbitrary-topos expectation needs a chosen class of functors and sheafification/exactness conditions. Yoneda on all modules does not introduce algebraic biduals. Undefined L and variance prevent a unique operations equivalence.',
 'Exact categorical theorems identified; standard universal properties independently rechecked. Explicit raw representable invariant example confirms that homotopy localization is a separate step. Touzé2026 introductionpp1–5 was read after the author bibliography led to it: Lemma3/Th5/Th9 concern exact strong tensor functors over a field and specified admissible targets, not the unspecified arbitrary-ring operation category.')
S(11,'Dold–Kan, signs, native tensor and transported nonlinear operations',[4,5,6,9,10,19,20,25,29,30,31],
 'Stacks019G full abelian Dold–Kan proof; Ekedahl2002§1p2 Karoubian version; Richter2009§7; Schwede–Shipley2003IntroTh1.1.',
 'Additive idempotent splittings and finite sums give normalization/denormalization. Richter transports a symmetric monoidal product, while the native levelwise tensor is only chain-equivalent to the usual tensor. Bicomplex totalization requires the Koszul sign.',
 'Ordinary symmetric/exterior/PD functors are not automatically derived functors, and native strict commutative integral dgas are not the same category as simplicial commutative algebras.',
 'Exact standard theorem and later refinements identified. Rank and sign counterexamples saved. BMT2016Prop3.5/Cor3.6p270, the rational odd-shift exterior result, verifies the framework for the new C205 quadratic alarm. No conjectural global PD homotopy classification is inferred.')
S(12,'Natural power operations and enriched homotopy comparison',[3,5,6,10,11,12,14,19,20,21,30,31,32],
 'Kelly Yoneda; SGA4XVII5.5.2.3–8; Roby1968; Richter–Sagave2020; Ekedahl/Horel/Toën exact theorems; Mandell2006 checked by parent.',
 'Nat(Hom(A,-),Hom(A,Gamma^p(-))) corresponds to A→Gamma^pA as set-valued natural transformations. Product/additivity/iteration translate to separate diagrams; full naturality across all modules is stronger than a fixed-object relation.',
 'Additivity in f is not built into ordinary set-valued Yoneda. Later E-infinity, binomial and affine reconstructions use additional operations and restricted spaces; they do not certify the incomplete list on325.',
 'Universal translation verified; exact equivalence of all partially written conditions remains unidentifiable without the missing types. Bare chain-homotopy data cannot recover cup products, checked independently. Touzé2026Lemma3 andTh5 provide a contemporary bounded uniqueness/existence comparison, requiring exact strong tensor functors over a field; the manuscript Hom-convolution functor is generally only lax and does not automatically meet those assumptions.')
S(13,'Convolution divided powers: flat positive result and nonflat/uniqueness limits',[1,3,4,7,10,11,12,13,14,15,16,18,19,20],
 'SGA4III originalXVII5.5.2.3–8pp374–375; Lundkvist2007/2008Prop2.2p4; Roby1968Prop1p99,Th5p107; Stacks07H1 and07GK.',
 'For flat A, Gamma^n A≅(A^tensor n)^Sigma_n and Gamma^qA is flat. The iterated coproduct therefore lifts canonically; the proof verifies addition, scalar, product and iteration through flat A/Gamma^qA only. J need not be flat.',
 'The assembled Hom-convolution theorem was not found verbatim. Nonflat A can admit no PD structure on the convolution ideal. The F2 uniqueness alternative satisfies positive-index composition and products only; it fails q=0 augmentation and full additive naturality.',
 'Flat sufficient-hypothesis theorem proved as a reconstruction. Nonflat obstruction checked exhaustively and symbolically. Restricted uniqueness counterexample bounded exactly; no unconditional rejection or novelty claim.')
S(14,'Projective structures, connection obstruction and curve normalization',[1,2,3,4,5,6,8,9,12,13,14,15,16],
 'Biswas–Hurtubise–Roubtsov2021Lemma2.2,Prop2.4,Cor2.6pp6–8; Dumas2009§2p7,§§3.2–3.3pp10–12. Atiyah1957 metadata found but originalPDF access failed.',
 'The nonsplit jet bundle with theta characteristic is a precise modern comparison. Uniformization gives the analytic Fuchsian section. A holomorphic projective connection on the literal split nonzero-degree bundle would induce a forbidden degree-zero line connection.',
 'Atiyah original theorem is not claimed read. The independent degree proof is recorded. Smooth/topological splitting is not holomorphic splitting; pointing and centered-disc conventions are needed for the uniqueness claim; SL2R covers PSL2R, not every real PGL2 component.',
 'Conditional obstruction and normalization corrections checked. The meaning of Omega, properness, plus sign and group notation remain ink questions; no modern bundle is substituted into the transcription.')
S(15,'SGA7 analytic/formal algebraization and lattice comparison',[17,18,22,23,24,26],
 'OriginalSGA7IXpp500–506(PDF505–511); Artin1969publisherpreviewIntropp21–23,Th1.6–1.7pp25–26; RaynaudBourbaki363pp279–295.',
 'Exact donor matches are read. Effective formal versal algebraization has a locally finite-presentation functor and the stated excellent/base assumptions. Relative GAGA supplies full faithfulness separately from existence.',
 'Broad questions on general proper analytic spaces in13.5.3 are not answered merely by citing Artin by title. Algebraic spaces and schemes are distinct conclusions.',
 'Exact donor-to-publication links identified. A complete later resolution of every broad13.5.3 question was not found in this bounded search; this is an identification limit, not evidence of novelty.')
S(16,'SGA7 p-divisible, abelian-part, extension and pairing claims',[17,18,22,23,26,27],
 'OriginalSGA7IXpp394,398–399,412,417–426,445; Levin p-DivisibleGroupsPartIITh1.2p3; originalTate1967URLattempts failed.',
 'Exact source statements and historical coefficient restrictions are retained. Levin states Tate full faithfulness for an integrally closed Noetherian domain with characteristic-zero fraction field; completeDVR is a reduction, not the full theorem.',
 'Tate does not remove semistability or equal-characteristic restrictions in unrelated steps. Pairing denominators depend on ramification normalization. Deferred torsor compatibility is not certified by reading the displayed diagram.',
 'Exact SGA7 donor fates identified, including scan262Prop7.5 omitted as a separate notes heading. OriginalTate access stays unverified; the modern lecture theorem and source dependency are separately checked.')
S(17,'Formal abelian quotient algebraization and ample descent',[17,18,22,23,24],
 'OriginalSGA7IX7.1.3–7.1.6pp400–402;13.5.3p503; Artin1969preview and Raynaud1969/1971.',
 'Normality and compatible polarization/quasi-projectivity enter the published formal quotient argument. The remark removing normality explicitly points forward. A doubled/symmetric biextension supplies the published workaround for direct ample descent.',
 'EGAIII5.4.1 and SGA3VIA3.2 are source dependencies, not separately re-proved or newly read here. General direct descent of an arbitrary chosen ample bundle is stronger.',
 'Published theorem and internal resolution matched exactly. Stronger direct-descent fate not identified; its unnecessary use in the source argument is avoided.')
S(18,'Semistable reduction, inertia criterion and original printed tensions',[17,18,22],
 'OriginalSGA7IX3.5pp350–351,3.6pp351–352,Cor3.8p353; originalimagesPDF355–358 inspected.',
 'The semistable-reduction/inertia setting and valuation assumptions are those of the published chapter. Statement/proof endpoints expose the V versus Vperp inclusion tension and the mislabeled implication.',
 'These tensions also occur in the original publication; they must not be called merely AI transcription mistakes. Reading a source criterion is not a new full proof of semistable reduction.',
 'Exact own-publication fate A under donor chronology; consistency alarms retained for source comparison. No manuscript ink changed.')
S(19,'Picard representability and formal smoothness',[11,12,13,23,24],
 'OriginalSGA7IX12.8.3p478; Stacks0D24Prop99.11.8; Artin1969intro and RaynaudBourbaki applications.',
 'Flat proper finitely presented X/B and universal O_T≅f_*O give the Picard algebraic space. Curve H² vanishing concerns smoothness, not representability itself.',
 'A smoothness proof alone does not establish existence of a representing scheme. Historical Mumford–Raynaud/Artin admission remains a separate source statement.',
 'A precise modern theorem with matched hypotheses is verified; the stronger unconditional scheme claim is not assigned.')
S(20,'Reused Dirichlet, periodic and geometric-series exercises',[22,23,25,26],
 'Gressman primarylectureURL located via search excerpt but403 onopen; guessed UCDavis route failed. The supplied exercises and direct elementary proof§13 were read/checked.',
 'Summation by parts with c_n↓0 and bounded initial sums gives a2M tail estimate; M requires interval-sum control. Periodic mean-zero criterion also needs divergence of the positive weight sum for the converse.',
 'Failed source access is not full-text verification. The geometric bound is uniform only away from z=1. The material is reused analysis support, not an extra PD lecture chapter.',
 'Classical results independently re-proved, exact counterexample to the sharper bound saved. No historical-first-source or novel result asserted.')

def tsv(name,rows):
 with (P/name).open('w') as f:
  w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
tsv('search_log.tsv',families)
raw=[];index=[]
for file in sorted((B/'research').glob('late_web_*.json')):
 d=json.loads(file.read_text());args=d['args']
 payload='\n'.join(c.get('text','') for c in d.get('result',{}).get('content',[]) if c.get('type')=='text')
 urls=list(dict.fromkeys(re.findall(r'https?://[^\s<>\)\]\}]+',payload)))
 index.append(dict(file=str(file.relative_to(B)),args=args,returned_urls=urls))
 for operation,requests in args.items():
  if operation=='response_length':continue
  for j,req in enumerate(requests,1):
   raw.append(dict(raw_log=str(file.relative_to(B)),operation=operation,request_number=j,request=json.dumps(req,ensure_ascii=False),result_record=str(file.relative_to(B)),assessment='Full substantive tool output retained in result field. Consult linked family synthesis for hypothesis assessment; an open request may have failed.'))
tsv('search_queries.tsv',raw)
(P/'raw_search_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
intro='''# Literature search record: late SA08 packages

All searches and source inspections below were performed on19November2026. Each
claim is explicitly assigned to one or more of the twenty assessed families.
The family grouping is an editorial index, not an inference of mathematical
equivalence. Every claim retains its own statement, hypotheses, fate and limits
in claims.json. Source records distinguish metadata, opened theorem passages,
source dependencies, failed access and independent proof.

The searches include official primary sources, arXiv, Numdam, SGA originals,
zbMATH-directed queries and MathOverflow leads. zbMATH0201.35602 redirected or
failed; the Roby metadata supplies Zbl0117.02302; the Garvin0945.55007 route was
reported failed by the early agent. MathOverflow was used for terminology and
reference discovery, not as a substitute for an exact technical source. Author
bibliography routes for Atiyah and Viruel were checked where accessible; access
failures remain in the raw logs. Later papers were followed backwards to Roby,
SGA4, Cartan, Miller, Dold–Kan and the formal algebraization inputs.

No negative or incomplete search is evidence of mathematical novelty. A class C
claim can have a checked local proof while its exact historical publication fate
remains unidentified; the dossier states these separately. Primary PDF downloads
and original-image checks outside the web interface are recorded in
source_checks.md and the reference-verification scopes. The root agent preserves
its own full-source outputs for shared SGA7/Cartan/Mandell checks.

'''
parts=[intro]
for f in families:
 parts.append(f"## {f['search_id']}. {f['subject']}\n\nClaims: {f['claims']}.\n\nSources inspected: {f['opened_sources']}\n\nExact match: {f['hypothesis_match']}\n\nLimits: {f['excluded_inference']}\n\nResult: {f['outcome']}\n\nRaw tool records: {f['raw_logs']}.\n")
(P/'search_log.md').write_text('\n'.join(parts))
assert all(c['searches'] and set(c['searches'])<=set(f['search_id'] for f in families) for c in claims)
print(json.dumps({'families':len(families),'claims_covered':len(claims),'raw_calls':len(index),'individual_requests':len(raw)},indent=2))
