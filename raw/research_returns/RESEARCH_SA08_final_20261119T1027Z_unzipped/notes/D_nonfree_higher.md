# Higher horizontal tests of the nonfree standard-tail image

2026-11-19, /root/shadows_coalgebras. This supplements D-027; it does not establish eventual admissibility.

## A proved finite higher class

The actual integral simplicial image has

\[
\pi_3(D_2^{4,1}(\mathbb Z))=\mathbb Z/2.
\]

This is an exact finite matrix result, with all matrices and bases saved in `logs/D_tail_H3_certificate.json` by `code/D_tail_H3_certificate.py`. Runtime: 0.10439396199944895 seconds.

To justify the normalized matrices, use cumulative coordinates \(T,X_1,\ldots,X_n\). The image has a multidegree decomposition: in multidegree \(\alpha\), the integral lattice is spanned by the vectors \(a\,df\), where \(a+f=\alpha\), the differentiated factor has total weight at least \(N\), and the coefficient is either supported on \(T\) alone or has weight at least \(N\). The coefficient of the basis one-form with differential \(dX_j\) is

\[
\prod_{i=0}^n\binom{\alpha_i-\delta_{ij}}{a_i}
\]

when \(f_j>0\), and zero otherwise. The HNF of these integer columns is an actual free basis of the integral image lattice. A missing variable \(X_j\) is exactly a simplicial degeneracy. Since each multidegree summand missing that variable is the image of the identical lattice calculation in one fewer variable, the normalized quotient of the image embeds in the normalized quotient of the ambient forms. It is computed by retaining precisely the multidegrees with \(\alpha_j\ge1\) for all \(j>0\).

At \(N=2,w=4\), normalized ranks in simplicial dimensions \(1,2,3,4\) are \(4,12,12,4\), and there are no terms above dimension four. The script constructs all alternating face maps, using the same cumulative-coordinate faces as D-027, and verifies their composites vanish.

For \(d_4:\mathbb Z^4\to\mathbb Z^{12}\), the gcd of all 495 four-by-four minors is 2. A three-by-three minor, rows \((0,3,9)\) and columns \((1,2,3)\), is 1. Thus the nonzero Smith factors are \(1,1,1,2\), and \(d_4\) has rank four. An explicitly stored eight-by-eight minor of \(d_3\) has determinant 24. Since \(d_3d_4=0\), its rank is at most eight and therefore exactly eight. Consequently the free rank of \(H_3\) is \(12-8-4=0\). The exact sequence

\[
0\longrightarrow H_3\longrightarrow\operatorname{coker}d_4
\longrightarrow\operatorname{im}d_3\longrightarrow0
\]

has free last term, so its torsion is exactly the torsion of \(\operatorname{coker}d_4\), namely \(\mathbb Z/2\). This proves the claim independently of a black-box Smith-normal-form output.

## Broader finite computations

`code/D_tail_integral_horizontal.py` computes actual integral HNF lattices and Smith factors in horizontal degrees 1 through 3. In 11 cases \(N=2,3\), \(N\le w\le7\), the only positive higher class is the preceding \(\mathbb Z/2\) and \(\pi_3(D_3^{6,1})=\mathbb Z/3\). The first-homotopy results agree with D-027. Output: `logs/D_tail_integral_horizontal.json`; final runtime 0.7971489670017036 seconds. The initial exploratory run attempted weight eight using SymPy's generic symbolic `.rank()` and was interrupted after the weight-seven partial output; the final script uses the exact integer-domain rank operation and saves incremental output. No interrupted calculation is used as a certificate.

`code/D_tail_integral_modp.py` reduces the **integral HNF lattices** modulo \(p\), then computes every normalized horizontal degree. This does not take the smaller image after reduction. In 32 cases, \(N=2,w=4,5,6,7,8\) and \(N=3,w=6,7,8\), with \(p=2,3,5,7\), the only nonzero groups are one-dimensional in degrees 3 and 4 at \((N,w,p)=(2,4,2),(3,6,3)\). This agrees with the universal-coefficient contributions of the integral third-homology classes. All normalized homology vanishes in the other 30 cases. Output: `logs/D_tail_integral_modp.json`; runtime 3.847327306000807 seconds.

The complete vanishing in these latter finite cases makes an eventual first-row bound above \(2N\) plausible, but provides neither an all-weight theorem nor evidence about all form degrees. The isolated weight-four and weight-six classes do not themselves obstruct eventual admissibility.

## Remaining construction issue

Even a proof that every \(D_N\) is admissible would not make these objects comparison sources for arbitrary targets: their degree-zero rows are standard tails, and C13 rules out maps from those tails to certain admissible targets already over \(\mathbb Q\). A universal construction would have to replace the degree-zero tail by a common resolution that maps to the selected targets, then choose genuinely nonfree differential relations without losing the simplexwise coefficient resolution or introducing extra degree-zero constants. A bare quotient by the C15 detector \(du_p\) makes \(u_p\) vertically closed and therefore fails. No such compatible quotient has been constructed here.

## A proved absolute-to-relative intersection reduction

For a free module \(V\), let \(E_N(V)\) be the differential subalgebra of the absolute PD de Rham algebra \(\Gamma(V)\otimes\Lambda(V)\) generated by all functions of weight at least \(N\), together with the scalar unit. Its positive form-degree part consists of sums

\[
a_0\,da_1\cdots da_q,
\]

where every \(a_i\), \(i>0\), has weight at least \(N\), and \(a_0\) is either a scalar or has weight at least \(N\). This differential subalgebra is closed under the standard divided powers: each decomposable positive even form has all higher divided powers zero, and the divided powers of a sum expand as sums of products of distinct summands. Thus imposing PD closure adds no further positive-form generators to this description.

The functor \(V\mapsto E_N^{w,q}(V)\) preserves simplicial linear homotopies: apply it to the maps defining such a homotopy, whose relations are equalities of composites and hence remain valid under any functor. As \(\Phi\) is simplicially linearly contractible and \(E_N^{w,q}(0)=0\) for \(w>0\), every positive-weight simplicial row \(E_N^{w,q}(\Phi)\) is contractible.

Projection from absolute to relative forms sends \(dT\) to zero. For \(q>0\), its image on \(E_N\) is exactly \(D_N^q\). The only extra coefficient allowed in the latter is a low-weight element of \(S\), and such a coefficient can be absorbed into the first differentiated function:

\[
c(T)\,df_1\cdots df_q
=d(c(T)f_1)\,df_2\cdots df_q
\quad\text{modulo }dT.
\]

The weight of \(c(T)f_1\) remains at least \(N\). Higher coefficients are already allowed in \(E_N\). Define the intrinsic intersection

\[
K_N^{w,q}=E_N^{w,q}(\Phi)\cap
\bigl(dT\wedge F^{w-1,q-1}\bigr)
\subset\Gamma(\Phi)\otimes\Lambda(\Phi).
\]

The exterior inclusion is canonical: lifts of relative forms give the same wedge with \(dT\), and the marked line splits in each simplicial degree. Consequently there is an exact sequence

\[
0\longrightarrow K_N^{w,q}\longrightarrow E_N^{w,q}(\Phi)
\longrightarrow D_N^{w,q}\longrightarrow0,
\qquad q>0.
\]

It gives canonical isomorphisms

\[
\pi_j(D_N^{w,q})\cong\pi_{j-1}(K_N^{w,q}),\qquad j\ge1,
\]

and \(\pi_0(D_N^{w,q})=0\). Thus the remaining eventual first-row problem is precisely the eventual acyclicity of the marked-line intersection \(K_N^{w,1}\subset\Gamma^{w-1}(\Phi)dT\). No bound for those intersections is proved by this reduction. For example, if \(J=\Gamma^{\ge N}(\Phi)\), then \(J^2dT\subset K_N^1\), because

\[
fg\,dT=f\,d(Tg)-(Tf)\,dg\qquad(f,g\in J).
\]

This large functorial submodule is contractible in positive weights, but controlling the quotient still requires a proof; it cannot be inferred merely from the contraction of its numerator or denominator.
