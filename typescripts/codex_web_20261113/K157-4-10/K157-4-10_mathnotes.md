# Mathematical notes on scans 148–163

Scan numbers refer to the archive PDF. L numbers refer to the individual frozen page files. Identifiers in parentheses link observations to the accompanying check register.

## What the pages do

**Scans 148–149. Cardinal estimates.** Varying the ordered indexing set costs at most a factor of $2^{r^{\pi_0}}$. Scan 148 combines an estimate for objects over $X$ with a bound on each Hom set to count arrows in the slice. Scan 149 applies the same count to $M^r$, isolates an identity for cardinal powers, and gives two corollaries. The same upper bound $2^{r^{\pi_0}}$ occurs for a Hom set and for the isomorphism classes of arrows in the slice. The exponent and class name in the first corollary are hard to read. (U148, S149)

**Scan 150. Repetitions of generators.** A single isomorphism class may contribute arbitrarily many members of $C_0$. The condition called « non pléthoricité cardinale » bounds each family $C_0(i)$ of generators isomorphic to $i$. Together with the bound on the number of classes, it gives $|C_0|\leq 2^{r^{\pi_0}}$. The last estimate bounds the set $\Delta(C_0,f)$ that indexes the next construction. (U150)

**Scans 150–152. One step and its iteration.** Each $X_D$ is a pushout. Finite partial sums under $X$ form a filtered system indexed by the nonempty finite subsets of $\Delta(C_0,f)$. Under (3.13), Lemma 3.3 puts $X_1(C_0,f)$ in $M^{s'}$ for $s'=s^{r^{\pi_0}}$. For $s'=s^t$ as on scan 152, another application gives the same bound, so $p_1$ preserves the indicated class of arrows. The corollary passes to $p_\alpha$ for $|\alpha|\leq s'$. (U151)

**Scans 152–154. Théorème 2.** Starting from a cardinal filtration and a small family $C_0$ of arrows admitting the pushouts in question, the theorem summarizes the functorial factorization through $X_\alpha(f)$. The first map belongs to $\Phi$ for every $\alpha$. The second belongs to $\Psi$ for $\alpha$ sufficiently large relative to $r^{\pi_0}$. Part 2 specifies cardinal levels preserved by these functors. The proof refers back to the accessibility of the objects of $M^r$. (U153)

**Scans 154–155. Définition 4.1.** A Quillen *précouple* consists of two classes of arrows. A commutative square with left edge in $\Phi$ and right edge in $\Psi$ has a diagonal filler, and every arrow factors as $pi$ with $i\in\Phi$ and $p\in\Psi$. The text calls such a pair *clos* when its two classes are closed on their respective sides. (U154)

**Scans 155–157. Proposition 4.2 and two corollaries.** For a fixed $j$, the left closure, the left lifting condition and being a retract of an element of $\Phi$ give equivalent tests. The retract can have the same source. Its maps satisfy $qj=i$, $pi=j$ and $pq=\mathrm{id}_B$. The proof uses factorization of $j$ in its final implication. The corollaries identify both closures with retract classes and characterize closed pairs by stability under retracts. (U155)

**Scans 157–158. Two factorizations.** The text introduces a localizer $W$ containing the isomorphisms and satisfying two-out-of-three. The pairs $(C,TF)$ and $(TC,F)$ supply lifting and factorization axioms M1 and M2. M′ gives $TC\subset C\cap W$ and $TF\subset F\cap W$. The author singles out the missing stability axioms M3 and M4 and the M″ conditions involving $\mathrm{Fib}_W$ and $\mathrm{Cof}_W$. (U157)

**Scans 158–160. Proposition 4.3.** Conditions a) and a′) compare the intersections with the retract closures. Conditions b), b′), c) and d) prescribe factorizations using different combinations of the original and closed classes. All except d) are equivalent, and d) implies them. If either $TC$ or $TF$ is retract-stable, d) joins the equivalence. For c) ⇒ a), the lifting square exhibits $j$ as a retract of $i$. For a) ⇒ b), $p$ and $pi$ belong to $W$, which puts $i$ in $W$. The primed implications follow by duality. (U158, S159)

**Scans 160–161. Corollaries 1 and 2.** If $TC$ is retract-stable, the equivalent conditions amount to $C\cap W=TC$. If $C$ and $W$ are retract-stable, they amount to $C\cap W=\widetilde{TC}$. The dual statements concern $F\cap W$, $TF$ and $\overline{TF}$. (U160)

**Scans 161–163. Closing the two pairs.** Corollary 3 closes both pairs, assuming the equivalent conditions and retract stability of $W$. Formula (4.3.6) gives $C'\cap W=TC'$, $F'\cap W=TF'$ and $W=TF'\circ TC'$. The margin of 161 proposes a weaker hypothesis involving containment of the two retract closures and a condition on retracts in $C$ or $F$. On 162 the proof relates these formulas to a closed Quillen triple, assuming finite limits, finite colimits and moderate saturation. Scan 163 identifies the last requirement with M5. The sideways Corollary 4 on 162 lists four tests involving the two intersections, the composite $TF\circ TC$, and a closed Quillen triple. Its hypothesis has several layers of rewriting. (U161)

**Scan 163. Construction 4.4.** Given a small $C_0$ with $C_{0*}\subset W$, set $C=\widetilde C_0$, $TC=C\cap W$, $TF=C_*=C_{0*}$ and $F=(TC)_*$. The author invokes the earlier factorization for $(C,TF)$. He identifies the factorization for $(TC,F)$ as the remaining problem. Once it is available, Proposition 4.3 supplies the final relations. The first relation sign is doubtful. The second reads $W=TF\circ TC$. (U163)

## Statements left without proof

- **Scan 151, L30–32.** « ce qu'on peut toujours supposer, quitte à réduire » introduces the assertion that $C_0$ may be reduced while preserving $\widetilde C_0$ and $C_{0*}$. The reduction itself is left implicit.
- **Scans 152–154.** « On le voit aussitôt par récurrence transfinie » gives the method for the corollary on 152. The successor and limit cases are left implicit. Theorem 2 recalls « On a (pour mémoire) » before $i_\alpha(f)\in\Phi$. Its proof cites « les objets de $M^r$ sont $r^{\pi_0}$-accessibles (cf. 3.2) ».
- **Scan 154, L8–9.** A struck draft of a stability corollary breaks off at « lorsque $s$ est ».
- **Scan 159, L28–29.** The primed part of the implication diagram is justified by « en résultant par dualité ». The unprimed proof occupies 159–160.
- **Scans 161–162.** The lower margin of 161 says « on sait que cela implique qu'en fait » before asserting retract stability for $W$. The sideways note on 162 introduces Corollary 4 with « Il en résulte le » and « Les cond. suivantes sont équiv. » It gives no separate derivation of the four tests.
- **Scan 163, L32–36.** « on sait déjà que » introduces the appeal to the earlier theorem for $(C,TF)$. The other pair still requires factorization.

## Questions and conjectures

**Scan 150, L22–29.** « Il y a une difficulté idiote » introduces the possible multiplicity of arrows representing one isomorphism class. The condition on $C_0(i)$ answers this difficulty on the same page.

**Scan 163, L8–15 and L32–36.** « Voici l'idée pour construire » is qualified by $\pm$ and quotation marks around « toutes ». This expresses an aim about the scope of the construction. The specific open step is « Il faut la factorisation pour le couple » $(TC,F=(TC)_*)$. The extract ends with the consequences conditional on that step.

## Slips

- **S149, scan 149, L26–29. High confidence for the isolated statement.** The lemma assumes only « $r$ un cardinal, $r'$ un cardinal $\geq r$ » and asserts $r^{r'}=2^{r'}$. For $r=r'=3$, its sides are 27 and 8. A sufficient refinement (S149R) requires $r'$ infinite and $2\leq r\leq r'$. The finite counterexample concerns the literal wording. These pages do not settle the conventions in the earlier discussion.
- **S150N, scans 149–150. Low confidence.** The two corollaries on 149 carry (3.10.) and (3.11). On 150 a new hypothesis is tagged (3.10), and the multiplicity condition has (3.1…) with its last character overwritten. A fresh pair of numbers may have been intended. These leaves give no unique replacement.
- **S152, scan 152, L22. High confidence.** « ce qui qui revient au même » has two successive instances of *qui* in the crop. Reading the sentence with a single *qui* removes the repetition.
- **S156, scans 155–156. Low confidence.** Scan 156, L16 calls the solid-line diagram « le diagramme donné 4.2.2. ». The triangle on 155, L37–40 bears (4.2.3.), a plausible intended pointer. The preceding identities carry a doubtful final digit.
- **S159, scans 158–159. Low confidence as a slip.** Scan 159, L10–12 gives « b′) resp b) » after $TC=\widetilde{TC}$ and $TF=\overline{TF}$. In the live formulas on 158, L58–61, the first substitution makes **b)** identical to d), and the second makes **b′)** identical to d). This suggests the order « b) resp b′) ». The comparison depends on distinguishing cancelled overmarks from live ones.

## Pointers

- **Scans 148–150.** Scan 148 invokes « en vertu de (3.8) où on fait $s=r$ » to finish (3.9). Its slanted note ends in « 23 », the author's page number on scan 149. Scan 149 refers to « L'argument de la page 21 », to « 3.7. », and to (3.8) and (3.9). Scan 150 inserts « par (3.8) » at the bound for $\Delta(C_0,f)$. (P148)
- **Scans 151–154.** Lemma 3.3 invokes (3.10), (3.11) and (3.13). The transfinite construction on 153 has « cf. » followed by a doubtful abbreviation and « 1 ». « cf lemme 3. » has a doubtful final numeral. Scan 154 refers to « cf. 3.2 » and points ahead to « 31 », where scan 157 states the criterion for a closed pair. (P154)
- **Scans 155–161.** The proof on 156 names parts a) and b) of Definition 4.1. Scan 158 places the earlier axioms at « XIII p. 27 déf. 1 » and invokes « prop. 4.2 (cor. 1) ». Scans 159 and 161 cite its second corollary. An insertion on 160, L11 reads « prop. 3.2 » or « 4.2 », followed by $a\Rightarrow d$. Proposition 4.2 has those labels. (P160)
- **Scans 162–163.** Scan 162 names Quillen directly and uses the English words “closed model category”. Its proof cites (4.3.1), (4.3.2) and (4.3.6). Scan 163 refers to the « conditions du § précédent » and « le théorème de factorisation du § 1 (p. 10) ».

## Remarks of the model

- **R153, scan 153, L32–37. Model remark, low confidence about a missing hypothesis.** At L17 the frozen text calls $r$ « un ordinal », while the preceding statement formulates bounds for cardinals. An initial ordinal can represent a cardinal. At L32–37 the text permits the first ordinal of any cardinal $r'>r^{\pi_0}$ and gives the successor as an example. A larger cardinal can have small cofinality. The precise accessibility argument on the earlier leaves would determine whether the general choice needs a cofinality qualification.
- **R161, scan 161, L27–29. Model reading question, low confidence.** The frozen line puts $TC$ to the right of $C\cap W$ after a leftward or two-headed connector. If this is the lifting relation, $F$ would fit the pair $(C\cap W,F)$ expressly named in the margin of 158, L66. The shape of the connector is uncertain. The page file retains $TC$.
- **R162, scans 158 and 162. Model remark, medium confidence about the change of scope.** The margin on 158, L36 says « ni qu'il soit stable par composition ». At 158, L61–62 the equality in d) is expressly conditional on stability under composition. On 162, L29–35 the equality with both closed factors is introduced by « Comme par hypothèse on a ». The reverse inclusion at that point uses closure of $W$ under composition once both factors are known to lie in $W$. The localizer introduced on 157 supplies this property. How far the weakened marginal hypothesis was meant to extend remains open.
- **R162L, scan 162, L5 and L19. Model reading question, low confidence.** The frozen readings are $E'$ or $C'$ in the triple and $TP'$ or $TF'$ in the inclusion. The later explicit occurrences $(W,C',F')$ at L41 and $W\supset TC',TF'$ at L24 favour $C'$ and $TF'$. The earlier letters are ambiguous.
- **R163, scan 163, L32. Model reading question, low confidence.** The change from « deux » to « un » is clear. The frozen noun reads « problème » with a doubtful terminal *s*. The live article favours the singular. The noun ending is too slight to attribute an agreement slip to the author.
