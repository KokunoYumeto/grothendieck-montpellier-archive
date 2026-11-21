# Fixed-field semidirect geometric towers: bounded primary-source probe

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.

## Outcome and exact target

This bounded search did **not obtain an applicable exponent bound**. It does not assert that no such theorem exists in the literature. No new main-route witness condition is closed, and no side-stream result is being counted as movement.

Write `p = char(k)`, let `ell` be an odd prime different from `p`, and fix a smooth projective curve `C/k` over a finite field. The proposed objects are unramified, geometrically cyclic covers `D_r -> C` of degree `n_r=ell^r`, defined over the original field and equipped with a rational lift of the prescribed point. Their deck groups may be nonconstant. Let `B_r` be the **actual primitive conductor n_r subvariety**, defined by the integral projector as in A45, and put

    M_r = exp B_r(k)[p^infinity].

For genus two in characteristic two, A47 would apply if

    ell^r > (2 M_r - 1)^2,

so a bound `M_r=o(ell^(r/2))` on a suitable pointed tower would suffice. A theorem about the number of generators, geometric p-rank, Newton slopes, an isogeny class, or a class-number limit in the ell-adic topology is not automatically such a bound.

## Primary sources checked and their exact scope

### 1. Bandini–Longhi, 2009: the arithmetic abelian tower is constant

Andrea Bandini and Ignazio Longhi, *Selmer groups for elliptic curves in Z_l^d-extensions of function fields of characteristic p*, Annales de l'Institut Fourier 59 (2009), 2301–2327. Proposition 4.3 and Lemma 4.4, printed pp. 2311–2313.

Primary: <https://www.numdam.org/article/AIF_2009__59_6_2301_0.pdf>.
Retrieval references: `turn643684767view0`, `turn744039191view0`.

For a function field of characteristic p whose constants do not contain the infinite constant Z_l-extension, Proposition 4.3 says its only arithmetic Galois Z_l-extension is the constant extension. In particular this applies to finite constants and l different from p. The proof uses the finite geometric abelian quotient left after taking Frobenius coinvariants of the Tate module. This is consistent with the finite group J_C(k) classifying constant abelian pointed unramified covers. It does not exclude nonconstant geometric deck groups or their nonabelian arithmetic normal closures.

**Read scope:** the setup, Lemma 4.2, Proposition 4.3 and Lemma 4.4, with their complete displayed proofs. The paper's Selmer-control assertions concern a fixed nonisotrivial elliptic curve; they are not used as statements about the growing primitive factors B_r.

### 2. Bandini–Longhi, 2025v3: cross-prime abelian formulas, no bound supplied

Andrea Bandini and Ignazio Longhi, *The algebra Z_l[[Z_p^d]] and applications to Iwasawa theory*, arXiv:2312.04666v3, 28 May 2025. Theorem 1.2, pp. 3–4; Theorem 7.12, pp. 39–40; Corollary 7.14 and Remark 7.15, pp. 40–41.

Primary: <https://arxiv.org/pdf/2312.04666>.
Retrieval references: `turn643684767view1`, `turn207791708view0`, `turn698794505view2`.

Their p is the tower prime and their l is the class-group prime. Theorem 1.2 concerns **abelian arithmetic Galois Z_p^d-extensions**; it expresses valuations/ranks using unspecified nonnegative coefficients. Theorem 7.12 identifies characteristic ideals with special-value ideals under explicit splitting and primitive-root/non-Wieferich hypotheses. Neither conclusion bounds those valuations. The stated eventual boundedness in the arithmetic example concerns a **constant-field tower**. Remark 7.15 extends that constant-field statement to other positive characteristics, not to geometric semidirect towers. An equality of ideals still requires a bound on its special values before it can supply M_r.

**Read scope:** opening setup, complete Theorem 1.2 statement, complete Theorem 7.12 statement, Corollary 7.14 and Remark 7.15. This audit does not claim a new whole-proof reading of Theorem 7.12; the sibling's separately retained audit records its earlier full reading.

### 3. Ozaki, 2023: genuinely nonabelian, but convergence in the other topology

Manabu Ozaki, *On the p-adic limit of class numbers along a pro-p-extension*, arXiv:2306.08407v1, 14 June 2023. Theorems 1–2 and Propositions 1–2, Section 2, pp. 2–7.

Primary: <https://arxiv.org/pdf/2306.08407>.
Retrieval reference: `turn442654420view0`.

Theorem 1 is stated for number fields and finitely generated, possibly nonabelian, pro-p Galois groups. Theorem 2 is abstract: a discrete prime-to-p torsion module with finite invariants under every open subgroup has invariant-group orders converging **p-adically** along normal filtrations. Relabeling the tower prime as ell, this is ell-adic convergence, not a bound on the exponent at the curve's characteristic p. The theorem is therefore not an exponent estimate even where its module hypotheses can be verified for a function-field system.

**Read scope:** both theorem statements and all of Section 2's displayed proof, including the reductions through the two propositions and the finite-group representation argument. The external representation theorem invoked there is not independently reproved here. Sections 3–4 were not audited.

### 4. Cais, 2022v2: geometric and nonabelian, but characteristic-primary towers

Bryden Cais, *Iwasawa Dieudonné theory of function fields*, arXiv:2207.02283v2, 4 September 2022. Introduction and Corollaries 1.4–1.5, pp. 1–7.

Primary: <https://arxiv.org/pdf/2207.02283>.
Retrieval references: `turn744039191view1`, `turn207791708view1`.

Here the tower group is pro-p and the ground-field characteristic is the same p. The curves have fixed constants; ramification, when present, is total at the specified finite set. Corollary 1.5 treats rational **p-torsion**, rather than the maximal exponent of the full p-primary group, in ramified torsion-free p-adic Lie towers. The geometric Dieudonné results are also in characteristic-primary towers. These hypotheses exclude the prime-to-characteristic cyclic covers required in the present route.

**Read scope:** opening setup on pp. 1–2 and complete Corollaries 1.4–1.5 statements. Neither the entire introduction nor the proofs of these corollaries were independently audited in this probe.

### 5. Bandini–Valentino, 2015: noncommutative Selmer control uses the tower prime

Andrea Bandini and Maria Valentino, *Control theorems for l-adic Lie extensions of global function fields*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (5) XIV (2015), 1065–1092. Theorems 1.2–1.3, pp. 1067–1068, and the preceding setup.

Primary: <https://journals.sns.it/index.php/annaliscienze/article/download/401/391>.
Retrieval reference: `turn272516663view0`.

The arithmetic extension has l-adic Lie Galois group, and the studied Selmer group is **l-primary for a fixed abelian variety**. The case l equal to the characteristic is treated separately, still with the coefficient and tower primes equal. Their finiteness and corank control statements cannot be substituted for a bound on characteristic-p primitive Jacobian exponents in an ell-adic tower with ell different from p.

**Read scope:** complete Introduction (Section 1), field/Galois-group setup in Section 2.1, and Theorems 1.2–1.3 statements. The control-theorem proofs were not audited here.

### 6. Deng–Kezuka–Li–Lim, 2025v2: a recent noncommutative theorem has the same mismatch

Li-Tong Deng, Yukako Kezuka, Yong-Xiong Li and Meng Fai Lim, *Non-commutative Iwasawa theory of abelian varieties over global function fields*, arXiv:2405.20963v2, 16 October 2025. Theorem 1.3 and admissibility definition, pp. 1–3.

Primary: <https://arxiv.org/pdf/2405.20963>.
Retrieval reference: `turn272516663view1`.

The coefficient prime p is explicitly **different from the field characteristic**, equals the Lie-tower prime, and the admissible extension contains the constant Z_p-extension. Theorem 1.3 proves the M_H(G) assertion and vanishing of the relevant mu-invariants for Selmer groups of a fixed abelian variety. It is not a characteristic-primary exponent bound on changing primitive Jacobian factors. The similarity of the nonabelian arithmetic group does not remove those differences.

**Read scope:** opening Introduction passages on pp. 1–3, admissibility definition, full Theorem 1.3 statement and ensuing scope discussion. Neither the entire introduction nor a theorem proof was audited.

## Complete algebra check: what semilinear descent does give

This paragraph independently checks the sibling's retained note
`work/row_audit/FIXED_FIELD_TOWER_DESCENT_NOTE.md`, SHA256
`45b7d4d4344608d355a89252abb02db088ccb39ab9449ee3d5a8cecdbab35649`.
It is conditional on the existence of a compatible Frobenius-stable rank-one Z_ell quotient; no assertion that every curve or selected ell has one is made.

Let `a` be the Frobenius multiplier on that quotient. It is a root of the Jacobian's Frobenius polynomial (or its inverse under the opposite convention), so is not a root of unity. Set

    t=ord(a mod ell),   s=v_ell(a^t-1).

Then `t | ell-1`, `1<=s<infinity`, and for ell odd the binomial lifting identity gives

    f_r=ord(a mod ell^r)=t ell^max(0,r-s).

Indeed every exponent giving 1 modulo ell is divisible by t; writing `a^t=1+ell^s u` with u a unit, binomial expansion, first for an ell-th power and then for a prime-to-ell power, gives `v_ell((a^t)^h-1)=s+v_ell(h)`. This proves the formula and makes the minimal deck field grow on the order of ell^r.

Put `O_r=Z_p[Z]/Phi_(ell^r)(Z)`, `tau_r(Z)=Z^a`, and `R_r=O_r^tau_r`. This uses the **full finite-etale product algebra**, not one selected local factor. The cyclic group of order f_r acts freely on primitive roots, so O_r/R_r is a finite-etale torsor of rank f_r. A45's integral descent, which does not require p to be prime to f_r, gives

    U_r := B_r(k_(f_r))[p^infinity]
         = O_r tensor_(R_r) N_r,
    N_r := B_r(k)[p^infinity].

Each factor of R_r is an unramified DVR. Thus the finite-etale R_r-module O_r is free of constant rank f_r, and its tensor product with any finite R_r-module is, additively and noncanonically, f_r copies of that module. Therefore

    #U_r=(#N_r)^f_r,
    dim_Fp U_r[p]=f_r dim_Fp N_r[p],
    exp U_r=exp N_r.

The primitive subvariety has dimension `(g(C)-1) phi(ell^r)`. Its geometric p-rank is at most that dimension, whence

    dim_Fp B_r(k)[p] <= (g(C)-1) phi(ell^r)/f_r.

For `r>=s` the right side equals the constant

    (g(C)-1)(ell-1)ell^(s-1)/t.

This is a bound on the number of rational p-primary generators, not on their orders. For every e>=1 the abstract module `O_r/p^e O_r`, with Frobenius tau_r, satisfies exactly the same finite descent hypotheses; its invariant group is `R_r/p^e R_r` and has exponent p^e. These abstract modules are **not claimed to be Jacobians or a compatible geometric tower**. They prove that the displayed semilinear identities alone cannot bound the exponent.

## Why the nonabelian limit theorem does not fill the gap

Even numerical ell-adic convergence permits arbitrarily large p-exponents: if d is the order of p modulo ell, then `p^(d ell^r)` tends to 1 ell-adically while the exponent of the cyclic group of that order grows much faster than sqrt(ell^r). This is a numerical nonimplication, not a geometric construction.

There is also an exact abstract-module version within Ozaki's hypotheses. Let `G=Z_ell`. For every r>=1 choose any e_r>=1 and let

    A_r=(Z_p[Z]/Phi_(ell^r)(Z))/p^e_r,
    A=direct_sum_(r>=1) A_r,

where a topological generator of G acts as multiplication by Z on A_r. The action is continuous on the discrete torsion group A. For `H_m=ell^m Z_ell`, its invariants are precisely the finite direct sum of A_r for r<=m: if r>m then `Z^(ell^m)-1` is a unit in O_r, because its reductions at all primitive roots in characteristic p are nonzero. Thus every open subgroup has finite invariants, as required by Ozaki's Theorem 2, while their exponents can grow arbitrarily by choosing e_r. The theorem's convergence conclusion remains valid. This is an algebraic illustration of its scope, not a function-field counterexample.

## Pointing and the exact unresolved arithmetic input

A constant arithmetic extension supplies new constants, not an unbounded family of geometrically connected pointed covers over the original k. Conversely, normal closures of the proposed nonconstant-deck covers add a semidirect arithmetic action; one cannot identify their rational primitive groups with class groups of constant extensions of a single fixed curve. Passing to the minimal deck field preserves the primitive exponent by A45, but its degree f_r grows and the archimedean bounds over that field do not become sub-square-root bounds in n_r.

An applicable theorem would need to control the largest p-primary elementary-divisor length of the **actual primitive return-Frobenius operator**, or directly M_r, for the prescribed-point tower. A unit theorem would also suffice. Neither an equality of characteristic ideals, a rank bound, nor ell-adic convergence of orders supplies that input in the sources checked here. This search therefore leaves the main tower-exponent gate unresolved.

## Evidence and limitations

The search used primary papers for every mathematical attribution above; secondary search hits were discovery aids only. All six primary PDFs and extracted texts are retained beside this note, with SHA256 values in `SOURCE_MANIFEST.json`. Exact URLs and web references are also given above. The bounded search was not exhaustive. No new numerical certificate, theorem of geometric exponent unboundedness, universal nonexistence claim, or formal verification is asserted. The installed 162-page paper and its matched build were not edited.
