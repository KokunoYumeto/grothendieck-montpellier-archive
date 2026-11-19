"""Human-authored claims map for the read cote93 Pro package.

Grouping follows mathematical assertions, not note-heading matching. Quotes and
locators refer to supplied diplomatic transcriptions, never repaired silently.
"""
from pathlib import Path
import json,csv,datetime
OUT=Path(__file__).resolve().parents[1]
items={i['id']:i for i in json.loads((OUT/'items.json').read_text())}
claims=[]
def c(n,ns,status,statement,computation,cl,fate,dates,refs,confidence='high',scans=None,lines=None,words=None,present=None):
    linked=[items[f'SA03-{i}'] for i in ns]
    claims.append(dict(id=f'CL-SA03-{n}',items=[i['id'] for i in linked],cote=93,
        scans=scans or sorted(set(sum([i['scans'] for i in linked],[]))),
        lines=lines or sorted(set(sum([i['lines'] for i in linked],[]))),
        his_statement=words or linked[0]['his_words'],statement=statement,
        status_on_pages=status,computation=computation,**{'class':cl},fate=fate,
        fate_date=dates,present_status='As of 19 November 2026: '+(present or fate),refs=refs,confidence=confidence))
E=['D_Deligne1968','D_Deligne1975']
ef='Search D-S01: exact counterpart in Deligne’s Tate formulary, circulated1968, published1975; reused material, not an independently dated Grothendieck discovery.'
dates='1968 IHES preprint; 3 September1975 publication. Date of annotations not established.'
poly='Exact integral polynomial substitutions in code/check_computations.py; zero residuals in outputs/computations.txt.'
c(601,[603,604],'proof sketched',
 'For the pointed proper flat finitely presented genus-one family of scan3, p_*O=O, R¹p_*O is invertible, and for n>0, R¹p_*O(ne)=0 while p_*O(ne) is locally free of rank n and commutes with arbitrary base change.',
 'Fibrewise Riemann–Roch and negative-degree vanishing, followed by cohomology/base change; argument and hypotheses recorded in proof_checks.md. No numerical experiment substitutes for base change.',
 'E',ef+' §1; modern foundational comparison: Stacks0E1J. Search D-S03.',dates,E+['D_StacksCoh'])
c(602,[604,605],'stated without proof',
 'The same Gorenstein genus-one family has relative dualizing line p*ω, with ω=(R¹p_*O)^∨. In modern cohomological conventions p!O=ω_(E/S)[1]; the positive R¹ in the supplied text is left for collation.',
 'Degree-zero fibrewise triviality plus relative duality; indexing/type check, not a proof of the duality theorem. See proof_checks.md.',
 'E',ef+' §1; Stacks0E6N supplies the modern shift and base-change statement. Search D-S03.',dates,E+['D_StacksDual'])
c(603,[603],'proof sketched',
 'O(3e) is relatively very ample for the stated family; locally it yields a cubic y²+a₁xy+a₃y=x³+a₂x²+a₄x+a₆ with section at infinity. Geometric fibres are smooth elliptic, nodal rational or cuspidal rational.',
 'Ranks of sections 1,2,3,6 and the pole-order relation explain the Weierstrass construction; curve singularity classification is carried as published background, not reproved.',
 'E',ef+' §§1–2.',dates,E)
c(604,[610],'stated without proof',
 'The displayed integral definitions of b₂,b₄,b₆,b₈,c₄,c₆,d₆,d₈,Δ satisfy every stated relation, including c₄³−c₆²=1728Δ, without inverting2 or3.',poly,'E',ef+' §§2–3.',dates,E)
c(605,[611],'false as stated',
 'With F(x,y)=y²+a₁xy+a₃y−x³−a₂x²−a₄x−a₆, substitution x=u²X+r,y=u³Y+su²X+t gives u⁴a₄′=−F_x(r,t)−sF_y(r,t). The literal −F(r,t) formula is false; this is an algebraic reading alarm, not an ink verdict.',
 poly+' The nonzero residual for the literal expression is printed. Refined formula is SA03-611.',
 'E',ef+' §2; polynomial verification, not the parallel printing, decides which algebraic formula is valid.',dates,E)
c(606,[610,611],'stated without proof',
 'Under the allowed coordinate changes the discriminant and c-invariants transform with weights12,4,6; b- and d-invariants have the inhomogeneous r-terms printed on scans8–9. The invariant differential scales by u.',
 poly+' Differential scaling follows by differentiating the coordinate substitution and the defining equation.',
 'E',ef+' §2.',dates,E)
c(607,[603,610],'proof sketched',
 'Over bases with6 invertible, a pointed genus-one curve with chosen nonzero invariant differential has a unique short Weierstrass model y²=x³+g₂x+g₃; the enlarged moduli problem including nodal/cuspidal fibres is the affine plane. For smooth curves invert its discriminant.',
 poly+' Solving successive x/y translations divides only by2 and3; distinction between the affine plane and its smooth open is retained.',
 'E',ef+' Proposition2.5. The source’s genus-one convention includes singular fibres.',dates,E)
c(608,[610],'proof sketched',
 'With2 invertible complete the square. If c₄ is a unit, the translation r=−d₆/c₄ imposes d₆=0 uniquely; the printed c₆,Δ and a₂a₄=9a₆ relations follow, giving the stated chart with a chosen differential.',poly,'E',ef+' §3, Proposition3.5.',dates,E,scans=[10,11])
c(609,[612],'proved there',
 'On the ordinary characteristic2 chart the equation can be written y²+xy=x³+a₂x²+a₆. The involution y↦y+x preserves the pointed curve and invariant differential, so the differential does not rigidify it.',
 'Substitution mod2 is identically zero; the automorphism is nonidentity on the smooth ordinary curve. Residual printed in outputs/computations.txt.',
 'E',ef+' §4; this checks the stated ordinary chart.',dates,E)
c(610,[613],'stated without proof',
 'In characteristic3 the stronger condition a₂=0 gives y²=x³+a₄x+a₆ and Δ=−a₄³; in characteristic2 the stronger condition a₁=0 gives y²+a₃y=x³+a₄x+a₆ and Δ=a₃⁴. The stronger vanishings must not be replaced by c₄=0 over nonreduced bases.',
 poly+' Dual-number distinctions recorded in outputs/additional_computations.txt.',
 'E',ef+' §5; the source itself explicitly strengthens the hypotheses.',dates,E)
c(611,[628],'proof sketched',
 'The assertions on reduction distinguish good, multiplicative and additive fibres using Δ and c₄. The phrase “Δ est elliptique” is not mathematically well-typed; candidate subject E and internal reference repairs are recorded separately.',
 'Checked against the smoothness criterion for the Weierstrass cubic and the source’s three fibre types; no independent proof of every relative reduction statement claimed.',
 'E',ef+' Proposition6.1.',dates,E,scans=[14])
c(612,[622],'proof sketched',
 'For pointed genus-one curves in the formulary without additive fibres, the relative Isom scheme is finite and unramified. Equality of j makes it surjective; where j and j−1728 are units it is finite étale of degree2. This is a local-isomorphism assertion, not a global section theorem.',
 'Chart equations and fibre conditions read on scans15–17; proof reduction is sketched in the text. No inference that a surjective finite map is automatically flat at exceptional j.',
 'E',ef+' Proposition6.3, partsI–III.',dates,E)
c(613,[622,623],'proof sketched',
 'The explicit Isom equations are quadratic when2 is invertible and Artin–Schreier on the characteristic2 ordinary chart. Scan17’s a₂x requires comparison with the quadratic coefficient in scan12’s referenced model.',
 'Weierstrass transformation substitution in code/check_computations.py verifies the coefficient equations and the relevant char2 involution. Torsor identification requires the retained chart hypotheses.',
 'E',ef+' §§6.4–6.6.',dates,E)
c(614,[619,621],'proof sketched',
 'Geometric pointed automorphism orders are2 generically,4 at j=1728 and6 at j=0 when6 is invertible,12 at the supersingular j in characteristic3 and24 in characteristic2. These are geometric orders; global sections over disconnected bases need not have that cardinality.',
 'Characteristic2 enumeration overF4 and full multiplication table; characteristic3 count overF9; outputs/computations.txt and additional_computations.txt. Tame cases follow the short-model scalar equations.',
 'E',ef+' Proposition6.9; geometric small-prime orders also DR VI§4.8.',dates,E+['D_DR1973'])
c(615,[621],'corrected by himself later (both places)',
 'The generic two-element automorphism statement is valid as a sheaf statement. Its literal global-section version fails on a disconnected base; the margin on scan19 explicitly requests sheafification, while scan20 retains the unqualified phrase in its proof.',
 'Two nonempty connected components give independent sign choices, hence four global sections. This refutes only the uncorrected cardinality assertion; refined statement SA03-621.',
 'E',ef+' Proposition6.9(I), with the supplied correction retained.',dates,E)
c(616,[624],'false as stated',
 'For T_(u,r,s,t)(X,Y)=(u²X+r,u³Y+su²X+t), composing outer(U,R,H,K) with inner(u,r,s,t) gives (Uu,R+U²r,H+Us,K+U³t+HU²r). The middle coefficient containing t′ in scan22 is inconsistent with this substitution.',
 'Exact two-stage polynomial substitution proves the ordered law; see outputs/computations.txt. Refined statement SA03-624; ink undecided.',
 'E',ef+' §6; an order convention is specified explicitly for the correction.',dates,E)
c(617,[626],'stated without proof',
 'The integral graded ring asserted in the formulary is Z[c₄,c₆,Δ]/(c₄³−c₆²−1728Δ), with weights4,6,12. One must distinguish all genus-one curves from the smooth open, for which Δ is inverted.',
 'The relation is symbolically checked; generation and absence of further relations are not proved by that computation. Source assertion, not independent ring-theorem proof.',
 'E',ef+' §§6–7; compare the displayed graded ring, not the unfinished scan21 corollary.',dates,E)
c(618,[626,627],'stated without proof',
 'The displayed characteristic2 and3 rings have generators a₁,Δ and b₂,Δ respectively, with weights(1,12) and(2,12). The Hasse scalar is a₁ or a convention-dependent sign times b₂. These give low-weight forms absent from naive reduction of the integral generators.',
 'Integral invariant reductions and degree-semigroup obstruction checked. The whole generation theorem is carried as published background.',
 'E',ef+' §7. Search D-S02: Katz§2.0 fixes Hasse normalization.',dates,E+['D_Katz1973'])
c(619,[606],'open on the pages',
 'At the Tate cusp in characteristicp, is the Hasse section equal to (du/u)^(p−1)? With the canonical differential the answer is yes: its q-expansion is1.',
 'The source’s weight correction is checked. Katz’s computation D^p=D for D=(1+t)d/dt gives the normalization; statement and short argument inspected, not the complete modular-scheme theory.',
 'B','Search D-S02: Katz1973§2.0, pp97–98 supplies exactly the cusp normalization; §2.1 treats its Eisenstein lift whenp>3.','Antwerp1972 lectures; publication1973.',['D_Katz1973'])
c(620,[607,608],'stated without proof',
 'For the smooth Legendre family λ≠0,1 in odd characteristic, j=256(1−λ+λ²)³/[λ²(1−λ)²], invariant under the six cross-ratio transforms. Forp=2n+1 its Hasse coefficient is (−1)^n Σ_i binom(n,i)²λ^i. The suspicious extra minus in the sixth listed transform fails the j identity.',
 'All six rational identities and coefficient extraction checked symbolically; finite primes3…31 supplement the general binomial proof. The extra-minus residual is nonzero. No count is inferred from the unresolved table numerator.',
 'E',ef+' scan4 formulas; Search D-S02 for the Hasse convention.',dates,E+['D_Katz1973'])
c(621,[609],'stated without proof',
 'The Hodge line on the compactified moduli stack of elliptic curves has degree1/24, in the stack-weighted convention. The manuscript states the degree, not the prior note’s full weighted supersingular mass argument.',
 'No independent intersection-theoretic proof. The weighted-mass deduction in SA03-609 is explicitly conditional on simple Hasse zeros.',
 'E','Search D-S02: DR VI§4.3–4.9 gives the degree and weighted zero formula, including the small-prime geometric stabilizers. This verifies the modern interpretation of the source’s degree.','Antwerp1972; publication1973.',['D_DR1973'])
c(622,[647],'stated without proof',
 'The q-series Q=1+240Σσ₃(n)q^n and R=1−504Σσ₅(n)q^n satisfy Q³−R²=1728q∏(1−q^n)^24. The displayed normalization agrees with c₄,c₆ andΔ.',
 'Exact series identity checked throughq^10 in check_additional_computations.py. This finite check is not a proof of the all-orders identity.',
 'E',ef+' scan4 q-series; Search D-S02: Katz AppendixA1.4 gives the derivative comparison.',dates,E+['D_Katz1973'])
c(623,[615],'open on the pages',
 'Compare the deformation disc of a pointed elliptic curve with the completed j-line modulo automorphisms. A rigorous geometric formulation uses a strict local coarse quotient, distinguishing the quotient stack, its invariant ring, residue-field descent, and ineffective stabilizers.',
 'No independent construction of the wild invariant ring. Small-prime examples establish valuation behaviour only, not the quotient theorem.',
 'B','Search D-S02: DR I§8.2.1–3 and III§1.2–1.3 supply the strict-local coarse-quotient and formal-deformation framework. The displayed W(k) formula over arbitrary perfect nonclosedk needs descent; arbitrary base change of coarse spaces is not inferred.','1972 lectures;1973 publication.',['D_DR1973'],confidence='medium')
c(624,[614,615],'false as stated',
 'With6 invertible the tame coarse parameters vanish to orders3 atj=0 and2 atj=1728: the latter is j−1728. The literal j∼t² near1728 cannot be true becausej is a unit, unless a translated-coordinate convention was intended.',
 'Short Weierstrass coordinates give j proportional to c₄³ with unit denominator near0, and j−1728=c₆²/Δ near1728. Refined statement SA03-614.',
 'E','Search D-S02: DR VI§1.9 identifies the corresponding stabilizers; exact ramification orders also follow directly from c₄³−c₆²=1728Δ. Annotation date unknown.','1968 formulary witness;1973 comparison.',['D_Deligne1968','D_DR1973'])
c(625,[616],'stated without proof',
 'For an equal-characteristic DVR with good elliptic reduction and nonzeroj, characteristic3 gives6|v(j), characteristic2 gives12|v(j). Without equal characteristic the stronger assertion fails, as the two explicit mixed-characteristic good-reduction examples show.',
 'All invariants, discriminants and valuations redone exactly. Families attain6 and12; mixed-characteristic values3 and15 refute only the stronger extension. Refined formulation SA03-616.',
 'E','Search D-S01–02: integral formulas in Deligne§§2,5 give the divisibilities immediately after reduction. No independent historical priority inferred from the margin.','1968/1975 formulary; annotation undated.',E)
c(626,[619],'open on the pages',
 'The characteristic2 supersingular automorphism group is Q₈⋊C₃ of order24. The central involution is ineffective on marked deformation classes; identifying the entire remaining faithful action requires a deformation argument beyond the order count.',
 'ExhaustiveF4 group law, element orders and quaternion kernel checked; central-kernel interpretation is separately explained in proof_checks.md and not equated to faithful action.',
 'B','Search D-S01–02: formulary§6 provides explicit automorphisms; DR I§8.2.3 separates ineffective stabilizers in the coarse-quotient framework. The margin’s effective-order interpretation remains our qualified reconstruction.','1968 formulary;1973 quotient framework.',E+['D_DR1973'],confidence='medium')
c(627,[625],'open on the pages',
 'An unfinished corollary on scan21 names a base flat overZ and begins a ring expression. No complete quantified conclusion survives in either supplied witness.',
 'Not a complete computation or proposition; no completion is fabricated.',
 'F','Search D-S01–02: the matching formulary and small-prime ring formulas do not identify the missing conclusion. It cannot be equated with unrestricted base change.','1968/1975 parallel witnesses; no resolution of missing conclusion.',E,confidence='low')

c(630,[630,635],'stated without proof',
 'Wanderley’s offprint asserts that sheaf exactness, separation, boundary-local isomorphism and point normalization force the orientation étalé space to be a two-sheeted cover. This is a claim of the included offprint, not an authenticated Grothendieck annotation.',
 'The boundary induction is described but not carried out in the three pages. No proof is supplied by counting sheets in examples.',
 'B','Search D-S04: Proposition on printedp214, with proof deferred to the cited1980 thesis. The offprint was read in the attachment; thesis and independent external reproduction not retrieved.','Thesis cited1980; submitted5January1981; issue19January1981.',['D_Wanderley1981','D_Wanderley1980'],confidence='medium')
c(631,[634],'stated without proof',
 'For manifolds of dimension≤N an orientation theory exists; any morphism of theories is unique and an isomorphism; whenN≠4 any two theories admit that unique isomorphism. The exceptional cutoffN=4 must not be read as excluding dimension4 objects from all larger categories.',
 'No complete proof of WanderleyTheorem1; quantifiers and the dependency on later listed results checked.',
 'B','Search D-S04: WanderleyTheorem1, printedp214. Kirby’s stable-homeomorphism theorem supplies the stated topological input outside dimension4.','1980 thesis cited;1981 offprint.',['D_Wanderley1981','D_Kirby1969'],confidence='medium')
c(632,[635],'stated without proof',
 'For sheaves on the category ofm-manifolds and open embeddings, local constancy, the stated separation condition, and invertibility of the action of the continuous injective self-map monoid ofR^m are equivalent.',
 'Read all three conditions of WanderleyTheorem2. They concern natural sheaves on the manifold category, not arbitrary separated sheaves on one fixed space.',
 'B','Search D-S04: exact assertion in WanderleyTheorem2, printedp215. Thesis proof unavailable; no broader fixed-space formulation is endorsed.','1980 thesis cited;1981 offprint.',['D_Wanderley1981','D_Wanderley1980'],confidence='medium')
c(633,[635],'stated without proof',
 'Evaluation onR^m gives an equivalence from the category of locally constant natural sheaves onm-manifolds to sets with an action ofΠ(m), the group completion of the continuous-embedding monoid.',
 'Source category, action and group-completion notation read; no reconstruction of the full topos comparison proof.',
 'B','Search D-S04: WanderleyTheorem3, printedp215; source-specific categorical theorem, not merely ordinary covering-space classification.','1980 thesis cited;1981 offprint.',['D_Wanderley1981'],confidence='medium')
c(634,[634,635],'stated without proof',
 'The degree mapΠ(m)→{±1} is an isomorphism exactly when every degree+1 self-homeomorphism ofR^m is a finite product of homeomorphisms equal to the identity on a nonempty open subset. The offprint deduces the isomorphism form≠4.',
 'Exact equivalence read as WanderleyTheorem4; Kirby and Quinn theorem statements inspected, not their full proofs. The extension using Quinn is conditional on the offprint’s equivalence.',
 'B','Search D-S04: Kirby1969Theorem1/addendum; Quinn1982§2.2Theorem2.2.2 provides the later dimension4 annulus input. No source was found redoing Wanderley’s full categorical deduction.','Kirby addendum1December1968/publication1969; Quinn1982.',['D_Wanderley1981','D_Kirby1969','D_Quinn1982'],confidence='medium')
c(635,[635],'stated without proof',
 'The category of Stokes triples of separated sheaves in consecutive dimensions, with the stated local boundary isomorphism, is equivalent via evaluation toΠ(m)-sets.',
 'All three pieces and the local-isomorphism condition read; no proof of essential surjectivity or descent reconstructed.',
 'B','Search D-S04: WanderleyTheorem5, printedp215; exact thesis proof not retrieved.','1980 thesis cited;1981 offprint.',['D_Wanderley1981','D_Wanderley1980'],confidence='medium')
c(636,[631,632,633],'proof sketched',
 'The handwritten orientation system uses the locally two-sided normal-side sheafρ_(Y/X) over a locally flat codimension-oneY, a natural map to Hom(ρ_(Y/X),Ω_Y), opposite induced orientations, local nonemptiness and separation. On a connectedX, two global orientations agreeing at one point agree everywhere.',
 'Opposite-half-space boundary sign and open-and-closed equality-locus proof checked in proof_checks.md. The full equivalence with the printed axioms is not established.',
 'C','Search D-S04: the offprint gives a closely related system; its exact equivalence with these six handwritten conditions remains a proof-comparison task, not an identified open topological theorem.','Handwritten leaves undated; comparison offprint1981.',['D_Wanderley1981'],confidence='medium')
c(637,[636,637],'proof sketched',
 'The anonymous English fragment claims a weak-operator-limit projectionθ ontoT-fixed vectors, with kernel those whose orbit closure contains0, andY=imθ⊕kerθ. Its semigroup hypotheses and invoked lemma are on missing pages.',
 'Given a two-sided absorbing projectionθ in the operator closure, the displayed uniqueness and direct-sum argument is valid. Existence of thatθ is not re-proved from the fragment’s incomplete hypotheses.',
 'F','Search D-S05: Huff1973 is a bibliographic candidate only; publisher front matter was opened, but chapter text and the missing lemma were not found.','Candidate1972 symposium/1973 publication; identity of fragment undetermined.',['D_Huff1973'],confidence='low')
c(638,[638,637],'proof sketched',
 'Under uniform boundednessM, θy in the norm-closed convex orbit hull, tθ=θ and eventual absorptiontt_i=t, the directed netty converges in norm toθy. The norm expression on scan32 requires a difference, not an equality sign inside the norm.',
 'Independent ε/(M+1) estimate with all absorption assumptions stated in proof_checks.md; the missing semigroup hypothesis is not inferred from weak compactness alone.',
 'F','Search D-S05: the visible estimate is verified conditionally, but the full source theorem remains unidentified.','Fragment date unknown; Huff candidate1973.',['D_Huff1973'],confidence='medium')
c(639,[639],'stated without proof',
 'For the fragment’s undefined space sba(A,X), an operator family indexed bypartitions is claimed to have conditionally weakly compact orbits, leading to a countably-additive/purely-finitely-additive decomposition. Its Proposition1 and definitions are absent.',
 'No computation can certify the missing compactness assertion for every possible interpretation of sba orX.',
 'F','Search D-S05: exact application not recovered from a verified complete source. Classical Yosida–Hewitt analogies do not supply missing vector-valued hypotheses.','Undetermined; Huff1973 candidate only.',['D_Huff1973'],confidence='low')
c(640,[640,641],'corrected by himself later (both places)',
 'Forf′ invertible, G(t,f)=[−2f‴/f′+3(f″/f′)²]dt² satisfiesG(t,exp f)=G(t,f)+(df)². Scan36 retains3(df)² in intermediate lines but deletes3 in the boxed/final formulas; f=t givesG(t,e^t)=dt².',
 'Exact symbolic differentiation in check_computations.py verifies every cancellation, the coefficient1 and the exponential test. The final correction agrees with the check.',
 'E','Search D-S06: this is−2times the classical Schwarzian; Ovsienko–Tabachnikov equations1–3 and Dumas§3.1 supply the transformation framework. Manuscript date/priority not established.','Classical identity; modern expositions2009.',['D_Ovsienko2009','D_Dumas2009'])
c(641,[642],'open on the pages',
 'The scan36 margin proposes invariance for an ambiguously read hyperbolic transformation groupπ. The valid precise classical statement is Möbius postcomposition invariance ofS(f), and the quadratic-differential transformation law under projective-coordinate changes.',
 'Cocycle and Möbius substitution checked symbolically in check_computations.py; no assertion about an unspecified nonlinearπ-action is inferred.',
 'E','Search D-S06: Ovsienko–Tabachnikov equations1–3; Dumas§§3.1–3.2. The uncertain word and action remain Stage4 targets.','Classical identity;2009 verified expositions.',['D_Ovsienko2009','D_Dumas2009'],confidence='medium')

# Montréal programme: publication is a witness to the announcement, not its proof.
G=['D_GrothBT1974']
gd='Course29June–24July1970; publication1974; manuscript annotation date not inferred.'
c(650,[650],'stated without proof',
 'Forp locally nilpotent onS andS₀=V(p), the programme invokes equivalence of its locally free absolute-crystal categories onS andS₀; D*(G) consequently depends only onG₀. Relative sites, filtrations and divided-power conventions are not interchangeable here.',
 'No independent proof of this site-level nil-invariance. The blank cross-reference is preserved and the exact printed witness checked.',
 'A','Search D-S07–08: publishedChapterV p108 repeats the assertion; deJong1995§2.3 supplies a modern crystalline-category comparison with explicit conventions. The full site equivalence is carried as background, not certified here.',gd,G+['D_deJong1995'],confidence='medium')
c(651,[651,652],'stated without proof',
 'The contravariant Dieudonné construction is cartesian in the base and equipsM=D*(G) withF:M^(p)→M andV:M→M^(p), satisfyingVF=p id_(M^(p)) andFV=p id_M. It agrees with classical perfect-field Dieudonné theory.',
 'Arrow domains force the corrected identity subscripts and variance. This type check does not prove existence of the functor; the published witness has well-typed identities.',
 'B','Search D-S07–08: Grothendieckp108 programme; BM1979§2Theorem2 constructs the locally free crystal. Modern exact base scopes are compared in deJong1995 and Lau2026.',gd,G+['D_BM1979','D_deJong1995','D_Lau2026'])
c(652,[653],'open on the pages',
 'Problem1 asks whether the ordinary crystalline Dieudonné functor forp-divisible groups is fully faithful over every characteristic-p base. Recovery of all geometric fibres alone is insufficient.',
 'No claimed reconstruction of the general-base counterexample: BMIII§4.4.1 is reported by two opened later primary sources, whose theorem statements and base hypotheses were read.',
 'C','Search D-S08: unrestricted full faithfulness fails (deJong1995 introduction; deJong–Messing1999§1 citingBMIII§4.4.1). Positive scopes include locallyp-based schemes (Lau2026Theorem1.9). Thus the literal universal question is negative, with qualified classifications.','Programme1970/1974; counterexample publication1990; positive comparisons1995,1999,2018preprint/2026publication.',G+['D_BM1990','D_deJong1995','D_deJongMessing1999','D_Lau2026'],present='The universal assertion is reported false in opened primary literature; the exact counterexample proof was not independently checked. Positive cases do not restore the unrestricted statement.')
c(653,[654],'open on the pages',
 'Problem1 further asks whether admissible ordinaryF-V crystals, with a locally split Hodge filtration satisfying the stated crystalline pullback condition, exhaust the image. The historical admissibility definition must be retained.',
 'No equivalence proof supplied by the programme; no replacement of ordinary by divided/prismatic objects is made silently.',
 'C','Search D-S08: Lau2026Remark1.12 explicitly compares Grothendieck’s problem; Theorem1.9 gives a classical equivalence for locallyp-based schemes, Corollary1.8 a filtered version forF-finite lci bases. Broader theorems use enriched targets.','2018first preprint;2026publication; prismatic firstpreprint2019/publication2023.',G+['D_Lau2026','D_Prismatic2023'],confidence='high')
c(654,[656,657],'open on the pages',
 'Construct a classification of finite locally free commutativep-groups using crystals with extra structure, possibly a derived filtration. The text explicitly says that it has not isolated this structure; the perfect-base simplification is tentative.',
 'No manuscript category exists to identify literally with a modern one. Comparison is at the level of the programme and its desired information.',
 'C','Search D-S09: BM1979§2Theorem3 constructs a perfect Dieudonné complex. Madapusi–Mondal2025TheoremA=7.1.1 gives a preprint classification using perfectF-gauges, a richer specified target. This substantially develops, but does not retroactively define, the old category.','BM1978meeting/1979publication; Madapusi–MondalfirstarXiv1September2025; no journal publication verified.',G+['D_BM1979','D_MadapusiMondal2025'])
c(655,[658,659],'open on the pages',
 'For a perfect characteristic-p base, Problem2 seeks an anti-equivalence between finite locally free commutativep-groups flat asΛ_n=Z/p^n-module sheaves and finite locally freeW_n(O_S)-modules withF,V, compatible with truncation. Flatness overΛ_n is stronger than being killed byp^n.',
 'Characteristic and variance are type-checked. No inference from perfect fields to arbitrary perfect schemes or from finite-level equivalences to effectivity of inverse limits.',
 'C','Search D-S09: Berthelot1980 treats perfect valuation bases; Lau–Zink2018§4 gives truncated-display comparison with explicit restrictions. These sources do not by themselves verify exactly the naiveF,V-only all-perfect-schemes formulation. The remaining gap here is exact-category comparison, not a claim that no theorem exists.','Programme1970/1974;1977preprint/1980publication;2014preprint/2018publication.',G+['D_Berthelot1980','D_LauZink2018'],confidence='medium')
c(656,[660],'stated without proof',
 'The contravariant evaluated crystal has the Hodge exact sequence0→ω_G→D*(G)_S→Lie(G*)→0. The prose’s conflicting starred tangent notation is a collation issue; these conventions state the modern comparison explicitly.',
 'Domains, duals and ranks checked. No independent proof of crystalline Hodge exactness from the fragment.',
 'B','Search D-S07–10: publishedprogramme p110; BM1979§3Prop3 and§5 compare the Hodge/co-Lie and duality structures. The typo persists in the printed programme and does not resolve the ink.',gd,G+['D_BM1979'])
c(657,[662],'corrected by himself later (both places)',
 'Across a nilpotent divided-power thickeningS⊂S′ withp locally nilpotent, lifts of a p-divisibleG are classified by locally direct-summand lifts ofω_G insideD*(G)_(S′), compatible with reduction. The final insertion is part of the statement.',
 'Read the entire correction and theorem in source and publishedp111. Only the linear filtration-lifting calculation is independently checked; the Grothendieck–Messing theorem is not reproved.',
 'B','Search D-S10: Messing1972IV2.2/V1.6 followed via opened ZinkTheorem92 and deJong1995§3.2.1; Illusie1985 reconstructs the deformation theory. Book proof itself was not opened.','1970announcement;1972Messing;1974programme;1985Illusie.',G+['D_Messing1972','D_Zink2002','D_deJong1995','D_Illusie1985'])
c(658,[662],'stated without proof',
 'The corrected programme also announces an alternative to nilpotent divided powers whenG or its dual satisfies the stated infinitesimal/ind-unipotent condition. This is stronger than merely requiring a nilpotent ordinary ideal.',
 'The exact alternative is preserved. No extrapolation from a proof of the nilpotent-PD case establishes it.',
 'C','Search D-S10: Zink2002 remark followingTheorem92 discusses removing PD nilpotence in the formal case but explicitly lacks a reference there. The exact full alternative was not located with matching hypotheses; this is a documented verification limit.','1970/1974announcement;2002comparison.',G+['D_Zink2002'],confidence='medium')
c(659,[664],'open on the pages',
 'Problem3 asks for an analogue of the deformation theorem for finite locally free commutativep-groups. The source says it has a candidate without giving it; the needed deformation object need not be an ordinary subbundle.',
 'No candidate reconstructed from silence. Finite-group derived deformation data kept distinct from the BT Hodge-bundle case.',
 'C','Search D-S09–10: BM1979§3 supplies co-Lie/derived structure; Madapusi–Mondal2025§4 andTheorem7.1.1 develop finite-groupF-gauge deformation and classification. Exact identification with the unnamed candidate is impossible.','1970programme;1979derived theory;2025preprint.',G+['D_BM1979','D_MadapusiMondal2025'],confidence='medium')
c(660,[665,666,667],'stated without proof',
 'For every Dieudonné crystal in its absolute-site sense the programme asserts exactness of the alternating reducedF,V complex and local freeness of all kernels/images on characteristic-p PD thickenings. Exactness, local freeness and crystal descent are separate obligations.',
 'Cancellation proves exactness forp-torsion-free lifts; the xy=p example shows that this argument alone does not prove local freeness. Neither zero maps nor xy=p is asserted to be a crystal counterexample.',
 'C','Search D-S07–09: publishedp113 preserves the universal assertion. Modern admissibility/divided-crystal conditions in Lau2026§3 and§8 show why an exact site/category comparison is needed. No matching unrestricted proof or actual crystalline counterexample was verified.','1970/1974programme;2026comparison.',G+['D_Lau2026'],confidence='medium')
c(661,[668,669],'proof sketched',
 'The programme answers its own filtration objection by asserting thatφ*Fil¹=kerF uniquely determines a locally split filtration; admissibility adds existence. Itsφ is the crystalline pullback, not automatically ordinary Frobenius on modules.',
 'Ordinary Frobenius over dual numbers identifies two distinct direct-summand lines; this refutes only that shortcut. The actual crystalline faithfulness theorem is not independently reproved.',
 'C','Search D-S07–08: publishedpp112–113; Lau2026§3Definition3.3/Lemma3.2 gives a precise modern admissibility framework and explicit hypotheses for forgetting filtration. The exact universal historical-site formulation remains a comparison issue.','Programme1970/1974;modern2018preprint/2026publication.',G+['D_Lau2026'],confidence='medium')
c(662,[670],'open on the pages',
 'Extend the theory by passage to inverse limits over p-adically separated complete rings, including compatible morphisms and effectivity. The heading gives no exact theorem or target category.',
 'No inverse-limit computation or proof appears on the page.',
 'C','Search D-S08–09: modern prismatic and perfectF-gauge theories treat specified p-adic formal bases. Their hypotheses/targets must be supplied before identifying a particular result with this heading.','Programme1970/1974;2023published prismatic theory;2025finite-group preprint.',G+['D_Prismatic2023','D_MadapusiMondal2025'],confidence='medium')
c(663,[671,672],'open on the pages',
 'The headings “isogenies … Tate” and “duality” announce further comparisons, without specifying a realization or every duality convention. They do not assert full faithfulness of geometric-point Tate modules in characteristicp.',
 'The earlier-runμ_(p∞) example refutes the naive geometric-point realization, not the programme heading. It is recorded as an item check, not as a false theorem of his.',
 'C','Search D-S07–09: BM1979§5 treats crystalline duality. Supplied Codexscans49–54 continue the Tate/isogeny programme and receive their own exact claims. The heading alone is too broad for a single final theorem.','1970/1974programme;1979duality.',G+['D_BM1979'],confidence='medium')
c(664,[673],'stated without proof',
 'For an abelian scheme on the programme’s nilpotent absolute crystalline site, H¹crys is locally free, cartesian under permitted base changes and evaluates as relative H¹dR; a permitted liftA′ computes its evaluation.',
 'No independent proof of proper smooth crystalline base change; theorem construction in the programme distinguished from proof.',
 'B','Search D-S07–10: programmepp114–115; BM1979§3 identifies the Dieudonné/cohomological realization. Later comparison does not remove the site and nilpotence hypotheses.',gd,G+['D_BM1979'])
c(665,[674],'stated without proof',
 'An unpolarized abelian scheme over an affine base admits a lift across the stated nil thickening; the manuscript cites Mumford. A prescribed polarization is not part of this existence assertion.',
 'The source theorem and historical locator were checked; no independent global obstruction-theory proof claimed.',
 'E','Search D-S10: Illusie1985Appendix1TheoremA1.1 dates the result to1962 and points to MumfordGITpp231–238, also noting a small inexactitude there. The opened Illusie result supplies the verified theorem.','1962result;GIT1965 firstedition;Illusie1985 exposition.',G+['D_Illusie1985'])
c(666,[675,676],'stated without proof',
 'The abelian Hodge sequence is0→f_*Ω¹_(A/S)→H¹dR(A/S)→R¹f_*O_A→0 with locally free terms and compatible base change. The transcript’sO_S is retained as a reading alarm.',
 'Sheaf domains and ranksg,2g,g checked; a cohomological proof is not supplied by correcting the letter.',
 'B','Search D-S07–10: programmepp115–116 and IllusieAppendix1 give the Hodge/deformation comparison. The sameO_S slip in the printed witness is not an ink correction.',gd,G+['D_Illusie1985'])
c(667,[676,677,682],'stated without proof',
 'Across a locally nilpotent divided-power thickening, the announced abelian-scheme deformation category is equivalent to lifts of the Hodge subbundle in its evaluated crystal. Codexscan47 continues the inverse construction but still defers its exponential justification.',
 'Square-zero subbundle lifts form a torsor underHom(F,H/F)⊗I, rankg²; this linear calculation does not prove categorical effectivity.',
 'B','Search D-S07–10: programmepp116–118; IllusieAppendix1TheoremA1.1/CorollaryA1.3 connects abelian and BT deformations. The continuation is checked at its supplied endpoint.','1970announcement/1974publication;1985verified exposition.',G+['D_Illusie1985'])
c(668,[678,682],'open on the pages',
 'Construct the crystal of universal vector extensionsE(A′) by canonical natural isomorphisms for different lifts, satisfying transitivity. Identifying objects up to unspecified isomorphism does not suffice.',
 'The cocycle/naturality obligation is explicit. Its construction is not completed by the phrase “à charge de définir”.',
 'B','Search D-S07–11: programmepp117–118; Fonseca–Matthes2024Theorems3.4/3.9 supplies a characteristic-zero D-group/crystalline comparison. Its scope is narrower than every PD setting in the programme.','1970programme/1974publication;2024modern comparison.',G+['D_FonsecaMatthes2024'],confidence='medium')
c(669,[679,680],'stated without proof',
 'Over aQ-scheme the programme asserts that the universal vector extension of an abelian scheme has a unique smooth-group lift with identified reduction across nilpotent, then general nil, thickenings. The cited old Tate letter is not identified here.',
 'The proposed cohomological first-order route is only a route: killing infinitesimal vector-field automorphisms after fixing the identity does not itself establish all group-law and limit compatibilities.',
 'C','Search D-S11: Fonseca–Matthes2024§2.1 and§3 constructs the characteristic-zero crystalline/D-group structure. The full arbitrary-nil rigidity statement and exact Tate letter were not checked from a matching source.','Programme1970/1974;2024comparison.',G+['D_FonsecaMatthes2024'],confidence='medium')
c(670,[681,682],'stated without proof',
 'The programme identifies the universal extension crystal ofA* with an appropriate crystalline R¹f_*G_m and its Lie crystal withD*(A). Components, rigidification, the absolute nilpotent site and the star onA* are essential.',
 'No identification with the unrestricted ordinary Picard sheaf is inferred. Codexscan47 supplies the explicit Lie statement missing from the Pro file end.',
 'C','Search D-S07–11: programmepp117–118 verifies the intended assertion; Fonseca–Matthes2024introduction relates the characteristic-zero universal extension to rank-one integrable-connection moduli. Exact all-base crystalline Picard conventions need further comparison.','Programme1970/1974;2024comparison.',G+['D_FonsecaMatthes2024'],confidence='medium')

def write():
    (OUT/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
    print(datetime.datetime.now(datetime.timezone.utc).isoformat(),'human-authored claims',len(claims))
if __name__=='__main__':write()
