# Sweep 1, scope s6: corrections and refinements

Claude Opus 5.5 at effort max (sweep 1, scope s6), 18 Nov 2026. Each item gives the row, what is wrong or can be
sharpened, the fix, how sure I am, and what I read. "Register row" means the one-line statement in
`results_register/REGISTER.tsv`. The check events are in `CHECK_EVENTS.tsv`. Nothing outside this folder was changed.

Abbreviations: S6_06 = S6_06_BLIND (GPT-6 Astra, ChatGPT Pro mode); its report is the cp35 report of 18 Nov 12:08 UTC.

## 1. S6_04 D.2.11: the blind run's "disagrees" is against a summary that drops a hypothesis

- **Row.** S6_04_MAPS_MANIFOLDS:D.2.11 (OS49, IV* + II + I_2, Q = 3P). Register row: "general admissible n has
  pi1 = H1..H4 = Z/|n|". S6_06 P3F.29, P3F.33, P3F.34 "disagree": for a free cap, H_2 = H_3 = Z/|n| + Z/g with
  g = gcd(3k, n, 3d) in {1, 3}; the free cap (m, n, d) = (9, 3, 1) has H_2 = H_3 = (Z/3)^2.
- **What I found.** The theorem as printed (S6_04 `sections/manifolds.tex` l. 2156-2185) assumes gcd(n, 3k) = 1.
  Then g divides gcd(3k, n) = 1, so the blind formula gives H_1..H_4 = Z/|n|, exactly D.2.11. The counterexample
  (9, 3, 1) has gcd(n, 3k) = 3 and lies outside D.2.11. The two runs agree on D.2.11's scope; S6_06 extends it to every
  free cap (P3F.33: free exactly when gcd(k, n, d) = 1 and 3 does not divide n or 3 | k), where the Z/3 appears.
- **Fix.** Restore "gcd(n, 3k) = 1" in the register row and the results table. Record P3F.34 as the general statement
  and D.2.11 as its case g = 1 (MERGES.tsv). The blind report's verdict should read "agrees on D.2.11's scope; extended
  to non-coprime free caps". This is the "noncoprime correction" of the S6_10 layout design: a new case, not an error
  of S6_04.
- **Wider point.** The blind prompt's stated values were these one-liners. Several of the 137 "undetermined"
  comparisons say so themselves ("the supplied statement does not specify ...": S6_04 D.2.2, D.2.27, D.2.49, D.2.50,
  B.6.10, B.6.17, B.6.20). A comparison prompt should carry the printed statements.
- **Sure:** high. **Read:** S6_04 manifolds.tex l. 2156-2200; register rows P3F.29, P3F.33, P3F.34, D.2.11; the cp35
  report's stated-value table.

## 2. The Theta_7 zero statements hold for the reference fan only

- **Rows.** S6_02_PUSH C.3.24, C.3.27, C.4.1, E.1.3; S6_04 B.6.2, B.6.21, B.6.24, B.6.25; S6_06 P3F.17, P3K.7, P3K.8 and
  the retained part of P3F.25.
- **What is wrong.** They say the positive-loop monodromy of the (3,4) family, of all its twist data and of every
  coprime (3k,4l) family is 0 in Theta_7 = Z/28. S6_06 computes the class for other periodic unimodular cusp fans,
  which give other holomorphic families of complex structures on S^6 (P3F.35: diagonal flops preserve the sphere):
  - the original K = L = 1 shorter loop on the fan T_2 has class 26 (P3K.74);
  - P3K.73 gives every fan for the original positive loop; 28 fan witnesses realize all of Theta_7 (report, item 3.1);
  - OS49 on the negative fan T_-: class -3k for the r-loop, -k for the w-loop, 27 at k = 1, every residue as k
    varies (P3K.65); on T_+ the class is 0;
  - primitive OS45: 3; weighted OS47: 4 (P3F.25, corrected); Liu-Rollenske u = w^2 on T_2: 26.

  The run's report: "The broader all-fan zero assertion is false."
- **Fix.** Add "for the cusp fan of [AC26] (the reference fan)" to every zero statement above. S3.4 then reads:
  - the reference-fan class is 0, by three methods in two runs and blind in a third;
  - S6_06 claims families with every class of Theta_7;
  - the classification by fan and source is open (P3K.75).
- **Sure:** high that the hypothesis must be stated; the run says so itself. The nonzero values have been checked by
  no one outside S6_06. Item 3.4 of its report is INCOMPLETE, and its signs were corrected once already, on 17 Nov
  (item 4). They are the most important unchecked claim of the S6 line.
- **My check (computation).** J = (p_rel - 12 s_delta)/24:
  - with C.3.18, C.3.21 and P3F.10: (-24 + 24)/24 = 0;
  - for (3k,4l), with P3F.17: (-24kl + 24kl)/24 = 0;
  - for OS47, with P3F.21: (-72 + 168)/24 = 4, the corrected class of P3F.25.
- **Read:** register rows; cp35 report, items 3.1-3.4.

## 3. Pairs (k, l) shown in the dual-line convention

- **Rows.** S6_04 B.6.17 (p_1 = -4y), B.6.20 (l = -4, k = -1); S6_06 P3K.9 ((k,l) = (-6,-24), then (-1,-4)), P3K.11
  ((k,l) = (-KL,-4KL)).
- **What is wrong.** These are the values for the meridian-one Thom line U = M^-1. For the physical line M the pair is
  the negative: (1,4) for the original return (P3K.68; report, item 3.3).
- **What is not affected.** The index A = (4k - l)/24 changes sign under (k,l) -> (-k,-l), so its vanishing is
  convention-free. The class 0 of item 2 stands.
- **Fix.** State the convention in each row, preferably the physical one.
- **Sure:** high. **Read:** register rows; the report's stated-value table for B.6.17 and B.6.20; P3K.68.

## 4. S6_06 keeps 33 refuted rows that also carry the corrected statements

- **Rows.** The 33 Refuted rows of S6_06 Part 3, among them P3F.25, P3F.53, P3K.6, P3K.10, P3K.17, P3K.22-P3K.25,
  P3K.27, P3K.29-P3K.37, P3K.40, P3K.41, P3K.43-P3K.46, P3K.50, P3K.52, P3K.54 and P3K.56-P3K.60. (The other two
  refuted rows of the run, P1.5 and P2.11, are pure refutations.)
- **What is wrong.** Each row opens with a "Physical-line correction", "Audit correction" or "Proved counterexample"
  of 17 Nov, and then keeps the refuted historical claim. The corrected statement has no tag of its own; it lives in
  the row's opening lines and in K68-K69. This produces 60 of the 73 "proved item cites a refuted row" flags of the
  scope.
- **Fix (register, sweep 2).** Give each correction its own item:
  - the corrected statement, status Proved, citing P3K.68/69;
  - the historical claim marked refuted, with "refined item: <new tag>";
  - dependents re-pointed to the new item.
- **My verdicts on the 73 flags** (FLAG_VERDICTS.tsv). I found no inconsistency.
  - In 16 the citing row uses a pure refutation.
  - In 54 it uses only what the correction retains (constructions, topology, page squares, zero classes), or reaches
    K68/K69 directly or through another row.
  - P3K.9 and P3K.11 need their (k,l) restated (item 3).
  - P3K.28 invokes K68 in its text but not in depends_on.
- **Sure:** high for the structure. The verdicts rest on the statements, not on the proofs.

## 5. S6_05 C.5.1: the one-line summary reads against the torsion locus

- **Row.** S6_05_ARITHMETIC:C.5.1, register row "CM and torsion occur only at completed special fibres 0,1". Read
  literally, it contradicts S6_02_FAMILY D.1.2 (dense countable torsion locus) and S6_05 C.4.3.
- **The printed statement** (S6_05 `sections/C_special.tex` l. 766-772): no t outside {0,1} has E_t with CM and P_t
  torsion at once; at t = 0, 1, after base changes of orders 3 and 4, the limiting points have orders 3 and 2. The
  source is Bourdon-Clark-Stankewicz 2017, Thm 4.15(a), arXiv:1411.2742v3 p. 23.
- **Fix.** Reword the row: "simultaneous CM and torsion occurs only at the completed fibres t = 0, 1".
- **Sure:** high.

## 6. S6_03 C.2.INT.3: the summary omits b_2 = 0

- **Row.** S6_03_CDP:C.2.INT.3, register row "Every reducible torus fibre has nonnegative Euler number".
- **What is wrong.** Unrestricted, this is false: C2b, C.2.UN.2 and C.2.UN.4 give negative even Euler numbers by
  vertical blow-ups. The theorem (S6_03 `sections/part_C2_interfaces.tex` l. 379) assumes the hypotheses of C.2.INT.2,
  that is H^2(Y;Q) = 0. With that hypothesis there is no conflict.
- **Fix.** Add "for Y with H^2(Y;Q) = 0" to the row.
- **Sure:** high.

## 7. S6_04 D.2.24, D.2.27, D.2.28 hold in a sector that the rows do not name

- **Rows.** D.2.24 (no homotopy six-sphere from the I_3* profiles), D.2.27 (none from the three I_1* profiles) and
  D.2.28 ("5 admit none").
- **What is wrong.** All three hold in S6_04's natural filling sector, the natural section-line initial rows of
  D.2.22. S6_06 P3F.36 and P3F.38 build spheres from I_1* sources with the corrected line O(aG - O - L_0), which lies
  outside that sector.
- **Fix.** Name the sector in the three rows. The five-profile count holds relative to it.
- **Sure:** medium. I did not read S6_04's definition of the sector. **Read:** register rows; the report's
  stated-value table for D.2.27, D.2.49 and D.2.50.

## 8. The combs: scope and the Kuranishi space

- **Rows.** S6_01 E2.1-E2.4 (combs with m >= 12, from Viaclovsky's theorems) and S6_03 E15 ("positive combs").
- **What E15 adds.** It gives h(T) = (2m+1, 8m+1, 6m+1, 0) and a smooth miniversal germ of dimension 8m+1. At m = 12
  that is 97, the top of S6_01 E2.3's bracket 88 <= dim Def <= 97.
- **Fix.**
  - E15 should state its range of m and its source for R^1 f_* O.
  - S6_01 E2.3 should read: settled by S6_03 E15 for the Kuranishi space; still open, the exact h^{1,1} and h^{1,2}
    (that is, h^0(K_m)). S6_01 E2.2 gives the strongest proved bounds, h^{1,1} >= 4m+1 and h^{1,2} >= 4m.
- **Sure:** medium. I did not read E15's proof.

## 9. The corner coefficient is -pn

- **Row.** S6_06 P2.2: Delta_R F = a n gamma - 6an(n-1) delta with a = -p (P2.1), so the radial class mod delta is
  -pn gamma. The readers' lead in the S6_06 prompt had +pn.
- **Effect.** S6_02_PUSH B.4.33 and S6_06 P2.7 need only pn != 0. No theorem changes; the handbook item for the corner
  must carry the sign.
- **Sure:** high. The arithmetic follows from P2.1 and P2.2.

## 10. The rank of the fourfold's subbundle

- **What S6_06 found.** P1.5: the formula handed to the blind run, P = image of l_0 ^ H with H the rank-two Hodge
  bundle, gives a subbundle of rank two, not three.
- **The conclusion stands.** With the corrected rank-three P (P1.5, P1.8), S6_04 F.3.6 holds: global holomorphic
  periods with transversality.
- **Fix.** Check whether S6_04 F.3.6's own text has the slip, or only the prompt's summary. The handbook should use
  the P1.5 form.
- **Sure:** medium. I did not read S6_04 F.3.6.

## 11. What "the fibre-product fourfold" is

- **Rows.** S6_04 E.1.1-E.1.4.
- **What I found.**
  - The literal fibre product X x_P1 S is singular. At the double curves of W it is locally xy = uv, times a line.
    Its Euler number is e(W) e(I_1) = 2.
  - E.1.1 refutes the literal normalization. The fourfold Z of E.1.2 is a small resolution, whose cusp is the
    index-one Kuhn fibre of E.1.3 (Euler number 6), so chi(Z) = 6 (E.1.4).
- **Fix.** Name Z the resolved fibre product. Its chi = 6 comes from the resolution.
- **Sure:** high on the count (computation in CHECK_EVENTS.tsv).

## 12. Notation for the handbook's one notation

Some letters carry several objects across the runs. Fix them before sweep 3:

| Letter | Objects | Proposed |
|---|---|---|
| M | the admissibility constant -(3/pi) log 6 | M_adm |
| | Engel's line bundle O(P - O) | L_E |
| | the fourfold | M_c |
| | the physical circle line | L_phys |
| W | the cusp fibre of X | W, kept for the cusp only |
| | the exterior square in S6_06 Part 1 | another letter |
| | Wang's family | another letter |
| P | the Mordell-Weil generator | |
| | the rank-three bundle of Part 1 | |
| | the fan matrices | |

**Sure:** high. This is a matter of presentation.

## 13. Corrections to the literature, confirmed in two runs or more

These belong on the outreach list (memory informing-authors):

| Statement in the literature | Status | Rows |
|---|---|---|
| [E26] Conjecture 8.2, as worded | Refuted by an Euler-number count | S6_02_PUSH A.3.2; S6_06 P2.11, blind, agrees |
| [E26] Remark 8.3 | The literal continuous extension fails | S6_04 A.1.2 = S6_02_PUSH C.3.12 |
| HKP Corollary 1.3, h^0(T) <= 2, repeated in [AC26] Remark 9.26 | False for the combs, whose h^0(T) = 2m+1 | S6_01 E2.4; S6_03 E15 |

Single-run:
- [E26] Remark 8.1: global descent over the u-disc is false, and the double-cover family corrects it
  (S6_02_FAMILY B.2.3).
- [AC26] Remarks 1.3 and 9.21: the torsion of Omega^1_{X/B} (S6_01 A4.2; also the workbench survey).
- Biro 2026, Conjecture 1: false as printed (S6_05 A.5.7, side lane).

## 14. Dependency hygiene

The 22 dependency flags of the scope (FLAG_VERDICTS.tsv) sort as follows. A script can resolve them in sweep 2.

| Kind | Count | Cases |
|---|---|---|
| The run's own section | 12 | |
| Typos | 3 | B6.22/B6.20, D2.16, D2.20 |
| Labels of the return with no register row | 2 | S6_04 E.2.6 "B.5.13", E.2.14 "B.5.16" |
| Literature | 3 | Demailly II.4.19 and 7.6; Banica-Stanasila III.4.10 and 4.12; Gross-Zagier I.(7.3) |
| Other runs | 2 | "K13 A2.2, A4.1" = S6_02_PUSH A.2.2 and A.4.1; "S6_02 B.4.2" = S6_02_FAMILY B.4.2 |

## 15. Register currency

- The register holds S6_06 cp33. cp35 (12:08 UTC) adds P3K.113-P3K.116 and rewrites P3K.75; I placed the four new
  rows, marked cp35 only.
- The register's `ret` and `results` paths for S6_06 point to the cp33 folder, which now sits under cp35's
  `_from_earlier_checkpoints/`.
- **Fix.** Rebuild on cp35 or on the final.

## 16. Q03_DEPOSIT is not S6

- **What it is.** Its 47 rows are the deposit post for Pm | prec, p_j = 1 | C_max (polynomial for every fixed m >= 3),
  a scheduling result. They are filed in the S6 line only because the files sit in `s6_pro_prompts_*`. I placed them in
  a separate part Q.
- **Its checks.**
  - One peer review: Claude Fable 5.2 at effort max, 15 Nov. Targets A and B were confirmed, and the review says it
    is "not a line-by-line re-proof of Sections 2-8".
  - Before it, three checks of the 23 Oct return by Claude Opus 5.5 at effort max (Message Batches API): one "proved
    with fixable gaps", two "proved as stated".
- **Fix.**
  - Give it its own tag space.
  - The claim is of a size that calls for a full line-by-line referee check before any deposit.
  - The open-problem history should be stated in the item with citations, not from memory.
- **Sure:** high on the placement. I did not check the proof.
