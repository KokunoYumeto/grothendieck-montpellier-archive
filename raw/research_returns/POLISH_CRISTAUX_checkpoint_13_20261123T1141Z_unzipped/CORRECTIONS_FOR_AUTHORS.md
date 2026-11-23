# Corrections for authors

Typographical and notation corrections verified from primary page images are recorded below. Substantive theorem corrections require exact source locators, a complete counterexample or proof, and an explicit literature check. Known published corrections (for example Zheng's treatment of earlier Raynaud-surface claims) are to be cited as background, not presented as a new discovery here.

## Internal corrections kept separate

1. The initial shorthand for the third-index interval suppresses the source's hypothesis p not dividing e.
2. An intake's description of e=216 as the first full-27-torsion case conflicts with its quoted criterion; that criterion allows e=162 and excludes every smaller permitted e. This is conditional arithmetic checking of the criterion, not yet a complete verification of its existence proof.
3. PDF-image and archive handwritten page numbers for cote 4 differ by one: the text of §8.3 starts on PDF image 4, archive sheet 3, and continues on image 5, sheet 4.

## Rains–Sam (2019), Remark5.8: typographical sign

Rains, E. M., & Sam, S. V. (2019). Vector bundles on genus2 curves and trivectors. Algebraic Geometry,6(3),328–345. DOI10.14231/AG-2019-016. Primary PDF: https://content.algebraicgeometry.nl/2019-3/2019-3-016.pdf. SHA256 f2690f05ded12faeb11dacf36ba8e1a755c808bf5f46cda04cc8c8bd637b6439.

Remark5.8, printedp342, PDF15, first establishes f16(pi(gamma))=Pf(Q(pi(gamma)))^2. Its next paragraph says that the first quantity vanishes if and only if the Pfaffian is nonzero. The inequality must be equality: over a field z^2=0 if and only if z=0. Both the reporting worker and root viewed the page image; the sign is present in the published image and is not OCR error. This is a typographical correction only, not a refutation of Theorem5.1. It stays outside the research papers. No author was contacted. Root confirmation recorded 2026-11-23T03:47:44.312686+00:00.

## Dimca–Greuel (2018), p. 115: ambient-ring notation

Dimca, A., & Greuel, G.-M. (2018). On 1-forms on isolated complete intersection curve singularities. Journal of Singularities, 18, 114–118. Primary PDF: https://www.journalofsingularities.com/volume18/dimca-greuel.pdf. SHA256 522f9549da5fa09d00cfdf268d8f9df3cb94f7f0bdbb5037984d40759f499bbc.

Page 114 defines O as the local ring of the curve. In the plane-curve paragraph immediately before Theorem 1.1 on p. 115, the displayed descriptions of the Milnor and Tjurina numbers must instead use the ambient regular local ring C{x,y}: mu=dim C{x,y}/(f_x,f_y) and tau=dim C{x,y}/(f,f_x,f_y). If O were read literally as the already-quotiented curve ring, the two expressions would coincide. The intended ambient-ring convention is explicit again in Section 4. This is a notation clarification only; the theorem and the local formulas used here are unaffected. Root visually checked the original p. 115 image and read the complete mathematical text, pp. 114–118. No author was contacted.

## Bhatt (2012), Construction 4.7: target of the presentation map

Bhatt, B. (2012). Completions and derived de Rham cohomology (arXiv:1207.6193v1). https://arxiv.org/abs/1207.6193. PDF SHA256 f885f25d6fdf475c5e96328a331c40b5798cb0b657a34245c8634c594f443e58.

In Construction 4.7, printed/PDF p. 8, after choosing a polynomial A-algebra presentation F→B, the ideal for completion is printed as ker(F→A). The target must be B: the construction completes the polynomial ambient ring along the presented quotient. The proof of Theorem 4.10 and the surrounding construction use precisely F→B. Root visually verified the original page, so this is not an extraction error. This is a typographical correction to the public preprint, with no effect on the comparison theorem. No author was contacted.

## Grammatica (2026), Remark 4.6: algebraically closed hypothesis

Root adopted 2026-11-23T06:53:12.134374+00:00 after reading the primary passage and original page image. This is a correction of the last two perfect-field conclusions only; the algebraically closed comparison used in this work is unaffected. No author has been contacted.

Livia Grammatica, *Some applications of the Nygaard filtration and quasisyntomic descent in positive characteristic*, arXiv:2507.08568v2, revised 31 October 2026, PDF dated 3 November 2026. Original PDF: https://arxiv.org/pdf/2507.08568v2 . Local primary file: external/papers3_4/grammatica2026.pdf . SHA256: 302ac0456845cf7fc61026db518e7e110f84bb5ed2ae85b419e7e652cb6ffd27 . Exact passage: Remark 4.6, printed/PDF p. 29, final two assertions. A rendered original page is external/infinitesimal_etale/grammatica_p29.png.

### Nearby context and the precise issue

The proof of Theorem 1.1 immediately above the remark assumes k algebraically closed. Remark 4.6 starts again with a smooth scheme over a perfect field k and defines RΓ_et(X,Z_p) as R lim_n RΓ_et(X,Z/p^n). Its exact triangle uses F−1 on crystalline cohomology. The last two assertions then give a fixed-point isomorphism for proper X over the perfect field and identify its W(k)-scalar extension with the unit-root submodule. As literally scoped to an arbitrary perfect field, those last assertions are false. The issue is the omitted preceding-degree cokernel of F−1, and the fact that a unit-root F-crystal over a general perfect field need not have a full basis of F-fixed vectors.

### Complete counterexample

Take k=F_p and X=Spec(F_p), which is smooth and proper over k. Its absolute Galois group is the inverse limit of the cyclic groups Gal(F_(p^m)/F_p), hence the procyclic group Z-hat, generated topologically by Frobenius. For the trivial finite module Z/p^n, degree-one continuous cohomology is
H_et^1(X,Z/p^n)=Hom_cont(Z-hat,Z/p^n)=Z/p^n.
The coefficient transition maps are the usual surjections. Also H_et^0(X,Z/p^n)=Z/p^n with surjective transitions. Thus the derived-limit correction in degree one is zero and
H_et^1(X,Z_p)=Z_p.
The étale/Galois identification is Stacks, §59.59, Lemmas 59.59.1–59.59.2, Tag 03QQ.

The smooth lift of this point is Spec(Z_p). Its relative de Rham complex over Z_p is Z_p in degree zero. The crystalline Poincaré comparison therefore gives RΓ_crys(X/Z_p)=Z_p[0]; its Frobenius is the identity because W(F_p)=Z_p. In particular H_crys^1(X/W(k))=0. The fixed-point isomorphism in degree one would identify Z_p with zero. The asserted scalar-extension description fails at the same degree, because its left side is Z_p while the unit-root part of H_crys^1 is zero.

### Correct general consequence and minimal repair

The exact triangle stated earlier in the remark yields, over a general perfect field, the natural short exact sequence
0 → coker(F−1:H_crys^(i−1)→H_crys^(i−1)) → H_et^i(X,Z_p) → ker(F−1:H_crys^i→H_crys^i) → 0.
For the point over F_p, the left term at i=1 is Z_p and accounts exactly for the discrepancy.

The minimal repair is to retain the algebraically closed hypothesis for the last fixed-point and scalar-extension conclusions. Under that hypothesis, F−1 is surjective on finite crystalline cohomology, including torsion, and the fixed points provide the expected integral descent. This is the scope already used just before Theorem 3.3.3 on p. 22, and it is the scope of Ogus, Corollary 4.11, p. 315. Alternatively, over a general perfect field retain the displayed exact sequence and the appropriate Galois descent data, rather than the two asserted isomorphisms.
