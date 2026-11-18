# Independent image reading · K72-03

The first paragraph for each scan was recorded from its three image strips before reopening its page file. Locations refer to the manuscript. The formula list follows the order in the revised page file. Source delimiters are retained so that small indices and exponents can be compared directly.

## Scan 35

2026-11-18T10:47:32Z to 2026-11-18T10:48:17Z (UTC).

**Reading from the image strips**

The writing occupies four principal lines. D’ailleurs, conique over a crossed q-word, invariante, Peut-être with a circumflex-shaped stroke, préalable, then the crossed forme quadratique. A separate higher line starts hyp… and ends in a short, apparently plural word. A large question mark stands at the left. The lower strips carry only the small archive number 34.

**Comparison with the page file**

The enlarged interline has three separated groups and an additional small group after the descender of hyp. The last has a tall initial l and joined short humps. Replaced the initial reading of the whole phrase. The dark stroke preceding the second invariante remains doubtful. Q and X are plain capitals, the little cross is raised only on the first φ. The main horizontal line cuts through forme quadratique and ends before the following word. The ? is independent of either bracket.

**Formulas and indices**

**1.**

~~~tex
$N=2$
~~~

**2.**

~~~tex
$\exists 1$
~~~

**3.**

~~~tex
$Q\subset X$
~~~

**4.**

~~~tex
$\varphi^{+}$
~~~

**5.**

~~~tex
$\varphi$
~~~

Index and exponent forms containing i or j do not occur.

**Changes**

- `hyps.\ plus intrinsèques` → `hyp.\ qu.\ \unsure{entière|encore} lisse`
- `\unsure{invariantes}` → `\unsure{invariante|invariantes}`

## Scan 36

2026-11-18T10:48:18Z to 2026-11-18T10:49:15Z (UTC).

**Reading from the image strips**

Supposons … inv., then three lisse equivalences. Read the left-hand terms as a descending, looped span symbol with a second hooked stroke. A long straight ditto line replaces forme sur in the last row. The side note reads dans V, f / ou C = P(V), Q / (n ≥ 2). The boxed gloss ends car. ≠ 2 !. Re-read se reconstruit, à partir, réflexion associée, direction; inv. recurs. Both raised perpendicular strokes are present in each factor on the right. At the bottom α is followed by squared parentheses and two separate f's. The sign before 1 in the last parentheses looks like +.

**Comparison with the page file**

The slanting three-line gloss at left has its own baseline and an underlining stroke under the first line. The short label over the box is particularly faint. The diagram brackets sit below the three a’s, with 2−α on each. The first α subscript in the two isolated inequalities collides with ≠, the second is overwritten. In the next display the 2 multiplying the sum is distinct from the −2 in the third hypothesis. Read the multiplication order under each ρ again. The tops of both V's rise above the modes of their exponents. The scribble preceding réflexion, small stroke under the first brace, and text after the first cosine remain cancelled. The projective P has an inner upright and the span glyph has a separate lower return.

**Formulas and indices**

**1.**

~~~tex
$\beta_i\inserted{=\alpha_i+2}$
~~~

**2.**

~~~tex
\[
\begin{aligned}
\text{forme sur }&\unsure{\mathrm{G}|\mathcal G}(a_{i-1},\unsure{a_i|\tau_i},a_{i+1})\ \text{lisse}\iff\alpha_{i-1}+\alpha_i\quad\text{inv.}\\
\text{forme sur }&\mathrm{G}(a_{i-1},a_i)\ \text{lisse}\iff 2-\alpha_{i-1}\quad\text{inv.}\\
\text{\rule{2.6cm}{0.35pt} }&\mathrm{G}(a_i,a_{i+1})\ \text{lisse}\iff 2-\alpha_i\quad\text{inv.}
\end{aligned}
\]
~~~

**3.**

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=0pt]
\deleted{\unsure{\alpha_i}} \& a_{i-1}\arrow[r,dash,to path={-- ++(0,-.65em) -| (\tikztotarget)},swap,"{2-\alpha_{i-1}}"] \& a_i\arrow[r,dash,to path={-- ++(0,-.65em) -| (\tikztotarget)},swap,"{2-\alpha_i}"] \& a_{i+1}
\end{tikzcd}
~~~

**4.**

~~~tex
\[
\begin{aligned}
\alpha_{\unsure{i|i-1}}&\ne 2\qquad\text{\unsure{l'une|hyp.} des val. propres }1\\
\alpha_{\unsure{i-1|i+1}}&\ne 2
\end{aligned}
\]
~~~

**5.**

~~~tex
\[
\left.\begin{aligned}
&\beta_0,\ldots,\beta_{n-1}\quad\text{inv.}\\
&2(\alpha_{i-1}+\alpha_i)\quad\text{inv.}\ \inserted{\boxed{\text{donc car. }\ne2\,!}}\\
&\alpha_{i-1}-2,\ \alpha_i-2\quad\text{inv}
\end{aligned}\right\}
\]
~~~

**6.**

~~~tex
$i$
~~~

**7.**

~~~tex
$1\le i\le n-1$
~~~

**8.**

~~~tex
$\tau_i$
~~~

**9.**

~~~tex
$\underset{\substack{\Vert\\ \tau_{i-1}\tau_i}}{\rho_{i-1}},\underset{\substack{\Vert\\ \tau_i\tau_{i+1}}}{\rho_i}$
~~~

**10.**

~~~tex
$\tau_{i-1}=\rho_{i-1}\tau_i$
~~~

**11.**

~~~tex
$\tau_{i+1}=\tau_i\rho_i$
~~~

**12.**

~~~tex
$V,f$
~~~

**13.**

~~~tex
$C=\mathbb{P}(V),\unsure{Q}$
~~~

**14.**

~~~tex
$(n\geq2)$
~~~

**15.**

~~~tex
$\tau_i={}$
~~~

**16.**

~~~tex
\[
\begin{aligned}
\left(
\underbrace{V^{\rho_{i-1}}}_{\substack{\deleted{\unsure{=}}\Vert\\\{a_{i-1},a_i\}^{\perp}}}
+\underbrace{V^{\rho_i}}_{\substack{\Vert\\\{a_i,a_{i+1}\}^{\perp}}}
\right)^{\perp}
&=\{a_{i-1},a_i\}^{\perp\perp}\cap\{a_i,a_{i+1}\}^{\perp\perp}\\
&=\mathrm{G}(a_{i-1},a_i)\cap\mathrm{G}(a_i,a_{i+1})
\end{aligned}
\]
~~~

**17.**

~~~tex
\[
\alpha_i=\frac{(a_i,a_{i+1})^2}{f(a_i)f(a_{i+1})}=4\cos^2\theta_i\ \deleted{\unsure{\cos 2}}
\]
~~~

**18.**

~~~tex
\[
\beta_i=\alpha_i+2=2\bigl(\underbrace{2\cos^{\unsure{2|1}}\theta_i+1}_{\deleted{\unsure{2}}\cos 2\theta_i}\bigr)=4\cos2\theta_i
\]
~~~

Index and exponent forms containing i or j include `_i`, `_{i-1}`, `_{i+1}`, `^{\rho_i}`.

**Changes**

- `\text{------------- }` → `\text{\rule{2.6cm}{0.35pt} }`
- `\text{l'une des \unsure{val.} propres }` → `\text{\unsure{l'une|hyp.} des val. propres }`
- `\uline{dans $V,f$} ou $C=\mathbb{P}(V),\unsure{Q}$ $(n\geq2)$` → `\margin{\uline{dans $V,f$} ou $C=\mathbb{P}(V),\unsure{Q}$ $(n\geq2)$}`

## Scan 37

2026-11-18T10:49:16Z to 2026-11-18T10:49:46Z (UTC).

**Reading from the image strips**

Single formula in the upper right. Aut is the only word, followed by two levels of parentheses. A broad U-shaped curve crosses a finer round stroke in the first capital. Its subscript has the loop, downward stem and turned foot seen on ρ on the following leaves. The first argument of Aut has two diagonals. The small mark to the right of τ is low. No accents or prose occur.

**Comparison with the page file**

At enlargement the live top-right diagonal of X crosses a smaller round older body. The outer capital on the left is a U with a second, rounded older stroke. The lower loop on the left is the ρ on scan 38. The low mark by τ has no independently resolved dot and stem. The isomorphism sign has one straight stroke. No other writing appears in the middle or bottom apart from 36 in the archive corner.

**Formulas and indices**

**1.**

~~~tex
\[
\deleted{\unsure{G}}U_{\rho}\simeq\operatorname{Aut}\bigl(\deleted{\unsure{E}}X,(\tau_{\unsure{*|\bullet|i}})\bigr)
\]
~~~

Index and exponent forms containing i or j do not occur.

**Changes**

- `\unsure{U|\mathcal U}_{\unsure{g|\rho}}` → `\deleted{\unsure{G}}U_{\rho}`
- `\unsure{X|Y}` → `\deleted{\unsure{E}}X`
- `\unsure{*|i}` → `\unsure{*|\bullet|i}`

## Scan 38

2026-11-18T10:49:46Z to 2026-11-18T10:53:06Z (UTC).

**Reading from the image strips**

Top: Soit; inversible i.e.; prenons la multiplication. The end-of-line addition looks like « lisse conn. de rel. 1 » with a return curve. schéma en groupes; hom, iso., sss, inversible. In the second paragraph: Considérons, hyperpolyèdre régulier, paramétré/ponctué, épinglé, de dim. n; the word over dim. n resembles a short parenthetical « ou 3 ». correspondant(s) and des invariants, parentheses after residues, square opening bracket before avec. Last line is a replacement, ending in angle brackets.

**Comparison with the page file**

The initial U has a darkened second stroke. E has the upright and second bar of the affine-line sign. The subscript under the underlined Spec expression includes both parentheses. The first lambda after the star has a prime, and only the second lambda in the product is primed. The intervening hook into « groupes » locates the small qualifier. The map has a bar at its tail, the line beneath it runs to G with a low m. On the penultimate line both i's are short without descenders. An older capital under the second coefficient and the final deleted rho formula are crossed. At the bottom the L has two long uprights and the prime belongs to the second pi. There is no typed material.

**Formulas and indices**

**1.**

~~~tex
$\rho\in\Gamma(S,\mathcal O_S)$
~~~

**2.**

~~~tex
$U_\rho\subset\unsure{\mathbb E|E}^{1}_{S}$
~~~

**3.**

~~~tex
$\lambda$
~~~

**4.**

~~~tex
$1+\lambda\rho$
~~~

**5.**

~~~tex
\[
U_\rho=\underline{\operatorname{Spec}}\ \mathcal O_S[T]_{(1+\rho T)}
\]
~~~

**6.**

~~~tex
\[
(\lambda\mathbin{\underset{\rho}{*}}\lambda'=\lambda+\lambda'+\lambda\lambda'\rho
\]
~~~

**7.**

~~~tex
$U_\rho$
~~~

**8.**

~~~tex
\[
\begin{aligned}
\lambda&\mapsto 1+\lambda\rho\\
U_\rho&\longrightarrow G_m
\end{aligned}
\]
~~~

**9.**

~~~tex
$\rho$
~~~

**10.**

~~~tex
$S$
~~~

**11.**

~~~tex
$n$
~~~

**12.**

~~~tex
$\mu_i$
~~~

**13.**

~~~tex
$(0\leq i\leq n)$
~~~

**14.**

~~~tex
$\unsure{\beta_i|\lambda_i}$
~~~

**15.**

~~~tex
$(0\leq i\leq n-1)$
~~~

**16.**

~~~tex
$\mu_i+1$
~~~

**17.**

~~~tex
$0\leq i\leq n$
~~~

**18.**

~~~tex
$\rho=\unsure{\mathbb L|L}_{n+1}(\mu_0,\lambda_0,\ldots,\lambda_{n-1},\mu_n)$
~~~

**19.**

~~~tex
\[
\unsure{=}\qquad \rho=\mathbb L_{n+1}(\mu_0,\lambda_0,\ldots,\lambda_{n-1},\mu_n)=\langle\pi,\pi'\rangle
\]
~~~

Index and exponent forms containing i or j include `_i`.

**Changes**

- `de \unsure{rel.}` → `\unsure{de rel.|de dim.\ rel.}`
- `(ou \unsure{3|1})` → `(\unsure{ou 3|ou 1|tous})`
- `correspondant à des invariants` → `correspondant \unsure{à|:} des invariants`

## Scan 39

2026-11-18T10:53:07Z to 2026-11-18T10:53:57Z (UTC).

**Reading from the image strips**

Donc ... opère(nt) fidèlem[en]t, the adverb is squeezed above sur. Parenthesis « représent... transposées l’une de l’autre »; transposées rises above a crossed word. Comme π, π′ invariantes ... ; two column arrows to Aut. « et de = avec E′ », On obtient en fait, en utilisant la section. Lower diagonal hand « opère par homothéties ». « évident en passant au quotient », On trouve; Thm underlined, De plus, si, ... « une section de X sur S) : on a que » followed on next page.

**Comparison with the page file**

The first small superscript is shaped like E; the one on the next line carries a prime. Both tensor signs have circles and both left factors bear a prime. The group on the s-membership line has a large loop and low n. The only ordinary i index is on tau. The small marks against the two displayed group maps are distinct from the arrows, whose heads point right. The diagonals on the lower diagram connect G_m to the two upper objects, with a hook near the left leg and wording beneath the right leg. The manuscript has « les scalaires ». Theorem heading has a rule, and the long stroke on the left of the last paragraph marks the theorem block without striking the words. The scribble before « sous les » is a cancellation; exact old letters are doubtful.

**Formulas and indices**

**1.**

~~~tex
$U_\rho$
~~~

**2.**

~~~tex
$\unsure{E|\mathcal E},E'$
~~~

**3.**

~~~tex
\[
\left\{\begin{aligned}
u_\lambda^E &=\mathrm{id}+\lambda\pi'\otimes\pi\\
u_\lambda^{E'}&=\mathrm{id}+\lambda\pi'\otimes\pi
\end{aligned}\right.
\]
~~~

**4.**

~~~tex
$\pi,\pi'$
~~~

**5.**

~~~tex
$\tau_i$
~~~

**6.**

~~~tex
$\varphi^E(s)$
~~~

**7.**

~~~tex
$\varphi_{\unsure{*|s}}^{E'}(s)$
~~~

**8.**

~~~tex
$(s\in\unsure{G_n|\mathcal G_n})$
~~~

**9.**

~~~tex
\[
\begin{aligned}
\unsure{\alpha_2|\alpha'}\quad U_\rho&\longrightarrow\underline{\operatorname{Aut}}(E,\varphi^E)\\
\alpha\quad U_\rho&\longrightarrow\underline{\operatorname{Aut}}(X,\varphi^X)
\end{aligned}
\]
~~~

**10.**

~~~tex
$=$
~~~

**11.**

~~~tex
$E'$
~~~

**12.**

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
(\unsure{\alpha\alpha|\alpha *}) \& G_m\times U_\rho\arrow[rr]\&\&\operatorname{Aut}(E,\varphi^E)\\
\&\&G_m\arrow[ul,hook']\arrow[ur,swap,"\text{opère par homothéties}"]\&
\end{tikzcd}
~~~

**13.**

~~~tex
$\alpha$
~~~

**14.**

~~~tex
$\alpha$
~~~

**15.**

~~~tex
$(\alpha\alpha)$
~~~

**16.**

~~~tex
$D_0=(H_1\cap\cdots\cap H_n)$
~~~

**17.**

~~~tex
$D_0^{**}=D_0\setminus\{c,d\}$
~~~

**18.**

~~~tex
$\unsure{\exists|\,}d=D_0\cap C$
~~~

**19.**

~~~tex
$X$
~~~

**20.**

~~~tex
$S$
~~~

Index and exponent forms containing i or j include `_i`.

**Changes**

- `\unsure{fidèlt}` → `\unsure{fidèlt|fidèlem.}`
- `Comme $\pi,\pi'$ invariants` → `Comme $\pi,\pi'$ \unsure{invariants|invariantes}`
- `(qui est une section de $X$ sur $S$) on a que` → `(qui est une section de $X$ sur $S$) \unsure{.|:} on a que`

## Scan 40

2026-11-18T10:53:58Z to 2026-11-18T10:54:49Z (UTC).

**Reading from the image strips**

opère (traces read as stablement? « sans … ») sur D₀ et D₀** ; torseur underlined, (trivialisé par son ...). Divider, Supposons maintenant les μᵢ=2, ... sorte qu'on a une forme quadratique, inv. underlined, canonique f sur E, unique par la condition. First trial f(a...) crossed. One Q in « d’où Q ⊂ X ». On sait que la pseudo-réflex... ; orthogonal, sss, projectiv... corr. ; dans X conserve Q, et ceci signifie que. Penultimate equation repeated with cancellation between it and (*)/(**).

**Comparison with the page file**

The terminal double-star is above D with a low 0, and the loop below torseur is its underline. The zero and minus-one indices in the normalization do not match each other. The script before « d’où » is a separate crossed verbal start. The blackboard P has a second downstroke and the exponent looks like n. The small formula at the right is written under a brace. In the first line of the lower display there is a crossed mark preceding f, a second crossed mark above its argument, then a prime on the factor following the parenthesis. These are not an extra live lambda before f. On the next line both underbrace annotations begin with minus, and the double tildes belong to sigma and rho. At the foot the reference has two marks between parentheses. The i on mu has no descender.

**Formulas and indices**

**1.**

~~~tex
$U_\rho$
~~~

**2.**

~~~tex
$D_0$
~~~

**3.**

~~~tex
$D_0^{**}$
~~~

**4.**

~~~tex
$D_0^{**}$
~~~

**5.**

~~~tex
$U_\rho$
~~~

**6.**

~~~tex
$\unsure{s_0|S_0}\ldots$
~~~

**7.**

~~~tex
$\mu_i=2$
~~~

**8.**

~~~tex
$f$
~~~

**9.**

~~~tex
$\unsure{E|\mathcal E}$
~~~

**10.**

~~~tex
\[
f(a_{-1})=0,\qquad f(e_0)=1,
\]
~~~

**11.**

~~~tex
$Q\subset X=\mathbb P^{n}(E)$
~~~

**12.**

~~~tex
$\mathrm{id}+\underbrace{\lambda\pi'\otimes\pi}_{\pi'\otimes\lambda\pi}$
~~~

**13.**

~~~tex
$X$
~~~

**14.**

~~~tex
$Q$
~~~

**15.**

~~~tex
\[
\begin{aligned}
&\deleted{\unsure{\lambda}}\unsure{f(\deleted{\unsure{\psi f}}\lambda\pi)}\pi'+\psi(\lambda\pi)=0\quad\text{i.e.}\\
&\lambda\bigl[\lambda\underbrace{f(\pi)}_{-\widetilde\sigma\widetilde\rho}\pi'+\underbrace{\psi(\pi)}_{-\sigma\pi'}\bigr]=0\qquad\text{i.e.}\\[-2pt]
&\hspace{1.5em}\deleted{\unsure{\lambda f\pi'+{}}}
\end{aligned}
\]
~~~

**16.**

~~~tex
\[
\lambda(\sigma+\lambda\widetilde\sigma\widetilde\rho)=0
\tag*{$(**)$}
\]
~~~

Index and exponent forms containing i or j include `_i`.

**Changes**

- `\deleted{\unsure{\lambda f}}\unsure{\lambda f(\lambda\pi)}` → `\deleted{\unsure{\lambda}}\unsure{f(\deleted{\unsure{\psi f}}\lambda\pi)}`
- `orthogonale sss` → `\unsure{orthogonal|orthogonale} sss`

## Scan 41

2026-11-18T10:54:50Z to 2026-11-18T10:55:32Z (UTC).

**Reading from the image strips**

1) Cas n pair, « l’équation s’écrit »; « Si σ et ρ̃ inversibles, la seule solution inversible (correspondant ... : une section de Uρ partout ≠1) est donnée par »; tiny « i.e. » above opening parenthesis. Underbrace under u and « antipodisme ». Crossed initial line under σ=0; D’autre part, conditions équivalentes. b), c), a) with a large curved arrow from a) to top. Enfin, si ρ̃=0, ces conditions équivalentes reviennent à la suivante; « loc. section ... partout ≠1 qui invarie fᴱ ... »; a double-rising crossed tail.

**Comparison with the page file**

The superscript over the deleted or at the right of Q is hatched. It stays inside a deletion. The live X is down below. The b of the first displayed condition has a distinct ascender and bowl. The long bent line moves a) to the head of the list; it does not cancel b) or c). The two numerators are 1, and the small black marks against rho in both denominators were traced as cancelled 2's, with uncertainty. There is no i or j index. At the foot the old parenthesis is split over two lines by the later addition. The exact ending of the verbal form after conditions is not clear enough to establish an agreement slip.

**Formulas and indices**

**1.**

~~~tex
$n$
~~~

**2.**

~~~tex
$\rho=2\widetilde\rho$
~~~

**3.**

~~~tex
$\sigma=\widetilde\sigma$
~~~

**4.**

~~~tex
\[
\lambda\sigma(1+\deleted{\unsure{2}}\lambda\widetilde\rho)=0
\]
~~~

**5.**

~~~tex
$\sigma$
~~~

**6.**

~~~tex
$\widetilde\rho$
~~~

**7.**

~~~tex
$U_\rho$
~~~

**8.**

~~~tex
$\ne 1$
~~~

**9.**

~~~tex
\[
\lambda=-\frac{1}{\deleted{\unsure{2}}\widetilde\rho}\qquad
\text{d'où}\qquad
\underbrace{u=\mathrm{id}-\frac{1}{\deleted{\unsure{2}}\widetilde\rho}\pi'\otimes\pi}_{\text{\uline{antipodisme}}}
\]
~~~

**10.**

~~~tex
$\sigma=0$
~~~

**11.**

~~~tex
$\unsure{G_\rho|U_\rho}$
~~~

**12.**

~~~tex
$f$
~~~

**13.**

~~~tex
$=$
~~~

**14.**

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=0pt,row sep=small]
{} \& {}\\
\mathrm b)\ \&U_\rho\ \text{invarie }f^E\\
\mathrm c)\ \&U_\rho\ \text{invarie } Q_X^{\deleted{\unsure{E|X}}}\\
\mathrm a)\arrow[uuu,bend left=75]\ \&\sigma=0
\end{tikzcd}
~~~

**15.**

~~~tex
$\widetilde\rho=0$
~~~

**16.**

~~~tex
$\sigma=0$
~~~

**17.**

~~~tex
$\exists$
~~~

**18.**

~~~tex
$U_\rho$
~~~

**19.**

~~~tex
$\ne1$
~~~

**20.**

~~~tex
$f^E$
~~~

**21.**

~~~tex
$=$
~~~

**22.**

~~~tex
$Q_X$
~~~

Index and exponent forms containing i or j do not occur.

**Changes**

- `\unsure{\mathrm b)|\mathrm b)}` → `\mathrm b)`
- `conditions équivalent encore` → `conditions \unsure{équivalent|équivalentes} encore`

## Scan 42

2026-11-18T10:55:33Z to 2026-11-18T10:56:31Z (UTC).

**Reading from the image strips**

2°) Cas n impair, l'équation s'écrit. « Donc si ... inv., ... ∃! solution u de Uρ, partout ≠1, ... qui invarie f, ou ce qui revient au =, qui invarie Q – savoir ». Margin, rotated into its own direction: NB Si σ̃ inv. et non σ (p. ex. en car. 2) on a solution bien ... au =, savoir que λ=−2/ρ, mais celle-ci peut être nulle en certains pts. Donnons énoncé commun aux cas 1°) et ... uniforme des [or de] σ ρ̃ inversibles; a separate tiny ib. D'autre part, condns équiv... a), bracketed NB « Si 2 inv. ... si 2=0 », then b/c; « Si ... ρ=0, ces conditions équivalent aussi à : d) ∃ loc. section ... partout ≠1 ... (ou encore, Qₓ) ».

**Comparison with the page file**

The complete long left note was read upright after rotation. Its symbols are a tilde sigma at the top, bare sigma on the next line, minus over the fraction with numerator 2, and rho below. The last box runs under the phrase inversibles. The small separate left note is slanted too. Returning to the main lines, the mark after the existential is a nearly undotted upright, hence the unresolved 1 / !. There is no i or j index. The operation sign in the u formula is an inked-over square. The lower bracket contains an abbreviated scalar condition with an ambiguous glyph against 2. The rule after U in c) repeats the verb of the preceding condition. The crossings through « la seule », « telle », the ending of « équiv. » and « de plus » have no effect on the following live clauses.

**Formulas and indices**

**1.**

~~~tex
$n$
~~~

**2.**

~~~tex
$\rho=\widetilde\rho$
~~~

**3.**

~~~tex
$\sigma=2\widetilde\sigma$
~~~

**4.**

~~~tex
\[
\lambda\widetilde\sigma(2+\lambda\rho)=0
\]
~~~

**5.**

~~~tex
$\sigma\inserted{\unsure{\sigma}}(=2\widetilde\sigma)$
~~~

**6.**

~~~tex
$\rho\inserted{(=\widetilde\rho)}$
~~~

**7.**

~~~tex
$\exists\unsure{1|!}$
~~~

**8.**

~~~tex
$u$
~~~

**9.**

~~~tex
$U_\rho$
~~~

**10.**

~~~tex
$\ne1$
~~~

**11.**

~~~tex
$f$
~~~

**12.**

~~~tex
$=$
~~~

**13.**

~~~tex
$Q$
~~~

**14.**

~~~tex
$\widetilde\sigma$
~~~

**15.**

~~~tex
$\sigma$
~~~

**16.**

~~~tex
$\lambda$
~~~

**17.**

~~~tex
$\lambda=-\dfrac{2}{\rho}$
~~~

**18.**

~~~tex
$\boxed{\sigma\widetilde\rho\ \text{inversibles}}$
~~~

**19.**

~~~tex
\[
\underbrace{u=\mathrm{id}\unsure{-|+}\frac{2}{\rho}\pi'\otimes\pi}_{\text{antipodisme}}
\]
~~~

**20.**

~~~tex
$2\widetilde\sigma=\sigma=0$
~~~

**21.**

~~~tex
$\widetilde\sigma\rho\inserted{(=\unsure{\widetilde\sigma\widetilde\rho})}=0$
~~~

**22.**

~~~tex
$\sigma=0$
~~~

**23.**

~~~tex
$\unsure{2\cdot1_S|2\,1_S}=0$
~~~

**24.**

~~~tex
$\widetilde\sigma\rho=0$
~~~

**25.**

~~~tex
$U_\rho$
~~~

**26.**

~~~tex
$f^E$
~~~

**27.**

~~~tex
$U_\rho$
~~~

**28.**

~~~tex
$Q_X$
~~~

**29.**

~~~tex
$\rho=0$
~~~

**30.**

~~~tex
$\exists$
~~~

**31.**

~~~tex
$U_\rho$
~~~

**32.**

~~~tex
$\ne1$
~~~

**33.**

~~~tex
$f^E$
~~~

**34.**

~~~tex
$Q_X$
~~~

Index and exponent forms containing i or j do not occur.

**Changes**

- `2) Cas` → `\unsure{2)|2°)} Cas`
- `$\exists 1$ section` → `$\exists\unsure{1|!}$ section`
- `(p. x. en car. 2) on a quand même unique solution` → `(p. \unsure{x.|ex.} en car. 2) on a \unsure{quand même} unique solution`
- `Donner énoncé commun aux cas 1°) et 2°) en termes de` → `\unsure{Donner|Donnons} énoncé commun aux cas 1°) et \unsure{2°)} \unsure{en termes de} `

## Scan 43

2026-11-18T10:56:32Z to 2026-11-18T10:57:11Z (UTC).

**Reading from the image strips**

Ex underlined. n=1, ρ=4−β=2−α, σ with black cancellation before 2, σ̃=1. 1°) si ρ inv., inserted i.e. Uρ ≃ Gm, ... telle que u invarie fᴱ (ou ce qui revient au =, ... la conique Qₓ); « savoir l’antipodisme, qui est l’unique section u telle que u²=1, uₛ ≠1 ∀s∈S ». 2°) Conditions équivalentes. S de car 2, loc. section, (ou encore, Qₓ). Proposition underlined; 1) ... inversible, 2) Conditions équivalentes. Parenthesis at right « cette dernière condition conséquence de la première si n pair ou 2 inv) ». Twice underscored condition near bottom; last line of ink touches the edge.

**Comparison with the page file**

There is an upper left bracket for the example and a matching right one after d). The subscript to u in the example is s, and the last sign has two diverging diagonals in ∀; there is no i or j index. The ring-shaped Q and the separately written low X recur in both lists. The bumpy subscript in U at the end of the second line has a rho, an equality, a numeral and a minus before alpha. Overwriting at that numeral leaves 2 and 1 possible. The upper and lower existential signs are followed by the same nearly straight pen stroke. The lower margin mark resembles a large 2 with a separate dot; it lacks an unequivocal question-mark stem. Both the short phrase before Q at the bottom and the hypothesis two lines above it have horizontal rules.

**Formulas and indices**

**1.**

~~~tex
$n=1$
~~~

**2.**

~~~tex
$\rho=4-\beta=2-\alpha$
~~~

**3.**

~~~tex
$\sigma=\deleted{\unsure{\alpha}}\;2$
~~~

**4.**

~~~tex
$\widetilde\sigma=1$
~~~

**5.**

~~~tex
$\deleted{\unsure{2}}\rho$
~~~

**6.**

~~~tex
$U_\rho\simeq G_m$
~~~

**7.**

~~~tex
$\exists\unsure{1|!}\ u\in U_{\rho=\unsure{2|1}-\alpha}$
~~~

**8.**

~~~tex
$\ne1$
~~~

**9.**

~~~tex
$u$
~~~

**10.**

~~~tex
$f^E$
~~~

**11.**

~~~tex
$=$
~~~

**12.**

~~~tex
$Q_X$
~~~

**13.**

~~~tex
$Q_X$
~~~

**14.**

~~~tex
$u$
~~~

**15.**

~~~tex
$u^2=1$
~~~

**16.**

~~~tex
$u_s\ne1$
~~~

**17.**

~~~tex
$\forall s\in S$
~~~

**18.**

~~~tex
$\rho=0$
~~~

**19.**

~~~tex
$S$
~~~

**20.**

~~~tex
$(2.1_S=0)$
~~~

**21.**

~~~tex
$U_\rho$
~~~

**22.**

~~~tex
$f^E$
~~~

**23.**

~~~tex
$U_\rho$
~~~

**24.**

~~~tex
$Q_X$
~~~

**25.**

~~~tex
$\rho=0$
~~~

**26.**

~~~tex
$\exists$
~~~

**27.**

~~~tex
$\ne1$
~~~

**28.**

~~~tex
$f^E$
~~~

**29.**

~~~tex
$Q_X$
~~~

**30.**

~~~tex
$\sigma\widetilde\rho$
~~~

**31.**

~~~tex
$\exists1$
~~~

**32.**

~~~tex
$u$
~~~

**33.**

~~~tex
$U_\rho$
~~~

**34.**

~~~tex
$\ne1$
~~~

**35.**

~~~tex
$f^E$
~~~

**36.**

~~~tex
$Q_X$
~~~

**37.**

~~~tex
$\sigma=0$
~~~

**38.**

~~~tex
$\widetilde\sigma\widetilde\rho=0$
~~~

**39.**

~~~tex
$n$
~~~

**40.**

~~~tex
$U_\rho$
~~~

**41.**

~~~tex
$f^{\deleted{\unsure{E|X}}E}$
~~~

**42.**

~~~tex
$U_\rho$
~~~

**43.**

~~~tex
$Q_X$
~~~

**44.**

~~~tex
$\widetilde\sigma\widetilde\rho=0$
~~~

**45.**

~~~tex
$\exists$
~~~

**46.**

~~~tex
$U_\rho$
~~~

**47.**

~~~tex
$\ne1$
~~~

**48.**

~~~tex
$f^E$
~~~

**49.**

~~~tex
$Q_X$
~~~

Index and exponent forms containing i or j do not occur.

**Changes**

- `$\exists1\ u` → `$\exists\unsure{1|!}\ u`
- `invarie $f^E$ (ou $Q_X$)` → `invarie $f^E$ (\uline{\unsure{ou}} $Q_X$)`

## Scan 44

2026-11-18T10:57:12Z to 2026-11-18T10:57:36Z (UTC).

**Reading from the image strips**

Upper right only: « Calculs de discriminants », with the last t crossed and a terminal s-like flourish, then « etc. » alone below. No accent in the heading. Centre and bottom thirds are blank except the pencilled number 43 at lower left.

**Comparison with the page file**

The initial C is a plain handwritten capital. The short stroke across the final t is its crossbar. There is no cancellation, formula, marginal note, manuscript page number, date or count. The line break before « etc. » is internal to the heading.

**Formulas and indices**

None on the sheet.

Index and exponent forms containing i or j do not occur.

**Changes**

No change.

## Scan 45

2026-11-18T10:57:37Z to 2026-11-18T10:58:22Z (UTC).

**Reading from the image strips**

f caractérisée par les conditions. a) f inv. par les τᵢ; b) f(s₀)=0, parenthesis « f nulle sur les sommets princ. [or pr…] de Π », c) f(a₀)=1, parenthesis « vecteurs arêtes sont unitaires ». Near main left « ij non consé[c]. »; « τ₀ str. orth. » on right. Final rule goes across two superimposed lines: αᵢ+2 inversibles ... ; τᵢ réflexion strictement orthogonale, with « str. orth » again on last line. Lower half blank apart from show-through, archived 44.

**Comparison with the page file**

The opening bracket embraces f and varphi. The second index in s_j descends below the i alongside it. The end factor in the top product is written with i−1. In the central paired formulas the respective ends of the products are i−1 and i. The inserted equality above −1 has its own s₀ and a₀; the main line beneath still reads a₁. Rechecked j and j−1 in the two following left-hand sides, and j−1 and j−2 on the right. The final qualification has i<j−1, not j<i. At the first right-pointing equivalence row the scalar ring has an upright and an oblique, and its star is high. A long nearly straight stroke crosses the superseded α-condition, but does not cancel the φ-line below. The right-hand words after « sommets » are faint; the final sign is a capital pi.

**Formulas and indices**

**1.**

~~~tex
\[
\left\{\begin{aligned}
f(s_i)&=0\\
\varphi(s_i,s_j)&=-(\alpha_0+2)\cdots(\alpha_{i-1}+2)\qquad 0\le i<j\le n+1
\end{aligned}\right.
\]
~~~

**2.**

~~~tex
$f$
~~~

**3.**

~~~tex
$f$
~~~

**4.**

~~~tex
$\tau_i$
~~~

**5.**

~~~tex
$f(s_0)=0$
~~~

**6.**

~~~tex
$\iff f$
~~~

**7.**

~~~tex
$\Pi$
~~~

**8.**

~~~tex
$f(a_0)=1$
~~~

**9.**

~~~tex
$\iff$
~~~

**10.**

~~~tex
\[
\begin{aligned}
f(a_i)&=(\alpha_0+2)\cdots(\alpha_{i-1}+2) &&0\le i\le n\\
\varphi(a_i,a_j)&=0 &&0\le i<j\le n,\ i\unsure{,|{}}j\ \text{non conséc.}\\
\varphi(a_i,a_{i+1})&=-(\alpha_0+2)\cdots(\alpha_i+2)\\
\varphi(s_0,a_i)&=0 &&1\le i\le n\\
\varphi(s_0,a_0)&=-1
\end{aligned}
\]
~~~

**11.**

~~~tex
\[
\left\{\begin{aligned}
\varphi(s_0,s_1)&=\varphi(s_0,a_1)\inserted{=\varphi(s_0,a_0)}=-1\\
\varphi(s_1,a_0)&=f(a_0)=1\\
\tau_0&\ \text{str. orth.}
\end{aligned}\right.
\]
~~~

**12.**

~~~tex
\[
\begin{aligned}
\varphi(s_j,a_i)&=0 &&0\le j<i\le n,\quad\deleted{\unsure{i\geq j+1}}\\
\varphi(s_j,a_{j\deleted{\unsure{+1}}})&=-(\alpha_0+2)\cdots(\alpha_{j-1}+2)&&0\le j\le n\\
\varphi(s_j,a_{j-1})&=+(\alpha_0+2)\cdots(\alpha_{j-2}+2)&&1\le j\le n+1\\
\varphi(s_j,a_i)&=0&&0\le i<j-1\le n
\end{aligned}
\]
~~~

**13.**

~~~tex
$\alpha_i+2$
~~~

**14.**

~~~tex
$(0\le i\le n-1)\iff\tau_{\unsure{i}}$
~~~

**15.**

~~~tex
\[
\begin{aligned}
\tau_i\ \text{réflexion strictement orthogonale}&\iff(\alpha_0+2),\ldots,(\alpha_{i-1}+2)\in\unsure{k^{*}|K^{*}}\\
(\tau_i\ \text{str. orth. }\ \forall 0\le i\le n)&\iff(\alpha_i+2)\in k^{*}\quad\forall 0\le i\le n-1
\end{aligned}
\]
~~~

Index and exponent forms containing i or j include `_i`, `_j`, `_{i-1}`, `_{i+1}`, `_{j-1}`, `_{j-2}`.

**Changes**

- `\unsure{génér.} du` → `\unsure{génér.|gén.} \unsure{du|au}`
- `n,\ i,j\ \text{non conséc.}` → `n,\ i\unsure{,|{}}j\ \text{non conséc.}`

## Scan 46

2026-11-18T10:58:23Z to 2026-11-18T10:59:24Z (UTC).

**Reading from the image strips**

Top f(sᵢ)=0, varphi(sᵢ,sᵢ)=0 above brace of two forms; multiple discarded f terms. Above line « Attention au chgt de notations »; consecutive range indicators, « i,j non consécutifs ». « Matrice de f par r. à la base (aᵢ)−1≤i≤n » or abbreviated par. Big first matrix started then crossed with left zigzag; replacement f=... . Lower « permutation circulaire ... », subscripts on c, F; two places of heavy ink over a minus or coefficient. Bottom examples F₁,F₂,F₃; old value struck above final factorisation. Left lower number 45.

**Comparison with the page file**

The upper phi-pair has two lowered i's and the next pair i,j; j descends. Reread the i−1, i+1 and a_{−1} endpoints individually. Crossout into the inequality adjoining j is localized to the sign. In the large replacement matrix the first diagonal positions are 0, an overworked 2/1, 2c₀, 2c₁, 2c₂ and 2c₃. Read both outside diagonals separately. First cofactor starts −1,−c₀,0,0, whereas the next minor starts 2c₀,−c₁. A separate zero is placed below the braced c₀ multiple of a determinant. In the lower independent determinant the first entry has index −1, two forms of the coefficient on c_{n−1} overlap at bottom right. The underbrace names n+1 arguments. In the lower recurrence the square is on c₁, not on F; in F₃ it appears again on c₂ inside parentheses. Re-read the dark spots under the leading factors in the last line as strokes of correction, distinct from the live coefficients.

**Formulas and indices**

**1.**

~~~tex
\[
\left\{\begin{aligned}
f(s_i)&=0 &\varphi(s_i,s_i)&=0\\
\varphi(s_i,s_j)&=-(\alpha_0+2)\cdots(\alpha_{i-1}+2)&0&\le i<j\le n+1
\end{aligned}\right.
\]
~~~

**2.**

~~~tex
$f(\unsure{s_0|a_0})$
~~~

**3.**

~~~tex
$f(\unsure{a_0})=$
~~~

**4.**

~~~tex
\[
\left\{\begin{aligned}
f(a_{-1})&=0\inserted{=c_{-2}},\quad f(a_i)=(\alpha_0+2)\cdots(\alpha_{i-1}+2)=c_{i-1}\\
\varphi(a_i,a_j)&=0\quad -1\le i\deleted{\unsure{\le}}<j\le n\qquad\deleted{\unsure{i,j\ \text{non successifs}}}\\
\varphi(a_i,a_{i+1})&=-(\alpha_0+2)\cdots(\alpha_i+2)=\deleted{\unsure{c_i}}-c_i\quad -1\le i\le n-1
\end{aligned}\right.
\]
~~~

**5.**

~~~tex
\[
\begin{aligned}
&0\le i\le n\\
&\deleted{\unsure{0\le i\le n}}\quad\varphi(a_i,a_i)=2f(a_i)=2(\alpha_0+2)\cdots(\alpha_{i-1}+2)\\
&0\le i\le n\\
&i,j\ \text{non consécutifs}
\end{aligned}
\]
~~~

**6.**

~~~tex
$f$
~~~

**7.**

~~~tex
$(a_i)_{-1\le i\le n}$
~~~

**8.**

~~~tex
\[
\deleted{\left(\begin{array}{ccccc}0&-1&&&\\-1&\unsure{2}&\unsure{-c_0}&&\\&\unsure{0}&c_0&&\\&&&c_1&\\&&&&c_{n-1}\end{array}\right)}
\qquad f=\left(\begin{array}{ccccccccc}
0&-1&&&&&&&\\
-1&\unsure{2|1}&-c_0&&&&&&\\
&-c_0&2c_0&-c_1&&&&&\\
&&-c_1&2c_1&-c_2&&&&\\
&&&-c_2&2c_2&-c_3&&&\\
&&&&-c_3&2c_3&&&\\
\text{--}&&&&&&\ddots&&\\
&&&&&&&2c_{n-2}&-c_{n-1}\\
&&&&&&&-c_{n-1}&2c_{n-1}
\end{array}\right)
\]
~~~

**9.**

~~~tex
$\det\unsure{M_{r}f}$
~~~

**10.**

~~~tex
\[
\begin{aligned}
\delta(f)&=\det\left(\begin{array}{ccccc}
-1&-c_0&0&0&\\
0&2c_0&-c_1&0&\\
\big|&\unsure{-}c_1&2c_1&-c_2&\\
\big|&0&\unsure{-}c_2&2c_2&\big|\\
0&\big|&\big|&-c_3&\ddots\\
0&0&0&\text{--}&2c_{n-1}
\end{array}\right)
=-1\det\left(\begin{array}{ccccc}
2c_0&-c_1&&0&\\
-c_1&2c_1&-c_2&&\\
&-c_2&\ddots&\ddots&\\
0&\ddots&&&-c_{n-1}\\
&&&-c_{n-1}&2c_{n-1}
\end{array}\right)\\
&\qquad{}+\underbrace{c_0\det\left(\begin{array}{cccc}0&&&\\0&-&-&\\\big|&&-&-\\0&\text{---}&&\end{array}\right)}_{0}
\end{aligned}
\]
~~~

**11.**

~~~tex
\[
\det\left(\begin{array}{ccccccc}
2c_{-1}&-c_0&0&0&\cdots&&0\\
-c_0&2c_0&-c_1&&&&\vdots\\
0&-c_1&2c_1&&&&\big|\\
\vdots&&&\ddots&&&0\\
\big|&&&&\ddots&&-c_{n-1}\\
0&\text{---}&&&0&-c_{n-1}&\deleted{\unsure{2}}2c_{n-1}
\end{array}\right)
=F_{n+1}(\underbrace{c_{-1},\ldots,c_{n-1}}_{n+1\ \text{arguments}})
\]
~~~

**12.**

~~~tex
\[
\begin{aligned}
-\delta(f)&=\unsure{a|{}}F_n(c_0,\ldots,c_{n-1})=2c_0F_{n-1}(c_1,\ldots,c_{n-1})+c_1\det
\left(\begin{array}{ccccc}
-c_1&-c_2&0&0&\\
0&2c_2&-c_3&0&\\
\big|&-c_3&2c_3&-c_4&\\
\big|&0&-c_4&2c_4&\\
&\big|&0&-c_5&\\
0&0&\vdots&\big|&\\
&&0&\big|&c_{n-1}
\end{array}\right)\\
&=2c_0\inserted{F_{n-1}(c_1,\ldots,c_{n-1})}\unsure{-|+}c_1^2F_{n-2}(c_2,\ldots,c_{n-1})
\end{aligned}
\]
~~~

**13.**

~~~tex
\[
0\to1\to2\to3\ \ldots\to n-1\to0\qquad\text{permutation \uline{circulaire $u$ ou $u^{-1}$}}
\]
~~~

**14.**

~~~tex
\[
\begin{aligned}
F_1(c_0)&=2c_0\qquad F_2(c_0,c_1)=4c_0c_1\unsure{-|+}c_1^2\\
&\hspace{9em}=c_1(4c_0-c_1)\\
F_3(c_0,c_1,c_2)&=2c_0(4c_1c_2-c_2^2)-2c_1^2c_2\\
&\deleted{=8c_0c_1\unsure{c_2}}\\
&=2c_2(4c_0c_1-\deleted{\unsure{2}}c_0c_2-\deleted{\unsure{2}}c_1^2)
\end{aligned}
\]
~~~

Index and exponent forms containing i or j include `_i`, `_j`, `_{i-1}`, `_{i+1}`, `_{-1\le i\le n}`.

**Changes**

- `0&\text{---}&&&0&-c_{n-1}&2c_{n-1}` → `0&\text{---}&&&0&-c_{n-1}&\deleted{\unsure{2}}2c_{n-1}`
- `\margin{-- Attention au chgt de notations}` → `\margin{-- Attention au \unsure{chgt|chgt de} \unsure{de notations|notation}}`

## Scan 47

2026-11-18T10:59:25Z to 2026-11-18T11:00:17Z (UTC).

**Reading from the image strips**

det, cᵢⱼ=0 si i≠j, i,j non consécutifs; admissible (overbrace). « nulle, sauf si », « Supposons n≥3, alors tt cycle de σ est de longueur 1 ou 2 et les cycles de long. 2 sont formés d’entiers consécutifs, donc τ est de la forme ... (τᵢ est la transposition de i,i+1), où i₁ i₂ ... iₚ sont des entiers non contifs ». Below « suites str. cr. d’entiers » strongly crossed; multi-level products, underlined indices and a crossed trial sum. « Supposons matrice symétrique », underlined symétrique; « on trouve ». At bottom dots, horizontal bars with small crossbars, labels c₁, c₂, c₃ ... cₙ and an isolated c.

**Comparison with the page file**

The diagonal pair ii differs from ij, where j descends. The top determinant has a raised question mark and the sum has a heavy S-shaped group sign. The adjoining broken arches below i−2, i−1, i have no decisive arrowheads. In the transposition product the long top strokes of the sigma-like letters may be intrinsic to the sign. Individual subscripts i₁, i₂ and iₚ all have the upright i and a lower numeral or p. The first three underlabels below the next expansion are i₁, i₂, i₃ and the last is iₚ. The alpha subscripts carry overwritten numerals. On the long product, the two c factors reverse the two displayed composite indices and the prefix of the r in the second is overworked. The equality sign in the first sum restriction and inequality in the second are distinct. In the symmetric specialization an inserted n−2p sits over 2. At the foot the ruled bars, isolated vertices, printed-in-ink labels and terminal stray c have been checked against the strip. The extra closing brace in the deleted summation is an encoding repair.

**Formulas and indices**

**1.**

~~~tex
\[
\det\bigl((c_{ij})_{1\le i,j\le n}\bigr)\overset{?}{=}
\qquad c_{ij}=0\quad\text{si } i\ne j,\ i,j\ \text{non consécutifs}
\]
~~~

**2.**

~~~tex
\[
\sum_{\sigma\in\unsure{\mathfrak S_n|\mathcal S_n}}\varepsilon_\sigma
\underbrace{\prod_{i=1}^{n} c_{i,\sigma(i)}}_{\phantom{c_{ii}}}
\quad\unsure{\text{''}}\quad\unsure{*}
\]
~~~

**3.**

~~~tex
$\sigma$
~~~

**4.**

~~~tex
$\overbrace{\forall i\in[1,n],\ \sigma i\in\{i-1,i,i+1\}}^{\sigma\ \text{admissible}}$
~~~

**5.**

~~~tex
$n\ge\unsure{3|2}$
~~~

**6.**

~~~tex
$\sigma$
~~~

**7.**

~~~tex
$\unsure{\tau|\sigma}$
~~~

**8.**

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small]
i-2\arrow[r,dash]\arrow[r,bend right,dash] \& i-1\arrow[r,dash]\arrow[r,bend right,dash] \& i
\end{tikzcd}
~~~

**9.**

~~~tex
\[
\unsure{\overline{\sigma}|\sigma|\tau}_{i_1}\overline{\sigma}_{i_2}\ldots\overline{\sigma}_{i_p}
\qquad 1\le i_1<i_2\ldots<i_p\le n-1
\]
~~~

**10.**

~~~tex
$\overline{\sigma}_i$
~~~

**11.**

~~~tex
$i,i+1$
~~~

**12.**

~~~tex
$i_1\ i_2\ldots i_p$
~~~

**13.**

~~~tex
\[
\deleted{\sum_{\substack{i_1\,i_2\ldots i_p\\\text{suites str. cr.}\\\text{d'entiers}}}}
\quad
\underbrace{1+\alpha_{\unsure{1|0}}}_{i_1}\quad
\underbrace{\deleted{\unsure{i_1+}}3+\alpha_{\unsure{1|0}}+\alpha_2}_{i_2}\quad
\underbrace{i_1+5+\alpha_0+\alpha_{\unsure{2|1}}+\alpha_3}_{i_3}\quad\ldots\quad
\underbrace{\deleted{\unsure{i_1+}}(2\unsure{(p-1)})+\alpha_0\ldots+\alpha_p}_{i_p}
\]
~~~

**14.**

~~~tex
\[
\begin{aligned}
&\deleted{1\le i_1\qquad i'_1+\alpha_1+\cdots+\alpha_{p-1}\le{}}\\
&\alpha_i\in\mathbb N\qquad \alpha_0+\cdots+\alpha_{p-1}\le n-2p
\end{aligned}
\]
~~~

**15.**

~~~tex
\[
\begin{aligned}
&\sum_{1\le p\le[n/2]}(-1)^p
\sum_{\substack{(\alpha_{\unsure{1|0}},\ldots,\alpha_p)\in\mathbb N^p\\\sum\alpha_i=n-2p}}
\deleted{\unsure{\prod_i}}
\prod_{\substack{1\le i\le n\\\text{non de la}\\\text{forme}\\
i\left\{\begin{smallmatrix}(2r-1)+(\alpha_{\unsure{1|0}}\,\ldots+\alpha_r)\\
2r+(\alpha_{\unsure{1|0}}\,\ldots+\alpha_r)\end{smallmatrix}\right.\\1\le r\le p}}
c_{ii}\\
&\quad\prod_{1\le r\le p}
\left(\begin{aligned}
&c_{2r-1+(\alpha_1+\cdots+\alpha_r),\,2r+(\alpha_1+\cdots+\alpha_r)}\\[-2pt]
&c_{2r+(\alpha_1+\cdots+\alpha_r),\,2r-1+(\alpha_1\ldots+\alpha_r)}
\end{aligned}\right)
\end{aligned}
\]
~~~

**16.**

~~~tex
$c_{i\,i+1}=-c_{i+1}$
~~~

**17.**

~~~tex
$c_{ii}=2c_i$
~~~

**18.**

~~~tex
\[
\det\bigl((c_{ij})_{1\le i,j\le n}\bigr)=
\sum_{1\le p\le[n/2]}(-1)^p2^{\inserted{n-2p}}
\sum_{\substack{\alpha_*\in\mathbb N^p\\\alpha_1+\cdots+\alpha_p\le n-2p}}
\prod_i c_i\prod_{1\le\unsure{t|r}\le p}
(c_{2r+\alpha_1+\cdots+\alpha_r})^2
\]
~~~

**19.**

~~~tex
\begin{tikzpicture}[x=.69cm,y=.55cm]
\fill (0,0) circle (1.4pt);
\node[below] at (0,-.07) {$c_1$};
\foreach \a/\b in {.5/1.45,1.7/2.75,2.9/3.42,3.65/4.74,5.5/6.85,7.95/9.55}{
\draw (\a,-.09)--(\a,.09) (\a,0)--(\b,0) (\b,-.09)--(\b,.09);}
\node[below] at (.78,-.12) {$c_2$}; \node[below] at (1.65,-.12) {$c_3$};
\foreach \a in {2.9,3.42,5.05,7.18,7.42,7.66,10,10.35,10.7}{\fill (\a,0) circle (1.15pt);}
\node[below] at (10.72,-.12) {$c_n$};
\end{tikzpicture}
~~~

**20.**

~~~tex
$c$
~~~

Index and exponent forms containing i or j include `_{ij}`, `_{1\le i,j\le n}`, `_{i=1}`, `_{i,\sigma(i)}`, `_{ii}`, `_{i_1}`, `_{i_2}`, `_{i_p}`, `_i`, `_{i_3}`, `_{i\,i+1}`, `_{i+1}`.

**Changes**

- `\overline{\sigma}_{i_1}` → `\unsure{\overline{\sigma}|\sigma|\tau}_{i_1}`
- `\text{d'entiers}}}` → `\text{d'entiers}}}}`
- `i_1+5+\alpha_0+\alpha_2+\alpha_3` → `i_1+5+\alpha_0+\alpha_{\unsure{2|1}}+\alpha_3`

## Scan 48

2026-11-18T11:00:17Z to 2026-11-18T11:01:42Z (UTC).

**Reading from the image strips**

Upper left: paired aᵢ,a′ⱼ cases; i et j non consécutifs, last sign differs between j and i in the first lower edge case. « Considérons ... projectiv... de c, orth. aux a′ᵢ »; « Cas où par ... » beside the lower end of the curved enclosure, with « on fait λᵢ=−1 pour ... ». Boxed ψ on right hatched across en bloc. Recurrence starts ζₙ=1 and ζₙ₋₁=2; curving brace leads to cancellation on ζₙ₋₄, underlined terms on the next line. « λπ= » above crossed bottom equation; A below f-expression. Final line has ρ with subscripted ζ’s, star over a₋₁, 2f(c′) on right.

**Comparison with the page file**

Compared the prime to the star on each member of the two a-bases. In the case array the left argument is indexed by i, the right by a descending j; in its conditions j−1, j, j+1 are on separate lines. The explicit a′ expansion has both stars and a prime, with lower j−1, j, j+1. The boxed endpoint formulas have several diagonal cancellation strokes. The notation line on the right has c_{−1}=1 and c_n=c_{n+1}=0; its outer boundary connects material distant on the sheet. In the expansion of f the second sum starts at −1 whereas the first right-hand sum starts at 0. Each recurrence shifts from n−1 through n−4 and a separate n−5 is followed by dots. The n−3 box has no visible closing ordinary parenthesis. The bottom pairing has a question over an unfinished equality, an older crossed trial involving lambda, and a final product with distinct subscripts 0 and −1. The small letter after a′ᵢ in the f(aᵢ) line can also be the remnant of a parenthesis. Both angle brackets, primes, equality signs and stars in the bottom computation were compared at their own locations.

**Formulas and indices**

**1.**

~~~tex
\[
\langle a_i,a'_j\rangle=
\begin{cases}
0&\text{si } i\ne j,\ i\text{ et }j\text{ non consécutifs}\\
1&\text{si \deleted{\unsure{voisins}} }i=j-1\\
\deleted{\unsure{+}}\lambda_j-1&\text{si \deleted{\unsure{égal}} }i=j\\
-\lambda_j+1+\alpha_j&\deleted{\unsure{\text{si $j$ voisin}}}\quad i=j+1
\end{cases}
\]
~~~

**2.**

~~~tex
\[
\begin{aligned}
a_i&=s_{i+1}-s_i\\
a'_j&=s_j^*+\lambda_j s_{j+1}^*+(1+\alpha_j)(s_{j+2}^* \ldots+s_{n+1}^*)\qquad 0\le j\le n\\
a'_n&=
\end{aligned}
\]
~~~

**3.**

~~~tex
\[
\deleted{\boxed{\begin{aligned}\psi(a_{-1})&=-a_0^*\\\psi(a_n)&=-c_{n-2}a_{n-1}^*+2c_{n-1}a_n^*\end{aligned}}}
\]
~~~

**4.**

~~~tex
\[
\left\{\begin{aligned}
a'_j&=a_{j-1}^*+\underbrace{(\lambda_j-1)}_{-2\ \text{si }\lambda_j=-1}a_j^*+
\underbrace{(1-\lambda_j+\alpha_j)}_{\beta_j=2+\alpha_j\ \text{si }\lambda_j=-1}a_{j+1}^*
\quad\deleted{\unsure{*}}0\le j\le n-1\\
a'_n&=a_{n-1}^*+(\lambda_n-1)a_n^*\deleted{\unsure{+}}\\
\pi&=a_{-1}^*\\
s_j&=a_{-1}+\ldots+a_{j-1}\qquad0\le j\le n+1
\end{aligned}\right.
\]
~~~

**5.**

~~~tex
\[
\begin{aligned}
f(a_i)\deleted{\unsure{\varphi(}}a'_i\unsure{1|)|{}}+\psi(\unsure{a_i|a'_i})&=0\\
f\bigl(\sum_{-1}^{n}\zeta_i a_i\bigr)&=\sum_{i=0}^{n}c_{i-1}\zeta_i^2\\
&\unsure{-|+}\sum_{-1\le i\deleted{\unsure{<}}\le n-1}c_i\zeta_i\zeta_{i+1}
\end{aligned}
\]
~~~

**6.**

~~~tex
$\psi(a_i)=-c_{i-1}a_{i-1}^*+2c_{i-1}a_i^*-\unsure{c_2|c_i}a_{i+1}^*$
~~~

**7.**

~~~tex
$0\le i\le n-1$
~~~

**8.**

~~~tex
$\longleftrightarrow$
~~~

**9.**

~~~tex
$c_{-1}=1$
~~~

**10.**

~~~tex
\[
\begin{aligned}
c_0&=(\alpha_0+2),\ldots\quad c_i=(2+\alpha_0)\cdots(2+\alpha_i)\\
&0\le i\le n\hspace{6em}0\le i\le n-1\\
c_n&=c_{n+1}=0
\end{aligned}
\]
~~~

**11.**

~~~tex
$c$
~~~

**12.**

~~~tex
$a'_i$
~~~

**13.**

~~~tex
$\lambda_i=-1$
~~~

**14.**

~~~tex
$0\le i\le n$
~~~

**15.**

~~~tex
\[
\begin{aligned}
c'&=\sum_{-1}^{n}\zeta_i a_i\quad(\zeta_n=1)\\
\zeta_{n-1}-2\zeta_n&=0\qquad\deleted{\unsure{\zeta_{n-1}=2}}\quad\boxed{\zeta_n=1,\ \zeta_{n-1}=2}\\
\zeta_{n-2}-2\zeta_{n-1}+(\alpha_{n-1}+2)\zeta_n&=0\qquad\boxed{\zeta_{n-2}=-(\alpha_{n-1}-2)}\\
\zeta_{n-3}\underbrace{-2\zeta_{n-2}+(\alpha_{n-2}+2)\zeta_{n-1}}_{\substack{2(\alpha_{n-1}-2)+(\alpha_{n-2}+2)2\\=2(\alpha_{n-1}+\alpha_{n-2})}}&=0
\qquad\boxed{\zeta_{n-3}=-2(\alpha_{n-1}+\alpha_{n-2}}\\
\zeta_{n-4}\underbrace{\unsure{-|+}2\zeta_{n-3}+(\alpha_{n-3}+2)\zeta_{n-2}}_{4(\alpha_{n-1}+\alpha_{n-2})\unsure{-|+}(\alpha_{n-3}+2)(\alpha_{n-1}-2)}&=0
\end{aligned}
\]
~~~

**16.**

~~~tex
\[
\boxed{\begin{aligned}
\zeta_{n-4}&=\deleted{\unsure{\alpha_{n-1}}(\alpha_{n-3}+2)+4\alpha_{n-2}+4+{}}\\
&-4-2(\alpha_{n-1}+2\alpha_{n-2}+\alpha_{n-3})\\
&\quad+\alpha_{n-1}\alpha_{n-3}
\end{aligned}}
\]
~~~

**17.**

~~~tex
\[
\begin{aligned}
&2\underline{\alpha_{n-1}}+4\underline{\alpha_{n-2}}+\underline{4}-\underline{\alpha_{n-1}\alpha_{n-3}}+2\underline{\alpha_{n-3}}\\
&\zeta_{n-5}=\ldots
\end{aligned}
\]
~~~

**18.**

~~~tex
\[
\begin{aligned}
\pi&=a_{-1}^*\\
\pi(c')&=\underline{\rho}(\underbrace{\alpha_0,\ldots,\alpha_{n-1}}_{A})=\rho=\zeta_{-1}\\
&\underline{\rho}\in\mathbb Z[A_0,\ldots,A_{n-1}]\\
c&=\frac{c'}{\rho}\\
f(c')&=\underbrace{\underline\sigma(\alpha_0,\ldots,\alpha_{n-1})}_{\underline\sigma\in\mathbb Z[A_0,\ldots,A_{n-1}]}=\sigma\\
f(c)&=\sigma/\rho^2\qquad 2\sigma=-\zeta_0\zeta_{-1}=-\rho\zeta_0
\end{aligned}
\]
~~~

**19.**

~~~tex
\[
\begin{aligned}
2f(c')&=\langle c',\psi(c')\rangle\overset{?}{=}\\
&\deleted{\psi(c')=\inserted{\lambda\pi={}}\lambda a_{-1}^*\qquad\lambda=\langle a_{-1},\psi(c')\rangle=\varphi(a_{-1},c')}\\
\langle a_i,\psi(c')\rangle&=\varphi(a_i,c')=\langle c',\underbrace{\psi(a_i)}_{-f(a_i)a'_i}\rangle
=\deleted{\unsure{-f(a_i)}}\qquad/\,\text{si }0\le i\le n\\
&=-f(a_i)\langle c',a'_i\rangle=0\ \deleted{\text{si }0\le i\le n}\\
\langle a_{-1},\psi(c')\rangle&=\langle c',\underbrace{\psi(a_{-1})}_{-a_0^*}\rangle=-\deleted{\unsure{\zeta_{-1}}}\zeta_0=\\
\psi(c')&=-\zeta_0 a_{-1}^*\\
&\qquad 2f(c')=\langle c',-\zeta_0a_{-1}^*\rangle=-\zeta_0\zeta_{-1}
\end{aligned}
\]
~~~

Index and exponent forms containing i or j include `_i`, `_j`, `_{i+1}`, `_{j+1}`, `_{j+2}`, `_{j-1}`, `_{i=0}`, `_{i-1}`, `_{-f(a_i)a'_i}`.

**Changes**

- `a'_i\unsure{1|{}}+\psi(a_i)` → `a'_i\unsure{1|)|{}}+\psi(\unsure{a_i|a'_i})`
- `\unsure{rappelons}` → `\unsure{rappelons|rappelons que}`

## Scan 49

2026-11-18T11:01:43Z to 2026-11-18T11:02:46Z (UTC).

**Reading from the image strips**

Δ double-prime at top over a former expression. Upper right: « ordre n », box at recurrence; Δ′ described by si n pair, si n impair. « Posons », first β list, « n−1 arguments fixés? ». Right bracket index of reduced deltas and divisors; small examples end « ... 4c₀c₁−c₀c₂−c₁² ». Lower shoulders « dgt homog[ène]? », « monique au signe près », bracketed « il n’y a pas de cancellation de termes » preceded by underlined NB. Main « Le monôme M ... s’écrit aussi ». Bottom circle « Attention p→0! »; at edge « ... altern… n−1 divise n! » possibly two lines of a qualification, very hard. Most crossing in lower subscripts and on the suspended sums; J, J′, J″, J‴ distinguished by small upright marks.

**Comparison with the page file**

Read the n+2 and n order notes as two pointers to the corresponding matrices. In the integrality lines distinguished upper Δ, lower δ, tilde, and primes individually. The division by 2 belongs to the odd branch. The second reduced small-degree formula visibly ends in a closing parenthesis. In the expansion, i in J′ has no descender and j in J″ does. The set J is the union of J_i. In the B monomial the first two exponents are n and n−1+ε₂, then the overworked B subscript before n−2+ε₃, then ε_n. The diagram bears 1, k, n in the same order. Checked i≥k, the exceptional i=k−1 and the prime-count at the end of the note. The arrow at the foot of the sum points to a warning whose ink can be read « n−1 et non n! »; the upper endpoint in the drawn sum itself is n. None of the cancelled specifications were promoted to live restrictions.

**Formulas and indices**

**1.**

~~~tex
$\Delta_{\unsure{n+2}}(0,1,c_0,\ldots,c_{n-1})$
~~~

**2.**

~~~tex
\[
\begin{aligned}
\deleted{\unsure{\det}}\ \Delta_n(\underbrace{c_0,\ldots,c_{n-1}}_{n\ \text{arg.}})
&=\unsure{-}\det\left(\begin{array}{cccccccc}
0&-1&0&0&0&0&\cdots&0\\
-1&2&-c_0&0&0&0&\cdots&0\\
0&-c_0&2c_0&-c_1&0&0&\cdots&\vdots\\
0&0&-c_1&2c_1&-c_2&0&\cdots&\vdots\\
0&0&0&&\ddots&-c_3&&0\\
\vdots&\vdots&\vdots&&&&&-c_{n-1}\\
0&0&0&\text{--}&\text{--}&0&-c_{n-1}&2c_{n-1}
\end{array}\right)_{\leftarrow(\text{ordre }n+2)}\\
&=\det\left(\begin{array}{ccccccc}
2c_0&-c_1&0&0&0&\text{---}&0\\
-c_1&2c_1&-c_2&0&0&&\\
0&-c_2&2c_2&-c_3&0&\cdots&\\
0&0&-c_3&2c_3&-c_4&&\vdots\\
\text{--}&\text{--}&\text{--}&\text{--}&\text{---}&\text{--}&-c_{n-1}\\
0&0&0&0&\cdots\ 0&-c_{n-1}&2c_{n-1}
\end{array}\right)_{\leftarrow\,\text{ordre }n}
\end{aligned}
\]
~~~

**3.**

~~~tex
\[
\boxed{\Delta_n(c_0,\ldots,c_{n-1})=2c_0\Delta_{n-1}(c_1,\ldots,c_{n-1})\unsure{-|+}c_1^2\Delta_{n-2}(c_2,\ldots,c_{n-1})}
\]
~~~

**4.**

~~~tex
\[
\Delta'_n(c_0,\ldots,c_{n-1})=
\begin{cases}
\Delta_n(c_0,\ldots,c_{n-1})&\text{si $n$ \deleted{\unsure{im}}pair}\\
\frac12\Delta_n(c_0,\ldots,c_{n-1})&\text{si $n$ impair}
\end{cases}
\]
~~~

**5.**

~~~tex
\[
\left.\begin{aligned}
c_0&=\beta_0,\ \unsure{c}\\
c_1&=\beta_0\beta_1\\
&\ldots\\
c_{n-1}&=\beta_0\beta_1\ldots\beta_{n-1}
\end{aligned}\right\}\quad n\!-\!1\ \text{\unsure{arguments} }\beta_i
\]
~~~

**6.**

~~~tex
\[
\begin{aligned}
\delta_n(\beta_0,\ldots,\beta_{n-1})&=\Delta_n(\beta_0,\beta_0\beta_1,\ldots,\beta_0\beta_1\ldots\beta_{n-1})\\
\delta'_n(\beta_0,\ldots,\beta_{n-1})&=\Delta'_n(\ldots)=\begin{cases}
\delta_n(\beta_0,\ldots,\beta_{n-1})&n\ \text{\unsure{pair}}\\
\frac12\delta_n(\beta_0,\ldots,\beta_{n-1})&n\ \text{impair}
\end{cases}
\end{aligned}
\]
~~~

**7.**

~~~tex
\[
\begin{aligned}
\Delta_n,\Delta'_n,\deleted{\unsure{\Delta'_n}}\inserted{\widetilde{\Delta}'_{\unsure{n|j}}}&\in\mathbb Z[C_0,\ldots,C_{n-1}]\\
\delta_n,\delta'_n,\widetilde{\delta}'_n&\in\mathbb Z[B_0,\ldots,B_{n-1}]\\
\Delta'_n[C_0,\ldots,C_{n-1}]&=C_{n-1}\widetilde{\Delta}'_{\unsure{n-1|n}}(C_0,\ldots,C_{n-1})\\
\delta'_n[B_0,\ldots,B_{n-1}]&=B_{n-1}\widetilde{\delta}'_n(B_0,\ldots,B_{n-1})
\end{aligned}
\]
~~~

**8.**

~~~tex
\[
\begin{aligned}
\Delta_1(c_0)&=2c_0,\quad\Delta'_1(c_0)=c_0\quad\widetilde{\Delta}'_1(c_0)=1\\
\Delta_2(c_0,c_1)&=4c_0c_1-c_1^2=c_1(4c_0-c_1)\quad\widetilde{\Delta}'_2(c_0,c_1)=4c_0-c_1)\\
\Delta_3(c_0,c_1,c_2)&=2c_2(4c_0c_1-c_0c_2-c_1^2),\quad
\Delta'_3=\deleted{\unsure{2}}c_2(4c_0c_1-c_0c_2-c_1^2),\\
&\ldots\qquad\inserted{\widetilde{\Delta}'_3(c_0,c_1,c_2)=4c_0c_1-c_0c_2-c_1^2}
\end{aligned}
\]
~~~

**9.**

~~~tex
\[
\begin{aligned}
\Delta_n(C_0,\ldots,C_{n-1})={}&\sum_{0\le p\le[n/2]}(-1)^p2^{n-2p}\sum_{\substack{\text{suites de }p\\\deleted{\unsure{\text{intervalles de}}}\\\text{él. de }\mathcal P_2([0,n-1])\\\text{disjoints}\\
\deleted{\unsure{K}}\,J_1\ldots J_p,\ \deleted{\unsure{\text{à deux él.}}}}}
\prod_{i\in J'}C_i\prod_{j\in J''}C_j^2
\end{aligned}
\]
~~~

**10.**

~~~tex
$J=\bigcup_{1\le i\le p}J_i$
~~~

**11.**

~~~tex
$J'=[0,n-1]\setminus J$
~~~

**12.**

~~~tex
$J''=$
~~~

**13.**

~~~tex
$J_i$
~~~

**14.**

~~~tex
$(J''\in\mathcal P_p([0,n-1]))$
~~~

**15.**

~~~tex
$\unsure{\Delta_n(C_0,\ldots,C_{n-1})}=$
~~~

**16.**

~~~tex
$M=\prod_{i\in J'}C_i\prod_{j\in J''}C_j^2$
~~~

**17.**

~~~tex
\[
\begin{aligned}
&\deleted{F_n(c_1,\ldots,c_n)=\beta_0}\\
&B_0^n B_1^{n-1+\varepsilon_2}B_{\unsure{3|2}}^{n-2+\varepsilon_3}\ldots B_{n-1}^{\varepsilon_n}
\qquad\varepsilon_k\in\{0,1\}\qquad2\le k\le n\\
&\varepsilon_k=1\ \text{sss }\ k\in J'''\quad\text{(il y \deleted{\unsure{en}} a \unsure{$p$ tels|plus} $k$)}
\end{aligned}
\]
~~~

**18.**

~~~tex
\begin{tikzpicture}[x=.75cm,y=.6cm]
\draw (0,0)--(5.4,.08);
\foreach \x/\lab in {0/1,2.6/k,5.4/n}{\fill (\x,.08*\x/5.4) circle(1pt);\node[below] at (\x,0) {$\lab$};}
\end{tikzpicture}
~~~

**19.**

~~~tex
\[
M=\prod_{1\le i\le n}C'_i\qquad
C'_i=\begin{cases}
C_i&\text{si }i\in J'\\
C_j&\text{si }j\in J''\\
C_{j+1}&\text{si }j\in\unsure{\complement J'|\complement J''}\ \unsure{J''}
\end{cases}
\]
~~~

**20.**

~~~tex
\[
\begin{aligned}
\delta_n(B_0,\ldots,B_{\unsure{n|n-1}})&=
 B_0^n B_1^{n-1}\ldots B_{n-1}^{1}\underbrace{L_n(B_1,\ldots,B_{n-1})}_{\text{polynôme \deleted{\unsure{homogène de degré $[n/2]$}}}}
 \deleted{\unsure{\text{degré}}}
\end{aligned}
\]
~~~

**21.**

~~~tex
$p\to0$
~~~

**22.**

~~~tex
$C'_i$
~~~

**23.**

~~~tex
$B_k$
~~~

**24.**

~~~tex
$i\ge k$
~~~

**25.**

~~~tex
$i=k-1$
~~~

**26.**

~~~tex
$i\in J^{\unsure{'''|''}}$
~~~

**27.**

~~~tex
$k\in J''$
~~~

**28.**

~~~tex
\[
\begin{aligned}
L_n(B_1,\ldots,B_{n-1})
&=\sum_{0\le p\le[n/2]}(-1)^p2^{n-2p}
\sum_{\substack{\deleted{\unsure{\text{suites de }p\,J_i}}\\J\in\mathcal P_p([1,n-1])\\J\text{ ne contient pas 2}\\\text{entiers consécutifs}}} B_J\\
&=2^n\unsure{-|+}2^{n-2}\sum_{\unsure{1|0}\le i\le n-1}B_i
+2^{n-4}\sum_{\substack{1\le i<j\le n-1\\j\ne i+1}}B_iB_j\\
&\quad-2^{n-6}\sum_{\substack{1\le i<j<k\le n\\\vdots\quad\vdots}}B_iB_jB_k+\ldots
\end{aligned}
\]
~~~

**29.**

~~~tex
$n-1$
~~~

**30.**

~~~tex
$n$
~~~

Index and exponent forms containing i or j include `_i`, `_{i\in J'}`, `_{j\in J''}`, `_j`, `_{1\le i\le p}`, `_{1\le i\le n}`, `_{j+1}`.

**Changes**

- `\unsure{mon signe} des lignes` → `\unsure{mon signe|sous-signe} des \unsure{lignes|signes}`
- `de cancell. de termes` → `de \unsure{cancell.tion|cancell.} de termes`
- `a \unsure{plus} $k$` → `a \unsure{$p$ tels|plus} $k$`
- `\margin{Attention, pas 0!}` → `\margin{Attention, \unsure{pas 0|$p\to0$}!}`
- `\unsure{Attention}, non circulaire !` → `\unsure{Attention}, \unsure{$n-1$ et non $n$|non circulaire} !`

## Scan 50

2026-11-18T11:02:47Z to 2026-11-18T11:03:43Z (UTC).

**Reading from the image strips**

L₁, L′₁ distinctly separate. Crossed first sum above product of adjacent primed B's, upper right Bᵢ = B′ᵢ + 4 with an extra stroke. Small-degree list mixed capital B, α; NB underlined reversal, line divide. In middle of L₄ calculation « 2α₂+ » circled. Rightmost minus or plus before 4 is a black square; bottom determinant first diagonal numeral has correction, brace below arguments. Lower small δ list contains a long crossed provisional line, plus struck L₂ and L₃ above; end of the δ₂ row continues on right in cancelled calculations, a long slant crosses the whole group. Archival 49 at lower left.

**Comparison with the page file**

The first sum is crossed, the equality at the top right survives, and primes occur in the consecutive-B products. In the L₃ trial the pen closes the parenthesis after B₂ and again after the discarded term. For L₄ the j in the sum descends, and the last bound has an overwritten 3. In the continuing calculation several pairs of parentheses and whole products have strokes through them. The circled 2α₂+ is attached to the inner sum by a curl. The reversal line is set apart by NB and a divider. The matrix starts with a live 2, a cancelled following c, and adjacent −c₀. The next formula has Δ_{n+1} at left and exponent 2 on the c in the last term. The small cases include a prime on δ′₃ and a subscript on its last alpha whose numeral is ambiguous. In the cancelled computation at the right, the horizontal rows and two by two determinant were reread through the broad diagonal cross. The four examples have separate subscripts 1 through 4.

**Formulas and indices**

**1.**

~~~tex
\[
\deleted{\Pi_p(B_1,\ldots,B_n)=\sum_{J\in\mathcal P_p[1,n]}}\qquad B_i=B'_i+4
\]
~~~

**2.**

~~~tex
\[
\begin{aligned}
\deleted{\unsure{\sum}}\quad B'_1B'_2&=B'_2B'_3\ldots=B'_nB'_{n+1}=0\\
(2-\tfrac{B_1}{2})(2-\tfrac{B_2}{2})\ldots(2-\tfrac{B_n}{2})&=\frac{(-1)^n}{2^{n}}.
\end{aligned}
\]
~~~

**3.**

~~~tex
\[
\begin{aligned}
L_1&=2\qquad L'_1=1\\
L_2&=4-(B_1\deleted{\unsure{+B_2}})=\deleted{\unsure{4-(\alpha_0+\alpha_1)}\ (\alpha_0+{}}2-\alpha_1=-(\alpha_1-2)\\
L_3&=8-2(B_1+B_2)\deleted{\unsure{+B_3}})=-2\bigl[\unsure{(}\alpha_1+\alpha_2\unsure{)}\deleted{\unsure{+2+2}}\bigr]\\
L_4&=\underbrace{16-4(B_1+B_2+B_3\deleted{\unsure{+B_4}})+\bigl(\sum_{1\le i\unsure{\le|<}j\le3}B_iB_j}_{\phantom{16}}
-(B_1B_2+B_2B_3+B_3B_4)
\end{aligned}
\]
~~~

**4.**

~~~tex
\[
\begin{aligned}
&\deleted{(2-\tfrac{B_1}{\unsure{2|1}})(2-\tfrac{B_2}{2})}\\
&-4(\alpha_1+\alpha_2+\alpha_3+\deleted{\unsure{\alpha_4}})-\unsure{8}+ \bigl[\deleted{(\alpha_0+2)(\alpha_1+2)}+(\alpha_0+2)(\alpha_2+2)+\deleted{\unsure{(\alpha_0+2)(\alpha_3+2)}}\\
&\hspace{17em}+\deleted{\unsure{(\alpha_1+2)(\alpha_3+2)}}\bigr]\\
&\deleted{=-4-4(\alpha_0+\alpha_1+\alpha_2\unsure{+\alpha_3})+2(\alpha_0+\alpha_2+\alpha_0+\alpha_3+\alpha_1+\alpha_3)+\alpha_0\alpha_2+\alpha_0\alpha_3}+\alpha_1\alpha_3\\
&\hspace{16em}\deleted{\unsure{2\alpha_0+2\alpha_2+\alpha_2+2\alpha_3}}\\
&=-4-2(\alpha_1+\inserted{2\alpha_2+}\alpha_3)+(\alpha_1\alpha_3\deleted{\unsure{+\alpha_0\alpha_2+\alpha_0\alpha_3}})=(\alpha_1-2)(\alpha_3-2)\unsure{-|+}4(\alpha_2+2)
\end{aligned}
\]
~~~

**5.**

~~~tex
$L_{n-1}(B_1,\ldots,B_{n-1})=L_{n-1}(B_{n-1},\ldots,B_1)$
~~~

**6.**

~~~tex
\[
\begin{aligned}
\det\left(\begin{array}{cccccc}
2\deleted{\unsure{c_0}}&-c_0&0&&&\\
-c_0&2c_0&-c_1&0&&\\
0&-c_1&2c_1&&&\\
0&0&-c_2&\ddots&&0\\
&&&&c_{\unsure{n-2|n-1}}&-c_{n-1}\\
&\ldots&&0&-c_{n-1}&2c_{n-1}
\end{array}\right)_{\leftrightarrow\,\substack{\deleted{\unsure{\text{ordre }n}}\\\text{ordre }n+1}}
&=\Delta_{n+1}(\underbrace{1,c_0,\ldots,c_{n-1}}_{n+1\ \text{arg}})=2\Delta_n(c_0,\ldots,c_{n-1})\\
&\hspace{7em}-c_0^2\Delta_{n-1}(c_1,\ldots,c_{n-1})
\end{aligned}
\]
~~~

**7.**

~~~tex
\[
\begin{aligned}
&=\delta_{n+1}(1,B_0,\ldots,B_{n-1})=B_0^n B_1^{n-1}\ldots B_{n-1}L_{n+1}(\deleted{\unsure{1,}}B_0,\ldots,B_{n-1})\\
&\deleted{\unsure{L_2}\delta_{n+1}(1,B_0)=B_{\unsure{n|0}}\ldots}
\qquad \deleted{\begin{aligned}L_2(1,B_0)&=4-{}\\ L_3(1,B_0,&\end{aligned}}\\
&\delta_2(1,B_0)\deleted{\unsure{B_1}}=B_0 L_2(1,B_0)=B_0(4-B_0)=-(\alpha_0+2)(\alpha_0-2)=4-\alpha_0^2\\
&\delta'_3(1,B_0,B_1)=B_0^2B_1L'_3(\deleted{\unsure{1,}}B_0,B_1)=\deleted{\unsure{B_0^2B_1(4}}-B_0^2B_1(\alpha_0+\unsure{\alpha_2|\alpha_1})\\
&\delta_4(1,B_0,B_1,B_2)=B_0^3B_1^2B_2\underbrace{L_4(B_0,B_1,B_2)}_{(\alpha_0-2)(\alpha_2-2)-4(\alpha_1+2)}
\end{aligned}
\]
~~~

**8.**

~~~tex
$\begin{aligned}
\det\begin{pmatrix}2c_0&-c_1\\-c_1&2c_1\end{pmatrix}
&=4c_0c_1-c_1^2=\\
&=c_1(4c_0-c_1)\\
&=B_0^2B_1(4-B_1)
\end{aligned}$
~~~

Index and exponent forms containing i or j include `_i`, `_j`.

**Changes**

- `8-2(B_1+B_2\deleted` → `8-2(B_1+B_2)\deleted`
- `\sum_{1\le i\le j\le3}` → `\sum_{1\le i\unsure{\le|<}j\le3}`

## Comparison of recurring signs before assembly

On 35, 39 and 45 the open-loop action or polar-form glyph was compared with the three-pronged ψ on 40 and 48. The × in a direct product on 39 differs from the circled tensor sign. Scans 38–43 separate lower ρ on U from the tilde over a coefficient. The paired stars above D on 39–40 differ from the star marking a dual basis vector on 48. The upright 1 beside ∃ is not consistently distinguishable from !. Scans 45–46 have the same i and descending j on s and a. In the change-of-notation note on 46 the enlargement supports **chgt de** followed by a possible singular or plural (*notations* / *notation*). The pre-freeze local reading was consolidated accordingly. Scans 46, 49 and 50 distinguish the F notation and triangular Δ from the looped δ; the capital B and C in polynomial expressions on 49–50 were kept distinct from β and c in evaluations. The pages are handwritten throughout. No typewriter double strikes were identified.

## Occurrence index for i and j

The table expands the formula lists above. It lists subscript and superscript arguments containing literal i or j in the pre-witness page files. Repetitions in a line are retained. A number in parentheses is the number of successive identical occurrences. The page-by-page readings above also describe free indices and inequalities.

| Scan | Page-file line | Index or exponent in source order |
|---|---|---|
| 35 | — | None |
| 36 | 2 | `_i` (2) |
| 36 | 6 | `_{i-1}`, `_i` (2), `_{i+1}`, `_{i-1}`, `_i` |
| 36 | 7 | `_{i-1}`, `_i`, `_{i-1}` |
| 36 | 8 | `_i`, `_{i+1}`, `_i` |
| 36 | 13 | `_i`, `_{i-1}` (2), `_i` (2), `_{i+1}` |
| 36 | 18 | `_{\unsure{i\|i-1}}` |
| 36 | 19 | `_{\unsure{i-1\|i+1}}` |
| 36 | 27 | `_{i-1}`, `_i` |
| 36 | 28 | `_{i-1}`, `_i` |
| 36 | 31 | `_i`, `_{i-1}`, `_i`, `_{i-1}`, `_i`, `_{i+1}`, `_i`, `_{i-1}` (2), `_i`, `_{i+1}`, `_i` (2) |
| 36 | 35 | `_i` |
| 36 | 40 | `^{\rho_{i-1}}`, `_{i-1}`, `_{\substack{\deleted{\unsure{=}}\Vert\\\{a_{i-1},a_i\}^{\perp}}}`, `_{i-1}`, `_i` |
| 36 | 41 | `^{\rho_i}`, `_i`, `_{\substack{\Vert\\\{a_i,a_{i+1}\}^{\perp}}}`, `_i`, `_{i+1}` |
| 36 | 43 | `_{i-1}`, `_i` (2), `_{i+1}` |
| 36 | 44 | `_{i-1}`, `_i` (2), `_{i+1}` |
| 36 | 49 | `_i` (2), `_{i+1}`, `_i`, `_{i+1}`, `_i` |
| 36 | 53 | `_i` (3), `_{\deleted{\unsure{2}}\cos 2\theta_i}`, `_i` (2) |
| 37 | 3 | `_{\unsure{*\|\bullet\|i}}` |
| 38 | 25 | `_i` (4) |
| 39 | 11 | `_i` |
| 40 | 6 | `_i` |
| 41 | — | None |
| 42 | — | None |
| 43 | — | None |
| 44 | — | None |
| 45 | 4 | `_i` |
| 45 | 5 | `_i`, `_j`, `_{i-1}` |
| 45 | 11 | `_i` |
| 45 | 19 | `_i`, `_{i-1}` |
| 45 | 20 | `_i`, `_j` |
| 45 | 21 | `_i`, `_{i+1}`, `_i` |
| 45 | 22 | `_i` |
| 45 | 37 | `_j`, `_i` |
| 45 | 38 | `_j`, `_{j\deleted{\unsure{+1}}}`, `_{j-1}` |
| 45 | 39 | `_j`, `_{j-1}`, `_{j-2}` |
| 45 | 40 | `_j`, `_i` |
| 45 | 44 | `_i`, `_{\unsure{i}}` |
| 45 | 48 | `_i`, `_{i-1}` |
| 45 | 49 | `_i` (2) |
| 46 | 4 | `_i` (3) |
| 46 | 5 | `_i`, `_j`, `_{i-1}` |
| 46 | 12 | `_i`, `_{i-1}` (2) |
| 46 | 13 | `_i`, `_j` |
| 46 | 14 | `_i`, `_{i+1}`, `_i` (3) |
| 46 | 22 | `_i` (3), `_{i-1}` |
| 46 | 28 | `_i`, `_{-1\le i\le n}` |
| 47 | 3 | `_{ij}`, `_{1\le i,j\le n}` |
| 47 | 4 | `_{ij}` |
| 47 | 9 | `_{i=1}`, `_{i,\sigma(i)}`, `_{\phantom{c_{ii}}}`, `_{ii}` |
| 47 | 21 | `_{i_1}`, `_{i_2}`, `_{i_p}` |
| 47 | 24 | `_i` |
| 47 | 27 | `_{\substack{i_1\,i_2\ldots i_p\\\text{suites str. cr.}\\\text{d'entiers}}}` |
| 47 | 29 | `_{i_1}` |
| 47 | 30 | `_{i_2}` |
| 47 | 31 | `_{i_3}` |
| 47 | 32 | `_{i_p}` |
| 47 | 38 | `_i` |
| 47 | 45 | `_{\substack{(\alpha_{\unsure{1\|0}},\ldots,\alpha_p)\in\mathbb N^p\\\sum\alpha_i=n-2p}}`, `_i` |
| 47 | 46 | `_i` |
| 47 | 47 | `_{\substack{1\le i\le n\\\text{non de la}\\\text{forme}\\ i\left\{\begin{smallmatrix}(2r-1)+(\alpha_{\unsure{1\|0}}\,\ldots+\alpha_r)\\ 2r+(\alpha_{\unsure{1\|0}}\,\ldots+\alpha_r)\end{smallmatrix}\right.\\1\le r\le p}}` |
| 47 | 50 | `_{ii}` |
| 47 | 59 | `_{i\,i+1}`, `_{i+1}`, `_{ii}`, `_i` |
| 47 | 64 | `_{ij}`, `_{1\le i,j\le n}` |
| 47 | 67 | `_i` (2) |
| 48 | 3 | `_i`, `_j` |
| 48 | 7 | `_j` |
| 48 | 8 | `_j` (2) |
| 48 | 14 | `_i`, `_{i+1}`, `_i` |
| 48 | 15 | `_j` (3), `_{j+1}`, `_j`, `_{j+2}` |
| 48 | 26 | `_j`, `_{j-1}`, `_j`, `_{-2\ \text{si }\lambda_j=-1}`, `_j` (2) |
| 48 | 27 | `_j` (2), `_{\beta_j=2+\alpha_j\ \text{si }\lambda_j=-1}`, `_j` (3), `_{j+1}` |
| 48 | 31 | `_j`, `_{j-1}` |
| 48 | 37 | `_i` (4) |
| 48 | 38 | `_i` (2), `_{i=0}`, `_{i-1}`, `_i` |
| 48 | 39 | `_{-1\le i\deleted{\unsure{<}}\le n-1}`, `_i` (2), `_{i+1}` |
| 48 | 43 | `_i`, `_{i-1}` (3), `_i` (2), `_{i+1}` |
| 48 | 48 | `_i` (2) |
| 48 | 54 | `_i` (2) |
| 48 | 58 | `_i` (2) |
| 48 | 97 | `_i` (3), `_{-f(a_i)a'_i}`, `_i` (2) |
| 48 | 98 | `_i` |
| 48 | 99 | `_i` (2) |
| 49 | 45 | `_i` |
| 49 | 60 | `_{\unsure{n\|j}}` |
| 49 | 82 | `_{i\in J'}`, `_i`, `_{j\in J''}`, `_j` |
| 49 | 85 | `_{1\le i\le p}`, `_i` (2) |
| 49 | 89 | `_{i\in J'}`, `_i`, `_{j\in J''}`, `_j` |
| 49 | 106 | `_{1\le i\le n}`, `_i` |
| 49 | 107 | `_i` |
| 49 | 108 | `_i` |
| 49 | 109 | `_j` |
| 49 | 110 | `_{j+1}` |
| 49 | 121 | `_i` |
| 49 | 127 | `_{\substack{\deleted{\unsure{\text{suites de }p\,J_i}}\\J\in\mathcal P_p([1,n-1])\\J\text{ ne contient pas 2}\\\text{entiers consécutifs}}}`, `_i` |
| 49 | 128 | `_{\unsure{1\|0}\le i\le n-1}`, `_i` |
| 49 | 129 | `_{\substack{1\le i<j\le n-1\\j\ne i+1}}`, `_i`, `_j` |
| 49 | 130 | `_{\substack{1\le i<j<k\le n\\\vdots\quad\vdots}}`, `_i`, `_j` |
| 50 | 3 | `_i` (2) |
| 50 | 18 | `_{1\le i\unsure{\le\|<}j\le3}`, `_i`, `_j` |
