# B.7: convolution divided powers, classification, and nonuniqueness

GPT-6 Astra (OpenAI, ChatGPT Pro mode), SA08 run, 19 November 2026.
No priority is claimed. The nonprimitive obstruction below is the example of
the attached Pro notes N43, independently checked and made finite by changing
the base from Z to Z/4. The primitive nonuniqueness calculation was derived in
this run; literature searches are recorded separately.

## D.7. An explicit intrinsic parameter space (Proved)

Fix a commutative ring k and a counital cocommutative k-coalgebra
(A,Delta,epsilon), with no flatness assumption. We classify **natural** divided
power structures on the convolution ideals

    Hom_k(A,J) subset Hom_k(A,B)

for all divided power k-algebras (B,J,gamma), natural for morphisms of divided
power k-algebras. The multiplication on Hom is (f*g)=mu_B(f tensor g)Delta.
This formulation specifies the naturality implicit in cote 136, scans 324--335.

The following maps are fixed, computable from the module A; they are not
additional structure to choose.

* delta_{r,s}:Gamma^{r+s}A -> Gamma^r A tensor Gamma^s A is the (r,s)
  component of Gamma(diag:A->A direct-sum A).
* rho_{m,n}:Gamma^m(Gamma^n A)->Gamma^{mn}A is induced by taking the m-th
  divided power in the free divided power algebra Gamma(A).
* c_{m,n}=(mn)!/(m!(n!)^m).
* chi_n:Gamma^n(A tensor A)->Sym^n A tensor Gamma^n A is obtained by the
  universal n-th divided power of the linear map
  a tensor b |-> a tensor gamma_1(b) in Sym(A) tensor Gamma(A).
  This tensor algebra is the free divided power Sym(A)-algebra on
  Sym(A) tensor A, so the definition works without flatness. Its (n,n)
  homogeneous component is the stated target.
* pi_n:A^{tensor n}->Sym^n A is the ordinary symmetric quotient.

Define P(A) to be the subset of

    product_{n>=0} Hom_k(A,Gamma^n A)

whose points u=(u_n) satisfy the following explicit equations of k-linear maps:

    u_0=epsilon,                     u_1=id_A;                      (U)
    delta_{r,s}u_{r+s}=(u_r tensor u_s)Delta,                       (A)
    chi_n Gamma^n(Delta)u_n
       = (pi_n tensor u_n) Delta^{(n+1)},                          (S)
    rho_{m,n} Gamma^m(u_n)u_m = c_{m,n}u_{mn}.                     (I)

Here r,s>=0 and m,n>=1; Delta^{(n+1)}:A->A^{tensor n} tensor A.
Every map, equation and parameter involves only A and its given coalgebra
structure. This is an intrinsic equation presentation, including all torsion;
it is not a criterion involving an unspecified target divided power algebra.

There is a bijection between P(A) and the natural convolution divided power
structures above. For a point u, the complete formula is

    gamma_n^A(f) = gamma_{J,n} Gamma^n(f) u_n,     f:A->J, n>=1,

where gamma_{J,n}:Gamma^n J->J is the linear map representing the n-th
divided power of J. The coalgebras in the requested class are exactly those
for which this explicitly presented parameter set is nonempty; the entire
indeterminacy is P(A). A stronger version of the manuscript, requiring
compatibility before applying rho, is the subset cut out by

    Gamma^m(u_n)u_m = sigma_{m,n}u_{mn},                            (I+)

where sigma_{m,n}:Gamma^{mn}A->Gamma^m(Gamma^n A) represents the polynomial
law a |-> gamma_m(gamma_n(a)). Since rho_{m,n}sigma_{m,n}=c_{m,n}, (I+)
implies (I). The two meanings must not be silently equated.

Proof of completeness. The functor (B,J)->Hom_k(A,J) is represented, in
divided power k-algebras, by the free algebra Gamma(A). Therefore any
natural operation gamma_n^A is determined by its value on the universal map
A->Gamma^1 A. This value is a linear map A->Gamma^+(A). The scalar axiom
applied after extending to k[z] gives homogeneity of weight n: compare
coefficients of z in the identity gamma_n^A(zf)=z^n gamma_n^A(f). Hence the
value factors through Gamma^n A and is exactly a parameter u_n as above.
Evaluation under the unique free divided power map Gamma(A)->B gives the
displayed formula; this proves both necessity of the parameterization and
uniqueness of the operation associated with u.

For the sum axiom use the universal pair A->Gamma(A direct-sum A). Under
Gamma(A direct-sum A)=Gamma(A) tensor Gamma(A), the component of bidegree
(r,s) is exactly (A). Thus (A) is necessary and sufficient for the sum axiom.
For the scalar axiom use the universal pair of maps A->Sym(A) and
A->Gamma^1(A) inside Sym(A) tensor Gamma(A). Their convolution is induced
by Delta; its n-th divided power is the left side of (S). The n-th ordinary
convolution power of the first map, multiplied by the n-th new divided
power of the second, is the right side. The universal algebra maps to every
pair f:A->B, g:A->J, proving necessity and sufficiency of (S).

The product identity follows from (A): compose with multiplication
Gamma^r A tensor Gamma^s A->Gamma^{r+s} A and use

    mu delta_{r,s}=binom(r+s,r) id.

This last formula is checked on divided-power monomials by the binomial
identity summing over all choices of r factors; it holds over Z and hence
over every base ring. Finally the iterated divided power axiom, evaluated
at the universal map A->Gamma^1 A, is precisely (I). Thus all divided power
axioms, including the unit and identity conditions (U), hold iff the listed
equations hold. They remain valid under every evaluation to (B,J), which
also proves naturality. This proves the classification.

This equation presentation deliberately records every compatibility. The
two equations written in scan 324 alone do not define P(A); D.10 gives an
explicit counterexample to that assertion.

## D.8. Flat coalgebras: existence and uniqueness (Proved)

If A is flat as a k-module, the parameter set P(A) has exactly one element.
It lies in the stronger subset (I+). Let

    theta_n:Gamma^n A -> (A^{tensor n})^{S_n}

be the canonical map, gamma_n(a)|->a^{tensor n}. For flat A it is an
isomorphism. Define u_n=theta_n^{-1}Delta^{(n)}, with u_0=epsilon.

For completeness, the flat comparison follows directly from finite free
modules. On a basis, divided-power monomials map to orbit sums, which are a
basis of the invariant tensors. Every flat module is a filtered colimit of
finite free modules; Gamma^n, tensor powers and invariants of the finite
group S_n commute with such colimits (the invariants are a finite kernel
diagram, and filtered colimits of modules are exact). Thus the comparison
is an isomorphism for flat modules. This is also the standard comparison
in Roby and SGA 4 XVII 5.5.2.5; Lundkvist (2008), Proposition 2.2,
was opened and confirms the comparison. An opened primary-paper reference is recorded
in the bibliography rather than assigning priority to this proof.

Coassociativity and cocommutativity imply that Delta^{(n)} is invariant.
Under the tensor-invariant identification, (A) says that an iterated
coproduct is unchanged when its factors are grouped into two blocks; (S)
says the same after selecting one factor from each of n pairs; and (I+)
says it after grouping mn factors into m blocks of n. Each is exactly
coassociativity and cocommutativity. These checks can be made after the
injective inclusion in A^{tensor(r+s)}, A^{tensor2n}, or A^{tensor mn},
respectively. The intermediate Gamma^n A is flat by the same filtered-free
argument, so the corresponding iterated comparisons are injective.
Thus u is a point of P(A), and its formula gives the claimed PD structure.

For uniqueness, iterate equation (A), taking n blocks of size one. The
result is

    theta_n u_n = Delta^{(n)}.

Since theta_n is injective for flat A, u_n is forced. This proves uniqueness
for the full natural structure, rather than for an incomplete list of
relations.

## D.9. Nonflat obstruction, fully finite (Refuted / corrected)

Let k=Z/4, A=k*1 direct-sum (k/2)*e, epsilon(1)=1, epsilon(e)=0, and

    Delta(1)=1 tensor1,
    Delta(e)=e tensor1+1 tensor e+e tensor e.

The module is not flat: tensoring 0->(2)->k with k/2 destroys injectivity.
The formulas respect 2e=0. They are cocommutative and counital, and are
coassociative because g=1+e satisfies Delta(g)=g tensor g.

Let B=k direct-sum (Z/2)t direct-sum (Z/4)u with t^2=2u, tu=u^2=0.
The ideal J=(t,u) is divided power with gamma_2(at+bu)=a^2u and gamma_n=0
for n>=3. The expression is well defined when a is taken modulo2, since
(a+2)^2-a^2 is divisible by4. The sum axiom is the identity
(a+c)^2-a^2-c^2=2ac; the scalar axiom is immediate from the multiplication;
all higher products and iterations are zero because Ju=0. In particular
x^2=2gamma_2(x). Thus this is a genuine PD ideal over the finite ring k.

Define f:A->J by f(1)=0,f(e)=t. Then convolution gives

    (f*f)(e)=t^2=2u !=0.

But every k-linear v:A->B has 2v(e)=v(2e)=0. Therefore f*f=2gamma_2(f) is
impossible for **any** prospective PD structure on Hom(A,J). This refutes
unrestricted existence, not merely a proposed formula.

The entire example is finite: |k|=4, |A|=8, |B|=32, |J|=8. The program
`code/D_finite_pd_checks.py` exhaustively checks the ring axioms, PD axioms,
coalgebra formulas and this obstruction. Its JSON output records counts
and elapsed time. Indices >=3 vanish identically, so checking through6
is supplemented by the preceding proof for all indices.

## D.10. The two written relations do not imply uniqueness (Refuted)

Take A=k=F_2 with Delta(1)=1 tensor1. The canonical family is
u_n(1)=gamma_n(1) for all n. A different family is

    v_0=1, v_1=id, v_n=0 for n>=2.

It satisfies both relations printed in scans 324 and 329:

    v_r*v_s=binom(r+s,r)v_{r+s},
    Gamma^r(v_s)v_r=sigma_{r,s}v_{rs}.

For the first, when r=s=1 both sides are zero because 2=0; if one index is
at least2 both sides are zero; zero indices give the unit. For the second,
an index1 gives an identity, and when both are at least2 both sides are
zero. Yet v_2 differs from u_2. The displayed finite coefficient check
examines every pair 1<=r,s<=16; the case argument proves all pairs.

The replacement is D.8: uniqueness follows for flat A after adding the
coproduct/addition compatibility. Indeed (A) for r=s=1 fails for v:
its left side is zero and its right side is 1 tensor1. Thus the family v
does not define a natural PD operation on arbitrary Hom(A,J).

## D.11. Nonflat coalgebras can admit several full natural structures (Proved)

Flatness is sufficient but not necessary. For any k-module M, the primitive
coalgebra A=k direct-sum M has Delta(m)=m tensor1+1 tensor m. Then
Hom(A,B)=B semidirect Hom(M,B), a square-zero extension. Its canonical
natural PD structure on Hom(A,J) is

    gamma_n(b,x)=(gamma_n(b),gamma_{n-1}(b)x),     n>=1.

It is defined for every M, including nonflat M. This is the square-zero
extension construction of Stacks Project, Lemma 60.3.1 (tag 07HH), opened
in this run: apply that lemma to B semidirect Hom(M,B), and restrict its
PD ideal J direct-sum Hom(M,B) to the stable subideal J direct-sum Hom(M,J).
The stability follows directly from the displayed formula.

Moreover the full natural structure need not be unique when M=k/2. In
that case Hom(M,B)=B[2]. For b in J and x in J[2], define, for n>=2,

    gamma'_n(b,x)=(gamma_n(b),
                  gamma_{n-1}(b)x+gamma_{n-2}(b)x^2),

with gamma'_0=1 and gamma'_1=id. This is a second natural PD structure,
and it agrees with the given PD structure on the embedded coefficient
ideal J via b|->(b,0).

Proof. Because 2x=0, the PD scalar axiom gives
4gamma_2(x)=gamma_2(2x)=0. Hence x^4=(2gamma_2 x)^2=0. Also 2x^2=0.
The sum formula follows by expanding the divided powers of b+c and
(x+y)^2=x^2+y^2. For multiplication by an arbitrary element (a,h) of
B semidirect B[2], the tangent part of the product is ax+bh. Expansion
uses b gamma_{n-1}(b)=n gamma_n(b) and
b^2 gamma_{n-2}(b)=n(n-1)gamma_n(b). The latter coefficient is even, so
its product with h^2 vanishes. The remaining terms give exactly
(a,h)^n gamma'_n(b,x), proving the scalar axiom.

The divided-power product identity has the correct x coefficient by
Pascal's identity. The difference between its two x^2 coefficients is
2 binom(m+n-2,m-1), which annihilates x^2. For iteration m,n>=2,
write y=gamma_{n-1}(b)x+gamma_{n-2}(b)x^2. Since x^4=0 and 2x=0,
y^2=gamma_{n-1}(b)^2 x^2. The coefficient of gamma_{mn-1}(b)x in the
iterated expression equals

    (mn-1)!/((m-1)!(n!)^{m-1}(n-1)!)=c_{m,n}.

The coefficient of gamma_{mn-2}(b)x^2 is the sum

    (mn-2)!/((m-1)!(n!)^{m-1}(n-2)!)
    + (mn-2)!/((m-2)!(n!)^{m-2}((n-1)!)^2)
    = c_{m,n},

because division of the two terms by c_{m,n} gives
(n-1)/(mn-1) and (m-1)n/(mn-1). This proves the iteration axiom; indices1
are the identity cases. All identities are natural under PD maps B->B'.

For an actual distinction take k=Z/4 and B,J as in D.9, but give A the
primitive coproduct. At (b,x)=(0,t), gamma_2 is zero while gamma'_2 is
(0,2u), which is nonzero. The finite program checks both full PD structures
on the 32-element convolution ideal inside its 256-element ring.

Thus an assertion of uniqueness without flatness is false even with all
PD axioms, and a flatness-only characterization of existence is false.
The exact indeterminacy is the parameter space P(A) in D.7; in the flat
case it is a singleton, whereas D.9 makes it empty and this example makes
it have at least two elements.

## D.12. The dual question and its concrete symmetric-coalgebra case (Proved)

The dual assertion needs its data typed. Let B'->B be a morphism of counital
cocommutative k-coalgebras and write C=coker(B'->B). Write pi:B->C for the quotient. Here is a completely typed version of
"divided copowers" which removes any reliance on finite duals. Choose
k-linear maps d_n:C->Sym^n(C), n>=1, and put tilde d_n=d_n pi for n>=1,
tilde d_0=epsilon_B. Require d_1=id_C. Let

    delta_{r,s}:Sym^{r+s}C->Sym^r C tensor Sym^s C

be the component induced by the diagonal C->C direct-sum C. Require

    delta_{r,s} tilde d_{r+s}
        = (tilde d_r tensor tilde d_s) Delta_B.                    (DA)

The coaction ell:C->B tensor C induced by (id_B tensor pi)Delta_B is
well-defined because B'->B is a coalgebra map. Let

    chi_n:Sym^n(B tensor C)->Sym^n B tensor Sym^n C

send the product of n pairs to the product of the n first factors tensored
with the product of the n second factors. Let
ell_n:C->B^{tensor n} tensor C be the iterated coaction and
pi_n:B^{tensor n}->Sym^n B the symmetric quotient. Require

    chi_n Sym^n(ell)d_n = (pi_n tensor d_n)ell_n.                   (DS)

Finally let rho_{m,n}:Sym^m(Sym^n C)->Sym^{mn}C multiply the m symmetric
monomials in the symmetric algebra. Require

    rho_{m,n} Sym^m(d_n)d_m = c_{m,n} d_{mn}.                       (DI)

These are explicit equations involving only B'->B and its quotient, and
are the dual sum, scalar and iteration compatibilities. The product
compatibility follows from (DA) by mu delta_{r,s}=binom(r+s,r).
No ordinary coalgebra is being assumed to possess this extra structure.

For every commutative k-algebra R the kernel

    K=ker(Hom_k(B,R)->Hom_k(B',R))=Hom_k(C,R)

has the induced divided powers

    gamma_n(f)=mu_R^{(n)} Sym^n(f) d_n,      n>=1,

where the answer is pulled back from C to B, and gamma_0 is the
convolution unit. The sum, scalar and iteration axioms follow respectively from (DA),
(DS), (DI), by evaluating the relevant symmetric algebras in R. The
product identity follows from (DA) as above. Conversely, every PD law
natural in commutative k-algebras R arises this way: Hom(C,R) is represented
by Sym(C), evaluation at the universal map determines d_n, and the scalar
z in k[z] forces it to have symmetric degree n. Testing the PD identities
in Sym(C direct-sum C), Sym(B) tensor Sym(C), and Sym(C), respectively,
recovers (DA), (DS), (DI). Thus these equations are necessary and sufficient,
not only sufficient. This proof uses no dual-module identification and no
flatness, projectivity or finite-generation hypothesis. It answers the
dual question with exactly its stated divided-copower data.

There is a completely explicit such structure for B=Sym_k(M), B'=k,
with its usual primitive coproduct on M, for every k-module M. If
f(1)=0, then for a monomial x_1...x_r,

    gamma_n(f)(x_1...x_r)
      = sum_{unordered partitions pi of {1,...,r} into n nonempty blocks}
            product_{D in pi} f(product_{j in D}x_j).

The expression is symmetric and multilinear in the x_j, so it descends
to Sym^r(M). For n>r it is zero. The n-fold convolution f^{*n} sums over
ordered partitions into n blocks; because f(1)=0, empty blocks contribute
zero. Dividing combinatorially by the n! possible orderings gives exactly
the stated gamma_n and proves f^{*n}=n!gamma_n(f) without dividing in k.
The sum formula colors the blocks of an unordered partition by f or g.
The product formula chooses which of m+n blocks belong to the first
factor, giving binom(m+n,m). Iteration partitions mn blocks into m
unordered groups of n, giving (mn)!/(m!(n!)^m). The scalar formula first
distributes the factors of a monomial among the scalar map and f, and
then partitions the f-factors; the two orders enumerate the same finite
set. These bijections prove every PD identity over Z, and therefore over
every ring and module. This is the concrete example named on scan324.

The note does not claim that an ordinary coalgebra B alone automatically
has divided copowers. Supplying only Delta_B would erase precisely the
extra data in the manuscript's second question.
