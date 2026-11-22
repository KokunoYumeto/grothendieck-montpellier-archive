"""NN-C032: explicit projective Weil restriction and coherent Frobenius over fixed F2."""

def append_c032(add,E,SGATRACE,VV):
    segre={'source':'Stacks Project, Constructions of Schemes',
           'locator':'Lemma27.13.6, Tag01WD, Segre embedding; the exact two-by-two-minor chart computation is proved below',
           'url':'https://stacks.math.columbia.edu/tag/01WD'}
    res={'source':'Stacks Project, Criteria for Representability',
         'locator':'Section97.11, Tag05Y8; equation97.11.0.2, Lemma97.11.1 (fppf sheaf) and Lemma97.11.2 (base change)',
         'url':'https://stacks.math.columbia.edu/tag/05Y8'}
    descent={'source':'Stacks Project, Descent',
             'locator':'Lemma35.23.29, Tag02VL: smoothness is fpqc local on the base',
             'url':'https://stacks.math.columbia.edu/tag/02VL'}
    bc={'source':'Stacks Project, Cohomology of Schemes',
        'locator':'Lemma30.5.2, Tag02KH, flat base change; especially its affine-base statement(2) and Cech proof',
        'url':'https://stacks.math.columbia.edu/tag/02KH'}
    kunneth={'source':'Stacks Project, Varieties',
             'locator':'Lemma33.29.1, Section Tag0BEC: coherent Kunneth for quasi-compact schemes with affine diagonal; cup-product normalization and complete proof',
             'url':'https://stacks.math.columbia.edu/tag/0BEC'}
    regular={'source':'Stacks Project, Varieties and Commutative Algebra',
             'locator':'Lemma33.25.3, Tag056S: smooth over a field implies regular; Lemma10.106.2, Tag00NP: a regular local ring is a domain',
             'url':'https://stacks.math.columbia.edu/tag/056S',
             'additional_url':'https://stacks.math.columbia.edu/tag/00NP'}
    weil={'source':'Deligne, La conjecture de Weil I, PMIHES43(1974),273--307',
          'locator':'Theorem1.6, printedp276',
          'url':'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf'}
    inputs=[{'source':'NN-C031','locator':'deterministic fixed-F4 smooth projective hypersurface, canonical coherent basis and absolute Frobenius coefficient omega*c'},
            segre,res,descent,bc,kunneth,regular,SGATRACE,weil,VV,
            dict(E,locator='Theorem1.1, original-source evaluator')]
    add('NN-C032','NEG_NIGHT-03',
        'An explicit fixed-F2 smooth projective model has four-dimensional coherent cohomology with hard Frobenius',
r'''From the fixed-$\mathbb F_4$ hypersurface $X=V(G)$ of NN-C031, with $G=H+\omega F$ in $r$ coordinates, one can deterministically construct a smooth geometrically integral projective scheme
\[
             W\subset\mathbb P^{r^2-1}_{\mathbb F_2},
              \qquad W\simeq\operatorname{Res}_{\mathbb F_4/\mathbb F_2}X.
\]
It has a polynomial-size homogeneous circuit-equation presentation consisting of $O(r^4)$ quadratic equations and $O(r)$ degree-$r$ equations. Put $d=r-2$, which is odd. Its coherent cohomology is
\[
 H^0(W,\mathcal O)=\mathbb F_2,\quad
 H^d(W,\mathcal O)=\mathbb F_2^2,\quad
 H^{2d}(W,\mathcal O)=\mathbb F_2,
\]
and every other group vanishes. In explicitly descended bases, absolute Frobenius is respectively
\[
                   1,\qquad
              c\begin{pmatrix}0&1\\1&0\end{pmatrix},
                   \qquad c,
\]
where $c$ is the original satisfying-assignment parity. Thus the entire coherent realization has dimension four, its basis is supplied, and one of its one-dimensional Frobenius scalars is parity-counting complete over the fixed prime field.

Moreover
\[
 \#W(\mathbb F_2)=\#X(\mathbb F_4),\qquad
 \#W(\mathbb F_2)\equiv1+c\pmod2,\qquad
 Z(W/\mathbb F_2,T)\equiv\frac{1-cT}{1-T}\pmod2.
\]
These yield deterministic parity-counting-complete problems on the encoded family. Every output is smooth projective and has pure l-adic cohomology. The presentation uses a projective system of equations; it is not asserted to be a hypersurface over $\mathbb F_2$.''',
        inputs,
r'''Write $K=\mathbb F_4$ and let $\sigma$ be its nontrivial automorphism, so $\sigma(\omega)=\omega^2=\omega+1$. Use $r^2$ homogeneous coordinates over $\mathbb F_2$: diagonal coordinates $a_i$, and coordinates $b_{ij},c_{ij}$ for every $i<j$. Form the matrix with entries in $K[a,b,c]$
\[
 M_{ii}=a_i,\qquad
 M_{ij}=b_{ij}+\omega c_{ij},\qquad
 M_{ji}=b_{ij}+\omega^2 c_{ij}\quad(i<j).
\]
Coefficientwise conjugation, with the coordinate indeterminates held fixed, satisfies $\sigma(M)=M^{\mathsf t}$. For a polynomial $A$ over $K$ in these coordinates, write uniquely $A=A_0+\omega A_1$ with $A_0,A_1$ over $\mathbb F_2$.

Define $W$ by the following homogeneous equations over $\mathbb F_2$: both coefficient components of every two-by-two minor of $M$, and both components of
\[
                     G(M_{1j},\ldots,M_{rj})
                       \quad(1\leq j\leq r).
\]
This is a closed projective scheme. There are $2\binom r2^2=O(r^4)$ minor equations and $2r$ column equations, with degrees two and $r$ respectively; redundant or zero equations may be retained.

We identify this scheme after the faithfully flat extension $K/\mathbb F_2$, including its scheme structure. On each off-diagonal pair, the coordinate change
\[
        (b_{ij},c_{ij})\longmapsto(M_{ij},M_{ji})
\]
has determinant $\omega^2-\omega=1$, so over $K$ the entries of $M$ are independent matrix coordinates. Imposing both $\mathbb F_2$ coefficient components of a polynomial is equivalent over $K$ to imposing that polynomial and its coefficientwise conjugate. For the minors the conjugates are other minors of the transpose, already in the list. Thus their equations define the ordinary projective rank-one matrix scheme.

Here is the exact scheme-theoretic chart check. On a projective chart where $M_{ij}$ is nonzero, normalize it to one. The minors force
\[
                         M_{kl}=M_{kj}M_{il}.
\]
The remaining entries of column $j$ and row $i$ are free coordinates, giving the standard affine chart of
$\mathbb P^{r-1}\times\mathbb P^{r-1}$ under the Segre map $(z,w)\mapsto zw^{\mathsf t}$. These charts cover the projective minor scheme, so no extra embedded component is being discarded. This is the explicit minor form of the Segre embedding in Stacks27.13.6.

Under $M=zw^{\mathsf t}$, the column equations are
\[
                      w_j^rG(z)=0\quad(1\leq j\leq r).
\]
Their conjugates are the row equations
\[
                      z_i^rG^\sigma(w)=0\quad(1\leq i\leq r),
             \qquad G^\sigma=H+\omega^2F.
\]
Locally on the product of projective spaces some $z_i$ and some $w_j$ are units, so the generated sheaf of ideals is exactly $(G(z),G^\sigma(w))$. This proves an isomorphism of schemes
\[
                         W_K\simeq X\times_K X^\sigma.
\]
In these matrix coordinates the descent automorphism conjugates coefficients and transposes $M$; it therefore interchanges the two factors with their conjugation data. This is precisely the descent datum of restriction of scalars for the quadratic extension. More formally, $K\otimes_{\mathbb F_2}K\simeq K\times K$, so the restriction-of-scalars functor base-changes to $X\times X^\sigma$, with that same factor exchange. The functor is an fppf sheaf and commutes with base change by Stacks97.11.1--97.11.2. The displayed compatible isomorphism over the faithfully flat cover thus descends to an identification of its sheaf with the represented sheaf of $W$. This proves the claimed Weil-restriction identification; no general projectivity theorem for restriction of scalars is needed because the projective equations are already explicit.

Both $X$ and $X^\sigma$ are smooth by NN-C031. Their product is smooth, and smoothness descends under the finite faithfully flat extension by Stacks35.23.29. Hence $W$ is smooth over $\mathbb F_2$, of dimension $2(r-2)=2d$. Over an algebraic closure, each factor has only the ground field as its degree-zero coherent cohomology, by NN-C023's Cech calculation. The same is true of the product by coherent Kunneth. It is therefore connected, since a decomposition into two open-and-closed pieces would give a nontrivial idempotent in its global functions. A smooth scheme over a field has regular local rings by Stacks33.25.3, and regular local rings are domains by Stacks10.106.2; distinct irreducible components consequently cannot intersect. Thus this connected smooth geometric scheme is integral. This proves geometric integrality of $W$ as well.

We now compute its full coherent Frobenius, taking care with descent and semilinearity. Over $K$, let $e$ be the canonical basis of $H^d(X,\mathcal O_X)$ from NN-C023 and let $e'$ be its conjugate basis on $X^\sigma$. Coherent Kunneth (Stacks33.29.1) and flat base change (Stacks30.5.2) show that the only cohomology groups of $W_K$ are
\[
 K\quad\text{in degree }0,\qquad
 Ke\oplus Ke'\quad\text{in degree }d,\qquad
 K(e\mathbin\cup e')\quad\text{in degree }2d.
\]
Here $e,e'$ in the middle line mean their pullbacks from the two factors. The Kunneth isomorphism is the pullback-and-cup-product map, so it is compatible with Frobenius and the factor exchange, including its graded sign.

The descent automorphism is semilinear on coefficients and sends $e$ to $e'$ and $e'$ to $e$. Thus the following middle vectors are fixed:
\[
                    v_1=e+e',\qquad
                    v_2=\omega e+\omega^2e'.
\]
They are independent over $K$, because the determinant of their coefficients is $\omega^2-\omega=1$. Their fixed coefficient combinations are exactly their $\mathbb F_2$ span. The top vector $w=e\cup e'$ is also fixed: exchange gives $e'\cup e=(-1)^{d^2}e\cup e'$, and this sign is one in characteristic two. Hence $v_1,v_2,w$ are explicit descended bases over $\mathbb F_2$. This also follows by taking the invariant vectors in the flat-base-change isomorphism; it does not require computing any unknown Frobenius entry.

Let $\mathfrak F$ denote absolute Frobenius on coherent cohomology. On the two factors, NN-C031 gives
\[
                \mathfrak F(e)=\omega c\,e,
                \qquad\mathfrak F(e')=\omega^2c\,e',
 \qquad \mathfrak F(a\xi)=a^2\mathfrak F(\xi).
\]
Under flat base change from $\mathbb F_2$ to $K$, this absolute Frobenius corresponds to Frobenius on $H^*(W,\mathcal O_W)$ tensored with squaring on $K$, not with the identity on $K$. Absolute Frobenius is natural for the displayed isomorphism with the product. Restricting its semilinear action to the descended $\mathbb F_2$ vectors therefore computes the original $\mathbb F_2$-linear Frobenius on $W$ exactly.
Applying these formulas to the descended middle basis gives
\[
       \mathfrak F(v_1)=c v_2,\qquad
       \mathfrak F(v_2)=c v_1.
\]
For example, the coefficient of $e$ in the second identity is
$\omega^2\omega c=c$, and the other coefficient is
$(\omega^2)^2\omega^2c=c$. Cup-product compatibility gives
\[
                 \mathfrak F(w)=\omega\omega^2c^2w=cw.
\]
On degree zero it is the identity over $\mathbb F_2$. These computations prove exactly the three displayed matrices. As a separate consistency check, the square of the middle matrix is $cI$, agreeing with $4$-power Frobenius on both factors; the top scalar has square $c$ as required. The argument supplies a basis and a symbolic matrix description in terms of $c$, not a polynomial-time evaluation of that unknown bit.

There is also an elementary exact rational-point bijection, which does not use a trace formula. If $[z]\in X(K)$, define
\[
                            M=z\sigma(z)^{\mathsf t}.
\]
It is Hermitian and rank one. Replacing $z$ by $\lambda z$ for $\lambda\in K^*$ leaves it unchanged, since $\lambda\sigma(\lambda)=\lambda^3=1$. Every column is a scalar multiple of $z$, so the column equations vanish. Its diagonal entries belong to $\mathbb F_2$, and every off-diagonal pair has the unique displayed $(b_{ij},c_{ij})$ coordinates in $\mathbb F_2$. Thus it defines an $\mathbb F_2$ point of $W$.

Conversely, an $\mathbb F_2$ point gives a nonzero Hermitian rank-one matrix over $K$. It has a nonzero diagonal entry. If every diagonal were zero, the minor relation
$M_{ij}M_{ji}=M_{ii}M_{jj}$ would force every off-diagonal entry to vanish, since $M_{ij}M_{ji}$ is its nonzero norm whenever $M_{ij}\ne0$. This would give the zero matrix. Choose $i$ with $M_{ii}=1$, and let $z$ be column $i$. The minors give $M=z\sigma(z)^{\mathsf t}$, with $z_i=1$. The column equation implies $G(z)=0$. The column space recovers $[z]$ uniquely. These two constructions are inverse, proving
\[
                             \#W(\mathbb F_2)=\#X(K).
\]
Projective scaling on the $\mathbb F_2$ matrix coordinates introduces no additional quotient, since $\mathbb F_2^*=\{1\}$.

For the full zeta congruence, apply SGA7 II XXII3.1 to the just-computed coherent Frobenius. The degree $d$ is odd and $2d$ is even. The middle determinant is
\[
       \det\left(I-Tc\begin{pmatrix}0&1\\1&0\end{pmatrix}\right)
                      =1-c^2T^2=(1-cT)^2
\]
in $\mathbb F_2[T]$. Dividing by the degree-zero and top determinants gives
\[
     Z(W/\mathbb F_2,T)\equiv
         \frac{(1-cT)^2}{(1-T)(1-cT)}
                   =\frac{1-cT}{1-T}\pmod2.
\]
The point-count congruence is also immediate from the exact bijection and NN-C031. The full series congruence is obtained from the coherent determinants, not inferred merely from parity of the first point count. Deligne's theorem applies to the smooth projective $W$, giving the actual pure l-adic realizations independently of this characteristic-two calculation.

All constructions are effective with polynomial output length. A $K$ arithmetic gate can be replaced by constantly many $\mathbb F_2$ gates computing its two coordinate components: for example
\[
 (a+b\omega)(u+v\omega)
                  =(au+bv)+(av+bu+bv)\omega.
\]
The $O(r^4)$ minors have constant-size circuits, and substituting each of the $r$ columns into $G$ multiplies its circuit size by at most $r$, up to a constant coordinate-arithmetic factor. There are only $r^2$ projective coordinates. No expansion of $G$ into all monomials is required, and no factorization or Galois-descent oracle is hidden in these formulas.

The source-to-$W$ construction is a deterministic polynomial-time reduction. Extracting the top Frobenius scalar is exactly extracting $c$, so it is $\oplus\mathrm P$-hard and is in $\oplus\mathrm P$ on the syntactic input family through the factor-choice verifier of NN-C023. Point-count parity is directly in $\oplus\mathrm P$: guess the $r^2$ binary projective coordinates, reject the zero vector, and check the homogeneous circuit equations. Every nonzero binary vector is already a unique projective representative. Its output is $1+c$, which has the same parity-counting complexity; complementation preserves $\oplus\mathrm P$ by adding one distinguished accepting computation. Thus the point-parity decision language is also complete under deterministic many-one reductions. A polynomial-time algorithm for either geometric task gives $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$ as before.

E evaluates $c$ through the original formula before its geometric padding and descent. The extra construction cost is polynomial in that source size. A and M are unused. The geometric input is a prescribed homogeneous circuit-equation family with its mechanically generated format; no polynomial-time recognition theorem for arbitrary smooth projective presentations is being asserted.''',
        'Complete explicit projective descent, scheme-structure, coherent-Frobenius, point-bijection and complexity proofs; independent review pending.',
r'''The hard coherent-Frobenius gate now occurs over the fixed prime field, in a smooth geometrically integral projective scheme with a supplied four-dimensional coherent basis. Neither random specialization, growing coefficient fields, singular fibers, unknown coherent rank nor unknown basis is the missing operation. The single bit $c$ is still parity-counting complete. The total l-adic rank and expanded equation size are not claimed polynomial. This identifies a concrete remaining scalar-extraction gate inside an actual pure finite Weil realization; it does not supply GCT's canonical-basis functor or an unconditional circuit lower bound.''',
r'''Let $X=V(H+\omega F)/\mathbb F_4$ be a hypersurface of NN-C031. The displayed Hermitian-matrix equations define a projective $\mathbb F_2$ scheme $W$ whose base change is the Segre product $X\times X^\sigma$ and whose descent datum is factor exchange. Thus $W$ represents the Weil restriction. It is smooth and geometrically integral, with coherent cohomology only in degrees $0,d,2d$, of ranks $1,2,1$. In the explicit descended bases $1$, $(e+e',\omega e+\omega^2e')$, and $e\cup e'$, its Frobenius operators are $1$, $c\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, and $c$. Its exact rational-point bijection with $X(\mathbb F_4)$ and its proper zeta congruence are proved above.

The scheme-theoretic interfaces are the explicit Segre chart proof with Stacks27.13.6, restriction-of-scalars sheaf/base-change Lemmas97.11.1--97.11.2, smoothness descent Lemma35.23.29, coherent flat base change Lemma30.5.2 and coherent Kunneth Lemma33.29.1. SGA7 II XXII3.1--3.2 supplies the coherent zeta congruence and Deligne Weil I1.6 supplies purity. These are exact locators, with no original Grothendieck archive cote claimed. The formula for the descended middle matrix is proved by semilinear arithmetic and cup-product compatibility, not guessed from point counts. The underlying count reduction and E evaluator are unchanged; the new construction removes the fixed-field obstruction while preserving an explicit small coherent realization.''',
        inputs)
