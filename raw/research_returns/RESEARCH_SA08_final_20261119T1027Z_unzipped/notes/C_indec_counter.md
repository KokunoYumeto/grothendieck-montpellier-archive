# Indecomposables are not invariant under arbitrary free PD resolutions

2026-11-19, agent /root/topos. This rules out one proposed shortcut in
the bar indecomposable calculation; it does not decide that calculation.

Let R=Z_(p), and let y be an even generator in positive homological
degree2. Put y_i=gamma_(p^i)(y), with y_i^p=p a_i y_(i+1), a_i a p-unit.
Use the free graded PD algebra

    C=Gamma_R(y) tensor Lambda_R(x_i:i>=0)
      tensor Gamma_R(v_i:i>=0),

with homological degrees

    |x_i|=2p^i+1,  |v_i|=2p^(i+1)+2,

and differential of degree minus one

    dx_i=y_i,  dy=0,
    dv_i=p a_i x_(i+1)-x_i y_i^(p-1).

The differential squares to zero. All generators have positive
homological degrees and the differential is triangular: y first,
then all x_i, then all v_i (or increasing homological degree).

Modulo p it factors, exactly as in C18, into

    Fp[y_i]/(y_i^p) tensor Lambda(x_i) tensor Gamma(v_i),

with dx_i=y_i and dv_i=-x_i y_i^(p-1). The same exhaustive monomial
identity-pair decomposition proves homology Fp in degree0 only.
Every homological degree is finite free over R. Universal coefficients
and Nakayama imply H_0(C)=R and H_j(C)=0 for j>0. The weightwise PID
splitting also proves universal base-change acyclicity. Therefore
C->R is an actual quasi-isomorphism of augmented free graded PD
differential algebras, all of whose generators are positive.

Take PD indecomposables: quotient the augmentation ideal by products
and by gamma_m of even elements for m>=2. The pair x_0->y remains
an identity pair. For i>=1, dx_i=gamma_(p^i)y becomes zero, and

    d v_(i-1)=p a_(i-1) x_i.

Consequently

    H_(2p^i+1)(Q_PD C)=R/pR  (i>=1),

whereas Q_PD(R)=0. Thus indecomposables do not preserve this
quasi-isomorphism. In particular there cannot be a general comparison
theorem asserting that all positive triangular free PD resolutions
are equivalent by a homotopy that induces a chain homotopy on their
PD indecomposables.

The usual minimality of a local acyclic closure may rule out this
deliberately nonminimal construction, but one must then prove that the
specific bar resolution has a suitable minimal cancellation. Its
quasi-isomorphism to a tensor of unary minimal closures is insufficient
by itself. The arity-m indecomposable pattern of the bar construction
therefore remains a separate question.
