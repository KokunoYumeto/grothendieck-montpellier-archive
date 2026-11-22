# Supersingular threefolds: finite torsion realization and the actual Hom gap

Owner: `/root/component_families`, 2026-11-19. Status: **proved method limitation and explicit bounded finite-torsion certificate; no main-gate movement**. Neither characteristic-two nor characteristic-three arbitrary supersingular threefolds are settled here. All constructions and arguments concern abelian varieties in the usual category and actual homomorphisms unless a finite group scheme is explicitly named.

## BT.1. Why this was a different route

C.4u and the universal threefold construction leave only the characteristic prime: (s_J(A)\mid2) in characteristic two and (s_J(A)\mid3) in characteristic three. Thus an actual factorization of some multiplication ([n]_A), with (p\nmid n), through a product of Jacobians would finish either case. The new lead was Pries and Ulmer's published theorem that every (BT_1) group scheme occurs as a direct factor of a Jacobian's (p)-torsion, with the curve defined over the prime field (Pries & Ulmer, 2022, Theorem 1.1). The full published thirteen-page article and every displayed proof have now been read.

That theorem has exactly the required finite group scheme direction, including the small characteristics. Its conclusion does not assert that the two splitting maps are restrictions of homomorphisms of abelian varieties. The following argument proves that a uniform lift of its constant-curve construction would be false, even for explicit supersingular threefolds. This is stronger than merely leaving the lifting step unproved, but it is only a limitation on this construction.

## BT.2. An elementary descent lemma for an actual prime-to-characteristic factorization

Let (k_0\subset k) be algebraically closed fields of characteristic (p>0). Call an abelian variety over (k) **constant** here if it is isomorphic, as an abelian variety, to a base change from (k_0).

**Lemma.** Suppose (B=B_0\times_{k_0}k) and there are homomorphisms

\[
 A\xrightarrow{u}B\xrightarrow{v}A,
 \qquad vu=[n]_A,
 \qquad p\nmid n.
\]

Then (A) is constant. No principal polarization or supersingularity assumption is required.

**Proof.** First, homomorphisms between constant abelian varieties do not enlarge under extension of algebraically closed fields. Here is a proof at the exact scope needed, rather than an appeal to a general trace construction. Spread a homomorphism (f:(B_0)_k\to(D_0)_k) and its group identities over an integral finite type (k_0)-scheme (T), after shrinking. Choose (t_0\in T(k_0)). The difference (f-f_{t_0}), viewed as a map (B_0\times T\to D_0), is zero on (B_0\times\{t_0\}) and on (\{0\}\times T). The proper-source rigidity theorem makes it identically zero. Thus (f) descends. The rigidity theorem and its complete proof were freshly reread in Milne (2008, I, Theorem 1.1, pp. 8–9); the equivalent Hom conclusion and complete displayed proof also appear in I, Corollary 16.4, p. 68. Spreading handles arbitrary algebraically closed extensions, not only a finitely generated one.

The endomorphism (uv\in\operatorname{End}(B)) therefore descends to an endomorphism (w_0) of (B_0). Since (vu=[n]), the map (v) is surjective and (u) has finite kernel. Consequently

\[
 C:=u(A)=\operatorname{im}(uv)
      =(\operatorname{im}w_0)_k.
\]

Write (C=C_0\times k). The restriction (v_C:C\to A) is an isogeny, and

\[
 v_Cu=[n]_A,
 \qquad uv_C=[n]_C.
\]

The second equality follows after precomposing with the surjection (u:A\to C). It implies (\ker v_C\subset C[n]). Since (p\nmid n), (C_0[n]) is a finite étale constant group scheme over the algebraically closed field (k_0). Every closed subgroup scheme of its base change descends: it is the union of a subset of its constant reduced points, and the subgroup condition is preserved. Let (H_0\subset C_0[n]) be this descended subgroup. Then

\[
 A\simeq C/\ker v_C\simeq(C_0/H_0)_k.
\]

This proves the lemma. The finite-subgroup quotient and the complementary isogeny use the usual scheme kernels, not merely rational points; compare Milne (2008, I, Remark 8.6 and the discussion following the construction of the quotient in §8). In the final step the subgroup is étale, so descent by reduced points is valid. \(\square\)

The argument allows any finite product of constant Jacobians, any choices of curves, and any signed sum of composites: a finite sum can be combined into a single factorization through their product. It does not require a fixed genus or a fixed Fermat degree.

## BT.3. Even a lifted retraction only on (A[p]) would suffice—and is excluded for nonconstant (A)

Suppose actual homomorphisms (u:A\to B) and (v:B\to A) restrict to a retraction on finite group schemes:

\[
 (vu)|_{A[p]}=1_{A[p]}.
\]

Then (e=vu) is an isogeny of degree prime to (p). Indeed its kernel has trivial intersection with (A[p]). If its reduced identity component had positive dimension, it would be a positive-dimensional abelian subvariety and would have nonzero (p)-torsion, a contradiction. Thus the kernel is finite. A nonzero finite commutative (p)-primary group scheme has nonzero kernel under multiplication by (p), so the kernel's (p)-primary part is zero. This proves the degree assertion. This reasoning does not confuse étaleness alone with prime-to-(p) degree.

Put (m=\deg e). The finite kernel is killed by (m), so the quotient property gives an actual homomorphism (h:A\to A) satisfying (he=[m]_A). Consequently

\[
 A\xrightarrow{u}B\xrightarrow{hv}A
 \quad\text{has composite }[m]_A,
 \qquad p\nmid m.
\]

If (B) is constant, BT.2 forces (A) to be constant. Thus for a nonconstant (A), **no retraction of (A[p]) inside the (p)-torsion of a constant abelian variety can be induced by a pair of actual homomorphisms**. The statement excludes all such pairs, rather than just one chosen finite-level splitting.

For the C.4u residual threefold problem, a lifted (p)-torsion retraction through a product of arbitrary Jacobians would prove (s_J(A)=1) by combining (m) with the existing (p)-power bound. This is an exact observation about what a lift would accomplish; it is not counted as a smaller existence gate or as progress on the missing lift.

## BT.4. Explicit supersingular threefolds witnessing the lifting failure

Fix (p=2) or (p=3), put (k_0=\overline{\mathbf F}_p), and let (k=\overline{k_0(t)}), where (t) is transcendental. Choose a supersingular elliptic curve (E/k_0) and a fixed (k_0)-isomorphism (\ker(F_{E/k_0})\simeq\alpha_p). Inside 

\[
 \ker(F_{E^3/k_0})_k\simeq\alpha_p^3
\]

take the closed subgroup

\[
 H_t=\{(z,tz,t^2z):z\in\alpha_p\}.
\]

The first coordinate makes this a closed immersion. Define the abelian threefold

\[
 A_t=E_k^3/H_t.
\]

It is supersingular because the quotient map is an isogeny from (E^3). It is not constant: if (A_t\simeq(A_0)_k), composing this isomorphism with the quotient map gives a homomorphism between constant abelian varieties, hence one defined over (k_0) by the rigidity argument in BT.2. Its scheme kernel would then descend to (k_0). But the tangent line of (H_t\subset\alpha_p^3) is 

\[
 k(1,t,t^2)\subset k^3.
\]

A line of this form defined over (k_0) would have (t\in k_0), by normalizing its first coordinate to one. This contradicts transcendence. Equivalently, in the coordinate Hopf algebra of (\alpha_p^3), the subgroup has ideal generated by (x_2-tx_1) and (x_3-t^2x_1); its degree-one relations do not descend.

It follows from BT.2–BT.3 that (A_t) admits neither a prime-to-(p) multiplication factorization nor an actual Hom lift of a (p)-torsion retraction through any product of constant Jacobians. Nevertheless Pries–Ulmer applies to (A_t[p]). The example therefore identifies the exact missing geometric information in this route. **It does not prove that (A_t) fails to be a direct summand of a product of Jacobians over (k)**, since such Jacobians may themselves be nonconstant.

The general (E^g/\alpha_p) construction is standard and also occurs in the already examined Jiang–Li–Lu argument in the other strand; no new claim about nonselfduality is made here. The descent proof above is independent of their nonselfduality theorem and does not require any a-number calculation.

## BT.5. A bounded, checked constant product already contains every possible threefold (p)-torsion type

There is no need to infer the finite-level existence from an unbounded search. For (d) prime to (p), let (C_d/\mathbf F_p) denote the smooth projective curve with affine equation

\[
 y^d=x(1-x).
\]

Using the word construction in Pries–Ulmer (2022, §§3–5 and Proposition 6.1(1)), form

\[
 B_p=\prod_{\lambda=2}^{6}
       J(C_{p^\lambda-1})^{\lfloor6/\lambda\rfloor}.
\]

Then (A[p]) is a direct factor of (B_p[p]) for every supersingular abelian threefold (A/k), for both (p=2,3). To see this, supersingularity implies that (A[p]) has neither an étale nor a multiplicative direct factor. In the Kraft classification every indecomposable factor therefore corresponds to a primitive cyclic word in (f,v) of length at least two, and the sum of all lengths is six. A factor of length (\lambda) occurs in (J(C_{p^\lambda-1})[p]), and its multiplicity in (A[p]) is at most (\lfloor6/\lambda\rfloor). Distinct words occur as distinct orbit summands, so those copies suffice simultaneously. This uses only the primitive-word statement, which has no (p>3) restriction. It does not incorrectly apply the nonprimitive-word part of Proposition 6.1 in characteristics two and three.

The genus is (\lfloor(d-1)/2\rfloor). Thus

\[
 \dim B_2=3\cdot1+2\cdot3+7+15+31=62,
 \qquad
 \dim B_3=3\cdot3+2\cdot12+39+120+363=555.
\]

The independent bounded program `code/check_bt1_height6_fermat.py` enumerates all primitive cyclic binary words of lengths two through six and verifies the complete integer base-(p) digit/orbit construction for (p=2,3). The counts are (1,2,3,6,9). It enumerates all sixteen local-local multisets of total height six and checks their required multiplicities. Exactly six have dimension and codimension three:

\[
 (fv)^3,\quad fv\oplus ffvv,\quad ffv\oplus fvv,
 \quad fffvvv,\quad ffvfvv,\quad ffvvfv.
\]

Here a word is a cyclic word, and the superscript in ((fv)^3) means three factors. These six are a covering list of balanced local-local (BT_1) types; **no assertion that every one is realized by a supersingular threefold is needed or made**.

Full words, all sixteen multisets, base-(p) representatives, and every orbit are retained in `output/bt1_height6_fermat.json`; the concise output is `output/bt1_height6_fermat.out`. Successful run: **2026-11-19 20:26:26.696167–20:26:26.697045 UTC**, measured runtime **0.0008756179959164001 seconds**, exit zero. This is a finite combinatorial certificate, not a computational proof of rigidity, quotient existence, or a geometric Hom lift. There was no failed run of this script.

**Word-order convention, independently flagged by the Frobenius peer.** The program's `actual_word` follows the orbit in the order $u_0u_1\cdots u_{\lambda-1}$. Pries–Ulmer §4.2 instead labels its associated word $w_a=u_{\lambda-1}\cdots u_1u_0$. These conventions differ by reversal, not necessarily by a cyclic rotation; in length six the asymmetric necklaces can therefore exchange labels. Reversal is a bijection on the entire set of primitive cyclic words of each length. Since this certificate includes every such word with the uniform capacity $\lfloor6/\lambda\rfloor$, the covering assertion, multiplicities, product dimensions, and proof remain unchanged. The retained JSON is interpreted in its explicitly stated forward convention; it is not claimed to use Pries–Ulmer's reversed label literally.

## BT.6. Other current-source checks and the precise scope limits

**Karemaker–Yobuko–Yu.** The published repository PDF returned HTTP403. The complete author v2, arXiv:2002.10960v2 (27 August2021 header; internal date30August2021), was acquired. I read the introduction and Theorems A–C, Definition3.14, Proposition3.15 including its reference-only proof, and Proposition3.16 with the full displayed proof, together with Remark3.17 and its counterexample. The flag-type and minimal-isogeny statements there explicitly start with a principally polarized threefold. They do not prove principal polarizability, prime-to-(p) principalization, or actual Jacobian splitting for an arbitrary supersingular threefold. Theorem-level promotion from those statements was rejected. I also saw an incidental extract from pp.24–26, including the end of the d-invariant argument, Remark5.15, Definition5.16, Lemma5.17 and its proof, Corollary5.18 and its proof, Lemma5.19, and the beginning of Corollary5.20; none is an input here. The dependent Li–Oort theory was not freshly audited in full.

**Viehmann2026.** The actual retrieved version is arXiv:2603.06033v2, **29 May2026**, twenty pages. I read the abstract/introduction, the initial polarized moduli formulation, and the complete §5 on pp.19–20, including Theorem5.1, Proposition5.3, Claim5.4, and the entire displayed proof by comparison with earlier sections. Crucially, §5 begins with **(g\ge4)**. Its conclusion concerns finite-order automorphisms of generic unpolarized (p)-divisible groups, not principalization or Jacobian factors; its threefold polarized background does not alter that. The proofs in §§3–4 on which the §5 comparison depends were not fully rederived or read in full, and this preprint supplies no theorem used in BT.2–BT.5.

**Pries–Ulmer2022.** Fresh complete published offprint, pp.525–537, all §§1–6 and every displayed proof read, including both small-characteristic cases in Theorem6.4 and §6.3. The prerequisite Kraft classification, Oda comparison, and Oort polarization theorem are correctly identified as the paper's inputs; their original complete proofs were not newly opened. For the supersingular application, the ordinary-factor supplement in §6.3 is unnecessary. The degree-prime-to-(p) maps between the explicitly constructed curves in §6 give genuine maps between their Jacobians; they do **not** give maps from the prescribed (A). No inference to such maps has been made.

**Milne2008.** Fresh complete reread of I.Theorem1.1 and Corollary1.2 with their proofs, pp.8–9; I.Propositions16.1–16.3 and Corollary16.4 with every displayed proof, pp.67–68; and I.Remark8.6. Proposition16.1 itself refers to Mumford's GIT for its proof; that separate proof was not opened. BT.2 instead uses the product rigidity theorem whose proof is fully present and read. The finite-type spreading and finite-subgroup quotient facts are standard foundational inputs, not asserted to have been rederived from the foundations of schemes.

## BT.7. Acquisition, failed access, and bibliography

Measured acquisition records are in `output/supersingular_bt1_sources_acquisition.json` and `output/bt1_source_retry_acquisition.json`, with the corresponding retained programs in `code/`. The first batch ran **20:23:12.242321–20:23:28.975630UTC**, wall runtime **16.733315614001185seconds**. It acquired Viehmann v2, Karemaker–Yobuko–Yu v2, and the Hatcher chapter used in the earlier Kummer support proof. The old Arizona Ulmer URL redirected to a homepage and was rejected as non-PDF. Milne's URL returned HTTP406 in that batch. The retained retry ran **20:24:13.969148–20:24:26.307078UTC**, runtime **12.337922614999115seconds**, and acquired the published Pries–Ulmer PDF from the author's current linked GitHub site and Milne's version2.0 notes with a normal browser user agent. Failed attempts remain in the original manifest.

Additional web failures: Karemaker–Yobuko–Yu's Utrecht published-PDF URL returned403; the Pries–Ulmer DOI URL was inaccessible to web retrieval; the old Arizona web link redirected to an inaccessible archive; the NSF PDF mirror returned502. The current author link was obtained by opening the author's research page and following its actual local-version link. None of the failed responses counts as source reading.

Source SHA256 values:

- Pries–Ulmer published PDF: `52ece38056d1720fa0ceebe83b3312177eeda136cd2eaf9a4a6778ded9ec5cd4` (246779bytes).
- Milne version2.0 PDF: `f5ca4e63e5092a4b102daad1470e4cbed5fe8f82115e3a28c8881e3f67f6aaef` (1291594bytes).
- Viehmann v2 PDF: `95ce8e9367e4bd8ac35828547c73164061a8834d36afdef41af079f8739f8cb6` (400471bytes).
- Karemaker–Yobuko–Yu v2 PDF: `8aff5ca9230ad3c60e2b26be0545d5626c02301a67340cb015e573eabb2fc3ae` (503717bytes).
- Hatcher chapter3 PDF, retained for the earlier KI support argument: `3fe35aae9c2bddc3720a86460e0d6bb6fd7dae3489f145f5475c3b4e71f6b793` (1292366bytes). The new download is not an additional claim of reading beyond that earlier exact scope.

APA references and exact opened versions are also in `C4_SUPERSINGULAR_BT1_references.bib`. The already existing Milne key `D_Milne2008KummerBridge` is reused, with this new read scope recorded here rather than duplicated.

Karemaker, V., Yobuko, F., & Yu, C.-F. (2021). Mass formula and Oort's conjecture for supersingular abelian threefolds. *Advances in Mathematics, 386*,107812. https://doi.org/10.1016/j.aim.2021.107812. Opened proof locators refer to https://arxiv.org/pdf/2002.10960v2.

Milne, J.S. (2008). *Abelian varieties* (Version2.0). https://www.jmilne.org/math/CourseNotes/AV.pdf.

Pries, R., & Ulmer, D. (2022). Every (BT_1) group scheme appears in a Jacobian. *Proceedings of the American Mathematical Society,150*(2),525–537. https://doi.org/10.1090/proc/15681. Opened published offprint: https://dlulmer.github.io/research/papers/2021c.pdf.

Viehmann, E. (2026). *Oort's conjecture on automorphisms of generic supersingular abelian varieties* (arXiv:2603.06033v2). https://arxiv.org/pdf/2603.06033v2.

## BT.8. Remaining mathematical task

The finite torsion realization supplies no actual homomorphism with composite prime to (p) for the remaining threefolds. BT.2–BT.4 prove that the constant-curve version cannot do so uniformly. To proceed by finite torsion one needs a Jacobian varying with (A), together with actual incoming and outgoing homomorphisms inducing a retraction; alternatively one needs a different integral cycle construction. Neither is proved here. The complex type-((1,2)) surface gate and the arbitrary supersingular threefold gates in characteristics two and three remain unchanged.

## BT.9. The proposed principally polarized fourfold bridge is also obstructed for this explicit family

During this continuation root proposed testing whether a supersingular threefold in characteristic three could be a factor of a principally polarized fourfold up to an integer prime to three; a subsequent Prym construction with only powers of two as denominators could then be useful. The following complete argument excludes that bridge for the same (A_t). It does not assume or audit any universal Prym theorem.

**Constant-complement lemma.** For every constant abelian variety (C=(C_0)_k), the product (X=A_t\times C) has no polarization of degree prime to (p). In fact (X\to X^\vee) has no isogeny of degree prime to (p).

**Proof.** Let (D=E^3\times C_0), and let

\[
 q:D_k\longrightarrow X
\]

be the quotient by (H_t\times0). Its degree is (p). If (\lambda:X\to X^\vee) were an isogeny of degree prime to (p), then

\[
 h=q^\vee\lambda q:D_k\longrightarrow D_k^\vee
\]

would be an isogeny with (v_p(\deg h)=2). Both its source and target are constant, so BT.2's Hom rigidity argument makes (h) a homomorphism defined over (k_0).

Take the differential of $h$ on the three elliptic factors. Its three columns $b_1,b_2,b_3$ lie in the $k_0$-vector space $\operatorname{Lie}(D^\vee)$. Since $h$ kills $H_t\times0$,

\[
 b_1+t b_2+t^2b_3=0\quad\text{in }\operatorname{Lie}(D^\vee)\otimes_{k_0}k.
\]

The elements $1,t,t^2$ are linearly independent over $k_0$, hence all three derivative columns vanish. We now justify the required group-scheme conclusion by an elementary formal-coordinate argument, so a full height-one classification theorem is unnecessary.

Let $f:\alpha_p\to G$ be a homomorphism to a smooth algebraic group with $df=0$. Choose formal coordinates at its identity. Each coordinate of $f$ is a polynomial in $z$ modulo $z^p$ with zero constant and linear coefficient. If $f$ is nonzero, let $m$ be the least degree with a nonzero coefficient in some coordinate, and write that coefficient as $c\ne0$. Then $2\le m<p$. The identity $f(z+w)=F_G(f(z),f(w))$ holds in $k[z,w]/(z^p,w^p)$. On the left, the coefficient of $z w^{m-1}$ of total degree $m$ is $mc\ne0$. On the right, the linear part of the formal group law contributes only pure powers in $z$ or $w$, and every nonlinear term has total degree at least $2m$. This is a contradiction. For $p=2$, zero constant and linear coefficients already make every coordinate zero. Thus $df=0$ forces $f=0$ in every characteristic under consideration.

Apply this to the restriction of $h$ to each of the three coordinate copies of $\alpha_p$. Each restriction is zero. Since $h$ is a group homomorphism, it is zero on their product. Consequently $\alpha_p^3\times0\subset\ker h$ as a subgroup scheme. Its order is $p^3$. Factoring the isogeny by this finite subgroup shows $p^3\mid\deg h$, contrary to $v_p(\deg h)=2$. $\square$

This argument concerns the scheme maps throughout; checking only the geometric points of $\alpha_p^3$, which all equal the identity, would prove nothing. An earlier version of this paragraph cited standard height-one Lie faithfulness; the explicit formal-coordinate proof above supplies precisely the needed special case without leaving that step as an external assumption.

**Elliptic-complement corollary.** The product (A_t\times L) has no polarization of degree prime to (p) for any elliptic curve (L/k).

If (L) is supersingular, it is defined over (\overline{\mathbf F}_p) up to isomorphism, so the lemma applies. If (L) is ordinary, there are no nonzero homomorphisms between (L) or (L^\vee) and (A_t) or (A_t^\vee): the latter are isogenous to powers of a supersingular elliptic curve, whereas ordinary and supersingular elliptic curves cannot be isogenous. Every homomorphism

\[
 A_t\times L\longrightarrow A_t^\vee\times L^\vee
\]

is consequently block diagonal. A polarization of degree prime to (p) would restrict to a polarization on (A_t) of degree prime to (p), contradicting the lemma with zero-dimensional complement.

**Actual fourfold-factor corollary.** There do not exist a principally polarized abelian fourfold (B/k), actual homomorphisms (u:A_t\to B), (v:B\to A_t), and an integer (n) prime to (p) such that (vu=[n]_{A_t}).

Indeed (u) has finite kernel and (v) is surjective. Put (L=(\ker v)^0_{\mathrm{red}}), an elliptic abelian subvariety of (B). The addition map

\[
 a:A_t\times L\longrightarrow B,
 \qquad (x,y)\longmapsto u(x)+y
\]

is an isogeny. Its kernel projects injectively to (A_t[n]): if (u(x)+y=0), applying (v) gives (nx=0), and (y) is determined by (x). Hence the kernel is a finite étale group of order prime to (p), and (\deg a) is prime to (p). Pulling a principal polarization back along (a) gives a polarization of (A_t\times L) of degree ((\deg a)^2), contradicting the preceding corollary. This rules out the precise prime-to-three fourfold bridge, without confusing an isogeny decomposition with an actual product decomposition.

**Scope.** The lemma is an additional construction exclusion, not a counterexample to Question2. Larger **nonconstant** complements, and products of nonconstant Jacobians of arbitrary dimensions, are not covered. The p-adic degree obstruction is the same elementary mechanism as the already known nonselfduality examples, now applied to the particular fourfold bridge; it is not counted as a fresh main theorem or a strict reduction of the main gate.

**Supplementary bounded certificate.** `code/check_alpha_p_constant_complement.py` retains the full coefficient-extraction matrices for (M(1,t,t^2)^\mathsf T), for (p=2,3) and complement dimensions zero and one. Their ranks are respectively9,12,9,12. It lists the monomial bases of the truncated coordinate Hopf algebras of (\alpha_p^3), with dimensions (p^3), and checks the conflicting degree valuations2 and at least3. Full output: `output/alpha_p_constant_complement.json`; summary: the same stem with `.out`. Successful run **20:32:42.575458–20:32:42.576001UTC**, runtime **0.0005373790045268834seconds**, exit zero. This verifies the bounded symbolic arithmetic only. In particular it does not replace the height-one group-scheme faithfulness, Hom rigidity, or isogeny arguments above. No failed run occurred.

## BT.10. Final source and proof-scope supplement

After the initial BT.9 proof, I freshly opened Milne's complete author PDF *Algebraic groups: The theory of group schemes of finite type over a field*, labelled as published by Cambridge University Press in2022 (659PDF pages, corrected header5October2021), at https://www.jmilne.org/math/Books/iAG2022.pdf. Fresh exact read scope: Proposition11.32 and Corollary11.33 with their entire displayed proofs on printedp.221; all of §11h, printedpp.221–223, including the construction of the restricted enveloping Hopf algebra and Propositions11.34–11.37 and Corollary11.38, with their full displayed proofs. The proof sketches refer to Demazure–Gabriel for additional details; that original source was not opened. The preceding tail of the finite-group order argument and the following Verschiebung discussion through Proposition11.40/Corollary11.41 were also present in the opened extract and read, but are not new inputs. No claim of reading the entire659-page book is made.

The existing bibliography key `rootMilneAlgebraicGroups2022` is reused; its earlier root scope is distinct from this owner's new scope. This is a web-opened source, not a newly downloaded local PDF. Milne's Proposition11.32 directly confirms the finite-group order fact used in BT.3. The general height-one equivalence is a useful check, but the final BT.9 proof uses the fully written elementary formal-coordinate argument instead. Thus the source scope has expanded while the proof's external dependency has become smaller.

Milne, J.S. (2022). *Algebraic groups: The theory of group schemes of finite type over a field*. Cambridge University Press. https://www.jmilne.org/math/Books/iAG2022.pdf.

A further possible stabilization approach was considered but not promoted: a proof that the full (p)-divisible group of (A_t) is indecomposable and not self-dual, together with an integral Hom comparison and an applicable Krull–Schmidt argument, might exclude nonconstant surface complements as well. The required module identification and comparison were not proved in this continuation. The actual argument in BT.9 stops at elliptic complements; it supplies neither a theorem about all larger complements nor a main-gate result. Similarly, a finite-level classification of all (A[p]) types cannot replace those missing full (p)-divisible-group and actual Hom statements.

## BT.11. Surface-complement extension considered at the checkpoint: not promoted

A different possible extension would use an explicit degree-$p$ presentation of a nonconstant supersingular abelian surface $C$ as $E^2/H_s$, with $H_s$ the line $(1,s)$ in $\alpha_p^2$ and $s\notin k_0$. Conditional on that presentation, the degree obstruction is immediate: the quotient $E^5\to A_t\times C$ has degree $p^2$. A prime-to-$p$ isogeny to the dual would pull back to a constant isogeny of degree valuation four. The independent coefficient comparisons $b_1+t b_2+t^2b_3=0$ and $c_1+s c_2=0$, followed by BT.9's elementary formal-coordinate lemma, would force its kernel to contain $\alpha_p^5$, whose order has valuation five. Constant surface complements are already covered by BT.9.

For a nonsupersingular surface complement, a further argument was only sketched: if it has no supersingular elliptic factor, Hom orthogonality should make the relevant homomorphism block diagonal. If it has such a factor, Poincare reducibility gives an elliptic complement, which must be ordinary; the intersection has no nontrivial $p$-primary subgroup because supersingular elliptic $p$-power torsion is local-local while ordinary elliptic $p$-power torsion is a product of multiplicative and etale groups. This should give a prime-to-$p$ product isogeny and reduce to BT.9. The exact presentation, classification dependencies, and full subgroup comparison were not audited to the required primary-proof standard before the source freeze. **No theorem excluding all surface complements or principally polarized fivefold factors is claimed here.** This remains a conditional proof attempt and supplies no main-gate movement.

Fresh opened source: Ibukiyama (2020), *Principal polarizations of supersingular abelian surfaces*, published twenty-page PDF at https://www.jstage.jst.go.jp/article/jmath/72/4/72_1161/_pdf. Exact scope: introduction, printed pp.1161–1163, including Theorems1.1–1.2 as statements; beginning of §2, including the quoted degree-$p$ quotient classification attributed to Oort, Lemma2.1 as a statement, and the beginning of the quaternion description. The complete original Oort proof and the full proofs of Ibukiyama's theorems were **not** opened. The PDF was opened on the web, not downloaded locally. Its quoted classification is suggestive evidence for the missing input and is not recorded as a newly verified complete proof.

Ibukiyama, T. (2020). Principal polarizations of supersingular abelian surfaces. *Journal of the Mathematical Society of Japan, 72*(4), 1161–1180. https://doi.org/10.2969/jmsj/82528252.
