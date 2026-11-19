# Sweep 1, scope s6: summary

By Claude Opus 5.5 at effort max, sweep 1, scope s6, 18 Nov 2026. The harness refused the agent's own write of this
file, so the main session (Claude Opus 5.5 Max) saved it from the agent's final message, unchanged in substance.

The runs are by GPT-6 Astra (ChatGPT Pro mode). The agent read:
- the one-line statements of all 1,124 rows;
- the S6_06_BLIND cp35 report tables;
- the S6 survey and the S6 prompts;
- the printed statements of S6_04 D.2.11, S6_05 C.5.1 and S6_03 C.2.INT.1–3.

It reread no other proofs. The S6_10 papers are out of scope.

## 1. Counts

**Rows.** 1,124: the register's 1,120, plus P3K.113–116, which S6_06_BLIND cp35 added after the register was built on
cp33.

| Run | Rows |
|---|---|
| S6_06_BLIND | 296 |
| S6_03 | 239 |
| S6_04 | 198 |
| S6_02_PUSH | 154 |
| S6_05 | 88 |
| S6_02_FAMILY | 55 |
| S6_01 | 47 |
| Q03_DEPOSIT | 47 |

| Status | Rows |
|---|---|
| Proved | 1,011 |
| Refuted | 70 |
| Known | 33 |
| Open | 8 |
| Other (Q03) | 2 |

**Placement.** 8 parts and 40 chapters: S0–S5 hold 1,041 S6 rows, SZ holds 36 side-lane rows, and Q holds the 47 Q03
rows, which are not S6. 1,083 rows were placed by script and 41 by reading.

**Merges.** 177 links: 114 come from S6_06_BLIND's comparison table, 63 from reading.

| Relation | Links |
|---|---|
| same | 97 |
| weaker | 50 |
| refines | 11 |
| stronger | 6 |
| refuted by | 5 |
| settled by | 4 |
| corrects | 4 |

**Flags.** 95 flags, no inconsistency.
- 73 say "proved item cites a refuted row":
  - 16 use a pure refutation;
  - 54 use only what a correction keeps, or the corrected transfer P3K.68/69;
  - 3 use values that do not depend on the convention;
  - P3K.28 should add K68 to its dependencies; P3K.9 and P3K.11 need their convention stated.
- 22 say "dependency names no id": 12 point to the run's own sections, 3 are typos, 2 are return labels with no register
  row, 3 are literature, and 2 are another run's rows.
- 1,007 say "no check recorded"; they are covered by joining the S6 check ledger in CHECK_COUNTS.tsv.

**Checks per row.** Each count adds up the distinct intake documents, the S6_09 writing run, S6_06_BLIND's blind
comparison and this sweep.

| Run | Mean checks per row | Rows with 3 or more checks |
|---|---|---|
| S6_01 | 2.45 | 18/47 |
| S6_02_FAMILY | 2.51 | 19/55 |
| S6_02_PUSH | 1.53 | 11/154 |
| S6_04 | 1.81 | 15/198 |
| S6_03 | 1.14 | 6/239 |
| S6_05 | 0.88 | none of its 36 side-lane rows has any |
| S6_06_BLIND | 0.29 | 213 of its 296 rows have none |

**S6_06_BLIND rechecking.** All 184 earlier rows it compares had been checked before: all by S6_09, 24 also by an
intake.
- It agrees on 42 and agrees in a narrower scope on 3; 1 is unresolved and 137 are undetermined.
- Its one "disagrees" is against a summary line, not the theorem.
- Its Part 5 rederives what four sources already gave: S6_01, S6_02_FAMILY, S6_03 E9 and DGKX v1.
- Its Part 4.2 rederives S6_03 C.2.G.1 in 78 rows.

## 2. The corrections that matter most (CORRECTIONS.md has 16 items)

1. **S6_04 D.2.11 stands.** As printed it assumes gcd(n,3k)=1, so g=1 and the two runs agree. S6_06_BLIND's
   P3F.33–34 extend it to all free caps, where a Z/3 can appear: (m,n,d)=(9,3,1) gives (Z/3)². Comparison prompts
   should quote printed statements, not one-liners.
2. **Θ₇ = 0 holds for the [AC26] reference fan only.** This covers S6_02_PUSH C.3.24 and C.3.27, S6_04 B.6.2, B.6.21
   and B.6.24, and S6_06_BLIND P3K.7–8. On other fans S6_06_BLIND finds:
   - 26 for the original loop on the T₂ fan;
   - every residue for OS49 on the T₋ fan (P3K.65);
   - 3 for OS45 and 4 for OS47.

   No one outside S6_06_BLIND has checked these. Its report marks item 3.4 INCOMPLETE, and it already flipped these
   signs once, on 17 Nov.
3. **Dual-line convention.** S6_04 B.6.17 and B.6.20 and S6_06_BLIND P3K.9 and P3K.11 give (k,l) for the meridian-one
   line; the physical pair is the negative. Zero classes do not change.
4. **Split S6_06_BLIND's 33 corrected rows into new items** that cite K68/69.
5. **Summary lines that misread their theorems.**
   - S6_05 C.5.1 means CM and torsion together, not torsion alone.
   - S6_03 C.2.INT.3 needs H²(Y;Q)=0.
   - S6_04 D.2.24, D.2.27 and D.2.28 hold only in the "natural sector".
6. **Q03 is a scheduling result, not S6.** It needs its own tag space and a full line-by-line referee check.

## 3. Per chapter

**S0, conventions (11 rows).** The [AC26]–[E26] dictionary: μ is the elliptic logarithm and λ₀=1. DGKX v1 is audited
and agrees.

**S1, one member X_c (74 rows).**
- Proved: the Hodge diamond, h¹¹=2 and h¹²=1, for every member.
- Proved: Frölicher at E₂, the Bott–Chern and Aeppli numbers, and the special metrics.
- Proved: h^i(T)=(1,1,1,0) and a smooth Kuranishi line, from four derivations plus DGKX v1.
- Proved: Aut=C*, twice, once blind.
- Open: C3.8, explicit formulas for G and Q. G and Q are known to exist; only the formulas are missing.

**S2, the family (221 rows).**
- Proved: X_c≅X_c′ exactly when c′−c∈2Z.
- Proved: M=−(3/π)log 6, so the w-disc has radius 216 (Arb-certified, two runs).
- Proved: no extension past |w|=216, and no filling at w=0 (B.4.33, and blind for every twist).
- Proved: [E26] Conjecture 8.2 is refuted, by two runs.
- Proved: the monodromy group Γ is the index-12 kernel.
- Open: the combs' h¹¹ and h¹², bounded below by S6_01 E2.2. Their Kuranishi space is settled by S6_03 E15.
- Open in the register but settled since: S6_02_FAMILY C.3.3, E.1.5 and E.2.3.

**S3, topology (245 rows).**
- Proved: the map to S³ has class 6ν′, and η₄η₅ appears.
- Proved: the reference-fan Θ₇ class is 0, by three methods and once blind.
- Open: P3K.75, every fan for every source. The strongest proved reductions are K73–74 and K88.

**S4, other manifolds (188 rows).**
- Proved: the universal covers are the manifolds M_d.
- Proved: S⁶ arises from III*+3I₁, OS49, Liu–Rollenske and seven further sources.
- Proved: the conifold transition gives S³×S³.
- Proved: Z has χ=6 (as a resolved fibre product).
- Proved: the three-connected fourfold is 3HP²#(−HP²), twice, once blind, with the exotic-sphere ambiguity settled.
- Open: D.2.4, the full classification. The strongest proved reduction is D.2.28.

**S5, CDP after S⁶ (302 rows, none open).**
- Proved: the sign theorem c₃∈{0,2}, in full by S6_03 and blind in the irreducible and normal-crossings case.
- Proved: a threefold with trivial monodromy and c₃=0, by two runs.
- Proved, one run only: a∈{0,1}.
- Proved: the Euler numbers of unrestricted fibres are exactly 2Z.
- Watch: S6_03 D.2.5 in its unrestricted form.

**SZ, side lanes (36 rows, no checks).**
- Proved: exponent 2/3+ε, the mean square and Ω±.
- Refuted: Biró's Conjecture 1.
- Proved: Aut J has order 12,597,120.
- Open: A.5.4.

## 4. Runs not fully taken in before, and what was found

- **S6_06_BLIND** had been read only up to cp11; a Pro intake is running from cp11 on. In it: the fan dependence of the
  Θ₇ class, the physical-line correction, the D.2.11 dropped hypothesis, the sign −pn of the corner coefficient
  (theorem unaffected), and the corrected rank of the subbundle. The register holds cp33, not cp35.
- **S6_04** had only 31 of its 198 rows named in intakes. In it: the sector-limited rows, the dual-line values, what Z
  is, and that D.2.11 stands.
- **S6_05** had only 12 of its 88 rows named in intakes. Its Part C is S6 mathematics, now placed in S2.4 and S2.8; C.5.1's
  summary line misreads; parts A and B have no checks.
