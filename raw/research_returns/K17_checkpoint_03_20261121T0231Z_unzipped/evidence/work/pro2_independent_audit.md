# Independent audit of the pro-2 moment argument

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. The reasoning-effort setting is not exposed to the reviewer. Date: 2026-11-21 UTC. Reviewed file: `work/pro2_moment_candidate.md`, including its revised finite-quotient construction A2 and all steps A–E. This is an ordinary mathematical proof review, not a formal proof certificate and not a claim of novelty.

## Verdict

**PASS for the theorem with the precise finite-prime ramification convention in the candidate.** I found no remaining mathematical gap in the proposed deduction from the cited arithmetic and rational Deligne–Ihara inputs. In particular, the bounded-measure coefficients really do retain every element of the pro-2 group, and substitution into the rational weight completion does not require a uniform integral lattice across all weights.

The conclusion being checked is that the usual pro-2 outer action of the tripod is faithful on the maximal pro-2 extension of Q unramified at every finite prime other than 2, allowing real places to complexify. It uses Brown and the special pro-2 arithmetic presentation; it does not use the proposed step-17 bound. It proves neither a general integral free-generation theorem for the weight Lie algebra nor a kernel theorem for irregular odd primes.

The published results are inputs whose precise statements and relevant comparison arguments were checked, not reproved in full. The new group-theoretic, topological, and analytic argument was checked in full. The following additions make its proof independent of shorthand about infinite-rank free groups and remove several possible interpretive ambiguities.

## 1. Source scope and the actual rational image

### 1.1 Arithmetic presentation

I independently opened Gras–Jaulent, *Note on 2-rational fields*, arXiv:0805.1168, Theorem/Definition 0 and Definition 1, pp.1–2, and Theorem 2, p.3. The paper distinguishes the group with splitting imposed at real places from the group unrestricted at infinity. The latter is the one in Theorem 2. For Q it is `C_2 * Z_2`.

The specialization of 2-rationality to Q was checked directly. A rational number with even valuations at every odd prime is, modulo rational squares, `epsilon 2^e`, with `epsilon=+/-1` and `e=0 or 1`. If it is a square in Q_2, valuation forces `e=0`, and reduction of odd squares modulo 8 excludes `epsilon=-1`. Thus the local-square group in condition (iv) is exactly Q-squares. The global and local 2-primary root-of-unity groups both have 2-rank one. This verifies the hypothesis without an unstated convention concerning real primes.

Primary URL: https://arxiv.org/pdf/0805.1168 . Retrieval `turn957389691view0`.

Kronecker–Weber identifies the maximal abelian pro-2 extension unramified outside 2 with Q(mu_(2^infinity)); hence the cyclotomic character is the full abelianization. This is a standard cited input. The two cyclic factors of the presentation therefore map to the corresponding independent factors of `Z_2^x`. Replacing the infinite generator by `c gamma` if necessary is an automorphism of the free pro-2 product and makes its cyclotomic image lie in `1+4Z_2`.

### 1.2 Hain–Matsumoto comparison

I independently read Hain–Matsumoto, arXiv:math/0006158v2, §§8.1–8.4, pp.24–27, including the proof of Proposition 8.2, the definition of the actual Zariski image in §8.3, Proposition 8.3 and its proof, Theorem 8.4 and its proof, Lemma 8.5, and Remark 8.6.

The scope is an arbitrary prime ell. Theorem 8.4 identifies the weight-graded Lie algebra of the **actual image radical** with the rationalized Ihara graded Lie algebra. Its proof explicitly supplies Zariski density of the cyclotomic-kernel image in that radical. Lemma 8.5 removes degree one for the tripod. Remark 8.6 cites Ihara for nonvanishing in the abelianization of all the odd-degree generators. No assertion about a primitive integral Soulé lattice is part of this input.

The factorization from the pro-2 outer action to its continuous rational unipotent completion is in the direction needed here: a trivial pro-2 outer automorphism induces a trivial rational outer automorphism. It is also immediate from functoriality: any representative inner automorphism becomes conjugation by the image of the same element in the unipotent completion. The candidate does not need the converse.

### 1.3 Brown's explicit bridge to the outer filtration

I opened Brown's original Annals paper, *Mixed Tate motives over Z*, 175 (2012), pp.949–950, Theorem 1.1 and the following paragraph. For the exact comparison to the outer arithmetic filtration I additionally checked Brown's own later account:

Francis Brown, *From the Deligne–Ihara conjecture to Multiple Modular Values*, arXiv:1904.00179, §§2.1–2.3, pp.1–4, https://arxiv.org/pdf/1904.00179 . Retrieval `turn345834156view0`.

Section 2.1 defines the pro-ell **outer** Galois filtration for any prime ell. Conjecture 1, p.2, is exactly freeness of its rational positive graded Lie algebra on one generator in each odd degree at least three. Section 2.3, p.4, supplies a continuous Zariski-dense ell-adic realization of the motivic Galois group; Theorem 2.1 and the following paragraph explicitly deduce Conjecture 1. This avoids relying merely on an informal passage from motivic groupoid faithfulness to arithmetic outer faithfulness.

Original Annals URL: https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf . Retrieval `turn473727680view0`.

### 1.4 From graded freeness to the completed Lie algebra

This passage is legitimate but should be stated. Choose a Levi section of the negatively weighted extension. Every finite weight quotient is a rational representation of G_m, so the weight filtration splits there into eigenspaces, compatibly in the inverse limit. In each odd degree choose a lift of the free graded generator with that weight. The induced continuous map from the weight completion of the free Lie algebra to Lie(U) is an isomorphism on associated gradeds. Both sides are separated and complete for the weight filtration, with finite-dimensional finite weight quotients. Induction on the quotient weight proves that the map on each finite quotient is an isomorphism; passing to the inverse limit proves the completed isomorphism. No integral lifting assertion is involved.

## 2. Finite quotients and the first nonzero Magnus degree

The revised A2 is a direct proof of the required topology.

Let F be the free pro-2 group on gamma,h. Let N_n be the closed normal subgroup generated by gamma^(2^n). The groups N_n decrease and have intersection one: any finite continuous 2-group quotient kills gamma^(2^n) for all sufficiently large n, and hence kills N_n. The natural map

`F -> lim F/N_n`

is injective by this intersection calculation and surjective because a compatible tuple of cosets is a nested family of nonempty closed subsets of the compact group F. The compatible quotient maps `F/N_n -> C_(2^n)` have inverse limit the cyclotomic quotient `F -> Z_2`. Kernels commute with this inverse limit, giving

`H = lim H_n`.

For each n, H_n is free pro-2 on the conjugates `gamma^i h gamma^(-i)`, for i modulo 2^n. Indeed, the free group on those symbols, with cyclic permutation action, has semidirect product with C_(2^n) possessing exactly the universal property of `C_(2^n) * Z_2`. Its kernel is the stated free group. The transition maps fold these bases by reduction of i.

This also proves topological generation of H by the compact orbit h_x. To spell out the point used in A2, the kernels K_n of `H -> H_n` decrease to one. Given any open normal subgroup V of H, some K_n is contained in V: otherwise the nested compact sets `K_n intersect (H minus V)` would have a point in their intersection, contradicting `intersection K_n={1}`. Thus every finite quotient of H factors through an H_n. The images of the h_x generate that quotient.

In degree r, the compatible integral Magnus coefficients are exactly

`M_r = lim_n Z_2[(Z/2^n)^r] = Z_2[[Z_2^r]]`.

Products of finite residue partitions are cofinal among finite clopen partitions of Z_2^r: a finite clopen partition is refined by a sufficiently fine product residue partition, by compactness. Inverse limits commute with products, so the completed algebra is `product_(r>=0) M_r`, with the stated concatenation product. It follows that a nonzero expansion has a first finite nonzero variable degree. There is no completion-only element invisible in every such degree.

### An independent proof of the finite-rank Magnus injection

The following proof removes the need to regard this step as an unchecked book citation. For a finite 2-group Q, its augmentation ideal I in F_2[Q] is nilpotent. Induct on |Q|: choose a central element z of order two. The ideal J generated by z-1 is central with J^2=0. The quotient algebra by J is F_2[Q/<z>]. If the latter augmentation ideal has N-th power zero, then I^N is contained in J, hence I^(2N)=0.

Consequently a map from the free pro-2 group on g_1,...,g_d to Q permits continuous substitution `X_i -> image(g_i)-1` in F_2<<X_1,...,X_d>>. The mod-2 Magnus homomorphism is defined by `g_i -> 1+X_i`; its evaluation under this substitution is exactly the given quotient map, because the maps agree on generators. If the Magnus expansion of g is one, g therefore maps to one in every finite 2-group quotient of the free pro-2 group. Residual finiteness implies g=1. The integral Magnus map reduces to this mod-2 map, so it too is injective.

## 3. Substitution and continuity, with denominators allowed

Fix a target weight cutoff N. Its free associative algebra quotient is finite-dimensional, and its augmentation ideal has zero (floor(N/3)+1)-st power, because every generator has weight at least three. Each coefficient of `Y_x=rho(h_x)-1` is a continuous Q_2-valued function on compact Z_2 and is therefore bounded.

For a continuous bounded Q_2-valued function f on a profinite space X and a Z_2-valued measure mu, the integral is well defined: multiply f by a fixed power of two to make it Z_2-valued, approximate uniformly by locally constant functions, and use the bound on mu to prove convergence. This integral depends continuously on mu for the inverse-limit topology of measures. Modulo any prescribed 2-adic precision the scaled f is constant on a finite clopen partition, so the integral at that precision uses only finitely many measure values.

For each d <= floor(N/3), the d-th Magnus coefficient can therefore be evaluated by integrating the ordered product `Y_(x_1)...Y_(x_d)` over Z_2^d. Only finitely many d occur. External products of measures and the same finite-partition argument prove multiplicativity. This constructs a continuous algebra substitution at weight cutoff N. These substitutions are compatible in N. Composing with Magnus gives a continuous homomorphism on H which agrees with rho on every h_x; topological generation then proves equality on H. This last argument does not apply the free pro-2 universal property directly to a noncompact Q_2-unipotent target.

If r is the first nonzero Magnus degree, the coefficient of an ordered word `s_(m_1)...s_(m_r)` receives no contribution from degrees below r, which vanish, or above r, which have generator length greater than r after substitution. Its value is therefore exactly the ordered r-variable moment in the candidate. The use of weight completion has not lost the generator-length filtration.

## 4. Nonzero linear coordinates and analytic separation

On the abelianization of U, the unipotent part of a lift acts trivially, and the torus acts on the m-th coordinate through chi^m. Thus `ell_m(rho(h_x))=a_m u^(mx)`. If a_m were zero, this coordinate would vanish on every topological generator h_x and therefore on H. Zariski density would force the corresponding nonzero algebraic quotient of U to vanish, a contradiction. This proves a_m is nonzero without any integral normalization.

The Amice transform of a bounded Z_2-valued measure is a bounded-coefficient power series on the open unit polydisc. Its injectivity may be justified by multivariate Mahler expansion or directly by the Iwasawa algebra identification. For the latter, on each finite quotient send the group generator to 1+T. The relations `(1+T)^(2^n)-1` tend to zero in the (2,T)-adic topology. Conversely, modulo 2^a and these relations, the augmentation ideal is nilpotent: modulo 2 it is generated by T with T^(2^n)=0, and lifting this nilpotence through the finite 2-power coefficient filtration proves nilpotence modulo 2^a. The quotient ideals and the (2,T)-adic ideals are therefore cofinal. Completion gives `Z_2[[Z_2]]=Z_2[[T]]`; the same proof in r coordinates gives the multivariate identification, with Dirac measure at x sent to the product of `(1+T_j)^(x_j)`.

The sample points `t_m=u^m-1`, odd m>=3, lie in 4Z_2. The distinct subsequence with m=1+2^j converges to u-1. On the closed disc of radius 1/2 the bounded-coefficient power series is convergent, so the one-variable nonarchimedean identity theorem applies at this interior accumulation point. Iterating the argument one variable at a time proves that a multivariate power series vanishing on the entire product grid is zero. Equivalently, after the first variable has been eliminated, apply the identity theorem to each of its coefficient functions in the next variable. This avoids making a false claim that the odd integers themselves are dense in all of Z_2.

Thus all the moments in Step D cannot vanish for a nonzero first Magnus coefficient. This proves injectivity on H. The cyclotomic action on geometric abelianization detects every kernel element outside H, and functoriality puts a pro-2 outer kernel element in the rational kernel. The claimed injectivity on P follows.

## 5. Review boundaries

The convention at infinity, the use of the actual rational image, and the boundedness of the source measures are essential. One cannot reuse the analytic argument with arbitrary unbounded distributions, and one cannot replace the actual image by an unrelated motivic group without constructing the arithmetic comparison. All three requirements are satisfied here.

The older literature's frequent statement of the kernel theorem only for odd regular primes is not used as evidence either for or against this separate proof. An attribution or novelty claim requires a separate literature review. This audit establishes the deduction written above, conditional only on the explicitly cited established theorems; it does not claim a computer-checked formalization.

