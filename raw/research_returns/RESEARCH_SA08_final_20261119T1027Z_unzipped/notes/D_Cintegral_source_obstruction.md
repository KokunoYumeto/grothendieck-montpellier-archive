# C.3: an obstruction to every multiweight elementary source over Z

Date: 2026-11-19. Author of this run: GPT-6 Astra (OpenAI), /root/shadows_coalgebras. No priority is claimed. This is a proved obstruction to a construction, not a counterexample to connectedness of the full admissible category.

## Exact theorem

Let S=Gamma_Z(T). Let E be any set, and for every alpha in E choose an integer d_alpha>0 and a_alpha in Z. Put R=Gamma_Z(U_alpha : alpha in E), wt(U_alpha)=d_alpha, and let f:R→S be the PD homomorphism U_alpha↦a_alpha T^[d_alpha]. For each alpha let Phi_alpha be the standard contractible simplicial marked disk, rescaled to weight d_alpha. Define

G = S tensor_R DR(direct_sum_alpha Phi_alpha; {U_alpha}),

where the relative forms kill the marked line in each Phi_alpha. Then G is an admissible eventual PD theory over Z if and only if E has one element, its weight is one, and its marking coefficient is +1 or -1. More precisely, every other choice fails eventual horizontal acyclicity already in exterior degree zero.

This includes arbitrary infinite sets of marked generators, rather than only the proposed generators in all weights n≥N.

## Proof

The simplexwise marked lines split off. Therefore DR_n is R tensored with the ordinary free PD Poincare complex on a free complement. G_n resolves S vertically, and every G_n^{w,q} is free over Z (possibly of infinite rank). The degree-zero simplicial R-module Gamma(direct_sum Phi_alpha) is a projective resolution of Z=R/R^+: it is R-free in each simplicial degree, and its positive-weight parts are contractible because the direct sum of the Phi_alpha is a contractible simplicial module and positive divided powers preserve its simplicial contraction. Consequently

pi_i(G^0)=Tor_i^R(S,Z).

Suppose G^0 is acyclic in every weight w≥W. Each normalized integral chain complex in such a weight is an acyclic complex of projective Z-modules concentrated in nonnegative degrees. Its cycle sequences split inductively, so it is contractible. Reduction modulo every prime p therefore remains acyclic in weights≥W.

Fix p, and write R_p, S_p for the reductions. Eventual vanishing of pi_0 means that S_p/(f(R_p^+)S_p) is bounded in weight. For large s, consider the indecomposable element x_s=T^[p^s] of S_p^+/(S_p^+)². In an expression for x_s in f(R_p^+)S_p, a term with a positive-weight multiplier maps to zero in indecomposables. The indecomposables of R_p are spanned by gamma_{p^r}(U_alpha), of weight d_alpha p^r. A nonzero image of weight p^s therefore requires d_alpha=p^e and a_alpha nonzero modulo p. Thus there exists an alpha of p-power weight N=p^e with p∤a_alpha.

For this alpha, S_p is finite free over R_alpha=Gamma_Fp(U_alpha), with basis T^[r], 0≤r<N. In weight mN+r the basis product has coefficient

a_alpha^m (mN)!/(m!(N!)^m) binom(mN+r,r),

which is nonzero modulo p: Legendre's formula gives valuation zero for the factorial quotient, and Lucas' theorem gives the same for the binomial factor. Hence S_p tensor_{R_alpha} Fp = S_p/I_N, where I_N is the full weight tail≥N. Decompose R_p=R_alpha tensor R_rest. Associativity of derived tensor and freeness give

S_p tensor^L_{R_p} Fp ≃ (S_p/I_N) tensor^L_{R_rest} Fp.

If E has another element beta, decompose each divided-power algebra in R_rest as its p-digit tensor factors Fp[y_{beta,r}]/(y_{beta,r}^p), with wt(y_{beta,r})=d_beta p^r. Split R_rest=L tensor H, where L consists of the factors of weight<N and H those of weight≥N. Every positive-weight generator of H acts by zero on V=S_p/I_N. Over the field Fp, the derived tensor Kunneth formula gives

Tor_*^{R_rest}(V,Fp) ≅ Tor_*^L(V,Fp) tensor Tor_*^H(Fp,Fp).

The degree-zero first factor V/L^+V is nonzero, since its augmentation surjects onto Fp and its weight-zero piece is Fp. The second factor has Tor_1=H^+/(H^+)², with independent classes y_{beta,r} for every sufficiently large r. Their weights d_beta p^r are unbounded. Thus pi_1(G_p^0) is nonzero in unbounded weights, contradicting eventual acyclicity. Therefore E has exactly one element. (The empty set fails pi_0 immediately.)

For this unique element the preceding pi_0 argument holds for every prime p. Thus d is a power of every prime, so d=1, and a is divisible by no prime, so a=±1. Conversely these choices give the standard theory after replacing the marked generator by its negative if necessary, and are admissible.

All uses of infinite tensor products are filtered-colimit statements; the argument needs no finite-generation assumption. The p-digit algebra decomposition follows by the divided-power basis and the fact that base-p digit factorials are units. The Kunneth decomposition can equivalently be obtained by tensoring free resolutions over L and H; the field hypothesis makes its homology tensor product exact.

## Consequence for the remaining global C.3 gate

For N>1 the standard tail subtheory A_N has S in weights<N and the standard theory F in weights≥N. It is admissible over Z, but its weight-one exterior-degree-zero simplicial module is the constant ZT. A map from the sole admissible elementary source of the theorem would have to send the standard marked disk to that constant module carrying its marked vector to ±T. Such a map is impossible: the marked vector is the boundary of the normalized degree-one disk generator, whereas the target has zero differential. Thus no multiweight elementary source of the above form maps to A_N.

This does not refute the common-source conjecture: A_N itself maps to F and is a non-elementary source for the pair (A_N,F). It proves that a global argument must genuinely leave the entire class of these free marked-disk sources. In particular the p-local G_N construction cannot be globalized merely by adding arbitrarily many independently marked generators.

## Other routes checked in this pass

- Tail truncation B_N(A)=im(S→A)+A_{weights≥N} is a sub-PD-DGA when the coefficient map is injective in low weights and terms remain flat. For integral torsionfree theories the coefficient map is in fact injective if it is eventually injective: a nonzero killed a T^[d] would have nonzero arbitrarily high divided powers over Z. The operation does not supply maps between different high tails, so it does not settle uniqueness.
- Taking an arithmetic product of p-local models still lacks a uniform flasqueness bound; the above theorem shows that an algebraic direct sum of independent marked generators does not repair it.
- A naive cosimplicial derived-Gamma replacement is now positively ruled out by A-022, not merely unproved: finite underived sections give different H² groups in weight two.
- No counterexample to connectedness or simple connectedness of the full integral admissible category has been obtained by these arguments. The precise remaining gate is a non-elementary strict-PD comparison with controlled eventual bounds, or an invariant of all admissible morphisms that distinguishes two such objects.
