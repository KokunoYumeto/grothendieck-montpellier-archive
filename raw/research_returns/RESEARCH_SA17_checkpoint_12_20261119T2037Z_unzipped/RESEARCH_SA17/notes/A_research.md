# Part A research record

## Sources opened
- Official Montpellier 131.pdf: viewed scans 14 and 16; rotated crop of margin14. The word Non is visible; it does not by itself prove L2.
- Murre, Expose294: full PDF downloaded and text extracted; F7, Theorem1, Corollary2, appendix theorem read.
- Stacks 0417, 053X, 01JJ, 02VI, 08KE, 08J1, 0CCJ read.

## Exact gates
- A.1: main finite-type interpretation still requires deriving the needed openness/constructibility from axiom8 and bridging formal versus local modularity. Literal scan14 omits a finiteness condition on Z; investigate square-zero direct-sum thickening as necessity counterexample.
- L1: naive noetherian induction does not identify M(T,eta) intersect a closed subscheme with modularity after that base change. Formal-thickening argument from Murre may supply the missing comparison; being formally etale and having isomorphic local rings remain distinct.
- A.2: dimension-one counterexample proved (A:ind-thickening). L2 remains: complete noetherian adic effectivity vs generic infinitesimal contraction; trying explicit quotient functors and a closed-diagonal argument.
- A.3/L3: completion descent settled by opened Murre theorem(d). Nonfinite quasi-projective effectivity false; Hironaka example can match the exact single-deleted-point cover of cote126. Preparing explicit adaptation and polarized descent correction.

## Attempts that do not yet close A.1
- Artin algebraization: cannot cite without excellence/versality hypotheses and exact comparison.
- General algebraic-space descent: fpqc sheaf property alone is not effective descent; use Murre for required noetherian case.
- Naive noetherian induction from generic modularity: obstruction is change of base to a reduced closed subset, which can erase infinitesimal obstructions.
- Formal completion detects etaleness, not local-ring isomorphism; étale charts could use Murre Cor2 to represent their base changes, but first openness at all points is needed.

## FINISH continuation, 2026-11-19 13:24 UTC

New unconditional proof of Corollaire 2 written in sections/A_finish.tex. The generic Artinian local ring represents F by 1–5; generic maximality of an unramified lift identifies the finite local quotient with A_p/I_p, hence ACTUAL generic modularity. Condition8 then gives local modularity on a dense open, which forbids thicker intermediate extensions there. This proves Murre F8 directly without the main A1 formal-to-local gate. Corrected NRb is Murre F7, so the published theorem applies. Independent targeted audit requested.

Further main-gate work: reopened de Jong–Olander Theorem2 (weakly etale only) and Cesnavicius Proposition3 (henselian loop rings only). Neither proves arbitrary-pair fpqc descent of P(R)=alpha_p(R^h_(t)). Attempted integral-element descent: b^p=0 gives a finite A[b], and the henselized cocycle gives (1+t c)(b tensor1−1 tensor b)=0, but no justified descent of this relation to a finite etale A-algebra has yet been established. This is an active approach, not a claimed proof.

### Artin approximation and finite-cover attempt (continuation, 13:45 UTC)

We tested whether complete noetherian local bases remove the formal-to-local gate by Artin approximation. Over an essentially finite-type local algebra of a complete noetherian local A, a formal point of the finitary fibre functor h_B x_F h_R does algebraize to a henselian/etale point: its finite equations and equality in F descend to a finitely presented R-algebra, and ordinary approximation applies. This establishes an etale-local lifting statement, not actual modularity. The missing descent remains infinitesimal.

A tempting repair was to refine this etale cover by a finite faithfully flat cover, whose double overlap has every maximal ideal over the original closed point; formal uniqueness would then descend the B-map. Stacks05WN, reopened exactly, supplies a finite locally free cover followed by a Zariski cover and a second finite locally free cover. The intervening Zariski opens need not remain finite over the local base. Their intersections can have maximal points away from the closed fibre, where formal uniqueness is unavailable. Thus it does not give the required single finite cover carrying one compatible B-map. No proof of actual modularity is claimed from this argument.

Fieldwise injectivity of finite formal branches can be proved by the trait/valuative argument even before etaleness; it does not detect nilpotent disagreements on these overlaps. The main gate is therefore not a missing topological separation argument. We continue with the diagonal and henselized infinitesimal routes.

### Henselized candidate eliminated for L2, 13:59 UTC

Proposition A:hensel-adic-failure gives an explicit noetherian complete adic ring where the candidate fails surjectivity of condition4. The compatible square-zero sections use infinitely many independent Artin–Schreier coefficients. Every element of one etale neighborhood has its coefficients in a single finite separable extension of Fp(t), giving a contradiction. The dieudonne agent independently checked the proof. This removes this candidate from L2 regardless of the still unresolved arbitrary-ring fpqc issue. We now return to the closed-diagonal argument and seek a different candidate only if that route fails.

### Main candidate gate narrowed, 14:20 UTC

A:hensel-remaining-gate now verifies conditions1,3–8 and nonrepresentability for P, including the literal actual7 (vacuous exactly when t is a nonnilpotent nonunit on the complete local base). The local test A[u]_(m,u)[epsilon]/epsilon² has a henselian Artin–Schreier nilpotent section missing from the finite formal alpha_p model. A minimal-prime reduction and the pole at infinity prove that absence. The descent_groups agent independently audited the actual7 and8 arguments. The sole missing main-counterexample axiom is arbitrary fpqc equalizer descent; fppf descent and fpqc separatedness are proved. This candidate remains unavailable for L2 because A:hensel-adic-failure refutes its strengthened adic4.

### L2 settled negatively, 14:27 UTC

The simpler supported subgroup H(R)={x:x^p=0 and x in tRx}, over S=Spec Fp[[t]], supplies the counterexample. The key new step is full adic4: compatible x_n give x in (tx)+I^n for every n, and Krull closure of the fixed principal ideal (tx) gives x in H(R). Its actual closed modular model is the identity base, whereas the generic functor is alpha_p. Conditions1,2,3,5,6,8 have direct proofs. Both descent_groups and dieudonne independently checked every axiom. A:L2-counterexample is the definitive ID; L2 is no longer an open gate. This does not settle A1, because H deliberately fails7. The quotient/henselized candidate P remains directed at A1.
