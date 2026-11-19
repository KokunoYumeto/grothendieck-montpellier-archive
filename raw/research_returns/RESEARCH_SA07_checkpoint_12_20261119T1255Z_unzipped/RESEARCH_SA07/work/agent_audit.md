# F.3 assertion audit: supplemental proofs and source scopes

This working document supplies the mathematical arguments still needed by the requested note-by-note audit. It is not a reconstruction of unread handwriting. The two supplied frozen transcriptions and their notes are the witnesses; no original archive scan has been inspected. The source-entry extraction contains exactly 154 requested entries: 52 from notes [I], 94 from notes [II] (including MB03b), and eight cote-18 standing-question rows. Every entry is retained in the accompanying assertion inventory, including cancelled assertions, readings, and documentary gaps. Reused typescripts outside those explicitly requested entries are excluded.

## F.3.1 — Oda's characteristic-p comparison and its Hodge extension

**Status: proved by the cited primary theorem, with its precise scope.** Let k be a perfect field of characteristic p, with no exclusion of p=2, and let A/k be an abelian variety. Write M for the contravariant Dieudonné functor on finite commutative p-primary group schemes, in the left-Dieudonné-module convention of Oda. There is a canonical isomorphism

\[
 M(A[p])\xrightarrow{\sim}H^1_{\mathrm{dR}}(A/k).
\]

Its domain carries the semilinear operators F and V, with FV=VF=p=0. The isomorphism sends VM(A[p]) to the Hodge subspace H^0(A,Ω^1), and the quotient to H^1(A,O_A). It consequently identifies the short exact sequence defined by that submodule with

\[
0\longrightarrow H^0(A,\Omega^1)\longrightarrow
H^1_{\mathrm{dR}}(A/k)\longrightarrow H^1(A,\mathcal O_A)
\longrightarrow0.
\]

These are actual maps of k-vector spaces with the additional Dieudonné operators transported by the displayed isomorphism. Oda's Corollary 5.11, printed p.131, states the comparison and compatibility; its proof composes Proposition 4.1 with Theorem 5.10. The same page describes the V-submodule by the Frobenius-twisted Dieudonné module of the Frobenius kernel. Thus the extension with its distinguished maps is recovered functorially from A[p]. A bare splitting of the underlying vector-space sequence is not part of that assertion. Nor does it supply a mixed-characteristic lift or a p-adic Galois representation of a lift. Those maps and their essential images are separately constructed in B.1–B.2.

**Opened source:** T. Oda, *The first de Rham cohomology group and Dieudonné modules*, Ann. Sci. ÉNS (4) 2 (1969), 63–135, Corollary 5.11, p.131 (PDF page 70). The local image of this printed page was inspected. URL: <https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf>.

## F.3.2 — The two Lefschetz operator images, and the integral obstruction

**Status: proved explicitly.** Let V_m have basis v_0,…,v_m. Define

\[
Ev_j=v_{j+1},\quad \Lambda v_j=v_{j-1},\quad
Fv_j=j(m-j+1)v_{j-1},\quad Hv_j=(2j-m)v_j,
\]

with the raising and lowering operators zero beyond the endpoints. For every basis vector, including both endpoints, direct subtraction gives

\[
[E,F]=H,\qquad[H,E]=2E,\qquad[H,F]=-2F.
\]

If π_j is projection to Qv_j, then the typed conversion maps in End_Q(V_m) are

\[
 F=\sum_{j=1}^m j(m-j+1)\Lambda\pi_j,\qquad
 \Lambda=\sum_{j=1}^m\frac{1}{j(m-j+1)}F\pi_j.
\]

This proves exactly the rational comparison asserted in MB03. For the simultaneous image take W=⊕_{m=0}^d V_m. Put B=1−EΛ and T=1−ΛE. On each string they project to its bottom and top. Hence

\[
B_m=B\Lambda^mTE^mB
\]

is projection onto the bottom of the length-m string alone: E^m kills shorter strings and T kills its image on longer strings. Therefore E^b B_m Λ^a, 0≤a,b≤m, sends v_a in that string to v_b and kills every other basis vector. They are the matrix units and prove, by their actual representation on W,

\[
\mathbf Q[E,\Lambda]=\prod_{m=0}^d\operatorname{Mat}_{m+1}(\mathbf Q).
\]

For the sl_2 image the Casimir C=H²+2H+4FE acts on V_m by m(m+2). These numbers are pairwise distinct for m≥0. Polynomial interpolation in C gives the projectors to the strings, and interpolation in H on each string gives π_j. The preceding conversion recovers Λ from E,F,H. Conversely H=[E,F] and the formula for F shows it lies in Q[E,Λ]. Thus these are equal subalgebras of End_Q(W), not merely abstractly isomorphic algebras. For W=⊕ P_m⊗V_m the image is the same product acting by identity on the multiplicity spaces P_m.

The integral equality fails already on the specified integral string V_2=Zv_0⊕Zv_1⊕Zv_2. Here F and H have all entries divisible by 2. Reducing Z[E,F,H] modulo 2 therefore gives the subalgebra F_2[E]. Each element sends v_2 into F_2v_2, whereas Λv_2=v_1. Consequently Λ∉Z[E,F,H]. The same matrix-unit proof gives Z[E,Λ]=Mat_3(Z). This proves the obstruction caused by the divisions in MB03 without asserting any failure for all alternative integral normalizations.

The finite exact certificate `work/code_triangle/audit_operators.py` checks the commutators and conversions for m=0,…,10 and all matrix-unit formulas for d=0,…,5. The preceding basis-vector proof covers all m,d and is the proof of the universal statements.

## F.3.3 — Four gradings and their actual comparison maps

**Status: proved explicitly; the indicated identifications fail.** For a smooth projective X of dimension d, define on H^i(X)

\[
w_X(t)=t^i,\qquad\lambda_X(t)=t^{i-d}.
\]

Thus λ_X(t)=t^{-d}w_X(t). Both conjugate a degree-j operator by t^j. The cohomological weight is tensor compatible, and w_{Q(1)}(t)=t^{-2}. For ε the character on Q(−1), ε∘w=t². This is the central grading of Deligne–Milne, Definition 5.1. It is an equality of the actual characters, so it cannot equal the manuscript's specified splitting with ε∘j=t.

A concrete parabolic calculation shows where that latter splitting lives. In GL_2 let B be the upper triangular subgroup, U its strictly upper triangular unipotent radical, L the diagonal Levi, and ε=det. The cocharacter j(t)=diag(t,1) is central in L and satisfies εj=t. It is not central in GL_2: conjugation by j(t) sends E_{12} to tE_{12}. Its centralizer is L. By contrast w(t)=tI is central and εw=t². These maps relate the Hodge-filtration splitting, its Levi centralizer, and the tensor weight without identifying their different characters. This example also proves why the word “central” on 18:11 cannot be moved from B/U to all of G without another assertion.

For H^*(P^1)=Qe_0⊕Qe_2 the matrices are

\[
 E=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
 F=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
 H=\operatorname{diag}(-1,1),\quad
 \rho(z)=\operatorname{diag}(1,z).
\]

Every ρ(z) fixes e_0, whereas exp(sE)e_0=e_0+se_2. This particular Lefschetz SL_2 representation therefore has no factorization through ρ(G_m). The relation that does hold is ρ(z)Eρ(z)^{-1}=zE and ρ(z)Fρ(z)^{-1}=z^{-1}F. The class of a point gives the equivariant morphism E:h^0→h^2(1), because its target twist cancels z. On H^1 of an elliptic curve, E and F have targets H^3 and H^{-1}, both zero, and the Lefschetz H=i−d equals zero. The resulting sl_2 action is zero; the standard nontrivial SL_2 action of the elliptic normalized period group on that two-dimensional space is consequently not that action. The displayed maps are all that is needed for this comparison; no assertion of unrelated mathematical theories is made.

## F.3.4 — Reconstruction, arithmetic base change, and the modern comparison maps

**Status: established theorems with the hypotheses retained.** For a neutral rigid abelian Q-linear tensor category C with exact faithful fibre functor ω, define G=Aut^⊗(ω). Its action on each ω(M) is compatible with a morphism a:M→N by the explicit equation

\[
g_N\,\omega(a)=\omega(a)\,g_M.
\]

Deligne–Milne, Theorem 2.11, proves that M↦(ω(M),g_M) is an equivalence C≃Rep_Q(G). Theorem 3.2 represents Isom^⊗ between fibre functors as a torsor. Those are the precise reconstruction arrows required by MB02. For a cohomological correspondence category the morphism represented by z is p_{2*}(p_1^*(−)∪cl(z)), with its degree and Tate twist as in F.1.3; composition is the push–pull formula on the triple product. Passing to projectors and Tate twists constructs the usual pure category. This construction is not a documentary claim that the unfinished historical category had already been specified.

Fix Qbar⊂C. For Nori motives with rational coefficients the pullback functor along Q→Qbar and the inclusion of Artin motives induce

\[
1\longrightarrow G_{\mathrm N}(\overline{\mathbf Q})
\longrightarrow G_{\mathrm N}(\mathbf Q)
\longrightarrow \operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)
\longrightarrow1.
\]

Here the last term is the proconstant Q-group, and all groups use the compatible Betti fibre functors. Exactness is Kahn (2025), Theorem 5.10 and §5.8 applied using Theorem 10.2 and Remark 10.3. His Theorem 5.10 does not require semisimplicity. In particular the left subgroup is normal and the quotient is the stated arithmetic group. The sequence supplies neither a distinguished splitting nor an identification of its kernel with the identity component. Kahn's introduction, p.589 and footnote 1, explains the gap in the older proof of Deligne–Milne Proposition 6.23(a), which had used normality before establishing it; the 2025 theorem supplies the argument rather than repeating that gap.

For a field k⊂C and a principal ideal coefficient domain Λ, Choudhury–Gallauer construct opposite Hopf-algebra maps between Ayoub's and Nori's Betti motivic Hopf algebras and prove in Theorem 9.1 that they are inverse isomorphisms. Applying Spec reverses the arrows and identifies the associated affine group schemes, with their specified Betti realization. It does not choose a lattice inside an arbitrary rational representation: a chosen integral representation and lattice are transported by the functor, but the representation alone has many lattices.

Arapura's Theorem 6.3.3 proves semisimplicity of the pure rational Nori category; Theorem 6.4.1 identifies it with André's category of motivated pure motives (at a point). The functor carries algebraic-cycle correspondences to motivated correspondences. General fullness of its Hodge realization is stated there as Conjectures 7.1.1–7.1.2, while Corollary 7.1.4 proves fullness for the subcategory generated by abelian varieties. Thus the actual pure and mixed comparison functors are specified, and the general realization essential-image or Hodge-fullness assertion remains an exact unresolved obligation, not a consequence of a Hopf-algebra isomorphism. For motives defined with homological algebraic-cycle correspondences, the fullness question is the Hodge-cycle surjectivity question on the relevant products as in C.1.2.

**Opened sources and locators:** Deligne–Milne, *Tannakian Categories*, 2012 corrected notes, Theorems 2.11 and 3.2; Kahn, *Galois descent for motivic theories*, TAC 44 (2025), Theorem 5.10 p.606, §5.8, Theorem 10.2 and Remark 10.3 p.612; Choudhury–Gallauer, *An isomorphism of motivic Galois groups*, arXiv:1410.6104v3, Theorem 9.1 p.41; Arapura, *An abelian category of motivic sheaves*, arXiv:0801.0261v4, Theorems 6.3.3, 6.4.1, Conjectures 7.1.1–7.1.2, Corollary 7.1.4.

## F.3.5 — Numerical quotient, centres, and the missing Tate extension data

**Status: proved, with the standard-conjecture gate expressed as an exact map.** A homologically trivial algebraic cycle is numerically trivial: pair its zero cohomology class with every complementary cycle class. Thus the identity on cycles induces a surjective quotient map

\[
\operatorname{Hom}_{\mathrm{hom}}(M,N)
\twoheadrightarrow\operatorname{Hom}_{\mathrm{num}}(M,N).
\]

Jannsen's Theorem 1 proves semisimplicity of the rational category for numerical equivalence. It does not construct a cohomology realization of that quotient. Such a realization, agreeing with the homological realization, factors through the displayed quotient exactly when every element of its kernel acts by zero in cohomology. On the relevant smooth projective products, Künneth and Poincaré duality identify a correspondence class with its linear cohomology action in all degrees. Consequently vanishing of every such action is precisely equality of numerical and homological equivalence for those correspondence classes. This proves the exact factorization criterion and retains the general standard-conjecture obligation.

Semisimplicity supplies no centre-free conclusion. A representation of G_m is a direct sum of integer-character spaces, giving semisimplicity of Rep_Q(G_m), whereas the kernel of the conjugation map G_m→Aut(G_m) is all of G_m. This is the explicit counterexample to the suggested inference.

Even the normalized group together with a surjection to the Tate torus need not specify the full group. Take (G_1,ε_1)=(GL_2,det) and (G_2,ε_2)=(G_m×SL_2,pr_1). Both kernels are SL_2. They are not isomorphic as algebraic groups: Z(G_1)=G_m is connected while Z(G_2)=G_m×μ_2 is disconnected. Their relation is the explicit central isogeny

\[
G_m\times SL_2\longrightarrow GL_2,\qquad(q,A)\longmapsto qA,
\]

whose kernel is {(1,I),(−1,−I)} and whose determinant is q². Thus this natural comparison changes the specified Tate character by a square. It proves exactly what extension datum is missing from reconstruction using only the normalized group.

**Opened sources:** Jannsen, *Motives, numerical equivalence, and semi-simplicity*, Invent. Math. 107 (1992), Theorem 1, p.448, and Corollary 1; Deligne–Milne Proposition 2.23. Grothendieck's printed 1969 standard-conjecture note, pp.195–196, gives printed C for algebraicity of Künneth projectors and printed B for algebraicity of Λ, together with B(X)⇒A(X) and A(X×X)⇒B(X). These establish the two recoverable parts of the historical letter dictionary; the absent historical definitions do not determine its remaining two letters. Kleiman (1994), printed p.17, defines D as numerical=homological and records the associated implications. None of these opened printed pages decides an unread historical symbol.

## F.3.6 — The linear maps underlying the anabelian comparisons

**Status: established theorems and explicit maps; the truncated LM6 statement remains a source gate.** Let k be a number field, viewed as a sub-p-adic field, and X,Y hyperbolic curves. Mochizuki's Theorem A identifies dominant k-morphisms with the appropriate open continuous homomorphisms of arithmetic fundamental groups over G_k, modulo geometric inner automorphisms. It also gives the geometrically pro-p version under its specified hypotheses. The statements are fully qualified Hom statements; arbitrary homomorphisms are not substituted for open ones.

For proper curves with chosen base points, the Albanese maps give, after geometric pro-ℓ abelianization,

\[
\pi_1(X_{\bar k})^{\mathrm{ab},\ell}\simeq T_\ell J_X,
\qquad
\pi_1(Y_{\bar k})^{\mathrm{ab},\ell}\simeq T_\ell J_Y.
\]

A morphism of curves sends the first module to the second by the map induced by its covariant map J_X→J_Y. Inner ambiguities disappear after abelianization. The compatible linear map is governed over a number field by the rational Faltings Hom theorem and over a finite field by Tate's integral Hom theorem. Hence the comparison from nonlinear fundamental groups to linear Tate modules is explicitly abelianization followed by Albanese; it does not recover a curve map from every Jacobian homomorphism. For example multiplication by 2 on a genus-g Jacobian induces an invertible rational Tate-module map. For a curve of genus g≥2, no degree-2-multiplication action can come from a nonconstant self-map: Riemann–Hurwitz forces a self-map to have degree 1, hence it preserves the principal polarization, whereas multiplication by 2 pulls it back to four times itself.

For an extension 1→Δ→Π→Γ→1 with Z(Δ)=1, define

\[
\Pi\longrightarrow\Gamma\times_{\operatorname{Out}(\Delta)}
\operatorname{Aut}(\Delta),\qquad
p\longmapsto(\bar p,\operatorname{Ad}(p)|_\Delta).
\]

Its kernel is Z(Δ), hence trivial. For a pair (γ,a) on the right, choose a lift p of γ. Equality of the outer classes says a=Ad(δ)Ad(p) for some δ∈Δ, so δp maps to that pair. This proves the reconstruction and its precise centre hypothesis. For the curve groups used here, Mochizuki's Lemma 1.3.1 and Corollary 1.3.2 supply the slimness and the application; these hypotheses are not replaced by semisimplicity of a representation category.

For a smooth projective real curve of genus at least two, Pál's Theorem 1.3 with Example 5.8 identifies connected components of X(R) with conjugacy classes of sections of the full profinite arithmetic fundamental-group sequence. If two sections lift complex conjugation by l and l′=δl, their actions on Δ^ab coincide because Ad(δ) acts trivially there. Thus the linear involution on first cohomology is independent of the component. The entire abelianized extension or a section cocycle can retain more data than that single involution; this argument only computes its conjugation action. It proves the exact loss at the linear map without making a broader non-reconstruction assertion.

Stix's Definition 26 requires Hom_{G_k}(Z_ℓ(1),T_ℓA)=0 for every abelian variety A and every ℓ. For number fields this follows at a good prime v∤ℓ: arithmetic Frobenius has eigenvalue q_v on the Tate twist and absolute values q_v^{1/2} on T_ℓA, so no nonzero equivariant map exists. His Definition 29 additionally requires an **open** arithmetic image of the normalizer and its cyclotomic conjugation action. Theorem 30 then characterizes nontrivial closed pro-ℓ subgroups of the geometric fundamental group lying in cusp inertia by cyclotomic normalization. The incomplete LM6 summary does not state all these premises and its missing character condition is retained as an exact source obligation. No theorem about a different predicate is substituted.

**Opened sources:** Tate (1966), Main Theorem p.134; Mochizuki (1999), Theorem A, PDF p.3, and author comments (2019); Mochizuki (2004), Lemma 1.3.1 and Corollary 1.3.2, and author comments (2016); Pál (2011), Theorem 1.3, PDF p.2, and Example 5.8; Stix (2012), Definitions 26 and 29, Theorem 30, PDF pp.10–11. The comments do not change the locators used here.

## F.3.7 — Real fixed points, the real splitting, and the withdrawn compact subgroup claim

**Status: explicit counterexamples and a proved corrected compact assertion.** The fixed points X(R) and the invariant cohomology of X(C) are related by restriction, but restriction need not be an isomorphism. For X=P^1_R, H^1(X(C),Q)^c=0 while X(R)=RP^1 is a circle and H^1(X(R),Q)=Q. The Riemann sphere carries conjugation as reflection through its real equator; choosing the representative in one closed hemisphere gives a homeomorphism from its quotient to a closed disk. Its cohomology is Q in degree zero and zero otherwise, exactly the invariant part of the sphere cohomology, since reflection acts by −1 on H^2. This verifies the quotient example asserted in RH08 without substituting the fixed set for the quotient. For X=Spec C over R, the complex base change consists of two points interchanged by conjugation, so H^0(X(C),Q)^c=Q, whereas X(R) is empty and its H^0 is zero. These calculate the exact maps and disprove both possible universal fixed-point equalities.

For the pure real motive and its triangle, let κ_B be coefficient conjugation, f_∞ rational real Frobenius, and κ_D the semilinear descent involution on de Rham coordinates. Their exact relation is

\[
\kappa_D=\alpha f_\infty\kappa_B\alpha^{-1}.
\]

On Betti Hodge summands both f_∞ and κ_B interchange (p,q), so their composite preserves every labelled summand. Thus the transported de Rham bigrading is κ_D-stable and the normalized splitting β is defined over R. Since γ=(βα)^{-1}, it follows that R(γ)=R(α). This is a real-rationality statement, not an algebraicity statement over Qbar.

The raw maximal-compact centralizer assertion fails for the pure Tate group: G=G_m and the Weil element C=1 have centralizer G_m(R)=R^×, which is not compact. Here is a corrected assertion for the weight-zero quotient in the polarizable real category of C.1.1. Let \dot G=G/im(w), for a finite tensor generator, and let C be the image of the Weil element h(i). Then C²=w(−1)=1 in \dot G, so the normalizer of {C,C^{-1}} is its centralizer. The relation f_∞Cf_∞^{-1}=C^{-1} therefore places f_∞ in that centralizer.

Choose a faithful weight-zero representation V of \dot G and a polarization q. It is an invariant real symmetric form, and B(x,y)=q(x,Cy) is positive definite. Let * be the adjoint for B. Invariance of q and C²=1 give

\[
\operatorname{Ad}(C)(g)=(g^*)^{-1}.
\]

Consequently K=Z_{\dot G(R)}(C)=\dot G(R)∩O(B) is compact. If a compact subgroup H contains K, then C∈K and H is stable under Ad(C). For g∈H, the preceding identity implies g*∈H and hence g*g∈H. This positive-definite self-adjoint operator has all its integer powers in the compact group H; each eigenvalue and its inverse therefore have bounded powers, so every eigenvalue equals 1 and g*g=1. Thus g∈K, proving that K is maximal among compact subgroups. This argument also covers a nonconnected finite-dimensional \dot G. For a pro-group it is a statement on each finite tensor-generator quotient; a finite-dimensional maximal-compact claim is not silently applied to an unspecified inverse limit.

This repairs the mathematical assertion after its explicitly written weight quotient. The paragraph remains withdrawn in the historical witness; the proof does not reverse its deletion state. Deligne–Milne Theorem 4.17(a) gives the related characterization of polarizable real Tannakian categories by compact real bands, with its own category and real structure. The construction above specifies the positive form and the subgroup required for this application.

## F.3.8 — Integral specialization, with the exact source status

For a smooth proper scheme X over a discrete valuation ring R, let i:X_s→X and j:X_η→X be the special and generic inclusions. At the level of Chow groups the specialization map has the explicit construction

\[
\operatorname{sp}:CH^r(X_\eta)\longrightarrow CH^r(X_s),
\qquad z\longmapsto i^!(\widetilde z),
\]

where \widetilde z is any lift in CH^r(X). A closure of cycles gives such a lift. The localization exact sequence says that different lifts differ by i_*a. Cartier Gysin self-intersection gives i^!i_*a=c_1(N_{X_s/X})a=0 because the normal line is trivial, cut out by a uniformizer. This proves independence of the lift and retains integral coefficients. On a prime cycle the formula is the special fibre of its flat closure, with scheme-theoretic multiplicities. Gysin compatibility with the intersection product gives the ring map in the smooth setting.

For a complete DVR and ℓ invertible in R, the compatible square on geometric fibres is stated with integral Z_ℓ coefficients in Fulton, *Intersection Theory*, second edition, Example 20.3.5, p.400. Its vertical cohomology map is the proper smooth specialization isomorphism. The Chow map on geometric fibres is obtained by the finite-extension construction described in that example and passage to the direct limit. The rational-equivalence quotient is integral throughout. Compatibility follows from the relative cycle class of a flat closure and its restrictions to the two fibres; functoriality then gives the equality on Chow classes. Fulton's Proposition and Corollary 20.3, p.399, also prove proper/flat/refined-Gysin compatibility and the ring assertion, with the diagonal proof given there. These statements answer the smooth proper complete-DVR version without discarding torsion.

**Opened primary locators:** Fulton's §20.3, Proposition 20.3, Corollary 20.3, Examples 20.3.1 and 20.3.5, printed pp.398–400, were opened in a text reproduction of the book at <https://djvu.online/file/Pl4avuZzLcI6I>; this was the source text, not a later summary. The university PDF found in search contains only twelve front-matter pages and is not represented as having supplied the theorem. The following Stacks lemmas were also opened: §62.4 (tag 0H4H), Lemmas 62.4.1–62.4.4; §42.29 (tag 02T7); §42.30 (tag 02TK), Lemma 42.30.2 (rational-equivalence descent), Lemma 42.30.3 (self-intersection), and Lemma 42.30.5 (commuting Gysin maps). Localization can also be seen directly: a rational equivalence on the generic fibre extends by closing each supporting variety and taking the same rational function; the discrepancy is supported on the special fibre and is in the image of i_*.

**Historical-source limitation:** the SGA 6 original scan from <https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf> was downloaded. Its PDF pages 586 and 587, inspected as images, show printed pp.579 and 581. They contain the beginning of Remark 7.13.11 and the end of the continuation, but the mirror omits printed p.580, which contains (7.13.12). Accordingly that middle original page is not claimed as inspected. The frozen supplied 18:7 transcription remains the archive witness, and the modern mathematical result is supported by the checked Fulton and Stacks locators. Neither the machine-produced SGA site nor the separate 24-page placeholder file is used as authority.

## F.3.9 — The transversal dimension on 18:15

**Status: proved dimension correction; reading retained.** Let Y be a smooth codimension-p subvariety of a smooth complex n-fold X at y, and let X′ be a smooth subvariety transverse to Y there. Transversality gives T_yX′+T_yY=T_yX. If the intersection is isolated and transverse, T_yX′∩T_yY=0. Taking dimensions gives dim X′+(n−p)=n, hence dim X′=p. Therefore the frozen label n−p has the ordinary required dimension only when n=2p. This proves the precise mathematical correction in I.P28 while retaining the possibility of an unstated convention and the original label. No archive scan was inspected.

## Exact obligations retained by the audit

The mathematical proofs above do not settle: the unspecified six global realization essential images; the general Hodge-fullness and algebraic-cycle standard-conjecture assertions; unspecified integral-model finiteness with no fixed category or equivalence relation; the incomplete LM6 normalizer predicate; the absent cote-14 singular-hypersurface construction; the missing two entries in the historical A–D dictionary; the literal unexplained “préminimal” symbol; or the arithmetic period gates identified in A.2–A.4. A requested named-conjecture implication in A.2 is classified as an implication proved there, not as the truth of its premise. Cancelled period drafts stay cancelled even when a corrected statement has a modern proof.

The final CSV gives each mathematical assertion its own row; purely documentary assertions are identified as such instead of being silently treated as mathematical theorems.
