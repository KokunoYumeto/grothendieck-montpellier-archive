# Primer: deterministic finite-field constructions after Dirichlet GRH (GRH_ALGORITHMS and its finishing run)

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), for the main session to read after a
compaction. It restates the run's mathematics; it develops nothing new.

**The runs.** GRH_ALGORITHMS (prompt 67) and its finishing run GRH_ALGORITHMS_FINISH (prompt 67c), both GPT-6 Astra
(ChatGPT Pro mode).

**The paper.** `research_returns\GRH_ALGORITHMS_FINISH_checkpoint_04_20261123T1744Z_unzipped\workbench\work\unfiled\v1\papers\grh_algorithms.tex`,
159 pages. Statement ids GRH-P001 to P146 are in `STATEMENTS.tsv` beside it, and the labels below are LaTeX labels in
the paper.

**Checks.** "Checked by us" means a targeted proof check by Claude Opus 5.5 at effort high, in the intakes of 22-23
Nov in `field_experts\intake_20261121\intakes\GRH_ALGORITHMS\` and `...\GRH_ALGORITHMS_FINISH\`. Everything else
carries the run's own checks.

**Notation.** A: every nontrivial zero of every Dirichlet L-function, ζ included, has real part 1/2 (Alpöge's theorem).
For primes p ≠ r, r odd: d = ord_r(p), q = p^d, a = v_r(q−1), N = Φ_d(p) (its r-part is r^a), and the formal algebra is
𝒟 = F_p[Z]/Φ_r(Z). The problem throughout is Lenstra's: given p and r, construct F_{p^r} (an irreducible polynomial of
degree r) deterministically. The hard inputs are r ∤ p−1 and a ≥ 2.

## 1. The algebraic gate
**Teichmüller equivalence** (`thm:teich`, P004; Lenstra 1991, Theorems 3.1, 5.1, 5.2). A presentation of F_{p^r} and an
element η ∈ 𝒟 of order r^a with σ_c(η) = η^{ω_a(c)} are interconvertible in deterministic polynomial time, with no
analytic input. Here σ_c(Z) = Z^c and ω_a(c) is the tame lift of c mod r^a.
- Mechanism: the maximal r-primary unit, made equivariant, generates the Kummer extension over 𝒟, and Galois descent
  along Gal(Q(ζ_r)/Q) gives the degree-r field.
- Every construction below outputs such an η (called U), and so F_{p^r).

## 2. The unconditional cofactor theorems (the paper's first main result)
**Statements.**
- `thm:small-cyclotomic-cofactor` (P128): cost poly(r, log p, M), where M = N/r^a.
- `cor:two-primary-cyclotomic-cofactor` (P131): the same with M₂ = N/(2^{v₂} r^a).
- `thm:threshold-cyclotomic-cofactor` (P144): cost (r + L + C_L + log p)^c, where C_L removes as well every prime power
  ℓ^k of N with ℓ ≤ L, ℓ ≠ r and r ∤ ℓ−1.
- `thm:selected-cyclotomic-cofactor` (P145): for disjoint sets S (roots of order ℓ supplied) and T (r ∤ ℓ−1, nothing
  supplied) of odd primes dividing N, cost (r + C + Σℓ + log p)^c, with C = N/(2^s r^a ∏_{S∪T} ℓ^{v_ℓ}).

No factorization of the cofactor and no root of unity beyond those listed is an input. Checked by us: the
root-extraction lemma (cp08) and P145/P144 (cp04).

**Proof mechanism (`lem:projected-primary-root-extraction`, then the descent of P105-P110).** First a field
calculation in one component K = F_q, simulated over 𝒟 by splitting on zero divisors.
1. To take an r-th root of a promised r-th power z, form R = K[X]/(X^r − z) ≅ K^r, with the automorphism
   τ(α) = ζα of order r.
2. Project to the primitive cyclotomic part: P(v) = v^{E_d}, E_d = ∏_{λ|d}(1 − p^{d/λ}), so that P(v)^N = 1 and
   r ∤ E_d.
3. Search the shifts α + i, i < trM, where t = 2^{ω(d)}. The coboundary δ_i = τ(b_i)/b_i of b_i = P(α+i), raised to
   the cofactor, is a non-scalar for some i. The proof: if every value failed, the rational function
   H(Y) = ∏_e ((F_e(ζβ)+Y)/(F_e(β)+Y))^{μ(e)} would satisfy H^{rM} = 1 at more points than the degree allows, so H
   would be constant. That contradicts H(0) = ζ^{E_d} ≠ 1 and H(∞) = 1.
4. A non-scalar element of prime order ℓ ≠ r, compared with the ℓ-th roots of unity, gives a proper factor of
   X^r − z. A proper factor of degree j with 0 < j < r gives a root, by Bézout on b^r = z^j.
5. The r-power-order case uses the odd-prime commutator of Bach, von zur Gathen and Lenstra (§5.10). If ν has order
   r² and both ν^r and τ(ν)/ν are scalar, then τ^j(c₀) = ε^{j(j−1)/2} ν^j c₀ at j = r forces ν^r = 1. That is a
   contradiction.
6. **New in P145**, for ℓ ∈ T with no root supplied: adjoin E = A₀[Y]/Φ_ℓ(Y). It is étale of rank ℓ−1, because
   ℓ | q−1. Find y with y^r = z in E by step 4 with θ = Y. Then b = Norm_{E/A₀}(y) satisfies b^r = z^{ℓ−1}. Since
   r ∤ ℓ−1, Bézout gives a root in A₀. No tensor product over T is ever formed.
7. Small characteristic (p < rhC) is handled by an absolute-Frobenius splitting of finite étale algebras.

## 3. The fixed-valuation theorem under A (the paper's second main result)
**Statements.**
- `thm:fixed-wild-cm` (P125) and `cor:fixed-wild-prime-degree-field` (P126): assume A. For each fixed odd prime r and
  fixed b ≥ 2, if v_r(p^d − 1) ≥ b, an equivariant U of order r^b in every component of 𝒟 is computed in time
  C_{r,b}(log p)^{c_{r,b}}. If the valuation equals b, F_{p^r} is constructed in that time, for every such p, with no
  exceptions.
- `thm:dirichlet-ninth-root-cubic` (P119): the case r = 3, b = 2, i.e. cubic fields when v₃(p+1) = 2.

Checked by the run: an adversarial audit and a statement-only reconstruction. Not checked by us.

**Proof mechanism** (after Pila 1990, Theorem D; Mumford 1967, §6; Lenstra 1991).
1. A gives an imaginary quadratic field of conductor O(log² p) in which p splits.
2. Its compositum with the fixed real subfield R_b of Q(ζ_{r^b}), of degree r^{b−1}, carries a primitive CM type
   with an explicit principal polarization.
3. Exact theta constants give equations and a complete addition law for the CM abelian variety of dimension r^{b−1}.
   Colmez/Faltings/Pazuki height bounds and algebraic recognition give its model; it has marked good reduction.
4. Reducing over all residue fields at once lets Pila's point-counting algorithm compute a Frobenius polynomial
   without choosing a factor of Φ_r.
5. The CM supports separate the real embeddings, and the cyclotomic tensor product turns one embedding into the
   equivariant root.
6. The exponent grows with r^{b−1}, so the bound is not uniform in the valuation.

`cor:fixed-set-cubic-cofactor` (P146), under A: combining P145 with A-only residue maps for fixed totally real Galois
fields (P140) gives cubic fields in time K_S(C_S(p) + log p)^{c_S} for any fixed finite S. Statement level only.

## 4. The pure-field gate and the classical route
**Pure-field equivalence** (`thm:kummer`, P001), under A: RH(ζ_{Q(p^{1/r})}) ⇔ RH(ζ_{Q(ζ_r, p^{1/r})}). Either gives an
auxiliary prime ℓ ≪ r² log²(rp) with ℓ ≡ 1 mod r and p^{(ℓ−1)/r} ≢ 1 mod ℓ, and the Adleman-Lenstra construction.
- Mechanism: the normal closure has group F_r ⋊ F_r^×. Its regular representation splits into abelian characters
  (covered by A) and copies of one induced order-r Hecke character, so ζ_E = ζ_K (ζ_F/ζ)^{r−1}.
- A one-sided window inequality would suffice (`prop:window`, P017); it is not derived from A.

## 5. Results from A alone
**Classical table** (§1 table; Q03). These follow from A:
- Miller's test with bases below 2 log² n;
- r-th nonresidues for r | p−1;
- primitive roots given the factorization of p−1, and Shoup's g(p) ≪ log⁶ p;
- the order/factoring equivalence;
- the least prime in a progression, ≤ (φ(q) log q)² with gcd(a, q) = 1;
- the Rubinstein-Sarnak limiting distribution.

Still needing more than A:
- the strict race densities (grand simplicity);
- Hooley (ζ of Q(ζ_k, a^{1/k}));
- Bach's class-group bound and class-group mixing (Hecke class characters);
- the isogeny expanders over imaginary quadratic fields, and CM split-prime selection (ring class zeta).

**Nonresidues in a presented extension** (`thm:nonresidue`, P006), under A.

**Averages over the input prime, under A.**
- `thm:fixed-r-almost-all-auxiliary` (P074): with C_r > (r−1)/(2 log r), all but O(√P log log P) primes in (P/2, P]
  have ℓ ≤ C_r log P log log P. Checked by us.
- `thm:almost-all-small-tate` (P092): with C > 1/log 3, Y³ − (k+3)Y² + kY + 1 is irreducible for some k ≤ C log P, for
  all but O(√P log log P) primes. Checked by us.
- `thm:aa-12r` (P068): a simultaneous table ℓ ≡ 1 mod 12r for all r ≤ (log P)^{a₀}.
- `thm:selected-menu-auxiliary` (P143): any k = ⌈log P/(2 log r)⌉ menu primes.

Mechanisms:
- Orthogonality: the indicator that p is an r-th power modulo every menu prime ℓ is a mean of characters mod
  M = ∏ ℓ, with coefficients of total mass one and exactly one principal character.
- A with uniform conductor dependence: |Σ Λ(n)χ(n) log(x/n) − δ_χ x| ≪ √x log q (`lem:dirichlet-log-weight`, from
  Lamzouri-Li-Soundararajan Lemmas 2.1-2.3).
- So the exceptional p count is O((P/r^m + √P log M)/log P), and r^m ≥ √P is enough.
- For P092, the independent characters come from the private prime divisors > K+3 of N(k) = k² + 3k + 9, of which
  there are at least (1/2 − o(1))K (after Cilleruelo's quadratic-value product estimates). Each such divisor ramifies
  in the cyclic cubic field of h_k, since disc h_k = N(k)².

## 6. Interfaces resting on outside preprints
**Tang's interfaces** (`thm:tangfront`, P009): polynomial-time factoring over a presented field, and construction from
a promised prime power. They assume OpenAI's prime-field theorem (Theorem 1.2, Proposition 10.1) and the uniform
Dedekind zero-free strip of Cureton and Thorner (Hexagon 2610.00200v2, Theorem 1.1; Lemma 8.1 needed Tang's posted
revision). Both are 2026 preprints. The paper marks every conclusion drawn from them.

**Quasipolynomial factoring** (`thm:quasipoly`, P008): factoring in time (d^{log d} log p^m)^{O(1)} under A and RH for
ζ_{Q(p^{1/r})}, r in the finite bad set 𝓑. P008 is unconditional when the bad set is empty.

## 7. The open rows (QUESTIONS.tsv at finishing checkpoint 04)
| row | state | current gate |
|---|---|---|
| Q01 | uniform construction from A alone; partly proved | **open** when the valuation and the cofactor C_L both grow. Proved: fixed (r, b) under A; C_L polynomial unconditionally |
| Q02 | the classical auxiliary prime ≪ poly(r, log p) from A alone | **open**. Gate: the one-sided window inequality for the induced order-r Hecke function (or pure-field RH) |
| Q05 | independent re-proofs | closed (same model) |
| Q06 | the paper | 159-page clean build. Changed-page readings and release pending |
| Q07 | density route | **open**. The log discriminant and conductor are of order r log(rp) |
| Q08 | elliptic trace route | **open**. A curve with trace-discriminant valuation exactly 1 |
| Q09 | CM discriminant selection | **open**. A polynomial-budget CM order with prime class outside r·Cl |

The many "route" propositions in the paper's second part (fixed menus, tensor cone, twist conductors, Jacobi sums,
supersingular and ordinary Tate trials) are proved obstructions to those particular methods. They are not impossibility
theorems.

## 8. Update, 24 Nov 2026: checkpoint 07 and Codex's edition
Added by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7); the text above is unchanged (backup in
`integration_backups/20261123/GRH_ALGORITHMS_FINISH/`).

**Sources.**
- Checkpoint 07: 190 pages, 164 statements, 575 check events.
- Codex's edition (GPT-6.2 Astra at reasoning effort ultra): 191 pages, at
  `Codex\2026-11-22\the-two-tracks-share-no-sound\outputs\67c_PUBLICATION_DRAFT\checkpoint-07\grh_algorithms.tex`.

**New main theorem, P149 (`thm:bounded-congruence-cofactor`, the edition's Theorem 1.2).**
- Statement: under A, for fixed odd prime r and fixed t, the cofactor construction of §2 also removes the full powers of
  odd primes ℓ ≠ r up to the cutoff L with v_r(ℓ−1) ≤ t. For t = 0 it is unconditional, which is P144. For r = 3,
  t = 1 that is every eligible ℓ except ℓ ≡ 1 mod 9.
- Mechanism:
  - P148: a prime-conductor cyclotomic quotient of Q(ζ_ℓ) of rank (ℓ−1)/r^s, which is prime to r, is cut out by its
    integral period basis. Its residue map comes from P147, a quantitative completely-split residue map in totally real
    Galois fields of fixed degree, under A, by CM theta of fixed dimension.
  - Then the norm-and-Bézout descent of P145, applied on that quotient instead of on the full Φ_ℓ.
- Example: p = 251, r = 3, L = 7. Here p + 1 = 2²3²7, so the t = 0 residual is 7 and the t = 1 residual is 1.

**Supporting results.**
- P151-P155: the cyclic descent interface and its limits. A supplied root whose period has bounded r-valuation
  descends (P151); the normalized cyclic lift (P152); the full-cyclotomic lift with a period-drop certificate (P153);
  the primitive cyclic obstruction (P154); balanced examples where the specified operations fail (P155).
- P156: removing the small Frobenius orbit keeps the r-primary depth.
- P157-P158: trace-one local units; residue maps from explicit ideal profiles.
- P159: fixed rational shift menus fail at positive-density primes.
- P160-P162: genus-two Frobenius collisions and quotients, and restricted CM reflex obstructions.
- P163: Guo's literal digit loop fails; constructive repair.
- P164: the Frobenius ideal detects residue degree one.

**Codex's five fixes, all checked by us 24 Nov** (`INTAKE_GRH_ALGORITHMS_FINISH_20261124_cp07.md`):
1. P160: the two displayed elliptic quotients are not all of them. At t = 0, (x, y) ↦ (x², y) gives v² = u³ + 1, with
   j = 0, whereas j(E_±(0)) = 54000.
2. P163: Guo's Hypothesis (*) needs "a supplied prime k | p^d − 1". The literal loop in his Lemma B.1 misses solutions:
   F₁₉, x = 4, y = 9 = x⁴; and F₁₀₉³, y = (v⁴, v¹³, v²²) with v = 97 of order 27. The repair extracts base-ℓ digits
   support by support.
3. P164: "detects residue degree one".
4. P156: a wording change.
5. P149: the sign b = (−1)^j f(0), and one auxiliary adjunction per root extraction.

**Open rows.** Unchanged from §7. The uniform gate of Q01 is now the cofactor after removing the bounded-congruence
primes (P149).
