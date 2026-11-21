# DEG_L / sharp growth for a fixed transported Weil witness

Run `DEG_L_20261121`, author `/root`, GPT-6 Astra Pro, effort not exposed. This result concerns the specified transport construction. It supplies no lower bound for the minimum degree among all cycles on a target.

## B20. Finite stabilizers prevent cancellation of the CM index for a fixed witness

Keep the fixed primitive CM type, maximal-order reference $A_0$, target $A$, index $J=[\Lambda:\Lambda^-]$, and compatible imaginary quadratic Weil action of B19. Let $\dim A_0=2n$ and $V=\chi(L)$ be fixed. Let $Z_0\subset A_0$ be an integral closed subvariety of dimension $n$ with
\[
 w_0=e_0[Z_0]\ne0,
 \qquad s_0=|\operatorname{Stab}_{A_0}(Z_0)|.
\]
Here $e_0$ is the generic Weil projector of B6 and its norm is the positive form $q_0=(-1)^n\int_{A_0}(-)\smile(-)$. Since the primitive CM type makes $A_0$ simple and $Z_0$ is proper and positive-dimensional, $s_0$ is finite. For every nonzero $E$-linear homomorphism $h:A_0\to A$, put $Z_h=h(Z_0)_{\mathrm{red}}$. Then
\[
 \deg(h|_{Z_0})
   =|\ker h\cap\operatorname{Stab}_{A_0}(Z_0)|\le s_0,
\tag{B20a}
\]
\[
 \|e_A h_*[Z_0]\|_{q_A}
       =\sqrt{\deg h}\,\|w_0\|_{q_0},
\tag{B20b}
\]
and consequently
\[
 \begin{aligned}
 \deg_L(h_*Z_0)&\ge n!\sqrt V\,\|w_0\|_{q_0}\sqrt{\deg h},\\
 \deg_L Z_h&\ge
   \frac{n!\sqrt V\,\|w_0\|_{q_0}}{s_0}\sqrt J.
 \end{aligned}
\tag{B20c}
\]
Together with B19.9 this pins the least degree among these reduced images between two positive fixed multiples of $\sqrt J$. In particular, transporting this one witness, or a fixed finite list of such witnesses, cannot give uniformly bounded degrees on a sequence of targets with $J\to\infty$.

**Proof.** The finiteness of the stabilizer is the simple-variety specialization of Ullmo--Yafaev, *O-minimal flows on abelian varieties*, arXiv:1610.01488v1, Proposition4.1(1), printed p8: the identity component of the stabilizer is an abelian subvariety, and a positive-dimensional one in a simple abelian variety would force the proper subvariety to equal the ambient variety. The statement and its proof were read at <https://discovery.ucl.ac.uk/id/eprint/1524974/1/Yafaev_1610.01488v1.pdf>.

Write $K_h=\ker h(\mathbf C)$. For every $a\in K_h$ not stabilizing $Z_0$, the intersection $Z_0\cap(Z_0-a)$ is a proper closed subset of the integral variety $Z_0$. Remove the finite union of these subsets. For any point $x$ of the remaining nonempty open set, the points of $Z_0$ mapping to $h(x)$ are exactly $x+a$ with $a\in K_h\cap\operatorname{Stab}(Z_0)$. They are distinct. Since an isogeny over $\mathbf C$ is finite etale, the generic fibre is reduced and this count equals the generic degree. This proves (B20a) without a smoothness hypothesis on $Z_0$.

Let $m=\deg h$. The $K$-linear isogeny commutes with the polynomial Weil projectors, and $h_*=(m)(h^*)^{-1}$ on rational cohomology. For any two middle-degree classes $u,v$ on $A_0$, the projection formula gives
\[
 \begin{aligned}
 m\int_A h_*u\smile h_*v
 &=\int_{A_0}h^*h_*u\smile h^*h_*v\\
 &=m^2\int_{A_0}u\smile v.
 \end{aligned}
\]
With $u=v=w_0$, this gives the exact positive norm identity (B20b). Apply B7 to the effective integral pushforward cycle $h_*Z_0$ to obtain the first inequality of (B20c). Since $h_*Z_0=\deg(h|_{Z_0})Z_h$, equation (B20a) bounds the division needed to pass to its reduced image.

Finally represent $h$ by multiplication by $\alpha\in E^\times$. The image lattice $\alpha I_0$ is $\mathcal O_E$-stable and lies in $\Lambda$, hence lies in $\Lambda^-$. Thus
\[
 \deg h=[\Lambda:\alpha I_0]
     =[\Lambda:\Lambda^-]\,[\Lambda^-:\alpha I_0]\ge J.
\]
This proves the second inequality. For the small isogeny chosen in B19, the reduced image has degree at most its integral pushforward degree, which is bounded by the right side of B19.9. The two constants depend only on the fixed reference witness and polarization volumes. For finitely many reference witnesses, take the minimum of their positive lower constants and the maximum of their upper constants. QED.

**Scope and next gate.** The irreducibility assumption ensures the exact generic-fibre count. Any effective witness has an irreducible component with nonzero Weil projection; one may fix that component at the start. The simplicity or finite-stabilizer condition is essential: B11 gives an explicit product example with growing mapping multiplicity and constant reduced-image degree. The result also does not exclude target-dependent cycles, rational normalizations followed by different integral extraction, or deformation of a new object. It locates the failure of the fixed finite-reference transport route precisely, even after generic degree is retained. No Dirichlet or Hecke GRH input enters this result.

**Grothendieck placement.** These are finite correspondences, proper pushforward of effective cycles, and their middle-degree Poincare realization; the positive Weil summand is the B6--B8 motive. Cote16, Coates letter, PDF45--46 (archive footers44--45), is the checked algebraic-Lefschetz/positivity framework; it supplies no claim of bounded cycles. FGA, Bourbaki221, Lemme2.4 p255 and Theoreme3.2 p260, supplies the precise bounded-cycle parameter spaces whose degrees this construction fails to bound. The generic-fibre count and the explicit index inequality are the present calculation, not statements attributed to those archival pages.

## Check status

Root and the bounds agent have read the complete proof. Both checked the projection-formula factor, the kernel/stabilizer count, the degree-to-index inequality, and the precise fixed-menu scope. The independent checker also read the full cited stabilizer argument. Actual check events are recorded; no formal proof-assistant verification is claimed.
