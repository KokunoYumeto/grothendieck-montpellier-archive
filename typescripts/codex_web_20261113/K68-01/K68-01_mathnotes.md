# Mathematical notes on cote 68, scans 2–16

## What the pages do

**Scans 2–3 · Positions, plays and length.** A game has a set of positions \(C\), a successor relation \(R\), players \(J\), and an initiative function on nonterminal positions. The set \(G_0(j)\) specifies where a terminal position counts as a win for \(j\). A play follows \(R\). The notes distinguish terminal, infinite and circular plays, then construct \(C_i\) by testing every immediate successor against \(C_{i-1}\). The corollaries relate membership to bounds on lengths of plays and to a strictly decreasing natural-number rank.

**Scan 3 · Strategies.** At a position controlled by \(j\), a strategy \(\Sigma\) specifies a set of permitted successors, nonempty whenever a move exists. Winning from \(x\) requires every compatible play starting there to be finite and every compatible completed play to end in \(G_0(j)\). The page names the set of winning starts \(G(j)\).

**Scans 4–6 · Successors of a winning position.** Theorem 1 distinguishes a move controlled by \(j\), for which one winning successor suffices, from an opponent’s move, for which every successor must be winning. A lemma passes a winning strategy to a successor it allows. The converse at a \(j\)-move tries changing the strategy at \(x\) to the singleton \(\{y\}\). Scan 5 considers separately a possible return from \(y\) to \(x\). Scan 6 treats the other player’s move and explicitly assumes finiteness in the argument.

**Scan 7 · Cancelled construction.** A separate draft well-orders \(R(x)\), takes a least eligible successor \(y(z)\), and tries to use the strategy indexed by it. Along a play the selected successors form a decreasing sequence in that order. The draft breaks off after “pour \(n\) assez grand, on aura”. The whole page is cancelled.

**Scans 6, 8–9 · A strategy common to several starts (S4).** The corollary asks for the greatest strategy winning at every \(x\) in a successor-stable subset \(\Gamma\) of \(G(j)\). The live construction keeps all moves outside \(\Gamma\) and takes \(R(z)\cap G(j)\) at the controlled positions inside. The proof traces a compatible play and then compares each allowed set with that of any other strategy winning on \(\Gamma\).

**Scans 9–11 · Acceptability.** A coalition \(J'\) controls the union of its members’ positions. Its strategy is acceptable against a designated opponent when compatible completed plays avoid that opponent’s terminal wins. Theorem 2 identifies the positions acceptable against \(j'\) with the complement of \(G(j')\). One direction uses a play compatible with both proposed strategies. For the converse the manuscript constructs a strategy and starts to check it along the play.

**Scan 12 · Auxiliary two-player game.** The coalition becomes a single player, the successor relation stays the same, and the two terminal winning sets are complementary. Acceptability against \(j'\) is compared with winning for the coalition player. The absence of infinite plays is written in the margin beside this comparison.

**Scan 13 · Approximating the winning set.** Starting from \(G_0(j)\), the page iterates the test “some successor” at a controlled move and “all successors” at an opposing nonterminal move. It defines \(G_\infty(j)\) as the union of the stages, queries equality with \(G(j)\), crosses out an attempted argument, and finishes with an induction restricted to \(C_i\).

**Scan 14 · Section heading.** “Elimination des parties” ends with the inserted adjective “infinies” and the qualification “(cas \(C\) fini)”. There is no argument below the heading.

**Scans 15–16 · Calculations.** Scan 15 sets out expressions in \(V_1,V_2,V_3\), conditions on even- and odd-indexed \(E\)’s under translation by \(E_2\), and arrays in \(a,b,a',b'\). Scan 16 expands a product involving \(V_1\) and \(\{x\}\), puts strings of small integers alongside additive relations, and ends with another product. The introductory prose visible in the opposite orientation to the archive folio is cancelled and written in a different-looking hand.

## Statements left without proof

| ID | Scan | Words on the page | Extent of the argument |
|---|---|---|---|
| S1 | 2 | “S'il existe une partie circulaire, existe une partie infinie. L'inverse est vrai, si \(C\) est fini.” | The proposition is followed immediately by the construction of \(C_i\). |
| S2 | 2–3 | “tte partie … à partir de \(x\) est de longueur \(\leq i\)”; “Conditions équivalentes”; “si \(l=l(x)\), on a \(x\in C_l\)” | The length characterization, its union corollary, and the equivalence with a decreasing rank are stated. The later NB does give a short counting argument in the finite case. |
| S3 | 3–4 | “\(G(j)\cap C_0=G_0(j)\)”; “Plus précisément \(\Sigma\) est aussi \(y\)-gagnante.” | The first is an NB. The lemma on successors is followed by “Trivial sur définitions.” |
| S5 | 12 | “On … prouve par réc. \(x_i\in\bar G(j')\)” and “prouvons \(x_{i+1}\in\bar G(j')\)\(\ldots\)” | The induction is started, then the writer turns to the auxiliary game. |
| S6 | 13 | “On voit par récurrence sur \(i\)”; “et aussi \(G_i(j)\subset G(j)\)”; “On prouve par récurrence sur \(i\geq0\) … en utilisant le th. 1.” | The page states monotonicity, containment, and \(G_\infty(j)\cap C_i=G(j)\cap C_i\). It gives the induction and reference, without the steps. |

## Questions and conjectures

- **Scan 4.** “On va essayer de définir une \(j\)-stratégie \(x\)-gagnante”. A struck line above may end “à vérifier”; both words are doubtful.
- **Scans 4–6.** “S'il n'y a pas de partie infinie” stands beside theorem 1. The sloping note on scan 5 begins “Supposons donc d'abord que” and considers a compatible play returning from \(y\) to \(x\). Scan 6 says “admettons qu'elle est finie” and “On suppose qu'il n'y a pas de partie infinie”.
- **Scan 12.** The margin begins “s'il n'y a pas de”; the singular or plural ending of “partie infinie” is open. It qualifies the comparison with the auxiliary game.
- **Scan 13.** “? Th 3 \(G_\infty(j)=G(j)\).” The margin starts “Si \(C\) fini”, mentions the absence of an infinite play, and continues “Plus généralemt si \(C=\bigcup C_i\) cf § 2”. The attempted proof underneath is cancelled.
- **Scan 15.** The parenthesis after “ss-gpe” may end in a question mark or a numeral. Its lettering is too uncertain to identify a conjecture.

## Slips

| ID | Scan and place | Written form | Possible correction and reason |
|---|---|---|---|
| L1 | 2, sentence after the construction | “de d'ensembles” | One preposition would suffice. The first short group carries a doubt mark, so this remains a low-confidence reading question. |
| L2 | 6, opening and last line before the corollary | \(Y\in G(j)\); later \(\in C(j)\) | The preceding quantifier binds \(y\), and the induction is preserving \(G(j)\). Both letters are marked. Low confidence as slips. |
| L3 | 8, final complete paragraph | \(\Sigma(x_i)=R(z)\cap G(j)\) | Substitution into the earlier definition gives \(R(x_i)\). The next line also tests membership in \(\Sigma(x_i)\). High confidence. |
| L4 | 9, heading and last condition | “Stratégie acceptables”; \(G(j_1)\) or \(G(j_0)\), followed by \(G_0(j)\) | The adjective ending is visible in both halves of the heading; either the noun or adjective could have been meant to change number. The definition names \(j_0\) as opponent. Its disputed final index makes the index correction low confidence. |
| L5 | 10, paragraph before theorem 2 | A winning \(\Sigma'\) is introduced; the parenthesis calls \(\Sigma\) winning, and the terminal contradiction uses \(j\). | The coalition had \(\Sigma\); the hypothetical winning strategy for \(j'\) would be \(\Sigma'\). The terminal contradiction would concern \(G(j')\). Medium confidence for the unprimed player in the terminal contradiction. The parenthetical predicate carries a doubt mark, so the proposed strategy-name correction there has low confidence. |
| L6 | 11, first paragraph, second case and following identity | \(\bar G(j)\) in the opening; \(z\in\bar C(j')\) after “sinon”; \(\bar G(z')\) twice | Theorem 2 concerns \(\bar G(j')\). The complement of the first case \(z\in G(j')\) likewise uses \(G\). The position in the identity is \(z\), while the argument of the winning set is \(j'\). High confidence for the local substitutions. |
| L7 | 12, opening and auxiliary-game paragraph | “compatible avec \(\Sigma\)”; later “gagnante pour \(x\)” followed by a doubtful sign | Scan 11 introduces \(\Sigma'\), including just before the page turn, so a prime is plausible (medium). The sign after \(x\) could begin \(\in C\); the operand is absent and the proposal has low confidence. The separate “(pour \(\mathbb J\))” sits above the next line, with its leader after “contre \(j'\)”. |
| L8 | 16, cancelled earlier paragraph | “grassmaniennes” | The expected spelling is “grassmanniennes”. The crop shows a single n before i; because the paragraph is struck, confidence in attributing a spelling slip is low. Its writer is unidentified. |

## Pointers

| Scan | Words on the page | Referent |
|---|---|---|
| 4 | “cf NB plus haut” | The NB on terminal winning positions above the lemma. The reference itself is in a cancellation. |
| 6, 8–9 | “par 1°. et 2°)”; “par le 1°) de la prop.”; “lemme après la prop.” | The two successor cases and their lemma on the preceding sheets. |
| 11, 13 | “par la prop. 2°”; “(en utilisant la prop.)”; “cf § 2”; “en utilisant le th. 1.” | The successor tests and the earlier construction of \(C_i\) for lengths of plays. |
| 16 | “à la Bruhat”; “cycles de Schubert” | Names in the cancelled paragraph about decompositions of homogeneous spaces. It gives no bibliographical title or cote. |

## Remarks of the model

**R1 · Model remark, high confidence.** The distinction between finite plays and a bound on their lengths matters to scan 13. Consider an opponent’s start with one choice of a forced chain of each positive finite length, all ending in a win for \(j\). Every play ends in a win, but the start belongs to no finite stage \(G_i(j)\). The margin’s stronger condition \(C=\bigcup C_i\) excludes that start.

**R2 · Model remark, high confidence.** A cycle explains the force of the marginal finiteness condition in the greatest-strategy corollary. At positions \(x,y\), let \(j\) choose either the other position or a winning terminal. Five of the nine possible strategies win from both starts. Their union allows the endless alternation \(x,y,x,y,\ldots\), so there is no greatest winning strategy for both starts in this example.

**R3 · Model remark, high confidence for the finite check.** On all 25 acyclic successor relations on three labelled positions, the length filtration agreed with maximum play length. For all 200 assignments of terminal outcomes and initiative, the finite winning-set recursion agreed with exhaustive strategy evaluation at all three positions. The formula on scans 8–9 gave the greatest strategy for \(\Gamma=G(j)\) in all 200 cases. The included finite-check script reproduces these counts.

**R4 · Model remark, medium confidence.** Scans 15 and 16 share several \(V\)-expressions and strings of digits. Their notation makes them natural to read together. Neither sheet identifies an earlier game, a player, or a successor relation to which its arrays apply. Their mathematical connection to the heading on scan 14 remains open.


**Q15 · Reading question recorded after the witness check.** On scan 15, file line 39, the frozen reading is `E'_{2n}+\{x\}`. In `015-oddplus.jpg` a separate dark dot stands directly above the upright of the plus, with a gap between them. The alternative `E'_{2n}\mathbin{\dot+}\{x\}` fits the ink and the dotted-plus form on scans 15–16. The dot is distinct from the prime over the preceding E. This observation is recorded here under the post-freeze rule.
