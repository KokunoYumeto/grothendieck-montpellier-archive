# Corrections and refinements found in sweep 1, scope `sections`

By Claude Opus 5.5 at effort max (sweep 1 over the register, scope `sections`), 18 Nov 2026. The returns are by GPT-6 Astra
(ChatGPT Pro mode); the earlier readings cited are by Claude Fable 5.2 at effort max (ab3f12f2, a2fedc2a) and Claude Fable
5.2 at effort high (the LM6 intake). Each item gives the rows, what is wrong or can be sharpened, the fix, how sure I am, and
what I read. My own checks are in `CHECK_EVENTS.tsv`. Nothing outside this folder was changed.

Most weight first.

## 1. Results conditional on Tool (1) are registered as Proved

- **Rows.** LM6_POINTS_AS_SECTIONS B.7, B.15, B.19, B.29, B.30, B.32, B.33, B.35, B.38, B.39, B.40, B.41, F.31, the last
  two sentences of E.12, the last assertion of A.3 (and B.37, whose notes name the stipulated input); FERMAT_SUCCESSOR A.20
  and A.31. Two more rest on another stipulated input, "the specified universal-curve input": LM6 B.18, B.23. FERMAT_SUCCESSOR
  C.13 rests on the unrefereed existence inputs LM7_PUSH D.20, D.21, D.51, D.52 (FERMAT_SUCCESSOR report, R16).
- **What is wrong.** Each of these is proved from the p-adic local section theorem stipulated by the prompt (Theorem 1.1 of
  the unrefereed OpenAI preprint of 6 Oct 2026, called Tool (1)). The runs say so ("Printed qualification: Proved using the
  prompt's local theorem"; "Proved, conditional on the stated local theorem"). Sweep 0 normalizes the status to Proved, and
  the qualification is lost. Among the consequences: "every section of Y_1(N) over Q is cuspidal" (B.15) and "the section set
  of U_n/Q is the three cusp packets" (E.12) are conditional. The intake of 14 Nov reported B.15 without the condition.
- **Fix.** Status "Conditional (Tool (1))" for these rows. In the handbook they go in the conditional environment with the
  hypothesis named, and their consumers inherit it. The sweep-0 builder should map a status or qualification containing
  "conditional", "using the prompt's local theorem" or "stipulated" to Conditional.
- **How sure.** High: the rows' own words. The list is by keyword over statement, notes and dependencies, read row by row.
  It may miss a row whose proof uses Tool (1) without saying so.

## 2. LM6 E.8: a false step in its proof (and in the preprint it follows); the statement survives

- **Rows.** LM6_POINTS_AS_SECTIONS E.8 (Known, "after Steklov's preprint"), used by E.9 and E.12; FERMAT_SUCCESSOR A.3, A.4
  (Refuted), A.5, A.6, A.8, A.9, A.11.
- **What is wrong.** The proof asserts that the residual cusp class is divisible by ℓ. The Tate parameter of the Legendre
  curve at λ = 0 is q = (λ²/256)(1 + λ + O(λ²)). For λ = u^ℓ the cusp class is 2ℓκ(u) − 8κ(2) (up to a principal unit), and
  v₂(q) = 2ℓ·v₂(u) − 8 is prime to ℓ for every odd ℓ. So the class is not divisible by ℓ at 2. FERMAT_SUCCESSOR A.4 refutes
  the step (ℓ = 5 over Q₂) and with it the general ramification-divisibility proposition of Steklov, *Fermat's Last Theorem
  for Selmer Sections*, arXiv:2602.17746v1. The conclusion of E.8 survives: A.3–A.6 give the corrected local twists, of Serre
  level 2. A second error of the same preprint is the claim Y₁(7)(Q) = ∅. LM6 E.10 and FERMAT_SUCCESSOR A.9 refute it: the
  point (0,0) on y² − xy − 4y = x³ − 4x² has exact order 7. (X₁(7) has genus 0, so Y₁(7)(Q) is in fact infinite.)
- **Fix.**
  - E.8 becomes "Proved (repaired)": its proof locator moves to FERMAT_SUCCESSOR A.3–A.6, and the handbook item carries a
    warning that the cusp class is not divisible by ℓ.
  - E.9, E.11 and the first sentence of E.12 are merged into FERMAT_SUCCESSOR A.8, A.10 and A.11 as their canonical proofs.
    FERMAT_SUCCESSOR A.6 is marked Known in its run, but it is the run's own repaired argument from Khare–Wintenberger, Kisin
    and Serre, so its status should be Proved.
  - For outreach (drafts to the user first): both errors bear on Steklov's preprint.
- **How sure.** High on the constant 1/256 and on the order-7 point; I checked both by computation. I did not recompute the
  ℓ = 5 tame matrices. Whether Steklov's proposition is word for word what A.4 refutes rests on FERMAT_SUCCESSOR's reading of
  the preprint; I did not open it.
- **Read.** Register rows. FERMAT_SUCCESSOR report: corrections, and the audit of R1–R20 (R3, R5). The LM6 intake of 14 Nov.
  SECTION_GHOSTS references.bib (Steklov2026).

## 3. LM6 E.12 is three statements; split it, and state the priority question exactly

- **What is wrong.** E.12 joins three statements with three different standings:
  - **(a)** every Selmer section of the plus Fermat curve U_n/Q is cuspidal, for odd n ≥ 3. This is proved, and re-proved by
    FERMAT_SUCCESSOR A.11 on the repaired route. FERMAT_SUCCESSOR A.16 extends it to the classical curve C_n for every n ≥ 3,
    with four cusp centres for even n.
  - **(b)** for even n the plus curve has no section at all. This is proved: for even n, X^n + Y^n + Z^n = 0 has no real
    point, so there is no real section. SECTION_GHOSTS E.100 strengthens it: there is no section already of the
    geometrically pro-2 abelian extension.
  - **(c)** every section is Selmer, hence the section set is the three cusp packets. This is conditional on Tool (1)
    (item 1).
- **Priority.** SECTION_GHOSTS C.5 cites Steklov 2026, Theorem A and Theorem 5.14, for prime exponent ≥ 7 (opened by that
  run on 18 Nov). Composite n with a prime factor ≥ 7 follow through U_n → U_ℓ. Exponent 3 goes through X₀(27) (LM6 E.11,
  which cites Kriz–Li 2019).
- **Fix.**
  - Three handbook items with three statuses: (a) proved, (b) proved, (c) conditional.
  - The new content against the literature is stated per exponent: ℓ = 5, the powers of 3 and 5, and the repaired step for
    ℓ ≥ 7 (Steklov's printed proof uses the two false claims of item 2). Check Steklov's Theorem A and Kriz–Li before any
    claim of novelty. Memory superseded-results-not-posted applies to the prime exponents ≥ 7.
- **How sure.** High on the split; medium on exactly what Steklov's Theorem A covers (not opened by me).

## 4. A1 is settled; three open rows of the line are stale

- **Rows.** ANABELIAN_149_PUSH A.30 (Unresolved: universal A1), A.C2.6 (Unresolved: the odd-torsion route in genus two over
  F̄₂) and A.C2.22 (46 of 48 classes); FLAGGED_149 B9 (Open: the prime-to-p point question). All four are covered by
  ANABELIAN_SUCCESSOR A.3 = ANABELIAN_A1 A.1 = ANABELIAN_A1_SUCCESSOR A.1. The extension to every hyperbolic curve over a
  finitely generated field of characteristic p is ANABELIAN_A1 A.33 (A.R5), read as sound by a2fedc2a.
- **Fix.** In the handbook these become "settled by ANABELIAN_A1_SUCCESSOR A.1", with a dated history entry; MERGES.tsv
  records them as weaker members.
- **The check record of A.1.**
  - Claude Fable 5.2 at effort max (ab3f12f2, a2fedc2a) read the whole chain as sound (pro_intake_20261116 and
    pro_intake_20261117).
  - The run's own successor added the finite certificate the expert asked for. ANABELIAN_A1_SUCCESSOR A.50: a cyclic
    19-cover over F₈ separating P = (0,1) and Q = (1,0) on y² + x(x+1)y = x⁵ + 1, with odd relative class number. B.85: a
    cyclic 3-cover over F₁₆ with relative class number 81. B.88: a pro-3 separator of degree 3⁷.
  - It also added the non-nilpotent test of A.CF2 (A.51: a quotient of order 75 with a non-central cusp).
  - It replaced the route through Saïdi–Tamagawa's finiteness theorem by a direct characteristic-p route (A.13–A.21,
    A.42–A.49, B.68).
- **What is still missing.** A line-by-line reading of A.CF1–A.CF2 by a reader outside both families, the experts' first
  item. All of the successor's checks are GPT-6 Astra (ChatGPT Pro mode) readings, as its report says.
- **How sure.** High that the rows are the same assertion. The correctness of A.1 is as the two Fable readings and the
  certificates stand.

## 5. Open or Refuted rows that contain proved results, used by proved rows

- **LM6 F.24 (Open).** Its proved half, that the local conditions characterize the geometric tangent subtorsor over Q
  (Prop. F-local-global-units), is what F.39, F.45 and F.46 use. Its open half is the residual defect Ê/E over a general
  number field. Split it.
- **LM6 D.8 (Open).** It contains the proved Proposition D-literal-minimum, which D.10 uses. Split it.
- **LM6 C.12 (Open).** It contains a fibre calculation, which C.15 uses. **LM6 A.22 (Open)** contains proved restrictions on
  candidates, which A.52 uses. Split both (statement level).
- **FLAGGED_149 D7 (Refuted).**
  - Its DVR assertion is true: centre ⟺ trivial inertia image, for elementary towers without fibres of type (0,0) or (0,1).
    ZD3 uses it, and ANABELIAN_A1_SUCCESSOR B.102 re-proves it and extends it to every ordered rank when the divisible part
    of the value group vanishes.
  - Only the arbitrary-valuation converse is false.
  - Split D7 into D7a (proved, canonical B.102) and D7b (refuted; refined by B.102's value-group condition, with B.99 the
    counterexample).
- **How sure.** High for F.24 and D7 (their own text says so); medium for D.8, C.12 and A.22 (statement level).

## 6. Δ on GT̂: a not yet taken-in return claims to settle it

- **Rows.** LM7_PUSH E.3 (Open) and FERMAT_SUCCESSOR C.15 (Open) ask whether full GT̂ reaches the extra CM coset, that is,
  Δ on GT̂. SECTION_GHOSTS E.191 (Proved) states Δ|GT̂ = 0, for "the historical continuous character Δ: GT̂₀ → F₂ with
  the literal signed pure frames of E.95": the vanishing clause of GT_TOWER_CHECK A.7, which checks EXIT_TOWER E.49. E.198
  adds GT̂ ⊊ ker Δ ⊊ GT̂₀, with a full profinite witness (the square of E.197's element, detected in an 11-primary nilpotent
  quotient of the five-point group).
- **What to settle.** Whether E.95's signed frames give the same character as LM7_PUSH E.61/E.65's CM parity. E.201
  reconstructs LM7 E.58's identity-relative family, which suggests that they do. If they do, E.3 and C.15 are settled
  (Δ|GT̂ = 0), and the programme map's main question E.3 is answered as EXIT_TOWER E.49 claimed.
- **Fix.** Route this to the GT field expert (registry), not to a new agent. Until then MERGES.tsv carries it as "stronger,
  if the characters coincide".
- **How sure.** Low to medium on the identification (statement level only). This is the item with the most consequence in
  my scope.

## 7. Scope corrections between runs, from SECTION_GHOSTS (final)

- **SECTIONS_OVER_Q A.207** and the order-32 exclusion concern locally point-or-cusp-matching sections. They may not be
  entered as unrestricted class-two or class-four failures (SECTION_GHOSTS B.2).
- **SECTIONS_OVER_Q A.196.** Its example is nonordinary at 3 and lives over a cubic field. Every finite class-three quotient
  lifts while the continuous one does not, but the example is not an ordinary ghost over Q (SECTION_GHOSTS E.43,
  E.166–E.169).
- **GT_TOWER_CHECK C.3.5** (outside my scope). Its full-pro-3 reading is refuted for a dense set of outputs; the original
  compact-test claim stands (SECTION_GHOSTS E.120–E.121).
- **"Lead L2".** The compactness of varying ghost families is false (SECTION_GHOSTS A.101). Compactness over a fixed abelian
  cocycle holds.
- **The prompt's R8** (the universal Fermat reading of LM6 E.16 and E.31–E.34 as ordinary tripod pairs) is false. Those
  families are nonordinary already at 2 (SECTION_GHOSTS E.98–E.100).
- **Fix.** Carry these as "refines" or "refuted by" in the items (MERGES.tsv), and state each statement's quotient and local
  condition in the handbook.
- **How sure.** High that the runs say so (the final's `checks` column). I did not check the proofs.

## 8. Corrections in FERMAT_SUCCESSOR's audit of R1–R20, besides item 2

- The Gaussian quartic quotients have CM by Z[i], not Z[√−2] (A.12).
- Stoll's finite-support step needs all-place descent; density one concerns only the supporting subscheme (A.2; Stoll's
  erratum read by the run).
- R17: the unrestricted next-layer exclusion of LM7_FERMAT_TOWER D.45 fails once cusp conjugation is allowed (C.25).
- R18: the obstruction excludes Galois-commuting third-derived lifts, not arbitrary peripheral lifts (C.14).
- R19: the density-intersection inference in Porowski's global argument has a gap. Two disjoint Chebotarev sets of density
  1/2 refute it, and strong positive upper density repairs it; no counterexample to the geometric theorem is claimed (A.22).
  This is a literature item for outreach, drafts first.
- **How sure.** As the run states them; not checked by me.

## 9. The register itself (sweep 0)

- **Stale run.** The SECTION_GHOSTS final arrived at 13:05 UTC and was unpacked at 14:20, after the register was built
  (14:06). The checkpoint-7 folder the register points to has been retired. The final adds 18 rows (P.15, P.16,
  E.203–E.218), with no status change. Rebuild the register. PLACEMENT.tsv already places the 18 rows.
- **Escaped underscores.** "SECTIONS\_OVER\_Q A.44" in the TeX of statements defeats the lineage regex. Only 37 "names"
  edges were found in my scope, against 168 checked relations in SECTION_GHOSTS alone. Normalize `\_` to `_` before
  matching.
- **False within-run edges.** SECTION_GHOSTS audit rows cite other runs' ids that collide with its own (C.4's "A.7" is
  GT_TOWER_CHECK A.7; E.2's A.25, A.32, A.42, A.44 are SECTIONS_OVER_Q's). The builder resolves them to SECTION_GHOSTS rows.
  The final's CSV has a `checks` column naming the run; read it. In general, resolve a token to the run named nearest before
  it in the dependency text.
- **Abbreviated cross-references** ("AS-A.3", "AN D.30", "LM6-E.8", "LM7 D.61", "F149-F17.7") are not resolved. The flag
  verdicts resolve those of my scope.

## 10. One object, several names (for the handbook's single notation)

- **The Fermat curve.** The plus curve U_n (X^n + Y^n + Z^n = 0 minus XYZ = 0) and the classical C_n (x^n + y^n = z^n) are
  isomorphic over Q for odd n. They differ for even n: the plus curve has no real point, while C_n has four rational cusp
  centres. LM6 E.12, LM7 and FERMAT_SUCCESSOR use both. Fix one notation and state both cases.
- **A1.** One theorem has six names: A1, AR.3, AS-A.3, ANABELIAN_SUCCESSOR A.3, ANABELIAN_A1 A.1 and A.R1. Prompt item
  labels (A1, A3, A5, A12, B1, B8, N2, N3, N4) collide with statement ids (A.1, A.3, ...).
- **One question each:**
  - N2 = LM6 A.22 = ANABELIAN_A1_SUCCESSOR B.118.
  - Conjecture A for the tripod = SECTIONS_OVER_Q A.1 = ANABELIAN_149_PUSH D.U1 = the first item of LM6 B.27 = SECTION_GHOSTS
    D.3.
  - Birational lifting for the tripod = SECTIONS_OVER_Q B.15 = ANABELIAN_149_PUSH D.U4 = LM6 F.15 = FLAGGED_149 ZD10. D.U2
    is the second half of B.15.
  - Δ on GT̂ = LM7_PUSH E.3 = FERMAT_SUCCESSOR C.15 (item 6).
- **Fix.** One tag for each, with the others as aliases (MERGES.tsv "same").

## 11. Consistency checks that found nothing wrong (recorded so that they are not redone)

- LM7_FERMAT_TOWER E.17 against E.19: different quotients (rank-two toric against pro-3 abelianization).
- LM7_PUSH A.5 against A.17 and A.18: the mixed tame example is class two only and has no metabelian lift.
- The 79 flags "proved item cites a refuted row": every one uses the counterexample, the corrected statement or the object
  of the refutation, never the refuted claim (FLAG_VERDICTS.tsv).
- The 16 proved rows with a register edge to an Open row: none uses the open claim as a premise. They are citations of
  scope, the proved half of a mixed row (item 5), or false edges (item 9).
