# A.4: the strict binomial bridge and its obstruction

2026-11-19, GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.

## A-015. The coefficient associated graded (Proved)

Write Num(V) for the ring of integer-valued rational polynomials in a free
abelian module V of linear coordinate functions, filtered by ordinary total
polynomial degree. In a basis x_1,...,x_d it has the integral basis
product_j binom(x_j,a_j). The leading term of this basis element is
product_j x_j^{a_j}/a_j!. Consequently there is a canonical functorial
isomorphism of graded rings gr Num(V)=Gamma_Z(V). Indeed multiplication
has leading coefficient product_j binom(a_j+b_j,a_j), and integral linear
substitutions preserve the filtration and its identified leading symbol.
The basis assertion follows successively from the finite-difference
expansion f(x)=sum_a (Delta^a f)(0) product_j binom(x_j,a_j): if f takes
integer values, every finite difference coefficient is an integer.

For the simplicial module Phi of vertex coordinates the degree-zero
associated graded is therefore Gamma(Phi). On the affine numerical
simplex with sum x_i=1 it is instead Gamma(Psi), since elimination of
x_0=1-sum_{i>0}x_i leaves n free coordinates and its leading linear
relation is sum x_i=0. Neither coefficient calculation supplies a
compatible differential or multiplication on forms.

## A-016. No strict simplicial filtered DGA bridge (Proved)

There is no simplicial filtered unital differential graded Z-algebra B
with all the following properties, even if its product is not assumed
graded commutative:

1. B_n^0=Num(Z^{n+1}), with its degree filtration and its usual simplicial
   pullbacks on vertex coordinates; T=sum_i x_i.
2. The image of Num(ZT) is central in B and dT=0 (a relative DGA).
3. The nonnegative exhaustive multiplicative filtration has
   gr B=Gamma(Phi) tensor Lambda(Psi), including its simplicial maps,
   its weight grading, its product and its PD de Rham differential.
   In particular F_0 B^1=0 and F_1 B^1=Psi.

Proof. For linear functions f,g, d f lies in F_1 B^1. Commutativity of
the associated graded gives [df,g]=df g-g df in F_1 B^1. This expression
is Z-bilinear. Adding a constant or a multiple of T to f or g does not
change it, by dT=0 and centrality of T and of integers. Hence it defines
a simplicial bilinear map b:Psi tensor Psi -> Psi. The equality
d(fg)=d(gf) also makes b symmetric, though symmetry is not needed below.

Let beta_2(f)=binom(f,2) in F_2 B^0. Its leading differential is f df,
so h(f)=d beta_2(f)-f df lies in F_1 B^1. Differentiating the exact
identity 2 beta_2(f)=f^2-f gives

    2 h(f) = [df,f]-df = b(df,df)-df.

Thus after reduction modulo 2, b(u,u)=u for every linear u in Psi.

We prove directly that no such simplicial bilinear map exists. Identify
Psi_1 over F_2 with F_2 by the difference of its two vertex values. For
Psi_2 use successive differences (a,b). Its three face maps to Psi_1
are a, b and a+b. The diagonal requirement on Psi_1 forces
b_1(s,t)=st. Naturality for the first two face projections forces

    b_2((a,b),(c,d))=(ac,bd).

Naturality for the third would give ac+bd=(a+b)(c+d), which fails for
(a,b)=(1,0),(c,d)=(0,1). This contradiction proves the theorem. The
attached finite program enumerates every candidate bilinear b_2.

The obstruction already occurs in weights <=2 and simplex dimensions
<=2. It does not use commutativity of B in positive cochain degrees.
It also excludes the strictly commutative version immediately.

## Scope and the still-distinct formulations of L2

The lead does not specify a filtered model. A-016 refutes its natural
strict simplicial-DGA interpretation, under exactly the stated data.
It does not refute an arbitrary homotopy-coherent filtered E-infinity
model, a filtered diagram category with a different monoidal product,
or a model whose degree-zero terms are not the numerical polynomial
rings. Those are different statements and need separate formulations.
No existence claim for one of them is made here merely from gr Num=Gamma.

The one-variable finite-difference calculus explains the obstruction:
dx f(x)=f(x+1) dx and d binom(x,n)=binom(x,n-1) dx have the desired
associated graded, but the coordinate-wise calculus fails naturality
when a simplex degeneracy identifies two variables. The calculation in
the proof is the degree-two form of that failure. The ordinary derivative
also fails integrality, since d binom(x,2)=x dx-(1/2) dx.

We searched the primary literature around Horel's binomial cochains,
integer-valued polynomial de Rham complexes and numerical spaces.
Horel's actual construction is a cosimplicial binomial-ring construction;
it is not a strict simplicial relative DGA satisfying the three conditions
above. A precise literature comparison is being added separately.
