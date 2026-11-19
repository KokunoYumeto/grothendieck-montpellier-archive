# Cote 84: the signs in the χ-split extensions

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 18 Nov 2026.

**Verdict:**
- Everything I checked on the scans says what the frozen transcription says.
- His sheets use two conventions, and the last word is the plus convention b′ᵢ = bᵢ + χUᵢ. With it, the product follows the same rule as its factors, and the cocycle law U″ = U + U′ holds; I checked both by hand.
- The missing χ on 130 and the condition "2 − χ = 1" on 140 are his slips. The second one he corrected himself on 152.
- The "signe étrange" on 136 is his own flag. The notes trace it to a −id in the dual extension; it stays open for sweep 3.

## Where

| What | Where |
|---|---|
| His pages | Cote 84, even scans 124-144 (MPL_84_097-145) and scans 146-170 (MPL_84_146-193; Work and Codex K84-10 for 146-160). The odd scans 125-145 are the reused Récoltes et Semailles typescript. |
| Scan images | `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/84.pdf`, PDF pages 130, 132, 136 and 140, read at 220 dpi. I did not view 134. |
| Notes | Pro notes MPL_84_097-145 B03-B19 (#42-#67, #112) and its research leads #29-#47 with the second audit #49; Pro notes MPL_84_146-193 #3-#34; Work and Codex K84-10 |
| Items | SA02-4: χ-split extensions (= H01R). SA02-9: the χ-groupoid (= H01W). SA01-36: K84-10 (= H01R). Related: SA02-1, the product of quadratic algebras (= H01I); SA01-17, λ-split extensions on cote 83 (= H00Z). |

## The set-up, from his pages

Notation as written on his sheets:
- **Extensions:** 0 → Lᵢ → Eᵢ → Mᵢ → 0, with Lᵢ and Mᵢ invertible modules.
- **Splittings and trivialisations:** splittings pᵢ and χ-trivialisations bᵢ ∈ Hom(Mᵢ, Lᵢ).
- **A change of splitting** is p′ᵢ = pᵢ − Uᵢ with Uᵢ: Mᵢ → Lᵢ. It gives b′ᵢ = bᵢ + χUᵢ (130).
- **The product E₁*E₂** satisfies x₁*u₂ = π₁(x₁)⊗u₂, u₁*x₂ = u₁⊗π₂(x₂) and u₁*u₂ = χ·u₁⊗u₂ (136). Together these force πᵢ = χ·id on Lᵢ.
- **The change for the product** is U = b₁⊗U₂ + U₁⊗b₂ + χU₁⊗U₂ (130, 132).
- **At χ = 2** this is the trace of a quadratic algebra (Tr = 2 on O), which is SA02-1.

## The readings, decided on the scan images

| Scan | The ink | Notes | Verdict |
|---|---|---|---|
| 130 | p′ᵢ = pᵢ − Uᵢ, then b′₁ = b₁ + χU₁, b′₂ = b₂ + χU₂; U = b₁⊗U₂ + U₁⊗b₂ + χU₁⊗U₂; last line π_{p′₁,p′₂}(η, ζ) = π_{(p₁,p₂)}(η, ζ) + U(η), with no χ before U(η) | B09 | The frozen reading is right. With his own definitions the line needs + χU(η): his slip. |
| 132 | Head: b′ᵢ = bᵢ + χUᵢ. Middle: b′₁⊗b′₂ = (b₁ − χU₁)⊗(b₂ − χU₂) = b₁⊗b₂ + χU. Upper right: b″ᵢ = b′ᵢ − χU′ᵢ and b″₁⊗b″₂ = b′₁⊗b′₂ − χU′. A crossed-out mixed line. The lower right rewritten with plus (b″₁ = b′₁ + χU′₁, b″₂ = b′₂ + χU′₂). Foot: "Je dis que U″ = U + U′", with U″ = b₁⊗(U₂+U′₂) + (U₁+U′₁)⊗b₂ + χ(U₁+U′₁)⊗(U₂+U′₂). | B10, B11 | Both conventions are in the ink, as the notes say. The plus convention is the last word. The middle expansion has minus signs but a plus result: a slip. |
| 136 | (U₁*U₂)(x₁*x₂) = −χ·U₁(x₁)⊗U₂(x₂), with an arrow to the minus and "signe étrange !" below. Under it: (x₁+u₁)*(x₂+u₂) = x₁*x₂ + x₁*u₂ + u₁*x₂ + u₁*u₂, with x₁*u₂ = π₁(x₁)⊗u₂, u₁*x₂ = u₁⊗π₂(x₂), u₁*u₂ = χ·u₁⊗u₂. | B13, B15 | Confirmed. The minus is his own flagged anomaly. |
| 140 | For x₁ = u₁ ∈ L₁ and x₂ = u₂ ∈ L₂: "(2 − χ)λ₁λ₂ u₁⊗u₂", partly struck, and the live line "2 − χ = 1". Then (f₁*f₂)(u₁⊗u₂) := λ₁λ₂ u₁⊗u₂. | B18, B19 | Confirmed. The line comes from taking πᵢ(uᵢ) = uᵢ; see below. |

## The mathematics, checked by hand

1. **The product follows the rule of its factors.** With the plus convention:

   b′₁⊗b′₂ = (b₁ + χU₁)⊗(b₂ + χU₂) = b₁⊗b₂ + χ(b₁⊗U₂ + U₁⊗b₂ + χU₁⊗U₂) = b₁⊗b₂ + χU. ✓

2. **The cocycle law.** If U″ is the change for U″ᵢ = Uᵢ + U′ᵢ, computed from b, and U′ is the change computed from b′ (b′ᵢ = bᵢ + χUᵢ), then U + U′ = U″ exactly. Using the minus convention inside U′ instead leaves the residual −2χ(U₁⊗U′₂ + U′₁⊗U₂). Note B11 finds the same.
   - His formula for U carries +χU₁⊗U₂. With that formula the plus convention is the consistent one, and it is the one he finishes with on 132.
   - A minus convention used throughout would need U = b₁⊗U₂ + U₁⊗b₂ − χU₁⊗U₂.
   - Only the mixing breaks the law.

3. **The last line of 130.** With π_p(η, ζ) = ζ + (b₁⊗b₂)(η) and item 1, π_{p′} = π_p + χU(η). The ink's "+ U(η)" lacks the χ, unless an unstated normalization of U is meant. Note B09 agrees.

4. **The condition "2 − χ = 1" on 140.**
   - The restriction of f₁*f₂ is λ₁π₁⊗f₂ + f₁⊗λ₂π₂ − χ f₁⊗f₂ (lead #41).
   - On u₁⊗u₂, with πᵢ(uᵢ) = χuᵢ (forced by 136) and fᵢ(uᵢ) = λᵢuᵢ, it gives (2χ − χ)λ₁λ₂ u₁⊗u₂ = χλ₁λ₂ u₁⊗u₂ = λ₁λ₂ (u₁*u₂). There is no condition on χ.
   - Taking πᵢ(uᵢ) = uᵢ and comparing with λ₁λ₂ u₁⊗u₂ gives his "(2 − χ) = 1".
   - His own later sheet (152, C E152.1) cancels "2χ = χ" and writes "χ = χ". So he found this himself, and B19 agrees.

5. **The "signe étrange" on 136.** The Uᵢ are maps on the quotients Mᵢ; the uᵢ are vectors in the submodules Lᵢ (B15).
   - **The notes' explanation (B13):** on 134 he attributes the sign to −id in the extension and dual-extension diagram, via φ(x, y) = −xψ(y) + yψ(x).
   - **My inference, not checked:** on 130 a change p′ᵢ = pᵢ − Uᵢ gives b′ᵢ = bᵢ + χUᵢ. So passing from splittings p to trivialisations b carries a factor −χ, and that is where such signs enter.
   - **Status:** a full reconciliation is sweep-3 work.

## What depends on what

- **SA02-4 is used by:**
  - SA02-9, the χ-groupoid with multiplication without division;
  - SA01-36 (K84-10, scans 146-160): the map Hom(M,L)⊗Hom(M′,L′) → Hom(M⊗M′, L⊗L′) and the question −χ(1 − δχ) ≟ χ on 156. The Work notes check its coefficients at χ = 2, δ = 1 (M156a).
- **SA02-4 uses** the pushout description of E₁*E₂ (101; SA02-1).
- **At χ = 2 it specializes to** the product of quadratic algebras (SA02-1, = H01I), whose identity was checked in sweep 1.

## What agrees and what conflicts

- **Agreement:** the ink and the frozen transcription agree on every line I viewed. The Pro notes B09-B19 and the leads describe these readings correctly, and the second audit (#49) settles the Hom exponents on 134 and 136.
- **Conflicts within his pages:**
  - the two conventions on 132;
  - the missing χ on 130;
  - "2 − χ = 1" on 140, which he corrected on 152.

## Corrections

For the commentary; the transcription stays as the ink is.
- Use the plus convention b′ᵢ = bᵢ + χUᵢ throughout. Then b′₁⊗b′₂ = b₁⊗b₂ + χU and U″ = U + U′.
- 84/130, last line: π_{p′} = π_p + χU(η).
- 84/132, middle expansion: (b₁ + χU₁)⊗(b₂ + χU₂).
- 84/140: no condition on χ. The scalar check is χλ₁λ₂ u₁⊗u₂ = λ₁λ₂ u₁*u₂, as he himself has it on 152.
- 84/136: the sign stands as his convention for maps on the quotients, flagged by him and explained by −id (B13). Its place in one convention for the whole product is open.

## Check events

Recorded in `sweep2/SA02/CHECK_EVENTS.tsv`:
- four readings checked on the scan images (130, 132, 136, 140);
- three computations by hand: items 1, 2 and 4 above.
