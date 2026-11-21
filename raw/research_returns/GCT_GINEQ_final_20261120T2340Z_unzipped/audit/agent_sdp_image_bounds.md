# Norm certificates on a flattening image

Run GCT_GINEQ. Agent `/root/grothendieck_sdp`, GPT-6 Astra Pro;
reasoning effort not exposed. 2026-11-20 UTC / 2026-11-21 Europe/Berlin.
Temporary I-IDs below are intended for root's F13/F14 consolidation.
These are elementary derived forms and applications; no priority claim is made.

## I-01. Image-substitution lemma: independent rederivation

Let T belong to A tensor H_1 tensor ... tensor H_b over C, where A may
itself be a grouped tensor product. Let U be the image of its A-versus-rest
flattening and let q=dim U>0. Then

    borderR(T) >= q + min_(0!=u in U) borderR(u) - 1.

The rank of T on the left is its CP border rank in all the original
factors; the rank on the right uses the ungrouped b remaining factors.
The analogous real statement holds for real Euclidean border rank.

**Proof.** Suppose borderR(T)=r, and take a sequence T_nu of CP rank at
most r converging to T. Over C, the algebraic border-rank closure admits
such a sequence, since the rank-at-most-r locus is constructible and its
complex Euclidean closure is its Zariski closure. Each decomposition of
T_nu has target factors that are simple tensors in H_1 tensor ... tensor H_b.
Let S_nu be their span; its dimension s_nu is at most r, and it contains
the image of the flattening of T_nu. The decomposition target atoms
span S_nu, so a subset is a pure-tensor basis of S_nu.

Choose q fixed source coordinate vectors whose images under the limiting
flattening are independent. For sufficiently large nu their images under
T_nu are still independent, and their span U'_nu is a q-dimensional
subspace converging to U. This step is necessary because the full image
dimension of T_nu may be larger than q. We have U'_nu contained in S_nu.
The span L_nu of any s_nu-q+1 members of a pure basis of S_nu meets U'_nu
in positive dimension, by the dimension inequality for subspaces of S_nu.
Choose a unit tensor u_nu in this intersection. It is a sum of at most
s_nu-q+1 <= r-q+1 simple tensors. A subsequence of these unit vectors
converges to a unit u, and convergence U'_nu -> U gives u in U. Closedness
of the border-rank-at-most-(r-q+1) locus gives borderR(u)<=r-q+1, proving
the assertion. Over R the same compactness argument applies to a real
approximating sequence and real spans. QED.

**Field requirement.** For the complex border rank of a real T, the u
obtained by this argument can be complex. Every uniform estimate on U
used below is therefore proved on U_C, not merely its real points.

## I-02. Projector norm and uniform spectral norm of a subspace

Let U be a nonzero Hilbert subspace of H_1 tensor ... tensor H_b and P_U
its orthogonal projector. Define

    alpha(U) = max_(||x_i||=1) ||P_U(x_1 tensor ... tensor x_b)||^2.

Canonically P_U is a 2b-tensor in the target tensor product tensored with
its conjugate tensor product. Its Hilbert injective norm satisfies

    epsilon(P_U) = alpha(U)
                = max_(u in U, ||u||=1) epsilon(u)^2.

In particular alpha(U)>0. If b>=2, the support-norm bound for an order-b
tensor yields

    min_(0!=u in U) borderR(u) >= ceil(alpha(U)^(-1/(b-1))).

Combining with I-01 gives

    borderR(T) >= q + ceil(alpha(U)^(-1/(b-1))) - 1.

**Proof.** Grouping the first b and conjugate last b factors identifies
the injective optimization with max |<P_U x,y>| over unit product x,y.
Since P_U is an orthogonal projector,

    |<P_U x,y>| = |<P_U x,P_U y>|
                <= ||P_U x|| ||P_U y|| <= alpha(U).

Equality is obtained by taking x=y at a maximizer of the defining
quadratic form. For each product x, the maximum of |<u,x>| over unit
u in U is ||P_U x||, by orthogonal projection. Interchanging these two
compact maxima proves the second identity. Injective norm is positive
on nonzero tensors, so alpha>0. Finally every unit u in U has
epsilon(u)^2<=alpha, and N-01's valid bound
borderR(u)>=(||u||_F/epsilon(u))^(2/(b-1)) gives the displayed conclusion.
QED.

**Conjugation check.** The projector is not being identified with a
holomorphic quadratic form. The second group is the conjugate Hilbert
space. Taking arbitrary complex unit product vectors in that group
is equivalent to taking arbitrary y in the Hermitian pairing above.

## I-03. Symmetric subspaces and the elementary symmetric maximum

If U is contained in Sym^b H, Banach's symmetric spectral-norm theorem
and I-02 give the simpler exact identity

    alpha(U) = max_(||x||=1) ||P_U x^(tensor b)||^2.

Indeed every u in U is symmetric, so its spectral norm is the maximum
of |<u,x^b>| over a single unit vector x. Interchange the maxima over
unit u in U and unit x, then use orthogonal projection. Banach's theorem
is used over C (also valid over R); this is not a real-only argument.

For p_1,...,p_n>=0 with sum p_i=1 and 2<=b<=n,

    e_b(p_1,...,p_n) <= binom(n,b)/n^b,

with equality at all p_i=1/n. Here e_b denotes the sum of all squarefree
products of b different p_i.

**Proof of the scalar maximum.** A maximum exists on the simplex. If
fewer than b coordinates are positive, e_b=0, smaller than its value at
the uniform vector. If exactly s>=b are positive, fixing all but two
positive coordinates p_i,p_j gives the expression

    p_i p_j e_(b-2)(others)+(p_i+p_j)e_(b-1)(others)+e_b(others).

The coefficient e_(b-2)(others) is positive. Averaging the two positive
coordinates therefore strictly increases the value unless they agree.
Thus all s positive coordinates of a maximizer equal 1/s. The value is
binom(s,b)/s^b=(1/b!) product_(j=0)^(b-1)(1-j/s), which is increasing
in s for s>=b. It is at most the value at s=n. QED.

## I-04. Matrix multiplication image

For the first-mode flattening of M_n, U has orthonormal basis

    u_ij = n^(-1/2) sum_(k=1)^n E_jk tensor E_ki.

A unit vector u in U corresponds to a coefficient matrix C=(c_ij)
with ||C||_F=1. As a bipartite matrix between the two remaining factors,
u is, up to row/column permutations and transpose conventions,
C tensor I_n divided by sqrt(n). Therefore

    epsilon(u) = ||C||_op/sqrt(n) <= 1/sqrt(n).

Equality is attained by a matrix-unit C, so alpha(U)=1/n. I-02, with
b=2 and q=n^2, gives

    borderR(M_n) >= n^2+n-1.

**Check.** The tensor's coefficient at (E_jk,E_li) is c_ij delta_(k,l)
divided by sqrt(n), which is exactly the stated Kronecker matrix after
index regrouping. The statement is valid over R and C.

## I-05. Row determinant image and its stronger mode-flattening bound

For a k-versus-(n-k) row flattening of D_n, let b=n-k>=2. The image is
the full alternating subspace U=Lambda^b C^n, embedded isometrically
in (C^n)^(tensor b). It has dimension q=binom(n,b).

First, the orthogonal projector is the antisymmetrizer. For unit vectors
x_1,...,x_b,

    ||P_U(x_1 tensor ... tensor x_b)||^2
      = det((<x_i,x_j>)_(ij))/b! <= 1/b!.

The inequality is the Gram determinant bound, and equality is attained
by orthonormal x_i. Hence alpha(U)=1/b! exactly.

A stronger norm-based uniform image bound is

    ||Flatten_1(u)||_op^2 <= ||u||_F^2/b

for every u in U, so every nonzero u in U has CP border rank at least b.
Consequently I-01 gives

    borderR(D_n) >= binom(n,k)+b-1.

**Full proof of the stronger bound.** For each b-subset I let e_I^wedge
be the normalized alternating tensor: (b!)^(-1/2) times its signed sum
of the b! ordered basis words. These tensors are orthonormal. Write
u=sum_I c_I e_I^wedge. Contracting the first tensor factor with e_1
gives zero for I not containing 1; for I containing 1 it gives
plus or minus b^(-1/2)e_(I minus {1})^wedge. The surviving vectors are
orthonormal, so

    ||u contracted with e_1||^2
      = (1/b) sum_(I containing 1)|c_I|^2 <= ||u||_F^2/b.

For an arbitrary unit x in C^n, use a unitary taking x to e_1. Its b-fold
tensor action preserves U and its Hilbert norm, so the same bound holds
for contraction with x. Maximizing over x is exactly the squared
operator norm of the mode-one flattening. The matrix stable-rank
inequality now gives rank Flatten_1(u)>=b, and that matrix rank lower-
bounds CP border rank. This argument is complex-uniform. QED.

## I-06. Row permanent image

For the same k,b, the row permanent flattening image has the orthonormal
basis

    v_I = (b!)^(-1/2) sum_(orderings of I) e_(i_1) tensor ... tensor e_(i_b),

over b-subsets I. It is the squarefree symmetric subspace. By I-03,

    alpha(U) = max_(||x||=1) sum_I |<v_I,x^b>|^2
             = max_(p_i>=0, sum p_i=1) b! e_b(p)
             = b! binom(n,b)/n^b.

The coefficient identity uses <v_I,x^b>=sqrt(b!) product_(i in I)x_i
up to the harmless Hermitian conjugation. For b>=2 this alpha is
strictly less than one, since it equals
product_(j=0)^(b-1)(1-j/n). Therefore

    borderR(P_n) >= binom(n,k)
                    + ceil((n^b/(b!binom(n,b)))^(1/(b-1))) - 1
                 >= binom(n,k)+1.

All maxima include complex x; their absolute squares reduce to the
nonnegative simplex variables p_i=|x_i|^2, so no field restriction is
hidden in the calculation.

## I-07. Symmetric determinant polynomial image

For the normalized symmetric polynomial tensor S_det_n, the image U
of the k-versus-b flattening has the orthonormal basis of normalized
symmetric b by b minor tensors S_(I,J), over b-row and b-column subsets.
Each basis tensor has coefficients +/-1/b! on its (b!)^2 valid ordered
slots, hence Hilbert norm one; their supports are disjoint. Its associated
polynomial is det X_(I,J). Thus I-03 gives

    alpha(U) = max_(||X||_F=1) sum_(|I|=|J|=b)|det X_(I,J)|^2
             = max_(s_i>=0, sum s_i^2=1) e_b(s_1^2,...,s_n^2)
             = binom(n,b)/n^b.

The middle identity is Cauchy--Binet, equivalently the squared Hilbert
norm of Lambda^b X; its singular values are the products of b distinct
singular values of X. Equality is attained at X=I/sqrt(n). In particular,

    borderR(S_det_n) >= binom(n,k)^2
              + ceil((n^b/binom(n,b))^(1/(b-1))) - 1.

This is an ordinary CP border-rank bound and therefore also a Waring
border-rank bound. For n=4,k=b=2, q=36 and alpha=6/16=3/8, so the
bound is 36+ceil(8/3)-1=38. No asserted equality between CP and Waring
rank is used.

**Elementary form of the Cauchy--Binet step.** In orthonormal wedge
bases the matrix of Lambda^b X consists exactly of the b by b minors.
Take a singular value decomposition X=U diag(s_i) V*. Exterior powers
of U,V are unitary, while the diagonal exterior power has the displayed
products of singular values. This proves the identity without imposing
that X be real, positive, or diagonal in the original coordinates.

## I-08. Symmetric permanent polynomial image: sufficient upper bound

The corresponding permanent-minor image U is a symmetric subspace of
H^b with H=Mat_n(C). Write H as an orthogonal sum of its n row subspaces
H_i. Every permanent-minor tensor uses b distinct rows, so U is contained
in the row-squarefree symmetric subspace W.

For X=sum_i X_i with X_i in H_i and ||X||_F=1, the projection of X^b
onto W retains exactly the ordered tensor summands with b distinct row
indices. Those summands lie in mutually orthogonal row-pattern subspaces.
With p_i=||X_i||_F^2 their total squared norm is

    ||P_W X^b||^2 = b! e_b(p_1,...,p_n).

Since U is contained in W, its orthogonal projection has smaller squared
norm. Applying I-03 to U and the scalar maximum therefore proves

    alpha(U) <= b! binom(n,b)/n^b < 1  (b>=2).

Thus

    borderR(S_per_n) >= binom(n,k)^2
                    + ceil((n^b/(b!binom(n,b)))^(1/(b-1))) - 1
                   >= binom(n,k)^2+1.

This proves only an upper bound on alpha(U); it does not assert that
the row-squarefree projection and the smaller permanent-minor projection
have the same norm. No unproved permanental singular-value formula is
being used. The assertion is complex-uniform because the row norms are
Hermitian norms and the symmetric spectral theorem is used over C.

## Checks and scope

The inequalities above apply to the ordinary CP border rank of the
original ungrouped tensors, because I-01 preserves the b target factors
and begins with a decomposition into pure tensors in all original
factors. They also give symmetric border-rank lower bounds for the
symmetric target tensors. They are lower bounds; none is presented as
an exact rank or as a current record.

The new information comes from a uniform norm restriction on every
nonzero tensor in the flattening image, followed by the image-substitution
lemma. It does not follow from the three scalar norms of T alone, and
it is not the same method as a single linear flattening-rank certificate.
Accordingly, it does not contradict N-01's support conversion limitation
or S-03's statement about matrix norm certificates of one linear map.
It also does not use or improve the scalar Grothendieck constant.
