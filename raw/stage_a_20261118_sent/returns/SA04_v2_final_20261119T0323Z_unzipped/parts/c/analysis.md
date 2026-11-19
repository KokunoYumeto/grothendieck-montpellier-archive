# SA04, part C: source audit and mathematical verification

Audit date: 19 November 2026. Author: GPT-6 Astra Pro, inherited effort, run `notes_93_98`. Source paths below are relative to the supplied `source/` directory. All 99 indexed entries of `MPL_93_221-236+161-5` and all eight indexed sections of `MPL_98` were read with the corresponding transcription passages. The eight sections contain 89 nested notes, which receive separate items. The eight indexed rows point to composite parent items; the nested records retain their parent's stable source id. The tables are authored judgments serialized by `programs/c_build.py`, not verdicts inferred from headings.

## 1. What the physical sequences contain

`SA04_texts/pro/MPL_93_221-236+161-5_transcription.tex` has three distinct handwritten sequences in cote 93: periods and Picard–Fuchs operators, scans 221–230, lines 2–223; formal exactness and differential operators, scans 231–233, lines 224–315; and comparison of square-zero lifts using torsors and homotopies, scans 234–236, lines 316–461. Its next cote marker introduces **cote 161-5**, scans 3–29, lines 463–1552. That is a separate archival object, not cote 93 scans 161–165.

The first cote 161-5 object is Serre's printed *Sur les groupes de Galois attachés aux groupes p-divisibles*, written in December 1966 and published in the 1967 *Local Fields* proceedings, pp. 118–131. The introduction explicitly credits Grothendieck's suggestion to use algebraic groups in connection with motives. That acknowledgment does not change the authorship of the printed propositions. The second printed object has an Annuaire cover for 1968–1969 and a course report concerning 1967–1968. Marginal references to Sen and possibly Springer's 1973 book can be later annotations; they do not date every handwritten sheet. The final handwritten comparison-data and nonabelian-cohomology sequence is treated separately from both printed reports. [Serre1967, Serre1979, Springer1973; source lines 463–498, 978–1113.]

`SA04_texts/pro/MPL_98_transcription.tex` contains 43 scans, numbered 2–44: two covers, four reused topology typescripts, six reused abelian-variety typescripts, and 31 handwritten faces. The scan count was rerun in `c_computations.py`. The handwritten sequences concern determinant norms, cohomology of group-set sites, and bounded coherent families with Tor and Ext base change. Neither the author of the reused typescripts nor the author of their pencil marks can be identified from these supplied sheets. Number 329 and number 268 distinguish the two typescript series; resemblance to a published textbook is not an attribution. The covers “SGA 4 XVII” and “SGA 6 XIII” indicate subjects but do not establish a common date for the stack.

The current MPL98 notes are already careful corrections of some contextual Hua98 assertions. In particular, **input flatness is present** in the Tor lemma; **bounded kernels and extensions are already named**; and the Ext argument's **all-degrees statement concerns a finite complex**, whereas its identification with Ext is restricted to the requested range. These are not fresh omissions discovered in the current Pro notes. The unavailable research packets, purported Lean proofs, and project-status labels are provenance only.

## 2. Periods, boundary terms, and formal operators

### 2.1 Logarithmic derivative and characteristic zero

For a matrix-valued map $g$, the left logarithmic derivative is $\theta=g^{-1}dg$. Differentiating $g^{-1}g=1$ gives $d(g^{-1})=-g^{-1}(dg)g^{-1}$, hence $d\theta=-\theta\wedge\theta$, or $d\theta+\frac12[\theta,\theta]=0$ in bracket notation. For a commutative group the bracket vanishes, so the form is closed. The right convention changes the sign of the bracket. This checks C-SA04-401, but cannot show whether a commutativity assumption stood on the missing preceding page. Michor's author draft §4.26 supplies an opened comparator for conventions. [Source cote 93/221, lines 10–26; Michor2006.]

Formal de Rham exactness over a characteristic-zero coefficient algebra is substantive. In a formal coordinate algebra over a $\mathbf Q$-algebra, split a differential form into homogeneous pieces by total degree, counting a $dx_i$ as degree one. Contraction with the Euler vector field obeys $d\iota_E+\iota_Ed=r$ on positive total degree $r$. Division by $r$ contracts every positive-degree piece, continuously in the adic topology. In characteristic $p$, $x^{p-1}dx$ has no formal primitive: the coefficient equation would be $p a_p=1$. The saved `CHAR_P_PRIMITIVE` calculation records precisely that obstruction; it is not evidence against a crystalline or divided-power Poincaré lemma with different objects. [SA04-406; C-SA04-414; cote 93/221 and 231.]

### 2.2 Holomorphic path integrals and the open-arc error

Under the source's local smooth holomorphic-family hypotheses, a relatively closed one-form has local primitives along finitely many coordinate neighbourhoods covering a chosen path. Differences of adjacent primitives are constant on connected fibre overlaps. Evaluating at holomorphic endpoint sections therefore gives a local holomorphic integral for a continuously transported path class. Changing the class adds a closed-cycle period. This is a local construction and makes no assertion of a single-valued global primitive. Concatenation gives

$$
I(a,c)=I(a,b)+I(b,c).
$$

A linear differential operator annihilating all period functions removes the ambiguity between different path choices. Applying it to this identity gives the additive endpoint cocycle in C-SA04-403. [Cote 93/222–223, lines 31–75.]

The claim at scan 227, lines 153–161, that an annihilating operator makes an integral over an **open horizontal arc** vanish is too strong. Take $X=\mathbf A^1_x\times S$, with the product connection, $\omega=dx$, and the constant sections $a=0,b=1$. The relative de Rham class is zero, so the order-zero operator $D=1$ belongs to its annihilator; both endpoints are horizontal. Nevertheless, the integral is one. Every stated local smoothness, closedness and horizontality condition holds. The valid conclusion for an exact differential is its endpoint difference; a closed cycle has zero boundary. `PERIOD_OPEN_ARC` certifies this example. C-SA04-406 is refuted, with C-SA04-407 and C-SA04-410 giving the corrected period/endpoint statements.

For a differentiable family of forms and paths on a local differentiable trivialization, differentiate the pulled-back form on the path interval. Cartan's formula gives

$$
\frac d{ds}\int_{\gamma_s}\omega_s
=\int_{\gamma_s}(\partial_s\omega_s+\iota_v d\omega_s)
 +[\iota_v\omega_s]_{a_s}^{b_s}.
$$

The derivative of pullback is $\partial_s+\mathcal L_v$, and Stokes converts $d\iota_v\omega_s$ into the two endpoint values, which proves the displayed formula. The exact test $\omega_t=t x\,dx$, $a_t=t,b_t=2t$, gives $9t^2/2$ on both sides; `MOVING_ENDPOINTS` separately prints the interior and boundary contributions. The general derivation is this argument, not an inference from one polynomial example. The source begins but does not finish this moving-endpoint calculation. [Cote 93/229–230, lines 187–223; C-SA04-410.]

The suggested simultaneous choice of a horizontal lift along two sections also needs a qualification at intersections. In $X=\mathbf A^1_x\times\mathbf A^1_s$, let $a(s)=0$ and $b(s)=s$. A lift of $\partial_s$ is $\partial_s+u(s,x)\partial_x$. Tangency to $a$ forces $u(0,0)=0$, whereas tangency to $b$ forces $u(0,0)=1$. Thus the arbitrary-intersecting-sections assertion fails. This is the `INTERSECTING_HORIZONTAL` check for C-SA04-409, not an obstruction to making disjoint local sections horizontal.

The deleted implication on scan 230 is separately false: with base coordinates $s,t$, fibre coordinate $x$, and $\omega=s\,dx$, relative closedness holds. Pullback by the section $x=t$ is $s\,dt$, whose absolute differential is $ds\wedge dt\ne0$. `RELATIVE_NOT_ABSOLUTE_CLOSED` verifies it. The deletion means that C-SA04-411 is **corrected in the source**, not a surviving error.

### 2.3 What Gauss–Manin literature does and does not settle

Katz–Oda, §2 Theorem 1 and §3, constructs the integrable connection on relative de Rham **hypercohomology** for a smooth morphism between smooth schemes over a field and compares it with the explicit construction. The paper records Mumford's 1966–1967 seminar and was communicated on 19 April 1968; its publication is 1968. No priority date is assigned to the undated manuscript. The naive quotient $f_*Z^1/d(f_*\mathcal O)$ represents that cohomology only when the missing higher-direct-image contribution vanishes. The source's Stein annotation at scan 224, line 82, is relevant. Fibrewise vanishing likewise needs the correct base-change comparison and suitable relative cohomology; over a reduced smooth base a locally free sheaf section vanishing in every fibre is zero. Reducedness cannot be dropped in an unrelated scheme generalization. [C-SA04-404–408; KatzOda1968; EGAIII2 §7.7.]

Katz1970, Theorem 10.0, applies to the paper's arithmetic base, a smooth proper family, and the stated local-freeness conditions on Hodge/de Rham direct images. It yields **global nilpotence**, with the theorem's bounded exponent. It does not assert zero $p$-curvature. Theorem 14.1 supplies regularity and quasi-unipotence in its complex-curve setting. The archive's arbitrary analytic period discussion does not by itself supply such an arithmetic model. Thus SA04-495 and C-SA04-463 are a conditional published comparison, not an extra manuscript theorem.

### 2.4 Formal exactness, principal parts, and the questioned injection

Cote 93/231 writes two finite-order operator sequences, in opposite variances and with different order shifts, using an undefined “formally exact” premise. EGA IV4, Proposition 16.8.4, proves the principal-parts representation of differential operators; Theorem 16.11.2 gives the local divided-differential basis under differential smoothness and a differential-coordinate basis. These exact sections were read in the downloaded primary PDF. They do not identify the manuscript's unexplained formal-exactness definition, especially the assertion for every auxiliary module in the contravariant sequence. Searches of EGA terminology and Spencer comparators did not locate an exact theorem with all those quantifiers. C-SA04-412–413 and 418 therefore retain a genuine identification limit, class F, instead of receiving an imagined proof.

One questioned consequence **does** have a short conditional proof. Let $d_0:E\to E\otimes\Omega^1$ and $d_1:E\otimes\Omega^1\to E\otimes\Omega^2$. Assuming the source's preceding quotient presentation, write $D=\Delta d_0\in\operatorname{Diff}_+$ and send it to $\Delta|_{\ker d_1}$. Changing $\Delta$ by $B d_1$ does not change that restriction. If the restriction is zero, then $D=0$, since $\operatorname{im}d_0\subset\ker d_1$. This proves C-SA04-415 under the stated presentation; it does not prove formal exactness itself. [Scan 232, lines 265–287.]

Likewise, an operator represented by an $\mathcal O$-linear map $P^i(E)\to F$ kills the specified horizontal generators exactly when it kills their $\mathcal O$-span. It therefore factors uniquely through $P^i(E)/\mathcal O\delta_i(E)$. For $M=E/N$, the same argument uses $\rho_i:E\to P^i(M)$ and gives $\Phi_i=P^i(M)/\mathcal O\rho_i(E)$. This is the ordinary universal property of a quotient, with the chosen left module structure. It proves C-SA04-416. [Scans 232–233, lines 279–306; EGAIV4 §16.8.4.]

The next assertion is distinct: the $\Phi_i$ form a strict projective system, determined by $M$ and $\rho_\infty$. The canonical transition $P^i(M)\to P^{i-1}(M)$ is surjective and sends $\rho_i(E)$ onto $\rho_{i-1}(E)$. It therefore induces a surjection $\Phi_i\to\Phi_{i-1}$. The compatible map $\rho_\infty$ determines each finite-order image and hence every quotient and transition. This proves C-SA04-417, which is expressly stated at scan 233, lines 308–312. It does not assert the converse integrability characterization: the source's next line 313 leaves additional conditions unspecified, and that separate issue remains C-SA04-418.

## 3. Square-zero lifts and the additive torsor roof

### 3.1 The actual first-order mechanism

Let $S_0\hookrightarrow S$ be defined by a square-zero ideal $I$, and let two smooth $S$-lifts of a fixed $S_0$-scheme be compared locally. Smoothness gives local lift maps; the difference of two such maps is an $S$-derivation into $I\mathcal O$. Conversely, adding a derivation to a lift preserves multiplication because all quadratic error terms lie in $I^2=0$. Thus the local comparison maps form an additive torsor where they exist. This is the exact scope of C-SA04-419; Stacks 17.28.11 checks the derivation identity. [Cote 93/234, lines 318–344.]

For a relative derivation $D$ with values in the base ideal, contraction satisfies $\mathcal L_D=d\iota_D+\iota_Dd$. The relative differential kills coefficients pulled from $I\subset\mathcal O_S$; two first-order error terms multiply to zero. Hence the pullbacks under two maps differing by $D$ differ by this chain homotopy. Addition of $D$'s adds the homotopies, and a second contraction has image in $I^2$, so it vanishes in this setting. The exact polynomial calculation `CARTAN_FIRST_ORDER` checks the sign and the pullback difference for a concrete vector field and form. The displayed derivation proof supplies the universal argument. **Cartan contraction** is the construction here; the characteristic-$p$ Cartier isomorphism is a different statement. [SA04-435,494; C-SA04-420; scan 234, lines 346–373.]

### 3.2 A completely specified reconstruction of scans 235–236

The source alternates multiplicative and additive expressions and contains type conflicts in $u,v,h,k$. The following is explicitly **our additive repair**. Let $P$ be a torsor under an abelian sheaf $G$, and let $K',K''$ be complexes of modules on a ringed site. Put $H=\underline{\operatorname{Hom}}^\bullet(K',K'')$, with differential

$$
d_H(f)=d_{K''}f-(-1)^{\deg f}f d_{K'}.
$$

Assume given $u:P\to Z^0H$ and an additive map $k:G\to H^{-1}$ such that

$$
u(p+g)-u(p)=d_Hk(g).
$$

The torsor defines an extension of abelian sheaves $0\to G\to\bar G\to\mathbf Z\to0$, whose fibre over one is $P$. It can be constructed from the free abelian sheaf on $P$, imposing $ [p+g]-[p]=g$. A local choice $p_0\in P$ identifies $\bar G\simeq G\oplus\mathbf Z$. Define $L=[G\to\bar G]$ in degrees **−1,0**, with augmentation $L\to\mathbf Z[0]$. Extend $u$ to $U:\bar G\to H^0$ by $U(g)=d_Hk(g)$. The assumed identity makes this well defined, and $k,U$ form a chain map $L\to H$.

Tensoring over $\mathbf Z$ with the structure sheaf gives $L_{\mathcal O}\to\mathcal O[0]$. Locally this is the direct sum of the identity on the unit and the contractible complex $G\xrightarrow{1}G$, tensored with $\mathcal O$. Consequently, for **any** $K'$, including an unbounded complex,

$$
L_{\mathcal O}\otimes K'\longrightarrow K'
$$

is a quasi-isomorphism: the local contracting homotopy remains a contracting homotopy after tensoring. No blanket assertion that $K'$ is K-flat is needed. The chain map to $H$, followed by evaluation, gives the other arrow in the roof

$$
K'\ \xleftarrow{\ \simeq\ }\ L_{\mathcal O}\otimes K'\ \longrightarrow\ K''.
$$

This proves C-SA04-421 and makes precise the canonicity in C-SA04-422. The map is functorial in the **given** torsor and homotopy data. Replacing those data without a compatible equivalence can change the derived class. Stacks 21.4.3 supplies the torsor/extension construction and 21.35 supplies the general derived tensor–Hom language; neither is quoted as a verbatim published version of this mixed-notation draft.

Choosing the homotopy data can change the class, as the indexed note already observes. Take an abelian sheaf $G$ with a torsor $P$ of nonzero class in $H^1(X,G)$, put $K'=\mathbf Z[0]$, $K''=G[1]$, and $u=0$. The differential in $\underline{\operatorname{Hom}}^\bullet(K',K'')$ is zero. Both $k=0$ and $k=1_G$ satisfy the additive compatibility. The first roof is zero; the second is the connecting morphism of the extension $0\to G\to\bar G\to\mathbf Z\to0$, hence is the nonzero torsor class, up to the shift convention. This supplies the precise canonicity qualification C-SA04-422; it is not a claim that the manuscript gives this example.

The caption placing $G,\bar G$ in degrees 0,1 at line 416 conflicts with the subsequent map to $H^{-1},H^0$, lines 427–432. It remains a scan question. The boxed universal isomorphism $\mathcal O\simeq R\underline{\operatorname{Hom}}(K',K'')$, line 449, is false: for $K'=K''=\mathcal O^2[0]$, its right side has rank four in degree zero. `RHOM_RANK` verifies the elementary example. The valid construction of **one map** in the derived category survives; C-SA04-423 is refuted with refinement C-SA04-421. No general crystalline equivalence or integral nil-invariance theorem follows from these first-order sheets.

## 4. The Serre material and the later comparison-data draft

### 4.1 Printed proofs, components, and arithmetic checks

C-SA04-424–439 separately register the printed propositions and theorems, including the hypotheses on compactness, semisimplicity, Hodge–Tate weights, geometric endomorphisms, and positive coprime multiplicities. They are not all unresolved Grothendieck claims. The weight convention is the printed covariant convention, with weights 0 and 1 for the Tate module; dualization reverses signs. “End” is explicitly the union over finite extensions before the endomorphism hypothesis is imposed. [Cote 161-5/5–16, lines 499–931.]

The source's arithmetic computations were rerun. If weights on $V$ are 0 and 1 with multiplicities $n_0,n_1$, weights on $\operatorname{End}(V)$ are −1,0,1. The determinant exponent of the normalized two-block cocharacter is $n_0n_1-n_1n_0=0$. If $\gcd(h,r)=1$, the identity

$$
r\binom hr=h\binom{h-1}{r-1}
$$

implies $h\mid\binom hr$. `SERRE_WEIGHT_ARITHMETIC` checks the symbolic identity and prints finite consistency tests, but those tests are not the proof of divisibility. The root-system classification used in Serre's argument is carried from the printed proof and the opened later paper; no finite table is represented as a new independent classification proof.

The red equality $M=I_{\rm alg}$, scan 10 line 690, omits component information. For a nontrivial finite ramified quadratic character over a mixed-characteristic local field, the representation is semisimple and Hodge–Tate of weight zero. Its Hodge–Tate cocharacter is trivial, while the inertia image has two elements. Thus its inertia algebraic group is nontrivial but its neutral component is trivial. This disproves the full-group equality C-SA04-431. Serre1979 §1.4 Theorem 2, attributed there to Sen, identifies the **neutral** group, yielding C-SA04-444. The finite-image corollary for weight zero is used with the printed algebraically closed residue-field hypothesis; arbitrary unramified infinite characters over a finite residue field are not counterexamples to that qualified statement.

### 4.2 Ramification: the lemma is proved on the next page

For a finite-height $p$-series $f(X)=\sum a_iX^i$, with first unit coefficient at degree $q=p^h$, choose $c_1>0$ bounding the valuations of the coefficients below degree $q$. For $0<v(x)<c_1/(q-1)$, the $a_qx^q$ term has strictly smaller valuation than every other term, so $v(f(x))=qv(x)$. At equality, cancellation is possible: $f(x)=2x+x^2$ and $x=-2$ have $v_2(x)=1$ and $f(x)=0$. Thus the printed strict inequality is essential. The inverse valuation estimate iterates a maximum of a contracted value and a translated value; eventually the contracted branch applies, giving an upper bound of a constant times $p^{-nh}$ for primitive division points. Since a positive valuation in $K(x)$ has denominator at most its ramification index, the lower ramification bound follows. `VALUATION_THRESHOLD` reruns the explicit cancellation and recurrence. [C-SA04-436–438; scans 15–16, lines 858–918.]

Serre invokes the primitive-point ramification bound temporarily on scan 15 and proves it on scan 16. Its role in the Haar-measure/Lie-orbit argument was read; the script does not certify that whole argument. Similarly, the final inertia openness conclusion is already obtained by passing to the unramified base; the subsequent request is for a **direct proof**, not for the truth of the theorem. [MP-SA04-109–111.]

Sen's 1972 ramification comparison is the bounded pair of inclusions, with $e=v_K(p)$, between upper ramification at $en\pm c$ and a $p$-adic Lie filtration. Fontaine–Ouyang, Appendix A.4, Theorem A.85, was opened with its totally ramified extension and complete DVR/perfect residue-field hypotheses. Gross1979 distinguishes the equal-characteristic situation. Literal equality of filtrations, or transfer to arbitrary characteristic-$p$ local fields, is not the theorem. The original Sen publisher record is verified; its subscription full text was not inspected, so the precise statement here rests on the opened exposition and its attribution. [C-SA04-442.]

### 4.3 The multiplicity-one centralizer reduction

The following targeted reduction checks the exact match behind C-SA04-440 and 446; it uses the opened Serre/Sen results and does not claim to reprove them. Let the neutral envelope $H$ act irreducibly on $V$ over $\mathbf Q_p$, and let its Hodge–Tate cocharacter have weights 0 and 1, with the weight-one space a line. The division algebra $D=\operatorname{End}_H(V)$ preserves that line, so restriction gives a unital injection $D\hookrightarrow C$. Therefore $D=E$ is a field. After scalar extension to $C$, $V=\bigoplus_{\tau:E\hookrightarrow C}V_\tau$, each summand is absolutely irreducible and occurs with multiplicity one; this follows equally from the simple-module density theorem for the algebra generated by $H$.

The cocharacter acts nontrivially on one summand and trivially on the others. Let $N$ be the connected normal subgroup generated by its $H_C$-conjugates. It acts trivially on the other summands. Its representation on the distinguished summand is isotypic, since $H_C$ is connected and irreducible there; the one-dimensional weight-one space forces that multiplicity to be one. Its weights are consequently $(0,1)$ with multiplicities $(m-1,1)$. For $m>1$, Serre1967 Proposition 5 applies with coprime positive multiplicities and gives the full $\mathrm{GL}_m$ on that summand. For $m=1$, the nontrivial cocharacter gives $\mathbf G_m$ directly. Galois conjugacy gives every factor. The smallest rational group generated by the cocharacter is therefore $\operatorname{Res}_{E/\mathbf Q_p}\mathrm{GL}_E(V)$. Sen's theorem identifies this with the neutral envelope; the open-image theorem supplies openness under the printed local hypotheses.

For a connected one-dimensional formal group, Serre1967 Proposition 8 gives the requisite irreducibility of the Lie action, and Proposition 7 identifies its commutant with geometric endomorphisms. Applying the preceding reduction over the unramified completion, where the residue field is algebraically closed, supplies the inertia version and hence openness in the indicated centralizer. This explains the dimension-one centralizer variant rather than citing an unrelated broad classification theorem. The report's broader two-weight classification is developed in Serre1979, Theorem 7 and §5; the marginal Springer identification remains only a dated bibliographic possibility. [MP-SA04-113.]

### 4.4 Full faithfulness and the scope of Hodge–Tate tensor data

de Jong's opened ICM report, §3, Theorem 2, states that for an integrally closed noetherian domain $R$, with fraction field $K$, every homomorphism between the generic fibres of two $p$-divisible groups over $R$ extends uniquely. The preceding theorem has a $p$-basis hypothesis in its $F$-crystal setting; the stated Theorem 2 does not inherit that extra condition. The report explicitly traces the equal-characteristic question to SGA 7 I, Exposé IX. The 1998 Inventiones article and its 1999 erratum are separately recorded. This settles the report's equal-characteristic hope C-SA04-448; it is not essential surjectivity of all generic $p$-divisible groups. [MP-SA04-114; deJongICM1998.]

The Serre–Tate lifting theorem is described in the source as known from Woods Hole 1964, while a new proposed proof has technical gaps. The contemporary Bourbaki bibliography records the mimeographed notes; Katz's later exposition gives a proof and, for ordinary abelian varieties over an algebraically closed residue field, the formal torus coordinates and their canonical origin. Thus C-SA04-449 concerns an unfinished method for an established theorem. Katz's §§3.7 and 4.3 also give a precise published Gauss–Manin/Serre–Tate connection, a more concrete comparator than an unsupported claim that all the archive's period and ordinary-lifting sheets already form one construction. [KatzSerreTate §§1–2; SerreBourbaki1968; MP-SA04-115.]

The handwritten category at cote 161-5/23, lines 1127–1145, is generated by **all** two-weight Hodge–Tate objects. The Barsotti–Tate objects form a fully faithful subcategory; the text does not identify the two. For a finite totally ramified extension of $W(k)[1/p]$, with $k$ perfect, Liu2013 Theorem 2.2.1 describes the Barsotti–Tate/crystalline integral correspondence in its stated setting. A Tate curve with $v(q)>0$ has a two-weight, semistable Tate module which is not crystalline, as the opened Gunton2021 discussion records. Therefore the larger category exceeds the good-reduction Barsotti–Tate image. This is a diagnostic for the domain, not a counterexample to a fully specified functor which the manuscript never finishes defining.

Fontaine1979, §§3.4–3.6, gives tensor structures and an equivalence on **B-admissible** objects for a suitable Barsotti–Tate period ring; §6.5 treats the associated proalgebraic objects. Those hypotheses are essential. The deleted data list, the changed fields $K,L$, the uncertain dual and positive twist, and the unfinished “Du moins si” prevent identifying the existence and uniqueness questions C-SA04-452–454 with a precise presently open theorem on the full Hodge–Tate category. They receive class F, not an assertion that p-adic Hodge theory has left a well-posed conjecture unresolved. [MP-SA04-116–118.]

## 5. Sections, normalized cocycles, and the last torus diagram

Let $1\to A\to E\to\Gamma\to1$ be an abstract group extension with one chosen section $\alpha$. It defines the action $\gamma\cdot a=\alpha(\gamma)a\alpha(\gamma)^{-1}$. Writing another section as $\beta(\gamma)=c(\gamma)\alpha(\gamma)$, multiplication gives

$$
c(\gamma\delta)=c(\gamma)\,\gamma(c(\delta)).
$$

Conversely this equation makes $\beta$ a section. Conjugation by $a\in A$ replaces $c(\gamma)$ by $a c(\gamma)\gamma(a^{-1})$. If the restriction to a subgroup $\pi$ is fixed to be $\alpha|_\pi$, then $c|_\pi=1$; conjugators preserving this normalization are exactly $A^\pi$. This proves C-SA04-456–457. Only if $\pi\triangleleft\Gamma$ does the normalized cocycle descend to the quotient action on $A^\pi$; normality is not supplied by the surviving group symbols. [Cote 161-5/28–29, lines 1454–1495; Conrad2012 Appendix B; SerreGC, bibliographic locator only.]

The neutral fibre of a restriction map is one pointed-set fibre. To compare arbitrary fibres, twist the action by a cocycle representing that fibre; writing $\gamma*_c a=c(\gamma)\gamma(a)c(\gamma)^{-1}$ turns its representative into the neutral one. Thus triviality of the untwisted neutral fibre alone does not prove injectivity. This is the distinction C-SA04-458 records. The conjugation orbit of a fixed section has stabilizer $A^\Gamma$, so the source's replacement of “torsor” by “homogeneous space” at line 1497 is mathematically necessary when that stabilizer is nontrivial.

Two diagnostic models delimit the undefined final question. For $\Gamma=\pi\times\mathbf Z$, trivial action and abelian coefficients, different images of the generator of $\mathbf Z$ give nonconjugate sections extending the same $\pi$-section. `DIRECT_PRODUCT_SECTION_MODEL` checks explicit distinct multipliers. If a field automorphism $\sigma$ preserves a discrete valuation, then $v(\sigma(a)/a)=0$; a uniformizer has nonzero valuation and is not a coboundary. `VALUATION_COCYCLE` records that obstruction. These examples disprove unrestricted abstract uniqueness, but cannot refute an intended arithmetic construction whose $\Gamma,\pi,A$, topology and action are incomplete. [C-SA04-459; SA04-486–488; MP-SA04-119.]

For $T=\operatorname{Res}_{K/\mathbf Q_p}\mathbf G_m$, the defining functor gives $T(\mathbf Q_p)=K^*$, whereas $T(K)=(K\otimes_{\mathbf Q_p}K)^*$. For a separable quadratic extension the latter algebra is $K\times K$, by its two embeddings; the exact symbolic idempotent check is `WEIL_RESTRICTION_POINTS`. Hence exchanging the point field in the last diagram changes the group. The exact valuation sequence $1\to\mathcal O_K^*\to K^*\xrightarrow v\mathbf Z\to0$ splits after choosing a uniformizer, by $n\mapsto\varpi^n$, and has no preferred such choice from the valuation alone. Integral points of an unspecified model must not be silently identified with all generic points. These are the verified portions C-SA04-461–462; the entire unfinished Néron-style diagram remains a reading and definition problem. [Scans 20 and 29, lines 1047–1055, 1521–1552; MP-SA04-120.]

## 6. Determinant norms and the degree axioms

**C-SA04-464–476; cote 98/3–14, transcription lines 9–363.** For a rank-$n$ locally free module $E$, the alternating map $\bigwedge^nE\to E^{\otimes n}$ has locally split rank-one image: in a basis, its ordered-tensor coefficient is one, so that coordinate projection splits it. No division by $n!$ is involved. The image is not the entire sign-eigenspace: over $\mathbf F_2$, for rank two, the latter is the three-dimensional symmetric tensors while the alternating image has dimension one. The exact computation ALT_CHAR2 verifies these dimensions.

For a finite locally free rank-$r$ algebra $B/A$, $\det_A(m_b)$ is a multiplicative homogeneous polynomial law. The divided-power/symmetric-tensor identification for flat modules gives an algebra map $\operatorname{TS}^r_A(B)\to A$ and the canonical section of the relative symmetric power. This identification, including arbitrary base change, is checked in Ferrand1998 §§2.5.1,3.1.1–3.1.2 and SGA4XVII 6.3.1–6.3.4. For $B=A[\epsilon]/\epsilon^2$, multiplication by $a+b\epsilon$ has matrix $\begin{pmatrix}a&0\\b&a\end{pmatrix}$, norm $a^2$; NORM_DUAL_NUMBERS reruns it. Mere constant fibre length without flatness is insufficient: $\operatorname{Spec}k\to\operatorname{Spec}k[\eta]/\eta^2$ has fibre length one but no section over the latter base. This is a diagnostic of a removed hypothesis, not the source's actual finite locally free example.

In the determinant expansion of $I+\epsilon M$, the coefficient of $\epsilon$ is the sum of diagonal entries, since selecting one nonidentity term forces it onto the diagonal. Thus norm differentiates to trace. NORM_TRACE checks a generic $3\times3$ matrix. Block-diagonal determinants multiply, proving the disjoint-sum formula; differentiation gives additive traces. An operation on ordered fibres descends only when its coefficient object has the requisite symmetric-descent property. SGA4 XVII 6.3.13.1 states it; 6.3.14 lists the representable, étale and quasi-coherent cases, and 6.3.15 supplies functoriality, base change, sums, rank and composition. An arbitrary presheaf does not automatically qualify.

Norm transitivity for a finite locally free tower rests on
\[
\det_A(M)=N_{B/A}(\det_B M)
\]
for a $B$-linear endomorphism of a finite free $B$-module. A universal verification introduces independent diagonal variables and inverts the successive pivot norms, which are monic and hence non-zero-divisors in those variables. Gaussian elimination then reduces to elementary unipotent and diagonal matrices, where both sides agree. Injectivity of the localization returns the identity before specialization. The exact published statement is SGA4 XVII 6.3.3, with its flatness distinction between symmetric tensors and the divided-power refinement; the trace consequence is 6.3.15(v). NORM_TOWER independently checks a rank-two-over-rank-two tower, $x=y^2$, $x^2=u$, on a generic element $a+by+cy^2+dy^3$. That specialization checks the calculation; it is not a sampling proof of the universal theorem.

For a permutation module $A[E]$, invariants have the orbit sums as a basis: invariant coefficients must be constant on each orbit. This proves arbitrary base-change compatibility without averaging by the group order. It fails for arbitrary actions: the sign action on $\mathbf Z$ has zero invariants, but reduction modulo two gives all of $\mathbf F_2$. PERMUTATION_INVARIANTS checks both cases.

The literal single-integer degree function on all morphisms is inconsistent with the empty target. Pull back any degree-$r$ map along $\varnothing\to Y$; it becomes the identity of the empty object, forcing $r=1$. Apply this to the disjoint sum of two identity fibres, whose degree is two by additivity, to get $2=1$. EMPTY_DEGREE records that contradiction. A degree predicate or locally constant rank function avoids it, but is a proposed repair. With a prescribed constant fibre cardinality, a finite $G$-set map has its canonical fibre-multiset section; pullback preserves it, disjoint sums concatenate it, and composition flattens a multiset of multisets. FINITE_SET_NORM_COMPOSITION checks an explicit case; this description proves the general finite-fibre identity. Étale-local trivialization gives the covering comparison, while determinant laws include ramified finite locally free maps. Rydh2008II §6 is the checked later Hilbert–Chow comparator; its broader Remark7.6 is not used as a proved theorem. The manuscript's last contracted-product sentence remains unfinished. [MP-SA04-121–123.]

## 7. Group-set sites, cover sequences and monodromy

**C-SA04-477–487; cote 98/16–24.** On the category of $G$-sets with finitely many orbits with the topology induced by jointly surjective covers, the sheaf attached to a $G$-set $A$ is $\operatorname{Hom}_G(-,A)$. Conversely, evaluate a sheaf $F$ at the regular orbit. Right translations $r_g(x)=xg$ and contravariance give $g\cdot a=F(r_g)a$, since $r_h\circ r_g=r_{gh}$. Descent along $G\to G/H$ gives $F(G/H)=F(G)^H$, and the cover by its finitely many orbits recovers all values. This proves the claimed equivalence and identifies the printed second argument $E$ in $\Phi_A(X)=\operatorname{Hom}_G(X,E)$ as a type alarm. Stacks03NP and Stacks00VZ supply the opened site comparators.

For infinite $G$, the smaller category is not closed under fibre products: the diagonal action on $G\times G$ has one orbit for every $g^{-1}h\in G$. A covering-sieve topology still makes sense, or one can work in the full $G$-set site. A Čech nerve must be interpreted there or at the sheaf level, rather than falsely asserting that all its objects have finitely many orbits.

The augmented free abelian complex on $T^{p+1}$, for nonempty $T$, is contracted by prepending a chosen point. The contraction need not be equivariant, but underlying exactness is exactness of $G$-modules. Apply $\operatorname{Hom}_G(-,I^\bullet)$ to an injective resolution: the resulting double complex gives the cover spectral sequence. A valid injective construction first embeds the underlying abelian group into an injective $J$, then coinduces $\operatorname{Hom}_{\mathbf Z}(\mathbf Z[G],J)$; coinduction preserves injectivity because its left adjoint, forgetting the action, is exact. An injective module retracts from this construction. Coinduction of an arbitrary abelian group is not automatically injective, already for $G=1$.

The vertical terms on an orbit are
\[
\operatorname{Ext}^q_{\mathbf Z[G]}(\mathbf Z[G/H],A)\simeq H^q(H,A),
\]
by induction/restriction adjunction and exact induction. The source's right-coset notation is consistent with the left action $g\cdot Hx=Hxg^{-1}$. A quotient-group Hochschild–Serre formulation requires normality of the relevant subgroup; an arbitrary subgroup chain does not supply it. The original HochschildSerre1953 paper and Stacks21.10.6/21.13.2 were opened. They settle ordinary cohomological descent, not a modern higher-topos hypercompleteness theorem. [MP-SA04-124.]

For the Picard–Brauer diagram write $E_2^{p,q}=\check H^p(T/S,\mathcal H^q(\mathbf G_m))$. If the $q=1$ row vanishes, the initial map $E_2^{2,0}\to H^2$ is injective and the next obstruction from $E_2^{0,2}$ is $d_3$. The degree-three middle term is the filtration piece $F^1H^3$, or the kernel of the edge map to $E_\infty^{0,3}$. The next obstruction is $d_3:E_3^{1,2}\to E_3^{4,0}$, whose cokernel is $E_4^{4,0}$, not automatically the total $H^4$. A finite field-extension cover has Artinian nerve terms and zero Picard groups, giving the stated qualified case.

The unrestricted fixed-cover injection is false. For a nonsplit real conic, the complex cover is $\mathbf P^1_\mathbf C$ and its degree-one line bundle is conjugation-invariant but does not descend. A semilinear lift has matrix $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ with $J\bar J=-I$. Its obstruction is $-1$ in $\mathbf R^*/N_{\mathbf C/\mathbf R}\mathbf C^*$, nontrivial since nonzero complex norms are positive. This is the nonzero incoming Picard $d_2$. REAL_CONIC_DESCENT verifies the matrix and norm; it does not refute the field-cover case.

The deleted “trivial local coefficients” must stay deleted. Circle reflection acts by $-1$ on $H^1(S^1,\mathbf Z)$; its mapping torus is the Klein bottle, whose cellular differential $(0,2)$ gives $H^1=\mathbf Z$, $H^2=\mathbf Z/2$. KLEIN_BOTTLE reruns that calculation. Likewise $O(2)$ modulo a reflection subgroup is a connected circle, with the nonidentity component acting by degree $-1$. CIRCLE_MONODROMY checks this action. Thus the conditional reading that cohomology action depends only on the permutation of fibre components is false; the ink and the intended acting group remain undecided.

## 8. Bounded families and field positions

**C-SA04-488–502,512–515; cote98/27–37,44.** FGA IV Theorem2.1 and its1962 erratum give boundedness for quotients of a fixed coherent sheaf with a finite set of Hilbert polynomials in the projective noetherian setting. Both conditions matter. The bundles $\mathcal O(n)\oplus\mathcal O(-n)$ on $\mathbf P^1$ have polynomial $2m+2$ but unbounded $h^0$. A finite-type bounded family on a proper scheme has bounded $h^0$, using a finite flatness stratification, so fixed polynomial alone fails. Conversely $\mathcal O(n)$ is a quotient of $\mathcal O^2$ via $X^n,Y^n$, is pure with associated cycle $[\mathbf P^1]$, and has polynomial $m+n+1$. Thus fixed source and associated cycle are insufficient. BOUNDEDNESS_POLYNOMIAL reruns the formulas. This refutes only the tentative pencil interpretation, not the established theorem. Relative chronology of the undated leaves and the May1961 talk is not inferred.

Lines675–684 already name bounded kernels and extensions. Properness is needed for the general operation: on $\mathbf A^1$, multiplication by $x^n$ maps the singleton family $\mathcal O$ to itself but has cokernels of unbounded length $n$. FGA IV Proposition1.2 includes properness. The affine-line projection also sends $\mathcal O$ to noncoherent $k[x]$ on a point. Generic rank one does not give an embedding into the structure sheaf: $\operatorname{Hom}(\mathcal O(n),\mathcal O)=H^0(\mathcal O(-n))=0$ for $n>0$. BOUNDEDNESS_AFFINE_COKERNEL records these tests. [MP-SA04-125.]

For transitivity of the field-equivalence relation, tensor the two witness fields over their specified middle field. The tensor product is nonzero because field extensions are faithfully flat. A prime quotient followed by its fraction field embeds both witnesses, so the two sheaf isomorphisms compose. A coherent object on a finite-type field scheme, its gluing maps and an inverse isomorphism use finitely many coefficients on a finite affine cover. They descend to a finitely generated coefficient field; quasi-compactness and quasi-separatedness make the data finite. This matches the opened Stacks32.10.2 statement.

An arbitrary prescribed compositum cannot replace a suitable witness. The point module $k(t)[x]/(x-t)$ in two copies of $k(t)$ agrees under aligned embeddings. Independent embeddings into $k(t_1,t_2)$ give distinct ideals $(x-t_1)$ and $(x-t_2)$ whose sum is the unit ideal; no further field extension makes them equal. The aligned tensor is nonzero, while the independent tensor is zero. RELATIVE_FIELD_POSITIONS checks both ideals. Hence operations on these geometric classes must be set-valued, allowing all relative positions. This is a negative answer to one reading of “composed/common extension”, not a decision that the ink cannot say “universal”. [MP-SA04-126.]

An algebraically closed field $\Omega/k$ of infinite transcendence degree represents every finite-data class. For two realizations that become isomorphic, descend both objects and the isomorphism to finite coefficient fields. Embed the finite witness in $\Omega$, extending one prescribed embedding. Extend the other coefficient-field isomorphism to an automorphism of $\Omega$ by algebraic closures and matching transcendence bases; removing finite transcendence degree leaves the same infinite cardinal. This proves the automorphism-orbit assertion for finite-presentation objects. It does not claim that $\Omega$ contains all field extensions. Finite transcendence degree cannot suffice: monic defining polynomials with arbitrarily many algebraically independent coefficients give cyclic modules requiring arbitrarily large coefficient transcendence degree.

The algebraically closed field proviso matters for support operations. If $a\notin k^p$, $k[x]/(x^p-a)$ is reduced but becomes nonreduced after adjoining a $p$th root; INSEPARABLE_SUPPORT checks the factorization. Embedded primary components are also noncanonical, even in characteristic zero:
\[
(x^2,xy)=(x)\cap(x^2,y-a x)
\]
for every scalar $a$. Reducing an element of $(x)$ modulo the second ideal shows that membership in the intersection is exactly membership in $(x^2,xy)$; PRIMARY_COMPONENTS verifies it by elimination with symbolic $a$. The manuscript lists such operations as sets and retains algebraically closed/characteristic-zero qualifications.

Products of parameter schemes represent relative positions for tensor products. For Hom, a finite presentation $B^r\to B^s\to M\to0$ gives $\operatorname{Hom}_B(M,N)=\ker(N^s\to N^r)$. Flatten $N$ and the finite cokernel of this map over the base. The sequences through its image stay exact after tensoring, giving the Hom comparison. This also explains why the second sheaf in the displayed source formula must be $G$. FGA IV §1 before Proposition1.2 and generic flatness supply the comparator.

For a bounded complex and fixed finite degree range, flatten finitely many terms, cycles, boundaries and cohomology modules on a dense open set, then repeat over the reduced closed complement by noetherian induction. Cohomology is recomputed on each stratum. This gives finitely many strata; it is not arbitrary nonflat pullback of original cohomology. For an unbounded complex of blocks $k[t]\xrightarrow{t-a_n}k[t]$ in disjoint degree pairs, infinitely many distinct $a_n$ require infinitely many exceptional loci: any dense stratum contains some such point and then fails that degree's kernel comparison. UNBOUNDED_COMPLEX records the rank jumps. A different all-degree failure is $B=k[x,y]/(x,y)^2$: the first syzygy of its residue field is $k^2$, each next syzygy doubles the copies, and all differentials vanish after tensoring with $k$. Hence $\dim\operatorname{Tor}_i^B(k,k)=2^i$, as RADICAL_SQUARE_ZERO_TOR records. Fixed-degree boundedness is not boundedness of the union over every degree.

## 9. The Tor and Ext proof audit

**C-SA04-503–511; cote98/38–44.** The source's input $A$-flatness is present. Its erroneous step is resolving $M_i$ freely over $B_i$ and tensoring over $B$ without $B$-flatness. With $B=k[x]$ and $B_i=M_i=k$, degree-zero $B_i$-free resolutions miss $\operatorname{Tor}_1^B(k,k)=k$, computed by the $B$-free resolution with differential $x$. WRONG_RING_TOR refutes that step, not the conditional comparison theorem.

Here is the complete finite-type repair. Assume $A$ noetherian, $B$ finite type over $A$, finitely many $B_i$ finite type over $B$, and $M_i$ finite over $B_i$. Choose polynomial $B$-algebras $C_i\twoheadrightarrow B_i$. Resolve $M_i$ by finite-rank free $C_i$-modules, possible since $C_i$ is noetherian; these terms are $B$-flat. Their total tensor complex has finite terms over $C=\bigotimes_B C_i$, hence coherent homology. Each element of $\ker(C_i\to B_i)$ acts by a chain map lifting zero on $M_i$, so it is null-homotopic and kills the total homology. That homology is therefore finite over $C/\sum_i\ker(C_i\to B_i)C=\bigotimes_B B_i$, the intended algebra.

If $B$ and all $M_i$ are $A$-flat, the resolutions remain exact after any base change $A\to A'$: their successive augmentation kernels are $A$-flat, by induction through short exact sequences with flat quotient. The total complex is $A$-flat and specializes to the appropriate derived tensor over $B'=B\otimes_A A'$. Thus
\[
\operatorname{Tor}_p^A(\operatorname{Tor}_q^B(M_1,\ldots,M_n),A')
\Longrightarrow \operatorname{Tor}_{p+q}^{B'}(M_1',\ldots,M_n')
\]
gives edge isomorphisms through total degree $N$ if the inner Tor groups for $q\le N$ are $A$-flat. The opened Stacks15.63.3 is the precise two-input form. This proves the repair C-SA04-506. [MP-SA04-127.]

Output flatness alone is insufficient. Set $A=k[t]$, $B=A[x]$, $M_1=B/(tx)$, $M_2=B/(x)$. Tensor the resolution by $x$ of $M_2$ with $M_1$. Both Tor0 and Tor1 are isomorphic to $A$, the latter generated by the class of $t$. At $t=0$, $M_1'=k[x]$, $M_2'=k$, so Tor1 is zero. TOR_INPUT_FLATNESS checks it. The source already assumes the input flatness that excludes this example.

Finite free terms in the Hom argument are substantive. For $M=\bigoplus_{n\ge1}\mathbf Z$ and $N=\mathbf Z$, all positive Ext vanish and Hom is the flat group $\prod_n\mathbf Z$. But $(\prod_n\mathbf Z)\otimes\mathbf Q\to\prod_n\mathbf Q$ misses $(1/n!)_n$: any element on the left has one common denominator. HOM_COMMON_DENOMINATOR records that obstruction.

Terminal-cokernel flatness is separately necessary. With $A=k[t]$, $B=A[x]$, $M=B/(x)$, $N=B/(x-t)$, all inputs are $A$-flat. The Hom complex of the usual resolution is $A\xrightarrow{t}A$. Its degree-zero cohomology is zero, whereas the special fibre has degree-zero cohomology $k$; the terminal cokernel $A/(t)$ is not flat. EXT_TERMINAL_COKERNEL verifies this example.

For the actual finite complex $K^0\to\cdots\to K^{N+1}$, suppose all terms, $H^p(K)$ for $p\le N$, and the final cokernel $H^{N+1}(K)$ are $A$-flat. Starting from the last term, exact sequences through boundaries, cycles and cohomology show successively that all cycles and boundaries are flat: kernels of surjections with flat middle and flat quotient are flat. Tensoring these sequences preserves exactness, so $H^p(K)\otimes_A A'=H^p(K\otimes_A A')$ in every complex degree. Only its identification with Ext is restricted to $p\le N$. Thus the source's all-degrees phrase is valid and the contextual overcorrection is rejected. These terms need be flat, not free.

The comparison maps arise from the natural termwise tensor–Hom morphism. Resolution lifts of an identity are chain-homotopic, hence give identical maps on cohomology, and the finite free construction commutes with localization. The local maps therefore agree and glue. This checks the explicit reader verification in C-SA04-510. EGA III2 §7.7 supplies the canonical-functor comparator. The final unrestricted Ext1 hope is not identified: Stacks36.30.7 gives a precise sufficient theorem for a finitely presented morphism, perfect first argument, bounded finitely presented base-flat second argument and proper support. It does not justify omitting those hypotheses. [MP-SA04-128–130.]

## 10. Reused topology and abelian-variety typescripts

For a quotient $f:X\to X/R$ and $A\subset X$, $A/R_A\to f(A)$ is a homeomorphism precisely when every relatively saturated open subset of $A$ is the trace of an open saturated subset of $X$. Such a trace is exactly the inverse image of a relatively open subset in $f(A)$; lifting that relatively open set to the quotient proves the converse. The closed formulation is equivalent. This proves C-SA04-516 and identifies the repeated $f(B)$ in scan6 line135 as a likely target-variable error. It does not say that every restriction of a quotient is a quotient. Crainic2023 is the opened quotient-topology comparator.

Finite-coordinate basic opens give coordinatewise continuity into a product and prove regrouping/permutation homeomorphisms in both directions. The graph map is a homeomorphism onto the graph when $f$ is continuous, with inverse the first projection; the second projection proves the converse. These establish C-SA04-517 independently.

For the gluing exercise use discrete $X_1=\{a,b\}$, the upper-set space $X_2$ for $a<c$, and the upper-set space $X_3$ for $c<b$, identifying matching labels. All singleton overlaps are homeomorphic, but the quotient opens are exactly $\varnothing,\{b\},\{b,c\},\{a,b,c\}$. The induced topology on $X_1$ loses $\{a\}$. GLUING_COUNTEREXAMPLE exhaustively verifies it. This proves the typescript's own negative exercise C-SA04-518; the source explicitly says arbitrary overlaps are insufficient and is not refuted by this example.

If all compatible gluing overlaps are open, saturation of an open set in one piece has an open trace in each other piece. If all are closed, the same reasoning applies to a closed set: its trace in another piece is its image under the single compatible overlap homeomorphism. Closedness in a disjoint sum is tested piece by piece, so no false finite-union assumption is needed. Each piece embeds. In the interval quotient, saturation by integer translation is a locally finite union of closed translates, proving the circle quotient. These verify C-SA04-519.

For $L\in\operatorname{Pic}^0(A)$ on an abelian variety, $m^*L\simeq p_1^*L\otimes p_2^*L$ gives additive pullback under sums of homomorphisms and $[n]^*L\simeq L^{\otimes n}$. The Pic0 restriction is essential. MilneAV Proposition9.2 and Remark9.3 identify this with translation invariance and algebraic triviality. Proposition8.1 makes finite kernel an isogeny for equal-dimensional source and target; Proposition9.1 identifies ampleness of an effective bundle with zero-dimensional stabilizer. The source postpones existence, surjectivity and a uniform integer $d$ in the kernel criterion; modern theory permits $d=1$, which is a comparator rather than literal wording. Theorem7.1 supplies projectivity. Historical “ample” remains the source's terminology, and point separation alone is not claimed to prove a closed immersion. [C-SA04-520–521,525; MP-SA04-131.]

For a finite-dimensional space with injective local expansion, successive scalar coefficient equations have kernels dropping by at most one dimension, with zero intersection. The last nonzero kernel is a line. A $K$-structure on both the space and the functionals gives a $K$-rational generator. But the first full-rank homogeneous prefix has only the zero solution: the basis $1,t$ gives the identity matrix. The immediately preceding prefix gives the intended line. JET_FLAG verifies these ranks, refuting C-SA04-523 with refinement522.

The degree-compatible monomial ordering makes the vanishing-tail condition an ideal: multiplication by positive degree moves a surviving monomial beyond the prefix; constants preserve the vanishings. The series lower limit infinity, the omitted coefficient index0, and the function/divisor equality are distinct scan alarms. The uncertain pencil note is not promoted to “Prouver!” or assigned an author. [C-SA04-524,526–527; MP-SA04-132.]

## 11. Independent checks for the coordinating audit

### 11.1 Manin's equality, coordinating claim C-SA04-620

The complete Codex K93-02 transcription, lines1–228, was read. The equality is at scan159 line215, with a verification query at218; scan160 is the following converse factorization. Let $J=P^\infty$ be jets. In the given stratified extension, $\lambda^+(p')$ is the ordinary jet minus the stratified horizontal extension, with zero augmentation. The cocycle gives $J(d_E)\lambda^+(p')=j(d_Pp')$: the horizontal term has zero differential. For $Dv=\Delta d_E$, naturality gives $u_DJ(v)=u_\Delta J(d_E)$, and hence
\[
\mu D(p')=u_\Delta j(d_Pp')=\Delta(d_Pp')=\nu\Delta(p').
\]
Changing the lift adds $\Delta d_Eu(e')=0$, so it descends and glues. This uses the supplied stratification, not the converse characteristic-zero existence lemma. The source warns that the plus inclusion itself is not compatible with the canonical stratification; it is not being called horizontal here.

The saved c_manin_check.py expands a generic degree-seven polynomial, its positive jet $F(x+h)-F(x)$, the $h+k$ cocycle and a generic order-four operator. All exact residuals vanish in outputs/c_manin_check.json. This finite coordinate check confirms signs; the preceding naturality argument is the universal proof.

### 11.2 Genus-two counterexample, coordinating claims C-SA04-647–648

The actual K93-05 source, lines218–264, was read; the issue is scan204 line245. For
\[
z^2+(x^2+x+1)z=x^5+x^3+x^2+1
\]
over $\mathbf F_2$, set $h=x^2+x+1$, $z=hy$. Expansion gives $y^2+y=x+1/h$. There are three geometric simple poles, the two distinct roots of $h$ and infinity. In the degree-two Artin–Schreier cover each is totally ramified with different exponent two, so Riemann–Hurwitz gives $2g-2=-4+6=2$. This agrees with the reduced-pole formula in the opened primary RAS2025, §2.2, equation (2.2); the companion p-rank formula is (2.3). The affine equation is smooth at $h=0$: then $z=0$ and its $x$ derivative is one modulo $h$. There is one rational point over infinity.

The independent c_review_genus2.py implements polynomial finite-field arithmetic and the trace criterion, checking every nonzero element's $(q-1)$st power. It gets counts3,7,9,31 over $\mathbf F_2,\mathbf F_4,\mathbf F_8,\mathbf F_{16}$. Newton identities from all four counts, without assuming the functional equation, give $P(T)=1+T^2+4T^4$ and $\#J(\mathbf F_2)=6$. Rational two-torsion therefore has dimension one, while root1 has algebraic multiplicity two in $P\bmod2=1+T^2$. Over $\mathbf F_2$ semilinearity introduces no ambiguity. This checks C-SA04-647 under the algebraic-multiplicity interpretation and supports the fixed-space correction C-SA04-648. It does not decide the meaning of the source's phrase “number of eigenvalues”. Full output: outputs/c_review_genus2.json.

## 12. What the checks certify

All 107 indexed verdicts and all 89 nested MPL98 notes were checked against the corresponding text. Every one of the 127 claims has an individual search-ledger row, with actual discovery queries and opened primary locators. Failed zbMATH access, unavailable Spencer full text and unsuccessful exact-formulation searches are useful negative results, not claims of nonexistence. A verified bibliography label means the listed primary URL or bibliographic record was opened; its annotation distinguishes full theorem inspection, metadata only, and direct-download fallback. Raw copyrighted web excerpts and primary PDFs are outside the deliverable.

Computation labels refer to saved programs and complete outputs. Finite examples, symbolic identities, independent elementary proofs and reference checks have different check events. Serre's classification, Sen's theorem, p-adic Hodge correspondences and proper-cohomology theorems are used under checked hypotheses; none is called independently re-proved by this run. de Jong's author erratum was also opened and read: it corrects Lemma2.1(iii) and the semistable-reduction definition, explicitly saying no other changes are necessary. It does not retract the generic-Hom extension theorem. The ranked Stage6 directions remain tasks for later runs, not newly solved research programmes.
