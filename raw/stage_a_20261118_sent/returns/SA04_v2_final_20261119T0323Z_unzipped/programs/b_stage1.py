"""Serialize manually authored judgments after reading every assigned note and passage.
No verdict is inferred from headings, keywords, or mathematical output.
Source extraction below only supplies the diplomatic quotation at a chosen locator.
"""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'SA04_work/parts/b';OUT.mkdir(parents=True,exist_ok=True)
P='MPL_93_047-091'; TEX='pro/'+P+'_transcription.tex'
text=(ROOT/'source/SA04_texts'/TEX).read_text().splitlines()
items=[];entries=[]
def add(n,src,kind,scans,lines,q,statement,reason,reconstruction='',check='agrees',verdict='kept',overrides=None):
    iid=f'SA04-{n}'
    words=' '.join(text[q[0]-1:q[1]]) if isinstance(q,tuple) else q
    items.append(dict(id=iid,sources=[f'{P}#{j}' for j in src],kind=kind,cote='93',scans=scans,lines=[f'{TEX}:{lines}'],his_words=words,statement=statement,reconstruction=reconstruction or 'The modern statement makes locality and category explicit; no missing manuscript assertion is supplied.',check=check,check_reason=reason))
    for k,j in enumerate(src):
        v,r=(overrides or {}).get(j,(verdict if k==0 else 'merged into '+iid,reason if k==0 else 'Same object or exact identity as the other cited entries. '+reason))
        entries.append(dict(entry_id=f'{P}#{j}',item_id=iid,verdict=v,reason=r))

add(201,[161],'idea of the earlier run',[73,74],'891–982','G_0',
    'In characteristic 2 the integral invariant and its negative coincide. This removes a sign ambiguity but proves no uniqueness among natural differential operators.',
    'The note correctly confines this observation to its own elementary reduction of the integral formula. The manuscript universal claim remains separate.',
    'This is the earlier run’s consequence of the displayed formula, not a separate assertion by Grothendieck.')
add(202,[162,163,164],'unproved claim',[73,74],'921–947',(945,947),
    'The proposed universal coherent recipient would identify a natural target F_X with omega_X squared. The stated conditions cannot force this if one may replace a valid pair (omega squared,G) by (omega squared direct-sum O,(G,0)) without requiring local surjectivity or minimality.',
    'The isomorphism claim is present. The direct-sum objection belongs to the earlier run and correctly identifies a missing hypothesis; merely requiring coherent functorial targets does not remove the objection.',
    'The direct-sum counterexample is a reconstruction. A repaired classification must specify naturality, finite order, target generation, and base change.',check='overstates',verdict='corrected',overrides={163:('merged into SA04-202','The earlier-run direct-sum counterexample addresses precisely the target-isomorphism assertion; retained as reconstruction, not manuscript claim.'),164:('merged into SA04-202','The functorial/coherent extension on scan 74 has the same missing minimality or epimorphism hypothesis as entry #162.')} )
add(203,[165,166,169,170],'unproved claim',[74],'949–964;972–979',(949,953),
    'Multiplying a cocycle by a unit phi identifies its torsor with the pushout by multiplication by phi. Multiplication by 12 gives a pushout even when 12 is not invertible, but does not then give an isomorphism. A scalar nonzero in every residue field is a unit; this does not exclude additional nilpotent-valued natural operators.',
    'The semilinear isomorphism and factor 12 are explicit. The adjective “most refined” and uniqueness over nonreduced bases are stronger than the elementary pushout construction.',
    'Torsor pushout and the fibrewise-unit argument are re-proved here; a universal optimality claim is not.',check='agrees',overrides={166:('corrected','Factor 12 is a valid pushout; it is not an isomorphism in characteristics 2 or 3 and does not prove that G_0 is universally finest.'),169:('merged into SA04-203','The base-dependent ambiguity is a global unit, with the displayed S versus S_0 indexing still a reading question.'),170:('corrected','Fibrewise nonvanishing makes a scalar multiplier a unit, but does not by itself classify operators over a nonreduced base.')} )
add(204,[167,168],'self-flagged step',[74],'966–982',(966,971),
    'The author proposes uniqueness, up to F_p multiplicative scalar, of the nonzero invariant satisfying the preceding cocycle, naturality, and projective-invariance conditions in a fixed positive characteristic. A margin questions the assertion and may limit it to differential order at most three.',
    'The claim and “faux?” are both present. No theorem is established by this paragraph; neither the order bound nor the scope of the objection can be fixed without the scans.',
    'Any precise classification by differential order, polynomial law, and base category is a later formulation.',check='agrees',overrides={168:('merged into SA04-204','The margin qualifies this exact uniqueness proposal; its uncertain attachment and reading are retained in Stage 4.')} )
add(205,[171],'unproved claim',[75],'992–998',(996,998),
    'For real local C^3 diffeomorphisms the displayed third-order Schwarzian expression is continuous and obeys the algebraic identities. Holomorphic local-root and exponential arguments need separate real sign and regularity hypotheses.',
    'The broad extension to real analytic, smooth, and C^3 categories is asserted. It does not automatically transport every subsequent complex torsor-surjectivity argument.',check='agrees')
add(206,[172,173,174,177],'unproved claim',[75],'1002–1041',(1007,1012),
    'On a smooth complex analytic curve, d:O to omega is a sheaf epimorphism with locally constant kernel. A(f,g)=dg-df is a translation-invariant additive cocycle; equality A(f,g)=A(f,h) together with g(x)=h(x) implies equality near x. Its quotient torsor is canonically the additive sheaf omega.',
    'These assertions are explicit and are verified by local integration. Epimorphism is sheaf-local, not surjectivity of global sections; the later restriction to etale functions changes the range.')
add(207,[175,176,178,179],'withdrawn in the same text',[75,76],'1018–1036;1045–1053',(1045,1052),
    'For local coordinates E_X the derivative has values in the frame torsor omega-star, and A-prime(f,g)=dg/df takes values in O-star and is locally onto. With fixed f, g maps to dg-df cannot be onto all omega on E_X, since the target -df would force dg=0.',
    'Scan 76 explicitly changes both target and invariant. Pro scan 75 reads E_X to omega epimorphic, while Codex K93-08:503–504 reads O_X to omega; only the former is false. The note must preserve this witness conflict.',check='agrees',overrides={175:('merged into SA04-207','The margin proposes E_X and scan 76 supplies the accompanying target change.'),176:('corrected','The counterexample refutes the Pro E_X reading. Codex reads O_X, for which local surjectivity holds; therefore no unconditional manuscript error is established.'),178:('merged into SA04-207','The ratio dg/df and its multiplicative cocycle are the corrected construction on scan 76.'),179:('merged into SA04-207','The range is the O-star torsor of frames of omega, not the additive sheaf omega.')} )
add(208,[180,182,183],'unproved claim',[76,77],'1055–1090;1099',(1067,1072),
    'For a holomorphic line bundle L on a smooth complex curve, a nonvanishing frame defines the connection for which it is horizontal; frames modulo locally constant C-star correspond locally to connections. For L=O, dlog:O-star/C-star to omega is an isomorphism of sheaves, and dlog g-dlog f is an additive cocycle.',
    'The local quotient and the displayed logarithmic cocycle occur. Their proof uses a local primitive and exponential; no assertion about global horizontal frames is justified.')
add(209,[181,190,191,192,226],'reading question',[76,78,82],'1074–1078;1149–1177;1449–1454',(1074,1078),
    'The affine quotient of local coordinates is the sheaf of connections on omega: f maps to the connection making df horizontal. Under this convention D_g-D_f=-dlog(g/f) for line-bundle frames, and D_dg-D_df=-dlog(dg/df). The positive expressions printed in the transcription have the opposite sign.',
    'The quotient construction is correct; the sign depends on what “associated connection” means. The later beta_n formula and gamma computation support the horizontal convention, but no ink correction is made.',
    'The sign is fixed here only for the explicitly stated horizontal-frame convention.',check='agrees',overrides={181:('corrected','The displayed positive dlog is not D_g-D_f if both named frames are horizontal. Retain the convention ambiguity for the scan check.'),190:('merged into SA04-209','The affine-invariant connection D_df is the same construction after translations and scalings.'),191:('merged into SA04-209','Aff(1) quotient is established locally by the two successive translation and scaling quotients.'),192:('corrected','The logarithmic derivative is a cocycle; its identification with the difference of horizontal-frame connections requires a minus sign.'),226:('merged into SA04-209','Scan 82 repeats the same connection difference with the same sign issue.')} )
add(210,[184,185,186,187,223],'withdrawn in the same text',[77,81],'1101–1127;1418–1427',(1115,1127),
    'The scale-invariant vector g/dg for a local coordinate g is not onto all vector fields. Equality g/dg=h/dh plus equal nonzero initial values forces g=h; at a common zero, g=t and h=2t give a counterexample. Restricting to nonvanishing local coordinates makes dlog g a nonzero one-form; g-prime/g=1/phi has local solutions c exp integral(1/phi), c nonzero, when phi is a frame.',
    'The nonzero initial-value condition and the failure of the old epimorphism are explicit, followed immediately by the domain restriction. The later ODE is a local formula, not a global integration theorem.')
add(211,[188,232,242],'reading question',[77,82,84],'1131–1132;1501–1505;1633–1640',(1131,1132),
    'The ratio (dg/g)/(df/f) equals (dg/df)(f/g), and its square is the later invariant for the inversion quotient. The Pro and Codex scan 77 product with g/f is algebraically incorrect; the unsimplified ratio on scan 82 and the square on scan 84 support the corrected algebra.',
    'The exact test f=t, g=t squared gives 2 for the ratio and 2t squared for the printed product. This is a mathematical alarm, not a decision whether ink, author, or transcription is at fault.',check='agrees',overrides={188:('corrected','Replace the mathematical expansion by (dg/df)(f/g), while leaving the diplomatic reading unchanged and listing it in Stage 4.'),232:('merged into SA04-211','The later unsimplified formula is correct and controls the earlier expansion.'),242:('merged into SA04-211','The scan 84 squared ratio is the same invariant after quotienting by inversion.')} )
add(212,[189],'self-flagged step',[77],'1135–1139',(1135,1139),
    'The successful examples have homogeneous target spaces under their transformation groups. The author suggests this as a condition for success, but does not state a quantified necessity or sufficiency theorem.',
    '“ce qui semble condition de succès” is heuristic, not a general classification of invariant differential operators.',check='agrees')
add(213,[193,194,207,243],'unproved claim',[78,80,84],'1179–1204;1288–1309;1633–1643',(1180,1185),
    'On nonvanishing local coordinates, scalings and inversion form G_m semidirect Z/2. The invariant (dlog f) squared identifies its local quotient with frames of omega squared over C. Equality of the squared forms gives dlog f=plus-or-minus dlog g locally, hence f=cg or c/g. Appropriate initial data distinguish the two branches.',
    'The group action and quotient are present; local square roots and integration prove the analytic version. These statements do not imply a positive-characteristic p-curvature theorem.')
add(214,[195,196,197,199,200,201,202,236,238],'unproved claim',[80,82],'1208–1258;1545–1575',(1210,1215),
    'For a nonzero integer n and a frame f(dt)^n on a complex curve, choose a local n-th root and its primitive. The induced projective coefficient is c_n(f)=[-2 f-double-prime/(n f)+(2n+1)(f-prime/f)^2/n^2](dt)^2. Root-of-unity and translation ambiguity leaves it unchanged. Mixed differences c_n(g)-c_m(f) form a cocycle, and c_nr(f^r)=c_n(f) for nonzero r. The connection map beta_n has coefficient -f-prime/(n f).',
    'The root construction and formula are on the page. The mixed cocycle and tensor-power identities are exact symbolic consequences, independently recomputed. The final scan 82 line omitting n is valid only for n=1 as its margin indicates.',
    'All roots, primitives, and maps are sheaf-local over C; n and r must be nonzero and invertible in any algebraic variant.',overrides={201:('corrected','The typed ds in the n-differential slot must be (ds)^n to match the displayed tensor weight; this is recorded as a scan question.'),202:('corrected','The subscript 0 denotes the coordinate-input map, not a meaningful substitution n=0 into denominators.'),236:('corrected','For the stated horizontal-frame convention beta_n=-dlog(f)/n. Pro preserves both signs; Codex’s positive differential formula conflicts with the group-arrow sign.'),238:('corrected','The coefficient (2n+1)/n squared is correct. The simplified 3 and -2 formula is its n=1 specialization, not a general formula.')} )
add(215,[198],'reading question',[80],'1232–1244',(1238,1244),
    'In the mixed expression c_n(g)-c_m(f), the term belonging to the second input must use f-prime/f throughout. The transcribed occurrence of g-prime/g in that second term makes the formula false.',
    'With m=1,n=2,f=t,g=t squared the correct difference is zero and the suspect formula is -9/t squared. The original ink is not available.',check='agrees',verdict='corrected')
add(216,[203,204],'self-flagged step',[80],'1261–1284',(1261,1267),
    'The passage first cancels a factor 12 and then displays another rescaling by 1/12; the precise relation of its renamed torsor to the old one is not settled by the typography. Reversing the mixed invariant’s arguments changes its sign, and a difference lies in the acting sheaf omega squared, not literally in an unpointed torsor.',
    'Both ambiguities are visible. Algebra can check signs and scalar pushouts but cannot supply a missing canonical base point or decide the cancelled normalization.',check='agrees')
add(217,[205,206],'unproved claim',[80],'1286–1296',(1286,1293),
    'The invariant is unchanged under fractional linear substitutions with coefficients pulled back from the base. In characteristic zero, df=dg locally implies f-g constant and therefore vanishing Schwarzian difference. For the integral Hasse invariant in characteristics 2 and 3, df=dg alone is too weak: t and t+t^p have the same ordinary differential but nonzero invariant.',
    'The note correctly separates the characteristic-zero deduction from the universal relative-invariance statement. The small-characteristic counterexamples use unit first derivative and are redone here.',overrides={206:('corrected','The conclusion from equality of ordinary differentials is characteristic-zero only; it fails for the integral invariant in characteristics 2 and 3.')} )
add(218,[208],'self-flagged step',[80],'1296–1309',(1296,1303),
    'If dlog f=c dlog g with constant c over C, then locally f=C g^c after a branch choice. This does not imply that f and g are projectively related: g=t, f=t squared on a punctured disc gives nonzero Schwarzian difference 3(dt/t)^2 in the manuscript normalization.',
    'The questioned proportionality is not a valid vanishing criterion. Equality of the squared logarithmic forms is the valid special case c=plus-or-minus 1.',check='agrees')
add(219,[209],'self-flagged step',[80],'1304–1311',(1304,1311),
    'The terminal product combining differences of differentials and logarithmic squares is an unfinished expression. It does not define a complete invariant or state a theorem.',
    'The note properly resists supplying a missing formula; no fate of an identifiable mathematical assertion can be assigned.',check='agrees')
add(220,[210,211,212,213,214,215,216,224],'self-flagged step',[81],'1315–1380;1427',(1320,1325),
    'A draft diagram uses a cover, path classes, an associated object, and several questioned arrows, but does not identify all objects D,U,B,V,Sigma and T-hat. The relation (c lambda,xi) equivalent to (c,lambda xi) has the usual associated-bundle meaning only once the indicated action and handedness are specified.',
    'Neither witness supplies the missing definitions. Codex marks substantial material deleted, while Pro records cancellation strokes without a determinate scope; the construction cannot be upgraded to a completed descent theorem.',
    'The associated-bundle interpretation is conditional reconstruction. All arrow identities remain unidentified where the data are absent.',overrides={216:('corrected','The quotient relation has a familiar conditional meaning; this alone does not prove that the unspecified objects and maps in the diagram exist.'),224:('corrected','Cancellation is recorded, but its exact scope differs between witnesses and must be checked on the scans.')} )
add(221,[217,218,219,220,221],'idea of the earlier run',[81],'1381–1411',(1381,1385),
    'Conditionally on E=Omega inverse direct-sum O, its endomorphism matrix is [[O,Omega inverse],[Omega,O]], and after tensoring by Omega its trace-zero part is Omega direct-sum O direct-sum Omega squared. On a compact connected smooth complex curve of genus g at least 2, the corresponding h^0 is g+1+(3g-3)=4g-2.',
    'The matrix entries support this reconstruction, but the manuscript identification of E and the isolated weight notation are uncertain. The numerical formula requires genus and compactness hypotheses absent from the sketch.',
    'The direct-sum identification and Riemann–Roch count are explicitly the earlier run’s conditional reconstruction, not a manuscript theorem.',overrides={220:('corrected','Retain the arithmetic only under compactness, connectedness and g at least 2; for g=1 the displayed 4g-2 count is not the same calculation.'),221:('corrected','The isolated Omega superscript 1 equals omega squared is a reading question, not an independently established weight convention.')} )
add(222,[222],'self-flagged step',[81],'1412–1416',(1412,1416),
    'To solve f+f inverse=h one needs a root of f squared-hf+1=0. Nonvanishing h does not ensure an etale solution f: the constant h=2 gives f=1 and the map f maps to f+f inverse is critical at f=plus-or-minus 1.',
    'The manuscript itself writes the quadratic with a question. The counterexample checks f nonzero but shows that an etale-source condition needs a discriminant/derivative restriction.',check='agrees')
add(223,[225,235],'unproved claim',[82],'1434–1450;1530–1544',(1434,1443),
    'For nonzero n, the ratio (dg/df)^n is a multiplicative cocycle and the n-th-power map of frames omega-star to (omega^n)-star is equivariant for u maps to u^n and a local epimorphism over C.',
    'The heading “additif” does not alter the multiplicative identity actually displayed. A claim of global surjectivity or characteristic-dividing-n etale surjectivity would need different hypotheses.',overrides={225:('corrected','The formula is multiplicative despite its additive label; retain the algebraic identity and flag the heading.'),235:('merged into SA04-223','The tensor-power arrow is locally surjective over C and equivariant for the power homomorphism.')} )
add(224,[227],'reading question',[82],'1449–1461;1522–1529',(1449,1454),
    'The target of the n-differential quotient map consists of nonzero frames of omega^n. Omitting its star would incorrectly add the zero section to a quotient of local coordinates.',
    'The later repeated diagram carries the star and supplies internal mathematical evidence for the missing frame restriction.',check='agrees',verdict='corrected')
add(225,[228],'idea of the earlier run',[82],'1451–1460;1522–1529',(1451,1456),
    'The exceptional arrow is transcribed (n=0) by Pro and (n not equal 0) by Codex. The nearby -1/n dlog requires n nonzero. The earlier note’s proposed interpretation through a special mu_0 kernel is unsupported by the second witness.',
    'The note explicitly labels its group-level mu_0 interpretation as possible, and its kernel identity is correct. The Codex witness lowers confidence in identifying the intended arrow; neither the identity nor the denominator decides its attachment on the scan.',check='agrees',verdict='corrected')
add(226,[229,230,237,239,241],'unproved claim',[82],'1462–1485;1563–1597',(1468,1485),
    'The inclusion Aff(1) in PGL2 induces gamma from line connections to projective connections. In coordinate t, gamma(D_dt+lambda dt)=c_t+(2lambda-prime+lambda squared)(dt)^2; variation by eta is 2D eta+eta squared. Substituting beta_1(df) recovers the manuscript Schwarzian. Also delta(alpha squared)=gamma(beta_1(alpha))+alpha squared.',
    'The quadratic variation and coordinate formulas are displayed and rechecked symbolically with the horizontal-frame convention. Their analytic quotients are local; this is not a Gauss–Manin construction.')
add(227,[231,234],'unproved claim',[82],'1487–1521',(1487,1495),
    'Exponentiation intertwines f maps to plus-or-minus f+a with g maps to e^a g to the plus-or-minus 1; dlog(exp f)=df explains the identity arrow between the resulting differential frame torsors.',
    'The group action and identity arrow match direct differentiation. The exponential has local inverse branches, with the usual locally constant periods.')
add(228,[240],'reading question',[82],'1586–1597',(1586,1597),
    'For a nonzero quadratic differential f(dt)^2, delta has coefficient f-f-double-prime/f+(5/4)(f-prime/f)^2 relative to c_t. It equals gamma(beta_2(f(dt)^2))+f(dt)^2.',
    'Pro and Codex differ in the linear f term and in derivative/coefficient alternatives. Independent substitution forces this formula under the preceding definitions; the source reading remains undecided.',check='agrees',verdict='corrected')
add(229,[244],'withdrawn in the same text',[84],'1641–1644',(1641,1644),
    'The short translation-related fragment at the end of scan 84 is cancelled and incomplete. It cannot be used as an additional quotient theorem.',
    'The note correctly treats the deleted fragment as documentary evidence, not a completed mathematical assertion.')
add(230,[233],'reading question',[82],'1507–1520',(1507,1515),
    'A projective connection coefficient transforms with tensor weight two. The displayed coefficient expression must be paired with (df)^2; the ambiguous omega power cannot be used to define a different weight.',
    'The surrounding Schwarzian formulas and subsequent diagram force quadratic tensor weight, but do not decide the exact written exponent.',check='agrees',verdict='corrected')
add(231,[246],'idea of the earlier run',[73,74],'891–982','G_0',
    'For an F_p-algebra A, the common kernel of the first three Hasse derivatives on A[t] is A[t^p] for p greater than 3, A[t^4] for p=2, and A[t^9] for p=3. Coefficients are arbitrary in A; these subrings need not consist of p-th, fourth, or ninth powers in A[t].',
    'This is the earlier run’s algebraic observation motivated by the manuscript integral formula, not a statement occurring on these pages. It is independently proved by base-p digits here.',
    'Entire statement is an explicitly attributed earlier-run reconstruction.')
add(232,[247],'idea of the earlier run',[73,74],'891–982','G_0',
    'In characteristic 2, s=t+t^2 has unit first derivative and Q(s)=1; in characteristic 3, s=t+t^3 has Q(s)=-1, where Q=-(D3s)/(D1s)+(D2s/D1s)^2. Equality of ordinary differentials therefore does not imply equality of integral projective jets.',
    'The earlier run’s examples are valid and were recomputed. They do not constitute an authorial claim or a general classification.',
    'The examples belong to the earlier run, with verification by this run.')
add(233,[248],'idea of the earlier run',[73,74],'891–982','G_0',
    'Let A be an F_p-algebra and q=p if p>3, q=4 if p=2, q=9 if p=3. In A[t]/(t^q), any s with unit D1s and Q(s)=0 is a fractional linear function of t with invertible determinant and denominator.',
    'This nilpotent-model theorem is absent from the manuscript passage; the prior-run proof is not attached. A new coefficient-normalization proof and finite-field diagnostics are provided here.',
    'The theorem is explicitly an earlier-run idea independently re-proved in this audit, with no novelty claim.')
add(234,[249],'idea of the earlier run',[73,74],'891–982','G_0',
    'The preceding theorem extends to A[t]/(t^q-alpha) if Pic(A)=0, by faithfully flat adjoining of a q-th root and descent of the locally unique projective matrix. Invertible determinant and denominator descend; determinant one need not.',
    'This is a carefully delimited reconstruction, not a theorem of scans 72–74. The descended line of matrix representatives is the reason for the Picard hypothesis.',
    'Earlier-run idea; the present proof identifies precisely the faithfully flat descent input.')
add(235,[250],'idea of the earlier run',[73,74],'891–982','G_0',
    'An invertible projective matrix need not admit a determinant-one representative over the base. For s=2t over F_5, every representative is a scalar multiple of diag(2,1), so its determinant is 2d squared and cannot be 1.',
    'The counterexample has unit derivative and zero invariant, and checks the projective matrix ambiguity explicitly. No determinant-one strengthening is inferred.',
    'Earlier-run counterexample, independently recomputed.')
add(236,[251],'other',[72,73,74],'713–982','G_0',
    'Hoshi’s characteristic-two construction uses Sugiyama–Yasuda locally exact differentials and Frobenius-projective structures of level two. It does not identify the manuscript’s integral omega-squared-valued operator or prove its universal uniqueness.',
    'The note’s distinction is confirmed by Hoshi §3 and §6. First circulation is April 2020 (RIMS-1914), publication 2024; both sources were opened.',
    'This is a checked external comparison, not a claim from the manuscript.')
add(237,[252],'other',[72,73,74],'713–982','G_0',
    'Wakabayashi’s 2021 Frobenius–Ehresmann framework supplies a comparison in odd characteristic for smooth varieties over an algebraically closed field. Its stated setup does not justify a characteristic-two identification of the integral G_0.',
    'The introduction and §1.7 explicitly fix an odd prime and locally noetherian schemes. The note correctly retains that restriction.',
    'External comparison only; no implication of manuscript priority or exact equivalence.')

# The projective-bundle and connection sequence, scanned leaves 86--91.
add(238,[254,255],'unproved claim',[86],'1647–1685',(1651,1658),
    'A projective line bundle is etale-locally P(E) and corresponds to a degree-two Azumaya algebra; a global E need not exist. For an actual rank-two E, End(E tensor L)=End(E), E-dual=E tensor det(E) inverse, and P(E) has the stated line-twist ambiguity.',
    'The opening presentation must be read locally unless a global splitting is assumed. A real conic with no real point supplies a counterexample to an unrestricted global P(E) assertion.',check='agrees',overrides={254:('corrected','The global assertion requires a split Brauer class. The local P(E) description and the Azumaya object remain valid.'),255:('merged into SA04-238','The line-twist and rank-two duality identities are characteristic-independent.')} )
add(239,[256],'reading question',[86],'1684–1695',(1687,1695),
    'For rank two, the trace kernel is Gamma^2(E) tensor det(E) inverse, whereas End(E)/O is Sym^2(E) tensor det(E) inverse. They agree after inverting 2 but must be distinguished in characteristic 2.',
    'The two displayed exact sequences support divided versus symmetric powers. Replacing Gamma^2 by Sym^2 universally would erase the small-characteristic distinction.',check='agrees')
add(240,[257],'unproved claim',[86],'1697–1700;1727–1735',(1697,1700),
    'With P(E) parametrizing rank-one quotients and E of rank two, the relative tangent line is O_P(2) tensor det(E) inverse. Its pushforward is End(E)/O with the infinitesimal projective action.',
    'The formula is correct for the quotient convention fixed by the source. Reversing the projectivization convention without changing the determinant twist would be an error.')
add(241,[258,259,279],'self-flagged step',[86,88],'1702–1718;1986–1992;2009–2017',(1987,1991),
    'For e=E12, h=diag(1,0) modulo scalar matrices, f=E21, the pgl2 brackets are [e,h]=-e, [f,h]=f, [e,f]=2h. Its Killing matrix is [[0,0,4],[0,2,0],[4,0,0]], determinant -32. In sl2 with H=diag(1,-1), the corresponding brackets are [e,H]=-2e, [f,H]=2f, [e,f]=H, and H maps to 2h.',
    'The tables and request to make them explicit occur on the pages. The Killing nondegeneracy assertion needs 2 invertible; exact matrix calculations are saved.',overrides={259:('corrected','Nondegeneracy of the Killing form requires 2 invertible; its determinant in the displayed basis is -32.'),279:('merged into SA04-241','The scan 88 sl2 table is the companion of the earlier pgl2 table under H maps to 2h.')} )
add(242,[260],'self-flagged step',[86],'1719–1730',(1721,1726),
    'The proposed identification of the matrix algebra M with the pushforward of first relative principal parts of the tangent line is questionable as a canonical equivariant identification. Relative jet prolongation gives the pushed extension a canonical O direct-sum g splitting, whereas M to g admits a PGL2-equivariant scalar retraction tr/2 only when 2 is invertible.',
    'The manuscript marks M with a question. In characteristic 2 the lack of an equivariant retraction obstructs that canonical identification; an unstructured local rank-four isomorphism is weaker.',
    'The distinction between equivariant vector-bundle identification and arbitrary local isomorphism is made explicit here.')
add(243,[261,262],'unproved claim',[86],'1727–1746',(1727,1742),
    'The scalar center of the matrix algebra is O, and g=M/O is the Lie algebra of vertical projective vector fields. The trace-zero subalgebra sl2 maps isomorphically to pgl2 exactly where 2 is invertible; in characteristic 2 scalars lie in sl2 and that map is not an isomorphism.',
    'The basic quotient description is correct. The warning about characteristic is essential for identifications involving trace-zero matrices.',overrides={262:('corrected','Retain the condition 2 invertible; sl2 and pgl2 are not interchangeable in characteristic 2.')} )
add(244,[263,280],'self-flagged step',[86,88],'1755–1763;1993–2005',(1755,1763),
    'The statement AutLie(pgl2)=PGL2 requires excluding characteristic 2. Over a field of characteristic 2, pgl2 is W semidirect kh with W=span(e,f) abelian and [h,w]=w; its Lie automorphisms form GL(W) semidirect W, dimension six. Hence there are more Lie automorphisms than projective automorphisms, and every line in W is h-stable.',
    'The author explicitly warns about characteristic. The note’s failure mechanism is verified by the displayed bracket algebra; the group-theoretic torus still distinguishes roots, so the failure concerns Lie data.',
    'The six-dimensional description and counterexample are reconstruction, not an extra manuscript theorem.')
add(245,[264,270,278],'unproved claim',[86,87,88],'1771–1782;1845–1850;1970–1971',(1771,1776),
    'A rank-two direct-summand left ideal of M2 corresponding to a projective point is the set of endomorphisms killing its kernel line. For a marked quotient L to O with kernel Omega, this ideal is Hom(L/Omega,L). Two transverse marked points give two complementary such left ideals as modules; this is not a product decomposition of algebras.',
    'The ideal descriptions are compatible with the quotient convention. Statements about Borel Lie subalgebras need care in characteristic 2 and are not replaced by the stronger module description.')
add(246,[265],'unproved claim',[87],'1786–1799',(1786,1799),
    'The standard rank-two representation of GL2 does not descend to PGL2, because scalar matrices act nontrivially. This explains the absence of a canonical global rank-two E for an unmarked projective bundle.',
    'The representation-theoretic explanation is supported by the passage. It concerns the standard representation, not the existence of every other faithful linear representation.')
add(247,[266,268,269,277],'unproved claim',[87,88],'1802–1848;1959–1968',(1804,1812),
    'A marked section of a projective line bundle gives a canonically rigidified relative O(1), whose pushforward is an extension 0 to Omega to L to O to 0; Omega is the conormal line of the section. Restriction to the first infinitesimal neighbourhood identifies the rank-two extension, and the complement of the section is the associated Omega-torsor. A second disjoint section splits it; reversing the order dualizes Omega.',
    'These constructions occur on scans 87–88 and are proved by local P1 calculations. The first neighbourhood must use I squared, not I; the latter has rank one.',overrides={268:('corrected','The jet quotient must be I squared L. Pro gives I squared or I, while Codex prints I; rank and H^0/H^1 of O(-1) support I squared as a scan question.'),269:('merged into SA04-247','The affine complement is the torsor attached to the same extension.'),277:('merged into SA04-247','The second disjoint section trivializes that torsor and splits the marked extension.')} )
add(248,[267],'reading question',[87],'1827–1831',(1827,1831),
    'A cancelled augmentation/nilpotent description occurs during the construction of the marked extension, but its exact claim and cancellation scope are uncertain.',
    'No valid algebra construction is supplied to replace the cancelled words; the secure extension is given independently in the following lines.',check='agrees')
add(249,[271,272],'self-flagged step',[87],'1853–1897',(1870,1876),
    'For the marked extension 0 to Omega to L to O to 0, the projective adjoint bundle has a three-step filtration with successive quotients Omega, O, Omega inverse; its two-step subbundle is L. The text asks to express one side in terms of the other, but Pro and Codex disagree about the direction of recovery.',
    'The filtration is concrete. Pro asks to express (g,L) from the extension, while Codex asks to express the extension from (g,L); both can be constructed with the stated marking but this does not decide the ink.',check='agrees')
add(250,[273],'self-flagged step',[87],'1898–1919',(1909,1919),
    'The pairing induces g/Omega isomorphic to L-dual when 2 is invertible. In characteristic 2 it can fail: for a nonsplit extension of O by O on a smooth elliptic curve, the adjoint quotient transition has coefficient 2a and splits, while the dual extension remains nonsplit.',
    '“vérifier!” and the earlier invertibility-of-2 warning are present. The note’s characteristic restriction is necessary, and the transition counterexample is independently checked.',check='agrees')
add(251,[274],'unproved claim',[87],'1901–1907',(1901,1907),
    'The central quotient SL2/mu2=PGL2 is valid as an fppf sheaf in every characteristic. In characteristic 2 the kernel mu2 is not etale, so an etale or pointwise quotient description would lose information.',
    'The group-scheme quotient and the Lie-algebra issue are distinct; the latter does not invalidate the fppf central isogeny.')
add(252,[275],'reading question',[87],'1944',(1944,1944),
    'Pro transcribes an isolated “faux” after the diagram, whereas Codex K93-09:523 reads “plus bas”. Neither the word nor its attachment can be resolved without the scan.',
    'The note’s retraction language is too strong given the independent witness. No earlier theorem is declared withdrawn solely on this basis.',check='overstates',verdict='corrected')
add(253,[276],'self-flagged step',[87],'1946–1953',(1946,1953),
    'The author asks for an explicit description of connections on the projective object in terms of the extension data. Scans 89–91 continue this request with a filtered adjoint connection and a universal first-order operator.',
    'This is a genuine forward problem, partly answered in the immediately following sequence; it is not an unrelated open question.')
add(254,[282],'unproved claim',[89],'2028–2051',(2030,2040),
    'A locally constant trivialization of the three-dimensional bracket bundle supplies a local flat reference connection c_0 preserving the bracket. This is a local device; a globally defined flat reference connection does not follow.',
    'The passage explicitly chooses local data. A global splitting or global flatness claim would exceed the construction.')
add(255,[283,286],'withdrawn in the same text',[89,90],'2052–2057;2081–2090;2160–2163',(2160,2163),
    'The assertion that every Lie derivation is inner is corrected on scan 90 by requiring 2 invertible. In characteristic 2, D(e)=f, D(h)=D(f)=0 is an outer derivation, and the bracket-preserving connection d+D dt need not preserve the stated filtration transversality.',
    'The restriction is an authorial later correction, with both locations retained. The counterexample meets the displayed bracket relations and is recomputed.',check='agrees',overrides={286:('corrected','Bracket compatibility alone does not force the desired transversality in characteristic 2; the added 2-invertible hypothesis restores the inner-derivation argument.')} )
add(256,[284,285,287,288,289],'unproved claim',[89,90],'2059–2076;2081–2109',(2088,2105),
    'Writing the inner connection coefficient as a e+b h+c f gives adjoint columns (b,-2c,0),(-a,0,c),(0,2a,-b). The induced maps on successive filtration quotients are O-linear, c12=-2c23, and c23=0 exactly when the connection preserves the marked Borel/section.',
    'The unfinished matrix of scan 89 is completed on scan 90. Exact brackets verify the coefficients; O-linearity follows because the Leibniz term dies in the graded quotient.',overrides={284:('merged into SA04-256','The following page completes the interrupted matrix, so this is not a permanent open calculation.'),288:('merged into SA04-256','The factor -2 is the matrix relation between the two successive second-fundamental-form maps.'),289:('merged into SA04-256','Vanishing normal component is exactly preservation of the Borel filtration for a projective connection.')} )
add(257,[290,291,292],'unproved claim',[90],'2111–2129',(2111,2124),
    'The sheaf of projective connections, locally nonempty, is a torsor under g tensor omega. Its normal component has a canonical zero because derivatives of changes of Borel frame are Borel-valued. Fixing a prescribed normal component i leaves a torsor under L tensor omega.',
    'The torsor assertions concern sheaves and local lifts. They do not assert that global sections of these torsors exist; the normal-component zero is compatible with Borel gauge change.')
add(258,[293,294,295,296,297,298,299,300],'unproved claim',[90,91],'2131–2209;2217–2254',(2217,2227),
    'The restricted connection C_Omega is a first-order operator Omega to L tensor omega with symbol the inclusion and quotient -2i. A quotient restriction retains the normal coefficient in characteristic 2 when C_Omega loses it. If -2i is an isomorphism, then 2 is invertible and omega is a line bundle; the restricted data are uniquely the principal-parts construction L=P^1(omega) tensor omega inverse with its universal operator. Full compatible connections, if any globally, still form an omega-squared torsor. Over a smooth complex curve the transverse projective connection with marked section is a PGL2-oper.',
    'The first-jet normal form concerns restricted data, not a unique full global connection. The phrase “exists iff omega invertible” inherits the preceding invertibility and transversality assumptions. Neither Gauss–Manin origin nor global connection existence follows.',overrides={294:('corrected','The quotient restriction can detect c in characteristic 2 whereas C_Omega only detects -2c; equivalence of these restrictions requires 2 invertible.'),296:('corrected','The condition that -2i be an isomorphism itself forces 2 invertible; it cannot be imposed nontrivially in characteristic 2.'),298:('corrected','The claimed existence of restricted triples requires all preceding hypotheses, including 2 invertible. Invertibility of omega alone does not assert smoothness or global full connections.'),299:('corrected','The remaining quadratic-differential torsor can have a global obstruction; local existence is what the construction supplies.'),300:('merged into SA04-258','The modern PGL2-oper identification is valid for smooth complex curves with transversality, and does not identify a period-family construction.')} )
add(259,[301],'reading question',[86,88],'1665–1668;2007–2017',(1665,1668),
    'The rank-three trace-zero algebra and its three displayed generators require sl2, not sl1.',
    'Pro gives an index alternative and Codex prints sl1. Rank and brackets support 2, but only the scan can decide the written index.',check='agrees',verdict='corrected')
add(260,[302],'reading question',[91],'2244–2254',(2244,2254),
    'The subscript on the universal first-order operator should name the line bundle whose jets are used, here omega, if the displayed principal-parts construction is intended.',
    'The alternative infinity-like subscript is not interpreted as a different operator; the exact written symbol remains a scan question.',check='agrees')

# Context-derived links and source registers. These are not new manuscript claims.
add(261,[303],'other',[72,73,74,75,76,77,78,80,81,82,84,86,87,88,89,90,91],'713–1597;1629–2254','',
    'The supplied leaves support a projective-differential sequence from Schwarzian cocycles to marked projective bundles and transverse connections.',
    'The object-level continuation is explicit. Its relation to a particular Gauss–Manin system requires separate family and comparison data.',
    'The sequence is an editorial synthesis, not an additional theorem.')
add(262,[304],'other',[47,48,49,51,53,54],'2–192','',
    'The crystalline and Barsotti–Tate pages form another sequence. Their general comparison with connections does not supply a specific period family for the later Schwarzian formulas.',
    'The note correctly resists joining the two sequences by catalogue headings alone; the concrete crystalline claims are audited by notes_93_a.',
    'Contextual separation, not an assertion of mathematical independence in every possible future construction.')
add(263,[253,305],'other',[72,73,74,80,81,82],'713–982;1206–1597','',
    'An integral low-jet invariant and its small-characteristic behavior do not by themselves define p-curvature, a Frobenius descent of a connection, or a Picard–Fuchs family.',
    'No family, horizontal connection with arithmetic models, or p-curvature computation is present in these formulas. The later related sections require independent comparison.',
    'This is a scope check of earlier context leads, not a negative theorem about every possible relation.')
add(264,[306],'other',[50,52,55,56,57,58,59,60,61,62,63,64,65,66,67,70,83],'77–158;195–712;1604–1626','',
    'The cancelled analysis exercises, administrative sheets, Euler-characteristic arguments, and homotopy question must be read as distinct sequences rather than a single Gauss–Manin proof.',
    'Titles, cancellations and topic changes support this documentary separation; the substantive claims are assigned to notes_93_a.',
    'Editorial organization only.')
add(265,[307],'other',[47,48,72,73,74,86,87,88,89,90,91],'2–51;713–982;1645–2254','',
    'The earlier run’s contextual references to cotes 159 and 64 lie outside the supplied topic sources and cannot be checked at both endpoints here.',
    'Retained only as contextual leads, with no verified Stage 5 mathematical link to unavailable material.',
    'An earlier-run context lead, explicitly not evidence from this manuscript.')
add(266,[308],'other',[72,73,74,82],'713–982;1563–1579','',
    'The contextual report of Hua sections VII–VIII (pages 95–107) concerns the Riccati relation 2lambda-prime+lambda squared=mu, the same local coefficient appearing on scan 82. Those target pages are absent from the supplied texts.',
    'The local formula on scan 82 is checked; the unavailable target cannot support a completed cross-folder verification.',
    'The cross-reference is inherited from the earlier notes; its target is not silently reconstructed.')
add(267,[245,309],'other',[72,73,74],'713–982','',
    'The contextual report about Frobenius level p squared and projective rigidity belongs to Hua section IX, reported pages 121–123, not to the displayed low-order formulas on scans 72–74. These target pages are not supplied.',
    'The note correctly separates low-order differential identities from the stronger later assertion. It is retained as an unchecked target lead, not a manuscript claim established in this scope.',
    'Earlier-run cross-reference; no theorem about arbitrary positive-characteristic schemes is inferred.')
add(268,[310],'other',[75,76,78,82,135,136,137,138,139,140],'990–1095;1149–1205;1429–1597; codex/K93-01 and K93-02 targets','',
    'The later uniformization/connection material reported for Hua section X (125–139) must distinguish a torsor of connections from a canonical global uniformization. Only its supplied overlap at scans 135–140 can be checked in this run.',
    'The source side is verified here; root audits the supplied target. The absent pages 125–134 are not counted as read.',
    'Context lead with partial supplied overlap; no universal canonical choice is attributed.')
add(269,[311],'other',[75,76,78,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161],'990–1095;1149–1205; codex/K93-01 and K93-02 targets','',
    'The later connection/de Rham/Picard–Fuchs discussion supplies possible comparison data, but a connection torsor is not automatically a distinguished Gauss–Manin connection.',
    'The note is retained as a qualified contextual comparison; the target is separately audited by root with corrected scan numbering.',
    'Earlier-run lead; target theorem and hypotheses belong to its own claim records.')
add(270,[312],'other',[47,48,162,163,164,165,166,167],'2–51; codex/K93-02:232–322; K93-03:2–105','',
    'The filtered Gauss–Manin connection in the later leaves can be compared with the crystalline continuation, only after specifying the de Rham object, filtration and relative morphism.',
    'The link is object-level; no filtered comparison equivalence follows from a shared word “connection”. The target is audited by root.',
    'Contextual comparison, not a new equivalence theorem.')
add(271,[313],'other',[72,73,74,169,170,171,172,173],'713–982; codex/K93-03:114–357','',
    'The later Cartier construction concerns cohomology classes of closed forms. A proposed form-level map dx maps to x^(p-1)dx is not additive before quotienting by exact forms; thus it cannot be imported as a direct description of the integral Schwarzian.',
    'The note’s cautious comparison is retained, with the target correction supplied by root’s audit. For p=2 the additivity defect is d(xy), confirming the need for the cohomology target.',
    'The connection is a contextual lead. The correction is a mathematical counterexample, not an ink correction.')
add(272,[314],'other',[72,73,74,194,195,196,197,198],'713–982; codex/K93-05:10–112','',
    'The later p-curvature and finite-monodromy question has arithmetic connection hypotheses absent from the Schwarzian pages. Its present status must be stated for the exact conjecture or special case.',
    'The note correctly does not treat a later broad theory as an identification. Root supplies the current literature status and exact target claim.',
    'Contextual lead, distinct from a proof of the p-curvature conjecture.')
add(273,[315],'other',[72,73,74,199,200,201,202,203,204],'713–982; codex/K93-05:113–249','',
    'Iterated Cartier or Frobenius operations and their eigenvalue questions belong to the later supplied leaves; they do not follow merely from a low Hasse-jet kernel calculation.',
    'Retained as a non-identification warning and a target lead, whose precise assertions are audited by root.',
    'Earlier-run contextual comparison only.')
add(274,[316],'other',[76,205,206,207,208,209,210,211,212,213],'1055–1090; codex/K93-05:250–294; K93-06:2–231','',
    'The Picard scheme of line bundles with connections and a universal vector extension provide a global moduli comparison with the local frame/connection quotient, subject to smoothness, properness and the chosen equivalence of connections.',
    'The source local quotient is checked here; root audits the target constructions. The local quotient alone does not prove global representability.',
    'Object-level comparison; global moduli assertions require their own hypotheses.')
add(275,[317],'other',[76,90,91,214,215,216,217,218],'1055–1090;2111–2254; codex/K93-06:232–404','',
    'The later obstruction class for line-bundle connections explains why a locally nonempty connection torsor need not have a global section. This is the precise limitation relevant to scans 90–91.',
    'The distinction is already necessary in the present local calculations; the target obstruction is audited separately by root.',
    'A checked conceptual link only when paired with root’s actual target record.')
add(276,[318],'other',[219,220],'codex/K93-06:405–432','',
    'The later organizational plan of the connection/cohomology material is a plan and an ordering device, not a completed proof or an established equivalence.',
    'The note keeps programme language distinct from claims. Root audits the actual plan leaves.',
    'Documentary link, not a mathematical result.')
add(277,[319],'other',[72,73,74,80,81,82,222,223,224,225,226,227,228,229,230],'713–982;1206–1597; later period-integral dossier','',
    'The later period-integral pages supply relative forms, cycles/paths and differential equations missing from the present Schwarzian formulas. Their admitted differentiation step remains a separate claim.',
    'The source-side absence and the later comparison are kept distinct. The later93 agent audits the period-integral target; Hua’s numbering is not copied as an exact supplied scan locator.',
    'Context lead with a separate target audit; no automatic Picard–Fuchs interpretation.')
add(278,[320],'other',[91,231,232,233],'2217–2254; later differential-operator dossier','',
    'The first principal-parts construction is a first-order universal property. It does not establish later higher-order exactness or differential-operator factorization from a formal Poincare hypothesis.',
    'The note is a correct scope restriction; the later93 agent audits the separate higher-order claims.',
    'Contextual comparison, not an implication proved by the first-jet argument.')
add(279,[321],'other',[47,48,234,235,236],'2–51; later canonical-comparison dossier','',
    'Canonical comparisons of lifts and their homotopies must descend through sheaf torsors of identifications. A check limited to groups with a chosen point is not already a check for arbitrary sheaf torsors.',
    'The note correctly isolates the stronger descent obligation; the later93 agent audits the supplied target and its qualifications.',
    'Earlier-run lead, with no unavailable proof-assistant development counted as a proof.')
add(280,[322],'other',[47,48,49,51,53,54],'2–192; notes:2802–2817','',
    'A source register for Barsotti–Tate, crystalline, Tate and period-domain assertions lists eight external works and the exact claimed uses.',
    'This is bibliography, not a new manuscript claim. The substantive source verification and counterexamples are in the corresponding notes_93_a claim records; inherited “checked” wording is not itself a check event here.',
    'The register’s historical statements are not taken as independent evidence.')
add(281,[323],'other',[55,56,58,60,62,64,66,83],'195–627;1604–1626; notes:2819–2831','',
    'The Euler/homotopy reference register records sources and the boundary between accessible survey proof and inaccessible original theorem.',
    'The bibliographic entry is retained as a register; notes_93_a verifies each source used by its own claims. No inherited source event is credited to this audit.',
    'Bibliographic evidence only.')
add(282,[324],'other',[72,73,74,80,81,82],'713–982;1206–1597; notes:2833–2841','',
    'The differential-invariant reference register separates classical complex projective structures, positive-characteristic comparisons, finite-projective descent, and the conditional Riemann–Roch inference.',
    'Dumas, Hoshi, Wakabayashi and the cited Stacks pages were actually opened in this audit; each precise limitation is retained. Earlier proof records named in the notes are not attached and were not claimed as rerun.',
    'Bibliographic source check, distinct from independent proof of the manuscript claims.')
add(283,[325],'other',[86,87,88,89,90,91],'1645–2254; notes:2843–2850','',
    'The projective-bundle reference register fixes quotient conventions, Azumaya locality, first principal parts, and the characteristic-zero oper comparison.',
    'All four listed URLs were opened here and matched to those limited uses. Their broad subjects do not establish every characteristic-dependent assertion in the notes.',
    'Bibliographic source check only.')
add(284,[281],'reading question',[88],'1978;2020–2023',(2020,2023),
    'The terminal “couple de Killing” may mean an ordered opposite-Borel or Cartan-related datum. Separately, the earlier parenthesis reads “cf. Ch. Klein|cf. Ch. Killing” in Pro and “ss. Cartan|SGA3” in Codex. Neither is an identifiable exact citation.',
    'A mathematical interpretation through opposite Borel subgroups is plausible, but no precise theorem or reference is identifiable from the transcriptions.',check='agrees')

seen=[int(e['entry_id'].split('#')[-1]) for e in entries]
assert sorted(seen)==list(range(161,326)), (sorted(set(range(161,326))-set(seen)),len(seen))
assert len(seen)==len(set(seen))
entries.sort(key=lambda e:int(e['entry_id'].split('#')[-1]))
with (OUT/'entries.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'entries':len(entries),'items':len(items),'entry_range':[min(seen),max(seen)]}))
