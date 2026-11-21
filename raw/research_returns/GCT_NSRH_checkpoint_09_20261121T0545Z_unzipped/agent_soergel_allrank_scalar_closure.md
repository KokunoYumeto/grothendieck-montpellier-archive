# F59 amendment: arbitrary bounded scalar coefficients in every ordinary type-A rank

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This report combines the fully checked descending-cohomology argument with the all-variable tensor-dimension application developed by /root/rectangular_and_theta. The latter is agent_soergel_top_module_all_variables.md, SHA256 b5a655cbc1748433c10cb29912d07f4af929ed60c03b52314f97cec739925de1. The complete elementary two-variable proof is preserved independently in agent_soergel_rankone_scalar_closure.md, SHA256 3272f93b6fe00db9d2f09c4e9bebc0d2e0dc18c6cc57e021680a24efa5dacb8f.

The new higher-dimensional input is a cited known theorem of Lichtenbaum. Its hypotheses are checked explicitly below. No specialization of spectator variables, unproved rank-one restriction, or claim that all torsion-free modules have projective dimension one is used.

## 1. Exact statement

Let k have characteristic zero and let A be the standard degree-two polynomial realization of the ordinary Soergel category for \(W=S_n\times S_n\), with n at least two. This includes the reflection realization and the permutation realization with its fixed coordinates. Fix a simple reflection s in each factor and put \(\tau=(s,s)\). The minus eigenspace of \(\tau\) has dimension two. Choose linear coordinates

\[
 A=k[x,y,z_1,\ldots,z_{N-2}],\qquad
 \tau(x)=-x,\quad\tau(y)=-y,\quad\tau(z_j)=z_j.
 \tag{AR1}
\]

Put \(\delta=v+v^{-1}\). Let X be a bounded ordinary Soergel complex with the actual ambient Hecke Euler class

\[
 [X]=b_s\otimes b_s+(b_s-\delta)\otimes(b_s-\delta).
 \tag{AR2}
\]

Let C be a bounded complex of finite graded k-vector spaces with

\[
 \chi_v(C)=\sum_{i,e}(-1)^i\dim_kH^i(C)_e\,v^e=\delta^2.
 \tag{AR3}
\]

### Theorem AR-A

There is no such pair admitting an actual isomorphism

\[
 X\otimes_A^{\mathbf L}X\simeq C\otimes_kX
 \tag{AR4}
\]

in the graded derived category of A-bimodules. Therefore no bounded homotopy-level ordinary Soergel construction with these data exists either.

This closes the nonflat-cohomology scalar-complex case in every stated type-A rank directly over its ambient polynomial ring. The coefficient remains a complex of scalar k-vector spaces; a complex of unit bimodules with nonconstant polynomial differentials is not automatically included. Changed ambient Euler classes, different categories, localization, and unbounded enlargement are not excluded by AR-A.

## 2. The known local theorem used

Lichtenbaum, On the vanishing of Tor in regular local rings, Illinois Journal of Mathematics 10(2) (1966), 220--226, Theorem 2, pp. 222--223, applies to a complete unramified regular local ring B and finite B-modules. The needed statements are:

- higher Tor Euler characteristics \(\chi_i\), when defined by finite lengths, are nonnegative;
- \(\chi_1=0\), with at least one module torsion-free, forces \(\operatorname{Tor}_1=0\);
- one vanishing positive Tor forces all subsequent Tor groups to vanish.

These are parts (2), (4), and (1), respectively. We apply them over the equicharacteristic power series ring \(k[[x_1,\ldots,x_N]]\), after replacing the arbitrary module by its torsion-free quotient.

The original author's uploaded article was opened and its full theorem plus proof context read at

https://www.researchgate.net/publication/247050802_On_the_vanishing_of_Tor_in_regular_local_rings

DOI: https://doi.org/10.1215/ijm/1256055103

My direct source reference is turn707593017view0. The extraction drops some subscripts, but the theorem structure and torsion-free clause are explicit. As an independent primary-author check of the exact field case and indices, I opened and read Hochster's Math 615, Winter 2012, supplementary lecture April 18, printed p. 169, Corollary (S. Lichtenbaum), case (1), at

https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/10/615W12.pdf

direct source reference turn707593017view1. The field case explicitly gives nonnegativity and vanishing exactly when all subsequent Tor groups vanish. The proof reduces the Tor assertion to the preceding Koszul-homology result. This report uses the weaker original torsion-free form and does not require the inaccessible 1984 Hochster paper.

Completion flatness and faithful flatness are Stacks Lemmas 10.97.2 and 10.97.3, tags 00MB and 00MC, independently opened and read:

https://stacks.math.columbia.edu/tag/00MB

https://stacks.math.columbia.edu/tag/00MC

Direct references turn281442546view1 and turn281442546view2. The applications below mainly need flatness; no completion argument is used to conceal a change of cohomology.

These are cited known results, not claimed as new theorems or reproved in this report. Retrieval status is web text, with an opened primary PDF for the lecture notes; no successful local PDF download or original-article visual audit is claimed.

## 3. Tensor dimension in every polynomial dimension

Let \(A_0=k[x_1,\ldots,x_N]\) with all variable degrees positive and \(\mathfrak m=(x_1,\ldots,x_N)\). Let V be a nonzero finite-dimensional graded right A_0-module and M a finite graded left A_0-module of rank r.

### Lemma AR-B

\[
 \dim_k(V\otimes_{A_0}M)\ge r\dim_kV,
 \tag{AR5}
\]

with equality if and only if M is graded free.

### Proof

For N=0 this is immediate. First suppose M=Q_0 is torsion-free. Construct its minimal graded free resolution F by homogeneous generators of the successive syzygies. The N-variable Koszul resolution of k implies \(\operatorname{Tor}_i^{A_0}(k,Q_0)=0\) for i>N. Minimality identifies this Tor with \(F_i/\mathfrak mF_i\); thus F is finite. If f_i is the rank of F_i, localization gives \(\sum_i(-1)^if_i=r\).

The right action of \(\mathfrak m\) on V is nilpotent by its finite grading. Consequently the tensor complex \(V\otimes F\) consists of finite-dimensional spaces, its Euler characteristic is \(r\dim_kV\), and

\[
 \dim_k(V\otimes Q_0)-r\dim_kV
    =\chi_1^{A_0}(V,Q_0).
 \tag{AR6}
\]

Localize at \(\mathfrak m\) and complete to
\(B=k[[x_1,\ldots,x_N]]\). This ring is complete, equicharacteristic, regular and unramified in the sense of the cited theorem. A finite torsion-free module over the domain A_0 embeds in a finite free module: choose a fraction-field basis and clear the finitely many denominators of a finite generating set. Flatness of completion preserves that injection. Hence \(\widehat Q_0=B\otimes_{A_0}Q_0\) is torsion-free over B.

Because \(\mathfrak m^aV=0\) for some a, extension to B leaves V unchanged. The completed resolution \(B\otimes F\) computes exactly the same tensor complex \(V\otimes F\). All Tor modules have finite length, and their B-lengths equal their k-dimensions, since the residue field is k. Thus the known local theorem applies with every required hypothesis verified. It gives \(\chi_1\ge0\).

If equality holds in AR6, Lichtenbaum's part (4) gives \(\operatorname{Tor}_1^B(V,\widehat Q_0)=0\), and part (1) gives vanishing of every positive Tor. If Q_0 were not graded free, its finite minimal resolution would have a last nonzero term F_t with t>0. Completion preserves its minimal differential entries in the maximal ideal. The nonzero socle of V, tensored with each free generator of F_t, lies in the kernel of that final differential. There is no incoming term beyond F_t. Hence \(\operatorname{Tor}_t^B(V,\widehat Q_0)\ne0\), a contradiction. Therefore equality implies Q_0 is graded free. The converse is immediate.

For arbitrary M, let T be its full graded torsion submodule and \(Q_0=M/T\). The quotient is finite graded torsion-free of rank r. If Q_0 is not free, strictness for \(V\otimes Q_0\) and the surjection \(V\otimes M\to V\otimes Q_0\) give strictness for M. If Q_0 is free, lift a homogeneous basis to split the quotient as a left-module map, so M is Q_0 direct sum T as a left module. If T is nonzero, \(V\otimes T\) surjects onto

\[
 (V/V\mathfrak m)\otimes_k(T/\mathfrak mT)\ne0.
\]

The factors are nonzero by graded Nakayama. Strictness follows again. Equality holds exactly when T=0 and Q_0 is free. This proves AR-B. The splitting is one-sided only. QED.

## 4. Generic actual cohomology and the global top

Let \(M_i=H^i(X)\), \(c_i=\dim_kH^i(C)\), and let Q be the ungraded fraction field of the actual ambient A in AR1. The exact ordinary graph localization has simples Q_g, g in W, with tensor product indexed by group multiplication. If

\[
 F(u)=\sum_{g\in W}f_g(u)g,\quad f_g\in\mathbb N[u,u^{-1}],
 \qquad d(u)=\sum_i c_iu^i,
\]

then the actual quadratic gives \(F^2=dF\) by generic Künneth. The ambient Euler classes give
\(F(-1)=2(e+\tau)\), \(d(-1)=4\).

Augmentation gives \(\sum_gf_g=d\). For each positive real u, \(f_g(u)/d(u)\) is an idempotent probability measure on the finite group. Its support is a fixed subgroup, and taking a maximal coefficient in the convolution identity shows that the measure is uniform there. Equality on all positive u is a Laurent-polynomial identity. The Euler support forces that subgroup to be exactly \(\{e,\tau\}\). Therefore

\[
 F(u)=\frac{d(u)}2(e+\tau),\qquad
 \operatorname{rank}_A M_i=c_i.
 \tag{AR7}
\]

This argument works in the full finite group \(S_n\times S_n\); it does not pass to a rank-one subcategory. Internal grading is explicitly forgotten at this step, as generic localization identifies some shifts.

For any nonzero finite graded A-bimodule M, finite on the left, its tensor square is nonzero. To see this put \(V=k\otimes_A M\); it is a nonzero finite-dimensional graded right origin module. The left-origin quotient of \(M\otimes_AM\) surjects onto
\((V/V\mathfrak m)\otimes_k(M/\mathfrak mM)\ne0\).

Let a be the highest global cohomology degree of X and c that of C. The top-truncation identity

\[
 H^{2a}(X\otimes_A^{\mathbf L}X)
       =M_a\otimes_AM_a\ne0
\]

and scalar Künneth force c=a. If b is the highest generic cohomology degree, total graph dimensions multiply, so the generic quadratic forces \(2b=b+c\). Thus b=c=a and \(r=\operatorname{rank}M_a=c_a>0\). The actual top relation is

\[
 M_a\otimes_AM_a\simeq H^a(C)\otimes_kM_a.
 \tag{AR8}
\]

Take its left-origin fiber and apply AR-B with \(V=k\otimes_AM_a\). The scalar multiplicity c_a equals rank r, so equality in AR5 holds. Hence M_a is graded left-free.

## 5. Global graph splitting and the complete induction

If a cohomology module is graded left-free, its generic support in e and \(\tau\) gives a global graph splitting. In the coordinates AR1, let U,V be right multiplication by x,y. Generically \(yU=xV\) and \(U^2=x^2I\); torsion-freeness extends these identities to A. Coprimality yields \(U=xZ,V=yZ,Z^2=I\). Every fixed z_j acts by its left scalar, first generically and then globally. The idempotents \((I\pm Z)/2\) are bimodule endomorphisms with graph types e and \(\tau\).

Their images are finite graded projective left modules, hence graded free: lift a homogeneous residue basis to a split free surjection and use graded Nakayama on its complementary kernel. Thus they are sums of actual shifted graph modules, and are also right-free. This argument is unchanged by the spectator coordinates; no specialization is used.

Starting with the free graph module M_a, assume all M_i for i>s are free graph modules. The canonical cycle cross-product is an isomorphism

\[
 \bigoplus_{i+j=a+s}M_i\otimes_AM_j
       \longrightarrow H^{a+s}(X\otimes_A^{\mathbf L}X).
 \tag{AR9}
\]

Here is the one-sided proof. Forget the left action. In the bounded right-projective complex X, split off the projective cohomology in degrees i>s successively from the top, cancelling acyclic top tails and contractible pairs. This leaves a right-projective complex with cohomology at most s and top M_s. Tensoring the higher summands with the second X gives \(M_i\otimes M_{a+s-i}\); the remaining top tensor group is \(M_s\otimes M_a\) by top truncation. These are exactly all summands of AR9. The resulting map is the canonical cycle cross-product. Its one-sided verification proves bijectivity, and its intrinsic bimodule linearity proves AR9 as a bimodule isomorphism. No bimodule formality is assumed.

Write \(\phi(N)=\dim_k(N/\mathfrak mN)\), put \(z=\phi(M_s)\), and retain \(r=c_a>0\). Both \(M_a\otimes M_s\) and \(M_s\otimes M_a\) have left-origin fiber dimension r z. A graph twist on either side preserves this dimension because every graph automorphism here fixes the homogeneous origin. Every other summand in AR9 is already graph-free, contributing

\[
 S_s=\sum_{\substack{i+j=a+s\\i>s,\ j>s}}c_i c_j.
\]

The left side of the actual quadratic has fiber dimension \(2rz+S_s\). Scalar Künneth on its right gives dimensions \(rz+rc_s+S_s\): the exceptional terms are \(H^a(C)\otimes M_s\) and \(H^s(C)\otimes M_a\), and AR7 identifies all remaining free ranks. Therefore

\[
 2rz+S_s=rz+rc_s+S_s,\qquad
 \phi(M_s)=c_s=\operatorname{rank}M_s.
 \tag{AR10}
\]

If c_s=0, graded Nakayama makes M_s zero. Otherwise its minimal graded free surjection has rank c_s and a rank-zero kernel inside a free module over a domain. The kernel is zero, so M_s is left-free. The graph splitting makes it right-free as well. This completes the descending induction in the ambient polynomial ring of any finite dimension.

## 6. The restored full grading is incompatible with the scalar Euler class

All cohomology is now a sum of globally defined shifted e- and \(\tau\)-graphs. Its character is \(a(v,u)e+b(v,u)\tau\), where a,b have nonnegative integral Laurent coefficients and b is nonzero. Put

\[
 d(v,u)=\sum_{i,e}\dim_kH^i(C)_e\,v^eu^i.
\]

One-sided splitting into right-projective cohomology now proves that the canonical cross-product Künneth map is a bimodule isomorphism in every degree. No maps connect distinct graph types, since their coefficients would be killed by 2x. Within each type the graded origin fiber determines multiplicities. Thus AR4 gives

\[
 a^2+b^2=da,\qquad 2ab=db.
\]

The integral Laurent polynomial ring is a domain and b is nonzero, so d=2a. Evaluating at u=-1 gives

\[
 v^2+2+v^{-2}=2a(v,-1),
\]

which contradicts the odd outer coefficients. This proves AR-A.

This final use of internal degree is global, after graph freeness has been proved. It is not the invalid generic full-grading argument that the earlier scalar report expressly ruled out.

## 7. Consequences, exact limits and the separate dictionary

The entire bounded scalar-complex alternative in the fixed ordinary type-A Soergel category is now excluded, even for derived rather than homotopy quadratics. There is no unresolved nonflat-cohomology case under these exact premises. A single named generator already fails its actual quadratic, so requiring simultaneous higher-rank relation maps cannot repair it.

The result does not exclude non-scalar central complexes, polynomial differentials in coefficient objects, changed K0 embeddings, nonproper sheaf convolution in a different category, the finite-state graded kernel model, unbounded categories or localizations. It does not prove or refute a general nonstandard canonical basis conjecture. No arithmetic Frobenius comparison, purity or designated basis is inferred from the theorem.

EGA I Theorem 1.3.7 p. 86, Corollary 1.3.8 p. 87 and Theorem 1.4.1 pp. 90--92 supply the affine module/sheaf dictionary. SGA6 I Definition 4.7 pp. 121--122 and Example 4.8 p. 122 supply the bounded perfect-complex framework. The new use of local Tor rigidity is stated and cited separately; its equality case keeps actual positive Tor information that an Euler identity alone does not retain.

The internal grading is represented by the split torus of SGA3 I4.7.2--3, with cote90 scan17. Actual and virtual graded coefficient representations belong to SGA6 V Sections2--3, with cote133 scan18; the existing original-scan qualification for SGA6 V remains. These are framework anchors, not archive provenance for the theorem and not a noncommutative lambda-ring assertion. The ordinary source normalization is Elias--Williamson, Hodge theory, Sections3.3--3.5; the exact generic graph framework is Elias--Williamson, Localized calculus, Sections1.1--1.2, including equations1.1--1.2, Theorem1.6 and Remark1.7.

## 8. Review scope

The author read the entire all-variable module report b5a655cbc1748433c10cb29912d07f4af929ed60c03b52314f97cec739925de1 and reconstructed every completion, finite-length and socle step. The exact primary contexts listed in Section2 were independently opened and read. The full elementary two-variable report already has independent complete reviews by root and theta; this report does not replace that proof.

The author independently checked that every subsequent step uses only finite graded modules over a polynomial domain, the global two-dimensional minus eigenspace, exact generic graph localization, and projectivity of the previously established cohomology. None depends on the total number of variables. Fresh whole-proof review of this complete all-rank statement is requested from /root and /root/gct_statements, with a source/hypothesis match from /root/rectangular_and_theta. No main paper or shared master log was edited.
