# A-088. Actual invariant-base modules for every hook cycle

Let $m\ge3$, let $W=\mathfrak h_m$ with its rational permutation action, and put
$P=\operatorname{Sym}W$ and $I=P^{S_m}=\mathbb Q[e_2,\ldots,e_m]$.
Use the total grading and actual Koszul maps HK.5. Write
$Z_0=P_+$ and $Z_r=\ker(\partial:P\otimes\Lambda^rW\to P\otimes\Lambda^{r-1}W)$ for $r\ge1$.
For a Specht module $[\nu]$ let $Z_{r,\nu}=\operatorname{Hom}_{S_m}([\nu],Z_r)$.
All comparisons below are maps of these actual graded modules.

## 1. Free nontrivial multiplicity modules in every hook degree

For every $\nu\ne(m)$ and $0\le r\le m-2$, the module $Z_{r,\nu}$ is finite graded free over $I$. Its basis degrees are exactly the exponents, with multiplicity, of

$$
f_\nu(q)e_r(q^{j-i+1}:(i,j)\in\nu\setminus\{(1,1),(2,1)\}).
$$

They are at most $\binom m2+r$.

Here is a complete construction. The homogeneous rational coinvariant section, averaged over $S_m$, gives the multiplication isomorphism $I\otimes H\to P$, with $H=P/(I_+)$. Consequently every
$A_{r,\nu}=\operatorname{Hom}_{S_m}([\nu],P\otimes\Lambda^rW)$
is a finite graded free $I$-module, with a chosen basis from
$\operatorname{Hom}_{S_m}([\nu],H\otimes\Lambda^rW)$.
The highest degree in this latter space is at most $\binom m2+r$.

For $r=0$, the nontrivial label has no constant component, so $Z_{0,\nu}=P_\nu$ is already free. Suppose a homogeneous free basis of $Z_{r-1,\nu}$ has been constructed. A basis map $b:[\nu]\to Z_{r-1}$ of total degree $D>0$ has the explicit lift

$$
\widetilde b=\frac1D d_P\circ b:[\nu]\longrightarrow
P\otimes\Lambda^rW.
$$

The identity $\partial d_P+d_P\partial=D$ and $\partial b=0$ give $\partial\widetilde b=b$. At $r=1$, the same calculation uses $\partial=0$ on $Z_0$ in positive degree. Define the section on the chosen free basis by these lifts and extend it $I$-linearly. The resulting map is a graded rational $I$-linear section of the actual differential. The gradient is not required to be $I$-linear before this basis extension.

Thus
$A_{r,\nu}=Z_{r,\nu}\oplus s(Z_{r-1,\nu})$
as actual graded $I$-modules. In particular $Z_{r,\nu}$ is graded projective. Choose homogeneous lifts of a vector-space basis of $Z_{r,\nu}/I_+Z_{r,\nu}$. Their multiplication map from the corresponding graded free module is surjective by graded Nakayama. Projectivity gives a graded splitting: an ordinary splitting may also be replaced by its degree-zero component. Reduction modulo $I_+$ is exact, and the kernel has zero quotient. A second application of graded Nakayama makes that kernel zero. This produces a free isomorphism, whose lifts and matrices can be obtained by rational row reduction.

The exact sequences give the numerator recurrence
$N_{r,\nu}=q^r f_{\nu\otimes\Lambda^r W}-N_{r-1,\nu}$.
Induction gives degree at most $\binom m2+r$. The actual character calculation and specified two-cell cancellation in G037 identify this numerator with the displayed positive polynomial. Since a graded free module's numerator records its homogeneous basis degrees, the asserted degrees and multiplicities follow.

This is a proof by explicit sections; it does not infer a free module from positivity of its Hilbert numerator.

## 2. Exact trivial cycles and their obstruction at the origin

Solomon's differential map and the invariant dot form give the actual invariant complex

$$
F_j=I\otimes\Lambda^j\langle\xi_2,\ldots,\xi_m\rangle,
\qquad \partial\xi_i=e_i,\qquad \xi_i=de_i/i.
$$

Put $s=m-1$. Its positive-multidegree complex is exact by the explicit contraction in HK.14: choose any positive-support index, use the corresponding basis vector of contraction value one, and wedge with it. Hence
$Z_r^{S_m}=\operatorname{im}(F_{r+1}\to F_r)$
for $0\le r\le s-1$, with $Z_0^{S_m}=I_+$.

There is an exact presentation
$F_{r+2}\to F_{r+1}\to Z_r^{S_m}\to0$.
Every entry of the first map belongs to $I_+=(e_2,\ldots,e_m)$. Tensoring the presentation with $I/I_+=\mathbb Q$ therefore gives

$$
\dim_{\mathbb Q}Z_r^{S_m}/I_+Z_r^{S_m}
=\binom{s}{r+1}.
$$

Over the fraction field, rescale one $\xi_i$ so that its contraction is one. The other $s-1$ vectors can be replaced by
$\xi_j-(e_j/e_i)\xi_i$.
The contraction kernel in exterior degree $r$ is exactly their exterior power, of dimension $\binom{s-1}{r}$; for $r=0$ it is the full fraction field. Thus the generic rank of $Z_r^{S_m}$ is $\binom{s-1}{r}$.

For $0\le r\le s-2$, the minimal generator number exceeds the rank by
$\binom{s-1}{r+1}>0$.
Localizing at the invariant origin, a free module would have minimal generator number equal to its rank. This proves that these particular modules are not locally free there, and consequently are not free over $I$. The exact presentation and the explicit fraction-field basis establish the comparison; no categorical distinction is asserted without it.

## 3. Top endpoint and off-origin trivializations

At $r=s-1=m-2$, exactness and the zero kernel at $F_s$ give a free rank-one cycle module. Its generator is the actual polynomial vector

$$
\partial(\xi_2\wedge\cdots\wedge\xi_m)
=\sum_{i=2}^m(-1)^{i-2}e_i\,
\xi_2\wedge\cdots\widehat{\xi_i}\cdots\wedge\xi_m.
$$

The map from $I$ multiplying this vector is injective because $I$ is a domain and $e_2\ne0$, and its image is the whole top cycle module. Its degree is
$2+\cdots+m=m(m+1)/2-1$.
This is precisely the sole top-leg tag in HK.15.

On each principal open $D(e_i)$, the vectors
$\xi_j-(e_j/e_i)\xi_i$, $j\ne i$,
and the rescaled contraction-one vector split the whole complex. Their exterior powers give an explicit free basis for every $Z_r^{S_m}$ on this open; $Z_0^{S_m}$ becomes the unit ideal. Thus the previously proved failure of local freeness is concentrated at the invariant origin. The localization maps and bases are specified.

## 4. Geometric transport and check status

The finite quotient morphism $\operatorname{Spec}P\to\operatorname{Spec}I$ is given by the elementary invariant polynomials. Pushforward along this finite affine map retains the actual Koszul modules; rational averaging and the Specht Hom projector extract their multiplicity sheaves. The nontrivial summands have the explicit free trivializations constructed in §1. The trivial summands have the presentations, generic bases and principal-open trivializations in §§2–3.

The stable flag and Young maps of G037 identify their degree-$a+r$ sections with the original stable-hook plethysm multiplicities, with its determinant sign. The associated coherent and vector-bundle classes use the already verified affine sheafification, frame and SGA6 representation maps. All matrices are rational and spread after inverting their finite denominators.

**Independent proof completed and reread.** The section construction, graded splitting/Nakayama step, exact numerator bound, minimal presentation modulo the invariant maximal ideal, generic rank and top endpoint have each been checked above. The primary inputs are precisely the Stanley/Solomon readings recorded in A086–A087; no new numerical computation is claimed for this proof.
