## The main question of this run (set on 25 November 2026)

This prompt was built for one question on these pages. It is the main question of the run: it comes first and it
gets most of the time. The entry for the object is written all the same, with every statement and every entry, as
the rest of this prompt says.

**His words.** The page is 57:97, headed « Critères d'équivalence » (57:98 is a blank verso; 57:99-100 continue the
subject, starting with a theorem on H¹(X, G) for the generic hyperplane section). On 57:97, X is a « variété projective non sing de dim n » and
Y a « section hyperplane non sing ». For Pic(X) → Pic(Y) the supplied reading has, by « Lef-Grauert », « inj si n ≥ 3,
H¹(Y, O_Y(−m)) = 0 pour m > 0 » and « surjectif si n ≥ 4, H²(Y, O_Y(−m)) = 0 pour m > 0 »; then « noyau un p-groupe
fini si n ≥ 3 (nul si Y général) »; and, in a box, « noyau nul si n ≥ 4 ». Lower on the page his « Question » asks for
the « Surjectivité (donc bijectivité) de Pic(X) → Pic(Y) pour n ≥ 4 sans conditions cohomologiques ». Look at the ink
of the box and of the question before you use them (step 3).

**The main question.** Let k be an algebraically closed field of characteristic p > 0, X a smooth connected
projective variety over k of dimension n ≥ 4, and Y a smooth hyperplane section of X: a smooth member of |L| for a
very ample invertible sheaf L. Is the restriction Pic(X) → Pic(Y) injective, with no cohomological condition? That is
his box. Decide it: a complete proof for every such X and Y, or a counterexample with every hypothesis checked,
followed by the corrected statement with its proof. Two more rows stand beside it and are decided in the same way:
- the same statement for a smooth member Y of |L| with L ample;
- his « Question »: under the hypotheses of the box, is Pic(X) → Pic(Y) surjective, and so bijective?

In characteristic zero both statements hold, by Kodaira vanishing and the Lefschetz theorems for the Picard group of
SGA 2, Exposé XII (our LaTeX edition is in `latex_sources/SGA2_EN/`; find the statement there and cite it by its
number). His words « sans conditions cohomologiques » are the point: in characteristic p the groups H^i(X, L^(−m)),
i = 1, 2, m > 0, need not vanish.

**Two statements to keep apart.** A statement about the Picard schemes (the kernel of Pic_{X/k} → Pic_{Y/k} as a group
scheme, or the map on tangent spaces) is not the statement about the groups Pic(X) and Pic(Y). Our runs report that
the scheme-level statement, read on α_p-torsors, already fails for ample divisors in every dimension, citing
S. Cotner and B. Zavyalov, *Lefschetz theorems in flat cohomology and applications*, Compositio Mathematica 160
(2024), 1850-1870 (doi:10.1112/S0010437X24007231), Example 3.3.6. Open it and match its hypotheses to his yourself
(`SA14/work/fhi/A_CotnerZavyalov_vacuity.tex` in the folder named below is our run's note on their Example 3.4.6).
The main question is the statement about the groups, which our runs left undecided. H. J. Kweon asks a neighbouring
question for Pic^τ of a smooth hyperplane section, and separates injectivity from closed immersion: *Bounds on the
torsion subgroup schemes of Néron-Severi group schemes*, Advances in Mathematics 409 (2022), 108687
(arXiv:2008.01908v2, Theorem 7.2 and Question 7.7).

**The literature on the main question.** Search for the exact statement, with its quantifiers and its hypotheses,
before you call a result of yours new: zbMATH Open, arXiv, MathOverflow, Numdam, and Hexagon (hexagonmath.org),
where results found by AI runs, ours and other people's, are posted. Where the literature decides the question, the outcome is the reference with its exact locator, opened by
you, with its hypotheses matched to his.

**What our runs have proved toward it** is in the folder `OBJ_H0A2-1_question/`, in LaTeX, and is open from the
start, because the main question is what these results leave open. Every status below is the run's own claim. Use a
statement of theirs only after you have rechecked it, and record that as a check event; a fault you find in one of
them is a result of this run.
- `SA14/`: our research run on the Picard folders, cotes 43-44 and 57-60 (RESEARCH_SA14_SA19, by GPT-6 Astra
  (ChatGPT Pro mode); its checkpoint of 20 November 2026). Its Part A (`sections/A.tex`) is about this page:
  - A4: an exact finite description of the kernel and of the cokernel, through the infinitesimal neighbourhoods of Y;
  - A4b: for n ≥ 4 the kernel and the cokernel are finite p-groups, killed by p^e as soon as p^e ≥ N + 1 (N as in
    A4); for n = 3 the kernel is a finite p-group;
  - A1r: the bijectivity for every n ≥ 4 is equivalent to its case n = 4, and a failure of injectivity in some
    dimension n ≥ 4 gives one in dimension 4;
  - A2b: injectivity fails in dimension 2;
  - A3: a smooth projective surface in characteristic 2 with a very ample L and H¹(X, L^(−1)) ≠ 0;
  - A2D, A2V, A2W, A2Y (entries K.207, K.219, K.220 and K.225 of the register `sections/K.tex`, with their proofs
    in `work/`): conditions that every counterexample has to meet. By A2W, if every global 1-form on X is closed,
    the kernel is zero for every smooth very ample divisor in dimension n ≥ 3. By A2Y, injectivity of Frobenius on
    H¹(Y, O_Y), or a smooth lifting of Y to W_2, excludes a kernel;
  - the rows A1 and A2 of `RESEARCH_SA14_SA19_results.csv`, both "Undecided", and in `work/` the run's attempts
    on A2 (the files `attempt_A2_*`), its audits and its research notes.
- `P90a_note_v3/`: our note that carries A3 to every characteristic (posted as hexagon:2611.00936, version 3).
- `POLISH_AG_paper_02/`: paper 2 of our run POLISH_ALGEBRAIC_GEOMETRY (by GPT-6 Astra (ChatGPT Pro mode); its
  checkpoint 35, of 24 November 2026). Among its theorems are those on the kernel of Pic(X) → Pic(Y) for a curve Y on
  a surface X in characteristic p: a strict genus bound for a nontrivial class of order p that is trivial on a smooth
  very ample curve, and an explicit positive lower bound for the excess in the conductor inequality
  (`thm:positive-excess-picard` in `main.tex`; see also `positive_square_picard_strictness.tex`). `STATEMENTS.tsv`
  lists every statement of the paper with its check events. A class in the kernel on a fourfold restricts, on each
  surface section, to a class that is trivial on the curve cut out by Y; whether it stays nontrivial there, and what
  the surface theorems then give, is for you to work out.

If these statements hold as claimed, his box holds for every n ≥ 4 exactly when no smooth projective fourfold X
carries a class of order p in Pic(X) that is trivial on a smooth hyperplane section Y. That is the gate at the
start. Put it, or the one your recheck leaves, at the top of the ledger.

**Where the outcome goes.** The proof or the counterexample of the main question is the section of `PROOFS.tex` under
its statement id, written so that it can be read by itself: the statement with every hypothesis, the complete proof,
and each result it uses with its exact locator. State the outcome at the head of `ENTRY.md`, before its section 1
(after the line INCOMPLETE, where that line is due): the statement decided, whether it is proved or refuted, and
where in `PROOFS.tex` the proof is.

