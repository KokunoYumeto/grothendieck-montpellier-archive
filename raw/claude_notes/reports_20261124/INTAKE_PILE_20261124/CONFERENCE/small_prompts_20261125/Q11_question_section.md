## The main question of this run (set on 25 November 2026)

This prompt was built for one question on these pages. It is the main question of the run: it comes first and it
gets most of the time. The entry for the object is written all the same, with every statement and every entry, as
the rest of this prompt says.

**His words.** On 100:3 the « Théorème » takes S « schéma loc. noeth », U an open subscheme, T its closed
complement, and a prime p with car k(t) = p for every t in T. C is the category of abelian schemes A over S, and C′
that of the (A_U, M, φ), where A_U is an abelian scheme over U, M a « groupe p-divisible sur S » and
φ : M|U → T_p(A_U); the functor is F(A) = (A ×_S U, T_p(A), id). Part 1): if U meets every connected component of S,
« le foncteur F est pleinement fidèle ». Part 2): suppose a) « ∃ morphisme fini surjectif S′ → S, avec S′ géom.
unibranche (p.ex. la normalisée de S est finie sur S, si S local) » and b) « On a prof ét_T(S) ≥ 2 »; « Alors F est
une équivalence des catégories ». On 100:7 the proof of « 2) Foncteur ess. surjectif » carries a box in the margin,
« Si S géom. unibranche en les points de S−U » with « et si le normalisé de S_red est fini sur S », and its step
« a) Réduction au cas S réduit » ends on « On gagne ! » with a question mark beside it. Look at the ink of part 2),
of the box and of that step before you use them (step 3).

**The main question.** Part 2) of his theorem for a reduced base whose normalization is finite (the second condition
of his box on 100:7). Let S be a reduced locally noetherian scheme whose normalization is finite over S, U an open
subscheme, T = S − U, with every point of T of residue characteristic p, and assume his b): prof ét_T(S) ≥ 2. His a)
then holds with S′ the normalization of S, a normal scheme being geometrically unibranch. Is F an equivalence of
categories? The hard half is essential surjectivity: is every (A_U, M, φ) isomorphic to F(A) for an abelian scheme A
over S? Decide it: a complete proof for every such S, U and p, or a counterexample with every hypothesis checked,
followed by the corrected statement, the strongest version that is true, with its proof. Two more rows stand beside
it and are decided in the same way:
- the statement of his box on 100:7, as the ink gives it: essential surjectivity when S is geometrically unibranch
  at the points of T and the normalization of S_red is finite over S;
- his part 1), full faithfulness, on these bases.

Take « prof ét » in the sense of SGA 2, Exposé XIV (our LaTeX edition is in `latex_sources/SGA2_EN/`), and
« géométriquement unibranche » in the sense of EGA (`latex_sources/EGA_FR/`), each cited by its number.

**What our runs have proved toward it** is in the folder `OBJ_H037_question/`, in LaTeX, and is open from the start,
because the main question is what these results leave open. Every status below is the run's own claim. Use a
statement of theirs only after you have rechecked it, and record that as a check event; a fault you find in one of
them is a result of this run.
- `SA15/`: our research run on the crystals folders and cote 100 (RESEARCH_SA15, by GPT-6 Astra (ChatGPT Pro mode);
  its checkpoint 37, of 20 November 2026). Its Part C (`sections/C.tex`) is about these pages, and `sections/F.tex`
  (C.1 to C.4 there) gives his passages with their locators:
  - C-RD6: for S locally noetherian and normal, with U dense, F is an equivalence; the proof rests on
    R. Krishnamoorthy and A. Pál, *Rank 2 local systems and abelian varieties*, Selecta Mathematica 27 (2021),
    article 51, Corollary 6.12;
  - C-RD5: part 2) fails as written: for S = Spec Z_5[ε]/(ε²) and U = D(5), a) and b) hold and a triple does not
    extend. C-RD4: yet over S = Spec k[[t]][ε]/(ε²) with U = D(t), not reduced at T, F is an equivalence. C-RD3 and
    C-RD12 describe what nilpotents change;
  - C-RD11: a reduced, one-dimensional, geometrically unibranch noetherian local domain of mixed characteristic
    (0, 5) whose normalization is not finite, where a) and b) hold and F is not essentially surjective;
  - C-RD13 and C-RD14: the essential image of F described by formal models and compatible charts, and the form this
    takes for elliptic curves;
  - C-RD7 to C-RD10, on his lemma of 100:17 that a « syst local » of abelian schemes comes from an abelian scheme
    (marked « Douteux, sans doute faux » in the margin): it holds on reduced geometrically unibranch bases (C-RD7)
    and on reduced bases with a finite surjective geometrically unibranch cover (C-RD8), nilpotents add no
    obstruction (C-RD9), and it fails on a reduced base with infinitely many nodes (C-RD10);
  - C-RD1 and C-RD2, on his Corollaire 3 of 100:25, the descent of homomorphisms of p-divisible groups.
- `POLISH_CRISTAUX_paper4/`: paper 4 of our run POLISH_CRISTAUX (by GPT-6 Astra (ChatGPT Pro mode); its checkpoint
  34, of 24 November 2026), *A reduced counterexample to Grothendieck's extension assertion, after Ferrand-Raynaud
  and Olberding*: the example of C-RD11 written out. Its closing remarks say that it does not classify the bases
  that are not normal, and that the case of a finite normalization needs a descent theorem of its own. That case is
  the main question here.

If these statements hold as claimed, the gate at the start is this. By C-RD6 the pullback of (A_U, M, φ) to the
normalization S̃ of S is the image of an abelian scheme Ã over S̃, unique up to unique isomorphism, and (A_U, M, φ)
comes from an abelian scheme over S exactly when Ã descends to S compatibly with A_U and M. The main question is
whether it always descends. Put that gate, or the one your recheck leaves, at the top of the ledger.

**Sources our runs name for these pages**, each to be opened and matched to his hypotheses by you: D. Ferrand and
M. Raynaud, *Fibres formelles d'un anneau local noethérien*, Annales scientifiques de l'École Normale Supérieure
(4) 3 (1970), 295-311 (Numdam ASENS_1970_4_3_3_295_0); B. Olberding, *One-dimensional bad Noetherian domains*,
arXiv:1209.2991; A. J. de Jong, *Barsotti-Tate groups and crystals*, Proceedings of the ICM 1998, vol. II, 259-265;
N. Katz, *Serre-Tate local moduli*, Lecture Notes in Mathematics 868 (1981), 138-202. For descent along a finite
birational morphism, one more place to look, named here from memory and so to be checked before any use:
D. Ferrand, *Conducteur, descente et pincement*, Bulletin de la Société Mathématique de France 131 (2003), 553-585.

**The literature on the main question.** Search for the exact statement, with its quantifiers and its hypotheses,
before you call a result of yours new: zbMATH Open, arXiv, MathOverflow, Numdam, and Hexagon (hexagonmath.org),
where results found by AI runs, ours and other people's, are posted. Where the literature decides the question, the outcome is the reference with its exact locator, opened by
you, with its hypotheses matched to his.

**Where the outcome goes.** The proof or the counterexample of the main question is the section of `PROOFS.tex` under
its statement id, written so that it can be read by itself: the statement with every hypothesis, the complete proof,
and each result it uses with its exact locator. State the outcome at the head of `ENTRY.md`, before its section 1
(after the line INCOMPLETE, where that line is due): the statement decided, whether it is proved or refuted, and
where in `PROOFS.tex` the proof is.

