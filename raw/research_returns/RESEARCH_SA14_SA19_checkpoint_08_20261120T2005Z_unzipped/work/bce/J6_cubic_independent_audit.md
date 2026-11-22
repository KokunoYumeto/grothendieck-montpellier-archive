# Separate AI audit of DGJ's cubic-pencil counterexample

GPT-6 Astra (OpenAI), delegated agent `/root/bce`, 20 November2026,17:56UTC.
This is a separate model audit, not independent human verification.

## Result

**PASS for the geometric and correspondence core.** The argument produces a nonzero constant elliptic factor in the generic member's codimension-two algebraic representative, while the smooth cubic fourfold has zero codimension-two algebraic representative. It therefore refutes the middle fixed-part assertion for the stated integral-fibre pencil hypothesis, subject to preserving the chosen modern meaning of the manuscript's P^2. The same elliptic contribution survives an incidence quotient because the transposed correspondence detects it.

## Exact equations and smoothness

Work over k=algebraic closure of F5. Let

F=x0^3+x1^3+x2^3+x3^2 x4+x4^3+x5^3,
X=V(F) in P5.

The six partial derivatives are
3x0²,3x1²,3x2²,2x3x4,x3²+3x4²,3x5².
If all vanish, x0=x1=x2=x5=0, and x3x4=0 together with x3²+3x4²=0 gives x3=x4=0. Thus X is smooth.

The pencil x5=t x4 has finite members
D_t: x0³+x1³+x2³+x3²x4+(1+t³)x4³=0 in P4.
If c=1+t³ is nonzero, the same Jacobian argument gives smoothness. If c=0, its singular support is the single point [0:0:0:0:1]. The infinite member x4=0 is the cone over the smooth Fermat cubic surface x0³+x1³+x2³+x5³=0, with its single singular vertex [0:0:0:1:0]. Every member is geometrically integral: a reducible cubic hypersurface in P4 has components whose intersection has dimension at least two, and is singular on that intersection; a repeated component also has positive-dimensional singular support. Neither is compatible with the computed singular loci.

The common axis B=V(x4,x5) in X is the cone over the smooth plane cubic E:x0³+x1³+x2³=0, with vertex v=[0:0:0:1:0:0]. The ideal (x4,x5) has height two in the regular scheme X and is a regular sequence. Its Rees algebra has the single linear relation, so the fibres of the blowup pencil are precisely these D_t, not these members plus an unseen component over v.

The independent exact polynomial script `code/check_J6_cubic_audit.py` checked all six projective Jacobian charts of X, all five generic D_t charts over F5(t), the homogeneous Jacobian ideals at c=0 and infinity, and the smoothness of E. All assertions passed, actual elapsed runtime0.102263309seconds. No finite sampling is used to infer integrality or Chow-theoretic claims.

## The ruling calculation

Let K=k(t), D=D_t over K, and p:D'=Bl_v(D)->D. On the affine chart x3=1 the equation is
x4+(x0³+x1³+x2³)+c x4³=0.
Since the x4 derivative at v is1, x0,x1,x2 are regular parameters; the divisor B_K defined by x4 has multiplicity exactly3 at v. Therefore its strict transform R in D' is the smooth ruled surface obtained by blowing up the cone vertex, with class
[R]=p^*H-3F_exc.
Let q:R->E_K be its ruling. Each fibre ell of q is the strict transform of a line through v. Thus p^*H·ell=1 and F_exc·ell=1, so
c1(N_{R/D'})·ell=-2.
The exceptional intersection is transverse: a local parameter of the ruling at its exceptional point is a local exceptional equation.

Let i:R->D'. The correspondence from E_K to D' is i_*q^*. On CH^1(E_K), the self-intersection formula and projection formula give exactly
q_* i^* i_* q^*(z)
=q_*(c1(N_{R/D'}) q^*z)
=(q_*c1(N_{R/D'})) z
=-2z.
In particular the induced homomorphisms on Pic0(E_K) and the algebraic representative compose to multiplication by−2. Since5 does not divide2, this is a nonzero isogeny of the elliptic curve. No positivity assertion or unidentified canonical self-duality is needed.

For the point blowup of a threefold, the Chow decomposition is
CH²(D')=CH²(D)⊕Z,
not simply an equality of entire Chow groups. The added summand has no algebraically trivial classes. Hence p_* and p^* induce inverse maps on algebraically trivial CH² and on their universal regular algebraic representatives. The ruling contribution consequently remains nonzero on D.

The universal correspondence is defined over the constant curve E/k. Hence its homomorphism E_K->Ab²(D/K) factors through the K/k trace. Its nonzero image is a fixed elliptic subvariety. The corresponding incidence homomorphism back to Pic0(E_K) detects it as well, so passing to the quotient by cycles invisible to all incidence pairings does not kill it.

Finally H³(X,Q_l)=0 by weak Lefschetz for the smooth cubic fourfold. Proposition8.2 of Achter--Casalaina-Martin--Vial supplies an injection of a prime-to-characteristic Tate module of Ab²(X) into this group after choosing l away from a miniversal-cycle degree. Therefore Ab²(X)=0. Its restriction image cannot equal the nonzero trace image found above.

## Sources independently opened

- Achter, Casalaina-Martin, Vial, *A functorial approach to regular homomorphisms*, author PDF https://www.math.uni-bielefeld.de/~vial/algrep-functor.pdf . Proposition8.2, printed31/PDF30, was read in full: the injection applies in codimension2 for all characteristics with l away from p and the miniversal-cycle integer. The codimension2 existence and separable base-change framework is also explicitly stated in the introduction and Theorems5.10 and6.1.
- Qingyuan Jiang, *On the Chow theory of projectivizations*, https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/on-the-chow-theory-of-projectivizations/3DA5197C99935D82CCB4E359214AF439 . Section2.3 Theorem2.8(3), the blowup Chow decomposition (citing Fulton Proposition6.7), opened and read. The self-intersection and projection operations used above are the usual Chow operations.
- The supplied exact transcription 44:4 was reread. It requires geometric integrality of the pencil fibres, and has no smooth-axis hypothesis. The counterexample exploits precisely that missing condition; it does not refute DGJ's separate theorem with smooth axis.
