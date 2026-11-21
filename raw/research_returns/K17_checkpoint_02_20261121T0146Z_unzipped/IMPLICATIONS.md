# Implications of the checked K17 findings

Status: timed checkpoint, work continuing. Precise proofs and primary locators are in K17.tex; unresolved assertions are in its separate second part and QUESTIONS.tsv.

## Step 17 and footnote 6

The missing source statement has been recovered. K17-HOST-POINT also has a closed source proof composition for the larger Host family, retaining its cyclotomic-layer bounds as explicit hypotheses. The relevant object is a strict local-condition subgroup of H1(Spec O_E[1/l],Q_l/Z_l(-e)), not unrestricted H1. Over Q, positive even e and the source admissibility hypotheses give a weighted length bound. The coefficient normalization is ramification length; the bottom coefficient ring is Z_l, so no residue-degree factor enters the K-group application.

Finite-coefficient arithmetic duality identifies the Q negative-twist localization kernel with the dual of K_(2e)(Z){l}. The trivial/quadratic class-group argument removes the excluded primes when e is even. The two-primary groups already vanish. Consequently the stipulated Alpöge theorem yields a polynomial bound on the complete order of K_(4k)(Z). Keeping the fixed levels and exact highest-weight dimensions makes the exponent seven. Its constant is still not evaluated.

This produces explicit inequalities in k and l and a finite trace-polynomial gcd certificate. VK-POLY-CERT permits a proved multiplicity-preserving overcount and removal of an exact scalar root; explicit evaluation points for K12 and K16 are included. The required complete integral Hecke model and its coverage proof have not been computed. It does not certify the informal “100ish” range or a newly specified vanishing degree. K4=0 and K8=0 are cited established results, not consequences first proved by this run.

## Vandiver and Soulé

For odd l, K_(4k)(Z){l}=0 is exactly the vanishing of the cyclotomic class component A_l^[-2k]. Vandiver at l is equivalent to these vanishings for every k, or the finite complete residue range. The periodicity concerns the vanishing condition, not canonical isomorphism of K-groups across degrees.

For the standard full-domain odd Soulé character, its index equals the order of the matching even K-group at odd l. Thus every vanishing actually certified here gives that character's primitivity on its full domain. This does not give a unit Soulé value on a chosen weight subgroup: Sharifi's factorial comparison gives a concrete failure at l=3,m=5.

## LM6 A.44–A.45

The odd regular-prime statement is the known Sharifi theorem with Brown's rational Deligne–Ihara theorem supplying its former conditional input. Step17 is unnecessary for this implication.

The prime2 branch changes status to proved in this run, with unrestricted real ramification. The proof uses the arithmetic group C2*Z2, measure-valued Magnus expansions of its cyclotomic kernel, the actual rational tripod image, and analytic separation by odd cyclotomic weights. It has author, root and two independent whole-proof reviews. These are mathematical checks, not a new formal proof certificate or external review.

The irregular branch is now proved for every odd prime below1000. K17-POLE-GENERAL proves a sufficient criterion: Vandiver and surjectivity of cup products from the odd-character summand of H1(P,F_p). It handles every cyclic even Iwasawa component, arbitrary finite lambda, nonsplit characteristic roots and repeated roots. The parity lemma matches Sharifi2007's p-unit cup theorem to this exact input. Published computations establish both arithmetic hypotheses throughout the stated range. Prime37 also has a separate fully explicit arithmetic/pole proof.

For larger irregular primes, the remaining gate is the arithmetic cup condition and Vandiver, or a weaker noncancellation condition along the pole divisors. If Vandiver fails, the present cyclic-module criterion must also be extended. The result is a deduction checked in this run from established inputs, independent of step17 and Masullo; no publication-priority or formal-verification claim is made.

## B3, S9, and Fable suggestion 5

Nonzero integral odd classes exist independently of step17. Odd regular primes have integral free generation by Sharifi–Brown. The proposed extension from Vandiver to integral odd generation is false: at37, Vandiver holds and all matching K-groups vanish, but the image Lie algebra has a nonzero degree32 abelianized component. The included exact Vandiver37 computation and McCallum–Sharifi Theorem9.7 establish the counterexample. Kernel-field equality at37 is separately proved. At691, Sharifi2007 and McCallum–Sharifi Theorem9.11 give a second explicit failure, now in weight12 with quotient Z/691. Thus integral odd generation fails even in cases where the kernel equality and all relevant K-group vanishings both hold.

At2, K17-OUT-SAT proves exact agreement of the original outer filtration with its rational pullback. The compact-group calculation K17-2-FINITE18 then proves integral odd generation through weight18. The all-weight problem has been reduced to an integral Hall/Newton correction and Gamma-stability theorem. The finite computation does not assert that theorem.

Deligne–Goncharov's mixed Tate category over Spec Z has rational coefficients. Current rational grt1 status is checked against Hirose's October2026 manuscript, Theorem4 and section1.2. The statement and reported consequence were checked, not its whole proof. A rational GRT theorem, a Z_(2) period span, and an arithmetic Z_p image lattice are different assertions. The original round-one B3/S9 row text is not present in the supplied round-two file; no missing wording is invented.

## Cote149 scans79–85 and war-game S24

The exact inverse-limit Kummer sequences now have their invertibility and derived-limit hypotheses written out. They locate the unit completion, Picard contribution and degree-two Chern obstruction precisely. The local root-coordinate obstruction is the Kummer class of the conormal line, with opposite sign for the dual normal line.

The torsor of geometric bases is acted on by the uncompleted global unit group. All splitting classes form a torsor under continuous H1. An explicit class with valuation1/(1-l^2) on Spec Z[1/l] belongs to the latter but not the former, even though Pic=0. Therefore higher even K-group vanishing cannot by itself identify geometric tangent bases with all splittings.

The general relative normalizer/formal-tube comparison and the intrinsic recognition requested in scan85 remain separate gates. The field-case cuspidal results of Stix do not supply recognition of the uncompleted-unit subset. Four mathematical transcription flags are recorded; the absent manuscript images prevent palaeographic confirmation. The normal/conormal sign is deliberately left as the author's own flagged convention.

## SA06 E.4 and Grothendieck's frameworks

The supplied E.4 intake contains summaries, not full proofs of a general all-twist H1 table. Its rows should be updated with exact scheme, twist, local conditions and coefficient category before any comparison is asserted. Kummer twist1 and the negative twist of step17 require arithmetic duality to meet; they are not directly the same cohomology group.

SGA4 supplies Kummer and Hilbert90; SGA1 supplies local tame-cover structure; SGA5 supplies the Chern-class convention; EGA IV2 supplies the Hartogs extension step. SGA6 lambda-operations on K0 do not replace higher etale K-theory. WeilII rational purity does not detect the finite torsion bounded here. No new crystalline, divided-power or FGA representability theorem is asserted without a comparison map.

## Conditional statements made unconditional

- Sharifi's odd regular-prime implication conditional on rational Deligne–Ihara is unconditional by Brown, independently of Alpöge.
- The order bound and the exponent-seven refinement use the stipulated Alpöge arithmetic theorem and the established comparison inputs.
- The pro2 field equality and the odd-prime Vandiver/cup criterion are separate checked deductions from established inputs; in particular every prime below1000 is covered. They do not depend on Alpöge or Masullo.
- Sharifi2007 makes the relevant McCallum–Sharifi nontrivial cup hypothesis unconditional at691, giving the precise integral weight12 defect. Brown supplies the rational freeness hypothesis in the general integral comparison.
- No conclusion in this package is conditional on Masullo; no Masullo statement is used.
