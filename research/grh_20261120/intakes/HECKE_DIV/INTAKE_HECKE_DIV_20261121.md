# Intake of HECKE_DIV checkpoint 01 (prompt 38, bounded division on Hecke orbits)

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), launched by the main session (Claude Opus 5.5 at effort
max), 21 Nov 2026, under `field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`, with the extra item "Hexagon readiness".
Work file: `agent_notes\20261121_intake_HODGE_SIGN_NOTES.md`. Check events: `INTAKE_HECKE_DIV_20261121_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\HECKE_DIV_checkpoint_01_20261121T0134Z_unzipped\`, checkpoint 01, the only HECKE_DIV
folder present.
- The run is GPT-6 Astra (ChatGPT Pro mode). It began at 00:49:30 UTC; the checkpoint is from 01:34 UTC.
- **The run is still going.** Its LaTeX is only partly integrated, and its newest quantitative work is in `work\`.
- The README names `work\severn_quantitative.md`, but no such file is in the checkpoint.

**What I read:**
- `deliverables\HECKE_DIV.tex`, lines 45–215 in full: R20, P0, R21, R22, R23 and R24A–D;
- the statements of P1–P3, P2b, M1–M4, P4, P5 and A1–A3;
- `LEDGER.md`, `CHECK_EVENTS.tsv`, `CHECKPOINT_README.md` and `TRANSCRIPTION_NOTES.tsv`;
- `work\grothendieck_locators.md`;
- the step-5 passage of `work\arithmetic.md`.

**Scope:**
- **Read in full with a targeted proof check (10):** P0, R21, R22, R23, R24A, R24A′, R24B, R24C, A1 and A2. For A2 I
  checked the formula against the Nakkajima–Taguchi isogeny formula (from memory: 7 splits in Q(ω), so the correction
  term vanishes).
- **Statement level, with spot checks (10):**
  - P1 (I checked Nm(3+ω) = 7, the eigenvalues and the separation);
  - P2 and P2b;
  - P3, M1, M2, M3, M4, P4, P5;
  - A3, which is a trivial countermodel.
- **Not checked:** the numerical E⁴ and E⁸ formulas (R = 2065542, the degree 3.4·10³³, G = 39191040). They are in work
  notes, under the run's own audit.

## 1. Verdicts, finding by finding

- **P0, degree controls the clearing multiplier: confirmed.** The argument:
  - β = *t is flat and harmonic, so it has constant pointwise norm h/√V on the flat torus;
  - the comass is at most that norm;
  - Wirtinger gives |∫_Z β| ≤ (h/√V)·deg_L Z/d!;
  - pairing with N·t gives N ≤ (deg Z⁺ + deg Z⁻)/(d!√V h).

  Clean and correct.
- **R21, closed loci and uniformity: confirmed.** The ingredients:
  - relative bounded-degree Chow (Kollár, 3.21);
  - flatness of cycle-class differences on connected components;
  - properness, so the image is closed;
  - Baire on a ball.

  The fixed-N uniformity is the same argument. It is the standard "countably many closed algebraic loci" principle for
  algebraicity of Hodge classes in families (Voisin's book, from memory). It is new only as stated here, with the integral
  effective complexity c_t.
- **R22: confirmed.**
  - Density of H(Q) (Milne, *Shimura varieties*, 5.4).
  - Riemann equivalence and transport by isogeny.
  - **The correction to the sketch stands:** the sketch's scalar c_x needs a tensor-compatible group, since a general
    unitary similitude moves the rank-two Weil plane through its K-determinant.
- **R23: confirmed** (André–Oort, Tsimerman 2018, Th. 1.3, for A_g). Strict special-genericity is the right hypothesis.
  The enumeration construction is correct.
- **R24A, R24B and R24A′: confirmed.**
  - **R24A′** refutes the signed-degree reading of sketch 2.4 with an integral class ζ of degree zero.
- **R24C: confirmed.** 1 + v with v² = 0 is an automorphism of isogeny degree one outside K. This refutes the
  endomorphism-degree claim of sketch 2.4. The graph-degree formula deg = g!·2^{g−2}(m²+4) is plausible; I checked it
  only at the level of the statement.
- **R24D: confirmed.** Every Hodge class on a variety isogenous to E^g (E = C/Z[ω]) is divisor-generated. This is the same
  fact as **HODGE_SIGN SG-04** and agrees with it.
- **A1: confirmed.**
  - Weak convergence plus the closed proper set S_C gives limsup μ_j(S_C) ≤ μ(S_C) = 0, by the portmanteau theorem.
  - (ii) follows by Markov's inequality.
  - **This is the exact statement of what equidistribution can and cannot give.**
- **A2: confirmed.**
  - h(E_{7^r}) = h(E) + (r/2) log 7, because 7 splits in Q(ω).
  - Hence h(B_{7^r}) = 2n·h(E) + n·r·log 7.
- **A3: confirmed.** A trivial formal countermodel.
- **P1 (the Weil projector), P2 and P2b (graph and divisor-product seeds), P3 (a seed criterion): statement level.**
  - I checked Nm(3+ω) = 9 − 3 + 1 = 7.
  - The eigenvalues are a^r ā^{2n−r}, distinct from a^{2n} and ā^{2n} because a/ā is not a root of unity.
  - deg Γ_B = n!·det(I + B†B) is plausible from the Pfaffian.
- **M1, qualitative fourfold boundedness: statement level. Conditional on Markman** (arXiv 2502.03415: the Hodge
  conjecture for abelian fourfolds), a cited preprint.
- **P4, qualitative bounded division on the split E⁸ family: statement level.**
  - It is **conditional on Severn, Theorem A (Hexagon 2610.00387v2)**, an unrefereed manuscript that the run "audited"
    itself.
  - In our convention it is conditional, not a theorem. The run calls Severn "the checked cited input"; that overstates
    its status.
- **M2, M3, M4 and P5: statement level.**

**Counts:**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 10 (P0, R21, R22, R23, R24A, R24A′, R24B, R24C, A1, A2) |
| Statement level, with spot checks | 10 (P1, P2, P2b, P3, M1–M4, P4, P5), plus A3, confirmed trivially |
| A gap | 0 |
| Refuted | 0 |
| Scope corrected | P4 (conditional on Severn); M1 (conditional on Markman's preprint) |

**The run's own refutations of the Hodge sketch: confirmed.**
- Sketch 2.4, the endomorphism-degree claim (R24C), and its signed-degree wording (R24A′).
- The sketch's 3.2 merges two letters into one (see section 4).

## 2. What is new

- **P0 + R21–R23 + A1** make the sketch's Route 2 an exact reduction: bounded division is equivalent to a single uniform
  integral effective bound, and equivalent to bounded complexity on one strictly special-generic CM sequence.
  - The ingredients are standard: Chow varieties, Baire, André–Oort.
  - The explicit forms are new as stated: the Wirtinger multiplier bound P0, the special-generic dichotomy, and the
    equidistribution limit A1.
- **R24C** is elementary. As a correction to our sketch, it is the useful kind.
- **P2b** gives integral seeds of small degree (80/80 on E⁴; 147456/175104 on E⁸), with raw transport growing as m^{2n}.
- **P4** would be the main result (the main question, qualitatively), but it rests on Severn.

**Against our results.**
- R24D is HODGE_SIGN SG-04, and my HODGE_SIGN intake (section 5) proposed exactly this divisor-product attack for prompt
  38. P2b carries it out at the base point.
- The transport growth m^{2n} shows that the denominators of divisor products are not uniform along the orbit. Uniformity
  is the gate.
- My HODGE_SIGN suggestion that End(E_v) stays fixed at split primes concerns special fibres. It is HECKE_DIV's P6/R26
  route (uniform degree at infinitely many good primes). I have not read that note.

## 3. The two proofs, and HODGE_SIGN

- **Alpöge:** cited. No finding read uses RH or GRH (R23 and P4 say so explicitly).
- **Masullo:** not used.
- **QA:** equidistribution under GRH is shown to be insufficient by itself (A1).
- **SG-08–SG-11 (H01):** not used, and not changed. The run's `work\arithmetic.md` reads Alpöge's step 5 and records "no
  cycle coercivity/saturation statement identified; no claimed implication used". A3 is the formal reason. This agrees
  with HODGE_SIGN SG-01, SG-06 and HS-05: the step-5 sign carries no bilinear form, and purity cannot see cycle-class
  kernels.
  - **For prompt 38's task 3, "the positivity of Alpöge's step 5" is now settled as no input.**
- **Overclaim:** "checked cited input" for Severn (P4). It is to be relabelled as conditional.

## 4. Integration

- **Scan numbering: settled by this run.** `work\grothendieck_locators.md`:
  - downloaded the official cote 16 PDF (`grothendieck.umontpellier.fr/16.pdf`, 56 pages, sha256 a03bc009…);
  - found that the printed folio is the one-based PDF page minus one.

  Our text of record numbers by PDF page (`\scanpage`) and records the folio (`\mspage`). For example, `16_scan044.tex`
  has `\mspage{43}`. So:
  - **HODGE_SIGN and HECKE_DIV use our numbering;**
  - **GCT_NSRH and THETA3 cite folios.**

  **Edit:** in the GCT_NSRH intake (item 1) and in the Hodge sketch's section-5 note, replace "an offset" by "folio
  numbering (folio = our scan − 1)".
- **Two letters, not one.**
  - PDF pages 44–47 (ours 044–047) are the letter of 4.1.67.
  - PDF pages 48–50 (ours 048–050) are a second letter, dated "6.1.1966" as written. Our `16_scan048.tex` already reads
    `\margin{6.1.1966}` and "Dear Coates".
  - So "C(X) + I(X×X) ⟹ semisimplicity" (049) and "Weil from C and A" (050) belong to the second letter.
  - **Edit, sketch 3.2:** replace "cote 16 scans 44–50, letter to Coates of 4.1.67" by "cote 16 scans 044–047 (letter of
    4.1.67) and 048–050 (letter dated 6.1.1966 as written)".
  - **Same edit in sketch section 5** (the cote 16 scans 44–50 row) and in sketch section 1.
  - The CSG transcriptions L10d and L11d agree.
- **Hodge sketch, Route 2:**
  - add "2.1–2.3 proved with corrected hypotheses as HECKE_DIV R21–R23 (checked)";
  - add "2.4: the endomorphism-degree statement is false (R24C), and the signed-degree reading is false (R24A′). The
    correct invariant is the effective or graph degree (R24A, R24B)";
  - add "equidistribution alone is insufficient (A1); Colmez heights grow in a fixed-field orbit (A2)".
- **Prompts:**
  - **39 (GHOST_CLASSES)** can use P1 (the explicit projector), P2b (integral seeds) and A2 directly.
  - **41 (DEGREES_ARE_L_VALUES)** can use P0, the multiplier bound from degrees.

## 5. Hexagon readiness

| Finding | 1 Complete | 2 Self-contained | 3 Stable | 4 Checked | 5 Of interest | Verdict |
|---|---|---|---|---|---|---|
| P0 + R21–R23 + A1 (the exact reduction of bounded division) | yes, as read | yes (Kollár, Milne, Tsimerman cited) | **no:** the run is going and will extend it | targeted check by me; no independent re-proof | medium: the principle is folklore, the explicit forms are useful | **two gates:** the final paper, and a literature search (Voisin; Cattani–Deligne–Kaplan) |
| P4 (qualitative bounded division on E⁸) | rests on Severn | **no:** an unrefereed manuscript | no | no | high | not a candidate unless Severn is refereed or re-proved |
| M1 (fourfolds) | rests on Markman | Markman is an arXiv preprint | no | no | medium | not yet |
| R24C, A2, A3 | yes | yes | yes | yes | low: corrections to our sketch | not post material |

**None passes, and none is one gate away with a strong test 5.** Nothing to flag. Watch P0 + R21–R23 + A1 for the final
return.

## 6. Prompt updates (HECKE_DIV successor)

1. **Label P4 and M1 conditional** on Severn's Theorem A and Markman's preprint. State exactly which statements of those
   papers are used.
2. **Main attack: P8, bounded division on the E⁸ orbit, without Severn.**
   - Use P2b's integral divisor-product seeds and P3.
   - The question is whether some fixed-degree effective cycle has a nonzero Weil projection along a strictly
     special-generic sequence.
   - Route through special fibres (P6/R26): at split ordinary primes End(E_v) = End(E), so the divisor-product
     intersection matrices are fixed (HODGE_SIGN SG-04, finite-field part). Test whether that gives a uniform degree at
     infinitely many primes.
3. **Write the numerical E⁴ and E⁸ formulas into the paper** with their independent audits. Supply the missing
   `severn_quantitative.md`.
4. **Archive:** cite by PDF page (= our scans) and folio, as `grothendieck_locators.md` does. Use our text of record:
   cote 16 scans 014–018 and 044–050.
