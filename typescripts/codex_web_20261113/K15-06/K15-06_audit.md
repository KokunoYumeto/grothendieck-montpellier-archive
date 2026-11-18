# Second reading of cote 15, K15-06

The independent ink lists were written before reopening the corresponding page files. Source line references refer to the individual files at the second reading. The registers include crossed-out material. The witness check follows this audit and is recorded separately.

## Scan 172

2026-11-18T12:46:33Z to 2026-11-18T12:47:01Z UTC.

**Independent reading of accents, endings and unusual words**

Top right, three lines. Calculs (small final hook), de cohomologie, absolue des Motifs, de Tate Z(n). There are no accents in these words. Uppercase M, capital T, lower-case n, round brackets, final dot. Bottom left 171.

**Comparison with the ink**

The hook at the end of the first word is so short that singular and plural remain possible. The capital M has two joined ascenders. The Z has a second slant and long horizontal strokes. No i/j indices, corrections, line through live letters, marginal writing or typed material. The middle and bottom thirds are blank apart from the archive pencil number.

**Formulas, including insertions and diagrams, in reading order**

- Source line 3 `$\mathbb{Z}(n)$`

Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

No change.

## Scan 173

2026-11-18T12:47:01Z to 2026-11-18T12:48:46Z UTC.

**Independent reading of accents, endings and unusual words**

Top-right ordre de q mod ℓ dans; upper left engendré par, frob (q high); module de t.f. sur le quel π opère continûment (the mark above the u is pale). Non canoniquement below the equals sign; two instances of quel que soit i. Ker, Coker, i.e., mod p-gpes ? and id in parentheses. Spec, Zariski, ouvert de Zariski de Spec Z, et n ≠ 0 (tout i). The separation of le and quel is conspicuous. No added accent on Spec. Signs to revisit: thin upright between the two Qℓ groups, slips under the not-congruent sign and under si i ≠ 3, underlining of coefficient letters and double stroke of the low H.

**Comparison with the ink**

Read the field link as a horizontal stroke without a head. The π annotation is below it. The second M has an oblique pen stroke and dot above the inked π underneath. The strokes under the second congruence, the extra stroke after the first Qℓ, the entire abandoned H-with-Z line, the previous Q under Z, the dense stroke under si/sf, and the underlying letters in the restriction formula are cancellations. The extra piece after the integral answer Z is detached and very low. The wavy baselines under Q and Z are deliberate and stop at the letters; neither n nor the following parentheses are struck. The three case rows align beside the quotient. In the upper right ω has two low arcs and a separate lowered ℓ. The second matching round-ended rule is a call sign. In the last group a second upright on the left of H is conspicuous in the pair at left, while H in the restriction has a single upright. F has a second left stem; Z has a second diagonal. The i in the general vanishing, in the universal conditions, in both Spec displays and in the source of restriction has a detached dot. The exponent on its target is faint; no clear j tail. All additions are on handwriting.

**Formulas, including insertions and diagrams, in reading order**

- Source line 2 `$\circ\!\!-\!\!-\quad \omega_\ell(q)={}$`
- Source line 2 `$q\bmod\ell$`
- Source line 2 `$(\mathbb{Z}/\ell\mathbb{Z})^{*}$`

Source line 4

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=large]
k=\mathbb{F}_q \arrow[r,dash,"\pi\simeq\widehat{\mathbb{Z}}"'] \& \bar{k}
\end{tikzcd}
~~~

- Source line 7 `$f=\mathrm{frob}^{q}$`
- Source line 7 `$M$`
- Source line 7 `$\mathbb{Z}_\ell$`
- Source line 7 `$\pi$`

Source line 8

~~~tex
\[
\begin{aligned}
H^0(\pi,M)&=M^\pi=M^{(1-f)}=\mathrm{Ker}\,(1-f)_M\\
H^1(\pi,M)&=M_{\deleted{\unsure{f|i}}\pi}=M_{(1-f)}=\mathrm{Coker}\,(1-f)_M=M/(1-f)M\\
H^i(\pi,M)&=0\qquad\text{si }\ i\geq 2
\end{aligned}
\]
~~~


Source line 16

~~~tex
\[
H^0(\pi,\mathbb{Z}_\ell(n))=0\quad\text{si }\ n\ne0,\quad =\mathbb{Z}_\ell\quad\text{si }\ n=0
\]
~~~


Source line 19

~~~tex
\[
\begin{aligned}
H^1(\pi,\mathbb{Z}_\ell(n))&\underset{\text{\inserted{non canoniquement}}}{=}\mathbb{Z}_\ell/(1-q^n)\mathbb{Z}_\ell=\begin{cases}
\mathbb{Z}_\ell&\text{si }\ n=0\\
0&\text{si }\ \ell\nmid(1-q^n)\quad\text{i.e. }\deleted{\unsure{n\ne0}}\ n\not\equiv0\ (\omega_\ell(q))\\
\mathbb{Z}/\ell^{\unsure{v|\nu}_\ell(1-q^n)}&\text{si }\ \underbrace{\ell\mid1-q^n}_{\text{i.e. }n\equiv0\ (\omega_\ell(q))},\ n\ne0
\end{cases}
\end{aligned}
\]
~~~

- Source line 28 `$\circ\!\!-\!\!-$`

Source line 29

~~~tex
\[
\left\{\begin{aligned}
H^{\unsure{i|0}}(\pi,\mathbb{Q}_\ell(n))&=0\quad\text{si }\ n\ne0,\quad\text{quel que soit }i\\
H^0(\pi,\mathbb{Q}_\ell)&=\mathbb{Q}_\ell\deleted{\unsure{f|1}},\ H^1(\pi,\mathbb{Q}_\ell)=\mathbb{Q}_\ell
\end{aligned}\right.
\]
~~~


Source line 36

~~~tex
\[
\deleted{H^i(\pi,\underline{\mathbb{Z}}(n))}
\]
~~~


Source line 39

~~~tex
\[
\left\{\begin{aligned}
\mathbb{H}^i(\mathbb{F}_q,\underset{\sim}{\mathbb{Q}}(n))&=0\quad\text{si }\ n\ne0,\quad\text{quel que soit }i\\
\mathbb{H}^0(\mathbb{F}_q,\underset{\sim}{\mathbb{Q}})&=\mathbb{Q},\ \mathbb{H}^1(\mathbb{F}_q,\underset{\sim}{\mathbb{Q}})=\underset{\sim}{\mathbb{Q}}.
\end{aligned}\right.
\]
~~~


Source line 45

~~~tex
\[
\left\{\begin{aligned}
H^0(\mathbb{F}_q,\underset{\sim}{\deleted{\mathbb{Q}}\mathbb{Z}})&=\mathbb{Z}\unsure{,|{}_\ell}\ (\text{mod }p\text{-gpes }?),\quad H^1(\mathbb{F}_q,\underset{\sim}{\mathbb{Z}})=\mathbb{Z}\quad(\text{mod }p\text{-gpes }?)\\
H^0(\mathbb{F}_q,\underset{\sim}{\mathbb{Z}}(\underset{\substack{\vert\\n\ne0}}{n}))&=0\quad(\text{id}),\quad H^1(\mathbb{F}_q,\underset{\sim}{\mathbb{Z}}(\underset{\substack{\vert\\n\ne0}}{n}))=\mathbb{Z}/(1-q^n)\mathbb{Z}\quad(\text{mod }p\text{-gpes }?)
\end{aligned}\right.
\]
~~~


Source line 53

~~~tex
\[
\begin{aligned}
\mathbb{H}^i(\mathrm{Spec}\,\mathbb{Z},\mathbb{Z}(1))&=\begin{cases}0&\text{\unsure{si|sf}}\deleted{\unsure{<}}\ i\ne3\\\mathbb{Z}&\text{si }\ i=3\end{cases}\\
\mathbb{H}^i(\mathrm{Spec}\,\mathbb{Z},\mathbb{Z})&=\begin{cases}0&\text{si }\ i\ne0\\\mathbb{Z}&\text{si }\ i=0\end{cases}
\end{aligned}
\]
~~~


Source line 59

~~~tex
\[
H^i(\mathrm{Spec}(\mathbb{Z}),\deleted{\unsure{\mathbb{Z}}}\mathbb{Q}(n))\xrightarrow{\sim} H^{\unsure{i|1}}(\deleted{\unsure{k}}U,\deleted{\unsure{\mathbb{Z}}}\mathbb{Q}(n))
\]
~~~

- Source line 62 `$U$`
- Source line 62 `$\mathrm{Spec}\,\mathbb{Z}$`
- Source line 62 `$n\ne0$`
- Source line 62 `$i$`

Indices/exponents containing literal i or j, in reading order: `^i`, `_{\text{i.e. }n\equiv0\ (\omega_\ell(q))}`, `^{\unsure{i|0}}`, `^i`, `^i`, `^i`, `^i`, `^i`, `^{\unsure{i|1}}`. See also operator indices or pullbacks in the register.

**Changes**

- `\underset{\text{non canoniquement}}{=}` -> `\underset{\text{\inserted{non canoniquement}}}{=}`
- `\mathbb{Z}_\ell\\[-2pt]
&=\begin{cases}` -> `\mathbb{Z}_\ell=\begin{cases}`
- `v_\ell(1-q^n)` -> `\unsure{v|\nu}_\ell(1-q^n)`
- `\mathbb{Z}\unsure{,}\ (\text{mod }` -> `\mathbb{Z}\unsure{,|{}_\ell}\ (\text{mod }`
- `de $\mathrm{Spec}\,\mathbb{Z}$ et` -> `de $\mathrm{Spec}\,\mathbb{Z}$\unsure{,} et`

## Scan 174

2026-11-18T12:48:47Z to 2026-11-18T12:49:55Z UTC.

**Independent reading of accents, endings and unusual words**

Spec Z (plain small pec), x at the point. Parenthetic minus one, square minus two. In the right-hand note: peu de mérite, car si i ≥ 4, les deux mbs doivent être = 0. Below: Si n ≠ 1, Si n = 1, tout i (underlined), [est-ce nul ??]; H³(U,M) underwritten = 0 ?; sauf pour i = 3, où on trouve Q ! Small i has a point in the exponents of H; ! and the long tail of * are distinct over i in the first display. A prior coefficient is covered by dark strokes, and another has diagonal hatching.

**Comparison with the ink**

The heading Z has a second diagonal. In the drawing the dot lies a little left of centre. There is a tiny pale disconnected stroke above and to its left, as well as a tick near the right end. The shriek has a distinct point. The thin upright after the equals sign has no identifying cross-stroke. The three connectors in the first long row have unequal ends; preserve the distinction between clearly pointed and nearly flat ends. In the central array the faint S and the small mark below i were checked in both rows; the latter does not warrant identifying every occurrence as x. Cancellations are the former Z below Q, the short H-start before the brace, a crossed stroke inside terminal 0, hatching before the lower M-coefficient Q, a small overwriting below Q, a dark sign after the twist, and the old sign at the first Q to the power S. Underlines go with Si n ≠ 1 and tout i, not with the neighbouring cases. Both right-hand notes are independent; the rule alongside peu de mérite does not cross its words. No typed matter or j exponent.

**Formulas, including insertions and diagrams, in reading order**

- Source line 2 `$\mathrm{Spec}\,\mathbb{Z}$`

Source line 4

~~~tex
\begin{tikzpicture}
\draw (0,0) .. controls (.8,-.02) and (1.4,.04) .. (2,0.04) .. controls (3,.05) and (3.55,-.08) .. (4.4,-.02);
\draw[gray!45,thin] (1.46,.37)--(1.55,.39);
\fill (1.8,.035) circle (1.5pt) node[below] {$x$};
\draw[thin] (4.08,-.05)--(4.05,-.12);
\end{tikzpicture}
~~~


Source line 10

~~~tex
\[
i_x^!(M)=\unsure{1|\vert}\,i_x^*(M)(-1)[-2]
\]
~~~


Source line 13

~~~tex
\[
\cdots\unsure{-|\to}H^{i-2}(x,i_x^*(M)(-1))\longrightarrow H^i(X,M)\unsure{-|\to}H^{\unsure{i|2}}(U,M)\unsure{-|\to}H^{i-1}(x,i_x^*(M)(-1))\to\cdots
\]
~~~


Source line 16

~~~tex
\[
M=\underset{\sim}{\deleted{\mathbb{Z}}\mathbb{Q}}(n)
\]
~~~

- Source line 19 `$i\geq4$`
- Source line 19 `$=0$`

Source line 20

~~~tex
\[
\deleted{\unsure{H^i}}\quad
\left\{\begin{aligned}
i\ne1,2,3\qquad&H^i(X,M)\xrightarrow{\sim}H^i(U,M)\\
0\to H^1(X,M)&\to H^1(U,M)\to H^0(S,i_x^*(M)(-1))\longrightarrow H^2(X,M)\\
&\longrightarrow H^2(U,M)\to H^1(S,i_{\unsure{x|\bullet}}^*(M)(-1))\to H^3(X,M)\\
&\longrightarrow\underset{\inserted{=0\,?}}{H^3(U,M)}\to\deleted{\unsure{H}}0
\end{aligned}\right.
\]
~~~


Source line 30

~~~tex
\[
M=\deleted{\unsure{\mathbb{Z}}}\mathbb{Q}_{\deleted{\unsure{S|\ell}}}(n),\quad i_{\unsure{\bullet|x}}^*(M)(\unsure{-1})\deleted{\unsure{x}}=\mathbb{Q}(n-1)_S
\]
~~~


Source line 33

~~~tex
\[
\text{\uline{Si $n\ne1$}}\qquad H^i(X,\mathbb{Q}(n))\xrightarrow{\sim}H^i(U,\mathbb{Q}(n))\qquad\text{\uline{tout $i$}}
\]
~~~

- Source line 36 `$??$`
- Source line 38 `$n=1$`

Source line 39

~~~tex
\[
\begin{aligned}
0\unsure{-|\to}H^1(X,\mathbb{Q}(1))&\to H^1(U,\mathbb{Q}(1))\to\deleted{\unsure{\mathbb{Z}}}\mathbb{Q}^S\longrightarrow H^2(X,\mathbb{Q}(1))\to\\
&H^2(U,\mathbb{Q}(1))\to\mathbb{Q}^S\longrightarrow H^3(X,\mathbb{Q}(1))\longrightarrow0
\end{aligned}
\]
~~~

- Source line 45 `$H^i(X,\mathbb{Q}(1))=0$`
- Source line 45 `$i=3$`
- Source line 45 `$\mathbb{Q}$`

Indices/exponents containing literal i or j, in reading order: `^{i-2}`, `^i`, `^{\unsure{i|2}}`, `^{i-1}`, `^i`, `^i`, `^i`, `^i`, `^i`, `^i`. See also operator indices or pullbacks in the register.

**Changes**

- `\fill (1.8,.035) circle` -> `\draw[gray!45,thin] (1.46,.37)--(1.55,.39);
\fill (1.8,.035) circle`

## Scan 175

2026-11-18T12:49:56Z to 2026-11-18T12:51:36Z UTC.

**Independent reading of accents, endings and unusual words**

engendré par frob with raised q and an extra short heavy stroke lower down; a) si π opère trivialement, c'est Hom; b) Si M est fini, donc π opère à travers π/U. Acute in engendré, grave in opère and à. Ker, Im, Hom, lim; Si n ≡ 0 (N) near the foot. No final word after the last sum. The letter after Si at the right is π, the variable in the calculation changes between f and x. Three long cancellation diagonals, in addition to horizontal strokes through individual starts and a heavily retraced numerator sign.

**Comparison with the ink**

The whole working is under three long oblique strikes. Within that deletion, the lower q under Fro(b), Mπ, the last line of the xya calculation, a short positive-power start, faint parentheses after n−1, the abandoned φ near the inverse, the beginning of the following quotient, and the earlier upright at M are independently cancelled or overwritten. The dark sign in the positive numerator retains its doubt. On the line for the cube, the last inter-term stroke is nearly horizontal with no definite vertical; its small following exponent is poorly closed. On the right, the 1 in (1−f) has an earlier stem. The quotient to the right of the inverse rule has no further factor on the final line. The arrow from the right of the quotient-group sequence descends to H²; comparison with the whole shows that it is separate from the diagonal cancellation. The isolated left H¹ is a marginal note. F is double-stroked, the k has a bar, the Z below the field line has a hat, and the M's are upright angular letters. No unstruck prose, typed additions or j indices.

**Formulas, including insertions and diagrams, in reading order**


Source line 4

~~~tex
\begin{tikzcd}[ampersand replacement=\&]
k=\mathbb{F}_q \arrow[r,dash,"\pi=\widehat{\mathbb{Z}}"'] \& \bar{k}
\end{tikzcd}
~~~

- Source line 7 `$\unsure{\mathrm{Frob}|\mathrm{frob}}^{q}_{\deleted{\unsure{q}}}$`

Source line 9

~~~tex
\[
\begin{aligned}
H^0(\pi,M)&=M^\pi\\
H^1(\pi,M)&=\varprojlim_n H^1\underbrace{(\pi,M/\ell^n M)}=
\end{aligned}
\]
~~~

- Source line 16 `$\pi$`
- Source line 16 `$\mathrm{Hom}(\pi,M)$`
- Source line 18 `$M$`
- Source line 18 `$\pi$`
- Source line 18 `$\pi/U\simeq\mathbb{Z}/n\mathbb{Z}$`
- Source line 20 `$H^1(\pi,M)$`

Source line 21

~~~tex
\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
0\unsure{-|\to} H^1(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})\unsure{-|\to} H^1(\pi,M)\arrow[r] \&
\underset{\substack{\shortparallel\\\mathrm{Hom}(U,M^\pi)}}{H^0(\pi/U,\mathrm{Hom}(U,M))}\arrow[d]\\
\& H^2(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})
\end{tikzcd}
~~~


Source line 26

~~~tex
\[
\deleted{M_\pi}\quad\frac{\mathrm{Ker}\,N}{\mathrm{Im}\,(1-f)}
\]
~~~


Source line 30

~~~tex
\[
\begin{aligned}
\varphi(xy)&=\varphi(x)+x\varphi(y)\\
\varphi(x)&=xa-a\\
\varphi(xy)&=xya-a\\
&=xa-a+x(ya-a)\\
&=\deleted{\unsure{xya-a}}
\end{aligned}
\]
~~~


Source line 39

~~~tex
\[
\underset{\substack{\shortparallel\\1+f+\cdots+f^{n-1}}}{N}\qquad 1-f
\]
~~~


Source line 42

~~~tex
\[
\varphi(f^n)=
\begin{cases}
(1+x+\cdots+x^{n-1})\varphi(x)=\dfrac{1\deleted{\unsure{+}}-x^n}{1-x}\,\varphi(x)&\text{si }n\geq1\\
0&\text{si }n=0\\
\unsure{(}&
\end{cases}
\]
~~~


Source line 50

~~~tex
\[
\varphi(f^{\unsure{n|m}})=1+x+\phantom{x} +x^{n-1}
\]
~~~


Source line 53

~~~tex
\[
\begin{aligned}
&\deleted{\varphi(x^n)=\varphi(x)+}\\
\varphi(x^{\unsure{2|1}})&=\varphi(x)+x\varphi(x)\\
\varphi(x^3)&=\varphi(x)+x\varphi(x)\unsure{-|+}x^{\unsure{2|3}}\varphi(x)\\
\varphi(x^n)&=(1+x+\cdots+x^{n-1}\deleted{\unsure{(x)}})\varphi(x)\\
0=\varphi(x^{-1}x)&=\varphi(x^{-1})+x^{-1}\varphi(x)\\
\deleted{\unsure{\varphi(x}}\qquad\varphi(x^{-1})&=-x^{-1}\varphi(x)\\
\varphi(x^{-n})&=-(1+x^{-1}+\cdots+x^{-(n-1)})x^{-1}\varphi(x)\\
&\deleted{\unsure{=-(x}}\quad-\frac{1-x^{-n}}{1-x^{-1}}x^{-1}\varphi(x)\\
&=\frac{1-x^{-n}}{1-x}
\end{aligned}
\]
~~~


Source line 67

~~~tex
\[
\begin{aligned}
\unsure{\varphi(f)}\qquad Z^1(\mathbb{Z},M)&\simeq M\\
B^1(\mathbb{Z},M)&\simeq (1-f)M\\
H^1(\mathbb{Z},M)&\simeq \deleted{\unsure{1}}M/(\deleted{\unsure{1}}1-f)M
\end{aligned}
\]
~~~


Source line 74

~~~tex
\[
\frac{1-f^n}{1-f}\,\varphi(f)
\]
~~~

- Source line 77 `$n\equiv0\quad(N)$`

Source line 78

~~~tex
\[
1+f+\cdots+f^{n-1}
\]
~~~


Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

- `\mathrm{Frob}^{q}` -> `\unsure{\mathrm{Frob}|\mathrm{frob}}^{q}`
- `\underbrace{H^1(\pi,M/\ell^n M)}` -> `H^1\underbrace{(\pi,M/\ell^n M)}`
- `a) Si $\pi$` -> `a) \unsure{si|Si} $\pi$`
- `\[
0\unsure{-|\to} H^1(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})\unsure{-|\to} H^1(\pi,M)\to
\underset{\substack{\shortparallel\\\mathrm{Hom}(U,M^\pi)}}{H^0(\pi/U,\mathrm{Hom}(U,M))}
\]
\[
\hfill\downarrow\qquad
H^2(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})
\]` -> `\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
0\unsure{-|\to} H^1(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})\unsure{-|\to} H^1(\pi,M)\arrow[r] \&
\underset{\substack{\shortparallel\\\mathrm{Hom}(U,M^\pi)}}{H^0(\pi/U,\mathrm{Hom}(U,M))}\arrow[d]\\
\& H^2(\pi/U,\underset{\substack{\shortparallel\\M}}{M^U})
\end{tikzcd}}`
- `\varphi(x^2)&` -> `\varphi(x^{\unsure{2|1}})&`
- `x\varphi(x)+x^2\varphi(x)` -> `x\varphi(x)\unsure{-|+}x^{\unsure{2|3}}\varphi(x)`
- `\unsure{1}}M/(1-f)M` -> `\unsure{1}}M/(\deleted{\unsure{1}}1-f)M`

## Scan 176

2026-11-18T12:51:36Z to 2026-11-18T12:52:54Z UTC.

**Independent reading of accents, endings and unusual words**

Lorsque; opening cancelled X est / l'on est sous les conditions de; les anneaux localisés stricts (last letters compressed) de X sont factoriels; on tire aisément de (5.3.); d'où, la proposition struck. Proposition 5.4., supposons que l'on soit sous les conditions de 5.1. a); X étant irréductible de pt gén. y; Alors les homomorphismes canoniques sont injectifs. Comme, il s'ensuit; Corollaire 5.5., Sous les mêmes conditions, est injectif. Ainsi, s'identifie, alors, à un sous-gpe du groupe de Brauer ... du corps des fonctions K=k(y) de X. Théorème 5.6., Soit X un préschéma, Si X est un schéma local, extension / morphisme, fini étale surjectif (galoisien si on veut), qui annule. Accent strokes in localisés, aisément, où, étant, irréductible, gén., mêmes, à, Théorème, préschéma, schéma, étale. The r of galoisien and the ending of fini need comparison.

**Comparison with the ink**

The words about the hypotheses at the very top and la proposition after d'où both have independent strike-throughs. The long insertion between 5.1. a) and Alors begins with X; the leader returns before Alors, not into homomorphismes. In the proposition, the last letter of the point's name looks like y elsewhere in the same display. Check the second R: round bowl and slanting leg, small X underneath, star above. H has one left stroke. Div has an underline stopping before X. The first map and the corollary map have flat ends; the second map in the proposition has a tip. Underlines are on Proposition, Corollaire and Théorème, leaving their numbers outside. The long addition beginning Soit X belongs to the theorem heading. A second insertion replaces the words about coming from an element, and a shorter insertion adds alors at s'identifie. Visible previous forms also occur at Br(K), extension, tel que … soit and the verb before annule. Rechecked the two consecutive group nouns: the first has only the g-p-e trace after the hyphen; the second is long enough for groupe. No typed additions or independent marginal note.

**Formulas, including insertions and diagrams, in reading order**

- Source line 2 `$X$`
- Source line 2 `$X$`

Source line 3

~~~tex
\[
H^1(X,\underline{\unsure{\mathrm{Div}|\mathrm{Dv}}}_X)=0
\]
~~~

- Source line 8 `$X$`
- Source line 8 `$\unsure{y|\eta}$`

Source line 9

~~~tex
\[
H^2(X,\mathrm{G}_{m\,X})\unsure{-|\to}H^2(X,\mathrm{R}_X^*)\longrightarrow H^2(y,\mathrm{G}_{m\,y})=\mathrm{Br}(y)
\]
~~~

- Source line 14 `$\mathrm{Br}(X)\subset H^2(X,\mathrm{G}_{m\,X})$`

Source line 17

~~~tex
\[
\mathrm{Br}(X)\unsure{-|\to}\mathrm{Br}(y)
\]
~~~

- Source line 22 `$\mathrm{Br}(X)$`
- Source line 22 `$\deleted{\unsure{\mathrm{B}}}\mathrm{Br}(K)$`
- Source line 22 `$K=k(y)$`
- Source line 22 `$X$`
- Source line 24 `$X$`
- Source line 24 `$\unsure{\zeta|\xi}\in H^2(X,\mathrm{G}_m)$`
- Source line 24 `$X$`
- Source line 24 `$\zeta\in H^2(X,\mathrm{G}_{m\,X})$`
- Source line 24 `$\zeta$`
- Source line 24 `$\mathrm{Br}(X)$`
- Source line 24 `$f\colon X'\to X$`
- Source line 24 `$\zeta|X'$`
- Source line 24 `$\zeta$`
- Source line 24 `$\zeta$`

Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

- `un sous-groupe du groupe` -> `un \unsure{sous-gpe|sous-groupe} du groupe`

## Scan 177

2026-11-18T12:52:55Z to 2026-11-18T12:54:25Z UTC.

**Independent reading of accents, endings and unusual words**

si / Si before conditions; peu de mérite (final short t-like stroke), car les deux sont nuls. Bottom somme des inv., underlined in two lines. No other accented prose. Isolated μ under the cancelled μₙ sequence; two more abandoned H expressions. In the first case table x is down at right, above it i; first glyph of second table's first answer heavily inked. Three middle answers have a bracket at their right. Next pair of degree lists is divided from Si by a diagonal rule. The last group has an equality-like pair of strokes below it followed by 0 ?.

**Comparison with the ink**

The first sequence, the start H³→H³ and the incomplete H with subscript x each have their own strike. The detached μ between them is live; its descending left line is part of the letter. Two small dark loops survive beside the i in the X and U terms of the long sequence. The S under the last H is larger than the x under the sheaf H. Compare H underlined, Z with two slants, and the two adjacent Gm subscripts. The heavy zero at the head of the five cases was written over another answer. The square bracket spans i=1,2,3 only; the double strokes below terms on the two bottom lines mean that the values beneath are attached to those terms. The bar over the X in the single restriction formula is heavier than the bars in the sequences. In the bottom left group both the exponent and the first letter in parentheses are overwritten; the latter still has an upstroke curving to the left. The margin reads peu de mérite, car les deux sont nuls; the two-line arrow label reads somme / des inv. The question mark under the penultimate group is separate from 0. The i marks are short with dots; no j descender or typed correction.

**Formulas, including insertions and diagrams, in reading order**


Source line 2

~~~tex
\[
\deleted{\mu_n\longrightarrow\mathrm{G}_m\xrightarrow{n}\mathrm{G}_m}
\]
~~~

- Source line 6 `$\mu$`

Source line 8

~~~tex
\[
\deleted{H^3(X,\mathrm{G}_m)\longrightarrow H^3}
\]
~~~


Source line 11

~~~tex
\[
\deleted{H_x^i(}
\]
~~~


Source line 14

~~~tex
\[
H^i_S(X,\mathrm{G}_m)\unsure{-|\to}H^{\deleted{\unsure{0|3}}i}(X,\mathrm{G}_m)\to H^{\deleted{\unsure{0|3}}i}(U,\mathrm{G}_m)\unsure{-|\to}H^{\unsure{i+1|i-1}}_S(X,\mathrm{G}_m)\to
\]
~~~


Source line 17

~~~tex
\[
\underline{H}^i_x(\mathrm{G}_m)=
\begin{cases}
0&\text{si }i=0\\
\mathbb{Z}_x&\text{si }i=1\\
0&\text{si }i\geq2
\end{cases}
\]
~~~


Source line 25

~~~tex
\[
H^i_S(X,\mathrm{G}_m)=H^{i-1}(S,\mathbb{Z})=
\left\{\begin{array}{lll}
\deleted{\unsure{\mathbb{Z}}}0&\text{si }i=0\\
\mathbb{Z}^S&\text{si }i=1\\
0&\text{si }i=2&\smash{\left.\rule[-2.3ex]{0pt}{6.5ex}\right]}\\
H^1(S,\mathbb{Q}/\mathbb{Z})&\text{si }i=3\\
0&\text{si }i\geq4
\end{array}\right.

\]
~~~


Source line 36

~~~tex
\[
0\unsure{-|\to}\mathbb{Z}\to\mathbb{Q}\unsure{-|\to}\mathbb{Q}/\mathbb{Z}\unsure{-|\to}0
\]
~~~


Source line 40

~~~tex
\[
\begin{aligned} i&=1,3\\i&=0,2\end{aligned}
\qquad\big/\qquad \text{Si }i\ne0,1,2,3,\qquad H^i(\unsure{\bar{X}|X},\mathrm{G}_m)\xrightarrow{\sim}H^i(U,\mathrm{G}_m)
\]
~~~


Source line 46

~~~tex
\[
\begin{aligned}
0&\to\underset{\substack{\shortparallel\\\mathbb{Z}^*=\{+1,-1\}}}{H^0(\bar{X},\mathrm{G}_m)}
\to H^0(\bar{U},\mathrm{G}_m)\to\mathbb{Z}^S\to
\underset{\substack{\shortparallel\\0}}{H^1(\bar{X},\mathrm{G}_m)}
\unsure{-|\to}\underset{\substack{\shortparallel\\0}}{H^1(\bar{U},\mathrm{G}_m)}
\to\underset{\substack{\shortparallel\\0}}{H^2_S(\bar{X},\mathrm{G}_m)}
\end{aligned}
\]
~~~


Source line 55

~~~tex
\[
\begin{aligned}
0&\to\underset{\substack{\shortparallel\\0}}{H^{\unsure{2|1}}(\bar{\deleted{\unsure{U|X}}X},\mathrm{G}_m)}
\to H^2(\bar{U},\mathrm{G}_m)\to\underset{\substack{\shortparallel\\(\mathbb{Q}/\mathbb{Z})^S}}{H^1(S,\mathbb{Q}/\mathbb{Z})}
\xrightarrow[\substack{\text{\uline{somme}}\\\text{\uline{des inv.}}}]{}
\underset{\substack{\shortparallel\\\mathbb{Q}/\mathbb{Z}}}{H^3(\bar{X},\mathrm{G}_m)}
\to\underset{\substack{\shortparallel\\0\,?}}{H^3(\bar{U},\mathrm{G}_m)}\to0
\end{aligned}
\]
~~~


Indices/exponents containing literal i or j, in reading order: `^i`, `^i`, `^{\unsure{i+1|i-1}}`, `^i`, `^i`, `^{i-1}`, `^i`, `^i`. See also operator indices or pullbacks in the register.

**Changes**

- `H^i(X,\mathrm{G}_m)\to H^i(U,\mathrm{G}_m)\unsure` -> `H^{\deleted{\unsure{0|3}}i}(X,\mathrm{G}_m)\to H^{\deleted{\unsure{0|3}}i}(U,\mathrm{G}_m)\unsure`
- `\left\{\begin{array}{ll}` -> `\left\{\begin{array}{lll}`
- `0&\text{si }i=2\\
H^1` -> `0&\text{si }i=2&\smash{\left.\rule[-2.3ex]{0pt}{6.5ex}\right]}\\
H^1`
- `\quad \raisebox{.1ex}{$\left.\vphantom{\begin{matrix}1\\2\\3\end{matrix}}\right]$}` -> ``
- `H^{\unsure{2|1}}(\bar{X},\mathrm{G}_m)` -> `H^{\unsure{2|1}}(\bar{\deleted{\unsure{U|X}}X},\mathrm{G}_m)`

## Scan 178

2026-11-18T12:54:25Z to 2026-11-18T12:55:39Z UTC.

**Independent reading of accents, endings and unusual words**

Ker (capital K) appears twice in the upper computations and once at the integral kernel. Conditions si i ≥ 3. At right petite modification, pour ℓ = 2, en dim 0; no written accent, except the possible dot in modification. The t crossbars in petite are long. A short struck group before the first H¹ with μ. G has a rounded single outline; μ has its left stem prolonged upwards as well as downwards. Lower X has no bar; local extra tails beneath the Q's in rows 1–3. The last Q and first two zeroes have dark central strokes.

**Comparison with the ink**

Bars sit above U in the top three blocks. The final four equations use X, without a bar. S is high on the free factors; n is high on ℓ inside the μ subscript. Read the signs over equals as tildes where drawn. The pair at integral degree 1 and degree 2 shares a left brace; degree 0 sits above it. The two t strokes across petite are similar to the author's ordinary t crossbars. In the first two coefficients of the bottom block, the tail of Q is very close to the following (1); the independent little stroke in degree 1 resembles the one in degree 2. The old signs in the first two answers and in the last answer remain visible under the new strokes, particularly the small closed oval in the second. The short struck word to the left of the μ calculation remains doubtful. No typed corrections or j indices.

**Formulas, including insertions and diagrams, in reading order**


Source line 2

~~~tex
\[
\begin{aligned}
H^0(\bar U,\mathrm{G}_m)&=\mathbb{Z}/2\mathbb{Z}+\mathbb{Z}^S\\
H^1(\bar U,\mathrm{G}_m)&=0\\
H^2(\bar U,\mathrm{G}_m)&=\mathrm{Ker}\left((\mathbb{Q}/\mathbb{Z})^S\longrightarrow\mathbb{Q}/\mathbb{Z}\right)\\
H^i(\bar U,\mathrm{G}_m)&=0\qquad\text{si }i\geq3
\end{aligned}
\]
~~~


Source line 10

~~~tex
\[
0\to\mu_{\ell^n}\to\mathrm{G}_m\xrightarrow{\ell^n}\mathrm{G}_m\to0
\]
~~~


Source line 14

~~~tex
\[
\begin{aligned}
H^1(\bar U,\mu_{\ell^n})&\simeq(\mathbb{Z}/\ell^n\mathbb{Z})^S\\
H^2(\bar U,\mu_{\ell^n})&\simeq\mathrm{Ker}\left((\mathbb{Z}/\ell^n\mathbb{Z})^S\longrightarrow(\mathbb{Z}/\ell^n\mathbb{Z})\right)\\
H^i(\bar U,\mu_{\ell^n})&=0\qquad\text{si }i\geq3
\end{aligned}
\]
~~~


Source line 21

~~~tex
\[
H^0(\bar U,\mathbb{Z}_\ell)\simeq\mathbb{Z}_\ell
\]
~~~


Source line 24

~~~tex
\[
\left\{\begin{aligned}
H^1(\bar U,\mathbb{Z}_\ell(1))&\simeq\mathbb{Z}_\ell^S\\
H^2(\bar U,\mathbb{Z}_\ell(1))&\simeq\mathrm{Ker}\left(\mathbb{Z}_\ell^S\longrightarrow\mathbb{Z}_\ell\right)
\end{aligned}\right.
\]
~~~

- Source line 30 `$\ell=2$`
- Source line 30 `$0$`

Source line 31

~~~tex
\[
\left\{\begin{aligned}
H^0(X,\mathbb{Q}(1))&=\deleted{\unsure{\mathbb{Q}}}0\\
H^1(X,\mathbb{Q}_{\unsure{\ell|\vphantom{\ell}}}(1))&=\deleted{\unsure{0}}0\\
H^2(X,\mathbb{Q}_{\unsure{\ell}}(1))&=0\\
H^3(X,\mathbb{Q}(1))&=\deleted{\unsure{0}}\mathbb{Q}
\end{aligned}\right.
\]
~~~


Indices/exponents containing literal i or j, in reading order: `^i`, `^i`. See also operator indices or pullbacks in the register.

**Changes**

- `H^1(X,\mathbb{Q}(1))&=0` -> `H^1(X,\mathbb{Q}_{\unsure{\ell|\vphantom{\ell}}}(1))&=\deleted{\unsure{0}}0`
- `H^3(X,\mathbb{Q}(1))&=\mathbb{Q}` -> `H^3(X,\mathbb{Q}(1))&=\deleted{\unsure{0}}\mathbb{Q}`

## Scan 179

2026-11-18T12:55:40Z to 2026-11-18T12:57:20Z UTC.

**Independent reading of accents, endings and unusual words**

On peut supposer X irréductible de pt générique y. L'inclusion … définit une suite spectrale (pour la cohomologie étale); Or … comme … les fibres … qui s'explicitent par de la cohomologie galoisienne, sont des groupes de torsion … on trouve qu'il …; où … est le faisceau (étale) des fonctions rationnelles non nulles sur X. D'autre part, on a la suite exacte; insertion si X est … sans idéaux premiers immergés, with the adjectival insertion noethérien. Prose below: où … est le faisceau (pour la top. étale) des diviseurs (de Cartier) sur X, ce qui implique compte tenu de ce que … est bijectif mod torsion si i ≥ 1. L'hypothèse de factorialité d'autre part implique … qu'on a un isomorphisme de faisceaux étales. Oblique pencil: donner le / corollaire / 5.4. Accents at irréductible, générique, définit, étale, où, idéaux, immergés, hypothèse, factorialité, étales. Check noethérien vs noethérien with plural strokes; les versus des before fibres.

**Comparison with the ink**

The first passage has a surrounding line and two diagonal cancellations. It ends before D'autre part; the new paragraph and its insertion are live. Nested strikes cover the repeated opening after Or, a short des, the abandoned phrase after que, the former definition after (*), a derived-image start after the second equals, and (Ceci étant. The upper spectral-sequence arrow has two shafts and points left. Its E has lower 2 and upper pq; the i in the image-direct symbol has a low star/x-shaped mark. The underlined letters in the sheaf name are distinct from its subscript X. Insertion points were followed for non nulles, si X est …, the modifier before the doubled quotation marks, the words before étale, and implique. The upward trace beneath top has the same sweeping return as the other leaders, so a second opening parenthesis before étale is doubtful. Beside the connecting map a thick earlier letter survives at the live G; the degree on the source is dotted. The two lower struck phrases beside the live factorialité conclusion remain in place. Rotated the lower left note: first line donner le, second corollaire, each independently underlined, then 5.4. No typed matter.

**Formulas, including insertions and diagrams, in reading order**

- Source line 3 `$X$`
- Source line 3 `$\unsure{y|\eta}$`
- Source line 3 `$y\unsure{-|\to}X$`

Source line 4

~~~tex
\[
H^*(y,\mathrm{G}_m)\Longleftarrow E_2^{pq}=H^p(X,\unsure{\mathbb{R}|\mathrm{R}}^qi_{\unsure{*|x}}(\mathrm{G}_m))
\]
~~~

- Source line 7 `$H^q(y,\mathrm{G}_m)$`
- Source line 7 `$\mathrm{R}^q i_*(\mathrm{G}_m)$`
- Source line 7 `$q>0$`

Source line 8

~~~tex
\[
H^p(X,\mathrm{R}_X^*)\tag*{$(*)$}
\]
~~~

- Source line 11 `$\mathrm{R}_X=\mathrm{R}i_*(\mathrm{G}_m)$`
- Source line 11 `$p>0$`
- Source line 11 `$\mathrm{R}_X^*=\deleted{\unsure{\mathrm{R}i_*}}i_*(\mathrm{G}_{m\,\unsure{x|y}})$`
- Source line 11 `$X$`
- Source line 13 `$X$`

Source line 14

~~~tex
\[
0\unsure{-|\to}\mathrm{G}_{m\,X}\longrightarrow\mathrm{R}_X^*\longrightarrow\underline{\mathrm{Div}}_X\longrightarrow0\tag*{(5.\unsure{1|2}.)}
\]
~~~

- Source line 17 `$\underline{\mathrm{Div}}_X$`
- Source line 17 `$X$`
- Source line 17 `$(*)$`

Source line 18

~~~tex
\[
H^{\unsure{i}}(X,\underline{\mathrm{Div}}_X)\xrightarrow{\partial}H^{i+1}(X,\deleted{\unsure{\mathrm{R}|\mathrm{D}}}\mathrm{G}_{m\,X}).
\]
~~~

- Source line 23 `$i\geq1$`

Indices/exponents containing literal i or j, in reading order: `^{\unsure{i}}`, `^{i+1}`. See also operator indices or pullbacks in the register.

**Changes**

- `(pour la \unsure{top}} (étale)` -> `(pour la \unsure{top|top.}} \unsure{(}étale)`
- `H^{i+1}(X,\mathrm{G}_{m\,X}).` -> `H^{i+1}(X,\deleted{\unsure{\mathrm{R}|\mathrm{D}}}\mathrm{G}_{m\,X}).`

## Scan 180

2026-11-18T12:57:21Z to 2026-11-18T12:57:55Z UTC.

**Independent reading of accents, endings and unusual words**

Calculs de cohomol. absolue / du motif de Tate / a tall Z or N and (n). Sloped hand, dot after shortened cohomol very pale, after (n) a fine speck. No apparent diacritics. Capital T has a long cross stroke; the following t also reaches the bar. Pencil 179.

**Comparison with the ink**

Read the formula on its own line. The large letter has two rising strokes with a long diagonal; both Z and N remain possible in this hand. A fine dot after the closing parenthesis is visible. The broad T-crossing in Tate belongs to the word. No other crossings, insertions, marginal notes, i/j indices or typed text. The hand differs from the adjacent notes; the title is unsigned.

**Formulas, including insertions and diagrams, in reading order**


Source line 3

~~~tex
\[
\unsure{\mathbb{Z}|N}(n).
\]
~~~


Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

No change.

## Scan 182

2026-11-18T12:57:56Z to 2026-11-18T12:58:26Z UTC.

**Independent reading of accents, endings and unusual words**

Four lines: Généralités fonctoriello-catégoriques / sur la distribution des / frobenius dans les gpes / de Galois motiviques. Three acute accents in Généralités and one in catégoriques, not an accent on the initial of frobenius. Lower-case f with a descender, doubled l before hyphen, gpes compact; G in Galois visibly different from the f. Final period. Pencil 181.

**Comparison with the ink**

The first component ends in two high loops, a small low oval and a hyphen. Capital G is a rounded letter. The initial of frobenius has a long descending stroke unlike the heavier capital F in the following prose page. No formulas, indices, marginal additions, cancellations, or typed matter. The rest is blank apart from the small pencilled archive number.

**Formulas, including insertions and diagrams, in reading order**


Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

No change.

## Scan 183

2026-11-18T12:58:26Z to 2026-11-18T13:00:13Z UTC.

**Independent reading of accents, endings and unusual words**

catégorie de motifs géométriques, de type [lié / …], préschéma, degrés, pairs, possible, certaines questions de distribution des Frobenius, pt fermé, permet donc, de définir des (une …tion de), Motivi­ques with capital M. Pour fixer les idées, choisissons un pt ℝ-motivique, d'où, gpe … ; démultiplier les point[s] fermés s, où, de type préférentiel, désigne, associé à. In the margin l'exposant 0 désigne des pts fermés; last word underlined. Soit S' l'ens de ces couples, A tout s' … associé … déterminé à isom près, d'où. De plus, si … est “le” gpe déduit … par torsion … on obtient un hom … compatible avec … déterminé en fait mod conjugaison par un élément de. The letters in the heavily covered words at the end may be longer than simple interior / automorphisme. Recheck the prime, i and possible subscript in the pair.

**Comparison with the ink**

Read the slanted note in its own direction: l'exposant / 0 désigne / des pts / fermés, the last word with an underline. The article is reduced. The first capital M has the long left foot of a script capital. R has two stems in the quoted name, the group indices and H¹; the first C is much plainer than the next. The superscript pair, the circle by S, and the or above G were separately checked. The second component of the pair has a compact dark foot; the i introducing the following map has a separate dark cancelled subscript. The low straight link before G(s) shows no distinct head. The torsor letter has an angular, descending trace. The faded text visible through the support is reversed; all the foreground text is handwriting. Struck la plupart des, a short phrase and old closing quotes after Motiviques, the verb below démultiplier, the word before préférentiel, Alors, d'où un, the old letter at G in H¹, the old index under G(s'), and the two last-line starts. The additions de type …, certaines, de M, fermés s and conjugaison have individual leaders or positions above the affected words. The last two G groups in the display have different arguments: s′ and s.

**Formulas, including insertions and diagrams, in reading order**

- Source line 2 `$\mathcal M$`
- Source line 2 `$S$`
- Source line 2 `$\mathbb Z$`
- Source line 2 `$\mathcal M$`
- Source line 2 `$\mathcal M$`
- Source line 2 `$\mathcal M^{\mathrm{pair}}$`
- Source line 2 `$s\in S$`
- Source line 2 `$\mathbb R$`
- Source line 2 `$\mathcal M$`
- Source line 4 `$\mathbb R$`
- Source line 4 `$\mathcal M$`
- Source line 4 `$\Lambda$`
- Source line 4 `$G_{\mathbb R}$`
- Source line 4 `$\mathbb R$`
- Source line 6 `$s$`
- Source line 6 `$S$`
- Source line 6 `$s'=(s,\unsure{i'|i|i_s})$`
- Source line 6 `$s\in S^0$`
- Source line 8 `$0$`
- Source line 9 `$i_{\deleted{\unsure{s|x}}}\colon G_{m\,\unsure{\mathbb C|C}}\unsure{-|\to}G(s)_{\mathbb C}$`
- Source line 9 `$G(s)$`
- Source line 9 `$\mathcal M_s$`
- Source line 11 `$S'$`
- Source line 11 `$s'\in S'$`
- Source line 11 `$\mathbb R$`
- Source line 11 `$\mathcal M$`
- Source line 11 `$\unsure{\zeta|\xi}(s')\in H^1(\mathbb R,\deleted{\unsure{F|G}}G_{\mathbb R}^{\mathrm{or}})$`
- Source line 11 `$G^{\mathrm{or}}$`
- Source line 11 `$G_{\mathbb R}^0\xrightarrow{\varepsilon}G_m$`
- Source line 11 `$G_{\mathbb R}^{\zeta(s')}$`
- Source line 11 `$G_{\mathbb R}$`
- Source line 11 `$\zeta(s')$`

Source line 12

~~~tex
\[
u(s')\colon G(s')_{\deleted{\unsure{R|k}}\mathbb R}=G(s)_{\mathbb R}\longrightarrow G_{\mathbb R}^{\zeta(s')}
\]
~~~

- Source line 15 `$\varepsilon_{\mathbb R},J_{\mathbb R}$`
- Source line 15 `$G_{\mathbb R}^{\mathrm{or}}(\mathbb R)$`

Indices/exponents containing literal i or j, in reading order: none. See also operator indices or pullbacks in the register.

**Changes**

- `\unsure{lié|lisse}` -> `\unsure{lié|lisse|fini}`
- `\deleted{\unsure{point de vue}}` -> `\deleted{\unsure{point de vue}''}`
- `\unsure{i'|i}` -> `\unsure{i'|i|i_s}`
- `$0$ désigne des pts` -> `$0$ désigne \unsure{des|les} pts`
- `$i\colon G_{m\,\mathbb C}` -> `$i_{\deleted{\unsure{s|x}}}\colon G_{m\,\unsure{\mathbb C|C}}`
- `d'où un $\zeta(s')\in` -> `d'où un $\unsure{\zeta|\xi}(s')\in`

## Cross-page notation and attachment of callouts

The above and below-line annotations already located in the formula registers were compared across scans 173, 175 and 177. The insertion markup was applied at the indicated points. Each literal replacement follows; repeated callouts were checked at both ends of the formulas.

- Scan 173, 1 occurrence(s): `\ n\not\equiv0\ (\omega_\ell(q))` -> `\ \inserted{n\not\equiv0\ (\omega_\ell(q))}`
- Scan 173, 1 occurrence(s): `_{\text{i.e. }n\equiv0\ (\omega_\ell(q))}` -> `_{\inserted{\text{i.e. }n\equiv0\ (\omega_\ell(q))}}`
- Scan 173, 2 occurrence(s): `{\substack{\vert\\n\ne0}}{n}` -> `{\substack{\vert\\\inserted{n\ne0}}}{n}`
- Scan 175, 2 occurrence(s): `{\substack{\shortparallel\\M}}{M^U}` -> `{\substack{\shortparallel\\\inserted{M}}}{M^U}`
- Scan 175, 1 occurrence(s): `\shortparallel\\\mathrm{Hom}(U,M^\pi)` -> `\shortparallel\\\inserted{\mathrm{Hom}(U,M^\pi)}`
- Scan 177, 1 occurrence(s): `\shortparallel\\\mathbb{Z}^*=\{+1,-1\}` -> `\shortparallel\\\inserted{\mathbb{Z}^*=\{+1,-1\}}`
- Scan 177, 4 occurrence(s): `\shortparallel\\0}}` -> `\shortparallel\\\inserted{0}}}`
- Scan 177, 1 occurrence(s): `\shortparallel\\(\mathbb{Q}/\mathbb{Z})^S` -> `\shortparallel\\\inserted{(\mathbb{Q}/\mathbb{Z})^S}`
- Scan 177, 1 occurrence(s): `[\substack{\text{\uline{somme}}\\\text{\uline{des inv.}}}]` -> `[\inserted{\substack{\text{\uline{somme}}\\\text{\uline{des inv.}}}}]`
- Scan 177, 1 occurrence(s): `\shortparallel\\\mathbb{Q}/\mathbb{Z}` -> `\shortparallel\\\inserted{\mathbb{Q}/\mathbb{Z}}`
- Scan 177, 1 occurrence(s): `\shortparallel\\0\,?` -> `\shortparallel\\\inserted{0\,?}`

The angular Z and double-stem F recur on scans 172–179. The open, sloping cover letter on 180 remains distinct. Underlined Div on 176 and 179 and the wavy under-letter strokes on 173 and 174 were compared separately. The H with two stems in the lower part of 173 is distinct from the local underlined H of 177. The y/eta of 176 and 179, and the class letter on 176 and 183, remain open where indicated. Lower-case frobenius on 182 and capital Frobenius on 183 reproduce their respective initials.

**Support of scan 183.** A magnified, horizontally reversed sample of the faint lettering reads in normal orientation and shows regularly aligned mechanical type. The inventory classifies the support as a reused typed sheet. All foreground additions on this side are handwritten.
