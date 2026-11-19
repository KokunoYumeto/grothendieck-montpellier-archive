# Two supplied motivic sources: opened-text checks

Checked 19 November 2026 by GPT-6 Astra Pro (OpenAI), inherited effort, RESEARCH_SA07, agent period_triangle. These two supplied texts are now included explicitly in `supplied_motivic_references.bib` and the merged source/check records. They introduce no new conjectural hypothesis into the unconditional triangle calculation.

## André, Galois theory, motives and transcendental numbers

Opened supplied file: `background/literature/andre_galois_theory_motives_transcendental/andre_galois_theory_motives_transcendental.tex`, especially lines250–360. Also opened https://arxiv.org/pdf/0805.2569, whose header identifies version1, 16May2008. The thirteen-page preprint corresponds to the EMS2009 chapter, pp.165–177; the publisher contents at https://ems.press/books/irma/71/contents gives DOI10.4171/073-1/4 and publication date24September2009.

Exact locators read: sections3.2–3.5, pp.4–6; section3.6, p.7; Conjecture4.1.1 and the following dimensional reformulation, pp.7–8; sections4.2–4.4, pp.8–9. The paper uses the comparison direction

\[
\varpi_M:H_{\mathrm{dR}}(M)\otimes\mathbf C\longrightarrow H_B(M)\otimes\mathbf C.
\]

Our comparison is its inverse: \(\alpha=\varpi_M^{-1}\). For every commutative scalar algebra \(R\), inversion sends a tensor isomorphism \(p:D_R\to V_R\) to the tensor isomorphism \(p^{-1}:V_R\to D_R\), and repeating inversion gives the identity. Matrix inversion is regular on the scheme of invertible matrices, so these maps give inverse morphisms of comparison torsors, not only a bijection of complex points. In particular, the entries of either matrix are rational functions in those of the other with determinant inverted, and the generated fields agree. This checks the exact conversion used in A.1.1–A.1.3 and A.2.4.

The genericity formulation in section4.1 includes connectedness over the ground field, not necessarily geometric connectedness. Our proofs use the component through the actual point after algebraic base extension and explicitly separate image dimension from actual transcendence degree. The elliptic discussion in section4.2 is treated as that source's account, with the original transcendence input checked in the parent elliptic audit.

Section3.3 describes an expected mixed category and discusses numerical motives inside that framework. It is not used to supply an unconditional Betti realization of all numerical motives: F.3.5 proves exactly that such a factorization requires the numerical kernel to act trivially. The paper's general discussion therefore remains background; it does not remove that proved realization condition.

Web locators: `turn734908132view1`, `turn229623994view3`, `turn596980020view5`; publisher metadata `turn734908132view2`.

## Huber–Müller-Stach, On the relation between Nori Motives and Kontsevich Periods

Opened supplied file: `background/literature/huber_mueller_stach_nori_kontsevich/huber_mueller_stach_nori_kontsevich.tex`; its title date is2April2012. Read the introduction and definitions, lines119–158, the rigidity theorem and proof at603–615, the full comparison-algebra argument at628–850, the full torsor argument at857–979, and PropositionC.4 with its proof at1907ff. Also opened https://arxiv.org/pdf/1105.0865; this current PDF identifies version5,21May2014 and retains the title date2April2012.

Exact numbered locators in that PDF:

| Statement | Page | Check |
|---|---:|---|
| Theorem1.14 | 8 | Nori rational motives are rigid and neutral Tannakian; the proof uses the stated perfect-pairing criterion. |
| Theorem2.6 | 10 | Formal diagram symbols identify with the dual comparison space; the explicit finite-dimensional argument is given below. |
| Remark2.9 | 11 | The authors explicitly preserve a question about whether the restricted normal-crossing presentation generates all relations. |
| Theorem2.10; Corollaries2.11–2.12 | 11–12 | The all-pairs formal-period algebra is the comparison algebra; very good pairs suffice; the evaluated algebra has the stated normal-crossing generators. |
| Lemma3.2; Theorem3.3; Corollary3.4 | 12–13 | The comparison algebra represents tensor isomorphisms; inversion identifies the two directions; the formal-period spectrum is a torsor. |
| PropositionC.4 | 28 | Generating perfect pairings yield rigidity under the appendix's specified category/fiber-functor hypotheses. |

Here is a precise check of Theorem2.6, making the linear-algebra quotient in its short proof explicit. For a finite diagram \(F\), put

\[
 E=\bigoplus_{v\in F}\operatorname{Hom}_{\mathbf Q}(T_1(v),T_2(v)),\qquad
 L=\bigoplus_{a:v\to w}\operatorname{Hom}_{\mathbf Q}(T_1(v),T_2(w)).
\]

Define the linear map \(\delta:E\to L\) by
\(\delta((h_v))_a=T_2(a)h_v-h_wT_1(a)\). Then \(\ker\delta=\operatorname{Hom}_F(T_1,T_2)\). Finite-dimensional duality gives

\[
 (\ker\delta)^\vee=E^\vee/\operatorname{im}(\delta^\vee).
\]

The canonical identification \(\operatorname{Hom}(U,V)^\vee\simeq U\otimes V^\vee\) sends \(\omega\otimes\gamma\) to the functional \(h\mapsto\gamma(h\omega)\). Under it, \(\operatorname{im}(\delta^\vee)\) is exactly the span of the diagram's change-of-variables relations. The resulting isomorphism is precisely the displayed \(\Psi\) of Theorem2.6. It is compatible with enlargement of finite diagrams and with tensor products, so passing to the filtered colimit gives the claimed algebra isomorphism. Thus the proof's wording about a subspace satisfying relations is replaced by the exact quotient-duality morphism rather than being silently accepted.

For \(X=\operatorname{Isom}^{\otimes}(T_1,T_2)\), the ternary torsor operation on points is \((a,b,c)\mapsto a\circ b^{-1}\circ c\), a map \(T_1\to T_2\). Its regularity follows from composition and inversion of tensor isomorphisms. This gives the coordinate formula in Remark3.5. Evaluation at the actual comparison point is a homomorphism \(P\to\mathbf C\). Constructing this homomorphism and the torsor does not prove that its kernel vanishes; no injectivity is imported into A.2.

The product pair is typed as \((X\times X', (D\times X')\cup(X\times D'))\), with the second component embedded by the evident product inclusions; the swap isomorphism \(D'\times X\to X\times D'\) supplies the coordinate identification when the displayed source formula uses the reversed product order. This exact identification is needed to read the boundary term as a subvariety of \(X\times X'\).

This check uses Definition2.8, whose second boundary term is printed \(D'\times X\). The introductory Definition0.1 instead repeats \(D\) in its second boundary term; that display alone does not type the product of two arbitrary pairs. The main definition and the stated factor-swap map give the product used here. Likewise, the reference to “Theorems2.6 and2.9” in the proof of Corollary3.4 points to Theorem2.10 for the second theorem, since2.9 is the intervening remark in this version. These local editorial errors do not enter our mathematical proof. The integral extension mentioned in Remark2.7 is not used: the finite-diagram proof written above is over \(\mathbf Q\), where finite-dimensional duality is exact.

Web locators: `turn734908132view0`, `turn596980020view0`–`turn596980020view4`, `turn229623994view1`–`turn229623994view2`.
