# Cubic balanced-RFE investigation: exact smaller gate

Working note, 2026-11-21. Author: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`, run CUE_GCT-20261121-purity. Parts 2-3 below were integrated as P18 after complete root and isolation proof reviews. P19 subsequently closes the full cubic gate by the middle-interval argument recorded below. The separate prolongation converse in part 1 remains an audit and is not a hidden input to P19.

## 1. Cubic prolongation converse in every characteristic

For distinct nodes, decode a multilinear cubic by the alternating tensor W_ijk=c_{ijk}/Delta_{ijk}. The HMM characterization says balanced I2 membership is the vanishing of its contractions by 1,a,a^2. For a fixed i, the quadratic partial has decoded two-vector B^i_jk=(a_j-a_i)(a_k-a_i)W_ijk. Its balanced I1 membership is contraction by 1,a equal to zero. For fixed i,k, write omega_h(i,k)=sum_j a_j^h W_ijk. Those two quadratic equations give omega_1=a_i omega_0 and omega_2=a_i omega_1. Swapping i,k and using alternation gives omega_1=a_k omega_0. Distinct nodes force omega_0=omega_1=omega_2=0. Thus every partial lying in I1 implies the cubic lies in I2, in every characteristic. The converse is the already used pole extraction. No Euler division by three is needed.

## 2. Minimal counterexamples have ordered three-interval support

Suppose there is a nonzero cubic in I2 of width at most three, and take one with the fewest essential variables. Delete unused variables first; the rational generator projects onto the same generator for the retained nodes, and coefficient-cut ranks do not increase.

At any proper prefix cut, let C_d be the coefficient block of left degree d. The HMM contraction equations connect only adjacent blocks: an output two-vector of left degree e receives a contraction from C_e on the right or C_(e+1) on the left. Therefore a zero block separates the kernel conditions on its two sides, exactly the mechanism in HMM Proposition8.6. In particular, if C1=0 then the C0 cubic alone lies in I2, and if C2=0 then the C3 cubic alone lies in I2. A nonzero such extreme component is obtained by zeroing the opposite variable set, so preserves the width bound and contradicts minimal essential-variable count.

If C0 is nonzero, C1 must consequently be nonzero; P17's three-consecutive-block lemma then forces C2=0; the preceding observation forces C3=0. Symmetrically, C3 nonzero implies only C2,C3 can be present. If neither extreme is present, only C1,C2 remain. Thus every prefix sees support counts in two adjacent degrees at most.

For any two support triples their prefix counts therefore differ by at most one. Let alpha be the largest first position among support triples, beta the smallest second position, gamma the largest second position, and delta the smallest third position. Then alpha<=beta and gamma<=delta: a strict reversal of either inequality supplies a prefix with counts differing by two. Every monomial has its first variable in [1,alpha], its second in [beta,gamma], and its third in [delta,n]. Since all variables are essential, any gap has length zero. The three ordered intervals overlap in at most one variable at each interface. Hence an unresolved minimal counterexample is an ordered trilinear polynomial with at most two shared boundary variables.

## 3. The disjoint ordered trilinear case is impossible

Assume f is homogeneous of degree one in each of three disjoint consecutive nonempty blocks U,V,W, belongs to balanced I2, and has coefficient-cut ranks at most three. Common translation fixes f because the ideal has no nonzero multilinear degrees below three. The three differentiated block degrees are distinct, so f is separately invariant under common translation within each block.

Let r be its coefficient rank across U | (V,W). Since f is linear in U, write f=sum_i X_i B_i(V,W), with span{B_i} of dimension r. Separate translation in U gives sum_i B_i=0. Every essential last U variable has B_i nonzero, and the preceding B's already span the full r-dimensional space. At the cut just before that last variable, the B_i rows from earlier variables span r dimensions and the constant-prefix row contains X_last B_last, which is independent by its X_last degree. Thus r+1<=3, so r<=2. Reversing the order proves the analogous bound across (U,V) | W.

Neither rank can be one: that would factor f into a nonzero linear form times a quadratic, impossible in the prime I2 ideal whose minimum nonzero degree is three. Hence both ranks are two. Choose independent linear vectors L(U),N(W) of length two and write f=L(U)^T M(V)N(W), where M(V)=sum_j X_j M_j is a 2-by-2 linear matrix.

For each essential middle variable j, the nonzero partial L^T M_j N lies in the prime balanced I1 ideal. If M_j had rank one, it would be a product of two nonzero linear forms, impossible in I1. Thus every nonzero M_j is invertible. Separate translation in V gives sum_j M_j=0, so at least two middle variables occur.

Cut between any two consecutive essential middle variables. The degree-two-left/degree-one-right part has coefficient rank two because the prefix contains an invertible M_j and L,N are independent. The degree-one-left/degree-two-right part also has rank two because the suffix contains an invertible M_j. Their degree blocks have disjoint row and column indices, giving rank at least four, a contradiction. This argument uses neither quadratic factorization nor division by the characteristic.

## Gate at the P18 stage, subsequently closed by P19

The shared-boundary-variable cases remain unresolved. Setting an overlapping boundary variable to zero does not automatically preserve the balanced I2 ideal: imposing a zero value at its node lowers the numerator budget and leads to an unbalanced rational generator after rescaling. Thus the disjoint trilinear argument cannot be promoted by an unjustified specialization. The two boundary variables, and their coupled quadratic partials in I1, are the remaining concrete cubic gate in this attempt.


## 4. Closure of both boundary cases: P19

In the minimal-counterexample intervals A,B,C, two essential variables j<k in B outside A union C have nonzero bilinear partials on A and C. Prime one-pair membership and absence of linear equations force each matrix to have rank at least two. At the cut after j, the partial at j is a literal degree-two-left submatrix, while the partial at k is a literal degree-one-left submatrix. The ranks add to at least four. Therefore B contains at most one exclusive variable and at most two shared endpoints, so |B|<=3. Every support triple meets B. But projection off B is injective on ker[1;a;a^2], by Vandermonde independence, hence on its third exterior power. The nonzero cubic decoder cannot vanish under that projection. This contradiction proves the full cubic theorem.

The complete independently reviewed proof is P19_all_cubic_balanced.tex, SHA2564bb5f2f9588840bf41986b657ba3493ebd92cda0f01bea09f52ba896b1535cee. It was integrated on 2026-11-21 after root and isolation complete readings. The one-boundary output-space calculation and the broader conjecture about two-dimensional spaces of one-pair quadratic annihilators were not needed; no unproved vector-valued quadratic claim is promoted.
