# Focused A.1 proof checks by the A.2/A.4 agent

GPT-6 Astra (OpenAI), inherited effort, run /root/a2_a4, 2026-11-19.

## A1.6 scalar-twist model

Read the transcription of scans75–84 and checked the root agent's proposed model with FinVect(F3), standard exponential divided powers, t2=-1 and tn=1 for n!=2, and c_{p,q}=t_{pq}/(t_p t_q^p). The cocycle associativity identity is formal by cancellation. Unit cases p=0,1 or q=0,1 must be included explicitly; in particular c_{p,0}=1/t_p is an isomorphism, and c_{0,q}=c_{1,q}=c_{q,1}=1.

The mixed-unit contradiction is sound when the asserted equivalence preserves the given exponential comparison isomorphisms and monoidal unit constraints. Let U=F3, let e0:0→U be the constant corresponding to1, and let m:U×U→U be represented by the standard weight-(1,1) projection Γ²(U⊕U)→U⊗U≅U. The strict mixed representability with degrees(0,1) supplies m(e0,id)=the inverse of the fixed standard unitor=id. Associativity and the cartesian product then imply m(e0,e0)=e0. The homogeneous formula using α'_{2,0}=-1 instead gives -e0. These differ in F3. The t_n transformation cannot absorb the defect while preserving the exponential comparison, because exponential-monoidality would require t2=t1², which fails. This does not claim that changing or forgetting the supplied exponential/unit structures is harmless.

## A1.8 inflated divided-power model

The root's category is finite nonnegative internally graded F2-vector spaces. T removes internal degree0. Define E^nX=direct_sum_{a+3b=n} D^aX tensor D^b(TX), using external weight3 on the second factor. E0=1, E1=Id, E^n1=1. Exponentiality follows from additivity of T and standard exponentiality of D. The inclusion i:D→E and projection pi:E→D are natural monoidal transformations with pi i=id.

For p,q≥2, α^E_{p,q}=i_p D^p(i_q) α^D_{p,q} pi_{pq}. The two triple composites for p,q,r≥2 agree: cancellation of pi_{pq}i_{pq} on one route and pi_{qr}i_{qr} on the other reduces both, by naturality of i and α^D, to the same D triple-composition followed by i_p D^p(i_q) D^pD^q(i_r). Cases involving0 or1 reduce to the separately specified identities and E^n1=1.

If V is placed in internal degree1, E3(V)=D3(V) in internal degree3 direct_sum V in internal degree1. A coherent natural homogeneous cubic strict polynomial law enriching E3 therefore induces one enriching the identity functor on the degree1 block. On one-dimensional Hom this must be t↦t³, since it takes1 to1. Coordinate projections force the law on a two-component column to be (x,y)↦(x³,y³). Naturality under the addition map F2²→F2 then forces (x+y)³=x³+y³ as polynomial laws. This is false in F2[x,y], whose two mixed monomials have coefficient1; it also fails at x=1,y=omega in F4, where omega²+omega+1=0.

Scope caveat: this rules out a **coherent natural enrichment**. A separately chosen map on an individual Hom module can be lifted pointwise by coordinatewise cubing in a chosen basis, so the claim must not be stated as nonexistence of every nonnatural per-pair polynomial law.
