# AM-R-012: an actual selected even-rank first lift with a single permitted finite translate

Author: /root, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC.

The rank-one starting correspondence of AM-R-009--010 is not the
starting edge in the recovered `Ranks` record. The construction here
uses the actual even ranks \(N_0\to N_1\), their selected compact
coefficient types, and the same splitting character on both groups.
It proves a controlled nonzero **first** theta lift with an exact
source input and a single permitted finite Heisenberg translate.
It does not yet identify its arithmetic row with the old elliptic
`StdPair`, or prove the later chain and six comparison identities.

The finite interpolation input is AM-K022, which specializes the
accepted DP56/DP59 allowed half-orbit theorem to the actual selected
polynomial. That proof and its check status are separate. In the
form used here it supplies one permitted translate with finite
Schwartz norm one and the nonzero jet bound (R12.5) below.

## 1. Actual fields, types, polynomial and character

Use
\[
 E'=\mathbf Q(\zeta_{28}),\quad F'=E'^+,\quad A=J^2,
 \quad G=U(I_a),\quad H=U(I_b),\quad a=k,
 \quad b=k+d=N_1.
 \tag{R12.1}
\]
All six selected complex places are those of AM-R-009, and the
positive Hom oscillator, trace-one vacuum, and period are exactly
those of AM-DO-022/026. Let \(w_0,w_1\) and
\(\nu_{0,\tau}\) be the weights and partitions of an actual
`HCParam`, as in AM-DO-025. Write
\[
 D=\sum_{\tau\in\Phi'}|\nu_{0,\tau}|,
 \quad P(Z)=\prod_{\tau\in\Phi'}p_{\nu_{0,\tau}}(Z_\tau).
 \tag{R12.2}
\]
Here each highest polynomial is the primitive bideterminant of
AM-R-011. The actual source compact type of the oscillator is
\(\sigma=\rho_0^\vee\), and the target compact type is
\(\rho_1\), where \(\rho_j\) has highest weight \(w_j\).
This is precisely the equal-character identification proved in
AM-DO-025, not the trivial-character rank-two special case.

There is an explicit globally admissible common character with
the required exponents \(-e_{0,\tau}\). Indeed AM-R-009 proves
\(T'(\mathbf A_f)=T'(F')K_{T,0}\), with intersection
\(\mu_{28}\). On the real norm-one torus set
\(\beta(t)=\prod_\tau t_\tau^{-e_{0,\tau}}\).
At one split place over29 choose the factor where
\(\zeta_{28}\mapsto2\), and define the compact residue character
\[
 \varrho(2)=\exp\!\left(\frac{2\pi i}{28}
                         \sum_{\tau\in\Phi'}e_{0,\tau}\tau\right).
 \tag{R12.3}
\]
It is trivial at every other compact place. Thus
\(\varrho|_{\mu_{28}}=\beta^{-1}\), so
\(\beta\varrho\) descends to a unitary automorphic norm-one
character \(\gamma\). Put \(\mu(x)=\gamma(x/\bar x)\).
Then \(\mu|_{\mathbf A_{F'}^\times}=1\),
\(\mu_\infty(z)=(z/\bar z)^{-e_{0,\tau}}\), and the
finite compact conductor divides29. Take
\(\chi_S=\chi_T=\mu\) on the edge. At nonsplit finite places
the norm-one group is compact and \(\gamma\) is trivial there;
at other split places it is unramified. All values needed for
the algebraic finite kernel lie in a finite algebraic coefficient
extension. This is the explicit character construction of
AM-R-009 applied to the present integral exponent vector.

Choose
\[
 e=\max\{1,\lceil\log_{29}(3D+2)\rceil\},\qquad M=29^e.
 \tag{R12.4}
\]
By AM-K022, after a fixed unramified coefficient extension at11,
one can choose a **single** permitted product-translate \(x\)
such that its normalized geometric jet \(a_x\) satisfies
\[
 a_x\ne0,\qquad
 v_{11}(a_x)\le
       B_\nu:=\sum_{\tau\in\Phi'}\sum_{i=1}^{a}
                              v_{11}(\nu_{0,\tau,i}!).
 \tag{R12.5}
\]
The integer in the bound is the derivative of the diagonal
monomial in \(P\); it is not the hook product and not an
unproved lower bound for every selected jet. The translate belongs
to the actual DP59 half-orbit after its specified odd-level
normalization. The corresponding finite Schwartz vector is
\(\phi_{f,x}=W_x\phi_0\) with its actual central multiplier,
and \(\|\phi_{f,x}\|=1\) by unitarity. No interpolation
coefficient norm is hidden in this selection of one orbit vector.

Let \(\phi_x=r_P\phi_{f,x}\phi_\infty\). The actual kernel
identity AM-DO-026, with the normalized level factors retained,
gives
\[
                  \vartheta_{\phi_x}(1,1)=C^{2ab}a_x\ne0.
 \tag{R12.6}
\]

## 2. A concrete source level and its exact identity-class mass

Let \(K_{a,0}\) be the standard full integral unitary compact.
Refine it to \(K_a(M)\) by principal congruence modulo29^e at
all six split places over29, leaving all other places unchanged.
Then \(K_a(M)\) fixes \(\phi_{f,x}\) exactly in the source
action. The same assertion holds for the target subgroup \(K_b(M)\).

To see this, at29 every permitted parameter has denominator
dividing \(M\) and lies in the selected isotropic split position
space. The linear action \(X\mapsto hXg^{-1}\) preserves that
position space. For \(g,h\equiv1\pmod M\), its displacement
is integral in the same space. The pairing with the original
parameter is zero, and the odd-place trace-one lattice character
of that displacement is one. The exact Weyl law therefore fixes
\(W_x\phi_0\). The compact determinant characters also equal
one on this level by (R12.3). Away from29 the parameter is
integral; the line is the original trace-one vacuum line, fixed
by the standard compacts and the unramified splitting. These are
exactly the split/unramified normalizations of AM-DO-022 and the
isotropic half-orbit argument of AM-R-010, now applied entrywise
to the matrix Hom space.

At the identity finite class the rational stabilizer is trivial:
\[
                   \Gamma=G(F')\cap K_a(M)=\{1\}.
 \tag{R12.7}
\]
First \(\Gamma\) is finite, because it preserves the integral
lattice and lies in a compact group at infinity. Its image at
one split place over29 is inside \(1+29M_a(\mathbf Z_{29})\),
which is torsion free. For completeness, if a nonzero matrix
\(B\) has minimum entry valuation \(s\ge1\), then
\((1+B)^{29}-1\) has minimum valuation exactly \(s+1\):
the term \(29B\) has that valuation, and all the other terms
have strictly larger valuation. Raising to an integer prime to29
leaves the minimum valuation \(s\). A finite-order element in
this group would therefore remain nonidentity after raising to
its order, a contradiction. The local embedding of the rational
matrix group is injective, proving (R12.7).

Normalize real Haar measure to have \(\operatorname{vol}(G_\infty)=1\),
and finite Haar measure by \(\operatorname{vol}(K_{a,0})=1\).
Use their compatible automorphic quotient measure; its total
volume is not silently set to one. The exact index and the
identity-class mass are
\[
 \begin{aligned}
 I_a(M)&=[K_{a,0}:K_a(M)]
       =29^{6a^2(e-1)}|\mathrm{GL}_a(\mathbf F_{29})|^6\\
       &=M^{6a^2}\prod_{i=1}^{a}(1-29^{-i})^6,
       \qquad w=I_a(M)^{-1}.
 \end{aligned}
 \tag{R12.8}
\]
The split reduction maps are surjective, with successive
congruence quotients of cardinality \(29^{a^2}\).
Counting ordered bases gives
\(|\mathrm{GL}_a(\mathbf F_{29})|=29^{a^2}\prod_i(1-29^{-i})\).
There are six places, and (R12.7) removes the stabilizer divisor
at this class. This proves (R12.8) with the actual chosen measure.

## 3. Compact matrix-coefficient extraction

Use the standard unitary metrics on the compact representations,
with highest vector of norm one. Let \(u\in\sigma\) be the
unit source vector corresponding to the source factor of the
highest polynomial \(P\), and put
\[
 d_\rho=\dim\rho_0=\dim\sigma,
 \qquad m(k)=\langle u,\sigma(k)u\rangle.
 \tag{R12.9}
\]
The Hermitian convention is conjugate-linear in the first
argument. At the identity finite class, the kernel can be written
\[
             \vartheta_{\phi_x}(k,1)=L(\sigma(k)u),
             \qquad L(u)=C^{2ab}a_x,
 \tag{R12.10}
\]
where the scalar relating the actual highest polynomial to unit
Schur vectors is included in \(L\). This is the actual source
equivariance of the theta kernel; its finite translate acts on a
different tensor factor and does not change the compact type.

Define an automorphic function \(f_0\) supported on the identity
finite class, whose value there is \(\overline{m(k)}\), and
whose value on all other finite classes is zero. Equation
(R12.7) makes this definition unambiguous. It is right
\(K_a(M)\)-invariant and smooth at infinity, with right compact
type \(\sigma^\vee=\rho_0\). This gives an actual automorphic
input, rather than a free representation parameter. It is
cuspidal because the definite rational group has no proper
rational parabolic subgroup.

Schur orthogonality, or the average of the rank-one projection
\(v\mapsto u\langle u,v\rangle\), gives
\[
 \int_{G_\infty}\sigma(k)u\overline{m(k)}\,dk
                      =u/d_\rho,
 \qquad \int_{G_\infty}|m(k)|^2\,dk=1/d_\rho.
 \tag{R12.11}
\]
Insert this into the literal **bilinear** theta integral, and
use the mass \(w\) of the supporting class. One obtains the
exact nonzero value and norm
\[
 \boxed{\Theta^{\rm bil}_{\phi_x}(f_0)(1)
        =\frac{C^{2ab}a_x}{I_a(M)d_\rho},\qquad
        \|f_0\|_2^2=\frac1{I_a(M)d_\rho},\quad
        \|f_0\|_\infty=1.}
 \tag{R12.12}
\]
The supremum is attained at the real identity. In the integral
coefficient presentation this is a class vector with primitive
highest coefficient: the highest-to-highest matrix coefficient
is the primitive bideterminant with the integral determinant
character attached, as in AM-R-011. Its value at the identity
is one. No claim that all scalar values on the real compact
group are algebraic integers is needed or intended.

Two useful alternative normalizations are consequently
\[
 \begin{array}{c|c|c}
 \text{input}&\text{squared norm}&\text{output at 1}\hline
 I_a(M)d_\rho f_0&I_a(M)d_\rho&C^{2ab}a_x\\
 \sqrt{I_a(M)d_\rho}\,f_0&1&C^{2ab}a_x/\sqrt{I_a(M)d_\rho}.
 \end{array}
 \tag{R12.13}
\]
Thus the source normalization cost for the extracting input is
exactly \(\tfrac12\log(I_a(M)d_\rho)\). It has not been
removed by using a nonprimitive scalar multiple of the row.

The compact dimension is explicitly
\[
 d_\rho=\prod_{\tau\in\Phi'}\prod_{1\le i<l\le a}
      \frac{\eta_{0,\tau,i}-\eta_{0,\tau,l}+l-i}{l-i}.
 \tag{R12.14}
\]
With fixed ranks and \(M<29(3D+2)\), the logarithmic source
cost is \(O(\log(D+2))\), with the exact finite index given
in (R12.8), rather than an unspecified level constant.
The full archimedean Schwartz norm is (R11.14), and the finite
Schwartz norm is one. Unit normalization of both input and
Schwartz vector therefore divides (R12.6) by
\(\sqrt{I_a(M)d_\rho}\,\|\phi_{x,\infty}\|\).

The normalized algebraic identity coefficient in the primitive
row convention has the controlled upper valuation
\[
 v_{11}\!\left(C^{-2ab}\Theta^{\rm bil}_{\phi_x}(f_0)(1)\right)
          \le B_\nu-v_{11}(I_a(M)d_\rho).
 \tag{R12.15}
\]
This is a selected nonzero entry, not a lower content bound for
every entry of an arithmetic row map. It is therefore not itself
the gain \(g_0\) in DP44.

## 4. A selected first coefficient with no positive 11-adic gain

For the `HCParam` example in AM-R-011, take the same parameters at
all six CM places. Then \(a=6,b=20\),
\(\nu_{0,\tau}=(1^6)\), \(\eta_{0,\tau}=0\),
\(D=36\), \(d_\rho=1\), and the explicit choice (R12.4) is
\(M=29^2=841\). The polynomial is the product of six
six-by-six determinants, and \(B_\nu=0\).

Furthermore
\[
 I_6(841)=29^{216}|\mathrm{GL}_6(\mathbf F_{29})|^6,
                         \qquad v_{11}(I_6(841))=0.
 \tag{R12.16}
\]
Indeed the order of29 modulo11 is10: \(7^5=-1\) modulo11,
while \(7\) and \(7^2\) are not one. None of
\(29^i-1\), \(1\le i\le6\), is divisible by11.
Equations (R12.5), (R12.12) and (R12.16) therefore give an
actual permitted first lift for which
\[
 v_{11}\!\left(C^{-240}\Theta^{\rm bil}_{\phi_x}(f_0)(1)\right)
                                  \le0.
 \tag{R12.17}
\]
Thus a strictly positive uniform 11-adic content for all these
allowed selected first coefficients would be false. The statement
is an upper bound; equality zero would additionally require
integrality of all the relevant reduced jet coefficients. Neither
that extra integrality nor the further noncompact `Hyp3`
conditions are assumed in this example.

Its exact archimedean Schwartz norm is
\[
 \|\phi_{x,\infty}\|^2
       =\det(2Y)^{-120}(6!)^6
                    \prod_{i=1}^{3}\left(\frac{\pi}{2G_i}\right)^{12}.
 \tag{R12.18}
\]
The primitive scalar input has squared norm \(I_6(841)^{-1}\).
All these quantities belong to the same actual first edge.
They do not bound the gains of the later restricted image or
the rebuilt-family DP44 difference.

## 5. What has and has not been supplied

The construction supplies one actual first edge at the source's
even ranks with its selected local types, a globally admissible
equal character, one permitted finite input of norm one, a
specific class-supported source function, and an exact nonzero
value up to the explicitly chosen algebraic jet \(a_x\). The
finite selection can be made deterministic by ordering the finite
permitted orbit and choosing the first tuple with the valuation
bound (R12.5). No search over an infinite Schwartz space is
required for this first edge.

It does not prove that every source row survives, or that the
resulting vector survives the next prescribed kernel. It does
not replace the old elliptic `HostRaw`/`StdPair` by definition,
identify the independently fixed arithmetic `rowAF`, or verify
the noncompact analytic assumptions in `AdmS`. Those are still
needed for the requested shorter chain and the DP44 comparison.
The exact first value, norms and index above are available for
that next step, without the previous rank-one starting mismatch.

Geometrically, the permitted translates are sections in the
Picard/theta-group construction, and (R12.5) is finite-jet
separation on the good integral model. The compact coefficient
is a Schur functor over \(\mathbf Z\), with the rational
class-function realization retaining its actual metric. The
relevant locators are FGA232 Theorem3.1; FGA236 Corollaries1.7
and2.3; SGA7 I VII2.7/2.9; EGA IV4 section16 on principal
parts; SGA3 I Proposition4.7.3 and SGA6 V/VI as qualified in
the geometric dictionary. No new crystalline or motivic
L-function implication is asserted by this first lift.

Exact carried inputs: DP56--59; AM-K022; AM-DO-022,
AM-DO-025 and AM-DO-026; AM-R-009--011. The source bilinear
integral is `WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`,
`liftT_apply`, lines160--167. The selected weights are
`Columns/BaseLemmas.lean`, `lamTrue_old`, `lamTrue_new`,
and `nuW_eq_true`, lines496--552. The source row normalization
is `DataCoeff.lean`, `normFock`, lines83--84. No Lean build
or formal source-record instantiation is claimed.
