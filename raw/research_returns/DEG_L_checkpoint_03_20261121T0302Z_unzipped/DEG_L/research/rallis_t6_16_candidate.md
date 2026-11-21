# Candidate T6.16: a distinct indecomposable switch with a Steinberg source

Status: candidate under whole-proof review, 2026-11-21. This file is separate from the checked T6.1–T6.15 module. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. It imports the global and local theorems already itemized in T6.15, and additionally uses Shin §4.3, Theorem 4.8, and §5.3, Theorem 5.13. No claim about an isolated numerical equality between special values is made.

## Proposed theorem T6.16

There exist a Galois CM field \(E\) of degree eight, four **distinct** odd CM sign functions \(v_i\), and an actual four-map surface witness in the framework of 032, Proposition 3.1, with the following properties.

1. \(v_1+v_2=v_3+v_4\), and the selected balanced list \(v_1,v_2,-v_3,-v_4\) has no nonempty proper balanced sublist. Thus this is an indecomposable four-factor switch in the literal tensor sense, rather than a wedge paired with its own conjugate. Distinctness here concerns the labeled CM types; it does not assert that the four abelian varieties are pairwise nonisogenous or simple.
2. There are a smooth connected projective compact ball quotient \(Y\), actual morphisms \(f_i:Y\to B(v_i)\), and nonzero eigenforms \(\alpha_i\in U(v_i)_1\), chosen with algebraic Betti coefficients, such that
   \[
   \int_Y f_1^*\alpha_1\wedge f_2^*\alpha_2
          \wedge\overline{f_3^*\alpha_3\wedge f_4^*\alpha_4}\ne0.
   \tag{T16.1}
   \]
3. In a specified full unitary Shimura variety containing \(Y\) as a connected component at a sufficiently deep level, the zero extension of the first wedge in (T16.1) has nonzero projection to an actual target automorphic isotypic space whose dimension-two theta source has cuspidal base change with a Steinberg local component. In particular its Weil–Deligne monodromy is nonzero at a fixed finite split place.
4. For the actual product morphism \(f=(f_1,f_2,f_3,f_4)\), some nonzero term in the exact degree formula T6.13 has such a rank-two source. The image of \(f\) is a surface. A product polarization can be used. The source parameter cannot be a sum of characters or a quadratic induction of a character.

The assertion is existential for this explicit switch, not for every prescribed indecomposable relation. It concerns the actual source in an exact theta-norm expansion of the degree; it does not identify that source standard parameter with a geometric Galois constituent of the CM cup image.

## Proof

### 1. The four sign functions and the rational spaces

Take a totally real biquadratic field \(F\), for example \(\mathbf Q(\sqrt2,\sqrt3)\), and put \(E=F(i)\). Choose the four representatives of \(\operatorname{Gal}(E/\mathbf Q)/\langle c\rangle\) that fix \(i\), and label them \(\mu,a,b,c_0\), with \(\mu=1\). (The label \(c_0\) is a real place and is not complex conjugation.) On these representatives set
\[
\begin{array}{c|rrrr}
 &\mu&a&b&c_0\\\hline
v_1&+1&+1&+1&+1\\
v_2&+1&-1&-1&+1\\
v_3&+1&+1&-1&+1\\
v_4&+1&-1&+1&+1.
\end{array}
\tag{T16.2}
\]
Extend each function oddly under complex conjugation. The equality of the two pair sums is immediate. The four functions are distinct. A proper balanced sublist cannot have one element. It cannot have three, since the sum of all four is zero and the omitted sign function is nonzero. It cannot have two: the two positive functions cannot cancel, since both take value \(+1\) at \(\mu\); the two negative functions cannot cancel; and a positive and a negative could cancel only if two of the four displayed functions were equal. This proves indecomposability. Since every element of this Galois group has order two, the inversion in 032's convention \(d_i(\tau)=v_i(\tau^{-1})\) makes no change.

Use \(\delta=i\) in 032 §4.2, so its imaginary coefficient is positive at all four chosen representatives. Accordingly \(d_i=+1\) means a negative Hermitian multiplicity line in the Fock convention used here. Choose a dimension-two Hermitian space \(W\) which is negative definite at \(\mu,c_0\), has signature \((1,1)\) at \(a,b\), and is quasi-split at every finite place. Such a space exists by the Hermitian classification and the norm-class product sequence in Gan–Gross–Prasad §15, printed p.161: a quasi-split plane has determinant class \(-1\), and the number of definite real places in this prescription is even. This uses the general classification there, rather than applying their all-definite Lemma 15.4 to the mixed signature prescription.

Choose by weak approximation a vector in \(W(E)\) of negative norm at all real places. Its line \(W_1\) and orthogonal complement \(W_2\) have precisely the signs \(d_1,d_2\) of (T16.2). Thus \(W=W_1\perp W_2\). Convert to a skew-Hermitian theta source by the same fixed trace-zero scalar as in T6.15. Write \(H=U(W)\). It is anisotropic over \(F\), because it is definite at \(\mu\); hence \([H]\) is compact, although two of its real factors are noncompact.

Choose weight-one unitary splitting characters \(\gamma_1,\gamma_2,\gamma_3\) for the first three line types, all restricting to \(\epsilon_{E/F}\), by the CM-character construction used in T6.15. Set
\[
\gamma_4=\gamma_1\gamma_2\gamma_3^{-1},\qquad
\chi_W=\gamma_1\gamma_2=\gamma_3\gamma_4,\qquad
\chi_V=\gamma_1^3.
\tag{T16.3}
\]
The infinity type of \(\gamma_4\) is the required fourth type, and its restriction is again \(\epsilon_{E/F}\). Use the common source splitting \(\chi_V\) for every line and the target splitting \(\gamma_i\) for that line. The source-splitting retwist in T6.12 changes only the source vector and preserves the actual rank-one theta form. For unintegrated kernels evaluated at the source identity, the retwisting character has value one. Crucially the two pairs have exactly the same total target splitting \(\chi_W\), not merely the same infinity type.

### 2. The required real representation, including its exact Gaussian vector

At \(\mu\) take the product of the two holomorphic one-form cocycles, with its nonzero determinant polynomial. At \(c_0\) take the product Gaussian. The same BMM and Haan central-action calculation as in T6.15 makes their source \(U(2)\) representations trivial.

At each of \(a,b\), the target is compact \(U(3)\) and the source is \(U(1,1)\). The total target splitting has zero angular exponent there. The common source splitting is calibrated by the all-negative choice \(\gamma_1^3\): in BMM's notation the twist is \(k=0,\ell=-3\). One can fix this calibration without any ambiguity in the notation for an angular character: at a compact target with a negative definite source plane, the same common splitting makes the Gaussian source invariant, and Proposition 4.15 gives its exponent \((\ell+3)/2\), hence \(\ell=-3\). At a mixed source the Gaussian therefore has maximal-compact character
\[
(z_+,z_-)\longmapsto z_+^{-3},
\tag{T16.4}
\]
where the positive source line is written first. Its character on the ordered pair \((W_1,W_2)\) is consequently \((0,-3)\).

Here is an elementary verification of the entire source representation generated by this vector. In the Fock space write \(x_1,x_2,x_3\) and \(y_1,y_2,y_3\) for the positive and negative variables, and put
\[
R=\sum_{j=1}^3x_jy_j,
\quad E_+=R,
\quad E_-=-\sum_{j=1}^3\partial_{x_j}\partial_{y_j},
\quad H_0=\operatorname{Euler}+3.
\tag{T16.5}
\]
After the usual Fock-unit normalization these are the source \(\mathfrak{sl}_2\) generators; BMM Proposition 5.1, printed p.40, gives the lowering operator, and the raising operator is its negative adjoint. Direct differentiation gives
\[
[E_+,E_-]=H_0,\quad [H_0,E_\pm]=\pm2E_\pm,
\qquad E_-R^j=-j(j+2)R^{j-1}.
\tag{T16.6}
\]
Thus the Gaussian generates \(\mathbf C[R]\), whose genuine \(U(1)\times U(1)\) weights are \((-3-j,j)\), \(j\ge0\), and whose squared monomial norms are \(j!(3)_j\) times the squared vacuum norm. The lowering coefficients are nonzero for every \(j>0\), so this is an irreducible highest-weight module. It is the discrete series \(D_3^-\) specified by these weights. For example, its disk model has reproducing kernel \((1-z\bar w)^{-3}\), or equivalently weighted area norm \(\int_{|z|<1}|f(z)|^2(1-|z|^2)\,dx\,dy\). The automorphy factor of exponent three gives the vacuum coefficient of modulus \((\cosh t)^{-3}\) on a Cartan element with entries \(\cosh t,\sinh t\). Its square is integrable against the Cartan density proportional to \(\sinh(2t)\,dt\). This also verifies square integrability directly.

The real source representation to be globalized is therefore
\[
\pi_\infty=1_{\mu}\boxtimes D_{3,a}^-\boxtimes D_{3,b}^-\boxtimes1_{c_0}.
\tag{T16.7}
\]
Its chosen archimedean vector is the product of the invariant vectors and the two lowest compact-type vectors. That compact-type space is one dimensional.

We also check the extra base-change hypothesis which was automatic in T6.15. For the derived \(\mathfrak{sl}_2\) at a mixed place, use the Casimir
\(C=H_0^2-2H_0+4E_+E_-\). It acts by \(3\). Since \(E_-=-E_+^*\), a unit vector of \(H_0\)-weight \(m\) in any unitary representation with this infinitesimal character satisfies
\[
\|E_-v_m\|^2=\frac{(m-3)(m+1)}4,
\qquad
\|E_+v_m\|^2=\frac{(m-1)(m+3)}4.
\tag{T16.8}
\]
The fixed central character imposes odd parity. Weights \(1,-1\) are impossible by nonnegativity. Starting from any nonzero compact-weight vector, the ladder identities and irreducibility force either the weights \(3,5,\ldots\), or \(-3,-5,\ldots\). They are exactly the two discrete-series members with this central and infinitesimal character. At the compact places the specified infinitesimal character permits only the trivial representation. Labesse's criterion in Remark 5.2, printed p.42, therefore gives hypothesis \((*)\) for (T16.7). This is an explicit verification; no assertion that arbitrary noncompact cohomological infinity types satisfy \((*)\) is used.

Finally the local doubling integral detects the **same** Gaussian vector. GQT §11.3, p.52, normalizes the Siegel–Weil section at \((h,1)\) as the oscillator matrix coefficient. In §11.6, p.54, its other factor is the **complex conjugate** of the source matrix coefficient (the overbar is visible in the original PDF). Identify the cyclic Gaussian module unitarily with \(D_3^-\) and choose its corresponding source vector of norm one. Schur orthogonality gives
\[
Z_v(1/2)=\|\phi_v\|^2\int_{H(F_v)}
       |\langle\pi_v(h)f_v,f_v\rangle|^2\,dh
       =d(\pi_v)^{-1}\|\phi_v\|^2>0.
\tag{T16.9}
\]
The compact-place version is the positive compact integral of T6.15. Thus every factor of this exact archimedean cocycle has nonzero local pairing.

### 3. Globalization, base change, and a nonzero holomorphic rank-two lift

Choose a finite split Steinberg place \(v_s\), a finite nonsplit Steinberg place \(v_i\), and two additional split places \(u_1,u_2\). Let \(S\) contain all real places, \(v_s,v_i\), and all finite bad places for the source, extension, characters and additive character, but exclude \(u_1,u_2\). At the finite places of \(S\), prescribe the unitary unramified-twist Steinberg orbits, as in T6.15. At infinity prescribe (T16.7).

Apply Shin Theorem 5.13, printed p.28, based on §4.3 and Theorem 4.8, pp.19–21. That version explicitly permits \(S\) to contain **all** infinite places and prescribes actual representations there. Its two auxiliary places can be chosen split. To make the local test precise, the characteristic function of the desired archimedean discrete-series tuple belongs to Shin's space \(\mathcal F\): its infinitesimal-character support is a point; twisting a representation of the full real group by an unramified unitary character does not change it, because its center is compact; and unitary parabolic induction from a proper real Levi cannot contain these strict discrete series. The latter assertion also follows from (T16.8) and the distinct infinitesimal characters of tempered principal series. Products with the finite discrete-series-orbit indicators of Example 5.6 remain in \(\mathcal F\). Their Plancherel integral is positive. Thus one may apply Theorem 4.8 directly to this indicator and use the proof of Theorem 5.13. This avoids an unproved selection of a member merely from a cohomological packet.

We obtain a cuspidal automorphic \(\pi\) with exactly (T16.7), Steinberg twists at all finite places of \(S\), unramified outside \(S\cup\{u_1,u_2\}\), square-integrable at \(u_1\), and supercuspidal at \(u_2\). Labesse Corollary 5.3 applies by the preceding verification of \((*)\). Its local compatibility at the split place \(v_s\) implies that its rank-two isobaric base change \(\Pi\) is cuspidal, by exactly the rank-two argument in T6.15. Theorem 5.9 then identifies all finite local base changes, since the source is quasi-split at every finite place.

Choose the dimension-three target with signature \((2,1)\) at \(\mu\), and positive definite at \(a,b,c_0\). At the nonsplit bad places Atobe–Gan Theorem D.2(i) permits both target spaces for a Steinberg source: its Weil–Deligne parameter has no \(\chi_V\otimes S_1\) summand. At every split place, including both auxiliary places, Mínguez's theorem makes the lift nonzero for every source representation. At the remaining places use the unramified theta lift. Correct global Hermitian coherence at \(v_i\), where both choices are allowed. The resulting \(V\) is anisotropic over \(F\), because it is definite at three real places.

The fixed real cocycle survives by (T16.9). Choose the finite bilinear local entries by GQT Proposition 11.6. The twisted unitary cuspidal \(\mathrm{GL}_2\) value at \(1\) is nonzero by the theorem cited in T6.15. GQT Theorem 11.4, with \(n=2,m=3,r=0\), therefore gives a nonzero global theta lift with this **fixed** real cocycle. Fix an actual source realization and a corresponding actual irreducible target realization \(\sigma\). The latter is irreducible by Wu's theorem as used in T6.13. At \(v_s\), its local parameter has nonzero monodromy by Mínguez's formula. These are precisely the compatibility conditions checked in T6.15, with the real step replaced by (T16.7)–(T16.9).

### 4. A total 032 theta input retaining this constituent

We first obtain a total unintegrated theta form with nonzero \(\sigma\) projection. Let \(\mathcal K_{\phi}(g,h)\) denote the rank-two kernel with the fixed real cochain and variable finite Schwartz input. Project in the source variable to the chosen actual realization of \(\pi\). The span of all scalar canonical-frame coefficients
\[
\mathcal I=\operatorname{span}_{\phi_f,g}
 P_\pi\mathcal K_{\phi_\infty\otimes\phi_f}(g,-)
\tag{T16.10}
\]
is nonzero by the nonzero global lift. It is stable under \(H(\mathbf A_f)\), by replacing \(\phi_f\) with its source translate. Its archimedean compact-type space is the one-dimensional space just specified. Thus irreducibility of the smooth finite representation gives \(\mathcal I=\pi_f^\infty\otimes\ell_\infty\).

Evaluation at the source identity is nonzero on this space after a suitable finite translate. Here is the needed density argument, since \(\pi_\infty\) is no longer trivial. The Cayley transform from skew-adjoint endomorphisms to \(U(W)\) gives a rational open chart. Weak approximation in its affine coordinates shows that \(H(F)\) is dense in \(H(F_\infty)\). For a point represented by \((h_\infty,h_f)\), choose \(q_n\in H(F)\) with \(q_{n,\infty}\to h_\infty\). The classes of \((1,q_{n,f}^{-1}h_f)\), represented also by \((q_{n,\infty},h_f)\), approach that point. Consequently the image of \(H(\mathbf A_f)\) is dense in \([H]\). A nonzero continuous automorphic vector in \(\pi_f^\infty\otimes\ell_\infty\) is nonzero at some such finite point; a finite right translate then has nonzero value at the identity and still lies in the same archimedean line.

It follows from (T16.10) that some projected kernel has nonzero value at \(h=1\). The mixed-source orthogonality and finite holomorphic spectral support established in T6.12 imply that this yields a nonzero target \(\sigma\) contribution in \(\mathcal K_\phi(-,1)\); the other source realization terms cannot cancel it. At infinity this unintegrated form is exactly the double-alternating degree-two theta tensor of 032, up to its allowed nonzero constant-line trivialization. Indeed the compact-place factors are its Gaussians and the active factor is the determinant obtained from the product of the two first tensors; this is the explicit coefficient calculation in 032, Proposition 4.6(i), pp.23–24, and BMM Proposition 5.19. Thus choose a finite total input for which
\[
\xi=\Xi_W(\phi;t_0),\qquad P_\sigma\xi\ne0.
\tag{T16.11}
\]
Take a sufficiently deep neat finite level fixing this input. One may work with the finite disjoint union of connected components of the full unitary Shimura variety. Each component admits a further principal special-unitary cover of the kind used in 032: the integral determinant subgroup is finite and is killed by a sufficiently deep neat level. Only finitely many components and inputs will be needed.

### 5. A Hecke projector preserves the two pair-type spans

At the fixed finite level let \(\mathcal H\) be the finite-dimensional space of holomorphic top forms on the full Shimura variety. The image of the finite-level Hecke algebra on \(\mathcal H\) is a finite-dimensional star algebra, with adjoints for the Petersson pairing. Its central orthogonal idempotents project to its irreducible isotypic spaces. In particular there is a finite Hecke operator \(Q\) equal to the orthogonal projection to the \(\sigma_f\)-isotypic space. This includes all its actual multiplicity copies, which is sufficient.

For precision, an irreducible smooth finite-adelic representation with nonzero level invariants is determined by its irreducible module for that level Hecke algebra: the full representation is generated by those invariants, and a module isomorphism extends through compact induction and its irreducible quotient. All target representations occurring in \(\mathcal H\) have the same holomorphic top-degree real representation, with trivial compact factors. Equivalently their scalar canonical coefficients are annihilated by the antiholomorphic lowering algebra and have the prescribed canonical compact type, whose irreducible highest-weight quotient is unique. Hence the relevant Hecke isotypic space consists of copies of the same full target representation \(\sigma\). At the Steinberg place every one of these copies has nonzero local monodromy. In particular \(Q\xi\ne0\).

Let \(\mathcal U_{12}\) be the span of products of theta one-forms of the first two line types, allowing all finite Schwartz inputs, and define \(\mathcal U_{34}\) similarly. A finite target translate of a product is the product of the same simultaneous translates of its two factors. Convolution by a compactly supported bi-level-invariant Hecke function is a finite sum of these translates on a fixed smooth vector. It follows that every finite Hecke operator, in particular \(Q\), preserves each of these two pair-type spans. This statement does not assert that it preserves one individual product. The translated individual factors may require a deeper common level than the final Hecke output; the finite expansions are first understood adelically, and all their factors descend together at the principal level chosen in the next step.

Apply 032, Proposition 4.6(iii) and Corollary 4.7, to the single input chosen in (T16.11). The rational decompositions \(W=W_3\perp W_4\) with signs \(d_3,d_4\) approach the first decomposition in total compact-place period data, with the active data exactly fixed. The global splitting choices agree by (T16.3). On the fixed quotient the resulting \(\xi'\) approach \(\xi\) smoothly. The operator \(Q\) is bounded, so
\[
\langle Q\xi,Q\xi'\rangle\longrightarrow\|Q\xi\|^2>0.
\tag{T16.12}
\]
Choose a sufficiently close rational endpoint. Both endpoint forms are holomorphic, and the finite wedge expansions of 032 give
\[
x=Q\xi\in\mathcal U_{12},\qquad
y=Q\xi'\in\mathcal U_{34},\qquad
\langle x,y\rangle\ne0,
\tag{T16.13}
\]
with \(x,y\) in the full \(\sigma\)-isotypic space. Continuity can be applied on the finitely many components at once; the same Gaussian estimates prove it on each compact component, so their finite sum has (T16.12).

### 6. Extract actual CM maps without losing the first constituent

Choose a connected component \(S\) on which the pairing of \(x|_S,y|_S\) is nonzero. There are only finitely many terms in their translated line-theta expansions. Apply 032, Corollary 6.7, printed p.45, to these finite families for all four sign functions and pass to one connected common principal cover \(Y\to S\). The pairing remains nonzero because it is multiplied by the degree of the finite étale cover. At the new full finite level the pullback of the global form \(y\) is still in the same full automorphic \(\sigma\)-isotypic space; pulling back has not changed the scalar adelic function.

Fix nonzero generators of the four selected eigenlines. The finite-family CM extraction and equality of harmonic representatives on a compact Kähler variety write
\[
x|_Y=\sum_r a_r A_r,\quad
A_r=h_{1r}^*\alpha_1\wedge h_{2r}^*\alpha_2;
\qquad
y|_Y=\sum_s b_s B_s,\quad
B_s=h_{3s}^*\alpha_3\wedge h_{4s}^*\alpha_4,
\tag{T16.14}
\]
where the \(h_{ir}\) denote rational Hodge maps, or corresponding rational homomorphisms from the Albanese. Since \(\langle x|_Y,y|_Y\rangle\ne0\), some \(r\) satisfies \(\langle A_r,y|_Y\rangle\ne0\). The zero extension \(A_r^0\) to the new full Shimura variety then has nonzero \(\sigma\)-projection, because its pairing with the global \(\sigma\)-form \(y\) is that same nonzero number. Next expand only \(y|_Y\) in (T16.14); some \(s\) satisfies \(\langle A_r,B_s\rangle\ne0\).

This sequential choice is necessary: a nonzero projected pairing alone would not justify choosing an individual pair whose unprojected period and projected first wedge are both nonzero. Here the first choice guarantees survival of its constituent before the second choice supplies the full period.

Clear the four rational-homomorphism denominators. By 032, Lemma 2.2 and Proposition 3.1, this gives actual morphisms \(f_i:Y\to B(v_i)\). Multiplication by the four nonzero integers scales each selected wedge and period by nonzero factors. It preserves the first wedge's nonzero \(\sigma\)-projection and proves (T16.1).

Finally choose a product ample polarization on \(\prod_i B(v_i)\). In each factor its chosen eigenform can be rescaled to be the first vector of a unit invariant coframe and then extended to such a coframe. The first two factors yield a coordinate wedge proportional to \(A_r\). The exact degree identity T6.1 therefore has a term with nonzero \(\sigma\)-projection; T6.13 can use the rank-two theta model already constructed for that projection. Mínguez's split-place formula prevents any rank-two source with zero monodromy from giving this same target local representation. A one-dimensional Weil–Deligne parameter, its direct sum with another, or its quadratic induction has zero monodromy, while the actual source has Steinberg monodromy. The first wedge is nonzero, so \(f\) has surface image. This proves all four assertions. QED.

## Primary-source additions and checks needed before promotion

- Shin, <https://math.berkeley.edu/~swshin/Plancherel.pdf>: Definition 2.1 and Example 2.3, pp.8–9; §4.3 and Theorem 4.8, pp.19–21; Example 5.6, p.26; §5.3 and Theorem 5.13, p.28. The crucial version includes infinity in the prescribed set. Its full short proof and the scope of §4.3 have been read.
- Labesse, <https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf>: Remark 5.2, p.42, Corollary 5.3, pp.43–44, Theorem 5.9, p.49. The new elementary Casimir computation supplies the specific sufficient condition in Remark 5.2.
- BMM, <https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6812-11511_2016_Article_136.pdf>: Proposition 4.15, p.38, and its adjoining proof; Proposition 5.1, p.40; Proposition 5.19, pp.49–50. The local real proof above imports the Fock action, then computes its cyclic module explicitly.
- GQT, <https://arxiv.org/pdf/1207.4709>: §11.3, p.52, and §11.6, p.54. Original p.54 visually checked for the overbar on the source matrix coefficient. The remaining local/global source locators are those already in T6.15.
- Gan–Gross–Prasad, <https://www.numdam.org/item/AST_2012__346__111_0.pdf>: §15, printed p.161, general Hermitian classification and product exact sequence. The new signature prescription uses two definite and two indefinite real places.
- Supplied 032: §4.1–4.2, pp.13–14; Proposition 4.6 and Corollary 4.7, pp.23–25, entire proofs reread; Corollary 6.7, p.45, entire proof reread. Their fixed-input continuity and finite CM extraction are imported with their stated hypotheses.

Review must examine the real splitting calibration, the direct Shin indicator application, the fixed archimedean-line source-spanning argument, identification with the 032 total tensor, the finite Hecke projector and its preservation of pair-type spans, and the component/cover/zero-extension order in the last extraction. Existing T6.15 has not been altered.
