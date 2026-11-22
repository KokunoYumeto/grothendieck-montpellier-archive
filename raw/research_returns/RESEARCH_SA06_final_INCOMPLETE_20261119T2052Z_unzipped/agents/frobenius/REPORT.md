# Part B and E.2 contribution

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited reasoning effort, run `/root/frobenius`. No priority claim is made.

| Requested item | State reached | Statements |
|---|---|---|
| B.1 | Proved, with the stronger exponent m=1; semisimple numerical-motive interpretation made precise | B.1a–B.1b |
| B.2 | Proved in every weight, including 0, 2, 3 and all listed edge cases | B.1a, B.2a, B.3b |
| B.3 | Proved for unrestricted number fields; fixed-field obstruction illustrated but refuted as an obstruction to realization | B.3a–B.3b |
| B.4 | Exact integral cokernel determined, including its 2-part; unpowered canonical-point premise refuted; corrected points, finite lift criterion, and explicit sufficient powers proved | B.4a–B.4g |
| E.2 | Arithmetic cone proved; integral normalized cocharacter and global finiteness refuted; motivic effectivity statement conditional on Tate classification | E.2a–E.2e |
| Lead B1 | Conclusion proved and strengthened; m=i works even if factors must remain in the original number field, m=1 allows root extraction | B.1a, B.3a |
| Lead B2 | False as a realization obstruction. Exact class/unit lattice obstruction and additional torsion issues identified | B.3a, B.4a–B.4f |
| Lead E1 | Precise rational finite-field version proved via facet normals; no integral normalized cocharacter on full M(q) | E.2b, E.2d |

## Principal findings

For a positive-weight Weil integer λ, choose α with α^i=λ. Integrality and the absolute-value condition imply that α is a weight-one Weil q-integer. Honda–Tate gives A/F_q, and H^1(A)^{⊗i} embeds as a Künneth summand in H^i(A^i). This is already implicit explicitly in Milne's Proposition 2.6 proof (there via restriction of scalars). It settles the supposed all-weight realization difficulty without a class-group argument. The prior sweep's assertion that higher-weight strong realization was open is wrong.

The lattice cokernel is not merely its image in Cl(L): its kernel is `(N(E_{L,S}) ∩ E_K)/N(E_L)`, and the full group extension is specified by a kernel presentation. This retains the 2-primary information rather than discarding it. A Smith-normal-form recipe is included for arbitrary finite Galois CM L.

R7's claimed point of D(M0/torsion) evaluating [u] as u is not defined, since [u]=[ζu]. Also D(M0/torsion) is the connected weight quotient, not automatically the connected kernel of the Tate character. A corrected powered point evaluates [u] as u^k for |μ(L)| dividing k. For the divisor isogeny its rational lift is characterized by finite norm-one equations over the decomposition field. The exponent `2 h_L |D_p| |μ(L)|` suffices (h_L may be replaced by the class-group exponent). For normalization in ker ε, the corresponding even power is specified separately. Merely changing q while resetting the full norm-one group changes nothing; base change acts through u↦u^k.

## Background read and checked

- Attached prompt: Part B, E.2, Leads B1/B2/E1, R5/R7/R13, proof and deliverable requirements.
- `sweep3_SA06/STUDY.md`, section 1: read and independently re-proved the norm-one anti-divisor construction actually used. Corrected its higher-weight-open status.
- `sweep3_SA06/readings/c14_c15rest.md`, Part 3 section B: read the claimed cokernel and lifting proofs; corrected the evaluation-on-quotient error and the compact-torus conflation.
- Primary transcriptions: 15:88, 90, 96, 98, 100, 106, 110–114, 121; 14:3, 5, 9, 11. The unrelated reused-paper content at 15:111 and 113 was identified as such and not used mathematically.
- No remark from Michel Hua's project was used.

## Computations

`code/verify_frobenius_cases.py` uses exact Python/SymPy arithmetic. Its scope is finite certificates, not a search over all CM fields or all Weil numbers.

Inputs: F8=F2[t]/(t³+t+1), E:y²+xy=x³+x²+(t+1); discriminant −23; the Gaussian example λ=15+20i with q=25.

Output: five affine E(F8) points and the origin, hence trace 3; Frobenius polynomials T²−3T+8 and T⁶−3T³+8; exact exterior-cube polynomial `(T²−3T+8)(T⁶−24T³+512)³`; the three reduced primitive forms of discriminant −23; no norm-2 integer in the proven certifying range; Gaussian slopes 3/2 and 1/2. The full output is in `output/verify_frobenius_cases.json` and `.txt`. Runtime for the recorded run: 0.160232 seconds, SymPy 1.14.0. All assertions passed.

The class-number assertion h(−23)=3 is proved independently from Minkowski's bound and ideal relations in B.3b; the form enumeration is a check, not an unsupported inference from a partial search. The cohomological significance of the 20×20 matrix is proved in B.3b: it is ∧³ of the H¹ Frobenius companion matrix.

## Source search and opening record

| Source | Opened status and exact locus | Use |
|---|---|---|
| Tate, Classes d'isogénie, Exposé 352 (1971 publication; talk November 1968) | Opened complete PDF; Theorem 1(i)–(ii), p.96; §3 Lemma1, p.100; screenshot checked for formulas on p.96 | Honda–Tate existence, dimension and restriction of scalars |
| Milne, Motives over finite fields (1994), corrected 2019 manuscript | Opened; Proposition2.6 and Remark2.7, pp.13–14; Proposition2.27, p.23 | All-weight realization already known; Tate hypothesis on arbitrary motive classification |
| Milne, original 1994 author manuscript | Opened; pp.25–26, definition preceding Proposition2.27 | Its W^L(q) has an extra normalized-valuation condition and is not the M0 of the prompt |
| Jannsen (1992) | Opened complete PDF; Theorem1, p.448; Corollary1, pp.449–450; Remarks1–2, p.451 | Numerical semisimplicity; nilpotent kernel for algebraic Künneth projectors |
| Deligne, Weil I (1974) | Opened; Theorem(1.6), p.276 | Necessity of integral and weight conditions |
| Milne, Algebraic Number Theory v3.08 (2020) | Opened; Theorems4.3–4.4, Theorem5.1 | Minkowski bound, class-group finiteness, units |
| Honda (1968) | Subsequently opened full primary paper through a mirrored PDF; unnumbered Main Theorem p.83, Propositions1–4 p.85, Theorem1 p.86, Theorem2 p.87. Rochester and J-STAGE PDFs failed; Project Euclid returned a service notice. See A_review.md for exact URLs. | Original existence theorem now directly verified, independently of the opened Tate exposition |

Queries used: Honda–Tate classification and Tate exposé352; Milne motives finite fields all-weight Weil-number realization; Jannsen numerical semisimplicity; Deligne Weil I theorem1.6; precise norm-one lattice and normalized W^L(q) definitions. No newness claim is made for the elementary deductions or norm-lattice calculation; a separate publication with the identical integral presentation was not located.

## Independent review of the root's Part A draft

Read `sections/A_deuring.tex` at the parent's request. Confirmed the minimal-index proof of the unique integral rank-two slope-1/2 lattice, the centralizer Zp* ambiguity, and the torsor argument after geometric realization. Flagged and corrected the orientation convention: with covariant action a↦(a∨)* on Hcris¹, the raw action on M/FM gives the tangent-space orientation in the supersingular case; an additional bar would reverse it. Parent agreed to repair via the Hodge sequence. Suggested making the Morita determinant comparison explicit through P=Hom(E,E'), deg(ta)=deg(t)Nrd(a), and primitivity of the degree ideal, rather than suppressing a possible local unit. The explicit F9 crystal counterexample and F7 quadratic-order counterexample were independently checked algebraically from the draft.

No passages have been removed from the contribution. A preliminary sentence incorrectly suggesting that the first 2g abelian-variety point counts directly determine H¹ Frobenius was replaced before delivery by an exact finite-torsion computation with coefficient bounds; that correction is mathematical, not a reported computation.

The independent `/root/real_weil` agent checked B.4d–B.4f. It confirmed the divisor factor 2, the decomposition-group norm factor, the root-of-unity exponent, the character-lattice identification, and the normalization into U^0. A missing TeX backslash was fixed; no mathematical fault was found in that targeted check.

## Subsequent Part A contribution and additional source verification

The parent assigned a second targeted review. The substantial result is a counterexample to the unrestricted ramified base-change Picard claim under the general module-category definition of Deuring categories. `A5_counterexample.tex` gives the complete proof; `A_review.md` explains its exact scope and determinant rigidifications. An exhaustive F9 certificate is supplied, and `/root/real_weil` independently confirmed the mathematical proof and the rigidification typing.

`A_review.md` also checks the A.2c/A.3a/A.4a sign and torsor claims, makes the positive global transport in Eq(C) explicit, and refines the A.1e intertwiner construction using scalar Hilbert 90. An unimplemented all-prime evaluator is a computational limitation, not a missing proof of the abstract explicit rule.

Honda1968, SGA4 XVIII Proposition1.4.15 and Corollary1.4.17, Langlands–Rapoport1987 Satz4.4 and conjecture5.e–5.g, and Kisin2017 Theorems0.3,2.2.3,4.6.7 were opened and their exact hypotheses checked. The new bibliography is kept separately in `additional_references.bib`; additional result rows are in `additional_results.csv`. All related check events are appended to `CHECK_EVENTS.tsv`.
