"""Manually authored semantic consolidation after reading all 127 entries and
all 1,683 lines of MPL_138_090-133_transcription.tex.  The program only serializes
those judgments; it does not infer verdicts from headings, keywords, or cues.
"""
from pathlib import Path
import json,csv,datetime
W=Path(__file__).resolve().parents[1]
items=[];entries=[]
T='MPL_138_090-133_transcription.tex'
def item(ns,kind,scans,lines,words,statement,reconstruction,check,reason,corrected=None):
    ident='SA09-'+str(253+min(ns)); sources=['MPL_138_090-133#'+str(n) for n in ns]
    items.append(dict(id=ident,sources=sources,kind=kind,cote=138,scans=scans,lines=[T+':'+x for x in lines],his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,n in enumerate(ns):
        verdict=('corrected' if corrected and n in corrected else ('kept' if j==0 else 'merged into '+ident))
        entries.append(dict(entry_id='MPL_138_090-133#'+str(n),item_id=ident,verdict=verdict,reason=(corrected[n] if corrected and n in corrected else reason)))
item([1],'unproved claim',[90],['4-24'],r'B_\nu\xrightarrow{\chi_\nu^\circ}\mathbb Z^*=\{\pm1\}\quad\text{surjectif}',
'For a sphere with n=ν+1 individually named punctures, ν≥2, the peripheral automorphism group of Fν has a surjective common-sign map; quotienting inner automorphisms gives the extended pure mapping-class group and its orientation kernel.',
'The topological interpretation uses punctures rather than parametrized boundary circles. Individually indexed peripheral classes and ν≥2 are inherited from the explicit definition on scan89, not newly inserted hypotheses; the page gives no proof of the topological identification.', 'agrees','The surjection and quotient are asserted at lines15–24; no arithmetic-image equality is claimed.')
item([2],'unproved claim',[90,89],['18-24'],r'L_\nu\hookrightarrow\operatorname{Ker}(\chi_\nu^\circ)',
'For ν≥2, Lν≅Fν has trivial center, so g↦(int(g),id) is injective. For ν=1 it is not.',
'The ν≥2 restriction is read at the immediately preceding package MPL_138_046-089_transcription.tex:1673 (scan89), not supplied by a conjectural repair.', 'overstates',
'The earlier note correctly identifies the center issue but treats scan90 in isolation; scan89 explicitly imposes ν≥2.',{2:'The prior package supplies ν≥2 at scan89, line1673; the dossier-level statement therefore has the needed hypothesis. Retain the ν=1 counterexample only as a boundary check.'})
item([3],'unproved claim',[90],['26-30'],r'On sait que $\mathcal T_2^\circ=1$',
'The pure orientation-preserving mapping-class group of a three-punctured sphere is trivial; for n≥4 the pure sphere braid group maps onto it with central C2 kernel.',
'This formulation assumes punctures, not fixed boundary circles; the uncertain /Z2 must remain a reading issue.', 'agrees','The ν↦ν+1 shift is explicit in line24 and nontriviality ν≥3 is inserted at29.')
item([4],'unproved claim',[90],['33-43'],r'\overline B_\nu/\widehat L_\nu=\widehat{\mathcal T}_\nu',
'The profinite completion of the discrete peripheral mapping-class group is identified with its closure in the outer automorphism group of the profinite punctured-sphere group.',
'This is a congruence comparison, not merely a definition; the inherited topological and labeling conventions matter.', 'agrees','The vertical hook at34 and equality at38 contain the additional injectivity/completion assertion.')
item([5],'conjecture',[90],['44'],r'$\widehat{\mathcal T}_\nu$ invariant dans $\Gamma_\nu$?',
'Is the closure of the extended pure discrete mapping-class group normal in the full profinite peripheral outer automorphism group Γν?',
'Normality is the question indicated by invariant; no identification of Γν with GT or the arithmetic image is imposed.', 'agrees','This is explicitly a question and not a theorem or a self-normalizer assertion.')
item([6],'reading question',[90],['44'],r'$\widehat{\mathcal T}_\nu^\circ$ \unsure{dist. ds} $\Gamma_\nu^\circ$?',
'Under the natural expansion distinguished in, is the completed oriented pure subgroup normal in the kernel of the profinite orientation character?',
'The abbreviation expansion remains conditional and the oriented question is separate from the full-group question.', 'agrees','The second question is separately written on line44; the abbreviation remains uncertain.')
item([7],'withdrawn in the same text',[90],['46-48'],r"Quand a-t-on $\widehat{\mathcal T}_\nu^\circ=\Gamma_\nu^\circ$; c'est faux pour $\nu=2$",
'The proposed equality is explicitly denied when ν=2; its validity for other ν is not settled here.',
'The note does not specify a nontrivial witness in Γ2°; any Galois-theoretic witness is additional argument.', 'agrees','The negative insertion at48 qualifies the equality at46 and is not a group-theoretic retraction.')
item([8],'unpursued implication',[91],['52-56'],r'L_\nu^\varepsilon=\{\lambda_i\mid\lambda_0\cdots\lambda_\nu=\lambda_i^{\varepsilon_i}=1\}',
'The peripheral presentation is extended by cone-point orders εi∈[1,∞]; for finite εi this is the usual orientable sphere-orbifold group presentation.',
'For εi=∞, omission of the power relation is a modern convention, not an ink decision; no universal surface-cover theorem is stated.', 'agrees','The page contains only the variant presentation and its infinity-range insertion.')
item([9,10],'reading question',[93,94],['61-90','108-119'],r'\pi_i=\operatorname{Aut}_\pi(T_i)\quad\text{commutant de }\pi',
'A right Γ-torsor C transports a Γ-group π, equivariant π-torsors Ti, their centralizer groups and stable inertia subgroups by contracted products. Inverse transport requires an opposite torsor and specified left/right actions.',
'The categorical contracted-product convention is a reconstruction; the final double-torsor inverse expression at85 is not a well-defined identity without its missing action conventions.', 'agrees','Scan94 explicitly defines the commutant, supporting but not deciding the commutants/commutatifs alternative on93; the inverse formula is still doubtful.')
item([11],'reading question',[94],['94-101'],r'C=\operatorname{Isom}(\overline{\mathbb Q},\unsure{\mathbb C})',
'The comparison torsor can be Emb(Qbar,C), or Isom(Qbar,Qbar_C); it cannot literally be the set of field isomorphisms from Qbar onto C.',
'Changing the codomain to the algebraic closure of Q inside C is only an alternative suggested by cardinality and algebraicity.', 'agrees','Qbar is algebraic over Q and countable, whereas C is not; the uncertain target must be checked on ink.')
item([12,15],'unproved claim',[94,95,96],['97-105','137-158','179-195'],r'\text{pas compatible avec }\Gamma;\quad l_1l_2\cdots l_n=1',
'Basepoint and path choices give actual Γ-actions and representatives of peripheral conjugacy classes; a product-one peripheral system requires simultaneous ordering and compatible conjugates.',
'The canonical unmarked formulation uses outer actions/groupoids. Arbitrary independent representatives or their powers do not automatically satisfy the sphere relation.', 'agrees','The choice-dependent comparison is explicitly declared non-Γ-compatible and the product-one calculation is unfinished.')
item([13,14],'unproved claim',[93,94,95],['88-90','114-119','162-171'],r'\varprojlim_n\mu_n(\overline{\mathbb Q});\quad\text{indépendant de }i',
'For rational punctures of P1_Q, with enough punctures for the local inertia inclusion, tame geometric inertia is ΓQ-equivariantly Zhat(1), hence each peripheral action has the same cyclotomic character.',
'The independence is of puncture index i; an independence of ν would require a specified comparison across configurations. This distinction does not decide the alternative glyph at90.', 'agrees','The unambiguous phrase on95 and Tate-module expression on94 support the common-character account, with no centralizer theorem implied.')
item([16,18,19,20],'reading question',[95,96],['162-171','200-211'],r'\widetilde I_i=C\wedge_\pi I_i;\quad\pi\prime\simeq\operatorname{Aut}(I_i)',
'If the acting group is ΓQ, its quotient by kerχ is Zhat×, and the compatible-primitive-root object is the induced cyclotomic torsor C/kerχ. The original full ΓQ-torsor is not thereby identified with that quotient.',
'The π/Γ substitution, σ/γ agreement and replacement of C by its cyclotomic quotient are proposed repairs, not transcription changes; image=all automorphisms additionally uses cyclotomic surjectivity.', 'agrees','No π-action on C is declared; line211 has omitted quotient data under the earlier ΓQ-torsor meaning. The four notes concern the same unfinished quotient paragraph.')
item([17],'reading question',[96],['179-198'],r"\alpha'_i(\varphi\gamma)=\alpha'_i(\varphi)\gamma_{\pi_i}",
'Assuming the two equivariance formulas and Γ-stability of Ii, the image α′i(φ)(Ii) is independent of φ for fixed i.',
'This follows by cancellation and torsor transitivity; it does not compare different punctures.', 'agrees','Direct substitution gives the displayed cancellation; image independence supports φ in the i/φ doubt but leaves the ink unchanged.')
item([21],'unpursued implication',[94],['121-130'],r'E_i/I_i=\widetilde E_i',
'Inertia orbits identify points in a branch fibre, but the orbit set alone forgets ramification lengths: (2,2) and (3,1) both give two orbits on four letters.',
'The four-letter example is the earlier run’s explanatory counterexample, independently retained as elementary reconstruction.', 'agrees','The diagram distinguishes transported action, forgetful functor and orbit quotient; it does not claim that the bare orbit set is a complete ramification invariant.')
item([22,23],'unproved claim',[98],['225-255'],r"p'(s')=\nu(\varphi,s)p(s),\quad\nu(\varphi,s)=\operatorname{Card}(\varphi_s^{-1}(s))",
'The literal fibre-cardinality morphism law fails composition and fails the standard cubic-star quotient. For cover morphisms the appropriate multiplier is local ramification at a source cell, not the number of cells in its target fibre.',
'The category counterexample uses source weights (2,4,4) above (2,2) above (1), and singleton degree-one A,F sets; every displayed hypothesis is satisfied separately, while the composite fails.', 'agrees','Both asserted category and functor are contradicted by the literal equations. Restricting to isomorphisms would avoid these counterexamples but changes the surviving morphism text.')
item([24,25,27,107],'unproved claim',[98,99,100,129],['258-271','302-303','1543-1548'],r'la catégorie des cartes orientées C_0-épinglées est rigide',
'Cell pinning labels the degree-bearing sets S,A,F, not flags. The pinned automorphism group is ker(Aut(C)→Aut(Fac(C))); it can be C2 for the genus-one map r=(1234),σ=(13)(24),ρf=r. Genus-zero geometric pinned covers are rigid since a Möbius automorphism fixes three points.',
'The kernel formula and counterexample are present-run rechecks of earlier-run reasoning; the genus-zero qualifier is a repair, not his unrestricted statement. Fixing cell sets is weaker than isotopy through map automorphisms.', 'agrees','The actual definition at261–267 has no flag marking. The verify margin at302 is genuine, and the torus half-turn also refutes the cell-fixing equivalence at1546.')
item([26],'unproved claim',[99],['273-279'],r'\prod_{n\in\mathbb N^*}(a_n!b_n!c_n!)',
'If γ=Aut(C0), the number of pinned isomorphism classes above an unpinned C is |γ|/|im Aut(C)|=|γ|·|KC|/|Aut(C)|; the total is its sum over unpinned classes. The displayed factorial product gives |γ| correctly.',
'The orbit-size denominator repairs the manuscript’s multiplication formula; the groupoid mass has denominator |Aut(C)| instead.', 'agrees','The cubic star has six labelings modulo C3, hence two pinned classes, which the manuscript itself records on104; its general multiplication formula gives six.')
item([28],'unproved claim',[100],['285-303'],r'un foncteur contravariant ... qui est représentable',
'The raw isomorphism-class presheaf of all cell-pinned tame covers is not representable: E_d:d y²=x³−x, f=x², d=1,2, with individually pinned ramification points, become isomorphic over Q(√2) but not over Q.',
'This explicit twist obstruction is the earlier run’s construction, checked here against all ramification and pinning conditions. A coarse geometric class space or a stack is a different functor.', 'agrees','The claimed fine representability rests on the false all-genus rigidity. Non-separatedness as an étale sheaf defeats representability already over Q.')
item([29],'unproved claim',[101],['307-314'],r'Le stabilisateur ... correspond ... aux autom du rev.',
'On geometric pinned isomorphism classes, the relabeling stabilizer is Aut(C)/KC, the effective action on cell labels; it is the full deck group only when KC=1.',
'The effective quotient is the corrected statement; relative-family descent requires further hypotheses.', 'agrees','For the regular C4 torus cover, KC=C2 and the relabeling stabilizer is C2, so the unrestricted full-group identification fails.')
item([30],'unproved claim',[100,101],['303','307'],r'fini ... \mathbb Z[1/\delta!];\quad\text{non ramifié en les }p>\delta',
'For a degree-δ cover its faithful monodromy lies in Sδ and has order dividing δ!; primes p>δ are therefore prime to that group. Tame specialization supports unramified finite geometric-class actions away from those primes.',
'This validates the prime bound for the corrected finite class space, not every claimed property of the nonrepresentable fine functor over Z.', 'agrees','The numerical group-order implication is sound; the scheme claim must be separated from the failed representability premise.')
item([31,32],'unproved claim',[101,102],['314-320'],r'\bigcap\text{conjugués de }H=\{e\};\quad E=G/H',
'A connected cover with faithful monodromy G corresponds to a core-free subgroup H and a generating triple with ρsρfσ=1, σ²=1 and prescribed cycle partitions. Geometric Galois-closure group type is Galois-stable and hence defines a clopen subset of a finite étale Q-class space.',
'Connectedness is required for the single transitive G/H description. The clopen scheme statement is conditional on the corrected geometric class space, not the raw functor.', 'agrees','The group criterion is exactly the line320 construction; nothing here proves its all-base family assertion.')
item([33],'reading question',[102],['320'],r"la classe d'isom. de G muni de ... n'est pas déterminée ... X\to\mathbb P^1_{\mathbb C}",
'A fixed complex cover over the fixed target determines its oriented dessin and its monodromy tuple up to simultaneous conjugacy after standard loops are chosen. Actual named elements in an independently identified abstract G depend on choices.',
'The distinction may explain part of the warning, but the parenthetical claim about the oriented map type conflicts with the standard fixed-target dictionary; no missing qualification is supplied.', 'agrees','The note correctly flags the exact negative sentence; the contradiction is with isomorphism classes, not with arbitrary element names.')
item([34,37,38,39,40],'unproved claim',[99,100,101,102,103,123],['275','285-327','1176'],r'M_{C_0}^{\alpha}(\overline{\mathbb Q})\simeq M_{C_0}^{\alpha}(\mathbb C);\quad\Gamma\text{ opère}',
'Finite oriented cartographic classes of prescribed type correspond to three-point covers over Qbar; a finite continuous ΓQ-set determines a finite étale Q-algebra. Constant relabeling by γ commutes with arithmetic conjugation.',
'The finite Galois-set conclusion is sound independently of the failed raw fine functor. Equality with C-points for an existing finite étale Q-algebra is formal; the map-to-Qbar existence input is separate.', 'agrees','The dictionary, arithmetic action and commutation are explicit on103. These five notes discuss the same finite-class construction rather than five independent historical discoveries.')
item([35,41],'reading question',[103],['329-331'],r"l'opération ... peut ne pas être triviale",
'The arithmetic action on unpinned classes can be nontrivial, as a chiral dessin is exchanged with its mirror by complex conjugation; universal nontriviality and faithfulness are not asserted.',
'The difference from the earlier modernization’s ne peut pas être triviale is textual, not a new ink reading.', 'agrees','The surviving text has peut ne pas, so the stronger alternative quoted elsewhere is not this transcription.')
item([36],'self-flagged step',[99,103],['281','324-327'],r'Définir ici C_{C_0} et C_{C_0}^{\alpha}',
'The author leaves an instruction to define the pinned class sets and relabeling action, then uses them on103.',
'The intended quotient is the orbit set of labelings; it does not supply the missing fine-moduli argument.', 'agrees','The instruction is explicit in the margin; it is a drafting obligation rather than a conjecture of new mathematics.')
item([42,44,45],'idea of the earlier run',[98,99,100,101,102,103,104,129],['261-331','1522-1548'],r'certains cas élémentaires',
'This range asserts the map-to-algebraic-cover direction and finite arithmetic actions, but neither the converse for every Qbar-curve nor global faithfulness, let alone faithfulness on regular dessins. Each fixed finite type has finite image and cannot faithfully represent ΓQ.',
'The bounded corpus comparison and finite-kernel observation are earlier-run analysis; later Belyi and regular-dessin theorems are comparisons, not attributed manuscript statements.', 'agrees','A complete read of these leaves finds no universal converse or faithfulness assertion; the finite-action argument is elementary.')
item([43],'title, date or page count',[106,110,133],['435','621-629','1663-1669'],r'11.1.1977;\quad12 Décembre 1977;\quad21 DECEMBRE 1977',
'The retained package has43 scan markers:90,91,93–133. Dated reused matter constrains those physical sheets but not the date of every mathematical leaf or a priority claim for Belyi’s theorem.',
'A terminus post quem assumes handwriting was added after the printed/typed matter. No mathematical colophon is supplied.', 'agrees','Dates belong to a recommendation draft and university notices; scan92 is absent, not an inferred blank manuscript page.')
item([46,49,50],'unpursued implication',[103,104,105,106,107,108,109,110,111,112],['331','333-788'],r"On va essayer de déterminer l'opération de \gamma\times\Gamma",
'The announced elementary programme is partly realized by small maps and a sextic passport. Its three-parameter arithmetic orbit has S3 action, one real member and a conjugate pair; its parameter field is Q(∛2).',
'The completed elimination and field identification are later-run computations, not written results of these leaves. They do not determine any CM/GT tower image or classify all profinite torsion.', 'agrees','The source announces elementary examples and leaves the P-versus-discriminant question unresolved; the earlier notes correctly delimit their finite calculation.')
item([47],'idea of the earlier run',[90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133],['1-1683'],r'Cartes sphériques en bas degrés;\quad Opérations sphériques',
'No identification with modular curves X(n), no general-ring regular-polyhedron definition, and no bi-icosahedron/M0,5 comparison is stated in this bounded range.',
'This is a bounded negative text finding, not a negative theorem about the archive or those external projects.', 'agrees','The whole retained transcription was read; small group names and covers do not supply those absent project-specific constructions.')
item([48],'idea of the earlier run',[122,123,124],['1130-1232'],r'préfaisceau;\quad sections',
'Naturality for map-covering morphisms is weaker than compatibility with all moduli boundary, gluing and forgetful morphisms.',
'This comparison with other projects is earlier-run analysis, kept apart from manuscript claims.', 'agrees','The displayed category concerns finite maps and finite operators; no higher moduli tower is constructed.')
item([51],'unproved claim',[104,105],['344-411','429-431'],r'f(z)=\tfrac4{27}\tfrac{z^3}{z-1}',
'The seven displayed functions z, z²,−4z(z−1), z²/[4(z−1)], z³,4z³/[27(z−1)],27z(z−1)²/4 have the asserted branch partitions over0,1,∞.',
'The exact factorization/derivative certificate is supplied in this run; the functions themselves are his.', 'agrees','All seven formulas are present and their rational-function degrees and fibres are directly checkable.')
item([52],'unproved claim',[105],['415-422'],r'2x(x^2+y^2)+(-3x^2+y^2)=0',
'For f=4z³/[27(z−1)], Im f(x+iy)=4y[2x(x²+y²)−3x²+y²]/[27((x−1)²+y²)]. Thus the inverse real axis is the stated union away from the pole, completed projectively.',
'The projective pole interpretation is explicit modern wording of the drawing statement.', 'agrees','The symbolic imaginary-part identity exactly checks the written algebraic curve.')
item([53],'unproved claim',[104],['396-403'],r'C_{C_0}^{\alpha}\text{ a deux éléments}',
'The cubic star z³ has six labelings of its three points over1, modulo the C3 deck group, hence two pinned classes; ΓQ acts through χ3 and relabeling S3 acts transitively.',
'The orbit-of-labelings proof is reconstructed; the conclusion itself is written.', 'agrees','This explicit count also diagnoses the missing denominator in the general scan99 formula.')
item([54,55,64,73],'idea of the earlier run',[106,107,117],['450-493','1039'],r'\rho_f=\rho_s^{-1}\sigma;\quad \rho_s r_5=r_{\unsure{4|2}}',
'With ρs=(123)(45), σI=(14)(36), σII=(14)(56), both groups are S6 and the face permutations are six-cycles. The passport (3,2,1)|(2,2,1,1)|(6), or its dual, has three oriented classes: one real/reflexible class and a mirror pair.',
'The finite enumeration is prior-run analysis rechecked here. The choice4 in the doubtful index is forced by bijectivity with the other entries fixed, but not decided palaeographically.', 'agrees','The two tables provide the actual permutations, and the repeated dual passport does not imply duplicate drawings; exact enumeration records the three classes.')
item([56,57,59,60,61,63],'idea of the earlier run',[107,108,109,111,112],['497-574','585-606','702-757'],r'P(c)=0;\quad Q(c)\ne0;\quad\delta(c)\ne0',
'For H=z³(z−1)²(z−c) and g=z²−(5c+4)z/6+c/2, H mod g=Pz+Q with P=−(25c²−32c+16)(25c³−12c²−24c−16)/7776 and Q=c(5c−8)(25c³−6c²+8)/2592. P has no roots0,1 or common root with Q, but its quadratic factor δ gives the forbidden repeated critical point; the remaining cubic R has arithmetic splitting group S3 and field Q(∛2).',
'The factorizations, nondegeneracy certificates and field change are completions by the earlier run, independently recomputed here; the manuscript supplies the remainder definition and explicitly asks about δ.', 'agrees','The notes correctly retain the source’s P, including its quadratic factor; replacing P directly by R would erase the answer to his question.')
item([58],'reading question',[111],['731-733'],r'c=16/25\pm24i/25',
'The roots of δ=25c²−32c+16 are16/25±12i/25, not the displayed24i/25.',
'The arithmetic correction is separate from a proposed ink reading and is credited to earlier commentary.', 'agrees','Substitution of the written candidate yields a nonzero value; the quadratic formula has denominator50.')
item([62,65,67,68],'reading question',[108,109,111,112],['530-559','598-606','736-740','766'],r'f(z)\unsure{+|-}1;\quad\mathbb Q[c]_{\delta c(c-1)}/P(c)Q(c)',
'The remainder expansion needs the minus sign in D=(α−2)β−(β+1)c and a u factor in its first term; the residual-fibre numerator must be f−1. The intended parameter algebra is Q[c,1/(δc(c−1)Q)]/(P)≅Q[c]/(R), not the literal quotient by(PQ). The isolated f′=0⇒f=0 requires a missing conditional context.',
'These are algebraically motivated alarms, not textual replacements. At c=8/5 the literal quotient retains a Q=0 point with P≠0, and admissible u,v contradict an unconditional zero-critical-value assertion.', 'agrees','The exact source conditions and formulas expose these conflicts; the precise deleted/conditional wording must be settled on scans.')
item([66],'unpursued implication',[112],['773-787'],r"\frac{f'}f=\frac{\varphi'}\varphi-\frac{\psi'}\psi",
'For coprime monic products φ=∏(z−αi)^pi, ψ=∏(z−βj)^qj with disjoint distinct roots and degφ>degψ, f′/f=Σpi/(z−αi)−Σqj/(z−βj). Its numerator over the squarefree product has degree a+b−1 and leading coefficient degφ−degψ.',
'The numerator degree and proposed elimination procedure are reconstructed; the page writes the logarithmic derivative and leaves the final numerator blank.', 'agrees','The subtraction is the mathematical candidate for the doubtful sign and qj symbol, without an ink decision.')
item([69],'withdrawn in the same text',[107],['487-495'],r'\tau_{14},\tau_{43}\text{ ou }\tau_{46}\ ?',
'The transposition alternatives are a cancelled trial preceding a fresh polynomial calculation; no surviving chosen factorization is stated.',
'Correctness of the cancelled powers of ρs does not recover the intended trial word.', 'agrees','The entire block is inside deleted markup; its question is not a live unanswered conjecture.')
item([70],'reading question',[110],['661'],r'=6N;\quad2(\sum p+\sum q+\sum r)',
'If N is the common dart degree, the equality follows by three equal degree sums; the isolated margin does not identify N with the monodromy-group order.',
'This conditional degree interpretation is a reconstruction. The sextic has degree6 and monodromy order720, so the alternatives differ.', 'agrees','The surrounding drawings do not define N or assert regularity; no group-order claim is extracted.')
item([71,72],'unproved claim',[115,116,118],['877-1029','1078'],r'\mathbb Z_2;\quad\mathfrak S_3;\quad\text{rigide}',
'The catalogue labels are finite map symmetries including reversal, not monodromy: degree1 gives C2, the cubic star gives S3, and the cubic loop-tail gives C2. The degree5 passport(4,1)|(2,2,1)|(4,1) consists of a chiral pair, each with trivial full map symmetry and monodromy order20.',
'The symmetry interpretation is inferred from diagnostic cases and verified permutations. Assignment of every rough drawing requires the scan; the live degree5 rigidity mark is distinguished from the deleted degree4 one.', 'agrees','The printed labels match the full-symmetry convention; the examples rule out identifying them with monodromy groups.')
item([74,76],'unproved claim',[99,114,118,120],['273-279','841','1086','1120-1121'],r'n=\sum_s q_s=\sum_f p_f;\quad\text{impossible}',
'Both vertex and face degree sums count darts. A connected map with V vertices has at least V−1 complete connecting edges, hence δ≥2(V−1); folded edges do not connect different vertices. This excludes(2,1,1,1) at degree5 and(2,1,1,1,1) at degree6.',
'The short spanning-tree proof is supplied here; the p/q letter roles differ locally from the precarte definition.', 'agrees','The degree identities and both impossibility annotations are checked under the connected map convention.')
item([75],'reading question',[120],['1106-1108'],r"1 sommet d’ordre3,1 d’ordre2,1 d’ordre2",
'The degree-six heading sums to7, whereas the adjacent passports are(3,2,1), summing to6.',
'Changing the final2 to1 is the mathematical alternative only; it is not made in the transcription.', 'agrees','The internal numerical conflict is direct and affects identification of the catalogue row.')
item([77,78],'withdrawn in the same text',[119],['1093','1102'],r'\deleted{\mathbb Z_2}\ 1;\quad\mathbb Z_2.\mathfrak S_3',
'A degree-six symmetry label C2 is replaced by1. The theta graph carries a dotted C2.S3 label beside a deleted D3×C2; the dot alone does not specify whether the extension splits.',
'The first replacement is a textual withdrawal; the theta notation change need not change the abstract group. Finite permutation models determine the standard theta symmetry group separately.', 'agrees','The deletion states are explicit. They do not authorize reading group1 as trivial monodromy or dot as a nonsplit extension.')
item([79],'reading question',[114],['843'],r'\unsure{\varphi(1)|\varphi(n)}=2',
'The isolated φ-symbol has no supplied definition and cannot be identified with Euler’s totient or an enumeration function.',
'Its coincidence with the degree-one full symmetry order is insufficient evidence of its meaning.', 'agrees','No defining occurrence is present in the retained range.')
item([80],'idea of the earlier run',[113,114,115,116,117,118,119,120],['792-1121'],r'Cartes sphériques en bas degrés',
'A complete catalogue comparison must distinguish oriented classes, their mirror identifications, duality, and deleted versus surviving drawings; a passport alone does not identify one class.',
'This is a proposed research task rather than his assertion that the catalogue is exhaustive.', 'agrees','The repeated passport and chiral examples demonstrate why a systematic list of sketches is not itself a completeness proof.')
item([81],'self-flagged step',[121],['1125'],r'axiomatique provisoire',
'The spherical-operation axioms are explicitly a working framework.',
'No completed general classification is inferred from the title.', 'agrees','The qualification is written on the section title leaf.')
item([82,83,84],'unproved claim',[122],['1130-1167'],r'F^\natural(C)=F(X)/\operatorname{Aut}^\circ(C)',
'For a contravariant functor with descent F(X/H)=F(X)^H, quotienting by identity-component map automorphisms is proposed to yield a presheaf, extended by F(C)^G/Aut(C,G)°. This requires liftability of isotopies and independence of lift modulo the source identity component.',
'The page sketches the lift argument but writes Aut(X)° where Aut(C)° would be needed. These groups cannot be identified without an additional convention.', 'agrees','The claimed presheaf and operator extension are real assertions; their descent proof and the X/C notation remain unfinished.')
item([85,86,87],'reading question',[123],['1171-1182'],r'\Gamma(F^\natural)\simeq\varinjlim_{H_\alpha} F^\natural(C_\alpha,G_\alpha)',
'Global compatible sections are to be reconstructed from finite regular cartographic covers, and for the powerset functor from subsets of the reference sphere modulo an isotopy group.',
'The written colimit needs an indexing/variance convention; the denominator Aut°(S, is unfinished. The qualifier inv is compatible with normal subgroups and differs from a later claim that the source said free.', 'agrees','The note preserves genuine incomplete formulas instead of deriving an unrestricted universal classification.')
item([88],'unproved claim',[123],['1190-1195'],r'\mathcal P(S)^{\uline c}/\operatorname{Aut}(S,\uline c,0,1,\infty)^\circ',
'The unoriented construction restricts to conjugation-invariant reference subsets modulo compatible isotopies.',
'Commutation with one real involution is not commutation with all ΓQ.', 'agrees','Conjugation is explicitly the equatorial involution; no arithmetic equivariance follows from this paragraph alone.')
item([89,90,91,92],'unproved claim',[123,125],['1196-1201','1235-1258'],r'X\setminus A_X\text{ a comp. conn. }\simeq\text{disques}',
'For a finite tame embedded connected graph A⊂S², inverse images under finite covers branched over{0,1,∞} are cellular exactly when each complementary disc contains at most one of those branch values, in the category allowing folded edges.',
'This is a clean finite reconstruction of the damaged criterion. The earlier modernization’s bound on points of A itself is false: A=[0,1] is the identity construction. Wild/infinite subsets are excluded.', 'agrees','The face-center instruction at1256–1258 supports a face-wise interpretation, but the damaged subject, negative and sphere exponent remain scan questions.')
item([93,94,95,96,97],'unproved claim',[124,125,128],['1211-1232','1260-1271','1514-1518'],r'A_X=(\varphi f)^{-1}([0,1]);\quad\text{cas exceptionnel}',
'A suitable reference graph with vertex/midpoint/face choices defines an outer branched sphere map φ, and pullback by f is postcomposition φ∘f. Marked values must map into{0,1,∞}; strict index2 over1 needs extra local conditions. A leaf at1 is exceptional because w↦w² lifts it to an ordinary edge midpoint.',
'The local explanation and sufficient strictness condition are reconstructions; the manuscript explicitly leaves the exceptional case open. Requiring all old branch values to avoid1 is sufficient but excludes the identity exception.', 'agrees','The composition equality is exact, while the exceptional question at1518 and uncertain converse arrow are not a completed classification.')
item([98],'unproved claim',[127],['1352-1356','1386-1392','1418-1421'],r'c=0\text{ ou }2',
'For the nondegenerate Möbius map m_c(z)=z/(cz+1−c), m_c²=id if and only if c=0 or2 over characteristic0; c=1 is excluded. For c=2 its fixed points are0 and1.',
'The equality with denominator2−1/z is the algebraic alternative to the uncertain2−1/2.', 'agrees','The matrix multiplication and fixed-point equation check directly with the nonconstant hypothesis.')
item([99,100],'unpursued implication',[127],['1444-1446','1500-1509'],r'g(z)=(2f(z)-1)^2',
'For q(t)=(2t−1)², g=q∘f has g=0 exactly when f=1/2 and g=1 exactly when f=0 or1. This preserves the three-point branch set when f is Belyi, but need not preserve index≤2 at1: f=z³ gives index3 at z=0. Cleaning with4f(1−f) makes every point over1 have index2.',
'The strictness counterexample and cleaned alternative are earlier-run analysis rechecked here; the page itself flags a possible unramified-at-marked-point requirement.', 'agrees','The fibre formulas are correct, and their local ramification is a separate condition.')
item([101,102,105],'unproved claim',[126,131],['1276-1288','1323-1330','1587-1592'],r'Le noyau ... est fini;\quad\text{si un autom. d’ordre fini est isotop. à id ... c’est id}',
'For a connected finite cellular map, a finite-order automorphism isotopic to identity through map automorphisms is identity; therefore a finite isotopy kernel is trivial. The analogous claim for infinite kernels fails, e.g. positive dilations on an orange.',
'The reduction to periodic interval/disc homeomorphisms is supplied under finite cellular hypotheses. The surviving condition concerns a finite kernel, not the cancelled finite-stabilizer version.', 'agrees','This is the actual revised condition and the proof target on126; no general infinite-group centralizer theorem is inferred.')
item([103,104],'unproved claim',[126],['1295-1304'],r'l’espace des rigidifications ... invariantes par G est contractile',
'Existence of a G-invariant rigidification, equivalence with realizing a combinatorial G-action, and contractibility of its choice space are asserted.',
'The space’s topology and full rigidification definition are not supplied here; the finite-order disc argument proves a different implication and cannot substitute for the contractibility construction.', 'agrees','The written évident chain and contractibility line do not include the necessary equivariant construction.')
item([106,127],'withdrawn in the same text',[129,130],['1522-1548','1556-1573'],r'Unicité d’un tel \varphi? ... Or c’est faux déjà pour la sphère',
'For finite maps the cover-classification input supplies an isotopic map isomorphism between two compatible strict Belyi functions; uniqueness of the function would require the holomorphic identity-component map group to be trivial. The author immediately exhibits sphere exceptions.',
'The finite cover-classification and removable-branch-point interpretation are background reconstruction; no infinite classification is supplied.', 'agrees','The proposed unconditional uniqueness is rejected on the same leaf before later tentative repairs.')
item([108,109],'reading question',[130],['1556-1573'],r'a,b,c,d\in\mathbb R;\quad\operatorname{Aff}(1,\mathbb C)',
'For a real-equator map preserving its faces and one fixed vertex∞ the identity group is z↦az+b with a>0,b∈R; with two fixed vertices0,∞, or for the dual single-edge ray, it is z↦az with a>0.',
'The real groups and one-dimensional dual group correct the written complex labels; the sign convention in the matrix is separately uncertain.', 'agrees','Preservation of real equator and individual faces forces real coefficients and positive orientation; the full complex affine group is too large.')
item([110,111,112],'self-flagged step',[130,131],['1574-1590'],r'une face dont l’ordre soit au moins trois;\quad J’ai l’impression que oui',
'For a connected finite holomorphic cellular map, the existence of one face with at least three corner prime ends forces an identity-isotopic holomorphic map automorphism to be identity. The condition is sufficient, but the proposed classification of its failures by I and oranges is false: z⁴/[4(z²−1)] has face orders2,1,1 and is neither.',
'The prime-end proof and two-loop counterexample are reconstructed; one face per component is the written hypothesis, not every face.', 'agrees','The manuscript explicitly qualifies its expectation to finite maps; its claimed equivalence with a short exception list is stronger than the valid sufficient statement.')
item([113,114,115],'conjecture',[129,131],['1529-1533','1587-1595'],r'si n\geq2, il n’y a pas d’automorphismes hol.\neq id',
'For every n≥1, F_n(z)=4z^n/(1+z^n)² realizes a strict holomorphic orange: its embedded graph is the n rays z^n≥0. Positive dilations preserve that graph and give distinct compatible functions, so the claimed n≥2 rigidity and the tentative final exception list fail.',
'The strict rational models are earlier-run counterexamples rechecked here; no threshold is altered in the transcription.', 'agrees','The counterexamples meet the exact index2 condition over1 and show that the additional oranges are not excluded by the source definition.')
item([116],'self-flagged step',[131],['1597-1600'],r'voir s’il s’applique aux cartes infinies',
'The conformal uniqueness argument and its extension to infinite maps are expressly left unfinished.',
'A plausible extension needs local finiteness, well-controlled face prime ends and a stated holomorphic covering category; the finite proof does not establish it.', 'agrees','This is an explicit outstanding step, not an editorial uncertainty marker.')
item([117],'unproved claim',[131],['1602-1606'],r'centres des faces ... les cas I) II) III) sont éliminés',
'In the displayed spherical examples, marking face centers removes the continuous Möbius freedom. Marking the edge-midpoint fibre removes the dilation freedom of II/III, but one midpoint still leaves positive dilations in I.',
'The statement is checked for these normalized examples only, not asserted for every infinite marked map.', 'agrees','The added marks are explicit; three fixed points give the bounded Möbius argument.')
item([118,119],'unproved claim',[132],['1618-1636'],r'Considérons les conditions;\quad mêmes groupes d’autom. hol.',
'The draft distinguishes existence of a compatible operation representative, isomorphic canonical complex surfaces, and a complex structure compatible simultaneously with both graphs and their supremum. Primed conditions additionally preserve holomorphic automorphism groups.',
'The page does not assert their equivalence; an equivalence or automorphism-preservation theorem would be an additional research claim.', 'agrees','The conditions are listed separately without a chain of implications.')
item([120,121],'reading question',[132],['1638-1647'],r'1\text{ en }\{0,\infty,1\};\quad\varphi(1)=1\Rightarrow\text{étale en }1',
'The special outer map may send1 to0 or∞ and is required unramified there only if it fixes1. Strict-input postcomposition needs φ({0,∞})⊂{0,∞}, index1 at1 if φ(1)=1, and index exactly2 at every other point over1.',
'The exact-index formulation follows from multiplicativity; replacing it by ≤2 may admit unwanted unramified preimages unless another graph condition excludes them. It is not an emendation.', 'agrees','The source permits all three images of1 and the uncertain exception qualifier; a summary saying that1 is always fixed is narrower than this text.')
item([122,123,124,125,126],'idea of the earlier run',[103,107,108,109,110,111,112,124,132],['327-331','499-757','1224-1232','1638-1647'],r'(\varphi f)^{-1}([0,1])',
'Postcomposition by a Q-defined Belyi-extending map is Galois-equivariant and pulls back any Galois invariant to another one. Arbitrary complex outer maps need not commute with ΓQ; the cleaned nonrational sextics give concrete failures. Mirror reversal on the S3 sextic orbit also fails to commute with every arithmetic element.',
'This is earlier-run comparison with Wood and Jones, not his theorem. G_K-equivariance is sufficient for a K-defined map, not a claim that larger equivariance is impossible; new invariants separate some orbits but are not proved complete.', 'agrees','The manuscript proves a pullback/composition identity and supplies no rationality condition; the external arithmetic theorem requires that added hypothesis.')

for obj in items:
    # Source quotation macros were entered as raw strings with escaped slashes.
    obj['his_words']=obj['his_words'].replace('\\\\','\\')
    if obj['id'] in ['SA09-254','SA09-255']:
        obj['lines'].append('MPL_138_046-089_transcription.tex:1664-1724')
        if 89 not in obj['scans']:obj['scans'].insert(0,89)
assert sorted(int(r['entry_id'].split('#')[1]) for r in entries)==list(range(1,128))
(W/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
with (W/'entries.tsv').open('w') as f:
    wr=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');wr.writeheader();wr.writerows(sorted(entries,key=lambda x:int(x['entry_id'].split('#')[1])))
print(json.dumps({'entries':len(entries),'items':len(items),'corrected':[r['entry_id'] for r in entries if r['verdict']=='corrected']},indent=2))
