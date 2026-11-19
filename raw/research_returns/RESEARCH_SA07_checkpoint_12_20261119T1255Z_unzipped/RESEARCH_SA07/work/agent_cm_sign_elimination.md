# AI-7. Elimination of the local-sign ambiguity on the full CM diagram

Proved work result. The argument was proposed by root and independently
re-proved here, including the exact reflex-norm maps and the rank-one
linear algebra. It uses only two CM types of each explicitly specified
CM field. It does not assert that the remaining all-abelian lattice
criterion is satisfied by a nontrivial Galois element, or that an
abelian comparison extends to all pure motives.

## 1. Exact input and finite CM test objects

Let sigma belong to Gamma_Qcm, and suppose one common local sign
lambda in product_l {+1,-1} gives actual integral Betti comparisons

    T_A^hat = lambda rho_A(sigma)

on the geometric CM/Artin diagram, with labelled endomorphisms and
all the finite-model Artin blocks of E.2.3. This is the consequence
of E.2.18 for every candidate in Sigma.

Fix an integer m>=3, put F=Q(zeta_m+zeta_m^{-1}), and L=F(i).
The extension F/Q is totally real and Galois, L/Q is Galois and CM,
and complex conjugation c fixes exactly F.
Choose any CM type Phi of L containing the identity embedding.
Let Phi' replace the identity embedding by c, leaving every other
conjugate pair unchanged. Both are CM types, even when either is
imprimitive. The standard CM construction gives abelian varieties
A_Phi and A_Phi' over Qbar with labelled action of L and rational
Betti homology free of rank one over L. Full geometric endomorphism
algebra equal to L is not required.

For completeness, the complex torus
C^Phi/Phi(O_L) admits a Riemann form: choose a totally imaginary
element xi in L whose Phi-values have the signs required for
positivity, and multiply by an integer to make
Tr_L/Q(xi x c(y)) integral on O_L. Such xi exists by weak
approximation in the anti-invariant F-line of L. Milne Example2.11
constructs this polarizable CM torus, and the CM algebraicity
theorem supplies its Qbar model. Its homology is the displayed
rank-one O_L lattice. Every labelled endomorphism and every
isogeny used below is defined over some finite number field,
so E.2.3 supplies its actual selected Betti block.

## 2. One idele and the exact reflex-norm formula

Choose ONE finite L-idele s whose Artin image is sigma|L^ab.
This is possible because L is totally imaginary, its infinite
idele group is connected and has trivial Artin image, and the
global Artin map is onto.

For a CM type Psi of L, let E_Psi be its reflex field, contained
in L because L/Q is Galois. Put

    s_Psi = Norm_{L/E_Psi}(s).

Norm compatibility gives

    Art_{E_Psi}(s_Psi) = sigma|E_Psi^ab.

Indeed E_Psi^ab L is abelian over L and is contained in L^ab;
this is the precise restriction diagram used here.
Milne CM2020 Proposition1.23, printedp16, identifies the composite
reflex norm as

    N_{L,Psi} = N_Psi o Norm_{L/E_Psi}.

Proposition1.26, printedp17, with k=E=L, gives

    N_{L,Psi}(s) = product_{psi in Psi} psi^{-1}(s).

There is NO extra stabilizer factor: this is the composite from
L, with the norm to the possibly smaller reflex field already
included. The identity holds for finite ideles by the morphism
of algebraic tori in Remark1.25, not only for principal ideals.

Theorem9.10, printedp78, gives an L-linear quasi-isogeny
alpha_Psi:A_Psi -> sigma A_Psi satisfying

    alpha_Psi(N_{L,Psi}(s)x) = sigma x

on rational finite Tate modules. Therefore

    alpha_Psi^hat = rho_A(sigma) N_{L,Psi}(s)^{-1}.

The actual Betti comparison T_A is L-linear relative to the
labelled actions on A and sigma A: the Artin-block naturality
equation is T_A iota(a)=(sigma iota(a))T_A for every a in L.
The same is true of alpha_Psi. Hence

    beta_Psi = alpha_Psi^{-1} T_A

is an L-linear endomorphism of the rank-one L-vector space
H_1(A,Q), and is multiplication by a unique b_Psi in L^times.
This is valid for imprimitive types as well; the centralizer of
the labelled rank-one L-action in End_Q(H_1) is exactly L.
After completion,

    b_Psi = lambda N_{L,Psi}(s) in A_f,L^times.             (1)

No Hodge-filtration preservation of the original comparison
has been used.

## 3. Two types force an F-idele

Apply (1) to Phi and Phi'. Their quotient is

    r = s/c(s) in L^times.

The equation r c(r)=1 holds as an exact equality in L.
It admits an explicit Hilbert-90 solution:

    b=1+r if r != -1, and b=i if r=-1.

In either case b/c(b)=r. Consequently

    t=s/b

is fixed by c, so t lies in A_f,F^times. This invariant-idele
identity follows place by place from
(L tensor_Q Q_l)^{<c>}=F tensor_Q Q_l.

Every CM type Psi contains one extension of each embedding of F.
Since t is F-idelic, its composite type norm is thus

    N_{L,Psi}(t)=Norm_{F/Q}(t).

Dividing (1) by the principal element N_{L,Psi}(b) shows

    lambda Norm_{F/Q}(t) in L^times.

The left side is a scalar rational finite idele. A diagonal
element of L that is scalar in L tensor_Q A_f is fixed by
Gal(L/Q), and hence is in Q. Therefore, for some a in Q^times,

    Norm_{F/Q}(t)=a lambda.                              (2)

The reciprocal placement of a is immaterial; (2) fixes the
notation used in the final Artin calculation.

## 4. Real cyclotomic reciprocity forces one global sign

Apply the rational finite-idele Artin map to (2).
Norm compatibility says its left side acts trivially on F:
the restriction is the action of Art_F(t) on the base field F,
which is the identity.

The finite principal idele a has infinite component 1.
After inserting its missing diagonal infinite component, global
reciprocity identifies its action on Qab with the action of
the inverse infinite component. Over Q this is either the
identity or actual complex conjugation, according to the sign
of a. Both act trivially on the totally real field F.
It follows that Art_Q(lambda) fixes F.

Since F=Q(zeta_m+zeta_m^{-1}), the cyclotomic description gives

    lambda modulo m belongs to {+1,-1}.

This holds for EVERY m. Equivalently, Art_Q(lambda) fixes the
union Qab,+ of all real cyclotomic fields. The exact Galois
quotient Gal(Qab/Qab,+) has two elements, identity and actual
complex conjugation. Under cyclotomic reciprocity they are the
two GLOBAL units +1 and -1 in Zhat^times. Thus lambda is one
global sign. The local-sign class delta is trivial.

The conclusion also follows directly by combining moduli:
the signs at any two distinct odd primes must agree modulo
their product, while a modulus divisible by 4 and an odd prime
forces the 2-adic sign to agree with them.

## 5. Explicit finite obstruction to the AI-6 sign

For lambda_5=-1 and lambda_l=+1 at every other prime, use m=15.
Its residue is 4 modulo15, which is neither 1 nor -1 modulo15.
Thus it acts nontrivially on the totally real cyclic quartic
field

    F_15=Q(zeta_15+zeta_15^{-1}).

Put L_15=F_15(i), a CM field of degree8. Two CM types of L_15
differing only at the identity/conjugate pair already give
the contradiction above. Their abelian varieties have dimension4.
The finite Artin diagram includes a common finite field of
definition, the labelled O_L basis endomorphisms, and the
required selected-block module maps. Therefore this is an
actual finite CM obstruction to extending AI-6's specified
comparison to these two additional CM objects.

This does not require the type of Q(zeta_5) to detect the sign.
For that cyclic quartic field, the direct local type-norm
equation alone is insufficient: with epsilon=(1+sqrt5)/2,
Norm_{Q(sqrt5)/Q}(epsilon)=-1, so a scalar local -1 is in
the type-norm image. The joint all-type/global Artin argument
supplies the additional constraint used above.

## 6. Exact consequence for the all-abelian criterion

In E.2.18 the scalar lambda can be replaced by one global sign,
which preserves every lattice. Hence the proved criterion is

    Sigma={sigma in Gamma_Qcm :
      rho_A(sigma)(Lambda_A)=Lambda_{sigma A}
      for every abelian variety A/Qbar},
    I_ab=Sigma disjoint-union c Sigma.

The two lifts differ by the global weight sign, as already
proved in E.2.15. This removes the local-sign variable from
the exact all-candidate criterion. It does not decide whether
Sigma contains a nonidentity element, whether the quartic
place-pair is related by one, or whether an abelian comparison
extends to the full pure diagram.

## 7. Checks and exact sources

2026-11-19: independent re-proof by period_generation of
root's argument. Read local primary Milne CM2020
Propositions1.23 and1.26, pp16-17, Remark1.25 p17, and
Example1.28 p18 to verify the inverse-embedding convention
and absence of an unaccounted stabilizer factor.
The exact normalization of Theorem9.10 p78 was rechecked
for AI-6. The global Artin norm map is Milne CFT2020
PropositionV.5.2 and the diagram after its proof, p178,
with reciprocity TheoremV.5.3 pp178-179.
No hypothetical theorem or unverified categorical extension
is used.

## 8. Fully specified additional dimension-four object

Take t=2cos(2pi/15), the largest root of X^4-X^3-4X^2+4X+1,
L=Q(t,i), and lattice O_L. Let Phi0 contain all embeddings fixing i,
and flip only its identity/conjugate pair to obtain Phi1. The Phi0
torus is isogenous to the fourth power of the Gaussian elliptic curve,
by a Q(i)-basis of L and commensurability with Z[i]^4. Thus it
already lies in the fixed-Gaussian category. The one additional
object is C^Phi1/Phi1(O_L), with integral Riemann form
Tr_L/Q(i(3-2t)x c(y)). Exact rational root intervals are
(-2,-19/10),(-1/4,-1/5),(13/10,7/5),(9/5,19/10). The quantity
3-2t is negative only at identity, whose i-sign is flipped. Every
Phi1-value of xi=i(3-2t) therefore has positive imaginary part.
Milne Example2.9 pp25-26 explicitly uses this sign for
psi(x,Jx)>0; xi is integral, so the trace is integral. The exact
root-isolation and C4xC2 trivial-stabilizer calculations passed
in verify_numberfield_descent.py. No simplicity claim is needed.
