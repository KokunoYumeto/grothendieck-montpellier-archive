# A projective-frame vanishing model in every outer degree

## G-015. The exact flag-sheaf model and its comparison map

Let \(m\ge3\), let \(n\ge0\), and let \(\lambda\vdash mn\) have at most \(m\) parts. Put
\[
E=\mathfrak h_m=\{(q_1,\ldots,q_m):\sum_iq_i=0\},\qquad
\tau=(\lambda_2,\ldots,\lambda_m),\qquad
k=\max(0,\lambda_2-n).
\tag{GF.1}
\]
Use the nondegenerate invariant form \(\sum_iq_iq'_i\) to identify \(E\) and \(E^*\); the restriction is nondegenerate over \(\mathbf Q\), since its orthogonal complement in \(\mathbf Q^m\) is the constant line. Let \(\mathcal F=\operatorname{Flag}(E)\), with tautological subbundles \(\mathcal S_j\), and let
\[
\pi:\mathcal F\longrightarrow\mathbf P(E)
\]
remember the first line. For \(r=m-1\), set \(\tau_{r+1}=0\) and define the \(S_m\)-linearized invertible sheaf
\[
\mathcal L_\tau=
\bigotimes_{j=1}^{r}
(\det\mathcal S_j^*)^{\otimes(\tau_j-\tau_{j+1})}.
\tag{GF.2}
\]
The last factor is the constant determinant line with its actual group action. In particular its contribution includes \(\operatorname{sgn}^{\lambda_m}\); it has not been discarded.

Let \(Z_m\) be the following reduced, \(S_m\)-stable set of \(m\) projective points:
\[
Z_m=\{[\ell_1],\ldots,[\ell_m]\},\qquad
\ell_i=e_i-\tfrac1m\mathbf1.
\tag{GF.3}
\]
They are distinct for \(m\ge3\). Every \(m-1\) of the vectors are independent and their sum is zero, so they form a projective frame.

There is an actual \(S_m\)-equivariant vector-space isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq
H^0\bigl(\mathcal F,
\mathcal L_\tau\otimes\pi^*\mathcal I_{Z_m}^{\,k}\bigr).}
\tag{GF.4}
\]
Thus for every \(\mu\vdash m\),
\[
\boxed{
p_{\mu,(n)}^\lambda=
\dim\operatorname{Hom}_{S_m}\!\left(
[\mu],H^0(\mathcal F,
\mathcal L_\tau\otimes\pi^*\mathcal I_{Z_m}^{\,k})\right).}
\tag{GF.5}
\]
The map in (GF.4) is exactly the balanced flag chart T-032, followed by the polynomial-extension criterion proved below. Its inverse on a section represented by a flag polynomial \(F\) is
\[
F\longmapsto u^{n-\lambda_2}F(v(X)),
\qquad u=\prod_iX_{i1},
\tag{GF.6}
\]
with the polynomial minors \(v\) of (C.3). Formula (GF.4) therefore gives a specified scheme-theoretic vanishing condition for the chart extension in every outer degree.

### 1. Sections and their flag-polynomial realization

The usual Schur/flag identification is
\[
H^0(\mathcal F,\mathcal L_\tau)\simeq S_\tau E^*
\simeq S_\tau E.
\tag{GF.7}
\]
The second map is the Schur functor of the invariant form fixed above. For the first map, a Plücker coordinate is evaluated on each exterior column of a flag frame, and products of these coordinates have precisely the degrees \(\tau_j-\tau_{j+1}\) in (GF.2). This fixes the linearization and the comparison with the polynomial flag algebra, including the full determinant factor. We use the known Borel–Weil identification in this exact form: P. Magyar, *A Borel–Weil Construction for Schur Modules*, arXiv:alg-geom/9411014v1, §2.2, **Proposition 4(a)–(c), printed p. 10**, together with **Proposition 1, pp. 5–6**, relating the section realization to the dual Schur module. The source statements and these explicit comparison maps were read. The standard full-flag pullback in Proposition 4(b) supplies (GF.2) when some adjacent parts agree.

By T-032, the left side of (GF.4) is identified with the subspace of (GF.7) satisfying
\[
u^k\mid F(v(X))\quad\hbox{in }\mathbf Q[X_{ij}].
\tag{GF.8}
\]
It remains to identify this condition with the sheaf in (GF.4). This is a local calculation along the \(m\) original coordinate divisors, and we give it for arbitrary \(m\).

### 2. The first-line coordinates and all transverse parameters

Write the first two matrix columns as \(x=(x_i)\), \(s=(s_i)\). The first smaller-flag vector in the chart is
\[
q=u\left((s_i/x_i)_{i=1}^m
-\tfrac1m\sum_j(s_j/x_j)\mathbf1\right).
\tag{GF.9}
\]
Every coordinate is polynomial: each denominator divides \(u\).

Treat the divisor \(x_m=0\), on the open set where \(x_1,\ldots,x_{m-1},s_m\) are nonzero. Put
\[
x_m=\epsilon,\quad s_m=S,\quad r_j=s_j/x_j\quad(1\le j<m).
\]
At \(\epsilon=0\), (GF.9) is a nonzero scalar multiple of \(\ell_m\). On the first-projective-factor chart \(q_m-q_1\ne0\), the point \([\ell_m]\) has the regular coordinate parameters
\[
a_j=\frac{q_j-q_1}{q_m-q_1},\qquad2\le j\le m-1.
\]
Their exact pullbacks are
\[
\boxed{a_j=\epsilon\frac{r_j-r_1}{S-\epsilon r_1}.}
\tag{GF.10}
\]
They are \(m-2\) independent parameters: the hyperplane equation \(\sum_iq_i=0\), together with \(q_m-q_1=1\), recovers every remaining affine coordinate from them. Because \(\pi\) is a flag bundle, its inverse image \(\mathcal F_m=\pi^{-1}([\ell_m])\) is smooth and the same \(a_j\) are regular parameters transverse to that fiber.

### 3. Independence from every coordinate of the image fiber

We verify the needed generic independence explicitly, including every higher flag coordinate. Restrict the original matrices at \(\epsilon=0\) to the subfamily
\[
X_{mj}=0\quad(3\le j\le m).
\tag{GF.11}
\]
For a minor \(v_{h+1,I}\) from (C.3), its value is zero when \(m\notin I\), because its prefactor then contains \(x_m\). When \(m\in I\), expand the determinant along its last row. Under (GF.11), that row has its sole nonzero entry \(S\) in column two. The result, with its ordinary determinant sign, is
\[
\left(\prod_{i\notin I}x_i\right)S
\det(X_{i,j})_{i\in I\setminus\{m\},\ j\in\{1,3,\ldots,h+1\}}.
\tag{GF.12}
\]
This expression is independent of every \(r_j=s_j/x_j\).

The quotient \(E/\mathbf Q\ell_m\) is identified with
\(\mathbf Q^{m-1}/\mathbf Q\mathbf1\) by restricting to the first \(m-1\) coordinates and then passing to the quotient. This is an isomorphism: its kernel in \(E\) is exactly \(\mathbf Q\ell_m\), and the dimensions agree. In these quotient coordinates, (GF.12) is the exterior flag generated by the arbitrary ratio columns
\[
(X_{ij}/x_i)_{1\le i<m},\qquad3\le j\le m,
\]
modulo their constant line. Their first \(m-2\) quotient columns may be any independent ordered frame. Hence (GF.12) realizes a dense open set of every flag in \(E/\mathbf Q\ell_m\), which is precisely the fiber \(\mathcal F_m\). Rescaling the successive columns realizes its nonzero Plücker frames, including the full determinant frame. All these values remain independent of \(r_1,\ldots,r_{m-1}\).

Consequently the \(m-2\) leading coefficients
\[
(r_j-r_1)/S\quad(2\le j\le m-1)
\]
in (GF.10) are algebraically independent over the function field of the image fiber, and remain independent after choosing any nonzero local Plücker-frame trivialization. This follows from the exhibited subfamily: every fiber flag and frame is attained while those \(m-2\) differences vary freely.

### 4. Equality of orders and global ideal-power membership

Take a nonzero section \(F\) of \(\mathcal L_\tau\). At the generic point of \(\mathcal F_m\), trivialize all its Plücker factors by coordinates nonzero there. Their pulled-back values in (GF.12) are nonzero, so these trivializations have valuation zero along \(x_m=0\). Let \(h\) be the section's order in the fiber ideal. Its first nonzero transverse part belongs to
\[
\mathbf Q(\mathcal F_m)[a_2,\ldots,a_{m-1}]_h.
\]
Under (GF.10) its coefficient of \(\epsilon^h\) is a nonzero homogeneous polynomial in the algebraically independent leading coefficients established above. Therefore it does not vanish. We have proved
\[
\operatorname{ord}_{x_m=0}F(v(X))
=\operatorname{ord}_{\mathcal F_m}F.
\tag{GF.13}
\]
Row permutations give the same equality for every \(i\).

For clarity, order at the generic point of this fiber detects its ordinary sheaf ideal power everywhere. The fiber is smooth and is a regular embedding in the smooth flag variety. Its associated graded ideal sheaf is
\(\operatorname{Sym}_{\mathcal O_{\mathcal F_i}}(\mathcal I_i/\mathcal I_i^2)\), a locally free sheaf on the integral fiber. A section of any such graded piece that is zero at the generic point is zero everywhere. Starting with the restriction modulo \(\mathcal I_i\) and proceeding through degrees \(0,\ldots,k-1\) proves that generic order at least \(k\) is equivalent to local membership in \(\mathcal I_i^k\) throughout the fiber. Outside the fiber this ideal is the whole structure sheaf.

The \(x_i\) are pairwise nonassociate primes in the original polynomial ring. Thus (GF.8) is equivalent to order at least \(k\) along every original divisor. By (GF.13) and the preceding paragraph it is equivalent to membership in every \(\mathcal I_i^k\). The fibers are disjoint, so the intersection of these powers equals their product. The flag bundle \(\pi\) is flat, and the reduced point ideals are pairwise comaximal; hence this product is precisely \(\pi^*\mathcal I_{Z_m}^k\). This proves (GF.4). Taking the explicitly specified \([\mu]\)-covariant summand gives (GF.5), by T-003.

## G-016. The full ideal of the projective frame and its permutation quotient

For every \(m\ge4\), the saturated homogeneous ideal of \(Z_m\subset\mathbf P(E)\) is generated by its quadratic part
\[
U_m=\ker\bigl(\operatorname{Sym}^2 E\longrightarrow\mathbf Q^{Z_m}\bigr),
\qquad\dim U_m=\frac{m(m-3)}2.
\tag{GF.14}
\]
The evaluation map uses the exact affine representatives \(\ell_i\). In every degree \(C\), its homogeneous coordinate quotient \(A\) has the actual \(S_m\)-modules
\[
\boxed{A_0=\mathbf1,\qquad A_1=E,\qquad
A_C=\operatorname{Perm}_m\quad(C\ge2).}
\tag{GF.15}
\]
We prove generation, the scheme statement, and these actions directly.

Choose \(r=m-1\) projective frame points as the coordinate points of \(\mathbf P^{r-1}\). The last point has every coordinate nonzero, and rescaling the coordinates makes it \([1:\cdots:1]\). The quadratic polynomials vanishing at these \(r+1\) points are precisely the linear combinations of \(z_iz_j\), \(i<j\), whose coefficient sum is zero. Thus their ideal is generated by
\[
z_i z_j-z_1z_2\qquad(i<j,\ (i,j)\ne(1,2)).
\tag{GF.16}
\]
Let \(B\) be the quotient by (GF.16), and write \(z=z_1z_2\). All cross-products in \(B\) equal \(z\). For distinct \(i,j\), choose an index \(a\) different from both; this is possible because \(r\ge3\). Then
\[
z_i z=z_i(z_jz_a)=z_j(z_i z_a)=z_j z.
\tag{GF.17}
\]
Multiplying this identity repeatedly shows that every degree-\(C\) mixed monomial, for \(C\ge2\), has the same image \(z z_1^{C-2}\). Therefore \(B_C\) is spanned by
\[
z_1^C,\ldots,z_r^C,\quad z z_1^{C-2}.
\tag{GF.18}
\]
Their evaluations at the \(r\) coordinate points and \([1:\cdots:1]\) are linearly independent: the first \(r\) point rows isolate the first \(r\) coefficients, and the last point then isolates the mixed coefficient. Thus the displayed spanning set is a basis and the evaluation kernel is zero in every degree \(C\ge2\). It is zero in degrees zero and one as well. The quotient by (GF.16) consequently embeds in the product of the coordinate rings of the \(m\) lines through the points, degree by degree. Its kernel is exactly the homogeneous ideal of their union. This proves radicality, saturation, and quadratic generation, without an unsupported claim about a projective set determining its affine scheme.

Return to the canonical affine representatives \(\ell_i\). The evaluation map in degree \(C\) is equivariant, since literal permutation matrices take \(\ell_i\) to \(\ell_{\sigma(i)}\). The degree-two functions \(q_i^2\), \(1\le i\le m\), evaluate to a matrix with diagonal \((1-1/m)^2\) and off-diagonal \(1/m^2\). Its two eigenvalues are \((m-2)/m\) and \((m-1)/m\), both nonzero. The analogous degree-three functions \(q_i^3\) give eigenvalues
\(1-3/m+3/m^2\) and \((m-1)(m-2)/m^2\), also nonzero. Multiplication by the invariant quadratic \(\sum q_i^2\), whose value is the same nonzero number at every \(\ell_i\), propagates surjectivity by two degrees. The coordinate-ring dimensions proved by (GF.18) make each evaluation an isomorphism in degrees \(C\ge2\). Degree one is the standard submodule of the permutation module, and degree zero its constant submodule. This proves every map and action in (GF.15), and dimension subtraction gives (GF.14).

For \(m=3\), the three projective points in \(\mathbf P(E)=\mathbf P^1\) have the principal ideal
\[
\left(\prod_{1\le i<j\le3}(q_i-q_j)\right).
\tag{GF.19}
\]
Each factor vanishes at exactly one of the three points, and their distinct linear factors generate the reduced degree-three divisor ideal. The generator has the sign character under literal row permutations. This also explains the degree-three correction in the rank-three flag formulas through the same map (GF.4).

## Geometric dictionary, scope, and the next exact operation

All objects in (GF.1)–(GF.19) are explicit schemes, locally free sheaves, or coherent ideal sheaves. The invariant form and the points are defined over \(\mathbf Z[1/m]\); their characteristic-zero global-section representations are those used in the stated equalities. The flag scheme is the successive locally free quotient construction, and \(\pi\) is the corresponding relative flag morphism. The comparison is the coordinate-ring morphism (C.3), localized at \(u\), followed by the exact regular-embedding calculation (GF.10)–(GF.13). The affine coordinate dictionary is EGA I 9.5.2–9.5.3, and the group actions are the constant-group comodules of SGA 3 I 4.7.2–4.7.3. Applying the Schur and determinant operations gives the exact representation-group classes of SGA 6 VI 3.3. The complete comparison maps, rather than only equality of dimensions, carry the proof into these frameworks.

For \(m=4\), (GF.16) consists of two quadrics and the full section evaluation is T-037. For \(m\ge5\), (GF.4) and (GF.16) leave a precise new task: evaluate the \(S_m\)-covariant global sections of the displayed powers of this explicitly generated projective-frame ideal. The general finite positive construction G-010 already evaluates every coefficient; the remaining direct-formula problem is to obtain small uniform positive descriptions for these particular section spaces. No vanishing of their higher cohomology or positive splitting of their ideal powers is assumed.
