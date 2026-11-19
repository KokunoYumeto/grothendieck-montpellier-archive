#!/usr/bin/env python3
"""Manually formulated claim records after complete source reading; no heading classifier."""
import json
from pathlib import Path
P=Path(__file__).parent
C=[]
SRC='sources/texts/pro/MPL_93_221-236+161-5_transcription.tex:'
def c(n,items,cote,scans,lines,his,statement,status,comp,cls,fate,date,refs,confidence='high'):
    C.append(dict(id=f'C-SA23-bt-{n:03d}',items=[f'SA23-{x}' for x in items],cote=cote,scans=scans,lines=SRC+lines,his_statement=his,statement=statement,status_on_pages=status,computation=comp,**{'class':cls},fate=fate,fate_date=date,present_status='As of 19 November 2026: '+fate,refs=refs,confidence=confidence))
G='bt_GrothCrystals1968'; KO='bt_KatzOda1968'; S='bt_Serre1967'; S79='bt_Serre1979'; MI='bt_Milne2017'
GD='Talks November–December 1966; published 1968. The archival sheets are undated here, so their chronological priority relative to the talks is not established.'
SD='Offprint dated December 1966; proceedings published 1967. No earlier circulation date established.'
ED='Classical result already used as known in the attached 1966/1967 text; exact first discovery not established.'
c(1,[206], '93',[221,231,232],'10-26,245-276','tout op. différentiel … à coeff cts … se factorise de façon canonique',
  'For a locally free stratified E with the asserted formal de Rham exactness, an augmentation-zero differential operator D:E→P factors as Δd⁰, and its induced additive map on Z¹=ker d¹ is independent of Δ. “Constant coefficients” means the manuscript’s Diff₊ relative to the stratification, not every translation-invariant operator. The precise finite-order exactness remains an explicit hypothesis.',
  'Open characteristic question on 221; conditional assertion on 231–232.',
  'Proof_checks §1; compute_checks block characteristic_p_coefficient_check: x^(p−1)dx has no polynomial/formal primitive in characteristic p. This obstructs the blanket formal-Poincaré argument, not every conceivable positive-characteristic reformulation.',
  'C','The characteristic-zero formalization/Poincaré framework is published in Grothendieck §6.2–6.5, pp.345–350. This supports the conditional factorization, while the exact finite-order “formally exact” axiom on these sheets is not supplied. Positive characteristic requires a different structure or additional hypotheses.',GD,[G])
c(2,[207],'93',[221],'24-26','g⁻¹dg → Z¹C(g)',
  'The ordinary Maurer–Cartan form of a smooth group is closed when the relevant Lie bracket is zero, in particular for a commutative group; for a general noncommutative group it satisfies the Maurer–Cartan equation and need not lie in ordinary Z¹. The preceding group hypothesis is not supplied on this retained page.',
  'Construction asserted; necessary group hypothesis is outside the retained excerpt.',
  'Proof_checks §1: d(g⁻¹dg)=−(g⁻¹dg)∧(g⁻¹dg); no commutativity is silently added.',
  'F','The closed-form target is identifiable in the commutative case; the universal claim is not identifiable without the missing hypothesis. Formal de Rham and connection sources do not justify deleting the bracket term.',ED,[G,'bt_Stacks0FKL'],'medium')
c(3,[208],'93',[222],'30-54','I(s)=∫a(s)^b(s)ωs est holomorphe en s',
  'For a smooth holomorphic submersion of complex manifolds, a relatively closed holomorphic one-form, holomorphic sections in the same fibre component, and a locally continuous family of piecewise differentiable fibre paths, the path integral is locally holomorphic. A change of path changes it by the corresponding locally transported period.',
  'Proof sketched using local primitives and subdivision.',
  'Proof_checks §2: cover the compact reference path by finitely many primitive charts; insert holomorphic local sections at subdivision points; primitive differences telescope. Continuous changes within these charts are homotopic and do not change the integral.',
  'E','The local proof is valid with relative holomorphic Poincaré lemma. Grothendieck §1.2 and §3.2–3.3 supply the de Rham/period framework; no claim of a new later theorem is needed.',ED,[G,KO])
c(4,[209],'93',[223],'56-74','μ(a,b)+μ(b,c)=μ(a,c)',
  'If every locally transported closed-cycle period is killed by ΣD_i applied to the associated ω_i, then μ(a,b)=ΣD_i∫a^bω_i is path-independent, holomorphic, and additive under concatenation of endpoints in a common fibre component.',
  'Proved from period ambiguity and concatenation.',
  'Linearity and concatenation check in proof_checks §2; no numerical experiment is needed.',
  'E','Valid elementary consequence of the stated annihilation hypothesis. It does not imply μ(a,b)=0.',ED,[G,KO])
c(5,[210,211],'93',[224],'76-106','Φ=f_*ZΩ¹/df_*O; connexion intégrable naturelle',
  'Relative de Rham hypercohomology has the Gauss–Manin connection under the usual smooth characteristic-zero hypotheses. The displayed quotient of global closed forms by global exact forms computes degree one only under acyclicity conditions, for example in the stated Stein setting; it is not a substitute for hypercohomology for arbitrary non-Stein X/S.',
  'Claim qualified by the author’s Stein warning.',
  'Proof_checks §2 checks where global exactness is used; no non-Stein assertion is inferred.',
  'A','Grothendieck §1.2, pp.307–308 explicitly uses hypercohomology and its Stein simplification; §3 constructs the connection. Katz–Oda §2 Theorem 1, p.204 gives the algebraic connection and §3 its explicit comparison.',GD,[G,KO])
c(6,[211],'93',[224,225],'81-115','chaque D_i se remonte … commutant à la diff. rel.; (9)',
  'An integrable holomorphic splitting lifts base differential operators to the relative de Rham complex; the resulting action on cohomology is independent of the splitting because the difference of vector-field lifts is vertical and its Lie derivative is dι+ιd. The lift on the complex itself is not canonical.',
  'Proof sketched; formula (9) asserted to be checked immediately.',
  'Proof_checks §2 independently checks Cartan’s identity, descent to cohomology, and composition to higher differential operators.',
  'A','Grothendieck §3.3, pp.324–326 and Katz–Oda §3 give this construction. Global derivation lifts can fail without an affine/Stein or local hypothesis; the published text also discusses that obstruction.',GD,[G,KO])
c(7,[209,210,214],'93',[224,225,229],'79-85,108-127,178-189','ΣD_iω′_i=0; Cela résulte du th. de De Rham sur les fibres',
  'A zero Gauss–Manin combination implies annihilation of all locally transported periods. Conversely, periods detect fibre cohomology; obtaining zero as a section of the sheaf under discussion additionally requires the correct hypercohomology, base-change/detection hypotheses. The source’s naive quotient alone is insufficient outside its Stein qualification.',
  'Forward proof sketched; converse asserted with a fibre de Rham reference.',
  'Proof_checks §2 verifies the forward primitive argument and identifies the missing sheaf-level implication in the converse.',
  'C','The standard smooth proper de Rham comparison supplies the period pairing and fibre detection; Grothendieck §1.2, §3.2 and Katz–Oda §4 match this qualified formulation. The source’s unrestricted nonproper/non-Stein converse is not established by those theorems.',GD,[G,KO])
c(8,[211],'93',[225,226],'119-140','(12), (13): D_s∫ω_s=∫D̄ω_s',
  'For horizontal endpoint sections for a fixed integrable splitting and compatible locally transported paths, differentiation of the relative path integral agrees with integrating the lifted differential operator on the form; higher-order operators follow by iteration and linearity.',
  'Proof sketched and continued with primitives on 227.',
  'Proof_checks §2: for ω=dφ and horizontal a,b, D(φb−φa)=(D̄φ)b−(D̄φ)a, then use a finite subdivision.',
  'E','The identity is the local primitive form of Gauss–Manin compatibility; published framework in Grothendieck §3.2–3.3 and Katz–Oda §3–4. It concerns derivatives of integrals, not their vanishing.',ED,[G,KO])
c(9,[211,212],'93',[225,227],'108-115,142-162','(14) μ(a,b)=φb−φa',
  'If ΣD̄_iω_i=dφ and a,b are horizontal for the chosen splitting, then μ(a,b)=φ(b)−φ(a).',
  'Derived on the pages from (13).',
  'Primitive calculation in proof_checks §2; compute_checks horizontal_arc_counterexample evaluates φ(b)−φ(a)=1 in the test below.',
  'E','Valid under the written assumptions. The endpoint difference need not vanish.',ED,[G,KO])
c(10,[212],'93',[227],'151-162','si a,b sont des sections horizontales … μ(a,b)=0',
  'The additional assertion that horizontality of both endpoints forces the Picard–Fuchs expression to vanish is false as transcribed.',
  'False as stated; no later correction of this sentence is visible.',
  'Counterexample: X=A¹_x×S with product integrable splitting, ω=dx, D=identity, a=0,b=1. The fibres are connected, ω is closed holomorphic, all cycle periods are zero, [ω]=0, both sections are horizontal, but μ(a,b)=1. Exact code/output: horizontal_arc_counterexample.',
  'C','The preceding valid statement is C-SA23-bt-009. Neither the published Gauss–Manin construction nor period annihilation gives endpoint vanishing; the error is independently refuted here. Scan checking is required to decide whether a missing extra condition or transcription issue caused the line.',GD,[G,KO])
c(11,[213],'93',[228],'164-176','Nous n’allons pas prouver (15) ici, et l’admettrons',
  'The Gauss–Manin action on a cohomology class is compatible with differentiation of its pairing against a locally constant fibre homology class, in the smooth complex setting where the de Rham comparison and local system exist.',
  'Explicitly admitted without proof.',
  'Independent primitive/Cartan check in proof_checks §2, with properness/local-triviality qualifications for the global local-system statement.',
  'A','Grothendieck §3.2, p.324 identifies the analytic horizontal sections with the locally constant cohomology sheaf; Katz–Oda §4, pp.211–213 compares the algebraic and analytic connections.',GD,[G,KO])
c(12,[215],'93',[229],'178-189','on peut supposer que … a,b sont horizontales',
  'Arbitrary intersecting holomorphic sections cannot always be made simultaneously horizontal for one connection.',
  'Reduction asserted; false without a condition on the sections.',
  'X=A¹_x×A¹_s, a(s)=0,b(s)=s. At s=0 both pass through x=0 but their tangent lifts of ∂s are ∂s and ∂s+∂x. A splitting gives one horizontal lift at that point, so cannot give both. Code block simultaneous_horizontal_obstruction.',
  'C','The reduction fails in this elementary example. The period identity can instead be proved directly using Cartan and endpoint corrections; published comparison sources do not require this simultaneous-horizontal assertion.',GD,[G,KO])
c(13,[216],'93',[229,230],'190-206','Il faut calculer les deux termes de droite',
  'The source leaves the moving-endpoint terms unfinished. Reconstruction: for a smooth one-parameter family of paths and closed relative form, the derivative equals the interior Lie-derivative contribution plus endpoint contractions with the vertical endpoint velocities; local primitives give the same formula.',
  'Open calculation on the pages; reconstructed here, not attributed to him as completed.',
  'Proof_checks §2 proves the first derivative formula. Exact polynomial example f(t,x)=tx²+t²x+1, a=t²,b=t+1 verifies Leibniz’s rule; code block endpoint_formula has symbolic difference zero.',
  'E','The missing first-order terms are standard differentiation under the integral sign/Cartan terms. Higher differential operators follow by iteration and bring further endpoint jets. This does not repair the written line by changing the transcription.',ED,[G,KO])
c(14,[218],'93',[230],'208-220','Cette … forme est encore fermée [deleted]',
  'A relatively closed form need not become an absolutely closed form on the base after a proposed pullback or endpoint construction; the text itself cancels the attempted argument.',
  'Withdrawn in the same text; false if retained without additional assumptions.',
  'X=A¹_x×A²_(s,t), ω=s dx is relatively closed; pullback by x=t gives s dt, whose exterior derivative is ds∧dt≠0. Code block relative_closed_pullback.',
  'C','The cancellation is mathematically justified. Relative and absolute differentials remain distinct in Grothendieck §3 and the de Rham-complex definition.',GD,[G,'bt_Stacks0FKL'])
c(15,[220],'93',[231],'229-240','une suite … formellement exacte … Diff^i(P,F)→Diff^(i+1)(P,G)→… exacte',
  'The asserted left-composition exactness with order bounds requires a definition of formal exactness and hypotheses on the orders of D,D′ and exactness of the relevant principal-parts complexes. They are not stated on the sheet.',
  'Stated without proof under an undefined quoted hypothesis.',
  'Type/order audit in proof_checks §3; first-order D,D′ are implicit in the displayed +1 shifts. No proof of an unspecified axiom is claimed.',
  'F','EGA IV₄ §16.8 and Grothendieck §6.2 supply the principal-parts representation and composition order, but the exact source hypothesis has not been identified. A general sheaf-exact complex does not by itself imply this assertion for every P.',GD,['bt_EGAIV4',G],'medium')
c(16,[220],'93',[231],'241-244','Diff^i(H,P)→Diff^(i+1)(G,P)→Diff^(i+2)(F,P) exacte',
  'Right-composition exactness for every P likewise needs a formally split/exact principal-parts condition sufficient for contravariant Hom to preserve the desired exactness. Ordinary exactness alone is insufficient.',
  'Stated without proof with the same undefined hypothesis.',
  'Contravariant-Hom and order-bound audit in proof_checks §3.',
  'F','The general formalizing machinery is published in Grothendieck §6.2–6.5, but neither the exact all-P finite-order condition nor its asserted implication can be recovered uniquely from the words on 231.',GD,[G,'bt_EGAIV4'],'medium')
c(17,[206,220,221],'93',[231],'245-259','lemme de Poincaré formel … S lisse … caractéristiques de T nulles',
  'For a smooth characteristic-zero formal neighbourhood with locally free stratified coefficients, the augmented relative de Rham complex satisfies the formal Poincaré lemma. Positive characteristic fails already for one formal coordinate without divided-power modifications.',
  'Assumed and given as a standard example.',
  'Formal-coordinate integration divides by positive integers; x^(p−1)dx in k[[x]] is closed and nonexact in characteristic p. Proof_checks §3 and characteristic_p_coefficient_check.',
  'A','Grothendieck §6.5, pp.349–350 proves the characteristic-zero formal Poincaré result and states the positive-characteristic obstruction. Exact order truncations remain governed by C-SA23-bt-015/016.',GD,[G])
c(18,[221,223],'93',[231,232],'251-271','Ker(Diff^i(E,P)→Hom(E,P)) … Diff^i_+(E,P)',
  'With the stratification section δ_i:E→P^i(E), Diff₊^i is the kernel of evaluation along δ_i. Under the displayed exact augmented complex it is the quotient of operators Ω¹(E)→P by those factoring through d¹ from Ω²(E), with the stated order bounds.',
  'Definition and conditional corollary.',
  'Kernel/cokernel argument in proof_checks §3; Ω² is type-forced for the preceding term, but retained as a reading alternative.',
  'C','Principal-parts representation and formal de Rham resolution establish this conditional interpretation. The word “constant” is not an assertion that all operator coefficients are scalar constants.',GD,[G,'bt_EGAIV4'])
c(19,[223],'93',[232],'269-277','hom naturel … injectif ?',
  'Assume the displayed quotient description and exactness. Restrict a representing Δ:Ω¹(E)→P to ker d¹. This is well-defined because additions Λd¹ vanish there; it is injective because if Δ vanishes on ker d¹ then D=Δd⁰=0, since d¹d⁰=0.',
  'Explicit injectivity question on the page; discharged conditionally by a short argument.',
  'Independent proof in proof_checks §3. No stronger surjectivity statement is asserted.',
  'E','The injection follows formally once the preceding presentation is granted; no separate unresolved research problem remains in that conditional formulation. The unresolved part is the earlier finite-order formal-exactness premise.',ED,[G,'bt_EGAIV4'])
c(20,[224],'93',[232,233],'279-309','P^(i)(E)/Oδ_i(E); Φ_i=P^i(M)/Oρ_i(E)',
  'Differential operators of order ≤i from M=E/N to P whose pullback to E has zero augmentation are represented by Φ_i=P^i(M)/O_Sρ_i(E), where ρ_i is induced by the stratification. The analogous formula for E is the case N=0.',
  'Construction asserted and explained.',
  'Universal-property proof in proof_checks §3: Hom out of a quotient imposes precisely annihilation of the indicated submodule. Transition maps are surjective because principal-parts truncations are surjective and the submodules are compatible.',
  'A','EGA IV₄ §16.8.1–16.8.4 gives the differential-operator/principal-parts dictionary; Grothendieck §6.2, pp.345–348 uses this formalization. The quotient assertion is an elementary consequence, not an independent classification theorem.',GD,['bt_EGAIV4',G])
c(21,[225],'93',[233],'301-313','syst. projectif strict … conditions d’intégrabilité',
  'The displayed Φ_i form a surjective inverse system; ρ∞ has surjective augmentation E→M. Reconstructing a stratification from an arbitrary map E→P∞(M) requires additional cocycle/integrability conditions, which the source does not write.',
  'Strictness asserted; integrability requirements explicitly left unspecified.',
  'Surjectivity proved in proof_checks §3. No arbitrary pro-map is upgraded to a stratification.',
  'C','Grothendieck’s Appendix, pp.356–357, supplies the general diagonal cocycle definition of stratification and the characteristic-zero integrable-connection equivalence. It does not by itself identify the complete necessary-and-sufficient axioms for this particular quotient presentation.',GD,[G])
c(22,[226],'93',[234],'316-375','loc. T-isom (sur X₀); torseur sous G',
  'For smooth T-schemes X′,X″ with identified reduction over a square-zero thickening T₀⊂T, their local T-isomorphisms inducing the identity on X₀ form a torsor under the additive sheaf of T-derivations of O_X₀ with values in I O_X₀ (equivalently Hom(Ω¹_X₀/T₀,I O_X₀)). Local existence uses smoothness.',
  'Construction asserted and motivated.',
  'Proof_checks §4: differences of lifts are derivations, composition is addition because I²=0, inverse id−δ, and formal smoothness gives local lifts.',
  'A','Grothendieck §3.4, pp.326–329 contains this exact square-zero torsor construction. Stacks 01UP supplies the square-zero difference-of-maps identity.',GD,[G,'bt_Stacks01UP'])
c(23,[227],'93',[234,235],'365-397','u(pg)=u(p)v(g); u,v and k in the abstract setup',
  'The geometric multiplicative formula for a torsor of isomorphisms becomes the additive Hom-complex relation u(p+g)−u(p)=d_Hom k(g). The abstract paragraph cannot simultaneously treat u as an arbitrary additive map and retain the multiplicative expression without specifying actions.',
  'Ill-typed/mixed notation in the transcription; corrected formulation is our reconstruction.',
  'Proof_checks §4 derives the additive relation and checks d_Hom k=d k+k d in cohomological degree −1.',
  'A','The exact published counterpart, Grothendieck §3.4, uses the additive relation and additive θ. It resolves the mathematical reconstruction but does not decide the archival ink.',GD,[G])
c(24,[229],'93',[235],'399-412','0→G→Ḡ→Z→0; j⁻¹(1)≃P',
  'An additive sheaf G and G-torsor P determine an extension 0→G→Ḡ→Z→0 whose degree-one fibre is P. One construction is (G⊕Z[P]) modulo [p+g]−[p]−g; locally choosing p gives Ḡ≅G⊕Z.',
  'Construction stated without full quotient proof.',
  'Independent quotient/local-gluing proof in proof_checks §4; a local section changes the splitting but not the extension.',
  'A','Grothendieck §3.4 uses precisely the extension; Stacks 03AJ gives the torsor/H¹ construction. The local quotient proof checks the concrete assertion.',GD,[G,'bt_Stacks03AJ'])
c(25,[228,230],'93',[235,236],'414-432','L⁰,L¹ … later φ⁻¹,φ⁰',
  'The complex L=[G→Ḡ] resolving Z must be placed in cohomological degrees −1,0 for the displayed augmentation and roof. The earlier 0,1 labels conflict with the following formulas.',
  'Degree conflict within the transcription, with later formulas giving the consistent convention.',
  'Locally L≅Z[0]⊕[G→G] with the latter contractible. Therefore L⊗K′→K′ is a quasi-isomorphism for every K′, with no flatness assumption needed. Proof_checks §4.',
  'A','Grothendieck §3.4 has the degree −1,0 resolution. This determines the valid mathematical statement, not whether the source contains a slip or a transcription error.',GD,[G])
c(26,[230,231],'93',[235,236],'399-444','un hom de la cat. dérivée',
  'Given the torsor P, the maps u(p):K′→K″, and an additive degree −1 homotopy k satisfying C-SA23-bt-023, one obtains the roof K′←Tot(L⊗K′)→K″. The construction depends on the homotopy data, not merely on the pointwise homotopy classes.',
  'Construction sketched.',
  'Proof_checks §4 checks well-definedness of the chain map and the locally contractible resolution. All tensor operations are over the coefficient ring in which the complexes and homotopies are linear.',
  'A','Grothendieck §3.4, pp.327–329 is an exact published counterpart. It includes transitivity when the compatible geometric data are composed.',GD,[G])
c(27,[231],'93',[235,236],'384-444','h|k [homotopy choice in the abstract construction]',
  'Earlier-run caution, not an asserted manuscript theorem: the resulting derived morphism need not be independent of a change in k. The torsor class can couple to a degree −1 map to change the derived morphism.',
  'Reader’s implication check; no blanket k-independence is stated on the pages.',
  'Proof_checks §4 gives X=S¹, constant G=Z, a nontrivial Z-torsor, K′=Z[0], K″=Z[1], u=0. k=0 gives zero; k=id gives the nonzero torsor class in H¹(S¹,Z).',
  'E','Standard torsor/Ext interpretation confirms dependence. Published geometric canonicity uses a specified contraction and compatibility, and is not a theorem that arbitrary k choices give the same roof.',ED,[G,'bt_Stacks03AJ','bt_Stacks08J7'])
c(28,[232],'93',[236],'445-450','O_X ≃ R Hom(K′,K″)',
  'The displayed universal identification of the coefficient sheaf with derived Hom is false for arbitrary complexes; the construction only needs a morphism from the coefficient unit to the Hom complex/derived Hom.',
  'False as transcribed in the abstract generality.',
  'Point X=Spec k, K′=K″=k² in degree zero: RHom=Mat₂(k) has dimension 4 while k has dimension 1. Code block derived_Hom_counterexample.',
  'A','Grothendieck §3.4 has the needed morphism into ordinary Hom followed by the natural map to derived Hom, not this universal isomorphism. It is the exact published repair, with archival sign/arrow still left for scan checking.',GD,[G,'bt_Stacks08J7'])
c(29,[233],'93',[236],'445-460','Tensorisant avec O_X … R Hom',
  'There is a natural ordinary-Hom-to-derived-Hom morphism; it need not be an isomorphism without resolutions. For relative de Rham complexes the differential is base-linear, generally not O_X-linear, so the derived category and tensor/Hom coefficient sheaf must be specified accordingly.',
  'Coefficient category and replacement choices compressed on the pages.',
  'Proof_checks §4: d(fα)=df∧α+f dα excludes O_X-linearity; K-injective replacement defines the comparison. No unsupported K-flat assertion is used.',
  'A','Grothendieck §1.3, §3.4 specifies the base-ring coefficient setting; Stacks 08J7 and 0FKL give the modern Hom/de Rham definitions.',GD,[G,'bt_Stacks08J7','bt_Stacks0FKL'])
c(30,[234],'93',[234],'365-375','v(g)−id=dk(g)+k(g)d',
  'For a square-zero infinitesimal automorphism id+δ inducing the identity on X₀, its action on relative forms differs from the identity by dι_δ+ι_δd. Products involving two I-factors vanish; contraction is additive and kills the I-multiple subcomplex.',
  'Cartan homotopy asserted.',
  'Proof_checks §4 verifies on f and df and extends by graded Leibniz. Terms with two I-factors vanish because I comes from the base and I²=0, so d_rel I=0.',
  'A','Grothendieck §3.4 explicitly uses this square-zero Cartan homotopy to make the descent construction.',GD,[G])
c(31,[235,277],'93',[234,235,236],'316-460','Construction de la connexion canonique en cohomologie de De Rham',
  'The compatible square-zero local comparisons induce a canonical, transitive derived comparison between smooth lifts of a fixed reduction, and hence the first-order cohomological connection. This alone is not an equivalence of every integral crystal category across arbitrary nilpotent thickenings.',
  'Construction sketched under square-zero smoothness.',
  'Proof_checks §4 checks identity and composition using additivity of contraction and I²=0; local chain maps are isomorphisms, hence the descended derived map is an isomorphism.',
  'A','Grothendieck §3.4 gives the exact derived construction, transitivity and application of Rf_*. §3.5, p.330 explains why ordinary higher stratification cannot be asserted indiscriminately in positive characteristic.',GD,[G])

# The following claims belong to Serre’s printed offprint and course summary,
# not to an unpublished theorem newly attributed to Grothendieck.
c(32,[237],'161-5',[5],'499-503','exponentielle … sur un sous-groupe ouvert de G',
  'For a compact subgroup G⊂GL(V) over Q_p, G is a p-adic Lie group and exponential with the Campbell–Hausdorff law identifies a sufficiently small neighbourhood in Lie(G) with an open subgroup.',
  'Carried as known with a reference.',
  'Carried as background; no independent convergence proof of exponential/BCH is claimed.',
  'E','Classical p-adic Lie fact used in Serre §1. It is not a new conjecture in this archive.',ED,[S])
c(33,[237],'161-5',[5],'505-521','Proposition 1: (a)⇔(b)⇔(c)',
  'For compact G⊂GL(V), V is semisimple for G iff it is semisimple for Lie(G), iff Lie(G) is reductive and its centre acts semisimply. The centre condition must not be dropped.',
  'Proof supplied, with a standard Lie-algebra reference.',
  'Proof_checks §5 checks passage to a small open normal subgroup and finite-index averaging in characteristic zero; the reductive Lie representation theorem is carried as background.',
  'E','Established in the printed Proposition 1; the exact centre qualification is retained.',SD,[S])
c(34,[237],'161-5',[5],'523-531','enveloppe algébrique … existence et unicité',
  'For any subgroup G⊂GL(V)(Q_p), its Zariski closure is the smallest algebraic subgroup containing G; it is defined by regular functions vanishing on G. Semisimplicity is not needed for existence.',
  'Construction proved in one paragraph.',
  'Proof_checks §5 checks closure under group multiplication/inverse by the Hopf ideal argument.',
  'E','Standard algebraic closure construction, correctly distinguished from the reductivity claims that follow.',ED,[S,MI])
c(35,[237],'161-5',[6],'533-551','Proposition 2 (i)–(iii)',
  'Under semisimplicity of V, Lie(G_alg)=the algebraic envelope of Lie(G), G_alg is reductive, and every connected component of G_alg meets G. The assertion includes disconnected algebraic groups.',
  'Proof supplied by finite cosets of a connected algebraic subgroup.',
  'Proof_checks §5 checks the finite-coset construction H=⋃H⁰g_i and the normalizing action; standard algebraicity of the semisimple Lie part is background.',
  'E','Printed Proposition 2 proves the statement; later Hodge–Tate theorems add algebraicity of the centre rather than removing component groups.',SD,[S,S79])
c(36,[237],'161-5',[6],'553-556','Si c est algébrique … G est … ouvert',
  'If the centre c of Lie(G) is algebraic under the preceding semisimplicity hypotheses, then Lie(G)=Lie(G_alg) and G is open in G_alg(Q_p).',
  'Proved as a corollary.',
  'Equal Lie algebras imply equality of sufficiently small exponential neighbourhoods; uses C-SA23-bt-032.',
  'E','Valid printed corollary; it does not say an arbitrary compact subgroup is open in its algebraic envelope.',SD,[S])
c(37,[238],'161-5',[6,7],'558-581','Proposition 3; Lemme 1 … déterminé par ses invariants tensoriels',
  'For a reductive algebraic H⊂GL(V) in characteristic zero, H is the stabilizer of all H-fixed mixed tensors in V and V*. Hence G_alg(k) for every commutative Q_p-algebra k is characterized by fixing all G-invariant mixed tensors. Reductivity and all tensor degrees are part of the claim.',
  'Lemma proof sketched; Proposition 3 deduced.',
  'Proof_checks §5 checks determinant correction V⊕det(V)*, separation of disjoint closed H-orbits by invariant polynomials, and polarization in characteristic zero. The all-k statement uses equality of closed subgroup schemes, not merely a pointwise slogan.',
  'E','Serre explicitly calls the invariant theorem known. The printed proof gives the appropriate reductive scope; modern Tannakian sources recover the same stabilizer principle.',ED,[S,MI])
c(38,[239],'161-5',[8],'591-631','Proposition 4: ⊕ X(i)⊗_K C → X injectif',
  'For complete discretely valued mixed-characteristic K with perfect residue field, C=completion of an algebraic closure, and a finite-dimensional continuous semilinear C-representation X, the natural sum of cyclotomic eigenspaces tensored to C maps injectively to X; Hodge–Tate means it is an isomorphism. Weights follow the source’s s(x)=χ(s)^i x convention.',
  'Minimal-relation proof supplied, using Tate’s invariant/eigenspace theorem as input.',
  'Targeted proof check of the minimal linear relation: normalize one coefficient, apply Galois and subtract; minimality forces the other coefficients to transform by the relative character. Tate’s vanishing of nonzero character eigenspaces in C and C^G_K=K are deep background inputs, not re-proved here.',
  'B','Established Tate Hodge–Tate theory, used by Serre Proposition 4; the exact formulation is read in the attached primary source. No conversion to the opposite modern twist sign is made silently.',SD,[S,'bt_FontaineOuyang'])
c(39,[239,257],'161-5',[8],'634-639','dual … produit tensoriel … la vérification est immédiate',
  'Hodge–Tate representations are closed under dual and tensor product; the weights of the dual are negated and tensor weights add, in the source’s convention.',
  'Immediate verification asserted.',
  'Proof_checks §5 expands the direct-sum decompositions over C, takes duals/tensors, and checks the semilinear action on each summand.',
  'E','Valid tensor identities; they do not say the subcategory with weights only 0 and 1 is itself rigid tensor closed.',ED,[S,'bt_FontaineOuyang'])
c(40,[239,247],'161-5',[9],'641-677','Théorème 1; Théorème 2: M⊂G_alg',
  'For a semisimple Hodge–Tate V, the Hodge cocharacter over C belongs to G_alg,C because it fixes all invariant tensors. The smallest Q_p-algebraic subgroup M whose base change contains that cocharacter is contained in G_alg.',
  'Proof supplied using the invariant characterization.',
  'Proof_checks §5: invariant tensors have weight zero; apply C-SA23-bt-037 and take the smallest Q_p-defined algebraic subgroup.',
  'B','Printed Theorems 1–2 establish the assertion. Later Sen/Serre results identify the connected inertia envelope, not every finite component.',SD,[S,S79,'bt_Sen1973'])
c(41,[237,247],'161-5',[10],'679-691','M est connexe; M⊂I_alg',
  'The group generated algebraically by the conjugates of a connected Hodge torus is connected, and M lies in the algebraic envelope of inertia. The passage to completed maximal unramified K is used to obtain the latter inclusion.',
  'Connectedness and inclusion proved; equality is a handwritten later annotation.',
  'Proof_checks §5 checks connected generation; the semilinear extension-to-completed-unramified-field theorem is carried as background.',
  'B','Serre §3 proves the inclusion. Sen’s theorem, as formulated in Serre 1979 under algebraically closed residue field, gives the neutral-component identification. Finite inertia components must be retained separately.', 'Printed 1967; Sen 1973; Serre’s expanded account 1979.',[S,S79,'bt_Sen1973'])
c(42,[247],'161-5',[10],'690','M=I_alg (Sen)',
  'The marginal equality without a neutral-component qualification is false for general semisimple Hodge–Tate representations.',
  'False as a literal unrestricted annotation.',
  'K=Q_3, V the ramified quadratic character from Q_3(√3)/Q_3. It becomes trivial over a finite extension, is Hodge–Tate of weight 0 and semisimple; M=1, while inertia image and its algebraic envelope are μ₂. Proof_checks §5 verifies every hypothesis.',
  'C','The correct comparison is with the connected inertia envelope (or its Lie algebra). Serre 1979 Theorem 2, p.159 and Corollary 3 expressly keep the connected group. Finite characters refute the stronger handwritten formula.', 'Sen publication 1973; precise later exposition 1979; first circulation not established.',[S79,'bt_Sen1973'])
c(43,[240],'161-5',[10],'693-719','H*.1–H*.3; Théorème 3',
  'If V is absolutely irreducible for Lie(G), Hodge–Tate with precisely weights 0 and 1 of positive coprime multiplicities n₀,n₁, then Lie(G)=End_Qp(V) and G is open in GL(V)(Q_p).',
  'Proved via Proposition 5.',
  'Proof_checks §6 checks reduction to the connected envelope and the group-theoretic Proposition 5; positivity excludes the degenerate one-weight case.',
  'B','Serre’s printed Theorem 3 establishes it. It is an open-image theorem with strong irreducibility and coprimality hypotheses, not a theorem for every two-weight representation.',SD,[S,S79])
c(44,[240],'161-5',[11,12,13],'721-815','Proposition 5: H=GL_V',
  'Over an algebraically closed field of characteristic zero, a connected reductive subgroup H⊂GL(V) with scalar commutant and containing a two-weight cocharacter of positive coprime multiplicities equals GL(V).',
  'Proof supplied across 11–13.',
  'Proof_checks §6 reconstructs derived-group irreducibility, positive Laurent-character factorization, the determinant-one cocharacter and the central-order test; code checks the arithmetic and exceptional dimensions.',
  'B','Printed Proposition 5 and Lemma 2 prove this exact group-theoretic criterion. Later classification in Serre 1979 is broader but not needed for the proof.',SD,[S,MI])
c(45,[240],'161-5',[11,12],'736-788','ψ(t)|V₀=t^n₁; ψ(t)|V₁=t^(−n₀); factorisation de F',
  'With h=n₀+n₁ and gcd(n₀,n₁)=1, ψ has determinant one and maps h-th roots of unity onto scalar μ_h. A product of positive-coefficient Laurent polynomials can have exactly two monomials only when all but at most one factor are monomials; coprimality of the two coefficients forces the other representation dimensions to be one.',
  'Computations used in the Proposition 5 proof.',
  'Proof_checks §6 gives the general support argument. Code blocks determinant_cocharacter and positive_binomial_factor_sample check determinant/gcd examples and bounded finite enumeration, explicitly supplementary rather than a proof of the universal assertion.',
  'E','The computation is correct. The proof uses nonnegative coefficients; arbitrary Laurent polynomials with cancellation would not satisfy the same inference.',SD,[S])
c(46,[240],'161-5',[12,13],'777-815','Lemme 2: S=SL_V',
  'For the simple connected semisimple group in this irreducible faithful h-dimensional representation, the presence of scalar μ_h forces S=SL_h. The root-system centre bounds exclude other types, with E₆ and D₄ eliminated by dimension.',
  'Proof by classification supplied.',
  'Cartan-matrix/root enumeration gives D₄:24 roots,dimension28,centre order4; E₆:72 roots,dimension78,centre order3; E₇:126,133,2; E₈:240,248,1. Compare D₄ dimension28>dim SL₄=15 and E₆ dimension78>dim SL₃=8. Code block simply_laced_classification_checks and proof_checks §6.',
  'E','The classification argument is valid with the faithful representation and centre-order assumptions. Milne §24c supplies an opened modern centre table; printed Serre gives the exact proof being checked.',ED,[S,MI])
c(47,[239,241],'161-5',[13],'807-815','Proposition 6: V(F) … n₁=dim F; n₀=dim F′',
  'For a p-divisible group F over the valuation ring A in Serre’s mixed-characteristic perfect-residue setting, its rational covariant Tate module is Hodge–Tate, with weights 0 and 1 of multiplicities dim(F^∨) and dim(F) respectively.',
  'Tate’s theorem stated and cited.',
  'Convention audit against the printed action and Liu Remark 2.2.5; no proof of the comparison theorem is claimed.',
  'B','Established Tate comparison; modern all-prime BT/crystalline correspondence in Liu Theorem 2.2.1 includes p=2 under its finite totally ramified K/K₀ hypotheses. The covariant normalization is preserved.',SD,[S,'bt_Liu2013'])
c(48,[241],'161-5',[14],'816-839','Proposition 7: commutant … End_A(F); End(F)',
  'The commutant of the Galois image on T_pF is End_A(F), and rationally End_A(F)⊗Q_p. The commutant of the Lie algebra is the rational endomorphism algebra after allowing finite base-field extensions. Integral and rational statements and the geometric End convention must be separated.',
  'Proof supplied using Tate full faithfulness and open subgroups.',
  'Proof_checks §7 checks the passage from Lie-invariance to an open subgroup and finite extension; deep Tate full faithfulness is carried as background.',
  'B','Printed Proposition 7; modern BT equivalence supplies full faithfulness in the stated finite-ramification setting. End(F)=union over finite extensions is essential for the Lie-algebra statement.',SD,[S,'bt_Liu2013'])
c(49,[240,241],'161-5',[14],'841-856','Théorème 4',
  'For V(F) semisimple, geometric End(F)=Z_p, and dim F,dim F^∨ positive and coprime, G is open in GL(V(F)); F and its dual are connected. The endomorphism hypothesis is geometric, not merely over the original A.',
  'Proof supplied using Proposition 7 and Theorem 3.',
  'Proof_checks §7 checks absolute irreducibility from semisimplicity and scalar commutant, then applies C-SA23-bt-043. Connectedness follows because an étale quotient would produce a nonzero inertia-trivial part inconsistent with full Lie algebra.',
  'B','Established in the printed Theorem 4 with the written hypotheses. It cannot be promoted to arbitrary BT groups.',SD,[S])
c(50,[242,243],'161-5',[14,15,16],'850-918','Proposition 8: g·z=V pour z≠0',
  'For a one-dimensional finite-height formal group over A, each nonzero z in its rational Tate module satisfies Lie(G)·z=V. The proof counts sufficiently many torsion conjugates using the ramification lower bound of Lemma 3.',
  'Proof completed after a temporarily admitted lemma.',
  'Proof_checks §7 checks the orbit-dimension contradiction: a d-dimensional p-adic orbit has O(p^(nd)) reductions, whereas primitive p^n torsion has ramification degree at least c p^(nh); hence d≥h=dim V.',
  'B','Printed Proposition 8 is proved on these pages; it is not an unresolved lemma merely because its proof is deferred by one page.',SD,[S])
c(51,[242,243],'161-5',[15,16],'858-918','Lemme 3 … e≥cp^(nh); φ(α)=min(p^hα,α+c₁)',
  'For a one-parameter finite-height h formal group and primitive p^n-torsion point x, the ramification index of K(x)/K is bounded below by c p^(nh), with c>0 independent of n. The valuation equality in the iterative proof holds strictly below c₁/(p^h−1), not at the boundary.',
  'Admitted temporarily on 15, proved by the end of 16.',
  'Proof_checks §7 checks valuation bounds, ψ(t)=max(t/p^h,t−c₁), eventual geometric decay of d_n and e≥c p^(nh). Code valuation_recurrence_example gives exact rational iterates; strict_boundary_example uses p=2 formal G_m, x=−2: v(x)=1=c₁/(2−1) but [2]x=0.',
  'B','The complete printed proof settles the provisional admission. The strict inequality is necessary and must not be silently weakened in transcription.',SD,[S])
c(52,[240,244],'161-5',[16],'920-928','Théorème 5: End(F)=Z_p ⇒ G ouvert',
  'For a one-dimensional finite-height formal group with geometric End(F)=Z_p, the Galois image is open in GL(V). Proposition 8 supplies irreducibility and the preceding endomorphism/group criterion supplies the conclusion.',
  'Proved from preceding results.',
  'Proof_checks §7 checks the dependence on geometric End and finite height; uses C-SA23-bt-049/050.',
  'B','Printed Theorem 5 establishes the result. The more general centralizer equality immediately following it is a separate claim.',SD,[S])
c(53,[244],'161-5',[16],'925-928','plus généralement … g est le commutant de End(F)',
  'For the one-dimensional formal-group setting, the Lie algebra is asserted to be the centralizer of the geometric endomorphism algebra; the proof is omitted. This is stronger than the scalar-endomorphism open-image special case.',
  'Stated without proof; later Sen annotation.',
  'No independent proof of Sen’s theorem is claimed. Exact scope checked in the printed sentence and in Sahu §3, Lemma 3.7/Proposition 3.8, including its formal-module and centralizer hypotheses.',
  'B','Sen’s 1973 Theorem 3 is explicitly credited in the opened later formal-group exposition. Sahu’s particular application assumes its good formal-module hypotheses; it is evidence for the attribution and mechanism, not a license to drop all hypotheses or a claim that Sen’s original proof was read.', 'Sen published 1973; first circulation unavailable in opened evidence; later explicit exposition arXiv v4 25 October 2019.',[S,'bt_Sen1973','bt_Sahu2019'],'medium')
c(54,[245],'161-5',[16,17],'929-937','inertie … sous-groupe ouvert; pas de démonstration directe',
  'In the formal-group setting, the inertia image has the same Lie algebra as the full Galois image and hence is open. Serre asks for a direct proof, while giving an indirect proof via base change to the completed maximal unramified extension.',
  'Theorem proved indirectly; methodological request remains.',
  'Proof_checks §7 tracks the base change and preservation of geometric endomorphisms. The comparison facts used by the printed proof are carried as background.',
  'B','The mathematical openness is established on the page and later by Sen’s Lie theory. The opened sources do not identify a uniquely designated “direct” proof answering Serre’s stylistic request; that is not an unsettled truth-value.',SD,[S,'bt_Sen1973','bt_FontaineOuyang'])
c(55,[246],'161-5',[17],'939-954','w=e_K v+O(1)?',
  'For a totally ramified p-adic Lie extension of a complete discretely valued mixed-characteristic field K with perfect residue field, the upper ramification filtration and a p-power Lie filtration are commensurable with bounded shifts: G^(ne+c)⊂G(n)⊂G^(ne−c), where e=v_K(p), after choosing a standard compatible Lie filtration.',
  'Explicit question; later annotation “Sen”.',
  'Hypotheses and exact inequalities read in Fontaine–Ouyang A.4.1/Theorem A.85, pp.197–200. No independent proof of Sen’s deep ramification theorem is claimed.',
  'B','Sen’s 1972 ramification theorem gives the bounded linear comparison. Gross 1979 discusses its mixed-characteristic setting; equal-characteristic analogies require separate qualifications.', 'Published 1972; first circulation not established. Gross exposition 1979; Fontaine–Ouyang manuscript undated.', ['bt_Sen1972','bt_Gross1979','bt_FontaineOuyang'])
c(56,[248],'161-5',[19,20],'1007-1041','pour tout module de Hodge-Tate … G ouvert dans H(Q_p)',
  'In the course’s standing setting with algebraically closed residue field, the image of a Hodge–Tate representation is open in its algebraic envelope, equivalently the Lie algebra is algebraic. The residue-field hypothesis is explicit and indispensable to this wording.',
  'Course theorem stated.',
  'Scope audit against Serre 1979 §1.1 and Theorem 1. For finite-residue K, an infinite unramified weight-zero character already refutes the finite-image consequence; a two-dimensional unramified representation with a one-dimensional nonalgebraic torus Lie algebra also refutes an unrestricted open-envelope statement. Details and scope in proof_checks §5.',
  'B','Serre 1979 Theorem 1, p.158 gives the precise established result, with algebraically closed residue field stated on p.156.', 'Courses 1967–68; Annuaire 1968–69; expanded published account 1979.',[S79,'bt_SerreCourses1968'])
c(57,[248],'161-5',[20],'1031-1046','H⁰ contient h(G_m); cas résoluble; Il est probable …; poids0 ⇒ fini',
  'Under the same algebraically closed-residue hypothesis, the neutral component contains the Hodge cocharacter. The course states that it is the smallest Q_p-defined group containing that cocharacter when the image is solvable, and conjectures the same without solvability; the general result implies that a weight-zero Hodge–Tate representation has finite image.',
  'Containment and the solvable case are stated as known in the course summary; the general characterization is conjectural, with a later Sen annotation.',
  'Connected-component qualification checked; C-SA23-bt-042 supplies the finite-character boundary. No claim that H⁰ equals the full disconnected envelope.',
  'B','Serre 1979 Theorem 2 and Corollary 3, pp.159–160 state the established result and credit Sen. For general local fields the corresponding conclusion concerns inertia, and weight zero need not mean finite full image.', 'Sen 1973; expanded Serre account 1979; first circulation not established.',[S79,'bt_Sen1973'])
c(58,[249,262],'161-5',[20,23],'1047-1050,1151-1162','H/H⁰ … Gal; G/G⁰ non tordu',
  'The inverse limit of the finite-dimensional algebraic envelopes is the Tannakian proalgebraic group H, and the Hodge–Tate category is equivalent to its finite-dimensional representation category. It has a profinite component quotient arising from finite Galois representations; finite extension does not alter the appropriate connected component. The handwritten “non twisted” wording must be read in that neutral Q_p-fibre-functor context.',
  'Course construction stated; later handwritten compressed reminder.',
  'Proof_checks §8 notes that all finite continuous representations are Hodge–Tate weight zero and that finite component data are distinct from the connected group.',
  'B','Serre 1979 §1–2 develops the proalgebraic envelope with its component and connected data; the course’s algebraically closed-residue context is retained. No universal motivic group is identified from the word “envelope”.', 'Course 1967–68, printed Annuaire 1968–69; expanded exposition 1979.',[S79,'bt_SerreCourses1968'])
c(59,[249],'161-5',[20,29],'1051-1056,1521-1528','Θ=lim T_E; T_E(Q_p)=E*',
  'In the course’s local setting, the maximal abelian quotient of the connected universal Hodge–Tate group is the indicated inverse limit of restriction-of-scalars tori, independent of K and depending only on p in the stated setting, with transition morphisms and embeddings supplied by the construction; T_E(Q_p)=E× is the defining functor-of-points identity.',
  'Theorem stated in the course summary; torus reused on 29.',
  'Restriction-of-scalars point calculation independently checked in proof_checks §10; no collapse of the protorus to a single torus.',
  'B','Serre 1979 §2.4 Theorem 6, p.174 gives the connected abelianization/protorus result. The lower diagram on 29 is not identified with that theorem merely by the same torus notation.', 'Courses 1967–68; expanded publication 1979.',[S79])
c(60,[258],'161-5',[21],'1060-1068','si n₁=1 … commutant … corps E; H⁰=Aut_E V',
  'In the course’s two-weight, simple-module setting with n₁=1, the commutant of H⁰ is a commutative field E and H⁰ is the full E-linear automorphism group; therefore the Galois image is open in that group under the standing local-field hypotheses.',
  'Result stated without proof in the summary.',
  'Scope checked against the preceding simplicity and weight conditions; no independent complete proof of this classification corollary is claimed.',
  'B','Serre 1979 §3.1–3.3 gives the representation-theoretic framework and classical/minuscule restrictions. The exact source result is an already printed course assertion, not an original new conjecture; its abbreviated hypothesis list must be retained.', 'Course 1967–68, Annuaire 1968–69; expanded classification 1979.',[S79,'bt_SerreCourses1968'],'medium')
c(61,[250,251],'161-5',[21],'1069-1077','classer … n’ayant que deux poids; Springer … alg. de Jordan',
  'Classify connected reductive groups with the relevant faithful/simple representation and a two-weight cocharacter. The algebraic classification is distinct from realizing every possibility as the Galois group of a p-divisible group.',
  'Classification programme stated; later note points to Springer’s Jordan-algebra book.',
  'Code End_weight_decomposition checks the induced End(V) degrees −1,0,1. This yields a Jordan pair through double brackets, not automatically a unital Jordan algebra.',
  'B','Serre 1979 §3.2–3.3, pp.175–185 proves classical/minuscule restrictions, Theorem 7 p.184; p.182 cites Springer §11, and p.185 expressly leaves realization questions separate. Springer’s 1973 edition is verified via that bibliography; the opened publisher page is a later reprint.', 'Springer first edition 1973; Serre expanded classification 1979. Reprint metadata 1998 is not the first edition.',[S79,'bt_Springer1973','bt_BertramNeeb2003'])
c(62,[252],'161-5',[21],'1078-1083','Raynaud … pleine fidélité … possible … égale caractéristique',
  'For p-divisible groups over a complete valuation ring, generic-fibre full faithfulness is known in mixed characteristic; the course asks for an equal-characteristic analogue. A precise later theorem extends Hom uniquely from the fraction field of an integrally closed Noetherian integral domain.',
  'Mixed-characteristic result reported; equal-characteristic hope.',
  'Exact quantifiers read in de Jong ICM 1998 Theorem 2, p.261, and the one-page 1999 erratum checked for impact. No stronger nonnormal-base statement inferred.',
  'B','De Jong proves generic-fibre full faithfulness in positive characteristic in the stated normal Noetherian integral setting. The 1999 erratum corrects Lemma 2.1(iii) and the semistable-reduction definition, explicitly requiring no other changes; it does not withdraw the Hom theorem.', 'Paper submitted 5 December 1995, revised 14 November 1997, published October 1998. Erratum received 16 April 1999, online 6 July 1999, issue October 1999; 2018 is later digitization metadata.', ['bt_deJong1998','bt_deJongICM1998','bt_deJongErratum1999'])
c(63,[253],'161-5',[21],'1082-1086','difficultés techniques … pas été entièrement résolues',
  'Serre distinguishes the already known Serre–Tate deformation theorem from technical gaps in the proposed proof through p-divisible groups. The standard theorem identifies deformations of an abelian scheme with compatible deformations of its p-divisible group over a nilpotent thickening with p nilpotent.',
  'Theorem known; proposed proof method not completed in the course.',
  'Katz 1981 Theorem 1.2.1, p.143 read with p-nilpotent base R and nilpotent ideal I; equivalence is of triples including the special-fibre identification. No theorem for arbitrary nonnilpotent thickenings claimed.',
  'B','Katz gives Drinfeld’s proof of the precise deformation equivalence. Serre 1979 p.188 points to Messing’s 1972 crystalline proof. Messing’s chapter metadata was opened, but its full proof was not read in this run.', 'Serre–Tate theorem reported as 1964 in the source; Messing publication 1972; Katz publication 1981. First public circulation of the Katz/Drinfeld proof not established.', ['bt_Katz1981','bt_Messing1972',S79])
c(64,[254],'161-5',[22],'1088-1105','relèvement canonique des variétés abéliennes ordinaires',
  'For an ordinary abelian variety over an algebraically closed perfect field k of characteristic p, Serre–Tate deformation parameters form a formal torus and the identity parameter gives the canonical lift; compatible finite-level lifts give the lift over W(k).',
  'Course construction and arithmetic applications reported.',
  'Katz Theorem 2.1, pp.148–149 and canonical parameter q=1 checked; ordinary and base hypotheses are retained.',
  'B','Established ordinary Serre–Tate theory. The course’s Hasse/complex-multiplication comments are context, not a new proof of every CM lifting assertion.', 'Course 1967–68; precise opened exposition Katz 1981; earlier first circulation not established here.', ['bt_Katz1981','bt_SerreCourses1968'])
c(65,[260,261,278],'161-5',[23],'1137-1144','Foncteur pl. fid (par Tate)',
  'The rational covariant Tate functor embeds p-divisible groups over V up to isogeny fully faithfully into Hodge–Tate representations with source weights 0 and 1. It is not essentially surjective onto all such Hodge–Tate representations.',
  'Full faithfulness stated; no essential-surjectivity theorem written.',
  'Compare C-SA23-bt-047/048 and the explicit Tate-curve counterexample C-SA23-bt-066.',
  'B','Liu Theorem 2.2.1 identifies the integral essential image with lattices in crystalline representations of the indicated weights in its finite totally ramified setting, all p including 2. Hodge–Tate is a weaker condition.', 'Tate theorem used in the 1966/1967 offprint; modern all-prime formulation published 2013, received 11 June 2012.', ['bt_Liu2013','bt_Gunton2021',S])
c(66,[261,268,279],'161-5',[23,24],'1145,1200-1202','M^BT … engendrée par M_K^(1)',
  'The literal category generated by all weight-{0,1} Hodge–Tate objects is larger than the category generated by the actual BT image. A Tate elliptic curve over a p-adic local field with v(q)>0 has Hodge–Tate Tate module of these weights but is not crystalline, hence is not the Tate module of a BT group over the valuation ring.',
  'Definition on the page; mismatch with the label exposed by a present/earlier-run check.',
  'Every counterexample hypothesis matched to Gunton §1.2 and Example 3.4, with covariant sign convention matched to Liu Remark 2.2.5. No claim that this forbids every abstract tensor functor of some other kind.',
  'C','Standard crystalline period functors solve the natural BT-generated version, not automatically the literal larger category. This generator ambiguity is decisive for the extension question and must be settled on the ink or by an explicitly different problem formulation.', 'Modern explicit opened example Gunton 2021; not assigned an invented first historical date.', ['bt_Gunton2021','bt_Liu2013'])
c(67,[262,263,266],'161-5',[23,26],'1147-1183,1371-1386','deux foncteurs fibres … Isom … Q',
  'The forgetful Q_p-valued fibre functor on a neutral Tannakian category defines its proalgebraic automorphism group; comparison of two fibre functors is represented by an isomorphism torsor. After scalar extension, two isomorphic underlying vector-space functors can carry different semilinear Galois actions, so an identity section need not descend.',
  'Construction stated in diagrams.',
  'Proof_checks §8 checks functor-of-points and equivariance; no automatic invariant section is inferred from an Ω-section.',
  'B','Standard Tannakian fibre-functor/torsor formalism; Ziegler’s Theorem 3.6 and §§4.2–4.3 supply precise graded/filtered versions. The source’s proalgebraic group is an envelope of the specified category, not an identified universal motivic Galois group.', 'General formalism established; opened Ziegler first arXiv 8 November 2011, journal online 20 December 2013, issue January 2015.', ['bt_Ziegler2015',MI,S79])
c(68,[263,264,275],'161-5',[23,25,26],'1163-1183,1290-1293,1324-1350','graduation … opération diagonale; S_Ω(i)|S_Ω(−i)',
  'A Hodge–Tate grading descends only after the appropriate cyclotomic twist and semilinear action are specified. The Pro and Codex witnesses disagree both about the twist sign and the order of conjugation in an action, so there is no single adjudicated literal formula.',
  'Construction sketched with conflicting transcription witnesses.',
  'Proof_checks §8 matches weight i eigenspaces with the cancelling character; sign depends on whether the named Tate line is the line or its dual. Both readings remain in readings.tsv.',
  'C','The standard Hodge–Tate/Tannakian construction is established, but the exact formula of this leaf is undecided without scans. Modern conventions cannot choose the historical sign automatically.',SD,[S,'bt_Ziegler2015'])
c(69,[265],'161-5',[26],'1357-1365','Un j … unique. Du moins si',
  'A genuine tensor-compatible Hodge grading is equivalent to a cocharacter and determines it uniquely. A cocharacter satisfying only an underspecified π-invariance condition need not be unique; the author’s qualification stops unfinished.',
  'Uniqueness asserted, immediately qualified by an unfinished condition.',
  'Proof_checks §8: on every representation a grading determines t↦⊕t^i; conversely recover eigenspaces. Galois invariance alone admits many cocharacters, e.g. powers in G_m.',
  'C','Ziegler Theorem 3.6 gives the precise grading/cocharacter equivalence. Tate’s eigenspace uniqueness supplies the Hodge decomposition once conventions are fixed; it does not complete the source’s missing condition verbatim.', 'Tate theory used in 1966/1967; precise opened graded-functor theorem arXiv 2011, published 2015.', ['bt_Ziegler2015',S])
c(70,[259,267,268,276,278,279],'161-5',[24],'1188-1202','Peut-on prolonger ces données … ⊗ et Hom',
  'The author asks for tensor/internal-Hom-compatible extension of F-isocrystal, de Rham filtration and graded Hodge comparison data from BT objects to M^BT. The literal M^BT is generated by all two-weight Hodge–Tate objects, and the scalar-extension formula reverses L⊂K. The standard corrected question restricts to the tensor category generated by crystalline BT representations and uses T_DR=T_cr⊗_L K.',
  'Open extension question with a field-direction and generator ambiguity.',
  'Type and essential-image audit: C-SA23-bt-066 plus proof_checks §8. No arbitrary all-Hodge–Tate object is assumed crystalline.',
  'C','Crystalline/de Rham comparison functors give the standard tensor-compatible construction on the BT-generated crystalline category; Liu Theorem 2.2.1 supplies the precise two-weight essential image. The literal larger-category question is not answered by that theorem and is not declared impossible merely from failure of D_cris admissibility.', 'Modern all-prime BT theorem 2013; original sheet undated; first period-functor circulation not established by opened sources.', ['bt_Liu2013','bt_FontaineOuyang','bt_Gunton2021'],'medium')
c(71,[266,269,279],'161-5',[24,26],'1202,1357-1386','unicité … à isom unique près',
  'Uniqueness of the requested tensor extension depends on fixing the source category, comparison maps, variance and admissibility; bare existence of some tensor functor into filtered isocrystals does not imply unique isomorphism. On the standard crystalline category the comparison construction is canonical with its comparison data.',
  'Explicit open uniqueness question.',
  'Audit in proof_checks §8 separates a chosen comparison datum from an unrigidified fibre functor and its automorphism torsor. No universal uniqueness theorem is manufactured.',
  'C','The standard period-functor construction answers a precisely rigidified crystalline version. Ziegler’s splitting torsor shows why a filtered fibre functor can have multiple splittings; the later Γ formulation has further genuine cohomological choices. Exact literal uniqueness remains underdetermined.', 'Relevant modern formulations: Ziegler arXiv 2011/online 2013/print 2015; Liu 2013.', ['bt_Liu2013','bt_FontaineOuyang','bt_Ziegler2015'],'medium')
c(72,[270],'161-5',[27],'1393-1410','R_L … U″_L … trivial',
  'For a specified filtered fibre functor, its splitting scheme is a torsor under the associated unipotent group; in characteristic zero over an affine base with pro-smooth automorphism group it admits a section. Existence of a section does not make that section canonical. Whether the manuscript R is exactly this splitting torsor requires its omitted definitions.',
  'Torsor and triviality asserted in compressed notation.',
  'Ziegler Theorems 4.13–4.16 and 4.39 read; proof_checks §8 separates fpqc local splitting, global splitting and canonical choice.',
  'C','The natural filtered-functor subcase is established by Ziegler under explicit hypotheses. The bare R in the source is not identified with a canonical section by that theorem.', 'arXiv 8 November 2011; journal online 20 December 2013; issue January 2015.', ['bt_Ziegler2015'],'medium')
c(73,[271],'161-5',[27],'1411-1421','G″_L≃G′_L non canonique',
  'If G″=Aut_G(Q), U⊂G″ and R is a trivial U-torsor, then a choice of section gives P=R×^UQ≅Q and Aut_G(P)≅G″. It does not identify either inner form canonically with the original G.',
  'Noncanonical comparison asserted.',
  'Independent contracted-product proof in proof_checks §8; changing the section conjugates the identification.',
  'E','Standard torsor twisting; the prime labels are mathematically substantive and retained. Milne §3k and §23.52 supply opened torsor/twisting formalism.',ED,[MI,'bt_Ziegler2015'])
c(74,[272,273,288],'161-5',[27,28],'1423-1448','Structure de descente; G_K-Isom … Γ',
  'Descent of P and a Frobenius-semilinear isomorphism are separate data; packaging them into Γ-actions requires a specified coefficient field, automorphism, topology, extension 1→π̃→Γ→Z→1 and embedding of the separately named π. Neither π=π̃ nor normality is given.',
  'Construction sketched; fields and indices unresolved.',
  'Type audit in proof_checks §8–9; no quotient Γ/π formed without normality and no S=Ω identification imposed.',
  'F','General semilinear descent and cocycle theory are established, but the exact group and action in this manuscript cannot be uniquely recovered. The opened period and nonabelian-cohomology sources do not fill the missing definitions by themselves.', 'Sheet undated; no exact later theorem identified for its unspecified Γ.', [MI,'bt_FontaineOuyang'],'low')
c(75,[281],'161-5',[28,29],'1454-1486','Si on a une telle section … cocycles',
  'Given a group extension 1→A→E→Γ→1 and one splitting α, every other splitting has form z(γ)α(γ), with z(γδ)=z(γ)·γ(z(δ)) for the α-conjugation action. A-conjugacy classes correspond to nonabelian H¹. This parametrization does not prove existence of α.',
  'Conditional construction proved by direct rewriting.',
  'Independent multiplication check in proof_checks §9. Continuous/algebraic versions require the corresponding regularity of all maps.',
  'E','Classical nonabelian cocycle description, already available in Serre’s Galois Cohomology (1964 original); exact formulas checked in Milne §3k.', 'Original Serre course 1962–63, publication 1964, chronology verified by 1997 foreword; exact first invention not claimed.', [MI,'bt_SerreGalois1997'])
c(76,[282],'161-5',[28,29],'1470-1495','φ(π)={e}',
  'For any subgroup π⊂Γ, the neutral fibre of H¹(Γ,A)→H¹(π,A) is the set of cocycles normalized by z|π=1 modulo A^π. This identifies extensions of a fixed partial splitting, once one extension exists; normality of π is unnecessary for this statement.',
  'Source gives normalization/conjugacy question; the precise neutral-fibre formulation is an earlier-run/current reconstruction.',
  'Proof_checks §9: trivial restriction is killed by a coboundary; a conjugator preserves normalized restriction iff it is π-fixed.',
  'E','Classical cocycle normalization; confirmed against Milne §3k and independently proved. It is weaker than full injectivity of the restriction map.',ED,[MI,'bt_SerreGalois1997'])
c(77,[283],'161-5',[29],'1489-1495','injectif … [plus simplement] noyau nul',
  'Triviality of the neutral fibre of a map of nonabelian H¹ sets does not imply full injectivity. All fibres are described by corresponding neutral fibres after twisting the coefficient action. The source’s parenthesis should not be silently read as equivalence.',
  'Question with a weaker alternative; entire upper block deleted in Codex but not Pro.',
  'Proof_checks §9 and H1_neutral_fibre_not_injectivity: Γ=A=A₅ with trivial action, π=< (12)(34) >. Neutral fibre is trivial by simplicity, but identity and conjugation by odd (12) are nonconjugate homomorphisms with equal π-restriction. Exact enumeration of A₅ normal closures and all 60 inner conjugators saved.',
  'E','Standard twisting formalism in Milne §23.52 explains the distinction. The finite example verifies the logical warning, not an identification of the manuscript’s Γ with A₅.',ED,[MI,'bt_SerreGalois1997'])
c(78,[284],'161-5',[27,29],'1438-1441,1480-1495','π⊂Γ',
  'Only if π is normal can a cocycle z with z|π=1 descend to Γ/π with values in A^π. Without normality the normalized-cocycle formulation remains valid but there is no such quotient-group reduction.',
  'Earlier-run hypothesis check; normality not stated on the page.',
  'Proof_checks §9: z(πγ)=πz(γ), z(γπ)=z(γ); normality equates these and forces A^π values.',
  'E','Classical inflation/restriction mechanism. No Γ/π=Z identification is made merely from the different kernel π̃ appearing earlier.',ED,[MI,'bt_SerreGalois1997'])
c(79,[285],'161-5',[29],'1496-1498','torseur [deleted] … esp. homogène',
  'If extensions of a fixed partial splitting form one orbit under A^π, the stabilizer of a chosen full splitting is A^Γ. The orbit is homogeneous and need not be a torsor.',
  'Local word correction explicit; larger paragraph’s cancellation status differs between witnesses.',
  'Proof_checks §9 computes the conjugation stabilizer exactly.',
  'E','The replacement is mathematically correct. Classical nonabelian torsor theory supports the stabilizer calculation; it does not settle the larger deletion scope on the ink.',ED,[MI])
c(80,[269,286],'161-5',[27,28,29],'1438-1498','Est-il vrai … conjugués',
  'Earlier-run explicit test: for K=Q_p, A=Ω×, Γ=G_K×Z acting on A through G_K, and fixed trivial G_K-part, normalized splittings have Z-multipliers b∈Q_p×. Conjugation by A^G_K=Q_p× is trivial, so multipliers 1 and p are not conjugate.',
  'Question on the page; counterexample addresses a stated reconstruction, not the unspecified original admissible-data problem.',
  'Proof_checks §9 and relative_cocycle_rank_one verify the cocycle action, fixed field and trivial conjugation.',
  'C','Bare uniqueness is false in this explicit model. The manuscript might intend additional admissibility/slope conditions, but none are supplied well enough here to assert their effect.', 'Elementary test rechecked 19 November 2026; no historical first-date claim.',[MI,'bt_FontaineOuyang'])
c(81,[287],'161-5',[27,29],'1428-1441,1493-1495','P_K≃P^(φ)',
  'Earlier-run semilinear test: if σ preserves the discrete valuation of F, every multiplicative coboundary σ(a)/a has valuation zero. A uniformizer gives a nonzero class in H¹(Z,F×)=F×/{σ(a)/a}. Thus semilinearity alone does not force uniqueness.',
  'Reader’s countermodel, not a theorem explicitly asserted in the source.',
  'Proof_checks §9 and semilinear_valuation prove v(σ(a)/a)=0 and distinguish a valuation-one representative.',
  'E','A standard elementary cohomology calculation. The precise coefficient ring, Frobenius action and admissibility of the original page remain unresolved.',ED,[MI,'bt_FontaineOuyang'])
c(82,[290],'161-5',[29],'1521-1551','T_K(Q_p)≃K*',
  'For T=Res_(K/Q_p)G_m and any Q_p-algebra R, T(R)=(K⊗_(Q_p)R)×. In particular T(Q_p)=K× but T(K)=(K⊗_(Q_p)K)×; for quadratic separable Galois K/Q_p this is K××K×.',
  'First identity written; second is a reader’s check on the diagram interpretation.',
  'Proof_checks §10 and restriction_of_scalars_quadratic use a⊗b↦(ab,σ(a)b). The correct base argument cannot be replaced by a similarly named field.',
  'E','Defining restriction-of-scalars identity. Serre 1979 uses these tori; Jordan–Ribet–Scholl §1.1/Proposition 1.4 gives an opened modern model-and-components exposition.',ED,[S79,'bt_JordanRibetScholl2024'])
c(83,[291],'161-5',[29],'1529-1551','0→V*→K*→Z→0; oblique π',
  'The valuation exact sequence splits on abstract groups after choosing a uniformizer ϖ: x↦(xϖ^(−v(x)),v(x)). The source’s oblique π could label such a choice, but that reading is not decided here.',
  'Valuation diagram displayed; label ambiguous.',
  'Proof_checks §10 and uniformizer_splitting check the inverse (u,n)↦uϖ^n and dependence on ϖ.',
  'E','Standard DVR calculation, also reflected in the Néron model’s integral points. A chosen splitting of point groups is not a canonical isomorphism of group schemes.',ED,['bt_JordanRibetScholl2024'])
c(84,[289,291],'161-5',[29],'1532-1551','Ñ_K≃g_K×Z_K; points diagram',
  'The source’s Ñ and base-field labels are insufficient to identify the full diagram. The Néron lft model of G_m over a DVR has generic fibre G_m and special fibre G_m×Z, whereas a generic-fibre product G_m,K×Z_K is disconnected. These cannot be identified merely by a comparison of selected point groups.',
  'Unexplained diagram; exact assertion not identifiable.',
  'Proof_checks §10 distinguishes generic/special fibres and the valuation exact sequence. No model is renamed or repaired silently.',
  'F','Jordan–Ribet–Scholl §1.1 and Proposition 1.4 precisely verify the standard Néron/Weil-restriction facts. They do not decide which model and base labels the handwritten diagram denotes.', 'Modern opened exposition online 26 March 2024, issue May 2024; standard Néron facts are not new in 2024.', ['bt_JordanRibetScholl2024'],'medium')
c(85,[295],'93',[224,225,226,227,228,229],'79-189','connexion intégrable naturelle [earlier-run proposed arithmetic bridge]',
  'Earlier-run conditional implication: if this connection is identified with algebraic Gauss–Manin cohomology of a smooth proper family over a suitable arithmetic model satisfying the locally free cohomology hypotheses, Katz’s global-nilpotence theorem applies. It gives nilpotent p-curvature, not identically zero p-curvature.',
  'Idea of the earlier run; no arithmetic model supplied by the analytic sheets.',
  'Exact hypotheses checked in Katz Theorem 10.0, pp.209–210; no p-curvature computation on an absent elliptic family claimed.',
  'B','Katz’s established theorem supports the conditional statement. Identifying the archive’s intended family or operator remains an unverified project lead, not a consequence of the theorem.', 'Published 1970; received 25 June 1970; website digitization/online dates are not treated as first circulation.', ['bt_Katz1970',KO])
c(86,[251],'161-5',[21],'1069-1077','two weights → Jordan structures [earlier-run route]',
  'Earlier-run route: a two-weight cocharacter induces a three-grading g=g_(−1)⊕g_0⊕g_1 on a stable Lie subalgebra of End(V). The extreme pieces are abelian and double brackets define a Jordan pair; a unital Jordan algebra requires extra data.',
  'Idea of the earlier run, suggested by the Springer annotation.',
  'Proof_checks §6 checks weight sums and vanishing brackets in degrees ±2; code End_weight_decomposition records the degree computation. The Jordan identities follow from Jacobi under the usual characteristic assumptions.',
  'B','Bertram–Neeb §3.1 gives the exact Jordan-pair construction and §5 the additional unital structure; Serre 1979 p.182 points to Springer §11. The route is established structure theory, not proof that every candidate is realizable by a BT group.', 'Springer 1973; Bertram–Neeb arXiv first submitted 18 June 2003. Journal publication metadata not relied on because publisher retrieval failed.', ['bt_BertramNeeb2003',S79,'bt_Springer1973'])

c(87,[206,207],'93',[221],'1-8','on trouve donc un isom. Γ(G)/E → Z¹C(g*)/d⁰(E)',
  'The retained page begins with a quotient comparison whose group G, subgroup/sheaf E, coefficient dual and preceding construction are not defined in the retained extract. Only the displayed assertion, with its uncertain isomorphism mark, can be recorded; no unique modern theorem is recoverable from it alone.',
  'Concluding assertion inherited from missing preceding leaves; notation uncertain.',
  'Boundary/typing audit only. Neither the source’s E nor the coefficient superscript is silently supplied.',
  'F','Formal de Rham and stratification sources give a related framework, but do not identify this exact quotient without the preceding definitions. Cote93/220 is not among the supplied retained leaves.',GD,[G,'bt_EGAIV4'],'low')
c(88,[226],'93',[234],'325','il suffit que X′,X″ soient loc. T-isom (sur X₀)',
  'Local isomorphism inducing the fixed reduction suffices for the isomorphism sheaf to be locally nonempty and a torsor under the automorphism sheaf. Dropping smoothness from the whole displayed formula needs separate care: identifying the actual reduction ideal J with I⊗O_X₀ uses flatness, and identifying Hom(Ω¹,J) with a tangent tensor uses local freeness.',
  'Marginal weakening suggested; its full scope is not specified.',
  'Proof_checks §4 verifies the torsor assertion from local nonemptiness. The stronger coefficient-identification claim is not assumed without flatness/local-freeness hypotheses.',
  'C','Grothendieck §3.4 supplies the smooth square-zero theorem. The local-isomorphism-only torsor assertion is formal; the exact proposed weakening of every later identification is not established by that smooth theorem.',GD,[G,'bt_Stacks01UP'])
c(89,[242,243],'161-5',[14,15],'850-868','a₁=p; a_n∈m (n<p^h); a_(p^h) inversible; T_n≃(Z/p^n Z)^h',
  'For a one-dimensional formal group of finite height h, its p-series has linear coefficient p, coefficients below degree p^h in the maximal ideal, and unit coefficient at p^h; the geometric p^n-torsion is abstractly (Z/p^n Z)^h in characteristic-zero generic fibre, with transition multiplication by p.',
  'Standard formal-group facts stated and referenced before the valuation proof.',
  'Coefficient roles checked in the valuation estimate; rank and divisibility of geometric BT torsion carried as standard background, not proved by the numerical recurrence.',
  'B','These are the precise formal-group inputs used by Serre Proposition8/Lemma3. Lubin’s cited paper metadata is verified as1967, not the source bibliography’s1961; the full Lubin proof was not read.',SD,[S,'bt_Lubin1967'])
(P/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
print(f'{len(C)} manually formulated claims saved')
