# F-23 over algebraically closed fields: checked candidate

Run: BR_PENCIL-20261121-R1/fields_literature. Author: GPT-6 Astra Pro (ChatGPT Pro mode); inherited reasoning effort, no separate numerical effort setting exposed. Date: 2026-11-21 UTC. This note distinguishes the integral tensor model from ordinary polynomial powers in small characteristic.

## FL-01. Integral models

Let k be any algebraically closed field. All ranks below are CP border ranks defined by Zariski closure in the indicated tensor space. For a free module A_n with basis e_1,...,e_n, define over Z

    D_n = sum_{sigma in S_n} sgn(sigma) e_{sigma(1)} tensor ... tensor e_{sigma(n)},
    P_n = sum_{sigma in S_n} e_{sigma(1)} tensor ... tensor e_{sigma(n)}.

Let V_n have basis x_ij (1<=i,j<=n), and define

    SD_n = sum_{sigma,tau in S_n} sgn(sigma)sgn(tau)
                  x_{sigma(1),tau(1)} tensor ... tensor x_{sigma(n),tau(n)},
    SP_n = sum_{sigma,tau in S_n}
                  x_{sigma(1),tau(1)} tensor ... tensor x_{sigma(n),tau(n)}.

In each of SD_n and SP_n, every ordered matching word occurs once, with coefficient ±1 or 1. The tensors are invariant under permuting the n slots, and hence are integral divided-power tensors (in the usual identification Gamma^n(V_n) with invariant tensors for a free module). In characteristic zero, they are n! times the normalized polynomial coefficient tensors used in GCT_GINEQ F-23. Multiplying by that nonzero scalar does not change rank. In characteristic p dividing n!, their images under the quotient V_n^{tensor n} -> Sym^n(V_n) are zero, even though the tensors themselves are nonzero. Thus the phrase 'polynomial tensor' must carry the divided-power convention in the all-characteristics theorem. This is not the operation of treating an ordinary polynomial as an invariant tensor by dividing its coefficients by n!.

The defining formulas have integer coefficients. In characteristic two the determinant and permanent models coincide, as they should. This is no obstruction to any proof below.

## FL-02. Border substitution by a proper incidence, any characteristic

Let T be a tensor in A_0 tensor V_1 tensor ... tensor V_b, and let U be its A_0-flattening image in W=V_1 tensor ... tensor V_b. Put q=dim U. Then

    BR(T) >= q - 1 + min_{0 != u in U} BR(u).

Here q>=1 and b>=1; border rank on the residual is with its b separate factors.

Proof. Replace A_0 by the support of T in its first factor, of dimension q. This can be done by a projection with a left inverse, so it does not change the tensor's border rank: product linear maps cannot increase rank or border rank, and applying the projection and its inclusion proves both inequalities. In this new ambient space, the flattening of T has rank q.

Let O be the open subset of A_0 tensor W where the flattening has rank q. The map f:O -> Gr(q,W) taking the image is a morphism. This follows directly on a nonzero-q-minor chart by row reduction, where its coordinates are quotients by that nonzero minor.

For s>=1 let Y be the Segre variety of residual pure tensors and define I_{q,s} to be the set of U' in Gr(q,W) such that P(U') meets sigma_s(Y). This is closed: inside Gr(q,W) times sigma_s(Y), the incidence is the zero locus of the map from the tautological line to the universal quotient W/U'; projection onto Gr(q,W) is proper since sigma_s(Y) is projective. A proper morphism is closed. This is the algebraic replacement for the Euclidean Grassmannian-limit step in GCT_GINEQ F-13/F-18.

Suppose BR(T)<=r. Plain flattening gives r>=q. Every actual rank-at-most-r tensor T' in O can be written as a sum of <=r terms a_i tensor z_i with z_i residual pure tensors. Let L be the span of the z_i, of dimension d with q<=d<=r. Choose d-q+1 linearly independent z_i. Their span L' has dimension d-q+1, and U'=f(T') is a q-plane in L. Consequently dim(U' intersect L')>=1. Every element of L' has residual rank <=d-q+1<=r-q+1. Hence f(T') belongs to I_{q,r-q+1}.

The point T lies in the closure inside O of actual rank-at-most-r tensors in O: for any subset S and open O, closure(S) intersect O = closure_O(S intersect O). Since f^{-1}(I_{q,r-q+1}) is closed in O and contains this set, it contains T. Therefore some nonzero u in U has BR(u)<=r-q+1, proving the inequality. All steps are scheme/variety-theoretic over k; no norm, characteristic-zero polarization, analytic arc, or base change of a secant ideal is used. QED.

Known-method attribution: this is the arbitrary residual-order and arbitrary-algebraically-closed-field form of border substitution; Landsberg-Michalek, arXiv:1608.07486v1, Proposition 2.3, printed p.3, gives the three-factor form for every retained dimension a'<=a, not merely for a'=1. The proof is supplied because the exact all-characteristics higher-order form is needed here, not as a novelty claim for substitution or multidimensional substitution.

## FL-03. Exact residual minima and recursive bounds

For 2<=b<n, group the first n-b slots of any of D_n,P_n,SD_n,SP_n. Write U_{n,b} for its residual image. Let T denote one of the four families consistently. Then

    min_{0 != u in U_{n,b}} BR_k(u) = BR_k(T_b),
    BR_k(T_n) >= binom(n,b)^s + BR_k(T_b)-1,

where s=1 for D,P and s=2 for SD,SP.

Proof. In the row families, the integral residual image has basis Q_I, indexed by b-element subsets I of [n], consisting of the embedded coordinate copy of D_b or P_b on I. Indeed, contraction against any ordered (n-b)-tuple with a repeated index is zero. For distinct indices, the result is ±Q_I (D) or Q_I (P) with I its complement. Every I occurs. Different I have disjoint tensor-basis supports, and each basis vector has a coefficient ±1, so this basis remains independent over every field.

In the polynomial/divided-power families, the corresponding integral image has basis Q_{I,J}, where I,J are b-element row and column subsets. A contraction against a partial matching gives ±Q_{I,J} or Q_{I,J}; a tuple not constituting a partial matching gives zero. Every pair occurs. Again the supports are disjoint and contain a unit coefficient, so the rank is binom(n,b)^2 over every field. This is the tensor form of the unit-coefficient complementary-minor calculation of GCT_GINEQ F-22. It is also a direct proof that no factor of b! or (n-b)! is present in this flattening.

Now take nonzero u in the image and choose one nonzero coordinate c. In a row family, project every residual factor onto the b coordinates I indexing c. Because every word of Q_{I'} uses every index of I', this kills Q_{I'} for I'!=I and maps Q_I to T_b. In a polynomial family, project onto the b-by-b matrix-entry block I times J in every residual factor. Every word of Q_{I',J'} uses every row in I' and column in J', so any distinct pair has a required row or column outside the retained block and is killed. The result is c T_b.

A product of linear maps takes pure tensors to pure tensors or zero; by continuity for Zariski closure it cannot increase border rank. Hence BR(u)>=BR(T_b). Conversely, a single Q_I or Q_{I,J} is a coordinate embedding of T_b with that projection as left inverse. The two maps show its border rank is exactly BR(T_b). This proves the exact minimum. Grouping the first n-b factors cannot increase CP border rank, since every original pure tensor remains pure after grouping. Apply FL-02 to this grouped tensor and the computed q; the resulting lower bound also applies to the original n-factor tensor. This obtains the recursion. QED.

## FL-04. Seed in every characteristic

D_2 and P_2 have 2-by-2 matrices [[0,1],[-1,0]] and [[0,1],[1,0]], respectively, so each has matrix/border rank 2 in every characteristic. SD_2 and SP_2, in variables x_11,x_12,x_21,x_22, have the two off-diagonal coordinate pairs (x_11,x_22), (x_12,x_21), with entries ±1. Their matrices are signed permutation matrices with determinant 1 and rank 4 over every field. Thus

    BR_k(D_n), BR_k(P_n) >= binom(n,2)+1,
    BR_k(SD_n), BR_k(SP_n) >= binom(n,2)^2+3.

In particular the divided-power polynomial models give the predecessor's 39 at n=4 over every algebraically closed field. These inequalities are superseded when stronger multidimensional certificates are available, but they establish exactly the requested F-23 extension.

## FL-05. Why ordinary polynomial powers need a separate statement

For a field of positive characteristic p<=n, the coefficient of a squarefree degree-n monomial in (sum_i a_i x_i)^n is n! times a product of coefficients, hence zero. Therefore the linear span of ordinary polynomial powers ell^n has zero coefficient on every squarefree degree-n monomial. This is a closed linear subspace. The ordinary determinant and permanent polynomials have nonzero squarefree matching coefficients, so neither belongs to any secant of the ordinary-power image; their border rank with respect to that image is infinite.

This does not contradict the finite CP border ranks of SD_n/SP_n, nor the finite symmetric border ranks relative to the complete-linear-system Veronese embedded in divided powers. In characteristic zero or p>n, n! is invertible, the usual symmetrization isomorphism applies, and the tensor CP lower bounds imply the usual polynomial symmetric border-rank lower bounds. In small characteristic, the finite meaningful all-field statement uses the divided-power/complete-Veronese convention. QED.

## Geometric dictionary and precise foundations

The free Z-modules and their coordinate projections define locally free sheaves and morphisms over Spec Z; arbitrary scalar extension preserves the displayed unit-coefficient residual bases and the split coordinate projections. For each algebraically closed fiber k, form the Segre secant over k and its incidence scheme with the tautological bundle on the Grassmannian. The proper image argument is fiberwise and does **not** assert that a global integral secant ideal reduces to the exact secant ideal in every characteristic.

The group schemes GL(A_n), GL(V_n), and products of these act on the tensor modules. The row/column diagonal torus used in the pencil argument is a split subtorus over Z, given on the matrix basis by x_ij -> r_i c_j x_ij. Exterior powers and the Koszul construction are maps of locally free sheaves with integral entries; their minors, not their K_0 classes alone, certify ranks. K_0, lambda and gamma operations track source and target bundles and cannot replace the rank calculation (predecessor F-20). No l-adic sheaf, purity, or motive is required to prove FL-01–FL-05; a constant stalk or abstract point motive forgets the embedding on which tensor rank depends (predecessor F-21). This precisely states where the proof transfers and where no claimed transfer exists.

Exact foundations (published locators, not claims that those texts contain tensor-complexity bounds): EGA II Definition 5.4.1 and Proposition 5.4.2, printed p.100; Theorem 5.5.3(i), printed p.104, NUMDAM PMIHES_1961__8__5_0, one-based PDF leaves 97 and101. FGA Bourbaki expose221, Theorems3.1–3.2, printed pp.259–260, PDF leaves12–13; Hilbert specialization after Proposition3.8 and Remarks3.9, pp.265–266, leaves18–19, NUMDAM SB_1960-1961__6__249_0. SGA3 ExposeI §§4.5–4.6 (GL and module schemes), p.29, scan leaf42. SGA6 ExposeV Definition2.1, Examples2.2(b), Lemma2.2.1, pp.314–316, leaves321–323; representation-ring example p.317/leaf324; Proposition3.2(ii) p.325/leaf332; §3.10 equation(3.10.1) p.331/leaf338. All the facsimile leaves listed in this paragraph were freshly downloaded, rendered and visually checked in this run on2026-11-21; see source_crosswalk.md and CHECK_EVENTS.tsv. Other inherited locators in the crosswalk retain their separate predecessor provenance.

No Montpellier manuscript cote for these modern findings is established. CSG17 and CSG44 are published-work catalog identifiers and must not be mislabeled unpublished-manuscript shelfmarks. The algebraic proof is independent of Grothendieck's analytic Resumé.

## Complete proof review

On 2026-11-21 the author reread the entire statements and proofs of FL-01–FL-05. The delicate points checked were: invariant tensor versus ordinary symmetric quotient; unit coefficients surviving p=2; full-rank open-domain image morphism; closure inside an open; properness of the incidence projection; rank monotonicity; disjoint-support independence and coordinate isolation; and the vanishing of squarefree coefficients of ordinary polynomial powers when p<=n. No gap found in these statements with the explicit model conventions above. This is a targeted proof check, not a formal theorem-prover verification. Independent parent review remains required before inclusion among checked final findings.
