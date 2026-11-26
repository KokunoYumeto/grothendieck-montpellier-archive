# K-theory of Z, CM points and the theta chain, read towards global Langlands

ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max).
The brief is `BRIEF.md` in this folder.

**Sources.** I built this from the primers in `field_experts/intake_20261121/intakes/`:
- KTOWER, K17, ZETA_NEXT, ZETA_TWO, DEG_L, DP_MULT and NIGHT_AFTER_ALPOGE (mine);
- ALP_MACHINE (abcaba9b's).

I also used the H15 and H06b notes in `reports_20261123/`, and the run texts at the locators given below.

**Status.** Statuses are those recorded in the intakes' check events. In this task I opened no new sources. The two
computations in §3.2 and §4.1 are mine and new here.

**Notation.**
- A: Alpöge's theorem (RH for every Dirichlet L-function). It is the GL_1 layer over Q.
- M: Masullo's draft. It is not a proof, and nothing here rests on it.

---

## 1. The maps, written out

### Map I. Quadratic characters → heights → Galois orbits of CM points (H15; NIGHT_AFTER_ALPOGE A.ORBIT)

**Objects.**
- On one side: the quadratic Hecke character χ_{E/F} of a totally real F, attached to a CM field E. By Stark's
  descent, its possible exceptional real zero comes from a quadratic Dirichlet character χ_d of Q.
- On the other side: the CM points x ∈ A_g(Q̄), with D_x = |disc Z(End A_x)|.

**The chain of maps** (`reports_20261123/h15_note/h15_note.tex`, §§4-6):

1. A on χ_d: no real zero in [1 − 1/(4 log |d|), 1).
2. Stark's Lemma 9: no real zero of L(s, χ_{E/F}) in [1 − 1/(16 r! log D_E), 1).
3. From the Hadamard product and the functional equation, with the zero sum bounded by Lemma 3:
   −L'(0, χ_{E/F})/L(0, χ_{E/F}) = Σ_ρ Re 1/(1−ρ) + ½ log(D_E/D_F) + (r/2)(ψ(½) − log π) < (75/2 + 16 r!) log D_E + …
4. Averaged Colmez:
   2^{−r} Σ_Φ h_W(E, Φ) = −½ L'/L(0, χ_{E/F}) − ¼ log(D_E/D_F).
   This gives h_F(A) ≤ a_r log D_E + b_r.
5. Saturation by the maximal order (an isogeny of degree ≤ [O : R]^{2g}) gives h_F(A) ≤ g(A_g + ½) log D + g B_g.
6. The Galois image lies in the centre, so D divides ∏_ℓ disc Z_ℓ[ρ_ℓ(G_K)].
7. Gaudron-Rémond 2023 (Thms 1.5(2), 1.8, read at the source in the H15 pass):
   D ≤ (C_g k max{1, log k, h_F + 3g/2})^{2g}.
8. Hence |Gal·x| ≥ c_g D_x^{1/(4g)}.

**What is transported.** One real zero of one GL_1 L-function over Q is moved into an arithmetic degree: the Faltings
height, the degree of the Hodge line bundle on the integral model of the CM point. That degree is then moved into a
bound on the size of a Galois orbit.

**Status.** Targeted proof check of every step by me (intake events of 23 Nov). The GR23 inputs were read at the source.

**Rung.** GL_1 over Q, through the quadratic Hecke character of F. Only its zeros near 1 are used, never its
off-centre zeros in general.

### Map II. K_{4k}(Z) → strict Selmer groups → residually reducible three-dimensional representations → U(3) and GL_2 Hecke eigenvalues (H18; K17, KTOWER)

**Objects and steps** (KTOWER.tex 134-282, 813-1052, 2487-4091; K17.tex 2804-2852, 3807-3875, 6277-6436):

1. The comparison of Rost-Voevodsky, Kurihara (Cor. 1.5) and Weibel (VI.8-10) makes K_{4k}(Z){ℓ} dual to the strict
   Selmer group S_ℓ(Q, 2k) of Q_ℓ/Z_ℓ in the relevant Tate twist. This is a Galois-cohomology object attached to the
   Tate motive.
2. Alpöge's archive theorem `OneCharU_s` bounds length S_ℓ by 2 Σ_ρ v_ℓ(tr ρ(s) − t). The sum runs over the
   three-dimensional representations of G_E, E = Q(√−3), that are residually of the shape built from 1 and the
   cyclotomic twists (t = p^{−e} + 1 + p^e is the trace of that reducible shape at s).
3. The admissible ρ are automorphic (coverage, KMSW + Shin + Adler-Lansky):
   - rank three: level-one forms on the compact U(3);
   - rank two (1 ⊕ W): forms on S_{2e+1}(Γ_0(3), χ_{−3}).
4. A nonzero K-group forces an ℓ-adic congruence tr ρ(s) ≡ t. This is an Eisenstein-type congruence between a cusp
   form and the reducible system.
5. The finite certificates show that no such congruence occurs for ℓ ≥ 2^31 and k ≤ 20.

**What is transported.** A torsion class in algebraic K-theory, through Galois cohomology (the Tate motive Z(2k+1) over
Z[1/ℓ]), into a congruence between automorphic eigenvalues on U(3).

**Status.** K_12 is checked in full (three independent recomputations). For k = 13-20, the classical halves and the
gcd steps were recomputed and the deductions read. The U(3) halves are carried.

**Rung.** A GL_1-motivic object (Tate twists over Z) controlled through GL_3, in the form of the unitary group U(3)/Q
(a form of GL_3 over E), and through GL_2.
- The functoriality used is endoscopic: U(1)×U(2) → U(3).
- One explicit instance is in the K_12 certificate. The U(3) Hecke value 157899 at 7 equals 7^6 + 40250, where 40250
  is a T_7-eigenvalue on M_13(Γ_0(3), χ_{−3}). This was recomputed in my cp03 intake; 7^6 + 40250 = 117649 + 40250 =
  157899.
- So the U(3) eigenvalue is the endoscopic transfer: the U(1) part contributes p^e, the U(2) part contributes a_p.

**Next rung.** Uniformity in k: Vandiver at every p, KTOWER Q1B and Q1C. The run reduced it to class-group components
of order 5 or ≥ 7 (KT-SMALL-ORDER, KT-ORDER-SIX, KT-ORDER-FIVE-LENGTH-ONE). §4.1 shows exactly why the size method stops
there.

### Map III. G_Q on the pro-p tower of P¹ − {0,1,∞} ↔ the Tate motives over Z ↔ K-groups (H06b; K17 P2-MOMENT, POLE-GENERAL; Ihara paper = hexagon:2611.00939)

**Objects.**
- The outer action ρ_p: G_Q → Out(π_1(P¹ − {0,1,∞})^{(p)}), restricted to H = Gal(Ω_p/Q(μ_{p^∞})).
- Its rational image: the prounipotent radical U_p, with gr Lie U_p free on s_m (m odd ≥ 3). This is Brown's theorem,
  with Hain-Matsumoto density.

**Correspondences.**
- s_m is the generator dual to the Soulé character κ_m: G → Z_p(m). These characters span the extensions
  Ext¹(Q(0), Q(m)) of mixed Tate motives over Z, the rational K_{2m−1}(Z).
- The integral question, whether each κ_m is surjective, is the same as K_{4k}(Z){p} = 0 (K17 §"four meanings", (B)).
  So Map II is the integral shadow of Map III.
- The kernel question Ω_p* = Ω_p is a faithfulness statement for the whole arithmetic group H, not only its graded
  quotient.
- The proof (Ihara paper, §§4-6):
  - Fukaya-Kato with Wake-Wang-Erickson turn Vandiver (or X^+ finite) into generation of H² by cups of cyclotomic
    p-units.
  - The cup comparison turns this into nonzero companion numerators of the class-two extension.
  - Pole separation turns those into injectivity of the Magnus expansion.

**What is transported.** An Eisenstein-ideal statement (Sharifi's map ϖ: H^-/IH^- → X_χ(1), an isomorphism; modular
curves X_1(p^r)) becomes a statement on fundamental groups. This is a GL_2 → (mixed Tate, GL_1) map: the modular
symbols of GL_2 reach the extension classes of Tate motives.

**Status.** Every step was checked in my second reading. WWE and FK were opened at the cited places.

**Rung.**
- GL_1 over Q: Tate motives and cyclotomic units.
- Through GL_2: Hida-family Eisenstein ideals, by Fukaya-Kato and Wake-Wang-Erickson.

**Next rungs.**
1. The CM-elliptic analogue (Ishii, arXiv:2312.04196). The once-punctured CM elliptic curve over K gives GL_1 over K
   (Hecke characters of the imaginary quadratic field). Ishii's Theorem A assumes an analogue of Deligne-Ihara and p
   prime to h(K(p)).
2. The non-CM analogue: GL_2 over Q.

### Map IV. The theta chain in Alpöge's step 8: theta lifts U(1) → U(n) → … (NIGHT_AFTER_ALPOGE Part B; ALP_MACHINE)

**Objects.**
- A chain of theta lifts between definite unitary groups over a CM field E/F, [F:Q] = f.
- It starts from Hecke characters, that is U(1).
- The size interface `SizesAt` forces the chain length m to satisfy
  x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400} and (log f)² ≤ m/2 − 1 (ALP_MACHINE LIFT54/55, checked by abcaba9b).

**Correspondences.**
- Each step is a Howe duality (U(n), U(n')) inside a symplectic group.
- The norm of a lift is computed by the Rallis inner product formula. DEG_L T6.11 (Haan, U(1) → U(3)) gives an
  L-value at s = 3/2 times local zeta integrals.
- The period that must be nonzero is, by LIFT077, a ratio of central L-values at s = ½ times local factors. This is of
  Ichino-Ikeda / Gan-Gross-Prasad shape.

**What is transported.** The arithmetic content of a GL_1 L-function (the Dirichlet character in step 1) is carried up
the chain into periods of higher-rank unitary forms.
- Positivity of Petersson norms is what Alpöge's sign mechanism exploits (ALP_MACHINE §2, the phase lemmas).
- The cost of each lift (row degrees, partner counts, class factors) is the bookkeeping the theta-chain paper's
  lemmas control:
  - B.ZERO_GRAM_IDENTITY;
  - B.CLASS_NUMBER_TERMINAL;
  - the zero-flag counts.

**Rung.**
- The theta correspondence is functoriality between unitary groups: forms of GL_n over E, a base change of GL_n over F.
- The chain starts at GL_1 over E (Hecke characters restricted to U(1)).
- So the RH proof climbs from GL_1 to large-rank unitary groups and back down to a GL_1 statement.

**Next rung, the question ALP_MACHINE Q3 asks.** Run the same machine for one cubic Kummer Hecke character over Q(ω).
That is GL_1 over an imaginary quadratic field, of finite order but not a Dirichlet character. It is the first case of
extended RH beyond A (Dunn-Radziwiłł's hypothesis for cubic Gauss sums).

---

## 2. Where each map sits, rung by rung

| Map | Input rung | Rung used in the proof | Output | Next rung, as a statement |
|---|---|---|---|---|
| I (CM orbits) | GL_1/Q: one zero of χ_d near 1 | GL_1/F: the quadratic Hecke character χ_{E/F}; averaged Colmez (Artin L-values of CM types, averaged) | heights → orbits on A_g | the individual Colmez formula for non-abelian CM types: L'(0) of the Artin L-function of a single type, GL_n via Artin |
| II (K_{4k}(Z)) | motivic GL_1/Q: Tate twists over Z | GL_3 as U(3)/Q(√−3); GL_2 (level 3 and 7); endoscopy U(1)×U(2) → U(3) | vanishing of K-groups for k ≤ 20 | all k: kill the class-group components of order 5 and ≥ 7 (§4.1) |
| III (Ihara) | mixed Tate motives over Z; GL_1 | GL_2: Eisenstein ideals in Hida families (FK, WWE) | faithfulness of the outer Galois action | the CM-elliptic tower (GL_1 over K); then GL_2 non-CM |
| IV (theta chain) | GL_1 over E (Hecke characters ⊃ Dirichlet) | unitary theta correspondence; Rallis and Siegel-Weil; central values (GGP) | RH for Dirichlet L (Alpöge) | RH for one cubic Hecke character over Q(ω) (ALP_MACHINE Q3) |

---

## 3. Structural notes: one mechanism in two places

### 3.1 Exceptional-zero descent and the Eisenstein congruence: two ways a GL_1 defect is localized

| | Map I | Map II |
|---|---|---|
| defect | one real zero β near 1 of ζ_E/ζ_F | one nonzero class in K_{4k}(Z){ℓ} |
| localization | Stark's Lemmas 8-9: β lives in a quadratic subfield | Herbrand-Ribet style: the class lives in a χ-eigenspace of Cl(Q(μ_ℓ)), dual to a congruence tr ρ ≡ t |
| killed by | A on that quadratic character | unit trace differences tr ρ(s) − t on U(3)/GL_2 eigenforms |
| quantity | 1/(1−β) < 16 r! log D | v_ℓ(N_7) = 0 for ℓ > 271 at k = 3 |

In both, a global defect of one object is pushed onto one character, where it can be tested by a single number.

### 3.2 Class-number size arguments, in both directions

- **H15 (lower bound):** h_E/h_F > c_r D_E^{1/4}/(log D_E)^r (NC01). It uses the analytic class number formula with a
  residue lower bound from A.
- **KTOWER (upper bounds, to show p ∤ h):**
  - order 3: h < 2p/3 (Moser-Payan);
  - order 4: h(F)/h(k) ≤ p/4 (Moser);
  - order 6: J = h_6/(h_2 h_3) < 49p/108 (Gras regulator bound + Louboutin).
- **Theta chain (upper bound as a cost):** h_E ≤ (π²/9)^f D_E (B.CLASS_NUMBER_TERMINAL, checked).

All of these are the same analytic class number formula, h·R = (w√D/2^{r_1}(2π)^{r_2})·∏ L(1, χ), read for a size
bound in different directions. The dictionary is the same throughout: residue or L(1) bound ↔ class-number bound, and
the regulator is the loss.

### 3.3 Separation by evaluation on a grid with an accumulation point

The same injectivity mechanism appears three times:
- **The Ihara proof, at p = 2 (K17-P2-MOMENT) and at odd p (Lemma 5.1).** A group element in the kernel gives a
  bounded measure μ on Z_p^r whose Amice transform vanishes at the grid points u^m − 1 (m odd, in one residue class).
  The points accumulate inside the open disc, so the transform vanishes and μ = 0. At odd p, the poles
  1/((1+T_1)(1+T_2) − α)^k at the roots α of the even characteristic polynomials separate the remaining words.
- **The theta chain.** Primitive detectors separate nonzero original rows: B.PRIMITIVE_CORE_PROJECTORS and
  B.PRIMITIVE_DETECTOR_QUOTIENT, at statement level. There, too, a family of characters (Bessel functionals) is
  evaluated against a finite-dimensional space, and a nonzero determinant, det A ≠ 0, gives injectivity.
- **Iwasawa theory.** A Λ-module element is determined by its values at the cyclotomic characters u^m. This is the
  same identity theorem, Weierstrass preparation.

The dictionary: Magnus word ↔ ordered tensor ↔ Bessel row; weight m ↔ Tate twist ↔ archimedean K-type; pole at α ↔
root of a characteristic polynomial ↔ an eigenvalue that a congruence can hit.

### 3.4 Indices of non-maximal orders controlling degree

| Place | Index | Degree it controls |
|---|---|---|
| A.SATURATION (H15) | I = [O : R] | isogeny degree ≤ I^{2g}; log I ≤ ½ log D |
| A.GALOIS (H15) | [R⊗Z_ℓ : S_ℓ] | disc S_ℓ = disc(R⊗Z_ℓ)·index² |
| DEG_L B19 | J = [Λ : Λ^−] | minimal isogeny degree in [J, K_E^g J/g^g]; Weil witness O(√J) |
| B.ZERO_FLAG_PRIMITIVE_COUNT (theta chain) | det(P) = G = Q_Δ/g^{2f} | the generic count |

In each case the lattice index of a non-maximal order, or the discriminant of a primitive sublattice, is the arithmetic
quantity that converts into a geometric degree or a count.

### 3.5 Positivity carrying an L-value

All four are one mechanism: a norm, which is nonnegative, equals an L-value or its derivative times local factors.
1. **DEG_L T6.1** (Hodge index): the degree of a surface is a positive sum of wedge norms.
2. **DEG_L T6.11 and IV** (the Rallis inner product): the norm of a theta lift is an L-value at the edge.
3. **H15** (averaged Colmez): an arithmetic degree equals −L'/L(0).
4. **ALP_MACHINE LIFT077**: a squared period equals a central L-value.

Alpöge's sign mechanism uses the positivity. Map I uses the derivative.

---

## 4. What it suggests, most promising first

### 4.1 The size method on cyclotomic class components stops exactly at φ(d) ≥ 4 (my computation)

**Setting.** Let F be the cyclic subfield of Q(μ_p) of degree d. The new part of its class number (the χ-parts for the
φ(d) characters of exact order d) satisfies, by the analytic class number formula,

  h_new · R_new = c·p^{φ(d)/2}·∏_{ord χ = d} |L(1, χ)|.

The conductor-discriminant formula contributes p^{½} per new character, and c is bounded in d.

**The test.** p ∤ h_new is guaranteed if h_new < p, that is, if

  R_new > c·p^{φ(d)/2 − 1}·∏ |L(1, χ)|.

**What is available.**
- Upper bounds |L(1, χ)| ≪ log p unconditionally, or ≪ log log p under A (LLS, as in ZETA_TWO IA02).
- Relative regulators bounded below only by powers of log p:
  - Gras for the sextic, R^* ≥ (3/16) log²((p−20)/4);
  - Schoof-Washington for the quintic, R ≥ log⁴(p/2)/25.

**Conclusion.** The method works exactly when φ(d)/2 − 1 ≤ 0, that is, φ(d) ≤ 2, that is, d ∈ {1, 2, 3, 4, 6}. These
are precisely the orders KTOWER cleared.

At d = 5 (φ = 4) it needs R_new ≫ p^{1+δ}. My numerical check (§§3.2-4.1 script): even with an LLS-type bound
U(p) ~ 2e^γ log log p in place of log p, the order-5 bound stays of size p²·(log log p/log p)^4, about 10^9·p at
p = 2^31.

**Next formulation, as a statement to prove.** For the cyclic quintic subfield F of Q(μ_p), give an arithmetic
annihilator of the single possible class of order p (KT-ORDER-FIVE-LENGTH-ONE leaves at most one). Two candidate
sources:
- the Stickelberger element of order 5 evaluated on that eigenspace: B_{1,ω^{−e}} as a p-unit test, which is Herbrand's
  criterion;
- the Euler system of cyclotomic units in F.

A sub-question: show that the norm map from the quintic layer of Q(μ_{p²}) (the capitulation criterion
KT-ORDER-FIVE-GREENBERG-UNIT-GATE) is surjective on units. This is the remaining arithmetic condition the run isolated.

### 4.2 Explicit-exponent Galois orbits beyond A_g (Map I upward)

Map I uses three things:
- the centre-discriminant comparison (Gaudron-Rémond);
- a height bound from averaged Colmez;
- level-3 descent.

The same three exist for any Shimura variety of Hodge type that embeds into A_g, where the CM points are the special
points.

**Statement to prove.** For a Hodge-type Shimura subvariety S ⊂ A_g, every special point x of S satisfies
|Gal·x| ≥ c_{S,g} D_x^{1/(4g)}. Here D_x is the centre discriminant of End(A_x), restricted from A_g. The only new
input is comparing D_x with the torus discriminant of S, the quantity Jaswal's Prop. 3.3 uses.

This would put an explicit exponent where Jaswal has 1/(16 t s n_T(n_T−1)).

### 4.3 The endoscopic part of the U(3) certificates as a closed formula (Map II)

At every weight, the U(3) characteristic polynomial factors into:
- an endoscopic part, with eigenvalues p^e + a_p(f), for f the CM and non-CM forms in S_{2e+1}(Γ_0(3), χ_{−3});
- a stable part.

**Statement to compute.** For the endoscopic part, the certificate factor is
(p^e + a_p − t·p^e)·(conjugate) = a function of the GL_2 data alone. This removes the large unitary computation for
that part.
- For the CM forms (3 | e) the factor is N_{Q(ω)/Q}(1 − π^{2e}), from my cp09 computation.
- So only the stable U(3) part needs the large matrices. KT-U3-ENDO-EXACT and KT-U3-SPECTRAL-SPLIT (KTOWER, statement
  level) already give the dimension split.
- This is the computation that would make an independent check of the U(3) halves for e = 26-40 cheap.

### 4.4 The CM-elliptic kernel question with the pole method (Map III sideways)

Ishii's Theorem A (once-punctured CM elliptic curves over K) assumes:
1. an analogue of Deligne-Ihara;
2. p ∤ h(K(p));
3. two primes above p in K(p²).

The Ihara paper's method replaces freeness by cup-product generation plus pole separation, and needs only
X^+-finiteness.

**Statement to prove.** Over an imaginary quadratic K of class number one, with p split: if the two-variable analogue
of Greenberg's conjecture holds for K(p^∞)/K, and the Lie algebra of the rational outer image is free (Ishii's
Conjecture 2.3), then the kernel field equals K(E[p])·Ω_{K(p)}. The ingredients needed are:
- a two-variable cup comparison: the pole lemma, with D_α a function of four variables;
- a K-analogue of the FK/WWE generation. This is the missing input, and what to ask for.

### 4.5 The theta chain at the next GL_1: one cubic character over Q(ω) (Map IV)

Map IV starts from a Dirichlet character, that is, GL_1 over Q seen in U(1) of E/F. For a cubic Hecke character χ of
Q(ω), the analogous chain begins in U(1) of a CM extension of Q(ω)·F. The phase lemmas S1-S3 (ALP_MACHINE §2) show
what the sign mechanism needs:
- a central involution commuting with Frobenius (S3: order d with d-th power traces);
- not a reflected relation sFs = F^{−1} (S2, which bounds nothing).

**Statement to compute first.** Determine whether the Weil representation attached to a cubic character carries an
operator s of order 3 that commutes with the Frobenius action on the relevant theta space, or only one that reflects
it. The answer decides at the outset whether Alpöge's sign mechanism can transfer to the cubic case. S1 already shows
that the antidiagonal C_3 dies when s is central.
