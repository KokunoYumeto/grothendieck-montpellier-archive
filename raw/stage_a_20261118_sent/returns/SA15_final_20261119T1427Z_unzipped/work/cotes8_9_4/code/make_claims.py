"""Manually authored claim map, following complete reading and targeted searches."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
items={int(x['id'][-3:]):x for x in json.loads((W/'items.json').read_text())}
claims=[];families={}
def c(n,ii,scans,lines,his,statement,status,cl,fate,refs=(),comp='',confidence='high',family='',date='First circulation/publication not established for this exact formulation.'):
    if isinstance(ii,int):ii=[ii]
    claims.append(dict(id=f'P894-C{n:03d}',items=[f'P894-I{i:03d}' for i in ii],cote=items[ii[0]]['cote'],scans=scans,lines=lines,his_statement=his,statement=statement,status_on_pages=status,computation=comp or 'No numerical computation. Source and proof-scope check recorded in check_events.tsv.',**{'class':cl},fate=fate,fate_date=date,present_status='As of November 2026: '+fate,refs=list(refs),confidence=confidence))
    families[f'P894-C{n:03d}']=family

c(1,1,[79],['3–25'],'Derived expression through f and Λ; final L is unnecessary when Λ is a field.',
 'For a multiplicative-type G/S with locally constant character sheaf M, ℓ_G≃M⊗ᴸ_ZO_S. If M descends from M₀ on Bπ and Λ→O_S, then ℓ_G≃f*(M₀⊗ᴸ_ZΛ)⊗ᴸ_ΛO_S; tensoring with O_S is underived when Λ is a field. Finitely generated characters admit a finite locally free character resolution; arbitrary characters require the limit justification omitted here.',
 'stated without proof; continuation of cote8:78','B','Bergh–Rydh, AppendixB, PropositionB.4 proves the formula; its proof explicitly permits arbitrary locally constant character sheaves. The infinite-torus step of the manuscript remains a proof-presentation issue, not a counterexample to the formula.',['BerghRydh2019'],family='F01',date='Verified author version2May2019; no priority claim.')
c(2,2,[80],['29–46'],'ω_G=M⊗O_S; n_G=Tor¹(M,O_S).',
 'H⁰ℓ_G=M⊗_ZO_S and H⁻¹ℓ_G=Tor¹_Z(M,O_S). In characteristic p these are (M/pM)⊗FpO_S and M[p]⊗FpO_S, respectively. The identifications are equivariant; an isomorphism between the two is not automatic for mixed elementary divisors.',
 'stated without proof','B','Established as the cohomology of the two-term character resolution; the locally free Z/n case has matching modules.',['BerghRydh2019'],comp='Independent two-term resolution check in check_calculations.py.',family='F01')
c(3,2,[80],['47–64'],'Classe canonique ξ∈H²(S,End(E)).',
 'If Λ=Z/n and M is a locally free finite Λ-module sheaf, both cohomology sheaves are E=M⊗ΛO_S and the co-Lie Postnikov class is in Ext²_O(E,E)=H²(S,End E). It is the image of the corresponding class over Λ. No O_S-flatness over Λ is needed: the cohomology modules of the defining two-extension are locally free.',
 'stated without proof; flatness hypothesis canceled','B','The derived/Postnikov construction is standard obstruction theory; the deleted flatness hypothesis is unnecessary under the displayed local-freeness assumptions.',['Illusie1972'],family='F01')
c(4,4,[81],['70–76'],'L’obstruction est celle de relever M₀ mod p² (attribuée à Illusie).',
 'For ρ:π→GL_d(Fp), the obstruction to lifting ρ to GL_d(Z/p²) is the extension class in H²(π,EndFp M₀), with conjugation action. Pullback to the base topos gives the corresponding ξ. For the universal ρ the class vanishes exactly when reduction GL_d(Z/p²)→GL_d(Fp) splits.',
 'stated without proof','B','This is the ordinary extension-class lifting obstruction. Illusie supplies the cotangent deformation framework; Singla records the splitting classification.',['Illusie1972','Singla2010'],family='F01')
c(5,4,[81],['76–78'],'ξ nulle pour d≤1.',
 'For rank0 the obstruction is zero. For rank1 every Fp-valued character lifts through the multiplicative Teichmüller section Fp*→(Z/p²)*, including the trivial p=2 case.',
 'stated without proof','E','The claim is correct by the explicit multiplicative section; no later novelty is assigned.',['Singla2010'],family='F01')
c(6,4,[81],['76–78'],'Sans doute pas nulle pour d≥2.',
 'The universal rank-d obstruction is expected nonzero for every d≥2 and every prime p. This is false for (d,p)=(2,2): the integral S3 representation in proofs.md gives a splitting. The recorded complete exceptional list is (2,2),(2,3),(3,2), in addition to rank1.',
 'open on the pages; false as stated','B','Singla introductionp3 attributes the exact exceptional classification to Sah1977 and Ginosar2001. Original Sah proof was not opened; the (2,2) refutation is independent and exhaustive.',['Singla2010','Ginosar2001'],comp='check_calculations.py: six-matrix S3 subgroup and all36 multiplication checks modulo4.',family='F01',date='Sah1977 and Ginosar2001 attribution checked through SinglaJanuary2010; independent certificate19Nov2026.')
c(7,5,[81],['79–83'],'H²(Bπ,M)→H²(S,M) injectif pour tout M.',
 'For a connected topos with the indicated universal cover, π its fundamental group and M a locally constant π-module, the comparison H²(π,M)→H²(S,M) is injective when H¹ of the universal cover with the pulled-back coefficients vanishes. The assertion is not justified for arbitrary non-locally-constant sheaves.',
 'stated without proof','E','The low-degree Cartan–Leray sequence gives the precise sufficient condition. Searches did not verify the unrestricted reading “tout M” beyond locally constant coefficients.',[],family='F01',confidence='medium')
c(8,7,[3],['128–159'],'Hodge exact sequence and perfect duality for M(G).',
 'For a p-divisible G over a perfect characteristic-p field, fix the contravariant convention. Its mod-p Dieudonné module has dimension ht(G), the Hodge submodule and quotient are invariant differentials and the tangent space of the Cartier dual, and the perfect dual pairing exchanges F and V with Frobenius twists.',
 'stated without proof','B','Oda gives the established Dieudonné/Hodge and duality framework (Theorem3.19, Corollary5.11 for abelian varieties).',['Oda1969','BerthelotMessing1979'],family='F02',date='Oda dissertationJune1967; article1969. Crystalline formulation Rennes1978/published1979.')
c(9,7,[3],['133–151'],'Im F=Ker V; Im V=Ker F.',
 'The reduction of a free Dieudonné module of a p-divisible group over a perfect field is a BT1 module: FV=VF=0 and Im F=Ker V, Im V=Ker F. These equalities need the BT hypothesis; they do not hold for every arbitrary module over the ring with FV=p.',
 'stated without proof','B','This is the BT1 structure in the opened Dieudonné sources.',['Oda1969','BerthelotMessing1979'],family='F02')
c(10,7,[3],['160–176'],'Purement infinitésimal; G [or G*] sans tore.',
 'In the contravariant convention connected G has nilpotent reduced F, and connected Cartier dual G* has nilpotent reduced V. Pro’s G sans tore and Codex’s G* sans tore cannot both express the same equivalence; μ_p∞ distinguishes them.',
 'stated without proof; reading discrepancy','B','The structural criterion is established. The disputed star remains an ink question; no transcription is amended.',['Oda1969'],comp='Direct μ_p∞/Qp/Zp convention check; no numerical computation.',family='F02')
c(11,7,[3],['151–159;169–176'],'The p-operation and a proposed H^(2|1)(G,Ga) identification.',
 'The page identifies the p-th power on invariant derivations with an operation induced by F or V and ends with an ambiguous cohomological degree. Twists and the superscript cannot be fixed from the two textual witnesses alone.',
 'stated without proof; not identifiable in full','F','Searches recover the standard restricted-Lie/Dieudonné relationship, but not a unique theorem matching the literal uncertain formula.',['Oda1969','BerthelotMessing1979'],family='F02',confidence='low')
c(12,8,[5],['196–242'],'Coefficient-of1 map and pairing.',
 'With k=Fp and A_n=Z_p[F,V]/(FV−p,F^(n+1),V^(n+1)), coefficient-of1 defines a nondegenerate pairing A_n×A_n→Z/p^(n+1). For general perfect k the two W-actions and Frobenius twisting must be distinguished. A target W_n interpreted as length n conflicts with the displayed truncation powers.',
 'computation; convention not fixed','C','The finite test supports the corrected index convention. Standard Dieudonné duality survives; the exact finite-ring formula depends on the unresolved notation.',['Oda1969'],comp='check_calculations.py: exhaustive perfect-pairing checks for (p,n)=(2,1),(3,1),(2,2), with wrong-target radical.',family='F02',confidence='medium')
c(13,8,[7],['303–335'],'A_n identified with its coefficient dual; direct-limit claim.',
 'The proposed finite dualizing-bimodule isomorphism and its direct limit are only conditionally meaningful after fixing the W_n truncation, left/right W-actions and transition maps. Codex marks the finite isomorphism canceled; Pro does not.',
 'self-flagged; cancellation status differs between witnesses','F','No exact unique formulation can be certified. Published Dieudonné duality does not decide whether this particular canceled presentation is the intended one.',['Oda1969','BerthelotMessing1979'],family='F02',confidence='low')
c(14,8,[8],['336–365'],'u·V=π(u∘F) at the top; later V_g formula.',
 'If the displayed dual F and dual V both use precomposition by F, the operators need not satisfy FV=p. Over Fp take F=J3,V=0; the alleged dual has F′V′=(J3ᵗ)²≠0. The later precomposition-by-V expression is a mathematically consistent alternative, with the appropriate semilinear twist.',
 'false as literally transcribed; possible misreading','F','The general duality is established, but ink must decide the isolated F/V.',['Oda1969'],comp='check_calculations.py: exact3×3 nilpotent counterexample.',family='F02')
c(15,8,[8],['365–392'],'Dual module and adjointness identities.',
 'For a finite free W(k) Dieudonné module, the dual module has F and V adjoint to V and F respectively, with σ/σ⁻¹ twists; after inverting p this is the usual dual isocrystal. The two coefficient actions on the ring-valued model must be kept separate.',
 'proof sketched; explicit warning','B','Verified in the standard Cartier/Dieudonné duality framework; no identification of the ambiguous finite bimodule is needed.',['Oda1969','BerthelotMessing1979'],family='F02')
c(16,9,[9],['393–425'],'Canceled torsor/chain-homotopy lemma for constructing Gauss–Manin.',
 'A canceled draft seeks descent of torsor-indexed chain maps when pairwise differences are null-homotopic. An actual descent theorem requires compatible higher data or a specific enhanced construction; the fragment does not specify it.',
 'withdrawn in the same text','F','The later Katz–Oda direct construction answers the general Gauss–Manin goal, not the exact erased descent lemma.',['IllusiePisa2015'],family='F03',confidence='medium',date='Katz–Oda1968 is recorded in the opened historical source; this draft’s exact fate not identified.')
c(17,10,[11],['430–441'],'Unicité par le théorème de Tate, mixed characteristic inserted.',
 'For a complete DVR of mixed characteristic(0,p) with perfect residue field, generic fiber is fully faithful on p-divisible groups over the DVR. Thus an integral model, if it exists, is unique up to the unique extension of its generic-fiber identification.',
 'invoked without proof','B','Illusie§2.3 states Tate’s theorem with this scope and records deJong’s equal-characteristic extension.',['IllusiePisa2015'],family='F04',date='Tate1970 publication cited by Illusie; deJong1998 for equal characteristic.')
c(18,10,[11],['432–441'],'K₀ class from a filtration with potentially good factors.',
 'For a generic p-divisible group with a finite filtration whose factors extend after a finite Galois extension, form the sum of their equivariant model classes in the appropriate Grothendieck group. Independence of the filtration needs an exact-category comparison; uniqueness of models alone is insufficient.',
 'stated without proof','C','The necessary full-faithfulness theorem is established; no opened source was found proving this exact equivariantK₀ construction with the manuscript’s unspecified category.',['IllusiePisa2015'],family='F04',confidence='medium')
c(19,11,[12],['442–458'],'Inertia-linear trace with residual coefficient action.',
 'For an equivariant good model over O_L, the special-fiber Dieudonné module is semilinear for Gal(L/K), but linear over W(k_L) for inertia. Its inertia trace is central and residual-Galois equivariant, where the quotient acts on both coefficients and conjugacy classes.',
 'stated without proof','B','The trace and semilinearity follow directly from the indicated action; modern finite potentially-good inertia is compatible with this construction.',['DembeleFreitasVoight2025'],family='F04')
c(20,11,[12],['458–472'],'Independence of the good-reduction extension.',
 'After scalar extension and passage to compatible inertia quotients, traces of a genuinely potentially-good p-divisible group are independent of enlargement of the good-reduction field. For the manuscript’s virtual class from potentially good factors this also needs the filtration independence inC018.',
 'stated without proof','C','Base-change compatibility is formal for a fixed good object; the more general virtual construction remains unverified at its exact stated scope.',['IllusiePisa2015','DembeleFreitasVoight2025'],family='F04',confidence='medium')
c(21,12,[13],['473–476'],'Potentially constant case and Brauer character.',
 'For a p-divisible group that becomes constant over a finite extension, the trace of a p-regular finite inertia action is recovered from the Brauer character of its mod-p representation, using Teichmüller lifts of eigenvalues. This uses an actual finite integral representation.',
 'stated without proof','E','Correct by the elementary p-regular Brauer-character construction. The finite-action hypothesis cannot be removed.',['DembeleFreitasVoight2025'],family='F04')
c(22,12,[13],['475–477'],'N’est pas vrai en général; multiplicative counterexample.',
 'The unrestricted comparison of special-fiber inertia trace with the Brauer character of generic mod-p torsion is false. For μ_p∞ over Qp, p>2, the former is trivial while the mod-p cyclotomic character is nontrivial on tame inertia.',
 'corrected by himself on the same page; false as stated','E','The author’s counterexample is valid and independently checked. It refutes equality with a Brauer character; it does not alone give two groups with the same mod-p module.',[],family='F04',comp='Direct cyclotomic-versus-good-model check in proofs.md; no numerical enumeration.')
c(23,13,[13,14],['477–487'],'Cas test with μp⊂K; constant p-torsion and marginal faux par Tate.',
 'Even with μp⊂K, two potentially-good elliptic curves with isomorphic mod-p Galois modules need not have the same p-regular potentially-good inertia character. Over K=F(5^(1/8)), F/Q5 unramified degree4, y²=x³+5⁴ and y²=x³−x both have constant5-torsion; finite inertia traces are−1 and2 on an order3 element.',
 'open on the pages with an ambiguously attached marginal denial; false as stated','C','Independent exact counterexample supplied in this run; searches found the general inertial-type classification but no verified identification of Tate’s historical example. The first curve has supersingular potential reduction.',['DembeleFreitasVoight2025'],comp='proofs.md§1; check_elliptic_inertia_counterexample.py and its complete JSON certificate.',family='F04',date='Independent counterexample checked19Nov2026; historical first refutation not located.')
c(24,13,[14],['481–487'],'Aut(E) cyclic of order2,4,6, if p≠2,3.',
 'For an elliptic curve over an algebraically closed field of characteristic≠2,3, origin-preserving automorphisms have order2,4,or6. A finite potentially-good inertia image embeds in this group and may have any subgroup order, including1 and3.',
 'stated without proof','E','The classical automorphism classification is consistent with the modern elliptic inertial-type list. Reading these as the only possible inertia orders would be wrong.',['DembeleFreitasVoight2025'],family='F04')
c(25,13,[14],['481–487'],'Trace equal to n=dimA; elliptic value2.',
 'For a g-dimensional abelian variety, the full Dieudonné/isocrystal or ℓ≠p Tate realization has rank2g. Its identity trace is2g, notg. The displayed n=dimA is inconsistent with the subsequent elliptic trace2 if n denotes the full realization.',
 'false as literally transcribed; reading question','F','Rank normalization is elementary; ink must decide whether a factor2 or a different n was intended.',[],family='F04')
c(26,14,[16],['499–517'],'Compatible stratification implies A₀ ordinary, sans doute.',
 'The author seeks a functorial full k-stratification of H¹_dR on every infinitesimal deformation of A₀, compatible with base change,F,V, and suggests that this forces A₀ ordinary. Universal-deformation quantifiers are essential: a constant nonordinary family alone is not a counterexample to that universal statement.',
 'open on the pages','C','Ordinary Serre–Tate coordinates and Gauss–Manin formulas are established, but no exact necessity theorem for this under-specified full-stratification condition was located.',['Katz1981','IllusiePisa2015'],family='F05',confidence='medium')
c(27,15,[16],['518–525'],'Ordinary Hodge splitting by ImF.',
 'For an ordinary abelian scheme in characteristicp, H¹_dR is the direct sum of its Hodge subbundle and the unit/conjugate subbundle ImF, interpreted via the relative Frobenius pullback.',
 'proof sketched','B','The ordinary decomposition is standard; the relative twists are essential.',['Katz1981','Oda1969'],family='F05')
c(28,15,[17,18],['526–563'],'Equality after F pullback; warning and smooth universal deformation remedy.',
 'Equality of subbundles after arbitrary Frobenius pullback need not descend. It does descend after faithfully flat Frobenius on the smooth universal deformation space, and the resulting equality specializes to any deformation classified by that space.',
 'corrected by himself later: warning17, remedy18','B','The warning is valid. The deformation space is formally smooth; the descent step is repaired by faithful flatness, under the required perfect-base hypotheses.',['IllusiePisa2015'],comp='proofs.md§3, dual-number line counterexample.',family='F05')
c(29,16,[18],['545–563'],'Canonical stratifications and discrete GL_g.',
 'A finite locally free module E with unit relative Frobenius F*E≃E is locally the scalar extension of a finite Fp-local system. This gives a full stratification. For the ordinary Hodge pieces this structure preserves Hodge; it is not thereby the Gauss–Manin connection.',
 'stated without proof; à préciser','B','The finite-unit-F correspondence gives the required construction. The structure group is constantGL_g(Fp), not algebraicGL_g,k.',['KatzSGA7XXII','Katz1981'],family='F05')
c(30,16,[19],['564–589'],'Radicial followed by étale; relative p-torsion.',
 'For an ordinary abelian scheme, the relative p-power map factors through the multiplicative connected factor and the finite étale quotient. Relative étale sheaves, not only their sections over k, recover the unit-F tangent data.',
 'stated without proof','B','Established ordinary connected–étale structure.',['Katz1981','Caraiani2017'],family='F05')
c(31,17,[19],['589–604'],'Formula using A[p](k) over a perfect k.',
 'The literal formula identifying a rank-g unit-F tangent module with k⊗FpA[p](k) or its dual is false for every perfect k. For E/F5:y²=x³−x, E is ordinary but E[5](F5)=0. Use geometric points plus Galois descent or a sheaf formulation.',
 'false as literally transcribed','F','A finite-field counterexample settles the literal reading; the correct sheaf theorem remains valid.',['Caraiani2017'],comp='check_calculations.py: eight points and Hasse coefficient3.',family='F05')
c(32,18,[20],['605–640'],'Polarization class lies in the middle summand.',
 'For an ordinary abelian scheme, a Néron–Severi class maps under deRham c1 to the Hodge×conjugate middle term; through cup-product duality this yields the tangent map A→A* induced by the associated homomorphism. The page also asserts compatibility with the transpose étale p-torsion map.',
 'stated without proof; initial opposite arrow canceled','B','The Chern-class/Dieudonné compatibility belongs to established duality. Exact signs require the manuscript’s altered variance convention.',['Oda1969','BerthelotMessing1979'],family='F06',confidence='medium')
c(33,19,[21,22],['641–674'],'Global Hasse section; ordinary iff nonzero.',
 'For an abelian scheme A/S in characteristicp, det of t_A^(p)→t_A is Ha_A∈Γ(S,ω_A^(p−1)), where ω_A=det(t_A)^∨. Its nonvanishing locus is exactly the ordinary locus. This makes no assertion about multiplicities of its divisor.',
 'construction with proof sketch','B','The exact determinant and invertibility criterion appear in Caraiani§4.1, Lemma4.1.7.',['Caraiani2017'],family='F06',date='Verified2017 lecture notes; no novelty or earliest-date claim.')
c(34,20,[22],['663–688'],'Canonical ω_A≃ω_A* compatible with Hasse and étale determinant.',
 'Hodge determinants and the top deRham trace give an isomorphism ω_A≃ω_A*. The text additionally claims compatibility with the ordinary unit-F structures and their Hasse invariants; this is a determinant-line statement, not a rank-g module isomorphism.',
 'construction given; compatibility stated without proof','C','Standard duality supplies the construction, but the exact unpolarized normalization and its compatibility with the later positive Tate determinant were not located as a named published result.',['Oda1969','Katz1981'],family='F06',confidence='medium')
c(35,21,[23],['689–713'],'Cartier duality and perfect-field splitting.',
 'For an ordinary p-divisible group over a perfect field, the connected–étale sequence splits canonically, and Cartier duality exchanges its multiplicative and étale factors. This does not choose a splitting over every nonperfect or infinitesimal base.',
 'stated without proof','B','Established ordinary structure; the relative extension is addressed separately inC036.',['Katz1981','Oda1969'],family='F05')
c(36,21,[23],['697–713'],'Expliciter la structure d’extension in general.',
 'For an ordinary abelian variety A over algebraically closed k of characteristicp and an artinian local deformation ring R with residuek, deformation classes are parametrized by bilinear maps T_pA_et×T_pA*_et→1+m_R; the associated extension of the étale by multiplicative p-divisible factors is the missing datum.',
 'open on the pages','B','Katz, Theorem2.1, supplies the exact ordinary formal deformation parameters. This is a deformation-neighborhood answer, not an assertion that every global base has such coordinates.',['Katz1981'],family='F05',date='Serre–Tate result earlier than1981; Katz’s published formulation1981. Grothendieck letter6.7 is discussed by Illusie2015.')
c(37,22,[24,25,27,28],['731–742;765–793;830–864'],'α_p(λ)=detT_p(λ)_et/√degλ; independence and integrality.',
 'For an ordinary abelian variety over a perfect field, dividing the étale determinant of a polarization λ by the positive rational integer√degλ gives a polarization-independent isomorphism of the integral rank-one Zp determinant lattices of A and A*. Base change and isomorphisms are respected, with the dual variance specified inC041.',
 'proof sketched; completed locally on scans27–28','C','The manuscript supplies a viable Rosati-positive and Cartier-kernel proof. Searches of determinant, polarization, Tate, bibliographic and author sources did not locate this exact normalization as a named theorem; no claim of undeveloped mathematics follows.',['Milne2008','Katz1981'],comp='Proof audit in proofs.md; sign and lattice subclaimsC039–C040; numerical normalization examples in check_calculations.py.',family='F06',confidence='medium')
c(38,23,[24,26,27],['745–761;798–826;831'],'Every endomorphism has square degree and positive square-root determinant.',
 'The discarded universal assertion is false: ordinary elliptic Frobenius has degreep, while−1 has degree1 and rank-one étale determinant−1. The canceled Zp[T]∩Q[T]=Z[T] claim also fails, for example1/2∈Z3∩Q.',
 'withdrawn in the same text; false as stated','E','Elementary counterexamples confirm the author’s withdrawal. They do not refute the later positive Rosati-symmetric restriction.',[],comp='check_calculations.py: degree, sign, and rational-integral counterchecks.',family='F06')
c(39,22,[25,27],['765–793;831–836'],'The positive-Hermitian sign; cqfd.',
 'On the rational Rosati-self-adjoint subspace, the étale determinant Δ is a Q-polynomial: values at the integral lattice are integers because Δ²=deg and degree of a symmetric homomorphism is a square. Interpolation gives rational coefficients. After extension to R, a positive self-adjoint u has a self-adjoint square root w, so Δ(u)=Δ(w)²>0. This chooses the positive sign in polarization independence.',
 'proved there modulo standard Rosati/degree facts','E','The standard Rosati positivity and degree facts validate the live argument. The previous sign doubt is resolved on the pages.',['Milne2008'],comp='Independent polynomial-interpolation and real-square-root proof audit; canceled integral-coefficient assertion separately refuted.',family='F06',confidence='medium')
c(40,22,[27,28],['838–864'],'Integral determinant lattice from self-dual kernel.',
 'For a polarization of an ordinary abelian variety, the p-primary kernel is Cartier self-dual; its étale and multiplicative parts have equal lengths. Hence the p-adic valuation of the étale determinant equals half v_p(degλ), so the normalized determinant is an isomorphism of Zp lattices.',
 'proof sketched','B','The argument follows from ordinary Cartier duality and is correct; it concerns length, not a chosen isomorphism of kernel factors.',['Katz1981','Milne2008'],comp='check_calculations.py checks the length/valuation identity on explicit elementary-divisor examples.',family='F06')
c(41,24,[28,29],['866–900'],'Mauvaise variance; use u*⁻¹.',
 'For an ordinary abelian variety, detT_p(u)_et·detT_p(u*)_et=deg(u) for an isogeny u. For an automorphism this equals1, so the determinant comparison intertwines u with u*⁻¹, not u*. The individual determinants need not be equal.',
 'corrected by himself later','B','The identity is the étale/multiplicative factorization of the total degree determinant. The corrected contragredient variance is necessary.',['Milne2008','Oda1969'],family='F06')
c(42,25,[29],['901–909'],'Biduality sign à vérifier.',
 'Determine the sign of α_(A*)∘α_A after the canonical A≃A** identification and the manuscript’s alternating-form convention. The page explicitly leaves this check open.',
 'open on the pages','C','Standard biduality exists, but searches did not identify the exact sign for this convention. It must not be filled from an unspecified convention.',['Milne2008','Oda1969'],family='F06',confidence='medium')
c(43,25,[29],['901–909'],'Compatibility with direct sums.',
 'Under the ordered exterior-product identification of determinant lines, ask whether α_(A×B)=α_A⊗α_B. Product polarizations reduce this to multiplicativity of positive square-root degree, with the chosen order of determinant factors.',
 'open on the pages','C','The determinant-level identity follows formally under that explicit order; no separate exact published locator was found for the manuscript normalization.',['Milne2008'],family='F06')
c(44,25,[29],['901–909'],'Reduction modp and earlier deRham comparison.',
 'Ask whether reduction of α_A agrees with the determinant comparison inC034. The literal final formula lacking det would identify full rank-g modules and does not follow. At determinant rank1 the normalization comparison remains a genuine check.',
 'open on the pages; literal rank mismatch','C','Existing duality is relevant but no exact normalization comparison was found. The missing determinant signs require the scans.',['Oda1969','Katz1981'],family='F06',confidence='medium')
c(45,26,[2],['938–968'],'F-nilpotence above the middle.',
 'Under the auxiliary sheet’s crystalline F,V setup for smooth proper n-dimensional X, the reduced free part and indicated p-torsion in degreei>n have nilpotent F. The clean stable statement is (H^i_cris/p)_st=H^(i+1)_cris[p]_st=0 for i>n, by stable augmentation and H^i(O_X)=0.',
 'stated without proof','B','The stable vanishing follows from derived base change and the augmentation theorem in KatzSGA7XXII(3.3.4).',['KatzSGA7XXII','Illusie1976'],family='F07')
c(46,26,[2],['938–968'],'V-nilpotence below the middle.',
 'The dual low-degree V-nilpotence statement follows by crystalline Poincaré duality only with its dimension twist and the adjacent torsion degree. F- and V-stable superscript/subscript conventions must be kept distinct; the literal auxiliary degree labels remain reading questions.',
 'stated without proof','C','Duality is established, but the exact terse F/V-indexed auxiliary formula cannot be fixed without the uncertain symbols.',['Illusie1976','BerthelotMessing1979'],family='F07',confidence='medium')
c(47,26,[2],['938–968'],'Middle-degree exact sequences.',
 'The middle F-sequence is the stable universal-coefficient sequence relating (H^n_cris/p)_st,H^n(O_X)_st and H^(n+1)_cris[p]_st, with the free/torsion splitting made explicit. The paired V-sequence is expected to be its shifted dual.',
 'stated without proof','C','The F-sequence has a standard derivation. The exact V-indexed transcription and transpose convention remain only partly identifiable.',['KatzSGA7XXII','Illusie1976'],family='F07',confidence='medium')
c(48,26,[2,3],['938–1019'],'Les deux suites sont sans doute transposées.',
 'The author expects the two middle F/V sequences to transpose under crystalline duality. Derived duality exchanges the relevant kernels and cokernels with a torsion degree shift; a naïve same-degree vector-space transpose is insufficient.',
 'open on the pages','C','The modern duality formalism supplies the method, but no exact printed statement matching these uncertain auxiliary formulas was verified.',['Illusie1976'],family='F07',confidence='medium')
c(49,27,[3],['969–997'],'Universal coefficients and deRham reduction.',
 'For X smooth proper over perfect k, derived reduction RΓ_cris(X/W)⊗ᴸ_Wk≃RΓ_dR(X/k) gives0→H^i_cris/p→H^i_dR→H^(i+1)_cris[p]→0 for everyi. The modern theorem includes p=2; the manuscript’s p≠2 attribution is uncertain.',
 'invoked without proof','B','Established crystalline base change; the shifted torsion is indispensable.',['Illusie1976','BMS2016'],family='F07',date='Berthelot thesis1974 summarized in lectureNov1974/published1976; modern integral comparison2016preprint/2018publication.')
c(50,27,[3],['989–1019'],'Snake-lemma comparison for X and Y.',
 'Apply the snake lemma to the two universal-coefficient sequences and restriction maps. Without suppressing the adjacent torsion cokernel or importing a canceled Gysin identification, this gives the kernel/cokernel six-term comparison used in the amended argument.',
 'proof sketched','E','The formal diagram argument is valid with all three vertical maps specified; later simplification depends onC051.',[],family='F07')
c(51,29,[4,5],['1020–1064'],'Integral weak Lefschetz, sans torsion cokernel.',
 'For smooth projective n-fold X over perfect k and a smooth ample divisorY, the manuscript assumes H^(n−1)_cris(X)→H^(n−1)_cris(Y) injective with torsion-free cokernel, with lower-degree isomorphisms. The opened modern theorem proves this for sufficiently high powers of an ample line bundle under coherent vanishing; it does not establish every smooth divisor in a fixed embedding.',
 'admitted ingredient, not proved','C','BMSLemma2.12 supplies the sufficiently ample integral statement. The manuscript’s all-degree saturation quantifier remains unverified in the sources opened.',['BMS2016'],family='F07',date='Berthelot weak-Lefschetz note1973 cited backwards; BMSpreprint9Feb2016, publication2018.')
c(52,28,[3,4,6,7,8],['1000–1048;1089–1102;1113–1119;1154–1156'],'Canceled cup-product w and Poincaré correction.',
 'The erased route identifies a torsion correction with cup product by the polarization and adds kernel/cokernel terms. The final live w instead means ker v→H^n_cris[p]_st. The old formula is not a premise of the revised theorem.',
 'withdrawn in the same text','F','General Gysin and duality results do not validate this particular discarded identification. It is excluded from the live claims.',['Illusie1976'],family='F07')
c(53,30,[5],['1049–1060'],'Le foncteur semi-simple est exact.',
 'Over a perfect field, taking the bijective/stable summand of a finite-dimensional p-semilinear vector space is an exact functor. This is a Fitting decomposition statement, not semisimplicity of a Galois representation.',
 'stated without proof','E','Independent proof in proofs.md; KatzSGA7XXII uses the same stable-F formalism.',['KatzSGA7XXII'],family='F08')
c(54,30,[5],['1049–1064'],'StableF modules and Fp Galois modules.',
 'Finite-dimensional k-spaces with bijective Frobenius-semilinear map are equivalent to finite-dimensional continuous Fp-representations of Gal(k^sep/k); tensoring the fixed vectors over k^sep reconstructs the module. Geometric Frob and the Galois generator have inverse conventions.',
 'stated without proof','B','The unit-F/local-system correspondence is established; the convention must be fixed before comparing eigenvalues.',['KatzSGA7XXII'],family='F08')
c(55,31,[6],['1065–1088'],'Augmentation induces isomorphism on ss parts.',
 'For proper X/k with finite deRham hypercohomology, k perfect, augmentation H^i_dR(X/k)→H^i(X,O_X) induces an isomorphism on stable Frobenius parts. Frobenius is zero in positive differential degree on the Hodge spectral sequence; apply the exact stable-part functor.',
 'proof sketched','B','Exact later match: KatzSGA7II,XXII,Theorem3.3,formula(3.3.4).',['KatzSGA7XXII'],family='F08',date='SGA7IIpublished1973.')
c(56,32,[6,7],['1089–1113'],'Revised conditional theorem8.5.',
 'Assume crystalline universal coefficients, the duality identifications used, and the integral weak-Lefschetz saturation. For smooth projective connected n-foldX over perfectk and smooth hypersurfaceY, letE=coker(H^(n−1)_crisX→H^(n−1)_crisY) be free and v the stable coherent restriction. Then0→ker v→H^n_cris(X)[p]_st→(E/p)_st→coker v→0.',
 'conditional proof sketched; statement altered in the text','C','The live sequence follows the manuscript’s amended diagram under its admitted inputs. The sufficiently high-degree case is supported by modern integral Lefschetz; all degrees are not certified.',['BMS2016','KatzSGA7XXII'],family='F07')
c(57,32,[7,8],['1126–1145'],'Dimension identity and inequality8.5.5–6.',
 'UnderC056, dim(E/p)_st=dim coker v+dimH^n_cris[p]_st−dimker v≥dimcoker v. The last inequality uses injectivity ofker v into the torsion term. Canceled negative cup-product corrections are absent.',
 'proved there from the amended exact sequence','E','Correct formal consequence ofC056; no later theorem is needed for the dimension calculation.',[],comp='Exact-sequence dimension calculation in proofs.md and check_calculations.py.',family='F07')
c(58,33,[7],['1120–1124'],'Number of unit Frobenius eigenvalues.',
 'For a finite free crystalline Frobenius module over W(Fq), the stable rank of its reduction equals the number of p-adic unit eigenvalues of the q-linear Frobenius, counted with multiplicity. Reduction of these eigenvalues agrees with stable reduction, with inverse arithmetic-Frobenius convention on the associated Fp representation.',
 'stated without proof','B','Established slope-zero/stable-rank comparison. The free hypothesis avoids pretending torsion has rational eigenvalues.',['Koblitz1975','KatzSGA7XXII'],family='F08')
c(59,33,[7],['1124'],'ℓ-adic and crystalline eigenvalues, conditional on algebraic Λ.',
 'The author compares the vanishing crystalline and ℓ≠p eigenvalues subject to algebraicity of a Lefschetz inverse. For smooth projective varieties over finite fields, the characteristic polynomials of crystalline and ℓ-adic Frobenius agree; applying this to restriction quotients requires the indicated exactness.',
 'stated conditionally without proof','B','Katz–Messing1974 removes that specific comparison proviso; it does not remove integral saturation or identify torsion. The original PDF yielded only a repository cover; the theorem was checked through Illusie’s primary contemporaneous exposition.',['KatzMessing1974','Illusie1976'],family='F08',date='Inventiones1974; no earlier circulation date verified.')
c(60,34,[8],['1147–1152'],'Je pense v injectif; n=2 and sufficiently large d.',
 'For smooth projective connected X of dimensionn≥2, v:H^(n−1)(O_X)_st→H^(n−1)(O_Y)_st is injective ifH^(n−1)(O_X(−d))=0, by the coherent long exact sequence. Forn=2 this follows from the π₁ Lefschetz statement and Artin–Schreier. The assertion for every dimension and every smooth hyperplane remains a separate quantifier.',
 'general question; special cases stated','C','The two stated sufficient cases are valid. Searches did not locate an exact all-degree unit-F cohomology theorem covering the full claim.',['KatzSGA7XXII','BerthelotEsnaultRulling2012'],family='F08',confidence='medium')
c(61,35,[8,9],['1158–1181'],'Generic maximum ss rank gives an open with constant unit count.',
 'After restricting to an open where stable Hasse–Witt ranks and the relevant coherent base changes are constant, and controlling ker v, the number of unit eigenvalues in vanishing crystalline cohomology is constant. High degree gives ker v=0 byC060.',
 'proof sketched with ker v qualification','B','The rank condition is governed by iterates of Hasse–Witt maps. It is not an automatic assertion on every initially chosen maximum-rank locus without base-change control.',['Koblitz1975'],family='F08')
c(62,35,[9],['1185–1196'],'Relative exact sequence of locally free modules/local systems.',
 'On a suitable open U_d of smooth hypersurfaces, the finite locally free unit-F pieces define finite Fp-local systems and the amended comparison varies as a morphism of such systems. Over an imperfect base the correct structure is an isomorphismF*E→E.',
 'stated without proof','C','The unit-F dictionary is established. The exact relative integral-vanishing-cohomology sequence with only the manuscript’s chosen open hypotheses was not separately verified.',['KatzSGA7XXII','Koblitz1975'],family='F08',confidence='medium')
c(63,35,[9],['1196–1204'],'Kernel constant from base k.',
 'The kernel of the relativeφ is the quotient of the constant base-field termH^n_cris(X)[p]_st byker v. Ifker v=0, or if its embedding is controlled as a constant sub-local-system, the kernel is pulled back fromk. Maximum Hasse–Witt rank alone does not establish that constancy.',
 'stated without proof','C','The asserted constant kernel is valid under these added control hypotheses. No source was found justifying the unconstrained literal statement.',['Koblitz1975'],family='F08',confidence='medium')
c(64,35,[9,10],['1199–1214'],'Finite extension makes the fixed Frobenius eigenvalues1.',
 'A finite Fp representation of the finite-field Galois group has finite image, so a finite base-field extension trivializes it. This eliminates the fixed constant contribution when studying mod-p Frobenius eigenvalue variation; it does not imply anything about geometric monodromy of the varying quotient.',
 'stated without proof','E','Correct finite-image argument. Keeping arithmetic and geometric monodromy separate is essential.',[],family='F08')
c(65,36,[9],['1173–1183'],'Generic stable vanishing cohomology positive for large d.',
 'For every projective equidimensional Cohen–MacaulayX/k of dimensionn≥1, there isd0 such that for everyd≥d0 the generic degree-d hypersurface sectionY has nonnilpotent Frobenius on H^(n−1)(Y,O_Y)/imH^(n−1)(X,O_X). For smoothX the generic smooth locus supplies the manuscript application.',
 'open in the running text; margin claims absent section7 proves it','B','Exact later theorem: KatzSGA7II,XXI,Theorem1.4, printedpp374–376. It is not merely a complete-intersection special case.',['KatzSGA7XXI'],family='F09',date='Published1973; first lecture/circulation date not verified.')
c(66,36,[9],['1173–1176'],'Unit root should be equivalent to motivic level n−1.',
 'A unit Frobenius eigenvalue obstructs positive coniveau, via divisibility of eigenvalues on positive-coniveau classes. The converse and the meaning of the manuscript’s “niveau” for arbitraryX require additional motivic definitions; they are not consequences of generic positivity alone.',
 'open on the pages','C','KatzSGA7XXICorollary2.2 supplies the divisibility direction; Theorem4.2 gives a maximal-coniveau result for smooth complete intersections. The exact general equivalence remains unverified.',['KatzSGA7XXI'],family='F09',confidence='medium')
c(67,39,[10],['1216–1221'],'φ bijective iff w onto; torsion-free sufficient.',
 'InC056,φ is always surjective and is bijective iffker v→H^n_cris[p]_st is surjective. Ifker v=0, this is equivalent toH^n_cris[p]_st=0. Absence of crystallinep-torsion in degreen is sufficient; the dual torsion degree is shifted.',
 'corrected by himself later','E','Correct directly from the amended exact sequence. The former nonsurjectivity version is withdrawn.',[],comp='Exact-sequence computation in proofs.md§2.',family='F07')
c(68,37,[10],['1222–1230'],'Express the sufficient torsion condition on a characteristic-zero lift.',
 'If X and its polarization lift to characteristic0, the author hopes for a criterion in p-adic étale torsion of the lift equivalent to his crystalline torsion sufficient condition. He does not assert an equality of all integral cohomology groups.',
 'open on the pages','C','BMSTheorem1.1 gives a one-sided torsion-length comparison, with strict examples in§2.3. It does not establish this exact stable-F criterion, so the question is only partly answered.',['BMS2016'],family='F07',date='arXivpreprint2016; publication2018.')
c(69,38,[10,11],['1232–1248;1271–1277'],'Canceled nonsurjectivity and higher-dimensional product.',
 'The initial request forφ not surjective contradicts the revised sequence and is canceled. The positive-degree crystalline cohomology of projective space has positive slopes, so the proposed projective-space factor does not provide the required stable-F summand.',
 'withdrawn in the same text','E','The author’s final question is failure of injectivity/bijectivity. The discarded product is not an example.',[],family='F07')
c(70,39,[11],['1250–1271'],'Serre’s free Z/p quotient surface yields kerφ≠0.',
 'Over an algebraically closed field of characteristic p, for the indicated smooth projective surface S obtained as a free Z/p quotient of a suitable simply connected complete intersection, H¹_cris(S)=0 andH¹_et(S,Fp)=Fp. Derived base change and stable augmentation giveH²_cris(S)[p]_st≅k. Sincev is injective for surfaces,kerφ has dimension1 whenever the admitted integral-Lefschetz setup definesφ.',
 'example sketched','E','Berthelot–Esnault–Rülling§9.2 verifies the Serre free-quotient construction and its cohomological use. The original1958scan could not be opened within the reader’s size limit. The stated implications are checked independently; no new higher-dimensional geometric example is claimed.',['BerthelotEsnaultRulling2012','Serre1958metadata'],family='F07',confidence='medium',date='SerreMexico1956lecture/published1958; later primary verification2012.')
c(71,39,[11],['1254–1260'],'φ bijective means inequality8.5.11.1 is equality.',
 'Letb=dim(H^(n−1)_cris,tor/p)_st,c=dimH^n_cris[p]_st,k0=dimker v. The displayed inequality’s defect isb+c, whiledimkerφ=c−k0. The alleged equivalence needs additional hypotheses such asb=0 andk0=0; it is not a consequence of the stated sequences in general.',
 'stated without proof; missing-hypothesis alarm','C','Independent exact-sequence derivation isolates the extra preceding-degree torsion. The algebraic patternb1,c0,k0=0 is a countermodel to the formal implication, not an asserted geometric counterexample.',['KatzSGA7XXII','BMS2016'],comp='proofs.md§2; check_calculations.py torsion criterion.',family='F07')
c(72,38,[11],['1271–1277'],'Canceled higher-dimensional projective-space examples.',
 'Tensoring the surface torsion class with a positive-degree projective-space class does not preserve a slope-zero Frobenius reduction: the latter has Frobenius divisible byp. The written proposed stable term is therefore not established, even if Künneth is granted.',
 'withdrawn in the same text','E','The elementary slope objection supports the cancellation. A different product is not developed here.',[],family='F07')
c(73,40,[12],['1280–1296'],'Irreducible, or even fullGL_r(Fp), hypersurface monodromy.',
 'For every fixed smooth projectiveX of dimensionn≥2, and appropriate generic smooth degree-d hypersurface locusU_d, ask whether the nonconstant unit-F vanishing local system is irreducible or has imageGL_r(Fp). Distinguish geometric image from arithmetic image and retain the degree/rank qualifications.',
 'open on the pages','C','Achter–PriesProposition4.8 provesGL_f(Fp),GL_f(Zp) for each component of a p-rank stratum in moduli of genusg curves, g≥2,1≤f≤g. That family does not settle the manuscript’s fixed-X hypersurface quantifiers. No exact general theorem was located.',['AchterPries2008','StienstraPutMarel1991'],family='F10',confidence='medium',date='Achter–PriesfirstarXiv13Jul2007; revised/published2008.')
c(74,41,[12],['1307–1312'],'Rank becomes arbitrarily large with d.',
 'The final programme needs generic stable vanishing rank r_d→∞ for a fixed smooth projective n-fold X⊂P^N of degreeD as d→∞. In fact r_d has leading term Dd^n/n!; subtracting the fixed image of H^(n−1)(O_X) does not change that leading term.',
 'stated as a needed expectation','B','KoblitzI§5Theorem1 explicitly states the leading term Dd^n/n! for a constructed section. Lemma4 transfers its stable-rank bound to the generic open for Cohen–MacaulayX and d sufficiently large; Theorem2 combines them. This proves the weaker unboundedness needed here without using the unread displayed defect bound.',['Koblitz1975','KatzSGA7XXI'],family='F09',confidence='high',date='Princeton thesis1974; published1975.')
c(75,41,[12],['1295–1301'],'Every element ofFp is a trace inGL_r(Fp),r≥2.',
 'For eacht∈Fp andr≥2, diag([[t−(r−2),−1],[1,0]],I_(r−2)) has determinant1 andtracet. Hence trace mapsSL_r(Fp),and thereforeGL_r(Fp),ontoFp.',
 'stated without proof','E','Independent elementary proof gives the full quantified statement.',[],comp='proofs.md§3; check_calculations.py finite checks plus general explicit formula.',family='F10')
c(76,41,[12],['1301–1312'],'Every-open point-count congruences over finite extensions.',
 'Conditional on suitable full geometric monodromy of the varying unit-F system, constant terms controlled after base extension, and Frobenius classes occurring in every nonempty open, the trace formula would give prescribed residues modulo p for hypersurface point counts over suitable finite extensions. Arithmetic monodromy alone does not permit every class in every extension-degree coset.',
 'conditional programme, not proved','C','KatzSGA7XXIICorollary3.2 supplies the coherent trace congruence; the required all-X monodromy is not verified. The manuscript’s varying finite-extension quantifier must be retained.',['KatzSGA7XXII','AchterPries2008'],family='F10',confidence='medium')
c(77,13,[13,14],['477–487'],'T_ℓ for any ℓ in the inertia comparison.',
 'At residue characteristicp, rawT_p(A) may have infinite inertia even for good reduction. To compare with the finite special-fiber inertia character useT_ℓ forℓ≠p, or the potentially-crystalline/Weil–Deligne realization atp. The literal “anyℓ” reading cannot mean rawp-adic Tate inertia.',
 'stated without proof; material interpretation alarm','F','Modern inertial-type formulations make this distinction explicit. No reading change is adopted.',['DembeleFreitasVoight2025'],family='F04')

c(78,11,[13],['476'],'Cela impliquerait que la fonction caractère est à valeurs dansZp.',
 'The margin infers Zp-valuedness conditionally whenK containsμp. For the defined special-fiber Dieudonné inertia trace a stronger statement holds: inertia commutes with semilinearFrobenius, invertible after invertingp, so trace is Frobenius-fixed and integral, hence inW(k)^σ=Zp, without theμp condition.',
 'conditional unproved implication in the margin','B','Independent proof separates this true trace-integrality assertion from the false mod-p recovery claim. The Dieudonné framework supplies the commuting operators.',['Oda1969','BerthelotMessing1979'],comp='Matrix identityBA=Aσ(B) givestrB=σ(trB); proofs.md§4.',family='F04')
c(79,12,[13],['474'],'No difficulty for potentially constant or multiplicative reduction ifμp⊂K.',
 'In the potentially constant case, finite integral inertia gives the Brauer trace. In the potentially multiplicative case, Cartier duality introduces the cyclotomic twist; ifμp⊂K its mod-p character is trivial, removing the counterexample used forμ_p∞ overQp. This does not include potentially supersingular reduction.',
 'stated without proof','B','The ordinary/multiplicative restriction is consistent with Cartier duality; the supersingular case is separately refuted inC023.',['Oda1969','Katz1981'],family='F04')
c(80,8,[5],['198–239'],'Coefficient functional is left/rightW-linear; twistedF,V identities and compatibility.',
 'In the Dieudonné ring withFa=σ(a)F,Va=σ⁻¹(a)V,FV=VF=p, the normal-form coefficientφ obeysφ(az)=aφ(z),φ(za)=φ(z)a,φ(Fz)=σφ(zF),φ(zV)=σφ(Vz). Compatible truncation maps preserveφ. The canceledφ(F^iV^i)=0 is false wheneverp^i survives.',
 'partial computation; two checks markedOK; final display unfinished','B','The monomial calculations are correct with the displayed Frobenius twists. They do not settle the separate finite-truncation perfectness or cancellation issue.',['Oda1969'],comp='Independent monomial derivation in proofs.md§4; check_dieudonne_twists.py checks nontrivial unramifiedquadraticW2 coefficients.',family='F02')

c(81,7,[3],['130–147'],'Enveloping group and Lie algebra of the dual extension.',
 'For a p-divisible group G over a perfect characteristic-p field, the enveloping extension is interpreted as its universal vector extension: its vector kernel is the group associated to ω_(G*), denotedV(t_(G*)) in the manuscript’s vector-group convention. Its Lie sequence is0→ω_(G*)→LieE(G)→LieG→0; the dual gives0→ω_G→D(G)_k→LieG*→0. No finite-type representability of the whole p-divisible sheaf is asserted.',
 'construction stated without proof','B','IllusiePisa2015pp16–17 explains the universal-extension route and Messing’s crystalline construction; Berthelot–Messing1979§2 and§5 provide the later cohomological and duality framework.',['IllusiePisa2015','BerthelotMessing1979'],family='F02',date='Grothendieck1966letter discussed in the primary historical source; Messing1972 construction cited there.')
c(82,40,[12],['1280–1296'],'n≥2 qualification and the projective-line boundary remark.',
 'For X=P1 and a smooth degree-d zero-dimensional section Y, the vanishing H⁰ representation is Fp^d/Fp and monodromy factors through the permutation groupS_d. It therefore cannot be fullGL_(d−1)(Fp) in general: p=3,d=3 gives order at most6 versus48. This checks the need to exclude n=1; it does not refute the stated n≥2 question.',
 'boundary case explicitly separated in the manuscript','E','The permutation representation gives an elementary exact boundary test. No implication for higher-dimensional hypersurface monodromy is asserted.',[],comp='check_monodromy_boundary.py enumerates the six quotient matrices and all48 invertible2×2 matrices overF3.',family='F10')

assert [int(x['id'][-3:]) for x in claims]==list(range(1,83))
assert all(families.values())
(W/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
(W/'claim_search_families.json').write_text(json.dumps(families,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(claims),'manually authored claims; every claim has a searched family.')
