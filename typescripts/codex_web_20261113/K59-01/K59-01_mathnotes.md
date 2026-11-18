# K59-01 — Mathematical notes

Scan numbers are archive numbers. The letters and primes below follow the manuscript. Statement identifiers refer to the accompanying check-event register.

## What the pages do

**M1 · Scans 002–003. Changing the section.** For a proper flat morphism of finite presentation with the stated condition on the direct image of its structure sheaf, a section $g$ normalizes an invertible sheaf $\mathcal L_g$ on $X\times_S P$. The determinant of its derived direct image is called $M_g$. Formula (*) compares $M_g$ and $M_{g'}$ by the $\chi$-th power of a ratio of restrictions of a Weil bundle. The sideways note calls this ratio algebraically equivalent to zero. Its restriction to $P^\delta$ gives a Néron–Severi class independent of $g$.

**M2 · Scans 003–006. A section of a torsor.** Write $B=P^\circ$ and $A=\underline{\mathrm{Pic}}^\circ_{B/S}$. Descent and change of base give $\varphi:\underline{\mathrm{NS}}_{X/S}\to\underline{\mathrm{NS}}_{B/S}$, which the manuscript calls « pas nécessairement additif ». A class $\lambda$ on $B$ supplies a homomorphism $\widetilde\lambda:B\to A$. This describes the component over $P^\delta$ as a contracted product. Taking $\lambda=\varphi(\delta)$, the manuscript factors the map out of $X$ through its Albanese torsor. It names the resulting section $L(\delta)$ in the frame on 005. The beginning of 006 draws the conclusion that the displayed $A$-torsor has a canonical trivialization.

**M3 · Scans 006–008. Computing the class.** Over a field, a choice of $p\in P^\delta(k)$ identifies $P^\delta$ with $B$, and the line bundle under consideration is expressed using the Weil bundle and $L$. Riemann–Roch gives a pushforward involving $D$, the class of the Weil bundle, and the Todd class of $X$. For smooth $X$ of dimension $n$, the manuscript places $D$ in $H^1(X)\otimes H^1(B)$ and expands the exponential. **M3.1.** A term of bidegree specified by $i,j$ must satisfy $2i+j=2n$ on the $X$ factor. Taking $j=2$ leaves $i=n-1$ and the factor $1/2$. The live formula on 008 uses $a_{n-1}$.

**M4 · Scans 008–010. The curve example.** In dimension one, $\delta$ has degree $d$. The calculation in a symplectic basis gives $\varphi(\delta)=\sum e_i\wedge f_i$, identified on 009 with the canonical polarization of the Jacobian. The manuscript gives $\chi(\delta)=1-g+d$ and uses the theta divisor to write $c:B\to A$. **M4.1.** The three torsors then have degrees $g-1-d,\ g-1,\ d$. Their sum is $2g-2$. Identifying the constructed section with $K$ remains a question, which leads to the NB about the universal curve.

**M5 · Scans 010–011. The abelian-scheme example.** With $X=A$, the correspondence written $\exp D$ defines a transform $\Phi$ on the geometric fibres. The page says it exchanges degrees and interchanges ordinary and convolution products. The degree-one part yields a polynomial expression of degree $n-1$ for $\varphi$. The two boxed compositions on 010 are both multiplication by $-\chi(\delta)$, on $A$ and $B$ respectively. Scan 011 discusses nondegeneracy, polarizations, their degrees, the primed class and the iteration $\varphi(\varphi(\delta))=\delta\chi(\delta)^{n-2}$.

**M6 · Scan 012. The degree-one case and translations.** The page rewrites the section from d) as an isomorphism of Picard torsors. When the polarization has degree one, its map identifies $A$ with $B$, and the isomorphism becomes one between the components labelled $\delta$ and $-\delta$ on $A$. A long margin note asks about the square of this isomorphism. The final paragraph uses translation invariance to recover the composite on $A$.

**M7 · Scans 013–014. Scaling and trivialization.** Replacing $\delta$ by $\lambda\delta$ gives contracted powers with exponents $\lambda^{n-1}$ and $\lambda^n$. Their difference gives a trivial torsor. At $\lambda=-1$ the square is trivial. Interchanging $A$ and $B$, iterating the primed construction, and considering even $\chi(\delta)$ yields further proposed trivializations. Scan 014 finishes with the case $n=2$. The identity of the resulting sections with the canonical ones is consistently a separate issue on 013.

## Statements left without proof

| Scan and line | Author’s words or formula | Scope of the omitted step |
|---|---|---|
| 002 l7–10, margin | « on suppose … valables » | The finiteness hypothesis needed for the perfect complex and determinant. The name of the result in the margin is uncertain. |
| 003 l1–12 | « on a un isom canonique » and « Par descente » | The component identifications and the descent of the section-independent class. The margin asks for detail. |
| 003 l14–20 and 004 l9–16 | « Cette action est triviale » and « se déduit de l’action évidente » | The translation action on the identity component and Néron–Severi group, and its description on the component labelled λ. |
| 005 l6–16 | « on trouve une factorisation » and « on applique la formule (*) de b) » | The Albanese factorization and the sign of its structural homomorphism. |
| 007 l6–23 | « se calcule par RR » and « D définit un isomorphisme » | Riemann–Roch and the duality supplied by the middle Künneth component are invoked. |
| 009 l8–22 | « C’est la classe de polarisation canonique » and « On sait que » | Identification with the theta class and the image of the first Albanese torsor in degree −1. |
| 010 l1–7 | « Il suffirait de déterminer le groupe en question en car. nulle. » | The reduction of the stated section-group problem to characteristic zero. |
| 010 l8–22 | « On sait que » … « transforme produit ordinaire en produit de convolution » and « On vérifie que » | The transform properties and both composite identities. Scan 012 gives the later translation argument for the composite on A. |
| 011 l1–9 | « On déduit d’ailleurs de la relation plus haut » | The degree comparison and choice of sign for χ(δ′). The margin sketches an argument from squares and positivity. |
| 013 l15–19, left | « χ(δ) pair implique que δ divisible par 2 » | A divisibility assertion in the marginal comparison. The page gives no additional condition or proof there. |

## Questions and conjectures

| Scan and line | Author’s words | Question |
|---|---|---|
| 003 l7–12 | « détailler » | Supply the details of descent. |
| 005 l11–17, 009 l9 and 010 l22 | « vérifier si le signe est correct ! », « vérifier que le signe est correct », « attention aux signes ! » | Check the scalar on the Albanese, the Jacobian identification and the two polarization composites. |
| 009 l13–22 and 010 l1–7 | « on s’attend à trouver la section canonique K (à prouver !) », « le groupe des sections de P sur S est engendré par K » | Does the construction give K? Does K generate the sections for the universal curve in the stated modular setting? |
| 011 l10–23 | « inspire confiance directement », « Il faudrait prouver » … « n’est plus divisible », « on s’attend à ce que φ(δ) engendre le groupe » | The iteration, primitivity of the transformed class, and generation of the section group of NS on each connected component. |
| 012 l6–17 and l22–24 | « compatible avec les sections canoniques », « à vérifier », « Attention au signe !?! » | Compatibility on squaring, a refinement using ₂A, and the translation sign. |
| 013 l8–19 | « Vérifier que la trivialisation est la trivialisation canonique », « vérifier que cette section est encore la section canonique » | Compare the constructed trivializations and sections with the canonical choices. The final paragraph’s theta comparison is cancelled. |

## Slips

| ID | Scan and line | As written and proposed reading | Confidence and reason |
|---|---|---|---|
| S1 | 004 l20–22 | $L_g\mid P^\delta$. The restriction from c) would be $M_g\mid P^\delta$. | Medium. Scan 002 puts the determinant on P and calls it M. The angular L on 004 is legible. |
| S2 | 007 l12–14 | $\Delta=\mathrm{cl}\,\Delta$. A definition using $\mathrm{cl}\,L$ would parallel the line for D. | Medium about intention. This occurrence of Δ has straight sides and was retained after reinspection. |
| S3 | 008 l5–15 | $a^i$ in the expansion and $a_{n-1}$ in the result. An upper $n-1$ would continue the preceding convention. | Medium. The lower index also occurs in the live line below the cancellation. |
| S4 | 011 l7–14 | $\delta''{}^{-1}$ starts a formula whose right side computes the map for $\delta''$. The elliptic specialization then has $\delta\chi(\delta)$ where exponent $n-2$ gives $\delta\chi(\delta)^{-1}$. | Low. The first formula starts beside a cancelled expression, and the elliptic line itself contains a reworking. |
| S5 | 011 l15–23 | $\varphi(\delta)=\delta'$ in the NB. The definition before it would give $-\varphi(\delta)=\delta'$. | Medium. Both the earlier definition and the explicit reminder on 012 have the minus sign. |
| S6, S6R | 013 l10–11 | « ppcm ». For $n\geq2$ the property is « pgcd ». | High. The values $\lambda^{n-1}(\lambda-1)$ are even and include $2$ or $-2$ at $\lambda=-1$. At $n=2,\lambda=3$, the value is 6, which cannot divide 2. The similarly worded partly struck passage on 014 has low value as evidence of intent. |
| S7 | 014 l5–12 | The component for δ starts on A/S, then carries B/S after the two composites. Keeping A/S would agree with the introduction of δ. | Medium. The earlier formulas distinguish the two bases. |
| S8 | 014 l22–23 | The exponent is $(\chi-1)\chi^{n-1}$. The difference of powers above gives $(\chi-1)\chi^{n-2}$. | Medium. The larger written exponent is a multiple of the smaller one, so the assertion of triviality can still hold. |

## Pointers

| Scans | Author’s words | Referent |
|---|---|---|
| 002–003 | « de Weil », « en vertu de b) » | The named bundle and the change-of-section calculation on 002. |
| 004–006 | « Reprenant les notations de c) », « la formule (*) de b) », « faisceau de Weil » | Components, the determinant identity, and the normalized line bundle. |
| 007 | « par RR », « Todd », « de Tate » | Riemann–Roch, the Todd class and Tate twists. No work or page is specified. |
| 009 and 012 | « de la fin de d) » | The torsor and section constructed on 005. |
| 010 | « Chow » | The groups on which the displayed transform acts. |
| 013–014 | « Dans l’isom can » and « de (*) » | The boxed isomorphism on 012 and the later chain of isomorphisms. |

No other archive cote, dated paper, bibliographic citation or correspondent is identified on these sheets.

## Remarks of the model

- **R1. Model, high confidence in the algebraic check.** On 008–009 the minus under the brace is consistent with passing an odd-degree class through another odd-degree class. Multiplying the displayed tensor in a symplectic basis gives two equal diagonal contributions. The check used genera 1 through 5. It does not identify the geometric theta class or resolve the author’s marginal sign question.
- **R2. Model, high confidence in the internal comparison.** Substituting the composite on 010 into the translation on 012 gives $\chi(\delta)a-\chi(\delta)a=0$. This explains why the two formulas have to use compatible signs. The comparison takes the boxed composite as given.
- **R3. Model, medium confidence about the scope of the divisibility question on 013.** The numerical relation $\deg\widetilde\delta=\chi(\delta)^2$ on 011 alone does not give a factor of two in a class. At the level of alternating forms, take two symplectic blocks $J$ and $2J$ with $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. The determinant is 4 and one entry is 1. The matrix check is exact. Applying it to the manuscript’s geometric assertion would require identifying the class and its integral form in the setting of that assertion.
