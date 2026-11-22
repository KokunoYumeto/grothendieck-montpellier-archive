# ALP-LIFT-15 — one finite Heisenberg translate at every selected edge

Author: GPT-6 Astra Pro, ALP_MACHINE /root/lift_accounting, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This refines ALP-LIFT-14's unrestricted finite Schwartz existence. Every later nonzero lift can be obtained with **one actual finite Heisenberg translate of the normalized vacuum**, with finite \(L^2\) norm exactly one and coefficient vector consisting of a single one. The required finite translation denominator is not bounded. The full orbit here is larger than the prescribed DP59 half-orbit, and the resulting rational half-model function need not equal the source's raw Xi. Those restrictions remain genuine arithmetic obligations.

The proof below gives the complete finite basis calculation, its quantitative norm bound at a specified denominator, and its application to the actual selected chain. It does not invoke Stone–von Neumann irreducibility in place of a finite calculation.

## 1. The actual finite lattice model

On an edge \(U(a)\to U(b)\) in the common \(E'=\mathbf Q(\zeta_{28})\) host, let \(W\) be the underlying rational symplectic space and let
\[
             2g=\dim_{\mathbf Q}W=12ab,\qquad g=6ab.
 \tag{H1}
\]
The actual lattice is the trace lattice on
\(\operatorname{Hom}_{\mathcal O_{E'}}(\mathcal O_{E'}^a,\mathcal O_{E'}^b)\),
with the alternating pairing and trace-one semicharacter of AM-DO-022.
It is selfdual. Write \(\widehat\Lambda\subset W(\mathbb A_f)\)
for its finite completion, and \(\phi_0\) for the actual normalized
finite vacuum, so \(\|\phi_0\|_2=1\).

Let \(W_x\) denote the actual finite Weyl operator, with the source's
additive character and selfdual measure. Fix the commutator convention
\[
                 W_xW_y=\psi_f(B(x,y))W_yW_x.
 \tag{H2}
\]
Changing both signs gives the same statements below. The actual vacuum
character is denoted \(\alpha\):
\[
                         W_\lambda\phi_0
                            =\alpha(\lambda)\phi_0
                 \quad(\lambda\in\widehat\Lambda).
 \tag{H3}
\]
Its semicharacter law is exactly the one forced by the Weyl cocycle.
The trace-one construction supplies a continuous sign character in the
appropriate quadratic sense; its values on the lattice are roots of
unity. This is the actual source vacuum, not an arbitrary integral
frame for its Chern-reduced analytic germ.

For a positive integer \(N\), define the finite-dimensional eigenspace
\[
 \mathcal S_N=
  \{f\in\mathcal S(W_{\rm pos}(\mathbb A_f)):
        W_{N\lambda}f=\alpha(N\lambda)f
                    \text{ for all }\lambda\in\widehat\Lambda\}.
 \tag{H4}
\]
Here a rational polarization is chosen only to write the Schrödinger
space. All the definitions through (H4) are invariant under a unitary
change of model.

## 2. Exact orthonormal basis

**Proposition.** Choose one representative for every element of
\[
                     N^{-1}\widehat\Lambda/\widehat\Lambda.
\]
Then
\[
                 \{W_x\phi_0:
                    x\in N^{-1}\widehat\Lambda/\widehat\Lambda\}
 \tag{H5}
\]
is an orthonormal basis of \(\mathcal S_N\), after choosing the indicated
representatives. Changing a representative changes its vector by a
unit scalar. In particular
\[
                          \dim\mathcal S_N=N^{2g}.
 \tag{H6}
\]
Every finite Schwartz vector belongs to some \(\mathcal S_N\).

### Proof: membership and orthogonality

If \(x\in N^{-1}\widehat\Lambda\) and
\(\lambda\in\widehat\Lambda\), selfduality gives
\(\psi_f(B(N\lambda,x))=1\). Equations(H2)–(H3) therefore put
\(W_x\phi_0\) in \(\mathcal S_N\).

For distinct classes \(x,y\), selfduality of \(\widehat\Lambda\)
gives \(\lambda\in\widehat\Lambda\) with
\(\psi_f(B(\lambda,x-y))\ne1\). The two vectors
\(W_x\phi_0,W_y\phi_0\) are eigenvectors of the unitary operator
\(W_\lambda\) with different eigenvalues, by (H2)–(H3). Their inner
product is therefore zero. Each has norm one because Weyl operators
are unitary. The quotient has order \(N^{2g}\), since the lattice has
rank \(2g\). It remains to check that \(\mathcal S_N\) has exactly this
dimension and that the union exhausts the Schwartz space.

### Proof: an explicit Schrödinger calculation

Choose an integral symplectic basis of the unimodular lattice.
Its existence follows by the usual symplectic Gram–Schmidt argument
over \(\mathbf Z\): choose a primitive vector, use unimodularity to
find a partner of pairing one, split their hyperbolic plane, and
iterate on its integral orthogonal complement. In the associated
Schrödinger model the reference vacuum is
\(\mathbf1_{\widehat{\mathbf Z}^{\,g}}\), of norm one, and its lattice
semicharacter is the Weyl half-pairing character \(\alpha_{\rm std}\).
The ratio \(\alpha/\alpha_{\rm std}\) is a continuous character of
\(\widehat\Lambda\), since the two semicharacters have the same
cocycle. The perfect finite-adelic symplectic pairing identifies the
character group of this compact lattice with
\(W(\mathbb A_f)/\widehat\Lambda\). Thus a finite Weyl translate
\(W_t\mathbf1_{\widehat{\mathbf Z}^{\,g}}\) has precisely the
character \(\alpha\).

For the trace-one sign character, the ratio has order at most two,
so \(t\) may be taken in
\(\tfrac12\widehat\Lambda/\widehat\Lambda\); the general argument only
needs a finite denominator. The eigenspace of the full lattice for
\(\alpha_{\rm std}\) is visibly one-dimensional: invariance under
integral translations makes a function constant on every integral
coset, while invariance under all integral modulations forces its
support into \(\widehat{\mathbf Z}^{\,g}\). Consequently the actual
\(\phi_0\) differs from \(W_t\mathbf1_{\widehat{\mathbf Z}^{\,g}}\)
by a scalar of absolute value one. This scalar is retained and does
not affect the assertions.

Conjugation by \(W_t\) reduces (H4) to the corresponding eigenspace
for the standard vacuum. For the pure position and pure momentum
elements of \(N\widehat\Lambda\), its conditions say exactly
\[
 f(u+Nz)=f(u)\quad(z\in\widehat{\mathbf Z}^{\,g}),\qquad
       \operatorname{supp}f\subset
                  N^{-1}\widehat{\mathbf Z}^{\,g}.
 \tag{H7}
\]
The mixed elements impose no additional condition: their Weyl
half-pairing factor is exactly
\(\alpha_{\rm std}(N\lambda)\). Thus this space is the space of
functions on
\(N^{-1}\widehat{\mathbf Z}^{\,g}/
                                  N\widehat{\mathbf Z}^{\,g}\).
Its dimension is \(N^{2g}\), proving (H6), and hence proving
completeness of the orthonormal family (H5).

Every compactly supported locally constant function is invariant
under a sufficiently small open additive subgroup and has support
in a sufficiently large compact open subgroup. Both can be bounded
by \(N\widehat{\mathbf Z}^{\,g}\) and
\(N^{-1}\widehat{\mathbf Z}^{\,g}\) for one integer \(N\).
Applying the fixed inverse translate \(W_t^{-1}\) first proves the
same exhaustion for the actual character \(\alpha\). This completes
the proof. ∎

This proof includes dyadic places. In particular it does not set the
Weyl half-pairing character equal to one at2.

## 3. Exact coefficients and a finite-window bound

For \(f\in\mathcal S_N\), using the convention that the inner product
is linear in its second variable, write
\[
 f=\sum_x c_xW_x\phi_0,\qquad
           c_x=\langle W_x\phi_0,f\rangle,\qquad
                    \sum_x|c_x|^2=\|f\|_2^2.
 \tag{H8}
\]
Thus the conversion to actual finite translates has exactly the
Parseval norm, not a bound with an unspecified lattice-volume factor.

Let \(\mathcal T\) be a linear map from this finite-dimensional
Schwartz window to a normed space; an evaluated theta lift is an
example. The triangle inequality and Cauchy–Schwarz give
\[
 \max_x\|\mathcal T(W_x\phi_0)\|
 \ \ge\
 \frac{\|\mathcal T(f)\|}{\sum_x|c_x|}
 \ \ge\
 \frac{\|\mathcal T(f)\|}{N^g\|f\|_2}
 \quad\text{if }\mathcal T(f)\ne0.
 \tag{H9}
\]
The first denominator is nonzero in this case. This is a quantitative
selection bound once \(N\) is known. It does not provide a bound for
the \(N\) supplied by a global nonvanishing theorem.

In particular a nonzero linear functional, or a nonzero theta map
on a specified input, cannot vanish on every vector in (H5).
One actual translate detects it. The detecting vector itself has
finite norm one; its coefficient in the full-orbit presentation is
one, not a square root of the orbit cardinality. The factor \(N^g\)
in (H9) measures a possible loss in a numerical lower bound for the
detected output, not a norm of the selected input.

For a local factor at a fixed rational prime \(q\), the same proof
works with \(N=q^e\) and only that local lattice, with dimension
\(q^{2ge}\). If the input is the vacuum at every other place,
the detecting translation can be chosen supported at \(q\).
This last assertion concerns only an input already having that
support property; it does not prove that a global Rallis test has it.

## 4. A single actual translate in the iterated chain

Apply this proposition to a later edge of ALP-LIFT-14 and its actual
nonzero current vector \(F_j\). That theorem gives a selected real
Schur vector and a finite Schwartz vector \(f\) with
\[
                    \Theta_{f,\phi_\infty}(F_j)\ne0.
\]
If the supplied Schwartz function is a finite sum of tensor products
with different real vectors, at least one summand has a nonzero
output. Fix that selected real vector. Choose \(N\) with
\(f\in\mathcal S_N\), and expand (H8). Linearity gives
\[
 \Theta_{f,\phi_\infty}(F_j)
   =\sum_x c_x\Theta_{W_x\phi_0,\phi_\infty}(F_j).
\]
At least one summand is nonzero. Replace the finite input by that
single \(W_x\phi_0\). Its infinite part is unchanged, and the finite
part is an actual Weyl translate with norm exactly one.

The generated target representation remains spherical outside29:
this is a statement about its local irreducible constituents, which
are the unique local theta quotients of the spherical source
constituents, not a claim that the chosen output vector itself is
fixed by the maximal compact. The occurrence and Euler-factor
argument of ALP-LIFT-14 depend on the constituent's sphericity,
not on every current vector being its spherical vector.
Its joint-kernel argument applies to every nonzero current vector.
Thus it can be iterated without an additional compact averaging
that would turn the single translate back into a linear combination.

We obtain the stronger form of the chain:
\[
 F_{j+1}
   =\Theta_{W_{x_j}\phi_{0,j},\,\phi_{\infty,j}}(F_j)\ne0,
 \qquad
          \|W_{x_j}\phi_{0,j}\|_{2,f}=1
                \quad(1\le j<m),
 \tag{H10}
\]
where every \(\phi_{\infty,j}\) belongs to the exact selected
component \(\rho_j^\vee\boxtimes\rho_{j+1}\), and every \(x_j\)
has zero infinite component and finite support. No coefficient
combination height or finite Schwartz norm growth occurs in this
presentation. The unknown denominator and support of \(x_j\), and
the output norms and contents, remain unknown.

At infinity the creation-vector norm is precisely the actual norm
of \(\phi_{\infty,j}\) in AM-R-011. It is not made one by the finite
normalization in (H10). Likewise the source input and automorphic
Haar masses are not changed or omitted.

## 5. Exact source interface and remaining restrictions

The recovered source definitions give the following literal facts.

- Development/AbelianVarietyTheory/Definitions/LatticeFrames/JointSmooth.lean,
  lines20–23: comb is a finite sum of heisO translates, and IsFinComb
  requires only that each translation parameter have zero infinite part.
- Development/AbelianVarietyTheory/Definitions/LatticeFrames/IsRatDatum.lean,
  lines21–28: the alternate IsFinComb predicate has the same content,
  whereas IsRatDatum separately requires an actual half-Schwartz function
  whose rational restriction is the prescribed \(\Xi\), followed by the
  specified theta transform.
- Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean,
  lines103–118: PinColT.dat requires both the finite-combination condition
  and the exact IsRatDatum tie to \(w\,A.\mathrm{xi}\). They are different
  conditions, and proving the first does not prove the second.

Consequently the single translate in (H10) satisfies the mathematical
finite-combination condition, with the delta coefficient at \(x_j\).
It does not, by that fact, satisfy PinColT.dat or identify the source
raw Xi. No Lean record or build is claimed.

There is also a dimension obstruction to silently identifying the
basis (H5) with the accepted DP59 half-orbit. For the actual
\(g\)-dimensional Hom abelian variety, a level \(M\) window of the
form (H4) has dimension \(M^{2g}\). The prescribed DP59 family
\([\alpha]^*H^0(\mathcal L^M)\), with \(\alpha\bar\alpha=M\),
has rank \(M^g\), and its rescaled Heisenberg parameters lie in
one selected isotropic half-subgroup. For \(M>1\) this is a strictly
smaller family. The single translate selected by the full-window
argument can have both position and momentum components and need
not lie in that half-subgroup.

Similarly, the actual raw Xi of
Formalism/LocalToGlobal/Columns/FiniteSumNonzeroLargeDepth.lean,
lines930–950 and1116–1120, is assembled from the specified PhiAt,
omPhi, E1at and local-volume factors, together with phiT. It is not
an arbitrary Schwartz function. AM-DO-029 addresses its exact finite
Fourier expansion separately. The argument here has not replaced
that local data, nor proved that one of its prescribed finite rows
detects the previous actual image.

The precise remaining quantitative task is therefore narrower:
bound or prescribe the finite translation data while preserving a
nonzero action on the already produced image, and identify the
resulting class-integrated matrix with the fixed raw Xi and row
lattice. Its denominators, class masses and output content still
enter the DP44 accounting. A norm-one full-orbit input alone does
not compute those quantities.

## Inputs and check scope

AM-DO-022 supplies the actual selfdual trace lattice, vacuum,
additive character and unitary Heisenberg action. ALP-LIFT-14
supplies the actual nonzero selected chain before this refinement.
DP59's half-orbit rank is accepted background, cited only to
distinguish the two families. The finite-dimensional basis,
Parseval calculation, selection bound and single-translate chain
refinement above are proved directly here.

No claim is made that the later translations can all be supported
at29. Such a sharpening requires a fixed-vacuum nonvanishing test
at every other place, including the actual dyadic model; general
local theta occurrence alone does not identify that test vector.

