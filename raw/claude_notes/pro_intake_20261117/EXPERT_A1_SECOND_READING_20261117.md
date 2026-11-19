# A1 after the full audit: second reading

Check by Claude Fable 5.2 at effort max (copy ab3f12f2 of the Longue Marche expert), reading the proofs, 17 Nov 2026.
Return: 03_ANABELIAN_A1, checkpoint 03 (its final), by GPT-6 Astra (ChatGPT Pro mode):
`longue_marche_pro_pilot_20261104/answers/ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped/ANABELIAN_A1/`.
Brief: `pro_intake_20261117/BRIEF_A1_SECOND_READING_20261117.md` (main session, Claude Opus 5.5 at effort max).
First check: `pro_intake_20261116/EXPERT_A1_ANABELIAN_20261117.md`.

**This note is written as the reading goes. A section that is not marked DONE is not finished.**

## 0. State of this reading (for a resumed or compacted reader: start here)

- Started 17 Nov 2026 at about 909k of 1M context; a compaction during the work is expected.
- Order of work, from the brief: (1) the main chain not read before: AG.39, the end of AG.41, AG.42, AR.8-AR.9, in the
  form the audit gives them; (2) the second "support-field" proof, without the finiteness of Saïdi-Tamagawa; (3) K1-K6
  as posed in the first check; (4) A.33 and B7 at the level of sense; (5) verdict, what was not read, what a second
  reader must still check.
- What the first check had established (do not redo): AR.3's assembly; AG.40 in full; AG.41 statement, steps 1-2 and
  the start of step 3 (the rest re-derived by me); the cusp transport re-derived by me. The one outside input of
  weight was Saïdi-Tamagawa 2009, Prop. 1.8 (vi) (finiteness of the exceptional set, over all constant extensions).
- Progress log (newest last):
  - step 0: brief read; this file created. Nothing of the return read yet.
  - **STOPPED at about 962k of 1M context, at the window's edge.** Done: sections 1.1-1.3, 2, 3 (K1-K4, K6) and a
    provisional verdict (section 5). **Left to do, in this order, by a resumed or compacted reader:**
    (a) `A_criterion.tex` lines 167-259 (A.CR6 in the audit's form);
    (b) `A_configuration.tex` lines 302-684 (A.CF5-A.CF9: the failure of the full sequence, i.e. AG.39) and K5 (the
        finite tests A.CF5, A.CF6, A.CF11 with `code/`), filling section 1.4;
    (c) `A_root_intro.tex` line 16 (A.R1), `A_root_fields.tex` lines 101-end (A.R4, A.R5; the brief's "A.33" is the
        extension: find its row in `ANABELIAN_A1_results.csv`), and B7 = rows B.46-B.48, B.50 (find them in
        `sections/B_*.tex`), both at the level of sense, filling section 4;
    (d) make section 5 final.
  - step 1: file map made (below). The report's first line is INCOMPLETE; its table marks item A1 "Proved" with
    statements A.1, A.19, A.21, and item A12 "Open".
- File map of the return (sizes in bytes), for the order of reading:
  - `sections/A_configuration.tex` (43,563): the configuration statements (AG.39, AG.41, AG.42 in the audit's form). Read first.
  - `sections/A_criterion.tex` (55,045): the criterion (AG.40) and, by its size, the second proof. Read second.
  - `sections/A_literature.tex` (31,356): the sources (K1, Saïdi-Tamagawa). `sections/A_root_fields.tex` (10,947):
    the extension to finitely generated fields (A.33). `sections/A_root_prime_sets.tex` (3,421), `A_root_intro.tex` (2,960).
  - `notes/configuration_audit.md` (14,196), `notes/criterion_audit.md` (51,497), `notes/literature_audit.md` (49,172):
    the run's audits. `ANABELIAN_A1_results.csv` (99,541; 121 statements); `ANABELIAN_A1_report.md` (36,547).
  - B7 is in the B sections (`sections/B_*.tex`); find its statement through the results CSV (row B.x named in the
    report's table line "B7").

## 1. The main chain (AG.39, end of AG.41, AG.42, AR.8-AR.9)

In the audit the configuration statements are `sections/A_configuration.tex`: A.CF1 (line 18, the monodromy lemma),
A.CF2 (64, exactness; this is AG.41), A.CF3 (142, specialization and the arithmetic fibre; the end of AG.41), A.CF4
(218, the diagonal boundary and cusp transport; this is AG.42), A.CF5-A.CF9 (304-684, the failure of the full
sequence; this is AG.39), A.CF10-A.CF12 (685-844).

### 1.1 A.CF2, lines 64-140: SOUND (read in full) — DONE

- For a finite quotient `Q` of `F_cr`, with `R` the image of the pro-`r` cusp kernel and `A = Q/R`: pass to the
  cover `C′ → C` with group `A`, and to `Y = C′ × C′` minus the graphs of the deck transformations. The punctures of
  `Y → C′` are labelled, the compactified family is a product, so the monodromy on `H_1(V′, F_r)` lies in the
  additive group `Hom(H_1(C′), W)`: an `r`-group, with no condition on `|A|` (lines 99-110). By A.CF1 the pro-`r`
  completion of the fibre group embeds.
- Lines 112-125: `H = π_1(Y)` is normal in `Γ = π_1(U)` with quotient `A × A`; a finite `r`-quotient of `H`
  dominating `R` on the fibre; its core `J*` over the finitely many cosets; `Γ/J*` is an extension of `A × A` by an
  `r`-group, and `J* ∩ Λ ⊂ J ∩ L ⊂ ker q`. Each containment checked.
- Lines 127-139: the quotient factors through `E_cr` (the image of `K_E` is in the `r`-group `H/J*`); the fibre map
  factors through `F_cr`; right exactness of completion gives the rest. Correct.
- This agrees with the argument I had completed myself in the first check. No gap.

### 1.2 A.CF3, lines 142-216: SOUND as read — DONE

- Specialization (153-197): lift the pointed curve to the Witt ring; `(𝒞 × 𝒞, diagonal)` is a smooth proper pair with
  smooth relative boundary; SGA 1 XIII 2.9-2.11 gives the isomorphism of the tame prime-to-`p` groups of the two
  geometric fibres, functorial for the fibre inclusion `x ↦ (x, P)`, which meets the diagonal transversally once.
  This is the standard comparison; the page citations of SGA 1 were not opened by me.
- The arithmetic fibre (199-215): the map `Π_{C−P,cr} → ℰ_cr ×_{Π_C, s_P} G_k` is the isomorphism of A.CF2 on
  geometric kernels and the identity on `G_k`, hence an isomorphism; the target is `pr_2^{-1}(s_P(G_k))`. Correct.
  The whole `G_k` is kept.

### 1.3 A.CF4, lines 218-300: SOUND as read — DONE

- `𝒟`, the image of the tame group of the diagonal boundary (through root stacks, SGA 1 XIII 5.2), is an extension
  of `Π_C` by the full `Z_r(1)`: the kernel is the image of inertia, and it has infinite order because the boundary
  loop maps to `1 + e_13` in the Heisenberg group over `Z_r` and A.CF2 keeps the fibre inside the total group
  (268-280). Includes `r = 2`.
- The cusp subgroup of `C − P` is `𝒟 ∩ pr_2^{-1}(s_P(G_k))`, by comparison of two extensions of `G_k` by inertia;
  the paths for `P` and `Q` are taken in the same boundary tower, so one `𝒟` serves both (282-288). This is the
  point I had argued myself ("the same diagonal component") and it is argued here correctly.
- Transport (290-299): `d ∈ 𝒟` geometric over `γ`; conjugation by `d` carries fibre to fibre and cusp to cusp and is
  `Inn(γ)` on the first coordinate; `e` in the geometric part of the `Q`-fibre over `γ^{-1}`; `Inn(e) Inn(d)` is over
  the identity of `Π_C`. Correct. No section of the configuration fibration is lifted.

### 1.4 A.CF5-A.CF9 (AG.39) and AR.8-AR.9

(not started)

## 2. The second support-field proof — DONE: complete, and it does not use Saïdi-Tamagawa's finiteness

`sections/A_criterion.tex`, A.CR7 (lines 260-304) and A.CR8 (306-357), read in full and every step checked.

- **A.CR7 (the Kummer step needs only a proper support field).** Hypothesis: the points transported by `β` keep
  their label outside `C(F)`, for one algebraic subfield `k ⊂ F ⊊ k̄`. Take `n` the exact order of `[P − Q]` and
  `f` with divisor `n(P − Q)`; `κ_r(f) − nχ` is a constant class `κ_r(a)`; so `f(R)/a` is an `r`-th power in the
  residue field of every `R` with unchanged label. `f/a` is not an `r`-th power geometrically (valuation if
  `r ∤ n`; exactness of the order if `r | n`), so the Kummer cover `D: z^r = f/a` is geometrically connected. Choose
  `ℓ` with finite exponent in `[F : k]` (exists because `G_F ≠ 1`) and the tower `L_m` of degree `ℓ^m` over a field
  `L ⊃ μ_r`; then `F ∩ ⋃ L_m` is a finite field, so only a bounded number `B` of points of `C(L_m)` are excluded,
  and `#D(L_m) ≥ r(#C(L_m) − B)`. The Weil bounds for `C` and `D` give
  `(r − 1)(Q_m + 1) ≤ (2g_D + 2r g_C)√Q_m + rB`, false for large `m`. I checked each inequality. Correct.
- **A.CR8 (the support field exists, elementary).** `B_C` = the points `R` with some `S ≠ R` and `[R − S]`
  of `p`-power order. (i) For `t ≠ 0` the set of pairs `(R, S)` with `[R − S] = t` has one or two elements: two pairs
  give `R + S′ ~ R′ + S`, so equality or the unique pencil of degree two, and then `(R′, S′) = (ι(S), ι(R))`.
  (ii) For an odd prime `ℓ ≠ p` not dividing `|GL_f(F_p)|` (`f` the `p`-rank), the factor `H = Z_ℓ` of `G_k` acts
  trivially on all `p`-power torsion of `J_C`: its image in `GL_f(Z_p)` is trivial modulo `p` and trivial in the
  pro-`p` kernel. (iii) `H` fixes `t` and acts on a set of one or two elements, so it fixes `R` and `S`. Hence
  `B_C ⊂ C(F)`, `F = k̄^H ⊊ k̄`. Each step is correct.
- **Use (lines 348-352).** `β` is over the identity of `Π_C`, so a transported point `S` of `R` has a section
  geometrically conjugate to that of `R`, hence `[R − S]` is `p`-primary (the Kummer step); so `R ∉ B_C` forces
  `S = R`. With A.CR7 this gives `P = Q`.
- **So the outside input of weight named in my first check (Saïdi-Tamagawa 2009, Prop. 1.8 (vi), and behind it
  Boxall) is no longer needed for A.1.** What the second proof still uses: the isomorphism `β` (A.CF2-A.CF4, sound,
  section 1), the same-prime lemmas A.CR1, A.CR2, the recognition of points A.CR5, the central extensions and the
  self-normalizer A.CR4 (these were AG.40 steps 2-4, read in the first check in their earlier form), the Weil bound.
- Scope: A.CR8 is stated for `p`-primary differences, i.e. for the set of all primes other than `p`. For a smaller
  set `Σ` the Kummer kernel is larger; the run's A.CR10, A.CR15 treat that (A.CR15 is Open) and I did not read them.
- **A.CR9 (lines 359-380, read): the equivalence with the emptiness of the exceptional set.** Correct as argued; it
  cites Saïdi-Tamagawa 2009, Prop. 1.8 (iii) and 2017, Prop. 2.11-2.12, for the equivalence only, not for A.1.

## 3. K1-K6

- **K2 (the same-prime statement, formerly (AG.39.15)) — DONE: proved as posed.** `A_criterion.tex`, A.CR1 (lines
  7-27) and A.CR2 (29-69), read in full.
  - A.CR1: for `N = ker(K → K^(r))` and every open `I ⊃ N`, `I^(r) = (I/N)^(r)`. Proof by two cores: `I_0` the core
    of `I`, `M` the core of `J ∩ I_0` for a finite `r`-quotient `I/J`; the image of `K` in `F/M` is an `r`-group, so
    `N ⊂ M ⊂ J`. Each step checked. Correct, with no condition on the index of `I`.
  - A.CR2: an open subgroup of the cuspidally pro-`r` group is the full prime-to-`p` group of its cover modulo `N`;
    killing the cusp inertia and taking the pro-`r` quotient gives `π_1(D)^(r)` of the compactification, equivariantly
    for Frobenius; so the Weil polynomials, the cusps with their degrees (double cosets) and the point counts of
    corresponding open covers agree. Correct. This is exactly what step 2 of AG.40 needed.
- **K3 (AG.41 step 3 and the arithmetic comparison) — DONE: proved as posed.** It is A.CF2 lines 112-139 and A.CF3
  (section 1.1, 1.2 above).
- **K4 (AG.42) — DONE: proved as posed.** It is A.CF4 (section 1.3 above), including the point that one boundary
  group `𝒟` serves both `P` and `Q`.
- **K1 (the finiteness input) — DONE: answered as posed, and no longer needed for A.1.** `A_criterion.tex`, A.CR3
  (lines 71-107), read. It quotes Saïdi-Tamagawa 2009: Definitions 1.3 (iii), 1.5, 1.10; Proposition 1.8 (vi) (for a
  cofinite set of primes the exceptional set modulo the group is finite); Remark 1.2 (commensurability classes do not
  change on open subgroups), from which the uniformity over all constant extensions follows (lines 92-94: correct).
  It retraces their proof (a non-hyperelliptic cover; the difference map injective off the diagonal; Boxall's theorem
  for the finite complementary set of primes) and says plainly that Boxall's theorem and the existence of the
  non-hyperelliptic cover were not re-proved. I opened no source. By section 2 this input is now only needed for the
  first proof.
- **The recognition of points (A.CR5, lines 135-164, read; A.CR4, 109-131, read).** The compactness argument is
  written out in full (product of the finite sets, finite-intersection property, a lift in the pro-cover, and
  `D ⊂ ⋂ H = S` with equality because both are sections). Correct, and it is whole-group recognition.
- K5 (the finite test by program) and K6 (AR.9): K6 is A.CR9 (section 2: correct). K5: (not yet checked; the finite
  tests are A.CF5, A.CF6, A.CF11 in `A_configuration.tex` lines 302-760 and `code/`).

## 4. A.33 and B7

(not started)

## 5. Verdict (provisional, written at about 950k of context; to be completed if the reading goes on)

**On what I read, A.1 stands as stated**, for the set of all primes other than `p`: every smooth proper
geometrically connected curve of genus at least two over a finite field has an injective geometrically prime-to-`p`
point-section map, with the whole `G_k` and after every finite constant extension.

The proof I have now read end to end, in the audit's form:
1. A.CF1-A.CF2: exactness of the fibration sequence with the cuspidal kernel made pro-`r` over the full proper
   prime-to-`p` group (sound; sections 1.1 and the first check).
2. A.CF3: specialization to characteristic `p` and the arithmetic fibre as the inverse image of the point section
   (sound as read; the SGA 1 statements were not opened).
3. A.CF4: one diagonal boundary group, the cusp subgroup as an intersection, and the transport isomorphism `β` over
   the identity of `Π_C` (sound).
4. A.CR1-A.CR2: the same-prime lemma and the preservation of point counts (sound).
5. A.CR4-A.CR5: self-normalizing sections; recognition of non-cuspidal points by compactness (sound).
6. A.CR6: the central extensions and the cocycle `χ` (read in the first check as AG.40 step 4; lines 167-259 of the
   audit's version not re-read).
7. A.CR7-A.CR8: the Weil-bound form of the Kummer step and the support field (sound; section 2). **This removes the
   dependence on the finiteness theorem of Saïdi-Tamagawa and on Boxall.**

**Not read in this second reading (so not covered):** A.CF5-A.CF12 (the failure of the full sequence, i.e. AG.39,
and the finite tests; K5); A.CR6 in its audit form (lines 167-259); A.CR10-A.CR15; `A_literature.tex`;
`A_root_*.tex` (A.R1-A.R6: the main theorem's final statement and the extension A.33); the B and C sections (B7);
the run's audits in `notes/`; the programs in `code/`; the paper. No source of the literature was opened.

**What a second reader must still check before anything public:**
1. A.CF1 and A.CF2 once more, line by line: everything rests on this exactness, and it is new.
2. A.CF3: the specialization statements of SGA 1 XIII (2.9-2.11) and the lifting (III 7.3-7.4) in the source, and
   that the comparison is functorial for the fibre inclusion.
3. A.CF4: the root-stack description of the boundary group and SGA 1 XIII 5.2 in the source.
4. A.CR6 lines 167-259 in the audit's form (the multiplier one, the residues of `χ`, the descent to `Π_C`).
5. The statement of A.R1 against what is proved: all primes other than `p`; whole `G_k`; every constant extension.
6. A search of the literature after 2017 for the emptiness of the exceptional set (the main session's task).
