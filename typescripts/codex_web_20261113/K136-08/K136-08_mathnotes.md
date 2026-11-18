# Mathematical notes on cote 136, scans 64–78

## What the pages do

**64 · Cohomology with sheaf coefficients.** For a sheaf of $k$-modules $F$ on $X_\bullet$, the page describes cochains as global sections of $C^*_{X_\bullet}\otimes F$. It identifies their cohomology with that of $F$, then extends the construction to a complex $F^*$ by taking total degree. A marginal arrow singles out the claim that the resolution is flasque.

**65–66 · The Stokes condition.** To give a degree-zero map from a complex of half-simplicial modules to $C^*_{*M}$, the author gives maps $K_n:A_n^n\to M$. Two triangles compare composition with the two differentials. Equating the composites gives the square labelled « condition de Stokes », with $K_n\partial_{n+1}=K_{n+1}d$.

**66–67 · Evaluation and derived sections.** The resulting cochain map represents a map to derived global sections. When $A^*$ resolves $M_*$ and the degree-zero map restricts to the identity on $M$, the author identifies it with the canonical map from ordinary to derived sections. For $f:X_\bullet\to A_\bullet^n$, its value in degree $n$ is the function $u^n(f)=K_n\circ f_n$ on $X_n$.

**67–68 · Extension from degree zero.** Conditions a), b) and c) bound the degrees of $A_n^i$ and require vanishing in two cohomological degrees. A Stokes system is then determined by $K_0$. The obstruction on scan 68 is its value on $\partial_1(\ker(d:A_1^0\to A_1^1))$. Taking $A_0$ modulo that subgroup gives the universal target. Condition c′) addresses $n=1$ and gives a case where $A_0$ itself serves.

**68–69 · Nondegenerate cochains and a divided-power example.** The nondegenerate cochains are written as an intersection of kernels. The factorization through $A_m^n$ explains the vanishing for $m<n$ under condition a). For a divided-power ideal $J$ of $S$ and $t\in J$, the example takes a quotient of $\Gamma^*(\Phi_{*S})\otimes_S\Lambda^*\Psi_{*S}$ by the divided-power relation involving $T-t$. It produces Stokes–De Rham integrals with values in $S$.

**70 and 72 · From sheaves to singular cochains.** Scan 70 specifies a resolution $\Omega^*$ of $k_X$, a choice $S(X)'$ of singular simplices with a local homology condition, and a map to $A_n^*$ from the direct limit of sections over neighborhoods of each simplex’s support. A restriction square expresses compatibility. On scan 72 these data give a map to the chosen singular cochain sheaf. The cube compares its global sections, the full singular cochains and derived global sections. The author identifies the bottom face as the derived image of a square of isomorphisms.

**71 · Reused typescript, IX, p. 140.** Lemma 11.6.8 extends the generic-fibre identification $ {}_n\Psi_K\simeq\underline M_{nK}$ to an open immersion $ {}_n\Psi\hookrightarrow\underline M_n$. The argument examines the special fibre to establish étaleness and the kernel to obtain a monomorphism. The page then defines $ {}_n\Phi$ as a quotient and starts describing it as a finite open subscheme.

**73 · Reused typescript, IX, p. 139.** The preceding typed page occurs later in scan order. It expresses (11.6.2) in terms of compatible finite-level isomorphisms with $\ker\widetilde u_n$. It introduces a filtration of $ {}_nA$ using fixed and toric parts, defines $ {}_n\Psi$ as the quotient by the fixed part of $ {}_nA^{\mathrm o}$, and gives its generic fibre. This is the quotient used at the head of typed p. 140.

**74 · The bigraded resolution and its kernel.** Starting with $\Phi_{*k}=i_{0*}(k)$ and its section $T$, the author takes the tensor product of the divided-power and exterior algebras of $\Phi$. Each positive total degree gives an exact sequence. With $\bar T=dT$, exterior multiplication defines a kernel in bidegree $(p,q+1)$. The page expresses this kernel, called $\mathrm{DR}^{pq}_*$, as $\Gamma^p\Phi_\bullet\otimes\Lambda^q\Psi_*$ for $\Psi_\bullet=\Phi_\bullet/k_\bullet$.

**75 · Exactness after taking sections.** The maps $i$ and $u$ give a short exact sequence with middle term $C_*^{p,q+1}$. Passing to sections, (A) records $C^{00}=H^{00}$ and the vanishing for $pq\ne0$. Statement (B) gives an exact sequence under multiplication by $\bar T$ for $p>0$. For $p=0$ the final display gives zero in degrees $n\leq1$ and $H^{n-1}(X_*,k)$ in degrees $n\geq2$.

**76 · Products involving the image of $u$.** The margin identifies $\operatorname{Im}i=\ker u$ and $i\circ u$ with multiplication by $\bar T$. Condition (C) sets $i(x)i(y)=0$. Two formulas characterize multiplication when either input belongs to $\operatorname{Im}u$. The page discusses why $i(x)y$ belongs to the kernel and depends only on $x$ and $u(y)$.

**77 · Divided powers and the remaining operations.** The author defines divided powers on the image by $u(x)^{(i)}=u(x^{(i)})$ and considers how the expression changes when $x$ is replaced by $x+y$ with $u(y)=0$. Condition (D) asserts vanishing of the relevant divided powers on the kernel. The surviving version of (E) lists products and divided powers in first degree zero, along with the need for the usual axioms.

**78 · Choosing sections.** The page asks for canonical splittings for $p\geq1$ and observes that $q=0$ is immediate. For $p=q=1$ it writes out the sequence and identifies a Hom group with zero using $\Psi_0=0$. It concludes « donc splitting unique », gives the direct sum, and ends by introducing a map $s$.

## Statements left without proof

| Scan | Words on the page | Claim or step left open here |
|---|---|---|
| 64 | « est une résolution de $F$, laquelle est d'ailleurs flasque » | The marginal verification request concerns flasqueness. The later cohomology and hypercohomology identifications use the resolution. |
| 67–68 | « est déterminé par la connaissance de » and « il existe un unique hom de complexes » | Under the listed hypotheses, $K_0$ extends exactly when it annihilates the indicated boundaries. The pages state the criterion and universal quotient without giving an inductive construction. |
| 69 | « c'est une résolution de $S$ » | The example invokes this resolution property when it constructs the $S$-valued integrals. |
| 70 | « alors … est une résolution de $k$ » | The margin asserts the resolution property for the chosen singular cochain sheaf, as for the full sheaf. |
| 74 | « qui est une résolution de $k$ » and « on trouve une suite exacte » | The positive-total-degree sequence is displayed. The text also asserts that its terms are flasque. |
| 75 | « le noyau … est flasque » and « est une suite exacte si $p>0$ » | The first assertion is used to pass to sections. The $p=0$ result follows on the sheet after the identification of a flasque resolution. |
| 78 | « est un $k$-Module projectif » | The existence of a splitting is inferred from projectivity for $p\geq1$. No argument for projectivity appears here. |

## Questions and conjectures

| Scan | Author’s words | Object of the question |
|---|---|---|
| 64 | « à vérifier ce point » | The arrow points to « flasque ». |
| 69 | « dont il faudrait étudier les propriétés multiplicatives » | What multiplicative properties do the integrals in the divided-power example have? |
| 78 | « trouver des splittings canoniques » and « On veut un choix simple. » | The question mark is on the proposed section in the upper diagram. The page reaches uniqueness in the first case $p=q=1$. |

## Slips

| ID and scan | As written | Possible correction and reason |
|---|---|---|
| S1 · 64, cohomology display | $C^*(X_*,F]$ | A closing parenthesis would match the opener. The square-looking stroke precedes a separate outer closing sign. |
| S2 · 68, first kernel test | $K_0(\partial_1(\operatorname{Ker}(A_1^0\to A_1^1))=0$ | A further closing parenthesis before the equals sign would balance the three opening signs. |
| S3 · 71, proof of 11.6.8 | « et comme $ {}_n\Psi$ donc ce noyau est séparé » | A predicate after $\Psi$ appears to be missing. The printed sentence gives too little to restore its exact wording. |
| S4 · 73, before (11.6.4) | « où des isomorphismes canoniques » | Likely « ou » because the author offers two equivalent ways of giving (11.6.2). The grave accent is visible on the typescript. |
| S5 · 73, after (11.6.4) | « comptatibles » | « compatibles » fits the phrase about transition morphisms. The extra first t is visible between p and a. |
| S6 · 73, below (11.6.5) | « du schéma en groupe » | Likely « en groupes », the form on two other lines of this page. Here the space follows e. |
| S7 · 78, last line | $s$ has target $\Phi_*\otimes\Phi_*$ | Low confidence as a slip. The middle term of the preceding sequence has $\bar\Phi_*$ in the second factor. An omitted bar or a change of notation would account for the difference. |

## Pointers

| Scan | Words or reference on the page | What they refer to |
|---|---|---|
| 66–69 | « condition de Stokes », « syst. de Stokes-De Rham », « intégrales de Stokes-De Rham » | Names attached to the square, the system of maps and the integrals. Scan 67 also has a cancelled « sous les conditions de la prop. 1 ». |
| 70 | « p.ex. complexe de DR sur $X$ variété $C^\infty$ » | The geometric example of a differential sheaf resolving $k_X$. |
| 71 | « pro-groupe de Barsotti-Tate », « La première des relations (5.5.8) », « (11.6.6) », « par (11.6.7) », « (3.1.3) », « (EGA IV 17.9.1) » | The typed lemma draws on the generic-fibre identification, the criterion used for the kernel, and the open-immersion result. |
| 72 | « Cartan » and « homot. … fin » | A label on the cube attributes a property of the full singular cochain sheaf to Cartan. The abbreviated qualifier is retained in the transcription. |
| 73 | « (11.6.2) », « (2.2.1) », « partie fixe (2.2.3) », « partie torique (5.1) », « (11.0) », « vu dans 6.1 », « SGA 3 … 3.2 et … 9.2 » | The typed page gives internal references for quasi-finiteness, the parts of the filtration, and the completeness and henselian hypotheses. The final references are to $\mathrm{VI}_A$ 3.2 and $\mathrm{VI}_B$ 9.2 for the quotient. |

## Remarks of the model

**R1 · Scans 74–75 · High confidence.** The degree bookkeeping agrees across the two pages. Adding the indicated differential degree $(-1,+1)$ to the degree $(1,0)$ of $T$ gives $(0,1)$ for $\bar T$. Multiplying by this element therefore takes the source degree $(p,q+1)$ in the kernel display to $(p,q+2)$. This checks the first kernel display without deciding the doubtful exponent in its repetition below.

**R2 · Scan 78 · High confidence, conditional on the displayed vanishing.** The Hom group on this page is exactly the group in which the difference of two sections takes values. Its source is $\Phi_*\otimes\Psi_*$ and the kernel is identified with $\Phi_*$. With a section already supplied by projectivity, vanishing of this group gives the stated uniqueness. This check takes the page’s Hom identification and existence assertion as premises.
