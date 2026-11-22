# AM-R-013: two literal analytic source predicates on the mixed definite host

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.

This result extracts the quantified analytic content of the first two
members of `AdmS` from the actual mixed-host construction. The first is
a corollary of ALP-LIFT-14 with an algebraic, rather than merely closed,
theta image. The second uses the actual terminal interlacing weights and
a finite rational translate to obtain a nonzero compact restriction.
Its period has an exact positive value. Neither assertion identifies
that period with the prescribed arithmetic `perCol` or `rowAF` lattice.
In particular this is not a construction of the old elliptic `D7`, a
proof of all six `AdmS` assertions, or a solution of `MainX`'s terminal
mass equation.

## 1. The source predicates being matched

The exact declarations are in
`Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean`.
`RallisSiegelWeilFormula`, lines154--161, requires actual irreducible
cuspidal subspaces \(\pi_j\) of the selected definite types, common
edge characters with infinity exponents \(-e_j\), and, for every
\(\phi\in\pi_{j+1}\), a finite identity
\[
 \phi=\sum_{i=1}^{r_\phi}
       \Theta^{\mathrm{bil}}_{\Phi_i}(\phi_i),
 \qquad \phi_i\in\pi_j,
 \tag{R13.1}
\]
with each \(\Phi_i\) factorizable and compact-finite. The predicate
does not prescribe the arithmetic row lattice or a norm bound for
these kernels.

`LiftParameterConditions`, lines163--166, requires that every actual
irreducible automorphic subspace of the selected last definite type
have a nonzero terminal period against some cusp form of the prescribed
last \(Y\)-type. The latter type is imposed on the conjugate form by
`IsDv`, lines123--125. For the ordinary compact restriction period the
literal combination of conjugations is
\[
 B_{\mathrm{top}}(\overline\phi,F)
       =\int_{[H]}\phi(\iota h)F(h)\,dh,
 \quad
 B_{\mathrm{top}}(f,F)
       :=\int_{[H]}\overline{f(\iota h)}F(h)\,dh.
 \tag{R13.2}
\]
Here \(G=U(I_n)\), \(n=N_m\), and
\(H=U(X')\) is the unitary group of the actual positive
codimension-one subspace \(X'=z^\perp\), identified with
the terminal \(Y_m\). The embedding \(\iota\) acts as
the identity on the orthogonal line. At each real place it is
conjugate to \(h\mapsto\operatorname{diag}(h,1)\);
no global isometry \(X'\simeq I_{n-1}\) is assumed.
This is the actual Hermitian restriction period, with its Haar measure
retained. We do not use the auxiliary identity-action Hilbert-space
model `thetaG` to obtain either conclusion.

## 2. An actual irreducible chain and finite factorizable spanning

Use the common host \(E'=\mathbf Q(\zeta_{28})\),
\(F'=E'^+\), the polarized \(J^2\), the same trace coefficient,
and all the characters, groups and compact types of ALP-LIFT-14.
For every fixed choice of the source rank and HC data there exist
actual irreducible cuspidal subspaces
\[
 \pi_j\subset\mathcal A(G_j),\qquad
        (\pi_j)_\infty\simeq\rho_j,
             \qquad 0\le j\le m,
 \tag{R13.3}
\]
such that (R13.1) holds for every edge. All these are specified
automorphic embeddings, so no multiplicity-one assertion for the
global spectrum is required.

**Proof.** The first input of AM-R-012 has fixed finite level and
compact real type. The automorphic space at that level and type is
finite-dimensional: it is a finite direct sum, over the definite
double-coset set, of invariant subspaces of the finite-dimensional
coefficient representation. Its spectral decomposition therefore
involves finitely many actual irreducible automorphic embeddings.
Decompose this input accordingly. Its first theta image is nonzero,
so at least one summand, belonging to an actual \(\pi_0\), has a
nonzero image with the same selected first real component.

Let \(\mathcal T(\pi_0)\) be the algebraic span of these theta
images, allowing all finite Schwartz functions and the selected real
component. It is stable under the target finite and real actions by
the exact equivariance of the Weil representation. All its automorphic
constituents have the unique local small-theta target at every finite
place, and the unique selected target compact type at infinity.
Consequently they have one global irreducible isomorphism type. The
automorphic multiplicity of that type is finite. The smooth algebraic
isotypic part is a finite direct sum of irreducible modules, hence is
semisimple. Its submodule \(\mathcal T(\pi_0)\) is semisimple as
well and contains an actual irreducible submodule \(\pi_1\).

This argument concerns algebraic spans, not just a dense image in a
Hilbert-space closure. By definition, every vector of \(\pi_1\)
is a finite sum of theta images of vectors of \(\pi_0\).
Every finite Schwartz function is a finite sum of restricted pure
tensors. Every vector in the selected real component is a finite sum
of tensors over the six archimedean places, and is compact-finite.
Expanding these finite sums and using bilinearity makes each kernel
factorizable without changing the image. This proves (R13.1) at the
first edge.

ALP-LIFT-14, sections3--7, proves nonvanishing for every actual
irreducible embedding with the resulting unramified parameters,
including each possible multiplicity copy. Apply it to \(\pi_1\),
then repeat the preceding algebraic-image argument. Induction gives
(R13.3) and (R13.1) at every edge. The input and output are cuspidal
because each positive definite rational group has no proper rational
parabolic. The characters are exactly the globally constructed equal
characters of LIFT14, so the required `IsMu` condition holds. ∎

The proof uses only even \(k,m,d=t+1\),
\(d\ge k+m+5\), the HC interlacing/parity, and
\(e_j-b_j,b_{j+1}-e_j\ge(d+2)/2\). Thus it applies also when
the source's auxiliary `TPar.t` replaces the fixed `Ranks.t`:
`TPar.t_ge`, `Hyp3.Interlace`, `TParity` and `Centred` imply exactly
these inequalities. The other `Ranks` inequalities, such as
\(3m<t\), are not used by the analytic nonvanishing proof.
This proves the first predicate's mathematical quantifiers for that
actual interpretation, whenever the surrounding geometric data have
been supplied. It is not an assertion that a Lean `ThetaX D` record
has been instantiated.

## 3. Exact terminal branching from the source HC lists

Fix one of the six complex places. Since \(m\) is even, the source
terminal Harish--Chandra lists have no residual \(\eta\)-shift.
From `DataTheta.lean`, `TPar.Xpar` and `TPar.Dpar`, lines538--548,
their decreasing rearrangements are
\[
 \begin{split}
 x={}&(u_0,\ldots,u_{k-1},\,
          B_{t+1}(-e_0),\ldots,B_{t+1}(-e_{m-1})),\\
 y={}&(v_0,\ldots,v_{k-2},-b_0,\,
       B_t(-e_0),-b_1,B_t(-e_1),\ldots,
                    -b_{m-1},B_t(-e_{m-1})),\\
 B_l(c)={}&(c+(l-1)/2,\,c+(l-3)/2,\ldots,c-(l-1)/2).
 \end{split}
 \tag{R13.4}
\]
In this display the terminal line \(y\) consists of its initial
\(k-1\) entries followed by the \(m\) pairs
\((-b_j,B_t(-e_j))\). It has length \(n-1\), whereas
\(x\) has length \(n=k+m(t+1)\). All source signature labels
are positive at \(j=m\).

The actual HC assumptions imply
\[
 x_i>y_i>x_{i+1}\qquad(0\le i<n-1).
 \tag{R13.5}
\]
Indeed, the initial entries alternate by the original \(u,v\)
interlacing. Next \(u_{k-1}>-b_0\), while
\(e_0-b_0\ge(t+3)/2\) places \(-b_0\) above the top
of the first \(x\)-block. Within each block the \(t\)
entries of \(B_t(-e_j)\) are exactly the midpoints between
the \(t+1\) adjacent entries of \(B_{t+1}(-e_j)\).
Between two blocks, \(b_{j+1}-e_j\ge(t+3)/2\) and
\(e_{j+1}-b_{j+1}\ge(t+3)/2\) place \(-b_{j+1}\)
strictly between their endpoint entries. These observations also
justify the stated decreasing rearrangements and the absence of
duplicates in the source finite sets.

Put
\[
 \lambda_i=x_i-(n-1)/2+i,\qquad
 \beta_i=y_i-(n-2)/2+i.
 \tag{R13.6}
\]
These are the dominant integral highest weights corresponding to
the two HC lists. The \(x_i\) are half-integers and the
\(y_i\) integers; hence each strict gap in (R13.5) is at
least \(1/2\). Substituting (R13.6) gives
\[
        \lambda_i\ge\beta_i\ge\lambda_{i+1}.
 \tag{R13.7}
\]
The compact branching theorem therefore gives
\[
 \dim\operatorname{Hom}_{U(n-1)}
      (V_\beta,\operatorname{Res}^{U(n)}_{U(n-1)}V_\lambda)=1.
 \tag{R13.8}
\]
This is the ordinary branching theorem, cited rather than re-proved:
Goodman and Wallach (2009), Theorem8.1.1, p.364. Restriction from the
complex algebraic groups to their compact forms preserves these
finite-dimensional representation multiplicities. Taking the external
tensor product over the six places gives the actual terminal compact
type \(\tau\) inside \(\rho_m|_{H_\infty}\), with multiplicity
one. Its HC parameter is exactly `Dpar m`, not a freely selected
branching constituent.

## 4. A compact restriction detector for every actual terminal embedding

The next elementary argument supplies the global existence needed
after the local branching statement. Local occurrence alone would
not justify restriction of a fixed automorphic vector at a fixed
finite point.

Let \(\pi\subset\mathcal A(G)\) be any nonzero irreducible
automorphic embedding with \(\pi_\infty=\rho_m\). There are
\(\phi\in\pi\) and a smooth cusp form \(F\) on \(H\)
such that
\[
 \overline F\text{ has real type }\tau,
 \qquad
 B_{\mathrm{top}}(\overline\phi,F)
       =\|\operatorname{Res}_H\phi\|_{L^2([H])}^{2}>0.
 \tag{R13.9}
\]
Here \(\phi\) is chosen so that its restriction already has
type \(\tau\); no projection denominator is suppressed.

**Proof.** First, \(G(F')\) is dense in \(G_\infty\).
For the identity Hermitian form, its Lie algebra over \(F'\)
is the vector space of matrices satisfying \(X^*=-X\).
Archimedean weak approximation for this vector space is elementary:
choose an \(F'\)-basis; the diagonal image of \(F'\) is dense
in the product of its real completions, since a rational basis gives
an invertible real embedding matrix and \(\mathbf Q^s\) is dense
in \(\mathbf R^s\). Approximate each coordinate independently.
The rational Cayley map
\[
             X\longmapsto(1+X)(1-X)^{-1}
 \tag{R13.10}
\]
is defined on every real skew-Hermitian matrix and maps onto the
open dense subset of the compact unitary group having no eigenvalue
\(-1\). Its inverse there is \((g-1)(g+1)^{-1}\).
The same rational identities hold over \(F'\). Approximation
through this chart proves density simultaneously at all real places.
No bound on denominators of the rational approximant is asserted.

Choose an actual nonzero finite vector in \(\pi_f\), and let
\(v\mapsto\phi_v\) be the resulting \(G_\infty\)-equivariant
map from \(V_{\rho_m}\) to the automorphic embedding. Some finite
point has nonzero evaluation on this map. A right finite translation
allows us to take that point to be the identity. There is then a
nonzero linear functional \(L\) on \(V_{\rho_m}\) with
\[
                  \phi_v(k,1)=L(\rho_m(k)v).
 \tag{R13.11}
\]
Let \(V_\tau\subset V_{\rho_m}\) be the nonzero branching
subspace supplied by (R13.8). The span of
\(\rho_m(G_\infty)V_\tau\) is a nonzero invariant subspace
of the irreducible \(\rho_m\), so it is the whole space.
Consequently there exist \(k\in G_\infty\) and
\(v\in V_\tau\) with \(L(\rho_m(k)v)\ne0\).
This inequality is open in \(k\). By the Cayley density just
proved, choose \(q\in G(F')\) with
\(L(\rho_m(q_\infty)v)\ne0\).

Right-translate \(\phi_v\) by \(q_f^{-1}\), and call the
result \(\phi\). For \(h\in H_\infty\), left rational
automorphy gives the exact identity
\[
 \begin{split}
 \phi(\iota h,1)
 &=\phi_v(\iota h,q_f^{-1})
  =\phi_v(q_\infty\iota h,1)\\
 &=L\bigl(\rho_m(q_\infty)\rho_m(\iota h)v\bigr).
 \end{split}
 \tag{R13.12}
\]
Thus the restriction is nonzero, already at the identity. Finite
translation commutes with the real group action. Since
\(v\in V_\tau\), the full restricted automorphic function
\(\operatorname{Res}_H\phi\), at all its finite points,
has real type \(\tau\).

Set \(F=\overline{\operatorname{Res}_H\phi}\). Restriction
is well-defined on \([H]\) by rational automorphy. It is smooth
and of some finite compact level. Both groups are anisotropic over
\(F'\), so their quotients are compact and all their automorphic
forms are cuspidal. Hence this \(F\) is permitted in the
analytic terminal predicate, and its conjugate has precisely the
required real type. Substitution into (R13.2) gives (R13.9).
The integral is positive because a nonzero continuous function on
the compact quotient is nonzero on an open set of positive Haar
measure. ∎

## 5. Retained class masses and the remaining arithmetic equation

The value in (R13.9) is exact for the chosen measure. For any compact
finite level \(K_H\) fixing the restricted function, choose
representatives \(h_c\) for
\(H(F')\backslash H(\mathbb A_f)/K_H\), and write
\(\Gamma_c=H(F')\cap h_cK_Hh_c^{-1}\).
Normalize real Haar measure to volume one and retain the finite
volume \(\operatorname{vol}(K_H)\). Then the same value is
\[
 \sum_c\frac{\operatorname{vol}(K_H)}{|\Gamma_c|}
       \int_{H_\infty}|\phi(\iota h,\iota h_c)|^2\,dh.
 \tag{R13.13}
\]
This follows by the ordinary quotient-measure disintegration over
the finite classes; it is the positive mass convention already
used in AM-DO-026 and AM-R-012. It neither normalizes the total
automorphic volume to one nor drops the stabilizers. Scaling
\(F\) by its reciprocal would force a unit period over
\(\mathbf C\), but AM-R-002 shows why this would still have
an arithmetic content and norm cost.

Equations(R13.1) and(R13.9) supply the first two analytic predicates
with their actual quantifiers and compact types. The other four
predicates involve the noncompact \(Y_j\) descent, specified
Fourier--Jacobi periods, the lower-tower vanishing, and real type
stability. Those are not supplied by this proof. In addition,
`TieRowIsom`, `TieIo`, and `TieBm` in `DataTheta.lean`,
lines739--752, still impose separate arithmetic comparisons.
In particular the explicit positive restriction period (R13.13)
has not been proved equal to the source's prescribed terminal
coefficient matrix. The finite translation \(q_f^{-1}\), the
resulting level, and the integral coefficient content remain
unquantified. These are precisely the limitations relevant to
the requested DP44 lift-count comparison.

## 6. Geometric interpretation and sources

The compact branching is a restriction of algebraic representations
of the reductive unitary groups, which become \(\mathrm{GL}_n\)
and \(\mathrm{GL}_{n-1}\) after splitting the CM extension.
The integral weights define the usual Schur functors and determinant
twists; their characters live in the representation \(\lambda\)-ring.
No rational projector in this proof is asserted to preserve a
chosen integral lattice. This distinction is the same one recorded
in the SGA6/SGA3 entries of `GROTHENDIECK_DICTIONARY.md`.
The theta kernels still arise from the principal polarization's
biextension and the CM Picard data already identified there
(SGA7I, Exp.VII, Proposition2.9.3, pp.172--174; Exp.VIII,
Theorem7.1, pp.299--300; FGA232, Theorem3.1, pp.148--149).
The restriction norm is an archimedean realization. A metrized
integral determinant-line comparison with it is additional work,
not a formal consequence of functoriality of motives or of weights
for sheaves over finite fields.

Primary new literature input: Goodman, R., & Wallach, N. R. (2009).
*Symmetry, representations, and invariants*. Springer.
Theorem8.1.1, p.364; DOI10.1007/978-0-387-79852-3.
The theorem was directly inspected in the primary book PDF at
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/goodwallx.pdf
(PDF page383). The compact branching theorem is cited as known.

Internal inputs, with their separate check histories: ALP-LIFT-14,
sections3--8; AM-DO-025--026; AM-R-002, AM-R-012; AM-K022.
Exact source declarations used above are `CayleySignature.lean`,
lines117--166, and `DataTheta.lean`, `TPar`, `block`, `Dpar`,
`Xpar`, `ThetaX.IsStable`, `typeX`, and `TieBm`.
No Lean execution or old-host instantiation is claimed.
