#!/usr/bin/env python3
"""Serialize individually authored semantic reviews after reading every source passage.
No keyword, heading or cue supplies a verdict. Source numbers below are manual assignments.
"""
import csv,json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
PK='MPL_138_046-089'
FILE=PK+'_transcription.tex'
items=[]; entries=[]
def add(ns,kind,scans,lines,words,statement,reconstruction,check,reason,verdict='kept'):
    ident='SA09-'+str(206+min(ns))
    items.append(dict(id=ident,sources=[PK+'#'+str(n) for n in ns],kind=kind,cote='138',scans=scans,lines=FILE+':'+lines if lines else 'No corresponding manuscript passage; methodological entry',his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for n in ns: entries.append(dict(entry_id=PK+'#'+str(n),item_id=ident,verdict=verdict if n==ns[0] else 'merged into '+ident,reason=reason if n==ns[0] else 'Read with its cited passage; same object/question as '+ident+'. '+reason))

add([1],'other',[], '', '',
 'The earlier run describes its contextual inputs, including an AI modernisation by Hua, a result register, and unprovided Longue Marche and Esquisse transcriptions; these are provenance statements, not manuscript mathematics.',
 'This run can verify that the note makes those declarations; it cannot verify absent project reports or the earlier run’s process.',
 'not on the page','A methodological ### heading is itself indexed. Retained as provenance with no attributed mathematical assertion; the cited contextual files are absent from this archive.')
add([2],'title, date or page count',[48,50,52,56,67,69],'98–154;218–307;384–455;564–644;964–1019;1074–1133','June 10, 1978',
 'Six retained printed documents carry June 1978 dates (8, 10, 15, 26, 27, 28 June). These establish dates of those documents, not dates of the mathematical handwriting or an otherwise unproved pairing of recto and verso.',
 'The restriction to documentary dating is editorial source criticism; the catalogue label 1976,77? is not treated as a date for every leaf.',
 'agrees','The dates occur in the complete transcription. Mumford’s 460-page journal allocation is not a count of these manuscripts.')
add([3],'unpursued implication',[47],'14–96',r'x_n^n=x_1;\quad u=\frac12-\frac14(z+z^{-1})',
 'For n≥1 over an algebraically closed field of characteristic zero, f_n(x)=1/2−(x^n+x^(−n))/4 is a degree-2n rational map P¹→P¹, Galois with dihedral deck group μ_n⋊C₂. Its branch indices are 2 above 0 and 1, and n at the two points above infinity (n=1 omits infinity from the branch locus).',
 'The composite formula, its Galois interpretation and characteristic-zero hypothesis are explicit modern completion of the two displayed maps; no universal Belyi assertion is present.',
 'agrees','The source gives x_n^n=z, the second formula, and local indices. It does not assert every curve arises from this family.')
add([4],'reading question',[46,47,81],'2–12;58–60;1460–1464',r'\mu_\infty;\quad T=\varprojlim_n\mu_n(k)',
 'A compatible projective system of roots of unity has Tate-module limit lim μ_n, whereas the torsion union colim μ_n is a different group. The notation μ∞ on scan47 has no specified transition maps. Scan46 withdraws a universal abelian-cover description in favour of a particular principal pro-cover.',
 'Neither limit convention nor the universality of the Fermat subsystem is supplied silently. Comparison to the explicit inverse limit at81 is diagnostic only.',
 'agrees','Both the cancellation at46 and unspecified μ∞ at47 are visible. The later limit does not resolve the earlier notation on the ink.')
add([5],'unpursued implication',[49,55],'158–184;546–561',r"x'=-x(x^2-3y^2),\quad y'=y(y^2-3x^2),\quad z'=z^3",
 'On the projective conic C:x²+y²+z²=0 in characteristic zero, the displayed homogeneous cubic polynomials have no common zero and define a self-map. Their sum of squares vanishes modulo x²+y²+z²; the coefficient in the displayed ambient polynomial expansion is 3, not 9.',
 'The global morphism check and reduction modulo the conic equation are this run’s verification. The doubtful deleted/inserted digits remain unchanged.',
 'agrees','The note correctly restricts the identity to C and credits the previous interpretation rather than claiming a new discovery.')
add([6,9],'self-flagged step',[49,51,55],'158–174;371–381;522–561',r"x',y',z' fonctions rat. de x,y,z ?? P.ex. z'=z^n",
 'For C/Q:x²+y²+z²=0, u=(y−ix)/z identifies C over Q(i) with P¹. The power map u↦u^m descends to Q exactly for odd positive m, since complex coefficient conjugation sends u to −u⁻¹. For odd m, write (y−ix)^m=B_m−iA_m and use (A_m:B_m:z^m).',
 'Parity descent is an idea of the earlier run, independently rechecked here. The source asks for rational coordinate functions and displays odd powers and the cubic example, but does not give this descent argument.',
 'agrees','The live question at55 and “n impair” at51 refer to the same power-coordinate issue. Preserve both the author’s open step and the earlier run’s field qualification.')
add([7],'reading question',[51],'311–381',r'x^2+y^2+z^2=0;\quad(x,y,z)=(1-t^2,2t,1+t^2)',
 'The displayed parametrisation lies on x²+y²−z²=0, not on x²+y²+z²=0. The two conics become isomorphic over Q(i) by multiplying the third coordinate by i; over Q the positive conic has no real points and is not the split conic.',
 'A change of conic model is a plausible reconstruction, not a correction to the sign. The separate use t=y/x is a projective ratio on the source, not automatically the inverse parameter of the displayed parametrisation.',
 'agrees','The plus and minus forms both occur. Neither the unannounced model change nor the intended coordinate domains are determined by the text.')
add([8],'idea of the earlier run',[49],'195–216',r'p-\lambda q=0;\quad p^{\prime}q-q^{\prime}p=0',
 'For coprime polynomials p,q in characteristic zero and f=p/q, finite nonpole critical points satisfy p′q−pq′=0; a critical value λ satisfies p−λq=p′−λq′=0 there. Global ramification analysis also requires poles and the point at infinity.',
 'The boundary-case audit is the earlier run’s proposed completion. The division λ=p′/q′ needs q′≠0 and cannot be used in general as an equivalence.',
 'agrees','The page contains a scratch elimination, not a certificate that the resulting map is branched only at three points. This run adds the explicit q′≠0 proviso.')
add([10],'self-flagged step',[53,54],'457–501',r"0'\leftrightarrow1',\quad1'\leftrightarrow\infty',\quad ?",
 'The roots-of-unity covering diagram contains an unresolved third slot. The standalone group Π_n=μ_n³/μ_n has rank two as a finite diagonal quotient, but arrows and a question mark do not determine a unique missing covering assertion.',
 'No missing theorem is invented; characterisations of every field extension in the crowded diagram would require the ink and compatible definitions from the preceding Fermat calculations.',
 'agrees','The exact question’s scope is not stated, so it remains an unidentified local problem, not a conjecture about the entire tower.')
add([11],'unpursued implication',[58,59],'654–727',r'\operatorname{Hom}_{f_0}(C,C^{\prime})\xrightarrow{\sim}\prod\operatorname{Isom}(f_0(a_i),f_0(x))\times\prod\operatorname{Hom}(\operatorname{Aut}(a_i),\operatorname{Aut}(f_0(a_i)))',
 'For a groupoid C, category D and object map f₀ constant up to isomorphism on each component, choose representatives a_i and arrows u_x:a_i→x with u_ai=id. A functor over f₀ is equivalent to isomorphisms t_x:f₀(a_i)→f₀(x) (t_ai=id) and group maps φ_i:Aut_C(a_i)→Aut_D(f₀(a_i)); F(g:x→y)=t_y φ_i(u_y⁻¹gu_x)t_x⁻¹.',
 'The reconstruction formula and choices u_ai=t_ai=id are expanded here; no later topological gluing theorem follows from them alone.',
 'agrees','The proposition and next-page criteria support the note. The source’s general target category is essential for evaluating its later corollary.')
add([12],'unproved claim',[58,59,61],'656–679;703–727;763–783',r"NB\ f\ \text{équivalence}\Longleftrightarrow a)\text{ et }c)\text{ sont vrais}",
 'For functors between groupoids, equivalence is equivalent to a bijection on components and isomorphisms of vertex groups; isomorphism additionally requires an object bijection. The abbreviated corollary is false for the previously allowed arbitrary target category.',
 'Counterexample: the unique functor from the one-object trivial groupoid to the one-object category with endomorphism monoid (N,+) has bijective objects/components and isomorphic unit groups, but is not full. The target-groupoid hypothesis is supplied for the corrected statement.',
 'agrees','Scan59 explicitly requires all target arrows in each relevant Hom-set to be invertible; scan61 omits this condition. The note diagnoses scope accurately, without changing “catégorie”.')
add([13],'unproved claim',[60,61,62],'731–759;786–796',r'\operatorname{Aut}(C)\longrightarrow\mathfrak S_{C_0}\quad\text{surjection}',
 'For a connected nonempty groupoid C, every object permutation extends to an automorphism after choices; Aut⁰(C)→Aut(π_a) is surjective with kernel naturally ∏_(x≠a)Aut_C(x), and splits after choosing transports. For disconnected C, the image consists only of permutations respecting component equivalence and isotropy-group isomorphism types.',
 'Connectedness is visible only in the cancelled setup. This run uses it as an explicit additional hypothesis of the repaired theorem, not as silently live text.',
 'agrees','A groupoid with one object of isotropy1 and one of isotropyC₂ refutes unrestricted surjectivity; the connected transport calculation is valid.')
add([14],'withdrawn in the same text',[62,63],'802–829',r'\deleted{commutant}\inserted{normalisateur de G}',
 'For the graph K(I) with two vertices and n parallel edges, the vertex-swap involution commutes with edge permutations. Its fundamental group has rank n−1. The manuscript changes the proposed calculation from a centralizer to a normalizer and stops before performing it.',
 'The rank is an elementary reconstruction. D labels polygon symmetries, while G later acts transitively on the two objects; their identification is not justified and may require adjoining the vertex swap.',
 'agrees','The deletion/insertion and unexplained D/G transition are both present. No profinite torsion classification or completed normalizer result is on these pages.')
add([15],'unpursued implication',[64,78],'831–878;1324–1333',r'\rho_2^+\rho_1^+\rho_0^+=\operatorname{id}_{E^+}',
 'If the six maps p_ij^±:E^±→D_ij are bijections, the indicated pairwise transition maps define permutations ρ_i^± whose displayed product telescopes to the identity; vertex sets S_i are asserted to be their orbit sets in the intended cellular incidence data.',
 'The bijection hypotheses and a consistent reading of the doubtful rho index are required for the formal calculation. Product one alone does not prove arbitrary diagrams come from a surface.',
 'agrees','The formula and orbit descriptions are explicit; this run checks the algebra conditionally without reconstructing the original drawn indices.')
add([16,17],'unproved claim',[65,66,68],'880–961;1023–1047',r'\frac2N=2-\sum_i(1-1/d_i)>0',
 'For a connected tame Galois cover P¹→Y of smooth projective curves over an algebraically closed field, with group order N and branch indices d_i≥2, Riemann–Hurwitz forces Y=P¹. The nontrivial possibilities are two branch points with indices (N,N), or three with (2,2,n),(2,3,3),(2,3,4),(2,3,5), of orders2n,12,24,60. No ≥4-point signature occurs.',
 'Tameness, smoothness, connectedness and geometric base field are stated explicitly in modern form. The live weak inequality on68 is insufficient by itself; the preceding strict inequality supplies the contradiction.',
 'agrees','The numerical classification is supported; it supplies no modular congruence-centralizer theorem. The cancelled detour and live middle block on68 are distinguished.')
add([18],'withdrawn in the same text',[68],'1049–1065',r'\text{p-extension ... inséparable};\quad H\simeq(\mathbb Z/p\mathbb Z)^r',
 'The cancelled draft discusses wild finite subgroups of PGL₂ and a putative Borel reduction. A finite p-subgroup over an algebraically closed field of characteristic p is conjugate to a group of translations and is elementary abelian; a finite group quotient of a function field is separable. The draft as a whole is not a proved wild-cover classification.',
 'The two correct general facts are separated from uncertain cancelled words. No inferential repair of the word “inséparable”, the exponent or the larger G is made.',
 'agrees','The whole lower discussion is inside a deleted block. Mathematical objections identify scan checks, not live conjectures.')
add([19],'self-flagged step',[68],'1067–1072',r"si X'\text{ de genre }0\ (\text{facile})",
 'Within a cancelled tame-dihedral reduction, a quadratic Kummer base change is proposed to eliminate two inertia-2 branch points; the genus-zero property of the appropriate connected normalization is left to check.',
 'For the explicit dihedral model the base change can be computed; it does not prove a statement about an unspecified connected component under arbitrary wild hypotheses.',
 'agrees','The verification wording and the outer cancellation both survive. “Facile” is not a proof and no unconditional reduction is attributed.')
add([20],'unpursued implication',[70,71,72],'1135–1165',r'T=\mathbb Z\wedge_{\mathbb Z/2}\omega',
 'For a two-element orientation torsor ω, T is its associated rank-one sign local module. A finite-type orientable surface obtained from a compact surface by removing finitely many points has an intrinsic end compactification; homeomorphisms extend uniquely to isomorphisms of the compactified pairs.',
 'The equivalence is between homeomorphism groupoids, not arbitrary continuous maps. “Freudenthal” is modern identification; the source itself mentions Čech.',
 'agrees','The orientation object and the categories with orientation-preserving homeomorphisms are written explicitly.')
add([21],'unproved claim',[72,73,74],'1167–1180',r"on devra expliciter ... le passage d'une description à l'autre",
 'Given finite disjoint sets S,J in a compact oriented surface, S denotes deleted points and J objects of a fundamental groupoid. Relating the marked-point description to the description obtained by puncturing J requires specifying filling maps and how peripheral subgroups change.',
 'The finite-marked-set version is used for comparison with the opened topology literature; the manuscript’s unspecified convention for an arbitrary discrete set is not replaced by an unstated finiteness assumption.',
 'agrees','The note correctly preserves the deferred construction and the distinction between deleted points and groupoid objects. The passage is not a completed tower action.')
add([22],'reading question',[74,75],'1198–1209;1227–1233',r'T\overset{\sim}{\longrightarrow}(\bigwedge^2\Pi_{\wedge\mathrm{ab}})^\vee',
 'For a closed oriented genus-g≥2 surface, H₁ has rank2g and (Λ²H₁)∨ has rank g(2g−1)>1. The orientation datum is a primitive nondegenerate alternating form with values in an orientation line (equivalently the cup product and H²), not an isomorphism from a rank-one module to the entire exterior-square dual.',
 'The corrected orientation datum is mathematical reconstruction. The uncertain arrow, crowded words and whether a subline rather than the full dual was intended require the scans.',
 'agrees','The rank obstruction is decisive against the literal isomorphism; it does not decide the ink or replace it with an injection.')
add([23],'self-flagged step',[74,75],'1210–1236',r'K(\mathbb Z,1)\ \text{resp.}\ K(\mathbb Z^2,1);\quad\text{vérifier}',
 'For finite-type oriented surfaces other than the sphere and plane, the peripheral fundamental group determines mapping classes; the unmarked open-annulus and torus identity components have typesS¹ andT². Fixing at least one point removes these exceptional identity-component homotopy types under the usual finite-marking, compact-open topology conventions.',
 'Precise topology, pointwise marking and finite-type restrictions are modern specifications. An arbitrary infinite discrete marking or operator-equivariant extension is not asserted to follow.',
 'agrees','The exceptions and the explicit “vérifier” are present. The check concerns an ∞-isotopy enhancement, not merely the π₀ classification.')
add([24],'idea of the earlier run',[70,75],'1137–1139;1233–1236',r'\text{surfaces compactes à opérateurs}',
 'Contractibility of the ordinary identity component of a homeomorphism group does not by itself establish contractibility or trivial π₁ of the centralizer of a specified operator group. The earlier run proposes an equivariant follow-up to the surface paradigm.',
 'The actual operator-centralizer kernel and Longue Marche verdicts are absent project leads; they are not checked by these local pages.',
 'agrees','The cover title promises operators, but the displayed argument is ordinary/marked. The note correctly separates the additional equivariant question.')
add([25],'reading question',[75],'1221–1228',r'\text{T-structure }\unsure{à bouts|à bout}',
 'A peripheral structure consists of outer homomorphisms from the orientation module to the surface group. Whether the handwritten abbreviation is “à bouts” or an abbreviation for “à lacets” cannot be determined from this transcription.',
 'The alternative comes from the earlier run’s comparison with an absent Longue Marche transcription, not from a new visual inspection.',
 'agrees','The doubtful wording is retained. Its mathematics is recognizable but the literal term remains undecided.')
add([26],'title, date or page count',[76],'1238–1241',r'\unsure{groupes}\ \unsure{prolibres|problèmes}\ \text{spéciaux}',
 'The cover title is uncertain between wording about special free profinite groups and wording about special problems. The next pages contain incidence diagrams; scan80 begins an explicit special-profinite-group definition.',
 '“Quelques problèmes spéciaux” is the earlier moderniser’s proposed reading only. No mathematical inference decides the first two handwritten words.',
 'agrees','The title alternatives must remain indexed separately from a theorem or page-count assertion.')
add([27],'unpursued implication',[77,78],'1243–1320;1322–1333',r'E=(R,q^{\prime})\times_A(R,q^{\prime\prime})',
 'The fibre product E of two incidence maps records compatible pairs of flags, with three displayed projections and a decomposition into orientation signs E⁺,E⁻. Recovering precise involutions requires consistent interpretation of bars and subscripts and the intended surface incidence model.',
 'No general assertion that arbitrary R,A and q-maps satisfy cartographic involution relations is reconstructed. The potential equality σ₀σ₂=σ₂ is separately flagged as degenerate if read literally.',
 'agrees','The fibre product is explicit but the detailed indices are doubtful. A related cancelled diagram in another project is only a lead.')
add([28],'idea of the earlier run',[78],'1365–1380',r'\mathbb P^1_{\overline{\mathbb Q}}\xleftarrow{\varphi}\mathbb P^1_{\overline{\mathbb Q}}',
 'The seven marked finite points match the special fibres of R(t)=27t²(t−1)²/[4(t²−t+1)³]: R⁻¹(0)={0,1,∞}, R⁻¹(1)={−1,1/2,2}, and R⁻¹(∞) consists of the two roots of t²−t+1. This is a candidate for the unlabelled quotient map, not its written equation.',
 'The rational function is proposed by the earlier run through a Longue Marche comparison and independently checked here. The source merely labels the points and φ.',
 'agrees','Matching fibres make the candidate precise but cannot prove authorial intention.')
add([29],'unproved claim',[80,81,89],'1397–1445;1670–1715',r'\pi\longrightarrow A_\nu^\circ\quad\text{injectif}',
 'The inner-action map from a free profinite group of rankν has kernel its centre. Atν=1 it is the zero map from Zhat and is not injective. Atν≥2 the free profinite group is centreless, so the map is injective. Scan89 imposesν≥2 whereas the earlier definition allowsν≥1.',
 'The later restriction is compatible with repair but is not called an explicit retraction of scan81. Any quotient sequence must use Inn(π) in full generality.',
 'agrees','Both parameter ranges were read, giving an explicit rank-one counterexample and a correct subsequent range.')
add([30],'unproved claim',[80,81,89],'1421–1455;1703–1709',r'\widetilde A_\nu\to\mathfrak S_{\nu+1}\times\widehat{\mathbb Z}^{*}\quad\text{surjectif}',
 'For the standard peripheral free profinite group of a sphere withν+1 punctures, automorphisms of the full system realise arbitrary puncture permutation and arbitrary common cyclotomic unit. In particular the ordered peripheral automorphism group maps onto Zhat×.',
 'A proof uses topological puncture permutations together with the arithmetic action for a rationally labelled punctured P¹ and surjectivity of Gal(Qbar/Q)→Zhat×. This supplies a proof outside these pages; it does not determine the arithmetic image.',
 'agrees','Both assertions occur without a supplied proof. The two factors cannot be inferred merely from the existence of their projection maps.')
add([31],'reading question',[81],'1444–1455',r'1-\pi\longrightarrow A_\nu^\circ\longrightarrow\Gamma_\nu\longrightarrow1',
 'The quotient of Aν° by inner automorphisms is named Γν° in the prose, but the next displayed sequence uses uncircled Γν. Under the definitions, the circled quotient is required, withν≥2 for the left injection.',
 'The missing circle is a candidate transcription/manuscript inconsistency, not an emendation. The rank-one issue is handled separately inSA09-235.',
 'agrees','The definition and display conflict exactly as the note says.')
add([32],'unpursued implication',[82,83],'1470–1514',r'\text{mod autom. intérieurs};\quad{}^{P(X/I/k)}\widetilde\Gamma_\nu',
 'The geometric fundamental group of a punctured curve depends on the fibre functor up to inner isomorphism. The markings form an outer-automorphism torsor P, and descent gives an action into the associated inner form of the standard outer automorphism group; identifying that group with a fixed standard target requires a marking.',
 'The torsor language is translated into modern based/outer distinctions; no canonical standard identification is inferred for a general curve.',
 'agrees','The source explicitly replaces the point by a fibre functor and twists the target.')
add([33],'unpursued implication',[83],'1496–1514',r'\Gamma\ \text{opère ... par transport de structure};\quad\text{Kummer-Tate}',
 'For a geometrically connected punctured P¹ over a characteristic-zero field k₀ with algebraic closure k, the arithmetic étale fundamental-group extension induces Gal(k/k₀)→Out(π₁^geom). Its action on tame inertia is the cyclotomic character on lim μ_n(k).',
 'Smooth geometric connectedness and exactness conventions are explicit modern hypotheses. The reversed notation π₁(k₀/k) is not silently interpreted as a newly defined different group.',
 'agrees','The transport construction, extension and multiplier are written. Neither faithfulness nor a full image description is asserted.')
add([34],'reading question',[81,82,83,84,85,86,87],'1444–1514;1534–1662',r'\Gamma;\quad\mathcal T',
 'The transcription uses Γ for arithmetic and quotient notation and script T for later special outer groups. Editorial replacement of one alphabet by another in a modernised commentary is not evidence for changing manuscript glyphs.',
 'Corresponding group meanings can be compared after definitions, but graphical identification and canonical mathematical identification are separate questions.',
 'agrees','The notation varies across these pages; no change is made.')
add([35],'reading question',[84,85],'1539–1546;1591–1605',r'\Gamma\longrightarrow\mu_n\simeq\mathbb Z/n;\quad\varepsilon_\nu i_\nu=\chi_n',
 'The arithmetic action on μ_n factors through Aut(μ_n)≅(Z/n)× by exponentiation. It is distinct from the translation action of the cyclic group μ_n itself. The literal intermediate target μ_n in scan84 is incompatible with the subsequent cyclotomic formula as a general description.',
 'The natural unit-group correction is mathematical evidence for checking an omitted Aut or star, not a determination of ink.',
 'agrees','The two incompatible targets occur on consecutive pages. The later formula is a precise internal comparison.')
add([36,37],'self-flagged step',[85],'1571–1590',r'q_i=\lambda_{\unsure{0|1}}\cdots\lambda_{i-1};\quad\text{vérifier ?}',
 'In Lν=<λ₀,…,λν|λ₀…λν=1>,ν≥2, the inserted reversed tuple preserves the relation for q_i=λ₁…λ_(i−1), but with lower index0 its product is λ₀λ₁⁻¹λ₀⁻¹λ₁≠1. For the relation-preserving reading, t²=Inn(λ₀⁻¹), so its outer class is involutive whereas this specific lift need not have order2.',
 'These conditional word calculations belong to the earlier run and are re-proved/recomputed here. Neither the lower index nor the existence of a different strict lift is decided by them.',
 'agrees','The naive tuple is cancelled and the replacement is explicitly flagged. Relation preservation and order two are distinct tests of that same proposed reversal.')
add([38],'unpursued implication',[84,85],'1548–1563;1591–1606',r'i_\nu(\Gamma)\text{ commute à }t_\nu',
 'For P¹ punctured atμ_n, geometric inversion commutes with the arithmetic action and Galois conjugates rotations through its cyclotomic action. These identities hold for the geometric outer action; a specific based reversal formula must be checked separately.',
 'Geometric inversion has orientation/Tate multiplier+1; arithmetic complex conjugation has multiplier−1. No torsion classification in a larger Grothendieck–Teichmüller group is inferred.',
 'agrees','The note accurately distinguishes the geometric symmetry from arithmetic conjugation and from unprovided project claims.')
add([39],'reading question',[84,85,86],'1534–1546;1591–1624',r'\mathcal T_\nu^!\ \text{le ss-groupe de}\ \mathcal T_\nu',
 'The intended arithmetic-compatible subgroup must retain puncture permutations when the punctures areμ_n. If the untilded ambient group fixes all punctures, not all cyclotomic multipliers can occur for generaln; the tilded ambient group is a plausible correction.',
 'A precise repaired definition uses outer automorphisms satisfying the geometric inversion/rotation relations and their permutation-cyclotomic compatibility. This is conditional reconstruction.',
 'agrees','The source shifts from tilded to untilded ambient notation before asserting character surjectivity. No star/exclamation or tilde is silently changed.')
add([40],'unpursued implication',[86,87],'1628–1653',r'\boxed{\Gamma\longrightarrow\mathcal T_2^{\mathfrak S_3}}',
 'For P¹_Q minus{0,1,∞}, rational Möbius transformations realise S₃ on the punctures and commute with arithmetic transport in outer automorphisms. The Galois action fixes each puncture and lies in the S₃-centralizer of the pure peripheral outer group. The split permutation extension is an outer-level statement.',
 'This containment is not a claim that the Galois image equals the centralizer or all groups satisfying later GT relations.',
 'agrees','The split product and boxed target are written, with no surjectivity or injectivity assertion about Γ.')
add([41,46],'conjecture',[87,89],'1655–1662;1720–1724',r'\text{On aurait envie de définir un iso can.};\quad\text{on veut élucider sa structure}',
 'The author hopes for canonical identifications T₂!≅T₂^(S₃) and T₂!≅Tν!, and seeks the structure of the peripheral outer quotient. A meaningful modern question must define the ambient groups and comparison maps and impose compatibility under changes of punctures.',
 'The requirement to compare filling/forgetting and incidence maps is an earlier-run research direction, not a completed construction or an exact-image theorem on the page.',
 'agrees','The wish, marginal question mark and interrupted continuation are explicit. The companion note’s tower-compatibility proposal is merged as a labelled proposed refinement.')
add([42],'unpursued implication',[83,87],'1499–1514;1642–1653',r'\Gamma\longrightarrow\mathcal T_2^{\mathfrak S_3}',
 'The middle packet constructs an arithmetic homomorphism but does not assert its injectivity. Claims about the stages of a Longue Marche proof are reports of an absent comparator, while the later published Esquisse faithfulness assertion can be checked independently.',
 'No later proof is retroactively attributed to these sheets. Its relation to Belyi’s theorem is an external historical comparison.',
 'agrees','The only word “fidèle” in these middle mathematical pages concerns functors of groupoids. The note preserves this distinction.')
add([43],'unpursued implication',[47,78,83],'34–65;1365–1380;1516–1530',r'X_n;\quad\mathbb P^1_{\overline{\mathbb Q}}',
 'The explicit covers in this packet do not state the universal converse that a smooth projective connected complex curve is definable overQbar iff it admits a nonconstant map toP¹ with at most three branch values. The latter is Belyi’s theorem and appears as a reported theorem in the later Esquisse.',
 'This is a comparison of exact quantifiers, not a claim that Grothendieck lacked knowledge of a statement absent from these pages.',
 'agrees','Every middle passage was read, including the explicit examples. None provides the universal assertion; source dates do not establish priority relative to Belyi’s circulation.')
add([44],'unpursued implication',[84,87],'1534–1537;1653–1662',r'\Gamma\longrightarrow\widetilde{\mathcal T}_\nu',
 'The earlier run compares the arithmetic action with modern faithful actions on regular dessins. Such faithfulness is stronger than ordinary dessin faithfulness but does not identify the arithmetic image inside a GT-type group. Ordinary maps with index≤2 over1 form a restricted class of dessins.',
 'All modern theorems are external comparisons, and their exact quantifiers are checked in the literature record rather than assigned to these pages.',
 'agrees','The local source is only the outer-action arrow; regular-dessin theorems are correctly labelled external.')
add([45],'reading question',[87,89],'1662;1724',r"Pour ceci, on va généraliser d';\quad\text{on veut élucider sa structure}",
 'The middle packet ends before the later precarte and moduli sections. The following package supplies those pages, allowing the dossier to compare their actual claims rather than a prior modernised summary.',
 'The earlier run’s packet-boundary warning is correct locally; at whole-dossier level the late pages are now available and are reviewed separately.',
 'agrees','The stopped sentences support the local scope warning. No fine-moduli representability theorem is inferred from them.')
add([47],'unpursued implication',[46,53,55],'2–12;459–493;546–561',r'\Pi_n=\mu_n^3/\mu_n',
 'The Fermat stages and conic powers are geometric examples. They do not compute the CM character, a pronilpotent lifting obstruction or a residual procyclic normalizer mentioned in unprovided research registers.',
 'Statuses of LM7_PUSH, EXIT_TOWER and LM6 results are reported leads only. This run neither endorses nor refutes those separate research returns.',
 'agrees','The manuscript does not contain the modern character decision. The note accurately limits its contribution, but its claims of external refereeing cannot be independently checked here.')

assert len(entries)==47 and len({e['entry_id'] for e in entries})==47
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
with (OUT/'entries.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(entries,key=lambda x:int(x['entry_id'].split('#')[1])))
print(json.dumps({'reviewed_entries':len(entries),'items':len(items),'semantic_verdicts_authored_individually':True}))
