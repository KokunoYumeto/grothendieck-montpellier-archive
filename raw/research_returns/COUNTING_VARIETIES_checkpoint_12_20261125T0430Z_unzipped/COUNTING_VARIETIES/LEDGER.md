# Research ledger

Started 2026-11-24, approximately 20:30 Europe/Berlin (19:30 UTC).

Checkpoint schedule: after each 45 elapsed minutes, beginning approximately 21:15 Europe/Berlin. Each checkpoint is a fresh ZIP and includes the current independently buildable paper.

Research reviews: approximately 23:30 Europe/Berlin, then hourly; stop research after two consecutive reviews without a changed open status or a strictly smaller gate, then finish verification and presentation.

## Initial gates

| Question | State | Current gate |
|---|---|---|
| Rank-one Frobenius at every fixed prime | Proof audit in progress | Boolean normalization, geometric smoothness, complexity membership |
| Stabilization over a coefficient space | Independently re-proved; writing in progress | Point-count sign depends on Q parity |
| Saturation-only sparse generators at fixed codimension | Open | Find an algorithm or a hard reduction respecting saturation |
| Sparse coordinate changes or sparse multiples in original span | Open | Recover/obstruct a sparse hypersurface generator |
| Odd-prime bounded monomial support with many linear equations | Open | Exact boundary in support versus number of terms/equations |
| Scheme-preserving compression over the input field | Open | Rational secant-avoiding center and explicit defining ideal cost |
| Hidden split-coordinate recovery | Open | Recover Boolean algebra, Walsh support and low-rank squared rows |
| Small total Betti number | Open | Separate rank-one coherent cohomology from total l-adic rank |

No literature-priority claims will be made. Proof and computation events are recorded separately.

## First mathematical progress

- 2026-11-24: bounded-support algorithm independently re-proved for every fixed prime, including the vanishing criterion from noninjective coordinate projections.
- 2026-11-24: saturation-only scalar recovery proved for a principal anticanonical ideal when all multiplier degrees are bounded by a fixed B; independent re-proof uses low-degree syzygies and a Frobenius-truncated quotient. This strictly narrows the principal saturation gate to unbounded multiplier degree.
- 2026-11-24: split-row normalization extended from squared rows in characteristic three to (p-1)st-power rows at every fixed odd prime; separately re-proved, including the distinction between affine Boolean-exponent changes and ambient affine coordinate changes.

## Before the first checkpoint

- 2026-11-24, approximately 21:10 Europe/Berlin: the integrated manuscript compiled to 58 pages, with resolved citations and references and no overfull boxes. This is a draft build, not final visual or whole-text certification.
- The odd-prime support gate narrowed further: after linear restriction, fixed nonlinear count and anticanonical total degree give a weighted syndrome algorithm with complexity T^{c(p-1)} p^K poly(L), K=(p-1) sum(sigma_i)-m. Near-minimal support with K=O(log L) is polynomial. Independently implemented exact tests compare both the syndrome algorithm and a different truncated-ring algorithm.
- Hidden split coordinates can be recovered deterministically under a marked-base, designated-complete-quadric-span hypothesis, by two combinations over a polynomial-size finite extension followed by descent. With fixed support and bounded powered-row rank this yields an emptiness algorithm. Extracting such a span from arbitrary equations and controlling support remain open.
- A private permutation of a finite split scheme changes squared-row rank from one to four. Thus that rank is not invariant under arbitrary isomorphism of the private fibre.
- Projection has an explicit sufficient extension bound q^e>(2n+2)(a^n delta)^2 and finite elimination bounds, but no polynomial-time, polynomial-size compression over the input field has been proved.
- Fixed total l-adic Betti number over a fixed field bounds dimension and leaves finitely many smooth projective zeta functions; this obstructs decoding unbounded exact counts solely from zeta. It does not rule out modular-counting hardness with bounded Betti number.

### Current proof-check gap

The main theorem's stabilization and coefficient mechanisms have separate statement-only checks. A fresh worker is still required for the complete Boolean-to-geometric main theorem, including its normalization and complexity membership, before final certification. Existing workers distinguish their blind re-proofs from source-informed checks.

## Checkpoint 01 saved

2026-11-24 21:15 Europe/Berlin (20:15 UTC): COUNTING_VARIETIES_checkpoint_01.zip. SHA-256 3b5a92e14f6a979db0f4e15f52daf093f6f1c06ec7896a14e3317e442841c71d. It was built from a fresh copy, with no undefined references or overfull boxes, and a hash comparison found no unchanged attached files. The complete then-current contribution records were included. Next checkpoint due approximately 22:00 Europe/Berlin.

## Continued research after checkpoint 01

- Quantitative small-zeta information bound derived and independently checked: the number of zeta functions with total Betti number at most B over F_q is at most (B+1)^(2B-1) 3^B 2^(B²) q^((B³-B)/2). Exact zeta-only decoding of all n-bit integer counts therefore requires B=Omega((n/log q)^(1/3)); at fixed dimension the same coefficient count gives a square-root bound. This is an unconditional information bound, not a complete classification and not an obstruction to modular encoding with bounded B.
- Sparse factorization and cofactor literature is being checked for improvements to the unbounded-cofactor saturation gate. Characteristic-zero lacunary gap results do not automatically apply at a fixed small prime.

## Checkpoint 02 saved

2026-11-24 22:00:11 Europe/Berlin (21:00:11 UTC): COUNTING_VARIETIES_checkpoint_02.zip, 1,016,562 bytes. SHA-256 9111aca6419f8eaecd764d6cfaf450e2da2c4c45eb706db59db5fc298f7f05db. A fresh-copy build produced a 67-page PDF with resolved citations and no overfull boxes. A hash comparison found no unchanged attached files; no third-party source texts were included. The checkpoint was saved successfully. Next checkpoint due 21:45 UTC.

## Continued research after checkpoint 02

- 2026-11-24, approximately 21:16 UTC: the principal-saturation gate strictly narrowed again. A statement-only same-model reconstruction confirms deterministic polynomial scalar recovery at fixed p,B if just one listed residual cofactor has total degree at most B; all other input degrees may be unbounded and binary. Restriction to any line through a point where that input is nonzero has no extraneous common cofactor, by the saturation promise. Modular univariate gcd gives a low-degree cofactor value oracle, followed by total-degree interpolation and translated Hasse coefficient extraction. Bounded individual degree of all cofactors is now a polynomial-time special case. The unrestricted gate is the case in which every residual cofactor has unbounded total degree.
- The complete Boolean-to-rank-one theorem, the odd-prime compact complete intersection, and the ordinary-projective trinomial presentation now have fresh statement-only same-model re-proofs, with written records. These do not constitute human or formal verification.
- Complete English SGA 2 reading has finished across four assigned readers; source-use and caveat records are being consolidated.
- 2026-11-24, 21:41 UTC: the higher-codimension saturation gate strictly narrowed. For fixed p,c,E, a long sparse list with smooth geometrically integral anticanonical complete-intersection saturation admits polynomial scalar recovery whenever 0<=c*max(deg inputs)-(N+1)<=E. No regular sublist is input. The proof constructs regular combinations over an explicit finite extension of polynomial degree, uses a bounded-degree annihilator line and the Koszul Frobenius adjoint, then descends by a norm. A more flexible indexed-sublist version allows fixed total excess and a fixed degree gap. The indexed theorem has an independent statement-only re-proof; the stronger no-sublist theorem has a full source-informed check and a fresh independent attempt in progress. Six original finite tests include nonreduced intermediate complete intersections and zero/nonzero scalars.

## Checkpoint 03 saved

2026-11-24 22:45:48 Europe/Berlin (21:45:48 UTC): COUNTING_VARIETIES_checkpoint_03.zip, 1,218,875 bytes. SHA-256 eba0a43fc66ca8ddad74fb806d6f668149167f17b1d0f925e12035e1072630c4. The 129-file checkpoint was saved at 21:46 UTC. A fresh-copy build produced an 81-page, 803,935-byte PDF with resolved citations and no overfull boxes. A content-hash comparison found no unchanged attached files, and no third-party source texts or generated TeX auxiliaries were included. The stronger no-sublist independent reconstruction was completed after the checkpoint snapshot and will enter the next scheduled checkpoint. The next checkpoint and first three-hour research review are due at 22:30 UTC.

## Continued research after checkpoint 03

- 2026-11-24, 21:51 UTC: the complete independent no-sublist reconstruction was read and passed. It uses a different construction: an uncomputed avoiding plane, a bounded-degree homogeneous resultant, and Kronecker specialization over an extension of controlled degree. Its semilinear quotient-line identity and norm descent were checked explicitly. Both higher-codimension results now have written statement-only re-proofs, followed separately by source audits.
- 2026-11-24, 21:53 UTC: a statement-only reconstruction establishes a Monte Carlo version of the sparse-cofactor algorithm when the good residual cofactor is not designated. Bounded-output sparse interpolation candidates are validated against the exact line-gcd oracle, and a union bound makes the error at most the supplied epsilon. This removes the index requirement only in the randomized version; the deterministic unidentified-index gate remains.


## First three-hour research review

Review basis: the initial question set and the strongest proved results now in the paper. The elapsed research interval began around19:30UTC; the recorded review time is 2026-11-24 22:30:16 UTC. The review concerns mathematical movement, not packaging or formatting.

**Movement: yes. Consecutive reviews without mathematical movement:0.** The principal saturation gate has narrowed from arbitrary sparse multiples to the residual case beyond one bounded-degree cofactor or a designated polynomial-degree/sparsity cofactor, with an additional randomized unidentified-index version. More strongly, fixed-codimension saturation is now solvable by a zero-error randomized algorithm whenever the actual input ideal after finite extension contains a regular sequence of bounded total excess. No tuple, degree profile or extension must be supplied; all other binary degrees are unrestricted. This strictly contains the earlier indexed fixed-gap class and the deterministic balanced-degree class as a randomized scope. The initial unresolved saturation question therefore has a strictly smaller gate, not merely another restatement.

The complete rank-one counting and universal-stabilization theorems, the compact sparse CI, and the projective trinomial presentation have statement-only same-model re-proofs. The two newest saturation theorems have separately saved statement-only reconstructions at22:09:37 and22:14:27UTC, then source-informed comparisons. Six nonreduced finite-slice tests and three regular-combination tests exercise the new algorithm. These are finite checks, not formal or human verification. The short Walsh multiplier positive construction has full source-informed proof checks but its demanded independent reconstruction remains an explicit checking task; unsuccessful independent attempts are preserved and are not relabelled as re-proofs.

### Main questions at this review

| Main question | Status and strongest current reduction |
|---|---|
| Fixed-prime modular counting on a smooth projective coherent line | Proved on the arithmetic-circuit and smoothness promise, with every fixed prime and the separate uniform-in-p cost. |
| Sparse presentations after saturation | Deterministic principal cofactor and balanced/fixed-gap CI algorithms; zero-error randomized bounded-input-ideal-CI-excess algorithm. Remaining unrestricted case: unbounded least excess, with deterministic selection a separate bounded-excess gate. |
| Support and compression | Logarithmic-support and logarithmic-excess algorithms; hardness at every fixed positive power of degree excess. Rational scheme-preserving polynomial-size compression over the input field remains open. |
| Small total Betti number | Exact zeta-only constant-B encoding over fixed q is impossible, with cube-root and fixed-dimension square-root quantitative lower bounds. Least growth and constant-B modular encoding remain open. |
| Natural polynomial-time invariants | The specified coarse invariants fail to recover the scalar, with explicit collisions. No classification of all possible efficiently computable invariants is claimed. |

### Every still-open row

| Question key | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Principal one-small-cofactor and fixed-codimension bounded input-ideal CI excess are solved in their stated deterministic or Las Vegas scopes; unrestricted remaining excess and derandomization remain |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Randomized recovery now holds if the actual input ideal after finite scalar extension contains a regular c-sequence of fixed total excess, without supplying it; other input degrees are arbitrary binary integers. Unbounded least CI excess and deterministic derandomization remain gates.; sp:thm:generators;sci:thm:gap;sci:thm:balanced;sci:thm:random-excess |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded excess after finite extension is now sufficient in expected polynomial time; no bound follows from smooth anticanonical saturation alone |
| Q-CI-DERANDOMIZE | current gate | Deterministic balanced-degree and fixed-gap subclasses are solved; choosing certified regular combinations and sufficient kernel-detecting fibres without randomness remains |
| Q-WALSH-INDEPENDENT-POSITIVE | check gate remains; positive mathematical statement not refuted | Converse proved unseen; positive general construction not obtained; see independent_walsh_attempt.md |

The next mathematical review is due at23:30UTC. Research continues on the residual saturation, support and compression gates. Expert and newcomer readings, every-page visual inspection, and predeposit-format completion continue separately and do not count as mathematical movement.

## Checkpoint 04 saved

2026-11-24 23:30:20 Europe/Berlin (22:30:20 UTC): COUNTING_VARIETIES_checkpoint_04.zip, 1,407,138 bytes. SHA-256 e7ae59cf1d0904c38baccfbd73c2bba9eec8edccf9023645a9db958867223aef. The154-file checkpoint contains an89-page,855,244-byte PDF built from a fresh directory with no undefined or duplicate references and no overfull boxes. It includes the first three-hour review at22:30:16UTC, all current independent and source-informed saturation records, the complete SGA2 coverage table, and the new finite-slice computations. A hash comparison found no unchanged attached files. The archive was saved successfully. The next checkpoint is due23:15UTC; the next mathematical review is due23:30UTC.

## Research developments after the first review, 22:46–23:14 UTC

The higher-codimension saturation gate has strictly narrowed. A graded free residual quotient proves that a fixed Newton grid recovers the degree-e annihilator exactly on every finite fibre, independently of the other binary input degrees. The grid and residual-freeness claim received a separate statement-only reconstruction before the originating proof was opened, a full source-informed comparison, and an expert delta reading.

Unequal-degree candidate regular sequences are now constructed deterministically by a prime-degree field tower. Thus the general bounded-excess theorem randomizes only the good projection centre. Scalar descent uses a coprime field degree and an inverse norm exponent; arbitrary-field kernel recovery is distinguished from that scalar statement.

A further deterministic theorem handles dim K_1=c-1. The fixed-number-of-linear-powers restriction gives the established semidiagonal identity test, whose complete small-characteristic mechanism and explicit finite-field bit model were checked from Saha–Saptharishi–Saxena. A separate statement-only geometric reconstruction preceded proof exposure. This closes the centre problem on that subclass; the remaining centre case has dim K_1<=c-2.

Radical-safe sparse Frobenius digit reduction now applies in every codimension. Full coordinate-cover examples have unbounded original CI excess but bounded excess after processing; a second such family enters the deterministic linear-prefix class. The pure-powers-only example was rejected because it generally has nonreduced saturation, and the valid cover-row example replaces it. General monomial-content division is not included.

The expert completed delta2 and delta3, including all new proofs and primary-source scope checks. The newcomer completed the entire checkpoint04 text and authorized clarity revisions; a final delta reading remains required after research stabilizes. A new excess-two two-parameter finite-grid computation passed in characteristics3,5,7. All fetched third-party PDFs/texts remain outside the deliverable tree.

This is a dated development record, not an extra hourly research review. The next scheduled research review remains23:30UTC, with the stationary counter still0 from the22:30 review. The next checkpoint is due23:15UTC; no checkpoint has been saved between the prescribed times.


## Checkpoint 05 saved

2026-11-24 23:15:16 UTC: COUNTING_VARIETIES_checkpoint_05.zip, 1,592,471 bytes. SHA-256 02bfaf79e37b43d3a59f26ad2e61f35176fbd03a0fa7c0d4575dbc183bcae465. The 207-file checkpoint contains a 94-page, 891,199-byte PDF built from a fresh directory with no undefined or duplicate references and no overfull boxes. It includes the deterministic fibre grid, unequal-profile candidate list, linear-prefix deterministic algorithm, radical-safe digit deflation and strict example families, together with their independent reconstructions or complete source-informed checks. The expert delta2 and delta3 reports and the newcomer whole-text and delta records are included. The archive was saved successfully at approximately 23:15:35 UTC. A content-hash comparison found no unchanged attached files, and no third-party paper or extraction is included. The next scheduled checkpoint is due 2026-11-25 00:00 UTC; the next mathematical review is due 2026-11-24 23:30 UTC.


## Second scheduled research review: 2026-11-24 23:30:08 UTC

**Movement: yes. Consecutive reviews without mathematical movement: 0.** The comparison interval is the first review at 22:30:16 UTC to this actual clock reading. The following are mathematical reductions of the main saturation gate, not packaging or checking activity.

1. Every finite fibre now detects the colon through a fixed total-degree-e Newton grid, with no numerical-degree bound on the other sparse rows. This removes the earlier random kernel-sampling gate.
2. Unequal-degree regular-tuple candidates are constructed deterministically over prime-degree field towers. Under the bounded-excess promise, only construction of a certified good projection centre remains randomized.
3. The centre is constructed deterministically when dim K_1=c-1. The remaining unrestricted bounded-excess centre case therefore has dim K_1<=c-2.
4. Radical-safe digit deflation works in arbitrary codimension. Explicit complete coordinate-cover families have unbounded original CI excess but bounded processed excess, including a deterministic linear-prefix family. Thus the unbounded-excess gate is now stated after this safe polynomial preprocessing.

The independent positive Walsh reconstruction was completed and checked during this interval. It closes a checking obligation, and is **not** being used as mathematical movement in this review. Expert/newcomer readings, index corrections, PDF work and checkpoint saving likewise do not count as movement. A factored-linear-prefix deterministic centre theorem is under independent review; it is not counted as proved at this review.

### Main questions at this review

| Main question | Status and strongest current reduction |
|---|---|
| Fixed-prime modular counting on a smooth projective coherent line | Proved for circuit input under the smoothness promise, with exact residue versus nonzero decision distinguished and uniform-in-p costs stated. |
| Sparse equations after saturation | Principal small-cofactor and fixed-codimension bounded processed CI-excess cases are solved in their stated deterministic or Las Vegas scopes. The bounded-excess random choice is only a centre; dim K_1=c-1 is deterministic. The unrestricted residual gate has unbounded processed excess. |
| Support and compression | Logarithmic support/excess algorithms and fixed-positive-power excess hardness remain as before. Construction of rational scheme-preserving sparse compression over the stated input field remains open. |
| Small total Betti number | Fixed-q constant-total-Betti exact zeta-only encoding is excluded, with quantitative lower bounds. Least growth and constant-B modular encoding remain open. |
| Natural polynomial-time invariants | Explicit collisions refute recovery from the specified coarse invariants. No classification of all polynomial-time invariants is claimed. |

### Every still-open indexed row

| Question key | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after radical-safe digit deflation has Las Vegas recovery; deterministic balanced/gap/linear-prefix and supplied-centre subclasses are proved. Unbounded residual excess and general deterministic centre construction remain. |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after radical-safe digit deflation has Las Vegas recovery; deterministic balanced/gap/linear-prefix and supplied-centre subclasses are proved. Unbounded residual excess and general deterministic centre construction remain. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after radical-safe digit deflation has Las Vegas recovery; deterministic balanced/gap/linear-prefix and supplied-centre subclasses are proved. Unbounded residual excess and general deterministic centre construction remain. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid; the linear-prefix case dim K_1=c-1 is solved. Remaining centre case has dim K_1<=c-2, after safe radical digit processing. |

A new proposed deterministic factored-prefix subclass is being checked from its statement before manuscript integration. Its exact input representation and proof dependencies are recorded separately; no change of status is claimed yet.

The next hourly mathematical review is due 2026-11-25 00:30 UTC. The next checkpoint remains due at 00:00 UTC. If the next two hourly reviews record no open-row resolution or strictly smaller main gate, research will stop at the second such review and final checking and delivery will follow.


## Research developments after the second review, through 23:58 UTC

The deterministic factored-prefix theorem is now in the paper. Its separate statement-only reconstruction uses a simpler component-witness merging method and was saved at23:38:41UTC before originating-proof exposure. The input explicitly designates an original regular tuple and its first c−1 linear-factor decompositions; this extra representation information is retained in the statement.

The saturation gate has further narrowed through certified coordinate division. Speculative preprocessing is used only to find finite quotient algebras imposing the original equations; a nonzero coordinate image is a sound global nonmembership certificate. On the true branch a degree-one deterministic grid finds every removable coordinate. Bounded CI excess after this processing and digit deflation has a zero-error polynomial algorithm, with centres its only random choices. The processed linear-prefix case is deterministic. The Fermat cover family has least excess exactly N−1 after digit-only processing and zero after certified division. Root checked the complete original proof and wrote the full result, deterministic corollary and family in a separate local LaTeX input. A separate statement-only reconstruction is being completed; its exact save boundary will be recorded, not backdated.

The complete positive Walsh reconstruction closes its earlier independent-checking gate. It additionally proves mask weight at most five; this full bounded-degree result and proof now appear in the paper. Earlier failed attempts remain preserved. The canonical record audit added a manual unnumbered-statement supplement, corrected the exact-formula stabilization mapping and rank-counterexample refutation target, repaired evidence paths, and consolidated repeated imports without deleting original dated records. These checking/indexing actions are not counted as mathematical movement. The next scheduled review remains00:30UTC.

At23:59:39UTC the separate certified-monomial statement-only reconstruction was saved before source exposure, SHA-256 783935482e1eb34a1368dac9a33c5402afedd9693788d62d5d8de75f5da5cb99. It is included in the scheduled checkpoint. Root's comparison with that separate proof will follow the checkpoint; the complete originating proof and manuscript derivation already received source-informed checks. The independent worker also proves c=1; the newly integrated higher-codimension theorem currently states c>=2, while the principal case is covered earlier.


## Checkpoint 06 saved

2026-11-25 00:00:21 UTC: COUNTING_VARIETIES_checkpoint_06.zip, 1,785,006 bytes. SHA-256 a9298bd3227ccafdba47ac4e85191a427b5e07b0c2c142d99ca5b095374e31ec. The242-file archive contains a102-page,933,404-byte PDF built from a fresh directory, with resolved references and no overfull boxes. The artifact was saved successfully. Its content-hash scan found no unchanged attached file. It contains the full certified-coordinate and factored-prefix additions and the bounded-degree Walsh multiplier, plus the separately saved certified-preprocessing reconstruction at23:59:39UTC. The final every-page visual inspection and final expert/newcomer delta readings remain outstanding. The next checkpoint is due00:45UTC; the next hourly research review is due00:30UTC.


## Third scheduled research review: 2026-11-25 00:30:35 UTC

**Movement: yes. Consecutive reviews without mathematical movement: 0.** This compares the previous scheduled review at 2026-11-24 23:30:08 UTC with the present observed clock. Certified coordinate-content removal, interleaved with the proved radical-safe digit operation, gives a strictly smaller saturation gate. The Fermat cover family has unbounded least regular-sequence excess after digit-only processing and excess zero after the certified coordinate division. The theorem, its deterministic processed-linear-prefix corollary, and the strict family are fully proved in the manuscript and have completed separate same-model statement-only and source-informed checks.

The factored-linear-prefix deterministic centre theorem is also now proved and checked, with its designated original tuple and given prime-field linear factors explicitly required. It extends a marked subclass; no factorization or extraction from an arbitrary unmarked list is claimed. The broad unmarked derandomization gate remains construction of a certified good centre.

The new constant-field relation preprocessing has a complete mechanism-exposed proof and source-informed root check. Its statement-only reconstruction is still in progress at this review, and a stronger arbitrary-monomial recognition variant is being separately recorded. Neither variant is used as the reason for movement at this review. The explicit dense Cartier iterate establishes an obstruction to monomial-state enumeration, not scalar hardness and not a smaller unrestricted scalar gate; it likewise is not counted as movement. Completion of independent checks A--G, editorial qualifications, record consolidation and PDF builds do not count as mathematical movement.

### Main questions at this review

| Main question | Status and strongest current reduction |
|---|---|
| Fixed-prime modular counting on a smooth projective coherent line | Proved for circuit input under the stated smoothness promise, with exact residue and nonzero decision tasks distinguished. The universal coefficient stabilization and point-count sign have full proofs and checks. |
| Sparse equations after saturation | Bounded excess after certified coordinate-content and radical digit processing has a zero-error randomized polynomial algorithm. Only centres are randomized; the processed linear-prefix and designated factored-prefix cases are deterministic. Unbounded processed excess and general centre derandomization remain. |
| Support and effective compression | Logarithmic support-excess algorithms and fixed-positive-power excess hardness are proved. Rational, scheme-preserving, efficiently constructed sparse compression over the specified input field remains open. |
| Small total Betti number | Fixed-field constant-total-Betti exact zeta-only encoding is excluded with quantitative bounds. The least possible growth and constant-Betti modular encoding remain open. |
| Natural polynomial-time invariants | Explicit collisions refute recovery from the specific coarse invariants studied. No classification of every polynomial-time invariant is claimed. |

### Every still-open indexed row

| Question key | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal interleaved with radical-safe digit deflation has Las Vegas recovery; a processed linear prefix is deterministic. Unbounded excess after this safe processing and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal interleaved with radical-safe digit deflation has Las Vegas recovery; a processed linear prefix is deterministic. Unbounded excess after this safe processing and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after certified coordinate-content removal interleaved with radical-safe digit deflation has Las Vegas recovery; a processed linear prefix is deterministic. Unbounded excess after this safe processing and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid. A processed linear prefix dim(K_circ)_1=c-1 is solved, as is a designated factored prefix with its factors given. The unmarked remaining case lies beyond these hypotheses, after certified coordinate and digit processing. |

The next hourly review is due 01:30 UTC, and the next checkpoint remains due 00:45 UTC. Research continues on geometric-integrality preprocessing and the unrestricted residual gate. If the next two scheduled reviews have no open-row resolution or strictly smaller main gate, research stops at the second such review and final checking and delivery follow. No earlier checkpoint is changed.


## Developments after the third review, through 00:44 UTC

The prime-field relation theorem and its arbitrary-monomial recognition strengthening are proved and source-checked, and have entered a complete new manuscript input with the growing-dimensional strict family and Cartier support obstruction. The original support-monomial statement-only reconstruction was frozen at00:41:23UTC and read in full by root at the00:43:36UTC tool boundary. Its conditional treatment of named earlier rules is preserved. The stronger isolated recognizer is under separate reconstruction with the exact degree-decrease interface supplied as background. The combined certified-coordinate proof now uses these safe, support-nonincreasing identity steps; its original finite-quotient certificate remains unchanged. The new theorem is not a universal factorization algorithm. A still more general linearized-block statement is recorded but unreviewed and is not asserted in the paper.

All seven remaining independent reconstructions and their full originating-proof comparisons have completed; exact original hashes and changed-input preservation are recorded. Newcomer delta02 covers the frozen pre-geometric input and identifies the later changes still to read. Its grid-per-tuple qualification, precise Macaulay reference, coordinate-index notation, and nonzero cofactor promise have been applied. Current working PDF has a clean build; final every-page visual inspection remains outstanding.


## Checkpoint 07 saved

2026-11-25 00:45:59 UTC: COUNTING_VARIETIES_checkpoint_07.zip, 2,286,465 bytes, SHA-256 239272f3e5ec0a042514c650142f5b3d551df8aac239e44306666c3d80671dfc. The335-file archive contains a107-page,966,965-byte PDF built from a fresh copy, with no unresolved or duplicate references and no overfull boxes. The artifact was saved successfully. No unchanged attached file was found by the content-hash comparison. The archive includes all current independent proof records and the new geometric-preprocessing input. It does not certify final every-page visual review. The next checkpoint is due01:30UTC, coinciding with the next scheduled research review.


## Fourth scheduled research review: 2026-11-25 01:31:15 UTC

**Movement: no. Consecutive reviews without mathematical movement: 1.** This review was due01:30UTC and is recorded at the first observed clock after the ongoing proof work. The prior review already recorded the complete constant-field mechanism and root check, although its separate reconstruction was still pending. Completion of that reconstruction is a checking event, not new mathematical movement. The later arbitrary-block linearized recognizer is now proved and integrated, but no strict enlargement over the full closure of the already available two templates has been proved. It therefore does not reset the research clock merely by introducing and closing a more narrowly phrased row. The explicit Cartier-support obstruction remains a representation limitation, not a smaller scalar-computation gate.

The affine no-root statement has a complete originating proof and a separately frozen reconstruction, with full comparison still in progress. Its possible row splitting and total-support control are recorded explicitly. No strict enlargement over the earlier preprocessing closure is claimed for it. A new homogeneous zero-sum route is under development: retaining every prime-field component may permit a safe degree reduction without selecting one component. Its global support growth and a proposed strict family are not yet fully checked, so it is not counted as movement here.

### Main questions at this review

| Main question | Status and strongest current reduction |
|---|---|
| Fixed-prime modular counting on a smooth projective coherent line | Proved in the circuit model, with exact-residue and nonzero decision distinctions, universal stabilization and point-count congruence. |
| Sparse equations after saturation | Bounded CI excess after the current certified coordinate, radical digit and recognized prime-field relation processing gives a zero-error randomized polynomial algorithm. A processed linear prefix and a designated factored prefix permit deterministic centres. Unbounded processed excess and general deterministic centre construction remain. |
| Support and effective compression | Logarithmic support-excess algorithms and fixed-positive-power excess hardness are proved. Efficient scheme-preserving compression over the input field remains open. |
| Small total Betti number | Exact constant-Betti zeta-only encoding is excluded at fixed field. Optimal growing Betti bounds and constant-Betti modular encoding remain open. |
| Natural polynomial-time invariants | The specified coarse invariants have explicit collisions. No classification of all polynomial-time functorial invariants is claimed. |

### Every still-open indexed row

| Question key | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and recognized prime-field linearized relations has Las Vegas recovery; a processed linear prefix is deterministic. The growing-dimensional Fermat family proves strict enlargement over coordinate/digit processing. Unbounded excess after these operations and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and recognized prime-field linearized relations has Las Vegas recovery; a processed linear prefix is deterministic. The growing-dimensional Fermat family proves strict enlargement over coordinate/digit processing. Unbounded excess after these operations and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and recognized prime-field linearized relations has Las Vegas recovery; a processed linear prefix is deterministic. The growing-dimensional Fermat family proves strict enlargement over coordinate/digit processing. Unbounded excess after these operations and general deterministic centre construction remain. The factored-prefix subclass requires its designated split factors as additional input. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid. A processed linear prefix dim(K_circ)_1=c-1 is solved, as is a designated factored prefix with its factors given. The remaining case lies beyond these hypotheses after certified coordinate, digit and recognized prime-field relation processing. |

The next scheduled hourly review is due02:30UTC. If it also records no open-row resolution or strictly smaller main gate, research stops at that review and final checking and delivery follow. The checkpoint due01:30UTC is being saved now, with its exact build and persistence times recorded separately; the next checkpoint remains due02:15UTC. No earlier archive is changed.


## Checkpoint08 saved

2026-11-25 01:32:25 UTC: fresh build for COUNTING_VARIETIES_checkpoint_08.zip, 2,444,100 bytes, SHA-256 e1edd2db603003b01bd4245eb2aadc5231d0febaa24711f74c65b7420f446dd9. The381-file archive contains a108-page,972,550-byte PDF, with no undefined or duplicate references and no overfull boxes. Persistence succeeded. No unchanged attached file was found. The new general linearized theorem and its separate reconstruction are included; the affine theorem remains a separately recorded checked proposal awaiting manuscript integration and completed comparison. The final every-page visual review is still outstanding. Next checkpoint02:15UTC; next review02:30UTC.


## Storage recovery and new follow-up intake

2026-11-25T02:13:46.884829+00:00: A second shared-workspace capacity incident interrupted the append to contributions/core/LITERATURE.md at16,384 bytes. The pre-existing prefix was intact; the complete intended append was restored by atomic replacement after space recovery. SOURCES.tsv was complete and unchanged by this repair. Only this run's temporary staging and already-extracted source directories were relocated under /tmp; all1,721 staging files and316 extracted-source files were compared byte-for-byte before their original paths were replaced by symlinks. No original attachment or saved checkpoint was changed.

The newly attached follow-up was read completely at02:12UTC. It adds a referee audit of the Artin–Mazur/Stienstra height-one deduction, higher-height complexity, and exact DP_MULT statements DP1/DP3/DP34 after the current preprocessing item, under the existing proof, checkpoint and review rules. These are new requested tasks, not established results. Personal Context returned unavailable; retrieval of the named DP_MULT material continues through available file access. The zero-sum independent draft was frozen at02:08:52UTC and root has read its full proof; source comparison is now authorized separately. The root-origin support budget is correct but weaker than the independently proved linear logarithmic support bound.


## Checkpoint09 and completed zero-sum integration

Checkpoint09 was freshly built at2026-11-25 02:15:37UTC:2,774,471 bytes,454 files,110-page PDF of982,088 bytes, ZIP SHA25636d2aa689f1c0eac496dd09a55a3b61e6d479fe681654b76dad5f916fcf88ef8. Persistence succeeded; no undefined or duplicate references, overfull boxes, or unchanged attached-file matches. The snapshot contains the full frozen zero-sum independent proof and draft section, before its later main inclusion. Next checkpoint03:00UTC.

2026-11-25 02:24:50 UTC: The zero-sum rule and strict family are now integrated into the manuscript, introductory preprocessing convention, certified theorem, and Questions. A fresh working build succeeded. The independent comparison identified an omitted contraction in the draft tree-count sentence. The replacement height-times-leaves proof gives total support <=16*T0*max(1,log_p D0), counts unary transitions explicitly, and strengthens the earlier budget. Source-informed expert delta6 explicitly retracts delta5's overbroad unary justification; both historical reports remain intact. A separate combined statement-only reconstruction covers the enlarged interface; full source comparison is completing. This is genuine mathematical progress during the current hourly interval: Q-CI-ZERO-SUM is proved and the strict characteristic-two family enters a polynomial designated-cofactor class beyond all preceding row rules. Review scheduling remains unchanged.

The new formal-group work begins after this current item. Exact DP_MULT source retrieval succeeded from the resolved earlier ALP_MACHINE archive, which stays outside every deliverable. No unverified higher-height complexity claim has been adopted.


## Hourly research review scheduled02:30UTC

Actual review: 2026-11-25 02:31:48 UTC. **Movement: yes. Consecutive stationary reviews:0.**

Since the preceding01:31 review, the zero-sum relation theorem was proved with complete hidden-data recognition, an exact ideal-divisibility certificate, a linear logarithmic total-support bound, and full polynomial iteration. Its characteristic-two family survives every earlier displayed-row rule and enters the polynomial numerical-degree-and-support cofactor class. This closes Q-CI-ZERO-SUM and strictly enlarges the proved saturation-recovery class. The origin proof was completed during this interval; this review does not count later checking or packaging alone as progress. The independent reconstruction exposed and repaired a tree-count wording omission before integration.

The new user follow-up adds formal-group questions after that completed item. Their source audit and higher-count calculations are in progress; no unverified higher-height classification is counted as a resolution. The table records every currently open or conditional question, including the new requests.

| Question | Status | Current gate or exact limitation |
|---|---|---|
| Q-CUBIC-MOTIVE | proved conditional only on stated standard cofiber/purity background | Normal framing integral over Z; base-change argument explicit |
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| Q-MAIN-INDEPENDENT | closed | The whole main theorem was independently reconstructed by blind_main at20:40:52UTC before proof-source exposure; the earlier contribution-specific limitation remains preserved in its original record |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid. A processed linear prefix dim(K_circ)_1=c-1 is solved, as is a designated factored prefix with its factors given. The remaining case lies beyond these hypotheses after certified coordinate, digit, nonzero-sum, affine and zero-sum prime-field relation processing. |
| Q-WALSH-INDEPENDENT-POSITIVE | closed | A complete statement-only same-model re-proof of the positive construction and converse was saved at 2026-11-24 23:23:36 UTC by walsh_blind, before manuscript or other proof exposure; root whole-proof check passed. Earlier failed attempts remain preserved as failed or partial attempts. |
| Q-WALSH-SELECTOR-SOURCE-AUDIT | verified after source exposure | Full source proof checked at 2026-11-24 23:32:20 UTC; binary increments cover the whole interval, positive H has exact valuation a, table size N is O(a), and at most 3N-1 masks are output; SOURCE_AUDIT.md |
| Q-FORMAL-HEIGHT-ONE | open | New follow-up: exact original source statements and coefficient normalization must be checked; no theorem yet asserted. |
| Q-FORMAL-HEIGHT-THREE | open | New follow-up: higher logarithm numerator and p-adic precision not supplied by the modulo-p scalar alone. |
| Q-FORMAL-ALL-HEIGHTS | open | New follow-up: must distinguish fixed height, variable height, promises, upper bounds and matching hardness. |
| Q-FORMAL-DP-MULT | open | Exact requested source statements not yet located; contextual summaries are not proof. Personal Context unavailable; file search ongoing. |

Next scheduled review03:30UTC. Two consecutive scheduled reviews without an open-row resolution or strictly smaller main gate still trigger the research stop and final verification. Next checkpoint03:00UTC; no extra checkpoint is created by this review.


## Formal-group research before checkpoint10

2026-11-25 02:58:53 UTC: The Artin–Mazur/Stienstra source audits and exact DP_MULT retrieval are complete as separate source-informed reports. The primary separately froze a height-one reconstruction before reading its originating report; full comparison is pending. A new origin proof gives the higher replica coefficient, its cyclic-orbit #P interpretation, a same-Boolean-function counterexample, fixed-threshold modular completeness, and an exact-height seed dichotomy. Its statement-only independent reconstruction is still in progress. A second reader is independently reconstructing the generic invariant-derivative laws. None of these new proofs has yet been integrated into the manuscript or labeled independently certified in this checkpoint.

Primary-source work has located a finite-height geometric bound, a full zeta algorithm, and supersingular elliptic seeds over every prime field. Their combined complexity proof is still being written. New finite-height existence results require explicit separation of algebraically closed fields from F_p; no universal prime-field realization claim has been adopted. The all-height and infinite-height lower-bound questions remain open. The scheduled research review remains03:30UTC and the checkpoint remains due03:00UTC.


## Checkpoint10 saved

Fresh build2026-11-25 03:00:31UTC; persistence completed by2026-11-25 03:01:11 UTC. COUNTING_VARIETIES_checkpoint_10.zip contains577 files and a114-page PDF of1,008,359 bytes. ZIP3,256,434 bytes, SHA256affedc57254dacd72161a828868a75ab4bbd46694affcfb4381938dfef845e2c. No undefined or duplicate references, no overfull boxes, and no unchanged attached-file matches. Exact copies of the newly supplied follow-up that had entered two audit snapshots were excluded before packaging; their historical hashes and exclusion mapping are preserved, while frozen reports are unchanged. The final every-page visual review remains outstanding. Next checkpoint03:45UTC; next hourly review03:30UTC.


## Hourly research review scheduled03:30UTC

Actual review: 2026-11-25 03:31:31 UTC. **Movement: yes. Consecutive stationary reviews:0.**

During this interval, the formal-group follow-up acquired complete proofs of its first-height deduction with the curve and denominator corrections, the genuine cyclic-orbit #P next invariant, the same-Boolean-function counterexample, and modular completeness for every fixed finite lower threshold. Generic invariant-derivative bounds and whole-operator next-height criteria were proved in full and reconstructed by a separate instance. These close Q-FORMAL-HEIGHT-ONE, Q-FORMAL-HEIGHT-THREE, and Q-FORMAL-DP-MULT in their exact scopes. The full height, including infinity, now has a polynomial-space algorithm; its coefficient-access and matrix-power proof has a separately frozen reconstruction and post-freeze comparison. This is genuine progress on requested open questions, not checking or packaging alone.

The new all-height prime-field seed construction is only a frozen proposal under independent attack at this review. It is not counted as a completed resolution. Exact-height membership and the seed dichotomy are proved; the remaining existence premise is currently under that check. Infinite-height matching hardness remains a separate open gate. Sparse saturation/compression and small-Betti gates are unchanged during this interval.

| Main question | Strongest current proved state |
|---|---|
| Rank-one coherent Frobenius | Fixed-prime circuit completeness, universal smooth stabilization and exact scalar/point-count normalizations are proved. |
| Sparse saturation | Certified coordinate, radical digit, and three prime-field relation rules feed bounded-excess Las Vegas recovery; deterministic linear/factored prefix cases and designated polynomial cofactors are solved. Unbounded residual complexity and general centre derandomization remain. |
| Support/compression | Logarithmic excess is tractable; fixed positive-power excess remains hard. Effective scheme-preserving compression over the input field remains open. |
| Small zeta/invariants | Fixed-field bounded-Betti exact zeta encoding is obstructed; modular encoding and general natural-invariant classifications remain at the recorded gates. |
| Formal heights | Every fixed lower threshold is Mod_p P-complete; exact fixed height is complete whenever its prime-field seed exists; full height is in PSPACE. Infinite-height hardness is unresolved. |
| Invariant derivatives | Generic unramified Witt-lift bounds, sharp witnesses, infinity endpoint and next-height operator equivalence are proved. Honda-dual-specific data are not inferred from height alone. |

### Every still-open indexed row

| Question | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid. A processed linear prefix dim(K_circ)_1=c-1 is solved, as is a designated factored prefix with its factors given. The remaining case lies beyond these hypotheses after certified coordinate, digit, nonzero-sum, affine and zero-sum prime-field relation processing. |
| Q-FORMAL-ALL-HEIGHTS | partly proved; residual gate | Every fixed exact finite height is in Mod_p P and is complete if one prime-field seed exists; otherwise its yes-locus is empty. Height two has a verified elliptic seed for every p. The full height including infinity is computable in O_p(L^2 log L) space. An explicit all-height prime-field seed proposal is under separate statement-only check. Matching hardness for infinite height remains open. |
| Q-FORMAL-INFINITE-HARDNESS | current gate | PSPACE membership is proved. Fixed-threshold reductions alone do not imply any lower bound for the infinite-height predicate. Need a polynomial-size construction enforcing an infinite-height alternative or a reduction to the finite monomial operator respecting the geometric constraints. |
| Q-FORMAL-PRIME-FIELD-SEEDS | open; explicit proposal under independent check | A deterministic coefficient seed with prescribed multinomial multiplicities and finite-jet smoothing is frozen. Origin proof awaits a separate statement-only reconstruction; no all-height conclusion adopted yet. |

Next scheduled hourly review04:30UTC. Two consecutive scheduled reviews without an open-row resolution or strictly smaller main gate still trigger the research stop and final checking. Next checkpoint03:45UTC; this review creates no extra checkpoint.


## Integration before scheduled checkpoint 11

At 2026-11-25 03:43:43 UTC, the formal-height, higher-counting, polynomial-space and invariant-derivative sections are integrated. The working manuscript had built at 133 pages before the explicit elementary polynomial-time corollary and direct Yobuko citations were added. Canonical consolidation now contains 465 scoped check events, 147 registered statements, 148 crosswalk rows, 77 questions and 93 source records. Classification migration preserves the earlier raw rows while removing a mere input freeze from mathematical checks and explicitly limiting the originating proof self-check. The old author text of formal_counting.tex is preserved byte for byte before the p-primitivity clarification.

Root has read the complete originating all-height seed proof and the complete formal-height literature audit and finds the arguments valid in their stated scopes. The separate seed reader reports a complete reconstruction, including exact coefficient preservation through p^h and the smooth degree p^h+p+1 output. Its full proof is still being frozen, so the main exact-height theorem remains conditional at this integration event. No seed result is silently counted as independently complete before that record is available. The expert integration read found no substantive defect and requested the wording, notation and explicit elementary-P proof corrections now made.


## Checkpoint 11 saved and all-height independent proof received

The scheduled checkpoint was built fresh at2026-11-25 03:45:21UTC and saved by03:46:12UTC. COUNTING_VARIETIES_checkpoint_11.zip has674 files, 3,723,864 bytes, SHA2565ec337014db3862729daec9078eb73086128c4699e6e97d58436a3f6f1569064. Its PDF has134 pages and1,124,671 bytes. The fresh build has no undefined or duplicate references and no overfull boxes. The attachment-hash exclusion scan found no unchanged copies. This checkpoint remains immutable and precedes final receipt of the new seed proof. Next checkpoint04:30UTC.

The complete all-height seed reconstruction was frozen at03:45:33.134027UTC, before any originating proof exposure: all_height_seed_blind/RECONSTRUCTION_DRAFT.md,599 lines,20,227 bytes,SHA256b0d62dd5a3fe1e8574426b80f983cfd3c8a011149d40fa7cf3f206764893616d. Root read every line by03:46:12UTC and checked the full proof against the earlier originating proof. All seed assertions and the exact integral smoothing identity pass. The proof also independently verifies smoothness and geometric integrality and treats h=1 by G=x1,Q=2p. Thus every prime and every finite positive h has a smooth anticanonical hypersurface of degree and variable count p^h+p+1 with exact height h. Together with the separately proved fixed-seed reduction, every fixed finite exact-height predicate is Mod_p P-complete. The isolated seed worker was authorized for source comparison only after this freeze and root reading; that separate comparison is being preserved. The all-height seed gate is now mathematically resolved and is substantive progress for the next scheduled hourly review. Infinite-height hardness remains open.


## Hourly research review scheduled 04:30 UTC

Actual review: 2026-11-25 04:30:00 UTC. **Movement: yes. Consecutive stationary reviews: 0.**

The explicit prime-field seed construction now has a complete separately frozen statement-only reconstruction, a whole post-freeze comparison, and full root reading of both proofs. It resolves Q-FORMAL-PRIME-FIELD-SEEDS for every prime and every positive finite height. Combined with the fixed-seed reduction, every fixed exact finite-height predicate is unconditionally Mod_p P-complete. A new separate reconstruction of the entire unconditional classification, including total promise-problem membership and all size bounds, was frozen at 04:12 UTC and fully read by root before this review; its comparison against the manuscript is underway. The seed resolution, rather than subsequent checking or packaging, is the qualifying research progress.

Infinite-height hardness for a single ordinary-projective anticanonical hypersurface remains unresolved. A separately frozen product-height law and its comparison establish a promising 1-or-infinity construction for explicit self-products under the stated classical interfaces; root has not yet read the originating product proof and comparison in full. That construction is outside the single-hypersurface presentation and does not close the original question. A further quotient recipe is proposed and unverified. The finite-jet stabilizer has not been shown to preserve infinite height; an exploratory characteristic-three example indicates a failure beyond the preserved range and is being checked.

Sparse saturation, support/compression, modular bounded-Betti realization, and structured-input recovery retain their previously recorded gates. No verification, stylistic edit, source lookup, or archive production is counted by itself as new mathematical movement.

### Every still-open indexed row

| Question | Status | Current gate |
|---|---|---|
| Q-BETTI-MODULAR | current gate | Finite zeta range alone does not make succinct classification efficient |
| Q-SATURATION | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| sp:saturation-principal-arbitrary | current gate | After polynomial deflation, the deterministic residual gate lacks a bounded-total-degree cofactor or designated polynomial-degree/support cofactor. A good but undesignated row is covered by the Monte Carlo corollary. Arbitrary numerical degree or support remains outside both.; sp:sec:saturation;sp:cor:unspecified-cofactor |
| sp:saturation-ci | partly proved; residual gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| sp:sparsify-coordinate | current gate | Uniform polynomial-time construction of one sparse equation would collapse Mod_p P to P. Existence of short coordinates alone is not ruled out.; sp:cor:compression;sp:thm:reembedding |
| sp:sparse-multiples | current gate | Fixed number conditionally obstructed. Long lists are tractable with one residual bounded-total-degree cofactor, or a designated residual cofactor of polynomial degree/support; unrestricted residual lists remain open.; sp:thm:one-cofactor;sp:thm:sparse-cofactor |
| sp:full-support-boundary | current gate | Hardness persists for every fixed eta>0 under K≤d^eta; K=O(log L) is tractable; intermediate excess remains unclassified; sp:thm:support-hardness;sp:thm:support-strip |
| sp:projection-input-field | current gate | Need rational center and explicit sparse image equations with controlled construction cost; extension existence and huge elimination bounds supplied; sp:sec:compression |
| sp:different-projective-scheme | current gate | Must specify coherent group and readout; fixed total equations or ideal-generating fixed-c anticanonical lists are conditionally obstructed; other cases remain; sp:sec:compression |
| Q-67E543764A | current gate | Recover a marked affine Boolean domain, affine operands/outputs, grouping and bijection of legal words with assignments, or directly a short affine partition, from an unmarked hypersurface; No general recovery algorithm proved; recognition and output sizes are additional costs |
| Q-4FFFB1FB4E | current gate | Recover controlled matrices and affine controls or a sparse Walsh indicator from the hypersurface; Readout is polynomial once recovered; reconstruction not supplied by an abstract isomorphism |
| Q-6CE82E3666 | current gate | Extract the complete split-quadric span and base/private map from an arbitrary ideal presentation, controlling support after recovery; The marked-span theorem does not perform this extraction; arbitrary monomial support may make affine expansion exponential |
| Q-0A53ADA5A4 | current gate | Replace variable-rank split-fibre cohomology by a fixed-rank geometric realization without losing hardness; A fixed population cap in the supplied sparse model has the proved polynomial emptiness test |
| Q-CI-UNBOUNDED-EXCESS | current gate | Bounded CI excess after certified coordinate-content removal, radical-safe digit deflation and all three recognized prime-field relation rules has Las Vegas recovery; a processed linear prefix is deterministic. The Fermat family strictly extends coordinate/digit processing. The binary zero-sum family survives the preceding rules and enters the polynomial designated-cofactor degree/support class. Unbounded residual excess or cofactor complexity after these operations and general deterministic centre construction remain. The factored-prefix subclass requires designated split factors as input. |
| Q-CI-DERANDOMIZE | current gate | Only deterministic construction of a certified good centre remains after deterministic profile candidates and a fixed Newton fibre grid. A processed linear prefix dim(K_circ)_1=c-1 is solved, as is a designated factored prefix with its factors given. The remaining case lies beyond these hypotheses after certified coordinate, digit, nonzero-sum, affine and zero-sum prime-field relation processing. |
| Q-FORMAL-ALL-HEIGHTS | partly proved; infinite-height hardness remains open | For every fixed p and finite h>=1, exact height h is unconditionally Mod_p P-complete on the smooth positive-dimensional anticanonical circuit promise. The full height, finite in binary or infinity, is computable in O_p(L^2 log(L+2)) space. Infinite-height hardness and a matching complete classification remain open. The additional exact_height_unconditional_blind proof was frozen at04:12:00UTC and has no root-comparison pass recorded by this integration; accepted completeness already follows from the separately checked seed and fixed-seed transfer results. Product/infinity proposals are not adopted here. |
| Q-FORMAL-INFINITE-HARDNESS | current gate | PSPACE membership is proved. Fixed-threshold reductions alone do not imply any lower bound for the infinite-height predicate. Need a polynomial-size construction enforcing an infinite-height alternative or a reduction to the finite monomial operator respecting the geometric constraints. |

Next scheduled hourly review: 05:30 UTC. Two consecutive scheduled reviews with no resolved open row or strictly smaller main gate trigger the research stop and final verification. Next checkpoint after this one: 05:15 UTC.
