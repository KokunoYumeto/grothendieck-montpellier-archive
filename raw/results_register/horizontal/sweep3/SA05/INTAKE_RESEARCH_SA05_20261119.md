# Intake of RESEARCH_SA05: Grothendieck's "Théorie des motifs I" (cotes 15, 12, 11)

## About this intake

**The run.** GPT-6 Astra (ChatGPT Pro mode) ran on account 1. The prompt was built in
`pro_prompt_builds/RESEARCH_SA05/PROMPT.md`; it has 20 items (A.1-A.5, B.1-B.5, C.1-C.6, D.1-D.4) and the statement
part E.
- It started at about 02:5x UTC on 19 Nov 2026 and saved checkpoints 01 to 09.
- It stopped at its formal review05 (09:50 UTC). This was the second consecutive review without qualifying movement,
  and the prompt's ledger rule required the stop. The session was not cut off. The final is marked INCOMPLETE, with 8
  of its 44 item rows open.

**The return** is at `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA05_final_INCOMPLETE_20261119T0951Z_unzipped`.
It contains:
- the report;
- `ITEM_STATUS.tsv`, with 44 rows;
- the results register `RESEARCH_SA05_results.csv`;
- `CHECK_EVENTS.tsv` (399 KB);
- `LITERATURE_CHECK.tsv`;
- the paper (136 pages by the run's count) and its sections;
- the part notes, `part_a` to `part_d`.

The run had no scans. It worked from our transcriptions and readings, so it makes no palaeographic claims of its own.

**Taken in by** Claude Opus 5.5 at effort max (agent a7b7747fd6dd29f87, which made the sweep-3 reading and built the
prompt), on 19 Nov 2026, finished at about 11:40 UTC. `field_experts/INTAKE_LEDGER.md` (rebuilt 11:19 UTC) has no
RESEARCH_SA05 row, so this is the first intake.

**What I read.**
- From the report: the outcome table, corrections, open work and the stopping decision.
- `ITEM_STATUS.tsv` with all its gates, and the Part A notes.
- The progress reviews in `PROGRESS_LEDGER.md`, and the `LITERATURE_CHECK.tsv` rows for the main locators.
- The statements of A:comparison, A:compacthasse, A:enrichment, A:crystalline, A:real, c:level-counterexample,
  c:fermat-counterexample, prop:d-metabelian-false, ex:B-X011, and thm:B-Sha-corank with its rank remark.
- thm:B-SpecZ-Q, with its proof.
- Our transcriptions of 15:3, 15:7, 15:11 and 12:120.

**Not read:** the other proofs of Parts B-D, the run's code, and the PDF. That was the limit of the compute bound.

**Files beside this one:**
- `INTAKE_RESEARCH_SA05_20261119_CHECK_EVENTS.tsv`: 24 events, INT-SA05-E01 to E24.
- `intake_RESEARCH_SA05_scripts/intake_checks.py`, with its `.out` and `_output.json`: seven independent finite checks,
  all PASS. They neither import nor run any program of the return.
- `intake_RESEARCH_SA05_scripts/write_check_events.py`: it writes the TSV.

## 1. The main question (A.3-A.4): the gerbe of F_p against Langlands-Rapoport and Milne

**A.3, the global class.** All four parts are settled.

- **(a) Proved: Ш²(Q, H⁰) = 0.**
  - For a torus compact over R, Ш² vanishes, and H²(Q,T) maps isomorphically onto ⊕_v H²(Q_v,T) (A:compacthasse).
  - I re-proved this (E01). Complex conjugation acts as −1 on X*(T), so it is central with no fixed vectors.
    Inflation-restriction then makes H¹(Q,X) inject into H¹(R,X), so Ш¹(Q,X) = 0, and ADT I.4.20 gives the rest.
  - For the protorus H⁰, the inverse-limit term vanishes because X*(H⁰) is a Q-vector space (E02).
  - The lim¹ H¹ step is the run's argument ("cofinal division"). I read it but did not re-prove it.
- **(b) Proved:** the μ₂-component is determined by the finite places (Br(Q)[2] and reciprocity; E03).
- **(c) Proved in the form 15:7 actually states.**
  - The bare class ξ₀ ∈ H²(Q,H) determines (M, gradation, augmentation, F₀) up to equivalence, and conversely.
  - It does not determine a choice of local functors. A framed example at p = 2 shows this: Q₃ is twisted by the
    square class 3. The four global candidates ±3, ±6 are each excluded by a residue test at 5, 7 or 13 (computed; E05).
  - 15:7 itself makes the distinction. With the F_ℓ added, he passes to a relative class "ξ ∈ H²(S mod T, H)", with T
    the disjoint union of the Spec Q_ℓ (checked on the transcription; E04).
- **(d) Determined.**
  - At p, the compact component is the functional m ↦ v_p(m) mod Z.
  - The μ₂-components are 1/2 at p and at ∞ and 0 elsewhere: the quaternion class ramified at {p, ∞} (E09).
  - The compact class has infinite order.

**A.4, the comparison.**
- **Strict equivalence is refuted.** Neither his H-gerbe nor his G-gerbe is equivalent to the pseudomotivic gerbe: π₀
  is μ₂ for H and Ẑ for G, while P is connected.
- **Corrected statement, proved.** Push out his Artin-Tate-rigidified H-gerbe along H ↪ P = G⁰. The result is the
  pseudomotivic P-gerbe of Milne 1994 (Theorems 3.29 and 3.31), with Milne 2003 (Theorem 6.3, Definition 6.6).
  Equivalently, it is the gerbe obtained by rigidifying the Artin motives alone.
- The dictionary is proved line by line under the hypotheses of A.1. Its main lines:
  - his F⁰ ↔ the Artin rigidification;
  - his η_p ↔ their morphism at p;
  - his μ₂ at ∞ ↔ their real Weil extension;
  - his Γ ↔ X*(P).
- I checked the band argument (E10). I did not open the source theorems; the run's `LITERATURE_CHECK` records them as
  opened, with these numbers.

## 2. Item by item

| Item | State reached, as checked | ITEM_STATUS |
|---|---|---|
| A.1 | (a) Γ is the group of Weil numbers of all weights ν ∈ Z: the ν ≥ 0 numbers are only a monoid (E23). (b) X*(H) = Γ', Γ'_tors = Z/2 by √p, H⁰ a compact protorus with uniquely divisible character group. (c) Endomorphisms under Tate and semisimplicity. | Fair. "Abelian part unconditional" rests on Van Hoften-Sempliner (Oct 2026), a dated preprint, and the report says so. |
| A.2 | (a) Neutral at ℓ ≠ p. (b) T_p over F_p is a genuine Q_p fibre functor; the isocrystal gerbe is the F̄_p object (E07). (c) No real fibre functor; the third argument repaired (E08). (d) Both μ₂-components 1/2. | Fair. |
| A.3 | See §1. | Fair. |
| A.4 | See §1. | Fair. "Refuted" refers to our Lead A1 as written, not to him. |
| A.5 | Corrected form proved (Kisin 2017 §§3.1, 3.5, Thm 3.1.9). The Lefschetz band L ≠ P, with an F₅ example whose arithmetic I recomputed (E11). | Fair. The band statement is carried. |
| B.1 | Abelian-type comparison proved; literal continuity refuted. Open gate: Chow injectivity in codimension m on (2m−1)-folds, proved for surface-supported zero-cycles (uniruled threefolds). | Fair (open). |
| B.2 | The Tate-motive comparison H^i_f proved; the general conjecture formulated and specialized; Scholbach's Hom fails the odd-Weil requirement. | Fair. |
| B.3 | Exact sequence and corank proved; X₀(11) confirmed (E13, E14). Full-Brauer form of 12:79 refuted (E21, carried). Prime-to-p finiteness equivalent to the Tate conjecture for divisors on simply connected surfaces with H¹(O) = 0 and very ample K over finite fields. | Fair: "undecided" is an exact equivalence with a named open conjecture. |
| B.4 | Rational groups of Spec Z̄ for all (i, n) proved (E15); "[est-ce nul ??]" answered: no. Integral groups only by a terminating procedure. | **Overstated** ("Proved"): the integral groups are not determined (Vandiver-type finite K-groups; E16). |
| B.5 | Finite duality with compact support, and the Artin-Tate rational case, proved. The general rational form is equivalent to Beilinson plus Parshin. | Fair (open). |
| C.1 | (a) Every relation and rank by finite contraction matrices; closed formulas only for curves and surfaces. (b) Graph rule. (c) Abelian varieties with o = 0 and hyperelliptic curves with o Weierstrass: all relations hold in Chow. The genus-3 failure is the Fermat quartic (Bloch 1984; E18). K3 all powers open (∧^{23−ρ} t₂(X) = 0). | (a) slightly **overstated**: the prompt also asked dimensions for abelian varieties and P^n, given only through the algorithm. (c) fair. |
| C.2 | Axioms stated; corrected definition proved; Frobenius-algebra reconstruction. | Fair. Not checked by me. |
| C.3 | Arithmetic invariant centre, geometric centre and analytic Lie algebra distinguished; each proved or refuted. | Fair. Not checked. |
| C.4 | Our prompt's level bound refuted (E12); corrected weight-level polygon; endpoint for j ≤ 2 and abelian type. Higher endpoint equivalent to weight-monodromy. | Fair, but "Proposed bound refuted" is **our** bound, not his (§4). |
| C.5 | Vasiu-Zink positive case. Explicit p = 2 abelian surface over W(k)[[u,v]]/(2 − uv), with a finite subgroup whose closure is not flat. | Fair as reported. **Not checked** (E22); it needs an independent check before any use. |
| C.6 | Abelian type proved; motivated rank implication conditional; general case open. | Fair (open). |
| D.1 | Integral model with schematic closure proved; the literal special-fibre bridge of Lead D1 refuted; exact-residue CM lifting. | Fair. |
| D.2 | (a) Abelian type proved. (b) Refuted: S4 Artin motives are Taniyama quotients (E17). (c) Aut(C) through Taniyama torsors. | Fair. |
| D.3 | Finite-place-trivial classes are the even-parity vectors (= 15:154); the Betti functor is unique only in the rank-one case (E19). | Fair. |
| D.4 | Image of ψ_Σ is the Mumford-Tate group of the CM type, by the saturated character lattice. | Fair (standard). |

## 3. His text: what is false, and what needs a repair

1. **15:3 is right; withdrawn in the follow-up (§9, E25).** He gives the band H = Ker(G⁰ → G_m) for "la sous-gerbe des
   foncteurs fibres de M prolongeant F⁰". His F⁰ includes the Tate object ("F⁰(Q(1)) = Q" stands on the page), so H is
   the right band. The run's "Artin-only band G⁰" is correct mathematics but is not what he wrote. E06 is withdrawn.
2. **15:11, third argument.** "L'argument de Serre sur la courbe elliptique d'inv. de Hasse nul" does not work over F_p
   as written. There End⁰(E) = Q(√−p) is a field. It needs the quaternion algebra over F_{p²}, brought down to F_p by
   restriction of scalars or by a Honda surface (E08).
3. **15:5.** Γ has to be the group of Weil numbers of all weights ν ∈ Z.
4. **12:63-64 and 12:75 (R6, confirmed).** The ℓ-adic comparison and "H¹(S,A)(ℓ) fini" are false over Z[1/11ℓ]
   for X₀(11). The corank is d + s − t, where t is the rank of the ℓ-adic closure of A^t(K).
5. **12:79.** "Br(S) → Br(X) surjectif mod groupes finis ??" is false with the p-part included (infinite 2-torsion over
   A¹/F₂). Away from p it is equivalent to the Tate conjecture for divisors on the stated surfaces.
6. **12:142.** Good reduction over a regular local ring of dimension 2 holds under Vasiu-Zink's conditions. In general
   the answer is no, by the run's p = 2 example (not checked).
7. **Cover 15:157, "(= Motifs métabéliens)".** The motives whose motivic group has a commutative identity component
   include the S4 Artin motives, so the name "métabéliens" does not fit literally. Over Q his category is CM(Q), the
   Taniyama quotients.
8. **15:174, "[est-ce nul ??]".** No: H¹(Spec Z, Q(n)) = Q for odd n ≥ 3 (Borel's regulator) and H²(Spec Z, Q(n)) = Q
   for even n ≤ −2. His H^i(Spec Z, Q(1)) = 0, 0, 0, Q is right.

## 4. Ours: where our study notes, readings or prompt were wrong

1. **STUDY.md §1 (15:7) and prompt A.3(c).** We wrote that ξ₀ determines M "with the T_ℓ and F⁰". The ink separates
   the bare class (M, gradation, augmentation, F₀) from the relative class with the F_ℓ (E04).
2. **STUDY.md §1 (15:3) and the prompt's Part A setting.** We glossed Niv⁰(M)⁰ as "the Artin motives" and left out
   his line F⁰(Q(1)) = Q. Read that way, the band H looked wrong. It is right as he wrote it (E25, which withdraws E06).
3. **Lead A2 is false.** T_p over F_p is a Q_p fibre functor. The Z/Ẑ remark concerns the continuity of Frobenius (E07).
4. **Lead A1 is false as written** (bands H or G). The right statement is the pushout to P = G⁰ (E10).
5. **Our sweep-3 check of "Serre's argument"** (STUDY.md §1, "Checked") used the quaternion algebra over F_p. That
   algebra is End⁰ over F_{p²}, not over F_p, so the check passed an argument that needs the repair in §3.2 (E08).
6. **Prompt C.4.** We stated the general-case level bound as Inf(i, d_y(f) − 1) + j. That is the immersion-case box of
   12:120. The final general box reads Inf(i, \unsure{n}) + j, with the margin asking about n − 1. Our form is false
   for an elliptic curve over F₅ (E12).
7. **Prompt B.3.** We used the abstract rank of A(K) in the corank formula. The right quantity is the ℓ-adic closure
   rank t (E14).
8. **R5** omitted the integral 2-torsion coming from the real place in the Spec Z tables (the run's correction; not
   re-checked).
9. **Lead D1** read the closure in G⁰ = A*/closure(E⁰) as profinite. The integral model needs the schematic closure.
   The page itself has both: the profinite A*(Ẑ)/E⁰ is the Galois group, and the group scheme carries the schematic
   closure (E20).
10. **Lead D2** ("metabelian = Taniyama quotients") is false: S4 is a counterexample (E17).
11. **Prompt bibliography.** We cited Milne's "Gerbes and abelian motives" as Math. Ann. 325. The run could not
    substantiate this and cites the 2003 author preprint (arXiv math/0301304).

## 5. New results (the run's, with the intake's check)

- **Explicit global class of the F_p gerbe** (A.3(d)): the compact class m ↦ v_p(m) mod Z, of infinite order, and the
  (p, ∞) quaternion class. Checked in its local parts (E09).
- **Hasse principle in degree 2** for R-compact tori and for this protorus (A:compacthasse, A:hasse). Re-proved for
  tori (E01).
- **A framed counterexample**: ξ₀ does not classify chosen local functors (E05).
- **A Lefschetz band strictly smaller than P**, from an explicit F₅ example (E11).
- **The level counterexample and the corrected weight-level polygon** of 12:120 (E12).
- **The tautological rings of 11:51-57.** All relations and ranks are determined by contraction matrices. All
  relations hold in Chow for abelian varieties and for hyperelliptic curves, and fail for the Fermat quartic.
- **The B.3 reduction** of 12:79 and of the torsor finiteness to divisor Tate for one class of surfaces. **The B.4
  table** for Spec Z̄ (E15).
- **D.3 and D.4**: the Q-forms of CM motives (even-parity vectors, uniqueness of the Betti functor only in rank one),
  and the image of ψ_Σ.
- **The p = 2 bad-reduction example of 12:142.** Checked and correct, but not new: it is an explicit instance of the
  Raynaud-Gabber example (§9, E32-E33).

## 6. Ink claims that need a reader on the scans

1. **12:120, the final general-case box.** "niveaux ≤ Inf(i, \unsure{n}) + j": is it n or n − 1, and what does n
   denote there (dim X, or d_y(f))? The margin "peut on remplacer par n − 1 si f de dim ≤ n − 1 ?" depends on it.
   C.4 rests on this.
2. **15:3, the band named for "prolongeant F⁰".** The transcription reads "H = Ker(G⁰ \unsure{ε|e} G_m)". Check also
   whether "augmentation" appears on 15:3 as it does on 15:7.
3. **15:5.** Whether his definition of Γ restricts to ν ≥ 0 (the run's "literal monoid reading").
4. **15:11.** The ground field of "l'argument de Serre"; the transcription has none. And the doubt mark
   "\unsure{U|H} est disconnexe" in the first argument.

## 7. Literature locators the main answers rest on

These are recorded as opened in the run's `LITERATURE_CHECK.tsv`, with the numbers below. The intake did not open the
sources.
- Milne 1994, *Motives over finite fields* (corrected author version, 2019): Theorems 2.9, 3.29, 3.31.
- Milne 2003, *Gerbes and abelian motives* (author preprint): Theorem 6.3, Definition 6.6.
- Milne, *Arithmetic duality theorems*: I.4.20. Its use was re-derived in E01.
- Langlands-Rapoport 1987: Theorems 2.2-2.3, Definition 3.1, Theorem 4.4.
- Kisin 2017 (author manuscript): Theorem 3.1.9, §§3.1, 3.5.
- Flach-Morin 2018: Corollary 3.12, Theorem 3.22, §5.8.3. Used for B.4.
- Borel 1974: Proposition 12.2.
- Bloch 1984: Theorem 4.1.

## 8. Is a finishing prompt warranted?

**No.** The run stopped by the prompt's own ledger rule (review04 and review05 without movement), not by a cut session.
Every one of the 8 open rows ends at a named open conjecture (E24):
- Chow injectivity of Bloch-Beilinson/Parshin type (B.1, Lead B1);
- the Tate conjecture for divisors on simply connected surfaces with H¹(O) = 0 over finite fields (B.3);
- Beilinson plus Parshin (B.5);
- the K3 condition ∧^{23−ρ} t₂(X) = 0 (C.1(c), Lead C1);
- weight-monodromy in mixed characteristic (C.4);
- ℓ-independence of monodromy ranks for general motives (C.6).

A successor would attack these conjectures and would grind detail, as the last two review intervals did. The main
question (A.3-A.4) is settled.

What remains is checking, not research. It can go to one of our readers:
1. C.5's p = 2 example (with a literature search for known counterexamples to purity at p = 2);
2. the lim¹ step of A:hasse;
3. the band statement L ≠ P of A.5;
4. the integral 2-torsion that R5 omitted.

If a finishing prompt were nevertheless wanted:
- **It would carry** the 8 open rows with their gates and approaches, from `ITEM_STATUS.tsv` (column 4) and
  `PROGRESS_LEDGER.md` (reviews 01-05).
- **It would restore from** this final: `sections/`, `part_*/`, `code/`, `RESEARCH_SA05_results.csv`,
  `CHECK_EVENTS.tsv` and `LITERATURE_CHECK.tsv`, with `_from_earlier_checkpoints/` for unchanged files.
- **It would drop** A.1-A.5, B.2, B.4 (rational part), C.1(a)-(b), C.2, C.3, C.5 (once checked) and D.1-D.4.

## 9. Follow-up checks (19 Nov 2026, same agent, at the coordinator's word)

The four places of §6 were read on the scans. The second-pass rows are in
`readings/c15b_c12_c11_SECOND_PASS_followup_20261119.md`; the crops are in
`second_pass/work/SA05_followup/`. The check events are E25-E33.

1. **15:3 (E25).** The page has "F⁰(Q(1)) = Q" right after the definition of F⁰. F⁰ therefore includes the Tate
   object, and the band H = Ker(G⁰ →ε G_m) of "les foncteurs fibres prolongeant F⁰" is right as written.
   - The arrow label is ε (doubt lifted, high).
   - "Augmentation" does not occur on 15:3.
   - E06 and the §3.1 claim are withdrawn. The error was our gloss of Niv⁰(M)⁰ (§4.2).
2. **12:120 (E26).** The final box reads "niveau ≤ Inf(i, n) + j" (n heavy and retraced; doubt lifted, medium).
   - Here n = d_y(f), defined just above as a local relative dimension at y.
   - The margin asks whether n − 1 will do when f has fibres of dimension ≤ n − 1.
   - His box is consistent with the F₅ elliptic curve. The run's counterexample refutes only our prompt's n − 1.
3. **15:5 (E27).** "Le sous-groupe Γ ⊂ Q̄*" is defined by "λ entiers algébriques … ν ∈ Z⁺ convenable", which is a
   monoid. The run's group completion stands as a correction of his text; the transcription is right.
4. **15:11 (E28).** "L'argument de Serre sur la courbe elliptique d'inv. de Hasse nul" names no field, so the repair
   over F_p is needed. "U est disconnexe" reads U (script U without crossbar; doubt lifted, medium).
5. **The lim¹ step of A:hasse (E29): re-proved.**
   - Choose the lattices with X_i ⊂ d_i·X_{i+1}, where d_i is the degree of a splitting field of T_i.
   - Then every transition map on H¹, global and local, factors through multiplication by d_i, which is zero, so
     lim¹ = 0.
   - Hence H²(–, H⁰) = lim H²(–, T_i), and Ш²(Q, H⁰) = lim Ш²(Q, T_i) = 0, each T_i being compact over R (E01).
6. **L ≠ P in A.5 (E30): re-proved in outline.**
   - λ is a Weil 5-number (E11). Honda-Tate gives A_λ over F₅.
   - The character 2[λ] − [α] − [β] is trivial on P.
   - On the Lefschetz group of E_α × E_β × A_λ (three Lefschetz groups over one multiplier), its restriction to the
     multiplier-one part of L(A_λ) is 2[λ] ≠ 0.
7. **R5's integral 2-torsion (E31): the run's correction holds.**
   - H¹(Spec Z, Z(1)) = Z^× = {±1} ≅ Z/2, where his table of 15:173 has 0.
   - Étale H^{2k}(Spec Z, Z) contains Ĥ^{2k}(R, Z) = Z/2 for k ≥ 2, from the real place. It vanishes only with the
     Tate modification at ∞.
   - R5 re-proved only the rational table.
8. **C.5's p = 2 example (E32): correct.**
   - The proof: I checked every identity in Z[u,v]/(uv − 2) (`intake_RESEARCH_SA05_scripts/check_c5_example.py`, all
     pass). The closure of the diagonal Z/2 is R ⊕ m·t, with a closed fibre of dimension 3 against generic rank 2, so
     it is not flat.
   - An abelian scheme extending B_K would extend the isogeny, whose kernel is finite flat. Over the height-one primes
     the closure is flat.
9. **C.5's novelty (E33): not new.** I opened Vasiu-Zink, Doc. Math. 15 (2010) 571-599, arXiv:0909.0969v3.
   - The ring R = W(k)[[u,v]]/(2 − uv) is the p = 2 case of the Raynaud-Gabber example
     Spec W(k)[[T₁,T₂]]/(p − (T₁T₂)^{p−1}), which is neither healthy nor p-healthy regular. Sources: Gabber's letter to
     Ogus of 22 July 1992; de Jong-Oort 1997, §6.
   - Vasiu-Zink cite it in their introduction (pp. 1-2), where it disproves the claim of Faltings-Chai, Ch. IV,
     Theorems 6.4, 6.4′ and 6.8. They generalize it in §5.4: Lemma 27, and Theorem 28(ii), which covers R with u = T₁,
     v = T₂.
   - Their abstract: extensions always exist for e ≤ p − 1, in most cases for p ≤ e ≤ 2p − 3, and not in general for
     e ≥ 2p − 2.
   - The run's elliptic-curve presentation is at most a new explicit instance.
   - Not opened by me: de Jong-Oort, Gabber's letter, Moret-Bailly's equal-characteristic examples (Astérisque 129),
     and Gabber-Vasiu (arXiv:0911.2474).

The verdicts of §2 change accordingly. For A.3-A.4 nothing changes. For C.5 the result is correct and classical.

## 10. Rows for the register

**Check events:** INT-SA05-E01 to E33, in `INTAKE_RESEARCH_SA05_20261119_CHECK_EVENTS.tsv`. E06 is withdrawn by E25. Its columns are id,
statement_id, date_utc, who, type, outcome and where.

**Corrections** (decided by the RESEARCH_SA05 final, GPT-6 Astra (ChatGPT Pro mode); intake by Claude Opus 5.5 at
effort max, a7b7747fd6dd29f87):

| id | where | kind | what | corrected | evidence |
|---|---|---|---|---|---|
| INT-SA05-K01 | STUDY.md §1, 15:7; prompt A.3(c) | our reading corrected | ξ₀ determines M with the T_ℓ and F⁰ | ξ₀ ∈ H²(Q,H) for (M, grad, aug, F₀); with the F_ℓ, ξ ∈ H²(S mod T, H) | E04 |
| INT-SA05-K02 | STUDY.md §1 (15:3); prompt Part A setting | our note corrected (his text stands) | Niv⁰(M)⁰ = the Artin motives, so the band H looked wrong | F⁰(Q(1)) = Q is on the page; F⁰ includes the Tate object and his band H is right | E25 (withdraws E06) |
| INT-SA05-K03 | prompt Lead A2 | our lead refuted | T_p is not a Q_p fibre functor | over F_p it is one; "Z, not Ẑ" is the continuity of Frobenius | E07 |
| INT-SA05-K04 | 15:11; STUDY.md §1 "Checked" | his argument repaired; our check corrected | Serre's supersingular-curve argument over F_p | needs F_{p²} (quaternion End⁰) or a Honda surface | E08 |
| INT-SA05-K05 | prompt Lead A1 | our lead refuted, refined | equivalence with band H or G | pushout along H ↪ P = G⁰ is the pseudomotivic gerbe | E10 |
| INT-SA05-K06 | prompt C.4; 12:120 | our statement refuted | levels ≤ Inf(i, d_y(f) − 1) + j | false (F₅ elliptic curve); final box reads Inf(i, \unsure{n}) + j | E12 |
| INT-SA05-K07 | prompt B.3 | our formula corrected | corank with rank A(K) | ℓ-adic closure rank t | E14 |
| INT-SA05-K08 | prompt Lead D2; cover 15:157 | our lead refuted; his name qualified | metabelian = Taniyama quotients | CM(Q) contains S4 Artin motives | E17 |
| INT-SA05-K09 | 15:174 | his question answered | "[est-ce nul ??]" | no: H¹(Q(n)) = Q for odd n ≥ 3, H²(Q(n)) = Q for even n ≤ −2 | E15 |
| INT-SA05-K10 | prompt bibliography | our citation corrected | Milne 2003 in Math. Ann. 325 | author preprint 2003 (arXiv math/0301304) | run's LITERATURE_CHECK |
