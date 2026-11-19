"""Serialize manually adjudicated Stage 1 records; no keyword classification."""
import csv,json
from pathlib import Path
ROOT=Path('/workspace/scratch/a77a578fa7d4')
OUT=ROOT/'SA12_work/reviews/29a'
PK='MPL_29_049-094'
items=[]; decisions={}
def add(n,src,kind,scans,lines,words,statement,reconstruction,check,reason,corrections=None):
    iid=f'SA12-{n}'
    items.append(dict(id=iid,sources=[f'{PK}#{j}' for j in src],kind=kind,cote=29,scans=scans,
        lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,
        check=check,check_reason=reason))
    for j in src:
        verdict='kept' if j==src[0] else 'merged'
        why=reason if verdict=='kept' else f'Same object or question as {PK}#{src[0]}; '+reason
        if corrections and j in corrections: verdict,why=corrections[j]
        assert j not in decisions
        decisions[j]=(iid,verdict,why)

add(1,[1],'other',[49,60,78,85,89],['Pro 2–31,380–385,1183–1195,1352–1396,1578–1626'],
    'π₁ et Pic^τ birationnels; Revêtements formels étales et th. de Mumford',
    'The retained leaves contain several work streams and reused typescripts, rather than one continuous proof.',
    'The grouping is editorial; neighbouring missing leaves are supplied only where an assigned Codex witness exists.',
    'agrees','The full transcription confirms the separate titles, pagination systems and subject changes.')
add(2,[2],'idea of the earlier run',[85,89,91,93],['Pro 1352–1396,1578–1626,1697–1750,1782–1834'],
    'groupe de Raynaud; Un groupe diagonalisable est réflexif',
    'The earlier run proposes comparisons to LM1 E.11/E.2 and MPL_11_043-058+56 N063/N100; the manuscript itself discusses Raynaud extensions and diagonalizable groups.',
    'The context files and cited external projects are absent; their claims are not imported as proved results.',
    'not on the page','The group-scheme topics are present; the modern project identifiers and their proof statuses occur only in the notes.')
add(3,[3,78],'self-flagged step',[48,50],['Codex K29-01 253–263; Pro 32–91'],
    'je crois; π₁(X_ȳ) → π₁(X) → π₁(Y) → 0',
    'Under the initial flatness/reduced-fibre and connected geometric generic-fibre hypotheses on scan 48, a finite étale cover trivial on that fibre is asserted to descend to a finite étale cover of the normal integral base; the π₁ sequence follows.',
    'The qualifier biréduit/réduit on scan 48 remains undecided. Properness is mentioned in comparison with a different fibre theorem, not securely imposed on this generic-fibre lemma.',
    'agrees','The note rightly refuses to read the continuation alone as a standalone theorem; Codex supplies its initial page, with a material unresolved adjective.')
add(4,[4,79],'unproved claim',[52],['Pro 138–146'],
    'Y loc. noeth. et univ. japonais; f_*(F) est constructible',
    'For a finite-type morphism to a locally noetherian universally Japanese base, the direct image of a constructible sheaf of finite sets is constructible.',
    'Constructibility here is degree zero, not a statement about R¹ or finite generation.',
    'agrees','The exact hypotheses are visible. The incomplete SGA/§A/Standart reference is a reading alert, not an identification.')
add(5,[5],'unproved claim',[52],['Pro 146–160'],
    'l’application … est à fibres finies',
    'For connected noetherian universally Japanese X, a finite locally closed partition X_i, and finite constant G, restriction H¹(X,G)→∏H¹(X_i,G) has finite fibres.',
    'H¹ is the nonabelian torsor set; finiteness of each stratum set then gives finiteness on X.',
    'agrees','The universal-Japanese insertion is retained; the stronger finite-fibre formulation replaces a deleted assumption that the stratum sets were finite.')
add(6,[6],'unproved claim',[52],['Pro 160–165'],
    'Hom(F,G) est fini',
    'The set of morphisms between constructible finite-set étale sheaves on a noetherian scheme is finite.',
    'A common finite connected stratification and geometric stalks give an independent proof.',
    'agrees','The note matches the lemma and its proof mechanism; see independent_checks.md §1.')
add(7,[7],'unproved claim',[54,56],['Pro 199–232,264–282'],
    'Les conditions suivantes sont équivalentes',
    'For a noetherian universally Japanese S and finite G, global H¹-finiteness for every finite-type S-scheme is reduced to smooth affine maps with geometrically connected nonempty fibres over finite étale covers of normal integral affine subschemes of S, and to generic opens of those bases. A sufficient criterion uses geometric fibres and every subgroup H≤G×G on those bases; for abelian G it suffices to use G. Prime-to-residue-characteristic corollaries follow.',
    'The detailed quantifiers are retained in the separate claim records; no replacement by just H¹(S,G) is allowed.',
    'agrees','The notes correctly identify the base-cover and subgroup quantifiers and distinguish equivalence from the sufficient condition.')
add(8,[8],'idea of the earlier run',[54,56,61],['Pro 199–282,386–440'],
    'H¹(X,G) est fini; topologiquement de génération finie',
    'Finiteness of H¹ for each finite target is weaker than topological finite generation of a profinite group.',
    'The product ∏(Z/p_i)^{d_i} with distinct primes and unbounded d_i is an external counterexample to the inference, not a scheme constructed on the pages.',
    'agrees','The two types of statements occur in distinct arguments. The abstract counterexample was independently rechecked.')
add(9,[9],'idea of the earlier run',[56,58,61],['Pro 264–282,318–344,386–440'],
    'ordre premier aux caractéristiques résiduelles',
    'In characteristic p, A¹ has infinitely many Z/p-torsors, so the prime-to-characteristic restriction cannot simply be removed from the affine H¹-finiteness statements.',
    'Artin–Schreier classes x^m with p∤m supply the counterexample.',
    'agrees','The restriction is on the page; the Artin–Schreier computation is the earlier run’s explanatory example, now rechecked.')
add(10,[10],'self-flagged step',[58],['Pro 318–341'],
    'à fibres géom. connexes non vides, de dim 1',
    'The dimension induction requires an appropriate smooth dense-open fibration by geometrically connected curves, followed by treatment of the complement.',
    'A generic projection and shrinking are a proposed completion, not an argument written in full on the page.',
    'agrees','The note identifies the missing geometric construction without replacing the curve-to-variety proposition’s quantifiers.')
add(11,[11,83],'conjecture',[61,64],['Pro 386–440,588–628'],
    'Question; topologiquement de génération finie',
    'For an algebraic scheme over an algebraically closed field of characteristic exponent p, the prime-to-p quotient is claimed finitely generated. A separate question asks finite generation after killing wild inertia at the codimension-one boundary of a proper normal compactification.',
    'The boundary-tame quotient is not identified with the prime-to-p quotient. A later explicit formulation occurs on scan 64.',
    'agrees','The note preserves the difference between the announced prime-to-p theorem and the stronger tame question; Codex disagrees about finite generation versus finite presentation on scan 64.')
add(12,[12],'reading question',[62,64],['Pro 441–531,588–628'],
    'doux',
    'The local boundary condition means tame ramification, not absence of ramification; a prime-to-p Kummer extension is the basic example.',
    'Modern terminology is supplied; the exact ramification-theoretic definition must be attached to the chosen valuation rings.',
    'agrees','Treating doux as étale would erase the inertia which the argument is studying.')
add(13,[13,84,86],'self-flagged step',[62,63],['Pro 441–565'],
    'À détailler',
    'A finite étale cover of U×Y, geometrically tame along the codimension-one boundary after normalization and trivial on a selected fibre, is proposed to descend from a neighbourhood in Y. The passage from normal to nonnormal X is left to descent.',
    'The dense-open, normalization, geometric generic-boundary, and rational-fibre qualifications are not interchangeable. Pro and Codex disagree on properness and theorem/question status.',
    'agrees','The warning is explicit. No completion of the nonnormal descent step is claimed by this review.')
add(14,[14],'idea of the earlier run',[66],['Pro 700–737'],
    'Y′ … de codim ≥2',
    'The attempted Chow reduction does not ensure that the full inverse image of the omitted codimension-two set still has codimension at least two.',
    'The blowup of a point on a smooth surface supplies a counterexample to this inference, not to the target finite-generation theorem.',
    'agrees','The transcribed clause is present and the codimension defect is real; whether it was an extra hypothesis must be decided on the scan.')
add(15,[15,89],'withdrawn in the same text',[67],['Pro 738–747'],
    'connexe ? non',
    'The proposal to replace irreducibility by connectedness in the generic-section argument is rejected on the page.',
    'Two planes meeting in a point provide a modern explicit example.',
    'agrees','Both the question and the answer non are present; this is a local rejected strengthening, not a withdrawal of Bertini.')
add(16,[16],'idea of the earlier run',[67],['Pro 748–760'],
    'k corps; X … irréductible',
    'The arbitrary-field statement needs geometric irreducibility to conclude irreducibility after the indicated algebraically closed generic parameter extension.',
    'P²_C regarded over R refutes the ordinary-irreducibility reading. Later scan 113 explicitly supplies the geometric hypothesis (parent endpoint check).',
    'agrees','The note correctly flags the hypothesis gap; the later witness supplies a mathematical refinement, not an ink correction to scan 67.')
add(17,[17,82,87],'unproved claim',[61,65,67],['Pro 413–440,629–659,761–785'],
    'π₁(X_u) → π₁(X_K) … surjectif',
    'Under normality and geometric irreducibility over an algebraically closed base, a suitable generic complete-intersection section gives a surjection on π₁ by connectedness of pullbacks of finite étale covers.',
    'The connected-cover criterion supplies the exact group-theoretic step; references and deformation to characteristic zero are separately indicated.',
    'agrees','The draft diagrams and the later corollary concern this same section argument; the note correctly keeps normality in the proof.')
add(18,[18],'unproved claim',[68],['Pro 786–805'],
    'au plus 2g générateurs',
    'For a fixed projective normal model and a codimension-two excluded set, a generic smooth projective curve of genus g avoiding that set gives the bound d(π₁(U))≤2g.',
    'The asserted conclusion is a generator bound, not a presentation or a formula for π₁.',
    'agrees','The note matches the numerical bound and its dependence on a fixed curve.')
add(19,[19],'idea of the earlier run',[64,68],['Pro 588–628,786–805'],
    '',
    'The notes reject a contextual claim that positive-characteristic fundamental groups of proper varieties are never known to be finitely presented. Modern results prove finite presentation for smooth projective varieties and subsequently all connected proper schemes over algebraically closed fields.',
    'This is a correction to an earlier context packet, not a new manuscript theorem. Tame good-compactification hypotheses remain distinct from arbitrary boundary quotients.',
    'not on the page','The alleged modern denial is not in the manuscript; the literature correction has exact modern sources and dates.')
add(20,[20],'unproved claim',[69],['Pro 817–878'],
    'codim ≥2; pureté',
    'A rational map from a regular open to a proper normal model is defined away from codimension two; purity handles its regular source, and normality of the target handles surjectivity on π₁.',
    'The two roles are separated in the reconstruction. Pro dominant versus Codex normal remains a material reading disagreement.',
    'agrees','The note’s distinction is needed: normality alone does not justify purity of a singular source.')
add(21,[21],'idea of the earlier run',[69,70],['Pro 817–915'],
    'groupe fondamental birationnel',
    'Fixing one regular open in a projective normal model produces compatible surjections to the fundamental groups of all proper normal models; compactness then gives a surjection to their inverse limit and a finite generator bound.',
    'Using a single source and the compactness argument is an explicit reconstruction of the compressed page.',
    'agrees','The reconstruction repairs the quantifier issue without assuming an unexplained uniform genus on every model.')
add(22,[22,92],'conjecture',[70],['Pro 890–903'],
    'système … essentiellement constant',
    'The system of π₁ of proper normal models is asked to be essentially constant; it is asserted to be so when a proper regular model exists.',
    'A uniform generator bound alone is insufficient, as the cyclic inverse system Z/ℓ^m shows. General geometric stabilization is not settled by that abstract example.',
    'agrees','The conditional result and the unrestricted question are distinct on the page.')
add(23,[23,24,93],'conjecture',[70],['Pro 903–915'],
    'π₁(U) → π₁ birat … isomorphisme ?',
    'For an arbitrary proper normal model X, does the regular locus U have the birational fundamental group, equivalently can each cover of U become étale on a proper modification?',
    'The quotient (P¹×P¹)/±1 over C supplies a counterexample, with an a-adic valuation ramified in K(√a) preventing extension on every proper model.',
    'agrees','The valuation is part of the same counterexample and is merged, not counted as a second question; every hypothesis is checked in independent_checks.md §4.')
add(25,[25,88],'conjecture',[66],['Pro 718–725'],
    'ker … est-il … de génération finie ?',
    'For a proper normal algebraic X and a codimension-two closed Y, is ker(π₁(X∖Y)→π₁(X)) topologically finitely generated?',
    'The exact geometric question is retained; an abstract semidirect product only disproves deduction from finite generation of the surrounding groups.',
    'agrees','The note does not pretend to settle the geometric kernel question with an abstract example.')
add(26,[26],'idea of the earlier run',[68,69,70],['Pro 786–915'],
    '2g',
    'The genus of a complete-intersection curve depends on the projective model and polarization; a uniform birational bound must use a chosen model once.',
    'This is a clarification of the earlier commentary, not a separate authorial genus-invariance claim.',
    'not on the page','No statement on the page declares that this genus is a birational invariant.')
add(27,[27],'idea of the earlier run',[63,65],['Pro 566–587,629–644'],
    'π′₁(X×Y) … π′₁(X)×π′₁(Y)',
    'The full étale product formula fails for A¹×A¹ in characteristic p, as shown by the Artin–Schreier torsor z^p−z=xy; the stated prime-to-p formula is not refuted.',
    'The example is external to the manuscript and constrains a proposed strengthening.',
    'agrees','The note properly distinguishes the prime-to-p isomorphism from the full-product surjection.')
add(28,[28,94],'self-flagged step',[71],['Pro 916–944'],
    'Y … régulier; X normal … sur k ?',
    'For a proper birational map of integral normal proper k-schemes X→Y with Y regular, pullback on Pic^τ is asserted an isomorphism. Margins question geometric normality, smoothness and projectivity.',
    'A clean modern version over an algebraically closed field with Y smooth is separated from the wider written claim; no hypothesis is silently inserted into the transcript.',
    'agrees','The notes appropriately treat the margins as unresolved qualifications, not removable punctuation.')
add(29,[29],'reading question',[71],['Pro 944–952'],
    'Pic(X) → Pic(U)',
    'The displayed restriction map reads Pic(X), although factoriality of Y and the following triangle require Pic(Y)→Pic(U).',
    'Y is a proposed mathematical correction only; both Pro and Codex read X.',
    'agrees','A blowup supplies a nonzero exceptional kernel for Pic(X)→Pic(U); the visible letter is not changed.')
add(30,[30,95,96],'self-flagged step',[71,72],['Pro 952–991'],
    'un lemme bien connu; vérifier ?; insuffisant',
    'A τ-trivial Cartier-divisor combination supported on the exceptional locus of a proper birational map to a regular target is claimed to vanish.',
    'An intersection/negativity argument requires its own hypotheses and a reduction in arbitrary dimension; the word insuffisant has disputed attachment between Pro and Codex.',
    'agrees','The result is announced as known, but the page expressly asks for verification and does not supply the complete argument.')
add(31,[31,97],'idea of the earlier run',[72],['Pro 991–1020'],
    'un isom sur les espaces tangents',
    'Equality of points and tangent spaces of a closed inclusion of proper group schemes does not by itself imply equality of the group schemes.',
    'α_p⊂α_{p²} means successive Frobenius kernels in G_a, with lengths p and p² and one-dimensional tangents; this refutes the bare criterion, not the birational Picard theorem.',
    'agrees','The proposed endpoint needs additional infinitesimal control; the later H¹ argument is recorded rather than omitted.')
add(32,[32],'reading question',[72,73],['Pro 1005–1059'],
    'F^{ν|1}',
    'The Frobenius argument must compare every iterated kernel on the nilpotent part as well as fixed vectors; comparing only ker F is insufficient.',
    'The two-dimensional nilpotent block gives an explicit counterexample to the one-iterate criterion; the exponent’s ink remains unresolved.',
    'agrees','The following repeated p^{ν|1} strengthens the reading question without deciding it.')
add(33,[33],'unproved claim',[73],['Pro 1021–1031'],
    'Le premier hom s’écrit',
    'For proper connected reduced schemes over an algebraically closed field of characteristic p, H¹_et(F_p) is the Frobenius-fixed subspace of H¹(O).',
    'Artin–Schreier and surjectivity of F−1 on k explain the displayed identification; purity is a separate input.',
    'agrees','The qualification supplied by the note is mathematically correct and the long exact sequence was rechecked.')
add(34,[34],'idea of the earlier run',[73],['Pro 1040–1059'],
    'sans torsion',
    'For a normal domain R, R^{1/p^ν}/R is torsion-free, because a root in Frac(R) integral over R lies in R.',
    'This local argument supplies injectivity of restriction from X to its dense open; it does not supply extension on Y.',
    'agrees','The integrality proof is valid and independently repeated.')
add(35,[35],'idea of the earlier run',[73],['Pro 1032–1059'],
    'Y lisse sur k (!)',
    'For regular finite-type Y over a perfect field, the Frobenius root quotient is finite locally free and its sections extend across codimension two.',
    'Kunz plus finiteness of Frobenius and reflexive extension are explicit additional inputs to the page’s triangle.',
    'agrees','Regularity of Y, rather than normality alone, supplies the required surjectivity.')
add(36,[36],'unproved claim',[74,75],['Pro 1060–1092'],
    'coh. plats … en dim 1; Cela prouve r=0',
    'The characteristic-zero H¹ comparison is reduced by spreading out, shrinking to coherent base-change loci and testing the constant-rank cokernel at positive-characteristic fibres.',
    'The model must preserve properness and the geometric hypotheses; the proof is a strategy with these obligations, not a complete certificate.',
    'agrees','The source is more precise about cohomological flatness than the modern context summary.')
add(37,[37],'unpursued implication',[75],['Pro 1092–1112'],
    'le système … inductif est essentiellement constant',
    'Conditional on the scheme-level birational Pic^τ theorem, a fixed proper smooth model gives a cofinal family of models with identical Pic^τ.',
    'Normal graph closures supply the cofinality argument. This is conditional on the theorem, not an independent repair of all its gaps.',
    'agrees','The note keeps the smooth-model hypothesis and explains its role.')
add(38,[38,98],'conjecture',[75],['Pro 1112–1124'],
    'Question; (i) … (ii) … (iii)',
    'Without assuming a smooth proper model, the author asks stabilization of Pic^τ along normal models and proposes bounds on dimension, torsion and h¹(O) as a criterion.',
    'The chain α_{p^m} shows that dimension, geometric-point torsion and tangent dimension do not control infinitesimal length in arbitrary group schemes. Whether torsion meant group-scheme length must be checked.',
    'agrees','The abstract counterexample attacks the numerical inference; the special geometry of the birational system is not settled by it.')
add(39,[39],'idea of the earlier run',[76],['Pro 1125–1155'],
    'dim Pic = 1/2 rang …',
    'The half-rank formula requires a prime ℓ different from char(k); using ℓ=p fails for a supersingular elliptic curve.',
    'The smooth curve y²=x³−x over F₃ has four rational points and p-rank zero, while dim Pic⁰=1. This refutes the unrestricted formula, not the dimension bound.',
    'agrees','No ℓ≠p qualification is visible in the supplied display; it is retained as a refinement and a scan question.')
add(40,[40],'idea of the earlier run',[76],['Pro 1140–1155'],
    'rang',
    'Kummer theory identifies T_ℓ Pic with H¹_et(Z_ℓ(1)), hence with Hom_cont(π₁^ab,Z_ℓ(1)), rather than directly with π₁^ab.',
    'The dual and twist do not alter the rank but matter for functorial identifications.',
    'agrees','The note corrects a contextual identification while preserving the manuscript’s numerical argument.')
add(41,[41],'idea of the earlier run',[76],['Pro 1130–1145'],
    'K⊗_k k̄',
    'Geometric normality alone does not make this tensor product a field; geometric integrality or a chosen geometric component is needed.',
    'Spec C over R gives C⊗_R C≅C×C, meeting geometric normality but disproving the field inference.',
    'agrees','The historical meaning of normal sur k and constant-field assumptions remain reading/context questions.')
add(42,[42,99],'conjecture',[77],['Pro 1156–1182'],
    'démonstration directe ???',
    'Can one bound the dimensions of Picard schemes of all proper normal models of a fixed function field directly by a fixed generic curve’s genus, without the π₁ argument or assuming properness of Pic^τ as input?',
    'Restriction to a curve and the classical Albanese/Picard variety furnish a precise modern comparison; infinitesimal Picard structure is not controlled by this dimension bound.',
    'agrees','The note’s Kleiman comparison is relevant but does not itself prove the exact all-model statement.')
add(43,[43],'unpursued implication',[75,76,77],['Pro 1112–1182'],
    '(i) résulte de (iii)',
    'The dimension of the Picard scheme is at most its tangent dimension h¹(O), so a uniform h¹ bound implies a dimension bound; the converse and stabilization do not follow.',
    'This is a general local-dimension inequality, separated from the author’s stronger hopes.',
    'agrees','The implication is correct; the three outputs are not collapsed.')
add(44,[44,102],'self-flagged step',[82],['Pro 1210–1240'],
    'descent; champ',
    'The editorial notes ask for fppf/fpqc descent of tame coverings and an associated étale stack.',
    'Pro reads fppf and Codex fpqc. Neither root stacks nor logarithmic geometry occur as named constructions on this page.',
    'agrees','The stack language is explicit, while links to later theories are contextual comparisons.')
add(45,[45],'self-flagged step',[82],['Pro 1230–1250'],
    'equations',
    'The notes ask for local Kummer equations for divisors and their compatibility under gluing.',
    'The ambient categories and ordinary/generalized Kummer conventions must be read with Murre’s letter, not guessed from the word equations alone.',
    'agrees','The request is present and matches the letter’s missing generalized-Kummer characterization.')
add(46,[46,101],'self-flagged step',[82],['Pro 1235–1260'],
    'Lefschetz',
    'A tame-covering Lefschetz variant is requested; modern exact comparisons require regular projective X, a normal-crossings boundary and a transverse ample section.',
    'Esnault–Kindler supplies a precise regular/SNC theorem, not every possible formulation of the short editorial request.',
    'agrees','The note correctly keeps the comparison’s hypotheses; the separate local prime-to-p request is cross-referenced to SA12-47.')
add(47,[47],'withdrawn in the same text',[82],['Pro 1235–1260'],
    'tame [deleted]; prime to p [inserted]',
    'A local finite-generation target is narrowed from the tame group to its prime-to-p quotient.',
    'The local geometric setting is too abbreviated for a single unqualified theorem; the cancellation changes the requested strength.',
    'agrees','The changed qualifier is substantive and must not be restored from the stronger deleted word.')
add(48,[48,76,106],'reading question',[84],['Pro 1305–1340'],
    'specialization paths',
    'A specialization path is described by a chosen lift of a geometric generization to a strict localization; the direction of the resulting stalk map must be fixed.',
    'The proposed product-of-fields description requires hypotheses on the generic fibre; the note reports a reversed description in external commentary, whose endpoint is absent.',
    'agrees','The source’s diagram supports the lift direction, not an unqualified inverse description.')
add(49,[49,105],'self-flagged step',[84],['Pro 1280–1305'],
    'equivalence of categories anyhow!! to check',
    'An equivalence between the chapter-VII categories is guessed and explicitly left to check.',
    'The categories are not defined in these leaves; no modern theorem is substituted for them.',
    'agrees','The check instruction is explicit; this remains unidentifiable at theorem-level from the present pages.')
add(50,[50,107],'self-flagged step',[86],['Pro 1397–1418'],
    'must be trivial',
    'Gluing quasi-coherent modules and testing finite type/presentation/local freeness on the pieces is asserted; a finite flat cover should be tame exactly when its restrictions are tame.',
    'The ambient gluing square and its hypotheses are absent, so these claims are conditional reconstructions, not universal descent assertions.',
    'agrees','The note correctly highlights omitted ambient assumptions rather than declaring the assertion false.')
add(51,[51,108],'withdrawn in the same text',[87],['Pro 1419–1459'],
    'Il faudrait vérifier',
    'A cancelled draft considers inverse image of quasi-coherent stratified modules and a lifting/compatibility step involving an unresolved abbreviation m.u. and unramified maps.',
    'Unramified objects are not uniquely deformable; formal unramifiedness only gives uniqueness for maps to a fixed target. The draft’s exact claim cannot be reconstructed securely.',
    'agrees','The page is cancelled and the verification request survives within it. Neither the abbreviation nor cancellation is silently resolved.')
add(52,[52,80,122],'other',[49,51,53,55,57,59],['Pro 2–31,92–137,170–198,233–263,283–317,345–379'],
    'N° 385; Distributions',
    'The reused sheets develop finite-order point-supported distributions, modules, tensor products, tangent vectors and coordinate change; their printed pages occur out of order.',
    'The writer, source publication and date are not identified by N°385. Bourbaki talk 385 is a different work and is not assigned here.',
    'agrees','The complete six-sheet reading confirms the reversed pagination and a placeholder reference; reuse does not constitute retraction.')
add(53,[53],'idea of the earlier run',[49,51,53,55,57,59],['Pro 2–31,92–137,170–198,233–263,283–317,345–379'],
    '(f.μ)×(g.ν)=(f×g).(μ×ν)',
    'Dual finite jet algebras explain the module, comultiplication, external-product, tangent-space and projection formulas in the typescript.',
    'Finite jets are a modern explanatory reconstruction. The ambiguous C^r order symbol is not repaired by choosing the convenient smoothness class.',
    'agrees','The algebraic identities were independently checked; finite-order tensor products require a total-order filtration.')
add(54,[54,123],'other',[83,85],['Codex C29-04 31–40; Pro 1352–1396'],
    'groupe de Raynaud; T₀ isotrivial',
    'A formal semiabelian object is algebraized into a Raynaud extension, with completion isomorphism and functorial adic base change; the reused continuation discusses torsor/extension algebraization and normality of the base.',
    'The whole-page crossing is evidence of reuse, not a substantive withdrawal. A^natural/A^sharp and a B/A completion splice remain reading questions.',
    'overstates','The named object changes in place, and the inserted isotriviality assumption must be retained. The note’s withdrawn classification is too strong for a reused typescript.',
    corrections={54:('corrected','The crossed reused Raynaud sheet is not established as a substantive withdrawal. Retain the internal revisions and classify it as a reused typescript; exact published counterpart SGA7IX7.2.2–7.2.6 confirms the continuing construction.')})
add(55,[55],'unproved claim',[89,91],['Pro 1578–1626,1697–1750'],
    'Un groupe diagonalisable est réflexif',
    'The sheets define D_S(M), establish character duality and biduality, and discuss representability of Hom under finite-generation assumptions.',
    'These are exact textual counterparts of SGA3 VIII §§1–2; blank typed operators are not supplied in the transcription.',
    'agrees','The published counterpart is identifiable at proposition level, including a later editorial expansion of the Hom proof.')
add(56,[56,72],'idea of the earlier run',[88,89,91,93],['Pro 1460–1577,1578–1626,1697–1750,1782–1805'],
    'n éléments; premier à p',
    'A finite diagonalizable group D(T) has scheme length |T|, while its geometric point count equals |T| only away from the residue characteristic; tame finite inertia coefficients are thus prime-to-p.',
    'The example μ_p has one geometric point but length p. The formal-coefficient crosslink is explanatory, not evidence that all profinite cohomology limits are harmless.',
    'agrees','The duplicated finite-inertia observation is merged with the exact group-scheme distinction.')
add(57,[57],'unproved claim',[93],['Pro 1805–1834'],
    'Théorème 3.1',
    'An exact sequence of abelian character groups dualizes to an fpqc-exact sequence of diagonalizable group schemes, with the right map faithfully flat and quasi-compact.',
    'The free group-algebra basis on coset representatives proves the flatness statement directly.',
    'agrees','The note and published SGA3 VIII 3.1 agree; the independent algebra check does not depend on missing display operators.')
add(58,[58],'unpursued implication',[88],['Pro 1460–1536'],
    'opère … via … μ',
    'Prime-to-p tame inertia is a quotient of the roots-of-unity module, with cyclotomic conjugation action of the base fundamental group.',
    'A noncentral S₃ tame extension over F₂((t)) demonstrates why this is a module extension, not automatically a central extension.',
    'agrees','The action is part of the written setup; the counterexample only rejects a centrality shortcut.')
add(59,[59],'reading question',[88],['Pro 1460–1480'],
    'U=X₀−D′₀',
    'The base U is the open subset of the special divisor X₀ obtained by removing the induced other boundary components.',
    'It is not the complement of X₀ in the formal scheme, whose underlying topological space is X₀.',
    'agrees','The displayed definition makes the distinction explicit.')
add(60,[60],'unproved claim',[88],['Pro 1537–1577'],
    'H¹(Ũ^t,J)=0',
    'For a finite constant prime-to-residue-characteristic coefficient group J, H¹ vanishes on the tame universal pro-cover because each torsor is killed at a finite tame stage.',
    'Extension to profinite I requires continuous cohomology and inverse-limit hypotheses; the finite-torsor proof alone does not give them.',
    'agrees','The note identifies the exact finite-coefficient scope of the argument.')
add(61,[61],'idea of the earlier run',[88],['Pro 1544–1568'],
    'courbes',
    'An unqualified vanishing of all higher cohomology on the tame universal cover of every smooth curve fails for P¹.',
    'For n invertible, π₁(P¹)=1 and H²(P¹,μ_n)=Z/n. The margin may intend affine or positive-genus curves; ink/context must decide.',
    'agrees','The example checks every geometric hypothesis of the unqualified curve reading without claiming the margin’s intended domain is known.')
add(62,[62],'idea of the earlier run',[90],['Pro 1627–1696'],
    'μ₀/Im π₂^t(U)',
    'For X₀=P¹ and normal degree d, the proposed π₂ quotient predicts prime-to-p cyclic inertia of order the prime-to-p part of |d| when d≠0, and infinite procyclic inertia when d=0.',
    'This is an illustrative deduction conditional on the tame homotopy identification, not a separate computation performed on the page.',
    'agrees','The zero-degree case is essential and was checked explicitly.')
add(63,[63,109],'self-flagged step',[88,90],['Pro 1520–1536,1627–1655'],
    'α=?; ρ(α)=σ(β)',
    'The extension class of the formal tame inertia sequence is to be identified with the restriction/pushforward of the Kummer Chern class of the normal bundle.',
    'Finite-level Čech roots establish the comparison with a fixed sign convention; normal versus conormal notation is a scan question.',
    'agrees','The question and later proposed formula are the same task, and are merged.')
add(64,[64],'idea of the earlier run',[90],['Pro 1655–1696'],
    'π₂^t',
    'Vanishing of π₂ does not imply that the inertia extension splits: the class may remain nonzero in H² of π₁.',
    'A degree-one line bundle on a complex elliptic curve gives a nontrivial Heisenberg-type extension, checked through finite quotients. The later endpoint scan96, read for Stage5, explicitly asserts triviality; formal_elliptic_nonsplitting.md checks a finite tame algebraic covering and its completion.',
    'agrees','Within scans88–94 the note tests an implication; actual later scan96 makes the false splitting assertion explicit. Root owns that later claim and the cross-package merge.')
add(65,[65],'unpursued implication',[92],['Pro 1751–1778'],
    'déjà … à un … fini',
    'A fixed class with a fixed finite coefficient quotient vanishes at some finite tame cover if it vanishes in the filtered limit.',
    'The finite stage depends on the coefficient quotient. One finite cover cannot generally kill all levels simultaneously.',
    'agrees','The exact finite quantifier is necessary for the intended construction.')
add(66,[66],'withdrawn in the same text',[94],['Pro 1835–1862'],
    'β₀=nγ₀+Σ λ_i β^i',
    'Divisibility of the normal-bundle class on U implies divisibility on X₀ modulo the classes of the boundary divisors, rather than ordinary divisibility in Pic(X₀).',
    'For regular X₀ this follows from divisor localization and does not require the boundary divisors to be pairwise disjoint. Other proof steps may still do so.',
    'agrees','The deleted stronger inference and inserted boundary sum are both retained.')
add(67,[67,74],'idea of the earlier run',[94],['Pro 1860–1889'],
    'uniquement divisibles par n',
    'The unrestricted assertion that the Picard kernel of a thickening or the indicated nonproper formal thickening is uniquely n-divisible is false, even with n invertible.',
    'The explicit E×G_m deformation gives ker Pic=H¹(O)/Za and a/n mod Za as nonzero n-torsion. The same defect affects the opened Stacks tag 0C6S statement; it is not accepted as background.',
    'agrees','The earlier-run warning was independently reconstructed, including exact global units, the boundary image and the formal version. No novelty claim is made.')
add(68,[68],'idea of the earlier run',[94],['Pro 1860–1889'],
    'β₀=nγ₀',
    'A specified nth-root pair of a fixed line bundle lifts across a nilpotent thickening when n is invertible, despite failure of unique divisibility of the whole Picard kernel.',
    'This corrected route uses invariance of the étale μ_n-gerbe/root groupoid or nth roots on principal units; effectiveness at the formal inverse limit is separate.',
    'agrees','The distinction repairs the relevant existence mechanism without endorsing the false unrestricted uniqueness statement.')
add(69,[69],'idea of the earlier run',[94],['Pro 1860–1889'],
    'Pic(𝔛)=lim Pic(𝔛_n)',
    'Identification of Pic of a formal scheme with the inverse limit of Pic of its thickenings needs a justification controlling compatible isomorphisms and the possible lim¹ of global units.',
    'Properness and a Mittag–Leffler condition in Lipman’s setting are a sufficient comparison, not a hypothesis present in this general formal setup.',
    'agrees','The inverse-limit issue is logically independent of the finite-level Kummer lifting argument.')
add(70,[70,111],'self-flagged step',[90,92,94],['Pro 1655–1696,1751–1781,1835–1889'],
    'J₀ apparaît comme groupe d’inertie',
    'The reverse inclusion in the proposed inertia kernel formula requires realizing every finite quotient of μ/Imπ₂ as tame inertia after a suitable finite cover.',
    'The Chern calculation gives one containment; realization, descent, formal effectiveness and the disjointness hypotheses are additional steps.',
    'agrees','The note refuses to identify the proved containment with the complete realization theorem.')
add(71,[71,110,113,114],'self-flagged step',[90,94],['Pro 1670–1682,1860–1889'],
    'à vérifier si ceci est indispensable; à vérifier en détail; dégager un lemme',
    'The disjointness of the boundary and the final formal-Picard/realization argument are expressly left for checking; a clean lemma is still to extract.',
    'The root-pair replacement is this review’s refinement. A local correction in the Picard step does not settle disjointness throughout the proof.',
    'agrees','All explicit reservations remain attached to the relevant steps; the text is not represented as a finished proof.')
add(73,[73],'other',[88,90,92,94],['Pro 1460–1577,1627–1696,1751–1781,1835–1889'],
    '',
    'The sequence, two cohomology classes, and formal-neighbourhood construction have a close published counterpart in Grothendieck–Murre (1971).',
    'A verified table of contents identifies the work, but exact theorem-level settlement requires the corresponding text and its hypotheses; a bibliographic match is not a reproof.',
    'agrees','The earlier note correctly limits the strength of its comparison.')
add(75,[75],'reading question',[82],['Pro 1260–1266'],
    'Normality assumption more natural',
    'Pro’s more natural, Codex’s over integral, and an external commentary’s unnatural differ materially.',
    'No reading is chosen without the scan; the context packet is not an authority over the supplied transcription.',
    'agrees','The disagreement is retained as a high-priority reading question.')
add(77,[77,112],'reading question',[92],['Pro 1779–1781; Codex K29-06 scan92'],
    '… est faux [all words unsure]',
    'The faint margin has no secure reading or referent and cannot establish retraction of the inertia argument.',
    'Codex instead reads a statement that composites of tame coverings remain tame; neither reading is imposed.',
    'agrees','The very low-confidence fragment is not converted into a mathematical verdict.')
add(81,[81],'conjecture',[58],['Pro 341–344'],
    'Prop ? … courbe … lisse',
    'If every smooth algebraic curve over a field k has finitely many finite étale covers of each degree, does the same hold for every finite-type k-scheme?',
    'This is a fieldwise finiteness reduction, distinct from the geometric curve-fibration step in SA12-10.',
    'agrees','The question mark and the full all-curves/all-finite-type quantifiers are retained.')
add(85,[85],'reading question',[62],['Pro 470–520'],
    'Quid ?; Si on sait',
    'Cancelled and conditional fragments on the tame fibre question record revisions, but do not securely define additional independent conjectures.',
    'They are retained as part of the textual history, with ambiguous attachment rather than a fabricated final formulation.',
    'agrees','The notes correctly preserve the cancelled layers and avoid settling their order.')
add(90,[90],'self-flagged step',[67],['Pro 779–785'],
    'section … spéciale',
    'A connectivity theorem is suggested for replacing the generic curve section by a suitable special section.',
    'A proper normal setting and the actual connectivity theorem are required; SGA1 X 2.10–2.11 is an exact subsequent comparison.',
    'agrees','This is separate from merely proving generic-section surjectivity.')
add(91,[91],'idea of the earlier run',[70],['Pro 879–887'],
    'comme groupe alg. …',
    'The author wonders whether to introduce the birational fundamental group as a group object in another algebraic formulation.',
    'The adjective lié/lin and the intended category are unresolved; no modern tannakian or proalgebraic replacement is asserted as his meaning.',
    'agrees','The short suggestion has too little mathematical specification for a unique theorem.')
add(100,[100],'reading question',[82],['Pro 1196–1215'],
    'I don’t understand …',
    'The review sheet contains questions about an implication and possible copied notes, with unclear reference targets.',
    'These are editorial reservations, not identifiable mathematical counterexamples.',
    'agrees','The uncertainty is preserved without assigning the words to a theorem not defined here.')
add(103,[103],'self-flagged step',[82,84],['Pro 1267–1274,1340–1351'],
    'Abhyankar lemma',
    'The editorial notes ask where Abhyankar’s lemma is stated and how its consequences should be used in the formal-covering exposition.',
    'The standard local Kummer theorem is identifiable, while the exact missing application depends on the reviewed manuscript’s numbering.',
    'agrees','Both occurrences ask for explanatory placement, not a new assertion that tame ramification is absent.')
add(104,[104],'reading question',[84],['Pro 1275–1295'],
    'What does this mean?; superfluous?',
    'Chapter-VI material is queried for meaning and possible redundancy.',
    'The missing chapter text prevents theorem-level identification; these reservations are not merged into the separate categorical equivalence.',
    'agrees','The editorial questions are explicit and their exact objects remain unspecified.')

# Pagination and title records are deliberately not mathematical claims.
page_rows=[
(115,[60],'Pro 380–385','π₁ et Pic^τ birationnels','The title joins the birational fundamental-group and Picard work; it gives no publication date.'),
(116,[68,70,71,76],'Pro 786–816,879–976,1125–1155','groupe fondamental birationnel; Pic','Marginal headings label subarguments within the alphabetic manuscript sequence.'),
(117,[78],'Pro 1183–1195','Revêtements formels étales et th. de Mumford','The live cover title and the cancelled earlier π₁/étale-sheaf title are distinct textual layers.'),
(118,[50,52,54,56,58],'Pro 32–91,138–169,199–232,264–282,318–344','II; III; IV; V; VI','Roman labels identify a continuation whose initial page I is recovered at Codex scan48; they are not an author-declared total.'),
(119,[61,62,63,64],'Pro 386–628','1; 2; 3; 4','Arabic labels follow the birational cover; the physical leaves and the pagination are separately recorded.'),
(120,[66,67,68,69,70,71,72,73,74,75,76,77],'Pro 700–1182','A … L','The alphabetic sequence is recorded without inferring an independent authorial count.'),
(121,[88,90,92,94],'Pro 1460–1577,1627–1696,1751–1781,1835–1889','1; 2; 3; 4','The formal-neighbourhood manuscript begins another numbering sequence, interleaved with typescripts.'),
(124,[82,84,86],'Pro 1196–1351,1397–1418','I; IV; VI; VII; VIII; IX','Chapter/page numbers in the English comments refer to the reviewed work, not archive foliation.'),
(125,[49,50,94],'Pro scanpage macros throughout','49 … 94','Archive scan numbers and apparent foliation are separate from authorial pagination; retained range gaps are not lost pages established by this review.'),
(126,[49,94],'Pro 1–1889','','No explicit author-declared total for the complete dossier is established by these retained leaves.')]
for n,sc,ln,w,st in page_rows:
    add(n,[n],'title, date or page count',sc,[ln],w,st,'Editorial inventory only; no theorem is inferred from numbering.','agrees','The complete page sequence and headers were compared with the notes.')
for n,subject in [(127,'birational fundamental groups'),(128,'Picard schemes'),(129,'formal neighbourhoods')]:
    add(n,[n],'other',[],['Pro notes bibliography headings 719–801'],'',
        f'The earlier run’s bibliography for {subject} is retained as a reference register, not as an authorial claim.',
        'Every citation used in this review has its own opened-URL verification scope; unavailable project citations remain unverified.',
        'not on the page','This indexed entry is bibliographic apparatus written by the earlier run, not text in the manuscript.')

# Codex-only supplements take no NOTES_INDEX verdict rows.
add(130,[],'other',[79],['Codex A29-01 143–171'],'Voorschoten 30-4-69',
    'Murre sends Grothendieck a preliminary version expanding the formal tame notes and plumbing; a chapter parallel to Mumford’s work remains unwritten.',
    'The writer is Murre, not Grothendieck; the letter supplies a circulation date for this draft, not a date for all manuscript leaves.',
    'agrees','This missing Pro page was read in the assigned Codex witness.')
add(131,[],'self-flagged step',[80,81],['Codex A29-01 172–230'],'2.1.8; 7.1.5; 9.3.3',
    'Murre asks for a generalized-Kummer algebra characterization, points out the ordinary-Kummer restriction in the formal lifting argument, and traces the disjoint-boundary assumption to that restriction.',
    'The exact unpublished chapter numbering is retained; the published numbering must be separately matched.',
    'agrees','These are authorial reservations in the accompanying letter and directly illuminate scans82–94.')
add(132,[],'self-flagged step',[80,81],['Codex A29-01 172–230'],'3.5.5; 3.6.5; 7.1.6; 8.1.6; 9.2.3',
    'Murre lists a proof only indicated, a delicate geometric realization, a canonical-isomorphism assertion, and a missing proof of the two-class comparison said to be explicit in a letter to Giraud.',
    'The absent Giraud letter is not counted as checked; each identifiable claim is separated in the claims map.',
    'agrees','The correspondence records work still required in the preliminary draft.')
add(133,[],'unproved claim',[83],['Codex C29-04 31–40'],'7.6.3; S normal',
    'The reused continuation asserts algebraization of coherent systems of finite-flat torsors and group extensions, with functorial base change; extension to a noetherian adic base depends on algebraizing the formal abelian quotient, possible under normality.',
    'The initial theorem hypotheses are outside this fragment; its assertion is not generalized to arbitrary nonproper formal schemes.',
    'agrees','The extra page is connected to the Raynaud sheet by its objects and numbering, not by physical adjacency alone.')

with (ROOT/'source/SA12_notes/NOTES_INDEX.tsv').open() as f:
    indexed=[r for r in csv.DictReader(f,delimiter='\t') if r['package']==PK]
assert len(indexed)==129
assert set(decisions)==set(range(1,130)),sorted(set(range(1,130))-set(decisions))
with (OUT/'entries.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['entry_id','item_id','verdict','reason'])
    for r in indexed:
        j=int(r['entry_id'].rsplit('#',1)[1]);w.writerow([r['entry_id'],*decisions[j]])
(OUT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print('Manual Stage 1 records:',len(indexed),'entries;',len(items),'items; all entry IDs unique and covered.')
print('Verdicts:',{v:sum(t[1]==v for t in decisions.values()) for v in sorted({t[1] for t in decisions.values()})})
