# Intake of ALP_MACHINE checkpoints 50–55 (run opened 21 Nov 19:35 UTC), by diff from checkpoint 48

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026, evening wave
(`INTAKE_WAVE_20261123_EVENING.md`).

- **Return:** `research_returns\ALP_MACHINE_checkpoint_55_20261123T1505Z_unzipped\ALP_MACHINE\` (newest filed;
  checkpoints 50–54 are its predecessors and are contained in its register). The run is GPT-6 Astra (ChatGPT Pro
  mode), active; reviews 37–41 all record movement.
- **Check events:** `INTAKE_ALP_MACHINE_20261123_cp55_CHECK_EVENTS.tsv`.
- **Integration:** `INTEGRATION_ALP_MACHINE_20261123.tsv`, with backups in
  `integration_backups\20261123\ALP_MACHINE\`.
- **Primer:** `PRIMER_ALP_MACHINE_20261123.md`.

## 0. Scope

**Read:**
- the register diff, 422 rows against 388: 34 new, all PROVED_IN_STATED_SCOPE, no state changes;
- every new row in full, up to 700 characters;
- the ledger headings 37–41;
- **LIFT110** (`agents\abelian_coefficient_normalized_ideal_obstruction.md` §§1–4) in full.

**Rederived myself:** the arithmetic part of LIFT109, and the rank-one example of AM-S4.

**Not read:** the other 32 proofs and every script.

**AM-S4 is not in this run.** It belongs to the other prompt-49 run, opened 20:03 UTC (ids AM-L, AM-SS, AM-ST, AM-S).
I read and checked its text on 22 Nov at that run's checkpoint 08 (`oscillator_sign.tex` §AM-S4), and recomputed its
example here. No newer return of that run is filed.

## 1. Verdicts

| Type | Findings |
|---|---|
| Targeted proof check | LIFT110 Theorem A, LIFT110 Theorem B |
| Computation or formal certificate (mine) | LIFT109 class-group arithmetic; AM-S4 rank-one canonical element |
| Used and rechecked | LIFT54/55 |
| Carried as background (statement level) | the other 31 new findings |
| Refuted | none |

**Main questions:** Q1 and Q2 OPEN, Q3 OPEN, Q4 PARTLY_PROVED, Q5 PROVED_IN_STATED_SCOPE. Only the texts of the Q1 and Q2
gates changed. **49b has not been taken up** through checkpoint 55: no ledger entry, no row.

## 2. What is new, usefulness first

1. **LIFT110: abelian coefficient fields cannot carry Alpöge's normalized ideal law.**
   - *What it is good for.* It tells anyone instantiating or simplifying step 8 of Alpöge's formal proof that the
     coefficient field of a literal instance cannot be the obvious cyclotomic one, nor any abelian extension of the
     quadratic field K. This is a second structural constraint on the interface, beside the size floors LIFT54/55.
   - *Theorem A (checked).* Let K be imaginary quadratic with μ(K) = {±1}, F/K finite abelian, J a nonzero integral
     K-ideal. If J O_F = (ξ) with |σ(ξ)|² = N(J) for every complex embedding σ of F, then [J]² = 1 in Cl(O_K).
   - *Proof outline.*
     1. Write J^h = (γ) in K. Then u = ξ^h/γ is a unit, and all its conjugates have absolute value 1, so u is a root
        of unity of some order m (Kronecker). Hence ξ^{hm} = γ^m.
     2. The splitting field of X^{hm} − γ^m over K lies in F(μ_{hm}), which is abelian over K.
     3. Schinzel's theorem then gives γ^{m·w} = b^{hm} with w = |μ_{hm}(K)| = gcd(hm, 2). Hence J^w = (b) in the ideal
        group.
   - *Theorem B (checked from the stated inputs).* Take the prime discriminant −d with d ≡ 7 mod 16 and d > 365.
     - The norm map N_{E/K}: Cl(E) → Cl(K) is onto (LIFT109; statement level).
     - h_K is odd. The class above 2 has odd order h₂ with 2^{h₂} ≥ (d+1)/4, so h₂ ≥ 7 (rederived by me).
     - So the normalized kPsi law in an F inside K^ab would make Cl(K) 2-torsion, hence trivial, contradicting h₂ ≥ 7.
     - In particular E·Q(ζ_M) and its compositum with the Hilbert class field of K are excluded, although the latter
       principalizes every ideal.
     - Non-abelian and non-Galois F remain possible.
   - *Novelty.* Theorem A is a short combination of Kronecker's and Schinzel's theorems. Its form may well be in the
     literature on normalized generators and Weil numbers; I have made no search.
2. **LIFT100–108: constructors for the formal source interface,** each conditional on the geometric records:
   ThNe0, all-ring theta-value totality, IsNab realizations, ShortValTot, ShortThetaUnit, the kPsi table reduced to
   the class group of the norm image (LIFT108), and the beta law from the accepted archive (R102).
   - *Good for:* a formalizer who wants the gap list of a literal instance; together with LIFT110 they give it.
   - Statement level.
3. **The finite signed gate (DO121–130, R098–103, K117–123):**
   - all of support 27 is removed, and DO129 allocates it into nonnegative completions;
   - the open sufficient inequality is now Re Σ_{support ≥ 28} w(h) > −1 + 2^{−230};
   - DO130 and R103 remove fixed-S sectors at supports 28–150.
   - *Good for:* only the run's own nonvanishing step. It is bookkeeping. Statement level.
4. **AM-S4 (other run, recomputed):** a formal half-weight variable v = √q is not a reduction to Hecke-character RH.
   - Already the P¹ point count and the rank-one canonical element b = H + v^{−1} (b̄ = b, b² = (v + v^{−1})b) use it.
   - *Good for:* it corrects the reading of the "√q → ERH" rung in our SPLIT_ZERO notes. The correction is applied
     with its locator.

## 3. Scope of the inputs

- **Alpöge's theorem** is cited as a theorem.
- **LIFT110** uses Kronecker (Milne, ANT, Cor. 5.6) and Schinzel 1977, Th. 2. I did not open either source; both are
  standard.
- **LIFT109–108** are taken as stated, except for the arithmetic I rederived.
- **Masullo:** no use.

## 4. Integration (applied; log in `INTEGRATION_ALP_MACHINE_20261123.tsv`)

- `reports_20261122\paper_seeds\SEED_ALP_MACHINE.md`: a new section "Update at checkpoint 55", with LIFT110's statement
  and proof, and the gate.
- `reports_20261122\MATHEMATICS_OF_THE_EVENING_20261122.md`: a status line at checkpoint 55 under the checkpoint-29
  block.
- `reports_20261123\NONSTANDARD_RH_SLICES_20261123.md`: the AM-S4 reference now names its run and file, and the
  recheck.
- The seed's f-convention correction from my checkpoint-11 Part-B intake was already applied by another hand.

**For the main session** (shared registers):
- the board rows of section 7;
- the HEXAGON_CANDIDATES updates listed in my HODGE_BOUNDED_CYCLES final intake;
- 49b: resend at a turn boundary, or fold it into the finishing prompt. The run has not seen it.

## 5. Prompt updates

1. The finishing prompt of this run should include the bounded-chain question with LIFT110 added to "where you are".
   The chain must avoid both the size floors and abelian coefficient fields.
2. Ask the run to search for Theorem A in the literature on normalized generators of principal ideals in abelian
   extensions, before calling it new.

## 6. Hexagon readiness

| Candidate | Proved | Checked by me | New | Gate left |
|---|---|---|---|---|
| Chain-length theorem (LIFT54/55; NIGHT_AFTER_ALPOGE Part B with Lean) | yes | yes | yes, for Alpöge's interface | the SizesAt bridge compiled, and a short note |
| LIFT110, as a section of that note ("two structural constraints on step 8") | yes | yes (Theorem A in full) | as applied to the interface, yes; Theorem A's form needs a search | a literature search for Theorem A; a read of LIFT107–109 |

## 7. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)

| Title | Statement | What it adds | Gate left |
|---|---|---|---|
| Abelian coefficient fields cannot carry normalized ideal generators | For imaginary quadratic K with μ(K) = {±1} and finite abelian F/K: if J O_F = (ξ) with \|σξ\|² = N J for all σ, then [J]² = 1 in Cl(K). Hence a literal instance of Alpöge's formal step 8, at a prime discriminant with d > 365, needs a coefficient field outside K^ab | a second structural constraint on the interface of Alpöge's proof, next to the size floors | literature search for Theorem A; LIFT107–109 read; to be written as a section of the chain-length note |

## 8. For the P vs NP fleet

No result of this wave bears on complexity. The one nearby item is AM-S4 (other run): a formal √q normalization does
not by itself feed an analytic input to a GCT canonical-basis statement. The map:
- **Node:** L-gct-011 (the Mulmuley–Sohoni separation conjecture). The proof graph has no node for GRH-conditional
  complexity results (Koiran's HN ∈ AM).
- **Translation:** "a canonical-basis positivity input via Hecke-character RH" needs an arithmetic object whose
  L-factors are the CM Hecke factors in question. The half-weight variable alone does not supply it.
- **Bridge work:** construct that arithmetic realization, or add a GRH-conditional node to the graph for the Koiran-type
  route, so that Alpöge's theorem, now a theorem for Dirichlet L-functions, can be attached where it applies.
