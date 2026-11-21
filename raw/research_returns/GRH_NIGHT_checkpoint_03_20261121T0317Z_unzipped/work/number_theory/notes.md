# Number-theory work notes

Owner: `/root/number_theory`; model GPT-6 Astra Pro; effort not exposed; run GRH_NIGHT/number_theory. Current work date 2026-11-21 UTC.

## Scope and evidence discipline

The 78-row current catalogue and `section.tex` are current working deliverables. A is the user-designated Alpöge theorem, without a claim to verify missing Lean imports. Every M result remains conditional. Existing IA02/IA09 and CX-N rows are carried background with precise links, never counted as new discoveries.

`evidence/` contains downloaded external publications and temporary page renderings for reference. **Exclude this directory from checkpoints/final deliverables.** `sources.json` retains URLs, exact locators, hashes where available, and verification scope. No full external publication is being redistributed. Our own proofs and notes are original prose, with no deliberate long literal quotations.

## New useful formulations

- NT-F01: explicit Chebotarev transfers to every class function with normalized L1 error.
- NT-F02: finite étale point-count average has error proportional to the number r of generic components; for a connected cover the main error is independent of degree. Additional removed primes cost at most d|S|log x.
- NT-F03: exact splitting-type counting from unions of conjugacy classes.
- NT-F04: finite-prime avoidance has an explicit count criterion; do not silently append arbitrary exclusions to Bach–Sorenson's least-prime theorem.
- NT-L02/03: a full fixed-character Lindelöf deduction, preserving nonuniform conductor dependence and handling pure norm twists.
- NT-H03 and NT-L06 are short useful formulations of classical inputs, not claims to a new general class-number or cancellation theorem.

## Source details resolved

1. Corrected LLS arXiv v3, not an earlier formula, is used throughout.
2. Grenié–Molteni2019 Theorem1.1/Corollary1.2 constants and unramified conventions inspected on images.
3. Shoup1992 Theorem3 original p4 inspected: r^4(log r+1)^4log²p.
4. Lenstra1977 Theorem9.1 original p218 inspected: #S≥2. OCR >2 was wrong.
5. Hughes–Rudnick first zero is nonnegative, including possible central zero; definition on p1. Mean/variance/low moments are unconditional analytic identities, with A supplying real ordinates.
6. ILS2000 p56 explicitly assumes family GL2-RH as well as Dirichlet GRH. The latter alone does not discharge Theorem1.1.
7. Milne CFT v4.03 VI Cor2.12/Example2.13 p191 confirms the ordinary class-number/full-unit-regulator convention.

## Gates and next routes

- Schoenfeld Corollary1 source gate resolved by an independent directly retrieved primary proof: Johnston2022 Theorem3.2 equation(3.6), with normalization explicitly addressed in §2. It also gives ψ threshold59. Original1976 page remains uninspected, but is not needed to certify the consequence.
- Bach1990 Theorem4 original AMS pages are unavailable; the exact inherited source locator is carried, not mislabelled as freshly inspected. Complexity agent owns the full algorithmic row.
- Hooley original final theorem locator is pp219–220; original endpoint blocked. The fully inspected Lenstra1977 Theorem3.1 already gives the density implication, so this is a bibliography-detail gate rather than a reason to omit the consequence.
- Quadratic-family symplectic low-zero density: the 1993 Özlük–Snyder paper has a smaller support range than the later 1999 theorem. Do not conflate them. The original 1999 download remains unavailable. The directly inspected FPS2017 Theorem1.1 now supplies the exact χ_{8d} family statement in NT-Z11 and the full ≥15/16 nonvanishing deduction NT-Z12.
- Further useful additions: exact quadratic-family nonvanishing proportion after the actual family/weight is checked; Li coefficients; prime-race hypotheses including LI; explicit AP Chebyshev bounds; optimal-density family moment theorems where primary sources are available.

## Peer review

Read root MT-L01 and MT-L02 in their entirety. Core proofs pass: normal convergence, no-invariant cancellation at s=1, meromorphic logarithmic derivative and integer residues. Requested the final standalone equivalence to explicitly include trivial ζ_K or say nontrivial Artin factors. Recorded targeted proof-check events. Geometry agent read NT-F01–04 in full and passed the proofs, with a finite-base interpretation correction in NT-F03 and a TeX typo fixed.

## Programme mapping

Finite étale rows attach to SGA1 V§7 and the inherited cote1 trace programme; class-number rows attach to Pic(Spec O_K), SA06 B.4a–e, REVLOC I.5/I.8b, IA02/IA09. Kummer-density rows extend the finite-field/Kummer mechanisms in CX-N02/CX-N05/CX-N11. Chebotarev rows reach SA07 D.3.2 and E.2/E.3. These are run-level links, not independently verified original archive scans. Root/geometry owns exact archive indexing.

## Expansion at 01:34 UTC

NT-L09/10 prove fixed Dirichlet and Hecke Möbius cancellation by a full truncated-Perron argument. NT-Z10 proves the unconditional fixed-character local zero count, including infinite-order Hecke characters, by Jensen with an explicit Euler-product lower bound. NT-P11/12 give uniform cyclotomic progression bounds and include the q≡2 mod4 prime2 correction. Geometry peer reviewed NT-F01–04; its finite-base interpretation correction has been incorporated.

At 2026-11-21 01:35:27 UTC, complete post-draft self-checks passed for NT-L09/L10, NT-Z10 and NT-P11/P12. The Perron proof specifies every contour and error term; the Jensen proof treats the pure norm pole and bounded-height range; the progression proof retains the modulus-two ramification exception. RV1999 original PDF download is now complete and its theorem statements have been read locally.

At 2026-11-21 01:40:12 UTC, the entire NT-Z12 proof was reread after drafting. Checked quadratic root-number parity, Schwartz Fourier support strictly inside (−2,2), L2-to-L1 approximation, order of the two limits, the 1/8 mean-multiplicity calculation, the even-order factor 1/2, and the positive/negative squarefree counting constants. Weighted and ordinary ≥15/16 assertions pass for the χ_{8d} family exactly. NT-Z11 is a cited theorem statement/locator check, not an independent reproof of FPS2017.

Catalogue hygiene: removed an overbroad generic M-prefix sentence saying only Dedekind RH was required in every row. Each row now states its own narrower input; the infinite-order Hecke growth/cancellation rows retain the actual Hecke-GRH hypothesis.

At 2026-11-21 02:03:43 UTC, full independent peer readings of root MT-H01/H02/H03 passed. This was a reading/check of the complete written proofs, not a second independent construction. HK2020 AppendixA.1 was opened independently (turn572782147view0, turn251532508view0, turn900625156view0); the local p=5 inertia calculation and even-symmetric ζ factor were checked explicitly.

At 2026-11-21 02:07:38 UTC, NT-H05/H06 added growing-field Brauer–Siegel and the exact TV basic inequality. NT-H07/H08 complete derived tower proofs passed whole self-check and geometry peer reading; the explicit strictly-increasing-degree subsequence was added as a precision improvement. NT-R01–04 separate the prime-race results under A from the exact additional GSH gate, based on actual pp174–178 images of the corrupt-text original PDF.

At 2026-11-21 02:15:24 UTC, NT-Z13–Z16 added exact argument, multiplicity, gap and first-zero consequences. Source gamma-pairing restriction is retained, finite-order Hecke axioms checked, and the entire NT-Z14 deduction reread after drafting. Degree remains inside the double logarithm in conductor aspect. Root peer review of H07/H08 passed; typography repaired.

At 2026-11-21 02:16:52 UTC, full root MT-M05/M06 peer review passed: actual ideal counterexample and polynomial-Gaussian closed-ideal repair, with all Frechet-density/ODE/Hermite steps checked. Two harmless cdot typography issues reported.

At 2026-11-21 02:21:13 UTC, NT-P13–P16 and NT-L11/12 added after original theorem-page image checks and exact quantifier review. Entire short new proofs read: prime-minimality, interval endpoint limit and Markov optimization. Root full-peer NT-Z14 passed. Full peer readings MT-M07/M08 passed; explicit nuclear Fourier normalization was requested and incorporated by root.

At 2026-11-21 02:25:49 UTC, NT-H09/H10 added the arbitrary closed-point and bounded-Frobenius-order extension of the tower argument. Complete post-draft self-reading passed; root/geometry peer review requested. MT-M09 complete peer reading passed and is logged. Geometry independently passed NT-Z13 specialization and the entire NT-Z14 proof.

At 2026-11-21 02:28:19 UTC, geometry independently passed entire NT-H09/H10 proofs. Full peer review of AG-FG-EXP/DER/PPOWER/PRODUCT also passed and is recorded with exact IDs; only exponent-comma typography fixes requested. Next route: ray-class Chebotarev errors whose class-group-order factors cancel via conductor–discriminant.

At 2026-11-21 02:39:04 UTC, NT-Z17 and NT-Z18 are synchronized. Whole post-draft readings passed: the conjugate shifted product has degree2n, paired gamma parameters, theta0, squared conductor and doubled central order; the degree-normalized double logarithm is unchanged and Theorem7 zeros return to the original character. Pure norm shifts are handled only by fixed-function translation. Root independently passed NT-Z17 against the source axioms. NT-Z18 uses the admissible closed-support sinc-squared test, real-ordinate positivity and indicator≤multiplicity, without a parity assumption.

At 2026-11-21 02:39:46 UTC, full independent peer reviews of root MT-M10/M11 passed. Checked the entire Baire/divided-difference cluster bound and all Blaschke/Harnack steps for arithmetic leading coefficients, including the full NT-Z10 analytic-growth interface. The jet basis is retained as an additional hypothesis. Fresh Neukirch page images locate conductor–discriminant VII(11.9) on printed534/PDF542, with its complete supplied proof across printed533–534, and the degree-one conductor identification VII(11.10) on printed535/PDF543.

At 2026-11-21 02:43:14 UTC, NT-C06/C07 full proofs passed post-draft self-reading. The ray-class error uses the exact average conductor and the sharper (1−1/h) modulus bound; primes in a degenerate modulus which remain unramified are removed explicitly. Ordinary and narrow class fields give degree-one prime representatives with the separate ζ_Q hypothesis stated. Neukirch primary proof pages are registered. Geometry peer passed NT-Z17/Z18; full independent readings of AG-ARTHUR-PARAM/MIN and AG-LEFSCH-LATTICE/SPLIT passed.

At 2026-11-21 02:49:14 UTC, full CX-GEO-012/013 and root MT-M12/M13 peer readings passed; exact checks are logged. Complexity independently passed NT-C06/C07 against primary GM and Neukirch images. NT-Z14 long inline covering-radius bound moved to a display as requested by root compilation review. Next arithmetic route: explicit ray-class Mertens constants and Euler products by fully quantified partial summation.

At 2026-11-21 02:51:09 UTC, NT-C08 full post-draft reading passed. It gives certified ray-class Mertens constants and Euler-product limits with fully computed tail errors, retaining norm2 endpoint, n/[2 floorx] higher-power tail and degenerate-modulus corrections. Catalogue now75 rows.

At 2026-11-21 02:57:01 UTC, NT-L13 full proof reading passed after original Chandee axioms/Cor1.1 page-image checks and the complete p7 corollary proof. This supplies genuine field/character/height uniformity and an explicit degree-sensitive threshold. The larger conductor is substituted while x remains free; no asymptotic conductor replacement is used. Source numerical prime-power certification is cited, not independently rerun. Whole MT-M14/M15 peer readings passed and are logged.

At 2026-11-21 03:03:02 UTC, NT-L14/H11 synchronized after complete post-draft readings. Original Lumley p3–4 images fix all one-line constants and conductor threshold; RH ζ_Q in its p10 lemmas is retained. Relative class-number–regulator proof includes every ramified Euler factor, exact finite-order infinity conductor, residue/signature/root-of-unity factors and unbounded small-conductor exceptions. Geometry independently passed NT-L13. Root M16 approach was checked but final draft awaits full review.

At 2026-11-21 03:08:34 UTC, complete independent peer readings of root MT-M16/M17 passed and were registered under those exact IDs. The argument handles unbounded multiplicities through local weighted products, factorial-normalized uniform jet estimates, a mass-one remainder, and O(log² T) trace-block counts. This supersedes the earlier approach-only check.

At 2026-11-21 03:12:07 UTC, NT-L15 and NT-Z19 synchronized with full post-draft readings. Weak mean square of inverse Hecke coefficients yields GRH, simplicity, Σ|ρL′|^−2≤B, and o(T²) reciprocal second moments by a complete Laplace/Abel-Bessel proof. This additional arithmetic hypothesis then supplies the canonical absolute basis and positive trace via MT-M16/M17. Original Titchmarsh pp376–377 image checked; full old contour proof not claimed recertified. Catalogue now80 rows and31 sources.
