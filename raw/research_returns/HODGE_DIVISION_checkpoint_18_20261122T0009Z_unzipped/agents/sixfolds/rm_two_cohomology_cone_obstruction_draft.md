# SF-E816: disjoint-class two-cohomology cones cannot be balanced RM seeds

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

**Status:** Whole-proof mathematical PASS reviews of §§1--6 were received from /root and /root/imprimitive on 2026-11-21 (GPT-6 Astra Pro; inherited effort not exposed). Root additionally read both complete written corollaries in §§7--8 and reported whole-proof PASS. Imprimitive independently read and approved the complete written SF-E816a proof, and verified that SF-E816b faithfully records his own complete derivation. The latter is contributor verification; root and sixfolds supplied its independent mathematical checks. The ordinary-gluable overlap argument in §7 was supplied by /root; the arbitrary-amplitude Postnikov argument in §8 was supplied by /root/imprimitive. Neither contribution is being promoted from an unwritten assertion: all proofs and maps are given below. The results permit negative virtual weights and nonsimple objects, within their precise factor and class hypotheses.

## 1. Statement and exact scope

Let \(X\) be a complex abelian fourfold with genuine real multiplication by a quadratic field \(F\), self-adjoint for a polarization \(\theta\), with holomorphic multiplicities \((2,2)\). Write

\[
 \theta=\theta_++\theta_-
\]

for its two real eigenspace components. Let \(G\subset X\times\widehat X\) be an effective finite subgroup with a specified coherent translation/tensor action of the kind in supplied DEG_L S-21. All equivariant objects below belong to this actual coherent action. No individual stable factor is assumed to admit its own linearization.

Let \(E\) be a perfect equivariant object whose only nonzero cohomology sheaves are the vector bundles

\[
 A=\mathcal H^0(E),\qquad B=\mathcal H^{-1}(E).
 \tag{E816.1}
\]

Assume that \(A\) and \(B\) admit filtrations by stable projectively flat vector bundles. For a factor \(Q\), call \(\beta(Q)=c_1(Q)/\operatorname{rk}Q\) its normalized divisor class. Require the following two conditions:

1. For any two unequal normalized classes occurring in either filtration, their difference is rational, block diagonal for the two real-multiplication planes, and primitive on each plane.
2. The sets of normalized classes occurring in \(A\) and in \(B\) are disjoint.

Line-bundle factors, with arbitrary degree-zero twists, are included. Factors and multiplicities may differ between the two sheaves; extensions within each normalized class are unrestricted.

Then it is impossible that both

\[
 e^D\operatorname{ch}(E)
  =N\left(1-\frac q2\theta_+^2\right)
      \left(1-\frac q2\theta_-^2\right),
 \qquad Nq\ne0,
 \tag{E816.2}
\]

for a rational algebraic divisor \(D\), and that the full invariant degree-two trace of \(E\) be injective. In particular no such object is a weakly \(G\)-semiregular balanced RM input, regardless of its equivariant endomorphism dimension. The parameter \(q\) may be positive, as in the intended input; the proof only needs it to be nonzero.

The theorem applies to every actual triangle

\[
 B[1]\xrightarrow{i}E\xrightarrow{p}A
       \xrightarrow{e}B[2],
 \qquad e\in\operatorname{Ext}^2_G(A,B),
 \tag{E816.3}
\]

with the stated factors. It does not assume any formality of a dg or \(A_\infty\) category. In particular it excludes the natural signed construction with all positive-class vertices in \(A\) and all distinct negative-class vertices in \(B[1]\), for every matrix of actual degree-two gluing classes.

## 2. Cross-Ext concentration and canonical class blocks

We give the requisite factor and filtration arguments rather than infer them from the Chern character. If a rational nonzero divisor difference \(\delta\) in hypothesis 1 vanished on one real-multiplication plane, its associated rational alternating form would be supported on the other. For an irrational field element \(u\in F\), one would have

\[
 \delta(ux,y)=\sigma(u)\delta(x,y)
\]

for all rational first-homology vectors \(x,y\), with \(\sigma(u)\) irrational. Both the left side and \(\delta(x,y)\) are rational. Choosing a pair with nonzero value contradicts irrationality. Thus both blocks of \(\delta\) are nonzero. A nonzero primitive Hermitian form on a complex two-plane has eigenvalues \(\lambda,-\lambda\), and hence signature \((1,1)\). The complete form of \(\delta\) is nondegenerate of signature \((2,2)\).

For stable projectively flat factors \(Q,R\), choose a positive integer \(m\) divisible by their ranks. We use the actual finite-isogeny splitting proved in SF-E813. Its construction is as follows. The stable factor has a Hermitian--Einstein connection for the polarization; its zero discriminant and the ordinary Chern--Weil energy identity make that connection projectively flat. For a rank-\(r\) factor \(Q\), the actual line bundle

\[
 L_Q=(\det Q)^{m^2/r}
\]

has the same harmonic scalar curvature as \([m]^*Q\). Consequently \([m]^*Q\otimes L_Q^{-1}\) is unitary flat. Its monodromy representation is a unitary representation of the abelian fundamental group, so it splits into characters. Therefore

\[
 [m]^*Q\simeq\bigoplus_{a=1}^{r}(L_Q\otimes P_a),
 \qquad P_a\in\operatorname{Pic}^0(X),
 \qquad c_1(L_Q)=m^2\beta(Q).
 \tag{E816.4}
\]

The same holds for \(R\) on this one cover. If their normalized classes are unequal, every line difference on the cover has signature \((2,2)\). The published Mumford index theorem gives cohomology only in degree two, including after every degree-zero twist. Finite étale pullback on Ext is injective: its composition with trace is multiplication by \(\deg[m]\ne0\). It follows that

\[
 \operatorname{Ext}^j(Q,R)=0\quad(j\ne2)
 \tag{E816.5}
\]

for unequal normalized classes. Negative Ext is already zero for sheaves; the assertion above degree four follows as well from the cover, or from Serre duality. The source is Mumford, *Abelian Varieties*, §16, the vanishing theorem on printed page 150, proof on pages 150--153, and the complex Hermitian-index corollary and proof on pages 162--163. The Hermitian--Einstein input is Siu, *Lectures on Hermitian--Einstein Metrics for Stable Bundles and Kähler--Einstein Metrics*, Chapter 1, §6.1--§6.4, in the rational polarization scope already recorded in SF-E811. No reflexive-sheaf extension is used.

The vanishing extends through filtrations in both arguments. Indeed, for a short exact sequence in one argument, its Ext long exact sequence shows that concentration in degree two for the two end terms implies the same concentration for the middle term. Induction first through one filtration and then through the other proves (E816.5) for any two vector bundles filtered entirely by unequal classes.

In particular their Hom and degree-one Ext vanish. These two vanishings give actual canonical class decompositions

\[
 A=\bigoplus_{\beta\in\mathcal A}A_\beta,
 \qquad
 B=\bigoplus_{\gamma\in\mathcal B}B_\gamma,
 \qquad\mathcal A\cap\mathcal B=\varnothing,
 \tag{E816.6}
\]

where each nonzero block is filtered entirely by its indicated normalized class. To see existence, induct through a filtration. If its last quotient has class \(\beta\), the extension by every already separated unequal-class block is zero in Ext degree one. Only the \(\beta\)-block can extend. This produces the direct sum in (E816.6). To see its canonicity, maps between two unequal-class blocks are zero. The projection of any second proposed \(\beta\)-block onto every different block is therefore zero, so the \(\beta\)-summand is uniquely determined as a subobject.

Translation and tensoring by \(\operatorname{Pic}^0\) preserve each rational normalized class, and are exact for the usual cohomological structure. The coherent action on \(E\) gives coherent actions on \(A,B\). Canonicity of (E816.6) then gives actual coherent equivariant structures on every \(A_\beta,B_\gamma\). No equivariant splitting of their chosen filtrations is asserted or needed.

Since the class sets are disjoint, the filtration argument proves

\[
 \operatorname{Ext}^j_G(A,B)
   =\operatorname{Ext}^j_G(B,A)=0\quad(j\ne2).
 \tag{E816.7}
\]

Here \(\operatorname{Ext}^j_G\) is the invariant Ext group for the specified coherent action. Over \(\mathbf C\), finite-group invariants are exact, so the ordinary vanishing implies (E816.7), and all the ensuing distinguished-triangle long exact sequences hold in the equivariant category itself.

## 3. Exact survival of both middle self-Ext groups

We compute the relevant maps in (E816.3), without any assumption on the class \(e\). Apply \(\operatorname{RHom}_G(A,-)\). For \(j=2,3\), the exact segment is

\[
 \operatorname{Ext}^{j+1}_G(A,B)
  \longrightarrow\operatorname{Ext}^{j}_G(A,E)
  \xrightarrow{p_*}\operatorname{Ext}^{j}_G(A,A)
  \longrightarrow\operatorname{Ext}^{j+2}_G(A,B).
\]

Both exterior terms vanish by (E816.7), so

\[
 \operatorname{Ext}^{j}_G(A,E)
       \simeq\operatorname{Ext}^{j}_G(A,A)
       \qquad(j=2,3).
 \tag{E816.8}
\]

Next apply \(\operatorname{RHom}_G(B[1],-)\). Its exact segment is

\[
 \operatorname{Ext}^{j-2}_G(B,A)
  \longrightarrow\operatorname{Ext}^{j}_G(B,B)
  \xrightarrow{i_*}\operatorname{Ext}^{j}_G(B[1],E)
  \longrightarrow\operatorname{Ext}^{j-1}_G(B,A).
\]

For \(j=1,2\), the exterior groups again vanish. Thus

\[
 i_*:\operatorname{Ext}^{j}_G(B,B)
       \xrightarrow{\sim}\operatorname{Ext}^{j}_G(B[1],E)
       \qquad(j=1,2).
 \tag{E816.9}
\]

Finally apply \(\operatorname{RHom}_G(-,E)\). The complete segment surrounding the middle self-Ext is

\[
 \begin{split}
 \operatorname{Ext}^1_G(B[1],E)
 &\xrightarrow{\partial_1}\operatorname{Ext}^2_G(A,E)
 \longrightarrow\operatorname{Ext}^2_G(E,E)\\
 &\longrightarrow\operatorname{Ext}^2_G(B[1],E)
 \xrightarrow{\partial_2}\operatorname{Ext}^3_G(A,E).
 \end{split}
 \tag{E816.10}
\]

Both displayed connecting maps are zero. More explicitly, (E816.9) writes any class of degree \(j=1,2\) as

\[
 f=i[j]\circ a[1],
 \qquad a:B\longrightarrow B[j].
\]

Up to the irrelevant conventional sign, its connecting class is

\[
 \partial_j(f)=f[1]\circ e
   =i[j+1]\circ a[2]\circ e.
 \tag{E816.11}
\]

The intermediate composite \(a[2]\circ e\) lies in
\(\operatorname{Ext}^{j+2}_G(A,B)\). This is zero for both \(j=1\) and \(j=2\), by (E816.7). The calculation takes place among actual equivariant morphisms and does not replace invariance by a dimension count.

Equations (E816.8)--(E816.11) prove the short exact sequence

\[
 0\longrightarrow\operatorname{Ext}^2_G(A,A)
  \longrightarrow\operatorname{Ext}^2_G(E,E)
  \longrightarrow\operatorname{Ext}^2_G(B,B)
  \longrightarrow0.
 \tag{E816.12}
\]

There is no claim of a canonical splitting. In particular,

\[
 \operatorname{ext}^2_G(E,E)
   =\operatorname{ext}^2_G(A,A)
     +\operatorname{ext}^2_G(B,B).
 \tag{E816.13}
\]

Thus every actual degree-two gluing class leaves these two middle self-Ext dimensions intact. The equality also holds for the zero gluing class. Neither simplicity nor gluability is needed for this equality.

## 4. A balanced four-vector needs at least four pure terms

We include the exterior-algebra proof in full. Put

\[
 W=H^0(X,T_X)\oplus H^1(X,\mathcal O_X),
 \qquad\dim_{\mathbf C}W=8.
\]

Choose a nonzero holomorphic volume form. The resulting Fock identification sends a diagonal Hodge character \(v\) to a four-vector \(\widetilde v\in\bigwedge^4W\), and identifies degree-two cap with

\[
 c_v^2:\bigwedge^2W\longrightarrow\bigwedge^6W,
 \qquad z\longmapsto z\wedge\widetilde v.
 \tag{E816.14}
\]

An exponential \(e^\beta\) becomes a nonzero decomposable four-vector. Indeed multiplication by the exponential is the invertible divisor shear applied to the decomposable Fock representative of the unit class. If \(w\) is a nonzero decomposable four-vector supported on a four-plane \(L\), choose a complementary four-plane \(M\). Only \(\bigwedge^2M\) contributes to wedge multiplication by \(w\), and its map is injective. Hence

\[
 \operatorname{rank}c_w^2=\dim\bigwedge^2M=6.
 \tag{E816.15}
\]

For the nonzero balanced character in (E816.2), the Fock vector has the form

\[
 v=\omega_+\wedge\omega_-,
 \qquad W=W_+\oplus W_-,\qquad\dim W_\pm=4,
 \tag{E816.16}
\]

where each \(\omega_\pm\in\bigwedge^2W_\pm\) is nondegenerate. Each two-plane character \(1-q\theta_\pm^2/2\) gives the sum of nonzero volume bivectors on its translation and tensor two-planes; its square is nonzero because \(q\ne0\). Overall nonzero scalars do not matter.

Define

\[
 K_\pm=\{z\in\bigwedge^2W_\pm:z\wedge\omega_\pm=0\}.
\]

Each \(K_\pm\) has dimension five. On \(\bigwedge^2W_+\) and \(\bigwedge^2W_-\), wedge multiplication by \(v\) has rank one in the distinct bidegrees \((4,2)\) and \((2,4)\). On \(W_+\otimes W_-\) it is the tensor product of the isomorphisms \(x\mapsto x\wedge\omega_\pm\), and has rank sixteen in bidegree \((3,3)\). Consequently

\[
 \operatorname{rank}c_v^2=18,
 \qquad\ker c_v^2=K_+\oplus K_-=:K.
 \tag{E816.17}
\]

Its common annihilator in four-vector degree is exactly one-dimensional:

\[
 \{w\in\bigwedge^4W:z\wedge w=0\text{ for every }z\in K\}
       =\mathbf C v.
 \tag{E816.18}
\]

Here is a direct proof. Decompose \(w\) into bidegrees \((p,4-p)\) for \(W_+,W_-\). The \(K_+\) equations kill the components with \(p=0,1\). For \(p=0\) this is immediate. For \(p=1\), the bivectors annihilating a fixed nonzero vector in a four-space form its three-dimensional wedge subspace; they cannot contain the five-dimensional \(K_+\). Applying linear functionals to the other tensor factor gives the same assertion for a tensor-valued component. The \(K_-\) equations likewise kill \(p=3,4\). For \(p=2\), the wedge pairing on \(\bigwedge^2W_+\) is nondegenerate, so annihilation by its primitive hyperplane forces the first factor to lie in \(\mathbf C\omega_+\). The other condition forces the second factor to lie in \(\mathbf C\omega_-\). This gives precisely (E816.18).

Now suppose that a nonzero balanced four-vector were a sum of \(s\) nonzero pure four-vectors, with arbitrary nonzero scalar coefficients. For \(s\le2\), the rank bound \(18\le6s\) from (E816.15) is impossible. If \(s=3\), absorb coefficients into the pure terms and write

\[
 v=w_1+w_2+w_3.
\]

Let \(S_i=\operatorname{im}c_{w_i}^2\), each of dimension six. Since

\[
 \operatorname{im}c_v^2\subset S_1+S_2+S_3,
\]

and the left side has dimension eighteen, the sum on the right has dimension eighteen and is direct. Therefore

\[
 c_v^2(z)=0
 \quad\Longleftrightarrow\quad
 c_{w_1}^2(z)=c_{w_2}^2(z)=c_{w_3}^2(z)=0.
 \tag{E816.19}
\]

Each \(w_i\) is thus annihilated by \(K=\ker c_v^2\). Equation (E816.18) forces each \(w_i\) to be proportional to \(v\), contradicting their cap ranks six and eighteen. This direct-sum image argument establishes the kernel implication explicitly; no unstated image/kernel duality is being used. We have proved

\[
 \boxed{\text{every nonzero balanced character needs at least four pure exponential terms.}}
 \tag{E816.20}
\]

The conclusion allows signed, rational, real, or complex nonzero coefficients. It is a statement about the actual number of pure terms in a presentation, not an independence assumption on those terms. A common divisor shear is invertible, preserves decomposability and all the displayed cap ranks, and therefore preserves the conclusion.

## 5. Invariant trace dimensions and the contradiction

For any nonzero actual equivariant class block \(A_\beta\), additivity through its filtration gives

\[
 \operatorname{ch}(A_\beta)=r_\beta e^\beta,
 \qquad r_\beta=\operatorname{rk}A_\beta>0.
\]

Hochschild evaluation is natural for the translation/tensor action. That action is trivial on Hochschild cohomology: translations and degree-zero tensor classes act trivially. Evaluation therefore takes values in \(\operatorname{Ext}^2_G(A_\beta,A_\beta)\). Its composition with the full trace is cap product with \(r_\beta e^\beta\). Equation (E816.15) implies

\[
 \operatorname{ext}^2_G(A_\beta,A_\beta)\ge6.
 \tag{E816.21}
\]

This does not require trace injectivity of the block. It is a rank lower bound from the actual invariant evaluation. The same applies to every \(B_\gamma\). Because (E816.6) consists of actual coherent equivariant summands, its diagonal self-Ext groups are direct summands of the self-Ext of \(A\) and \(B\). Put \(s=|\mathcal A|+|\mathcal B|\). Equations (E816.13) and (E816.21) give

\[
 \operatorname{ext}^2_G(E,E)\ge6s.
 \tag{E816.22}
\]

On the other hand,

\[
 \operatorname{ch}(E)
   =\sum_{\beta\in\mathcal A}r_\beta e^\beta
       -\sum_{\gamma\in\mathcal B}t_\gamma e^\gamma,
 \qquad r_\beta,t_\gamma>0.
 \tag{E816.23}
\]

The disjoint-class hypothesis ensures that these are \(s\) actual pure terms with nonzero signed coefficients. Under the common shear \(e^D\), they are still pure terms. If (E816.2) holds, (E816.20) therefore gives \(s\ge4\), and so

\[
 \operatorname{ext}^2_G(E,E)\ge24.
 \tag{E816.24}
\]

Finally suppose the invariant full degree-two trace of \(E\) were injective. The CY4 trace/evaluation adjunction in supplied S-21 makes the invariant Hochschild evaluation surjective: the two maps are adjoint for the perfect Serre pairing on invariant degree-two Ext and the perfect Hochschild pairing. The Serre pairing remains perfect on invariants because the finite translation/tensor action preserves it and averaging is exact. The identity-sector normalization may multiply the trace/cap identity by a nonzero scalar depending on \(|G|\); it changes no rank.

Thus injectivity implies that the trace image is exactly the image of cap product with \(\operatorname{ch}(E)\), and gives

\[
 \operatorname{ext}^2_G(E,E)
    =\operatorname{rank}c^2_{\operatorname{ch}(E)}=18,
 \tag{E816.25}
\]

by (E816.17) and invariance under the divisor shear. This contradicts (E816.24), proving the theorem. There was no equivariant simplicity assumption and no Euler-divisibility argument in the proof.

## 6. What has and has not been removed

SF-E815 excludes equivariantly simple repairs with nonnegative aggregate weights in the stated primitive class models. The present result excludes a different proposed escape: negative aggregate weights implemented by putting disjoint class sets in two adjacent cohomological degrees and joining them by arbitrary degree-two extensions. It excludes these objects even when they are nonsimple and their finite action has projective multiplicity spaces.

If the same normalized class occurs in both \(A\) and \(B\), the cross groups in degrees one, three or four need not vanish without further information. The connecting maps in (E816.10) could then be nonzero. Corollary SF-E816a below shows that ordinary gluability supplies the needed further information and removes the disjoint-class assumption for two cohomology sheaves. Objects with three or more nonzero cohomology sheaves have additional Postnikov data; corollary SF-E816b treats them when the normalized class sets are globally disjoint. General overlapping-class complexes with more cohomology sheaves, singular stable factors, twisted categories, and classes outside the common primitive real-multiplication space remain outside these results. None is inferred to exist or to be semiregular.

The proof is an exact long-exact-sequence and exterior-algebra argument. No new computer calculation is needed or claimed for the universal theorem. The already recorded exact exterior calculations for SF-E801 independently corroborate the balanced rank eighteen and its one-dimensional common annihilator; the written derivations above are the proofs used here.

## 7. SF-E816a: ordinary gluability removes normalized-class disjointness for two sheaves

Retain the setting of §1, including the primitive-difference condition for unequal normalized classes, but drop condition 2. Instead assume that \(E\) is **ordinary gluable**:

\[
 \operatorname{Ext}^j_X(E,E)=0\qquad(j<0).
 \tag{E816.26}
\]

Then the same impossibility theorem holds, even when \(A\) and \(B\) have overlapping normalized classes and cancelling virtual terms. It still does not require equivariant simplicity. The ordinary condition (E816.26), rather than only its invariant counterpart, is the hypothesis used in this corollary.

### 7.1. Gluability detects the extreme cohomology map

There is a canonical isomorphism

\[
 \operatorname{Hom}_{D^b(X)}(E,E[-1])
       \simeq\operatorname{Hom}_X(A,B).
 \tag{E816.27}
\]

Indeed \(E\) lies in \(D^{\le0}\), whereas \(E[-1]\) lies in \(D^{\ge0}\). A map between these two objects factors uniquely through their degree-zero cohomology sheaves. Their degree-zero cohomology sheaves are \(A\) and \(B\), respectively. This proves (E816.27) directly from the standard cohomological structure. Ordinary gluability therefore gives

\[
 \operatorname{Hom}_X(A,B)=0.
 \tag{E816.28}
\]

This conclusion is independent of the Postnikov invariant \(e\).

### 7.2. Stable factors of the same normalized class

Let \(Q,R\) be stable projectively flat vector bundles of the same normalized class \(\beta\). Choose the Hermitian--Einstein metrics used in (E816.4). Their scalar curvature forms are the harmonic representative of the same class \(\beta\), so the induced connection on \(Q^\vee\otimes R\) is unitary flat. Since \(\pi_1(X)\) is abelian, its unitary representation splits into one-dimensional characters. Thus \(Q^\vee\otimes R\) is an actual direct sum of unitary flat line bundles.

A nontrivial unitary flat line bundle on a complex torus has no cohomology. For completeness, equip the torus with its flat Kähler metric. The Laplacian on a flat line-valued \((0,j)\)-form is the connection Laplacian, since both the metric curvature and the line curvature vanish. A harmonic form is therefore parallel by integration of the squared covariant derivative. The tangent bundle is parallel trivial, so a nontrivial line character admits no such forms in any degree. The trivial character contributes precisely \(H^j(X,\mathcal O_X)\). Consequently the parallel-invariant subspace gives a natural graded isomorphism

\[
 \operatorname{Ext}^*_X(Q,R)
     \simeq\operatorname{Hom}_X(Q,R)\otimes
                    H^*(X,\mathcal O_X).
 \tag{E816.29}
\]

Stable vector bundles of the same slope have no nonzero Hom unless they are isomorphic; any nonzero map is an isomorphism by the slope inequalities for its image. Thus two nonisomorphic stable factors of the same normalized class have

\[
 \operatorname{Ext}^j_X(Q,R)=0\quad\text{for every }j.
 \tag{E816.30}
\]

No assertion of individual equivariant structures is made here. This is an ordinary vanishing for the actual stable bundles.

### 7.3. Separate stable isomorphism types and exclude a shared type

Within each fixed normalized-class block of \(A\) or \(B\), use (E816.30) and the same filtration induction as in §2. The block has an actual canonical decomposition into pieces filtered by one stable isomorphism type each. Ext degree one gives existence of this decomposition; Hom vanishing between distinct types gives uniqueness. Denote the pieces of type \(Q\) by \(A_Q\) and \(B_Q\), when present.

If both pieces were nonzero, a last filtration quotient would give a surjection \(A_Q\twoheadrightarrow Q\), and a first filtration subobject would give an injection \(Q\hookrightarrow B_Q\). Their composite is a nonzero morphism \(A_Q\to B_Q\), and hence a nonzero morphism \(A\to B\), contradicting (E816.28). Thus no stable isomorphism type occurs in both sheaves.

For factors of equal normalized class across \(A\) and \(B\), (E816.30) now gives complete Ext vanishing. For factors of unequal normalized class, (E816.5) gives concentration in degree two. Two filtration inductions therefore give

\[
 \operatorname{Ext}^j_X(A,B)
       =\operatorname{Ext}^j_X(B,A)=0\quad(j\ne2),
 \tag{E816.31}
\]

and taking invariants gives (E816.7). The actual equivariant triangle proof of §3 applies unchanged. Notice that the stable-type decompositions were used only to prove ordinary vanishing. They need not be preserved one by one by \(G\); only the normalized-class decompositions used in the dimension bound need to be equivariant, and those are canonical as before.

### 7.4. The character count still gives the contradiction

Let \(s\) now be the number of nonzero normalized-class blocks in \(A\), plus the number in \(B\), counting a class twice if it occurs in both. Their characters form the actual signed pure-term presentation (E816.23), with nonzero positive ranks before the signs, even if some terms repeat or partially cancel. Multiplication by \(e^D\) preserves purity. The at-least-four-term result of §4 applies to this presentation without any independence or distinctness requirement, so a balanced nonzero character forces \(s\ge4\).

Each of these \(s\) actual equivariant blocks contributes at least six to the sum in (E816.13), by the invariant evaluation argument in §5. Thus \(\operatorname{ext}^2_G(E,E)\ge24\). Weak invariant semiregularity would again give exactly eighteen. This proves SF-E816a, with arbitrary normalized overlaps and cancellations in the two-cohomology model.

## 8. SF-E816b: arbitrary amplitude with globally disjoint class sets

There is a separate extension with no gluability assumption. Let \(E\) be any bounded perfect equivariant complex whose cohomology sheaves are vector bundles filtered by stable projectively flat factors. Assume the primitive-difference condition from §1 for all unequal normalized classes occurring anywhere. Assume that the normalized class sets of any two distinct nonzero cohomology sheaves are disjoint.

Then

\[
 \operatorname{ext}^2_G(E,E)
      =\sum_j\operatorname{ext}^2_G(\mathcal H^j(E),\mathcal H^j(E)).
 \tag{E816.32}
\]

If its character is nonzero balanced after a common divisor shear, this equality rules out weak invariant semiregularity, regardless of simplicity or the number of cohomology sheaves. We prove (E816.32) using actual Postnikov triangles, rather than assume degeneration of a self-Ext spectral sequence.

Shift the top nonzero cohomological degree to zero, put

\[
 A=\mathcal H^0(E),\qquad F=\tau_{\le-1}E,
\]

and use the canonical equivariant triangle

\[
 F\xrightarrow{i}E\xrightarrow{p}A\xrightarrow{e}F[1].
 \tag{E816.33}
\]

Every successive Postnikov piece of \(F\) is
\(\mathcal H^{-k}(E)[k]\) for some \(k\ge1\). By the disjointness hypothesis and §2, cross Ext between \(A\) and \(\mathcal H^{-k}(E)\), in either direction, is concentrated in degree two. It follows that

\[
 \begin{split}
 \operatorname{Ext}^j_G(A,\mathcal H^{-k}(E)[k])
       &=\operatorname{Ext}^{j+k}_G(A,\mathcal H^{-k}(E))=0
              &&(j\ge2),\\
 \operatorname{Ext}^j_G(\mathcal H^{-k}(E)[k],A)
       &=\operatorname{Ext}^{j-k}_G(\mathcal H^{-k}(E),A)=0
              &&(j\le2).
 \end{split}
 \tag{E816.34}
\]

For each fixed \(j\) in the indicated range, vanishing is preserved by the distinguished-triangle long exact sequence. Induction through the finite Postnikov tower therefore gives

\[
 \operatorname{Ext}^j_G(A,F)=0\quad(j\ge2),
 \qquad
 \operatorname{Ext}^j_G(F,A)=0\quad(j\le2).
 \tag{E816.35}
\]

Apply \(\operatorname{RHom}_G(A,-)\) to (E816.33). The exterior terms vanish by (E816.35), giving

\[
 \operatorname{Ext}^j_G(A,E)\simeq\operatorname{Ext}^j_G(A,A)
            \qquad(j=2,3).
 \tag{E816.36}
\]

Apply \(\operatorname{RHom}_G(F,-)\). The two adjacent groups with target \(A\) vanish, giving

\[
 i_*:\operatorname{Ext}^j_G(F,F)
         \xrightarrow{\sim}\operatorname{Ext}^j_G(F,E)
            \qquad(j=1,2).
 \tag{E816.37}
\]

Finally \(\operatorname{RHom}_G(-,E)\) gives the exact segment

\[
 \operatorname{Ext}^1_G(F,E)\xrightarrow{\partial_1}
 \operatorname{Ext}^2_G(A,E)\longrightarrow
 \operatorname{Ext}^2_G(E,E)\longrightarrow
 \operatorname{Ext}^2_G(F,E)\xrightarrow{\partial_2}
 \operatorname{Ext}^3_G(A,E).
 \tag{E816.38}
\]

Represent any degree-\(j\) class, for \(j=1,2\), by \(f=i[j]\circ a\), with \(a:F\to F[j]\), using (E816.37). Its connecting image is, up to sign,

\[
 \partial_j(f)=f[1]\circ e
   =i[j+1]\circ a[1]\circ e.
 \tag{E816.39}
\]

The middle composite belongs to \(\operatorname{Ext}^{j+1}_G(A,F)=0\), by (E816.35). Hence both connecting maps vanish, and (E816.36)--(E816.38) give

\[
 0\longrightarrow\operatorname{Ext}^2_G(A,A)
    \longrightarrow\operatorname{Ext}^2_G(E,E)
    \longrightarrow\operatorname{Ext}^2_G(F,F)
    \longrightarrow0.
 \tag{E816.40}
\]

Induction on the number of nonzero cohomology sheaves proves (E816.32). A shift of a sheaf has the same self-Ext groups, which supplies the base case.

Each cohomology sheaf has the actual canonical equivariant normalized-class blocks of §2. Let \(s\) be the total number of such nonzero blocks. Their signed characters, with signs determined by their cohomological degrees, present \(\operatorname{ch}(E)\) as \(s\) nonzero pure terms. Global class disjointness ensures they occur in only one cohomological degree, but no additional independence claim is needed. If the full character is balanced, §4 gives \(s\ge4\). Equations (E816.21) and (E816.32) then give \(\operatorname{ext}^2_G(E,E)\ge6s\ge24\), contradicting (E816.25).

This proves SF-E816b for arbitrary bounded amplitude and arbitrary actual higher Postnikov invariants. The general case in which normalized classes overlap between several different cohomological degrees is not settled by this argument.
