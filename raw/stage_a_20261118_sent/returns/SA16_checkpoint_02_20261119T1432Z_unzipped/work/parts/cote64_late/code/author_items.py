"""Manually authored scholarly consolidation after full note-and-passage reading.
This program serializes decisions; it never infers a verdict from keywords/headings.
Read evidence is preserved in outputs/notes_* and outputs/tex_*.
"""
from pathlib import Path
import json,csv,datetime
BASE=Path('/workspace/scratch/208fb206de03/work/parts/cote64_late')
A='MPL_64_078-115';B='MPL_64_116-157'
items=[];entries=[];keys={}
def I(key,src,kind,scans,lines,quote,statement,reconstruction,check,reason,corrections=None):
 id='SA16-'+str(501+len(items));keys[key]=id
 sources=[(A if p=='A' else B)+'#'+str(n) for p,n in src]
 item=dict(id=id,sources=sources,kind=kind,cote='64',scans=scans,lines=lines,his_words=quote,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason)
 items.append(item)
 for k,s in enumerate(sources):
  v='kept' if k==0 else 'merged'
  why=reason if k==0 else 'Same mathematical or documentary object as '+id+'. '+reason
  if corrections and s in corrections:v,why=corrections[s]
  entries.append(dict(entry_id=s,item_id=id,verdict=v,reason=why))
 return id
I('square_group',[('A',1)],'withdrawn in the same text',[78],A+':6–31',r'\mu_4^{\deleted{\unsure{*}}}\simeq\operatorname{Aut}^{+}(Q_0)',
 'For an oriented combinatorial square over a base where 2 is invertible, its rotation group is the four-element group scheme μ4 after the specified orientation identification; μ4* is a two-element torsor, not that group.',
 'The geometric cardinality comparison is our check; the deletion of the asterisk is already present in the transcription.', 'agrees','The note correctly retains the authorial deletion and distinguishes group from primitive-root torsor; Hua comparison is only a reported earlier reading.')
I('square_example',[('A',2)],'idea of the earlier run',[78,86],A+':15–31,193–202',r's_{i\prime}=i\,s_i',
 'Earlier-run/Hua example: over Z[1/2], Q0=Spec Z[1/2,s]/(s^4+4), with s_i=1-i after i²=-1, is a μ4-torsor; quotient by sign is μ4* via -s²/2.',
 'This explicit polynomial model is not written on the manuscript page. We independently verify it as an example of the described square.', 'not on the page','The page specifies side endpoints and their relation, while the explicit x^4=-4 model is correctly credited to Hua by the note.')
I('tensor_twist',[('A',3)],'unproved claim',[80,81],A+':65–83,98–106',r'M^{\sharp}\otimes M^{\sharp}\simeq M^b',
 'The literal identity is false for a general O_S-module M. For scalar torsor twists the valid functorial identity is (M^sharp)⊗2 ≅ (M⊗2)^b. With trivial torsors and M=O(1) on P¹_C the written formula would identify O(2) and O(1).',
 'The corrected identity is a mathematical reconstruction, not a changed reading. The later O(2) specialization is written correctly.', 'agrees','The definition in the margin at line69 is M^sharp=M⊗O_S^sharp; line74 omits a tensor power that line104 supplies in the specialization.')
I('pinning_torsors',[('A',4)],'unproved claim',[82,83,87,88,119],A+':124–151,209–241; '+B+':149–158',
 'Pour α fixé ... torseur sous μ2; L_E/S/μ2 ≃ μ4*∧ω_J',
 'For E/S with 2 invertible, Legendre pinnings with a fixed orientation identification α:μ4*≅ω_J form a μ2-torsor. Allowing α to vary gives a μ4-torsor L_E/S, with quotient the μ2-torsor μ4*∧ω_J. Q_E/S is the naive μ4-torsor, with quotient ω_J, and L≅Q_E/S∧μ4 Q0.',
 'Modern sheaf language spells out the group actions; the data and quotient formulas are on the pages.', 'agrees','The fixed/all distinction is explicit at83 and87–88, and recurs at119. No general level-N assertion follows.')
I('residual_aut',[('A',5)],'unproved claim',[79,84,85],A+':50,162–183','n’est pas rigide; exceptionnelle hexagonale',
 'Legendre pinning without ordering J may retain even permutations of the three nonzero 2-torsion points fixing t. Over an algebraically closed field of characteristic not 2 or 3 this residual stabilizer is C3 precisely at the equianharmonic parameters.',
 'Characteristic3 needs a separate fixed-scheme analysis; the manuscript base only excludes2.', 'agrees','The note correctly distinguishes the nonrigid Legendre problem at84 from the already combined rigid Legendre–Jacobi problem at79.')
I('fine_moduli',[('A',6)],'unproved claim',[79,80,81,82,83,85,86,91],A+':41–58,108–154,175–204,295–305','représentable par le schéma U_03×μ4*',
 'Over S0=Spec Z[1/2], the category of elliptic curves with the stated Legendre pinning and an ordering J≅{0,1,∞} is asserted equivalent to the functor U_03×μ4*. Its universal tangent line is O(1)^sharp, trivialized to O(1) after choosing i. Over Z[1/2,i], direct pinnings give U_03.',
 'This is the precise manuscript assertion. Rigidity follows from level2 automorphisms ±1 and the tangent pinning; existence and descent of the specified symmetric normalization still require the requested reconstruction.', 'agrees','The note correctly names all extra data and the proof boundary at83; standard Legendre structures in modern references are not automatically this symmetric normalization.')
I('dicyclic',[('A',7),('A',41)],'unproved claim',[90,91],A+':269–305',r'\mathbb D_3\prime=S_3\times_{\mathbb Z/2}(\mathbb Z/4)',
 'After choosing i, D3′={(g,z)∈S3×C4:sgn(g)=z²} has order12 and is C3⋊C4 where C4 acts through inversion on C3. Its central extension 1→C2→D3′→S3→1 does not split.',
 'Nonsplitting and the semidirect presentation are our independent deductions from the displayed fibre product. The alleged La Longue Marche normal-complement identification is retained solely as a project lead.', 'agrees','The displayed fibre product determines the finite group; each transposition lift has order4. The external normal-complement theorem is not available as a source here.')
I('abelianization',[('A',8)],'unproved claim',[92],A+':347–366',r'D_{3,ab}\prime\simeq\mu_4',
 'The canonical projection D3′→μ4 is its abelianization; its commutator subgroup is the order3 subgroup, and its centre has order2.',
 'The abelianization is his inserted claim. Centre and explicit commutators are our check.', 'agrees','Commutation with a transposition lift inverts a three-cycle, so commutators generate C3; the quotient is C4.')
I('line_action',[('A',9)],'unproved claim',[86,89,90,91,92],A+':204,248–269,307–366',r'T_{g,λ}ξ=λ(g,λ).ξ; T_{g,λ}τ=λ²sg(g)(g,λ).τ',
 'On the modular parameter, (g,λ) acts on U03 by g and on μ4* through sgn(g)λ². The modular tangent-line linearization is the tautological one multiplied by λ. On its tensor square and the quotient tangent it acquires λ² and λ²sgn(g), respectively; the last scalar is1 on D3′.',
 'We separate three line/tangent actions and check scalar compatibility; we do not identify χ4 with an arithmetic cyclotomic multiplier.', 'agrees','Base action47 and line actions51–54 answer the preceding requests to explicate the modular group. The exponent uncertainty in52 remains a scan issue.')
I('left_right',[('A',10)],'reading question',[89],A+':248–256','action [inserted à g.]',
 'The retained transcription specifies a left action of μ4×S3; the earlier modernization reportedly calls it a right action. Comparison requires inversion with a declared convention.',
 'No change of ink is proposed; absence of the modernization in the attached sources limits the external comparison.', 'agrees','The left-action insertion is present. An opposite-action convention is mathematically available, but cannot be silently substituted.')
I('special_parameters',[('A',11)],'unpursued implication',[84,85],A+':162–175','t=ρ(t)',
 'For the standard Legendre coordinate λ, an order3 transformation λ↦1/(1−λ) fixes λ²−λ+1=0. In characteristic not2,3 these two values have j=0. The harmonic orbit {−1,2,1/2} has j=1728.',
 'The explicit λ-coordinate calculation and normalized j formula are earlier-run additions; the page states the fixed-locus/hexagonal criterion in t.', 'agrees','The deduction is compatible with his fixed-locus statement, provided the change of branch-order convention is stated.')
I('char3_special',[('A',12)],'idea of the earlier run',[80,84,85],A+':65,162–175','car. rés. ≠2',
 'In characteristic3, λ²−λ+1=(λ+1)², all six anharmonic transformations fix λ=−1, and the order3 fixed subscheme is nonreduced. For y²=x³−x over an algebraic closure of F3, translations x↦x+a and (x,y)↦(−x,iy) generate the order12 origin-preserving automorphisms.',
 'This explicit characteristic3 computation is an earlier-run extension; it is not written in the excerpt. The subgroup retaining a Legendre pinning must still be distinguished from all automorphisms.', 'not on the page','The base includes characteristic3; the calculation refines the scope without supplying a deformation theorem or a profinite statement.')
I('root_reconstruction',[('A',13),('A',58)],'unproved claim',[83,94,95],A+':146–154,395–464','la donnée ... équivaut à celle d’un module inv. T ... T⊗2≃T_Σ,t',
 'For fixed cubic étale J/S and t∈Σ_J\D_J, the text asserts an equivalence between elliptic curves with these branch data and square roots of the tangent line T_Σ,t. Once one root T0 exists, roots are equivalent to μ2-torsors by contracted product; after α is fixed the distinguished curve E_α is universal for the pinned problem.',
 'The torsor equivalence is proved independently here. Identifying the root groupoid with the elliptic-curve groupoid is a reconstruction assertion, not proved merely by55. Earlier scans71–74 must be read with this boundary.', 'agrees','Scans94–95 directly state the equivalence and its conditional choice of T0; the earlier-note limitation is now checked against the full available cote64 rather than only this packet.')
I('choose_i',[('A',14)],'unpursued implication',[95,96],A+':466–484','Les deux pts de vue sont équivalents ... une section i',
 'Naive pinning with an orientation ω of J and twisted pinning with α:μ4*≅ω_J become equivalent after choosing i∈μ4*. This is a base change to Z[1/2,i], not an equivalence that forgets the cyclotomic datum over Z[1/2].',
 'We use torsor language to make the required choice explicit.', 'agrees','The qualification is stated at96; choosing i for every t is independent of having CM.')
I('cm_scope',[('A',15),('B',20),('B',22)],'idea of the earlier run',[79,90,95,96,150,151,152,156],A+':50,291,466–484; '+B+':1263–1341,1552–1555','avec un choix fixé de i=√−1; l’invariant modulaire exceptionnel',
 'The notes propose comparing finite pinning characters and square/hexagonal lattice stabilizers with LM6 A.22 and LM7_PUSH E.3. The current pages do not define those profinite CM-image problems; choosing i is not itself a CM restriction.',
 'This is a scope check of earlier-run ideas, not an assertion that the unseen project results are true or false.', 'agrees','The parameter runs through all smooth curves, whereas CM involves extra endomorphisms. The arithmetic appendix neither computes characteristic3 stabilizers nor names a CM coset.')
I('square_normalization',[('A',16),('A',59),('B',47),('B',55)],'self-flagged step',[98,99,100,120,121,126],A+':593–706; '+B+':222–289,470–484','Il reste ensuite à exprimer (73); la condition c) s’écrit Dieu sait comment — il faudra y revenir',
 'For a fixed orientation identification, the coordinate vectors ψ^ω(δ)∈F_t satisfy sign/orientation covariance, weight−1 under δ rescaling, and a prescribed tensor-square identity. Linear conditions Σψ_i=Σc_iψ_i=0 determine only a line; the required scale remains uncomputed at100 and121. The cyclic-difference line at126 does not determine its square normalization.',
 'We identify equations73 and83c as the same missing normalization obligation. The link from loose sheets123–126 to83b is an editorial inference, not his explicit cross-reference.', 'agrees','Both explicit deferrals are present, and the later calculation supplies proportionality only. The packet59 continuation lead is now verified directly against121.')
I('ambient_basis',[('A',17)],'reading question',[96,100],A+':495–509,694–698','(e_i) est la base can. de [V_J?]; base canonique de k^J',
 'V_J=ker(k^J→k) has dimension2; three standard coordinate vectors form a basis of k^J, not V_J. The margin at96 should be checked against the explicit k^J at100.',
 'The alternative follows from dimension and ambient-vector typing; no reading is replaced.', 'agrees','The later explicit ambient basis confirms the mathematical diagnosis but not the earlier ink.')
I('jacobi_name',[('A',18)],'withdrawn in the same text',[85,86],A+':175–193','[deleted Torelli][inserted Jacobi]; Legendre-Torelli',
 'The author renames the combined level2 structure Legendre–Jacobi at85; the older name survives in86. This is terminological revision, distinct from the later integral Torelli framing.',
 'No mathematical hypothesis is changed by the surviving name.', 'agrees','Both the replacement and the retained older wording are visible in the transcription.')
I('twist_glyph',[('A',19)],'reading question',[80,81,82,94,97],A+':65–83,100,126,413–419,544','M^{[sharp?]}',
 'The recurring uncertain glyph denotes the μ4-torsor twist defined by22; its shape remains undecided. Sharp/natural are editorial notation choices, not distinct mathematical operations once22 is fixed.',
 'Definition-based identification of the operation does not decipher the glyph.', 'agrees','The note correctly preserves the uncertainty; Hua’s reported glyph choice is not independent scan evidence.')
I('branch_coordinate',[('A',20)],'reading question',[79,80,106,109],A+':43–58,930–941,1074–1077','t∈U_0,3; t↦∞',
 'In the manuscript coordinate z the three nonzero 2-torsion images are0,1,∞ and O maps to t. Sending O to∞ by x=(1−t)z/(z−t) gives λ=1−t; using x=t(z−1)/(z−t) gives λ=t with the first two labels exchanged.',
 'The Möbius changes are independently computed comparison maps; λ=t is not a literal unlabelled identity of the two conventions.', 'agrees','The branch-labelled quotient and the later Weierstrass infinity convention agree only after an explicit change of coordinates.')
I('derivation_symbol',[('A',21)],'unproved claim',[102,103,104],A+':741–795,831–834','μ_δ est la multiplication par δ; can.',
 'For the invariant derivation Dδ with δ≠0 and canonical principal-part map pp_n:F_n/F_n−1≅t_E⊗n, gr_nDδ=−n·μδ. Multiplicatively rescaled symbols ε_n=c^n pp_n give −nc·μδ. No such convention makes every degree arrow coefficient1 while retaining Leibniz and multiplication.',
 'The precise principal-part convention is reconstructed; the manuscript calls the arrow canonical without an explicit Laurent definition. Its all-degree coefficient1 assertion is mathematically incompatible with a nonzero derivation.', 'agrees','Differentiating t^(−n) gives−n t^(−n−1). This also identifies the uncertainty n/n+1 on the target and flags the unshifted parity targets in104.')
I('charp_kernel',[('A',22),('A',23)],'unproved claim',[102,103],A+':716–724,787–795',r'Ker Θ_δ=F_1=k.1_E',
 'For a smooth elliptic curve over an algebraically closed field of odd characteristic p and δ≠0, ker(Dδ|F_n)={g^p:g∈F_floor(n/p)}. Its dimension is max(1,floor(n/p)); x^p for x of pole order2 first gives a nonconstant kernel element at2p. The manuscript’s unrestricted constant-kernel claim, and the reported modernization’s sufficient condition p∤n, fail.',
 'The exact replacement uses the differential-kernel theorem and pole valuations; it is our modern reconstruction. In characteristic0 the filtered kernel is k.', 'agrees','For n=2p+1, p∤n but x^p∈F_n survives; the note correctly separates graded invertibility from the accumulated filtered kernel.')
I('graded_constants',[('A',24)],'reading question',[102,103],A+':730–761,790–803','F_* ... algèbre graduée; dérivation de degré +1',
 'For the Rees section ring R=⊕F_nT^n, extend D by D(fT^n)=D(f)T^(n+1). In characteristic0 its kernel is k[S] with S=1T. In characteristicp over a perfect field, ker D=R^p[S]. On the filtered union F∞ the kernels are instead k and F∞^p.',
 'This specifies the graded/filtered typing omitted in12. The p-th power statement is proved degree by degree, not inferred from a keyword.', 'agrees','The manuscript moves between F∞ and F_*; distinct constant sections in each degree explain why literal k as the whole graded kernel is insufficient.')
I('monic_convention',[('A',25)],'reading question',[105,106,115],A+':878–900,943–958,1315–1329','wp′=Θ_δ(wp); ε_3(wp′)=δ³',
 'With ordinary principal parts and pp2(x)=δ², y=Dδx has pp3(y)=−2δ³ and y² has leading term4x³. With multiplicative ε_n=(−1/2)^n pp_n and ε2(x)=δ², y=Dδx instead has ε3(y)=δ³ and a monic cubic. The induced symbol is then(n/2)μδ, not1 in every degree.',
 'Both coherent normalizations are ours; no unconditional alteration of the manuscript cubic is licensed because its ε_n normalization is not explicit.', 'agrees','The note correctly isolates the unavoidable all-degree defect from a convention-dependent monic equation.')
I('nonzero_delta',[('A',26)],'unproved claim',[105,115],A+':878–895,1315–1325','δ∈t_E; est une base de t_E',
 'The coordinate-basis construction requires δ≠0. Atδ=0, ε2(x)=0 forces x∈F1 and Dδx=0, so neither displayed basis exists. Scan115 explicitly says δ is a basis.',
 'The inequality is a necessary hypothesis extracted from the construction and the later wording, not an added mark in105.', 'agrees','The note accurately detects the missing local qualification and the later explicit restriction.')
I('double_prime',[('A',27)],'reading question',[108],A+':1015–1030',r'wp^{\unsure{\prime|\prime\prime}}=1/2(3wp²+2a_1wp+a_2)',
 'For y²=f(x), Dx=y and char≠2, differentiating the relation forces Dy=D²x=f′(x)/2. The double-prime alternative is compatible; the single-prime alternative fails at a finite simple branch point.',
 'The branch-point counterexample is mathematical evidence only.', 'agrees','Equation32 already defines D(P′), while33 has the uncertain derivative order.')
I('cubic_exponent',[('A',28)],'reading question',[108],A+':1008–1020',r'a_2P^{\unsure{2}}; a_2\unsure{P²|P}',
 'The relation and derivation are compatible with the term a2P; retaining a2P² while using DP=P′ and DP′=(3P²+2a1P+a2)/2 gives residual a2(1−2P)P′.',
 'We do not decide between the written alternatives; the exact nonzero residual is the alarm.', 'agrees','The derivative in32 and its explicitly written stable ideal in1020 support the linear alternative.')
I('vandermonde',[('A',29)],'unproved claim',[105,106],A+':907–941','sont tous distincts, O.K.',
 'Restriction F3→k^J has kernel F3−=k·y. Odd functions vanish on J because2 is invertible; the even part span{1,x} injects because x takes three distinct values. For the quotient coordinate these values may be normalized to−1/t,1/(1−t),0, and the3×3 Vandermonde determinant is nonzero.',
 'We supply the determinant simplification; the proof is completed on the page.', 'agrees','The temporary words il reste à voir are discharged on106, so this is not an unresolved problem.')
I('cubic_sign',[('A',30)],'reading question',[107,114,115],A+':962–981,1298–1313',r'wp^{\unsure{2|3}}+a_1wp²+a_2wp+a_3; wp³+a_1wp²+a_2wp\unsure{−|+}a_3',
 'With aα=(−1)^α times the elementary symmetric functions of the three roots, f(x)=x³+a1x²+a2x+a3=∏(x−ξ_i). Degree3 and the plus sign before the fixed a3 are required by the proof and the later coefficient formulas.',
 'These compatible alternatives remain scan questions; coefficients are not silently redefined to absorb a sign.', 'agrees','Line971 uses−wp³; scan114 explicitly gives a3=−∏ξ_i, settling the algebraic convention but not the uncertain ink.')
I('translation',[('A',31)],'unpursued implication',[106,107,114],A+':954–958,984–999,1274–1296','pour [wp choisi]; wp↦a wp+b',
 'For fixed δ, translation x↦x+b preserves its principal part and Dx but replaces (a1,a2,a3) by(a1−3b,a2−2a1b+3b²,a3−a2b+a1b²−b³). Hence δ alone does not determine the coefficients; x and the ordinate normalization must be fixed.',
 'The explicit transformation is a checked deduction. The manuscript margin is uncertain between readings, whereas its affine ambiguity is explicit later.', 'agrees','The earlier modernization’s reported for δ chosen would overstate uniqueness; the present note correctly restricts it to a chosen function.')
I('trace_char3',[('A',32)],'unpursued implication',[107,114],A+':984–997,1290–1296','Si car. k≠3',
 'For char k≠3, trace over J gives a canonical complement W_E=ker Tr⊂F2 to constants and permits a1=0. In characteristic3 constants already have trace0, and x-translation cannot change a1.',
 'The structural explanation is our check of an explicit manuscript hypothesis.', 'agrees','The manuscript does exclude characteristic3 precisely at this normalization step; it does not exclude it throughout the folder.')
I('inverse_cubic',[('A',33)],'unproved claim',[102,108,109,114],A+':738–740,1008–1014,1044–1077,1286–1289','on vérifie ... définissent une courbe elliptique; Proj(F_[*|∞])',
 'For a squarefree monic cubic f over an algebraically closed field of char≠2, Y²Z=X³+a1X²Z+a2XZ²+a3Z³ is a smooth genus1 curve with O=[0:1:0]. Its weighted section ring has generators S,X2,Y3 of weights1,2,3 and relation Y3²=X2³+a1X2²S²+a2X2S4+a3S6. Its Proj is E; its affine algebra is E\{O}. The degree2 map is branched at the3 roots and∞.',
 'Homogenization, smoothness, and grading make explicit what109 abbreviates. Proj of an ungraded F∞ is not defined by the text alone.', 'agrees','The note supplies the missing verification and correctly keeps infinity among all four branch values.')
I('determinant',[('A',34),('B',5)],'withdrawn in the same text',[110,111,117,118],A+':1100–1178; '+B+':59–117','tous distincts; Si deux ... sont égaux, (42) est tjrs vérifié',
 'For three distinct finite points P,Q,R on a smooth monic Weierstrass cubic, P+Q+R=O iff det(1,x,y)=0. Repeated rows do not encode tangent multiplicity, so the unrestricted criterion is false. In the later half-division application,2P_i=ε_i with distinct ε_i ensures distinctness.',
 'The explicit repeated-point counterexample and the verification of the later hypotheses are our checks. The author already repairs the original proposition.', 'agrees','Scan110 inserts distinctness and explains why;111 proves the corrected converse;117 explicitly cites Proposition3 and notes the points are distinct.')
I('secant',[('A',35)],'unpursued implication',[112,113],A+':1184–1256','pour z=−(x+y) ... dès que x_0≠y_0',
 'For P=(u,r),Q=(v,s) with u≠v on y²=f(x), m=(r−s)/(u−v),b=(su−rv)/(u−v),w=m²−a1−u−v, the point(w,mw+b) equals−(P+Q). The factorization f(T)−(mT+b)²=(T−u)(T−v)(T−w) verifies extension when the third intersection repeats one of P,Q.',
 'The factorization is our certificate. The domain u≠v is retained even where a temporary pointwise condition omits it.', 'agrees','The final paragraph states exactly this secant domain and the negative-sum convention; the earlier exclusions are withdrawn by prolongation.')
I('tangent',[('A',36)],'idea of the earlier run',[113],A+':1253–1256','Par principe de prolongement',
 'For P=(u,v) with v≠0, m=f′(u)/(2v),b=v−mu,w=m²−a1−2u give(w,mw+b)=−2P; when v=0,2P=O. Only2v is divided by, so characteristic3 is allowed.',
 'The manuscript ends with the secant extension; this tangent continuation is an earlier-run addition rechecked here.', 'not on the page','The addition is mathematically valid but must not be counted as a separate proved manuscript formula.')
I('mobius',[('A',37),('B',7)],'unproved claim',[115,116],A+':1332–1353; '+B+':4–49','Déterminons l’autom involutif; Si ζ_i=0',
 'For distinct roots r,u,v, σ_r(z)=r+(r−u)(r−v)/(z−r) descends translation by(r,0); its matrix squares to(r−u)(r−v)I. Fixed values satisfy(z−r)²=(r−u)(r−v). The polynomial formula covers r=0 and gives σ_0(z)=uv/z; divided forms involving a3/r require r≠0 or this extension.',
 'Matrix and zero-root verification are our checks of the manuscript calculation and explicit domain warning.', 'agrees','The undivided numerator agrees with115 and116(61); the zero-root margin warns against literal division by0.')
I('cusp_scope',[('A',38),('A',39),('B',24)],'reading question',[80,85,86,109,114,145],A+':56–65,183–202,1044–1077,1270–1289; '+B+':991–1010','U_0,3; wp(0_E)=∞; exp(2iπτ)',
 'Scans78–115 keep a smooth elliptic parameter and use∞ only as the image ofO on an individual quotient. Scan145 later supplies C*/q^Z with0<|q|<1, an analytic cusp chart, but no extension overq=0 or arithmetic inertia/decomposition calculation appears through157.',
 'The distinction is based on reading the full two packets. Reports about cote149/LM140 cusp passages remain external project leads.', 'agrees','The later analytic material refines the packet-local negative finding but does not supply a Tate model or a cyclotomic-residue calculation.')
I('level4_program',[('A',40),('B',1),('B',27),('B',54)],'self-flagged step',[93,117,118,120,121],A+':382–391; '+B+':76–125,222–289','montrer comment ... un épinglage de Legendre; associer canoniquement',
 'Given sections P_i of E[4] over the nonzero2-torsion ε_i with2P_i=ε_i andΣP_i=0, construct a canonical Legendre pinning, functorial inE and compatible with base change, without a remaining arbitrary tangent scale or choice ofi. Scan118 resumes the task announced at93; condition83c and choice independence remain unfinished at121.',
 'The strongest text-supported formulation is this symmetric relative-level4 construction, not all modular levels or any profinite kernel theorem.', 'agrees','The same announced map runs across the packet boundary and is explicitly deferred. Coordinates71 alone are not the required canonical construction.')
I('normal_twist_comparison',[('A',42)],'idea of the earlier run',[86,90,91,92],A+':193–202,269–366','courbe elliptique ... universelle; D_3′',
 'The earlier run proposes identifying the symmetric pinned family with a λ(1−λ)-twist attached to a normal complement in Γ(2), by matching branch order, tangent linearization, base point and loops. An abstract order12 group isomorphism does not identify such families or monodromy maps.',
 'The proposed comparison is not a claim of Grothendieck in these pages; the external normal-complement source is absent.', 'not on the page','Retained as a concrete research lead with its own-source status, not as a settled identification.')
I('outer_scope',[('A',43),('B',29)],'idea of the earlier run',[89,90,91,92,146,147,150],A+':248–366; '+B+':1015–1119,1231–1259','χ_4:D_3′→μ4; g∈SL(2,Z)',
 'Finite χ4 and the complex geometric SL2(Z) action have different sources and targets from the arithmetic outer actions reported as LM2 C.d1/C.r1–C.r3. They do not compute all projective congruence kernels, an arithmetic outer image, or a unique cyclotomic multiplier.',
 'The external project statuses are carried as statements of the earlier notes only.', 'agrees','The current pages define finite and discrete geometric actions; the arithmetic extensions and profinite targets named by the earlier runs are not defined here.')
I('gt_torsion_scope',[('A',44)],'idea of the earlier run',[84,85,86,115],A+':162–204,1332–1353','Pour éliminer les autom.; autom involutif',
 'The finite changes-of-pinning group, automorphisms of an object with pinning fixed, and descended2-torsion translations are distinct. Their explicit geometric examples do not classify arbitrary profinite torsion or prove LM4 D.12.',
 'This is a boundary on a prior-run project comparison, not a theorem about an unavailable GT group.', 'agrees','The manuscript objects are explicitly finite geometric ones; the note correctly avoids promoting them to profinite claims.')
I('arithmetic_image_scope',[('A',45)],'idea of the earlier run',[79,80,90,93],A+':50–65,269–291,368–391','donnée arithmétique',
 'The root of−1 and finite pinning characters are arithmetic data of the moduli problem, but the manuscript does not specify the arithmetic-image target, index or inertia tests reported as EXIT_TOWER E.24.',
 'We retain only the scope statement and the external run identifier; no missing target is reconstructed.', 'agrees','The arithmetic adjective at79 is not a complete arithmetic Galois image computation.')
I('higher_kernels_scope',[('A',46)],'idea of the earlier run',[79,85,88,93],A+':50,175–183,237,382–391','échelon2; échelon4',
 'These pages name levels2 and4 only. They do not compute the higher congruence kernels K5,K7,K11 reported in LM4_SUCCESSOR B.38.',
 'A negative textual scope finding, not a mathematical verdict on the external kernels.', 'agrees','Full reading confirms the explicit level-four task and absence of any all-level calculation.')
I('connection_scope',[('A',47),('B',3),('B',31),('B',32),('B',36)],'idea of the earlier run',[82,103,108,120,121,143,144,149,151],A+':122–136,757–761,1015–1030; '+B+':236–249,266–277,934–970,1187–1214,1263–1276','dérivation de degré+1; φ_i^ω(λδ)=λ^(−1)φ_i^ω(δ); une base φ de t_E',
 'The invariant derivation acts on one elliptic fibre; weight−1 covariance makes δ_i=φ_i(δ)δ coordinate-independent; a differential rigidification is a nonzero tangent vector. The later local system and holomorphic period ratio are inputs from which one can form a Gauss–Manin connection, but none of these formulas itself specifies a base connection, Cartier operator or p-curvature.',
 'The separation of objects is our check. S20/P09 are earlier-run comparison programmes, not authorial connection assertions in this fragment.', 'agrees','The earlier notes correctly distinguish fibre derivatives, tensor weights, line frames and rank2 flat bundles; reading shows no explicit identification of these with the missing cotes93/159 objects.')
I('picard_fuchs',[('A',48),('B',33)],'idea of the earlier run',[85,86,109,143,144],A+':183–202,1044–1077; '+B+':934–970','représentable ... U_03; τ=z_2/z_1',
 'For a separate standard Legendre family y²=x(x−1)(x−λ) in characteristic0, L=λ(1−λ)∂λ²+(1−2λ)∂λ−1/4 satisfies L(dx/y)=d_x[x(x−1)/(2(x−λ)y)]. Thus periods satisfyLf=0. Where the period ratio is locally univalent, its Schwarzian equals(λ²−λ+1)/(2λ²(λ−1)²).',
 'Both operators are earlier-run mathematical additions and are rechecked independently; neither is written by Grothendieck here.', 'not on the page','Retained as a conventional bridge calculation, with the branch-coordinate convention and characteristic0 hypothesis stated.')
I('hasse',[('A',49)],'idea of the earlier run',[80,109],A+':65,1044–1077','car. rés.≠2',
 'For oddp andm=(p−1)/2, H_p(λ)=Σ binom(m,k)²λ^k satisfiesLH_p=0 modp and [x^(p−1)](x(x−1)(x−λ))^m=(−1)^mH_p. Over a perfect field the Cartier operator on a smooth specialized fibre sends dx/y to ((−1)^mH_p)^(1/p)dx/y.',
 'An earlier-run computation, not manuscript content; relative Frobenius twisting and nonzero versus zero p-curvature must be distinguished.', 'not on the page','The notes correctly limit the conclusion to the Cartier/Hasse calculation and do not infer zero p-curvature from one polynomial solution.')
I('missing_p09',[('A',50)],'reading question',[81,82,83,94,99],A+':90–154,395–429,644–652','T_E,0⊗2≃T_Σ,t',
 'The earlier note cites only the title of MPL_93_002-046 P09. The present branch, tangent-square and orientation data provide possible comparison inputs, but cannot verify an unseen list of tests.',
 'The absent external text remains absent in this consolidation; available cote64 passages were read directly.', 'agrees','Retained as an evidence-limit record, not counted as a newly formulated mathematical claim by Grothendieck.')
I('coarse_deformation',[('A',51)],'idea of the earlier run',[83,84,85,86],A+':146–204','champ ... n’est pas rigide; catégorie ... rigide',
 'An unrigidified moduli stack retains automorphisms that a coarse parameter loses. The earlier run proposes this as a warning for MPL_93 E14, whose exact deformation statement is not supplied.',
 'The elementary stack/coarse distinction follows from the present stabilizer computation; no external deformation equation is identified.', 'agrees','The note’s limited comparison is supported, while its missing target cannot acquire a verdict from resemblance.')
I('missing_e16',[('A',52)],'reading question',[109],A+':1044–1077','Δ(a_1,a_2,a_3)≠0',
 'MPL_93 E16’s reported smallest orders are not specified in the attached note. No pole order, characteristic3 stabilizer or deformation order in cote64 can be identified with them from this evidence.',
 'This is source criticism of a prior-run lead, not a manuscript problem.', 'agrees','The cubic construction is visible; the other orders and their quantifiers are not.')
I('tangent_bridge',[('A',53)],'idea of the earlier run',[82,94,96],A+':122,402,512','t_E⊗2≃T_Σ,t',
 'The earlier run proposes comparing the branch tangent-square isomorphism with the unspecified first-order map of MPL_93 C29. A valid comparison would need actual deformation tangent spaces and an identified map on the other side.',
 'This remains an explicitly attributed research proposal.', 'not on the page','The tangent-square isomorphism is present; its identification with a missing deformation map is not.')
I('missing_c35',[('A',54)],'reading question',[110,111],A+':1100–1178','Si deux ... sont égaux',
 'The visible determinant correction is unrelated, on current evidence, to the external note MPL_93 C35 whose concern is reportedly withdrawn. The two withdrawals must not be conflated.',
 'No assertion about the correctness of the absent C35 withdrawal is made.', 'agrees','This is a correct boundary on an earlier-context analogy.')
I('early_combinatorics',[('A',55)],'other',[78,80,88],A+':6–31,65–83,225–241','Q_0; carré combinatoire',
 'The square/orientation and rank-two Z/4 constructions earlier in cote64 underlie Q0 and the later relative-level4 pinnings. Unlike the earlier packet, this consolidation has those preceding transcripts, so the relation can be checked at both available endpoints.',
 'The association is a mathematical crosslink, with exact early locators in links.tsv; no unseen proof is borrowed.', 'agrees','The earlier note was appropriately cautious about its packet scope. The topic-wide run supplies the earlier transcript endpoint.')
I('char5_oct',[('A',56),('B',53)],'idea of the earlier run',[80,118],A+':65; '+B+':125','car. rés.≠2; canoniquement',
 'In characteristic5 the bare six-point set{0,∞,±1,±i}=P¹(F5) has120 projective symmetries, whereas those preserving the three opposite pairs have24. This is distinct from the characteristic3 exceptional Legendre parameters and is relevant only if the earlier octahedral statement forgets the pairing.',
 'The finite count was an earlier-run addition; the present consolidation can now compare the earlier c64 statement directly. No supplied Lean certificate is claimed.', 'agrees','The later notes preserve the structure/bare-set distinction; the upstream endpoint is now available and separately checked by the early-c64 analysis.')
I('four_point_link',[('A',57)],'other',[81,82,115],A+':108–124,1332–1353','E/(±id_E)≃Σ_J; x↦x+ε_i',
 'The earlier(0,4) and Klein-quotient construction connects to the branch quotient E/±1 and the descended2-torsion translations. These are related geometric operations but their actual maps must be identified, not inferred solely from the four-point vocabulary.',
 'The link is checked against the earlier available transcript endpoints, with no profinite conclusion.', 'agrees','The local later maps are explicit; earlier constructions are documented separately in links.tsv.')
I('late_analytic_lead',[('A',60)],'other',[101,131,143,145,151],A+':708–712; '+B+':522–544,934–1010,1263–1296','Descriptions explicites; théorie transcendante',
 'The former packet’s out-of-range analytic lead is now directly verified: later sheets describe lattices, Torelli frames, upper-half-plane moduli, q, and tangent rigidification. They do not themselves identify a Cartier or p-curvature construction.',
 'The topic-wide scope changes the evidence boundary, not the content of the earlier note.', 'agrees','The later sections have been read in this run; their relation is documentary and geometric, with S20 kept separate.')
I('arithmetic_lead',[('A',61),('B',52)],'idea of the earlier run',[153,154,155,156],B+':1343–1575','λ=2^α3^β l’invariant modulaire exceptionnel',
 'The later appendix studies quadratic orders over Z[T] and an example T(T−λ). Identifyingλ with1728 andT withj is a plausible earlier-run/Hua interpretation; the page does not specifyα,β or namej.',
 'We verify the appendix directly but preserve the coordinate/value identification as inference, not transcription.', 'agrees','The description fits an exceptional modular value but does not determine a unique coordinate normalization or CM arithmetic image.')
I('weierstrass_title',[('A',62)],'title, date or page count',[78,80,82,84,86,88,90,92,94,101,102,104,106,108,110,112,114,115],A+':2–3,708–717,1258–1259','IV Descriptions explicites par fonctions wp de Weierstrass',
 'Scans78–115 contain38 retained scan markers: a continuation78–100, title101, and algebra102–115; author numbering restarts at1 on102. No total author-written page count or composition date occurs here.',
 'Counts are taken from the supplied transcription markers; without scans, physical nonblank status is a source report, not an independent image audit.', 'agrees','The heading and numbering are direct. The earlier note’s physical and catalogue-dating assertions are retained only at their stated evidence level.')
I('old_records',[('A',63)],'other',[],A+'_notes.md:464–487','',
 'The earlier run describes research scripts, compiled wrappers and source hashes that are not included in this topic archive. Their claimed checks are not inherited as checks in this run; only newly performed events enter CHECK_EVENTS.tsv.',
 'This is metadata about the prior return, not a manuscript passage.', 'not on the page','The note is kept as documentary provenance; it cannot certify unprovided code, scans, hashes or computations.')
# Remaining second-package objects: each decision follows the read entry and its passage.
I('tautological_sequence',[('B',2)],'unproved claim',[119],B+':160–196','la deuxième suite exacte est canoniquement isom.',
 'For the line F_t of sections of O(1) vanishing at t∈P(V), tensoring0→F_t→V→O_t(1)→0 byF_t∨ gives0→k→H⁰(O(t))→T_tP(V)→0. The middle map sendsv⊗f∨ to the meromorphic ratio v/f and is independent of rescalingf.',
 'This explicit ratio map is our proof of the claimed canonical comparison.', 'agrees','The two exact sequences and tensor factor are displayed; the note’s independence claim is correct.')
I('cyclic_differences',[('B',4),('B',8)],'unproved claim',[123,125,126],B+':319–346,419–482','Cela détermine(λ_i) mod mult. par scalaire inv.; t correspond donc à',
 'For distinctζ1,ζ2,ζ3, the kernel of the2×3 matrix with rows(1,1,1),(ζ1,ζ2,ζ3) is spanned by(ζ2−ζ3,ζ3−ζ1,ζ1−ζ2). WithΔ0=(ζ1−ζ2)(ζ2−ζ3)(ζ3−ζ1), the equations on125 implyΔ0f1=Σ(ζj−ζk)e_i and−Δ0f2=Σζ_i(ζj−ζk)e_i.',
 'We compute the identities but preserve the dot/minus alternative beforeΔ0f1. Their attachment to the missing pinning scale remains editorial inference.', 'agrees','Rank2 proves uniqueness; the supplied formulas determine the compatible signs and only the line, not the pinning normalization.')
I('division_signs',[('B',6)],'reading question',[116,118],B+':9–49,101–112','En mettant ensemble les équations pertinentes',
 'Forr=ζ_i,u=ζ_λ,v=ζ_μ, the radical is(r−u)(r−v)=−(a1r+2a2−3uv). Scan118’s bracket with+3uv and its marginal constant a2+2uv have wrong signs relative to116(61). At(r,u,v)=(1,2,3), the correct radical2 becomes−34 in the bracket.',
 'The sign corrections are algebraic alternatives for a later scan audit; no manuscript reading changes.', 'agrees','Both errors follow froma3=−ruv and are isolated by symbolic residuals; the earlier note’s diagnosis is confirmed.')
I('lattice_moduli',[('B',9)],'unproved claim',[131,143,144,145],B+':524–544,934–1010','E≃V/H; pas d’autom.≠id; applications holomorphes',
 'A complex elliptic curve is a complex line modulo a rank2 lattice. For a holomorphic family, H is an integral local system and its lattice sections must be holomorphic in a holomorphic line bundle. A global oriented basis gives a holomorphic mapτ:S→H and pullback of(H×C)/Z²; preserving the basis kills all automorphisms.',
 'The family-level holomorphic condition, explicit in143, is essential; pointwise complex structures alone do not suffice.', 'agrees','The second draft states the missing family hypothesis and represents the framed functor; no new 1980-era general uniformization theorem is implied.')
I('inverse_phi',[('B',10)],'reading question',[131,132],B+':546–573','ux=φ(−iφ^(−1)(x))=−φ(iφ(x))',
 'Forφ:L→V, the second expression is ill-typed forx∈V; it must useφ^(−1)(x) to agree with the first. The convention is conjugate transport,J=−φ i φ^(−1).',
 'The corrected typing is mathematics, not paleography.', 'agrees','The domains in131 make the missing inverse decisive.')
I('orientation_withdrawal',[('B',11),('B',56)],'withdrawn in the same text',[132,134,135,136,137,139],B+':570–573,662,687–692,738–744,754–782,862–866','C’est faux, cf calcul plus bas; base inverse',
 'WithL_z=C(z,1),z=x+iy,y>0, and conjugate transport byRe, J_z=(1/y)[[−x,x²+y²],[−1,x]]. Thusdet(e1,J_ze1)=−1/y<0. The claim that the upper half-plane yields the original positive orientation is withdrawn at135 and corrected in the margin139 by changing the line convention.',
 'The matrix is our independent computation from the written transport; competing bars/inverses remain transcription doubts.', 'agrees','The author’s explicit rejection and later inverse-basis calculation are both present; this is not a live conjecture.')
I('antiholomorphic',[('B',12),('B',49),('B',57)],'self-flagged step',[139,140,143,144,145],B+':855–879,911–918,934–1010','faudrait vérifier ... bien analytiquement naturel; E_z=C/(Z+Z(−bar z))',
 'The literal first-draft family with period−bar z is antiholomorphic in the upper-half-plane parameter and cannot represent a holomorphic framed family there. The author requests analytic naturality after revising conventions; the second draft uses a holomorphicτ and gives a consistent family.',
 'The obstruction is a modern period-map check. The later draft is his revision, while replacing the first formula is an editorial alternative requiring scans.', 'agrees','The note correctly separates mathematical correction, authorial deferral and later consistent construction. Its combined rank-one comparison is separately indexed.')
I('modular_conventions',[('B',13),('B',25),('B',71)],'unproved claim',[146,147,148,150],B+':1033–1049,1095–1119,1121–1167,1220–1228','échange de a et de d; τ_∞=diag(−1,1)',
 'The right framing action givesτ∘g=(dτ+b)/(cτ+a). The anti-automorphismσ(g)=Jg^(−1)J, J=diag(−1,1), converts it to the usual left Möbius action. This J is a determinant−1 convention switch, not an arithmetic cusp inertia group. Physical scan147 precedes the explanation148; no reordering is imposed.',
 'We verifyσ(gh)=σ(h)σ(g) and keep the chronological/logical ordering distinct.', 'agrees','All formulas are explicit and coherent in the second draft; the infinity subscript and scan order do not warrant further identification.')
I('universal_action',[('B',14)],'unproved claim',[147,149],B+':1064–1119,1172–1183',r'T_g(τ,z)=(gτ,z/(cτ+d)); T_{g,m,n}',
 'The automorphy factorj(g,τ)=cτ+d satisfiesj(g,hτ)j(h,τ)=j(gh,τ), soT_g is an action and descends through lattice translations. For the orderT_v∘T_g written at149, the induced action on translation columns isρ(g)=[[a,−b],[−c,d]], and(g,v)(h,w)=(gh,v+ρ(g)w).',
 'The semidirect product law and cocycle check are our explication of the displayed construction.', 'agrees','The note matches the precise order of operations; an unqualified standard semidirect action would hide the sign convention.')
I('stack_universal_cover',[('B',15)],'reading question',[139,140,149,150],B+':870–899,1187–1259','la famille ... est un revêtement universel de M_1,1',
 'The framed baseH→[H/SL2(Z)] is the universal orbifold/stack covering;π1 of the moduli stack isSL2(Z), with central±I ineffective onH but effective on the universal family. The total universal family overH hasπ1=Z² and is not the universal covering space ofM_1,1; the coarse j-line also forgets stabilizers.',
 'The stack interpretation reconstructs the intended target and distinguishes it from the literal predicate on the family.', 'agrees','The theorem’s wording conflates the classifying family with its base. The note’s topological countercheck is valid; no coarse-space substitution is made.')
I('punctured_rank',[('B',16)],'reading question',[140,150],B+':911–916,1252–1259','Π_ab ... libre de rang1',
 'For a once-punctured torusΠ≅F2 andΠ_ab≅Z². The rank1 parenthesis in the first draft is false; the later corollary repeats the isomorphism without that parenthesis.',
 'Rank2 follows from the cellular/retraction calculation, but no ink is changed.', 'agrees','The note correctly marks a local rank slip, not a failure of the mapping-class/outer-automorphism theorem.')
I('outer_action_task',[('B',17),('B',58)],'self-flagged step',[140,150],B+':918,1252–1259','Il faudrait expliciter l’action extérieure ... sur Π',
 'Give the oriented outer actionSL2(Z)→Out(F2) explicitly. In a chosen basisF2=<x,y>, liftsS:x↦y,y↦x^(−1) andT:x↦x,y↦xy induce the standard matrices and preserve the commutator conjugacy class. The modular presentation relations hold modulo inner automorphisms.',
 'The request is his; the displayed generators and word checks are the earlier run’s proposed solution, independently rechecked here. This is a discrete statement.', 'agrees','The margin requests actual formulas, and the second draft restates the theorem without supplying generators; the supplied solution is correctly credited as an addition.')
I('frames',[('B',18)],'unproved claim',[141,151,152],B+':924–929,1263–1324','base φ de t_E; un réseau H⊂C',
 'The doubly framed period spaceP={(z1,z2):Im(z2/z1)>0}≅C*×H has the left actionR(g)=PgP=[[d,c],[b,a]] on period columns. Rescaling the tangent basis byλ divides both periods and the fibre coordinate byλ. The universal family is(P×C)/Z².',
 'We check the representation and interpret differential rigidification as a tangent frame, not a connection.', 'agrees','The coordinate action21–22 and the moduli meaning agree;141 gives the same underlying topological principal bundle.')
I('free_action_withdrawal',[('B',19),('B',59)],'withdrawn in the same text',[152],B+':1326–1341','pts ... d’ordre2!; [deleted] opération libre',
 'Each separate C* andSL2(Z) action onP is free, but(−1,−I) fixesP and sendsz↦−z on each fibre. Its four fixed points areE[2], including three nonzero points, so removingO does not make the product action free.',
 'The fixed-point computation verifies the author’s marginal correction; the cancelled assertion is not retained as an open claim.', 'agrees','The note correctly reads the correction and deletion together.')
I('circle_complex',[('B',21),('B',60)],'unproved claim',[131,132,133,134],B+':546–617,619–682','exactement2 sous-espaces propres; n impair; voir une autre explication',
 'A faithful circle subgroup ofGL_R(V) with exactly two conjugate complex weight spaces has weights±1. Choosing one of its order4 elements givesJ or−J. In real dimension2n their orientations differ by(−1)^n; only oddn permits orientation to select one. In dimension2 invariant positive metrics differ by scale.',
 'We supply the weight/faithfulness and orientation proof. The earlier margin asks for another explanation, which the following circle discussion provides; it does not posit a separate conjecture.', 'agrees','The hypotheses and odd-dimensional qualification are written. The temporary explanatory deferral is not lost, but is not made into an unresolved research problem.')
I('split_scratch',[('B',23)],'other',[154],B+':1349–1391','g=ux=yu; g′g=(u′u)(u^(−1)x′u)x',
 'In any split extension with normal subgroupN, left and right normal forms satisfyy=uxu^(−1) and the displayed multiplication formula. The surrounding diagram suggests an augmentation-kernel F2-module, but its specific group is not defined enough to identify.',
 'The associativity identity is checked; identifying the uncertain diagram with a particular moduli group would be speculation.', 'agrees','The whole scratch calculation is cancelled, but cancellation alone does not make its algebra false.')
I('analytic_monodromy',[('B',26)],'idea of the earlier run',[145,147],B+':991–1010,1104–1119','exp(2iπτ); T_g(τ,z)',
 'For a positive loopq(t)=q0e^(2πit), liftτ(t)=τ0+t. The period basis returns as(1,τ0+1), givingT=[[1,1],[0,1]]; conjugation byS yields[[1,0],[−1,1]].',
 'This is an earlier-run analytic consequence, not an arithmetic inertia comparison or a computation written on the page.', 'not on the page','The stated q-chart and action support the calculation, but the missing arithmetic enhancement is kept separate.')
I('levelN_reduction',[('B',28)],'unpursued implication',[144,145,146],B+':972–1010,1033–1049','t:Z_S²≅H',
 'OverC, an oriented Torelli frame givesEτ[N]=(1/N)(Z+Zτ)/(Z+Zτ)≅(Z/N)². The subgroup fixing the ordered basis isΓ(N), the kernel ofSL2(Z)→SL2(Z/N). This does not identify a projective GT congruence kernel without an additional comparison map.',
 'Finite-level reduction is the earlier run’s consequence; the full integral framing is the manuscript object.', 'agrees','The lattice quotient makes the limited geometric deduction exact; all-level profinite preservation remains outside the page.')
I('congruence_distinction',[('B',30)],'idea of the earlier run',[140,150],B+':911–918,1252–1259','autom. ext. à lacets ... orientation',
 'The discrete identificationOut⁺(F2)≅SL2(Z) does not make the classical homological completion map intoSL2(Zhat) injective. The nonabelian procongruence action retainsF2hat instead; Asada’s theorem distinguishes these completions.',
 'The modern comparison is an earlier-run addition and is checked in the cited primary paper; it is not stated in these scans.', 'not on the page','Retained to prevent a false inference from the discrete corollary, with exact source and target types.')
I('pcurvature_general',[('B',34)],'idea of the earlier run',[143],B+':956','système local H ... rang2',
 'For a smooth proper elliptic family over a smooth characteristicp base, Gauss–Manin p-curvature is nilpotent of exponent≤2 under Katz’s hypotheses. Cartier descent of a connection requires zero p-curvature, a stronger condition; Hasse–Witt, Cartier on forms and p-curvature are different operators.',
 'This is modern background introduced by the earlier run, not an authorial claim in these pages.', 'not on the page','The note states a useful restriction on the proposed S20/P09 comparison without attributing it to Grothendieck’s local-system sentence.')
I('pcurvature_example',[('B',35)],'idea of the earlier run',[143,144],B+':956–970','τ=z_2/z_1',
 'For the Legendre companion solution connection∇=∂−A, A=[[0,1],[1/(4u(1−u)),−(1−2u)/(u(1−u))]], inF3(u) its p-curvature is[[-(u+1),(u+1)²],[-1,u+1]]/[u²(u−1)²], nonzero and square-zero; at supersingularu=−1 it remains nonzero. The dual coefficient connection has−transpose p-curvature.',
 'The example and basis conventions are the earlier run’s additions, checked here by exact rational arithmetic.', 'not on the page','Neither this matrix nor a characteristic3 connection calculation appears in the manuscript; its role is a discriminating comparison test.')
I('dvr_normality',[('B',37),('B',50)],'unproved claim',[155],B+':1428–1447','A [anneau jauge?]; B normal ssi a∉m²',
 'For a DVR A, B=A[S]/(S²−a) witha≠0, residue characteristic≠2 is normal iffv(a)≤1. The same necessity and valuation1 sufficiency hold in residue characteristic2. It is false as a necessity for a regular local ring of arbitrary dimension:Q[[x,y,S]]/(S²−xy) is normal althoughxy∈m².',
 'DVR is a hypothesis required by the valid theorem, not a decipherment of anneau jauge. The original claim’s intended scope therefore remains a reading question.', 'agrees','The note correctly prevents the modernization’s guessed regular-local reading from becoming an established criticism of the manuscript.')
I('dyadic_unit',[('B',38)],'unproved claim',[155],B+':1443–1477','ne dépend que de a, et pas du choix de α',
 'For a DVR of residual characteristic2 and unita, nonsquare residue makesB a DVR with residuek(√abar), usually inseparable. Ifabar=alphabar², setb=α²−a. Its class inm/m² is independent ofα; B is normal iffb∉m². Ifb∈m², (S−α)/π is integral and missing fromB.',
 'No perfectness or completeness is imposed. The statement concerns normality, not necessarily étaleness.', 'agrees','The first-order calculation2αm+m² is explicit in substance and validates the intrinsic obstruction claimed in the margin.')
I('ordinary_double',[('B',39)],'unproved claim',[155,157],B+':1476–1478,1594–1615','Ce dernier cas correspond à une ... singularité quadratique ordinaire',
 'For a dyadic DVR with uniformizerπ, unita=α²−b andb∈π²A, the tangent quadratic isX²+overline(2α/π)XY+overline(b/π²)Y². It is geometrically an ordinary node exactly whenv(2)=1. The unrestricted assertion fails forF2[[π]],a=1+π³ and forZ2[√2],a=5, whose tangent cones have a doubled line.',
 'The v(2)=1 refinement and counterexamples are ours; scan157’s cross-term calculation is consistent with the restricted applicationA=Z[T]_(2).', 'agrees','The note identifies a true missing hypothesis on the literal broad assertion, while preserving uncertain local-ring terminology.')
I('global_normality',[('B',40)],'unpursued implication',[154,155],B+':1417–1424,1499–1518','B est normal en codim1 ... nb fini ... pts non normaux',
 'For primitive squarefreeP=±qQ defining a genuine quadratic extension, B=Z[T,S]/(S²−P) is a hypersurface, henceS2. If its height1 local rings are normal, Serre’s criterion makesB normal everywhere; the possible finite exceptional nonnormal set in the manuscript is empty under these hypotheses.',
 'This is the earlier run’s sharpening of a weaker correct assertion, rechecked here; it does not apply to arbitrary finite orders.', 'agrees','The note uses the actual hypersurface model and its squarefree height1 hypotheses; no contradiction with the weaker page statement is claimed.')
I('signed_radicand',[('B',41)],'reading question',[154,155,156],B+':1394–1414,1499–1518,1538–1550','Q(t) est un carré mod4; P=εQ',
 'ForP=εqQ the dyadic normality test must apply toP, not to the unsigned primitive factorQ. For exampleQ=1 is square mod4 whereasP=3 or−1 is not, and the corresponding dyadic quadratic order is normal. Later156 correctly writesεQ whenq=1.',
 'The diagnosis is conditional on howQ is being reused at154; the notation may abbreviate the full radicand. It is reserved for ink/context review.', 'agrees','The note properly qualifies its counterexamples and uses the later signed expression to constrain the interpretation.')
I('normalization_sufficiency',[('B',42)],'unproved claim',[156],B+':1523–1550','Cette condition est aussi suffisante',
 'For primitive squarefreeP defining a genuine quadratic extension ofQ(T), its normalization is generically étale above every rational prime iffq=1 andP≡r² mod4 for somer∈Z[T]. IfP=r²+4h, the normalized order isZ[T,u]/(u²−ru−h), u=(S+r)/2; its discriminantP is invertible onD(P), so it is finite étale there.',
 'The explicit integral generator and normality proof are our reconstruction of the asserted sufficiency; the manuscript does not supply them.', 'agrees','The note correctly fills a stated-without-proof step, retaining squarefree and primitive hypotheses and all-characteristic quantifiers.')
I('mod4_example',[('B',43)],'reading question',[156],B+':1552–1559','Q(T)≡T² [≡?](2) ⇔ λ≡0(4)',
 'For nonzero integerλ, T(T−λ) is a square modulo4 iff4|λ, and only the positive signed radicand works. Congruence toT² modulo2 requires only2|λ, soλ=2 refutes the literal written equivalence.',
 'Replacing(2) by(4) is the mathematical alternative for scan review, not an adopted correction.', 'agrees','The note correctly distinguishes a useful modulo4 criterion from the weaker literal modulo2 statement.')
I('infinity_sign',[('B',44),('B',46)],'reading question',[156],B+':1560–1575','δ²−(λT′−1); T′=1/T',
 'Forλ=4m, x=1/T sendsS²=T(T−λ) to(S/T)²=1−λx. The finite étale normalization onSpec Z[x,(λx−1)^−1] is u²−u+mx=0. The written opposite radicandλx−1 remains dyadically ramified: atλ=4,x=0 it givesZ[i]. The corrected fibre at∞ is splitu(u−1)=0.',
 'The compatible sign, integral chart and split boundary are mathematical reconstructions. The mod2 equationu²+u+mbar x is an earlier-run consequence, not a Tate degeneration.', 'agrees','The exact coordinate substitution reverses the written sign; the note’s counterexample checks the claimed étaleness at a permitted point.')
I('completion',[('B',45)],'unproved claim',[155],B+':1449–1466','Bhat≃A[[T]]/(T²+2αT+b)',
 'A[[T]]/(T²+2αT+b) is theT-adic completion ofB. Ifb≠0 for a DVR and the dyadic square-residue case, (T) is maximal-ideal-primary, so this is also the local completion even ifA was not complete. Ifb=0, the topologies need not agree;A=Z_(2),a=α=1 is a split counterexample to an unrestricted maximal-ideal interpretation.',
 'The topology qualification is ours. The intended genuine quadratic-field case forcesb≠0.', 'agrees','The note correctly avoids an automatic demand thatA be complete and identifies the exact exceptional boundary.')
I('braid_frame',[('B',48)],'idea of the earlier run',[141,151],B+':924–929,1263–1296','fibré principal associé; un réseau H⊂C',
 'The tangent/differential-frame moduli space overC is isomorphic to the discriminant complement{(g2,g3):g2³−27g3²≠0}; its fundamental group isB3. UnderB3→SL2(Z), the central full twist maps to−I and the kernel is generated by its square.',
 'The identification is an explicitly credited Hua/earlier-run extension, absent from the manuscript; we verify the cited literature and central matrix calculation.', 'not on the page','The frame construction supports the implication, but no braid-group conclusion is stated on141 or151.')
I('cover_discrepancy',[('B',51)],'reading question',[152,153],B+':1336–1345','[deleted] M_1,2^!; normalité des ext. quadratiques',
 'The retained transcription ends152 with a deletedM_1,2^! and records a nonblank title at153. The earlier modernization reportedly gaveM_1,1^! and called its page152 blank; those reports cannot override the supplied transcript.',
 'This is documentary comparison; no claim is made to have inspected the absent modernization or scans.', 'agrees','Both current endpoint readings are explicit; the deleted moduli identification is not used as an active theorem.')
I('uncertainty_markers',[('B',61)],'reading question',[138,154,156],B+':827–849,1417–1424,1547–1559','[?]; sauf ... au dessus; Cette condition est aussi suffisante',
 'The doubtful question mark in138 belongs to competing action formulas, while sauf at154 describes an exceptional locus. The sufficiency sentence156 is an unproved assertion rather than an explicit authorial doubt. The visible range contains no distinct conjecture that can be formulated solely from these markers.',
 'This is a bounded inventory of the supplied selection, not of the whole archive.', 'agrees','Read context prevents turning editorial doubts and ordinary exception clauses into artificial open problems.')
I('title_relations',[('B',62)],'title, date or page count',[128],B+':509–512','Relations entre M_11 et M_04',
 'Scan128 is a separate title sheet relating the elliptic and four-pointed rational moduli problems; no written count occurs there.', 'The scan-marker count is documentary, not a theorem.', 'agrees','The heading is preserved separately from the following analytic draft.')
I('title_analytic',[('B',63),('B',64)],'title, date or page count',[129,131,143,152],B+':514–522,932–947','Approche transcendante; (22|21 p); Modules ... théorie transcendante',
 'The doubtful pencilled count at129 is21 or22, with uncertain hand. Scans131–152 span22 scan positions and retain21 transcript pages because142 is omitted as blank. First and second analytic attempts begin131 and143; those draft labels are editorial.',
 'Arithmetic counts do not decide the handwritten count or authorship. No composition date is supplied by these titles.', 'agrees','The note accurately separates physical positions, retained pages, titles and inferred editorial organization.')
I('title_normality',[('B',65)],'title, date or page count',[153,155],B+':1343–1345,1426–1432','normalité des ext. quadratiques; Normalité des extensions quadratiques',
 'Scan153 is an arithmetic-section title cover and155 repeats the heading; neither gives a page count.', 'No scan evidence beyond the transcription is claimed.', 'agrees','Both headings are directly recorded; the earlier report that153 was blank is contradicted by the supplied transcript.')
I('notice_thesis',[('B',66)],'title, date or page count',[124],B+':356–413','Montpellier, le4 novembre1980; PAPPALARDO Alain',
 'The printed thesis notice is dated4 November1980 and announces Alain Pappalardo’s defense on12 November1980. These date the reused printed sheet, not adjacent mathematics.', 'At most a physical terminus post quem for writing on that particular sheet; no date is assigned to neighboring leaves.', 'agrees','The actual printed dates and subject are present, and the note correctly limits their chronological force.')
I('notice_jambon',[('B',67)],'title, date or page count',[127],B+':486–507','LES NOMBRES ENTIERS ... LANGAGE ALGORITHMIQUE',
 'The printed seminar announcement schedules Jambon’s lecture for12 December1980. It does not independently date the analytic drafts that follow.', 'No inference about the mathematical composition date beyond availability of this sheet.', 'agrees','The printed event date and title agree with the note.')
I('notice_exams',[('B',68)],'title, date or page count',[157],B+':1577–1615,1622–1634','[1?]9 JUIN1981;16 JUIN1981; Surveillance des examens',
 'The reused examination notice bears9 June1981 preceded by an uncertain1 and assigns exams16 June1981; quadratic scratch calculations are written across it.', 'The uncertain digit and neighboring chronology remain unresolved; no continuous composition date is inferred.', 'agrees','The note preserves the diplomatic uncertainty and separates printed chronology from the mathematical scratchwork.')
I('marteaux',[('B',69)],'reading question',[140,150],B+':901,1238','grands théorèmes [marteaux-pilons?]',
 'The first occurrence is lexically doubtful and a reported modernization gives orthodoxes; the later page150 explicitly reads marteaux-pilons. The mathematical reference is to general mapping-class/Teichmüller results.', 'A later similar phrase improves plausibility but does not decide the earlier ink.', 'agrees','The note is a lexical reading question, with no mathematical conclusion changed by the alternative.')
I('multiplier_label',[('B',70)],'reading question',[147],B+':1064–1088','[ζ|ξ]=z_1/z_1′=1/(a+cτ)',
 'The diagram’s uncertain Greek label denotes the scalar1/(a+cτ). A reported label2 cannot represent the general multiplier unless it is merely a mark; the symbolic letter remains a scan question.', 'We identify the scalar’s role from the adjacent equation, without choosing its ink glyph.', 'agrees','The note’s functional identification is direct and does not normalize the transcription.')
# Generate source verdict rows only from the explicit manually chosen source lists above.
(BASE/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
(BASE/'item_keys.json').write_text(json.dumps(keys,indent=2)+'\n')
with (BASE/'entries.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
expected={A+'#'+str(i) for i in range(1,64)}|{B+'#'+str(i) for i in range(1,72)}
ids=[r['entry_id'] for r in entries]
assert len(ids)==len(set(ids)), 'duplicate entries'
assert set(ids)==expected,(expected-set(ids),set(ids)-expected)
msg=f'{len(items)} manually authored items; {len(entries)} unique entry verdicts; all134 covered.'
(BASE/'outputs/items_validation.txt').write_text(msg+'\n')
with (BASE/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\tSTAGE1\t'+msg+'\n')
print(msg)
