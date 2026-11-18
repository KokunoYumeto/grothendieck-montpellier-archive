# K47-01 · Mathematical notes

## What the pages do

**U1 · The transform (003).** For an abelian scheme \(A/S\), a scheme \(X/S\), and a line bundle \(L\) on \(A\times_S X\) satisfying the conditions at the identity and on fibres, Grothendieck defines \(\Phi_L(F)\) by pullback, tensor with \(L\), and direct image to \(X\). He distinguishes the functor on perfect complexes from its map \(\varphi_L\) on \(K\). Proposition 1 says that it takes Pontryagin convolution to the ordinary product. The margin suggests versions with proper supports and with torsors.

**U2 · Proof of Proposition 1 (003–004).** Base change reduces the assertion to the dual abelian scheme \(B\) and its Weil line bundle. Two diagrams track addition, projection and the diagonal of \(B\). The theorem of the square splits the pullback of \(L\) into two factors. The projection formula, base change and Künneth then identify the transform of a convolution with the tensor product of the transforms.

**U3 · The composite and its kernel (004–006).** The next statement composes the transform for \(L\) with the transform for the transposed line bundle. The \(K\)-group version displays the inversion \(s_A\) and the sign \((-1)^n\). The categorical statement includes \(\tau_A[-n]\). Grothendieck forms a kernel on the triple product, regroups it as \(C\times B\) with \(C=A\times A\), and uses the map \(C\to B^*\) supplied by the birigidified line bundle. In this case he identifies its kernel with the antidiagonal, the graph of \(s_A\).

**U4 · The Weil module (006–008).** Lemma 1 places its direct image on the identity section with a tangent determinant and a shift. The corollary pulls this description back to \(C\). Lemma 2 gives vanishing for a nontrivial line bundle algebraically equivalent to zero. Grothendieck admits that lemma, constructs the comparison at the identity from top cohomology, and separates the fibres off and on the identity section. He leaves a compatibility check at the latter.

**U5 · Sections, Euler characteristics and determinants (008–009).** Remark 1 records the transforms of section classes and the associated line bundles, then relates augmentation and Euler characteristic under \(\Phi_L\). Remark 2 composes the transform with the determinant, maps the relative Picard schemes and specifies the components indexed by \(\delta\) and \(-\delta'\). The next page gives the relation \(\widetilde{\delta'}\,\widetilde{\delta}=-\chi(\delta)\mathrm{id}_A\).

**U6 · Chern classes (009).** With \(\chi(\delta)\ne0\), Grothendieck proposes a fractional-power expression in quotation marks for the transformed class of \(L\). He writes the character as \(\chi\exp(-D'/\chi)\) and the total Chern class as \((1-D'/\chi)^\chi\). He asks about torsion, singles out cohomological equivalence, and writes an integrality assertion for a multiple of \(\delta'^k\).

**U7 · Riemann–Roch and products (010–011).** He introduces \(T=\mathrm{Todd}(t_A)\) and the graded transform \(\psi_D\) associated with \(\exp D\). A long attempted computation is crossed out. In the surviving calculation he applies the character to the convolution identity and boxes \(\psi_D(a*b)=\psi_D(a)\psi_D(b)\). Scan 011 starts from the ordinary product, carries the sign and the factor involving \(\omega_A\) into a second boxed formula, and refers to Kleiman.

**U8 · Duality and automorphisms (011).** Subsection 4 gives a functorial duality isomorphism involving \(\check F\otimes\omega_A[n]\) and its virtual-class counterpart. Subsection 5 gives equivariance for an automorphism \(u\) and the contragredient \(u'\). The last sentence specializes to the symmetry \(s_A\) and includes \(\varphi_L\).

## Statements left without proof

| ID | Scan and words | Scope |
|---|---|---|
| P1 | 003, margin, “peut se généraliser au cas …” and “on peut enfin généraliser …” | The two extensions, including the one with torsors, are sketched in the margin. |
| P2 | 004, “(th. du carré) un isom can.” and “Künneth” | These are invoked in the proof of Proposition 1. |
| P3 | 007, “Nous allons ici admettre le lemme 2” | The vanishing used in the support argument is explicitly admitted. The sheet retains a cancelled start of a proof. |
| P4 | 007, “Or on sait que l’on a un isom canonique” | The exterior-power identification of top cohomology with the determinant of the tangent space is recalled. |
| P5 | 008, “à faire une vérification de compatibilité….” | The remaining comparison at the identity fibre is specified and left incomplete. |
| P6 | 008–009, “définit”; “déjà caractérisé par ailleurs”; “Elles sont vraies au moins … mod équivalence cohomologique” | The component calculation and the asserted cohomological validity of the Chern formulas are stated here. |
| P7 | 011, “Il résulte du Th. de dualité” and “par transport de structure un isom canonique” | Duality and equivariance are cited as the grounds for the last two remarks. |

## Questions and conjectures

- **Q1 · 009.** “On peut se proposer … de ‘calculer’ la classe” leads to “on devrait avoir” and the quoted class \(\chi L'^{-1/\chi}\). The qualifying word beginning *Heuristiq…* is abbreviated or compressed. The condition on \(\chi(\delta)\) is part of the proposal.
- **Q2 · 009.** “Ces formules sont-elles bien vraies mod torsion ?” The large question mark in the left margin accompanies this question. The writer then asserts a weaker setting and indicates a divisibility consequence. There is no answer here to the full torsion question.

## Slips

| ID | Scan | Reading, proposed correction and reason |
|---|---|---|
| S1 | 004 | The left \(R\mathrm{pr}_2\) in the Künneth line lacks the pushforward star. \(R\mathrm{pr}_{2*}\) matches the right-hand factor and the defining direct image. The apparent \(L\) in the next \(\Phi\) could also be \(F\). Calling that letter a slip has **low** confidence because the ink is doubtful. |
| S2 | 005 | \(M\in D_{\mathrm{parf}}(A)\) appears where \(D_{\mathrm{parf}}(A\times A)\) would match the displayed \(\mathrm{pr}_{13*}\) from \(A\times B\times A\). At the foot, the component map ends in \(B\); the adjoining parenthesis gives \(B^*\). The plain B is clear even though the connector is doubtful. |
| S3 | 006 | The base-change calculation has \(\mathrm{pr}_{2*}\) and \(\mathrm{pr}'_{2*}\). Its square has \(\mathrm{pr}_1,\mathrm{pr}'_1\), and the following corollary uses \(\mathrm{pr}_{1*}\). The first projections match those particular factors. Later \(\varphi:A\simeq C^*\) has a clear C where the component map on scan 005 gives \(B^*\). |
| S4 | 007 | \(H^i(X,L)\) in Lemma 2 appears to mean \(H^i(B,L)\). Its hypothesis makes \(L\) a line bundle on \(B\) and introduces no \(X\). |
| S5 | 009 | The quadratic and cubic coefficients of the written total Chern expansion are each a factor of \(\chi\) larger than the coefficients of the displayed power. **S5-R** gives the matching denominators \(2\chi^2\) and \(3!\chi^3\) when the written numerators are retained. The general denominator likewise shows \(n!\chi^{n-1}\); the sign in its last numerator factor is faint. The explicit degree-two and degree-three comparison uses only uncancelled, clear coefficients. |
| S6 | 010 | \(D\in\mathrm{Gr}^1(A\times A)\) appears to mean \(\mathrm{Gr}^1(A\times B)\). The line says that \(L\) defines \(D\), and the projection used later on the same sheet has source \(A\times_S B\). |
| S7 | 011 | There is space between the two right-hand transforms in the first box. The opening \(\varphi_L(xy)\) identity on the sheet has an explicit \(*\) between the corresponding terms. A lost \(*\) is a plausible editorial restoration of the box, with **medium** confidence. The box in subsection 4 lacks a closing parenthesis on the right. An added ) after \([n]\) would complete the grouping in the preceding unboxed identity. |

## Pointers

| Scan | Words on the sheet | Referent |
|---|---|---|
| 003–004 | “faisceau de Weil”, “th. du carré”, “Künneth” | Named objects or results used in Proposition 1. No publication is specified. |
| 005–007 | “Prouvons la prop. 2”, “modulo dém. du Lemme 1”, “(Mumford)” | Internal references to the composite and its kernel, then a name attached to the admitted vanishing lemma. |
| 009 | “par ailleurs”, “indépendant des résultats de Mumford” | The first allusion gives no identifiable text. The marginal note names Mumford without a title. |
| 010 | “par R.R.” | Riemann–Roch for the maps indicated on the sheet. |
| 011 | “par Kleiman dans ‘10 Exposés…’”, “n’a pas tenu compte du facteur \((-1)^n\) !” | Grothendieck attributes related formulas to Kleiman and comments on the sign. This is his report about that work. |
| 011 | “Th. de dualité” | The projection from \(A\times_S B\) to \(B\). No numbered external source is given. |

## Remarks of the model

- **M1 · Model, high confidence (009).** The coefficient discrepancy can be isolated without interpreting the overtraced argument of \(\varphi_L\). At \(\chi=3\), the displayed power has quadratic coefficient \(1/3\) and cubic coefficient \(-1/27\). The two written coefficients give \(1\) and \(-1/9\). The preceding exponential, by contrast, has the written quadratic and cubic coefficients. This checks the scalar expansions only.
- **M2 · Model, high confidence (006–008).** The gap the writer identifies is local to his comparison at points of the form \(e(s)\). He explicitly assigns the other points to Lemma 2 and writes “à faire une vérification de compatibilité” after reducing the identity-section case. Thus admitting Lemma 2 and leaving that compatibility open are two distinct features of the argument.
- **M3 · Model, low confidence (009).** The final proposed divisibility denominator \(k!\chi^{k-2}\) is worth comparing with the total-class calculation just above it. A symbol immediately before the fraction has been cancelled. The scalar check cannot determine what integral cycle statement was intended or answer Q2.
