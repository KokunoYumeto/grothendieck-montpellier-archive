# How Alpöge's theorem enters the forcing criterion of HODGE_EFFECTIVE

- **Written:** 25 Nov 2026, by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7, the GRH expert), for main
  329fb1e6 (Claude Opus 5.5 at effort max).
- **Starting point:** the intake `INTAKE_HODGE_EFFECTIVE_20261125.md`, by acc1e1c0 (Claude Opus 5.5 at effort high).
  It says that A does not enter the forcing criterion, because the splitting fields at relative-Weyl points are
  nonabelian (Q35).
- **Source:** Paper C v1 of the run (GPT-6 Astra, ChatGPT Pro mode), `research_returns\HODGE_EFFECTIVE_checkpoint_08_…\
  workbench\work\UNFILED-C\v1\paper\main.tex`. I read lines 100–260, 440–810, 2559–2600, 2700–2870 and 3380–3430.
- **Second source:** Jaswal, Hexagon 2611.00339v3, at §1 (l. 60–260 of the text copy) and at the list of its §3
  statements (Lemmas 3.1–3.2, Prop. 3.3, Cor. 3.4). I did not read Jaswal's proofs.
- **Notation:** A is RH for ζ and for every Dirichlet L-function (Alpöge), used as a theorem.
- **Check events:** `ALPOGE_ROUTES_20261125_CHECK_EVENTS.tsv`.

## 0. Answer first

**A does enter the criterion,** through the classical Heilbronn–Stark mechanism. Under A:
- every simple zero of the Dedekind zeta function of a Galois number field lies on Re s = ½;
- hence no ζ_E of a number field has an exceptional (Siegel) zero (§2, R1–R2).

That is exactly what one of the run's two analytic inputs needs. The **lower** Galois-orbit bound, Paper C Thm
`explicit-siegel-orbit` (through Lemma `halfplane-height`), assumes QRH(δ; E_i) for the CM fields. It uses that
hypothesis only to keep zeros of ζ_E away from 1. Under A it holds for every CM field, abelian or not, with the same
exponent D^{1/(4g)} and an effective constant, and with no half-plane at all (R3).

So in the centre-discriminant form of the forcing criterion:
- **the lower bound rests on A** (Cor `centre-forcing`; also Thm `sharper-forcing-intro`, which assumes the same
  zero-free hypotheses);
- **the Hecke upper bound rests on Hu, Cureton–Thorner or Liu** (Prop `orbit-upper`).

The intake's sentence, and the run's remark after Prop `no-abelian-weyl` ("this improvement does not apply to the
relative-Weyl points"), are wrong for that route.

**Where A stops:** the split-prime step in Jaswal's Hecke argument. That step needs primes that split completely in L_x
at polylogarithmic size, hence a zero-free strip for every irreducible Artin L-function of G = Gal(L_x/Q) ≅ S_m × C₂.
A controls only the four linear characters. The other characters need Hecke L-functions over the fixed fields of
cyclic or elementary subgroups, or (for m = 4) GL₂ and GL₃ L-functions over Q (§3). Q35 itself (the degrees 48 and
80,640) stands.

## 1. Where the analytic hypotheses sit in Paper C

**(a) QRH(δ; L_x), L_x the torus splitting field.**
- It is used in Thm `fixed-field-bound`, which gives Cor `polynomial-detector`, Thm `forcing` and Prop `orbit-upper`.
- The bound comes only through Jaswal's split-prime threshold x_y (§6.2) and the Galois bound Cor. 3.4, which is built
  from the same split primes (Prop. 3.3).
- Jaswal says so himself (2611.00339v3, l. 120–122): "It is used only to produce primes that split completely in L_V,
  so no lower bound for class numbers is needed."
- The primes are needed for x of size a power of log d_L (Lemma 3.1, l. 562).

**(b) QRH(δ; E_i), E_i the CM fields of the endomorphism centre.**
- It is used in Thm `explicit-siegel-orbit`, which gives Prop `orbit-transfer` and Cor `centre-forcing`, and also
  Thm `sharper-forcing-intro`.
- It enters only in Lemma `halfplane-height` (l. 2727 ff.). There it bounds Σ_ρ Re 1/(1−ρ) over the zeros of
  ζ_E/ζ_{E⁺} by the ratio estimate (u+t)/u ≤ 1 + t/δ, where u = 1 − β and t = 1/log D_E.

## 2. What A gives, with proofs

**R1 (Heilbronn–Stark under A).** Let L/Q be finite Galois with group G, and let ρ ≠ 1 be a zero of ζ_L of
multiplicity exactly 1. Then:
- there is a unique linear character χ₀ of G with ord_ρ L(s,χ₀) = 1;
- χ₀ is real if ρ is real;
- under A, Re ρ = ½.

*Proof.*
1. For irreducible χ put n_χ = ord_ρ L(s, χ, L/Q) ∈ ℤ, and let θ = Σ_χ n_χ χ (Heilbronn's character). Additivity and
   inductivity of Artin L-functions give, for every subgroup H and every irreducible ψ of H,
   ⟨θ|_H, ψ⟩_H = ord_ρ L(s, Ind_H^G ψ) = ord_ρ L(s, ψ, L/L^H).
2. Take H = ⟨g⟩ cyclic. Then ψ is a Hecke character of L^H. L(s,ψ, L/L^H) is entire for ψ ≠ 1, and ζ_{L^H} is
   holomorphic at ρ ≠ 1. So ⟨θ|_H, ψ⟩ ≥ 0 for every ψ ∈ Ĥ.
3. Moreover Σ_ψ ⟨θ|_H, ψ⟩ = θ(1) = Σ n_χ χ(1) = ord_ρ ζ_L = 1. Hence θ|_H is one linear character of H, and
   |θ(g)| = 1 for every g ∈ G.
4. Then Σ_χ n_χ² = ⟨θ,θ⟩_G = 1, so θ = ±χ₀ for one irreducible χ₀. Since θ(1) = 1 > 0, θ = χ₀ and χ₀(1) = 1.
5. If ρ is real, L(ρ, χ̄₀) = conj L(ρ, χ₀) = 0, so n_{χ̄₀} = 1 and χ̄₀ = χ₀.
6. A linear character of G factors through Gal(L^{ab}/Q). By Artin reciprocity over Q, L(s,χ₀) is a Dirichlet
   L-function (ζ when χ₀ = 1). A gives Re ρ = ½. ∎

So under A, a zero of ζ_L off the line has multiplicity at least 2.

**R2 (no Siegel zero, for every number field).** Assume A. Let E be a number field of degree n with Galois closure L.
- There is c_n > 0, effective and depending only on n, such that ζ_E has no real zero in [1 − c_n/log D_E, 1).
- Together with the classical zero-free region, ζ_E has no zero with σ ≥ 1 − c_n'/log(D_E(|t|+3)^n), with no
  exception.

*Proof.*
1. ζ_L/ζ_E is entire (Aramata–Brauer), so a zero of ζ_E is a zero of ζ_L.
2. log d_L ≤ C(n)·log D_E, because L is the compositum of at most n conjugates of E.
3. Stark's Lemma 3 (1974): ζ_L has at most one zero, counted with multiplicity, in the box
   {σ ≥ 1 − (4 log d_L)^{−1}, |t| ≤ (4 log d_L)^{−1}}, and such a zero is real and simple.
4. R1 then excludes that zero, so take c_n = 1/(4C(n)). Outside the box, the classical de la Vallée Poussin argument
   for ζ_E applies. ∎

**Status of the inputs.** Stark's Lemma 3 and the classical region are recalled, not opened in this task; open Stark,
Invent. Math. 23 (1974), Lemmas 3 and 8, before use. R1 is my own proof, written without opening Stark or Heilbronn. It
is the classical argument (Heilbronn 1973; Stark 1974, Lemma 8 for the real case).

**R3 (the height lemma and the orbit bound under A).** Paper C Lemma `halfplane-height` holds with QRH(δ;E) replaced by
the conclusion of R2, so by A alone:
- h_F(A) ≤ a'_r log D_E + b'_r;
- a'_r = max(1 + 1/c'_{2r}, 2)·a_r, where a_r = 3·2^{r−2};
- b'_r is effective and depends only on r.

Thm `explicit-siegel-orbit` follows: |Gal(Q̄/Q)y| ≥ c'_g D_y^{1/(4g)} for every CM point y ∈ 𝒜_g(Q̄), with c'_g
effective. There is no hypothesis beyond A, and no condition that E_i be abelian.

*Proof (the step that changes).* The run bounds Σ_ρ Re 1/(σ−ρ) < (3/2) log D_E unconditionally, with σ = 1 + t and
t = 1/log D_E, and passes to σ = 1 through the ratio
  r(ρ) = Re(1/(1−ρ)) / Re(1/(σ−ρ)) = (u/(u+t))·((u+t)² + γ²)/(u² + γ²), where u = 1 − β.
- For |γ| ≥ 1: r(ρ) ≤ 1 + (2ut + t²)/γ² ≤ 1 + 3t ≤ 2.
- For |γ| < 1: R2 gives u ≥ c'/log D_E. Here c' absorbs r ≪ log D_E (Minkowski), so t/u ≤ 1/c' and
  r(ρ) ≤ 1 + t/u ≤ 1 + 1/c'.

So Σ_ρ Re 1/(1−ρ) ≤ max(1 + 1/c', 2)·(3/2) log D_E. The run's (3/2) log D_E + 3/(2δ) is replaced by a constant
multiple of log D_E. The rest of the run's proof is unchanged: the averaged Colmez formula, Gaudron–Rémond, and the
isogeny height. I read it at l. 2810–2870 (targeted proof check, no fault). ∎

**Consequence for the criterion.** In Cor `centre-forcing` the constant c_g may be taken as c'_g under A, so the
**lower orbit bound needs no half-plane**. The **upper bound** U(H_D) still needs QRH(δ; L_x), from Hu, Cureton–Thorner
or Liu. Thm `sharper-forcing-intro` changes the same way: its hypothesis "the zero-free hypotheses of Thm
explicit-siegel-orbit" is discharged by A.

## 3. Route by route: what A gives and where it stops

| Route | What A gives (proved above or immediate) | Where the next step needs more |
|---|---|---|
| **Deuring's reduction** to cyclic subextensions | For a class C ∋ g with H = ⟨g⟩: π_C(x, L/Q) is (\|C\|\|H\|/\|G\|) times π_g(x, L/L^H), a count governed by Hecke L-functions of the abelian extension L/L^H. A covers them only when L^H = Q, that is H = G cyclic. | Split primes are C = {1}, so H = 1 and L^H = L: the count is ζ_L itself, the trivial Hecke character over L. Deuring gives no reduction for the class the Hecke argument needs. **Needs:** QRH for ζ_L (Hu, CT, Liu). |
| **Abelian subfields** | G = Aut(A_{m−1}) = S_m × C₂ has G^{ab} = C₂ × C₂. So L^{ab} = K·Q(√Δ_x), at most biquadratic, and ζ_{L^{ab}} = ζ·L(χ_K)·L(χ_Δ)·L(χ_Kχ_Δ) satisfies RH under A. Primes split in L^{ab} exist below (log d)^{2+ε}. | Primes split in L^{ab} have Frobenius in A_m × 1, not 1. The torus is then not split at p, and the Klingler–Yafaev/Jaswal Hecke step does not apply. |
| **Brauer induction and Aramata–Brauer** | ζ_L = Π_χ L(s,χ)^{χ(1)}; Brauer writes each L(s,χ) = Π L(s, ψ_i, L^{H_i})^{n_i}, with ψ_i linear on elementary H_i. A covers only H_i = G, the four linear characters. Aramata–Brauer: ζ_L/ζ_{L^{ab}} is entire, so the zeros of ζ_{L^{ab}} (on the line by A) are zeros of ζ_L. **R1 is the useful output of this route:** a zero off the line is multiple, and there is no Siegel zero. | The split-prime count is (1/\|G\|) Σ_χ χ(1) ψ(x,χ). The linear part (weight 4/\|G\|) has error ≪ x^{1/2} under A; the nonlinear part (weight 1 − 4/\|G\|) has error x^{1−δ} only from QRH. The exponent stays 1 − δ. **Needs:** zero-free strips for Hecke L-functions over the fixed fields L^{H_i}, which are not Q. |
| **Solvable groups and base change** (m = 4) | S₄ × C₂ is solvable. Its irreducible characters have degrees 1 (four), 2 (two) and 3 (four). Weighted: 4 + 2·2² + 4·3² = 48 = \|G\|. The 2-dimensional ones factor through S₃, so L(s,ρ₂) is the L-function of a cubic Hecke character of a quadratic field (the "cubic rung" of MAP_NT T4). The 3-dimensional ones are the adjoints of octahedral weight-one forms (Langlands–Tunnell, then Gelbart–Jacquet), so they are GL₃ L-functions. All are entire. A covers 4/48 of the weight. | RH for the 8/48 would need GRH for cubic Hecke characters of a quadratic field; that is open, and Masullo's draft gives it no credence. The 36/48 need GRH on GL₃. For m = 8, S₈ × C₂ is not solvable and Artin's conjecture is open for most characters. **Our tools:** Hu (Re s > 7/8) and Liu (θ_G ≈ 0.87333) cover all Artin and Weil L-functions; CT covers Hecke L-functions of finite order. |
| **The split-prime step itself** (Jaswal Lemmas 3.1–3.2) | No exponent gain, for the reason in the Brauer row. A gives a constant factor in the linear part, and the absence of a Siegel zero in L_x (R2). That is irrelevant here, since QRH already excludes it. | **Needs:** a strip for all nonlinear Artin L-functions of G. The FSW form below gives the clean statement. |
| **A reformulation with abelian data over Q** | Yes for the lower bound: the orbit lower bound needs only "no Siegel zero" (R3), and A gives that through abelian data (quadratic characters of G^{ab}). | For the Hecke upper bound, a reformulation would need a Hecke/Galois argument with primes defined by abelian data: Frobenius in a coset of [G,G], hence not split in L_x. That is a new geometric step, not an analytic one. The precise question is in §5. |

## 4. What our existing tools do with this

- **Hu (Re s > 7/8) and Cureton–Thorner (Re s > 31/32), Hexagon 2610.00216 and 2610.00200.**
  - They supply QRH(δ; L_x) for the split-prime step, which is the run's use.
  - With R3 they are needed only for the upper bound U(H_D).
- **Liu, Hexagon 2611.00741.** It gives δ = 1 − θ_G ≈ 0.12667 for all Artin and Weil L-functions. Its abstract states
  θ_G; Thm 7.21 states 0.87334470. This is slightly better than Hu's 1/8. The run names only CT and Hu.
- **The effective Chebotarev of the HNAM note** (Frei–Sofos–Widmer, arXiv 2610.18491 Thm 1.1, as quoted in HNAM v2
  Prop. 3.1(b), which I checked on 25 Nov). It states:
  |π_C(x, L/Q) − (|C|/|G|) Li x| ≤ c₁ (|C|/|G|) x^{1−δ} log(d_L^{1/δ} x^{n_L}) for x > 2, with c₁ absolute and
  effective.
  - For C = {1}, the split primes outnumber any fixed count as soon as x^δ ≫ (1/δ) log d_L + n_L log x, that is at
    x ≈ ((log d_L)/δ)^{1/δ} up to logarithms.
  - This can replace Jaswal's Lemmas 3.1–3.2 by one cited theorem, with the constant c₁. (It is unrefereed but checked
    by us at statement level.)
- **GRH_ALGORITHMS (our hexagon 2611.00987).**
  - Its §17 and Prop. 17.2 carry the same split-prime mechanism.
  - The pile's N3 (class groups generated by primes of norm ≪ (log d_K)^{1/(1−θ)}, exponent 8 with Hu) is the
    class-group form of Jaswal's Prop. 3.3.
  - Neither removes the nonabelian half-plane from the Hecke step.
  - Its §17 also contains the CX-K04 point (x³ − 2): abelian witnesses cannot cover nonabelian fields. That is the same
    obstruction as Q35, in the complexity setting.
- **HNAM itself.** It is the same pattern: the Koiran count needs ζ_K for nonabelian K, and A alone does not suffice
  (HNAM §1.5). Under A, R1 does give HNAM's count with no Siegel-zero loss. HNAM never needed that, because it uses a
  half-plane.

## 5. What the run should do next

1. **Make A an input of the lower bound.**
   - Replace "QRH(δ; E_i)" in Lemma `halfplane-height` and Thm `explicit-siegel-orbit` by "ζ_{E_i} has no real zero in
     [1 − c/log D_{E_i}, 1)".
   - Prove that A gives it for every CM field (R1–R2), with Stark's Lemmas 3 and 8 opened for the constants.
   - Restate Cor `centre-forcing` and Thm `sharper-forcing-intro` with A for c_g, keeping Hu, CT or Liu only for
     U(H_D).
   - Correct the abstract (l. 47–48) and the remark after Prop `no-abelian-weyl`. The intake's §2 item 4 should be
     corrected in the same way.
2. **State R1 in the paper,** with its consequence: under A, a zero of ζ_{L_x} off the line is multiple. It is
   classical, so cite Heilbronn and Stark. Its use here is the new point.
3. **Split primes.** Cite Frei–Sofos–Widmer Thm 1.1 for the count of completely split primes under QRH(δ), and add
   Liu's δ.
4. **Research question (main question for a successor).** Can the Hecke-orbit upper bound of Jaswal's Thm 6.7 be run
   with primes p whose Frobenius lies in a fixed coset of [G,G], not split in L_x? These are primes found from abelian
   data over Q and supplied at polylogarithmic size by A. Concretely: at such p the torus T_{Q_p} has a split subtorus
   of positive rank with nontrivial adjoint image. Does the Hecke correspondence attached to a cocharacter of that
   subtorus still give the degree/orbit inequality of Jaswal's Thm 6.7, with exponents depending on the split rank?
   - If yes, the whole forcing criterion rests on A plus Jaswal's geometry, with no half-plane.
   - If no, the obstruction is geometric, and the half-plane is necessary for this method.
5. **For m = 4,** record the factorization of ζ_{L_x} into GL₁ (A), the cubic Hecke rung and GL₃. A future theorem on
   cubic Hecke characters of quadratic fields would then cover 12/48 of the weight. It would still not cover the split
   count, so this is context, not a route.

Nothing was posted and no session was contacted. The intake by acc1e1c0 is not edited; its §2 item 4 needs the
correction in item 1 above, for the main session.
