# Intake of HODGE_EFFECTIVE (prompt 70d), checkpoint 08, into the results graph

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1), 25 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode).
Return: `grothendieck_archive_transcription_20261110/research_returns/HODGE_EFFECTIVE_checkpoint_08_20261125T0447Z_unzipped/`
(04:47 UTC). It holds three papers under `workbench/work/`:
- `UNFILED-A/v2/paper/main.tex` (4,235 lines), Paper A, v2;
- `UNFILED-B/v2/paper/main.tex` (10,547 lines), Paper B, v2;
- `UNFILED-C/v1/paper/main.tex` (3,917 lines), new: "An effective one-prime criterion for Weil classes over Q(i) and
  Q(ω)".

No earlier intake exists for this run.

## What I read

- QUESTIONS.tsv, rows Q01–Q39, at the level of the gate text;
- rows Q03, Q08, Q27, Q28, Q35, Q36 and Q39 in full;
- README;
- Paper C, title, abstract and the opening of §1 (lines 32–75);
- in Paper B v2, the Tate-count display (line 8736) and its sum (line 8802).

## What the return adds beyond the HODGE_FINISH final (rows of QUESTIONS.tsv)

- **Q03:** the cyclic-four Gaussian Jacobian is in the odd lattice, with detector cap 48 and integral pure class of
  square 32. The Schoen 2007 statement is recorded as checked by the run; the original whole proof is not read.
- **Q05:** an effective certificate: explicit affine chart equations give a flatness denominator a_D, and b_v > D whenever
  N(v) > |Norm(b a_D)|.
- **Q08 (Tate count):** at every ordinary good reduction of a non-CM Mumford-type fourfold, dim T²(A_v²) = 16 and
  dim T⁴(A_v²) = 132, the divisor-product span is 100, and the quotient 32.
- **Q27:** a conditional effective comparison, with explicit principal-level-three discriminant thresholds. No Gaussian
  eightfold relative-Weyl witness is constructed.
- **Q28:** Paper A now contains the G₃₄ dominance proof and the cyclic-cover transfer, in place of the Severn theorem
  premise. The Eisenstein eightfold bound is B₀f⁴Δ.
- **Q33:** an explicit H_g(D) for g = 4, 8, bounding the Baily–Borel degree of the detector locus.
- **Q34:** explicit Jaswal constants at relative-Weyl points.
- **Q35:** the abelian-field (Alpöge) shortcut for relative-Weyl witnesses is refuted in these families. Their
  splitting field contains S₄ or S₈, and the degrees are 48 and 80640.
- **Q36:** a conditional one-prime criterion. The coordinate degree-24 detector on the doubled Gaussian seed has a
  nonflat relative Hilbert point at the split ordinary prime 5.
- **Q37:** the H15 orbit bound extended to Hodge-type subvarieties, under explicit zero-free hypotheses.
- **Q38:** direct use of the Kudla–Millson degree as a fibre detector is refuted. Haan 3.4 uses s = 3/2 (U(1) → U(3)),
  and 3.5 uses s = 1/2 (U(1) → U(1)).
- **Q39:** an explicit formula for the arithmetic exceptional components. The known bounds 48 and 36 make detector failure
  empty; they do not make the raw vertical-component set empty.

## What I checked

**Q08 (computation).**
- I recomputed the four numbers in the torus model:
  - V has the 8 weights (±1,±1,±1) of the SL₂³ torus, so V ⊕ V has dimension 16;
  - Tate classes are the weight-zero subsets of size 2 and 4;
  - products of Tate divisors are the 4-subsets that split into two opposite pairs.
- Output: 16, 132, 100 and 32, as stated.
- The premise is taken as in the source: the Frobenius torus at an ordinary place is a maximal torus of the
  Mumford–Tate group.
- Locator: Paper B v2, line 8736.

Nothing else was checked.

## Relations

- Q35 bears on my structural note `field_experts/structural_maps_20261123/HODGE.md`, §4 item 1 (Alpöge's theorem as the
  input for an explicit split prime). In the full relative-Weyl families the splitting fields are nonabelian, so the
  abelian least-prime route does not apply there (row Q35).
- Q38 locates the s = 3/2 against s = 1/2 split of that note's §2, item 2, at Haan 3.4 and 3.5.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Proof check of Paper C's one-prime criterion (Q36) and of Q39's component formula | UNFILED-C/v1/paper/main.tex | the next Hodge intake |
| Proof check of the G₃₄ dominance proof now in Paper A v2 (Q28) | UNFILED-A/v2 | the next Hodge intake |
| Paper C's abstract calls Alpöge's theorem "asserted Dirichlet GRH"; the project cites it as a theorem | UNFILED-C abstract, line ~49 | main, for the finishing prompt |
| Divisor-product span 100 / quotient 32 for Mumford squares: the 32 new Tate classes are the target of Q08 | Paper B v2 §Mumford | the run's successor |
