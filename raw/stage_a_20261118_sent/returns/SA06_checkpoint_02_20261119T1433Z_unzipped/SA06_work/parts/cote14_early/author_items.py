#!/usr/bin/env python3
"""Serialize manually adjudicated entries after reading notes and source passages.

All judgments below were authored individually. No headings/keywords assign verdicts.
Line references are physical lines in the supplied combined .tex files, not ink lines.
"""
from pathlib import Path
import csv, json
from datetime import datetime, timezone

OUT=Path(__file__).resolve().parent
P='MPL_14_002-044'
items=[]; entries=[]
def add(n, sources, kind, scans, lines, words, statement, reconstruction, check, reason, verdict='kept'):
    ss=[f'{P}#{s}' for s in sources]
    item=dict(id=f'SA06-{n}',sources=ss,kind=kind,cote='14',scans=scans,lines=lines,
              his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason)
    items.append(item)
    for j,s in enumerate(ss):
        entries.append(dict(entry_id=s,item_id=item['id'],verdict=('merged into item '+str(n) if j else verdict),reason=reason))

add(1,[1],'idea of the earlier run',[41,42],'Pro 893–929',
    'La conj de Tate; produit de deux courbes elliptiques',
    'Earlier-run comparison: for finite-field abelian varieties and l invertible, Tate Hom compares Hom(A,B)⊗Z_l with Galois-equivariant Tate-module maps; abelianizing a dominant map of proper hyperbolic curves gives the corresponding Jacobian map. The anabelian theorem uses sub-p-adic base fields and a different domain of morphisms.',
    'The anabelian comparison and both modern Hom theorems are the earlier run’s additions; the pages only assume a divisor Tate assertion and announce invariant generation.',
    'agrees','The note itself explicitly keeps the different base fields and says no anabelian theorem occurs here. Retained as an earlier-run idea, not an authorial conjecture.')
add(2,[2],'idea of the earlier run',[3,7,11],'Pro 13–28,90–107,194',
    'classes de rep.; Regarder G commutatif !',
    'For G=G_m over characteristic zero, Rep(G) is semisimple but Z(G)=G. Thus semisimplicity of a Tannakian category does not imply a trivial center of its Tannaka group. Comparing this with center-free geometric fundamental groups is only a comparison of different actions.',
    'All center comparisons are editorial; no center-free assertion about motives is on these pages.',
    'agrees','The stated torus example tests a possible contextual conflation and preserves the distinction between tensor automorphisms and conjugation.')
add(3,[3],'idea of the earlier run',[11,13],'Pro 184,244–250',
    'définissant une polarisation; Ker ε est compact',
    'A polarization in a Tate category is related to a compact inner real form of the kernel of its Tate character. For a real abelian variety with a real polarization, conjugation changes its Weil pairing by the cyclotomic character, equal to −1 at conjugation.',
    'The comparison with real sections of hyperbolic curves is an earlier-run construction. The absent structure 3° prevents identifying all of the manuscript’s polarization axioms.',
    'agrees','The note carefully identifies a common Tate-module realization without asserting that this answers the author’s effectivity questions.')
add(4,[4],'idea of the earlier run',[3,7,11,41],'Pro 27–28,107,196,893–915',
    'motifs effectifs de poids; éléments de Frobenius',
    'For a characteristic-zero open curve U=X−D, the toric cusp part of the geometric abelianized fundamental group maps to the Tate module of its generalized Jacobian; rational cusp inertia has cyclotomic conjugation. Openness of a normalizer image alone is not an equality of characters.',
    'The exact fundamental-group sequence, weights −2 and −1, and the normalizer comparison are the earlier run’s additions.',
    'agrees','Nothing on the cited manuscript passages proves the named LM normalizer result; the note explicitly leaves its status unchanged.')
add(5,[5],'other',[11,41],'Pro 196,893–915',
    'propriétés arithmétiques plus profondes',
    'The cited LM7 E.23, FLAGGED_149 B9, LM6 A.22, LM7 C.5/C.8 and LM7_PUSH E.67 are earlier-project register records, not claims recoverable from this manuscript. They receive no new mathematical verdict here.',
    'No reconstruction of missing project definitions is made.',
    'agrees','The body explicitly bounds its claim to unavailable register content and records no Gaussian-norm formula on these pages.')
add(6,[6,94],'reading question',[2,3,9,11],'Pro 3–13,139–146,180–192',
    "Structure d'effectivité; 4°) La donnée d'une sous-catégorie",
    'The surviving title is Structure d’effectivité, after a cancelled broader title. The numbered fourth structure is imposed on an already named category M; these sheets do not construct M or define the preceding third structure.',
    'M is not silently identified with Chow, numerical, Nori or André motives. H01’s title observation is the same documentary item.',
    'agrees','Both notes correctly distinguish a surviving local title and pre-existing notation from an absent construction; no total page count is written.')
add(7,[7],'unproved claim',[3],'Pro 13–30',
    "Il y a lieu de poser d'autres axiomes",
    'Proposed structure: a strictly full subcategory M+ closed under finite sums, tensor products and subobjects, containing the Tate object Λ(−1), with every object effective after some integral Tate twist. Additional proposed conditions concern nonnegative grading, G0 and a rational-character cone. The text asserts descent between Q and C descriptions.',
    'Finite sums and finite-dimensional rational representations make the modern wording precise; the deleted quotient closure, deleted unit, and uncertain λ/Λ operation are not reinstated. Unrestricted complex subcategories do not descend without Galois compatibility.',
    'agrees','The note calls these proposed axioms and does not turn the rational/complex equivalence into a proved unrestricted descent theorem.')
add(8,[8],'self-flagged step',[3,15],'Pro 27–28,310',
    'nb fini de types de motifs effectifs de poids; ???',
    'The proposed fixed-weight finiteness has an undefined word “types”. It cannot mean all isomorphism classes: E⊕r has the same weight and dimension r dim E. The separate weight-zero condition is that G0 act trivially.',
    'Restricting “types” to irreducibles is a possible reconstruction, not a reading. Even irreducible Artin motives need not be finite globally; a fixed finite-type quotient would change the question.',
    'agrees','The earlier note’s direct-sum objection is valid and explicitly refrains from deciding the intended quantifier.')
add(9,[9],'reading question',[3,5],'Pro 13,57–61',
    'E(-n); E(n)',
    'Both displayed signs are retained. If n ranges over all integers, existence of E(n) is equivalent to existence of E(−n). For a nonnegative twist exponent N, tensoring with Λ(−1)^N shifts every i-weight a to a+Nε(i).',
    'The formula fixing the direction of the weight shift is an editorial calculation; the page specifies ε(i)>0.',
    'agrees','No contradiction follows from unrestricted integer quantification, but a directional construction needs the sign convention.')
add(10,[10],'unproved claim',[5],'Pro 57',
    'ses conjugués; en particulier de bar i',
    'For i′=g i g−1, ρ(g) maps the i-weight-a space to the i′-weight-a space; hence P(i)=P(i′). Conjugation by field automorphisms has the same consequence when the representation and selected effective subcategory have the stated rational descent data.',
    'The explicit intertwining identity supplies a proof of the inner-conjugation statement; the descent qualification is kept separate.',
    'agrees','The note does not infer field-automorphism invariance from inner conjugation alone.')
add(11,[11],'self-flagged step',[5,9],'Pro 64–65,135–137',
    'sauf peut être au dernier sur la graduation',
    'Intersections preserve the listed closure properties but can lose eventual Tate effectivity. In G_m², ε=x and i_m(t)=(t,t^m) for all integers m, the character yε^N has weight m+N and no single N makes it nonnegative for every m.',
    'The counterexample is the earlier run’s exact model, not the author’s own example; it does not decide which final condition the uncertain wording names.',
    'agrees','The explicit family verifies a genuine uniformity obstruction relevant to the author’s caveat.')
add(12,[12],'self-flagged step',[7],'Pro 90–107',
    "invariant pr W (mais peut-être pas pr W'!",
    'The cone is required to be invariant under the Weyl group, not all outer automorphisms. For a split rank-two torus W=1; y↦y−1 sends (1,1) outside the cone generated by (2,0),(1,1), while fixing ε=x and j=(2,0).',
    'This earlier-run test uses only the displayed lattice conditions and is not a counterexample to unseen polarization axioms.',
    'agrees','The note preserves exactly this limited scope.')
add(13,[13],'reading question',[7,13,15],'Pro 92–107,236,291–297',
    "Γ'=Γ/W; Γ=S(C); via un quotient fini",
    'The conjugacy-orbit set is Γ/W, not generally Γ. A finite-rank torus character lattice has continuous Galois action through a finite quotient. An infinite product of restriction-of-scalars tori can have infinite total Galois image.',
    'The missing prime is a scan alarm. The protorus example is the earlier run’s boundary test; finite-rank is explicit on scan13.',
    'agrees','Finite-type and inverse-limit statements are correctly distinguished; no prime is silently supplied.')
add(14,[14],'self-flagged step',[9],'Pro 135–137',
    'saturation que nous ne précisons pas ici',
    'The claimed cone parametrization includes an undefined saturation condition and asks if it is automatic. The polar-interior phrase does not specify an ambient vector space, topology or quotient-cone structure.',
    'A modern Galois connection between cocharacters and nonnegative character inequalities is a possible reformulation, not an identification of the missing definition.',
    'agrees','The exact unspecified datum is retained; no standard saturation is substituted.')
add(15,[15],'idea of the earlier run',[9],'Pro 135,141',
    'ε i1=id',
    'The monoids 2N and N in X*(G_m) impose the same nonnegative character inequalities. Their equality of positivity tests does not settle injectivity for normalized cocharacters satisfying ε∘i=id.',
    'Entire rank-one test is editorial.',
    'agrees','The normalization excludes the naive doubling argument as a counterexample to the author’s stated map.')
add(16,[16],'unpursued implication',[9,13],'Pro 141,238',
    'i1 bar i1=j',
    'With rational ε and ε∘i1=id, applying ε to i1 bar i1=j gives ε∘j(t)=t². Thus Λ(−1) has weight +2 in this convention and its dual has weight −2.',
    'The modern notation Q(−1) is a comparison convention; the missing third structure is not reconstructed.',
    'agrees','The weight conclusion follows from the displayed normalization, without additional motivic assertions.')
add(17,[17],'self-flagged step',[11],'Pro 182–190',
    'Cette dernière application; injective ?',
    'Two nearby possible questions must be retained: injectivity of I^a(G)→Pol(G)×Eff(G), and of I(G)→Eff(G). Real conjugacy is mentioned, but I(G) depends on missing earlier axioms.',
    'Neither domain is silently completed; the precise normalized problem is therefore only partially identifiable.',
    'agrees','The note correctly avoids resolving this ambiguity by an unrelated scaling counterexample.')
add(18,[18],'self-flagged step',[11],'Pro 188',
    'sont elles dans Im I(G) ?',
    'The author asks whether effectivity structures arising from motives equal P(i1) for one admissible normalized cocharacter, rather than an intersection of positivity subcategories.',
    'Admissibility is not fully specified in the fragment, so the strongest precise modern statement requires an explicit chosen motivic category and realization.',
    'agrees','The question is correctly separated from the existence of arbitrary cone descriptions and from later Nori comparisons.')
add(19,[19],'unproved claim',[11],'Pro 190–192',
    'intrinsèque à la catégorie; en tordant pr un torseur',
    'Changing a fiber functor through P=Isom⊗(ω,ω′) transports representations by P×G V and the group by its inner form. Trivializations change cocharacters by conjugation, preserving their weight inequalities.',
    'The contracted-product proof is a modern reconstruction of the suggested torsor argument; descent of unspecified I(G) conditions is not proved.',
    'agrees','The page claims intrinsicness and suggests the correct mechanism; the note properly bounds the completed argument.')
add(20,[20],'self-flagged step',[11,13],'Pro 192,232',
    'motif sur schéma connexe S; foncteur de De-Rham',
    'The author proposes examining four structures for motives over connected S with a rational point and a de Rham fiber functor. The opening Hodge/de Rham sentence on scan13 is deleted.',
    'No relative category or six-functor formalism is present. The comparison with external cote54 is a context lead whose other endpoint is absent from this part.',
    'agrees','The earlier note does not substitute degree-one comparison sequences for the missing relative construction.')
add(21,[21],'reading question',[11],'Pro 194',
    'G=Sl(2,Q)|Gl(2,Q)',
    'The group name is unresolved. In GL2, θ(g)=det(g)−1g fixes SL2 pointwise and sends det to det−1, so a distinguished Tate character matters. SL2 itself has no nontrivial algebraic character to G_m.',
    'The automorphism test is earlier-run mathematics. The character obstruction favors checking GL2 on the ink but does not determine it.',
    'agrees','The note preserves both readings and tracks the exact character rather than promoting a register result.')
add(22,[22],'conjecture',[11],'Pro 196',
    'peuvent être sans doute formulées; éléments de Frobenius',
    'The author expects arithmetic refinements and interpretations of structures 3° and 4° through Frobenius. No field of definition, realization or exact criterion is stated.',
    'A modern Frobenius criterion cannot be reconstructed uniquely from this expectation.',
    'agrees','The note correctly retains an expectation rather than an identifiable theorem.')
add(23,[23],'unproved claim',[13,15],'Pro 236–240,291–308',
    'K(T)=Z(M)^π',
    'For a Q-torus split by finite Galois L/Q with character lattice M, rational characters identify K(T) with Z[M]^Gal(L/Q); actual representations correspond to invariant sums with nonnegative integer coefficients. This invariant ring is finitely generated over Z.',
    'The orbit-representation descent proof is editorial; finite generation follows from finite-group invariant theory for the finitely generated Laurent ring.',
    'agrees','The claim concerns representation characters, not an intrinsically selected motivic effective cone.')
add(24,[24],'unproved claim',[13],'Pro 244–250',
    'J’affirme; Ker ε est compact',
    'For the polarizable torus under consideration, the author asserts compactness of ker ε and split quotient dimension one. The attempted two-dimensional proof beneath this assertion is cancelled.',
    'Under modern polarized Tate-triple axioms the compact-inner-form criterion gives the conclusion because a torus has trivial inner action; identification with missing 3° remains conditional.',
    'agrees','The assertion survives. Only the attempted proof, not automatically the assertion, is withdrawn.')
add(25,[25],'withdrawn in the same text',[13,15],'Pro 244–250,310',
    'ne peut pas; Q pr R; Fausse',
    'In the fixed-weight finiteness discussion, replacing Q by R is explicitly rejected. The final uncertain phrase does not securely retract the earlier compact-kernel assertion.',
    'The scope of “Fausse” remains a reading question; no new target is supplied.',
    'agrees','Both the surviving assertion and the later rejection are retained with their separate scopes.')
add(26,[26],'self-flagged step',[15],'Pro 300',
    'valeurs ≥0; S(R)° ??',
    'Nonnegative evaluation on positive real points does not characterize actual representation characters or nonnegative cocharacter weights: x−1>0 has negative weight, and x²−x+1>0 has a negative coefficient.',
    'These are the earlier run’s counterexamples to the literal proposed real-value test, with T=G_m.',
    'agrees','The two failures concern distinct notions; the question marks on the page are preserved.')
add(27,[27],'unproved claim',[15],'Pro 300–308',
    'fonction polynômiale i.e. restant finie; t→0',
    'A finite Laurent polynomial over R is bounded near zero if and only if it contains no nonzero negative-power term. For an actual character restricted along i1, coefficients are nonnegative, so this is equivalent to nonnegative i1-weights.',
    'The least-exponent proof is editorial and requires an actual representation for the inference from the restricted character to weights.',
    'agrees','The note verifies the chosen-cocharacter test without claiming it selects i1 intrinsically.')
add(28,[28],'idea of the earlier run',[3,15],'Pro 27–28,310',
    'T est de dim ≥3',
    'For T_R=G_m×U(1)², ε=a, j=(2,0,0), i1=(1,1,0), infinitely many irreducible real characters e^(rc)+e^(−rc) have weight and i1-degree zero, despite compact ker ε.',
    'The example violates the additional condition that effective weight-zero objects have trivial G0 action; it therefore only tests the Q-to-R simplification.',
    'agrees','The earlier note explicitly records this extra hypothesis and does not claim a counterexample to the full intended structure.')
add(29,[29],'idea of the earlier run',[3,11],'Pro 13,190–192',
    'catégorie de motifs M',
    'The correspondence construction of pure motives uses triples (X,p,m), idempotent-completed correspondence groups and composition p13*(p12*f·p23*g), with a specified adequate equivalence and coefficient field.',
    'This is a modern contextual construction, not a construction contained in these pages. The choice of contravariant convention fixes the displayed Hom degree.',
    'agrees','The note explicitly acknowledges that the manuscript begins with M already in use.')
add(30,[30],'idea of the earlier run',[3,9],'Pro 13,141',
    'M; i1 bar i1=j',
    'For a smooth quasi-projective base over a field and a polarized abelian scheme, rational relative Chow motives admit the Lefschetz decomposition and algebraic Lefschetz isomorphisms of Künnemann’s theorem.',
    'Entire comparison belongs to the earlier run; it does not identify integral unit-step lowering with normalized sl2 lowering.',
    'agrees','The source passage contains none of the later theorem’s construction; the note labels its purpose as a published bridge.')
add(31,[31],'idea of the earlier run',[9,13],'Pro 141,238',
    'i1 bar i1=j',
    'On a length-r primitive string v_a, e v_a=v_(a+1), f v_a=a(r−a+1)v_(a−1), h v_a=(2a−r)v_a satisfy sl2 brackets. Unit-step lowering differs by these coefficients. Over Q, Casimir and weight projectors generate all matrix blocks on ⊕_(r=0)^n Sym^r Q².',
    'All sl2 calculations and the direct-sum algebra model are earlier-run additions; they are not asserted by the cited effectivity pages.',
    'agrees','The calculations are mathematically checkable but must remain outside the inventory of authorial claims on these scans.')
add(32,[32],'idea of the earlier run',[3,9,13],'Pro 23,141,238',
    'graduations positives',
    'On H*(X) for a smooth projective d-fold, with degree cocharacter w acting by t^r on H^r and Lefschetz h acting by r−d, dw=h+d·id. The corresponding group equation is ρ(w(t))=t^d λ_sl2(t) on this chosen realization.',
    'This is an earlier-run comparison, not an identity of universal group morphisms across objects of different dimensions.',
    'agrees','The note gives a realization-specific scalar shift, correctly illustrated on P1.')
add(33,[33],'idea of the earlier run',[3,11],'Pro 13,190,194',
    'Λ(-1); indép. du foncteur',
    'Tensor naturality for L:h^r(X)⊗L→h^(r+2)(X) gives gLg−1=χ_L(g)L; ker χ_L commutes with normalized Lefschetz sl2. The Tate category generated by h(P1)=1⊕L has group G_m, precluding an sl2 subgroup inducing its nonzero Lefschetz action.',
    'The naturality computation and counterexample belong to the earlier run. They require a category in which the displayed operators are morphisms, such as motivated/pure Nori motives.',
    'agrees','The note does not infer an sl2 inclusion into every motivic Galois group; it supplies an exact obstruction.')
add(34,[34],'idea of the earlier run',[3,11],'Pro 13,190–192',
    'foncteur qui la réalise',
    'For a characteristic-zero field embedded in C and the coefficient PID of the cited comparison, Choudhury–Gallauer identify Nori’s motivic Galois group with the group represented by degree-zero Ayoub Betti Hopf algebra.',
    'This later theorem is an earlier-run contextual addition; it neither identifies the undefined M nor proves algebraicity of all Lefschetz inverse cycles.',
    'agrees','The note states the comparison’s domain and the Tate inversion boundary.')
add(35,[35],'idea of the earlier run',[3],'Pro 23–28',
    'graduations; poids',
    'With Q coefficients and fixed Betti embedding, Arapura’s pure Nori category is equivalent to André motivated motives; mixed Nori motives retain a pro-unipotent kernel over the pro-reductive pure quotient.',
    'Neither motivated=algebraic cycles nor semisimplicity of all mixed motives is inferred.',
    'agrees','The note properly distinguishes the correspondence theories and the pure/mixed boundary.')
add(36,[36],'idea of the earlier run',[3,11],'Pro 13,190',
    'catégorie de motifs M',
    'Jannsen proves semisimplicity for numerical motives with characteristic-zero coefficients. A homological cycle action descends to the numerical quotient only if every numerically trivial correspondence in its kernel acts trivially. A semisimple quotient alone does not imply this.',
    'The dual-number quotient Q[u]/u²→Q is an editorial algebra counterexample to an implication, not a geometric counterexample to the standard conjectures.',
    'agrees','The note makes the exact missing factorization explicit.')
add(37,[37],'idea of the earlier run',[3,11],'Pro 13,192',
    'motifs effectifs; De-Rham',
    'The Kummer relative motive H^1(G_m,{1,2}) in cohomological convention yields 0→Q(0)→M→Q(−1)→0; after twist its Hodge extension class log 2 modulo 2πiQ is nonzero, so the motive cannot split.',
    'This example is from the earlier run, not the manuscript; H^1 notation is intended throughout.',
    'agrees','The argument uses a necessary consequence of a hypothetical splitting and preserves the pure/mixed distinction.')
add(38,[38],'reading question',[7,13,15],'Pro 107,236,291–297',
    'π1(Q,C) opère',
    'These pages give Galois actions on torus/cocharacter data but no motivic Galois exact sequence. The later Nori sequence has the proconstant absolute Galois group as quotient and does not by itself identify its kernel with the identity component.',
    'The comparison sequence is contextual literature, not an authorial claim on these scans. Other supplied cote15 folders must be checked separately.',
    'agrees','The earlier note’s absence claim is correctly bounded to its forty scans; it must not become absence from the entire present dossier.')
add(39,[39],'reading question',[11,13],'Pro 192,232',
    'en tordant pr un torseur; De-Rham',
    'The local torsor suggestion is about changing realizations. It does not state injectivity of period evaluation on the comparison torsor; that later conjecture is a separate assertion.',
    'The formal-period spectrum and evaluation map are earlier-run comparisons; no period conjecture is imputed to this fragment.',
    'agrees','Torsor existence is not a proof of genericity of the comparison point.')
add(40,[40],'idea of the earlier run',[19,21],'Pro 359–470',
    'des signes différents !!',
    'For E elliptic, Y=E×P and X a projective completion of a line bundle on Y, the family z=(id×i)*Θ has degree of s*(z²) equal to −2 deg(c|{0}×P), giving ±2. Diagonal pullback compares this with the self-pairing correspondence on E×E.',
    'The diagonal comparison to external cote44 is the earlier run’s construction; that second endpoint is not supplied here. The sign computation is present and redone.',
    'agrees','The formula is valid after distinguishing c on Y from c′ on E×Y; the literal support ambiguities are recorded separately.')
add(41,[41],'reading question',[19,21],'Pro 395,441–470',
    'p*(Θ²)=−2(0×0×P)',
    'The prose defines i′:E×Y→E×X but the marginal arrow is reversed. The pushforward p*(Θ²) is on Y=E×P and should have support {0}×P; writing two E coordinates confuses it with the class before pushforward.',
    'The proposed coordinate deletion and c versus c′ distinction are mathematical alternatives only.',
    'agrees','Typing exposes the problem without deciding whether it is an ink error, notation shorthand or transcription error.')
add(42,[42],'other',[24,25],'Pro 506–531',
    'S_Y(ν)=0; égal à',
    'The relation is generated by evaluations Z*(ν), where T is smooth connected with bracketed projectivity, degν=0 and Alb_T(ν)=0. Its proposed quotient lies between Chow groups and cycles modulo algebraic equivalence.',
    'For a rigorous modern definition we work over algebraically closed k with smooth projective T and Chow correspondences; those hypotheses are explicitly marked as a reconstruction.',
    'agrees','This definition is on the page. The comparison with an unidentified relation in external cote44 remains a lead.')
add(43,[43],'self-flagged step',[24,29,30],'Pro 506,616,640',
    '[projectif]; Ici il semble; projectives lisses',
    'Projectivity of the parameter T is bracketed in the definition and specifically queried for the endpoint theorem. The product proof explicitly uses projective smooth connected parameter varieties.',
    'The dossier’s precise quotient statements retain projective parameters; a quasi-projective extension would need a separately chosen generalized Albanese.',
    'agrees','The note correctly treats the parameter category as a mathematical hypothesis, not cosmetic wording.')
add(44,[44],'reading question',[26,33,36],'Pro 543–559,740,792',
    'A_Y(k) est divisible!',
    'The choices of rational points and divisibility of A_Y(k) hold over algebraically closed k. They need not hold over an arbitrary field. The local definition says only “corps k”.',
    'An algebraically closed field is a necessary reconstruction for the written pointwise proofs as used; K14-04 scan49 later explicitly fixes it for Sorites, not retrospectively as an ink insertion.',
    'agrees','The note correctly identifies an omitted field convention and the exact multiplication map requiring surjectivity.')
add(45,[45],'unproved claim',[25,26],'Pro 533–569',
    'sous réserve que Z a été choisi',
    'Closure under addition uses T×T′, ν×a′+a×ν′ and the sum of pulled-back correspondences. Cross terms vanish because the relevant projection sends a degree-zero cycle to zero, provided all evaluations are defined.',
    'Chow correspondence operations supply a modern formal proof over algebraically closed k with projective smooth parameters; simultaneous representative choices are not written out.',
    'agrees','The qualification is accurately preserved. Codex reads the margin “Lemme à dégager”, versus Pro’s uncertain “Lemme d’isog.”; neither is silently selected.')
add(46,[46,76],'self-flagged step',[24,25,27,28,29,30,34],'Pro 506–610,616–645,749–755',
    'à vérifier; Nous laissons ici les détails',
    'Pullback stability of the Albanese-kernel relation requires compatible rationally equivalent representatives for a family and parameter zero-cycle. The author expressly leaves this moving verification unwritten; the prior Hua register wording “shows” must therefore be qualified.',
    'The register’s mathematical content is checked only against the supplied note excerpt; its absent original is not reconstructed. The same moving gap governs the quotient ring claims.',
    'agrees','A37 repeats the qualification of the same unfinished step and is merged. The notes’ explicit caution is supported by scan28.')
add(47,[47],'unproved claim',[25,28],'Pro 520–531,604–610',
    'les mêmes propriétés formelles générales; formule de projection',
    'The relation is asserted to define a graded ideal stable under pullback and proper pushforward, hence a quotient ring with projection formula. The external-product argument reduces ideal stability to pullback along the diagonal.',
    'Using Chow correspondence composition reconstructs these formal implications; the author cites an unresolved abbreviation AQT and omits the moving verification.',
    'agrees','The note correctly distinguishes stated consequences from completed representative-level proofs.')
add(48,[48],'unproved claim',[29,30],'Pro 617–630',
    'ν est de degré 0; S_X(ν)=0',
    'For smooth projective connected X over algebraically closed k and projective parameters, the zero-cycle relation is exactly ker(deg,Alb), while in codimension one it is rational equivalence; the divisor proof factors through Alb(T)→Pic0(X).',
    'The zero-cycle converse invokes a blank reference; K14-04 Cor1.2 states the needed correspondence functoriality but does not identify that blank bibliographically.',
    'agrees','The endpoint maps are actually displayed; their dependence on projectivity and field conventions is retained.')
add(49,[49],'reading question',[29,52],'Pro 625; Codex K14-04 104–122',
    'résulte de [ , 1.2.]',
    'The blank citation supports preservation of the Albanese kernel by zero-cycle correspondences. K14-04 scan52 contains precisely such Corollary1.2, following its Theorem1.1.',
    'Matching number and mathematical content gives an internal-reference candidate, not proof that this is the author’s intended citation.',
    'understates','The earlier run lacked scan52. The present archive supplies a matching statement, so the dossier records the new crosslink while retaining the blank.', 'corrected')
add(50,[50],'conjecture',[29],'Pro 623',
    'Vrai pr tous les cycles???',
    'The author asks whether Albanese equivalence equals rational equivalence, already for zero-cycles. Over C, E×E has h20=1 and a nonzero Albanese kernel by Mumford’s theorem; hence the proposed general equality is false.',
    'The specified counterexample uses the modern identification of the quotient from Theorem1.4 and the nonzero-kernel conclusion of Mumford (communicated1968, published1969).',
    'agrees','The note supplies a genuine counterexample rather than merely citing large Chow groups without an Albanese comparison.')
add(51,[51],'idea of the earlier run',[30],'Pro 640–645',
    'On ignore si cet ν est lin. équiv. à 0',
    'On E×E, boxes [(x,y)]−[(x,0)]−[(0,y)]+[(0,0)] have zero degree and Albanese image. They generate the Albanese kernel after subtracting the two axis projections, so some boxes are rationally nonzero by Mumford.',
    'The existence argument does not exhibit a particular transcendental pair (x,y); it proves that not all boxes vanish.',
    'agrees','The earlier note correctly uses existence, not an unverified explicit point choice.')
add(52,[52],'unproved claim',[30,34],'Pro 632–645,755',
    "Alors zz'=0",
    'In the reconstructed quotient with projective smooth parameters, products of two algebraically trivial classes vanish: represent them by families on T,T′ and evaluate their external product on a four-point box in ker Alb(T×T′).',
    'The modern formulation uses Chow pullbacks and exterior products and inherits the established quotient-operation hypotheses.',
    'agrees','The displayed box calculation is a proof sketch of square-zero, not a claim that the corresponding Chow product itself vanishes.')
add(53,[53],'conjecture',[30,34],'Pro 632–633,753–755',
    'num. équiv. à 0??',
    'The open strengthening asks whether one algebraically trivial and one numerically trivial factor have zero product in the Albanese quotient for projective X. The written corollary proves only the case that a positive multiple of the second factor is algebraically trivial.',
    'The τ interpretation is supported by the subsequent mu=0 argument, not supplied as a new reading of every τ elsewhere in the archive.',
    'agrees','Numerical and τ equivalence are not silently identified; the divisibility proof has exactly the weaker hypothesis.')
add(54,[54],'reading question',[31,36],'Pro 654–668,792–800',
    'A_Y^*(k); A_Y^0(k)',
    'The degree-graded Albanese object must be distinguished from its identity component. On degree-zero cycles the family map is Alb0(Y)(k)→P^i(X); all zero-cycles also retain their degree.',
    'The notation Alb* is a componentwise reconstruction. Codex reads degree0 where Pro reads degreen in scan31; this is preserved as a witness discrepancy.',
    'agrees','The note correctly prevents the zero-degree subgroup from being equated with all CH0 modulo the relation.')
add(55,[55],'self-flagged step',[31,34],'Pro 672–673,749',
    'À réserver pr plus tard; Pour (i)',
    'The dependence of u_Z only on the τ-class of Z is postponed on scan31 and addressed on scan34: algebraically trivial Z acts by zero using square-zero, while mu=0 and m-divisibility of Alb(Y)(k) imply u=0.',
    'This is a valid conditional proof over algebraically closed k once the quotient operations and square-zero have been justified.',
    'agrees','The item is a step subsequently addressed, not an outstanding proof gap or a retracted claim.')
add(56,[56],'self-flagged step',[32,33],'Pro 691–714',
    'on ne sait pas si on peut trouver U',
    'The integral universal-zero-cycle condition is Alb_Y(U(a)−U(0))=a for all a∈Alb(Y). It fails for some smooth projective complex threefolds even with representable CH0, by Voisin’s2025 Theorem1.4.',
    'Normalization at zero is made explicit. The manuscript’s replacement by multiplication n is strictly weaker.',
    'agrees','The exact condition matches the modern counterexample; this is not a claim that rational universal cycles fail.')
add(57,[57],'unproved claim',[33],'Pro 712–744',
    'On prend comme isogénie la multiplication pr n',
    'An integral cycle U with Alb_Y∘U*=[n] produces a family Z′ with v_Z′=u_Z∘[n]. Existence follows in the usual smooth-projective algebraically-closed setting by a curve surjecting on Alb(Y) and an isogeny splitting after a positive multiple.',
    'The curve/isogeny construction supplies a modern proof of the author’s unproved existence assertion; it does not prove an integral degree-one universal cycle.',
    'agrees','The displayed equality and chosen isogeny are accurately recorded.')
add(58,[58],'reading question',[33],'Pro 725–742',
    'deleted U(a)=nν; U(a)=|≡ nν',
    'Equality of Albanese images implies equality in the Albanese quotient, not equality of raw cycles. Applying Z in the quotient then gives Z′(Albν)=nZ(ν).',
    'The modern proof makes the quotient map explicit; the alternative glyph remains undecided.',
    'agrees','The note correctly preserves the cancelled n² stage and the difference between literal and quotient equality.')
add(59,[59],'reading question',[34],'Pro 751',
    'un diviseur de la forme Z(a0)',
    'For arbitrary codimension i the evaluated class Z(a0) is a codimension-i cycle, not generally a divisor. The corollary’s numbering is also uncertain between2.2 and2.7.',
    '“Cycle” is a mathematical alternative to check on the scans, not an emendation.',
    'agrees','The type mismatch is explicit and does not invalidate the correctly graded family formulation.')
add(60,[60],'unproved claim',[34],'Pro 753–755',
    'est n divisible',
    'P^i(X), the algebraically trivial subgroup of the Albanese quotient over algebraically closed k, is divisible since it is generated by images of abelian parameter groups. If z is algebraically trivial and m z′ is algebraically trivial, write z=mw to get zz′=w(mz′)=0.',
    'Divisibility alone does not establish that P^i(X) is represented by an abelian variety or give a uniform dimension bound.',
    'agrees','The note retains exactly the representability gap and the weaker product corollary.')
add(61,[61],'idea of the earlier run',[35],'Pro 764–783',
    'Si Nφ est alg., φ l’est',
    'For arbitrary point maps this saturation statement is false: Y=P1_C, X=E elliptic, t≠0 in Pic0(E)[2], φ(∞)=t and φ=0 elsewhere. Then2φ=0 is algebraic but φ fails to annihilate [∞]−[0], whose Albanese image is zero.',
    'Within maps already satisfying Definition2.5(1), multiplying the integer in condition(2) proves saturation. Which ambient group is intended requires ink/context checking.',
    'agrees','Every counterexample hypothesis is met; the note explicitly limits its refutation to unrestricted maps.')
add(62,[62],'idea of the earlier run',[35,36],'Pro 787,803',
    'un cycle à coeff rationnels quelconque',
    'The rational correspondence (1/2)Δ_E does not define an integral point-group endomorphism h of E(C) satisfying2h=id: for t∈E[2] nonzero,2h(t)=h(2t)=0≠t.',
    'This earlier-run elementary group test verifies the author’s caution; it does not deny rational correspondence actions after tensoring groups with Q.',
    'agrees','The distinction between divisible and uniquely divisible groups is exact.')
add(63,[63],'unproved claim',[36],'Pro 801–803',
    'Ces homs se composent',
    'If Nφ and Mψ are induced by integral correspondences acting on the Albanese quotient, their composed correspondence induces MN(ψφ); hence the defined algebraic homomorphisms compose.',
    'The proof is a formal consequence of descended correspondence composition and inherits its earlier intersection hypotheses.',
    'agrees','No representability of all groups P^i is needed for this specific formal closure assertion.')
add(64,[64],'conjecture',[37],'Pro 808–809',
    's’ils peuvent s’inverser',
    'If φ:P^j(X′)→P^i(X) is a group isomorphism and a positive multiple is induced by an integral correspondence, must a positive multiple of φ−1 also be induced by a correspondence?',
    'The problem concerns these quotient point groups, not automatically an inverse in a numerical-motive category.',
    'agrees','The note preserves the source and target; a later semisimplicity theorem does not directly settle it.')
add(65,[65],'unproved claim',[37],'Pro 811–818',
    'i+j=n+1',
    'For smooth projective X of dimension n, an abelian A and Z∈CH^i(X×A), transposition has the complementary action P^j(X)→P^(i+j−n)(A)=P1(A)≅A∨(k) when i+j=n+1.',
    'A correspondence-level degree calculation is established; descent to the induced homomorphism requires the separately flagged kernel statement.',
    'agrees','The note does not promote the announced bijection to a completed duality theorem.')
add(66,[66],'self-flagged step',[37,38,39],'Pro 820–825,840–878',
    'pas du cycle Z; Cf plus bas',
    'To define transpose on algebraic homomorphisms one must show that a correspondence inducing zero A(k)→P^i(X) also induces zero P^j(X)→A∨(k). The general transposition question is stated again for P-groups on two varieties.',
    'The following l-adic section addresses a related kernel assertion but ends before its proof; the broader transposition descent is not thereby proved.',
    'agrees','The note correctly treats the cross-reference as a dependency, not a completed argument.')
add(67,[67],'idea of the earlier run',[24,35,37],'Pro 506–510,764–775,811–820',
    'S_Y(ν)=0',
    'For complex smooth projective X with projective smooth parameters T, the family-induced Abel–Jacobi map factors through Alb(T); it therefore kills Z*(ker Alb_T) and induces P^i(X)→J_a^(2i−1)(X).',
    'This comparison map is an earlier-run deduction. Its injectivity and identification of P^i(X) with an algebraic representative are not proved.',
    'agrees','The note gives only factorization, which follows from regularity and the Albanese universal property.')
add(68,[68],'self-flagged step',[38,39],'Pro 838–878',
    'dém. pas faite',
    'Theorem3.1 proposes u_Z=0⇒a(tZ)=0 on rational l-adic cohomology, where a(tZ):H^(2(n−i)+1)(X)(n−i)→H1(A), for l≠char k and Z∈CH^i(X×A). The attempted reduction stops at the middle curve Künneth component.',
    'Correct source degree and rational coefficients are explicit modern reconstruction from the opening formula. The page’s abbreviated exponent is left unchanged.',
    'agrees','The author explicitly marks the proof unfinished; curve projectors do not complete the remaining kernel argument.')
add(69,[69],'reading question',[38],'Pro 840',
    'mod. torsion (i.e. à coefficients Q_l!)',
    'For finitely generated Z_l-modules, killing torsion and tensoring Q_l are different objects but give equivalent vanishing tests for a homomorphism: its rationalization vanishes exactly when its image is torsion.',
    'The lattice inclusion M/tors↪M⊗Q_l is supplied by the earlier run; equality of these modules is not asserted.',
    'agrees','The parenthetical is harmless for the displayed vanishing claim but cannot justify an integral isomorphism.')
add(70,[70],'reading question',[38],'Pro 838,848,861',
    'H^{(n-i)+1}',
    'For codimension-i Z on X^n×A, pA*(pX*α∪cl Z) has degree degα+2i−2n. Target H1(A) forces degα=2(n−i)+1, agreeing with the opening formula and exposing the short theorem exponent.',
    'The exponent2(n−i)+1 is a mathematical alternative to check; no transcript replacement is made.',
    'agrees','The note’s degree audit is exact; Codex also leaves the theorem exponent uncertain.')
add(71,[71],'reading question',[38,39],'Pro 852–872',
    'C(k)–A(k) surjectif',
    'A smooth ample curve included in an abelian surface is not surjective on algebraically closed points. The appropriate surjection is J(C)→A, whose image is generated by C; H1(A)→H1(C) is injective.',
    'The Jacobian replacement is a proposed reconstruction, not a reading; it is sufficient for a group-homomorphism vanishing reduction when the relevant family maps factor through J(C).',
    'agrees','The dimensional counterexample refutes the literal point-set surjectivity while preserving the intended route.')
add(72,[72],'unproved claim',[39],'Pro 874–878',
    'est algébrique, comme on vérifie aisément',
    'For a pointed smooth projective curve(C,c0), the cycles c0×C, Δ−c0×C−C×c0, C×c0 induce H0,H1,H2 projectors under the push-to-second-factor convention; external product with Δ_X gives the decomposition on X×C.',
    'Explicit projectors complete the local algebraicity assertion. They do not prove the subsequent middle-factor vanishing.',
    'agrees','The note provides the right convention and keeps the remaining gap distinct.')
add(73,[73],'conjecture',[38,39],'Pro 848–878',
    'A-t-on une réciproque',
    'Does a(tZ)=0 on rational l-adic cohomology imply u_Z=0 in the Albanese quotient for an abelian family of codimension-i cycles?',
    'Over C a comparison with J_a exists; identifying its kernel with zero requires an additional theorem about this specific quotient, not merely algebraic-representative existence.',
    'agrees','The converse is a separate question and is not settled by the printed reduction.')
add(74,[74],'idea of the earlier run',[38],'Pro 838–850',
    'ne dépend que de u_Z',
    'For a surjective regular homomorphism from codimension-i algebraically trivial cycles to an abelian B and a miniversal cycle of degree r, the cited modern Tate-module embedding is proved for i=1,2,dimX and primes l≠charK with l∤r.',
    'This concerns B and its miniversal cycle; identifying B(k) with the manuscript quotient is extra work.',
    'agrees','The note retains codimension and prime restrictions and does not claim a general proof of Theorem3.1.')
add(75,[75],'idea of the earlier run',[19,37],'Pro 375–392,811–820',
    'Dualité; pas du cycle Z',
    'For geometrically stably rational smooth projective threefolds over perfect fields, the cited2025 work constructs canonical autoduality of the codimension-two algebraic representative using −tZ∘Z. In characteristic zero it matches the intermediate-Jacobian principal polarization.',
    'The positive-characteristic positivity conjecture and arbitrary-codimension program remain separate.',
    'agrees','The note matches the transpose and sign while preserving its specific hypotheses.')
add(77,[77],'idea of the earlier run',[38,39],'Pro 830–878',
    'Homomorphisme l-adique',
    'Oda’s degree-one characteristic-p results compare Dieudonné modules of p-torsion and de Rham cohomology, retaining the full Picard group scheme rather than only its reduced identity component.',
    'This crystalline/de Rham comparison is contextual and does not prove the manuscript’s l-adic kernel claim. The external cote54 endpoints are absent here.',
    'agrees','The note explicitly separates its additional comparison from the unfinished theorem.')
add(78,[78],'unpursued implication',[44],'Pro 939–943',
    'mod équivalence algébrique, tensorisé par Q',
    'The letter’s C^i_alg maps onto the rational image A_H^i of the cycle-class map with kernel Griff_H^i(X)_Q. Hyperplane multiplication commutes with these quotient maps, so printed standard-conjecture formulations on A_H differ from the letter’s formulation on C_alg.',
    'The exact quotient sequence is a modern comparison; the rational image is not replaced by its Q_l-span.',
    'agrees','The note preserves the equivalence relation that determines the strength of the claim.')
add(79,[79],'idea of the earlier run',[44],'Pro 939–943',
    'Le premier cas; i=1,n=3',
    'For very general smooth quintic V⊂P4_C, C1_alg(V)=QH while Griff2(V)_Q≠0. The letter’s L:C1_alg→C2_alg has image QH², which intersects Griff2 trivially since ∫H³=5; hence it is not surjective.',
    'This is a verified modern counterexample to the literal algebraic-equivalence formulation, not a counterexample to standard conjecture B on cohomology.',
    'agrees','The note checks dimension, smoothness, algebraically closed base, ample class and rational coefficients.')
add(80,[80],'reading question',[44,45,46],'Pro 939–943; Codex K14-04 4–22',
    'Conjecture A; Conjecture B',
    'In the complete supplied letter, A is Lefschetz on C_alg, A′ is hyperplane pushforward, A″ is affine vanishing, and B is primitive positivity. The later published letters A,B,C,D refer to cohomological algebraic classes, inverse Lefschetz operators, Künneth projectors, and numerical=homological equivalence.',
    'No global dictionary equating every draft letter is asserted; the letter’s B aligns in content with later Hodge-type positivity, not printed B.',
    'understates','K14-04 supplies the continuation absent in the earlier run. Its statements now allow a precise local draft dictionary.', 'corrected')
add(81,[81],'self-flagged step',[44,45,46,47],'Pro 943–945; Codex K14-04 4–33',
    'Modulo vérification que je n’ai pas écrite en détail',
    'The author qualifies reduction to odd-dimensional surjectivity and then to A′. The continuation additionally notes a possible need for nonclosed fields or restriction to homological equivalence.',
    'The reduction is not proved here. The first line of scan45 joins exactly the interrupted Gysin sentence on44; the letter continues through signature on47.',
    'understates','The earlier run’s missing-continuation statement was correct for its package but is superseded by the supplied Codex folder.', 'corrected')
add(82,[82],'unpursued implication',[41,42],'Pro 915–929',
    'a été vérifié pr Mumford; produit de deux courbes elliptiques',
    'The author cites the divisor Tate assertion for powers of a finite-field elliptic curve, reduced to the pair case. Tate1966 explicitly credits Mumford’s deduction from Deuring; later invariant theory proves geometric Tate classes on powers of elliptic curves are generated by divisor classes.',
    'A chosen finite-field model and l≠p make the modern assertion precise; geometric Tate classes mean invariance after a finite field extension.',
    'agrees','The exact Mumford attribution is matched, not merely a broad reference to Tate’s theorem.')
add(83,[83],'unproved claim',[41,42],'Pro 893–929',
    'à priori on a les inclusions; égalité des extrêmes',
    'The text asserts divisor-generated⊆algebraic⊆g-invariant even cohomology, with equality under the stated Tate-divisor and ambiguous representation condition(b). The elliptic-power specialization is identifiable; the general pseudoalgebraic condition is not.',
    'No unproved identification of g-invariants with finite-field geometric Tate classes is made beyond the specified specialization.',
    'agrees','The note preserves the unknown general hypothesis and gives a rigorously scoped later case.')
add(84,[84],'reading question',[41],'Pro 893–915',
    'ε q^(−1/2), ε une racine de l’unité',
    'For E/F5:y²=x³+x+1, #E(F5)=9 and a=−3. If α is a Frobenius eigenvalue, (α/√5+√5/α)²=9/5, so α/√5 is not a root of unity. Inverse eigenvalues have magnitude5^(−1/2) without necessarily being root-of-unity multiples.',
    'The test separates arithmetic/geometric Frobenius, duality, scalar extension and supersingularity. It does not refute the alternative two-eigenspace hypothesis for ordinary elliptic curves.',
    'agrees','The note correctly raises distinct reading/convention alarms; the Tits attribution remains unidentified.')
add(85,[85],'reading question',[44,45,46,47],'Pro 939–943; Codex K14-04 4–33',
    'variété projective lisse connexe; toute variété affine lisse',
    'The supplied continuation generalizes the affine vanishing proposal to all smooth affine varieties and then suggests homological⇒τ equivalence for all smooth varieties. It still gives no singular-variety formulation.',
    'This corrects the package-bounded absence observation while preserving the smooth/singular distinction; external cote16 singular hypersurface work is not supplied here.',
    'understates','Newly available scans45–47 contain a nonprojective smooth extension, though not the singular program sought by the earlier run.', 'corrected')
add(86,[86],'reading question',[4,6,8,10,12,14,16],'Pro 36–51,72–82,113–127,152–173,204–228,258–284,318–347',
    'The Brauer group of a ringed space.',
    'Seven reused English typescript leaves concern local separability, tensor-Hom, commutants and the Brauer group. Their internal order is II.9,III.4–III.7,IV,IV.2, opposite the scan sequence. The title matches B.Auslander’s1966 publication.',
    'A title match establishes a bibliographic candidate, not the identity of the particular draft or authorship by Grothendieck.',
    'agrees','The earlier note’s bibliographic restraint is correct; the mathematical claims are tracked separately as reused text.')
add(87,[87],'reading question',[4,6],'Pro 40,76–82',
    'if L is in C1; L is equivalent to A',
    'The theorem says L∈C1′ iff its Brauer class is trivial; the first proof sentence loses the prime. Over R, H is central simple but is not stably a real matrix algebra, so literal C1 would be false.',
    'C1′ is a mathematical alternative supported by the theorem statement; no ink correction is made.',
    'agrees','The quaternion corner-algebra obstruction verifies the need for the distinction.')
add(88,[88],'unproved claim',[10,12,14],'Pro 154–169,210–228,263–284',
    'we see immediately; Theorem III.1',
    'Reused typescript claims: local separability iff finite presentation with central-separable stalks; End of a finite projective module is separable, and End of a faithful locally finite-projective sheaf is locally separable; tensor products and scalar extensions preserve this property.',
    'These are not authorial motivic assertions. Their missing dependencies are identified rather than assumed read; standard Azumaya/Morita arguments justify the modern versions.',
    'agrees','The note accurately locates the absent earlier theorem/appendix and retains finite presentation and faithfulness where needed.')
add(89,[89],'unproved claim',[8],'Pro 115–127',
    'commutant; Since ... it is finitely presented',
    'For locally separable A-algebras L,M, the canonical map L→Hom_(M^e)(M,L⊗_A M), p↦(q↦p⊗q), identifies L with the commutant of M, and symmetrically for M.',
    'The proof is cut off. Finite presentation comes from local separability, not from finite generation alone over arbitrary rings.',
    'agrees','The note retains the cutoff and does not infer an unrestricted finite-type⇒finite-presentation theorem.')
add(90,[90],'unpursued implication',[4,16],'Pro 47–51,321–347',
    'is an isomorphism for every x; the induced map of sheaves',
    'For finite-projective modules, End(M)⊗End(N)≅End(M⊗N). For a faithful finite-projective generator M1, Morita evaluation Hom_End(M1)(M1,M2)⊗M1→M2 is an isomorphism, with sheaf versions checked locally.',
    'The standard maps are explicitly reconstructed; the truncated typed proofs and absent hypotheses from prior pages are not claimed complete.',
    'agrees','The note gives exact operations without identifying these reused leaves as a construction of motives.')
add(91,[91],'reading question',[20,22],'Pro 405–419,478–495',
    'n°391; s′(x)=s(x)+2t',
    'The two reused French leaves join scan22→scan20, internally pages−14−→−15−. The note’s external cote54 page−13− allegedly already has later propositions; that unavailable endpoint does not establish a consecutive three-leaf sequence.',
    'Only the local join is verified here; version/pagination relation to the absent external page remains unverified.',
    'agrees','The note correctly distinguishes subject/number agreement from exact consecutive-leaf provenance.')
add(92,[92],'idea of the earlier run',[20,22],'Pro 407–409,491–495',
    's′s est la translation 2t',
    'For parallel nonisotropic affine hyperplanes H,H′ in a nondegenerate quadratic space over a field of characteristic≠2, write H′=H+t with t normal. Orthogonal reflections compose s′∘s(x)=x+2t; over R with positive form, ||t|| is their distance.',
    'The elementary coordinate calculation completes the printed proof and is not a new result of Grothendieck.',
    'agrees','The note checks composition order and retains the nonisotropic hypothesis.')
add(93,[93],'other',[20,22,3,5,7,9,11,13,15,24,26,27,28,29,30,31,32,33,35,36,37,38,39,41,42,44],'Pro 417–419 and the individually cited lines of SA06-7–85',
    'C=∩D_H(C)',
    'The reused chamber lemma says a locally finite union of affine real hyperplanes is closed and nowhere dense and each chamber is the intersection of its chosen open half-spaces. A segment from one chamber point proves the missing reverse inclusion. The remainder of this omnibus ### entry is a secondary standing-step/title index, cross-referencing all already adjudicated effectivity, Albanese and Tate items.',
    'The segment proof is the earlier run’s completion. Its appended counts86/24/155 refer to absent prior audit registers and are not accepted as new source claims; the present census is recomputed independently.',
    'agrees','The lemma and each standing-table occurrence were checked against the source. The appended index adds no distinct verdict rows or proof to the referenced gaps.')
add(95,[95],'title, date or page count',[17,24,31,38],'Pro 351,500–506,652,830',
    'Équivalence d’Albanese et de Picard des cycles algébriques',
    'The title sheet names Albanese/Picard equivalence; the inner title names Théorie de l’équivalence d’Albanese des cycles, with sections on the quotient ring, families and the l-adic homomorphism. No total page count is written.',
    'Codex reads the margin “Consulter Weil, Critères d’Équivalence”, whereas Pro suggests “Conjectures Weil”; the potentially bibliographic rather than title function needs ink review.',
    'agrees','Titles and local sections are supported; the discrepant margin is not promoted to an authorial title.')
add(96,[96],'title, date or page count',[2,40,44,45,46,47],'Pro 7,883–889,935–947; Codex K14-04 3,17,25,30–33',
    'Astuce de Tate; 27.8.65; Mon Cher Serre',
    'Forty retained Pro scans correspond to2–44 excluding18,23,43. The Pro mspage values equal scan−1; Codex identifies these as archival foliation, so they are not securely authorial pagination. The dated Serre letter comprises scans44–47, with typed continuation leaves2–4 and signature.',
    'The letter join is directly read. Archival-versus-authorial status of the lower-corner marks cannot be settled without scans.',
    'understates','The numeric census is correct, but the earlier statement “only first letter page supplied” is superseded and page marks must not be assumed authorial.', 'corrected')
add(97,[97],'title, date or page count',[4,6,8,10,12,14,16,20,22],'Pro 36,72,113,152,204,258,318,405,478',
    'IV. The Brauer group of a ringed space.; n°391',
    'The English and French reused-text headings/pagination are as in SA06-86 and91. This final omnibus entry also contains the earlier register-delta table and bibliography: these are editorial leads, not additional authorial results; all references used in this consolidation have separate verification records.',
    'Unavailable project-register statuses and the claimed prior scan audit are not reproduced as checks by the present run. Exact primary references actually used are checked independently.',
    'agrees','Both title families were read; all appended material was inspected and its evidentiary status is kept separate.')

# Codex-only source items: no artificial NOTES_INDEX verdict rows.
add(98,[],'conjecture',[45,46,47],'Codex K14-04 4–33',
    "Conjecture A′; Conjecture A″; Conjecture B",
    'The remaining letter states weak hyperplane pushforward A′, affine vanishing A″, and primitive positivity B for the same rational algebraic-equivalence classes. It states implications for Künneth classes, integrality, finite-dimensionality, semisimplicity and intermediate Jacobians, explicitly retracting an earlier equivalence of A with Künneth.',
    'These are newly recovered within this consolidation from Codex-only pages. τ is interpreted only in light of the letter’s initial definition; each conditional implication is separately recorded in the claims map.',
    'agrees','Scans45–47 form a continuous signed letter with44; conjectures, qualified implications and one explicit correction remain distinct.')
add(99,[],'unproved claim',[49,50,51],'Codex K14-04 40–99',
    'il y a env.4=2×2 cas à distinguer',
    'The Sorites survey describes the four Picard/Albanese source-target types of correspondence-induced homomorphisms, rational realization of abelian homomorphisms by cycles, and algebraicity of inverses when the realization is an isomorphism. It queries denominators in CasesI–II and states they enter CaseIV.',
    'Picard means the reduced connected Picard variety in these statements; integral assertions are not inferred from rational inverses.',
    'agrees','The field is explicitly algebraically closed here, unlike the earlier local definition; the survey announces details developed in following sheets.')
add(100,[],'unproved claim',[52,53,54,55,56,57],'Codex K14-04 104–206',
    'u_Z ne dépend que de classe d’équiv. numérique de Z',
    'For smooth projective connected X^n,Y^m over algebraically closed k and a codimension-n correspondence Z on X×Y, there is a unique Alb(Y)→Alb(X) compatible with degree-zero cycles; it depends only on the numerical class. A Poincaré-divisor construction is given, with intersection Lemma1.5 omitted.',
    'The proof’s map targets Pic0(B), where B=Pic0_red(X); the isolated Pic0(A_X) in Lemma1.4 is a type alarm. Numerical-class dependence concerns the induced abelian map, not arbitrary cohomological actions.',
    'agrees','Uniqueness and the construction are sketched; the missing moving details and reference request are preserved.')
add(101,[],'unproved claim',[56,57],'Codex K14-04 190–206',
    'on vérifie sans difficulté; indépendant du nb premier l',
    'Theorem1.6 states commutativity of the l-adic H1 correspondence action with the Albanese realization. For abelian X,Y, Cor1.7 identifies actions induced by integral codimension-dimX correspondences with pullbacks by unique abelian homomorphisms Y→X, independent of l.',
    'Assume l invertible in k and the usual H1 comparison. “Isomorphisms modulo finite groups” does not justify silently replacing integral lattices by rational spaces.',
    'agrees','The source gives a proof outline through the preceding construction, not a complete cohomological diagram verification.')
add(102,[],'unpursued implication',[57,58],'Codex K14-04 208–211',
    'Généralisation de1.1; base quelconque S',
    'The author proposes a relative version for smooth projective geometrically connected fibers using a codimension-n class in the associated graded K-theory and existing Albanese schemes, or a morphism to a para-abelian torsor.',
    'Existence assumptions on relative Albanese/Picard objects and compatibility with base change must be stated; no unrestricted representability over arbitrary S is supplied.',
    'agrees','The conditional wording “si ... existent” is essential and remains visible.')
add(103,[],'unproved claim',[58],'Codex K14-04 213–226',
    'échanger le rôle de X et Y ?',
    'A one-cycle Z on smooth projective X×Y induces a map Pic0_red(X)→Alb(Y), by sending an algebraically trivial divisor D to Alb_Y(pr2*((D×Y)·Z)) when defined.',
    'The factor order is verified by dimension; the author’s marginal question and the cutoff after “Cet homomorphisme” remain.',
    'agrees','This is a correspondence-level construction beginning here and continuing in the next Codex folder; no claim of a complete local proof is made.')

for name,content in [('items.json',items)]:
    (OUT/name).write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n')
with (OUT/'entries.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
assert len(entries)==97 and len({x['entry_id'] for x in entries})==97
with (OUT/'progress.log').open('a') as f:f.write(datetime.now(timezone.utc).isoformat()+'\tSTAGE1\t97 individually read entry verdicts; 101 items including6 Codex-only items; two intra-package merges.\n')
print(json.dumps({'entries':len(entries),'items':len(items),'note_entries_complete':True,'method':'individual manual judgments after full passage reads'},indent=2))
