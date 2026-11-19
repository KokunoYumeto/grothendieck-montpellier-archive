# Nonlinear vertical closures and the actual simplicial repair gate

2026-11-19. GPT-6 Astra (OpenAI), automorphisms parallel agent.
This note separates proved auxiliary statements from the open
coherent-extension problem.

## Audit of the explicit p-local closure

The construction in notes/C_odd_disk_closure.md, sections1--4,
passes independent audit.

The formula y_i^p=p a_i y_(i+1) has a_i a p-local unit by the
factorial valuation. The displayed differential squares to
zero. Modulo p, the basis monomials separate into exactly the
two listed families of identity disks: the extra differential
term for x_i y_i^a gamma_m(v_i) contains x_i^2, and the extra
term on y_i^a gamma_m(v_i) with a>0 contains y_i^p. Both vanish.
No unpaired nonconstant monomial remains.

In each fixed cochain degree there are finitely many generators
and basis monomials. Thus the integral cohomology is finite
over Z_(p), and the universal-coefficient injection together
with Nakayama proves positive cohomology zero. The cycle
sequences split weight by weight over the PID. This establishes
arbitrary base change, not merely reduction modulo p.

The delayed-tail subalgebra is closed under products, PD
operations, and d. Each differential replacement has no greater
delay than its original generator. In a fixed cochain range
only finitely many basis monomials occur, so a finite maximum
of their weights plus delays proves eventual equality with
the full closure. All terms are free over the ground PID.
This proves the stated eventual vertical resolution, while
leaving the map-extension problem open.

## What functorial length-one presentations do not solve

For a simplicial abelian group M, the levelwise free cover
F(M)=Z[underlying M] and its kernel give a functorial
degreewise free length-one presentation. They do not make
F(M) projective in simplicial abelian groups.

An explicit test is M=K(Z,1). Let E be the Dold--Kan object
of the identity complex Z->Z in homological degrees1,0.
The map E->M projecting to the degree-one term is
degreewise surjective, E is acyclic, and its kernel is
constant Z. The evaluation F(M)->M has a normalized
one-cycle [1]-[0] mapping to the generator of pi_1(M).
It therefore has no simplicial lift through E.

An extra simplicial resolution followed by a diagonal
cannot remove this particular obstruction while preserving
that nonzero pi_1 map: every map through E has zero
pi_1 image. This is a counterexample to a general lifting
principle, not yet a counterexample for the special
cycle maps of the p-local closure.

## The first actual repair functor, p=2

Let M be a free abelian parameter module for an odd
degree-one generator x and its even differential y.
The quadratic weight piece of the free PD disk has
the natural cochain complex

$$
\Lambda^2M\longrightarrow M\otimes M\longrightarrow
\Gamma^2M
$$

in form degrees2,3,4. The first map sends
a wedge b to b tensor a minus a tensor b; the second
is divided-power multiplication, with diagonal
a tensor a mapping to2 gamma_2(a).
It is exact in the first two degrees and has
H4=M/2M, naturally in M.

The identification with M/2 does not supply a natural
linear cycle representative M->Gamma^2M. The map
a->gamma_2(a) is quadratic. Thus choosing a basis and
applying the single-generator closure does not by
itself give compatible simplicial face maps.

A completely natural, longer linear presentation uses
the whole displayed complex. It would introduce repair
generators in form degrees3,2,1, instead of just3,2.
Its first maps can be written as a shifted cone on
the quadratic weight complex. Whether iterating this
natural construction preserves flatness, eventual
horizontal acyclicity, and coherent maps to arbitrary
targets remains unproved.

## A coherent first repair for an absolute sphere parameter

Here is a positive result for the specific first repair.
It is not yet a relative cell-attachment theorem.
Let k be a ring, M=K(k,r) with r>=2, and let
x:M->A^(w,1) be a simplicial k-linear map into a
termwise-flat eventual theory. Choose w large enough
that A^(w,1) is horizontally acyclic, the cycle objects
Z^j(A^(2w,*)) have horizontal type k[j] for j<=4,
and the relevant vertical maps onto cycles are
surjective. Put y=dx.

Form the free PD DGA on the original disk and the
following additional parameter modules, all of
parameter arity2 and total weight2w:

* z indexed by Gamma^2 M, in form degree3;
* u indexed by M tensor M, in form degree2;
* v indexed by Lambda^2 M, in form degree1.

Let mu:M tensor M->Gamma^2 M be multiplication,
and let alt(a wedge b)=b tensor a-a tensor b.
Define, with xy(a tensor b)=x(a)y(b) and
xx(a wedge b)=x(a)x(b),

$$
dz=\Gamma^2(y),\qquad
du=z\mu-xy,\qquad
dv=u\,\mathrm{alt}+xx.
$$

These are closed right-hand sides at each successive
step: d(xy)=mu Gamma^2(y), mu alt=0, and
d(xx)=xy alt. They therefore define a PD differential.
In parameter arity2 the resulting cochain complex is
the identity cone on the old three-term complex,
with alternating signs. It is contractible. Thus
the first torsion has actually been removed, although
new nonlinear effects in higher arities remain.

The given map to A extends over all three new modules
by actual simplicial linear maps:

1. The cycle map Gamma^2 M->Z^4(A^(2w,*)) factors
   through Gamma^2(A^(w,1)). This middle simplicial
   module is acyclic by C05, because the row is
   flat and acyclic. The normalized source is
   degreewise free, so the cycle map is linearly
   nullhomotopic. A nullhomotopy lifts through
   the degreewise surjection A^(2w,3)->Z^4,
   giving z.
2. The next closed map M tensor M->Z^3 is null:
   Eilenberg--Zilber gives M tensor M the derived
   type k[2r], and 2r>3. The target has type
   k[3]. The same homotopy-lifting argument gives u.
3. The final closed map Lambda^2 M->Z^2 is null:
   M_n=0 for n<r and M_r=k, so Lambda^2 M has
   no simplices, hence no normalized terms, in
   degrees at most r. Its normalized complex
   is degreewise free and starts in degree
   r+1>=3. It has no derived maps to k[2].
   Lift to obtain v.

For clarity, the lifting assertion is elementary.
If a chain map f:P->Z is chain-nullhomotopic, P has
projective terms, and B->Z is degreewise surjective,
lift the components of a nullhomotopy to B. Applying
the chain differential to the lifted homotopy gives
a chain map P->B projecting to f. Dold--Kan gives
the asserted simplicial linear map.

This proves the first absolute sphere repair, not
its relative-boundary version. In an actual cell
attachment the parameter is a pair W subset V;
compatibility with previously chosen repairs on W
must also be established. Taking V contractible
does not remove that requirement, because V/W is
the sphere parameter and records the boundary data.

## Exact normalized calculations and the next possible obstruction

code/B_pd_square_normalization.py and
logs/B_pd_square_normalization.json give exact
integer matrices for all three square functors on
K(Z,r), 1<=r<=4. The basis consists of pairs of
surjections [n]->[r]; a pair survives normalization
exactly when its two cut sets cover all n positions.
All face matrices, chain identities, vertical
identities, and Smith invariant results are recorded;
unimodular decompositions are verified during the run.
Runtime:32.646618114999seconds.

For r=2 the nonzero homology is

$$
H_*(\Gamma^2K(\mathbb Z,2))
=\mathbb Z/2[2]\oplus\mathbb Z[4],
\quad
H_*(\Lambda^2K(\mathbb Z,2))=\mathbb Z/2[3],
\quad
H_*(M\otimes M)=\mathbb Z[4].
$$

For example the normalized divided-square ranks
in degrees2,3,4 are1,3,3, with differentials

$$
d_3=(2,0,-2),\qquad
d_4=\begin{pmatrix}
0&-1&-1\\
1&1&0\\
0&-1&-1
\end{pmatrix}.
$$

There is no automatic repetition of the first
connectivity argument. The new odd degree-three
parameter is P=Gamma^2K(Z,2). A further quadratic
repair of that odd disk has a relation map
P tensor P->Z^7(A). Its possible obstruction
group is nonzero:

$$
\operatorname{Hom}_{D(\mathbb Z)}
\bigl(NP\otimes NP,\mathbb Z[7]\bigr)
\cong(\mathbb Z/2)^2.
$$

Indeed over Z the bounded free complex NP has
derived type Z/2[2] plus Z[4]. Its tensor square
has two copies of Z/2 in degree6; their Ext^1
against Z supply the displayed group. The exact
matrix calculation in code/B_pd_square_next_obstruction.py
confirms this using the saved complex, without
recomputing the earlier cases. Its tensor ranks
are1,6,15,18,9 in degrees4 through8, and its
Hom-complex Smith factors are2,2. Receipt:
logs/B_pd_square_next_obstruction.json;
The initial runtime was0.03182814300089376seconds.
A subsequent0.03249293299813871second run expanded
the saved certificate to include every Smith
change-of-basis matrix, its unimodular determinant,
and the verified D=S*M*T identities.

This is a nonzero group in which an actual
obstruction may lie, not a claim that the
specific obstruction class is nonzero. Its
value can depend on earlier primitive choices
and on the coupled repairs of the full algebra.
The next precise gate is to compute that class
and the relative-boundary compatibility, or
give a structural reason they can always be
made zero. Connectivity alone no longer does so.

The first absolute repair was independently audited
by the shadows agent, who checked all signs,
the acyclic factorization, normalized projectivity,
both t-structure vanishings, and the actual
homotopy lift. The paper statement is C20 in
sections/B_C3_targets_repair.tex.

## The actual second stage is repairable (C22)

The possible (Z/2)^2 group above is not a surviving obstruction.
The actual quadratic disk of an already prescribed
z:P=Gamma^2K(Z,2)->A^(2w,3) has three-term complex
C=(Lambda^2P -> P tensor P -> Gamma^2P), in form degrees6,7,8.
Its sole vertical homology is P/2 in degree8.
N(P/2) is supported in horizontal degrees2..4, with terms of
Z-projective dimension1, hence pd_sAb(P/2)<=5.
Therefore Ext^8_sAb(P/2,const Z)=0.

When the target weight4w is vertically a resolution through8
and horizontally acyclic in rows0..8, the ordinary cochain-Hom
complex computes derived Hom in degree0. The proof is explicit
in sections/B_C3_hyperext.tex: normalized projective sources
have Ext^{>0} zero against acyclic rows, by degreewise splitting
and dimension shifting. Hyper-Ext entries have total degree
t+j-i; for t>0 and total<=1, i<=8 forces j<=8.
The resulting vanishing gives one actual strict cochain
homotopy of C's entire algebra map. Thus all three new
primitives can be chosen together, keeping the original z fixed.

D independently audited this argument, including the bounded
comparison and the assertion that the original z can be retained.
Root independently audited the written full proof on2026-11-19.
The formal result is C22 in sections/B_C3_hyperext.tex.

## Derived adjunction and every absolute fixed arity (C23)

For arbitrary k and a simplicial k-module Y,
RHom_sMod(Y,const k) = RHom_k(NY,k).
The left adjoint of const is H0. In a projective resolution in
the abelian category of nonnegative complexes, the projective
terms are sums/retracts of disks and degree-zero projectives.
The first-quadrant total complex identifies LH0(Y) with NY.
Derived adjunction gives the assertion. In particular all Ext
to constants vanish for an acyclic Y, without any flatness
assumption on Y itself.

For one original odd disk x:P->A^(w,q), q odd positive, take
its arity-m cochain complex D_m(P), with terms
Lambda^a P tensor Gamma^c P, a+c=m, in degree mq+c.
The actual map factors through D_m(U), U=A^(w,q).
If U is flat and horizontally acyclic, C05 makes every
horizontal term of D_m(U) acyclic. Hence its derived Hom to
const k is zero. Vertical resolution of the target through
b=m(q+1) and the bounded Hom comparison turn the actual
factorization into a strict simplicial cochain nullhomotopy.
Adjoining sD_m(P), with d(sc)=c-s(dc), gives an identity cone.
For m>=2 all added generators have positive form degree.
The complete hypotheses and proof are C23 in the same fragment.

This also removes the separate low-degree branch identified
by D: the first C20 cone has a new odd degree-one parameter
Q=Lambda^2K(Z,2). Since NQ has type Z/2[3],
N(Q/2) has type Z/2[3] plus Z/2[4], so the possible quadratic
Ext^4_sAb(Q/2,const Z) is Z/2. C23 nevertheless kills the
actual class, provided its indicated finite conditions hold.
No new computation is needed for that assertion; it uses
the already certified exterior-square complex.

### Exact remaining gates

The factorization in C23 belongs to an original disk. A
previously chosen nonlinear primitive map on an entire
repaired algebra need not extend functorially to the full
target row. Thus mixed repaired terms are not covered.
Nor does C23 preserve prescribed repairs on a cell boundary.
Finally, one fixed weight w need not satisfy
mw>=mu(m(q+1)) for every m if the eventual bounds mu are
arbitrary. Coefficient-tail delayed repairs are still needed
for a global eventual theory.

## C19 finite certificate

code/B_check_fermat_pushout.py and
logs/B_fermat_pushout_checks.json check p=3,5,7 over exact
rational polynomial rings. They verify LQ=U^p+W^p,
the differentiated identities, the closedness syzygy
T^p(Q_U-Q_W)=Q(f_U-f_W)-f(Q_U-Q_W),
weight2p, the formal infinity expansion, and residue-1.
The leading coefficient beta+1 is verified invertible
modulo (beta^p+1)/(beta+1). Runtime0.9373666769970441sec.
An initial symbolic coefficient extraction returned0 because
SymPy retained denominators of the form (beta+1)t; replacing
that extraction by the exact limit t*dlog(u+w) gave-1.
This was a certificate implementation correction, not a
change to the residue argument.
