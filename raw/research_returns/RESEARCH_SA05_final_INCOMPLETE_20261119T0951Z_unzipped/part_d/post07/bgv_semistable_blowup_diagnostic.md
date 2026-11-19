# Arbitrary residue varieties in semistable strata do not give the required pure encoding

19 November 2026, Part D. This is a proved geometric diagnostic for the attempted converse in C6. It is not a counterexample to independence of coefficient primes and is not counted as movement of its universal gate.

## 1. A strictly semistable model containing arbitrary residue cohomology

Let k be a finite field, R=W(k), and K=Frac(R). Let X/k be smooth projective. Choose a closed embedding

\[
X\hookrightarrow\mathbf P^N_k
\]

of codimension c≥1; increase N if necessary. Regard X as a closed subscheme of Y=\mathbf P^N_R and form

\[
\mathcal Y=\operatorname{Bl}_X(Y).
\]

Then \mathcal Y is regular, projective and flat over R, with generic fibre \mathbf P^N_K and a reduced strict normal-crossing special fibre with two smooth components

\[
Y_1=\operatorname{Bl}_X(\mathbf P^N_k),\qquad
Y_2=E=\mathbf P_X(N_{X/Y}).
\]

Their intersection is

\[
D=\mathbf P_X(N_{X/\mathbf P^N_k}).
\]

Here \mathbf P denotes lines in the displayed normal bundle. In particular E is a projective-space bundle of relative dimension c and D one of relative dimension c−1. We do **not** assume that the normal sequence

\[
0\longrightarrow N_{X/\mathbf P^N_k}
 \longrightarrow N_{X/Y}
 \longrightarrow\mathcal O_X\longrightarrow0
\]

splits. Such a splitting is unnecessary for either the geometry or the cohomology argument.

### Local charts and reduced semistability

Because X and \mathbf P^N_k are smooth over k, near every point of X there are étale coordinates t_1,…,t_N on Y over R for which the ideal of X is

\[
(p,t_1,\ldots,t_c).
\]

One can obtain these by lifting local equations for the smooth embedding and completing their linearly independent differentials to an étale coordinate system. The following calculation therefore takes place after an étale localization of Y, which is sufficient to check regularity and strict semistability.

In the p-chart of the blowup, put t_j=p u_j for 1≤j≤c. This chart is smooth over R; its special fibre is the exceptional component.

In the t_i-chart, put

\[
p=t_i v,\qquad t_j=t_i u_j\quad(j\ne i,\ 1\le j\le c).
\]

After eliminating t_j, the only equation is p=t_i v. This is the standard strictly semistable chart. Its special fibre is t_i v=0 with both multiplicities one. The two components meet transversely along t_i=v=0. Away from X the blowup is the identity, and the original special fibre is smooth. These charts prove the claimed regularity and reduced normal crossings. They also prove flatness: the local rings are p-torsion-free; over the DVR R this is flatness.

The exceptional divisor is the projectivized normal bundle of the regular immersion X→Y. The strict transform of the old special fibre is its blowup along X. Its exceptional divisor is D, as described by the normal subbundle in the exact sequence above. Since X is contained in the special fibre, the blowup is an isomorphism on the generic fibre.

Thus an arbitrary h(X), with its projective-bundle Tate shifts, is already present among the special-fibre strata of a strictly semistable model of a pure, entirely Tate, generic variety. This construction does not require X to have a smooth projective lift to R.

## 2. Exact cancellation in the weight spectral sequence

Fix ℓ≠p and take geometric étale cohomology with Q_ℓ coefficients. The projective-bundle formula gives

\[
H^m(E)=\bigoplus_{j=0}^{c}H^{m-2j}(X)(-j),\qquad
H^m(D)=\bigoplus_{j=0}^{c-1}H^{m-2j}(X)(-j).
\]

The restrictions of the relative hyperplane class on E to D are the relative hyperplane class on D. Therefore

\[
H^m(E)\longrightarrow H^m(D)
\]

is surjective in every degree: the displayed generators for D all lift. This remains true for a nonsplit normal sequence.

There are no triple intersections. The row of the Rapoport–Zink E_1 complex of fixed second index q has the three terms

\[
H^{q-2}(D)(-1)
 \xrightarrow{\gamma}
H^q(Y_1)\oplus H^q(E)
 \xrightarrow{\rho}
H^q(D),
\]

in columns −1,0,1, with the usual signed Gysin and restriction maps. This is exactly the two-component specialization of Rapoport–Zink Satz 2.10 and formula (2.11), already opened in the main C4 audit. Since the E-restriction is surjective, ρ is surjective. By Poincaré duality, the complementary signed Gysin map γ is injective. Consequently

\[
E_2^{-1,q}=0=E_2^{1,q}
\]

for every q. No weight-monodromy conjecture is used.

Only column zero survives. Its cohomology is H^q(\mathbf P^N_{\bar K}), either directly from convergence or by the blowup and projective-bundle formulas:

\[
H^q(Y_1)=H^q(\mathbf P^N_{\bar k})
 \oplus\bigoplus_{j=1}^{c-1}H^{q-2j}(X)(-j).
\]

Subtracting the two outer terms from the middle terms cancels precisely all the additional X contributions. The monodromy operator is zero on the abutment, also immediately because the generic variety is \mathbf P^N_K with good reduction.

An arbitrary algebraic cycle on X therefore may occur in the strata without supplying a surviving monodromy block. Realizing the strata is strictly less than the cycle-to-monodromy construction needed for the converse. One needs a prescribed cycle to control an actual surviving map on a pure generic summand, with simultaneous coefficient-prime compatibility.

## 3. What an ordinary hypersurface cut does to the given class

Suppose a relative hypersurface or finite relative complete intersection \mathcal H⊂\mathcal Y has smooth generic fibre and intersects Y_1,E,D transversely, so that its induced model is again strictly semistable. Write

\[
E'=E\cap\mathcal H,\qquad D'=D\cap\mathcal H.
\]

Both retain their maps to X, and the map D'→E' commutes with these maps. If α∈CH^r(X)_Q, then the cohomological pullback of its class to D' extends from E':

\[
\pi_{D'}^*\operatorname{cl}_\ell(\alpha)
=\operatorname{res}_{E'\to D'}
  \bigl(\pi_{E'}^*\operatorname{cl}_\ell(\alpha)\bigr).
\]

The same is true after multiplication by any relative hyperplane class or other class restricted from E'. Thus these particular classes lie in the image of the restriction differential ρ and vanish in its cokernel. In the two-component weight spectral sequence, the target of the only possible N block is such a restriction cokernel (with the appropriate degree and Tate twist). The direct projective-bundle realization of α consequently does not survive there merely by taking transverse hypersurface cuts.

This is a precise limitation of the direct cut construction, not a nonexistence theorem for every possible construction. Primitive cohomology newly created by a cut can have nonzero monodromy. Establishing that a prescribed arbitrary cycle controls a suitable primitive relation, and producing the required pure projector, would be a separate argument. No such argument has been supplied here.

## Sources and verification boundaries

The local blowup calculation and the restriction-surjectivity argument are supplied above in full. The only spectral-sequence input is the already opened Rapoport–Zink original: Satz 2.10 and equation (2.11), printed pages 40–41, https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf. The projective-bundle and smooth-center blowup cohomology formulas are used in their explicit displayed form; the dimension check is redundant with spectral-sequence convergence and the known generic fibre. This note does not assert that an arbitrary residue correspondence lifts to a generic correspondence.

Root and Part C independently read this entire note and passed the written proof. Part C reported its completed audit at 08:28 UTC. Both checks explicitly retained the nonsplit normal sequence and the restricted scope of the cut obstruction; neither treated it as a proof against all possible primitive constructions. Their truthful audit events are preserved in Part D's check ledger.
