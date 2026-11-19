"""Serialize manually authored source judgments for Codex-only early cote84.
No verdicts are inferred from headings. Quotes are literal extracts at hand-selected
source locations. The reviewed prose below, not a classifier, supplies each claim.
"""
import csv,datetime,json
from pathlib import Path
W=Path(__file__).resolve().parents[1]; S=W.parent/'source/SA02_texts/codex'
O=W/'parts/root_early';O.mkdir(parents=True,exist_ok=True)
claims=[]
def add(n,f,scans,lines,quote,statement,status,calc,cls,fate,refs,search,proof,confidence='high'):
 name=f'K84-{f:02d}_transcription.tex';raw=(S/name).read_text().splitlines()
 excerpt='\n'.join(raw[quote[0]-1:quote[1]]).strip()
 claims.append(dict(id=f'CL-SA02-{n:03d}',items=[],cote=84,scans=scans,
  lines=[dict(file='SA02_texts/codex/'+name,start=lines[0],end=lines[1])],
  his_statement=excerpt,statement=statement,status_on_pages=status,
  computation=dict(program='programs/root_computations.py',output='outputs/root_computations.json',certificate_ids=calc,independent_argument='evidence/root_proofs.md#'+proof.lower().replace(' ','-')),
  **{'class':cls},fate=fate,fate_date=dict(first_circulation='See exact reference dates in SA02_references.bib; undated manuscript pages do not establish priority.',assessment='2026-11-19'),
  present_status='As of 19 November 2026: '+fate,refs=refs,confidence=confidence,
  search_ids=[search],source_quote_lines=dict(start=quote[0],end=quote[1]),attribution='Source claim; modern statement and independent argument are this run’s reconstruction.'))

add(700,1,[2,3],[8,257],[60,77],
 'The parity-graded multiplication obtained from commutative monoids R0,R1 and maps alpha,beta is associative when beta(alpha(x)u)=x beta(u) and alpha(beta(u))=u alpha(beta(1)); the concrete discriminant/parity model satisfies these identities.',
 'proved there',['R01-000','R01-001','R01-010','R01-011','R01-100','R01-101','R01-110','R01-111'],'D',
 'The formal algebra is verified independently. Searches of quadratic-algebra monoids, Clifford/Arf references and author bibliographies found related constructions but no exact publication of this two-sort presentation; this is a bounded negative search, not a novelty claim.',
 ['Voight2016','BichselKnus1994'], 'SR-ROOT-01','P01', 'medium')
add(701,1,[2],[112,170],[146,164],
 'A degree-reindexed graded monoid can be normalized by powers of a chosen odd element; negative powers require invertibility. The displayed c1/Arf normalization is formal and does not yet define a general invariant of quadratic bundles.',
 'open on the pages',['R02'],'F',
 'The intended higher-rank invariant is not determined by these formulas. Classical and generalized Clifford/Arf theories were located, but their hypotheses cannot identify the unfinished normalization uniquely.',
 ['BergeMartinet1985','BichselKnus1994'],'SR-ROOT-01','P01','medium')
add(702,1,[4],[269,332],[278,297],
 'For three algebras R[ui]/(ui²+ci), seven nonzero exponent vectors and seven planes in F2³ give the displayed rank2 and rank4 subalgebras. The monomial tensor decomposition is an isomorphism when all ci are units. Equating this condition with étaleness additionally requires2 invertible; fixed-ring descriptions by sign involutions fail unchanged in characteristic2.',
 'false as stated',['R03','R04'],'C',
 'The monomial statements are elementary and checked. The unqualified étale/fixed-ring gloss is false; the corrected étale interpretation is standard finite étale algebra theory. No unrestricted extension is supported.',
 ['Voight2016','TateOort1970'],'SR-ROOT-01','P01')
add(703,1,[6],[352,402],[371,393],
 'For an étale quadratic algebra, u↦u/bar(u) has the usual norm-one torsor interpretation. It is not a surjection of fppf sheaves for every quadratic algebra: in characteristic2 dual numbers have bar=id but nontrivial norm-one elements1+bε.',
 'false as stated',[],'C',
 'The étale Hilbert90 statement is established. The broad nonétale version is refuted here; it must not be conflated with the different fppf exact sequence of the norm morphism.',
 ['StacksKummer','TateOort1970'],'SR-ROOT-03','P03')
add(704,1,[9,10,11,12],[420,514],[472,486],
 'Scalar similarity classes are identified with cyclic submodules locally; faithfulness means a zero annihilator, while universal faithfulness of a line in a finite locally free module is the primitive/unit-ideal condition.',
 'proof sketched',[],'E',
 'This is elementary local module algebra; the direct proof is supplied. Modern primitive-form statements use precisely the stronger condition, not merely a zero annihilator. No composition date is inferred from the classification E.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(705,1,[12,13,14,15,16,17,18],[516,742],[527,541],
 'For rank2 E there is a natural exact sequence O→End(E)→Sym²(E∨)⊗det(E), u↦(x↦x∧u(x)). The opposite wedge order reverses its sign. The source’s quotient and dual-line descriptions must respect this value line.',
 'proved there',['R05'],'B',
 'The rank2 construction is independently verified by coefficients and is compatible with Wood’s global binary-form/algebra correspondence after dualizing the module convention. The formula in the transcription has an unresolved wedge-order sign alarm.',
 ['Wood2011','Wood2009','BichselKnus1994'],'SR-ROOT-02','P02')
add(706,1,[13,14,15],[545,633],[618,630],
 'An O-submodule generated locally by1 and one endomorphism of a rank2 module is a subalgebra, by the degree2 Cayley–Hamilton identity; when the generators are independent it is a quadratic algebra.',
 'proved there',['R06'],'E',
 'Cayley–Hamilton proves the claim over every commutative ring. The modern correspondence confirms the construction but does not create the elementary identity.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(707,1,[14,15,16],[595,660],[633,652],
 'The wedge form is primitive exactly when its quadratic algebra acts on E as on an invertible module; locally this is equivalent to existence of a cyclic vector. No characteristic restriction is needed.',
 'proof sketched',[],'B',
 'Wood2011 Theorem1.5 proves the primitive/invertible-module correspondence over arbitrary schemes (already in Wood2009, Theorem2.1.4). The explicit source construction agrees after the duality convention checked here.',
 ['Wood2011','Wood2009'],'SR-ROOT-02','P02')
add(708,1,[16,17,18],[659,742],[666,674],
 'The value line in the duality formula is determined by Sym²(E∨)⊗det(E); dualizing an auxiliary line in the wrong direction gives a different bundle. The source has incompatible formulas and a separately flagged wedge sign.',
 'false as stated',['R05'],'C',
 'The type-correct formula is fixed by the natural tensor construction; whether the conflicting display is authorial or transcriptional is undecided without scans. Wood’s conventions provide a checked comparator, not an ink decision.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(709,2,[19],[5,40],[9,20],
 'For a binary form αx²+βxy+γy² the discriminant is β²−4αγ and equals minus the determinant of its polar pairing; a form valued in J has discriminant valued in J²⊗det(E)^−2.',
 'proved there',['R07'],'E',
 'The coefficient identity is checked universally and agrees with Wood2011 Theorem1.6. The earlier transcribed positive determinant-line exponent is a type error to inspect on ink.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(710,2,[20,21,22,23],[65,195],[168,189],
 'Every line-valued binary form has a canonical quadratic algebra obtained by the End(E)/O pullback construction; locally u²−βu+αγ=0 with u acting as[[0,−γ],[α,β]]. Its norm is the determinant. The zero form yields dual numbers with trivial nilpotent action.',
 'proved there',['R08','R09','R10'],'B',
 'Wood2011 Theorems1.4 and2.1 give the arbitrary-scheme correspondence with traceable modules, with local formulas in§2. The source’s dual module convention has been checked explicitly.',
 ['Wood2011','Wood2009','MondalBalaji2026'],'SR-ROOT-02','P02')
add(711,2,[23,24],[183,212],[190,201],
 'The quadratic-algebra construction is natural under base change, invertible rescaling and change of basis; the source postpones the general change-of-basis formula.',
 'open on the pages',['R10'],'B',
 'Wood2011 Theorem2.1 states a moduli-stack equivalence and§2–3 checks the change-of-basis construction. The deferred local step is settled in that precise arbitrary-scheme framework, not merely for forms over fields.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(712,2,[24,25,26],[202,292],[227,243],
 'Primitive line-valued binary quadratic bundles correspond to quadratic algebras equipped with an invertible algebra-module; an algebra-line norm is determined up to a line from the base.',
 'proof sketched',[],'B',
 'This is the primitive case of Wood2011 Theorem1.5 and Wood2009 Theorem2.1.4. The 2026 Clifford formulation is corroborative only; fixing a particular algebra’s Picard group additionally requires attention to automorphisms/orientation as in Dallaporta Theorem3.24.',
 ['Wood2011','Wood2009','Dallaporta2025','MondalBalaji2026'],'SR-ROOT-02','P03')
add(713,2,[27],[297,306],[297,306],
 'The parenthetical assertion that étale and fppf norm-one torsors give the same classification for every quadratic algebra is false. Over k=F2(t), q=t x² on A=k[ε]/ε² is primitive and its frame torsor x²=t^−1 has no étale local point.',
 'false as stated',[],'C',
 'Refuted with every hypothesis checked in P03. Refined statement CL-SA02-714 retains fppf classification; the étale version is valid when the norm-one group is smooth. Stacks59.28 records the same topology obstruction for Kummer torsors.',
 ['StacksKummer','Wood2011'],'SR-ROOT-03','P03')
add(714,2,[26,27],[279,306],[280,292],
 'For a finite locally free quadratic algebra A, 1→G_A→Res(A/S)Gm→Gm→1 is exact as fppf sheaves, and the scalar-valued primitive norm-form classification is the corresponding G_A-torsor classification. It becomes étale-local when G_A is smooth.',
 'proof sketched',[],'B',
 'The fppf statement is valid; its norm epimorphism follows by adjoining a square root of a unit. Wood’s primitive correspondence and the checked Kummer exactness give the precise framework. This is the refined statement for CL-SA02-713.',
 ['Wood2011','StacksKummer'],'SR-ROOT-03','P03')
add(715,2,[27,28],[308,318],[308,318],
 'For a primitive binary form the associated quadratic cover is its degree2 zero divisor in P(E), with the projective-bundle convention fixed; local reduction to a norm form proves the identification.',
 'proof sketched',[],'B',
 'Wood2011§3 gives the geometric construction from the zero scheme of the universal form; in the primitive case the derived construction is represented by the degree2 zero scheme. The source’s primitive hypothesis is retained.',
 ['Wood2011'],'SR-ROOT-02','P02')
add(716,2,[28,29],[320,342],[320,336],
 'The rank2 endomorphism construction admits a formulation in a rank4 Azumaya algebra, using reduced norm and its Severi–Brauer conic; assertions requiring a global rank2 module need a splitting of the Azumaya algebra.',
 'proof sketched',[],'C',
 'Grothendieck’s BrauerI§§5,8 supplies the exact Azumaya/torsor/Severi–Brauer infrastructure (May1965 exposition,1966 publication). The broader proposed correspondence is only sketched here; no exact later theorem for every unstated generalization was located.',
 ['GrothendieckBrauerI1966','BichselKnus1994'],'SR-ROOT-04','P04','medium')
add(717,2,[29,30,31,32],[344,473],[465,473],
 'The proposed identification E≅End(E)/A up to a base line is rejected by the author on scan32. It is false in general: A=O×O on P1 and E=O⊕O(1) give quotient O(−1)⊕O(1), with no compatible base-line twist of E.',
 'corrected by himself later',[],'C',
 'The source retracts the assertion at32:473 after the tensor-square calculation on31. The counterexample confirms that retraction. CL-SA02-718 is the refined formula; later Picard/orientation discussions do not restore a canonical square root.',
 ['Wood2011','Dallaporta2025'],'SR-ROOT-02','P04')
add(718,2,[30,31,32],[386,473],[432,442],
 'For E an invertible module over a quadratic A, End_O(E)/A has the tensor-square description E⊗_A E⊗det_O(E)^∨, with the conjugate action on duals accounted for.',
 'proved there',[],'B',
 'The local bimodule calculation is valid and has been independently rechecked in the split model; global descent follows from the line-valued construction. It is compatible with the module/dual conventions in Wood§6, not an isomorphism with E itself.',
 ['Wood2011'],'SR-ROOT-02','P04')
add(719,2,[33,34],[477,566],[482,501],
 'For φ_u(θ)=uθ−θbar(u), the reduced-norm polar pairing Tr(θ bar(θ′)) makes φ_u skew-adjoint; this is not the ordinary pairing Tr(θθ′). Its intertwiner line continues into the reflection analysis. The local trace of u satisfying u²+bu+c is−b.',
 'proof sketched',['R12','R14'],'E',
 'The matrix identities are checked over the universal coefficient ring. The general endomorphism/Clifford framework is established, while the conflicting trace sign remains an ink alarm.',
 ['Wood2011','BichselKnus1994'],'SR-ROOT-02','P05')
add(720,3,[35,36,37,38,39],[5,175],[11,29],
 'The near-conjugation automorphism calculation imposes2α=0 and α(α+b)=0; these equations permit extra automorphisms on nonétale characteristic2 fibres. An automorphism inducing−1 on A/O is not automatically canonical conjugation.',
 'proof sketched',['R11'],'E',
 'Substitution in the defining quadratic relation verifies the equations. The characteristic2 qualifications are essential; CL-SA02-721 records the separate false uniqueness corollary.',
 ['TateOort1970','Wood2011'],'SR-ROOT-03','P05')
add(721,3,[36],[38,59],[50,59],
 'The corollary characterizing conjugation solely by its action−1 on A/O fails even for the étale algebra F2×F2: identity and swap have the same quotient action. A nonidentity qualification on characteristic2 fibres is required.',
 'false as stated',['R18'],'C',
 'Explicit finite counterexample; the main statement’s overwritten qualifier could repair it, but ink is unavailable. Standard étale quadratic torsor theory gives the corrected nontrivial automorphism.',
 ['TateOort1970','Voight2016'],'SR-ROOT-03','P05')
add(722,3,[37,38,39,40,41],[61,254],[70,86],
 'For Q(e)=1 the reflection σ_e(x)=B_Q(e,x)e−x is an involution preserving Q and conjugating the associated quadratic algebra by its canonical involution.',
 'proved there',['R15','R16','R17'],'E',
 'The reflection formula is verified integrally in a norm basis, including characteristic2. Classical Clifford theory is background, while the independent coefficient proof supplies the exact local check.',
 ['BichselKnus1994','Wood2011'],'SR-ROOT-02','P05')
add(723,3,[38,39,40,41,42],[103,289],[216,233],
 'Conjugate-linear endomorphisms of an invertible A-module form an invertible A-module; locally each is m_zS and has determinant−N(z). The determinant−1 locus is the corresponding locally trivial norm-one torsor.',
 'proved there',['R12','R13'],'B',
 'The intertwiner and determinant statements are verified by universal matrices and descent. They agree with the primitive-module correspondence; no global choice of conjugation on E is claimed.',
 ['Wood2011'],'SR-ROOT-02','P05')
add(724,3,[42],[260,289],[270,281],
 'The covariance is f(uD)=(u/bar(u))f(D) with fixed action conventions. The further expression involving bar(u)² requires a norm-one restriction and cannot be used for an arbitrary unit.',
 'false as stated',['R12','R13'],'C',
 'The unrestricted simplification is not valid; the unsimplified ratio is verified. This is a local formula correction, with the exact bar/sign placement still assigned to the scan audit.',
 ['Wood2011'],'SR-ROOT-02','P05')
add(725,3,[44,45,46,47,48],[304,558],[309,325],
 'A quadratic algebra has canonical trace, determinant norm, involution and discriminantδ=T²−4N; in affine polynomial coordinates these transform compatibly under changing the lift of the quotient line.',
 'proved there',['R20','R33','R34'],'E',
 'These identities are standard and independently recomputed. Dallaporta’s parity/discriminant formalism gives an exact modern invariant comparison under2regularity, while trace and norm themselves require no such regularity.',
 ['Dallaporta2025','Voight2016'],'SR-ROOT-05','P06')
add(726,3,[47,48],[425,558],[436,448],
 'With the displayedδ=T²−4N and φ_N conventions, Q(φ_N(x))=−δN(x), not the transcribed positive sign; the later specialization Q=−N is consistent with the negative sign.',
 'false as stated',['R19','R20','R21','R22'],'C',
 'Universal coefficient expansion fixes the mathematical sign. The same conflict recurs at84/53–54; neither transcription is changed without ink inspection.',
 ['Dallaporta2025'],'SR-ROOT-05','P06')
add(727,3,[49,50],[610,680],[610,628],
 'When2 is O-regular, quadratic algebras are classified by an invertible lineL, δ∈L² and trace parityT0∈L/2L with locally lifted congruenceT0²≡δ mod4. The congruence uses local lifts and is independent of their choice.',
 'proof sketched',['R25','R26'],'B',
 'Exact match: Dallaporta Proposition2.23 and Theorem2.25, first arXiv26Nov2021, published IJNT21(4)(2025)739–767. Its Examples2.29–2.30 also show the necessity of the2regular hypothesis. Priority relative to these undated sheets is not established.',
 ['Dallaporta2025'],'SR-ROOT-05','P06')

add(728,3,[49,50],[568,680],[634,650],
 'On a2regular base, sections of the quadratic cover are congruence roots z²=δ, z≡T0 mod2 via x=(T+z)/2. Over arbitrary test schemes the congruence-root functor need not be the original finite cover.',
 'proved there',['R25'],'B',
 'The root formula follows from the parity presentation, exactly compatible with Dallaporta Proposition2.23. The functor distinction on test schemes with2torsion is real; it must not be erased by the base regularity hypothesis.',
 ['Dallaporta2025'],'SR-ROOT-05','P06')
add(729,3,[49],[568,609],[576,589],
 'The fpqc subgroup functor μ2′(R)={λ:λ²=1,λ≡1 mod2} is not representable if the base has a local point where2 is nonzero and noninvertible. The analogous congruence-root functor has the same obstruction after a flat root extension.',
 'stated without proof',['R50'],'D',
 'Independently proved here by the failure of left exactness of M↦2M∩M[2]. Searches of representability, parity/Kummer groupoids and MathOverflow located relevant cotangent and torsor frameworks but no exact published statement of this congruence-subfunctor obstruction. This does not leave the elementary assertion mathematically open.',
 ['StacksDerivations','Pirashvili2016','Dallaporta2025'],'SR-ROOT-06','P07','medium')
add(730,4,[51,52,53,54],[1,206],[8,27],
 'For2regular O, the trace-coordinate algebra is the lattice{(b,r):b≡rT0 mod2}, with unit(2,0), norm(b²−r²δ)/4 and product((bb′+rr′δ)/2,(br′+b′r)/2). The divisions are uniquely defined on that lattice.',
 'proved there',['R21','R22','R23','R24'],'B',
 'This is the trace-coordinate form of the valid parity construction in Dallaporta Proposition2.23/Theorem2.25. The products and divisibilities have been checked directly; no invertibility of2 is imposed.',
 ['Dallaporta2025'],'SR-ROOT-05','P06')
add(731,4,[52,53,54],[62,206],[178,206],
 'Under the dual pairing(λb+rζ)/2, the quadratic form is(ζ²−λ²δ)/4; its trace section has Q(T)=−δ. The positive sign in the final transcribed check conflicts with this formula.',
 'false as stated',['R21','R22','R23','R24'],'C',
 'The negative sign is forced by substitution and agrees with CL-SA02-726. The local multiplication and norm are valid; the positive occurrence remains a high-weight ink alarm.',
 ['Dallaporta2025'],'SR-ROOT-05','P06')
add(732,4,[54,55,56],[211,313],[218,239],
 'For an étale quadratic cover, extension of structure group Z/2→μ2 forgets the trace-parity refinement. A μ2-cover described by(L,Θ) has underlying quadratic discriminant4Θ and trace parity0.',
 'proof sketched',[],'B',
 'This comparison sits in Kummer and quadratic-torsor theory; Pirashvili’s groupoid maps and the standard fppf Kummer sequence give checked comparators. The factor4 is verified directly on R[u]/(u²−Θ).',
 ['StacksKummer','Pirashvili2016'],'SR-ROOT-03','P06')
add(733,4,[55,56],[242,313],[264,289],
 'The forgetful operation from μ2-torsors to all quadratic covers does not preserve the displayed algebra monoid product over a base such asZ: discriminants give4 on one route and16 on the other for the unit-square example. The proposed odd–odd replacement is expressly left to reformulate.',
 'open on the pages',[],'C',
 'The nonmonoidality is an immediate discriminant calculation. Modern quadratic-algebra monoids and Pirashvili’s parameterized torsor groupoids explain related operations with additional data; they do not identify the unfinished odd–odd functor uniquely.',
 ['Voight2016','Pirashvili2016'],'SR-ROOT-08','P09','medium')
add(734,4,[57,58],[318,419],[318,338],
 'In characteristic2, F_T(u)=u²+Tu is an additive finite locally free degree2 map, fppf-surjective and étale precisely whenT is invertible. A quadratic cover with traceT is a torsor underG_T=ker(F_T).',
 'proved there',['R27','R28'],'B',
 'This is the additive order2 group-scheme case of Tate–Oort1970, introduction and Theorem2; the source’s exact equations and torsor action are independently proved. No separability is required for the fppf statement.',
 ['TateOort1970','Pirashvili2016'],'SR-ROOT-07','P08')
add(735,4,[58],[370,419],[377,395],
 'For trace parametersT,T′ in characteristic2 the mapG_T×G_T′→G_TT′ is(u,u′)↦T′u+Tu′; pushing out the product torsor gives the quadratic-cover product with the corresponding trace.',
 'proof sketched',['R29','R30'],'B',
 'The kernel homomorphism and coefficient relation are verified universally in characteristic2. Voight’s product and the Tate–Oort/Pirashvili torsor framework supply exact comparisons for this branch.',
 ['TateOort1970','Voight2016','Pirashvili2016'],'SR-ROOT-07','P08')
add(736,4,[59,60,61,62],[423,614],[423,448],
 'A quadratic algebra is equivalently a rank2 module with a primitive unit and a quadratic norm taking value1 on it; the trace is its polar value at the unit. Equivalently use a monic polynomial on an affine line torsor, or the stated extension with an admissible quadratic form.',
 'proved there',['R33','R34'],'B',
 'The pointed-norm construction is checked in a basis by u²−tu+n. It fits the general binary-form/quadratic-algebra correspondence and the standard quadratic-ring presentations; the polar trace is indispensable.',
 ['Wood2011','Voight2016'],'SR-ROOT-02','P08')
add(737,4,[61,62],[540,614],[574,593],
 'The condition4N−T²∈L² alone does not forceT to be the polar trace in the presence of2torsion; the author adds the actual conditionT=B_N(-,1), locallyt=−b.',
 'corrected by himself later',['R35'],'C',
 'The coefficient obstruction is recomputed. The corrected pointed-norm formulation is valid, while the weakened criterion loses the mixed coefficient; modern traceable-module definitions keep trace compatibility explicitly.',
 ['Wood2011'],'SR-ROOT-02','P08')
add(738,4,[63,64,65],[628,732],[647,668],
 'For Ai=R[ui]/(ui²+biui+ci), the quadratic product has b=b1b2 and c=b2²c1+b1²c2−4c1c2, with a map toA1⊗A2 sendingu to b2u1+b1u2+2u1u2. The source’s c1c1 occurrence and exchanged subscripts are inconsistent with the universal identity.',
 'proved there',['R30'],'B',
 'Exact product match with Voight Construction3.14(3.15) after w=u+b1b2,t=−b1,s=−b2; Loos gives its earlier categorical construction. The integral identity is verified here and remains valid over rings with2torsion.',
 ['Voight2016','Loos1997'],'SR-ROOT-08','P09')
add(739,4,[63,64,65],[628,732],[675,698],
 'The quadratic-product discriminant isδ1δ2 and its coefficient formula is associative and commutative; the identity is the split quadratic algebra and the dual-number algebra is absorbing on isomorphism classes.',
 'proof sketched',['R31','R32'],'B',
 'Voight Lemma3.16 states the commutative monoid with identity and absorbing element; Loos1997§§2.8–2.10 provides natural associativity/commutativity/unit constraints. The discriminant and coefficient identities are recomputed independently.',
 ['Voight2016','Loos1997'],'SR-ROOT-08','P09')
add(740,5,[67,68],[4,68],[9,28],
 'For0→L→E→O→0, a liftT ofχ is equivalent to a retractionπ:E→L restricting toχ id_L, viaπ(x)=χx−Tψ(x). This equivalence requires no regularity ofχ.',
 'proved there',[],'E',
 'Exactness gives both directions directly. Searches of extension products and Picard categories found the general cohomological framework, but the simple identity already proves this source claim without a literature-dependent hypothesis.',
 ['DeligneSGA4XVIII'],'SR-ROOT-09','P10')
add(741,5,[68,69,70,71],[70,222],[161,180],
 'The tensor filtration and its pushout define the product ofχ-trivialized extensions for arbitraryχ; itsχ-retraction is induced byπ1⊗π2. Locally the product coefficient isb1⊗b2.',
 'proved there',['R36','R37','R38'],'D',
 'The source pushout construction is re-proved in local split coordinates and glued by its universal property. SGA4 gives extension/Picard background and Loos settles the quadratic specialization; no exact publication of this unrestricted variable-moduleχ-product was located in the recorded search.',
 ['DeligneSGA4XVIII','Loos1997','Pirashvili2016'],'SR-ROOT-09','P10','medium')
add(742,5,[71,72,73,74,75],[226,505],[476,495],
 'The relationχT12=T1*T2 holds even whenχ is a zero divisor. The early cancellation argument has a regularity hypothesis, but the direct computation on scan75 removes it. The sign convention for localb changes explicitly on scan73.',
 'corrected by himself later',['R39','R40'],'E',
 'The final integral identity is verified independently. The earlier proof cannot cancelχ without regularity; its later coordinate proof is a genuine source correction, not an additional assumption.',
 ['Loos1997'],'SR-ROOT-09','P10')
add(743,5,[76,77,78],[509,603],[546,562],
 'The universal property must retain a bilinear mapf together with its coefficient mapα:L1⊗L2→M satisfying the two boundary conditions. In generalα cannot be recovered fromf. The printed right side on77:551 must be interpreted inM viaα.',
 'proof sketched',[],'E',
 'The pushout universal property proves the version with the pair(f,α). Theχ=0,b1=b2=0 example shows whyf alone loses data. No exact unrestricted replacement theorem was located beyond this elementary categorical proof.',
 ['DeligneSGA4XVIII'],'SR-ROOT-09','P10')
add(744,5,[79,80],[607,679],[609,629],
 'The earlyχ-extension product has natural commutativity, associativity and unit constraints; the manuscript sketches them but leaves the coherence sentence unfinished. The identical multilinear expansion of all bracketings proves coherence for this construction.',
 'proof sketched',['R37','R38','R41'],'C',
 'The coherence of the early pushout product is independently justified here. Loos1997§2.10 supplies the quadratic-algebra case; SGA4/Pirashvili provide categorical comparators with different stated scopes. This does not settle the later fixed-endpoint comparison for arbitraryχ.',
 ['Loos1997','DeligneSGA4XVIII','Pirashvili2016'],'SR-ROOT-09','P10','medium')
add(745,5,[79,80],[635,679],[651,670],
 'Aχ-trivialized extension is invertible for the displayed product iffL is a line andb modχ generatesL/χL; locally this permits coordinates in whichb is a unit and the object is the unit.',
 'proof sketched',[],'D',
 'The local criterion is re-proved using the two casesχ unit orχ in the maximal ideal. Searches found related invertibility criteria for quadratic-torsor groupoids, but no exact unrestrictedχ statement; this is not evidence of an unsolved mathematical question.',
 ['Pirashvili2016','DeligneSGA4XVIII'],'SR-ROOT-09','P10','medium')
add(746,5,[80,81],[684,745],[691,711],
 'Atχ=2, σ=Tψ−id is an involution compatible with the extension. If multiplication by2 is invertible onL, a canonical splitting results; this is a condition onL and need not mean2 is a unit inO.',
 'proved there',['R43'],'E',
 'The involution square follows fromψ(T)=2. The splitting is obtained from the2-retraction by the inverse of2 onL. The condition in the source is retained exactly.',
 ['Loos1997'],'SR-ROOT-09','P10')
add(747,6,[82,83,84],[5,91],[34,53],
 'For theχ=2 product, the tensor-to-product map has cokernel coker(π1)⊗coker(π2); the simultaneous involution relation maps to zero. These are module assertions preceding the quadratic-form specialization.',
 'proved there',['R43','R44'],'E',
 'The tensor/pushout calculation is valid with its exact boundary maps. The line-kernel matrix is checked explicitly; the quadratic-algebra specialization appears in Loos’s canonical tensor map.',
 ['Loos1997','Voight2016'],'SR-ROOT-08','P11')
add(748,6,[83,84,85,86,87],[33,170],[117,139],
 'For positive-rank finite locally free kernels, the coinvariant-to-product map is an isomorphism iff at every characteristic2 point at least oneT_i generatesL_i. As literally stated for arbitrary finite ranks it fails: overF2, L1=0,L2=F2,T1=T2=0 gives coinvariant dimension2 and product dimension1. The exact all-ranks correction is: at each such point either both kernels have rank0, or one kernel has rank1 and itsT generates it.',
 'false as stated',['R44','R45','R46','R47','R51'],'C',
 'The positive-rank theorem, including arbitrary rank for the other kernel, is proved over rings by block elimination in P11. The rank-zero counterexample refutes the literal broader formulation. Loos/Voight supply the quadratic line-kernel specialization; they do not remove this extension-category edge case.',
 ['Loos1997','Voight2016'],'SR-ROOT-08','P11','medium')
add(749,6,[86,87],[140,170],[149,169],
 'Under the corrected criterion of CL-SA02-748, applyingHom(-,M) gives the invariant description for everyM, and its finite locally free dual gives the stated universal invariant-algebra comparison. The source’s uncorrected rank-zero OR-condition inherits the same counterexample.',
 'false as stated',['R44','R46','R47','R51'],'C',
 'The corrected assertion follows from the proved coinvariant presentation by the universal property of the cokernel; it is stable under base change. The source’s all-ranks criterion needs the correction in CL-SA02-748.',
 ['Loos1997','Voight2016'],'SR-ROOT-08','P11','medium')
add(750,6,[87,88,89],[174,226],[179,197],
 'Atχ=0 the product torsor is the pushout under(u1,u2)↦u1b2+b1u2. For a fixed admissible trace datum, admissible quadratic forms form anL²-torsor. The displayT_Q=Q is type-inconsistent and should be checked againstT_Q=T.',
 'proved there',[],'E',
 'Theχ=0 specialization of the exact local product proves the torsor formula; subtracting two admissible forms gives the quotient-line square. The specific printed letter remains an ink question.',
 ['DeligneSGA4XVIII','Loos1997'],'SR-ROOT-09','P10')
add(751,6,[90,91,92],[247,336],[255,279],
 'There is a unique admissible quadratic form on the product with the stated homogenized formula, including both augmentation squares. Its discriminant isδ1δ2. The construction is integral, despite a heuristic calculation dividing by4.',
 'proved there',['R30','R31','R42'],'B',
 'The homogenized formula and discriminant are universally checked. Voight’s product and Loos1997§§2.8–2.10 give the exact quadratic construction without inverting2.',
 ['Voight2016','Loos1997'],'SR-ROOT-08','P09')
add(752,6,[91,92],[295,336],[313,336],
 'The quadratic product is étale exactly when both input algebras are étale, since its discriminant is their product. With one étale factor, the product is an étale-local twist of the other factor.',
 'proved there',['R31'],'B',
 'The criterion and twist interpretation agree with the established quadratic monoid and étale torsor product. The one-étale condition does not assert that the product itself is étale when the other factor is ramified.',
 ['Voight2016','Loos1997'],'SR-ROOT-08','P11')
add(753,6,[92,93],[338,343],[338,343],
 'The natural mapX1×X2→X1∧X2 is faithfully flat away from simultaneous nonétaleness and fails there over geometric fibres; this obstruction occurs in characteristic0 as well as2. The source explicitly cancels the characteristic2-only qualification.',
 'corrected by himself later',['R48','R49'],'C',
 'The étale-splitting proof and dual-number counterexamples establish the corrected fibrewise assertion. The relative finite-presentation locus follows from the fibrewise flatness criterion. No interpretation as an unrestricted invariant subalgebra is valid.',
 ['Loos1997','Voight2016','StacksFibreFlatness'],'SR-ROOT-08','P11')
add(754,6,[93,94,95,96],[345,495],[466,495],
 'The cancelled norm-coordinate attempt is restarted, and g_x(y)=ψ(x)y−ψ(y)x gives the wedge duality between a rank2 extension and its dual. The final homomorphism-of-extensions claim continues on scan97 and includes a sign on the submodule.',
 'proof sketched',[],'E',
 'The wedge formula is elementary and checked in the same basis as the rank2 duality. The scan97 continuation is linked to the first Pro packet rather than counted as a new independent theorem; the extension sign must be retained.',
 ['Wood2011'],'SR-ROOT-02','P02')

def save():
 (O/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
 (O/'quote_review.txt').write_text('\n\n'.join(c['id']+' '+str(c['scans'])+'\n'+c['his_statement'] for c in claims)+'\n')
 print(f'{len(claims)} manually authored early-cote84 claim records written.')

if __name__=='__main__':save()
