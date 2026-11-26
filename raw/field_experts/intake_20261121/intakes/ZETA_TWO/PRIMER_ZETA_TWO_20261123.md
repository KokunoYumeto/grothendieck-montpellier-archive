# Primer: ZETA_TWO (prompt 35, "RH for the zeta functions of schemes over Z and of motives over Q, from the two proofs")

**Author:** ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026. Recall from my intake
`INTAKE_ZETA_TWO_20261121.md` and from the return.

**The run:**
- GPT-6 Astra (ChatGPT Pro mode); final return only, 21 Nov 00:32 UTC.
- Return: `research_returns/ZETA_TWO_final_20261121T0032Z_unzipped/ZETA_TWO.tex`.

**The two inputs:**
- **A** = Alpöge's theorem: RH and GRH for every Dirichlet L-function. A theorem.
- **M** = GRH for all Hecke L-functions, Masullo's draft. It is not a proof: anything resting on it is conditional
  and is given no credence.

**Checks.** In my intake, 21 findings were checked step by step and 0 refuted.

## Main results

### ZT01: Artin-Tate counts give Dirichlet products

**Statement.** Suppose X is of finite type over Z with exact counts #X(F_{p^r}) = Σ_i p^{ir} Tr(F^r | V_i^{I_p}) at
**every** p. Then ζ_X = ∏_i L(V_i, s−i). In the abelian case, A puts every non-integer divisor on Re s = i + 1/2.

**Mechanism.** Take the Euler product of the count identity prime by prime. Inertia invariants give the bad factors
exactly.

**Relations.** It is the same as bridges F1 and ALPOGE_BRIDGES BR-AT-01.

### ZT03: Dedekind zeta functions

**Statement.** Spec O_K has exact Artin-Tate counts (the permutation representation C[Hom(K, Q̄)]). So RH for ζ_K
holds:
- by A, when K is abelian;
- by M, in general.

**Mechanism.** ZT01 combined with Brauer induction (ZT02).

### ZT02: Artin L-functions under M

**Statement.** Under M, every virtual Artin L(V, s) has its zeros and poles in the strip on Re s = 1/2. Holomorphy is
not claimed.

**Mechanism.** Brauer induction. Finite-order Hecke characters suffice.

### ZT04 and ZT05: identities off a finite set, and a warning

**ZT04.** If the count identity holds only off a finite set S, then ζ_X = R_{X,S}·∏ L(V_i, s−i), where R_{X,S} is a
finite product of rational functions of p^{−s}.

**ZT05.** For Spec Z[1/p], ζ = (1 − p^{−s})ζ(s) has non-real zeros 2πik/log p on Re s = 0.

**What it is good for.** It refutes the gloss "RH for every Λ-scheme": Z[1/p] is binomial, hence a Λ-ring (DP_MULT
DP11). This is the origin of ZETA_NEXT's Λ-scheme rows.

### ZT06: every scheme of finite type, as an algebraic reduction

**Statement.**

  ζ_X = ∏_{p∈S} Z(X_p, p^{−s}) · ∏_a L^S(H^j(Y_a), s)^{±n_a},

with Y_a smooth projective over Q.

**Inputs.**
- Bittner, Thm 3.1.
- EGA IV_3 (8.8.2), spreading out.
- Weil I, 1.6, for convergence.

**Gap I found.** The clause "the CM factors satisfy RH under M" needs a CM/non-CM splitting of the H^j(Y_a).
ZETA_NEXT NG01 closed this gap for motives of abelian type.

### ZT07: an elliptic curve E/Q

**Statement.** ζ_E = ζ^S(s)ζ^S(s−1)/L^S(E, s). Under A, in 1/2 < Re s < 3/2 and off Re s = 1, the order of ζ_E is
minus the order of L(E, s).

**What it is good for.** An off-line zero of L(E, s) cannot cancel inside ζ_E.

### ZT08: the Euler factor is a λ-ring invariant

**Statement.** det(1 − tF) = Σ_j (−t)^j Tr ∧^j, and Tr ψ^r = Tr F^r. So the Euler factor is blind to extensions and to
lattices.

**Source.** SGA 6 V §2.

### CM01: CM motives under M

**Statement.** Under M, for a pure motive of weight w in Anderson's CM category, every zero or pole of L(M, s) in
w/2 < Re s < w/2 + 1 lies on Re s = (w+1)/2.

**Mechanism.** Anderson 1986, Cor. 5.7.2 factors L(M, s) as a product of Hecke L(ψ_a, s)^{m_a}. Twist ψ by |·|^{−w/2}.
This needs M for **infinite-order** unitary characters, which is the draft's claim (Masullo §1.2, p. 12).

### IA rows: A-effective arithmetic

- **IA02.** A gives the bounds of Lamzouri-Li-Soundararajan v3, Thm 1.5:
  - V(q)^{−1} ≤ |L(1, χ)| ≤ U(q) for q ≥ 10^10;
  - bounds for h(−D);
  - n(p) < (log p)²;
  - h_K R_K bounds for abelian K.

  Constants are at statement level.
- **IA03.** The number of supersingular j in F_p is c_p h(−D_p), with explicit two-sided bounds under A.
- **IA05.** A removes the no-Siegel-zero gate for CM Faltings heights: Stark's descent sends an exceptional zero of a
  normal field to a quadratic Dirichlet L-function. This was the seed of ZETA_NEXT and of H15.
- **IA06.** h_F^st of CM by Z[ζ_5] is −1.45251…
- **IA07.** h(Q(ζ_23)) = 3.
- **IA08.** L(1, χ_5) = 2 log φ/√5.
- **IA09.** For every odd p, some odd χ mod p has |L(1, χ)| ≤ π/√6.

IA06-IA09 were recomputed by me.

### Smaller rows

- **SV01, SV02.** An unramified Euler factor sees only the class in K_0. The Kummer extension for the unit 2 over
  Z[1/2] has the same L-function as the split object.
- **ML01, ML02.** Elementary checks of Masullo 1.7.1.1 and 12.5.1.1: the test domain of the latter contains no
  positivity test.
- **ALP01, ALP02.** Divided-power derivation lemmas. ALP02 is a formal consequence of Alpöge's Lean statement
  `detDepth_lower_bound_saturated_even_type`.

## Open rows and gates

- **Q01/Q02, RH for ζ_X in general.**
  - The gate is RH for the non-CM summands up to Tate twist. The first case is h¹(E) for E non-CM.
  - It is not a weight condition.
- **Bad fibres of Λ-schemes.** Taken up and decided by ZETA_NEXT:
  - refuted for nonseparated schemes;
  - proved for proper ones.

## Where it went

- The prompt for ZETA_NEXT (43) was built from §6 of my intake.
- IA05 led to H15, the note `reports_20261123/h15_note/`.
