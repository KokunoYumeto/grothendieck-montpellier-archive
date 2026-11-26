# Paper seed: GCT_PLETH, positive plethysm formulas (register H20 and H21)

Seed by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 22 Nov 2026, for the main session (Claude Opus 5.5
at effort max). The results are by GPT-6 Astra (ChatGPT Pro mode), effort not exposed, in two runs that have ended:
GCT_PLETH (checkpoint 09, 21 Nov) and GCT_POS (final, 22 Nov). One paper is proposed.

Two path prefixes are used below:
- `PL` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped`
- `POS` = `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GCT_POS_final_20261122T0219Z_unzipped`

## Read this first: three claims of ours that the paper must not repeat

1. **"The first polynomial-size #P descriptions with varying outer degree"** (my intake part 4, §3) is false as worded.
   Pak-Panova-Swanson (arXiv:2511.02312, v1 4 Nov 2025) give positive interpretations of ⟨s_μ[s_ν], s_λ⟩ for every μ
   and ν when λ has at most two rows. Narayanan (arXiv:2403.03443) gives the hook restriction coefficients positively.
2. **"Polynomial bit complexity" and "in #P" are not the news for fixed |μ|.** Kahle-Michałek give piecewise
   quasi-polynomials for every fixed μ, computed for |μ| ≤ 5. Fischer-Ikenmeyer record that the coefficient is then
   computable in polynomial time, and a nonnegative function computable in polynomial time is in #P. What is ours is
   the explicit positive structure and the complete list of zeros.
3. **The stable hook series is essentially known.** It is Macdonald's specialization of s_ν[(1−z)/(1−q)], and the
   bigraded multiplicities of Specht modules in Sym ⊗ Λ are credited to Kirillov-Pak and Molchanov. Ours are the
   reduction with its exact range, the single polytope and the support test.

---

## Paper 1

### Title

**Every vanishing plethysm coefficient of outer degree five, with positive formulas in degrees four and five and in
stable families**

A shorter one: **Plethysm in degree five: positive formulas and all the zeros**

### Notation

For partitions μ ⊢ m and λ ⊢ mn, p^λ_{μ,(n)} = ⟨s_λ, s_μ[h_n]⟩ is the multiplicity of S_λ V in S_μ(Sym^n V). W is the
(m−1)-dimensional standard representation of S_m, and [ν] the Specht module.

### The main theorem, at its exact strength

**Theorem A (outer degree five: all zeros).** Let n ≥ 0, μ ⊢ 5, λ ⊢ 5n. If λ has more than five rows the coefficient
is 0. Otherwise put d = λ₅ and g = (λ₁−λ₂, λ₂−λ₃, λ₃−λ₄, λ₄−λ₅), and let ν = μ for even d, ν = μ′ for odd d.
- **g = 0:** only ν = (5) occurs, with multiplicity one.
- **All four gaps positive:**
  - the five middle labels (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1) always occur;
  - the two one-dimensional labels both vanish exactly on g = (L,1,1,1) and (1,1,1,L), L ≡ 1 mod 5;
  - the trivial label also vanishes on (1,2,2,1) and (2,1,1,2);
  - there is no other zero.
- **Some but not all gaps zero:** write g = (a,b,c,e), L₁ = max(1, 3b+2c+e), L₄ = max(1, a+2b+3c), and normalize g to
  (L₁ + ((a−L₁) mod 10), b, c, e) if a ≥ L₁, else to (a, b, c, L₄ + ((e−L₄) mod 10)) if e ≥ L₄, else to g itself. The
  coefficient is zero if and only if the normal form is one of 344 listed vectors and ν is one of the labels listed
  for that vector.

So the support is decided by a fixed table and a bounded number of integer operations.

**Theorem B (outer degrees four and five: positive formulas).**
- For every μ ⊢ 4 and every n and λ, the coefficient is the number of integer points of at most 108 explicitly tagged
  bounded rational polytopes, each in at most five variables (36 for μ = (4) and (1⁴); 72 for (2,2)). The proof is an
  S₄-equivariant freeness theorem: with W the sign-twisted standard module, R = Q[q,t]/(q·t) is isomorphic to
  Sym(U) ⊗ H, U = [(2,2)] in degree (2,0), with every graded piece of H given explicitly.
- For every μ ⊢ 5 and every n and λ, it is the number of integer points of at most 152 such polytopes, each in at most
  eleven variables. All data are fixed. The evaluation uses a fixed number of arithmetic operations and binomial
  coefficients of order at most six.

**Theorem C (varying outer degree, stable tails).** Let m ≥ 3, t ≥ 0, n ≥ a+t, μ ⊢ m, and ν = μ for even t, μ′ for
odd t.
- **Hooks.** For a ≥ 1, 0 ≤ r ≤ m−2 and λ = (mn−a−(m−1)t−r, a+t, (t+1)^r, t^(m−2−r)), the coefficient equals the
  multiplicity [S_(a,1^r) W : ν]. It is the number of integer points of one polytope in at most m²+3m−4 variables,
  and its support is given by a closed criterion:
  - for ν ≠ (m), let C be the cells of ν other than (1,1), (2,1), with weights j−i+1, and let L be
    b(ν) = Σ(i−1)ν_i plus the r smallest of these weights. With D = a+r the coefficient is positive iff D ≥ L and
    not (D = L+1, ν rectangular, r ∈ {0, m−2});
  - for ν = (m), put L₀ = (r+2)(r+3)/2 − 1. It is positive iff D ≥ L₀ and not (r = m−2, D = L₀+1).
- **Two-row tails.** For a ≥ b ≥ 2 and λ = (mn−a−b−(m−1)t, a+t, b+t, t^(m−3)), the coefficient equals
  [S_(a,b) W : ν], and:
  - b = 2: at most C(m,2)+4 polytopes, each in at most 3m−3 variables, by a displayed positive series;
  - b = 3: at most C(m,2)+7 polytopes, each in at most 3m−1 variables, likewise;
  - every fixed b: a positive polytope formula whose construction, evaluation and support decision cost
    f(b)(m + bits(a,t,n,μ) + 1)^g(b), with computable f and g.

The size bounds are in m and the binary lengths of the other parameters. At t ≥ 1 that is polynomial in the ordinary
input, since λ then lists m positive parts. At t = 0 no bound in log m is claimed. Nothing is claimed for b varying
without bound.

**Unpublished inputs:** none from outside the run. Every lemma used is in GCT_PLETH and has to be proved in the paper:
the balanced module and stable chart (G-015, T-032 to T-036), and for degree five G-021, G-027, G-028, G-033, G-034,
G-035, T-049, T-059, as their proofs use them. A, B and C use neither GRH, nor Alpöge, nor Masullo.

**What it implies, and no more:**
- nonvanishing in outer degree five is completely known, off-chamber walls included;
- fixed outer degree four and five have manifestly positive formulas, which Kahle-Michałek's signed
  quasi-polynomials do not give;
- restriction coefficients of S_(a,b)(C^m) to S_m get positive formulas for each fixed b, since S_(a,b)(W ⊕ 1) is the
  sum of S_γ W over the interlacing γ. This last corollary is derived here; it must be proved and searched;
- it solves GCT VII Problem 1.1 only in these families. It gives no positive formula for general plethysm, and no
  statement about P versus NP, Foulkes' conjecture or saturation.

### Why it matters

A plethysm coefficient counts how often one irreducible representation occurs in a composite of two Schur functors.
Stanley asked for a positive rule for these numbers, and Mulmuley made such a rule a problem of geometric complexity
theory. Signed formulas can't show when a coefficient is zero. Here every zero in outer degree five is listed and
every value is counted by polytopes. The stable families show where a positive rule survives when the outer degree
itself grows, and exactly which parameter still blocks a uniform rule (the second row of the tail).

### The works it continues, corrects or answers

| Work | Statement and place | Relation | Status |
|---|---|---|---|
| Mulmuley, GCT VII, arXiv:0709.0749 | Problem 1.1 (Plethysm problem) | answers it for these families | **source opened** (`main.tex`); arXiv number from memory |
| Kahle-Michałek, *Plethysm and lattice point counting*, arXiv:1408.5708, Found. Comput. Math. 16 (2016) | abstract; the theorem labelled `t:big` (piecewise quasi-polynomial, computed for \|μ\| = 3, 4, 5) | continues: signed to positive, and all zeros | **source opened** (LaTeX); page and printed number from the PDF still needed |
| Kahle-Michałek, *Obstructions to combinatorial formulas for plethysm*, arXiv:1507.07131, EJC 25 (2018) P1.41 | Theorem 5: some rays are no homogeneous Ehrhart function | the reason that finitely many, possibly inhomogeneous, polytopes are used | from memory and the runs' source audit |
| Fischer-Ikenmeyer, complexity of plethysm | NP-hardness theorem (inner degree fixed ≥ 3); Proposition `prop:plethysm-dichotomy` (P for fixed \|μ\|) | bounds what may be called new | **source opened** (`sections/results.tex`); bibliographic data and page still needed |
| Sarkar, *Stability of plethysm coefficients and modified polynomial induction*, arXiv:2610.07929v2 | Theorem D = 6.4; Theorem E = 7.3 (four columns); the remark after it (five columns by Littlewood-Richardson, six by decomposing Λ(Λ³C⁶)) | T-012 and T-013 carry out that remark for five and six columns | **source opened** (LaTeX, introduction and remark) |
| Pak-Panova-Swanson, arXiv:2511.02312v3 | abstract: positive marked-tree rule for two-row λ, all μ and ν | must be credited and compared with Theorem C | **source opened** (arXiv abstract page); theorem number and page still needed |
| Narayanan, *Hook restriction coefficients*, arXiv:2403.03443v2 | Theorem 5.7: positive rule for hook restriction from GL_n to S_n, on Cⁿ | near Theorem C, hooks; our module is W | **source opened** through a fetched summary of the HTML; reread the theorem |
| Lee, *Restriction coefficients for partitions with at most three columns*, arXiv:2506.11837v2 | Theorems 1.1 and 1.3 | neighbouring range | **source opened** through a fetched summary of the HTML |
| Narayanan-Paul-Prasad-Srivastava, arXiv:2211.15252 | trivial and sign restriction coefficients | neighbouring range, two-row and hook | search result and from memory |
| Macdonald, *Symmetric functions and Hall polynomials*, 2nd ed. | I §3 Examples 2-3, p. 45 | gives the hook series | from memory and the run's citation |
| Kirillov-Pak 1990; Molchanov 1992 | bigraded multiplicity in Sym W ⊗ ΛW | prior form of the hook series | from memory; a search confirmed the attribution to Kirillov-Pak only |
| Solomon, *Invariants of finite reflection groups*, Nagoya Math. J. 22 (1963) | §3, theorem p. 59 | invariant branch of the hooks | from memory and the run's citation |
| Aschenbrenner, *Ideal membership in polynomial rings over the integers*; Liang, arXiv:1905.07517v3 | Theorem 3.2; Corollary 42 | degree bounds in the fixed-b algorithm | from memory and the run's citations |
| Manivel; Brion; Littlewood | stability of plethysm in the first row; restriction as plethysm | the stable reduction is classical in substance | from memory; locators needed |

It corrects no published theorem that I know of.

### The other results, in the order of the argument

1. The balanced module, the stable chart, and the reduction to Schur functors of W (G-015, T-032, T-033).
2. Outer degree four: chambers, four-point model, freeness, polytopes (T-034 to T-037).
3. Outer degree five: the two-row five-point formula (G-021), the walls (G-033, G-034), the two remaining regions
   (T-059, G-035), the assembly (G-036).
4. All zeros in degree five: the strict chamber (G-028), then the walls and their finite closure (G-031).
5. Stable hooks (G-037), then b = 2, 3 (G-038, G-039), then fixed b (G-040).
6. Hooks just outside the stable range, n = a+t−k: jets and a parameterized positive formula for a ≥ 2k
   (T-062 to T-065). Its polytope bound is exponential in k through Stirling numbers.
7. Stable Foulkes tails of width five and six (T-012, T-013), as the completion of Sarkar's remark.
8. The limits:
   - PNEW-010: at m = 2r, b = r(r+1)+1 the cover used by the fixed-b construction needs at least 2^(r−1) generators,
     so that construction is not polynomial in b. This is no lower bound on other formulas.
   - PNEW-012: for two-row output in outer degree six, at most 45 polytopes in at most 11 variables. It compiles
     Pak-Panova-Swanson and is credited to them.

### The research question of the prompt

> **Give a positive formula for [S_(a,b) W : ν], uniform in the second row b: a #P description of size polynomial in
> m, b and the bit length of a, for every ν ⊢ m, with an exact support criterion.**

It would turn Theorem C from "each fixed b" into all two-row stable tails, and with them all two-row restriction
coefficients from GL_m to S_m.

**Current gate.** The finite cokernel C_ν of the polarization map in G-040. PNEW-010 proves that a minimal cover of it
can have 2^(r−1) generators, and the Aschenbrenner and Liang bounds are doubly exponential in the number of low
variables (at most b−2). So the basis itself has to be avoided, and only compressed or bijective counts remain.

**Routes not yet tried in our runs:**
- S_(a,b) W as the sl₂-highest vectors of bidegree (a,b) in Q[W ⊕ W], with a positive basis of diagonal invariants
  (bipartite P-partitions, descent monomials) made compatible with the lowering operator;
- the marked trees and the KOH identity of Pak-Panova-Swanson, with two gradings in place of one;
- Narayanan's two sign-reversing involutions, extended from one column to one row in the tail;
- a succinct basis of C_ν indexed by partitions with at most b parts, counted by a dynamic program and never listed;
- the corresponding algebraic-geometric statement: sections of twisted ideal sheaves of the m simplex points on P(W),
  with a degeneration that splits the first jets.

The next question after it: every zero and a positive formula in outer degree six beyond two-row output. The checked
reference table has 5,214 coefficients (POS, R-NEW-001).

### Proofs, programs and checks

The TeX lines are those of `PL\GCT_PLETH.tex`. "Run" means GPT-6 Astra (ChatGPT Pro mode), effort not exposed. "Intake"
means Claude Opus 5.5 at effort high, agent a0805369bae2ebddc.

| Result | TeX lines | Working proof: file, lines | Program or data | Checked by the run | Checked by the intake |
|---|---|---|---|---|---|
| T-012 | 2641-2757 | `PL\work\theta\few_columns_report.md` 100-172 | `few_columns.py`, `EXTERIOR_CUBE_RANK_5.tsv` in that folder | whole argument, two agents; table | targeted proof check; table recomputed; lattice sums not evaluated |
| T-013 | 2758-2931 | the same file, 173-273 | `EXTERIOR_CUBE_RANK_6.tsv` | the same | targeted proof check; 156-row table recomputed; lattice sums not evaluated |
| T-032 to T-036 | 5255-6169 | `PL\work\root\general_fiber_model.md` 1-195; `PL\work\theta\general_chart_report.md` 1-143; `PL\work\theta\outer4\chamber_report.md` 1-247; `four_fibers_report.md` there, 1-299 | `check_chambers.py` | see PL check events | proofs not read |
| T-037 | 6170-6689 | `PL\work\theta\outer4\full_outer4_report.md` 1-413 | `outer4_positive.py`, `check_outer4_positive.py` | whole proof, two agents; computations | 60 of 60 table rows recomputed; proof not read |
| G-015 | 6690-6882 | paper | none | reviewed (A-series) | proof not read |
| G-021 | 12003-12627 | `PL\work\root\five_point_two_row_report.md` 1-535 | through the router | reviewed | proof not read |
| G-028 | 14545-14814 | `PL\work\root\five_row_strict_nonvanishing.md` 1-253 | `FIVE_ROW_STRICT_CERTIFICATE.json` | reviewed | covered by the G-031 computation |
| G-033 | 16921-17285 | `PL\work\root\all_order_zero_twist_report.md` 1-369 | through the router | reviewed | proof not read |
| G-034 | 17917-18395 | `PL\work\root\all_order_one_twist_report.md` 1-376 | through the router | reviewed | proof not read |
| G-035 | 18989-19409 | `PL\work\root\normalized_below_report.md` 1-420 | through the router | reviewed | proof not read |
| T-059 | 19410-19835 | `PL\work\theta\outer5\variable_wall\generic_high_twist_report.md` 1-433 | through the router | reviewed | proof not read |
| G-036 | 19836-20108 | `PL\work\root\complete_outer_five_report.md` 1-284 | `PL\work\root\outer_five_positive.py` with its imports and data | whole proof, two agents; 1,708 balanced tests | 539 of 539 coefficients from the run's evaluator against my characters, the evaluator not read before running; proof not read |
| G-031 | 20109-21036 | `PL\work\root\all_five_row_support_report.md` 1-719 | `FIVE_ROW_SUPPORT_INDEX.json`, `ALL_WALL_SUPPORT_GRAPH.json`, `five_row_support.py` | whole proof; graph closure | **22 Nov, my own code: all 2,408,042 coefficients with n ≤ 22, 29,515 zeros, 0 failures; all 344 catalogue vectors with their seven values, up to n = 37.** Proof of exhaustion not read |
| G-037 | 22255-22626 | `PL\work\root\stable_hook_report.md` 1-426 | `stable_hook_positive.py` | whole proof; 4,872 tests | 790 of 790 from the run's evaluator, read in part; **22 Nov, my own code: support criterion, 15,943 cases, 0 failures**; §1 and the series identity read, the polytope proof not |
| G-038 | 22964-23337 | `PL\work\root\stable_second_row_report.md` 1-435 | `stable_second_row_positive.py` | whole proof; computation | **22 Nov, my own code: formula, 2,511 coefficients, m = 3..9, 0 failures**; proof not read |
| G-039 | 23338-23782 | `PL\work\root\stable_third_row_report.md` 1-525 | `stable_third_row_positive.py` | whole proof; computation | **22 Nov, my own code: formula for m ≥ 4, 2,250 coefficients, 0 failures**; m = 3 and the proof not checked |
| G-040 | 23783-24181 | `PL\work\root\fixed_second_part_report.md` 1-468 | none complete | whole proof, by the author after writing | statement and the citation of the bounds only |
| Stable reductions in Theorem C | in G-037 to G-040 | as there | none | as there | **22 Nov, my own code: 10,164 coefficients against direct plethysm, m = 3, 4, 5, 0 failures** |
| T-062, T-063 | 24182-24527 | `PL\work\theta\unstable_hook\higher_hook_jets_report.md` 1-373 | in that folder | whole proof; computations | statement only |
| T-064 | 24528-24832 | `fixed_order_hook_report.md` there, 1-343 | `check_fixed_order_hook.py` | whole proof; computations | statement only |
| T-065 | 24833-25000 | `hook_endpoint_report.md` there, 1-182 | in that folder | whole proof; computations | statement only |
| PNEW-010 | none | `POS\branches\plethysm\uniform_positive_gate.tex` 1-235 | none | reviewed | statement and opening of the proof |
| PNEW-012 | none | `POS\branches\plethysm\outer_six_scalar_positive.tex` 1-421 | `scripts\outer_six_scalar.py`, `certificates\outer_six_scalar_polytopes.json` | computations | statement only |

Check events of the intakes: `<local>/Documents\field_experts\intake_20261121\intakes\GCT_PLETH\*CHECK_EVENTS.tsv`.
The programs of 22 Nov are `check_seed1.py` and `check_nodes.py`, with `check22.txt` and `check_nodes.txt`, in the
temporary folder
`<local>/AppData\Local\Temp\claude\f2c80a22394db22f\e0d20ada-e036-40ad-83b1-31e9a63b69bc\scratchpad\chk\seeds1`.
Their events, each a computation and none a proof check, are in
`<local>/Documents\field_experts\intake_20261121\intakes\GCT_PLETH\INTAKE_GCT_PLETH_20261122_seed_CHECK_EVENTS.tsv`.

**Before the theorem is called checked**, whoever writes the paper has to prove or re-prove: the exhaustion in G-031,
the three providers of G-036, the freeness in T-037, and G-040.

### To attach

- `PL\GCT_PLETH.tex`, `PL\CHECK_EVENTS.tsv`, and every working proof, program and data file of the table, with the
  import closure of `outer_five_positive.py`;
- the two POS files with their script and certificate;
- my intakes of GCT_PLETH with their events, and this seed;
- LaTeX: `PL\sources\LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm\main.tex`; arXiv e-prints 1408.5708,
  1507.07131, 2610.07929v2, 2511.02312v3, 2403.03443v2, 2506.11837v2, 2211.15252, 1905.07517v3, and Fischer-Ikenmeyer's
  complexity paper (on disk in NEG_NIGHT checkpoint 15, `sources\LIT_Fischer_Ikenmeyer_plethysm_complexity\`).

### Not for GitHub (someone else's)

- `PL\sources\LIT_*\**` (Borger; Bürgisser-Ikenmeyer-Panova; Ikenmeyer-Panova; Landsberg; Mulmuley);
- `PL\sources\ALPOGE_remark.pdf`;
- in `PL\_from_earlier_checkpoints\GCT_PLETH_checkpoint_06_20261121T0331Z_unzipped\work\theta\`:
  - `sarkar\**` and `sarkar_source.tar` (Sarkar's paper and source);
  - `outer4\jacobians.pdf` (a fetched paper, as far as its name shows; author not checked, so treat it as not ours);
- every e-print fetched for the prompt. Pak-Panova-Swanson is CC BY-NC-ND, so no adapted copy either;
- `PL\sources\ARCHIVE_*.tex` are our transcriptions of Grothendieck's text: they belong to the archive repository
  under its rights notice and not to this paper's payload.

### Workbench

The GCT workbench.
