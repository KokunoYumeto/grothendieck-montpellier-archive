"""Manually reconciled claims of the Pro 36:002--052 selection.

Each semantic record was authored after reading the complete source passage.
The helper in build_p3.py only fills repeated locator metadata.
"""
claim(250,[7],
 'Let f:G→H be a homomorphism of semiabelian varieties over a field k. The filtration by the maximal torus and abelian quotient is strict in the category up to isogeny. For ell invertible in k, f is an isogeny exactly when V_ell(f) is an isomorphism on geometric rational Tate modules.',
 'stated without proof','B',
 'The semiabelian/weight formalism is explicit in Deligne HodgeIII10.1.3–10.1.10 (documented preprintJanuary1972, publication1974). A direct proof uses absence of homomorphisms from an abelian variety to a torus and the exact Tate sequence; integral strictness is not inferred. No proof of the Tate isogeny conjecture is involved: the map f already exists.',
 ['Deligne1974HodgeIII','Deligne1972HodgePreprint','Milne1986Abelian'],['P3-S01'],computation='review.md §Semiabelian filtration: direct argument; no numerical computation.')
claim(251,[9],
 'For a morphism f:G→H in an abelian sheaf category, K=ker f satisfies K[n]=ker(G[n]→H[n]). If G[n],H[n] are finite étale group schemes over the same base, this kernel is finite étale. The additional specialization inclusion on the leaf has no recoverable complete base hypotheses.',
 'stated without proof','E',
 'The kernel identity is a formal intersection of two kernels and is independently proved here. Finite étale kernels follow by étale local constant finite groups. SGA7IX concerns the specialization context, but the isolated eta/s-subscript assertion is not uniquely identified.',
 ['SGA7IX'],['P3-S02'],computation='review.md §Kernel identity; separate unresolved specialization assertion is C-SA13-310.')
claim(252,[10],
 'For a discretely valued field K, a prolongation of its valuation to K^sep determines decomposition and inertia subgroups. A different prolongation conjugates these subgroups. A nonhenselian trait does not select a preferred embedded inertia subgroup without the choice.',
 'stated without proof','E',
 'Standard valuation-theoretic construction; SGA7IX3.5 explicitly passes to a henselization when formulating the inertia criterion. Brinon–Conrad2009§1.1 also makes the place/embedding choice explicit. The draft criticism is justified at the level of this choice, without judging the absent paragraph.',
 ['SGA7IX','BrinonConrad2009'],['P3-S02'])
claim(253,[11],
 'For a henselian discretely valued K with residue field k, the exact quotient G_K→G_k by inertia gives a morphism of classifying étale topoi. The sheet proposes a ringed-topos relative-scheme interpretation of the Néron construction, but the choice of k/K and its alleged equivalence are underdetermined.',
 'open on the pages','F',
 'The classifying-topos part is standard; the tubular-neighbourhood relative-scheme theorem cannot be uniquely reconstructed from the uncertain base and omitted definitions. SGA7IX and the primary bibliography of the chapter were searched; no exact theorem match was certified.',
 ['SGA7IX'],['P3-S02'],confidence='medium')
claim(254,[20],
 'Proposed counterexample: deform E×F, with E ordinary elliptic and F nonordinary elliptic in characteristic p, through abelian schemes so the generic abelian surface is geometrically simple. Then the special ordinary elliptic factor cannot lift as a positive-dimensional proper abelian subvariety of the generic fibre.',
 'proof sketched','C',
 'The implication from a generically simple family is valid; the page does not construct that family or specify the intended lifting category. Searches of the SGA7IX and abelian-deformation literature did not certify the exact family here. This does not rule out a formal or p-divisible subgroup lift, and is not recorded as a completed refutation of a recovered published theorem.',
 ['SGA7IX','Robert2023'],['P3-S03'],confidence='medium')
claim(255,[22],
 'In the missing draft setup, finite and toric parts of the expected ranks should exist up to isogeny. The object, base, expected ranks and functoriality are not fully copied on the editorial leaf.',
 'open on the pages','F',
 'SGA7IX2 and5 do construct finite/toric parts under specific hypotheses, but the editorial expectation has insufficient quantifiers for an exact identification. Publication1972 is not evidence that every possible version of this question was proved.',
 ['SGA7IX','Robert2023'],['P3-S02'],confidence='medium')
claim(256,[28],
 'Let R be a DVR and A its generic-fibre abelian variety with Néron model. Under the standard unramified base-change hypotheses (ramification index one and separable residue extension, including completion in the cited formulation), the Néron model base-changes to the Néron model over the completed trait.',
 'open on the pages','B',
 'An established Néron-model theorem is stated with its precise hypotheses in Robert2023 Proposition3.1.5 and traced there to BLR1990. The leaf itself asks for the reference. The publisher record for BLR is verified; its full proof was not inspected, and no arbitrary limit theorem is asserted.',
 ['Robert2023','BLR1990'],['P3-S04'])
claim(257,[29],
 'Determine whether extending a given biextension over a trait is equivalent to extending its restrictions on ell-primary torsion, with the relevant component, divisibility and representability conditions. The leaf records an interlocutor’s claim only conditionally.',
 'open on the pages','F',
 'SGA7VII–IX contain extension and torsion reconstruction results, but the exact omitted claim cannot be identified from the paraphrase. The finite-level reconstruction on36:048–050 is a related precise statement, not a proof of the trait-level equivalence as worded here.',
 ['SGA7VII','SGA7VIII','SGA7IX'],['P3-S05'],confidence='medium')
claim(258,[31],
 'In an abelian sheaf topos, for a locally constant finite free lattice M, internal Ext^1(M,Gm)=0; locally M=Z^r, and internal Hom(M,-)=(-)^r is exact. Global Ext^1 need not vanish.',
 'stated without proof','E',
 'This is the elementary local-freeness input in Deligne1974§10.2.1 and the standard complex-biextension definition. Independently checked by localizing to a basis. The distinction between internal Ext and global Ext is essential.',
 ['Deligne1974HodgeIII'],['P3-S01'],computation='review.md §Internal and global Ext.')
claim(259,[31],
 'For an abelian scheme B/S, every homomorphism of S-group schemes B→Gm is trivial, universally in S. Properness and geometrically connected fibres give f_*O_B=O_S and identity preservation removes the scalar.',
 'stated without proof','E',
 'Standard abelian-scheme rigidity, used in the 1-motive duality formalism. The argument is independently rechecked and does not say that arbitrary maps B→Gm vanish: they are constant.',
 ['Milne1986Abelian','Deligne1974HodgeIII'],['P3-S01'],computation='review.md §Internal and global Ext.')
claim(260,[32,33],
 'A biextension of complexes [M→G],[M′→G′] in degrees -1,0 is a biextension of G×G′ together with trivializations on M×G′ and G×M′ whose restrictions to M×M′ agree. In the extension construction on the leaf, the two chosen lifts must induce this same trivialization.',
 'stated without proof','B',
 'Precisely the definition and compatibility in Deligne1974§10.2.1, already present in the January1972 preprint. The manuscript’s cancelled explanation is not restored as a completed proof.',
 ['Deligne1974HodgeIII','Deligne1972HodgePreprint'],['P3-S01'])
claim(261,[33],
 'For complexes K,L concentrated in degrees -1,0 of an abelian topos and an abelian sheaf G, Biext^i(K,L;G)=Ext^i(K⊗^L L,G) for i=0,1, with the compatible-trivialization definition.',
 'proof sketched','B',
 'Exact published match: Deligne1974§10.2.1, with general-topos hypotheses and i=0,1. Documented circulationJanuary1972. Bertolin2008/2012 develops a further 1-motive-valued version, which is not needed to fill the manuscript’s stopped argument.',
 ['Deligne1974HodgeIII','Deligne1972HodgePreprint','Bertolin2012Biextensions'],['P3-S01'])
claim(262,[35],
 'For A=[M→G] in degrees -1,0, H^0RHom(Z/n,A) is represented by pairs (m,g) with u(m)=ng, modulo (nm′,u(m′)); signs are fixed by this cone convention. This is an equality of sheaves, so lift existence is local.',
 'stated without proof','B',
 'Deligne1974§10.1.5 gives the torsion realization; a direct two-term free resolution of Z/n independently reproduces the formula here. No characteristic assumption is needed for the formal complex calculation.',
 ['Deligne1974HodgeIII'],['P3-S01'],computation='review.md §Torsion complex; computations.py verifies the finite cyclic test model.')
claim(263,[35],
 'If M[n]=0 and n:G→G is an epimorphism, that torsion realization fits 0→G[n]→V_n(A)→M/nM→0. The quotient map sends [(m,g)] to m mod n.',
 'stated without proof','B',
 'Exact sequence in the torsion realization of 1-motives (Deligne1974§10.1.5–10.1.7). Independently proved by local lifts and the explicit quotient: the kernel is represented by (0,g), uniquely modulo M[n].',
 ['Deligne1974HodgeIII'],['P3-S01'],computation='review.md §Torsion complex; computations.py finite cyclic model.')
claim(264,[36],
 'Over a separably closed field, for a 1-motive [M→G] and ell invertible in the field, taking inverse limits of the torsion sequences with the standard multiplication transitions gives 0→T_ell G→T_ell A→M⊗Z_ell→0. Arbitrary inverse limits on an arbitrary topos require an additional derived-limit argument.',
 'stated without proof','B',
 'The 1-motive realization is established in Deligne1974§10.1.7–10.1.10. Exactness of the geometric sequence follows from surjective transition maps. The source does not justify every possible sheafwise limit or section functor.',
 ['Deligne1974HodgeIII'],['P3-S01'],computation='review.md §Tate transition argument.')
claim(265,[37,41],
 'A biextension gives a bilinear pairing on n-torsion by comparing its two canonical n-fold trivializations. The value is independent of the chosen lift because changes multiply both trivializations by the same n-th power.',
 'proof sketched','B',
 'Deligne1974§10.2.5 explicitly constructs this for 1-motives over an algebraically closed characteristic-zero field; the typed sheaf calculation on36:034,032,030 belongs to the SGA7 biextension formalism. The local cancellation calculation is rechecked here without promoting the incomplete Ext-arrow diagram to a proof.',
 ['Deligne1974HodgeIII','SGA7VII'],['P3-S05'],computation='review.md §Finite pairing and transitions; computations.py cyclic pairing checks.')
claim(266,[41,43,67],
 'For n′=mn the finite pairing obeys the one-factor transition obtained from multiplying an n′-torsion lift by m; with both factors multiplied, e_n(mx,my)=e_n′(x,y)^m. The target in the Tate limit is Z_ell(1), and swapping factors changes the sign under the convention used for the derived tensor.',
 'proof sketched','B',
 'Milne1986 section16, especially Lemma16.1, verifies the simultaneous-multiplication power. Deligne1974§10.2.4 verifies the interchange sign in the complex interpretation. Suspect n/n′ and P/Q indices in the transcript are kept as reading alarms, not silently repaired.',
 ['Milne1986Abelian','Deligne1974HodgeIII'],['P3-S05'],computation='computations.py: exact Fraction pairing transition identity.')
claim(267,[38],
 'For dual 1-motives, weight -2 torus torsion is orthogonal to weight -1 semiabelian torsion on the other side; the associated graded pairings are lattice–torus evaluation and the abelian Weil pairing.',
 'stated without proof','B',
 'Deligne1974§10.2.2–10.2.6 realizes the duality and its finite/weight-compatible pairings. The general finite-flat all-characteristic version belongs to SGA7VIII; the independently checked argument here concerns the formally identified graded pairings and does not erase the extra geometric hypotheses.',
 ['Deligne1974HodgeIII','SGA7VIII','Milne1986Abelian'],['P3-S01'])
claim(268,[38],
 'In a finite filtered object with exact Cartier duality, if a pairing respects opposite filtrations and every associated graded pairing is perfect, the total pairing is perfect. This applies to finite locally free torsion group schemes once the orthogonality statements and graded identifications have been proved.',
 'stated without proof','E',
 'The implication is an elementary induction on exact sequences (five lemma), independently proved here. It is not a deduction from equal ranks alone. The concrete graded factors are standard in Deligne’s1-motive and abelian duality formalism.',
 ['Deligne1974HodgeIII','Milne1986Abelian'],['P3-S01'],computation='review.md §Filtered perfectness; computations.py checks the block-triangular matrix illustration, not a proof for every sheaf.')
claim(269,[44],
 'For a smooth proper geometrically connected curve X over algebraically closed k, and n invertible in k, Kummer identifies H^1_et(X,mu_n) with Pic(X)[n]=J[n](k); H^2_et(X,mu_n)=Z/n through degree. Poincaré duality induces the perfect degree-one cup pairing.',
 'stated without proof','E',
 'The finite-coefficient curve theorem is standard étale duality, with Kummer hypotheses explicitly verified in Stacks59.28. The handwritten table omits the curve/base conventions and appears to mix finite and ell-adic coefficient symbols; it is not accepted for arbitrary X.',
 ['Stacks03PK','Milne1986Abelian','SGA4XVIII'],['P3-S06'],computation='review.md §Curve table; no numerical calculation.')
claim(270,[45],
 'In characteristic p, mu_p requires fppf rather than étale Kummer theory, Z/p uses Artin–Schreier, and alpha_p uses 0→alpha_p→Ga→Ga→0 with Frobenius in the fppf site. For proper X over algebraically closed k, H^1(alpha_p)=ker(F on H^1(O_X)). These are three different coefficient objects.',
 'stated without proof','E',
 'The Kummer and Artin–Schreier sequences are checked in Stacks59.28 and59.63; the alpha_p statement follows by the same exact-sequence calculation and surjectivity of Frobenius on k. The uncertain coefficient glyph in36:036 is not decided by this reconstruction.',
 ['Stacks03PK','Stacks0A3J','Oda1969'],['P3-S06'],computation='review.md §Curve table; computations.py Frobenius finite-field diagnostic.')
claim(271,[46],
 'A local-to-global Ext spectral sequence can compare H^p of internal Ext^q with global Ext^{p+q}, under the usual boundedness/acyclicity hypotheses. The handwritten f_! comparison is only a proposed programme; its functors and category are not defined on the leaf.',
 'open on the pages','F',
 'Stacks20.43 gives an exact bounded ringed-space comparator; SGA4XVIII and Deligne1974 provide related derived duality formalisms. No unique f_! theorem can be identified from the displayed unfinished chains. The standard spectral sequence is not evidence of the claimed unspecified abutment.',
 ['Stacks0BQP','SGA4XVIII','Deligne1974HodgeIII'],['P3-S07'],confidence='medium')
claim(272,[47],
 'For X smooth proper over a field and A an abelian variety, H^1_et(X,A)=H^1_fppf(X,A) is torsion. The page uses this before its Kummer comparison. It must not be extended merely to arbitrary normal X.',
 'stated without proof','B',
 'Exact primary comparison inspected in original SGA4XVIII1.2.9(b), printedp497 (1973): for smooth X the proof invokes Raynaud XIII2.6 to conclude torsion of H1(X,A). Raynaud’s1970 book is the cited earlier result; the first-circulation date was not found. Singular extensions can fail and normality alone is not sufficient. The proper smooth curve case is also independently checked here.',
 ['SGA4XVIII','Raynaud1970Torsors','MOAbelianTorsion'],['P3-S08'],confidence='medium',computation='review.md §Abelian torsors: regular-curve proof; broad normal-base statement expressly excluded.')
claim(273,[48],
 'For a pointed smooth proper connected X over algebraically closed k and an abelian variety A, Kummer gives 0→Hom(Alb_X,A)/n→H^1(X,A[n])→H^1(X,A)[n]→0, because the constant A(k) summand is divisible. For ell prime to char(k), the middle group is Hom(pi1^ab_et(X),A[ell^r](k)) at n=ell^r.',
 'stated without proof','E',
 'Kummer and torsor classification provide the exact finite-level sequence. Pointed Albanese accounts for maps and removes constants only after using divisibility of A(k). No canonical identification of all Pic^0,Pic^tau,Pic is inferred. Finite étale abelian covers are checked in Milne15.3.',
 ['Stacks03PK','Milne1986Abelian'],['P3-S08'],computation='review.md §Kummer and the direct limit.')
claim(274,[49],
 'With the standard transition H/nH→H/(mn)H, h mod n↦mh mod mn, the filtered colimit is H⊗Q/Z, not H⊗Q. The natural target of a colimit of finite torsion pieces is torsion.',
 'false as stated','F',
 'The literal coefficient Q in the transcribed limiting formula cannot be justified by this standard Kummer limit. The refined Q/Z statement is independently proved by tensoring colim Z/n=Q/Z. This refutes the literal displayed standard-transition reading; a different intended transition convention remains possible, so ink is undecided.',
 ['Stacks03PK'],['P3-S08'],computation='review.md §Kummer and the direct limit; computations.py exact denominator compatibility.')
claim(275,[50,51],
 'A proposed comparison between H^1(X,A) and Ext^1(A^t,Pic_X) needs the relative site, Picard component, internal versus global Ext, and base cohomology terms. The sheet asks whether its unspecified form extends to singular X.',
 'open on the pages','F',
 'Raynaud1970 Proposition6.2.1 verifies a precise finite-flat duality theorem, and Mehidi–Poiret2025 extends finite-flat/log torsor methods to nodal curves. Neither is an exact proof of this abelian-group formula with its missing conventions; searches did not recover an exact theorem at the displayed generality.',
 ['Raynaud1970Picard','MehidiPoiret2025','SGA4XVIII'],['P3-S08'],confidence='medium')
claim(276,[51],
 'The interpretation “smooth proper X implies H^i_et(X,Gm)=0 for every i≥2” is false over an arbitrary base field: X=Spec R is smooth proper over R and H^2_et(X,Gm)=Br(R)=Z/2.',
 'false as stated','E',
 'The real quaternion algebra gives the nonzero Brauer class; equivalently H^2(Gal(C/R),C*)=R*/N(C*)=±1. This independently refutes only the i≥2 absolute reading. It does not refute i>2 or the geometrically based singular-duality question.',
 ['Stacks03R1'],['P3-S08'],computation='review.md §Two precise counterexamples; computations.py norm identity.',authorship='Reviewer diagnostic counterexample; not an assertion copied from Grothendieck')
claim(277,[51],
 'Torsion of abelian torsors does not extend to every singular proper curve: over C, glue the trivial A-torsor on P1 by translation by an infinite-order a∈A(C) between 0 and infinity on the nodal curve. Its class has infinite order.',
 'open on the pages','E',
 'This is the present reviewer’s independently checked diagnostic of an unrestricted singular extension, not a counterexample to a specified theorem on the page. The MathOverflow reference trail points to Raynaud’s analogous examples. Normalization maps P1→A are constant, so n times the torsor is trivial exactly when na=0.',
 ['MOAbelianTorsion','Milne1986Abelian'],['P3-S08'],computation='review.md §Two precise counterexamples; no numerical sampling used.',authorship='Reviewer diagnostic counterexample; not an assertion copied from Grothendieck')
claim(278,[53],
 'Let f:X→S be proper, flat and finitely presented with f_*O_X=O_S universally. For a finite locally free commutative S-group G, R^1f_*(G_X) is canonically Hom(G^D,Pic_X/S), as sheaves. This precise form does not identify absolute H^1 without accounting for base terms.',
 'stated without proof','B',
 'Exact primary theorem: Raynaud1970 Proposition6.2.1, obtained by putting M=G^D. The page’s broader affine G formula is only partly identified: arbitrary affine groups need a different dual object and topology. Modern nodal-curve versions do not remove this distinction.',
 ['Raynaud1970Picard','MehidiPoiret2025'],['P3-S09'])
claim(279,[53],
 'Over a characteristic-zero field there is no nonconstant polynomial group homomorphism Ga→Gm on reduced field points, but the sheaf of characters on all test algebras is nontrivial: over k[epsilon]/epsilon², x↦1+epsilon x is multiplicative.',
 'open on the pages','E',
 'Independent algebra calculation clarifies why a pointwise character test cannot refute sheaf/formal Cartier duality. Raynaud’s finite-flat theorem is a different scope. The broad formula remains underdetermined, not disproved by Ga alone.',
 ['Raynaud1970Picard'],['P3-S09'],computation='computations.py dual-number character; review.md for the units-in-k[x] argument.')
claim(280,[55],
 'For gamma=Z^r constant finite free, internal Hom(gamma,G)=G^r and H^1 commutes with the finite product, giving the proposed exchange. For general gamma or undefined relative categories the exchange is not automatic; higher Ext and acyclicity terms intervene.',
 'open on the pages','C',
 'The finite-free special case is independently proved. The general question is a derived-functor comparison, for which Stacks20.43 supplies a bounded ringed-space model, not an affineness-only theorem. No exact settlement of the missing general setup was identified.',
 ['Stacks0BQP'],['P3-S07'],computation='review.md §Derived exchange obligations.')
claim(281,[56],
 'An equality exchanging relative H^1 with internal Ext^1 requires compatible derived adjunctions and vanishing of all competing edge terms/differentials. No unrestricted equality follows from the handwritten symbols or affineness.',
 'open on the pages','F',
 'The local-to-global Ext spectral sequence is established, but the site and the functors in this specific formula are unprovided. Searches in SGA4XVIII, Deligne’s complex formalism and Stacks20.43 did not identify the exact statement as written.',
 ['Stacks0BQP','SGA4XVIII'],['P3-S07'],confidence='medium')
claim(282,[57],
 'For a proper birational map to a normal integral scheme, its inverse is defined at codimension-one points; extending a divisor from the resulting open produces a Weil divisor, and local factoriality is needed to guarantee that this is Cartier. The manuscript cancels the whole proposed proof.',
 'corrected by himself later','F',
 'The elementary normal/codimension-one facts and the locally factorial repair are standard. They do not establish an unqualified Picard-invariance theorem for arbitrary integral schemes. No exact theorem can be attached to the cancelled draft without its intended hypotheses.',
 ['Robert2023','Stacks0BQP'],['P3-S10'],confidence='medium',computation='review.md §Cancelled divisor argument: no theorem is inferred from the cancellation.')
claim(283,[58],
 'The displayed degree-two group is not generally a direct sum of Ext^1 against Pic^(1) and Hom against Pic^(2). In a derived comparison, filtration extensions and spectral-sequence differentials must be retained; identifying the abutment requires its own duality theorem.',
 'stated without proof','E',
 'The manuscript actually writes not-equal, with emphasis. Truncation triangles and the local-to-global Ext spectral sequence explain why a direct sum cannot be inferred. The modern repair is a reviewer/earlier-run reconstruction and does not assert the missing abutment comparison.',
 ['Stacks0BQP','Deligne1974HodgeIII'],['P3-S07'],computation='review.md §Derived exchange obligations.')
claim(284,[60,61],
 'A shifted duality for an abelian group A is proposed beside a shriek/star adjunction programme. The degrees, sites and dualizing object are not defined enough to produce one precise equivalence of derived functors.',
 'open on the pages','F',
 'SGA4XVIII and Deligne10.2.1 show established derived frameworks, but no exact quantified theorem is identifiable from the unfinished draft. A shift by one cannot be erased by treating f^!,f_! as primes or stars.',
 ['SGA4XVIII','Deligne1974HodgeIII'],['P3-S07'],confidence='medium')
claim(285,[61],
 'If X/S has a section x and gamma is a commutative group sheaf, evaluation at x splits the sheaf of maps X→gamma as constants gamma times maps vanishing at x. The pointed factor vanishes only under a separate universal rigidity assumption.',
 'proof sketched','E',
 'Independent proof sends h to (h(x),h-h(x)), with inverse (c,h0)↦c+h0. Connectedness alone is not sufficient for arbitrary gamma. This elementary statement gives a precise meaning to one draft line without completing the unrelated adjunction definition.',
 ['Milne1986Abelian'],['P3-S11'],computation='review.md §Rigidity and primitive torsors.')
claim(286,[63],
 'For a proper geometrically connected A over algebraically closed characteristic-p k, Artin–Schreier gives H^1_et(A,Z/p)=ker(F-1:H^1(A,O)→H^1(A,O)). For arbitrary k the omitted term is k/(F-1)k; over F_p it is F_p and is split off by the origin.',
 'stated without proof','E',
 'Exact sequence checked in Stacks59.63. The reviewer recomputes the H0 term; the bare absolute formula is false over F_p but the geometric version is established. This records a hypothesis repair, not a claimed error in the unspecified original base.',
 ['Stacks0A3J'],['P3-S12'],computation='computations.py finite-field F-1 kernel/cokernel; review.md exact sequence.')
claim(287,[62,64],
 'Artin–Schreier–Witt gives 0→Z/p^r→W_r(O)→W_r(O)→0 in the étale topos. Over an algebraically closed field with the proper connected geometric conventions, its fixed-part H^1 realizes p-power étale cohomology. Passing to a stable W-module and an inverse limit needs explicit transition and continuity conventions.',
 'corrected by himself later','C',
 'The finite-level realization and slope-zero relationship are established in the Witt/Dieudonné theory. Oda1969 gives a primary Picard/Dieudonné comparison and Katz/SGA7XXII develops Frobenius-fixed sheaves. The locally undefined W_infinity and stable subscript prevent an exact identification of every integral limit assertion. The initial stable-part pairing is visibly cancelled, replaced by fixed points.',
 ['Oda1969','SGA7XXII','Stacks0A3J'],['P3-S12'],confidence='medium',computation='review.md §Frobenius fixed versus stable; finite-level diagnostic in computations.py.')
claim(288,[65],
 'For an abelian variety A over algebraically closed k, every connected finite étale cover pointed above zero has a unique abelian-variety structure making it an isogeny. Its geometric pro-ell fundamental group is lim A[ell^r](k); at ell=p only the étale p-torsion contributes.',
 'stated without proof','E',
 'Milne15.3 explicitly states the cover theorem and geometric Tate description, referring to Mumford’s original abelian-variety treatment. Finite, connected and pointed hypotheses have been restored; the arithmetic fundamental group has the additional Galois quotient.',
 ['Milne1986Abelian'],['P3-S13'])
claim(289,[66],
 'The literal statement that a positive-dimensional abelian variety A has no torsion is false: for every ell different from char(k), A[ell](kbar) has ell^{2dim A} points. The likely nearby torsion-free object is NS(A), but that reading is not decided.',
 'false as stated','F',
 'The torsion calculation and torsion-freeness of the classical NS of an abelian variety are standard, and the Weil-pairing description supplies the diagnostic. Only the scan can determine whether A denotes a quotient or whether another letter was written.',
 ['Milne1986Abelian'],['P3-S13'],computation='review.md §Tate and Néron–Severi reading alarm.')
claim(290,[67],
 'For an abelian variety A over k and n prime to char(k), the Poincaré biextension yields a perfect Galois-equivariant pairing A[n](ksep)×A^t[n](ksep)→mu_n; finite-flat Cartier duality states the group-scheme version for arbitrary n. Standard multiplication transitions yield the perfect ell-adic pairing into Z_ell(1).',
 'stated without proof','E',
 'Milne section16 explicitly verifies the finite and inverse-limit pairing, with Lemma16.1 for the transition power. This does not settle the earlier editorial Artin–Mazur sign/equality question, whose two formulas are absent.',
 ['Milne1986Abelian','SGA7VIII'],['P3-S13'],computation='computations.py cyclic symplectic pairing; review.md transition exponent.')
claim(291,[68],
 'Given 0→P′→P→P″→0 in an abelian sheaf topos, nQ=Q and an epimorphism P[n]→P″, a biextension of P×Q by G is proposed to be equivalent to its restriction E′ on P′×Q plus a torsion pairing P[n]×Q[n]→G agreeing with that of E′ on P′[n]×Q[n]. Morphisms must preserve that pairing.',
 'stated without proof','C',
 'The long proof on36:048 is cancelled and its morphism clause is unfinished. SGA7VII is the primary reconstruction comparator; exact printed proposition matching is recorded separately if obtained. Independently verified consequences of the assumptions do not alone prove categorical essential surjectivity.',
 ['SGA7VII'],['P3-S14'],confidence='medium',computation='review.md §Reconstruction: tensor vanishing is proved; the full equivalence is not labelled independently re-proved.')
claim(292,[68],
 'Under the assumptions of C-SA13-291, nP″=0 and P″⊗Q=0. Indeed every local section of P″ locally lifts to P[n], and q locally equals nq′, so x⊗q=nx⊗q′=0.',
 'proof sketched','E',
 'Formal tensor vanishing, independently proved in this run. It is a subsidiary step of the reconstruction argument, not the whole theorem. Searches in SGA7VII verify the surrounding derived-tensor context.',
 ['SGA7VII'],['P3-S14'],computation='review.md §Reconstruction; direct sheaf-local proof.')
claim(293,[71],
 'If colim_{n supported in Pi}P[n]→P″ is an epimorphism and pQ=Q for p∈Pi, the finite reconstruction data must be given compatibly for every n, together with E′. The corollary is about finite pairings before taking limits.',
 'proof sketched','C',
 'This is the manuscript’s all-level reconstruction claim, spanning36:048 and050. SGA7VII supplies the established framework, but exact generality and the excluded module formulation must be matched, not assumed from a similar theorem. The marginal divisibility correction is retained.',
 ['SGA7VII'],['P3-S14'],confidence='medium')
claim(294,[72],
 'For two exact sequences P′→P→P″ and Q′→Q→Q″ with Pi-primary quotients lifted from torsion, the stated assumptions pP=P and pQ′=Q′ permit the one-variable reconstruction first for (P,Q′) and then for (P,Q). Stronger divisibility is needed for a Tate-module-only restatement.',
 'proof sketched','C',
 'The iterative proof route is actually written. Its validity depends on the one-variable equivalence and compatibility of the restrictions. It has not been replaced by the symmetric stronger assumption pP=pQ=P,Q without explanation. The finite-system correction is the reliable surviving scope.',
 ['SGA7VII'],['P3-S14'],confidence='medium')
claim(295,[73],
 'In ordinary abelian groups take P=Z/ell and Q=G=Q_ell/Z_ell. Then lim_r P[ell^r] under multiplication by ell is zero, while Biext^1(P,Q;G)=Hom(Z/ell,G) is nonzero. Thus inverse-limit pairings alone can discard finite torsion biextension data.',
 'open on the pages','E',
 'This is an earlier-run diagnostic, independently re-proved here using P⊗^L Q≃Q[ell][1] and injectivity of G. The nonzero compatible finite pairings are exhibited exactly. It validates the author’s warning, but it is not a general counterexample in every sheaf or pro-category convention.',
 ['Deligne1974HodgeIII','SGA7VII'],['P3-S14'],computation='computations.py: bounded-P transition test and nonzero phi_r(a,b/ell^r)=ab/ell.',authorship='Idea of the earlier Pro run, independently checked here')
claim(296,[75],
 'If internal Hom_gr(A,G)=0 on S, the low-degree local-to-global Ext sequence identifies global Ext^1(A,G) with H^0(S,internal Ext^1(A,G)). This is weaker than vanishing of all pointed maps A→G.',
 'stated without proof','E',
 'The two outer H1/H2 terms of internal Hom vanish; this independently proves the displayed edge isomorphism. Stacks20.43 gives the spectral-sequence comparator. Nothing here lets one forget an extension law without the stronger rigidity condition.',
 ['Stacks0BQP'],['P3-S11'],computation='review.md §Rigidity and primitive torsors.')
claim(297,[75],
 'If every pointed map A_T→G_T is zero for every T→S and e:S→A is the zero section, every map A_T→G_T is constant and f_*G_A=G. The universality is needed, not only vanishing on one set of S-points.',
 'stated without proof','E',
 'Independent proof subtracts the value at the zero section after each base change. This is the precise condition used by the handwritten extension/torsor argument.',
 ['SGA7VII'],['P3-S11'],computation='review.md §Rigidity and primitive torsors.')
claim(298,[77],
 'If f:A→S has a section and f_*G_A=G, the Leray five-term exact sequence splits in degree1: H^1(A,G_A)=H^1(S,G)⊕H^0(S,R^1f_*G_A). The second summand is identified by ker(e^*).',
 'stated without proof','E',
 'Independently proved: e^*f^*=1 on H2 makes H2(S,G)→H2(A,G_A) injective, forcing the transgression to vanish; e^* splits H1. Unique rigidification of torsors additionally needs pointed-map rigidity and is not part of the cohomological splitting alone.',
 ['Stacks0BQP','SGA7VII'],['P3-S11'],computation='review.md §Rigidity and primitive torsors, five-term sequence proof.')
claim(299,[78],
 'Under universal pointed-map rigidity A→G, the forgetful functor from commutative group extensions of A by G to G-torsors on A trivialized at zero is fully faithful between discrete groupoids. Its image consists of primitive classes m^*L=pr1^*L+pr2^*L.',
 'stated without proof','E',
 'The normalized multiplication isomorphism exists for a primitive class and is unique; associativity, symmetry and inverses follow because their defects are pointed maps A^r→G and hence vanish. This independent proof checks the stronger categorical statement on36:052, not just injectivity on cohomology classes.',
 ['SGA7VII'],['P3-S11'],computation='review.md §Rigidity and primitive torsors: full coherence argument.')
claim(300,[80],
 'The defect map L↦m^*L-pr1^*L-pr2^*L has primitive extension classes as kernel. Therefore the sheaf quotient of rigidified torsor classes by extensions injects into the relevant symmetric birigidified torsors on A×A. Identifying this quotient with a classical NS sheaf needs the geometric hypotheses.',
 'stated without proof','E',
 'This is the elementary kernel/quotient step of the Picard/extension formalism developed in SGA7VII–VIII and continued directly on36:054–058. Exact archive endpoint checking is recorded in links.tsv; no arbitrary generalized NS is automatically the classical Pic/Pic0.',
 ['SGA7VII','SGA7VIII'],['P3-S11'],computation='review.md §Rigidity and primitive torsors.')
claim(301,[82],
 'For an algebra E over Q and a nilpotent derivation u, exp(u)=sum u^r/r! is an algebra automorphism. The higher Leibniz rule proves multiplicativity, and exp(-u) is its inverse. The analogous truncated exponential need not be multiplicative in characteristic p.',
 'proved there','E',
 'The computation is already present on the reused printed sheet and is independently redone here. Its earlier ambient characteristic-zero hypotheses are absent from the retained page. Exact bibliographic identification of the reused page98,number316 remains unresolved, so this mathematical result is not attributed to Grothendieck.',
 ['BourbakiLieCandidate'],['P3-S15'],computation='computations.py: factorial Leibniz coefficients, polynomial translation, characteristic-p counterexample.',authorship='Unidentified reused printed Lie-algebra source; not attributed to Grothendieck')
claim(302,[83],
 'For a finite-dimensional Lie algebra over characteristic-zero k and x in its nilradical, ad(x) is nilpotent and exp(ad x) preserves every ideal, since each power of ad x does.',
 'stated without proof','E',
 'The ideal-preservation argument is formal once nilpotence is known; the nilradical Engel property is a standard characteristic-zero Lie result. The reused source’s exact bibliographic identity remains unverified, not inferred from the archive folder.',
 ['BourbakiLieCandidate'],['P3-S15'],computation='review.md §Reused Lie leaf.',authorship='Unidentified reused printed Lie-algebra source')
claim(303,[83],
 'Under a surjection g→h of finite-dimensional characteristic-zero Lie algebras, the image of a Levi subalgebra of g is a Levi subalgebra of h. Quotients of semisimple Lie algebras are semisimple and the solvable radical maps onto the radical.',
 'stated without proof','E',
 'Independently re-proved from the Levi decomposition and the semisimple quotient. This standard fact is not evidence that the unidentified printed leaf was written by Grothendieck. A bibliographic candidate remains explicitly unverified.',
 ['BourbakiLieCandidate'],['P3-S15'],computation='review.md §Reused Lie leaf.',authorship='Unidentified reused printed Lie-algebra source')
claim(304,[85],
 'The inclusion of abelian sheaves on a site into presheaves preserves injective objects because its left adjoint sheafification is exact.',
 'proved there','E',
 'Exact modern match: Stacks21.10.1. The adjunction proof is both written on36:049 and independently checked. No assumption that evaluation of arbitrary sheaves is exact is substituted.',
 ['Stacks03AV'],['P3-S16'],computation='review.md §Čech leaves.',authorship='Reused SGA-style typescript; precise edition/author not established')
claim(305,[85],
 'For q>0 the presheaf U↦H^q(U,F) attached to a sheaf F has zero associated sheaf: cohomology classes become zero locally. Its degree-zero sheafification recovers F.',
 'proved there','E',
 'The injective-resolution proof is standard and explicitly matches Stacks21.10.1–21.10.3. In a resolution a cocycle is locally a boundary because the sheaf complex is exact in positive degree; the resulting cohomology presheaf therefore sheafifies to zero.',
 ['Stacks03AV'],['P3-S16'],computation='review.md §Čech leaves.',authorship='Reused SGA-style typescript')
claim(306,[85],
 'Under the site/slice conventions of the reused text, cohomology of a sheaf evaluated over U is computed by the right derived functors of its section/evaluation functor. The corresponding composite produces the local-to-global spectral sequence shown on the page.',
 'stated without proof','E',
 'The injective-preservation and acyclicity inputs give the standard Grothendieck spectral-sequence construction. Stacks21.10 explicitly supplies the sheaf/presheaf comparison and Čech-to-cohomology map. The exact old edition is not identified from paper reuse.',
 ['Stacks03AV','Grothendieck1957Tohoku'],['P3-S16'],authorship='Reused SGA-style typescript')
claim(307,[84],
 'The Čech H0/plus-type functor on presheaves is left exact, as corrected in the typescript; it need not be right exact. Its right derived functors give the stated Čech cohomology construction with the chosen covering-sieve convention.',
 'corrected by himself later','E',
 'The crossed-out right-exact wording is replaced by left-exact on36:051. Standard sheaf/Čech theory confirms that limits and filtered cover refinements preserve finite kernels. The convention at the empty object is separately recorded; it must not be silently normalized.',
 ['Stacks03AV','Godement1958Candidate'],['P3-S16'],authorship='Reused SGA-style typescript; handwriting correction not separately attributed')
claim(308,[84,86],
 'The chosen Čech cohomology of a presheaf is a filtered colimit over covering sieves of derived section groups on the sieve; comparison with the cited T.F definition needs P(empty)=0. The typescript explicitly warns that a constant presheaf distinguishes conventions.',
 'stated without proof','F',
 'The general Čech/sheaf framework is established, but the exact cited T.F ChapterII§5 Theorem10.2 was not identified from an opened original edition. Godement is a bibliographic candidate only. Thus no exact convention-equivalence is certified beyond the printed conditional statement.',
 ['Stacks03AV','Godement1958Candidate'],['P3-S16'],confidence='medium',authorship='Reused SGA-style typescript')
claim(309,[14],
 'For a finite group of order m, the functions supported at the identity with values1 andm have normalized counting integrals1/m and1, respectively; ordinary counting integrals are1 andm.',
 'stated without proof','E',
 'Elementary normalization calculation, independently repeated. It explains the manuscript’s two Dirac conventions but is an earlier-run interpretation rather than an additional written integral formula.',
 ['SGA7IX'],['P3-S02'],computation='computations.py: Dirac masses for m=1,2,3,7.',authorship='Interpretation of the earlier Pro run, independently checked here')
claim(310,[9],
 'The proposed inclusion of the special/generic torsion kernel into an unramified group, and the anticipated zero-dimensional kernel on36:005, require the missing relative hypotheses and the eta/s reading.',
 'open on the pages','F',
 'SGA7IX kernel and fixed-part constructions were searched, but the exact fibre statement cannot be reconstructed from the editorial fragment. C-SA13-251 certifies the formal kernel equality only; it does not resolve this specialization question.',
 ['SGA7IX'],['P3-S02'],confidence='medium')
claim(311,[41],
 'With nP=P and nQ=0, the canonical Tor boundary identifies Tor1(P,Q) with P[n]⊗Q under the appropriate sheaf hypotheses; the biextension-to-pairing map factors through Hom(Tor1(P,Q),G) in the situation where P⊗Q=0.',
 'proof sketched','A',
 'The typed proof explicitly invokes its preceding equations1.1.3 and1.3.4. Original SGA7VIII1.1.3–1.1.4 and1.3.4, printed pages220–222, provide the Tor and finite-pairing comparison; Deligne10.2.1 supplies the complex formulation; the divisibility and killed-by-n assumptions ensure the degree-zero tensor vanishes. The last compatibility sentence is cut off, so page completeness is not upgraded.',
 ['SGA7VIII','Deligne1974HodgeIII'],['P3-S05'],computation='review.md §Tor boundary; two-term resolution calculation.',authorship='Reused SGA7-style typescript; matched to SGA7 VIII1.1.3–1.1.4 and1.3.4; authorship and date of this physical leaf are not independently inferred.')
