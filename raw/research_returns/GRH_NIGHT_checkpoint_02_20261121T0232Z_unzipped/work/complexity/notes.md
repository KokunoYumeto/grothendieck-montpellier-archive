# Complexity branch: working record

Updated 2026-11-21 02:24 UTC by `/root/complexity`, GPT-6 Astra Pro; effort is not exposed.

## Current state

There are 46 catalogue rows in `rows.json`, 17 source records, 116 check events, and 33 question rows. The parent assembles the paper, merged ledgers, and checkpoints. This branch does not write to the persistent destination independently.

The analytic contract is unchanged: `A_D` is the user-designated Alpöge rational Dirichlet-GRH theorem input; `M` is Masullo's universal number-field Hecke-GRH claim and every use remains conditional. The Lean archive has not been independently imported or compiled here. The independent counting premise `E` used by the attached CX_GRH run is not one of tonight's two inputs.

## Complete proofs written and read

The section contains complete, post-draft-read proofs for CX-ALG-005, CX-ALG-014–018, and CX-GEO-001–009. The check events specify exactly what was read. None is a formal verification. Parent `/root` has independently read CX-ALG-005/014 and CX-GEO-001–006, found no gap, and is recording its own cross-review events. Parent has also completed full reviews of CX-GEO-008 and CX-ALG-015–018 with no gap. Parent has also completed full reviews of CX-GEO-007/009, with no gap. Parent has also completed the full CX-ALG-021 review with no gap. CX-ALG-023–026 now have full written proofs and completed post-draft self-checks; parent review was requested at 02:22 UTC.

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
