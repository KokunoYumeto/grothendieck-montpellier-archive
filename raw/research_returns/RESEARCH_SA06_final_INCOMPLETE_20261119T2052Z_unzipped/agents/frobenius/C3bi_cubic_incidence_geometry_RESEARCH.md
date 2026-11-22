# Explicit smooth incidence input for the proposed C.3bi

AI-produced by GPT-6 Astra (OpenAI), ChatGPT Pro mode, run RESEARCH_SA06, agent `/root/frobenius`, 19 November 2026. This note proves the geometric input and the indicated cup-rank statement. It does **not** prove that the relative class survives in the absolute Chow group; that separate step belongs to the C.3bi draft.

## 1. Completely specified coefficients

We work over an algebraic closure of F5. Let lambda be a root of

`lambda^3+lambda+1=0`.

This cubic takes the nonzero values 1,3,1,1,4 at 0,1,2,3,4, so it is irreducible. Thus lambda belongs to F125 and not to F5. Direct reduction gives

`lambda^12=2-lambda`.

In particular lambda is nonzero and lambda^12 is none of 1,3,4.

Let W be the Fermat cubic `w0^3+w1^3+w2^3+w3^3=0`, let D be its line `w0+w1=w2+w3=0`, and let C be the Fermat quartic `z0^4+z1^4+z2^4=0`. Put A=O_W(1), S=W×C, and B=A box K_C. Define

`a0=z0*w0+z1*w1`,

`a1=z0*w2+lambda*z2*w3`.

These are actual sections of B over F125. On P1_x×S put

`ell=x0*a0+x1*a1`.

## 2. The complete base curve is smooth

For every point of C, the two rows

`(z0,z1,0,0)` and `(0,0,z0,lambda*z2)`

are nonzero and independent. Indeed z0=z1=0 or z0=z2=0 would give a coordinate point not on the Fermat quartic. Each row defines a base-point-free canonical pencil. Its kernel in O_C^2 is K_C^(-1), so their common projective kernel is canonically a P1-bundle isomorphic to C×P1. A homogeneous parametrization is

`(w0,w1,w2,w3)=(z1*s,-z0*s,lambda*z2*t,-z0*t)`.

This is a fibrewise projective linear isomorphism onto the common kernel. The remaining Fermat cubic equation is

`A0*s^3+B0*t^3=0`,

where A0=z1^3-z0^3 and B0=lambda^3*z2^3-z0^3 are sections of K_C^3.

The divisor of A0 consists of twelve distinct points. At an A0-zero we have z0 nonzero, and z1/z0=zeta with zeta^3=1. The remaining equation is `(z2/z0)^4=-(1+zeta)`. Its right side is nonzero: zeta=-1 is not a cube root of 1 in characteristic five. Thus the three distinct lines each meet C in four transverse points.

For B0 the same argument uses z2/z0=xi/lambda, xi^3=1. The remaining fourth-power equation has nonzero right side unless `1+lambda^(-4)*xi=0`. Cubing this equality would give lambda^12=-1=4, which was excluded. Hence the twelve B0-zeros are also distinct.

The two zero divisors are disjoint. If they met, set zeta=z1/z0 and xi=lambda*z2/z0. Then zeta^3=xi^3=1 and

`1+zeta+rho*xi=0`, where rho=lambda^(-4).

If zeta=1 this gives rho^3=2. For either primitive cube root, `1+zeta=-zeta^2`, hence rho^3=1. Equivalently lambda^12 is 3 or 1, both excluded. An exact resultant check is

`Res_y(y^3-1,(1+y)^3+r)=(r-2)*(r-1)^2` over F5.

It follows that the base scheme Z0=V(a0,a1) in S is smooth. On C×P1, away from the two branch divisors the derivative of A0*s^3+B0*t^3 in a fibre coordinate is nonzero (3 is invertible, and s,t are both nonzero). Above an A0-zero, s is nonzero and the derivative in the base direction is s^3*dA0, which is nonzero by transversality. The B0 case is identical. This verifies smoothness at every geometric point, with no finite-point inference.

The map Z0→C is finite of degree three. Since A0/B0 has a valuation equal to one at each A0-zero, it is not a cube in the function field of C. The degree-three Kummer equation is consequently irreducible over that field, so Z0 is geometrically connected. Connectedness is not needed for the incidence smoothness argument, but is available.

In particular Z0 is a smooth codimension-two complete intersection in the smooth threefold S; da0,da1 are independent along Z0.

## 3. The incidence divisor and its contraction

The divisor H0=V(ell) in V=P1×W×C is smooth. Off the base Z0, its projection to S is locally an isomorphism. At a point above Z0 its differential along S is x0*da0+x1*da1, which cannot vanish because the two differentials are independent and (x0,x1) is nonzero. This also identifies H0 with the blow-up of S along the two-generated regular ideal (a0,a1), although that identification is not required for the differential proof.

Let H=z0^2*z1^2+z0^2*z2^2+z1^2*z2^2, the quartic deformation already used and checked in C.3bf. On the total space of O_{P1×W×P2}(-1,-1,-1), with tautological fibre coordinate tau, take

`F_C+tau*ell*H=0`,  `f=tau*ell`.

The zero section is V, with conormal L=O_P1(1) box A box K_C. Its smoothness follows from the smoothness of C, independently of the deformation coefficient. The projection to W is retained, so the divisor D pulls back to an actual Cartier divisor on this resolution.

For completeness the contraction can be given by the twenty-four Segre coordinates

`v_(a,i,j)=tau*x_a*w_i*z_j` (a=0,1; i=0,...,3; j=0,1,2).

The function f is the explicit linear form

`v_(0,0,0)+v_(0,1,1)+v_(1,2,0)+lambda*v_(1,3,2)`.

Take the reduced affine image cut out by rank-one tensor relations, the cubic Fermat row equations in the w-index, and the deformed quartic row equations

`F_C(v_(a,i,0),v_(a,i,1),v_(a,i,2)) + f*H(v_(a,i,0),v_(a,i,1),v_(a,i,2))=0`.

At every nonzero tensor, choosing a nonzero row recovers the equation of the total-space model; the tensor factorization is unique in the product of projective spaces. The graph-closure and normalization argument of C.3bf therefore applies unchanged. Normalize the reduced image, localize at its vertex and strictly henselize. The model is integral because F_C is irreducible and does not divide ell*H. It is regular near the entire proper exceptional fibre V; after shrinking at the vertex its puncture is regular. The pullback of the vertex ideal is I_V because the Segre sections generate L, so some coordinate divided by tau is a unit at every point of V.

On this model f=0 is the union of V and the strict transform Q, where Q is the split total line bundle over the smooth H0. The two divisors meet transversely along H0. Thus the punctured principal divisor is regular as well. The local ring has dimension five, since V has dimension four. These are the exact geometric properties required for the proposed r=2,N=5 example.

## 4. Rank of the relevant coefficients and line cup

Writing ell as sum_j g_j*z_j gives

`g0=x0*w0+x1*w2`, `g1=x0*w1`, `g2=lambda*x1*w3`.

They are independent in H0(P1,O(1)) tensor H0(W,A): the coefficient minor on the monomials x0*w0,x0*w1,x1*w3 has determinant lambda.

Write the coordinates on D as w0=-s,w1=s,w2=-t,w3=t. Then

`g0|D=-x0*s-x1*t`, `g1|D=x0*s`, `g2|D=lambda*x1*t`.

The independently audited cubic-line calculation in `notes/ROOT_CUBIC_SURFACE_LINE_CUP_RESEARCH.md` identifies the Serre-dual pairing of mu_D(a)=a*c1(O_W(D)) with the nonzero functional taking st to a nonzero scalar and killing s^2,t^2. Thus mu_D(s),mu_D(t) are independent. The image of the span of g0,g1,g2 under id tensor mu_D has rank exactly two, and is in particular nonzero.

The C.3bf quartic deformation has a nondegenerate cup form (the retained exact residue computation gives a common nonzero multiple of -I3). Hence its Picard-extension vector image is exactly U=span(g0,g1,g2). The finite Verschiebung kernel image spans U over k. It cannot lie entirely in the kernel of id tensor mu_D, so some actual finite p-torsion image has nonzero indicated cup. This is only a first-order nonvanishing statement; it makes no assertion about the subsequent K1 boundary or Chow detection.

## 5. Reproduction and scope of computation

`code/check_cubic_incidence_geometry.py` verifies the field polynomial, lambda^12=2-lambda, all three excluded branch values, the exact resultant, the global kernel parametrization, the restricted cubic equation, the coefficient determinant and the rank-two restriction. Its JSON and full text output are retained at `output/C3bi_cubic_incidence_geometry.json` and `.out`. The all-geometric-point proof is in Sections2–3 above; the program is a finite algebra certificate for its identities.

An earlier, unused trial pair with consecutive shifted w-coefficients was tested by four affine Jacobian ideals. Its first chart reduced to the unit ideal in76.761647651seconds, but the run was interrupted before the other charts completed. No smoothness claim or certificate is based on that incomplete trial. Its script is retained as `code/test_cubic_incidence_pair.py` for transparency.

No new literature theorem or originality claim is introduced. The contraction, ordinary quartic, actual Picard-family and first-order deformation inputs are precisely the previously opened and audited C.3bf/bg sources. This auxiliary note has not been promoted to a separately numbered statement.
