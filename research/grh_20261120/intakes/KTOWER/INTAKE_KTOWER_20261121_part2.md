# Intake of KTOWER (prompt 47), part 2: checkpoint 09, 21-22 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), still going at this checkpoint (progress review 04 at 21:30 UTC with
movement; next review due 22:30 UTC). Part 1 read checkpoint 03.

## 0. What was read

- **Return folder:** `research_returns\KTOWER_checkpoint_09_20261121T2229Z_unzipped` (22:29 UTC; paper 18,041 lines, 207 pages).
- **Read:** `QUESTIONS.tsv` (all rows); `LEDGER.md` lines 242-327 (progress reviews 03 and 04, the cubic entries, the auxiliary bound
  entry); in `KTOWER.tex` the statements of KT-K80-VANISH, KT-SMALL-ORDER-COMPONENT-REDUCTION **with its proof**,
  KT-SELFDUAL-SOURCE-UNIT-EXCLUSION and KT-JACOBI-TWO-UNIT-FIELD.
- **My computation:** the CM eigenvalues of S_{2e+1}(Γ_0(3), χ_{−3}) at p = 7 from Z[ω] (below).
- **Checked in full (1):** KT-SMALL-ORDER-COMPONENT-REDUCTION (the class-number bounds carried). **Computation (1):** the CM branch of
  the certificate. **Statement level:** the rest.

## 1. What moved since checkpoint 03

| Row | cp03 | cp09 | Findings |
|---|---|---|---|
| KT-Q1C-NEXT-32, -34, -36; KT-Q1C-FURTHER-38, -40 | open (running) | **PROVED** | KT-K64-VANISH, KT-K68-VANISH, KT-K72-VANISH, KT-K76-VANISH, **KT-K80-VANISH: K_{4k}(Z) = 0 for every 1 ≤ k ≤ 20** (under the archive convention A and the carried inputs); KT-COMPONENT-EXTENSION-16 … -20 |
| KT-Q1B-ORDINARY, -ADJOINT, -SELFDUAL | new | proved with explicit source hypotheses | unit exclusions of the ordinary rank-two branch, the adjoint branch, and every essentially self-dual stable Type I source (KT-SELFDUAL-SOURCE-UNIT-EXCLUSION: B_{1,ηω^e} ∈ Z_p^× ⇒ R^∨ ≄ R) |
| KT-Q1B-FIELD-TWO | new | proved under an explicit Bernoulli seed | KT-JACOBI-TWO-UNIT-FIELD: for p ≥ 29 and odd b with B_{2b}/2b a p-unit there is an odd negative fundamental discriminant D, \|D\| ≤ 4p − 1, with B_{1,χ_D} and B_{1,χ_Dω^{b−1}} p-units (so two of the three auxiliary units of KT-FIELD-CHARACTER-REDUCTION, uniformly in the weight along b mod p − 1) |
| KT-Q1C | open | open, reduced | **KT-SMALL-ORDER-COMPONENT-REDUCTION:** for p > 3 and even e with ord(ω^e) ∈ {1, 2, 3, 4}, A_p^{[−e]} = 0 and K_{2e}(Z){p} = 0; the remaining components of the all-weight problem have ord(ω^e) ≥ 5 |
| KT-Q7 | open reduced | open reduced | KT-RM-FROB-AVOID, KT-RM-FROB-NONDETERMINATION added |
| KT-Q1B (all-weight), KT-Q5 (Ihara, remaining characters) | open | open | the third auxiliary unit, inside the actual GD; arithmetic Triple-NV |

The cubic work (KT-ORDINARY-CUBIC-SHUFFLE, KT-CUBIC-BOCKSTEIN-NORM-IDENTIFICATION, with a gap found and repaired by the run at 21:05
UTC) is a comparison of the Q3-IRREG cubic obstruction with Sharifi's norm system; no norm class is evaluated, and the run counts none of
it as movement.

## 2. Verdicts

| Id | Verdict |
|---|---|
| **KT-SMALL-ORDER-COMPONENT-REDUCTION** | **confirmed, class-number bounds carried.** With F = L^{ker ω^{−e}} of degree d ∈ {1,2,3,4}: Cl(F){p} = 0 by h(Q(√p)) ≤ ⌊√p/2⌋ (Le), h < 2p/3 for the cyclic cubic field of conductor p (Moser-Payan 1981, p. 705), and h(k) ≤ √p/2, h(F)/h(k) ≤ p/4 with h(k) \| h(F) for the quartic (Moser 1979-80, exposé 3). Then for x ∈ A_p^{[−e]} ⊆ A_p^H (H = ker ω^{−e}), jN(x) = Σ_{σ∈H}σx = \|H\|x and N(x) ∈ Cl(F){p} = 0, so x = 0 since \|H\| is prime to p. Correct. |
| KT-K64 … KT-K80-VANISH | statement level (the run reports complete two-field replays and combined audits; part 1 checked the GL_2 inputs at e = 26, 28, 30). |
| KT-SELFDUAL-SOURCE-UNIT-EXCLUSION, KT-JACOBI-TWO-UNIT-FIELD, KT-Q1B-ORDINARY, -ADJOINT rows | statement level. |
| **CM branch of the certificate (my computation)** | The CM forms in S_{2e+1}(Γ_0(3), χ_{−3}) are theta series of α ↦ α^{2e} on Z[ω]; at the split prime 7 = ππ̄ (π = 3 + ω) their eigenvalue is π^{2e} + π̄^{2e}, independent of the choice of π because u^{2e} = 1 for u ∈ μ_6 when 3 \| e. Computed: e = 6 gives −153502, the CM eigenvalue of part 1. So the CM factor of the unit certificate is exactly **1 + 7^{2e} − (π^{2e} + π̄^{2e}) = N_{Q(ω)/Q}(1 − π^{2e})**; for e = 6 it is 2^6·3^4·7·13²·37·61, all of whose primes divide K17's N_7. |

## 3. What it gives, and how it bears

- **H18.** The range is now k ≤ 20 (K_4 through K_80). The gates of part 1 stand: the compiled `#print axioms` on `OneCharU_s` and
  `corGK`, the coverage theorems, the U(3) halves for e ≥ 26 (I checked only e = 6), and the final.
- **The uniform mechanism (Vandiver).** Two reductions are now proved: components of order 1-4 vanish (KT-SMALL-ORDER), and two of the
  three auxiliary field units exist uniformly in a residue class (KT-JACOBI-TWO-UNIT-FIELD). The open part is precisely: components with
  ord(ω^e) ≥ 5, and the third unit inside the actual GD.
- **Why no fixed-prime certificate can be uniform (from the CM branch).** ℓ divides N(1 − π^{2e}) exactly when π^{2e} ≡ 1 modulo a prime
  λ | ℓ of Z[ω], i.e. when the order of π in (Z[ω]/λ)^× divides 2e. For each such ℓ this happens along an arithmetic progression of e. So
  every fixed auxiliary prime gives nonunit CM factors for infinitely many weights, and a uniform proof must remove them by reflection or
  by the component argument, as the run does for its large stable primes (KT-STABLE-PROPAGATION). This is a proved fact, not a heuristic.

## 4. The direction of this round (1)-(3): every statement of the run that touches it

1. **Alpöge's sign mechanism, and its μ_6 = μ_2 × μ_3.** The run does not treat the sign-only mechanism (steps 3, 5). What it does use is
   the same field: the auxiliary field of the whole certificate is E = Q(ω), the compact group is Γ = Aut(O_E³) = μ_6³ ⋊ S_3 of order
   1296, and the Hecke operator at 7 = (3 + ω)(3 + ω̄) is a sum over the 57 points of P²(F_7), in Γ-orbits of sizes 3, 18, 36 (KT-U3-SECOND).
   The six units of Z[ω] enter the certificate exactly as in Alpöge's footnote: through the ambiguity u^{2e} of π^{2e}.
2. **The order-3 phase.** At level 3 the CM theta series exist only when 3 | e (the cm_dimension of the run's `gl2_uniform.json` is 0 for
   e = 4, 8, 10 and 1 for e = 6, 12): for 3 ∤ e the Größencharakter α ↦ α^{2e} is defined on ideals only after the primary normalization,
   i.e. after a cubic character mod 3, and it lives at level 9. So the cubic phase of direction (2) is exactly what the level-3 certificate
   avoids, and what an extension of the certificate to level 9 (or to the cubic metaplectic data of Kubota and Patterson) would have to
   carry. **The certificate needs no zero of any L-function:** the Hecke L-functions over Q(ω) appear through values of their coefficients
   (N(1 − π^{2e})), not through RH. RH for Hecke L-functions over Q(ω) of cubic characters (the hypothesis of Dunn-Radziwiłł, Annals 200
   (2024)) is M, not A; nothing in KTOWER proves or uses it.
3. **Erdős-Straus classes, A_4 = V_4 ⋊ C_3, Δ on GT-hat = χ_12∘u, the inert C_3 cell:** not touched by KTOWER.
   - The one structural parallel is KT-SMALL-ORDER: the class-group components are cleared for Teichmüller characters of order 2, 3 and 4
     (quadratic, cubic, quartic subfields of Q(ζ_p)), and the first open order is 5. **The next order the C_6 = C_2 × C_3 structure
     names is 6:** clearing it needs p ∤ h(F) for the cyclic sextic subfield F of Q(ζ_p)^+, i.e. a relative class number bound
     h(F)/(h(F_2)h(F_3)) < p, the sextic analogue of Moser's quartic Theorem B.

## 5. The attack this opens

- **Order 6 (and 5):** prove p ∤ h(F) for the real cyclic sextic (and quintic) subfield of Q(ζ_p). Under A, |L(1, χ)| ≤ U(p) = 2e^γ(log log p
  + O(1)) for each of the order-6 characters (LLS, ZETA_TWO IA02), so the relative class number is bounded by p^{(d−d')/2}·(log log p)^{O(1)}
  divided by a relative regulator; the missing input is a lower bound for the relative regulator of order p^{1−ε}, as in Moser's quartic
  argument. This is concrete, it uses A, and it would move KT-Q1C from "order ≥ 5" to "order ≥ 7".
- **The cubic phase:** extend the certificate to level 9 for 3 ∤ e, where the CM factor becomes N(1 − ψ(π)) with ψ the Größencharakter of
  infinity type z^{2e} twisted by a cubic character mod 3; this is the first place where cubic residue symbols enter the K-group
  computation, and it is computable with the same scripts.

## 6. Hexagon readiness (for the register; not edited)
- **H18:** now k ≤ 20. Gates unchanged in kind (`#print axioms`; coverage theorems; U(3) halves for e ≥ 26; final).
- **KT-SMALL-ORDER-COMPONENT-REDUCTION:** complete, short, checked by me; it is a clean consequence of published class-number bounds. Its
  literature status needs a search (it may be classical: the order-1-to-4 eigenspaces of Q(ζ_p) are known to have no p-torsion by these same
  bounds). Not a post on its own.
