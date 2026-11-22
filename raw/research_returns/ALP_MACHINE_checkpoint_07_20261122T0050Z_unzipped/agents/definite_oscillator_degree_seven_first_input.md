# AM-DO-034: a new selected first lift on the degree-seven principal host

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`,
21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

This extends AM-DO-030/033 to the actual principally polarized
`J^14` host of AM-K030. The selected polynomial is constructed
afresh in the forty-two CM matrix blocks. The proof does not
transport the old six-block upper witness through a change of
individual CM weights. It retains the standard-lattice rescaling,
the ramified rational-29 level, the finite Steinberg norm, and
the exact class-supported extraction.

The inputs are the proved geometry and integral action of AM-K030,
the finite splitting proof of AM-DO-022, the local selected-type
calculation of AM-DO-025, and the actual DP59 half-orbit theorem
in the checked form AM-K022. The construction is conditional only
on the displayed stage character and rank/weight data being
provided. AM-K031 is supplying concrete such even characters and
auxiliary primes. None of this asserts the unchanged full
`Dat.Ok`, the original `Fields.Kq` wrapper, or every numerical
source-rank condition on this new host.

## 1. Actual host and two coordinate conventions

Keep the notation of AM-K030:

\[
 E_0=\mathbf Q(\zeta_{28}),\qquad
 B\subset\mathbf Q(\zeta_{29}),\quad[B:\mathbf Q]=7,
 \qquad K=E_0B,\quad F=K^+,\quad [F:\mathbf Q]=42.
 \tag{DO34.1}
\]

Let `Psi` be the induced CM type, with forty-two members. Let
`pi_B` be K030's totally positive generator of the prime of B
above29 and `e_0,...,e_6` its explicit orthonormal trace basis
of `pi_B^(-3) O_B`. The actual principally polarized variety is

\[
 \mathcal A=(J^2)^7=J^{14},\qquad
 \Lambda=\pi_B^{-3}\mathcal O_K,
 \quad\xi_0=\frac{\zeta_7-\zeta_7^{-1}}{14}.
 \tag{DO34.2}
\]

In the standard `O_K` lattice convention the same polarization
has coefficient

\[
 \boxed{\xi_K=\xi_0\pi_B^{-6}.}
 \tag{DO34.3}
\]

This is an equality of the actual integral trace form, not only
of its discriminant. It identifies the standard line with the
product trace-one line. Its reduced seed in ordinary product
coordinates is `c^14 product sigma_q`, as in K030(PH22).

Index the CM embeddings by
`tau=(i,epsilon,l)`, with `i=1,2,3`, `epsilon=+,-`, and
`l=0,...,6`. For every matrix entry of a Hom space, write the
fourteen ordinary-J coordinates as `(u_(i,j),v_(i,j))`, and put

\[
 w_{i,\pm,j}=u_{i,j}\pm i v_{i,j},\qquad
 z_{i,\pm,l}=\sum_jU_{lj}w_{i,\pm,j},
 \quad U_{lj}=\tau_l(e_j),\quad U^tU=1.
 \tag{DO34.4}
\]

These are K030's product-eigen coordinates on the lattice
`Lambda`. To use the standard `O_K` lattice, define instead

\[
       \zeta_\tau=\tau(\pi_B)^3z_\tau,
       \qquad
       \partial_{\zeta_\tau}
                 =\tau(\pi_B)^{-3}\partial_{z_\tau}.
 \tag{DO34.5}
\]

Indeed the map from the standard lattice to `Lambda` is
multiplication by `pi_B^(-3)`, so its product-eigen coordinate
is `z_tau=tau(pi_B)^(-3) zeta_tau`. This proves (DO34.5) and
explains why (DO34.3) and (DO34.5) must be used together.
It is not legitimate to keep both the old coefficient `xi_0`
and the new standard lattice.

All the changes in (DO34.4)–(DO34.5) and their inverses are
integral at11. In particular the standard `zeta` derivations
give an integral invariant tangent basis after a coefficient
extension. The `U` matrix is real orthogonal, so it introduces
no real operator-norm loss. The old `plus/minus i` change and
the positive diagonal factors in (DO34.5) still have to be
included in norms and other local valuations.

## 2. A new highest polynomial in the actual forty-two blocks

Fix even ranks `a=k`, `b=k+t+1`, with `b>a`, and actual source
weight data of the form used in AM-DO-025 at all `tau in Psi`.
Let `e_tau` be the exponent parameter and let `w_(0,tau)` be
the actual dominant initial coefficient weight. Define

\[
 \nu_{\tau,i}=w_{0,\tau,i}+e_\tau-b/2,
 \quad 1\le i\le a,
 \qquad d_\tau=|\nu_\tau|,
 \qquad D=\sum_{\tau\in\Psi}d_\tau.
 \tag{DO34.6}
\]

AM-DO-025 proves that these are nonnegative partitions under
the displayed source HC gap conditions. That calculation is
local at one real place and does not depend on the number of
CM embeddings. It therefore applies to each of the forty-two
places here.

For `Z_tau` the `a by b` matrix of formal standard-coordinate
creation variables, set `nu_(tau,a+1)=0` and define

\[
 P_\nu(Z)=
 \prod_{\tau\in\Psi}\prod_{r=1}^{a}
 \det\bigl(Z_{\tau,[1,r],[1,r]}\bigr)
                   ^{\nu_{\tau,r}-\nu_{\tau,r+1}}.
 \tag{DO34.7}
\]

This is a new polynomial, defined directly in the new CM
eigenspaces. It has total degree D and separate degree `d_tau`
in each block. Its diagonal monomial is

\[
             \prod_{\tau,i}Z_{\tau,i,i}^{\nu_{\tau,i}}
 \tag{DO34.8}
\]

with coefficient exactly one. Only the diagonal term of every
minor can produce a monomial with no off-diagonal variable,
and summing its exponents telescopes to `nu_(tau,i)`. Thus
`P_nu` is primitive in the standard CM polynomial coefficient
lattice, in particular at11.

For the common splitting character with infinity component
`mu_tau(z)=(z/bar z)^(-e_tau)`, the actual compact Fock module
at `tau` is

\[
 \det_a^{e_\tau-b/2}\boxtimes
 \det_b^{-e_\tau+a/2}\otimes
       \operatorname{Sym}(\mathbf C^b\otimes(\mathbf C^a)^*).
 \tag{DO34.9}
\]

The bideterminant (DO34.7) belongs already to its Cauchy
summand indexed by `nu_tau`. Its source type is exactly
`rho_(0,tau)^vee` and its target type is the source's
`rho_(1,tau)`, by DO25.5–9. Taking the tensor product over
`Psi` gives source type `sigma=rho_0^vee` and target type
`rho_1`. No Schur projector, averaging denominator, or claim
that the transported old polynomial still has one CM weight
is needed. This resolves the first-edge weight-projection gate
for a newly constructed selected polynomial.

The standard-coordinate polynomial and the analogous
product-eigen polynomial satisfy the exact differential identity

\[
 P_\nu(\partial_\zeta)
       =c_\nu P_\nu(\partial_z),\qquad
 c_\nu=\prod_{\tau\in\Psi}
                      \tau(\pi_B)^{-3d_\tau}.
 \tag{DO34.10}
\]

Separate homogeneity proves this identity. In particular it
is an11-adic unit scalar, but it is not discarded at29 or at
infinity. With the valuation normalized by `v_29(29)=1`,

\[
            v_{29}(c_\nu)=-3D/7.
 \tag{DO34.11}
\]

Each entry of `U` also has valuation `-3/7` at29. Expressing
the full standard derivative polynomial in ordinary product
derivatives therefore gives the coefficient bound `-6D/7`
at29. At2 it retains the old upper denominator bound `2^D`.
These are upper bounds on denominators, not assertions that
every coefficient attains them. At11 the coordinate changes
are invertible and none of these denominators appears.

## 3. The actual allowed half-orbit survives the field repair

On the edge use the actual variety and line

\[
 X=\mathcal A^{ab}=J^{14ab},\qquad
 g=\dim X=42ab,\qquad
 \mathcal L=L_{2\infty}^{\boxtimes14ab}.
 \tag{DO34.12}
\]

Choose

\[
 \alpha=(1+2\sqrt{-7})^e\in E_0\subset K,
 \quad M=29^e,\quad e\ge1,
 \qquad\alpha\bar\alpha=M.
 \tag{DO34.13}
\]

Multiplication by alpha commutes with the B-action and acts
diagonally on the fourteen ordinary factors. Its actual Rosati
adjoint is bar alpha. Hence its polarization norm is exactly
M on the new product. The ideals `(alpha)` and `(bar alpha)`
remain coprime after extension to K: they lie on the two
different relative split halves at29. At a selected prime of
K above29 their nonzero valuations are `7e`, since the
absolute ramification degree there is seven.

Take the exact DP59 tensor product basis on the fourteen
ordinary factors, and then on all `ab` entries. It is an
integral basis of

\[
 \mathcal W_M=[\alpha]^*H^0(X,\mathcal L^M)
         \subset H^0(X,\mathcal L^{M^2}),
 \qquad \operatorname{rank}\mathcal W_M=M^{42ab}.
 \tag{DO34.14}
\]

The prescribed quotient representatives give parameters

\[
           t'_\lambda\in X[\alpha^2],\qquad
           x_\lambda=M t'_\lambda\in X[\alpha]\subset X[M].
 \tag{DO34.15}
\]

They retain their actual odd-order symmetric lift scalars.
They are exactly the permitted product orbit, not the whole
theta group of `L^(M^2)`. All statements follow by the actual
diagonal product identification, so they do not require a
new conjectural CM theta-span theorem. At11, `[alpha]` is
étale and is a formal isomorphism because its degree is a
power of29. The integral principal line and section are the
ones in K030, so the K018 reduced/Chern gauge applies to
this ordinary product.

The actual finite vacuum is the transport of the product
vacuum through the exact symplectic lattice isometry in
K030(PH17–20). Its finite norm is one. At every nonsplit
odd place, K/F is unramified and the opposite even identity
Hermitian lattice is integrally hyperbolic. The proof in
DO022 §3 therefore applies with the new local field and
the coefficient `xi_K`, which generates the actual absolute
codifferent. Its Pan conductor condition uses that exact
valuation and does not require absolute unramifiedness.
All dyadic places are relatively split, because splitting
of E0/F0 at2 persists under base change. DO020 covers them.
Consequently the standard splitting and the two normalized
moved-lattice averages agree, with their actual determinant-root
characters, exactly as in DO22.8. This is a transport of
the proved local hypotheses and proof, not an inference
from equality of vacuum lines alone.

The same Heisenberg reading therefore has the fixed product
period `C^(14ab)`, where C is the already fixed ordinary-J
period of DO022/R006. All finite Weyl and symmetric-lift
scalars remain in the reading. The equality holds as a
reduced germ and hence after the actual polynomial
`P_nu(partial_zeta)`.

## 4. Simultaneous jets and one selected nonzero coefficient

Fix an auxiliary finite vector

\[
 \phi_{\rm aux}=\mathcal O\phi_0\ne0,
 \qquad\mathcal O=\sum_{r=1}^{s}b_rW_{y_r},
 \tag{DO34.16}
\]

supported at odd rational primes away from11 and29. Reduce
the parameters modulo the actual selfdual lattice, combine
their exact phases, and retain distinct classes with nonzero coefficients as
in DO030. Let a fixed odd integer `d` prime to11·29 kill
these classes. Then they give s distinct points of `X[d]`.

Every step of DO030 is valid on (DO34.12), for the following
specific reasons. First, the new lattice is perfect by
K030, so the same rational representative `r_j=M z_j`,
where `M z_j=t_j`, has the fixed phase on the whole orbit.
This uses the rational inclusions
`delta_(j,29) in M Lambda_29` and
`x_lambda in M^(-1) Lambda_29`; it does not substitute29
for a uniformizer. Second, the prime-to11 torsion points
remain distinct on the good model. Third, the translated-line
comparison is still made by the actual `[d]` pullback and
its integral symmetric theta lift, so its fibre scalar is
an11-unit. No translated theta-null is divided out. Finally,
the integral simultaneous-jet proof depends on `L^3` being
very ample and on the actual product line and base change,
not on the number of factors.

Thus the same explicit threshold gives the surjection

\[
 M\ge3s(D+1)-1
 \quad\Longrightarrow\quad
 \mathcal W_M\twoheadrightarrow
       \bigoplus_{j=1}^{s}
           \operatorname{Jet}^D_{z_j}(\mathcal L^{M^2}).
 \tag{DO34.17}
\]

For completeness, sections of `L^3` that vanish at all but
one of the s specializations supply the factor of degree
`3(s-1)(D+1)`. At the selected point choose g formal
parameters as ratios of sections of `L^3`, and homogenize
an arbitrary D-jet with degree `3D`. The remaining exponent
is at least2 and supplies a section nonzero at that point.
The construction uses only unit inverses, so it is integral.
Pullback by the actual alpha isogeny gives (DO34.17).

Take the standard CM tangent basis in (DO34.5). Its diagonal
monomial (DO34.8) has coefficient one, and an ordinary jet
with that coefficient evaluates under `P_nu` to the factorial

\[
       \prod_{\tau,i}\nu_{\tau,i}!,\qquad
       B_\nu=\sum_{\tau,i}v_{11}(\nu_{\tau,i}!).
 \tag{DO34.18}
\]

Prescribe this degree-D monomial at an auxiliary point whose
`b_r` has minimum valuation, and prescribe zero D-jets at
all other auxiliary points. Multiply the monomial by the
unit `M^D` to retain the source's normalized level reading.
There are no lower terms. Therefore the possibly nonintegral
higher coefficients of the Chern gauge cannot affect the
degree-D derivative. The resulting functional has valuation
`min_r v_11(b_r)+B_nu`. Expanding the interpolating section
in the integral actual basis (DO34.14) implies that at least
one individual basis section has valuation no larger.

Consequently one permitted lambda satisfies

\[
 a_\lambda\ne0,\qquad
 v_{11}(a_\lambda)\le\min_rv_{11}(b_r)+B_\nu,
 \qquad
 \vartheta_{r_{P_\nu}\mathcal O\phi_\lambda}(1,1)
                   =C^{14ab}a_\lambda.
 \tag{DO34.19}
\]

This proves selected first nonvanishing in the forty-two
CM blocks. It does not assert the old fixed-row sharp slope,
which concerned a different explicitly selected directional
witness. The present factorial upper bound is its own
fully proved statement.

## 5. Finite Steinberg input on the new host

Suppose `g_0,g_1` are distinct odd rational primes, different
from11 and29, that split completely in K. Fix the forty-two
selected relative split places above each. Let the common
character mu be unramified away from these G places and29,
tame at G, and trivial on the principal rational29 level
used below. Its infinity exponent must be the one in
(DO34.6). The concrete character supplied in K031 is
unramified at29 and meets this last condition.

At each G place use exactly the determinant-corrected free
residue-matrix construction of DO033. Its genuine source
action is
`eta(det g)^(-1)|det g|^(b/2) f(Xg)`. It contains the pure
finite Steinberg type, has raw value one at `[I_a;0]`, and
has squared norm

\[
          \gamma_q=q^{-ab}\frac{|\mathrm{GL}_a(\mathbf F_q)|}
                                         {q^{a(a-1)/2}}.
 \tag{DO34.20}
\]

Its Fourier expansion is an actual auxiliary Heisenberg
combination with at most `q^(ab)` terms, minimum coefficient
valuation zero at11, and squared coefficient norm gamma_q.
These facts are the local theorem of DO033 and require no
new field extension argument once the local fields are
actually degree one.

Tensoring over the eighty-four selected G places gives

\[
 \begin{split}
 d_G&=(g_0g_1)^{21a(a-1)},\\
 \Gamma_G&=(g_0g_1)^{42(-ab+a(a+1)/2)}
       \prod_{\epsilon=0}^{1}\prod_{i=1}^{a}
                                     (1-g_\epsilon^{-i})^{42},\\
 s_G&\le(g_0g_1)^{42ab},\qquad
 \min_rv_{11}(b_r)=0,\qquad
 \|\mathcal O_G\phi_\lambda\|_f^2=\Gamma_G.
 \end{split}
 \tag{DO34.21}
\]

Apply (DO34.19) with this actual vector and choose

\[
 e=\max\{1,\lceil\log_{29}(3s_G(D+1)-1)\rceil\},
                  \qquad M=29^e.
 \tag{DO34.22}
\]

The result is one permitted half-translate, still carrying
the selected real source type and the pure finite Steinberg
source type, with nonzero coefficient and upper valuation
`B_nu`. Its finite norm is exactly as in (DO34.21); no
norm of an interpolating linear combination is being used.

## 6. The new level, rational stabilizer, and exact extraction

At29 use principal congruence modulo the rational ideal
`(M)=(29^e)` at all six real-field primes over29. At each
G place keep the full integral compact, and let the source
function vary there by its finite matrix coefficient. Keep
the full integral compact elsewhere. Denote the resulting
product by `K*`.

The principal29 subgroup fixes every permitted finite
translate exactly. Its parameter lies in the selected
relative split isotropic position space, with denominator
dividing M. Acting by `g,h=1 mod M` displaces it by an
integral vector in that same space. The symplectic pairing
and the odd-place trace-one phase on that displacement
are zero. This proves the exact Weyl fixation, even though
the valuation of M at that local prime is `7e`. The compact
character is trivial there by hypothesis.

Normalize real Haar measure to volume one, and give the
standard full finite compact volume one. K030(PH26) gives

\[
 I_a^{K}(M)=[K_{a,0}:K^*]
       =M^{42a^2}\prod_{i=1}^{a}(1-29^{-i})^6,
                  \qquad\operatorname{vol}K^*=(I_a^K(M))^{-1}.
 \tag{DO34.23}
\]

The notation here records the index caused by the29
refinement; the G compact factors have not been shrunk.
There are six residue fields, each equal to `F_29`, and
each congruence length is `7e`. Replacing the exponent6
on the residue product by42 would be incorrect.

The rational stabilizer `G(F) intersect K*` is trivial.
It is finite because it preserves the global integral
lattice and is compact at all real places. At a place
over29 it lies in `1+29 M_a(O_(F_v))`. If a matrix B has
minimum uniformizer valuation `s>=7`, the unique lowest
term of `(1+B)^29-1` is `29 B`, of valuation `s+7`:
all middle terms have valuations at least `7+2s`, and
`B^29` has valuation `29s>s+7`. Raising to an integer
prime to29 preserves the minimum valuation. Thus this
congruence subgroup is torsion free. The rational
matrix embedding is injective, proving the assertion.

Let `u_infty` be the unit source highest vector and `u_G`
the product of DO033's unit generic Steinberg vectors.
Set `d_rho=dim rho_0`. On the identity finite `K*` class
define

\[
 F(k_\infty,k_f)=
 \overline{\langle u_\infty,\sigma(k_\infty)u_\infty\rangle
             \langle u_G,\tau_G(k_G)u_G\rangle},
 \tag{DO34.24}
\]

and set it to zero on all other classes. Triviality of the
rational stabilizer makes this a well-defined automorphic
function. It is cuspidal because the rational unitary group
is definite. Its real type is `rho_0`, and its G compact
type is the contragredient finite Steinberg type, with the
literal initial inverse generic character.

On that class the actual kernel is
`L(sigma(k_infty)u_infty tensor tau_G(k_G)u_G)` with value
`C^(14ab) a_lambda` at the original tensor. Applying compact
Schur orthogonality to both unit vectors returns the original
tensor divided by `d_rho d_G`. The class volume is the one
in (DO34.23). Therefore

\[
 \boxed{
 \Theta^{\rm bil}_{r_{P_\nu}\mathcal O_G\phi_\lambda}(F)(1)
       =\frac{C^{14ab}a_\lambda}{I_a^K(M)d_\rho d_G}\ne0,
 \quad
 \|F\|_2^2=\frac1{I_a^K(M)d_\rho d_G},\quad
 \|F\|_\infty=1.}
 \tag{DO34.25}
\]

This is an actual first automorphic lift on the new host.
It has an actual irreducible source constituent containing
the finite Steinberg type. Finite-dimensional compact
projection to a nonzero constituent is injective on that
irreducible compact copy. Its Borel-fixed line therefore
gives an Iwahori-fixed vector in the constituent. This
supplies the initial hypothesis of the local theorem
ALP-LIFT-19 on this host, whenever its stage characters
and global rank-gap hypotheses are also supplied.

No class-number-one statement about K or F is needed:
the input is supported on a single actual class, whose
mass was computed using its trivial stabilizer.

## 7. Norms and costs that remain after the repair

Let `h(nu)` be the hook product of a partition. In the
standard-coordinate convention (DO34.5), the exact real
Schwartz norm is

\[
 \|r_{P_\nu}\phi_{0,\infty}\|^2
 =\det(2Y)^{-7ab}\,
   |c_\nu|^2
   \prod_{\tau\in\Psi}
        \left[ h(\nu_\tau)
          \left(\frac{\pi}{2G_{i(\tau)}}\right)^{d_\tau}\right].
 \tag{DO34.26}
\]

The vacuum exponent is `14ab/2=7ab`. The Fischer norm
of each primitive highest bideterminant is its hook
product, by AM-R-011. Orthogonality of U and the metric
in K030(PH25) give the creation scale `pi/(2G_i)`.
Equation (DO34.10) supplies the exact remaining scalar.
This derives (DO34.26) in the actual product measure;
it does not normalize the real Gaussian to one.

Unit-normalizing the finite input and the source input
changes (DO34.25) to

\[
 \frac{C^{14ab}a_\lambda}
        {\sqrt{\Gamma_G}\sqrt{I_a^K(M)d_\rho d_G}}.
 \tag{DO34.27}
\]

If the real Schwartz vector is also made unit, divide
this value by the square root of (DO34.26). Thus the
standard-lattice scalar, all Gaussian/hook factors,
and the auxiliary finite normalization remain visible.

At11 one has

\[
 \begin{split}
 v_{11}(d_G)&=0,\\
 v_{11}(I_a^K(M))&=6\sum_{i=1}^{a}v_{11}(29^i-1),\\
 v_{11}(\Gamma_G)&=42\sum_{\epsilon=0}^{1}
                         \sum_{i=1}^{a}v_{11}(g_\epsilon^i-1),\\
 v_{11}\!\left(C^{-14ab}\Theta^{\rm bil}(F)(1)\right)
     &\le B_\nu-v_{11}(I_a^K(M)d_\rho).
 \end{split}
 \tag{DO34.28}
\]

For the candidate primes `4,615,409` and `5,276,377`
supplied by K031 and rank `a=42`, all three integers
`29,g_0,g_1` have order10 modulo11, and
`v_11(q^10-1)=1`. Thus the sums over `1<=i<=42`
equal4, giving the exact fixed factors

\[
          v_{11}(I_{42}^{K}(M))=24,
          \qquad v_{11}(\Gamma_G)=336.
 \tag{DO34.29}
\]

This last calculation is independent of e. Unit finite
normalization has scalar valuation cost168 in this
example. It does not invalidate the raw minimum
coefficient valuation zero used in (DO34.19).

For fixed ranks, fixed G primes, and variable selected
weights, (DO34.22) has `log M=O(log(D+2))`; the class
index and compact dimension consequently give an
`O(log(D+2))` source extraction cost. The coordinate
factor in (DO34.10), its29 denominators, and the real
hook/Fock norm have their own degree dependence and
are not included in that logarithmic assertion. In
particular the possible `6D/7` ordinary-coordinate
29 denominator is not a constant-level cost.

## 8. Scope and exact inputs

This proves an actual selected first kernel, with a
single permitted29 half-translate, a specified finite
Steinberg auxiliary vector, and an exact class-supported
source input on the new principal host. It closes the
first CM-weight and actual-half-orbit transfer gap.
It does not identify this auxiliary vector with the
literal raw `PhiG` or `Xi`, prove the terminal restricted
Gram nonvanishing, or compute the integral lattice of
a later iterated theta image. It also does not turn
the enlarged field into the unchanged original host
record when unrelated field/rank wrappers fail.

The local selected Schur identity and splitting proof
are used as settled earlier findings. The novelty here
is their exact simultaneous realization on K030's
standard principal lattice and allowed orbit, with
the forty-two-block polynomial and the changed costs.

Exact locators:

- AM-K030(PH3–9, PH17–26): explicit trace basis,
  actual integral product polarization, standard
  coefficient, K-eigen coordinates, and rational29
  congruence index.
- AM-DO-022 §§3–4: standard finite splitting comparison,
  Pan conductor and compact phase, arbitrary odd local
  base field, determinant roots, and split dyadic case.
- AM-DO-025(DO25.3–9): literal common-character compact
  Cauchy summand and source/target coefficient match;
  source `Columns/BaseLemmas.lean` lines496–552.
- AM-K022(J3–5, J6–16, J19–27): actual DP59 orbit,
  integral jet threshold, factorial detection and
  source-normalized differential reading.
- AM-DO-030 §§2–4: fixed auxiliary phases, translated-line
  unit comparison and simultaneous integral jets.
- AM-DO-033 §§1–5: primitive finite Steinberg vector,
  actual determinant-corrected residue model, Fourier
  norm and compact source extraction.
- AM-R-011: exact Fischer coefficient formula, highest
  bideterminant hook norm, and creation/Gaussian scaling.
- Primary geometric facts are the already read Milne,
  *Abelian Varieties*, I§6, p.30, and Mumford(1966),
  *On the equations defining abelian varieties I*,
  §1(II), p.289, as documented in K022/DO030.

