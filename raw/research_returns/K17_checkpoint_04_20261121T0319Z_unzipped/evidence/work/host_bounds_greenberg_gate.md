# What the Step 17 and Host bounds imply about Greenberg and K12

Date: 2026-11-21 UTC. Author/reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; reasoning effort not exposed.

## Finding K17-HOST-GREENBERG-GATE

The recovered quantitative conclusions do **not** supply a proof that the one-variable plus Iwasawa module is finite. This is more precise than an appeal to the conjecture's status: an explicit nonfinite, torsion, μ-zero Iwasawa module satisfies bounds stronger than the numerical conclusions under consideration. The full Host and downstream window quantifiers do not exclude it. Their uniformity is over an auxiliary family adding only extensions of 2-power degree, while the odd cyclotomic tower either changes the fixed character or enters through a layer estimate retained as a hypothesis.

The same numerical information does not force K12 to vanish. Below is an exact abstract example that satisfies the seventh-power size bound with constant one and has a nonzero simulated K12 group at a prime above the verified Vandiver range. There is also an explicit pair of artificial trace polynomials satisfying the integrality, Galois stability and archimedean restrictions, whose evaluation gcd has that prime as a divisor.

These examples are counterexamples to the proposed inference from **those numerical and module-theoretic properties**. They are not cyclotomic counterexamples, not actual K-groups, and not actual automorphic trace systems. No assertion is made that the entirety of the stipulated arithmetic source contract logically cannot imply Greenberg by a different argument.

## 1. Exact source statements and quantifier order

All Lean references below are relative to `src/Development/AutomorphicArithmetic/`, at pinned revision `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of the supplied public source mirror. These are source-content readings, not a new Lean build.

### Case I

`AutomorphicVarieties/HeightAndVanishing/Counts.lean:CountI` says

    for every fixed χ, there exist C,r1,r2,
    for every admissible host h with h.χ=χ, every admissible t,
    every 0<e<t and every finite set of Case-I primes,
    the normalized sum of local-kernel lengths is at most (N t)^C.

The bad-prime and exceptional-character exclusions are part of Case I. Neither length finiteness nor a positive polynomial upper bound says that a length is zero. The closed proof composition is already recorded in `work/host_refinement.tex`.

### Full PointHV

`AutomorphicVarieties/HeightAndVanishing/LayerLe.lean:PointHV` says

    for every χ and every function j:N→N, there exist C,r1,r2,
    for every admissible host h, t and B≥0,
    if LayerLe χ ℓ (j(ℓ)) t B holds for every ℓ in Bχ,
    then the sum of all odd-prime plus lengths is at most (N t)^C+C B.

The function j is chosen before the constants. For a fixed odd prime p it supplies one fixed tower depth j(p), not a variable running through all depths. Replacing j(p) by successively larger numbers permits C,r1,r2 to change. Moreover, B is an input bound for the finite-layer groups, and the output retains it with a nonnegative multiplier C. The theorem does not bound B independently of layer depth and gives no contraction of that term.

`LayerLe`, in the same file, quantifies over presentations of the full cyclotomic base `Lchi χ ℓ=Q(μ_(ℓm))` and over cyclotomic ℓ-power extensions of degree ℓ^j. `StmtFields.lean:IsLayer` requires both a cyclotomic ℓ-power extension and exactly that degree. `LengthEqAddEigen.lean:VVat` requires finiteness and bounds the sum of the strict Selmer lengths for 1≤e<t. Thus no unbounded-tower uniformity is concealed in the definition.

The source's final `PointArith.point` combines the already obtained outside-bad-set bound with the bad-set estimates `SumIn`; those retain the same B. Its proof was previously read completely, and the exact declarations were read again for the present task.

### The closed downstream window theorem

The potentially stronger endpoint was also checked. Freshly retrieved and Git-blob-verified:

- `CharacterBoxes/ExistsPageN.lean`, complete file;
- `AutomorphicVarieties/CMFieldExponentialBounds/AdmissibleOfPageN.lean`, complete file and complete proof of `vwinAt_of_joint`.

Retrieval hashes and pinned API URLs are in `work/host_strength_retrieval.json`. The exact public file URL for the endpoint definition is

<https://github.com/CocoSgt/riemann-hypothesis-lean/blob/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean>.

`VWin` means `∀χ, VWinAt χ 401`. For each fixed χ, each fixed 0<ε<1/52 and each admissible function a(x) satisfying

    x^(2+8ε) ≤ 2^a(x) ≤ 2 x^(2+8ε),

it chooses J≥1 and X0. In certain intervals Y≤x≤Y² with X^(1/J)≤Y and Y²≤X, the conclusion is

    Σ_ℓ log(ℓ) Σ_(1≤e<floor(x^401)) length(S_ℓ(E,e))
        ≤ sqrt(exp(x^ε)) = exp(x^ε/2).

The primes q,d and the field E are also required to satisfy the explicit `WinPair` and `IsChiField` conditions. The conclusion is a growing bound on a sum, including both signs and the prime two. Its threshold and window exponent are chosen after ε and the page function. Sending ε to zero at a fixed x is therefore an invalid exchange of quantifiers. A fixed polynomial in x is eventually smaller than exp(x^ε/2) for every fixed ε>0, so even a uniform polynomial contribution across all x would satisfy this endpoint, without needing the flexibility of selecting windows.

The intermediate definitions `ThmBab`, `ThmHV` and `JointWin` in `AutomorphicVarieties/PrimeSetBoundDataOfPrimitiveChar.lean` and the complete proof of `HeightAndVanishing/ThmHV.lean:thmHV` were also read. Their passage to windows chooses the fixed depth `j(ℓ)=floor(log_ℓ R_ℓ)+3` before applying PointHV. It does not make this depth a new freely varying argument of the final bound.

For exact closure of the endpoint, the source composition is `UpperTheory.V.v_window_of_literal_automorphy_n UpperTheory.V.SmallClassNumbers.litN`. The latter is in `SmallClassNumbers/CorGKOf.lean`; the former is the final theorem of `ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean`. The complete intermediate `HVCore.lean:of_four_alt` was freshly read: it obtains a BConst and its ThmBab proof from `Win.thmBab_of_lemmaK` using Poitou–Tate, local finiteness/duality, `FW.ferreroWashington` and the established LemmaK witness. It supplies ThmBcFree by `Odd.thmBcFree_of (ML.iv (U.pt_s hN) hN.coh.uo)`. Finally `HeightAndVanishing/JointWinOfCounts.lean:vwin_of_counts` obtains JointWin401 through `jointWin_of_counts` and ThmBc401 through `thmBc_iff`. These are the exact providers for the conditional premises of `vwin_of_joint`, under the same stipulated source contract as CorGK. The compatibility model argument would also apply if VWin were merely imposed as a stronger numerical test.

## 2. The Host family does not contain an odd cyclotomic tower

Fix χ of modulus m and order o. The actual associated field is

    E_h = F_χ Q(μ_(2^(a+2)))^+ Q(sqrt(−q)) Q(sqrt(−d)),
    N = lcm(2^(a+2),m) q d.

The three fields adjoined to F_χ have degrees a power of two, two and two. Consequently [E_h:F_χ] is a power of two. All these fields are abelian over Q. For any fixed odd p, the p-primary part of Gal(E_h/Q) therefore maps isomorphically to the p-primary part of Gal(F_χ/Q). In particular its order is the fixed number p^(v_p(o)), independent of a,q,d.

Thus varying a increases the two-primary tower only. Varying q,d changes quadratic fields, not the depth of a p-cyclotomic tower. An unbounded tower Q(μ_(p^(n+1))) requires unbounded p-parts of the fixed character's order, hence changing χ. The source constants may then change. In such a cyclotomic specialization p divides its modulus and lies in Bχ, so the full PointHV also carries the p-layer premise explicitly.

Restriction followed by norm across a host extension of 2-power degree is multiplication by that degree, a p-adic unit. Where the local conditions are preserved, this gives an injection or direct summand on p-primary groups. It can transport a host upper bound to a smaller field, but the right side grows with N; it supplies no decreasing bound or vanishing. The host-size requirement q,d>2t+1 itself forces N>4t². Taking large hosts or a large twist interval makes the displayed polynomial bound larger.

Even replacing the available field-dependent CorGK by the separately defined stronger global CorG with fixed conductor and discriminant exponents would not settle this issue. At cyclotomic conductor p^(n+1), a polynomial conductor bound is exponential in n, whereas the λ=1 module below has finite-layer length only n+1. Such an estimate is quantitatively compatible with positive λ.

## 3. A nonfinite μ-zero module satisfying all the relevant growth scales

Let p be an odd prime, let Γ≅Z_p have generator γ, let u=1+p and let

    Λ=Z_p[[Γ]],       M=Λ/(γ−u).

The identification γ↦1+T identifies this quotient with Z_p[[T]]/(T−p)=Z_p. Thus M is not finite, is Λ-torsion, is Z_p-torsion-free, and has μ=0 and λ=1. For every e≥1, its Tate-twisted Γ-coinvariants are

    M(e)_Γ = Z_p/(u^(e+1)−1),
    length_Zp M(e)_Γ = 1+v_p(e+1).                    (H1)

Here is a direct valuation proof. If b=1+p^s c with s≥1 and c a p-adic unit, the first nonzero term in b^p−1 is p^(s+1)c and every later binomial term has strictly higher valuation, since p is odd. Induction gives v_p(u^(p^n)−1)=n+1. Raising a number of that form to an exponent prime to p does not change the valuation of its difference from one. Writing any positive integer k=p^n k0 therefore gives v_p(u^k−1)=1+v_p(k), proving (H1).

These lengths are finite at every positive twist and satisfy

    log(p)·length M(e)_Γ ≤ log(p)+log(e+1).

Their aggregate satisfies the stronger exact formula

    Σ_(e=1)^(t−1) length M(e)_Γ
        = (t−1)+v_p(t!)
        ≤ (t−1)+t/(p−1) < 3t/2.                     (H2)

The factorial inequality follows by summing floor(t/p^j) over j≥1 and bounding the geometric series. Selecting one Δ-character progression only decreases this sum. The individual lengths fit every positive power of e with a sufficiently large fixed coefficient; the aggregate fits a linear bound in t. With t=floor(x^401), their sum is O(x^401); even allowing a number of auxiliary character components polynomial in x still fits exp(x^ε/2) for every fixed ε>0.

On the other hand, the finite cyclotomic-layer quotients of M satisfy

    M/(γ^(p^n)−1)M ≅ Z_p/p^(n+1),                   (H3)

so their lengths are unbounded and M remains infinite. These quotients have compatible surjective norm-model maps given by reduction, and their inverse limit is M. The model already has the μ-zero and finite-generation properties used in the Greenberg discussion; those properties together with the size estimates do not kill λ.

## 4. A fixed-character example also permits a nonzero simulated K12

Take the prime

    p=2147483659=2^31+11,

and give M the even Δ-character θ=ω^(−6). Let

    S_e = (M(e)_Γ)^Δ.

Since |Δ|=p−1 is a p-adic unit, the idempotent decomposition is integral, and

    S_e = M(e)_Γ if e≡6 mod(p−1), and S_e=0 otherwise.

In particular S_6≅Z/p. The character θ is neither trivial nor quadratic, so this model does not use the exceptional characters already proved to vanish in the rational K-group argument. Its nonzero positive twists start at e=6. For every such e,

    log |S_e| ≤ log p+log(e+1) < 22+e ≤ e^7.

At all other twists the length is zero. Thus defining the purely formal finite groups G_k=S_(2k) gives

    log |G_k| ≤ (2k)^7 for every k≥1,
    G_3=Z/p ≠0.

This demonstrates that even a seventh-power bound with absolute constant one, all the relevant elementary character exclusions, μ=0 and the verified-prime cutoff do not imply either finiteness of M or vanishing of the formal degree-twelve group. The model is not asserted to be an arithmetic realization of X or K-theory.

Primality of p was checked by exact trial division through floor(sqrt(p))=46340. A compact additional check is p−1=2·3·149·2402107, with the factors prime by trial division, and Lucas witness 2: 2^(p−1)=1 mod p and gcd(2^((p−1)/q)−1,p)=1 for every displayed prime factor q. Reproducible exact arithmetic is in `work/host_strength_model.py` and `work/host_strength_model_results.json`.

## 5. The two trace-prime bounds do not force a numerical certificate

The checked refinement gives actual, uncomputed trace integers n_7(6), n_13(6) with

    |K12(Z)| divides gcd(|n_7(6)|,|n_13(6)|)^2.

A computed gcd equal to one would prove the desired vanishing. Counting bounds and size bounds do not determine that gcd. The following exact artificial example makes this limitation explicit even after retaining the usual trace-polynomial restrictions.

For q=7,13 put E_q=q^12+q^6+1 and b_q equal to the least nonnegative residue of −E_q² modulo p. Define F_q(X)=X²+b_q. These are monic integral polynomials, their root multisets are Galois stable, and every root α has |α|²=b_q<p<9q^12. Thus the normalized roots α/q^6 obey the trace absolute-value bound |α/q^6|<3. Their evaluation is nonzero and divisible by p. The exact values are

| q | E_q | b_q | F_q(E_q) |
|---|---:|---:|---:|
| 7 | 13841404851 | 1328819029 | 191584488250615151230 |
| 13 | 23298089949291 | 1446269942 | 542800995285254312397672623 |

Their gcd is exactly 15032385613=7p. The degree-two index sets also fit the cohomological counting upper bounds by a wide margin. Therefore monicity, integrality, Galois stability, the archimedean trace bound, nonvanishing, bounded cardinality and two-prime square divisibility do not alone imply a trivial gcd. These polynomials are deliberately abstract; their roots have not been identified with automorphic representations or a single global compatible system. Information making that identification, or an actual complete Hecke polynomial computation, is extra input.

The coarser global bound is even less decisive at k=3. Its stated natural constant C is at least one, so C·6^7 is at least 279936, far above log(2^31). An argument combining the verified small-prime range with a total-size bound would need log|K12|<log(2^31), or an equally strong prime-by-prime replacement. The available bound provides neither inequality.

## 6. Exact remaining gates

For Greenberg, a genuinely new input must eliminate positive-rank Λ-torsion in X^+, rather than merely show finite specialization lengths or bound their growth. For example, with the appropriate arithmetic control already proved, a uniform bound on the p-class-group orders throughout the actual p-cyclotomic tower would address λ; the Host theorem does not supply that uniformity. The new kernel theorem may continue to use X^+ finite as its explicit hypothesis.

For K12, possible additional inputs remain an actual multiplicity-preserving Hecke polynomial certificate with a sufficient evaluated gcd, an independent vanishing theorem for the required cohomology, or the finite-rank topological gates being investigated separately. The new low-perfection-excess simpliciality lemma is valid, but it does not by itself supply these homology vanishings. No new primary K12 vanishing was obtained from the Host or window bounds.

## Actual checks performed

Read the complete reconstructed Host theorem, the exact source definitions of CountI, LayerLe, PointHV, IsLayer, Host, Big, X, CaseI, VVat, VVplusLe, ThmBab, ThmHV, JointWin, VAt and VWin. Read the full `thmHV`, `vwinAt_of_joint` and `vwin_of_joint` proofs and the relevant assembly files. Rechecked the rational quantitative audit and the two-prime norm follow-up. Retrieved two missing primary source files at the pinned commit and verified their Git blob hashes. Independently proved (H1)–(H3), the fixed-character specialization, the Host degree restriction, and the abstract polynomial example. Ran exact integer primality, modular power, evaluation and gcd checks; no floating-point eigensystems or actual Hecke matrices were used. No original scan verification or new Lean execution is claimed.
