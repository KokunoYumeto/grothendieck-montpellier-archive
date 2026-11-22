# AM-R-006: the exact scalar joining the translated theta and the normalized trace-one section

Author: `/root`, GPT-6 Astra Pro; reasoning effort not externally exposed;
run ALP_MACHINE, 21 November 2026. This finding uses AM-R-004,
AM-DO-015--016 and ALP-LIFT-07--08. It removes the remaining scalar
between their two actual sections of the same principal theta line.
It is not an identification of an iterated automorphic lift image.

## Statement

Use the period coordinates of AM-R-004, with \(u=Pz\),
\(Y=\operatorname{Im}\tau\), and
\(Q(z)=\pi z^tY^{-1}z/2\). Put
\[
 \theta_0=\theta[0;0](0;\tau),\qquad
 \theta_K(z)=\theta[\tfrac12(1,1,1);\tfrac12(1,0,1)](z;\tau).
 \tag{R6.1}
\]
By AM-DO-015 the exact normalized Mumford translate is
\[
 \Sigma_{\rm tr}(u)=-i\,e^{Q(P^{-1}u)}
                   \frac{\theta_K(P^{-1}u)}{\theta_0}.
 \tag{R6.2}
\]
Let \(\sigma_q\) be the reduced germ of the actual trace-one section
\(s_q\) of ALP-LIFT-08, whose first nonzero homogeneous term is
\(q(u)=u_1u_3-u_2^2\). Define the nonzero scalar by the exact convergent
analytic expression
\[
 c=-\frac{i}{\theta_0}
     \left.\partial_{u_1}\partial_{u_3}
         \theta_K(P^{-1}u)\right|_{u=0}.
 \tag{R6.3}
\]
This fixes its phase, not merely an unspecified root. Then
\[
 \Sigma_{\rm tr}=c\,\sigma_q.
 \tag{R6.4}
\]
For \(S=\{1,3,5\}\), \(S^c=\{0,2,4,6\}\), set
\[
 R_S=\prod_{a\in S}\prod_{b\in S^c}(\zeta_7^a-\zeta_7^b)
 =49(-\zeta_7^5-\zeta_7^4-2\zeta_7^2+\zeta_7-2).
 \tag{R6.5}
\]
The scalar is algebraic and satisfies the exact phase-independent identity
\[
 c^8=\frac{R_S^2}{4^8},\qquad
 |c|=\frac{|R_S|^{1/4}}4.
 \tag{R6.6}
\]
In normalized valuations \(v_p(p)=1\), at every place above the
indicated rational prime,
\[
 v_2(c)=-2,\qquad v_7(c)=\frac12,\qquad
 v_p(c)=0\quad(p\ne2,7).
 \tag{R6.7}
\]
The primitive integral scalar contents of the translated section are
therefore
\[
 c_2(\Sigma_{\rm tr})=-\frac67,\qquad
 c_p(\Sigma_{\rm tr})=0\quad(p\text{ odd}).
 \tag{R6.8}
\]
Here content is relative to the integral rigidified trace-one line of
ALP-LIFT-08. Equation (R6.8) concerns the entire algebraic section,
not the coefficient integrality of a Chern formal frame.

The following explicit global estimate now holds for the actual
quadratic-normalized trace-one germ:
\[
 |\sigma_q(u)|<\frac{6125}{16}
       \exp\!\left(\frac\pi2\sum_{j=1}^3\frac{|u_j|^2}{G_j}\right).
 \tag{R6.9}
\]
Consequently, for every multiindex \(\alpha\),
\[
 |\partial^\alpha\sigma_q(0)|
 <\frac{6125}{16}\,\alpha!
   \prod_{j:\alpha_j>0}
      \left(\frac{\pi e}{\alpha_jG_j}\right)^{\alpha_j/2}.
 \tag{R6.10}
\]
For any positive integer \(M\), substitution of \(Mu\) multiplies
the right side before level normalization by \(M^{|\alpha|}\).
Thus the source factor \(M^{-|\alpha|}\) cancels this increase
exactly; for the actual arithmetic `Level` one retains its oddness
condition. The section \(\sigma_q(Mu)\) is in the correct trace-one
line for every such odd \(M\).

## Proof

### The derivative Thomae comparison with all differential factors retained

We use the derivative Thomae formula as a literature theorem, rather
than reprove it. Bernatska (2020), arXiv v3, Corollary 2, equations
(34)--(37), printed p. 18, and Example 4, equations (38)--(39),
printed p. 19, identify the Hessian of the unique singular even theta
characteristic in genus three. Her differentials are
\[
 d v_1=-\frac{x^2dx}{2y},\qquad
 d v_3=-\frac{x dx}{2y},\qquad
 d v_5=-\frac{dx}{2y};
\]
this follows from her equation (2), printed p. 2, with
\(f=-y^2+x^7-1\). Hence
\[
 (v_1,v_3,v_5)=-\tfrac12(u_3,u_2,u_1).
 \tag{R6.11}
\]
The cited Hessian formula says that the degree-two term of
\(\theta_K\), in these variables, is
\(C_3(v_1v_5-v_3^2)\). The derivative normalization of \(C_3\)
is stated immediately after (39). In the original \(u\) variables
the term is therefore exactly
\[
 \frac{C_3}{4}(u_1u_3-u_2^2).
 \tag{R6.12}
\]
An eighth-root phase in the homology/characteristic convention is
included in the actual derivative value \(C_3\); equation (R6.3)
selects it in our fixed period convention. The quadratic exponential
in (R6.2) has constant term one, so it cannot alter (R6.12).

Both \(\Sigma_{\rm tr}\) and \(\sigma_q\) are nonzero sections
of the same rigidified principal line, represented in its same
reduced frame. Its section space has dimension one. Comparing their
first nonzero jets proves (R6.4) with
\(c=-iC_3/(4\theta_0)\). This argument does not assume a global
algebraic trivialization of that ample line.

Bernatska's Remark 3 and equation (30), printed p. 16, give
\(C_3\) as the product of the square root of the period determinant
factor and the fourth root of the Vandermonde in all seven finite
branch points. The first Thomae formula for the nonsingular
characteristic belonging to \(S\) gives the same period determinant
factor times the fourth root of the two within-part Vandermondes.
In our period convention that nonsingular characteristic is precisely
the zero characteristic, by ALP-LIFT-07. Dividing the two formulas
cancels the period determinant. The result is
\[
 \frac{C_3}{\theta_0}=\epsilon R_S^{1/4},\qquad \epsilon^8=1,
 \tag{R6.13}
\]
with the ordering sign absorbed in the root convention. This is also
the displayed consequence of first Thomae immediately after (30).
Taking absolute values and eighth powers proves (R6.6). In particular
the scalar defined analytically in (R6.3) is algebraic. There is no
need to select an arbitrary fourth root in place of that exact
analytic definition. The cyclotomic reduction in (R6.5) is ordinary
polynomial multiplication modulo \(1+T+\cdots+T^6\), and is
independently reproduced by the accompanying script.

### Finite valuations and integral section content

For distinct seventh roots of unity, their difference is a unit
away from 7 and has normalized valuation \(1/6\) at 7. For example
\(\zeta^a-\zeta^b=\zeta^b(\zeta^{a-b}-1)\); the quotient of
\(\zeta^{a-b}-1\) by \(\zeta-1\) is a unit and
\(v_7(\zeta-1)=1/6\). There are twelve factors in (R6.5), so
\(v_7(R_S)=2\), with zero valuation elsewhere. Applying valuations
to (R6.6) yields
\[
 8v_p(c)=2v_p(R_S)-8v_p(4),
\]
which proves (R6.7) at every place after any further finite extension.
Roots of unity have valuation zero, including at 2, so the phase
convention causes no exception.

Scalar contents add under multiplication of a section by a scalar.
ALP-LIFT-08 gives content \(8/7\) at 2, \(-1/2\) at 7, and zero
elsewhere for \(s_q\). Adding (R6.7) proves (R6.8). This also
checks compatibility with the finite normalization of the original
value-one section in ALP-LIFT-07: the translated section has exactly
the same dyadic content \(-6/7\), and is primitive at 11 and at
every other odd prime on the stated good models. The equality of
these contents is a computed conclusion; it was not assumed from
integrality of a two-torsion translation in characteristic two.

### The archimedean estimate and derivatives

Every difference of two distinct seventh roots of unity has absolute
value at least \(2\sin(\pi/7)>4/5\). The rational trigonometric
certificate in AM-R-004 proves this elementary inequality. Thus
\[
 |R_S|>(4/5)^{12},\qquad |c|>\frac14(4/5)^3=\frac{16}{125}.
 \tag{R6.14}
\]
AM-DO-015's normalized Mumford translation preserves the AM-R-004
Gaussian estimate, including its constant 49. Divide that estimate
by (R6.14), and use \(49\cdot125/16=6125/16\), to obtain (R6.9).
This bound is valid on all of \(\mathbb C^3\), not only a compact
set or a formal neighborhood.

Apply the multivariable Cauchy estimate on a polydisc of radii
\(r_j>0\). For \(\alpha_j>0\), minimize
\(e^{\pi r_j^2/(2G_j)}r_j^{-\alpha_j}\) at
\(r_j^2=\alpha_jG_j/\pi\). For zero entries let \(r_j\) tend
to zero after applying Cauchy. This gives (R6.10). Composition with
\([M]\) acts on the universal cover by \(u\mapsto Mu\), and
the chain rule gives the final level-normalization assertion.

## Consequence and limits for the main question

The source-line section can now be used with a fixed algebraic
quadratic normalization, exact finite scalar content, and an explicit
archimedean Cauchy bound. Its relation to the literal finite Schwartz
input of AM-DO-016 is
\[
 e^{Q(z)}\Theta(\varphi_t;z,\tau)
       =\theta_0 c\,\sigma_q(Pz).
 \tag{R6.15}
\]
The exact scalar is retained on the right. This closes the scalar
comparison for that actual CM fibre. It neither makes the reduced
formal frame integral nor computes the automorphic quotient volume,
the terminal mass, a selected lift's actual gain/error, or a common
all-polynomial `MainX` identity. Those are separate questions.

In the Picard and biextension formulation this is an equality of
sections of the same rigidified line after the two-torsion change
of characteristic; the scalar valuations measure its integral
section lattice. In determinant-of-cohomology terms, the chosen
quadratic jet is the cup-product determinant of ALP-LIFT-08.
The comparison concerns the metric and integral lattice of a line,
not an identity of higher cohomological weights. See the exact
FGA/SGA7/cote54 locators in `GROTHENDIECK_DICTIONARY.md`.

## Primary reference and computation

Bernatska, J. (2020). General derivative Thomae formula for singular
half-periods. *Letters in Mathematical Physics, 110*, 2983--3014.
https://doi.org/10.1007/s11005-020-01315-8 . The directly inspected
version is https://arxiv.org/pdf/1904.09333v3 , equation (2),
Remark 3/equation (30), Corollary 2/equations (34)--(37), and
Example 4/equations (38)--(39), printed pp. 2, 16, 18--19.

`scripts/trace_one_theta_scalar.py` performs exact cyclotomic
multiplication and an independent 60-digit theta-series diagnostic
of the Hessian shape, scalar modulus and eighth-power identity.
The latter is explicitly numerical, not an interval or formal proof.
The theorem above uses the exact literature formulas and elementary
algebra, independently of the numerical diagnostic.
