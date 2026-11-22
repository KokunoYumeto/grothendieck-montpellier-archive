# C.3bt: complete combined proof and primary-source review

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not exposed.

Completed full mathematical read: 19 November2026,18:41UTC; final source/wording receipt saved18:42UTC. **PASS.**

Reviewed complete files:

- `../cycles/SNC_unconditional_edge_kernel_draft.tex`, VE.1–VE.10, including the full marked edge-family construction.
- `C3_unconditional_edge_totalization.tex`, UK.1–UK.7, including the exact remaining quotient.

Authorship distinction: VE is independently audited sibling work. The reviewer supplied the UK totalization fragment and independently reconstructed its argument before typing it; this receipt is not represented as an independent second authorship-free audit of that contribution. Root and Frobenius separately performed complete independent audits of both fragments, and cycles independently read UK. No program or build rerun, nor inspection of an as-yet-unprovided bt-specific certificate, is claimed here.

## 1. Full new marked-family proof

The finite collection of normalized Poincare bundles is placed on one actual proper parameter curve through the identity and the prescribed Picard tuple. Every marked evaluation line bundle has a rational section with divisor disjoint from the two endpoints and with value one in the prescribed identity-fibre trivialization. Curve Riemann–Roch supplies a function with only the prescribed pole, the required nonzero value at the target endpoint, and simple zeros at all finitely many divisor supports and an additional point.

The norm-one cover `(g−1)^2=hg` is irreducible and separable in every characteristic. In odd characteristic its discriminant has an odd valuation at a simple zero of h. In characteristic two, the Artin–Schreier equation `y²+y=1/h` has a simple pole, which cannot occur for a rational Artin–Schreier coboundary. The normalization is therefore a smooth connected proper curve. The zeros and poles of g lie only above the identity endpoint. Above the chosen divisor supports, g equals one, including all ramified points. The target endpoint with g=u exists even when ramified.

On the smooth surface `C_e×P`, frames lifting the fixed trivialization along every zero/pole fibre have transitions `1+z b_ij`. The displayed Dennis–Stein expression

`m⟨z,−b_ij⟩ + {v,1+z b_ij}`

extends `{g,b_ij}` for `g=z^m v`, including negative m. Local regular Gersten injectivity makes these genuine sheaf sections glue and gives the cocycle and frame-change identities. This is local sheaf injectivity, not an asserted global-affine K2 injection. Every boundary specialization is zero by the defining Dennis–Stein word; the target restriction is the usual unit-times-Picard cup.

For a marked point, the normalized rational section of the evaluation line bundle gives the exact Gersten representative supported on its divisor. The zero/pole-fibre comparison contributes no hidden scalar: the section has value one in the prescribed trivialization there. At every remaining support point, g=1, so each point K1 term is zero individually. This proves literal zero in `H¹(P,K2)`, without using a norm or merely zero endpoint values.

The Brown–Gersten lift is correctly made through the **sheaf hypercohomology/Postnikov filtration**, not an unsupported contravariance of the support filtration. On the regular surface the `(1,2)` term has no possible incoming or outgoing differential. Any lift in descent F1 gives the specified H1K2 class. Functorial pullback to each regular horizontal/vertical curve kills F2 because its cohomological dimension is one. Consequently both endpoint and marked K1 restrictions are determined by the displayed sheaf classes, and the lift has no determinant/unit ambiguity. The result is an actual integral K1 family on a fixed proper product in all characteristics.

## 2. Complete totalization implication and exact remaining gate

The canonical geometric closed-cover totalization is retained, including its actual nullhomotopy. At a point parameter, a pure weight-two component tuple has an obstruction with Adams eigenvalue four and zero edge K0 restriction. Exactness puts it in the image of vertex K1(k), of eigenvalue two, so the obstruction is zero rationally. No semisimplicity of the intermediate homotopy group is assumed. Thus the component map is surjective without a dual-complex hypothesis.

For its kernel, the polynomial `(ψ²−2)/2` gives the required weight-two edge vector. The negative energy identity removes the degree-unit part by actual component divisor-times-unit classes, whose canonical totalization boundary is zero. The new marked-family lemma treats the remaining Pic0-times-unit vectors with literal zero restrictions at every triple point. Exactness therefore supplies an actual `π1(T_P)` lift. The difference from any chosen point lift lies in the image of the vertex K2(k) terms; the previously audited proper-curve Milnor-symbol construction kills their double boundaries by actual proper families. A rational K0 weight projector on the product preserves the wanted endpoint class. Arbitrary coherent-lift ambiguity is thus accounted for, not silently discarded.

Combining this with the already proved degree and weighted Albanese reductions gives exactly UK.7: the direct sum of component rational Albanese kernels, divided by the images of `J_K∩S00` and of the exceptional cycle image intersected with S00. The denominator splitting uses the actual Poincare subgroup lying in both relation groups. No assertion is made that all component Albanese kernels lift to globally compatible proper families, or that the resulting quotient vanishes for arbitrary components. Vanishing when every component Albanese kernel is zero is justified.

## 3. Exact primary sources freshly read in this review

- Thomason–Trobaugh1990, full primary Rochester PDF, Sections3.14–3.15 pp317–319; Theorem10.3 and its complete descent proof pp383–386; AppendixD.4–D.5 and full displayed Postnikov proof pp424–426. The latter supplies the sheaf-hypercohomology construction and functoriality used for the horizontal and vertical pullbacks. URL: `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf`.
- Weibel, K-book ChapterIII, Definition5.11 and the complete displayed Dennis–Stein word and identities D1–D3, chapterpp43–44. The sign in VE.6 agrees with the modern convention `⟨r,s⟩={r,1−rs}`. No assumption that two is invertible is used. URL: `https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf`.
- Quillen1973, original full primary scan, Section7 Proposition5.6/5.8 and Theorem5.11 with its complete proof, including Lemma5.12. The regular semilocal finite-type-over-a-field hypotheses apply to all local rings of the smooth surface and curves. URL: `https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf`.

For the reused totalization, Picard-times-units, Adams boundary, energy and proper-symbol inputs, this receipt relies on the exact full primary reads already recorded for C.3bq/C.3br/C.3bs and EL, rather than claiming they were all newly reopened in this one block. No metadata-only page supplies a mathematical input.

## 4. Version and validation limits

The first complete combined text was read before the routine display repairs. The subsequent two UK changes only moved b to a display and shortened the restriction-degree sentence; both were reread. The latest inspected combined draft uses TT AppendixD.4–D.5 explicitly. Own-fragment SHA256 after those repairs: `71f2a345844ee778a73b21c108d8f3b46f7c556847198b7746f3aa10fa21be24`. No mathematical edit is requested.

This is approval of the complete typed proof and the stated sources. Computational and compiled-layout receipts remain separately attributed to their actual owners.
