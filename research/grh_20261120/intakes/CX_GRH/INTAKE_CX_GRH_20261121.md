# Intake of CX_GRH (prompt 28, "GRH and ETH in complexity: Koiran, GCT V"), 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), a coordinator and three researchers; the run's own ledger says
"inference effort not exposed by runtime". It began 20 Nov 23:00:34 UTC and delivered its final after about 1 h 03 min of
work, before any three-hour review was due.

## 0. What was read, and the scope

- **Return folder:** `research_returns\CX_GRH_final_20261121T0005Z_unzipped` (the final; checkpoint 01 is not in the
  folder and was not needed).
- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\28_GRH_and_ETH_in_complexity_Koiran_GCT_V\PROMPT.md`
  (read in full). The run's `research/PROMPT.md` is the same task.
- **Read:** README.md, QUESTIONS.tsv (39 rows), LEDGER.md, the type counts of CHECK_EVENTS.tsv (197 events: 102
  targeted proof checks, 81 used and rechecked, 8 background, 3 computation, 2 independent re-proofs, 1 refutation),
  and in `CX_GRH.tex` (3,867 lines) lines 57-1060, 1276-2255, 2383-2410, 2510-2530, 2958-3020, 3148-3292 and 3500-3520.
- **Read in full, with every step of the proof checked (21 findings):** CX-R01, R02, K01, K02, K03, K04, K05, N01, N02,
  N03, N04, N05 (transfer), N09 (transfer), N10 (transfer), N11, N13, N14, N15, E01, E04 (transfer), G06.
- **Read at the level of the statement (18 findings):** K06, K07, N06, N07, N08, N12, E02, E03, E05, E06, E07, E08, K08,
  G01, G02, G03, G04, G05; and the six unproved extensions CX-U01 to U06 (as gates).
- **Not opened:** the `work/` component files (the paper is the authoritative assembly, per README), the PDF, the visual QA
  images, the attached-source ZIP. Citations to IKRS 2008, AL86, BGL 2001, LO77, Bach 1990, Shoup 1992, Bach-Sorenson
  1996, GCT V, Forbes-Shpilka, Guo-Saxena-Sinhababu were taken as stated by the run; I checked none against its source.

## 1. Verdicts, finding by finding

Notation as in the run: **A_D** = Alpöge's GRH for Dirichlet L-functions (a theorem); **M** = Masullo's claimed GRH for
Hecke L-functions of every number field (conditional); **E** = OpenAI's fixed-width #k-SAT counter (a theorem).

### Main question: which GRH each result uses (Part I)

| id | statement (short) | uses | verdict |
|---|---|---|---|
| CX-R01 | A_D gives RH for ζ_K, K/Q abelian; M gives RH for ζ_K and every finite-order Hecke L of every K | A_D; M | **confirmed** (targeted check). Washington Thm 4.3 factorization; imprimitive factors have zeros on Re s = 0 only. |
| CX-R02 | the permutation representation of Q(2^{1/3}) is not a virtual sum of rank-one characters | none | **confirmed**: every rank-one character is 1 on the commutator c of lifts of (12),(23); trace 0 ≠ 3. |
| CX-K01 | Koiran's analytic input localizes to RH for ζ_E, E the field of Koiran's bounded solution; no Galois closure | RH(ζ_E): M | **confirmed**. LO77 Thm 1.1 applied to the Galois extension E/E is the prime-ideal theorem under RH for ζ_E; degree ≥ 2 primes cost ≤ d√x; each rational p carries ≤ d primes; with log D_E, d ≤ 2^{q(N)} and x = 2^{P(N)} the main term Li(x)/d beats every error and Koiran's Thm 5 bound for inconsistent systems; primes keep polynomial bit length. The step "every number field occurs as a solution field" (R(x)=0) is correct. |
| CX-K02 | under M: HN for circuit systems and nonzero homogeneous points in AM ⊆ Π₂P | M | **confirmed** (gate variables; Σ u_i x_i = 1). |
| CX-K03 | under A_D: the promise problem with explicitly bounded abelian witnesses is in AM | A_D | **confirmed**; it is a direct consequence of K01 plus R01. |
| CX-K04 | x³−2 has no root in any abelian extension | none | **confirmed** (non-normal cubic field cannot sit in an abelian extension). |
| CX-K05 | under M: an h.s.o.p. of linear forms for an equation-given standard-graded cone is constructible in FP^{Σ₂P}; PSPACE unconditionally | M | **confirmed**. "Good(I,L)" is the complement of K02's AM predicate, so co-AM ⊆ Σ₂P; the prefix search and the graded Krull argument (dim R/(L) ≥ d − s > 0 for s < d) are right. This sharpens GCT V Thm 3.4 ("PH") to a level. |
| CX-K06 | under M: GCT V Thms 4.10, 5.12 (strict s.s.o.p., EXPH) transfer; Thms 4.1, 5.5 (h.s.o.p.) keep their equation-access hypothesis | M | **statement level**: the premise bookkeeping is plausible; the GCT V proofs were not re-read. |
| CX-K07 | small separating systems already have an unconditional PSPACE construction (Forbes-Shpilka Thm 7.1; GSS19 Thms 1.5-1.6) | none | **statement level**; a credit correction, not a new theorem. |
| CX-N01 | Miller with Bach's cutoff is deterministic polynomial under A_D; quadratic characters suffice (Schoof 2008 Thm 2.2) | A_D | **confirmed** (transfer; Bach 1990 Thm 2 p. 372 as cited). |
| CX-N02 | specified r \| p−1: an r-th nonresidue in F_p in poly(log p) | A_D | **confirmed**. |
| CX-N03 | primitive root of F_p given the factorization of p−1 | A_D | **confirmed** (product of primary components). |
| CX-N04 | Shoup's least primitive root O((log p)^6), a candidate list only | A_D | **confirmed** at the level of the transfer (t(log t+1) = O(log p) is right). |
| CX-N05 | Shoup's F_{p²} candidate set needs ray-class Hecke characters of K = Q(√−δ) | M | **confirmed** as a scope statement (the ray class field is not abelian over Q). |
| CX-N06 | Buchmann-Shoup generating sets: ζ_Q, ζ_E, ζ of a ray class field | M | statement level. |
| CX-N07 | Bach's class-group bound 12(log\|Δ_K\|)² needs class-character Hecke L over K | M (A_D when H_K/Q is abelian) | statement level; agrees with ALPOGE_BRIDGES CC-F03/F03b. |
| CX-N08 | Lenstra's index verification certifies the S-unit index under stated hypotheses | M | statement level. |
| CX-N09 | Evdokimov (d^{log d} log q)^{O(1)} factoring transfers under M (EVD89 convention: Dirichlet characters of abelian number fields, i.e. Hecke characters over them) | M | **confirmed** as a transfer; EVD94's internal reduction was not retrieved by the run (it says so). |
| CX-N10 | BGL special-field factoring keeps its parameters s(p^k) | M | confirmed as a transfer. |
| CX-N11 | RH for ζ_Q and ζ_E, E = Q(ζ_{2n}, p^{1/n}), gives q = O(n⁴ log²(np)), q ≡ 1 (2n), gcd((q−1)/ord_q p, n) = 1 | M | **confirmed in full**: Eisenstein at primes above p, the class of σ (σ(α) = ζ_n α) is stable under conjugation (τστ⁻¹ = σ^u), Frobenius σ^u gives p^{(q−1)/n} = ζ_n^u of order n, the discriminant bound O(n² log(np)) and Bach-Sorenson Thm 5.1. |
| CX-N12 | Biasse-Erukulangara: Las Vegas class group of imaginary quadratic fields in L(d)^{3/√8+o(1)} under M | M | statement level. |
| CX-N13 | specified r \| p−1: an r-th nonresidue in any supplied F_{p^m}, poly(m log p), under A_D; r = 2, m even unconditional (BIMS17 Cor 1.3) | A_D | **confirmed in full**. r ∤ m: the constant a works (ζ^m ≠ 1). r \| m, r odd: a nonzero u with u^Q = ζu exists (ζ lies in the order-S image of v ↦ v^{Q−1}), and S = 1+Q+…+Q^{r−1} ≡ r (mod r²) for odd r, so u^{(p^m−1)/r} = ζ. r = 2, m even: iterated square roots from −1. [For r = 2 cite also GRH_NIGHT CX-ALG-018, an independent complete proof without GRH (confirmed); GRH_NIGHT CX-ALG-016 shows one BIMS17 formula needs a nonzero test, which this odd-r proof does not use. (corrected 21 Nov 2026 after the intake of GRH_NIGHT, Claude Opus 5.5 at effort high)] |
| CX-N14 | split algebra F_p^d with automorphism τ of order h, prime r \| h: a zero divisor in poly(d, log p) if (i) p ≤ d, (ii) r \| p−1 (A_D), or (iii) v_r(p^s−1) = 1 (unconditional); counterexample p = 17, r = 3 to dropping (iii) from that proof | A_D in (ii) | (i) and (ii) **confirmed in full** (in (ii): τ(z^r) = z^r, a τ-invariant r-th root y by Gao Lemma 2.6, ∏(z − ζ^j y) = 0 with no factor zero). (iii) **rests on IKRS Prop 4.6 and Lemma 4.2**, carried as background. The moved-component ideal J is right. The **counterexample is confirmed by hand**: ord₃17 = 2, v₃(288) = 2, τ(x) = ζx, x³ = (ζ,ζ,ζ), Frobenius acts as −1 = ω₂(2) mod 9, so ⟨x, ζ⟩ = ⟨x⟩ is cyclic. |
| CX-N15 | under M: complete deterministic factorization over F_q in (d^{log d} log q)^{O(1)}; the analytic input is exactly RH for ζ_Q and ζ_{Q(ζ_{2ν}, p^{1/ν})}, ν = sr or a prime ℓ \| r−1, ν ≤ d² | M | **confirmed modulo the cited algorithms** (AL86 Algorithm A; BGL Thm 2; IKRS Main Theorem, Prop 4.6, Lemma 4.2). I checked line by line the new steps: the r-th nonresidue c = u^r in B = F_Q from u^Q = ζu in F_{Q^r}; η₀ = c^{w₀} of order R = r^e; p ≡ ω(p mod r) mod R (p mod R lies in the prime-to-r torsion, on which reduction mod r is injective); the interpolation P(ζ^a) = η₀^{ω(a)} has P^{(p)} = P, so P ∈ F_p[T]; ρ_b(η) = η^{ω(b)}; noncyclicity of ⟨x, η⟩ since η of maximal order R is τ-fixed; Berlekamp subalgebra B_f ≅ F_p^t; the branch p ≤ d; the node count 2d−1. No gap found in the new parts. |

### ETH (Part I, section 4)

| id | statement | uses | verdict |
|---|---|---|---|
| CX-E01 | E refutes ETH, #ETH, fixed-width SETH and #SETH, their randomized forms, Gap-ETH, NSETH; it refutes neither OVC, 3SUM, APSP nor FPT ≠ W[1] | E | **confirmed** (h_k(n) = C_k n log log n/√log n = o(n); for SETH one ε = 1/2 serves every k). |
| CX-E02 | a lower bound falls only through a reduction to fixed-width CNF with O(u) variables | E | statement level (correct in form). |
| CX-E03 | Circuit-SAT by gate encoding has n + s variables, so E gives no saving in n alone | E | statement level (correct). |
| CX-E04 | some L ∈ E^NP has circuit size > c n √log n infinitely often | E | **confirmed as a transfer**: this is OpenAI Cor 1.4 verbatim in substance; the run says so. |
| CX-E05 | sparse permanent counting transfer | E | statement level. |
| CX-E06 | nothing here settles VP vs VNP, the permanent, or GCT V's border-hardness premises (Thms 1.7, 2.4, 5.11, 5.14) | E | statement level (a correct scope statement). |

### The geometric restatements (Part II)

| id | verdict |
|---|---|
| CX-K08, CX-E07, CX-E08, CX-G01-G05 | statement level. They are correct dictionaries (finite étale algebras and their idempotents, Kummer μ_r-torsors, Pic and S-units, K_0 and λ-operations, integral orbit models, Hilbert/Quot). None adds mathematics; E07 (a CNF count = degree of a constant finite étale scheme) is standard. |
| CX-G06 | **confirmed**: finite-monodromy sheaves are pointwise of weight 0; this gives no global zero location. |

### Unproved extensions (Part III)

CX-U01 to U06 are gates, not findings; correctly kept apart. No finding claims more than it proves.

**Counts.** 39 findings. Confirmed with every step checked: 21 (four of them, N05, N09, N10 and E04, as transfers of cited
theorems; N14 (iii) and N15 modulo the cited IKRS/BGL/AL86 algorithms). Read at the level of the statement, no fault
found: 18. Gaps: 0. Refuted: 0. The run's own refutations (K04, R02, the N14 counterexample, and the inference
refutations in QUESTIONS Q05, Q09, Q10, Q17, Q20, Q27, Q29, Q36, Q39) are all correct where I read them.

**Model naming.** The run writes "GPT-6 Astra Pro; inference effort not exposed by runtime". Under our rule it is
"GPT-6 Astra (ChatGPT Pro mode)"; its check events should be relabelled so when they enter the ledger.

## 2. What is new

- **Against the literature.**
  - *CX-K01* states exactly what Koiran's proof needs: RH for ζ_E of one bounded solution field. It does not need the
    Galois closure or Artin holomorphy. The step is standard, LO77 Theorem 1.1 applied to E/E, but I did not check whether
    Koiran's own §5 Theorem 9 (journal p. 282) already states it for the root field. It is safest to call it an exact
    reading, not a discovery.
  - *CX-K05* (FP^{Σ₂P}) pins GCT V Theorem 3.4's "PH" down to a level. This is new as a statement, and the proof is short.
  - *CX-N13* (nonresidues in every F_{p^m} for r | p−1 under A_D) is elementary and plausibly folklore. It is new as an
    explicit statement with the uniform bound.
  - *CX-N15* is the run's main contribution. It localizes Evdokimov's GRH to an explicit finite family, RH for
    ζ_{Q(ζ_{2ν}, p^{1/ν})} with ν ≤ d². That is the same as GRH for the finite-order Kummer Hecke characters over the
    cyclotomic fields Q(ζ_{2ν}). It also gives a self-contained composition through IKRS, with a new interpolation
    descent of the maximal Teichmüller unit. Evdokimov's 1989 convention ("Dirichlet characters of abelian number fields")
    was already of this kind; the explicit Kummer family and the ν ≤ d² bound are new as stated.
  - *CX-N14*: the counterexample (p = 17, r = 3) is new but small.
  - The ETH findings are consequences of OpenAI Theorem 1.1 and Corollary 1.4 and of standard logic, with no new
    mathematics. Their value is the exact scope.
- **Against tonight's other run (ALPOGE_BRIDGES checkpoint 01).** The two runs agree independently in three places:
  - Masullo's Theorem 13.3.1.2 (PDF p. 522) has no body;
  - LO77 Theorem 1.1 needs RH for the top field (CX-K01 and ALPOGE_BRIDGES CC-C01);
  - the class-group hypothesis is a Hecke hypothesis that A_D does not cover. CX-R02 shows this with x³−2 and CX-N07;
    ALPOGE_BRIDGES shows it with x³−x−1 over Q(√−23) in CC-F03, and gives the abelian-Hilbert-class-field exception in
    CC-F03b.
- **Against our own results.**
  - The bridges run of 20 Nov had Q07 as "open: Koiran uses GRH for Dedekind zetas of arbitrary number fields". CX_GRH
    makes it exact and settles it conditionally on M (K01, K02). It proves the A_D promise version (K03) and refutes the
    abelian shortcut (K04).
  - Q08 ("settled by A3/A4 with Bach") is confirmed with verified locators, and sharpened: quadratic characters suffice
    (CX-N01, after Schoof 2008 Thm 2.2).

## 3. The scope of the two proofs

- **A_D only (unconditional):** R01 (abelian part), K03, N01, N02, N03, N04, N13, N14 (ii). The prime selection in N05
  (δ) is also A_D only.
- **M (conditional on Masullo):** K01's general case, K02, K05, K06, N05 (ray-class part), N06, N07, N08, N09, N10, N11,
  N12, N15.
- **None:** R02, K04, K07, N14 (i), (iii), and the E and G findings.
- **More than both (Artin holomorphy, GL₂, automorphic):** no finding uses it. The run correctly avoids Artin holomorphy
  throughout: LO77 and Bach-Sorenson need only Dedekind zeta functions.
- **Flags:** no finding claims more than its input gives.
- **Remark for our own scope tables.** Conditionally on M, every Artin L-function has no zeros and no poles in
  0 < Re s < 1 off the central line. By Brauer's induction theorem, L(ρ, s) = ∏ L(ψ_i, s)^{n_i}, a product of
  finite-order Hecke L-functions over subfields with n_i ∈ Z, and M places every zero of every factor on the line.
  Holomorphy on the line is not given. So "Artin GRH" in the zero-location sense is conditional on M, not "beyond both".
  Prompt 35 already says this (line 38). The brief's "Artin: neither gives" holds for Artin's holomorphy conjecture only.
  For CM motives (Q02) the Hecke characters are algebraic of weight w; after the unitary twist they have infinite
  order. So the CM case needs M for all unitary Hecke characters (ZETA_TWO CM01), which is what Masullo §1.2 (PDF
  p. 12) claims; GRH for finite-order Hecke characters does not suffice. (corrected 21 Nov 2026 after the intake of
  ZETA_TWO, Claude Opus 5.5 at effort high)
- **Masullo's locators.** The run cites M by its introduction (§1.2, §1.2.3, PDF pp. 12-16) because 13.3.1.2 is empty.
  This is correct, and it should be the locator in our ledgers too.
- **Masullo's draft, located defects** (added 21 Nov 2026 after the intake of GRH_NIGHT, Claude Opus 5.5 at effort high):
  every "conditional on M" goes with the note that the draft has located gaps at §9.3.2 (Lemmas 9.3.2.4 and 9.3.2.5,
  Theorem 9.3.2.6, pp. 425-426: GRH_NIGHT MT-M01, MT-M05, MT-M02, checked on the PDF), at §11.3 (p. 495, F-SM-19,
  repaired) and at §12.3-§12.4 (the intertwiner, ALPOGE_BRIDGES), that (10.3.2.4) on p. 454 is off by one at odd s
  (TRACE_DET MAS-BOUND), and that Theorem 13.3.1.2 (p. 522) is blank.

## 4. Integration: where each checked finding goes, and the attacks it opens

Following the coordinator's note of 21 Nov, each entry says how the finding bears on an open problem, where a route
stops, and the next attack.

### 4.1 Open rows of our earlier runs

1. **bridges 20 Nov, QUESTIONS.tsv Q07** (`reports_20261120\alpoge_rh\bridges\QUESTIONS.tsv`). New state: "proved
   conditional on Masullo (CX_GRH CX-K01, CX-K02); the A_D promise version is proved (CX-K03); the abelian-witness route is
   refuted (CX-K04, x³−2)". The gate is now exact: RH for ζ_E, E the field of one bounded solution, where E need not be
   normal. Locators replacing "unverified": Koiran, J. Complexity 12 (1996), §2 Thm 2, pp. 276-277, and §5 Thm 9 and
   Cor 1, p. 282; DIMACS TR, §2 Thm 2, pp. 5-6; the 1997 erratum; LO77 Thm 1.1.
   - **Where the A_D route stops.** The obstacle is the *range* of the unconditional prime-ideal theorem. LO77 Thm 1.3 needs
     log x ≥ 10 d (log D_E)², with d and log D_E of size 2^{poly(N)}, so the primes it supplies have exponential bit
     length, and Koiran's verifier must reduce the system modulo p.
   - A_D does help: by Stark (1974) a real exceptional zero of ζ_L comes from a quadratic subfield, and A_D excludes it.
     But it leaves that range exponential.
   - **Next attacks.**
     - (a) A log-free zero-density estimate for ζ_E with exponent polynomial in log D_E, of the Weiss or Thorner-Zaman
       kind but uniform at exponential degree. Short of that, a proof that no ζ_E-only method can work at this degree.
     - (b) Use the structure of the solution set rather than one point. Lang-Weil gives many F_p-points for every p with
       a degree-one prime in the field of definition F of a geometric component, so the gate drops from the residue field
       of a point to F. The zero-dimensional case with non-abelian F stays as the core case.
     - (c) A different AM protocol that hashes over pairs (p, 𝔭) with 𝔭 of degree one in an abelian subfield of E.
       CX-K04 rules this out for x³−2 only when the subfield is required to contain the solution, not as a counting
       device.
2. **bridges Q08.** New state: "settled; quadratic Dirichlet characters suffice; Bach 1990 Thm 2 p. 372, p. 373; Miller
   1976 Thm 2 p. 301; Schoof 2008 Thm 2.2 pp. 105-106 (CX-N01; ALPOGE_BRIDGES CC-C03)".
3. **bridges Q01 and Q02 (Artin-Tate).** Conditionally on M, by the Brauer remark of §3, the gate "GRH for non-abelian
   Artin L-functions" is met in the zero-location sense, without holomorphy. The remaining gate of Q01 and Q02 is then RH
   for motives of positive weight that are not Artin-Tate. Edit the "state" column of Q01 and Q02 accordingly. This is
   for prompt 35's successor to prove in full.
4. **Bridges F1-F4.** CX_GRH does not touch steps 3 and 5 (F3, F4). CX-R01 restates F1/F2 for Dedekind zeta functions of
   abelian fields, with the same proof.

### 4.2 The reading of Grothendieck's texts

- **Cote 34, scans 64 and 74.** CX-G06 uses the same two passages as bridges Q03 and Q04 and reads them the same way.
  Remark 1.17 (34/64) is crossed out, and (2.5.5) (34/74) is the curve case. No change.
- **Cotes 2/5, 28/3 and 98/11-12, 44.** CX_GRH offers these only as places where the language occurs. I did not check
  them against the scans, and they carry no mathematical weight. No reading of Grothendieck changes. Do not enter them as
  "archive locations of complexity results" anywhere. The run itself says "locations of the language, not historic
  primality or factoring algorithms".

### 4.3 Study and companion notes

- In the bridges IMPLICATIONS.md (`reports_20261120\alpoge_rh\bridges\IMPLICATIONS.md`), in the GCT/complexity
  paragraph, add after the Koiran sentence: "CX_GRH (21 Nov) localizes Koiran's input to RH for ζ_E of one bounded
  solution field (CX-K01) and proves HN ∈ AM ⊆ Π₂P conditionally on Masullo (CX-K02). A_D gives the bounded abelian
  promise (CX-K03). The equation-given h.s.o.p. search is in FP^{Σ₂P} under M (CX-K05)."
- In the FABLE_PROGRAM_SUGGESTIONS of 20 Nov, wherever "deterministic factoring" or "Noether normalization" appears as an
  A_D consequence, correct it: deterministic factoring is conditional on M (CX-N15). Under A_D only the cases r | p−1 and
  v_r = 1 are covered (CX-N13, CX-N14). I did not open that file; the main session should search it for "factor" and
  "Noether".

### 4.4 Successor prompts and the prompts it feeds

Prompts 30-35 were moved to `SENT\` on 21 Nov at 00:04 (+01:00), so they are no longer unsent. What follows is for their
successors. Prompt 36 (CUE/GCT, built 21 Nov) is still in `1_Archive_research_by_topic\`.

- **30 (GRH_ANABELIAN, Hooley, Chebotarev, cote 149).**
  - CX-K01 shows the LO77 input in the form our rows need: Chebotarev for E/E, with no Galois closure.
  - CX-N11 is a fully checked Bach-Sorenson application in a non-abelian Kummer field, and it is the template for
    effective Galois images.
  - Its successor should cite both by id and not re-derive them.
- **33 (TRACE_DET).** The empty 13.3.1.2 is confirmed by two runs. Successors cite Masullo's §1.2.3 for M.
- **35 (ZETA_TWO).** The Brauer remark above, and CX-R01 for the abelian Dedekind case.
- **36 (CUE/GCT).** CX-K07 (Forbes-Shpilka Thm 7.1 PSPACE hitting sets, GSS19 Thms 1.5-1.6) is exactly the
  "Forbes-Shpilka Noether normalization" item of prompt 36. Add CX-K05, K06, K07 and E06 to its attached results so
  that it does not redo the scope work.

## 5. Prompt updates: what a CX_GRH successor needs

1. **The sharpened gates as the main questions.** Under A_D the run reduces the remaining number-theoretic gates to two
   families of Hecke characters. A successor should ask whether Alpöge's method proves GRH for them. His steps 2-3 use CM
   theta values on C/Z[ω], step 8 iterated theta lifts between unitary groups over a CM field, step 12 Bessel periods
   "independent of the Hecke characters", and step 15 "an integral structure glued across Hecke characters"; these are
   the ingredients to test.
   - **(i) Finite-order Hecke characters of the cyclotomic fields Q(ζ_n), Kummer characters included.** This gives
     deterministic factoring with Evdokimov's bound (CX-N15), Adleman-Lenstra field construction, and Buchmann-Shoup
     (CX-N06).
   - **(ii) Ray-class and class-group characters of imaginary quadratic fields**, i.e. dihedral Artin L-functions and
     weight-one CM forms. This gives Bach's class-group bound for imaginary quadratic fields, Shoup's F_{p²} construction
     (CX-N05) and Biasse-Erukulangara (CX-N12).
   - Koiran (arbitrary E) is not in either family and stays with M; the attacks of §4.1 go in the same prompt.
2. **The factoring gate CX-U02 as a separate item.**
   - The obstacle is exactly the construction of the maximal coefficient Teichmüller unit η ∈ D_r of order r^e, with
     ρ_b(η) = η^{ω(b)}, when r ∤ p(p−1) and r² | p^s − 1. CX-N15 constructs it from F_{p^{sr}}, and that field needs the
     Kummer auxiliary prime.
   - [Narrowed: a supplied F_{p^r} gives η unconditionally, and conversely (GRH_NIGHT CX-ALG-023, confirmed; classical
     equivalence, Lenstra 1991 Thms 5.1-5.2); under A_D, RH for ζ_{Q(p^{1/r})} is equivalent to RH for
     ζ_{Q(ζ_r, p^{1/r})} by the AGL₁(F_r) identity, and gives an explicit F_{p^r} (CX-ALG-024, confirmed). So the gate
     is RH for ζ_{Q(p^{1/r})}, one degree-r non-Galois field per encountered prime r ≤ d; the exact list of such r
     (r ∤ (p−1)m, higher valuation) is CX-ALG-025, at statement level. That RH is RH for one order-r Kummer Hecke
     character over Q(ζ_r). (corrected 21 Nov 2026 after the intake of GRH_NIGHT, Claude Opus 5.5 at effort high)]
   - Attack 1: any deterministic A_D-only construction of an r-th nonresidue in F_{p^s} for s = ord_r(p) > 1 closes it,
     by Step 1 of CX-N15 read backwards.
   - Attack 2: least-prime bounds in the Kummer field that are polynomial in n log p and need only RH for ζ of its
     abelian subfield Q(ζ_{2n}), via a large-sieve or zero-density argument over the n characters of E/F.
3. **The full Lean tree.** The run had only the two interface files. Attach the Lean archive's scan TSV, or state that it
   is not attached, so that no run needs to disclaim it.
4. **Model and effort.** Ask the run to write itself as "GPT-6 Astra (ChatGPT Pro mode)" in its CHECK_EVENTS; "effort not
   exposed" is not to be written.
5. **Archive locators.** Ask for an archive passage only where Grothendieck states or uses the mathematics, by cote and
   scan, and for none otherwise. "Companions of the language" add nothing.
6. **The ETH part is finished.** A successor should not repeat it, except for one item: whether E gives any unconditional
   arithmetic-circuit consequence through Kabanets-Impagliazzo (derandomizing PIT versus permanent lower bounds), which
   CX-E06 leaves as a scope statement.
