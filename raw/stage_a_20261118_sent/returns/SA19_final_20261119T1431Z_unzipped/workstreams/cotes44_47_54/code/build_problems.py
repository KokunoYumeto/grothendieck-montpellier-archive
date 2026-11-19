"""Hand-authored index of the questions/unfinished steps actually on these sheets."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
P=[]
def problem(n,title,occ,as_he,today,art,why,worth,refs):
    P.append(dict(id=f'MP-SA19-{n}',title=title,occurrences=occ,as_he_states=as_he,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs))
problem(80,'Extending the convolution transform beyond abelian schemes',
 ['cote47 scan3, original tex2113–2140; SA19-202; CL-SA19-402'],
 'The margin proposes flat group schemes with properly supported quasi-coherent inputs, then torsors and three arbitrary kernels compatible with a mapP×Q→R.',
 'A binary integral-transform identity holds when support, Tor-amplitude and pushforward/base-change hypotheses are fixed; a monoidal structure requires coherent associativity and a unit, in addition to one binary kernel isomorphism.',
 'Laumon(1996),§1.3, verifies the relative abelian case; Stacks Project,Tag0FYP, gives kernel composition in specified derived categories. Neither asserts all marginal unbounded cases without hypotheses. Status19November2026: a standard framework exists; the unrestricted written formulation is incomplete.',
 'The manuscript supplies no subsequent completion or reason for abandoning the margin. The missing coherent/support hypotheses are mathematical omissions identified by this audit, not a documented historical motive.',
 'Worth one focused run only if a modern companion needs the exact categorical formulation and its unit/coherence data.', ['Laumon1996','Stacks0FYP'])
problem(81,'The zero-fibre compatibility in Fourier inversion',
 ['cote47 scan7 original tex2350–2377; scan8,2381–2393; SA19-205; CL-SA19-406,408'],
 'ConstructRp_*P→e_*τ[−g] and verify its compatibility on the zero fibre; the page expressly ends by leaving this check to do.',
 'Prove that this particular map, not just its source/target fibre dimensions, is an isomorphism; a perfect cone vanishing at every geometric point then vanishes.',
 'Laumon(1996),Lemma1.2.5, proves the relative formula; Mukai(1981),Theorem2.2, gives the field kernel calculation. The Koszul target hasH^i=Λ^{g−i}T^∨⊗detT≅Λ^iT. Status19November2026: result established, manuscript proof remains visibly unfinished.',
 'The text itself records the missing compatibility. It gives no reason why it was left unfinished.',
 'Worth one run to write the omitted map-level diagram with the manuscript’s determinant and shift conventions.', ['Laumon1996','Mukai1981','Stacks0621','Stacks0G99'])
problem(82,'The exponential formula for a nondegenerate line bundle',
 ['cote47 scan9 original tex2425–2447; SA19-208; CL-SA19-413,414'],
 'Forχ(L)≠0, heuristicallyΦ(L)=χ(L) times a fractional negative power of a determinant line, hencechΦ(L)=χexp(−D′/χ), over the general base being considered.',
 'Over an algebraically closed field, a nondegenerate line bundle satisfies the index theorem; in the ample caseE=Φ(L) is a bundle andch(E)=r exp(−D′/r) in rational Chow. For families retain the index, relative determinant and Todd data rather than posit an actual fractional line bundle.',
 'Mukai(1981),Proposition3.11, givesφ_L^*E as copies ofL^-1, with the index convention in the nonample case; Beauville(1983) supplies the rational Chow Fourier setting. Status19November2026: precise field statement known; the unqualified general-base heuristic has not been identified as the same theorem.',
 'The page labels the argument heuristic. No source documents the author’s reason for not returning to it.',
 'Worth a short run to formulate the exact relative family theorem and determine which base line factors survive.', ['Mukai1981','Beauville1983','Laumon1996'])
problem(83,'Modulo torsion and integral Fourier formulas',
 ['cote47 scan9 original tex2432–2468; SA19-209,210,211; CL-SA19-415–417'],
 'Are the displayed character/Chern formulas really true modulo torsion? The final line also asks for an integral algebraic-cycle lift of a rational coefficient.',
 'Separate three questions: the corrected Chern classes of one transformed bundle; integrality of its explicitly displayed multiple; and preservation ofCH/torsion by the Fourier transform for allclasses. SpecifyGr and the coefficient ring before claiming equivalence.',
 'The first two restricted ample-field statements follow from actual Chern classes; the literal expanded coefficient is refuted by the degree(1,2) elliptic product. Beckmann and de Gaay Fortman(2023),Theorem3.8, equate several integral lifting properties in the principally polarized symmetric-line-bundle setting; Question3.9 records the general problem. Hasan etal.(2025),§§3–5, work over a smooth quasi-projective base with characteristic0/liftability/base-change hypotheses and coefficientsZ[1/(2g+d+1)!]. Status19November2026: substantial partial results, no blanket integral theorem.',
 'The exact filtration is not defined on the page. The later references explain denominator/torsion difficulties; they do not document why Grothendieck dropped this question.',
 'Worth a bounded run to compare the exact manuscript integrality multiple with the modern minimal-cycle criterion; avoid launching the general integral Fourier problem as a few-hour task.', ['Mukai1981','BeckmannDeGaay2023','HasanEtAl2025'])
problem(84,'Identifying universal extensions with de Rham duality',
 ['cote54 scan3 original tex2628–2652; scan5,2685–2694; SA19-218,219; CL-SA19-426–428'],
 'IdentifyLieE(A) withH1_dR(A^∨), identify its extension as the transpose ofS_A, and extend the degree-one duality to total cohomology.',
 'The universal vector extension and the Poincaré bundle canonically give the claimed tangent and Hodge-filtered pairings; exterior powers extend them, withA/B variance and no chosenHodge splitting.',
 'Coleman(1998),Theorem2.2(i),§4 andTheorem1.1, give the extension comparison and equality/nondegeneracy of the de Rham pairings for reduced orZ-flat bases, including fields. Laumon(1996),§2.2, quotes Mazur–Messing’s exact tangentHodge sequence. Status19November2026: established.',
 'The pages call the comparison straightforward but give no construction; no historical reason for the omission is documented.',
 'Worth one run for a convention-exact companion proof and cross-reference to cote43’s duality questions.', ['Coleman1998','Laumon1996','Oda1969'])
problem(85,'Recovering the Hodge extension from the finite group schemeA[p]',
 ['cote54 scan7 original tex2721–2730; SA19-222; CL-SA19-429–431'],
 'Can the restricted Lie extensionS_A, with zero p-power on its additive kernel, be deduced from the knowledge ofp^A?',
 'ForA over a perfect field, recoverH1_dR(A), itsHodge subspace andF/V from the finite group schemeA[p]; then identify the source’s restricted p-operation and duality conventions. Geometric p-torsion points alone are insufficient.',
 'Oda(1969),Corollary5.11,p131, givesM(A[p])≅H1_dR(A) withVM=kerF corresponding toH0Ω1. Definition3.5,Proposition3.13 andTheorem3.19 specify semilinear duality and Frobenius twists. His thesis circulatedJune1967, before the1969 publication. Status19November2026: filtered finite-group reconstruction established; a local notation comparison remains.',
 'The question is explicit. Oda’s preprint/dissertation chronology is documented, but no source here says when Grothendieck learned this answer or why the sheet stopped.',
 'Worth one run to align restricted p-power, Frobenius, Verschiebung and biduality signs across cotes43 and54.', ['Oda1969','Gabriel1970','Coleman1998'])
problem(86,'Which equivalence is the proposed Albanese equivalence?',
 ['cote44 scan2 original tex2787–2800; scan8,2974–2979; scan9,2991–2995; SA19-225; CL-SA19-440,442'],
 'The letter explicitly says the relation definingJ^i is not yet well identified, while the programme definesN_ξ only in substance as a kernel.',
 'Compare separately the quotient detected by all divisor/Picard correspondences (incidence), the universal regular representative (Samuel abelian equivalence), and the algebraic Abel–Jacobi image. Determine which kernel the actual construction uses, integrally or only up to isogeny.',
 'Saito(1979),Definition3.1 andTheorem3.6, constructs the all-codimension Picard/incidence quotient; Kleiman(1971),pp445–447, separates abelian,Picard andWeil equivalence. Kahn(2021) repairs codimension2 regular universality; ACMV(2023) gives the modern functorial formulation. Ottem–Suzuki(2020),Corollary4.2, separates universal regular andAbel–Jacobi targets in codimension3 on a complex fourfold. Hernandez–Pelaez(2026) models kernels ofgiven regular homomorphisms in motives and does not supply universal existence. Status19November2026: several models exist; exact manuscript identification remains open.',
 'His own words document uncertainty about the relation. No source justifies attributing abandonment to the later counterexamples.',
 'Highest-value short research direction: build a hypothesis-by-hypothesis kernel comparison from the actual incidence correspondence and the1970–1979 sources.', ['Saito1979','Kleiman1971ICM','Kahn2021','ACMV2023','OttemSuzuki2020','HernandezPelaez2026'])
problem(87,'The uniform dimension bound needed for existence',
 ['cote44 scan2 original tex2793–2795; scan8,2974; SA19-226; CL-SA19-441'],
 'Bound every family quotientAlb(S)/N_ξ by a number depending only onX, specifically half the(2i−1)stBetti number.',
 'For correspondence-induced Picard homomorphisms fromA^i(X), prove2dimimage≤b_(2i−1)(X) forallsuch homomorphisms. For allregular homomorphisms this is a different stronger problem.',
 'Saito(1979),Proposition3.4,p110, proves the all-codimension Picard bound and explicitly creditsGrothendieck; the original argument appears in Kleiman(1971),p447. Kahn(2021),Theorem0.1, settles codimension2 for the stronger regular target. Status19November2026: the incidence bound is established and closely matches the manuscript strategy.',
 'The1964 sheets lack a proof; the later primary sources preserve attribution but do not state why this local version was left incomplete.',
 'Worth one run to reconstruct the exact cohomological injection in Kleiman/Saito and trace whether it matchesN_ξ.', ['Saito1979','Kleiman1971ICM','Kahn2021'])
problem(88,'Constructing the cycle abelian variety',
 ['cote44 scan2 original tex2796–2800; scan8,2974–2979; SA19-225,226; CL-SA19-442,444'],
 'Give the algebraically trivial cycle quotientP^i(X) an abelian-variety structure, withPicard andAlbanese endpoints.',
 'The incidence quotient is an abelian variety in everycodimension; the universalregular target needs its own existence theorem and must not be identified from dimensions or endpoint agreement alone.',
 'Saito(1979),Theorem3.6, proves the incidence statement with functoriality. Kahn(2021) andACMV(2023) verify regular representatives in codimensions1,2,dimX; no general all-codimension existence theorem was found in the2025–2026 updates checked. Status19November2026: precise incidence version established, unspecified universal version remains broader.',
 'The relation was not fixed in the letter, so its representability question was not yet a single modern problem. No later source documents a reason for dropping it.',
 'Worth developing the historical incidence construction, with separate statements for regular representatives, before pursuing any new existence claim.', ['Saito1979','Kahn2021','ACMV2023','ACMV2026Twist','HernandezPelaez2026'])
problem(89,'Complementary duality and the integral lattice',
 ['cote44 scan2 original tex2799–2800; scan8,2974; SA19-225; CL-SA19-443'],
 'J^i andJ^(n+1−i) are canonically dual; the programme’s ambiguous index is resolved only by the separate explicit letter formula.',
 'For the incidence model construct the complementary dual isogeny; determine separately whether a canonical integral isomorphism exists and what finite kernel or normalization obstructs it.',
 'Saito(1979),Proposition4.4, gives duality up to isogeny. Peters(2026),Theorem5.8, recalls the correspondence construction. The stronger integral isomorphism does not follow. Status19November2026: isogeny statement established, original exact integral wording unverified.',
 'The source does not describe an integral lattice or the full/connected kernel convention. No biographical explanation is provided.',
 'Worth one run to compute finite kernels and normalize thePoincaré correspondence in a small example.', ['Saito1979','Peters2026','Grothendieck1964Letter'])
problem(90,'What stronger Tate-module embedding was intended?',
 ['cote44 scan8 original tex2974–2976; SA19-227; CL-SA19-445,446'],
 'After asserting thatT_lJ is a quotient of a submodule ofoddcohomology, the letter expects it to be a submodule itself.',
 'The bareZ_l assertion splits noncanonically becauseT_lJ is finite free; formulate a natural, correspondence-induced or equivariant realization if the stronger expectation is to be nontrivial. The source does not explicitly give those qualifiers.',
 'ACMV(2023),Proposition8.2, constructs aGalois-equivariant correspondence map fori=1,2,dimX, l different fromthe characteristic and coprime to the chosen miniversal-cycle multiplicityr, into cohomology modulo torsion. Status19November2026: strong restricted realizations known; abstract splitting proved in thisaudit.',
 'The local letter gives no explanation of which geometric structure the stronger submodule should preserve. This is an interpretive gap rather than evidence that a bare module theorem remained open.',
 'Worth a short run to identify the missing naturality/integral-lattice condition from nearby archive material and compare excluded primes.', ['ACMV2023','Saito1979'])
problem(91,'The Hodge tangent realization',
 ['cote44 scan8 original tex2976–2978; SA19-225; CL-SA19-447'],
 'In characteristic0 replace the Weil-cohomological realization byH^i(X,Ω_X^(i−1)); the margin conjecturally putsLieJ^i inside it.',
 'For the algebraic Abel–Jacobi image overC, the tangent lies in theHodge componentH^(i−1,i)≅H^iΩ^(i−1); do not identify a full intermediate-Jacobian tangent with this single component or assert equality.',
 'Peters(2026),Lemma5.4(2), gives the family tangent inclusion inH^(i−1,i); ACMV(2023),Example1.14, identifies the algebraic image as an abelian variety. Status19November2026: exact tangent statement known for thatmodel; identification ofthe manuscriptJ remains conditional.',
 'The margin is conjectural and its relation sign is uncertain. No later historical reason for leaving it so is documented.',
 'Worth a short comparison once the equivalence relation inMP86 is fixed.', ['Peters2026','ACMV2023'])
problem(92,'Positivity of the middle incidence correspondence',
 ['cote44 scan2 original tex2802–2803; scan8,2979–2981; scan9,2989–2995; SA19-230; CL-SA19-448–450,459,461–463'],
 'For dimX=2m−1, prove the symmetric correspondenceD=r_*(p*z·q*z), after quotient by its kernel, gives an ampleNéron–Severi class; the margin insists on primitive decomposition. The letter permits the testT=Pic0(Y), codim_XY=m−1, and notes a factor2 in passing from symmetric correspondences toNS.',
 'Specify connected versus full kernel and integral versusrational descent first; full-kernel integral descent fails in the explicit elliptic-product example. Then formulate the primitive signedHodge pairing, its algebraic realization and positivity on the identified abelian quotient. The elementary factor2 construction does not prove ampleness.',
 'Saito(1979),Proposition4.4, supplies complementary isogeny duality; Peters(2026),Criterion7.3 andCorollaries7.8–7.9, gives conditional/special-case incidence comparisons using primitive algebraicity. Caibar–Clemens arXiv1109.2932 must not be counted as a solution: the final version was withdrawn19February2013 because of an error in the last theorem’s statement. Status19November2026: identified abelianAJ parts are polarizable; this exact canonical integral incidence claim remains stronger.',
 'The manuscript expressly marks positivity unproved and primitive decomposition necessary. The only documented later abandonment in this audit concerns the withdrawnCaibar–Clemens preprint; no such reason is known forGrothendieck’s own work.',
 'Worth a few-hour run on quotient normalization and thePic0(Y) test; the general positivity/standard-conjecture question is not a bounded short task.', ['Saito1979','Peters2026','CaibarClemensWithdrawn','ACMV2023','MoonenAVDuality'])
problem(93,'Height equals intersection in a hyperplane pencil',
 ['cote44 scan4 original tex2850–2871; SA19-229; CL-SA19-451,452'],
 'Relate theNéron–Tate pairing of algebraically trivial restrictionsZ|Y,Z′|Y to(−1)^mZ·Z′; expect both sideszero except the balancedmiddle case.',
 'For a fixed regular model over a curve, choose vertically orthogonal cycle extensions and a normalized geometric height. In dimension2 this becomes the negative intersection of corrected degree-zero divisors; higher-cycle statements require a suitable height theory and algebraic representatives.',
 'Ulmer(2014),§4.3,Proposition4.3.1 in thearXiv version, proves the divisor height/intersection construction; overF_q it becomes the canonical height after multiplyinglogq. Hiserrata limits some general-ground-fieldclaims, so finite/algebraicallyclosed bases are retained here. Künnemann(2001),Corollary1.7, is a higher-cycle abelian-number-field result, not the assertedgeneric-pencil theorem. Status19November2026: restricted analogue established; sourceformula lacks essentialnormalizations.',
 'The author leavesmundefined outside thebalancedcase and supplies no model/vertical-correctiondata. Laterheight theory explains these mathematical requirements but gives no documentedreason forhis stopping.',
 'Worth one run to work out the n=2 Lefschetz-pencil case exactly, including blow-up and fibre corrections, before attemptinghighercodimension.', ['Ulmer2014','UlmerErrata','Kunnemann2001'])
problem(94,'Fibration and local variants of the height identity',
 ['cote44 scan4 original tex2872–2874; SA19-229; CL-SA19-451'],
 'The source expects a more general fibration statement and a local variant of the pairingformula.',
 'Formulate local biextension/height pairings on specified models, with verticalcorrections and normalization; compare them to intersection only in hypotheses ensuring independence of the extension.',
 'Künnemann(2001),Theorem1.6 andCorollary1.7, establishes a model-theoretic route forabelian varieties overnumberfields; Ulmer(2014),§4.3, explains the geometriccurve/Jacobian case. These are exact restricted developments; no sourceopened settles the manuscript’s unspecifiedall-fibrationversion. Status19November2026: partlydeveloped.',
 'Thepage provides only an expectation, with no definite local formula. No historical reason forits omission is documented.',
 'Worth developing only afterMP93 has fixed the model and degree conventions; one run can compare one local divisor example.', ['Kunnemann2001','Ulmer2014'])
problem(95,'Lefschetz restriction for the cycle varieties',
 ['cote44 scan4 original tex2876–2885; SA19-225,229; CL-SA19-453'],
 'Theorem6 proposes low-degree isomorphism, a middle fixedfactor and high-degree surjectivity forP^i(X)→P^i(Y); its middle finite-kernel clause is crossedout.',
 'Fix the incidence orregular representative and formulate restriction in the isogenycategory first. CohomologicalweakLefschetz andfixedpart theorems do not automatically imply identicalintegralcyclevarieties.',
 'Saito(1979),Proposition5.3, gives a precise hyperplane propagation ofincidence/AJ isogeny comparison. ClassicalPicard endpoints andcohomologicallowdegreesare known; the full three-clause integral statement forunknownP^i is not identified. Status19November2026: partial/conditional comparison, not a completed universaltheorem.',
 'The source provides no proof and explicitly withdraws thefinitekernel phrase. No reason beyondthevisible correction is documented.',
 'Worth one run on thePicard andthreefold cases, preserving thewithdrawnclause andcheckingthefixedpartdefinition.', ['Saito1979','ACMV2023'])
problem(96,'Numerical versusτ-equivalence',
 ['cote44 scan6 original tex2942–2944; SA19-231; CL-SA19-454,460'],
 'Theorem7 asserts numericalequivalence equalsτ-equivalence for cycles on a smoothprojectivevariety, withMatsusaka in the margin;τ is notdefinedlocally.',
 'Ifτ is algebraicequivalence up to nonzerointeger multiple, retain the theoremfordivisors and rejectthe all-codimensionextension; first check theink andnearbydefinition beforeidentifyingthe intendedclaim.',
 'Grothendieck(1962),FGA VI§4,p242,recordsMatsusaka’s divisorcriterion. Clemens(1983),Theorem0.2 togetherwith(0.1),gives non-torsionhomologicallytrivialcodimension2cycles moduloalgebraicequivalence onaverygeneralsmoothcomplexquinticthreefold. Status19November2026: divisorversionknownbefore1964; unrestrictedusualinterpretationfalse.',
 'The pagesdo notdefineτ and give no proof; the latercounterexampledoesnotshowthatτ wasmisread orwhytheauthorlefttheprogramme.',
 'Worth a scan/context run to decide the symbolandscope; no new proof ofthe unrestrictedusualstatement should be pursued.', ['Grothendieck1962Picard','Clemens1983','Matsusaka1957'])

(ROOT/'problems.json').write_text(json.dumps(P,ensure_ascii=False,indent=2)+'\n')
print(f'{len(P)} manuscript-grounded problems serialized; no earlier-run idea silently promoted to an authorial open question.')
