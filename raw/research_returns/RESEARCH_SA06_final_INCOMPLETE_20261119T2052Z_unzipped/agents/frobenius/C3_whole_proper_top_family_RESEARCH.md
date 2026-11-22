# Whole proper top-family lifting by finite-support correction

**Research fragment; unregistered; pending independent audit.** Written 19 November 2026 by `/root/frobenius_continuation`. This strengthens the prescribed-family conclusion of the audited C.3bn proof in its stated resolved scope. It is not claimed as a reduction of the remaining component Albanese-kernel gate.

## 1. Statement and exact scope

Retain every hypothesis of `../real_weil/C3_all_dimension_endpoint.tex`: (k) is algebraically closed of characteristic (p>0), (R) is an excellent henselian algebraizable local coefficient-(k) algebra with residue field (k), (Z\to\operatorname{Spec}R) is projective, regular of pure dimension (d+1), and an isomorphism away from the closed point, (d\ge1). An effective Cartier divisor (D\subset Z) has the whole reduced closed fibre (E) as support, and (\mathcal O_D(-D)) is ample. Let (P/k) be a fixed smooth connected projective curve and put (T=D\times_kP).

The proposed strengthening is

\[
F_\gamma^dK_0(T)_{\mathbf Q}\ \subseteq\
\operatorname{im}\bigl(K_0(Z\times_kP)_{\mathbf Q}\longrightarrow K_0(T)_{\mathbf Q}\bigr).
\tag{WP.1}
\]

The equality is with the prescribed class on the **entire fixed product**. All groups are perfect (K)-groups. There is no assertion that a prescribed bundle, as an object, extends. There is no affine-parameter assertion and no replacement of (R\otimes_kK) by a local or henselian ring after a field extension.

The proof uses the exact perfect determinantal identities and the actual fixed-product line-bundle lifting of AE.2–AE.9. Its additional input is the exact lifting of the finite perfect corrections discarded in the endpoint argument.

## 2. The finite-scheme lifting lemma

Call a finite subscheme (F\subset T) admissible if it is cut out by a regular sequence of length (d+1), its support lies in the smooth top-dimensional strata of (E\times P), and the differentials of a local defining sequence are independent on those strata. Its possible nilpotent structure inherited from (D) is retained.

**Lemma WP.2.** For an admissible (F), the perfect class ([\mathcal O_F]\in K_0(T)) is the restriction of an actual class in (K_0(Z\times P)), integrally.

**Proof.** Choose (d) sufficiently high relatively ample line bundles on (Z\times P), also ample in the (P) direction. On (T), choose their sections in (I_F) so that the induced ((d+1)\times d) conormal matrix has rank (d) on (F). The rank-defective locus has codimension two; because (F) is finite, a general choice avoids it. Surjectivity onto twisted conormal sections follows from Serre vanishing, and Nakayama upgrades the condition on (F_{\mathrm{red}}) to a locally split injection on (F).

Away from (F), impose transversality to a finite smooth stratification of (E\times P), for each prefix of the flag. These are precisely the finite first-jet incidence conditions used in AE.5–AE.7; the same proof works with total codimension (d). Sections lift to the fixed (Z\times P) because sufficiently high twists have zero first cohomology after tensoring by (\mathcal O(-D\times P)).

Let (j:W\hookrightarrow Z\times P) be the resulting intersection and let (H=W\cap T). Independent ambient differentials show that (W) is regular of pure dimension two along its whole closed fibre. Its nonregular locus is closed by excellence; its proper image in the local scheme (\operatorname{Spec}R), if nonempty, would contain the closed point. Thus it is empty. The same argument excludes components of unintended dimension. Consequently (j) is a regular immersion of codimension (d). The flag has the expected intersection dimension one with the closed fibre, so (H\subset W) is an effective Cartier divisor with full closed-fibre support.

The conormal condition says that the flag equations form the first (d) members of a regular-sequence generating set of (I_F). Its last member cuts out (F) as an effective Cartier divisor on the possibly nonreduced Cohen–Macaulay curve (H). Put (Q_0=\mathcal O_H(-F)) and (J=\mathcal O_W(-H)). For every (n\ge1),

\[
H^2\bigl(H,J^n/J^{n+1}\bigr)=0,
\tag{WP.2a}
\]

because the noetherian space (H) has dimension one (The Stacks Project Authors, 2026, Proposition 20.20.7, Tag 02UZ). The square-zero unit sequence therefore lifts (Q_0), without taking a power, through all the thickenings of (H) (Tag 0C6R).

The ideals (J) and (\mathfrak m\mathcal O_W) have the same radical and hence cofinal powers. The formal bundle and its inverse algebraize over (\widehat R) by proper Grothendieck existence. Popescu and descent to one smooth (R)-algebra, followed by henselian smooth lifting of its specified (R/\mathfrak m^M)-point for (\mathfrak m^M\mathcal O_W\subset J), give an actual line bundle (Q\) on the fixed (W) with (Q|_H\simeq Q_0). This is exactly the finite-jet argument in AE.9; no étale replacement of (Z\times P) is retained.

Since (H\) is Cartier on (W), the square obtained by pulling (j) back along (T\hookrightarrow Z\times P) is Tor-independent. If (i:H\hookrightarrow T), perfect pushforward and derived base change yield

\[
\bigl(j_*(1-[Q])\bigr)|_T
 = i_*(1-[\mathcal O_H(-F)])
 = [\mathcal O_F]\quad\text{in }K_0(T).
\tag{WP.2b}
\]

The final equality is the Cartier exact sequence. Every complex in it is perfect, so no passage through coherent (G_0), no Cartan injectivity, and no gamma-pushforward formula is used. This proves the lemma.

## 3. The top gamma tail is generated by admissible finite schemes

Set (n=\dim T=d+1). Apply the construction of AE.2–AE.6 with total gamma degree (n), instead of (d). Modulo (F_\gamma^{n+1}), any element of (F_\gamma^nK_0(T)\) is a sum of products of gamma operations of total degree (n), on sufficiently generated bundles. The exact Eagon–Northcott identity AE.3 replaces each factor by its perfect maximal-minor class modulo the next gamma term.

The general simultaneous degeneracy locus now has dimension zero. It misses every lower-dimensional stratum, and the next rank-drop incidence for a factor of degree (i_a\) has codimension

\[
2(i_a+1)+\sum_{b\ne a}i_b=n+i_a+2>n.
\]

Near the intersection all matrices reduce to a block identity and their defining functions; the (n) combined differentials are independent on the smooth top stratum. Cohen–Macaulayness gives a regular sequence. Thus each resulting product is exactly ([\mathcal O_F]) for an admissible finite scheme, by the same perfect tensor-resolution argument as AE.6.

The dimension theorem for the vector-bundle gamma filtration on a projective (n)-dimensional scheme gives (F_\gamma^{n+1}K_0(T)_{\mathbf Q}=0) (Weibel, 2013, Chapter II, Remark 8.8.5). Consequently

\[
F_\gamma^{d+1}K_0(T)_{\mathbf Q}
\text{ is spanned by admissible }[\mathcal O_F].
\tag{WP.3}
\]

Lemma WP.2 therefore lifts the whole top tail. The proof only needs the rational dimension theorem; no stronger integral vanishing is asserted here.

## 4. Exact finite-support corrections on the curve representatives

Let (C\subset T) be one of the perfect curves constructed in AE.5–AE.6. It is a projective Cohen–Macaulay curve, possibly nonreduced, regularly immersed in (T) with codimension (d). Its intersection with every lower-dimensional stratum of (E\times P) is finite. On the complement of those finitely many points, (C_{\mathrm{red}}) is smooth and its defining differentials in the top stratum are independent.

For every line bundle (M\) on (C), there are admissible finite Cartier divisors (F_+,F_-\subset C) such that

\[
[M]-1=[\mathcal O_{F_+}]-[\mathcal O_{F_-}]
\quad\text{in perfect }K_0(C).
\tag{WP.4}
\]

Indeed choose an ample bundle (A) and (N\) so large that (M\otimes A^N) and (A^N) have generated first jets. General sections avoid all associated points and the finite bad set just described, and have simple zeros on the smooth reduction there. Their zero schemes (F_+) and (F_-) are finite effective Cartier divisors with support in that good locus. The exact sequences give

\[
[M\otimes A^N]-[A^N]
 =[\mathcal O_{F_+}(F_+)]-[\mathcal O_{F_-}(F_-)].
\]

Every line bundle on a finite (k)-scheme is trivial, because its ring is Artinian semilocal. Thus multiplication by (A^{-N}), and the displayed twists, leave both finite classes unchanged. This proves WP.4. The composite regular immersions (F_\pm\hookrightarrow C\hookrightarrow T) are cut out by the (d) original functions and the transverse section on (C); they satisfy the admissibility conditions of Lemma WP.2.

For completeness, the semilocal assertion follows directly by the Chinese remainder theorem: choose one basis in the rank-one residue vector space at each maximal ideal, lift them simultaneously to one element, and apply Nakayama at every maximal ideal. The resulting map from the ring to the invertible module is an isomorphism. This is the proof indicated in Stacks Lemma 10.78.7, Tag 02M9; that source explicitly labels its proof as omitted and supplies these hints.

Now perform the AE flag for (C): (W\) is a regular threefold, (H=W\cap T) is Cartier on (W), and (C\subset H) is Cartier. The AE.8–AE.9 argument produces a finite (a=p^e) and a line bundle (Q\) on the actual fixed (W) such that

\[
Q|_H\simeq\mathcal O_H(-aC).
\]

With (j:W\hookrightarrow Z\times P), put (b_C=j_*(1-[Q])). The whole square with (T), and not only its endpoint squares, is Tor-independent: the flag is regular and the equation of (D) is a nonzerodivisor on (W). The successive Cartier sequences therefore give the exact equality

\[
 b_C|_T
  =\sum_{r=0}^{a-1}
    [\mathcal O_C\otimes\mathcal O_H(-rC)|_C].
\tag{WP.5}
\]

Subtract (a[\mathcal O_C]). Each summand in the difference is the perfect pushforward from (C) of a line-bundle difference. Formula WP.4 expresses it as a finite integral combination of admissible finite classes in (K_0(T)); Lemma WP.2 lifts each of them exactly. If (c_C\) is the resulting integral correction on (Z\times P), then

\[
 (b_C-c_C)|_T=a[\mathcal O_C].
\tag{WP.6}
\]

Division by (a) gives an actual rational lift of the entire prescribed curve class. This is the only division introduced by this correction step.

## 5. Completion of the proposed theorem

The exact perfect determinantal proof of AE.2–AE.6 writes any
(\beta\in F_\gamma^dK_0(T)_{\mathbf Q}), modulo (F_\gamma^{d+1}), as a finite rational sum of these curve classes. Formula WP.6 lifts each curve. Formula WP.3 and Lemma WP.2 lift the remaining top tail. Their finite sum gives (b\in K_0(Z\times P)_{\mathbf Q}) with (b|_T=\beta), proving WP.1.

Nilpotent invariance in characteristic (p), as used in AE.13, identifies (K_0(T)_{\mathbf Q}) with (K_0(E\times P)_{\mathbf Q}) as rational lambda rings. Thus the same whole-family conclusion holds for (F_\gamma^dK_0(E\times P)_{\mathbf Q}).

## 6. Consequence in exceptional dimensions one and two

When (d=2), the proposed proof also gives

\[
K_0(Z\times P)_{\mathbf Q}\longrightarrow K_0(E\times P)_{\mathbf Q}
\quad\text{surjective}.
\tag{WP.7}
\]

First, ranks lift from (E) by the audited point isomorphism FF.4 and pull back to the fixed product. After subtracting such a lift, the prescribed class has rank zero on every connected component. Its determinant is a line bundle on (T). A finite (p)-power of **any** line bundle on (T) lifts to (Z\times P) by the AE.8–AE.9 argument with (W=Z\times P) and (H=T): the ample conormal is relative to (T\to P), so relative Serre and the coherent cohomological dimension one of (P) give the required eventual (H^2) vanishing. Taking a rational logarithm in the nilpotent augmentation ideal, or equivalently the finite binomial polynomial for an (a\)-th root of a line-bundle class, gives a rational (K_0) lift of ([M]-1) from a lift of (M^a). One may also use the rank-and-determinant description of (K_0/F_\gamma^2): a rational multiple of the lifted line-bundle difference has the required determinant modulo (F_\gamma^2), and WP.1 lifts the remainder. No line-bundle root as an object is claimed.

The standard rank-and-determinant description leaves precisely (F_\gamma^2), which WP.1 lifts. The same conclusion for (d=1) follows directly by lifting ranks and applying WP.1 to (F_\gamma^1).

Combining WP.7 with the already proved fixed-product exact obstruction FF.1 gives, in these same resolved hypotheses and for a proper smooth parameter curve,

\[
K_{-1}(\operatorname{Spec}R\times_kP)_{\mathbf Q}=0
\qquad(d\le2).
\tag{WP.8}
\]

This is a consequence of the geometric lifting proof, **not** an application of Drinfeld to a nonlocal product. It does not apply to the previously retained affine two-dimensional parameter example. It neither supplies an actual family for independent component cycles nor proves that arbitrary affine exceptional families compactify.

## 7. Fixed-base limitation and audit hooks

The argument repeatedly uses that (Z\times_kP) and every flag (W) are proper over the original local ring (R). After replacing (k) by (k(u)), the ring (R\otimes_k k(u)) is generally not local or henselian. The closed-fibre regularity argument and the finite-jet specialization to (R) cannot then be repeated. Localizing or henselizing at a point changes the fixed product. Consequently this note does not turn the HK construction with a symbolic unit (u) into a lift on the original constant regular product, and supplies no valuation descent of the remaining component classes.

The points requiring independent checking are: (i) the finite-support flag has a regular **surface** everywhere on the actual product; (ii) the divisors representing a line-bundle difference can avoid every bad point on (C\) while retaining the nonreduced structure; (iii) the whole (T)-square in WP.5 is Tor-independent; (iv) the perfect finite-tail identities survive without passing to (G_0); and (v) no improper parameter or nonlocal scalar extension enters the Picard algebraization step.

## 8. Sources and source-scope ledger

The complete AE proof was freshly reread on 19 November 2026 at approximately 19:34 UTC. Its independent receipt and source audit are reused explicitly: `C3_all_dimension_endpoint_independent_REVIEW.md` and `../real_weil/C3_all_dimension_endpoint_SOURCE_AUDIT.md`. No second fresh reading of all their cited external proofs is claimed here.

- Bruns, W., & Vetter, U. (1988). *Determinantal rings*. Springer. Construction §2.C, Theorems 2.1 and 2.16. The exact perfect identities, the grade bound, and the first-jet argument are the already audited AE inputs.
- The Stacks Project Authors. (2026). *Grothendieck vanishing*, Proposition 20.20.7, [Tag 02UZ](https://stacks.math.columbia.edu/tag/02UZ). Entire displayed proof freshly read in this continuation, 19 November 2026. Used for (H^2) on the one-dimensional (H) in WP.2.
- The Stacks Project Authors. (2026). *Finite projective modules*, Lemma 10.78.7, [Tag 02M9](https://stacks.math.columbia.edu/tag/02M9). Entire statement and the source's proof hints freshly read. The elementary rank-one proof is supplied above; no nonexistent complete printed proof is attributed to this page.
- The Stacks Project Authors. (2026). *Ample invertible sheaves and cohomology*, Lemma 30.17.1, [Tag 01XO](https://stacks.math.columbia.edu/tag/01XO); *Picard groups of thickenings*, Lemma 37.4.1, [Tag 0C6R](https://stacks.math.columbia.edu/tag/0C6R); *Grothendieck's existence theorem, I*, Lemma 30.24.3, [Tag 0885](https://stacks.math.columbia.edu/tag/0885); *The main theorem: Popescu*, Theorem 16.12.1, [Tag 07GC](https://stacks.math.columbia.edu/tag/07GC); *Lifting and henselian pairs*, Lemma 15.13.3, [Tag 0H74](https://stacks.math.columbia.edu/tag/0H74). Complete prior source audits are reused through AE.8–AE.9 and the exact bibliography `C3_smooth_exceptional_references.bib`.
- Weibel, C. A. (2013). *The K-book: An introduction to algebraic K-theory*. American Mathematical Society. Chapter II, §8, especially Remark 8.8.5. The singular projective gamma-filtration bound and rank/determinant description are reused from the audited endpoint proof; no global Gersten injectivity or Adams semisimplicity is invoked.
- The exact rational nilpotence and fixed-product blow-up statements are the already audited GH/KST/TT inputs in `C3_fixed_family_negative_K.tex`, FF.1–FF.4. The current proof does not assert an inverse-limit exactness theorem beyond those earlier statements.
