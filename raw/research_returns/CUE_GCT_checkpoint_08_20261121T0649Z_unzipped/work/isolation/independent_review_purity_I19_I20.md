# Independent targeted whole-proof review: I-19 and I-20

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read the complete statements, proofs, examples, and scope paragraphs of I-19 and I-20 in `work/isolation/findings.tex`. The arguments pass this targeted mathematical review. This record does not claim a formal verification, a new execution of the author's examples, or a complete literature audit.

## I-19: higher-rank cuts

Over F(x), the columns selected by J form a basis of the rank-r column space, and the restriction to I has invertible coordinate matrix M. Thus A=A_{*,J}M^{-1}A_{I,*}. Clearing det M gives the claimed polynomial identity, with degrees δ for U, at most rδ for V, and at most rδ for Δ. The identity holds over any field; no characteristic-dependent division remains after clearing Δ.

The grouped product has the displayed matrix dimensions: the first boundary ends in dimension r₁, each interior block has dimensions rⱼ by rⱼ₊₁, and the last boundary begins in dimension rₘ. Treating the cut variables as elements of K=F(X) removes precisely those variables from the coefficient-variable blocks. It does not make the remaining block matrices univariate or prove that their internal width has fallen; the text correctly states a product over disjoint blocks and retains the original dependencies over F.

For disjoint blocks, each coefficient of the product is an ordered product of one coefficient from each block, with the boundary contractions. Replacing each family by another spanning the same K-vector space leaves the span of these ordered products unchanged by multilinearity. Independent parameter sets are necessary for this argument and are explicitly imposed. The local Lagrange-curve discussion is also correct: sampled values span the coefficient span if every nonzero scalar functional is hit, and interpolation gives both inclusions of coefficient spans.

The example with A(x)=[[1,x],[x,x²]] and e₁ boundaries computes 1+xy. It correctly shows that the residual rational coefficient-field dependence is not tested by sampling an empty collection of remaining blocks. For the sufficient gate, a cut variable occurs with degree at most (rⱼ+1)δ≤wδ. A point hitting the multiplied output also hits the original output. No uniform construction for the shared-variable higher-rank class is inferred from the factorization alone.

## I-20: bounded total corank

Since a nonzero output cannot contain a rank-zero factor, every singular layer has positive generic rank and contributes at least one to the total corank. Hence the true singular variable set has cardinality at most κ. A chosen nonzero coefficient g in those variables has individual degree at most δ. Multiplying by one nonzero maximal minor of each singular factor raises the corresponding individual degree to at most (rᵢ+1)δ≤wδ. The product is nonzero in the polynomial ring, so the specified (wδ+1)-point grid has a point where both g and every chosen minor survive. Specialization cannot exceed the generic rank, because all larger minors vanish identically. It therefore preserves every cut rank exactly while leaving a nonzero remaining output.

The product of the determinants of the other factors is a nonzero univariate polynomial of degree at most nwδ. Thus the common shift exists. The proposed gauge is algebraically correct: Pᵢ=Pᵢ₋₁Aᵢ(a) at an invertible layer and Pᵢ=Pᵢ₋₁ at a constant cut, and the transformed factors Pᵢ₋₁AᵢPᵢ⁻¹ telescope. Invertible-layer constant coefficients become I; each constant cut is conjugated by an invertible matrix and retains its rank. Only the right boundary changes by Pₙ.

Let dᵢ be the dimension of the span of all prefix coefficient rows. At an I-constant layer, dᵢ can only grow. At a constant cut of rank rᵢ, its decrease is at most w−rᵢ, because right multiplication has a kernel of that dimension on the full row space. All dᵢ are positive; otherwise the final polynomial would vanish. If U and D are the sums of increases and decreases, then U−D=dₙ−1, so U≤w−1+κ.

The support induction selects actual coefficient rows. At an I-constant layer, retained rows survive as coefficients with exponent zero in the new variable. If the dimension grows, all candidate rows are old selected coefficient rows multiplied by a new nonconstant coefficient; their support rises by at most one, and the cumulative dimension increase rises by at least one. If the dimension does not grow, the old basis is retained. At a constant cut, a basis can be selected from images of the old basis, without increasing support. Consequently all final basis rows have support at most U≤w−1+κ. Some such row has nonzero contraction with the final boundary.

Setting the other shifted variables to zero preserves that nonzero coefficient. The (δ+1)-point product grid on its support supplies a nonzero evaluation. Counting the possible cut subsets and assignments and the remaining perturbation supports gives the displayed upper bound; overcounting overlapping descriptions is harmless. The family is invariant under variable permutation, so the unknown order poses no additional constraint. For δ=0 the output is constant, all three grids have size one, and the same proof has its expected trivial endpoint.

The positive conclusion is polynomial for fixed w+κ. The proof does not bound κ for an arbitrary ROABP, so it does not resolve the general construction gate.
