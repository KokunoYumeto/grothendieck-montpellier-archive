# Final N15 integration review

## Outcome

The requested broad finite-field factorization transfer is now complete at its stated quasipolynomial degree bound, conditional on M. CX-N15 supplies a full accessible composition; the original EVD94 proof's retrieval status is a historical limitation, not a missing step in that composition. An unrestricted replacement of the sufficient cyclotomic–Kummer zeta hypotheses by A_D remains an unproved extension, not an unfinished part of the established M-transfer.

Root's revised `work/paper_scope.tex`, paragraphs CX-U02 and CX-U03, now state these distinctions correctly. I read the revised text and found no further correction necessary. The updated N15 paragraph in `work/root_geometry.tex` also correctly gives the Frobenius-fixed component algebra, inherited idempotents, and retained conditional complexity bound. The latest assembly includes N15 and extends the Part II crosswalk through N15.

No shared summary file was edited by this reviewer. The only authorized direct change was the E08 source-locator insertion described below.

## Exact remaining edits for `deliverables/IMPLICATIONS.md`

### 1. Replace the general finite-field factoring table row

Replace the row beginning `| General finite-field factoring |` with:

```markdown
| General finite-field factoring | CX-N15 gives a complete independent deterministic factorization proof under M, through explicit cyclotomic–Kummer Dedekind-zeta hypotheses and the AL86/BGL/IKRS algorithms. | Time remains (d^{log d} log q)^{O(1)}. The unrestricted A_D-only replacement is unproved; no general polynomial-time degree bound is asserted. |
```

This removes the stale description of the broad conclusion as depending on the historical Hecke/radical route and its opaque later radical calls.

### 2. Insert the following after the CX-N11 auxiliary-prime paragraph

```markdown
CX-N15 completes the general finite-field factorization transfer through a separate accessible proof. For a degree-d input over Fq, q=p^m, the small-characteristic branch p≤d is handled unconditionally. In the other branch, a sufficient analytic family is RH for ζ_Q and ζ_{E_ν}, where E_ν=Q(ζ_(2ν),p^(1/ν)), ν=sr with s=ord_r(p), or ν is one of the auxiliary primes ℓ dividing r−1 required by BGL. Every used ν is at most d² and is coprime to p. These are sufficient hypotheses, not a claim of necessity.

The proof constructs F_(p^(sr)), takes its Frobenius-fixed F_(p^s) subfield, and constructs a maximal r-primary unit by a Frobenius eigenvector. Equivariant interpolation places that unit in the cyclotomic coefficient algebra required for IKRS descent. For the original polynomial, the algebra fixed by p-power Frobenius is a split Fp-algebra indexing its irreducible factors. Its idempotents yield those factors, with the same quasipolynomial bound. No general factorization or historical radical oracle is called in this construction.

The original full EVD94 proof was not retrieved. That historical source limitation does not leave a proof gap in CX-N15, which uses the accessible AL86 Theorem 1 and Algorithm A, BGL Theorem 2, and the IKRS Main Theorem, Lemma 4.2 and Proposition 4.6. The main conditional transfer is established; extending it to A_D alone remains a separate question. The rank-one and higher-valuation counterexamples refute specified shortcuts, not the possibility of a different A_D-only algorithm.
```

The final sentence refers to CX-R02 and the added p=17, r=3 example in CX-N14. It keeps the logical limit explicit.

### 3. Extend the geometric summary's finding range

In the Section 4 dictionary row currently beginning `CX-N01–N06, CX-N09–N14`, replace the second range by `CX-N09–N15`.

The existing statement that factorization computes primitive idempotents remains correct; N15 now constructs the needed component projectors under its explicit sufficient zeta family. The full Part II N15 paragraph already supplies the separate mathematical dictionary.

### 4. Optional short source-locator addition

After the existing paragraph listing published locators, append:

```markdown
The independent factoring composition uses Adleman–Lenstra (1986), Theorem 1 p.350, Algorithm A pp.350–351 and Lemma 6 p.352; BGL (2001), Theorem 2 p.7; Lenstra (1991), the explicit-data convention p.329 and subfield construction p.332; and IKRS (2008), Main Theorem p.3, Lemma 4.2 p.14 and Proposition 4.6 pp.16–17.
```

These are precisely the statements/interfaces used by N15, rather than inferred theorem numbers for an unavailable EVD94 proof.

## Per-ID E01–E08 Part II audit

**Coverage passes for all eight IDs.** E01–E06 each have a distinct row in `work/eth_geometry.tex`, under “Geometric restatements of CX-E01–CX-E06.” E07 and E08 each have their own Part II subsection and complete proof. The common Part II source crosswalk supplies the historical dictionary locators; the Part I results and bibliography supply the exact complexity premises. The new transfers and CRT/gate identifications are proved in the report, not misattributed as old SGA complexity theorems.

| ID | Separate Part II dictionary | Exact primary premise or modern locator | Historical geometric locator already present |
|---|---|---|---|
| E01 | Individual E01 row: nonemptiness and finite étale degree; E07 proves the component decomposition. | Supplied OpenAI Theorem 1.1 (`thm:main`) and §§1.1.1–1.1.3. | SGA 1, Exp. V §4 Theorem 1 and §7; SGA 6, Exp. VI 3.2–3.3 for the rank/Grothendieck language. |
| E02 | Individual E02 row: emptiness, rank, witness bijections; E07 distinguishes a count equality from a specified component isomorphism. | Supplied Theorem 1.1 and Corollary 1.3; the parameter-preserving transfer and clique encoding are the report's complete new proofs. | SGA 1, Exp. V §7, with the explicit CRT proof in E07. |
| E03 | Individual E03 row: gate projection is an actual scheme isomorphism; E07 constructs the inverse. | Supplied Theorem 1.1, fixed density k=3,D=5; Williams author version, Theorem 1.1 p.2 for the separate all-polynomial-size Circuit-SAT premise. | SGA 1, Exp. V §7; the gate isomorphism itself is proved in E07. |
| E04 | Individual E04 row: the degree algorithm retains a Boolean-language circuit conclusion and does not produce a coordinate-ring representation. | Supplied Corollary 1.4, Appendix C.1 / `quantitative-circuits.tex`; Williams Theorems 2.1 p.7 and 6.1 pp.20–21; JMV Theorem 1 p.2. | SGA 6, Exp. VI 3.2–3.3 for the retained degree/rank interpretation; G05 explicitly proves that rank does not determine representation data. |
| E05 | Individual E05 row: the perfect-matching scheme has permanent as its degree and O(r+e) Boolean coordinates. | Supplied Theorem 1.1 and Corollary 1.3; the sharper fixed-density matching encoding is proved in E05. | SGA 1, Exp. V §7; SGA 6, Exp. VI 3.2–3.3; E07 proves the scheme/rank equality directly. |
| E06 | Individual E06 row: numerical rank versus symbolic polynomial and graded equivariant coordinate algebra. | Valiant Theorem 2 p.254; Bürgisser Definitions 2.9/2.25, Theorems 2.20/2.29/7.3; attached GCT V Theorems 1.7,2.4,5.11,5.14 with source-label map. | SGA 3, Exp. I 4.6.3.1 and 4.7.1–4.7.2; FGA Exp.221 §3 Theorems 3.1–3.2; SGA 6 V2.4, as developed in G04–G05. |
| E07 | Dedicated subsection: finite étale Z-scheme, degree/rank, K0, exterior powers, reduced γ-class and geometric finite-field cohomology. | Self-contained CRT and componentwise proofs; supplied Theorem 1.1 is the computational premise. | SGA 6 V3.10 and VI3.2–3.3; SGA 5 XV §3 no.1 Proposition 1 and no.2; precise geometric cohomology is also stated in G06. |
| E08 | Dedicated subsection: graded equivariant quotient and multiplicity inequality; exact proof identifies the extra data missing from a rank count. | **Direct locator now inserted:** Bürgisser §7.4, equation (7.6) p.38 and equation (7.9) p.39. These explicitly state the quotient/multiplicity argument. | SGA 3 I4.7.1–4.7.2; FGA221 §3 Theorem 3.2 and Proposition 3.8; SGA 6 V2.4; Macdonald I§3(3.4), p.41 for the Schur-class operation in G05. |

### E08 source-locator edit actually made

In `work/eth_geometry.tex`, the sentence now reads:

```latex
A reversed inequality would obstruct the containment
\cite[\S7.4, (7.6), p.~38, and (7.9), p.~39]{Burgisser2024}.
```

No proof statement changed. The existing `Burgisser2024` bibliography key already names the correct v1 edition, so no new bibliography item is required.

Updated `eth_geometry.tex` SHA-256:

```text
72e73b127dad2189370fc2516c261a7fe4459d75768fc10000e4a995ee8b1f46
```

The locator was directly checked in the author PDF at https://arxiv.org/pdf/2406.06217, source ref `turn318824175view0` (also `turn955108749view2`). Equation (7.6) and the reductive decomposition are on printed p.38; the orbit-closure quotient and equation (7.9) are on printed p.39.

## Check scope

This was a semantic integration and per-ID source-coverage review, not another generic test run. I read the amended U02/U03 text, N15's new Part II paragraph, every individual E dictionary entry and E07–E08 proof, and the exact Bürgisser §7.4 source paragraphs. The earlier full proof reviews of E01–E08 and N15 remain recorded separately. Historical SGA/FGA locators were checked for presence and linkage here; this review does not claim a second fresh inspection of every archival scan or every underlying SGA proof.

Model: GPT-6 Astra Pro; inherited reasoning effort not exposed. No formal verification is claimed.

Review completed 2026-11-21 00:59:28 Europe/Berlin (2026-11-20 23:59:28 UTC).
