"""Build the requested human-readable result tables, without inventing check events."""
from pathlib import Path
import csv, hashlib, json

ROOT=Path(__file__).resolve().parent.parent
D=ROOT/'deliverables' if (ROOT/'deliverables').is_dir() else ROOT
rows=[
('Q20', 'Prompt; bridge sketch', 'Route 2 definition of c; task 1', 'What must be fixed for a meaningful uniform bound?', 'proved', 'R20;P0', 'Fix the flat rational target, integral effective signs, polarization and finite-type component. Uniformity over all rational rescalings is false.'),
('Q21', 'Bridge sketch', '2.1', 'Are bounded-complexity loci closed, and is everywhere/very-general algebraicity equivalent to uniform boundedness?', 'proved', 'R21', 'Projective relative Chow components and Baire; fixed-N version included.'),
('Q22', 'Bridge sketch', '2.2', 'Does a single tensor-compatible Hecke orbit test the fixed flat class?', 'proved', 'R22', 'Use the rational subgroup acting on H1 and fixing the chosen tensor; the special-unitary suborbit is sufficient.'),
('Q22-SCALAR', 'Bridge sketch', '2.2 scalar c_x', 'Does an arbitrary unitary similitude preserve a chosen rational Weil line?', 'refuted', 'R22;P2', 'Its K-determinant can rotate the two-dimensional rational Weil space. Use SU or track the full tensor action.'),
('Q23', 'Bridge sketch', '2.3', 'What is the precise CM dichotomy and generic-sequence condition?', 'proved', 'R23', 'André–Oort plus eventual avoidance of every proper special subvariety; bounded infinite subsequence suffices.'),
('Q24-EFFECTIVE', 'Bridge sketch', '2.4 extra divisors', 'Is the locus of bounded effective extra divisors proper closed?', 'proved', 'R24A', 'Yes when the very general Néron–Severi rank is one.'),
('Q24-SIGNED', 'Bridge sketch', '2.4 unqualified divisor degree', 'Does signed intersection degree suffice?', 'refuted', 'R24Asigned', 'The nonzero integral trace-free class (theta^g)eta-(eta.theta^(g-1))theta has signed degree zero on the dense elliptic-power orbit.'),
('Q24-SUBVARIETY', 'Bridge sketch', '2.4 abelian subvarieties', 'Is the locus of bounded-degree nonzero proper abelian subvarieties proper closed?', 'proved', 'R24B', 'Use finitely many Hilbert polynomials, subgroup specialization, and identity components; assume very general simplicity.'),
('Q24-ENDOMORPHISM', 'Bridge sketch', '2.4 last endomorphism assertion', 'Must isogeny degrees of extra endomorphisms grow?', 'refuted', 'R24C', 'For a nonzero integral nilpotent v with v²=0, 1+v is an extra automorphism of degree one. Its graph degree can grow.'),
('Q24-LEFSCHETZ', 'Bridge sketch', '2.4 blanket exclusion of divisor constructions', 'Do bounds on effective extra ingredients alone exclude every bounded final divisor-polynomial representative?', 'invalid inference; final exclusion not established', 'R24D', 'The argument only excludes uniformly bounded effective extra ingredients. Every rational Hodge class on an elliptic CM power is divisor-generated, but this does not bound the degrees of its divisor-polynomial presentations. Cancellation of unbounded ingredients is not excluded.'),
('Q24-KSTABLE', 'Bridge sketch', '2.4 order-stable subvariety assertion', 'Does an irreducible middle-dimensional subvariety stable under all nonzero scalars in an imaginary quadratic order have zero Weil projection?', 'proved', 'R24E', 'Yes for a compatible polarization; one preserving scalar with a/bar(a) not a root of unity suffices. Its restriction has degree Nm(a)^n, distinct from both extreme pushforward eigenvalues. Invariance under an unspecified finite scalar group is insufficient.'),
('Q24-DIVISOR-VANISHING', 'Bridge sketch', '2.4 divisor and curve zero-projection assertion', 'Must every cycle built from divisors and curves by intersection and Pontryagin product have zero Weil projection on the balanced CM elliptic powers?', 'refuted', 'R24F;P2b', 'For E^4 and E^8, the integral Weil basis u_n,v_n is represented by signed sums of divisor intersections. This refutes vanishing, without proving uniform bounds for final divisor-polynomial presentations along a Hecke orbit.'),
('Q24-SEED', 'Bridge sketch', '2.4 final nonzero-period criterion', 'Does one bounded effective cycle with nonzero Weil projection suffice for a fixed Weil target?', 'proved', 'P3;SQ9', 'Positive integral Weil lattice plus an explicit K-endomorphism gives coefficient and clearing bounds.'),
('Q-DENOMINATOR', 'Prompt', 'bounded degree and denominator gate', 'Can the multiplier vary when integral effective degrees are bounded?', 'proved', 'P0;P6', 'Over complex abelian families, degree controls N quantitatively for a fixed nonzero flat Hodge class. Over primes, finite-type cycle parameters give the varying-N criterion for a fixed nonzero global Q_ell realization compatible with the rational Betti class.'),
('Q-PROJECTOR', 'Bridge sketch', '2.4 polynomial K-projector', 'Compute an algebraic Weil projector and its degree cost.', 'proved', 'P1;SQ8', 'Exact rational polynomials for dimensions 4,6,8; integer-pair eigenvalue checks; restricted to the middle homological motive.'),
('Q-RAW', 'Prompt', 'tasks 2–3, raw orbit transport', 'Compute the degrees and multipliers of explicit elliptic-power seeds along the orbit.', 'proved', 'P2;P2b', 'Integral seeds have bounds (80,80) in dimension4 and (147456,175104) in dimension8; raw SU clearing and degree scale as m^(2n).'),
('Q4-EXISTENCE', 'Prompt; bridge sketch', 'task 2; T5', 'Is uniform fourfold bounded division known from Markman?', 'proved', 'M1;R21', 'Exact consequence of Markman Corollary1.6.1 and the closed-Chow/Baire reduction.'),
('Q4-TWIST', 'Markman supplied source', '§7.4; task 2', 'What clears the determinant-normalized twisted characteristic class?', 'proved', 'M2;M4', '[r] kills the actual mu_r cocycle. Multipliers r^4,2r^6,12r^8 apply in codimensions2,3,4; 2*96^6=1565515579392 for the sixfold characteristic section.'),
('Q4-PROPERNESS', 'Bridge sketch; Markman supplied source', 'Route2 mechanism; commented lines580–582', 'Does the stated proper-moduli/stability shortcut supply the bound?', 'refuted', 'M6', 'The relevant proper-moduli passage is inactive and conditional. Fixed Hilbert polynomial alone is insufficient: L^m direct-sum L^(-m). The proof instead uses local regularity and cycle loci.'),
('Q4-INPUT', 'Markman supplied source', 'genus-three seed; §9.2', 'Can the input regularity be made numerical?', 'proved', 'MR1–MR3', 'Input regularity445, evaluation rank2384568978, locally free kernel regularity449.'),
('Q4-OUTPUT', 'Markman supplied source', 'Proposition9.2.1; task 2', 'Can the output and normalized family be bounded explicitly?', 'proved', 'M7;M8;M9', 'Output regularity112; stronger nef-twist vanishing; normalized regularity2065542; source effective degree3426088289770714707027306735206400.'),
('Q4-T5', 'Prompt; bridge sketch', 'task 2; T5', 'Compute uniform fourfold degrees and denominators from Markman, including transfer.', 'proved', 'M10a;M10b;M10', 'M=4*16^6*108^3; D6=16^3*M^6*Dsrc; H3=max(1,floor(delta3² D6²/648)). For t=(a u2+b v2)/q: N<=1080qH3 and D<=3240H3 B3 D6(|a|+|b|); common multiplier uses lcm(1,...,H3).'),
('Q8-MARKMAN-SEED', 'Markman supplied source', 'Example8.2.3; task 3', 'Does the indicated genus-four cyclic ideal seed extend the semiregularity method?', 'refuted', 'M3;M5', 'For d>=3 its invariant Ext² dimension is at least8d+6>28. This does not refute other complexes or transforms.'),
('Q8-QUALITATIVE', 'Prompt; bridge sketch', 'task 3; T8 E8 branch', 'Does the fixed split E8 Weil family have bounded division?', 'proved using the cited manuscript input', 'P4;R21', 'Severn2610.00387v2 internalv1.5 TheoremA supplies algebraicity; manuscript status and targeted independent audit remain explicit.'),
('Q8-INPUT-AUDIT', 'Severn2610.00387v2', '§§4–9; AppendixA', 'Do the supplier/transfer/dominance mechanisms and finite data withstand the performed checks?', 'checked cited input; no fault found in stated audit scope', 'S1;S2;S3', 'Complete targeted proof readings of both mechanisms; group, centre, parabolic basis, Gram form and all17 geometric monodromies reconstructed exactly. Not a Lean verification.'),
('Q8-DEGREE', 'Prompt', 'task 3, explicit uniform degree', 'Can the supplier construction be made quantitatively uniform?', 'proved using the cited geometric inputs', 'SQ1–SQ7', 'G39191040, coefficient boundR, Schoen orbit-sum mass, actual globally generated divisor spanning set,40G nef comparison, two-sided2Delta lattice denominators give D8(Delta)=(4G^8Delta)^8 B0.'),
('Q8-MULTIPLIER', 'Prompt', 'task 3, explicit uniform denominator', 'Convert the seed degree into a bound for every fixed Weil target.', 'proved', 'SQ8;SQ9', 'General cap (B4 D8)^4(q_t+4T+4); principal target formulas and one common LCM multiplier are fully explicit.'),
('Q-EQUIDISTRIBUTION', 'Prompt', 'task 3 arithmetic bullet1', 'What cycle information would Hecke equidistribution turn into uniform boundedness?', 'proved reduction', 'A1', 'A fixed positive asymptotic mass in S_C or one uniform first moment suffices. Without boundedness, complexity escapes in probability.'),
('Q-GRH', 'Prompt; Alpöge', 'task3; Remark steps3,5 and footnote3; Main.lean/Statements.lean', 'Do the positive family bounds depend on RH, Dirichlet-GRH, or general Hecke-GRH?', 'proved dependency statement', 'A1–A3;M10;SQ1–SQ9', 'No. Full-Hecke-packet equidistribution input used here is unconditional. Alpöge is carried as a cited theorem, not formally recompiled.'),
('Q-MASULLO', 'Prompt; supplied statements index', '§1.2 as attributed; Theorem13.3.1.1 PDFp522', 'Which exact Masullo premise is available and used?', 'current source limit at session close', 'U6', 'Only the index was supplied; it identifies Trace Formula13.3.1.1 but no verifiable numbered general-GRH conclusion. General Hecke-GRH remains conditional and unused.'),
('Q-HEIGHT', 'Prompt', 'task3 arithmetic bullet2', 'Does fixing K bound Faltings heights throughout the polarized Hecke datum?', 'refuted', 'A2', 'For the fixed integral block-action family of type(1^n,3^n), hF(E_(7^r)^(2n))=2n hF(E)+nr log7. This is not an unbounded-cycle-complexity example.'),
('Q-POSITIVITY', 'Prompt; Alpöge', 'task3 arithmetic bullet3; step5', 'Does a positive realization pairing alone bound effective degrees or saturation?', 'refuted as a formal inference', 'A3', 'Fixed-lattice monoids generated by(m,1),(m+1,1) require sign degree m+1 for target(1,0); separate mZ lattice has multiplier m. These are logical, not geometric Hodge, counterexamples.'),
('Q-PRIMES', 'Prompt; bridge sketch', 'main question; 2.5–2.6', 'State and prove the exact bounded-prime lifting criterion.', 'proved', 'P6', 'For one fixed smooth projective model over a number field and a fixed nonzero global Q_ell realization compatible with the rational Betti class, a common bound for the integral effective sign degrees at infinitely many geometric residue fibres suffices even when N_v varies. An occurring N_0 lifts with the same D.'),
('Q-032-SCOPE', 'OpenAI032 supplied PDF', 'Remark8.5 printedpp50–51', 'Does pointwise specialization algebraicity include non-CM varieties, and what remains for lifting?', 'proved source-scope consequence', 'P6;U4', 'Remark8.5 applies to any A/Qbar with good reduction, not only CM. It supplies no common integral effective degree.'),
('Q-MOTIVE', 'Prompt language requirement', 'homological and numerical correspondences', 'What motivic splitting follows from algebraic Weil classes?', 'proved', 'P5', 'The pure middle Weil summand is Q(-n)^2 in rational homological motives; no integral Chow idempotent or effective-degree inference.'),
('Q-HODGE-CONSEQUENCE', 'Prompt', 'task4', 'What follows on the families where the bound is reached?', 'proved exact consequence of cited inputs', 'M1;M10;P4;SQ9;P5', 'All fourfolds satisfy Hodge by Markman; Weil plane algebraic on fixed split eightfold family; full Hodge for all powers under full-SU Hodge-group hypothesis via Severn11.2.'),
('Q-ARCHIVE', 'Bridge sketch', '§3.2; cote16 scans44–50', 'Are scans44–50 one Coates letter dated4.1.67?', 'refuted', 'G1', 'PDF44–47 is the4.1.67 letter; PDF48–50 is a separate letter dated6.1.1966 as written. Original scans and CSGL10d/L11d agree.'),
]
with (D/'QUESTIONS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['id','source','locator','question','state','finding_ids','finding_or_current_gate']);w.writerows(rows)

implications=r'''# Implications of HECKE_DIV_20261121

The findings concern fixed rational flat classes in fixed polarized families. Degree means the intersection degree of **integral effective positive and negative parts**, without a factorial normalization. All results and proofs are in `HECKE_DIV.tex`; `QUESTIONS.tsv` records the source question for each conclusion.

## Hodge conjecture and bounded division

**The fourfold test T5 is quantitative.** Markman's Theorem 1.5.1 and Corollary 1.6.1 supply the geometric input and the qualitative fourfold theorem. M7–M10 compute an output regularity bound, its normalized Chern-cycle degrees, the maximal-order and polarization comparison, and the compensation correspondence. For the principal split datum and t=(a u₂+b v₂)/q, the bounds are

    Dsrc = 3426088289770714707027306735206400
    M = 4·16⁶·108³ = 84537841287168
    D6 = 16³ M⁶ Dsrc
    δ3 = 1701760099946011389900
    B3 = 6493952361560098735300
    H3 = max(1, floor(δ3² D6²/648))
    L3 = lcm(1,...,H3).

Each fibre has representatives with N≤1080qH3 and both sign degrees ≤3240H3 B3 D6(|a|+|b|). A single common multiplier is 1080qL3, with both degrees ≤3240L3 B3 D6(|a|+|b|). These are sufficient, nonoptimal bounds. The exact expanded arithmetic through H3 and the cap coefficients is in `work/markman_output_numbers.json`, independently checked by a separate rational-arithmetic program.

**The split eightfold question has an explicit bound, using Severn's version-specific manuscript input.** The independently inspected input is Severn (2026), internal version1.5, Hexagon2610.00387v2, TheoremA, supplier/transfer arguments §§4–5, and dominance §§6–9. The manuscript is unrefereed; the report records the full targeted readings and reconstructed finite data rather than calling it formally certified. SQ1–SQ9 extract a new explicit quantitative bound:

    G = 39191040; g = 4G+1
    R = (2G+1)G!G^G; L = 2gR
    S0 = G^(2g)(g!)²; SB = (L/2)! S0^R; k = L/2+4
    B0 = (40G)^k binom(k,4) SB · 8! · G^8
    D8(Δ) = (4G^8Δ)^8 B0.

Here Δ is the fixed polarization elementary-divisor product and the integral lattice is stable under Z[ω]. The principal balanced E⁸ datum has Δ=1. The quantity D8 is an explicit effective seed degree on an analytic open. A closed bounded-cycle locus then carries the explicit class bounds to every fibre, including the entire tensor-compatible Hecke orbit.

For a fixed nonzero t, choose q_t with q_t t integral, put T=∫(q_t t)², and B=B₄D8(Δ), where

    B4 = 497657009489489182584908205353846834744.

Then c_t≤B⁴(q_t+4T+4). For the principal basis u₄,v₄, set

    δ4 = 411891354565851759965785179617340330000
    H4 = max(1, floor(δ4² D8(1)²/31104)).

For t=(a u₄+b v₄)/q one may take N≤1265qH4 and each sign degree≤6325H4 B4 D8(1)(|a|+|b|). The common multiplier is 1265q·lcm(1,...,H4), with the same formula after replacing H4 by that LCM. The integers are specified by finite arithmetic expressions; no optimality or feasible decimal expansion is claimed.

**Scope of the Hodge consequence.** The Weil plane is algebraic on every fibre in this fixed eightfold family. If a member has full special-unitary Hodge group, the invariant-theory criterion in Severn, Theorem11.2, gives the full Hodge conjecture for all its powers. The two-dimensional calculation alone is not a proof for every additional Hodge class on every special eightfold, or for every abelian variety in every dimension. P5 identifies the resulting pure middle Weil summand with Q(−n)² in rational homological motives. The algebraic correspondence splitting passes to numerical motives, without asserting an integral splitting in Chow motives.

## What changes in the general reduction

R21 proves the full relative Chow/Baire equivalence, including the same-multiplier version. R22 requires the tensor stabilizer acting on rational H¹; SU fixes a chosen Weil class, whereas a general unitary determinant rotates the rational plane. R23 uses sequences eventually outside each proper special subvariety. R24 corrects the sketch: under the respective hypotheses of very general Néron–Severi rank one and very general simplicity, bounded effective extra divisors and nonzero proper abelian subvarieties give closed proper loci. Signed divisor degree and isogeny degree of an extra endomorphism do not give the asserted conclusions. Extra unipotent automorphisms have degree one. The conclusion excludes bounded ingredients, not every final cycle expressible through divisors with cancellations.

R24E proves the zero-Weil-projection assertion for an irreducible middle-dimensional subvariety preserved by the nonzero endomorphisms of the quadratic order. One preserving scalar with a non-torsion quotient a/bar(a) suffices; finite scalar invariance does not. R24F refutes the separate blanket vanishing assertion for divisor/curve constructions by the explicit integral divisor-product Weil cycles of P2b. Neither assertion settles uniform degrees of final divisor-polynomial presentations along the orbit.

P0 removes a separate multiplier gate when integral effective sign degrees are bounded for a fixed nonzero flat Hodge class. P3 reduces the Weil problem to one bounded effective nonzero projection and computes the ensuing coefficients using the positive integral lattice. P6 proves the arithmetic analogue for one fixed smooth projective model over a number field and a fixed nonzero global Q_ell realization compatible with a rational Betti class: a common bound for the integral effective sign degrees at infinitely many geometric good fibres suffices even when N_v varies. This condition is equivalent to rational algebraicity of that Betti class. One occurring multiplier lifts with the same degree bound. Its parameter proof uses a finite type cover with genuine relative cycles and flattening; it does not assume a universal flat subscheme on a coarse mixed-characteristic Chow scheme.

OpenAI032, Remark8.5 (printedpp50–51), applies to arbitrary A/Qbar at good reduction, including non-CM A. Its simultaneous realization statement supplies pointwise rational cycles. It supplies no common integral effective degree. This distinction is the precise remaining prime gate for a general family where no construction like M7–M10 or SQ1–SQ9 is available.

## Arithmetic routes

A1 proves the exact use of equidistribution: a positive limiting mass in one bounded locus, or a uniformly bounded first moment of c_t, forces a global bound. Conversely, if no bound exists, mass in every S_C tends to zero. Eskin–Oh (2006), Theorem1.2, is an unconditional full-Hecke-packet input. GRH-dependent Galois-orbit estimates are a different statement. No new conclusion here relies on Alpöge or Masullo.

A2 gives a fixed-field, fixed integral block-action datum with unbounded Faltings height: h_F(E_(7^r)^(2n))=2n h_F(E)+nr log7. The polarization type is (1^n,3^n); the family is decomposable and is not claimed to be a generic or high-cycle-complexity sequence. The conductor term, in Barquero-Sanchez et al. (2017), Theorem1.3, is essential. A height-dependent growing upper bound is not a uniform orbit bound.

A3 refutes the abstract inference from a positive realization pairing to bounded effective degrees or saturation, using explicit fixed-lattice monoids. Alpöge's Remark, steps3 and5, footnote3 onp3 continuingp4, concerns a trace-formula sign and Parseval cancellation; it is not an effective Chow estimate. The supplied Main.lean and Statements.lean entrypoints were inspected, but the full imports were not compiled. The user's theorem convention is retained. Masullo's general Hecke-GRH statement remains a conditional, unused premise: the supplied index identifies Theorem13.3.1.1, Trace Formula, PDFp522, but does not provide the exact numbered general-GRH assertion attributed to§1.2.

## Tate and standard conjectures

The supplied CM-Hodge theorem (OpenAI032, Theorem1.1; van Hoften–Sempliner, TheoremI) and Milne's report (2026, Theorems2.1,3.1,3.5) are external inputs. Milne's report records the full Tate conjecture for abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties. Those statements are not newly proved by this run. They establish structure and positivity for algebraic correspondences under the cited framework; A3 explains why they do not alone provide effective positive/negative representatives for an arbitrary Hodge tensor. No new claim about Tate over number fields is made.

## Exact Grothendieck locator map

Archive scan numbering below means one-based PDF pages including the cover. The printed folio is one less on the inspected cote16 pages. These are framework correspondences, not assertions that Grothendieck's pages contain the new estimates.

| Findings | Cote/scan or foundational locator | Precise relationship |
|---|---|---|
| R20, R24E–F, P0, P1, P2, P2b, P3, P5, SQ8–SQ9 | Cote16, §7, PDF14–17 / folios13–16; §8, PDF18 / folio17 | Integral exterior cohomology, wedge/contraction, Lefschetz correspondence ring and index pairing. No effective cycle bound occurs in those pages. |
| R21, R24A–B, M1, M4; globalization in M10 and SQ9 | FGA, Bourbaki exposé221, Theorems3.1–3.2, pp259–260; relative Chow refinement Kollár Definition3.21(3.21.1–2),p119 | Projective parameter spaces; distinguish fixed Hilbert polynomial from bounded degree. |
| R22, R23, SQ2 and SQ7 local-system comparison | SGA1, ExposéXII, Theorem5.1 | Finite topological covers algebraize; modern real approximation, isogeny and André–Oort statements retain their own exact sources. |
| M2, M3, M5–M10, MR | FGA exposé221, Theorems3.1–3.2; SGA6, ExposéX, Appendix§7, equation7.13.10,pp578–579 | Coherent sheaf/cycle framework and rational cycle-class compatibility. The analytic openness actually used is Grauert1960, §7 Satz3,pp62–63, not a falsely quoted algebraic EGA theorem. |
| SQ2–SQ7 geometric supplier cycles | Cote16 §8 PDF18 / folio17; SGA1 XII5.1; FGA221 Theorems3.1–3.2 | Algebraic correspondences, finite covers and projective cycle loci. Schoen and Milne supply the modern construction and invariant theory. |
| P6 | SGA4, ExposéXVI, Corollary2.2; SGA6, ExposéX, Appendix§7, equation7.13.10,pp578–579 | Smooth proper specialization and compatibility of rational cycle classes. Mixed-characteristic cycle parameters use Suslin–Voevodsky4.4.11/4.4.13 and flattening2.2.2; the trait uses Stacks054F. |
| P5 and A3 | Cote16 first Coates letter dated4.1.67, PDF44–47 / folios43–46; separate letter dated6.1.1966 as written, PDF48–50 / folios47–49 | Lefschetz inverse, index and semisimplicity structure; rational correspondence positivity does not control effective presentations. |
| A1–A2 | Cote16 correspondence framework; no archival equidistribution or Colmez formula asserted | Modern exact inputs: Eskin–Oh1.2 and Barquero-Sanchez et al.1.3. |
| G1 | Cote16 PDF44–50 / folios43–49, original letter headings | The sketch conflates two letters; the second date reads6.1.1966 as written. CSG L10d/L11d agree. |

No original cote44 or cote47 page was used. No new transcription correction is asserted there. `TRANSCRIPTION_NOTES.tsv` contains the one verified bibliographical correction, with its confidence and limitation.

## Mapping to the supplied sketch and earlier run labels

| Source run/label | Effect of this run | Certification boundary |
|---|---|---|
| HODGE_BRIDGE_SKETCH_20261121,2.1 | R21 proves the reduction with all hypotheses and fixed-N variant. | Directly checked supplied statement. |
| Same,2.2 | R22 fixes tensor compatibility; P2/P2b compute raw scaling; M10 and SQ9 provide uniform replacements in the test families. | Distinguish one class from the full Hodge conjecture. |
| Same,2.3 | R23 proves the strict-generic-sequence dichotomy without GRH. | Eventual avoidance is essential. |
| Same,2.4 | R24A–F retain valid closed loci, refute the literal degree and blanket-vanishing claims, and prove the order-stability assertion; P1/P3 prove the effective seed criterion. | No blanket exclusion of all divisor-built final cycles. |
| Same,T5 | Closed by M7–M10, with explicit normalized fourfold bounds. | Sufficient bounds, not minimum complexity. |
| Same,T8, E8 branch | Closed for the fixed polarized integral split Weil datum by SQ1–SQ9 using checked Severn input. | No blanket all-orders/all-polarizations constant. |
| Same,2.5–2.6 and T9 | P6 strengthens the lifting equivalence to varying N_v; Remark8.5 scope verified. | Does not compute the least degree of the specific032 transported cycles as a function of p; that is assigned to the separate ghost-prime run. |
| Same,T6–T7 | No new Rallis-degree identity or semiregularity theorem for the032 surface is asserted. | These are separate supplied parallel-run tasks. |
| Same,3.2 | G1 corrects the two-letter attribution. | No CSG transcription error claimed. |
| War game of12Nov,H8; RESEARCH_SA06,C.4a–x | P1/P2b/P3 provide independent explicit integral-lattice and denominator calculations relevant to the stated programme. | Original run packages not supplied; their statement-level proofs not certified or rewritten. |
| War game,H7 and H9; sketch3.4–3.5; cote44/cote47 | No new conclusion on their uninspected statements. | Archive and prior-run proof sources absent from this run. |
| RESEARCH_SA06,C.2c,C.2h,C.2j,C.3ac,D.4f,E.2a; RESEARCH_SA07 labels in sketch | Milne's cited consequences remain relevant background. | No row-by-row transfer claimed without those original statements and proofs. |

## References and source status

The paper's bibliography gives APA-style author-year entries with exact theorem/section/page locators. The unrefereed Severn input, the supplied2026 theorem convention, the unavailable Masullo theorem numbering, and the absence of previous run packages are explicit. All new proof checks are recorded in `CHECK_EVENTS.tsv`; ordinary exact computations are not described as formal proof-assistant verification.
'''
(D/'IMPLICATIONS.md').write_text(implications)

manifest=[]
for p in sorted((ROOT/'source').rglob('*')):
    if p.is_file(): manifest.append((str(p.relative_to(ROOT)),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),'supplied input; unpacked once'))
with (D/'SOURCE_MANIFEST.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['source_path','bytes','sha256','provenance']);w.writerows(manifest)
print(f'Wrote {len(rows)} question rows, implications, and {len(manifest)} supplied-source hashes.')
