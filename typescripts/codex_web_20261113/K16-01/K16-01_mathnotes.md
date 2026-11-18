# K16-01 · Mathematical notes

## What the pages do

**Grading by projectors (003–004, §§1–2).** For a finitely graded module, the degree-$i$ projector is $\pi_i$. Multiplying an endomorphism on its two sides by projectors extracts a component $\pi_j u\pi_i$. Summing those with $j-i=\nu$ gives its degree-$\nu$ part. The sheets then give the idempotence, orthogonality and unit-sum conditions that let one repeat this construction in an abstract ring.

**Recovering the projectors (004–006, §3).** The family is required to vanish outside $[0,2n]$. Assuming the projectors beyond both ends of a shorter interval are known, Grothendieck isolates the corner $\pi_{2n-i}E\pi_i$. Its left and right annihilators in the centre of the degree-zero ring are used to recover the two endpoint projectors.

**Sufficient conditions on maps (006–007, §4).** On a module, an intersection of kernels and a sum of images give criteria for the two annihilator conditions. A map inducing an isomorphism between the complementary degrees gives both criteria. The two identities (4.4) express a pair of inverse maps on the specified components in the language of the graded ring.

**Existence inside a subring (008, §5, sheet 5 bis).** The projectors are initially in a larger graded ring $F$. Cutting $v_i,w_i$ down by the two truncating projectors gives two elements in $E$. Their products in the two possible orders yield $\pi_i$ and $\pi_{2n-i}$, the step in the outside-in induction.

**The Lefschetz condition and primitive pieces (007, 009, §6).** The argument resumes from the foot of 007 with a degree-two $L$. Its powers are required to identify complementary degrees, and (6.2) asks for their inverses to come from $E$. The notes express this with $w_i$, recall the primitive decomposition and name the refined projectors $\pi_{i,\alpha}$.

**The theorem (010).** Conditions (i)–(iii) compare the isomorphisms and their inverses, the identities of (6.3), and membership of the degree-minus-two operator $\Lambda$ in $E$. The consequences concern the refined projectors and the uniqueness of the grading projectors. A further item (vi) and its two equations are struck through.

**Induction on the refined projectors (011–012).** The proof advances inward on $i$ and descends on $\alpha$. The cutoff $q_{i,\alpha}$ removes terms already known. Formula (6.9) expresses $\pi_{i,\alpha}$ using $L$, the inverse $w_{i-2\alpha}$ and this cutoff. Formula (6.10) transports the result to the complementary degree.

**Recovering the lowering operator (012–013).** Formula (6.11) separates $\Lambda$ into its actions on the refined projectors. Formulas (6.12) and (6.13) give the actions on the two halves of the grading. A separate proposed converse ends with the request for a proof.

**Relations (013–014).** The remark collects eight identities under (6.14), with the aim of determining $\Lambda$ and the refined projectors from $L$ and the original $\pi_i$. The two identities of (6.15) are proposed in place of the final four. A question then asks for a presentation involving the operators alone.

**Exterior-algebra model (014–015, §7).** The model starts with a free module of rank $2n$ over $\mathbb Z$, an alternating form and its dual. Exterior multiplication and contraction define its two operators. They generate $\Phi_0$. The next sheet gives candidates for a basis, separate formulas for raising and lowering, and a rule for multiplying two basis elements.

**The homomorphism from the model (015–016).** A proposition relates the Lefschetz condition and $\Lambda\in E$ to a graded homomorphism $\Phi_0\longrightarrow E$ with prescribed images of $L_0$ and the degree projectors. Its proof invokes the product table in one direction and applies the map to the two complementary inverse identities in the other. The last paragraph invokes simultaneous characterization to address uniqueness.

## Statements left without proof

- **006, §3.** “dans un anneau commutatif, un idempotent est connu quand on connaît son annulateur.” The text uses this fact to identify a projector from an ideal.
- **009, before (6.4).** “Nous avons vu comment … cette condition implique la décomposition de $M^*$ … de morceaux primitifs”. The primitive decomposition is recalled here.
- **010, (6.5).** “défini par” is followed by a brace and dots. The definition of $\Lambda$ is left blank at this location.
- **013, following (6.13).** “que (iv) implique (ii). Il suffit de prouver en fait que l'on a alors $\pi_i=\pi'_i$. Démonstration à fournir.” This is an explicit outstanding proof.
- **013–014.** “Voici un système de conditions déterminant de façon unique” introduces (6.14). “on peut d'ailleurs remplacer les quatre dernières par les suivantes plus simples” introduces (6.15). No separate proof of this replacement is given here.
- **014, foot.** The exterior model “satisfait à la condition de (6.1)” and its contraction is called “l'opération associée définie par (6.5)”. A small parenthesis after (6.1) remains unresolved. The assertion is given without a computation.
- **015, opening and middle.** “$\Phi_0$ est un module libre sur $\mathbb Z$” and “La multiplication des élémts de cette base ne dépend pas du choix” accompany a displayed family and multiplication rule. No independent proof of freeness or of this independence is written here.
- **004 and 015, marginal extensions.** “on peut remplacer $\mathbb Z$ par un groupe quelconque” concerns the grading group on 004. “$\mathbb Z$ peut être remplacé par n'importe quel anneau” concerns coefficients on 015. Neither margin gives an argument.

## Questions and conjectures

- **003–004, §2.** “A quelle condition les formules (1.3) définissent-elles … une structure d'anneau gradué ?” The answer starts “Il suffit que l'on ait les relations (1.1.)”.
- **004–005, §3.** “posons nous la question de l'existence et l'unicité d'une famille” of degree projectors. On 005 the author narrows the immediate question with “On s'occupera ici de l'unicité”. The inserted page 5 bis takes up existence.
- **014, after (6.15).** “Donner un système de … relations en les $\Lambda,L$ exclusivement”, then relations “exprimant les $\pi_i$ comme polynômes non comm en $L,\Lambda$ ou qui définissent $\Lambda$ en termes de $L$ et des $\pi_i$”. This is an explicit request for relations. No separate conjecture is labelled in the run.

## Slips

- **S01 · 004, line 13, medium.** The projections are said to be defined by (1.2.). Their displayed formula is (1.3)b on 003. The older number may have survived the renumbering there.
- **S02 · 004, line 13, medium.** “une graduation de $k$-module sur $E^{(\nu)}$” apparently means a grading on $E$. The ensuing direct sum has $E$ on the left.
- **S03 · 004, line 13, high.** “Noter aussi que (1.4.) que (1.4) reste valable” repeats the connective and reference. Deleting either occurrence restores the construction.
- **S04 · 004, line 29, low.** In $\sum_i\pi_{j+\nu}u\pi_\alpha$, the last projector varies with $\alpha$, so $\sum_\alpha$ appears intended. The first subscript on the other side of the equality is uncertain.
- **S05 · 005, lines 16–17, low.** Both complementary cutoff sums have $\pi_i$ under a sum over $\alpha$. The complementary-projector calculation favours $\pi_\alpha$ in each. The lower margin of the first summation sign is overwritten.
- **S06 · 005, line 13 and 008, line 8, medium.** The claim that only $\pi_n$ remains when $i=n-1$ needs both endpoints already known. The interval in the stated hypothesis still contains $n-1,n,n+1$. The one-projector complement applies at $i=n$, or after a separate step for the two endpoints.
- **S07 · 005, line 23, high.** The expression ending in $E\pi_\alpha\varphi_i$ has a trailing right parenthesis. The parenthesis around the degree shift already closes inside its subscript.
- **S08 · 005–006, across the page break, medium.** “l'unicité … de $u_i$, $u_{2n-i}$” appears to refer to $\pi_i,\pi_{2n-i}$. These are the unknowns named before the break. The following $u$ is a variable in the centre.
- **S09 · 011, line 16, medium.** “Pour prouver 6.8.” precedes the hypothesis (6.8). The announced target is (6.7′), and the descending step has conclusion (6.8′).
- **S10 · 011, line 35, high.** The last summand in the definition of $q$ has $\pi_{i,\alpha}$ although the bound variable is $\alpha'$. The apparently intended summand is $\pi_{i,\alpha'}$.
- **S11 · 012, line 9, high.** The map is labelled $L^{n-i-2\alpha}$, whereas its image on the same line has $L^{n-i+2\alpha}$. A degree check gives the displayed target $2n-i+2\alpha$ with the plus exponent.
- **S12 · 013, line 18, low.** In the remark, $\Lambda$ is placed in $E^{(2)}$. Scan 010 explicitly gives its degree as $-2$, so $E^{(-2)}$ appears intended. The exponent on 013 has no visible minus. The adjacent ring letter is marked.
- **S13 · 015, line 6, low.** The upper bound for the two power indices is $2n-i$. If they index the nonzero positions of a string starting in primitive degree $i$, the bound would be $n-i$. Powers of $L$ advance the degree by two and the complementary degree is $2n-i$.
- **S14 · 016, line 11, medium.** The multiplication table is called “donnée au nᵒ 6”. In the order of these sheets it stands in §7, on 015. A marginal proposal there explains why §6 might have been cited.

## Pointers

- **007, margin at §6.** “cf 5. v. p 5bis” points to the inserted sheet, scan 008.
- **009.** “en vertu des nᵒˢ 4, 5” points back to the annihilator and existence arguments. “Nous avons vu comment” introduces the primitive decomposition without naming a source.
- **014, beside the question.** “cf nᵒ 7 pour l'anneau $\Phi$ : système de relations …” directs the reader to the model on the same sheet.
- **015–016.** The margin on 015 says that the basis elements and their products “devraient être donnés au nᵒ 6”. Scan 016 cites “la table de multiplication … donnée au nᵒ 6, et dudit th. donné au nᵒ 6.” The theorem is on 010. The displayed product rule is on 015.
- **016, cancelled proof.** “Cf Proposition ci-dessous pour ce point” is part of the rejected argument. Its intended target cannot be identified securely in this run.
- **015.** “condition de … Lefschetz” names Lefschetz. The intervening deleted name is read tentatively as “Hodge”. The leaves give no bibliographic title, other cote or external page reference.

## Remarks of the model

**R1 · Model remark, high confidence, scan 011, definition of $q$.** Even after supplying the missing prime in S10, the two expressions for $q$ take their units in different rings if read as global endomorphisms. On $M^i$, the unit is $\pi_i$. On a separate degree the global unit remains nonzero and the truncated sum acts by zero. A three-component diagonal example distinguishes the two readings.

**R2 · Model remark, low confidence, scan 009, line 29.** The frozen candidates are $ni+\alpha$ and $n-i+\alpha$. The degrees in (6.4) support the second. Between $n$ and $i$ the ink does not separate a minus from the adjoining strokes. This is a reading question.

**R3 · Model remark, low confidence about the scope of the assertion, scan 014.** The unqualified integral reading of (6.1) already fails for a free module of rank four with the usual exterior product. For $\xi=e_1\wedge e_2+e_3\wedge e_4$ the alternating matrix has determinant 1, but $\xi^2=2e_1\wedge e_2\wedge e_3\wedge e_4$. Thus $L^2$ from degree zero to degree four is multiplication by 2. The small uncertain parenthesis after (6.1) matters to attributing the unqualified reading to the author. **R3a**, the narrower statement verified here, is that this particular map becomes an isomorphism when 2 is invertible.

**R4 · Model remark, medium confidence, scans 013–016.** The requirement that the homomorphism carry the degree projectors to the given ones is underlined on 016 and accompanied by “condition essentielle !”. The uniqueness paragraph uses exactly these prescribed images when it invokes the characterization on 013. The last digit of the written reference itself is uncertain.
