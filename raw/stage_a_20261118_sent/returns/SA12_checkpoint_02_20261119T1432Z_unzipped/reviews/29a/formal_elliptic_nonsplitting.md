# The elliptic nonsplitting example in the formal tame category

The subsequent actual transcription was read here: cote29 scan96, CodexK29-07 lines51–64, explicitly excludes the projective-line/empty-boundary case from π₂=0, then calls the remaining curve extension `triviale`. Thus the example in `independent_checks.md` §7 bears on an explicit later manuscript assertion. Root owns its claim ID and will merge the crosslink to SA12-64.

The following algebraic construction retains the formal setting. Work over C and let E be an elliptic curve, L=O_E(0) its symmetric degree-one line bundle, and n>1. Put M=L^n. Symmetry gives [n]^*L≅L^(n²)=M^n. On total spaces the nth-power map M→M^n, followed by the finite étale base map [n]:E→E, gives a finite map to the total space of L. Off the zero sections it is étale; along the zero section it has Kummer ramification index n, hence is tame. Completing along the zero sections gives a covering in the regular formal divisor setup of scans88–96. The covering is algebraic before completion.

Let H be the automorphisms of M covering translations by E[n] whose nth powers agree, under M^n≅[n]^*L, with the canonical descent action on [n]^*L. Each translation lift exists because K(M)=E[n]. Its nth power may differ from the required action by a scalar; that scalar has an nth root over C, so the lift can be rescaled. Thus H maps onto E[n] with kernel μ_n. The compatibility condition is preserved by composition. It follows that H has order n³ and acts by deck transformations of the connected degree-n³ cover M^×→L^×. The cover is therefore Galois with group H.

The commutator pairing on E[n] is the nondegenerate theta pairing of M, so H is noncommutative. The nondegeneracy is the exact statement of Mumford1966 §1 Theorem1, printed pp293–294; the primary paper and its proof were opened. Moonen’s opened ChapterVIII8.24–8.25 gives the corresponding Heisenberg description. Locally at the zero section the μ_n kernel is inertia, and completion retains this finite tame covering and its noncommuting deck transformations. Its connectedness is visible on the connected special fibre E.

The base E has abelian étale fundamental group and its cyclotomic action is trivial over C. A split inertia extension would therefore be a direct product of abelian groups and could have no nonabelian finite quotient. The constructed H contradicts this. Equivalently c₁(L) modn is nonzero: Kummer injects Pic(E)/n into H²(E,μ_n), and a degree-one line bundle is not an nth power. The finite-level Čech comparison in `independent_checks.md` §7 identifies that obstruction with the extension class.

This is an independent reconstruction/check of a standard example, not a novelty claim. C14 in `checks.py` verifies a finite Heisenberg commutator; the construction above supplies the formal-geometric passage that a topological torus diagnostic alone would not supply.

## Opened sources

- Mumford, *On the Equations Defining Abelian Varieties I* (1966), §1 Theorem1 pp293–294 and the symmetric multiplication formula p289: https://pazuki.perso.math.cnrs.fr/index_fichiers/Mumford66.pdf . Accessed2026-11-19.
- Van der Geer–Moonen, ChapterVIII, §§8.1–8.6 and8.24–8.25, version15 September2011: https://www.math.ru.nl/~bmoonen/BookAV/ThetaGr.pdf . Accessed2026-11-19.
- Kummer sequence: https://stacks.math.columbia.edu/tag/03PK . The units term is retained.

## Check scope

The theta pairing theorem was read and used, not independently reproved in full. The construction of the finite formal tame cover, its lift-normalization condition, order n³, and the nonsplitting deduction were independently checked here. The exact degree-n symmetric line-bundle identity is the opened primary input, so no analytic-to-formal equivalence is silently assumed.
