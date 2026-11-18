
## Scan 33

Start UTC: 2026-11-17T21:07:13+00:00  
Crop-only observations saved before opening page file: 2026-11-17T21:07:37+00:00

### Crop-only words, accents and shapes

Top matrix has extensive overtyping in rows i, i+1 and lower diagonal; u and v are small Latin-looking open strokes. No bold or double-struck capital. Formula (17): initial index i, then 1 through n+1; a sum annotation begins x_{i+2}. Formula (18) has an inserted −x_i+ before the second-row expression, and a small cancellation at its right-hand zero; the next term begins x_i+. Prose read afresh: “réflexion”, “ssi”, “ces relations sont conséquence”, “iième”, “exprimera”, “comb. lin.”, “Ceci signifie:”. The parenthesis before qui is not visibly closed. Below (19): “donc les seuls paramètres qui restent”, struck “sont”; λ_i above u_{i,i}; “ce dernier pour ... pas pour σ_n”; “de sorte qu’on peut écrire”. Equation (20) has a blot before (1−λ_i) and a sum expansion written above Σ_i. These are crop-only observations, before opening the page file.

### Comparison and changes

Read all five numbered displays, including all visible matrix rows; (17) has two semicolons, (18) has a colon at H_i and a left brace, (19) two columns of conditions, and (20) a comma before the continuation. The notation is u, v/nu, sigma, Sigma, lambda and mu; no script or double-struck capital is supported. i in u/v pairs stays i, while first-column position labels and i+1/i+2 were checked individually. Matrix (16) remains the least secure region: lower entries have ink written directly over ink, not a recoverable clean matrix. Its visible zeros, vertical continuation strokes, horizontal rules and residual v entries are retained without reconstructing a canonical matrix.

Changes: (18), second summand x_{i+1} -> unsure{x_{i+2}|x_{i+1}}: the terminal numeral has a curved descending stroke that favours 2; the parallel formula favours 1, which is not substituted. The heavy zero in the second row now retains a doubtful overwritten a before 0. In the inserted parameter restriction, 1<=i<=n-1 -> unsure{0<=i<=n-1|1<=i<=n-1}; the first character is rounded. No mathematical normalization of Sigma_2 was made. Re-read the oblique insertion “ce dernier...” along its baseline; its linking line leads after mu_i, not after lambda_i. The upper sum annotations are attached to their own Sigma_i. The line through “sont” is cancellation; the long line under the insertion is an attachment, not a cancellation of the next sentence. Accents and unfinished parenthesis are retained. No other change.

### Formula register checked against the crops

1. Display: `\sigma_i= \left(\begin{array}{c c c c c c c c} \overset{\unsure{i-1}}{\overline{\left(\begin{smallmatrix}1&&0\\&\ddots&\\0&&1\end{smallmatrix}\right)}}  &0&u_{i1}&\unsure{v_{i1}|\nu_{i1}}&v_{i1}&\cdots&v_{i1}&0\\  & &\vdots&\vdots&\vdots&&\vdots&\vert\\  & &u_{i,i-1}&v_{i,i-1}&\unsure{v_{ii}}&\cdots&\unsure{v_{ii}}&0\\  &0&u_{ii}\deleted{\unsure{1}}&v_{ii}\deleted{\unsure{+1}}&\unsure{v_{i,i+1}}&\cdots&v_{i,i+1}&0\\ 0&1&u_{i,i+1}&v_{i,i+1}&v_{i,i+1}&&&\\  &0&0&\deleted{\unsure{v_{i,i+2}}}\,0&\deleted{\unsure{v_{i,i+2}}}\,0&&0&0\\  & & & &\deleted{\unsure{v_{i,i+2}}}\,0&&&\\ \unsure{\overline{0\ \cdots}}&\overline{0}&\overline{0}&\overline{0}&\overline{0}&&\overline{v_{i,i+2}}&\overline{0}\\ 0\ \cdots\ \deleted{0}\,0& &0&0&0&&0&\unsure{1} \end{array}\right) \tag*{(16)}`
2. Display: `\begin{aligned} \sigma_i(x_1,\ldots,x_{n+1})={}&(x_1+u_{i1}x_{i+1}+v_{i1}\overset{\inserted{x_{i+2}+\cdots+x_{n+1}}}{\Sigma_i},\ x_2+u_{i2}x_{i+1}+v_{i2}\Sigma_i,\ \ldots\\  &\cdots\ x_{i-1}+u_{i,i-1}x_{i+1}+v_{i,i-1}\Sigma_i;\\  &u_{i,i}x_{i+1}+v_{ii}\Sigma_i,\ x_{i\deleted{\unsure{+1}}}+u_{i,i+1}x_{i+1}+v_{i,i+1}\Sigma_i;\\  &v_{i,i+2}x_{i+2},\ \ldots,\ v_{i,i+2}x_{n+1}) \end{aligned} \tag*{(17)}`
3. Display: `H_i:\left\{\begin{aligned} u_{i1}x_{i+1}+v_{i1}\Sigma_i&=u_{i2}\unsure{x_{i+2}|x_{i+1}}+v_{i2}\unsure{\Sigma_2|\Sigma_i}=\cdots=u_{i,i-1}x_{i+1}+v_{i,i-1}\Sigma_i=0\\ \inserted{-x_i+}u_{ii}x_{i+1}+v_{ii}\Sigma_i&=\deleted{\unsure{a}}0,\quad x_i+(u_{i,i+1}\deleted{\unsure{x_{i+1}}}-1)x_{i+1}+v_{i,i+1}\Sigma_i=0\\ (v_{i,i+2}-1)x_{i+2}&=\cdots\ (v_{i,i+2}-1)x_{n+1}=0 \end{aligned}\right. \tag*{(18)}`
4. Inline: `\sigma_i`
5. Inline: `i`
6. Inline: `x_i`
7. Inline: `x_{i+1},\ldots,x_{n+1}`
8. Display: `\left\{\begin{aligned} u_{ii}+u_{i,i+1}&=1&v_{i,i}+v_{i,i+1}&=0\\ v_{i,i+2}&=1\\ u_{i1}=\cdots=u_{i,i-1}&=0,&v_{i1}&=\deleted{\unsure{0}}\cdots=v_{i,i-1}=0 \end{aligned}\right. \tag*{(19)}`
9. Inline: `u_{i,i}\inserted{=\lambda_i}`
10. Inline: `v_{i,i}=\mu_i`
11. Inline: `0\leq i\leq n-1`
12. Inline: `1\leq i\leq n-1`
13. Inline: `\sigma_n`
14. Display: `\begin{aligned} \sigma_i(x_{\deleted{\unsure{0}}1},\ldots,x_{n+1})={}&(x_1,\ldots,x_{i-1},\ \lambda_i x_{i+1}+\mu_i\overset{\inserted{x_{i+2}+\cdots+x_{n+1}}}{\Sigma_i},\ x_i\deleted{\unsure{+}}+(1-\lambda_i)x_{i+1}-\mu_i\Sigma_i,\\ &x_{i+2},\ldots,x_{n+1}) \end{aligned} \tag*{(20)}`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{1}`
- deleted 2: `\unsure{+1}`
- deleted 3: `\unsure{v_{i,i+2}}`
- deleted 4: `\unsure{v_{i,i+2}}`
- deleted 5: `\unsure{v_{i,i+2}}`
- deleted 6: `0`
- deleted 7: `\unsure{+1}`
- deleted 8: `\unsure{a}`
- deleted 9: `\unsure{x_{i+1}}`
- deleted 10: `\unsure{0}`
- deleted 11: `sont`
- deleted 12: `\unsure{0}`
- deleted 13: `\unsure{+}`
- inserted 1: `x_{i+2}+\cdots+x_{n+1}`
- inserted 2: `-x_i+`
- inserted 3: `=\lambda_i`
- inserted 4: `(ce dernier pour \unsure{$0\leq i\leq n-1$|$1\leq i\leq n-1$}, pas pour $\sigma_n$)`
- inserted 5: `x_{i+2}+\cdots+x_{n+1}`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T21:08:26+00:00

## Scan 34

Start UTC: 2026-11-17T23:40:41+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:41:02+00:00

### Crop-only words, accents and shapes

Read the three thirds afresh after recovery. “On a.” twice; “ssi”; a small “De” or “D°” before sigma_0; “d’où” beside (22) possibly abbreviated; “Cas général”, “paramètres”, “donc 2n+1 paramètres”; “Cas n-polyèdral”/“polyédral”, accented vowel not settled; “il reste n paramètres μ_i ...”. The range at the top is 1<=i<=n. X_i has no final mu term. X_{i+1} has two oblique cancellation strokes below its outer mu Sigma terms and a positive mu term in its reduced line. Lower lambda_i row has a struck mu. No j is visible in any index. Box (21) uses lambda_i=1, box (22) lambda_0=0. These observations were saved before reopening the page file. The earlier audit attempt ended at the workspace outage and its elapsed time is not counted.

### Comparison and changes

Compared every factor in both coordinate computations: brackets, plus/minus signs, square on (lambda_0−1), and all Sigma subscripts. The first reduced X_i line really stops after its x_{i+1} term; the next reduced line really has +(1−lambda_i)mu_i Sigma_i and coefficient one on x_{i+1}. Kept these apparent computational slips. Checked all i indices against the dotted shapes; there is no j, and zero in sigma_0/lambda_0/mu_0 is distinguished from the i in the preceding unit. X is a plain capital, not a script or double-struck glyph; Sigma is the ordinary summation-style Greek capital. The two diagonals below the mu terms are cancellation marks, not minus signs; both terms remain in deleted macros. The thick blot after lambda_i in the parameter list is retained as a doubtful deleted mu_i. No angled margin prose is present; the lambda conditions at the right belong to the bottom block, not to the archive number.

Changes: comma after x_{i−1} in the first image tuple -> semicolon; added the visible right brace joining the two equivalences before (21). Plain i.e. near (22) -> unsure{i.e.|v.e.}, since the first downstroke is unusually hooked. Rechecked the ending of polyèdral/polyédral without resolving the accent. All other words, underlines, boxes, ranges 0<=i<=n and 0<=i<=n−1, and trailing dots are unchanged. No missing algebraic term has been supplied.

### Formula register checked against the crops

1. Inline: `(1\leq i\leq n)`
2. Display: `\sigma_i^2(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{i-1};X_i,X_{i+1},x_{i+2},\ldots,x_{n+1})`
3. Display: `X_i=\lambda_i\bigl[x_i+(1-\lambda_i)x_{i+1}-\mu_i\Sigma_i\bigr]+\mu_i\Sigma_i =\lambda_i x_i+\lambda_i(1-\lambda_i)x_{i+1}`
4. Display: `\begin{aligned} X_{i+1}&=\bigl[\lambda_i x_{i+1}+\deleted{\mu_i\Sigma_i}\bigr]+(1-\lambda_i)\bigl[x_i+(1-\lambda_i)x_{i+1}-\mu_i\Sigma_i\bigr]-\deleted{\mu_i\Sigma_i}\\ &=(1-\lambda_i)x_i+x_{i+1}+(1-\lambda_i)\mu_i\Sigma_i \end{aligned}`
5. Display: `\left.\begin{aligned} X_i&\equiv x_i\quad\text{ssi}\quad\lambda_i=1\\ X_{i+1}&\equiv x_{i+1}\quad\text{ssi}\quad\lambda_i=1 \end{aligned}\right\} \qquad\boxed{\sigma_i^2=\mathrm{id}\quad\text{ssi}\quad\lambda_i=1} \tag*{(21)}`
6. Inline: `=`
7. Display: `\sigma_0^2(x_1,\ldots,x_{n+1})=(X_1,x_2,\ldots,x_{n+1})`
8. Display: `\begin{aligned} X_1&=1+(\lambda_0-1)\bigl[1+(\lambda_0-1)x_1+(\mu_0-1)\Sigma_0\bigr]+(\mu_0-1)\Sigma_0\\ &=\lambda_0+(\lambda_0-1)^2x_1+\lambda_0(\mu_0-1)\Sigma_0 \end{aligned}`
9. Display: `X_1\equiv x_1\quad\text{ssi}\quad\lambda_0=0\qquad\text{\unsure{i.e.|v.e.}}\quad \boxed{\sigma_0^2=\mathrm{id}\quad\text{ssi}\quad\lambda_0=0} \tag*{(22)}`
10. Display: `\left\{\begin{aligned} &\text{\uline{Cas général} paramètres}\quad \left\{\begin{aligned}\lambda_i\deleted{\unsure{,\mu_i}}&&0\leq i\leq n\\\mu_i&&0\leq i\leq n-1\end{aligned}\right.\\ &\qquad\text{\uline{donc $2n+1$ paramètres}}\\[1ex] &\text{\uline{Cas $n$-\unsure{polyèdral|polyédral}}}\quad(\sigma_i^2=1\quad\text{pour}\quad0\leq i\leq n)\quad \begin{aligned}\lambda_0&=0\\\lambda_i&=1\quad1\leq i\leq n\end{aligned}\\ &\qquad\text{il reste $n$ paramètres}\quad\mu_i\ \ldots \end{aligned}\right.`

### Corrections, cancellations and margins rechecked

- deleted 1: `\mu_i\Sigma_i`
- deleted 2: `\mu_i\Sigma_i`
- deleted 3: `\unsure{,\mu_i}`
- inserted: none.
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:41:40+00:00

## Scan 35

Start UTC: 2026-11-17T23:41:40+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:42:05+00:00

### Crop-only words, accents and shapes

“Partie homogène de σ_0”, “valeurs propres”, “k corps de car. p>0”, “une translation”, “Deux cas”, “i.e.” twice in case b, “translation par (1,0)”, bottom “qui n’est pas l’identité”. Accent on homogène and final identité visible. Top replacement lambda_0−1 is a looped eta/gamma with long descender; alpha_0 is used for mu_0−1. The matrix multiplication has ac′+b′c, then b′=1 above the equality. Repeated powers 2,3,n/m; exponent on the last eta in the nth power is n−1, with a small subscript resembling n rather than 0. Case a has crossed expressions and an overwritten divisibility sign; case b has p not dividing n/m. Sigma_0 at (x,0) carries a struck superscript. The origin calculations at right are wholly struck. The final powers at (x,0) omit the second coordinate except for the first line.

### Comparison and changes

Read the two affine formulas, homogeneous matrix, general triangular product, its specialization, powers 2/3/n, identity equivalence, both cases and all four orbit formulas. Alpha_0 and eta_0/gamma_0 remain distinct; the powers n/m and the doubtful eta_n subscript remain marked. Prime strokes in a′,b′,c′ were checked individually, including b′c in the first product and c+ac′ in the specialization. No i/j indices here: the relevant small signs are 0,1,n, prime and V. The upper-right k note was re-read on its slightly oblique baseline; “corps de car. p>0” remains live. The short dash over the nth matrix is isolated, not a rule across the whole matrix. The lower case labels are compressed, although the a/b letters are clear. No double-struck or script capitals are supported; V is an ordinary V.

Changes: an overline spanning the nth matrix -> a short doubtful dash above the matrix, matching the ink's extent. Added the possible reading (eta_0^n=1) to the deeply struck condition in case a; retained (eta_0≠1) first because its left-to-right strokes fit better. Marked the compressed “Cas a)” and “Cas b)” as unsure. No change to the positive-characteristic restriction, to p not dividing n in case b, or to the coordinate omissions in sigma_0^2 and sigma_0^3. Checked that all visible earlier cancelled determinant/linear-part expressions, the overtyped matrix entry, and the crossed origin evaluations remain deleted. The last “qui n’est pas l’identité” is live; there is no cancellation through it.

### Formula register checked against the crops

1. Display: `\left\{\begin{aligned} \sigma_0(x,y)&=(1+(\lambda_0-1)x+(\mu_0-1)y,y)=(1+(\lambda_0-1)x+\alpha_0y,y)=(1+\unsure{\eta_0|\gamma_0}x+\alpha_0y,y)\\ \sigma_1(x,y)&=(\lambda_1y\deleted{\unsure{+}},x+(1-\lambda_1)y) \end{aligned}\right.`
2. Inline: `k`
3. Inline: `p>0`
4. Inline: `\sigma_0`
5. Display: `\begin{pmatrix}\deleted{\unsure{\lambda_0-1}}\eta_0&\alpha_0\\0&1\end{pmatrix}`
6. Inline: `\det(t\,\mathrm{id}-\sigma_{0V})=`
7. Inline: `1`
8. Inline: `\lambda_0-1=\eta_0`
9. Display: `\deleted{\unsure{\sigma_{0V}}}\quad \begin{pmatrix}a&c\\0&b\end{pmatrix} \begin{pmatrix}a'&c'\\0&b'\end{pmatrix} =\begin{pmatrix}aa'&ac'+b'c\\0&bb'\end{pmatrix} \overset{\text{si }b'=1}{=}\begin{pmatrix}aa'&c+ac'\\0&b\end{pmatrix}`
10. Display: `\begin{pmatrix}a&c\\0&b\end{pmatrix} \begin{pmatrix}\eta_0&\alpha_0\\0&1\end{pmatrix} =\begin{pmatrix}\eta_0a&c+\alpha_0a\\0&b\end{pmatrix}`
11. Display: `\begin{pmatrix}\eta_0&\alpha_0\\0&1\end{pmatrix}^{2} =\begin{pmatrix}\eta_0^2&\alpha_0+\deleted{\unsure{\alpha}}\unsure{\alpha_0\eta_0}\\0&1\end{pmatrix}`
12. Display: `\begin{pmatrix}\eta_0&\alpha_0\\0&1\end{pmatrix}^{3} =\begin{pmatrix}\eta_0^3&\alpha_0(1+\eta_0+\eta_0^2)\\0&1\end{pmatrix}`
13. Display: `\overset{\unsure{-}}{\begin{pmatrix}\eta_0&\alpha_0\\0&1\end{pmatrix}}^{\unsure{n|m}} =\begin{pmatrix}\eta_0^n&\alpha_0(1+\eta_0+\cdots+\unsure{\eta_n^{n-1}|\eta_0^{n-1}})\\0&1\end{pmatrix}`
14. Display: `\sigma_{0V}^n=1\quad\Longleftrightarrow\quad \left\{\begin{aligned} \eta_0^n&=1\quad\text{i.e.}\quad(\unsure{\eta_0|\eta}-1)(1+\eta_0+\cdots+\eta_0^{n-1})=0\\ \deleted{\unsure{\alpha_0(1+}}&&\alpha_0(1+\eta_0+\cdots+\eta_0^{n-1})=0 \end{aligned}\right.`
15. Display: `\Updownarrow\qquad\sigma_0^n\text{ une translation}`
16. Display: `\left\{\begin{aligned} \text{a)}\quad&\deleted{\unsure{\eta_0^n}}1+\eta_0+\cdots+\eta_0^{n-1}=0\quad\text{i.e.}\quad \deleted{\unsure{(\eta_0\ne1)|(\eta_0^n=1)}}\eta_0^n=1\\ &\hspace{7em}\text{et }(\eta_0\ne1\text{ ou }p\deleted{\unsure{\nmid}}\mid n)\\ \text{b)}\quad&\eta_0=1,\ \alpha_0=0\quad[\text{i.e. }\sigma_{0V}=\mathrm{id}\text{ i.e. }\sigma_0\text{ est la}\\ &\qquad\text{translation par }(1,0)]\text{ et }p\nmid n \end{aligned}\right.`
17. Display: `\sigma_0^n(0)=?\qquad \begin{aligned} &\deleted{\sigma_0(0)=(1,0)}\\ &\deleted{\unsure{\sigma_0^2(0)=(1+\eta_0}} \end{aligned}`
18. Display: `\begin{aligned} \sigma_0^{\deleted{\unsure{1}}}(x,0)&=(1+\eta_0x,0)\\ \sigma_0^2(x,0)&=1+\eta_0+\eta_0^2x\\ \sigma_0^3(x,0)&=1+\eta_0+\eta_0^2+\eta_0^3x\\ &\cdots\\ \sigma_0^n(x,0)&=1+\eta_0+\cdots+\eta_0^{n-1}+\eta_0^n x =\left\{\begin{aligned} &\text{\unsure{Cas a)}}\quad\eta_0^n x=x\\ &\text{\unsure{Cas b)} translation par }(n,0)\\ &\qquad\text{qui n'est pas l'identité.} \end{aligned}\right. \end{aligned}`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{+}`
- deleted 2: `\unsure{\lambda_0-1}`
- deleted 3: `\unsure{$\det(t\,\mathrm{id}-\sigma_{0V})=$}`
- deleted 4: `\unsure{\sigma_{0V}}`
- deleted 5: `\unsure{\alpha}`
- deleted 6: `\unsure{\alpha_0(1+}`
- deleted 7: `\unsure{\eta_0^n}`
- deleted 8: `\unsure{(\eta_0\ne1)|(\eta_0^n=1)}`
- deleted 9: `\unsure{\nmid}`
- deleted 10: `\sigma_0(0)=(1,0)`
- deleted 11: `\unsure{\sigma_0^2(0)=(1+\eta_0}`
- deleted 12: `\unsure{1}`
- inserted: none.
- margin 1: `$k$ corps de car. $p>0$`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:43:05+00:00

## Scan 36

Start UTC: 2026-11-17T23:43:05+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:43:33+00:00

### Crop-only words, accents and shapes

“On trouve donc”, “donc”, “Ordre de”, “sauf si”, “auquel cas”, “transvection”, “qui est d’ordre 1 ssi α_0=0, sinon d’ordre p”, underlined “Cas impropre”, “d’ordre infini”, “sinon”. Top exceptional case a visually says α_0=1 and sigma_0=id, while b says α_0≠1: do not change by algebra. The inserted i.e. det sigma_{0V}=1 points after eta_0=1. Exponent on sigma_0 resembles ell/epsilon. Below a horizontal divider, sigma_1 squared has x,y separated by commas, two long lines; characteristic polynomial t²−(1−lambda_1)t−lambda_1; extra factorization and eta/eta′ calculations are crossed through. Slanted lower-left word looks “alors”/“choix” and is enclosed with cancelled work. The final identity line has a short crossed or not-equal mark immediately before “identité”; this needs zoom before deciding whether word or sign. The last exceptional condition looks delta=1, although the preceding live eigenvalue is eta_1. These are independent crop notes.

### Comparison and changes

Full two-unit comparison. Top sigma_0 exponent ell/epsilon, the geometric-sum endpoint ell−1, all zeros on eta_0/alpha_0/sigma_0 and V subscripts were rechecked. The case split visibly reads alpha_0=1 and alpha_0≠1, whereas the preceding parenthesis reads alpha_0=0: retained, with no harmonization. The p-divisibility clauses and p² order claim lie in crossed work; sigma_0^p=id immediately to the right is live. The lower coordinate calculation preserves both parenthesized pairs and the polynomial lambda_1²−lambda_1+1. The characteristic polynomial's cancelled alternative contains delta, not eta_1. The eta/eta′ relations and fractions are retained as struck; prime strokes and n exponents were inspected separately. The isolated x=lambda_1 y remains live beside the struck y=. All i-like strokes here are numeral 1, not i/j. k has an ordinary star; none of the capitals is script/double-struck.

Read the lower-left oblique word after rotating its crop: still unsure{alors|choix}, favouring alors from the initial a and tall l. The enclosing line does not itself strike the word. Rechecked the added determinant condition and its attachment after eta_0=1. Changes: “au pt.” -> unsure{au pt.}, because its last strokes are compressed; wrapped the replacement eigenvalue line 1,−lambda_1=eta_1 in inserted, following its curved connector to the struck eta,eta′. At the very bottom, deleted{unsure{non}} -> unsure{deleted{non}|ne}: the mark could instead be a live inequality sign, so cancellation status is explicitly doubtful. The words identité and d’ordre remain live. No other changes, including the exceptional delta=1 despite the nearby renamed eta_1.

### Formula register checked against the crops

1. Display: `\sigma_0^{\unsure{\ell|\varepsilon}}=\mathrm{id}\quad\Longleftrightarrow\quad 1+\unsure{\eta_0|\gamma_0}+\cdots+\eta_0^{\ell-1}=0`
2. Inline: `\sigma_0=`
3. Inline: `\eta_0\in k^*`
4. Inline: `\eta_0=1`
5. Inline: `\det\sigma_{0V}=1`
6. Inline: `\sigma_{0V}`
7. Inline: `\begin{pmatrix}1&\alpha_0\\0&1\end{pmatrix}`
8. Inline: `1`
9. Inline: `\alpha_0=0`
10. Inline: `p`
11. Display: `\eta_0=1\quad\left\{\begin{aligned} \text{a)}\quad&\alpha_0=1\quad\sigma_0=\mathrm{id}\qquad\text{\uline{cas impropre}}\\ \text{b)}\quad&\alpha_0\ne1\quad\left\{\begin{aligned} p=0\quad&\sigma_{0V}\text{ d'ordre infini, a fortiori }\sigma_0\text{ d'o. inf.}\\ p>0\quad&\sigma_{0V}\text{ d'ordre }p,\quad\sigma_0^p=\deleted{\text{translation}}\inserted{\text{\unsure{au pt.}}}\\ &\deleted{\unsure{(n,0)}}\quad\left\{\begin{aligned} &\deleted{p\mid n\ \Longrightarrow}\ \sigma_0^p=\mathrm{id}\\ &\deleted{p\nmid n\quad\sigma_0\text{ d'ordre }p^2} \end{aligned}\right. \end{aligned}\right. \end{aligned}\right.`
12. Display: `\begin{aligned} \sigma_1^2(x,y)&=(\lambda_1x+\lambda_1(1-\lambda_1)y,(1-\lambda_1)x+(\lambda_1+(1-\lambda_1)^2)y)\\ &=(\lambda_1x+\lambda_1(1-\lambda_1)y,(1-\lambda_1)x+(\lambda_1^2-\lambda_1+1)y) \end{aligned}`
13. Display: `\sigma_1=\begin{pmatrix}0&\lambda_1\\1&1-\lambda_1\end{pmatrix}`
14. Display: `\det(t\,\mathrm{id}-\sigma_1)=t^2-(1-\lambda_1)t-\lambda_1 =\deleted{t^2-(1+\delta)t+\delta}`
15. Inline: `\eta,\eta'`
16. Inline: `1,-\lambda_1=\deleted{\delta}\eta_1`
17. Display: `\deleted{\left\{\begin{aligned}-\lambda_1&=\eta\eta'\\1-\lambda_1&=\eta+\eta'\end{aligned}\right.} \qquad\deleted{-\lambda_1=\delta_1=\delta}`
18. Display: `\deleted{\left\{\begin{aligned}\eta\eta'&=\delta\\\eta+\eta'&=1+\delta\end{aligned}\right.}`
19. Display: `\deleted{\eta^{\unsure{n|m}}=\eta'{}^n=1}\quad\deleted{\Longrightarrow\delta^n=1}`
20. Display: `\deleted{\frac{\eta}{\delta}}\qquad\deleted{\frac{\eta'}{\delta}}\qquad \deleted{\frac{\eta}{\delta}}\qquad\deleted{\frac{\eta'}{\delta}}\qquad \deleted{y=}\quad x=\lambda_1y`
21. Display: `\deleted{\unsure{\delta\ne1}}`
22. Inline: `\sigma_1=`
23. Inline: `\eta_1\in k^*`
24. Inline: `\delta=1`
25. Inline: `\lambda_1=-1`
26. Display: `\sigma_1(x,y)=(-y,x+2y)\quad\text{transvection}`
27. Inline: `\ne`
28. Inline: `p=0`
29. Inline: `p`

### Corrections, cancellations and margins rechecked

- deleted 1: `\text{translation}`
- deleted 2: `\unsure{(n,0)}`
- deleted 3: `p\mid n\ \Longrightarrow`
- deleted 4: `p\nmid n\quad\sigma_0\text{ d'ordre }p^2`
- deleted 5: `t^2-(1+\delta)t+\delta`
- deleted 6: `\unsure{$\eta,\eta'$}`
- deleted 7: `\delta`
- deleted 8: `\left\{\begin{aligned}-\lambda_1&=\eta\eta'\\1-\lambda_1&=\eta+\eta'\end{aligned}\right.`
- deleted 9: `-\lambda_1=\delta_1=\delta`
- deleted 10: `\left\{\begin{aligned}\eta\eta'&=\delta\\\eta+\eta'&=1+\delta\end{aligned}\right.`
- deleted 11: `\eta^{\unsure{n|m}}=\eta'{}^n=1`
- deleted 12: `\Longrightarrow\delta^n=1`
- deleted 13: `\frac{\eta}{\delta}`
- deleted 14: `\frac{\eta'}{\delta}`
- deleted 15: `\frac{\eta}{\delta}`
- deleted 16: `\frac{\eta'}{\delta}`
- deleted 17: `y=`
- deleted 18: `\unsure{\delta\ne1}`
- deleted 19: `non`
- inserted 1: `i.e. $\det\sigma_{0V}=1$`
- inserted 2: `\text{\unsure{au pt.}}`
- inserted 3: `$1,-\lambda_1=\deleted{\delta}\eta_1$`
- margin 1: `\unsure{alors|choix}`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:44:34+00:00

## Scan 37

Start UTC: 2026-11-17T23:44:35+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:44:53+00:00

### Crop-only words, accents and shapes

Sparse sheet: three transformation formulas and two short assertions, with the middle/bottom thirds otherwise blank. “Valeurs propres de σ_i:”, “1 de multiplicité n−1”, “ordre de σ_i =? ordre de η_i ∈ k* si η_i≠1”. Question mark is above the equality. First two formulas use Sigma_0/Sigma_i; last sigma_n subscript has a blot. General formula −eta_i x_{i+1}+(1+alpha_i)Sigma_i, next coordinate x_i+(eta_i+1)x_{i+1}−(1+alpha_i)Sigma_i. At left 1<=i<=n−1. Long lower horizontal line and left bracket enclose the formulas; no diagonal cancellation through this block. The only accents are in “multiplicité” and “propres” is unaccented.

### Comparison and changes

All three coordinate formulas were compared coordinate by coordinate. In the middle formula the positions i−1, i+1, i+2 and n+1 were checked separately; the letter with a dot is i, not j. The zero-index formula has +alpha_0 Sigma_0, whereas the internal formula has +(1+alpha_i)Sigma_i, retained. The last formula's negative eta_n and later +(1+eta_n) are both visible. The doubtful deleted subscript after n remains because ink is blotted at precisely that position. The formula bracket is enclosing, not cancelling. The reported multiplicity is n−1 and the equality in the final order statement carries a question mark; both retained without mathematical correction. Sigma is ordinary Greek; k and the starred exponent are plain; no script/double-stroke candidate. No margins, other cancellations or insertions were found in the two mostly blank crops. No change.

### Formula register checked against the crops

1. Display: `\begin{array}{|l} \sigma_0(x_1,\ldots,x_{n+1})=(1+\unsure{\eta_0|\gamma_0}x_1+\alpha_0\Sigma_0,x_2,\ldots,x_{n+1})\\ \quad\cdots\\ \begin{aligned} 1\leq i\leq n-1\qquad\sigma_i(x_1,\ldots,x_{n+1})={}&(x_1,\ldots,x_{i-1},-\eta_i x_{i+1}+(1+\alpha_i)\Sigma_i,\ x_i+(\eta_i+1)x_{i+1}-(1+\alpha_i)\Sigma_i,\\ &x_{i+2},\ldots,x_{n+1}) \end{aligned}\\ \quad\cdots\\ \sigma_{n\deleted{\unsure{+1}}}(x_1,\ldots,x_{n+1})=(x_1,\ldots,x_{n-1},-\eta_nx_{n+1},x_n+(1+\eta_n)x_{n+1})\\\hline \end{array}`
2. Inline: `\sigma_i`
3. Display: `\left\{\begin{aligned}&1\text{ de multiplicité }n-1\\&\eta_i\end{aligned}\right.`
4. Inline: `\sigma_i\overset{?}{=}`
5. Inline: `\eta_i\in k^*`
6. Inline: `\eta_i\ne1`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{+1}`
- inserted: none.
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:45:08+00:00

## Scan 39

Start UTC: 2026-11-17T23:45:08+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:45:24+00:00

### Crop-only words, accents and shapes

Cover only. Small pencil “(9 p)” upper middle; upper-right struck title seems “Th. des Topos” and a separate scratched numeral. Live title uses two quote strokes around “étude locale”, then “des n-polyèdres et des n-cartes”, followed by “(vieille rédaction)”. The word polyèdres is reduced at the right edge. The first é of étude is visible; rédaction has an acute accent. No date. All remaining surfaces blank except archive 38.

### Comparison and changes

Re-read all cover ink including the pencilled parenthesis and the separately scratched numeral. The dark hatching crosses the earlier title only; the étude locale title and vieille rédaction remain live. The quotation marks are paired double strokes, not guillemets. The only mathematical inline items are the two n prefixes; no indexed formula, script or double-struck letter appears. The pencil page count is kept uncertain, with unknown hand in the inventory. Change: added “Th. de Topos” as an alternative to “Th. des Topos” because a plural s is not individually separable from the cancellation. No other change. The visible 38 is the archive number, not a manuscript page number.

### Formula register checked against the crops

1. Inline: `n`
2. Inline: `n`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{Th. des Topos|Th. de Topos}`
- deleted 2: `\unsure{7}`
- inserted: none.
- margin 1: `\unsure{(9 p)}`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:45:41+00:00

## Scan 40

Start UTC: 2026-11-17T23:45:41+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:46:15+00:00

### Crop-only words, accents and shapes

Opening independently reads “Soit ... une carte combinatoire C de moquette E — un G_n-ensemble — où”, not de rang n. “Rappelons”, “i-facettes”, “éléments de l’ens”, “Considérons, pour f_i∈D_i fixé, l’ens des facettes f′_j de C ... <f_i”, “de dim j<i”, “provienne d’un él. de E”. Dense corrections around E−(i) and G_n+(i). Generated subgroups note above Considérons: “sont engendrés respectiv[...], σ_0 ... σ_{i−1} et σ_{i+1}, ... σ_n”. Lower: “et sauf erreur c’est un (i−1)-... polyèdre”, then “i.e. σ_0, ... σ_{i−1} et les produits de tels éléments qui commutent opèrent sans pts fixes dans E−(i).” Underlined transition has “Ainsi E−(i)” and “les fibres de” overlapping with “correspond:”. Bottom “comp. connexes correspondent aux él. de D_i i.e. aux i-facettes f_i. Soit Π−_{f_i} ... Ces j-facettes sont”. The Pi shape has two legs joined by a long top; a Gamma reading would miss the right leg. Accents: combinatoire, éléments/él., Considérons, fixé, opèrent. Plus/minus superscripts have overwriting and require magnification. At least two cancelled lines lie below the quotient diagram.

### Comparison and changes

Read the full group presentation, facet quotient, both generated subgroups, the quotient map, the operator-group isomorphism and every inline facet/index expression. The commutation condition is j>=i+2; the facet condition is j<i. The small hat excludes sigma_i, not sigma_j. f′_j contains both a prime and a descender on j; f_i has neither. E and G carry overwritten opposite signs in the quotient map, retained as cancellation before the final signs. Later G_n+(i)≃G_{i−1} really has a plus in the crop; did not correct it from the expected group action. D is rounded but sometimes triangular enough for Delta; first-page uncertainty retained. C is a plain open C. The lower Pi has two legs: not Gamma or a script T. All added lines and the late inserted definition were followed to their attachment points. The underlined transition is especially difficult: the overlapping “Ainsi E−(i)”, “les fibres de” and “correspond:” are preserved without silently rewriting the sentence. No typed text or double-struck capitals.

Changes: “de rang n, E” -> “de moquette E” from the visible m-o-q-u-e-t-t-e; this removes an invented rank phrase. “des f′ facettes” -> “des facettes inserted{f′}”, following its placement above facettes. “proviennent” -> unsure{provienne|proviennent}, since final nt is not fully resolved. In the struck line, “flèche sur ... illegible{3}” -> unsure{flèche vers|flèche sur} ... unsure{avec ces|avec les}; the recovered letter shapes allow attempted readings instead of an unreadability gap. Added faux; as an alternative to pur; in the small insertion. Gamma_{f_i} -> Pi_{f_i} from its right-hand leg. All other uncertain words and the deeply cancelled preliminary formula remain explicitly doubtful. Rechecked the live words next to the striking lines: “c’est un ens.”, “et sauf erreur”, the action without fixed points and the final “Ces j-facettes sont” stay live.

### Formula register checked against the crops

1. Inline: `X`
2. Inline: `C`
3. Inline: `E`
4. Inline: `G_n`
5. Display: `\begin{aligned} G_n=\{\sigma_0,\ldots,\sigma_n\mid{}&\sigma_0^2=\cdots=\sigma_n^2=1,\\ &\sigma_i\sigma_j=\sigma_j\sigma_i\quad\text{si }j\geq i+2\} \end{aligned}`
6. Inline: `i`
7. Display: `\unsure{D_i|\Delta_i}=E/(\sigma_0,\ldots,\widehat{\sigma_i},\ldots,\sigma_n) =E/(G_n^{\deleted{\unsure{+}}-}(i)\times G_n^+(i))`
8. Inline: `G_n^-(i)\subset G_n`
9. Inline: `G_n^+(i)\subset G_n`
10. Inline: `\sigma_0,\ldots,\sigma_{i-1}`
11. Inline: `\sigma_{i+1},\ldots,\sigma_n`
12. Inline: `f_i\in D_i`
13. Inline: `f'`
14. Inline: `C`
15. Inline: `<f_i`
16. Inline: `j<i`
17. Inline: `(f'_j,f_i)`
18. Inline: `E`
19. Inline: `E(i)^+`
20. Display: `E^{\deleted{+}-}(i)=E/G_n^{\deleted{-}+}(i)\longrightarrow D_i`
21. Inline: `D`
22. Inline: `E^+(i)=E/G_n`
23. Inline: `G_n^+(i)\simeq G_{i-1}`
24. Inline: `D_i`
25. Inline: `D_i`
26. Inline: `(i-1)`
27. Inline: `\sigma_0,\ldots,\sigma_{i-\unsure{1}}`
28. Inline: `E^-(i)`
29. Inline: `E^-(i)`
30. Inline: `(i-1)`
31. Inline: `D_i`
32. Inline: `i`
33. Inline: `f_i`
34. Inline: `\Pi_{f_i}^{\unsure{-}}`
35. Inline: `(i-1)`
36. Inline: `f_i`
37. Inline: `f_i`
38. Inline: `j`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{$X$}`
- deleted 2: `\unsure{+}`
- deleted 3: `\unsure{dont un qui}`
- deleted 4: `donc`
- deleted 5: `\unsure{$E(i)^+$}`
- deleted 6: `+`
- deleted 7: `-`
- deleted 8: `\unsure{``$D$ augmenté i''}`
- deleted 9: `\unsure{$E^+(i)=E/G_n$}`
- deleted 10: `et la \unsure{flèche vers|flèche sur} $D_i$ est \unsure{compatible} \unsure{avec ces|avec les} \unsure{opérations}`
- deleted 11: `\unsure{$D_i$ est un quotient.}`
- deleted 12: `\unsure{est}`
- deleted 13: `\unsure{poly}`
- deleted 14: `qui`
- deleted 15: `la fibre de $f_i$`
- inserted 1: `$C$`
- inserted 2: `$G_n^-(i)\subset G_n$, $G_n^+(i)\subset G_n$ sont engendrés respectiv. par $\sigma_0,\ldots,\sigma_{i-1}$ et $\sigma_{i+1},\ldots,\sigma_n$.`
- inserted 3: `$f'$`
- inserted 4: `\unsure{pur;|faux;}`
- inserted 5: `\uline{correspond:}`
- inserted 6: `la \deleted{\unsure{poly}} $(i-1)$-carte connexe \deleted{qui} \unsure{déf.} par $f_i$`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:47:32+00:00

## Scan 41

Start UTC: 2026-11-17T23:47:33+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:48:00+00:00

### Crop-only words, accents and shapes

Continuation: “les él. de” repeated, “qui ... s’envoient dans f_i∈D_i”, “drapeaux de type (j,i)”, “composante de ... dim i”, “Plus gén.”. Index range for j_1,...,j_p is cramped at right edge. “On l’appelle le ... bord ... de la facette f_i, noté ∂f_i”; carte is inserted above bord. “Dualement, considérons”, “sur lequel G_n+(i)≃G_{n−i−1} opère”, “le quotient étant D_i. On trouve une moquette ... (sauf erreur)”. Added “de (n−i−1)-cartes”. Quotes around “sont”. Drapeaux type (i,i+j+1), added “de Π”. Bottom insertion: “un drapeau d_{ij} de type (i,j), défini par”; underlying “deux facettes”; f_i<f_j and revised range j>=i+2 over struck i<j. Cancelled E(i,j) quotient at bottom. Pi has two legs here too. Hat indices j and i are distinct; plus/minus on E/G also distinct.

### Comparison and changes

Both quotient formulas checked: hat on sigma_j in the first, hats on sigma_j and sigma_i in the second; upper endpoint i−1 in the first denominator, n in the second. Checked all f_i, f′_j, j_1, j_p, (j,i), (j_1,...,j_p,i), i+j+1 and j>=i+2 positions; the handwritten descenders distinguish j from i. The edge of the crop still leaves the upper bound i−1/i uncertain. In the dual construction E+ divides by G−, while G+ acts: signs retained. Pi, partial, E, D and G are ordinary handwritten forms; D/Delta remains marked at its first page occurrence. The quoted “sont” is not a cancellation. The long line under the final insertion is its connector; the original two-facet formulation and the quotient formula below are struck.

Changes: restored the omitted small d_{ij} above “drapeau”, nested within the longer inserted clause. “définissant” -> unsure{défini par|définissant}; the right-edge strokes are incomplete. Duellement -> unsure{Dualement|Duellement}, preserving uncertainty about the middle vowel. The bord clause now reads unsure{le|la}, with inserted underlined carte and the quotes attached to bord as on the crop; notée -> unsure{notée|noté}. The cancellation “au delà” was inspected at larger size and remains doubtful; no replacement by an expected word. No other changes. All other inserted/cancelled spans in the register were compared with their nearby live words.

### Formula register checked against the crops

1. Display: `E^-_{\deleted{\unsure{f}}}(i)_{f_i}/(\sigma_0,\ldots,\widehat{\sigma_j},\ldots,\sigma_{i-1}),\quad\text{i.e.}`
2. Display: `E^-(i)/(\sigma_0,\ldots,\widehat{\sigma_j},\ldots,\sigma_{i-1}) \simeq E/(\sigma_0,\ldots,\widehat{\sigma_j},\ldots,\widehat{\sigma_i},\ldots,\sigma_n)`
3. Inline: `f_i\in\unsure{D_i|\Delta_i}`
4. Inline: `(j,i)`
5. Inline: `i`
6. Inline: `f_i`
7. Inline: `(j_1<\cdots<j_p)`
8. Inline: `0\leq j_1,\deleted{\unsure{j}}j_p\leq\unsure{i-1|i}`
9. Inline: `(j_1,\ldots,j_p,i)`
10. Inline: `\Pi`
11. Inline: `i`
12. Inline: `f_i`
13. Inline: `f_i`
14. Inline: `\partial f_i`
15. Display: `E^+(i)=E/G_n^-(i)\inserted{=D_{i,i+1,\ldots,n}}\longrightarrow D_i`
16. Inline: `G_n^+(i)\simeq\deleted{\unsure{n-i}}G_{n-i-1}`
17. Inline: `D_i`
18. Inline: `(n-i-1)`
19. Inline: `j`
20. Inline: `(0\leq j\leq n-i-1)`
21. Inline: `(i,i+j+1)`
22. Inline: `\Pi`
23. Inline: `i`
24. Inline: `f_i`
25. Inline: `d_{ij}`
26. Inline: `(i,j)`
27. Display: `f_i<f'_j\qquad(\deleted{i<j}\inserted{j\geq i+2})`
28. Display: `\deleted{\unsure{E(i,j)=E/(\sigma_0-\sigma_{i-1};\sigma_{j+1},\ldots,\sigma)}}`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{f}`
- deleted 2: `\unsure{au delà}`
- deleted 3: `degré`
- deleted 4: `\unsure{j}`
- deleted 5: `dont`
- deleted 6: `\unsure{n-i}`
- deleted 7: `dont`
- deleted 8: `deux facettes`
- deleted 9: `i<j`
- deleted 10: `\unsure{E(i,j)=E/(\sigma_0-\sigma_{i-1};\sigma_{j+1},\ldots,\sigma)}`
- inserted 1: `\uline{carte}`
- inserted 2: `=D_{i,i+1,\ldots,n}`
- inserted 3: `de $(n-i-1)$-cartes`
- inserted 4: `de $\Pi$`
- inserted 5: `un drapeau \inserted{$d_{ij}$} de type $(i,j)$, \unsure{défini par|définissant}`
- inserted 6: `$d_{ij}$`
- inserted 7: `j\geq i+2`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:48:58+00:00

## Scan 42

Start UTC: 2026-11-17T23:48:58+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:51:35+00:00

### Crop-only words, accents and shapes

Top: “et l’application” precedes the arrow; “Le groupe engendré par”, “avec comme quotient”, “Sans doute il opère cartographiquement” (last word underlined), “et on trouve une”. Middle: “les composantes connexes correspondent”, small added “sur Π(dᵢⱼ)”; “les facettes de dim h”; “Cas particuliers”, “un peu idiot” (compressed final word); “polygone, d’où un invariant” (underlined invariant). Bottom: two abandoned beginnings “On s’intéresse au” and “Introduisons”; “Formellement” heavily compressed, plus overwritten short material around the two Π expressions. Doublestriking is visible in N with bar and star; Π has two legs throughout. i has no descender, j has one, including dᵢⱼ and j−i−2; the h+1 in the middle flag is crowded. The margin starts 0≤i, and the final n+1 is crowded at the edge. No date.

### Comparison and changes

Read all three thirds again, with enlarged middle insertion and heavily cancelled bottom. Every displayed and inline formula is registered below. In E(i,j), the first divisor ends at i−1, the second starts at j+1; the next live operators start at i+1 and end at j−1. Kept E/G⁻(i)×G⁺(j) without adding grouping parentheses. The margin begins 0, with i≤i+2; its last n+1 remains doubtful rather than being corrected. The flag middle index is i+h+1 and its added underbrace inequality is i+1≤ [blank] ≤j−1; no term has been supplied into the source blank. D/Delta is marked at first occurrence; Π has two vertical legs, N has two strokes, an overbar and a star. The two case lines carry i+2 and i+3. The roof over the o in polygône is retained. Changes: “un invariant” -> “un \uline{invariant}”; Π⁻(fᵢ) -> Π with unsure minus/equality superscript, because the mark is thick and layered; added the small cancelled “au” below the first bottom Π phrase; final Π⁺(fᵢ) -> Π⁺(unsure f^i|f_i|f′), because the small mark is high and could be a raised i or prime. The first candidate follows the local height, not the earlier fᵢ. All six cancelled fragments were revisited; the crowded right-hand cancellation and the material erased after −1,i remain low-confidence tentative readings. “Formellement” remains live between two struck beginnings. The insertion “sur Π(dᵢⱼ)” is above “les facettes”, not a new main paragraph. The large bottom strokes cancel only the recorded fragments, not the following live definitions. No other change.

### Formula register checked against the crops

1. Display: `E(i,j)=E/(\sigma_0,\ldots,\sigma_{i-1};\sigma_{j+1},\ldots,\sigma_n) =E/G^-(i)\times G^+(j)=\unsure{D_{i,i+1,\ldots,j}|\Delta_{i,i+1,\ldots,j}}`
2. Display: `E(i,j)\longrightarrow D_{i,j}\ \deleted{\unsure{D_j}}`
3. Inline: `0\leq i\leq i+2\leq j\leq\unsure{n+1}`
4. Inline: `\sigma_{i+1},\ldots,\sigma_{j-1}`
5. Inline: `E(i,j)`
6. Inline: `D_{i,j}`
7. Inline: `(j-i-2)`
8. Inline: `d_{ij}\in D_{ij}`
9. Inline: `\Pi(d_{ij})`
10. Inline: `h`
11. Inline: `(0\leq h\leq j-i-2)`
12. Inline: `(i,\underbrace{i+h+1}_{\inserted{i+1\leq\ \leq j-1}},j)`
13. Inline: `d_{ij}`
14. Display: `\begin{aligned} j=i+2&\quad\text{\unsure{un peu idiot}}\\ j=i+3&:\quad\text{on trouve un polygône, d'où}\\ &\qquad\text{un \uline{invariant}}\quad\unsure{p|\rho}(d_{ij})\in\overline{\mathbb{N}}^* \end{aligned}`
15. Display: `(\text{où }1\leq p(d_{ij})\leq+\infty)`
16. Inline: `\Pi^{\unsure{-|=}}(f_i)`
17. Inline: `\Pi(d_{-1,i\deleted{\unsure{f_i}}})`
18. Inline: `d_{-1,i}`
19. Inline: `f_i`
20. Inline: `\Pi`
21. Inline: `(-1)`
22. Inline: `\Pi^+(\unsure{f^i|f_i|f'})`
23. Inline: `\Pi(d_{i,n+1})`
24. Inline: `d_{i,n+1}`
25. Inline: `f_i`

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{D_j}`
- deleted 2: `On \unsure{s'intéresse au}`
- deleted 3: `Introduisons`
- deleted 4: `\unsure{au}`
- deleted 5: `\unsure{f_i}`
- deleted 6: `\unsure{pour $\Pi$}`
- deleted 7: `\unsure{$(-1)$-facettes}`
- deleted 8: `par`
- inserted 1: `sur $\Pi(d_{ij})$`
- inserted 2: `i+1\leq\ \leq j-1`
- margin 1: `$0\leq i\leq i+2\leq j\leq\unsure{n+1}$`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:52:17+00:00

## Scan 43

Start UTC: 2026-11-17T23:52:17+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:52:35+00:00

### Crop-only words, accents and shapes

“essentiels sont”; a) “Les” then ν(Π⁻ with f₂ below); the naming word before p₀ is compressed (possibly “dénoté” or “noté”); each “régulier” is underlined. b) “notés”; c) the tiny word before “noté” may be “ici”. “Supposons Π régulier, je dis que”. Right margin: “vrai tout au moins dans le cas des géométries d’incidences (``polyèdres''...)”, with “régularité” underlined in following main text. “En effet,” then a scribbled cancellation before “sous hypoth. de régularité”. Below: “est l’ordre de σ₀σ₁ opérant sur”; added quotient equality above E⁻(2) with subscript f₂; crossed-out next attempted order statement. Last gₓ has small cancelled material before and after it. Bottom scratch consists of indices and inequalities, no arrows. No double-struck capitals: E is angular; G has a curve with interior cross-stroke; Π is unmistakably two-legged. ν/v and p/ρ shapes remain close.

### Comparison and changes

Read the three thirds in order, then enlarged both naming words and the cancelled lower formula. Every formula is listed below. The initial index is f₂, the last in (c) fₙ₋₂; b has d₀,₃, d₁,₄ and dₙ₋₃,ₙ, while the named parameters end at pₙ₋₂. Kept the extra grouping parentheses of the last term in b. In the order list p₀ has an equality but p₁ and pₙ₋₁ have colons; initial capital “Ordre” is retained at the last line. All σ products checked independently. ν/v and p/ρ remain marked on first occurrence. Ordinary E and G have no independent doubled stroke; Π has two legs. The margin is read horizontally and says “vrai tout au moins...” with its quoted “polyèdres”; it is a qualification, not cancelled. The source “En effet” is live despite the adjacent scribble over Π. Changes: dénoté -> unsure dénoté at a; noté -> unsure dénoté|noté at c (there is an initial looped cluster before noté); régularité -> underlined régularité. In the cancelled ν(Π(dᵢ,ᵢ₊₃)) added the small raised loop as unsure a|o on d; the mark lies above the main crossing zigzag and is not secure. The quotient inserted above E⁻(2) has Gₙ⁺(2) and the whole parenthesis has subscript f₂. Both small cancellations around gₓ were inspected; neither is treated as live multiplication. The bottom index scratch is reproduced as an array, preserving the displaced i−1, i, j+1, last i, and unsure ≥|= below j. No omitted equation is inferred from that scratch. No other change.

### Formula register checked against the crops

1. Inline: `\unsure{\nu|v}(\Pi^-_{f_2})`
2. Inline: `\unsure{p|\rho}_0(\Pi)`
3. Inline: `\Pi`
4. Inline: `\nu(\Pi(d_{0,3})),\nu(\Pi(d_{1,4}))\cdots(\nu(\Pi(d_{n-3,n})))`
5. Inline: `p_1(\Pi),p_2(\Pi),\ldots,p_{n-2}(\Pi)`
6. Inline: `\Pi`
7. Inline: `\nu(\Pi^+_{f_{n-2}})`
8. Inline: `p_{n-1}(\Pi)`
9. Inline: `\Pi`
10. Inline: `\Pi`
11. Display: `\left\{\begin{aligned} p_0&=\text{ordre de }\sigma_0\sigma_1\\ p_1&:\text{ordre de }\sigma_1\sigma_2\\ &\cdots\\ p_{n-1}&:\text{Ordre de }\sigma_{n-1}\sigma_n \end{aligned}\right.`
12. Inline: `\Pi`
13. Inline: `\nu(\Pi^-_{f_2})`
14. Inline: `\sigma_0\sigma_1`
15. Inline: `E^-(2)_{f_2}\inserted{=(E/G_n^+(2))_{f_2}}`
16. Inline: `\nu(\Pi(d^{\unsure{a|o}}_{i,i+3}))`
17. Display: `(\sigma_0\sigma_1)^p x=\deleted{\unsure{x}}g_x\deleted{\unsure{\cdot}}x\qquad g_x\in G_n^+(2)`

Diagram/table 1 (objects, labels and directions included):

```latex
\(\begin{array}{ccccc}
i-1&&\unsure{i+1\leq j-1}&j+1&\\
&i&j&&i\\
&&\unsure{\geq|=}&&\\
&&i+2&&
\end{array}\)
```

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{$\Pi$}`
- deleted 2: `\unsure{$\nu(\Pi(d^{\unsure{a|o}}_{i,i+3}))$ est l'ordre}`
- deleted 3: `\unsure{x}`
- deleted 4: `\unsure{\cdot}`
- inserted 1: `=(E/G_n^+(2))_{f_2}`
- margin 1: `vrai tout au moins dans le cas des géométries d'incidences (``polyèdres''\ldots)`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:53:26+00:00

## Scan 44

Start UTC: 2026-11-17T23:53:26+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:53:44+00:00

### Crop-only words, accents and shapes

Opening has “Π une n-carte”, “comb.” added with a curved insertion line, “de moquette R=Rep(Π)”; the upper right corner is missing. “Gₙ-ensemble (où”; G has a loop/cross-stroke, not a double-struck letter. “Une représentation géom” is underlined; small φ/varphi has a loop and a descender. “un espace affine E (sur ... k disons)” with the ring word compressed; an abandoned “de rg n+1” is struck to the right. The cancelled word after “d’” resembles “une hom.”. Formula (1) uses “Drap max”; below it E₀⊂E₁...⊂Eᵢ⊂...⊂Eₙ⊂E in braces; a curved connector adds “ss-espace affine de E de rg i”. “telle que pour r∈R, 0≤i≤n, on ait”; (2) uses πⱼ twice and the condition i≠j. Bottom “où πⱼ(d) désigne la composante de dim j d’un drapeau d.”; the phrase after “Il revient” seems a short equals-like sign with “de dire” added underneath. Then “à dire que par passage au quotient, πⱼφ_R se factorise en”. The last target has abbreviated Gr/Grass aff with j below. No date or handwritten additions on type; all ink is handwritten.

### Comparison and changes

All three thirds were read first, then the page file; the lower compressed phrase and clipped group relation were enlarged. Top R and Rep have ordinary single main strokes, G has its interior cross-stroke, E has three bars, and Π two legs. No bold or blackboard alphabet inferred from heavy pen. The first φ/varphi ambiguity is marked; later φ_R and φ_j follow it. In the presentation both σ squares carry exponent 2; the commuting product reverses i and j; the edge condition j≥i+2 is partly clipped, with its 2 still doubtful. The damaged corner is noted as damage, not supplied text. The “comb.” connector goes after n-carte. The cancellation “de rg n+1” sits beside “dans”, and “une hom.” is struck immediately before live “application”. Diagram (1) has R→Drap max(E), label φ_R, and a vertical equality to the flag set; E_i’s curved explanatory connector is represented as an insertion. Every inclusion and index 0,1,i,n checked. Display (2) has outer π_j, φ_R, σ_i r; its right side is π_jφ_R(r), and i≠j is explicit. Diagram (3) has D_j(Π)→Gr aff_j(E), φ_j and the range 0≤j≤n. D/Delta and Gr/Grass ambiguity remains explicit. Changes at the bottom: “même|=” -> “$=$|même” because the crop has two definite parallel strokes, not legible letters; inserted “de dire” -> unsure “de par.|de dire” because a descender in the small note resembles p; the following live “de dire” -> “à dire”, following the separate accented first character. This awkward phrase is not regularized to idiomatic French. Other text and formulas: no change.

### Formula register checked against the crops

1. Inline: `\Pi`
2. Inline: `n`
3. Inline: `R=\operatorname{Rep}(\Pi)`
4. Inline: `G_n`
5. Display: `G_n=\{\sigma_0,\ldots,\sigma_n\mid\sigma_0^2=\cdots=\sigma_n^2=1,\ \sigma_i\sigma_j=\sigma_j\sigma_i\text{ si }j\geq i+\unsure{2}\}`
6. Inline: `\unsure{\varphi|\phi}`
7. Inline: `\Pi`
8. Inline: `n+1`
9. Inline: `E`
10. Inline: `k`
11. Inline: `E_i`
12. Inline: `E`
13. Inline: `i`
14. Inline: `r\in R`
15. Inline: `0\leq i\leq n`
16. Display: `\left\{\begin{aligned} \pi_j(\varphi_R(\sigma_i r))&=\pi_j\varphi_R(r)\quad\text{si}\\ 0\leq i,j&\leq n,\qquad i\ne j \end{aligned}\right. \tag*{(2)}`
17. Inline: `\pi_j(d)`
18. Inline: `j`
19. Inline: `d`
20. Inline: `=`
21. Inline: `\pi_j\varphi_R`
22. Inline: `(0\leq j\leq n)`

Diagram/table 1 (objects, labels and directions included):

```latex
(1)\quad\begin{tikzcd}[ampersand replacement=\&]
R\arrow[r,"\varphi_R"]\&\operatorname{Drap\,max}(E)\arrow[d,equal]\\
\&\{(E_0\subset E_1\cdots\subset E_i\subset\cdots\subset E_n\subset E)\}
\end{tikzcd}
```

Diagram/table 2 (objects, labels and directions included):

```latex
(3)\quad\begin{tikzcd}[ampersand replacement=\&]
\unsure{D_j|\Delta_j}(\Pi)\arrow[r,"\varphi_j"]\&\unsure{\mathrm{Gr\,aff}_j|\mathrm{Grass\,aff}_j}(E)
\end{tikzcd}\quad$(0\leq j\leq n)$
```

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{de rg $n+1$}`
- deleted 2: `\unsure{une hom.}`
- inserted 1: `comb.`
- inserted 2: `$E_i$: ss-espace affine de $E$ de rg $i$`
- inserted 3: `\unsure{de par.|de dire}`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:54:29+00:00

## Scan 45

Start UTC: 2026-11-17T23:54:29+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:54:58+00:00

### Crop-only words, accents and shapes

Viewed the three original crops; s1 is blank apart from stray spots, s2 and s3 are upside down. Rotated s3 then s2 to read the draft in writing order. The entire written block is cancelled by long diagonals. “Considérons une réalisation géom. φ de Π”; small insertion under the first line “dans l’espace affine E de rg n+1”; original second-line parenthesis seems “(affine dans)”, with affine already overwritten heavily. Right upper marginal parenthesis looks “régulière équivar.”, ending at edge; both words compressed. “sur un anneau k, donnée par”. The diagram has G=Aut(Π)→Aff(E), R=Rep(Π)→Drap max(E), and Dᵢ(Π)→Gr affᵢ(E); lower right has a thick overwritten-looking mark beneath the i. Two separate “G-hom.” labels, one on a curved connector to R’s downward map and one below φ_R. φ has a circular top with a descender. Bottom brace has φ_R(r)=(E₀⊂E₁⊂...⊂Eₙ⊂E), then σᵢEⱼ=Eⱼ si i≠j and three dots. A very faint equals-like pair appears after the first tuple. No genuine picture; the long lines cancel the draft.

### Comparison and changes

Read s1–s3 in the scan orientation, then rotated s3 and s2 through 180 degrees. The writing order is thus the reverse of the scan thirds; original s1 has no text. Read every line under the cancellation diagonals and both right-hand margin/insertion fragments. No change to readings. The whole draft remains deleted, including the marginal parenthesis, insertion, all diagram objects/labels, and both equations. The original “affine dans” remains inside the abandoned wording; it is not silently removed when the insertion “dans l’espace affine E de rg n+1” is placed after Π. Diagram: G=Aut(Π)→Aff(E) labelled φ_G; R=Rep(Π)→Drap max(E) labelled φ_R, with two G-hom. annotations, and downward arrows to D_i(Π) and Gr.aff_i(E), the right arrow labelled π_i; the lower arrow is φ_{D_i}. i occurs in all three places, not j. The visibly heavy shape below “aff” was enlarged: it continues the descending f stroke, rather than being a separate D; no extra letter added. Capitals G, R, E, D and Π are plain handwritten forms, with no separate double strokes or script replacement. Bottom equations: the first flag has E₀,E₁,...,Eₙ,E, with inclusions, and the second uses σ_i E_j=E_j with i≠j; the dots are present. The small curved stroke beneath the r argument is treated as part of the handwritten r. A faint equals-like trace after the flag has the pale character of show-through/erased background, unlike the live dark writing, so it is not silently asserted as live ink. No content is inferred from the large blank remainder. Marginal compressed words and the G-hom. ending remain uncertain.

### Formula register checked against the crops

1. Inline: `\unsure{\varphi|\phi}`
2. Inline: `\Pi`
3. Inline: `E`
4. Inline: `n+1`
5. Inline: `k`
6. Inline: `G`
7. Inline: `G`
8. Inline: `G`
9. Display: `\left\{\begin{aligned} &\deleted{\varphi_R(r)=(E_0\subset E_1\subset\cdots\subset E_n\subset E)}\\ &\deleted{\sigma_i E_j=E_j\quad\text{si }i\ne j\qquad\ldots} \end{aligned}\right.`

Diagram/table 1 (objects, labels and directions included):

```latex
\begin{tikzcd}[ampersand replacement=\&,row sep=large,column sep=huge]
\deleted{G=\operatorname{Aut}(\Pi)} \arrow[r,"\deleted{\varphi_G}"] \& \deleted{\operatorname{Aff}(E)} \\
\deleted{R=\operatorname{Rep}(\Pi)} \arrow[r,"\deleted{\varphi_R}"] \arrow[d] \arrow[dr,phantom,"\deleted{\text{$G$-hom.}}"] \& \deleted{\operatorname{Drap\ max}(E)} \arrow[d,"\deleted{\pi_i}"] \\
\deleted{\unsure{D|\Delta}_i(\Pi)} \& \deleted{\unsure{\operatorname{Gr.aff}|\operatorname{Gr.\ aff}}_i(E)}
\arrow[from=3-1,to=3-2,"\deleted{\varphi_{D_i}}"]
\arrow[from=2-1,to=3-1,phantom,"\deleted{\text{\unsure{$G$-hom.|$G$-homo}}}"',shift left=6ex]
\end{tikzcd}
```

### Corrections, cancellations and margins rechecked

- deleted 1: `(\unsure{régulière équivar.})`
- deleted 2: `Considérons une réalisation géom. $\unsure{\varphi|\phi}$ de $\Pi$ \inserted{dans l'espace affine $E$ de rg $n+1$} (\unsure{affine dans}) sur un anneau $k$, donnée par`
- deleted 3: `G=\operatorname{Aut}(\Pi)`
- deleted 4: `\varphi_G`
- deleted 5: `\operatorname{Aff}(E)`
- deleted 6: `R=\operatorname{Rep}(\Pi)`
- deleted 7: `\varphi_R`
- deleted 8: `\text{$G$-hom.}`
- deleted 9: `\operatorname{Drap\ max}(E)`
- deleted 10: `\pi_i`
- deleted 11: `\unsure{D|\Delta}_i(\Pi)`
- deleted 12: `\unsure{\operatorname{Gr.aff}|\operatorname{Gr.\ aff}}_i(E)`
- deleted 13: `\varphi_{D_i}`
- deleted 14: `\text{\unsure{$G$-hom.|$G$-homo}}`
- deleted 15: `\varphi_R(r)=(E_0\subset E_1\subset\cdots\subset E_n\subset E)`
- deleted 16: `\sigma_i E_j=E_j\quad\text{si }i\ne j\qquad\ldots`
- inserted 1: `dans l'espace affine $E$ de rg $n+1$`
- margin 1: `\deleted{(\unsure{régulière équivar.})}`

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:55:41+00:00

## Scan 46

Start UTC: 2026-11-17T23:55:41+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:56:01+00:00

### Crop-only words, accents and shapes

“Lorsque la n-carte Π est un polyèdre (= géométrie d’incidences), alors la donnée de φ_R satisfaisant (2) équivaut” with équivaut underlined. “soumises” is clipped/compressed at the far right. “compatibles avec les relations d’incidences”; “Dans le cas général, on peut dire” with “encore” added above dire. “se généralise en des applications”. Diagram (4) has D with subscript set {j₀,j₁,...,jₚ}; target also ends (Π), not (E). “pour tte partie”; Δₙ is triangular and followed by colon then {0,1,...,n}. “applications verticales pour les inclusions de parties de Δₙ”; “condition de fonctorialité précédente” at bottom. “on peut donc les interpréter” followed by added “les φ_R” before comme. “hom. de géométries de drapeaux basées sur” with small addition “l’ensᵇˡᵉ ordonné” before Δₙ. Last D_* is angular, star/bullet hard to distinguish, and Drap.aff_* has a clear cross-like star. No double-struck letters and no cancelled block.

### Comparison and changes

Read all thirds before the file; enlarged the two lower insertions and the target of (4). All formulas, including the repeated φ_R and the ordered index set, are listed below. The top source has (2), then (3); the new arrow is (4). Its source and target index sets both contain j₀,j₁,...,jₚ with braces; the arrow’s label has the abbreviated j₀,...,jₚ. The target ends (Π), clearly two-legged: preserved this apparent slip, not replaced by E. Δₙ in the prose is a separate triangular letter, unlike the large curled D in the diagram. D/mathscr-D remains doubtful at its first occurrence, and star/bullet is marked in D_* at the bottom. The superscript-like strokes of the inserted abbreviation after l’ens are crowded but lie on the same writing baseline, so no raised type is invented. “encore” goes after dire; “les φ_R” is inserted just before comme; “l’ens... ordonné” goes after sur. The long curves here are insertion connectors, not cancellation strokes. Change: unsure les -> les before interpréter; the enlarged crop has a clear l followed by the connected es. The resulting repeated “les ... les φ_R” is retained rather than edited for grammar. “soumises|soumis”, “tte” and the abbreviation ending remain doubtful. No changes to the mathematical arguments, indices, inclusions or Π/E distinction. There are no margins or deleted passages on this page.

### Formula register checked against the crops

1. Inline: `n`
2. Inline: `\Pi`
3. Inline: `\unsure{\varphi|\phi}_R`
4. Inline: `\varphi_j`
5. Inline: `(0\leq j\leq n)`
6. Inline: `\{j_0<j_1<\cdots<j_p\}`
7. Inline: `\Delta_n:\{0,1,\ldots,n\}`
8. Inline: `\Delta_n`
9. Inline: `\varphi_R`
10. Inline: `\varphi_R`
11. Inline: `\Delta_n`
12. Inline: `D_{\unsure{*|\bullet}}(\Pi)`
13. Inline: `\operatorname{Drap.aff}_*(E)`

Diagram/table 1 (objects, labels and directions included):

```latex
\begin{tikzcd}[ampersand replacement=\&,column sep=huge]
(4)\quad \unsure{D|\mathscr{D}}_{\{j_0,j_1,\ldots,j_p\}}(\Pi) \arrow[r,"\varphi_{\{j_0,\ldots,j_p\}}"] \& \operatorname{Drap\ aff}_{\{j_0,j_1,\ldots,j_p\}}(\Pi)
\end{tikzcd}
```

### Corrections, cancellations and margins rechecked

- deleted: none.
- inserted 1: `encore`
- inserted 2: `les $\varphi_R$`
- inserted 3: `l'ens\unsure{ble} ordonné`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:56:45+00:00

## Scan 47

Start UTC: 2026-11-17T23:56:45+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:57:09+00:00

### Crop-only words, accents and shapes

Upper half has three long oblique cancellation strokes, including “Fixons une telle composante connexe, i.e. un”. Opening “Ceci dit, considérons la r:=(j−i−2)-carte” with Πᵢ,ⱼ added above définie; the inequality starts 0≤i≤i+2≤j≤n, a heavy ≤ after i. NB is underlined; quotient denominators use i−1 and j+1. The later σ sequence has i+1 and j−1, identified by short vertical equal signs with primed σ₀ and σ_{j−i−2=r}. “qui en font une r-carte, dont l’ens des composantes connexes s’identifie à D... (Π)”. Live restart “Ceci dit, soit fᵢ∈Dᵢ(Π)”, added 1≤i≤n, “Eᵢ=φᵢ(fᵢ)”. “la (i−1)-carte induite”, with boundary-like ∂ followed by fᵢ and a raised c/inclusion mark. “dont l’ens des repères est”; “image rec.” rather than expansion. Small (Π) added to source of quotient diagram. “On trouve alors”, added “en termes de φ”, “une réalisation géom. canoniq.”, “(dite ``induite'')”. Final “Légèrement moins évidente est la définition de la représentation induite de la (n−i−1)-carte”, with a raised right-facing inclusion mark on boundary fᵢ. Formula capitals are ordinary R,E,D; Π is two-legged. No date.

### Comparison and changes

All three thirds were read first. Enlarged the rank definition, the cancelled component-set subscript, and the live lower connector. The first handwritten r is heavy, but its two following bars are an equals sign, not an additional colon: kept r=(j−i−2). The inserted Π has i,j below. The inequality is 0≤i≤i+2≤j≤n, retained literally. The quotient defining R_ij omits σ_i through σ_j; the NB examples use R₀ⱼ with j+1,...,n and Rᵢ,ₙ with 0,...,i−1. In the operation array, unprimed i+1,j−1 correspond to primed 0,j−i−2=r. The long diagonal strokes cancel every part of the upper block, including Fixons...i.e. un; the second Ceci dit is live. Change: subscript unsure ij|j on the cancelled component set -> j, because the enlargement shows a single dot and a long j descender, with no separate i. This is kept even though an ij index would fit the construction. Lower f_i, D_i, E_i, φ_i, and the inserted range 1≤i≤n checked individually. The first boundary sign and raised subset/c remain doubtful, as does the final superset decoration. The source of the live lower map has an inserted (Π). Change: confident rightward arrow -> unsure plain stroke|leftward arrow|rightward arrow, rendered as a doubtful connector inside tikz-cd: the curved insertion line overlaps the left end, while the horizontal heavy trace has no decisive right-hand arrowhead. Direction is not inferred from “image rec.”. The added “en termes de φ” goes after alors, and canoniq. remains a tentative abbreviation. No script or double-struck replacement is inferred from pen thickness. The final sentence remains unfinished at “dans l’un des”, continuing on the next scan.

### Formula register checked against the crops

1. Inline: `r=(j-i-2)`
2. Inline: `\Pi_{i,j}`
3. Inline: `(0\leq i\leq i+2\leq j\leq n)`
4. Display: `\deleted{R_{ij}=R/(\sigma_0\cdots\sigma_{i-1},\sigma_{j+1},\ldots,\sigma_n)}`
5. Display: `\deleted{R_{0j}=R/(\sigma_{j+1},\ldots,\sigma_n),\qquad R_{i,n}=R/(\sigma_0\cdots\sigma_{i-1}))}`
6. Inline: `\begin{array}{ccc} \deleted{\sigma_{i+1}}&\deleted{,\ldots,}&\deleted{\sigma_{j-1}}\\ \deleted{\Vert}&&\deleted{\Vert}\\ \deleted{\sigma'_0}&\deleted{,\ldots,}&\deleted{\sigma'_{j-i-2=r}} \end{array}`
7. Inline: `r`
8. Inline: `\unsure{D|\Delta}_j(\Pi)`
9. Inline: `f_i\in D_i(\Pi)`
10. Inline: `(1\leq i\leq n)`
11. Inline: `E_i=\unsure{\varphi|\phi}_i(f_i)`
12. Inline: `(i-1)`
13. Inline: `\unsure{\partial|\delta}f_i^{\unsure{\subset|c}}`
14. Inline: `D_{01\ldots i}(f_i)`
15. Inline: `\{f_i\}`
16. Inline: `\varphi`
17. Inline: `\partial f_i`
18. Inline: `E_i`
19. Inline: `(n-i-1)`
20. Inline: `\unsure{\partial f_i^{\supset}|\partial f_i\supseteq}`

Diagram/table 1 (objects, labels and directions included):

```latex
$\begin{array}{ccc}
\deleted{\sigma_{i+1}}&\deleted{,\ldots,}&\deleted{\sigma_{j-1}}\\
\deleted{\Vert}&&\deleted{\Vert}\\
\deleted{\sigma'_0}&\deleted{,\ldots,}&\deleted{\sigma'_{j-i-2=r}}
\end{array}$
```

Diagram/table 2 (objects, labels and directions included):

```latex
\begin{tikzcd}[ampersand replacement=\&]
D_{0,1,\ldots,i}\inserted{(\Pi)} \arrow[r,phantom,"{\unsure{-|\longleftarrow|\longrightarrow}}" description] \& D_i(\Pi).
\end{tikzcd}
```

### Corrections, cancellations and margins rechecked

- deleted 1: `Ceci dit, considérons la $r=(j-i-2)$-carte \inserted{$\Pi_{i,j}$} définie par la moquette $(0\leq i\leq i+2\leq j\leq n)$`
- deleted 2: `R_{ij}=R/(\sigma_0\cdots\sigma_{i-1},\sigma_{j+1},\ldots,\sigma_n)`
- deleted 3: `(\uline{NB}`
- deleted 4: `R_{0j}=R/(\sigma_{j+1},\ldots,\sigma_n),\qquad R_{i,n}=R/(\sigma_0\cdots\sigma_{i-1}))`
- deleted 5: `avec les opérations induites par passage au quotient par`
- deleted 6: `\sigma_{i+1}`
- deleted 7: `,\ldots,`
- deleted 8: `\sigma_{j-1}`
- deleted 9: `\Vert`
- deleted 10: `\Vert`
- deleted 11: `\sigma'_0`
- deleted 12: `,\ldots,`
- deleted 13: `\sigma'_{j-i-2=r}`
- deleted 14: `qui en font une $r$-carte, dont l'ens des composantes connexes s'identifie à $\unsure{D|\Delta}_j(\Pi)$. Fixons une telle composante connexe, i.e. un`
- inserted 1: `$\Pi_{i,j}$`
- inserted 2: `$(1\leq i\leq n)$`
- inserted 3: `(\Pi)`
- inserted 4: `en termes de $\varphi$`
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:58:24+00:00

## Scan 48

Start UTC: 2026-11-17T23:58:24+00:00  
Crop-only observations saved before opening page file: 2026-11-17T23:58:49+00:00

### Crop-only words, accents and shapes

Top continues with “repères est”; Dᵢ,ᵢ₊₁,...,ₙ(fᵢ)=image inv. de {fᵢ}, “par” followed by a clear right arrow to Dᵢ. A cancelled initial “Ce” before “Les sommets”; a cancelled f with crowded i+1-like subscript before the live (i,i+1)-drapeaux. “dont la iᵉ composante est fᵢ, et ils s’envoient sur des drapeaux de E de type (i,i+1) dont la i-composante est fᵢ”; the second fᵢ is plainly f, even though the following couple uses E. Another crossed little “les” before i.e. “des couples (Eᵢ⊂Eᵢ₊₁), Eᵢ₊₁ de rg i+1”. A tiny low mark under the first i is dark and may be a cancelled 2. “Mais si Vᵢ est l’espace des translations de Eᵢ, les Eᵢ₊₁ correspondent à des droites de” then E-bar=E/Vᵢ. The first E has a separate overbar; the second is heavier, with no independent extra stroke to justify blackboard type. The remainder of s2 and all s3 are blank apart from archive number 47.

### Comparison and changes

Read all three thirds, including the blank lower part. The first D has i,i+1,...,n and argument f_i; the map omits arguments and has a decisive rightward arrow to D_i, unlike the obscured connector on scan 47. All displayed and inline formulas are registered below. The crossed initial Ce, the cancelled f_{i+1}|f_{1n}, and the short cancelled les were re-read; their following live words are not struck. Both live occurrences of f_i remain f_i, including the one naming the component of an E-flag: no mathematical correction to E_i. In the couple, the first E has i plus a tiny uncertain cancelled 2 underneath, the second has i+1; the rank is i+1. Change: unsure i-ème composante -> unsure i-composante|i-ème composante (LaTeX preserves the ordinal as the second candidate). Enlargement shows a short separate horizontal stroke following i and no securely raised ending, so the hyphenated reading comes first. Last paragraph: V_i and E_i are ordinary capitals; the final first E has a separate bar, whereas the quotient numerator is merely heavy and is not double-struck. No following words are supplied into the large blank space. No margin or insertion occurs here. The page-break continuation triggered a further source check on scan 47, documented separately below.

### Formula register checked against the crops

1. Inline: `\unsure{D|\Delta}_{i,i+1,\ldots,n}(f_i)=\text{image inv. de }\{f_i\}`
2. Inline: `\unsure{f_{i+1}|f_{1n}}`
3. Inline: `(i,i+1)`
4. Inline: `\Pi`
5. Inline: `i`
6. Inline: `i`
7. Inline: `f_i`
8. Inline: `E`
9. Inline: `(i,i+1)`
10. Inline: `i`
11. Inline: `f_i`
12. Inline: `(E_{i\deleted{\unsure{2}}}\subset E_{i+1})`
13. Inline: `E_{i+1}`
14. Inline: `i+1`
15. Inline: `V_i`
16. Inline: `E_i`
17. Inline: `E_{i+1}`
18. Inline: `\overline{E}=E/V_i`

Diagram/table 1 (objects, labels and directions included):

```latex
\begin{tikzcd}[ampersand replacement=\&]
D_{i,i+1,\ldots,n} \arrow[r] \& D_i.
\end{tikzcd}
```

### Corrections, cancellations and margins rechecked

- deleted 1: `\unsure{Ce}`
- deleted 2: `$\unsure{f_{i+1}|f_{1n}}$`
- deleted 3: `\unsure{les}`
- deleted 4: `\unsure{2}`
- inserted: none.
- margin: none.

All handwritten: no corrections on typed text. The formula register includes the i/j positions reviewed; indices are not inferred from adjacent formulas.

End UTC: 2026-11-17T23:59:43+00:00

### Scan 47–48 page-break recheck — 2026-11-17T23:59:43+00:00

Enlarged the last words of scan 47 s3 after reading scan 48. Change: `dans l'un des` -> `dont l'ens des`. The last stroke of the first word is an angular t, and the abbreviation has an initial looped e and final descending s. This reads continuously with scan 48’s “repères est”; the change is based on the enlarged ink, not solely on syntax. The original scan-47 audit’s statement that the phrase ended “dans l’un des” is superseded by this correction. No other page-47 change.

## Notation reconciliation before freeze — 2026-11-18T00:01:54+00:00

Compared the D forms across scans 40–42 and 44–48 with the separately triangular Δₙ on scan 46. Reopened 40 s1 and 41 s1 and compared their bowls/stems with the later enlarged D and the just-audited later crops. Changes: first-occurrence D|Delta alternatives on 40,41,42,44,45,47,48 -> D. These have a curved right bowl and distinct left stem; the earlier triangular reading was overcautious. The unusually long entry stroke in scan 46 still allows D|mathscr-D and remains marked. The two-legged Π on scan 40 agrees with 41–48; its obsolete Gamma notation-table entry is replaced, following the earlier scan-40 audit. The ambiguous ν/v of scan 43 is a separate glyph use from the v/ν matrix coefficients on 33; no unsupported identification was made. η/γ, φ variants, p/ρ, boundary sign, stars, and the raised mark on f were compared at their audited occurrences and remain as locally marked. Plain R,E,G are not made double-struck because of ink thickness; the separate bar and doubled N on scan 42 are retained. Quotation marks stay paired backticks/apostrophes. No change to source abbreviations.
