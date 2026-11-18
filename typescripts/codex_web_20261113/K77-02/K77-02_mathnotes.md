# K77-02 · Mathematical notes

Scan numbers are those of the supplied PDF images. Parenthesized numbers are Grothendieck's formula labels; numbering begins afresh with *Extensions quadratiques*. The IDs also identify statements in CHECK_EVENTS.tsv.

## What the pages do

**U18 · Scan 018.** Under the standing assumption that $\alpha^2-4$ is invertible, Grothendieck distinguishes two cases for quadratic forms on the translation space. For invertible $\alpha$ he obtains multiples of $xy$. For $\alpha=0$ he compares $x^2+y^2$ and $x^2-y^2$ on the vertices of $P$. The former takes the two values $2,-2$; the latter vanishes on the vertices and defines a degenerate circumscribed conic.

**U19 · Scan 019.** Five vertices with indices $0,1,-1,2,-2$ are given in universal affine coordinates. Imposing incidence on the first three removes the constant and determines the two linear coefficients. The other two evaluations yield equations for $a,b,c$. The sheet reaches the multiple of $q_0=(x^2-x)+(y^2-y)-\alpha xy$ in (2). A diagonal note at the lower left discusses normalization on differences of consecutive vertices.

**U20 · Scan 020.** For the plane along $D_\zeta$, the adjoint-matrix calculation produces three coefficients. After cancelling $1+\zeta$ the equation is $z=(1-\zeta)(x-\zeta^{-1}y)$. Grothendieck then uses $D_\zeta\subset H_\zeta\subset E$ to describe $C$ as a projective closure. The expression $(E/H_\zeta)^{\otimes-1}\otimes(H_\zeta/D_\zeta)$ and the coordinate sketch identify the two quotient lines involved.

**U22 · Scans 021–022.** The cover opens a new set of notes. A quadratic cover of $S$ is a finite locally free $S$-scheme of rank two. Writing it as $\Omega=\operatorname{Spec} B$ gives a quadratic algebra and the invertible quotient $\check L=B/O_S$. The affine line bundle $E$ parametrizes linear maps $B\to O_S$ taking the unit to $1$. Algebra maps are among them, giving the inclusion on sections in (5).

**U23 · Scans 022–023.** The inclusion is compatible with change of base, hence gives $\Omega\hookrightarrow E$. For an affine bundle $F$ defined by an extension, the text successively identifies a map $\Omega\to F$ with an algebra map, a linear map $C\to B$ preserving the distinguished units, and a map of extensions. This gives the pointwise and relative forms of the affine-envelope property, (9) and (10).

**U24 · Scan 024.** A splitting gives coefficients $b\in\Gamma L$ and $c\in\Gamma L^{\otimes2}$. The product of two lifted elements has scalar part $-cuv$ and lifted part $s(buv)$. Taking trace and determinant of multiplication gives $\operatorname{tr}(\lambda\oplus u)=2\lambda+bu$ and $N(\lambda\oplus u)=\lambda^2+\lambda bu+cu^2$. A boxed marginal equation realizes the cover by $x^2-bx+c=0$; the sideways note describes the data $(L,b,c)$ when the splitting is retained.

**U25 · Scans 024–025.** Replacing $s$ by $s+\tau$ and multiplying two lifted elements gives $b'=b+2\tau$ and $c'=c+\tau b+\tau^2$. Substitution shows why $b^2-4c$ survives the change of splitting. It defines the discriminant as a section of $L^{\otimes2}$.

**U26a · Scans 025–026.** The attempt at the bottom of 025 is cancelled. On 026 the polar form of the norm is written as $\varphi(\zeta,\eta)=\operatorname{tr}\zeta\,\operatorname{tr}\eta-\operatorname{tr}(\zeta\eta)$. Pairing with $1$ gives the trace, and (22) recovers the norm of a sum.

**U26b · Scan 026.** The induced pairing on the exterior square is written as a two-by-two determinant. Choosing the unit and a lift $s(u)$ reduces it to $(4c-b^2)u^2$. This gives (19), with a minus between the discriminant of the polar form and the discriminant of the algebra.

**U27 · Scan 027.** Trivializing $L$ and choosing a splitting amounts to choosing a section $t$ such that $(1,t)$ is a basis of $B$. In this basis $t^2-bt+c=0$, $b=\operatorname{tr}t$ and $c=N(t)$. Trivializing the tensor square represents the discriminant by $b^2-4c$.

**U28 · Scan 028.** A quadratic cover is described as a relative divisor of degree two in its affine envelope. For degree $n$, a section trivializes the affine bundle. The elementary symmetric functions then give coordinates on its symmetric power, valued successively in $L,L^{\otimes2},\ldots,L^{\otimes n}$.

**U29 · Scans 028–029.** The square compares translation of the $n$ inputs with the induced transformation $\varphi_n(\tau)$ of their elementary symmetric functions. With $\sigma_0=1$, the contribution of $\sigma_p$ to the degree-$i$ coordinate is $\binom{n-p}{i-p}\tau^{i-p}\sigma_p$. This is the factorial coefficient in (33), with $p+q=i$.

**U30 · Scan 030.** The preceding affine transformations give an associated affine bundle description of $\Sigma^n(E)$ in (34). For $n=2$ the translation sends $(\sigma_1,\sigma_2)$ to $(\sigma_1+2\tau,\sigma_2+\tau\sigma_1+\tau^2)$. Its linear part in (36) sends the pair to $(\sigma_1,\sigma_2+\tau\sigma_1)$.

**U31 · Scans 030–031.** A crossed passage tries to describe the action on a tensor product of an extension. The surviving construction tensors (37) by $L$, and a splitting gives the identification (38). The proposition identifies the translation bundle of $\Sigma^2(F)$ with $\check B\otimes L$, an extension of $L$ by $L^{\otimes2}$.

**U32 · Scans 031–032.** Quotienting that affine bundle by the $L^{\otimes2}$ direction leaves $2F$, the fibre over the section $2$ of the base line. The resulting morphism $\underline b:\Sigma^2(F)\to2F$ takes a pair of sections to their sum. Grothendieck calls it « une sorte de trace universelle ».

**U33 · Scans 032–033.** The divisor of a pair of sections is described by the product of their ideals. Its universal trace is $s_1+s_2$. Relative to a local section $s$, (43) gives $b(s)=(s_1-s)+(s_2-s)$. Finally (44) separates the choice of a quadratic divisor into a section of $2F$ and a section of the affine line over it, with translation module $L^{\otimes2}$.

## Statements left without proof

- **P18 · Scan 018.** « elles sont comprises parmi les … » and « on trouve comme dessus » use a classification of the quasi-invariant forms. This sheet gives values on vertices and refers back for the classification.
- **P19 · Scan 019.** « Comme celle-ci est invariante sous $G$, la » asserts invariance of (2) and breaks off. No verification of the group action follows in these scans.
- **P24 · Scan 024.** The sideways note says the category of covers « munis d'un scindage équivaut à celle des … $(L,b,c)$ ». The multiplication is given explicitly; the verification on morphisms is left implicit.
- **P26 · Scan 026.** « une formule plus générale, valable pour $\zeta,\eta\in\operatorname{End}(B)$, où $B$ est un fibré vectoriel de rang 2 quelconque » is offered as a second route to verification. The general endomorphism calculation is not written out on the sheet.
- **P28 · Scan 028.** « On sait que … sont des fibrés affines … de rangs respectifs $n$ » introduces the general symmetric-power statement. The pages construct coordinates and their descent, while taking the divisor/symmetric-power identification as known.
- **P31 · Scans 031–032.** « On trouve que … » leaves the transition after (38) blank. The proposition about the translation bundle follows; the detail that identifies its transition maps with those of $\check B\otimes L$ is implicit.
- **P32 · Scan 032.** « est caractérisé par la condition de commuter aux chgts de base, et de transformer … » states the characterization of (40) by its value on pairs. These sheets give the split formula and its interpretation, without a separate uniqueness argument.

## Questions and conjectures

- **Q18 · Scan 018.** « Il reste à étudier » the quasi-invariant forms « d'abord pour $\alpha=2$ et $\alpha=-2$, puis éventuellement pour $\alpha$ “variable” général ». The hook before the final dots is a doubtful question mark. The exceptional cases themselves are clearly named.
- **Q24 · Scan 024.** « attention à la convention de signe ! » and « signe $-$ ! » record the author's concern about the product signs. The marked passages do not establish an alternative global convention.
- **Q31 · Scan 031.** « On trouve que … » leaves space in the argument. No specific conjectural equality is supplied in the gap.

## Slips

- **S19a · Scan 019, lines 25–35; low confidence.** The third incidence equation concludes $v=-b$. The corrected relation **S19a.r** is $v=-c$, by substituting $(0,1)$. The $c/b$ at the left is overwritten. The two later evaluations favour $\alpha$ in $b(1+\alpha)$ and the vertex label $s_{-2}$ where the ink is doubtful.
- **S19b · Scan 019, line 39; medium confidence.** The hypothesis reads « Si $\alpha-1$ inv. ». The corrected hypothesis **S19b.r** is invertibility of the displayed common factor $1+\alpha$. At $\alpha=-1$ over the rationals the written hypothesis would allow cancellation of zero.
- **S20a · Scan 020, lines 22–24; medium confidence.** The page puts $\zeta=-1$ alongside invertibility of $1+\zeta$. The needed fibrewise condition **S20a.r** is $\zeta\ne-1$. **S20b · Line 17; low confidence.** An apparent extra $\zeta$ before $\alpha$ in $B$ conflicts with its next expression if $\alpha=\zeta+\zeta^{-1}$. The coefficient at that place carries a doubt mark.
- **S24a · Scan 024, lines 35–46; low confidence for the revision.** The first matrix has $-bu$ at lower right. The corrected entry **S24a.r** is $+bu$ by the multiplication formula and the second matrix at $\lambda=0$. The earlier signs around (13) and (14) are overwritten. **S24b · Line 63; medium confidence.** The difference of two splittings should belong to $\Gamma(L)$; (16) writes $\Gamma(E)$. Scan 028 uses $\Gamma L$ for that translation.
- **S25a, S25b · Scans 025–026; low confidence.** A crossed (19) on 025 has $-4D$, and a crossed norm formula has $\operatorname{tr}(\zeta\eta)$ alone as cross-term. The corresponding live formulas on 026 give $-D$ (**S25a.r**) and $\operatorname{tr}\zeta\,\operatorname{tr}\eta-\operatorname{tr}(\zeta\eta)$ (**S25b.r**). These are abandoned formulas, with uncertain details in the struck writing. **S25c · Scan 025, line 23; low confidence.** If the character is $\tau'$ rather than $c'$, the following rearrangement requires $c'$.
- **S29a · Scan 029, lines 22 and 28; low confidence.** The translated second factor may contain a minus. The common translation requires a plus. A crossed expression for the second symmetric function appears to omit $\tau$ in $(n-1)\tau\sigma_1$. **S29b · Line 32; medium confidence.** In the unrestricted double sum, the denominator $(n-p-q)!$ calls for $p+q\le n$; alternatively the coefficient needs the out-of-range zero convention. Formula (33) enforces the range degree by degree.
- **Stext · Scans 024, 026–030.** Likely literal slips include « la multiplication … est donné » (024, line 33; *donnée*), « la forme discriminant » (026, line 24; *discriminante*), « une section de $t$ de $B$ » (027, line 7; *une section $t$ de $B$*), and « interprête » (030, line 33; *interprète*). On 028–030 some parentheses around the vector-bundle expressions have only one written side. The doubts file gives the places.

## Pointers

**Ptr18 · Scan 018.** « comme dessus » and « comme nous avons remarqué » point to earlier arguments about forms and the degenerate conic. They give no title, cote, author or numbered result.

**PtrLocal · Scans 023–033.** Identifiable numbered pointers are internal. Examples are « de (3) dans (7) » for the affine-envelope property (023), « de (20) » for the determinant pairing (026), « formule (13) » for the basis computation (027), and « correspondant à l'extension … (37) » in the proposition (031). No named person, other cote or external paper is cited on these sheets.

## Remarks of the model

- **R1 · My observation, high confidence; scans 025–026.** For the surviving multiplication rule, the polar Gram matrix in the basis $(1,t)$ is $\left(\begin{smallmatrix}2&b\\b&2c\end{smallmatrix}\right)$. Its determinant is $4c-b^2$. This checks the surviving determinant identity directly, irrespective of how one reads the older crossed coefficient.
- **R2 · My observation, high confidence; scans 029–030.** In degree two, subtracting the value of (35) at $(0,0)$ gives (36). Composition of two transformations of (35) adds their parameters. Both statements follow directly from that unmarked display.
- **R3 · My observation, high confidence for the two split formulas; scans 025 and 033.** On 033 replacing the reference section $s$ by $s+\tau$ in (43) subtracts $2\tau$ from $b(s)$. On 025 adding $\tau$ to the algebra splitting adds $2\tau$ to its trace coefficient. The object being shifted is specified differently on the two sheets; the two explicit computations can be checked separately.
- **R4 · My reading question, low confidence; scan 019, line 55.** The frozen margin reads $q(s-s')=1$. The letter on the page is $q$; a possible intended referent is the homogeneous quadratic part of $q_0$. For the difference $(1,0)$ the homogeneous part has value 1 and the full $q_0$ has value 0. The short slanted note does not expressly make that distinction.
- **R5 · My reading question, low confidence; scan 031, lines 2–7.** The frozen text marks « d'où une opération » and the following extension formula as deleted. The alternative is an enclosure setting off a preliminary construction. The long rule crosses the formula and also turns into the margin, so its editorial force is less clear than its position.
