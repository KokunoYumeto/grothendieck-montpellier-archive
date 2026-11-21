# Candidate quantitative bound on the split Eisenstein Weil family

GHOSTS-20261121, root, 21 November 2026. **DRAFT: not yet accepted after independent review.**

## R10. One bounded effective surface detects the Weil plane

Let (A,theta) be a principally polarized complex abelian fourfold with an integral O_K-action, K=Q(omega), of signature (2,2), whose Rosati involution restricts to conjugation. Let W be its rational Weil plane. Set R=[omega]^* and S=[sqrt(-3)]^* on H^4. Then

    54 e_W = (9+S)(2-R-R^2).

Indeed, after splitting K, on the summand wedge^a V_sigma tensor wedge^(4-a) V_barsigma, R has eigenvalue omega^(2-a) and S has eigenvalue 9(-1)^a. The displayed numerator has eigenvalue54 for a=0,4 and zero otherwise. The projector is orthogonal for the Hodge inner product: the eigenspace decomposition of the normal operators coming from K is orthogonal, as the Rosati involution is conjugation.

Suppose Z is an effective surface of theta-degree≤D0 with e_W[Z] nonzero. Put u=54e_W[Z]. It is an integral cohomology class with an integral cycle representative

    u = [18Z+2[sqrt(-3)]^*Z]
        -[9[omega]^*Z+9[omega^2]^*Z
          +[sqrt(-3)omega]^*Z+[sqrt(-3)omega^2]^*Z].

Pullback is flat because all maps are isogenies. Each side has degree≤36D0: the unit maps preserve theta, while [sqrt(-3)]^*theta=3theta and degree of a codimension2 pullback is multiplied by9. This formula remains valid over any algebraically closed field of characteristic different from3, including inseparable multiplication maps if relevant.

The real Weil plane is primitive of Hodge type(2,2), so its intersection form is positive definite. R is an isometry and satisfies 1+R+R^2=0 on W. Thus u,Ru form a basis, and, with d=(u,u)>0,

    Gram(u,Ru)= [[d,-d/2],[-d/2,d]].

Here d is a positive even integer (the middle exterior-power intersection lattice of an abelian fourfold is even).

## R11. Explicit extraction cost from one bounded effective surface

Let t in W, t≠0, and let delta≥1 satisfy delta t in H^4(A,Z(2)). Write T=(t,t)>0. Use the invariant flat metric whose Kähler form represents theta. Its total volume is theta^4/4!=1. For the harmonic class alpha=[Z] and every unit L2 harmonic4-form beta, beta is translation-invariant and has pointwise norm1. Therefore

    |integral_Z beta| ≤ volume(Z) = deg_theta(Z)/2.

Poincare duality with the Hodge star gives ||alpha||≤D0/2. Since e_W is orthogonal and the Hodge norm on W is its intersection norm,

    0<d=u^2 ≤54^2 D0^2/4 =729 D0^2=:M.

Put p=(delta t,u), q=(delta t,Ru), both integers, and Delta=3d^2/4, also a positive integer. Cramer's rule gives

    Delta delta t = a u + b Ru,
    a=dp+(d/2)q,  b=(d/2)p+dq.

The positive-definite Cauchy--Schwarz inequality gives

    |a|+|b| ≤3 delta sqrt(T) d^(3/2).

Consequently one can take

    N=delta Delta≤delta M^2,
    deg Z^+,deg Z^- ≤108 delta D0 sqrt(T) M^(3/2).

In particular, with M=729D0^2, the integer

    C=531441 delta D0^4 (1+4 ceil(sqrt(T)))

is a simultaneous bound for N and both effective degrees. It is deliberately coarse. This is a constructive certificate after choosing Z; it is not an assertion of minimality. Because only delta,T,D0 occur, it is uniform whenever these three data are fixed in a family.

## R12. A proposed explicit D0 from Schoen's unramified triple Prym construction

Take an unramified connected cyclic triple cover C→X, with genus(X)=3 and genus(C)=7. Let J=Jac(C), Theta its principal polarization, B the connected Prym of dimension4, and L=Theta|B. Standard complementary-polarization calculations give type(L)=(1,1,3,3), hence L^4=216. The family of these Pryms dominates the four-dimensional split Eisenstein Weil moduli component (Schoen1988 §3, with the polarization qualification corrected by Schoen1998).

Let W4(C)⊂J be the degree4 Abel image. Its class is Theta^3/3!, and hence, in the projective embedding given by3Theta,

    deg W4(C)=3^4*7!/3!=68040,
    deg(B)=3^4*216=17496.

Schoen's r=0 construction in Theorem2.0 uses the canonical linear system |K_X|=P^2⊂Sym^4X. The inverse image of this P^2 in C^4 is finite over P^2. Its cycles representing U pull back from the Weil plane of B under

    f:C^4→B,   f=P∘Abel,   P=3 Id−(1+sigma+sigma^2).

The map f is dominant and generically finite (Schoen §3, dominance argument for P∘Xi). Thus f_*f^* acts by a nonzero degree, so some positive irreducible component in the construction has nonzero Weil projection after pushforward.

Every Abel image of such a component is contained in W4(C)∩T for some translate T of B in Norm^-1(K_X). The whole preimage of Norm^-1(K_X) in Sym^4C is finite over |K_X|, because Sym^4C→Sym^4X is finite. Consequently these intersections have dimension≤2. A contributing two-dimensional image is therefore an irreducible component S_i of W4(C)∩T. On T, P is multiplication by3 followed by translation. Multiplication acts by a nonzero scalar on H^4(B), so at least one S_i, translated to B, itself has nonzero Weil projection.

Fulton's general Bezout inequality (Intersection Theory, Example8.4.6) gives

    deg_(3Theta)(S_i) ≤68040*17496.

Since S_i is a surface,

    deg_L(S_i) ≤68040*17496/9 =132269760=:D0.

No multiplicity from the ordered product is needed: we select a reduced irreducible image component with nonzero projection. Nonzero projection of a sum implies nonzero projection of at least one constituent. The map [3] is also omitted once nonvanishing of the constituent is known, so its degree is not charged.

### Passing to principal polarization

The finite kernel K(L) is (Z/3)^4 and is contained in B∩image(Jac(X)→J). The deck transformation acts trivially on that image, so it acts trivially on K(L). A maximal isotropic subgroup H of K(L) of order9 is therefore O_K-stable. The quotient q:B→A=B/H carries a principal polarization theta with q^*theta=L. Hence q_*S_i is an effective surface with

    deg_theta(q_*S_i)=deg_L(S_i)≤D0,

and its Weil projection is nonzero because q_* is an isomorphism on rational cohomology and commutes with K. The quotient construction is a finite isogeny correspondence on the moduli spaces, so the image of the dominant Prym family is still four-dimensional.

The remaining identification to check carefully is that this principal-polarization component is the component in T5 containing E^4 with its product polarization and mixed K-action. One route is the uniqueness of the unimodular Eisenstein Hermitian lattice of signature(2,2): the underlying rank8 indefinite rational quadratic form has an isotropic vector by Meyer's theorem; take a primitive O_K-vector, use unimodularity to find a partner of pairing1, and use surjectivity Tr(O_K)→Z to make the partner isotropic. Split a hyperbolic plane. The remaining rank2 Hermitian space has determinant−1 and is rationally isotropic, so the same argument splits it. This yields the hyperbolic lattice U⊕U, also isometric to diag(1,1,−1,−1), the E^4 lattice.

### Extending the numerical bound to the whole family

Once the component identification and the source-support assertion have been checked, apply R10--R11 with this D0 at every point of the dense Prym-quotient image. For a fixed flat Weil class t, delta and T are constant. The bounded cycle-class locus S_C is Zariski closed by B01's complex-family form. It contains the dense image, hence is all S. Thus the displayed C bounds the entire principal split Eisenstein Weil family and its Hecke orbit, and by specialization every good reduction of every arithmetic member for which the chosen polarization extends.

This would be an explicit (very large) completion of the T5 bounded-division gate. It does not give the least complexity at an arbitrary point of that family, and does not extend the argument to open higher-dimensional Weil families whose cyclic Prym maps are not dominant.

## Audit status

R10 projector and R11 linear algebra/mass estimate derived and read by root. R12 is a candidate awaiting independent adversarial review of: Schoen support and nonvanishing, finite symmetric-product map, the selected component argument, polarization descent, moduli component identification, and applicability of the existing Prym dominance theorem. No claim of proof is yet made for R12.
