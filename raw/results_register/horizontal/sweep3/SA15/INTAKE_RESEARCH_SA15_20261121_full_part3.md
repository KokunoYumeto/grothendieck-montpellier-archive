# Full intake of RESEARCH_SA15 (cp37), part 3 of 3: ids 637-955 of the ledger's list

Claude Opus 5.5 at effort max, agent a1cf7c6b5992a5d3b (the SA15 c5_c6 sweep-3 reader: cote 5 and cote 6), 22 Nov 2026
(UTC). Task from the coordinator, at the user's word (21 Nov ~23:5x UTC: [the user's words, omitted]). The run:
RESEARCH_SA15, GPT-6 Astra (ChatGPT Pro mode), with its internal sub-agents `/root/monodromy`,
`/root/obstructions_crystals`, `/root/reduction_descent` (same run, same model). Return read: checkpoint 37,
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`
(register `RESEARCH_SA15_results.csv`, 1018 rows; `sections/*.tex`). My list: the ids 637-955 of
`field_experts/INTAKE_LEDGER.md` section 9, row RESEARCH_SA15, in the order listed there (319 ids); afcdf31b has 1-318,
a8d07e78 319-636. Earlier intakes: `INTAKE_RESEARCH_SA15_20261120_part1.md` (a8d91f19) and `_part2.md` (afcdf31b).
Check events: `INTAKE_RESEARCH_SA15_20261121_full_part3_CHECK_EVENTS.tsv` (columns statement_id, date_utc, who, type,
outcome). Work notes: `agent_notes/a1cf7c6b5992a5d3b_NOTES.md`. Scripts: my scratchpad
(`.../e0d20ada-e036-40ad-83b1-31e9a63b69bc/scratchpad`), run with `python -I -B`, never inside the return.

Where my 319 ids are: `A_monodromy.tex` 165, `B.tex` 94, `D.tex` 18, `F.tex` 13, `C.tex` 8, and 21 in the smaller
`A_*.tex` files.

## 1. Ids already checked by the earlier intakes (19): re-filed

Nineteen of my ids carry check events in the part-1 and part-2 TSVs under the form "RESEARCH_SA15 cp37 <id>", which the
ledger did not match to the bare id: thm:B-RD1, thm:B-RD2, thm:C-RD6 to thm:C-RD13, thm:DE-E2-coherent-Noetherian,
thm:DE-E2-counterexample, thm:DE-PD-pi, thm:DE-coherent-obstruction, thm:DE-curves, thm:DE-hasse, thm:DE-ordinary-sign,
thm:DE-split, thm:projective-all-residues. I re-filed each event unchanged under the bare id, with its original date,
agent and type, and the source line named in the outcome. These are the earlier intakes' checks, not mine.

## 2. Parts D, E and the quotes of F (D.tex, F.tex): 23 further ids

Intake part 1 read all of D.tex and F.tex and gave verdicts in its text, but filed events only for some rows. I checked
these 23 myself.

- **Quotes (rem:DE-quote-D1 ... E11, 13 ids).** Every quoted sentence is on the scan the remark names, in our Pro
  transcriptions (5:41, 6:7, 6:14, 7:17, 7:19, 7:24, 7:43, 7:70, 8:50, 8:81, 9:22, 9:29); the arithmetic in E.1 (c_n mod p
  from the base-p digits; 1/2 != 1 at n = 2) and E.9 (eps_g = (-1)^{g(g+1)/2}, the factor (-1)^{gh}) re-derived; the
  mapping of each page to its theorem agrees with the statements. Targeted check each.
- **Two of the run's theorems settle questions the sweep-3 reading of my stretch left open.** thm:DE-PD-pi answers 5:41
  "peut on définir les π^(n)" yes for every Z_(p)-algebra (hunch H2 of c5_c6 part 1 asked exactly this); and
  thm:DE-simply-connected-convergent proves the "principe d'approche transcendante" of 6:14 under a proper smooth lift with
  simply connected complex fibre (hunch H3 of c5_c6 part 2).
- **thm:DE-old-Gm** (the literal flat site of 7:18 fails the rational affine test): targeted check of the Čech-cocycle
  computation (u(x,t+s) = u(x,t) + u(x+t,s), the logarithm term killed by the coefficients (-1)^{n-1}c/n at n = p^k, the
  units binom(s, p^{v_p(s)})); the extension to all old-site objects followed.
- **thm:DE-simply-connected-convergent**: targeted check, given the cited full faithfulness (Esnault-Shiho 2018).
- **rem:DE-universal-negative**, **rem:DE-E2-Noetherian-scope** (the insertion of 6:7 found in our transcription; the
  relative-Frobenius description re-derived), **rem:DE-E2-coherent-faithfulness-scope**,
  **rem:DE-E2-flat-Noetherian-scope**: targeted checks.
- **thm:DE-inf** (Ogus 1975), **thm:DE-intrinsic-nerve** (Bhatt 2012; the cusp case re-derived),
  **thm:DE-integral-MW-independence** (Ertl-Sprang 2018): known results, carried as background without fault found;
  the sources were not opened by me.
- **rem:DE-E2-coherent-derived-heart**: read at the level of the statement (the bound K_T in D^{<=0} is a claim about the
  proof of thm:DE-E2-coherent-Noetherian, which I did not re-derive).

## 3. The smaller A files (Part A, cote 4): 21 ids

- **A.1, the injectivity questions of 4:4 ("Nous admettrons", 8.3).**
  - thm:OC-surface-coherent-counterexample: **targeted check, confirmed.** Re-derived the Tango curve y^p - y = x^m
    (m = hp - 1; at infinity w = y/x^h is a parameter and (dx) = p d P with d = h(p-1) - 2; p = 2 gives g = 7), the
    nonvanishing H^1(S, L^{-1}) != 0 of the Raynaud surface through the last eigensheaf (Sym^{p-2}E)^v (x) T^{p-2}, which
    contains O_C, and the root cover that keeps H^1(S, L^{-1}) as a direct summand of H^1(X, A^{-1}), the restriction
    kernel. The Raynaud-surface construction itself is cited (Zheng 2017; Mukai).
  - thm:A-coherent-restriction-false (the sixfold, degree n - 1 = 5): **targeted check, confirmed** (the cyclic-cover
    lemma: multiplication by y maps the summand H^{n-1}(R, L^{-1}) identically into H^{n-1}(X, O_X); the Lauritzen-Rao
    nonvanishing through the apolar functional (u_0 z_1 - u_1 z_0)^{p-2}, value (p-2)! on its test monomial; p = 2: rank 34
    of the 40 -> 35 map); its certificate rerun for p <= 13.
  - thm:OC-integral-injectivity-counterexample: **the deduction confirmed** (843 > 842 through the conjugate edge
    injection and the universal-coefficient sequence); the two numbers rest on the threefold of lem:OC-threefold-multiroot,
    not re-derived; certificate rerun PASS.
  - thm:A-all-degree-ranges: targeted check of the cone and Nakayama steps; the Hodge-cone bound is Cotner-Zavyalov 2024
    (cited).
  - Certificates rerun in fresh folders of mine (rows rem:OC-injectivity-degrees, rem:OC-exact-degree-scope,
    rem:OC-product-degree-checks): all PASS with the numbers the remarks state. rem:OC-integral-degree-gate: its W/p -> W/p^2
    illustration re-derived.
  - Statement level only: thm:OC-exact-integral-injectivity-degrees, thm:OC-explicit-integral-counterexample (the product
    with m = 591 * 9^556 + 2), thm:OC-product-exact-degrees.
  - **Consistency with sweep 3.** The coherent kernels found here are not semisimple: STUDY.md §1 (check event SA15-S3-3)
    proves that the semisimple part of H^{n-1}(X, O) injects for every smooth ample section. The two results fit: the
    failures of full injectivity live where Frobenius is nilpotent, and 8.5.7 (the semisimple statement Grothendieck needed)
    stands.
- **A.3-A.5, plane curves in characteristic 2.** thm:plane-char2-all-groups (monodromy GL_g(F_2) for even d >= 4, the
  stabilizer of a canonical covector for odd d; irreducible exactly in even degree): **targeted check of the induction
  step**, conditional on thm:all-char2-theta-orbits, the base degrees and the cited classification
  (Churikov-Vasil'ev-Zvezdina 2022); H^1(GL_N(F_2), F_2^N) = 0 for N >= 4 re-derived; the numerical inequalities of the
  induction verified for every d from 7 to 20000. This answers 8.6 (4:12) for X = P^2 in characteristic two: the
  representation is not irreducible in odd degree, so Grothendieck's "irréductible ... image tout Aut(V)" fails there,
  and holds in even degree.
- **Other monodromy rows in these files.** Certificates rerun: rem:root-mixed-six-three-certificate (minor c^5),
  rem:nonordinary-ppav-covector-checks: PASS. Statement level: thm:root-every-nonordinary-ppav-degree-three-full-candidate
  (GL_80(F_2) on |9Θ|; the rank 80 = h^0(9Θ) - 1 agrees), thm:nonordinary-ppav-all-covectors, thm:ppav-three-theta-jets,
  thm:ss-rectangular-all-degrees, rem:root-three-neighbor-boundary-scope-candidate, rem:root-trigonal-direct-scope-candidate,
  rem:root-theta-avoidance-scope.

## 4. Part B (cote 9:11-14 and 100:48-53): 94 ids in B.tex

What Part B is: the question of 9:11-14 on inertia characters of Barsotti-Tate groups with potentially good reduction,
made precise as B.4: the least torsion level ν_min(p, e, h) at which M[p^{ν+1}] determines the prime-to-p special inertia
character. The run builds explicit counterexamples to the mod-p good-reduction criterion (B-RD1-B-RD12, B-RD23, B-RD26),
then a long series of exact least-index results in height two.

- thm:B-RD1, thm:B-RD2: checked by intake part 1 (re-filed, section 1).
- thm:B-RD8 (defect twelve with full rational 3-torsion over Q_3(i, ζ_3)): **independent computation**: the 3-division
  polynomial of the displayed curve splits completely over Q(ζ_12), with rational y-coordinates, so E[3] is K-rational;
  v(j) = 6 (potentially good), v(Δ_min) = 3 (additive), j ≡ 0 (potentially supersingular). The exact defect 12 was not
  recomputed.
- **Cross-consistency of the exact least-index theorems** (statement level, checked against each other): B-RD49 (1 <=
  ν <= 2 at e = p-1) is closed by B-RD61 (= 1); B-RD31/B-RD34 (p = 3) by B-RD42 (= 2); B-RD45 (dyadic, 3..7) by B-RD48 (= 3);
  B-RD64-B-RD72 (ν = 2 at e = 2(p-1), (p^2-1)/2, t(p-1) for 2 <= t <= 2p+1 with p ∤ t, p^2-1, (p+2)(p-1), 2(p^2-1)) all lie in
  B-RD73's range "ν = 2 iff p < e < p^3 (p ∤ e)"; B-RD63's ambiguity for e > p^{2n-3} gives the lower bound ν >= 3 above p^3,
  consistent with B-RD73; B-RD100-exact (ν = 3 at e = 2p(p-1)) lies outside B-RD73's hypothesis p ∤ e. No contradiction
  among the statements.
- **Presentation note (not an error of mathematics).** Several scope remarks describe the state at their point of the
  paper and are closed later in the same paper: rem:B-RD54-scope ("the remaining finite interval is unresolved") is
  closed by thm:B-RD61; an edition of the paper should mark such remarks as superseded.
- **Statement level only** (status line and opening of each statement read; proofs not read): the other 45 theorems of my
  list in B.tex (thm:B-RD7, B-RD10, B-RD12, B-RD17, B-RD23, B-RD26-wild, B-RD31, B-RD34, B-RD42, B-RD45, B-RD48, B-RD49,
  B-RD52, B-RD57 to B-RD75 (B-RD63-arc, B-RD74-upper), B-RD78, B-RD80, B-RD82, B-RD90-tame-exclusion, B-RD91-large,
  B-RD92-crossing, B-RD93-crossing, B-RD94-six-rows, B-RD95-tracefree, B-RD96-residual-wild, B-RD98-irreducible,
  B-RD99-irreducible, B-RD100-ambiguity, B-RD100-exact) and all 46 scope remarks rem:B-RD53-scope to rem:B-RD99-scope.
  The run records full independent audits by its own sub-agents for almost all of them (GPT-6 Astra, ChatGPT Pro mode,
  same run): those are not intake checks.

## 5. Part A, the monodromy programme (A_monodromy.tex): 165 ids

What these rows are: the run's answers to 8.6 of cote 4 (4:12): is the representation of π_1(U_d) on the semisimple part
V of the vanishing H^{n-1}(Y, O_Y) irreducible, with image all of GL(V)? Intake part 2 read lines 1906-6377 in full; my rows
lie in 181-1905 and 6600-34127.

**Checked.**
- thm:odd-plane-char2-obstruction: **independent re-proof** (my own argument). In characteristic two the sheaf B_C of
  locally exact differentials is a theta characteristic, with H^0(B_C) = ker(F | H^1(O_C)) = 0 on the ordinary locus; for
  odd d >= 5 the plane theta characteristic O_C((d-3)/2) has h^0 = binom((d+1)/2, 2) > 0; so their quotient is a nonzero
  2-torsion line bundle defined over the whole ordinary locus, a nonzero monodromy invariant. **8.6 fails for plane
  curves of odd degree in characteristic two: V is reducible.**
- thm:plane-char2-all-groups (section 3 above) and its input thm:all-char2-theta-orbits (targeted check: the incidence
  dimension binom(e+2,2) - 1 + 3e + 10 - 1 = d(d+3)/2 = N_d re-derived; the exclusions of singular and nonreduced contact
  forms followed). Together: in characteristic two the image is GL_g(F_2) for even d >= 4 and the full stabilizer
  2^{g-1}:GL_{g-1}(F_2) of the canonical covector for odd d >= 5. The base cases d = 5, 6, 7 (thm:quintic-char2-monodromy,
  thm:sextic-full-monodromy, thm:septic-stabilizer-monodromy): their order certificates rerun (|Stab| = 319,979,520 for
  d = 5; ord_31(2) = 5 with a non-reciprocal factor for d = 6; orbit 2^15 - 2 for d = 7); the geometric degenerations and
  the cited classifications were not re-derived.
- thm:all-X-explicit-positive-rank: **targeted check, confirmed** (degeneration to d general hyperplane sections, the
  normal-crossings spectral sequence, lower semicontinuity of the stable rank). This is the positivity
  dim E(Y, O_Y)_ss > 0 for every X and d >= d_0 that 8.5.8 of cote 4 needs and attributes to a "n° 7" not in the dossier;
  with 8.5.7 (proved in sweep 3, STUDY.md §1) it gives Grothendieck's aim in 8.5.8 for every X. It also gives the
  asymptotic f = D d^n/n! + O(d^{n-1}).
- thm:plane-all-residues: the degrees 1-3 re-derived (an ordinary cubic never has #E ≡ 1 mod p); the every-open
  statement for d >= 4 followed in outline.
- Certificates rerun in fresh folders of mine (22 rows, all PASS): the obstruction/crystal rank checks behind the A.3 rank
  formulas (rem:DE-A3-ss-product-computation, -ppav-rank-checks, -separable-rank-scope, -ordinary-all-rank-scope,
  -ordinary-arbitrary-embedding-checks, -mixed-fixed-refinement, -mixed-nonproduct-scope, -mixed-thin-residue-checks,
  -primitive-unipotent-scope, -all-ss-rectangles-checks, rem:DE-A4-third-value-checks, -uniform-triple-local-scope), the
  monodromy graph and grid checks (rem:mixed-all-odd-norm-scope-candidate, -degree-two-wreath-grid-, -strip-,
  rem:nine-theta-transfer-, rem:nonordinary-degree-three-neighbour-, rem:three-total-ramification-Cartier-certificate-
  candidate), and four theorems' finite identities (thm:ordinary-ppav-eventual-full, thm:ordinary-products-eventual-full,
  thm:ss-product-exact-covectors, thm:ppav-level3-Cartier-symmetric). These are reruns of the run's own code: they confirm
  that the code does what the text says, not the geometry.
- Arithmetic consistency of the stated ranks (statement level, not counted as checks): on E × E with L = O(3O) ⊠ O(3O), a
  section in |L^d| has genus 1 + 9d^2, so the coherent space E(Y, O_Y) has dimension 9d^2 - 1, matching every rank formula
  quoted (GL_8 in degree 1, 35 and 33 in degree 2, GL_80 in degree 3); on a principal surface |9Θ| gives rank 80.

**Statement level only** (statement read; proof not read): the remaining theorems of my list in A_monodromy.tex (the
ordinary, supersingular and mixed products; the principal surfaces, ordinary and nonordinary; the A.3 rank formulas
thm:DE-A3-*; the Lang, Moore and Cartier-tensor theorems; the self-isogeny and norm-transfer "candidate" theorems;
thm:relative-ordinarity-fails-smooth; thm:root-primitive-prime-permutation-counterexamples), and the scope remarks other
than those with certificates. Many carry "-candidate" in their label while their status line says "Proved; independent
audits passed": the label is historical, the status is the run's claim.

## 6. Refuted or corrected

- **Nothing of the run is refuted** in what I checked. No gap was found in the proofs I followed.
- **Our own records, corrected by the run's results:**
  - Hunch H1 of `sweep3/SA15/HUNCHES.md` ("the answer to 8.6 is yes for d large: the monodromy of E(Y, O_Y)_ss over U_d is
    all of GL(V)") is **false as stated**: for X = P^2 and p = 2 the representation is reducible in every odd degree
    d >= 5 (thm:odd-plane-char2-obstruction, re-proved here). Refined statement, from the run: for P^2 in characteristic
    two the image is GL_g(F_2) in even degree and the stabilizer of the canonical covector in odd degree
    (thm:plane-char2-all-groups); for odd p intake part 2 confirmed the full group for plane curves.
  - `sweep3/SA15/STUDY.md` §1 says that 8.5.8's aim follows "from Illusie's generic ordinarity ... as far as I know" and
    that the "n° 7" is not in the dossier: thm:all-X-explicit-positive-rank now proves the needed positivity directly, for
    every X, with an explicit d_0 (checked here).
  - The open questions left by the sweep-3 reading of my own stretch that the run settles: 5:41 (hunch H2 of c5_c6 part
    1: yes, thm:DE-PD-pi) and 6:14 (hunch H3 of c5_c6 part 2: yes under a proper smooth lift with simply connected complex
    fibre, thm:DE-simply-connected-convergent).
- **Presentation (for an edition of the run's paper):** scope remarks written at intermediate stages are closed later in the
  same paper (rem:B-RD54-scope by thm:B-RD61; the intervals of B-RD31/B-RD34 and B-RD45 by B-RD42 and B-RD48); many
  theorem labels still end in "-candidate" while their status says "Proved".

## 7. What is new (to us), and implications

- 8.6 of cote 4 is answered for plane curves in characteristic two, in every degree, and the answer is not the one
  Grothendieck hoped for in odd degree: a canonical 2-torsion point (B_C against O_C((d-3)/2)) is invariant, so V is
  reducible; in even degree the image is all of GL(V). This is the archive's question settled in a case, with the
  obstruction proved in a few lines.
- Positivity of the unit-root rank of the vanishing cohomology for every X and d >= d_0 (with D d^n/n! asymptotics): the
  missing "n° 7" of 8.5.8.
- Full coherent and integral crystalline weak Lefschetz fail (A.1), but only off the semisimple part; Grothendieck's
  8.5.7 needed only the semisimple part, which holds.
- Implication for the SA15 records: STUDY.md §1 and HUNCHES.md H1 should carry these corrections; the deliverable rows for
  cote 4 can cite the run's theorems for 8.5.8 and 8.6.

## 8. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

1. **"Grothendieck's monodromy question (cote 4, 8.6) for plane curves in characteristic two"**: the obstruction
   (thm:odd-plane-char2-obstruction) and the exact groups in every degree (thm:plane-char2-all-groups with
   thm:all-char2-theta-orbits and the base cases d = 5, 6, 7).
   - Test 1 (complete): the obstruction yes; the exact groups yes as written, resting on the cited classification
     (Churikov-Vasil'ev-Zvezdina 2022) and on Christ-He-Tyomkin.
   - Test 2 (self-contained): yes with those citations; the base cases use ATLAS/Basheer-Moori inputs.
   - Test 3 (stable): not settled: the run is INCOMPLETE and may continue; no literature search has been done on whether
     the char-2 obstruction (a canonical theta characteristic against B_C) is known.
   - Test 4 (checked): the obstruction has my independent re-proof; the induction has a targeted check; the theta-orbit
     theorem and the base-case degenerations have not had a full check.
   - Test 5 (interest): modest outside the archive project; real for it.
   - Verdict: **not ready; two gates** (literature search; a full check of thm:all-char2-theta-orbits and the base
     cases). Not flagged.
2. **"Generic positivity of the unit-root rank of hypersurface sections, with an explicit bound"**
   (thm:all-X-explicit-positive-rank).
   - Tests 1-2: complete and elementary.
   - Test 3: a literature search is needed (generic ordinarity, Illusie 1990, Ekedahl).
   - Test 4: a targeted check only.
   - Verdict: **not ready** (literature search; an independent re-proof or computation).
3. Part B's exact least indices and the A.1 counterexamples: not candidates now. They are specialized, and the integral
   counterexamples rest on constructions I did not re-derive.

## 9. Additions after sections 3-5, and the counts

Further checks made after sections 3-5 were written:
- thm:root-primitive-prime-permutation-counterexamples: **targeted check, confirmed.** The curves are separable double
  covers of a curve of 2-rank 0; Deuring-Shafarevich gives n branch points, so the monodromy factors through S_n acting
  on F_2^n/F_2. On these five primitive (1, n) systems (n = 5, 7, 11, 13, 17) on a fixed 2-rank-0 surface, 8.6's
  "image all of Aut(V)" fails, although the module is irreducible for odd n. This is a second, different negative
  answer to 8.6, next to the odd-degree plane curves.
- thm:relative-ordinarity-fails-smooth: **targeted check, confirmed** (α_4 = Pic^0 embeds in every J_Y, so g_Y - f_Y >= 2).
  There is a surface X for which Frobenius on the vanishing cohomology is never bijective, so generic relative ordinarity
  fails for that X.
- thm:B-RD7: **necessity re-derived** (Weierstrass count me = (p-1)(A + pB), m | p+1, the supersingular j-criteria).
- Assembly checks (each theorem follows from its cited ingredients, which were not re-derived): thm:B-RD17, thm:B-RD42,
  thm:B-RD48, thm:ss-product-all-full-groups, thm:product-char2-all-full-groups, thm:DE-A3-positive-index-bounds,
  thm:compatible-cyclic-intermediate-criterion.
- Certificates. Every script cited in my 319 statements was rerun from a fresh folder of mine (109 scripts). After the
  fixes (an `outputs` folder, sibling modules) about 94 ran to completion; only those with a PASS verdict gave events. A few could not run:
  - Unix-only calls (signal.SIGALRM, resource);
  - missing probe inputs;
  - two that call subprocess, which I skipped.
  This gave 67 events on remarks and 49 on theorems. A theorem's event comes from the scope remark that follows it, and
  covers only the finite computations of its proof.

**Counts (statement_id rows of the TSV).** Of the 319 ids:

| Best check per id | Ids |
|---|---:|
| independent re-proof (mine) | 1 |
| targeted proof check (mine; 38, of which 7 assembly-only and 1 necessity-only) | 38 |
| computation or formal certificate (mine; 147, of which 2 partial reruns; almost all are reruns of the run's code) | 147 |
| carried as background without fault found (mine) | 3 |
| refuted, with the refined statement | 0 |
| checked by the earlier intakes only (19 events re-filed under the bare id) | 19 |
| read at the level of the statement only | 111 |

The TSV has 208 rows: 189 events of mine and 19 re-filed. Some ids carry several events; the table counts each id once,
at its strongest type.

**Refutations: none of the run.** Our own hunch H1 (sweep3/SA15/HUNCHES.md) is refuted as stated (section 6).

**Read at the level of the statement only (111 ids).** The list is in the order of the ledger:
rem:B-RD54-scope, rem:Cartier-kernel-wall-inertia-scope, rem:DE-A3-mixed-axis-scope, rem:DE-A3-positive-Petri-radical-scope-note, rem:DE-A3-positive-bundle-scope, rem:DE-A3-positive-cup-derivative-scope-candidate, rem:DE-A3-positive-index-gate, rem:DE-A3-positive-index-variation-candidate, rem:DE-A3-positive-monad-gate-note, rem:DE-A3-positive-norm-pencil-scope-candidate, rem:DE-A3-positive-smooth-pencil-scope, rem:DE-A3-positive-trace-probe-scope, rem:DE-A3-residual-pencil-boundary-scope, rem:DE-A3-symmetric-boundary-kernel-scope, rem:DE-A3-twisted-pencil-lift-scope, rem:DE-A4-product-Frobenius-interpolation-scope, rem:DE-E2-coherent-derived-heart, rem:DE-Lang-deck-slice-scope, rem:DE-Lang-main-orbit-scope, rem:DE-Lang-polar-irreducibility-scope, rem:DE-Lang-wedge-pole-scope, rem:DE-common-Cartier-incidence-scope, rem:DE-compatible-residual-module-scope, rem:DE-five-evaluation-fibre-scope, rem:DE-general-odd-source-scope, rem:DE-odd-Cartier-evaluation-scope, rem:all-theta-fixed-point-jets-scope-candidate, rem:compatible-cyclic-intermediate-scope, rem:cubic-component-norm-transfer-scope-candidate, rem:generic-mixed-modulus-gate, rem:good-theta-norm-transfer-scope-candidate, rem:nonordinary-arbitrary-odd-neighbor-scope-candidate, rem:nonordinary-even-addition-scope-candidate, rem:nonordinary-odd-block-scope-candidate, rem:nonordinary-polar-stability-gap-candidate, rem:nonordinary-ppav-degree-one-next-gate-candidate, rem:nonordinary-three-torsion-triple-scope-candidate, rem:odd-full-hyperplane-inertia-scope, rem:p-rank-one-polar-unit-certificate-candidate, rem:p-rank-zero-polar-unit-certificate-candidate, rem:p-rank-zero-ppav-degree-one-scope-candidate, rem:ppav-twisted-Cartier-Moore-scope, rem:primitive-prime-generic-rank-scope, rem:principal-theta-Cartier-bridge-scope, rem:root-nonordinary-odd-theta-nodality-scope, rem:root-theta-avoidance-scope, rem:root-three-neighbor-boundary-scope-candidate, rem:root-trigonal-direct-scope-candidate, rem:ss-self-tacnode-global-gate, rem:three-theta-conditional-geometric-gates-candidate, rem:uniform-seven-scope-candidate, rem:uniform-thirteen-verification-scope-candidate, thm:B-RD10, thm:B-RD100-ambiguity, thm:B-RD100-exact, thm:B-RD12, thm:B-RD23, thm:B-RD26-wild, thm:B-RD31, thm:B-RD34, thm:B-RD45, thm:B-RD49, thm:B-RD52, thm:B-RD62, thm:B-RD63-arc, thm:B-RD74-upper, thm:B-RD98-irreducible, thm:DE-A3-mixed-index-ordered-ranks, thm:DE-A3-mixed-thin-all, thm:DE-A3-ss-product-rank, thm:DE-Lang-polar-irreducible, thm:DE-Lang-theta-wedge-quotient-bound, thm:DE-compatible-residual-module-sum, thm:DE-odd-polarization-Cartier-surjection, thm:OC-explicit-integral-counterexample, thm:OC-product-exact-degrees, thm:cubic-component-arbitrary-odd-norm-transfer-candidate, thm:every-nonordinary-ppav-degree-one-full-candidate, thm:generic-mixed-product-all-groups-candidate, thm:generic-nonordinary-ppav-groups-candidate, thm:good-theta-odd-norm-step-candidate, thm:mixed-every-fixed-modulus-all-even-candidate, thm:nine-theta-arbitrary-odd-norm-candidate, thm:nonordinary-arbitrary-odd-neighbor-candidate, thm:nonordinary-even-addition-candidate, thm:nonordinary-ppav-odd-natural-block-candidate, thm:nonordinary-ppav-polar-stable-conditional-candidate, thm:odd-cover-full-hyperplane-inertia, thm:ordinary-ppav-Hasse-kernel, thm:ordinary-products-Hasse-irreducible, thm:p-rank-zero-ppav-degree-one-full-candidate, thm:ppav-non-two-torsion-cross-Cartier, thm:ppav-three-theta-jets, thm:prime-Heisenberg-birational-radical, thm:primitive-prime-generic-curve-rank, thm:product-Hasse-irred, thm:root-every-nonordinary-ppav-degree-three-full-candidate, thm:ss-all-odd-Hasse, thm:ss-all-odd-full-groups, thm:ss-even-full-group-if-unit-Hasse-irreducible, thm:ss-even-unit-Hasse-irreducible, thm:ss-product-degree-one-full-group, thm:ss-product-degree-three-full-group, thm:ss-product-degree-two-full-group, thm:ss-rectangular-all-degrees, thm:ss-uniform-GL8-block, thm:three-theta-conditional-full-image-candidate, thm:uniform-eleven-nodal-self-isogeny-candidate, thm:uniform-f0-five-self-isogeny-nodal-candidate, thm:uniform-seven-nodal-self-isogeny-candidate, thm:uniform-thirteen-nodal-self-isogeny-candidate

These are mostly the scope remarks of the A.3 positive-index programme and the nonordinary principal surfaces, the
remaining Part B theorems without a certificate-bearing remark (B-RD7 aside), and the self-isogeny and norm-transfer
theorems. A successor intake should give targeted checks first to:
- thm:all-char2-theta-orbits (a full check);
- thm:ss-all-odd-full-groups;
- thm:ordinary-ppav-eventual-full;
- thm:primitive-prime-generic-curve-rank;
- thm:B-RD12, thm:B-RD23, thm:B-RD26-wild and thm:B-RD100-exact.
They carry the run's main positive and exact answers.

## 10. Round 2 (22 Nov, at the coordinator's request): the 8.6 chain in full, then certificate rows read

**The exact plane groups in characteristic two (8.6 for X = P^2, p = 2): the whole chain is now checked.**
- thm:all-char2-theta-orbits: **full check**, every step re-derived (new event; the earlier partial one stays). It covers:
  - lem:contact-conductor: contact reciprocity, the conductor inclusion through the branch valuations, and
    h^0(J) >= t (+1 when t > 0);
  - lem:no-low-degree-contact: the incidence bound recomputed as N_d - s(d-s-3)/2 - |eps|/2 + t;
  - the canonical incidence of dimension N_d, the exclusion of effective θ_Q, the nodal descent condition (linear after
    square roots in characteristic 2), and the nonreduced forms R^2 S.
  - The input the proof states without proof, that every noncanonical theta characteristic is effective, I proved: for
    M != 0 in Pic[2], tensoring 0 -> O -> F_*O -> B -> 0 by M and using F_*O ⊗ M = F_*(M^2) = F_*O puts k inside
    H^0(B ⊗ M). The quintic proof also gives this argument, citing Stöhr-Voloch through Ishitsuka-Ito, Thm 3.1.
- The base cases, each read in full and checked (new events):
  - thm:quintic-char2-monodromy: contact conics, dim I = 20 = dim S; the reducible conics at 19; the maximal subgroups of
    2^5:GL_5(2), with their orders and divisibility by 7 and 31 recomputed;
  - thm:sextic-full-monodromy: contact cubics, 27 = 27; every singular stratum at 24-26; the element of order 31 with a
    non-reciprocal factor; the Hering alternatives excluded, with group orders recomputed;
  - thm:septic-stabilizer-monodromy: contact quartics, 35 = 35; all strata at 32-34, including my recomputation of the
    normalization-genus bounds; H = GL_14(2) on the quotient; the unipotent kernel all present.
- The quartic base case (GL_3(F_p) for plane quartics) is Achter-Pries 2008, Prop. 4.8, applied through the PGL_3-torsor
  over the nonhyperelliptic locus of M_3. It is a published result, carried as background; it is not a row of my list.
- thm:plane-char2-all-groups: upgraded. Within the cited classifications (Churikov-Vasil'ev-Zvezdina 2022, Lemma 3.3;
  Basheer-Moori 2021, Table 1) and Achter-Pries 2008, the exact groups in every degree d >= 4 are confirmed:
  - GL_g(F_2) for even d;
  - the full stabilizer 2^{g-1}:GL_{g-1}(F_2) of the canonical covector for odd d.
- **Hexagon candidate 1, revised.** Tests 1, 2 and 4 now hold for this chain:
  - test 1: complete as written;
  - test 2: inputs published and cited;
  - test 4: my targeted checks of every step, and my independent re-proof of the odd-degree obstruction.

  Test 3 is still open: a literature search on the characteristic-2 theta-characteristic monodromy of plane curves, and
  whether a successor run is planned. Test 5 is modest outside the archive project. So it is **one gate away**, but not
  flagged at once, since test 5 is not strong.
- **Abelian surfaces, supersingular product E × E (8.6 for X = E × E, p = 2).** thm:ss-all-odd-full-groups: proof read in
  full and its structure checked: the relative bundle is Ω^1 of P(H^0(L^d)); irreducibility; the group is generated by
  transvections (stable rank drops by one on the single Hasse divisor; purity on projective space); the GL_8 block excludes
  every invariant alternating form, which leaves SL = GL in the Kantor-Seress / McLaughlin list. Its inputs
  thm:ss-all-odd-Hasse and thm:ss-uniform-GL8-block are still at statement level (the GL_8-block proof is a long
  jet-and-nodal-image argument, A_monodromy 8247-8420, not yet checked).
- **Part B, the exact indices.**
  - Assembly checks: thm:B-RD73 (ν = 2 exactly for p < e < p^3), thm:B-RD61 (ν = 1 at e = p - 1), thm:B-RD100-exact (ν = 3
    at e = 2p(p-1)). For B-RD100 the coefficient recurrence gives q_1 = 2p-1, q_2 = 2p^2-1, q_3 = 2p^3-1, and the stated
    surplus 2p-1 corresponds to N = p^2 - 1.
  - thm:B-RD26-wild: the arithmetic of its existence construction verified by my own script on 1,182,275 parameter cases
    (3 | A, A >= 3^{2r}, A < 3^{2r+2} unless r = n-1, and the parity conditions for m = 6, 12).
- **The supersingular product chain, continued.** thm:ss-uniform-GL8-block was read in full and its global steps and
  arithmetic checked:
  - odd d: the self-isogeny with phi^dagger phi = [d], the norm line bundle equal to L^d, 9(d^2-1) nodes and stable rank
    9d^2 - 1, the prime 31;
  - even d: f_Y = 9d^2 - 3, the node permutation group S_N, the prime 11, which does not divide |GL_8(F_2)|;
  - both parities: Goursat and H^1 = 0.

  thm:ss-all-odd-Hasse and thm:ss-even-unit-Hasse-irreducible were checked at their global and degree steps; the latter
  rests on 9(d-1)^2 + (18d-9) = 9(d-3)^2 + (54d-81) = 9d^2, (d-4)^2 = 6 having no integer solution, and 135 against 81 +
  63. thm:ss-even-full-group-if-unit-Hasse-irreducible: structure checked. With these, the full groups on E × E
  (E supersingular, p = 2) in every degree are checked down to their supporting lemmas, namely:
  - the norm-family and tangent-triple lemmas;
  - the nodal-image transversality;
  - lem:char2-defect-one-inertia, lem:irreducible-hasse-quotients-trivial;
  - the cited classifications (Kantor-Seress 2001; Entin 2021).
- Also checked in this round: thm:DE-A3-ss-product-rank (lower bounds re-derived: the isogeny pullback C_1 + C_2 with m^2
  nodes and stable rank m^2 - 1; the union of two members for even m with rank m^2 - 3; the upper bound rests on
  lem:DE-A3-ss-prym).

**Running counts after round 2 so far** (best check per id): independent re-proof 1, targeted proof check 50, computation
or formal certificate 143, carried as background 3, earlier intakes only 19, statement level 103 (of 319). Refutations of
the run: none.
- **Independent computations in this round.**
  - thm:ss-product-degree-two-full-group: I rebuilt the Cartier matrices from the elliptic rules with my own code
    (scratchpad `ss_deg2.py`) and reproduced every certificate claim: ranks 33, det(TI - C(s_1)) = T^3 (T+1) f with f
    irreducible (binary integer 4853921047), rank(C(s_2) - I) = 35, and (C(s_2) - I) mu = lambda.
  - thm:ss-product-degree-three-full-group: the degree-80 polynomial checked (irreducible, not reciprocal, a root of
    order divisible by the prime 4278255361 with ord = 80).
  - thm:ss-product-degree-one-full-group: T^8+T^7+T^5+T+1 checked (irreducible, not reciprocal, root order 85).
  - thm:product-Hasse-irred: global argument checked.

**Round 2, second part (after a compaction; machine clock 22 Nov 2026, 00:38-01:3x UTC).** Every row that was at
statement level has now been read with its proof. None remains at statement level.

- **8.6 on principally polarized and product surfaces, characteristic two.**
  - Ordinary products and ordinary ppav: thm:ordinary-products-Hasse-irreducible (its symmetrizer and squarefreeness
    lemmas recomputed by hand), thm:ppav-three-theta-jets (full), thm:ppav-level3-Cartier-symmetric (full; upgraded from a
    rerun), thm:ordinary-ppav-Hasse-kernel, thm:ordinary-ppav-eventual-full. For the last, the text only says "opened
    classification" for the symmetric-group case of Kantor-Seress; I supplied the exclusion (a subgroup of S_m fixing
    a codimension-8 subspace of the deleted permutation module moves at most 22 points, while GL_8(2) has minimal
    permutation degree 255).
  - Nonordinary ppav in degree one: the conditional polar-stable theorem, the two-rank-zero and two-rank-one normal
    forms, and thm:every-nonordinary-ppav-degree-one-full-candidate. thm:nonordinary-ppav-all-covectors: all twelve
    entries of its Cartier table recomputed by hand, giving 2^f invariant covectors in even degree and none in odd degree.
  - Higher degrees: the odd natural block, the three-theta conditional theorem, generic mixed products, all even mixed
    degrees, the generic nonordinary groups, even addition, the five-, seven-, eleven- and thirteen-self-isogenies, the
    good-theta and nine-theta norm steps, the arbitrary odd neighbour, the cubic-component transfer and degree three on
    every nonordinary surface. Their assemblies and all dimension counts were checked (for example R = 18t+8 and
    8+17t > R/2; 80+161t > 81t+40; r+(18e^2-1)t = R-t).
  - Ranks and the Lang programme: thm:ss-rectangular-all-degrees, thm:DE-A3-mixed-thin-all,
    thm:DE-A3-mixed-index-ordered-ranks; thm:DE-Lang-polar-irreducible, thm:DE-Lang-theta-wedge-quotient-bound (its
    characteristic-two vanishing of H^0(P^(N-1), Omega^k(t)), t <= k, through the exterior Euler sequence),
    thm:DE-compatible-residual-module-sum (the group-algebra identities over F_2), thm:DE-odd-polarization-Cartier-surjection,
    thm:prime-Heisenberg-birational-radical, thm:primitive-prime-generic-curve-rank, thm:odd-cover-full-hyperplane-inertia,
    thm:ppav-non-two-torsion-cross-Cartier and, in part, thm:DE-Moore-singular-parameters (its support lemma not reread).
  - Part A.1: thm:OC-explicit-integral-counterexample, with lem:OC-explicit-differential-bound checked line by line
    (35+556 = 591, so h^0(Omega^1_X) <= 591.9^556 < m-1), and thm:OC-product-exact-degrees.
- **Part B.** The 13 remaining theorems were read in full and their arithmetic re-derived: B-RD10 (every index recipe and its
  exceptions), B-RD12 ((B.12.4) to (B.12.5) and the criterion (B.12.1)), B-RD23 (all valuations of the full-nine
  construction; m = 4 excluded at e = 24, 30, 42, 48 by (B.12.1)), B-RD31, B-RD34, B-RD45, B-RD49, B-RD52, B-RD62,
  B-RD63-arc, B-RD74-upper, B-RD98-irreducible (the decisive N(p^4-3p^3+1) > 0) and B-RD100-ambiguity.
- **The 52 scope remarks.** Each was read in full and compared with its theorem; none claims more than its theorem. Two
  are stale within the paper (presentation only):
  - rem:Cartier-kernel-wall-inertia-scope says that the nonemptiness of H_U is not asserted; it is supplied later by
    prop:odd-cover-common-rank-wall-nonempty and used in thm:odd-cover-full-hyperplane-inertia;
  - rem:B-RD54-scope is closed by thm:B-RD61 (section 6).

  B-RD31, B-RD34 and B-RD45 are intermediate bounds superseded by B-RD42 and B-RD48, as their own proofs say.
- **Independent computations (my own code, in my scratchpad).**
  - `ss_deg1.py`, both certificates of thm:ss-product-degree-one-full-group: the third Frobenius iterate has
    characteristic polynomial T(T^8+T^7+T^5+T+1); the transvection data are exact (ranks 8 and 7, u, s_0.u = 0,
    v = (0,0,0,0,4,3,0,5,5)); the relative determinant has valuation one along the line.
  - `polar_p0.py` and `polar_p1.py`, for two-rank zero and two-rank one. From each displayed trivector I computed:
    - the nine 8-Pfaffians, which are x_i times one cubic;
    - its polar B, equal to the displayed one;
    - the 81x81 Lie-stabilizer minors, which are 1 in F_2[a,b,c] and b^4 in F_2[a,b] as stated.
- **Reruns of the run's own code** in my folder:
  - PASS: `verify_nonordinary_seven_good_parameters.py` (only its Unix SIGALRM lines removed in my copy),
    `verify_p3_ranges.py` (its exceptions agree with my hand derivation) and `verify_full9_construction.py`;
  - not rerunnable: `verify_nonordinary_thirteen_certificates.py`. Its five stored coefficient outputs are not in
    checkpoint 37.
- **A correction of my own.** In the row for thm:ordinary-ppav-eventual-full I first wrote that a GL_8(2) block would move
  at most 18 points, and compared its order with 20!. That bound was wrong. I corrected the row to the argument above.
- **Open gates the run states itself** (not errors):
  - sharp ranks in positive polarization index on mixed surfaces (the variation-image bound (DE-PT6));
  - generation of the whole image by hyperplane radicals in the odd-cover and Lang programme;
  - fixed two-rank-zero surfaces in odd degrees not divisible by 3, 5, 7, 11 or 13 (first 17);
  - two-rank one in degrees 5 and 8.
- **Hexagon.**
  - Candidate 1 (the plane-curve chain) is unchanged.
  - A possible third candidate: GL_8(F_2) in degree one on every nonordinary principally polarized surface in
    characteristic two. My checks cover the whole chain except lem:root-nonordinary-Coble-identification-candidate,
    which is not in my list, and the cited Rains-Sam results. It is not ready: that lemma needs a check, and the
    literature search has not been done.
- **Clock.** The clock times in my notes file before 00:38 UTC were estimates and are wrong. The TSV timestamps are the
  machine clock.

**Counts after these items** (best check per id, 319 ids):

| Check | Ids |
|---|---|
| independent re-proof | 1 |
| targeted proof check | 154 |
| computation or formal certificate | 142 |
| carried as background without fault found | 3 |
| earlier intakes only | 19 |
| statement level | 0 |

13 ids carry both a targeted check and a computation of their own. Refutations of the run: none. Remaining for item (2):
50 theorem rows whose only own event is a certificate rerun. Their proofs are being read next, and they are listed below
as they are done.

**Item (2), the certificate-only theorem rows (machine clock 22 Nov, about 01:3x-01:5x UTC).** I read the proofs behind
the following and recorded new targeted events. Each row keeps its rerun event.
- 8.6 in degree one and two, and the eventual theorems:
  - thm:mixed-every-fixed-modulus-degree-one-candidate, -degree-three-candidate and -all-odd-candidate;
  - thm:every-nonordinary-ppav-degree-two-full-candidate;
  - thm:nonordinary-degree-three-from-neighbour-candidate;
  - thm:RD-A4-three-step;
  - thm:ordinary-products-eventual-full;
  - thm:ss-product-degree-two-full-group. Its group argument is now checked as well, including why the irreducible f
    of degree 32 forces the primitive prime 65537. Its certificates I had recomputed earlier.
- The relative ranks: thm:ss-product-two-axis-cross-squarefree, thm:DE-A3-mixed-all-product-ranks,
  thm:DE-A3-ordinary-arbitrary-embedding and thm:DE-A3-all-ss-rectangles.

**Not yet read beyond their reruns: 38 theorem rows.**
- Part B: B-RD8, B-RD26-wild (whose construction arithmetic I verified by my own script), B-RD57, 58, 59, 64-72, 75, 78,
  80, 82, 90-96 and 99.
- The DE-A3 rank theorems: mixed-generic, mixed-nonproduct, ordinary-all, ppav and separable.
- thm:DE-Moore-Fermat-nondivisibility, thm:DE-SS-odd-pullback-dual-rank, thm:DE-primitive-one-three-full-image,
  thm:OC-exact-integral-injectivity-degrees, thm:mixed-every-fixed-modulus-degree-two-candidate,
  thm:mixed-three-by-b-full-groups-candidate and thm:ss-product-exact-covectors.

They carry a rerun of the run's own code, and nothing more from me. The remaining 92 certificate-only ids are remarks
that hold a certificate.

**Final counts** (best check per id, 319 ids):

| Check | Ids |
|---|---|
| independent re-proof | 1 |
| targeted proof check | 166 |
| computation or formal certificate | 130 |
| carried as background without fault found | 3 |
| earlier intakes only (re-filed) | 19 |
| statement level | 0 |

25 ids have both a targeted check and a computation. In total the TSV has 346 rows: 327 events of mine and 19 re-filed
rows. Refutations of the run: none.
