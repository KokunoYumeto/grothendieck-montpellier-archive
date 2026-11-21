# Intake of THETA3, part 4: checkpoint 07, the final return (prompt 37)

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 21 Nov 2026, round 5. Part 3 read checkpoint 04. Check
events: `INTAKE_THETA3_20261121_part4_CHECK_EVENTS.tsv`.

## 0. What I read

**The return:** `research_returns\THETA3_checkpoint_07_20261121T0604Z_unzipped\`, from 06:04 UTC. **By the user's rule
of 20 Nov the run has ended at this return**: its newest return is more than three hours old. So this is its final.

**What I read:**
- the `LEDGER.md` headings from review 02 to checkpoint 07;
- the closing paragraph "Checked developments before checkpoint07";
- the QUESTIONS rows added after checkpoint 04 (22 rows) and the four main rows;
- the statements of C32 and C36.

My context is near its limit, so everything is at statement level. **No finding I checked in parts 1–3 is changed or
withdrawn.** Formal reviews 02 (04:49) and 03 (05:49) both recorded MOVEMENT.

## 1. Verdicts (statement level)

**The main rows at the end:**

| Row | Final state |
|---|---|
| Q1 (sketch 1.7) | PARTLY PROVED; an exact finite transform and an analytic rank theorem proved (A1–A15, B9–B29, C37) |
| Q2 | an explicit finite certificate for the actual inverse |
| Q3 | the exceptional target extracted |
| Q4 | the chosen horizontal cycle comparison proved |

**The sketch's 1.7 is still not proved.** The arithmetic MainX matching was never completed. A16 refutes "universal
field-preserving full-host enlargement", with an explicit non-normal quartic CM field.

**C32 is the notable new finding.**
- **Statement:** for the hyperelliptic curves H: y² = z·∏_{j=1}^4 (z² − a_j²), with the order-4 automorphism
  ρ(z,y) = (−z, iy), the Jacobian A = J(H) carries an explicit integral cycle C_A ∈ CH²(A) with
  0 ≠ cl(C_A) ∈ W_{Q(i)}(A) and ∫cl(C_A)² = 73728.
- This family includes C25's simple non-CM fourfold, with End = Z[i] and NS rank 1. The pullback by [2+i] gives the
  second direction of the Weil plane, the same device as HD-G05/Q1-04.
- **Its method is Schoen 1988, Th. 2.0 (p. 11) and Cor. 3.1 (p. 24), in a ramified case with paired branch points.** It
  is not the theta machine. It uses neither Markman nor a supplied Weil cycle.
- So C27's quartic test, which vanishes on the covers in C28 and C30, was bypassed by a Schoen-type correspondence.
- **For our quantity:** C32 gives an explicit detector on a non-CM Q(i) fourfold. With HD-WQ, the Weil classes there have
  explicit division bounds once the degree of C_A is recorded. Only its self-intersection is stated in what I read.

**C36:** product targets in every even dimension built from C25/C32. These are products, so not new exceptional cases
beyond the fourfold.

**C30 and Q3-single-fibration-tower:** refuted with exact Albanese decompositions. Two-base Pryms and single-fibration
towers do not give new sources. This is consistent with my Propositions O and O′ (curve-cover sources reach only n ≤ 3).

## 2. What is new

- **C32:** an explicit Schoen-type exceptional cycle on an explicit non-CM Q(i) Weil fourfold. Its Weil classes are
  already algebraic (Markman; van Geemen and Schoen for Q(i) Weil fourfolds). The explicit cycle and its
  self-intersection are new as an example.
- **For the theta line, the net result:** the analytic side of 1.7 is complete; the arithmetic matching is not.

## 3. The two proofs, and H01

No RH or GRH, no Masullo, no H01. Markman is not used in C32.

## 4. Integration

- **Hodge sketch, Route 1, 1.7:** "THETA3 final (ckpt 07): analytic seesaw and finite transform proved; the arithmetic
  MainX matching is open; A16 refutes universal full-host enlargement."
- **Division attack, §2.1 table:** add "the C25 non-CM Q(i) fourfold: an explicit Schoen-type detector C_A (THETA3 C32,
  statement level)".
- **Scan numbering:** THETA3 cites folios to the end. In our numbering they are cote 16 scans 044–047 and cote 44
  scans 008–009.

## 5. Hexagon

No new candidate stands alone. C32 could join H12 as an explicit example on a non-CM fourfold. The gates: an intake read
of C32's proof; the degree of C_A.

## 6. What the successor needs (the run has ended)

1. **1.7:** choose CM types for which A7's multiplicity space is totally definite. Solve the MainX kernel/covolume and
   terminal-mass equations there (Part II, G1, of the paper).
2. **C32:** state deg_θ C_A. Then apply HD-WQ for an explicit c_t on the C25 fourfold.
3. Write the proofs of A15–A17, B29–B30 and C37–C38 into the paper. Some are saved drafts that were not integrated at
   checkpoint 07.
4. Cite cote 16 and cote 44 by our scan numbers (PDF pages), with folios in parentheses.
