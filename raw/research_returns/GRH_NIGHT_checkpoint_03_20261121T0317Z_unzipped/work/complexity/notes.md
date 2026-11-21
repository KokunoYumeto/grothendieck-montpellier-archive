# Complexity branch: working record

Updated 2026-11-21 03:10 UTC by `/root/complexity`, GPT-6 Astra Pro; effort is not exposed.

## Current state

There are 54 catalogue rows in `rows.json`, 19 source records, 136 check events, and 42 question rows. The parent assembles the paper, merged ledgers, and checkpoints. This branch does not write to the persistent destination independently.

The analytic contract is unchanged: `A_D` is the user-designated Alpöge rational Dirichlet-GRH theorem input; `M` is Masullo's universal number-field Hecke-GRH claim and every use remains conditional. The Lean archive has not been independently imported or compiled here. The independent counting premise `E` used by the attached CX_GRH run is not one of tonight's two inputs.

## Complete proofs written and read

The section contains complete, post-draft-read proofs for CX-ALG-005, CX-ALG-014–018, and CX-GEO-001–009. The check events specify exactly what was read. None is a formal verification. Parent `/root` has independently read CX-ALG-005/014 and CX-GEO-001–006, found no gap, and is recording its own cross-review events. Parent has also completed full reviews of CX-GEO-008 and CX-ALG-015–018 with no gap. Parent has also completed full reviews of CX-GEO-007/009, with no gap. Parent has also completed the full CX-ALG-021 review with no gap. CX-ALG-023–026 have full written proofs and completed post-draft self-checks; parent independently read each complete proof at 02:24:49 UTC and found no gap (exact events in work/checks/root_peer_reviews.tsv, included in CP2).

The strongest new formulations are:

- Existential constructible feasibility in AM under M, with polynomial-size Boolean selector encoding; radical membership and reduced algebraic-set containment/equality in coAM.
- Orbit membership under explicit action equations in AM under M; a separate unconditional PSPACE route for explicit-coordinate polynomial GL/SL orbit closures, using APS and a fixed elementary-unipotent parameterization of the SL big cell.
- A finite Frobenius trace test with the exact Bach–Sorenson bound, and an explicit quadratic-compositum refinement excluding any prescribed finite set of primes. It recognizes permutation representations and zeta functions, not finite covers themselves.
- A seven-point transitive GL3(F2) G-set counterexample to trace-to-cover-isomorphism reconstruction, with a full character and stabilizer proof.
- Bounded Frobenius classes detect every proper subgroup of a specified finite Galois group; arbitrary representatives generate it, and a sublist of at most floor(log2|G|) suffices.
- The literal fixed-generator resolvent formula in BIMS17 Theorem 3.1 fails over F7[X]/(X³−2), ζ3=4. A nonzero projection is recovered by scanning a power basis. This is an explicit correction of the formula, not a refutation of the paper's construction conclusions.

CX-ALG-015 is the explicit-input-length form of Miller's classical supplied-exponent factoring reduction, not a new claim of general integer factorization in polynomial time. CX-ALG-018 is an independent re-proof of an inherited theorem, not a new discovery of the even-degree quadratic case. The original CX_GRH CX-N13 retains priority for the supplied-extension nonresidue transfer; it now has a fresh complete proof here after the source audit.

## Source audit that changed the proof state

The full BIMS17 Theorem 3.1 statement and proof were read, and the source PDF page 3 was rendered and inspected. Its fixed choice `L = sum ζ^i α^(q^(ki))` can be zero, so the step dividing by L is unjustified as written. The counterexample uses q=7, r=d=3, f=X³−2, ζ=4: α^7=4α, α^49=2α, and L=0 whereas the claimed final power is 2.

For odd r, or r=2 with 4|(q−1), the corrected linearized map is nonzero because its polynomial degree is less than the field cardinality. It therefore has a nonzero value on a power basis. The exponent congruence and norm calculation then work. This closes that exact gate without enlarging the runtime or analytic input.

The p≡3 mod4, m≡2 mod4 quadratic branch is handled independently in Fp². Trace-zero linear algebra gives an explicit square root i of −1; repeated square roots of norm-one a+bi are obtained from exactly one of (a+1)/2 and (a−1)/2 being a square in Fp. Each step doubles the 2-power order; norm −1 ends the loop and certifies a nonsquare. The odd-degree lift to Fp^m preserves it. If p≡1 mod4 or 4|m, a single anti-invariant under Frobenius^(m/2) already suffices. `/root/number_theory` independently confirmed the construction, with an alternative quadratic-tower formulation.

## Inherited results and limits

The supplied attachment contains prior intakes, questions, implications and ledgers, but not the complete prior `CX_GRH.tex`. Elaborate prior compositions, especially CX-N15 finite-field factoring and CX-K05 normalization search, are carried with exact old IDs and modest check status. They are not claimed as freshly audited complete absent proofs.

The inherited general finite-field polynomial factorization result is quasipolynomial, `(d^(log d) log q)^O(1)`, under the precise Dedekind-zeta family of CX-N15, supplied by M. That older sufficient input remains valid. The new complete composition CX-ALG-023–026 shrinks the analytic family to pure prime-degree fields and adds the unconditional r|m branch for a supplied F_{p^m}. The residual A_D-only coefficient-field gate is now p>d, r∤p(p−1)m, and v_r(p^(ord_r(p))−1)>1. It is equivalent to constructing F_{p^r}; it is still unresolved in general.

The class-group bound supplies a small factor base, not a relation-search runtime. The complete imaginary-quadratic algorithm CX-N12 is now present as CX-ALG-019 with fresh primary-statement and certification checks; the broader class-group relation/saturation gate remains algorithm specific. Hilbert class fields of abelian base fields need not be abelian over Q.

Koiran's exact input is the zeta function of a bounded algebraic solution field, which need not be normal. No Galois closure or Artin holomorphy is inserted. The bounded abelian-witness promise transfers under A_D, while x³−2 refutes the proposed universal abelian-witness replacement. The 1997 erratum was read in full; the main result survives with its prime-count correction.

Historical GCT V equation-access conditions are conditions of that cited route. They are not a proof that all possible algorithms need equations. Earlier unconditional PSPACE separating-parameter constructions receive their original credit. No general PIT derandomization, BPP=P, polynomial-time general integer factoring, or VP≠VNP is claimed.

## Literature access and precise locators

The source registry preserves URLs and web retrieval references. Author-hosted Koiran PostScript and erratum were downloaded and converted; the main theorem is on printed p12/PDF13, not the initially guessed later page. Shoup's font encoding was unreliable, so Theorem 3 was read from a rendered image: O(r^4(log r+1)^4 log²p), r=ω(p−1).

Bach 1990's original publisher PDF remains inaccessible in this session (403). The exact prior Theorem 2–4 locators are carried, not falsely marked newly read. Bach–Sorenson 1996 is available as a primary author-uploaded PDF: §2 p1720 specifies the zeta premise and Theorem 5.1 p1729 gives `(4 logΔ+2.5n+5)^2`. Its stated theorem does not itself exclude an arbitrary extra set S; CX-GEO-004 proves the extension trick needed for that refinement.

The GSS journal PDF was recovered at `theoryofcomputing.org` after a failed alternate host. APS is Theorem 1.3 p5; the image-closure characterization is Lemma 4.1/Theorem 4.2 pp15–16; the exact separating-e.s.o.p. statements are Theorems 1.5–1.6 p6. Miller's original Lemma 5 and Theorem 3 p310 were visually checked; its supplied λ′ multiple and bit-growth hypotheses are explicit.

All cote/scan companions in this section are inherited crosswalk locators unless expressly stated otherwise. No original Grothendieck archive scan was freshly inspected by this branch. SGA/EGA locators serve as geometric frameworks, not as claims that those texts contain the modern complexity bounds.

## Peer review performed for the parent

MT-ART01 was read in full and matched to Khare–Wintenberger Corollary 10.2(ii), author PDF p21: finite-image irreducible odd two-dimensional complex representations are modular of weight one. The independent holomorphy theorem plus M's Brauer divisor support gives GRH, including projective A5 image, without pretending to prove general Artin holomorphy.

MT-ART02 was read in full: the central convolution spectrum is exactly nχ/χ(1), with the stated normalization; cyclic restrictions recover nonnegative Hecke orders, and Θ(1)=ord ζ_L. The whole strengthened MT-ART04 A5 example was independently checked as written. It passes every induced-linear positivity test while retaining a negative irreducible coefficient. It is expressly an abstract character counterexample, not a claimed realization as actual Artin zero orders.

## Next useful steps

JMV mixing is CX-ALG-020, the A_D-only genus-quotient refinement with explicit generator bound is CX-ALG-021, and the ordinary isogeny graph/solver-transfer result is CX-ALG-022. Their exact-ID events are recorded. The next useful step is parent cross-review of CX-ALG-023–026, then further movement on its reduced A_D-only gate or a comparably concrete GCT promise. Add exact proof-check events for subsequent edits rather than rewriting old dates. Preserve the distinction between a smaller sufficient input and a proof of unrestricted derandomization.

## Further peer review — 2026-11-21T02:10:01+00:00

Fully read the five proofs in `work/root/artin_automorphic_transfer.tex`: MT-ART07/08 and MT-S501/502/503. All pass at their stated scope. The finite-exception lemma uses the Artin functional equation, requires finite local exceptions rather than density-one agreement, and needs the self-dual hypothesis or a separately controlled dual. Calegari primary §1/PDF2, Theorems1.1/1.2 PDF2–3 and5.1 PDF15 were freshly checked. The publisher leaves H undefined in1.2; the parent supplies the v1 definition H=EF, which this branch did not freshly retrieve. Prasad–Yogananda §3.3 PDF8–9 supplies the exact gamma/functional-equation convention.


## Finite-field gate movement — 2026-11-21 02:24 UTC

CX-ALG-023 gives a full rewritten proof of the classical Lenstra equivalence between a supplied prime-degree field F_{p^r} and a maximal Teichmüller unit in D_r=F_p[Z]/Phi_r. A normal basis makes the weighted resolvent nonzero in every coefficient component. The Teichmüller product projection produces y of order rR, whose rth power descends and has order R. The converse is a Kummer extension followed by invariants; a free action on geometric points proves the invariant field has degree r, including when p divides r−1. This is classical mathematics with a new application here: r|m in a supplied F_{p^m} removes the entire higher-valuation branch for that r.

CX-ALG-024 replaces a Galois splitting-field zeta input by the pure degree-r field F_r=Q(p^(1/r)). For E_r=Q(zeta_r,p^(1/r)) and K_r=Q(zeta_r), the exact identity is zeta_E=zeta_K(zeta_F/zeta_Q)^(r−1). It follows from reg_G=(r−1)(Ind_H^G 1−1)+Ind_N^G 1 in AGL_1(F_r). Under A_D the two remaining abelian factors have no off-line critical-strip zeros, so RH for F_r is equivalent to RH for E_r. The explicit field-discriminant bound is r^[r(2r−3)] p^[(r−1)^2], giving a suitable inertness prime q at most [4r(2r−3)log r+4(r−1)^2log p+2.5r(r−1)+5]^2. Adleman–Lenstra Algorithm A constructs F_{p^r} from that prime, with no further radical oracle. The number-theory agent independently confirmed the character identity; no composite-n Hooley input is silently removed.

CX-ALG-025 writes the entire factoring composition using the prime-Frobenius fixed algebra B=F_p^t. The IKRS automorphism theorem is applied over F_p, independent of m. Four branches supply the coefficient unit: r|m; r|p−1 under A_D; valuation one unconditionally; or the one pure degree-r zeta input. A maximal-order coefficient unit cannot generate a cyclic group together with the moving resolvent element, so IKRS noncyclicity produces a proper idempotent and hence a polynomial gcd factor. Runtime stays quasipolynomial. If every prime r≤d divides m or has valuation one, this composition is unconditional. Small characteristic p≤d is separately unconditional polynomial time.

CX-ALG-026 transfers the same input to exact field construction using Lenstra Theorem9.1. Only prime divisors r of n not dividing m need initial degree-r irreducibles; characteristic-p Artin–Schreier and valuation-one branches need no analytic hypothesis. An output of degree n necessarily charges n to the input/output-size convention.

Exact diagnostic examples for the new coefficient construction were computed earlier in this run, with alpha=1+X: p17/r3/R9 in F17[X]/(X³+X+3) gives eta=6+15zeta; p107/r3/R27 in F107[X]/(X³+X+1) gives eta=17+57zeta; p7/r5/R25 in F7[X]/(X⁵+X+3) gives eta=4+6zeta+zeta³. Resolvent, full-order, descent and equivariance identities were checked exactly. These are diagnostics, not a substitute for the proofs, and the diagnostic choice of irreducible input polynomials is not an asserted construction algorithm.

Source checks: Lenstra1991 Theorems3.1,5.1/5.2,7.1,9.1 and Lemma9.2 were fully read, with pp338–339 rendered. Adleman–Lenstra1986 Algorithm A and its complete pp350–352 correctness argument were read. IKRS2011 Lemmas2.3/4.2 and Proposition4.6 were fully read; Theorem5.8's exact interface and runtime were checked without claiming a full audit of all its upstream proofs. All four new written proofs were read post-draft and logged at 02:23:43 UTC.


## Cocharacter/closure gate movement — 2026-11-21 02:34 UTC

CX-GEO-010 and CX-GEO-011 were written and fully read after drafting; exact-ID events are dated 02:33:34 UTC, after the CP2 cutoff. The input is explicitly a connected split reductive group over Q, affine group equations with any necessary inverse coordinates, polynomial action circuits over Q, rational coordinate vectors, and the entire binary torus-weight list in a supplied full cocharacter lattice. All these descriptions are charged to input length. No checking of those structural promises is hidden in the algorithm.

For N coordinate weights with entries bounded by H, a complete sign pattern has an integer cocharacter with coordinates bounded by N!H^N. The proof uses a feasible nonnegative linear system, a minimal support of independent columns, and Cramer's rule. This is a bit-length bound, not a polynomial bound on exponent values. Boolean bits represent signed cocharacters and bounded positive slack integers; selector equations enforce exact signs and exact coordinate limits over C. Therefore one-cocharacter reachability has one polynomial-size HN encoding even with the target vector left unknown.

Every reductive orbit closure has a unique closed orbit accessible by one cocharacter. Two closures intersect precisely when both have one-cocharacter limits in a shared orbit. Two copies of the encoding with a shared unknown target give a direct HN reduction, hence AM under M and coAM for disjointness. If a specified target orbit is closed, membership in the source closure has the same reduction. Nullcone membership is included because zero has a closed orbit. Arbitrary-target closure membership is not concluded: one-cocharacter accessibility to every point is not automatic.

This closes the unary Laurent-precision gate for these explicitly weighted questions. It does not construct invariant separators or h.s.o.p.s, prove any multiplicity inequality, or justify expanding exponentially large GCT coordinate spaces from a succinct point circuit. The exact analytical input is still the bounded number-field solution witness for the new HN system; A_D alone needs its own abelian-witness promise. Neither rational points nor integer cocharacters make the group-element witness field abelian.

Primary source: Bate–Herpel–Martin–Röhrle arXiv1411.7849v5 introduction p1 and Theorem4.3 pp12–13, whose complete proof was read. The paper identifies Kempf1978 Theorem1.4 as the classical input; the old original proof was not retrieved here. GCT V Theorem9.8 p68 and subsequent Remark3 p69 were read to retain the distinction from its invariant-search, explicit-quotient and fixed-rank results. No first-priority claim is made for the complexity formulation.

## Further gate movement and peer review, 02:48 UTC

CX-GEO-010/011 now give full polynomial-size HN reductions for explicit-coordinate one-cocharacter reachability, closed-target orbit membership, null-cone membership and intersection of two orbit closures. Binary exponents are bounded by the proved sign-pattern lemma rather than expanded in unary. Parent independently read both complete proofs and found no gap.

CX-GEO-012 extends the earlier unary-degree Laurent-arc promise to polynomially many terms at every intermediate circuit gate, with arbitrary original exponents. The proof preserves all exponent equalities and signs while fixing the complex coefficients, and then encodes coefficient cancellation without interpolation or a hidden order predicate. CX-GEO-013 forces val(X)≥2^s in an O(s)-size circuit even though every gate has width one; thus a universal polynomial unary-precision shortcut is false. Number theory independently read both complete proofs and the antecedent sign-pattern lemma, and found no gap. Parent final assembly records the external review events.

I independently read NT-C06/07 in full and found no gap. The two exact-ID peer events are in events.tsv. GM2019 Theorem1.1/Corollary1.2 were freshly checked on original images at authorpp2–3 (fresh web ref turn752158989view0; URL https://sites.unimi.it/molteni/research/papers-pdf/44-molteni-An_explicit_Chebotarev_density_theorem_under_GRH.pdf). Neukirch’s complete supplied VII11.7–11.9 proof was read on printed533–534/PDF541–542, with degree-one conductor identification11.10 on printed535/PDF543 (URL https://www.math.toronto.edu/~ila/Neukirch_Algebraic_number_theory.pdf; primary record S-NT-NEUKIRCH). Earlier local-conductor and standard representation-theory inputs are cited, not newly re-proved. The exact ray-class correction removes only modulus primes which remain unramified in the ray field.

## Recent algebraic input isolated at 03:00 UTC

CX-ALG-027/028 are complete transfer proofs using an explicitly additional recent-manuscript input PF26 (OpenAI2026, Theorem1.2 and Proposition8.1 with uniform implementation in §§2–10). They do not silently adopt the companion analytic theorem. I read every invoked algebraic proof paragraph in §§2–10; root separately read all of §6 and Lemma2.2, while geometry separately read all of §4. No gap was found in those readings. These are reading checks, not formal certification or an implementation.

Under M+PF26 the finite-field factoring bound becomes polynomial. The exact auxiliary-prime bound in027 comes from BS and explicit discriminant bounds for Q(ζ12r,p^(1/r)); its prime is O(B^4), including r2. Row028 instead uses the directly exposed primary-table odd splitter and our smaller pure-prime-degree ζ family. It retains the supplied r|m branch and valuation-one branch; PF26 alone suffices if every table prime is in one of those two branches. The existing CX-ALG-025 quasipolynomial result remains independently available without PF26. The prime-field and integer-factorization problems remain separate.

Rows/sources were extended directly in their canonical JSON files at this point. The earlier helper build_domain.py predates027/028; do not rerun it without first preserving the current canonical JSON additions. Parent continues to own assembly/persistence.

## Further exact promise diagnostics

CX-GEO-014 proves HN-completeness for the exact supplied-circuit sparse-arc problem even at width one and quadratic output degree. The guard1+X_i is on the path to outputY_i(1+X_i), and forces X_i constant under the width-one condition. This is not a lower bound against polynomial-time HN.

CX-GEO-015 gives the explicit SL cocharacter showing a form with proper variable support is unstable. Hence the padded permanent for m>n fails the closed-target promise of011. Separately, every affine GL orbit closure of a positive-degree homogeneous form contains0, so the corresponding intersection question is always positive. No projective statement is inferred. Both proofs have complete post-draft reading events; parent review requested next. Parent has now independently read both full CX-ALG-027/028 transfers and found no gap; PF26 remains explicitly additional.

## Integral Lefschetz peer review, 03:10 UTC

Read the complete AG-LEFSCH-LATTICE/SPLIT/INDEX/DEFECT statements and proofs, including the C8 sharpness example. All checks passed. INDEX uses only integrality of the normalized raising map and a Weyl isomorphism between the two weight lattices; no global isotypic splitting is needed for its determinant. DEFECT isolates Smith ambiguity to common-divisor primes. The C8 lattice satisfies precisely the weaker local conditions, and its explicit matrix verifies that the product annihilator cannot generally be replaced by the lcm. Four exact-ID peer events are recorded in events.tsv.
