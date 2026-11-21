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
])
updates={
 'QFermat-Selmer':'AR-19 and H9-T15 now supply the specific Katz value and conductor-correct Selmer bound. Remaining sufficient gate: scalar-extended Abel–Jacobi injectivity over the specified field, with field-of-definition and real-height radical issues retained.',
 'Q6':'JAC-P00–02 underB(X); P08 for specified products; P16 for every geometric abelian-type variety, in every characteristic.',
}
rows=[tuple(list(row[:4])+[updates.get(row[0],row[4])]) for row in rows]
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
'''
(D/'IMPLICATIONS.md').write_text(implications)

(D/'README.md').write_text('''# JAC1964 working package

Read JAC1964.pdf or its self-contained LaTeX source JAC1964.tex. QUESTIONS.tsv is the live question-by-question status; LEDGER.md preserves dated progress and the mandatory movement reviews. CHECK_EVENTS.tsv records what each check actually did. IMPLICATIONS.md explains the mathematical consequences. TRANSCRIPTION_NOTES.tsv distinguishes mathematical repairs from uncertain historical readings.

The proof sources, numerical scripts and their outputs, reviews and source locators are included under work/ and documentation/. External full papers are not redistributed. The accepted attached results are used as requested; no complete Lean verification is claimed. This is a research checkpoint, not a claim that every remaining question is settled. The full arithmetic complementary-height gate and the specified remaining geometric gates are explicit.
''')

(R/'documentation/CONTINUE.md').write_text('''# Continuing JAC1964

The task specification is documentation/TASK_PROMPT.md. Start time is 2026-11-21T00:51:37Z. The input archive was unpacked exactly once into sources/; restore from the original attachments and the source manifest if necessary. This package contains all current authored deliverables and documentation, without earlier checkpoint ZIPs or external full papers.

Current findings: see QUESTIONS.tsv and the paper. The principal new results through this update are primitive Th4 in every characteristic, explicit H9 counterexamples and repairs, full height theorems for abelian fourfold pencils and generic axes, actual Ab2 polarizations, exact positive Fermat height and its CM plane, the Griffiths-quotient reduction, and finite-field rational Chow=numerical for geometric abelian-type varieties. Source-level checks caught a section-wide conductor assumption in Castella; the Selmer route remains conditional.

The live open gates are: the fixed higher-dimensional axis form; new norm-zero nonalgebraic cycles after separable covers; the full arithmetic complementary Griffiths quotient and its algebraic radical; the associated Bost comparison/norm estimate or rigorously applicable height formula. The known positive Fermat plane does not span the entire Chow group by any proved theorem here. H9_constant_finite_field.tex is being developed from finite-field specialization; integrate it only after whole-proof checks.

Timing is immutable: checkpoint01 01:36:37UTC and02 02:21:37UTC have been saved; checkpoint03 due03:06:37UTC, then04 03:51:37UTC,05 04:36:37UTC, etc. First movement review is due03:51:37UTC, then hourly. No review is due before that. Stop after two consecutive reviews with no actual open-row status change or strict main-gate reduction. Do not count packaging or restating gates as movement.

Rebuild with python work/build/assemble.py, then work/build/compile.sh. The assembler is workspace-relative. The local TeX format can be regenerated by the compile script; do not rely on a stale PDF. Run python work/build/merge_checks.py after new events. Inspect the rendered PDF before final delivery. All new proofs need recorded whole-proof checks; numerical certificates must state their arithmetic assumptions and actual execution. Do not claim formal verification.

Persist scheduled checkpoint ZIPs and the final JAC1964_final.zip. Do not overwrite or nest earlier ZIPs. The user requested that work be delivered only through these ZIPs. The final package must contain every mandatory file named in the task, checked and unresolved findings separated, and the exact remaining gates. Continue the mathematics until the user's stopping rule applies or the session ends.
''')
shutil.copyfile(R/'upload/PROMPT(20261121-005045).md', R/'documentation/TASK_PROMPT.md')
print(f'Updated {len(rows)} question rows and live metadata at {now}.')
