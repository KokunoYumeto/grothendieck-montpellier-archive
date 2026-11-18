# Mathematical notes · K78-08

These notes use the scan numbers printed in the LaTeX fragment. A reference to L is to the corresponding page file. Short French quotations preserve the manuscript wording. Identifiers refer to the check register.

## What the pages do

**Incidence and automorphisms, 103–104.** The argument starts in part b) of an ongoing proof. Lifts of a vertex and of its incident edges are compared with their images in the affine plane. Part c) recalls that the vertices span the plane. Part d) uses transitivity on repères to identify the image group with the automorphisms of the realization. Part e) tests the polygon map on the two operations $\sigma_0,\sigma_1$.

**Faithfulness, 105–106.** A regular realization is tested on vertices, edges, the automorphism group and its orientation-preserving subgroup. The proof turns a repetition $s_i=s_{i+d}$ into a power of $u$ fixing the spanning vertices. A corollary identifies the stabilizer of a vertex in the orientation-preserving action. To recover incidence, the proof considers a line meeting the circumscribed conic in more than two points and recalls the singular case with two distinct parallel lines.

**The quotient polygon, 107–108.** A corollary identifies the number of image vertices, the number of image edges, the size of the orientation-preserving image group and the order of $u$. This number determines a quotient polygon on which the realization is faithful. The final sentence asks for the preceding material on polygon morphisms needed to speak of those quotients.

**Laurent polynomials, 109–110.** After the title sheet, the author puts $U=T+T^{-1}$ and introduces $\Sigma_i$ and two formulas for $F_n$, according to parity. He records degrees, values at $2$ and $-2$, initial examples and an ideal equality. He multiplies an identity by $(T-1)(T^2-1)T^{n-1}$ and marks cancelling terms. The recurrence then identifies $X_n$ and $Y_n$ as products of adjacent $F$’s. The two inverted calculations on scan 111 belong with this work.

**Reused typescript, 111.** The text discusses hostility toward foreigners in France and quotes a charge of providing food and lodging to Kuniomi Masunaga. Its hand corrections and dates belong to the typescript. The mathematical writing occupies the opposite orientation at its foot.

**A second argument and the affine matrix, 112.** Monicity, degree and the roots of two polynomials in $T$ give another argument for the formula for $X_n$. The author writes the images of $s_0,s_1,s_{-1}$ and uses their coordinates to write a matrix for $u^n$. A matrix covered by large cancellation loops precedes the live one.

**The vanishing criterion, 113–114.** Over a ring $k$, the transformation $u_\alpha(x,y)=(1-y+\alpha x,x)$ carries the initial vertex through the sequence $s_n$. The theorem relates $u_\alpha^n=\mathrm{id}$, return of a vertex and $F_n(\alpha)=0$. The converse uses an integral polynomial combination of $F_{n-1}$ and $F_{n+1}$. A short note on the next sheet proposes coefficients.

**Primitive roots and faithful realizations, 115–116.** The author defines $\Phi_n$ by its roots, records its degree and the divisor product for $T^n-1$, and introduces $\Psi_n$ using $T+T^{-1}$. The condition $\Psi_n(\alpha)=0$ expresses faithfulness after passage to the quotient under the stated characteristic hypothesis. The text gives a modular ring when $n$ is neither prime nor twice a prime, considers the prime case, and begins the twice-prime case. Much of the work in the latter two cases is cancelled.

**German letter fragment, 115.** Three cancelled lines thank Dagmar for birthday greetings. They end after “lieben Geburtstagsgrüsse.” No date or signature is visible.

## Statements left without proof

- **103, L21.** “$S$ engendre $E$ : connu.” The spanning assertion is invoked again on 105.
- **104, L13–16.** “on l'a vu dans la dém. de a) et b).” Compatibility with the two operations is referred back to the preceding argument. Part a) is outside this set of scans.
- **106, L32–35.** “Mais le cas $\alpha=-2$ a été examiné”. The description by two parallel lines is used here. The examination it refers to is outside this passage.
- **107–108.** “Mais il manque un [sorite|sorte] sur les morphismes ...”, continuing “de parler du quotient”. The quotient property is stated before the proposed treatment of the morphisms.
- **110, L39–41.** The ideal equality $(F_n,F_{n+2}^{\,\text{[possible prime]}})=(1)$ is written on a separate line. The small prime-like stroke belongs to the reading apparatus. No argument is attached at that point.
- **110 and 112.** “$X'_n=X_n$” and “On a vu que ce sont les racines de $A_n(T)$” use earlier information about $X_n$ or its zeros. Scan 112 gives a second argument, rather than a new derivation of those earlier data.
- **113–114.** “Or $\exists A_n(U),B_n(U)\in\mathbb Z[U]$ tels que …”; “On peut prendre …”. The proposed coefficients are recorded without a substitution on these sheets.
- **115–116.** “il f. et s. que on ait … $\Psi_n(\alpha)=0$”; “alors l'anneau modulaire … est …”. The factorization and ring identifications are stated. At “Supposons enfin que $n=2p$”, the continuation below “Si $p$ impair” consists of crossed calculations.

## Questions and conjectures

**107–108.** “Mais il manque un [sorite|sorte] sur les morphismes (étales) de polygônes comb. …, nous permettant de parler du quotient …”. This is an explicit gap in the exposition. No mathematical assertion here is expressly labelled “conjecture” or “à vérifier”.

## Slips

| ID | Scan and reading | Correction or qualification | Confidence and grounds |
|---|---|---|---|
| S1 | 105, L32–34. “$\exists d<n$ … $s_i=s_{i+d}$” | Among integral period differences require $0<d<n$, or require a nonzero class modulo $n$ when $n$ is finite. | High for the missing exclusion of zero. With $d=0$ the equality holds even for distinct vertices. See C1. |
| S2 | 110, L59. The recurrence ends in $X_{n-2}$ after two primed terms. | If the recurrence is being proved for the newly defined sequence, the third term would be $X'_{n-2}$. | Medium. The induction identifies the two sequences lower down, which can make the printed distinction harmless after that step. The last X has no visible prime. |
| S3 | 111, L39. $1+T^2+T^4=(T^{-2}+T^2)+1$. | Multiply the first member by $T^{-2}$ to obtain the middle expression. | High. At $T=2$ the two written members have different values; the corrected one equals $U^2-1$. See C2. |
| S4 | 113, L37. The summary ends “$a\Leftrightarrow b\Leftrightarrow c$”. | The immediately preceding two implications concern the condition labelled b with an i-like subscript. | Low for the identification of c with that precise subscript, which carries a doubt mark. There is no c-labelled condition in the statement. |
| S5 | 113, L47. “la relation $F_n(\alpha)=1$”. | Read $0$ for the intended conclusion of this implication. | High. The linear combination of the two zero products on L41–42 is zero, and the stated coefficient identity on L45 makes that combination $F_n(\alpha)$. The triangle example in C3 also distinguishes 0 from 1. |
| S6 | 114, L5–6. After the coefficient rewrites, $B_n=F_n$, $A_n=F_{n-2}-UF_{n-1}$. | In the second term, $-UF_n$ gives the coefficient obtained by collecting the recurrence on 110, L65. | Low as a diagnosis of the author's intended revision because the two coefficient letters are overwritten. The algebraic discrepancy for the displayed readings is reproducible. For $n=3$, the left side on 113 becomes $U^2+1$; replacing the last index gives 1 in that case. See C4. |

## Pointers

- **103–105.** “et par a)”, “Dans la dém. de a)”, “on l'a vu dans la dém. de a) et b)” refer to the ongoing polygon proof.
- **106 and 112.** “le cas $\alpha=-2$ a été examiné” and “On a vu que ce sont les racines de $A_n(T)$” refer back without naming another document.
- **111.** The typescript names “Kuniomi Masunaga”, the “Tribunal Correctionnel de Montpellier”, “l'article 21” and “l'ord. du 16.11.1945”. These are references in the document.
- **115.** “Liebe Dagmar” gives the addressee's first name only. No mathematical paper, other cote or named mathematical author is cited in this group.

## Remarks of the model

**R1 · High, 110.** The leading-term shorthand in $\Sigma_i(U)=U^i+\cdots$ needs care at $i=0$. The definition in $T$ gives $\Sigma_0=2$. Thus a literal monic leading coefficient cannot cover this endpoint; the ellipsis does not specify how the endpoint should be read. See C5.

**R2 · High for this example, 113.** At $\alpha=-1$, the displayed affine map permutes $(0,0),(1,0),(0,1)$ cyclically. Also $F_3(-1)=0$, using $F_3(U)=1+U$ from the Laurent sum. This is a direct check of a single instance of the return criterion. See C3.

**R3 · Low, 112.** The first matrix has no decipherable ink for the upper two entries of its middle column. The third coordinate pair and the right column of the live matrix contain overwritten indices. The action on the three vertices suggests how a completed calculation could be checked, but those expected entries do not settle the overwritten strokes.
