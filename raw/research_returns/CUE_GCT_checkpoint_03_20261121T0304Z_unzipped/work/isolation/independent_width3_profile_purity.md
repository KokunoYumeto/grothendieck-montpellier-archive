# Independent derivation of the width-three rank-profile concentration lemma

Reviewer/deriver: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

This note gives a direct specialized proof, developed while trying to break the critical rank-profile argument in Liu's unrefereed preprint. The source is Liu (2026), §3.1, Theorem 3.2 and Lemma 3.3, printed pp. 5–6, https://hexagonmath.org/pdf/2611.00634v1 . Its acknowledgment says OpenAI models were used to formulate results and develop/review proofs. Repository dissemination is not a correctness judgment: https://hexagonmath.org/about . The present result is limited to the explicit profile below; it does not certify every theorem of that preprint.

## Claim and algebraic setting

Let L be any field and R be the tensor product of the local truncated polynomial rings L[Yᵢ]/(Yᵢ^{eᵢ+1}). Let Aᵢ depend only on Yᵢ and have size three. Suppose each nonempty interval product has **unit rank** in {0,2,3}: its rank at all Y=0 is that integer, and its next-order minors vanish in the truncated ring. Then for every constant row u, the coefficient rows of uA₁⋯Aₙ are spanned by those supported on at most four variable positions. The constant four is optimal.

Here coefficient rows and their spans are over L. A row obtained as a linear combination of coefficient rows with support at most c is assigned cost at most c. Multiplication by a coefficient at a new position adds at most one to this cost. Constant changes of basis at the cuts preserve costs and all interval unit ranks.

If an interval has unit rank zero then its matrix is zero, so the conclusion is immediate. If the full constant product has rank three, all constant factors are invertible. Normalize them to I. The prefix coefficient-row spaces are nested, start in dimension at most one, and have dimension at most three. At each strict growth select actual coefficient rows obtained by multiplying previous selected rows by a nonconstant coefficient at that position. Retained rows propagate through I. At most two strict dimension increases occur, giving the stronger support bound two.

## Compatible normalization when the full constant rank is two

Write Cᵢ=Aᵢ(0). Choose a two-dimensional row subspace U₀ complementary to the left kernel of C₁⋯Cₙ, and let Uᵢ=U₀C₁⋯Cᵢ. Every Uᵢ has dimension two, since a loss would persist in the full product. Put Uₙ=im(C₁⋯Cₙ), and choose a one-dimensional complement Vₙ. For each cut i let Vᵢ be the inverse image of Vₙ under the suffix map Cᵢ₊₁⋯Cₙ. The composite of this suffix with projection onto L³/Vₙ has rank two because it is an isomorphism on Uᵢ, so Vᵢ has dimension one and complements Uᵢ. The maps Cᵢ send Uᵢ₋₁ isomorphically to Uᵢ and Vᵢ₋₁ into Vᵢ. Transport bases of U₀ and select bases of the Vᵢ. In these cut bases,

\[
C_i=\operatorname{diag}(I_2,q_i),\qquad q_i\in L.
\]

At least one qᵢ is zero. Let π be projection onto the first two coordinates. If Sᵢ is the span of all prefix coefficient rows, then πSᵢ₋₁⊆πSᵢ: the constant coefficient of the next factor retains the first two coordinates. Thus the active projection grows strictly at most twice.

## Stable-projection segment lemma

Consider a consecutive segment on which πSᵢ=T is fixed. Suppose a basis of the starting space is chosen as lifts B₀ of a basis H of T, each of cost at most c, together with a basis of the kernel of π, each of cost at most c+1. Then the final space is spanned by coefficient rows of cost at most c+1.

First suppose every qᵢ in the segment is nonzero. Normalize the remaining scalar constants to one by diagonal cut changes that fix π. All coefficient-row spaces become nested and have dimension at most dim T+1. If the initial kernel has dimension one, there can be no dimension growth and the initial basis of costs at most c+1 suffices. If it has dimension zero, the initial lifts are a basis of cost at most c, and there is at most one growth. A new coefficient row at that growth has cost at most c+1. This proves the claim in this case.

Otherwise let c₀ be the last position in the segment with q_{c₀}=0, and let Q=A_{c₀}⋯A_b be the suffix through the segment's end. Its constant rank is two. By the interval hypothesis it has unit rank two. Its leading two-by-two block U has invertible constant part, hence is invertible in the truncated ring. The vanishing three-by-three determinant gives the Schur-complement graph description: a row in the row module of Q is determined by its first two entries.

Propagate the starting lifts through constant factors to the cut before c₀; call the resulting matrix B. Its rows still have cost at most c and project to H. Since all coefficient-row projections stay in T, write

\[
\pi(BQ)=R H,\qquad \pi(sQ)=\lambda H
\]

for each s in the coefficient-row space at that cut. Here R is a square polynomial matrix with R(0)=I and is therefore invertible. Both sQ and λR⁻¹BQ belong to the row module of Q and have the same active projection, so the graph description gives

\[
sQ=\lambda R^{-1}BQ.
\]

Thus their coefficient rows lie in the span of the coefficient rows of BQ. The reverse inclusion holds because the constant-propagated rows of B belong to the original cut space. If T=0, the graph description directly gives sQ=0 and the same conclusion with the zero space.

We may consequently restart at c₀ using only coefficients of BA_{c₀}. Its constant rows are the lifts of cost at most c, and its remaining coefficient rows cost at most c+1. Their span projects to T. A kernel basis can be obtained by linear combinations of those rows and the lifts, so it still has cost at most c+1. Every later qᵢ is nonzero by the choice of c₀, and every restarted projection equals T because the restarted spaces are contained in the original ones and contain the constant lifts. The preceding invertible-tail argument completes the stable-segment lemma.

All inverses used here exist in the specified finite local algebra. No rational-function specialization at a pole is used. Multiplication by λR⁻¹ proves a coefficient-span containment; it is not an assertion preserving the supports of each individual row. The replacement by B and the restart are the separate steps that establish the cost bound.

## Counting the growth steps

Assume uA₁⋯Aₙ is nonzero; otherwise there is nothing to prove. If πu≠0, the initial projection has dimension one, so there is at most one strict projection growth. Apply the stable-segment lemma with starting cost zero, spend at most one for that growth factor, and apply it again. The total support cost is at most 1+1+1=3.

If πu=0, the initial stable run lies in the one-dimensional passive row space. It is spanned by the constant propagation of u: if a qᵢ vanished during that run, the rank-two suffix graph would force the whole prefix row to be zero, which would force the final row to be zero. Hence the initial run costs zero. There are then at most two strict active-projection growth factors. Each raises the current cost bound by at most one, and each following stable segment raises it by at most one. The total cost is at most four. This proves the claimed concentration over every field and every choice of truncation orders.

## Exact sharpness example

Let P=diag(1,1,0), let Eᵢⱼ be elementary matrices, and take

\[
A_1=P+x_1E_{31},\quad A_2=I+x_2E_{13},\quad
A_3=P+x_3E_{32},\quad A_4=I+x_4E_{23},\qquad u=e_3^\mathsf T.
\]

Direct multiplication gives

\[
uA_1A_2A_3A_4=x_1e_1^\mathsf T+x_1x_2x_3e_2^\mathsf T
 +x_1x_2x_3x_4e_3^\mathsf T.
\]

Every interval containing A₁ or A₃ factors through a rank-two matrix and has constant product P, so its generic and constant ranks are both two. The other nonempty intervals are invertible. This remains a unit-rank assertion after multilinear truncation. Coefficients of support at most three span only e₁,e₂; support four is necessary for e₃. The exact symbolic check of the product and all ten intervals is in `work/purity/check_width3_profile.py` and `width3_profile_check.json`; it is finite evidence for this example, not the proof of the general statement.

## Implication checked for the smaller original-coordinate generator

For width three, the rank-two minor tests have an invertible width-three compound chunk, whose lowest monomials have support at most two, plus at most two endpoint positions. Four sparse interpolation pairs detect them. Once all rank-two intervals survive, rank-one tests have chunks with interval profile {2,3}; the result above gives support at most four, plus two endpoint positions. Six more pairs detect them. Fresh pairs permit setting the later perturbation to zero, so all earlier nonzero minors remain nonzero as polynomials in the enlarged parameter field. The common center t in every original variable is individually transcendental and preserves every full-rank interval. Thus the original-coordinate construction uses t·1+SV₁₀, without a Hasse-jet estimate, a moment curve, an affine-coordinate claim, or any RH/GRH assumption. Isolation's standalone theorem supplies the complete interval-test induction and final evaluation grids.
