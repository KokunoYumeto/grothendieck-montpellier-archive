# F65 — Joint normalization of two actual VIII coefficient types

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting is not exposed. Date: 2026-11-21 UTC.

This is a separate source audit and two conditional arithmetic propositions. It does not alter the frozen named-generator or pure-point reports. The first distinguishes an ambient transition coefficient from a canonical multiplication coefficient. The stronger second uses two actual canonical multiplication constants and requires both to have pure point Euler interpretations. VIII does not state these arithmetic comparisons as theorems or conjectures in the forms used here.

## 1. The source actually changes the parameter

Use u for the parameter in IV's Hecke relation
\[
                  (T_s-u)(T_s+u^{-1})=0.
 \tag{JN1}
\]
The supplied IV TeX uses a macro \u that renders as q. To avoid the papers' reuse of q, write q_src for the parameter of VIII's right-hand Hecke section.

The relation between these conventions is
\[
                         q_{\rm src}=u^2.
 \tag{JN2}
\]

This is supported by explicit convention statements, as well as the displayed calculations:

- IV, Section 3, printed p20, equation (22), source label "e Hecke algebra def", states JN1 and explains that its Hecke parameter agrees with the usual quantum-group parameter. The paragraph distinguishes it from the square-root convention frequently used for Hecke algebras.
- IV, Section 3.1, printed p21, immediately after equation (24), source label "e Kazhdan-Lusztig polynomials", explicitly gives the relation q_KL^{1/2}=u.
- VIII, Section 3, printed p18, immediately after the Wedderburn display (11), source labels scanonicalB and eqweder, says that the role of q in Section 2.2 is played by q^{1/2} in the present section. It then places the rescaled generators in the usual Z[q^{1/2},q^{-1/2}] ambient Hecke form.

The last statement is a change between the quantum-group convention in VIII Section 2 and its right-hand Hecke convention in Section 3. Together with IV's explicit quantum/Hecke matching, it gives JN2 for the corresponding Kronecker example. It does not assign any finite-field Frobenius eigenvalue to either formal parameter.

### Independent check using the actual presentations

Set
\[
 D=(u+u^{-1})^2=q_{\rm src}+2+q_{\rm src}^{-1}.
\]
VIII Section 5.1, printed p28, gives
\[
\begin{aligned}
 c_1&=(q^6+2q^5+3q^4+4q^3+3q^2+2q+1)/q^3,\\
 c_2&=(q^4+q^3+4q^2+q+1)/q^2,\\
 b_1&=-(q^2+1)^2/q^2,\qquad b_2=(q+1)^2/q.
\end{aligned}
\]
With q=q_src these satisfy exactly
\[
 b_2=D,\quad -b_1=(D-2)^2,\quad
 c_1=D(D-2)^2,\quad c_2=D+(D-2)^2.
 \tag{JN3}
\]
The two factors D and (D-2)^2 are the factors in IV Theorem 11.16, printed p65, equations (111)–(112), using the preceding equation (110) and a_1=u+u^{-1}, a_2=D-2. Thus VIII's degree-five coefficients agree with the actual IV presentation under JN2.

The printed repeated b_1 in VIII equation (17) is not used to distinguish the two basis families here. JN3 only uses the unambiguous displayed scalar definitions and the common degree-five expression.

## 2. Two different coefficient types in the source

The following are both printed in VIII's same rank-three Kronecker example.

### Ambient transition coefficient

Figure 1, printed p30, source label fw1w2, contains
\[
                  h(q)=4\,\frac{1+q}{\sqrt q}
                       =4(q^{1/2}+q^{-1/2}).
 \tag{JN4}
\]
It occurs in rows 13 and 18, columns 1 and 3 of the displayed table.

The caption identifies this as a table of coefficients of W1 and W2 in a symmetrized Kazhdan–Lusztig basis. Section 5.1.2, printed p29, explains that the ambient algebra is H3(q) tensor H3(q), and that the symmetrization and order are inherited from IV. There is a printed labeling inconsistency: the next sentence names the first two columns as gamma_1^1 and gamma_12^1, which the preceding cell list places in V1 rather than W1. Nothing here resolves that label inconsistency. Only the unambiguous raw entries and their ambient-transition role are used.

Thus h is an **ambient transition coefficient**, not a canonical multiplication constant. Its raw normalization is part of the hypothesis of the proposition below. No assertion that it must have a geometric Euler interpretation follows just from its appearance in that table.

### Canonical multiplication coefficient

Figure 2, printed p34, source label fmultkron2, gives
\[
 c(q)=c(\gamma_2^1,\gamma_1^1;\gamma_{21}^1)
       =-\frac{(q^2+q+1)(q-1)^2}{q^2}
       =-q^2+q+q^{-1}-q^{-2}.
 \tag{JN5}
\]
Section 5.1.2 distinguishes these multiplicative constants from the preceding transition coefficients. It describes their signed, vanishing-factor positivity in q^{1/2},q^{-1/2}; it does not claim that the raw constants are unsigned effective Laurent characters.

Under JN2,
\[
             c(u^2)=-(u-u^{-1})^2(u^2+1+u^{-2}).
 \tag{JN6}
\]
This is the normalization used for the explicit mixed torus/projective coefficient in F62.

The same Figure 2 also gives the positive multiplication constant
\[
 d(q)=c(\gamma_1^1,\gamma_1^1;\Sigma)
        =\frac{(1+q)^2}{q}=q+2+q^{-1}.
 \tag{JN6a}
\]
It is printed as equal to three other multiplication constants with output Sigma. The exact first triple displayed above is sufficient; no column-label issue from Figure 1 enters this formula.

The source PDF was inspected visually at printed pp18, 30 and 34. The complete surrounding Section 5.1 text on pp28–29 and the complete convention paragraphs in both supplied TeX files were read. The coefficient types above agree with those contexts.

## 3. Finite power-sum uniqueness and the weight constraint

Fix a prime power Q>1, a prime ell not dividing Q, and a finite ell-adic coefficient field E large enough for the finitely many eigenvalues under consideration. Choose embeddings of their algebraic eigenvalues into C, and use the positive real value of Q^a for real rational a.

We use geometric Frobenius. An algebraic eigenvalue of integer Deligne weight m has absolute value Q^{m/2} under the specified complex embedding; ordinary mixed integral-weight cohomology has eigenvalues whose weights are integers. This hypothesis is explicit. Arbitrary finite Weil representations with nonintegral weights are not excluded.

If beta_1,...,beta_s are distinct nonzero complex numbers, the sequences beta_j^n are linearly independent even for all sufficiently large integers n. Indeed, choosing s consecutive such n gives a Vandermonde matrix times an invertible diagonal matrix. Therefore the grouped Euler multiplicity of every visible root is determined by all-extension Euler traces.

For a bounded mixed complex, cancellations may remove some roots. They cannot manufacture a visible root not present in its cohomology. Hence every nonzero root in a proposed Euler trace of an integral-weight mixed complex must itself have an integer weight.

For a pure point complex of one integer weight w, BBD Section 5.1.8 further puts every eigenvalue of point weight m in the unique degree i=m-w. Consequently a fixed root cannot cancel across different degrees. Its nonzero Euler multiplicity has sign (-1)^{m-w}. This does not require arithmetic semisimplicity; Jordan blocks contribute their dimensions to traces.

## 4. Joint-normalization proposition

### Proposition JN-A

Let a be a nonzero rational number. Suppose the same all-extension parameter rule
\[
                         q_{\rm src}=Q^{an}
 \tag{JN7}
\]
is used for both actual source coefficients JN4 and JN5.

Assume:

1. h(Q^{an}) is the Euler trace of a bounded ordinary mixed point complex whose cohomology has integral Deligne weights.
2. c(Q^{an}) is the Euler trace of a bounded pure point complex of one integral weight.

Either trace comparison may be required only for all sufficiently large n. Then these two assumptions are incompatible.

The coefficients need not share a complex, a common weight, a basis, or an operation. The incompatibility already follows from their two scalar trace requirements and the common parameter rule.

### Proof

By JN4,
\[
                h(Q^{an})=4(Q^{a/2})^n+4(Q^{-a/2})^n.
 \tag{JN8}
\]
Since a is nonzero, these are two distinct nonzero roots. Power-sum uniqueness forces both to occur with nonzero grouped Euler multiplicity. Their absolute values have weights a and -a. The first hypothesis therefore forces
\[
                              a\in\mathbb Z.
 \tag{JN9}
\]

By JN5, the other required sequence is
\[
             c(Q^{an})=-(Q^{2a})^n+(Q^a)^n
                            +(Q^{-a})^n-(Q^{-2a})^n.
 \tag{JN10}
\]
Its four roots are distinct because a is nonzero. Their weights are 4a,2a,-2a,-4a. By JN9 all four are even integers. In a pure point complex of weight w their possible cohomological degrees all have parity w. Every nonzero Euler multiplicity must consequently have the same sign (-1)^w. The displayed multiplicities -1,+1,+1,-1 have both signs, contradiction.

Additional invisible eigenvalues cannot repair the contradiction: in a pure point complex each eigenvalue has its unique allowed degree, so opposite-parity cancellation for that eigenvalue is impossible. This proves the proposition. QED.

The excluded a=0 case would give h(1)=8 and c(1)=0, so it is deliberately not included.

### Exact logical scope

This is a **joint arithmetic-comparison obstruction**, not a variable-independent canonical-constants-only statement. The first hypothesis concerns the ambient transition table and the second concerns the canonical multiplication table. VIII does not supply both as ordinary integral-weight geometric Euler comparisons. If the first coefficient is discarded, rescaled, or interpreted in a larger weight category, the argument must be checked again.

For a nonzero integral a, h itself has an ordinary mixed arithmetic realization by four copies of each of the two integral-weight eigenlines. The contradiction concerns making the second raw coefficient pure with that same rule; it is not a failure of all arithmetic coefficient objects.

### Proposition JN-B: two multiplication constants suffice

Let a be a nonzero rational number. Suppose both actual multiplication constants d and c in JN6a and JN5 are, under the common rule q_src=Q^{an}, the Euler traces of bounded pure point complexes of integral weights. The two pure complex weights may be different. Equality for all sufficiently large n is enough. Then these hypotheses are incompatible.

Unlike JN-A, this conclusion makes no assumption about any ambient transition coefficient.

### Proof

The required trace for d is
\[
                     d(Q^{an})=(Q^a)^n+2+(Q^{-a})^n.
 \tag{JN10a}
\]
Its three roots are distinct. If its pure complex weight is w_d, the root 1, of point weight zero, can occur only in degree -w_d. Its positive Euler multiplicity 2 forces this degree even, so w_d is even.

The roots Q^a and Q^{-a} have point weights 2a and -2a. They must have integral weights, and their positive Euler multiplicities force both allowed degrees 2a-w_d and -2a-w_d to be even integers. Since w_d is even, 2a is an even integer, hence a is an integer.

The second coefficient is then exactly in the situation of JN10: its four distinct roots have even integer weights, but their nonzero Euler multiplicities have both signs. No pure point complex of any one integral weight can realize it. This proves JN-B. QED.

This is a stronger raw-canonical-coefficient comparison gate. It still does not refute VIII's signed/factored positivity: that positivity does not assert that both raw constants are pure point Euler traces. In particular mixed or nonproper coefficient constructions, or pure objects whose specified trace comparison is different, are outside the proposition.

As a consequence, a claimed realization of both raw constants by pushforwards of pure objects along proper structure morphisms X -> Spec F_Q, with X a scheme of finite type, would also be excluded if it used this same all-extension parameter rule. BBD 5.1.13–5.1.14, p128, supplies the two weight bounds; properness gives f_!=f_* and dual stability, so the point pushforward is pure. For a proper morphism to a higher-dimensional base, arbitrary stalks of the pure pushforward need not be pure; that situation requires a separate pure-point-extraction hypothesis and is not included here. The stated raw-coefficient comparison remains extra data.

## 5. The isolated half-step normalization escape is real

For the isolated multiplication coefficient, choose a=1/2. Put v=Q^{n/2}; then
\[
 c(v)=-v^2+v+v^{-1}-v^{-2},\qquad
                  -c(-v)=v^2+v+v^{-1}+v^{-2}.
 \tag{JN11}
\]
The pure-point criterion is satisfied with pure complex weight 1.

To construct it explicitly, let L_e be the arithmetic Weil line with geometric Frobenius eigenvalue Q^{e/2}, using the chosen positive square root in a finite extension of Q_ell. Then
\[
           K=L_2[-1]\oplus L_1
                  \oplus L_{-1}[2]\oplus L_{-2}[3]
 \tag{JN12}
\]
is pure of weight 1: its nonzero cohomological degrees are 1,0,-2,-3 and its point weights are respectively 2,1,-1,-2. Its Euler trace is exactly JN11 at every extension degree. These eigenvalues are ell-adic units, so the lines can also be taken as continuous arithmetic Galois representations. No geometric half-Tate motive is claimed.

This does not contradict either proposition. The same rule gives
\[
                         h(Q^{n/2})
                         =4Q^{n/4}+4Q^{-n/4},
\]
whose two roots have weights 1/2 and -1/2. It cannot be the Euler trace of a bounded ordinary mixed integral-weight complex, by the same Vandermonde argument.

Also d(Q^{n/2})=Q^{n/2}+2+Q^{-n/2} is not a pure point Euler trace: its positive constant root forces an even complex weight, whereas its positive roots of point weights 1 and -1 force an odd complex weight. Thus the real isolated c escape does not extend even to the second multiplication constant.

Also, because q_src=u^2, this isolated choice changes the IV quantum parameter to u=Q^{n/4}. It is not the same grading-to-Frobenius comparison as u=Q^{n/2}, q_src=Q^n.

One may of course choose finite Weil eigenlines of these nonintegral weights. That enlarges the arithmetic weight convention and lies outside the ordinary integral-Deligne-weight hypothesis. The report does not claim such finite Weil representations do not exist.

## 6. Separate dictionary

The source parameter statement concerns a formal split-torus grading, whose representation characters are Laurent polynomials in the chosen character. The action vocabulary is SGA 3, I, 4.7.2–3 and cote 90, scan 17; the coefficient representation and effective/virtual language is SGA 6, V, Sections 2–3 and cote 133, scan 18. These frameworks do not assign a Frobenius weight to the formal character and do not identify the two different source coefficient tables. JN-B avoids that cross-table comparison, but still requires pure Euler realizations of both raw multiplication constants.

The point coefficient complexes fit the bounded perfect-complex framework of SGA 6, I, Definition 4.7, pp121–122 and Example 4.8, p122. The integral-weight and pure-complex conventions used in the proof are BBD Sections 5.1.5 and 5.1.8, printed pp125–127; the proper structure-morphism consequence uses BBD 5.1.13–5.1.14, p128, with f_!=f_* and dual stability. No purity of arbitrary stalks on a positive-dimensional base is inferred. The Vandermonde and parity deductions are proved here. No archival text is claimed to supply the extra trace-comparison hypotheses.

No lambda-ring structure on a noncommutative Hecke word algebra, unknown nonstandard scheme-group realization, canonical projector, or perverse coefficient object is inferred from these scalar calculations.

## 7. Source and check record

Supplied TeX sources:

- sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex, Section3 labels "e Hecke algebra def" and "e Kazhdan-Lusztig polynomials"; Theorem label "t S3 coprod relations".
- sources/LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/main.tex, labels scanonicalB, eqweder, sexpkronecker, fw1w2 and fmultkron2.

Primary PDFs:

- https://arxiv.org/pdf/cs/0703110 — IV, version4 locally.
- https://arxiv.org/pdf/0709.0751v2 — VIII, 71 pages. Local PDF SHA256 504345a1ffd36900ba6166df17cb595f335ba7f15be1fe2739318fa0b7fb80be; extracted text SHA256 89368a77d8d81f11889cbb15df40140afe48351b08e4d30b1e3c95b49322da12.

Checks actually performed:

1. Read both full convention paragraphs and matched VIII equation (11) and Figures1/2 to the rendered primary PDF.
2. Read VIII Section5.1 and Section5.1.2 completely; kept ambient and multiplicative coefficients separate.
3. Reconstructed JN3 against the complete actual IV presentation.
4. Proved eventual Vandermonde uniqueness, integer-weight necessity, and pure-degree parity directly.
5. Constructed the isolated a=1/2 pure complex and checked all four degrees and signs.
6. Ran the accompanying exact symbolic certificate verify_joint_normalization_gate.py.
7. Verified the second Figure2 multiplication constant and reconstructed the constant-root/outer-root parity proof of JN-B.

Independent whole-proof review is requested before integration. No root master artifact was edited.

