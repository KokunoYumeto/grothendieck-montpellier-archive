# Second reading of cote 84

Locations follow the physical page. Formulae and corrections are in transcription order. Where a mark has several readings they remain together. The readings below precede the witness check.

Fifteen independent second-reading intervals were shorter than two minutes. The longer interval belongs to scan 10. The times below give the duration of that pass only. Later comparisons of marked passages with the crops are recorded in the witness table.

## Scan 002

2026-11-18T03:13:34Z to 2026-11-18T03:14:44Z (UTC).

**Reading from the three crops before reopening the page file**

Top: the diaeresis in « monoïdes » is visible twice, with « hom de monoïdes » below. Read « applications ensembl. » with caution, « pour commencer par mettre », « comm., ass., unitaire », « loi de composition », « par vér. égal à », and « i.e. ». In the case list the small clarifications read « ass. dans », « mult. de α », « comm. » and « OK ». Across the middle I see « Donc il faut vérifier », abbreviations near the first box, « cela donne », « Et (2) devient alors », and « Vér. … d’espèces ». In the lower right read « On définit », « On trouve ainsi un », « de tte façon », « est pair », « si … est impair », « si 2 inv. … alors », and « un isom. plus fin que ». The left foot has « où », « Mais ». Several terminal strokes are insulated from their word by the paper fold.

**Comparison against the transcription**

The two short horizontal arrows have opposite heads. The third law has an obliterated term immediately before xα(y). The bracket beneath yz on the right spans the pair. In the first starred test y,z are in R₁; in the last, all three are in R₁. Questioned equals signs remain. Traced the arrows leaving the large A/B box and collated the independent computations to its right. The lower sum, exterior product and tensor quantities have index i (short, dotted, no descending stem), repeated in Lᵢ and δᵢ. There is no index j. Numerals 1 and 0 on R have distinct strokes. Blackboard Z has a second diagonal; handwritten R, L and E and the looped O do not have that diagonal. The side calculations below the torn edge and the three lines beside NB are separate from the Arf calculation. Underlined « non inv. » is live; the strokes above NB and across the two abandoned formulae below it are cancellations. In the sign chains under A/B, the tiny crossed letters and the entries under the braces remain less secure than the outer equalities.

**Formulae in reading order**

- top left, paired arrows — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;] R_1 \arrow[r,shift left,"\deleted{\unsure{\alpha}}\beta"] \&amp; R_0 \arrow[l,shift left,"\deleted{\unsure{\beta}}\alpha"] \end{tikzcd}}</code>.
- top, alongside paired arrows — <code>$R_0,R_1$</code>.
- top, two maps — <code>\[ \begin{aligned} \alpha:R_0\longrightarrow R_1&amp;\quad\text{hom. de monoïde}\quad (L,\delta\in\Gamma(L^{\otimes2}),T_0\in\Gamma L_0)\longmapsto (L,\unsure{\Gamma|\delta})\\ \beta:R_1\longrightarrow R_0&amp;\quad\text{\unsure{applicat. ensembl.|application ensem.} (pas comp. avec produits)}\quad (L,\delta)\longmapsto(L,4\delta,0) \end{aligned} \]</code>.
- upper left, grading — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;] R_\ast\arrow[d] \&amp; {}=R_0\amalg R_1\\ \mathbb Z/2\mathbb Z \&amp; \end{tikzcd}}</code>.
- upper centre, beside grading — <code>$(x,y)\mapsto x\wedge y$</code>, <code>$R_\ast\longrightarrow\mathbb Z/2\mathbb Z$</code>.
- upper centre, products of components — <code>\[ \text{i.e.}\quad \begin{aligned} R_0\cdot R_0&amp;\subset R_0\\ R_1 R_1&amp;\subset R_0\\ R_1\cdot R_0=R_0\cdot R_1&amp;\subset R_1 \end{aligned} \]</code>.
- upper third, definition of wedge — <code>\[ \begin{aligned} x,y\in R_0&amp;\Longrightarrow x\wedge y=x\cdot y\\ x,y\in R_1&amp;\Longrightarrow x\wedge y=\beta(x\cdot y)\qquad\text{(pas néc. égal à $\beta(x)\,\beta(y)$)}\\ x\in R_1,\ y\in R_0&amp;\qquad x\wedge y=y\wedge x=\deleted{\unsure{\alpha(x)y}}\,x\alpha(y) \end{aligned} \]</code>.
- upper third, associativity — <code>\[(x\wedge y)\wedge z=x\wedge(y\wedge z)\]</code>.
- upper third, cases a to d — <code>\[ \begin{aligned} \text{a)}\quad x,y,z\in R_0&amp;\quad\text{OK}\quad\deleted{\text{(ass. dans $R_0$)}}\qquad\text{ass. dans $R_0$}\\ \text{b)}\quad x\in R_1,\ y,z\in R_0&amp;\quad (x.\alpha(y)).\alpha(z)=x.\underbrace{\alpha(y.z)}_{(\alpha(y)\alpha(z))}\quad\text{mult. de $\alpha$ + ass. dans $R_1$}\\ \text{c)}\quad y\in R_1,\ x,z\in R_0&amp;\quad (\alpha(x)y)\alpha(z)=\alpha(x)(y\alpha(z))\quad\text{ass. dans $R_1$}\\ \text{d)}\quad z\in R_1,\ x,y\in R_0&amp;\quad \alpha(x.y).z=\alpha(x)(\alpha(y).z)\quad\text{mult. de $\alpha$ + ass. de $R_1$} \end{aligned} \]</code>.
- upper middle, primed cases — <code>\[ \begin{aligned} \text{b$'$)}\quad x\in R_0,\ y,z\in R_1&amp;\quad\beta((\alpha(x).y).z)\overset?=x.\beta(y.z)\quad (\ast)\\ \text{c$'$)}\quad y\in R_0,\ x,z\in R_1&amp;\quad\beta((x\alpha(y)).z)=\beta(x.(\alpha(y).z))\quad\text{ass. dans $R_1$}\\ \text{d$'$)}\quad z\in R_0,\ x,y\in R_1&amp;\quad\underset{\Vert}{\beta(x.y)z}\overset?=\underset{\Vert}{\beta(x(y\alpha(z)))}\quad\text{comme $(\ast)$ + comm. et ass. dans $R_1$}\\ &amp;\quad z\,\beta(y.x)\qquad\beta((\alpha(z)y)x)\\ \text{a$'$)}\quad x,y,z\in R_1&amp;\quad\alpha(\beta(x.y)).z\overset?=x\,\alpha(\beta(y.z)) \end{aligned} \]</code>.
- middle, circled 1 — <code>\[ \beta(\alpha(x).\underbrace{yz})=x\,\beta(\underbrace{yz}_{u})\qquad\text{i.e.}\tag*{\textcircled{1}} \]</code>.
- middle right, opposite circled 1 — <code>$y$</code>, <code>$z=1$</code>, <code>$\boxed{\beta(\alpha(x)u)=x\beta(u)}$</code>, <code>$\swarrow$</code>, <code>$\boxed{\beta(\alpha(x))=x.\beta(1)}$</code>.
- middle, circled 2 and specialization — <code>\[ \begin{aligned} (\alpha.\beta(xy))z&amp;=x\,\alpha\beta(yz)\\ (\alpha\beta(x))z&amp;=x\,(\alpha\beta(z)) \end{aligned}\tag*{\textcircled{2}} \]</code>.
- middle right, opposite circled 2 — <code>$y=1$</code>, <code>$z=1$</code>, <code>$\boxed{\alpha\beta(x)=x.\underbrace{\alpha\beta(1)}_{\unsure{\xi|\eta}}}$</code>.
- middle, following circled 2 — <code>$(xy\zeta)z=x(yz\zeta)$</code>, <code>$R_1$</code>.
- middle left, boxed A and B with two arrows — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;,column sep=small] \boxed{\begin{aligned}\text{\textcircled{A}}&amp;\quad\beta(\alpha(x)u)=x\beta(u)\\ \text{\textcircled{B}}&amp;\quad\alpha\beta(x)=x.\underbrace{\eta}_{(\underline{\mathcal O}_X,4.\underline{1}_{\mathcal O_X})}\ \text{où }\eta=\alpha\beta(1)=\alpha(\zeta)\quad\zeta=\underbrace{\beta(1)}_{(\underline{\mathcal O}_X,4\underline1_{\mathcal O_X},0_{X_0})}\end{aligned}}\arrow[d,Rightarrow]\arrow[dr,Rightarrow] \&amp;\\ \boxed{\beta\alpha(x)=x\zeta} \&amp; \boxed{(\beta x)(\beta y)=\zeta\,\beta(x.y)} \end{tikzcd}}</code>.
- middle left, cancelled formula and comparison below — <code>\[ \begin{aligned} &amp;\deleted{\beta(1)\beta(x.y)1=\beta}\\[-2pt] &amp;\boxed{\underbrace{\beta(x)\beta(y)}_{\Vert\,\text{\textcircled{A}}}\overset?=\deleted{\unsure{\beta(xy)}}\underbrace{\zeta}_{\beta(1)}\cdot\beta(\overbrace{x.y}^{u})}\\ &amp;\beta(\underbrace{\alpha\beta(x)}_{x\eta\ \text{\textcircled{B}}}y)\qquad\quad\Vert\,\text{\textcircled{A}}\\ &amp;\beta(xy\eta)\qquad \beta(\underbrace{\underbrace{\alpha(\zeta)}_{\eta}xy}_{\alpha\beta(xy)\ \text{\textcircled{B}}})=\beta\underbrace{\alpha\beta(xy)}_{\beta\unsure{(\beta|1\,\beta)}(xy)\eta)} \end{aligned} \]</code>.
- middle right, verification in coordinates — <code>\[ \begin{aligned} \underline{x=(L,\delta)}&amp;\qquad\beta(x)=(L,4\delta,0)\qquad\alpha\beta(x)=(L,4\delta)\\ x=(L,\delta,T_0),\ u&amp;=(L',\delta')\qquad\qquad\quad=(L,\delta)(\underline{\mathcal O},4\underline1_X)\\ \alpha(x)&amp;=(L,\delta)\\ \alpha(x).u&amp;=(LL',\delta\delta')\\ \beta(\alpha(x).u)&amp;=(LL',4\delta\delta',0)\\ \beta(u)&amp;=(L',4\delta',0)\qquad x\beta(u)=(LL',4\delta\delta',0) \end{aligned} \]</code>.
- right, outlined block extending to lower third — <code>$R_\ast=R\times_{\mathbb Z}\mathbb Z/2\mathbb Z$</code>.
- right, definition of w, even and odd — <code>\[ \begin{aligned} &amp;R_\ast\xrightarrow{\deleted{\unsure{w_n}}} R_0\quad\text{par}\\ &amp;\text{a) si }n=2\nu\qquad R_{2\nu}\xrightarrow{w_n} R_0\qquad w_n(x)=x\zeta^\nu\\ &amp;\hspace{45pt}\deleted{\unsure{R_1}}\quad R_0\\ &amp;\text{b) si }n=2\nu+1\qquad\deleted{n+1=2\nu+2}\qquad w_n(\unsure{x})=\beta(x)\zeta^\nu\\ &amp;\hspace{48pt}\underset{R_1}{\underset{\Vert}{R_n}} \end{aligned} \]</code>.
- right, end of outlined block — <code>$w:R_\ast\longrightarrow R_0$</code>, <code>\[w'_1:R_\ast\longrightarrow\mathbb Z\times R_0\]</code>.
- lower left and centre, E and w1 — <code>\[ \begin{aligned} E&amp;=\bigoplus_{1\leq i\leq n}(L_i,\delta_i)\\ w_1(E)&amp;=\bigwedge_{1\leq i\leq n}(L_i,4\delta_i,0) =\left(\bigotimes\unsure{\vphantom{L}\zeta} L_i,\underbrace{4^n}_{=(2^n)^2}\underbrace{\textstyle\prod\delta_i}_{\delta},0\right) \end{aligned} \]</code>.
- lower left, Arf, adjoining parity notes — <code>\[ \begin{aligned} \operatorname{Arf}(E)&amp;=\left(\bigotimes L_i,\underbrace{2^\nu}_{4^{\nu'}=(2^{\nu'})^2}\underbrace{\textstyle\prod\delta_i}_{\delta},0\right) \quad\begin{aligned}\nu&amp;=n\ \text{si $n$ pair}\\\nu&amp;=n+1\ \text{si $n$ impair}\end{aligned}\\ \operatorname{Arf}(E)&amp;=w_1(E).\zeta_n\qquad \zeta_n=(\underline{\mathcal O}_X,2^n\mathbin{\unsure{:|.}}1,1 \end{aligned} \]</code>.
- lower right, directly below w prime — <code>$\nu$</code>, <code>$\nu=2\nu'$</code>, <code>$\nu'=\left[\dfrac{n+1}{2}\right]$</code>.
- lower left, two lines for L — <code>\[ \begin{aligned} w_1(\unsure{L})&amp;=(L,4\delta,0)\\ \operatorname{Arf}(\unsure{L})&amp;=(L,4\unsure{\delta},0) \end{aligned} \]</code>.
- lower centre right, NB and cancellations — <code>$\unsure{n}$</code>, <code>$2$</code>, <code>$X$</code>, <code>$\unsure{d}\sim\quad\otimes$</code>, <code>$\operatorname{Arf}(E)\sim$</code>.
- bottom centre, exponent computation — <code>\[ n-\frac{n+1}{2}=\frac{\unsure{n-1}}2\qquad \nu''=\begin{cases}\frac n2&amp;\text{si $n$ pair}\\ \frac{n-1}2&amp;\text{si $n$ impair}\end{cases} \]</code>.
- bottom left, boxed c1 and xi — <code>\[ \boxed{c_1(E)=\operatorname{Arf}(E).\zeta^{(n-\nu')=\nu''}} \qquad \begin{aligned} \text{où}\quad\zeta&amp;=(\underline{\mathcal O}_X,4,0)\\ &amp;=\operatorname{Arf}(\mu_{2X}/X) \end{aligned} \]</code>.
- bottom centre, beside exponent — <code>$\operatorname{Arf}(E)$</code>, <code>$c_1(E)$</code>, <code>$2$</code>, <code>$X$</code>.
- bottom right, comparison if 2 invertible — <code>\[ \begin{aligned} c_1(E)&amp;\simeq\left(\bigotimes L_i,\unsure{\delta},0\right)\\ \operatorname{Arf}(E)&amp;\simeq\left(\bigotimes L_i,\delta,0\right) \end{aligned} \]</code>.
- bottom left, last line — <code>$c_1(E)$</code>.

**Alterations, additions, marginal writing and underlining**

- top left, paired arrows — <code>\deleted{\unsure{\alpha}}</code>.
- top left, paired arrows — <code>\deleted{\unsure{\beta}}</code>.
- top, alongside paired arrows — <code>\deleted{\unsure{hom. de monoïde}}</code>.
- upper centre, beside grading — <code>\inserted{$(x,y)\mapsto x\wedge y$ comm., ass., unitaire,}</code>.
- upper third, definition of wedge — <code>\deleted{\unsure{\alpha(x)y}}</code>.
- upper third, cases a to d — <code>\deleted{\text{(ass. dans $R_0$)}}</code>.
- middle right, opposite circled 1 — <code>\margin{(faisant $y$ ou $z=1$)\quad $\boxed{\beta(\alpha(x)u)=x\beta(u)}$\quad $\swarrow$ $\boxed{\beta(\alpha(x))=x.\beta(1)}$}</code>.
- middle right, opposite circled 2 — <code>\margin{si $y=1$ cela donne et si $z=1$\quad $\boxed{\alpha\beta(x)=x.\underbrace{\alpha\beta(1)}_{\unsure{\xi|\eta}}}$}</code>.
- middle left, boxed A and B with two arrows — <code>\underline{\mathcal O}</code>.
- middle left, boxed A and B with two arrows — <code>\underline{1}</code>.
- middle left, boxed A and B with two arrows — <code>\underline{\mathcal O}</code>.
- middle left, cancelled formula and comparison below — <code>\deleted{\beta(1)\beta(x.y)1=\beta}</code>.
- middle left, cancelled formula and comparison below — <code>\deleted{\unsure{\beta(xy)}}</code>.
- middle right, verification in coordinates — <code>\underline{x=(L,\delta)}</code>.
- middle right, verification in coordinates — <code>\underline{\mathcal O}</code>.
- right, definition of w, even and odd — <code>\deleted{\unsure{w_n}}</code>.
- right, definition of w, even and odd — <code>\deleted{\unsure{R_1}}</code>.
- right, definition of w, even and odd — <code>\deleted{n+1=2\nu+2}</code>.
- right, end of outlined block — <code>\uline{hom}</code>.
- lower left, Arf, adjoining parity notes — <code>\underline{\mathcal O}</code>.
- lower right, directly below w prime — <code>\margin{de ttes façons $\nu$ est pair\quad $\nu=2\nu'$\quad $\nu'=\left[\dfrac{n+1}{2}\right]$}</code>.
- lower centre right, NB and cancellations — <code>\margin{\deleted{On peut prendre} \inserted{$\unsure{n}$} NB si $2$ inv. \inserted{sur $X$} alors \deleted{$\unsure{d}\sim\quad\otimes$} \deleted{$\operatorname{Arf}(E)\sim$}}</code>.
- lower centre right, NB and cancellations — <code>\deleted{On peut prendre}</code>.
- lower centre right, NB and cancellations — <code>\inserted{$\unsure{n}$}</code>.
- lower centre right, NB and cancellations — <code>\inserted{sur $X$}</code>.
- lower centre right, NB and cancellations — <code>\deleted{$\unsure{d}\sim\quad\otimes$}</code>.
- lower centre right, NB and cancellations — <code>\deleted{$\operatorname{Arf}(E)\sim$}</code>.
- bottom left, boxed c1 and xi — <code>\underline{\mathcal O}</code>.
- bottom centre, beside exponent — <code>\uline{non}</code>.
- bottom centre, beside exponent — <code>\uline{inv.}</code>.

**Changes**

- <code>\unsure{comm.}, ass.</code> -> <code>comm., ass.</code>
- <code>Vér. sur les d'espèces</code> -> <code>Vér. \unsure{les cas|sur cas} d'espèces</code>
- <code>\beta(\alpha(x).\underbrace{yz})=x\,\beta(y\underbrace{z}_{u})</code> -> <code>\beta(\alpha(x).\underbrace{yz})=x\,\beta(\underbrace{yz}_{u})</code>
- <code>\text{applicat. d'ens. (pas comp. avec produits)}</code> -> <code>\text{\unsure{applicat. ensembl.|application ensem.} (pas comp. avec produits)}</code>

## Scan 003

2026-11-18T03:14:45Z to 2026-11-18T03:15:34Z (UTC).

**Reading from the three crops before reopening the page file**

Upper face: « Je vais ouvrir » (the last word is very pale), an underlined first word and « Mr. Pascal ». In the pencil working I see « monoïde unitaire », « est un hom de Monoïdes », « Impair », « Pair », « partie étale », « ce n'est pas un hom de monoïdes ! », « d'où » or « discr. », « deux ou trois parités impaires ». The wrapper bears « Offsetpapier (hochweiß, holzfrei) », « super white, woodfree », « extra blanc, sans bois », « wit, houtvrij », and « Made in W.-Germany ». At the foot « Merci pour bonnes choses », the plural-looking word « Conversations », « hier et aujourd hui », « aide et assistance ! », « Avant-hier », « Comment on compte pour figues », « 13 kg », « tu me rembourses », « Comme ça je n'ai pas besoin de peser », « apportes-moi stp mon ail », « gâter », « Demain ? », « Plant », « beaucoup de manquants un peu partout », « radis ?? », « semer ». The hyphen and word endings by the edge are light.

**Comparison against the transcription**

The printed rectangle is sideways; on rotation its grade reads VII and the column of units reads g/m², gsm, grs/m², grs/m². A torn flap covers part of the printed dimensions but the 7 is visible on its right. In the pencil work, both H exponents read 1 with an upright stroke. No i or j index. Blackboard Z has two diagonals; R and Θ have open and closed bowls respectively. Read the last map of the four products as a plain shaft first. The heavy marks below the δ arrow and two products remain doubtful. The underlining beneath Impair/Pair, the names, « ail », « Demain », « Plant » and « radis » is distinct from the pencil cancellations across the calculations. The arrow beside « choses » points upward to the interlinear parenthesis. Zoom reveals an extended terminal stroke in « conversations ».

**Formulae in reading order**

- middle left, four products — <code>\[ \begin{aligned} &amp;R_1\qquad R_0\\ R_1\times R_1&amp;\longrightarrow R_0\\ R_0\times R_0&amp;\longrightarrow R_0\\ R_0\times R_1&amp;\longrightarrow R_1\\ R_1\times R_0&amp;\mathrel{\unsure{-|\to}} R_1 \end{aligned} \]</code>.
- middle right, parity map — <code>$R=R_1\amalg R_0$</code>.
- middle right, following line — <code>$R\xrightarrow{\varepsilon}\mathbb Z/2\mathbb Z$</code>.
- middle right, fibres and étale part — <code>\[ \begin{aligned} R_1&amp;=\varepsilon^{-1}(1)\\ R_0&amp;=\varepsilon^{-1}(0)\\ R_{00}&amp;\subset R_0\quad\longrightarrow\text{partie étale}=H^1(X,\mathbb Z/2\mathbb Z) \end{aligned} \]</code>.
- middle left, parity and coordinate diagram — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;,column sep=small] \&amp;\text{\uline{Impair}}\&amp;(L,\delta,T_0)\\ (L,\delta)\arrow[r,mapsto]\&amp;( \pi\ \unsure{w})\arrow[u]\arrow[d]\&amp;(L,\delta,T_0)\arrow[r,mapsto]\&amp;(L,\delta)\\ (L,4\delta,0)\&amp;\text{\uline{Pair}}\&amp;(L,\delta) \end{tikzcd}}</code>.
- centre, loose pairs — <code>\[\deleted{\unsure{\delta}}\qquad(\underline L,\delta)\qquad\underline L,\]</code>.
- centre right, arrow and question — <code>$R_1\longrightarrow R_0$</code>.
- centre right, map and annotation — <code>\[ (L,\underset{\substack{\downarrow\\\text{\unsure{discr.}}\\\text{\unsure{divisé}}}}{\delta})\longrightarrow (L,4\delta,0) \]</code>.
- centre left, H and computations — <code>\[ \begin{aligned} &amp;R_1\longrightarrow H^1(\underline L)\qquad \deleted{R_1\times R_0}\\ &amp;\Theta=2\delta\qquad\deleted{2\delta}\qquad\deleted{2\delta,\ 2\delta\quad 2\delta}\\ &amp;\Theta'=2\delta'\qquad\Theta\Theta'=4\delta\delta',\ \deleted{2\delta\delta'}\,0\\ &amp;\Theta\delta'=2\qquad\Theta=\underline{2\delta}. \end{aligned} \]</code>.
- lower middle right, four products in frame — <code>\[ \boxed{\begin{aligned} (L,\delta)(L',\delta')&amp;=(LL',4\delta\delta',0)\\ (L,\delta)(L',\delta',T'_0)&amp;=(LL',\deleted{\unsure{2}}\delta\delta')\\ (L,\delta,T_0)(L',\delta')&amp;=(LL',\delta\delta')\\ (L,\delta,T_0)(L',\delta',T'_0)&amp;=(LL',\delta\delta',T_0T'_0) \end{aligned}} \]</code>.
- lower middle, triple product beneath box — <code>\[ \begin{aligned} &amp;(LL'L'',4\delta\delta'\delta'',0\ \text{ou }\unsure{T_0T'_0T''_0})\quad \text{si deux ou trois parités impaires}\\ &amp;\text{sinon}\quad LL'L'',\delta\delta'\delta'',\ T_0T'_0T''_0 \end{aligned} \]</code>.
- lower third, figs and weight — <code>\[13\,\mathrm{kg}=\text{----}\]</code>.

**Alterations, additions, marginal writing and underlining**

- top right, address — <code>\uline{\unsure{Pourny|Pourry}}</code>.
- top right, address — <code>\uline{Mr. Pascal}</code>.
- middle left edge, rotated paper label — <code>\uline{21}</code>.
- middle right, following line — <code>\deleted{\unsure{et}}</code>.
- middle left, parity and coordinate diagram — <code>\uline{Impair}</code>.
- middle left, parity and coordinate diagram — <code>\uline{Pair}</code>.
- centre, loose pairs — <code>\deleted{\unsure{\delta}}</code>.
- centre right, arrow and question — <code>\uline{pas}</code>.
- centre left, H and computations — <code>\deleted{R_1\times R_0}</code>.
- centre left, H and computations — <code>\deleted{2\delta}</code>.
- centre left, H and computations — <code>\deleted{2\delta,\ 2\delta\quad 2\delta}</code>.
- centre left, H and computations — <code>\deleted{2\delta\delta'}</code>.
- centre left, H and computations — <code>\underline{2\delta}</code>.
- lower middle right, four products in frame — <code>\deleted{\unsure{2}}</code>.
- lower third, thanks — <code>\inserted{(\uline{\unsure{conversations|conversation}})}</code>.
- lower third, thanks — <code>\uline{\unsure{conversations|conversation}}</code>.
- lower third, thanks — <code>\uline{Avant}</code>.
- lower third, thanks — <code>\uline{hier}</code>.
- lower third, figs and weight — <code>\uline{figues}</code>.
- foot, garlic and garden — <code>\uuline{ail}</code>.
- foot, garlic and garden — <code>\uuline{Demain\,?}</code>.
- foot, garlic and garden — <code>\uline{\unsure{Plant}}</code>.
- foot, garlic and garden — <code>\inserted{beaucoup de}</code>.
- foot, garlic and garden — <code>\uline{radis}</code>.
- foot, garlic and garden — <code>\uline{semer}</code>.

**Changes**

- <code>\unsure{conversation}</code> -> <code>\unsure{conversations|conversation}</code>
- <code>Et apporte-moi</code> -> <code>Et \unsure{apportes-moi|apporte-moi}</code>
- <code>(\uline{Avant}-hier)</code> -> <code>(\uline{Avant}-\uline{hier})</code>

## Scan 004

2026-11-18T03:15:34Z to 2026-11-18T03:16:19Z (UTC).

**Reading from the three crops before reopening the page file**

Top right « extensions quadratiques, involutions canoniques », « se prolongent à A de façon canonique par … etc. ». Above equals « déf ». In the side column I read « correspondent aux sept droites vect. de », then « i.e. aux » and « sept éléments non nuls » with a word crossed out. At the bottom « si les cᵢ inv i.e. les Aᵢ étales », « il y a 7 + 7 = 14 situations “quadratiques” typiques (quand les Aᵢ sont étales…) ». The sideways note has « correspondant », « plans de », « algèbres », « engendrés », and « même » with a doubtful ending.

**Comparison against the transcription**

Reading the left margin rotated brings « hyper-plans de F₂³ », « i.e. par pol. orth. » and a cancelled final phrase into one orientation. On the right the crossing between the parenthesis and the exponent does not cancel the field. The two arrays were compared line by line: in the lower incidence list both short indices beside B₂ look more like 1 than 2. The i in uᵢ², cᵢ, σᵢ(uᵢ), Aᵢ, A′ᵢ, Bᵢ and B′ᵢ has a short stem; none of them descends as j. Distinguish the simple capital A, the heavier overwritten A and B in the tables, the double-stroked F, and σ with an open lower return. The marks on the last line before « quadratiques » overlap. No pen stroke crosses the numerical count.

**Formulae in reading order**

- top left, three extensions and bases — <code>\[ \begin{array}{ccc} A_1&amp;A_2&amp;A_3\\ 1\ u_1&amp;1\ u_2&amp;1\ u_3 \end{array} \qquad u_i^2+c_i=0 \]</code>.
- top right, four lines — <code>$\sigma_1,\sigma_2,\sigma_3$</code>, <code>$\sigma_i(u_i)=-u_i$</code>, <code>$A$</code>, <code>$\sigma_1\otimes\mathrm{id}\otimes\mathrm{id}$</code>.
- upper left, tensor product and monomials — <code>\[ \begin{aligned} &amp;A_1\otimes A_2\otimes A_3\overset{\unsure{\mathrm{déf}|\mathrm{dfn}}}=A\\ &amp;1\quad u_1\quad u_2\quad u_3\quad u_2u_3\quad u_3u_1\quad u_1u_2\quad u_1u_2u_3 \end{aligned} \]</code>.
- left edge, beside first table — <code>$\mathbb F_2^3$</code>, <code>$\mathbb F_2^3$</code>.
- upper half, table from k to B0 — <code>\diagram{$\begin{array}{llll} k&amp;1&amp;\sigma_1,\sigma_2,\sigma_3,\sigma_2\sigma_3,\sigma_3\sigma_1,\sigma_1\sigma_2,\sigma_1\sigma_2\sigma_3=\tau&amp;\\ A_1&amp;1,u_1&amp;\sigma_2,\sigma_3,\sigma_2\sigma_3&amp;\\ A_2&amp;1,u_2&amp;\sigma_3,\sigma_1,\sigma_3\sigma_1&amp;\\ A_3&amp;1,u_3&amp;\sigma_1,\sigma_2,\sigma_1\sigma_2&amp;\\ B_1&amp;1,u_2u_3&amp;\sigma_1,\sigma_2\sigma_3,\sigma_1\sigma_2\sigma_3=\tau&amp;B_1\simeq A_2\wedge A_3\\ B_2&amp;1,u_3u_1&amp;\sigma_2,\sigma_3\sigma_1,\sigma_2\sigma_3\sigma_{\unsure{1|3}}=\tau&amp;B_2\simeq A_3\wedge A_1\\ B_3&amp;1,u_1u_2&amp;\sigma_3,\sigma_1\sigma_2,\sigma_3\sigma_1\sigma_2=\tau&amp;B_3\simeq A_1\wedge A_2\\ B_0&amp;1,u_1u_2u_3&amp;\sigma_2\sigma_3,\sigma_3\sigma_1,\sigma_1\sigma_2&amp;B_0\simeq A_1\wedge A_2\wedge A_3 \end{array}$}</code>.
- middle, table of primed letters — <code>\diagram{$\left.\begin{array}{lll} A'_1=(A_{\unsure{2|3}},A_3,B_1)&amp;1,u_2,u_3,u_2u_3&amp;\sigma_1\\ A'_2=(A_3,A_1,B_2)&amp;1,u_3,u_1,u_3u_1&amp;\sigma_2\\ A'_3=(A_1,A_2,B_3)&amp;1,u_1,u_2,u_1u_2&amp;\sigma_3\\ B'_1=(A_1,B_1,B_0)&amp;1,u_1,u_2u_3,u_1u_2u_3=u&amp;\sigma_2\sigma_3\\ B'_2=(A_2,B_2,B_0)&amp;1,u_2,u_3u_1,u_2u_3u_1=u&amp;\sigma_3\sigma_1\\ B'_3=(A_3,B_3,B_{\unsure{0}})&amp;1,u_3,u_1u_2,u_3u_1u_2=u&amp;\sigma_1\sigma_2\\ B'_0=(B_1,B_2,B_3)&amp;1,u_2u_3,u_3u_1,u_1u_2&amp;\sigma_1\sigma_2\sigma_3 \end{array}\right\}$}</code>.
- right of brace on second table — <code>$(\mathbb F_2^3)^{\deleted{\unsure{\ast}}}$</code>.
- lower left, comparison maps — <code>\[ \begin{aligned} &amp;A_i\otimes A'_i\xrightarrow{\sim} A\\ &amp;[B_i\subset B'_i]\\ &amp;B_0\otimes B'_0\xrightarrow{\sim} A\quad\text{si les $c_i$ inv. i.e. les $A_i$ étales} \end{aligned} \]</code>.
- foot left, inclusions and identifications — <code>\[ \begin{aligned} A_1&amp;\subset A'_2,A'_3,B'_1\\ A_2&amp;\subset A'_3,A'_1,B'_2\\ A_3&amp;\subset A'_1,A'_2,B'_3\\ B_1&amp;\subset A'_1,B'_1,B'_0\\ B_2&amp;\subset A'_{\unsure{1|2}},B'_{\unsure{1|2}},B'_0\\ B_3&amp;\subset A'_3,B'_3,B'_0\\ B_0&amp;\subset \underset{B_0(A_1)}{\underset{\Vert}{B'_1}},\underset{B_0(A_2)}{\underset{\Vert}{B'_2}},\underset{B_0(A_3)}{\underset{\Vert}{B'_3}} \end{aligned} \]</code>.
- lower right, beside inclusions — <code>$7+7=14$</code>, <code>$A_i$</code>.

**Alterations, additions, marginal writing and underlining**

- left edge, beside first table — <code>\margin{correspondent aux sept hyperplans de $\mathbb F_2^3$, i.e. par \unsure{pol.} \unsure{orth.} aux sept droites de $\mathbb F_2^3$, i.e. aux \deleted{sept éléments non nuls}}</code>.
- left edge, beside first table — <code>\deleted{sept éléments non nuls}</code>.
- right of brace on second table — <code>\deleted{\unsure{\ast}}</code>.
- right of brace on second table — <code>\deleted{sept}</code>.

**Changes**

- <code>\overset{\mathrm{dfn}}=</code> -> <code>\overset{\unsure{\mathrm{déf}|\mathrm{dfn}}}=</code>
- <code>A'_{\unsure{2|1}},B'_{\unsure{2|1}}</code> -> <code>A'_{\unsure{1|2}},B'_{\unsure{1|2}}</code>
- <code>``biquadratiques''</code> -> <code>``\unsure{bi}quadratiques''</code>

## Scan 005

2026-11-18T03:16:20Z to 2026-11-18T03:17:01Z (UTC).

**Reading from the three crops before reopening the page file**

After rotation the printed folio is 449. « prononcé », « éloge », « funèbre », « troisième médaille Fields de L'IHES », « même », « périphrase », « théorie », clipped « cohomologi », « géométrie », « sûrement », « généralité », « ça », « à plein nez », « complète », « d'être donnée », « chef-d'oeuvre ». The quotation has « de là », « théorie de Hodge classique », a broken-looking l in « l-adiques », « suggérées », « où Gr. a trouvé », « sérieuses », « rédigeant », « généralités », « dégagé », « variété algébrique », « variétés », « prouvé », « difficulté », « résultat », « après », « allé chercher là », « ramené », « à une série ». Later « contribué », « grothendieckeries-là », « généraliste-naturaliste », « été », « à nous », « douté », « l'idée saugrenue ». Footnote « (18 mai) », « Eloge Funèbre », « à la terminologie », « perçois », « dérision », « extrême », « donnés », « découle », « censé », unaccented « echos », « été choqué », « dédain », « vis-à-vis », « à ce sujet », « La Perversité » and « n°76 ». Brackets, [?], [!!] and [???] have conspicuously heavy edges.

**Comparison against the transcription**

Read in the order bottom crop, middle crop, top crop after rotating all three by 180 degrees. At the right of the quotation « core » starts the next line in full; the preceding n is at the copying edge. In the footnote « ment » likewise starts a new line in full. Each of seven pairs of square brackets was inspected. The thick end caps are confined to the brackets, with [?], [!!] and [???] enclosing ordinary type. Hand attribution of the reinforcement is uncertain. The rule above the footnote is a separator; there is no adjoining struck text. No marginal prose, formula or i/j index. The capital D in Deligne, H in Hodge, and letters in IHES and Fields are uniform type, with no distinct doubled stem. The initial mark in the first « l-adiques » looks interrupted, while the second « l-adique » has a continuous l.

**Formulae in reading order**


**Alterations, additions, marginal writing and underlining**

- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{[}</code>.
- upright upper middle, quoted passage with brackets — <code>\handwritten{]}</code>.

**Changes**

- <code>en\unsure{core}</code> -> <code>e\unsure{n}core</code>
- <code>naturelle\unsure{ment}</code> -> <code>naturell\unsure{e}ment</code>

## Scan 006

2026-11-18T03:17:01Z to 2026-11-18T03:17:40Z (UTC).

**Reading from the three crops before reopening the page file**

This leaf is almost entirely formulas. The prose strokes read « si 2 inv. », « si c = 0 », « si N(u) = 0, alors … », a second « inv. », and, inside the bottom diagram, « cart. » followed by a second small word. The two occurrences of Tr differ: the first T has a very wide top, the second is crowded by an earlier stroke. A slash of ink runs between the central norm calculation and the left calculation. A small sentence above v and a formula above the N(u) line are crossed.

**Comparison against the transcription**

The bars over u and v are horizontal strokes, with −1 placed high after the barred u. In the product v times its conjugate the exponent on β has been touched by another stroke. There is no subscript i or j. N has one diagonal, Tr has a crossbar and a distinct low r, and G is looped; none shows a second typewriter strike. The long line dividing the two calculations is a separator. The signs in the norm lines and the discarded diagram terms are local cancellations. The arrows below the lowest complete row continue to the edge. Their lower objects are outside the image. I retained plain connections where heads were absent, and recorded the two short words between the vertical arrows as doubtful.

**Formulae in reading order**

- top, two lines — <code>\[ \begin{aligned} 1,u&amp;\qquad -u+\lambda\\ 1,u&amp;\longrightarrow \bar u+\alpha \end{aligned} \]</code>.
- upper third, norm and trace — <code>\[ \begin{aligned} N(\bar u+\alpha)&amp;=N(\bar u)\quad(=N(u))\qquad \operatorname{Tr}(\bar u+\alpha)=\operatorname{Tr}\bar u\ (= \operatorname{Tr}u)\\ \Vert&amp;\\ N(\bar u)+\alpha\operatorname{Tr}(\bar u)+\alpha^2&amp;=N(\bar u)\\ \left\{\begin{aligned}\alpha(\underbrace{\operatorname{Tr}\bar u}_{b}+\alpha)&amp;=0\\2\alpha&amp;=0\end{aligned}\right.&amp;\quad\Longrightarrow\alpha=0\quad\text{si $2$ inv.} \end{aligned} \]</code>.
- middle, loose cancellation and norm-one condition — <code>\[ \begin{aligned} &amp;\deleted{\lambda+\mu u}\qquad\qquad u\bar u=N(u)\\ &amp;N(v)=1\quad\Longrightarrow\quad v=u\bar u^{-1}\ \deleted{\unsure{\in}}\ (=u^2N(u)^{-1})\\ &amp;\hspace{50pt}u^2+ub +c=0\qquad \operatorname{Tr}u=-b \end{aligned} \]</code>.
- middle left and right, norm computation — <code>\[ \begin{aligned} v&amp;=\alpha+\beta u&amp; N(v)&amp;=\alpha^2\deleted{\unsure{+}}-\alpha\beta b+\beta^2c=1\\ \bar v&amp;=(\alpha-\beta b)-\beta u&amp;&amp;=\alpha(\alpha-\beta b)\quad\text{si }c=0\\ v\bar v&amp;=\alpha(\alpha-\beta b)-\beta^{\unsure{2|+}}c\,-\\ v&amp;=\alpha\unsure{-|+}\beta u&amp;v\bar v&amp;=\alpha^2+\beta^2+\alpha\beta\underbrace{(u+\bar u)}_{\operatorname{Tr}u}\\ \bar v&amp;=\alpha+\beta\bar u \end{aligned} \]</code>.
- lower middle, norm of w — <code>\[ \begin{aligned} w&amp;=\lambda1+\mu u\quad\text{si }\deleted{\unsure{N(u)=}}\,N(u)=0,\ \text{\unsure{donc|et si} }N(w)\ \text{inv.}\\ N(w)&amp;=\lambda^2\deleted{\unsure{+}}-\lambda\mu b=\lambda(\lambda-\mu b)\qquad\Longrightarrow\lambda\ \text{inv.} \end{aligned} \]</code>.
- lower right, isolated equality — <code>\[\alpha(\alpha-\beta b)=1\]</code>.
- foot left, three rows with incoming arrows at lower edge — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;,column sep=small] 1\arrow[r]\&amp; SW/\mu_{\unsure{2}}\arrow[r,"\sim"]\&amp;W^\ast/G_m\arrow[r]\&amp;1\&amp;\\ \&amp;\deleted{\unsure{w\bar w}}\&amp;\deleted{\unsure{N}}\&amp;\&amp;\\ 1\arrow[r]\&amp; SW\arrow[uu]\arrow[r,dash]\&amp; W^\ast\arrow[uu]\arrow[r,"N"]\&amp; G_m\arrow[uu]\arrow[r]\&amp;1\\ 1\arrow[r]\&amp;\mu_2\arrow[u]\arrow[r,dash]\&amp;G_m\arrow[u,"{\text{cart.}\atop\text{\unsure{et commut.|évident}}}"']\arrow[r,"{\unsure{\zeta^2|z^2}}"]\&amp;G_m\arrow[u,equal]\arrow[r]\&amp;1\\ \&amp;{}\arrow[u]\&amp;{}\arrow[u]\&amp;{}\arrow[u]\&amp; \end{tikzcd}} % archive sheet number: 5</code>.

**Alterations, additions, marginal writing and underlining**

- middle, loose cancellation and norm-one condition — <code>\deleted{\lambda+\mu u}</code>.
- middle, loose cancellation and norm-one condition — <code>\deleted{\unsure{\in}}</code>.
- middle left and right, norm computation — <code>\deleted{\unsure{+}}</code>.
- lower middle, norm of w — <code>\deleted{\unsure{N(u)=}}</code>.
- lower middle, norm of w — <code>\deleted{\unsure{+}}</code>.
- foot left, three rows with incoming arrows at lower edge — <code>\deleted{\unsure{w\bar w}}</code>.
- foot left, three rows with incoming arrows at lower edge — <code>\deleted{\unsure{N}}</code>.

**Changes**

- <code>\unsure{ub|ub\,}</code> -> <code>ub</code>
- <code>\deleted{\unsure N}</code> -> <code>\deleted{\unsure{N}}</code>
- <code>\text{\unsure{évident}}</code> -> <code>\text{\unsure{et commut.|évident}}</code>
- <code>\text{donc }N(w)</code> -> <code>\text{\unsure{donc|et si} }N(w)</code>

## Scan 007

2026-11-18T03:17:41Z to 2026-11-18T03:18:56Z (UTC).

**Reading from the three crops before reopening the page file**

Folio 444. « vérité », « à la trouver », « même à la prouver à son entière satisfaction », « sûrement », « empaillé si ça se trouve », « à son entière », « placé », « désire la connaître », « connaît », « tiède ou fraîche », « agitée », « sûrement la connaîtra », « peu ou prou », « d'étapes », « désire connaître ». Then « j'ai été », « tour à tour », « critères objectifs », « çà! » (grave over a), « qu'à », « difficulté », « à distinguer les étapes successives », « décantation », « à partir de cette étape », « ou nul pressenti affleurant à la conscience », « soupçonner », « au delà », « présentent », « à travers », « éveils », « amène », « appréhension », « délicate », « complète », « différente », « découverte », « mathématiques », « s'approfondit peu à peu (fût-ce à travers … corrigées) », « irrécusable », « là », « intérieure », « curiosité », « vis à vis », « dépister », « découvrir ». The a of affleurant and s of s'approfondit are dark. Spaced type on « du », « ses amours », « progression », « connaissance », « assurance », « ouverture au doute », « foi ».

**Comparison against the transcription**

Magnified « succéssives »: a separate diagonal rises above the first e after cc; the next « successifs » has none. The small stop after « cas » is printed; the expected stop after the clipped « prou » cannot be seen. There is a faint two-stroke mark to the right of 444. The a in affleurant and the s in s'approfondit are superimposed on darker earlier letters. Their underlying forms and the manner in which the upper letters were made remain uncertain. The stroke below « indispensable » does not run through its type. The interior p in the spaced word « progression » is ordinary type, and none of the capital initials of paragraphs shows doubled construction. No formulas, i/j indices or independent marginal words.

**Formulae in reading order**


**Alterations, additions, marginal writing and underlining**

- top, typed foliation — <code>\handwritten{\unsure{h|4}}</code>.
- lower middle, stages of discovery — <code>\deleted{\unsure{e}}</code>.
- lower middle, stages of discovery — <code>\handwritten{a}</code>.
- lower middle, stages of discovery — <code>\deleted{\unsure{a}}</code>.
- lower middle, stages of discovery — <code>\handwritten{s}</code>.

**Changes**

- <code>\mspage{444}</code> -> <code>\mspage{444} \handwritten{\unsure{h|4}}</code>
- <code>ou en tous cas\unsure{.}</code> -> <code>ou en tous cas.</code>

## Scan 009

2026-11-18T03:18:56Z to 2026-11-18T03:19:52Z (UTC).

**Reading from the three crops before reopening the page file**

Heading « Formes quadratiques binaires et revêtements quadratiques » and « Forme[s] quadratique[s] à scalaire près, structure de similitude ». §1.1 has « désigne », « un schéma, plus généralement un topos loc. annelé », « Soit E un Module », « loc. libre de type fini », « iso. can. », « en général », « seulement un homomorphisme can. », « transforme … en », « opère », « d'où », « quotient », « s'appelle », « correspond », « ensembliste », « à fibres non vides », « transitivement ». Later « localement », « définie », « définissent », « ssi », « Le cas le plus intéressant », « sans * ! », « injectif », and a crossed phrase before the final equals sign.

**Comparison against the transcription**

The Hom display really ends in E. The first symbol inside its parentheses has a horizontal cap and downstroke, consistent with Γ rather than a looped script T; its exponent is 2. All three instances of the dual have a small vee on E. The subscript on Q in the product line is overtraced; f and g remain alternatives to a comma-separated pair. No i or j index. Underlining is integral to the names Quad, Hom, Sym, Sim and the structure sheaf where actually drawn. The upper stroke by « formes » touches a letter and does not strike it. The isolated scribble just before « en groupes » is separate from the final O. In the last paragraph « sans * ! » has a star and a separate exclamation mark, and the last equals sign continues onto scan 10.

**Formulae in reading order**

- 1.1, opening — <code>$(X,\underline{\mathcal O}_X)$</code>, <code>$E$</code>, <code>$X$</code>.
- upper third, definition — <code>\[\underline{\mathrm{Quad}}(E)\simeq\underline{\mathrm{Hom}}(\Gamma^2(E),E)\]</code>.
- below first formula — <code>$E$</code>, <code>$E$</code>.
- upper third, canonical isomorphism — <code>\[\underline{\mathrm{Quad}}(E)\simeq\underline{\mathrm{Sym}}^2(E^\vee),\]</code>.
- upper middle, homomorphism — <code>\[\underline{\mathrm{Sym}}^2(E^\vee)\longrightarrow\underline{\mathrm{Quad}}(E),\]</code>.
- middle, description of map — <code>$f.g$</code>, <code>$f,g\in\Gamma E^\vee$</code>, <code>$Q_{\unsure{fg|f,g}}:x\longmapsto f(x)g(x)$</code>, <code>$E$</code>.
- middle, group action — <code>$\unsure{\underline{\mathcal O}}$</code>, <code>$\underline{\mathcal O}_X^\ast$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>.
- middle, quotient — <code>\[\underline{\mathrm{Sim}}(E)\simeq\underline{\mathrm{Quad}}(E)/\underline{\mathcal O}^{\ast}.\]</code>.
- lower half, definition and local representatives — <code>$E$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>, <code>$\mathcal O^\ast$</code>, <code>$Q$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>, <code>$E$</code>, <code>$Q$</code>, <code>$Q'$</code>, <code>$=$</code>, <code>$\exists$</code>, <code>$a\in\Gamma\underline{\mathcal O}_X^\ast$</code>, <code>$Q'=aQ$</code>.
- foot, injectivity condition — <code>$a\mapsto aQ$</code>.
- foot, scalar map — <code>\[a\longrightarrow a.Q:\underline{\mathcal O}_X\ (\text{sans $\ast$\,!})\longrightarrow\underline{\mathrm{Quad}}(E)\]</code>.
- last line continues — <code>$Q'$</code>, <code>$=$</code>.

**Alterations, additions, marginal writing and underlining**

- top, title — <code>\uline{quadratiques binaires et}</code>.
- 1.1, opening — <code>\underline{\mathcal O}</code>.
- upper third, definition — <code>\underline{\mathrm{Quad}}</code>.
- upper third, definition — <code>\underline{\mathrm{Hom}}</code>.
- upper third, canonical isomorphism — <code>\underline{\mathrm{Quad}}</code>.
- upper third, canonical isomorphism — <code>\underline{\mathrm{Sym}}</code>.
- upper middle, homomorphism — <code>\underline{\mathrm{Sym}}</code>.
- upper middle, homomorphism — <code>\underline{\mathrm{Quad}}</code>.
- middle, group action — <code>\deleted{$\unsure{\underline{\mathcal O}}$}</code>.
- middle, group action — <code>\underline{\mathcal O}</code>.
- middle, group action — <code>\underline{\mathcal O}</code>.
- middle, group action — <code>\underline{\mathrm{Quad}}</code>.
- middle, quotient — <code>\underline{\mathrm{Sim}}</code>.
- middle, quotient — <code>\underline{\mathrm{Quad}}</code>.
- middle, quotient — <code>\underline{\mathcal O}</code>.
- lower half, definition and local representatives — <code>\uline{structure de similitude}</code>.
- lower half, definition and local representatives — <code>\underline{\mathrm{Quad}}</code>.
- lower half, definition and local representatives — <code>\deleted{loc}</code>.
- lower half, definition and local representatives — <code>\underline{\mathrm{Quad}}</code>.
- lower half, definition and local representatives — <code>\deleted{\unsure{deux}}</code>.
- lower half, definition and local representatives — <code>\underline{\mathcal O}</code>.
- foot, injectivity condition — <code>\deleted{$a\mapsto aQ$}</code>.
- foot, scalar map — <code>\underline{\mathcal O}</code>.
- foot, scalar map — <code>\underline{\mathrm{Quad}}</code>.
- last line continues — <code>\deleted{si}</code>.
- last line continues — <code>\deleted{\unsure{est connu de}}</code>.
- last line continues — <code>\inserted{définit la}</code>.

**Changes**

- <code>homomorphisme can</code> -> <code>homomorphisme can.</code>
- <code>similitude sss</code> -> <code>similitude \unsure{sss|ssi}</code>

## Scan 010

2026-11-18T03:19:53Z to 2026-11-18T03:26:20Z (UTC).

**Reading from the three crops before reopening the page file**

Continuation « structure de similitude », « globalement » underlined, « unique (car on a aussi l'unicité) ». Addition « Structure de similitude fidèle : définie loc. par une Q telle que … injectif », then « un choix de Q, seulement de la structure de similitude ». In 1.2 « on peut regarder le sous-Module engendré », « et on voit que … donne une bijection entre l'ens. des structures … et l'ens. des sous-Modules », « localement monogènes », « fidèles », « inversibles ». N.B. has « Comm. », « Dans le cas où … », « un hom. qq̲u̲e̲l̲c̲. », « n'induit évidemment pas structur… ». §1.3 « loc. lib. de type fini », « de = de », « strictement fidèle », « universellement fidèle », « l'hom. précédent », « universellement injectif », « revient au = », « sur chaque fibre résiduelle ».

**Comparison against the transcription**

In the upper margin the insertion belongs before « fidèle ». The word « unicité » is clearer than the clause that precedes it. The quotient action has a raised star and a small smudged subscript, distinct from the large X on the preceding page. The short P→Δ line has scarcely a head; the later map from Δ has a clear hook and head. The note before 1.3 crosses an abandoned start to the next line. In that start the loop after « loc. » is compatible with an abbreviation of « libre »; its reading as a standalone script L is weak. Rechecked the second power of Sym: the manuscript shows (E), with no vee. No i/j subscript. Sloping baseline strokes beneath globalement, fidèles, inversibles and strictement fidèle are underlines.

**Formulae in reading order**

- top, end of 1.1 — <code>$\exists\,a\in\Gamma\underline{\mathcal O}_{\unsure{\alpha|X}}^\ast$</code>, <code>$Q'=aQ$</code>, <code>$a$</code>, <code>$Q$</code>, <code>$a\longmapsto aQ$</code>, <code>$Q$</code>.
- upper third, 1.2 — <code>$P\subset\underline{\mathrm{Quad}}(E)$</code>.
- upper third, generated submodule — <code>\[\Delta=\Delta_P\subset\underline{\mathrm{Quad}}(E),\]</code>.
- middle, correspondence — <code>\[P\mathrel{\unsure{-|\longrightarrow}}\Delta_P\]</code>.
- middle, local generators — <code>$E$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>.
- lower middle, inclusion — <code>\[\Delta\lhook\joinrel\longrightarrow\underline{\mathrm{Quad}}(E)\]</code>.
- small interline note above 1.3 — <code>$\Delta\longrightarrow\underline{\mathrm{Quad}}(E)$</code>.
- foot, 1.3 — <code>$E$</code>, <code>$=$</code>, <code>$\underline{\mathrm{Quad}}(E)\simeq\underline{\mathrm{Sym}}^2(E)$</code>, <code>$=$</code>.

**Alterations, additions, marginal writing and underlining**

- top, end of 1.1 — <code>\underline{\mathcal O}</code>.
- top, end of 1.1 — <code>\uline{globalement}</code>.
- top, end of 1.1 — <code>\deleted{On appelle des}</code>.
- top, end of 1.1 — <code>\inserted{Structure de similitude}</code>.
- top, end of 1.1 — <code>\deleted{cela ne dépend pas du choix de}</code>.
- top, end of 1.1 — <code>\deleted{$Q$}</code>.
- upper third, 1.2 — <code>\deleted{\unsure{Soit}}</code>.
- upper third, 1.2 — <code>\deleted{\unsure{par}}</code>.
- upper third, 1.2 — <code>\underline{\mathrm{Quad}}</code>.
- upper third, generated submodule — <code>\underline{\mathrm{Quad}}</code>.
- middle, local generators — <code>\underline{\mathrm{Quad}}</code>.
- middle, local generators — <code>\deleted{\unsure{formes q}}</code>.
- middle, local generators — <code>\deleted{fidèl}</code>.
- middle, local generators — <code>\uline{fidèles}</code>.
- lower middle, inclusion — <code>\underline{\mathrm{Quad}}</code>.
- lower middle, end of 1.2 — <code>\uline{inversibles}</code>.
- small interline note above 1.3 — <code>\margin{\uline{NB} Dans le cas où on a un hom \uline{quelc.} $\Delta\longrightarrow\underline{\mathrm{Quad}}(E)$ (donc non \unsure{forc.} injectif) \unsure{s'in.}\ \deleted{\unsure{est}} \deleted{\unsure{fid}} définissant \deleted{une} \deleted{structure}}</code>.
- small interline note above 1.3 — <code>\uline{NB}</code>.
- small interline note above 1.3 — <code>\uline{quelc.}</code>.
- small interline note above 1.3 — <code>\underline{\mathrm{Quad}}</code>.
- small interline note above 1.3 — <code>\deleted{\unsure{est}}</code>.
- small interline note above 1.3 — <code>\deleted{\unsure{fid}}</code>.
- small interline note above 1.3 — <code>\deleted{une}</code>.
- small interline note above 1.3 — <code>\deleted{structure}</code>.
- foot, 1.3 — <code>\inserted{\unsure{loc\textsuperscript{t}.}}</code>.
- foot, 1.3 — <code>\deleted{\unsure{résulte}}</code>.
- foot, 1.3 — <code>\underline{\mathrm{Quad}}</code>.
- foot, 1.3 — <code>\underline{\mathrm{Sym}}</code>.
- foot, 1.3 — <code>\uline{strictement fidèle}</code>.

**Changes**

- <code>similitude sss</code> -> <code>similitude \unsure{sss|ssi}</code>
- <code>en quoi résume l'\unsure{unicité}</code> -> <code>\unsure{en quoi résume|en quoi réside} l'unicité</code>
- <code>\inserted{\unsure{loc\textsuperscript{t}.}} $\unsure{\mathscr L|L}$ de type fini, il en \unsure{résulte}</code> -> <code>\inserted{\unsure{loc\textsuperscript{t}.}} \unsure{lib.|L.} de type fini, il en \deleted{\unsure{résulte}}</code>

## Scan 011

2026-11-18T03:26:20Z to 2026-11-18T03:26:54Z (UTC).

**Reading from the three crops before reopening the page file**

« les structures de similitude strictement fidèles », « sous-fibrés vectoriels de rang 1 du fibré vectoriel », « ou encore aux sections du fibré en espaces projectifs ». In 1.4 « Soient Δ un Module inv. sur X », « un hom (pas néc. injectif) », « définissant donc une structure », « Je dis qu'on a une forme quadratique … canonique à valeurs dans le module inversible », « Pour la définir, je vais d'abord définir », « (indép. de la donnée de …) », « forme quadratique canonique ». Foot « sa valeur, pour une section locale », « est la forme linéaire », « pour toute section (locale) », « celle-ci dépend de x de façon quadratique, i.e. », and some overwriting where the alleged polarized map begins.

**Comparison against the transcription**

In the vector bundle symbol there is an extra small low turn before the oblique strokes; both W and V deserve recording. The corresponding projective P carries a separate raised vee. The little label over Δ→Quad(E) has a dot above the live i and an overwritten earlier stroke. No i or j below or above another mathematical letter. At the foot the two pointers reach the evaluation formula and its qualifications; they do not strike the f(x) on the right. The function word after « la » is crossed through. The dual mark after Quad(E) and the subscript f on the polarization are distinct. The heavy initial Q of Q=Q_E is traced over, without a legible different letter beneath it. The paired f and x in the angle brackets have a comma between them.

**Formulae in reading order**

- top, continuation of 1.3 — <code>$\unsure{W|V}(\underline{\mathrm{Quad}}(E))$</code>, <code>$P^\vee(\underline{\mathrm{Quad}}(E))$</code>.
- upper third, 1.4 — <code>$\Delta$</code>, <code>$X$</code>.
- upper third, morphism i — <code>\[\deleted{\unsure{\Delta}}\qquad\Delta\xrightarrow{\deleted{\unsure{\alpha}}i}\underline{\mathrm{Quad}}(E)\]</code>.
- middle, form with values in the dual — <code>$\Sigma$</code>, <code>$E$</code>, <code>$Q_\Sigma$</code>, <code>$Q$</code>, <code>$\Delta^\vee$</code>, <code>$i$</code>, <code>$\Sigma$</code>.
- lower third, universal evaluation — <code>\[Q=Q_E:E\longrightarrow\underline{\mathrm{Quad}}(E)^\vee:\]</code>.
- lower third, first description — <code>$x$</code>, <code>$E$</code>.
- lower third, evaluation formula and insertion — <code>\[Q(x)=\{f\longmapsto f(x)\}\quad\inserted{\text{i.e. }f(x)=\langle f,Q(x)\rangle}\]</code>.
- interlined below evaluation — <code>$f$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>, <code>$x$</code>, <code>$E$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>, <code>$x$</code>, <code>$E\times E\longrightarrow\underline{\mathrm{Quad}}(E)^\vee$</code>.
- foot, polarization — <code>\[ \unsure{\text{qui transforme}}\quad x,y\ \text{en}\quad Q(x+y)-Q(x)-Q(y)=\{f\longmapsto\underbrace{f(x+y)-f(x)-f(y)}_{\varphi_f(x,y)}\} \]</code>.

**Alterations, additions, marginal writing and underlining**

- top, continuation of 1.3 — <code>\uline{sous-fibrés vectoriels de rang 1}</code>.
- top, continuation of 1.3 — <code>\underline{\mathrm{Quad}}</code>.
- top, continuation of 1.3 — <code>\underline{\mathrm{Quad}}</code>.
- upper third, morphism i — <code>\deleted{\unsure{\Delta}}</code>.
- upper third, morphism i — <code>\deleted{\unsure{\alpha}}</code>.
- upper third, morphism i — <code>\underline{\mathrm{Quad}}</code>.
- middle, form with values in the dual — <code>\inserted{donc}</code>.
- middle, form with values in the dual — <code>\inserted{$Q_\Sigma$ ou $Q$}</code>.
- lower third, universal evaluation — <code>\underline{\mathrm{Quad}}</code>.
- lower third, first description — <code>\deleted{elle associe}</code>.
- lower third, evaluation formula and insertion — <code>\inserted{\text{i.e. }f(x)=\langle f,Q(x)\rangle}</code>.
- interlined below evaluation — <code>\inserted{(pour toute section (locale) $f$ de $\underline{\mathrm{Quad}}(E)$, $x$ de $E$,}</code>.
- interlined below evaluation — <code>\underline{\mathrm{Quad}}</code>.
- interlined below evaluation — <code>\underline{\mathrm{Quad}}</code>.
- interlined below evaluation — <code>\deleted{fonction}</code>.
- interlined below evaluation — <code>\underline{\mathrm{Quad}}</code>.

**Changes**

- <code>Vectoriel $W(</code> -> <code>Vectoriel $\unsure{W|V}(</code>
- <code>\unsure{je} vais</code> -> <code>je vais</code>

## Scan 012

2026-11-18T03:26:55Z to 2026-11-18T03:27:58Z (UTC).

**Reading from the three crops before reopening the page file**

Upper continuation « est bilinéaire en x,y », « Comme on a, par transposition de i », « on déduit une forme quadratique composée », « Dans le cas d'une structure de similitude fidèle », « ne dépend, à iso. can. unique près », « ce qui justifie alors la notation ». N.B. « Quand on se donne une base e de Δ », « s'identifie à une forme quadr. ordinaire », « i.e. à val. dans O », « et ce n'est autre que ». Rotated left margin: §1.5 « la donnée d'une structure de similitude », « strictement », « sur E », « équivaut à celle d'un Module inv. Δ sur X, et d'une forme quadratique », « i.e. sur aucune fibre résiduelle », « identiquement nulle ». §2.1 « On suppose à partir de maintenant », « loc. libre de rang 2 », « son Module déterminantiel », « qui est un Module inversible », « Notons l'iso. can. », « donné par », « i.e. », « associé à l'accouplement canonique ».

**Comparison against the transcription**

Rotating both pieces of the marginal §1.5 makes « sur aucune fibre résiduelle » legible across the join. The rising leader carries « strictement » into the qualifier. Q has domain E and target Δ dual, followed by a second Δ dual in the generation clause. Qᵢ has a short, dotted subscript i; in the arrow label i is a main letter carrying a superscript vee. No j. The three arrows of the triangle were compared for source and target. Below, the T-shaped component of det is underlined, the dual mark over E is open and low, and the double wedge in the last formula is an exterior power with superscript 2. The baseline of « déterminantiel » runs through the middle letters and is not a separate cancellation. The giant angled rule at the left brackets §1.5.

**Formulae in reading order**

- top, end of polarization — <code>$x,y$</code>.
- upper third, transpose — <code>$i:\Delta\longrightarrow\underline{\mathrm{Quad}}(E)$</code>.
- upper third, dual arrow — <code>\[\underline{\mathrm{Quad}}(E)^\vee\xrightarrow{i^\vee}\Delta^\vee,\]</code>.
- upper middle, composition triangle — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;] \&amp;\underline{\mathrm{Quad}}(E)^\vee\arrow[dr,"i^\vee"]\&amp;\\ Q_i\ \text{ou }Q_\Sigma:\quad E\arrow[ur,"Q"]\arrow[rr]\&amp;\&amp;\Delta^\vee. \end{tikzcd}}</code>.
- middle, independence — <code>$\Sigma$</code>, <code>$(\Delta,i)$</code>, <code>$\Sigma$</code>, <code>$=$</code>, <code>$Q_i$</code>, <code>$Q_\Sigma$</code>.
- middle, small NB above rule — <code>$e$</code>, <code>$\Delta$</code>, <code>$\Delta\simeq\Delta^\vee\simeq\underline{\mathcal O}$</code>, <code>$Q_\Sigma$</code>, <code>$E$</code>, <code>$\underline{\mathcal O}$</code>, <code>$\unsure{f(x)}$</code>, <code>$f=i(e)$</code>.
- left edge, section 1.5, turned clockwise to read — <code>$E$</code>, <code>$\Delta$</code>, <code>$X$</code>, <code>$Q:E\longrightarrow\Delta^\vee$</code>, <code>$Q(E)$</code>, <code>$\Delta^\vee$</code>, <code>$Q_x$</code>.
- lower third, 2.1 — <code>$E$</code>.
- lower third, determinant — <code>\[L=\underline{\det}E=\bigwedge^2 E\]</code>.
- near foot, isomorphism — <code>\[E\xrightarrow{\sim} E^\vee\otimes L\]</code>.
- near foot, wedge map — <code>\[(x\longmapsto(y\longmapsto x\wedge y)),\quad\text{i.e.}\]</code>.
- last line — <code>\[E\times E\longrightarrow L=\bigwedge^2 E:(x,y)\longmapsto x\wedge y.\]</code>.

**Alterations, additions, marginal writing and underlining**

- top, end of polarization — <code>\deleted{\unsure{S}}</code>.
- upper third, transpose — <code>\underline{\mathrm{Quad}}</code>.
- upper third, dual arrow — <code>\underline{\mathrm{Quad}}</code>.
- upper middle, composition triangle — <code>\underline{\mathrm{Quad}}</code>.
- middle, independence — <code>\inserted{$\Sigma$}</code>.
- middle, independence — <code>\inserted{can.}</code>.
- middle, independence — <code>\deleted{Quand on}</code>.
- middle, small NB above rule — <code>\uline{NB}</code>.
- middle, small NB above rule — <code>\underline{\mathcal O}</code>.
- middle, small NB above rule — <code>\underline{\mathcal O}</code>.
- middle, small NB above rule — <code>\deleted{$\unsure{f(x)}$}</code>.
- middle, small NB above rule — <code>\inserted{$f=i(e)$.}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\margin{1.5. La donnée d'une structure de similitudes \inserted{(\uline{strictement})} \uline{fidèle} \inserted{sur $E$} \unsure{équivaut|revient} à celle d'un Module inv. $\Delta$ sur $X$, et d'une forme quadratique $Q:E\longrightarrow\Delta^\vee$ telle que \uline{$Q(E)$ engendre} $\Delta^\vee$, i.e. \deleted{\unsure{$Q_x$ est non}} sur aucune fibre résiduelle, \deleted{\unsure{est nul}} identiquement nulle.}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\inserted{(\uline{strictement})}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\uline{strictement}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\uline{fidèle}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\inserted{sur $E$}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\uline{$Q(E)$ engendre}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\deleted{\unsure{$Q_x$ est non}}</code>.
- left edge, section 1.5, turned clockwise to read — <code>\deleted{\unsure{est nul}}</code>.
- lower third, determinant — <code>\underline{\det}</code>.

**Changes**

- <code>revient à celle</code> -> <code>\unsure{équivaut|revient} à celle</code>
- <code>Module déterminant,</code> -> <code>Module déterminantiel,</code>
- <code>\unsure{sur aucune fibre résiduelle}</code> -> <code>sur aucune fibre résiduelle</code>

## Scan 013

2026-11-18T03:27:58Z to 2026-11-18T03:28:42Z (UTC).

**Reading from the three crops before reopening the page file**

« On en déduit des iso. can. », « Il en résulte un isom. canonique de faisceaux », « qui transforme le sous-Module loc. monogène Δ … dans … », « On trouve que … sont inverses l'un de l'autre », « notions de [structures de] similitudes fidèles, strictement fidèles, non-dégénérées transversalement … universellement … », « pour E et pour E dual se correspondent ». §2.2 « Considérons encore l'iso. can. (dépendant du choix d'un signe) », the added « à droite » and tensor sign, « on trouve », « D'autre part on a », « pour tout », « suite exacte canonique », « et on peut mettre un 0 à g. si E loc. libre … ». No accents are visible on the short « can. » labels in the map.

**Comparison against the transcription**

Compared each E with the form carrying a little vee to its upper right. In the second crop, directly above the E after the struck Sym, the ink is a filled patch; the likely former vee is classified as cancelled. The smaller addition at the far right sits below the power of L and meets the crop edge. The two small marks over the Sim arrow are both above the shaft. In the left display the same negative tensor power is written under a brace, not in the baseline formula. The two leaders on the « notions » sentence are insertions. The written lower-case can has subscript E or E-dual; there are no i or j indices. The looped capitals of Sim and Sym have no separate second vertical. In the bottom map the order in the difference is x⊗y then y⊗x.

**Formulae in reading order**

- upper third, bracketed identifications — <code>\[ \left\{\begin{aligned} E^\vee&amp;\simeq E\otimes L^\vee\\ \underbrace{\mathrm{Sym}^2(E^\vee)}_{\underline{\mathrm{Quad}}(E)} &amp;\simeq\underbrace{\mathrm{Sym}^2(E)}_{\underline{\mathrm{Quad}}(E^\vee)}\otimes \underbrace{L^{\vee\otimes2}}_{L^{\otimes(-2)}} \end{aligned}\right. \]</code>.
- upper right, abbreviation beside second identification — <code>$\underline{\mathrm{Quad}}(E)\simeq\mathrm{Quad}(E^\vee)\otimes L^{\otimes\unsure{-2}}$</code>.
- upper middle, map of similarity sheaves — <code>\[\underline{\mathrm{Sim}}(E)\xrightarrow{\substack{\mathrm{can}_E\\\sim}}\underline{\mathrm{Sim}}(E^\vee)\]</code>.
- middle, effect on a submodule — <code>$\Delta$</code>, <code>$\underline{\mathrm{Sym}}^2(E^\vee)\simeq\mathrm{Quad}(E)$</code>.
- middle, tensor powers — <code>\[ \begin{aligned} \Delta\otimes L^{\otimes(\unsure{2|-2})}&amp;\subset \deleted{\underline{\mathrm{Sym}}^2(E)}\ \underline{\mathrm{Quad}}(E^{\deleted{\unsure{\vee}}})\otimes L^{\otimes2} \simeq \mathrm{Quad}(E^\vee)\otimes L^{\otimes(-2)}\inserted{\unsure{\otimes L^{\otimes2}|\otimes2}}\\ &amp;\simeq\mathrm{Quad}(E^\vee). \end{aligned} \]</code>.
- middle lower, inverse and corresponding properties — <code>$\mathrm{can}_E$</code>, <code>$\mathrm{can}_{E^\vee}$</code>, <code>$E$</code>, <code>$E^\vee$</code>.
- lower third, dual of E — <code>\[E^\vee\simeq E\otimes L^\vee,\]</code>.
- lower third, multiplying on right — <code>$\otimes$</code>, <code>$E$</code>.
- near foot, tensor product — <code>\[E^\vee\otimes E\simeq E\otimes E\otimes L^\vee\]</code>.
- near foot, short exact sequence — <code>$\underline{\mathcal O}_X$</code>, <code>$0$</code>, <code>$E$</code>.
- bottom, maps — <code>\[ \begin{aligned} \bigwedge^2 E&amp;\longrightarrow E\otimes E\longrightarrow\mathrm{Sym}^2(E)\longrightarrow0,\\ x\wedge y&amp;\longrightarrow x\otimes y-y\otimes x \end{aligned} \]</code>.

**Alterations, additions, marginal writing and underlining**

- upper third, bracketed identifications — <code>\underline{\mathrm{Quad}}</code>.
- upper third, bracketed identifications — <code>\underline{\mathrm{Quad}}</code>.
- upper right, abbreviation beside second identification — <code>\margin{i.e. $\underline{\mathrm{Quad}}(E)\simeq\mathrm{Quad}(E^\vee)\otimes L^{\otimes\unsure{-2}}$}</code>.
- upper right, abbreviation beside second identification — <code>\underline{\mathrm{Quad}}</code>.
- upper middle, map of similarity sheaves — <code>\underline{\mathrm{Sim}}</code>.
- upper middle, map of similarity sheaves — <code>\underline{\mathrm{Sim}}</code>.
- middle, effect on a submodule — <code>\underline{\mathrm{Sym}}</code>.
- middle, tensor powers — <code>\deleted{\underline{\mathrm{Sym}}^2(E)}</code>.
- middle, tensor powers — <code>\underline{\mathrm{Sym}}</code>.
- middle, tensor powers — <code>\underline{\mathrm{Quad}}</code>.
- middle, tensor powers — <code>\deleted{\unsure{\vee}}</code>.
- middle, tensor powers — <code>\inserted{\unsure{\otimes L^{\otimes2}|\otimes2}}</code>.
- middle lower, inverse and corresponding properties — <code>\inserted{structures de}</code>.
- middle lower, inverse and corresponding properties — <code>\uline{fidèles}</code>.
- middle lower, inverse and corresponding properties — <code>\inserted{pour $E$ et pour $E^\vee$}</code>.
- lower third, multiplying on right — <code>\inserted{$\otimes$-}</code>.
- lower third, multiplying on right — <code>\inserted{à droite}</code>.
- near foot, short exact sequence — <code>\deleted{\unsure{un is. canonique}}</code>.
- near foot, short exact sequence — <code>\inserted{(pour tout $\underline{\mathcal O}_X$-Module)}</code>.
- near foot, short exact sequence — <code>\underline{\mathcal O}</code>.

**Changes**

- <code>E^{\unsure{\vphantom E\vee}}</code> -> <code>E^{\deleted{\unsure{\vee}}}</code>
- <code>\xrightarrow[\sim]{\mathrm{can}_E}</code> -> <code>\xrightarrow{\substack{\mathrm{can}_E\\\sim}}</code>
- <code>L^{\otimes(-2)\,\unsure{\otimes2}}</code> -> <code>L^{\otimes(-2)}\inserted{\unsure{\otimes L^{\otimes2}|\otimes2}}</code>

## Scan 014

2026-11-18T03:28:43Z to 2026-11-18T03:29:16Z (UTC).

**Reading from the three crops before reopening the page file**

« et dans le cas actuel … est inversible », then crossed « et de plus », « donc », « d'où en multipliant par ». « Je dis que par l'iso. can. vertical, le sous-Module … est transformé en le sous-Module … de End(E), de façon plus précise que l'on a … un diagramme commutatif », « d'iso. canonique ». At the foot, under the diagram « d'où par retour … à la notation … ». The det abbreviation sits over the O/L column. First and last terms of both horizontal rows are small zeroes.

**Comparison against the transcription**

The mark on the first equals sign has a long descender, like the corresponding abbreviation on scan 4. The middle segment leading to Sym² in the first sequence has a long shaft with no distinct head. I distinguished that from the arrow into E⊗E. In the comparison diagram the arrows point down, and the first has a separate id with small underlined O as its subscript. None of these is an indexed i or j. The left edge of L overlaps a previous curl; the dual power beside L remains visible. End is underlined, the capital E has no doubled vertical, and the low O after the slash in the lower output diagram is not underlined. The words leading to « un diagramme » are crossed at the right, independently of the rule beneath the insertion.

**Formulae in reading order**

- top, continuation of 2.2 — <code>$\bigwedge^2 E\overset{\unsure{\mathrm{déf}|\mathrm{dfn}}}=L$</code>.
- upper third, exact sequence — <code>\[0\mathrel{-}L\longrightarrow E\otimes E\mathrel{\unsure{-|\longrightarrow}}\mathrm{Sym}^2(E)\mathrel{-}0,\]</code>.
- upper third, tensoring — <code>$L^\vee$</code>.
- upper third, twisted sequence — <code>\[0\longrightarrow\underline{\mathcal O}\longrightarrow\underbrace{(E\otimes E)\otimes L^\vee}_{\rotatebox{90}{$\simeq$}\ E^\vee\otimes E\simeq\underline{\mathrm{End}}(E)}\mathrel{-}\mathrm{Sym}^2(E)\otimes L^\vee\mathrel{-}0\]</code>.
- middle, identification of scalars — <code>$L\otimes L^\vee\simeq\underline{\mathcal O}$</code>, <code>$\underline{\mathcal O}.1_E$</code>, <code>$\underline{\mathrm{End}}(E)$</code>.
- middle to lower third, comparison of the two rows — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;,column sep=small,row sep=large] 0\arrow[r,dash]\&amp;\underset{\underline{\mathcal O}}{\underbrace{\overbrace{L}^{\det E}\otimes L^\vee}}\arrow[r]\arrow[d,"\sim"'," {\mathrm{id}_{\underline{\mathcal O}}}"]\&amp;(E\otimes E)\otimes L^\vee\arrow[r,dash]\arrow[d,"\sim"']\&amp;\overbrace{\mathrm{Sym}^2(E)}^{\mathrm{Quad}(E^\vee)\simeq\mathrm{Quad}(E)\otimes L^{\otimes2}}\otimes L^\vee\arrow[r]\arrow[d,"\sim"']\&amp;0\\ 0\arrow[r,dash]\&amp;\underline{\mathcal O}\arrow[r,hook]\&amp;\underset{\substack{\simeq\\\underbrace{E^\vee}_{E\otimes L^\vee}\otimes E}}{\underline{\mathrm{End}}(E)}\arrow[r,dash]\&amp;\underline{\mathrm{End}}(E)/\underline{\mathcal O}\arrow[r,dash]\&amp;0, \end{tikzcd}}</code>.
- foot, vertical identification — <code>\diagram{\begin{tikzcd}[ampersand replacement=\&amp;] \mathrm{Sym}^2(E)\otimes L^\vee\simeq\mathrm{Quad}(E)\otimes L\quad(\simeq\mathrm{Quad}(E,L))\arrow[d,"\sim"']\\ \underline{\mathrm{End}}(E)/\mathcal O \end{tikzcd}} % archive sheet number: 13</code>.

**Alterations, additions, marginal writing and underlining**

- top, continuation of 2.2 — <code>\deleted{et de plus}</code>.
- upper third, twisted sequence — <code>\underline{\mathcal O}</code>.
- upper third, twisted sequence — <code>\underline{\mathrm{End}}</code>.
- middle, identification of scalars — <code>\underline{\mathcal O}</code>.
- middle, identification of scalars — <code>\underline{\mathcal O}</code>.
- middle, identification of scalars — <code>\underline{\mathrm{End}}</code>.
- middle, identification of scalars — <code>\inserted{un diagramme}</code>.
- middle, identification of scalars — <code>\deleted{de \unsure{du}}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathcal O}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathcal O}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathcal O}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathrm{End}}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathrm{End}}</code>.
- middle to lower third, comparison of the two rows — <code>\underline{\mathcal O}</code>.
- foot, vertical identification — <code>\underline{\mathrm{End}}</code>.

**Changes**

- <code>E\otimes E\longrightarrow\mathrm{Sym}^2(E)\mathrel{-}0</code> -> <code>E\otimes E\mathrel{\unsure{-|\longrightarrow}}\mathrm{Sym}^2(E)\mathrel{-}0</code>
- <code>\overset{\mathrm{dfn}}=</code> -> <code>\overset{\unsure{\mathrm{déf}|\mathrm{dfn}}}=</code>
- <code>\deleted{et \unsure{de plus}}</code> -> <code>\deleted{et de plus}</code>

## Scan 015

2026-11-18T03:29:17Z to 2026-11-18T03:30:06Z (UTC).

**Reading from the three crops before reopening the page file**

« On en conclut », « loc. libre de rang 2 », « correspondent can. », « loc. monogènes », another « loc. libres de rang 3 » above the quotient; « structures de similitudes strictement fidèles », « sous-fibrés vectoriels », « fibré vect. de rang 4 », « qui contiennent le sous-fibré ». « Lemme 1 », « qui contient », « Conditions équivalentes », « est monogène », « ∃ loc. une section u … t.q. », « est engendré loc. par deux sections ». In the slanted margin « résulte de l'équation de H.C. ». In the packed conclusion « la loi d'algèbre », « un faisceau d'anneaux comm. », « ou plutôt », « en question », « ceci … que », « sous-algèbres commutatives », « str. fidèles », « locᵗ », with a cancelled « loc. définis par u ».

**Comparison against the transcription**

The long bent line at the top leads from du to the words about the module of rank three, ahead of End(E)/O; the shorter, similar line in the next paragraph introduces the rank-four bundle. The mark following can is level and isolated. The left slanted note, rotated roughly 53 degrees, reads H.C. with two actual stops followed by the quadratic equation. The first identity is subscripted E; no i or j index. The light line under Lemme 1 is an underline. The overwritten word after « par » and the discarded expression before « tels que » are cancellations. The intervening words between « Ainsi » and « correspondent » are cramped between two longer baselines and several leaders; their order and some letters remain uncertain. The A with the looped lower-left return is calligraphic here; the underlined O in the conditions contrasts with the bare O in the quotient at the top.

**Formulae in reading order**

- top, conclusion with insertions interlined — <code>$E$</code>, <code>$\underline{\mathrm{End}}(E)/\mathcal O$</code>, <code>$\mathcal A$</code>, <code>$\underline{\mathrm{End}}(E)$</code>.
- upper middle, two conditions — <code>\[ \begin{aligned} 1^\circ)&amp;\quad\mathcal A\supset\underline{\mathcal O}\cdot1_E\\ 2^\circ)&amp;\quad\mathcal A/\underline{\mathcal O}\unsure{/|\cdot}1_E \text{ soit loc. monogène.} \end{aligned} \]</code>.
- middle, strict structures — <code>$\underline{\mathrm{End}}(E)$</code>, <code>$\underline{\mathcal O}\cdot1_E$</code>.
- lower middle, underlined heading — <code>$\mathcal A$</code>, <code>$\underline{\mathrm{End}}(E)$</code>, <code>$\underline{\mathcal O}\cdot1_E$</code>.
- bottom third, indented a and a prime — <code>$\mathcal A/\underline{\mathcal O}1_E$</code>, <code>$'$</code>, <code>$\exists$</code>, <code>$u$</code>, <code>$\mathcal A$</code>, <code>$\mathcal A=\underline{\mathcal O}\cdot1_E+\underline{\mathcal O}\cdot u$</code>.
- bottom third, indented b — <code>$\mathcal A$</code>.
- slanted left of lemma — <code>$u^2-\mathrm{Tr}(u)\,u+N(u)=0$</code>.
- lower, algebra paragraph and conclusion — <code>$\mathcal A$</code>, <code>$\underline{\mathrm{End}}(E)$</code>, <code>$A$</code>.
- foot, bracketed correspondence — <code>$E$</code>, <code>$\underline{\mathrm{End}}(E)$</code>, <code>$\deleted{\mathcal A}\mathcal A_u$</code>, <code>$u$</code>, <code>$u$</code>.

**Alterations, additions, marginal writing and underlining**

- top, conclusion with insertions interlined — <code>\uline{les structures de similitude}</code>.
- top, conclusion with insertions interlined — <code>\inserted{Module (loc. libre de rang 3)}</code>.
- top, conclusion with insertions interlined — <code>\underline{\mathrm{End}}</code>.
- top, conclusion with insertions interlined — <code>\underline{\mathrm{End}}</code>.
- upper middle, two conditions — <code>\underline{\mathcal O}</code>.
- upper middle, two conditions — <code>\underline{\mathcal O}</code>.
- middle, strict structures — <code>\inserted{fibré vect. de rang 4}</code>.
- middle, strict structures — <code>\underline{\mathrm{End}}</code>.
- middle, strict structures — <code>\underline{\mathcal O}</code>.
- lower middle, underlined heading — <code>\uline{Lemme 1}</code>.
- lower middle, underlined heading — <code>\underline{\mathrm{End}}</code>.
- lower middle, underlined heading — <code>\underline{\mathcal O}</code>.
- bottom third, indented a and a prime — <code>\underline{\mathcal O}</code>.
- bottom third, indented a and a prime — <code>\underline{\mathcal O}</code>.
- bottom third, indented a and a prime — <code>\underline{\mathcal O}</code>.
- slanted left of lemma — <code>\margin{résulte de l'équation de H.C. $u^2-\mathrm{Tr}(u)\,u+N(u)=0$}</code>.
- lower, algebra paragraph and conclusion — <code>\deleted{\unsure{la}}</code>.
- lower, algebra paragraph and conclusion — <code>\underline{\mathrm{End}}</code>.
- lower, algebra paragraph and conclusion — <code>\inserted{(op. ou plutôt, \unsure{A de plus})}</code>.
- lower, algebra paragraph and conclusion — <code>\deleted{ainsi}</code>.
- foot, bracketed correspondence — <code>\inserted{structures de}</code>.
- foot, bracketed correspondence — <code>\inserted{commutatives}</code>.
- foot, bracketed correspondence — <code>\underline{\mathrm{End}}</code>.
- foot, bracketed correspondence — <code>\deleted{\mathcal A}</code>.
- foot, bracketed correspondence — <code>\deleted{loc. définis par $u$}</code>.

**Changes**

- <code>de \unsure{rg|rang} 2</code> -> <code>de rang 2</code>
- <code>can\textsuperscript{\unsure{t}}</code> -> <code>can.</code>
- <code>aux sous-\deleted{Modules} local. monogènes de $\underline{\mathrm{End}}(E)/\mathcal O$, \inserted{Modules (loc. libres de rang 3)}</code> -> <code>aux sous-\unsure{Modules} loc. monogènes du \inserted{Module (loc. libre de rang 3)} $\underline{\mathrm{End}}(E)/\mathcal O$,</code>
- <code>\unsure{H.C.|H. C.}</code> -> <code>H.C.</code>
- <code>qui contienne $\underline</code> -> <code>qui contient $\underline</code>
- <code>Un tel $A$</code> -> <code>Un tel $\mathcal A$</code>
- <code>aux $\deleted{A} A_u$</code> -> <code>aux $\deleted{\mathcal A}\mathcal A_u$</code>

## Scan 016

2026-11-18T03:30:06Z to 2026-11-18T03:30:52Z (UTC).

**Reading from the three crops before reopening the page file**

« un scalaire sur aucune fibre résiduelle », « est appelé l'anneau des homothéties (sous-entendu : directes) », « envisagée », « on le note », « Lemme 2 », « Anneau des homothéties », « Conditions équivalentes », « strictement fidèle », « est de rang 2 », « injectif pour tout … », « sous-fibré vectoriel », « n'est pas un scalaire », « inversible », « loc. libre de rang 1 », « monogène », « pour la structure régulière gauche », « engendré par 2 élémᵗˢ ». In the corollary « Sous ces conditions, soit … », « loc. lib. » crossed, « inv. de », « On aura donc un iso. can. », « où », « d'où ». Exponent over the exterior power by the right edge looks a little like 7.

**Comparison against the transcription**

The downward loop to the right of d) looks like g with a stop; the preceding small strokes allow à or a semicolon. In d′ the word before « engendré » appears to contain a question-like stroke; the uncertainty is retained. The b′ definition has u as a subscript and a definition abbreviation above its equals, while 1 has a subscript E. No indexed i or j. A of the ring has a loop, the open E in d) is visually different from the E in End. Sigma is the uneven zigzag with a separate top stroke. The rule over condition b) is a leader, and « loc. libre de … » in c) and the former opening of Cor. 1 are actually struck. The dual marks switch sides between the final two lines and the last power of L in the second line is unmarked.

**Formulae in reading order**

- upper, underlined name — <code>$A$</code>, <code>$\Sigma$</code>, <code>$\mathcal A_\Sigma$</code>.
- first third, lemma heading and insertion — <code>$\Sigma$</code>, <code>$E$</code>, <code>$\mathcal A_\Sigma$</code>, <code>$\subset\underline{\mathrm{End}}(E)$</code>.
- a and b — <code>$\deleted{\unsure{\Sigma|\Sigma_u}}\Sigma$</code>, <code>$\mathcal A(s)$</code>, <code>$\mathcal A(\deleted{\unsure{x}}s)\unsure{-|\to}\underline{\mathrm{End}}(E(s))$</code>, <code>$s\in X$</code>, <code>$\mathcal A$</code>, <code>$\underline{\mathrm{End}}(E)$</code>.
- middle b prime — <code>$'$</code>, <code>$\mathcal A=\mathcal A_u\overset{\mathrm{déf}}{=}\underline{\mathcal O}\cdot1_E+\underline{\mathcal O}\cdot u$</code>, <code>$\forall s\in X$</code>, <code>$u(s)\in\underline{\mathrm{End}}(E(s))$</code>.
- c and c prime — <code>$E$</code>, <code>$\mathcal A$</code>, <code>$'$</code>, <code>$E$</code>, <code>$\mathcal A$</code>.
- d and d prime — <code>$\mathcal E=\underline{\mathrm{End}}(E)$</code>, <code>$\mathcal A$</code>, <code>$'$</code>, <code>$\mathcal E$</code>, <code>$\mathcal A$</code>.
- lower third, corollary with replaced clause — <code>$x\in\Gamma E$</code>, <code>$x$</code>, <code>$\Delta\subset\underline{\mathrm{Quad}}(E)$</code>, <code>$\underline{\mathrm{Quad}}(E)$</code>, <code>$\Sigma=\Sigma_\Delta$</code>.
- foot, two lines — <code>\[ \begin{aligned} &amp;\Delta\simeq(\mathcal A/\mathcal O)\otimes L^\vee &amp;&amp;(\text{où } L=\Lambda^{\unsure{2|7}}E=\det E)\\ \text{d'où}\qquad&amp;\Delta^\vee\simeq(\mathcal A/\mathcal O)^\vee\otimes L&amp;&amp;, \end{aligned} \]</code>.

**Alterations, additions, marginal writing and underlining**

- upper, underlined name — <code>\uline{homothéties}</code>.
- upper, underlined name — <code>\inserted{sous-entendu :}</code>.
- upper, underlined name — <code>\uline{directes}</code>.
- upper, underlined name — <code>\deleted{\unsure{de}}</code>.
- first third, lemma heading and insertion — <code>\uline{Lemme 2}</code>.
- first third, lemma heading and insertion — <code>\inserted{$\subset\underline{\mathrm{End}}(E)$}</code>.
- first third, lemma heading and insertion — <code>\underline{\mathrm{End}}</code>.
- a and b — <code>\deleted{\unsure{\Sigma|\Sigma_u}}</code>.
- a and b — <code>\inserted{$\mathcal A(s)$ est de rang 2 et}</code>.
- a and b — <code>\deleted{\unsure{x}}</code>.
- a and b — <code>\underline{\mathrm{End}}</code>.
- a and b — <code>\underline{\mathrm{End}}</code>.
- middle b prime — <code>\underline{\mathcal O}</code>.
- middle b prime — <code>\underline{\mathcal O}</code>.
- middle b prime — <code>\underline{\mathrm{End}}</code>.
- c and c prime — <code>\deleted{loc. libre de \unsure{rg}}</code>.
- c and c prime — <code>\inserted{inversible}</code>.
- c and c prime — <code>\inserted{loc. \deleted{\unsure{mon}}}</code>.
- c and c prime — <code>\deleted{\unsure{mon}}</code>.
- d and d prime — <code>\underline{\mathrm{End}}</code>.
- lower third, corollary with replaced clause — <code>\uline{Cor. 1}</code>.
- lower third, corollary with replaced clause — <code>\deleted{$x\in\Gamma E$, alors $x$ est}</code>.
- lower third, corollary with replaced clause — <code>\inserted{$\Delta\subset\underline{\mathrm{Quad}}(E)$}</code>.
- lower third, corollary with replaced clause — <code>\underline{\mathrm{Quad}}</code>.
- lower third, corollary with replaced clause — <code>\deleted{loc. lib.}</code>.
- lower third, corollary with replaced clause — <code>\underline{\mathrm{Quad}}</code>.

**Changes**

- <code>$\mathcal A$-Module ; \unsure{cf.}</code> -> <code>$\mathcal A$-Module \unsure{à|;} g.</code>
- <code>On aura donc un isom. can.</code> -> <code>On aura donc un iso. can.</code>

## Scan 017

2026-11-18T03:30:53Z to 2026-11-18T03:31:37Z (UTC).

**Reading from the three crops before reopening the page file**

Top continuation « et une … forme quadratique de définition de la structure … de similitude »; struck « Ceci posé, soit ». « Plus généralement, soit Δ′ un Module inversible », « un hom de Modules », « d'où une structure de similitudes », « correspond. à un sous-anneau », « Soit x une section de E. Conditions équivalentes ». « générateur », « épi », « est une base … comme … Module », « est un iso », « inversible » (underlined). Crossed « Cor 2 Soit Q ». Last lines « Si u est un gén. loc. de l'Alg. », crossed « tout », « non vect. propre » (underlined). Dots, primes and the two forms of Δ at top are distinct.

**Comparison against the transcription**

The triangular glyph carries both a prime and a short open vee on the second display; both belong to Δ. In the first display, the final vee is on L in the parenthesis, and the expression is preserved even though the preceding scan gave another dual formula. The definition abbreviation is above =. The relation between the two A's has a downward hook under the second of the two horizontal strokes. In c) Q(s) has no extra x inside it. At a) and a′) the interlinear arrows label the maps A→E; the earlier Q(x) is struck at a′). The three final lines read « non vect. propre », with two separate underlines. No indexed i or j. The large Q has a closed oval, unlike the narrow zigzag of Σ or the open loop on A; none of them is double-struck.

**Formulae in reading order**

- top, first map — <code>\[ Q_\Sigma:E\longrightarrow\Delta^\vee\overset{\mathrm{déf}}{=}\Delta' \;(\simeq\mathcal A/\mathcal O\otimes L^\vee) \]</code>.
- struck start and replacement below — <code>$\Delta'$</code>.
- upper middle, map and parenthesis — <code>\[ Q:E\longrightarrow\Delta'\qquad(\text{i.e. }\Delta^{\prime\vee}\longrightarrow\underline{\mathrm{Quad}}(E)\quad\text{un hom. de Modules}) \]</code>.
- middle, structure and algebra — <code>$\Sigma=\Sigma_Q$</code>, <code>$E$</code>, <code>$\mathcal A\unsure{=|\supset}\mathcal A_\Sigma$</code>, <code>$\underline{\mathrm{End}}(E)$</code>.
- middle, generator and base — <code>$x$</code>, <code>$E$</code>, <code>$\{x\}$</code>, <code>$E$</code>, <code>$\mathcal A$</code>, <code>$\lambda\mapsto\lambda\cdot x$</code>, <code>$\mathcal A\longrightarrow\deleted{\unsure{\mathcal A}}E$</code>, <code>$'$</code>, <code>$Q(x)$</code>, <code>$\{x\}$</code>, <code>$E$</code>, <code>$\mathcal A$</code>, <code>$u\mapsto u\cdot x$</code>, <code>$\mathcal A\longrightarrow E$</code>.
- lower third b and b prime — <code>$\{Q(x)\}$</code>, <code>$\deleted{\unsure{E|L}}\Delta'$</code>, <code>$'$</code>, <code>$\Delta'=\underline{\mathcal O}$</code>, <code>$Q(\unsure{u|x})\in\Gamma\underline{\mathcal O}_X$</code>.
- foot c and cancelled heading — <code>$\forall s\in X$</code>, <code>$Q(s)\ne0$</code>, <code>$Q$</code>.
- foot d — <code>$u$</code>, <code>$\mathcal A$</code>, <code>$s\in X$</code>, <code>$x(s)\in E(s)$</code>, <code>$u(s)\in\mathrm{End}\,E(s)$</code>.

**Alterations, additions, marginal writing and underlining**

- top continuation — <code>\deleted{\unsure{ho.}}</code>.
- top continuation — <code>\deleted{quadratique}</code>.
- top continuation — <code>\inserted{de}</code>.
- struck start and replacement below — <code>\deleted{Ceci posé, soit}</code>.
- upper middle, map and parenthesis — <code>\underline{\mathrm{Quad}}</code>.
- middle, structure and algebra — <code>\underline{\mathrm{End}}</code>.
- middle, generator and base — <code>\inserted{$\lambda\mapsto\lambda\cdot x$,}</code>.
- middle, generator and base — <code>\deleted{\unsure{\mathcal A}}</code>.
- middle, generator and base — <code>\deleted{$Q(x)$ \unsure{es}}</code>.
- middle, generator and base — <code>\inserted{$u\mapsto u\cdot x$:}</code>.
- lower third b and b prime — <code>\deleted{\unsure{E|L}}</code>.
- lower third b and b prime — <code>\underline{\mathcal O}</code>.
- lower third b and b prime — <code>\underline{\mathcal O}</code>.
- lower third b and b prime — <code>\uline{inversible}</code>.
- foot c and cancelled heading — <code>\deleted{\uline{Cor. 2} Soit $Q$}</code>.
- foot c and cancelled heading — <code>\uline{Cor. 2}</code>.
- foot d — <code>\deleted{tout}</code>.
- foot d — <code>\uline{non vect.}</code>.
- foot d — <code>\uline{propre}</code>.

**Changes**

- <code>\Delta'^\vee</code> -> <code>\Delta^{\prime\vee}</code>
- <code>correspond\textsuperscript{\unsure{t}}</code> -> <code>\unsure{correspond.|correspond\textsuperscript{t}}</code>

## Scan 018

2026-11-18T03:31:38Z to 2026-11-18T03:32:46Z (UTC).

**Reading from the three crops before reopening the page file**

§2.3 « Considérons à nouveau l'iso. can. », « Soit u une section … i.e. un endom. de E », crossed « considér… », « son image est donc une forme quadratique … à valeurs dans L », « Je dis qu'on a ». Parenthesis « il faut vérifier le signe ! », struck « mais » and « C'est », then « On revérifie directement par des coordonnées ». In the bracket « NB. Si », « alors », « est id. nul en λ, μ ssi … i.e. », « avec … arbitraire », « parmi lesquels », « On a » and crossed « alors ». The first superscript on λ in the final polynomial is steeply hooked. There is an opaque change before the term in b, and multiple earlier marks in the little scalar matrix.

**Comparison against the transcription**

Traced the boxed wedge from left to right: its first argument is u(x) and its second x. The unreadable former sign and the live horizontal-looking sign before bμ² remain marked; the minus on the upper-right entry of each of the two later matrices is much clearer. The low index of u on the penultimate matrix is a and that on the last matrix a rounded 0. Q has subscript u; id has subscript E, and neither contains an indexed i or j. The two large square-bracket strokes enclose the NB as a whole. The long upper and lower strokes around the wedge make a box rather than a cancellation. The heading has no double-struck capital, the first End and Quad are underlined, and the final Quad in parentheses is plain.

**Formulae in reading order**

- first line of mathematics — <code>\[ \underline{\mathrm{End}}(E)/\underline{\mathcal O}\cdot1_E\simeq\underline{\mathrm{Quad}}(E)\otimes\underline L\;(\simeq\mathrm{Quad}(E,L)) \]</code>.
- first third, definition — <code>$u$</code>, <code>$\underline{\mathrm{End}}(E)$</code>, <code>$E$</code>, <code>$Q_u$</code>, <code>$L$</code>.
- boxed formula — <code>\[ \boxed{Q_u(x)=u(x)\wedge x} \]</code>.
- middle, two-way implication — <code>\[ Q_u=0\quad\Longleftrightarrow\quad u\in\Gamma\underline{\mathcal O}\cdot\mathrm{id}_E \]</code>.
- matrix — <code>\[ u=\begin{pmatrix}a&amp;b\\c&amp;d\end{pmatrix} \]</code>.
- coordinate expression, overwritten sign — <code>\[ Q_u(\lambda,\mu)=c\lambda^2+(d-a)\lambda\mu\deleted{\unsure{+|-}}\unsure{-|+}b\mu^2 \]</code>.
- condition below, diagonal matrix heavily overwritten — <code>$\lambda,\mu$</code>, <code>$b=c=0$</code>, <code>$d=a$</code>, <code>$u=\deleted{\unsure{a}}\begin{pmatrix}a&amp;\deleted{\unsure{c|a}}0\\0&amp;a\end{pmatrix}\deleted{\unsure{=a}}=a\,\mathrm{id}_E$</code>.
- lower third — <code>$Q=\alpha\lambda^{\unsure{2|7}}+\beta\lambda\mu+\gamma\mu^2$</code>, <code>$u$</code>, <code>$Q_u=Q$</code>.
- bottom, family of matrices — <code>\[ u_a=\begin{pmatrix}a&amp;-\gamma\\\alpha&amp;a+\beta\end{pmatrix},\quad\text{avec }a\in\Gamma\underline{\mathcal O}\text{ arbitraire} \]</code>.
- foot of bracket — <code>\[ u_0=\begin{pmatrix}0&amp;-\gamma\\\alpha&amp;\beta\end{pmatrix}\qquad\ldots\qquad] \]</code>.

**Alterations, additions, marginal writing and underlining**

- first line of mathematics — <code>\underline{\mathrm{End}}</code>.
- first line of mathematics — <code>\underline{\mathcal O}</code>.
- first line of mathematics — <code>\underline{\mathrm{Quad}}</code>.
- first third, definition — <code>\underline{\mathrm{End}}</code>.
- first third, definition — <code>\deleted{considér\unsure{ons}}</code>.
- beneath box, open sign question — <code>\deleted{mais}</code>.
- beneath box, open sign question — <code>\deleted{C'est}</code>.
- middle, two-way implication — <code>\underline{\mathcal O}</code>.
- coordinate expression, overwritten sign — <code>\deleted{\unsure{+|-}}</code>.
- condition below, diagonal matrix heavily overwritten — <code>\deleted{qui}</code>.
- condition below, diagonal matrix heavily overwritten — <code>\deleted{\unsure{a}}</code>.
- condition below, diagonal matrix heavily overwritten — <code>\deleted{\unsure{c|a}}</code>.
- condition below, diagonal matrix heavily overwritten — <code>\deleted{\unsure{=a}}</code>.
- bottom, family of matrices — <code>\underline{\mathcal O}</code>.
- last line, at edge — <code>\deleted{alors}</code>.

**Changes**

No change.
