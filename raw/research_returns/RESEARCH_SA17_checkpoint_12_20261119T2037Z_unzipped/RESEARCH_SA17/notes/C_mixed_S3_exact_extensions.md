# Mixed shallow S3: exact extensions and the graded presentation

AI-produced research note, GPT-6 Astra (OpenAI, ChatGPT Pro mode), RESEARCH_SA17_FINISH/c1_mixed_s3. Created 2026-11-19 after19:03UTC. Uncompiled research; no main gate is claimed closed. The checkpoint10 source/bibliography freeze is respected.

## Exact graded algebra presentation

Over any commutative ring in which2 is invertible, the S3 group algebra has the presentation

    k<S,b> / (S²−1, Sb+bS, b³+3b),

where b=t−t² for a three-cycle t, and S is a transposition. The inverse formula is

    t=(b²+b+2)/2,   t²=(b²−b+2)/2.

Indeed b²=t+t²−2, hence b³=−3b. Conversely b⁴=−3b² gives the displayed square formula, and the product of those two expressions is1. Conjugation by S sends b to−b and therefore t to t². Thus the two presented algebras are inverse by the generator formulas; this does not merely identify their generic fibres.

A finite free S3 representation is therefore a Z/2-graded free k-module with an odd endomorphism b satisfying b³+3b=0. The two summands are the images of (1±S)/2, and are free when k is local. For k=A⋉J, A=Z3[zeta3], pi=zeta3−1, pi J=0, write b=b0+v. Then v is odd and the linear equation is

    b0²v+b0vb0+vb0²=0,

since3v=0 and J²=0. After removing regular cubic summands, the residual N=b0 modpi has N²=0 and the equation is NvN=0. This repackages the existing tangent problem; it does not prove additivity of its Swan class. Also

    1+t+t²=b²+3,   t−1=b(b+1)/2.

Here b+1 is a unit on every residual-nilpotent local block, so the cyclic Tate complex can be represented by b and b²+3 up to an invertible factor. Its odd/even S-parities must be retained if this is used for an invariant.

## Exact two-block extension

Let T0 be any constant cubic lattice, let U,V be J-valued tangent matrices, and put T=T0 modpi. For the block matrix

    E(U,V)=[[T0+U, I],[0,zeta*T0+V]],

the constant upper-right block of E³ is zero. Its first-order part is

    TU+2UT+2TV+VT = [T,U−V].

The diagonal blocks are cubic identities by the tangent hypotheses. Consequently E(U,V) is a cubic action if and only if [T,U−V]=0. This equivalence is literal in M_r(J), and hence valid for an arbitrary F3-vector space J, not just one-dimensional dual numbers.

If H is another J-valued matrix commuting with T, conjugation by the invertible shear [[I,0],[H,I]] gives

    E(U,V)  ~  [[T0+U+H,I],[0,zeta*T0+V−H]].

The lower-left block is zero because it is [T,H] and all quadratic J terms vanish. Both triangular descriptions are admissible free-block exact sequences. If d_L(W) denotes the relative cubic class at the fixed constant lattice and z is the constant zeta character, this gives

    d_L(U)+z*d_L(V)=d_L(U+H)+z*d_L(V−H),

provided [T,U−V]=0 and [T,H]=0.

For a fixed arbitrary U, define f_U(H)=d_L(U+H)−d_L(U) on commuting H. The same argument used in the compiled commuting theorem shows that f_U is additive and z fixes f_U(H). This is additivity of commuting TRANSLATIONS at one fixed noncommuting background. It does not identify f_U(H) with f_0(H), nor imply additivity between the two opposite noncommuting arrow spaces. No such inference is made here.

Taking V=U makes E(U,U) a valid cubic action for every tangent U. Its residual nilpotent matrix is [[N,I],[0,N]]. When N has a size-two block, this four-dimensional part has one size-three and one size-one block; a size-one block gives one size-two block. After splitting off regular cubic summands, the numbers of residual size-one and size-two blocks interchange. The regular summand can be removed using the previously proved coinduced splitting, but the operation alone is NOT a new cancellation theorem: E(U,U) is the tensor product of the given representation with the constant pair-gluing lattice L01 (after rescaling the upper block by its invertible cubic action). Thus this is the familiar stable syzygy relation, and treating it as independent additivity would be circular.

## Scope remaining

The opposite-signed rank-six L012 and Q mixtures still have both arrow directions. The existing2398-action curvature experiment has no detections, but this does not settle their Swan classes. The exact extension above explains which additional translations are legitimate and which are unproved. The next useful target is an admissible relation that changes the noncommuting arrow background, or an additive invariant sensitive to these mixed bands. There is no finite counterexample asserted in this note and no program certificate is claimed.
