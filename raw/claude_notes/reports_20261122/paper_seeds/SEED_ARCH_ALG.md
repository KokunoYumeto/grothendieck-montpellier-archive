# Paper seeds: ARCH_ALG final, with the checked cote 133 findings

Seed by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), 22 Nov 2026, for the main session (Claude Opus 5.5
at effort max). The results are by GPT-6 Astra (ChatGPT Pro mode), effort not exposed: ARCH_ALG (final, INCOMPLETE,
22 Nov), ALPOGE_BRIDGES (checkpoint 09, the final return) and, for cote 133, GCT_PLETH (checkpoint 09).

Path prefixes, all under `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\`:
- `AR` = `ARCH_ALG_final_20261122T0622Z_unzipped`
- `AB` = `ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z_unzipped`; "AB l. a-b" is a range of `AB\ALPOGE_BRIDGES.tex`
- `PL` = `GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped`; "PL l. a-b" is a range of `PL\GCT_PLETH.tex`

"Run" is GPT-6 Astra (ChatGPT Pro mode), effort not exposed. "Intake" is Claude Opus 5.5 at effort high, agent
a0805369bae2ebddc.

**Five papers, one for each cote: 136 (lead), 134-8, 15, 123, 133.** They share no proof. Cote 133 is not in ARCH_ALG;
its checked findings make Paper 5 and go into none of the other four. The strongest is Paper 1. Paper 4 and Paper 5
are short notes with mostly classical proofs.

---

## Paper 1 (cote 136). The lead

### Title

**Grothendieck's conjectures on divided-power de Rham theories: false strictly, true up to homotopy over semilocal
rings**

### The setting, for a reader without our files

Let k be a commutative ring and S = Γ_k(T) the divided-power algebra. An admissible theory is a simplicial object C
of nonnegatively bigraded (weight w, form degree q), strictly commutative differential algebras with divided powers
over S, such that:
- for each d there is a W, independent of the simplex, with H⁰(C_n^{w,*}) = S^w and H^p(C_n^{w,*}) = 0 for
  1 ≤ p ≤ d, for all w ≥ W and all n;
- for each q the simplicial module C_*^{w,q} has acyclic normalization, degree zero included, for all large w.

𝒜_k is the category of these. Its model is B_n = Γ_k(x₀,…,x_n) ⊗ Λ_k(e₀,…,e_n)/(Σe_j), with dx_j = e_j. This
precise category is our reading of the two admissibility conditions on the sheets. The paper must say so.

Two parallel maps are *homotopic* (≃) if they are joined by a finite chain of maps into the cotensors
n ↦ C(Δ[n]×Δ[1]), preserving all operations and the coefficients.

### The main theorem, at its exact strength

**Theorem.**
1. *(The strict equalizer conjecture is false.)* For every nonzero commutative ring k, ℤ included, there are admissible
   theories and two maps j₀, j₁ : B ⇉ B ⋉ M that no admissible C″ → B equalizes. The second is given by the universal
   relative divided-power derivation.
2. *(What replaces it.)* For every commutative ring k, inverting all maps of 𝒜_k is computed by right fractions modulo
   ≃. Two parallel maps f, g become equal there iff fh ≃ gh for some admissible h : E → C. "Every parallel pair is
   equalized up to ≃ after precomposition" holds iff each component of the resulting groupoid is simply connected.
   Together with the existence of common sources this is the same as the groupoid being a point.
3. *(Both conjectures hold over semilocal rings.)* Suppose all but finitely many rational primes are invertible in k
   (every ℚ-algebra, every ℤ_(p)-algebra, every algebra over a semilocalization of ℤ; no flatness, noetherian or
   reducedness hypothesis). Then:
   - every finite family of admissible theories has a common admissible source, by strict maps;
   - every parallel pair is equalized up to ≃ after a precomposition;
   - the groupoid obtained by inverting all maps is equivalent to a point.
4. *(The bound.)* Over a ℤ_(P)-algebra, P = {p₁,…,p_s} finite and nonempty, with N a bound for zero-form acyclicity of
   the given family and N_i = p_i^{a_i} ≥ N, the arithmetic comparison object is horizontally acyclic in form degree q
   for w ≥ (q+1)·max N_i and has coefficient cohomology through degree d for w ≥ N(d+2). The resulting common source
   has no bound that contains a sum over the primes.

**What it does not say.**
- Over ℤ neither the existence of common sources, nor terminality, nor equalization up to homotopy is proved or
  refuted.
- The homotopy reading of the word « égalise » is our specified reading, justified from the sheet. The quotation marks
  don't determine it.
- Nothing identifies 𝒜_k with crystals on a scheme, and no crystalline comparison theorem follows.

**Unpublished inputs:** ALPOGE_BRIDGES AQ-136-COMPARISON, DP-MODEL, STRICT, RATIONAL, PLOCAL, COTENSOR,
PLOCAL-LOCALIZATION, SEMILOCAL, COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES, with the lemmas they cite. All are
proved in AB and must be proved in the paper. No use of GRH, Alpöge or Masullo.

### Why it matters

In 1976 Cartan made de Rham cochains over ℤ work by weights and divided powers. In these notes Grothendieck asks
whether all theories of that kind are the same: any two with a common refinement, any two comparisons equal. The
answer found here is no for strict equality over every ring, and yes after homotopy whenever only finitely many primes
are non-units. It also isolates what is special about ℤ: one bound that has to work for all primes at once.

### The works it continues, corrects or refutes

| Work | Place | Relation | Status |
|---|---|---|---|
| A. Grothendieck, manuscript, Montpellier archive cote 136 | physical pp. 111, 117, 119, 121 (footers 110, 116, 118, 120) | refutes the strict form of conjecture (b); proves (a) and the homotopy form of (b) over semilocal rings | our transcriptions, read through the run's statements; scans not opened by me |
| H. Cartan, *Théories cohomologiques*, Invent. Math. 35 (1976) | axioms of a cohomology theory | continues | from memory; AB (AQ-136-CARTAN-SCOPE) inspected it; pages to be verified |
| E. Y. Miller, *De Rham cohomology with arbitrary coefficients*, Topology 17 (1978) | divided-power model | the model B is of this type | from memory |
| B. Cenkl, R. Porter, tame de Rham theory and integer cochains (1980s; Cenkl 1989) | filtered forms with arbitrary coefficients | nearest prior work; the run reports that Cenkl 1989 does not decide the ℤ question | from memory and the run's audit |
| Berthelot, *Cohomologie cristalline*; Stacks Project Tags 04VB, 01A4, 019M, 019G | crystalline Poincaré lemma; right fractions; Dold-Kan | tools and language | from memory and the run's locators |
| Caradot-Lin, arXiv:2511.22614v4 | Proposition 3.10, pp. 19-20 | the run cautions against an unrestricted lifting reading; not part of the theorem | from the run; not opened |

### The other results, in the order of the argument

1. The comparison theorem H^j(C^{w,*}(X)) ≅ H^j(X;k) ⊗ S^w for large w, uniformly in X (COMPARISON).
2. The model B, and the strict counterexample.
3. Path objects, pullbacks, right fractions (ARCH-136-PATHS, FRACTIONS), common sources ⇔ connectedness.
4. ℚ, one prime, finitely many primes by the fracture sequence; the sharpened bound (ARITH-BOUND).
5. Toward ℤ, as a short last section:
   - a partial free source with every condition except vertical exactness in degree two (DEGREE-TWO-FREE);
   - the obstruction as differences of coefficient residues (DEGREE-TWO-RESIDUE);
   - no repair retains an arbitrary prescribed partial source with its two maps (LOW-TATE-RETAINED-COMPLETION,
     FREE-PARTIAL-NONCOMPLETION). The targets there are equal, so this refutes a route and not the conjecture;
   - positive: the associative analogue is terminal over ℤ (ASSOCIATIVE-TERMINAL).

### The research question of the prompt

> **Decide over ℤ whether any two admissible theories have a common admissible source (connectedness of 𝒜_ℤ), and
> then whether its all-arrow groupoid is a point.**

**Current gate.** A source whose horizontal and vertical cutoffs work for all primes at once. The gluing keeps
max N_i, and N_i ≥ p for p > N, so the prescribed local models cannot be glued. In the free constructions the gate is
the degree-two (or three, or four) repair: simultaneous lifting of a class of H²[N] with its coefficient residues.
The run ended with that gate open after two reviews without movement.

**Routes not yet tried:**
- an invariant that all maps of 𝒜_ℤ preserve and that can differ between two theories: weight-tail π₀ of the space of
  maps from B, or Steenrod-type operations with the weight multiplication, outside the degree-one products already
  shown rigid;
- a model not defined by local sources: the PD envelope of the integer-valued-polynomial (binomial) forms, or the
  weight-filtered crystalline complex of the simplices;
- a transfinite small-object argument in a model structure on the partial theories, changing old maps and not
  retaining them, which is exactly what the noncompletion theorems leave open;
- descent along ℤ → ∏ℤ_(p) with a bound on q·p^{a_p}/w in place of a uniform w.

### Proofs, programs and checks

No program is needed for the theorem.

| Result | Proof | Checked by the run | Checked by the intake |
|---|---|---|---|
| COMPARISON | AB l. 3035-3112 | whole proof | **22 Nov: targeted proof check, read in full** |
| DP-MODEL | AB l. 3146-3222 | whole proof | 21 Nov: targeted proof check, confirmed |
| STRICT | AB l. 3223-3338 | whole proof | 21 Nov: targeted proof check, confirmed |
| RATIONAL | AB l. 3339-3474 | whole proof | statement level. Not needed: SEMILOCAL covers every ℚ-algebra |
| PLOCAL | AB l. 3549-3676 | whole proof | **22 Nov: targeted proof check, read in full** |
| COTENSOR | AB l. 3705-3760 | whole proof | not read; what is used follows from ARCH-136-PATHS, which was checked |
| PLOCAL-LOCALIZATION | AB l. 3761-3866 | whole proof | not read; SEMILOCAL step 4 repeats the argument it uses |
| SEMILOCAL | AB l. 4417-4832 | whole proof, three readers | **22 Nov: targeted proof check, all five steps read** |
| COSPAN, CONNECTED-SOURCES, SEMILOCAL-SOURCES | AB l. 5601-5800 | three readers | **22 Nov: targeted proof check, read in full** |
| ARCH-136-HOM-DEFINITION, PATHS, FRACTIONS, HOM-SEMILOCAL | `AR\research\cote136\homotopy.tex` 1-209 | two whole-proof readers | **22 Nov: targeted proof check, read in full** |
| ARCH-136-ARITH-BOUND | `AR\research\cote136\arithmetic_improvement.tex` 1-185 | two whole-proof readers | **22 Nov: targeted proof check, read in full**, given PLOCAL and SEMILOCAL's sequence |
| DEGREE-TWO-FREE; RESIDUE; noncompletion | in `AR\research\cote136\`: `prime_degree_agent\degree_two_free_variant.tex`, `degree_two_residue.tex`, `prime_degree_agent\free_partial_noncompletion.tex`; `AR\research\cote15\136\low_tate_compatibility_obstruction.tex` (each whole) | whole-proof checks | statements in IMPLICATIONS only |
| ASSOCIATIVE-TERMINAL | `AR\research\cote136\counterexample_agent\associative_terminality.tex` (whole) | whole proof | statement in IMPLICATIONS only |

Intake: `<local>/Documents\field_experts\intake_20261121\intakes\ARCH_ALG\INTAKE_ARCH_ALG_20261122_final.md`, with its check events. It found no gap in the chain of the main theorem.

### To attach

`AB\ALPOGE_BRIDGES.tex`; `AR\ARCH_ALG.tex` with `AR\research\cote136\**` and `AR\research\cote15\136\**` (the second
folder holds cote 136 modules despite its name); both runs' check events; my intakes of both; our transcriptions
`ARCHIVE_136_scan111, 113, 115, 117, 119, 121`; arXiv:2511.22614v4.

### Not for GitHub

Cartan's, Miller's, Cenkl-Porter's and Caradot-Lin's papers, and any scan or copy of them in an input ZIP. The scans
of cote 136. Our transcriptions of them belong to the archive repository under its rights notice, not to the paper's
payload. No literature file is inside AR.

### Workbench

A topical workbench on divided-power de Rham theories, pointed to from grothendieck-montpellier-archive (no such
workbench exists yet, to my knowledge).

---

## Paper 2 (cote 134-8)

### Title

**A derived left adjoint that does not preserve coproducts, and Grothendieck's localization test for linear
homotopy types**

### The main theorem, at its exact strength

Grothendieck's hypotheses, in our fixed reading: a k-linear abelian category ℳ with enough projectives; an exact
scalar embedding κ with adjoints φ ⊣ κ ⊣ ψ and Lφ∘κ = id; a symmetric monoidal bilinear tensor; an interval 1 → J
that stays monic after tensoring, with Lφ(J ⊗ C) = 0 for every C. He asks whether inverting the maps inverted by
Lφ gives the connective derived category of k.

**Theorem.** For every field k there is a complete and cocomplete such ℳ, with a tensor preserving all colimits in
each variable and with flat interval and quotient, in which:
1. the comparison ⊕_s L₂φ(X_s) → L₂φ(⊕_s X_s) fails to be surjective for a countable family: its source is 0 and its
   target is E(k^(ℕ)) ≠ 0, E(V) = V**/V;
2. the class W of maps inverted by Lφ is not closed under countable coproducts;
3. nevertheless ℳ[W⁻¹] ≅ D_{≥0}(k).

So compatibility with coproducts is not a consequence of the hypotheses and not necessary for the conclusion. **It is
no counterexample to Grothendieck's Thm(?)**, which stays open in that generality.

**Unpublished inputs:** F-SM-34 (the category 𝒩 and L_{2r}φ_𝒩(κV) = E^r(V)).

### Why it matters

It is the natural proof of such a localization theorem that fails: one wants to resolve by sums and apply Lφ termwise.
The example keeps every stated axiom and breaks exactly that step, so a general proof needs another idea.

### Works

| Work | Place | Relation | Status |
|---|---|---|---|
| A. Grothendieck, *Les Dérivateurs* manuscripts, cote 134-8 | physical pp. 48-49 (footers 47-48), the « Thm(?) » | answers the auxiliary question, leaves the theorem | our transcriptions, through the run; scans not opened by me |
| Stacks Project, localization and Dold-Kan | tags cited in AR | tools | from the run |
| Nakamura-Yoshino (2018) | Theorem 9.2, Remark 9.3 | input of the raw-counit theorem | from the run; not opened |
| Neeman, Roos on AB4 and products in derived categories | none | neighbouring phenomena; search before any novelty claim | from memory |

### The other results, in order

1. Positive: the Thm(?) when coproducts are compatible, so in particular under AB4 with enough projectives (F-SM-32),
   and in countable form (F-SM-33).
2. Comparison monic in all degrees and bijective in degrees 0 and 1 (F-SM-44).
3. The square-zero unitization (ARCH-134-01), the example (02), its localization (03).
4. The raw counit over noetherian rings of finite Krull dimension under a scalar-compatible interval (ARCH-134-04).
5. Two further models (ARCH-134-05, 06); in the second the conclusion again holds.

### The research question

> **Prove ℳ[W⁻¹] ≅ D_{≥0}(k) from the stated axioms alone, or construct a counterexample in which the localization
> itself differs.**

**Gate:** every proof in hand uses coproduct compatibility or the all-scalar counit (test SM25.2).
**Not yet tried:** a proof by the interval alone (simplicial resolutions by J^{⊗n}, finite sums only); localization by
a calculus of fractions in the homotopy category of cofibrant objects without small-object arguments; a counterexample
with a non-reflective W, from an adjunction whose derived unit needs uncountable sums.

### Proofs and checks

| Result | Proof | Run | Intake |
|---|---|---|---|
| ARCH-134-01, 02, 03 | `AR\research\cote1348\arch134_checked.tex` 1-390 | two whole-proof readers | **22 Nov: targeted proof check, read in full; confirmed given F-SM-34** |
| ARCH-134-04 | `AR\research\cote1348\arch134_raw.tex` 1-135 | whole proof | statement only |
| ARCH-134-05, 06 | `arch134_ultrapower.tex` 1-179, `arch134_even_shift.tex` 1-301, same folder | whole proof | statement only |
| F-SM-44, 32, 33, 34 | AB l. 26029-26297, 26298-26722, 26723-26884, 26885-27226 | several readers | statement level |

### To attach; not for GitHub; workbench

Attach those files, both runs' events, my intakes, the transcriptions of cote 134-8 scans 046-056. Not for GitHub:
Nakamura-Yoshino's paper and the scans. Workbench: the Dérivateurs topical workbench, beside
grothendieck-derivateurs.

---

## Paper 3 (cote 15)

### Title

**An abelian threefold over F₅₁₂ whose isogeny class does not descend as far as its class number predicts**

### The main theorem, at its exact strength

Let K = ℚ(√−23), s² = −23, γ = 12 − 4s, a Weil 2⁹-number with γ + γ̄ = 24.
1. The abelian variety A/F₅₁₂ of γ is a geometrically simple threefold with Frobenius polynomial (t² − 24t + 512)³.
   Its geometric endomorphism algebra is the division algebra of degree 3 over K with local invariants 1/3 and 2/3 at
   the two primes over 2. Here h_K = 3.
2. No abelian variety over F₈ = F_{2^{h_K}} is geometrically isogenous to A.
3. Hence Proposition 2.9 of D. Thakur, arXiv:2001.00210v1, p. 6, which asks for a model up to isogeny over
   F_{p^{h_K}}, is false as stated there. Its proof gives the generator of 𝔭^{h_K} the division algebra of A, while
   that generator has index 1 and dimension 1.

Nothing is said about later versions or other statements of that preprint. Inputs: Honda-Tate theory and Tate's
isogeny theorem, both published. No GRH and no CM preprint.

### Why it matters

It is a small, exact obstruction in the arithmetic of Grothendieck's motives over finite fields: the class of a
Frobenius as a Weil number and the field of definition of its motive are governed by different data, the ideal class
and the Brauer invariants.

### Works

| Work | Place | Relation | Status |
|---|---|---|---|
| D. Thakur, arXiv:2001.00210v1 | Definition 2.3, Proposition 2.9, p. 6 | refutes the proposition | from the run, which inspected v1; not opened by me. **Check the newest version before writing** |
| J. Tate, Séminaire Bourbaki 352 | Theorem 1(ii), p. 96 | invariants and dimension | from memory and the run |
| A. Grothendieck, manuscript, cote 15 | physical pp. 94-106 | the question of motives over F_p | our transcriptions, through the run |
| Shioda-Katsura; Huybrechts, *Lectures on K3 surfaces*, Ch. 1 Ex. 1.3(iii); Honda; Milne 2001, App. A.7 | as cited in AR | the companion constructions | from memory and the run |

### The other results, in order

1. The example and the descent failure.
2. Kummer surfaces in characteristic ≠ 2: h(K) is a Chow summand of h(A) ⊕ h(A[2]) ⊗ L, by an explicit degree-two
   map.
3. Split cubic fourfolds f(x) + g(y) = 0 in characteristic ≠ 3: an explicit degree-three map from a blown-up product
   of cubic surfaces, hence forward cycles into an abelian-Artin-Tate target.
4. For an arbitrary cubic fourfold and finite-height K3: under the fixed target's abelian hypothesis, forward cycles
   exist iff a stated finite family of mixed Tate classes is algebraic. This is a reduction and proves no Tate case.
5. Ordinary K3 surfaces and cubic fourfolds: a target from published inputs only (ORDINARY-TARGET).

Items 2-5 are a second section. Their geometry is classical (Kummer; Shioda-Katsura) and is cited as such.

### The research question

> **Determine, for every simple abelian variety over a finite field, the least field to which its geometric isogeny
> class descends, and the sharp bound in terms of h_K and the Brauer index that replaces Proposition 2.9.**

**Gate:** the minimum of the stabilized exponent and the index over all labels α with α^N in the given germ.
**Not yet tried:** a formula by Shimura-Taniyama types and the class of 𝔭 in the quotient by norms; a search over CM
fields of degree 2 and 4 for the extremal ratio; the functorial form through the Weil-number torus.

### Proofs and checks

| Result | Proof | Run | Intake |
|---|---|---|---|
| ARCH-15-HONDA-CHECK | `AR\research\cote15\cote15_honda_check.tex` 1-247 | whole proof, two readers; `cote15_honda_computation.txt` | **22 Nov: lines 1-150 and 203-214 read; targeted proof check of invariants, dimension and nondescent** |
| CC-AG14; BR-15-CLASSBOUND | AB l. 10651-11258; 12734-12820 | whole proof | class-number half confirmed 21 Nov |
| cycles | `AR\research\cote15\cote15_core.tex` 1-480, `cote15_ordinary_target.tex` 1-189 | whole proofs | statements read (59-78, 153-192, 345-372); the rest by IMPLICATIONS |

### To attach; not for GitHub; workbench

Attach those files, the events, arXiv:2001.00210 (v1 and newest), transcriptions of cote 15 scans 092-107. Not for
GitHub: Thakur's and Tate's papers, Huybrechts' book draft, the scans. Workbench: motives over finite fields.

---

## Paper 4 (cote 123)

### Title

**Answers to Grothendieck's 1969 letter to Kostant on tori in apposition**

### The main theorem, at its exact strength

For every simple complex adjoint group, with h the Coxeter number, z the order of the center of the simply connected
cover and W the Weyl group:
1. An apposition pair of maximal tori with a Borel through each has |W|²/(h z φ(h)) classes under inner conjugation,
   and the stabilizer of the pair acts freely on the choices of Borels.
2. Some choice of the two Borels is always opposite. Every choice is opposite exactly in types A_r with r+1 prime,
   B₂ = C₂ and G₂.
3. A class fixed by all outer automorphisms exists iff the type is not A_{2m}. It is in general not unique: in type
   A_{n−1}, n = 2^s u even ≥ 4, exactly [2^m m!]²/(n²φ(n)) · c classes have automorphism group C₂, where n = 2m and
   c = (n/2)2^{ω(u)} for s = 1, n·2^{ω(u)} for s ≥ 2. For n = 4 that is 8 of 18.
4. His two guesses on subregular elements fail: in every simple type the subregular orbit is unique and the adjoint
   quotient has tangent rank r−1 there. **This is a known theorem** (Richardson 1987, Lemma 5.1, crediting Slodowy),
   as are the answers on the dimension of Springer fibres (Steinberg) and on rational singularities.

Unpublished inputs: ALPOGE_BRIDGES CC-APG01-11 with its computations in G₂, F₄, E₈.

### Why it matters

The letter asks concrete questions on Kostant's principal elements. Some had known answers and some, as far as a
limited search shows, did not (the opposition table, the A_{2m} exclusion).

### Works

| Work | Place | Relation | Status |
|---|---|---|---|
| A. Grothendieck to B. Kostant, 22 Oct 1969, cote 123 | physical pp. 22-23 | answers the questions | our transcription, through the run |
| B. Kostant 1959; Kostant 2010, *cyclic elements and Coxeter tori* | Theorem 8.6; equation (0.6) | apposition, principal elements | from the run |
| R. W. Richardson 1987 | §5, Lemma 5.1, p. 234 | the rank theorem | from the run |
| Steinberg 1965, 1976; Slodowy, LNM 815 | as cited in AR | known answers | from memory and the run |
| Guest-Ho, arXiv:1802.01126; Elashvili-Kac-Vinberg, arXiv:1205.0515 | as cited in AR | neighbours | from the run |

### The research question

> **Decide whether some rule singles out one class, natural in the group, in every type other than A_{2m}, and count
> the Out-fixed classes in D_r, E₆ and type A uniformly by one formula.**

**Gate:** invariance alone leaves many classes (8 of 18 already for n = 4).
**Not yet tried:** positivity (Lusztig's totally positive part of the pair); minimal length of the relative position;
compatibility with folding and with central isogenies.

### Proofs and checks

| Result | Proof | Run | Intake |
|---|---|---|---|
| CC-APG01 | AB l. 18648-18719 | whole proof | 21 Nov: confirmed |
| CC-APG02, 03 | AB l. 18720-18995 | whole proof | statement |
| CC-APG04 | AB l. 18996-19131 | whole proof | 21 Nov: existence confirmed; converse given the normal form |
| CC-APG06-08; 09-11 | AB l. 19189-19550; 20058-20256 | whole proof | statement |
| BR-12302; CC-RK04-05 | AB l. 17336-17429; 20849-20930 | whole proof | 21 Nov: sp₄ example and RK04 confirmed |
| ARCH-123-NORMAL, COUNT | `AR\research\cote123\companion.tex` 193-363; `normal_form_check.py` | whole proof; n = 2..7 by computation | 22 Nov: statements read; **count confirmed by own computation, n = 3..9** |

### To attach; not for GitHub; workbench

Attach the companion, the AB ranges, Kostant 2010's LaTeX, our transcription of scans 022-024. Not for GitHub:
Kostant's, Richardson's and Steinberg's papers; the letter's scan, whose transcription stays in the archive
repository under its notice. Workbench: the archive repository's companion, until a Lie-theory workbench exists.

---

## Paper 5 (cote 133; from GCT_PLETH)

### Title

**When do symmetric powers generate the representation rings of symmetric groups over a local ring? Notes on
Grothendieck's λ-ring manuscript**

### The main theorem, at its exact strength

Grothendieck asks on cote 133, scans 28-29, whether for a local ring k the classes ρ_i of the trivial
representations of S_i freely generate ⊕_n K₀(k[S_n]-modules finite free over k) as a ring under induction.
1. **Yes for every discrete valuation ring of characteristic zero:** rationalization
   K₀(O[S_n]-lattices) ≅ R_K(S_n) is an isomorphism, and ⊕R_K(S_n) is ℤ[h₁,h₂,…]. This rests on a classical theorem
   (Swan; Curtis-Reiner).
2. **No for local rings in general, even of characteristic zero:** over A = ℤ_(2)[ε]/(2ε,ε²) the character
   g ↦ 1+ε of S₂ has determinant 1+ε, which the subgroup generated by ρ₂ and ρ₁² cannot reach. **No over F₂:**
   ρ₁² = 2ρ₂.
3. **His split Witt-Green ring is not a special λ-ring, even with 2 invertible:** over F̄₃ and G = C₃, ψ³ is not
   multiplicative on it.
4. **The tensor-power identity of scan 28 holds integrally** in exact equivariant K₀, but its monomial terms are
   virtual and not effective: τ²(E) = ψ²(E)ρ₂ + Λ²(E)ρ₁².

Statements 2 and 3 are checked; 1 was read in part; in 4 the noneffectivity is checked and the integral identity is
at statement level. **The wording of the question must be read on the scan before it is quoted.**

### Why it matters

A question Grothendieck left in his own notes gets an answer in both directions, by a determinant that fits on one
line, and it shows exactly which λ-structures survive in modular characteristic.

### Works

| Work | Place | Relation | Status |
|---|---|---|---|
| A. Grothendieck, manuscript, cote 133 | scans 6, 8, 19, 28-29 | answers, corrects | our transcriptions and study; scans not opened by me |
| Curtis-Reiner, *Methods of representation theory* I; Swan | §39 | statement 1 | from memory |
| G. James, LNM 682 | Theorem 11.5 | rank p(p)−1 over F_p | from memory and the run |
| J. Borger, *Λ-rings and the field with one element* | none | language | from memory (LaTeX in PL) |
| Esnault-Kahn-Viehweg, J. reine angew. Math. 441 (1993) | Prop. 5.5 | credit for the hyperbolic Stiefel-Whitney formula | from the run; not opened |

**Two items of our own study, not of Grothendieck, to correct there and not in the paper:** the equivariant
identity marked "Checked" for scan 19 (A-001: in B(C₂), E² ≠ 2λ²E + E), and our paraphrase "direct summands of a
single Hom(I,−)" for scans 24-27 (A-013). Neither may be attributed to him before the scan is read.

### The research question

> **Determine exactly the commutative local rings k for which the ρ_i freely generate ⊕_n K₀ of k[S_n]-lattices.**

**Gate:** necessary are Hom(S_n, k^×) = {±1} and injectivity; the run conjectures that a determinant condition with
rationalization suffices, without proof.
**Not yet tried:** regular local rings of mixed characteristic by dévissage and Swan's theorem; reduced rings by
gluing generic points; an obstruction group from deformations of characters (Hom(S_n, 1+𝔪)) and of higher Specht
lattices.

### Proofs and checks

| Result | Proof | Run | Intake |
|---|---|---|---|
| A-021 | PL l. 42428-42653 | whole proof | read in part |
| A-023 | PL l. 42863-42967 | whole proof | 21 Nov: targeted proof check, confirmed |
| A-020 | PL l. 42400-42427 | whole proof | statement |
| A-003; A-015 | PL l. 40006-40155; 41812-41933 | whole proof | A-003: independent re-proof of the key computation; A-015 statement |
| A-004, A-005 (the hyperbolic quotient; λ-operations don't descend) | PL l. 40156-40292 | whole proof | statement |
| A-007; A-012 | PL l. 40358-40516; 40913-41165 | whole proof | A-007 confirmed; A-012 statement |

### To attach; not for GitHub; workbench

Attach the PL ranges with their events, my GCT_PLETH intakes, our study of cote 133 and the transcriptions of the
scans named. Not for GitHub: `PL\sources\LIT_Borger_*`, the cited books and papers, the scans. Workbench: λ-rings and
symmetric groups, beside the GCT workbench.

---

## Not proposed as papers

- The 60-odd cote 136 repair lemmas beyond Paper 1's last section: they are route records for a run on ℤ and belong
  in the workbench.
- ARCH-136-FREE-COMPLEX-LIFT-CAUTION alone: a caution on a reading of another paper, not a checked erratum.

## Not for GitHub, from the return itself

AR holds 185 files. None is a paper or scan of someone else by name or format (`ARCH_ALG.pdf` and
`cote15_honda_computation.txt` are the run's own). The inputs named in `AR\INPUT_MANIFEST.json` are not to be
republished from it.
