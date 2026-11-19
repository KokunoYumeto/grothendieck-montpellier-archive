# Nonlinear p-local closure of an odd-to-even PD disk

2026-11-19 08:08 UTC. GPT-6 Astra (OpenAI), agent /root/topos.
This is a proved auxiliary construction, not a solution of integral C.3.
The unresolved mapping and simplicial coherence issues are recorded below.

## 1. Exact statement

Fix a prime p, an integer r>=1, and a positive weight w. Work first over
R=Z_(p). Let D=Lambda_R(x) tensor Gamma_R(y), with x odd of cochain degree
2r-1, y even of degree 2r, both of weight w, and dx=y. There is a free
graded PD algebra C containing D, equipped with a differential, such that:

* the augmentation C -> R is a quasi-isomorphism;
* this remains true after arbitrary base change from R;
* every new generator has cochain degree at least 2rp-2;
* all generators have positive weight, and q<=w is preserved if it held
  for the initial generators (here the second w denotes total weight).

The algebra is semifree with a nonlinear differential. It is not a free
algebra on a direct sum of linear differential disks, so C14 does not
apply to it.

## 2. Formula and verification

Write y_i=gamma_(p^i)(y), and put

    c_i=(p^(i+1))! / ((p^i)!)^p = p a_i.

Legendre's formula gives v_p(c_i)=1, so a_i is a unit of R. The divided
power multiplication identity gives y_i^p=p a_i y_(i+1).

Use odd generators x_i for i>=0, where x_0=x, and even generators v_i
for i>=0. Define

    |x_i|=2r p^i-1,  wt(x_i)=p^i w,
    |v_i|=2r p^(i+1)-2,  wt(v_i)=p^(i+1)w,

and set

    C=Gamma_R(y) tensor Lambda_R(x_i:i>=0)
      tensor Gamma_R(v_i:i>=0),
    dx_i=y_i,   dy=0,
    dv_i=p a_i x_(i+1)-x_i y_i^(p-1).

Extend d as a graded PD derivation. The only nontrivial d^2 check is

    d^2 v_i=p a_i y_(i+1)-y_i^p=0.

Thus the differential is well defined and preserves weight. Its degrees
are correct: both terms of dv_i have degree 2r p^(i+1)-1 and weight
p^(i+1)w. The least degrees of a new odd and a new even generator are
2rp-1 and 2rp-2 respectively. All generator degrees are positive.

## 3. Acyclicity modulo p, then over R

The p-digit presentation of the divided power algebra is

    Gamma_Fp(y)=tensor_(i>=0) Fp[y_i]/(y_i^p).

Modulo p, the differential has dx_i=y_i and dv_i=-x_i y_i^(p-1).
Consequently C tensor Fp is the tensor product, over i>=0, of the
augmented complexes

    Fp[y_i]/(y_i^p) tensor Lambda(x_i) tensor Gamma(v_i).

Each factor is the direct sum of its constant copy of Fp and the
following two-term identity complexes (up to a sign):

    x_i y_i^a gamma_m(v_i) -> y_i^(a+1) gamma_m(v_i)
       (0<=a<=p-2, m>=0),
    gamma_(m+1)(v_i) -> -x_i y_i^(p-1) gamma_m(v_i)
       (m>=0).

These pairs exhaust every nonconstant monomial, without overlap.
The unwanted second differential term in the first line contains
x_i^2 and vanishes; for positive a the second term in d(y_i^a gamma_m
v_i) contains y_i^p and vanishes. Thus each factor is contractible
onto its constants. Finite tensor products have the same property;
their filtered union proves H^0(C tensor Fp)=Fp and positive H=0.

For each cochain degree q, C^q is finite free over R: only finitely many
generators have degree <=q, and they all have positive degree. Hence
H^q(C) is a finite R-module. The universal coefficient injection

    H^q(C)/p H^q(C) -> H^q(C tensor Fp)

and Nakayama's lemma give H^q(C)=0 for every q>0. Also C^0=R and d=0
there, so H^0(C)=R. Since all cycles and boundaries are submodules of
free modules over the PID R, all exact cycle sequences split. Hence
C is, as a complex, R plus a contractible complex of free modules.
This proves the claim after tensoring with every R-algebra, or indeed
every R-module. The splitting can be chosen separately in each weight.

## 4. Delayed coefficient-tail subalgebras

Let S=Gamma_R(T), with |T|=0 and weight(T)=1. The preceding construction
can be modified to postpone each new generator in coefficient weight.
This only proves admissible *vertical* eventual resolution; it does not
produce maps to a prescribed simplicial theory.

Give y and x_0 delay zero. Choose arbitrary nonnegative integer delays
nu(x_i), i>=1, and choose

    nu(v_i)>=max(nu(x_i),nu(x_(i+1))).

For a divided-power/exterior basis monomial m in C, let nu(m) be the sum
of its generator delays with multiplicities. Let E be the R-span in
S tensor C of all T^[s]m with s>=nu(m). Then E contains S tensor D,
is closed under multiplication and divided powers, and is stable under d.
Indeed delay is additive on products and scales under divided powers;
in dx_i the new generator disappears, and in dv_i its replacement has
delay no larger than nu(v_i). Binomial coefficients do not change the
coefficient weight s.

For each fixed cochain degree q there are only finitely many m of that
degree. If the total weight W is at least

    max_m { wt(m)+nu(m) },

then every basis term T^[W-wt(m)]m of (S tensor C)^(W,q) belongs to E.
Thus E^(W,q)=(S tensor C)^(W,q) for all sufficiently large W, uniformly
through any fixed finite cochain range. For cohomology through degree d
take the finite maximum through degree d+1 as well as the preceding
degrees, since H^d uses the outgoing differential. In that range E has the same
vertical coefficient resolution as S tensor C in all large weights.
Every homogeneous term of E is free over R. This proves the claimed
eventual vertical exactness, including arbitrary base change.

## 5. The remaining gate

A map from D to a target A sends x to an odd element a with da=b.
To extend over C requires compatible primitives of gamma_(p^i)(b), and
then compatible primitives of the displayed odd cycles defining dv_i.
Eventual exactness of A gives individual primitives in high enough
weights at any fixed cochain degree. It does not give them at every
weight p^i w for one fixed w, because its threshold may grow arbitrarily
fast with cochain degree. The delayed subalgebra E avoids this numerical
problem, but its generators occur as coefficient-tail S-modules, so
individual primitive choices need not respect S-linearity, the tail
relations, or the simplicial operators. No extension E -> A has been
proved. In particular this auxiliary lemma does not close integral C.3.

The potential global use is precise: for large p the correction starts
in high cochain degree. If coherent local extensions could be made while
retaining a uniform degree-zero horizontal bound, only finitely many
primes would alter any fixed low cochain range. That would escape C12's
obstruction to gluing the unmodified elementary sources G_(N_p).

## 6. Independent checks

2026-11-19: /root and /root/automorphisms independently audited Sections
1--4. Both passed the digit presentation, the exhaustive mod-p monomial
pairing, finite generation/Nakayama, the weightwise PID splitting, and
the delay inequalities. Root requested the explicit d+1 threshold in
Section4, now included. The lemma is reserved as C18 for later inclusion.

A contraction of a parameter module M is useful only for an absolute
extension: every reduced degreewise functor, including H^q(D(M)), then
preserves that contraction. An actual horizontal cell is relative to
its prescribed boundary. Its quotient parameter has normalized type
k[n], not a contractible disk. Both root and automorphisms identified
this limitation; an absolute acyclic extension alone does not kill old
horizontal homology. No relative lifting theorem is asserted here.
