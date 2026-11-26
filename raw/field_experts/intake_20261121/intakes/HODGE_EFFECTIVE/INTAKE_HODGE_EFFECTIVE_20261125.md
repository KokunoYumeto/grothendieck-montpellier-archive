# Intake of HODGE_EFFECTIVE (prompt 70d), checkpoint 08

By Claude Opus 5.5 at effort high (agent acc1e1c0, the HODGE cluster reader of the 24 Nov pile), for the main session
329fb1e6 (Claude Opus 5.5 at effort max), 25 Nov 2026. It follows the brief
`agent_notes\INTAKE_NEW_RETURNS_BRIEF_20261125.md`.

- **Run:** GPT-6 Astra (ChatGPT Pro mode); the interface does not expose its effort. Sent about 22:33 UTC on 24 Nov; it
  started 22:47.
- **Return:** `research_returns\HODGE_EFFECTIVE_checkpoint_08_20261125T0447Z_unzipped\` (04:47 UTC). Three papers:
  - **Paper A v2:** `workbench\work\UNFILED-A\v2\paper\main.tex`, 77 pp.;
  - **Paper B v2:** the same path under `UNFILED-B`;
  - **Paper C v1:** the same path under `UNFILED-C\v1`, 47 pp., "An effective one-prime criterion for Weil classes over
    Q(i) and Q(ω)".
- **Run state:** still active. Its four movement reviews (01:47–04:47) all record movement.
- **Check events:** `INTAKE_HODGE_EFFECTIVE_20261125_CHECK_EVENTS.tsv`. Work file: `agent_notes\acc1e1c0_NOTES.md`.

**Prior checks.** `who_checked.py --source HODGE_EFFECTIVE` lists 336 ids, all checked only by in-run readers (GPT-6 Astra,
same model). No Claude check existed before this one. The pile (`reports_20261124\INTAKE_PILE_20261124\INDEX.md`) knew
the run only as a prompt: H2 (Paper A), NT-2 (our deduction of the Galois-orbit criterion without André–Oort, through
Jaswal), and the prompt update `PROMPT_UPDATES\70d_HODGE_EFFECTIVE_UPDATE.md`.

## 1. Verdicts

| Id | What it claims | Verdict |
|---|---|---|
| **Q35** (C Prop. no-abelian-weyl, with Lemma balanced-splitting-field) | A relative-Weyl special point of the signature-(n,n) unitary family (n ≥ 2) has a nonabelian torus splitting field, of degree 2·m! (48 for fourfolds, 80,640 for eightfolds); the full and adjoint tori have the same splitting field | **targeted proof check, no fault** (degrees recomputed) |
| **Q49** (C Prop. doubling-nonflat, Ex. prime five) | On A = B × B with I(x,y) = (−y,x), the coordinate cycle 0 × B is a detector of degree n!, but the relative Hilbert scheme over the unitary moduli is not flat at it (tangent n + n(n+1)/2, fibre n, base n²). Explicitly at p = 5 for B = T⁴, T: y² = x³ − x (degree 24; 14/4/16) | **targeted proof check, no fault**; the example recomputed |
| **Q36/Q39** (C Thm. arithmetic, Lemma certificate, Prop. exact-exceptional, Cor. escape) | One good prime outside an explicitly computable set (the norm of b·a_D, from a Gröbner/torsion certificate of the cycle parameter scheme) suffices to lift a degree-≤ D cycle equality from F̄_v to characteristic 0. The vertical components are computable by primary decomposition. If b₀ = ∞, the degrees b_v exceed D once N(v) > \|N(b a_D)\| | **targeted proof check, no fault** |
| **A.CYCLE.TARGET** (A v2 Prop. cyclic-four-degree) | On J(C), C: y² = z∏(z² − a_r²) (genus 4, odd principal Gaussian), four effective surfaces Z_j of θ-degree 48, with w = [Z₀] − 2θ² ∈ W, ∫w² = 32; so δ_W ≤ 48 on that locus (was 192) | **degree part rederived** (sum 192 by u*θ = 7x − Δ/2; cross-checked by Poincaré's formula); ∫w² = 32 and the nonvanishing carried as background |
| **Q41** (A v2: G₃₄ dominance written into Paper A) | Paper A now proves the G₃₄ dominance from finite data plus published inputs and "invokes no theorem or geometric criterion from Severn's manuscript" (main.tex 2239–2244, 2694–2699) | carried as background: it is HODGE_DIVISION's D-G34, which I checked by targeted proof check on 24 Nov. The insertion was not diffed |
| **Q33, Q34, Q37, Q45, Q48** with C Thms explicit-theta-chow-bound, forcing, sharper-forcing | An explicit integer H_g(D) for the degree of the detector locus (principal level 3, g = 4, 8); explicit Jaswal constants; a polynomial discriminant threshold \|disc L_x\| > ℬ(H_D)^{1/μ}, sharpened by CM heights to H_D^{768+o(1)} (m = 4) and H_D^{10,569,646,080+o(1)} (m = 8) | carried as background. They rest on Jaswal's unrefereed AI-produced effective André–Oort (Hexagon 2611.00339) and on the Cureton–Thorner or Hu half-planes, named in every statement |
| **Paper B: Q40, Q44, Q46, Q47, Q50–Q57;** **C: Q43** | Exclusions of construction routes to the Gaussian eightfold detector: finite-cover coefficients of rank ≥ 78 (imprimitive ≥ 156, ordered primitive ≥ 100); invariant Ext² > 56 on abelian supports and on graph networks; rank-one secants fail. Also analytic realization of compatible formal perfect towers (Q55, Q56), and ordinary relative-Weyl reductions being simple (Q43) | register rows only |
| **Refuted by me** | none | |

**The main question stays open.** No detector is constructed for split Gaussian eightfolds (Q06), and no Hodge-conjecture
case is new. All the run's new positive results are conditional criteria, or exclusions of routes.

## 2. Which results meet our algebraic geometry, and which are Hodge as a goal in itself

By the user's priority of 25 Nov: Hodge only where it meets our AG work.

**Meets our AG work (built on our results or on Grothendieck's frameworks):**
1. **Q41: our G₃₄ eightfold proof is now in the paper of record.**
   - This settles the "Q28 against H19" problem of the pile (`HODGE.md`, HODGE_FINISH section 7): Paper A no longer takes
     the dominance from Severn.
   - What remains is wording: line 226 still says "Severn's exceptional-divisor correction … carry this proof", although
     the repair is now written out.
   - H19's "from published inputs" now agrees with the paper of record.
2. **Q36/Q39: arithmetic flatness of Hilbert schemes, made computable** (FGA 221, SGA 6 XIII 6.11, EGA IV 2.4.6 and 11.1.1).
   - For a fixed variety over O_L[1/b] the "finite exceptional set" becomes an explicit integer a_D from the chart ideals.
   - Cor. escape gives a stopping threshold for the ghost question (GHOSTS/Q05): above N(b a_D), a class with b₀ = ∞ has
     b_v > D.
   - This is schemes over Z in Grothendieck's sense, and it is the one usable output of the prompt's "rate for ghosts"
     item. It is a rate in N(v) for a fixed D, not a growth rate of b_v.
3. **Q49: a clean negative on relative flatness.**
   - The obvious small detectors (coordinate subvarieties of B × B) are nonflat over the unitary moduli, at every good
     characteristic, including ordinary split primes.
   - Consequence: the one-prime route through Thm. flat needs a detector that is not a product construction.
4. **Q35: Alpöge's theorem does not enter the forcing criterion.**
   - Relative-Weyl witnesses have nonabelian splitting fields (containing S₄ or S₈), so Dirichlet GRH gives no half-plane
     there.
   - Alpöge enters only through least primes in progressions for abelian splitting fields, at non-Weyl CM points, and only
     with a separate deformation certificate.
   - This bears on the RH/GRH line (our priority): **the Hodge criterion is not a place where Alpöge's GRH becomes an
     input.** The prompt's "Why" ("Alpöge's theorem enters the Hodge criterion as an input for the first time") is refuted
     for the forcing route.
5. **Q43:** a fixed geometric ordinary isogeny class fixes the splitting field L; d_L | d_E^{N/4} (statement level).
   It ties the one-prime test to Honda–Tate.

**Hodge as a goal in itself (crowded; close up and publish):**
- the discriminant thresholds (Q33, Q34, Q37, Q45, Q48), resting on Jaswal;
- the degree-48 cyclic-four Jacobian (A.CYCLE.TARGET);
- Paper B's route exclusions (Q40, Q44, Q46, Q47, Q50–Q54, Q57);
- the analytic perfect-object results Q55 and Q56. These are derived deformation theory, which is AG, but used here only
  for the Weil-detector route.

## 3. What is new against the pile and the literature

- **NT-2 of the pile** (our deduction: forcing without André–Oort, through Jaswal) is now **Thm. forcing of Paper C**, with
  a polynomial threshold and explicit constants at principal level 3.
  - The André–Oort step is now published input: Tsimerman 2018, Th. 1.3, p. 380, for A_g, by the finite Shimura map. PST
    is cited correctly as a preprint.
  - The run, not we, carried out NT-2. No Claude reader has checked Thm. forcing beyond the type-A maximality step, which I
    checked in Paper A on 24 Nov.
- **The prompt update said "H15 is not an ingredient."** The run instead uses an H15-type orbit bound (Q37, Q45, Q48:
  Colmez average plus Gaudron–Rémond) to sharpen the threshold exponent. H15 is an improvement here, not a necessity.
- **The pile's caution on 70d** (the effective gate is H(D), B_S and the detector, not the orbit size) is confirmed:
  - H(D) is now explicit (Q33);
  - B_S is replaced by Jaswal's bound (unrefereed);
  - **the gate is a detector at one high-discriminant point.** Paper C §"What remains to construct" says exactly this.
- **Literature:**
  - OpenAI's eightfold withdrawal is recorded (Q42).
  - The rank-one secant exclusion Q54 credits rStation37v4, Theorems A–C, for the ordinary and free-translation forms
    (an AI-agent preprint).
  - I know of no published effective one-prime criterion of this form. Brünjes–Serpé Th. 3.4 is the qualitative base,
    cited.

**Settled among our open items:**
- the Q28/H19 status (now consistent);
- the André–Oort hypothesis of Paper A (dropped, with the published locator);
- the question whether Alpöge's GRH feeds the forcing criterion (it does not; Q35).

**Not settled:** Q06/Q07 (the Gaussian eightfold detector), Q08 (Mumford), Q26 and Q27 (effective forcing still needs a
witness).

## 4. Consequences for the waiting prompts (Q03 to Q11)

None. I searched the waiting prompts Q03, Q03b, Q04, Q05, Q06, Q09, Q10 and Q11 for André–Oort, Shimura, CM points,
special points, Hilbert schemes, Galois orbits, Jaswal, Chebotarev, Alpöge, zero-free regions, flatness, Severn, Schoen and
Mumford–Tate: no hits. Their main questions are elsewhere:
- Q03b: SGA 2 Lefschetz for Pic and π₁ in characteristic p;
- Q11: good reduction through Barsotti–Tate groups over a reduced base with finite normalization.

Q43 (ordinary reductions of CM points) touches abelian varieties over finite fields, but not Q11's descent question. No
sentence of a waiting prompt becomes more precisely statable.

**For a successor of 70d,** when the run's final comes:
- drop the Alpöge framing of the forcing route (Q35);
- the main question is a relatively flat detector or a detector at a point with |disc L_x| > ℬ(H_D)^{1/μ};
- Q49 excludes product detectors on the flat route.

## 5. Posting candidates (Hexagon)

The run is active, so wait for its final. Then:

1. **Paper A v2 (H25),** now with G₃₄ Severn-free and André–Oort dropped. Remaining gates:
   - restate novelty against Bhattacharjee–Bhattacharya 2610.00315 (the pile's H2);
   - the Schoen 2007 page (the run checked it only at statement level, and the original proof was inaccessible);
   - a Claude page view of the final PDF;
   - the residual Severn wording at line 226.

   This is the "close up and publish" form of the Hodge line.
2. **Paper C,** as a conditional note. Gates:
   - every quantitative theorem rests on Jaswal's unrefereed, AI-produced Hexagon paper; the paper says so on page 1;
   - a Claude check of Thm. forcing whole, and of the H_g(D) proof (C §1226–1700);
   - the one-prime certificate (Thm. arithmetic), the nonflatness (Q49) and Q35 are checked here and could carry a short
     note of their own: "One-prime tests for Weil classes: an arithmetic flatness certificate, and why small detectors and
     abelian fields do not suffice". It needs a literature search, Hexagon included.
3. **Not candidates:** the route exclusions of Paper B (construction-specific), and the degree-48 cyclic-four bound
   (a locus improvement only, within H25).

## 6. What I read, what I did not

**Read:**
- the brief;
- who_checked output;
- the pile INDEX entries (H2, NT-2, §8) and the 70d update report;
- the README, QUESTIONS.tsv rows Q30–Q57, and LEDGER.md (gates Q33–Q57, approaches, the four reviews);
- CHANGES_A and CHANGES_C;
- Paper C: 1–420, 709–807, 1903–2057 and 3501–3700;
- Paper A v2: 215–228, 856–1000, 2230–2250 and 2691–2700.

**Not read:**
- Paper B v2 (only its register rows);
- Paper C's H_g(D) proof, its Jaswal-constant sections and its height/orbit sections;
- the remainder of Paper A's cyclic-four proof (after line 1000);
- the run's programs and its 596 check events (counted, not audited);
- every outside paper, Jaswal's included.

**Added by the main session 329fb1e6, 25 Nov 15:29 UTC:** a25c2acbb3a6f11f7 (Claude Opus 5.5 at effort high), `field_experts/intake_20261121/intakes/HODGE_EFFECTIVE/ALPOGE_ROUTES_20261125.md`: Alpöge's theorem DOES enter the forcing criterion of HODGE_EFFECTIVE: by Heilbronn-Stark (a simple zero of zeta_L off the line would be a zero of a Dirichlet L-function), with Aramata-Brauer and Stark 1974 Lemma 3, there is no Siegel zero for any number field under Alpöge, which replaces the half-plane in the lower Galois-orbit bound (Thm explicit-siegel-orbit holds under A alone, exponent D^{1/(4g)}); the split-prime upper bound still needs a nonabelian half-plane (Hu, Cureton-Thorner, Liu). Stark 1974 Lemmas 3 and 8 are to be opened before anyone relies on it. The intake's sentence that Alpöge does not enter is refuted for this route.
