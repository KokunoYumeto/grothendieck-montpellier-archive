# Intake of THETA3, part 3: checkpoint 04 (prompt 37)

By Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent), 21 Nov 2026, round 4. Part 2 read checkpoint 03. Check
events: `INTAKE_THETA3_20261121_part3_CHECK_EVENTS.tsv`.

## 0. What I read

**The return:** `research_returns\THETA3_checkpoint_04_20261121T0349Z_unzipped\`, the newest present. It is from 03:49
UTC; the run is still going. The checkpoint-03 folder has been retired, so I compared against my part-2 notes and against
this checkpoint's ledger.

**What I read:**
- the new `QUESTIONS.tsv` rows;
- `LEDGER.md` from checkpoint 03 to the **first formal progress review (03:49:30 UTC: MOVEMENT)**;
- the statements of C25 and C27, and C25's scope paragraph.

**New since checkpoint 03:** twelve rows.
- Q1-CM-jet-functional (B19), Q1-isotropic-completion (B20), Q1-common-product-module (A10), Q1-cross-type-period
  (B21);
- Q2-period-size (B22);
- Q3-balanced-Weil-alln (C24), Q3-exceptional-fourfold (C25), Q3-finite-cup-test and Q3-fixed-source-deformation (C27);
- Q4-isotropic-frame (A9, C26), Q4-integral-A6 (C23), Q4-biextension-KR (C23).

**No finding I checked in parts 1–2 is changed or withdrawn.**

## 1. Verdicts (all at statement level; nothing new bears on SG-08–SG-11 or needed a full proof read here)

- **C25: a geometrically simple Q(i)-Weil fourfold** (a hyperelliptic Jacobian with branch points from 8- and 13-torsion
  of y² = x³ − 30x − 25). It has End = Z[i], NS rank 1, and an entirely exceptional Weil space. It occurs as a quotient of
  the Albanese of a ball cover of degree ≤ 43264. Statement level. The run checked F₁₀₉ point counts with independent
  implementations.
  - **Scope, correctly stated by the run:** Markman already proves these Weil classes algebraic. C25 is a test object for
    the theta construction, not a new Hodge case.
- **C27: the map-based route reduces to a finite quartic cup test** F_X on Hom_K⁰(Alb X, A), with at most 5^m integer
  combinations to try. A fixed-source deformation is obstructed, because the Kodaira–Spencer map is injective. Statement
  level.
  - **Sound in outline:** the quartic is ∫_X ∧(Σ z_j f_j^* v_r). It agrees with C13 and C14 (the same projector, and
    curve products vanish).
- **B19–B22, A9, A10 and C23–C24, C26: statement level, from their rows and the ledger.** Notable:
  - B21 locates the residual raw scalar as a full Hodge-determinant period ratio, and shows linear CM-type balance does
    not make it algebraic;
  - C23 extends the A6 cycle to a smooth proper integral model, and its pure kernels have explicit balanced Poincaré
    representatives (SGA 7 I VIII).

**The main question (1.7) is still PARTLY PROVED.** The gate is the common arithmetic datum and its class-kernel/covolume
match, as the review says.

**The project's terms.** THETA3 still cites cote 44 "scans 7–8" and cote 16 "scans 43–46". Those are folios; ours are 008–009
and 044–047. This is unchanged from parts 1–2.

## 2. Hexagon

No candidate. C25 with C27 is a clean, explicit test case, but the run is still going, and the goal (a nonzero ball-derived
Weil projection on C25) is open. H12 and H04 are not affected.

## 3. Prompt update

The decisive next step is now concrete: compute Hom_K⁰(Alb X, A) and the quartic F_X of C27 for one cover X of degree
≤ 43264 over the C25 target. A nonzero value gives the first theta-derived exceptional Weil cycle on a non-CM fourfold.
