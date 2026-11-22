# Independent root derivation of the eight-support repair

This is a proof-audit note for the forthcoming Fermat-divisibility classification. It is not itself a promoted monodromy theorem. It replaces the unsuccessful attempt to locate four simple opposite-pair binomial coefficients in the monic remainder: all four such locator lists in the earlier exploratory output are empty.

Write the points of F3² in lexicographic order, and put z_i=c_i³. The necessary affine-line conditions select one zero-sum z-line in each of the four directions. The 81 choices have a concurrent orbit and a triple-plus-one orbit. The necessary coefficient of x_0⋯x_8 is (Σz_i)³, hence Σz_i=0. The three parallel-line product sums used below are also necessary, through their cubes as exact determinant coefficients. Their coefficient identities must be independently verified in the final certificate.

If the four selected lines are concurrent at h, their four equations imply Σz_i=z_h. For eight-support c the unique zero must therefore be h. The line through h in each direction then gives z_(h+v)=z_(h−v), which is the desired four opposite-cube equalities.

For the nonconcurrent orbit choose the lines x=0, y=0, x+y=0, and x+2y=1. Their unique triple point is 0. The three double points have indices2,3,7; the three single points have indices1,5,6; the two uncovered points have indices4,8. The stabilizer acts transitively on each of these classes; this finite affine action is to be checked by the final certificate.

If the unique zero is the triple point, the three lines through it already give three opposite-cube equalities. The total cube sum gives the fourth. If the zero is an uncovered point, the total cube sum, after the line equations, is z_4+z_8, so both uncovered coordinates vanish, contradicting eight-support.

In the remaining cases the triple coordinate is nonzero. Scale it to1. The same equations give

    (z_0,…,z_8)=(1,A,1+A,B,D,A+B,1+B,1+A+B,D).

Since c_4³=c_8³ and neither coordinate is zero, character multiplication c_v↦ζ^{ell(v)}c_v can make c_4=c_8=d. It leaves every affine-line product sum unchanged because the sum of a linear functional on a three-point affine line is0 in F3. Thus write

    c=(1,a,u,b,d,v,w,t,d),
    A=a³, U=u³=1+A, B=b³, D=d³,
    V=v³=A+B, W=w³=1+B, T=t³=1+A+B.

The relevant product equations are

    au+d(bv+wt)=0,
    bw+d(at+uv)=0,
    vt+d(ab+uw)=0.

For a single zero it suffices, by the stabilizer, to take a=0. The first equation gives bv=wt. Cubing yields B²=(1+B)² and therefore1=0, a contradiction.

For a double zero it suffices to take u=0. Then A=1, T=B, and V=W=1+B. The second equation gives bw=dat. Cubing and dividing by the nonzero B yields D=W. Consequently the cube coordinates agree in the four pairs reflected about index2:

    (0,1), (3,7), (4,6), (5,8).

This proves the opposite-cube conclusion for eight-support in every affine-line configuration, provided the stated necessary determinant coefficients and the finite orbit split have been verified. The earlier symbolic phase test can then be applied: after opposite-pair normalization, all cube-root ratios lie in μ3; its nine character patterns give identically zero determinant, and its72 other patterns have an actual nonzero monomial remainder coefficient. No finite-field sampling is used to infer a statement over an algebraic closure.

For comparison, on full support the same normal form yields, with K=d²abuvwt,

    (D+A)U=K, (D+W)B=K, (D+V)T=K.

The identities BV+WT=U, AT+UV=B, AB+UW=T give these equations by cubing the three product sums. Adding the first two left sides gives the third, whereas K+K=0 in characteristic two. Thus K=0, contradicting full support. This is independent of the eight-support repair.
