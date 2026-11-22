# ALP_MACHINE: lift accounting and explicit CM metric calculations

Author: /root/lift_accounting, GPT-6 Astra Pro. Reasoning effort: not exposed.
Started 2026-11-21 19:35 UTC. This working contribution is not a resolution of
DP_MULT Q3e. Accepted DP findings are cited and are not re-proved.

The later, complete companion findings are:

* `hodge_lattice_and_cm_basis.md`: ALP-LIFT-05, the actual stable Hodge
  lattices at 2 and 7, full determinant metric/height, and a primitive
  induced CM eigenbasis with Gram matrix \(G_B I\).
* `directional_budget_cancellation.md`: ALP-LIFT-06, the exact
  directionwise prime constants and the arbitrary-order-vector
  cancellation against the actual diagonal Cauchy cost.
* `finite_theta_null_normalization.md`: ALP-LIFT-07, the exact finite
  theta-null normalization, explicit zero characteristic, trace-one
  principal line and the surviving two-torsion difference at source
  odd levels.
* `trace_one_leading_jet.md`: ALP-LIFT-08, the unique actual trace-one
  section with leading jet \(u_1u_3-u_2^2\), primitive at every
  \(p\nmid14\), and its complete finite scalar contents at 2 and 7.

* `actual_torus_first_lift.md`: ALP-LIFT-09, the norm-one torus
  class calculation, an explicit honest global splitting, actual
  nonzero first U(1) to U(2) theta lift, and the exact finite-index
  cost of a common fixed-weight first-image projector.

* `permitted_orbit_first_image.md`: ALP-LIFT-10, the exact DP59
  half-torsion finite-input family, common actual first-lift input,
  exact index/norm and exceptional-prime projection costs. AM-K018
  closes the ordinary-power source gauge; explicit DP59 harmonic
  sharp values now occur in an actual first image. Ordinary
  mixed-line values use a separate multiweight projector.

* `fixed_conductor_type_repair.md`: ALP-LIFT-11, an explicit
  global torus character with arbitrary integral infinity type
  and fixed conductor29, its exact determinant twist of the
  actual first lift, and removal of the specified next-edge
  real-type obstruction. Its fixed bilinear repair works for
  all degrees; the common source-character pins remain separate.

* second_definite_lift_nonvanishing.md: ALP-LIFT-12, an actual
  nonzero U(2) to U(4) lift of every nonzero repaired first-image
  vector, including automorphic multiplicities. The proof checks
  all finite local occurrence, the explicit compact-real Rallis
  factor, and absolute nonvanishing of the standard L-value.
  AM-R009 gives the concrete same-host corollary over E-prime.
  The second Schwartz function is unrestricted; its prescribed
  arithmetic row and cost data are not constructed.

* fixed_section_sharp_first_images.md: ALP-LIFT-13, actual
  sharp first-image coefficients at3 and5 from the single
  fixed section in AM-K020. One fixed finite vacuum and
  one unit-norm source character realize every nonzero
  witness; the exact Fock norm and common period are retained.

`cmdata_theta_constructor_audit.md` records the directly checked input
and output of the generic six-identity constructor. Its principal
distinction is already accepted DP52 background, not a new finding.

Each companion proof has been read in full and its actual checks are
recorded in `lift_accounting_CHECK_EVENTS.tsv`. None identifies the
complete selected `SizeData₂` or constructs the requested lift chain.

## 1. Source boundary and the actual cost variables

The attached DP_MULT return contains the paper, proof snapshots and manifests,
but no raw Lean modules. The present run recovered the pinned mirror modules
listed in lift_sources/FETCH_MANIFEST.json. Their hashes are compared separately
with the intake's original-author manifest; a source read is not a Lean build.

The exact primary declarations are:

* Formalism/LocalRingCardinality/DataParams₂.lean, SizeData₂, lines 79–183:
  the fields gain, F, E, tau, supp, aT, logDerivativeAtOne and the size windows.
* The same file, sz, gainD, Ga, Ee, logOm and MAIN, lines 203–234.
* Formalism/LocalRingCardinality/DataHost.lean, rdE and v, lines 140–145:
  \(v=\operatorname{rd}(E)/2\), not \(\sqrt d/2\).
* Formalism/SharpRestriction/GlobalTheoremInputs.lean, LinkDIV_at,
  lines 77–89; flG, loG, LinkG_at, lines 100–136.
* Formalism/LocalRingCardinality/SpanPowerMembership/NZRowAsm.lean,
  ExtraNZIn, lines 61–86.

In particular, a Jacobian, a prime, a CM type and an admissible Ranks record
do not determine numerical gain or error fields. The two-sided LinkG_at
conditions include the coarse bound
\[
 0\le {\rm gain}_{j,w}\le
 4\,|{\rm TT}|\,a/p,
\]
as well as the lower ramplike certificate. The latter is not an equality.
LinkDIV_at controls each \(e_j\) within \(C B_0\) of
\[
 \left(\sum_t A_t\right)\log(g(0)g(1)).
\]
Its actual value still depends on the selected geometric and integral data.
The exact period scalar of the old field package is
\[
 \log\Omega=
 \gamma+\log(2\pi)-\log\operatorname{rd}(E)
 -\frac{L'(1,\chi_K)}{L(1,\chi_K)}.
 \tag{L0}
\]
Consequently the old \(H\), before any mixed-type replacement, is
\[
 H=\sum_t A_t\left[
 \log A_t-1-\gamma-\log(2\pi)+\log\operatorname{rd}(E)
 +\frac{L'(1,\chi_K)}{L(1,\chi_K)}
 \right].
 \tag{L1}
\]
This is an exact substitution in source definitions, not a value of a newly
constructed mixed theta family.

DP44 and DP52 already settle rank reconstruction, the generic Hermitian
spaces, the conditional six-identity induction and the endpoint-period
interface. DP65 supplies actual CM-labelled local rows, but explicitly does
not supply one SizeData₂ package or membership in a prescribed theta image.
Its final statement must not be substituted for either of those missing
identifications.

## 2. ALP-LIFT-01: the comparison for two rebuilt families

Let the old family have length \(M\), and the new family length \(M'<M\).
Primes, fields and norms may differ; define their scalar totals separately:
\[
 Q_M=\sum_{j=1}^{M}(g_j-e_j)-T_\tau-MH+K,\qquad
 Q'_{M'}=\sum_{j=1}^{M'}(g'_j-e'_j)-T'_\tau-M'H'+K'.
\]
No identification of local place sets is needed to compare these real
numbers. Then
\[
\begin{split}
 Q'_{M'}-Q_M={}&-\sum_{j=M'+1}^{M}(g_j-e_j-H)\\
 &+\sum_{j=1}^{M'}[(g'_j-g_j)-(e'_j-e_j)]\\
 &+(T_\tau-T'_\tau)+(K'-K)+M'(H-H').
\end{split}
\tag{L2}
\]
If an additional allowance is subtracted, the right side acquires
\(B_M-B'_{M'}\).

**Proof.** Split the old gain and error sums at \(M'\), subtract the two
definitions, and use
\(MH-M'H'=(M-M')H+M'(H-H')\).
This accounts for every displayed term and proves (L2). Adding the allowance
is direct subtraction. No positivity assertion is used. \(\square\)

When the retained data and all global terms are equal, (L2) is precisely
DP44.3. For a genuinely changed CM type it is the second through fourth
lines, rather than the deleted tail alone, that must be computed as well.
Moreover, \(Q'_{M'}<Q_M\) alone would not prove failure of a global threshold
condition: both quantities could exceed that threshold. This last observation
is elementary logic about inequalities; it is not an example of an admissible
geometric family.

## 3. ALP-LIFT-02: exact stable CM-height penalty for the proposed Jacobian

Put \(E=\mathbb Q(\zeta_7)\), \(K=\mathbb Q(\sqrt{-7})\). Let \(J\) have its
actual integral CM action of type \(\Phi=\{1,2,3\}\), as in DP22 and DP49.
Choose a CM elliptic curve \(B\) with full ring \(\mathcal O_K\), and define
\[
 A_{\mathrm{ind}}=\mathcal O_E\otimes_{\mathcal O_K} B
\]
using the embedding of \(K\) for which the induced type is
\(\Psi=\{1,2,4\}\). In any common standard normalization of stable Faltings
height for three-dimensional abelian varieties,
\[
\boxed{\;
 h_F(J)-h_F(A_{\mathrm{ind}})
 =\log\frac{\Gamma(2/7)\Gamma(4/7)^3}
                  {\Gamma(3/7)^3\Gamma(5/7)}
 =:\delta_7>0.\;}
\tag{L3}
\]
The exact rational computation accompanying this proof certifies
\[
       0.05568702<\delta_7<0.05568705.
\tag{L4}
\]
The higher precision decimal \(0.0556870335243028288211564027305\ldots\)
is a numerical cross-check, not the rational certificate.

### Proof: integral comparison variety

Let \(S=\zeta_7+\zeta_7^2+\zeta_7^4\), \(T=-1-S\). The roots
\(\zeta_7,\zeta_7^2,\zeta_7^4\) give
\[
 \zeta_7^3-S\zeta_7^2+T\zeta_7-1=0.
\]
Since \(\mathcal O_K=\mathbb Z[S]\), \(\mathcal O_E=\mathbb Z[\zeta_7]\),
and \([E:K]=3\), the elements \(1,\zeta_7,\zeta_7^2\) are an
\(\mathcal O_K\)-basis of \(\mathcal O_E\). The Serre tensor construction
therefore identifies \(A_{\mathrm{ind}}\) with \(B^3\) as an abelian variety
(over a common field of definition), not merely up to isogeny. Thus
\(h_F(A_{\mathrm{ind}})=3h_F(B)\). The \(\mathcal O_E\)-action has exactly
the embeddings extending the chosen \(K\)-embedding, namely \(\Psi\).
No isogeny-invariance assertion for general Faltings heights is being used.

### Proof: the normalized Colmez class function

Let \(\sigma=\sigma_3\) generate \({\rm Gal}(E/\mathbb Q)\), and let
\(\chi(\sigma)=\exp(2\pi i/6)\). Then \(\chi^3=\chi_{-7}\), and the
exponent sets of \(\Phi\) and \(\Psi\) are respectively \(\{0,1,2\}\) and
\(\{0,2,4\}\).

Use Haar probability measure in convolution:
\[
 A_\Phi=\mathbf1_\Phi*\mathbf1_{\Phi^{-1}}.
\]
For \(\sigma^k\), \(k=0,\ldots,5\), its values are
\[
 (1/2,\,1/3,\,1/6,\,0,\,1/6,\,1/3).
\]
The corresponding induced-type values are
\((1/2,0,1/2,0,1/2,0)\). Discrete Fourier expansion gives
\[
 A_\Phi=\frac14\mathbf1+
             \frac19(\chi+\bar\chi)+\frac1{36}\chi^3,\qquad
 A_\Psi=\frac14\mathbf1+\frac14\chi^3.
\tag{L5}
\]
These expansions can also be checked at the six group elements, using
\(\chi+\bar\chi=(2,1,-1,-2,-1,1)\) and
\(\chi^3=(1,-1,1,-1,1,-1)\).

The abelian Colmez theorem applies to both integral CM types. Its
normalization is explicit in Yang (2010), Section 3, pp. 464–466,
Conjecture 3.1 and the elliptic example (3.3); the abelian case is supplied
by Colmez (1993), Théorème 0.5 and Théorème III.2.9, with the possible
dyadic ambiguity removed by Obus (2013), Theorem 3.9 in arXiv:1107.0684v2. Write
\(Z_\eta=L'(0,\eta)/L(0,\eta)\). In the difference, the trivial character
and metric constants cancel. All three nontrivial characters here have
conductor \(7\), and their coefficient difference sums to zero. The
conductor term therefore cancels as well. Multiplication by \([E:\mathbb
Q]=6\), which converts the type-normalized height to the actual
three-dimensional height, gives
\[
 h_F(J)-h_F(A_{\mathrm{ind}})
   =-\frac23(Z_\chi+Z_{\bar\chi}-2Z_{\chi^3})
   =\frac43(Z_{\chi^3}-\operatorname{Re}Z_\chi).
\tag{L6}
\]

### Proof: reduction to gamma values

For any nontrivial Dirichlet character \(\eta\) modulo \(7\), the Hurwitz
formula, together with DLMF 25.11.13 and 25.11.18, gives
\[
 L(0,\eta)=-\frac17\sum_{a=1}^{6}a\eta(a),\qquad
 L'(0,\eta)=-\log7\,L(0,\eta)+
                 \sum_{a=1}^{6}\eta(a)\log\Gamma(a/7).
\tag{L7}
\]
Here the constant from \(\zeta'(0,x)=\log\Gamma(x)-\tfrac12\log(2\pi)\)
vanishes because the character sum is zero.

Put \(\ell_a=\log\Gamma(a/7)\).
The character values give \(L(0,\chi^3)=1\) and
\[
 L(0,\chi)=\frac{4+2\sqrt3\,i}{7},\qquad
 L(0,\chi)^{-1}=1-\frac{\sqrt3}{2}i.
\]
Consequently
\[
 Z_{\chi^3}=-\log7+\ell_1+\ell_2-\ell_3+\ell_4-\ell_5-\ell_6
\]
and
\[
 \operatorname{Re}Z_\chi=
 -\log7+\ell_1+\frac14\ell_2+\frac54\ell_3
                    -\frac54\ell_4-\frac14\ell_5-\ell_6.
\]
Substitution in (L6) proves the equality in (L3).

### Proof: strict sign and exact rational certificate

Let \(f(x)=\log\Gamma(x)\), \(h=1/7\). The expression in (L3) is
\(-\Delta_h^3 f(2/7)\). By differentiating DLMF 5.15.1,
\[
 f'''(x)=-2\sum_{n\ge0}(n+x)^{-3}<0 \quad(x>0).
\]
Repeated integration of a finite difference therefore gives
\[
 \delta_7=-\int_{[0,h]^3} f'''(2/7+s+t+u)\,ds\,dt\,du>0.
\]
This proves the strict sign without numerical approximation.

For a reproducible rational bound, the Weierstrass product (or the same
integral identity after integration term by term) yields
\[
 \delta_7=\sum_{n=0}^{\infty}
 \log\frac{(7n+3)^3(7n+5)}{(7n+2)(7n+4)^3}
 =\sum_{n=0}^{\infty}\log(1+x_n),
\quad
 x_n=\frac{14n+7}{(7n+2)(7n+4)^3}.
\]
For \(t=x/(2+x)\), the six-term sum
\[
 2\sum_{k=0}^{5}\frac{t^{2k+1}}{2k+1}
\]
is a lower bound on \(\log(1+x)\); the omitted positive tail is at most
\(2t^{13}/(13(1-t^2))\). Bound the first \(100\) terms with exact
fractions. Each remaining logarithm is a third finite difference of
\(\log x\), and lies between
\(2/(7n+5)^3\) and \(2/(7n+2)^3\). Integral comparison bounds the tail
starting at \(N=100\) between
\[
 \frac1{7(7N+5)^2},\qquad \frac1{7(7N-5)^2}.
\]
The script colmez_height_certificate.py implements exactly these rational
inequalities and verifies (L4). This completes the proof. \(\square\)

### Independent normalization cross-check against Wilms

In Yang's height convention, (L5) gives
\[
 h_F^Y(J)=-\frac43\operatorname{Re}Z_\chi
               -\frac16Z_{\chi^3}-\frac34\log7
          =-2.0840659166599491401\ldots,
\]
\[
 h_F^Y(A_{\mathrm{ind}})
          =-\frac32Z_{\chi^3}-\frac34\log7
          =-2.1397529501842519690\ldots.
\]
Wilms (2026), Theorem 1.1, specialized to \(n=7,g=3\), gives
\[
 h_F^W(J)=\log7-\frac32\log\pi+\frac3{14}\log2
     -\sum_{j=1}^{3}
       \log\frac{\Gamma((2j-1)/14)}{\Gamma((j+3)/7)}.
\tag{L8}
\]
His Section 7, pp. 12–13, explicitly records the normalization
\(h'_F=h_F^W+(g/2)\log\pi\). The duplication formula and
\(\prod_{a=1}^6\Gamma(a/7)=(2\pi)^3/\sqrt7\) show algebraically that
(L8) equals \(h_F^Y(J)-(3/2)\log\pi\).
The independent numerical evaluation is
\(-3.8011607454340494014\ldots\). This check catches the degree-six,
dimension-three and metric factors; it is not used to prove (L3).

### Exact implication and limit

The actual Jacobian has a strictly larger base CM stable height than the
specified integral induced-type product. Thus replacing that product by J
does not provide a free saving in this complete invariant of the base
Hodge determinant. It does not follow that \(H'\ge H\): the source's \(H\)
also incorporates a particular derivative normalization, root
discriminant, unequal embedding weights, gauges and other fields.
The identification of that source metric with this determinant line is a
separate equation that must be proved in a mixed-type construction.
There is no asserted sign for \(Q'_{M'}-Q_M\).

In Grothendieck's language, (L3) compares the arithmetic degrees of the
metrized determinants of the Hodge bundles \(e^*\Omega^1_{\mathcal J}\)
and \(e^*\Omega^1_{\mathcal A_{\mathrm{ind}}}\) on a common semistable
integral base. The CM idempotents are those acting on the \(H^1\) motive;
(L5) is the explicit Artin-character expression entering its period
height. FGA's Picard-scheme theorem supplies the Jacobian, as already
used in DP22; the exact FGA locators are carried from that finding.
No new manuscript cote or scan is asserted to contain the Colmez formula.

## 4. ALP-LIFT-03: full complex Hodge metric in the actual CM basis

For \(C:y^2=x^7-1\), put \(\omega_i=x^{i-1}dx/y\) for \(i=1,2,3\).
Equip \(H^0(C,\Omega^1)\) with
\[
 (\omega,\eta)=\frac{i}{2}\int_{C(\mathbb C)}\omega\wedge\bar\eta.
\]
Then
\[
 (\omega_i,\omega_j)=0\quad(i\ne j),\qquad
\boxed{\;
 \|\omega_i\|^2=\frac{2\pi}{7}
 \frac{\Gamma(i/7)\Gamma(1/2-i/7)}
      {\Gamma(1-i/7)\Gamma(1/2+i/7)}.\;}
\tag{L9}
\]
The norm squares are approximately
\(9.47604253508638,\ 8.00728744152725,\ 15.34580357802465\).

**Proof.** The automorphism \(x\mapsto\zeta_7 x\) preserves the integral
and multiplies \(\omega_i\wedge\bar\omega_j\) by
\(\zeta_7^{i-j}\). For \(i\ne j\) this scalar is not one, proving
orthogonality. Branch points have measure zero. Over the affine line,
the map from C has degree two and the two sheets contribute equally, so
\[
 \|\omega_i\|^2=
 2\int_{\mathbb C}
       \frac{|x|^{2i-2}}{|x^7-1|}\,dA(x).
\]
Substitute \(z=x^7\), accounting for its degree seven and Jacobian
\(49|x|^{12}\). The expression becomes
\[
 \frac27\int_{\mathbb C}|z|^{2a-2}|1-z|^{-1}\,dA(z),
 \qquad a=i/7.
\tag{L10}
\]
For \(a,b>0\) and \(a+b<1\), the complex beta integral is
\[
 \int_{\mathbb C}|z|^{2a-2}|1-z|^{2b-2}\,dA(z)
 =\pi\frac{\Gamma(a)\Gamma(b)\Gamma(1-a-b)}
            {\Gamma(1-a)\Gamma(1-b)\Gamma(a+b)}.
\tag{L11}
\]
For completeness, write each negative power as its positive gamma
integral, apply Tonelli, and integrate the Gaussian in z:
\[
 \frac{\pi}{\Gamma(1-a)\Gamma(1-b)}
 \int_{s,t>0}\frac{s^{-a}t^{-b}}{s+t}
                  e^{-st/(s+t)}\,ds\,dt.
\]
With \(s=uv,t=u(1-v)\), this becomes
\[
 \frac{\pi\Gamma(1-a-b)}{\Gamma(1-a)\Gamma(1-b)}
 \int_0^1 v^{b-1}(1-v)^{a-1}\,dv.
\]
The ordinary beta identity proves (L11). All changes of variables are
valid on positive integrands; the stated inequalities give convergence.
Set \(b=1/2\) in (L11) and substitute into (L10). This proves (L9).
\(\square\)

This supplies the full complex metric for arbitrary unequal embedding
weights once the geometric differential basis is tied to the chosen
theta connection and source gauge. It does not remove that tie or the
integral corrections at 2 and 7. In particular the Hodge norms are not
silently declared to be the source's \(\Omega\).

Geometrically, (L9) gives the Hermitian metric on the Hodge subbundle of
the de Rham realization of \(h^1(J)\), split by the \(\mathcal O_E\)
idempotents. Its dual metric controls invariant tangent derivations.
The connection to the Poincaré biextension and its theta sections still
requires the arithmetic comparison asked for in THETA3 G1.

## 5. ALP-LIFT-04: the exact constant in the saturated bare-budget difference

This result uses the accepted DP64 definition (CB1); it does not repeat
the cyclic-display or global-integrality proofs behind that definition.
It determines the linear term left undetermined by DP64's general
\(O(N)\) comparison for this particular pair of types and equal orders.

Continue with \(\Phi=\{1,2,3\}\), \(\Psi=\{1,2,4\}\). For a rational
prime \(p\ne7\), define the **formal slope totals**
\[
 S_\Phi(p)=\sum_{i\in\Phi}\sum_{r\ge1}
       \frac{\mathbf1_{p^r i\notin\Phi}}{p^r},\qquad
 \Delta S(p)=S_\Phi(p)-S_\Psi(p),
\]
where labels are multiplied modulo 7. Let \(S\) be a fixed finite set of
primes containing 7. Set
\[
 \delta_{7,S}=\delta_7-
       \sum_{p\in S\setminus\{7\}}\Delta S(p)\log p.
 \tag{L12}
\]
Then the following are exact statements about these explicitly specified
arithmetic certificates:

1. The local difference is
   \[
   \boxed{\quad
   \Delta S(p)=
   \begin{cases}
   \displaystyle\frac{2p(p+1)}{p^3-1},&p\equiv2,4\pmod7,\\[4pt]
   \displaystyle-\frac{2p(p-1)}{p^3+1},&p\equiv3,5\pmod7,\\[4pt]
   0,&p\equiv1,6\pmod7.
   \end{cases}\quad}
   \tag{L13}
   \]
2. In ordinary increasing rational-prime order,
   \[
   \boxed{\quad
   \lim_{X\longrightarrow\infty}
     \sum_{\substack{p\le X\\p\notin S}}
            \Delta S(p)\log p=\delta_{7,S}.
   \quad}
   \tag{L14}
   \]
   This convergence is conditional. No rearrangement of the primes is
   authorized by (L14).
3. Put equal derivative order \(n\) on each of the three CM directions
   in both types, and use the DP64 integer certificates
   \[
   D_S(n)=\sum_{p\notin S}\log p
       \left(\sum_{i\in\Phi}E^\Phi_{i,p}(n)
                   -\sum_{i\in\Psi}E^\Psi_{i,p}(n)\right).
   \]
   The sum is finite, since a term can be nonzero only when \(p\le n\).
   For some constants \(c>0,C_S>0\),
   \[
   \boxed{\quad
       D_S(n)=n\delta_{7,S}
                  +O_S\!\left(n e^{-c\sqrt{\log n}}\right)
       \qquad(n\longrightarrow\infty).
   \quad}
   \tag{L15}
   \]
   In particular, with total order \(N=3n\), the exact coefficient of
   \(N\) is \(\delta_{7,S}/3\).
4. The same linear term holds before saturation. If \(D_S(n;X)\)
   denotes the definition of \(D_S(n)\) with \(p\le X\), then, uniformly
   for \(n\ge4\), \(X\ge2\), with some fixed \(c>0\),
   \[
   D_S(n;X)=n\delta_{7,S}
     +O_S\!\left(n e^{-c\sqrt{\log\min\{X,\sqrt n\}}}\right).
   \tag{L15a}
   \]
   Consequently \(D_S(n;X(n))/n\to\delta_{7,S}\) for *every*
   \(n\to\infty\) and \(X(n)\to\infty\), including cutoffs much
   smaller than the derivative order. The three directions still
   have the same order \(n\), fixed as \(p\) varies.

The source-supported common good-model range in DP49/DP64/DP65 excludes
2 and 7. It is therefore the specialization
\[
 \boxed{\quad
 \delta_{7,\{2,7\}}=
       \delta_7-\frac{12}{7}\log2<0,
 \quad}
 \tag{L16}
\]
that applies to that range. The identity with \(\delta_7\) itself uses
the *formal* cyclic slope at 2; it does not assert an available integral
good-model certificate at 2 for the specified curve. Every additional
discarded prime has the explicit correction in (L12). The strict sign
in (L16) follows from (L4) and the elementary inequality
\(\log2>1/2\).

### Proof: exact local class function

For \(a\in(\mathbb Z/7)^\times\), put
\[
 b(a)=\#\{i\in\Phi:ai\notin\Phi\}
                  -\#\{i\in\Psi:ai\notin\Psi\}.
\]
The Haar normalization already checked in (L5) gives
\[
 b(a)=-6(A_\Phi-A_\Psi)(\sigma_a).
\]
Thus \(b(1)=b(6)=0\), \(b(2)=b(4)=2\), and
\(b(3)=b(5)=-2\). Write \(b(0)=0\). The function has mean zero over
the six nonzero residues, and
\[
 b(a)=-6\sum_{\eta\in\{\chi,\bar\chi,\chi^3\}}d_\eta\eta(a),
 \qquad(d_\chi,d_{\bar\chi},d_{\chi^3})=(1/9,1/9,-2/9).
 \tag{L17}
\]
Directly from the DP64 definitions,
\[
 \Delta S(p)=\sum_{r\ge1}\frac{b(p^r)}{p^r}.
 \tag{L18}
\]
For residues 2 or 4 the period-three numerator is \((2,2,0)\), giving
\(2(p^2+p)/(p^3-1)\). For residues 3 or 5 the period-six numerator is
\((-2,2,0,2,-2,0)\). Its rational sum is
\[
 \frac{-2p^5+2p^4+2p^2-2p}{p^6-1}
   =-\frac{2p(p-1)}{p^3+1}.
\]
Residues 1 and 6 give zero at every power. This proves (L13), including
\(\Delta S(2)=12/7\), \(\Delta S(3)=-3/7\), and
\(\Delta S(11)=132/665\).

### Proof: ordinary prime-order convergence and the constant

The known fixed-modulus prime number theorem, as stated in Rudnick
(2015), Section 2, printed p. 2 immediately before equation (1), implies
for some fixed \(c_0>0\)
\[
 B_1(x):=\sum_{p\le x}b(p)\log p
           =O\!\left(xe^{-c_0\sqrt{\log x}}\right).
 \tag{L19}
\]
Indeed the six residue-class main terms cancel because the mean of
\(b\) is zero. Replacing the displayed von Mangoldt sum in that theorem
by its prime-only part changes it by
\(O(\sqrt{x}\log^2x)\), which is absorbed by the stated error after
possibly decreasing \(c_0\). Partial summation now shows convergence of
\(\sum_p b(p)\log p/p\): its tail is at most a constant times
\[
 (1+\sqrt{\log X})e^{-c_0\sqrt{\log X}}.
\]
The contribution of \(r\ge2\) in (L18) is absolutely convergent, since
\[
 \sum_p\log p\sum_{r\ge2}\frac{|b(p^r)|}{p^r}
 \le2\sum_p\frac{\log p}{p(p-1)}<\infty.
\]
This proves the convergence assertion in ordinary prime order before
any use of analytic continuation. Conversely, (L13) and the same
fixed-modulus prime theorem give
\[
 \sum_{p\le X}|\Delta S(p)|\log p
           =\frac43\log X+O(1),
 \tag{L20}
\]
so the series is not absolutely convergent.

For real \(s>1\), the absolutely convergent Euler product, DLMF 25.15.2,
and (L17) give
\[
 \sum_{p\ne7}\log p\sum_{r\ge1}\frac{b(p^r)}{p^{rs}}
       =6\sum_\eta d_\eta\frac{L'(s,\eta)}{L(s,\eta)}.
 \tag{L21}
\]
The left side tends as \(s\downarrow1\) to the ordinary prime sum just
proved convergent. To justify the passage without a Tauberian premise,
apply partial summation to (L19): the prime, first-power part is an
integral with integrand bounded, uniformly for \(1\le s\le2\), by a
constant times \(e^{-c_0\sqrt{\log x}}/x\), which is integrable at
infinity. The higher-power part admits the absolute majorant above.
Dominated convergence therefore applies. Nonvanishing of the three
\(L(1,\eta)\) is the classical Dirichlet nonvanishing theorem
(DLMF 25.15.9).

All three characters are odd, primitive and of conductor 7. The
functional equation (DLMF 25.15.5), logarithmically differentiated at
\(s=1\), yields
\[
 \frac{L'(0,\eta)}{L(0,\eta)}
   +\frac{L'(1,\bar\eta)}{L(1,\bar\eta)}
       =\gamma+\log(2\pi/7).
 \tag{L22}
\]
For clarity, in the DLMF normalization the sine factor has logarithmic
derivative \((\pi/2)\cot(\pi s/2)=0\) at 1, while
\(\Gamma'(1)/\Gamma(1)=-\gamma\); the Gauss sum is constant. The
conjugate in (L22) is essential. Since the \(d_\eta\) are
conjugation-invariant and sum to zero, (L21) at 1 equals
\[
 6\sum_\eta d_\eta\frac{L'(1,\eta)}{L(1,\eta)}
 =-6\sum_\eta d_\eta\frac{L'(0,\eta)}{L(0,\eta)}
 =\delta_7,
\]
where the last equality is the already-proved (L6). Removing the fixed
finite set of prime summands proves (L12) and (L14).

### Proof: the actual integer floors have the same linear constant

First take \(S=\{7\}\). Define an arithmetic sequence
\(a(d)=b(d)\Lambda(d)\), where \(\Lambda\) is the von Mangoldt
function and \(b(d)\) is read modulo 7. Thus \(a(d)=0\) except at
prime powers, and
\[
 D_{\{7\}}(n)=\sum_{d\le n}a(d)\left\lfloor\frac nd\right\rfloor.
 \tag{L23}
\]
The fixed-modulus prime theorem directly gives
\[
 A(x):=\sum_{d\le x}a(d)
       =2\psi(x;7,2)+2\psi(x;7,4)
          -2\psi(x;7,3)-2\psi(x;7,5)
       =O\!\left(xe^{-c_0\sqrt{\log x}}\right).
 \tag{L24}
\]
Also \(\sum_{d\le y}|a(d)|\le2\psi(y)=O(y)\), by the same known
prime theorem. Partial summation proves that \(\sum_da(d)/d\)
converges, with a tail
\(O((1+\sqrt{\log y})e^{-c_0\sqrt{\log y}})\). Its value is
\(\delta_7\): the prime-first-power sum is the same one as before,
and every prime-power term of exponent at least two belongs to an
absolutely convergent series. This last absolute convergence justifies
the change from increasing primes to increasing prime powers.

Put \(y=\lfloor\sqrt n\rfloor\). Expanding the floor as a count of
positive integers gives the exact finite identity
\[
 D_{\{7\}}(n)=
 \sum_{d\le y}a(d)\left\lfloor\frac nd\right\rfloor
 +\sum_{k\le n/y}\bigl(A(n/k)-A(y)\bigr).
 \tag{L25}
\]
Here the second sum enumerates exactly the pairs \((d,k)\) with
\(d>y\), \(dk\le n\); if \(n/k=y\), its summand is zero.
The first sum is
\[
 n\sum_{d\le y}\frac{a(d)}d+O(y)
 =n\delta_7+
 O\!\left(n(1+\sqrt{\log y})e^{-c_0\sqrt{\log y}}+y\right).
\]
For the second sum, (L24), \(n/k\ge y\), and the harmonic-sum bound
give
\[
 \sum_{k\le n/y}|A(n/k)-A(y)|
 \ll n(1+\log n)e^{-c_0\sqrt{\log y}}.
\]
As \(y\asymp\sqrt n\), these errors together are
\(O(n e^{-c\sqrt{\log n}})\) for some smaller \(c>0\).
This proves (L15) for \(S=\{7\}\).

For one fixed omitted prime \(p\ne7\), the floor error and the
geometric tail give
\[
 \sum_{r\ge1}b(p^r)\left\lfloor\frac n{p^r}\right\rfloor
       =n\Delta S(p)+O_p(1+\log n).
\]
Indeed there are \(O_p(1+\log n)\) nonzero floors, each rounding error
has absolute value at most 2, and the omitted geometric tail after
\(p^r>n\) contributes \(O_p(1)\). Removing finitely many such
contributions proves (L15) and (L16). This completes the proof.
\(\square\)

### Proof of the unsaturated-cutoff refinement (L15a)

It suffices first to treat \(S=\{7\}\). Split the sum into prime
first powers and powers with exponent at least two. Write
\[
 C_1(X)=\sum_{p\le X}b(p)\log p/p,\qquad
 C_2(X)=\sum_{p\le X}\log p\sum_{r\ge2}b(p^r)/p^r.
\]
The argument above gives
\[
 C_1(X)+C_2(X)=\delta_7+
             O\!\left(e^{-c_1\sqrt{\log X}}\right)
 \tag{L26}
\]
for some smaller \(c_1>0\); also
\(C_2(\infty)-C_2(X)=O((1+\log X)/X)\).

The second-power-and-higher rounding error is uniform in \(X\).
Indeed, let
\[
 H_2(t)=\sum_{\substack{p^r\le t\\r\ge2}}\log p
            =O(\sqrt t\log t).
\]
This bound follows from \(\theta(u)=O(u)\), by summing
\(\theta(t^{1/r})\) over at most \(\log_2t\) exponents. The floor
errors for \(p^r\le n\) have total absolute value at most \(2H_2(n)\).
The linear geometric terms with \(p^r>n\) have total absolute value at
most \(2n\int_{(n,\infty)}t^{-1}\,dH_2(t)\), which is
\(O(\sqrt n\log n)\) by integration by parts. These bounds remain
valid after imposing \(p\le X\). Thus that whole contribution equals
\[
                    nC_2(X)+O(\sqrt n\log n)
 \tag{L27}
\]
uniformly in \(X\).

Put again \(y=\lfloor\sqrt n\rfloor\). If \(X\le y\), the
first-power contribution is \(nC_1(X)+O(\theta(X))\), hence (L26) and
(L27) give (L15a). If \(X\ge y\), its exact hyperbola decomposition is
\[
 \sum_{p\le X}b(p)\log p\left\lfloor\frac np\right\rfloor
 =\sum_{p\le y}b(p)\log p\left\lfloor\frac np\right\rfloor
  +\sum_{k\le n/y}
       \bigl(B_1(\min\{X,n/k\})-B_1(y)\bigr).
 \tag{L28}
\]
In each summand, \(y\le\min\{X,n/k\}\le n/k\). Applying (L19) and
the harmonic-sum bound makes the second sum
\(O(n(1+\log n)e^{-c_0\sqrt{\log y}})\). The first sum is
\(nC_1(\infty)+O(n e^{-c_1\sqrt{\log y}}+y)\).
Together with (L27) and
\(|C_2(\infty)-C_2(X)|\ll(1+\log y)/y\), this proves (L15a)
after decreasing \(c\). In both cases \(\sqrt n\log n\) is absorbed
by \(n e^{-c\sqrt{\log\min\{X,\sqrt n\}}}\).

For a fixed finite exceptional set, once \(X\) contains it, the
omitted-prime estimate following (L25) applies unchanged. If it does
not yet contain it, the missing finite correction is bounded by a
constant depending on \(S\) times \(n\), while \(X\) stays below the
fixed largest exceptional prime. Enlarging the implied constant
therefore proves the stated uniform assertion for all \(X\ge2\).
\(\square\)

### Consequence, and precise limitation

For the formal all-unramified-prime slope comparison, the finite part
of the mixed-type gain equals the complete stable CM-height difference
in (L3). For the actual common good-model range, the finite part is
(L16), with the missing formal 2-adic amount explicitly visible. The
new statement reaches the order-\(n\) term of the integer certificates
both at saturation and along any growing cutoff, so it is stronger
than a comparison of leading \(n\log n\) terms or an Abel-regularized
identity.

It is still a theorem about the bare lower certificates, with equal
orders held fixed over all primes. It does not identify those
certificates with \(g_j\), does not give an upper bound on a selected
theta value, and does not replace the source bad-prime, gauge, orbit,
connection, row-lattice or division-error terms. In particular the
height/slope equality cannot be inserted into \(Q_M\) until the
coefficient with which the actual source metric occurs is proved.
No conclusion of minimal chain length or impossibility of a shorter
mixed-type chain follows from (L12)–(L16).

In motivic terms the same Artin class function
\(A_\Phi-A_\Psi\) controls this finite part of the Frobenius-weighted
bare certificate and the CM Hodge determinant height, through the
functional equation. The exact identification here is a calculation
for these two specified invariants; it supplies no new comparison
isomorphism between the abelian theta kernel and an automorphic
kernel.

## 6. Approaches pursued and present Q3e boundary

1. Re-read DP44's exact comparison and the actual SizeData₂ declarations.
   The numerical arrays are inputs and the lower certificate is not their
   exact value. No actual mixed family was found in the supplied return.
2. Re-read DP52's six-identity induction and DP65's sharp full-row
   witnesses. These occupy different interfaces; the latter does not
   instantiate the former's arithmetic theta family.
3. Tested whether field/type or rank restrictions alone give minimality.
   DP44 already rules out rank minimality; DP25 and DP52 exclude only
   reuse of the unchanged induced-type wrappers. They do not prohibit
   a new theta correspondence.
4. Examined the old logOm and root-discriminant normalization. This
   produces exact expressions (L0)–(L1), but not a mixed-family \(H\).
5. Calculated the actual complete base CM height, with its strict positive
   comparison (L3), and the complete complex Hodge Gram (L9). These
   remove vague dependence on the base CM period as far as these
   specified metrics are concerned.
6. No admissible rescaling counterexample is asserted. Changing gain/E
   fields in a bare record would not preserve the geometric ties.

The remaining concrete problem is to identify the classical mixed-type
theta kernel, its invariant differential operators and its integral
lattices with one source-compatible kernel package, then evaluate its
gain/error arrays and the gauge change from (L9) in that same package.
The full difference is (L2). Neither its strict negativity nor a shorter
valid chain has been proved in this contribution.

## 7. Sources with exact locators

* Colmez, P. (1993). Périodes des variétés abéliennes à multiplication
  complexe. Annals of Mathematics, 138(3), 625–683.
  Théorèmes 0.3, 0.5 and III.2.9.
  https://webusers.imj-prg.fr/~pierre.colmez/artin.pdf
* Obus, A. (2013). On Colmez's product formula for periods of
  CM-abelian varieties. Mathematische Annalen, 356, 401–418.
  Theorem 3.9 in the inspected arXiv:1107.0684v2, Section 3.3.
  https://arxiv.org/abs/1107.0684
* Yang, T. (2010). The Chowla–Selberg formula and the Colmez conjecture.
  Canadian Journal of Mathematics, 62(2), 456–472.
  Section 3, pp. 464–466, definition of \(A_\Phi\), Conjecture 3.1,
  and equation (3.3); p. 457 states the abelian case.
  https://doi.org/10.4153/CJM-2010-028-x
* Wilms, R. (2026). On the Faltings height of the curve \(y^2=x^n-1\).
  arXiv:2601.15271v1. Theorem 1.1; Section 7, pp. 12–13;
  Remark 10.2 (the cyclotomic CM type).
  https://arxiv.org/abs/2601.15271
* NIST Digital Library of Mathematical Functions. Equations 5.15.1,
  25.11.13, 25.11.18. The multiplication and duplication identities
  used for the cross-check are 5.5.6 and 5.5.5.
  For ALP-LIFT-04: 25.15.2 (Euler product), 25.15.5 (primitive
  functional equation, including the conjugate character), and
  25.15.9 (nonvanishing at 1).
  https://dlmf.nist.gov/25.15
* Rudnick, Z. (2015, May 26). Primes in arithmetic progressions: Fixed
  modulus. Course notes, Section 2, printed p. 2, quantitative prime
  number theorem immediately before equation (1). The theorem is
  used as known; no proof of it is claimed here.
  https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf
* DP_MULT checkpoint 06: DP22, DP25, DP44, DP49, DP52, DP65, each
  cited at statement level with the intake status retained.
  ALP-LIFT-04 additionally uses DP64 (CB1), with its explicit fixed
  exceptional-set convention and distinction from theta-selected
  values.

Web retrieval references for parent reuse: Yang turn507172355view2 and
turn815074106view2; Wilms turn507172355view1 and turn815074106view1;
Obus turn477052200view3; DLMF turn477052200view0 and turn477052200view2.
The parent must itself open a source before citing its web reference.
ALP-LIFT-04 primary retrievals: Rudnick turn953517703view0;
DLMF functional equation/Euler product/nonvanishing turn953517703view1.


## ALP-LIFT-14: actual selected even-rank chain

Full proof: `selected_even_chain_nonvanishing.md`, E1-E28. Starts from AM-R-012 on the common Eprime host, uses literal bilinear source convention and equal stage characters. Exact standard factors reduce to one absolutely convergent initial factor and nonzero angular Hecke factors at 1 through d; spherical local occurrence and compact real Schur tests give an actual nonzero chain with unrestricted later finite Schwartz vectors. Whole-proof author check logged 2026-11-21T22:39:18.688282+00:00. Raw Xi membership, later integral restricted-image matrices, six identities and DP44 costs remain open.


## ALP-LIFT-15: one finite unit-norm translate per edge

Full proof: `single_finite_heisenberg_chain.md`, H1-H10. Every later actual nonzero selected lift in LIFT14 can use one finite Heisenberg translate of the actual vacuum, norm exactly1 and coefficient1. A depth-N full window has an orthonormal basis of N^(2g) such vectors and selection bound N^g. Required depth and support are uncontrolled; the family is larger than DP59 and does not identify raw Xi. Author whole-proof PASS 2026-11-21T22:49:14.726742+00:00.


## ALP-LIFT-16: 29-only single translates and exact level masses

Full proof: `spherical_tests_and_29_only_chain.md`, S1-S27. Exact spherical-vacuum transforms, including residue2, refine LIFT15 to one norm-one translate supported only at29 on every later edge. A sufficient rank-n principal level is29^(2e), with exact index I_n=29^(12 e n^2) product_(i=1)^n(1-29^(-i))^6 and all stabilizers trivial. Its v11 is6(r+v11(r!)), r=floor(n/10), independent of unknown depth e. Every-vector and multiplicity details are retained. Whole-proof author PASS 2026-11-21T23:04:38.479472+00:00. Depth bounds, raw Xi and the restricted arithmetic image remain open. Finite arithmetic certificate: `spherical_test_level_certificate.py`.


## ALP-LIFT-17: prescribed local column types exclude the spherical chain

Full proof: `prescribed_column_local_type_obstruction.md`, F1-F19. For1<=j<m the actual colLev_j has nontrivial determinant-block characters and occurs in no unramified local representation. Forj>=2, distinct block characters also exclude every tame determinant twist of an unramified representation. Thus the29-only chain cannot itself supply these explicit column modules at the prescribed G places. The variable ChIdx family and raw Xi remain separate. Any genuine source IsMu0 realization has conductor norm(g0*g1)^12 on Eprime; global existence is not asserted. Author whole-proof PASS 2026-11-21T23:20:39.359309+00:00. Finite certificate: `column_type_flag_certificate.py`.


## ALP-LIFT-18: exact literal-G even characters

Full proof: `literal_g_character_compatibility.md`, G1-G21. The source G half has Norm_Eprime/Kq(zeta28)=1, so literal residue characters impose exactly sum_(a in Phi) a e_i,a=0 mod28; class-one norm-one torus descent proves necessity and sufficiency for IsMu0. Uniform e_i divisible7 works. Explicit primes113/281, coefficient fieldQ(zeta560), conductor norm31753^12, and numerical Hyp3 family k6,m2,t1795,C46539458987 are supplied. Odd etaT and subsequent prescribed local kernel/type nonvanishing remain open. Author whole-proof PASS 2026-11-21T23:30:15.183105+00:00. Exact certificate: `literal_g_character_certificate.py`.


## ALP-LIFT-19: actual ramified theta constituents with prescribed nonterminal finite types

Full proof: `ramified_column_type_chain.md`, T1-T24. At any degree-one split G place, an initial finite Steinberg type plus distinct literal tame stage characters gives irreducible actual local theta descendants and the exact inverse adelic column type at every j<m. Explicit finite Mackey vectors are primitive and have norm squared q^[k(k-1)/2+d*j*(j-1)/2+epsilon*k*j] divided by the Gaussian multinomial index for(k,d^j), with an exact11-valuation formula. DO033 supplies an old-host actual first input; LIFT14 extends analytically with unrestricted later finite Schwartz. Terminal HXm, raw Xi and global integral image remain open. Author whole-proof PASS 2026-11-21T23:49:36.760890+00:00. Exact certificate: `ramified_column_type_certificate.py`. Independent DO033 review: `review_steinberg_first_input.md`.


## ALP-LIFT-20: exact raw first G kernel and Steinberg extraction

Full proof: `raw_first_g_steinberg_bridge.md`, RG1-RG24. For m=2 and the actual allowed class y=q^(-1)e_k, both source PhiG/PhiGS give the primitive generic-unipotent residue function f_U. Its full Steinberg component is (|U|^2/|GL_k|) f_St, with exact compact-filter and first theta-extraction formulas. The raw finite Heisenberg coefficient absolute sum is1; raw norm squared is q^(-bk)|U| and all11 averaging denominators are retained. Other raw T/Q factors, terminal PhiTop, later images and full DP44 costs remain separate. Author whole-proof PASS 2026-11-21T23:59:38.030210+00:00. Exact certificate: `raw_first_g_steinberg_certificate.py`.


## ALP-LIFT-21: actual raw terminal G quotient preserves the preceding column

Full proof: `raw_terminal_g_theta_quotient.md`, TG1-TG28. For m=2, the literal terminal PhiTop/ftY factor maps every nonzero vector in the actual LIFT19 preceding column into the actual small theta quotient. A compact full-rank integral and the primary Minguez boundary filtration prove the quotient identification. Exact identity value is vol(J)v (sharp vol(J)/q^k); graph-plane norms are computed, and removing that volume gives a saturated injection of the natural induced11-lattices. The global automorphic scalar and exact row-lattice comparison remain open. Author whole-proof PASS 2026-11-22T00:26:12.923878+00:00. Exact finite diagnostic: `raw_terminal_g_certificate.py`.


## ALP-LIFT-22: the two fixed sharp raw G edges compose on the actual middle level

Full proof: `composed_raw_sharp_g_chain.md`, CG1-CG21. Unwinding actual ChIdx.Ok forces the m2 sharp middle level Hsharp and its inverse character; midGSD uses this chF level, not generic ColV1. The first PhiGS forces the unique G class qy=e_k. Its actual quotient image is the identity-parabolic section already in that middle type, and the fixed terminal sharp kernel preserves it. Their composition is injective on the initial generic type, with exact Haar scalar, composed norms, and saturated natural11-lattice image after scalar removal. Global quotient pins, other places/Y sum, and row-lattice comparison remain open. Author whole-proof PASS 2026-11-22T00:34:08.173546+00:00. Certificate: `composed_raw_sharp_g_certificate.py`.


## ALP-LIFT-23: exact full coupled-Q Fourier contraction

Full proof: raw_coupled_q_fourier.md, Q1-Q20. At an unramified degree-one Q place the entire literal m2 Y sum collapses to the cofactor-supported Fourier function q^(-d)G(chi,psi)chi(-c)^(-1). The auxiliary depth cancels exactly. Joint Schwartz norm, primitive11 content, and scalar height (d-1/2)logq are explicit. This is a raw coupled-array identity; actual second theta-image survival and the global row scalar remain separate. Author whole-proof PASS 2026-11-22T00:47:32Z. Certificate: raw_coupled_q_fourier_certificate.py,10496 exact transforms.
