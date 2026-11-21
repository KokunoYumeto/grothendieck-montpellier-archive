# Non-CM investigation — working notes

Date: 2026-11-21 (Europe/Berlin). Agent: /root/noncm_gate. Model: GPT-6 Astra Pro; effort not exposed.

## Settled construction

The missing ZETA_TWO ZT06 splitting exists canonically for all absolute-Hodge motives of abelian type, not merely for individual H1 factors. For the finite motivic Galois group G of an abelian motive M, its identity component is its Mumford–Tate group (Deligne–Milne 6.25 plus 6.23; Commelin Remark 4.14(1)). The derived subgroup D=[G^0,G^0] is characteristic, hence normal in G. Semisimplicity yields the canonical D-trivial isotypic part V^D and the sum of the nontrivial D-isotypic parts. Both are G-stable. Their projection is a morphism of motives over Q, so it is an absolute-Hodge projector. The first part is CM by Commelin 4.16 (generation by Artin and potentially CM abelian motives); the complement has no CM motivic subobject. No algebraicity of all Hodge projectors or Mumford–Tate conjecture is assumed.

All l-adic exterior powers of H1(A) are semisimple: Faltings makes the algebraic l-adic monodromy reductive, whose characteristic-zero rational representations are semisimple. This is not the claim that every l-adic projector is motivic. The maximal potentially abelian l-adic subspace uses [G_l^0,G_l^0]-invariants; equality with the motivic maximal-CM subspace must not be silently asserted in arbitrary exterior degree.

## Exact universal lists

For curves, normalize and compactify. Apart from explicit finite Artin terms and their Tate twist, only H1 of the Jacobian occurs. Split the Jacobian up to Q-isogeny into Q-simple factors, selecting those geometrically of CM type. Non-CM factors are exactly the remaining H1(B_i), with their multiplicities.

For an abelian g-fold, let P^r be primitive cohomology (0 <= r <= g) and N_r its maximal-CM complement. The residual product is precisely product_{r=1}^g product_{k=0}^{g-r} L^S(N_r,s-k)^{(-1)^r}; zero objects are omitted. The representation algorithm is invariants of derived Mumford–Tate Lie algebra on each primitive space, once this group is specified. This is an exact formula for arbitrary A, not an effective algorithm computing its Mumford–Tate group from equations.

For E non-CM and E^m, the full list is Sym^{a-b} H1(E)(-b), 0 <= b <= a <= m, with multiplicity binom(m,a)binom(m,b)-binom(m,a+1)binom(m,b-1). The CM terms are exactly a=b. In particular E^2 introduces Sym^2 E; discarding only H1 of CM simple factors misses this and the three Tate classes in H2.

## Sources read

- ZETA_TWO ZT04–ZT08 and CM01 in supplied paper; relevant intake table and §5.1.
- Faltings, Endlichkeitssätze ..., Invent. Math. 73 (1983), §5, Sätze 3–4, printed p.360 / PDF p.12. Primary scan retrieved via Chicago.
- Deligne–Milne, Tannakian Categories, corrected 2012 transcription, unchanged statement numbers: 6.5 (semisimple), 6.13 (exterior algebra), 6.14 (curve/Jacobian), 6.21 (weight-one), 6.23 (descent), 6.25 (fully faithful Hodge functor), 6.26–6.27 (additional abelian-type examples).
- Deligne, Hodge cycles on abelian varieties, Theorem 2.11, Proposition 2.9.
- Commelin, The Mumford–Tate conjecture for products of abelian varieties, Algebraic Geometry 6(6) (2019), Lemma 3.8; Theorem 4.13; Remark 4.14; §4.16; Lemmas 4.17–4.18.

## Scope limits to state

The phrase non-CM means no nonzero potentially-CM subobject in the absolute-Hodge category. Arbitrary minimal l-adic constituents are not automatically algebraic or absolute-Hodge motivic. Strict compatibility of the maximal-CM complement follows at good primes by quotienting the known total factor by its compatible CM factor; no general theorem about arbitrary projectors is needed. No converse from a product RH to every residual factor is asserted where meromorphic cancellation could occur.

## Archive map

Carry ZETA_TWO's documented cote 60 scans 3,5,7,9 for determinants/exterior powers and weights, and cote 34 scans 64,74 for finite-field Riemann–Weil context. Scans themselves are not supplied and no new scan reading is claimed. Framework locators carried from ZETA_TWO: SGA4 XVII §§5.1–5.3; SGA5 XV §3 no.2 equation(1); SGA6 V §2 and §7 (7.1.1); EGA IV_3 (8.8.2). These are a framework map, not invented historical locations for Faltings/Deligne's later projector theorem.

## Check completion

2026-11-21T04:16:13+01:00 — Read all six written proofs in full; tightened F-descent in NG06, made the common Tannakian group explicit for functoriality in NG01, retained bad fibres separately, and used the incomplete curve product to avoid an uncited bad-local assertion. All stated proofs passed author checking. Root independent review remains separate. Exact finite NG05 computation passed 440 degrees, m=1..20.

## Explicit non-Tate CM counterexample

2026-11-21T04:20:39+01:00 — Added NG07: A=Jac(y^3=x^5-x-1), an absolutely simple non-CM abelian fourfold over Q. Zarhin Theorem 1.1 and Examples 1.3(1), arXiv:math/0103203v2 PDF p2, give its exact geometric endomorphism ring Z[zeta3]. The determinant over K=Q(zeta3) has Hodge types (3,1),(1,3), descends as a rank-two summand over Q because the entire geometric endomorphism algebra is Galois-normalized, and belongs to primitive h4 for the canonical polarization. This provides the specific non-CM example not asserted by the general signature construction NG06. Entire written NG07 proof reread after its final edits; exact checks passed and saved in COMPUTATION_NG07.txt. Literature statement read, theorem proof not independently re-proved.

## Independent CM orbit review and curve extension

2026-11-21T04:30:03+01:00 — Completed independent full-proof review of NC03–NC04 from named NC01–NC02 inputs and primary cm/sources statements. No gap found. Detailed reconstruction in cm_orbit_review.md; both events correctly typed targeted proof check and identify the independent reviewer. No cm/findings.tex edits made. Added NG02.4 covering arbitrary finite-type curves, including nonseparated ones, by disjoint dense affine opens and a finite Artin complement; entire added deduction reread and checked. The framework paragraph uses separated-stratum compact-support classes in this case.
