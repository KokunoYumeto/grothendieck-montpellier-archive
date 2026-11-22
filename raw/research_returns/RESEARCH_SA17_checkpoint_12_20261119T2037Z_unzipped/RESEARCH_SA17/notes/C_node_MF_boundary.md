# Ramified node: exact boundaries for two proposed routes

AI-produced research note, GPT-6 Astra Pro (OpenAI), RESEARCH_SA17 / c1_mixed_s3, 2026-11-19. This is an uncompiled research note. It does not establish a nonzero Swan class or a new positive coefficient family. The checkpoint11 source freeze is respected.

## The displayed rank-two C4 action does not extend directly to D8

Let A be the complete dyadic DVR with uniformizer pi and pi^2=2, and let R=A[[x,y]]/(xy-pi^3). Put a=1+pi. The matrix

    T = [[a,x],[-a*y,-a]]

satisfies T^2=-I: a^2-a*pi^3=-1. There is no invertible R-linear F with FT=-TF. In particular this particular rank-two C4 representation cannot be extended to D8 by an involution that inverts its C4 generator. The same argument excludes a direct Q8 extension.

Indeed, write F=[[u,v],[w,z]]. The upper-right anticommutator entry is x(u+z). Since R is a domain, z=-u. Its diagonal equation is

    2*a*u + x*w - a*y*v = 0.

Modulo (x,y), this gives pi^2*a*u=0 in A/(pi^3), so u lies in the maximal ideal m=(pi,x,y). Modulo m^2 the remaining equation becomes x*wbar-y*vbar=0. The classes of x and y are linearly independent in m/m^2, hence v,w also lie in m. Thus every entry of F lies in m, and F is not invertible.

This says nothing about the class induced from C4 to D8 or S4, or about higher-rank extensions.

## The ungraded Tate-cokernel construction is not a retraction from Swan classes to matrix-factorization classes

Let S0 be a ring, g a non-zero-divisor, and let Phi,Psi be square matrices over S0 with Phi*Psi=Psi*Phi=g*I. Put R=S0/(g), and reduce both matrices to R. Then their two-periodic complex is exact: ker Phi=im Psi and ker Psi=im Phi. On the free R-module of twice the rank, the matrix

    T = [[I,Phi],[Psi,-I]]

is an involution. Its standard lift has (Ttilde^2-I)/g=I, so selecting the invertible-curvature part does not remove either block.

There is a canonical short exact sequence of R-modules

    0 -> coker Psi -> coker(T-I) -> coker Phi -> 0.

The right map is projection onto the first coordinate modulo im Phi. The left map sends the class of b to the class of (0,b). For injectivity, a relation (0,b)=(Phi*v,Psi*u-2*v) forces v=Psi*w, and hence b=Psi*(u-2*w). Surjectivity onto the kernel follows by subtracting (T-I)(0,v) whenever the first coordinate is Phi*v.

The two matrix-factorization cokernels differ by a suspension in the singularity category. Therefore their K0 classes sum to zero, and

    [coker(T-I)] = 0 in K0(Dsg(R)).

Consequently a proposed retraction that remembers only this ungraded Tate cokernel, even after selecting the invertible-curvature part, vanishes on the entire displayed matrix-factorization image. A successful retraction would have to retain additional structure.

This boundary does not say that the forward matrix-factorization-to-Swan map is zero. The already compiled cubic-nil construction with Phi=epsilon and Psi=epsilon^2 gives nonzero order-three examples in its separate coefficient setting. Nor does the argument prove that the forward map is well-defined on every asserted triangulated quotient; that step is being checked independently.

## Derivatives for explicit ramified matrices

The operation d/dpi is not a derivation of A=Z_2[pi]/(pi^2-2). For a concrete matrix identity whose entries are polynomials in an independent symbol pi, it is legitimate to differentiate that polynomial identity first and then specialize pi^2=2. This does not justify differentiating arbitrary A-valued matrix factorizations: a chosen lift may have an extra multiple of pi^2-2, whose derivative survives specialization. The current explicit rank-four anticommuter calculation uses the legitimate polynomial-identity order.

No finite counterexample or computational proof is claimed in this note. All displayed statements follow from the elementary identities and exact-sequence argument written here.
