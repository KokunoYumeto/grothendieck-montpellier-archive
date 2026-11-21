# An exact polynomial model for every highest-weight boundary kernel

Statement **R-017**. This is an unconditional reformulation of the common-polarization kernel, not a classification of its remaining multiplicities. Written and checked on 2026-11-21 UTC by GPT-6 Astra Pro, /root/rectangular_cases; effort setting not exposed. The first-coordinate evaluation underlying the reformulation is also used in Kadish–Landsberg, arXiv:1204.4693, Theorem 1.3 and its proof in section 2.

Fix \(r\ge1\), \(b\ge L\ge0\), and \(m\ge2\). In each of the \(r\) slots write

\[
 v_i=(x_i,y_{i,2},\ldots,y_{i,m}),\qquad
 z_{i,j}=y_{i,j}/x_i.
\]

For a polynomial \(P(z_1,\ldots,z_r)\) whose degree in each block \(z_i\) is at most \(b\), define its separate homogenization

\[
 H_b(P)=\prod_{i=1}^r x_i^b
 P(y_{1,2}/x_1,\ldots,y_{r,m}/x_r).
 \tag{R017.1}
\]

The block degree bounds make this a polynomial. Evaluation at every \(x_i=1\) is its inverse. These are exact linear isomorphisms between polynomials of block degrees at most \(b\) and polynomials separately homogeneous of degree \(b\) in the \(v_i\). They commute with slot permutations.

## Highest vectors become translated-polynomial invariants

The raising operator \(E_{1j}\), \(j>1\), acts on a separately homogeneous polynomial as \(\sum_i x_i\partial_{y_{i,j}}\). Direct differentiation gives

\[
 E_{1j}H_b(P)=
 \prod_i x_i^b\sum_i\partial_{z_{i,j}}P.
 \tag{R017.2}
\]

Thus its kernel corresponds exactly to invariance under simultaneous translation
\(z_{i,j}\mapsto z_{i,j}+c_j\). The equality follows by exponentiating the displayed locally nilpotent derivations in characteristic zero; differentiating the translation identity proves the converse.

For \(2\le k<j\le m\), the remaining raising operators correspond exactly to

\[
 \sum_i z_{i,k}\partial_{z_{i,j}}.
 \tag{R017.3}
\]

A source highest vector of weight \(\lambda\vdash rb\) therefore corresponds to a symmetric, simultaneously translation-invariant polynomial \(P\), of individual block degrees at most \(b\), with coordinate weights \((\lambda_2,\ldots,\lambda_m)\), annihilated by (R017.3). Its total \(z\)-degree is

\[
 D=\lambda_2+\cdots+\lambda_m=rb-\lambda_1.
 \tag{R017.4}
\]

Every polynomial satisfying these displayed properties homogenizes to precisely such a highest vector; the formulas above prove both directions.

## Polarization is weighted block truncation

For a monomial

\[
 z^\alpha=\prod_{i=1}^r\prod_{j=2}^m z_{i,j}^{\alpha_{i,j}},
 \qquad d_i=\sum_{j=2}^m\alpha_{i,j},
\]

define the explicit diagonal operator

\[
 Q_{L,b}(z^\alpha)=
 \begin{cases}
 \left(\prod_i\binom{b-d_i}{L}\right)z^\alpha,
       &d_i\le b-L\text{ for every }i,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{R017.5}
\]

The coefficient-extraction map satisfies the exact identity

\[
 T_{r,L,b}(H_b(P))(v_1,\ldots,v_r;\,e_1)
 =H_{b-L}(Q_{L,b}P).
 \tag{R017.6}
\]

To prove it, a monomial in (R017.1) is
\(\prod_i x_i^{b-d_i}y_i^{\alpha_i}\). Substitution of \(v_i+t_ie_1\) changes only \(x_i\) to \(x_i+t_i\). The coefficient of \(t_i^L\) is
\(\binom{b-d_i}{L}x_i^{b-d_i-L}y_i^{\alpha_i}\), with value zero for \(b-d_i<L\). Multiplication over all slots gives (R017.6) on every monomial.

Restriction of a highest image to common vector \(e_1\) detects its vanishing. To see this directly, let \(G(v_1,\ldots,v_r;w)\) be such an image. It is annihilated by every \(E_{1j}\), and is homogeneous of degree \(rL\) in the common vector \(w=(w_1,\ldots,w_m)\). On the dense open set \(w_1\ne0\), apply the unipotent substitutions

\[
 w_j\mapsto w_j-\frac{w_j}{w_1}w_1=0,\qquad
 y_{i,j}\mapsto y_{i,j}-\frac{w_j}{w_1}x_i
 \quad(j>1).
\]

Invariance under the exponentials of \(E_{1j}\) leaves \(G\) unchanged. The common vector becomes \(w_1e_1\), and common-vector homogeneity gives

\[
 G(v_1,\ldots,v_r;w)
 =w_1^{rL}
 G(v'_1,\ldots,v'_r;e_1).
 \tag{R017.7}
\]

Hence a zero restriction at \(e_1\) makes \(G\) zero on a dense open set and therefore identically zero. The converse is immediate.

Combining (R017.1)–(R017.7) gives the exact highest-weight kernel isomorphism

\[
 \boxed{
 H_b^{-1}\bigl((\ker T_{r,L,b})_\lambda^{\mathrm{highest}}\bigr)
 =
 \ker Q_{L,b}\ \cap\
 \{\text{polynomials satisfying (R017.2)–(R017.4) and slot symmetry}\}.
 }
 \tag{R017.8}
\]

All nonzero diagonal coefficients in (R017.5) are nonzero rational integers. Its kernel is therefore exactly the kernel of ordinary monomial truncation retaining only the monomials with every block degree at most \(b-L\). This identifies the relevant subspace with explicit linear equations, rather than inferring it from source and target multiplicities.

## The precise boundary degree gap

At \(r\ge2,L\ge1,b=rL-1\), a source partition has \(\lambda_1\ge b\), because its length is at most \(r\) and its size is \(rb\). Equality forces the rectangle \((b^r)\). For that rectangle,

\[
 D=(r-1)b=r(b-L)+1,
\]

so every monomial exceeds the total degree allowed by the block truncation. In dimensions \(m\ge r\), the determinant power provides the corresponding source highest vector exactly when \(b\) is even; at this boundary that parity is equivalent to \(r\) and \(L\) both odd. For \(m<r\), that Schur functor is zero.

Every other source partition has \(\lambda_1\ge b+1=rL\), so (R017.4) gives \(D\le r(b-L)\). The total-degree obstruction is then absent. Formula (R017.8) specifies the actual remaining kernel problem as a translation-invariant symmetric polynomial truncation problem; it does not assert that its remaining intersection is zero. R-011, R-012, R-015 and R-016 supply the completely certified finite cases currently established in this run.
