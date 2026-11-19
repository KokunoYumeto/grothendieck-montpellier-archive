# Mathematical notes on cote 157-5, scans 069–084

## What the pages do

**069 · End of 3.3 and Lemme 3.4.** On cofibrant diagrams the argument writes $f=pi$, with $i$ a trivial cofibration and $p$ a left inverse to a trivial cofibration $j$. It follows the images of all three arrows to show that $u_!$ preserves the indicated weak equivalences. Lemme 3.4 says that including the cofibrant objects $M_c$ in $M$ induces an equivalence after localization. The lemma is applied to a diagram category here. Its own proof is deferred.

**069–071 · Corollaire 3.5.** The question is whether the constructed $u_!^W$ is left adjoint to the localized restriction $u_W^*$. For Artinian ordered sets the corollary gives two alternatives, Noetherian $\mathrm{Esp}(I)$ and $\mathrm{Esp}(I')$, or stability of $C$ and $TC$ under transfinite composition. It also requires $u^*$ to preserve cofibrant diagrams, as happens under the stated local cofilteredness condition. The ordinary adjunction on those diagrams then passes to the localizations.

**071–072 · Remarque 3.6.** A full $C_0\subset C$ can suffice to construct both localized functors and still leave the adjunction in doubt. Take $C'=C$, both original functors the identity, $W'$ the isomorphisms, and $W$ all arrows. Restriction becomes the canonical functor $C\to\Pi C$. When $C$ is 1-connected and $e$ has only the identity endomorphism, the author takes $C_0=\{e\}$. The proposed adjunction would force $e$ to be initial. An example with a final object that is not initial gives the objection to Anderson.

**073 · Théorème 3.7.** For an increasing map of Artinian ordered sets, the theorem gives the adjunction without the separate condition on $u^*$ in 3.5. An insertion requires the category with cofibrations to be stable under finite colimits. Alternative (a) assumes the two associated spaces are Noetherian. Alternative (b) assumes transfinite composition for $C,TC$ and small filtered colimits in $M$. The word “petites” is inserted in (b).

**073–075 · Mapping cone and Lemme 3.8.** The factorization $u=vw$ has a closed immersion $w:I\to C(u)$ and a retraction $v:C(u)\to I'$. The gluing bifunctor is $H(i',i)=\mathrm{Hom}_{I'}(i',u(i))$. The insertion below it identifies this set with the corresponding hom-set in $C(u)$. In the category under $i'_0$ the morphism condition is a commuting triangle with sides $\alpha,\beta,\gamma$. At $\alpha=\mathrm{id}_{i'_0}$ it becomes $\gamma=\beta$. This gives the displayed initial object and the cofilteredness property used for $v$.

**075–077 · Completion of 3.7.** The hypotheses on the ordered sets pass to the cone, and 3.5 applies to $v$. For $J=C(u)$ the fibre calculation gives $w_!X(j)\simeq X(j)$ on $I$ and $w_!X(j)\simeq\varnothing_M$ on $J\setminus I$. This allows $w_!$ to pass directly to the localizations. The proof combines the adjunctions for $w$ and $v$.

**077–078 · Corollaire 3.9 and 3.10.** On $\mathrm{Diag}_0$ the predérivateur satisfies Der 1, 2, 3, 4 bis, 5 bis and 6. Here $\mathrm{Diag}_0$ consists of the Artinian ordered categories with Noetherian associated space. With the transfinite composition hypothesis the corollary uses $\mathrm{Diag}$, dropping that last restriction. The two leaves both use the label Der 6. On 077 it concerns $W$-cocartesian squares. On 078 it concerns $W$-cartesian squares. For the remaining assertions about $u_*$ and squares, 3.10 proposes a dual fibration structure $(M,W,F)$ sharing the same $W$. It compares the conditions relating $C,F$ in a Quillen structure, including the two factorization pairs $(C,TF)$ and $(TC,F)$, with the axioms attributed to K.S. Brown.

**079–081 · Arbitrary targets and Anderson’s argument.** The fibre formula for $u_!$ on cofibrant diagrams reduces compatibility with localization to the case $I'=e$, by replacing $I$ by $I/i'$. This permits an arbitrary target in the construction. The adjunction still presents a difficulty because the cone for such a target can fall outside the ordered categories equipped with the preceding cofibration structure. Grothendieck objects both to assuming an adjunction for locally finite orders and to assuming that a fully faithful restriction stays fully faithful after localization. He invokes his example 3.6 a second time.

**082–083 · 3.11.** Strictness asks for a functorial choice in the factorization axiom Cof 3. The comparison with factorization in $M(I)$ uses the fibrewise classes $W(I),C(I)$ and explicitly distinguishes $C(I)$ from $C_I$. A smallness qualification follows the inserted $\pm$. The author prefers to define strictness through stability. He describes what a derivator relative to the indicated category of shapes means for $u_!$, also after passage to the induced $\mathbb D_Z$. The square on 083 expresses the corresponding fibrewise base-change isomorphism.

**084 · Beginning of §4.** The new hypotheses concern filtered colimits in $M$, accessibility of its objects, the conditions Cof 1 and Cof 2 in the margin, and transfinite composition for $C$ and $TC$. A cancelled version already places $TF$ inside $W$. The live definition sets $TF=C_*\subset\mathrm{Fl}\,M$. The asserted factorization $f=pi$, with $p\in TF$ and $i\in C$, assumes a small $C_0\subset C$ with $C\subset\widetilde{C_0}$, expressed also as $TF=(C_0)_*$. The leaf ends with the further hypothesis $TF\subset W$ and a comma.

## Statements left without proof

- **069.** For Lemme 3.4, “Nous donnerons la démonstration” is followed by a difficult parenthetical reference and “ultérieurement”.
- **071, 075.** Cofibrancy under restriction is asserted for the case “si $u$ est loc. […] cofiltrant”. Later the proof appeals to “les hypothèses faites sur $I,I'$ se transportent à $C(u)$”. These statements enter the argument without separate proofs on these leaves.
- **078.** “On va […] les obtenir en principe” announces the use of the dual fibration structure for the outstanding axioms.
- **079.** The claim that the inverse image along the indicated étale slice projection is cofibrant is referred to “(cf. 3.2. a)”.
- **082–083.** “Il revient” with inserted $\pm$, followed by “au moins si”, qualifies the equivalence of the two factorization conditions. “On voit alors que le prédérivateur” introduces the relative derivator assertion, subsequently explained by its behaviour under products.
- **084.** The margin refers Cof 3 onward with “Pour Cof 3, cf plus bas.” The sentence “c'est le cas si la structure provient d'une structure de Quillen close” asserts transfinite stability in that case. For $f=pi$ the source is “il résulte du th. de factorisation”.

## Questions and conjectures

- **069–071.** “Il se pose la question si” asks about the left adjoint in (3.3.1). Corollaire 3.5 answers under its extra hypotheses.
- **079–080.** “il reste le pb de les construire pour une flèche […] quelconque” concerns general arrows of $\mathrm{Cat}$. Even after constructing the functor with an arbitrary target, 080 returns to “la perplexité si le foncteur (3.3.1) ainsi construit est bien un adjoint à gauche”.
- **080–081.** “il semblerait qu'on soit pratiquement paralysé” concerns the missing diagram cofibration structure. Even granting adjunction, “il n'est absolument pas clair” that localized restriction is fully faithful.
- **083–084.** “je ne vois aucun moyen de prouver l'existence” concerns $u_!$ for all arrows. “On voudrait […] dégager des conditions” asks for Der 4 bis and Der 5 bis in that generality, including the calculation of fibres.

## Slips

| Scan and TeX line | As written | Possible intended form and grounds |
|---|---|---|
| 079 L6 | The opening shaft has $I'$ on its left and $I$ on its right. | Low confidence. The subsequent functor and fibre formulas suggest $u:I\to I'$. The head on the opening shaft is uncertain. |
| 081 L10 | The restriction symbol has $W$ high and a small crossed sign low. | Low confidence. $u_W^*$ would agree with the adjacent occurrences. The crossed sign itself is uncertain. |
| 081 L19 | The parenthesis beginning “(i.e. si” closes after $C=C'$ with a square bracket. | Medium confidence. A closing round parenthesis would match the opening one. |
| 084 L30, L36 | Both live displays carry (4.1). | Medium confidence. (4.2) for the factorization display would give consecutive numbering before (4.3) and (4.4.). Both live digits read 1. |

## Pointers

- **069–071, 073, 075–080.** The internal references include “3.3”, “du th. 3.1”, “du lemme” or “le lemme précédent”, “(3.3.1)”, “notamment 3.5.” and “(cf. 3.2. a)”. The reference in the promised proof on 069 is doubtful. The raised functor in the corollary on 071 also has a doubtful numerical reference.
- **072, 080–081.** Anderson is named with the English words “it is clear that …” on 072. On 080–081 the “démonstration” attributed to him is discussed against “Le contre-exemple 3.6.”
- **075.** “le mapping-cone défini p.ge 60” points to manuscript folio 60, scan 073.
- **078, 082, 084.** “p. 39” refers back to the earlier axioms. On 078 the comparisons name “Quillen” and “l'axiomatique de K.S. Brown”. Quillen recurs on 084.
- **084.** The factorization theorem has a reference read tentatively as “X §1”, with a cancellation at the section sign. The marginal “cf plus bas” points forward within the argument.

## Remarks of the model

- **Model remark R3.6-2pt · high confidence · 072.** The order $0<1$ supplies the distinction between final and initial objects used here. Enumerating the hom-sets gives sizes $1,1$ into $1$ from $0,1$, and sizes $0,1$ out of $1$ to $0,1$. This checks the terminal-object example at the level of the ordinary category.
- **Model remark T3.8-id · high confidence · 074–075.** The two routes in the drawn triangle give $\gamma\circ\alpha=\beta$. Substituting the identity for $\alpha$ leaves $\gamma=\beta$. The check was limited to that substitution.
- **Model observation · high confidence · 083 L7, L15.** The prose writes $\mathrm{id}_Z\times u$. The square labels its left side $u\times\mathrm{id}_Z$ and puts $Z$ as the right factor in both objects. Each order is legible in its own place.
