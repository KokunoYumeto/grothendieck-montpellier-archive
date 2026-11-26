# Weak fundamental localizers that are not fundamental localizers, and Corollaire 7.7.2 of Grothendieck's *Les Dérivateurs*

**Abstract.** In Chapter XVI of *Les Dérivateurs* Grothendieck axiomatized the classes W of weak equivalences between
small categories by a saturation axiom, the asphericity of categories with a final object, and Quillen's Theorem A in an
absolute form, Loc (3). He wrote that a relative form, Loc (3 bis), was the more important one, and in Corollaire 7.7.2
he derived it from three further axioms: gluing along Mayer–Vietoris squares, Loc (6′a); stability under filtered
colimits, Loc (8); and accessibility, Loc (9). A footnote adds: "Loc (3 bis) pas prouvé, probablement faux". Classes
satisfying the absolute form are now called weak fundamental localizers (Maltsiniotis), classes satisfying the relative
form fundamental localizers, and Cisinski proved that the weak homotopy equivalences form the smallest class of either
kind. We show that the absolute form does not imply the relative one: there are weak fundamental localizers that are not
fundamental localizers. The smallest of our witnesses is a functor between groupoids with two objects over the group of
order two; other examples are strongly saturated and satisfy Loc (8) and Loc (9), or are accessible and satisfy
Loc (6′a). Conversely, a weak fundamental localizer is a fundamental localizer if and only if it satisfies Loc (6′a) and
Loc (8); this direction rests on Cisinski's correspondence between fundamental localizers and localizers of simplicial
sets. So Corollaire 7.7.2 holds, and holds without Loc (9): the footnote's "probablement faux" is not borne out. Neither
of the other two hypotheses can be omitted, and the doubt becomes true as soon as one of them is dropped; nor can Loc (8)
be weakened to stability under countable colimits. In all our examples the aspherical categories are exactly the weakly
contractible ones, so the difference between the two axiom systems is invisible to asphericity. The four classes and
the sufficiency of the two axioms were found by GPT-6 Astra (OpenAI, ChatGPT Pro mode); their necessity and the text are
by Claude Opus 5.5 (Anthropic) at effort max, and the example showing that Loc (8) cannot be weakened is by Claude Fable
5.2 (Anthropic) at effort max. The proofs were checked by Claude Opus 5.5 at efforts max and high and by Claude Fable 5.2
at effort max. No human has checked them.

- Paper: `D3_paper.pdf` (19 pages), source `src/D3_paper.tex` (one file). Built 25 Nov 2026 with pdflatex: no overfull
  box, no undefined reference or citation; every page looked at (`pages/`), before and after the repairs of the check.
- AI-produced: results of GPT-6 Astra (ChatGPT Pro mode), four runs, 11–18 Nov 2026; text by a34c04448e8299803
  (Claude Opus 5.5 at effort max), 25 Nov 2026. Independent check of the whole text: afceadd46f7598ec4 (Claude Fable 5.2
  at effort max), 25 Nov 2026 (`CHECK_D3_INDEPENDENT.md`): no mathematical error; repairs R1–R15 applied (R13 in part,
  see `PROVENANCE.md`). Three results of that checker (Proposition 4.2, the failure of Loc (8 bis) for W_circ, the
  failure of Loc (9) for W_π) are in the paper, checked line by line by the writer. No human has checked any part. No
  check by a model of another family than Claude of the writer's and checker's own arguments.
- Not posted. The workbench deposit (`CHECK_EVENTS.tsv`, `PROVENANCE.md`, the check report, and the four programs
  named in Section 8 of the paper) is still to be made by whoever posts.
- MSC 2020: 55U35 (abstract and axiomatic homotopy theory), 18N40 (homotopical algebra, Quillen model categories,
  derivators), 18N50 (simplicial sets, simplicial objects).
- Keywords: fundamental localizer; weak fundamental localizer; Quillen's Theorem A; Grothendieck; *Les Dérivateurs*;
  localizer of simplicial sets; Mayer–Vietoris gluing; accessible class; Cisinski.
