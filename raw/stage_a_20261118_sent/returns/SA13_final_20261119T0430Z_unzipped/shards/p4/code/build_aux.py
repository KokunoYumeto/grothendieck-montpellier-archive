"""Manually authored p4 stages 3–6 and research bibliography.
Only locators, identifiers, tabular serialization and coverage checks are automated.
"""
from pathlib import Path
import json,csv
OUT=Path(__file__).resolve().parents[1]
items={x['id']:x for x in json.loads((OUT/'items.json').read_text())}
claims=json.loads((OUT/'claims.json').read_text())
problems=[]
def problem(n,title,ids,as_he,plausible,art,why,worth,refs):
    loc=[]
    for i in ids:
        for l in items[f'SA13-{i}']['lines']:
            if l not in loc:loc.append(l)
    problems.append(dict(id=f'MP-SA13-{n}',title=title,occurrences=loc,as_he_states=as_he,plausible_today=plausible,state_of_art=art,why_open=why,worth=worth,refs=refs))
problem(90,'Flatness in the quotient relation',[402],
 'Can flatness replace the smoothness used in the quotient-relation argument on the reused GIT leaf?',
 'A represented flat locally finitely presented equivalence relation admits an algebraic-space sheaf quotient under the usual hypotheses; descent to a scheme and finite type require additional assumptions.',
 'Mumford–Fogarty §0 fixes the geometric-quotient conventions; Hashimoto proves finite-type results for universal strict orbit spaces. Neither is a literal answer to the incomplete margin.',
 'The retained margin omits the surrounding hypotheses; no source states why the author left it.',
 'Worth a short source-and-ink check, because one missing qualifier changes the category of quotient.',
 ['P4_MumfordFogarty1982','P4_HashimotoQuotients','P4_DeJongGIT'])
problem(91,'Finite type of an orbit quotient',[404],
 'The typed source expects the algebraicity assumption on the quotient to be unnecessary.',
 'For a flat finite-type group scheme over a noetherian base, a universal strict orbit space has the finite-type property asserted in Hashimoto’s theorem.',
 'The checked GIT second-edition footnote says the question was settled by Fogarty; Hashimoto gives a primary modern proof in an explicitly stated quotient setting.',
 'The original retained typed version predates the checked revised footnote; no date of reuse or authorial priority is inferred.',
 'A bibliographic task of modest interest; the relevant theorem is established.',
 ['P4_MumfordFogarty1982','P4_HashimotoQuotients'])
problem(92,'A doubled Picard extension',[409],
 'Construct the displayed lift and split the Picard/NS extension after pullback by2.',
 'A homomorphic lift s with hs=2id splits the pullback extension; a canonical sheaf-level construction needs the base and rigidifications specified.',
 'The cube identity and symmetric/antisymmetric decomposition are checked in Moonen et al. II2.12; the exact unfinished lift is not identified.',
 'The page ends mid-construction. No reason beyond the interruption is supplied.',
 'Worth a few hours to identify the precise Picard functor and its2-torsion obstruction.',
 ['P4_MoonenLineBundles','P4_SGA7VII'])
problem(93,'All amended finite invariant-cycle cases',[414,419,421],
 'Extend the degree-one invariant-cycle exact sequence to the inserted arbitrary-n cases, with the Brauer term θ(n).',
 'Prime-to-p étale Kummer gives the displayed mechanism; p-primary statements need flat cohomology, a specified Picard functor and the exact geometric assumptions.',
 'Raynaud1970 §§6,8 and SGA7 IX12.1 identify divisor and curve ingredients. The complete amended sequence with all alternatives has not been located exactly.',
 'The page changes the prime restrictions and adds the obstruction; it does not explain a later abandonment.',
 'High-interest identification task: trace the1967 announcements against the1970 full paper before proposing a new theorem.',
 ['P4_Raynaud1970','P4_Raynaud1967Announcements','P4_SGA7IX','P4_ColliotTheleneSkorobogatov'])
problem(94,'Factorization of total multiplicity gcd',[416],
 'The inserted expression identifies gcd(μ_i d_i) with gcd(d_i)gcd(μ_i).',
 'The total multiplicity/index formula is valid in Raynaud’s curve setting; the separate gcd factorization requires a further relation on the geometric data.',
 'The unrestricted arithmetic identity is disproved by (d_i)=(2,3),(μ_i)=(1,2). Raynaud §7.1 and SGA7 IX12.1 are the exact geometric comparison targets.',
 'No justification is written for this inserted simplification.',
 'Worth an ink check and then a geometric realizability test; the numerical example alone does not refute a geometric theorem.',
 ['P4_Raynaud1970','P4_SGA7IX'])
problem(95,'Which vertical torsion is the NS kernel?',[417,428],
 'Is R=ker(Γ→NS(X_s)) the full torsion subgroup of Γ?',
 'R⊂tors Γ is cyclic; equality holds in the appropriate relative-curve comparison. In higher dimension P^0 and P^τ must be distinguished.',
 'Raynaud Theorem6.4.1 proves E∩P^τ=tors E. Proposition8.1.2 specializes to curves. It does not replace P^τ by P^0 in arbitrary dimension.',
 'The page explicitly asks the kernel question after using only a finite cyclic subgroup.',
 'High interest: isolate the quotient P^τ/P^0 and its interaction with vertical divisors in a concrete higher-dimensional model.',
 ['P4_Raynaud1970','P4_SGA7IX'])
problem(96,'Brauer transition maps in the inverse limit',[420],
 'Pass from bounded-exponent obstruction groups to their zero inverse limit.',
 'The conclusion follows for the actual multiplication-by-l Kummer transitions and uniformly bounded l-exponent; it is false for arbitrary transition maps.',
 'The Kummer diagram and the direct argument x_i=l^N x_(i+N) settle the step; Colliot-Thélène–Skorobogatov §1.4 and§4.3 supply the surrounding Brauer facts.',
 'The manuscript omits the transition-map computation, not necessarily the needed structure.',
 'Low remaining research interest after the check; retain it as a proof obligation for the companion edition.',
 ['P4_ColliotTheleneSkorobogatov','P4_Raynaud1970'])
problem(97,'Cancelled injectivity proofs and Raynaud’s exact locator',[425],
 'Obtain the needed injectivity through the cited Raynaud theorem after the preliminary proofs are cancelled.',
 'Use Raynaud’s separated Picard/divisor theory under its actual hypotheses; do not revive the cancelled cover argument.',
 'Raynaud1970 §6.4 is relevant, but the cited short-announcement th.3/prop.7(ii) numbering remains unresolved.',
 'The cancellations and appeal to Raynaud are explicit; no external reason for abandoning the sketches is known.',
 'Worth a targeted bibliographic session because an exact locator would settle several dependent statuses.',
 ['P4_Raynaud1970','P4_Raynaud1967Announcements'])
problem(98,'Weakening regularity to local factoriality',[429,431],
 'The margin suggests weakening the regularity hypothesis to local factoriality in the divisor argument.',
 'The Cartier-divisor lattice step only needs local factoriality; other uses of resolution, smoothness and Picard representability must be checked separately.',
 'Raynaud §§6.1.11,8.1.4 use local factoriality in precise results. They do not establish an unrestricted replacement throughout the full manuscript proof.',
 'The margin marks a local weakening, not a revised complete theorem.',
 'Worth separating the proof dependencies; a few hours should settle the lattice part, not the entire p-primary statement.',
 ['P4_Raynaud1970','P4_SGA7IX'])
problem(99,'Arithmetic orthogonality beyond a trait',[432,438],
 'Prove orthogonality over the broader written adic base using Frobenius weights and torsion finiteness.',
 'The arithmetic argument gives the specified pairing vanishing/inclusion. Equality of the orthogonal complement requires rank or geometric input.',
 'SGA7 IX2.6(a) explicitly separates this arithmetic inclusion from Theorem2.4 over a henselian trait.',
 'The manuscript changes ambient bases and leaves the equality mechanism unstated; no source claims the broader formulation solved.',
 'High interest only after the base and finiteness assumptions are fixed; otherwise it is an underdetermined extension.',
 ['P4_SGA7IX'])
problem(100,'Finite subgroup closure and specialization',[433,435],
 'Control finite closures of generic torsion and their special-fibre pairings over the written base.',
 'Finite étale lifting is controlled over proper henselian bases; arbitrary finite flat torsion and general adic bases require separate representability and flatness hypotheses.',
 'Stacks0A48 and09ZL give exact finite-étale equivalences. They do not assert smoothness of a finite flat p-group scheme.',
 'The leaf queries or uses the relevant closure property without a full uniform construction.',
 'Worth a focused comparison with the precise model category, not a blanket finite-group-scheme assertion.',
 ['P4_Stacks0A48','P4_Stacks09ZL','P4_SGA7IX'])
problem(101,'One model for every torsion level',[436,439],
 'Choose a finite-type model or extension that works simultaneously for all ν.',
 'Finite-level descent gives ∀ν∃K′; uniformity requires a single finite amount of geometric data or a separate l-adic finiteness theorem.',
 'SGA7 IX2.6(a) makes the arithmetic reduction in its stated setting. No source exactly matches the manuscript’s broader adic-base all-level assertion.',
 'The question mark is explicitly attached to the all-level model step.',
 'High-interest short task: identify the finite presentation data controlling the whole Tate tower.',
 ['P4_SGA7IX'])
problem(102,'Equivalence of polarization corollaries',[438],
 'The equivalence of two corollaries is left to the reader.',
 'The stated polarization-induced isogeny compares the rational pairings; clearing its denominator and using torsion-free Tate lattices gives the integral vanishing implication.',
 'SGA7 IX2.5 provides the published polarization comparison; the linear-algebra step is supplied in the proof audit.',
 'It is left as an exercise, not presented as an open conjecture.',
 'No new research needed; include the short proof in the companion commentary.',
 ['P4_SGA7IX'])
problem(103,'Geometric meaning of the discriminant form',[443,444,445,446],
 'Identify the explicit lattice pairing with the obstruction from the Poincaré biextension, and understand weighted perfectness.',
 'Under the regular relative-curve hypotheses and a rational point, compare with the restricted intersection pairing; retain residue-field and weight qualifications.',
 'SGA7 VIII7.1(b) supplies the extension obstruction. Bosch–Lorenzini Theorem4.6 identifies the Jacobian pairing and Corollary4.7 specifies its perfectness cases.',
 'The manuscript asserts geometric meaning after an abstract calculation; it does not include the full comparison proof.',
 'High interest for a concrete weighted example, with a few-hour run capable of computing the two finite groups and their comparison map.',
 ['P4_SGA7VIII','P4_BoschLorenzini2002','P4_Raynaud1970'])
problem(104,'Henselianity versus formal inverse closure',[449,450],
 'Does henselianity of the A_n imply closure under all formal inverse maps, and what is the smallest such family?',
 'Implicit algebraic equations are controlled by henselian-pair criteria; arbitrary chosen formal-coordinate inverses are a separate closure property unless the family is explicitly the algebraic power-series system.',
 'Stacks09XD/09XI give the exact henselian definition. Modern Weierstrass systems add closure axioms stronger than the manuscript’s bare question.',
 'The first draft asks the converse and proposes algebraic series as a test case without a proof.',
 'High interest: compare minimal H-closure with henselization in a fixed coefficient field.',
 ['P4_Stacks09XD','P4_Stacks09XI','P4_AschenbrennerSrhir2024','P4_ChiuHauser2021'])
problem(105,'Smallest flow-closed family',[451,452],
 'Require closure under formal flows, including time-dependent fields, and obtain primitives and elementary transcendental functions.',
 'The extra flow axiom gives these solutions; henselian/algebraic-series closure alone does not, since exp(t) is not algebraic in characteristic0.',
 'Formal ODE recursion and the autonomous-time construction are checked; modern analytic systems and formal Frobenius provide comparisons, not an exact classification of the minimal A-family.',
 'The pages introduce desired closure properties rather than prove their minimal realization.',
 'Worth a few-hour axiomatic closure construction; a full classification is a larger project.',
 ['P4_BolsinovZuev2009','P4_AschenbrennerSrhir2024'])
problem(106,'BCH integration inside A',[453],
 'The Hausdorff formal-group construction should work in the chosen family; the sketch ends after reduction using Ado.',
 'Formal BCH exists over characteristic-zero fields. Membership in A needs a proof from the actual flow and substitution axioms, with no illicit formal evaluation at1.',
 'The ambient formal Frobenius theorem is checked; the exact A-membership theorem has not been identified in the searched analytic/formal literature.',
 'The argument stops at its stated reduction; no later source explaining the omission was found.',
 'High-interest proof-completion task, starting with a nilpotent matrix Lie algebra and then auditing the Ado step.',
 ['P4_BolsinovZuev2009','P4_CluckersLipshitz2017'])
problem(107,'Pfaff converse in a restricted function class',[454,455],
 'Integrate a regular involutive Pfaff system in A; compare the rank-one case with flow closure.',
 'The ambient formal Frobenius theorem holds over characteristic-zero fields; A-valued first integrals require an additional closure theorem or axiom.',
 'Bolsinov–Zuev Theorem2 proves the ambient theorem. The wholly cancelled39:8 retraction draft is not a second proof.',
 'The converse is expressly desired, and the following attempted geometric formulation is cancelled.',
 'High interest, but begin with rank2 and a precisely generated family; the full arbitrary-A question exceeds a short session.',
 ['P4_BolsinovZuev2009','P4_CluckersLipshitz2017'])
problem(108,'Projective and finite module coordinates',[457],
 'Replace free finite coordinate modules by projective modules, perhaps all finite modules.',
 'Finite projective modules permit coordinate-free smooth formal affine spaces and local descent. Arbitrary finite modules can define singular spaces and need a broader category.',
 'Strickland formal schemes provide the ambient setting; no exact treatment of this A-family extension was identified.',
 'The page explicitly asks both extensions, with no claimed construction.',
 'Moderate interest: the finite-projective descent problem is feasible; keep arbitrary finite modules separate.',
 ['P4_StricklandFormal','P4_StricklandFPFP'])
problem(109,'Transverse products before H',[458],
 'Construct transverse fibre products in the A-category under the axioms then in force.',
 'H supplies the needed inverse-coordinate construction. Under the earlier axioms alone, closure of the solution in A has not been established.',
 'Chiu–Hauser Lemma1.2 proves the ambient inverse theorem, not selected-family closure.',
 'The assertion precedes the added inverse-closure axiom.',
 'Worth a short dependency audit and an explicit two-equation example.',
 ['P4_ChiuHauser2021'])
problem(110,'Rejected evaluation at1 and its repair',[459,460],
 'Use an inverse formal map to prove ambient-unit closure; the text rejects its own evaluation at1.',
 'H gives the Jacobson property of the augmentation ideal. H+D gives full ambient-unit reflection by extracting the coefficient of the auxiliary variable.',
 'The proof audit supplies both repairs and the full H-only counterfamily Z+(t)Q[[t]]. Henselian-pair references verify the target notion.',
 'The text itself identifies the illegal evaluation and continues with a weaker statement.',
 'No new theorem is needed for these two conclusions; the scan should decide which stronger assertion survives.',
 ['P4_Stacks09XD','P4_ChiuHauser2021'])
problem(111,'Henselian factor lifting from H',[461,462],
 'Deduce coprime-factor lifting and the implicit-function theorem from inverse closure.',
 'The coefficient multiplication map has unit Sylvester determinant; H and zero evaluation give the lift, together with the Jacobson property.',
 'The direct proof is supplied; Stacks09XD/09XI give equivalent henselian criteria and Chiu–Hauser gives the ambient inverse criterion.',
 'The pages sketch rather than fully expand the determinant and the permitted substitution.',
 'Low remaining research interest; useful as a complete companion proof.',
 ['P4_Stacks09XD','P4_Stacks09XI','P4_ChiuHauser2021'])
problem(112,'Faithful flatness of the ambient formal ring',[463],
 'Is k[[t_1,…,t_n]] faithfully flat over A_n if k is faithfully flat over A_0?',
 'Under a D-only reading the polynomial family is a counterexample to faithfulness. Under H+D the question needs a new argument or a full-family counterexample.',
 'Modern Weierstrass/analytic systems have extra hypotheses; none of the opened results certifies arbitrary A-families. The polynomial counterexample is carefully restricted to its admissible reading.',
 'A margin asks the question, and the letter d has changed meaning between drafts.',
 'Very high interest once the ink fixes d; a few-hour run can test coherent/noetherian examples, not settle all families.',
 ['P4_AschenbrennerSrhir2024','P4_CluckersLipshitz2017','P4_Stacks09XD'])
problem(113,'Ordinary versus divided derivatives',[464],
 'The characteristic-zero margin suggests ordinary derivative closure is equivalent to divided derivative closure.',
 'This holds for a Q-algebra coefficient ring. Characteristic0 alone does not permit division by factorials.',
 'Hasse identities are recomputed. Z[t,t²/2] disproves the bare ring inference, but is not offered as a complete H/composition family.',
 'The manuscript shifts from a field draft to an arbitrary-ring draft.',
 'Worth fixing the precise coefficient assumption; a full-family counterexample would be a separate task.',
 ['P4_CluckersLipshitz2017','P4_AschenbrennerSrhir2024'])
problem(114,'Functorial principal parts and differential operators',[465,466],
 'Give infinitesimal neighborhoods and differential operators canonical A-structures, compatible with transverse pullback.',
 'In A-charts, Hasse identities and coefficient extraction verify the construction. Globalization needs coordinate-change/descent hypotheses.',
 'The local calculation is checked; the exact arbitrary-A globalization is not identified in Strickland or the analytic-structure literature.',
 'The leaf lists functorial properties without a complete descent proof.',
 'Moderate interest: formulate and prove the chart-transition lemma first.',
 ['P4_StricklandFormal','P4_CluckersLipshitz2017'])
problem(115,'Induced structures and smooth completion sections',[467,468],
 'Construct the induced A-structure on a smooth formal subspace and a section in the smooth-completion situation.',
 'With an A-transverse chart, the graph criterion gives uniqueness and local existence; an unnamed global construction cannot be supplied from the leaf alone.',
 'The ambient inverse theorem and formal smooth geometry are established comparisons. No exact unrestricted A-section theorem was located.',
 'The construction is unnamed and relies on earlier desired closure properties.',
 'Worth a short proof audit in affine charts before attempting projective descent.',
 ['P4_ChiuHauser2021','P4_StricklandFormal'])
problem(116,'Integral quotient effectivity',[469,470],
 'Make the relation defined by an integrable distribution effective in the A-category; decipher the X/X′ target in the quotient criterion.',
 'A regular formal distribution has a local ambient quotient in characteristic0. Effectivity and A-membership are additional requirements.',
 'Bolsinov–Zuev Theorem2 settles the ambient first-integral statement, not arbitrary A-effectivity.',
 'The leaf introduces this as a further axiom rather than deriving it.',
 'High interest if pursued after the Pfaff problem; first specify the relation and its categorical quotient.',
 ['P4_BolsinovZuev2009','P4_StricklandFormal'])
problem(117,'Division with a complete linear topology',[471],
 'Prove unique division and regularity for a distinguished series over a separated complete linearly topological ring.',
 'The full statement holds with finitely many topologically nilpotent lower coefficients and a unit leading coefficient.',
 'Strickland FPFP Theorem33.1/Corollary33.2 match the scope. The proof audit supplies the discrete-quotient and nilpotent-filtration argument, retaining the full unit series.',
 'The manuscript abandons two proof routes, then supplies a third. Its final scalar notation is a reading alarm, not cancellation of the theorem.',
 'No open theorem remains here; a few-hour task could produce a clean constructive companion with explicit precision control.',
 ['P4_StricklandFPFP','P4_StricklandFormal','P4_MoretBailly2023'])
(OUT/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

def tsv(name,fields,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

readings=[]
def rd(c,s,l,r,a,e,w='high',conf='medium'):
 readings.append(dict(cote=c,scan=s,line=l,reading=r,alternative=a,evidence=e,weight=w,confidence=conf))
rd(36,53,'7–17','flatness/smoothness in relation argument','Check whether the margin changes the ambient relation hypothesis or only a proof step.','Finite-type quotient and algebraic-space quotient hypotheses differ; missing scope prevents a precise modern theorem.')
rd(36,59,'161–177','minus in parallelogram identity; Δ arrow toward the product','Plus in the quadratic identity; diagonal arrow from A to A×A.','At u=1,v=0 the minus identity gives0=2[L] for an ample NS class; diagonal variance is forced.','high','high')
rd(36,61,'204–240','Γ displayed with denominator but missing numerator','The component-cycle group ⊕_i Z X_i divided by the special-fibre multiplicity relation.','The numerator appears on65 and69; Raynaud6.1 identifies the vertical-divisor lattice.')
rd(36,61,'204–240','H¹ with arbitrary n and unlabelled cohomology topology','Determine whether flat Kummer cohomology is intended in the p-primary insertion.','μ_p is not an étale torsor in characteristicp; the all-n assertion changes its meaning with the site.')
rd(36,61,'226–240','gcd(μ_i d_i)=gcd(d_i)gcd(μ_i)','Check cancellation or a missing hypothesis linking the multiplicities.','The unrestricted numerical identity fails at d=(2,3),μ=(1,2), but no geometric counterexample is claimed.')
rd(36,61,'242–247','R⊗Z_l identified with Z/l','Z/l^{v_l(e)} for R=Z/e.','Tensoring the cyclic presentation proves the exponent; e=l² refutes the literal expression.','high','high')
rd(36,65,'336–397','cancelled injectivity proof and later Raynaud appeal','Check the full cancellation boundary and exact th.3/prop.7(ii) locator.','The cancelled argument must not be revived as a surviving proof; exact announcement numbers remain unidentified.')
rd(36,66,'399–407','Δ_U∩Δ_V=Δ_(U∩V)','Δ_U∩Δ_V=Δ_(U∪V), or the union-inclusion actually needed by the proof.','The discrete Z, H=2Z example satisfies all neighborhood conditions and refutes the printed equality.','high','high')
rd(36,66,'409–413','Lie groups satis- (word cut off)','Leave the missing word unresolved.','No-small-subgroups implies the mathematical example; it cannot decide the missing ink.','low','low')
rd(36,67,'419–478','δ[n]/δ′[n] versus (δ/δ′)[n]','Retain the author’s correction and check which quotient remains live.','Z/4 with subgroup2Z/4 and n=2 distinguishes the expressions.','high','high')
rd(36,69,'494–545','R versus all torsion of Γ; d′ used in differing roles','Check R/P⁰ versus the P^τ torsion comparison and the two d′ meanings.','Raynaud6.4.1 involves P^τ; the manuscript itself asks whether R is the entire cyclic torsion.')
rd(36,71,'567–613','order d substituted for previously denoted e','Retain e until R=tors Γ has been established.','Only e|d was proved; the separate kernel question remains live.')
rd(36,74,'635–662','general adic-base orthogonal-complement equality','Check whether the statement is only vanishing/inclusion.','SGA7 IX2.6(a) explicitly says the arithmetic method gives the inclusion, whereas equality uses separate geometry.')
rd(36,75,'665–704','finite flat group called smooth','Check étale/smooth versus flat wording and prime restriction.','Finite flat p-torsion need not be smooth; μ_p is the basic obstruction.')
rd(36,77,'748–777','single finite-type model for all ν','Check the uniform quantifier and associated question mark.','Levelwise descent does not give one model for the entire tower.')
rd(36,79,'789–819','K on the last finite-level display after passing to K′','K′ if the torsion rationality assumption is used.','The field enlargement is explicit immediately before the display.')
rd(36,81,'833–864','whole strict-henselian draft cancelled','Preserve the cancellation; do not count a second proof.','The surviving proof is on other leaves.','high','high')
rd(36,83,'877–914','β∘α where u is omitted','β∘u∘α.','The two maps otherwise have incompatible source/target lattices; the later formula includes u.','high','high')
rd(36,83,'899–914','u symmetric and parfait cancelled','Weighted transpose relation D u symmetric; perfectness only with the added lattice hypotheses.','The δ=(1,2) exact example gives index2 for the purported integral duality.','high','high')
rd(39,3,'984–1034','unit axiom target S_n or A_n; c deleted in minimum','A_n for unit reflection; retain c if the minimum uses prime-field coefficients in characteristic0.','Z[t] overQ satisfies the weaker family axioms and lacks1/2.','high','medium')
rd(39,8,'1151–1177','retraction/product argument wholly cancelled','No live result extracted from that draft.','Later quotient axioms are separate assertions.','medium','high')
rd(39,10,'1179–1211','nilpotent constants versus arbitrary constants in substitution','Only the continuous/nilpotent-constant substitution is legal.','Evaluation at1 fails for an arbitrary formal power series; finite nilpotent substitution is valid.')
rd(39,11,'1217–1249','evaluation at1 in inverse-map proof','Keep the self-rejection; H+D allows coefficient extraction instead.','The full H-only family Z+(t)Q[[t]] refutes strong ambient-unit reflection.','high','high')
rd(39,12,'1252–1292','unit of k treated as a unit of k₀','Require unit reflection or extract coefficients using D.','A₀=Z inside k=Q provides a complete H-family counterexample.')
rd(39,13,'1317–1323','d in faithful-flatness question','Resolve H versus D from the changed axiom labels.','The polynomial counterexample applies to D alone and not H; the answer depends on this ink.')
rd(39,15,'1340–1353','characteristic0 suffices for ordinary/divided derivative equivalence','A₀ is a Q-algebra, or verify additional axioms forcing factorial inverses.','Characteristic0 does not itself invert factorials; the ring Z[t,t²/2] illustrates the gap.')
rd(39,16,'1356–1374','X/X′ in quotient-structure criterion','Check target and source against the preceding diagram.','The object receiving the quotient A-structure must be distinguished from the space carrying the relation.')
rd(39,20,'1439–1455','last reduction replaces F by scalar α Z^N','F modJ=Z^N U(Z) with a unit series U.','F=2+4Z+Z²+Z³ over Z/8 reduces toZ²(1+Z), so a scalar loses a term.','high','high')
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)

links=[]
def link(kind,fr,to,what,evidence,notes=''):
 links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=notes))
P='MPL_36_053-085+39#'
link('folder','36:061,065,069,071','36:083–084','Vertical-divisor kernel and curve component lattice are two related exact-sequence defects, not the same cokernel.','Both supplied passages read; R=kerw and the intersection-map coker have distinct definitions.',P+'17;'+P+'50;'+P+'58')
link('folder','36:074–077','36:079–081','Finite-level pairing argument and arithmetic Tate-module vanishing.','Both sides read; field extension may depend on ν;81 is cancelled.',P+'38;'+P+'45;'+P+'47;'+P+'48')
link('folder','39:003–008','39:010–017','Two formal-function axiom drafts change coefficient ring and axiom names.','Both drafts read in full; H,D and quotient effectivity have to be compared by content.',P+'60')
link('folder','39:011–013','39:015','Self-rejected evaluation at1 and the divided-derivative repair.','Both sides read; D extracts the coefficient of an auxiliary variable and zero evaluation is permitted.',P+'73;'+P+'74;'+P+'82')
link('folder','39:019','39:020','Division statement and its sequence of cancelled/live proofs.','Both pages read; the final live argument uses discrete quotients and the unit-series associated graded.',P+'90;'+P+'92;'+P+'94;'+P+'95')
published=[
 ('36:053,055,057','P4_MumfordFogarty1982 §0 Prop0.7–0.9; §1 Def1.5, Th1.1','Reused GIT leaves identified, with original/revised reductivity and freeness conventions.','1;2;3;4;5'),
 ('36:054–058','P4_SGA7VII 2.9.4–2.9.6,3.6.5; P4_SGA7VIII1.1.4,1.4','Biextension rigidity, additivity and internal Hom–Ext identification.','6;7;8'),
 ('36:059','P4_MoonenLineBundles II2.12','Cube and multiplication formula; the printed minus is not the quadratic identity.','9;10'),
 ('36:066,068,070,072','P4_BourbakiIntegration78 VIII§5 nos.1–4','Exact source of the reused Haar-measure draft, after bibliographic follow-up.','13;14;15;16'),
 ('36:061–071','P4_Raynaud1970 6.1.3,6.1.11,6.4.1; P4_SGA7IX12.1','Vertical divisors and finite invariant-cycle ingredients; no full arbitrary-n identification claimed.','17;21;25;34;35;37'),
 ('36:074–077','P4_SGA7IX2.4,2.6(a)','Full trait orthogonality and the distinct arithmetic inclusion.','38;49;97'),
 ('36:083–084','P4_Raynaud1970 8.1.2,8.1.4','Curve component lattice and the additional Néron hypotheses.','50;52;58'),
 ('36:084','P4_SGA7VIII7.1(b); P4_BoschLorenzini2002 Th4.6,Cor4.7','Biextension obstruction versus the intersection discriminant pairing.','54;57;59'),
 ('39:012–013','P4_Stacks09XD Def15.11.1; P4_Stacks09XI Lem15.11.6; P4_ChiuHauser2021 Lem1.2','Henselian-pair and ambient formal inverse comparisons, with selected-family closure kept separate.','75;78;79'),
 ('39:007,016–017','P4_BolsinovZuev2009 Th2','Ambient formal Frobenius; not automatic A-effectivity.','67;68;89'),
 ('39:019–020','P4_StricklandFPFP Th33.1,Cor33.2; P4_StricklandFormal5.14–5.16','Complete linear-topology division/preparation with no noetherian hypothesis.','90;91;92;96')]
for fr,to,what,ns in published:link('published work',fr,to,what,'Supplied passage and stated source locators read; see bibliography verification scope.',';'.join(P+n for n in ns.split(';')))
prior=[
 ('LM7 E.23','LM7_FERMAT_TOWER_results.csv; §51.16; folios733v–736v; scans172–178','No inference about metabelian/depth-two section-map image or fibres.'),
 ('LM4 D.12','LM4_FINITE_GROUP_ACTIONS_results.csv;25bis,folios157v–160,scans312–317;§30,folio194v,scan384','Vertical-divisor torsion is not full profinite GT₀ torsion.'),
 ('LM4 F.7','LM4_FINITE_GROUP_ACTIONS_results.csv;§30,folios194–196,scans383–387','No conclusion about nonsolvable completion centralizers or the A₅ comparison.'),
 ('LM7_PUSH C.6','LM7_PUSH_results.csv;C.3; no scan supplied','Preparation does not re-prove the class-two germ classification.'),
 ('INTAKE LM7_CONTINUED E.37','INTAKE_LM7_CONTINUED.md;PartE/E.37;truncated rank44 criterion','No transfer from formal convergence to section-map corrections.'),
 ('MPL_33_002-049 §96','MPL_33_002-049_notes.md;register excerpt','Inventory lead only; earlier unseen rows unavailable.'),
 ('MPL_33_002-049 §2','MPL_33_002-049_notes.md;truncated scans002…','Published-comparison lead, not an exact checked cross-folder match.'),
 ('MPL_142_001-093 §316','MPL_142_001-093_notes.md;bibliographic excerpt','Method comparison only; no mathematical claim inferred.'),
 ('MPL_14_002-044 §107','MPL_14_002-044_notes.md;effectivity/Lefschetz excerpt','Different categories; no proof transfer of effectivity.'),
 ('MPL_33_002-049 §93','MPL_33_002-049_notes.md;title inventory excerpt','Current numbering does not complete an unseen earlier title sheet.'),
 ('MPL_91_099-143 §68','MPL_91_099-143_notes.md;scan124 title,126,128 thickness','Greenberg thickness not identified with Tate finiteness or intersection weights.'),
 ('WG H9','WARGAME_MATH_HUNCHES_20261112.md;cote44 Th4–5;no scans','Weighted curve lattice does not prove higher-codimension Mordell–Weil/Hodge index.'),
 ('WG2 §2.1 #2','PROGRAM_WARGAME_ROUND2_20261112.md;Sur certains anneaux gradués,ms1–16,scans003–018; cote unresolved','Transpose analogy supplies no universal Lefschetz operator or grading projector.'),
 ('Hua 36-h1-invariant-cycle-defect','notes/RESULTS_STATE.md;36:061–071','The present review adds prime/site qualifications and kernel distinction; intake was unverified.'),
 ('Hua 36-orthogonality-regular-adic-base','notes/RESULTS_STATE.md;36:074–077','The live base does not assume regularity; arithmetic inclusion does not prove full equality.'),
 ('Hua 39-inverse-function-axioms-henselian','notes/RESULTS_STATE.md;39:010–013,015','Henselian repair retained; stronger H-only unit-reflection refuted by the full family example.'),
 ('LM4;LM7;LM7_PUSH run state','MATHS_PROMPTS_TALLY.md;LM7_PUSH checkpoint09','RETURNED is provenance, not a referee verdict for an individual claim.'),
 ('S19 / package218 plan','README.md;unchecked placement/comparison request','No originality certification is implied.')]
for title,target,what in prior:link('our projects',P+'101;'+P+'102',title+' — '+target,what,'Earlier-run context lead only. Backing return/manuscript is not attached; not a verified mathematical link.',P+'101;'+P+'102')
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)

searches=[
 ('P4-S01','Mumford Geometric Invariant Theory Reynolds operator Proposition0.9 free action; exact text fragments pages53,55,57,59','GIT second-edition primary reproduction; publisher edition history','Exact reused GIT text located. Freeness and linear reductivity recovered; no priority of reused leaves inferred.','P4_MumfordFogarty1982'),
 ('P4-S02','Fogarty geometric quotients algebraic schemes finite type Hashimoto; de Jong GIT quotient universal submersive','Primary Hashimoto paper and de Jong author commentary','Finite-type orbit-space result verified under universal strict orbit-space hypotheses; flat-replacement margin underdetermined.','P4_HashimotoQuotients;P4_DeJongGIT'),
 ('P4-S03','SGA7 VII2.9.4 2.9.6 biextensions Hom Ext; VIII1.1.4 1.3 1.4 2.2.8 4.10 4.14 7.1','Original SGA7I scan; Springer chapter metadata; digital index used only for discovery','Exact locators found for rigidity, Hom–Ext, torsion pairings, obstruction. Digital mirror formulas not accepted without original/re-proof.','P4_SGA7VII;P4_SGA7VIII'),
 ('P4-S04','abelian variety theorem cube multiplication n line bundle n(n+1)/2 Moonen','Author chapter Line bundles and divisors','II2.12 matches multiplication formula and repairs quadratic sign; exact unfinished doubled lift remains partial.','P4_MoonenLineBundles'),
 ('P4-S05','Bourbaki integration Haar measures sous groupes fermés n384 covolume Chabauty; Chabauty1950 limite ensembles','Bourbaki author bibliography; primary book text; Numdam Chabauty','Exact source VIII§5 found. Chabauty1950 alone has narrower original hypotheses.','P4_BourbakiIntegration78;P4_Chabauty1950'),
 ('P4-S06','Raynaud Spécialisation foncteur Picard1967 th3 proposition7;1970 6.4.1 8.1.2 multiplicité totale','Numdam full1970 article and original SGA7IX12.1','Vertical Cartier divisors, P^τ torsion, curve lattice and Néron hypotheses verified. Announcement numbering remains unverified.','P4_Raynaud1970;P4_Raynaud1967Announcements;P4_SGA7IX'),
 ('P4-S07','strictly henselian discrete valuation Brauer group index zero cycle Kummer transition; invariant cycles Picard p-primary','Colliot-Thélène–Skorobogatov author book; Raynaud1970; SGA7IX12','Br(K) p-primary and degree-one splitting verified. Whole amended manuscript sequence not exactly located.','P4_ColliotTheleneSkorobogatov;P4_Raynaud1970;P4_SGA7IX'),
 ('P4-S08','SGA7 IX2.4 2.6 arithmetic orthogonality Frobenius; VIII4.10 toric affine','Original SGA7I pp338,341–342; VIII4','The arithmetic argument is expressly an inclusion; equality is a separate theorem over a trait.','P4_SGA7IX;P4_SGA7VIII'),
 ('P4-S09','henselian proper scheme finite étale covers specialization; finite étale henselian pair Stacks','Stacks Tags0A48,09ZL opened in full','Exact finite-étale comparison, not arbitrary finite-flat p-torsion smoothness.','P4_Stacks0A48;P4_Stacks09ZL'),
 ('P4-S10','Bosch Lorenzini Grothendieck pairing component groups Jacobians Theorem4.6 weighted intersection','Author-hosted published paper; Raynaud1970','Abstract discriminant and geometric Jacobian comparison identified with rational-point and residue-field conditions.','P4_BoschLorenzini2002;P4_Raynaud1970'),
 ('P4-S11','Grothendieck formal function axioms henselian Weierstrass systems faithful flatness Hasse derivatives; zbMATH arXiv MathOverflow variants','Aschenbrenner–Srhir2024; Cluckers–Lipshitz2017; primary formal-scheme references','Modern systems impose stronger axioms. No exact classification or arbitrary-family faithful-flatness theorem located; no nondevelopment claim made.','P4_AschenbrennerSrhir2024;P4_CluckersLipshitz2017;P4_StricklandFormal'),
 ('P4-S12','formal inverse function arbitrary commutative ring invertible Jacobian; henselian pairs coprime monic factor lifting','Chiu–Hauser Lemma1.2; Stacks09XD/09XI','Ambient inverse criterion and henselian definitions verified; H-closure within A remains an axiom.','P4_ChiuHauser2021;P4_Stacks09XD;P4_Stacks09XI'),
 ('P4-S13','formal Frobenius theorem involutive distribution characteristic zero; BCH formal flow Ado analytic system','Bolsinov–Zuev2009 Theorem2; formal/analytic-system references','Ambient first-integral theorem verified; chosen A-membership and exact BCH closure were not identified.','P4_BolsinovZuev2009;P4_CluckersLipshitz2017'),
 ('P4-S14','Cluckers Lipshitz strictly convergent analytic structures henselian system unique solution','Author-hosted JEMS2017 paper §3.2.1 Lem3.2.3','Primary modern comparison uses strictly convergent/Weierstrass data, not an exact resolution of all arbitrary-A claims.','P4_CluckersLipshitz2017'),
 ('P4-S15','Strickland formal schemes finite projective modules nilpotent substitution formal groups','Author text Formal schemes and formal groups; FPFP draft','Ambient category and nilpotent substitution verified; projective/finite A-structures not exactly located.','P4_StricklandFormal;P4_StricklandFPFP'),
 ('P4-S16','Weierstrass preparation complete linearly topological ring topologically nilpotent Strickland33.1 OMalley1972 MoretBailly','Strickland FPFP33.1–33.2; Formal5.14–5.16; Moret-Bailly1.1/1.2','Full topological scope matched in Strickland; OMalley original failed retrieval, recorded only as backward bibliographic lead.','P4_StricklandFPFP;P4_StricklandFormal;P4_MoretBailly2023;P4_OMalley1972')]
rows=[]
for sid,q,where,outcome,refs in searches:
 mapped=[c['id'] for c in claims if sid in c.get('search_ids',[])]
 rows.append(dict(search_id=sid,date='2026-11-19',queries=q,sources=where,outcome=outcome,claim_ids=';'.join(mapped),reference_keys=refs))
tsv('search_log.tsv',['search_id','date','queries','sources','outcome','claim_ids','reference_keys'],rows)

events=[]
who='GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p4'
def event(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for c in claims:
 event(c['id'],'used and rechecked in this run','Statement scoped against supplied passage and the cited primary-result locators; '+c['present_status'])
for i in [400,405,408,409,410,411,413,415,417,418,420,423,426,434,438,443,444,447,451,452,456,459,460,461,462,464,465,466,471,478,481,482,483,484,485,487,488,489]:
 event(f'C-SA13-{i}','independent re-proof','The general algebraic argument, hypotheses and limits are supplied in proof_audit.md; this does not certify any larger geometric statement merely by analogy.')
for i in [400,408,410,416,418,420,426,434,439,443,444,445,451,452,453,456,459,460,461,462,463,464,465,466,471,478,481,487]:
 event(f'C-SA13-{i}','computation or formal certificate','Exact executable finite checks passed in code/computations.py; full output and precision limits in outputs/computations.txt.')
for i,refined in [(408,'C-SA13-478'),(410,'C-SA13-410 (corrected formula)'),(418,'C-SA13-418 (refined exponent)'),(460,'C-SA13-459 and C-SA13-460 (H+D / Jacobson refinements)'),(483,'C-SA13-482')]:
 event(f'C-SA13-{i}',"refuted, with the refined statement's id",'Literal assertion refuted with all relevant example hypotheses stated; refined statement: '+refined+'. No manuscript ink changed.')
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
print('core auxiliary files:',len(problems),'problems,',len(readings),'reading alarms,',len(links),'links,',len(rows),'search groups,',len(events),'check events')
