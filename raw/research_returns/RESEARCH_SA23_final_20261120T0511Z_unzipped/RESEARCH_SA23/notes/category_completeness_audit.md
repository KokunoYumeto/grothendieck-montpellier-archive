# Final scope audit against the exact task

Date: 2026-11-20. Auditor: GPT-6 Astra, inherited effort, category agent.
Inputs actually read: `upload/PROMPT(20261120-001045).md`,
`notes/outcome_table.tsv`, RP6 and the relevant original cote-26 headings,
current F, H and K sections, and the category sections already independently
checked. This is a scope audit, not a repetition of all earlier proof audits.

## Concrete findings and their disposition

1. **F does not need an invented unconditional finite-order theorem.**
   RP6 explicitly allows “locality and finiteness hypotheses to be stated”.
   The formal-locality/affine finite-presentation/quasi-compact-base theorem
   addresses that wording. The fixed-order theorem handles a wider target
   with effective descent, and the unaugmented versus augmented jet-group
   distinction is now proved explicitly. These are stated hypotheses,
   not an unannounced special case of RP6.

2. **K(g) and K(h) now give the whole promised classification groupoids.**
   The finite locally free Hopf-coaction criterion, its torsor identity,
   effective descent and arrow convention cover the noncommutative and
   inseparable finite-flat cases. Nonflat groups remain under the explicit
   covering/cocycle classification. The relative P1 answer now includes
   all finite projective chart modules through arbitrary finite idempotent
   matrices and explicit inverse overlap maps; freeness of polynomial-ring
   modules is not assumed. Their field and finite-étale specializations
   are no longer being substituted for the full answers.

3. **K(c)'s exact cited criterion was independently opened.**
   Stacks Lemma 97.18.3, tag 06PL, says the classifying stack of the trivial
   action is algebraic exactly when the group algebraic space is flat and
   locally of finite presentation. Thus the nonflat-quotient argument is
   supported by the source actually cited. No additional flatness hypothesis
   was hidden in its converse.

4. **K(e) had a short removable scope restriction.**
   The original proof ruled out locally finitely presented algebraicity of
   the unpolarized abelian stack. The stack is limit preserving: objects,
   group structure, morphisms and all finite identities descend under
   filtered affine limits; properness and smoothness descend; the number
   of geometric components is the locally constant degree of the finite
   étale Stein factor, and dimension is read from the rank of the tangent
   module at the identity. The two bad loci are clopen; their idempotents
   vanish at a later stage when they vanish in the colimit. Hence all data
   descend as abelian schemes of fixed dimension. Stacks Proposition
   102.3.8, tag 0CMY, then upgrades the contradiction to nonalgebraicity
   without a separate finite-presentation assumption. This proof and the
   exact opened sources were sent to the geometry agent, who is inserting
   the strengthening. Fine representability is already refuted without
   any finite-presentation condition by the twist example. No claim that
   a coarse moduli functor equals the stack is made by this argument.

5. **H.2 really refutes the requested all-operator formula.**
   The literal infinite decreasing rearrangement already fails for
   reciprocal finite-rank perturbations of the identity. The independent
   scalar examples then show that no assignment to `0·infinity` can make
   the proposed total extended determinant multiplicative on all
   scalar-plus-compact operators. Thus restricting the replacement to the
   spectral-trace determinant on `1+L1`, with all bounded operators when
   the trace is finite, does not leave the original universal assertion
   undecided. A claim of a unique maximal possible alternative domain is
   neither made nor needed; such a domain is not specified by the question.

6. **J's existence question is now explicit.**
   J1 formerly described the relative H1 groupoid after choosing an
   extending section. The added unconditional factor-set equations from
   an arbitrary set-theoretic lift describe all solutions and emptiness
   before any reference solution is chosen. Multiplication, gauge action,
   fixed-subgroup restriction and continuity of the actual section were
   checked directly. The existing H1 description is the trivial-factor-set
   specialization. This removes an implicit existence oracle in a
   “Determine” task.

7. **Historical source qualifications are not automatically new tasks.**
   The full-1956 proof-architecture audit is preserved separately in
   `notes/category_fredholm1956_audit.md`. A clearly identified reprinting
   of the 1955 memoir is evidence about the inspected work; first-printing
   collation is an edition qualification, not an additional task explicitly
   required by the prompt. The manuscript-sheet date is different: no
   date should be inferred from the dossier's separate 1953 letter.
   The original Lead says “may predate”, so absence of a date neither
   proves that possibility occurred nor refutes a stronger priority claim
   that the user never made. The exact archival date remains unproved.

8. **A.3's missing P is a documentary limit, not a proved definition.**
   The noetherian adic lifting theorem is proved independently of a guessed
   P; preservation is then proved for each of the two explicitly defined
   standard module-projectivity readings. This settles those full
   mathematical formulations. It does not identify the wording of the
   missing preceding section or prove preservation of an arbitrary unknown
   extra property. The outcome table must retain its explicit two-reading
   qualification; source underdetermination is not itself a mathematical
   proof of what the absent definition meant.

## Opened primary locators for the K(e) strengthening

- https://stacks.math.columbia.edu/tag/01ZM — Lemma 32.10.1,
  parts (1)–(3): objects, morphisms and eventual equality.
- https://stacks.math.columbia.edu/tag/0C0C — Lemma 32.8.9:
  smoothness descends at a later stage.
- https://stacks.math.columbia.edu/tag/081F — Lemma 32.13.1:
  properness descends at a later stage.
- https://stacks.math.columbia.edu/tag/0E0D — Lemma 76.36.9:
  the proper flat finitely presented geometrically reduced Stein factor
  is finite étale; schemes are included in the stated algebraic-space scope.
- https://stacks.math.columbia.edu/tag/0CMY — Proposition 102.3.8:
  an algebraic-stack morphism is limit preserving exactly when locally
  of finite presentation. Its section is tag 0CMQ.
- https://stacks.math.columbia.edu/tag/06PL — Lemma 97.18.3:
  the classifying-stack criterion used in K(c).

All six pages were opened, and their statements and applicable hypotheses
were read. No core section owned by another agent was edited in this audit.
