# Rank and determinant on a constant proper curve, and whole K1 family lifting

**Proved auxiliary under the stated hypotheses; unregistered and pending complete peer review.** Written after checkpoint23 thaw on 19 November 2026 by `/root/frobenius_continuation`. No main-gate movement is claimed. The field extension needed for a symbolic valuation remains an actual-base-change problem.

## NK.1. The rank-and-determinant statement

Let (k) be an algebraically closed field, (R) a noetherian local coefficient-(k) algebra with residue field (k), and (P/k) a smooth connected projective curve. Put (B=\operatorname{Spec}R\times_kP). Then rank and determinant induce an integral isomorphism of abelian groups

\[
K_0(B)\xrightarrow{\ (\mathrm{rk},\det)\ }
                       \mathbf Z\oplus\operatorname{Pic}(B).
\tag{NK.1}
\]

The augmentation ideal has square zero and

\[
F_\gamma^2K_0(B)=0,\qquad
 (\psi^q-1)(\psi^q-q)=0\text{ on }K_0(B)
                    \quad(q\ge1).
\tag{NK.2}
\]

No henselian, normal, regular, or characteristic assumption is needed for NK.1–NK.2. The algebraically closed coefficient field is used for a general section on the closed curve; the argument more generally works over an infinite field with a geometrically integral closed curve and the same section argument.

### Proof: every bundle has a line-bundle filtration

Fix an ample line bundle (H) on (P), and denote its pullback by the same symbol. For a vector bundle (V) of rank (r\ge2), relative Serre generation gives finitely many global sections generating (V\otimes H^n) on (B), for (n\) sufficiently large. Their restrictions generate on the closed fibre (P).

There is a (k)-linear combination of these restricted sections which is nowhere zero on (P). In the finite-dimensional coefficient space, vanishing at a fixed point imposes (r) independent linear conditions. The corresponding incidence over the one-dimensional (P) therefore has dimension at most the coefficient-space dimension plus (1-r), strictly smaller than the coefficient-space dimension. Properness of (P) makes its image closed; a general coefficient vector avoids it. Lift the coefficients using (k\subset R).

The zero scheme of the resulting actual section on (B) is closed and proper over (\operatorname{Spec}R). If nonempty, its proper image is a nonempty closed subset of a local scheme and therefore contains the closed point, contrary to the construction on (P). Thus the section is nowhere zero on all of (B). It gives a line subbundle (H^{-n}\hookrightarrow V) with locally free quotient of rank (r-1). Induction gives a filtration with line-bundle quotients. Since (B) has an ample line bundle relative to an affine base, its perfect (K_0) is its vector-bundle (K_0). Consequently (K_0(B)) is generated additively by line-bundle classes.

### Proof: line differences have finite semilocal support

Let (M) be a line bundle on (B). For (n\) sufficiently large, both (M\otimes H^n) and (H^n) have generating global sections. Choose sections whose restrictions to the integral closed curve are nonzero. Their closed-fibre zero schemes are finite effective Cartier divisors, possibly empty.

Let (D_+) and (D_-) be their actual zero schemes on (B). These schemes are locally principal by construction. At every point of the closed fibre where a zero occurs, the fibrewise Cartier criterion applies to the flat finite-presentation map (B\to\operatorname{Spec}R): Stacks Lemma31.19.9(3), Tag062Y, gives an open neighbourhood on which that zero scheme is an effective Cartier divisor flat over (R). Where the section is a unit the same assertion is immediate. These neighbourhoods cover the entire closed fibre. Their union must equal (B), because its closed complement is proper over the local base and misses that fibre. Thus (D_\pm) are relative effective Cartier divisors everywhere.

Each (D_\pm\to\operatorname{Spec}R) is proper with finite closed fibre. Stacks Lemma37.44.2, Tag02UP, makes it finite over an open neighbourhood of the closed point, and every such open in a local scheme is the whole scheme. Hence (D_\pm) is finite over (R). A finite algebra over a local ring is semilocal. Every line bundle on it is trivial by the Chinese-remainder/Nakayama proof already supplied for WP.4 (Stacks02M9).

The two Cartier exact sequences, followed by multiplication by (H^{-n}), now give the exact identity

\[
[M]-1=[\mathcal O_{D_+}]-[\mathcal O_{D_-}]
                         \quad\text{in perfect }K_0(B).
\tag{NK.3}
\]

For any other line bundle (N) on (B), its restriction to either finite semilocal divisor is trivial. The projection formula for the perfect Cartier pushforward consequently gives

\[
([M]-1)([N]-1)=0\quad\text{in }K_0(B).
\tag{NK.4}
\]

No assertion that a general coherent sheaf on (B) is perfect is used: the finite divisor sheaves are perfect because their immersions are Cartier.

### Proof: exact rank, determinant and operations

Because line classes generate, the rank-zero subgroup (I) is generated by ([M]-1). Formula NK.4 says (I^2=0). Thus

\[
[MN]-1=([M]-1)+([N]-1),
\]

and (M\mapsto[M]-1) is a group homomorphism (\operatorname{Pic}(B)\to I). It is inverse to determinant on the generating line differences, proving NK.1. In a special lambda ring generated by line elements, gamma operations on rank-zero expressions are products of their line differences: (\gamma_z([M]-1)=1+([M]-1)z). Every term of gamma degree at least two therefore vanishes by NK.4. Finally

\[
\psi^q([M])=[M]^q=1+q([M]-1)
\]

proves NK.2 directly. This is a calculation of the operator; no semisimplicity assumption is needed.

## NK.2. Injectivity after a normal modification

Now assume (R) is a normal domain and (g:Z\to\operatorname{Spec}R) is a proper birational morphism of integral noetherian schemes. Assume (Z) is regular when invoking the (K)-theory conclusion below. Put (g_P:Z\times P\to B). Then

\[
g_{P*}\mathcal O_{Z\times P}=\mathcal O_B,
\qquad
\operatorname{Pic}(B)\hookrightarrow\operatorname{Pic}(Z\times P).
\tag{NK.5}
\]

Here is a direct check of the structure-sheaf assertion. A regular function on (Z) is a rational function in (\operatorname{Frac}R). For every height-one prime of the normal noetherian (R), the local ring is a DVR. Properness extends its generic-point map to (Z); pulling back the function shows that it belongs to that DVR. The intersection characterization of a noetherian normal domain gives that the function lies in (R). The same argument on affine opens gives (g_*\mathcal O_Z=\mathcal O_{\operatorname{Spec}R}). Equivalently, proper coherent finiteness makes this ring a finite (R)-subalgebra of its fraction field, and integral closedness gives the equality.

Products with affine opens of (P) preserve this equality: compute global sections by a finite affine Čech cover of the separated (Z) and use exactness of tensoring over the field (k). These opens give NK.5's first assertion. For an invertible (M) on (B), the elementary projection formula gives

\[
g_{P*}g_P^*M=M\otimes g_{P*}\mathcal O_{Z\times P}=M.
\]

A trivial pullback therefore implies (M\simeq\mathcal O_B), proving Picard injectivity.

It follows that

\[
K_0(B)\longrightarrow K_0(Z\times P)
\quad\text{is injective}.
\tag{NK.6}
\]

Indeed a class mapping to zero has rank zero and trivial determinant after pullback. Picard injectivity and NK.1 make its original class zero. This deduction does not require a rank-and-determinant description of the target.

## NK.3. The actual whole K1-family lift

Retain the characteristic-(p>0) hypotheses of FF.1: (R) is a normal noetherian local coefficient-(k) domain, (g:Z\to\operatorname{Spec}R) is proper with regular integral (Z), and it is an isomorphism away from the closed point. Let (E) be the reduced closed fibre. For every fixed smooth connected proper curve (P/k),

\[
K_1(Z\times_kP)[1/p]\longrightarrow K_1(E\times_kP)[1/p]
                         \quad\text{is surjective}.
\tag{NK.7}
\]

This assertion is dimension-independent and does not require the ample conormal or henselian hypotheses used for C.3bu. It concerns (K_1) classes, not specified automorphisms as objects.

The already proved KST/GH exact sequence underlying FF gives

\[
K_1(Z\times P)[1/p]\oplus K_1(P)[1/p]
 \longrightarrow K_1(E\times P)[1/p]
 \longrightarrow K_0(B)[1/p]
 \longrightarrow K_0(Z\times P)[1/p]\oplus K_0(P)[1/p].
\tag{NK.8}
\]

The final map is injective by NK.6, so the preceding map is surjective. The (K_1(P)) contribution is already the restriction of its pullback to (Z\times P). Subtracting that actual pullback proves NK.7. This is an actual fixed-product conclusion, with no replacement of (R), (Z), or (P).

## NK.4. Pointwise kernel and exact pure-weight endpoints

The same FF sequence for a point shows

\[
\ker\bigl(K_1(Z)_{\mathbf Q}\longrightarrow K_1(E)_{\mathbf Q}\bigr)
       \subseteq\operatorname{im}\bigl(K_1(R)_{\mathbf Q}\to K_1(Z)_{\mathbf Q}\bigr).
\tag{NK.9}
\]

To account explicitly for the (K_1(k)) term, exactness first represents a pair ((a,0)) as the image of (b\in K_1(R)\), so every kernel element is in the displayed image. Conversely an arbitrary image need not restrict to zero unless its residue vanishes: the correct equality is therefore

\[
\ker\bigl(K_1(Z)_{\mathbf Q}\to K_1(E)_{\mathbf Q}\bigr)
  =\operatorname{im}\bigl(\ker[K_1(R)_{\mathbf Q}\to K_1(k)_{\mathbf Q}]
                              \to K_1(Z)_{\mathbf Q}\bigr).
\tag{NK.9a}
\]

Thus NK.9 is the useful containment, and NK.9a records the exact residue-zero subgroup. The coefficient-field section splits (K_1(k)\to K_1(R)), and constant terms can be tracked through the diagonal if needed. Since (R) is commutative local, elementary row reduction gives (K_1(R)=R^*\); Adams (\psi^q) is multiplication by (q) on this additive unit group. Hence the kernel in NK.9a is pure weight one.

Suppose, in addition, that an actual proper (K_1) family on (E\times P) has endpoint difference **exactly** (\{u\}\beta), where (u\in k^*\) and (\beta\in K_0(E)_{\mathbf Q}) has weight two. Under the henselian point isomorphism FF.4 let (\beta_Z\) be its unique weight-two lift to (Z). Lift the family by NK.7. The difference between its endpoint class on (Z) and (\{u\}\beta_Z) lies in NK.9a and is killed by (\psi^2-2). Applying

\[
                    (\psi^2-2)/6
\tag{NK.10}
\]

to the lifted proper family therefore makes its endpoint difference **exactly** (\{u\}\beta_Z): the desired product has eigenvalue (2\cdot4=8), so NK.10 acts as one on it. There is no projector on all of (K_1(Z\times P)) and no semisimplicity assertion. This conclusion is conditional on the exact exceptional endpoint, which HK alone originally prescribed only componentwise.

## NK.5. The scalar-extension and finite-closure gaps remain

For a symbolic (u), (R\otimes_k k(u)) generally is not local or henselian. NK.1's properness argument cannot be repeated there, and neither NK.7 nor NK.10 gives an actual family on the original constant product after such a replacement.

A finite étale stage near a chosen point of a henselization can be placed in a finite normalization by Zariski Main under the appropriate excellent finite-type hypotheses. This does not by itself extend a (K_1) class. On a regularized finite cover, if the class is defined only on an open (V), the exact obstruction to extension is its localization boundary in (K_0) with support in the complement. Conjugation transports that boundary; summing conjugates gives its trace, which has not been proved zero. Opens containing different closed-fibre branches overlap generically, so the classes do not acquire a canonical extension by zero. A coherent closure can extend a (K_0) class while failing to extend a (K_1) automorphism together with its inverse. No vanishing of the pushed boundary modulo the exceptional subgroup (Q) and actual proper relations has been established.

This is a precise missing step of the trace repair, not a counterexample to every possible repair and not a main-quotient counterexample. The Artin–Schreier example retained in `../cycles/notes/henselian_branch_closure_countermodel.md` remains a method test; no K-theoretic nonvanishing is imported from it.

## Sources and exact reading scope

- The Stacks Project Authors. (2026). *Relative effective Cartier divisors*, Lemma31.19.9, especially(3), [Tag062Y](https://stacks.math.columbia.edu/tag/062Y). Entire statement and printed proof freshly read before checkpoint23 freeze; used at the closed-fibre points in NK.3.
- The Stacks Project Authors. (2026). *Applications of Zariski's Main Theorem, I*, Lemmas37.44.1–37.44.2, [Tag02LS](https://stacks.math.columbia.edu/tag/02LS), [Tag02UP](https://stacks.math.columbia.edu/tag/02UP). Both complete printed proofs freshly read; used to make the relative Cartier supports finite over the actual local (R).
- The Stacks Project Authors. (2026). *Finite projective modules*, Lemma10.78.7, [Tag02M9](https://stacks.math.columbia.edu/tag/02M9). Fresh statement/proof-hints read in the WP audit; the complete elementary rank-one proof is supplied there and reused here. The source does not print a complete proof.
- The relative Serre generation, properness, perfect Cartier pushforward and projection formula are the exact inputs already audited in AE and WP. The normal-domain and coefficient-field Čech argument is supplied explicitly in NK.5.
- NK.8 is the same every-degree fixed-product exact sequence already proved in `C3_fixed_family_negative_K.tex` from Kerz–Strunk–Tamme(2018), Geisser–Hesselholt(2011), and Thomason–Trobaugh(1990). Their preceding complete source audits are reused, not relabelled as fresh.
- Weibel, C. A. (2013). *The K-book*. Chapter IV, Example5.4.1 and Theorem5.9 give the unit Adams action and product compatibility; the latter full printed proof and Example5.9.1 were freshly read in the read-only checkpoint interval. The elementary local (K_1=R^*) identification is also directly the stable Gaussian-elimination argument.
