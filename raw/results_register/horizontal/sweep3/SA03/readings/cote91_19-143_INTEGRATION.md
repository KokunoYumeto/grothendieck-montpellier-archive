## STUDY

Reader R3 (Claude Opus 5.5 at effort max) of a6d42bf6fe2b0d8a8, 19 Nov 2026. Read: every transcribed scan of 91/19-143 (114 scans) in both witnesses, K91-02..10 and the Pro packages MPL_91_019-058, 059-098 and 099-143 (GPT-6 Astra, ChatGPT Pro mode); mean similarity 0.85. The stage-A dossier (GPT-6 Astra, ChatGPT Pro mode), §2, was used as a witness. No scan was viewed. 13 check events, 10 corrections.

**91/19-32 (SA03-1, SA03-2).**
- The proof of the relative unramified Hom theorem (begun on 91/16) ends by an obstruction calculus. ξ in Ext¹ is killed by π^n, then passed through Hom(M_{u_0}, J_n) to Hom(N, J). The algebra checks; two compatibilities are admitted on the page.
- The second route by splittings of extensions has an error: the compatibility condition must vanish on the kernel of the combined map L ⊕ M' → M, not on R_1 + R_2. The stage-A dossier agrees.
- Corollaries:
  - representability of ∏_{X/S}P/X from flat probes Z_i, with separatedness only for P/X separated;
  - his question whether components are of finite type: no (an infinite chain of P¹ over a point);
  - Isom and Aut over a field (Matsumura-Oort);
  - Aut_S(X) after a finite étale cover.
- The English letter to Anantharaman (11.9.1967) summarizes the method.

**91/34-59 (SA03-3, SA03-4): the Weil restriction f_*.**
- Plans for "Schémas Hom" and for a chapter on descent.
- Nagata's counterexample to Galois descent.
- f_*(V̌F) = V̌(f_*F).
- The existence criterion: multisections in affine opens, = BLR §7.6, Theorem 4.
- Preserved properties; projectivity through det f_*(L) and Grassmannian equations.
- Smoothness and étaleness preserved; the counts n^ν (needs separatedness) and λ^{ν_s}; "homogeneous" finite flat morphisms.
- The dimension corollary is wrong as written (only pure dimension d ⇒ nd).
- The étale envelope π_0(T/S); his general claim about left-exact functors on π_1-sets is false (fixed points, identity) and needs étale-local compatibility.

**91/61-80 (SA03-6): Weil restriction and Greenberg realization in one frame.** Functors 𝕎 "de nature locale" and their right adjoint 𝕎^a:
- finite limits;
- the affine case through a generating ring scheme;
- gluing lemmas;
- existence for special Greenberg functors and finite locally free radicial S' → S;
- preservation of immersions and finiteness.

All checked as stated.

**91/81-122 (SA03-7): schematic sets and the constructible topology.**
- Constructible maps and piecewise isomorphisms.
- His "Si X noethérien Y l'est" holds for spaces, not for schemes, even reduced: B = k + x·k[x, y].
- His question "Cons(lim) = lim Cons?" has a negative answer (indicator functions on A¹_ℚ).
- The constructible topology: his "antitypique" = pro-constructible. Quasi-compact f ⇔ f^cons proper; Spec(A)^cons compact; the absolutely flat hull A^cons; compact schemes are affine.

**91/124-142 (SA03-9, SA03-10).**
- Thick points of pro-schemes (open implications).
- The Greenberg realization over a DVR with set maps from generic morphisms (stated, not proved).
- The loop group A((t))^*: an ind-scheme whose stages are non-reduced; (i)-(iii) checked, (iii) needs n' > n.
- Pro-categories of schemes.
- Jets and coordinate changes; the composition formula checked.

**Versos.** Bourbaki rédactions n° 316, 288, 285 and 371: identified, not reproduced.

## HUNCHES

- **H91-2 (new).** The loop-group theorem of 91/134-135 is an early form of the structure of the ind-scheme A ↦ A((t))^*: a reduced part ℤ × G_m × (1 + tA[[t]]) and a formal nilpotent part (1 + t^{-1}·nil(A)[t^{-1}]). This decomposition underlies the symbol of C. Contou-Carrère, C. R. Acad. Sci. Paris 318 (1994) (locator to be checked), the author of the cote 71 manuscript. The non-reduced stages 𝒢_n and the failure of open immersion for |ν| < n are exactly the nilpotent factor. Grounds: SA03-R91-10.
- **H91-3.** The 𝕎/𝕎^a frame of 91/61-80 is the common generalization of Weil restriction and Greenberg realization now found in A. Bertapelle and C. González-Avilés (locators to be checked; cited by the stage-A dossier). His Theorem 1 for radicial finite locally free S' → S is the case n(s) = 1 of BLR §7.6, Theorem 4. Grounds: SA03-R91-07.
- **H91-4.** His "parties antitypiques" (91/104-111, reading uncertain) are the pro-constructible sets of EGA IV 1.9. The leaves look like a draft of that section: the same statements, Prop. 1-2 and Cor. 1-3, appear there in final form, with the absolutely flat hull of 91/115 = EGA IV 1.9.16 and Olivier's construction. Grounds: SA03-R91-09.

## PACKAGES

- **P91-2: the representability of ∏_{X/S}P/X from flat probes (91/19-29).**
  - **Question:** prove the theorem of 91/26 with the corrected obstruction (SA03-K91-01) and with P/X separated:
    - representability locally of finite presentation;
    - quasi-affineness over ∏ ∏_{Z_i};
    - essential quasi-projectivity.
  - Decide his Corollary 9 with U' = U (effectivity of descent data).
  - **Why it matters:** it is the theorem announced in the letter of 1967, and the base of the Hom, Isom and Aut statements.
  - **What it rests on:** 91/16-29 (SA02-R91-05, SA03-R91-01..03).
  - **Strongest reduction on the pages:**
    - the openness of the unramified locus (91/16-17);
    - the obstruction calculus in Ext¹(M_u, J) (91/19-21);
    - the corrected kernel condition.
  - **Material:** `cote91_19-143.md`, `sweep3/SA02/readings/cotes90_91-2-18.md`, K91-01..03, MPL_91_019-058, the stage-A dossier §2.1. Literature: Olsson 2006 and Matsumura-Oort 1967 (locators to be checked).
- **P91-3: schematic sets and constructible maps (91/81-122).**
  - **Question:** set up the category of schematic sets with its finite-partition morphisms and characterize what is invariant: the underlying space, Cons, X^cons, and noetherianity of the space but not of the scheme. Answer his questions on 91/97 and 91/99 (the limit comparison, and whether quasi-schematic sets form a "catégorie géométrique").
  - **Why it matters:** this is his frame for the Greenberg-Néron programme (91/118, 131-136).
  - **What it rests on:** 91/87-122 (SA03-R91-08, R91-09, R91-13).
  - **Strongest reduction:** the finite-partition lemma, Spec(A)^cons compact, the absolutely flat hull.
  - **Material:** `cote91_19-143.md`, K91-06..09, MPL_91_059-098 and 099-143, the stage-A dossier §2.4. Literature: EGA IV 1.8-1.9, Olivier 1967-68, Liu-Sebag (locators to be checked).
