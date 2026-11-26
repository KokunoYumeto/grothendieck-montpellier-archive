# Intake of NEG_NIGHT (prompt 54), checkpoint 15, by diff; GCT first, for the follow-up to prompt 56

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 22 Nov 2026, for the main session (Claude Opus 5.5
at effort max). The run is GPT-6 Astra (ChatGPT Pro mode); its files give the effort as "not exposed". The earlier
intakes read checkpoint 04: `INTAKE_NEG_NIGHT_20261121.md` (agent a17221e5) and `INTAKE_NEG_NIGHT_20261121_G.md`
(agent a8d75352), both Claude Opus 5.5 at effort high.

## The answer for prompt 56

- **Nothing in this checkpoint supersedes or contradicts an item of prompt 56** (A1-A7, B1-B3, N1), in what I read.
- **One addition strengthens A1:** a corollary on periods and recurrences. For plethysm the method is NN-G002 and
  NN-G018. The Kronecker form is derived here from PNEW-013.
- **One small addition to A3:** the recurrence bound of NN-G018. Its period bound is already in P-F31.
- **One addition sharpens A7:** NN-G003. Large strict indices do not give a vanishing coefficient, so a refutation of
  PH2 or SH(a) must not be worded as one.
- **N1 does not change.** The new GCT VIII findings (G032-G038) concern noncanonical lifts of the rank-three table.
- The three additions are stable: their NEG_NIGHT inputs are unchanged since checkpoint 04. §3 has the exact text.

## 0. Return, method and scope

- **Return:** `research_returns\NEG_NIGHT_checkpoint_15_20261122T0719Z_unzipped`: 164 findings, assembled 07:14 UTC on
  22 Nov. The run says it is continuing. At 13:48 UTC it was the newest on disk, and I saw no newer one in the two
  download folders. By the three-hour rule of 20 Nov the run counts as ended here unless a later checkpoint turns up.
- **Read in full, with proofs:**
  - new: G032, G033, G034, G035, G036, G037, G038;
  - old, because prompt 56 may need them: G001, G002, G003, G004, G013, G014, G015, G017, G018, G020, and G011 as the
    base of G033.
- **Read in full as statements:** the other 50 new findings (§2b). Their proofs were not read.
- **Also read:** prompt 56 as sent, in full; both earlier intakes, in full; README lines 1-45; the last 40 lines of the
  ledger (lines cut at 520 bytes); GCT VI Definitions 1.2.2 and 1.2.4; the head of GCT_POS N-012.
- **No code of the return was run.** My programs are written from the statements and read JSON data only. They and
  their outputs are in a temporary folder, which a reboot or cleanup can clear:
  `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\chk\negnight15`
  (`check_gct15.py`, `diff_nn.py`, `diff_cp04.py`, `diff_last.py`, `diff_c.py`, `inventory.py`, `drop_patterns.py`).
- **No literature search. No cote or scan read:** the run's locators (cote 2 scan 17; cote 133 scans 19, 28) are not
  repeated as mine. The trace table it uses is byte for byte our `E4_scripts\e3_constants.json` (SHA-256).

## 1. What changed, by content

The return still holds the manifests of checkpoints 04 to 09. The pushed copies of 06 and 09 on disk give the texts;
their findings files match those manifests by SHA-256 (line endings normalized).

| Against | New | Changed (statement, proof or inputs) | Same in those three fields |
|---|---|---|---|
| checkpoint 09 | 17 | 5: A042, C043, C044, G037, G038 | 142 |
| checkpoint 06 | 36 | 2: A037, S019 | 126 |
| checkpoint 04 (what our intakes read) | **57**: A031-A051, C031-C055, S017-S019, G032-G039 | none found, at the strength below | see below |

How far "none found" reaches for the 107 findings of checkpoint 04:

| Findings | Evidence | Result |
|---|---|---|
| G001-G031 | verified copy of checkpoint 04's GCT chapter and findings file | statement, proof and inputs the same; each chapter section the same up to white space |
| S001-S016 | the eight proof files, SHA-256 | whole files the same |
| A001-A030 | SHA-256 of the analytic TeX files of checkpoint 04; stored statements | the 24 proof files are the same (only the list of inputs, `chapter.tex`, grew); every stored statement the same as far as stored |
| C001-C004 | the lines stored by the earlier intake's reads | the same, except four sentences of review status |
| C005-C030 | stored statements; checkpoint 06's findings file | statements the same as far as stored; proofs the same since checkpoint 06. Their proofs at 04 could not be compared (the complexity chapter grew) |

## 2. Verdicts on the 57 new findings

### 2a. GCT VIII's rank-three table (read in full, with proofs)

The objects are dimension rings: effective C₂-lifts of the trace table of P-F-E3-01, scored by cancelling pairs. They
are noncanonical. None decides a hypothesis of GCT VI or a conjecture of GCT VIII.

| Id | Statement | Check | Verdict | In the project's terms |
|---|---|---|---|---|
| G032 | Existence of a symmetric lift of total mass ≤ N is decidable in time F(N)(L+1)^c | targeted proof check | **confirmed** | projection of lattice chambers of grading cocharacters (diagonalizable groups, SGA 3 I 4.7); NN-G010's kernel category |
| G033 | An explicit lift with 2744 cancelling pairs, 1296 of them in the bottom cell | targeted proof check; own computation of all 132 positions, all 1000 triples, domination, parity and score | **confirmed** | Artin-Tate structure objects whose sign trace is the E₃ table (E4 §7) |
| G034 | With δ₁, G₁, U₁ fixed, 2744 is the minimum, uniquely attained | targeted proof check | **confirmed**, given G031 | integral character divisibility, restriction to μ₂ and μ₄ |
| G035 | Every competitive closed table lies in 43 mass rows with 467 increments | targeted proof check; own enumeration gives 55, 12, 43, 467, 21 and relaxed bound 1700 | **confirmed**, given G030 and G031 | ordinary ranks of the graded structure objects |
| G036 | 2744 is the exact, uniquely attained minimum of the symmetric closed-table class | targeted proof check; own program finds each of the 43 rows covered by a printed exclusion, and the mass preconditions I tested hold | **confirmed**, given G030, G031, G034, G035 | Gauss's lemma in the character ring of the torus, reduction at 2 |
| G037 | Every lift, on all 810 positions, has ≥ 112 pairs; the pair parities lie in a 92-dimensional space | targeted proof check; own replay of the 61 and 112 certificates (gaps 72,768 and 2,028,372) and of rank 718, 421 singletons | **confirmed**. The intermediate certificates 104-110 were not replayed and are not needed | associativity scheme on ordinary ranks; second Hasse coefficient on the grading torus |
| G038 | Tables on the original 132 positions form a 19-parameter open torus; there at least 932 pairs | targeted proof check of classification and lemmas; own computation of 20 random tuples and of the 932 scalar table | **classification and lemmas confirmed; the bound 932 carried** on the run's enumeration (181,032,863 divisor choices), which I did not rerun | open subscheme of the associativity scheme; first-jet obstruction at μ₄ |

Current intervals: [112, 2744] on all positions, [932, 2744] on the original support, exactly 2744 in the symmetric
closed-table class. Our record "minimum 7,952" (SPLIT_ZERO_IN_CONNES_CONSANI_TERMS, lines 157-158, flagged in the G
intake) holds only in its search window.

### 2b. The other 50: statements read in full, proofs not read

Verdict for each: **carried as background; no fault seen in the statement**. E is the designated counting theorem,
A Alpöge's theorem, M Masullo's draft. The input column is what the run's statement and inputs say.

| Id | Statement | Input | In the project's terms |
|---|---|---|---|
| G039 | lim a·j*(−a) = x*²/8 for Jensen degrees, so simplicity of zeros ⇔ a·j* → ∞ | A for the limit | hyperbolicity of finite Jensen algebras (trace form) |
| S017 | The counting cubic is a wedge of N motivic spheres (P¹)^∧v | E only to evaluate | Tate motive, SGA 6 |
| S018 | Its K₀ and γ-filtration; the F₂-rank of a graded piece is #P-complete | E only to evaluate | λ-ring, γ-filtration |
| S019 | Exponential monotone circuits against 2^o(n) integral circuits for partition polynomials on expanders | E | positive against virtual classes in a torus representation ring |
| A031 | CUE labels are positive in proportion → 1/2, with rate 1/log N | none | determinantal point process |
| A032 | Sign of the central second jet of real Dirichlet L-functions; exact branch counts | A in part | completion, root number |
| A033 | Martinet's Q₈ field: central order 2, exactly two branches, both right | none | Artin factor |
| A034 | Q₈×C₃ compositum: exactly two excess left branches | none | Artin factorization |
| A035 | Multiple zeros are transverse by the second Puiseux order | none locally; A globally | jets of the shifted family |
| A036 | A positive proportion of zeta zeros has definite normal velocity | A | purity as zero location |
| A037 | Mixed phase mean 0; at least 1/6 of zeros transverse | A | Hardy phase |
| A038 | Hermite orbital radius is Θ(√m) | none; A in the application | unitary orbits |
| A039 | Both branch signs occur in every window (T, BT) | A | Puiseux branches |
| A040 | Exact phase mean; both signs in windows of length √T·log²T | A | twisted explicit formula |
| A041 | Each branch sign has T^(1−ε) log T centers | A | the same |
| A042 | Each branch class has positive lower proportion | A | the same |
| A043 | The same for Dedekind zeta functions | RH for ζ_K; through M conditional | zeta function of Spec O_K |
| A044 | Downward simple tangencies bend strictly left | none locally | jets |
| A045 | Each strict sign at T^(1−ε) log T simple zeta zeros | A | jets and explicit formula |
| A046 | Square-root signed cancellation for fixed primitive characters | A | the same |
| A047 | Each strict velocity sign has lower proportion ≥ 10^(−14) for zeta | RH | mollified moments |
| A048 | The same for each fixed primitive character | A | the same |
| A049 | Branches of both signs survive in disks c/T, uniformly for q ≤ T^κ | A | deformation of the divisor of zeros |
| A050 | Almost 2/3 of zeros stay real and simple for −c/log²T ≤ t ≤ 0 | RH | heat deformation |
| A051 | Nonreal zeros of H₋ₐ occur below height exp(exp(C/√a)) | none; RH for the limit | heat deformation |
| C031 | Smooth hypersurfaces over F₄ with ⊕P-complete Frobenius scalar | none | coherent Frobenius |
| C032 | A smooth projective model over F₂ with four-dimensional coherent cohomology | none | Weil restriction |
| C033 | Symbolic counting circuits in every characteristic p | E | partition polynomial as a trace |
| C034 | The same over ℤ, constant-free | E | base change from ℤ |
| C035 | Weighted CNF polynomials in characteristic 2, any density | E | zero set over F₂ |
| C036 | Integral weighted CNF polynomials, any density | E | integral Nullstellensatz |
| C037 | Dense factors are outside E's linear layouts | none beyond the interface | rank and divisor bound |
| C038 | Scope n^o(1); permanents with support r^(1+o(1)) | E | integral identity |
| C039 | The same, charged by Boolean degree | E | integral identity |
| C040 | No low-degree deformation with few generic values | none | jets |
| C041 | Permanent of sparse plus supplied rank o(n) | E | integral identity |
| C042 | Counting at growing clause width | E | zero schemes |
| C043 | Bounded-output evaluation with flat radicals of polynomial lcm | none | residue fields |
| C044 | Advice simulation for algebraic constants of logarithmic degree | none | residue fields |
| C045 | The same for nested constants of bounded depth rank | none | towers |
| C046 | Uniform evaluation for faithful towers | none | towers |
| C047 | One principal root gives PosSLP-hardness | none | choice of embedding |
| C048 | Binary cyclotomic conductors | A | splitting of primes, abelian |
| C049 | Prime square roots: identity testing in coRP | none | quadratic characters |
| C050 | Faithful odd towers at binary degree | A | degree-one residue fields |
| C051 | Flat binary-degree radicals | A | residue fields of degree ≤ 2 |
| C052 | All real odd-root circuits | A | residue fields |
| C053 | Removes A from C050-C052 in the stated scopes | none | unconditional prime sampler |
| C054 | Principal complex roots have exactly PosSLP oracle complexity | none | embedding |
| C055 | Permanents of nested cut-coordinate trees with sparse leaves | E | boundary algebra of matchings |

**Counts for the 57:** 6 confirmed (G032-G037), 1 confirmed in part (G038), 50 carried at statement level, 0 refuted.

### 2c. Old GCT findings read again for prompt 56 (unchanged; no verdict changes)

| Id | Check here | Verdict | Against prompt 56 |
|---|---|---|---|
| G001 | targeted proof check; point counts for seven primes ≤ 17 | confirmed, given PLE-F5/F8 and Kahle-Michałek Theorem 5 | **duplicates** the example under A6; adds the zeta remark, not needed there |
| G002 | targeted proof check | confirmed, given P-F31 | **duplicates** P-F31 (the period clause, lines 190-196 of its file); **strengthens A1** when applied to PNEW-013 |
| G003 | targeted proof check against Definitions 1.2.2 and 1.2.4; computed for L ≤ 80 | confirmed | **sharpens A7**. It contradicts nothing: it is no plethysm or Kronecker family |
| G004 | targeted proof check | confirmed, given P-F56 and P-F57 | follows from A3; concerns one formula's conditioning; not needed |
| G013, G014 | targeted proof check | confirmed | isolation; outside A and B |
| G015 | targeted proof check | confirmed | countermodel on information; claims nothing about the orbit closures of B; not needed |
| G017 | targeted proof check; computed for L ≤ 40 | confirmed | large conductors for torus gradings; no plethysm family; not needed |
| G018 | targeted proof check | confirmed, given P-F31 | **strengthens A3** (recurrence order, trace rank) and, with PNEW-013, **A1** |
| G020 | targeted proof check; 400 random formulas | confirmed | torus rays with NP-complete first coefficient; refutes no hypothesis as stated; not added |

## 3. For the follow-up to prompt 56

### 3a. Stable: to add or change

**A1, add Corollary A1-C.** Inputs: GCT_POS PNEW-013, with the method of NEG_NIGHT NN-G002 and NN-G018.

> Let n ≥ 2, let k_n and r be as in A1, and put N = 2^(n-1)·3^r.
> (a) Every quasi-period of the quasi-polynomial k_n is divisible by N, hence is ≥ 2^(n-1).
> (b) Every linear recurrence with constant coefficients that k_n(s) satisfies for all large s has order
> ≥ φ(N) ≥ 2^(n-2). In particular, if k_n(s) = tr(A F^s) for all large s, with A and F endomorphisms of a
> finite-dimensional space V in characteristic zero, then dim V ≥ 2^(n-2).
>
> Proof. Cite the quasi-polynomiality of stretched Kronecker coefficients. (a) A quasi-polynomial of period L has a
> generating series with poles only at L-th roots of unity, and A1 gives a pole at a primitive N-th root. (b) A
> recurrence of order d gives a rational series whose denominator has degree ≤ d. By A1 it has poles at all φ(N)
> primitive N-th roots, and φ(N) ≥ φ(2^(n-1)) = 2^(n-2). By Cayley-Hamilton, s ↦ tr(A F^s) satisfies a recurrence of
> order dim V.

Check level: derived and proved here, checked only by its author (a targeted check); A1 carries the main session's
check. GCT_POS's corollary states only the bound on max a_i. Novelty not searched. The corollary gives no r = 0, no
bound on p or s, and no circuit lower bound.

**A3, add one sentence.** Inputs: P-F31, NN-G018.

> For n ≥ 4, every linear recurrence satisfied eventually by the plethysm sequence f_n of P-F31 has order
> ≥ φ(2^(n-1)) = 2^(n-2), by the proof of Corollary A1-C(b). Its period bound is the one P-F31 already states.

**A7, add a proposition and fix the wording.** Input: NN-G003.

> For L ≥ 2 let f_L(n) = L⌊n/L⌋ + 1. It is positive at every n ≥ 0, its generating series
> (1+(L-1)t^L)/((1-t)(1-t^L)) is a positive form, and p(f_L) = s(f_L) = L-2 (GCT VI Definitions 1.2.2 and 1.2.4).
>
> Proof. On n ≡ i mod L the constituent of f_L(n+p) is X+p+1-((i+p) mod L). All constant terms are nonnegative exactly
> when p ≥ L-2, and all values at X = 1, hence at all X ≥ 1, are positive exactly when p ≥ L-2.
>
> In every cell of A7, a refutation of PH2 or SH(a) is worded as a bound on the strict indices of the constituents. It
> is not worded as the vanishing of a coefficient, and it is not used against SH(b) or a relaxed decision statement.

Check level: targeted proof check, twice (a8d75352; this intake), and a computation for L ≤ 80.

**N1: no change.** N-012 concerns the minimum over the scaling exponent in Conjecture 3.2; G036 is a minimum over
noncanonical lifts of a fixed table, so they do not meet. The run takes the corrected sign of b₂ as an input (chapter
preamble), so it is no further check of N1's third point. G011 says that it makes no unimodality claim.

**A2, A4, A5, A6, B1, B2, B3: no change.** The new permanent circuits (C034, C038, C041, C055) concern supplied sparse
or structured matrices and say nothing about per_n in the orbit closure of det_n.

### 3b. Files to attach

Prompt 56's ZIP holds no NEG_NIGHT file. Attach:
- this intake and `INTAKE_NEG_NIGHT_20261122_cp15_CHECK_EVENTS.tsv`;
- `INTAKE_NEG_NIGHT_20261121_G.md` and its check events, for the earlier checks of G002, G003 and G018;
- `work/gct/chapter.tex` of checkpoint 15, pointing to NN-G002 (lines 103-134), NN-G003 (135-186) and NN-G018
  (1210-1314) only.

### 3c. Moving: do not put into prompt 56

- **G037:** a search at added mass 224 was under way (solver state and exploration files); the last section states that
  a new numerical bound needs its own certificate.
- **G038:** the 932 scalar table has no graded lift yet, and the bound rests on the run's enumeration.
- **G037, G038, A042, C043, C044** changed between checkpoints 09 and 15.
- **Review 09 (07:05 UTC) records movement** on the algorithms, transfers and zero-motion questions (MAIN 01, 04, 09):
  A049, C054, C055. The refinements after that review were not yet assessed by the run.
- **Open GCT gate of the run (MAIN05):** canonical scalings and label order in rank four, integral constants, then an
  effective associative lift.

## 4. What is new

- **Against our results:** the 57 of §2. In GCT the new content is the exact optimum 2744 in the closed-table class,
  the two general lower bounds, and the 19-parameter classification.
- **Against prompt 56's runs:** Corollary A1-C is not in the three GCT_POS files I searched for it
  (`modular_pole_transfer.tex`, IMPLICATIONS, QUESTIONS). G001, G002 and G004 repeat or follow from ALPOGE_GCT.
- **Against the literature: unknown, for every item.** C047 itself credits the real-root bound to Meiburg
  (arXiv:2610.10514v1), which I did not open.

## 5. The scope of the two proofs

- **A:** used as marked in §2b, always for ζ or Dirichlet L-functions, which is what A gives. A047 and A050 need RH only.
- **M:** used only by A043, which the run marks conditional.
- **Beyond both:** no statement read asks for GRH for Artin or automorphic L-functions. A034 works unconditionally with
  an Artin factor and assumes no central nonvanishing.
- **GCT:** G032-G038 and the three additions of §3 use neither A, M nor E. In G001, G017 and G020 A only locates the
  zeros of a shifted zeta function.
- No statement read claims more than its named input gives. The proofs of the 50 were not audited for this.

## 6. Faults

- **Mathematics:** none found in the proofs read.
- **Run's packaging, false as stated:** README and `EXTERNAL_REFERENCE_COPIES.json` say that third-party copies are
  represented by locators and checksums, "full original not redistributed". The checkpoint contains the full EGA IV
  PDF (49.85 MB) and its extracted text under `work/gct/source_inputs/primary_jensen/`, with the recorded SHA-256 and
  a different recorded path, and also the Borcea-Brändén PDF, which has no checksum there. Do not push these.
- **Run's text, stale stages:** G036 still says "an improvement requires dimension at least 72 ... 20 triples", and
  G038 says the bound on all 810 positions is 61. Later paragraphs supersede both, as the README warns.
- **Our earlier intakes, for the main session (not edited):** events typed "independent re-proof" for NN-A001, NN-A017
  and NN-G012 are computations ("independent re-proof by computation", or a check of a table). They should be typed
  computation.

## 7. Integration, prompt updates, Hexagon readiness

**Edits proposed, none made:**
- prompt 56's follow-up: §3;
- `SPLIT_ZERO_IN_CONNES_CONSANI_TERMS`, lines 157-158: "minimum 7,952 within the search window; NN-G036: 2744 is exact
  in the symmetric closed-table class; unrestricted [112, 2744]";
- E4 §7: cite G033 as the smaller composing realization, stated as noncanonical;
- register H02b: add Corollary A1-C.

**A successor of prompt 54 needs:** the 932 enumeration certified by a second program; a graded lift or an exclusion
at 932; the 224-mass certificate finished or dropped; literature searches for A047-A051, G039 and C052-C053; proofs of
those checked whole; no third-party originals in checkpoint ZIPs. The frameworks: the run translates each finding into
algebraic geometry (field `geometry_translation`); the short forms are in the last column of §2.

**Prompts 30-36:** not reread, so no edit is proposed.

**Hexagon, the five tests:**

| Candidate | Complete | Self-contained | Stable | Checked | Interest | Gate left |
|---|---|---|---|---|---|---|
| A1-C, inside H02b | yes, given A1 | no, until A1's write-up | yes | by its author only | high, with A1 | prompt 56's check and search; not a separate post |
| G036, with G033-G035 | yes in its class | needs G010, G029-G031 and the E₃ table | yes for itself | targeted check and computation here | low outside the project | not ready: companion material |
| G037, G038 | no (open intervals) | as above | no | 112 yes; 932 no | low | not ready |
| A047, A048 | claimed | RH or A, and cited moment theorems | unknown until the run is closed | statement only | high | whole-proof check, literature with Hexagon, write-up |
| A050 | claimed | RH and cited pair correlation | the same | statement only | high | the same |
| G039, A051 | claimed | A or RH; Borcea-Brändén, Dobner | the same | statement only | high | the same |
| C052, C053 | claimed | cited prime theorems | the same | statement only | high | the same |
| S017, S018 | claimed | NN-C027 and classical motivic inputs | the same | statement only | moderate | the same |

None passes all five tests now.

**Next attack, where the routes stop:**
- A1-C stops at periods. PH2 and SH(a) still need the coefficient-mass bound of GCT_POS PNEW-016c.
- G036's optimum stops at the fixed presentation. The next step is an extra-position lift below 2744, found inside
  G037's 92-dimensional parity space, or a certificate excluding one.
- G020 stops outside plethysm and Kronecker families. The next step would be a parsimonious map of its torus rays
  into one of those families that keeps the stretching parameter.

## 8. What to keep (nothing deleted)

Sizes are decimal MB; the return is about 257 MB in 2,463 files. "Named" means named by a deliverable, a cited file or
a cited program (manifests excluded).

**Keep:**
- the root deliverables: `NEG_NIGHT.tex`, `.pdf`, the registers (`*.tsv`, `*.md`, `CONSEQUENCES.json`), the manifest,
  BUILD_STATE, TASK_PROMPT;
- `paper_parts/**`;
- `_from_earlier_checkpoints/**` (2.1 MB: the manifests are the only diff evidence for checkpoints 04-09);
- `work/{gct,analytic,complexity,root}/`: chapters and inserted TeX, registers, every `verify_*`, `check_*` and
  `*_certificate.json`, every review and replay record, and every named file;
- `work/reviews/**`, `work/gate_history/**`, `work/receipts/**`, `work/source_manifest.json`,
  `work/pdf_qa/*.json`;
- `sources/OURS_counting_scripts/e3_constants.json`, which the GCT verifiers read;
- `work/complexity/goldreich_izsak12*` (the README records its CC BY licence).

**Can be dropped after intake:**

| Pattern | Files | MB | Condition or exception |
|---|---|---|---|
| `work/pdf_qa/*.png` | 306 | 88.34 | page images |
| `work/gct/source_inputs/primary_jensen/ega_iv4_original.{pdf,txt}` | 2 | 51.0 | checksums are in EXTERNAL_REFERENCE_COPIES.json |
| `work/gct/*fresh_state*`, `*.mps`, `*.bas` | 3 | 30.00 | solver state: once no continuation of the 224 search is planned |
| `sources/**`, less `e3_constants.json` above | 1,209 | 29.8 | each file has the same bytes in the ZIP of prompt 54 as sent; restore from it to rerun programs |
| `work/gct/*exploration*.json`, `work/gct/*candidate*` | 54 | 11.06 | not the 13 named files below |
| `work/texbuild/**`, `work/cp*_build.log`, `NEG_NIGHT.{aux,log,out,toc}` | 22 | 2.79 | build products |
| `work/*/explore_*.py`, `work/*/*_explore.py` | 39 | 0.17 | not the 8 named files below |
| `work/finalize_cp*.py`, `work/build_pdf.py`, `work/check_pdf_layout.py` | 11 | 0.08 | packaging |
| `work/gct/*.log` | 6 | 0.02 | not the 5 named files below |
| `work/gct/source_inputs/primary_jensen/borcea_branden_2009.pdf` | 1 | 0.38 | record its checksum and locator first |

**Named files that those patterns must spare:**
- logs:
  - `check_elementary_claims.check.log`, `check_signpoint_Hecke_trace.check.log`;
  - `support132_combined_jet_932_candidate_check.log`;
  - `verify_dimension_7276.check.log`, `verify_signpoint_matrix_block.check.log`.
- scripts:
  - `explore_cyclic_local_932.py`;
  - `explore_unrestricted_hasse_moments.py`, `explore_unrestricted_mass_lp.py`;
  - `explore_unrestricted_lattice_moments.py`, with its `_cold_version.py` and `_fresh_version.py`;
  - `explore_unrestricted_shared_quadratic.py`, `explore_unrestricted_shifted_warm.py`.
- exploration data:
  - `cyclic_local_932_exploration.json`, `unrestricted_mass_lp_exploration.json`;
  - `unrestricted_lattice_M224_fresh_exploration.json`, `unrestricted_lattice_M224_hasse_exploration.json`;
  - `unrestricted_shifted_squares_M224_exploration.json`, `unrestricted_shifted_warm_M224_exploration.json`;
  - `unrestricted_weighted_squares_M224_exploration.json`.
- candidate certificates:
  - `support132_bottom_saturation_candidate_certificate.json`;
  - `support132_combined_jet_932_candidate_certificate.json`;
  - `unrestricted_difference_quadratic_107_candidate_certificate.json`;
  - `unrestricted_shared_quadratic_106_candidate_certificate.json`;
  - `unrestricted_weighted_squares_110_candidate_certificate.json`;
  - `unrestricted_weighted_squares_112_candidate_certificate.json`.

Anything matched by no pattern stays. The file-by-file classification is `inventory.tsv` in the temporary folder of §0.
