# Primer: HODGE_BOUNDED_CYCLES (prompt 70): the Hodge conjecture for abelian varieties as a uniform bound over finite fields

By Claude Opus 5.5 at effort high (agent aaf694615cb43adc1, a copy of abcaba9b6ae84b747, author of the seed), 23 Nov
2026. The sources are the intakes in this folder (checkpoint 02 and final), with their check events.

- **Returns:** `research_returns\HODGE_BOUNDED_CYCLES_checkpoint_02_20261123T0005Z_unzipped\` and
  `…final_20261123T0508Z_unzipped\` (the paper at `workbench\work\UNFILED\v1\paper\`, 27 .tex files, 120 pages).
- **Run:** GPT-6 Astra (ChatGPT Pro mode), 22 Nov 22:34 UTC to 23 Nov 05:08 UTC. It stopped after two reviews without
  movement.
- **Successor:** HODGE_FINISH (70c) split this paper into Papers A and B (`../HODGE_FINISH/PRIMER_HODGE_FINISH_20261123.md`).

## 1. The equivalence (Q01; main.tex 80–310; targeted check at checkpoint 02)

**Statement.** For a special family (S, θ, t):
- S is a connected Shimura variety at neat level, with S → A_{g,N} induced by a morphism of Shimura data;
- t is a flat Hodge class.

The following are equivalent:
- (i) algebraic everywhere;
- (ii) c_t bounded;
- (iii) bounded on one dense set (for example a Hecke orbit);
- (iv) one D such that, for every CM point x, every model, infinitely many good v (in any prescribed infinite set),
  some geometric place, some ℓ and some M, sp(t_x) = (cl Z⁺ − cl Z⁻)/M with deg ≤ D.

Globally, the Hodge conjecture for abelian varieties ⟺ this for every special family. Published inputs only.

**Lemmas:**
- **Parameter spaces (2.1):** SGA 6 XIII 6.11 bounds Hilbert polynomials; FGA 221 Th. 3.2 gives projectivity; the trace
  of SGA 4 XVIII 2.9 and SGA 4½ Cycle give locally constant classes.
- **Closed loci (2.2):** {c_t ≤ C} is closed.
- **Automatic multiplier bound (2.3):** at most one M on each component.
- **Baire (2.4).**
- **Poincaré pairing (3.1):** on A×A with P = m*θ − θ₁ − θ₂ and q_t = |∫(t⊠t)P^{2d}| > 0, we have
  M²q_t ≤ C(2d,d)(deg Z⁺ + deg Z⁻)².
  - Mechanism: (∧^{2d}E)(x,x) = (∧^{2d}G)(x,x) > 0, since ∧^{2d}J fixes a real (p,p) class;
  - |∫_{Z×Z′}P^{2d}| ≤ ∫H^{2d} = C(2d,d)·deg Z·deg Z′, with H ± P nef (from the theorem of the square). A factor 1/2 is
    omitted in one line, harmlessly.
  - It holds in every characteristic.
- **Lifting (4.1):** components not dominating Spec R lie over finitely many places; a flat horizontal component and a
  generization; smooth proper base change (SGA 4 XVI 2.2); descent to a Q̄-point.
- **Spreading (4.2).**
- **Special families (5.1):** an isogeny to a principal polarization; the Mumford–Tate datum of Hodge type; CM density by
  real approximation (Milne, *Shimura varieties*, 5.4).

**Precedents, credited:**
- Brünjes–Serpé, arXiv 0901.4853, Def. 2.3(ii), Th. 3.4;
- Cattani–Deligne–Kaplan, p. 483 (the Baire/Chow mechanism);
- Bhattacharjee–Bhattacharya, Hexagon 2610.00315v2, Lemmas 4.2–4.3, Th. 4.5.

**Quantifiers:** ∀family ∃D ∀CM x ∃∞v. If the unrefereed CM Hodge proofs (OpenAI 032; van Hoften–Sempliner) are accepted,
the content is exactly the uniformity in x.

## 2. The dichotomy (Q05; main.tex 319–325; checked)

For one variety over a number field and one class, b_v = b₀ outside finitely many v if b₀ < ∞; otherwise
{v : b_v ≤ D} is finite for every D.

## 3. The Weil engine (weil.tex, small.tex; checked)

- **Extraction (Q02, weil.tex 13–126).** δ_W ≤ c_t ≤ ⌈2·16^n/n!⌉ δ⌈√T⌉ Nm(a)^{n(2n+1)} δ_W², for every polarization
  type.
  - P(S) = ∏(S − β_j), S = a^* + ā^*, β_j = q^j(a^{2n−2j} + ā^{2n−2j}): mass ≤ 4^n q^{n²}D.
  - u = P(S)[Y], v = a^*u; m = [W_Z : Zu + Zv] with mc = det(u,v); mδt = ru + sv with r = δdet(t,v)/c and
    s = δdet(u,t)/c.
  - Rederived by me.
- **Small detectors (Q03):** 48, 192, 36, as in the HODGE_DIVISION primer. 36 rests on Schoen 2007, Th. 1.1, whose full
  text the run did not obtain.
- **Stabilization (Q04, weil.tex 192–262).**
  - Qualitative, for every K: λ = rϑ₁ + sϑ₂ makes the product split; three very ample classes Nλ, Nλ + η_i.
  - Explicit, for class number one: [Γ_u] + [Γ_{−u}] = 2(ϑ₁ + Nm(u)ϑ₂) ≤ 2κλ, and (n+1)∫_Y θ^nλ ≤ D, giving
    δ_W ≤ max(1, Nm τ/Δ)/(n+1)·D_{n+1}(Δ²).
- **Principal quotient (Q10, polarization-quotients.tex 1–130; checked in the final).**
  - Every split Weil 2n-fold with O_f-action is isogenous to a principally polarized split one with lattice H(Q),
    q*Θ = t_K f L, deg q = (t_K f)^{2n}Δ.
  - Mechanism: saturation of a maximal isotropic subspace, splitting, the shear by η with η + η̄ = t_K, and Steinitz.
  - δ_W ≤ (t_K f m_K)^n Δ C_U, with m_K ≤ (2/π)√|disc K|.
- **Strong semiregularity (Q12, pure-weil-complexes.tex 1–110; checked in the final).**
  - For e^B ch E = w ∈ W \ 0: injective on invariant Ext² ⟺ dim Ext²(E,E)^G = 2n(2n−1).
  - Mechanism: HKR; σ² is Serre-adjoint to ev^{g−2}; η = a·vol_{H₁} + b·vol_{H₂} has annihilator H₁⊗H₂ on ∧²H.
- **Higher bounds with declared inputs (Q09, Q28):**
  - all-field split sixfolds δ_W < 10^179 d^53 f³ Δ (Perry);
  - Eisenstein eightfolds B₀f⁴Δ (Severn).

## 4. Constructions and obstructions (statement level for me)

- Q11: 35 invariant quadratic relations of the Gaussian minus projection; minimum rank 24, against the needed rank 10.
- Q13: two-level gluing gives Ext² = 448, against 56.
- Q16, Q17: tree and generic networks are refuted.
- Q18: a positive Gaussian trace network (6,272 equations); Q19 open.
- Q20: coherent sheaves on very general Weil tori are excluded.
- Q21: global resolution is refuted.
- Q29: a coniveau-one criterion for Mumford fourfold powers.
- Q30: the BHPS fibre-product supplier is refuted.

## 5. Open rows (final)

| Row | Gate |
|---|---|
| Q06 | split eightfolds outside Q(√−3): a principal U⁴ seed with invariant Ext² = 56 |
| Q07 | uniform split detectors in every dimension |
| Q08 | the exceptional Mumford family |
| Q19 | off-vertex products |
| Q22 | the analytic perfect bridge |
| Q25 | uniform CM degrees |
| Q26 | a fixed complete-intersection multiple |
| Q27 | effective Galois orbits |
| Q23, Q24, Q32 | unchecked at the final; settled in HODGE_FINISH |

## 6. Where it went

- HODGE_FINISH (70c) with my 70b fixes, giving Papers A and B.
- Hexagon register: H12, H19, H25.
- The fleet map `pequalnp_work\fleet_map\maps\hodge_theory.md`, row HT-07.
