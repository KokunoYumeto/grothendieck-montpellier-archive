# Two follow-ups on HNAM (hexagon:2611.01018v1): the Cureton–Thorner Lean statement, and Zentner/Kuperberg

- **Checker:** Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7.
- **Date:** 25 Nov 2026.
- **Asked by:** main 329fb1e6 (Claude Opus 5.5 at effort max), for the Fable conference.
- **Status rule:** each status below comes from what I opened and checked in this task.
- **Source copies:** in the session scratchpad.
  - `ct_lean/src/`: a GitHub API tarball of AxiomMath/DedekindZetaZeroFree at commit 09afbb4ce6, the head of `main`.
  - `zk_dl/`: arXiv PDFs and text of 2611.06705, 1605.08530v4 and 1112.0845.

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | The Lean statement of CT's main theorem says what Thm 1.1 of hexagon:2610.00200v2 says, with no hidden hypothesis or axiom | **Holds at statement level.** The axioms are as recorded by the repository and backed by my source scan. I did not rebuild it, and I found no public comparator log |
| 2a | Zentner's coNP result (and Kuperberg's) uses GRH only through the Koiran/Lagarias–Odlyzko small-prime step, so HNAM Thm A(2) and a half-plane remove GRH | **Holds.** But it is **already published**: Baldwin–Sivek, arXiv 2611.06705 (4 Nov 2026), Thm 1.3, modulo the quasi-RH that CT claims. We must not claim it |
| 2b | Anything since settled unconditionally? | Unknot recognition (knottedness) has been in coNP unconditionally since Lackenby, Adv. Math. 387 (2021), so Kuperberg's GRH result is superseded. Hyperbolic knot recognition is unconditional by Haraway–Hoffman. 3-sphere recognition in coNP: no unconditional proof other than through a quasi-RH (Baldwin–Sivek, Remark 1.4) |
| 2c | Credit gap in the posted HNAM v1 | **Yes.** It cites neither Frei–Sofos–Widmer, arXiv 2610.18491 (13 Oct 2026; effective Chebotarev from the quasi-RH), nor Baldwin–Sivek. Their Thm 2.1 is the single-polynomial form of HNAM Prop. 3.2 with Thm 4.1. v2 should cite both. Draft in §3 |

## 1. The Cureton–Thorner Lean certificate

**The repository.** CT §15 (`ct200.txt` l. 2334–2346) names https://github.com/AxiomMath/DedekindZetaZeroFree and says that it
"reports successful verification with the Lean comparator".
- The repository was created on 12 Oct 2026; its last push was 13 Oct 10:11 UTC (commit 09afbb4ce6).
- The toolchain is `leanprover/lean4:v4.35.0-rc3`, with Mathlib at 0493595e and TauCeti at c197d7bd as dependencies.
- A vendored class-field-theory library has 1,658 modules. The repository has 5,528 `.lean` files in all.

**The challenge statement** (`Challenge/DedekindZetaChallenge.lean`; it imports only Mathlib):
```lean
theorem main (K : Type) [Field K] [NumberField K] : ∃ f : ℂ → ℂ, DifferentiableOn ℂ f ({1}ᶜ : Set ℂ) ∧
      (∀ s, 1 < s.re → f s = NumberField.dedekindZeta K s) ∧
      ∀ s, 31 / 32 < s.re → s ≠ 1 → f s ≠ 0 := by sorry
```

**Why this is CT's Thm 1.1** ("If K is any number field, then ζ_K(s) ≠ 0 when Re s > 31/32 and s ≠ 1").
- `NumberField.dedekindZeta K` is, at the pinned Mathlib (`Mathlib/NumberTheory/NumberField/DedekindZeta.lean`
  l. 49–50, opened at rev 0493595e), the L-series with coefficients #{I : N(I) = n}. On Re s > 1 that is ζ_K.
- A function holomorphic on the connected open set ℂ∖{1} that agrees with ζ_K on Re s > 1 is, by the identity theorem,
  the meromorphic continuation of ζ_K. So the statement says exactly that the continued ζ_K has no zero for
  Re s > 31/32, s ≠ 1, for every number field K. Every number field is isomorphic to one in `Type`.
- There is no hidden hypothesis. The only assumptions are `[Field K] [NumberField K]`.
- `heckeCorollary` likewise states Cor. 1.2 for ray class characters modulo m ≠ ⊥: narrow ray classes, with
  positivity at the real places.

**The solution.** `Solution/DedekindZetaSolution.lean` restates the same two theorems verbatim and proves them by
`exact DedekindZetaZeroFree.dedekindZeta_ne_zero K` and `exact heckeL_ne_zero K m hm χ`.

**What is recorded.**
- **`comparator.json`:** names the challenge and solution modules and the two theorem names, and lists the permitted
  axioms as `propext`, `Quot.sound`, `Classical.choice`.
- **`formalization.yaml` (status block):** sorry_count 0, sorry_in_definitions 0, axioms [propext, Quot.sound,
  Classical.choice] for both main results. It says "The full default build passes for all library modules, the
  Challenge, and the Solution, admitting only the three standard axioms." The README says the same.
- **CI (GitHub Actions, workflow "Lean verification", `lake build` via leanprover/lean-action):**
  - run 38381604779 on 09afbb4ce6, 13 Oct 10:11 UTC: success;
  - the earlier runs: success, success, and one cancelled.
- **Not public:** the CI job compiles but does not itself print axioms. The comparator or Palomar run is a separate
  `workflow_dispatch` job, and none appears among the repository's Actions runs. So the comparator verification is the
  authors' report; I found no log of it.

**My scan of the source at 09afbb4ce6** (text search, not a build):
- no `sorry` or `admit` outside the two intentional placeholders in `Challenge/`;
- no `axiom` declarations;
- no `native_decide`, `implemented_by`, `@[extern]`, `unsafe def`, `Lean.ofReduceBool` or skip-kernel options.

There is one `opaque` declaration (vendored `.../FinitePadicAuxiliaryField.lean` l. 1021). An `opaque` constant has
no definitional equation and adds no axiom, so it is sound. The Mathlib and TauCeti dependencies were not scanned.

**Not rebuilt.** The project has 5,528 files on a release-candidate toolchain; a build is hours, not cheap.

**Verdict.** The formal statement is faithful to Thm 1.1 and Cor. 1.2, with no hidden hypothesis. The axiom claim is
recorded by the authors in three places and is consistent with my scan. A `#print axioms` / comparator run by us is
the remaining step to make it our own check. The four HNAM items that rest on CT rest on this certificate in exactly
this sense.

The repository formalizes the theorems of v1 (12 Oct). Thm 1.1 of v2, which I opened, has the same statement.

## 2. Zentner and Kuperberg

**Kuperberg, "Knottedness is in NP, modulo GRH"** (arXiv 1112.0845; Adv. Math. 256 (2014)). Thm 1.1: knottedness
of a knot given by a diagram is in NP, assuming GRH. The GRH step is used only in Thm 3.2 ("Lagarias–Odlyzko,
Weinberger"):

> h ∈ ℤ[x] irreducible of degree D, R = ‖h‖; under GRH there is a prime p = poly(D, log R) with a root of h mod p.

He quotes it as Koiran's Cor. 1. The rest of the argument is unconditional:
- Thm 3.1 is Koiran's Thms 4 and 7: a solution through a primitive element, with the denominator absorbed.
- Thm 3.3 is Koiran's Lemma 3.
- Thm 3.4 gives a homomorphism Γ → G(ℤ/p) with noncommutative image, log p = poly(ℓ).
- The certificate is checked without GRH; GRH only guarantees that it is short.

**Zentner, "Integer homology 3-spheres admit irreducible representations in SL(2,ℂ)"** (arXiv 1605.08530v4; Duke
Math. J. 2018), §11.
- Thm 11.2: for an integer homology 3-sphere given by a Heegaard diagram, "Y is not S³" is in NP, provided GRH
  holds.
- The proof uses Kuperberg's Thm 3.4 (quoted as Thm 11.1, "assume that GRH holds") applied to π₁(Y), with the
  nonabelian SL(2,ℂ) representation from his Thm 9.4.
- GRH enters nowhere else.
- So 3-sphere recognition is in coNP under GRH. Homology is certified directly when H₁ ≠ 0.

**What follows.** HNAM Thm A(2) gives, under (P_η), a prime p ≤ x₀ with a solution of the whole system in 𝔽_p^n, for
any satisfiable system. Applied to Kuperberg's system (the representation equations plus Rabinowitsch's
noncommutativity equation), it gives Kuperberg's Thm 3.4 with log p = poly. Therefore, given the CT or Hu half-plane:
- knottedness ∈ NP;
- S³-recognition ∈ coNP (Zentner);
- torus knot recognition ∈ coNP (Baldwin–Sivek 2019);
- hyperbolicity of cusped 3-manifolds ∈ coNP (Haraway–Hoffman 2019 with Zentner).

**But this is already published.** Baldwin and Sivek, "3-manifold decision problems and Riemann hypotheses", arXiv
2611.06705v1 (4 Nov 2026):
- **Thm 1.3:** the problems of their Thm 1.1 (unknot, 3-sphere, torus and hyperbolic knot recognition, hyperbolicity
  of cusped 3-manifolds) are in coNP modulo their Hypothesis 1.2. That hypothesis is a uniform zero-free half-plane
  Re s > 1 − δ for all ζ_K.
- **Thm 2.1:** Kuperberg's Thm 3.2 modulo Hypothesis 1.2. It is proved from Frei–Sofos–Widmer's effective Chebotarev
  under the quasi-RH (arXiv 2610.18491, 13 Oct 2026).
- **Thms 2.2–2.3:** the analogues of Kuperberg's Thm 3.4 and Thm 5.1.
- They cite CT as having "communicated a Lean-formalized proof of Hypothesis 1.2 with δ = 1/32", but they keep the
  results conditional because it is not clear that a human has understood that proof.
- They report that Agol was aware of the same.

**What is superseded.**
- Unknot recognition in coNP is unconditional by Lackenby (Adv. Math. 387 (2021)), and by Agol, unpublished; this is
  Baldwin–Sivek's Table 1 and Remark 1.4.
- Hyperbolic knot recognition in coNP is unconditional by Haraway–Hoffman.
- For 3-sphere recognition and hyperbolicity of cusped manifolds, Baldwin–Sivek know no other strategy.

**Literature searched:** one web search (3-sphere recognition, coNP, unconditional), the arXiv abstracts of
2611.06705 and 2610.18491, and the full text of 2611.06705.

## 3. Draft paragraph for HNAM v2 (§1.5 Context; references to be added)

> *Three-manifold topology.* Kuperberg's proof that knottedness is in NP under GRH \cite{Kup14}, and the coNP results
> built on it, Zentner's for 3-sphere recognition \cite[Theorem~11.2]{Zen18} among them, use GRH only to find a prime
> $p$ of polynomial bit length modulo which an irreducible integer polynomial has a root \cite[Theorem~3.2]{Kup14}.
> Theorem~A(2) gives this for the whole system, under $\Ph\eta$. Baldwin and Sivek made this observation before us:
> from the effective Chebotarev theorem of Frei, Sofos and Widmer under a uniform zero-free half-plane \cite{FSW26},
> they prove Kuperberg's prime estimate \cite[Theorem~2.1]{BS26}. With it, unknot, 3-sphere, torus knot and hyperbolic
> knot recognition, and hyperbolicity of cusped 3-manifolds, are in coNP modulo such a half-plane
> \cite[Theorem~1.3]{BS26}. Unknot recognition was already in coNP unconditionally by Lackenby \cite{Lac21}. Frei,
> Sofos and Widmer's theorem also contains Proposition~\ref{prop:PIT}(b) in substance, which should be read as a
> restatement of theirs. Our Theorem~A adds the step from the count to $\HN\in\AM$ and the explicit threshold.

New bibliography entries:
- BS26: J. A. Baldwin and S. Sivek, *3-manifold decision problems and Riemann hypotheses*, arXiv:2611.06705v1
  (4 Nov 2026), Thms 1.1, 1.3, 2.1–2.3, Table 1, Remark 1.4.
- FSW26: C. Frei, E. Sofos and M. Widmer, *Some applications of the quasi-Riemann hypothesis to class groups and small
  generators of number fields*, arXiv:2610.18491v2 (14 Oct 2026). This must be opened at its effective-Chebotarev
  theorem before it is cited at a locator.
- Kup14: G. Kuperberg, *Knottedness is in NP, modulo GRH*, Adv. Math. 256 (2014), 493–506; arXiv:1112.0845, Thms 1.1,
  3.2, 3.4.
- Zen18: R. Zentner, Duke Math. J. 167 (2018), 1643–1712; arXiv:1605.08530v4, §11, Thm 11.2.
- Lac21: M. Lackenby, Adv. Math. 387 (2021), 107796.

The journal page numbers above come from memory and must be checked before use.

Also for v2:
- Change "New here" so that it no longer suggests that the prime ideal estimate from a half-plane is ours. FSW26 has
  it, and our own 2611.00987 has it too.
- Keep the claim to the AM step, the explicit x₀, the derivation through Hu's Cor. 9.6, and Corollary D.
