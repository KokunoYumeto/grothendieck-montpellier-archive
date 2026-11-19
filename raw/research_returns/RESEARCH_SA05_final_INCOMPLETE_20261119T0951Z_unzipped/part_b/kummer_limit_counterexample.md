# A concrete obstruction to exchanging the two limits

This is a proved diagnostic for the attempted B1 symbol argument. It does
not settle the degree-four invariant whose vanishing remains the first
threefold gate.

Let k be an algebraic closure of F_2, L=k(t), and ell=3. For dense open
subsets U of P^1_k consider the natural map

    colim_U H^1_cont(U,Z_3(1)) -> H^1_cont(Spec L,Z_3(1)).

It is injective but not surjective. It remains non-surjective after
tensoring with Q_3, and an explicit omitted class is invariant under
Gal(k/F_2).

Indeed, the opens U=A^1_k minus a finite set D are cofinal. Their Picard
groups vanish, since their coordinate rings are localizations of the PID
k[t]. Kummer theory, divisibility of k^*, and the Mittag-Leffler property
of the roots-of-unity system give

    H^1_cont(U,Z_3(1)) = direct_sum_(a in D) Z_3,

where the coordinate is the valuation at t=a. On the field one instead
gets

    H^1_cont(Spec L,Z_3(1))
      = lim_r L^*/(L^*)^(3^r)
      = { (v_a) in product_(a in k) Z_3 :
          for every r, all but finitely many v_a belong to 3^r Z_3 }.

For the last equality, L^*/k^* is the free abelian group on the linear
polynomials t-a. Its 3-adic completion has exactly the stated description.
Jannsen's continuous-cohomology exact sequence (3.1) has no lim^1 term
here because H^0(mu_(3^r)) has surjective transition maps. Thus this is
continuous cohomology, not discrete etale cohomology with a constant
Z_3 sheaf.

Enumerate the monic irreducible polynomials P_n in F_2[t], n>=1, by
increasing degree and then increasing binary coefficient encoding. There
are infinitely many, and they are pairwise coprime and square-free. Put

    c_r = product_(1<=n<r) P_n(t)^(3^n), viewed in L^*/(L^*)^(3^r).

The relation c_(r+1)/c_r=P_r(t)^(3^r) makes (c_r)_r compatible. Its
valuation at each geometric root of P_n is 3^n, which is nonzero in Z_3.
Every c_r is already in F_2(t), so the class is invariant for the natural
Galois action on geometric Kummer cohomology. Infinitely many distinct
roots have nonzero valuations. Hence no single finite D supports it,
and it cannot lie in the colimit over opens. Multiplication by any
nonzero integer, or by any nonzero element of Q_3, leaves infinitely many
nonzero valuations. The failure therefore persists rationally.

The exact finite certificate `code/kummer_limit_counterexample.py` checks
the first twelve irreducible factors by exhaustive trial division,
every adjacent Kummer congruence through level twelve, and the next
nonzero valuation outside each initial support. Its output is
`output/kummer_limit_counterexample.txt`. The proof for every finite
support is the preceding infinite-support argument; a finite computation
is not being used to infer the infinite assertion.

## Consequence for the attempted B1 proof

Norm-residue isomorphisms hold at each finite coefficient level. They
do not by themselves identify

    colim_U H^4_cont(U,Q_ell(3))

with a tensor product of a Milnor K-group, nor permit exchanging colim_U
with lim_r. An argument that represents successive finite reductions by
symbols must also keep the ramification inside one fixed open set.
The explicit degree-one class above shows that this extra requirement
is substantive even for projective space. The degree-four invariant and
the rational Chow-phantom gate remain unresolved.

## Actual independent checks

At 08:00 UTC on 19 November 2026, root read the complete written proof
and passed all parts, including its rational and invariant scope. Part D
independently read the complete note, program and saved output, and
passed the same arguments while explicitly not claiming a separate
reading of Jannsen. Both checks are recorded in the event ledger.
