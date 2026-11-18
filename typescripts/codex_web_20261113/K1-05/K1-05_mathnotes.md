# K1-05 · Mathematical notes

The line references follow the numbered manuscript lines in the LaTeX files. Statement identifiers connect a check to its row in CHECK_EVENTS.tsv.

## What the pages do

**U01 · Genus, scan 108, lines 1–11.** The page continues an earlier product representation. Given the least integer \(k\) for which the series over nonzero roots converges and a polynomial \(g\) of degree \(r\), the larger of \(k\) and \(r\) is called the genus. The substitution of « grand » for « petit » is part of the definition on the page. Formula (3) writes the expansion with the exponential factors visible.

**U02 · Genus zero and order, scans 108–109.** Formula (4) isolates a constant times a product whose reciprocal roots are summable. The next heading defines order through the upper limit of \(\log\log M(r)/\log r\). The qualification « pour \(r\) assez grand » completing the growth condition is on the following sheet.

**U03 · Hadamard–Borel, scan 109, lines 2–21.** Finite order controls the sum over nonzero roots in (5) and the factorization when \(f(0)\ne0\). The corollary gives genus zero for order below one. A second inequality bounds order by genus plus one. The boxed interval explains why an integer order can leave two possible genera. The names attached to the symbols in the adjacent sentence are discussed below.

**U04 · Examples and operations, scan 110, lines 1–9.** An exponential and a product with roots \(n^\alpha\) illustrate the preceding distinction. The author explicitly qualifies the claimed order of the latter. He gives an upper bound for the order of a product, says the same for a sum, and describes the resulting classes of entire functions as algebras.

**U05 · A coefficient criterion, scan 110, lines 10–12.** Hadamard’s theorem is stated in terms of \(n^\alpha\sqrt[n]{|c_n|}\) tending to zero. The conclusion on this sheet is expressed as a bound on the genus.

**U06 · A coefficient majorant, scans 111–112.** A genus-zero entire function majorizes the coefficients of \(f\) in modulus. With the additional reciprocal-root sum finite, the claim is that \(f\) has genus zero. The proof isolates \(e^{\beta z}\), draws a sector where it gives growth, and introduces \(g(z)g(\omega z)g(\omega^2z)\). A boundedness argument leads to the conclusion written sideways on 112. The abandoned inequality at the foot of 111 precedes this sector argument.

**U07 · Two exponents of a sequence, scan 113, lines 1–12.** For a decreasing positive sequence tending to zero, one infimum uses domination by \(n^{-1/s}\) and the other uses convergence of the series of \(s\)-th powers. The text compares them in both directions and gives a logarithmic expression involving \(1/\rho\).

**U08 · The little-o lemma, scan 113, lines 13–23.** The statement about a multiple of \(n^{-1/s}\) is crossed out and sharpened to little o. After reduction to \(s=1\), the proof groups consecutive terms between indices \(n_{i-1}\) and \(n_i\). It compares the sizes of these blocks with a summable sequence \(\varepsilon_i\). The resulting bound on the strictly increasing integers ends the argument.

**U09 · Growth of a positive product, scan 114, lines 1–19.** The sequence exponent is identified with the order of the product with positive coefficients. For the model \(\alpha_n=n^{-\beta}\), the author splits the product at \(\nu\), estimates the tail by an integral and chooses \(\nu\) just above \(r^{1/\beta}\). He then bounds the initial factors by a power of \(1+r\).

**U10 · Maximum term and change of coefficients, scans 114–115.** Scan 114 closes with the coefficient maximum \(B(r)\) and an order formula using it. Scan 115 compares the two products built from \(\lambda_i\) and \(\alpha_i=|\lambda_i|\), and asserts that their orders agree.

**U11 · Orders beyond one sequence, scan 115, lines 8–18.** The summability exponent is attached to a countable set of complex numbers. The author calls rapid decrease order zero. For a sequence in a Banach or Fréchet space he distinguishes strong and absolute summability. For a bounded set he asks how small the order of a sequence can be whose closed, convex, balanced hull contains the set.

**U12 · Counting radii, scan 116.** For a sequence of positive radii tending to infinity, \(n(r)\) counts indices with \(r_\nu\le r\). A finite-interval identity uses the one-sided values \(n(b-0)\) and \(n(a+0)\). Integration by parts then relates convergence of a reciprocal-power series to a weighted integral of \(n\). The proof uses a circled « 1 bis » and a sequence \(b_i\) going to infinity.

**U13 · The limit and a general weight, scan 117.** A lower bound for disjoint blocks of the convergent series gives a contradiction unless \(n(r)/r^\alpha\) tends to zero. The author passes to an infinite endpoint, then gives the corresponding test and tail formula for a decreasing differentiable weight \(\lambda\) tending to zero.

**U14 · Counting zeros by a circular mean, scan 118.** The radii are now the moduli of zeros. The author writes the count as a circle integral, interchanges two integrations and integrates the logarithmic derivative in the radial direction. The oblique instruction « en prenant les parties réelles » leads to the mean \(V(r)\) of \(\log|f|\). A final box substitutes \(\mu=-\lambda'\).

**U15 · The endpoint zero, scan 119.** The parenthetical formula uses \(r^2\mu(r)\to0\) and \(|f(0)|=1\) to take the lower endpoint to zero. The final lines relate a weighted integral of the count to the maximum modulus. The remaining surface is blank.

**U16 · A function on \(l^1\), scan 120.** The elementary symmetric sums \(\alpha_n(\lambda)\) give the coefficients of a product of genus zero. The proposition defines \(S(\lambda)=\sum n!\alpha_n(\lambda)\), states its local convergence radius, and distinguishes finite-dimensional holomorphic restrictions from boundedness on the unit ball. The corollary records the coefficient decay in root and factorial forms.

**U17 · Beginning of the proof, scan 121.** Applying the corollary on the line \(\lambda z\) introduces a scalar power series and Stirling’s formula. For a decreasing positive sequence, the author splits the product into its first \(n+1\) factors and a tail of total mass \(\rho_{n+1}\). He obtains a bound with a product of small \(\varepsilon\)'s divided by \((n+1)!\). The last visible words are « D’où ».

## Statements left without proof

| Scan, lines | Author’s words | Status on these pages |
|---|---|---|
| 109, 2–10 | « Théorème 2 (Hadamard-Borel) » | The root-sum and finite-order factorization are invoked. |
| 109, 15–17 | « Il est très facile de se convaincre que » | The upper bound of order by genus plus one is given without a derivation. |
| 110, 1–9 | « P. ex. » and « Notons que l’ordre du produit de deux fonctions entières… » | The examples and the sum and product bounds are stated. |
| 110, 10–12 | « Théorème 3 (Hadamard) » | The coefficient criterion is stated without a proof. |
| 111, 18–21 | « on sait que … toute fonction de genre zéro … admet une majoration » | The estimate with arbitrarily small positive ε is used in the proof. |
| 113, 8–11 | « On a aussi » and « Le critère de Riemann affirme » | The logarithmic expression and one direction of the exponent comparison are asserted. The following lemma treats the converse. |
| 114, 20–22 | « Rappelons que si on pose » | The formula for the order using \(B(r)\) is recalled. |
| 117, 10–17 | « Des résultats analogues seraient obtenus » | The general-weight criterion and endpoint identity are stated after the power-weight argument. |
| 118, 3, 8–12 | « On aura » and « car les intégrales … doubles qui interviennent sont convergentes » | The initial circle count and the justification for exchanging integrations are used without a separate proof. |
| 119, 3–5 | « Comme … on obtient une majoration » | The estimate using the maximum modulus is stated. |
| 120, 11–21 and 121, 22 | « est absolument convergente », « un rayon de convergence égal à 1 », « cette fonction n’est pas bornée dans la boule unité » | The proof starts in this extract. Its conclusion, including a demonstration of unboundedness, is not reached by the final « D’où ». |

## Questions and conjectures

Scan 110, lines 2–3, explicitly qualifies the claimed order of the product by « sauf erreur ». No other explicit conjecture or question about a mathematical step was identified. The proof ending at the boundary of scan 121 carries no authorial question mark.

## Slips

| ID | Scan, lines | Written form and possible correction | Confidence and reason |
|---|---|---|---|
| S109 | 109, 16–18 | The sentence assigns « le genre et l’ordre » to \(\omega,g\). Exchanging the nouns agrees with the boxed \(\omega-1\le g\le\omega\). | High for the local interchange. The preceding two inequalities identify the roles without using the doubtful letters at the foot. |
| S110 | 110, 2–3 | The order of the product with roots \(n^\alpha\) is given as 1, « sauf erreur ». The later model gives \(1/\alpha\). | High for the discrepancy for \(\alpha>1\). Rotation by a half-turn preserves the circle maximum, and scan 114 gives the order of the positive model. |
| S111a | 111, 9 | The simple factors are preceded by a sum. A product would fit the stated genus-zero majorant. | Low. The neighbouring constant is doubtful. Read as a sum, the infinitely many terms at \(z=0\) already equal 1 each. |
| S111b | 111, 14–17 | The substitution uses \(\Theta=\beta/|\beta|\). The choice giving a positive coefficient in \(f(\Theta z)\) is \(\overline\beta/|\beta|\) for nonzero \(\beta\). | High for the substitution as written. For \(\beta=i\) the written multiplier produces \(-1\). |
| S112 | 112, 1–5 | The chosen angle is between \(\pi/3\) and \(\pi\). An angle in \((\pi/3,\pi/2)\) permits the positive lower bound for the real part. | High for the bound’s failure over the whole written range. At angle \(2\pi/3\) a unit vector has negative real part. |
| S113 | 113, 8 | The logarithmic characterization of \(1/\rho\) has an upper limit. The infimum defined above it gives a lower limit. | Low as a textual diagnosis because the adjacent comparison was overwritten. Eventual upper bounds for \(\alpha_n\) give eventual lower bounds for \(\log(1/\alpha_n)/\log n\). |
| S116 | 116, 9 | The second boxed sum has \(1/r_\nu\). The formula for a general \(\alpha\) requires \(1/r_\nu^\alpha\). | High. The finite-endpoint formula and the integral in the same box agree on the exponent. |
| S117 | 117, 2–5 | The endpoints named \(b_i\) become \(\lambda_i\) in the block estimate. One consistent name would suffice. | High for the change on lines 2–4. The numerator on line 5 is itself a low-confidence reading. |
| S117-ref | 117, 8–9 | « on obtient (2) » appears to refer to the second boxed formula on scan 116. Its label there might be (1) or (1′). | Low. The earlier label is doubtful. |
| S120 | 120, 2–4 | The bound begins with \(\alpha_n(\lambda)\le\cdots\). A modulus on the left would make it meaningful for complex \(\lambda\). | High. The first coefficient can be nonreal, for example at \(\lambda=(i,0,\ldots)\). |
| S121a | 121, 9–14 | The Cauchy estimate has \(M(R)/R^{n+1}\). The coefficient estimate has \(M(R)/R^n\). | High. For \(1+z\) and \(R=2\) the written estimate would bound 1 by \(3/4\). |
| S121b | 121, 15–18 | Substitution of \(R=(n+1)/\rho_{n+1}\) yields \(e^{n+1}\) from the tail estimate. The two live exponential factors have \(e^n\). | High for the substitution using the live factors. No inference uses the adjacent cancelled product. |

## Pointers

| Scan | Wording | Referent on these sheets |
|---|---|---|
| 108, 4 | « dans la représentation (2) » | An earlier numbered representation outside the extract. |
| 109, 2 and 110, 10 | « Hadamard-Borel », « (Hadamard) » | Named theorems, without a publication reference. |
| 113, 10 | « Le critère de Riemann » | The sequence comparison used at this point. |
| 115, 7 | « (voir ci-dessus) », « (th. de Hadamard) » | The earlier product-order argument and the named theorem. |
| 116, 12 and 117, 8–9 | « (1) s’écrit », « dans (1 bis) », « on obtient (2) » | Local formula references. The last label is discussed above. |
| 120, 1 and 115, 13–15 | « l’espace de Banach », « Banach, ou de Fréchet » | Names of the spaces under discussion. |
| 121, 4–5 and 8–9 | « la formule de Stirling », « l’inégalité de Cauchy » | The factorial asymptotic and the coefficient estimate used in the proof. |

## Remarks of the model

- **M116 · Model, high confidence.** The strict endpoints in the finite-interval sum matter. For \(r_\nu=2^\nu\) starting at \(\nu=1\), the open interval \((1,3)\) contains just 2. With \(\alpha=2\) the boundary term \(1/9\) and the integral contribution \(5/36\) add to \(1/4\). This checks one instance of scan 116, line 4.
- **M119 · Model, medium confidence about scope.** The condition \(|f(0)|=1\) in the parenthesis on scan 119 matters if the following absolute-value estimate is read independently. For the constant \(f=e^{-2}\), the mean is \(-2\) and the maximum modulus is \(e^{-2}\). The paragraph break leaves the intended scope open.
- **M120 · Model, high confidence for the finite example.** Four equal coordinates \(1/8\) and all other coordinates zero give \(S=891/512\) by direct summation of the elementary symmetric coefficients. This checks the coefficient construction on scan 120 in a case where the series terminates.
- **Reading question · Model, low confidence.** In scan 120, line 7, the frozen argument of \(f\) is given as \(\lambda\), \(n\), or \(z\), in that order. The product uses \(z\), while the small arch inside \(f(\,)\) resembles the other two candidates. The later argument on scan 121 uses \(f(z)\).
