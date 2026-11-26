# Intake: POLISH_CRISTAUX, checkpoint 12 (prompt 92), 23 Nov 2026

Intake by Claude (Claude Opus 5.5 at effort high), launched by the main session (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode); the run does not expose its effort setting, and the run's records say so. Work file: `<local>/Documents\agent_notes\20261123T1107Z_Intake_POLISH_CRISTAUX_cp12_NOTES.md`.

## 0. What I read and my scope

Return: `grothendieck_archive_transcription_20261110\research_returns\POLISH_CRISTAUX_checkpoint_12_20261123T1045Z_unzipped\`. The top folder is the one holding `README.md`, sealed at 10:45:19 UTC. It is a snapshot of a run that is still going.

- **Prompt as sent:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\92_POLISH_CRISTAUX\PROMPT.md`, read in full. I did not open its ZIP.
- **Read in full:**
  - `README.md` and `CORRECTIONS_FOR_AUTHORS.md`;
  - `REGISTER_CENSUS.json` and `REGISTER_CURRENT_CENSUS.json`;
  - `QUESTIONS.tsv` (all 43 rows, columns id to gate);
  - the `LEDGER.md` blocks from Review06 to "Immutable checkpoint 12";
  - the `LITERATURE.md` classification rule, its first novelty search and the prime-to-p search block.
- **Read in full, every step rederived:**
  - Paper 1: `main.tex`, `injectivity.tex`, `positive_ranges.tex`, `DEPOSIT.md`;
  - Paper 3: `main.tex`;
  - Paper 4: `main.tex`.
- **Paper 2 (92 pp.), read in part:**
  - read in full: `paper.tex`, `introduction.tex`, `complete_prime_main.tex`, `canonical_iteration.tex` and `central_ramification.tex`;
  - read at statement level only: the lemmas these cite from the other 16 section files.
- **Papers 5 to 17:** abstract and README scope only (statement level). I did no check of these.
- **CHECK_EVENTS.tsv:** summarized by script (section 1.6). I did not read it row by row.
- **REGISTER.tsv:** used only to locate rows.
- **Primary pages opened for the corrections** (fetched PDFs; their SHA-256 match the run's records):
  - Grammatica, arXiv 2507.08568v2, p. 29;
  - Bhatt, arXiv 1207.6193v1, p. 8;
  - Rains–Sam 2019, p. 342 (PDF p. 15).

## 1. Each paper's main theorems: verdicts

Every check type below is in the rubric's terms. The run's "independent re-proofs" are separate workers of the same model (GPT-6 Astra, ChatGPT Pro mode), and the papers say so.

### 1.1 Paper 1: "Counterexamples to integral weak Lefschetz in Grothendieck's *Cristaux*, after Raynaud and Mukai" (Prompt Paper 1, the OC chain)

**Verdict: confirmed (targeted proof check), for all three main theorems.**

- **Thm 1.1 (explicit characteristic-2 surface and product threefold).** Read in full; every step rederived.
  - Recomputed:
    - genus 7 for y^2+y=x^15; the pole semigroup <2,15> gives h^0(N)=2 and h^0(N^3)=4;
    - h^0(L)=6;
    - h^1(S,L^-r)=1,0,... from m_i(1)=1,2,2 (only the i=2 summand H^0(O_C) survives);
    - h^0(L^9)=210+186+160=556;
    - h^0(Ω_S) <= 9+9+17 = 35 = B_2;
    - very-ample margin ℓn-3=3;
    - m=591·9^556+2 makes a(m-1)-u(X) >= 1.
  - The product criterion was checked line by line:
    - the kernel complex K^j = Ω_Z^j(log Y)(-Y);
    - the Künneth vanishings;
    - injectivity of d_1 on H^1(K^1), via the composite with restriction;
    - the Tor argument for Q[p]=0.
  - Injectivity holds for every d >= 1. Saturation holds iff d >= 2. Both are correct.
- **Thm 1.2 (every characteristic).**
  - The vanishing H^1(X,A^-r)=0 for r >= p^2-p holds: the largest exponent is pi-s-(p+1) < 0.
  - The vanishing H^0(Ω_X ⊗ A^-r)=0 for r >= p+1 holds, because m_i(p+1) = p+⌈pi/(p+1)⌉.
  - m=u(X)+2 suffices.
- **Thm 1.3 = Thm 5.x (iterated Tango threefold, noninjective exactly in degrees 1 and 2).** Read in full.
  - Recomputed:
    - g=421 for x^843;
    - the Tango divisors 210N_0 → 10B → 2L;
    - h^0(B)=2+22=24 and h^0(B^5)=Σ_{i=0}^{5}(6+20i)=336;
    - m_j(1)=1,1,2,2,2 and e_j=-3,1,5, so h^1(R,L^-1)=24+336=360;
    - h^1(L^-2)=1 (the j=3 term H^0(O_S));
    - h^1(U,H^-1)=360+843=1203, giving a kernel on C^2[2] of dimension at least 1203-842=361.
  - Checked: Sym^2V ≅ V ⊕ B^20 in characteristic 2 (the cross term vanishes, and the Frobenius-split coboundary gives the complement).
  - Checked: non-annihilation, since sα corresponds to s^2η ≠ 0.
  - Checked: the closed-form argument for injectivity when d >= 3.
  - The first-lattice lemma (Stein factorization, the Riemann–Hurwitz degree bound, Pic^0, Illusie II 3.11) was read and holds. This is the most delicate step. It deserves the different-model re-proof first.
- **Thm 8.1 (regularity bound).** Correct. It is presented as a form of BMS Lemma 2.12 and is not claimed as new.
- **Record defect:**
  - `paper1/DEPOSIT.md`'s method note says the saturation and iterated-Tango separate reconstruction "is not claimed".
  - `main.tex`'s method note says that separate derivations cover them.
  - The two must be reconciled. The check events (`thm:OC-exact-integral-injectivity-degrees`, a separate reconstruction with an omitted step repaired) support `main.tex`.

### 1.2 Paper 2: "Ramification thresholds for Grothendieck's inertia-character question, after Bondarko and Drinfeld" (Prompt Paper 2)

**Verdict: top-level argument confirmed (targeted proof check). Not read in full: the cited inputs were read at statement level only.**

- **Thm complete-prime-index: ν_min(p,e,2) = ⌈(1+log_p e)/2⌉, for p >= 5, (p-1) | e, p ∤ e, μ_p ⊂ K.** It is new at 10:38 UTC today. I checked:
  - the assembly proof;
  - the equivalence with p^{2r-3} < e < p^{2r-1} (strict, since p ∤ e);
  - p^{3n-3}/(p^n-1) = p^{2n-3}+p^{n-3}+p^{n-3}/(p^n-1);
  - S_n/(p-1) = p^n+1+1/(p^n-1);
  - the choice of c (the least c with p^c z > e) and the condition p ∤ (p+1)e - z_c.
- **Thm central p^2 rigidity.** Read in full and followed. The steps:
  - the Newton values A=(p+1)e-z on p-1 points and B=z/p, whose sum gives v_L(p);
  - "central" (z > e) makes v_L(T(Q)) = A/p^2;
  - [F:L] = p^2 and [F_0:L] = p;
  - the lower break b = (p^2-1)A, from the Serre-type valuation lemma, whose equality clause applies since p ∤ A;
  - transport by stabilizers gives t >= A;
  - prime-Hasse recovery, or strict ordering, closes the argument.

  The case analysis of t (canonical/central, noncanonical, one-slope) is consistent.
- **Inputs read at statement level only:**
  - rc-lem:newton, rc-thm:primehasse, rc-cor:strictordering;
  - fc-thm:valuation (the graph bound, which gives z >= (p-1)p^{2n-1}/(p^n-1));
  - lem:actual-quotients, lem:one-slope-recovery;
  - prop:mixed-obstruction and cor:sharp-mixed-prime (the lower examples);
  - thm:minimal-index.

  The lower bound of the exact index rests entirely on the mixed constructions, which I did not read.
- **Prompt-named items** (ν_min(5,20,2)=2, ν_min(p,2p(p-1),2)=3, cor:B-RD27-exact-three, thm:three-range): statement level only.
  - From the stated criterion of thm:three-range I recomputed that the least e for full rational 27-torsion with additive reduction is **162** (u=81, s=4, m=12).
  - At e=216 only defect 12 works: m=6 gives 6·216=1296 < 1944.
  - This agrees with the paper.
- **Structure:** the introduction still states Cor prime-recovery-intro (index 3 up to (p-1)(p^4+1)), which the complete theorem supersedes. The prompt asks to restructure around the stronger result.

### 1.3 Paper 3: "Grothendieck's Frobenius-stable Lefschetz formula for every smooth ample divisor, after Ogus" (Prompt Paper 3, A2-EXACT and A2-UNIT)

**Verdict: confirmed (targeted proof check), for Thm 1.1 (sequence (8.5.1) with the term T^n(X)[p]_st), Thm 1.2 (the unit-root count), Cor transpose and Cor star-dual.**

- Checked:
  - exactness of stable extraction (Fitting and Artin–Rees);
  - the edge lemma: F = ba on Ω^•, where a is the projection to O[0] and b is f ↦ f^p;
  - the snake-lemma derivation of (8.5.1);
  - Z[T]-integrality of the quotient polynomial;
  - the linking-pairing degrees.
- Recomputed the plane cubics over F_5:
  - Y_1: y^2=x^3+x+1 has 9 points, P = 1+3T+5T^2, stable dimension 1;
  - Y_2: y^2=x^3+1 has 6 points, P = 1+5T^2, stable dimension 0.
- **Novelty is weak.** The paper presents these as consequences of Ogus 1975 (Lemma 4.8, Thm 4.9, Cor 4.11) and Katz–Messing, without priority. The Frobenius-nilpotence-of-negative-twists argument is a standard one. I expect "known in substance".

### 1.4 Paper 4: "A reduced counterexample to Grothendieck's extension assertion, after Ferrand–Raynaud and Olberding" (Prompt Paper 4, C-RD4 and C-RD11)

**Verdict: confirmed (targeted proof check), for Thm 1.1, Thm 1.2, Prop mixed and Lemma ring.**

- Recomputed:
  - the Hasse coefficient 2a = -6t/(t-1728) ≡ 4t/(t-3) (mod 5);
  - j(E_t) = t;
  - Δ = 1728^2 t^2/(t-1728)^3 (using 16·108 = 1728);
  - for the mixed example, Δ = -496 and j = 6912/(31+54ε) = 6912/31 - (373248/961)ε.
- Lemma ring: checked m = (p,z), m^2 = pm, noetherian via m^{2s} ⊂ aR, and normalization not finite (the conductor argument with u_N).
- Checked the Serre–Tate contradiction: j(A) maps to t+ε under R/5 ≅ k[ε], while the constant deformation has j = t.
- Checked that the generic isomorphism is defined over F (Isom is finite étale and F is relatively algebraically closed).

### 1.5 Papers 5 to 17

These are further papers the prompt allows ("the rest of the register"). I read them at statement level only and made no check. The run's own scope statements (README table) record:
- separate same-model reconstructions for the main theorems of each;
- open gates in Papers 10, 12, 15 and 17;
- auxiliaries at targeted-check scope only (9, 10, 16).

None is a published-work correction.

### 1.6 CHECK_EVENTS.tsv in numbers (5,414 events)

- **Split:** 4,747 are imported history (`IMPORTED_EVIDENCE_NOT_A_NEW_CHECK`); 667 are current (`RECORDED_CURRENT_CHECK_WITH_STATED_SCOPE`).
- **By type:**

| Type | Events |
|---|---|
| targeted proof check | 3,325 |
| independent re-proof | 467 |
| computation or formal certificate | 452 |
| carried as background | 373 |
| "statement read only (no check)" | 248 |
| used and rechecked | 152 |
| mixed or nonrubric labels ("full mathematical/source/code audit", "artifact verification", "source-check", "proof+independent-parent-audit") | about 200 |

- **Events dated 22–23 Nov:** 1,831. Of these, 1,094 come from our three earlier intakes (agents a8d07e78, a1cf7c6b, afcdf31b, Claude Opus 5.5 at effort max).
- **Current independent re-proofs:** they cover 132 statement keys, among them the whole OC chain, B-RD74, C-RD10, C-RD12, C-RD13 and many B-RD lemmas.
- **Refutation events:** 17. They include A6-COUNTEREXAMPLE (with refined A6-SMALL), B-RD4 (Lead B′), C-RD2 and C-RD4.
- **Still to do:** 712 of 1,018 register rows are NOT_YET_RECHECKED. The nonrubric type labels should be normalized in a successor.

## 2. Corrections to published work

| Item | My check | Already corrected? | Report? |
|---|---|---|---|
| **Grammatica**, arXiv 2507.08568v2 (31 Oct 2026), Remark 4.6, p. 29, last sentence ("It follows that when X is proper over the perfect field k there is an isomorphism H^i_ét(X,Z_p) ≃ H^i_cris(X/W(k))^{F=1}…") | **Confirmed** from the primary page. Counterexample X = Spec F_p: H^1_ét(X,Z_p) = Hom_cont(Ẑ,Z_p) = Z_p, but H^1_cris = 0. The triangle she states is correct and gives 0 → coker(F−1 \| H^{i−1}) → H^i_ét → ker(F−1 \| H^i) → 0. The repair is to restrict the two conclusions to algebraically closed k (as Ogus Cor. 4.11 does), or to keep the exact sequence. | No: v2 is the newest version and has it. | **Yes** (draft 1). |
| **Bhatt**, arXiv 1207.6193v1, Construction 4.7, p. 8: "completion of F along the I = ker(F → A)" | **Confirmed.** It must be ker(F → B). | Only v1 exists, with no journal-ref; uncorrected. | Optional (draft 2): a pure typo in a 2012 preprint. I'd send it only if the user wants. |
| **Rains–Sam**, Algebraic Geometry 6(3) (2019), Remark 5.8, p. 342: "this is equivalent to Pf(Q(π(γ))) ≠ 0" | **Confirmed** from the page: f16 = Pf(Q)^2, so the condition is "= 0". | I did not search for an erratum, or check the arXiv version. | Optional (draft 3): a typo with no mathematical effect. |
| **Dimca–Greuel** (2018), p. 115, ambient-ring notation | Not re-verified by me (the run's reading is plausible). It is notational only. | — | No draft. |

## 3. Corrections to our own work

1. **"27-torsion at e = 216" (PROMPT.md line 56)** reads as if 216 were the first index for full 27-torsion. The least index is **162**; I recomputed it from the criterion of thm:three-range.
   - The source sentence (RESEARCH_SA15 `sections/B.tex:1923`, as quoted in `field_experts\intake_20261120\SORTED\RESEARCH_SA15.tsv` line 47) says "the first higher case **beyond this construction**". That is correct, because the tame construction misses 216.
   - Edit: in any successor prompt and in the SA15 field record, write: "full rational 27-torsion with additive reduction: least index e = 162 (defect 12); e = 216 is the first index the tame construction misses, realized with defect 12."
   - The intake the run cites as the source of the wording is in `ours/intakes_sweep3` of the prompt ZIP, which I did not open. Its line should carry the same note.
2. **The third-index interval shorthand must carry p ∤ e** (run's internal item 1). The prompt's "p^3 < e < p^4" omits it. The papers have it.
3. **Paper 1 record mismatch:** `workbench/papers/paper1/DEPOSIT.md`, section "Note on method", sentence 3 ("The saturation and iterated-Tango arguments received targeted rereading; their complete separate statement-first reconstruction is not claimed"). It disagrees with `main.tex`'s Note on method. The run should reconcile them; I made no edit.
4. **The run's own record-level item** (cote 4 sheet/image offset by one) is consistent with the quotations in Papers 1 and 3.

## 4. What is new against the literature (main theorems)

| Paper | Main theorems | Status against the literature |
|---|---|---|
| **1** | All three | NEW_CANDIDATE. The coherent and flat failures are known (Raynaud, Mukai; Cotner–Zavyalov Ex. 3.3.6, crediting Totaro), and the paper says so. What is new is the integral **crystalline** statements with exact degree thresholds for a fixed very ample embedding. The run's search was bounded. One targeted search is still owed: whether "Kodaira failure ⇒ extra crystalline torsion on hyperplane sections" is folklore, via the citations forward from Cotner–Zavyalov and Mukai. |
| **2** | Complete prime-to-p index | NEW_CANDIDATE, against Bondarko 2006, Hattori 2008, Smith 2023 and Ozeki–Yoshida 2026 (bounded search). It is hours old, and the run is still working on the p-divisible branches. |
| **3** | All | Most likely known in substance (Ogus 1975 plus Katz–Messing). The paper calls them consequences. |
| **4** | All | An application of a known ring construction (Ferrand–Raynaud, Olberding) to Grothendieck's manuscript assertion; new as an answer to that assertion only. Krishnamoorthy–Pal settle the normal case. |

## 5. Hexagon readiness (the five tests and HOW.md boxes)

- **Box 8 for all papers:** no paper has a section headed "Proof overview". Papers 1 and 3 have a "Why the proof works" paragraph, Paper 4 has "The mechanism", and Paper 2 has scattered mechanism paragraphs. All 17 fail box 8 in its new form. Boxes 1 to 7 are met in Papers 1, 3 and 4 as far as I read.

| Candidate | Complete | Self-contained | Stable | Checked | Of interest | Gate left |
|---|---|---|---|---|---|---|
| **Paper 1: integral weak Lefschetz fails** (the H-list entry "SA15 part 2") | Pass | Nearly: rational crystalline weak Lefschetz is cited from Nakkajima–Yobuko's arXiv v3. Better to cite a published form, or derive it from Katz–Messing and ℓ-adic weak Lefschetz in a line. | Pass as far as visible: the run is now on Papers 2 and 17. | Pass: my targeted check of every step, earlier intakes, same-model separate reconstructions and the programs. | Moderate | (a) The forward literature search above. (b) A "Proof overview" section and the DEPOSIT fix. (c) The run's final. **One gate away once the run ends.** |
| **Paper 4: reduced counterexample to the extension assertion** | Pass | Pass (the ring lemma is proved in the paper) | Pass | Pass | Modest (narrow audience) | Box 8 and the run's final. |
| **Paper 3** | Pass | Pass | Pass | Pass | Fails as a new result (known in substance) | Fit only as an exposition; not recommended. |
| **Paper 2: complete prime-to-p index** | — | — | Fails (proved today; the run is still moving) | Fails: only the top-level argument has a check outside the run (mine); the inputs and lower constructions do not | — | A full-chain check, preferably by a different model, and the run's final. |
| **Grammatica correction** | — | — | — | — | — | Not a post; email only. |

## 6. What a successor or finishing prompt needs

1. Restructure Paper 2 around the complete prime-to-p theorem: remove or demote Cor prime-recovery-intro and the one-quotient intervals. Settle the remaining p-divisible-index branches named in its open section, at p >= 7 and e = p(p-1).
2. Add a section headed "Proof overview" to every paper (HOW.md box 8).
3. Reconcile `paper1/DEPOSIT.md` with `main.tex`. Replace the arXiv citation for rational crystalline weak Lefschetz with a published one, or derive it.
4. Carry the 162/216 wording fix and the p ∤ e hypothesis into every record.
5. Normalize the roughly 450 nonrubric event-type labels (section 1.6) to the six rubric types.
6. Recheck 712 register rows still marked NOT_YET_RECHECKED, or state explicitly why each does not enter a paper.
7. For Paper 3, consider merging into Paper 1 as its positive companion, or labelling it an exposition of known consequences.
8. Run a different-model independent re-proof of:
   - the Paper 1 first-lattice lemma (Stein degree, Pic^0);
   - the Paper 2 graph bound (fc-thm:valuation);
   - the Paper 2 mixed constructions.
