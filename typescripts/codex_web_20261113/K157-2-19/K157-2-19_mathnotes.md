# Mathematical notes on scans 291–306

The manuscript numbers are 32–47. References of the form L18 give a line in the frozen TeX file for the scan. Statement identifiers also appear in CHECK_EVENTS.tsv.

## What the pages do

**U1 · Scan 291.** A map out of an oriented interval is decomposed into its restrictions to the ordered critical subintervals. Consecutive restrictions must agree at the shared endpoint. The first and last restrictions must also preserve the outer endpoints for the result to be a morphism of intervals. Dropping this last condition gives the corresponding description of functors.

**U2 · Scans 292–293.** The image of a critical subinterval on which a functor is nonconstant lies in a unique critical subinterval of the target. For an increasing functor the two signs agree. Applying this to successive critical vertices $s_i$ shows that every target critical vertex between $f(s_i)$ and $f(s_j)$ is reached by an intermediate critical vertex. In particular, an interval morphism reaches every critical vertex of its target in this way.

**U3 · Scan 294.** The opposite inclusion can fail. In the two-row example the middle two vertices of the alternating source both go to the middle vertex of the direct target interval. That target vertex is noncritical.

**U4 · Scans 294–296.** Each source critical interval on which $f$ is nonconstant determines a target critical interval. The image is a segment in the order on critical intervals. The notes describe this segment using the outer endpoint images. For an interval morphism the assignment is surjective. In the increasing case the numerical *portées* of the source pieces add up to the target length. A reduced target gives a bijection on the selected critical intervals. A cancelled draft about transition arrows continues across the break between 296 and 297.

**U5 · Scans 297–299.** For a reduced target each selected critical interval contains exactly one transition arrow with nonidentity image. These arrows correspond to the target transition arrows in their order and with their signs. Proposition 8 classifies maps to a fixed reduced type by the ordered subsets of source transition arrows whose signs spell that type. Taking a one-arrow target gives the two displayed descriptions of positive and negative transition arrows by Hom sets.

**U6 · Scans 299–302.** To obtain contravariance for an arbitrary target, Grothendieck uses the *portée ensembliste* of $f$ on a transition arrow. Consecutive distinct endpoint values $t_j$ partition the target. Each target transition arrow belongs to exactly one of these pieces, which selects a source transition arrow of the same sign. For a composite he compares the two ends of the three unit intervals. The inequalities on scan 302 give the required containment for the composite.

**U7 · Scans 302–304.** With the source type fixed, each transition arrow is given its numerical portée, with value zero on a degenerate image. The resulting function to $\mathbb N$ is unrestricted. Its positive support, in source order, gives the signs of the target factors. The positive values give their lengths. The map is constant across the groups of vertices joined by degenerate transitions. The construction on 304 specifies it on each remaining transition interval.

**U8 · Scans 304–306.** With the target fixed, $E'$ records the endpoints of images of nondegenerate source transition arrows. It contains the critical vertices of the target. Each $t_i$ in $E'$ carries the type $\tau_i$ of its fibre. The ordered fibres and the signs of the intervening target segments reconstruct the source. One source transition connects each consecutive pair of fibres, even when its image crosses several target edges. At $N=0$ only $\tau_0$ remains. The final page writes the source and target types, their lengths and a piecewise description of the vertex map.

## Statements left without proof

- **P1 · Scan 291, L21–26.** For the ordered family of critical subintervals he writes “dont $I_\tau$ est la somme amalgamée (on reviendra sur ce point …)”. The promised discussion of the sum does not appear in these sheets. The last word inside the parenthesis has a doubt mark.
- **P2 · Scan 292, L14, slanted lemma.** For a subset in which two elements are always joined by an arrow, the conclusion reads “dans un intervalle critique (unique si $\operatorname{Card}J\geq2$)”. The margin gives the assertion without a separate proof. The ending of the word read as *contenue* is uncertain.
- **P3 · Scans 294–296.** “L’image de $(*)$ … est un segment”, followed by “l’application induite … est … surjective” and “On a de plus, si $f$ est …” before the length sum. Corollary 2 states these assertions and describes the fibres. The pages give no separate derivation of the sum before using it for the bounds.
- **P4 · Scan 297, L11–14.** “On voit tout de suite qu’il existe alors une unique flèche de … transition … telle que $f(u)\ne\mathrm{id}$.” He invokes this observation about the surjection onto the one-edge interval to pass from critical intervals to individual arrows.

## Questions and conjectures

None expressly posed. The parenthesis on scan 291 defers a discussion and is recorded under P1.

## Slips

**S1 · Scan 292, L20–24.** The constant-functor parenthesis says that if its value “n’est pas une extrémité” there are “exactement deux intervalles critiques” through which it factors. The generality of this wording admits the direct target drawn on scan 294. Its interior vertex $1$ lies in a single critical interval. **S1a** is the narrower two-interval case, where the value is an interior critical vertex common to consecutive critical intervals. Confidence in this proposed missing qualification is low. The example tests the mathematical wording.

The remaining entries are reading questions. All proposed slips in this list have **low confidence**.

| ID | Scan and line | Frozen reading | Possible correction and reason |
| --- | --- | --- | --- |
| S2 | 293, L26–28 | $I_{\tau'}$, with $I_\tau$ also marked | $I_\tau$ would contain the source vertices $s_i,s_j$. The next line takes their images under $f$. The high mark after the type is faint. |
| S3 | 295, L35 and L41 | $J$, alternative $J'$ | $J'$ would name the target interval in the inverse images. Earlier $J$ denotes its preimage. The same unprimed singleton recurs at the top of 296. |
| S4 | 298, L20 | “un ens. de totalement ordonné” | Omitting the doubtful *de* would agree with “ens. tot. ordonnés” a few lines later. The compressed group remains visible. |
| S5 | 299, L17 | $u_1$, also read as $v_1$ or $i_1$ | $i_1$ would begin the increasing list of indices $i_2,\ldots,i_{n'}$. The ink resembles a rounded letter more closely at this spot. |
| S6 | 300, L6 | $\mathrm{Tr}^-(\tau_1)$ at the end of the second row | $\mathrm{Tr}^-(\tau_2)$ would have the same target index as the plus row and the combined map immediately below. |
| S7 | 302, L18 | $gf(u)$, alternative $gf(i)$ | $gf(i)$ would compare the upper endpoints, in parallel with $gf(i-1)$ directly above it. The short letter itself can be read as $u$. |
| S8 | 305, L44 | $l_i=t_i-t_{i-1}$, followed by a sign read as $\ne1$ or $\geq1$ | $\geq1$ follows from the strictly increasing list. A stroke crosses the relation on the page. |
| S9 | 306, L50–53 | The displayed outputs read $l_2$ and $l_i$. | The second target vertex would be $t_2=l_1+l_2$. The last row's endpoints involve $\lambda_{i+1}$, which suggests $t_{i+1}$ if the row describes that fibre. Both the right-hand symbols and the indexing of the final interval deserve review. |

## Pointers

- **Scan 294** uses “via la prop. 7” for the unique receiving critical interval. The proposition is restated at the foot of 292 and continues on 293.
- **Scans 297, 298 and 300** refer back by “plus précis que le cor. 4”, “(cor. 5)” and “Dans le cor. 5 plus haut”. These references connect the reduced-target bijection with the later definition for an arbitrary target.
- **Scan 302** returns to “le cor. 1 plus haut”, the signed Hom bijections on scan 299.
- **Scan 304** says “donné par $(*)$” while describing the factor of the reconstructed target. The product on 303 is a possible referent. Its label is uncertain. A separate insertion on 304 says “cf page 41”, the handwritten number on scan 300 where the critical vertices for $f$ were named.
- **Scan 306** says “la formule $*$, ci-dessus”, referring to the source-type formula near the top of the same page. The later target-type formula has the label $(*')$.

## Remarks of the model

- **R1 · Scans 293–294. Model remark, high confidence.** Reading the four downwards arrows of the example in order gives the vertex map $(0,1,1,2)$. The three source arrows have images $0\to1$, the identity at $1$, and $1\to2$. This explains how all target critical vertices can be reached even though two source critical vertices go to a noncritical vertex. The computation uses the diagram independently of the doubtful form of its upper-left capital.
- **R2 · Scan 302. Model remark, high confidence for the finite check.** For all nondecreasing maps between vertex intervals of lengths one through three, the two displayed containment hypotheses selected 3,646 triples of unit intervals, counted with their maps and interval lengths. Every selected triple satisfied the composite endpoint comparisons when the upper endpoint was read as $i$.
- **R3 · Scans 305–306. Model remark, high confidence in the arithmetic, low confidence in S9.** With successive target lengths $2,1$, the vertex list is $0,2,3$. Thus the second length and the second endpoint already differ in this small example. It distinguishes two possible meanings of the letters at the right edge of scan 306.
- **R4 · Scans 302–306. Model remark, medium confidence.** For a fixed source, positive weights locate the transitions that survive. For a fixed target, the fibre types retain the intervals collapsed between those transitions. This follows from comparing the reconstruction instructions in the two sections. The symbols $E$ and $E'$ range over different sets there.
