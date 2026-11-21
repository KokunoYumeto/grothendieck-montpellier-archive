# Implications of HECKE_DIV_20261121

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
