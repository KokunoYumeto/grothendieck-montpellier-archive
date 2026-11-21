"""Refresh the live status files; dated ledger entries are append-only."""
from pathlib import Path
import csv, datetime, shutil

R = Path(__file__).resolve().parents[2]
D = R / 'deliverables'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
rows = [
('Q34','Bridge 3.4; cote44 scans2,8–9','Primitive Th4 for abelian varieties in every characteristic','PROVED','JAC-T4.1–3; T4.5 arbitrary-field descent; 032 Cor8.4'),
('Q34-raw','cote44 scans2,9, read with scan8','A single signed polarization on the full middle incidence variety','REFUTED','JAC-P03: two opposite-sign nondegenerate incidence blocks on E^3'),
('Q34-Ab2','cote44 scan2 Th3/4; ACMV Prop8.1','Actual primitive codimension-two algebraic representative of an abelian threefold','PROVED','JAC-T4.4, from032'),
('QH9a','Hunch H9(a); cote44 scan4 Th5','Uncorrected pencil height equals the ambient signed intersection','REFUTED','H9-C1: split quadric pencil in every characteristic; generic Chow restriction zero but proposed value2'),
('QH9-local','cote44 scan4 local-variant margin','Correct admissible geometric height formula','PROVED','H9-T1 Schur correction; H9-T2 specialization-injectivity criterion; explicit correction1 at each quadric singular fibre'),
('QH9b','Hunch H9(b)','Incidence-Jacobian interpretation of all homologically trivial restrictions','REFUTED AS STATED','JAC-P04 domain obstruction; H9-C1 kernel obstruction; H9-T3 retains an actual map/comparison/kernel as hypotheses'),
('QH9-full4','cote44 scan4; H9-T7/T8','Full homological-cycle height for an abelian fourfold Lefschetz pencil','PROVED','H9-T8: semipositive over the original function field; exact radical is image of total-space homologically trivial cycles'),
('QH9-axis','H9-T7; cote16 no7 scans34–40,49–50','Full height for an arbitrary higher-dimensional abelian pencil','OPEN','H9-T7: signed primitive algebraic intersection form on the fixed axis; ambient summand positive by032'),
('QH9-generic-axis','Katz–Pandharipande Cor3; JAC-P09','Full height for geometric-generic degree-d axes, d>=3','PROVED','JAC-P09 kills the primitive algebraic axis space; H9-T7 yields semipositivity and exact radical'),
('QH9-trace','cote44 scan4; Kahn Prop6.2/6.6','Height on algebraically trivial primitive incidence cycles and its radical','PROVED','H9-T9: semipositive, radical exactly inverse image of the function-field trace'),
('QH9-Ab2','cote44 scan2; ACMV2023 Th6.1/8.1,Prop8.2','Actual Ab2 of a generic threefold section','PROVED','H9-T10: variable part; fixed part for abelian ambient under032; entire Ab2 for complete-intersection fourfold ambient'),
('QH9-finite-pure','Kahn Prop3.9,Prop4.12(c),Th4.14(b)','Finite purely inseparable base extension of the full height results','PROVED','H9-T12: rational Chow invariance and height scaling'),
('QH9-finite-sep','Kahn Prop3.9,Prop4.12(c),Th4.14(b)','Full positivity after arbitrary finite separable base extension','OPEN','H9-T12: old part orthogonal to norm-zero new part; algebraically trivial part controlled; remaining new non-algebraic cycles not controlled'),
('QH9-products','cote16 no7; H9-T11','Recover algebraic Hodge positivity from primitive Th4 on X times an elliptic curve','PROVED CONDITIONAL REDUCTION','H9-T11: curve-correspondence proof gives positivity modulo numerical equivalence; D needed separately for cohomological strictness'),
('Q35-alg','Bridge3.5; Kunnemann1996 Th8.2,12.1(ii)','Arithmetic signed height on the algebraically trivial incidence quotient','PROVED AS CITED BACKGROUND','Kunnemann comparison and existence hypotheses, with exact incidence sign'),
('Q35-full','Bridge3.5; arithmetic sibling','Full primitive homologically trivial arithmetic height positivity','OPEN','AR-1 grade-one reduction; AR-2 actual orthogonal Picard Chow summand; AR-15 reduces complementary semipositivity to its Griffiths quotient; strictness also needs algebraic radical zero'),
('Q35-GRH','Alpoge Remark step5; Main.lean and Statements.lean','What the accepted analytic signs imply for heights','PROVED CONDITIONAL IMPLICATION','AR-4/5: real self-dual analytic sign plus applicable height identity with correct positive constants and local terms; Dirichlet GRH alone is insufficient'),
('Q35-Bost','Alpoge Remark step13; Gu2026 Th1.3,Prop5.3','An arithmetic slope proof of the full height sign','OPEN','AR-6/10 construct exact height line and slope criterion; missing comparison map and norm bound; AR-18 gives equivalent sum/difference surface-height ordering in dimension3'),
('QFermat-Lprime','BDP2017 Sect5.2; AR-11','Central derivative of the Fermat weight-four L-function','PROVED','AR-11 exact tail bound Lprime(2)>7/20, independently reproduced enclosure'),
('QFermat-finite','Liu Ex10.4.39 pp548–549','Exact stable Faltings-height difference','PROVED','JAC-P10: hF(J)-3hF(E_i)=log(2)/4; exact stable Hodge lattice'),
('QFermat-height','AR-8/9/12/13','Sign of the specified complementary Fourier–Ceresa height','PROVED WITH NUMERICAL CERTIFICATE','AR-13: normalized height>0.0114303576>1/100; independently rerun IEEE/Arb certificate; no Lprime-height identity used'),
('QFermat-CMplane','Milne AV Prop14.2/Th14.3; JAC-P11','Height on the CM orbit of the Fermat class','PROVED','JAC-P11: positive Q(i)-line Q eta + Q Teta; exact height matrix h(eta)I2; independent modulo algebraic equivalence'),
('QFermat-tautological','Polishchuk Th0.2(i),Remark2','Does the ordinary tautological ring or abelian-endomorphism orbit span the complement?','REDUCED; GENERATION OPEN','JAC-P12: Teta outside ordinary tautological ring; JAC-P14: entire endomorphism orbit remains exactly the known CM plane'),
('QFermat-motive','Kimura nilpotence; AEH2015 Th4.2.3(3)','Identify the complementary motive and its exact endomorphism action','PROVED','JAC-P13: N=h3(J)^G as Chow motives; JAC-P14: determinant character of M3(Q(i)); entire Chow group is a Q(i)-module'),
('QFermat-full','AR-15/16; JAC-P13/14','Full positivity on the Fermat complementary Chow group','OPEN','AR-15: height descends to Griff2(N); positive CM line known; strictness needs algebraically trivial subgroup zero and positive quotient'),
('QFermat-Selmer','Nekovar Sect2–4; Castella2025 Sect5; Dee1999 Th5.1.2','Can a Selmer-rank result close the full Chow gate?','OPEN','AR-16: dimension<=2 AND scalar-extended Abel–Jacobi injectivity suffice over a specified field; AR-17 source audit retains conductor, local-factor, Katz-value and injectivity gaps'),
('Q1','cote44 scan2 Th1','Family kernel in the incidence quotient','ESTABLISHED INCIDENCE INTERPRETATION','Saito construction; no universal regular representative in every codimension asserted'),
('Q2','cote44 scan2 Th2','Half-odd-Betti dimension bound','PROVED AS CITED BACKGROUND','Saito Prop3.4; every characteristic'),
('Q3','cote44 scan2 Th3','Higher Picard variety and complementary-index duality','PROVED AS CITED BACKGROUND','Saito Th3.6,Prop4.4: incidence quotient and rational isogeny duality; no integral principal duality'),
('Q6','cote44 scan4 Th6','Hyperplane restriction ranges and critical fixed factor','PROVED UNDER B(X)','JAC-P00–02; all abelian varieties every characteristic; JAC-P08 extends to specified products of complete intersections/curves/abelians'),
('Q7','cote44 scan6 Th7','Numerical=tau with customary saturation of algebraic equivalence','REFUTED IN GENERAL','JAC-P05: CM Fermat-quartic Jacobian in characteristic0, using Bloch Th4.1; true for divisors and zero-cycles'),
('Q7-finite','cote44 scan6; 032Cor8.3; Kahn2003Th1.10','Numerical=tau over finite fields and their algebraic closures','PROVED','JAC-P15: rational Chow=numerical for every geometric abelian-type variety; hence customary numerical=tau; all abelian varieties/all codimensions'),
('Qnext-fixed','cote44 scans8–9; cote16 scan40','Primitive fixed part of a generic ample abelian section','PROVED','H9-T4 from032'),
('Qnext-variable','SGA7I IX10.4; SGA7II XVIII6.6,6.7.2','Primitive variable incidence polarization','PROVED FOR GENUINE LEFSCHETZ PENCILS','H9-L1/L2/T6 and H9-T6a; all characteristics; no variable factor if its realization vanishes'),
('Qnext-conditionA','SGA7II XVIII6.7.2','Condition A for even-dimensional abelian pencils','PROVED','JAC-P07: explicit positive variable rank; supplies specialization hypothesis for H9-T7'),
('Qnext-CI','cote44 scans8–9; SGA7II XVII2.5.1','Primitive polarization on odd complete intersections in abelian varieties','PROVED IN STATED GENERIC-LAST-SECTION SCOPE','H9-T13: smooth fixed earlier sections, genuine last Lefschetz pencil, every characteristic; m2 actual Ab2'),
('Qnext-Newton','SGA7II XVIII6.7.2; H9-T5','Eliminate variable incidence by a finite-field Newton witness','PROVED CONDITIONAL CRITERION','H9-T5: a slope outside [m-1,m] forces variable incidence zero under irreducibility; existence of a witness remains unproved'),
]
rows.extend([
('Q7-constant','cote44 scan6; H9-T14','Numerical=tau after arbitrary extension of finite-field constants','PROVED','H9-T14: numerical=homological=algebraic over every F/Fbarp for constant geometric abelian-type varieties; rational=numerical is not asserted over transcendental extensions'),
('QH9-constant','cote44 scan4; H9-T14','Full primitive homological height on constant odd abelian varieties','PROVED','H9-T14: full domain is algebraically trivial; semipositive with radical the preimage of constant trace points; quotient Hom(J(C),B)_Q'),
('QFermat-Katz','BK2007 Def3.8/3.9,Th3.11; CastellaTh2.2.1','Nonzero Katz value at5 for the Fermat character','PROVED','AR-19: exact critical theta coefficient and integral congruence give unit residue; no ramified Rankin–Katz formula required'),
('QFermat-conductor','CastellaSect4.2; RubinII2.3/VI3.5; LZProp2.8','Rank-one Selmer implication at the actual conductor(1+i)^4','PROVED','H9-T15 separately reconstructs the arbitrary-conductor reciprocity/Euler-system/duality proof; combined withAR19 gives the specified Selmer dimension'),
('Q6-abelian-type','cote44scan4; cote16scan49; Jannsen1992Th1','Th6 for every smooth projective variety of geometric abelian type','PROVED','JAC-P16 transfers D on all products, algebraic Kunneth classes and B(X); applyP02; geometric Hodge-standard positivity remains a distinct question'),
('QH9-axis-char0','cote44 scan4; Griffiths1970 Sect2(2.7) p133','Full geometric height for every smooth fixed axis in characteristic zero','PROVED','H9-T8a: classical Hodge–Riemann makes both H9-T7 summands positive; exact radical H0; no032 needed in this characteristic'),
('QH9-isotrivial','cote44 scan4; H9-T14 isotrivial corollary','Full primitive homological height for abelian varieties geometrically isogenous to finite-field constants','PROVED','H9-T14: full domain becomes algebraically trivial; primitive height semipositive with exact actual K/k-trace radical, including inseparable isogeny descent'),
('QFermat-fields','BDP Sect5.2 pp24–25; JAC-P17','Precise fields of the complementary motive, Ceresa class, and central CM operation','PROVED','JAC-P17: N and eta overQ, T overQ(i), c(T)=-T; exact whole-Chow decomposition V_Q(i)=V_Q plus T V_Q; orthogonal height descent'),
('QFermat-AJ','AR-16a; AR-19; H9-T15; JAC-P17','Scalar-extended arithmetic Abel–Jacobi injectivity for N overQ','OPEN','AR-16a: map V_Q tensor Q5 to a one-dimensional Selmer group; injectivity equivalent overQ/Q(i) and would force V_Q=Q eta; not supplied by MurreD or finite-dimensionality'),
('QFermat-algradical','AR-15a; Vial2012 Th2,Cor4.10','Vanishing of the algebraically trivial complementary subgroup','OPEN','AR-15a: a nonzero class yields nonzero homologically trivial CH2_(0) on B times J for some JacobianB; grade-zero injectivity on every such product would suffice'),
('QFermat-specialization','AR-20; Kahn2024 Sect4/5.7','Can finite-field rational-Chow injectivity detect the arithmetic complement?','REFUTED ROUTE','AR-20: CHr(hjB)_Q=0 over finite fields if j!=2r; every good specialization of all CH2(N), including positive eta, is zero'),
('QH9-axis-smoothing','H9-T16; Saito2003 Cor2.2.4/Prop2.4.4; ItoTh1.1','Lift a fixed primitive axis class through the proposed fixed-elliptic semistable smoothing','REFUTED IN SPECIFIED GENERIC SCOPE','H9-T16: weight block survives and rational operational-Chow gluing holds, but a nonzero fixed-E algebraic lift contradicts finite-index absolute irreducibility when variable rank>2; incidence-constrained families remain a different question'),
('Q35-single-curve','AR-21; Stacks0FD4/0BGJ/01OF/01VG','Reduce the whole primitive odd Chow sign to one geometrically integral curve','PROVED REDUCTION','AR-21: Ce(W)=M z over the original number field; exact height denominator12h0M²; comparison for all such single curves is equivalent to the original sign'),
('Q35-divisor-index','AR-22; Yuan–Zhang2017 Th3.2 pp1134–1135','Does divisor Hodge index orient the sum/difference height comparison?','PROVED BOUND; SIGN UNRESOLVED','AR-22: full one-parameter family gives a symmetric absolute bound on the height; it is invariant under reversing the cubic sign and does not imply the required orientation'),
('QH9-cover-primitive0','Zhang2010 Th1 pp1–2; H9-T17','Threefold height after covers on the admissible Albanese-primitive domain in characteristic zero','PROVED','H9-T17: Alb(hz)=0 gives semipositivity, radical from numerically trivial global lifts; orthogonal hPic0 part has negative height with exact trace kernel'),
('QH9-cover-primitivep','H9-T12/17; Zhang Remark2','Positivity of new admissible Albanese-primitive threefold cycles after covers in positive characteristic','OPEN','Algebraically trivial primitive incidence domain controlled; Zhang reduction needs codim2 Hodge index on the new smooth total space;032 for abelian varieties alone has not supplied that form'),
('QFermat-AJ-image','Bloch1984 Sect4 p104; AR-23','Do the positive Fermat classes realize the entire proved Selmer target?','PROVED','AR-23: AJ5(eta) nonzero; regulator surjective overQ andQ(i); explicit Q5 splitting by the known classes pluskerAJ; no rational or real-height splitting asserted'),
('QFermat-fourfold','JAC-P18; MurreD; Xu–XuCor3.9; KimuraTh2.1','Can the possible algebraic Fermat radical be detected on a fourfold?','PROVED CONDITIONAL REDUCTION','P18: a nonzero algebraically trivial N-class gives a nonzero homologically trivial cycle in (pi1C tensorpiN)CH2(C timesJ), fixed bypi4; injectivity on this component/MurreD for these fourfolds would kill it'),
('Q35-modified-diagonal','AR-24; Zhang2010 Lem2.1.1/Th2.3.5/Conj2.4.1','Replace every complementary class by an explicit projected Gross–Schoen cycle','PROVED REDUCTION','AR-24: exact selftranspose E_N on C³ and h(z)=δ/(36M²) h(E_N Delta_e); whole-diagonal positivity and generic moduli bounds do not control this projection'),
('QH9-cover-variable','H9-T18; cote16 no7;032Cor8.4; KahnTh6.2/6.6','Reduce the primitive cover sign to one variable algebraic middle subspace','PROVED EQUIVALENCE','H9-T18: fixed primitive form on A4 timesC is positive with exact b,−3b,1/g! factors; primitive height semipositivity is equivalent to ∫v²>=0 on Alg2(X) intersectker(k_*), for the smooth incidence fourfoldX'),
('QFermat-tensors','AR-25; Zhang2010 Th2.3.5,Conj2.4.1 p27–28','Place the entire Fermat sign gate inside an explicit tensor-correspondence inequality','PROVED REDUCTION','AR-25: exact central-polynomial identification, tensor projector on C³ and h(z)=1/(16DM²) times16 normalized triple intersections; ZhangConj2.4.1 would imply semipositivity but remains additional input'),
])
updates={
 'QFermat-Selmer':'AR-19, H9-T15 and P17 give exact dimensions1 overQ and2 overQ(i). AR-16a reduces the remaining sufficient gate to scalar-extended Abel–Jacobi injectivity overQ; injectivity is equivalent overQ(i).',
 'QFermat-full':'AR-15: semipositivity reduces to Griff2(N). P17 reduces the full Q(i) height to V_Q. AR-16a supplies a sufficient single remaining injectivity gate overQ; strictness still needs the algebraic radical zero if pursued directly.',
 'QH9-axis':'H9-T7: signed primitive algebraic intersection form on the fixed axis in positive characteristic, m>2; H9-T8a closes every characteristic-zero axis.',
 'Q7-constant':'H9-T14: numerical=homological=algebraic over every F/Fbarp for constant geometric abelian-type varieties and abelian varieties geometrically isogenous to constants; rational=numerical not asserted after transcendental extension.',
 'Q35-Bost':'AR-6/10 give exact height line and slope criterion; comparison map and norm bound missing. AR-18/21 reduce the threefold sign to effective sum/difference surfaces of one integral curve; AR-22 divisor-Hodge-index bounds are symmetric and do not orient the comparison.',
 'QH9-finite-sep':'H9-T17 refutes unrestricted semipositivity in every characteristic: A=E4, separable elliptic cover unramified above critical values, new norm-zero z=hD with exact height−12d³. Corrected primitive and Lefschetz domains have different signs.',
 'QFermat-algradical':'AR-15a and P18: a nonzero class gives a homologically trivial nonzero degree-four component on the fourfold C timesJ; componentwise cycle-class injectivity/MurreD there would suffice. Equivalent Jacobian-product grade-zero obstruction retained.',
 'QFermat-AJ':'AR-16a/23: the regulator V_Q tensorQ5 onto the one-dimensional Selmer line has explicit section eta; remaining gate is kerAJ=0, equivalently overQ(i); no known real-height factorization through this kernel.',
 'QH9-cover-primitivep':'H9-T18: equivalent to semipositivity of the intersection form on Alg2(X) intersectker(k_*:H4(X)→H6(A4 timesC)); all fixed terms and the cohomological primitive correction are proved in every characteristic.',
 'Q6':'JAC-P00–02 underB(X); P08 for specified products; P16 for every geometric abelian-type variety, in every characteristic.',
}
rows=[tuple(list(row[:4])+[updates.get(row[0],row[4])]) for row in rows]
state_updates={'QH9-finite-sep':'REFUTED WITHOUT PRIMITIVE QUALIFICATION'}
rows=[tuple(list(row[:3])+[state_updates.get(row[0],row[3]),row[4]]) for row in rows]
with (D/'QUESTIONS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['id','source_and_locator','question','state','finding_or_current_gate'])
    w.writerows(rows)

implications = r'''# Implications of the checked findings

Run JAC1964-20261121. This live statement supersedes the checkpoint-01 summary; the dated ledger preserves the history. The accepted 032, Milne and Alpöge statements remain inputs, not independently certified breakthroughs in this run. The main paper gives every new deduction with its proof and exact literature locators.

## Cote 44, Th.4: incidence polarizations

JAC-T4.1–3 prove the rational primitive incidence polarization of an odd-dimensional abelian variety in every characteristic, including characteristic 2. JAC-T4.5 descends it to arbitrary fields. The curve-transfer calculation applies 032 Corollary 8.4 on a product with a Jacobian; the positive transfer factor and the half-diagonal divisor are explicit. The incidence sign is (-1)^m, distinct from the cup-product sign (-1)^(m-1). JAC-P03 shows that omitting the primitive qualification produces opposite-sign blocks even on E^3.

This realizes cote 44 scans 8–9 using the algebraic Lefschetz correspondences of cote 16, no.7, scans 34–40 and 49–50. It does not assert an integral principal polarization. JAC-T4.4 additionally proves the primitive polarization for the actual codimension-two algebraic representative of an abelian threefold; it is not merely an incidence-quotient statement.

H9-T4 and H9-T6/T6a extend the polarization to the geometric generic member of a genuine abelian Lefschetz pencil. H9-T13 extends the fixed-part argument to the stated odd complete intersections, with fixed smooth earlier sections and a generic last section. SGA 7 I IX10.4 supplies integral positive toric monodromy; SGA 7 II XVIII6.6/6.7.2 supplies the variable irreducibility. In codimension two H9-T10/T13 also identify the actual algebraic representative up to isogeny.

## Cote 44, Th.5 and hunch H9: corrected height geometry

H9(a)'s uncorrected identity and the literal scan-4 formula are refuted by H9-C1 in every characteristic: the generic restricted Chow class is zero, while the proposed ambient value is 2. Each of two singular fibres supplies a missing correction of 1. H9-T1 proves the admissible Schur-complement formula. H9-T2 gives the exact specialization-injectivity criterion under which the uncorrected form is valid on its stated quotient.

H9(b) also has a domain defect. JAC-P04 gives homologically trivial generic restrictions that are not algebraically trivial or tau-trivial; such classes do not automatically give incidence-Jacobian points. The corrected implication H9-T3 therefore retains a real map, height comparison and kernel statement. H9-T9 proves the comparison and exact trace radical on the algebraically trivial incidence domain.

The full homologically trivial geometric height nevertheless admits a stronger treatment. H9-T7 identifies its quotient by total-space homologically trivial cycles with an orthogonal sum of ambient and axis primitive algebraic classes. The ambient form is positive by032. H9-T8 closes the axis gate for abelian fourfold pencils using the surface index theorem. JAC-P09 closes it for geometric-generic degree-at-least-three axes in the stated dimensions by orthogonal monodromy. H9-T12 transports these full statements through purely inseparable extensions and isolates, for finite separable extensions, the new norm-zero homological cycles. Positivity on those new cycles, for arbitrary covers and arbitrary axes, remains open.

## Cote 44, Th.6 and Th.7

JAC-P00–02 prove the rational restriction ranges and the critical fixed-part statement under B(X), hence for all abelian X in every characteristic. The proof spreads actual cycle families and uses the blow-up formula; it does not infer algebraic representability merely from invariant cohomology. JAC-P08 extends the scope to the stated products of complete intersections, curves and abelian varieties. JAC-P07 proves condition A for genuine even-dimensional abelian pencils.

With its customary meaning, tau-equivalence is saturation of algebraic equivalence. JAC-P05 refutes numerical=tau in characteristic zero even for a CM abelian threefold, using Bloch's non-torsion Fermat Ceresa class. Divisors and zero-cycles retain their classical positive statements.

There is a different positive conclusion over finite fields. JAC-P15 applies the accepted Tate theorem, 032 Corollary8.3 (pp49–50), and Kahn2003 Theorem1.10 (p982) to prove rational Chow=numerical for every smooth projective variety whose geometric Chow motive is of abelian type. This includes every abelian variety and every product of curves, in all dimensions and codimensions, over finite fields and their algebraic closures. Numerical=tau follows. Kahn's Corollary2.2 then gives rational vanishing of positive higher K-groups over the finite field. This uses the stronger Tate input, not Corollary8.4 alone. It does not prove numerical=tau for arbitrary nonconstant varieties over transcendental characteristic-p fields.

## Arithmetic sibling 3.5

The algebraically trivial comparison is established background, cited with Künnemann's exact hypotheses. AR-1 proves a Beauville-grade reduction; AR-2 splits an actual orthogonal Picard Chow motive for CM varieties. Its height is Néron–Tate positive. The remaining sign is on a complementary Chow motive, not on a cohomological vector space of known rank.

For the Fermat-quartic Jacobian, AR-7/8 give a nonzero complementary Fourier–Ceresa class eta. JAC-P10 computes the exact finite Hodge-lattice contribution, hF(J)-3hF(E_i)=log(2)/4. AR-12 fixes the analytic normalization. AR-13 provides a reproducible IEEE/Arb certificate, independently rerun in this session, showing h(eta)>0.0114303576>1/100. This is a specified-cycle theorem; no height/L-derivative identity is assumed. AR-11 separately proves the positive central derivative of the associated weight-four L-function.

JAC-P11 makes Q eta + Q Teta a positive Q(i)-line, independent even modulo algebraic equivalence. JAC-P12 shows that the second direction lies outside the usual tautological ring. JAC-P13 identifies the exact complementary Chow motive as h3(J)^G, and JAC-P14 proves that the entire abelian-endomorphism orbit is still just this known plane. Thus more endomorphisms alone cannot settle the remaining cycle-generation question.

AR-15 proves that the algebraically trivial subgroup of the complement is in the radical against the entire complement. Semipositivity therefore reduces to its Griffiths quotient. Strict positivity also requires that algebraically trivial subgroup to vanish. AR-16 records a sufficient Selmer criterion with scalar-extended Abel–Jacobi injectivity; a Selmer dimension by itself is insufficient. AR-17 checks the actual conductor, local-factor, field and injectivity restrictions in the proposed CM literature route. In particular Castella's section-wide conductor hypothesis cannot be dropped merely because the displayed theorem does not repeat it.

AR-10 constructs the canonical adelic height line and an exact intersection formula. AR-18 gives a further dimension-three reduction to an ordering between canonical heights of effective difference and sum surfaces. Zhang's nonnegativity of each height does not prove their ordering. The Bost route still needs a comparison map and a norm estimate. Alpöge's accepted RH/Dirichlet-GRH statements do not supply a general Hecke height identity or eliminate its local terms.

## What is and is not changed for the standard conjectures and parallel runs

The new results turn accepted algebraic cycle positivity into ampleness on concrete incidence varieties and into the stated geometric-height theorems. H9-T11 conversely recovers primitive algebraic Hodge positivity from Th4 on a product with an elliptic curve, with numerical equivalence and any additional D hypothesis kept distinct. No new claim of the Hodge conjecture for every non-CM complex abelian variety, the standard conjectures for every smooth projective variety, or full arithmetic height positivity is made.

The supplied bridge's run40 questions 3.4, 3.5 and H9 are the only external-run rows treated. No completed results of runs37–39 or41 were supplied, and none are invented. Their possible implications require their actual statements and hypotheses.
'''
implications += '''
## Further gate closures at the third checkpoint

H9-T14 proves numerical=homological=algebraic with rational coefficients for every constant geometric abelian-type variety over every extension of Fbar_p, including imperfect extensions. The numerical proof specializes all intersection degrees to a closed constant-field fibre, killed by P15. It gives numerical=tau in this scope. For constant odd-dimensional abelian varieties it also proves the full primitive homological height theorem, with exact trace radical and quotient Hom(J(C),B)_Q. Rational equivalence need not equal numerical equivalence after transcendental extension.

JAC-P16 proves B(X), algebraic Kunneth components and D on every power for a smooth projective variety of geometric abelian type in every characteristic. The proof transfers numerical/homological ideals through actual summand presentations and uses Jannsen semisimplicity to invert hard Lefschetz. Th6 therefore extends to this whole class. Positivity of an arbitrary variety's specific primitive form is not inferred from semisimplicity.

The Katz and conductor gates mentioned in the earlier arithmetic source audit are now addressed by separate deductions. AR-19 computes an exact Eisenstein–Kronecker coefficient and a nonzero mod5 Katz residue. H9-T15 reconstructs the rank-one Euler-system argument at the actual conductor, without dropping Castella's section-wide hypothesis. This establishes the relevant Selmer dimension. The passage from Selmer dimension to rational Chow dimension remains conditional on the scalar-extended Abel–Jacobi injectivity in AR-16; real-height factorization through that map is not supplied by the Selmer theorem.

## Exact fields, remaining injectivity, and characteristic-zero closure

JAC-P17 descends the actual Fermat Chow motive N and the Fourier–Ceresa class eta to Q, identifies the two Fermat models overQ on this summand, and constructs the central operation T overQ(i) with conjugation c(T)=-T. The entire complementary Chow group overQ(i) is the orthogonal sum V_Q plus T V_Q, without any assumed finite generation. AR-16a gives Selmer dimensions1 overQ and2 overQ(i); scalar-extended Abel–Jacobi injectivity is equivalent over these two fields. If it holds, the known positive eta spans V_Q and its CM plane spans V_Q(i). The injectivity statement itself remains open in this investigation.

AR-15a makes the possible algebraic height radical concrete: a nonzero class would produce a homologically trivial grade-zero codimension-two class on B times J for a JacobianB. Vial's threefold Murre theorem does not supply injectivity on all such higher-dimensional products, nor the required degree-one arithmetic Abel–Jacobi injectivity. AR-20 proves a separate exact obstruction to finite-fibre detection: all good finite-field specializations of CH2(N) are zero, including eta and Teta. Thus the finite-field Chow theorem cannot close the number-field regulator gate by specialization.

H9-T8a closes the fixed-axis height question in characteristic zero in every dimension, by applying classical Hodge–Riemann to the two primitive summands of H9-T7. The remaining fixed-axis sign question is in positive characteristic and dimension at least four. H9-T14 also extends the constant finite-field height theorem to varieties geometrically isogenous to constants, with their actual function-field trace as radical. These scope extensions do not identify arbitrary new separable-cover cycles with old ambient or axis cycles.

H9-T16 tests a concrete degeneration. Correcting both the degree-one fixed component and the nonregular total space gives a semistable model with a surviving axis-times-elliptic cohomology block. Torsion attaching points even permit rational operational-Chow gluing. Nevertheless, an algebraic lift with the same fixed elliptic parameter would have rank at most two in a larger absolutely irreducible generic variable system, and cannot exist. This closes that proposed lifting route under its explicit hypotheses; it does not refute the axis sign or every incidence-constrained deformation.

AR-21 replaces an effective rational cycle by one geometrically integral curve after scaling, without extending its number field. Thus the remaining threefold comparison is a single-curve test with exact square scaling. AR-22 applies the published adelic divisor Hodge index theorem to a full one-parameter family on the normalization product. It proves an absolute bound but the inequalities are symmetric under sign reversal of the cubic Poincare intersection. They do not supply the asymmetric comparison that Bost would still need.

## A negative finite-cover direction and the exact primitive repair

H9-T17 closes the previously open unrestricted finite-cover sign question by a counterexample. Pull an E4 Lefschetz pencil back along an elliptic double cover whose branch values avoid every critical value. A nonconstant Poincare divisor D on the new fibre gives z=hD with cor(z)=0 and exact middle self-height−12d³. It is algebraically and homologically trivial, but Alb(hz) is nonzero and it is not Chow primitive. Thus homological triviality alone cannot select the positive Lefschetz sign after base change.

The corrected threefold statement is stronger and more precise than a blanket sign claim. In characteristic zero, Zhang's Theorem1 proves semipositivity on admissible cycles with Alb(hz)=0, with its stated global numerical radical. H9-T17 splits the full admissible group orthogonally into that subgroup and hPic0; Kahn's theorem makes the latter negative modulo trace. The all-characteristic primitive incidence theorem remains valid. For new nonalgebraic primitive cycles in positive characteristic, the new total-space Hodge-index form remains a gate.

AR-23 also checks that the explicit positive Fermat classes realize the entire Selmer target. Bloch's original projected5-adic class is nonzero even after rationalization; Fourier transport identifies it with eta. The regulator is surjective and has an explicit section overQ5. This isolates its scalar-extended kernel, but does not make its projection rational or identify that kernel with the radical of the real height.

The negative finite-cover example works in every characteristic: a separable pencil in |N·0| on the elliptic base, with N prime to the characteristic, gives exact norm zero by the fibre divisor sum. The intersection remains−12d³, independent of that cover degree. Zhang's positive primitive statement still has its characteristic-zero scope.

P18 confines the possible algebraic-radical obstruction to an explicit fourfold C times J and its pi1(C) tensorpiN component. The needed componentwise faithfulness is not supplied by existing Murre(A),(B) results on that product. AR-24 constructs an exact selftranspose projector on C³ carrying a scaled modified diagonal to every complementary class, with positive factorδ/(36M²) in the height. The theorem for the whole Gross–Schoen diagonal does not orient this selected component; the cited Zhang tensor formulas and conjectural sign are kept distinct.

H9-T18 proves the precise remaining positive-characteristic threefold-cover reduction. On the incidence fourfold in A4 times C, the ambient primitive form has three explicitly positive terms. The curve term transfers to J(C) times A with coefficientg!, and the vertical correction becomes cohomologically primitive using the already algebraic Lefschetz operators. Both directions then identify the height sign question with the algebraic part of ker(k_*) in the fourfold's middle cohomology. No generic-hypersurface monodromy is assumed for this special incidence family.

For the Fermat motive, AR-25 makes the modified-diagonal projector a finite rational sum of tensor products of normalized curve correspondences. Its exact central polynomial and Kimura argument identify the actual Chow projector after isogeny. The height becomes1/(16DM²) times a specified sum of16 admissible triple intersections. Zhang's proved identity applies literally; his Conjecture2.4.1 would give the missing sign but is not promoted to a theorem. This supplies a concrete tensor inequality for the full Fermat gate, parallel to the sufficient scalar-extended injectivity criterion.
'''
(D/'IMPLICATIONS.md').write_text(implications)

(D/'README.md').write_text('''# JAC1964 working package

Read JAC1964.pdf or its self-contained LaTeX source JAC1964.tex. QUESTIONS.tsv is the live question-by-question status; LEDGER.md preserves dated progress and the mandatory movement reviews. CHECK_EVENTS.tsv records what each check actually did. IMPLICATIONS.md explains the mathematical consequences. TRANSCRIPTION_NOTES.tsv distinguishes mathematical repairs from uncertain historical readings.

The proof sources, numerical scripts and their outputs, reviews and source locators are included under work/ and documentation/. External full papers are not redistributed. The accepted attached results are used as requested; no complete Lean verification is claimed. This is a research checkpoint, not a claim that every remaining question is settled. The full arithmetic complementary-height gate and the specified remaining geometric gates are explicit.
''')

(R/'documentation/CONTINUE.md').write_text('''# Continuing JAC1964

The task specification is documentation/TASK_PROMPT.md. Start time is 2026-11-21T00:51:37Z. The input archive was unpacked exactly once into sources/; restore from the original attachments and the source manifest if necessary. This package contains all current authored deliverables and documentation, without earlier checkpoint ZIPs or external full papers.

Current findings: see QUESTIONS.tsv and the paper. PrimitiveTh4 is proved in every characteristic. H9 is refuted as written and repaired: full heights are controlled for abelian fourfold pencils, generic axes, and every fixed axis in characteristic zero. Actual Ab2 polarizations, exact positive Fermat height/CM plane, finite-field rational Chow=numerical, B(X) for geometric abelian type and constant/isotrivial full homological-domain heights are proved. AR19 plus H9T15 close the exact Katz/conductor Selmer-rank gates. P17 and AR16a give rational descent and reduce the sufficient full-Fermat gate to scalar-extended Abel–Jacobi injectivity overQ.

The live open gates are: the positive-characteristic fixed higher-dimensional axis form; new norm-zero nonalgebraic cycles after separable covers in scopes not closed by cited results; the full arithmetic complementary Griffiths quotient and its algebraic radical; scalar-extended Abel–Jacobi injectivity overQ for the Fermat N; the associated Bost comparison/norm estimate or rigorously applicable height formula. The known positive Fermat plane does not span the entire Chow group by any proved theorem here. All good finite-field specializations of this complement vanish (AR20); Vial's Murre theorem does not imply the missing injectivity. H9T14, P17, AR15a/16a/20 have whole-proof checks.

Timing is immutable: checkpoints01 01:36:37UTC,02 02:21:37UTC and03 03:06:37UTC have been saved. Checkpoint04 is due03:51:37UTC,05 04:36:37UTC, etc. First movement review is due03:51:37UTC, then hourly. No review is due before that. Stop after two consecutive reviews with no actual open-row status change or strict main-gate reduction. Do not count packaging or restating gates as movement. Read the dated LEDGER for later updates to this schedule summary.

Rebuild with python work/build/assemble.py, then work/build/compile.sh. The assembler is workspace-relative. The local TeX format can be regenerated by the compile script; do not rely on a stale PDF. Run python work/build/merge_checks.py after new events. Inspect the rendered PDF before final delivery. All new proofs need recorded whole-proof checks; numerical certificates must state their arithmetic assumptions and actual execution. Do not claim formal verification.

Persist scheduled checkpoint ZIPs and the final JAC1964_final.zip. Do not overwrite or nest earlier ZIPs. The user requested that work be delivered only through these ZIPs. The final package must contain every mandatory file named in the task, checked and unresolved findings separated, and the exact remaining gates. Continue the mathematics until the user's stopping rule applies or the session ends.
''')
shutil.copyfile(R/'upload/PROMPT(20261121-005045).md', R/'documentation/TASK_PROMPT.md')
print(f'Updated {len(rows)} question rows and live metadata at {now}.')
