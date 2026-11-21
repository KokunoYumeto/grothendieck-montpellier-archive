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

At 2026-11-21 03:18:09 UTC, NT-H12/H13 synchronized after entire post-draft proof readings. The EV exponent is explicitly classical; the complete new input reduction needs only RH ζ_K. Exact finite removal inequality, cyclic-cover counts and Kummer H¹/unit/localized-Pic factors are proved. Catalogue now82 rows/34 sources. Added 34 exact S-NT bibliography-ID events as retrospective transcriptions of this run’s documented source checks, preserving statement-versus-whole-proof limits and unresolved original-page gates.

At 2026-11-21 03:21:13 UTC, complete independent peer reading of root MT-M18 passed. This covers the whole block synthesis/interpolation/topology proof, including the unconditional fixed infinite-order Hecke analytic interface. Exact-ID event registered. Point-jet coordinates and adapted block coordinates remain explicitly distinguished.

At 2026-11-21 03:24:36 UTC, full independent MT-M19/M20 readings passed and exact-ID events were registered. Nuclear/trace-class distinctions, zero-side Weil positivity, weaker simple-zero Hilbert completion and faithful nilpotent obstruction all checked. Root and geometry full-peer reports on NT-H12/H13 were transcribed with their source-inspection scopes kept distinct.

At 2026-11-21 03:29:14 UTC, NT-L16/L17 synchronized after full post-draft readings. Exact multiplicity-sensitive mean-square limsup bound proved. Prime-r Kummer fields give actual infinitely repeated Hecke zeros, so universal Dedekind weak Mertens and faithful full-jet positive Hilbert completion are impossible without affecting conditional GRH or trace positivity. Source GM AppendixA p26 image and the CX-ALG-024 arithmetic dependency checked to recorded scope. Catalogue now84 rows/34 sources.

At 2026-11-21 03:45:12 UTC, NT-E01–05 synchronized after entire post-draft proof reading. Cyclic-density input is exactly squarefree division-field Dedekind RH; Lang–Trotter upper bounds use known abelian holomorphy. The new E05 counting formulation improves logarithmic factors via the checked LLS class-number lower bound, with both remainder branches solved explicitly. Catalogue now89 rows/38 sources. Four exact bibliography-ID events added. L17 entireness locator corrected to RV7-19p279; geometry and complexity peer reports transcribed honestly.

At 2026-11-21 03:47:12 UTC, strengthened NT-L16/17 synchronized after entire revised proof reading. The exact denominator improves from (2m−1)! to (2m−1)((m−1)!)², and a finite Gram–Bessel argument yields the sum over all critical zeros of each exact multiplicity. Complexity suggested the polynomial-wave improvement; the complete normalized proof is now written and self-checked. Revised peer requested.

## 2026-11-21 03:56:58 UTC — joint Frobenius law route

NT-R05–07 now synchronized in focused frobenius_laws.tex, section.tex and rows.json. Fiorilli–Jouve primary Proposition3.18 already supplies the B² analytic theorem without Artin holomorphy via cyclic induction. The new complete deductions retain the |C|/|G| coefficient normalization, produce the joint covariance through the compact rotation group (no independence claim), and prove a finite étale negative-mean/positive lower-log-density result. Only RH for the fixed splitting-field Dedekind zeta is required. No claim of literature novelty. Original external PDF and rendered page remain evidence-only. Source Murty title spacing was corrected as requested for assembly.

Root MT-M23 and MT-ART09 entire new proofs passed independent review at03:54:33; fresh source statement checks were scoped separately from root’s full-paper reading. Root’s own03:50:00 E01–05 and L16/L17 peer events remain in the root peer ledger, without duplicate transcription.

## 2026-11-21 04:04:48 UTC — NT-R08 registered after CP4

The discriminant-uniform finite-étale lower-density proof was held in its new focused file during the CP4 freeze, whole-read by the author and independently by geometry, then synchronized after release. The source variance scaling was checked on the original FJ p11 image: its author Theorem2.1(17) lacks a square, while Prop4.6(87) and the p41 proof correctly have the squared L1 norm. Our proof bypasses that statement via GM A.1. No registered file was edited during the freeze.

## 2026-11-21 04:16:14 UTC — CM moving endpoints

Registered NT-E06–08 (96 total rows) after entire author and root proof readings. Classical uniform CM power-sum premise is BFK Prop2.5(2.3), original Erdős–Turán TheoremIII provides interval-independent discrepancy. The strict floor endpoint works even for square norms. Geometric mesh h=x^(-1/8) yields an integral main term and x^(5/8) log² error. Quadratic descent is proved by CM eigenspace swapping and norm-square counting. James–Pollack theorem plus erratum is comparison only; its revised sector estimate is not claimed independently certified. Next route: shrinking deficit windows approaching the natural square-root boundary, and Rajan1998 general Hecke discrepancy.

At 2026-11-21 04:18:16 UTC, NT-E09 whole author proof reading passed and was synchronized (97 rows). The exact arcsine integral and explicit logarithmic derivative retain the whole fixed-parameter range −1/2<λ<1/2. Root suggested the useful λ>3/10 Taylor-remainder scope warning, now proved and included.

At 2026-11-21 04:21:56 UTC, NT-A04/05 and S-NT-RAJAN registered after whole author proof reading (99rows/43sources). Rajan supplies a primary general-Hecke version of the CM discrepancy premise. The finite-order-times-norm exception is essential and is checked by a complete nonzero Fourier-moment proof. The normalized shrinking arc formula retains exactly0<alpha<1/2. Local source downloads failed; the primary indexed full text and entire supplied short Prop4 proof were read, with no invented image check.

At 2026-11-21 04:29:22 UTC, NT-E10 synchronized as row100 after whole author and root proof readings. Root suggested the endpoint norm-form route; the full algebraic centralizer and exact strict-threshold proof are now written. In the same interval, independent full reading of all752lines of MT-M28 passed and was registered under that exact ID. Uniform completed gamma ratios and the actual Hilbert operator identity, not just eigenvalues, were checked.

## 04:37 UTC: almost-sure Gaussian angles
NT-A06/A07 specialize the checked Rudnick–Waxman variance premise and give a complete Borel–Cantelli all-real-scales deduction for degree-one primes. The fixed-center quantifier, center-dependent threshold and explicit dyadic factor are separated from the unknown numerical variance constant. Full author proof read; root peer requested. Moving next to simultaneous finite ray-class and infinite Hecke-angle constraints.

## 2026-11-21 04:51:08 UTC — joint ray class and Hecke angle

NT-A08–A11 synchronized after the CP5 freeze and complete author/root proof readings. The primary IK definition has a conjugate-pair gamma restriction, so the complete reduction uses shifted conjugate products only for entire non-pure-norm characters and recovers imaginary coefficients through two bounded-variation Abel steps. This yields an absolute degree/conductor bound, no factor h in joint discrepancy, an optimized h-sensitive shrinking-arc error, and a uniform least-prime norm. All finite, archimedean and discriminant parameters remain explicit. Source scope is public primary indexed text, not a claimed page-image or whole-book audit. Catalogue now106rows/45sources/41questions.

Independent whole reading of MT-M30 passed and was registered under its exact ID. The unconditional ideal-valued splitting genuinely transfers the compact norm-one-vanishing test condition to the full closed quotient; no zero-location conclusion is inferred without the remaining geometric trace identity.

At04:54:06 UTC, full independent MT-S504 reading passed. Fresh primary source reading covered the exact final comparison lemmas in both arXiv and publisher numbering; upstream automorphic construction remains classical input. The proposed M-only central no-pole consequence is logically valid, and ζ_F/ζ_Q handles the quadratic twist on the whole real critical interval. Parent owns S505. A06.3 and the RW bibliography title received the requested purely typographical layout changes.

## 2026-11-21 05:01:58 UTC — improved generators and finite certificates

NT-C09–C13 synchronized (111rows/48sources/43questions). The 2025 primary source supplies all correction terms and exact low-degree threshold ranges; its proof identifies containment of Cl². The certificate has a strictly smaller RH family than the uniform bound. Complete new quotient/exclusion and finite-algebra enumeration proofs are written; the latter has an independent whole-proof pass from complexity. The source’s numerical constants are credited and were not rerun. Parent suggested this breadth route; original Bach access remains honestly unresolved. The enumeration adds two to the sharp real-valued norm bound only for certified rounding, avoiding an unproved logarithm/integer separation claim.

## 2026-11-21 05:14 UTC — nonabelian Frobenius and Hecke torus

NT-A12–A14 and NT-E11 synchronized after entire author and independent complexity proof readings. The explicit cyclic induction avoids any general Artin-holomorphy assumption. Exact conductor–discriminant averaging retains the finite density in both error terms, while norm pullback preserves the required nondegeneracy. The optimized CM application retains the arcsine integral and yields the fixed-data extremal-trace error x^(5/8)sqrt(log x). All source premises were already registered; this is a new full deduction, not a literature-priority claim.

Full independent M33/M34 peer readings passed and events are saved, with the M33 compact-invariance clarification checked. The M34 theta-density antecedent was checked against M24.9 and the complete M25 proof; original source image inspection remains credited to root/complexity.

## 2026-11-21 05:23:48 UTC — mixed Hecke tensors and an actual endpoint obstruction

NT-A15–A17/E12 synchronized after complete author/root proof readings. Source S-NT-DP adds an exact original-page-checked multidimensional discrepancy statement, with its upstream proof scope explicitly limited. The positive results need all mixed Hecke products and no monomial finite-order/norm relation. The unconditional CM centralizer result proves a real obstruction at the two-extremal-coordinate total exponent1/2, rather than only a failure of this estimate. Q37 now distinguishes E09’s valid older potential-CM bound from E11’s optimized all-CM-defined-over-base result. A09 alignment and A10/E11 internal tags were corrected in focused and synchronized sources; all owned split/aligned/gathered blocks were scanned.

At05:27UTC, cross-checked every registered NT and S-NT ID against the event ledger: all119 consequence IDs and all49 bibliography IDs have exact-ID events, without duplicate row/source IDs. Reconciled stale peer-request wording in Q23/25/26/29/32/34/35 against actual existing root/geometry/complexity review events; C12 placement now states its completed peer review. No new proof verification was invented by this metadata cleanup.

At05:28UTC, NT-E13 synchronized after whole author and root proof readings, removing the all-endomorphisms-defined premise from the nonzero common-endpoint obstruction. Its concrete Q-pair excludes every rational primep>3, with exact common trace-zero exception retained. Catalogue now120rows/49sources/47questions. Registered files are ready for the05:31–05:33 checkpoint freeze; subsequent work will use reads or new unregistered focused files.

## 2026-11-21 05:46:17 UTC — harmonic closed-point measures

NT-A18/A19 synchronized after whole author/root readings. Reciprocal-prime weights allow nontrivial norm drift: every mixed Fourier harmonic series has an actual finite constant, with the exact pure-norm tail and the induced Hecke family retained. A finite A_D family already gives explicit progression examples with weighted Haar and ordinary-weight failure. No frequency-uniform shrinking claim is added. Catalogue now122 rows/50 sources/49 questions. NT-A20/A21 Euclidean-ideal/localization draft is author-read and reserved for geometry peer review; its classical analytic sufficiency remains cited.

At 2026-11-21 05:47:50 UTC, source cross-check located BFK Remark4.11p1743/author22: the rational two-CM positive-extreme obstruction is already there and credited to Sutherland. E12/E13 focused/assembled text and rows now state this explicitly, while retaining the proved broader arbitrary-base, absolute-trace, square-norm and potential-CM formulations. No mathematical assertion changed.

## 2026-11-21 05:49:31 UTC — Euclidean ideal classes and bounded localization

NT-A20/A21 synchronized after complete author/geometry proof readings. Lenstra1979 supplies precisely the |S|>=2 squarefree unit-Kummer analytic sufficiency; its primary p127 image and complete elementary pp124–125 arguments were checked. The source does not print the analytic proof, and the text preserves that boundary. The full new one-prime localization formulation retains cyclicity, the C07 prime norm bound, selected-ring Kummer family and existence-versus-runtime distinction. Catalogue now124 rows/50 sources/51 questions.

## 2026-11-21 06:03:24 UTC — finite elliptic detection

Registered NT-E14–E16 after whole author/root/geometry proof checks. Exact Mayle–Wang published constants and actual bounded-degree Dedekind RH family are retained. The new all-CM input-bit formulation uses the genuine A/2A lattice quotient, a quadratic avoidance extension, and direct finite-field point enumeration; it requires neither factorization nor conductor computation. Source gates closed by Milne ANT8.42–8.43, MW NOS8/9, and original Faltings Cor2 cofinite-local-factor equivalence. New source Faltings registered; Milne existing source augmented. No claim of a new published priority or proof of non-CM GL2 GRH.

## 2026-11-21 06:15:50 UTC — quadratic-only CM recognition

Registered NT-E17/E18 after complete author/root readings. Full explicit biquadratic avoidance and resultant certificate proof gives deterministic polynomial CM recognition from A_quad alone, including varying number fields with dense input. Kept faster published CS bounds separate; exact CM order discriminant/explicit endomorphisms are not outputs. Direct BCRS Phi construction source read and registered. No new empirical or numerical verification claimed.
