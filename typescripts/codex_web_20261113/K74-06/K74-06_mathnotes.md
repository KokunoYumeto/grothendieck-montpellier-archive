# Mathematical notes · K74-06

## What the pages do

**106. Local configurations.** A sheet of drawings compares isolated points, triangles, and stars of triangles. The captions count the triangles through a vertex. The slanting note characterises a centre as a point linked to every other point and discusses its uniqueness.

**107–108. Triangle symmetries and transitivity.** To a triangle $\underline t=\{a,b,c\}$ the author attaches an involution $\sigma_{\underline t}$. He gives its restriction to the triangle and a neighbouring set, characterises its fixed points, and writes its conjugate by an automorphism. The symmetry-generated subgroup $G^0$ is invariant. The next theorem concerns transitivity on arcs, vertices, edges and triangles. Its margin isolates the bitriangle at $c=1$.

**108–110. Moving linked points.** The first lemma joins points by one or two applications of triangle symmetries. The next asks for an element fixing $a$ and exchanging two points linked to $a$. Scan 109 strengthens the requested fixed-point condition and tries a construction using labelled triangles. After the cancellations, 110 changes notation, chooses an intermediate $u$, and uses two symmetries at intersecting triangles. Scan 113 continues the cancelled note at the foot of 110.

**111–115. Upper triangles and sections.** A corollary uses even products of symmetries and describes an action on upper triangles. The next lemma seeks a point $s_1$ which can be reached from $s$ and $t$ in the indicated way. The argument partitions two fibres into $B',B''$ and $A',A''$. The contradiction at the foot of 112 continues at the top of 114. A second lemma there exchanges vertices of two upper triangles. The corollary gives a product of four symmetries on 115. A stronger assertion involving six is cancelled.

**116. Counting pins and automorphisms.** The number of pinned triangles is identified with the number of arcs. It is multiplied by $2c^2$ to count pinned bitriangles. The page discusses $c=2$ and $c=1$ separately and divides the pinned count by 72 to count bitriangles.

**117. A cancelled group calculation.** Beginning with $xyz=1$, the author writes a map on triples and a condition on $a$. A group of exponent two leads him to additive notation. Two diagrams accompany remarks on the action of subgroups, stabilisers, and the sets above the triangle vertices. The long diagonal stroke passes through the calculation.

**118–120. Counts of incident structures.** The primed and unprimed $c_{\beta\gamma}$ count structures of type $\beta$ inside type $\gamma$, respectively with and without a pin. Two boxed identities relate these counts to an automorphism order and to the number of extensions of a smaller pinned structure. The last two sheets evaluate the factors and give one table for each count.

## Statements left without proof

| Scan | Author's words or formula | Status on these sheets |
|---|---|---|
| 107 | “est injective, et a comme image l'ens des autom involutifs … tels que … $\operatorname{card}S^u=3$”; “C'est $\pm$ évident…” | No separate proof of this characterisation follows. |
| 108 | “Sauf exception $c\,(=\operatorname{Card}E_a)=1$”; “d'indice $2$” | The marginal exception gives the group description and orbit behaviour without a calculation there. |
| 112 | “C'est faux si $c=1,2$” | The margin excludes these cases without giving a counterexample on this sheet. |
| 114–115 | “alors $\pi$ … échange $w_1$ et $w_2$”; “produit de $4$ … symétries” | The lemma and the following corollary state the exchange and product bound. There is no separate proof between this corollary and the new count on 116. |
| 116 | “un bitriangle épinglé est l'identité”; “simplement transitif” | In the $c=2$ note the first quotation ends the clause about an automorphism. Its verb is overwritten. The triviality of the stabiliser is asserted here. |
| 117 | “isom. au grpe des parties paires”; “est injectif” | Assertions in the cancelled group passage. The target in the final bracket is difficult to read. |
| 119 | “On trouve” | The three displayed extension factors are given without a local enumeration. Their numerical consequences can be checked without establishing their combinatorial derivation. |

## Questions and conjectures

**112.** After identifying the two parts of a partition the author writes “et sans doute cela impliquera $t=s'$, mais pour l'instant on ne peut le prouver”. He then looks for an intermediate $\bar s_1$ meeting both nonempty-intersection conditions. This is the one explicit conjectural implication in the batch.

## Slips

- **108, Lemme 2.** The conclusion introduces “$\exists\,g\in G^0$” and ends with “$u(a)=a,\ u(s)=t,\ u(t)=s$”. Using $g$ for the three occurrences of $u$, or introducing $u$ from the beginning, would give one name to the element. Medium confidence about the intended repair. The change of letter itself is visible.
- **116, second NB.** The subscript on the second symmetric group looks like 5 or 3. The expression one line lower has two subscript 3's, as does the related marginal expression on 108. If the first occurrence is 5, 3 is the apparent intended value. Low confidence because the numeral is doubtful.
- **120, the $c_{0,\gamma}$ line [S1].** After $1/72$ the manuscript repeats the unprimed $c_{0,\gamma}$. The relation on 118 and the two tables call for $c'_{0,\gamma}$. In the expanded expression an extra factor $(c_\gamma-1)$ also appears. The consistent expression is $c_{0,\gamma}=c'_{0,\gamma}/72=c_\gamma^2(c_\gamma+1)(2c_\gamma+1)/6$ [S1R]. At $c_\gamma=1$ the factor in the manuscript gives zero, while the two tables give $72/72=1$. High confidence for this discrepancy. The clean diagonal cell suffices for the comparison.

## Pointers

- **108.** “Résulte des deux lemmes suivants” points from the theorem and corollary to the ensuing lemmas.
- **108.** “donc (vu a)” and “d'où immédiatement b” are internal references to the parts of Lemme 1.
- **118.** “alors la formule (2) nous donne” refers to the boxed recursion earlier on the same page.

No person, separately titled paper, other cote, or dated work is cited on these sheets.

## Remarks of the model

- **Model [M1], high confidence for the numerical evaluation.** On 116, $12c^2(1+2c)(1+c)$ gives 72 and 720 at $c=1,2$. This checks the two displayed integers. The assertion about transitivity is a separate premise of the author's group-order interpretation.
- **Model [M2], high confidence for the table arithmetic.** The factors $1\cdot1,\ 2\cdot3,\ 3\cdot5,\ 5\cdot9$ at the left of 119 correspond to $c_\gamma=0,1,2,4$ in $(1+c_\gamma)(1+2c_\gamma)$. Using the listed successive extension factors reproduces the ten entries on or above the diagonal of the primed table. In column $\gamma=2$ they are $270,8640,25920,51840$. This numerical check uses the legible factors from 119 and does not determine the overwritten signs on 120.
- **Model [M3], high confidence for the division.** Dividing each row of the table on 119 by its own diagonal value, respectively $6,72,720,51840$, reproduces all sixteen cells on 120. In particular $25920/720=36$. The separately written polynomial in [S1] agrees with that row at $c_\gamma=2$ by coincidence, since $c_\gamma-1=1$ there.
- **Model [M4], low confidence about the author's intention.** The continuation at the top of 119 writes $N_\gamma=N_\beta N_{\beta\gamma}$. The cancelled lines immediately before it call $c'_{\beta\gamma}$ the index of the stabiliser. If those lines were intended as the premise, the corresponding factor would be that index. The earlier cancellation leaves the status of this argument unclear.
- **Reading question, 118, middle of the induction paragraph.** The frozen words include “cl|calcul”, “soit”, and “déduira|déduire”. The computation on either side suggests a sentence about deducing one count from the other. The crossed baselines leave the wording uncertain.
- **Reading question, 119, opening, line 2.** The frozen reading separated a short “un|le” from a raised wave. At the witness check the lower stroke and the wave could be read together as $\simeq$. The transcription records the raised element as an insertion. The ink alone leaves open whether the upper stroke was added later.
